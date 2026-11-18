---
# qou-8jfh
title: The chi-cache regeneration covered 8 of 20 caches — every bar-image (at-qinv) and every free cache is still on the superseded grouped word
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T06:02:19Z
updated_at: 2026-10-04T15:24:53Z
parent: qou-5vkl
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


## 🛑 CORRECTION to my own denominator — it is 59 caches, not 20

The "8 of 20" above counted only what the glob
`chi-*-at-q*-50dps.witness.json` matches. The family is **59**
`computations/chi-*.witness.json`, and it excludes the `-colour-weighted`
variants, the `-matrix-m` variants and several others. Measured across all 59:

| | count |
|---|---|
| on the borromean word (`computedAt` ≥ 2026-09-06) | **21** |
| dated pre-ruling | **18** |
| **unstamped** — no `computedAt` at all | **20** |

The 18 dated-stale span **13 producers**, not two. **Do not read all 38 as
stale-and-wrong**: several are audits, benchmarks or probes on other objects
(`chi_convention_audit`, `chi_numpy_dtype_fix_benchmark`,
`chi_witness_completeness_audit`), and whether each is word-dependent is
**unmeasured**. The finding that stands is the specific one: the *bar-image*
and *free* caches for the four bound atoms were not regenerated.

## DONE 2026-09-07 — the bar-image half is regenerated

`chi_at_q_inv_via_native_mpfr.py`, all four atoms, **exit 0**, ~7 minutes
(deuteron/tritium/³He at 06:05, ⁴He at 06:12). **8 of 8** atom bar-image
caches — the four plain and the four `-colour-weighted` — now carry
`computedAt 2026-09-07`.

**Safety invariant verified, not assumed.** All 12 at-q0 caches are
**byte-identical** to a pre-run snapshot (`cmp`), so this producer touched
exactly the eight files it owns. That is the property `qou-w8rv` was fixed to
guarantee, checked rather than trusted.

**How far they moved**, per-partition character, old against new:

| cache | partitions | max \|rel move\| | moved |
|---|---|---|---|
| deuteron h6 | 11 | 3.0500038 | 10/11 |
| ³He h9 | 30 | 2.9793666 | 28/30 |
| tritium h9 | 30 | 4.4092553 | 28/30 |
| ⁴He h12 | 77 | 5.5656440 | 75/77 |

So the bar-image caches were substantially stale, and the straddle in
`bar_pairing_binding_observable.compute_atom` was real.

## 🛑 But the move is NOT attributable to the intra-ordering alone

⁴He behaves exactly as the structure predicts: the two partitions that did
**not** move are the trivial `(12)` and the sign `(1¹²)`, whose characters are
products of per-letter scalars and therefore order-invariant.

**The deuteron's trivial rep `(6)` DID move**, and pure reordering cannot do
that. Verified directly: for all four atoms the borromean and grouped words are
the **same multiset** (`Counter` equality, lengths 23 / 35 / 35 / 47), so a
reordering leaves any product-of-scalars character fixed.

Two candidate explanations, neither established here:

1. **`_classify_word` is position-dependent.** The at-qinv producer derives its
   signed word through `_classify_word` / `_avg_shifts_at` — names that suggest
   a positional shift — so a reordering could change the *classification* and
   hence the trivial character legitimately.
2. **The caches were 12 days stale, not 1.** They dated to 2026-08-26 and the
   window contains other changes to the corpus.

**Consequence: do not quote the 3.05–5.57 figures as "the effect of the
intra-ordering ruling".** They are the effect of *twelve days of drift, of
which the ruling is one component*. Separating them needs a run of the old
producer against the new word, which I did not do.

## Still outstanding

The **free** caches (`chi-*-free-*`, 8 files, 2026-07-19 or unstamped). Their
producer is `bar_pairing_binding_observable.py`, whose cache key is `q` and
`dps` — so re-running is a **no-op** and they must be deleted first. That is now
safe (the `qou-w8rv` ownership refusal protects the at-q0 atom caches), but it
was not attempted in this pass.



## Q3 RESOLVED 2026-09-07 — provenance investigated, then re-pinned

Owner disposition: investigate provenance first, then re-derive and re-pin.
**The investigation inverted the framing for two of the three**, which is
exactly what it was for.

### What the three anchors actually are

I had called all three "stale pinned anchors". Reading
`carrier_saturation_mechanism_probe.py` and
[`2026-08-26-carrier-saturation-five-failures-diagnosis.md`](docs/audits/2026-08-26-carrier-saturation-five-failures-diagnosis.md):

| assertion | what it is |
|---|---|
| `li6_amplification_reproduced` | **DERIVED INDEPENDENTLY** — "PROMOTED from a regression pin"; ⁶Li free χ via `chi_free_via_frobenius`, the power-sum / Murnaghan–Nakayama route, which **forms no Littlewood–Richardson coefficient** and so does not go through the probe's own LR path. The two agree to **1.3e-67 on all 385 ⁶Li blocks**. |
| `anchor_kappa5Li_reproduced` | **DERIVED INDEPENDENTLY**, same second route, agreeing to **1.5e-69 on all 176 ⁵Li blocks**. |
| `carrier_band_ratio_pinned` | an admitted **REGRESSION PIN** on max/min of `m_e·S` over A=2..6, with no derivation behind it. |

So two of the three were **not** stale constants — they were live two-route
cross-validations, and blind re-pinning would have destroyed the check while
leaving the assertion green.

### The decisive test, and it came out clean

`carrier_table_convention_d_rederivation.py` — the independent MN route — had
last run **2026-08-26**, before the regeneration, while the
`chi-free-via-frobenius` witness it consumes was re-run 2026-09-06. Re-running
it:

| atom | LR route (the probe) | MN route (independent) |
|---|---|---|
| ⁵Li | 64.1028242404330184753… | **64.102824** |
| ⁶Li | 82.8548137338655139679… | **82.854814** |

**Both routes moved together and still agree.** That makes these *re-derived
values*, not constants bent to match a computation — the distinction the
provenance check existed to draw. `W = Σp = 1.0` to **1.81114e-71** across all
six atoms, so the normalisation identity is intact.

### Re-pinned

    anchor_kappa5Li_reproduced    102.51379 -> 64.10282
    li6_amplification_reproduced  107.88563 -> 82.85481
    carrier_band_ratio_pinned        1.8375 -> 1.50250

Each `source` string now records the superseded value, the ruling that moved
it, and — for the two derived ones — that both routes moved together. The
regression pin's note says explicitly that it, unlike the other two, has **no
derivation behind it**.

**Probe: 10 assertions, all passed.**

### An observation I cannot explain and am not claiming to

`anchor_kappaD_reproduced` (6.4161462) and `anchor_kappa4He_reproduced`
(73.5943) are **unchanged** and pass, while ⁵Li and ⁶Li moved by ~30 %. The D
and ⁴He caches were regenerated, so their inputs did move. Why 𝒜 is stable for
A ≤ 4 and not for A ≥ 5 is **unmeasured**.

- **Round 97 (`litlfred/qou#8432`)**: Advanced in `feat/round97-monotone-multbound-ncpart-nonuniform-onebody-43c1` (Commit 1 `e883e42fdde30a6d22e385b72041c6f52899312f`, Commit 2 `56d66b28962228fdc58ad152218bdd3754f7c059`, probe sha256 `e41a92695f7287bc24947a7f23e2cb1aff6e02fcb3b0e34fb76f50f0c076b259`).
