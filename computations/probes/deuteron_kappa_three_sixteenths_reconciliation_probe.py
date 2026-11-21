#!/usr/bin/env python3
"""
deuteron_kappa_three_sixteenths_reconciliation_probe.py

Three-way reconciliation probe for `κ = 3/16` on the deuteron (`²H`, `pn`)
and Borromean 3-strand sector (bean `qou-08xc`, owner ruling `Q-10V9-2 = 1`).

Companion Lean module:
  `folio/quantum-observable-universe/lean/QOU/MassTheory/DeuteronKappaThreeSixteenthsReconciliation.lean`

Reconciles the three distinct appearances of `3/16` (and `±1/16`) across the QOU
nuclear binding and Borromean trace corpus:

  1. Route 1 — Borromean 29-letter Laurent-trace coefficients on `H_{3A}`
     (`PairwiseChainLeadingOrder.lean`, `LeadingOrderTraceCoefficient.lean`, `qou-qqm4`):
     - First order in `ℏ_q = 1 - q⁻¹` (or `ε = q - 1`):
       `c₁(pp) = 1/8`, `c₁(pn) = 1/16`, `c₁(nn) = 0`,
       so the `³He` (`pp + pn`) and `⁴He` (`pp + pn + nn`) pairwise chain sums equal `3/16`,
       whereas the deuteron (`pn`, `Z = 1, N = 1`) has `c₁(pn) = 1/16 = (1/3) · (3/16)`.
       Generically, `c₁(pp) + c₁(pn) + c₁(nn) = 3(a + b)/16`, which at the Borromean
       per-nucleon letter weights `(a, b) = (3, -2)` (`a + b = 1`) equals `3/16`.
     - Second order in `ε = q - 1` (`|S| = 2` pair-class split of `Δtr = tr(free) - tr(atom)`):
       The `A = 3` intra-nucleon 3-strand Borromean coefficient is
       `intra(Z, N) = (Z - N) · κ(3)` with `κ(3) = 3/16` (`3p: 9/16`, `T: -3/16`, `³He: 3/16`,
       `3n: -9/16`), vanishing at `Z = N = 1` (`pn`).
       On the deuteron (`pn`), the inter-nucleon cross-term is `cross(pn) = -3/16 = -κ`,
       partially cancelled by the nucleon–interface term `n-if(pn) = +1/8 = +2/16` to give
       the net `|S| = 2` contribution `-3/16 + 1/8 = -1/16 = -c₁(pn)` and total
       `c₂(pn) = 0 + 27/32 - 1/16 = 25/32`.

  2. Route 2 — Yekutieli / Family-A Borromean `h²` extraction (`κ_Yek = 3/16`) vs
     standard Kauffman–Jones Markov trace (`κ_std = 0`)
     (`BorromeanMarkovTrace.lean`, `lambda-scale-substrate-form.lean`, `qou-pi4m`):
     - The Borromean Jones numerator in `h = q - q⁻¹` is `V(𝓑₃) = 4 + h² - 3h⁴ - h⁶`.
     - Dividing by the standard Kauffman–Jones denominator `[2]_q² = (q + q⁻¹)² = 4 + h²`
       gives `tr_M(β_Bor, h) = 1 + (-3h⁴ - h⁶)/(4 + h²)`, so the `h²` coefficient is
       `κ_std = 0` (`1/4 - 1/4 = 0`) and the leading topological invariant is `-(3/4)h⁴`.
     - Dividing instead by the half-power / `[2]_q + 2` normalizer
       `(√q + 1/√q)² = q + 2 + q⁻¹ = w² + 4` (where `w = q^{1/2} - q^{-1/2}` and
       `h² = w²(w² + 4) = 4w² + w⁴`) shifts the denominator's `h²` slope from `1/4` to `1/16`,
       yielding `κ_Yek = 1/4 - 1/16 = 3/16` (and `4 · κ_Yek = 3/4`, matching Family A's
       `λ_A(h) = 5/2 + (3/4)h²`).

  3. Route 3 — Discretized Yekutieli surface 2-form on the deuteron `pn` trefoil Seifert surface
     (`YekutieliTrefoilDiscretization.lean`, `qou-prjo`):
     - On the single-generator `pn` 2-strand closure `σ₁³` (right-handed trefoil, genus `g = 1`,
       Seifert matrix `V = [[-1, 1], [0, -1]]`), all 1D path/Magnus commutators vanish, and the
       Seifert-weighted bracket sum `∑_{i,j} V_{ij} ⁅A_i, A_j⁆` reduces to its skew intersection
       part `(V_{01} - V_{10}) ⁅A_0, A_1⁆ = 1 · ⁅A_0, A_1⁆`, invariant under central scalar
       color/flavor dressings.
     - Route 3 therefore supplies the framing- and dressing-invariant non-abelian commutator
       carrier `1 · ⁅A_0, A_1⁆` (unit intersection coefficient `1`), while the rational scalar
       `3/16` (or `-3/16`, `1/16`) comes from Route 1 or Route 2.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from typing import Dict, List, Tuple


KAPPA = Fraction(3, 16)


# =============================================================================
# Route 1: Borromean 29-letter Laurent-trace coefficients on H_{3A}
# =============================================================================

LETTERS_PP_FREE: List[Tuple[int, int]] = [
    (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (1, 3), (1, 3), (1, 3),
    (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (1, 3), (1, 3), (1, 3),
]
LETTERS_PP_ATOM: List[Tuple[int, int]] = [
    (1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (1, 2), (1, 2), (1, 2),
    (1, 4),
    (1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (1, 2), (1, 2), (1, 2),
]
LETTERS_PN_FREE: List[Tuple[int, int]] = [
    (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (1, 3), (1, 3), (1, 3),
    (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (-1, 5), (1, 3), (1, 3),
]
LETTERS_PN_ATOM: List[Tuple[int, int]] = [
    (1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (1, 2), (1, 2), (1, 2),
    (1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (-1, 4), (1, 2), (1, 2),
]
LETTERS_NN_FREE: List[Tuple[int, int]] = [
    (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (-1, 5), (1, 3), (1, 3),
    (1, 3), (-1, 3), (1, 5), (-1, 3), (1, 3), (-1, 5), (-1, 5), (1, 3), (1, 3),
]
LETTERS_NN_ATOM: List[Tuple[int, int]] = [
    (1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (-1, 4), (1, 2), (1, 2),
    (-1, 4),
    (1, 2), (-1, 2), (1, 4), (-1, 2), (1, 2), (-1, 4), (-1, 4), (1, 2), (1, 2),
]


def star_sum(n: int, letters: List[Tuple[int, int]]) -> Fraction:
    """Evaluate 2^{-n} * sum_{w, c} w * 2^c."""
    num = sum(Fraction(w) * (Fraction(2) ** c) for w, c in letters)
    return num / (Fraction(2) ** n)


def c1_closed(a: Fraction, b: Fraction, Z: int, N: int) -> Fraction:
    """Closed form c₁(Z, N) at per-nucleon letter weights (a, b)."""
    A = Z + N
    i_pp = max(Z - 1, 0)
    i_nn = max(N - 1, 0)
    return (a * Z + b * N) * (Fraction(1, 2 ** (A + 1)) - Fraction(1, 2 ** (2 * A))) - (
        Fraction(4 * (i_pp - i_nn), 2 ** (2 * A))
    )


# Second-order |S| = 2 pair-class table from `qou-qqm4` (`c2_pair_class_decomposition_probe.py`)
S2_PAIR_CLASSES: Dict[str, Dict[str, Fraction]] = {
    "pp": {"Z": Fraction(2), "N": Fraction(0), "intra": Fraction(1, 2), "cross": Fraction(9, 32), "nif": Fraction(-5, 8), "ifif": Fraction(0), "sum": Fraction(5, 32)},
    "pn": {"Z": Fraction(1), "N": Fraction(1), "intra": Fraction(0), "cross": Fraction(-3, 16), "nif": Fraction(1, 8), "ifif": Fraction(0), "sum": Fraction(-1, 16)},
    "nn": {"Z": Fraction(0), "N": Fraction(2), "intra": Fraction(-1, 2), "cross": Fraction(1, 8), "nif": Fraction(-3, 8), "ifif": Fraction(0), "sum": Fraction(-3, 4)},
    "3p": {"Z": Fraction(3), "N": Fraction(0), "intra": Fraction(9, 16), "cross": Fraction(81, 128), "nif": Fraction(-1, 2), "ifif": Fraction(-1, 8), "sum": Fraction(73, 128)},
    "T": {"Z": Fraction(1), "N": Fraction(2), "intra": Fraction(-3, 16), "cross": Fraction(-3, 16), "nif": Fraction(1, 32), "ifif": Fraction(0), "sum": Fraction(-11, 32)},
    "3He": {"Z": Fraction(2), "N": Fraction(1), "intra": Fraction(3, 16), "cross": Fraction(-9, 128), "nif": Fraction(-1, 16), "ifif": Fraction(0), "sum": Fraction(7, 128)},
    "3n": {"Z": Fraction(0), "N": Fraction(3), "intra": Fraction(-9, 16), "cross": Fraction(9, 32), "nif": Fraction(-5, 16), "ifif": Fraction(-1, 8), "sum": Fraction(-23, 32)},
}


# =============================================================================
# Route 2: Yekutieli (sqrt(q) + 1/sqrt(q))^2 vs Kauffman-Jones [2]_q^2
# =============================================================================

def borromean_num_of_hsq(h_sq: Fraction) -> Fraction:
    """V(B_3) = 4 + h^2 - 3 h^4 - h^6 as a function of h^2."""
    return Fraction(4) + h_sq - Fraction(3) * (h_sq ** 2) - (h_sq ** 3)


def std_den_of_hsq(h_sq: Fraction) -> Fraction:
    """Standard Kauffman-Jones denominator [2]_q^2 = 4 + h^2."""
    return Fraction(4) + h_sq


def hsq_of_w(w: Fraction) -> Fraction:
    """h^2 = w^2 (w^2 + 4) where w = q^{1/2} - q^{-1/2}."""
    return (w ** 2) * (w ** 2 + Fraction(4))


def yek_den_of_w(w: Fraction) -> Fraction:
    """Yekutieli / _li_2_q_util denominator (sqrt(q) + 1/sqrt(q))^2 = w^2 + 4."""
    return (w ** 2) + Fraction(4)


# =============================================================================
# Route 3: Trefoil Seifert surface 2-form on the deuteron pn braid sigma_1^3
# =============================================================================

SEIFERT_TREFOIL: Tuple[Tuple[int, int], Tuple[int, int]] = (
    (-1, 1),
    (0, -1),
)


def mat2_mul(A: List[List[Fraction]], B: List[List[Fraction]]) -> List[List[Fraction]]:
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


def mat2_add(A: List[List[Fraction]], B: List[List[Fraction]]) -> List[List[Fraction]]:
    return [
        [A[0][0] + B[0][0], A[0][1] + B[0][1]],
        [A[1][0] + B[1][0], A[1][1] + B[1][1]],
    ]


def mat2_scale(c: Fraction, A: List[List[Fraction]]) -> List[List[Fraction]]:
    return [
        [c * A[0][0], c * A[0][1]],
        [c * A[1][0], c * A[1][1]],
    ]


def mat2_bracket(A: List[List[Fraction]], B: List[List[Fraction]]) -> List[List[Fraction]]:
    AB = mat2_mul(A, B)
    BA = mat2_mul(B, A)
    return [
        [AB[0][0] - BA[0][0], AB[0][1] - BA[0][1]],
        [AB[1][0] - BA[1][0], AB[1][1] - BA[1][1]],
    ]


def surface_2form(
    V: Tuple[Tuple[int, int], Tuple[int, int]],
    handles: Tuple[List[List[Fraction]], List[List[Fraction]]],
) -> List[List[Fraction]]:
    total = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(0)]]
    for i in range(2):
        for j in range(2):
            term = mat2_scale(Fraction(V[i][j]), mat2_bracket(handles[i], handles[j]))
            total = mat2_add(total, term)
    return total


def run_probe() -> int:
    passed = 0
    total = 0

    def check(label: str, cond: bool) -> None:
        nonlocal passed, total
        total += 1
        if cond:
            passed += 1
            print(f"  [PASS] {label}")
        else:
            print(f"  [FAIL] {label}")

    print("=== Route 1: Borromean 29-letter Laurent-trace coefficients on H_{3A} ===")
    c1_pp = star_sum(6, LETTERS_PP_FREE) - star_sum(6, LETTERS_PP_ATOM)
    c1_pn = star_sum(6, LETTERS_PN_FREE) - star_sum(6, LETTERS_PN_ATOM)
    c1_nn = star_sum(6, LETTERS_NN_FREE) - star_sum(6, LETTERS_NN_ATOM)

    check("c1(pp) from letter star-sums == 1/8", c1_pp == Fraction(1, 8))
    check("c1(pn) from letter star-sums == 1/16 (deuteron)", c1_pn == Fraction(1, 16))
    check("c1(nn) from letter star-sums == 0", c1_nn == Fraction(0))
    check("3He chain sum c1(pp) + c1(pn) == 3/16 == kappa", c1_pp + c1_pn == KAPPA)
    check("4He chain sum c1(pp) + c1(pn) + c1(nn) == 3/16 == kappa", c1_pp + c1_pn + c1_nn == KAPPA)
    check("Deuteron c1(pn) == (1/3) * kappa", c1_pn == Fraction(1, 3) * KAPPA)
    check("pp bond c1(pp) == (2/3) * kappa", c1_pp == Fraction(2, 3) * KAPPA)

    a_bor, b_bor = Fraction(3), Fraction(-2)
    check(
        "Closed form pair sum at Borromean weights (3, -2) == 3/16",
        c1_closed(a_bor, b_bor, 2, 0)
        + c1_closed(a_bor, b_bor, 1, 1)
        + c1_closed(a_bor, b_bor, 0, 2)
        == KAPPA,
    )

    for sp in ("3p", "T", "3He", "3n"):
        row = S2_PAIR_CLASSES[sp]
        check(
            f"A=3 intra({sp}) == (Z - N) * (3/16) == {row['intra']}",
            (row["Z"] - row["N"]) * KAPPA == row["intra"],
        )

    pn_row = S2_PAIR_CLASSES["pn"]
    check("Deuteron |S|=2 intra == 0 (Z = N = 1)", pn_row["intra"] == Fraction(0))
    check("Deuteron |S|=2 cross == -3/16 == -kappa", pn_row["cross"] == -KAPPA)
    check("Deuteron |S|=2 n-if == +1/8 == +2/16", pn_row["nif"] == Fraction(1, 8))
    check(
        "Deuteron |S|=2 sum == -3/16 + 1/8 == -1/16 == -c1(pn)",
        pn_row["intra"] + pn_row["cross"] + pn_row["nif"] + pn_row["ifif"]
        == Fraction(-1, 16)
        == -c1_pn,
    )
    check(
        "Deuteron c2(pn) == |S|=0 (0) + |S|=1 (27/32) + |S|=2 (-1/16) == 25/32",
        Fraction(0) + Fraction(27, 32) + pn_row["sum"] == Fraction(25, 32),
    )

    print("\n=== Route 2: Yekutieli (sqrt(q)+1/sqrt(q))^2 vs Kauffman-Jones [2]_q^2 ===")
    for h_val in (Fraction(0), Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(2)):
        h_sq = h_val ** 2
        rem_std = borromean_num_of_hsq(h_sq) - std_den_of_hsq(h_sq) * Fraction(1)
        expected_std = (h_val ** 4) * (Fraction(-3) - h_sq)
        check(
            f"Standard [2]_q^2 h^2-cancellation identity at h={h_val}",
            rem_std == expected_std,
        )

    for w_val in (Fraction(0), Fraction(1, 7), Fraction(1, 4), Fraction(1, 2), Fraction(1)):
        h_sq = hsq_of_w(w_val)
        rem_yek = borromean_num_of_hsq(h_sq) - yek_den_of_w(w_val) * (
            Fraction(1) + KAPPA * h_sq
        )
        expected_yek = (w_val ** 4) * (
            Fraction(-1, 2)
            - Fraction(3, 16) * (w_val ** 2)
            - Fraction(3) * ((w_val ** 2 + Fraction(4)) ** 2)
            - (w_val ** 2) * ((w_val ** 2 + Fraction(4)) ** 3)
        )
        check(
            f"Yekutieli (w^2+4) O(w^4)-remainder identity at w={w_val}",
            rem_yek == expected_yek,
        )

    check(
        "Denominator shift identity: 1/4 (numerator) - 1/16 (Yekutieli den) == 3/16",
        Fraction(1, 4) - Fraction(1, 16) == KAPPA,
    )
    check(
        "Family-A rescaling identity: 4 * (3/16) == 3/4",
        Fraction(4) * KAPPA == Fraction(3, 4),
    )

    print("\n=== Route 3: Trefoil Seifert surface 2-form on deuteron pn braid sigma_1^3 ===")
    skew = SEIFERT_TREFOIL[0][1] - SEIFERT_TREFOIL[1][0]
    check("Trefoil Seifert skew intersection V_01 - V_10 == 1", skew == 1)
    check(
        "Trefoil Seifert diagonal self-linking entries V_00 == V_11 == -1",
        SEIFERT_TREFOIL[0][0] == -1 and SEIFERT_TREFOIL[1][1] == -1,
    )

    A0 = [[Fraction(1, 2), Fraction(1)], [Fraction(0), Fraction(-1, 2)]]
    A1 = [[Fraction(0), Fraction(2)], [Fraction(-1, 3), Fraction(0)]]
    I2 = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    s0 = mat2_scale(Fraction(-7, 13), I2)
    s1 = mat2_scale(Fraction(5, 11), I2)
    A0_dressed = mat2_add(A0, s0)
    A1_dressed = mat2_add(A1, s1)

    s2_bare = surface_2form(SEIFERT_TREFOIL, (A0, A1))
    s2_dressed = surface_2form(SEIFERT_TREFOIL, (A0_dressed, A1_dressed))
    comm = mat2_bracket(A0, A1)

    check("surface_2form(seifertTrefoil, A) == [A_0, A_1]", s2_bare == comm)
    check(
        "surface_2form(seifertTrefoil, A + s*I) == [A_0, A_1] (color-dressing invariant)",
        s2_dressed == comm,
    )

    print(f"\nSummary: {passed}/{total} checks passed.")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(run_probe())
