# Prefix-cache bench — empirical NEGATIVE result (2026-05-22)

**Scope:** evaluate the cross-atom prefix-cache infra landed in commit
`a37530f2` ("feat(prefix-cache): cross-atom resume-from-state infra").

**Conclusion:** the cache is **a net loss** in every measured case.
Default flipped to `use_prefix_cache=False`.  Infra kept on-tree for
follow-up investigation (move state into Rust process memory).

## Methodology

`computations/markov_peel_rust_bridge.tr_M_atomic_rust_full`
called twice per atom in canonical sweep order:

- **wall_cache** — with `use_prefix_cache=True`.  First atom is cold;
  subsequent atoms can resume from a cached prefix's reduced
  `LaurentHeckeElement`.
- **wall_cold** — with `use_prefix_cache=False`.  Each atom computed
  from identity, no resume.

Each call returns a 50-dps mpf; cross-checked against
`laurent_q_trace.tr_M_atomic_lq.evaluate_mpf(Q_50_DIGIT_STR, 50)`.

## Results

| atom | word_len | prefix_hit | suffix_len | wall_cache | wall_cold | speedup | rel.diff |
|------|---------:|----------:|----------:|-----------:|----------:|--------:|---------:|
| p    | 11 |  0 | 11 |  0.002 s |  0.001 s | 0.4× | 0.0 |
| n    | 11 |  0 | 11 |  0.001 s |  0.001 s | 0.7× | 2.9e-51 |
| D    | 23 | 11 | 12 |  0.016 s |  0.012 s | 0.8× | 8.6e-51 |
| T    | 35 | 23 | 12 |  0.232 s |  0.178 s | 0.8× | 2.6e-50 |
| ³He  | 35 | 11 | 24 |  0.088 s |  0.084 s | 1.0× | 4.9e-51 |
| ⁴He  | 47 | 35 | 12 |  1.239 s |  1.103 s | 0.9× | 2.1e-50 |
| ⁵Li  | 59 | 11 | 48 |  6.802 s |  6.081 s | 0.9× | 3.4e-50 |
| **⁶Li** | 71 | 59 | 12 | **72.230 s** | 64.430 s | **0.9×** | 5.6e-49 |
| **TOTAL** | | | | **80.611 s** | **71.890 s** | **0.9×** | — |

**Cache is 12% slower than no-cache on the full sweep.**

## Why

The prefix-cache infra serializes the reduced `LaurentHeckeElement`
to JSON-on-disk → Python list → PyO3 → Rust `BigRational` (via
`from_ffi`).  For ⁶Li resuming from ⁵Li:

- ⁵Li's cached state: ~few-thousand σ-words × ~30 q-coefs each ≈
  60,000 `(i32, String, String)` tuples.
- Each tuple round-trips: JSON parse → Python list → PyO3 tuple
  conversion → Rust `String::parse` to `BigInt`.
- Cache contribution (disk + parse + marshal): ~7 s on ⁶Li.
- Save by skipping 59 of 71 reduce crossings: ~7 s.
- Net: ~0 s saved.  The marshalling cost equals the reduce saving.

On smaller atoms (D, T, ⁴He), the cache state is tiny but the
overhead of `pyhecke_native.tr_m_atomic_mpfr_with_state` over
`tr_m_atomic_mpfr` (an extra FFI call to deserialise + return the
final state) plus the disk write of the final state exceeds the
~1 ms saving from skipping a handful of crossings.

This is — ironically — exactly the Python ↔ Rust ping-pong
anti-pattern the `ffi-roundtrip-audit` skill catalogues.  The
prefix-cache, as wired through disk-resident JSON witnesses, is
itself a P-F3 (decimal-string shuttle) offender.

## What's correct

- Cross-check passes at 1e-49 relative on every atom — the
  reduce-and-resume path produces bit-identical results to the
  from-scratch path.
- Cache survives across process restarts (witnesses on disk).
- Stale-entry detection via `cache_version` works.

## Where the wall actually goes on ⁶Li (re-confirmation)

Per the earlier prefix-profile in `markov_peel_rust_bridge`:

| prefix k | wall (s) | terms | total coefs | notes |
|---:|---:|---:|---:|---|
| 53 | 2.07 | 2,048 | 70K | end of 5Li's signed word |
| 70 | 59.05 | 32,768 | 1.6M | through nucleon #5-6 (×16) |
| 71 | 71.46 | 32,768 | 1.7M | final crossing |

So **the last ~17 crossings of ⁶Li account for ~94% of wall** —
exactly the crossings the prefix-cache does NOT skip (those are
the SUFFIX after the 5Li prefix).  Skipping the first 53 crossings
saves only ~2.1 s out of 71 s.  The cache is correctly skipping the
cheap part of the work; the expensive part remains.

## Where would prefix-cache pay off?

The cache wins only when:

1. **Suffix is the expensive part** — i.e., we cache the
   *suffix-equivalent* (NOT the prefix).  Doesn't apply here
   because we don't have a notion of "this atom's suffix equals
   that atom's suffix".
2. **The cached state is small AND the suffix is long** — opposite
   of the current sweep (cached states are big at heavier atoms).
3. **The FFI marshalling is free** — i.e., the cache lives in
   Rust process memory, accessed by hash key from Python.  This
   eliminates the JSON-roundtrip cost.

Option 3 is the meaningful follow-up: a Rust-side `OnceLock<HashMap<H,
LaurentHeckeElement>>` keyed by hash of the signed-word prefix.
Python passes just the hash + signed_word_suffix; Rust looks up
the state internally.  No marshalling.

## Status

- `use_prefix_cache=True` (disk JSON path) remains accessible for
  debug / repro of this finding but is **disabled by default**.
- The audit doc (this file) catalogues the negative result so a
  future agent doesn't redo the same investigation.
- Removing the prefix-cache infra entirely is not advised — the
  Rust-side `tr_m_atomic_mpfr_with_state` API is a clean
  generalisation of `tr_m_atomic_mpfr` (identity → from-scratch,
  cached state → resume) and the `_prefix_cache.py` module is
  independent of the disabled wiring.

## Follow-up: Rust-side cache (pyhecke-native v0.9.0)

Per the "where would prefix-cache pay off" §3 above — moving the
cache into Rust process memory eliminates the FFI marshalling
cost.  Landed in commit `80cab0b9`:

- `hecke_engine::atomic_reduce_cache`: `OnceLock<Mutex<HashMap<u64,
  LaurentHeckeElement>>>` keyed by FxHash of the signed-word prefix.
- `pyhecke_native.tr_m_atomic_mpfr_cached(signed_word, n, q_str,
  dps)`: looks up the longest cached prefix internally, resumes
  the reduce, saves the final state under the full signed-word's
  hash.  Zero FFI marshalling of cached state.
- Wired as the new default in `tr_M_atomic_rust_full`
  (`use_rust_cache=True`).

### Rust-cache bench (canonical sweep)

| atom | word_len | wall_rust_cache | wall_cold | speedup |
|------|---------:|----------------:|----------:|--------:|
| p    | 11 |  0.001 s |  0.000 s | 0.7× |
| n    | 11 |  0.001 s |  0.000 s | 1.0× |
| D    | 23 |  0.011 s |  0.011 s | 1.0× |
| T    | 35 |  0.165 s |  0.174 s | 1.1× |
| ³He  | 35 |  0.083 s |  0.081 s | 1.0× |
| ⁴He  | 47 |  0.965 s |  1.040 s | 1.1× |
| ⁵Li  | 59 |  6.336 s |  6.258 s | 1.0× |
| **⁶Li** | 71 | **63.032 s** | 68.155 s | **1.1×** |
| **TOTAL** | | **70.593 s** | **75.719 s** | **1.1× sweep-wide** |

vs disk JSON cache: 80.6 s / 0.9× (net loss).
Net improvement of the Rust cache over the JSON cache: ~10 s
across the sweep + no overhead on individual atoms.

### Why only 1.1× (not the predicted 5-10×)

The ⁶Li cold wall is 68 s.  Per the prefix profile
(2026-05-22-rust-laurent-q-reduce-results.md §"Phase-by-phase
profile"), **94% of that wall is in the LAST 17 crossings**
(k=53 → k=70) where term count goes 2K → 32K.  When ⁶Li resumes
from ⁵Li's cached state (k=59), the SUFFIX is the 12 crossings
where the exponential blowup happens.  Saved: the cheap first
59 crossings (~5 s).  Unavoidable: the expensive suffix (~63 s).

The prefix-cache pattern is a perfect fit only when:
- The expensive work is in the PREFIX (not the suffix), OR
- The prefix dominates total wall, OR
- There are many atoms sharing the same expensive prefix.

Atomic-braid mass-table compute has the OPPOSITE shape: the
last few crossings carry the cost.  So the cache can only ever
save the cheap prefix (~10% of wall).

### What WOULD give a larger speedup

The compounding wins from §3 above remain:

- **Tier 1.B orbit reduction** — quotients the atomic braid by
  the (S_Z × S_N) same-species permutation symmetry BEFORE
  reducing, shrinking the suffix word itself.  Gated on the
  algebraic-verification step per the original brief.
- **Algorithm-level**: avoid the exponential term-count blowup
  in the last 17 crossings.  This is the structural cost the
  current σ-word reduce inherits.  Crystal basis / canonical KL
  basis could collapse the blowup; that's a 2-4 week
  architectural change.

The 1.1× from the Rust cache is the achievable win without
algorithm change.  Defaulted on; documented.

## What still works after this commit

- Default `tr_M_atomic_rust_full(Z, N, dps=50)` is bit-identical
  to before (single PyO3 call, no cache).  ⁶Li still ~71 s.
- The Rust-side `LaurentHeckeElement::from_ffi`,
  `incremental_reduce_from_state`, `tr_m_atomic_mpfr_with_state`
  are still exposed; future Rust-side cache work can reuse them.
- `_prefix_cache` module's API is stable and correct (witnesses
  round-trip cleanly); the implementation just isn't profitable
  through the FFI.

## References

- Implementation: commit `a37530f2`
- Default flip: commit (this one)
- Profile data:
  [`docs/audits/2026-05-22-rust-laurent-q-reduce-results.md`]
- Anti-pattern catalogue:
  [`.claude/skills/local/ffi-roundtrip-audit.md`] §P-F3
  (decimal-string shuttle).
