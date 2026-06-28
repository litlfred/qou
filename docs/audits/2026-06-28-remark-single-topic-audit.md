# Definition / statement clarity audit — 2026-06-28

Scanner: [`content/pipeline/definition-clarity-audit.ts`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/pipeline/definition-clarity-audit.ts). Skill: [`local/definition-clarity-audit`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/.claude/skills/local/definition-clarity-audit.md).

High-recall heuristic candidates — a `fail` is a candidate the `definition-clarity-audit` skill confirms, not a verdict.

## Summary

Lead with the **major** column — those are the high-confidence
candidates. `minor` candidates (e.g. an unbolded term, a slightly
over-length statement) are cheaper, lower-stakes fixes.

| Criterion | pass | fail · major | fail · minor | n/a |
|---|--:|--:|--:|--:|
| `clarity-defterm-bold` | 0 | 0 | 0 | 0 |
| `clarity-defn-single` | 0 | 0 | 0 | 0 |
| `clarity-defn-tight` | 0 | 0 | 0 | 0 |
| `clarity-stmt-tight` | 0 | 0 | 0 | 0 |
| `clarity-stmt-pure` | 0 | 0 | 0 | 0 |
| `clarity-grad-style` | 0 | 0 | 0 | 0 |
| `clarity-rhetorical-header` | 0 | 0 | 0 | 0 |
| `clarity-defn-misplaced` | 0 | 0 | 0 | 0 |
| `clarity-remark-single-topic` | 300 | 245 | 139 | 0 |

Blocks scanned: **684**. Total candidate fails: **384**.

## `clarity-defterm-bold` — 0 candidate(s)

_No candidates._

## `clarity-defn-single` — 0 candidate(s)

_No candidates._

## `clarity-defn-tight` — 0 candidate(s)

_No candidates._

## `clarity-stmt-tight` — 0 candidate(s)

_No candidates._

## `clarity-stmt-pure` — 0 candidate(s)

_No candidates._

## `clarity-grad-style` — 0 candidate(s)

_No candidates._

## `clarity-rhetorical-header` — 0 candidate(s)

_No candidates._

## `clarity-defn-misplaced` — 0 candidate(s)

_No candidates._

## `clarity-remark-single-topic` — 384 candidate(s)

| block | sev | evidence | metrics |
|---|---|---|---|
| [`rem:bar-involution-properties`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/braids-and-knots/bar-involution-properties.md) | major | remark bundles 49 topical sub-sections ("Silver outliers: $\{5\}$. Golden outliers: $\emp", "Proposition (Lean: `decompose x`).", "Proposition (Lean: `isBarSymmetric_zero`, `isBar", "Proposition (Lean: `IsBarSymmetric.add`).", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=50, topicalHeaders=49 |
| [`rem:braid-group-n-strand`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/braids-and-knots/braid-group-n-strand.md) | major | remark bundles 6 topical sub-sections ("$n$-strand braid group + Markov closure + Hecke ", "Defined objects", "Specialisations", "Significance", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=6, topicalHeaders=6 |
| [`rem:braid-link-types`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/braids-and-knots/braid-link-types.md) | major | remark bundles 6 topical sub-sections ("Both atomic Track-C axioms are now Lean theorems", "Constructed infrastructure", "The atomic theorem (Atom 1 discharged)", "The composed chain", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=6, topicalHeaders=6 |
| [`rem:h3-hecke-idempotents`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/braids-and-knots/h3-hecke-idempotents.md) | major | remark bundles 4 topical sub-sections ("Substantive content (no vacuous classes)", "Connection to the Q-YST class", "Explicit projector normalization — the $S_3$ Poi", "Remaining work") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=4, topicalHeaders=4 |
| [`rem:color-tube-constraints`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/brings-surface/color-tube-constraints.md) | major | remark bundles 4 topical sub-sections ("Spacetime recovery.", "Shifted quadric.", "Shifted cubic.", "Commutative-limit specialisation.") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=4, topicalHeaders=4 |
| [`rem:braid-group-action`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/brings-surface/braid-group-action.md) | major | remark bundles 4 topical sub-sections ("(i) Spacetime action ($\mathbb{P}^1(\mathbb{C})$", "(ii) Spectral $S_3$ (trefoil action).", "(iii) Coordinate $S_3$.", "Geometric $S_3$.") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=4, topicalHeaders=4 |
| [`rem:fivefold-symmetry`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/brings-surface/fivefold-symmetry.md) | major | remark bundles 5 topical sub-sections ("Theorem (Crystallographic Restriction).", "The crystallographic obstruction", "The Bring surface and its five sheets", "Five-fold symmetry in the affine chart", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=5, topicalHeaders=5 |
| [`rem:brings-qou-4tuple`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/brings-surface/brings-qou-4tuple.md) | major | remark bundles 4 topical sub-sections ("1. CR manifold $M_S$.", "2. Principal bundle $P$.", "3. State bundle $\mathcal{S}$.", "4. Connection, Levi form, and substrate paramete") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=5, topicalHeaders=4 |
| [`rem:trivial-knot-photon-interpretation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/brings-surface/trivial-knot-photon-interpretation.md) | major | remark bundles 18 topical sub-sections ("Vacuum channel ($\gamma$):", "Linear polarization channels ($\sigma_0$, $\sigm", "Positive Hopf link ($L_+$):", "Negative Hopf link ($L_-$):", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=18, topicalHeaders=18 |
| [`rem:qvalue-observation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/qvalue-observation.md) | major | remark bundles 4 topical sub-sections ("Predicted vs observed Q-values.", "Headline demonstration: ${}^{90}\mathrm{Sr}$.", "Method.", "Error structure.") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=4, topicalHeaders=4 |
| [`rem:epistemic-status-of-calibrations`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md) | major | remark bundles 6 topical sub-sections ("CAL-1 ($m_e$) — unit choice + cohomological peri", "CAL-2 ($m_\mu/m_e$) — substrate $q_0$ pin (self-", "CAL-3 ($\mathfrak{D}_\pi$, proxy $m_\pi$) and th", "Summary table", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=7, topicalHeaders=6 |
| [`rem:bw-mass-decomposition-dictionary`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/bw-mass-decomposition-dictionary.md) | major | remark bundles 4 topical sub-sections ("Remark.", "Dictionary.", "Operational meaning.", "Scope of the dictionary.") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=4, topicalHeaders=4 |
| [`rem:confinement-curvature-rank`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/confinement-curvature-rank.md) | major | remark bundles 6 topical sub-sections ("Remark (curvature-rank as confinement layer).", "Confinement layers.", "String tension = curvature 2-cocycle.", "Gluon condensate = chirality channel.", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=6, topicalHeaders=6 |
| [`rem:strangelet-merger-signature`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/strangelet-merger-signature.md) | major | remark bundles 5 topical sub-sections ("Mergers are different.", "The energy budget.", "Three signatures.", "Absence of surface emission.", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=5, topicalHeaders=5 |
| [`rem:double-slit-two-modes`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/double-slit-two-modes.md) | major | remark bundles 4 topical sub-sections ("Band-width predictions versus observation.", "Observation and coherence loss.", "Experimental discriminant.", "Color-content discriminant.") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=4, topicalHeaders=4 |
| [`rem:shell-threading-energy`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/shell-threading-conjecture.md) | major | remark bundles 6 topical sub-sections ("Conjecture.", "The threading link $L_0$.", "Example: ${}^{14}\mathrm{C} \to {}^{14}\mathrm{N", "Two-level structure of $L_0$.", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=7, topicalHeaders=6 |
| [`rem:strutinsky-from-graded-trace`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/strutinsky-from-graded-trace.md) | major | remark bundles 5 topical sub-sections ("Remark.", "Identification.", "Exactness of the analogy.", "Corollaries.", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=5, topicalHeaders=5 |
| [`rem:pair-creation-energy`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/pair-creation-energy.md) | major | remark bundles 4 topical sub-sections ("Standard physics: conversion is forbidden; only ", "In the QOU: crossing energy of the trefoil.", "Three energy scales for "conversion".", "Physical interpretation of each route.") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=5, topicalHeaders=4 |
| [`rem:symmetry-preserving-leptons`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/symmetry-preserving-leptons.md) | major | remark bundles 4 topical sub-sections ("Remark (interpretation).", "Reading.", "Physical consequence.", "Scope of the claim.") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=4, topicalHeaders=4 |
| [`rem:cfl-neutron-star-observables`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/cfl-neutron-star-observables.md) | major | remark bundles 4 topical sub-sections ("1. Equation of state: stiffening at the CFL tran", "2. Cooling anomaly: the CFL gap suppresses neutr", "3. Gravitational wave $f$-mode splitting.", "Summary of predictions.") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=4, topicalHeaders=4 |
| [`rem:feynman-qou-comparison`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/feynman-qou-comparison.md) | major | remark bundles 4 topical sub-sections ("Term dictionary", "Comparison", "Sources of discrepancy", "Improving: the pion channel") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=4, topicalHeaders=4 |
| [`rem:w-boson-mass-discrepancy`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/w-boson-mass-discrepancy.md) | major | remark bundles 20 topical sub-sections ("Table 1: Forward-predicted $\delta q$ and mass s", "Table 2: Higgs boson mass measurements.", "Table 3: $W$ boson mass measurements.", "Table 4: Higgs $\delta q$ by experiment and chan", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=21, topicalHeaders=20 |
| [`rem:color-confinement-observation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/color-confinement-observation.md) | major | remark bundles 4 topical sub-sections ("The analogy.", "Observation: why exactly three colors.", "Observation: confinement strength from $q$.", "Quantitative prediction.") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=4, topicalHeaders=4 |
| [`rem:finiteness-bound-interpretation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/finiteness-bound-interpretation.md) | major | remark bundles 10 topical sub-sections ("Both $A = 5$ nuclei are unbound.", "Translation to standard nuclear physics", "Left side: $[A\!-\!1]_q!$ = configuration comple", "Right side: $[2]_q^{A-1}$ = binding suppression", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=10, topicalHeaders=10 |
| [`rem:mass-formula-validation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/mass-formula-validation.md) | major | remark bundles 22 topical sub-sections ("Certificate field origins.", "Irrep decomposition.", "Necessity of the full $6 \times 6$.", "Key observations:", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | sectionHeaders=22, topicalHeaders=22 |
| … and 359 more | | | |

