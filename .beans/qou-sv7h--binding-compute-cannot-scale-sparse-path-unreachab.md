---
# qou-sv7h
title: 'Binding compute cannot scale: sparse path unreachable, zero Rust, float64 straddle'
status: in-progress
type: task
priority: high
created_at: 2026-08-30T15:41:58Z
updated_at: 2026-09-03T03:35:17Z
---

Full measured analysis: `docs/audits/2026-08-30-binding-compute-scaling-bottleneck.md`.

Blocks `qou-i7ju` (hadron-knot-table regeneration). The regeneration is not the
problem; the producer cannot finish its second atom.

## Localisation

Every stage of `compute_atom` is sub-millisecond except `binding_energy`.
Inside it, `unified_iterative_correction` is the whole cost. 11/11 py-spy
samples on `hecke_core_legacy.py:1102` = `np.asarray(A) @ np.asarray(B)`.

## The six findings

1. **The O(dim*nnz) sparse path is unreachable.** Guard is
   `if s['sparse'] and not exact_chain:`, and `exact_chain` is True for EVERY
   physical chain (measured over all nucleon/prev/n_gens combos). Coefficient
   histogram: ('int','int') 132, ('int','mpf') 132, ('float','float') 48 -- the
   mpf are real 50-dps values, and `c` is int 1 which is not a float. So both
   inner branches are dead, INCLUDING the COO object accumulator written for
   exactly this case. Everything runs O(dim^3) at dims up to 2310.
   Deuterium ~40 days; Fe-56 ~16 years.
2. **Zero Rust in the hot file.** grep pyhecke_native|hecke_engine in
   hecke_core_legacy.py -> 0 hits.
3. **The Rust MPFR matmul exists and is not exported.**
   `dense_dense_mul_mpfr` in dense_la_mpfr.rs, called 16+ times inside Rust,
   has no #[pyfunction]. Python gets inverse/kron/nullspace but not multiply.
   Measured Rust speed >=24x the Python path at dim 16 (401us vs 9600us), and
   that is a lower bound (includes PyO3 + seminormal construction).
4. **Half the matmuls are float64.** Counter recorded
   {'float64': 275, 'object': 271}. Measured relative error vs an all-mpf
   reference: 1.40268e-16 = float64 eps, in a 50-dps producer. Also
   `q_parameter.Q` and `h` are Python floats; intra-nucleon coefficients are
   50-dps mpf but the inter-nucleon nn crossing carries float64 -h. A straddle
   inside one product.
5. **The `dim >= 8` numpy branch is a pessimization.** Its docstring claims a
   speedup; measured at dim 16 it is 31% SLOWER than the Python loop
   (0.0126s vs 0.0096s). object dtype has no BLAS.
6. **The q-Gaussian tier is dead.** k_exact defaults to k_max, so
   active_gaussian is empty (measured: 193 exact, 0 gaussian).

## The one-line fix is necessary but NOT sufficient -- TESTED

`if s['sparse']:` was applied and run. py-spy confirms it takes the COO path
(lines 1495/1500, no _matmul_dim). Deuterium STILL had not completed after
11 minutes. Complexity drops ~500x at dim 2310 but every scalar op is still a
Python-level mpmath call. Both layers must be fixed.

**Patch was reverted, not committed.** With neither version completing there is
no way to verify it preserves the number, and this is a binding-energy producer.
Landing it needs a value-equality check on a subset that completes both ways
(use k_exact to shrink the partition set; do NOT use deuterium).

## Order of work

1. Fix the guard (one line, ~500x) -- with the equality check above.
2. Export dense_dense_mul_mpfr via PyO3, route _matmul_dim + the COO
   accumulator through it (>=24x, on top of 1). This is what makes higher
   isotopes reachable.
3. Fix the precision straddle: Q and h as mpf from Q_50_DIGIT_STR; stop
   seeding accumulators with np.eye / 0.0. Correctness, independent of 1-2.
4. Delete the dim>=8 numpy branch.
5. Decide the q-Gaussian tier: real default below k_max, or delete.

## Scaling law

Partition set is FIXED (193 at k<=11, dims 1..2310; 37s just to materialise) --
it does not grow with A. Crossings grow O(A^2). Cost ~ A^2 * sum_lambda f(dim),
f = dim^3 today, dim*nnz after fix 1. Relative to deuterium: Li-7 ~5x,
O-16 ~17x, Fe-56 ~144x.


## 2026-09-03 — items 1-3 resolved. Deuterium: "~40 days" -> 44 seconds.

### Item 1 (the guard) was already fixed

`if s['sparse']:` is in the tree. Confirmed, nothing to do.

### Item 2/3: the answer was not to export a matmul — it was to CALL the Rust
### that is already exported

This bean proposed exporting `dense_dense_mul_mpfr` via PyO3 (">=24x"). That
would have worked and it would have been the wrong shape. `pyhecke_native`
already exports **`chi_q_atomic_mpfr(shape, factors, q_str, dps)`**, which
computes `χ_λ(Π_i (c_i·σ_{g_i} + d_i·I))` — the ENTIRE per-partition product,
not one matmul. Its `factors` are `(c_str, d_str, gen_1based)` DECIMAL
STRINGS, so nothing crosses an f64 boundary: NO-FLOAT64 is satisfied by the
ABI rather than by care. `chi_q_atomic_all_partitions_mpfr` is rayon-parallel
on top of that.

Item 2's finding ("zero Rust in the hot file") was right. Its proposed remedy
was aimed one level too low.

### Measured — per-partition character, same chains, 50 dps

    shape        dim   python     rust   speedup   agreement
    (2, 2)         2    0.5 ms   0.3 ms      1.6x   2.9e-50
    (3, 2)         5    3.5 ms   0.4 ms      8.0x   1.2e-49
    (3, 2, 1)     16   71.3 ms   0.9 ms     82.7x   1.9e-50

The speedup grows with dim, which is the whole problem — the partition set
reaches dim 2310.

### Value equality, which this bean required before landing

    k_exact    python      rust   speedup   agreement
          4     0.01s     0.01s      0.9x   7.274e-50
          5     0.03s     0.02s      2.0x    1.13e-48
          6     0.43s     0.03s     16.4x   6.967e-49
          7     1.86s     0.05s     37.0x    4.71e-49

Same at (Z,N) = (1,1), (1,2), (2,1). Pinned in
`tests/test_unified_correction_rust_parity.py` (9 tests), which also asserts
that `use_rust=None` actually picks the fast path and that `use_rust=True`
with no kernel RAISES rather than silently falling back — a silent fallback
would turn a 40x regression into something only a stopwatch could find.

### The headline

    k_exact    rust
          8    0.13s
          9    0.57s
         10    4.49s
         11   44.95s      <- K_PARTITION_MAX, the full 193-partition set

    unified_iterative_correction(1, 1)  [deuterium, all defaults]:  43.96s

Before: did not finish in 150 s of profiling; this bean estimated ~40 days.

### The profile that motivated it

At the 150 s cap, A=2, pre-change:

    27,951,480 calls  mpmath __mul__   26.1s
    20,151,976 calls  mpf_mul          19.0s
    19,852,634 calls  mpmath __add__   18.1s
    13,020,726 calls  convert          11.3s
                      _msig_object_safe  46.7s cumtime / 423 calls
                      _build_ysn_matrices 22.4s cumtime / 193 calls

Not a precision cost to engineer around — a loop in the wrong language.

### Known inefficiency, deliberately accepted for now

The Rust kernel computes `Tr M^(0..step)` from the whole prefix each step
rather than updating a running matrix, so the prefix is re-multiplied every
step: O(A^2) crossing-applications where Python did O(A). That trades a factor
of A for a factor of ~dim, and dim reaches 2310 while A reaches 40 — but it
does mean the A-scaling is worse than the per-call speedup suggests.

`tr_m_atomic_mpfr_with_state` exists and looks like the fix, but it is a
DIFFERENT quantity — the Markov trace `tr_M` of a signed braid word, not the
per-partition character of a `(c, d, gen)` factor chain.

**RESOLVED — see the prefix-traces section below.** No state handle was needed.

### Items 4 and 5 still open

- [x] Item 4 — **SCRAPPED, the recommendation was wrong.** See below.
- [x] Item 5 — decided and landed: the tier is deleted. See below.


## 2026-09-03 (later) — the prefix recomputation is gone. New Rust kernel.

### A state registry was the wrong shape, and unnecessary

The obvious fix was a stateful χ holding the running matrix in Rust between
calls. That does not fit: at 50 dps a dim×dim MPFR matrix is ~213 MB at
dim 2310, and Σ_λ dim_λ² = 11! ≈ 4·10^7 Floats ≈ 1.6 GB across the partition
set. Holding state for every partition at once is not affordable.

It is also unnecessary. `chi_q_atomic_mpfr` computes the trace **per basis
vector** — it propagates `e_i` through the factor list and reads `buf[i]`,
never materialising a dim×dim product. Propagating `e_i` ALREADY passes
through every intermediate product, so recording `buf[i]` at each step
boundary costs one read and no extra memory.

Added `chi_q_atomic_prefix_traces_mpfr(shape, factors, segment_lengths,
q_str, dps) -> Vec<String>`: one propagation, one trace per segment.

    tools/hecke-engine/src/seminormal_mpfr.rs   kernel
    tools/pyhecke-native/src/lib.rs             #[pyfunction] + registration

Complexity goes from O(dim²·A³) to **O(dim²·A²)** — the same order as the
incremental matrix product, at MPFR precision and the Rust constant.

### Order note (why forward iteration is safe)

`chi_q_atomic_mpfr` applies factors in REVERSE and so forms `F_{n-1}···F_0`;
the new kernel applies them forward and forms `F_0···F_{n-1}`. They agree
because the Hoefsmit seminormal blocks are SYMMETRIC:

    Tr(F_0···F_m) = Tr((F_0···F_m)^T) = Tr(F_m···F_0)

That is also why the Python path (which builds `M = X_0 X_1 ··· X_m`
left-to-right) matched the Rust from the start despite the opposite
convention. Forward order is what makes the prefixes come out in caller order.

### The Python side is one call per partition for the WHOLE run

The per-step chains depend only on `ordering`, never on accumulated state, so
every crossing is known before the loop starts. `unified_iterative_correction`
now precomputes the entire trace trajectory per partition in a single kernel
call, then the existing step loop just reads `s['traces'][kk]`.

### Measured (clean, no competing job)

                  per-step Rust    prefix Rust    improvement
    A=2 (D)            49.64s         31.33s          1.58x
    A=3 (T)           100.47s         51.27s          1.96x
    ratio A=3/A=2       2.02x          1.64x

Values identical to the per-step path and to the pure-Python path
(-9.14773623102088067 at A=2; the 9 parity tests still pass).

Batching over partitions was measured and REJECTED:
`chi_q_atomic_all_partitions_mpfr` gave 0.9x-1.2x on 4 cores at k=8,9,10 —
one large-dim partition dominates, so the outer axis has nothing to give.
(The Rust docstring already says this and chooses a serial outer loop
deliberately; the measurement agrees with it.)

### Fallback preserved

`_rust_chi_prefix_traces` falls back to per-step `chi_q_atomic_mpfr` calls
when the installed wheel predates the new function — slower, same numbers.
Note the wheel is EPHEMERAL per `scripts/build-pyhecke-native.sh`: it installs
to user site-packages and dies with the container, so a fresh session must
re-run that script or it silently takes the slow fallback.


## 2026-09-03 — items 4 and 5 closed. Item 4 was wrong.

### Item 4: SCRAPPED. Deleting the numpy branch would have been a regression.

The item said to delete the `dim >= 8` numpy branch in `_matmul_dim`, citing
"31% SLOWER than the Python loop at dim 16 (0.0126s vs 0.0096s); object dtype
has no BLAS."

Re-measured on the input types the function actually receives — nested TUPLES
of mpf, not lists — min-of-runs:

    dim   mpf (object)         float64
      8   numpy 1.03x faster   numpy  4.20x faster
     12   numpy 1.03x faster   -
     16   numpy 1.03x faster   numpy  9.24x faster
     24   numpy 1.03x faster   -
     32   numpy 1.10x faster   numpy 22.43x faster
     64   numpy 1.02x slower   numpy 49.42x faster

The claim's REASONING is right — object dtype has no BLAS — but the
conclusion does not follow. On mpf it is a wash (±5%, no consistent sign),
not a 31% loss; I could not reproduce that figure in either input form.

And the item missed that `_matmul_dim` is also called with **float64**
matrices, by the q-sweep in `sdp_cross_channel.chi_at_q`. There the branch is
worth 4x-49x and growing with dim. Deleting it would have traded nothing on
the mpf path for a large regression on the f64 one.

Landed the corrected measurement as the function's docstring instead, since
the old one ("significant speedup for higher Hecke levels") is true only for
f64 and misleading for the mpf path this module mostly runs.

### Item 5: the tier is deleted, its derivation kept

The q-Gaussian block computed `log_trace_approx`, discarded it into a
diagnostic, and then added a **hardcoded** `delta_g = 0.0` — the zero was
never derived from the approximation it had just computed. So it could not
affect the answer under any input. And with `k_exact = k_max` (the default,
and the only value any caller passes — no external call site passes `k_exact`
at all; only this branch's own parity tests do) `active_gaussian` is empty and
it never ran. Dead twice over.

Deleted rather than repaired, on this corpus's own precedent (`qou-26f2`, the
self-comparing `tr_M` assertion): there was nothing to repair it TO. The
LP-complementary-slackness argument for why the contribution is zero is the
valuable part and is kept as a comment in place; `n_gaussian_partitions` still
reports how many partitions the cutoff skipped, which was the one honest
signal the block produced. `_q_gaussian_character_approx` went with it (61
lines removed in total).

Verified no consumer outside this module read `log_trace` / `method:
q_gaussian` across the .py and .json corpus (excluding the `qou-mass/`
vendored copy). Full suite 178 passed.
