---
# qou-i6cn
title: 'TRIAGE: 29 library files carry 59 standalone axioms — Mathlib-gap or laundering?'
status: todo
type: task
priority: normal
created_at: 2026-08-08T14:57:07Z
updated_at: 2026-08-08T15:28:23Z
---


## CORRECTION (2026-08-08, same session) — 29 files, not 8

The "8 files" in the title came from the same loose grep that produced
the wrong consumer counts in `qou-up56`. A proper scan (regex for
`^axiom\s+NAME` across `QOU/**/*.lean`, minus files where the axiom
feeds a discharging instance) gives:

**29 files, 59 axioms.**

| axioms | file |
|---|---|
| 9 | `QOU/HeckeAlgebra/MarkovTrace.lean` |
| 5 | `QOU/BraidsKnots/LinearJSJVolume.lean` |
| 5 | `QOU/HeckeAlgebra/Formal.lean` |
| 4 | `QOU/MathlibExt/SDPRankEquality.lean` |
| 4 | `QOU/HeckeAlgebra/JonesMarkovWenzl.lean` |
| 3 | `QOU/BraidKnot/IwahoriHeckeAPI.lean` |
| 3 | `QOU/HeckeAlgebra/Hoefsmit.lean` |
| 2 | `QOU/BraidKnot/QuantumDilogarithm.lean` |
| 2 | `QOU/BraidKnot/PSDFeasibilityProxy.lean` |
| 2 | `QOU/BraidKnot/LpDualityHypothesisClass.lean` |
| 2 | `QOU/HeckeAlgebra/Common.lean` |
| 1 each | `StaircaseCornerHook`, `JetHorizon`, `MathlibExt/SDP`, `MathlibExt/PhiBProd`, `QuantumObservableUniverses/QIntegralTransforms`, `Mathlib/RSKBridge`, `IwahoriHecke/Defn`, `AppendixSurreals/B1HyperbolicRowsTheorem`, `Archimedean/NuclearGroebnerReduction`, `Archimedean/WeierstrassProjection`, `Archimedean/BorromeanVolumeCatalan`, `BraidKnot/CommutativeCrossingEnergy`, `HeckeAlgebra/Wedderburn`, `FlavorDressing/DressedMassFromSubstrateSplit`, `Hecke/MarkovTrace`, `Hecke/Wedderburn`, `Eightfold/Sym2Gate`, `QBeta/MarkovZToCkMapping` |

Note three of the previously-listed eight are absent: two
(`n-v-bring-action`, `n-v-leading-order-derivation`,
`spectral-chart-correspondence`, `figure-eight-branching-rule`,
`q-codifferential-formula-prop`, `y-lambda-recipe-from-partition`) were
content-block sibling `.lean` files rather than library files and are
covered by their `.qa.json` sidecars; the axiom-bearing library set is
the table above. Re-derive the list before working it — do not trust
either the old 8 or this 29 without re-running the scan.

## The triage question, sharpened

The one axiom-discharged *instance* left in the corpus
(`SDPRealUniqueness`) turned out to be legitimate, and for a reason that
generalises to this queue. The test is **not** "is there an axiom" but:

> Does the axiom assert **an open conjecture of this framework**, or **a
> published theorem that Mathlib does not yet have**?

- **Published-theorem / Mathlib-gap** → legitimate. Keep, provided it
  carries a `-- Ref:` citation to the actual source (AGENTS.md §1) and
  the class/statement it discharges is content-bearing. `SDPRankEquality`
  and `SDPRealUniqueness` are the exemplars.
- **Open QOU conjecture** → laundering. The honest state is a
  content-bearing carrier with no instance (§3b-tax).

`HeckeAlgebra/MarkovTrace.lean` (9) and `HeckeAlgebra/Formal.lean` (5)
are the highest-value reads: Markov-trace properties are load-bearing
for the whole mass chain, and whether those nine are Jones/Wenzl
citations or QOU assertions materially changes what the mass results
rest on.

**Do not batch-process.** Every file needs the question above answered
by reading it.
