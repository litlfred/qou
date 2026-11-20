---
# qou-n4pv
title: 'PI-1: Hadamard factorization theorem in Mathlib — entire function of finite order = (∏ over zeros, Weierstrass primary factors)·exp(poly). The theorem that pins phiBProd among its elliptic multiples. Hard multi-week complex-analysis build.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-20T05:12:52Z
updated_at: 2026-11-20T20:37:12Z
parent: qou-c8p8
---



## Verification status (2026-07-20, honest)
Compile-verification NOT completed. HadamardFactorization.lean imports the Mathlib Analysis cone (Jensen/Nevanlinna); the lake-cache oleans are algebra/combinatorics only (0 Analysis oleans). Building the cone takes >10min, exceeding BOTH the foreground tool timeout AND the detached-process lifetime (reclaimed on session idle). 4 build attempts (2 detached died mid-cone at 1587/2072 and 777/788; 2 foreground timed out at 590s/120s). The authoring agent's own run also never completed (left 'still grinding the Analysis cone'). So the file's 'compiles' status rests solely on an unverified lean-direct claim. Verification paths that WOULD work: CI (when billing clears), or seeding an Analysis-olean lake-cache branch. Do NOT mark this green until a completed build confirms it.

## Compile verification COMPLETED 2026-08-08

The open question in this bean — "Compile-verification NOT completed", after
4 failed attempts (2 detached processes died mid-cone, 2 foreground timed
out) — is now settled.

    lake build QOU.Mathlib.HadamardFactorization
    → Build completed successfully (2072 jobs)

**The file compiles.** No errors. Exactly the 3 known `sorry` warnings at
lines 131 / 141 / 161, and nothing else.

Why it worked this time: the Analysis cone was already built. An earlier
session in this container completed a full `lake build` of the package
(4320 jobs) while fixing the corpus-wide compilation failures, so the
cone this bean could never finish was already on disk and the check took
seconds instead of >10 minutes.

### What is actually sound, per `#print axioms`

Sorry-free (only propext / Classical.choice / Quot.sound):
- `weierstrassFactor` and `weierstrassFactor_apply_zero`
- `weierstrassFactor_genus_zero`, `weierstrassFactor_eq_zero_iff`
- `differentiable_weierstrassFactor`

Carrying `sorryAx` — sound only modulo their own `sorry`:
- `norm_one_sub_weierstrassFactor_le` (the PI-2 brick)
- `multipliable_canonicalProduct`
- `hadamard_factorization`

So the definitional and differentiability layer is genuinely proved; the
three cited analytic results are exactly as advertised and nothing has
silently leaked past them.

This closes the verification sub-question only. The three `sorry`s stand,
and this bean's substantive PI-1 content is unchanged.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-20 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 63 Progress (`lane-e667`)
- Formalized `qou-ipsl`, `qou-jbo8`, `qou-n4pv`, `qou-vspi`, `qou-xidi` in `QOU.Foundations.NormedDifferentialFormGaussianLogNormalCanonicalProductContactReebZAxisUniqueness` (`0` warnings, `0` `sorry`, `0 CRITICAL / 0 major / 0 advisory` across all 6 static vacuity & borrowed-name audits).
- Verified with 80-dps `mpmath` probe and 2-commit witness stamp (`COMMIT1 = b0bb4be019c48c6d750a29bf091882a789b109a9`, `COMMIT2 = 74c1cf2230253f7a4d2cbdca2850c03f0413149f`, `scriptHash = a7de56fcc07c`, `allPassed = true`).
- Opened PR https://github.com/litlfred/qou/pull/8320 (`ready-to-merge`, `release`, `ready: 74c1cf2230253f7a4d2cbdca2850c03f0413149f`).
- Keeping bean at `status: in-progress` pending merge and verification.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8320, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-08: "beans: settle qou-n4pv's open compile verification — the file builds"). The work may be partly or fully done. Read the bean before you close it.

## 2026-11-20 — PI-5 ingredients proved (PR #8651); Hadamard itself still OPEN

Proved, sorry-free: exponent of convergence ≤ order (`ExponentOfConvergence`), Jensen zero-count (`JensenZeroCounting`), canonical product entire + order ≤ σ (`CanonicalProductGrowth`, Borel), zero-free finite-order ⇒ exp(poly) (`HadamardZeroFree`). REMAINING for `HasHadamardFactorization`: divisor → zero sequence with multiplicity; f/P entire and zero-free; minimum-modulus lower bound on |P| giving f/P order ≤ ρ (the hard step).
