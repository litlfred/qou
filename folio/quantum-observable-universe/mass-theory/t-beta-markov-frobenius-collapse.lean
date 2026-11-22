/-
  # T_β = S · 1 — Markov-Frobenius min-norm collapse

  Sibling .lean for the `prop:t-beta-markov-frobenius-collapse` block.

  The block's claim is stated for any unital `R`-algebra `H` with an
  `R`-linear trace `τ` (`τ 1 = 1`) and an `R`-linear anti-involution
  `†` (`1† = 1`, `τ (X†) = τ X`), with the TWISTED Frobenius form
  `⟨X, Y⟩ = τ (X * Y†)`.  The two analytic inputs are hypotheses, not
  conclusions:

  * positivity `0 ≤ τ (Y * Y†)` — for the Jones–Markov trace on
    `H_n(R, q)` in the orthogonal seminormal form this is
    `Σ_λ y_λ ‖Y_λ‖²_F ≥ 0` with every `y_λ ≥ 0` (Wenzl);
  * non-degeneracy `τ (Y * Y†) = 0 → Y = 0`, needed only for the
    equality case (the block notes the minimiser is unique only up to
    the radical when this fails).

  The twist is essential: the untwisted `τ (X * X)` is not positive on
  `H_n` for `n ≥ 3` (the block's `σ₁σ₂ − σ₂σ₁` example).

  Replaces (bean `qou-uu6g`, 2026-11-22) a substrate-model statement
  `(h : X = S) : X * X = S * S := by rw [h]`, which proved nothing about
  the minimum-norm claim.

  Ref: [pr1750] https://github.com/litlfred/qou/pull/1750
       [jones1987] https://doi.org/10.2307/1971403
                   Theorem 6.1 (Markov-trace existence + uniqueness)
       [wenzl1988] https://doi.org/10.1007/BF02101492
                   Lemma 2.4 (non-degeneracy of the Markov trace)
       docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace QOU.QBeta.MarkovFrobeniusCollapse

/-- **Completing the square for the twisted Frobenius form.**

    For any `X ∈ H` and `S ∈ R`,
    `τ (X X†) = τ ((X − S·1)(X − S·1)†) + 2 S τ(X) − S²`.
    Pure algebra: no order on `R` is used. -/
theorem twisted_completing_the_square {R H : Type*} [CommRing R] [Ring H] [Algebra R H]
    (τ : H →ₗ[R] R) (dag : H →ₗ[R] H)
    (hτ1 : τ 1 = 1) (hdag1 : dag 1 = 1) (hτdag : ∀ X, τ (dag X) = τ X)
    (X : H) (S : R) :
    τ (X * dag X) = τ ((X - S • 1) * dag (X - S • 1)) + 2 * S * τ X - S * S := by
  have hd : dag (X - S • (1 : H)) = dag X - S • 1 := by
    rw [map_sub, map_smul, hdag1]
  rw [hd]
  have hexp : (X - S • (1 : H)) * (dag X - S • 1)
      = X * dag X - S • X - S • dag X + (S * S) • 1 := by
    simp only [sub_mul, mul_sub, mul_smul_comm, smul_mul_assoc, one_mul, mul_one, smul_smul,
      smul_sub]
    abel
  rw [hexp, map_add, map_sub, map_sub, map_smul, map_smul, map_smul, hτdag, hτ1]
  simp only [smul_eq_mul, mul_one]
  ring

variable {R H : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
  [Ring H] [Algebra R H]

/-- **Min-Frobenius-norm bound.**  If `τ` is positive on the twisted
    squares `Y Y†`, every `X` with `τ X = S` has `S² ≤ ‖X‖²_τ = τ (X X†)`. -/
theorem t_beta_min_norm (τ : H →ₗ[R] R) (dag : H →ₗ[R] H)
    (hτ1 : τ 1 = 1) (hdag1 : dag 1 = 1) (hτdag : ∀ X, τ (dag X) = τ X)
    (hpos : ∀ Y, 0 ≤ τ (Y * dag Y)) (X : H) (S : R) (hX : τ X = S) :
    S * S ≤ τ (X * dag X) := by
  have h := twisted_completing_the_square τ dag hτ1 hdag1 hτdag X S
  have hp := hpos (X - S • 1)
  rw [hX] at h
  nlinarith

/-- **T_β = S · 1 (the collapse).**  Under positivity and non-degeneracy
    of the twisted form, among all `X` with `τ X = S` the bound `S²` is
    attained exactly at `X = S · 1`. -/
theorem t_beta_collapse (τ : H →ₗ[R] R) (dag : H →ₗ[R] H)
    (hτ1 : τ 1 = 1) (hdag1 : dag 1 = 1) (hτdag : ∀ X, τ (dag X) = τ X)
    (hpos : ∀ Y, 0 ≤ τ (Y * dag Y)) (hnd : ∀ Y, τ (Y * dag Y) = 0 → Y = 0)
    (S : R) :
    (∀ X : H, τ X = S → S * S ≤ τ (X * dag X)) ∧
      (∀ X : H, τ X = S → (τ (X * dag X) = S * S ↔ X = S • 1)) := by
  refine ⟨fun X hX => t_beta_min_norm τ dag hτ1 hdag1 hτdag hpos X S hX, fun X hX => ?_⟩
  have h := twisted_completing_the_square τ dag hτ1 hdag1 hτdag X S
  rw [hX] at h
  constructor
  · intro he
    exact sub_eq_zero.mp (hnd _ (by linarith))
  · rintro rfl
    rw [h, sub_self, zero_mul, map_zero]
    ring

end QOU.QBeta.MarkovFrobeniusCollapse
