/-
  The electron `σ₀σ₁σ₀` IS a two-photon product in the Temperley–Lieb quotient of
  `H₃(q)` (the two-dimensional block plus the trivial character; the sign character
  dropped). Companion to `ElectronNotTwoPhoton`, which proves the negative when the sign
  character is kept.

  Photon (owner ruling 2026-11-20): `γ(a, b, c) = 1 + a·σ₀ + b·σ₁ + c·σ₀σ₁⁻¹`.

  Explicit family (field `R`; `q`, `q - 1`, `q + 1`, `q⁴ + 1`, `q⁴ - q² + 1` all nonzero):
  * `γ₁ = γ(0, -q³/(q⁴-q²+1), -1)`,
  * `γ₂ = γ(-q³(q⁴-q²+2)/D, -q(q⁴-q²+1)/((q-1)(q+1)(q⁴+1)), q²(q³-q²+1)(q³+q²-1)/D)`,
    `D = (q-1)(q+1)(q⁴+1)(q⁴-q²+1)`,
  * `λ = q/((q-1)(q+1)(q⁴-q²+1)²)`.

  Results.
  * `electron_two_photon_block`: `photonMat γ₁ * photonMat γ₂ = λ • electronMat`.
  * `electron_two_photon_triv`: `trivPhoton γ₁ * trivPhoton γ₂ = λ * q³`.
  * `lam_ne_zero`: `λ ≠ 0`.
  * `electron_two_photon_sign_defect`: under the sign character the product misses
    `-λ/q³` by exactly `(q²+1)(q²-q+1)(q²+q+1)/(q²(q-1)(q+1)(q⁴+1))`. This is the defect
    `ElectronNotTwoPhoton.electron_not_two_photon` shows cannot be removed.

  The Wedderburn bridge (block identities ⇔ identity in the TL quotient of `H₃(q)`) is not
  formalised here; the statements are the block identities themselves.

  Data: `computations/probes/proton_q3_photon_factorisation/electron_two_photon_tl_probe.py`.

  -- Ref: [leitner2026] def:photon; audit 2026-11-21-proton-q3-kl-coordinate
-/
import QOU.MassTheory.ElectronNotTwoPhoton

namespace QOU.MassTheory.ElectronTwoPhotonTL

open Matrix QOU.MassTheory.ElectronNotTwoPhoton

variable {R : Type*} [Field R]

/-- `D = (q-1)(q+1)(q⁴+1)(q⁴-q²+1)`. -/
def den (q : R) : R := (q - 1) * (q + 1) * (q ^ 4 + 1) * (q ^ 4 - q ^ 2 + 1)

/-- Coefficients of `γ₁ = γ(0, -q³/(q⁴-q²+1), -1)`. -/
def a₁ (_q : R) : R := 0
def b₁ (q : R) : R := -q ^ 3 / (q ^ 4 - q ^ 2 + 1)
def c₁ (_q : R) : R := -1

/-- Coefficients of `γ₂`. -/
def a₂ (q : R) : R := -q ^ 3 * (q ^ 4 - q ^ 2 + 2) / den q
def b₂ (q : R) : R := -q * (q ^ 4 - q ^ 2 + 1) / ((q - 1) * (q + 1) * (q ^ 4 + 1))
def c₂ (q : R) : R := q ^ 2 * (q ^ 3 - q ^ 2 + 1) * (q ^ 3 + q ^ 2 - 1) / den q

/-- The scalar `λ = q/((q-1)(q+1)(q⁴-q²+1)²)`. -/
def lam (q : R) : R := q / ((q - 1) * (q + 1) * (q ^ 4 - q ^ 2 + 1) ^ 2)

section

variable (q : R) (hq : q ≠ 0) (hm : q - 1 ≠ 0) (hp : q + 1 ≠ 0)
  (h4 : q ^ 4 + 1 ≠ 0) (h6 : q ^ 4 - q ^ 2 + 1 ≠ 0)
include hq hm hp h4 h6

omit h4 in
theorem lam_ne_zero : lam q ≠ 0 := by
  unfold lam
  exact div_ne_zero hq (mul_ne_zero (mul_ne_zero hm hp) (pow_ne_zero _ h6))

/-- **Two-dimensional block.** `γ₁·γ₂ = λ·σ₀σ₁σ₀`. -/
theorem electron_two_photon_block :
    photonMat q (a₁ q) (b₁ q) (c₁ q) * photonMat q (a₂ q) (b₂ q) (c₂ q) =
      lam q • electronMat q := by
  rw [photonMat_eq q _ _ _ hq, photonMat_eq q _ _ _ hq, electronMat_eq q hq,
    Matrix.mul_fin_two, Matrix.smul_of]
  simp only [a₁, b₁, c₁, a₂, b₂, c₂, lam, den]
  generalize hs : q - 1 = s at *
  generalize ht : q + 1 = t at *
  generalize hv : q ^ 4 + 1 = v at *
  generalize hu : q ^ 4 - q ^ 2 + 1 = u at *
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp only [Fin.zero_eta, Fin.mk_one, Fin.isValue, Matrix.of_apply, Matrix.cons_val',
      Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.empty_val', Matrix.cons_val_fin_one,
      Pi.smul_apply, smul_eq_mul] <;>
    (field_simp; subst hs ht hv hu; ring)

omit hq in
/-- **Trivial character.** `triv(γ₁)·triv(γ₂) = λ·q³`. -/
theorem electron_two_photon_triv :
    trivPhoton q (a₁ q) (b₁ q) (c₁ q) * trivPhoton q (a₂ q) (b₂ q) (c₂ q) =
      lam q * q ^ 3 := by
  simp only [trivPhoton, a₁, b₁, c₁, a₂, b₂, c₂, lam, den]
  generalize hs : q - 1 = s at *
  generalize ht : q + 1 = t at *
  generalize hv : q ^ 4 + 1 = v at *
  generalize hu : q ^ 4 - q ^ 2 + 1 = u at *
  field_simp
  subst hs ht hv hu
  ring

/-- **Sign character: the defect.** `sign(γ₁)·sign(γ₂) + λ/q³` is the explicit nonzero
rational function below, so this family does not lift to `H₃(q)`. -/
theorem electron_two_photon_sign_defect :
    signPhoton q (a₁ q) (b₁ q) (c₁ q) * signPhoton q (a₂ q) (b₂ q) (c₂ q) + lam q / q ^ 3 =
      (q ^ 2 + 1) * (q ^ 2 - q + 1) * (q ^ 2 + q + 1) /
        (q ^ 2 * (q - 1) * (q + 1) * (q ^ 4 + 1)) := by
  simp only [signPhoton, a₁, b₁, c₁, a₂, b₂, c₂, lam, den]
  generalize hs : q - 1 = s at *
  generalize ht : q + 1 = t at *
  generalize hv : q ^ 4 + 1 = v at *
  generalize hu : q ^ 4 - q ^ 2 + 1 = u at *
  field_simp
  subst hs ht hv hu
  ring

end

end QOU.MassTheory.ElectronTwoPhotonTL
