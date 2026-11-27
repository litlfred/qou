import QOU.Core.LieDerivativeFunctionLinear
import Mathlib.Analysis.Calculus.VectorField
import Mathlib.Analysis.Calculus.FDeriv.Symmetric
import Mathlib.Analysis.Calculus.DifferentialForm.Basic
import Mathlib.Analysis.NormedSpace.Alternating.Curry
import Mathlib.Analysis.NormedSpace.Alternating.Uncurry.Fin
import Mathlib.Analysis.Normed.Module.FiniteDimension

/-!
# Smooth vector fields on a normed space as a Lie–Rinehart pair

Smooth functions `SFun 𝕜 E` (`C^∞` maps `E → 𝕜`, a subalgebra) and smooth vector fields
`SVF 𝕜 E` (`C^∞` maps `E → E`, with Mathlib's `VectorField.lieBracket`) form a Lie–Rinehart
pair (`IsLieRinehart`): fields act on functions by `X f = Df(X)`, and `(f • X)(y) = f y • X y`.
So the function-linear Cartan calculus of `QOU.Core.LieDerivativeFunctionLinear` applies to
non-constant vector fields.

A smooth scalar form `φ : E → E [⋀^Fin n]→L[𝕜] 𝕜` gives a function-linear cochain `toCEv φ`.
Main results, on a finite-dimensional `E`:

* `ceDAlt_toCEv`: the Koszul differential of `toCEv φ` is `toCEv (extDeriv φ)`, for arbitrary
  smooth fields. The proof is algebraic: both sides are tensors
  (`funLinear_ceDAlt`), tensors are determined on a spanning set (`FunLinear.eq_of_span`), the
  constant fields span (`span_const`), and on constant fields the bracket terms vanish.
* `cartan_smoothField`: Cartan's formula `L_X φ = d(ι_X φ) + ι_X dφ` for smooth `X`, with
  Mathlib's `extDeriv` and `VectorField.lieBracket`.

Axioms: `propext`, `Classical.choice`, `Quot.sound`. The choice comes from Mathlib's library
(it is already in the purely algebraic `cartan_formula`), not from an analytic hypothesis, so
there is nothing here for the `Coev` locatedness class to take over.

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

/-! ### Differential forms as function-linear cochains -/

/-- Evaluation of smooth functions at a point, as a ring homomorphism. -/
def SFun.evalHom (y : E) : SFun 𝕜 E →+* 𝕜 where
  toFun f := f y
  map_one' := rfl
  map_mul' _ _ := rfl
  map_zero' := rfl
  map_add' _ _ := rfl

/-- Evaluation of smooth vector fields at a point. -/
def SVF.evalHom (y : E) : SVF 𝕜 E →+ E where
  toFun X := X y
  map_zero' := rfl
  map_add' _ _ := rfl

/-- The constant vector field with value `c`. -/
def SVF.const (c : E) : SVF 𝕜 E :=
  (⟨fun _ => c, show ContDiff 𝕜 ∞ (fun _ : E => c) from contDiff_const⟩ : svfSub 𝕜 E)

@[simp] lemma SVF.const_apply (c y : E) : (SVF.const c : SVF 𝕜 E) y = c := rfl

lemma SVF.coe_const (c : E) : ((SVF.const c : SVF 𝕜 E) : E → E) = fun _ => c := rfl

lemma SVF.lie_const (a b : E) : ⁅(SVF.const a : SVF 𝕜 E), (SVF.const b : SVF 𝕜 E)⁆ = 0 :=
  SVF.ext fun y => by
    rw [SVF.lie_apply, SVF.coe_const, SVF.coe_const]
    simp [lieBracket]

variable {n : ℕ}

lemma eval_update [DecidableEq (Fin n)] (v : Fin n → SVF 𝕜 E) (i : Fin n) (X : SVF 𝕜 E) (y : E) :
    (fun j => Function.update v i X j y) = Function.update (fun j => v j y) i (X y) := by
  funext j
  by_cases h : j = i
  · subst h; simp
  · simp [Function.update_of_ne h]

lemma eval_cons (X : SVF 𝕜 E) (v : Fin n → SVF 𝕜 E) (y : E) :
    (fun j => (Fin.cons X v : Fin (n + 1) → SVF 𝕜 E) j y) =
      Fin.cons (X y) (fun j => v j y) := by
  funext j; refine Fin.cases ?_ (fun j => ?_) j <;> simp

/-- Currying a smooth form against a smooth field is smooth. -/
lemma contDiff_curryLeft_gen {F : Type*} [NormedAddCommGroup F] [NormedSpace 𝕜 F] {m : ℕ}
    {φ : E → E [⋀^Fin (m + 1)]→L[𝕜] F} (hφ : ContDiff 𝕜 ∞ φ) {X : E → E}
    (hX : ContDiff 𝕜 ∞ X) : ContDiff 𝕜 ∞ (fun z => (φ z).curryLeft (X z)) := by
  -- elaborated without an expected type: with one, the normed instances on the codomain of
  -- `curryLeftLI` are not found
  have h0 := ((ContinuousAlternatingMap.curryLeftLI (𝕜 := 𝕜) (E := E) (F := F)
    (n := m)).contDiff.comp hφ).clm_apply hX
  exact h0

/-- A smooth form applied to smooth vector fields is a smooth function. -/
lemma contDiff_apply_fields : ∀ {n : ℕ} {φ : E → E [⋀^Fin n]→L[𝕜] 𝕜},
    ContDiff 𝕜 ∞ φ → ∀ (v : Fin n → SVF 𝕜 E), ContDiff 𝕜 ∞ (fun y => φ y (fun i => v i y))
  | 0, φ, hφ, v => by
    have e : (fun y => φ y (fun i => v i y)) = fun y => φ y Fin.elim0 := by
      funext y; congr 1; funext i; exact i.elim0
    rw [e]; exact (ContinuousAlternatingMap.apply 𝕜 E 𝕜 Fin.elim0).contDiff.comp hφ
  | m + 1, φ, hφ, v => by
    have hψ : ContDiff 𝕜 ∞ (fun y => (φ y).curryLeft (v 0 y)) :=
      contDiff_curryLeft_gen hφ (v 0).contDiff
    have := contDiff_apply_fields hψ (Fin.tail v)
    convert this using 2 with y
    rw [ContinuousAlternatingMap.curryLeft_apply_apply]
    congr 1; funext i; refine Fin.cases ?_ (fun i => ?_) i <;> simp [Fin.tail]

/-- A smooth scalar form `φ : E → E [⋀^Fin n]→L[𝕜] 𝕜` as a cochain on smooth vector fields:
`v ↦ (y ↦ φ y (v₀ y, …, vₙ₋₁ y))`. -/
def toCEv (φ : E → E [⋀^Fin n]→L[𝕜] 𝕜) (hφ : ContDiff 𝕜 ∞ φ) :
    SVF 𝕜 E [⋀^Fin n]→ₗ[𝕜] SFun 𝕜 E where
  toFun v := (⟨fun y => φ y (fun i => v i y), contDiff_apply_fields hφ v⟩ : smoothAlg 𝕜 E)
  map_update_add' v i X Y := SFun.ext fun y => by
    change φ y _ = φ y _ + φ y _
    rw [eval_update, eval_update, eval_update, SVF.add_apply, (φ y).map_update_add]
  map_update_smul' v i c X := SFun.ext fun y => by
    change φ y _ = c • φ y _
    rw [eval_update, eval_update, SVF.const_smul_apply, (φ y).map_update_smul]
  map_eq_zero_of_eq' v i j h hij := SFun.ext fun y =>
    (φ y).map_eq_zero_of_eq (fun k => v k y) (congrArg (fun X : SVF 𝕜 E => X y) h) hij

@[simp] lemma toCEv_apply (φ : E → E [⋀^Fin n]→L[𝕜] 𝕜) (hφ : ContDiff 𝕜 ∞ φ)
    (v : Fin n → SVF 𝕜 E) (y : E) : toCEv φ hφ v y = φ y (fun i => v i y) := rfl

/-- Cochains coming from forms are function-linear (tensors). -/
lemma funLinear_toCEv (φ : E → E [⋀^Fin n]→L[𝕜] 𝕜) (hφ : ContDiff 𝕜 ∞ φ) :
    FunLinear (toCEv φ hφ) := fun v i f X => SFun.ext fun y => by
  change φ y _ = f y * φ y _
  rw [eval_update, eval_update, SVF.smul_apply, (φ y).map_update_smul, smul_eq_mul]

lemma contDiff_extDeriv {φ : E → E [⋀^Fin n]→L[𝕜] 𝕜} (hφ : ContDiff 𝕜 ∞ φ) :
    ContDiff 𝕜 ∞ (extDeriv φ) := by
  have := (ContinuousAlternatingMap.alternatizeUncurryFinCLM 𝕜 E 𝕜).contDiff.comp
    (hφ.fderiv_right (m := ∞) top_add_one_le)
  convert this using 1

/-- In finite dimension the constant fields span the smooth fields over the smooth functions:
`X = Σⱼ (coordⱼ ∘ X) • bⱼ`. -/
lemma span_const [FiniteDimensional 𝕜 E] :
    Submodule.span (SFun 𝕜 E) (Set.range (SVF.const : E → SVF 𝕜 E)) = ⊤ := by
  let b := Module.finBasis 𝕜 E
  refine eq_top_iff.2 fun X _ => ?_
  let c : Fin (Module.finrank 𝕜 E) → SFun 𝕜 E := fun j =>
    (⟨fun y => b.coord j (X y),
      (LinearMap.toContinuousLinearMap (b.coord j)).contDiff.comp X.contDiff⟩ : smoothAlg 𝕜 E)
  have hX : X = ∑ j, c j • SVF.const (b j) := SVF.ext fun y => by
    rw [show (∑ j, c j • SVF.const (b j)) y = SVF.evalHom y (∑ j, c j • SVF.const (b j)) from rfl,
      map_sum]
    exact (b.sum_repr (X y)).symm
  rw [hX]
  exact Submodule.sum_mem _ fun j _ => Submodule.smul_mem _ _ (Submodule.subset_span ⟨b j, rfl⟩)

lemma bracketPart_eq_zero (η : SVF 𝕜 E [⋀^Fin n]→ₗ[𝕜] SFun 𝕜 E) (v : Fin (n + 1) → SVF 𝕜 E)
    (h : ∀ i j, ⁅v i, v j⁆ = 0) : bracketPart η v = 0 := by
  cases n with
  | zero => rfl
  | succ m =>
    show bracketSum η v = 0
    refine Finset.sum_eq_zero fun i _ => Finset.sum_eq_zero fun j _ => ?_
    split_ifs
    · rw [h, η.map_coord_zero 0 (by simp), smul_zero]
    · rfl

/-- On constant fields the Koszul differential is `extDeriv`. -/
lemma ceDAlt_toCEv_const (φ : E → E [⋀^Fin n]→L[𝕜] 𝕜) (hφ : ContDiff 𝕜 ∞ φ)
    (c : Fin (n + 1) → E) (y : E) :
    ceDAlt (toCEv φ hφ) (fun i => SVF.const (c i)) y = extDeriv φ y c := by
  rw [ceDAlt_apply, ceD_eq, bracketPart_eq_zero _ _ fun i j => SVF.lie_const _ _, add_zero,
    extDeriv_apply ((hφ.differentiable (by simp)) y)]
  rw [show firstSum (toCEv φ hφ) (fun i => SVF.const (c i)) y =
    SFun.evalHom y (firstSum (toCEv φ hφ) (fun i => SVF.const (c i))) from rfl]
  simp only [firstSum, map_sum, map_zsmul]
  rfl

/-- **Bridge to Mathlib's exterior derivative, for arbitrary smooth vector fields.** On a
finite-dimensional normed space, the Chevalley–Eilenberg differential of the cochain of a
smooth form `φ` is the cochain of `extDeriv φ`. The bracket terms of the Koszul formula are
the ones that make this hold for non-constant fields. -/
theorem ceDAlt_toCEv [FiniteDimensional 𝕜 E] (φ : E → E [⋀^Fin n]→L[𝕜] 𝕜)
    (hφ : ContDiff 𝕜 ∞ φ) :
    ceDAlt (toCEv φ hφ) = toCEv (extDeriv φ) (contDiff_extDeriv hφ) := by
  refine FunLinear.eq_of_span (funLinear_ceDAlt (funLinear_toCEv φ hφ))
    (funLinear_toCEv _ _) span_const fun v hv => ?_
  -- a constant field is determined by its value at `0`, so no choice is needed here
  have hv' : v = fun i => SVF.const (v i 0) := funext fun i => by
    obtain ⟨c, hc⟩ := hv i
    rw [← hc]; rfl
  rw [hv']
  exact SFun.ext fun y => ceDAlt_toCEv_const φ hφ (fun i => v i 0) y

/-- Pointwise form of `ceDAlt_toCEv`. -/
theorem ceDAlt_toCEv_apply [FiniteDimensional 𝕜 E] (φ : E → E [⋀^Fin n]→L[𝕜] 𝕜)
    (hφ : ContDiff 𝕜 ∞ φ) (v : Fin (n + 1) → SVF 𝕜 E) (y : E) :
    ceDAlt (toCEv φ hφ) v y = extDeriv φ y (fun i => v i y) := by
  rw [ceDAlt_toCEv]; rfl

lemma contDiff_curryLeft_field {φ : E → E [⋀^Fin (n + 1)]→L[𝕜] 𝕜} (hφ : ContDiff 𝕜 ∞ φ)
    (X : SVF 𝕜 E) : ContDiff 𝕜 ∞ (fun z => (φ z).curryLeft (X z)) :=
  contDiff_curryLeft_gen hφ X.contDiff

lemma toCEv_curryLeft (φ : E → E [⋀^Fin (n + 1)]→L[𝕜] 𝕜) (hφ : ContDiff 𝕜 ∞ φ)
    (X : SVF 𝕜 E) :
    toCEv (fun z => (φ z).curryLeft (X z)) (contDiff_curryLeft_field hφ X) =
      (toCEv φ hφ).curryLeft X := by
  ext v y
  change (φ y).curryLeft (X y) (fun i => v i y) = φ y _
  rw [ContinuousAlternatingMap.curryLeft_apply_apply]
  congr 1; funext i; refine Fin.cases ?_ (fun i => ?_) i <;> simp

/-- **Cartan's magic formula for arbitrary smooth vector fields on a finite-dimensional
normed space**, with Mathlib's `extDeriv` and `curryLeft`:
`(L_X φ)(v) = d(ι_X φ)(v) + (dφ)(X, v)`, where `L_X φ` is the algebraic Lie derivative
`X(φ(v)) - Σᵢ φ(…, ⁅X, vᵢ⁆, …)` and `⁅X, vᵢ⁆` is Mathlib's `VectorField.lieBracket`. -/
theorem cartan_smoothField [FiniteDimensional 𝕜 E] (X : SVF 𝕜 E)
    (φ : E → E [⋀^Fin (n + 1)]→L[𝕜] 𝕜) (hφ : ContDiff 𝕜 ∞ φ) (v : Fin (n + 1) → SVF 𝕜 E)
    (y : E) :
    lieDerivAlt X (toCEv φ hφ) v y =
      extDeriv (fun z => (φ z).curryLeft (X z)) y (fun i => v i y) +
        extDeriv φ y (Fin.cons (X y) (fun i => v i y)) := by
  rw [← ceDAlt_toCEv_apply _ (contDiff_curryLeft_field hφ X), ← eval_cons,
    ← ceDAlt_toCEv_apply φ hφ, toCEv_curryLeft, ceDAlt_apply, ceDAlt_apply, lieDerivAlt_apply,
    ← cartan_formula X (toCEv φ hφ) v]
  rfl

end QOU.Transcendental.SmoothVectorFields

end
