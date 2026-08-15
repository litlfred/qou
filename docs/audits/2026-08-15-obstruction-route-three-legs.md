# The obstruction route across the three Millennium legs — what it can and cannot decide

**Date:** 2026-08-15
**Branch:** `claude/agent-obstruction-spaces-kxl3pg` · **PR:** [#5116](https://github.com/litlfred/qou/pull/5116)
**Beans:** `qou-uynz`, `qou-nhso`, `qou-rm42`, `qou-qllz`, `qou-9a7h`, `qou-i140`,
`qou-0bmx`, `qou-iz5k`, `qou-2xor`, `qou-n975`

## The question

Suppose `q-NS`, `q-Collatz`, `q-P≠NP` were **false**. What would the
counterexample be, and can we exclude it — is the obstruction space
zero-dimensional, or is the obstruction non-zero?

## The answer

**Neither disposition decides anything.** The obstruction space is
*one*-dimensional (`thm:qou-obstruction-reduction`) and the class
`χ(A) = -6` is non-zero — and the several restrictions of `κ₀` carry
**different verdicts at the same time**. The class is shared; the verdicts
are not; the shared class transfers nothing between legs.

The decisive pair, both from the corpus:

| Restriction | Verdict at `χ(A) = -6` | Source |
|---|---|---|
| Collatz even-branch, Kummer level 2 | **vanishes** (`2 ∣ -6`) | `qcollatz_kummer_removable_of_chi_neg_six`, proved |
| resolution-tree residue at `q₀` | **non-zero** (`q₀` strictly non-torsion, no finite level applies) | `QouPNeqNp.chiResidual_ne_zero` |

Vanishing and non-vanishing, same class, simultaneously, with no
inconsistency — because vanishing is **level-indexed**
(`kappa_vanishes : ℕ → Prop`), not a proposition.

## What was proved (sorry-free, `lean`-direct exit 0, no `sorryAx`)

**`QOU.Information.ObstructionVerdictCap`** — carries three *distinct* Props
plus an explicit named `SingleVerdict` hypothesis; proves what collapsing the
verdicts would cost (q-Collatz ⟺ q-NS regularity ⟺ `¬(P ≠ NP)`), then refutes
the hypothesis from the table above (`single_verdict_refuted_by_counter_model`).

**`QOU.Information.SkeinCounterfactual`** — the counterfactuals, as
contrapositives of the bridge's descent lemmas:

- `not_descent_of_not_halts` — a q-Collatz counterexample refutes **every**
  descent measure on every forward-invariant cone containing it.
- `not_len_nonincreasing_of_blowsUp` — a q-NS blow-up witness refutes every
  monotone Lyapunov filtration on that orbit.
- `not_orbit_descent_of_counterexample` — a counterexample on **either** leg
  kills the *shared* orbit-descent ingredient of
  `regular_and_halts_of_len_orbit_descent`, hence the common route to the
  other. The two walls do not fail independently *as proof routes*.
- `not_halts_of_blowsUp` — within **one** system with a periodic normal form,
  an orbit of unbounded filtration cannot reach it: boundedness and descent are
  coupled questions *of one instance*.

**Scope, stated sharply because an earlier revision got it wrong.** These
lemmas fix one `sys` and one `P`. They do **not** identify a Navier–Stokes
singularity with a q-Collatz divergence, because the corpus instantiates the two
legs as *different systems* — `qCollatzSystem` (whose `len` is a caller-supplied
parameter) versus `vortexReductionSystem`, on which `BlowsUp` is outright
unsatisfiable since `vortexReductionSystem_regular` proves it regular. "Three
predicates on one shared object" means one shared **type**; the theorems
quantify over one **value** of it. See the third correction below.

The P-vs-NP direction already existed sorry-free upstream
(`no_horizon_cost_of_polyObservable`).

## Defects found and fixed

1. **The barrier was flagged on one leg of three.** A corpus-grep over
   `content/` and `docs/` found the algebrization / genericity caveat attached
   exclusively to P-vs-NP; **no** equivalent argument, under any wording,
   on Collatz or NS. Caveats added to both. The NS leg was worse than
   unflagged: `ns-kummer-specialisation.md` proves *cofinite* non-vanishing and
   presents it as establishing a persistent obstruction — precisely the
   inference `ObstructionGenericity.lean` exists to prune.

2. **Proportionality was stated as derived in one block and conjectural in
   another.** `rem:qou-obstruction-millennium-specializations` read *"the
   one-dimensionality of `HH²` means these three evaluations are
   proportional"*; `conj:qou-p-neq-np` reads *"the proportionality of the four
   evaluations is part of the conjecture, not a consequence of it."* The
   latter is correct — one-dimensionality of the target constrains the class,
   not the images of three different restriction maps into three different
   groups — and the counter-model above settles it concretely. Corrected.

3. **A Lean docstring contradicted a result the corpus cites.**
   `SkeinHorizonLowerBound.lean` justified its lemma with *"an algebraic
   observation (the Jones polynomial / Markov trace) is an efficiently-evaluable
   object"*. Exact Jones evaluation at non-torsion `q` is `#P`-hard
   (`[jaeger1990]`, restated in `conj:qou-p-neq-np`), and `q₀` is strictly
   non-torsion. The lemma is fine — it is hypothetical in `PolyObservable` —
   but the stated reason was wrong. Replaced with the genericity argument,
   which is the one that actually bites.

4. **Six barrier references were missing from the bibliography.**
   Aaronson–Wigderson and Bürgisser–Ikenmeyer–Panova were named in **six** Lean
   docstrings with no `references.ts` entry — a live `-- Ref:` discipline
   violation independent of this work. Added, with Razborov–Rudich,
   Baker–Gill–Solovay, Mulmuley–Sohoni, and Grochow–Kumar–Saks–Saraf (the
   algebraic-natural-proofs barrier, sharper than algebrization for a
   *polynomial* separating invariant).

5. **The millennium-unification table mixes two inference patterns.** Five rows
   run *hypothetical cost exceeds budget ⇒ drift forbidden ⇒ `δ = 0` ⇒
   conjecture holds*. The Navier–Stokes row has **no `δ` in its cost column**:
   `𝒵_q ≍ ε^{-4/3}` is a fixed rate, the inequality is (per its own source
   block) "automatic", and the conclusion is that the event **occurs**. Both
   patterns are individually coherent; they are not the same argument, and the
   block's unifying sentence — *"translating the classical statement into the
   vanishing of this drift"* — does not cover the NS row. Scoped, without
   touching the row's mathematics.

## Non-defects — do not re-raise

**The trichotomy block does not contradict the reduction theorem.**
`rem:skein-filtration-trichotomy` says *"the halting set is undecidable, hence
not cut out by any ideal"*, which reads at first like a denial of the
obstruction framing. It is not. "The halting **set** is not cut out by an ideal"
is a statement about a *subset of states*; "`κ_C = 0` ⟺ every element
converges" is a single *truth-value* equivalence. These are logically
independent — a scalar can encode the truth of a `∀`-statement while the
underlying set is non-algebraic. Two separate agent passes in this session
raised this as a contradiction; both were making the pointwise-vs-`∀` conflation
described below. Recorded here so a third does not.

**No non-polynomial escape hatch exists in the corpus.** Every proposed
obstruction reduces to the integer `χ(A) = -6` or to finite-place data. The two
candidates that might escape do not: the depth-`ω` grade's carrier `κ̂` is
**never defined anywhere in the corpus** (two occurrences, both inside one
remark, no construction, no Lean sibling), and the block itself calls the
statement *"a re-grading, not a new theorem"*; the motivic Galois character's
own proof sketch reduces non-triviality at `p` to `-6 ≢ 0 mod p`. Scope-(a) per
candidate — no proved invariant forbids a non-polynomial obstruction from
existing, only these particular ones from being it.

## Retraction record

An earlier revision of this branch (commits `4c9c02cd`, `54177c7d`) asserted
that the corpus was internally inconsistent — that the shared class plus the
three faithfulness claims "predict q-Collatz is false, contradicting
`conj:q-collatz`". **Retracted** in `d6e8425b`; correction records sit in both
Lean module docstrings.

Two distinct errors, one root cause:

- modelling a **level-indexed family** `kappa_vanishes : ℕ → Prop` as a single
  shared `Prop`; and
- applying the proportionality claim to **q-Collatz**, which that claim's own
  scope (RH / NS / BSD / P-vs-NP) excludes.

A third instance of the same root cause was caught in the same review: a
`SkeinCounterfactual` docstring claimed "the type mismatch alone bars the
route", derived from `no_scalar_faithful_to_halts`. That theorem attacks
**pointwise** faithfulness, `∀ P, v ↔ Halts P`. Every corpus claim is instead
scalar ⟺ a *single universally-quantified* proposition, and a scalar is
faithful to that trivially. Re-scoped to (a).

### Second correction: the cross-leg transfer was vacuous as first stated

The cross-leg transfer (`not_halts_of_blowsUp` — "a q-NS blow-up witness *is* a
q-Collatz divergence witness") was first written with the hypothesis
`step normalForm = normalForm`. That hypothesis is not merely restrictive; it is
**provably false** for the corpus's q-Collatz system. The `QCollatz` class
carries both

```
attractor_period_two : C (C attractor) = attractor
attractor_not_fixed  : C attractor ≠ attractor
```

because the attractor is the **2-cycle** `{q⁻¹, 1 + q⁻¹}`, the q-lift of the
classical `{1, 2}`. So the theorem was vacuous on the single instance it was
written for — the honesty caveat in its docstring correctly said the attractor
is a 2-cycle, but drew the wrong conclusion from it ("the cyclic case needs the
orbit-level argument") instead of the right one ("this hypothesis is refutable
here, so the theorem says nothing about q-Collatz").

Fixed by generalising the hypothesis from a fixed point to a **periodic** normal
form, `Function.IsPeriodicPt step p normalForm` with `0 < p` — which
`attractor_period_two` supplies directly at `p = 2`. The argument goes through
unchanged: an orbit that lands in a finite cycle still visits finitely many
states, so its filtration is bounded. The theorem now applies to the system it
was written for.

**Lesson, distinct from the first:** an honesty caveat that names the obstacle is
not the same as checking whether the obstacle *refutes* the hypothesis. "The
attractor is a 2-cycle, not a fixed point" was written down and then not acted
on. When a docstring names a reason the hypothesis might not hold, grep the class
for whether the corpus *proves* it does not.

### Third correction: shared *type* is not shared *instance*

The cross-leg transfer was then narrated as "a q-NS blow-up witness **is** a
q-Collatz divergence witness". False. `not_halts_of_blowsUp` fixes one
`sys : SkeinObservationSystem S V` and one `P : S`, reading both predicates off
the *same* `step`, `normalForm` and `len`. The corpus's two legs are different
instances of that type: `qCollatzSystem` (`step = QCollatz.C`, `len` a free
caller-supplied parameter — the bridge concedes "any ℕ-measure typechecks")
versus `vortexReductionSystem`, the only concrete NS instance, on which the
hypothesis is **unsatisfiable** because `vortexReductionSystem_regular` proves
it regular. The theorem is a coupling *inside* one instance; the prose promoted
it to a coupling *between legs*.

Re-scoped in the Lean header, the content block, and the summary above. The
theorems are unchanged and correct — only the narration was wrong.

**This is the same root cause as the first correction, one abstraction level
up:** shared abstraction mistaken for shared instance, exactly as level-indexed
family had been mistaken for its universal closure.

### Fourth instance of the pointwise-vs-`∀` conflation — in this branch's own prose

Worth recording flatly: while the audit doc's "do not re-raise" section (below)
correctly explains that "the halting set is not cut out by an ideal" (set-level)
is independent of "`κ_C = 0` ⟺ every orbit converges" (truth-value), **this
branch simultaneously wrote that exact invalid inference into
`q-collatz-conjecture.md`** — "hence not cut out by any ideal, so no algebraic
class can be equivalent to it". Three files apart, in one session: the doc
naming the fallacy and the content block committing it. Corrected in the block;
the `SkeinCounterfactual` docstring already carried the refutation
(`∃ v, (v ↔ ∀ P, Halts P)` is trivially inhabited).

**Root cause of the first correction, stated once:** conflating a predicate that
varies over states or levels with the single truth value of its universal
closure. The corpus-grep
checklist was run on the *topic* but not on the *claim shape* — on "what does
the corpus say about obstructions" rather than "does the corpus actually assert
one shared vanishing proposition". The second question is the one that would
have caught it, and it is the question to ask before writing any "X ⟺ Y"
into a durable artifact.

The proofs were sound at every stage; only the interpretation was wrong. Caught
by adversarial review before merge, per the standing critical-distance license.

## Verification

CI auto-triggers are disabled repo-wide (`workflow_dispatch` only), so agent
verification is the gate (AGENTS.md rule 10).

- `lean`-direct **exit 0** on both new files and on the edited
  `SkeinHorizonLowerBound.lean`, against the real import cone. The restored
  `lake-cache` oleans for `QCollatz` / `ComputationalHorizon` were **stale**
  against current source (`QCollatz` had become a `Type`, and
  `reaches_of_descent_of_forward` was unknown); `SkeinObservationBridge` and its
  cone were rebuilt from source before checking.
- `#print axioms` on every new declaration: no `sorryAx` — only `propext`,
  `Classical.choice`, `Quot.sound`.
- Render-QA grep battery clean on all edited math-bearing `.md`: `$`/`$$`,
  braces, `\begin`/`\end`, `\bigl`/`\bigr` balanced; no `\operatorname`; no
  list-parser hijack inside `$$`. All new cite keys resolve in `references.ts`.
- The **pipeline render was not run** — `folio-assistant` is not set up in this
  container — so the math edits are hand-validated, **not** machine-validated.
