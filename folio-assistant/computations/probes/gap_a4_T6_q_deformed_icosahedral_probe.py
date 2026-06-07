#!/usr/bin/env python3
"""GAP-A-4 T6 probe — q-deformation of the icosahedral character matrix.

After T4 confirmed claim (2) (5-strand A_5-Hecke matching at q=1) and T5
REFUTED 3 candidate functors to the 3-strand H_3 Borromean h⁴ = −3/4,
this probe tabulates the q-deformed per-A_5-irrep weights and extracts
their h-expansions to see whether the SO(3) icosahedral H-sector carries
any structural h⁴ pattern OF ITS OWN (regardless of the 3-strand link).

For each A_n-irrep R (n=4: tetrahedral, n=5: icosahedral) define the
per-irrep dim_q weight

  Q_R(q) := Σ_{λ ⊢ n} dim_q(V_λ) · mult_R(λ)

where mult_R(λ) is the integer Schur-Weyl multiplicity from T4 (classical
A_n character branching at q=1).  Q_R(q) is the natural q-deformed
"icosahedral character entry" for irrep R weighted by Wedderburn
multiplicity — the matrix elements of the closed-form decomposition
T4 verified.

Tests:

  (a) Sum identity at q_0:
      Σ_R Q_R(q_0) ≟ Σ_{λ⊢n} dim_q(V_λ)
      (matrix re-summation; sanity check the decomposition.)

  (b) h-expansion of each Q_R(q) at small h via algebraic
      closed-forms: extract h⁰, h², h⁴ coefficients.

  (c) The icosahedral H-sector specifically:
      Q_H(q) = dim_q((3,2)) + dim_q((2,2,1)) = 2·[5]_q
             = 2·(h⁴ + 5h² + 5)
             = 10 + 10h² + 2h⁴   (closed form)
      h⁴ coefficient = +2.  NOT structurally related to the
      Borromean −3/4 from H_3.  This complements T5 — even at
      the H-sector level, the h⁴ coefficient lives in a different
      magnitude regime than the 3-strand Borromean one.

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-T6-q-deformed-icosahedral-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402

# Centralised q=1-safe q-integer / dim_q helpers + Q_0_50DPS
# (addresses Gemini deduplication review on PR #1904).
from _gap_a4_qsafe import (  # noqa: E402
    Q_0_50DPS,
    dim_q_partition,
)

from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent


# ── A_n integer multiplicities (from T4) ──────────────────────────


# S_4 partitions × A_4 irreps [trivial, ω, ω², T(3)]
S4_TO_A4_MULT = {
    (4,):           [1, 0, 0, 0],
    (3, 1):         [0, 0, 0, 1],
    (2, 2):         [0, 1, 1, 0],
    (2, 1, 1):      [0, 0, 0, 1],
    (1, 1, 1, 1):   [1, 0, 0, 0],
}
A4_IRREPS = ["A(1)", "ω(1)", "ω²(1)", "T(3)"]
A4_DIMS = [1, 1, 1, 3]

# S_5 partitions × A_5 irreps [A(1), T_1(3), T_2(3), G(4), H(5)]
S5_TO_A5_MULT = {
    (5,):              [1, 0, 0, 0, 0],
    (4, 1):            [0, 0, 0, 1, 0],
    (3, 2):            [0, 0, 0, 0, 1],
    (3, 1, 1):         [0, 1, 1, 0, 0],
    (2, 2, 1):         [0, 0, 0, 0, 1],
    (2, 1, 1, 1):      [0, 0, 0, 1, 0],
    (1, 1, 1, 1, 1):   [1, 0, 0, 0, 0],
}
A5_IRREPS = ["A(1)", "T_1(3)", "T_2(3)", "G(4)", "H(5)"]
A5_DIMS = [1, 3, 3, 4, 5]


def per_irrep_dim_q_sums(s_to_a_mult: dict, irreps: list,
                          q_0: mp.mpf) -> list:
    """Σ_λ dim_q(V_λ) · mult_R(λ) for each A_n irrep R."""
    out = [mp.mpf(0)] * len(irreps)
    for lam, mults in s_to_a_mult.items():
        dq = dim_q_partition(lam, q_0)
        for i, m in enumerate(mults):
            out[i] += dq * m
    return out


# ── h-expansion via small-h sampling + least-squares ──────────────


def h_expansion(f, hs: list, max_order: int) -> list:
    """Fit f(h) = c_0 + c_1·h² + c_2·h⁴ + ... + c_{max_order}·h^{2·max_order}
    via least-squares on samples at h-values hs.  Returns [c_0, c_1, ...].
    """
    n = len(hs)
    cols = max_order + 1
    rows = []
    rhs = []
    for h_val in hs:
        rows.append([h_val ** (2 * k) for k in range(cols)])
        rhs.append(f(h_val))
    A = mp.matrix(rows)
    b = mp.matrix(rhs)
    AT = A.transpose()
    coeffs = mp.lu_solve(AT * A, AT * b)
    return [coeffs[k] for k in range(cols)]


def dim_q_at_h(lam: tuple, h_val: mp.mpf) -> mp.mpf:
    """dim_q(V_λ) evaluated as a function of h = q - q⁻¹.  Uses
    q = (h + √(h²+4))/2."""
    q_h = (h_val + mp.sqrt(h_val * h_val + 4)) / 2
    return dim_q_partition(lam, q_h)


def per_irrep_at_h(s_to_a_mult: dict, irrep_idx: int,
                   h_val: mp.mpf) -> mp.mpf:
    """Q_R(h) = Σ_λ dim_q(V_λ)(h) · mult_R(λ)."""
    out = mp.mpf(0)
    for lam, mults in s_to_a_mult.items():
        if mults[irrep_idx] == 0:
            continue
        out += dim_q_at_h(lam, h_val) * mults[irrep_idx]
    return out


# ── Test runners ──────────────────────────────────────────────────


def transpose_partition(lam: tuple) -> tuple:
    """Conjugate (transpose) partition λ^T."""
    if not lam:
        return ()
    return tuple(sum(1 for r in lam if r > k) for k in range(max(lam)))


def test_per_irrep_table(s_to_a_mult: dict, irreps: list, dims: list,
                         q_0: mp.mpf, label: str) -> dict:
    print("=" * 78)
    print(f"{label} — q-deformed icosahedral matrix (per-irrep dim_q sums)")
    print("=" * 78)

    Q_at_q0 = per_irrep_dim_q_sums(s_to_a_mult, irreps, q_0)
    Q_at_q1 = per_irrep_dim_q_sums(s_to_a_mult, irreps, mp.mpf(1))

    # h-expansion of each Q_R(h)
    hs = [mp.mpf("1e-2") * k for k in range(1, 8)]
    h_exp = []
    for i in range(len(irreps)):
        coeffs = h_expansion(
            lambda h, i=i: per_irrep_at_h(s_to_a_mult, i, h),
            hs, max_order=2,
        )
        h_exp.append(coeffs)

    print(f"  {'irrep':<8} {'dim':>4} {'Q_R(q=1)':>11} "
          f"{'Q_R(q_0)':>13} {'h⁰':>10} {'h²':>10} {'h⁴':>10}")
    print("-" * 78)
    for i, (name, d) in enumerate(zip(irreps, dims)):
        h0, h2, h4 = h_exp[i]
        print(f"  {name:<8} {d:>4} {mp.nstr(Q_at_q1[i], 8):>11} "
              f"{mp.nstr(Q_at_q0[i], 10):>13} "
              f"{mp.nstr(h0, 6):>10} {mp.nstr(h2, 6):>10} "
              f"{mp.nstr(h4, 6):>10}")
    sum_Q_q0 = sum(Q_at_q0)
    sum_dimq = sum(
        dim_q_partition(lam, q_0) for lam in s_to_a_mult
    )
    # Self-conjugate partitions split under Res^{S_n}_{A_n} via
    # Clifford theory: their Σ_R mult_R = 2 (two conjugate A_n irreps)
    # rather than 1.  So Σ_R Q_R = Σ_λ dim_q·(Σ_R mult_R) overshoots
    # Σ_λ dim_q by exactly Σ_{λ=λ^T} dim_q(λ).
    self_conj = [lam for lam in s_to_a_mult
                 if transpose_partition(lam) == lam]
    self_conj_dimq_sum = sum(
        dim_q_partition(lam, q_0) for lam in self_conj
    )
    expected_excess = self_conj_dimq_sum
    actual_excess = sum_Q_q0 - sum_dimq
    print(f"  Σ_R Q_R(q_0) = {mp.nstr(sum_Q_q0, 10)}")
    print(f"  Σ_λ dim_q(q_0) = {mp.nstr(sum_dimq, 10)}")
    print(f"  Excess = {mp.nstr(actual_excess, 10)}  "
          f"(= dim_q of self-conj λ ∈ {self_conj}: "
          f"{mp.nstr(expected_excess, 10)})")
    excess_match = abs(actual_excess - expected_excess) < mp.mpf("1e-30")
    print(f"  Clifford excess identity: {'✓' if excess_match else '✗ DRIFT'}")
    return {
        "irreps": list(irreps),
        "dims": list(dims),
        "Q_R_at_q1": [str(x) for x in Q_at_q1],
        "Q_R_at_q0": [str(x) for x in Q_at_q0],
        "h_expansion_coeffs_per_irrep": [
            {"h0": str(c[0]), "h2": str(c[1]), "h4": str(c[2])}
            for c in h_exp
        ],
        "self_conjugate_partitions": [list(l) for l in self_conj],
        "self_conjugate_dimq_sum": str(self_conj_dimq_sum),
        "clifford_excess_identity_holds": excess_match,
        "sum_Q_at_q0": str(sum_Q_q0),
        "sum_dimq_at_q0": str(sum_dimq),
        "actual_excess": str(actual_excess),
    }


def test_H_sector_closed_form() -> dict:
    print()
    print("=" * 78)
    print("Q_H(q) — icosahedral H-sector closed-form expansion")
    print("=" * 78)
    # Both (3,2) and (2,2,1) contribute to H with mult 1; both have
    # dim_q = [5]_q.  So Q_H = 2·[5]_q.
    # [5]_q = q⁴ + q² + 1 + q⁻² + q⁻⁴.  In s = q + q⁻¹, s² = h²+4:
    #   [5]_q = s⁴ − 3s² + 1 = (h²+4)² − 3(h²+4) + 1
    #         = h⁴ + 8h² + 16 − 3h² − 12 + 1 = h⁴ + 5h² + 5
    # Q_H(q) = 2·[5]_q = 2h⁴ + 10h² + 10.
    print("  Closed form: Q_H(q) = dim_q((3,2)) + dim_q((2,2,1)) "
          "= 2·[5]_q")
    print("              [5]_q = h⁴ + 5h² + 5  (via s = q+q⁻¹, "
          "s² = h²+4)")
    print("              Q_H(q) = 2h⁴ + 10h² + 10")
    print()
    print("  h⁰ coefficient: +10  (= 2·dim(H) = 2·5)")
    print("  h² coefficient: +10")
    print("  h⁴ coefficient:  +2  ← structural H-sector h⁴")
    print()
    print("  Comparison to Borromean H_3 (DIFFERENT group algebra):")
    print("    tr_M(β_Bor) h⁴ coefficient = −3/4   (on H_3)")
    print("    Q_H(q)      h⁴ coefficient = +2     (on H_5, dim_q-summed)")
    print(f"    Ratio: (+2)/(−3/4) = {float(mp.mpf(2)/mp.mpf('-0.75'))}  "
          "= −8/3 (no clean structural interpretation)")
    return {
        "Q_H_closed_form": "2·[5]_q = 2h⁴ + 10h² + 10",
        "h0_coeff": 10,
        "h2_coeff": 10,
        "h4_coeff": 2,
        "comparison": (
            "Q_H(q) h⁴ = +2 (on H_5) vs Borromean h⁴ = −3/4 (on H_3); "
            "ratio −8/3 not structurally interpretable — different "
            "group algebras, confirms T5 negative."
        ),
    }


# ── main ─────────────────────────────────────────────────────────


def main():
    mp.mp.dps = 50
    w = WitnessBuilder(
        "gap-a4-T6-q-deformed-icosahedral-probe",
        engine="mpmath",
    )
    w.set_audit_only("docs/audits/2026-06-01-s5-so3-su2-u1-fiber-action.md")
    w.set_description(
        "GAP-A-4 T6 — q-deformed icosahedral character matrix. "
        "Tabulates per-A_n-irrep dim_q sums Q_R(q) for n=4 (A_4) and "
        "n=5 (A_5), extracts h⁰/h²/h⁴ coefficients, and shows Q_H(q) "
        "= 2·[5]_q has h⁴ coefficient +2 — NOT the Borromean −3/4 "
        "(which lives on H_3 not H_5). Complements T5 by exhibiting "
        "the H-sector's OWN h⁴ structure for comparison."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)

    print(f"  q₀ = {Q_0_50DPS[:18]}...")
    print()

    a4_result = test_per_irrep_table(
        S4_TO_A4_MULT, A4_IRREPS, A4_DIMS, q_0,
        "A_4 (tetrahedral)",
    )
    print()
    a5_result = test_per_irrep_table(
        S5_TO_A5_MULT, A5_IRREPS, A5_DIMS, q_0,
        "A_5 (icosahedral)",
    )
    h_sector = test_H_sector_closed_form()

    w.add_data("A4_per_irrep_table", a4_result)
    w.add_data("A5_per_irrep_table", a5_result)
    w.add_data("H_sector_closed_form", h_sector)

    w.add_assertion(
        "A4_clifford_excess_identity",
        # Compute the difference in mp.mpf to preserve the precise
        # cancellation (float64 leaves ~1e-15 residue that breaks
        # tolerance=1e-30, per Copilot #2050 review). The assertion
        # API accepts mp.mpf numeric directly.
        computed=(mp.mpf(a4_result["actual_excess"])
                  - mp.mpf(a4_result["self_conjugate_dimq_sum"])),
        expected=0.0,
        tolerance=1e-30,
        source=(
            "Σ_R Q_R(q_0) − Σ_λ dim_q(q_0) for A_4 equals "
            "dim_q of self-conjugate partition (2,2): Clifford theory "
            "splits S^{(2,2)} into ω ⊕ ω² under A_4, so Σ_R mult_R((2,2)) "
            "= 2 and the excess in the row-sum is exactly dim_q((2,2))."
        ),
    )
    w.add_assertion(
        "A5_clifford_excess_identity",
        # Same as A4 above — mp.mpf cancellation preserves the
        # tight tolerance=1e-30 (Copilot #2050).
        computed=(mp.mpf(a5_result["actual_excess"])
                  - mp.mpf(a5_result["self_conjugate_dimq_sum"])),
        expected=0.0,
        tolerance=1e-30,
        source=(
            "Σ_R Q_R(q_0) − Σ_λ dim_q(q_0) for A_5 equals "
            "dim_q((3,1,1)) — the unique self-conjugate partition of 5, "
            "which Clifford-splits into T_1 ⊕ T_2 under A_5."
        ),
    )

    synthesis = (
        "Q_R(q) = Σ_λ dim_q(V_λ)·mult_R(λ) defines the q-deformed "
        "icosahedral character matrix's row sums; for A_5 the H-sector "
        "Q_H(q) = 2·[5]_q has closed-form h-expansion 10 + 10h² + 2h⁴ "
        "(by algebraic identity [5]_q = h⁴+5h²+5). The structural h⁴ "
        "coefficient is +2 — DIFFERENT in sign AND magnitude from the "
        "Borromean H_3 reference h⁴ = −3/4. This complements T5: the "
        "H-sector carries its own h⁴ structure, but in a different "
        "group algebra than the Borromean trace coefficient — the "
        "ratio +2/(−3/4) = −8/3 has no clean structural meaning. "
        "The Clifford excess identity Σ_R Q_R − Σ_λ dim_q = dim_q(λ_self-conj) "
        "holds to machine precision for both A_4 (excess = dim_q((2,2))) "
        "and A_5 (excess = dim_q((3,1,1))) — this is the Wedderburn "
        "decomposition's q-deformed signature: self-conjugate partitions "
        "split into 2 conjugate A_n irreps under Res^{S_n}_{A_n}, and the "
        "excess weighting tracks this splitting at q ≠ 1. The q-deformed "
        "icosahedral matrix is a well-defined object at q_0; its H-sector's "
        "h⁴ structure is internally clean but NOT linked to the 3-strand h⁴ "
        "obstruction."
    )
    w.add_data("synthesis_verdict", synthesis)

    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    out_path = w.save()
    print()
    print(f"  Wrote witness: {out_path}")


if __name__ == "__main__":
    main()
