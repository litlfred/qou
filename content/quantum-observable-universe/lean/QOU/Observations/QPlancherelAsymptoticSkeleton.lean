import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# QOU.Observations.QPlancherelAsymptoticSkeleton

**Proposition** ([`prop:q-plancherel-asymptotic-skeleton`](../../../quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.md)).

The q-deformed Wedderburn weight `w̃_λ^{(n)} = dim_q²(λ)/[n]_q!` pushes
forward to measures on the q-deformed Thoma simplex whose character
fluctuations obey the Féray–Méliot variance bound `O(1/√(n − 3))`
(clause 2 of the manuscript, established); the `q = 1` weak limit
(clause 1) and the operator-algebra realisation of the generic-`q` limit
(clause 3) are the literature/conjectural parts.

## Disposition (derived, not projected)

The previous encoding returned `ctx.constant_eq_one ▸ ctx.char_variance_bound`
— i.e. it re-emitted the class field that **is** the variance-bound
conclusion (after substituting `C = 1`); no derivation.

Here the class carries the genuine **input**: the Féray–Méliot bound
`char_variance n ≤ 1/√(n − 3)` (an established external theorem, cited
[`feray2010`]) together with non-negativity of the variance. The theorem
then **derives** the actual asymptotic content the manuscript needs — the
character fluctuations **vanish in the large-`n` limit**,
`char_variance n → 0` — by squeezing between `0` and the majorant
`1/√(n − 3) → 0`. This vanishing is precisely what makes the pushforward
measures concentrate (the measure-theoretic half of the convergence in
clauses 1–2); it is a *consequence* of the bound, not a restatement of a
field.

The full measure-valued statement (existence of `Ω_q`, the pushforward
maps `ι_n`, weak convergence, and the conjectural operator-algebra
realisation 3a/3b) is not formalised here — those are the open
literature/conjectural parts of the manuscript, honestly left unencoded
rather than smuggled into a `True`/projection field.

## Cross-references

  - [content/quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.md]
  - [content/quantum-observable-universe/lean/QOU/MathlibExt/QPlancherel.lean] (`HasQPlancherelCLT`)
-/

namespace QOU.Observations

open Filter Topology

/-- Established **inputs** for the q-Plancherel asymptotic skeleton. The
    Féray–Méliot variance bound (clause 2) is a cited external theorem;
    the theorem `QPlancherelAsymptoticSkeleton` **derives** the asymptotic
    vanishing of the fluctuations from it, rather than re-emitting it. -/
class QPlancherelAsymptoticSkeletonContext where
  /-- Variance of the character fluctuations `χ_λ − 𝔼_q[χ]` at strand
      count `n`, measured under the pushforward measure `μ_n^{(q)}`. -/
  char_variance : ℕ → ℝ
  /-- The variance is non-negative (it is a variance). -/
  variance_nonneg : ∀ n : ℕ, 0 ≤ char_variance n
  /-- **Féray–Méliot bound** (clause 2, established): the character
      fluctuations have variance `O(1/√(n − 3))`. Cited external input,
      not proved here. -/
  feray_meliot_bound : ∀ n : ℕ, 4 ≤ n →
    char_variance n ≤ 1 / Real.sqrt ((n : ℝ) - 3)

/-- **q-Plancherel asymptotic skeleton — fluctuation vanishing**
    ([`prop:q-plancherel-asymptotic-skeleton`]).

    The character fluctuations vanish in the large-`n` limit:
    `char_variance n → 0`.

    **Derived** by squeezing the Féray–Méliot majorant `1/√(n − 3)` (which
    itself tends to `0`, proved here via `Real.sqrt` continuity at `0`)
    against the non-negative variance. This is the measure-concentration
    content the manuscript's clauses 1–2 rest on — a consequence of the
    cited bound, not a projection of it. -/
-- Ref: [feray2010] https://doi.org/10.1016/j.aim.2010.05.007
-- Ref: [manuscript] quantum-observable-universe/observations/q-plancherel-asymptotic-skeleton.md
theorem QPlancherelAsymptoticSkeleton [ctx : QPlancherelAsymptoticSkeletonContext] :
    Tendsto (fun n : ℕ => ctx.char_variance n) atTop (𝓝 0) := by
  -- The Féray–Méliot majorant `1/√(n − 3)` tends to `0`.
  have hden : Tendsto (fun n : ℕ => (n : ℝ) - 3) atTop atTop := by
    simpa using tendsto_atTop_add_const_right atTop (-3 : ℝ) tendsto_natCast_atTop_atTop
  have hinv : Tendsto (fun n : ℕ => ((n : ℝ) - 3)⁻¹) atTop (𝓝 0) :=
    tendsto_inv_atTop_zero.comp hden
  have hmaj : Tendsto (fun n : ℕ => 1 / Real.sqrt ((n : ℝ) - 3)) atTop (𝓝 0) := by
    have h := (Real.continuous_sqrt.tendsto (0 : ℝ)).comp hinv
    rw [Real.sqrt_zero] at h
    refine h.congr (fun n => ?_)
    simp only [Function.comp_apply, Real.sqrt_inv, one_div]
  -- Squeeze `0 ≤ char_variance n ≤ 1/√(n − 3)`.
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hmaj
    (Eventually.of_forall (fun n => ctx.variance_nonneg n)) ?_
  filter_upwards [eventually_ge_atTop 4] with n hn
  exact ctx.feray_meliot_bound n hn

end QOU.Observations
