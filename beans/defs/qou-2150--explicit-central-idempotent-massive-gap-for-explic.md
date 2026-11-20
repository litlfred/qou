---
# qou-2150
title: 'explicit-central-idempotent: Massive gap for explicit_central_idempotent_via_murphy'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-12T10:22:30Z
updated_at: 2026-11-20T19:30:00Z
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

## 2026-11-20: the involution, chosen by the owner (option C, live card), and its downstream reach

**Owner chose C:** ⋆ = bar (σ ↦ σ⁻¹, q ↦ q⁻¹) for the physical statement, plus # (σ ↦ −σ⁻¹) stated separately as the λ ↔ λ′ pairing.

**Measured** (probe `computations/probes/central_idempotent_involution_probe.py`, commits 964e2857b1 and 429e1a2a1a; exact arithmetic, n = 2–4 at two values of q):
- bar fixes every e_λ;
- Stokes reversal (bar composed with word reversal) fixes every e_λ;
- # sends e_λ to e_λ′;
- h − z_D(q) = z_D(−1/q), so # maps tr_D at q to tr_D at −1/q;
- the convention-D two-row weights are bar-invariant (n ≤ 5).

**Downstream:**
- The production `y_lambda_wenzl_bridge` weights agree at q₀ and 1/q₀ to about 1e-51 (measured at 50 dps, not committed). The bar-symmetrisation `(y(q₀) + y(1/q₀))/2` in `computations/bar_pairing_binding_observable.py` therefore changes nothing.
- No number in any mass or binding producer depends on ⋆. The e_λ are the same elements whichever involution is chosen.
- `two-filtration-bridge` makes depth-lift components antisymmetric on chiral pairs λ ↔ λ′. That needs #, not bar; under C it should cite #.

**Next (option C, in Lean):**
- bar fixes every e_λ, for all n;
- #(e_λ) = e_λ′, for all n.

Route for both: use `seminormalRep_qJMInv` with a general diagonal-Lagrange image lemma (`f(d) = q^(−2d)` for bar). The # case also needs a transpose bijection SYT(λ) ≃ SYT(λ′) with negated contents; the corpus SYT type has no transpose.

Not yet started in Lean.

## 2026-11-20: option C done in Lean, all n (PR #8587, head c260e33303)

- **Cross-check 3:** `IsBar.fixes_centralIdem`. Any bar map fixes every e_λ.
- **Cross-check 4:** `hashMap_centralIdem`. The constructed sign twist sends e_λ to e_λ′. This needed the SYT transpose (`sytTranspose`, `tr_bijective`).
- **Conj block restated:** both involutions defined; the formula runs over all contents |d| ≤ n−1; characteristic 0.
- **Verification:** 112-module forced cone rebuild on the rebased head, ok=112. No sorryAx.

All four cross-checks are now proved. The mathematical subject of this bean is closed.

Left open, both owner calls:
- promote the conj block from `conjecture` and re-point both blocks' `lean.ref`;
- retire the scalar carrier `ExplicitCentralIdempotentConjecture`.

Status stays in-progress until the owner rules on those.



## 2026-11-20T18:55Z — #8625 merged (969c4aa9fe)
Cross-checks promoted to thm:explicit-central-idempotent-cross-checks; char-0 hypothesis removed (QOU.SchurWeyl.HeckeWedderburnAnyChar); instance over Frac R[q,q^-1] (cross_checks_laurent: Q(q), F_p(q)). Axioms clean. Left: regenerate renamed .jsonld; owner call on retiring scalar carrier ExplicitCentralIdempotentConjecture.


## 2026-11-20T19:20Z — owner "1 2": PR #8660
jsonld regenerated for both e_lambda blocks; scalar carrier ExplicitCentralIdempotentConjecture + its library module + the prop sibling .lean retired. Cone 113/113 ok. Awaiting merge permission.


## 2026-11-20T19:55Z — #8660 merged (eccebd47a5)
Carrier retired, jsonld regenerated. All four cross-checks proved for every n, any characteristic (#8587, #8625). Nothing open: completing.
