import CompactQuantumMetrics.OqSU2HaarState
import Mathlib.LinearAlgebra.Basis.Basic
import Mathlib.LinearAlgebra.Finsupp.VectorSpace

/-!
# PBW basis of `O_q(SU(2))`: the ordered monomials form an `R`-basis

Bean `qou-q3dc` (q-NS Part A). `OqSU2HaarState` builds the left regular representation
`monoRep` on the free module `R^(ℤ × ℕ × ℕ)` with basis `e(a, b, c)` and remarks that the
PBW theorem is "not needed and not proved". This file proves it, over any commutative ring
`R` and any unit `q : Rˣ`, with no hypothesis on `q`.

## The ordered monomials

For `(a, b, c) ∈ ℤ × ℕ × ℕ` put

* `mono (a, b, c) = α^a β^b γ^c` when `0 ≤ a`,
* `mono (a, b, c) = δ^(-a) β^b γ^c` when `a < 0`.

## Results (sorry-free)

* `mono_span` — **spanning.** The `R`-span of the ordered monomials is all of
  `O_q(SU(2))`. Proof: the span contains `1` and is stable under left multiplication by
  each generator. The only non-monomial products are `α δ^(n+1)` and `δ α^(n+1)`, which the
  determinant relations rewrite as `δ^n + r δ^n βγ` and `α^n + r' α^n βγ`
  (`alpha_mul_delta_pow_succ`, `delta_mul_alpha_pow_succ`).
* `monoRep_mono` — `π(mono i) e(0,0,0) = e(i)`: the model representation sends the ordered
  monomial `i` to the basis vector `i`.
* `mono_linearIndependent` — **independence**, read off from `monoRep_mono`.
* `pbwBasis` — the ordered monomials are an `R`-basis of `O_q(SU(2))`
  (`pbwBasis_apply`), and `pbwEquiv : O_q(SU(2)) ≃ₗ[R] R^(ℤ × ℕ × ℕ)` is
  `x ↦ π(x) e(0,0,0)` (`pbwEquiv_apply`). So the model of `OqSU2HaarState` is faithful:
  `monoRep_faithful`.

Everything is algebraic and holds over any commutative ring; no empirical value enters.

## Consumers

`QOU/FluidDynamics/q_ns_haar_field_invariance_full.lean` uses `pbwBasis` to extend
`h ∘ X₊ = 0` and `h ∘ X₋ = 0` from the blocks of PR #9713 to the whole algebra.

References: S. L. Woronowicz (1987), Theorem 1.2 (the monomials `α^k β^m γ^n`,
`δ^k β^m γ^n` form a basis); A. Klimyk & K. Schmüdgen (1997) §4.1.5, Proposition 4.
-- Ref: [woronowicz1987]
-/

namespace QOU.AlgebraicSubstrate.OqSU2

open Finsupp

variable {R : Type*} [CommRing R]

/-! ## Skew-commutation of powers -/

section Skew

variable {A : Type*} [Ring A] [Algebra R A]

/-- `x y = r (y x)` propagates to `x yⁿ = rⁿ (yⁿ x)`. -/
theorem skew_pow_right {x y : A} {r : R} (h : x * y = r • (y * x)) (n : ℕ) :
    x * y ^ n = r ^ n • (y ^ n * x) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, mul_assoc, h, mul_smul_comm, smul_smul,
      ← mul_assoc, pow_succ]

/-- `x y = r (y x)` propagates to `xⁿ y = rⁿ (y xⁿ)`. -/
theorem skew_pow_left {x y : A} {r : R} (h : x * y = r • (y * x)) (n : ℕ) :
    x ^ n * y = r ^ n • (y * x ^ n) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ', mul_assoc, ih, mul_smul_comm, ← mul_assoc, h, smul_mul_assoc, smul_smul,
      mul_assoc, ← pow_succ', pow_succ r]

end Skew

variable (q : Rˣ)

/-! ## The relations in skew form -/

local notation "qi" => (((q⁻¹ : Rˣ) : R))

theorem beta_alpha : β q * α (R := R) q = qi • (α q * β q) := by
  rw [rel_ab, smul_smul]; simp

theorem gamma_alpha : γ q * α (R := R) q = qi • (α q * γ q) := by
  rw [rel_ag, smul_smul]; simp

theorem gamma_beta : γ q * β (R := R) q = (1 : R) • (β q * γ q) := by
  rw [one_smul, rel_bg]

/-- `βγ δ = q² δ βγ`. -/
theorem betaGamma_delta : β (R := R) q * γ q * δ q = ((q : R) * q) • (δ q * (β q * γ q)) := by
  rw [mul_assoc, rel_gd, mul_smul_comm, ← mul_assoc, rel_bd, smul_mul_assoc, smul_smul,
    mul_assoc]

/-- `βγ α = q⁻² α βγ`. -/
theorem betaGamma_alpha : β (R := R) q * γ q * α q = (qi * qi) • (α q * (β q * γ q)) := by
  rw [mul_assoc, gamma_alpha, mul_smul_comm, ← mul_assoc, beta_alpha, smul_mul_assoc, smul_smul,
    mul_assoc]

/-- `α δ^(n+1) = δ^n + r δ^n βγ` for some scalar `r`. -/
theorem alpha_mul_delta_pow_succ (n : ℕ) :
    ∃ r : R, α q * δ q ^ (n + 1) = δ q ^ n + r • (δ q ^ n * (β q * γ q)) := by
  induction n with
  | zero =>
    refine ⟨q, ?_⟩
    have h := rel_det_left (R := R) q
    rw [zero_add, pow_one, pow_zero, one_mul]
    rw [sub_eq_iff_eq_add] at h
    rw [h, add_comm]
  | succ n ih =>
    obtain ⟨r, hr⟩ := ih
    refine ⟨r * ((q : R) * q), ?_⟩
    rw [pow_succ, ← mul_assoc, hr, add_mul, smul_mul_assoc, mul_assoc, betaGamma_delta,
      mul_smul_comm, smul_smul, ← pow_succ]
    simp only [pow_succ, mul_assoc]

/-- `δ α^(n+1) = α^n + r α^n βγ` for some scalar `r`. -/
theorem delta_mul_alpha_pow_succ (n : ℕ) :
    ∃ r : R, δ q * α q ^ (n + 1) = α q ^ n + r • (α q ^ n * (β q * γ q)) := by
  induction n with
  | zero =>
    refine ⟨qi, ?_⟩
    have h := rel_det_right (R := R) q
    rw [zero_add, pow_one, pow_zero, one_mul]
    rw [sub_eq_iff_eq_add] at h
    rw [h, add_comm]
  | succ n ih =>
    obtain ⟨r, hr⟩ := ih
    refine ⟨r * (qi * qi), ?_⟩
    rw [pow_succ, ← mul_assoc, hr, add_mul, smul_mul_assoc, mul_assoc, betaGamma_alpha,
      mul_smul_comm, smul_smul, ← pow_succ]
    simp only [pow_succ, mul_assoc]

/-! ## The ordered monomials -/

/-- `β^b γ^c`. -/
noncomputable def monoY (b c : ℕ) : OqSU2 R q := β q ^ b * γ q ^ c

/-- `α^n β^b γ^c`. -/
noncomputable def monoA (n b c : ℕ) : OqSU2 R q := α q ^ n * monoY q b c

/-- `δ^n β^b γ^c`. -/
noncomputable def monoD (n b c : ℕ) : OqSU2 R q := δ q ^ n * monoY q b c

/-- The ordered monomial indexed by `(a, b, c) ∈ ℤ × ℕ × ℕ`: `α^a β^b γ^c` for `0 ≤ a`,
`δ^(-a) β^b γ^c` for `a < 0`. -/
noncomputable def mono (i : MonoIdx) : OqSU2 R q :=
  if 0 ≤ i.1 then monoA q i.1.toNat i.2.1 i.2.2 else monoD q (-i.1).toNat i.2.1 i.2.2

theorem monoA_zero (b c : ℕ) : monoA q 0 b c = monoY (R := R) q b c := by
  simp [monoA]

theorem monoD_zero (b c : ℕ) : monoD q 0 b c = monoY (R := R) q b c := by
  simp [monoD]

theorem mono_nat (n b c : ℕ) : mono q ((n : ℤ), b, c) = monoA (R := R) q n b c := by
  simp [mono]

theorem mono_neg_nat (n b c : ℕ) : mono q (-(n : ℤ), b, c) = monoD (R := R) q n b c := by
  rcases n with _ | n
  · simp [mono, monoA_zero, monoD_zero]
  · have h : ¬ (0 ≤ -((n + 1 : ℕ) : ℤ)) := by omega
    simp only [mono, if_neg h, neg_neg, Int.toNat_natCast]

theorem mono_zero : mono q (0, 0, 0) = (1 : OqSU2 R q) := by
  simp [mono, monoA, monoY]

/-- `βγ · β^b γ^c = β^(b+1) γ^(c+1)`. -/
theorem betaGamma_mul_monoY (b c : ℕ) :
    β q * γ q * monoY (R := R) q b c = monoY q (b + 1) (c + 1) := by
  have h := skew_pow_right (gamma_beta (R := R) q) b
  rw [one_pow, one_smul] at h
  unfold monoY
  rw [mul_assoc, ← mul_assoc (γ q), h, pow_succ', pow_succ']
  simp only [mul_assoc]

theorem beta_mul_monoY (b c : ℕ) : β q * monoY (R := R) q b c = monoY q (b + 1) c := by
  rw [monoY, monoY, ← mul_assoc, ← pow_succ']

theorem gamma_mul_monoY (b c : ℕ) : γ q * monoY (R := R) q b c = monoY q b (c + 1) := by
  have h := skew_pow_right (gamma_beta (R := R) q) b
  rw [one_pow, one_smul] at h
  rw [monoY, monoY, ← mul_assoc, h, mul_assoc, ← pow_succ']

/-! ## Spanning -/

/-- The `R`-span of the ordered monomials. -/
noncomputable abbrev monoSpan : Submodule R (OqSU2 R q) := Submodule.span R (Set.range (mono q))

theorem monoA_mem (n b c : ℕ) : monoA q n b c ∈ monoSpan (R := R) q :=
  Submodule.subset_span ⟨_, mono_nat q n b c⟩

theorem monoD_mem (n b c : ℕ) : monoD q n b c ∈ monoSpan (R := R) q :=
  Submodule.subset_span ⟨_, mono_neg_nat q n b c⟩

theorem alpha_mul_monoA (n b c : ℕ) : α q * monoA (R := R) q n b c = monoA q (n + 1) b c := by
  rw [monoA, monoA, ← mul_assoc, ← pow_succ']

theorem delta_mul_monoD (n b c : ℕ) : δ q * monoD (R := R) q n b c = monoD q (n + 1) b c := by
  rw [monoD, monoD, ← mul_assoc, ← pow_succ']

theorem alpha_mul_monoD_mem (n b c : ℕ) : α q * monoD (R := R) q n b c ∈ monoSpan q := by
  rcases n with _ | n
  · rw [monoD_zero, ← monoA_zero, alpha_mul_monoA]; exact monoA_mem q _ _ _
  · obtain ⟨r, hr⟩ := alpha_mul_delta_pow_succ (R := R) q n
    rw [monoD, ← mul_assoc, hr, add_mul, smul_mul_assoc, mul_assoc, betaGamma_mul_monoY]
    exact add_mem (monoD_mem q _ _ _) (Submodule.smul_mem _ _ (monoD_mem q _ _ _))

theorem delta_mul_monoA_mem (n b c : ℕ) : δ q * monoA (R := R) q n b c ∈ monoSpan q := by
  rcases n with _ | n
  · rw [monoA_zero, ← monoD_zero, delta_mul_monoD]; exact monoD_mem q _ _ _
  · obtain ⟨r, hr⟩ := delta_mul_alpha_pow_succ (R := R) q n
    rw [monoA, ← mul_assoc, hr, add_mul, smul_mul_assoc, mul_assoc, betaGamma_mul_monoY]
    exact add_mem (monoA_mem q _ _ _) (Submodule.smul_mem _ _ (monoA_mem q _ _ _))

theorem beta_mul_monoA (n b c : ℕ) :
    β q * monoA (R := R) q n b c = qi ^ n • monoA q n (b + 1) c := by
  rw [monoA, ← mul_assoc, skew_pow_right (beta_alpha q), smul_mul_assoc, mul_assoc,
    beta_mul_monoY, monoA]

theorem gamma_mul_monoA (n b c : ℕ) :
    γ q * monoA (R := R) q n b c = qi ^ n • monoA q n b (c + 1) := by
  rw [monoA, ← mul_assoc, skew_pow_right (gamma_alpha q), smul_mul_assoc, mul_assoc,
    gamma_mul_monoY, monoA]

theorem beta_mul_monoD (n b c : ℕ) :
    β q * monoD (R := R) q n b c = (q : R) ^ n • monoD q n (b + 1) c := by
  rw [monoD, ← mul_assoc, skew_pow_right (rel_bd q), smul_mul_assoc, mul_assoc,
    beta_mul_monoY, monoD]

theorem gamma_mul_monoD (n b c : ℕ) :
    γ q * monoD (R := R) q n b c = (q : R) ^ n • monoD q n b (c + 1) := by
  rw [monoD, ← mul_assoc, skew_pow_right (rel_gd q), smul_mul_assoc, mul_assoc,
    gamma_mul_monoY, monoD]

/-- Left multiplication by `g` maps the monomial span into itself once it maps every
`monoA` and `monoD` into it. -/
theorem mul_mem_monoSpan_of {g : OqSU2 R q}
    (hA : ∀ n b c, g * monoA q n b c ∈ monoSpan q) (hD : ∀ n b c, g * monoD q n b c ∈ monoSpan q)
    {y : OqSU2 R q} (hy : y ∈ monoSpan q) : g * y ∈ monoSpan q := by
  have hle : monoSpan q ≤ (monoSpan q).comap (LinearMap.mulLeft R g) := by
    rw [Submodule.span_le]
    rintro _ ⟨⟨a, b, c⟩, rfl⟩
    show g * mono q (a, b, c) ∈ monoSpan q
    rcases le_or_gt 0 a with ha | ha
    · obtain ⟨n, rfl⟩ := Int.eq_ofNat_of_zero_le ha
      rw [mono_nat]; exact hA n b c
    · obtain ⟨n, hn⟩ := Int.exists_eq_neg_ofNat ha.le
      subst hn
      rw [mono_neg_nat]; exact hD n b c
  exact hle hy

/-- **PBW spanning.** The ordered monomials span `O_q(SU(2))` over `R`. -/
theorem mono_span : monoSpan (R := R) q = ⊤ := by
  let T : Subalgebra R (OqSU2 R q) :=
    { carrier := {x | ∀ y ∈ monoSpan q, x * y ∈ monoSpan q}
      mul_mem' := by
        intro x y hx hy z hz
        rw [mul_assoc]; exact hx _ (hy _ hz)
      add_mem' := by
        intro x y hx hy z hz
        rw [add_mul]; exact add_mem (hx _ hz) (hy _ hz)
      algebraMap_mem' := by
        intro r z hz
        rw [← Algebra.smul_def]; exact Submodule.smul_mem _ _ hz }
  have hα : α q ∈ T := fun y hy => mul_mem_monoSpan_of q
    (fun n b c => by rw [alpha_mul_monoA]; exact monoA_mem q _ _ _)
    (fun n b c => alpha_mul_monoD_mem q n b c) hy
  have hδ : δ q ∈ T := fun y hy => mul_mem_monoSpan_of q
    (fun n b c => delta_mul_monoA_mem q n b c)
    (fun n b c => by rw [delta_mul_monoD]; exact monoD_mem q _ _ _) hy
  have hβ : β q ∈ T := fun y hy => mul_mem_monoSpan_of q
    (fun n b c => by rw [beta_mul_monoA]; exact Submodule.smul_mem _ _ (monoA_mem q _ _ _))
    (fun n b c => by rw [beta_mul_monoD]; exact Submodule.smul_mem _ _ (monoD_mem q _ _ _)) hy
  have hγ : γ q ∈ T := fun y hy => mul_mem_monoSpan_of q
    (fun n b c => by rw [gamma_mul_monoA]; exact Submodule.smul_mem _ _ (monoA_mem q _ _ _))
    (fun n b c => by rw [gamma_mul_monoD]; exact Submodule.smul_mem _ _ (monoD_mem q _ _ _)) hy
  rw [eq_top_iff]
  intro x _
  have h1 : (1 : OqSU2 R q) ∈ monoSpan q := Submodule.subset_span ⟨_, mono_zero q⟩
  simpa using mem_of_gens T hα hβ hγ hδ x 1 h1

/-! ## Independence, through the model representation -/

theorem monoRep_alpha : monoRep q (α q) = mA (R := R) q := by simp [monoRep]
theorem monoRep_beta : monoRep q (β q) = mB (R := R) q := by simp [monoRep]
theorem monoRep_gamma : monoRep q (γ q) = mG (R := R) q := by simp [monoRep]
theorem monoRep_delta : monoRep q (δ q) = mD (R := R) q := by simp [monoRep]

theorem mG_pow_e (b c : ℕ) : (mG (R := R) q ^ c) (eb R 0 b 0) = eb R 0 b c := by
  induction c with
  | zero => simp
  | succ c ih => rw [pow_succ', Module.End.mul_apply, ih, mG_e]; simp

theorem mB_pow_e (b c : ℕ) : (mB (R := R) q ^ b) (eb R 0 0 c) = eb R 0 b c := by
  induction b with
  | zero => simp
  | succ b ih => rw [pow_succ', Module.End.mul_apply, ih, mB_e]; simp

theorem mA_pow_e (n b c : ℕ) : (mA (R := R) q ^ n) (eb R 0 b c) = eb R n b c := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ', Module.End.mul_apply, ih, mA_e_nonneg q (Int.natCast_nonneg n)]
    push_cast; rfl

theorem mD_pow_e (n b c : ℕ) : (mD (R := R) q ^ n) (eb R 0 b c) = eb R (-(n : ℤ)) b c := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ', Module.End.mul_apply, ih, mD_e_nonpos q (by omega)]
    congr 2; push_cast; ring

theorem monoRep_monoY (b c : ℕ) : monoRep q (monoY q b c) (eb R 0 0 0) = eb R 0 b c := by
  rw [monoY, map_mul, map_pow, map_pow, Module.End.mul_apply, monoRep_beta, monoRep_gamma,
    mG_pow_e, mB_pow_e]

/-- `π(mono i) e(0,0,0) = e(i)`. -/
theorem monoRep_mono (i : MonoIdx) : monoRep q (mono q i) (eb R 0 0 0) = Finsupp.single i 1 := by
  obtain ⟨a, b, c⟩ := i
  rcases le_or_gt 0 a with ha | ha
  · obtain ⟨n, rfl⟩ := Int.eq_ofNat_of_zero_le ha
    rw [mono_nat, monoA, map_mul, map_pow, Module.End.mul_apply, monoRep_monoY, monoRep_alpha,
      mA_pow_e]
  · obtain ⟨n, hn⟩ := Int.exists_eq_neg_ofNat ha.le
    subst hn
    rw [mono_neg_nat, monoD, map_mul, map_pow, Module.End.mul_apply, monoRep_monoY,
      monoRep_delta, mD_pow_e]

/-- The evaluation map `x ↦ π(x) e(0,0,0)`. -/
noncomputable def monoEval : OqSU2 R q →ₗ[R] MonoMod R :=
  (LinearMap.applyₗ (eb R 0 0 0)).comp (monoRep q).toLinearMap

theorem monoEval_apply (x : OqSU2 R q) : monoEval q x = monoRep q x (eb R 0 0 0) := rfl

/-- **PBW independence.** The ordered monomials are linearly independent over `R`. -/
theorem mono_linearIndependent : LinearIndependent R (mono (R := R) q) := by
  apply LinearIndependent.of_comp (monoEval q)
  have : (monoEval q) ∘ (mono q) = fun i => Finsupp.single i (1 : R) := by
    funext i; exact monoRep_mono q i
  rw [this]
  exact Finsupp.linearIndependent_single_one (ι := MonoIdx) (R := R)

/-- **PBW basis.** The ordered monomials `α^a β^b γ^c` (`a ≥ 0`), `δ^(-a) β^b γ^c` (`a < 0`)
form an `R`-basis of `O_q(SU(2))`. -/
noncomputable def pbwBasis : Module.Basis MonoIdx R (OqSU2 R q) :=
  Module.Basis.mk (mono_linearIndependent q) (mono_span q).ge

@[simp] theorem pbwBasis_apply (i : MonoIdx) : pbwBasis (R := R) q i = mono q i := by
  simp [pbwBasis]

/-- The evaluation `x ↦ π(x) e(0,0,0)` is the coordinate map of the PBW basis. -/
theorem monoEval_eq_repr : monoEval (R := R) q = (pbwBasis q).repr.toLinearMap := by
  apply (pbwBasis q).ext
  intro i
  show monoEval q (pbwBasis q i) = (pbwBasis q).repr (pbwBasis q i)
  rw [Module.Basis.repr_self, monoEval_apply, pbwBasis_apply, monoRep_mono]

/-- `O_q(SU(2)) ≃ R^(ℤ × ℕ × ℕ)`, `x ↦ π(x) e(0,0,0)`. -/
noncomputable def pbwEquiv : OqSU2 R q ≃ₗ[R] MonoMod R := (pbwBasis q).repr

theorem pbwEquiv_apply (x : OqSU2 R q) : pbwEquiv q x = monoRep q x (eb R 0 0 0) := by
  rw [← monoEval_apply, monoEval_eq_repr]; rfl

/-- The model representation of `OqSU2HaarState` is faithful. -/
theorem monoRep_faithful : Function.Injective (monoRep (R := R) q) := by
  intro x y h
  apply (pbwEquiv q).injective
  rw [pbwEquiv_apply, pbwEquiv_apply, h]

end QOU.AlgebraicSubstrate.OqSU2
