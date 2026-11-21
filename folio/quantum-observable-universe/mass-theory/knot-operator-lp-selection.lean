/-
  Knot-operator LP selection via the Frobenius Gram pseudo-inverse.

  Companion: knot-operator-lp-selection.md
  Path: folio/quantum-observable-universe/mass-theory/

  The block's LP (primal, MINIMISED):

      min  Σ_o t(o) x(o)   s.t.   x ≥ 0,   (G⁺ S) x ≥ n_T

  with `G` the Frobenius Gram matrix on a basis `{b_i}` of `H_n(q)` and
  `G⁺` its Moore–Penrose pseudo-inverse, i.e. the inverse of the trace form
  on the quotient `H_n(q)/rad` (`IsMoorePenrose`, carried as a field of the
  LP data; in code `pyhecke.gram.G_PINV` / `gram_quotient_inverse`). When
  `det G` is a unit, `G⁺ = G⁻¹` (`gramPinv_eq_inv_of_isUnit_det`);
  `S` the supply matrix (column `o` = NF profile of knot operator `o`),
  `t` the crossing energies, `n_T` the demand of target `T`. The dual is

      max  Σ_i n_T(i) y(i)   s.t.   y ≥ 0,   (G⁺ S)ᵀ y ≤ t.

  PROVED here, sorry-free, over any ordered commutative ring `R` (§7c):
  * `weak_duality`: every dual-feasible `y` bounds every primal-feasible `x`;
  * `optimal_of_objectives_eq`: a primal/dual pair with equal objectives is
    a certificate — `x` is optimal (minimal) and `y` is dual-optimal;
  * `complementary_slackness`: for such a pair, `y(i) · slack_i = 0` and
    `x(o) · reduced-cost_o = 0`, i.e. a constraint with nonzero shadow
    price is tight and an operator in the support has zero reduced cost
    (the "active set");
  * `knot_operator_lp_selection` bundles the three;
  * `gramPinv_eq_inv_of_isUnit_det`: on a non-degenerate Gram matrix the
    pseudo-inverse is the inverse.

  The LP lemmas use nothing about `G⁺` beyond `M = G⁺ S`; the pseudo-inverse
  property fixes which matrix `M` is built from.

  NOT proved here: strong duality (that an optimal pair with equal
  objectives EXISTS whenever the primal is feasible and bounded). Mathlib
  at this pin has no finite-dimensional LP-duality theorem; the statement
  is therefore conditional on the certificate, and says so in its name of
  hypotheses. Ref: [schrijver1986theory] §7.2 (strong duality), §7.4
  (complementary slackness).

  RETIRED (QA re-adjudication 2026-11-20): the previous Lean `Optimal`
  MAXIMISED the objective and dropped the Gram factor, contradicting the .md, and
  its class `KnotOperatorLPSelection` was uninhabitable — at `n_T = 0`
  strong duality forces the zero selection to be optimal, and
  complementary slackness then demands its empty support be a singleton.
  That is proved below as `KnotOperatorLPSelectionLegacy.isEmpty`; the
  theorem it carried was therefore vacuous.
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.LinearAlgebra.BilinearForm.Properties
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Data.Fintype.Basic

namespace QOU.BraidsAndKnots

open Finset

/-! ### The block's LP (minimisation with `G⁺ S`) -/

/-- `P` is the Moore–Penrose pseudo-inverse of `G` (the four Penrose
    conditions, with transpose as the adjoint). For a symmetric Gram matrix
    with radical, this is the inverse of the form on the quotient by the
    radical, extended by `0`. -/
def IsMoorePenrose {R : Type*} [CommRing R] {n : Type*} [Fintype n]
    (G P : Matrix n n R) : Prop :=
  G * P * G = G ∧ P * G * P = P ∧
    Matrix.transpose (G * P) = G * P ∧ Matrix.transpose (P * G) = P * G

/-- On a non-degenerate matrix (`det G` a unit), any matrix satisfying the
    first Penrose condition is the inverse. -/
theorem eq_inv_of_mul_mul_eq {R : Type*} [CommRing R] {n : Type*} [Fintype n]
    [DecidableEq n] {G P : Matrix n n R} (hG : IsUnit G.det) (h : G * P * G = G) :
    P = G⁻¹ := by
  calc P = (G⁻¹ * G) * P * (G * G⁻¹) := by
        rw [Matrix.nonsing_inv_mul _ hG, Matrix.mul_nonsing_inv _ hG, Matrix.one_mul,
          Matrix.mul_one]
    _ = G⁻¹ * (G * P * G) * G⁻¹ := by simp only [Matrix.mul_assoc]
    _ = G⁻¹ := by rw [h, Matrix.nonsing_inv_mul _ hG, Matrix.one_mul]

/-- LP data for knot-operator selection in an `R`-algebra `H`: a finite
    operator set `Op`, a finite Frobenius basis `Basis`, the Gram matrix,
    the supply matrix and the crossing energies. -/
structure KnotOperatorLP (R : Type*) [CommRing R]
    (H : Type*) [Ring H] [Algebra R H]
    (Op Basis : Type*) [Fintype Op] [Fintype Basis] [DecidableEq Basis] where
  /-- Each operator's image in `H` (the braid word as a Hecke element). -/
  toH : Op → H
  /-- Frobenius Gram matrix `G_{ij} = tr(b_i b_j)` on the basis. -/
  gram : Matrix Basis Basis R
  /-- The pseudo-inverse `G⁺` (the inverse on `H_n(q)/rad`). -/
  gramPinv : Matrix Basis Basis R
  /-- `G⁺` is the Moore–Penrose pseudo-inverse of `G`. -/
  gramPinv_spec : IsMoorePenrose gram gramPinv
  /-- Supply matrix: column `o` is the NF profile of operator `o`. -/
  supply : Matrix Basis Op R
  /-- Crossing-energy cost `t(o)` of each operator. -/
  cost : Op → R

namespace KnotOperatorLP

variable {R : Type*} [CommRing R] [PartialOrder R] [IsOrderedRing R]
  {H : Type*} [Ring H] [Algebra R H]
  {Op Basis : Type*} [Fintype Op] [Fintype Basis] [DecidableEq Basis]
  (lp : KnotOperatorLP R H Op Basis)

/-- The constraint matrix `M = G⁺ S`. Under convention D the Frobenius Gram
    matrix on `H_3(q)` has a radical (see `prop:knot-operator-selection`'s
    notes), so `G⁻¹` does not exist and `G⁺` is the inverse on the quotient. -/
def M : Matrix Basis Op R := lp.gramPinv * lp.supply

omit [PartialOrder R] [IsOrderedRing R] in
/-- On a non-degenerate Gram matrix the pseudo-inverse is the inverse, so the
    constraint matrix is `G⁻¹ S`. -/
theorem gramPinv_eq_inv_of_isUnit_det (hG : IsUnit lp.gram.det) :
    lp.gramPinv = lp.gram⁻¹ :=
  eq_inv_of_mul_mul_eq hG lp.gramPinv_spec.1

/-- Primal objective `Σ_o t(o) x(o)`. -/
def primalObj (x : Op → R) : R := ∑ o, lp.cost o * x o

/-- Dual objective `Σ_i n_T(i) y(i)` (independent of the LP data except
    through the index type; `lp` is taken explicitly for field notation). -/
@[nolint unusedArguments]
def dualObj (_lp : KnotOperatorLP R H Op Basis) (n_T : Basis → R) (y : Basis → R) : R :=
  ∑ i, n_T i * y i

/-- `(G⁺ S x)_i`. -/
def supplyOf (x : Op → R) (i : Basis) : R := ∑ o, lp.M i o * x o

/-- `((G⁺ S)ᵀ y)_o`. -/
def priceOf (y : Basis → R) (o : Op) : R := ∑ i, y i * lp.M i o

/-- Primal feasibility: `x ≥ 0` and `G⁺ S x ≥ n_T`. -/
def Feasible (n_T : Basis → R) (x : Op → R) : Prop :=
  (∀ o, 0 ≤ x o) ∧ ∀ i, n_T i ≤ lp.supplyOf x i

/-- Primal optimality (MINIMISATION, as in the .md). -/
def Optimal (n_T : Basis → R) (x : Op → R) : Prop :=
  lp.Feasible n_T x ∧ ∀ x', lp.Feasible n_T x' → lp.primalObj x ≤ lp.primalObj x'

/-- Dual feasibility: `y ≥ 0` and `(G⁺ S)ᵀ y ≤ t`. -/
def DualFeasible (y : Basis → R) : Prop :=
  (∀ i, 0 ≤ y i) ∧ ∀ o, lp.priceOf y o ≤ lp.cost o

/-- Dual optimality (maximisation). -/
def DualOptimal (n_T : Basis → R) (y : Basis → R) : Prop :=
  lp.DualFeasible y ∧ ∀ y', lp.DualFeasible y' → lp.dualObj n_T y' ≤ lp.dualObj n_T y

omit [PartialOrder R] [IsOrderedRing R] in
/-- The duality-gap identity:
    `t·x − n·y = Σ_i y_i ((Mx)_i − n_i) + Σ_o x_o (t_o − (Mᵀy)_o)`. -/
theorem gap_eq (n_T : Basis → R) (x : Op → R) (y : Basis → R) :
    lp.primalObj x - lp.dualObj n_T y =
      (∑ i, y i * (lp.supplyOf x i - n_T i)) +
      ∑ o, x o * (lp.cost o - lp.priceOf y o) := by
  have hswap : ∑ i, y i * lp.supplyOf x i = ∑ o, x o * lp.priceOf y o := by
    simp only [supplyOf, priceOf, Finset.mul_sum]
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun o _ => Finset.sum_congr rfl fun i _ => ?_
    ring
  simp only [primalObj, dualObj, mul_sub, Finset.sum_sub_distrib]
  rw [hswap]
  have hc : ∑ o, lp.cost o * x o = ∑ o, x o * lp.cost o :=
    Finset.sum_congr rfl fun o _ => mul_comm _ _
  have hn : ∑ i, n_T i * y i = ∑ i, y i * n_T i :=
    Finset.sum_congr rfl fun i _ => mul_comm _ _
  rw [hc, hn]
  ring

theorem gap_terms_nonneg {n_T : Basis → R} {x : Op → R} {y : Basis → R}
    (hx : lp.Feasible n_T x) (hy : lp.DualFeasible y) :
    (0 ≤ ∑ i, y i * (lp.supplyOf x i - n_T i)) ∧
      0 ≤ ∑ o, x o * (lp.cost o - lp.priceOf y o) :=
  ⟨Finset.sum_nonneg fun i _ => mul_nonneg (hy.1 i) (sub_nonneg.2 (hx.2 i)),
   Finset.sum_nonneg fun o _ => mul_nonneg (hx.1 o) (sub_nonneg.2 (hy.2 o))⟩

/-- **Weak duality.** -/
theorem weak_duality {n_T : Basis → R} {x : Op → R} {y : Basis → R}
    (hx : lp.Feasible n_T x) (hy : lp.DualFeasible y) :
    lp.dualObj n_T y ≤ lp.primalObj x := by
  have h := lp.gap_eq n_T x y
  obtain ⟨h1, h2⟩ := lp.gap_terms_nonneg hx hy
  exact sub_nonneg.1 (h ▸ add_nonneg h1 h2)

/-- **Optimality certificate.** A feasible primal/dual pair with equal
    objectives is optimal on both sides. -/
theorem optimal_of_objectives_eq {n_T : Basis → R} {x : Op → R} {y : Basis → R}
    (hx : lp.Feasible n_T x) (hy : lp.DualFeasible y)
    (heq : lp.primalObj x = lp.dualObj n_T y) :
    lp.Optimal n_T x ∧ lp.DualOptimal n_T y :=
  ⟨⟨hx, fun _ hx' => heq ▸ lp.weak_duality hx' hy⟩,
   ⟨hy, fun _ hy' => heq ▸ lp.weak_duality hx hy'⟩⟩

/-- **Complementary slackness.** For a feasible pair with equal objectives,
    every shadow price times its slack vanishes, and every operator weight
    times its reduced cost vanishes. -/
theorem complementary_slackness {n_T : Basis → R} {x : Op → R} {y : Basis → R}
    (hx : lp.Feasible n_T x) (hy : lp.DualFeasible y)
    (heq : lp.primalObj x = lp.dualObj n_T y) :
    (∀ i, y i * (lp.supplyOf x i - n_T i) = 0) ∧
      ∀ o, x o * (lp.cost o - lp.priceOf y o) = 0 := by
  have h := lp.gap_eq n_T x y
  rw [heq, sub_self] at h
  obtain ⟨h1, h2⟩ := lp.gap_terms_nonneg hx hy
  obtain ⟨hA, hB⟩ := (add_eq_zero_iff_of_nonneg h1 h2).1 h.symm
  refine ⟨fun i => ?_, fun o => ?_⟩
  · exact (Finset.sum_eq_zero_iff_of_nonneg
      (fun i _ => mul_nonneg (hy.1 i) (sub_nonneg.2 (hx.2 i)))).1 hA i
      (Finset.mem_univ i)
  · exact (Finset.sum_eq_zero_iff_of_nonneg
      (fun o _ => mul_nonneg (hx.1 o) (sub_nonneg.2 (hy.2 o)))).1 hB o
      (Finset.mem_univ o)

end KnotOperatorLP

/--
  **Knot-operator LP selection** (`prop:knot-operator-lp-selection`).
  Given a feasible selection `x` and dual prices `y` of the
  `G⁺ S`-constrained minimisation LP whose objectives agree, `x` is an
  optimal (minimum-crossing-energy) selection, `y` is dual-optimal, every
  constraint with a nonzero shadow price is tight, and every operator in
  the support of `x` has zero reduced cost.

  Conditional on the certificate `heq` (strong duality is not available in
  Mathlib at this pin): it proves what the certificate implies, not that
  one exists.
-/
theorem knot_operator_lp_selection
    {R : Type*} [CommRing R] [PartialOrder R] [IsOrderedRing R]
    {H : Type*} [Ring H] [Algebra R H]
    {Op Basis : Type*} [Fintype Op] [Fintype Basis] [DecidableEq Basis]
    (lp : KnotOperatorLP R H Op Basis) {n_T : Basis → R}
    {x : Op → R} {y : Basis → R}
    (hx : lp.Feasible n_T x) (hy : lp.DualFeasible y)
    (heq : lp.primalObj x = lp.dualObj n_T y) :
    lp.Optimal n_T x ∧ lp.DualOptimal n_T y ∧
      (∀ i, y i * (lp.supplyOf x i - n_T i) = 0) ∧
      ∀ o, x o * (lp.cost o - lp.priceOf y o) = 0 := by
  -- Ref: [schrijver1986theory] §7.2, §7.4
  obtain ⟨h1, h2⟩ := lp.optimal_of_objectives_eq hx hy heq
  exact ⟨h1, h2, lp.complementary_slackness hx hy heq⟩

/-! ### Retired formulation, and why

The previous Lean statement (kept here only to record the defect) maximised
the objective, dropped the Gram factor, and asserted via a class that every optimum
is supported on exactly one operator. That class has no instance. -/

/-- The previous LP data, verbatim except for the name (was
    `KnotOperatorFamily`). -/
structure KnotOperatorFamilyLegacy
    (R : Type*) [CommRing R]
    (H : Type*) [Ring H] [Algebra R H]
    where
  Op : Type*
  opFinite : Fintype Op
  toH : Op → H
  Basis : Type*
  basisFinite : Fintype Basis
  crossingEnergy : Op → R
  supply : Op → Basis → Basis → Basis → R

namespace KnotOperatorFamilyLegacy

variable {R : Type*} [CommRing R] {H : Type*} [Ring H] [Algebra R H]

noncomputable def objective (ops : KnotOperatorFamilyLegacy R H) (x : ops.Op → R) : R :=
  letI := ops.opFinite
  ∑ o : ops.Op, ops.crossingEnergy o * x o

noncomputable def supplyAction (ops : KnotOperatorFamilyLegacy R H)
    (x : ops.Op → R) (i : ops.Basis) : R :=
  letI := ops.opFinite
  ∑ o : ops.Op, x o * ops.supply o i i i

def Feasible [PartialOrder R] (ops : KnotOperatorFamilyLegacy R H)
    (x : ops.Op → R) (n_T : ops.Basis → R) : Prop :=
  (∀ o : ops.Op, 0 ≤ x o) ∧ (∀ i : ops.Basis, n_T i ≤ ops.supplyAction x i)

/-- MAXIMISING optimality — the defect: the .md minimises. -/
def Optimal [PartialOrder R] (ops : KnotOperatorFamilyLegacy R H)
    (x : ops.Op → R) (n_T : ops.Basis → R) : Prop :=
  ops.Feasible x n_T ∧
    ∀ x' : ops.Op → R, ops.Feasible x' n_T → ops.objective x' ≤ ops.objective x

end KnotOperatorFamilyLegacy

/-- The previous class, verbatim except for the name (was
    `KnotOperatorLPSelection`). -/
class KnotOperatorLPSelectionLegacy
    (R : Type*) [CommRing R] [PartialOrder R] [IsOrderedRing R]
    (H : Type*) [Ring H] [Algebra R H]
    (ops : KnotOperatorFamilyLegacy R H)
    where
  frob : LinearMap.BilinForm R H
  frob_nondegenerate : frob.Nondegenerate
  strongDuality :
    ∀ (n_T : ops.Basis → R), ∃ x : ops.Op → R, ops.Optimal x n_T
  complementarySlackness :
    ∀ (n_T : ops.Basis → R) (x : ops.Op → R), ops.Optimal x n_T →
      ∃ oStar : ops.Op, ∀ o : ops.Op, x o ≠ 0 ↔ o = oStar

/-- **The previous class is uninhabitable.** At `n_T = 0`, any optimum `x`
    has `2x` feasible, so `obj x ≤ 0`; hence the zero selection is also
    optimal, and complementary slackness would make its empty support a
    singleton. So the theorem formerly proved under this class
    (`knot_operator_lp_selection`, old form) was vacuous. -/
theorem KnotOperatorLPSelectionLegacy.isEmpty
    {R : Type*} [CommRing R] [PartialOrder R] [IsOrderedRing R]
    {H : Type*} [Ring H] [Algebra R H] (ops : KnotOperatorFamilyLegacy R H) :
    IsEmpty (KnotOperatorLPSelectionLegacy R H ops) := by
  refine ⟨fun inst => ?_⟩
  letI := ops.opFinite
  obtain ⟨x, hxF, hxO⟩ := inst.strongDuality (fun _ => 0)
  have h2 : ops.Feasible (fun o => x o + x o) (fun _ => 0) := by
    refine ⟨fun o => add_nonneg (hxF.1 o) (hxF.1 o), fun i => ?_⟩
    have := hxF.2 i
    simp only [KnotOperatorFamilyLegacy.supplyAction, add_mul,
      Finset.sum_add_distrib] at this ⊢
    exact add_nonneg this this
  have hle := hxO _ h2
  have hobj : ops.objective (fun o => x o + x o) = ops.objective x + ops.objective x := by
    simp only [KnotOperatorFamilyLegacy.objective, mul_add, Finset.sum_add_distrib]
  rw [hobj, add_le_iff_nonpos_left] at hle
  have h0O : ops.Optimal (fun _ => 0) (fun _ => 0) := by
    refine ⟨⟨fun _ => le_rfl, fun _ => by
      simp [KnotOperatorFamilyLegacy.supplyAction]⟩, fun x' hx' => ?_⟩
    have hz : ops.objective (fun _ => (0 : R)) = 0 := by
      simp [KnotOperatorFamilyLegacy.objective]
    rw [hz]; exact (hxO x' hx').trans hle
  obtain ⟨oStar, h⟩ := inst.complementarySlackness _ _ h0O
  exact (h oStar).2 rfl rfl

end QOU.BraidsAndKnots
