#!/usr/bin/env python3
"""Classify the `mpf(Q_50_DIGIT_STR)` input-ceiling sites: DELIBERATE vs FIXABLE.

WHY THIS EXISTS
    `Q_50_DIGIT_STR` carries 50 significant digits while `OUTPUT_DPS` is 60, so
    a producer that builds `q` from the STRING publishes ten digits nothing
    supplies. Measured against an independent `q_at(110)` solve:

        mpf(Q_50_DIGIT_STR)  ->  1.91571e-50   from the solve
        Q_MP                 ->  6.97057e-72   from the solve

    i.e. substituting `Q_MP` is strictly more correct by a factor 2.75e21.
    `Q_MP = q_at(_DPS_DEFAULT)` with `_DPS_DEFAULT = 70` since 14a9e822427.

    `Q_50_DIGIT_STR` itself must NOT be changed: its name is its specification
    and 1216 files import it. The fix is at the CONSUMER.

WHY A BLIND SWEEP IS WRONG, AND THIS IS THE POINT OF THE SCRIPT
    206 of the 803 real call sites want 50 digits DELIBERATELY -- 159 of them
    emit an artifact whose own NAME says `50dps`, so changing their `q` to 70
    digits would make that name a lie. A `sed` over the pattern breaks them
    silently. Run this first and skip what it marks deliberate.

TWO FALSE-POSITIVE CLASSES ALREADY REMOVED
    * PROSE. A first version counted raw text and flagged its own sibling audit
      scripts, whose DOCSTRINGS contain the literal `mpf(Q_50_DIGIT_STR)`. Six
      files mention it and never call it. `_source_normalise.code_only()` --
      which this corpus already ships for exactly this, and whose header notes
      that a bare-token pattern needs it while an anchored assignment-shaped
      one does not -- blanks comments and docstrings in place.
    * The 50-digit pin being read from the call alone. The deliberate signal is
      in the file's NAME, its emitted artifact names, or a pin comment on the
      line -- never in the call, which is identical in both cases.

WHAT THIS SCRIPT DOES NOT ESTABLISH
    Whether a fixable site's witness actually MOVES. That needs a producer
    re-run with a CONTROL ARM IN THE SAME ENVIRONMENT: comparing a patched run
    against the committed witness attributes environment churn to the patch
    (measured -- installing `pyhecke_native` strengthens the recorded
    environment block and shows up as movement, including on a file that never
    calls the pattern at all). Open; see the audit doc.
"""
import re, subprocess, sys
from pathlib import Path
sys.path.insert(0, "/home/user/qou/computations/audits")
sys.path.insert(0, "/home/user/qou/computations")
from _source_normalise import code_only

ROOT = Path("/home/user/qou")
CALL   = re.compile(r"(?:mpmath\.)?mpf\s*\(\s*Q_50_DIGIT_STR\s*\)")
NAME50 = re.compile(r"50dps|50_dps|50-dps|_50\b", re.I)
TEXT50 = re.compile(r"50\s*-?\s*(?:dps|dig|decimal|sig)|(?:dps|digits?)\s*=?\s*50", re.I)
PINWORD= re.compile(r"\b(pin(?:ned)?|deliberat\w*|exactly|canonical|must\s+(?:stay|remain)|do\s+not\s+change)\b", re.I)

def ls(p): return subprocess.run(["git","-C",str(ROOT),"ls-files",p],capture_output=True,text=True).stdout.split()
pys=[p for p in ls("computations/") if p.endswith(".py") and "_deprecated" not in p and "__pycache__" not in p]

prose_only=[]; deliberate=[]; fixable=[]; unpatchable=[]
for p in pys:
    try: raw=(ROOT/p).read_text(errors="replace")
    except OSError: continue
    if not CALL.search(raw): continue
    try: code = code_only(raw)
    except Exception: code = raw
    if not CALL.search(code):
        prose_only.append(p); continue                 # mentions it, does not call it
    why=[]
    if NAME50.search(Path(p).name): why.append("filename-says-50")
    if re.search(r"50dps|50-dps", raw, re.I): why.append("emits-a-50dps-artifact")
    for line in raw.splitlines():
        if "Q_50_DIGIT_STR" in line and PINWORD.search(line) and TEXT50.search(line):
            why.append("pin-comment-on-the-line"); break
    if why: deliberate.append((p,"+".join(sorted(set(why))))); continue
    if re.search(r"^\s*(?:from\s+\S+\s+import\s+|import\s+)[^\n#]*\bQ_MP\b", code, re.M):
        fixable.append((p,"Q_MP already imported")); continue
    if re.search(r"^\s*from\s+\S+\s+import\s+[^\n#]*\bQ_50_DIGIT_STR\b", code, re.M):
        fixable.append((p,"extend the existing import")); continue
    unpatchable.append((p,"no import to extend"))

tot=len(prose_only)+len(deliberate)+len(fixable)+len(unpatchable)
print(f"files whose RAW TEXT contains mpf(Q_50_DIGIT_STR) : {tot}")
print(f"  PROSE ONLY -- mentions it, never calls it       : {len(prose_only)}")
print(f"  real call sites                                 : {tot-len(prose_only)}")
print(f"    DELIBERATE 50-digit pin (must NOT change)     : {len(deliberate)}")
print(f"    FIXABLE                                       : {len(fixable)}")
print(f"    UNPATCHABLE (no import to extend)             : {len(unpatchable)}")
print()
from collections import Counter
print("why deliberate:", dict(Counter(w for _,w in deliberate)))
print()
print("prose-only sample:"); [print("   ",p) for p in prose_only[:6]]
if "--emit" in sys.argv:
    out = Path(sys.argv[sys.argv.index("--emit") + 1])
    out.mkdir(parents=True, exist_ok=True)
    (out / "fixable.txt").write_text("\n".join(p for p, _ in fixable) + "\n")
    (out / "deliberate.txt").write_text(
        "\n".join(f"{p}\t{w}" for p, w in deliberate) + "\n")
    (out / "unpatchable.txt").write_text("\n".join(p for p, _ in unpatchable) + "\n")
    print()
    print(f"wrote fixable.txt / deliberate.txt / unpatchable.txt to {out}")
else:
    print()
    print("pass `--emit <dir>` to write the three lists")
