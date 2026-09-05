---
# qou-tsnp
title: 'GAP: 12 conjecture carriers axiomatised as `holds : Prop` assert nothing'
status: in-progress
type: task
priority: normal
created_at: 2026-08-09T00:12:10Z
updated_at: 2026-09-05T05:56:57Z
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
