#!/usr/bin/env python3
"""Phase 3 — symbolic Hecke NF + Markov trace for helium-3 (³He).

Mirrors atom_nf_symbolic_D.py for Z=2, N=1 (3A=9 strands).
Outputs `atom-nf-symbolic-He3.witness.json`.
"""
import os
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

os.environ.setdefault("ATOM_LABEL", "He3")
import atom_nf_symbolic_D as base  # noqa: E402


def main_He3() -> int:
    import json, time, sympy as sp, mpmath as mp
    from datetime import datetime, timezone
    from witness_base import WitnessBuilder
    from witness_polynomial import expose_polynomial
    print("=" * 100)
    print("PHASE 3 — Symbolic Hecke NF of ³He atom braid")
    print("  Pipeline: atom Hecke element → GS NF → Markov trace → Jones")
    print("=" * 100)

    Z, N = 2, 1  # ³He
    print(f"\n  Building ³He's symbolic Hecke NF (Z={Z}, N={N}, 3A=9 strands)…")
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
        print("\n  Computing symbolic Markov trace tr_M(³He's NF)…", flush=True)
        t0 = time.time()
        tr = base.tr_M_element(elem, 3 * (Z + N))
        elapsed_trace = time.time() - t0
        print(f"  Elapsed (trace): {elapsed_trace:.2f} s")
        tr_simp = sp.simplify(tr)
        try:
            tr_val = complex(tr_simp.subs(q_sym, q0_rat))
        except Exception:
            tr_val = None
        print(f"  tr_M(³He-atom)|_{q_sym}=q_0  = {tr_val}")

    out = (
        WitnessBuilder("atom-NF-symbolic-He3", engine="sympy")
        .set_description(
            "Symbolic Hecke NF of ³He atom braid via Gröbner–Shirshov "
            "(SymbolicHeckeDivision). Mirror of atom-NF-symbolic-D for "
            "Z=2, N=1 (3A=9 strands)."
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
        .add_data("at_q0", {"tr_M_He3": str(tr_val)})
        .add_data("trace_elapsed_sec", elapsed_trace)
    )
    out_path = out.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main_He3())
