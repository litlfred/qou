import QOU.StandardModel.ElectronWordTrace

/-!
# The photon on the electron, and the electron cube

Two facts about the words that enter the `α_em` functional `τ = χ₃ − χ₁₁₁`.

* The photon `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` has four terms. Its chiral vertex
  `σ₀σ₁⁻¹` has writhe 0, so `τ` vanishes on it; the two single letters carry
  `q + q⁻¹` each.
* `(σ₀σ₁)⁵` (the `T(3,5)` braid, writhe 10) equals the electron cubed times one
  photon letter, `(σ₀σ₁σ₀)³ σ₁`, on every irreducible block of `H₃(q)`. This is the
  braid identity `(σ₀σ₁)⁵ = Δ²·Δ·σ₁`, with `Δ = σ₀σ₁σ₀` the electron word and
  `Δ² = (σ₀σ₁)³` the full twist, which acts as `1` on the hook block.

These are statements about which words occur. They do not say why `α_em` should
read the writhe-10 word, and they fix no value.
-/

namespace QOU.AlphaEM.PhotonElectron

open Matrix QOU.AlphaEM.IotaOdd QOU.AlphaEM.ElectronWord

variable {K : Type*} [Field K]

/-- The photon's chiral vertex `σ₀σ₁⁻¹`. -/
def chiralVertex : List Letter := [(0, true), (1, false)]

/-- `(σ₀σ₁)⁵`, the `T(3,5)` braid. -/
def t35 : List Letter :=
  [(0, true), (1, true), (0, true), (1, true), (0, true), (1, true),
   (0, true), (1, true), (0, true), (1, true)]

/-- The electron cubed times the photon letter `σ₁`. -/
def electronCubeTimesS1 : List Letter := electron ++ electron ++ electron ++ [(1, true)]

/-- **`τ` vanishes on the chiral vertex** (writhe 0). -/
theorem chiralVertex_tau (q : K) (hq : q ≠ 0) :
    symWord q chiralVertex - altWord q chiralVertex = 0 := by
  simp [symWord, altWord, chiralVertex, symLetter, altLetter]
  field_simp
  ring

/-- **`τ` on a single photon letter is `q + q⁻¹`.** -/
theorem letter_tau (q : K) (i : Fin 2) :
    symWord q [(i, true)] - altWord q [(i, true)] = q + q⁻¹ := by
  simp [symWord, altWord, symLetter, altLetter]

/-- **The full twist `Δ² = electron²` acts as `1` on the hook block.** -/
theorem electron_sq_hook (q : K) (hq : q ≠ 0) :
    hookWord q (electron ++ electron) = 1 := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [hookWord, electron, hookLetter, hookGen, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> (try ring_nf) <;> simp

/-- **`T(3,5) = electron³ · σ₁` on the hook block.** -/
theorem t35_hook (q : K) (hq : q ≠ 0) :
    hookWord q t35 = hookWord q electronCubeTimesS1 := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [hookWord, t35, electronCubeTimesS1, electron, hookLetter, hookGen,
      Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> (try ring_nf) <;> simp

/-- **`T(3,5) = electron³ · σ₁` on the two one-dimensional blocks.** -/
theorem t35_sym_alt (q : K) :
    symWord q t35 = symWord q electronCubeTimesS1 ∧
      altWord q t35 = altWord q electronCubeTimesS1 := by
  constructor <;>
    simp [symWord, altWord, t35, electronCubeTimesS1, electron, symLetter, altLetter]

end QOU.AlphaEM.PhotonElectron
