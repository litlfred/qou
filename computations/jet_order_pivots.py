"""Jet-order independence pivots from the canonical Markov traces.

Discharges (numerically, as a compute witness) the base case of
`conj:three-knot-jet-order-independence`: the h-jet expansions of the
canonical Markov traces tr_M(K) of the three QOU knots
(4_1, 5_2, Borromean 𝓑₃) are linearly independent at jet order 2.

The jet order = h-order of the expansion about q = 1 (per the canonical
chain's jet/GB-filtration mapping, cheat-sheet §2 step 7 +
`docs/audits/2026-05-24-derivation-chain-gb-jet-orders-and-pentagon.md`).
Each tr_M(K) is the framework's own Markov trace of the canonical braid
word (`knot_braid_database.braid_word_for_knot`), a single-variable
rational function in q with the Markov parameter already canonically
substituted.

Output: the 3×3 jet-coefficient matrix M (rows = knots, cols =
h^0,h^1,h^2), its determinant (the GB-elimination determinant), and the
LU pivots — the real GB-elimination certificate wired into
`QOU.Archimedean.JetOrderIndependence.jetPivots`.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE / "substrate"))  # witness_base shim
sys.path.insert(0, str(_HERE.parent / "qou-mass" / "src"))

import sympy as sp  # noqa: E402

from qou_mass._internal.markov_trace_recursive import markov_trace_of_word  # noqa: E402
from knot_braid_database import braid_word_for_knot  # noqa: E402

KNOTS = ["4_1", "5_2", "Borromean"]
JET_ORDER = 2  # expand to h^2 → 3 coefficients (h^0, h^1, h^2)


def jet_coeffs(knot: str, order: int = JET_ORDER) -> list[sp.Rational]:
    """h-jet coefficients of tr_M(knot) about q = 1, orders 0..`order`."""
    h = sp.symbols("h")
    bw = braid_word_for_knot(knot)
    word = [s * g for (s, g) in bw]
    tr = markov_trace_of_word(3, word)
    # Use the trace's OWN q symbol (not a freshly-created one, which would
    # be a distinct object and make `.subs` a silent no-op). Look it up by
    # name — set iteration order is not deterministic, so `next(iter(...))`
    # could pick the wrong symbol if the trace ever carries more than q.
    q_syms = [s for s in tr.free_symbols if s.name == "q"]
    if len(q_syms) != 1:
        raise ValueError(
            f"expected exactly one 'q' symbol in tr_M({knot}); "
            f"got free_symbols={sorted(str(s) for s in tr.free_symbols)}"
        )
    q = q_syms[0]
    # Expand about q = 1 (the jet/h grading): q = 1 + h.
    ser = sp.series(tr.subs(q, 1 + h), h, 0, order + 1).removeO()
    poly = sp.Poly(sp.expand(ser), h)
    return [sp.nsimplify(poly.coeff_monomial(h**k)) for k in range(order + 1)]


def main() -> int:
    # Construct the witness builder BEFORE the compute so its durationMs
    # reflects the actual SymPy work (not just serialization).
    from witness_base import WitnessBuilder

    w = WitnessBuilder("jet-order-pivots", engine="sympy")

    rows = []
    print("Jet-order coefficient vectors (h^0, h^1, h^2) of tr_M(K):")
    for K in KNOTS:
        c = jet_coeffs(K)
        rows.append(c)
        print(f"  {K:>10}: {[str(x) for x in c]}")

    M = sp.Matrix(rows)
    det = sp.simplify(M.det())
    print(f"\nGB-elimination determinant det(M) = {det}")
    assert det != 0, "jet-order independence FAILS at order 2 (det = 0)"

    # LU pivots = diagonal of U (product = ±det); these are the
    # GB-eliminated pivots to wire into Lean.
    _, U, _ = M.LUdecomposition()
    pivots = [sp.nsimplify(U[i, i]) for i in range(M.shape[0])]
    print(f"LU pivots (echelon diagonal): {[str(p) for p in pivots]}")
    print(f"product of pivots          : {sp.simplify(sp.prod(pivots))}")

    # Populate the witness (builder constructed at the top of main, pre-compute).
    w.add_data("knots", KNOTS)
    w.add_data("jet_order", JET_ORDER)
    w.add_data("jet_jacobian", {
        K: [str(x) for x in r] for K, r in zip(KNOTS, rows)
    })
    w.add_data("elimination_det", str(det))
    w.add_data("lu_pivots", [str(p) for p in pivots])
    w.set_content_block("conj:three-knot-jet-order-independence")
    w.add_assertion(
        "jet_order_independence_base_case",
        computed=1 if det != 0 else 0,
        expected=1,
        source=(
            "h-jet expansion of canonical Markov traces tr_M(4_1/5_2/"
            "Borromean) about q=1 has non-singular 3x3 jet-Jacobian "
            "(det = 1/16) ⇒ jet-order independent at order 2"
        ),
    )
    out = w.save()
    print(f"\nWitness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
