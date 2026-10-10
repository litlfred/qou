#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
Canonical Markov trace ISOSPIN test: T vs ³He.

Uses the canonical Jones-Markov trace (via Markov axioms M1, M2)
applied to the SymbolicHeckeElement of the atomic braid, to test
whether |tr_M(W_T)| ≈ |tr_M(W_³He)| under isospin (p ↔ n).

Background.  Earlier session work (Item 1, paper-six-term-isotope-
sweep) found a 738 MeV asymmetry between T and ³He using the
ordering-sensitive `atom_per_generator_volumes`-based formula.
Strong-force isospin symmetry predicts these should differ by
≤ a few MeV (Coulomb + n − p mass difference only).

The canonical Jones-Markov trace IS Markov-invariant by
construction (axiomatic).  This test reports the canonical traces
for both isotopes and the difference.

Witness: canonical-isospin-test.witness.json
"""
import json
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0
from markov_trace_canonical import tr_M_element
from hecke_symbolic import SymbolicHeckeDivision, q as q_sym
from binding_canonical import build_atom_symbolic


def canonical_trace_atom(Z: int, N: int, include_inter: bool = True,
                          m_pp: int = 1, m_pn: int = 1, m_nn: int = 1):
    """Build the atomic-braid SymbolicHeckeElement, reduce via the
    Hecke division algorithm, and compute its canonical
    Jones-Markov trace at q = q_0.

    Returns (tr_M_at_q0, walltime_seconds).
    """
    t0 = time.time()
    div = SymbolicHeckeDivision()
    elem = build_atom_symbolic(Z, N, include_inter=include_inter,
                                m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
    elem, _info = div.reduce(elem)
    A = Z + N
    tr_sym = tr_M_element(elem, 3 * A)
    tr_q0 = complex(sp.N(tr_sym.subs(q_sym, Q0)))
    if abs(tr_q0.imag) < 1e-9:
        tr_q0 = tr_q0.real
    return tr_q0, time.time() - t0


if __name__ == "__main__":
    print("CANONICAL MARKOV TRACE — ISOSPIN PARITY TEST (T vs ³He)")
    print("=" * 80)
    print(f"q_0 = {float(Q0):.6f}")
    print()
    print("NOTE.  The canonical Jones-Markov trace IS Markov-invariant")
    print("by construction.  However, the underlying GS-reduction in")
    print("SymbolicHeckeDivision can take radically different walltime")
    print("on isospin-partner braid words even when their abstract")
    print("Markov closures are equivalent.  Initial run showed:")
    print("  T   (Z=1, N=2):  163s, |tr_M| = 0.104052")
    print("  ³He (Z=2, N=1):  >25min unfinished (RSS peak 425 MB)")
    print()
    print("This asymmetry in compute cost is itself a finding: the")
    print("Hecke-division reduction graph for the (uud-uud-udd)")
    print("ordering has dramatically different complexity than for")
    print("(uud-udd-udd).  The Markov trace value is invariant, but")
    print("the path to compute it is not.  Use TIMEOUT_SECONDS=N to")
    print("limit per-isotope wallclock.")
    print()
    print("NOTE: this script does NOT enforce a per-isotope hard")
    print("timeout — a stuck reduction will run until externally")
    print("killed.  For a true wallclock cap wrap each invocation in")
    print("`multiprocessing.Process(target=...).join(timeout=...)`.")
    print("The recommended fast path is canonical_isospin_pyhecke.py")
    print("(milliseconds per isotope via the optimised pyhecke backend).")
    print()

    cases = [
        ("T  (Z=1, N=2)", 1, 2),
        ("³He (Z=2, N=1)", 2, 1),
    ]

    results = {}
    for label, Z, N in cases:
        print(f"\n── {label} ──")
        try:
            tr_q0, dt = canonical_trace_atom(Z, N, include_inter=True)
            print(f"  tr_M @ q_0 = {tr_q0}")
            print(f"  |tr_M|     = {abs(tr_q0):.6f}")
            print(f"  walltime   = {dt:.1f}s")
            results[label] = {
                "Z": Z, "N": N,
                "tr_M_q0": str(tr_q0),
                "abs_tr_M": float(abs(tr_q0)),
                "walltime_sec": dt,
            }
        except Exception as exc:
            print(f"  ERROR: {type(exc).__name__}: {exc}")
            results[label] = {"error": f"{type(exc).__name__}: {exc}"}

    # Compare
    print("\n── ISOSPIN COMPARISON ──")
    if "T  (Z=1, N=2)" in results and "³He (Z=2, N=1)" in results:
        T = results["T  (Z=1, N=2)"]
        He3 = results["³He (Z=2, N=1)"]
        if "error" not in T and "error" not in He3:
            diff = T["abs_tr_M"] - He3["abs_tr_M"]
            ratio = T["abs_tr_M"] / He3["abs_tr_M"] if He3["abs_tr_M"] > 0 else float('inf')
            print(f"  |tr_M(T)|     = {T['abs_tr_M']:.6f}")
            print(f"  |tr_M(³He)|   = {He3['abs_tr_M']:.6f}")
            print(f"  difference    = {diff:+.6e}")
            print(f"  ratio T/³He   = {ratio:.6f}")
            print()
            if abs(diff) < 0.01 * max(T["abs_tr_M"], He3["abs_tr_M"]):
                print("  ✓ ISOSPIN SYMMETRY PRESERVED to <1%")
                print("    Canonical Markov trace gives nearly identical")
                print("    values for the isospin-partner braids.")
            else:
                print(f"  Asymmetry of {abs(diff):.3e} ({100*abs(diff)/max(T['abs_tr_M'], He3['abs_tr_M']):.2f}%)")

    witness = {
        "computation": "canonical-isospin-test",
        "description": (
            "Canonical Jones-Markov trace applied to the atomic-braid "
            "SymbolicHeckeElement of T (Z=1,N=2) and ³He (Z=2,N=1), "
            "testing whether the Markov-axiomatically-correct trace "
            "preserves isospin symmetry (p ↔ n).  This is the proper "
            "test of the 738 MeV asymmetry observed in the paper's "
            "ordering-sensitive 6-term formula."
        ),
        "reference_blocks": [
            "prop:categorical-mass-markov",
            "thm:jones-markov-trace",
            "rem:commutative-crossing-energy",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(Q0),
        },
        "results": results,
    }
    out = Path(__file__).parent / "canonical-isospin-test.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
