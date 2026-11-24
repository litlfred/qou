/-
  The collision-as-gradient flow, made precise on the multiplier side.

  Setting (issue #7895).  Finitely many candidate words `i : ι`, each with a
  cost `c i` and a channel vector `x i : Fin m → ℝ` (its Wedderburn block
  characters on the live channels).  The Lagrangian of the selection program
  `min c i  s.t.  x i ≥ 0` is `L(i, μ) = c i − μ ⬝ x i`, and its dual function is

      g(μ) = min_i ( c i − μ ⬝ x i ).

  Owner's picture: "the gradient gives the incidence vector".  This file proves
  the precise version.

  * `dual_concave`       — `g` is concave (a minimum of affine functions).
  * `isSupergradient`    — if word `i` attains the minimum at `μ` ("is active"),
    then `−x i`, its incidence vector, is a supergradient of `g` at `μ`.
  * `incidence_points_to_optimum` — ATTRACTION: for any `μ★`, the incidence
    vector of every active word satisfies `(μ★ − μ) ⬝ (−x i) ≥ g μ★ − g μ`.
    If `μ★` maximises `g` and `μ` does not, the force points strictly towards it.
  * `step_shrinks_distance` — one step `μ ↦ μ + s·(−x i)` with
    `0 < s` and `s · ‖x i‖² < 2 (g μ★ − g μ)` strictly decreases `‖μ − μ★‖²`
    (Polyak's step argument), so the flow is attracted to the optimal set.

  What this does NOT give: locality.  The attraction here is global in
  multiplier space.  A "very small neighbourhood" would need a map from
  configurations of the two exceptional divisors to `μ`, which no block defines.

  Archimedean (ℝ): real inner products and order.
-/
import Mathlib.Data.Matrix.Mul
import Mathlib.Data.Real.Basic
import Mathlib.Order.ConditionallyCompleteLattice.Finset
import Mathlib.Data.Fintype.Lattice
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Abel
import Mathlib.Topology.Algebra.Module.FiniteDimension
import Mathlib.Topology.Instances.Matrix

namespace QOU.Optimization.LagrangianCollisionFlow

open Matrix

variable {ι : Type*} [Fintype ι] [Nonempty ι] {m : ℕ}

/-- The Lagrangian dual function `g(μ) = min_i (c i − μ ⬝ x i)`. -/
noncomputable def dual (c : ι → ℝ) (x : ι → Fin m → ℝ) (μ : Fin m → ℝ) : ℝ :=
  Finset.univ.inf' Finset.univ_nonempty (fun i => c i - μ ⬝ᵥ x i)

/-- Word `i` is active at `μ`: it attains the minimum. -/
def Active (c : ι → ℝ) (x : ι → Fin m → ℝ) (μ : Fin m → ℝ) (i : ι) : Prop :=
  dual c x μ = c i - μ ⬝ᵥ x i

theorem dual_le (c : ι → ℝ) (x : ι → Fin m → ℝ) (μ : Fin m → ℝ) (i : ι) :
    dual c x μ ≤ c i - μ ⬝ᵥ x i :=
  Finset.inf'_le _ (Finset.mem_univ i)

/-- Some word is always active. -/
theorem exists_active (c : ι → ℝ) (x : ι → Fin m → ℝ) (μ : Fin m → ℝ) :
    ∃ i, Active c x μ i := by
  obtain ⟨i, -, hi⟩ :=
    Finset.exists_mem_eq_inf' Finset.univ_nonempty (fun i => c i - μ ⬝ᵥ x i)
  exact ⟨i, hi⟩

/-- **`g` is concave.** -/
theorem dual_concave (c : ι → ℝ) (x : ι → Fin m → ℝ) (μ ν : Fin m → ℝ)
    {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1) :
    a * dual c x μ + b * dual c x ν ≤ dual c x (a • μ + b • ν) := by
  unfold dual
  refine Finset.le_inf' _ _ (fun i _ => ?_)
  have h1 := dual_le c x μ i
  have h2 := dual_le c x ν i
  unfold dual at h1 h2
  have e : c i - (a • μ + b • ν) ⬝ᵥ x i
      = a * (c i - μ ⬝ᵥ x i) + b * (c i - ν ⬝ᵥ x i) := by
    rw [add_dotProduct, smul_dotProduct, smul_dotProduct, smul_eq_mul, smul_eq_mul]
    have : c i = a * c i + b * c i := by rw [← add_mul, hab, one_mul]
    linarith [this]
  rw [e]
  nlinarith [mul_le_mul_of_nonneg_left h1 ha, mul_le_mul_of_nonneg_left h2 hb]

/-- **The incidence vector is a supergradient.**  If `i` is active at `μ`, then
for every `ν`, `g ν ≤ g μ + (ν − μ) ⬝ (−x i)`. -/
theorem isSupergradient {c : ι → ℝ} {x : ι → Fin m → ℝ} {μ : Fin m → ℝ} {i : ι}
    (hi : Active c x μ i) (ν : Fin m → ℝ) :
    dual c x ν ≤ dual c x μ + (ν - μ) ⬝ᵥ (-x i) := by
  have h := dual_le c x ν i
  rw [hi, dotProduct_neg, sub_dotProduct]
  linarith

/-- **Attraction.**  The incidence vector of every active word points towards
any better multiplier: `(μ★ − μ) ⬝ (−x i) ≥ g μ★ − g μ`. -/
theorem incidence_points_to_optimum {c : ι → ℝ} {x : ι → Fin m → ℝ}
    {μ : Fin m → ℝ} {i : ι} (hi : Active c x μ i) (μs : Fin m → ℝ) :
    dual c x μs - dual c x μ ≤ (μs - μ) ⬝ᵥ (-x i) := by
  have := isSupergradient hi μs
  linarith

/-- Strictly, when `μ★` is strictly better than `μ`. -/
theorem incidence_points_strictly {c : ι → ℝ} {x : ι → Fin m → ℝ}
    {μ : Fin m → ℝ} {i : ι} (hi : Active c x μ i) {μs : Fin m → ℝ}
    (hbetter : dual c x μ < dual c x μs) :
    0 < (μs - μ) ⬝ᵥ (-x i) := by
  have := incidence_points_to_optimum hi μs
  linarith

/-- **One step shrinks the distance to a better point** (Polyak).  With
`d = −x i` for an active `i`, `μ' = μ + s • d`, `0 < s` and
`s · (d ⬝ d) < 2 (g μ★ − g μ)`, we get `‖μ' − μ★‖² < ‖μ − μ★‖²`. -/
theorem step_shrinks_distance {c : ι → ℝ} {x : ι → Fin m → ℝ}
    {μ : Fin m → ℝ} {i : ι} (hi : Active c x μ i) (μs : Fin m → ℝ) {s : ℝ}
    (hs : 0 < s)
    (hstep : s * ((-x i) ⬝ᵥ (-x i)) < 2 * (dual c x μs - dual c x μ)) :
    (μ + s • (-x i) - μs) ⬝ᵥ (μ + s • (-x i) - μs) < (μ - μs) ⬝ᵥ (μ - μs) := by
  set d := -x i
  set e := μ - μs
  have hrw : μ + s • d - μs = e + s • d := by
    simp only [e]; abel
  have hatt : dual c x μs - dual c x μ ≤ (μs - μ) ⬝ᵥ d :=
    incidence_points_to_optimum hi μs
  have hneg : (μs - μ) ⬝ᵥ d = -(e ⬝ᵥ d) := by
    simp only [e]
    rw [← neg_sub, neg_dotProduct]
  have hexp : (e + s • d) ⬝ᵥ (e + s • d)
      = e ⬝ᵥ e + 2 * s * (e ⬝ᵥ d) + s * s * (d ⬝ᵥ d) := by
    rw [add_dotProduct, dotProduct_add, dotProduct_add, smul_dotProduct, smul_dotProduct,
      dotProduct_smul, dotProduct_smul, smul_eq_mul, smul_eq_mul, smul_eq_mul, smul_eq_mul,
      dotProduct_comm d e]
    ring
  rw [hrw, hexp]
  have h1 : s * (2 * (e ⬝ᵥ d) + s * (d ⬝ᵥ d)) < 0 := by
    apply mul_neg_of_pos_of_neg hs
    linarith
  nlinarith

/-! ### Unobservability inside a cell

The observable outcome of the flow is the selected word, i.e. the active one.
Where a word is the *unique* active word, it stays the unique active word on a
whole open neighbourhood: the multiplier can move without any observable change.
Observable events (a change of selected word, the knot step) can only happen on
the walls where two words tie.  This is the precise form of "non-directly-
observable behaviour before the collision". -/

/-- The cell where word `i` is the unique active word. -/
def cell (c : ι → ℝ) (x : ι → Fin m → ℝ) (i : ι) : Set (Fin m → ℝ) :=
  {ν | ∀ j, j ≠ i → c i - ν ⬝ᵥ x i < c j - ν ⬝ᵥ x j}

omit [Fintype ι] [Nonempty ι] in
theorem continuous_lagr (c : ι → ℝ) (x : ι → Fin m → ℝ) (j : ι) :
    Continuous (fun ν : Fin m → ℝ => c j - ν ⬝ᵥ x j) :=
  continuous_const.sub (continuous_id.dotProduct continuous_const)

omit [Nonempty ι] in
/-- **Cells are open.** -/
theorem isOpen_cell (c : ι → ℝ) (x : ι → Fin m → ℝ) (i : ι) : IsOpen (cell c x i) := by
  have : cell c x i = ⋂ j, {ν | j ≠ i → c i - ν ⬝ᵥ x i < c j - ν ⬝ᵥ x j} := by
    ext ν; simp [cell]
  rw [this]
  refine isOpen_iInter_of_finite (fun j => ?_)
  by_cases hji : j = i
  · simp [hji]
  · simpa [hji] using isOpen_lt (continuous_lagr c x i) (continuous_lagr c x j)

/-- In its cell, word `i` is active. -/
theorem active_of_mem_cell {c : ι → ℝ} {x : ι → Fin m → ℝ} {i : ι} {ν : Fin m → ℝ}
    (h : ν ∈ cell c x i) : Active c x ν i := by
  unfold Active dual
  apply le_antisymm (Finset.inf'_le _ (Finset.mem_univ i))
  refine Finset.le_inf' _ _ (fun j _ => ?_)
  by_cases hji : j = i
  · rw [hji]
  · exact (h j hji).le

/-- **The selected word is locally constant**: around any point of a cell there
is a neighbourhood on which the same word is active. -/
theorem selected_locally_constant {c : ι → ℝ} {x : ι → Fin m → ℝ} {i : ι}
    {μ : Fin m → ℝ} (h : μ ∈ cell c x i) :
    ∀ᶠ ν in nhds μ, Active c x ν i :=
  Filter.mem_of_superset ((isOpen_cell c x i).mem_nhds h)
    (fun _ hν => active_of_mem_cell hν)

end QOU.Optimization.LagrangianCollisionFlow
