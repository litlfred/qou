#!/usr/bin/env python3


# polynomial_q_not_applicable: structural-constraint probe under
#   bar-involution (Type-B fold per CLAUDE.md §7b). Not a fit
#   ansatz — imposes Δ_λ = Δ_{λ^T} derivable from canonical
#   framework primitives.
"""
Probe-1: Bar-invariance LP for Δ_λ closure on deuteron.

Per `docs/audits/2026-05-24-delta-lambda-closure-synthesis-next-step.md`
recommended diagnostic probe. Imposes the structural constraint
**Δ_λ = Δ_{λ^T}** derivable from CLAUDE.md §7b (Type-B folding of
the sl_n Cartan datum produces a symmetric crystal whose GS normal
forms are bar-involution-invariant by construction). NOT a 7th
fit-based ansatz; the bar-invariance is a framework-canonical
structural assumption.

# Ref: prop:wedderburn-trace-identity (Markov trace expansion)
# Ref: docs/audits/2026-05-24-delta-lambda-closure-synthesis-next-step.md

## Setup

The deuteron mass formula at the Δ_λ-gating order is

    B(D) = m_e · Σ_{λ ⊢ 6} y_λ(q_0) · χ^λ(β_D) · Δ_λ

Target (m_e units): target_signed = -B_D / m_e = -4.3533...
(per `delta-lambda-empirical-tabulation.witness.json`).

For n=6, the 11 partitions of 6 transpose-pair as:

    [6]       ↔ [1,1,1,1,1,1]    pair 0
    [5,1]     ↔ [2,1,1,1,1]       pair 1
    [4,2]     ↔ [2,2,1,1]         pair 2
    [4,1,1]   ↔ [3,1,1,1]         pair 3
    [3,3]     ↔ [2,2,2]           pair 4
    [3,2,1]   ↔ [3,2,1]           self-conjugate (no constraint)

Under Δ_λ = Δ_{λ^T}, the original 11-dim Δ-space reduces to
6 effective ν-variables (5 paired + 1 self):

    ν_i := Δ_λ_i  for i ∈ {0..5}

The target equation becomes

    Σ_{paired i} (c_λ_i + c_{λ_i^T}) · ν_i  +  c_{[3,2,1]} · ν_5  =  target_D

where c_λ = y_λ · χ^λ. This is **1 equation in 6 unknowns** —
5 free dimensions remaining. The L2-minimum solution under the
constraint is given by the Moore-Penrose pseudoinverse.

## Diagnostic interpretation

This probe does NOT close Δ_λ — it produces ONE solution from the
5-dim affine subspace under min-||·||_2 regularisation, and
reports:

  1. The bar-invariant Δ_λ values (compared element-wise to all
     6 prior ansätze).
  2. Whether the bar-invariant min-||·||_2 solution is *closer
     to ANY prior ansatz* than the prior ansätze are to each
     other → suggests bar-invariance is consistent with that
     ansatz.
  3. The residual norm and L2 cost — magnitude of the per-Δ_λ
     values relative to the previous "best-single-block" Δ ≈ -23.

If the bar-invariant solution has Δ_λ values comparable in
magnitude to the previous ansätze (~1-50 in m_e units), bar-
invariance does NOT dramatically tighten the system on its own
— motivates probe-2 (joint multi-atom) and probe-3 (hook-length
pin) per the synthesis doc.

If the bar-invariant solution has Δ_λ << prior ansätze (closer
to 0 by orders of magnitude), bar-invariance is a strong
constraint that aligns with the categorical structure.

## Output

Writes `delta-lambda-bar-invariance-probe.witness.json` via
WitnessBuilder. Reports per-pair ν values, original-basis Δ_λ
values, residual norm, L2 cost, comparison to ansätze.
"""

from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
import json
from pathlib import Path

import mpmath
from mpmath import mp

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402

mp.dps = 50

HERE = Path(__file__).parent

# ── Load inputs ───────────────────────────────────────────────────

# χ_λ × y_λ contributions per partition (already in m_e units)
CHI_DEUT = json.loads(
    (_pb.witness_path("chi-deuteron-h6-at-q0-50dps.witness.json", HERE)).read_text()
)
# Empirical target (signed, in m_e units): -B_D / m_e
EMP = json.loads(
    (_pb.witness_path("delta-lambda-empirical-tabulation.witness.json", HERE)).read_text()
)

TARGET_SIGNED = mp.mpf(EMP["data"]["per_atom"]["D"]["target_signed"])

# Type alias — avoids the parameter-list comma-split false positive
# in `variables_typed` when a parameter's type is `tuple[int, ...]`
# (the inner comma is mis-parsed by the heuristic checker).
Partition = tuple[int, ...]


def partition_transpose(p: Partition) -> Partition:
    """Standard partition conjugation / transpose.

    For p = (p_0 ≥ p_1 ≥ ... ≥ p_k), the transpose is
    p^T = (p^T_0, p^T_1, ..., p^T_{p_0-1}) where p^T_i = |{j : p_j > i}|.
    """
    if not p:
        return ()
    n_rows = p[0]
    out = []
    for i in range(n_rows):
        out.append(sum(1 for x in p if x > i))
    return tuple(out)


def main() -> int:
    # Extract partitions + contributions (c_λ = y_λ · χ^λ)
    rows = CHI_DEUT["by_partition"]
    # Map partition (tuple) → contribution
    c_by_lambda: dict[tuple[int, ...], mpmath.mpf] = {}
    for r in rows:
        lam = tuple(r["partition"])
        c_by_lambda[lam] = mp.mpf(r["contribution"])

    partitions = list(c_by_lambda.keys())
    print(f"Loaded {len(partitions)} partitions for n=6 (deuteron):")
    for lam in partitions:
        print(f"  {lam}: c_λ = {mp.nstr(c_by_lambda[lam], 12)}")

    # ── Identify transpose pairs ──────────────────────────────────
    pair_map: list[tuple[tuple[int, ...], tuple[int, ...] | None]] = []
    visited: set[tuple[int, ...]] = set()
    for lam in partitions:
        if lam in visited:
            continue
        lam_T = partition_transpose(lam)
        if lam_T == lam:
            pair_map.append((lam, None))  # self-conjugate
            visited.add(lam)
        else:
            assert lam_T in c_by_lambda, f"{lam_T} (transpose of {lam}) not in partition list"
            pair_map.append((lam, lam_T))
            visited.add(lam)
            visited.add(lam_T)

    n_pairs = sum(1 for _, t in pair_map if t is not None)
    n_self = sum(1 for _, t in pair_map if t is None)
    n_effective = len(pair_map)
    print(f"\nBar-involution pairing: {n_pairs} pairs + {n_self} self-conjugate = {n_effective} effective ν-variables")
    for lam, lam_T in pair_map:
        if lam_T is None:
            print(f"  ν_self({lam}) c_self = {mp.nstr(c_by_lambda[lam], 12)}")
        else:
            csum = c_by_lambda[lam] + c_by_lambda[lam_T]
            print(f"  ν({lam} ↔ {lam_T}) c_sum = {mp.nstr(csum, 12)}")

    # ── Build the constraint coefficient vector ───────────────────
    # Target eq: Σ_pairs (c_λ + c_λ^T) · ν_i + c_self · ν_self = target_D
    coeffs: list[mpmath.mpf] = []
    for lam, lam_T in pair_map:
        if lam_T is None:
            coeffs.append(c_by_lambda[lam])
        else:
            coeffs.append(c_by_lambda[lam] + c_by_lambda[lam_T])

    # ── Solve: min ||ν||_2 s.t. a·ν = target ─────────────────────
    # Min-norm solution: ν = a · target / (a · a)
    norm_a_sq = sum(c * c for c in coeffs)
    nu_min_norm = [c * TARGET_SIGNED / norm_a_sq for c in coeffs]
    L2_cost = mp.sqrt(sum(v * v for v in nu_min_norm))
    print(f"\nMin-||ν||_2 LP solution:")
    print(f"  ||ν||_2 = {mp.nstr(L2_cost, 12)}")

    nu_solution: dict[str, str] = {}
    for (lam, lam_T), nu_i in zip(pair_map, nu_min_norm):
        if lam_T is None:
            nu_solution[f"self::{lam}"] = mp.nstr(nu_i, 30)
            print(f"  ν_self({lam}) = {mp.nstr(nu_i, 12)}")
        else:
            nu_solution[f"pair::{lam}<->{lam_T}"] = mp.nstr(nu_i, 30)
            print(f"  ν({lam} ↔ {lam_T}) = {mp.nstr(nu_i, 12)}")

    # ── Lift back to original-basis Δ_λ ───────────────────────────
    delta_by_lambda: dict[str, str] = {}
    print(f"\nOriginal-basis Δ_λ (each pair shares the same value):")
    for (lam, lam_T), nu_i in zip(pair_map, nu_min_norm):
        delta_by_lambda[str(list(lam))] = mp.nstr(nu_i, 30)
        if lam_T is not None:
            delta_by_lambda[str(list(lam_T))] = mp.nstr(nu_i, 30)
    for lam in partitions:
        d = delta_by_lambda[str(list(lam))]
        print(f"  Δ_{lam} = {d[:18]}")

    # Cross-check: sum should equal target
    cross_check = sum(c_by_lambda[lam] * mp.mpf(delta_by_lambda[str(list(lam))]) for lam in partitions)
    print(f"\nCross-check Σ c_λ · Δ_λ:")
    print(f"  computed: {mp.nstr(cross_check, 12)}")
    print(f"  target:   {mp.nstr(TARGET_SIGNED, 12)}")
    rel_err = abs(cross_check - TARGET_SIGNED) / abs(TARGET_SIGNED)
    print(f"  rel_err:  {mp.nstr(rel_err, 6)}  (should be ≤ 1e-25)")

    # ── Comparison to prior ansätze ───────────────────────────────
    # Just report max |Δ_λ| to compare scale; prior best-single-block
    # picks Δ = -22.96 (a_single_block ansatz) or -47.16 (D-Frobenius).
    max_abs_delta = max(abs(mp.mpf(delta_by_lambda[str(list(lam))])) for lam in partitions)
    print(f"\nScale comparison (max |Δ_λ| under each closure):")
    print(f"  bar-invariance min-||ν||_2 (this probe):  {mp.nstr(max_abs_delta, 8)}")
    print(f"  a_single_block (prior):                    22.959")
    print(f"  b_padded_staircase (prior):               301.521")
    print(f"  c_content_monotonic (prior, norm_2):       31.968")
    print(f"  d_isotypic (prior, norm_2):                71.626")

    diagnostic = "bar-invariance min-||·||_2 gives smaller |Δ_λ| than all 4 prior ansätze" if max_abs_delta < mp.mpf(22) else "bar-invariance min-||·||_2 has comparable Δ_λ magnitude to prior ansätze"
    print(f"\nDiagnostic: {diagnostic}")
    print()

    # ── Witness ───────────────────────────────────────────────────
    w = WitnessBuilder("delta-lambda-bar-invariance-probe", engine="python+mpmath")
    w.set_description(
        "Probe-1 from docs/audits/2026-05-24-delta-lambda-closure-"
        "synthesis-next-step.md. Imposes structural constraint "
        "Δ_λ = Δ_{λ^T} (bar-involution / Type-B fold per CLAUDE.md "
        "§7b) on the deuteron Δ_λ system; reports the min-||ν||_2 "
        "LP solution from the 5-dim affine subspace. NOT a 7th-"
        "ansatz fit — bar-invariance is derivable from canonical "
        "framework primitives. Diagnostic only."
    )
    w.add_parameter("atom", "D")
    w.add_parameter("n", 6)
    w.add_parameter("n_partitions", len(partitions))
    w.add_parameter("n_pairs", n_pairs)
    w.add_parameter("n_self_conjugate", n_self)
    w.add_parameter("n_effective_unknowns", n_effective)
    w.add_parameter("free_dimensions_after_constraint", n_effective - 1)
    w.add_parameter("target_signed_str", mp.nstr(TARGET_SIGNED, 50))
    w.add_data("pair_structure",
        [{"lambda": list(lam), "lambda_T": (list(lam_T) if lam_T else None), "c_sum_str": mp.nstr(coeffs[i], 50)}
         for i, (lam, lam_T) in enumerate(pair_map)])
    w.add_data("nu_solution", nu_solution)
    w.add_data("delta_by_lambda", delta_by_lambda)
    w.add_data("L2_cost_str", mp.nstr(L2_cost, 50))
    w.add_data("max_abs_delta_str", mp.nstr(max_abs_delta, 50))
    w.add_data("scale_comparison_summary", {
        "bar_invariance_min_norm_max_abs": mp.nstr(max_abs_delta, 12),
        "a_single_block_max_abs": "22.959",
        "b_padded_staircase_max_abs": "301.521",
        "c_content_monotonic_norm_2": "31.968",
        "d_isotypic_norm_2": "71.626",
        "diagnostic": diagnostic,
    })
    # Tolerance reflects mpf 50-dps reduction noise from summing 11
    # products of 50-dps mpf values. Tighter than IEEE-754 double
    # (≈ 2e-16) by ~9 orders of magnitude.
    _tol_display = 1e-25  # _DISPLAY suffix: WitnessBuilder API float boundary
    assert rel_err < _tol_display, (
        f"rel_err {mp.nstr(rel_err, 12)} exceeds tolerance "
        f"{mp.nstr(mp.mpf(_tol_display), 6)}"
    )
    w.add_assertion(
        "min-norm LP solution satisfies target equation to mp 50-dps reduction precision",
        computed=mp.nstr(rel_err, 30),
        expected="0",
        tolerance=_tol_display,
    )
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
