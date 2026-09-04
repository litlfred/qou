#!/usr/bin/env python3
"""Infer an LP/SDP dual record's SOLVER BACKEND from its numbers.

WHY. `lp_dual_solver` records `backend` and `precision_bits` on every result it
produces today, but 105 committed dual records predate that field, so nothing
in the file says whether they were solved in float64 or at ~50 dps -- a
difference measured at 28 orders of magnitude in the residual (bean `qou-dke6`,
worked case `borromean-axial-coupling`: 3.81e-16 -> 3.57e-44).

THE IDEA: no producer run is needed. The two backends leave different floors,
and the floor is visible in the published numbers:

    rel = log10( duality_gap / max|x*| )

CALIBRATION, on the records that DO declare a backend -- this is the part that
makes it a measurement rather than a guess:

    declared backend        n      min   median     max
    clarabel-mpfr         117    -53.7    -48.8   -37.9
    (none declared)        14    -55.9    -16.8   -12.8

Every labelled MPFR record sits below -37.9; the undeclared population has a
median of -16.8, which is the float64 epsilon signature. The cut is placed at
-30, inside the empty band between the two, with the -37.9..-30 interval
reported as AMBIGUOUS rather than forced either way.

🛑 AN INFERENCE IS NOT A DECLARATION. A classification here is evidence about
   how a record was probably produced; the fix is still to re-run the producer
   so it records `backend` itself. Do not write an inferred backend into a
   witness.

🛑 AND SOME RECORDS HAVE NO PRIMAL, FOR TWO DIFFERENT REASONS. 44 of 187
   leaf records carry no `x_star`, and lumping them together was a mistake of
   this script's first version. Split on whether the gap is exactly zero:

     29  CLOSED-FORM dual -- no LP was solved, so x* is correctly absent and
         there is nothing to certify. 27 are `sigma_f_electron_shell_chain`,
         confirmed by reading it: it builds the dual from Wedderburn weights
         and writes `"duality_gap": "0"` with the comment "closed-form =>
         exact strong duality". It never calls a solver.
     15  a REAL solve whose primal was dropped at serialization. These are
         the ones invisible to the certified-residual check (`qou-fr4d`), and
         six of the fifteen are one family, `nucleus-real-sdp-*`.

   So the actionable population is 15 records across ~10 producers, not 84.
   That is per-producer work; it is NOT an argument for adding `x_star` to
   the LP-dual required-field list in AGENTS.md. `x_star` is not in the LP-dual required-field list in AGENTS.md
   (that names y0_star / y_star / active_set / primal_obj / dual_obj /
   duality_gap), so this is not a contract violation -- but it does mean both
   this audit AND the certified-residual check from `qou-fr4d` are blind to
   them. That is the real structural gap, and it is larger than the f64
   question.

WHAT IT FOUND, which deflates the bean that prompted it. The live f64-era
exposure is ONE record, `borromean-axial-coupling`, already fixed. There is no
sweep to run. Run the script for the current split; do not quote a figure from
this docstring, which has already been wrong once (it read "84 of the 105"
before the wrapper filter landed, counting 54 hoisted parent dicts as records
in their own right).

NO-FLOAT64: all arithmetic is mpmath; float() only inside f-strings.

    python3 computations/audits/lp_dual_backend_inference_audit.py
"""
from __future__ import annotations

import argparse
import collections
import json
import subprocess
from pathlib import Path

from mpmath import mp

mp.dps = 60
_ROOT = Path(__file__).resolve().parents[2]
LP_KEYS = {"y0_star", "y_star", "primal_obj", "dual_obj", "duality_gap"}
F64_CUT = mp.mpf("-30")      # above this => float64 era
MPFR_EDGE = mp.mpf("-37.9")  # tightest labelled clarabel-mpfr record


def _tracked():
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", "HEAD", "computations/"],
                         capture_output=True, text=True, cwd=_ROOT).stdout.split("\n")
    return [f for f in out if f.endswith(".witness.json")]


def _has_nested_record(o) -> bool:
    """True when a DESCENDANT of `o` (not `o` itself) is also an LP record.

    Such a dict is a WRAPPER, not a solve: producers routinely hoist
    `primal_obj` / `dual_obj` / `duality_gap` / `active_set` / `y0_star` /
    `y_star` onto a parent alongside a nested key holding the real record.
    Counting both double-counts the solve AND -- because the hoisted copy
    omits `x_star` -- manufactures a phantom "record with no primal vector".
    Measured: 54 of the 241 five-key matches are wrappers, and 41 of them are
    `pn-alpha-lp-dual.witness.json`'s `.lp_dual_scan_h3[i]`, whose nested
    `.lp_dual` carries the x* the parent lacks.
    """
    def walk(x, top=False):
        if isinstance(x, dict):
            if not top and LP_KEYS <= set(x):
                return True
            return any(walk(v) for v in x.values())
        if isinstance(x, list):
            return any(walk(v) for v in x)
        return False
    return walk(o, top=True)


def _records(o, p=""):
    """Yield LEAF LP records only -- wrappers are skipped, not counted."""
    if isinstance(o, dict):
        if LP_KEYS <= set(o) and not _has_nested_record(o):
            yield p, o
        for k, v in o.items():
            yield from _records(v, f"{p}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from _records(v, f"{p}[{i}]")


def _mpf(v):
    try:
        x = mp.mpf(str(v))
        return x if mp.isfinite(x) else None
    except (ValueError, TypeError):
        return None


def classify(rec):
    """-> (verdict, rel or None). Verdict is one of: f64-era, mpfr-era,
    ambiguous, or a reason string beginning 'unclassifiable:'."""
    xs = rec.get("x_star_str") or rec.get("x_star")
    g = _mpf(rec.get("duality_gap_str") or rec.get("duality_gap"))
    if not isinstance(xs, list) or not xs:
        # NOT one bucket. A record without a primal vector is either a
        # CLOSED-FORM dual -- no LP was solved, so there is no x* to omit and
        # nothing to certify -- or a real solve whose primal was dropped on
        # serialization. `duality_gap == 0` exactly separates them in practice:
        # a closed form is exact by construction, a solve is not.
        #
        # Verified by reading the source, not inferred: 27 of the 29
        # gap-zero hits are `sigma_f_electron_shell_chain`, which builds
        # y0_star / y_star / active_set directly from Wedderburn weights and
        # sets `"duality_gap": "0"  # closed-form => exact strong duality`.
        # It never calls an LP solver. Its missing x* is CORRECT.
        if g is not None and g == 0:
            return "no primal: closed-form dual (x* correctly absent)", None
        return "no primal: solve with x_star unserialized", None
    if g is None:
        return "unclassifiable: gap not numeric", None
    if g == 0:
        return "unclassifiable: gap exactly 0", None
    xv = [_mpf(v) for v in xs]
    if any(v is None for v in xv):
        return "unclassifiable: x* not numeric", None
    mx = max(mp.fabs(v) for v in xv)
    if mx == 0:
        return "unclassifiable: x* all zero", None
    rel = mp.log10(g / mx)
    if rel > F64_CUT:
        return "f64-era", rel
    if rel < MPFR_EDGE:
        return "mpfr-era", rel
    return "ambiguous", rel


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--include-deprecated", action="store_true",
                    help="also list hits under computations/_deprecated/")
    args = ap.parse_args()

    declared = collections.Counter()
    verdicts = collections.Counter()
    inferred_f64 = []
    calib = collections.defaultdict(list)

    for f in _tracked():
        try:
            doc = json.loads((_ROOT / f).read_text())
        except Exception:
            continue
        for path, rec in _records(doc):
            b = rec.get("backend")
            declared[b or "NO backend field"] += 1
            v, rel = classify(rec)
            if b and rel is not None:
                calib[b].append(rel)
            if b:
                continue
            verdicts[v] += 1
            if v == "f64-era":
                inferred_f64.append((f, path, rel))

    print("LP/SDP dual records by DECLARED backend:")
    for k, n in declared.most_common():
        print(f"   {k:<22} {n:>5}")

    print("\nCALIBRATION -- log10(duality_gap / max|x*|) by declared backend:")
    for b, vals in sorted(calib.items()):
        v = sorted(vals)
        print(f"   {b:<22} n={len(v):<4} min={float(v[0]):7.1f} "
              f"median={float(v[len(v)//2]):7.1f} max={float(v[-1]):7.1f}")
    print(f"   cut at {float(F64_CUT)}; ambiguous band ({float(MPFR_EDGE)}, {float(F64_CUT)})")

    print(f"\nUNDECLARED records ({declared['NO backend field']}), what can be inferred:")
    for k, n in verdicts.most_common():
        print(f"   {k:<34} {n:>5}")

    live = [r for r in inferred_f64 if "_deprecated/" not in r[0]]
    dep = [r for r in inferred_f64 if "_deprecated/" in r[0]]
    print(f"\nINFERRED f64-era: {len(inferred_f64)} "
          f"({len(dep)} deprecated, {len(live)} live)")
    for f, path, rel in live:
        print(f"   LIVE       rel={float(rel):7.1f}  {f}{path}")
    if args.include_deprecated:
        for f, path, rel in dep:
            print(f"   deprecated rel={float(rel):7.1f}  {f}{path}")
    elif dep:
        print(f"   ({len(dep)} under _deprecated/ hidden; --include-deprecated to list)")

    print("\n  An inference is evidence, NOT a declaration. The fix for a")
    print("  live hit is to re-run the producer so it records `backend`")
    print("  itself -- never to write an inferred value into a witness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
