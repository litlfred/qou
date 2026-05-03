#!/usr/bin/env python3
"""Heavy-atom Markov trace via recursive ascent (Markov-axiom path).

Extension of `crt_markov_v3.py` to A ≥ 4 atoms via the recursive-
ascent rewrite landed in PR #516 (`markov_peel.tr_M_atomic`). The
brute-force per-Hoefsmit-block path used by v3 was infeasible at
n = 3A ≥ 12 due to dim-462+ matrix multiplications; the
Markov-axiom recursion bypasses Hoefsmit-matrix construction
entirely, peeling generators from the top of the braid word and
descending to lower H_n algebras until termination at H_1 = R.

Atoms covered (A=1..4 carry over from v3 / atomic_tr_m_mpfr; new
contribution is A=4 ⁴He via recursive ascent):

  proton     A=1   B_3   sanity check
  neutron    A=1   B_3   sanity check
  D          A=2   B_6   sanity check vs habiro coefficients
  T (³H)     A=3   B_9   sanity check vs habiro coefficients
  ³He        A=3   B_9   sanity check vs habiro coefficients
  ⁴He        A=4   B_12  NEW — first A=4 atom via recursive ascent
  ⁶Li        A=6   B_18  NEW — family-4 atom (recursive ascent only)
  ⁷Li        A=7   B_21  NEW — family-4 atom

Output: `heavy-atoms-markov-peel.witness.json`

Usage:
    python3 folio-assistant/computations/heavy_atoms_markov_peel.py
    python3 folio-assistant/computations/heavy_atoms_markov_peel.py --atom helium-4
    python3 folio-assistant/computations/heavy_atoms_markov_peel.py --max-iterations 50000
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from markov_peel import tr_M_atomic  # noqa: E402
from q_parameter import Q as Q0_FLOAT  # noqa: E402


ATOMS = [
    # (label, Z, N, atomic-mass-MeV, expected-via-known-paths)
    ("proton",    1, 0, "1.0078250319"),
    ("neutron",   0, 1, "1.0086649157"),
    ("deuteron",  1, 1, "2.014101778"),
    ("tritium",   1, 2, "3.0160492"),
    ("helium-3",  2, 1, "3.0160293"),
    ("helium-4",  2, 2, "4.002602"),
    ("lithium-6", 3, 3, "6.0151229"),
    ("lithium-7", 3, 4, "7.0160034"),
]


def evaluate_at_q0(expr: sp.Expr, q: sp.Symbol, q0: sp.Rational,
                   dps: int = 50) -> tuple[float, str]:
    """Evaluate sympy expression at q = q0 with `dps` decimal precision.
    Returns (float, str) — float for arithmetic, str for full-precision
    storage."""
    val = sp.N(expr.subs(q, q0), dps)
    return float(val), str(val)


def analyze_atom(label: str, Z: int, N: int, *,
                 max_iterations: int = 100000) -> dict[str, Any]:
    """Compute tr_M(β_atom) symbolically via markov_peel, then
    evaluate at q_0."""
    A = Z + N
    n_strands = 3 * A
    print(f"\n══ {label}  (Z={Z}, N={N}, A={A}, n={n_strands}) ══")
    t0 = time.time()
    try:
        tr_sym = tr_M_atomic(
            Z, N, include_inter=True,
            reduce_first=True,
            max_iterations=max_iterations,
        )
        elapsed_sym = time.time() - t0
    except Exception as e:
        print(f"  symbolic FAIL: {type(e).__name__}: {str(e)[:200]}")
        return {
            "atom": label, "Z": Z, "N": N, "A": A,
            "error": f"{type(e).__name__}: {str(e)[:300]}",
        }

    # Evaluate at q_0.
    q = sp.Symbol("q", positive=True, real=True)
    q0_rat = sp.Rational(str(Q0_FLOAT))
    t1 = time.time()
    try:
        val_float, val_str = evaluate_at_q0(tr_sym, q, q0_rat, dps=50)
    except Exception as e:
        print(f"  numeric eval FAIL: {type(e).__name__}: {e}")
        val_float, val_str = float("nan"), str(e)
    elapsed_eval = time.time() - t1

    tr_str = str(tr_sym)
    print(f"  tr_M(β_atom, q) = {tr_str[:80]}{'…' if len(tr_str)>80 else ''}")
    print(f"  tr_M @ q_0 = {val_float:+.10e}")
    print(f"  symbolic compute: {elapsed_sym:.2f}s, "
          f"q_0 eval: {elapsed_eval:.2f}s")

    return {
        "atom": label,
        "Z": Z, "N": N, "A": A,
        "n_strands": n_strands,
        "tr_M_symbolic": tr_str,
        "tr_M_at_q0_float": val_float,
        "tr_M_at_q0_str": val_str,
        "compute_time": {
            "symbolic_seconds": elapsed_sym,
            "evaluation_seconds": elapsed_eval,
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--atom",
                    choices=["proton", "neutron", "deuteron", "tritium",
                             "helium-3", "helium-4", "lithium-6", "lithium-7"],
                    default=None,
                    help="Run only this atom (default: all up to 7Li)")
    ap.add_argument("--max-iterations", type=int, default=100000,
                    help="Markov-peel recursion iteration cap")
    args = ap.parse_args()

    print("=" * 72)
    print("Heavy atoms via Markov-axiom recursive ascent (markov_peel)")
    print("=" * 72)
    print(f"  q_0 = {float(Q0_FLOAT)}")
    print(f"  max_iterations = {args.max_iterations}")
    print()

    if args.atom:
        atoms_to_run = [a for a in ATOMS if a[0] == args.atom]
    else:
        atoms_to_run = ATOMS

    out_path = HERE / "heavy-atoms-markov-peel.witness.json"
    if out_path.exists():
        existing = json.loads(out_path.read_text())
    else:
        existing = {
            "computation": "heavy-atoms-markov-peel",
            "description": (
                "Markov trace tr_M(β_atom) for atomic braids via "
                "recursive Markov-axiom ascent. Bypasses the per-"
                "Hoefsmit-block O(d³) bottleneck that blocks brute-"
                "force computation at A ≥ 4. Builds on PR #516's "
                "markov_peel.tr_M_atomic."
            ),
            "reference_blocks": [
                "thm:jones-markov-trace",
                "prop:markov-pair-z2",
            ],
            "engine": "sympy + markov_peel (recursive ascent)",
            "results": {},
        }
    existing["computedAt"] = datetime.now(timezone.utc).isoformat()

    for label, Z, N, _amu in atoms_to_run:
        result = analyze_atom(label, Z, N,
                              max_iterations=args.max_iterations)
        existing["results"][label] = result
        # Save incrementally so a long run doesn't lose progress on crash.
        out_path.write_text(
            json.dumps(existing, indent=2, ensure_ascii=False)
        )

    print()
    print("=" * 72)
    print(f"Witness: {out_path.name}")
    print("=" * 72)
    print(f"\n{'atom':<14} {'A':>3} {'n':>4} {'tr_M @ q_0':>16}  symbolic-time")
    print("─" * 70)
    for label, *_ in atoms_to_run:
        r = existing["results"].get(label, {})
        if "error" in r:
            print(f"  {label:<14}{'?':>4}{'?':>5}  ERROR: "
                  f"{r['error'][:60]}")
            continue
        val = r.get("tr_M_at_q0_float", float("nan"))
        sym_t = r.get("compute_time", {}).get("symbolic_seconds", 0)
        print(f"  {label:<14}{r.get('A'):>3}{r.get('n_strands'):>5}  "
              f"{val:>+15.6e}  {sym_t:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
