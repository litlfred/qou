import HeckeTemperleyLieb.MarkovAxiomsPrimitive
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# Markov loop value with `Real.sqrt` (deprecated, Transcendental companion)

Split from `HeckeTemperleyLieb.MarkovAxiomsPrimitive` (bean `qou-dk7p`). The generic
`markovZax (u : R)` with `u² = q` stays there; this file keeps the deprecated
`Real.sqrt` form under its original name.
-/

namespace QOU.BraidKnot

/-- **Legacy unsafe form** of `markovZax` — `Real.sqrt q` without the
    `0 < q` hypothesis. Kept for backward compatibility with the
    pre-Tier-2 callsites; new code should use one of:
      - generic `markovZax (u : R)` with `u² = q` for `[Field R]`
        (Tier 2 — preferred; avoids `Real.sqrt` entirely)
      - `markovZax_real (q : ℝ) (hq : 0 < q)` (Tier 5 archimedean
        shim with explicit positivity)
    Do NOT migrate to `markovZax (Real.sqrt q)` — that still triggers
    the `q-usage-positivity-implicit` warning since `Real.sqrt` carries
    no positivity hypothesis. -/
@[deprecated "Migrate to (a) the generic `markovZax (u : R)` with an explicit u² = q hypothesis (Tier 2 — preferred), or (b) `markovZax_real q hq` carrying `0 < q` (Tier 5). Avoid `markovZax (Real.sqrt q)` — still positivity-implicit. See docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md." (since := "2026-08-03")]
noncomputable def markovZax_legacy (q : ℝ) : ℝ :=
  1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

end QOU.BraidKnot
