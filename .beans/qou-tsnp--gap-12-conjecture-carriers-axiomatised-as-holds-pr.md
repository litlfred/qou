---
# qou-tsnp
title: 'GAP: 12 conjecture carriers axiomatised as `holds : Prop` assert nothing'
status: in-progress
type: task
priority: normal
created_at: 2026-08-09T00:12:10Z
updated_at: 2026-09-05T06:05:54Z
---


## The defect

Twelve conjecture sibling carriers are axiomatised as

```lean
class C where
  holds : Prop
```

A field of type `Prop` names *some* proposition; it does not assert it.
`instance : C := ⟨True⟩` discharges the class, so the carrier asserts
nothing. This is the AGENTS.md §3b-tax failure ("the carrier must assert
something"), in a shape neither `proof-no-empty-prop-carrier` (fires on
*zero* fields) nor `proof-claims-unencoded`'s `true-class-field` pattern
(fires on a field typed literally `: True`) currently catches.

**Known, not new.** Named vacuous for one instance in
[`2026-06-07-klr-gs-order-formalization-plan.md` §Layer 1](../docs/audits/2026-06-07-klr-gs-order-formalization-plan.md)
("the current stub `class CrystalGraphRealization where holds : Prop` is
vacuous"), and as `reduction_holds : Prop` in
[`2026-06-24-devils-advocate-wave10.md`](../docs/audits/2026-06-24-devils-advocate-wave10.md).
This bean is the **corpus-wide census** and the drain queue.

## Scope — the 12 (verified: no library decl exists under the ref leaf)

| block | class |
|---|---|
| `mass-theory/borromean-bloch-group-element` | `BorromeanBlochGroupElement` |
| `mass-theory/dim-master-pentagon` | `DimMasterPentagon` |
| `mass-theory/isospin-from-canonical-bowtie` | `IsospinFromCanonicalBowtie` |
| `mass-theory/kashaev-density-equals-sdp-multiplicity` | `KashaevDensityEqualsSdpMultiplicity` |
| `mass-theory/p-from-braid-mirror` | `PFromBraidMirror` |
| `mass-theory/poincare-lefschetz-borromean` | `PoincareLefschetzBorromean` |
| `nuclear-interactions/spin-from-so3-fiber` | `SpinFromSo3Fiber` |
| `nuclear-interactions/t-from-trace-cyclicity` | `TFromTraceCyclicity` |
| `nuclear-interactions/type-b-folding-cpt` | `TypeBFoldingCpt` |
| `nuclear-interactions/wigner-su4-from-spin-isospin` | `WignerSu4FromSpinIsospin` |
| `q-geometric-langlands/mirror-3d-3d-correspondence` | `Mirror3d3dCorrespondence` |
| `stochastic-mechanics/lusztig-canonical-basis-q-eq-1` | `LusztigCanonicalBasisQEq1` |

**Count correction.** An earlier pass put this at 18, then 16. Both were
too high: 4 of the 16 (`brunnian-property-of-borromean`,
`gs-graded-markov-trace-existence`, `hyperbolic-volume-transcendence`,
`q-gl-conjecture`) do have substantive library formalisations, declared
under the **ref's leaf name in a differently-named file**, which a
class-name match misses. Those 4 were shadows and are now deleted. 12 is
the verified figure.

## Repair shape

Per §3b-tax and the klr plan: replace `holds : Prop` with fields that
encode the conjecture's **content** — parameter-quantified statements in
the shape of the claim, so that an instance is a real commitment and
downstream `[C]`-conditional theorems are conditional on something.

The exemplars now reachable after the shadow deletions show the target
shape, e.g. `QOU.Archimedean.HyperbolicVolumeIndependence.no_relation`
(a full algebraic-independence statement) and
`QOU.QGeometricLanglands.QGeometricLanglandsConjecture` (functor +
`hecke_compatible` + `recovers_eigenvalue`).

**Not mechanical.** Each requires reading the block's `.md` and stating
its actual claim in Lean. Do not batch-rewrite. Do not substitute a
`sorry`-carrying restatement for an honest one — a carrier with no
instance is the correct representation of an open conjecture.

## Guard

This is the *ideal* end state, not a licence to fabricate content. If a
conjecture's claim cannot yet be stated against existing types (the
`categorical-proton` failure mode — the type has no field for the
asserted property), the honest outcome is to say so and leave the
carrier, noting what type must grow first.

## Progress

**1 of 12 closed — `t-from-trace-cyclicity` (2026-08-09).**
`holds : Prop` replaced by
[`QOU/BraidsAndKnots/TFromTraceCyclicity.lean`](../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/TFromTraceCyclicity.lean):

- **4 unconditional theorems** — `timeReversal_involutive` (T² = id),
  `timeReversal_crossings`, `timeReversal_perm` (generator indices + signs
  preserved), `timeReversal_append`. Verified `lean`-direct **exit 0**;
  `#print axioms` = `[propext]` only, **no `sorryAx`**.
- **1 conjectural class field** — `trace_reversal_invariant`, quantified
  over every representation and every braid word (the shape of the claim,
  not an opaque `Prop`).

Sibling stub deleted; module wired into `QOU.lean`; `.ts` set to
`validation: "validated"`.

### Two findings from doing it

1. **The block's stated derivation is a non-sequitur.** The `.md` gets
   reversal invariance "by the Markov trace cyclicity axiom". Cyclicity
   gives *rotation* invariance (`markovTrace_append_comm`); reversal is a
   different operation and `tr(ABC) ≠ tr(CBA)` for non-commuting matrices.
   The claim is plausible via the generator-fixing anti-automorphism, but
   that route is not in the corpus — hence a class field, not a proof.
   Recorded as an `authorNotes` caveat on the block.
2. **`BraidWord` is overloaded** — `QOU.BraidWord` (a `structure` in
   `PhotonThreading.lean`) vs `QOU.Archimedean.BraidWord (n : ℕ)`. A bare
   `open QOU` silently resolves to the wrong one and the file will not
   elaborate. Anything touching Hecke braid words must fully qualify.

**11 remain.** Each needs the same treatment: read the `.md`, state the
actual claim, prove what is unconditional, carry only the genuinely open
part as a class field.


## 2026-08-23 — census WIDENED 9x, from PR #5562 (branch bring-surface-categorical-trace)

Contribution from another branch, not a takeover of this bean.

**A re-runnable detector now exists**: `scripts/free-prop-field-audit.py`
(`--self-test`, 4 hand-read cases). Worth having because this bean's own count
history (18 -> 16 -> 12) is the hand-count decay problem.

```
free `: Prop` fields: 166 in 113 carrier(s), 101 file(s)
  UNPINNED-EMPTY      109  (66%)
  UNPINNED-FAKE-IF     39  (23%)
  PINNED               18  (11%)
```

**113 is NOT a fourth correction of the 12 — read this before "fixing" the
count.** The three prior corrections were all downward because the earlier
figure was WRONG, so a bigger number here has exactly the shape of a fourth bad
count. It is not. Different SETS:

- only **21** of the 113 have a field literally named `holds`
- **11** are on this bean's list of 12. The twelfth, `TFromTraceCyclicity`,
  **has since been repaired** — it now carries a real quantified statement
  (`∀ ρ w, markovTrace ρ (timeReversal w) = markovTrace ρ w`). So the live
  count for this bean's own scope is **11**, not 12.
- the other **102** are outside this bean's scope by construction:
  **67 in LIBRARY files** (`lean/QOU/**`), 30 chapter siblings, 5 glossary.

**The library concentration is what the `holds`-named + conjecture-sibling scope
could not see**, and it is the more consequential half — these are definitions,
not conjecture stubs:

| carrier | free fields | what the docstring says it encodes |
|---|---|---|
| `IwahoriHeckeAlgebra` | `hecke_relation`, `braid_relation`, `far_commute` | the Hecke presentation itself (§7a) |
| `MarkovTraceRecursion` | `markov_axiom_holds` | the Markov axiom |
| `ClassicalLimitFunctor` | `is_exact` | exactness — the docstring ADMITS it |

**Three buckets, because not every free `Prop` is a defect.** A field PINNING it
(`regular_iff : regular ↔ 0 < x`) makes `True` refutable. A field merely
asserting it (`hP : P`) or using it as an antecedent (`impl : P → X`) does not —
the antecedent case is its own weaker defect where the CONDITIONALITY is fake
while the consequents may still carry content.

**Verified, not asserted**: `docs/audits/2026-08-23-free-prop-field-triviality-probe.lean`,
`lean` exit 0 — three carriers instantiated as `⟨True, …⟩`, and a
`[HabiroFlowSolution]`-conditional theorem shown unconditional.

**Scope**: a claim about Lean ENCODINGS, not the mathematics. That
`IwahoriHeckeAlgebra`'s Lean does not encode the Hecke relation says nothing
about whether the relation holds.

Full write-up: `docs/audits/2026-08-23-free-prop-field-census.md`.


### 2026-08-23 (2) — units correction, and the wiring decision this needs

**Units.** The census bucket table counts **FIELDS**; a drain queue is
**CARRIERS**. 109 `UNPINNED-EMPTY` fields sit in **77** carriers; 39 `FAKE-IF`
fields in 32. I wrote "109 ... carriers" in PR #5562's body — corrected there and
in the audit doc. Quoting the field count as a carrier count overstates the
queue by 40%.

**The wiring decision.** Adding this as a criterion to
`content/pipeline/lean-vacuity-axiom-audit.ts` closes a measured blind spot —
**zero** of these carriers appear in the ledger under any criterion today. But
`--check-ledger` exits 1 unless every non-exempt candidate carries a fresh
verdict, so wiring it seeds a large `needs-agent` batch and turns the gate red
**for every branch**, not just the one that wires it:

| | ledger | gate |
|---|---|---|
| today | 124 | green |
| wire `UNPINNED-EMPTY` only | ~201 (+77) | red until all 77 are read |
| wire `EMPTY` + `FAKE-IF` | ~233 (+109) | red until all 109 are read |

That is a sequencing call for the owner, not something to land quietly — so it
is recorded here rather than done. `scripts/free-prop-field-audit.py` is the
interim: it measures the class without gating anyone.


## 2026-09-03 — the population is 24, and the defect is an INVERTED IMPLICATION

This bean opened on `class C where holds : Prop` — a carrier that names a
proposition without asserting it. Measured corpus-wide on `origin/main` (2552
files) with `scripts/lean-cited-not-proved-audit.py --kind prop-field`, the
shape is broader than `holds`, and narrower than the raw `Prop`-field count.

| | count |
|---|---|
| `Prop`-typed fields | 95 |
| parameterised (a `Prop` used as a *component* of another field's statement) | 56 — legitimate |
| self-nominating (a companion field's type IS the `Prop` field) | 39 |
| — **consumed**: a proof term projects the witness | **24 — the defect** |
| — unconsumed: an open input carried as an input | 15 — honest §3b |

**The sharper statement of the defect.** The recurring encoding is

```lean
X      : Prop        -- antecedent, named but not stated
h_X    : X           -- ...and its witness, supplied by the class
impl_t : X -> Q
theorem t [ctx] : Q := ctx.impl_t ctx.h_X
```

which is **inhabitation-equivalent to a single field `: Q`** (take `X := True`).
So the antecedent is free and a docstring reading *"X forces Q"* is, in the
Lean, *"Q"*. **The convention inverts the implication it was written to
express.** `qou_ns_in_qou.lean` is the clean illustration: its docstring says
"observability forces chi(A) != 0", `descartesQOU` literally sets
`observability := True`, and steps 2-3 of the same chain ARE genuine
implications between content-bearing data.

**A mechanical collapse is NOT the fix.** It changes nothing logically, so a
bulk pass would be AGENTS.md §1a audit-dodging. It is not detector-destroying
(`lean-self-assuming-audit.py` has a class-field mode that catches the collapsed
shape — 11 corpus-wide, over 8 files disjoint from these), so it is defensible
as a *legibility* fix, but it must never be reported as progress on derivation.

**What actually closes one: a proved upstream lemma to build on.** That is what
made `tm_eigenspace_decomp` tractable (PR #6543) — the splitting it had been
assuming is `JetChain.decomposition`, proved in `JetProlongation`, so the class
was left carrying only the two genuinely-open inputs, as equations in its own
data.

Checked and REJECTED as targets, so the next agent does not re-open them:
`NonAbelianStokes` (its own docstring says the carrier is self-certifying and
genuine models await a Mathlib Lie-valued-forms library that #6512 established
does not exist); `MassGap` (`impl_witness` already forces a content-bearing
`YangMillsMassGap`, so collapsing is logically identical); `qou_ns_in_qou`
(scrupulously scoped under an owner directive — reported, not reshaped).

**The sharpest instance, and it is not fixable here.**
`QOU/AppendixSurreals/B1TorusKnotRowsTheorem.lean` carries `bloch_suslin : Prop`
and `garoufalidis_le : Prop` with witnesses fed straight into the conclusion —
two named literature results laundered through opaque `Prop`s — and its
conclusion's predicate `b1_holds : Nat -> Nat -> Prop` is itself
instance-chosen, so the theorem is fully vacuous. Neither result is in Mathlib
nor derivable from the corpus.

Both discriminators were found by a FALSE POSITIVE on a file opened intending to
fix it (`noble_gas_characterization.lean`, then `BringWPlaneMonodromy.lean`) —
in each case the detector's own output would have damaged a correct file, and
only reading the file stopped it.

Full write-up: [`docs/audits/2026-09-03-prop-field-implication-inversion.md`](../docs/audits/2026-09-03-prop-field-implication-inversion.md).


## 2026-09-05 — progress, and one entry whose prescribed action is WRONG

Three of this list worked in order (D9 → D10 → D11), reading each block first per
*"not mechanical … do not batch-rewrite"*. Two repaired; the third is mis-scoped.

**Repaired, in the prescribed shape** — content encoded as caller-supplied
parameters so the class is refutable, refutability discharged as a theorem, **no
instance** provided:

- `IsospinFromCanonicalBowtie` (D9) — PR #6671. Content is the block's
  `Δm/M_N = ℏ_q²·h·[2]_q·(1+ℏ_q³)/3`; conventions **read from the producer**
  `verify_isospin_bar_anomaly.py`, and one would have been wrong if guessed —
  `[2]_q` there is the **symmetric** `q + q⁻¹`, not `QGenericBase.qBracket`'s
  unbalanced `1 + q`.
- `SpinFromSo3Fiber` (D10) — PR #6683. Content is the block's own named missing
  object, the level → Wedderburn-coefficient map, constrained at `h² = 0` and
  `h⁴ = −3/4`. The block's Family-A identity is **derived as a theorem**, not
  axiomatised. Guard case applied: the functor's *construction* is left unstated
  and what must grow first is named (a level type indexed against `H₃`'s blocks).

**🛑 `WignerSu4FromSpinIsospin` (D11) — the same repair would be WRONG.** A
substantive D11 carrier already exists: `QOU.WignerSU4FromSpinIsospin` at
`lean/QOU/ParticleInteractions/WignerSU4FromSpinIsospin.lean` (imported at
`QOU.lean:421`), with two real parameter-quantified fields
(`E_gate = E_0·log(1/W_λ)`, `c_λ = B_AME/E_gate`) plus three `: True` fields that
each carry an `opaque marker` docstring naming why they are unstatable. The `.ts`
refs the **stub** instead — the names differ by **capitalisation and namespace**
(`WignerSu4` in `QOU.BraidsAndKnots` vs `WignerSU4` in `QOU`), and the stub's own
header named a third path that does not exist.

So this is **this bean's own shadow case**, a fifth one its 18 → 16 → 12 correction
could not catch: that pass keyed on *"the ref's leaf name in a differently-named
file"*, and here the file name matches while the case and namespace do not.
Writing content into the stub would create a second D11 competing with the real
carrier. **The defect is the ref, not the encoding.**

Blast radius measured: **zero consumers** of either class. The ref repoint is left
as an author decision (§0a prefers candidate-2 resolution, which would need a
namespace alignment in a directory that has no single convention). Finding:
`docs/audits/2026-09-05-d11-is-a-mis-ref-not-a-vacuous-carrier.md`.

**Net for this queue:** two closed, one re-classified. The syntax count is right;
for D11 the implied action is not.

## 2026-09-05 — re-measured: the repair queue is FIVE, and my matcher was wrong five times

Read every one of the twelve declarations directly (not matched). Result:

**Already repaired (6):** `IsospinFromCanonicalBowtie` (#6671, this session),
`SpinFromSo3Fiber` (#6683, this session), `PoincareLefschetzBorromean` (3 fields,
someone else), `BorromeanBlochGroupElement` (`{B : Type*} [AddCommGroup B]`),
`LusztigCanonicalBasisQEq1` (`(R : Type u) [CommRing R] (q : R)`), and
`TFromTraceCyclicity` — the last **done differently**: stub deleted, `.ts` ref
`qou:QOU.BraidsAndKnots.TFromTraceCyclicity` matching the library carrier's
namespace exactly. That is a worked example of the disposition D11 still needs.

**Mis-ref (1):** `WignerSu4FromSpinIsospin` — see the 2026-09-05 section above.

**GENUINELY OPEN (5):** `DimMasterPentagon`, `KashaevDensityEqualsSdpMultiplicity`,
`PFromBraidMirror`, `TypeBFoldingCpt`, `Mirror3d3dCorrespondence`. Each confirmed to
have exactly ONE `^class` in its file whose sole field is `holds : Prop`.

So this bean's title (12) and its body's live count (11) are both right about the
census and neither is the number **needing the repair**, which is **5**.

**🛑 THE METHOD TRAP, which is the part worth keeping.** Five successive matchers,
each returning a plausible number, each wrong on a different Lean feature: (1) missed
the file it was pointed at — reported 3 content-free carriers against a true 17;
(2) read **docstring continuation lines as fields**; (3) didn't skip **module**
docstrings `/-! … -/`, so it read a *quoted example of the old carrier* as a live
class and **reported D9 and D10 as unrepaired one hour after I repaired them**;
(4) required `where` on the declaration line, so it called two repaired carriers
MISSING because their signatures are multi-line. Only direct reading was right.

Trap 3 is the one that stings: `qou-hprp` had already written it down — *"a grep
that reads comments as code would have sent an agent to fix the one file in the
chapter that is already correct"* — and I did exactly that, to two files, in a
session that had read that bean. The control that would have caught 1, 3 and 4 is
the same each time: **a carrier known to be repaired must not come back as
unrepaired.**

Full detail: `docs/audits/2026-09-05-qou-tsnp-queue-is-five-and-five-parsers-were-wrong.md`.

## 2026-09-05 (final) — all five open carriers repaired; what is left is two author decisions

The five from the re-measurement above are closed. Each in the prescribed shape:
content encoded as **caller-supplied parameters** (per `ConditionalClasses.lean`'s
own rule — *"an `∃` over a quantity you get to pick cannot be false, while a `∀`
about a quantity the caller supplies can"*), refutability **discharged as a
theorem** rather than claimed in a docstring, and **no instance** provided.

| carrier | PR | encoded | derived | left unstated, and what must grow first |
|---|---|---|---|---|
| `PFromBraidMirror` | #6728 | `involutive`, `writhe_neg`, `fixes_q` — the third is what separates `P` from bar | `p_fixed_point_writhe_zero` | `bar = P·C·T`; needs one braid-word type carrying `P`, `C`, `T` at once |
| `DimMasterPentagon` | #6731 | master identity + specialisation | the transport | — |
| `KashaevDensityEqualsSdpMultiplicity` | #6734 | the prefactor identity | — | the density half; said plainly rather than fabricated |
| `Mirror3d3dCorrespondence` | #6737 | `four_loop_matches`, `borromean_h4 = −3/4` | `mirror3d3d_four_loop_value` | a 3d `N=2` partition-function type with a loop-order expansion |
| `TypeBFoldingCpt` | #6741 | `fold_reverses`, `foldAct_involutive`, `stable_iff_fixed`, `anti_iff_moved` | **four** theorems, incl. `typeBFold_no_global_chirality_grading` | `CPT = C⊗P⊗T` (same missing object #6728 names); the type-`B`-*specifically* label needs a root-system/Cartan type |

Three properties of this batch worth keeping:

1. **Two carriers independently named the same missing object.** #6728 and #6741
   both stopped at `bar = P·C·T` / `CPT = C⊗P⊗T` for the same reason — no single
   type carries `C`, `P`, `T` and the fold action simultaneously. Two agents
   reaching the same boundary from different blocks is evidence the boundary is
   real, not a convenience.
2. **#6741 re-derives a corpus result from its own repaired fields.**
   `typeBFold_no_global_chirality_grading` entails
   `StandardModel.Chirality.stable_matter_and_global_chirality_incompatible`.
   That is the strongest available check that a repaired carrier asserts enough:
   it now implies a known non-trivial fact about its own subject, and with the
   sign the right way round.
3. **The D11 lesson was applied prospectively, twice.** A library-twin check ran
   before #6737 and #6741 and came back empty for the first; for the second it
   came back **non-empty** — `QOU.BraidKnot.SymmetricCrystalPairProduction`
   already carries the bar-invariance leg — so that leg was deliberately **not**
   restated. D11's failure mode (a second carrier competing with a real one) was
   avoided by design rather than caught after the fact.

**Seven dead pointers dropped across the batch** — `lean/QOU/…/<Carrier>.lean`
"(file pending)" headers naming files that do not exist, plus one `.md` section
reference with no such section. This rot is systematic in the queue, not
incidental; a carrier repair should grep its own header before trusting it.

### What remains — both are author decisions, neither is repair work

- **D11 `WignerSu4FromSpinIsospin` ref repoint** (the mis-ref above). Zero
  consumers of either class, so the no-op is safe and cheap.
- **The 2026-08-23 wiring decision** (`UNPINNED-EMPTY` as a ledger criterion,
  which turns `--check-ledger` red corpus-wide until ~77 carriers are read).

Both are framed with evidence, options, defaults and blast radius in
[`docs/audits/2026-09-05-four-decisions-from-the-carrier-queue.md`](../docs/audits/2026-09-05-four-decisions-from-the-carrier-queue.md)
(PR #6740).

### One defect found — it was in FOUR merged PRs, not two, and it is now fixed

`voice-scholarly-default`'s `SECOND_PERSON_RE`
([`qa-checkers-voice.ts:873`](../folio-assistant/content/pipeline/qa-checkers-voice.ts))
lists `get` in its `you (?:can|…|get|…)` alternation, and the criterion reads
Lean docstrings when a `.lean` is present (`qa-criteria-registry.ts:177`,
`also_invalidated_by: ["lean"]`). Every carrier that quoted
`ConditionalClasses.lean`'s design rule **verbatim** therefore contains a
matching string, and each read `pass` **only because its sidecar predates the
repair**. Measured on `spin-from-so3-fiber` (#6683): recorded lean hash
`01a66001ac03` against a live `dc3554e7761d`; `p-from-braid-mirror` (#6728),
`828d9508850d` against `8c59ae7dbda4`.

**The count needed correcting, and the correction is the point.** #6741's report
named **two** siblings. Re-measured by running the actual regex over every
sidecar'd content-block `.lean` in the tree — rather than over the two files
named — the answer is **four**: #6683, #6728, #6734 (`kashaev-…`) and #6737
(`mirror-3d-3d-…`). #6671 and #6731 never carried the quote; #6741 paraphrased.
A report naming instances is not a measurement of the population, even when the
instances it names are real.

**Fixed** on the decision-brief branch under the adjacent-bug rule: all four
paraphrase the rule instead of quoting it, the regex now returns **0** hits
across sidecar'd content Lean, and all four verify `lean`-direct **exit 0**.

The general hazard stands and is not fixed by this: **a stale sidecar reads
exactly like a pass**, so a sweep against a file its sidecar predates certifies
nothing. Four criteria-clean verdicts here were about files that no longer
existed in that form.

## 2026-09-05 (ruled) — D11 closed, and TWO MORE mis-refs found in the same shape

The author ruled *"do as recommended"* on the four-decision brief. D11 — the one item this
bean had left as an author decision — is **closed**, and applying the ruling turned up two
further instances of the same defect that were not in this bean's list of twelve.

**D11 is closed, but not the way the brief described.** The library carrier this bean
called *"substantive, 2 real fields"* was **uninhabitable**: both content fields quantified
over all reals with no hypothesis, so `E_gate = E_0·log(1/W_λ)` at `E_gate := 1, E_0 := 0`
forces `1 = 0`, and `¬ Nonempty WignerSU4FromSpinIsospin` was provable (`lean`-direct,
exit 0). **That is a worse defect than the `holds : Prop` stub it was to replace** — a
vacuous carrier makes a conditional theorem conditional on *nothing*; an uninhabitable one
makes it **vacuously true**, which reads as *proved*. Both were repaired: stub deleted,
file moved to `QOU/BraidsAndKnots/` so decl path matches file path, and the class
re-stated on caller-supplied parameters.

**New shape for this bean's taxonomy: `_satisfiable` as well as `_refutable`.** Every
repair in this queue discharged refutability. D11 shows that is only half the check —
*"no instance is provided"* and *"no instance could exist"* are indistinguishable from
outside, and this carrier was the second while reading as the first. Carriers should
discharge **both** directions.

**Two more mis-refs, found by decision 4.** `quantum-langlands-dual` and
`reverse-limit-q-to-infinity` each carry a `holds : Prop` stub **shadowing** a substantive
library carrier via §0a candidate-1 — `QOU.Conjectures.QuantumLanglandsDual` (4 fields) and
`QOU.IwahoriHecke.TypeA.ReverseLimitQToInfinity` (a proved identity **with an instance**).
Neither is on this bean's list of twelve, because that list was built from carriers
*verified to have no library decl under the ref leaf* — and here the leaf names differ from
the ref's namespace, exactly the D11 blind spot. Both stubs deleted; the Langlands ref
repointed.

**So the shadow class is bigger than the three this bean has recorded** (`TFromTraceCyclicity`,
D11, and the four from the 18 → 16 → 12 correction). The mis-ref is a *sibling* defect to
`holds : Prop`, not a subcase, and no detector in this bean's history looks for it: the
`free-prop-field-audit` finds the vacuous class and says nothing about whether a real one
exists elsewhere under a different name. Worth a bean of its own if the pattern recurs.

### Method note — a cached `fail` prints as absent

`qa-sweep`'s summary line counts only criteria **evaluated in that run**. Measured: a second
sweep of `p-from-braid-mirror` printed `0 critical, 0 major, 0 minor` while its sidecar held
`detangler-no-forward-ref` as `fail`/major from an earlier run. **A false clean**, and it
would have gone into a PR body as "all seven blocks clean". Read the sidecar entry, not the
summary. Same lesson as the stale sidecars one entry up, one level higher: the artifact that
reports the verdict is not the verdict.
