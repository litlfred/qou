import QOU.Core.LieDerivativeFunctionLinear
import Mathlib.Analysis.Calculus.VectorField
import Mathlib.Analysis.Calculus.FDeriv.Symmetric

/-!
# Smooth vector fields on a normed space as a Lie–Rinehart pair

Smooth functions `SFun 𝕜 E` (`C^∞` maps `E → 𝕜`, a subalgebra) and smooth vector fields
`SVF 𝕜 E` (`C^∞` maps `E → E`, with Mathlib's `VectorField.lieBracket`) form a Lie–Rinehart
pair (`IsLieRinehart`): fields act on functions by `X f = Df(X)`, and `(f • X)(y) = f y • X y`.
So the function-linear Cartan calculus of `QOU.Core.LieDerivativeFunctionLinear` applies to
non-constant vector fields.

Behind the transcendental/analytic boundary (owner ruling 2026-11-27, bean `qou-dk7p`).
Sorry-free; no empirical value. Bean `qou-pn77`.
-/

open scoped ContDiff

noncomputable section

namespace QOU.Transcendental.SmoothVectorFields

open VectorField QOU.LieDerivative

variable {𝕜 : Type*} [RCLike 𝕜] {E : Type*} [NormedAddCommGroup E] [NormedSpace 𝕜 E]

lemma top_add_one_le : (∞ : WithTop ℕ∞) + 1 ≤ ∞ := by simp

lemma minSmoothness_two_le : minSmoothness 𝕜 2 ≤ (∞ : WithTop ℕ∞) := by
  simp; exact WithTop.coe_le_coe.2 (le_top : (2 : ℕ∞) ≤ ⊤)

variable (𝕜 E) in
/-- Smooth scalar functions on `E`. -/
def smoothAlg : Subalgebra 𝕜 (E → 𝕜) where
  carrier := {f | ContDiff 𝕜 ∞ f}
  mul_mem' {f g} hf hg := by simp only [Set.mem_setOf_eq] at *; exact hf.mul hg
  add_mem' {f g} hf hg := by simp only [Set.mem_setOf_eq] at *; exact hf.add hg
  algebraMap_mem' r := by simp only [Set.mem_setOf_eq]; exact contDiff_const

variable (𝕜 E) in
/-- The algebra of smooth functions. -/
def SFun : Type _ := smoothAlg 𝕜 E

instance : CommRing (SFun 𝕜 E) := inferInstanceAs (CommRing (smoothAlg 𝕜 E))
instance : Algebra 𝕜 (SFun 𝕜 E) := inferInstanceAs (Algebra 𝕜 (smoothAlg 𝕜 E))
instance : CoeFun (SFun 𝕜 E) (fun _ => E → 𝕜) := ⟨fun f => (f : smoothAlg 𝕜 E).1⟩

@[ext] lemma SFun.ext {f g : SFun 𝕜 E} (h : ∀ y, f y = g y) : f = g :=
  Subtype.ext (funext h)

@[simp] lemma SFun.add_apply (f g : SFun 𝕜 E) (y : E) : (f + g) y = f y + g y := rfl
@[simp] lemma SFun.mul_apply (f g : SFun 𝕜 E) (y : E) : (f * g) y = f y * g y := rfl
@[simp] lemma SFun.one_apply (y : E) : (1 : SFun 𝕜 E) y = 1 := rfl
@[simp] lemma SFun.zero_apply (y : E) : (0 : SFun 𝕜 E) y = 0 := rfl
@[simp] lemma SFun.smul_apply' (c : 𝕜) (f : SFun 𝕜 E) (y : E) : (c • f) y = c • f y := rfl

variable (𝕜 E) in
/-- Smooth vector fields on `E`, as a submodule. -/
def svfSub : Submodule 𝕜 (E → E) where
  carrier := {X | ContDiff 𝕜 ∞ X}
  add_mem' {f g} hf hg := by simp only [Set.mem_setOf_eq] at *; exact hf.add hg
  zero_mem' := by simp only [Set.mem_setOf_eq]; exact contDiff_const
  smul_mem' c f hf := by simp only [Set.mem_setOf_eq] at *; exact hf.const_smul c

variable (𝕜 E) in
/-- Smooth vector fields. -/
def SVF : Type _ := svfSub 𝕜 E

instance : AddCommGroup (SVF 𝕜 E) := inferInstanceAs (AddCommGroup (svfSub 𝕜 E))

instance : CoeFun (SVF 𝕜 E) (fun _ => E → E) := ⟨fun X => (X : svfSub 𝕜 E).1⟩

lemma SVF.contDiff (X : SVF 𝕜 E) : ContDiff 𝕜 ∞ X := (X : svfSub 𝕜 E).2

lemma SVF.differentiable (X : SVF 𝕜 E) : Differentiable 𝕜 X :=
  X.contDiff.differentiable (by simp)

@[ext] lemma SVF.ext {X Y : SVF 𝕜 E} (h : ∀ y, X y = Y y) : X = Y :=
  Subtype.ext (funext h)

@[simp] lemma SVF.add_apply (X Y : SVF 𝕜 E) (y : E) : (X + Y) y = X y + Y y := rfl
@[simp] lemma SVF.zero_apply (y : E) : (0 : SVF 𝕜 E) y = 0 := rfl
@[simp] lemma SVF.neg_apply (X : SVF 𝕜 E) (y : E) : (-X) y = -X y := rfl
@[simp] lemma SVF.sub_apply (X Y : SVF 𝕜 E) (y : E) : (X - Y) y = X y - Y y := rfl

lemma SFun.contDiff (f : SFun 𝕜 E) : ContDiff 𝕜 ∞ (f : E → 𝕜) := (f : smoothAlg 𝕜 E).2

lemma SFun.differentiable (f : SFun 𝕜 E) : Differentiable 𝕜 (f : E → 𝕜) :=
  f.contDiff.differentiable (by simp)

/-- Function coefficients on vector fields, `(f • X)(y) = f y • X y`. -/
instance : SMul (SFun 𝕜 E) (SVF 𝕜 E) :=
  ⟨fun f X => (⟨fun y => (f : E → 𝕜) y • X y, f.contDiff.smul X.contDiff⟩ : svfSub 𝕜 E)⟩

@[simp] lemma SVF.smul_apply (f : SFun 𝕜 E) (X : SVF 𝕜 E) (y : E) :
    (f • X) y = (f : E → 𝕜) y • X y := rfl

instance : Module (SFun 𝕜 E) (SVF 𝕜 E) where
  one_smul X := SVF.ext fun y => by simp only [SVF.smul_apply, SFun.one_apply, one_smul]
  mul_smul f g X := SVF.ext fun y => by simp only [SVF.smul_apply, SFun.mul_apply, mul_smul]
  smul_zero f := SVF.ext fun y => by simp only [SVF.smul_apply, SVF.zero_apply, smul_zero]
  smul_add f X Y := SVF.ext fun y => by simp only [SVF.smul_apply, SVF.add_apply, smul_add]
  add_smul f g X := SVF.ext fun y => by simp only [SVF.smul_apply, SVF.add_apply, SFun.add_apply, add_smul]
  zero_smul X := SVF.ext fun y => by simp only [SVF.smul_apply, SFun.zero_apply, zero_smul, SVF.zero_apply]

/-- `𝕜`-scalars on vector fields. -/
instance : Module 𝕜 (SVF 𝕜 E) := inferInstanceAs (Module 𝕜 (svfSub 𝕜 E))

@[simp] lemma SVF.const_smul_apply (c : 𝕜) (X : SVF 𝕜 E) (y : E) : (c • X) y = c • X y := rfl

/-- The Lie bracket of smooth vector fields. -/
def SVF.bracket (X Y : SVF 𝕜 E) : SVF 𝕜 E :=
  (⟨lieBracket 𝕜 X Y, X.contDiff.lieBracket_vectorField Y.contDiff top_add_one_le⟩ :
    svfSub 𝕜 E)

instance : LieRing (SVF 𝕜 E) where
  bracket := SVF.bracket
  add_lie X Y Z := SVF.ext fun y => by
    change lieBracket 𝕜 (X + Y : E → E) Z y = _
    exact lieBracket_add_left (X.differentiable y) (Y.differentiable y)
  lie_add X Y Z := SVF.ext fun y => by
    change lieBracket 𝕜 X (Y + Z : E → E) y = _
    exact lieBracket_add_right (Y.differentiable y) (Z.differentiable y)
  lie_self X := SVF.ext fun y => by
    change lieBracket 𝕜 X X y = 0
    simp
  leibniz_lie X Y Z := SVF.ext fun y =>
    leibniz_identity_lieBracket minSmoothness_two_le X.contDiff.contDiffAt
      Y.contDiff.contDiffAt Z.contDiff.contDiffAt

@[simp] lemma SVF.lie_apply (X Y : SVF 𝕜 E) (y : E) : ⁅X, Y⁆ y = lieBracket 𝕜 X Y y := rfl

instance : LieAlgebra 𝕜 (SVF 𝕜 E) where
  lie_smul c X Y := SVF.ext fun y => by
    change lieBracket 𝕜 X (c • (Y : E → E)) y = _
    exact lieBracket_const_smul_right (Y.differentiable y)

/-- A vector field acting on a function: `X f = Df(X)`. -/
def SVF.act (X : SVF 𝕜 E) (f : SFun 𝕜 E) : SFun 𝕜 E :=
  (⟨fun y => fderiv 𝕜 (f : E → 𝕜) y (X y),
    (f.contDiff.fderiv_right (m := ∞) top_add_one_le).clm_apply X.contDiff⟩ : smoothAlg 𝕜 E)

lemma fderiv_act (X Y : SVF 𝕜 E) (f : SFun 𝕜 E) (y : E) :
    fderiv 𝕜 (fun z => fderiv 𝕜 (f : E → 𝕜) z (Y z)) y (X y) =
      fderiv 𝕜 (fderiv 𝕜 (f : E → 𝕜)) y (X y) (Y y) +
        fderiv 𝕜 (f : E → 𝕜) y (fderiv 𝕜 Y y (X y)) := by
  have h2 : Differentiable 𝕜 (fderiv 𝕜 (f : E → 𝕜)) :=
    (f.contDiff.fderiv_right (m := ∞) top_add_one_le).differentiable (by simp)
  rw [fderiv_clm_apply (h2 y) (Y.differentiable y)]
  simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.comp_apply,
    ContinuousLinearMap.flip_apply]
  abel

instance : LieRingModule (SVF 𝕜 E) (SFun 𝕜 E) where
  bracket := SVF.act
  add_lie X Y f := SFun.ext fun y => map_add (fderiv 𝕜 (f : E → 𝕜) y) (X y) (Y y)
  lie_add X f g := SFun.ext fun y => by
    change fderiv 𝕜 ((f : E → 𝕜) + (g : E → 𝕜)) y (X y) = _
    rw [fderiv_add (f.differentiable y) (g.differentiable y)]
    rfl
  leibniz_lie X Y f := SFun.ext fun y => by
    change fderiv 𝕜 (fun z => fderiv 𝕜 (f : E → 𝕜) z (Y z)) y (X y) =
      fderiv 𝕜 (f : E → 𝕜) y (lieBracket 𝕜 X Y y) +
        fderiv 𝕜 (fun z => fderiv 𝕜 (f : E → 𝕜) z (X z)) y (Y y)
    rw [fderiv_act, fderiv_act, lieBracket, map_sub,
      (f.contDiff.contDiffAt.isSymmSndFDerivAt minSmoothness_two_le) (X y) (Y y)]
    abel

@[simp] lemma SVF.lie_fn_apply (X : SVF 𝕜 E) (f : SFun 𝕜 E) (y : E) :
    ((⁅X, f⁆ : SFun 𝕜 E) : E → 𝕜) y = fderiv 𝕜 (f : E → 𝕜) y (X y) := rfl

instance : LieModule 𝕜 (SVF 𝕜 E) (SFun 𝕜 E) where
  smul_lie c X f := SFun.ext fun y => map_smul (fderiv 𝕜 (f : E → 𝕜) y) c (X y)
  lie_smul c X f := SFun.ext fun y => by
    change fderiv 𝕜 (c • (f : E → 𝕜)) y (X y) = _
    rw [fderiv_const_smul (f.differentiable y)]
    rfl

/-- **Smooth vector fields and smooth functions form a Lie–Rinehart pair.** -/
instance : IsLieRinehart (SFun 𝕜 E) (SVF 𝕜 E) where
  lie_mul X f g := SFun.ext fun y => by
    change fderiv 𝕜 ((f : E → 𝕜) * (g : E → 𝕜)) y (X y) = _
    rw [fderiv_mul (f.differentiable y) (g.differentiable y)]
    simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply, smul_eq_mul]
    rfl
  smul_lie_fn f X g := SFun.ext fun y => by
    change fderiv 𝕜 (g : E → 𝕜) y ((f : E → 𝕜) y • X y) = _
    rw [map_smul, smul_eq_mul]
    rfl
  smul_lie f X Z := SVF.ext fun y => by
    change lieBracket 𝕜 (fun z => (f : E → 𝕜) z • X z) Z y = _
    rw [lieBracket_fmul_left (f.differentiable y) (X.differentiable y)]
    simp only [SVF.sub_apply, SVF.smul_apply, SVF.lie_apply]
    change _ = _ - fderiv 𝕜 (f : E → 𝕜) y (Z y) • X y
    rw [neg_smul, sub_eq_add_neg, add_comm]

end QOU.Transcendental.SmoothVectorFields

end
