import QOU.BraidKnot.LpDualityHypothesisClass
import QOU.Optimization.MatrixFarkasInstance
import Mathlib.Topology.Order.Compact
import Mathlib.Topology.MetricSpace.ProperSpace

/-!
# Strong duality for the operator-selection LP

`QOU.BraidKnot.OperatorSelectionLP` is the LP
`min Σ tᵢ xᵢ  s.t.  Σ xᵢ = nTarget,  (G x)ᵢ ≥ 0,  xᵢ ≥ −M`.
This file proves, with no hypothesis beyond feasibility:

* `exists_primal_min`: the feasible set is compact (closed, and each coordinate
  lies in `[−M, nTarget + card·|M|]`), so the minimum is attained;
* `exists_optimal_pair`: there is a dual-feasible `(y₀, y, w)` with zero
  duality gap at that minimum (Schrijver §7.2);
* `HasFiniteLPDuality.ofFeasible`: hence the class `HasFiniteLPDuality lp`
  holds for every feasible `lp` (bean `qou-7t1n`, issue #8911).

The dual certificate comes from the Farkas alternative proved in
`QOU.Mathlib.FinitelyGeneratedConeClosed` (`farkas_alternative_real`), applied
to the standard form with `u = x + M` and slacks `s = G x`.
-/

namespace QOU.BraidKnot.OperatorSelectionLP

open scoped BigOperators

variable (lp : OperatorSelectionLP)

/-- The feasible set is closed. -/
theorem isClosed_feasible : IsClosed {x : lp.Λ → ℝ | lp.PrimalFeasible x} := by
  have h1 : IsClosed {x : lp.Λ → ℝ | ∑ i, x i = lp.nTarget} :=
    isClosed_eq (continuous_finset_sum _ fun i _ => continuous_apply i) continuous_const
  have h2 : IsClosed {x : lp.Λ → ℝ | ∀ i, 0 ≤ lp.Gx x i} := by
    simp only [Set.setOf_forall]
    exact isClosed_iInter fun i => isClosed_le continuous_const
      (continuous_finset_sum _ fun j _ => continuous_const.mul (continuous_apply j))
  have h3 : IsClosed {x : lp.Λ → ℝ | ∀ i, -lp.M ≤ x i} := by
    simp only [Set.setOf_forall]
    exact isClosed_iInter fun i => isClosed_le continuous_const (continuous_apply i)
  have : {x : lp.Λ → ℝ | lp.PrimalFeasible x} =
      {x | ∑ i, x i = lp.nTarget} ∩ {x | ∀ i, 0 ≤ lp.Gx x i} ∩ {x | ∀ i, -lp.M ≤ x i} := by
    ext x; simp [PrimalFeasible, and_assoc]
  rw [this]; exact (h1.inter h2).inter h3

/-- Each coordinate of a feasible point lies in `[-M, nTarget + card·|M|]`. -/
theorem feasible_coord_le {x : lp.Λ → ℝ} (hx : lp.PrimalFeasible x) (j : lp.Λ) :
    x j ≤ lp.nTarget + Fintype.card lp.Λ * |lp.M| := by
  classical
  have hsum := hx.1
  have hsplit : ∑ i, x i = x j + ∑ i ∈ Finset.univ.erase j, x i :=
    (Finset.add_sum_erase _ _ (Finset.mem_univ j)).symm
  have hrest : ∑ i ∈ Finset.univ.erase j, (-|lp.M|) ≤ ∑ i ∈ Finset.univ.erase j, x i :=
    Finset.sum_le_sum fun i _ => le_trans (neg_le_neg (le_abs_self lp.M)) (hx.2.2 i)
  simp only [Finset.sum_const, Finset.card_erase_of_mem (Finset.mem_univ j),
    Finset.card_univ, nsmul_eq_mul] at hrest
  have hc : (1 : ℝ) ≤ Fintype.card lp.Λ := by
    exact_mod_cast Fintype.card_pos_iff.mpr ⟨j⟩
  have hM := abs_nonneg lp.M
  have hcast : ((Fintype.card lp.Λ - 1 : ℕ) : ℝ) = Fintype.card lp.Λ - 1 := by
    rw [Nat.cast_sub (by exact_mod_cast hc)]; simp
  rw [hcast] at hrest
  nlinarith

/-- The feasible set is compact. -/
theorem isCompact_feasible : IsCompact {x : lp.Λ → ℝ | lp.PrimalFeasible x} := by
  refine Metric.isCompact_of_isClosed_isBounded (lp.isClosed_feasible) ?_
  rw [Metric.isBounded_iff_subset_closedBall 0]
  refine ⟨|lp.nTarget| + Fintype.card lp.Λ * |lp.M| + |lp.M|, fun x hx => ?_⟩
  rw [Metric.mem_closedBall, dist_zero_right, pi_norm_le_iff_of_nonneg (by positivity)]
  intro j
  rw [Real.norm_eq_abs, abs_le]
  have h1 := lp.feasible_coord_le hx j
  have h2 := hx.2.2 j
  constructor
  · nlinarith [le_abs_self lp.M, abs_nonneg lp.nTarget,
      (by positivity : (0:ℝ) ≤ Fintype.card lp.Λ * |lp.M|)]
  · nlinarith [le_abs_self lp.nTarget, abs_nonneg lp.M]

/-- A feasible operator-selection LP attains its minimum. -/
theorem exists_primal_min (h : ∃ x, lp.PrimalFeasible x) :
    ∃ x, lp.PrimalFeasible x ∧ ∀ x', lp.PrimalFeasible x' → lp.primalObj x ≤ lp.primalObj x' := by
  obtain ⟨x, hx, hmin⟩ := lp.isCompact_feasible.exists_isMinOn h
    (continuous_finset_sum _ fun i _ => continuous_const.mul (continuous_apply i)).continuousOn
  exact ⟨x, hx, fun x' hx' => hmin hx'⟩


/-! ### Strong duality through the standard form

With `u = x + M` and slacks `s = G x`, the LP becomes
`min Σ t u  s.t.  Σ u = nTarget + k·M,  G u − s = M·(G 1),  u, s ≥ 0`
over `Fin (k + k)` variables and `Fin (k + 1)` rows, `k = card Λ`. -/

section Standard
variable {k : ℕ} (e : lp.Λ ≃ Fin k)

/-- Constraint matrix of the standard form. -/
noncomputable def stdA : Fin (k + 1) → Fin (k + k) → ℝ := fun r =>
  Fin.lastCases (fun q => Fin.addCases (fun _ => 1) (fun _ => 0) q)
    (fun i q => Fin.addCases (fun j => lp.G (e.symm i) (e.symm j))
      (fun i' => if i' = i then -1 else 0) q) r

/-- Right-hand side of the standard form. -/
noncomputable def stdRhs : Fin (k + 1) → ℝ :=
  Fin.lastCases (lp.nTarget + k * lp.M) (fun i => lp.M * ∑ j, lp.G (e.symm i) (e.symm j))

/-- Cost of the standard form. -/
noncomputable def stdCost : Fin (k + k) → ℝ := Fin.addCases (fun j => lp.t (e.symm j)) (fun _ => 0)

/-- Original point of a standard-form point. -/
def ofStd (v : Fin (k + k) → ℝ) : lp.Λ → ℝ := fun a => v (Fin.castAdd k (e a)) - lp.M

/-- Standard-form point of an original point. -/
noncomputable def toStd (x : lp.Λ → ℝ) : Fin (k + k) → ℝ :=
  Fin.addCases (fun j => x (e.symm j) + lp.M) (fun i => lp.Gx x (e.symm i))

theorem sum_symm (g : lp.Λ → ℝ) : ∑ j : Fin k, g (e.symm j) = ∑ a, g a := e.symm.sum_comp g

theorem stdCost_obj (v : Fin (k + k) → ℝ) :
    ∑ q, stdCost lp e q * v q = lp.primalObj (lp.ofStd e v) + lp.M * ∑ a, lp.t a := by
  rw [Fin.sum_univ_add]
  simp only [stdCost, Fin.addCases_left, Fin.addCases_right, zero_mul, Finset.sum_const_zero,
    add_zero, primalObj, ofStd]
  rw [← sum_symm lp e (fun a => lp.t a * (v (Fin.castAdd k (e a)) - lp.M)),
    ← sum_symm lp e (fun a => lp.t a), Finset.mul_sum, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun j _ => ?_
  simp only [Equiv.apply_symm_apply]; ring

theorem ofStd_toStd (x : lp.Λ → ℝ) : lp.ofStd e (lp.toStd e x) = x := by
  funext a; simp [ofStd, toStd]

theorem toStd_feasible {x : lp.Λ → ℝ} (hx : lp.PrimalFeasible x) :
    (∀ r, ∑ q, stdA lp e r q * lp.toStd e x q = stdRhs lp e r) ∧ ∀ q, 0 ≤ lp.toStd e x q := by
  refine ⟨fun r => ?_, fun q => ?_⟩
  · refine Fin.lastCases ?_ (fun i => ?_) r
    · simp only [stdA, stdRhs, Fin.lastCases_last, Fin.sum_univ_add, Fin.addCases_left,
        Fin.addCases_right, toStd, one_mul, zero_mul, Finset.sum_const_zero, add_zero]
      rw [Finset.sum_add_distrib, sum_symm lp e (fun a => x a), hx.1]
      simp
    · simp only [stdA, stdRhs, Fin.lastCases_castSucc, Fin.sum_univ_add, Fin.addCases_left,
        Fin.addCases_right, toStd]
      simp only [ite_mul, neg_one_mul, zero_mul, Finset.sum_ite_eq', Finset.mem_univ, if_true]
      rw [sum_symm lp e (fun a => lp.G (e.symm i) a * (x a + lp.M)),
        sum_symm lp e (fun a => lp.G (e.symm i) a), Gx, Finset.mul_sum,
        ← Finset.sum_neg_distrib, ← Finset.sum_add_distrib]
      refine Finset.sum_congr rfl fun j _ => ?_
      ring
  · refine Fin.addCases (fun j => ?_) (fun i => ?_) q
    · simp only [toStd, Fin.addCases_left]; linarith [hx.2.2 (e.symm j)]
    · simp only [toStd, Fin.addCases_right]; exact hx.2.1 _

theorem ofStd_feasible {v : Fin (k + k) → ℝ}
    (hv : (∀ r, ∑ q, stdA lp e r q * v q = stdRhs lp e r) ∧ ∀ q, 0 ≤ v q) :
    lp.PrimalFeasible (lp.ofStd e v) := by
  refine ⟨?_, fun a => ?_, fun a => ?_⟩
  · have h := hv.1 (Fin.last k)
    simp only [stdA, stdRhs, Fin.lastCases_last, Fin.sum_univ_add, Fin.addCases_left,
      Fin.addCases_right, one_mul, zero_mul, Finset.sum_const_zero, add_zero] at h
    simp only [ofStd]
    rw [Finset.sum_sub_distrib, e.sum_comp (fun j => v (Fin.castAdd k j)), h]
    simp [Fintype.card_congr e]
  · have h := hv.1 (Fin.castSucc (e a))
    simp only [stdA, stdRhs, Fin.lastCases_castSucc, Fin.sum_univ_add, Fin.addCases_left,
      Fin.addCases_right, ite_mul, neg_one_mul, zero_mul, Finset.sum_ite_eq', Finset.mem_univ,
      if_true, Equiv.symm_apply_apply] at h
    have hs := hv.2 (Fin.natAdd k (e a))
    have : lp.Gx (lp.ofStd e v) a = v (Fin.natAdd k (e a)) := by
      simp only [Gx, ofStd]
      rw [← e.symm.sum_comp, Finset.mul_sum] at *
      have h' : ∑ j : Fin k, lp.G a (e.symm j) * v (Fin.castAdd k j)
          - ∑ j : Fin k, lp.M * lp.G a (e.symm j) = v (Fin.natAdd k (e a)) := by linarith
      rw [← h', ← Finset.sum_sub_distrib]
      refine Finset.sum_congr rfl fun j _ => ?_
      simp only [Equiv.apply_symm_apply]; ring
    rw [this]; exact hs
  · simp only [ofStd]; linarith [hv.2 (Fin.castAdd k (e a))]

end Standard


/-- **Strong duality for the operator-selection LP.** A feasible LP has a
primal-feasible `x` and a dual-feasible `(y₀, y, w)` with zero duality gap.
The minimum exists by compactness (`exists_primal_min`); the dual certificate
comes from the Farkas alternative (`farkas_alternative_real`) applied to the
standard form. -/
theorem exists_optimal_pair (h : ∃ x, lp.PrimalFeasible x) :
    ∃ x y₀ y w, lp.PrimalFeasible x ∧ lp.DualFeasible y₀ y w ∧ lp.duality_gap x y₀ w = 0 := by
  classical
  obtain ⟨x, hx, hmin⟩ := lp.exists_primal_min h
  set k := Fintype.card lp.Λ
  let e : lp.Λ ≃ Fin k := Fintype.equivFin lp.Λ
  obtain ⟨l, hl, hγ⟩ := QOU.Mathlib.farkas_alternative_real
    (stdA lp e) (stdRhs lp e) (stdCost lp e) (∑ q, stdCost lp e q * lp.toStd e x q)
    ⟨lp.toStd e x, lp.toStd_feasible e hx⟩ (by
      rintro ⟨v, hv, hlt⟩
      rw [stdCost_obj, stdCost_obj, ofStd_toStd] at hlt
      have := hmin _ (lp.ofStd_feasible e hv)
      linarith)
  set y₀ := l (Fin.last k)
  set y : lp.Λ → ℝ := fun a => l (Fin.castSucc (e a))
  set w : lp.Λ → ℝ := fun a => lp.t a - y₀ - ∑ b, lp.G b a * y b
  -- the two families of dual constraints, read off `hl`
  have hcol : ∀ a, y₀ + ∑ b, lp.G b a * y b ≤ lp.t a := by
    intro a
    have h := hl (Fin.castAdd k (e a))
    simp only [stdA, stdCost, Fin.sum_univ_castSucc, Fin.lastCases_castSucc, Fin.lastCases_last,
      Fin.addCases_left, Equiv.symm_apply_apply, mul_one] at h
    rw [← e.sum_comp (fun i => l (Fin.castSucc i) * lp.G (e.symm i) a)] at h
    simp only [Equiv.symm_apply_apply] at h
    have : ∑ b, lp.G b a * y b = ∑ b, l (Fin.castSucc (e b)) * lp.G b a :=
      Finset.sum_congr rfl fun b _ => mul_comm _ _
    rw [this]; linarith
  have hy : ∀ a, 0 ≤ y a := by
    intro a
    have h := hl (Fin.natAdd k (e a))
    simp only [stdA, stdCost, Fin.sum_univ_castSucc, Fin.lastCases_castSucc, Fin.lastCases_last,
      Fin.addCases_right, mul_zero, add_zero, mul_ite, mul_neg, mul_one, mul_zero,
      Finset.sum_ite_eq, Finset.mem_univ, if_true] at h
    simp only [y]; linarith
  have hdual : lp.DualFeasible y₀ y w :=
    ⟨fun j => by simp only [w]; ring, hy, fun a => by simp only [w]; linarith [hcol a]⟩
  refine ⟨x, y₀, y, w, hx, hdual, ?_⟩
  -- the dual objective of `l` is `dualObj y₀ w + M Σ t`
  have hobj : ∑ r, stdRhs lp e r * l r = lp.dualObj y₀ w + lp.M * ∑ a, lp.t a := by
    simp only [stdRhs, Fin.sum_univ_castSucc, Fin.lastCases_castSucc, Fin.lastCases_last,
      dualObj, w, Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
    rw [← e.sum_comp (fun i => lp.M * (∑ j, lp.G (e.symm i) (e.symm j)) * l (Fin.castSucc i))]
    simp only [Equiv.symm_apply_apply]
    have hG : ∀ a, ∑ j : Fin k, lp.G a (e.symm j) = ∑ b, lp.G a b := fun a => e.symm.sum_comp _
    simp only [hG, Finset.sum_comm (f := fun a b => lp.G b a * y b) ]
    simp only [y, Finset.mul_sum, Finset.sum_mul]
    have e1 : y₀ = l (Fin.last k) := rfl
    have e2 : ((Fintype.card lp.Λ : ℕ) : ℝ) = (k : ℝ) := rfl
    rw [e1, e2, mul_sub, mul_sub, Finset.mul_sum, Finset.mul_sum]
    simp only [Finset.mul_sum, mul_assoc]
    ring
  have hweak := lp.weak_duality hx hdual
  rw [hobj, stdCost_obj, ofStd_toStd] at hγ
  unfold duality_gap
  rw [abs_eq_zero]; linarith

end QOU.BraidKnot.OperatorSelectionLP

namespace QOU.BraidKnot.HasFiniteLPDuality

/-- **Every feasible operator-selection LP carries the strong-duality
certificate.** The instance is built from `exists_optimal_pair`, so
`HasFiniteLPDuality lp` is no longer an assumption for a feasible `lp`. -/
noncomputable def ofFeasible (lp : OperatorSelectionLP) (h : ∃ x, lp.PrimalFeasible x) :
    HasFiniteLPDuality lp :=
  let hp := lp.exists_optimal_pair h
  { x := hp.choose
    y₀ := hp.choose_spec.choose
    y := hp.choose_spec.choose_spec.choose
    w := hp.choose_spec.choose_spec.choose_spec.choose
    primal_feasible := hp.choose_spec.choose_spec.choose_spec.choose_spec.1
    dual_feasible := hp.choose_spec.choose_spec.choose_spec.choose_spec.2.1
    dualityGapZero := hp.choose_spec.choose_spec.choose_spec.choose_spec.2.2 }

end QOU.BraidKnot.HasFiniteLPDuality
