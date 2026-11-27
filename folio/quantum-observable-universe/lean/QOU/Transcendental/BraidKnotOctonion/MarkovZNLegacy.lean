import Mathlib.Analysis.SpecialFunctions.Sqrt
import BraidKnotOctonion.BraidGroupNStrand

/-!
# The legacy Markov parameter `1/(√q + 1/√q)` (transcendental boundary)

Split out of `BraidKnotOctonion.BraidGroupNStrand` under the owner ruling of
2026-11-27 (bean `qou-dk7p`, card choice "Also the convention-C items"). The
algebraic file pins the stabilisation factor of `MarkovTraceN` to
`markovZN u` for a square root `u ≥ 0` of `q` carried as a parameter; here the
deprecated real form is kept, together with the bridge lemma showing it is that
same value.
-/

namespace QOU.BraidKnot

/-- **Legacy unsafe form** of `markovZN` — `Real.sqrt q` without the
    `0 < q` hypothesis. Kept for backward compatibility with the
    pre-Tier-2 callsites; new code should use one of:
      - generic `markovZN (u : R)` with explicit `u² = q` for `[Field R]`
        (Tier 2 — preferred; avoids `Real.sqrt` entirely)
      - `markovZN_real (q : ℝ) (hq : 0 < q)` (Tier 5 archimedean shim)
    Do NOT migrate to `markovZN (Real.sqrt q)` — that still triggers
    the `q-usage-positivity-implicit` warning. -/
@[deprecated "Migrate to (a) the generic `markovZN (u : R)` with explicit `u² = q` (Tier 2 — preferred), or (b) `markovZN_real q hq` carrying `0 < q` (Tier 5). Avoid `markovZN (Real.sqrt q)` — still positivity-implicit. See docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md." (since := "2026-08-03")]
noncomputable def markovZN_legacy (q : ℝ) : ℝ :=
  1 / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-- The legacy form is the kernel at any non-negative square root of `q`. -/
theorem markovZN_legacy_eq_markovZN {q u : ℝ} (hu : u ^ 2 = q) (hu0 : 0 ≤ u) :
    markovZN_legacy q = markovZN u := by
  subst hu
  rw [markovZN_legacy, Real.sqrt_sq hu0, markovZN]
  rcases hu0.lt_or_eq with h | h
  · field_simp
  · subst h; simp

end QOU.BraidKnot
