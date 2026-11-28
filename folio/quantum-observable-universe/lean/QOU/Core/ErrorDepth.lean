import QOU.Core.ErrorFiltration
import QOU.BringsSurface.DominationSqueeze
import QOU.Core.MassInRing

/-!
# QOU.Core.ErrorDepth — error order, the squeeze and the jet valuation are one object

Companion to `QOU.Core.ErrorFiltration`. Three error notions in the corpus are
instances of a single construction:

* the **error filtration** of `QOU.Core.ErrorFiltration` ("`x − y ∈ F n`", the adic
  instance of the cut core);
* the **squeeze** of `QOU.BringsSurface.DominationSqueeze` (a valuation `val` with the
  ultrametric bound; a strictly dominant term cannot be cancelled);
* the **jet valuation** `jetVal` (order of vanishing of a coefficient sequence).

The depth core (`AddFiltration`, `depth`, the jet tower) lives in
`QOU.Core.FiltrationDepth`, below the squeeze. This file adds the bridges.

The construction: an antitone tower of additive subgroups `F 0 = ⊤ ⊇ F 1 ⊇ …` has a
**depth** `depth x = sup {n | x ∈ F n} ∈ ℕ ∪ {⊤}`, characterised by
`n ≤ depth x ↔ x ∈ F n` (`coe_le_depth_iff`). The depth is a `Domination`
(`toDomination`), so the squeeze lemmas apply to any filtered error.

* For an error filtration, "agree to order `n`" is `n ≤ depth (x − y)`
  (`near_iff_le_depth`), and depth is super-additive under products
  (`le_depth_mul`).
* The jet valuation is the depth of the "vanishing below `n`" tower
  (`jetFiltration_depth`), so `jetDomination` is this construction
  (`jetDomination_val_eq`); `jetDomination`'s axioms are now proved from the depth
  axioms.
* Ring maps respecting levels are near-system maps (`nearMap`, the specialisation of
  `MassInRing.ringHomNearMap`) and do not decrease depth (`depth_le_depth_map`).
* Squeeze for errors (`depth_add_of_lt`): a term of exact depth `d` plus an error of
  order `n > d` has depth `d` and is non-zero.

No `sorry`, no axiom beyond Lean's three, no empirical value.
-/

namespace QOU.Core.Error

open QOU.AlgebraicSubstrate

namespace AddFiltration

variable {A : Type*} [AddCommGroup A] (E : AddFiltration A)

/-- **Every filtration is a domination structure.** The squeeze lemmas of
`DominationSqueeze` (`val_add_eq_of_lt`, `add_ne_zero_of_val_lt`, …) apply to the
depth of any filtered error. -/
noncomputable def toDomination : Domination A ℕ where
  val := E.depth
  val_zero := E.depth_zero
  val_neg := E.depth_neg
  le_val_add := E.min_depth_le_depth_add

/-- **Squeeze for errors.** A term of exact depth `d` perturbed by an error of order
`n > d` keeps depth `d` and cannot vanish. -/
theorem depth_add_of_lt {x e : A} {d n : ℕ} (hx : E.depth x = (d : WithTop ℕ)) (he : e ∈ E.F n)
    (hdn : d < n) : E.depth (x + e) = d ∧ x + e ≠ 0 := by
  have hlt : E.toDomination.val x < E.toDomination.val e := by
    show E.depth x < E.depth e
    rw [hx]
    exact lt_of_lt_of_le (WithTop.coe_lt_coe.mpr hdn) (E.coe_le_depth_iff.mpr he)
  exact ⟨(E.toDomination.val_add_eq_of_lt hlt).trans hx,
    E.toDomination.add_ne_zero_of_val_lt hlt⟩

end AddFiltration

/-! ### Error filtrations -/

namespace ErrorFiltration

variable {R : Type*} [CommRing R] (E : ErrorFiltration R)

/-- The additive tower underlying an error filtration. -/
def toAddFiltration : AddFiltration R where
  F n := (E.F n).toAddSubgroup
  anti _ _ h _ hx := E.anti h hx
  zero_top := by ext x; simp [E.zero_top]

/-- Error depth: the order to which `x` vanishes. -/
noncomputable def depth (x : R) : WithTop ℕ := E.toAddFiltration.depth x

theorem coe_le_depth_iff {x : R} {n : ℕ} : (n : WithTop ℕ) ≤ E.depth x ↔ x ∈ E.F n :=
  E.toAddFiltration.coe_le_depth_iff

/-- "Agree to order `n`" is "the difference has depth at least `n`". -/
theorem near_iff_le_depth {n : ℕ} {x y : R} :
    E.near.near ⟨n⟩ x y ↔ (n : WithTop ℕ) ≤ E.depth (x - y) :=
  (E.coe_le_depth_iff).symm

/-- **Depth is super-additive under products**: orders of errors add. -/
theorem le_depth_mul (x y : R) : E.depth x + E.depth y ≤ E.depth (x * y) := by
  induction hx : E.depth x using WithTop.recTopCoe with
  | top =>
    rw [top_add]
    refine withTop_le_of_forall fun _ _ => E.coe_le_depth_iff.mpr ?_
    exact Ideal.mul_mem_right y _ (E.coe_le_depth_iff.mp (hx ▸ le_top))
  | coe a =>
    induction hy : E.depth y using WithTop.recTopCoe with
    | top =>
      rw [add_top]
      refine withTop_le_of_forall fun _ _ => E.coe_le_depth_iff.mpr ?_
      exact Ideal.mul_mem_left _ x (E.coe_le_depth_iff.mp (hy ▸ le_top))
    | coe b =>
      exact (E.coe_le_depth_iff (n := a + b)).mpr <| E.mul_mem (E.coe_le_depth_iff.mp (by rw [hx]; exact le_rfl))
        (E.coe_le_depth_iff.mp (by rw [hy]; exact le_rfl))

/-- **Ring maps between error filtrations.** A ring hom `ψ` that sends each level
into the corresponding level is a map of near systems (`MassInRing.ringHomNearMap`,
specialised) and does not decrease depth. -/
def nearMap {S : Type*} [CommRing S] (E' : ErrorFiltration S) (ψ : R →+* S)
    (h : ∀ n, E.F n ≤ Ideal.comap ψ (E'.F n)) :
    QOU.Core.MassInRing.NearMap E.near E'.near :=
  QOU.Core.MassInRing.ringHomNearMap ψ E.F E.anti E'.F E'.anti h

theorem depth_le_depth_map {S : Type*} [CommRing S] (E' : ErrorFiltration S) (ψ : R →+* S)
    (h : ∀ n, E.F n ≤ Ideal.comap ψ (E'.F n)) (x : R) : E.depth x ≤ E'.depth (ψ x) :=
  withTop_le_of_forall fun _ hn =>
    E'.coe_le_depth_iff.mpr (h _ (E.coe_le_depth_iff.mp hn))

end ErrorFiltration

/-! ### The jet valuation is a depth -/

/-- The squeeze's jet instance `jetDomination` is the depth construction on the jet
tower (`QOU.AlgebraicSubstrate.jetFiltration_depth`). -/
theorem jetDomination_val_eq (f : ℕ → ℝ) :
    jetDomination.val f = (jetFiltration ℝ).toDomination.val f :=
  (jetFiltration_depth f).symm

end QOU.Core.Error
