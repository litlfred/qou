---
# qou-szd6
title: 'V7 Lean carrier + infra hygiene (foundational): abstract keystone carriers (#3773), de-fabricate vacuous carriers (#3793 needs reconcile vs current main), sign audit (#4054). Formalization spine + olean cone growth.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T02:56:27Z
updated_at: 2026-10-04T15:25:24Z
parent: qou-5vkl
---


## Census 2026-08-16 — the vacuous-carrier class, measured

This bean was title-only. Filling it with what is actually there, because the
sub-item "de-fabricate vacuous carriers (#3793 needs reconcile vs current
main)" is still true and now has numbers.

### The class, and why the existing detectors cannot see it

Three vacuity detectors exist and all three look at **theorems**:

| detector | shape it catches |
|---|---|
| `scripts/lean-self-assuming-audit.py` | `theorem … (h : P) : P := h` (`qou-q407`) |
| `content/pipeline/lean-vacuity-axiom-audit.ts` | `sorry`, axioms, `: True` conclusions (`qou-6qbv`), `proof-no-self-assuming-projection` |
| folio-assistant triviality probe | semantically-vacuous theorem statements (`qou-z3k1`) |

The class this bean names is different: the vacuity is in a **`structure`/`class`
that stands in for a claim**. There is no proof term to inspect, no `True`
conclusion, no `sorry`. The single vacuity criterion in the TS gate is
`proof-no-trivial-true` — nothing examines carrier bodies.

**Measured, not assumed.** Both static detectors, pointed at
`lean/QOU/QuantumObservableUniverse/` (16 files, which contains three
hand-verified instances listed below):

- `lean-self-assuming-audit.py` → `scanned 16 .lean files — 0 self-assuming candidate(s)`
- `lean-vacuity-axiom-audit.ts` → `scanned 16 .lean, 0 defect candidate(s)` (6 exempt, none in the two files concerned)

### Population: 43 claim-carrying structures, 9 referenced nowhere

Scanned all 1939 `.lean` files for `structure`/`class` declarations whose
docstring carries a `\label{thm:|prop:|lem:|cor:}` — i.e. Lean that stands in
for a **claim** rather than a definition. There are **43**.

Counting references by identifier across the tree, **9 appear exactly once in
the entire corpus — their own declaration line**. Nothing instantiates them,
nothing consumes them, they are not mentioned even in their own file:

| declaration | label |
|---|---|
| `BraneBoundaryStructure` | `prop:brane-boundary` |
| `BriggsKleinChart` | `prop:chiral-elliptic` |
| `ChiralSectorCoords` | `prop:genus-maximal-descent` |
| `EigenspaceDecomposition` | `prop:descent-eigenspaces` |
| `IsLeibnizAlgebra` | `prop:dq-squared` |
| `MassIdentityC` | `cor:mass-identity-C` |
| `SelfDualCurvature` | `prop:self-dual-curvature` |
| `TruncatedLerayProfile` | `thm:ns-singularity-descartes` |
| `VolumeFromRigidity` | `lem:volume-from-rigidity` |

Spot-verified 5/5 by independent per-name count. `MassIdentityC` corroborates
`qou-puwe`, which found it zero-consumer by a different route.

**Caveat on the counter, stated because it bit this scan.** Reference counts
are **name-based**, not resolution-based, so they *over*-count: `YoungDiagram`
scored 881 because there are **two** distinct `YoungDiagram` structures
(`QOU/PathIntegrals.lean:329`, `QOU/BraidKnot/ShellNeutrality.lean:59`) and the
counter summed both. Over-counting is the safe direction here — it means the
nine zero-reference results are a **lower bound** on the vacuous set, never an
inflation of it. Do not quote the non-zero counts as consumer counts.

A carrier having no consumer is not automatically a defect — a §3b-conditional
carrier is legitimate, and `MassTraceIsFibreCategorical` is a good example
(consumed, non-degeneracy exercised, scope stated). The defect is a carrier
that neither constrains the objects its label names nor is consumed by
anything.

### Three hand-verified instances in the foundational definitions

Found while working `qou-n1dj`; these are the worst placement, since everything
downstream cites them.

1. **`QuantumObservableUniverse.volumeForm`** (`CategoricalFoundations.lean`) —
   condition (v), the categorical volume constraint, is encoded as
   `exteriorSquare : C` plus `volumeForm : exteriorSquare ⟶ (𝟙_ C)`. Nothing
   ties `exteriorSquare` to `Λ²(fundamentalObj)`; there is no non-degeneracy,
   epi, or invariance hypothesis. `QuantumUniverse` carries a
   `HasZeroMorphisms C` instance (needed for block orthogonality), so
   `volumeForm := 0` inhabits the field for **any** object. The formalised
   axiom constrains nothing.
2. **`QOU.SU2Emergence`** (`VolumeForm.lean:41`) — carries
   `\label{thm:su2-emergence}`. Fields: an abstract `gaugeGroupType`, an action
   on `exteriorSquare`, and `det_one : ∀ g, ext_sq_action g = 𝟙 exteriorSquare`.
   It says a group acts trivially on an unconstrained object. It does not
   mention `SU(2)` and does not mention the rank. Satisfied by the trivial
   group acting by identity on anything.
3. **`SU2EmergenceVolumeDeterminant (det_g : ℝ) : Prop where det_eq_one :
   det_g = 1`** and its twin `SU2EmergenceDaggerUnitarity` — single-field
   classes over free parameters, asserting their own conclusions. Their
   docstrings say the witness is "pending the categorical determinant
   formalisation in Mathlib", so they are honest placeholders — but a
   placeholder cannot source a claim.

**Downstream consequence, already live.** `lightning_path_synthesis`
(`LightningPath.lean:105`) is the corpus's declared dependency sink and
"evidence summary". Its docstring states pillar 1 as "the volume constraint
**forces** `Aut⊗(ω) ≅ SU(2)` (Theorem `thm:su2-emergence`)". The conjunct it
actually proves is `∀ … (emg : SU2Emergence C exteriorSquare) (g), emg.ext_sq_action g = id`,
discharged by `fun emg g => emg.det_one g` — the field projected verbatim, over
a structure with no SU(2) content. The file already has the disclosure habit
(it caveats pillars 3–4 in a "Canonical-accuracy note"); pillar 1 has no such
note. That is a gap in an otherwise careful file, not a systemic problem.

### #3793 did not land, and exactly half the fix is missing

The sub-item above says "#3793 needs reconcile vs current main". Checked: PR
**#3793 is closed, never merged** (closed 2026-08-03). On current main,
`QOU/BraidKnot/HabiroResidueSumEquivalence/archimedean_agreement.lean` still
has

```lean
class archimedean_agreement where
  residual : ℝ
  residual_eq_zero : residual = 0
```

The **fabricated instance is gone** ("No instance is provided — that is the
honest open state") — that half landed. The **contentless class body remains**,
and the file's own comment says it "is inhabited by `⟨0, rfl⟩`". #3793's
replacement (`class archimedean_agreement (traceEval gbMass ε : ℝ) where agree :
|traceEval − gbMass| ≤ ε`) is content-bearing and parameter-quantified, and is
still worth landing.

### Disposition — not fixed here, deliberately

Per `qou-q407`: rewriting a claim's Lean changes what the corpus claims, so each
of these needs an owner-level call (prove / state-with-`sorry`+Ref / demote to
conjecture / delete as never-cited). This entry is the census and the detector
gap; the dispositions are separate work.

**Suggested order**, cheapest and least contentious first:
1. Land #3793's class body (already written, reviewed, and content-bearing).
2. Add a disclosure note to `LightningPath` pillar 1, matching the pillars 3–4 note.
3. Adjudicate the nine zero-reference carriers — several may simply be deletable.
4. Strengthen `QuantumObservableUniverse` condition (v). Blocked on the editorial
   question in `qou-n1dj` item 2 (does "non-degenerate epimorphism" mean iso?);
   answering it makes this well-posed.
5. Only then consider a detector. A carrier-vacuity criterion is not obviously
   mechanisable — "the fields do not constrain the objects the label names" is
   semantic — but *zero references across the tree* is trivially mechanisable
   and would have surfaced all nine.

## 2026-08-21 — the nine adjudicated, and a correction to my own census

Re-measured on `main @ 78e3872b`. **Correcting the census I wrote in PR #5226**:
it said the nine are "referenced nowhere in the tree" and "not mentioned even in
their own file". The scan behind that walked **`lean/` only**. Re-run over the
whole corpus, three of the nine *are* referenced — from co-located `.lean`
stubs, which `lake` does not compile:

| | library refs | stub refs |
|---|---:|---:|
| `BraneBoundaryStructure` | 1 (its own decl) | **7** |
| `BriggsKleinChart` | 1 | **2** |
| `MassIdentityC` | 1 | **1** |
| the other six | 1 | 0 |

The zero-**library**-reference figure was right; describing it as "the entire
corpus" was not. Consumption from an uncompiled stub is documentary, not formal
— still worth knowing, but "orphan" overstated it for those three.

### The decisive test: what does each label's block actually reference?

Not "does anything consume this carrier" — a *definition* needs no consumer.
The sharp question is whether the block that owns the carrier's `\label` points
**at it** or **elsewhere**.

| carrier | its `\label` | the block's `lean.ref` | verdict |
|---|---|---|---|
| `EigenspaceDecomposition` | `prop:descent-eigenspaces` | `…idempotent_direct_sum_decomposition` → **UNRESOLVED** | **broken ref — FIXED here** |
| `TruncatedLerayProfile` | `prop:leray-profile` | `…FluidDynamics.leray_profile` → resolves | **stale label** on a superseded structure |
| `VolumeFromRigidity` | `lem:volume-from-rigidity` | `QOU.volume_from_rigidity` → resolves | **stale label** |
| `BraneBoundaryStructure` | `prop:brane-boundary` | `…Torsion.brane_boundary_structure` → resolves | **stale label** |
| `IsLeibnizAlgebra` | `prop:q-jacobiator` | `QOU.q_jacobiator` → resolves | **stale label**, and a genuine **duplicate**: the label appears **twice** in `Elaboration.lean` (lines 245 and 321) |
| `BriggsKleinChart` | `def:briggs-klein-chart` | `QOU.BriggsKleinChart` → itself | **canonical, no defect** |
| `MassIdentityC` | `cor:mass-identity-C` | `QOU.MassIdentityC` → itself | **canonical, no defect** |
| `ChiralSectorCoords` | `def:chiral-sector-coords` | **no block carries that label** | orphan label |
| `SelfDualCurvature` | `prop:self-dual-curvature` | **no block carries that label** | orphan label |

**The pattern:** an older CamelCase `structure Foo` carrying `\label{prop:foo}`
sits beside a newer snake_case `theorem foo_bar` in its own module, and the
block references the theorem. The structure is a **superseded leftover still
holding the label**. Four of the nine are that. This is not "nine vacuous
carriers"; it is one broken ref, four stale labels, two clean definitions, and
two orphan labels — and only the first needed fixing.

### Fixed here

`prop:descent-eigenspaces` repointed from the nonexistent
`QOU.Torsion.idempotent_direct_sum_decomposition` to
`QOU.Torsion.EigenspaceDecomposition`, verified through the canonical resolver.

**Third instance of the sibling-masking failure** (after `thm:su2-emergence`
and `def:ns-regular-qou`): the block has a co-located sibling
`descent-eigenspaces.lean`, `walkBlocks` resolves the sibling first, so every
checker audited the stub and passed while the library ref sat dead. Found by the
label test, not by any gate. That is now three independent confirmations that
**a sibling stub hides a broken library ref from every gate we run** — see
`qou-2u26`.

### Recommended, not done

Removing the four stale `\label` lines so each label has exactly one owner.
Low risk — it is attribution, not a claim rewrite — but it edits four library
files and changes the label→decl map that the resolver's decl-map candidate
uses, so it wants a nod first. `prop:q-jacobiator` is the strongest case: two
declarations in **one file** claim it.

The two orphan labels (`def:chiral-sector-coords`, `prop:self-dual-curvature`)
name blocks that do not exist — either the block was deleted or never written.
Worth a decision: drop the label, or write the block.

## 2026-08-22 — correcting my own recommendation: MOVE the labels, do not remove them

The previous entry recommended "removing the four stale `\label` lines so each
label has exactly one owner". **That is wrong for three of the four**, and I
checked before acting rather than after.

For `prop:leray-profile`, `lem:volume-from-rigidity` and `prop:brane-boundary`
the label appears **exactly once in the whole tree** — on the superseded
structure, **not** on the theorem the block references. Removing it would delete
the label from the corpus entirely and break the label test for those blocks.
The correct operation is **move**: put the label on the declaration the block
actually points at, so it has one owner *and* the right one.

`prop:q-jacobiator` is different again. Its second occurrence reads
`\label{prop:q-jacobiator}`, **conclusion at line 571** — a deliberate
cross-reference from a hypothesis-carrier to a conclusion elsewhere, not a
competing claim. Removing it may well be wrong too. **Left alone.**

So the four "stale labels" are three moves and one probable non-defect.

### Done: `prop:leray-profile` moved

Best-evidenced of the three, and the only one changed here:

- the block `fluid-dynamics/leray-profile.ts` references
  `QOU.FluidDynamics.leray_profile`;
- that theorem's docstring **already named the block in prose**
  (`**Leray-profile reconstruction** ([prop:leray-profile])`) — it simply
  lacked the machine-readable form;
- the label sat on `TruncatedLerayProfile`, which is the *data the proposition
  is stated over*, not the proposition.

Moved. Verified exactly one declaring owner remains, and it is on the referenced
theorem. Both modules compile (`lean-direct-cone -k`, 21-module cone, err=0).
`content_validate` unchanged at the pre-existing 29 issues — no regression.

**One trap worth recording:** my first draft of the explanatory note in
`GaugeFieldFluidDynamics.lean` wrote the label out in full. That would have
registered the docstring as a **second owner** to any label-based tool — the
same false-positive-from-your-own-changelog mode that the `residual_eq_zero`
census hit. Reworded to name the label indirectly.

### Remaining, unchanged

`lem:volume-from-rigidity` and `prop:brane-boundary` want the same move; neither
target theorem names its block in prose, so the evidence is one step weaker than
the leray case and each deserves its own look. `prop:q-jacobiator` left alone
pending a read of whether the cross-reference is intentional.
