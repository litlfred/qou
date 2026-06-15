#!/usr/bin/env python3
"""GAP-A-4 T17 probe — Schur-Weyl R-matrix derivation of tr_{V⊗3}(β_Bor).

Follow-up to T15 (polynomial closed form χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶)
and T16 (combinatorial-coincidence observations).  T17 is the FIRST
categorical / topological distinguisher in the T4-T17 arc: it derives
the FULL trace of β_Bor on V_{1/2}^⊗3 directly from the U_q(sl_2)
R-matrix action, then cross-checks against the T15 polynomial via
Schur-Weyl block decomposition.

SCHUR-WEYL DECOMPOSITION OF V_{1/2}^⊗3:

  V_{1/2}^⊗3  ≅  V_{3/2} ⊗ S^{(3)}  ⊕  V_{1/2} ⊗ S^{(2,1)}
                 (dim 4 ⊗ dim 1)      (dim 2 ⊗ dim 2)
                 ──── 4 + 4 = 8 ────  ✓

The Hecke H_3(q) action on the right side splits the trace:

  tr_{V^⊗3}(β_Bor) = dim_q(V_{3/2}) · χ^{(3)}(β_Bor)
                   + dim_q(V_{1/2}) · χ^{(2,1)}(β_Bor)

PREDICTION (the testable closed form):

The ORDINARY trace (not the quantum trace) on V^⊗3 — which is the
trace computed by the direct 8×8 R-matrix construction below — splits
under Schur-Weyl with the CLASSICAL integer dimensions of the sl_2
irreps (4 and 2), NOT the q-deformed [4]_q / [2]_q.  This convention
matches the H_n(q)-side classical-dim convention from T8's sl_2
q-Schur centralizer identity ([2]_q^n = Σ dim_q(V_j) · dim(S^λ)
where dim(S^λ) is classical).  Concretely:

  tr_{V^⊗3}(β_Bor) = dim(V_{3/2}) · χ^{(3)}(β_Bor)
                   + dim(V_{1/2}) · χ^{(2,1)}(β_Bor)
                   = 4 · 1  +  2 · (2 − 3h⁴ − h⁶)
                   = 8 − 6h⁴ − 2h⁶

For β_Bor with writhe 0 and image id ∈ S_3, χ^{(3)}(β_Bor) = 1
exactly; per T15, χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶.

At q = 1 (h = 0): tr = 8 = dim V^⊗3 ✓ (identity case).

DIRECT R-MATRIX COMPUTATION (the categorical derivation):

  Build the R-matrix on V⊗V (V = ℂ²_q) as q·P_sym − q⁻¹·P_antisym,
  then σ_1 = R ⊗ I and σ_2 = I ⊗ R as 8×8 matrices on V^⊗3.  Compute
  β_Bor = (σ_1⁻¹ σ_2)^3 by matrix multiplication.  Trace and compare
  to the prediction at q_0 = 1.10998.

If the direct R-matrix trace matches the prediction to 50 dps, T17
provides the FIRST first-principles categorical derivation of the
T15 polynomial form (modulo the Hecke convention factor).

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-T17-schur-weyl-rmatrix-probe.witness.json`.
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
from _gap_a4_qsafe import Q_0_50DPS  # noqa: E402

TOL_50DPS = mp.mpf("1e-40")


# ── R-matrix on V⊗V (V = C²_q) ────────────────────────────────────


def R_matrix(q: mp.mpf):
    """U_q(sl_2) R-matrix on V⊗V (V = ℂ²_q).

    Basis {↑↑, ↑↓, ↓↑, ↓↓}.  Standard form:
      R |↑↑⟩ = q |↑↑⟩
      R |↑↓⟩ = (q − q⁻¹) |↑↓⟩ + |↓↑⟩
      R |↓↑⟩ = |↑↓⟩
      R |↓↓⟩ = q |↓↓⟩
    """
    R = mp.zeros(4, 4)
    R[0, 0] = q
    R[1, 1] = q - 1 / q
    R[1, 2] = mp.mpf(1)
    R[2, 1] = mp.mpf(1)
    R[2, 2] = mp.mpf(0)
    R[3, 3] = q
    return R


def R_inverse_matrix(q: mp.mpf, R=None):
    """R⁻¹ for the BRAIDED R-matrix satisfying the Hecke relation
    R² = (q − q⁻¹)R + I.  Solving for R⁻¹ : R · R⁻¹ = I gives
    R⁻¹ = R − (q − q⁻¹)·I.  (NOT R(q→q⁻¹), which is a common
    mistake — that would be valid only for the UNbraided / universal
    R-matrix, not Ř = τ ∘ R.)  R can be passed in to avoid
    re-computing (Gemini review #1933 optimisation)."""
    if R is None:
        R = R_matrix(q)
    return R - (q - 1 / q) * mp.eye(4)


def kron(A, B):
    """Kronecker product of two mpmath matrices."""
    m, n = A.rows, A.cols
    p, qq = B.rows, B.cols
    out = mp.zeros(m * p, n * qq)
    for i in range(m):
        for j in range(n):
            for k in range(p):
                for ell in range(qq):
                    out[i * p + k, j * qq + ell] = A[i, j] * B[k, ell]
    return out


def matrix_trace(A) -> mp.mpf:
    s = mp.mpf(0)
    for i in range(A.rows):
        s += A[i, i]
    return s


# ── Direct β_Bor on V^⊗3 ──────────────────────────────────────────


def beta_bor_matrix(q: mp.mpf):
    """β_Bor = (σ_1⁻¹ σ_2)^3 acting on V^⊗3 (V = C²_q), as an 8×8 matrix.

    σ_1 = R ⊗ I  (acts on positions 1, 2)
    σ_2 = I ⊗ R  (acts on positions 2, 3)
    Both are 8×8 mpmath matrices.
    """
    R = R_matrix(q)
    Rinv = R_inverse_matrix(q, R)  # reuse R, Gemini review #1933
    I2 = mp.eye(2)
    sigma1_inv = kron(Rinv, I2)  # 8×8
    sigma2 = kron(I2, R)         # 8×8
    one_factor = sigma1_inv * sigma2          # mpmath native *
    return one_factor * one_factor * one_factor


# ── Tests ─────────────────────────────────────────────────────────


def check_rmatrix_hecke_relation(q: mp.mpf) -> dict:
    """Verify the Hecke relation (R − q)(R + q⁻¹) = 0 on V⊗V."""
    print("=" * 78)
    print("T17a — Hecke relation (R − q)(R + q⁻¹) = 0 on V⊗V")
    print("=" * 78)
    R = R_matrix(q)
    I4 = mp.eye(4)
    R_minus_q = R - q * I4
    R_plus_qinv = R + (1 / q) * I4
    product = R_minus_q * R_plus_qinv  # mpmath native *
    max_entry = max(abs(product[i, j]) for i in range(4) for j in range(4))
    print(f"  max |((R − q)(R + q⁻¹))_{{ij}}| = {mp.nstr(max_entry, 14)}")
    holds = max_entry < TOL_50DPS
    print(f"  Hecke relation: {'✓' if holds else '✗'}")
    return {
        "max_residual_entry": str(max_entry),
        "hecke_relation_holds": holds,
    }


def check_direct_vs_schur_weyl(q: mp.mpf) -> dict:
    """Compute β_Bor's trace on V^⊗3 via direct R-matrix; compare to the
    Schur-Weyl prediction tr = 4·χ^{(3)} + 2·χ^{(2,1)} = 8 − 6h⁴ − 2h⁶
    (classical sl_2 dims 4, 2 — not q-deformed [4]_q/[2]_q; see gotcha 1)."""
    print("=" * 78)
    print("T17b — Direct R-matrix vs Schur-Weyl prediction")
    print("=" * 78)
    M = beta_bor_matrix(q)
    tr_direct = matrix_trace(M)
    # Schur-Weyl prediction (ORDINARY trace, not quantum trace):
    # tr_{V^⊗3}(β_Bor) = dim(V_{3/2}) · χ^{(3)}(β_Bor)
    #                  + dim(V_{1/2}) · χ^{(2,1)}(β_Bor)
    # The H_n(q)-side dim in the centralizer is the CLASSICAL integer
    # dim, NOT the q-deformed one — same convention as T8 sl_2 q-Schur
    # centralizer identity [2]_q^n = Σ dim_q(V_j) · dim(S^λ).
    # χ^{(3)}(β_Bor) = 1 exactly (trivial rep, writhe 0).
    # χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶ (T15).
    h = q - 1 / q
    chi_21 = 2 - 3 * h ** 4 - h ** 6
    dim_V_three_half = mp.mpf(4)
    dim_V_one_half = mp.mpf(2)
    tr_pred = dim_V_three_half * 1 + dim_V_one_half * chi_21
    diff = abs(tr_direct - tr_pred)
    print(f"  q_0 = {mp.nstr(q, 12)}")
    print(f"  h_0 = {mp.nstr(h, 12)}")
    print(f"  dim(V_{{3/2}}) · χ^{{(3)}}    = 4 · 1 "
          f"= {mp.nstr(dim_V_three_half, 14)}")
    print(f"  dim(V_{{1/2}}) · χ^{{(2,1)}} = 2 · (2 − 3h⁴ − h⁶) "
          f"= {mp.nstr(dim_V_one_half * chi_21, 14)}")
    print(f"  Schur-Weyl prediction tr   = 8 − 6h⁴ − 2h⁶ = "
          f"{mp.nstr(tr_pred, 14)}")
    print(f"  Direct R-matrix trace      = {mp.nstr(tr_direct, 14)}")
    print(f"  |diff|                     = {mp.nstr(diff, 14)}")
    match = diff < TOL_50DPS
    print(f"  Match: {'✓ (categorical derivation succeeds)' if match else '✗'}")
    return {
        "tr_direct_rmatrix": str(tr_direct),
        "tr_schur_weyl_prediction": str(tr_pred),
        "absolute_difference": str(diff),
        "categorical_derivation_succeeds": match,
        "components": {
            "dim_V_3_2_times_chi_3": str(dim_V_three_half),
            "dim_V_1_2_times_chi_2_1": str(dim_V_one_half * chi_21),
            "chi_2_1_at_q0": str(chi_21),
        },
    }


def check_identity_dim_at_h_zero() -> dict:
    """At h = 0 (q = 1), tr_{V^⊗3}(id) = 8 = dim V^⊗3."""
    print("=" * 78)
    print("T17c — Classical-limit identity check (q = 1)")
    print("=" * 78)
    # At q=1, β_Bor → id and tr = 8.
    M = beta_bor_matrix(mp.mpf(1))
    tr_at_q1 = matrix_trace(M)
    print(f"  tr_{{V^⊗3}}(β_Bor)|_{{q=1}} = {mp.nstr(tr_at_q1, 14)}")
    print(f"  expected: 8 = dim V^⊗3")
    match = abs(tr_at_q1 - 8) < mp.mpf("1e-30")
    print(f"  Match: {'✓' if match else '✗'}")
    return {
        "tr_at_q1": str(tr_at_q1),
        "matches_dim_8": match,
    }


# ── main ─────────────────────────────────────────────────────────


def main():
    w = WitnessBuilder("gap-a4-T17-schur-weyl-rmatrix-probe",
                       engine="mpmath")
    w.set_audit_only(
        "docs/audits/2026-06-06-gap-a4-T9-T14-followup-retrospective.md"
    )
    w.set_description(
        "GAP-A-4 T17 — First categorical / topological distinguisher in "
        "the T4-T17 arc.  Derives tr_{V^⊗3}(β_Bor) directly from the "
        "U_q(sl_2) R-matrix action on V_{1/2}^⊗3 and cross-checks "
        "against the Schur-Weyl prediction 4·χ^{(3)} + 2·χ^{(2,1)} "
        "= 8 − 6h⁴ − 2h⁶ (classical sl_2 dims 4, 2 — not q-deformed "
        "[4]_q/[2]_q; combining T15 polynomial χ^{(2,1)} with the "
        "trivial rep's χ^{(3)}(β_Bor) = 1 for writhe-0 braids)."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)

    print(f"  q₀ = {Q_0_50DPS[:18]}...")
    print()

    hecke = check_rmatrix_hecke_relation(q_0)
    print()
    schur = check_direct_vs_schur_weyl(q_0)
    print()
    classical = check_identity_dim_at_h_zero()

    w.add_data("hecke_relation_check", hecke)
    w.add_data("direct_vs_schur_weyl", schur)
    w.add_data("classical_limit_check", classical)

    w.add_assertion(
        "hecke_relation_holds_on_V_tensor_V",
        computed=float(mp.mpf(hecke["max_residual_entry"])),
        expected=0.0,
        tolerance=float(TOL_50DPS),
        source=(
            "(R − q)(R + q⁻¹) = 0 on V⊗V — the defining Hecke quotient "
            "relation for σ_i.  Verified to 50 dps."
        ),
    )
    w.add_assertion(
        "direct_rmatrix_matches_schur_weyl_prediction",
        computed=float(mp.mpf(schur["absolute_difference"])),
        expected=0.0,
        tolerance=float(TOL_50DPS),
        source=(
            "tr_{V^⊗3}(β_Bor) via direct 8×8 R-matrix computation "
            "equals the Schur-Weyl prediction "
            "dim(V_{3/2})·χ^{(3)}(β_Bor) + dim(V_{1/2})·χ^{(2,1)}(β_Bor) "
            "= 4·1 + 2·(2 − 3h⁴ − h⁶) = 8 − 6h⁴ − 2h⁶ "
            "(classical integer sl_2 dims 4, 2 — NOT q-deformed "
            "[4]_q/[2]_q, per gotcha 1; χ^{(3)}(β_Bor) = 1 from writhe 0 "
            "+ T15 polynomial)."
        ),
    )
    w.add_assertion(
        "trace_at_q_one_equals_dim_8",
        computed=float(mp.mpf(classical["tr_at_q1"])),
        expected=8.0,
        tolerance=1e-30,
        source=(
            "At q = 1, β_Bor → identity ∈ S_3, so tr_{V^⊗3}(β_Bor) = "
            "tr_{V^⊗3}(id) = dim V^⊗3 = 2³ = 8."
        ),
    )

    if schur["categorical_derivation_succeeds"]:
        verdict = (
            "T17 SUCCEEDS as the FIRST first-principles categorical "
            "derivation in the T4-T17 arc: the direct 8×8 R-matrix "
            "computation of tr_{V^⊗3}(β_Bor) reproduces the Schur-Weyl "
            "Wedderburn-block prediction "
            "tr = dim(V_{3/2}) · χ^{(3)} + dim(V_{1/2}) · χ^{(2,1)} "
            "= 4 + 2·(2 − 3h⁴ − h⁶) = 8 − 6h⁴ − 2h⁶ to 50 dps at q_0. "
            "Subtle: the H_n(q)-side dim in the q-Schur centralizer is "
            "the CLASSICAL integer dim (4 for V_{3/2}, 2 for V_{1/2}), "
            "NOT the q-deformed [4]_q / [2]_q — same convention as T8's "
            "sl_2 q-Schur centralizer identity.  This confirms (a) the "
            "T15 polynomial χ^{(2,1)}(β_Bor) = 2 − 3h⁴ − h⁶ is the "
            "correct (2,1)-block character, and (b) the categorical "
            "Schur-Weyl decomposition picks out the (2,1) block "
            "correctly from the 8-dim V^⊗3 trace.  This is the FIRST "
            "distinguisher in the T16 enumeration: the Schur-Weyl "
            "projector is the correct category-theoretic source of the "
            "(2, 0, −3, −1) coefficient 4-tuple at the (2,1) block, NOT "
            "the other combinatorial candidates that happened to match "
            "values.  Subtle gotcha (worth recording for future probes): "
            "the braided R-matrix inverse Ř⁻¹ = Ř − (q − q⁻¹)·I, NOT "
            "Ř(q → q⁻¹) — initial v1 of this probe had the wrong inverse "
            "and produced a 0.39 numerical discrepancy."
        )
    else:
        verdict = (
            "T17 FAILS to verify the Schur-Weyl prediction against the "
            "direct R-matrix computation — investigate R-matrix "
            "convention / sign / normalisation mismatch."
        )
    w.add_data("synthesis_verdict", verdict)

    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in verdict.split(". "):
        print(f"    {chunk.strip()}")

    out_path = w.save()
    print()
    print(f"  Wrote witness: {out_path}")


if __name__ == "__main__":
    main()
