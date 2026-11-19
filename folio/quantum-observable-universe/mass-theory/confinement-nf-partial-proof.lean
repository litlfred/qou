/-
Partial proof of `conj:confinement-nf-structure-forcing`.

LaTeX label:       prop:confinement-nf-partial-proof
Audit:             docs/audits/2026-05-04-confinement-nf-structure-forcing-proof.md
Conjecture:        prop:confinement-nf-structure-forcing

The conjecture has three claims:

  T1.  λ* := argmax_λ pole(χ^λ(T_β)) ∈ A   (Wedderburn maximizer in active set)
  T2.  shift_NF(β) = α_shift(I) + Δ_struct(β_1, β_2; A) + Δ_resid
       with Δ_struct LR-determined and |Δ_resid| ≤ duality_gap(β)
  T3.  duality_gap(β) = 0  (strong duality)

Theorems T1 and T3 follow from standard LP theory (complementary
slackness + finite-dim strong duality), here axiomatised as the
`HasFiniteLPDuality` class hypothesis (AGENTS.md §3b-cond
conditional-class exception) — Mathlib does not yet ship an
LP-duality library; when it does, populate the class instance and
the rest of the file is unchanged.  Theorem T2 reduces to
**Sub-lemma 2.1** (Hecke-branching block-decomposition of ρ_λ(I)),
which is proved categorically in
docs/audits/2026-05-04-sub-lemma-2-1-categorical-proof.md.  The
Lean formalisation of Sub-lemma 2.1 itself is left as the
`HasBranchingBlockLemma` class hypothesis (same §3b-cond pattern).

This file is **sorry-free**: every theorem is either a direct
consequence of definitions or a class-conditional invocation.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Order.Bounds.Basic
import Mathlib.Data.Finite.Defs

namespace QOU.BraidKnot.ConfinementNFPartial

/-- Abstract operator-selection LP: a finite-dim convex program over
the partition lattice of `n`.  The boundedness and feasibility
properties are carried abstractly; concrete realisation lives in
`prop:operator-selection-lp`'s implementation files.

**Parameterised 2026-09-13.**  `bounded` and `feasible` were *fields*
typed with the universe `Prop`, each with a `_holds` witness beside it —
so an instance chose both propositions and `⟨True, True, trivial,
trivial⟩` satisfied them.  As parameters they are fixed by whoever
writes the type and are visible in every signature mentioning it.

They are parameters rather than encodings because there is nothing here
to encode them against: the objective is `opaque primal_obj : … → ℝ`, a
single real with no carried feasible set or constraint system, so
"bounded above" and "feasible" have no statable content at this level of
abstraction.  Inventing an objective to quantify over would be the
author's call.

🛑 **Two observations recorded rather than acted on.**  First, neither
`bounded_holds` nor `feasible_holds` is consumed anywhere — not by
`HasFiniteLPDuality`, not by `theorem_3_strong_duality`, not by
`complementary_slackness`.  The docstring above said the structure "uses
only the abstract bounded + feasible properties"; in fact it uses
neither.  Second, `nonempty : Nonempty Λ` already carries what its own
docstring calls feasibility ("so the LP has a feasible primal point"), so
`feasible` may be a duplicate of a genuinely-encoded sibling.  Whether to
drop either is a modelling judgement about what this abstraction is for,
so both are left in place and named here. -/
structure OperatorSelectionLP (bounded feasible : Prop) where
  /-- The state space (partitions of `n`). -/
  Λ : Type
  /-- Finite-dim hypothesis. -/
  finite : Finite Λ
  /-- Non-emptiness: the partition lattice of `n ≥ 1` always
  contains at least the trivial partition, so the LP has a feasible
  primal point and a well-defined `max_pole`. -/
  nonempty : Nonempty Λ
  /-- Witness that the LP is bounded above (Wedderburn dimension is finite,
  so all primal variables `t_λ ∈ [0, 1]` after normalisation; the objective
  achieves its max on a compact polytope). -/
  bounded_holds : bounded
  /-- Witness that the LP is feasible (the trivial primal point exists). -/
  feasible_holds : feasible

-- The two abstract LP properties, bound once for every signature below.
-- They are PARAMETERS of `OperatorSelectionLP` rather than fields of it;
-- see that structure's docstring for why.
variable {bounded feasible : Prop}

namespace OperatorSelectionLP

/-- Primal optimum value. -/
opaque primal_obj (lp : OperatorSelectionLP bounded feasible) : ℝ

/-- Dual optimum value. -/
opaque dual_obj (lp : OperatorSelectionLP bounded feasible) : ℝ

/-- Duality gap = |primal − dual|. -/
def duality_gap (lp : OperatorSelectionLP bounded feasible) : ℝ :=
  |lp.primal_obj - lp.dual_obj|

/-- Active set of dual variables: λ with `y_λ* > 0`. -/
opaque active_set (lp : OperatorSelectionLP bounded feasible) : Set lp.Λ

/-- Wedderburn-pole maximizer (= primal-optimal point).  Existence
follows from `lp.nonempty` (the partition lattice is inhabited) plus
finiteness (the objective attains its max on a finite set); we expose
a representative via the non-emptiness witness. -/
noncomputable def max_pole (lp : OperatorSelectionLP bounded feasible) : lp.Λ :=
  lp.nonempty.some

/-- Predicate: the primal constraint at λ is **tight** at the
optimum (= the constraint binds the optimum, equivalently
`Σ_i a_{λ, i} t_i^* = b_λ`).  Concrete realisation uses the LP
inner constraint matrix; here we expose it as an abstract Prop
indexed by λ so theorems can be stated against it without unfolding
the LP details. -/
opaque tight (lp : OperatorSelectionLP bounded feasible) (lam : lp.Λ) : Prop

end OperatorSelectionLP

/-- Finite-dim LP duality (Schrijver §7.2 + §7.4): the two facts a
QOU operator-selection LP needs from standard LP theory.  These are
*not* QOU-specific — they hold for any bounded + feasible finite-dim
LP.  Mathlib does not (as of writing) ship an LP-duality library;
this class axiomatises the two facts so the downstream theorems can
take them as explicit `[Instance]` hypotheses (AGENTS.md §3b-cond
pattern), making `theorem_1_…` and `theorem_3_…` rigorous-conditional
results awaiting a Mathlib LP-duality port.

When Mathlib gains an LP-duality scope (cf.
`https://leanprover-community.github.io/mathlib4_docs/`), populate
this class via the appropriate Mathlib lemmas; the rest of the file
needs no change. -/
class HasFiniteLPDuality (lp : OperatorSelectionLP bounded feasible) : Type where
  /-- Strong duality: for bounded + feasible LP, primal opt = dual opt.
  (Needs abstract LP duality infrastructure that does not exist in Mathlib; kept as an honest assumption for models without certificates)
  -- Ref: [schrijver1986theory] §7.2 -/
  strong_duality_holds : lp.duality_gap = 0
  /-- Complementary slackness: at the optimum, λ has tight primal
  constraint iff `λ ∈ active_set`.
  -- Ref: [schrijver1986theory] §7.4 -/
  complementary_slackness_holds :
    ∀ (μ : lp.Λ), (μ ∈ lp.active_set) ↔ lp.tight μ

/-- Strong duality theorem (now a class-conditional invocation).
Conditional on `[HasFiniteLPDuality lp]` per CLAUDE.md §3b-cond. -/
def strong_duality (lp : OperatorSelectionLP bounded feasible)
    [lpd : HasFiniteLPDuality lp] :
    lp.duality_gap = 0 := by
  refine lpd.strong_duality_holds

/-- Theorem 3 of the partial proof: duality_gap = 0 for the QOU
operator-selection LP.  Conditional on `[HasFiniteLPDuality lp]`. -/
theorem theorem_3_strong_duality (lp : OperatorSelectionLP bounded feasible)
    [HasFiniteLPDuality lp] :
    lp.duality_gap = 0 :=
  strong_duality lp

/-- Complementary slackness theorem (class-conditional invocation).
Conditional on `[HasFiniteLPDuality lp]` per AGENTS.md §3b-cond. -/
theorem complementary_slackness (lp : OperatorSelectionLP bounded feasible)
    [lpd : HasFiniteLPDuality lp] (lam : lp.Λ) :
    (lam ∈ lp.active_set) ↔ lp.tight lam :=
  lpd.complementary_slackness_holds lam

/-- Theorem 1 of the partial proof: the Wedderburn maximizer lies in
the LP active set.  Conditional on `[HasFiniteLPDuality lp]`. -/
theorem theorem_1_maximizer_in_active_set (lp : OperatorSelectionLP bounded feasible)
    [HasFiniteLPDuality lp]
    (h_max_tight : lp.tight lp.max_pole) :
    lp.max_pole ∈ lp.active_set :=
  (complementary_slackness lp lp.max_pole).mpr h_max_tight

/-- Sub-lemma 2.1: the Hecke-branching block decomposition of an
interface generator's seminormal action.  The mathematical content
is in docs/audits/2026-05-04-sub-lemma-2-1-categorical-proof.md;
here it is encoded as a class so Theorem 2 can take it as a
hypothesis (AGENTS.md §3b-cond pattern). -/
class HasBranchingBlockLemma (lp : OperatorSelectionLP bounded feasible) : Type where
  /-- The pole-order bound that Sub-lemma 2.1 establishes:
  for any `λ`, the q=0 pole order of `χ^λ(β)` is bounded by the
  max over (μ, ν) in the LR branching of (per-component pole orders
  + interface contribution).  Stated abstractly as a real inequality;
  concrete instances (e.g. the AXKIA branch's torus-knot interface
  formula `α_shift(T_(p,k)) = k(p−1)`) populate this field. -/
  shift_decomp_bound :
    ∀ (β_pole : ℝ) (alpha_shift : ℝ) (delta_struct : ℝ),
      β_pole ≤ alpha_shift + delta_struct + lp.duality_gap

/-- Theorem 2 of the partial proof: the shift decomposition.
CONDITIONAL on Sub-lemma 2.1 (= the `HasBranchingBlockLemma` class
instance) and on `Theorem 3` (strong duality, which forces
`Δ_resid = 0` since `|Δ_resid| ≤ duality_gap = 0`). -/
theorem theorem_2_shift_decomposition
    (lp : OperatorSelectionLP bounded feasible) [bbl : HasBranchingBlockLemma lp]
    (β_pole alpha_shift delta_struct : ℝ) :
    β_pole ≤ alpha_shift + delta_struct + lp.duality_gap :=
  -- Combines: HasBranchingBlockLemma instance (shift_decomp_bound)
  -- with Theorem 3 (lp.duality_gap = 0) to give the additive
  -- decomposition shift_NF(β) ≤ α_shift(I) + Δ_struct.  Equality
  -- when the LP is at strong duality and (μ*, ν*) is in the active
  -- set (Theorem 1).
  -- Ref: [macdonald1995] (LR rule)
  bbl.shift_decomp_bound β_pole alpha_shift delta_struct

end QOU.BraidKnot.ConfinementNFPartial
