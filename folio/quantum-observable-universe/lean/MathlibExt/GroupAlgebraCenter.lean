import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.Algebra.Group.ConjFinite
import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.Finsupp.LinearCombination

/-!
# Counting: conjugacy classes of `S_n`, and the centre of a group algebra

Two bounds needed by the completeness half of the Specht classification
(`SpechtClassification.specht_exhausts_irreducibles`), where the chain is

  `#{simple k[Sₙ]-modules} ≤ dim_k Z(k[Sₙ]) ≤ #conj classes of Sₙ ≤ #partitions of n`.

This file supplies the two right-hand steps. Both are stated as **inequalities**,
which is what the count needs and is markedly cheaper than the equalities:

* `#conj classes ≤ #partitions` needs only that `Equiv.Perm.partition` separates
  conjugacy classes — **not** that every partition is realised as a cycle type,
  which Mathlib does not have.
* `dim_k Z(k[G]) ≤ #conj classes` needs only that the class sums **span** the
  centre — **not** that they are independent.

## Mathlib coverage

`Equiv.Perm.partition` and `partition_eq_of_isConj` exist; the induced injection
on `ConjClasses` does not. For group algebras Mathlib has no centre API at all at
the pinned revision — no class sums, no dimension formula. Both are genuine gaps.
-/

open scoped BigOperators

namespace QOU.MathlibExt.GroupAlgebraCenter

/-! ## 1. Conjugacy classes of `S_n` inject into partitions of `n` -/

section Perm

variable {α : Type*} [Fintype α] [DecidableEq α]

instance decidableIsConjPerm : DecidableRel (IsConj : Equiv.Perm α → Equiv.Perm α → Prop) :=
  fun _ _ => decidable_of_iff _ Equiv.Perm.isConj_iff_cycleType_eq.symm

/-- The cycle-type partition, as a map out of conjugacy classes. -/
def conjPartition : ConjClasses (Equiv.Perm α) → (Fintype.card α).Partition :=
  Quotient.lift Equiv.Perm.partition fun _ _ h => Equiv.Perm.partition_eq_of_isConj.mp h

theorem conjPartition_injective :
    Function.Injective (conjPartition (α := α)) := by
  refine fun a b => Quotient.inductionOn₂ a b (fun σ τ hst => ?_)
  exact Quotient.sound (Equiv.Perm.partition_eq_of_isConj.mpr hst)

/-- **Conjugacy classes of a symmetric group inject into partitions.**  Two
permutations are conjugate exactly when they have the same cycle type, so the
partition map separates classes.

Surjectivity — every partition is a cycle type — is *true* but not needed for
the count, and is not in Mathlib. -/
theorem card_conjClasses_le (α : Type*) [Fintype α] [DecidableEq α] :
    Fintype.card (ConjClasses (Equiv.Perm α)) ≤ Fintype.card ((Fintype.card α).Partition) :=
  Fintype.card_le_of_injective _ conjPartition_injective

/-- The `Fin n` case, with the cardinality reduced. -/
theorem card_conjClasses_perm_fin_le (n : ℕ) :
    Fintype.card (ConjClasses (Equiv.Perm (Fin n))) ≤ Fintype.card (n.Partition) := by
  have h := card_conjClasses_le (Fin n)
  rwa [Fintype.card_fin] at h

end Perm

/-! ## 2. The centre of a group algebra is spanned by class sums

An element of `k[G]` is central iff its coefficient function is constant on
conjugacy classes, so it is a combination of the class sums.  Only this
direction — centre ⊆ span — is proved, since only the resulting dimension
*bound* is used. -/

section Center

variable {k G : Type*} [CommRing k] [Group G] [Fintype G] [DecidableEq G]

open MonoidAlgebra

variable [DecidableRel (IsConj : G → G → Prop)]

/-- The **class sum** of a conjugacy class: the sum of its elements in `k[G]`. -/
noncomputable def classSum (c : ConjClasses G) : MonoidAlgebra k G :=
  ∑ g ∈ c.carrier.toFinset, MonoidAlgebra.single g (1 : k)

omit [Fintype G] [DecidableEq G] [DecidableRel (IsConj : G → G → Prop)] in
/-- Conjugation-invariance of the coefficients of a central element.

`z` central means `single h 1 * z = z * single h 1` for every `h`; comparing
coefficients at `h * g` gives `z g = z (h⁻¹ * g * h)`. -/
theorem coeff_conj_eq_of_mem_center {z : MonoidAlgebra k G}
    (hz : z ∈ Subalgebra.center k (MonoidAlgebra k G)) (h g : G) :
    z (h * g * h⁻¹) = z g := by
  have hcomm : MonoidAlgebra.single h (1 : k) * z = z * MonoidAlgebra.single h (1 : k) :=
    Subalgebra.mem_center_iff.mp hz _
  have hL : (MonoidAlgebra.single h (1 : k) * z) (h * g) = z g := by
    rw [MonoidAlgebra.single_mul_apply]
    simp
  have hR : (z * MonoidAlgebra.single h (1 : k)) (h * g) = z (h * g * h⁻¹) := by
    rw [MonoidAlgebra.mul_single_apply]
    simp
  rw [← hL, hcomm, hR]

omit [Fintype G] [DecidableEq G] [DecidableRel (IsConj : G → G → Prop)] in
/-- The coefficients of a central element are constant on conjugacy classes. -/
theorem coeff_eq_of_isConj {z : MonoidAlgebra k G}
    (hz : z ∈ Subalgebra.center k (MonoidAlgebra k G)) {g g' : G} (hc : IsConj g g') :
    z g' = z g := by
  obtain ⟨u, hu⟩ := hc
  have hg' : (u : G) * g * (u : G)⁻¹ = g' := by
    rw [hu.eq]; group
  rw [← hg']
  exact coeff_conj_eq_of_mem_center hz _ _

omit [DecidableEq G] in
/-- Each conjugacy class's carrier is the fibre of `ConjClasses.mk` over it. -/
theorem carrier_toFinset_eq_filter (c : ConjClasses G) :
    c.carrier.toFinset = Finset.univ.filter (fun g : G => ConjClasses.mk g = c) := by
  ext g
  simp [ConjClasses.mem_carrier_iff_mk_eq]

omit [DecidableEq G] in
/-- **The centre is contained in the span of the class sums.**

A central `z` is constant on classes, so `z = Σ_c z(cᵒᵘᵗ) · classSum c`; the
carriers partition `G`, which turns the double sum back into `Σ_g single g (z g) = z`.

Only this inclusion is proved — the class sums are in fact a *basis*, but the
counting argument needs no more than the resulting dimension bound. -/
theorem center_le_span_classSum :
    Subalgebra.toSubmodule (Subalgebra.center k (MonoidAlgebra k G))
      ≤ Submodule.span k (Set.range (classSum (k := k) (G := G))) := by
  classical
  intro z hz
  have hzc : z ∈ Subalgebra.center k (MonoidAlgebra k G) := hz
  refine (Submodule.mem_span_range_iff_exists_fun k).mpr ⟨fun c => z c.out, ?_⟩
  -- expand each class sum and replace `z cᵒᵘᵗ` by `z g` inside the class
  have hstep : ∀ c : ConjClasses G,
      (z c.out) • classSum (k := k) c
        = ∑ g ∈ Finset.univ.filter (fun g : G => ConjClasses.mk g = c),
            MonoidAlgebra.single g (z g) := by
    intro c
    rw [classSum, Finset.smul_sum, carrier_toFinset_eq_filter]
    refine Finset.sum_congr rfl (fun g hg => ?_)
    have hmk : ConjClasses.mk g = c := (Finset.mem_filter.mp hg).2
    have hconj : IsConj g c.out := by
      rw [← ConjClasses.mk_eq_mk_iff_isConj, hmk]
      exact ((ConjClasses.quotient_mk_eq_mk c.out).symm.trans (Quotient.out_eq c)).symm
    rw [MonoidAlgebra.smul_single, smul_eq_mul, mul_one, coeff_eq_of_isConj hzc hconj]
  rw [Finset.sum_congr rfl (fun c _ => hstep c)]
  -- the classes partition `G`
  rw [Finset.sum_fiberwise_of_maps_to (fun g _ => Finset.mem_univ (ConjClasses.mk g))]
  -- and `Σ_g single g (z g) = z`
  rw [← Finsupp.sum_fintype z (fun g c => MonoidAlgebra.single g c) (by simp)]
  exact Finsupp.sum_single z

end Center

section CenterField

variable {k G : Type*} [Field k] [Group G] [Fintype G] [DecidableEq G]
  [DecidableRel (IsConj : G → G → Prop)]

omit [DecidableEq G] in
/-- **`dim_k Z(k[G]) ≤ #conj classes`.**  Immediate from `center_le_span_classSum`
and `finrank_range_le_card`. -/
theorem finrank_center_le_card_conjClasses :
    Module.finrank k (Subalgebra.toSubmodule (Subalgebra.center k (MonoidAlgebra k G)))
      ≤ Fintype.card (ConjClasses G) := by
  classical
  haveI : Module.Finite k (MonoidAlgebra k G) := by
    unfold MonoidAlgebra; infer_instance
  exact (Submodule.finrank_mono center_le_span_classSum).trans
    (finrank_range_le_card _)

end CenterField

/-! ## 3. Class functions

A function `G → k` constant on conjugacy classes is determined by its values on
`ConjClasses G`, so the space of them has dimension at most the number of
classes.  This is the target the characters of pairwise non-isomorphic simple
modules land in, and the reason `#simples ≤ #conj classes`. -/

section ClassFunctions

variable (k G : Type*) [CommRing k] [Group G]

/-- The **class functions** `G → k`: those constant on conjugacy classes. -/
def classFunctions : Submodule k (G → k) where
  carrier := {f | ∀ g h : G, f (h * g * h⁻¹) = f g}
  zero_mem' := by intro _ _; rfl
  add_mem' hf hg := by intro x h; simp only [Pi.add_apply, hf x h, hg x h]
  smul_mem' c f hf := by intro x h; simp only [Pi.smul_apply, hf x h]

variable {k G}

theorem mem_classFunctions {f : G → k} :
    f ∈ classFunctions k G ↔ ∀ g h : G, f (h * g * h⁻¹) = f g := Iff.rfl

/-- A class function takes the same value on conjugate elements. -/
theorem classFunctions_apply_of_isConj {f : G → k} (hf : f ∈ classFunctions k G)
    {g g' : G} (hc : IsConj g g') : f g' = f g := by
  obtain ⟨u, hu⟩ := hc
  have hg' : (u : G) * g * (u : G)⁻¹ = g' := by rw [hu.eq]; group
  rw [← hg']
  exact hf g u

variable [Fintype G] [DecidableRel (IsConj : G → G → Prop)]

/-- Restriction of a class function to conjugacy classes. -/
noncomputable def onClasses : classFunctions k G →ₗ[k] (ConjClasses G → k) where
  toFun f := fun c => (f : G → k) c.out
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

omit [Fintype G] [DecidableRel (IsConj : G → G → Prop)] in
theorem onClasses_injective : Function.Injective (onClasses (k := k) (G := G)) := by
  intro f₁ f₂ hf
  refine Subtype.ext (funext (fun g => ?_))
  have hcls := congrFun hf (ConjClasses.mk g)
  have hconj : IsConj g (ConjClasses.mk g).out := by
    rw [← ConjClasses.mk_eq_mk_iff_isConj]
    exact ((ConjClasses.quotient_mk_eq_mk _).symm.trans
      (Quotient.out_eq (ConjClasses.mk g))).symm
  rw [← classFunctions_apply_of_isConj f₁.2 hconj,
    ← classFunctions_apply_of_isConj f₂.2 hconj]
  exact hcls

end ClassFunctions

section ClassFunctionsField

variable {k G : Type*} [Field k] [Group G] [Fintype G]
  [DecidableRel (IsConj : G → G → Prop)]

/-- **`dim_k {class functions} ≤ #conj classes`.**  A class function is
determined by its values on classes. -/
theorem finrank_classFunctions_le :
    Module.finrank k (classFunctions k G) ≤ Fintype.card (ConjClasses G) := by
  classical
  haveI : Module.Finite k (G → k) := Module.Finite.pi
  have h := LinearMap.finrank_le_finrank_of_injective
    (f := onClasses (k := k) (G := G)) onClasses_injective
  rw [Module.finrank_fintype_fun_eq_card] at h
  exact h

end ClassFunctionsField

end QOU.MathlibExt.GroupAlgebraCenter
