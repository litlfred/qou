---
# qou-a30t
title: 'Self-assuming context classes: one machine-checked criterion for four ledger patterns (46 live genuine entries)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-12T12:02:39Z
updated_at: 2026-09-12T12:30:45Z
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

`content/quantum-observable-universe/lean/QOU/Habiro/FlowSolution.lean` still carries three
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
