/-
  Bar-parity energy decomposition — the 𝔇 (decay-width) reinterpretation.

  Every binding energy splits under the bar involution σ (the substrate
  q ↦ q⁻¹) into a bar-EVEN "retained" channel (cosh — binding proper) and a
  bar-ODD "emitted" channel (sinh — the radiated γγ̄ / decay-width 𝔇 sector).
  This is the complex-volume 𝔙 = Vol + i·CS shape read at the energy level,
  and it is exactly the split the mass-binding dashboard already tabulates as
  the `retained E` / `emitted E` columns.

  The "reinterpret E_unit via 𝔇" statement is: the deuteron unit lives in the
  bar-ODD (emitted / decay-width) channel, `E_unit = ℏ/𝔇`, which this file
  makes precise via the canonical bar-parity projection.

  Content:
    * evenPart / oddPart — the σ-parity projections (retained / emitted)
    * evenPart_barEven, oddPart_barOdd — each projection has its parity
    * even_add_odd — reconstruction E = retained + emitted (char ≠ 2)
    * oddPart_eq_zero_iff_barEven — the emitted channel vanishes iff E is
      purely retained (pure binding, no decay channel)
    * retained_emitted_of_frakD — if `E_unit = ℏ/𝔇` with the width datum 𝔇
      bar-odd, then E_unit is its own emitted part (purely decay-channel)

  Generic field with an involutive ring endomorphism; no ℝ, no √ (§7c).

  -- Ref: [neumann-zagier1985] https://doi.org/10.1007/BF01388558
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

import Mathlib.Tactic

namespace QOU.MassTheory.FrakD

variable {F : Type*} [Field F]
variable (σ : F →+* F)

/-- Bar-even ("retained", cosh) projection `(E + σE)/2`. -/
def evenPart (E : F) : F := (E + σ E) / 2

/-- Bar-odd ("emitted", sinh — the decay-width 𝔇 channel) projection
    `(E − σE)/2`. -/
def oddPart (E : F) : F := (E - σ E) / 2

section Involutive
variable (hσ : Function.Involutive σ)

include hσ in
/-- The retained part is bar-even: `σ(retained E) = retained E`. -/
theorem evenPart_barEven (E : F) : σ (evenPart σ E) = evenPart σ E := by
  unfold evenPart
  rw [map_div₀, map_add, hσ E, map_ofNat]
  ring

include hσ in
/-- The emitted part is bar-odd: `σ(emitted E) = −emitted E` — the sinh /
    decay-width channel. -/
theorem oddPart_barOdd (E : F) : σ (oddPart σ E) = - oddPart σ E := by
  unfold oddPart
  rw [map_div₀, map_sub, hσ E, map_ofNat]
  ring

end Involutive

/-- **Reconstruction.** `E = retained E + emitted E` (char ≠ 2): every energy
    is its bar-even binding part plus its bar-odd decay part. -/
theorem even_add_odd (hchar : (2 : F) ≠ 0) (E : F) :
    evenPart σ E + oddPart σ E = E := by
  unfold evenPart oddPart
  field_simp
  ring

/-- **Pure-binding criterion.** The emitted (decay-width) channel vanishes iff
    `E` is bar-even: a nucleus radiates no γγ̄ / carries no 𝔇 channel exactly
    when its binding is purely retained. -/
theorem oddPart_eq_zero_iff_barEven (hchar : (2 : F) ≠ 0) (E : F) :
    oddPart σ E = 0 ↔ σ E = E := by
  unfold oddPart
  rw [div_eq_zero_iff]
  constructor
  · rintro (h | h)
    · exact (sub_eq_zero.mp h).symm
    · exact absurd h hchar
  · intro h; left; rw [h]; ring

/-- **The 𝔇 reinterpretation.** If the deuteron unit is a decay-width energy
    `E_unit = U` with `U` bar-odd (`σ U = -U` — the width datum `ℏ/𝔇` lives in
    the emitted/sinh sector), then `E_unit` equals its own emitted part and
    has zero retained part: it is a *purely decay-channel* energy. -/
theorem frakD_is_pure_emitted (hchar : (2 : F) ≠ 0) (U : F) (hU : σ U = -U) :
    oddPart σ U = U ∧ evenPart σ U = 0 := by
  refine ⟨?_, ?_⟩
  · unfold oddPart; rw [hU]; field_simp; ring
  · unfold evenPart; rw [hU]; ring

end QOU.MassTheory.FrakD
