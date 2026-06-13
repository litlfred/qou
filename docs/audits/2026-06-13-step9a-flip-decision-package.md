# Step-9a flip decision package — per-block `tr_M` vs `linking_weight` production switch

**Date:** 2026-06-13 · **Branch:** `claude/leanval-witness-step9a-followups-2026-06-13` (PR #2213)
**Status:** decision support only — **no production path changed**. The flip
itself is owner-gated per
[Option-A scoping §3](2026-06-04-option-a-vol-per-knot-scoping.md).
**Data source:** every number below is read from the existing
`probes/option-a-vol-per-knot-light-series.witness.json` (2026-06-04, all
chi-caches present) — no new compute, no fit.

## The question

Production (`mass_table_comprehensive.py:208`) evaluates absolute masses with
the uniform shortcut `vol_density_borromean(q₀) = [Vol(𝓑₃)/ℏ_q²] ·
linking_weight_family_a(q₀)` (Family-A scalar ≈ 2.53). The paper-faithful
per-block form is `vol_density_per_block(Vol(K), tr_M(β_K, H_{3A}), q₀)`.
Should production flip?

## The data (Option-A witness, 50 dps inputs)

| K | tr_M(β_K, H₃ₐ) | m per-knot (MeV) | m uniform (MeV/nucleon) | CODATA total | per-knot gap | required residual R(K) |
|---|---|---|---|---|---|---|
| p | 1.0653 | 406.33 | 966.05 | 938.27 | −56.7 % | 2.309 |
| n | 0.9232 | 352.14 | 966.05 | 939.57 | −62.5 % | 2.668 |
| D | 0.3883 | 88.94 | 966.05 | 1875.61 | −90.5 % | 21.09 |
| T | 0.1041 | 44.88 | 966.05 | 2808.92 | −95.2 % | 62.59 |
| ³He | 0.2065 | 78.78 | 966.05 | 2808.39 | −91.6 % | 35.65 |
| ⁴He | 0.0553 | 84.44 | 966.05 | 3727.38 | −90.9 % | 44.14 |

`R(K) = m_CODATA(K) / m_perknot(K)` is the factor a flipped production
would still need to supply.

## Three observations the table forces

1. **The discrepancy is not the quoted constant 2.38×.** That figure is the
   proton-only ratio (`linking_weight 2.53 / tr_M(𝓑₃) 1.065`). Across the
   light series, R(K) runs **2.3 → 62.6 and is strongly A-dependent**,
   because the H₃ₐ Markov trace of the full atom word decays with strand
   count (1.065 at H₃ → 0.055 at H₁₂) while masses grow ∝ A.
2. **"Flip + re-pin" is refuted by the witness's own numbers.** No single
   recalibration of (q₀, m_e, or a global scale) absorbs an A-dependent
   2→63× factor. Re-pinning at the proton leaves D off by ×9.1 and T by
   ×27.1. This closes a tempting shortcut without any new computation.
3. **Why the uniform shortcut "works" (+2.9 % → +3.7 %).** It predicts the
   *same* ≈ 966.05 MeV per nucleon for every isotope; observed per-nucleon
   masses span only 931.8–939.6 MeV. The shortcut is a proton-calibrated
   per-nucleon constant, structurally blind to A — which is exactly the
   Vol-uniform bug (the A-trend of its gap, +2.89 % at p to +3.67 % at
   ⁴He, is the visible residual of that blindness).

## Decision options

- **(A) Status quo.** Keep the shortcut for absolute masses; use per-block
  `tr_M` only where the constant cancels (ratios, isotope deltas).
  Cost: the +2.9→3.7 % A-trend stays; the paper's Stage-4 per-block form
  remains unwired in production.
- **(B) Flip as a derivation milestone — OWNER-SELECTED 2026-06-13.**
  Treat R(K) as the
  missing per-A normalisation — the same object as the step-9b per-block
  density leg (`ρ(K)` / Δ_λ; cf. the trace-canonical residual
  `Δ_λ(K) ≈ q₀^(10A−5)` thread,
  [2026-06-09 residual audit](2026-06-09-delta-lambda-canonical-residual.md)).
  Wire-up order: derive the normalisation → flip → regenerate the
  dashboards. Until then the flip has no free-parameter-free form, and
  flipping early just converts a 3 % uniform bias into a 57–95 % deficit.
- **(C) Flip + re-pin.** **Refuted** (observation 2). Recorded so the
  option is not re-derived; this is the same class of error as the
  four-session c₃ wire/un-wire flip-flop.

Observation recorded in passing (not a proposal): the adjudicated binding
law `B_AME ≈ ρ·m_e·Vol(K)` (PR #2192, 1–3 %) uses Vol *without* the H₃ₐ
trace, while the mass identity uses `Vol·tr_M/ℏ_q²`; the pair brackets
where the per-A normalisation must live.

## What this package deliberately does not do

No seventh Δ_λ ansatz, no R(K) curve-fit, no production edit, no
re-pin experiment — per the Δ_λ gate and the three-calibration
discipline. The next *computational* step under (B) is the 9b
derive-or-refute `10A−5` item already on the cheat-sheet frontier, not a
new search.
