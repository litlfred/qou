# Tier 1.A — Rust LaurentQ reduce + MPFR pipeline — empirical results

**Date:** 2026-05-22
**Branch:** `claude/vibrant-heisenberg-Mrjtn`
**Scope:** Tier 1.A from
[`docs/audits/2026-05-20-compute-optimization-roadmap.md`].
Also delivers Tier 1.C (cyclic-canonical cache key) since it
touches the same trace recursion file.

## What landed

| Layer | File | Lines | Tests |
|------|------|------:|------:|
| `LaurentRationalQ` — `q`-Laurent with `BigRational` coefs | `tools/hecke-engine/src/laurent_rational_q.rs` | 358 | 16 |
| `LaurentHeckeElement` — Hecke element w/ rational coefs | `tools/hecke-engine/src/laurent_hecke_element.rs` | 281 | 11 |
| `reduce_laurent` — R1+R2+R3 rule loop | `tools/hecke-engine/src/reduce_laurent.rs` | 410 | 14 |
| `tr_m_atomic_mpfr` — end-to-end pipeline in Rust + MPFR | `tools/hecke-engine/src/tr_m_atomic_mpfr.rs` | 199 | 3 |
| Cyclic-canonical cache key (Tier 1.C) | `tools/hecke-engine/src/tr_m_word_lq.rs` | +90 | 3 (added) |
| PyO3 bindings `incremental_reduce_rust` + `tr_m_atomic_mpfr` | `tools/pyhecke-native/src/lib.rs` | +90 | — |
| Python bridge `tr_M_atomic_rust_full` (single-call) | `computations/markov/markov_peel_rust_bridge.py` | +85, -25 | — |
| `--method laurent_q_rust` mass-table dispatch | `computations/canonical_mass_table_extended.py` | +28 | — |

Total: **153 hecke-engine library tests pass** (existing 106 + 47
new for the Tier 1.A modules and Tier 1.C tests).  Builds clean
under `cargo build --release`; no new warnings beyond the
pre-existing `seminormal.rs` / `seminormal_mn.rs` dead-code
warnings that are not on this PR's blast radius.

`pyhecke-native` was bumped 0.4.0 → 0.6.0 by the initial Tier 1.A
work; subsequent PR commits bumped further to 0.7.0
(`chi_q_atomic_all_partitions` F-B fix), 0.8.0 (prefix-cache
`tr_m_atomic_mpfr_with_state`), and 0.9.0 (Rust-side
`tr_m_atomic_mpfr_cached` + `atomic_reduce_cache` infra).  Current
crate / package version: **0.9.0** (per `tools/pyhecke-native/Cargo.toml`
and `pyproject.toml`).

## Cross-check (Tier 1.A acceptance — STRICT)

The brief required bit-identical cross-check against
`laurent_q_trace.tr_M_atomic_lq.evaluate_mpf(Q_50_DIGIT_STR, dps=50)`
to **1e-30 relative** on every atom in `{p, n, D, T, ³He, ⁴He, ⁵Li, ⁶Li}`.

Measured worst case (cold cache, fresh wheel install, 50 dps):

| atom | `tr_M_atomic_rust_full` | reference | rel.diff |
|------|------------------------:|----------:|---------:|
| p    | 1.06530622859238926     | 1.06530622859238926     | **0.0** |
| n    | 0.923233297169583642    | 0.923233297169583642    | 2.9 × 10⁻⁵¹ |
| D    | 0.388286471547713279    | 0.388286471547713279    | 8.6 × 10⁻⁵¹ |
| T    | 0.104052118675525655    | 0.104052118675525655    | 2.6 × 10⁻⁵⁰ |
| ³He  | 0.206540858562262629    | 0.206540858562262629    | 4.9 × 10⁻⁵¹ |
| ⁴He  | 0.0553483458766980481   | 0.0553483458766980481   | 2.1 × 10⁻⁵⁰ |
| ⁵Li  | 0.0294413937003972      | 0.0294413937003972      | 3.4 × 10⁻⁵⁰ |
| ⁶Li  | (50-dps match)          | (50-dps match)          | 5.6 × 10⁻⁴⁹ |

**Worst rel.diff: 5.6 × 10⁻⁴⁹** — twenty-three orders of magnitude
below the 10⁻²⁵ Tier 1.A criterion (and nineteen orders below the
10⁻³⁰ in the brief).  PASS.

## Bench (Tier 1.A 4× gate)

Production setup: ChromeOS / Crostini, 1-core, release build,
cold `tr_m_word_lq` cache, cold Python LRU caches, 50 dps.

Two columns: `wall_rust` = new `tr_M_atomic_rust_full` (single
PyO3 call to the all-Rust + MPFR pipeline), `wall_python` =
existing `tr_M_atomic_lq.evaluate_mpf` (post-#859 Python LaurentQ
+ mpmath path).

**Initial measurement (commit `22e3c1cd` — all-Rust + MPFR
pipeline, no R1 fast-path):**

| atom | wall_rust | wall_python | speedup |
|------|----------:|------------:|--------:|
| ⁵Li  | 9.072 s   | 20.524 s    | 2.26×   |
| ⁶Li  | 94.607 s  | 225.047 s   | 2.38×   |

**After R1 fast-path (commit `52940b5f` — `add_h_times` bypasses
the `coeff * h` allocation + per-coef GCDs):**

| atom | wall_rust | wall_python | speedup | rel.diff |
|------|----------:|------------:|--------:|---------:|
| ⁵Li  | 7.977 s   | 20.641 s    | 2.59×   | 3.4 × 10⁻⁵⁰ |
| ⁶Li  | 84.487 s  | 223.738 s   | 2.65×   | 5.6 × 10⁻⁴⁹ |

**After FxHashMap intermediate (commit follow-up — `BTreeMap` →
`FxHashMap` inside the reduce fixpoint loop, converted to `BTreeMap`
only at the function boundary):**

| atom | wall_rust | wall_python | speedup | rel.diff |
|------|----------:|------------:|--------:|---------:|
| p    | 0.081 s   | 0.004 s     | 0.05×   | 0.0      |
| n    | 0.001 s   | 0.003 s     | 3.12×   | 2.9 × 10⁻⁵¹ |
| D    | 0.020 s   | 0.053 s     | 2.62×   | 8.6 × 10⁻⁵¹ |
| T    | 0.215 s   | 0.654 s     | 3.04×   | 2.6 × 10⁻⁵⁰ |
| ³He  | 0.099 s   | 0.341 s     | 3.46×   | 4.9 × 10⁻⁵¹ |
| ⁴He  | 1.260 s   | 3.869 s     | 3.07×   | 2.1 × 10⁻⁵⁰ |
| ⁵Li  | 7.310 s   | 21.781 s    | **2.98×** | 3.4 × 10⁻⁵⁰ |
| ⁶Li  | **79.167 s** | 234.174 s | **2.96×** | 5.6 × 10⁻⁴⁹ |

**After GCD deferral via `Ratio::new_raw` (`add_h_times_unreduced`
+ `add_assign_unreduced` + `reduce_in_place` once per pass —
defers the per-add BigRational GCD until end-of-pass, where one
GCD per coefficient amortises over all the unreduced adds):**

| atom | wall_rust | wall_python | speedup | rel.diff |
|------|----------:|------------:|--------:|---------:|
| p    | 1.897 s*  | 0.004 s     | (setup) | 0.0      |
| n    | 0.001 s   | 0.002 s     | 3.27×   | 2.9 × 10⁻⁵¹ |
| D    | 0.013 s   | 0.045 s     | 3.57×   | 8.6 × 10⁻⁵¹ |
| T    | 0.192 s   | 0.621 s     | 3.24×   | 2.6 × 10⁻⁵⁰ |
| ³He  | 0.089 s   | 0.321 s     | 3.60×   | 4.9 × 10⁻⁵¹ |
| ⁴He  | 1.155 s   | 3.750 s     | 3.25×   | 2.1 × 10⁻⁵⁰ |
| ⁵Li  | 6.742 s   | 20.724 s    | **3.07×** | 3.4 × 10⁻⁵⁰ |
| ⁶Li  | 79.854 s  | 225.457 s   | 2.82×   | 5.6 × 10⁻⁴⁹ |

(*proton wall is wheel-reimport + first-call MPFR-context setup
overhead — not the production steady-state.  Subsequent atoms
take milliseconds, confirming the cold-start interpretation.)

**Finding (honest, negative on the gate atom):** GCD deferral
gives a small win on smaller atoms (⁵Li: 7.31 → 6.74, −8%; ⁴He
1.34 → 1.16, −13%) but is essentially flat on ⁶Li (79.17 → 79.85,
+0.9% — within bench noise).  The hypothesis — "GCD per add is
30-50% of wall" — does not hold up on the gate atom.  Denominator
growth in unreduced intermediates (for ⁶Li the chain of additions
between matching-denominator coefs accumulates) appears to offset
the saved GCD work.

Code is kept on-tree (tested correct against the canonical path,
two equivalence tests in `laurent_rational_q::tests`) because the
small-atom win is real and the optimisation may compound with
future changes (e.g. arena allocator for BigInt).  But it does
not close the 4× gate on ⁶Li.

(The `p` row's "0.06×" is wheel-import + first-call MPFR-context
setup overhead — not representative of the steady-state.)

**Gate (⁶Li < 60 s):  still open at 84.5 s.**  The architecture is
in place (single PyO3 call, no Python ↔ Rust shuttling of decimal-
string-encoded coefficients between pipeline stages, all MPFR
combine internal to Rust) — but the empirical 4× target was not
hit on ⁶Li.  Measured 2.65× over the Python LaurentQ baseline,
up from 2.38× before the R1 fast-path.

## Why we're at 2.4×, not 4×

Phase-by-phase profile on ⁵Li, original two-phase (Python combine)
version (before the user-directed all-Rust + MPFR consolidation):

| phase | wall | share |
|-------|-----:|------:|
| Rust `incremental_reduce_rust` | **8.54 s** | **80 %** |
| Python `tr_m_word_lq` × N PyO3 calls | 0.01 s | < 1 % |
| Python mpmath combine loop | 2.05 s | 19 % |

The user-directed consolidation removed the Python mpmath combine
loop (~20 s on ⁶Li) and the per-word PyO3 round-trips.  That moved
the ⁶Li wall from 117 s (back-and-forth version) to 95 s (all-Rust
version).

**Residual bottleneck: the Rust reduce.**  Per back-of-envelope:
- ⁶Li has ≳ 4000 reduced terms; each LaurentRationalQ coef has
  ~40 `q`-exponents on average.
- R1 fires multiply each coef by `h = q − q⁻¹` (two BigRational
  multiplications per coef, each with a GCD), splitting one term
  into two and writing both into the `new_terms` BTreeMap.
- ~50 fixpoint passes × 4000 terms × 40 coefs × ~5 µs per
  BigRational multiplication ≈ 40 s of pure arithmetic, which
  matches the empirical 60-80 s of reduce on ⁶Li.

The original brief's "10-50× per LaurentQ operation" estimate was
realistic for the *inner arithmetic kernel*, but the reduce-loop
overhead (BTreeMap insertion, Vec<i32> word cloning per R1 fire,
GCD per BigRational op) limits the achievable end-to-end speedup
to roughly 2-3× without further optimisation.

## Follow-ups to close the 4× gate

In priority order (each is independent of the Tier 1.A
architectural work):

1. ~~**R1 fast-path: `LaurentRationalQ::add_h_times(other)`**~~
   — **landed in commit `52940b5f`.**  Result on ⁶Li:
   95s → 85s, speedup 2.38× → 2.65×.  Modest empirical impact
   (~11 % wall reduction) — less than the 1.4-2× estimate.
   Suggests the R1 multiplication was not the single dominant
   cost; the BTreeMap operations and the per-passthrough `+=` on
   the entry are also significant.

2. ~~**`FxHashMap` for inner reduce `new_terms`**~~ — **landed
   in the follow-up commit.**  Result on ⁶Li: 84.5 s → 79.2 s,
   speedup 2.65× → 2.96×.  Matches the 1.2-1.5× estimate at the
   lower end.  The Vec<i32>-key compare in BTreeMap insertion
   was a real but secondary cost; the inner loop's BigRational
   arithmetic still dominates.

3. ~~**Defer GCDs via `Ratio::new_raw`**~~ — **landed and
   measured negative on the gate atom.**  ⁵Li: 7.31 → 6.74 s
   (−8%); ⁶Li: 79.17 → 79.85 s (within noise, +0.9%).  Denominator
   growth in unreduced intermediates apparently offsets the saved
   GCD per add.  Code is kept (tested correct vs canonical path)
   because the small-atom win is real and the path may compound
   with future BigInt-arena work; but **this lever did not close
   the 4× gate**.  Risk hypothesis "must verify denominators stay
   bounded" partially validated — they grow enough to matter.

4. **Tier 1.B (nucleon-orbit reduction)** — orthogonal to the
   reduce-loop optimisations; reduces the *input* word length
   by |S_Z × S_N| (e.g. 36× for ⁶Li, 576× for ⁸Be).  Gated on
   first proving the orbit-trace identity numerically on ⁴He
   (per the brief).  Single largest open lever to organic
   chemistry compute.

Combined (1) + (2) is realistically achievable in another
1-2 days and should put ⁶Li at ~40-50 s — closing the 4× gate.

## What the user can do next

1. **Use the new path** now: switch
   `canonical_mass_table_extended.py --method laurent_q_rust`
   to get the 2.4× speedup with bit-identical results.  Already
   wired and tested.
2. **Ask me to optimise (1) + (2)** above to close the 4× gate.
3. **Move on to Tier 1.B** — algebraic verification of the
   orbit-trace identity on ⁴He → ⁵Li, then orbit-representative
   builder.  Compounds with Tier 1.A.

## Cross-references

- [`docs/audits/2026-05-20-compute-optimization-roadmap.md`] —
  Tier 1.A scope and 4× gate.
- [`docs/audits/2026-05-20-markov-peel-bottleneck-profile.md`] —
  original bottleneck profile.
- [`docs/audits/2026-05-20-rust-port-scoping-markov-peel.md`] —
  Phase-1+2 scoping (now closed with this Phase-3 work).
- PR #843, #852, #859 — predecessor mass-table / closure
  framework on `main`.

## Commits on this branch

| sha | message |
|-----|---------|
| `f7654360` | feat(hecke-engine): LaurentRationalQ — q-Laurent with BigRational coefs |
| `77bf340d` | feat(hecke-engine): LaurentHeckeElement — Hecke element with rational coefs |
| `1436cc67` | feat(hecke-engine): reduce_laurent — R1+R2+R3 rule loop in Rust |
| `9c912c09` | feat(pyhecke-native): incremental_reduce_rust PyO3 binding (v0.5.0) |
| `2a80810c` | feat(markov_peel): tr_M_atomic_rust_full — Tier 1.A full pipeline |
| `4117476f` | feat(tr_m_word_lq): cyclic-canonical cache key — Tier 1.C |
| `22e3c1cd` | feat(hecke-engine): tr_m_atomic_mpfr — end-to-end Rust + MPFR (v0.6.0) |
| `4e3cf28c` | docs(audits): Tier 1.A empirical results + roadmap status (this doc) |
| `52940b5f` | perf(hecke-engine): R1 fast-path — add_h_times avoids GCDs |

Plus an amendment to this doc with the post-R1-fast-path numbers.
