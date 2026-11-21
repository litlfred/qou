import Mathlib.Analysis.Calculus.DifferentialForm.Basic
import Mathlib.Algebra.Lie.Basic
import Mathlib.Analysis.Normed.Operator.Mul
import Mathlib.Tactic.NoncommRing

/-!
# QOU.Mathlib.LieValuedForms — a concrete model of Lie-algebra-valued forms

`QOU.Mathlib.NonAbelianStokes.LieValuedOneForm` is an abstract carrier with no
model.  This file gives a **concrete** model on a real normed space `E`, built
on Mathlib's differential forms
(`Mathlib.Analysis.Calculus.DifferentialForm.Basic`, where an `n`-form is
`E → E [⋀^Fin n]→L[ℝ] F` and `extDeriv` is the exterior derivative).

## The bracket

Mathlib has no normed Lie algebras: `LieRing` extends `AddCommGroup`, so
`[NormedAddCommGroup 𝔤] [LieRing 𝔤]` would carry two unrelated additive
structures.  We therefore take the bracket as data on a normed space:
`ContinuousLieBracket 𝔤` is a continuous bilinear map `𝔤 →L[ℝ] 𝔤 →L[ℝ] 𝔤`
vanishing on the diagonal and satisfying the Leibniz (Jacobi) identity.
`ContinuousLieBracket.toLieRing` / `toLieAlgebra` show that this is exactly a
Lie algebra structure on the *same* additive group, and `commutatorBracket`
supplies the (generally non-abelian) commutator bracket on any normed
`ℝ`-algebra.

## What is defined

* `OneForm E 𝔤`, `TwoForm E 𝔤` — `𝔤`-valued 1- and 2-forms on `E`.
* `bracketWedge L α β` — the 2-form
  `[α ∧ β](v, w) = ⁅α v, β w⁆ − ⁅α w, β v⁆`, built with Mathlib's
  `alternatizeUncurryFin` (the same operation `extDeriv` is built from).
* `curvature L α = dα + ½ [α ∧ α]` — the curvature / structure equation.
* `covExtDeriv L α β = dβ + [α ∧ β]` — the covariant exterior derivative
  of a 1-form `β`.

## What is proved

* evaluation formulas (`bracketWedge_apply`, `curvature_apply`);
* graded symmetry `[α ∧ β] = [β ∧ α]` for 1-forms (`bracketWedge_comm`) —
  this uses antisymmetry of the bracket and fails for a non-alternating
  bilinear map;
* bilinearity of `[· ∧ ·]`, and additivity of `covExtDeriv` in `β`;
* abelian reduction: if the bracket is zero, `curvature α = dα`;
* `extDeriv` of a constant form is zero, hence the curvature of a constant
  `𝔤`-valued 1-form `A` is `½[A ∧ A]`, and a constant connection is flat
  **iff** all brackets `⁅A v, A w⁆` vanish (`curvature_const_eq_zero_iff`).

## What is NOT here

No multiplicative (path-ordered) integral, no holonomy, no parallel
transport, no non-abelian Stokes theorem, no forms on manifolds, and no
Bianchi identity: Mathlib has none of this infrastructure, and nothing here
supplies it.  `QOU.Mathlib.NonAbelianStokes` remains an axiomatised class.

-- Ref: [leitner2026] standard: Kobayashi–Nomizu, Foundations of Differential Geometry I, Ch. II §5 (curvature form, structure equation)
-/

namespace QOU.Mathlib.LieValuedForms

open ContinuousAlternatingMap

/-! ### Continuous Lie brackets on a normed space -/

/-- A continuous Lie bracket on a real normed space: a continuous bilinear map
vanishing on the diagonal and satisfying the Leibniz form of the Jacobi
identity (the form used by Mathlib's `LieRing.leibniz_lie`). -/
structure ContinuousLieBracket (𝔤 : Type*) [NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤] where
  /-- The bracket `⁅x, y⁆ = bracket x y`. -/
  bracket : 𝔤 →L[ℝ] 𝔤 →L[ℝ] 𝔤
  /-- `⁅x, x⁆ = 0`. -/
  self_eq_zero : ∀ x, bracket x x = 0
  /-- `⁅x, ⁅y, z⁆⁆ = ⁅⁅x, y⁆, z⁆ + ⁅y, ⁅x, z⁆⁆`. -/
  leibniz : ∀ x y z, bracket x (bracket y z) = bracket (bracket x y) z + bracket y (bracket x z)

namespace ContinuousLieBracket

variable {𝔤 : Type*} [NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤] (L : ContinuousLieBracket 𝔤)

/-- Antisymmetry, derived from `⁅x, x⁆ = 0` and bilinearity. -/
theorem swap (x y : 𝔤) : L.bracket y x = -L.bracket x y := by
  have h := L.self_eq_zero (x + y)
  simp only [map_add, ContinuousLinearMap.add_apply, L.self_eq_zero, zero_add, add_zero] at h
  exact eq_neg_of_add_eq_zero_left h

/-- The bracket makes the underlying additive group of `𝔤` a Lie ring. -/
@[reducible] def toLieRing : LieRing 𝔤 where
  bracket x y := L.bracket x y
  add_lie x y z := by simp
  lie_add x y z := by simp
  lie_self x := L.self_eq_zero x
  leibniz_lie x y z := L.leibniz x y z

/-- … and an `ℝ`-Lie algebra (with the normed-space scalar action). -/
@[reducible] def toLieAlgebra : @LieAlgebra ℝ 𝔤 _ L.toLieRing :=
  @LieAlgebra.mk ℝ 𝔤 _ L.toLieRing (inferInstance : Module ℝ 𝔤) (fun t x y => by
    change L.bracket x (t • y) = t • L.bracket x y
    simp)

theorem toLieRing_bracket (x y : 𝔤) :
    (letI := L.toLieRing; ⁅x, y⁆) = L.bracket x y := rfl

end ContinuousLieBracket

/-- The commutator bracket `⁅x, y⁆ = x * y − y * x` on a normed `ℝ`-algebra,
as a continuous Lie bracket.  Non-abelian whenever `A` is noncommutative. -/
noncomputable def commutatorBracket (A : Type*) [NormedRing A] [NormedAlgebra ℝ A] :
    ContinuousLieBracket A where
  bracket := ContinuousLinearMap.mul ℝ A - (ContinuousLinearMap.mul ℝ A).flip
  self_eq_zero x := by simp
  leibniz x y z := by simp; noncomm_ring

@[simp] theorem commutatorBracket_apply (A : Type*) [NormedRing A] [NormedAlgebra ℝ A]
    (x y : A) : (commutatorBracket A).bracket x y = x * y - y * x := by
  simp [commutatorBracket]

/-! ### Lie-valued forms -/

variable {E 𝔤 : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [NormedAddCommGroup 𝔤] [NormedSpace ℝ 𝔤]

variable (E 𝔤) in
/-- `𝔤`-valued 1-forms on `E` (Mathlib's representation of differential forms). -/
abbrev OneForm := E → E [⋀^Fin 1]→L[ℝ] 𝔤

variable (E 𝔤) in
/-- `𝔤`-valued 2-forms on `E`. -/
abbrev TwoForm := E → E [⋀^Fin 2]→L[ℝ] 𝔤

/-- The continuous linear map underlying the value of a 1-form. -/
noncomputable def toCLM (f : E [⋀^Fin 1]→L[ℝ] 𝔤) : E →L[ℝ] 𝔤 :=
  (ofSubsingleton ℝ E 𝔤 (0 : Fin 1)).symm f

@[simp] theorem toCLM_apply (f : E [⋀^Fin 1]→L[ℝ] 𝔤) (v : E) :
    toCLM f v = f (fun _ => v) := rfl

theorem toCLM_add (f g : E [⋀^Fin 1]→L[ℝ] 𝔤) : toCLM (f + g) = toCLM f + toCLM g := by
  ext v; simp

theorem toCLM_smul (c : ℝ) (f : E [⋀^Fin 1]→L[ℝ] 𝔤) : toCLM (c • f) = c • toCLM f := by
  ext v; simp

variable (L : ContinuousLieBracket 𝔤)

/-- Auxiliary curried map `v ↦ (w ↦ ⁅a v, b w⁆)`. -/
noncomputable def wedgeAux (a b : E →L[ℝ] 𝔤) : E →L[ℝ] E [⋀^Fin 1]→L[ℝ] 𝔤 :=
  ((ofSubsingletonLIE (𝕜 := ℝ) (E := E) (F := 𝔤) (0 : Fin 1)).toContinuousLinearEquiv :
      (E →L[ℝ] 𝔤) →L[ℝ] E [⋀^Fin 1]→L[ℝ] 𝔤) ∘L
    ((ContinuousLinearMap.compL ℝ E 𝔤 𝔤).flip b ∘L (L.bracket ∘L a))

theorem wedgeAux_apply (a b : E →L[ℝ] 𝔤) (v : E) (u : Fin 1 → E) :
    wedgeAux L a b v u = L.bracket (a v) (b (u 0)) := by
  simp [wedgeAux]

/-- Pointwise bracket-wedge of two `𝔤`-valued covectors. -/
noncomputable def bracketWedgeAt (a b : E →L[ℝ] 𝔤) : E [⋀^Fin 2]→L[ℝ] 𝔤 :=
  alternatizeUncurryFin (wedgeAux L a b)

theorem bracketWedgeAt_apply (a b : E →L[ℝ] 𝔤) (v : Fin 2 → E) :
    bracketWedgeAt L a b v = L.bracket (a (v 0)) (b (v 1)) - L.bracket (a (v 1)) (b (v 0)) := by
  rw [bracketWedgeAt, alternatizeUncurryFin_apply, Fin.sum_univ_two]
  simp [wedgeAux_apply, Fin.removeNth_apply, Fin.tail, sub_eq_add_neg]

/-- The bracket-wedge `[α ∧ β]` of two `𝔤`-valued 1-forms, a `𝔤`-valued 2-form. -/
noncomputable def bracketWedge (α β : OneForm E 𝔤) : TwoForm E 𝔤 :=
  fun x => bracketWedgeAt L (toCLM (α x)) (toCLM (β x))

/-- `[α ∧ β](v₀, v₁) = ⁅α v₀, β v₁⁆ − ⁅α v₁, β v₀⁆`. -/
theorem bracketWedge_apply (α β : OneForm E 𝔤) (x : E) (v : Fin 2 → E) :
    bracketWedge L α β x v =
      L.bracket (α x (fun _ => v 0)) (β x (fun _ => v 1)) -
        L.bracket (α x (fun _ => v 1)) (β x (fun _ => v 0)) := by
  simp [bracketWedge, bracketWedgeAt_apply]

/-- Graded symmetry for 1-forms: `[α ∧ β] = [β ∧ α]`.  Uses antisymmetry of
the bracket; false for a non-alternating bilinear map. -/
theorem bracketWedge_comm (α β : OneForm E 𝔤) : bracketWedge L α β = bracketWedge L β α := by
  funext x; ext v
  rw [bracketWedge_apply, bracketWedge_apply, L.swap (α x (fun _ => v 1)) (β x (fun _ => v 0)),
    L.swap (α x (fun _ => v 0)) (β x (fun _ => v 1))]
  abel

/-- `[α ∧ α](v₀, v₁) = 2 ⁅α v₀, α v₁⁆`. -/
theorem bracketWedge_self_apply (α : OneForm E 𝔤) (x : E) (v : Fin 2 → E) :
    bracketWedge L α α x v = (2 : ℝ) • L.bracket (α x (fun _ => v 0)) (α x (fun _ => v 1)) := by
  rw [bracketWedge_apply, L.swap (α x (fun _ => v 0)) (α x (fun _ => v 1)), two_smul,
    sub_neg_eq_add]

theorem bracketWedge_add_left (α α' β : OneForm E 𝔤) :
    bracketWedge L (α + α') β = bracketWedge L α β + bracketWedge L α' β := by
  funext x; ext v
  simp only [bracketWedge_apply, Pi.add_apply, ContinuousAlternatingMap.add_apply, map_add,
    ContinuousLinearMap.add_apply]
  abel

theorem bracketWedge_add_right (α β β' : OneForm E 𝔤) :
    bracketWedge L α (β + β') = bracketWedge L α β + bracketWedge L α β' := by
  rw [bracketWedge_comm, bracketWedge_add_left, bracketWedge_comm L β, bracketWedge_comm L β']

theorem bracketWedge_smul_left (c : ℝ) (α β : OneForm E 𝔤) :
    bracketWedge L (c • α) β = c • bracketWedge L α β := by
  funext x; ext v
  simp only [bracketWedge_apply, Pi.smul_apply, ContinuousAlternatingMap.smul_apply, map_smul,
    ContinuousLinearMap.smul_apply, smul_sub]

/-! ### Curvature and covariant exterior derivative -/

/-- Curvature (structure equation) `F_α = dα + ½ [α ∧ α]`. -/
noncomputable def curvature (α : OneForm E 𝔤) : TwoForm E 𝔤 :=
  fun x => extDeriv α x + (1 / 2 : ℝ) • bracketWedge L α α x

/-- `F_α(v₀, v₁) = dα(v₀, v₁) + ⁅α v₀, α v₁⁆`. -/
theorem curvature_apply (α : OneForm E 𝔤) (x : E) (v : Fin 2 → E) :
    curvature L α x v = extDeriv α x v + L.bracket (α x (fun _ => v 0)) (α x (fun _ => v 1)) := by
  rw [curvature, ContinuousAlternatingMap.add_apply, ContinuousAlternatingMap.smul_apply,
    bracketWedge_self_apply, smul_smul]
  norm_num

/-- Abelian reduction: for the zero bracket, the curvature is `dα`. -/
theorem curvature_of_bracket_eq_zero (hL : L.bracket = 0) (α : OneForm E 𝔤) :
    curvature L α = extDeriv α := by
  funext x; ext v
  rw [curvature_apply, hL]
  simp

/-- The exterior derivative of a constant form vanishes. -/
theorem extDeriv_const {n : ℕ} (A : E [⋀^Fin n]→L[ℝ] 𝔤) (x : E) :
    extDeriv (fun _ : E => A) x = 0 := by
  rw [extDeriv, fderiv_const_apply, ← alternatizeUncurryFinCLM_apply]
  exact _root_.map_zero (alternatizeUncurryFinCLM ℝ E 𝔤)

/-- The curvature of a constant 1-form `A` is `½ [A ∧ A]`. -/
theorem curvature_const (A : E [⋀^Fin 1]→L[ℝ] 𝔤) (x : E) :
    curvature L (fun _ => A) x = (1 / 2 : ℝ) • bracketWedge L (fun _ => A) (fun _ => A) x := by
  rw [curvature, extDeriv_const, zero_add]

/-- A constant connection is flat iff the bracket vanishes on its image. -/
theorem curvature_const_eq_zero_iff (A : E [⋀^Fin 1]→L[ℝ] 𝔤) :
    curvature L (fun _ : E => A) = 0 ↔
      ∀ v w : E, L.bracket (A (fun _ => v)) (A (fun _ => w)) = 0 := by
  constructor
  · intro h v w
    have := congrArg (fun F => F 0 ![v, w]) h
    simpa [curvature_apply, extDeriv_const] using this
  · intro h
    funext x; ext v
    rw [curvature_apply, extDeriv_const]
    simp [h]

/-- Covariant exterior derivative of a `𝔤`-valued 1-form `β` relative to the
connection `α`: `d_α β = dβ + [α ∧ β]`. -/
noncomputable def covExtDeriv (α β : OneForm E 𝔤) : TwoForm E 𝔤 :=
  fun x => extDeriv β x + bracketWedge L α β x

/-- `d_α α = F_α + ½ [α ∧ α]`. -/
theorem covExtDeriv_self (α : OneForm E 𝔤) (x : E) :
    covExtDeriv L α α x = curvature L α x + (1 / 2 : ℝ) • bracketWedge L α α x := by
  simp only [covExtDeriv, curvature, add_assoc, ← add_smul]
  norm_num

/-- The trivial connection gives the ordinary exterior derivative. -/
theorem covExtDeriv_zero (β : OneForm E 𝔤) : covExtDeriv L 0 β = extDeriv β := by
  funext x; ext v
  simp [covExtDeriv, bracketWedge_apply]

/-- `d_α` is additive on differentiable forms. -/
theorem covExtDeriv_add (α β β' : OneForm E 𝔤) (x : E)
    (hβ : DifferentiableAt ℝ β x) (hβ' : DifferentiableAt ℝ β' x) :
    covExtDeriv L α (β + β') x = covExtDeriv L α β x + covExtDeriv L α β' x := by
  simp only [covExtDeriv, extDeriv_add hβ hβ', bracketWedge_add_right, Pi.add_apply]
  abel

end QOU.Mathlib.LieValuedForms
