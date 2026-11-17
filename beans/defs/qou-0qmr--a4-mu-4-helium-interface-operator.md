---
# qou-0qmr
title: A=4 / mu_4 helium interface operator
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T00:53:31Z
updated_at: 2026-11-17T07:28:00Z
parent: qou-v2om
---


## Corpus-grep result (2026-08-07): the obvious attack is already WALLED — do not re-run it

Before starting, ran the corpus-grep checklist. A=4 magnitude is **not** open in the
way "move up to μ₄" suggests. It is at a sharp scope-(a) wall, recorded in
[`docs/audits/2026-08-02-a4-interface-magnitude-one-scalar-gate.md`](../docs/audits/2026-08-02-a4-interface-magnitude-one-scalar-gate.md),
Lean `QOU/MassTheory/A4InterfaceMagnitude.lean` (sorry-free):

- The ⁴He `[1⁴]` complete-graph exchange matrix `G` has exact spectrum `{±√5, ±1}`, so
  with one per-pair bond magnitude `m`, `det(I+G) = (1−5m²)(1−m²)` and
  `b₄(m) = −ln det(I+G)`, with physicality ceiling `m < 1/√5`.
- **`magnitude_form_surjective`** proves that for EVERY positive target `t` there is an
  `m ∈ (0, 1/√5)` hitting it exactly, via a closed form. The one-scalar family reaches
  the **entire positive axis**.

Consequence: **matching an AME target at A=4 is vacuous** unless an independent
categorical driver fixes `m`. The reaching `m` is a function of the target — an anchor
inversion, i.e. a **FIT**. So any "μ₄ magnitude closure" probe that tunes `m` to an AME
number is laundering, and the discipline review will catch it.

**Do not re-attack the magnitude.** The genuinely open item is the *independent driver*
for `m`, which is the standing Δ_λ magnitude gate — not an A=4-specific question.

## What IS new and unexamined at A=4

The μ₃ machinery landed 2026-08-07 (#4657, #4662) has not been applied at A=4:

1. **The spectrum there is heavily mixed-sign.** A=4 lives at `n = 12`, where the proved
   content-threshold parity (`YLambdaSignThreshold.wenzl_sign`, #4662) gives **36 of 77**
   negative `y_λ` — measured in `ylambda-sign-content-threshold.witness.json`. The
   one-scalar gate assumes a *uniform positive* per-pair magnitude `m` across blocks;
   whether that is compatible with a sign-alternating weight spectrum is not established
   either way in the audit above.
2. **`door_mechanism_dichotomy` (#4657) has not been run at A=4.** At A=3 the dominant
   submodular push is *negative weight on supermodular geometry*, not Fréchet violation.
   Whether the same holds at A=4 is unmeasured.

Both are measurement/classification questions — cheap, non-vacuous, and they do NOT
touch the walled magnitude. That is the honest next step here, if this bean is worked.

## Round 62 Update (PR #8255)
- Formalized in PR https://github.com/litlfred/qou/pull/8255 (head `b4ec4b15ca43f486c66d8f53b0eeb216293fc6aa`, Commit 1 `c715790dad2efe16f1713c8a17825e912524e641`, `scriptHash: e2eb499467fc`).
