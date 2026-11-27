import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic

/-!
# Beltrami fields: steady Euler, exact Navier–Stokes, and the sl₂ Reeb field

Bean `qou-byzu` (NS vector 5). Audit:
`docs/audits/2026-10-12-ns-v5-beltrami-reeb.md`.

This file proves three groups of facts. All are sorry-free, use no `axiom`,
and state no manifold-level Navier–Stokes fact as a hypothesis.

**Part A: flat calculus on ℝ³, in coordinates.** Partial derivatives are
Mathlib `deriv` of coordinate slices.
* `lamb₁/₂/₃`: the Lamb identity `(u·∇)u = ∇(|u|²/2) − u × curl u`.
* `beltrami_steady_euler`: if `curl u = λ u` and `div u = 0`, then `u` solves
  steady Euler with pressure `p = −|u|²/2`.
* `beltrami_eigen_ns`: if in addition `Δu = −μ u`, then
  `U(t) = e^{−νμt} u` with `P(t) = −e^{−2νμt}|u|²/2` solves incompressible
  Navier–Stokes exactly.

**Part B: the ABC flow on T³.** The field
`u = (A sin z + C cos y, B sin x + A cos z, C sin y + B cos x)` satisfies
`curl u = u`, `div u = 0` and `Δu = −u`, computed by `deriv` with no
hypothesis. Hence `e^{−νt} u` is an exact, globally smooth, `2π`-periodic NS
solution (`abc_ns_exact`, `abc_periodic`).

**Part C: the left-invariant model of `UT(Σ_g) = Γ\PSL₂(ℝ)`.** The basis
`X = H/2`, `Y = (E+F)/2`, `V = (E−F)/2` of `sl₂(ℝ)` has brackets
`[X,Y] = V`, `[X,V] = Y`, `[Y,V] = −X` (`sl2_brackets`, checked as 2×2
matrices). Take the metric `diag(1, 1, s²)` and the Koszul connection of the
left-invariant metric. Then:
* `V` is Killing, since `ad_V` is skew;
* `∇_V V = 0`;
* `curl V = −s V`, so `curl² V = s² V`;
* `Ric V = (s²/2) V` and `∇*∇ V = (s²/2) V`;
* Weitzenböck holds on `V`: `∇*∇ V + Ric V = curl² V`;
* the deformation viscous operator `Δ_H − 2 Ric` annihilates `V`.

**Scope of Part C.** Part C is the computation on the Lie algebra, i.e. on
left-invariant fields. It does *not* formalize that left-invariant
fields, forms and the Levi-Civita connection descend to `Γ\PSL₂(ℝ)`. That
step is standard: `Γ` acts on the left and every object here is
left-invariant. Nor does it formalize that the manifold operators restricted
to left-invariant data are the formulas used here. Both steps are stated in
the audit as `[S]` (standard, not formalized).
-/

namespace QOU.FluidDynamics.BeltramiSteadyEuler

open Real

noncomputable section

/-! ## Part A — flat calculus in coordinates -/

/-- A scalar field on ℝ³ in coordinates `(x, y, z)`. -/
abbrev SField := ℝ → ℝ → ℝ → ℝ

/-- `∂/∂x` as the derivative of the `x`-slice. -/
noncomputable def px (f : SField) : SField := fun x y z => deriv (fun a => f a y z) x
/-- `∂/∂y`. -/
noncomputable def py (f : SField) : SField := fun x y z => deriv (fun b => f x b z) y
/-- `∂/∂z`. -/
noncomputable def pz (f : SField) : SField := fun x y z => deriv (fun c => f x y c) z

/-- A vector field on ℝ³, as three component functions. -/
structure VField where
  u₁ : SField
  u₂ : SField
  u₃ : SField

namespace VField

variable (u : VField)

noncomputable def curl₁ : SField := fun x y z => py u.u₃ x y z - pz u.u₂ x y z
noncomputable def curl₂ : SField := fun x y z => pz u.u₁ x y z - px u.u₃ x y z
noncomputable def curl₃ : SField := fun x y z => px u.u₂ x y z - py u.u₁ x y z

noncomputable def div : SField := fun x y z => px u.u₁ x y z + py u.u₂ x y z + pz u.u₃ x y z

/-- Kinetic-energy density `|u|²/2`. -/
noncomputable def ke : SField := fun x y z => (u.u₁ x y z ^ 2 + u.u₂ x y z ^ 2 + u.u₃ x y z ^ 2) / 2

/-- Advective derivative `(u·∇) f`. -/
noncomputable def adv (f : SField) : SField := fun x y z =>
  u.u₁ x y z * px f x y z + u.u₂ x y z * py f x y z + u.u₃ x y z * pz f x y z

/-- `curl u = λ u` everywhere. -/
def IsBeltrami (lam : ℝ) : Prop :=
  ∀ x y z, u.curl₁ x y z = lam * u.u₁ x y z ∧ u.curl₂ x y z = lam * u.u₂ x y z ∧
    u.curl₃ x y z = lam * u.u₃ x y z

/-- Every component has differentiable coordinate slices at every point. -/
def SlicesDiff : Prop :=
  ∀ f ∈ [u.u₁, u.u₂, u.u₃], ∀ x y z : ℝ,
    DifferentiableAt ℝ (fun a => f a y z) x ∧ DifferentiableAt ℝ (fun b => f x b z) y ∧
      DifferentiableAt ℝ (fun c => f x y c) z

end VField

/-- Flat Laplacian, diagonal second partials. -/
noncomputable def lap (f : SField) : SField := fun x y z =>
  px (px f) x y z + py (py f) x y z + pz (pz f) x y z

/-- Derivative of a sum of three squares, halved. -/
theorem deriv_half_sq_sum (f g h : ℝ → ℝ) (t : ℝ) (hf : DifferentiableAt ℝ f t)
    (hg : DifferentiableAt ℝ g t) (hh : DifferentiableAt ℝ h t) :
    deriv (fun a => (f a ^ 2 + g a ^ 2 + h a ^ 2) / 2) t =
      f t * deriv f t + g t * deriv g t + h t * deriv h t := by
  have H := (((hf.hasDerivAt.pow 2).add (hg.hasDerivAt.pow 2)).add
    (hh.hasDerivAt.pow 2)).div_const 2
  rw [show (fun a => (f a ^ 2 + g a ^ 2 + h a ^ 2) / 2) =
      (fun x => (f ^ 2 + g ^ 2 + h ^ 2) x / 2) from rfl, H.deriv]
  push_cast
  ring

/-- `deriv` of a negated function, in the `fun a => -f a` form. -/
theorem deriv_neg_fun (f : ℝ → ℝ) (t : ℝ) : deriv (fun a => -f a) t = -deriv f t :=
  deriv.neg

section Lamb

variable (u : VField) (hu : u.SlicesDiff)
include hu

theorem px_ke (x y z : ℝ) :
    px u.ke x y z = u.u₁ x y z * px u.u₁ x y z + u.u₂ x y z * px u.u₂ x y z +
      u.u₃ x y z * px u.u₃ x y z :=
  deriv_half_sq_sum (fun a => u.u₁ a y z) (fun a => u.u₂ a y z) (fun a => u.u₃ a y z) x
    (hu _ (by simp) x y z).1 (hu _ (by simp) x y z).1 (hu _ (by simp) x y z).1

theorem py_ke (x y z : ℝ) :
    py u.ke x y z = u.u₁ x y z * py u.u₁ x y z + u.u₂ x y z * py u.u₂ x y z +
      u.u₃ x y z * py u.u₃ x y z :=
  deriv_half_sq_sum (fun b => u.u₁ x b z) (fun b => u.u₂ x b z) (fun b => u.u₃ x b z) y
    (hu _ (by simp) x y z).2.1 (hu _ (by simp) x y z).2.1 (hu _ (by simp) x y z).2.1

theorem pz_ke (x y z : ℝ) :
    pz u.ke x y z = u.u₁ x y z * pz u.u₁ x y z + u.u₂ x y z * pz u.u₂ x y z +
      u.u₃ x y z * pz u.u₃ x y z :=
  deriv_half_sq_sum (fun c => u.u₁ x y c) (fun c => u.u₂ x y c) (fun c => u.u₃ x y c) z
    (hu _ (by simp) x y z).2.2 (hu _ (by simp) x y z).2.2 (hu _ (by simp) x y z).2.2

/-- Lamb identity, first component: `((u·∇)u)₁ = ∂ₓ(|u|²/2) − (u × ω)₁`. -/
theorem lamb₁ (x y z : ℝ) :
    u.adv u.u₁ x y z = px u.ke x y z -
      (u.u₂ x y z * u.curl₃ x y z - u.u₃ x y z * u.curl₂ x y z) := by
  rw [px_ke u hu]; simp only [VField.adv, VField.curl₂, VField.curl₃]; ring

theorem lamb₂ (x y z : ℝ) :
    u.adv u.u₂ x y z = py u.ke x y z -
      (u.u₃ x y z * u.curl₁ x y z - u.u₁ x y z * u.curl₃ x y z) := by
  rw [py_ke u hu]; simp only [VField.adv, VField.curl₁, VField.curl₃]; ring

theorem lamb₃ (x y z : ℝ) :
    u.adv u.u₃ x y z = pz u.ke x y z -
      (u.u₁ x y z * u.curl₂ x y z - u.u₂ x y z * u.curl₁ x y z) := by
  rw [pz_ke u hu]; simp only [VField.adv, VField.curl₁, VField.curl₂]; ring

/-- For a Beltrami field the advection is a pure gradient: `(u·∇)u = ∇(|u|²/2)`. -/
theorem beltrami_adv_grad {lam : ℝ} (hb : u.IsBeltrami lam) (x y z : ℝ) :
    u.adv u.u₁ x y z = px u.ke x y z ∧ u.adv u.u₂ x y z = py u.ke x y z ∧
      u.adv u.u₃ x y z = pz u.ke x y z := by
  obtain ⟨h1, h2, h3⟩ := hb x y z
  refine ⟨?_, ?_, ?_⟩
  · rw [lamb₁ u hu, h2, h3]; ring
  · rw [lamb₂ u hu, h1, h3]; ring
  · rw [lamb₃ u hu, h1, h2]; ring

/-- **Steady Euler.** A divergence-free Beltrami field solves steady Euler,
`(u·∇)u + ∇p = 0` and `div u = 0`, with `p = −|u|²/2`. -/
theorem beltrami_steady_euler {lam : ℝ} (hb : u.IsBeltrami lam)
    (hdiv : ∀ x y z, u.div x y z = 0) (x y z : ℝ) :
    u.div x y z = 0 ∧
    u.adv u.u₁ x y z + px (fun a b c => -u.ke a b c) x y z = 0 ∧
    u.adv u.u₂ x y z + py (fun a b c => -u.ke a b c) x y z = 0 ∧
    u.adv u.u₃ x y z + pz (fun a b c => -u.ke a b c) x y z = 0 := by
  obtain ⟨g1, g2, g3⟩ := beltrami_adv_grad u hu hb x y z
  refine ⟨hdiv x y z, ?_, ?_, ?_⟩
  · simp only [px] at g1 ⊢; rw [deriv_neg_fun, g1]; ring
  · simp only [py] at g2 ⊢; rw [deriv_neg_fun, g2]; ring
  · simp only [pz] at g3 ⊢; rw [deriv_neg_fun, g3]; ring

end Lamb

/-! ### Time-dependent Navier–Stokes -/

/-- Scaling a field by a constant. -/
def VField.smul (c : ℝ) (u : VField) : VField :=
  ⟨fun x y z => c * u.u₁ x y z, fun x y z => c * u.u₂ x y z, fun x y z => c * u.u₃ x y z⟩

theorem px_const_mul (c : ℝ) (f : SField) (x y z : ℝ) :
    px (fun a b d => c * f a b d) x y z = c * px f x y z := by
  simp only [px]; exact deriv_const_mul_field c
theorem py_const_mul (c : ℝ) (f : SField) (x y z : ℝ) :
    py (fun a b d => c * f a b d) x y z = c * py f x y z := by
  simp only [py]; exact deriv_const_mul_field c
theorem pz_const_mul (c : ℝ) (f : SField) (x y z : ℝ) :
    pz (fun a b d => c * f a b d) x y z = c * pz f x y z := by
  simp only [pz]; exact deriv_const_mul_field c

theorem lap_const_mul (c : ℝ) (f : SField) (x y z : ℝ) :
    lap (fun a b d => c * f a b d) x y z = c * lap f x y z := by
  have hx : px (fun a b d => c * f a b d) = fun a b d => c * px f a b d := by
    funext a b d; exact px_const_mul c f a b d
  have hy : py (fun a b d => c * f a b d) = fun a b d => c * py f a b d := by
    funext a b d; exact py_const_mul c f a b d
  have hz : pz (fun a b d => c * f a b d) = fun a b d => c * pz f a b d := by
    funext a b d; exact pz_const_mul c f a b d
  simp only [lap, hx, hy, hz, px_const_mul, py_const_mul, pz_const_mul]
  ring

/-- Navier–Stokes residuals of a time-dependent field `U` with pressure `P`:
`∂ₜUᵢ + (U·∇)Uᵢ + ∂ᵢP − ν ΔUᵢ`. -/
noncomputable def nsRes₁ (ν : ℝ) (U : ℝ → VField) (P : ℝ → SField) (t x y z : ℝ) : ℝ :=
  deriv (fun s => (U s).u₁ x y z) t + (U t).adv (U t).u₁ x y z + px (P t) x y z -
    ν * lap (U t).u₁ x y z
noncomputable def nsRes₂ (ν : ℝ) (U : ℝ → VField) (P : ℝ → SField) (t x y z : ℝ) : ℝ :=
  deriv (fun s => (U s).u₂ x y z) t + (U t).adv (U t).u₂ x y z + py (P t) x y z -
    ν * lap (U t).u₂ x y z
noncomputable def nsRes₃ (ν : ℝ) (U : ℝ → VField) (P : ℝ → SField) (t x y z : ℝ) : ℝ :=
  deriv (fun s => (U s).u₃ x y z) t + (U t).adv (U t).u₃ x y z + pz (P t) x y z -
    ν * lap (U t).u₃ x y z

/-- `U` with pressure `P` is an exact incompressible NS solution on ℝ⁴ = ℝₜ × ℝ³. -/
def IsNS (ν : ℝ) (U : ℝ → VField) (P : ℝ → SField) : Prop :=
  ∀ t x y z, (U t).div x y z = 0 ∧ nsRes₁ ν U P t x y z = 0 ∧
    nsRes₂ ν U P t x y z = 0 ∧ nsRes₃ ν U P t x y z = 0

theorem deriv_exp_decay (k a t : ℝ) :
    deriv (fun s => Real.exp (-k * s) * a) t = -k * (Real.exp (-k * t) * a) := by
  have H := (((hasDerivAt_id t).const_mul (-k)).exp).mul_const a
  rw [show (fun s => Real.exp (-k * s) * a) = fun s => Real.exp (-k * id s) * a from rfl,
    H.deriv]
  simp only [id]; ring

/-- **Exact NS from a Beltrami eigenfield.** Let `u` be divergence-free, Beltrami
(`curl u = λu`), with `Δuᵢ = −μ uᵢ`. Then `U(t) = e^{−νμt} u`,
`P(t) = −e^{−2νμt}|u|²/2` solves incompressible Navier–Stokes exactly on
ℝₜ × ℝ³. The nonlinear term is balanced by the pressure, and the viscous term
by the time derivative. -/
theorem beltrami_eigen_ns (u : VField) (hu : u.SlicesDiff) {lam μ ν : ℝ}
    (hb : u.IsBeltrami lam) (hdiv : ∀ x y z, u.div x y z = 0)
    (hlap : ∀ x y z, lap u.u₁ x y z = -μ * u.u₁ x y z ∧ lap u.u₂ x y z = -μ * u.u₂ x y z ∧
      lap u.u₃ x y z = -μ * u.u₃ x y z) :
    IsNS ν (fun t => u.smul (Real.exp (-(ν * μ) * t)))
      (fun t a b c => Real.exp (-(ν * μ) * t) ^ 2 * (-u.ke a b c)) := by
  intro t x y z
  obtain ⟨g1, g2, g3⟩ := beltrami_adv_grad u hu hb x y z
  obtain ⟨l1, l2, l3⟩ := hlap x y z
  have dt : ∀ f : SField, deriv (fun s => Real.exp (-(ν * μ) * s) * f x y z) t =
      -(ν * μ) * (Real.exp (-(ν * μ) * t) * f x y z) :=
    fun f => deriv_exp_decay (ν * μ) (f x y z) t
  have nx : px (fun a b c => -u.ke a b c) x y z = -px u.ke x y z := by
    simp only [px]; exact deriv_neg_fun _ _
  have ny : py (fun a b c => -u.ke a b c) x y z = -py u.ke x y z := by
    simp only [py]; exact deriv_neg_fun _ _
  have nz : pz (fun a b c => -u.ke a b c) x y z = -pz u.ke x y z := by
    simp only [pz]; exact deriv_neg_fun _ _
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp only [VField.div, VField.smul, px_const_mul, py_const_mul, pz_const_mul]
    have := hdiv x y z; simp only [VField.div] at this
    rw [← mul_add, ← mul_add, this, mul_zero]
  · simp only [nsRes₁, VField.adv, VField.smul, px_const_mul, py_const_mul, pz_const_mul,
      lap_const_mul, dt, nx, l1]
    simp only [VField.adv] at g1; rw [← g1]; ring
  · simp only [nsRes₂, VField.adv, VField.smul, px_const_mul, py_const_mul, pz_const_mul,
      lap_const_mul, dt, ny, l2]
    simp only [VField.adv] at g2; rw [← g2]; ring
  · simp only [nsRes₃, VField.adv, VField.smul, px_const_mul, py_const_mul, pz_const_mul,
      lap_const_mul, dt, nz, l3]
    simp only [VField.adv] at g3; rw [← g3]; ring

/-! ## Part B — the ABC flow -/

section ABC

variable (A B C : ℝ)

def abc₁ : SField := fun _ y z => A * sin z + C * cos y
def abc₂ : SField := fun x _ z => B * sin x + A * cos z
def abc₃ : SField := fun x y _ => C * sin y + B * cos x

/-- The Arnold–Beltrami–Childress field. -/
def abc : VField := ⟨abc₁ A C, abc₂ A B, abc₃ B C⟩

theorem d_sin_add (a k t : ℝ) : deriv (fun s => a * sin s + k) t = a * cos t :=
  (((hasDerivAt_sin t).const_mul a).add_const k).deriv
theorem d_add_cos (k a t : ℝ) : deriv (fun s => k + a * cos s) t = -(a * sin t) := by
  rw [(((hasDerivAt_cos t).const_mul a).const_add k).deriv]; ring
theorem d_cos (a t : ℝ) : deriv (fun s => a * cos s) t = -(a * sin t) := by
  rw [((hasDerivAt_cos t).const_mul a).deriv]; ring
theorem d_neg_sin (a t : ℝ) : deriv (fun s => -(a * sin s)) t = -(a * cos t) :=
  ((hasDerivAt_sin t).const_mul a).neg.deriv
theorem d_sin (a t : ℝ) : deriv (fun s => a * sin s) t = a * cos t :=
  ((hasDerivAt_sin t).const_mul a).deriv

-- first partials
theorem px_abc₁ : px (abc₁ A C) = fun _ _ _ => 0 := by
  funext x y z; simp [px, abc₁]
theorem py_abc₁ : py (abc₁ A C) = fun _ y _ => -(C * sin y) := by
  funext x y z; exact d_add_cos _ _ _
theorem pz_abc₁ : pz (abc₁ A C) = fun _ _ z => A * cos z := by
  funext x y z; exact d_sin_add _ _ _
theorem px_abc₂ : px (abc₂ A B) = fun x _ _ => B * cos x := by
  funext x y z; exact d_sin_add _ _ _
theorem py_abc₂ : py (abc₂ A B) = fun _ _ _ => 0 := by
  funext x y z; simp [py, abc₂]
theorem pz_abc₂ : pz (abc₂ A B) = fun _ _ z => -(A * sin z) := by
  funext x y z; exact d_add_cos _ _ _
theorem px_abc₃ : px (abc₃ B C) = fun x _ _ => -(B * sin x) := by
  funext x y z; exact d_add_cos _ _ _
theorem py_abc₃ : py (abc₃ B C) = fun _ y _ => C * cos y := by
  funext x y z; exact d_sin_add _ _ _
theorem pz_abc₃ : pz (abc₃ B C) = fun _ _ _ => 0 := by
  funext x y z; simp [pz, abc₃]

theorem abc_beltrami : (abc A B C).IsBeltrami 1 := by
  intro x y z
  simp only [VField.curl₁, VField.curl₂, VField.curl₃, abc, px_abc₂, px_abc₃, py_abc₁,
    py_abc₃, pz_abc₁, pz_abc₂, abc₁, abc₂, abc₃]
  refine ⟨?_, ?_, ?_⟩ <;> ring

theorem abc_div : ∀ x y z, (abc A B C).div x y z = 0 := by
  intro x y z; simp [VField.div, abc, px_abc₁, py_abc₂, pz_abc₃]

theorem abc_lap : ∀ x y z,
    lap (abc A B C).u₁ x y z = -1 * (abc A B C).u₁ x y z ∧
    lap (abc A B C).u₂ x y z = -1 * (abc A B C).u₂ x y z ∧
    lap (abc A B C).u₃ x y z = -1 * (abc A B C).u₃ x y z := by
  intro x y z
  refine ⟨?_, ?_, ?_⟩
  · simp only [lap, abc, px_abc₁, py_abc₁, pz_abc₁]
    simp only [px, py, pz, deriv_const', d_neg_sin, d_cos, abc₁]; ring
  · simp only [lap, abc, px_abc₂, py_abc₂, pz_abc₂]
    simp only [px, py, pz, deriv_const', d_neg_sin, d_cos, abc₂]; ring
  · simp only [lap, abc, px_abc₃, py_abc₃, pz_abc₃]
    simp only [px, py, pz, deriv_const', d_neg_sin, d_cos, d_sin, abc₃]; ring

theorem abc_slices : (abc A B C).SlicesDiff := by
  intro f hf x y z
  simp only [abc, List.mem_cons, List.mem_singleton, List.not_mem_nil, or_false] at hf
  rcases hf with rfl | rfl | rfl <;> simp only [abc₁, abc₂, abc₃] <;>
    refine ⟨?_, ?_, ?_⟩ <;> fun_prop

/-- **ABC is an exact global NS solution.** For every `ν, A, B, C`,
`U(t) = e^{−νt} u_ABC` with `P(t) = −e^{−2νt}|u_ABC|²/2` solves incompressible
Navier–Stokes at every `(t, x, y, z) ∈ ℝ⁴`. -/
theorem abc_ns_exact (ν : ℝ) :
    IsNS ν (fun t => (abc A B C).smul (Real.exp (-(ν * 1) * t)))
      (fun t a b c => Real.exp (-(ν * 1) * t) ^ 2 * (-(abc A B C).ke a b c)) :=
  beltrami_eigen_ns (abc A B C) (abc_slices A B C) (abc_beltrami A B C) (abc_div A B C)
    (abc_lap A B C)

/-- The ABC field is `2π`-periodic in each variable, so it descends to `T³`. -/
theorem abc_periodic (x y z : ℝ) :
    (abc A B C).u₁ (x + 2 * π) y z = (abc A B C).u₁ x y z ∧
    (abc A B C).u₁ x (y + 2 * π) z = (abc A B C).u₁ x y z ∧
    (abc A B C).u₁ x y (z + 2 * π) = (abc A B C).u₁ x y z ∧
    (abc A B C).u₂ (x + 2 * π) y z = (abc A B C).u₂ x y z ∧
    (abc A B C).u₂ x (y + 2 * π) z = (abc A B C).u₂ x y z ∧
    (abc A B C).u₂ x y (z + 2 * π) = (abc A B C).u₂ x y z ∧
    (abc A B C).u₃ (x + 2 * π) y z = (abc A B C).u₃ x y z ∧
    (abc A B C).u₃ x (y + 2 * π) z = (abc A B C).u₃ x y z ∧
    (abc A B C).u₃ x y (z + 2 * π) = (abc A B C).u₃ x y z := by
  simp [abc, abc₁, abc₂, abc₃, sin_add_two_pi, cos_add_two_pi]

/-- Non-vacuity: the ABC field with `A = B = C = 1` is not identically zero. -/
theorem abc_nonzero : (abc 1 1 1).u₁ 0 0 0 = 1 := by simp [abc, abc₁]

end ABC

/-! ## Part C — the metric Lie algebra `(sl₂(ℝ), diag(1,1,s²))` -/

/-- `X = H/2` (geodesic flow), `Y = (E+F)/2`, `V = (E−F)/2` (fibre rotation). -/
def Xm : Matrix (Fin 2) (Fin 2) ℝ := !![1/2, 0; 0, -1/2]
def Ym : Matrix (Fin 2) (Fin 2) ℝ := !![0, 1/2; 1/2, 0]
def Vm : Matrix (Fin 2) (Fin 2) ℝ := !![0, 1/2; -1/2, 0]

theorem sl2_brackets :
    Xm * Ym - Ym * Xm = Vm ∧ Xm * Vm - Vm * Xm = Ym ∧ Ym * Vm - Vm * Ym = -Xm := by
  refine ⟨?_, ?_, ?_⟩ <;> ext i j <;> fin_cases i <;> fin_cases j <;>
    simp [Xm, Ym, Vm, Matrix.mul_apply, Fin.sum_univ_two] <;> norm_num

/-- Coefficients `(a, b, c)` of `aX + bY + cV`. -/
@[ext] structure L3 where
  a : ℝ
  b : ℝ
  c : ℝ

namespace L3

def toMat (u : L3) : Matrix (Fin 2) (Fin 2) ℝ := u.a • Xm + u.b • Ym + u.c • Vm

def add (u v : L3) : L3 := ⟨u.a + v.a, u.b + v.b, u.c + v.c⟩
def sub (u v : L3) : L3 := ⟨u.a - v.a, u.b - v.b, u.c - v.c⟩
def smul (k : ℝ) (u : L3) : L3 := ⟨k * u.a, k * u.b, k * u.c⟩

/-- Lie bracket in the basis `(X, Y, V)`. -/
def br (u v : L3) : L3 := ⟨-(u.b * v.c - u.c * v.b), u.a * v.c - u.c * v.a, u.a * v.b - u.b * v.a⟩

/-- `br` is the matrix commutator, so the coefficient bracket is the bracket of `sl₂`. -/
theorem toMat_br (u v : L3) : (br u v).toMat = u.toMat * v.toMat - v.toMat * u.toMat := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [toMat, br, Xm, Ym, Vm, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

def eX : L3 := ⟨1, 0, 0⟩
def eY : L3 := ⟨0, 1, 0⟩
def eV : L3 := ⟨0, 0, 1⟩

variable (s : ℝ)

/-- Left-invariant metric: `X, Y` orthonormal, `|V| = s`, all orthogonal. -/
def g (u v : L3) : ℝ := u.a * v.a + u.b * v.b + s ^ 2 * u.c * v.c

/-- Koszul expression `⟨∇_u v, w⟩` for left-invariant fields. -/
noncomputable def K (u v w : L3) : ℝ := (g s (br u v) w - g s (br v w) u + g s (br w u) v) / 2

/-- Levi-Civita connection on left-invariant fields, solved from Koszul. -/
noncomputable def nab (u v : L3) : L3 := ⟨K s u v eX, K s u v eY, K s u v eV / s ^ 2⟩

/-- Orthonormal frame `e₁ = X, e₂ = Y, e₃ = V/s`. -/
noncomputable def e3 : L3 := ⟨0, 0, 1 / s⟩

/-- Curvature `R(u,v)w = ∇_u∇_v w − ∇_v∇_u w − ∇_{[u,v]} w`. -/
noncomputable def curv (u v w : L3) : L3 :=
  sub (sub (nab s u (nab s v w)) (nab s v (nab s u w))) (nab s (br u v) w)

/-- Ricci operator `Ric(z) = Σᵢ R(z, eᵢ) eᵢ`. -/
noncomputable def ric (z : L3) : L3 :=
  add (add (curv s z eX eX) (curv s z eY eY)) (curv s z (e3 s) (e3 s))

/-- Rough Laplacian `∇*∇ z = −Σᵢ (∇_{eᵢ}∇_{eᵢ} z − ∇_{∇_{eᵢ}eᵢ} z)` on left-invariant `z`. -/
noncomputable def rough (z : L3) : L3 :=
  smul (-1) (add (add
    (sub (nab s eX (nab s eX z)) (nab s (nab s eX eX) z))
    (sub (nab s eY (nab s eY z)) (nab s (nab s eY eY) z)))
    (sub (nab s (e3 s) (nab s (e3 s) z)) (nab s (nab s (e3 s) (e3 s)) z)))

/-- `curl z` for left-invariant `z`: `(curl z)♭ = ⋆ d z♭` with `d z♭(u,v) = −g(z,[u,v])`.
Its frame components are `(dz♭(e₂,e₃), dz♭(e₃,e₁), dz♭(e₁,e₂))`, for orientation
`(X, Y, V)`. -/
noncomputable def curl (z : L3) : L3 :=
  ⟨-g s z (br eY (e3 s)), -g s z (br (e3 s) eX), -g s z (br eX eY) / s⟩

variable {s}

theorem nab_torsion_free (hs : s ≠ 0) (u v : L3) : sub (nab s u v) (nab s v u) = br u v := by
  ext <;> simp only [sub, nab, K, g, br, eX, eY, eV] <;> field_simp <;> ring

theorem nab_metric (hs : s ≠ 0) (u v w : L3) :
    g s (nab s u v) w + g s v (nab s u w) = 0 := by
  simp only [nab, K, g, br, eX, eY, eV]; field_simp; ring

/-- `V` is Killing: `ad_V` is skew for `g`, so right translations by `exp(tV)`
are isometries. -/
theorem V_killing (u v : L3) : g s (br eV u) v + g s u (br eV v) = 0 := by
  simp [g, br, eV]; ring

/-- Non-vacuity of `V_killing`: `ad_X` is never skew (the defect is `1 + s²`),
so the left-invariant field `X` is not Killing and the property is specific
to `V`. -/
theorem X_not_killing : g s (br eX eY) eV + g s eY (br eX eV) ≠ 0 := by
  simp only [g, br, eX, eY, eV]; nlinarith [sq_nonneg s]

/-- Closed form of the Koszul connection (the `/s²` cancels). -/
theorem nab_eq (hs : s ≠ 0) (u v : L3) :
    nab s u v = ⟨v.b * u.c * s ^ 2 / 2 + v.b * u.c + v.c * u.b * s ^ 2 / 2,
      -(v.a * u.c * s ^ 2 / 2) - v.a * u.c - v.c * u.a * s ^ 2 / 2,
      (v.b * u.a - v.a * u.b) / 2⟩ := by
  ext <;> simp only [nab, K, g, br, eX, eY, eV] <;> field_simp <;> ring

theorem nab_VV (hs : s ≠ 0) : nab s eV eV = ⟨0, 0, 0⟩ := by
  ext <;> simp only [nab, K, g, br, eX, eY, eV] <;> field_simp <;> ring

/-- **Beltrami.** `curl V = −s V`. -/
theorem curl_V (hs : s ≠ 0) : curl s eV = smul (-s) eV := by
  ext <;> simp only [curl, g, br, eX, eY, eV, e3, smul] <;> field_simp <;> ring

theorem curl_curl_V (hs : s ≠ 0) : curl s (curl s eV) = smul (s ^ 2) eV := by
  rw [curl_V hs]; ext <;> simp only [curl, g, br, eX, eY, eV, e3, smul] <;> field_simp <;> ring

theorem ric_V (hs : s ≠ 0) : ric s eV = smul (s ^ 2 / 2) eV := by
  ext <;> simp only [ric, curv, add, sub, nab_eq hs, br, eX, eY, eV, e3, smul] <;>
    field_simp <;> ring

/-- Ricci on `X` (Milnor: `2μ₂μ₃ = −1 − s²/2`). -/
theorem ric_X (hs : s ≠ 0) : ric s eX = smul (-1 - s ^ 2 / 2) eX := by
  ext <;> simp only [ric, curv, add, sub, nab_eq hs, br, eX, eY, eV, e3, smul] <;>
    field_simp <;> ring

theorem rough_V (hs : s ≠ 0) : rough s eV = smul (s ^ 2 / 2) eV := by
  ext <;> simp only [rough, add, sub, nab_eq hs, br, eX, eY, eV, e3, smul] <;>
    field_simp <;> ring

/-- **Weitzenböck check on `V`.** `∇*∇V + Ric V = curl curl V`. The Hodge
Laplacian of the divergence-free field `V` equals rough plus Ricci. -/
theorem weitzenbock_V (hs : s ≠ 0) : add (rough s eV) (ric s eV) = curl s (curl s eV) := by
  rw [rough_V hs, ric_V hs, curl_curl_V hs]; ext <;> simp only [add, smul, eV] <;> ring

/-- **Deformation Laplacian kills V.** `Δ_H V − 2 Ric V = 0`: under the
Ebin–Marsden / Taylor convention `ν·2 div Def u`, the viscous term on `V`
vanishes. -/
theorem deformation_V (hs : s ≠ 0) : sub (curl s (curl s eV)) (smul 2 (ric s eV)) = ⟨0, 0, 0⟩ := by
  rw [curl_curl_V hs, ric_V hs]; ext <;> simp only [sub, smul, eV] <;> ring

end L3

end

end QOU.FluidDynamics.BeltramiSteadyEuler
