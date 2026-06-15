#!/usr/bin/env python3
"""
Full-census canonical Markov trace via pyhecke for Z ≤ 10.

Extends `canonical_isospin_pyhecke.py` (which only covered the
6-atom base set: p, n, D, T, ³He, ⁴He) to all 23 stable isotopes
in the Z ≤ 10 census used by `low_isotope_mass_table.py`.

The pyhecke entry point `markov_trace_symbolic_eval(Z, N, ...)`
already constructs the atomic braid in H_{3A} from strand types
internally, so this sweep just calls it for each (Z, N) pair.

Per-atom wallclock is ~1–3 ms after the first call (CRT backend
warm).  No new infrastructure needed; this fixes the gap that
forced `low_isotope_mass_table.py` to fall back to non-categorical
strategies (census/α-cluster/partial-shell volumes) for Z ≥ 3.

Output:
  canonical-isospin-pyhecke-full-census.witness.json

Refs:
  - prop:categorical-mass-markov
  - thm:jones-markov-trace
  - canonical_isospin_pyhecke.py (6-atom version)
  - low_isotope_mass_table.py (non-categorical fallbacks)
"""
from __future__ import annotations

import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "../../tools/pyhecke/python"))
import pyhecke

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0


# 23 stable isotopes with Z ≤ 10, matching low_isotope_mass_table.AME
ATOMS: list[tuple[str, int, int]] = [
    ("1H",   1,  0),
    ("2H",   1,  1),
    ("3H",   1,  2),
    ("3He",  2,  1),
    ("4He",  2,  2),
    ("6Li",  3,  3),
    ("7Li",  3,  4),
    ("8Be",  4,  4),
    ("9Be",  4,  5),
    ("10Be", 4,  6),
    ("10B",  5,  5),
    ("11B",  5,  6),
    ("12C",  6,  6),
    ("13C",  6,  7),
    ("14N",  7,  7),
    ("15N",  7,  8),
    ("16O",  8,  8),
    ("17O",  8,  9),
    ("18O",  8, 10),
    ("19F",  9, 10),
    ("20Ne", 10, 10),
    ("21Ne", 10, 11),
    ("22Ne", 10, 12),
]


def main() -> int:
    print("=" * 80)
    print("  FULL-CENSUS canonical Markov trace via pyhecke (Z ≤ 10, n_strands = 3A)")
    print(f"  q_0 = {float(Q0):.10f}")
    print(f"  pyhecke version: {getattr(pyhecke, '__version__', '?')}")
    try:
        crt_avail = pyhecke.trace.has_crt_backend()
        print(f"  CRT backend:    {'AVAILABLE' if crt_avail else 'unavailable'}")
    except Exception:
        print(f"  CRT backend:    unknown")
    print("=" * 80)
    print(f"\n  {'atom':>5} {'Z':>2} {'N':>2} {'A':>3} {'n':>3}  "
          f"{'tr_M(q_0)':>16}  {'log|tr_M|':>10}  {'sec':>6}")
    print("  " + "-" * 70)

    results: dict[str, dict] = {}
    for label, Z, N in ATOMS:
        A = Z + N
        n_strands = 3 * A
        # Single nucleon ⇒ no inter-nucleon generator, mirror existing witness
        include_inter = (A >= 2)
        t0 = time.time()
        try:
            tr = pyhecke.trace.markov_trace_symbolic_eval(
                Z, N, include_inter, 1, 1, 1, float(Q0), precision=30
            )
            # Coerce to a finite real if the imag part is negligible; keep
            # complex otherwise so abs()/log() still work without TypeError.
            if hasattr(tr, "imag") and abs(tr.imag) >= 1e-9:
                tr_val = complex(tr)
                tr_disp = f"{tr_val.real:+.6e}{tr_val.imag:+.2e}j"
            else:
                tr_val = float(tr.real if hasattr(tr, "imag") else tr)
                tr_disp = f"{tr_val:>+16.6e}"
            log_tr = math.log(abs(tr_val)) if abs(tr_val) > 0 else float("nan")
            dt = time.time() - t0
            print(f"  {label:>5} {Z:>2} {N:>2} {A:>3} {n_strands:>3}  "
                  f"{tr_disp:>16}  {log_tr:>+10.4f}  {dt:>6.3f}")
            results[label] = {
                "Z": Z, "N": N, "A": A, "n_strands": n_strands,
                "include_inter": include_inter,
                "tr_M_q0": (str(tr_val) if isinstance(tr_val, complex)
                            else tr_val),
                "log_abs_tr_M_q0": log_tr,
                "walltime_sec": dt,
            }
        except Exception as exc:
            dt = time.time() - t0
            print(f"  {label:>5} {Z:>2} {N:>2} {A:>3} {n_strands:>3}  "
                  f"ERROR  {type(exc).__name__}: {str(exc)[:50]}  {dt:>6.3f}")
            results[label] = {
                "Z": Z, "N": N, "A": A, "n_strands": n_strands,
                "include_inter": include_inter,
                "error": f"{type(exc).__name__}: {exc}",
                "walltime_sec": dt,
            }

    successes = sum(1 for r in results.values() if "tr_M_q0" in r)
    total_walltime = sum(r["walltime_sec"] for r in results.values())
    print()
    print(f"  Successes: {successes}/{len(ATOMS)}  total walltime: {total_walltime:.2f}s")

    witness = {
        "computation": "canonical-isospin-pyhecke-full-census",
        "description": (
            "Full-census canonical Markov trace tr_M(q_0) for all 23 stable "
            "isotopes with Z ≤ 10 in the low_isotope_mass_table.py census. "
            "Extends canonical_isospin_pyhecke.py (6 atoms) to the full set "
            "by simply iterating the existing pyhecke entry point — no new "
            "infrastructure needed.  Removes the 'no canonical tr_M for "
            "Z ≥ 3' bottleneck identified in PR #514 follow-up."
        ),
        "reference_blocks": [
            "prop:categorical-mass-markov",
            "thm:jones-markov-trace",
            "rem:commutative-crossing-energy",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(Q0),
            "precision": 30,
            "n_atoms": len(ATOMS),
        },
        "results": results,
    }

    out_path = Path(__file__).parent / "canonical-isospin-pyhecke-full-census.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
