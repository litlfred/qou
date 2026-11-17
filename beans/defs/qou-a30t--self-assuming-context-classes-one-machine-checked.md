---
# qou-a30t
title: 'Self-assuming context classes: one machine-checked criterion for four ledger patterns (46 live genuine entries)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T12:02:39Z
updated_at: 2026-10-04T15:13:54Z
parent: qou-6qbv
---

## The criterion (2026-09-12, PR #7208)

`QOU/ProofHygiene/SelfAssumingContexts.lean` — Mathlib-only, no QOU imports, citable from
anywhere in the tree. Sorry-free; of its 16 declarations **14 depend on no axioms at all**
and 2 only on `propext`.

  `Contentless K C  :=  Nonempty K ↔ C`

The class is inhabited exactly when the conclusion holds, so instantiating it is logically
identical to assuming `C` — **however the conclusion is extracted**: by projection, by
application, or by a chain of either. That "however" is what lets one criterion cover
shapes that four separate detectors see differently.

| ledger pattern | shape | theorem |
|---|---|---|
| `field-projection`, `exact-field-projection` | a field of the conclusion's own type | `selfAssuming_contentless` |
| `tuple-projection` | several conclusions bundled, one projected | `tuple_contentless` |
| `decoy-hypothesis` | `⟨P : Prop, hP : P, impl : P → C⟩`, extracted by **application** | `decoy_contentless` |

**46 live `genuine` entries** between them, measured against the recorded `file_sha` so
stale verdicts are excluded (bean `qou-wsx3`).

`selfAssuming_contentless` is what AGENTS.md §3b-cond item 5 calls a *"vacuous
self-assuming projection"* — stated there in prose since the rule was written, now
machine-checked.

## The test a reviewer can actually run

`not_contentless_of_witness` — **exhibit an instance without already having the
conclusion**, and the class carries something. `conditional_not_contentless` runs it on the
shape that should pass: a genuine §3b-cond `ConditionalContext H C` carries the implication
and *not* the antecedent, so at `H = C = False` it is inhabited while the conclusion fails.

The operative question, and it has a definite answer: **does the class supply its own
antecedent?**

## Why the existing detector misses the decoy shape

`proof-no-self-assuming-projection` looks for a field *of the conclusion's type* being
projected. `DecoyContext` has no such field — it has `P → C`, and `ctx.impl ctx.active` is
an **application**. A field-projection scan is structurally blind to it, which all 13 decoy
ledger entries say in nearly identical words. That is a detector blind spot of the same
family the taxonomy in `2026-08-15-detector-blindness-taxonomy.md` catalogues.

## A Lean detail worth not rediscovering

A structure all of whose fields are `Prop`s lands in **`Prop`**, not `Type`. Three of the
four shapes here are therefore `Prop`s (`DecoyContext` is not — its `premise : Prop` field
is `Type`-valued), so `Contentless` must quantify over `Sort*`. With `Type*` the file does
not compile, and the error names a sort mismatch rather than anything about the
mathematics.

## Deliberately NOT done

- **No claim that the 46 conclusions are false or doubtful.** Several are plainly intended
  as honest §3b axiomatisations of open inputs. The claim is narrower and entirely about
  the Lean: *as structured, those declarations prove nothing beyond assuming their
  conclusions*, so they may not be cited as evidence for them.
- **No file restructured.** Each fix is a per-file mathematical judgement about what the
  genuine sub-hypotheses are — the conclusion *composed* from fields rather than applied
  from one — which is the author's call, and doing 46 of them is a sweep the ASK-OWNER
  directive gates.

Left in-progress: the artifact exists; the 46 entries are not drained.


## Correction and a fifth pattern (same day)

**The count above is wrong. It is 48, not 46** — `field-projection` 22 +
`exact-field-projection` 2 + `tuple-projection` 11 + `decoy-hypothesis` 13. The 46 came
from my own arithmetic, not from a stale measurement, and it reached the Lean docstring,
a commit message and this bean before being re-counted. Recount with the script rather
than quoting any of the three.

**A fifth pattern is now covered: `prop-universe-field` (19 live), for 67 across five.**
It is the sharpest of them and the only one that is a *type-level* error rather than a
judgement about intent. The ledger states it identically in all 19:

> *"Every field of this carrier is typed bare `: Prop` — the UNIVERSE of propositions, not
> a proposition. An instance therefore supplies a proposition rather than a proof of one,
> so `instance := ⟨True⟩` type-checks and discharges the class."*

Proved rather than trusted:

- `propUniverse_inhabited` — the carrier is inhabited **outright**, `⟨True⟩`.
- `propUniverse_contentless` — so it is contentless for **`True`**: it asserts nothing
  whatever, which is strictly worse than the self-assuming shapes, which at least assert
  their conclusion.
- `conditional_on_propUniverse_is_unconditional` — **the harm, exactly**: every theorem
  stated conditional on such a carrier is unconditional, because the hypothesis discharges
  itself. A `[C]`-conditional result downstream of one of these 19 is conditional on
  nothing, and the §3b-cond exception does not apply to it however the block is labelled.
- `propUniverse_vs_propField` — the discriminator is the field's **type**, mechanically:
  `PropUniverseContext` is always inhabited, `SelfAssumingContext False` never is. So
  `claim : Prop` versus `claim : C` is the whole difference, settled by looking at the
  field rather than the docstring.

All five new declarations depend on **no axioms at all**.


## 🛑 Correction: the fifth pattern was NOT prose-only, and I said it was

`docs/audits/2026-08-23-free-prop-field-triviality-probe.lean` already demonstrated the
`prop-universe-field` triviality **in Lean**, on 2026-08-23 — reproducing three carriers
verbatim (`DimMasterPentagon`, `BringSurfaceSmoothness`, `HabiroFlowSolution`), discharging
each with `⟨True, …⟩`, and exhibiting the unconditional consequence
(`conditional_on_habiro [HabiroFlowSolution] (P : Prop) (hP : P) : P := hP`).

I wrote that this file "turns the finding into a theorem" and that the ledger recorded it
"as prose". **That is true of the four self-assuming patterns and false of this fifth
one.** I ran the corpus-grep against the *ledger* and not against the tree for prior
formalizations of the pattern, which is the checklist's own point.

What this file genuinely adds for the fifth pattern is **generality and placement**, not
discovery: the probe is a self-contained demonstration in `docs/audits/` over three named
classes; these declarations abstract the shape, live in the library tree where a block can
cite them, and connect the pattern to the other four through `Contentless`. The probe
deserves the credit and now has it, in the file's own §.

## And the probe carries a trap this file was missing

`HabiroFlowSolution` has a **fourth field conjoining the three** (`all_hold : p ∧ q ∧ r`),
which looks like it forces them to hold. It does not — the three are *propositions*, so
`⟨True, True, True, ⟨trivial, trivial, trivial⟩⟩` discharges the whole carrier.

That is exactly what an author adds on being told the carrier asserts nothing, and it
changes nothing while looking like a fix. Now stated for the shape:
`propUniverseWithConjunction_inhabited` / `_contentless`. The repair is to type the fields
by actual propositions, never to conjoin propositions-as-values.


## Damage bound: the 15 remaining carriers are LATENT, not active (2026-09-12)

Measured two things after fixing four of the nineteen, and both correct my earlier framing
that the remaining drain was high-value-urgent.

**1. No other carrier has its triviality cashed into a claimed proof.** Scanned all 15
remaining live `prop-universe-field` files for a `theorem`/`lemma` whose proof term feeds
`True` into the carrier — the `brings_smoothness_resolution` shape. **0 hits.**

The scan is **self-tested against the known positive**: run against
`brings-smoothness-resolution.lean` at its pre-fix revision it reports
`CAUGHT: brings_smoothness_resolution`. So the 0 is evidence rather than a vacuous
detector reporting on nothing — which is the distinction AGENTS.md demands and which a
bare "I found none" would not have earned.

**2. None of the 15 carriers has an instance anywhere in the tree.** So no downstream
`[C]`-conditional theorem is *actually* discharged today; the hazard is that writing
`instance := ⟨True⟩` would silently make every one of them unconditional, and nothing
stops that.

### What this changes

`prop:brings-smoothness-resolution` (bean `qou-c46w`) was the **only** one of the nineteen
where the defect had been cashed — a paper proposition with `True ∧ True ∧ True` as its
cited proof. The other 15 are a **latent hazard**: real, worth fixing, but not currently
making any false claim. I called them "the best-specified drain in the ledger" and implied
urgency; that was right about specification and wrong about urgency.

Nine of the 15 have **zero consumers** and are one-file mechanical fixes
(`BorromeanHopfEnergyCrossoverContext`, `BringPeriodSublattice`, `ClassicalRiemannZeta`,
`DegreeZeroDatum`, `DescentData`, `HadronFibreEmbedding`, `HorizonStructure`,
`ObstructionParallel`, `SaddleTrajectory`). Three have one consumer, one has two.
`HeckeAnyonicSubstrate` (6) and `KnotOperator` (14) are not chips and need their own call.

### Limits of the measurement, stated

- The `True`-theorem scan is one regex validated against **one** known positive. A
  differently-spelled discharge (`⟨trivial⟩` via a `have`, a `decide`, an instance-argument
  route) would not be caught. It bounds the obvious shape, not the class.
- The instance scan greps `instance … : <Carrier>`; an instance introduced by `haveI`,
  `letI` or `deriving` would be missed.
- Both are cheap re-runs, so re-measure rather than quoting these.


## 🛑 Two corrections from checking the 2026-08-23 probe's own carriers

The probe names three carriers. I checked what became of the two that are **not** in my
live-15 list, and both answers correct something I told the author.

### 1. `DimMasterPentagon` was already fixed — by a sibling, better than I have been fixing them

Commit `bff4027fc`: *"lean(qou-tsnp D17): DimMasterPentagon asserted nothing; encode the
master identity + the specialisation, prove the transport"*. The live class is
`class DimMasterPentagon {F : Type uF} (master : PentagonDatum.{uA, uO})`; the old
`holds : Prop` survives only as a quoted historical line inside the new docstring, which
diagnoses the defect in almost the same words I used.

**Their fix is strictly stronger than mine.** They *encoded the identity and proved the
transport*; I *parameterised*, which removes the `⟨True⟩` discharge but supplies no
mathematics. Parameterising is the right move when nothing in the import cone can state
the proposition (the Wenzl and OS-reflection cases genuinely cannot). It is the **weaker**
move where the content is statable — and `bff4027fc` shows that is sometimes the case.

So this drain was **already underway under bean `qou-tsnp`**, and I did not find it: my
corpus-grep reached the probe but never asked what had happened to the carriers the probe
names. That is the checklist's own point, missed twice in one session.

### 2. `HabiroFlowSolution` is still broken and has NO ledger entry at all

`folio/quantum-observable-universe/lean/QOU/Habiro/FlowSolution.lean` still carries three
bare `: Prop` fields plus the `all_hold` conjunction — the exact shape
`propUniverseWithConjunction_inhabited` now covers. Searching the ledger for
`Habiro`/`FlowSolution` returns **one** entry, an unrelated `borrowed-name` in a different
file.

**So the ledger does not track it**, and therefore:

> **"19 live `prop-universe-field` entries" is a LOWER BOUND, not a population count.**

I have been quoting 19 (and 15 remaining, and 67 across five patterns) as if they were
counts of the defect. They are counts of *what the ledger holds*. At least one carrier the
corpus's own probe named in August is outside them. Anyone drain-planning from those
figures will finish the list and still have carriers left.

The right population query is a **detector run over the tree**, not a ledger query. That
has not been done here and the figures above should not be quoted until it is.


## The `Contentless` criterion is sound but UNDER-DISCRIMINATING — measured on 2 of the 46 (2026-09-14, from qou-9yt9)

`Contentless K C := Nonempty K ↔ C` correctly captures *"this declaration adds no
logical content."* It does **not** capture *"this declaration is a defect"* — because it
says nothing about **how `Nonempty K` is obtained.** Two cases collapse into one verdict:

| `Nonempty K` is … | reading |
|---|---|
| **assumed** (no instance, or instance is `sorry`/`True`) | self-assuming projection — defect |
| **proved** (closed instances over the index range) | the **Mathlib accessor idiom** — legit |

Both satisfy `Nonempty K ↔ C`. The criterion cannot separate them, and the corpus already
contains the separation as a **verdict/disposition contradiction inside the ledger**.

### The two measured instances, both in `QOU/Archimedean/QHookBound.lean`

`qInt_ratio_bound_small` (:415) and `qFact_ratio_bound` (:608) each carry
`verdict: genuine` with `disposition: accessor-idiom-legit` — and entry 2's own evidence
says *"Same accessor idiom as qInt_ratio_bound_small; re-confirms prior **legit**"* while
entry 1's says *"It remains a **genuine** field-projection."* The two entries disagree
about the same idiom.

**The substance decides it, and it is machine-checkable in three greps:**

1. **The field is not a universe-`Prop`.** `bound : |qIntReal q m / m - 1| <= (q - q⁻¹)^2 * m / 6`
   — a concrete inequality fixed by the class parameters. A constructor cannot choose it;
   `True` cannot discharge it. (Contrast the seven carriers closed under `qou-9yt9`, whose
   fields were typed with the universe `Prop` and *were* constructor-chosen.)
2. **Every instance is closed.** All **8** instances (`qIntRatioBoundSmall_one..four`,
   `qFactRatioBound_zero..three`) take **no context-class binder** — they are `nlinarith` /
   `simp` / `qInt_ratio_bound_m1` proofs, so they cannot be chaining the assumption.
3. **Zero `sorry` in the file** (`grep -c` on the word = 0).

`QIntRatioBoundSmall` binds `1 <= m` and `m <= 4`, so those four instances cover the
**entire index range** — `Nonempty K` is a theorem for every admissible `m`, given only
`q > 1` and `q < 3/2`.

### Proposed third axis for the criterion

```
field type is universe Prop                                     -> irreparably vacuous
concrete field type, no closed instance                         -> self-assuming (defect)
concrete field type, closed instances covering the index range  -> accessor idiom (legit)
```

Axis 1 is already greppable; axis 3 is `instance` decls whose signature carries no
`[_ : <ContextClass> ...]` binder, plus a sorry check. Neither needs the class to be read
semantically.

### Scope — what this does NOT establish

- Measured on **2 of the 46**, chosen because their own ledger entries contradict
  themselves. **I have not re-read the other 44**, and I am not proposing a sweep.
- **`QFactRatioBound` has a real coverage gap**: `k : ℕ` is **unbounded** and instances
  exist only for `k = 0,1,2,3`. For `k >= 4` the accessor is *unusable* (no instance found),
  not *unsound* — but a downstream file supplying its own `instance ... := ⟨sorry⟩` would
  turn it back into laundering. That is caught by the sorry audit, not by this criterion.
- I did **not** verify that no consumer supplies such an instance.

### Not enacted

The two verdicts are left at `genuine`. Correcting them would exempt them and move
`proof-no-self-assuming-projection` 57 -> 55, and it overrides another agent's explicit
"It remains a genuine field-projection" — a judgement call between two prior readings,
not a precision fix, so it waits (AGENTS.md §ASK THE OWNER). Recorded here because this
bean owns the criterion.


## CORRECTION to the block above (same session, 2026-09-14) — I merged two cases the corpus separates

Three measurements after writing the block above, two of which I should have made first.

### 1. A prior corpus artifact already adjudicated one of them — and it is in Lean

`docs/audits/2026-08-30-context-classes-hand-adjudicated.lean` §`HandAdjudicated7` is
headed **"`ConvergenceBound` and `QIntRatioBoundSmall` — NOT vacuous"** and says they are
*"scored here rather than counted."* It backs that with **compiling** demonstrations:

```lean
example (q : ℝ) (hq : q > 1) (hq2 : q < 3/2) :
    QIntRatioBoundSmall q hq hq2 1 (by norm_num) (by norm_num) := inferInstance
example ... 2 ... := inferInstance
```

Its own discriminator is sharper than mine and worth adopting verbatim:
**"A class refutable at one parameter assumes something at every parameter."**
It demonstrates that too — `convergenceBound_refutable` exhibits `k = 4, C = 1, f = 100 vs 0`
where the bound fails.

So the contradiction is not one I found; the corpus recorded it on **2026-08-30**, the same
day as the two ledger entries' `reviewed_at` (14:13:22Z). The ledger is the outlier.

### 2. The two are NOT the same case — the index ranges differ, and that is the whole question

I wrote *"Same accessor idiom"*, following the ledger entry's own evidence text. **Wrong**,
and the prior audit adjudicates only the first:

| accessor | index range | instances | reading |
|---|---|---|---|
| `qInt_ratio_bound_small` | `1 <= m <= 4` — **bounded** | m = 1,2,3,4 — **complete** | every ground instance is proved |
| `qFact_ratio_bound` | `k : ℕ` — **UNBOUNDED** | k = 0,1,2,3 only | **assuming for k >= 4** |

`QFactRatioBound` is not adjudicated in that audit file at all. Its class is refutable at a
large enough `k` in exactly the sense quoted above, so by the audit's own criterion it
**assumes something at every parameter** — which is the opposite of what my block concluded
for it.

### 3. And the general-`m` form still carries the assumption even where coverage is complete

Instance resolution matches the index **syntactically**. The four instances have types at the
literals `1,2,3,4`; `qInt_ratio_bound_small` is stated at a **variable** `m` with
`hm : 1 <= m`, `hm4 : m <= 4`, and no instance matches a variable. So the theorem is
dischargeable at each literal and is an assumption in its stated general form. Nothing
unproved can be *extracted* (every ground case is proved), but "complete coverage" does not
make the general-`m` statement a proof.

### What this does and does not change

**Unchanged, and if anything strengthened:** the `Contentless` criterion conflates
*class has content* with *theorem is not a defect*. The prior audit's "NOT vacuous" is a
verdict on the **class**; I treated it as settling the **theorem**, which is the same
conflation running the other way. Both directions need the third axis.

**Withdrawn:** my recommendation that both verdicts flip to `legit`. At most
`qInt_ratio_bound_small` has a corpus artifact behind it, and even there the general-`m`
form is arguable. `qFact_ratio_bound` should stay `genuine` on the unbounded index alone.

### One fact that makes all of this currently academic

`grep` across every `.lean`: **zero** instances of either class outside `QHookBound.lean`,
and **zero** consumers of either accessor anywhere in the corpus — in-file uses are two
comments. So the `k >= 4` laundering hazard I flagged is **unrealised**, and neither
accessor is load-bearing for any result.


## Re-confirming your HabiroFlowSolution lead (2026-09-14) — it holds, and the cause is worse than "no ledger entry"

Your 2026-09-12 correction (`1af1fe232c`) says `HabiroFlowSolution` is still broken with no
ledger entry, and that *"the right population query is a DETECTOR RUN OVER THE TREE, not a
ledger query."* Re-measured two days later, both halves hold — and the detector run does not
save you either.

**Still broken, and it is the exact shape** of the seven carriers closed under `qou-9yt9`:
`QOU/Habiro/FlowSolution.lean:49` carries **three literal universe-`Prop` fields** —
`expQ_solves_base_reeb : Prop`, `fourier_diagonalises_qheat : Prop`,
`liTwoQ_volumetric : Prop` — plus `all_hold` conjoining them. Any instance picks all three;
`True ∧ True ∧ True` discharges the lot.

**Still no ledger entry.** The only Habiro/FlowSolution key is
`ZHabiroCauchy.lean::truncSection_zHabiroLimit::proof-borrowed-name` — a different file, a
different category, exactly as you found it.

### The new part: the DETECTOR does not flag it either, and the drain is why

`docs/audits/2026-06-17-lean-vacuity-axiom-audit.json` has **zero** entries for
`QOU/Habiro/FlowSolution.lean` in any category. The two `Habiro`-named hits are
`UniversalHabiroStructure` and `QPochhammerHabiroEvaluation` — other files, both exempt.

The file's own comment says why:

```
/-! ### Removed 2026-08-30 — self-assuming projections
- `habiro_flow_solutions_realise_synthesis` — body was `inst.all_hold`: the conclusion
  was the projected field verbatim, so the declaration restated its own hypothesis.
```

**The 2026-08-30 drain removed the consumer, and with it the detector's only handle on the
file.** The carrier was left in place. So fixing the projection made the vacuous carrier
*invisible* — a blind spot the drain itself created, which is worse than a native one
because draining manufactures more of them. That is a new row for
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` if you want it; I have not added it,
since this is your arc.

### It corrects my own framing three blocks up

I wrote that all 57 non-exempt `proof-no-self-assuming-projection` hits carry a ledger
verdict, and concluded *"this is a confirmed repair backlog, not a triage problem."* The
first clause is a measurement and stands; **the conclusion over-states completeness.** 57 is
what *this detector* sees on *this run*, against a documented 45-row blind-spot taxonomy, and
`HabiroFlowSolution` is a live counterexample sitting outside it. Read the 57 as a lower
bound.

So your point generalises one step further: **a detector run is a lower bound too**, and a
ledger that covers 57 of 57 detector hits is evidence about the ledger's coverage of the
detector, not about the corpus.

### One interaction with your `DimMasterPentagon` note, stated against myself

You wrote that encoding-and-proving-the-transport (`bff4027fc`) is the stronger move and
*"parameterising ... is the weaker move where the content is statable."* Two of the carriers
I closed were **parameterised**, so by your criterion they need the statability test:

- `KnotOperator.is_knot` (#7359) — the file has no knot theory in its cone at all
  (`gram_matrix` is the zero matrix), so nothing there can state single-componentness.
  Parameterising looks right by your test.
- `DegreeZeroDatum.formallyProvable` (#7360) — needs a provability predicate over a formal
  system, which Mathlib does not carry at this toolchain. Defensible, but I have **not**
  exhaustively established that no Mathlib route states it, so treat it as argued rather
  than measured.

Neither is a claim that parameterising was optimal; it is the test you asked for, applied.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 58 — PR #8304)
- **Status:** `in-progress` (opened `litlfred/qou#8304`, branch `claude/round58-devacuify-6qbv-b9cj`, HEAD `e72e4e04168ffebca669be8e58b6df711ee7f5ed`, C1 `e3528dd09222e2ddccf5556168d0aa31aca7f5d7`).
- **Target:** `folio/quantum-observable-universe/lean/QOU/Habiro/FlowSolution.lean` + 80-dps witness `computations/probes/round58-devacuify-6qbv-b9cj.witness.json` (`scriptHash = a44d91e59ddc`, `allPassed = true`, `0` `float64`).
- **Updated at:** `2026-11-17T10:34:25Z`.
