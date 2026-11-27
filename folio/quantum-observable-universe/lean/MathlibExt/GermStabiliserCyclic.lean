import Mathlib.Analysis.Calculus.InverseFunctionTheorem.Deriv
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Analysis.Calculus.FDeriv.Analytic
import Mathlib.GroupTheory.SpecificGroups.Cyclic
import Mathlib.RingTheory.IntegralDomain
import Mathlib.Tactic.FieldSimp
import Mathlib.GroupTheory.SpecificGroups.Alternating
import Mathlib.Tactic.IntervalCases

/-!
# `QOU.RiemannSurface.GermStabiliserCyclic` — finite groups of germs fixing a point are cyclic

Bean `qou-m1bg` (Bring milestone M1b), parent `qou-qhcr`.

## Statement

Let `𝕜` be a complete nontrivially normed field of characteristic zero (`ℂ` is the case of
interest). A finite group `G` acts by **germs** at `0 ∈ 𝕜`: each `g` gives a map `act g`
fixing `0`, strictly differentiable at `0` with derivative `d g`, and the action laws hold
**as germs**, i.e. eventually near `0` (`GermAction`). Then

* `g ↦ d g` is a group homomorphism `G →* 𝕜` (`GermAction.derivHom`), by the chain rule;
* its kernel acts trivially near `0` (`GermAction.eventuallyEq_id_of_deriv_eq_one`);
* hence, if the germ action is **effective** (no `g ≠ 1` is the identity germ), `g ↦ d g` is
  injective and `G` is **cyclic** (`GermAction.isCyclic`).

The last step is Mathlib's `isCyclic_of_subgroup_isDomain`. The kernel step uses Cartan's
averaging linearizer instead of the power-series route sketched in the bean:

  `φ(z) = Σ_g (d g)⁻¹ · act g z`,  so `φ'(0) = |G| ≠ 0` and `φ ∘ act h = d h · φ` near `0`.

For `d h = 1` this gives `φ ∘ act h = φ` near `0`. `φ` is locally injective at `0`, by the
inverse function theorem (`HasStrictFDerivAt.eventually_left_inverse`), so `act h = id` near
`0`. No formal-power-series composition and no identity theorem are needed: strict
differentiability at the fixed point is enough. For a holomorphic germ, analyticity supplies it
(`AnalyticAt.hasStrictFDerivAt`).

## Consequence for the Riemann–Hurwitz capstone

`card_mem_of_isCyclic`: a cyclic subgroup of a group all of whose elements have order in a
set `S` has cardinality in `S`. With `S = {1,2,3,5}` (the element orders of `A₅`) or
`S = {1,…,6}` (those of `S₅`), this turns "point stabilisers are cyclic" into the hypotheses
`hstabA` / `hstabS` of `genus_eq_four_of_cellular` (PR #8365). The element-order fact for the
concrete `A₅` is `alternatingGroup_five_orderOf`.

## What is NOT proved here (stays a hypothesis)

* **The chart step.** A stabiliser of a point `p` of a Riemann surface, acting holomorphically,
  gives a `GermAction` on a chart centred at `p`. This needs Riemann surfaces as charted
  spaces with holomorphic transition maps (milestone M2). It is not in Mathlib in usable form.
* **Effectiveness on germs.** That a non-identity automorphism of a connected Riemann surface is
  not the identity near any point is the identity theorem on the surface (also M2). Here it is
  the explicit hypothesis `heff` of `GermAction.isCyclic`.

Ref: [farkas-kra1992] Farkas–Kra, *Riemann Surfaces*, §III.7.7 (stabilisers are cyclic). The
averaging linearizer is the standard proof of Cartan's linearization lemma.
-/

namespace QOU.RiemannSurface.GermStabiliserCyclic

open Filter Topology

variable {𝕜 : Type*} [NontriviallyNormedField 𝕜]

/-- A finite-group action by germs at `0` that are strictly differentiable at `0`. The action
laws hold only eventually near `0`, which is what a group of germs means. `d g` is the
derivative of `act g` at `0`. -/
structure GermAction (G : Type*) [Group G] (𝕜 : Type*) [NontriviallyNormedField 𝕜] where
  /-- The representative map of the germ of `g`. -/
  act : G → 𝕜 → 𝕜
  /-- The derivative of `act g` at `0`. -/
  d : G → 𝕜
  /-- Every germ fixes `0`. -/
  map_zero : ∀ g, act g 0 = 0
  /-- `act g` is strictly differentiable at `0` with derivative `d g`. -/
  hasStrictDerivAt : ∀ g, HasStrictDerivAt (act g) (d g) 0
  /-- The identity element is the identity germ. -/
  act_one : act 1 =ᶠ[𝓝 0] id
  /-- Composition of germs. -/
  act_mul : ∀ g h, act (g * h) =ᶠ[𝓝 0] act g ∘ act h

namespace GermAction

variable {G : Type*} [Group G] (A : GermAction G 𝕜)

/-- **Holomorphic germs.** An action by germs analytic at `0` is a `GermAction`, with `d g` the
derivative `deriv (act g) 0`. -/
noncomputable def ofAnalytic (act : G → 𝕜 → 𝕜) (map_zero : ∀ g, act g 0 = 0)
    (han : ∀ g, AnalyticAt 𝕜 (act g) 0) (act_one : act 1 =ᶠ[𝓝 0] id)
    (act_mul : ∀ g h, act (g * h) =ᶠ[𝓝 0] act g ∘ act h) : GermAction G 𝕜 where
  act := act
  d g := deriv (act g) 0
  map_zero := map_zero
  hasStrictDerivAt g := (han g).hasStrictFDerivAt.hasStrictDerivAt
  act_one := act_one
  act_mul := act_mul

/-- Chain rule: `d (g * h) = d g * d h`. -/
theorem d_mul (g h : G) : A.d (g * h) = A.d g * A.d h := by
  have hg : HasStrictDerivAt (A.act g) (A.d g) (A.act h 0) := by
    rw [A.map_zero h]; exact A.hasStrictDerivAt g
  have hcomp : HasDerivAt (A.act g ∘ A.act h) (A.d g * A.d h) 0 :=
    (hg.comp 0 (A.hasStrictDerivAt h)).hasDerivAt
  exact (A.hasStrictDerivAt (g * h)).hasDerivAt.unique
    (hcomp.congr_of_eventuallyEq (A.act_mul g h))

/-- `d 1 = 1`. -/
theorem d_one : A.d 1 = 1 :=
  (A.hasStrictDerivAt 1).hasDerivAt.unique ((hasDerivAt_id (0 : 𝕜)).congr_of_eventuallyEq A.act_one)

/-- The derivative at the fixed point is a homomorphism `G →* 𝕜`. -/
def derivHom : G →* 𝕜 where
  toFun := A.d
  map_one' := A.d_one
  map_mul' := A.d_mul

@[simp] theorem derivHom_apply (g : G) : A.derivHom g = A.d g := rfl

theorem d_ne_zero (g : G) : A.d g ≠ 0 := by
  intro h
  have := A.d_mul g g⁻¹
  rw [mul_inv_cancel, A.d_one, h, zero_mul] at this
  exact one_ne_zero this

theorem d_inv (g : G) : A.d g⁻¹ = (A.d g)⁻¹ := by
  have := A.d_mul g g⁻¹
  rw [mul_inv_cancel, A.d_one] at this
  exact (eq_inv_of_mul_eq_one_right this.symm)

section Linearizer

variable [Fintype G]

/-- Cartan's averaging linearizer `φ(z) = Σ_g (d g)⁻¹ · act g z`. -/
noncomputable def linearizer (z : 𝕜) : 𝕜 := ∑ g : G, (A.d g)⁻¹ * A.act g z

/-- `φ` is strictly differentiable at `0` with derivative `|G|`. -/
theorem linearizer_hasStrictDerivAt :
    HasStrictDerivAt A.linearizer (Fintype.card G : 𝕜) 0 := by
  have hsum : HasStrictDerivAt (∑ g : G, fun z => (A.d g)⁻¹ * A.act g z)
      (∑ g : G, (A.d g)⁻¹ * A.d g) 0 :=
    HasStrictDerivAt.sum (fun g _ => (A.hasStrictDerivAt g).const_mul _)
  have hfun : (∑ g : G, fun z => (A.d g)⁻¹ * A.act g z) = A.linearizer := by
    funext z; simp [linearizer, Finset.sum_apply]
  have hval : (∑ g : G, (A.d g)⁻¹ * A.d g) = (Fintype.card G : 𝕜) := by
    simp [inv_mul_cancel₀ (A.d_ne_zero _), Finset.card_univ]
  rw [hfun, hval] at hsum
  exact hsum

/-- **Equivariance.** `φ ∘ act h = d h · φ` near `0`. -/
theorem linearizer_comp (h : G) :
    ∀ᶠ z in 𝓝 (0 : 𝕜), A.linearizer (A.act h z) = A.d h * A.linearizer z := by
  have hall : ∀ᶠ z in 𝓝 (0 : 𝕜), ∀ g : G, A.act (g * h) z = A.act g (A.act h z) :=
    eventually_all.2 fun g => A.act_mul g h
  filter_upwards [hall] with z hz
  unfold linearizer
  rw [Finset.mul_sum]
  refine Fintype.sum_equiv (Equiv.mulRight h) _ _ (fun g => ?_)
  simp only [Equiv.coe_mulRight]
  rw [← hz g, A.d_mul, mul_inv]
  field_simp [A.d_ne_zero g, A.d_ne_zero h]

variable [CompleteSpace 𝕜] [CharZero 𝕜]

/-- **Kernel acts trivially.** A germ with derivative `1` at the fixed point is the identity
germ. -/
theorem eventuallyEq_id_of_deriv_eq_one (h : G) (hd : A.d h = 1) :
    A.act h =ᶠ[𝓝 0] id := by
  have hcard : (Fintype.card G : 𝕜) ≠ 0 := Nat.cast_ne_zero.2 Fintype.card_ne_zero
  have hφ := (A.linearizer_hasStrictDerivAt).hasStrictFDerivAt_equiv hcard
  have hinv := hφ.eventually_left_inverse
  have htend : Tendsto (A.act h) (𝓝 0) (𝓝 0) := by
    have := (A.hasStrictDerivAt h).hasDerivAt.continuousAt.tendsto
    rwa [A.map_zero h] at this
  have hinv' := htend.eventually hinv
  filter_upwards [hinv, hinv', A.linearizer_comp h] with z h1 h2 h3
  rw [hd, one_mul] at h3
  rw [id, ← h2, h3, h1]

/-- **The derivative map is injective on an effective germ action.** -/
theorem derivHom_injective (heff : ∀ g : G, A.act g =ᶠ[𝓝 0] id → g = 1) :
    Function.Injective A.derivHom := by
  rw [injective_iff_map_eq_one]
  intro g hg
  exact heff g (A.eventuallyEq_id_of_deriv_eq_one g hg)

/-- **M1b.** A finite group acting effectively by strictly differentiable germs fixing a point,
over a complete nontrivially normed field of characteristic zero, is cyclic. -/
theorem isCyclic (heff : ∀ g : G, A.act g =ᶠ[𝓝 0] id → g = 1) : IsCyclic G :=
  isCyclic_of_subgroup_isDomain A.derivHom (A.derivHom_injective heff)

end Linearizer

end GermAction

/-! ## From cyclic stabilisers to the `hstab` hypotheses -/

/-- A cyclic subgroup of `Γ` has cardinality equal to the order of some element of `Γ`. -/
theorem exists_orderOf_eq_card {Γ : Type*} [Group Γ] (H : Subgroup Γ) [Fintype H]
    [IsCyclic H] : ∃ x : Γ, orderOf x = Fintype.card H := by
  obtain ⟨y, hy⟩ := IsCyclic.exists_generator (α := H)
  refine ⟨(y : Γ), ?_⟩
  rw [Subgroup.orderOf_coe]
  rw [orderOf_eq_card_of_forall_mem_zpowers hy, Nat.card_eq_fintype_card]

/-- If every element of `Γ` has order in `S`, every cyclic subgroup has cardinality in `S`. -/
theorem card_mem_of_isCyclic {Γ : Type*} [Group Γ] (S : Set ℕ)
    (hS : ∀ x : Γ, orderOf x ∈ S) (H : Subgroup Γ) [Fintype H] [IsCyclic H] :
    Fintype.card H ∈ S := by
  obtain ⟨x, hx⟩ := exists_orderOf_eq_card H
  exact hx ▸ hS x

/-- Element orders transfer along a group isomorphism. -/
theorem orderOf_mem_of_mulEquiv {Γ Δ : Type*} [Group Γ] [Group Δ] (e : Γ ≃* Δ) (S : Set ℕ)
    (hS : ∀ y : Δ, orderOf y ∈ S) (x : Γ) : orderOf x ∈ S := by
  rw [← MulEquiv.orderOf_eq e x]; exact hS _

/-! ### Element orders of `S₅` and `A₅` (kernel `decide`) -/

set_option maxRecDepth 100000 in
/-- Every permutation of five letters satisfies `σ⁴ = 1`, `σ⁵ = 1` or `σ⁶ = 1`. -/
theorem perm_five_pow (σ : Equiv.Perm (Fin 5)) : σ ^ 4 = 1 ∨ σ ^ 5 = 1 ∨ σ ^ 6 = 1 := by
  revert σ; decide +kernel

set_option maxRecDepth 100000 in
/-- Every even permutation of five letters satisfies `σ² = 1`, `σ³ = 1` or `σ⁵ = 1`. -/
theorem even_perm_five_pow (σ : Equiv.Perm (Fin 5)) (hσ : Equiv.Perm.sign σ = 1) :
    σ ^ 2 = 1 ∨ σ ^ 3 = 1 ∨ σ ^ 5 = 1 := by
  revert σ; decide +kernel

/-- The element orders of `S₅` lie in `{1, …, 6}`. -/
theorem perm_five_orderOf (σ : Equiv.Perm (Fin 5)) :
    orderOf σ ∈ ({1, 2, 3, 4, 5, 6} : Set ℕ) := by
  rcases perm_five_pow σ with h | h | h <;>
  · have hd := orderOf_dvd_of_pow_eq_one h
    have hle := Nat.le_of_dvd (by norm_num) hd
    interval_cases (orderOf σ) <;> simp_all

/-- The element orders of `A₅` lie in `{1, 2, 3, 5}`. -/
theorem alternatingGroup_five_orderOf (σ : alternatingGroup (Fin 5)) :
    orderOf σ ∈ ({1, 2, 3, 5} : Set ℕ) := by
  rw [← Subgroup.orderOf_coe]
  rcases even_perm_five_pow σ (Equiv.Perm.mem_alternatingGroup.1 σ.2) with h | h | h <;>
  · have hd := orderOf_dvd_of_pow_eq_one h
    have hle := Nat.le_of_dvd (by norm_num) hd
    interval_cases (orderOf (σ : Equiv.Perm (Fin 5))) <;> simp_all

/-- **`hstabA` from cyclicity.** If `Γ ≅ A₅`, every cyclic subgroup of `Γ` (in particular a
point stabiliser, once M1b + the chart step make it cyclic) has order `1`, `2`, `3` or `5` —
the disjunction `hstabA` of `genus_eq_four_of_cellular`. -/
theorem card_cyclic_of_A5 {Γ : Type*} [Group Γ] (e : Γ ≃* alternatingGroup (Fin 5))
    (H : Subgroup Γ) [Fintype H] [IsCyclic H] :
    Fintype.card H = 1 ∨ Fintype.card H = 2 ∨ Fintype.card H = 3 ∨ Fintype.card H = 5 := by
  have := card_mem_of_isCyclic _ (orderOf_mem_of_mulEquiv e _ alternatingGroup_five_orderOf) H
  simpa using this

/-- **`hstabS` from cyclicity.** If `Γ ≅ S₅`, every cyclic subgroup of `Γ` has order in
`{1, …, 6}` — the disjunction `hstabS` of `genus_eq_four_of_cellular`. -/
theorem card_cyclic_of_S5 {Γ : Type*} [Group Γ] (e : Γ ≃* Equiv.Perm (Fin 5))
    (H : Subgroup Γ) [Fintype H] [IsCyclic H] :
    Fintype.card H = 1 ∨ Fintype.card H = 2 ∨ Fintype.card H = 3 ∨ Fintype.card H = 4
      ∨ Fintype.card H = 5 ∨ Fintype.card H = 6 := by
  have := card_mem_of_isCyclic _ (orderOf_mem_of_mulEquiv e _ perm_five_orderOf) H
  simpa using this

end QOU.RiemannSurface.GermStabiliserCyclic
