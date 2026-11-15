import Mathlib.Tactic
import QOU.BringConeIcosahedral
import QOU.Interactions.confinementUniversality

/-!
# The chirality unit `u` as a point of the polarization line ℙ¹(ℂ)

Bean `qou-qs2u` (epic `qou-qs0e`). `QOU/BringCone.lean` proved that the chirality
grading `Γ_u = L_u ∘ M_i` on the model cone `BringCone R = Quaternion R` needs a pure
unit `u` (a point of `S²`), and that nothing in the cone fixes it
(`QOU/BringConeIcosahedral.lean`, `QOU/BringConeGauge.lean`). This file asks whether
that `S²` is the photon polarization line `ℙ¹(ℂ) ∋ [v₁ : v₂]` of
`mass-theory/breit-wheeler-vertex.md`.

## The identification used

`mass-theory/reeb-bundle.md` states the exceptional divisor
`𝒮_p ≅ ℙ¹(ℂ)` is the base of the Hopf fibration `S³ → S²` whose `U(1)` fibre is the
Reeb flow. On the model cone the Reeb fibre is right multiplication by complex scalars
`a + b i` (`M_i` is right multiplication by `i`), so a polarization state is a right
`ℂ`-line `p · ℂ`, and the Hopf map is `p ↦ p i p̄`. That `𝒮_p` of the vertex and the
Hopf base of this cone are the same `S²` is the reading of `reeb-bundle.md`; it is an
identification of two descriptions, not a theorem proved here.

## Proved here (generic `[CommRing R]`, §7c)

1. **Well defined on rays** (`hopf_mul_cplx`): `hopf (p λ) = |λ|² · hopf p` for complex
   `λ`. The Reeb phase does not move the point.
2. **Equivariant** (`hopf_leftMul`): `hopf (g p) = g · hopf p · ḡ`, the same conjugation
   by which a triad-commuting symmetry acts on `u` (`leftMul_conj_chiralGammaU`).
3. **The left-handed eigenspace of `Γ_u` is exactly one polarization line**: for a
   unit `p`, the whole complex line `p · ℂ` is `Γ_{hopf p} = −1` (`hopf_eigen_line`),
   and two unit vectors with the same Hopf image differ by a complex scalar
   (`hopf_eq_ray`). Together with `chiralGammaU_eigen_iff`, a choice of `u` is the same
   as a choice of which polarization line is called left-handed.
4. **An orthogonal photon pair fixes the grading up to the global flip**
   (`hopf_orth`, `orth_pair_chirality`): if `p₂` is Hermitian-orthogonal to `p₁`
   (the `ℂ`-part of `p̄₁ p₂` vanishes), then `hopf p₂ = −hopf p₁`; for the grading
   `Γ_{hopf p₁}`, `p₁` is left-handed and `p₂` right-handed, and swapping the photons is
   `Γ ↦ −Γ` (`chiralGammaU_neg`).
5. **Real polarizations are a great circle** (`hopf_real_imJ`): a line with real
   coordinates `[v₁ : v₂]` has Hopf image orthogonal to `j`. Circular lines
   `[1 : ±i]` map to `∓2j` (`hopf_circular_plus`, `hopf_circular_minus`).

## What is NOT proved

* That the Breit–Wheeler "perpendicular" condition (`σ₀` vs `σ₁`, distinct coordinate
  patches) is Hermitian orthogonality. Item 4 is conditional on that reading.
* Any map from the Hecke photon coefficients `(φ₀, φ₁, φ₀₁)` of
  `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁` to a cone vector `p`. The corpus has none, so "u is
  inherited through γγ" is stated here on the cone side only.

No `sorry`, no axiom, no `native_decide`, no class.
-/

namespace QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-- The Hopf map on the model cone: `p ↦ p i p̄`. -/
def hopf (p : BringCone R) : BringCone R := p * unitI * star p

/-- A complex scalar `a + b i`, the Reeb fibre direction. -/
def cplx (a b : R) : BringCone R := ⟨a, b, 0, 0⟩

theorem cplx_mul_unitI_comm (a b : R) : cplx a b * unitI = unitI * cplx a b := by
  ext <;> simp [cplx, unitI]

/-- `hopf (p w) = p (w i w̄) p̄`. -/
theorem hopf_mul (p w : BringCone R) :
    hopf (p * w) = p * (w * unitI * star w) * star p := by
  simp only [hopf, star_mul, mul_assoc]

/-- `λ i λ̄ = |λ|² i` for complex `λ`. -/
theorem cplx_conj_unitI (a b : R) :
    cplx a b * unitI * star (cplx a b) = (a * a + b * b) • unitI := by
  ext <;> simp [cplx, unitI] <;> ring

/-- **The Hopf image is constant on Reeb fibres**: `hopf (p λ) = |λ|² · hopf p`. -/
theorem hopf_mul_cplx (p : BringCone R) (a b : R) :
    hopf (p * cplx a b) = (a * a + b * b) • hopf p := by
  rw [hopf_mul, cplx_conj_unitI, mul_smul_comm, smul_mul_assoc]
  rfl

/-- **Equivariance**: a left multiplication moves the Hopf image by conjugation. -/
theorem hopf_leftMul (g p : BringCone R) : hopf (g * p) = conjBy g (hopf p) := by
  simp only [hopf, conjBy, star_mul, mul_assoc]

theorem star_mul_self_of_normSq {p : BringCone R} (hp : Quaternion.normSq p = 1) :
    star p * p = 1 := by
  rw [Quaternion.star_mul_self, hp]; rfl

theorem mul_star_self_of_normSq {p : BringCone R} (hp : Quaternion.normSq p = 1) :
    p * star p = 1 := by
  rw [Quaternion.self_mul_star, hp]; rfl

/-- **The whole complex line through a unit `p` is left-handed for `Γ_{hopf p}`.** -/
theorem hopf_eigen_line {p : BringCone R} (hp : Quaternion.normSq p = 1) (a b : R) :
    chiralGammaU (hopf p) (p * cplx a b) = -(p * cplx a b) := by
  have hsp := star_mul_self_of_normSq hp
  have hpi : ∀ x : BringCone R, star p * (p * x) = x := by
    intro x; rw [← mul_assoc, hsp, one_mul]
  simp only [chiralGammaU, leftMul, reebM_i_eq_mul_unitI, hopf, mul_assoc, hpi]
  rw [← mul_assoc unitI (cplx a b), ← cplx_mul_unitI_comm, mul_assoc,
    unitI_mul_unitI]
  simp

/-- **Two unit vectors with the same Hopf image span the same complex line**:
`w = p̄ p'` is complex (`imJ = imK = 0`) and `p' = p w`, when `2` is cancellable. -/
theorem hopf_eq_ray (h2 : ∀ x : R, 2 * x = 0 → x = 0) {p p' : BringCone R}
    (hp : Quaternion.normSq p = 1) (hp' : Quaternion.normSq p' = 1)
    (h : hopf p = hopf p') :
    (star p * p').imJ = 0 ∧ (star p * p').imK = 0 ∧ p' = p * (star p * p') := by
  have hsp := star_mul_self_of_normSq hp
  have hsp' := star_mul_self_of_normSq hp'
  have hps := mul_star_self_of_normSq hp
  -- `i w = w i` with `w = p̄ p'`
  have hcomm : unitI * (star p * p') = (star p * p') * unitI := by
    have e1 : star p * hopf p * p' = unitI * (star p * p') := by
      simp only [hopf]
      calc star p * (p * unitI * star p) * p' = (star p * p) * unitI * (star p * p') := by
            simp only [mul_assoc]
        _ = unitI * (star p * p') := by rw [hsp, one_mul]
    have e2 : star p * hopf p' * p' = (star p * p') * unitI := by
      simp only [hopf]
      calc star p * (p' * unitI * star p') * p' = (star p * p') * unitI * (star p' * p') := by
            simp only [mul_assoc]
        _ = (star p * p') * unitI := by rw [hsp', mul_one]
    rw [← e1, ← e2, h]
  set w := star p * p' with hw
  have hJ := congrArg (fun x : BringCone R => x.imJ) hcomm
  have hK := congrArg (fun x : BringCone R => x.imK) hcomm
  simp [unitI] at hJ hK
  refine ⟨h2 _ ?_, h2 _ ?_, ?_⟩
  · linear_combination -hJ
  · linear_combination hK
  · rw [hw, ← mul_assoc, hps, one_mul]

/-- For `w = c j + d k`, `w i w̄ = −(c² + d²) i`. -/
theorem orth_conj_unitI (c d : R) :
    (⟨0, 0, c, d⟩ : BringCone R) * unitI * star (⟨0, 0, c, d⟩ : BringCone R)
      = -((c * c + d * d) • unitI) := by
  ext <;> simp [unitI] <;> ring

/-- **A Hermitian-orthogonal partner has the antipodal Hopf image**: if the `ℂ`-part of
`p̄₁ p₂` vanishes and `p₁` is a unit, `hopf p₂ = −|p₂|² hopf p₁`. -/
theorem hopf_orth {p₁ p₂ : BringCone R} (hp₁ : Quaternion.normSq p₁ = 1)
    (hre : (star p₁ * p₂).re = 0) (hi : (star p₁ * p₂).imI = 0) :
    hopf p₂ = -(((star p₁ * p₂).imJ * (star p₁ * p₂).imJ
      + (star p₁ * p₂).imK * (star p₁ * p₂).imK) • hopf p₁) := by
  have hps := mul_star_self_of_normSq hp₁
  have hw : star p₁ * p₂ = ⟨0, 0, (star p₁ * p₂).imJ, (star p₁ * p₂).imK⟩ := by
    ext <;> simp [hre, hi]
  have hp2 : p₂ = p₁ * (star p₁ * p₂) := by rw [← mul_assoc, hps, one_mul]
  conv_lhs => rw [hp2, hopf_mul, hw, orth_conj_unitI]
  rw [mul_neg, neg_mul, mul_smul_comm, smul_mul_assoc]
  rfl

/-- **An orthogonal pair of unit photons, read through `Γ_{hopf p₁}`**: `p₁` is
left-handed and `p₂` right-handed. -/
theorem orth_pair_chirality {p₁ p₂ : BringCone R} (hp₁ : Quaternion.normSq p₁ = 1)
    (hp₂ : Quaternion.normSq p₂ = 1)
    (hre : (star p₁ * p₂).re = 0) (hi : (star p₁ * p₂).imI = 0) :
    chiralGammaU (hopf p₁) p₁ = -p₁ ∧ chiralGammaU (hopf p₁) p₂ = p₂ := by
  refine ⟨(chiralGammaU_eigen_iff hp₁ _).mpr rfl, ?_⟩
  have hn : (star p₁ * p₂).imJ * (star p₁ * p₂).imJ
      + (star p₁ * p₂).imK * (star p₁ * p₂).imK = 1 := by
    have h1 : Quaternion.normSq (star p₁ * p₂) = 1 := by
      rw [map_mul, Quaternion.normSq_star, hp₁, hp₂, one_mul]
    rw [Quaternion.normSq_def', hre, hi] at h1
    linear_combination h1
  have ho := hopf_orth hp₁ hre hi
  rw [hn, one_smul] at ho
  have h1 : hopf p₁ = -hopf p₂ := by rw [ho, neg_neg]
  rw [h1, chiralGammaU_neg, (chiralGammaU_eigen_iff hp₂ _).mpr rfl, neg_neg]

/-- **Swapping the two photons is the global flip** `Γ ↦ −Γ`. -/
theorem orth_pair_swap_is_flip {p₁ p₂ : BringCone R} (hp₁ : Quaternion.normSq p₁ = 1)
    (hp₂ : Quaternion.normSq p₂ = 1)
    (hre : (star p₁ * p₂).re = 0) (hi : (star p₁ * p₂).imI = 0) (x : BringCone R) :
    chiralGammaU (hopf p₂) x = -chiralGammaU (hopf p₁) x := by
  have hn : (star p₁ * p₂).imJ * (star p₁ * p₂).imJ
      + (star p₁ * p₂).imK * (star p₁ * p₂).imK = 1 := by
    have h1 : Quaternion.normSq (star p₁ * p₂) = 1 := by
      rw [map_mul, Quaternion.normSq_star, hp₁, hp₂, one_mul]
    rw [Quaternion.normSq_def', hre, hi] at h1
    linear_combination h1
  have ho := hopf_orth hp₁ hre hi
  rw [hn, one_smul] at ho
  rw [ho, chiralGammaU_neg]

/-! ## Linear and circular polarizations

A polarization line `[v₁ : v₂]` with `v₁ = a + b i`, `v₂ = c + d i` is the right
`ℂ`-line of `pol a b c d := v₁ + j v₂`. -/

/-- The cone vector of the polarization line `[a + b i : c + d i]`. -/
def pol (a b c d : R) : BringCone R := cplx a b + unitJ * cplx c d

/-- **Real (linear) polarizations have Hopf image orthogonal to `j`**: they fill the
`i`–`k` great circle. -/
theorem hopf_real_imJ (a c : R) : (hopf (pol a 0 c 0)).imJ = 0 := by
  simp [hopf, pol, cplx, unitJ, unitI]; ring

/-- The Hopf image is always pure. -/
theorem hopf_re (p : BringCone R) : (hopf p).re = 0 := re_hopf p

/-- Circular polarization `[1 : i]` goes to `−2 j`. -/
theorem hopf_circular_plus : hopf (pol (1 : R) 0 0 1) = ⟨0, 0, -2, 0⟩ := by
  ext <;> simp [hopf, pol, cplx, unitJ, unitI] <;> ring

/-- Circular polarization `[1 : −i]` goes to `+2 j`. -/
theorem hopf_circular_minus : hopf (pol (1 : R) 0 0 (-1)) = ⟨0, 0, 2, 0⟩ := by
  ext <;> simp [hopf, pol, cplx, unitJ, unitI] <;> ring

end QOU.Tetraplectic

/-! ## Confinement universality makes an inherited `u` invisible at nucleon level

`prop:confinement-universality` is conditional on `ConfinementUniversalityConjecture`,
which says the nucleon NF `N_F φ₀ φ₁ φ₀₁` takes one value for every real photon
coefficient. If the chirality unit is a function `U` of those coefficients, no read-out
`g` of the nucleon NF can return it unless `U` is constant. This is a one-line corollary
of the class field `h_N_F`; it is recorded because it settles the direction of the
tension: an inherited `u` is hidden by confinement, not contradicted by it. The class
quantifies over **real** coefficients only, so under the reading `φ ↦ [v₁ : v₂]` it
speaks only about the linear-polarization circle (`hopf_real_imJ`), not about circular
states. -/

namespace QOU.StandardModel.Chirality

open QOU.Interactions

/-- **Conditional on `ConfinementUniversalityConjecture`**: a photon-dependent unit
`U` that can be read off the nucleon NF is constant. -/
theorem inherited_unit_invisible_of_confinement (ctx : ConfinementUniversalityContext)
    [h : ConfinementUniversalityConjecture ctx] {X : Type*}
    (U : ℝ → ℝ → ℝ → X) (g : ℝ → X)
    (hg : ∀ a b c, g (ctx.N_F a b c) = U a b c) (a b c a' b' c' : ℝ) :
    U a b c = U a' b' c' := by
  rw [← hg, ← hg, h.h_N_F, h.h_N_F]

end QOU.StandardModel.Chirality
