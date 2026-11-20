---
# qou-2150
title: 'explicit-central-idempotent: Massive gap for explicit_central_idempotent_via_murphy'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-12T10:22:30Z
updated_at: 2026-11-20T17:30:00Z
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

## 2026-11-20 — general n: cross-checks 1–2 and centrality PROVED; cross-check 4 FALSE at n = 2 (PR #8587)

Owner: "Work at the conjecture for all n".

- **`ef932e8ebc`, `QOU.BraidKnot.ExplicitCentralIdempotentGeneral`, sorry-free.** At generic q (q ≠ 0, not a root of unity, char 0), `e_λ = Σ_{T∈SYT(λ)} π_T` in `H_{n+1}(q)` is central, idempotent, nonzero, pairwise orthogonal, and Σ_λ e_λ = 1. Each π_T is idempotent, and distinct π_T are orthogonal. Capstone: `explicit_central_idempotent_cross_checks`.
  - It rests only on existing corpus results: `heckeWedderburn` and `JMProjector.heckeWedderburn_symm_single`.
  - `mulProj_eq_proj`: the .md formula in the multiplicative J_k = L_k equals the additive-JM projector.
  - This connection had not been made: no prior file links JMProjector to this conjecture.
- **`6381686552`, cross-check 4 (bar-pairing) is FALSE at n = 2** for the bar involution σ ↦ σ⁻¹, q ↦ q⁻¹.
  - `bar_fixes_eTriv`: any such semilinear endomorphism fixes e_(2), and `eTriv_ne_eSign` gives e_(2) ≠ e_(1,1).
  - `hash_swaps_eTriv`: the linear σ ↦ −σ⁻¹ is the involution that pairs λ with λ′.
  - Scope: the conj block never defines ⋆, so which involution was meant is an OWNER call.
- **Finding:** the conj block's product over the boxes of λ can divide by zero (diagonal boxes share a content). The prop block's formula is the well-defined one.

**Still open:**
- cross-check 3 (no self-conjugate λ at n = 2; general n needs a bar involution in Lean);
- a general-n statement of cross-check 4 for whichever involution is chosen;
- primitivity is not stated;
- re-pointing the two blocks' `lean.ref` and retiring the scalar carrier (owner).

Stays open (rule 13a).

