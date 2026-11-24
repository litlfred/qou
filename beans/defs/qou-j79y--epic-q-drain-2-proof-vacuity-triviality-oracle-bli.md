---
# qou-j79y
title: 'EPIC [Q-Drain-2]: Proof Vacuity, Triviality Oracle & Blind Round-Trip Audit Remediations'
status: in-progress
type: epic
priority: high
created_at: 2026-11-23T20:55:45Z
updated_at: 2026-11-24T00:28:35Z
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


## 2026-11-23 Backlog Drain Batch 2 Audit (`claude/backlog-drain-batch2-20261123` vs `origin/main` `cfd526231ce`)
- **Completed (2/13, 100% landed non-conjecture beans):**
  - `qou-sibdup` (`completed`): `scripts/lean-sibling-hypothesis-audit.py` landed in `a6850a0cc0e` (PR #8919, `4adbb646d0b7c91bcb06e2af7394fafac4a0776d`); `--selftest` green.
  - `qou-nbz9` (`completed`): PR #8165 ported in `9dd5e021cb6`; live `lean-vacuity-axiom-audit.ts --check-ledger docs/audits/lean-vacuity-review-ledger.json` (`ef11adcb395`) confirms `35/38` refactored out of `proof-no-self-assuming-projection` and `3/3` remaining hits carry fresh `genuine` verdicts (`0/38` `needs-agent`).
- **Narrowed & Kept Open per Rule 13a / Remaining Sweep Scope (11/13):**
  - `qreal`: all 8 `q_real` ties landed in `cecac49f8ef` (port #8151); narrowed to Rule 13a 0-instance guard on `BraneTowerQLaplacianDecayContext`.
  - `qou-ref10`: all 9 primary `lean.ref`s resolved (`06378846e71` port #8259, `35203efbc72` port #8274); narrowed to Rule 13a 0-instance guard on `GBResidueSpectralSum` + 2 weak-ref follow-ups (`recursive-atom-knot-atlas`, `q-momentum-properties`).
  - `qou-hprp`: live `lean-overclaim-audit.py` confirms `contentless-carrier` drained `39 -> 1` (`HigherStrandCharacterBifurcation` in `QOU/KnotTheory/MetallicPiecewise.lean:70`); narrowed to that 1 carrier + D11 ref mismatch + Rule 13a 0-instance classes.
  - `qou-z3k1`: `hadron_operations_closure` (`b67ed293ec6`), `cp_violation_spectral_form` (`237c6aab718`), and `cases-decide` rung (`d7bf4e59930`) landed; narrowed to `LevelSufficiency` + `mass_tower_coefficient_stratification` + Rule 13a 0-instance classes (`CPViolationSpectralForm`, `ConfinementLevel`, `LevelSufficient`).
  - `qou-6f4w`, `qou-kyst`, `qou-skgn`, `tmvac`: audited against `#9180..#9219` (`06253f4b4b4`, `e5e181fad21`, `9ce8d04d27a`, `70e23fed87a`, `fe4f1320214`) and narrowed to their exact 0-instance Rule 13a classes.
  - `qou-zqno`, `qou-wnm3`, `qou-da6d`: Pass 1 + Pass 3 (`35a56274abb`) landed; narrowed to `--offset 15..39` and `--offset 60..407` (`348` blocks).
