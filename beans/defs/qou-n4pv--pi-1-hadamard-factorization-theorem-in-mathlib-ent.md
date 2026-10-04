---
# qou-n4pv
title: 'PI-1: Hadamard factorization theorem in Mathlib — entire function of finite order = (∏ over zeros, Weierstrass primary factors)·exp(poly). The theorem that pins phiBProd among its elliptic multiples. Hard multi-week complex-analysis build.'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-20T05:12:52Z
updated_at: 2026-10-04T15:13:29Z
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
