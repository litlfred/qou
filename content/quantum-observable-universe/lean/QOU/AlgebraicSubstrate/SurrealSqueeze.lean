import Mathlib.Algebra.Order.Field.Basic
import QOU.AppendixSurreals.Basic

/-!
# QOU.AlgebraicSubstrate.SurrealSqueeze — the squeeze lemma

The common punchline of every millennium-problem remark in the
paper: for every standard real `δ > 0`, the cost `δ² · ε⁻¹` of a
standard-scale deviation strictly exceeds the mass-gap budget `ε³`
in the ordered field `ℝ(ε) ⊂ 𝐍𝐨`.

Informal proof: multiply the claim by `ε > 0` to reduce to
`δ² > ε⁴`, which holds because `δ²` is a strictly positive
standard real and `ε⁴` is a positive infinitesimal.

Two formalisations are provided:

1. **surreal_squeeze** — the surreal-field version with the
   intended hypotheses (ε infinitesimal in some SurrealField K,
   δ a positive standard real).  Proved using the
   IsInfinitesimal infrastructure from QOU.AppendixSurreals.Basic.

2. **surreal_squeeze_of_pow_lt** — the abstract pure-algebra form
   over any linearly ordered field, taking the substantive size
   separation ε^4 < δ^2 directly as a hypothesis.  Used internally
   by surreal_squeeze and available to callers who already control
   the ε^4 < δ^2 bound by other means.

LaTeX label: `lem:surreal-squeeze`.

## References

- [conway1976] Conway, *On Numbers and Games*, §0.
- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*. DOI:10.1017/CBO9780511629143.
-/

namespace QOU.AlgebraicSubstrate

universe u

/-- **surreal_squeeze (provable form)**: with the sharper hypothesis
    `ε^4 < δ^2` (which captures the substantive size separation
    between standard δ and infinitesimal ε), the conclusion holds in
    any `LinearOrderedField`. This is the form callers should use;
    `surreal_squeeze` above is the loose-hypothesis version that
    requires a surreal-completion model. -/
theorem surreal_squeeze_of_pow_lt
    {F : Type u} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (ε δ : F) (hε : 0 < ε) (hsq : ε^4 < δ^2) :
    δ^2 * ε⁻¹ > ε^3 := by
  -- Multiply both sides by ε > 0:
  --   δ²·ε⁻¹ > ε³ ⟺ δ²·ε⁻¹·ε > ε³·ε ⟺ δ² > ε⁴ ✓ (hsq).
  -- Avoid divison-tactic name churn by manipulating the inequality
  -- directly: multiply both sides of `hsq : ε⁴ < δ²` by `ε⁻¹ > 0`.
  have hε_inv : 0 < ε⁻¹ := inv_pos.mpr hε
  have hε_ne : ε ≠ 0 := ne_of_gt hε
  have key : ε^4 * ε⁻¹ < δ^2 * ε⁻¹ :=
    (mul_lt_mul_right hε_inv).mpr hsq
  -- Reduce ε^4 * ε⁻¹ = ε^3 by `pow_succ` + `mul_inv_cancel`.
  have h_pow : ε^4 * ε⁻¹ = ε^3 := by
    rw [show (4 : ℕ) = 3 + 1 from rfl, pow_succ, mul_assoc,
        mul_inv_cancel₀ hε_ne, mul_one]
  rw [h_pow] at key
  exact key

/-- **surreal_squeeze**: in any `SurrealField K`, for every strictly
    positive infinitesimal `ε ∈ K` and every strictly positive standard
    real `δ`, the cost `(ofReal δ)² · ε⁻¹` of a standard-scale deviation
    strictly exceeds the mass-gap budget `ε³`.

    This is the surreal-coefficient version intended by the paper
    (`lem:surreal-squeeze`).  The proof reduces — via
    `surreal_squeeze_of_pow_lt` — to the size separation
    `ε⁴ < (ofReal δ)²`, which holds because `ε⁴` is infinitesimal
    (closure of infinitesimals under multiplication by finite
    elements, applied iteratively) and `(ofReal δ)²` is a strictly
    positive standard real.

    Ref: [conway1976] https://doi.org/10.1201/9781439864159
    Ref: [gonshor1986] https://doi.org/10.1017/CBO9780511629143 -/
theorem surreal_squeeze
    {K : Type u} [QOU.AppendixSurreals.SurrealField K]
    (ε : K) (δ : ℝ)
    (hε : 0 < ε) (hε_inf : QOU.AppendixSurreals.SurrealField.IsInfinitesimal ε)
    (hδ : 0 < δ) :
    (QOU.AppendixSurreals.SurrealField.ofReal δ : K)^2 * ε⁻¹ > ε^3 := by
  -- Strategy: reduce to `surreal_squeeze_of_pow_lt` with `δ' := ofReal δ`.
  -- Need `ε^4 < (ofReal δ)^2`.  Since `ε^4` is infinitesimal and
  -- `(ofReal δ)^2 = ofReal (δ^2)` is a strictly positive standard real,
  -- the inequality follows directly from `IsInfinitesimal`.
  --
  -- (ofReal δ)^2 = ofReal (δ^2)
  have hpow_ofReal :
      (QOU.AppendixSurreals.SurrealField.ofReal δ : K)^2
        = QOU.AppendixSurreals.SurrealField.ofReal (δ^2) :=
    (map_pow _ _ _).symm
  -- ε^4 is infinitesimal: ε * (ε * (ε * ε)) with the leftmost ε
  -- carrying the `IsInfinitesimal` flag and the rest carrying
  -- `IsFinite` (since infinitesimals are finite).
  have hε_fin : QOU.AppendixSurreals.SurrealField.IsFinite ε :=
    hε_inf.isFinite
  have hε2_fin : QOU.AppendixSurreals.SurrealField.IsFinite (ε * ε) :=
    hε_fin.mul hε_fin
  have hε3_fin : QOU.AppendixSurreals.SurrealField.IsFinite (ε * (ε * ε)) :=
    hε_fin.mul hε2_fin
  have hε4_inf : QOU.AppendixSurreals.SurrealField.IsInfinitesimal
      (ε * (ε * (ε * ε))) :=
    hε_inf.mul_finite hε3_fin
  -- Rewrite ε^4 = ε * (ε * (ε * ε)).
  have hε4_eq : ε^4 = ε * (ε * (ε * ε)) := by ring
  -- δ^2 > 0 in ℝ.
  have hδ_sq_pos : (0 : ℝ) < δ^2 := by positivity
  -- |ε^4| < ofReal (δ^2) from the infinitesimal definition.
  have habs : |ε * (ε * (ε * ε))|
      < (QOU.AppendixSurreals.SurrealField.ofReal (δ^2) : K) :=
    hε4_inf (δ^2) hδ_sq_pos
  -- ε^4 ≥ 0, so |ε^4| = ε^4.
  have hε4_nonneg : 0 ≤ ε * (ε * (ε * ε)) := by
    have h : 0 ≤ ε^4 := by positivity
    rw [hε4_eq] at h; exact h
  have habs_eq : |ε * (ε * (ε * ε))| = ε * (ε * (ε * ε)) :=
    abs_of_nonneg hε4_nonneg
  rw [habs_eq] at habs
  -- Assemble: ε^4 < (ofReal δ)^2.
  have hsq : ε^4 < (QOU.AppendixSurreals.SurrealField.ofReal δ : K)^2 := by
    rw [hε4_eq, hpow_ofReal]; exact habs
  -- Apply the abstract pure-algebra form.
  exact surreal_squeeze_of_pow_lt ε
    (QOU.AppendixSurreals.SurrealField.ofReal δ) hε hsq

end QOU.AlgebraicSubstrate
