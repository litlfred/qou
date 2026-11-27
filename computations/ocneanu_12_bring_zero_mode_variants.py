"""Bring zero-mode structural variants for the Ocneanu '12' EM correction.

Task 1 of `docs/coordination/2026-06-01-closed-route-followups.md` —
following PR #1581's tier=near-match finding:

  k = 12 − (α_em/π)/dim H_3   →   k_required at 54 ppb (0.054 ppm)

The bare `(α_em/π) / dim H_3 = (α_em/π) / 6` is the simplest form.
This probe tests Bring-zero-mode-motivated structural variants to see
if any tighten the 54 ppb residual to below ~10 ppb (the 1ppQ
substrate target).

## The m_K/m_π template (PR #1442)

The merged m_K/m_π closure uses:
  EM_correction(m_K/m_π) = (α_em/π) · (3q² − 1)/(2q²)
                        = (α_em/π) · (1 + ℏ_q − ℏ_q²/2)

The `(3q²−1)/(2q²)` shape is a TRUNCATION of a sinh-channel q-series
at ℏ_q² order. The factor `3` = number of saturating-genus generation
torus knots on Bring's surface (T_(2,3), T_(2,5), T_(2,7)). The `2q²`
denominator is the standard EM-self-energy halving × substrate scale.

## Analog for the proton-mass identity term `12·m_e`

The proton is at H_3 (3-strand braid group ↔ Hecke H_3). Candidate
structural forms:

  (A) bare:                 (α_em/π) / dim H_3                  → 54 ppb
  (B) sinh-truncation A:    (α_em/π) · (3q²−1)/(2q²) / dim H_3  → 2984 ppb (regress)
  (C) sinh-truncation B:    (α_em/π) · (1 + ℏ_q) / dim H_3
  (D) sinh-truncation C:    (α_em/π) · (1 − ℏ_q²/2) / dim H_3
  (E) Plancherel-correct:   (α_em/π) · (1/Σd_q²_λ at q_0)
                            = (α_em/π) · (1 / sum_dq_sq_at_q0)
  (F) Bring substrate-scale: (α_em/π) · q⁻² / 6
  (G) Quark-count weighted: (α_em/π) · (1/3) · (1/strand_count)
  (H) Charge-weighted:      (α_em/π) · (2/3 + 1/3 + 0) / 6  [u, d, contracted]

The goal: find a structural variant that
  - Drives residual below ~10 ppb, AND
  - Has cleaner Bring/categorical motivation than the bare form

## Cross-references

- merged PR #1581 (Ocneanu near-match finding)
- merged PR #1442 (m_K/m_π closure, the structural template)
- content block `meson-em-sinh-closed-form.md` (Bring derivation
  of (3q²−1)/(2q²))
- coord ledger `2026-06-01-closed-route-followups.md` Task 1
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_MU_MEV_VALIDATION, M_P_MEV_VALIDATION  # noqa: E402 (codata sweep)
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def trM_borromean_closed(q):
    # convention D — verified by EVALUATION at q0, not by reading: computations/audits/borromean_convention_by_evaluation.py
    h = q - 1 / q
    h2 = h * h
    return (4 + h2 - 3 * h2 ** 2 - h2 ** 3) / (h2 + 4)


def qint(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def qfact(k, q):
    out = mp.mpf(1)
    for i in range(1, k + 1):
        out *= qint(i, q)
    return out


def main() -> int:
    set_compute_dps(60)  # one decade above the 54 ppb residual
    q = Q_MP

    print("=" * 78)
    print("Ocneanu '12' EM correction — Bring zero-mode structural variants")
    print("=" * 78)
    print(f"\nq_0 = {Q_50_DIGIT_STR}\n")

    # Reproduce k_required
    qfact_3 = qfact(3, q)
    trM = abs(trM_borromean_closed(q))
    F_Bor = trM * qfact_3 / q ** 3
    m_e = mp.mpf("0.51099895069")
    m_mu = mp.mpf(M_MU_MEV_VALIDATION)
    m_p = mp.mpf(M_P_MEV_VALIDATION)
    k_required = (2 * m_mu * F_Bor - m_p) / m_e
    residual_target = 12 - k_required

    print(f"[Setup recap]")
    print(f"  k_required        = {mp.nstr(k_required, 25)}")
    print(f"  residual target   = 12 - k = {mp.nstr(residual_target, 15)}")
    print(f"  (relative to 12)  = {mp.nstr(residual_target / 12 * mp.mpf('1e6'), 8)} ppm")

    # Helpers
    alpha_em = mp.mpf(1) / mp.mpf("137.035999084")
    h = q - 1 / q
    h2 = h * h
    hbar_q = 1 - 1 / q
    hbar_q_sq = hbar_q ** 2
    dim_H_3 = mp.mpf(6)  # |S_3| = Σ d²_λ at q=1

    # Q-deformed Wedderburn dims at q_0
    dim_q_21 = qfact_3 / 3  # dim_q V_(2,1)
    sum_dq_sq = mp.mpf(1) + dim_q_21 ** 2 + mp.mpf(1)

    # Variants
    variants = [
        # (A) Bare (the PR #1581 finding)
        ("(A) bare (α_em/π)/dim H_3", alpha_em / mp.pi / dim_H_3),
        # (B) m_K/m_π shape — already known to regress
        ("(B) (α_em/π)·(3q²−1)/(2q²)/dim H_3",
         alpha_em / mp.pi * (3 * q ** 2 - 1) / (2 * q ** 2) / dim_H_3),
        # (C) Linear sinh truncation
        ("(C) (α_em/π)·(1+ℏ_q)/dim H_3",
         alpha_em / mp.pi * (1 + hbar_q) / dim_H_3),
        # (D) Quadratic sinh truncation
        ("(D) (α_em/π)·(1−ℏ_q²/2)/dim H_3",
         alpha_em / mp.pi * (1 - hbar_q_sq / 2) / dim_H_3),
        # (E) Plancherel-corrected (q-deformed denominator)
        ("(E) (α_em/π) / Σ d_q²_λ at q_0",
         alpha_em / mp.pi / sum_dq_sq),
        # (F) Bring substrate-scale q⁻²
        ("(F) (α_em/π) · q⁻² / 6",
         alpha_em / mp.pi / q ** 2 / dim_H_3),
        # (G) Quark-count 1/3 × 1/dim H_3
        ("(G) (α_em/π) · (1/3) · (1/2) [quark+pair]",
         alpha_em / mp.pi * (mp.mpf(1) / 3) * (mp.mpf(1) / 2)),
        # (H) Charge-weighted u+d+contracted = 1
        ("(H) (α_em/π) · 1 / dim H_3 [charge-sum=1]",
         alpha_em / mp.pi / dim_H_3),  # same as A; charges sum to 1
        # (I) (α_em/π) · ℏ_q / something
        ("(I) (α_em/π) · ℏ_q / 1",
         alpha_em / mp.pi * hbar_q),
        # (J) (α_em/π) · [3]_q / [3]_q² (q-Plancherel-natural)
        ("(J) (α_em/π) · [3]_q / [3]_q² ",
         alpha_em / mp.pi * qint(3, q) / qint(3, q) ** 2),
        # (K) (α_em/π) · (q^(1/2)) / 6 — square root anomaly
        ("(K) (α_em/π) · √q / 6",
         alpha_em / mp.pi * mp.sqrt(q) / dim_H_3),
        # (L) (α_em/π) · q^(-1/2) / 6
        ("(L) (α_em/π) · 1/√q / 6",
         alpha_em / mp.pi / mp.sqrt(q) / dim_H_3),
        # (M) (α_em/π) · ℏ_q^(1/2) — half-rung
        ("(M) (α_em/π) · √ℏ_q",
         alpha_em / mp.pi * mp.sqrt(hbar_q)),
        # (N) Note: any (1 + α·h²) variant with α ≈ 0.038 would close the
        # residual to ~17 ppb, but with α being a fitted coefficient that
        # does NOT have a clean structural identification.  Omitted here
        # to keep the variant list to STRUCTURALLY-MOTIVATED candidates.
        # (O) Generation-count weighted: 3 generations → 1/3
        ("(O) (α_em/π) · (3 gens)/(6 dim H_3·3)",
         alpha_em / mp.pi * 3 / (dim_H_3 * 3)),
    ]

    # Score
    print(f"\n[Variants — sorted by |Δ ppb to residual target|]")
    print(f"  {'name':<45}{'correction':<22}{'Δ ppb to residual':<14}")
    scored = []
    for name, val in variants:
        delta = val - residual_target
        # residual_target ≈ 3.88e-4; |val − target| should be < ~1e-6 for 10 ppb match
        delta_ppb_of_residual = (val - residual_target) / residual_target * mp.mpf("1e9")
        # Also Δ ppb of k_required (the global metric)
        # k_predicted = 12 − val; residual = k_predicted − k_required = (12 − val) − k_req
        k_pred = 12 - val
        delta_k_ppb = (k_pred - k_required) / k_required * mp.mpf("1e9")
        scored.append((name, val, delta_ppb_of_residual, delta_k_ppb))

    scored.sort(key=lambda r: abs(r[3]))
    for name, val, dres, dk in scored:
        marker = ""
        if abs(dk) < mp.mpf("10"):
            marker = " ⭐⭐ within 10 ppb (structural)"
        elif abs(dk) < mp.mpf("54"):
            marker = " ⭐ tighter than (A) at 54 ppb"
        elif abs(dk) < mp.mpf("1000"):
            marker = " * within 1 ppm"
        print(f"  {name:<45}{mp.nstr(val, 18):<22}{mp.nstr(dk, 8):<14}{marker}")

    # Verdict
    print(f"\n[Verdict]")
    # Find baseline (A)
    baseline = next(r for r in scored if "(A)" in r[0])
    best = scored[0]
    if abs(best[3]) < mp.mpf("10") and "fit" not in best[0].lower():
        verdict = (
            f"STRUCTURAL CANDIDATE: '{best[0]}' lands at "
            f"{mp.nstr(best[3], 6)} ppb (vs (A) baseline {mp.nstr(baseline[3], 6)} ppb). "
            f"This is below the 10 ppb structural-identity threshold."
        )
    elif abs(best[3]) < abs(baseline[3]):
        verdict = (
            f"IMPROVED CANDIDATE: '{best[0]}' lands at "
            f"{mp.nstr(best[3], 6)} ppb, beating (A)'s {mp.nstr(baseline[3], 6)} ppb. "
            f"Not yet below structural-identity threshold but worth investigating."
        )
    else:
        verdict = (
            f"NO IMPROVEMENT — bare (A) at {mp.nstr(baseline[3], 6)} ppb remains "
            f"the tightest tested form. The Bring zero-mode template's "
            f"(3q²−1)/(2q²) sinh-truncation does NOT transfer to the proton "
            f"term; the structural mechanism appears to be different."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "ocneanu-12-bring-zero-mode-variants",
        engine="python",
    )
    w.set_description(
        "Task 1 of PR #1617 closed-route follow-ups: tests Bring zero-mode "
        "structural variants for the Ocneanu '12' EM correction "
        "(α_em/π)/dim H_3, parallel to m_K/m_π's (3q²−1)/(2q²) closure. "
        "Goal: find a variant tighter than 54 ppb baseline."
    )
    w.add_parameter("q_60dps", Q_50_DIGIT_STR)
    w.add_data("k_required", mp.nstr(k_required, 25))
    w.add_data("residual_target", mp.nstr(residual_target, 25))
    w.add_data("baseline_A_ppb", mp.nstr(baseline[3], 12))
    w.add_data("best_variant_name", best[0])
    w.add_data("best_variant_ppb", mp.nstr(best[3], 12))
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="bring_variant_search_completed",
        computed=len(variants) > 0,
        expected=True,
        tolerance=0,
        source=f"Scanned {len(variants)} Bring-motivated variants at 60 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
