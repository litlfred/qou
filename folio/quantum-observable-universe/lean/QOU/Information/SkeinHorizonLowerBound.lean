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

/-! ### The algebrization obstruction: a poly shortcut refutes the lower bound

Why does the provable lower bound stay confined to the decision-tree model? The
structural reason: **any polynomial-time shortcut to the observation refutes
`hcost`.** `treeSearch` survives only because its observation is a *black-box*
counter — no shortcut exists, so `hcost` is inhabited there and nowhere yet in
the Skein setting.

**Correction (2026-08-15).** This paragraph previously read: *"An algebraic
observation (the Jones polynomial / Markov trace) is, by contrast, an
efficiently-evaluable object: evaluating it directly is exactly such a
shortcut."* That is **false at the substrate point**, and contradicts a result
the corpus itself cites: exact evaluation of the Jones polynomial at all but
finitely many `q` is `#P`-hard (Jaeger–Vertigan–Welsh, `[jaeger1990]`, restated
in `conj:qou-p-neq-np`), and `q₀` is strictly non-torsion. The Markov trace at
`q₀` is precisely *not* efficiently evaluable, so "it is shortcuttable" cannot be
the reason an algebraic observation fails to carry the bound.

**No replacement reason is offered, because none is on record.** With the
tractability argument gone, nothing currently establishes that `hcost` *fails*
in the Skein setting — it is simply not established there either way. Note the
deleted premise in fact points the other way: if exact Jones evaluation at `q₀`
is `#P`-hard, that is prima facie evidence *for* an exponential arrival time,
not against one. Stating the gap is the honest disposition.

Do not substitute the genericity argument here. That argument
(`ObstructionGenericity`: a nonzero polynomial obstruction has cofinite
non-vanishing locus, so its non-vanishing is cheap) concerns the separating
**invariant** in `conj:qou-p-neq-np`, a different object from `hcost`; nothing
about the root locus of a polynomial in `q` bears on whether an observation's
arrival time is exponentially bounded below. Keeping the conclusion while
swapping in an unrelated premise is how the original error survived.

The lemma below is unaffected: it is hypothetical in `PolyObservable` and takes
the shortcut as an assumption rather than asserting one exists. Only the prose
justifying it was wrong.

-- Ref: [jaeger1990] https://doi.org/10.1017/S0305004100068936
-- Ref: [aaronsonwigderson2009] https://doi.org/10.1145/1490270.1490272 -/

/-- **A polynomial shortcut refutes the horizon lower bound.** If the observation
    is reachable within a budget `poly` the horizon exceeds
    (`PolyObservable poly P` with `poly (len P) < 3^{len P}`), then the
    exponential lower bound `hcost` cannot hold for `P`. Contrapositive of
    `not_polyObservable_of_horizon_cost`: an efficiently-shortcuttable (algebraic)
    observation is incompatible with a `3^{len}` lower bound — the structural core
    of why an algebraic invariant cannot separate the classes. -/
theorem no_horizon_cost_of_polyObservable {S V : Type*}
    (sys : SkeinObservationSystem S V) (poly : ℕ → ℕ) (P : S)
    (hpoly : sys.PolyObservable poly P) (hbudget : poly (sys.len P) < 3 ^ sys.len P) :
    ¬ (∀ k : ℕ, sys.obs (sys.step^[k] P) = sys.obs sys.normalForm →
        3 ^ sys.len P ≤ k) :=
  fun hcost => sys.not_polyObservable_of_horizon_cost poly P hcost hbudget hpoly

/-- **Dichotomy (query-hard XOR shortcuttable).** Fixing an input whose horizon
    exceeds the budget, a system cannot both admit the exponential lower bound
    `hcost` and a polynomial shortcut. The lower bound lives exactly where no
    algebraic shortcut does — the decision-tree side, witnessed by `treeSearch`. -/
theorem not_polyObservable_or_not_horizon_cost {S V : Type*}
    (sys : SkeinObservationSystem S V) (poly : ℕ → ℕ) (P : S)
    (hbudget : poly (sys.len P) < 3 ^ sys.len P) :
    ¬ sys.PolyObservable poly P ∨
      ¬ (∀ k : ℕ, sys.obs (sys.step^[k] P) = sys.obs sys.normalForm →
          3 ^ sys.len P ≤ k) := by
  by_cases h : sys.PolyObservable poly P
  · exact Or.inr (no_horizon_cost_of_polyObservable sys poly P h hbudget)
  · exact Or.inl h

/-- Iterating `n ↦ n + 1` from an arbitrary starting leaf `m` reaches `m + k`
    after `k` steps (`bean qou-4hbq`). -/
theorem succ_iterate_add (m k : ℕ) : (fun n => n + 1)^[k] m = m + k := by
  induction k with
  | zero => rfl
  | succ n ih =>
    rw [Function.iterate_succ_apply', ih]
    omega

/-- For any depth `d`, the filtration length `(treeSearch d).len 0 = d` is strictly
    dominated by the normal-form leaf index `3 ^ d`. -/
theorem treeSearch_len_lt_normalForm (d : ℕ) :
    (treeSearch d).len 0 < (treeSearch d).normalForm := by
  change d < 3 ^ d
  exact Nat.lt_pow_self (by norm_num : 1 < 3)

end QOU.Information
