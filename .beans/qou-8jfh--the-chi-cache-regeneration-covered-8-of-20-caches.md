---
# qou-8jfh
title: The chi-cache regeneration covered 8 of 20 caches — every bar-image (at-qinv) and every free cache is still on the superseded grouped word
status: todo
type: task
priority: normal
created_at: 2026-09-07T06:02:19Z
updated_at: 2026-09-07T06:03:08Z
---

## The claim

The 2026-09-06 chi-cache regeneration (owner ruling "regen", bean `qou-92u9`,
following the intra-ordering ruling `qou-hu1f`) covered **8 of the 20** chi
caches on disk. The other **12 are still on the superseded GROUPED word**, and
they are not a random 12 — they are *every* bar-image cache and *every* free
cache:

| group | count | state |
|---|---|---|
| at-q0 **atom**, `chi_at_q0_via_hoefsmit_mpfr.py` | **8** | regenerated 2026-09-06 ✓ |
| at-qinv **atom** (bar image), `chi_at_q_inv_via_native_mpfr.py` | **4** | 2026-08-26 ✗ |
| **free** at-q0, `bar_pairing_binding_observable.py` | **2** | 2026-07-19 ✗ |
| **free**, unstamped — no `computedAt`, no `producer` | **6** | date unknown ✗ |

Method: every `computations/chi-*-at-q*-50dps.witness.json`, split on
`computedAt`. Reproduce with the inventory in this bean's commit.

## Why it matters — a braid-word straddle, not just staleness

`bar_pairing_binding_observable.compute_atom` builds `B_arch + B_bar` from the
**free/atom pair at q₀ and q₀⁻¹**. Three of those four inputs are now on the
grouped word and one on the borromean word. That is a straddle of exactly the
shape AGENTS.md forbids for the muon/proton layers — *"Never straddle the two
layers inside one quantity"* — one axis over: two braid-word conventions inside
one computed number.

## It also re-reads two of the seven post-regeneration "regressions"

Dating all 24 currently-failing witnesses against `3cc4b2aab1~1` gives **7
genuine regressions and 17 pre-existing**. At least two of the seven are
probably **artifacts of this straddle rather than results**, and should not be
read as findings until the 12 are regenerated:

- `probe_d_delta_lambda_terms` — `bar_conjugate_law_broken_by_colour_weighting`
  compares `χ^λ(β_D, q⁻¹)` against `(−1)^L χ^{λ'}(β_D, q)`. Its recorded residual
  is `≈2.6e-4`, a real colour-weighting asymmetry. With at-q0 regenerated and
  at-qinv not, that comparison is now **cross-convention**, so the assertion
  flipping says nothing about the bar-conjugate law.
- `li6_h18_amplification_discriminator` — `lr_free_path_validated_at_4He`
  computes `4.845843445340255525…` against a `1e-5` tolerance. This is the one
  that exposed the gap: `chi_free_lr(2,2)` composes the **regenerated** nucleon
  caches through Littlewood–Richardson coefficients, and compares the result
  against a **2026-07-19** free cache. Two routes, two words.

The LR route is worth keeping in view: it is a genuinely independent structural
check on the free caches (the free word is a disjoint product over nucleon
strand blocks, so its character decomposes by LR), and once the free caches are
regenerated it becomes a real cross-validation rather than a straddle detector.

## Why the guard did not catch it, and why it now can be fixed

`_load_or_compute_chi`'s cache key is **`q` and `dps`**. Neither moved, so every
cache reads valid and the producer returns it without recomputing. **A braid-word
change is invisible to the cache key by construction.** That is the root cause,
and it is separate from the field-name defect fixed in `qou-w8rv`.

Two consequences worth stating plainly:

1. **Regenerating the 12 requires deleting them** (or adding the word to the
   cache key). Re-running the producer alone is a no-op — verified: the
   `qou-w8rv` probe measures 16/16 cache hits with zero recomputes.
2. **The `qou-w8rv` fix is what makes that safe.** Before it, running
   `bar_pairing_binding_observable.py` silently recomputed and overwrote the
   four canonical at-q0 atom caches with a different schema. Deleting the free
   caches and re-running would have destroyed the regenerated atom caches in the
   same pass. It no longer does.

## What is NOT established

- Whether the **at-qinv** caches *should* move. The bar image is `χ(β, q₀⁻¹)`
  for the same braid word, so if the word changed they must — but
  `chi_at_q_inv_via_native_mpfr.py` was not read, and whether it derives its
  word from `atom_braid_word_3A` or carries its own is unchecked.
- The **6 unstamped** caches' provenance. They carry neither `computedAt` nor
  `producer`, so "not regenerated" is inferred from their absence from the
  2026-09-06 run, not read off the file.
- The **cost** of regenerating. ⁴He is `n = 12`, 77 partitions; the at-q0 run
  took ~9 minutes for eight caches, but the free/qinv producers are different
  code and were not timed.

## Disposition

Completing the regeneration looks in scope for the standing "regen" ruling —
these are chi caches the sweep missed, not a new decision. But it moves numbers
in the bar-pairing observable, so it is recorded here rather than done
unilaterally in the same turn it was found.
