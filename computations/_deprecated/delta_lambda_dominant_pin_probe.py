#!/usr/bin/env python3
# polynomial_q_not_applicable: structural-constraint probe pinning
#   the dominant Δ_{λ*} via GAP-A-4 (ρ = round(dim_q(λ*))). Not a
#   fit ansatz — pins one Δ_λ from the framework-canonical quantum
#   dimension, then min-norm solves the residual.
"""
Probe-3: Hook-length dominant-λ pin for Δ_λ closure on deuteron.

Per `docs/audits/2026-05-24-delta-lambda-closure-synthesis-next-step.md`
§3.3 — third single-session diagnostic probe. Pins the dominant
Δ_{λ*} (largest |y_λ · χ^λ|) at the value predicted by GAP-A-4:

    ρ = round(dim_q(λ*))

then solves the residual system for non-dominant Δ_λ under
min-||·||_2. NOT a fit-based ansatz: the dominant pin is derived
from the canonical quantum dimension (a framework primitive),
not from optimising fit quality.

# Ref: prop:operator-selection-lp (LP dual infrastructure)
# Ref: conj:rho-prefactor-structural (GAP-A-4 dominant prefactor)
# Ref: docs/audits/2026-05-24-delta-lambda-closure-synthesis-next-step.md

## Setup

The deuteron mass formula at the Δ_λ-gating order is

    B(D) = m_e · Σ_{λ ⊢ 6} y_λ(q_0) · χ^λ(β_D) · Δ_λ

Target (m_e units): target_signed = -B_D / m_e = -4.3533...

For n=6, dominant partition (largest |y_λ · χ^λ|):

    λ*(D) = (5, 1)         c_λ* = +0.18961       (driving term)

GAP-A-4 pin (ρ = round(dim_q(λ*))):

    dim_q((5,1)) at q_0 = 5.22044 → round = 5
    ⇒ Δ_{(5,1)} = 5  (positive small integer)

Two variants reported:

- **variant A (pin alone)**: 11 unknowns − 1 pin = 10 free; 1 target
  equation. Min-||Δ||_2 over the 10 non-dominant Δ_λ.
- **variant B (pin + bar-invariance)**: combines probe-1's bar-fold
  with the dominant pin. 5 effective ν (pairs + 1 self) − 1 fixed
  = 4 effective ν. 1 target eq. Min-||ν||_2 over the 4 free ν.

Diagnostic value:

- If variant A gives small residual ||Δ||_2 with bounded non-dominant
  |Δ_λ|, the dominant pin is consistent with the empirical target.
- If variant B narrows further (smaller max |Δ_λ| than probe-1's
  15.69), GAP-A-4 + bar-invariance together over-constrain Δ_λ
  productively.
- If variant A or B requires large non-dominant |Δ_λ|, the dominant
  pin is inconsistent (Δ_{(5,1)} ≠ 5 categorically).

## Caveats

- The pin Δ_{λ*} = round(dim_q(λ*)) is ITSELF the conjecture
  conj:rho-prefactor-structural (GAP-A-4). This probe TESTS the
  pin's consistency with the empirical target equation; a positive
  result strengthens the conjecture but does NOT prove it.
- The probe does NOT impose Δ_λ ∈ ℤ on non-dominant entries (an
  integrality pin would be a separate probe).
- 5-3 = ≥3 free dimensions remain in both variants. Closure requires
  the multi-atom probe-2 OR the Option E categorical work.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath
from mpmath import mp

# Path bootstrap for in-tree imports
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from alpha_5_jucys_murphy_central import dim_q_num  # noqa: E402

mp.dps = 50
Q0 = mp.mpf(Q_50_DIGIT_STR)

# χ_λ × y_λ contributions per partition (already in m_e units)
CHI_DEUT = json.loads(
    (HERE / "chi-deuteron-h6-at-q0-50dps.witness.json").read_text()
)
# Empirical target (signed, in m_e units): -B_D / m_e
EMP = json.loads(
    (HERE / "delta-lambda-empirical-tabulation.witness.json").read_text()
)

TARGET_SIGNED = mp.mpf(EMP["data"]["per_atom"]["D"]["target_signed"])

Partition = tuple[int, ...]


def partition_transpose(p: Partition) -> Partition:
    """Standard partition conjugation."""
    if not p:
        return ()
    n_rows = p[0]
    return tuple(sum(1 for x in p if x > i) for i in range(n_rows))


def main() -> int:
    rows = CHI_DEUT["by_partition"]
    c_by_lambda: dict[Partition, mpmath.mpf] = {}
    for r in rows:
        lam = tuple(r["partition"])
        c_by_lambda[lam] = mp.mpf(r["contribution"])

    partitions = list(c_by_lambda.keys())

    # ── Identify dominant λ* via |c_λ| = |y_λ · χ^λ| max ──────────
    lam_star = max(partitions, key=lambda lam: abs(c_by_lambda[lam]))
    c_lam_star = c_by_lambda[lam_star]
    print(f"Dominant partition: λ*(D) = {lam_star}")
    print(f"  |c_λ*| = {mp.nstr(abs(c_lam_star), 12)}")

    # ── GAP-A-4 pin: ρ = round(dim_q(λ*)) ─────────────────────────
    dim_q_star = dim_q_num(lam_star, Q0)
    # mp.nint returns the nearest integer as an mpf — preserves
    # substrate precision through the rounding, then a single int()
    # cast at the boundary (int() is exact for mpf integers, not a
    # float-precision boundary).
    delta_pin = int(mp.nint(dim_q_star))
    print(f"  dim_q({lam_star}) at q_0 = {mp.nstr(dim_q_star, 12)}")
    print(f"  Δ_pin = round(dim_q) = {delta_pin}")

    # Verify bar-invariance of the pin: dim_q(λ) = dim_q(λ^T)
    lam_star_T = partition_transpose(lam_star)
    dim_q_T = dim_q_num(lam_star_T, Q0)
    bar_pin_consistent = abs(dim_q_star - dim_q_T) < mp.mpf("1e-40")
    print(
        f"  bar-invariance check: dim_q({lam_star_T}) = "
        f"{mp.nstr(dim_q_T, 12)}, equal? {bar_pin_consistent}"
    )

    # ── Variant A: dominant pin alone ──────────────────────────────
    print()
    print("─── Variant A: dominant pin alone ───")
    non_dominant = [lam for lam in partitions if lam != lam_star]
    residual_target = TARGET_SIGNED - c_lam_star * delta_pin
    # Solve: Σ_{λ ≠ λ*} c_λ · Δ_λ = residual_target, min ||Δ||_2
    # Min-||Δ||_2 solution: Δ_λ = c_λ · residual_target / Σ c_λ²
    c_vec_A = [c_by_lambda[lam] for lam in non_dominant]
    sum_c_sq_A = sum(c * c for c in c_vec_A)
    delta_A = {
        lam: c_vec_A[i] * residual_target / sum_c_sq_A
        for i, lam in enumerate(non_dominant)
    }
    delta_A[lam_star] = mp.mpf(delta_pin)
    max_abs_A = max(abs(d) for d in delta_A.values())
    norm_A = mp.sqrt(sum(d * d for d in delta_A.values()))
    # Cross-check
    sum_check_A = sum(c_by_lambda[lam] * delta_A[lam] for lam in partitions)
    rel_err_A = abs(sum_check_A - TARGET_SIGNED) / abs(TARGET_SIGNED)
    print(f"  max |Δ_λ| = {mp.nstr(max_abs_A, 12)}")
    print(f"  ||Δ||_2   = {mp.nstr(norm_A, 12)}")
    print(f"  rel_err   = {mp.nstr(rel_err_A, 6)}")

    # ── Variant B: dominant pin + bar-invariance ───────────────────
    print()
    print("─── Variant B: dominant pin + bar-invariance ───")
    # Pair partitions under transpose; track visited
    pair_map: list[tuple[Partition, Partition | None]] = []
    visited: set[Partition] = set()
    for lam in partitions:
        if lam in visited:
            continue
        lam_T = partition_transpose(lam)
        if lam_T == lam:
            pair_map.append((lam, None))
            visited.add(lam)
        else:
            pair_map.append((lam, lam_T))
            visited.add(lam)
            visited.add(lam_T)

    # The dominant pin fixes one pair (since dim_q is bar-invariant).
    # Identify the pair containing lam_star.
    pinned_pair_idx = None
    for i, (a, b) in enumerate(pair_map):
        if a == lam_star or b == lam_star:
            pinned_pair_idx = i
            break
    assert pinned_pair_idx is not None

    # Free ν indices (excluding the pinned pair).
    free_indices = [i for i in range(len(pair_map)) if i != pinned_pair_idx]
    # Coefficient for ν_i: c_λ_i + c_λ_i^T (or just c_λ for self-conjugate)
    nu_coefs = []
    for i in range(len(pair_map)):
        a, b = pair_map[i]
        if b is None:
            nu_coefs.append(c_by_lambda[a])
        else:
            nu_coefs.append(c_by_lambda[a] + c_by_lambda[b])

    # Target after subtracting pinned pair: B has 1 pair, so the
    # pinned contribution is (c_λ* + c_{λ*^T}) · Δ_pin.
    a_star, b_star = pair_map[pinned_pair_idx]
    c_star_total = c_by_lambda[a_star] + (
        c_by_lambda[b_star] if b_star is not None else mp.mpf(0)
    )
    residual_B = TARGET_SIGNED - c_star_total * delta_pin

    # Solve: Σ_{i free} nu_coefs[i] · ν_i = residual_B, min ||ν||_2
    free_c = [nu_coefs[i] for i in free_indices]
    sum_c_sq_B = sum(c * c for c in free_c)
    nu_free = [c * residual_B / sum_c_sq_B for c in free_c]

    # Reconstruct full Δ_λ from ν values
    delta_B: dict[Partition, mpmath.mpf] = {}
    nu_full: list[mpmath.mpf] = [mp.mpf(0)] * len(pair_map)
    nu_full[pinned_pair_idx] = mp.mpf(delta_pin)
    for k, idx in enumerate(free_indices):
        nu_full[idx] = nu_free[k]
    for i, (a, b) in enumerate(pair_map):
        delta_B[a] = nu_full[i]
        if b is not None:
            delta_B[b] = nu_full[i]

    max_abs_B = max(abs(d) for d in delta_B.values())
    nu_norm_B = mp.sqrt(sum(n * n for n in nu_full))
    sum_check_B = sum(c_by_lambda[lam] * delta_B[lam] for lam in partitions)
    rel_err_B = abs(sum_check_B - TARGET_SIGNED) / abs(TARGET_SIGNED)
    print(f"  max |Δ_λ| = {mp.nstr(max_abs_B, 12)}")
    print(f"  ||ν||_2   = {mp.nstr(nu_norm_B, 12)}")
    print(f"  rel_err   = {mp.nstr(rel_err_B, 6)}")

    # ── Per-partition reports ──────────────────────────────────────
    print()
    print("Δ_λ values (variant B, pin + bar-invariance):")
    for lam in partitions:
        marker = "  ← pinned" if lam in (lam_star, partition_transpose(lam_star)) else ""
        print(f"  Δ_{lam} = {mp.nstr(delta_B[lam], 12)}{marker}")

    # ── Comparison vs probe-1 ──────────────────────────────────────
    print()
    print("Scale comparison vs probe-1 + prior ansätze:")
    print(f"  bar-invariance min-||ν||_2 (probe-1):       15.694866")
    print(f"  variant A (pin alone):                       {mp.nstr(max_abs_A, 12)}")
    print(f"  variant B (pin + bar-invariance):            {mp.nstr(max_abs_B, 12)}")
    print(f"  a_single_block (prior):                      22.959")
    print(f"  b_padded_staircase (prior):                 301.521")
    print(f"  c_content_monotonic (prior, norm_2):         31.968")
    print(f"  d_isotypic (prior, norm_2):                  71.626")

    if max_abs_B < mp.mpf("15.694866"):
        diagnostic = (
            "pin + bar-invariance gives SMALLER max |Δ_λ| than probe-1 alone — "
            "GAP-A-4 dominant pin is consistent with bar-invariance and tightens "
            "the closure further"
        )
    elif max_abs_B < mp.mpf("22.959"):
        diagnostic = (
            "pin + bar-invariance still beats all 4 prior ansätze but is not "
            "tighter than probe-1 alone — pin adds constraints without reducing "
            "the dominant-norm element"
        )
    else:
        diagnostic = (
            "pin + bar-invariance gives LARGER max |Δ_λ| than probe-1 alone — "
            "GAP-A-4 dominant pin may be inconsistent at q_0 or requires the "
            "non-dominant Δ_λ to compensate at the cost of larger norm"
        )
    print(f"\nDiagnostic: {diagnostic}")

    # ── Witness emission ──────────────────────────────────────────
    w = WitnessBuilder(
        "delta-lambda-dominant-pin-probe",
        engine="python+mpmath",
    )
    w.add_parameter("q0", mp.nstr(Q0, 50))
    w.add_parameter("target_signed", mp.nstr(TARGET_SIGNED, 30))
    w.add_parameter("partition_count", len(partitions))
    w.add_data("dominant_partition", {
        "lambda_star": list(lam_star),
        "lambda_star_transpose": list(partition_transpose(lam_star)),
        "c_lambda_star": mp.nstr(c_lam_star, 30),
        "dim_q_lambda_star": mp.nstr(dim_q_star, 30),
        "delta_pin": delta_pin,
        "bar_pin_consistent": bool(bar_pin_consistent),
    })
    w.add_data("variant_a_pin_alone", {
        "max_abs_delta": mp.nstr(max_abs_A, 30),
        "norm_2": mp.nstr(norm_A, 30),
        "rel_err": mp.nstr(rel_err_A, 30),
    })
    w.add_data("variant_b_pin_plus_bar_invariance", {
        "max_abs_delta": mp.nstr(max_abs_B, 30),
        "nu_norm_2": mp.nstr(nu_norm_B, 30),
        "rel_err": mp.nstr(rel_err_B, 30),
        "pair_count": len(pair_map),
        "free_dim_count": len(free_indices),
    })
    w.add_data("delta_by_lambda_variant_b", {
        str(list(lam)): mp.nstr(delta_B[lam], 30) for lam in partitions
    })
    w.add_data("scale_comparison_summary", {
        "probe_1_bar_invariance_max": "15.694866",
        "variant_a_pin_alone_max": mp.nstr(max_abs_A, 12),
        "variant_b_pin_plus_bar_max": mp.nstr(max_abs_B, 12),
        "a_single_block": "22.959",
        "b_padded_staircase": "301.521",
        "c_content_monotonic_norm_2": "31.968",
        "d_isotypic_norm_2": "71.626",
        "diagnostic": diagnostic,
    })
    # Assertion: both variants reproduce target equation to mp 50-dps
    # reduction precision. _tol_display = display-context tolerance.
    _tol_display = 1e-25
    assert rel_err_A < _tol_display, (
        f"variant A rel_err {mp.nstr(rel_err_A, 12)} exceeds tolerance"
    )
    assert rel_err_B < _tol_display, (
        f"variant B rel_err {mp.nstr(rel_err_B, 12)} exceeds tolerance"
    )
    w.add_assertion(
        "variant A (pin alone) satisfies target equation to mp 50-dps",
        computed=mp.nstr(rel_err_A, 30),
        expected="0",
        tolerance=_tol_display,
    )
    w.add_assertion(
        "variant B (pin + bar-invariance) satisfies target equation to mp 50-dps",
        computed=mp.nstr(rel_err_B, 30),
        expected="0",
        tolerance=_tol_display,
    )
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
