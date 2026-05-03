#!/usr/bin/env python3
"""Phase 3 — symbolic Hecke NF + Markov trace for tritium (³H).

Mirrors atom_nf_symbolic_D.py for Z=1, N=2 (3A=9 strands).
Outputs `atom-nf-symbolic-T.witness.json`.
"""
import os
import sys
from pathlib import Path

# Override D's main with T's parameters
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

# Set up T-specific names then run the D module's pipeline
os.environ.setdefault("ATOM_LABEL", "T")

import atom_nf_symbolic_D as base  # noqa: E402

# Patch the symbol so the witness lands at atom-nf-symbolic-T.json
ORIG_MAIN = base.main


def main_T() -> int:
    # Re-implement main with Z=1, N=2 and witness name change
    import json, time, sympy as sp, mpmath as mp
    from datetime import datetime, timezone
    from witness_base import WitnessBuilder
    from witness_polynomial import expose_polynomial
    print("=" * 100)
    print("PHASE 3 — Symbolic Hecke NF of T (³H) atom braid")
    print("  Pipeline: atom Hecke element → GS NF → Markov trace → Jones")
    print("=" * 100)

    Z, N = 1, 2  # Tritium
    print(f"\n  Building T's symbolic Hecke NF (Z={Z}, N={N}, 3A=9 strands)…")
    elem, stats = base.build_atom_nf_symbolic(Z, N, reduce_every=4)
    print(f"  Input factors: {stats['n_factors']}")
    print(f"  GS reductions: {stats['n_reductions']}")
    print(f"  NF terms:      {stats['n_terms_nf']}")
    print(f"  Elapsed (NF):  {stats['elapsed_sec']:.2f} s")

    SKIP_TRACE = os.environ.get("SKIP_TRACE", "0") == "1"
    q_sym = base.q_sym
    q0_rat = base._Q0_RATIONAL

    if SKIP_TRACE:
        tr_simp = sp.S(0)
        tr_val = 0j
        elapsed_trace = 0.0
    else:
        print("\n  Computing symbolic Markov trace tr_M(T's NF)…", flush=True)
        t0 = time.time()
        tr = base.tr_M_element(elem, 3 * (Z + N))  # n strands
        elapsed_trace = time.time() - t0
        print(f"  Elapsed (trace): {elapsed_trace:.2f} s")
        tr_simp = sp.simplify(tr)
        try:
            tr_val = complex(tr_simp.subs(q_sym, q0_rat))
        except Exception:
            tr_val = None
        print(f"  tr_M(T-atom)|_{q_sym}=q_0  = {tr_val}")

    out = (
        WitnessBuilder("atom-NF-symbolic-T", engine="sympy")
        .set_description(
            "Symbolic Hecke NF of T (³H) atom braid via Gröbner–Shirshov "
            "(SymbolicHeckeDivision). Mirror of atom-NF-symbolic-D for "
            "Z=1, N=2 (3A=9 strands)."
        )
        .add_parameter("Z", Z)
        .add_parameter("N", N)
        .add_parameter("A", Z + N)
        .add_parameter("n_strands", 3 * (Z + N))
        .add_data("stats", stats)
        .add_data("markov_trace_symbolic", str(tr_simp))
        .add_data(
            "markov_trace_polynomial",
            expose_polynomial(tr_simp, q_sym, simplify=False),
        )
        .add_data("at_q0", {"tr_M_T": str(tr_val)})
        .add_data("trace_elapsed_sec", elapsed_trace)
    )
    out_path = out.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main_T())
