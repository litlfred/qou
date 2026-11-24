#!/usr/bin/env python3
"""qou-oiz3 option 1 (v2) -- exposed-witness identification. READ-ONLY.

v1 over-matched 6x (1519 candidates vs the audit's measured ~243) because its
one-hop rule flagged any producer importing `q_parameter`, which DEFINES q_int.
That measured exposure to the MODULE, not to the FIX. v2 keeps direct CALLS only
and splits the surface by which landed/pending fix it belongs to:

  A  calls q_hook_product / wedderburn_weight / q_factorial / q_dimension
  B  calls q_int(                     -- A and B are OPTION 4's population
  C  calls mpf(Q_50_DIGIT_STR)        -- OPTION 3's population (input ceiling)

Gate: the witness must publish >50 significant digits, else a refresh is a
no-op diff whatever the producer does.

Calibration is ASSERTED, not assumed: the run FAILS if a known answer misses.
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path("/home/user/qou")
A_FUNCS = ("q_hook_product", "wedderburn_weight", "q_factorial", "q_dimension")
CALL_A = re.compile(r"\b(?:" + "|".join(A_FUNCS) + r")\s*\(")
CALL_B = re.compile(r"\bq_int\s*\(")
# C is the INPUT CEILING: a consumer that builds q from the 50-digit STRING
# caps itself at 50 significant digits while OUTPUT_DPS is 60, so digits 51-60
# of anything it serializes carry no information.
#
# This was originally `\b[A-Z][A-Z0-9_]*_MP\b`, which measured the WRONG THING:
# the *_MP family is derived from `Q_MP = q_at(_DPS_DEFAULT)` with
# `_DPS_DEFAULT = 70` (commit 14a9e822427), so referencing an _MP constant is
# not a ceiling -- it is already the full-precision path. The _MP regex also
# could not match `Q_50_DIGIT_STR`, which does not end in `_MP`, so the real
# channel was invisible to it. Found by running this audit, not by reading it.
REF_C  = re.compile(r"(?:mpmath\.)?mpf\s*\(\s*Q_50_DIGIT_STR")
REF_A  = re.compile(r"\b(?:" + "|".join(A_FUNCS) + r")\b")
FINE   = re.compile(r"-?\d+\.\d{45,}|-?0?\.\d{50,}")

def ls(pat):
    return subprocess.run(["git", "-C", str(ROOT), "ls-files", pat],
                          capture_output=True, text=True).stdout.split()

# SCOPE, stated because it is checkable: root `computations/` plus the two
# packages the fixes live in. There is a SECOND computations tree at
# `folio/quantum-observable-universe/computations/`, measured 2026-11-20 at
# 2 .py files and 2 witnesses -- a known, bounded gap, not a tree.
allfiles = ls("computations/") + ls("tools/qou-substrate/") + ls("tools/pyhecke/")
SELF = "computations/audits/exposed_witness_identification.py"
# Exclude THIS FILE. It names every family-A function in its own A_FUNCS tuple,
# so without this it classifies itself as a producer on the fixed surface and
# the derived calibration reads 96 instead of 95. An auditor is not a producer.
# Caught by the calibration assertion the moment the file became tracked.
pys = [p for p in allfiles if p.endswith(".py")
       and "_deprecated" not in p and "__pycache__" not in p and p != SELF]
src = {}
for p in pys:
    try: src[p] = (ROOT / p).read_text(errors="replace")
    except OSError: pass

famA = {p for p, t in src.items() if CALL_A.search(t)}
famB = {p for p, t in src.items() if CALL_B.search(t)}
famC = {p for p, t in src.items() if REF_C.search(t)}
refA = {p for p, t in src.items() if REF_A.search(t)}
opt4 = famA | famB
exposed = opt4 | famC

# ---- CALIBRATION: fail loudly, never self-certify -------------------------
fails = []
wed = [p for p in src if p.endswith("pyhecke/wedderburn.py")]
if not wed:
    fails.append("wedderburn.py not in scanned set at all")
elif wed[0] not in famA:
    fails.append(f"{wed[0]} must be family A (it defines+calls the trio)")
# DERIVED calibration: my scope == live referencing files minus the trees I
# deliberately exclude (qou-mass generated mirror, tools/sage-examples).
# DERIVED calibration, not a guessed band. The audit's "124 files reference the
# trio" is a WHOLE-REPO count. Split by tree it is 132 = 23 fsh-guts/deprecated
# + 10 docs/audits (prose) + 99 live code (90 computations, 6 tools, 3 qou-mass).
# This scan excludes the qou-mass generated mirror (3) and tools/sage-examples
# (1), so it must read exactly 99 - 4 = 95. If it does not, the scan scope has
# drifted and every count below is about the harness.
EXPECT_REF_A = 95
if len(refA) != EXPECT_REF_A:
    fails.append(f"family-A reference count {len(refA)} != derived {EXPECT_REF_A} "
                 f"-- scan scope drifted; re-derive the tree split before trusting counts")
if fails:
    print("CALIBRATION FAILED -- verdicts below would be about the harness:")
    for f in fails: print("  !", f)
    sys.exit(2)
print(f"calibration OK: wedderburn.py in family A; refA={len(refA)} "
      f"== derived {EXPECT_REF_A} (the audit's 124 is a WHOLE-REPO count; see above)")
print()

wits = [p for p in ls("computations/") if p.endswith(".witness.json")]

def producer(d):
    v = d.get("scriptFile")
    if isinstance(v, str) and v: return v
    w = d.get("witness")
    if isinstance(w, dict):
        v = w.get("scriptFile")
        if isinstance(v, str) and v: return v
    return None

bybase = {}
for p in src: bybase.setdefault(Path(p).name, p)

rows = {k: [] for k in ("opt4_fine", "opt4_coarse", "optC_only_fine",
                        "not_exposed", "no_producer", "unresolved")}
for wp in wits:
    try:
        raw = (ROOT / wp).read_text(errors="replace"); d = json.loads(raw)
    except Exception:
        continue
    sf = producer(d)
    if not sf: rows["no_producer"].append(wp); continue
    pp = bybase.get(Path(sf).name)
    if pp is None: rows["unresolved"].append((wp, sf)); continue
    fine = bool(FINE.search(raw))
    if pp in opt4:
        rows["opt4_fine" if fine else "opt4_coarse"].append((wp, pp))
    elif pp in famC:
        if fine: rows["optC_only_fine"].append((wp, pp))
        else: rows["not_exposed"].append(wp)
    else:
        rows["not_exposed"].append(wp)

print("=" * 70)
print("PRODUCERS (direct calls only; _deprecated and __pycache__ excluded)")
print("=" * 70)
print(f"  scanned .py                              : {len(src)}")
print(f"  A  call the wedderburn trio / q_dimension: {len(famA)}")
print(f"  B  call q_int(                           : {len(famB)}")
print(f"  A u B  = OPTION 4 surface                : {len(opt4)}")
print(f"  C  cap q via mpf(Q_50_DIGIT_STR)         : {len(famC)}")
print(f"  A u B u C                                : {len(exposed)}")
print()
print("=" * 70)
print(f"WITNESSES  (tracked total {len(wits)})")
print("=" * 70)
print(f"  no producer recorded                     : {len(rows['no_producer'])}")
print(f"  producer recorded but not tracked        : {len(rows['unresolved'])}")
print(f"  producer not on any exposed surface      : {len(rows['not_exposed'])}")
print(f"  OPTION 4 surface, >50 sig digits         : {len(rows['opt4_fine'])}   <-- refresh candidates")
print(f"  OPTION 4 surface, coarse (refresh = noop): {len(rows['opt4_coarse'])}")
print(f"  OPTION 3 (50-digit cap) only, >50 digits : {len(rows['optC_only_fine'])}")
print()
print(f"distinct producers behind the option-4 candidates: "
      f"{len({p for _, p in rows['opt4_fine']})}")
print()
print("option-4 refresh candidates (first 20):")
for wp, pp in sorted(rows["opt4_fine"])[:20]:
    print(f"   {wp}")
