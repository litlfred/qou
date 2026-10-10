---
# qou-u4mx
title: 'FALSE: ClausenFunctionMathlibFiller.lean:33 says Cl_2 periodicity awaits Fourier infra — Mathlib has Analysis/Fourier/AddCircle, and the lemmas need no Fourier'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:08:24Z
updated_at: 2026-10-04T15:19:07Z
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
