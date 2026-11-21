import Mathlib.Analysis.Calculus.DifferentialForm.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.FiniteDimensional.Lemmas
/-!
# Contact forms on normed spaces (three-dimensional case)

Bean `qou-vspi`.  Mathlib (pin `f897ebc`) has differential forms on normed spaces
(`E → E [⋀^Fin n]→L[𝕜] F`, `extDeriv`) but no wedge product of forms and no contact or
symplectic geometry.  This file supplies the minimum needed to state and check the contact
condition in dimension 3, at the normed-space (not manifold) level.

## What is built (all proved, no `sorry`)

* `wedge12 a b` — wedge of a 1-form value with a 2-form value, a continuous alternating
  3-map, with the evaluation formula `wedge12_apply`
  `(a ∧ b)(v₀,v₁,v₂) = a(v₀)b(v₁,v₂) − a(v₁)b(v₀,v₂) + a(v₂)b(v₀,v₁)`.
  Multilinearity, the alternating property and the operator-norm bound are proved by hand.
* `IsContactFormOn α s` : `∀ x ∈ s, α x ∧ dα x ≠ 0`, with `dα = extDeriv α` (Mathlib's);
  `IsContactForm3` on `ℝ³ = Fin 3 → ℝ`.
* The standard example `alphaStd = dz − y dx`: `dα = dx ∧ dy` computed from `extDeriv`
  (`extDeriv_alphaStd_apply`); `α ∧ dα` evaluated on any `v` equals `det v`
  (`wedge_alphaStd_apply`) and `1` on the standard basis, hence `alphaStd_isContact`.
* Non-example: `dz` is not contact (`dzConst_not_contact`), because `d(dz) = 0`.
* `contactPlane α x = ker α_x`; on a 3-dimensional space it has `finrank 2` whenever
  `α x ≠ 0`, and a contact form is nowhere zero, so the standard structure is a plane field
  (`finrank_contactPlane_alphaStd`).

## What is NOT built

* No general wedge `Ωᵏ × Ωˡ → Ωᵏ⁺ˡ`.  Mathlib's `AlternatingMap.domCoprod` exists, but its
  value is a sum over `Equiv.Perm.ModSumCongr`, and relating it to `wedge12` was not done;
  hence no `α ∧ (dα)ⁿ` for `n ≥ 2` and no contact condition in dimension `2n + 1 > 3`.
* `wedge12` uses the shuffle normalisation, chosen so that the standard volume form is the
  determinant; it is not checked against any other Mathlib convention.
* No manifold-level version, no Reeb vector field, no Darboux theorem, no Gray stability,
  no contact structure as a co-oriented plane field independent of a defining form.
-/

open ContinuousAlternatingMap
namespace QOU.Mathlib.ContactForms
variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-! ### Slot-wise linearity of 1- and 2-forms written with `![…]` -/

section Slots
variable (a : E [⋀^Fin 1]→L[ℝ] ℝ) (b : E [⋀^Fin 2]→L[ℝ] ℝ) (u u' w : E) (c : ℝ)

theorem one_add : a ![u + u'] = a ![u] + a ![u'] := by
  have h := a.map_update_add ![u] 0 u u'
  have e : ∀ z : E, Function.update ![u] 0 z = ![z] := fun z => by
    funext i; fin_cases i; simp
  rwa [e, e, e] at h
theorem one_smul : a ![c • u] = c * a ![u] := by
  have h := a.map_update_smul ![u] 0 c u
  have e : ∀ z : E, Function.update ![u] 0 z = ![z] := fun z => by
    funext i; fin_cases i; simp
  rwa [e, e] at h
theorem two_add_left : b ![u + u', w] = b ![u, w] + b ![u', w] := by
  have h := b.map_update_add ![u, w] 0 u u'
  have e : ∀ z : E, Function.update ![u, w] 0 z = ![z, w] := fun z => by
    funext i; fin_cases i <;> simp
  rwa [e, e, e] at h
theorem two_smul_left : b ![c • u, w] = c * b ![u, w] := by
  have h := b.map_update_smul ![u, w] 0 c u
  have e : ∀ z : E, Function.update ![u, w] 0 z = ![z, w] := fun z => by
    funext i; fin_cases i <;> simp
  rwa [e, e] at h
theorem two_add_right : b ![w, u + u'] = b ![w, u] + b ![w, u'] := by
  have h := b.map_update_add ![w, u] 1 u u'
  have e : ∀ z : E, Function.update ![w, u] 1 z = ![w, z] := fun z => by
    funext i; fin_cases i <;> simp
  rwa [e, e, e] at h
theorem two_smul_right : b ![w, c • u] = c * b ![w, u] := by
  have h := b.map_update_smul ![w, u] 1 c u
  have e : ∀ z : E, Function.update ![w, u] 1 z = ![w, z] := fun z => by
    funext i; fin_cases i <;> simp
  rwa [e, e] at h
theorem two_self : b ![u, u] = 0 :=
  b.map_eq_zero_of_eq ![u, u] (i := 0) (j := 1) rfl (by decide)
theorem two_antisymm : b ![u, w] = - b ![w, u] := by
  have h := b.map_swap ![w, u] (i := 0) (j := 1) (by decide)
  have e : (![w, u] ∘ Equiv.swap (0 : Fin 2) 1) = ![u, w] := by
    funext i; fin_cases i <;> simp
  rw [e] at h; exact h
end Slots

/-- The explicit wedge formula
`(a ∧ b)(v₀,v₁,v₂) = a(v₀)b(v₁,v₂) − a(v₁)b(v₀,v₂) + a(v₂)b(v₀,v₁)`
(shuffle convention, so `dx ∧ dy ∧ dz` evaluates to the determinant). -/
def wedge12Fun (a : E [⋀^Fin 1]→L[ℝ] ℝ) (b : E [⋀^Fin 2]→L[ℝ] ℝ) (v : Fin 3 → E) : ℝ :=
  a ![v 0] * b ![v 1, v 2] - a ![v 1] * b ![v 0, v 2] + a ![v 2] * b ![v 0, v 1]

/-- `wedge12Fun a b` is multilinear and alternating. -/
def wedge12Alt (a : E [⋀^Fin 1]→L[ℝ] ℝ) (b : E [⋀^Fin 2]→L[ℝ] ℝ) : E [⋀^Fin 3]→ₗ[ℝ] ℝ where
  toFun := wedge12Fun a b
  map_update_add' := by
    intro inst m i x y
    obtain rfl : inst = instDecidableEqFin 3 := Subsingleton.elim _ _
    fin_cases i <;>
      simp [wedge12Fun, one_add, two_add_left, two_add_right] <;> ring
  map_update_smul' := by
    intro inst m i c x
    obtain rfl : inst = instDecidableEqFin 3 := Subsingleton.elim _ _
    fin_cases i <;>
      simp [wedge12Fun, one_smul, two_smul_left, two_smul_right] <;> ring
  map_eq_zero_of_eq' v i j hij hne := by
    fin_cases i <;> fin_cases j
    all_goals first
      | exact absurd rfl hne
      | (simp only [Fin.zero_eta, Fin.mk_one, Fin.reduceFinMk, Fin.isValue] at hij
         simp only [wedge12Fun, hij, two_self, two_antisymm b (v 2) (v 1),
           two_antisymm b (v 1) (v 0)]
         ring)

/-- Operator-norm bound making the wedge continuous. -/
theorem norm_wedge12Fun_le (a : E [⋀^Fin 1]→L[ℝ] ℝ) (b : E [⋀^Fin 2]→L[ℝ] ℝ) (v : Fin 3 → E) :
    ‖wedge12Fun a b v‖ ≤ (3 * (‖a‖ * ‖b‖)) * ∏ i, ‖v i‖ := by
  have ha : ∀ u : E, ‖a ![u]‖ ≤ ‖a‖ * ‖u‖ := fun u => by
    simpa using a.le_opNorm ![u]
  have hb : ∀ u w : E, ‖b ![u, w]‖ ≤ ‖b‖ * (‖u‖ * ‖w‖) := fun u w => by
    simpa [Fin.prod_univ_two] using b.le_opNorm ![u, w]
  have hP : ∏ i, ‖v i‖ = ‖v 0‖ * ‖v 1‖ * ‖v 2‖ := by
    simp [Fin.prod_univ_three]
  have t : ∀ (i j k : E), ‖a ![i] * b ![j, k]‖ ≤ ‖a‖ * ‖b‖ * (‖i‖ * ‖j‖ * ‖k‖) := by
    intro i j k
    rw [norm_mul]
    calc ‖a ![i]‖ * ‖b ![j, k]‖ ≤ (‖a‖ * ‖i‖) * (‖b‖ * (‖j‖ * ‖k‖)) :=
          mul_le_mul (ha i) (hb j k) (norm_nonneg _) (by positivity)
      _ = _ := by ring
  have t0 := t (v 0) (v 1) (v 2)
  have t1 := t (v 1) (v 0) (v 2)
  have t2 := t (v 2) (v 0) (v 1)
  rw [hP]
  unfold wedge12Fun
  calc ‖a ![v 0] * b ![v 1, v 2] - a ![v 1] * b ![v 0, v 2] + a ![v 2] * b ![v 0, v 1]‖
      ≤ ‖a ![v 0] * b ![v 1, v 2]‖ + ‖a ![v 1] * b ![v 0, v 2]‖ + ‖a ![v 2] * b ![v 0, v 1]‖ := by
        refine (norm_add_le _ _).trans ?_
        gcongr
        exact norm_sub_le _ _
    _ ≤ _ := by nlinarith [t0, t1, t2]

/-- Wedge of a continuous alternating 1-map with a 2-map: a continuous alternating 3-map,
i.e. the pointwise value of a 3-form in Mathlib's convention. -/
noncomputable def wedge12 (a : E [⋀^Fin 1]→L[ℝ] ℝ) (b : E [⋀^Fin 2]→L[ℝ] ℝ) :
    E [⋀^Fin 3]→L[ℝ] ℝ :=
  (wedge12Alt a b).mkContinuous (3 * (‖a‖ * ‖b‖)) (norm_wedge12Fun_le a b)

theorem wedge12_apply (a : E [⋀^Fin 1]→L[ℝ] ℝ) (b : E [⋀^Fin 2]→L[ℝ] ℝ) (v : Fin 3 → E) :
    wedge12 a b v =
      a ![v 0] * b ![v 1, v 2] - a ![v 1] * b ![v 0, v 2] + a ![v 2] * b ![v 0, v 1] := rfl

/-- `ℝ³` with coordinates `(x, y, z) = (p 0, p 1, p 2)`. -/
abbrev R3 := Fin 3 → ℝ

/-- The constant coordinate 1-form `dxᵢ` (`i = 0, 1, 2` for `dx, dy, dz`). -/
noncomputable def coord1 (i : Fin 3) : R3 [⋀^Fin 1]→L[ℝ] ℝ :=
  ContinuousAlternatingMap.ofSubsingleton ℝ R3 ℝ 0 (ContinuousLinearMap.proj i)

@[simp] theorem coord1_apply (i : Fin 3) (v : Fin 1 → R3) : coord1 i v = v 0 i := rfl

/-- The linear map `p ↦ −y(p) · dx`. -/
noncomputable def yDx : R3 →L[ℝ] (R3 [⋀^Fin 1]→L[ℝ] ℝ) :=
  (-(ContinuousLinearMap.proj 1 : R3 →L[ℝ] ℝ)).smulRight (coord1 0)

/-- The standard contact form `α = dz − y dx` on `ℝ³`. -/
noncomputable def alphaStd : R3 → R3 [⋀^Fin 1]→L[ℝ] ℝ := fun p => coord1 2 + yDx p

theorem alphaStd_apply (p : R3) (v : Fin 1 → R3) : alphaStd p v = v 0 2 - p 1 * v 0 0 := by
  simp [alphaStd, yDx]; ring

/-- `α` is affine in the base point, so its derivative is the constant `yDx`. -/
theorem fderiv_alphaStd (p : R3) : fderiv ℝ alphaStd p = yDx := by
  unfold alphaStd
  rw [fderiv_const_add, ContinuousLinearMap.fderiv]

/-- `dα = dx ∧ dy`, computed with Mathlib's `extDeriv`. -/
theorem extDeriv_alphaStd_apply (p : R3) (v : Fin 2 → R3) :
    extDeriv alphaStd p v = v 0 0 * v 1 1 - v 0 1 * v 1 0 := by
  rw [extDeriv, fderiv_alphaStd, alternatizeUncurryFin_apply]
  simp [Fin.sum_univ_two, yDx, Fin.removeNth]
  ring


/-- `α` is a contact form on `s` in the three-dimensional (`n = 1`) sense: `α ∧ dα` is
nowhere zero on `s`.  It is the contact condition only when `finrank ℝ E = 3`; the
definition itself does not impose that. -/
def IsContactFormOn (α : E → E [⋀^Fin 1]→L[ℝ] ℝ) (s : Set E) : Prop :=
  ∀ x ∈ s, wedge12 (α x) (extDeriv α x) ≠ 0

/-- Contact form on all of `ℝ³`. -/
def IsContactForm3 (α : R3 → R3 [⋀^Fin 1]→L[ℝ] ℝ) : Prop := IsContactFormOn α Set.univ

/-- `α ∧ dα = dx ∧ dy ∧ dz` for the standard form: its value on `v` is `det v`. -/
theorem wedge_alphaStd_apply (p : R3) (v : Fin 3 → R3) :
    wedge12 (alphaStd p) (extDeriv alphaStd p) v = (Matrix.of fun i j => v i j).det := by
  rw [wedge12_apply, Matrix.det_fin_three]
  simp only [alphaStd_apply, extDeriv_alphaStd_apply, Matrix.of_apply, Matrix.cons_val_zero,
    Matrix.cons_val_one]
  ring

/-- On the standard basis `α ∧ dα` evaluates to `1`. -/
theorem wedge_alphaStd_basis (p : R3) :
    wedge12 (alphaStd p) (extDeriv alphaStd p) (fun i => Pi.single i 1) = 1 := by
  rw [wedge_alphaStd_apply]
  have : (Matrix.of fun i j => (Pi.single i (1 : ℝ) : R3) j) = 1 := by
    ext i j
    simp [Matrix.one_apply, Pi.single_apply, eq_comm]
  rw [this, Matrix.det_one]

/-- `dz − y dx` is a contact form on `ℝ³`. -/
theorem alphaStd_isContact : IsContactForm3 alphaStd := by
  intro p _ h
  have := wedge_alphaStd_basis p
  rw [h] at this
  simp at this

/-- The closed 1-form `dz` (constant coefficients). -/
noncomputable def dzConst : R3 → R3 [⋀^Fin 1]→L[ℝ] ℝ := fun _ => coord1 2

/-- `d(dz) = 0`. -/
theorem extDeriv_dzConst (p : R3) : extDeriv dzConst p = 0 := by
  rw [extDeriv, show dzConst = fun _ => coord1 2 from rfl, fderiv_fun_const, Pi.zero_apply]
  ext v; simp [alternatizeUncurryFin_apply]

/-- Non-example: `dz` is not contact, since `d(dz) = 0` forces `dz ∧ d(dz) = 0`. -/
theorem dzConst_not_contact : ¬ IsContactForm3 dzConst := by
  intro h
  apply h 0 (Set.mem_univ _)
  ext v
  simp [wedge12_apply, extDeriv_dzConst]

/-- The contact distribution `ξ_x = ker α_x`. -/
def contactPlane (α : E → E [⋀^Fin 1]→L[ℝ] ℝ) (x : E) : Submodule ℝ E :=
  LinearMap.ker (((ContinuousAlternatingMap.ofSubsingleton ℝ E ℝ (0 : Fin 1)).symm (α x) :
    E →L[ℝ] ℝ) : E →ₗ[ℝ] ℝ)

/-- A contact form vanishes nowhere. -/
theorem ne_zero_of_isContactFormOn {α : E → E [⋀^Fin 1]→L[ℝ] ℝ} {s : Set E}
    (h : IsContactFormOn α s) {x : E} (hx : x ∈ s) : α x ≠ 0 := by
  intro h0
  apply h x hx
  ext v
  simp [wedge12_apply, h0]

/-- On a 3-dimensional space the kernel of a nonzero 1-form value is a plane. -/
theorem finrank_contactPlane (hdim : Module.finrank ℝ E = 3)
    (α : E → E [⋀^Fin 1]→L[ℝ] ℝ) (x : E) (hx : α x ≠ 0) :
    Module.finrank ℝ (contactPlane α x) = 2 := by
  haveI : FiniteDimensional ℝ E := Module.finite_of_finrank_eq_succ hdim
  set L := (ContinuousAlternatingMap.ofSubsingleton ℝ E ℝ (0 : Fin 1)).symm (α x) with hL
  have hL0 : L ≠ 0 := by
    intro h0
    apply hx
    have : α x = ContinuousAlternatingMap.ofSubsingleton ℝ E ℝ (0 : Fin 1) L := by
      rw [hL, Equiv.apply_symm_apply]
    rw [this, h0]
    ext v; simp
  obtain ⟨u, hu⟩ : ∃ u, L u ≠ 0 := by
    by_contra hc
    push_neg at hc
    exact hL0 (ContinuousLinearMap.ext hc)
  set f : E →ₗ[ℝ] ℝ := (L : E →ₗ[ℝ] ℝ) with hf
  have hr : Module.finrank ℝ (LinearMap.range f) = 1 := by
    have htop : LinearMap.range f = ⊤ := by
      rw [eq_top_iff]
      intro t _
      refine ⟨(t / L u) • u, ?_⟩
      simp [hf, map_smul, smul_eq_mul, div_mul_cancel₀ t hu]
    rw [htop, finrank_top, Module.finrank_self]
  have := LinearMap.finrank_range_add_finrank_ker f
  show Module.finrank ℝ (LinearMap.ker f) = 2
  omega

/-- The standard contact structure on `ℝ³` is a plane field. -/
theorem finrank_contactPlane_alphaStd (p : R3) :
    Module.finrank ℝ (contactPlane alphaStd p) = 2 :=
  finrank_contactPlane (by simp) alphaStd p
    (ne_zero_of_isContactFormOn alphaStd_isContact (Set.mem_univ p))

end QOU.Mathlib.ContactForms

-- Ref: [leitner2026] standard: Geiges, An Introduction to Contact Topology, Ch. 1–2 (contact forms, the standard contact structure on ℝ³)
