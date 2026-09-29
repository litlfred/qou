import Mathlib.Tactic

/-!
# QOU.Observations.centered_hecke_variance_positive

**Canonical declaration** for content block
[`prop:centered-hecke-variance-positive`](../../../quantum-observable-universe/observations/centered-hecke-variance-positive.md): *the centred Hecke generator has strictly positive variance*.

## Base ring (§7c)

Under **convention D** (`z = q³/(q²+1)`, owner ruling 2026-08-09) the Markov
parameter is a rational function of `q`: no radical is taken anywhere in this
file, so every statement below is ordered-field algebra and the scalars are a
generic `R` with `[Field R] [LinearOrder R] [IsStrictOrderedRing R]`. The
substrate evaluation `Var(σ_i) ≈ 0.75270211325196540159` at `q₀ ≈ 1.10998` is
the instantiation `R := ℝ` and lives on the archimedean side of the wall.

## Convention-D rewrite (2026-08-29)

This module previously stated the block's **convention-C** form
`z = 1/(q^{1/2} + q^{-1/2})` and quoted `Var ≈ 0.855` at `q₀` — a figure the
`.md` explicitly **withdrew** on 2026-08-09 when the block was corrected to
convention D. The module is not imported by `QOU.lean`, so it was never
compiled and the drift was never surfaced.

The rewrite is also a **strengthening**, and the reason is worth recording. The
old encoding was `§3b`-conditional: it carried

    term1_pos : 0 < (q - q⁻¹) * z
    term2_pos : 0 < 1 - z ^ 2

as context-class axioms and obtained positivity by `linarith` from them. Under
convention D those two hypotheses are **not** jointly satisfiable on the domain
the `.md` claims. `term1_pos` forces `q > 1`; `term2_pos` is `z < 1`, i.e.
`q³ < q² + 1`, forcing `q < ψ` where `ψ = 1.465571231876768…` is the
supergolden ratio. So the class was inhabited only on `q ∈ (1, ψ)` — a fact
stated nowhere — while the `.md` claims positivity for **every** `q > 0`. The
substrate `q₀ ≈ 1.10998` sits inside that window, which is why the restriction
went unnoticed.

Worse for the block's two headline claims: `q = 1` is *excluded* (there
`q - q⁻¹ = 0`, so `term1_pos` fails), and `q = 1` is exactly where the `.md`
now says the minimum `3/4` is **attained**. The old encoding could not express
the strengthening its own `.md` had just made.

Splitting `Var` into two separately-positive pieces is therefore the wrong
decomposition under D. The closed form `(q⁴ + q² + 1)/(q² + 1)²` is a ratio of
manifestly positive polynomials, so positivity needs no hypothesis beyond
`q ≠ 0`, and the minimum falls out of the exact identity
`Var - 3/4 = (q² - 1)²/(4(q² + 1)²)`. Everything below is unconditional and
sorry-free; there is no context class and no axiom.
-/

namespace QOU.Observations

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Markov parameter in **convention D**: `z = q³/(q² + 1)`
(owner ruling 2026-08-09; convention C `z = 1/(q^{1/2} + q^{-1/2})` excised). -/
def markovZD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- The centred Hecke generator is `σ̃ᵢ := σᵢ - z · 1`; its variance under the
Markov trace is `Var(σᵢ) = tr_M(σ̃ᵢ²) = (q - q⁻¹) z + 1 - z²`. -/
def centeredVariance (q : R) : R :=
  (q - q⁻¹) * markovZD q + 1 - markovZD q ^ 2

/-- `q² + 1` is strictly positive in any strict ordered field, so it is a
legitimate denominator. -/
theorem sq_add_one_pos (q : R) : 0 < q ^ 2 + 1 := by positivity

/-- **Closed form.** `Var(σᵢ) = (q⁴ + q² + 1)/(q² + 1)²`.

This is the identity the block's `.md` states under convention D.

No `q ≠ 0` hypothesis is needed. The block reads `q > 0` throughout and `q⁻¹`
is only meaningful there, but Mathlib's `0⁻¹ = 0` makes both sides equal `1` at
`q = 0` as well, so the identity is unconditional as stated in Lean. The
hypothesis was carried in a first draft and removed once the linter showed it
unused — recorded here so a reader does not re-add it. -/
theorem centeredVariance_closed_form (q : R) :
    centeredVariance q = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
  have h1 : q ^ 2 + 1 ≠ 0 := ne_of_gt (sq_add_one_pos q)
  unfold centeredVariance markovZD
  field_simp
  ring

/-- **Positivity, unconditional.** For every `q ≠ 0`, `0 < Var(σᵢ)`.

No regime hypothesis is needed: under convention D the closed form is a ratio of
manifestly positive polynomials. In particular positivity holds at `q = 1` and
for all `q < 1`, both of which the previous class-axiomatised encoding excluded. -/
theorem centeredVariance_pos (q : R) : 0 < centeredVariance q := by
  rw [centeredVariance_closed_form q]
  have hnum : (0 : R) < q ^ 4 + q ^ 2 + 1 := by positivity
  have hden : (0 : R) < (q ^ 2 + 1) ^ 2 := by positivity
  exact div_pos hnum hden

/-- **Exact gap to the minimum.** `Var(σᵢ) - 3/4 = (q² - 1)²/(4(q² + 1)²)`. -/
theorem centeredVariance_sub_three_quarters (q : R) :
    centeredVariance q - 3 / 4 = (q ^ 2 - 1) ^ 2 / (4 * (q ^ 2 + 1) ^ 2) := by
  have h1 : q ^ 2 + 1 ≠ 0 := ne_of_gt (sq_add_one_pos q)
  rw [centeredVariance_closed_form q]
  field_simp
  ring

/-- **Lower bound.** `3/4 ≤ Var(σᵢ)` for every `q ≠ 0`. -/
theorem three_quarters_le_centeredVariance (q : R) :
    3 / 4 ≤ centeredVariance q := by
  have h := centeredVariance_sub_three_quarters q
  have hgap : (0 : R) ≤ (q ^ 2 - 1) ^ 2 / (4 * (q ^ 2 + 1) ^ 2) := by positivity
  linarith [h, hgap]

/-- **The minimum is attained exactly at `q = 1`.** For `q ≠ 0`,
`Var(σᵢ) = 3/4 ↔ q² = 1`.

Over `ℝ` with `q > 0` this is `q = 1` and only there — the `.md`'s claim, which
the previous encoding could not state because its `term1_pos` axiom fails
precisely at `q = 1`. -/
theorem centeredVariance_eq_three_quarters_iff (q : R) :
    centeredVariance q = 3 / 4 ↔ q ^ 2 = 1 := by
  have h := centeredVariance_sub_three_quarters q
  have hden : (4 : R) * (q ^ 2 + 1) ^ 2 ≠ 0 := ne_of_gt (by positivity)
  constructor
  · intro hv
    rw [hv] at h
    have hz : (q ^ 2 - 1) ^ 2 / (4 * (q ^ 2 + 1) ^ 2) = 0 := by linarith
    rcases div_eq_zero_iff.mp hz with h1 | h2
    · have hq1 : q ^ 2 - 1 = 0 := by
        by_contra hne
        exact pow_ne_zero 2 hne h1
      linarith
    · exact absurd h2 hden
  · intro hq1
    rw [hq1] at h
    norm_num at h
    linarith

/-- **The old convention-C decomposition is not available under D.**
The discarded hypothesis `0 < (q - q⁻¹) * z` forces `1 < q`: it is false at
`q = 1`, where the variance nevertheless attains its minimum `3/4 > 0`.

This is the concrete witness that the previous encoding's domain was strictly
smaller than the `.md`'s. Stated over `ℚ` so it is a closed arithmetic fact. -/
theorem old_term1_pos_fails_at_one :
    ¬ (0 : ℚ) < (1 - (1 : ℚ)⁻¹) * markovZD (1 : ℚ) ∧
      centeredVariance (1 : ℚ) = 3 / 4 := by
  constructor
  · unfold markovZD; norm_num
  · unfold centeredVariance markovZD; norm_num

end QOU.Observations
