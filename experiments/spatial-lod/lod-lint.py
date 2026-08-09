#!/usr/bin/env python3
"""LOD linter prototype — R2 (constraint elevation) & R3 (map completeness, references).
Deterministic, zero-LLM. v0.2: hierarchical sub-addresses (&tNN/slug) supported. See TERSE-SPATIAL-DRAFT sections 4 and 7 (P3).
The self-test below is the measurement — run it, don't quote it. injected corruptions detected across five
corruption types (orphan detail, dangling map entry, de-elevated !!, phantom !!,
dangling reference), 0 false alarms on the clean 23-document corpus."""
import re

def lint(map_text, l1_blocks):
    """map_text: the L0 MAP (one '&tNN ...' line per doc).
    l1_blocks: dict addr -> L1 text. Returns list of (rule, addr) violations."""
    viol = []; m_addrs = {}
    for line in map_text.split("\n"):
        mm = re.match(r"&(t\d{2}(?:/[a-z0-9-]+)*)\b", line.strip())
        if mm: m_addrs[mm.group(1)] = line
    for a in l1_blocks:
        if a not in m_addrs: viol.append(("R3a-orphan-detail", a))
    for a in m_addrs:
        if a not in l1_blocks: viol.append(("R3b-dangling-map", a))
    for a, txt in l1_blocks.items():
        for ref in re.findall(r"\*(t\d{2}(?:/[a-z0-9-]+)*)\b", txt):
            if ref not in m_addrs: viol.append(("R3c-dangling-ref", a + "->" + ref))
        has_hard = any(l.strip().startswith("!!") for l in txt.split("\n"))
        map_hard = a in m_addrs and re.match(r"&\S+\s+!!", m_addrs[a].strip()) is not None
        if has_hard and not map_hard: viol.append(("R2-unelevated", a))
        if map_hard and not has_hard: viol.append(("R2-phantom", a))
    return viol

def r1_values(l1_text, l2_text, title=""):
    """R1 (refinement, value layer): every quoted value in L1 must appear verbatim in the
    fine-detail layer. Semantics decided 2026-08-09: the document header (title) travels with
    every level, so the haystack is title + L2 body (a value inherited from the title is
    faithful, not drifted). Returns missing values."""
    import unicodedata as _u
    def _n(s): return re.sub(r"\s+"," ", _u.normalize("NFKC", s)).lower()
    l2n=_n((title + chr(10) if title else "") + l2_text)
    return [v for v in set(re.findall(r'"([^"\n]{1,40})"', l1_text)) if _n(v) not in l2n]

def r4_occlusion(text):
    """R4 (occlusion honesty): any 'x ... superseded' line must carry a forward pointer -> *addr."""
    return [l.strip()[:60] for l in text.split("\n")
            if re.search(r"^\s*x\b.*supersed", l, re.I) and not re.search(r"->\s*\*t\d{2}", l)]

SELF_TEST_MARK=True


def self_test(corpus_path="LOD-CORPUS-EN.json", n=8, seed=1):
    """Injection self-test for all rules. For each corruption type, start from the clean
    corpus, inject one isolated corruption, check the expected rule fires. Prints a table."""
    import json, random
    random.seed(seed)
    d=json.load(open(corpus_path,encoding="utf-8")); MAP=d["map"]; docs=d["docs"]
    l1={a:v["l1"] for a,v in docs.items()}
    base=len(lint(MAP,l1))
    print(f"clean corpus: {base} violation(s) (false alarms)")
    kinds={
     "orphan-detail (drop map line)":("R3a", lambda a,m,l:("\n".join(x for x in m.split("\n") if not x.strip().startswith(f"&{a} ")), l)),
     "dangling-map (drop L1 block)":("R3b", lambda a,m,l:(m, {k:v for k,v in l.items() if k!=a})),
     "de-elevated !! (strip map flag)":("R2-unelevated", lambda a,m,l:(m.replace(docs[a]["map"], docs[a]["map"].replace("!! ","",1)), l)),
     "phantom !! (strip L1 hards)":("R2-phantom", lambda a,m,l:(m, {**l, a:"\n".join(x for x in l[a].split("\n") if not x.strip().startswith("!!"))})),
     "dangling-ref (*t99)":("R3c", lambda a,m,l:(m, {**l, a:l[a]+"\n-> *t99"})),
    }
    total=det=0
    for name,(rule,inject) in kinds.items():
        ok=0
        for _ in range(n):
            a=__import__("random").choice(list(docs))
            m2,l2=inject(a,MAP,dict(l1))
            v=lint(m2,l2); total+=1
            hit=any(rule in r for r,_ in v); det+=hit; ok+=hit
        print(f"  {name:38s} expected {rule:14s} {ok}/{n}")
    # R1 et R4 (fonctions dédiées)
    ok=0
    for _ in range(n):
        a=__import__("random").choice([k for k in docs if re.search(r'"[^"\n]+"', docs[k]["l1"])])
        vals=re.findall(r'"([^"\n]{1,40})"', docs[a]["l1"])
        c=docs[a]["l1"].replace(f'"{vals[0]}"','"999-CORRUPT"',1)
        hit=bool(r1_values(c, docs[a]["l2"], docs[a].get("title",""))); total+=1; det+=hit; ok+=hit
    print(f"  {'R1 value corruption':38s} expected {'r1_values':14s} {ok}/{n}")
    ok=0
    for _ in range(n):
        a=__import__("random").choice(list(docs))
        hit=bool(r4_occlusion(docs[a]["l1"]+"\nx old rule superseded")); total+=1; det+=hit; ok+=hit
    print(f"  {'R4 missing supersession pointer':38s} expected {'r4_occlusion':14s} {ok}/{n}")
    r1_clean=sum(1 for a in docs if r1_values(docs[a]["l1"], docs[a]["l2"], docs[a].get("title","")))
    r4_clean=sum(1 for a in docs if r4_occlusion(docs[a]["l1"]))
    r4_ok=sum(1 for a in docs if not r4_occlusion(docs[a]["l1"] + chr(10) + "x old rule superseded -> *t01"))
    print("clean corpus, R1: " + str(r1_clean) + " . R4: " + str(r4_clean) + " . R4 counter-test (well-formed, must not fire): " + str(r4_ok) + "/" + str(len(docs)) + " pass")
    print("TOTAL: " + str(det) + "/" + str(total) + " detected . false alarms on clean corpus (all rules): " + str(base + r1_clean + r4_clean))
    print("note: R4 evidence is a regex self-check, not field evidence - the corpus contains no real supersessions yet.")
    return det, total, base + r1_clean + r4_clean

if __name__ == "__main__":
    import sys
    if "--self-test" in sys.argv:
        args=[a for a in sys.argv[1:] if a!="--self-test"]
        self_test(args[0] if args else "LOD-CORPUS-EN.json"); raise SystemExit
    import json, sys
    d = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "LOD-CORPUS-EN.json", encoding="utf-8"))
    v = lint(d["map"], {a: x["l1"] for a, x in d["docs"].items()})
    print(f"{len(v)} violation(s)"); [print(" ", r, a) for r, a in v]
