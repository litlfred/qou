#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic identity delta_q = h*[k]_q for the
# basis knots; reset-resilient proof (no Lean env needed).
"""
SYMBOLIC PROOF: delta_q(T_{2,k}) = q^k - q^{-k} = h*[k]_q, exactly, for the
alpha_{basis-knot} couplings (step 4 of the program — the Lean is the trivial
field_simp formalisation, written separately; this sympy proof is the
reset-resilient cross-check that the identity holds as a polynomial identity in
R = Z[q^{+-1/2}, h^{-1}], no archimedean evaluation, no pi).

  [k]_q := (q^k - q^{-k}) / (q - q^{-1})        (quantum integer)
  h     := q - q^{-1}                           (Hecke deformation)
  delta_q(T_{2,k}) := q^k - q^{-k}              (q-dimension decoration)

  Claim:  delta_q(T_{2,k}) = h * [k]_q   <=>   q^k - q^{-k} = (q-q^{-1}) * [k]_q
          (immediate from the definition of [k]_q; proven exactly below).

Refs: prop:alpha-em-categorical-trace-ratio; docs/workplans/2026-06-10-
alpha-basis-knot-couplings.md; alpha_basis_knot_couplings.py (the foundation).
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

try:
    import sympy as sp
    HAVE_SYMPY = True
except Exception:
    HAVE_SYMPY = False


def main() -> None:
    w = WitnessBuilder("delta-q-h-bracket-identity", engine="python")
    if not HAVE_SYMPY:
        print("sympy unavailable — install sympy to run the symbolic proof.")
        w.set_description("delta_q = h[k]_q symbolic proof (sympy unavailable).")
        w.add_data("status", "sympy-unavailable")
        w.save()
        return

    q = sp.symbols("q", positive=True)
    h = q - 1 / q
    print("=" * 70)
    print("Symbolic proof: delta_q(T_{2,k}) = h*[k]_q  (exact, in R, no pi)")
    print("=" * 70)
    all_ok = True
    rows = {}
    # The 6 cohomological force-knots' effective 2-strand exponents (T_{3,5}->10).
    for k in (3, 5, 7, 9, 10):
        delta = q ** k - q ** (-k)                    # delta_q(T_{2,k})
        qbracket = (q ** k - q ** (-k)) / (q - 1 / q)  # [k]_q
        # the identity: delta - h*[k]_q == 0 (as a rational function in q)
        diff = sp.simplify(delta - h * qbracket)
        ok = (diff == 0)
        all_ok = all_ok and ok
        # also confirm [k]_q is the q-integer 1+q^2+...+q^{2(k-1)} times q^{-(k-1)}
        qint = sp.simplify(qbracket * q ** (k - 1))    # should be a polynomial in q^2
        rows[f"k{k}"] = {"delta_eq_h_bracket": bool(ok),
                         "qbracket_times_qk1": str(sp.expand(qint))}
        print(f"  k={k:2d}:  delta_q - h*[k]_q simplifies to {diff}   "
              f"=> identity holds: {ok}")
    print()
    print(f"  ALL basis-knot exponents satisfy delta_q = h*[k]_q exactly: {all_ok}")
    print(f"  (purely q-rational; no archimedean evaluation, no pi)")

    w.set_description(
        "Symbolic (sympy) proof that the q-dimension decoration delta_q(T_{2,k}) "
        "= q^k - q^{-k} equals h*[k]_q exactly, h = q - q^{-1}, for the basis-knot "
        "exponents k in {3,5,7,9,10} (the alpha_{basis-knot} couplings). A "
        "polynomial identity in R = Z[q^{+-1/2}, h^{-1}] — pre-archimedean, no pi. "
        "This is the reset-resilient cross-check for the trivial field_simp Lean "
        "formalisation (step 4 of the alpha_{basis-knot} program)."
    )
    w.set_content_block("prop:alpha-em-categorical-trace-ratio")
    w.add_data("basis_knot_exponents", [3, 5, 7, 9, 10])
    w.add_data("per_k", rows)
    w.add_assertion(
        "delta_q(T_{2,k}) = h*[k]_q exactly for all basis-knot exponents",
        computed=bool(all_ok), expected=True,
        source="sympy.simplify(q^k - q^{-k} - (q-q^{-1})*[k]_q) == 0",
    )
    w.add_data(
        "finding",
        "delta_q(T_{2,k}) = q^k - q^{-k} = h*[k]_q is an exact polynomial identity "
        "in R = Z[q^{+-1/2}, h^{-1}] (no pi), verified symbolically for the basis-"
        "knot exponents {3,5,7,9,10}. The Lean formalisation is the trivial "
        "field_simp proof of deltaQ q k = (q - q^{-1}) * qbracket q k; this sympy "
        "proof is the reset-resilient cross-check while the Lean env is restoring."
    )
    w.save()
    print("\nDone. Witness saved (delta-q-h-bracket-identity).")


if __name__ == "__main__":
    main()
