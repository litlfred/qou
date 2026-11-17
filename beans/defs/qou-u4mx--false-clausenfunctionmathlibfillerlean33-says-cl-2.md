---
# qou-u4mx
title: 'FALSE: ClausenFunctionMathlibFiller.lean:33 says Cl_2 periodicity awaits Fourier infra — Mathlib has Analysis/Fourier/AddCircle, and the lemmas need no Fourier'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:08:24Z
updated_at: 2026-11-17T10:33:06Z
parent: qou-c8p8
---

**FALSE CLAIM (and self-contradicting).**
`QOU/Archimedean/ClausenFunctionMathlibFiller.lean:33-34`:

> "Periodicity / antisymmetry lemmas (sketch — full proofs **awaiting Fourier-series
> infrastructure in Mathlib**)."

**Mathlib has it.** Measured 2026-09-04 against pinned mathlib `f897ebcf72c`:
`Mathlib/Analysis/Fourier/AddCircle.lean` carries `fourierCoeff`,
`hasSum_fourier_series_L2` (`:374`), `hasSum_fourier_series_of_summable` (`:409`),
`has_pointwise_sum_fourier_series_of_summable` (`:419`), and Parseval
(`tsum_sq_fourierCoeff`). The directory also holds `PoissonSummation.lean`,
`Inversion.lean`, `FourierTransform.lean`, `RiemannLebesgueLemma.lean`.

**And the lemmas do not need it.** `Cl_2` is defined in that same file (`:80`) as an
explicit `tsum` of `sin (k θ) / k²`. Periodicity and antisymmetry follow **termwise**
from `Real.sin` periodicity and oddness — no Fourier theory, no convergence subtlety
beyond what the `tsum` already carries.

**The file contradicts itself thirteen lines later.** At `:47-50` it records the
duplication formula `Cl₂(2θ) = 2Cl₂(θ) − 2Cl₂(π−θ)` as **CLOSED 2026-07-26**, adding
explicitly *"**no Fourier identities needed**, just the sine duplication under the
integral representation plus the series↔integral bridge"* — and at `:52-58` records the
derivative, the Zagier integral bridge, continuity and the boundary lemmas as **CLOSED
2026-07-19**, all sorry-free in `QOU/Knot/Clausen.lean`. So the harder facts closed
without Fourier while the header still says the easier ones are blocked on it.

**Fix:** delete the "awaiting Fourier-series infrastructure" clause; either prove the
two lemmas termwise (small) or state them as simply not yet written. The rest of that
gap list is correct and should stay — `Real.dilog`, `BlochGroup`, the Suslin map, and
the general `D : ℂ∖{0,1} → ℝ` are all genuinely absent from Mathlib (`polylog` → **0**
files at this pin).

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §F4, §H9.

### Progress Update (2026-11-17, Round 61 — lane-e667)
- **PR:** `litlfred/qou#8303` (`https://github.com/litlfred/qou/pull/8303`), head `2a91d843d44db15a0190138e20fb1878634fbbeb` (`COMMIT1 = 0caff4971a8a2c0d7aec04c9a5a8e20f7218d2b3`), labeled `ready-to-merge` + `release`, `ready: 2a91d843d44db15a0190138e20fb1878634fbbeb` (`https://github.com/litlfred/qou/pull/8303#issuecomment-6945508253`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/AlternatingThreeFormPrimaryFactorUpperHalfPlaneCatalanClausenSymmetry.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-jvua`: `alternating_three_form_antisym_diag_and_unit_frame`.
  - `qou-kp89`: `primary_factor_linear_cancellation_and_cubic_remainder`.
  - `qou-m8xt`: `upper_half_plane_shifted_modulus_pos_and_cyclic_closure`.
  - `qou-mame`: `quarter_turn_even_vanishing_and_odd_alternation`.
  - `qou-u4mx`: `termwise_periodic_and_odd_two_harmonic_sum`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/alternating_three_form_primary_factor_upper_half_plane_catalan_clausen_symmetry_probe.py` + `computations/probes/alternating-three-form-primary-factor-upper-half-plane-catalan-clausen-symmetry.witness.json` (`scriptHash = 0ee532c9f9a2`, `scriptCommitSha = 0caff4971a8a2c0d7aec04c9a5a8e20f7218d2b3`, `allPassed = True`).
- **Adversarial Cross-Review (Round 61):** Verified `litlfred/qou#8285` (`250465c60a6cea44d9f569e88cc79ee2c8d8051b`, `0` advisories on all 5 added theorems, valid witness `39a564805d3e`) and `litlfred/qou#8299` (`7794a07bbdcd4212b670d7ed777098efe60dc9a4`, `0` advisories, valid witness `001b12183bba`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.
