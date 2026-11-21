import QOU.Basic

/-!
# QOU.BraidKnot.LpDualityHypothesisClass — finite LP strong-duality + complementary slackness as a §3b-cond class

Class-axiomatises the two routine LP-theory inputs to the
operator-selection-LP machinery:

  1. **Strong duality** (Schrijver §7.2): for a bounded + feasible
     finite LP, the primal and dual optima coincide, giving
     `duality_gap = 0`.
  2. **Complementary slackness** (Schrijver §7.4): at the optimum,
     a partition `λ` lies in the LP active set iff its primal
     constraint is tight.

These are the two `sorry`s in
`content/.../braids-and-knots/confinement-nf-partial-proof.lean`
(theorems `strong_duality` + `complementary_slackness`).  Per
AGENTS.md §3b-cond, axiomatising them as a class lets the two
theorems be derived as `class.field` references rather than
free-standing `sorry`s — the proper conditional-class locale for
LP-theory inputs that aren't yet wired in Mathlib.

The class is purely a hypothesis carrier; the trivial model fills
both fields via the LP-theory citations (single `sorry` per
field, with explicit `-- Ref: [schrijver1986theory]` per AGENTS.md
§1).  When Mathlib gets a finite-dim LP-duality library
(`Mathlib.Analysis.Convex.LinearProgramming` or similar), the
trivial-model sorrys can be discharged unconditionally without
touching the consumer side of the class.

Bridge to `prop:confinement-nf-partial-proof`: a future refactor
can add `[lpDuality : HasFiniteLPDuality lp]` to the hypotheses of
`theorem_3_strong_duality` and `theorem_1_maximizer_in_active_set`,
deriving them from `lpDuality.dualityGapZero` and
`lpDuality.complementarySlackness` respectively — no `sorry`s in
the consumer file, only in the trivial model.

LaTeX: `\label{def:lp-duality-hypothesis-class}`

References:
- Schrijver, A. (1986). Theory of Linear and Integer Programming,
  Wiley. §7.2 (strong duality), §7.4 (complementary slackness).
-/

namespace QOU.BraidKnot

universe u

/-- **The operator-selection LP** of `prop:operator-selection-lp`, as data
(repaired 2026-11-20, bean `qou-dx7g`):

    minimise   Σᵢ tᵢ xᵢ
    subject to Σᵢ xᵢ = n_target,   Σⱼ Gᵢⱼ xⱼ ≥ 0 (∀ i),   xᵢ ≥ -M (∀ i),

with dual (multipliers `y₀` free, `yᵢ ≥ 0`, `wᵢ ≥ 0`)

    maximise   n_target · y₀ - M Σᵢ wᵢ
    subject to y₀ + Σᵢ Gᵢⱼ yᵢ + wⱼ = tⱼ (∀ j).

Before the repair this record carried `primal_obj`, `dual_obj`, `active_set`
and `tight` as *free fields* and no constraint data, so "strong duality" related
two numbers the instance chose.  Now the objectives, the active set and
tightness are definitions computed from the LP data and a primal/dual pair. -/
structure OperatorSelectionLP where
  /-- Index set of the basis `b_i` (the partitions / NF words). -/
  Λ : Type
  [fintype : Fintype Λ]
  /-- Objective `tᵢ = tr_M(bᵢ)`. -/
  t : Λ → ℝ
  /-- Frobenius Gram matrix `Gᵢⱼ = tr_M(bᵢ bⱼ)`. -/
  G : Λ → Λ → ℝ
  /-- Net target. -/
  nTarget : ℝ
  /-- Box bound `M`. -/
  M : ℝ

attribute [instance] OperatorSelectionLP.fintype

namespace OperatorSelectionLP

variable (lp : OperatorSelectionLP)

/-- `(G x)ᵢ = Σⱼ Gᵢⱼ xⱼ`. -/
def Gx (x : lp.Λ → ℝ) (i : lp.Λ) : ℝ := ∑ j, lp.G i j * x j

/-- Primal feasibility. -/
def PrimalFeasible (x : lp.Λ → ℝ) : Prop :=
  (∑ i, x i = lp.nTarget) ∧ (∀ i, 0 ≤ lp.Gx x i) ∧ (∀ i, -lp.M ≤ x i)

/-- Dual feasibility. -/
def DualFeasible (y₀ : ℝ) (y w : lp.Λ → ℝ) : Prop :=
  (∀ j, y₀ + ∑ i, lp.G i j * y i + w j = lp.t j) ∧ (∀ i, 0 ≤ y i) ∧ (∀ i, 0 ≤ w i)

/-- Primal objective `Σ tᵢ xᵢ`. -/
def primalObj (x : lp.Λ → ℝ) : ℝ := ∑ i, lp.t i * x i

/-- Dual objective `n_target · y₀ - M Σ wᵢ`. -/
def dualObj (y₀ : ℝ) (w : lp.Λ → ℝ) : ℝ := lp.nTarget * y₀ - lp.M * ∑ i, w i

/-- **Weak duality, with the slack written out.**  For any primal `x` meeting
    the net constraint and any dual pair meeting the equality constraints,
    `primalObj - dualObj = Σᵢ yᵢ (Gx)ᵢ + Σⱼ wⱼ (xⱼ + M)`. -/
theorem primalObj_sub_dualObj (x : lp.Λ → ℝ) (y₀ : ℝ) (y w : lp.Λ → ℝ)
    (hnet : ∑ i, x i = lp.nTarget)
    (heq : ∀ j, y₀ + ∑ i, lp.G i j * y i + w j = lp.t j) :
    lp.primalObj x - lp.dualObj y₀ w
      = ∑ i, y i * lp.Gx x i + ∑ j, w j * (x j + lp.M) := by
  have ht : lp.primalObj x = ∑ j, (y₀ + ∑ i, lp.G i j * y i + w j) * x j := by
    unfold primalObj; exact Finset.sum_congr rfl (fun j _ => by rw [heq j])
  have hcross : ∑ j, (∑ i, lp.G i j * y i) * x j = ∑ i, y i * lp.Gx x i := by
    unfold Gx
    simp_rw [Finset.sum_mul, Finset.mul_sum]
    rw [Finset.sum_comm]
    exact Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => by ring))
  rw [ht]
  simp_rw [add_mul]
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib, ← Finset.mul_sum, hnet, hcross]
  unfold dualObj
  simp_rw [mul_add]
  rw [Finset.sum_add_distrib, ← Finset.sum_mul]
  ring

/-- **Weak duality.** -/
theorem weak_duality {x : lp.Λ → ℝ} {y₀ : ℝ} {y w : lp.Λ → ℝ}
    (hx : lp.PrimalFeasible x) (hy : lp.DualFeasible y₀ y w) :
    lp.dualObj y₀ w ≤ lp.primalObj x := by
  have h := lp.primalObj_sub_dualObj x y₀ y w hx.1 hy.1
  have h1 : 0 ≤ ∑ i, y i * lp.Gx x i :=
    Finset.sum_nonneg (fun i _ => mul_nonneg (hy.2.1 i) (hx.2.1 i))
  have h2 : 0 ≤ ∑ j, w j * (x j + lp.M) :=
    Finset.sum_nonneg (fun j _ => mul_nonneg (hy.2.2 j) (by linarith [hx.2.2 j]))
  linarith

/-- Duality gap `|primal − dual|` of a primal/dual pair. -/
def duality_gap (x : lp.Λ → ℝ) (y₀ : ℝ) (w : lp.Λ → ℝ) : ℝ :=
  |lp.primalObj x - lp.dualObj y₀ w|

/-- The LP active set of a dual vector: constraints with positive shadow price. -/
def active_set (y : lp.Λ → ℝ) : Set lp.Λ := {i | 0 < y i}

/-- The Frobenius-positivity constraint `i` is tight at `x`. -/
def tight (x : lp.Λ → ℝ) (i : lp.Λ) : Prop := lp.Gx x i = 0

end OperatorSelectionLP

/-- **Finite LP strong-duality hypothesis** for a specific operator-selection
    LP: there is a primal-feasible `x` and a dual-feasible `(y₀, y, w)` with
    zero duality gap — i.e. an optimal pair, certified (Schrijver §7.2: a
    feasible, bounded finite LP has one).

    The certificate is data, but it is not free: feasibility and zero gap
    together make both points optimal, and an LP with no optimum (infeasible
    or unbounded) has **no** instance.  Complementary slackness is a theorem
    below (`complementary_slackness`), not a field.

    **What changed (2026-11-20).**  Formerly `dualityGapZero` was
    `|primal_obj - dual_obj| = 0` on two instance-chosen reals, and
    `complementarySlackness` was `λ ∈ active_set ↔ tight λ` on two
    instance-chosen predicates; the instance `primal_obj = dual_obj = 0`,
    `active_set = ∅`, `tight = False` satisfied both for every index type.
    The iff is moreover **not** a consequence of strong duality: only
    `active → tight` is.  The converse is strict complementarity
    (Goldman–Tucker), which holds for *some* optimal pair, not for every one;
    it is carried separately by `HasStrictComplementarity`. -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986
class HasFiniteLPDuality (lp : OperatorSelectionLP) : Type where
  /-- Optimal primal point. -/
  x : lp.Λ → ℝ
  /-- Optimal dual multiplier of the net constraint. -/
  y₀ : ℝ
  /-- Optimal dual multipliers of the Frobenius constraints (shadow prices). -/
  y : lp.Λ → ℝ
  /-- Optimal dual multipliers of the box constraints. -/
  w : lp.Λ → ℝ
  primal_feasible : lp.PrimalFeasible x
  dual_feasible : lp.DualFeasible y₀ y w
  /-- Strong duality (Schrijver §7.2). -/
  dualityGapZero : lp.duality_gap x y₀ w = 0

/-- **Strict complementarity** (Goldman–Tucker) of the certified optimal pair:
    a Frobenius constraint carries a positive shadow price iff it is tight.
    Not a consequence of `HasFiniteLPDuality`; Goldman–Tucker guarantees that
    *some* optimal pair has it. -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986, §7.9
class HasStrictComplementarity (lp : OperatorSelectionLP) [d : HasFiniteLPDuality lp] :
    Prop where
  strict : ∀ i, i ∈ lp.active_set d.y ↔ lp.tight d.x i

namespace HasFiniteLPDuality

/-! ### No global instance — and why the two that were here proved `False`

This namespace used to carry

```lean
axiom schrijver_strong_duality :
    ∀ (lp : OperatorSelectionLP), lp.duality_gap = 0
axiom schrijver_complementary_slackness :
    ∀ (lp : OperatorSelectionLP) (lam : lp.Λ),
      lam ∈ lp.active_set ↔ lp.tight lam
```

plus a `schrijverModel` building a `HasFiniteLPDuality lp` from them for any
`lp`. **Each axiom independently made the library inconsistent.**

`OperatorSelectionLP` carries `primal_obj` and `dual_obj` as *arbitrary,
independent* reals — it has no feasibility, boundedness or optimality data at
all — and `duality_gap` is **defined** as `|primal_obj − dual_obj|`. So the
first axiom asserts that any two reals are equal:

```lean
def badLP : OperatorSelectionLP where
  Λ := Empty; finite := by infer_instance
  primal_obj := 0; dual_obj := 1
  active_set := ∅; tight := fun _ => True

theorem strong_duality_axiom_is_inconsistent : False := by
  have h : badLP.duality_gap = 0 := schrijver_strong_duality badLP
  simp [OperatorSelectionLP.duality_gap, badLP] at h
```

The second is separately inconsistent for the same reason: `active_set` and
`tight` are independent fields, so an LP with an empty active set and a
universally-true tightness predicate refutes the iff. Both proofs compiled,
with `#print axioms` naming one axiom each.

**The mathematics is not at fault — the transcription is.** Schrijver §7.2
holds for a *bounded and feasible* LP at its *optimum*. Those hypotheses were
dropped, and `OperatorSelectionLP` does not even carry the fields needed to
state them, so the axioms quantified over structures for which the theorem is
simply false. Same shape as the JSJ/Thurston case (PR #4774): a correct
citation attached to a statement broader than the cited result.

**The class shape was right but its content was not** (corrected 2026-11-20:
the fields still related instance-chosen numbers, see `HasFiniteLPDuality`). The module docstring above says
— *"The class is purely a hypothesis carrier."* Taking `HasFiniteLPDuality lp`
as an instance hypothesis for a *specific* `lp` is the correct §3b-cond
pattern, and `theorem_3_via_class` / `theorem_1_via_class` below consume it
correctly. What was wrong was manufacturing that hypothesis for free, for
every `lp`, via two false axioms. Removed, not completed: a caller must now
supply the instance for their own LP, which is where the real LP-theory
obligation belongs.

Follow-up (bean `qou-7t1n`): to state Schrijver honestly, `OperatorSelectionLP`
needs its constraint data plus feasibility/boundedness/optimality predicates,
and the duality result should be conditional on those. That is a genuine
modelling task, not a transcription fix, and is deliberately not attempted
inside an unsoundness repair. -/

/-- Theorem 3 of `prop:confinement-nf-partial-proof`: the certified optimal
    pair has zero duality gap (a projection: this *is* the hypothesis). -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986
theorem theorem_3_via_class
    (lp : OperatorSelectionLP) [hyp : HasFiniteLPDuality lp] :
    lp.duality_gap hyp.x hyp.y₀ hyp.w = 0 :=
  hyp.dualityGapZero

/-- **Complementary slackness, derived** (Schrijver §7.4): at the certified
    optimum a constraint with positive shadow price is tight.  Proved from
    feasibility and zero gap via `primalObj_sub_dualObj`; not an axiom. -/
theorem complementary_slackness
    (lp : OperatorSelectionLP) [hyp : HasFiniteLPDuality lp] (i : lp.Λ)
    (hi : i ∈ lp.active_set hyp.y) : lp.tight hyp.x i := by
  have hgap := hyp.dualityGapZero
  unfold OperatorSelectionLP.duality_gap at hgap
  have h := lp.primalObj_sub_dualObj hyp.x hyp.y₀ hyp.y hyp.w
    hyp.primal_feasible.1 hyp.dual_feasible.1
  rw [abs_eq_zero.mp hgap] at h
  have hy := hyp.dual_feasible.2.1
  have hG := hyp.primal_feasible.2.1
  have h1 : 0 ≤ ∑ k, hyp.y k * lp.Gx hyp.x k :=
    Finset.sum_nonneg (fun k _ => mul_nonneg (hy k) (hG k))
  have h2 : 0 ≤ ∑ j, hyp.w j * (hyp.x j + lp.M) :=
    Finset.sum_nonneg (fun j _ =>
      mul_nonneg (hyp.dual_feasible.2.2 j) (by linarith [hyp.primal_feasible.2.2 j]))
  have hsum : ∑ k, hyp.y k * lp.Gx hyp.x k = 0 := by linarith
  have hterm := (Finset.sum_eq_zero_iff_of_nonneg
    (fun k _ => mul_nonneg (hy k) (hG k))).mp hsum i (Finset.mem_univ i)
  have hyi : 0 < hyp.y i := hi
  exact (mul_eq_zero.mp hterm).resolve_left (ne_of_gt hyi)

/-- Theorem 1 (Wedderburn maximizer in active set) of
    `prop:confinement-nf-partial-proof`: a tight constraint lies in the active
    set.  This is the *converse* of complementary slackness and does **not**
    follow from strong duality; it is conditional on strict complementarity of
    the certified pair (`HasStrictComplementarity`). -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986
theorem theorem_1_via_class
    (lp : OperatorSelectionLP) [hyp : HasFiniteLPDuality lp]
    [sc : HasStrictComplementarity lp]
    (max_pole : lp.Λ) (h_tight : lp.tight hyp.x max_pole) :
    max_pole ∈ lp.active_set hyp.y :=
  (sc.strict max_pole).mpr h_tight

end HasFiniteLPDuality

end QOU.BraidKnot
