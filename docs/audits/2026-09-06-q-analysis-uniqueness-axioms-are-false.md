# The q-analysis uniqueness family: six false axioms, one defect

**Date:** 2026-09-06 · **Beans:** `qou-9yt9` · **PR:** #6933

Six axioms in the q-analysis display siblings assert false propositions.
Each was verified `lean`-direct against the axiom's **verbatim** text,
with `#print axioms` showing the derived `False` depending on exactly
that one axiom and nothing else non-standard — no `sorryAx`.

| # | axiom | file:line | status |
|---|---|---|---|
| 1 | `QDilogarithm.unique_axiom` | `q-dilogarithm-unique.lean:46` | deleted, refuted, registered |
| 2 | `QDilogarithm.unique_up_to_shift_axiom` | `q-dilogarithm.lean:63` | verbatim duplicate of 1 |
| 3 | `QExponential.unique_axiom` | `q-exponential-unique.lean:47` | deleted, refuted, registered |
| 4 | `QExponential.unique_axiom` | `q-exponential.lean:62` | verbatim duplicate of 3 |
| 5 | `QLogarithm.unique_axiom` | `q-logarithm-unique.lean:59` | deleted, refuted, registered |
| 6 | `QDilogarithm.exists_axiom` | `q-dilogarithm-exists.lean:26` | deleted; **repaired** to a real theorem |

None had a consumer outside its own file: each fed only the wrapper
theorem sitting under it.

## The defect

Over-quantification, for the fourth incident class running. Each
structure carries its ambient maps — coproduct, counit, Jackson
derivative, the pentagon's `mul`/`compl`/`div` — as **free function
fields**, and its axioms as proof fields *about those maps*. So the maps
can be chosen to make the axioms hold for **every** value of the
distinguished element:

```
coprod := fun x => (x, x)   ⇒  grouplike, primitive_left, primitive_right
counit := fun _ => c        ⇒  counit_eq_one, counit_eq_zero
D_q    := id                ⇒  flow_invariant
```

Two records then agree on every hypothesised field and differ in the
concluded one.

`QDilogarithm` is starker. The conclusion was about `Li2`, and **the
`pentagon` field does not mention `Li2` at all** — it constrains
`Li2_eval`, a different field, with nothing tying the two. `Li2` is free
data, so no hypothesis about the pentagon could ever have reached it.
That is why the repair concludes about `Li2_eval`: not a weakening, a
correction to the only thing the structure constrains.

`exists_axiom` is the same defect in the carrier rather than the fields:
it quantified over *every* type with an `Add`, including `Empty`, where
`log_q : H` cannot be supplied.

## The refutation was already in the corpus

The counterexample records are not exotic. They are, field for field,
the same shape as the "trivial witness" records the corpus's own
`*-exists.lean` siblings use — `QExponential.exists_in_shuffle_hopf` and
`QLogarithm.exists_in_shuffle_hopf`, each of which says in a comment
that its witness is trivial and the intended Kassel construction is
sharper.

**The existence witness and the uniqueness counterexample are the same
degenerate record.** The corpus contained, in the sibling file next
door, the object refuting its own axiom. Nothing had to be constructed
to find these; something had to be *compared*.

That is the reusable observation. The docstring sweep that closed the
canonicity family in PR #6882 keyed on the author having noticed the
defect and written it down. This one would have been caught by a
narrower question still: **does a structure's own existence witness
satisfy the hypotheses of its uniqueness claim while differing in the
conclusion?** That is mechanically checkable and is a stronger signal
than any shape heuristic tried so far.

## What the citations actually say

- [kassel1995] §III.3 proves grouplikes are **linearly independent** —
  not that they are unique.
- [kassel1995] §IV.3 identifies primitives with a **Lie algebra**, which
  is a statement that primitives are *not* unique in general.

Both are real theorems; neither is the Lean statement that cited it.
Same finding as the SDP family (Alizadeh–Haeberly–Overton needs dual
nondegeneracy, not strict complementarity alone) and the Jones–Markov
axiom (Wenzl's Lemma 3.2 is about a normalised trace).

## The repair

The narrative proofs are **not** obviously wrong. Each takes one step it
asserts rather than proves, and the repair makes exactly that step a
named hypothesis:

| block's narrative proof asserts | hypothesis |
|---|---|
| *"The flow equation on primitives has only the trivial solution"* | `flow_rigid` |
| *"a primitive fixed by `D_q` with trivial counit vanishes"* | `prim_rigid` |
| *"The solution space … is one-dimensional modulo lower-level primitives"* | `pentagon_rigid` |

Each is **kernel triviality about a single element**, from which
two-element uniqueness is *derived* by subtraction. That is what keeps
these clear of the self-assuming projection §3b-cond item 5 forbids: a
hypothesis "any two agree" would be the conclusion; a hypothesis "the
difference vanishes" is a strictly weaker input the proof has to work
with.

The narrative proofs also silently need the ambient maps to be
**additive** — they form `e₁ − e₂` and apply `Δ`, `ε`, `D_q` to it. A
bare carrier type supports none of that, which is the deeper reason the
original encodings could not have been those proofs. Additivity is now
explicit, over `AddCommGroup`.

Result: three theorems, no axioms, in
`QOU/QuantumObservableUniverses/QAnalysisUniqueness.lean`. The gap is
now **visible in the type** instead of hidden in an axiom — discharging
any `*_rigid` needs a graded q-shuffle Hopf algebra, which the corpus
does not have.

Axiom 6 was repairable in substance: over an `AddZeroClass` the type
really is inhabited, proved with no axiom. But the witness is the
all-zero record, so what it establishes is **inhabitation of the
structure**, not the shuffle recursion the prose described. The block's
prose and title are narrowed to match rather than left to imply more
than the Lean says.

## Also fixed

`QExponential` and `QLogarithm` were **inlined in four siblings apiece**.
The 2026-06-09 audit created `QAnalysis.lean` precisely so the
`*-unique.lean` files could import real structures instead of
auto-bound variables, and relocated only `QDilogarithm`; the axioms
refuted here were stated against the copies it left behind. Both are now
in the library and the `*-unique` siblings import them.

## Verification

- Six refutations, `lean`-direct exit 0, verbatim axiom text, each
  `False` depending on exactly one corpus axiom.
- Nine touched Lean files exit 0 with `-DautoImplicit=false -s 65536`.
- Eight new rows in `scripts/lean-axiom-guard.py`, all `clean`.
- `bun run scripts/run-validate.ts content/quantum-observable-universe`
  exit 0 against pinned platform `428ca5c`; the 9 reported issues are
  all pre-existing and none is in a file touched here.
