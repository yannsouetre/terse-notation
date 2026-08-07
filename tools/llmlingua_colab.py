# ==============================================================================
# TERSE Bench — LLMLingua-2 corpus generator (Google Colab)
# ==============================================================================
# WHAT IT DOES
#   From corpus-EN.json / corpus-FR.json, produces:
#     corpus-LLML-{lang}.json        prose compressed by LLMLingua-2, per-document
#                                    rate MATCHED to that document's TERSE ratio
#                                    (fair fight: equal token budget)
#     corpus-LLMLxTERSE-{lang}.json  the TERSE version further compressed by
#                                    LLMLingua-2 (exploratory combo)
#   Both keep the original "prose" and "questions" untouched, so each output file
#   loads directly in TERSE Bench v0.11: the compressed texts go in the "llml" and
#   "llmlx" fields of the flat corpus schema, which the bench exposes as their own
#   run-matrix columns (LLML, LLML+TERSE) alongside prose / short / terse.
#   An integrity report flags any document where negation words or numbers
#   disappeared during compression (LLMLingua has no semantic guarantees).
#
# HOW TO RUN (10 minutes)
#   1. Open colab.research.google.com -> New notebook.
#   2. Runtime -> Change runtime type -> GPU (T4) if available; CPU works, slower.
#   3. Paste this whole file into one cell.
#   4. Left sidebar -> Files -> upload corpus-EN.json and/or corpus-FR.json.
#   5. Run the cell. Download the corpus-LLML-*.json files it creates.
# ==============================================================================

import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "llmlingua"])

import json, re, os
from llmlingua import PromptCompressor

# LLMLingua-2, multilingual (works for French), token-classification based
compressor = PromptCompressor(
    model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",
    use_llmlingua2=True,
)

NEG = ["not ", "n't", " no ", "never", "except", "without",
       " ne ", " pas ", "aucun", "aucune", "jamais", "sauf", "sans "]

def integrity(src, out):
    """Report negation words and numbers present in src but absent from out."""
    lost_neg = [n for n in NEG if n in (" " + src.lower() + " ") and n not in (" " + out.lower() + " ")]
    src_nums = set(re.findall(r"\d+(?:[.,]\d+)?", re.sub(r"(\d)[\s\u202f\u00a0](\d)", r"\1\2", src)))
    out_norm = re.sub(r"(\d)[\s\u202f\u00a0](\d)", r"\1\2", out)
    lost_num = [n for n in src_nums if n not in out_norm]
    return lost_neg, lost_num

def compress(text, rate):
    res = compressor.compress_prompt(text, rate=max(0.2, min(0.95, rate)),
                                     force_tokens=["!", "?", ".", "\n"])
    return res["compressed_prompt"]

for lang in ["EN", "FR"]:
    src_path = f"corpus-{lang}.json"
    if not os.path.exists(src_path):
        print(f"[skip] {src_path} not uploaded")
        continue
    corpus = json.load(open(src_path, encoding="utf-8"))
    llml, combo = {"docs": []}, {"docs": []}
    print(f"\n=== {lang}: {len(corpus['docs'])} docs ===")
    for d in corpus["docs"]:
        ratio = len(d["terse"]) / len(d["prose"])   # matched budget per document
        c_prose = compress(d["prose"], ratio)
        c_terse = compress(d["terse"], 0.75)         # gentle extra pass on TERSE
        for name, out in [("LLML", c_prose), ("LLMLxTERSE", c_terse)]:
            ln, lnum = integrity(d["prose"], out)
            flag = f"  !! REVIEW {d['id']} [{name}]: lost negations {ln} / numbers {lnum[:6]}" \
                   if (ln or len(lnum) > 3) else ""
            if flag: print(flag)
        llml["docs"].append({**d, "llml": c_prose})
        combo["docs"].append({**d, "llmlx": c_terse})
        print(f"  {d['id']}: target ratio {round(ratio*100)}% -> LLML {round(len(c_prose)/len(d['prose'])*100)}% | combo {round(len(c_terse)/len(d['prose'])*100)}% of prose")
    json.dump(llml,  open(f"corpus-LLML-{lang}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(combo, open(f"corpus-LLMLxTERSE-{lang}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"  -> corpus-LLML-{lang}.json and corpus-LLMLxTERSE-{lang}.json written")

print("\nDone. Download the files from the sidebar, load each in TERSE Bench,")
print("run the LLML and LLML+TERSE columns with questions = all. Any '!! REVIEW' line above means the")
print("compressor dropped negations or numbers there - inspect before trusting")
print("that document's accuracy numbers.")
