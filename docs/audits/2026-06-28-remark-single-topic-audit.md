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
| `clarity-remark-single-topic` | 569 | 65 | 50 | 0 |

Blocks scanned: **684**. Total candidate fails: **115**.

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

## `clarity-remark-single-topic` — 115 candidate(s)

| block | sev | evidence | metrics |
|---|---|---|---|
| [`rem:bar-involution-properties`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/braids-and-knots/bar-involution-properties.md) | major | remark bundles 7 topical sub-sections ("The two canonical projections", "Classification of QOU quantities by bar-type", "Key algebraic identities", "Geometric reading", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=8, topicalHeaders=7 |
| [`rem:braid-group-n-strand`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/braids-and-knots/braid-group-n-strand.md) | major | remark bundles 5 topical sub-sections ("Defined objects", "Specialisations", "Significance", "Specialisations landed", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=5, topicalHeaders=5 |
| [`rem:braid-link-types`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/braids-and-knots/braid-link-types.md) | major | remark bundles 5 topical sub-sections ("Constructed infrastructure", "The atomic theorem (Atom 1 discharged)", "The composed chain", "Track-C atoms (Step A)", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=5, topicalHeaders=5 |
| [`rem:h3-hecke-idempotents`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/braids-and-knots/h3-hecke-idempotents.md) | major | remark bundles 4 topical sub-sections ("Substantive content (no vacuous classes)", "Connection to the Q-YST class", "Explicit projector normalization — the $S_3$ Poi", "Remaining work") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=4, topicalHeaders=4 |
| [`rem:fivefold-symmetry`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/brings-surface/fivefold-symmetry.md) | major | remark bundles 4 topical sub-sections ("The crystallographic obstruction", "The Bring surface and its five sheets", "Five-fold symmetry in the affine chart", "Beyond shell dynamics") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=4, topicalHeaders=4 |
| [`rem:trivial-knot-photon-interpretation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/brings-surface/trivial-knot-photon-interpretation.md) | major | remark bundles 5 topical sub-sections ("The sixteen cross-products", "Collecting by output channel", "Physical interpretation of each channel", "Cancellation conditions", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=5, topicalHeaders=5 |
| [`rem:epistemic-status-of-calibrations`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md) | major | remark bundles 6 topical sub-sections ("CAL-1 ($m_e$) — unit choice + cohomological peri", "CAL-2 ($m_\mu/m_e$) — substrate $q_0$ pin (self-", "CAL-3 ($\mathfrak{D}_\pi$, proxy $m_\pi$) and th", "Summary table", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=7, topicalHeaders=6 |
| [`rem:feynman-qou-comparison`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/feynman-qou-comparison.md) | major | remark bundles 4 topical sub-sections ("Term dictionary", "Comparison", "Sources of discrepancy", "Improving: the pion channel") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=4, topicalHeaders=4 |
| [`rem:w-boson-mass-discrepancy`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/w-boson-mass-discrepancy.md) | major | remark bundles 7 topical sub-sections ("The vertex $\delta q$ formula", "Predictions for each production channel", "CDF–LHC discrepancy", "Higgs boson: multi-experiment comparison", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=8, topicalHeaders=7 |
| [`rem:mass-formula-validation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/mass-formula-validation.md) | major | remark bundles 9 topical sub-sections ("The ruler: $m_e$ as external scaling parameter", "Genuine predictions of the substrate parameter $", "BW mass table (k=12, zero fitted parameters)", "Q-value table (atomic mass differences)", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=9, topicalHeaders=9 |
| [`rem:atom-mass-full-hecke`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/atom-mass-full-hecke.md) | major | remark bundles 4 topical sub-sections ("Three-channel decomposition", "Mass decomposition (fibre / horizontal / mixed)", "Results for $Z = 1$--$10$", "Key observations") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=4, topicalHeaders=4 |
| [`rem:ns-blowup-physical-evidence`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/ns-blowup-physical-evidence.md) | major | remark bundles 5 topical sub-sections ("Physical meaning of a blow-up", "Predicted physical signatures", "Quantitative handles", "Physical finiteness of the mathematical blow-up", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=5, topicalHeaders=5 |
| [`rem:k12-barrier-bypass`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/k12-barrier-bypass.md) | major | remark bundles 4 topical sub-sections ("Scope of the matrix-evaluation programme's verif", "Limits of the matrix-evaluation programme", "Contribution of the homological / LR-fusion fram", "Empirical-verification reframing") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=4, topicalHeaders=4 |
| [`rem:building-block-knots`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/observations/building-block-knots.md) | major | remark bundles 8 topical sub-sections ("Visual convention", "Table 1: Fundamental knots (single-component, to", "Table 2: Derived knots (from Skein operations on", "Table 3: Links (multi-component, for force carri", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=8, topicalHeaders=8 |
| [`rem:conway-normal-form`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/appendix-surreals/conway-normal-form.md) | major | remark bundles 6 topical sub-sections ("Leading exponent, leading coefficient", "Dictionary: Big-O / little-o $\leftrightarrow$ l", "Advantages over classical Big-O", "Example rewrites", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=6, topicalHeaders=6 |
| [`rem:calculus-up-to-epsilon`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/appendix-surreals/calculus-up-to-epsilon.md) | major | remark bundles 5 topical sub-sections ("1. Differential calculus: Jackson derivative as ", "2. Formal integration: antiderivative exists, me", "3. Limits become evaluations", "4. Formal power series: the safe regime", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=6, topicalHeaders=5 |
| [`rem:q-beta-gamma-gamma-canonical-derivation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/stochastic-mechanics/q-beta-gamma-gamma-canonical-derivation.md) | major | remark bundles 4 topical sub-sections ("The chain", "Story A vs Story B resolution", "Track-C open question", "Track-B open question") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=4, topicalHeaders=4 |
| [`rem:t211-ideal-annihilation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/climax-volume-mass/t211-ideal-annihilation.md) | major | remark bundles 5 topical sub-sections ("1. Algebraic survival, physical death", "2. Behaviour on the jet bundle", "3. No :refterm[descent]{#descent} to shells", "4. No $S_{11}$ symmetry — crystallographic obstr", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=5, topicalHeaders=5 |
| [`rem:knot-operator-basis-table`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/appendix-knot-operations/knot-operator-basis-table.md) | major | remark bundles 4 topical sub-sections ("Table L.1: NF basis multiplication table ($T_{1,", "Table L.2: $T_{2,3}$ operator (trefoil / electro", "Table L.3: $T_{2,1}$ operator (single crossing)", "Summary: operator channel opening") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=4, topicalHeaders=4 |
| [`rem:witness-computation-method`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/appendix-nf-witnesses/witness-computation-method.md) | major | remark bundles 4 topical sub-sections ("Crossing convention", "Inductive construction", "Arithmetic", "Scalability") — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=4, topicalHeaders=4 |
| [`rem:term6-binding-density`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/mass-theory/term6-binding-density.md) | major | remark bundles 6 topical sub-sections ("Term 6 explicit form", "$A^3$ normalization", "Magic-shell correction $\delta_M$", "Empirical calibration", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=6, topicalHeaders=6 |
| [`rem:hecke-markov-interpretation`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/mass-theory/hecke-markov-interpretation.md) | major | remark bundles 6 topical sub-sections ("Overview: SYT paths on the Young graph", "Dictionary", "Non-local correlations from local transitions", "Planck steps", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=6, topicalHeaders=6 |
| [`rem:frobenius-packing-density`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/mass-theory/frobenius-packing-density.md) | major | remark bundles 5 topical sub-sections ("Frobenius packing density", "The packing dictionary", "The two-density rule", "Topological triggers for alt saturation", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=5, topicalHeaders=5 |
| [`rem:hecke-quandle`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/mass-theory/hecke-quandle.md) | major | remark bundles 5 topical sub-sections ("The quandle axioms as Reidemeister moves", "The Hecke quandle $Q_H(q)$", "Flavour-parameterised quandle", "Relevance of quandles to the mass formula", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=5, topicalHeaders=5 |
| [`rem:ck-extraction-from-algebraic-rules`](https://github.com/litlfred/qou/blob/claude/clarity-stmt-pure-subsections-2026-06-28/content/quantum-observable-universe/mass-theory/ck-extraction-from-algebraic-rules.md) | major | remark bundles 5 topical sub-sections ("The four reduction rules", "The extraction function", "Per-order agreement", "Significance of the reframing", …) — a remark should cover ONE topic; split into separate remark blocks, each `interprets:` its parent | topLevelHeaders=5, topicalHeaders=5 |
| … and 90 more | | | |

