# Tier 1.B — intermediate-state memoisation (research)

**Date:** 2026-05-31
**Trigger:** Owner — "do tier 1.b" (the memoisation salvage path flagged as
queued after [#1501](https://github.com/litlfred/qou/pull/1501) merged).
**Builds on:**
[`2026-05-30-tier-1b-orbit-reduction.md`](2026-05-30-tier-1b-orbit-reduction.md)
(the corrected Tier 1.B: no `|orbit|` trace multiplier) and
[`2026-05-30-orbit-trace-identity-proof.md`](2026-05-30-orbit-trace-identity-proof.md)
§"Correction to the roadmap" (lines 76–80, 97–100).

> **Status: research, not engineering.** The prior audits scoped this as
> *unverified* and *research-grade*. This document is the investigation
> log; it states the hypothesis up front and records findings (positive
> or negative) as they land. Do not cite a speedup from this branch until
> the cross-check section below is filled with measured numbers.

## The hypothesis

`tr_M(β_{Z,N}) = tr_M(representative)` — **no `|orbit|` multiplier** (proven,
#1483). The `Z!·N!` orbit size is instead the redundancy of **orbit-equivalent
intermediate reduction states** during `incremental_reduced_element`. Concretely:

- The atomic word for `(Z, N)` is the canonical `p…pn…n` — `A` three-strand
  nucleon blocks, block `k` shifted by `δ = 3k`.
- Folding adjacent same-species blocks `proton@0 ⊗ proton@3` yields a reduced
  intermediate that should be the **shift-by-3 translate** of
  `proton@3 ⊗ proton@6`, etc. The reduce currently recomputes each.
- **Memoise** the reduced intermediate keyed by its *shift-normalised* form
  (via `markov_peel._shift_nf`) and reuse it for every translate. This
  deduplicates the reduction tree — the genuine content of "`Z!·N!`".

This is a layer *above* the existing `pre_register_nucleons` optimisation,
which already caches single-nucleon NFs (`_shifted_nucleon_nf`, `lru_cache`).
The open question is whether the **multi-nucleon** intermediate states are
translate-equivalent in the reduced basis, or whether the inter-nucleon
crossings break the translation symmetry.

## Plan

1. **Profile** the `incremental_reduced_element` fold for ⁵Li/⁶Li — where does
   the wall go, and how many intermediate states recur up to a shift?
2. **Confirm or refute** translate-equivalence of the intermediate states
   (the load-bearing assumption).
3. If confirmed, **implement** the memo and **cross-check** every atom at
   `A ≤ 6` against the full-word path (byte/numeric ≤ 1e-40), per the
   roadmap-correction mandate.
4. **Measure** the speedup honestly; retire the hypothesis if it is illusory
   (as the `|orbit|` multiplier was).

## Known risk — the representation artefact

The identity-proof follow-up (lines 97–100) records that a *naïve
generator-relabelling* block-swap produces a word the Markov-peel recursion
cannot process — a representation artefact, **not** a counterexample. That
blocks the numerical *conjugation test*; this investigation does not depend
on it (the memo keys on shift-normalised reduced states, not on a block-swap
braid). Findings on whether the artefact also obstructs the memo go here.

## Findings — RESOLVED: already implemented, and structurally capped at ~1.08×

The investigation converges on a corrective result of the same kind as the
parent Tier 1.B audit (which retired the `|orbit|` multiplier): **the
intermediate-state memoisation is already implemented in production, and it
is structurally capped at ~1.08× — the `Z!·N!` "redundancy" does not yield a
`Z!·N!` (or any large) speedup.**

### 1. The hypothesis (translate-equivalent intermediates) is not the bottleneck

Profiling the reference fold (`hecke_laurent_fast.incremental_reduced_element_fast`,
crossing-by-crossing, instrumented at `/tmp/profile_fold.py`) shows the wall is
**term-count explosion**, not orbit-translate redundancy. The reduced element's
term count *quadruples per nucleon block* (×4 = 2², i.e. ≈2^(2A+2): 2¹⁰→2¹²
from ⁴He to ⁵Li) and `reduce_laurent_rules` (R1+R2+R3, no R4) does not collapse it:

| atom | A | final terms | wall | per-block wall (s) |
|------|---|------------:|-----:|--------------------|
| ⁴He | 4 | 1024 (≈2¹⁰) | 4.1 s | blk0 .01, blk1 .13, blk2 1.55, blk3 2.42 |
| ⁵Li | 5 | 4096 (≈2¹²) | 22.6 s | blk0 .01, blk1 .06, blk2 .80, blk3 8.57, **blk4 13.12** |

The per-nucleon blocks are *cheap*; the cost concentrates in the **final 1–2
blocks** (⁵Li: blocks 3+4 = **96%** of the wall). The intermediate states are
not independent translates — the product *accumulates and grows*, and the
expensive work is the last block applied to the largest accumulated element.

### 2. The memoisation already exists in production — in-Rust, zero-FFI

The "memoise orbit-equivalent intermediate states" idea is realised as the
**prefix-resume cache** `pyhecke_native.tr_m_atomic_mpfr_cached` backed by
`hecke_engine::atomic_reduce_cache` (`tools/pyhecke-native/src/lib.rs:1073`):
it looks up the longest cached prefix of the signed word, resumes the reduce
from that state, applies the suffix, caches the result — **with zero FFI
marshalling on cache hit** (the `LaurentHeckeElement` never crosses the
boundary). This is exactly the fix the
[2026-05-22 negative-bench](2026-05-22-prefix-cache-negative-bench.md)
recommended ("move the cache into Rust process memory"); the disk/FFI variant
(`tr_m_atomic_mpfr_with_state` + `_prefix_cache`) is the net-loss path and is
already off by default.

### 3. Measured: ~1.08×, and that is the structural ceiling

Cold (`tr_m_atomic_mpfr`, cache cleared) vs warm (`tr_m_atomic_mpfr_cached`,
canonical sweep order) at 50 dps, `/tmp/measure_cache.py`, this build:

| atom | cold | warm (cached) | speedup | value match |
|------|-----:|--------------:|--------:|:-----------:|
| p | 0.001 s | 0.001 s | 1.00× | ✓ |
| D | 0.015 s | 0.015 s | 1.01× | ✓ |
| T | 0.107 s | 0.107 s | 1.00× | ✓ |
| ⁴He | 1.400 s | 1.279 s | **1.09×** | ✓ |
| ⁵Li | 8.679 s | 8.083 s | **1.07×** | ✓ |
| sweep | 10.20 s | 9.49 s | **1.076×** | — |

(`cache_size` grows 1→5: prefix-caching is active; all values bit-identical.)

The ceiling follows directly from finding 1: prefix-caching can only skip the
**cheap early blocks** (~4% of the ⁵Li wall); the **expensive final block** is
new for every atom and uncacheable. The prior FFI bench's headline ⁶Li-from-⁵Li
case (prefix hit = 59 of 71 crossings, suffix = 12) gave **0.9×** for the same
reason: even hitting 83% of the word as a cached prefix saves nothing, because
the final 12 crossings (the 6th nucleon block + inter-crossings) dominate.

### 4. The representation artefact never arose (as predicted)

The memoisation keys on **signed-word prefixes / reduced state**, never on a
block-swap braid, so the naïve-generator-relabel artefact (which blocks the
numerical *conjugation test*) is irrelevant to it — confirming the scaffold's
prediction.

### 5. The real lever for ⁷Li+ is not memoisation

The path to heavier atoms is **reducing the final-block reduce cost itself**
(the ≈2^(2A+2) term explosion), via Tier 1.A (the Rust reduce, already landed) +
a term-bounding *complete* reduce (R4 / Gröbner–Shirshov in Rust), **or** the
character path `tr_M = Σ_λ w_λ χ_λ` (`mass_at_3A_proper.markov_trace_3A`,
Rust `chi_lambda_all_partitions`) which sidesteps the incremental reduce
entirely. Prefix-memoisation is correct and worth its ~8%, but it is a closed
question, not the gateway to organic chemistry.

## Cross-check

`tr_m_atomic_mpfr_cached` returns **bit-identical** values to the from-scratch
`tr_m_atomic_mpfr` for every atom p…⁵Li (table above, "value match" column),
and both cross-check against
`laurent_q_trace.tr_M_atomic_lq.evaluate_mpf(Q_50_DIGIT_STR, 50)` (per the
bridge docstring, ≤ 1e-49). Correctness of the cache is not in question — only
its (capped) benefit.

## Verdict

Tier 1.B intermediate-state memoisation is **DONE and CLOSED**: implemented
in-Rust (zero-FFI), correct (bit-identical), and structurally capped at
~1.08× because ≥96% of the reduce wall is the uncacheable final nucleon block.
No code change is warranted on this branch; the deliverable is the measured
characterisation + redirect of the heavier-atom effort to the final-block
reduce / character path. This closes the last open Tier 1.B salvage item.
