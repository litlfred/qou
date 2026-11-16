---
# qou-qbc7
title: Lean-encode the CITED RSZ assertions so a mis-citation is a type error, not prose drift
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T09:35:00Z
updated_at: 2026-11-16T19:22:00Z
parent: qou-6qbv
---

**Motivation — a real incident, this session.** The chain "C1 slope 1/2 =>
RSZ level d=2 => B_{q,2} => F(P1,P2) = C^2 => two Stokes multipliers" stood in
the corpus since 2026-08-01 and drove a staged attack plan. Reading RSZ §3.3
showed the pivotal step inverts the meaning of the central parameter: RSZ p.38
defines `d := mu_2 - mu_1 in N` (the DIFFERENCE of two consecutive slopes), not
the denominator of one slope, and §3.3 is titled "in the case of INTEGRAL
SLOPES". See `qou-qbp5`.

**Prose citations do not typecheck. Typed statements do.** Had the cited
assertions been Lean declarations with their hypotheses as binders, applying them
to a single non-integral slope would have failed to elaborate. That is the point
of this bean: not to re-prove RSZ, but to make the *interfaces* of the results we
cite explicit enough that misuse is mechanically visible.

## Design (respect the anti-vacuity rules)

Two tiers, and do NOT blur them:

**Tier A — provable outright, prove it.** Purely combinatorial content of the
cited statements, no external input needed:

1. `dim F(P1..Pk) = sum_{i<j} r_i r_j (mu_j - mu_i)` (RSZ Thm 3.3.5) as a
   DEFINITION `rszIsoformalDim`, plus the theorem that it is **0 when k = 1**
   (empty sum). This is the fact that killed the C1 framing, so it should be a
   lemma, not a remark.
2. `rszLevel mu1 mu2 := mu2 - mu1` as a def with the two-slope arity visible in
   the signature. A single slope simply cannot be supplied to it.
3. The kernel recurrence + growth -- **ALREADY DONE** (`qou-qbk1`,
   `QBorelKernelLevel`). Cross-reference rather than redo.

**Tier B — external results, §3b conditional classes.** RSZ's classification
theorems are not going to be proved here. Encode each as a `class` whose fields
carry its ACTUAL content and, critically, its HYPOTHESES:

- integral-slope hypothesis of §3.3 (`forall i, mu_i in Z`)
- strict ordering `mu_1 < ... < mu_k`
- `k >= 2` where the statement needs two slopes

Downstream results cite the class as an `[Instance]` binder (§3b-cond), so any
consumer inherits the hypotheses in its type.

**Vacuity discipline (STRICT).** Per §3b-tax the carriers must ASSERT something:
no empty `class C : Prop`, no field typed `: True`, no docstring promising
properties that are not encoded. A class that merely names "RSZ Thm 3.3.5"
without carrying the integral-slope and `k >= 2` hypotheses is worse than no
class, because it would have passed the very misuse this bean exists to prevent.
`lean-vacuity-axiom-audit.ts` will flag those; do not fight it.

## Scope

Only assertions the corpus ACTUALLY cites and depends on. Do not sweep all of
RSZ. Start with the four above (three Tier A, plus the §3.3 hypothesis class),
since those are exactly the ones the C1 chain leaned on.

## Cross-refs

`qou-qbp5` (the objection this came from), `qou-qbk1` (S0, done),
`qou-qbg2` (S1, interpretation withdrawn), `qou-qbq6` (A1,A2, blocked).
Plan: `docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md`.

## Progress Update (2026-11-16 — Round 48, PR #8165)

- Extended `folio/quantum-observable-universe/lean/QOU/MathlibExt/RSZIsoformalInterface.lean` with Tier A positivity lemmas `rszLevel_pos_of_integralSlopeSetting` and `rszIsoformalDim_two_pos` plus the Tier B §3b conditional class `RSZIsoformalClassification` (`extends IntegralSlopeSetting k μ`) and `rszIsoformalDim_pos_of_classification_two` (`0` `sorry`).
- Opened PR `litlfred/qou#8165` (`cf010d07bb34f2e3118733212559b61ede4b8cc4`) with `ready-to-merge` + `release` labels.
