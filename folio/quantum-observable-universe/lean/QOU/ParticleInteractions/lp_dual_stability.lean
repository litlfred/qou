import Mathlib.Tactic
import QOU.Optimization.MatrixFarkasInstance

/-!
# QOU.ParticleInteractions.lp_dual_stability

**Proposition** ([`prop:lp-dual-stability`](../../../quantum-observable-universe/nuclear-interactions/lp-dual-stability.md)):
*LP dual stability of confined hadrons.*

The block claims four things about the confined optimum `x*` of the
operator-selection LP

    min tᵀx   s.t.   Σⱼ xⱼ = n_target,   G x ≥ 0,   x ≥ 0 :

1. `x*` is LP-stable: `G x* ≥ 0` in every channel;
2. the dual shadow prices are bounded: `|y*ᵢ| ≤ κ(G) · ‖t‖`;
3. the `B₃` sub-braid `σ₀σ₁⁻¹` is LP-unstable;
4. strong duality: `tᵀx* = y₀* · n_target`.

## What is proved here (2026-11-21)

Until this date the file's `LpDualStabilityContext` carried all four
conclusions as fields and `lp_dual_stability` returned them
(`⟨ctx.primal_stable, …⟩`), the self-assuming projection of AGENTS.md
§3b-cond item 5, while this docstring claimed the opposite.

The LP is now written out in standard form (`opSelA`, `opSelRhs`,
`opSelCost`, with one slack per channel), and **claims 1 and 4 are
derived** from primal optimality alone:

* `stable_of_feasible` — any feasible point satisfies `G x ≥ 0`;
* `count_of_feasible` — any feasible point has `Σ xⱼ = n_target`;
* `lp_dual_stability` — at a primal optimum there is a dual optimum `l`
  with `y₀ = l (Fin.last k)` and `tᵀx = n_target · y₀`, via the in-repo
  unconditional `QOU.Optimization.lp_strong_duality_uncond`.

**Claims 2 and 3 are not proved.** Claim 2 is not a consequence of LP
duality: LP shadow prices are not bounded by the Gram condition number in
general, so it is a property of the specific `6 × 6` Gram matrix at `q₀`.
Claim 3 is a sign condition on one explicit vector, also specific to that
matrix. Neither is stated as a hypothesis here.

LaTeX label: `prop:lp-dual-stability`.
-/

namespace QOU.ParticleInteractions

open QOU.Optimization

/-- Constraint matrix of the operator-selection LP in standard form, over
    `k` channel variables followed by `k` slacks. Row `castSucc i` reads
    `Σⱼ G i j xⱼ − sᵢ = 0`; the last row reads `Σⱼ xⱼ = n_target`. -/
def opSelA (k : ℕ) (G : Fin k → Fin k → ℝ) : Fin (k + 1) → Fin (k + k) → ℝ :=
  Fin.lastCases
    (fun col => Fin.addCases (fun _ => (1 : ℝ)) (fun _ => 0) col)
    (fun i col => Fin.addCases (fun j => G i j) (fun i' => if i' = i then -1 else 0) col)

/-- Right-hand side: `0` on the `G` rows, `n_target` on the count row. -/
def opSelRhs (k n : ℕ) : Fin (k + 1) → ℝ :=
  Fin.lastCases (n : ℝ) (fun _ => 0)

/-- Cost: `t` on the channel variables, `0` on the slacks. -/
def opSelCost (k : ℕ) (t : Fin k → ℝ) : Fin (k + k) → ℝ :=
  Fin.addCases t (fun _ => 0)

/-- The channel variables of a standard-form point. -/
def chan {k : ℕ} (z : Fin (k + k) → ℝ) (j : Fin k) : ℝ := z (Fin.castAdd k j)

/-- **LP stability is feasibility.** Every feasible point of the
    operator-selection LP satisfies `G x ≥ 0` in every channel. -/
theorem stable_of_feasible {k n : ℕ} {G : Fin k → Fin k → ℝ} {z : Fin (k + k) → ℝ}
    (hz : PrimalFeasible (opSelA k G) (opSelRhs k n) z) (i : Fin k) :
    0 ≤ ∑ j, G i j * chan z j := by
  have h := hz.eq (Fin.castSucc i)
  simp only [opSelA, opSelRhs, Fin.lastCases_castSucc, Fin.sum_univ_add,
    Fin.addCases_left, Fin.addCases_right] at h
  have hs : ∑ i' : Fin k, (if i' = i then (-1 : ℝ) else 0) * z (Fin.natAdd k i')
      = - z (Fin.natAdd k i) := by
    simp [ite_mul, Finset.sum_ite_eq']
  rw [hs] at h
  have := hz.nonneg (Fin.natAdd k i)
  simp only [chan]
  linarith

/-- Every feasible point carries `n_target` in total. -/
theorem count_of_feasible {k n : ℕ} {G : Fin k → Fin k → ℝ} {z : Fin (k + k) → ℝ}
    (hz : PrimalFeasible (opSelA k G) (opSelRhs k n) z) :
    ∑ j, chan z j = n := by
  have h := hz.eq (Fin.last k)
  simp only [opSelA, opSelRhs, Fin.lastCases_last, Fin.sum_univ_add,
    Fin.addCases_left, Fin.addCases_right, one_mul, zero_mul,
    Finset.sum_const_zero, add_zero] at h
  simpa [chan] using h

/-- The primal objective of the standard form is `tᵀx` on the channels. -/
theorem primalObj_opSelCost {k : ℕ} (t : Fin k → ℝ) (z : Fin (k + k) → ℝ) :
    primalObj (opSelCost k t) z = ∑ j, t j * chan z j := by
  unfold primalObj opSelCost chan
  rw [Fin.sum_univ_add]
  simp only [Fin.addCases_left, Fin.addCases_right, zero_mul, Finset.sum_const_zero,
    add_zero]

/-- The dual objective collapses to `n_target · y₀`. -/
theorem dualObj_opSelRhs (k n : ℕ) (l : Fin (k + 1) → ℝ) :
    dualObj (opSelRhs k n) l = (n : ℝ) * l (Fin.last k) := by
  simp [dualObj, opSelRhs, Fin.sum_univ_castSucc]

/-- **LP dual stability of confined hadrons, claims 1 and 4**
    ([`prop:lp-dual-stability`]). At a primal optimum `z` of the
    operator-selection LP, (1) `G x ≥ 0` in every channel, the total is
    `n_target`, and (4) there is a dual optimum `l` whose net-constraint price
    `y₀ = l (Fin.last k)` satisfies `tᵀx = n_target · y₀`.

    Derived, sorry-free: (1) from feasibility, (4) from the in-repo
    unconditional LP strong duality. Claims 2 and 3 of the block are specific
    to the Gram matrix at `q₀` and are not proved (see the module docstring). -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP strong duality)
-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/lp-dual-stability.md
theorem lp_dual_stability {k n : ℕ} (G : Fin k → Fin k → ℝ) (t : Fin k → ℝ)
    (z : Fin (k + k) → ℝ)
    (hz : PrimalOptimal (opSelA k G) (opSelRhs k n) (opSelCost k t) z) :
    (∀ i, 0 ≤ ∑ j, G i j * chan z j) ∧
    (∑ j, chan z j = n) ∧
    ∃ l, DualOptimal (opSelA k G) (opSelRhs k n) (opSelCost k t) l ∧
      ∑ j, t j * chan z j = (n : ℝ) * l (Fin.last k) := by
  refine ⟨stable_of_feasible hz.1, count_of_feasible hz.1, ?_⟩
  obtain ⟨l, hl, hobj⟩ := lp_strong_duality_uncond hz
  refine ⟨l, hl, ?_⟩
  rw [← primalObj_opSelCost, ← hobj, dualObj_opSelRhs]

end QOU.ParticleInteractions
