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

---

# Addendum: the vacuous class, and a probe for it

Five further axioms came out of this tranche that are **not false** —
they are *provable*, and were sitting as axioms anyway.

| axiom | file | closes by |
|---|---|---|
| `chart_glue_from_spectrum` | `spectral-chart-correspondence.lean` | `⟨_, rfl⟩` |
| `su2_emergence` | `su2-emergence.lean` | a constant-field record |
| `ordering_extends` | `ordering-jet-compatibility.lean` | `exact hab` |
| `antipode_involution` | `frobenius-antipode-lean-stub.lean` | `rfl` |
| `markov_trace_antipode_invariant` | `frobenius-antipode-lean-stub.lean` | `rfl` |

## Why this class is worse to live with, and easier to fix

A false axiom announces itself the moment anyone looks for a
counterexample. That is how eighteen have now been found in this corpus.
A vacuous axiom announces nothing: nothing unsound follows from it, so
no downstream contradiction ever surfaces, and it can stand for years
cited as Tannaka–Krein reconstruction or as *"the wall — the categorical
model of `O_q(P¹)` is not in Mathlib"*.

`ordering_extends` is the sharpest instance the arc has produced:

```lean
axiom ordering_extends (k : ℕ) (a b : MonomialBasis)
    (hab : degLex a b) : degLex a b
```

The conclusion **is** the hypothesis, and `k` — the level index the
claim is entirely about — does not occur in the statement.

## The shared symptom: the docstring carries what the type does not

In every one of the five, the prose describes content absent from the
type:

- `SpinDecomposition` has no simplicity condition, no injectivity of
  `simpleObj`, no dimension field — so *"simple objects indexed by
  half-integer spin labels with `dim = 2j+1`"* is nowhere in the
  statement.
- Nothing in `chart_glue_from_spectrum` mentions a chart, a transition
  map, or `P_q(V)`.
- `ordering_extends`'s jet embedding `ℓ_n` appears in no binder.
- The antipode pair's *"sign-twist depending on the parity of the braid
  word"* cannot appear in a statement whose two sides are the same term,
  because `antipodeS = id` on this file's model — which the file says
  out loud, and which the theorem two declarations above already relies
  on. An axiom was sitting beside a theorem with the same justification.

The walls those docstrings describe are real. None of these axioms was
standing at one.

## The probe

[`scripts/lean-axiom-provability-probe.py`](../../scripts/lean-axiom-provability-probe.py)
rewrites each axiom into a theorem with a short tactic block and
compiles it. **A PASS is a proof, not a heuristic** — sound in the
direction that matters. A FAIL is evidence of nothing; the tactic list is
deliberately short, because a long one turns the probe into an unbounded
proof search whose failures say nothing.

Full run over `content/`: **122 axioms probed, 3 provable** — the three
in the table not already found by hand. All five are now theorems.

The risk audit could not have found any of them, and this is structural
rather than a tuning failure: it ranks by the *shape* that made the five
SDP axioms **false**, and a vacuous axiom has no such shape. The two
tools are complements, not overlapping heuristics.

## The probe's own blind spot, asserted rather than hidden

It catches `chart_glue_from_spectrum` and **not** `su2_emergence`.
Closing the latter needs a witness record built field by field; after
`⟨?sd, rfl⟩` the metavariable is a whole structure and unification
cannot invent one.

Rather than pad the tactic list until it lands — a list tuned to its own
fixtures measures itself — the miss is recorded as `SELFTEST_KNOWN_MISS`
and the self-test **requires it to stay unprovable**. If a future tactic
addition catches it the test fails and says to move the row, so coverage
can never grow silently.

---

# Addendum 2: an axiom that shadowed a real definition

A third class, one instance, in
`climax-volume-mass/vertex-algebra-relations.lean`:

```lean
axiom AlgElement.zero {n : ℕ} : AlgElement (HeckeGen n) ℝ
```

`UGB.GrobnerShirshov.AlgElement.zero` is a real `def`
(`UGB/GrobnerShirshov/Elem.lean:105`) with a real `isZero_zero` theorem,
and it was **already in scope** through this file's `HeckeGS` import.

Measured by compilation, not inferred: inside `namespace
QOU.VertexAlgebra` the bare name resolved to the **axiom**, whose type
`{n : ℕ} → AlgElement (HeckeGen n) ℝ` differs from the library's
`{G} → {k} → [Ring k] → AlgElement G k`, so `isZero_zero` did not apply
to it. Deleting the axiom makes the name resolve to the library
definition and the `isZero` example goes through.

**The consequence was not cosmetic.** `markov_nondegenerate` concludes

```lean
    (∀ g, MarkovTrace hp (AlgElement.mul f g) = 0) → f = AlgElement.zero
```

Under the axiom that reads *"`f` equals a fixed unknown element"*, not
*"`f` is zero"* — a **different proposition** from the one it looks like,
which is a failure mode neither of the other two classes covers. It is
not false and it is not vacuous; it is *mis-referring*.

## What remains axiomatised there, and why it is a third thing again

`MarkovTrace`, `AlgElement.mul` and `AlgElement.embed_succ` have no
library counterpart and stay axiomatised. Claims about them —
`markov_stabilisation`, `markov_nondegenerate`, `observability`,
`first_chern_vanishes`, `descartes_trace`, `self_dual_curvature` — are
**specifications, not theorems**: with an opaque operator there is no
definition to unfold, so they can be neither proved nor refuted. In
particular `descartes_trace : MarkovTrace hp (singleton []) = -6` is
consistent for the trivial reason that `MarkovTrace` is unconstrained.

No inconsistency among them was established here, and no claim is made
that there is none.

## The scan, and why it could not have found this

A corpus scan for axiom names colliding with a definition reports
**16** matches raw. Eight are English prose inside block comments —
`and`, `for`, `is`, `it`, `of`, `that`, `to`, `with` at the start of a
wrapped line — the exact trap
`lean-axiom-degenerate-risk-audit.py` documents and strips. With comments
stripped and the search restricted to *importable* library modules the
figure is **6**, and checking those files' imports shows **none of them
imports a module carrying the colliding name**: same name, different
file, no path between them. So the confirmed count corpus-wide is **one**.

**And the scan cannot see the one true positive.** `AlgElement.zero` is
declared upstream as `def zero` inside `namespace AlgElement`, so a
line-matching search for the name `AlgElement.zero` never matches it. A
scan of this shape is structurally blind to exactly the case that
motivated it, which is why it is recorded here rather than shipped as a
tool: settling any candidate needs a compile, and the compile is what
settled this one.

---

# Addendum 3: an axiom that collapsed its own type, and what is left

## `degree_filtered_reduction_correct` — stronger than false

```lean
axiom degree_filtered_reduction_correct
    {G} {k} [Ring k] [DecidableEq G]
    (ord) (sys) (hgs : IsGrobnerShirshovBasis G k ord sys)
    (f nf_full nf_filtered : AlgElement G k)
    (h_full : ReducesToNF ord sys f nf_full)
    : nf_full = nf_filtered
```

`nf_filtered` is bound and never mentioned again — not in a hypothesis,
not in `h_full`, nowhere but the conclusion. The axiom therefore says
`nf_full = X` for **every** `X`, and the degree restriction it is named
for lives in a **comment** beside the binder.

From the axiom alone, any single reduction makes every element of
`AlgElement G k` equal to every other
(`degree_filtered_reduction_collapses_type`, which needs no witness
because the two applications share one `nf_full`). An axiom of that
shape proves anything about the algebra it quantifies over.

It is the purest instance of the root cause the whole arc keeps finding:
a binder that should have been tied is left free. Here it is not merely
under-constrained — it is *unconstrained*.

## A verification note that cost real time

This is a **UGB library** file, and the restored olean cache carries only
six UGB modules. `Flatness`, in `JetOrder`'s own import list, was absent,
so `lean`-direct failed with

```
object file '.../UGB/GrobnerShirshov/Flatness.olean' of module
UGB.GrobnerShirshov.Flatness does not exist
```

which reads like a real error and is not one. Building that single
module into the session overlay first is enough; the file then exits 0.
`lean-content-sweep.sh` and `lean-library-sweep.py` do not cover UGB
(AGENTS.md says so), so a UGB library file needs its cone built by hand.

## What remains flagged, and why each is left standing

Four, none of which is a refutation the corpus can currently support:

| axiom | why it stays |
|---|---|
| `markov_trace_unique_axiom` | **Resists refutation.** The braid relation forces all generators equal in any commutative carrier, so a counterexample needs a genuine `H₃(q)` — and there **cyclicity pins** the apparently-free direction: `tr(σ₁σ₂σ₁) = tr(σ₂σ₁²) = h·z² + z`. The docstring's *"field set is too weak"* is about provability, not falsity. |
| `markov_nondegenerate` | Opaque-operator class: `MarkovTrace` and `AlgElement.mul` are themselves axioms in the same file. |
| `descartes_trace` | Same. `MarkovTrace hp (singleton []) = -6` is consistent for the trivial reason that `MarkovTrace` is unconstrained. |
| `protonExample_archimedean_agreement_axiom` | Same shape: `protonHabiroTrace` is `opaque`, so an axiom pinning its evaluation to a decimal literal can be neither proved nor refuted. |

**The opaque-operator group is a disposition question, not a refutation
task.** With no definition to unfold, these three are *specifications*:
they say what the operator must satisfy, and nothing can check that
they do. The options are to define the operator (large), to demote the
claims to a conditional class carrying them as hypotheses (medium, and
the §3b-cond pattern already used elsewhere in this corpus), or to leave
them as specifications with that status stated at each site (small).
Choosing among those is an authorial call about how much of the Hecke
machinery to formalise, and is not made here.

---

# Addendum 4: two more vacuous, and three things the probe cannot see

`antipode_anti_hom` (`frobenius-antipode-lean-stub.lean`) and
`strong_multiplicativity_on_generators`
(`UGB/GrobnerShirshov/StrongMultiplicativity.lean`) are both provable and
were both axioms.

The second is the plainest instance of the whole arc:

```lean
axiom strong_multiplicativity_on_generators … :
    ∀ (f _g : AlgElement G k), bialg.comul f = bialg.comul f
```

`X = X`, closed by `rfl`, under twenty lines of docstring citing
[fred2005, Thm 4.12] and explaining why the result "requires"
axiomatisation. The file says so on the conclusion line —
*"placeholder for the proper AlgElement multiplication"* — with the real
statement written beneath it as a comment.

`antipode_anti_hom` is subtler: on that file's scalar-coefficient model
`antipodeS = id` and `heckeMul` is real multiplication, so
`S(ab) = S(b)S(a)` collapses to `mul_comm`.

## Three limits of the provability probe, all measured

**1. A fixed tactic list cannot do case-specific unfolding.**
`antipode_anti_hom` needs `antipodeS` and `heckeMul` unfolded, and both
are plain `def`s with no `@[simp]`. Measured on a minimal reproduction:
`rfl`, `trivial`, `simp`, `simp_all`, `simp [mul_comm]`,
`constructor <;> ring`, `decide` and `aesop` **all fail** — `aesop`
reporting *"made no progress"*. Those tactics were added after the miss
and then **reverted**: they cost runtime and caught nothing. Knowing
which definitions to unfold is case-specific, so this class is out of
reach rather than one tactic away. Recorded as the second asserted blind
spot, alongside the witness-record class (`su2_emergence`,
`categorical_jet_prolongation`).

**2. A missing olean is indistinguishable from "not provable" — and it
cost a real finding.** The first corpus run reported 122 probed / 3
provable and did **not** find
`strong_multiplicativity_on_generators`. It could not: `Flatness`, in
that UGB subtree's import closure, was absent from the restored cache,
so the file failed to compile for environment reasons and the probe
recorded a FAIL. After building that one module into the overlay, the
same axiom came back `PROVABLE` on the next run. **A FAIL from this
probe means "did not compile with a proof", not "is not provable".**

**3. The self-test rotted, in exactly the way this branch had already
fixed once.** Its fixtures were read from `--selftest-rev`, so as soon as
the fixtures' own axioms were converted the test went red with
`SELFTEST FAIL: ... not parsed at <rev>` — the same failure the risk
audit had that morning, reading the SDP axioms from `origin/main`. The
fix is the same in kind and better in detail: each fixture row now pins
an **immutable commit sha**, which cannot rot; a shallow clone lacking
the object reports `SELFTEST ERROR` rather than passing silently.

Making the same mistake twice in one day, hours after documenting it, is
worth recording as plainly as the findings are.
