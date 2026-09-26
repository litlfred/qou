---
# 2x2i
title: 'Docs: new refuted-class row C15 + ledger update + coordinate w/ 5nx8+s5bb'
status: completed
type: task
priority: normal
created_at: 2026-07-06T11:48:04Z
updated_at: 2026-09-04T07:40:02Z
---

2026-07-13: refuted-class row added as C19 (NOT C15 — C15 taken by Borromean class PR #3536). Scope-tagged per AGENTS.md: odd m & m=2 scope-(b) unconditional (integer-u grading + forbidden c1 rung PR #1602); even m=4,6 scope-(b) on the ζ₄-faithful arm, conditional on conj:binding-qbeta-complex-volume, citing the new Lean lemma. STILL OPEN: unconditional even-m refutation needs Arm-1 symbolic probe qbeta_fmap_power_class_prune.py — NOT run (no-scan discipline). Left in-progress.


## 2026-09-04 — CLOSED: the blocker was already resolved, and the ledger row is current

This bean's one open item read: *"STILL OPEN: unconditional even-m refutation needs
Arm-1 symbolic probe `qbeta_fmap_power_class_prune.py` — NOT run (no-scan
discipline)."*

**It was run.** `computations/probes/qbeta-fmap-power-class-prune.witness.json`,
`computedAt` 2026-08-30, `allPassed: true`. Every obstruction fires with an exact
closed form and `exact_match: true`:

| m | verdict | coefficient |
|---|---|---|
| 1 | REFUTED — leading half-integer `u_L^{1/2}` | `-5/4` |
| 2 | REFUTED — forbidden c₁ rung, `a₁² ` | `25/16` |
| 3 | REFUTED — leading half-integer `u_L^{3/2}` | `-125/64` |
| **4** | **REFUTED unconditional** — sub-leading odd-ε, `m·a₁³·a₂` | `1625/128` |
| 5 | REFUTED — leading half-integer `u_L^{5/2}` | `-3125/1024` |
| **6** | **REFUTED unconditional** — sub-leading odd-ε, `m·a₁⁵·a₂` | `121875/4096` |

So the even-m arm no longer rests on `conj:binding-qbeta-complex-volume`; the
half-integer obstruction at **sub-leading** order does it unconditionally, and the
ζ₄ arm now stands as an independent conditional confirmation rather than as the
only route.

**And the ledger row is already correct.** C19 in
[`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`](../docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
reads *"REFUTED — FULL CLASS, scope-(b) UNCONDITIONAL … odd m, m=2, and m=4,6 all
unconditional; the ζ₄ arm stands as an independent conditional confirmation for
even m."* Nothing to write.

**One dating note, recorded so it is not read as a discrepancy:** the row cites the
Arm-1 probe as executed 2026-07-13 (PR #3781) while the witness `computedAt` is
2026-08-30. That is a later regeneration of the same probe, not a second result —
the coefficients are the ones the row quotes.

Marked completed: the row exists, is scope-tagged, and its stated blocker is gone.
