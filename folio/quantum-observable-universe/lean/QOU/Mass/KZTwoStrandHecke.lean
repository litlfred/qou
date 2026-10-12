import QOU.Mass.KZHolonomy.BraidRep
import QOU.Mass.BraidHeckeFactor
import Mathlib.Tactic.Module
import Mathlib.Tactic.FieldSimp

/-!
# The two-strand KZ holonomy satisfies the Hecke quadratic, exactly

Let `A` be a complete normed `ℂ`-algebra, `ρ : S₂ →* A` and `κ, c ∈ ℂ`. This file computes the
image of the Artin generator under the KZ holonomy representation
`QOU.Mass.KZHolonomy.kzBraidRep ρ κ c : BraidGroup 1 →* Aˣ` (two strands) **in closed form**,
from the definition of that representation as a transport, and proves that it satisfies the
Hecke quadratic.

* `kzForm_genPath_two` — along the half-turn `γ₀` the KZ coefficient is the constant
  `θ • (P − c)`, with `P = ρ(s₀)` and `θ = 2πiκ`. (Both ordered pairs contribute
  `(u₀−u₁)/(z₀−z₁) = e'/e = iπ`.)
* `genFund_two_one` — the transport is `T = e^{θ(1−c)} e₊ + e^{−θ(1+c)} e₋`, where
  `e± = (1 ± P)/2` are the eigenprojections of the involution `P`. This is the unique
  fundamental solution (`IsFundSol.eqOn`) of `U' = θ(P − c)U`.
* `kzBraidRep_two_σ` — hence `θ(σ₀) = P T = e^{θ(1−c)} e₊ − e^{−θ(1+c)} e₋`.
* `kzTwoStrand_isHeckeQuad` — with `q = e^{θ} = e^{2πiκ}` and the scalar `s = e^{θc}`,
  `β = s • θ(σ₀) = q e₊ − q⁻¹ e₋` satisfies `β² = (q − q⁻¹)β + 1`.
* `heckeOfKZTwoStrand` — so the two-strand KZ representation factors through `H₁(q)`
  (`QOU.Mass.BraidHeckeFactor.heckeOfBraidRepOfZero`).

**Scope.** Two strands only. For `n ≥ 3` strands the coefficient along the half-turn `γ_j`
is not constant — the pairs with one moving and one fixed point contribute — and the
quadratic relation for `θ(σ_j)` needs the local-monodromy (regular singularity) analysis at the
collision divisor `z_j = z_{j+1}`. That step is not done here; see
`QOU.Mass.KohnoComparison` for the precise statement of what remains open. By
`QOU.Mass.BraidHeckeFactor.isHeckeQuad_all_of_zero` it would suffice to do it for one
generator.

For the real pin, the coupling is purely imaginary, so `q = e^{2πiκ}` is a positive real;
no numerical value is used here.
-/

namespace QOU.Mass.KZTwoStrandHecke

open Set Complex QOU.Mass.KZHolonomy QOU.MathlibExt.Braid QOU.Mass.BraidHeckeFactor

variable {A : Type*} [NormedRing A] [NormedAlgebra ℂ A]

/-! ## The eigenprojections of an involution -/

section Involution

/-- `e₊ = (1 + P)/2`. -/
noncomputable def eP (P : A) : A := (1 / 2 : ℂ) • (1 + P)

/-- `e₋ = (1 − P)/2`. -/
noncomputable def eM (P : A) : A := (1 / 2 : ℂ) • (1 - P)

variable {P : A}

lemma P_mul_eP (hP : P * P = 1) : P * eP P = eP P := by
  unfold eP
  rw [mul_smul_comm, mul_add, mul_one, hP, add_comm]

lemma P_mul_eM (hP : P * P = 1) : P * eM P = -eM P := by
  unfold eM
  rw [mul_smul_comm, mul_sub, mul_one, hP, ← smul_neg, neg_sub]

lemma eP_add_eM : eP P + eM P = 1 := by
  unfold eP eM
  module

lemma eP_mul_eP (hP : P * P = 1) : eP P * eP P = eP P := by
  unfold eP
  rw [smul_mul_smul_comm, add_mul, mul_add, mul_add, one_mul, mul_one, one_mul, hP]
  module

lemma eM_mul_eM (hP : P * P = 1) : eM P * eM P = eM P := by
  unfold eM
  rw [smul_mul_smul_comm, sub_mul, mul_sub, mul_sub, one_mul, mul_one, one_mul, hP]
  module

lemma eP_mul_eM (hP : P * P = 1) : eP P * eM P = 0 := by
  unfold eP eM
  rw [smul_mul_smul_comm, add_mul, mul_sub, mul_sub, one_mul, mul_one, one_mul, hP]
  module

lemma eM_mul_eP (hP : P * P = 1) : eM P * eP P = 0 := by
  unfold eP eM
  rw [smul_mul_smul_comm, sub_mul, mul_add, mul_add, one_mul, mul_one, one_mul, hP]
  module

/-- **The Hecke quadratic on the split involution.** `β = q e₊ − q⁻¹ e₋` satisfies
`β² = (q − q⁻¹)β + q q⁻¹`. -/
theorem split_hecke (hP : P * P = 1) {q : ℂ} (hq : q ≠ 0) :
    (q • eP P - q⁻¹ • eM P) * (q • eP P - q⁻¹ • eM P) =
      (q - q⁻¹) • (q • eP P - q⁻¹ • eM P) + (q * q⁻¹) • (1 : A) := by
  rw [← eP_add_eM (P := P)]
  simp only [sub_mul, mul_sub, smul_mul_smul_comm, eP_mul_eP hP, eM_mul_eM hP, eP_mul_eM hP,
    eM_mul_eP hP, smul_zero, sub_zero, zero_sub, sub_neg_eq_add]
  rw [mul_inv_cancel₀ hq]
  match_scalars <;> field_simp <;> ring

/-- The KZ residue `θ (P − c)` acts on `e₊` by `θ(1 − c)`. -/
lemma resid_mul_eP (hP : P * P = 1) (θ c : ℂ) :
    (θ • (P - algebraMap ℂ A c)) * eP P = (θ * (1 - c)) • eP P := by
  rw [smul_mul_assoc, sub_mul, P_mul_eP hP, Algebra.algebraMap_eq_smul_one, smul_mul_assoc,
    one_mul]
  module

/-- The KZ residue `θ (P − c)` acts on `e₋` by `−θ(1 + c)`. -/
lemma resid_mul_eM (hP : P * P = 1) (θ c : ℂ) :
    (θ • (P - algebraMap ℂ A c)) * eM P = (-(θ * (1 + c))) • eM P := by
  rw [smul_mul_assoc, sub_mul, P_mul_eM hP, Algebra.algebraMap_eq_smul_one, smul_mul_assoc,
    one_mul]
  module

end Involution

/-! ## The explicit fundamental solution -/

section Solution

variable (P : A) (θ c : ℂ)

/-- `U(t) = e^{tθ(1−c)} e₊ + e^{−tθ(1+c)} e₋`. -/
noncomputable def Usol (t : ℝ) : A :=
  Complex.exp (t * (θ * (1 - c))) • eP P + Complex.exp (t * (-(θ * (1 + c)))) • eM P

lemma hasDerivAt_cexp_mul (a : ℂ) (t : ℝ) :
    HasDerivAt (fun s : ℝ => Complex.exp (s * a)) (a * Complex.exp (t * a)) t := by
  have h := ((hasDerivAt_id' t).ofReal_comp.mul_const a).cexp
  convert h using 1
  simp only [ofReal_one, one_mul]
  ring

variable {P}

theorem usol_isFundSol (hP : P * P = 1) :
    IsFundSol (fun _ : ℝ => θ • (P - algebraMap ℂ A c)) (Usol P θ c) := by
  refine ⟨?_, fun t _ => ?_⟩
  · simp only [Usol, ofReal_zero, zero_mul, Complex.exp_zero, one_smul]
    exact eP_add_eM
  · refine HasDerivAt.hasDerivWithinAt ?_
    have h := ((hasDerivAt_cexp_mul (θ * (1 - c)) t).smul_const (eP P)).add
      ((hasDerivAt_cexp_mul (-(θ * (1 + c))) t).smul_const (eM P))
    convert h using 1
    simp only [Usol, mul_add, mul_smul_comm, resid_mul_eP hP, resid_mul_eM hP, smul_smul]
    congr 1 <;> rw [mul_comm]

end Solution

/-! ## The two-strand KZ computation -/

section KZ

lemma eArc'_eq (t : ℝ) : eArc' t = (Real.pi * I) * eArc t := by
  apply Complex.ext <;> simp [eArc, eArc'] <;> ring

lemma eArc_ne_zero (t : ℝ) : eArc t ≠ 0 := by
  intro h
  have h1 := congrArg Complex.re h
  have h2 := congrArg Complex.im h
  rw [eArc_re] at h1
  rw [eArc_im] at h2
  simp only [zero_re, zero_im] at h1 h2
  have := Real.sin_sq_add_cos_sq (Real.pi * t)
  rw [h1, h2] at this
  norm_num at this

lemma dlog_two (t : ℝ) :
    (-(eArc' t / 2) - eArc' t / 2) / (((0 : ℕ) : ℂ) + 1 / 2 - eArc t / 2 -
      (((0 : ℕ) : ℂ) + 1 / 2 + eArc t / 2)) = Real.pi * I := by
  have he := eArc_ne_zero t
  rw [eArc'_eq]
  have h1 : -((Real.pi * I) * eArc t / 2) - (Real.pi * I) * eArc t / 2 =
      (Real.pi * I) * (-eArc t) := by ring
  have h2 : ((0 : ℕ) : ℂ) + 1 / 2 - eArc t / 2 - (((0 : ℕ) : ℂ) + 1 / 2 + eArc t / 2) =
      -eArc t := by ring
  rw [h1, h2, mul_div_assoc, div_self (neg_ne_zero.2 he), mul_one]

variable (ρ : Equiv.Perm (Fin 2) →* A) (κ c : ℂ)

/-- **The two-strand KZ coefficient is constant** along the half-turn:
`ω(γ₀(t))(γ₀'(t)) = θ (ρ(s₀) − c)` with `θ = 2πiκ`. -/
theorem kzForm_genPath_two (t : ℝ) :
    kzForm ρ κ c (genPath (0 : Fin 1) t) (genPath' (0 : Fin 1) t) =
      (2 * κ * (Real.pi * I)) • (ρ (adjSwap (0 : Fin 1)) - algebraMap ℂ A c) := by
  rw [kzForm_apply]
  have hs : Equiv.swap (1 : Fin 2) 0 = Equiv.swap 0 1 := Equiv.swap_comm _ _
  have hadj : adjSwap (0 : Fin 1) = Equiv.swap (0 : Fin 2) 1 := rfl
  have hd01 : dlogPair (genPath (0 : Fin 1) t) (genPath' (0 : Fin 1) t) 0 1 = Real.pi * I := by
    simp only [dlogPair, genPath, genPath']
    simpa using dlog_two t
  have hd10 : dlogPair (genPath (0 : Fin 1) t) (genPath' (0 : Fin 1) t) 1 0 = Real.pi * I := by
    rw [dlogPair_comm, hd01]
  simp only [kzOp, Fin.sum_univ_two, dlogPair_self, zero_smul, zero_add, add_zero, hd01, hd10,
    hs, hadj]
  module

variable [CompleteSpace A]

omit [NormedAlgebra ℂ A] [CompleteSpace A] in
lemma rho_adjSwap_sq : ρ (adjSwap (0 : Fin 1)) * ρ (adjSwap (0 : Fin 1)) = 1 := by
  rw [← map_mul, adjSwap, Equiv.swap_mul_self, map_one]

/-- **The two-strand KZ transport in closed form** (at time `1`). -/
theorem genFund_two_one :
    genFund ρ κ c (0 : Fin 1) 1 = Usol (ρ (adjSwap (0 : Fin 1))) (2 * κ * (Real.pi * I)) c 1 := by
  have hspec := genFund_spec ρ κ c (0 : Fin 1)
  unfold IsTransport at hspec
  have hfun : (fun t => kzForm ρ κ c (genPath (0 : Fin 1) t) (genPath' (0 : Fin 1) t)) =
      fun _ => (2 * κ * (Real.pi * I)) • (ρ (adjSwap (0 : Fin 1)) - algebraMap ℂ A c) :=
    funext (kzForm_genPath_two ρ κ c)
  rw [hfun] at hspec
  exact hspec.eqOn continuousOn_const (usol_isFundSol _ _ (rho_adjSwap_sq ρ))
    ⟨zero_le_one, le_rfl⟩

/-- **The image of the Artin generator in closed form.** With `P = ρ(s₀)`, `θ = 2πiκ`:
`θ(σ₀) = e^{θ(1−c)} e₊ − e^{−θ(1+c)} e₋`. -/
theorem kzBraidRep_two_σ :
    ((kzBraidRep ρ κ c (σ (0 : Fin 1)) : Aˣ) : A) =
      Complex.exp (2 * κ * (Real.pi * I) * (1 - c)) • eP (ρ (adjSwap (0 : Fin 1))) -
        Complex.exp (-(2 * κ * (Real.pi * I) * (1 + c))) • eM (ρ (adjSwap (0 : Fin 1))) := by
  have hP := rho_adjSwap_sq ρ
  rw [kzBraidRep_σ, genFund_two_one, Usol, mul_add, mul_smul_comm, mul_smul_comm, P_mul_eP hP,
    P_mul_eM hP, smul_neg, ← sub_eq_add_neg]
  simp only [ofReal_one, one_mul]

/-- **The two-strand KZ generator satisfies the Hecke quadratic.** With `θ = 2πiκ`,
`q = e^{θ}` and `s = e^{θc}`, the rescaled generator `β = s • θ(σ₀)` satisfies
`β² = (q − q⁻¹)β + q q⁻¹`. -/
theorem kzTwoStrand_isHeckeQuad :
    IsHeckeQuad (Complex.exp (2 * κ * (Real.pi * I) * c))
      (Complex.exp (2 * κ * (Real.pi * I))) (Complex.exp (2 * κ * (Real.pi * I)))⁻¹
      ((kzBraidRep ρ κ c (σ (0 : Fin 1)) : Aˣ) : A) := by
  set θ := 2 * κ * (Real.pi * I)
  have hP := rho_adjSwap_sq ρ
  have hβ : Complex.exp (θ * c) • ((kzBraidRep ρ κ c (σ (0 : Fin 1)) : Aˣ) : A) =
      Complex.exp θ • eP (ρ (adjSwap (0 : Fin 1))) -
        (Complex.exp θ)⁻¹ • eM (ρ (adjSwap (0 : Fin 1))) := by
    rw [kzBraidRep_two_σ, smul_sub, smul_smul, smul_smul, ← Complex.exp_add, ← Complex.exp_add,
      ← Complex.exp_neg]
    congr 3 <;> ring
  unfold IsHeckeQuad
  rw [hβ]
  exact split_hecke hP (Complex.exp_ne_zero θ)

/-- **The two-strand KZ representation factors through `H₁(q)`**, `q = e^{2πiκ}`:
`σ₀ ↦ e^{2πiκc} • θ(σ₀)`. -/
noncomputable def heckeOfKZTwoStrand :
    QOU.SchurWeyl.Hecke ℂ (Complex.exp (2 * κ * (Real.pi * I)))
      (Complex.exp (2 * κ * (Real.pi * I)))⁻¹ 1 →ₐ[ℂ] A :=
  heckeOfBraidRepOfZero (s := Complex.exp (2 * κ * (Real.pi * I) * c)) (kzBraidRep ρ κ c)
    (fun _ => kzTwoStrand_isHeckeQuad ρ κ c)

end KZ

end QOU.Mass.KZTwoStrandHecke
