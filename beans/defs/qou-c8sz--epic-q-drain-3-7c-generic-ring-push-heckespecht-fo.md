---
# qou-c8sz
title: 'EPIC [Q-Drain-3]: §7c Generic-Ring Push, Hecke/Specht Foundations & Nakayama/Frobenius Algebra'
status: todo
type: epic
priority: high
created_at: 2026-11-23T20:55:46Z
updated_at: 2026-11-23T20:55:46Z
parent: qou-hksc
blocking:
    - qou-xip2
---

**Theme:** §7c Generic-Ring Push, Hecke/Specht Foundations & Nakayama/Frobenius Algebra
**Rationale:** Eliminates CharZero/R over-restrictions (§7c), reconciles qInt conventions, and closes 4T/Hecke/Frobenius coproduct & rank-5 Gram gaps.
**Child Beans (12):** `qou-bgq9`, `qou-73kb`, `qou-f3mc`, `qou-qint`, `qou-pbjv`, `qou-ltwg`, `qou-3exy`, `qou-aawz`, `qou-xapv`, `qou-6moa`, `qou-sw8n`, `qou-fadg`

### Prioritized Beans in This Batch
- **`qou-bgq9`** (`critical`, `in-progress`) — QFT-2 (math): 4T relations and the braid-to-chord-diagram jet (Drinfeld–Kohno / Kontsevich) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-73kb`** (`high`, `todo`) — CHAR-ZERO: audit which Specht CharZero hypotheses are load-bearing and which are proof artifacts
- **`qou-f3mc`** (`high`, `todo`) — GAP: Mathas 3.7 forward half -- the source''s selection rule for the inductive step is wrong; find a correct one *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-qint`** (`high`, `todo`) — Reconcile the 8 q-integer definitions — `qInt` names two conventions *(Rule 13a: 0-instance classes: `QCollatz`)*
- **`qou-pbjv`** (`high`, `todo`) — Infra: Hecke algebra H_n(q) as braided monoidal category in Lean (n≥3) — τ-functor F1/F2 source
- **`qou-ltwg`** (`high`, `todo`) — M4 [Mathlib4 Infra]: General-n Iwahori–Hecke H_n(q), Hoefsmit/Murphy Bases, Ocneanu Markov Trace & Macdonald/Plancherel *(Rule 13a: 0-instance classes: `BraneTower, GBResidueSpectralSum, GradedTraceResidueSplit, HasPartitionFunction, HasQPlancherelCLT, HasRealAxisData`)*
- **`qou-3exy`** (`high`, `todo`) — M5 [Mathlib4 Infra]: Quantum Groups U_q(sl_N), Universal R-Matrix, Ribbon/Modular Categories & GPMT Modified Traces *(Rule 13a: 0-instance classes: `BarSymmetricDegreeDoubling, BraidRelation, BrunnianVassilievBridge, PivotalCategory, QuantumSu2Relations, RootOfUnityMTCTruncation`)*
- **`qou-aawz`** (`high`, `todo`) — GAP: is there a NON-TRIVIAL FrobeniusHopfData? the corpus only exhibits A = 1 *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-xapv`** (`high`, `in-progress`) — GAP: which Frobenius coproduct does the framework fix (density u in m = |∫(u·ϱ)|)? *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-6moa`** (`high`, `in-progress`) — DEFECT in AGENTS.md: markovWeights_eq_jones_of_threeRow_eq_zero is cited for its own HYPOTHESIS
- **`qou-sw8n`** (`high`, `in-progress`) — def:confinement-level is a FOURTH reading of J^bullet that no audit has, and it evades both exclusion routes *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-fadg`** (`medium`, `todo`) — frobenius_admissibility_diagnostic reasons from a rank-6 Gram that is rank 5

### Worker Protocol
- Claim individual child beans via `beans update <bean-id> --status in-progress --body-append "Claimed by <branch> (YYYY-MM-DD)"`.
- Never mark a bean `completed` while an uninstantiated conjecture `class` or explicit `stays open` item remains (AGENTS.md Rule 13a).
- Enforce single-thread CPU caps (`LEAN_NUM_THREADS=1`, `nice -n 15`), zero float64 (`mpmath` >= 50-80 dps), and zero fitting.
