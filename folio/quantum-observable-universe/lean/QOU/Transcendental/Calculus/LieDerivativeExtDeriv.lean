import QOU.Core.LieDerivativeComplex
import Mathlib.Analysis.Calculus.DifferentialForm.Basic
import Mathlib.Analysis.Calculus.FDeriv.Symmetric
import Mathlib.Analysis.NormedSpace.Alternating.Curry

/-!
# Bridge: Chevalley–Eilenberg calculus ↔ Mathlib's analytic `extDeriv`

`QOU.Core.LieDerivative` and `QOU.Core.LieDerivativeComplex` prove the Cartan calculus
(`L_x = d ι_x + ι_x d`, `d ∘ d = 0`, `[L_x, d] = 0`, `[L_x, L_y] = L_⁅x,y⁆`) for
Chevalley–Eilenberg cochains of a Lie algebra `L` with values in a Lie module `M`, over a
generic commutative ring. This file connects that algebra to Mathlib's analytic exterior
derivative `extDeriv` on a normed space `E` over `𝕜` (`ℝ` or `ℂ`).

It sits behind the transcendental/analytic boundary (owner ruling 2026-11-27, bean
`qou-dk7p`): it uses `fderiv`, smoothness and the symmetry of second derivatives. Nothing
in `QOU.Core` imports it.

* `ConstVF E` is `E` with the zero bracket: the Lie algebra of constant vector fields.
* `Smooth 𝕜 E F` is the module of `C^∞` maps `E → F`; a constant field `x` acts on it by
  the directional derivative `D_x`. The Lie-module axiom is the symmetry of second
  derivatives (`ContDiffAt.isSymmSndFDerivAt`).
* `toCE ω` reads a smooth Mathlib form `ω : E → E [⋀^Fin n]→L[𝕜] F` as a cochain.

Main results:

* `ceDAlt_toCE`: the Koszul differential of `toCE ω` is `extDeriv ω`.
* `lieDerivAlt_toCE`: the Lie derivative along a constant field is `fderiv 𝕜 ω y x`.
* `cartan_constField`: Cartan's formula `D_x ω = d (ι_x ω) + ι_x (d ω)` for Mathlib forms
  and constant fields, transported from the algebraic `cartan_formula`.

Scope: constant vector fields only, so the bracket part of `d` is zero. Non-constant fields
(Mathlib's `VectorField.lieBracket`) are covered by
`QOU.Transcendental.Calculus.SmoothVectorFields`, through `C^∞(E)`-linear cochains.
Sorry-free; no empirical value enters this file. Bean `qou-pn77`.
-/

open scoped ContDiff

noncomputable section

namespace QOU.Transcendental.LieDerivativeExtDeriv

open QOU.LieDerivative

variable {𝕜 : Type*} [RCLike 𝕜]
  {E : Type*} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  {F : Type*} [NormedAddCommGroup F] [NormedSpace 𝕜 F]

/-- Constant vector fields on `E`: the vector space `E` with the zero bracket. -/
def ConstVF (E : Type*) : Type _ := E

instance (E : Type*) [AddCommGroup E] : AddCommGroup (ConstVF E) :=
  inferInstanceAs (AddCommGroup E)

instance (E : Type*) [AddCommGroup E] : LieRing (ConstVF E) where
  bracket _ _ := 0
  add_lie _ _ _ := (add_zero 0).symm
  lie_add _ _ _ := (add_zero 0).symm
  lie_self _ := rfl
  leibniz_lie _ _ _ := (add_zero 0).symm

instance (E : Type*) [AddCommGroup E] [Module 𝕜 E] : LieAlgebra 𝕜 (ConstVF E) :=
  { (inferInstanceAs (Module 𝕜 E)) with
    lie_smul := fun c _ _ => by change (0 : E) = c • (0 : E); exact (smul_zero c).symm }

/-- The constant vector field with value `x`. -/
def ConstVF.of (x : E) : ConstVF E := x

@[simp] lemma constVF_lie (x y : ConstVF E) : ⁅x, y⁆ = 0 := rfl

variable (𝕜 E F) in
/-- Smooth (`C^∞`) functions `E → F`, as a `𝕜`-submodule. -/
def smoothFns : Submodule 𝕜 (E → F) where
  carrier := {f | ContDiff 𝕜 ∞ f}
  add_mem' {f g} hf hg := by simp only [Set.mem_setOf_eq] at *; exact hf.add hg
  zero_mem' := by simp only [Set.mem_setOf_eq]; exact contDiff_const
  smul_mem' c f hf := by simp only [Set.mem_setOf_eq] at *; exact hf.const_smul c

variable (𝕜 E F) in
/-- The type of smooth functions. -/
abbrev Smooth : Type _ := smoothFns 𝕜 E F

lemma smooth_contDiff (f : Smooth 𝕜 E F) : ContDiff 𝕜 ∞ (f : E → F) := f.2

lemma smooth_differentiable (f : Smooth 𝕜 E F) : Differentiable 𝕜 (f : E → F) :=
  (smooth_contDiff f).differentiable (by simp)

lemma contDiff_fderiv_apply {f : E → F} (hf : ContDiff 𝕜 ∞ f) (x : E) :
    ContDiff 𝕜 ∞ (fun y => fderiv 𝕜 f y x) :=
  (hf.fderiv_right (m := ∞) (by simp)).clm_apply contDiff_const

/-- The directional derivative `D_x f` of a smooth function along a constant field. -/
def dirDeriv (x : E) (f : Smooth 𝕜 E F) : Smooth 𝕜 E F :=
  ⟨fun y => fderiv 𝕜 (f : E → F) y x, contDiff_fderiv_apply (smooth_contDiff f) x⟩

@[simp] lemma dirDeriv_apply (x : E) (f : Smooth 𝕜 E F) (y : E) :
    (dirDeriv x f : E → F) y = fderiv 𝕜 (f : E → F) y x := rfl

lemma dirDeriv_comm (x y : E) (f : Smooth 𝕜 E F) :
    dirDeriv x (dirDeriv y f) = dirDeriv y (dirDeriv x f) := by
  have hf := smooth_contDiff f
  have h2 : Differentiable 𝕜 (fderiv 𝕜 (f : E → F)) :=
    (hf.fderiv_right (m := ∞) (by simp)).differentiable (by simp)
  apply Subtype.ext
  funext z
  show fderiv 𝕜 (fun w => fderiv 𝕜 (f : E → F) w y) z x =
    fderiv 𝕜 (fun w => fderiv 𝕜 (f : E → F) w x) z y
  rw [fderiv_clm_apply (h2 z) (differentiableAt_const _),
    fderiv_clm_apply (h2 z) (differentiableAt_const _)]
  simp
  exact ((hf.contDiffAt).isSymmSndFDerivAt
    (by simp; exact WithTop.coe_le_coe.2 (le_top : (2 : ℕ∞) ≤ ⊤))) x y

instance : LieRingModule (ConstVF E) (Smooth 𝕜 E F) where
  bracket x f := dirDeriv (x : E) f
  add_lie x y f := by
    apply Subtype.ext; funext z
    exact map_add (fderiv 𝕜 (f : E → F) z) (x : E) y
  lie_add x f g := by
    apply Subtype.ext; funext z
    show fderiv 𝕜 (fun w => (f : E → F) w + (g : E → F) w) z (x : E) = _
    rw [fderiv_fun_add (smooth_differentiable f z) (smooth_differentiable g z)]
    rfl
  leibniz_lie x y f := by
    apply Subtype.ext; funext z
    have hc := congrArg (fun g : Smooth 𝕜 E F => (g : E → F) z)
      (dirDeriv_comm (𝕜 := 𝕜) (F := F) (show E from x) (show E from y) f)
    change fderiv 𝕜 (fun w => fderiv 𝕜 (f : E → F) w (show E from y)) z (show E from x) =
      fderiv 𝕜 (f : E → F) z (0 : E) +
        fderiv 𝕜 (fun w => fderiv 𝕜 (f : E → F) w (show E from x)) z (show E from y)
    rw [map_zero, zero_add]
    exact hc

@[simp] lemma lie_smooth_apply (x : ConstVF E) (f : Smooth 𝕜 E F) (z : E) :
    ((⁅x, f⁆ : Smooth 𝕜 E F) : E → F) z = fderiv 𝕜 (f : E → F) z (x : E) := rfl

instance : LieModule 𝕜 (ConstVF E) (Smooth 𝕜 E F) where
  smul_lie c x f := by
    apply Subtype.ext; funext z
    exact map_smul (fderiv 𝕜 (f : E → F) z) c (x : E)
  lie_smul c x f := by
    apply Subtype.ext; funext z
    show fderiv 𝕜 (fun w => c • (f : E → F) w) z (x : E) = _
    rw [fderiv_fun_const_smul (smooth_differentiable f z)]
    rfl

/-! ### Differential forms as Chevalley–Eilenberg cochains -/

variable {n : ℕ}

lemma contDiff_apply_const {φ : E → E [⋀^Fin n]→L[𝕜] F} (hφ : ContDiff 𝕜 ∞ φ)
    (v : Fin n → E) : ContDiff 𝕜 ∞ (fun y => φ y v) :=
  (ContinuousAlternatingMap.apply 𝕜 E F v).contDiff.comp hφ

/-- A smooth Mathlib differential form `φ : E → E [⋀^Fin n]→L[𝕜] F`, read as an alternating
map from constant vector fields to smooth functions: `v ↦ (y ↦ φ y v)`. -/
def toCE (φ : E → E [⋀^Fin n]→L[𝕜] F) (hφ : ContDiff 𝕜 ∞ φ) :
    ConstVF E [⋀^Fin n]→ₗ[𝕜] Smooth 𝕜 E F where
  toFun v := ⟨fun y => φ y v, contDiff_apply_const hφ v⟩
  map_update_add' v i a b := by
    apply Subtype.ext; funext y; exact (φ y).map_update_add v i a b
  map_update_smul' v i c a := by
    apply Subtype.ext; funext y; exact (φ y).map_update_smul v i c a
  map_eq_zero_of_eq' v i j h hij := by
    apply Subtype.ext; funext y; exact (φ y).map_eq_zero_of_eq v h hij

@[simp] lemma toCE_apply (φ : E → E [⋀^Fin n]→L[𝕜] F) (hφ : ContDiff 𝕜 ∞ φ)
    (v : Fin n → ConstVF E) (y : E) :
    ((toCE φ hφ v : Smooth 𝕜 E F) : E → F) y = φ y v := rfl

/-- With constant vector fields the bracket part of the Koszul differential vanishes. -/
lemma bracketPart_constVF (φ : ConstVF E [⋀^Fin n]→ₗ[𝕜] Smooth 𝕜 E F)
    (v : Fin (n + 1) → ConstVF E) : bracketPart φ v = 0 := by
  cases n with
  | zero => rfl
  | succ m =>
    show bracketSum φ v = 0
    refine Finset.sum_eq_zero fun i _ => Finset.sum_eq_zero fun j _ => ?_
    split_ifs
    · rw [constVF_lie, φ.map_coord_zero 0 (by simp), smul_zero]
    · rfl

/-- The coadjoint part of the Lie derivative vanishes for constant vector fields. -/
lemma theta_constVF (x : ConstVF E) (φ : ConstVF E [⋀^Fin n]→ₗ[𝕜] Smooth 𝕜 E F)
    (v : Fin n → ConstVF E) : theta x φ v = 0 :=
  Finset.sum_eq_zero fun i _ => by
    rw [constVF_lie]; exact φ.map_coord_zero i (by simp)

/-- **Bridge to Mathlib's exterior derivative.** On constant vector fields the
Chevalley–Eilenberg differential `ceDAlt` of `QOU.Core.LieDerivativeComplex` is Mathlib's
analytic `extDeriv`. -/
theorem ceDAlt_toCE (φ : E → E [⋀^Fin n]→L[𝕜] F) (hφ : ContDiff 𝕜 ∞ φ)
    (v : Fin (n + 1) → ConstVF E) (y : E) :
    ((ceDAlt (toCE φ hφ) v : Smooth 𝕜 E F) : E → F) y = extDeriv φ y v := by
  rw [ceDAlt_apply, ceD_eq, bracketPart_constVF, add_zero,
    extDeriv_apply ((hφ.differentiable (by simp)) y)]
  simp only [firstSum, Submodule.coe_sum, Finset.sum_apply, Submodule.coe_smul_of_tower,
    Pi.smul_apply, lie_smooth_apply]
  rfl

/-- **Lie derivative along a constant field** is the directional derivative of the form. -/
theorem lieDerivAlt_toCE (x : E) (φ : E → E [⋀^Fin n]→L[𝕜] F) (hφ : ContDiff 𝕜 ∞ φ)
    (v : Fin n → ConstVF E) (y : E) :
    ((lieDerivAlt (ConstVF.of x) (toCE φ hφ) v : Smooth 𝕜 E F) : E → F) y =
      fderiv 𝕜 φ y x v := by
  have hd := (hφ.differentiable (by simp)) y
  simp only [lieDerivAlt_apply, lieDeriv, constVF_lie, AlternatingMap.map_update_zero,
    Finset.sum_const_zero, sub_zero]
  exact fderiv_continuousAlternatingMap_apply_const_apply hd v x

lemma contDiff_curryLeft {φ : E → E [⋀^Fin (n + 1)]→L[𝕜] F} (hφ : ContDiff 𝕜 ∞ φ) (x : E) :
    ContDiff 𝕜 ∞ (fun z => (φ z).curryLeft x) :=
  ((ContinuousAlternatingMap.curryLeftLI (𝕜 := 𝕜) (E := E) (F := F) (n := n)).contDiff.comp
    hφ).clm_apply contDiff_const

lemma toCE_curryLeft (φ : E → E [⋀^Fin (n + 1)]→L[𝕜] F) (hφ : ContDiff 𝕜 ∞ φ) (x : E) :
    toCE (fun z => (φ z).curryLeft x) (contDiff_curryLeft hφ x) =
      (toCE φ hφ).curryLeft (ConstVF.of x) := by
  ext; rfl

/-- **Cartan's magic formula for constant vector fields on a normed space**, stated with
Mathlib's analytic `extDeriv` and `ContinuousAlternatingMap.curryLeft`:
`D_x ω = d (ι_x ω) + ι_x (d ω)`. It is the algebraic `cartan_formula` transported along
`ceDAlt_toCE`. -/
theorem cartan_constField (x : E) (φ : E → E [⋀^Fin (n + 1)]→L[𝕜] F) (hφ : ContDiff 𝕜 ∞ φ)
    (v : Fin (n + 1) → E) (y : E) :
    fderiv 𝕜 φ y x v =
      extDeriv (fun z => (φ z).curryLeft x) y v + extDeriv φ y (Fin.cons x v) := by
  rw [← ceDAlt_toCE _ (contDiff_curryLeft hφ x) v y, ← ceDAlt_toCE φ hφ (Fin.cons x v) y,
    ← lieDerivAlt_toCE x φ hφ v y, toCE_curryLeft, ceDAlt_apply, ceDAlt_apply,
    lieDerivAlt_apply]
  exact (congrArg (fun g : Smooth 𝕜 E F => (g : E → F) y)
    (cartan_formula (ConstVF.of x) (toCE φ hφ) v)).symm

end QOU.Transcendental.LieDerivativeExtDeriv

end
