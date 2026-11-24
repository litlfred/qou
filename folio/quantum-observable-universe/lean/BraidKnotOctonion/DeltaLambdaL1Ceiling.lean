/-
  ℓ¹-ceiling for the per-block binding closure — sign-only fixes are
  structurally excluded.

  Companion to
    docs/audits/2026-06-28-delta-lambda-l1-ceiling-sign-only-prune.md
    computations/delta-lambda-l1-ceiling-sign-prune.witness.json

  Context.  The per-block binding closure (Track D / Option-E) is
    B(K)/m_e = Σ_λ y_λ(q₀) · χ^λ(β_K) · Δ_λ(K),
  with the proven chirality form (PR #2416, S5SO3FiberAction.lean,
  `binding_magnitude_eq_dim` + `deltaSign_mixed`)
    Δ_λ = sgn(w₀^{S_{λ'}}) · dim_λ.
  Write  aλ := y_λ · χ^λ · dim_λ  for the per-block MAGNITUDE carrier and
  let only the per-block SIGN sλ vary — any chirality rule replacing the
  proven sgn(w₀^{S_{λ'}}), so sλ = ±1, or more generally any bounded weight
  |sλ| ≤ 1.  The achievable binding magnitude is then capped by the ℓ¹ norm
  ‖a‖₁ = Σ |aλ|, INDEPENDENT of the sign choice (triangle inequality).

  Measured (the witness): ‖a‖₁ / |target| ∈ [0.36, 0.59] < 1 for D/T/³He/⁴He,
  so no sign-only re-derivation closes the binding deficit; a
  magnitude-adding ingredient is necessary.  This file machine-checks the
  LOGICAL CORE of that prune: the triangle ceiling and its strict-undershoot
  corollary.  It is the magnitude-side mirror of the PROBE-4 KL-positivity
  prune (signs ↛ magnitude, here; magnitude ↛ sign, there).

  Base ring: generic `[Field R] [LinearOrder R] [IsStrictOrderedRing R]`
  (§7c — the bound is purely algebraic; the archimedean evaluation at q₀
  instantiates `R := ℝ` in the witness, downstream of this file).

  -- Ref: [leitner2026] docs/audits/2026-06-28-delta-lambda-l1-ceiling-sign-only-prune.md
-/
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Field.Basic

namespace QOU.BraidsAndKnots

open Finset

variable {ι : Type*} {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **ℓ¹ ceiling.**  For per-block magnitude carriers `a : ι → R` and any
    per-block weight `s : ι → R` bounded by `1` in absolute value (in
    particular any chirality sign `s i = ±1`), the weighted sum is bounded
    in absolute value by the ℓ¹ norm `∑ |a i|`, for **every** `s`. -/
theorem abs_weighted_sum_le_l1 (S : Finset ι) (a s : ι → R)
    (hs : ∀ i ∈ S, |s i| ≤ 1) :
    |∑ i ∈ S, s i * a i| ≤ ∑ i ∈ S, |a i| := by
  calc |∑ i ∈ S, s i * a i|
      ≤ ∑ i ∈ S, |s i * a i| := Finset.abs_sum_le_sum_abs _ _
    _ = ∑ i ∈ S, |s i| * |a i| := by simp_rw [abs_mul]
    _ ≤ ∑ i ∈ S, |a i| := by
          refine Finset.sum_le_sum ?_
          intro i hi
          calc |s i| * |a i| ≤ 1 * |a i| :=
                mul_le_mul_of_nonneg_right (hs i hi) (abs_nonneg _)
            _ = |a i| := one_mul _

/-- **Sign-only prune.**  If the ℓ¹ ceiling `∑ |a i|` is strictly below the
    target magnitude `T`, then NO bounded weight reassignment reaches `T`:
    `|∑ s i * a i| < T` for every `s` with `|s i| ≤ 1`.  With
    `a := y_λ χ^λ dim_λ` and `s` the chirality sign, this is the structural
    exclusion behind the Δ_λ prune (the witness measures
    `∑ |a i| / T ∈ [0.36, 0.59] < 1`). -/
theorem weighted_sum_below_target (S : Finset ι) (a s : ι → R) (T : R)
    (hs : ∀ i ∈ S, |s i| ≤ 1) (hceil : ∑ i ∈ S, |a i| < T) :
    |∑ i ∈ S, s i * a i| < T :=
  lt_of_le_of_lt (abs_weighted_sum_le_l1 S a s hs) hceil

/-- **Chirality specialization.**  A genuine sign function (`s i = ±1`)
    satisfies `|s i| ≤ 1`, so the prune applies to ANY chirality rule
    replacing the proven `sgn(w₀^{S_{λ'}})`.  This is the exact statement
    used by the Δ_λ ℓ¹-ceiling prune. -/
theorem chirality_sum_below_target (S : Finset ι) (a s : ι → R) (T : R)
    (hs : ∀ i ∈ S, s i = 1 ∨ s i = -1) (hceil : ∑ i ∈ S, |a i| < T) :
    |∑ i ∈ S, s i * a i| < T := by
  refine weighted_sum_below_target S a s T (fun i hi => ?_) hceil
  rcases hs i hi with h | h <;> simp [h]

end QOU.BraidsAndKnots
