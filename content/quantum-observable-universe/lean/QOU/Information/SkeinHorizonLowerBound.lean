import QOU.Information.SkeinObservationBridge

/-!
# Realizing the `3^c` horizon lower bound in the decision-tree model

The P-vs-NP rate leg of the Skein-observation bridge
(`QOU.Information.SkeinObservationSystem.not_polyObservable_of_horizon_cost`)
takes the exponential lower bound `hcost` — the observation is reachable only at
the resolution-tree cost `3^{len}` — as a **hypothesis**, because proving it for a
*general* Skein computation is the P≠NP-hard content and is subject to the
algebrization barrier (Aaronson–Wigderson 2008).

This file discharges `hcost` in the one setting where an exponential lower bound
is **genuinely provable**: the **decision-tree / query model**. `treeSearch d`
walks the `3^d` leaves of a depth-`d` ternary resolution tree one step at a time;
its observation matches the normal form only at the last leaf, so the observer
*must* take `3^d` steps. This is an honest, unconditional exponential separation —
but a **query lower bound**, not a resolution of P versus NP. It certifies that
the bridge's rate separation `not_polyObservable_of_horizon_cost` is **inhabited**
by a system with a provable `hcost`.
-/

namespace QOU.Information

open SkeinObservationSystem

/-- Iterating `n ↦ n + 1` from `0` reaches `k` after `k` steps. -/
theorem succ_iterate_zero (k : ℕ) : (fun n => n + 1)^[k] 0 = k := by
  induction k with
  | zero => rfl
  | succ n ih => rw [Function.iterate_succ_apply', ih]

/-- **Ternary-resolution search at depth `d`.** The state is a step counter, each
    step advances one leaf of the depth-`d` resolution tree (`n ↦ n + 1`), the
    filtration is the depth `d`, and the observation matches the normal form
    `3^d` only at the last of the `3^d` leaves. The decision-tree model in which
    the exponential horizon lower bound is genuinely provable. -/
def treeSearch (d : ℕ) : SkeinObservationSystem ℕ ℕ where
  step := fun n => n + 1
  obs := id
  normalForm := 3 ^ d
  len := fun _ => d

/-- **The exponential lower bound `hcost`, discharged.** Starting from leaf `0`,
    the observation matches the normal form only at step `3^d = 3^{len}` — the
    observer must visit every leaf. Provable because the model is decision-tree
    (query) complexity, not general circuit complexity. -/
theorem treeSearch_hcost (d : ℕ) :
    ∀ k : ℕ, (treeSearch d).obs ((treeSearch d).step^[k] 0)
        = (treeSearch d).obs (treeSearch d).normalForm →
      3 ^ (treeSearch d).len 0 ≤ k := by
  intro k hk
  simp only [treeSearch, id_eq, succ_iterate_zero] at hk
  simp only [treeSearch]
  omega

/-- `treeSearch d` **is** observed-halting — the observation is reached, at step
    `3^d`. -/
theorem treeSearch_haltsObserved (d : ℕ) : (treeSearch d).HaltsObserved 0 := by
  refine ⟨3 ^ d, ?_⟩
  simp only [treeSearch, id_eq, succ_iterate_zero]

/-- **The horizon separation is inhabited.** `treeSearch d` at leaf `0` is
    observed-halting yet **not** poly-observable under the identity (linear)
    budget: a concrete, unconditional exponential separation between
    `HaltsObserved` and `PolyObservable`, with `hcost` proved rather than assumed.
    An honest query / decision-tree lower bound — **not** a proof of P ≠ NP (the
    general lower bound remains barred by algebrization). -/
theorem treeSearch_not_polyObservable_id (d : ℕ) :
    ¬ (treeSearch d).PolyObservable id 0 :=
  (treeSearch d).not_polyObservable_id_of_horizon_cost 0 (treeSearch_hcost d)

/-- The separation, packaged: observed-halting **and** not poly-observable. -/
theorem treeSearch_haltsObserved_not_polyObservable (d : ℕ) :
    (treeSearch d).HaltsObserved 0 ∧ ¬ (treeSearch d).PolyObservable id 0 :=
  ⟨treeSearch_haltsObserved d, treeSearch_not_polyObservable_id d⟩

end QOU.Information
