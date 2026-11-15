import Mathlib.Tactic
import QOU.StandardModel.ChiralityPolarizationHopf

/-!
# Real structures on the polarization line, and λ-covariance of the dictionary

Bean `qou-qs2u`, owner E2 and D2.3 (2026-11-15). Fixing the free phase `λ` in the
dictionary `(φ₀, φ₁) ↦ [φ₁ : λ φ₀]` (`ChiralityPolarizationHopf.lean`) needs an
antilinear involution on the polarization line `𝒮_p ≅ ℙ¹(ℂ)`: its fixed circle would be
the "real", that is linear, polarizations. This file records what the model cone itself
supplies. Here antilinear means relative to the right `ℂ`-structure `p ↦ p i`, the Reeb
fibre.

## Proved here (generic `[CommRing R]`)

1. **The Reeb triad's `j` is a quaternionic structure, not a real structure.** Right
   multiplication by `j` is antilinear (`rightJ_antilinear`) and squares to `−1`
   (`rightJ_sq`). On points of `S²` it is the antipodal map (`hopf_rightJ`), which has no
   fixed point (`hopf_rightJ_no_fixed`). So it singles out no circle of real
   polarizations.
2. **The cone carries a whole circle of real structures.** For every unit
   `u = c j + d k`, conjugation `p ↦ u p ū` is antilinear (`realStr_antilinear`) and an
   involution (`realStr_involutive`). Its fixed set for `u = j` is `span(1, j)`
   (`realStr_unitJ`), which is the `λ = 1` real circle. For `u = k` it is `span(1, k)`
   (`realStr_unitK`), which is the `λ = i` circle. The structure itself does not choose
   between them.
3. **The dictionaries for different `λ` are related by the SU(2) action**
   (`dict_rotate`, `hopf_dict_rotate`). For a unit complex `e`, replacing `v₂` by
   `ē² v₂` is left multiplication by `e` up to the Reeb phase. On `S²` it is conjugation
   by `e`, a rotation about the `i`-axis, which fixes the `σ₀`/`σ₁` chart centres `∓i`.
   So **WLOG `λ = 1`, covariantly**: every statement proved for `λ = 1` holds for every
   `λ ∈ U(1)` after this rotation, and it acts on chirality gradings by the same
   conjugation (`leftMul_conj_chiralGammaU`).

## λ-independent conclusions (they stand without a choice)

The chirality, orthogonal-pair and transitivity theorems (`hopf_eigen_line`,
`hopf_eq_ray`, `orth_pair_chirality`, `orth_pair_eq_leftMul_std`), the Hecke obstruction
(`no_automorphism_to_orthogonal_pair`) and the QED probe use no dictionary at all. The
axis images `hopf_pol_v1_axis` and `hopf_pol_v2_axis` hold for every `λ`. Only "which
real `φ` are linear" depends on `λ` (`polDict_one_linear` vs `polDict_i_circular`).
`|λ|` is not in `U(1)`: rescaling `v₂` by a positive real is not unitary, so it does not
preserve Hermitian orthogonality; requiring the dictionary to be an isometry fixes `|λ|`.

No `sorry`, no axiom, no `native_decide`, no class.
-/

namespace QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-! ## 1. `j` from the Reeb triad: a quaternionic structure -/

/-- Right multiplication by `j`. -/
def rightJ (p : BringCone R) : BringCone R := p * unitJ

/-- **`R_j` is antilinear** for the Reeb complex structure: `R_j (p i) = −(R_j p) i`. -/
theorem rightJ_antilinear (p : BringCone R) :
    rightJ (p * unitI) = -(rightJ p * unitI) := by
  ext <;> simp [rightJ, unitI, unitJ]

/-- **`R_j² = −1`**: a quaternionic structure, not a real one. -/
theorem rightJ_sq (p : BringCone R) : rightJ (rightJ p) = -p := by
  ext <;> simp [rightJ, unitJ]

/-- **On `S²`, `R_j` is the antipodal map.** -/
theorem hopf_rightJ (p : BringCone R) : hopf (rightJ p) = -hopf p := by
  ext <;> simp [hopf, rightJ, unitI, unitJ] <;> ring

/-- **The antipodal map fixes no point** of the sphere, when `2` is cancellable. -/
theorem hopf_rightJ_no_fixed (h2 : ∀ x : R, 2 * x = 0 → x = 0) {p : BringCone R}
    (hfix : hopf (rightJ p) = hopf p) : hopf p = 0 := by
  rw [hopf_rightJ] at hfix
  have hz : ∀ f : BringCone R → R, f (hopf p) = -f (hopf p) → f (hopf p) = 0 :=
    fun f hf => h2 _ (by linear_combination hf)
  ext
  · exact hz (fun x => x.re) (by simpa using congrArg (fun x : BringCone R => x.re) hfix.symm)
  · exact hz (fun x => x.imI) (by simpa using congrArg (fun x : BringCone R => x.imI) hfix.symm)
  · exact hz (fun x => x.imJ) (by simpa using congrArg (fun x : BringCone R => x.imJ) hfix.symm)
  · exact hz (fun x => x.imK) (by simpa using congrArg (fun x : BringCone R => x.imK) hfix.symm)

/-! ## 2. A circle of real structures -/

/-- Conjugation by `u`: `p ↦ u p ū`. -/
def realStr (u p : BringCone R) : BringCone R := u * p * star u

/-- **Antilinear** for every `u = c j + d k`. -/
theorem realStr_antilinear (c d : R) (p : BringCone R) :
    realStr (orthW c d) (p * unitI) = -(realStr (orthW c d) p * unitI) := by
  ext <;> simp [realStr, orthW, unitI] <;> ring

theorem orthW_mul_self {c d : R} (h : c * c + d * d = 1) :
    orthW c d * orthW c d = -1 := by
  ext <;> simp [orthW] <;> first | ring1 | linear_combination -h

theorem star_orthW_mul_self {c d : R} (h : c * c + d * d = 1) :
    star (orthW c d) * star (orthW c d) = -1 := by
  ext <;> simp [orthW] <;> first | ring1 | linear_combination -h

/-- **An involution** for every unit `u = c j + d k`. -/
theorem realStr_involutive {c d : R} (h : c * c + d * d = 1) (p : BringCone R) :
    realStr (orthW c d) (realStr (orthW c d) p) = p := by
  have e : realStr (orthW c d) (realStr (orthW c d) p)
      = (orthW c d * orthW c d) * p * (star (orthW c d) * star (orthW c d)) := by
    simp only [realStr, mul_assoc]
  rw [e, orthW_mul_self h, star_orthW_mul_self h]
  simp

/-- `u = j` negates the `i` and `k` parts: its fixed set is `span(1, j)`, the `λ = 1`
real polarizations `pol a 0 c 0`. -/
theorem realStr_unitJ (p : BringCone R) :
    realStr (orthW 1 0) p = ⟨p.re, -p.imI, p.imJ, -p.imK⟩ := by
  ext <;> simp [realStr, orthW]

/-- `u = k` negates the `i` and `j` parts: its fixed set is `span(1, k)`, the `λ = i`
circle (`pol a 0 0 d = a − d k`). -/
theorem realStr_unitK (p : BringCone R) :
    realStr (orthW 0 1) p = ⟨p.re, -p.imI, -p.imJ, p.imK⟩ := by
  ext <;> simp [realStr, orthW]

/-! ## 3. λ-covariance: the dictionaries differ by a rotation about the `i`-axis -/

/-- For a unit complex `e`, `e (v₁ + j v₂) = (v₁ + j ē² v₂) e`. -/
theorem dict_rotate {a b : R} (he : a * a + b * b = 1) (x y c d : R) :
    cplx a b * (cplx x y + unitJ * cplx c d)
      = (cplx x y + unitJ * (star (cplx a b) * star (cplx a b) * cplx c d)) * cplx a b := by
  ext <;> simp [cplx, unitJ] <;>
    first
    | ring1
    | linear_combination (-(a * c + b * d)) * he
    | linear_combination (a * d - b * c) * he

/-- **The `λ`-dictionaries differ by a rotation**: the Hopf image of `v₁ + j ē² v₂` is
the conjugate by `e` of the Hopf image of `v₁ + j v₂`. -/
theorem hopf_dict_rotate {a b : R} (he : a * a + b * b = 1) (x y c d : R) :
    hopf (cplx x y + unitJ * (star (cplx a b) * star (cplx a b) * cplx c d))
      = conjBy (cplx a b) (hopf (cplx x y + unitJ * cplx c d)) := by
  rw [← hopf_leftMul, dict_rotate he, hopf_mul_cplx, he, one_smul]

end QOU.Tetraplectic
