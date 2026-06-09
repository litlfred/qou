# Coordination ledger — atom→V_hyp→Δ_λ closure

**Goal.** Close per-isotope binding `B(K)=m_e Σ_λ y_λ χ^λ Δ_λ(K)` via the
atom→V_hyp map (`⋈_K` on active sets → depth-2 `Li_2^q` volume image →
`vol_density` Δ_λ). Workplan: [#2078](https://github.com/litlfred/qou/pull/2078)
/ [`docs/workplans/2026-06-09-atom-to-vhyp-map-delta-lambda.md`](../workplans/2026-06-09-atom-to-vhyp-map-delta-lambda.md).

## Scope map (2026-06-09)

| PR | scope | classification | action |
|----|-------|----------------|--------|
| **#2078** (mine) | atom→V_hyp→Δ_λ workplan | — | — |
| **#2062** matrix-M reduced-block kernel (Phase 1.4) | per-nucleus χ^λ reduction toward A=8,9 | **dependency** (Stage ① χ at A≥4) | intent posted ([comment](https://github.com/litlfred/qou/pull/2062#issuecomment-4664003573)); read-only consumer |
| **#2023** matrix-M determinism | `chi_via_matrix_m_mpfr` reproducible decimal strings | **dependency** (χ-witness reproducibility) | intent posted ([comment](https://github.com/litlfred/qou/pull/2023#issuecomment-4664003929)) |
| #2057 depth-stratified tower binding | binding-tower default | related (monitor; no direct file dep) | watch |

**Merged upstream I build on:** #2074 (SDP-v2 Wedderburn-spectral), #2076
(Δ_λ feed analysis), #2067 (additive-baseline purge), #2049 (galois compute).

## Consistency check (skill §6) — NO inconsistencies

- #2062 states "Δ_λ-gate / 3-calibration: same trace identity — pure
  structural rearrangement, no ansatz/fit." This **matches** my Δ_λ feed
  analysis (#2076): the matrix-M reduction is structural; the Δ_λ closure
  is the canonical `vol_density`, not a fit. No reframing needed.
- #2023 is a pure reproducibility fix — orthogonal, consistent.

## Cherry-picks (skill §10) — none

The matrix-M PRs are **upstream** of my workplan (I consume their χ
output); nothing to pull into my branch. My branch is docs-only.

## Next concrete task (non-overlapping)

Build the **Stage ①→③ driver** on the A≤3 matrix-M set (Route A):
`chi_at_q0_via_matrix_m_mpfr` → depth-2 `Li_2^q` volume image →
`vol_density_per_block` → `Δ_λ(K)` → `B_pred(K)` vs AME. This consumes
matrix-M χ read-only (no overlap with #2062/#2023) and is the decisive
closure test on the tractable subset. Gated on matrix-M coverage for
the volume route; extension A=4→9 tracked on #2062.
