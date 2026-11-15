/-
  Bar-parity energy decomposition — the bar-skew reinterpretation.

  Every binding energy splits under the bar involution σ (the substrate
  q ↦ q⁻¹) into a bar-EVEN "retained" channel (cosh — binding proper) and a
  bar-ODD "emitted" channel (sinh — the radiated γγ̄ / bar-skew sector P_skew).
  This is the complex-volume 𝔙 = Vol + i·CS shape read at the energy level,
  and it is exactly the split the mass-binding dashboard already tabulates as
  the `retained E` / `emitted E` columns.

  The "reinterpret E_unit via 𝔇" statement is: the deuteron unit lives in the
  bar-ODD (emitted / decay-width) channel, `E_unit = ℏ/𝔇`, which this file
  makes precise via the canonical bar-parity projection.

  Content:
    * evenPart / oddPart — the σ-parity projections (retained / emitted)
    * evenPart_barEven, oddPart_barOdd — each projection has its parity
    * even_add_odd — reconstruction E = retained + emitted
    * oddPart_eq_zero_iff_barEven — the emitted channel vanishes iff E is
      purely retained (pure binding, no decay channel)
    * frakD_is_pure_emitted — if `E_unit = ℏ/𝔇` with the width datum 𝔇
      bar-odd, then E_unit is its own emitted part (purely decay-channel)

  Base ring (AGENTS.md §7c). A generic commutative ring `{R : Type*}
  [CommRing R]` with an involutive ring endomorphism, plus `[Invertible
  (2 : R)]` for the halving in the projections — written `⅟(2 : R)`, so no
  division and no field appears. This is exactly the §7c prescription for a
  `/2` over a `CommRing`, and it is *stronger* than the old field statements:
  `Invertible 2` subsumes the `(2 : F) ≠ 0` side conditions those carried, so
  they are gone from the signatures. No ℝ, no √, no ordering.

  -- Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Data.Nat.Cast.Basic
import Mathlib.Algebra.Ring.Invertible
import Mathlib.Logic.Function.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

namespace QOU.MassTheory.FrakD

variable {R : Type*} [CommRing R] [Invertible (2 : R)]
variable (σ : R →+* R)

/-- A ring endomorphism fixes `⅟2`: it fixes `2`, so `σ(⅟2)` is a left
    inverse of `2` and hence *is* `⅟2`.  (The analogue of `map_div₀` /
    `map_ofNat` for the `Invertible` halving.) -/
theorem map_invOf_two : σ (⅟(2 : R)) = ⅟(2 : R) := by
  have h2 : σ (2 : R) = (2 : R) := map_ofNat σ 2
  have h : σ (⅟(2 : R)) * (2 : R) = 1 := by
    calc σ (⅟(2 : R)) * (2 : R) = σ (⅟(2 : R)) * σ (2 : R) := by rw [h2]
      _ = σ (⅟(2 : R) * (2 : R)) := (map_mul σ _ _).symm
      _ = σ 1 := by rw [invOf_mul_self]
      _ = 1 := map_one σ
  exact (invOf_eq_left_inv h).symm

/-- Bar-even ("retained", cosh) projection `(E + σE)/2`. -/
def evenPart (E : R) : R := (E + σ E) * ⅟(2 : R)

/-- Bar-odd ("emitted", sinh — the bar-skew channel P_skew) projection
    `(E − σE)/2`. -/
def oddPart (E : R) : R := (E - σ E) * ⅟(2 : R)

section Involutive
variable (hσ : Function.Involutive σ)

include hσ in
/-- The retained part is bar-even: `σ(retained E) = retained E`. -/
theorem evenPart_barEven (E : R) : σ (evenPart σ E) = evenPart σ E := by
  unfold evenPart
  rw [map_mul, map_add, hσ E, map_invOf_two]
  ring

include hσ in
/-- The emitted part is bar-odd: `σ(emitted E) = −emitted E` — the sinh /
    decay-width channel. -/
theorem oddPart_barOdd (E : R) : σ (oddPart σ E) = - oddPart σ E := by
  unfold oddPart
  rw [map_mul, map_sub, hσ E, map_invOf_two]
  ring

end Involutive

/-- **Reconstruction.** `E = retained E + emitted E`: every energy is its
    bar-even binding part plus its bar-odd decay part. -/
theorem even_add_odd (E : R) :
    evenPart σ E + oddPart σ E = E := by
  have h : (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self 2
  unfold evenPart oddPart
  linear_combination E * h

/-- **Pure-binding criterion.** The emitted (bar-skew) channel vanishes iff
    `E` is bar-even: a nucleus radiates no γγ̄ / carries no 𝔇 channel exactly
    when its binding is purely retained. -/
theorem oddPart_eq_zero_iff_barEven (E : R) :
    oddPart σ E = 0 ↔ σ E = E := by
  unfold oddPart
  constructor
  · intro h
    have h2 : E - σ E = 0 := by
      have hmul : (E - σ E) * (⅟(2 : R) * (2 : R)) = 0 := by
        rw [← mul_assoc, h, zero_mul]
      rwa [invOf_mul_self, mul_one] at hmul
    exact (sub_eq_zero.mp h2).symm
  · intro h; rw [h]; ring

/-- **The 𝔇 reinterpretation.** If the deuteron unit is a bar-odd energy
    `E_unit = U` with `U` bar-odd (`σ U = -U` — the width datum `ℏ/𝔇` lives in
    the emitted/sinh sector), then `E_unit` equals its own emitted part and
    has zero retained part: it is a *purely decay-channel* energy. -/
theorem frakD_is_pure_emitted (U : R) (hU : σ U = -U) :
    oddPart σ U = U ∧ evenPart σ U = 0 := by
  have h : (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self 2
  refine ⟨?_, ?_⟩
  · unfold oddPart; rw [hU]; linear_combination U * h
  · unfold evenPart; rw [hU]; ring

end QOU.MassTheory.FrakD
