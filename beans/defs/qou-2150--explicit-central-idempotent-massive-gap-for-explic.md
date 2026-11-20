---
# qou-2150
title: 'explicit-central-idempotent: Massive gap for explicit_central_idempotent_via_murphy'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-12T10:22:30Z
updated_at: 2026-11-20T16:00:00Z
parent: qou-d8c7
---

## 2026-10-10 — reparented to the mass-endomorphism epic

This bean is carrier M4 of epic `qou-d8c7` (issue litlfred/qou#7547). Parent moved from `qou-rtxm` to `qou-d8c7`; nothing in the body above was changed by the move.


## 2026-10-10 — carrier M4 of epic `qou-d8c7` (issue #7547)

This bean had no body. It is now the single carrier for the explicit central idempotent of `chap:mass-endomorphism`. It absorbs `qou-1bua` and links `qou-hqi8` (completed) and `qou-t99b` (scrapped).

State on `main` 2026-10-10: `class ExplicitCentralIdempotentConjecture` (`QOU/BraidKnot/ExplicitCentralIdempotent.lean:102`) is a primary conjecture with **no instance**, by design. The open mathematics is idempotency of the explicit element built from Murphy's basis (`explicit_central_idempotent_via_murphy`). Stays open (rule 13a): this is the only open bean on that conjecture, which is why it was kept and given a body instead of being scrapped.

### Progress (Round 71 — PR litlfred/qou#8300)
- Formalized in PR `litlfred/qou#8300` (`feat/round71-deltalambda-idempotent-ajtrefoil-n5-gbdepth-43c1`, Commit 1 `a2b0ac0a51416e015d2c71b026de5cf8836daab0`, Head `432940fd4ad329afd23f7d920528ba787ac8691a`, `scriptHash: 06c965f4587d`).

## 2026-11-20 — W1 survey (session_01VQDpPcT9hCf4RF1bQwk66r, epic PR #8534)

Claim released. Rule 13a: open conjecture, stays open. Finding: the carrier cannot express a proof. `centralIdempotent` is an `opaque` element of a commutative ring `R`, and `proj` is valued in `R`, so the class's idempotency and orthogonality fields are statements about scalars, not Hecke elements. Next honest step, as a recommendation (judgement): re-state over the real Hecke algebra `QOU.SchurWeyl.Hecke R q qi N`, which exists on main (see `presEquivHecke`, `QOU/IwahoriHecke/JonesWordsIndependent.lean`), with Jucys–Murphy elements, and prove n=2 first. Open batch PR #8300 (W4's queue) also names this bean; not reviewed here.

## 2026-11-20 — owner ruling D2: re-state on the real Hecke algebra; n = 2 proved (PR #8587, commit d4db59e2b1)

Owner chose 'Re-state on Hecke' (live, structured choice). New module `QOU.BraidKnot.ExplicitCentralIdempotentHecke` adds `lagrangeProj`, built from the Murphy elements `qJM` in `QOU.SchurWeyl.Hecke`, and `MurphyLagrangeComplete`. `murphyLagrangeComplete_two` is proved sorry-free: in H_2(q) the projectors for (2) and (1,1) are idempotent, orthogonal and sum to 1, for q·qi = 1 and q² ≠ qi². NEXT: state the general conjecture with the family = q-content vectors of all SYT of size n+1. That needs a choice among the corpus SYT types (`QOU.SchurWeyl` TableauCells `cellOf` is the natural one, since it is what `QJucysMurphyEigen` uses) plus a Fintype. Then re-point the conj block's lean.ref and retire the scalar carrier. Stays open (rule 13a). Claimed by this session.
