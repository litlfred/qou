#!/usr/bin/env python3
"""
qbeta_gram_determinant_root_multiplicity_law_probe.py — the H_3 Markov Gram
determinant, its four roots, and which block each one kills.

# Ref: https://github.com/litlfred/qou/pull/5337#issuecomment-5430196684
# Ref: computations/qbeta/qbeta_admissible_functionals_bracket_probe.py

WHERE THIS CAME FROM. A sibling on `qou-s7z2` posted the closed-form n = 3
Markov Gram determinant and read its third factor as the convention-D pin:

    det G = -(z-q)^5 (qz+1)^5 ((q^2+1)z - q^3) (q^3 z + qz + 1) / q^8

    "the third factor ((q^2+1)z - q^3) IS the convention-D pin z = q^3/(q^2+1)
     rearranged ... If you need to assert 'the D pin is what kills the
     antisymmetric block' without routing through y_lambda or a z grep, that
     factorisation is a complete test on its own."

Three things follow, and they run in both directions.

--- 1. THE DETERMINANT IS RIGHT, independently ------------------------------

Re-derived here from the Ocneanu trace as solved in this branch, not quoted:
the trace form G_ij = tr_M(T_i T_j) on the six-element basis has exactly that
determinant, ratio 1, symbolically in q and z. That is an independent
confirmation of the sibling's formula.

--- 2. IT CONTAINS BOTH OF MY ROOTS, and the FIRST factor is the one they
       did not flag ------------------------------------------------------

`qbeta_admissible_functionals_bracket_probe` solved y_(1,1,1)(z) = 0 and found
TWO roots, z = q and z = z_D. The sibling read the third factor (z_D) and passed
over the first, (z - q)^5 — which is the same z = q. So their factorisation
corroborates the completeness result from an entirely different object, and this
probe corroborates their determinant. Mutual, and neither side had noticed.

--- 3. BUT det G = 0 IS NOT SUFFICIENT for the two-row condition ------------

The determinant has FOUR roots; only TWO annihilate the (1,1,1) weight:

    z = -1/(q^3+q)   mult 1   kills (3)
    z = -1/q         mult 5   kills (3) and (2,1)
    z = q            mult 5   kills (2,1) and (1,1,1)
    z = q^3/(q^2+1)  mult 1   kills (1,1,1)

So "det G = 0" admits z = -1/q and z = -1/(q^3+q), where the antisymmetric block
survives. Read charitably the sibling may mean the FACTOR ((q^2+1)z - q^3) is a
complete test, and that reading is correct — the factor pins z_D exactly. Read as
"the determinant vanishing is the test", it is necessary and not sufficient. The
distinction is worth stating because the sentence is one a later reader inherits.

--- THE LAW THAT MAKES IT USABLE -------------------------------------------

Each root's multiplicity in det G is exactly the sum of dim(lambda)^2 over the
blocks whose weight vanishes there:

    (3): 1,  (2,1): 4,  (1,1,1): 1
    mult 1 = 1        (one 1-dim block)
    mult 5 = 4 + 1    (the 2-dim block and a 1-dim one)

Verified for all four roots. So the determinant is not a binary test at all — it
is a READABLE diagnostic: the multiplicity says which blocks die, and the D pin
is the root of multiplicity 1 that kills (1,1,1) alone.

NO fit, NO wiring, no value proposed. Exact symbolic in q and z. Scope-(a).
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    q, h, N, BASIS, LEFT, basis_vec, reg_char, length,
)

set_compute_dps(50)

Z = sp.Symbol("z")
LABELS = ["(3)", "(2,1)", "(1,1,1)"]
DIMS = [1, 2, 1]


def main() -> int:
    w = WitnessBuilder("qbeta-gram-determinant-root-multiplicity-law", engine="sympy")
    w.set_description(
        "The H_3 Markov Gram determinant re-derived independently; its four "
        "roots identified with the blocks they annihilate; and the law that "
        "each root's multiplicity is the sum of dim^2 over those blocks."
    )
    ok, notes = [], []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        if note:
            notes.append({"assertion": name, "note": note})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    TR = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]

    def tr(v):
        return sp.expand(sum(v[i] * TR[i] for i in range(N)))

    G = sp.zeros(N, N)
    for i in range(N):
        for j in range(N):
            G[i, j] = tr(LEFT[i] * basis_vec(j))
    det = sp.factor(sp.simplify(G.det()))

    sib = (-(Z - q)**5 * (q * Z + 1)**5 * ((q**2 + 1) * Z - q**3)
           * (q**3 * Z + q * Z + 1) / q**8)
    check("reproduces_the_sibling_gram_determinant_independently",
          sp.simplify(sp.cancel(det / sib) - 1) == 0,
          "(ratio exactly 1 — re-derived from this branch's Ocneanu trace, "
          "not quoted from gram-matrix-h3-symbolic)")

    # the weights
    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI = [chi3, chi21, chi111]
    ys = sp.symbols("y0 y1 y2")
    sol = sp.solve([sp.Eq(sum(ys[k] * CHI[k](basis_vec(i)) for k in range(3)), TR[i])
                    for i in (0, 1, 3)], ys, dict=True)[0]
    Y = [sp.simplify(sp.factor(sol[ys[k]])) for k in range(3)]

    facs = sp.factor_list(sp.expand(sp.numer(sp.together(det))), Z)[1]
    roots = []
    for f, m in facs:
        rs = sp.solve(f, Z)
        for r in rs:
            roots.append((sp.simplify(r), m))
    roots.sort(key=lambda t: str(t[0]))
    check("the_determinant_has_exactly_four_roots_in_z", len(roots) == 4,
          f"({[str(r) for r, _ in roots]})")

    rows, law_ok = [], True
    for r, m in roots:
        killed = [k for k in range(3) if sp.simplify(Y[k].subs(Z, r)) == 0]
        s = sum(DIMS[k] ** 2 for k in killed)
        law_ok = law_ok and (s == m)
        rows.append({"root": str(r), "multiplicity": int(m),
                     "blocks_killed": [LABELS[k] for k in killed],
                     "sum_dim_squared": int(s)})
        print(f"    z = {str(r):<18} mult {m}   kills {[LABELS[k] for k in killed]}"
              f"   Σdim² = {s}")

    check("MULTIPLICITY_LAW_mult_equals_sum_of_dim_squared_over_blocks_killed",
          law_ok,
          "(so the determinant is a READABLE diagnostic, not a binary test)")

    zD = q**3 / (q**2 + 1)
    kills111 = [r for r, _ in roots if sp.simplify(Y[2].subs(Z, r)) == 0]
    check("both_of_my_two_row_roots_appear_in_the_determinant",
          any(sp.simplify(r - q) == 0 for r in kills111)
          and any(sp.simplify(r - zD) == 0 for r in kills111),
          "(z = q is the sibling's FIRST factor (z-q)^5, which their note did "
          "not flag — mutual corroboration of the completeness result)")
    check("det_G_eq_zero_is_NOT_SUFFICIENT_for_the_two_row_condition",
          len(kills111) < len(roots),
          f"({len(kills111)} of {len(roots)} roots kill (1,1,1); at z = -1/q "
          "and z = -1/(q³+q) the antisymmetric block SURVIVES)")
    check("but_the_named_FACTOR_alone_IS_a_complete_test_for_z_D_CONTROL",
          sp.simplify(sp.solve((q**2 + 1) * Z - q**3, Z)[0] - zD) == 0,
          "(so the sibling's claim is correct on the charitable reading — the "
          "FACTOR pins z_D exactly; it is the determinant-vanishing reading "
          "that over-admits)")

    w.add_data("gram_determinant", str(det))
    w.add_data("roots", rows)
    w.add_data("block_dims", {LABELS[k]: DIMS[k] for k in range(3)})
    w.add_data("markov_convention",
               "convention-free — z is symbolic; the D pin appears as one root")
    w.add_data("assertion_notes", notes)

    verdict = (
        "The sibling's H_3 Markov Gram determinant is re-derived here "
        "independently (ratio exactly 1) from this branch's Ocneanu trace, and "
        "its four roots are identified with the blocks they annihilate. Two "
        "results run in opposite directions. CORROBORATION: the determinant's "
        "FIRST factor (z-q)^5 is the second root of y_(1,1,1)(z) = 0 that this "
        "branch found by solving the two-row condition -- so their "
        "factorisation independently contains the completeness result, and "
        "their note flagged only the third factor. CORRECTION: det G = 0 is "
        "NECESSARY BUT NOT SUFFICIENT for the two-row condition -- of the four "
        "roots only two kill (1,1,1), and at z = -1/q and z = -1/(q^3+q) the "
        "antisymmetric block survives. On the charitable reading the sibling "
        "means the FACTOR ((q^2+1)z - q^3), and that reading is exactly right; "
        "it is 'the determinant vanishing is the test' that over-admits. "
        "THE LAW: each root's multiplicity equals the sum of dim(lambda)^2 over "
        "the blocks whose weight vanishes there (1, 5 = 4+1, 5 = 4+1, 1), which "
        "turns the determinant from a binary test into a readable diagnostic -- "
        "the D pin is the multiplicity-1 root that kills (1,1,1) alone. "
        "Scope-(a); nothing wired."
        if all(ok) else
        "INCONCLUSIVE -- an assertion failed; re-derive before citing.")
    w.add_data("verdict", verdict)
    path = w.save()
    print(f"\n{verdict}\n\nWitness: {path}")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
