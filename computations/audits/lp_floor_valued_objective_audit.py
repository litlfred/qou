#!/usr/bin/env python3
"""Which LP/SDP witnesses publish an objective that is the ARITHMETIC FLOOR?

MOTIVATION (bean `qou-sof3`). `qbeta-symbolic-sdp-strict-complementarity`
publishes `primal_obj = 3.9236...e-44` to 50 digits. Re-running the producer at
higher working precision gives 3.8e-100 at `prec_bits=400` and 3.8e-196 at 800:
the objective TRACKS THE WORKING PRECISION, which is the signature of a true
value of zero reported at whatever the arithmetic floor happens to be. Every
published digit of it is noise. Its `duality_gap ~ 0` assertion was therefore
vacuous -- it compared two floor values against a tolerance 38 orders larger.

THE CRITERION. A sum of terms of magnitude `max|x*|` computed at `p` bits
resolves to about `max|x*| * 10^(-p*log10 2)`. So if the objective is far below
that, it is not a number the arithmetic could have produced:

    cancellation_decades = log10(max|x*|) - log10(|primal_obj|)
    available_decades    = prec_bits * log10(2)          # 50.27 at p=167
    FLAG when cancellation_decades > FRACTION * available_decades

🛑 MEASURED RESULT: THIS CRITERION DOES NOT DECIDE. It is kept as a RANKING
   and as the record of a negative, not as a detector. Two measurements, both
   from the run that introduced it:

   1. THE THRESHOLD IS A CLIFF, so any flag count is an artifact of where it
      is set, not a property of the corpus:

          fraction   0.80  0.90  0.95  0.96  0.98  1.00  1.05
          flagged      74    62    62    62     7     7     3

      55 records sit in a narrow band at ratio ~0.97. Do NOT quote "62".

   2. IT MISSES THE ONE KNOWN POSITIVE. `qbeta-symbolic-sdp-strict-
      complementarity` was PROVED floor-valued by sweeping `prec_bits`
      (3.9e-44 at 167 -> 3.8e-100 at 400 -> 3.8e-196 at 800; bean qou-sof3).
      It scores ratio 0.97 -- inside the cluster, and BELOW the only
      threshold-free setting (ratio > 1, meaning the objective is beneath
      what the arithmetic can resolve at all). A criterion that cannot rank
      its own confirmed positive above 55 unknowns is not separating them.

   The reason is structural: a legitimately tiny optimum and a floor-valued
   one look identical in the published numbers. The ONLY discriminator is
   whether the objective MOVES when `prec_bits` changes, which needs the
   producer re-run -- deliberately not done here, since re-running producers
   rewrites sibling witnesses (AGENTS.md).

   So: use the ranking to CHOOSE which producer to sweep. Never report a flag
   as a defect. The corpus keeps a 26-row detector-blindness taxonomy
   precisely because detectors get quoted as measurements.

NO FLOAT64: all arithmetic is mpmath. `float()` appears only in f-strings.

Usage:  python3 computations/audits/lp_floor_valued_objective_audit.py [--fraction 0.9]
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from mpmath import mp

mp.dps = 60

_ROOT = Path(__file__).resolve().parents[2]
LP_KEYS = {"y0_star", "y_star", "primal_obj", "dual_obj", "duality_gap"}
LOG10_2 = mp.log10(2)


def _tracked_witnesses() -> list[Path]:
    out = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "HEAD", "computations/"],
        capture_output=True, text=True, cwd=_ROOT,
    ).stdout.split("\n")
    return [_ROOT / f for f in out if f.endswith(".witness.json")]


def _records(obj, path="<root>"):
    """Yield (path, dict) for every LP/SDP dual record found anywhere."""
    if isinstance(obj, dict):
        if LP_KEYS <= set(obj):
            yield path, obj
        for k, v in obj.items():
            yield from _records(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _records(v, f"{path}[{i}]")


def _mpf(v):
    try:
        m = mp.mpf(str(v))
        return m if mp.isfinite(m) else None
    except (ValueError, TypeError):
        return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fraction", type=float, default=1.0,
                    help="flag when cancellation exceeds this fraction of the "
                         "available precision (default 1.0 -- the only "
                         "threshold-free setting; see module docstring)")
    args = ap.parse_args()
    frac = mp.mpf(str(args.fraction))

    flagged, clean, unscorable = [], [], []
    for w in _tracked_witnesses():
        try:
            doc = json.loads(w.read_text())
        except Exception:
            continue
        for rpath, rec in _records(doc):
            xs = rec.get("x_star_str") or rec.get("x_star")
            po = rec.get("primal_obj_str") or rec.get("primal_obj")
            name = f"{w.relative_to(_ROOT)}{rpath[6:]}"
            if not isinstance(xs, list) or not xs or po is None:
                unscorable.append((name, "no x_star / primal_obj"))
                continue
            xv = [_mpf(v) for v in xs]
            pv = _mpf(po)
            if pv is None or any(v is None for v in xv):
                unscorable.append((name, "non-finite"))
                continue
            mx = max(mp.fabs(v) for v in xv)
            if mx == 0 or pv == 0:
                unscorable.append((name, "max|x*| or primal_obj is exactly 0"))
                continue
            cancel = mp.log10(mx) - mp.log10(mp.fabs(pv))
            bits = rec.get("precision_bits")
            avail = mp.mpf(str(bits)) * LOG10_2 if bits else mp.mpf(53) * LOG10_2
            row = (name, cancel, avail, bits, mx, pv)
            (flagged if cancel > frac * avail else clean).append(row)

    flagged.sort(key=lambda r: -(r[1] / r[2]))
    total = len(flagged) + len(clean)
    print(f"LP/SDP dual records scored : {total}")
    print(f"  FLAGGED (candidates)     : {len(flagged)}")
    print(f"  not flagged              : {len(clean)}")
    print(f"  unscorable               : {len(unscorable)}")
    print(f"  criterion                : cancellation > {args.fraction} x "
          f"available decades\n")

    if flagged:
        print(f"{'ratio':>6}  {'cancel':>7}  {'avail':>6}  {'bits':>5}  record")
        print("-" * 100)
        for name, cancel, avail, bits, mx, pv in flagged:
            print(f"{float(cancel/avail):6.2f}  {float(cancel):7.1f}  "
                  f"{float(avail):6.1f}  {str(bits or '-'):>5}  {name[:70]}")

    # Sensitivity is printed EVERY run, so a reader cannot take one count as
    # a measurement without seeing how much it moves with the threshold.
    print("\n  threshold sensitivity (same data, varying --fraction):")
    scored = flagged + clean
    for f in ("0.80", "0.90", "0.95", "0.96", "0.98", "1.00", "1.05"):
        fm = mp.mpf(f)
        n = sum(1 for _n, c, a, *_ in scored if c > fm * a)
        mark = "  <- default" if f == f"{args.fraction:.2f}" else ""
        print(f"      fraction {f} -> {n:>4} flagged{mark}")
    print("  A cliff between two adjacent rows means the count is an artifact")
    print("  of the threshold. Measured on this corpus: 62 at 0.96, 7 at 0.98.")

    # Where does the ONE confirmed positive rank? If it is not near the top,
    # the ranking is not doing its job -- say so rather than let a reader
    # assume it is.
    KNOWN = "qbeta-symbolic-sdp-strict-complementarity"
    hit = [(i, r) for i, r in enumerate(sorted(scored, key=lambda r: -(r[1]/r[2])))
           if KNOWN in r[0]]
    print()
    if hit:
        i, r = hit[0]
        print(f"  CALIBRATION -- the one producer PROVED floor-valued by a")
        print(f"  prec_bits sweep (qou-sof3) ranks {i + 1} of {len(scored)} "
              f"at ratio {float(r[1]/r[2]):.2f}.")
        print(f"  It is NOT in the threshold-free set. Treat the ranking as a")
        print(f"  hint about where to spend a sweep, never as a verdict.")
    else:
        print("  CALIBRATION: the known positive was not scored -- the ranking")
        print("  is uncalibrated in this run; do not act on it.")

    print("\n  ratio > 1 means the objective is BELOW what the arithmetic can")
    print("  resolve -- it cannot be a computed value. ratio near the")
    print("  threshold is where legitimate small optima live; those are the")
    print("  likely false positives and are NOT evidence of anything on their")
    print("  own. Confirm by re-running the producer at a higher prec_bits:")
    print("  a floor-valued objective MOVES, a real one does not.")
    if unscorable:
        print(f"\n  {len(unscorable)} unscorable (first 5):")
        for name, why in unscorable[:5]:
            print(f"    {why:36s} {name[:60]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
