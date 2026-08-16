---
# qou-szd6
title: 'V7 Lean carrier + infra hygiene (foundational): abstract keystone carriers (#3773), de-fabricate vacuous carriers (#3793 needs reconcile vs current main), sign audit (#4054). Formalization spine + olean cone growth.'
status: todo
type: task
priority: normal
created_at: 2026-07-19T02:56:27Z
updated_at: 2026-07-19T02:57:06Z
parent: qou-wzgm
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
