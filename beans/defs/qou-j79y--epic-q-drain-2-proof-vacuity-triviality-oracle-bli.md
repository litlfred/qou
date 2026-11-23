---
# qou-j79y
title: 'EPIC [Q-Drain-2]: Proof Vacuity, Triviality Oracle & Blind Round-Trip Audit Remediations'
status: todo
type: epic
priority: high
created_at: 2026-11-23T20:55:45Z
updated_at: 2026-11-23T20:55:46Z
parent: qou-hksc
blocking:
    - qou-xip2
---

**Theme:** Proof Vacuity, Triviality Oracle & Blind Round-Trip Audit Remediations
**Rationale:** Drains RT-1/2/3 semantic mismatches, tactic-ladder vacuity hits, de-exempted projections, and holds:Prop/trivial carriers.
**Child Beans (13):** `qou-zqno`, `qou-wnm3`, `qou-da6d`, `qou-z3k1`, `qou-nbz9`, `qou-qreal`, `qou-6f4w`, `qou-hprp`, `qou-kyst`, `qou-ref10`, `qou-sibdup`, `qou-skgn`, `qou-tmvac`

### Prioritized Beans in This Batch
- **`qou-zqno`** (`critical`, `in-progress`) — RT-1 (Audit Sweep): Blind `Lean -> English -> Lean` Statement Round-Trip & Paper Statement Equivalence Across Provable Claims
- **`qou-wnm3`** (`critical`, `in-progress`) — RT-2 (Audit Sweep): Blind `English Narrative Proof -> Lean Stmt/Skeleton` & `Lean Proof -> English Narrative` Semantic Equivalence
- **`qou-da6d`** (`critical`, `in-progress`) — RT-3 (Audit Sweep): Blind `Theorem Statement <-> English Narrative Proof` Bidirectional Mathematical Self-Consistency
- **`qou-z3k1`** (`high`, `in-progress`) — GAP: tactic-ladder oracle finds 3 vacuous decls the vacuity audit misses (+2 definitional restatements) *(Rule 13a: 0-instance classes: `CPViolationSpectralForm, ConfinementLevel, LevelSufficient`)*
- **`qou-nbz9`** (`high`, `in-progress`) — Adjudicate the 38 projections de-exempted by the isDefProof narrowing
- **`qou-qreal`** (`high`, `in-progress`) — GAP: a redundant `q_real : ℝ` shadows the inherited substrate parameter `q : R` *(Rule 13a: 0-instance classes: `BraneTowerQLaplacianDecayContext`)*
- **`qou-6f4w`** (`high`, `todo`) — P1 [QOU Bridge Drain]: Discharge QOU Physics-Bridge Axiom-Field Classes, Shim Guards & Toy Instances *(Rule 13a: 0-instance classes: `BarInvolution, BigBangHeatDeath, BringZeroModeBlochClass, BringsEulerCharacteristicContext, CemeteryGroupEmergence, ClassicalLimitStpart`; Rule 13a `stays open`/conjecture guard)*
- **`qou-hprp`** (`medium`, `in-progress`) — 23 conjecture carriers assert nothing — the `holds : Prop` shape *(Rule 13a: 0-instance classes: `CrystalBasisCorrespondence, IsospinFromCanonicalBowtie, KazhdanLusztigClassicalLimit, ModularSTransformQQTilde, QuantumLanglandsDual, SpinFromSo3Fiber`; Rule 13a `stays open`/conjecture guard)*
- **`qou-kyst`** (`medium`, `in-progress`) — Discharging the keystone conjecture and its one vacuous premise *(Rule 13a: 0-instance classes: `MISWAbelianisation, QDifferenceKernelIsProlongationSymbol`)*
- **`qou-ref10`** (`medium`, `in-progress`) — TASK: ten lean.refs with no formalisation — and two of them DO exist elsewhere *(Rule 13a: 0-instance classes: `GBResidueSpectralSum`)*
- **`qou-sibdup`** (`medium`, `in-progress`) — Detector: a content-block theorem assuming what a sibling block proves
- **`qou-skgn`** (`medium`, `in-progress`) — prop:skein-generation is a self-assuming projection — the class field IS the conclusion *(Rule 13a: 0-instance classes: `SkeinGenerationContext`; Rule 13a `stays open`/conjecture guard)*
- **`qou-tmvac`** (`medium`, `todo`) — GAP: the topological-mass cluster defines its content trivially (0, 1, identity) *(Rule 13a: 0-instance classes: `TopologicalDecompositionMass, TransientLocalisationNormEquality`; Rule 13a `stays open`/conjecture guard)*

### Worker Protocol
- Claim individual child beans via `beans update <bean-id> --status in-progress --body-append "Claimed by <branch> (YYYY-MM-DD)"`.
- Never mark a bean `completed` while an uninstantiated conjecture `class` or explicit `stays open` item remains (AGENTS.md Rule 13a).
- Enforce single-thread CPU caps (`LEAN_NUM_THREADS=1`, `nice -n 15`), zero float64 (`mpmath` >= 50-80 dps), and zero fitting.
