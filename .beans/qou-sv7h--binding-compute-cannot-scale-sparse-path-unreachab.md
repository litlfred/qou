---
# qou-sv7h
title: 'Binding compute cannot scale: sparse path unreachable, zero Rust, float64 straddle'
status: in-progress
type: task
priority: high
created_at: 2026-08-30T15:41:58Z
updated_at: 2026-09-05T14:30:00Z
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


## 2026-09-03 — item 4's scrap rationale is VOID under NO FLOAT64 EVER

Owner restated the directive. My reason for keeping the `dim >= 8` numpy
branch was that it accelerates the FLOAT64 q-sweep in
`sdp_cross_channel.chi_at_q` by 4x-49x. Under the directive that sweep should
not have been f64 at all, and it no longer is — so there is no f64 caller left
to protect. "It accelerates a float64 path" is not an argument for anything
here.

The branch stays anyway, but on the measurement alone: every caller is now
mpf, and on mpf numpy is 1.03x-1.10x AHEAD, so deleting it is a small
regression for no gain. Object dtype means elementwise Python arithmetic on
mpf either way — no BLAS, no precision lost — so it is a speed question, not
a precision one. Docstring corrected to say that instead.


## 2026-09-03 (later) — one term of three was not enough

Routing `unified_iterative_correction` through Rust took deuterium's LP-dual
term from ~40 days (estimated) to 31 s, and I restarted the nuclide table on
that basis. **It ran 21 minutes without completing deuterium.**

`binding_energy` is three terms:

    unified_iterative_correction     <- routed to Rust, 31 s
    sdp_cross_channel_contribution
    binding_from_frobenius_pairing   <- still O(dim^3) mpmath

The third goes `binding_from_frobenius_pairing` -> `atom_markov_trace` ->
`atom_character_raw` once per partition, over the same YSN matrices. One
accelerated term out of three is no faster than the slowest term — an obvious
thing to have checked before starting a multi-hour run, and I did not.

`atom_character_raw` now takes the same route. It needs only the FINAL trace,
so a single `chi_q_atomic_mpfr` call replaces the whole accumulation; no
prefix-traces kernel required. `log_norm` comes back exactly 0 because the
`m_max > 1e80` rescaling exists to stop a float-range product overflowing and
MPFR does not have that problem — both callers multiply `chi * exp(log_norm)`
back together, so the product is unchanged.

Measured at 50 dps, ascending dim:

    partition                dim      python       rust   speedup        rel
    (4, 3, 3)                210   10907.0ms     47.9ms    227.9x   5.157e-50
    (3, 3, 1, 1, 1, 1, 1)    385   31870.1ms    100.3ms    317.7x   3.169e-50

The speedup grows with dim, as the complexity change predicts (O(dim^3) ->
O(dim^2 * |factors|)). The table's largest partitions are dim 2310.

Four new parity tests in `tests/test_unified_correction_rust_parity.py`,
covering both `include_inter` conventions, the `use_rust=None` default, and
the loud failure when the kernel is absent.

### The wheel really is ephemeral — confirmed the hard way

The container was reclaimed mid-measurement and
`chi_q_atomic_prefix_traces_mpfr` was gone on the next turn, exactly as the
earlier note warned. `scripts/build-pyhecke-native.sh` has to be re-run after
every reclaim or every Rust path silently takes the slow fallback. The
`use_rust=True` overloads raise rather than fall back for this reason; only
`use_rust=None` degrades quietly.


## 2026-09-03 — where the three YSN loop copies stand now

`binding_energy` = `unified_iterative_correction` + `sdp_cross_channel_contribution`
+ `binding_from_frobenius_pairing`. Traced all three:

- `unified_iterative_correction`  -> Rust (`chi_q_atomic_prefix_traces_mpfr`)
- `binding_from_frobenius_pairing` -> `atom_markov_trace` -> `atom_character_raw`
  -> Rust (`chi_q_atomic_mpfr`)
- `sdp_cross_channel_contribution` -> builds an active set and solves an
  SDP (`sol['cross_blocks']`). It does NOT go through a YSN matrix product at
  all, so there is nothing to route; it was never the bottleneck.

So both heavy terms are Rust-routed, which matches the observed per-atom
times.

### The one remaining copy — and it is unreachable

`_contrib_single_partition` is still the O(dim^3) mpmath loop with
`_msig_object_safe`. Its only callers are `conjugate_pair_cross_term` and
`unified_iterative_correction_jet`, and **neither has a caller outside
`hecke_core_legacy` itself** (checked across `computations/` and `tools/`).
So it is on no live producer path and is not blocking anything.

Left un-routed deliberately, but recorded rather than forgotten: this bean and
`qou-9ay6` have both now been bitten by divergence between copies of this loop
(three `.dot` sites, then three wrong `a_rho` sites). A fourth copy drifting
out of sync is the standing failure mode here, so if `_contrib_single_partition`
ever acquires a live caller it should be routed at the same time, not after.

Not editable right now in any case: the nuclide-table regeneration's resume
key hashes `hecke_core_legacy.py`, so touching it would discard the run.


## Summary of Changes

Closed. All five items resolved; two of them by contradicting the bean.

1. **Sparse guard** — already fixed in the tree (`if s['sparse']:`).
2 & 3. **The fix was not to export a matmul, but to CALL Rust that was already
   exported.** This bean proposed exporting `dense_dense_mul_mpfr` (">=24x").
   `pyhecke_native` already exported `chi_q_atomic_mpfr`, which computes the
   ENTIRE per-partition product, taking `(c,d,gen)` decimal STRINGS so
   NO-FLOAT64 holds by ABI rather than by care. Routed
   `unified_iterative_correction` and later `atom_character_raw` (the latter
   because one accelerated term of three is no faster than the slowest term —
   the table ran 21 minutes without finishing deuterium until it was done).
   Added `chi_q_atomic_prefix_traces_mpfr` (new Rust kernel) to get every
   step's trace from one propagation, O(dim^2*A^2) rather than O(dim^2*A^3);
   a state registry was measured as unaffordable (~1.6 GB) and proved
   unnecessary, since the per-basis-vector formulation already passes through
   every intermediate product.

       deuterium   ~40 days (this bean's estimate)  ->  118 s
       atom_character_raw at dim 660                ->  301x
       value equality verified at 4 k_exact levels, 3 nuclides, ~1e-48

4. **SCRAPPED — the recommendation was wrong.** Deleting the `dim >= 8` numpy
   branch would have been a regression: re-measured on the real input types it
   is a wash on mpf (±5%, not the claimed 31% loss), and the item missed that
   `_matmul_dim` was also called with float64 by the q-sweep. Under NO FLOAT64
   EVER that f64 path was then excised anyway, so the branch now stays purely
   on the mpf measurement.
5. **Done** — the q-Gaussian tier is deleted. It added a hardcoded `0.0` never
   derived from the approximation it computed, and was empty by default.

Also mapped all three `binding_energy` terms and confirmed the one remaining
un-routed copy of the loop (`_contrib_single_partition`) is reachable from no
live producer.

Follow-up not blocking this bean: if `_contrib_single_partition` ever gains a
live caller it should be routed at that moment — divergence between copies of
this loop has now caused two separate defects (three `.dot` sites, then three
wrong `a_rho` sites).

---

## MERGE NOTE 2026-09-05 — two scopes, two records, both kept

This bean was `completed` on `claude/anchor-followups-2026-08-08`
for the COMPUTE-SCALING scope (the sparse path, the Rust kernel
routing, deuterium ~40 days -> 118 s). Meanwhile a sibling on
`claude/rag-document-ingestion-options-orasrw` read it as `todo`
and claimed the SIGN question, which is a different sub-question
and genuinely open.

Status resolved to **in-progress**, theirs, not mine. My scope's
completion is recorded in the section above; their claim follows.
A sibling's active claim is not something this branch gets to
close, and the conservative status is the one that does not
silently retire work someone is doing.

---

## CLAIMED 2026-09-05 — branch claude/rag-document-ingestion-options-orasrw

Taking the SIGN question specifically, on owner direction. The prior session
(`session_01Cb9sX3NisBDY4WN4z5wJL4`) last committed 2026-09-03; this bean is
still `todo`, so this is a claim on an unclaimed item rather than a takeover.

**Scope I am taking:** why `unified_iterative_correction` is negative. Its own
commit `815b2a46a0` says "nothing here says WHY the sign is wrong -- that is the
physics question this measurement opens and does not answer."

**Scope I am NOT taking**, so it stays available: 6Li / A>=6, which
`aaa2ef9c51` names as the discriminating measurement for the extensive term's
SHAPE. That is a different question from the sign and ~5x deuterium's cost.

**Route:** formalize-first, per AGENTS.md STRICT — locate where the sign is
DETERMINED in term 1 and ask whether it is forced, rather than scanning. The
strongest existing evidence that it is structural is this bean's own: the
accumulator is negative on BOTH matrix families (old braid-violating: -0.0319
at k=4 to -2.1955 at k=8; corrected: -0.0896 to -2.0200), so it survives a
change of the underlying representation.

**Falsifier stated in advance:** if the sign traces to a free choice — an
orientation, a w_0 convention, an ordering of the LP objective — then it is not
structural and this framing is wrong.

## Step 2 answered 2026-09-05 (qou-0wqd / PR #6708) — nothing moves; step 3 is what is left

Step 2 was "wire the correct family in, then re-run the binding numbers and
report what moved". Measured: `1e-14`, not the 71-221 % the step-2 first-half
table predicted. The correct family is now in
`hecke_core_legacy._build_ysn_matrices` (`a_rho = h/(1 - q^(-2 rho))`, braid
defect `0.7315 -> 7.5e-17`, `ysn_braid_relation_audit.py` exit 0).

Two independent reasons the accumulator could not move:

1. **The kernel bypasses the Python family entirely.**
   `_lp_kernel_steps(partition, chains)` takes the partition SHAPE, not
   `entry['ysn']`, so Rust rebuilds its own braid-satisfying family; both
   consumers early-return on it. 193 calls, 193 served.
2. **The consumers take traces, and the trace cannot see the defect.**
   `Tr(ABA) - Tr(BAB) = Tr(B) - Tr(A) = 0` from the quadratic relation alone, in
   any dimension. Established at MPFR in
   `computations/audits/ysn_trace_blindness_probe.py` (9/9): legacy MATRIX braid
   defect `0.731514`, legacy TRACE braid defect `6.68e-52`.

**Step 3 (performance / precision) is now the live item**, and it is joined by a
consumer this arc has not assessed: `q_sweep_sdp_atom` in
`sdp_cross_channel.py` imports `_build_ysn_matrices` directly and uses the
matrices, not their traces — so it is the one place where the defect could have
had a numerical consequence, and nobody has measured it.


## The `q_sweep_sdp_atom` gap is closed — it has no callers (2026-09-05)

Measured, correcting my own note above: `q_sweep_sdp_atom` is defined at
`computations/sdp_cross_channel.py:394` and **called nowhere in the repo**. A
tree-wide grep returns its own `def` plus only the three places this session
wrote *about* it (this bean, `qou-0wqd`, and the audit doc). No witness
references it.

It was named as "the one place the defect could still bite" because it is the
only importer of `_build_ysn_matrices` outside `hecke_core_legacy` and it uses
the **matrices** rather than their traces. That reasoning was right; the
premise was not — there is no caller, so no recorded number came from it, and
the fix makes it correct before anyone writes one.

This is a grep, not a run: it establishes there is no consumer, not that the
function is otherwise correct.

**So the arc's remaining item is step 3 alone** — the builder is still float64
(`math.sqrt`, `1.0` literals, no `mp.dps`), which is why the Python family
agrees with the Rust MPFR reference only to ~1e-16.


### Cross-reference for the sign claim (from `qou-0wqd` / PR #6708, 2026-09-05)

The claim section above rests its "the sign survives a change of the underlying
representation" argument on the accumulator values *"old braid-violating:
-0.0319 at k=4 to -2.1955 at k=8; corrected: -0.0896 to -2.0200"*. Those are the
2026-08-31 audit's step-2 table, which PR #6708 **retires**: its *corrected*
column is what today's `main` already produces WITH the braid-violating
matrices, and its *current* column reproduces on no tree measured there.

**The conclusion is strengthened, not weakened.** Varying only the matrix family
moves the accumulator by `1e-14`, and for a proved reason — the consumers take
traces, and `Tr(ABA) - Tr(BAB) = Tr(B) - Tr(A) = 0` follows from the quadratic
relation alone in any dimension. So the sign is invariant under that change by a
structural argument rather than by two numerical runs that happened to agree in
sign. Quote the invariance, not the table.

**And it narrows the falsifier usefully:** since the representation cannot move
the accumulator at all, the sign cannot be traced to anything in the seminormal
family — the free-choice candidates worth checking are the ones OUTSIDE it (the
LP objective's ordering, an orientation, a `w_0` convention).


## The sign IS answered — the Pass-2 gate forces it (2026-09-05, PR #6752)

The falsifier stated in advance above asked whether the sign traces to a free
choice. **It traces to the gate**, which is neither a free convention nor part
of the seminormal family — so the narrowing in the cross-reference section
above ("look OUTSIDE the family") pointed the right way.

`unified_iterative_correction` returns `B = sum over GATED lambda of
C_lambda * ( ln|Tr M_lambda(A)| - ln d_lambda )`. Three measured steps:

1. `C_lambda >= 0` everywhere — **0 of 682** negative.
2. Pass 2 keeps exactly the partitions with final trace `<= 0` (complementary
   slackness).
3. `|Tr| >= d` holds in **34.1 %** of `Tr > 0` cases and **3.4 %** of
   `Tr <= 0` cases — a 10x asymmetry, structural because `Tr(I) = +d`.

Non-negative scale times a negative log ⇒ `B < 0` forced, for any nucleus.
**Same cause explains the A-independence**: gated-set size across A = 2..6 is
`[15, 9, 9, 10, 15]` while AME spans 12.7x — the output is a property of the
gate's selection, not of the nucleus.

Probe: `computations/probes/uic_sign_forced_by_gate_probe.py` (5/5).

## The gate's justification is disproved — by a proof already in the corpus

`content/quantum-observable-universe/mass-theory/operator-selection-lp.md`
(commit `6b7d2ec4a8`) proves the operator-selection LP degenerate: `b_1 = 1`
makes the first Frobenius row equal the objective vector, so the optimum is
identically 0, `y_0* = 0` by strong duality, and the minimiser set is a
positive-dimensional face. That commit fixed the content blocks and never
touched `hecke_core_legacy.py`.

- `lp_shadow_price` sets `y_0 = 1/[k]_q!` and calls it "the dual variable of
  the normalisation constraint". Measured 0.497 (k=2) to 1.56e-4 (k=7) —
  never 0. What it actually does is zero the two extremes `(k)` and `(1^k)`.
- Substituting the **proved** `y_0* = 0` makes the sign MORE negative
  (2H -1.3657 -> -1.6092; 6Li -1.0770 -> -1.6065). So correcting the dual is
  necessary and **not sufficient** — the gate is the mechanism.

Probe: `computations/probes/uic_gate_justification_disproved_probe.py` (5/5).

## Replacement objective — written up, two falsifiers run, decision is the owner's

`docs/proposals/2026-09-05-operator-selection-objective-replacement.md`.

New measurement: **an index-set mismatch**. The primal LP is NF-basis-indexed
(`d = n! = 720` at n=6) while `prop:mass-coefficient-shadow-price` claims a
**partition's** shadow price — 11 partitions of 6, not 720. No partition-indexed
LP exists in the corpus. The natural bridge makes the object a `d_lambda x
d_lambda` matrix, not the scalar the code multiplies; and the `d_lambda = 1`
blocks, where the scalar type IS correct, are exactly the two `y_0 = 1/[k]_q!`
zeroes out. Probe: `lp_partition_index_mismatch_probe.py` (4/4).

Five options O1-O5 with cost / risk / what-each-forecloses; **which one to take
is the owner's decision**, the same one `6b7d2ec4a8` declined, one level down.

- **O3 falsifier FIRES** (`sdp_o3_falsifier_probe.py`, 6/6). The block SDP does
  exclude all six LP-optimal vertices (min eig -7.33 / -3.85) but is degenerate
  by a different route: SU(2) gives `y_(1,1,1) = 0` exactly, so a Phi on that
  block is PSD with objective 0 and nonzero net (0.02016). The ray matches the
  known q-antisymmetriser radical to **6.4e-51** — not a new object. Amended to
  **O3' — pose the SDP on `H_n(q)/radical`**.
- **O3' falsifier does NOT fire** (`sdp_o3prime_weight_positivity_probe.py`,
  5/5). n = 3..12 at the proton pin: >2-row partitions vanish exactly, every
  survivor strictly positive, `sum y_lambda f^lambda = 1` throughout; still
  positive at `k_max = 11` (9.2e-4). Cross-validated at n=3 to 14 digits
  against the weights the O3 probe solved independently.

**Do not start O3' expecting it to fix the sign.** It fixes the type error;
the feasible geometry still does not distinguish `B_3`, so selection stays open.

## Still open on this bean

- Step 3 (the float64 builder) — untouched by this session.
- 6Li / A>=6 for the extensive term's SHAPE (`qou-brng`) — a run is in flight
  but that is a different question from the sign.

## Owner ruling 2026-09-05 — O2 + O3′ chosen; O2 done, O3′ formalized

Author picked **1 and 2**: fix the documentation, and re-pose as the block SDP
on the radical quotient.

**O2 applied, six sites, no number moved.** The false claim was that
`y_0 = 1/[k]_q!` is "the dual variable of the normalisation constraint". It is
`min_λ(w_λ/d_λ)`, a weight normalisation; and the real net-constraint dual of
`prop:operator-selection-lp` is identically zero. Corrected in
`mass-coefficient-shadow-price.{md,ts}`, `knot-operator-energy.md`,
`unified-iterative-correction.lean` (docstring only), and three sites in
`hecke_core_legacy.py` — one of which additionally claimed the LP assigns
"unique invariants" to the partition basis, false twice over (NF-indexed, and a
positive-dimensional minimiser face). Content validate exit 0; `lean`-direct
exit 0. `shell-closure-stability.md` makes the same shape of claim about the
**confinement** LP and was left alone: different program, and settling it is a
measurement rather than a doc fix.

**O3′ begun formalize-first** — `QOU/MassTheory/BlockSDPNondegeneracy.lean`,
5 declarations, `lean`-direct exit 0, `#print axioms` clean on all five (no
`sorryAx`). `obj_pos_of_pos_weights`: on the quotient every feasible point has
strictly positive objective, so no degenerate ray.
`exists_zero_obj_of_zero_weight`: one vanishing weight restores the degeneracy
at any target — the falsifier as a theorem. `feasible_smul`: the value is
homogeneous of degree one in `n_target`, the property the LP lacks. **Not
proved: that O3′ selects.** The compute half of O3′ is not started.

## 🛑 My A-independence claim is UNVERIFIED, and ⁶Li is anti-correlated

`binding_energy(3,3)` with `_HAS_LP_KERNEL` asserted, 4039.8 s:
**B_pred = −3.065019520558719** against AME **+31.994**.

Against the only other production figure I measured myself (²H, kernel live,
−7.271102124876717): predicted `|B|` **falls ×0.42** while AME binding **rises
×14.4**. Per nucleon, predicted `|B|/A` falls ×7.1 against AME's ×4.8 rise. The
prediction is **anti-correlated** with its target, not merely sign-flipped. The
sign is negative at A = 6 too, consistent with the gate.

**The four-point plateau I quoted in PR #6752 (−7.271 / −7.742 / −7.456 /
−6.829) has provenance for ONE of its four figures.** A fixed-string grep for
the other three across `*.md`, `*.json`, `*.py` returns nothing anywhere in the
tree; they came from conversation context. Kernel-vs-fallback differ by 17.29 %
on the same atom, so an unverified figure could be either. Marked unverified,
not retracted. If the plateau is real, ⁶Li breaks it (2.4× smaller than the
smallest of the four) — deciding that needs A = 3,4,5 re-measured kernel-live,
~2 h, claimed separately.

Second tension, open: the k_max = 6 reconstruction does **not** show the A = 6
drop (⁶Li is second *largest* there at −1.0770), and the gated-set size at
A = 6 is **15**, the largest in the series. Production magnitude falls where the
gate admits the most partitions. The truncation argument covers absolute scale,
not a reversed trend.

Audit: `docs/audits/2026-09-05-li6-production-binding-anticorrelates.md`.
## Step 3 done — and the builder was float64 in three places, not one (2026-09-05, PR #6794)

I had recorded the remaining defect as "the builder is still float64
(`math.sqrt`, `1.0` literals, no `mp.dps`)" and framed leaving it as a
deliberate ordering choice. Both were wrong: NO-FLOAT64 makes it a defect, not
a deferred nicety, and the description named only the smallest of three.

| defect | evidence |
|---|---|
| `Q`/`Q_INV`/`HA` from `q_parameter` are Python **floats** — float64 from the INPUTS | `type(qp.Q).__name__ == 'float'` |
| `mp.dps` is **15** on a bare import — float64's significand, so mpf without raising it buys nothing | `mp.dps == 15` after import |
| **124 of 193** ysn entries (64 %, max dim 2310) were `scipy` `csr_matrix` — float64 by construction, kernels reject `dtype=object` | measured over `_PARTITION_TABLE` |

Fixed: exact twins `Q_MP`/`Q_INV_MP`/`HA_MP`, `mp.sqrt`, and
`mp.workdps(_precision.COMPUTE_DPS)` (70, read not hardcoded, restores the
caller's dps on exit). `_ExactCOO` replaces `csr_matrix` — deliberately not a
scipy type so `issparse` is False for it and no consumer can route it into
float64 BLAS.

The consumer dispatch moved with it: all three accumulators keyed on the
RUNNING matrix's dtype, which starts as `np.eye` (float64), so an exact sigma
would have sent the first crossing into a scipy call that raises. They key on
sigma now, and the COO accumulator is `dtype=object` rather than
`zeros_like(M_run)`.

**Verified.** Against the closed form derived in `qou-4m9u`
(`-1/(q(q^2+1))` at rho = -2): **9.5e-52**, was ~1e-16. Braid audit exit 0
with the Python rows at `4.0e-50 / 3.2e-50` against Rust's `1.2e-50 / 2.0e-50`
— previously `1.49e-16 / 1.52e-16`.

**A hypothesis of mine, REFUTED.** I proposed that main's "17.3 % off at
deuterium" banner was the sparse path, since the 1e-14 merged in #6708 came
from k = 4,5,6 which carry zero sparse partitions. Measured at k = 7 (2 sparse)
and k = 8 (12 sparse): rel **1.7e-14** and **8.9e-15** — same order. The
float64 defect does NOT account for 17.3 %.

**Still open, and not mine to close without measuring:** that banner's *braid*
claim is stale (#6708 fixed it; the audit exits 0), so it tells a user their
numbers are invalid when they are not. The 17.3 % half compares fallback
against kernel — a different comparison from the one above, unrun here.

## A-series COMPLETE (2026-09-05) — the plateau does not exist, and that was my claim

Owner asked for A = 3,4,5 kernel-live. Probe
`computations/probes/uic_binding_a_series_kernel_live_probe.py`, 5/5, 11350 s.

**All three unverified figures reproduce exactly** — ³H `−7.742121347136118`
(vs −7.742), ³He `−7.45619950551758` (vs −7.456), ⁴He `−6.828594293148849`
(vs −6.829). The series was kernel-live; my caution was procedurally right and
the substance was sound.

**And it identifies the set:** ²H, ³H, ³He, ⁴He — **A = 2, 3, 3, 4**, the same
five atoms as `[15, 9, 9, 10, 15]` minus ⁶Li. I labelled both "A = 2..5" and
both were wrong identically, because they are one set. **No A = 5 point had
ever been computed.**

| atom | A | Z | N | B_pred | AME |
|---|---|---|---|---|---|
| ²H | 2 | 1 | 1 | −7.2711 | 2.2246 |
| ³H | 3 | 1 | 2 | −7.7421 | 8.4818 |
| ³He | 3 | 2 | 1 | −7.4562 | 7.7180 |
| ⁴He | 4 | 2 | 2 | −6.8286 | 28.2957 |
| ⁵He | 5 | 2 | 3 | −6.7896 | 27.5607 |
| ⁵Li | 5 | 3 | 2 | **−8.1363** | 26.3307 |
| ⁶Li | 6 | 3 | 3 | −3.0650 | 31.9940 |

**I committed a two-branch prediction before ⁵Li landed and BOTH failed.**
⁵He and ⁵Li share A = 5 and differ only in Z, so: ⁵Li ≈ −6.8 ⇒ break at A = 6;
⁵Li ≈ −3 ⇒ break at Z = 3. It is **−8.136**, below the whole plateau.

**So the "A = 2..5 plateau with a cliff at A = 6" does not exist** — an artefact
of a sample holding one atom per mass number above A = 3. What survives:

- the **same-A mirror split grows ~5×** (³H/³He 3.835 %, ⁵He/⁵Li 19.84 %) — same
  A, differing only in Z, and the gate account predicts nothing about it;
- the **largest single jump is same-Z, adjacent-A**: ⁵Li → ⁶Li = 2.655×;
- predicted spread 2.655× against AME's 14.4×, every point the wrong sign.

**Scoped:** the probe's anti-correlation assertion compares only the extreme A
points and the series is not monotone (⁵Li sits below ²H) — true of two
endpoints, weaker than its passing suggests.

**Post-merge check:** ²H re-run after the sibling's #6794 exact-`mpf` fix is
**bit-identical** (`−7.271102124876717`, MOVED: False), so the series stands.
Mechanism: with the kernel live the Python sigma family is never consumed.

**Still open:** ⁶Li is the most extreme point and the one row not measured by
this probe (carried from a standalone run). It wants an independent re-run
before anything is built on it.

## ⁶Li independently confirmed; O3′ appears to SELECT (2026-09-05, later)

**⁶Li re-run is bit-identical** — `−3.065019520558719`, MOVED: False, 4024.9 s
against the recorded 4039.8 s run. The extreme outlier is real, and every row of
the A-series is now measured or independently confirmed. It doubles as a much
harder post-merge check than ²H (A = 6 exercises far more of the partition
table), so **#6794 does not move `binding_energy` on the kernel path**,
confirmed at both ends of the mass range.

**🛑 O3′ appears to SELECT — correcting my own §8 recommendation.** I told the
owner O3′ would fix the type error and leave selection open. Under the natural
lift `T_λ = t_λ·I`, the block SDP reduces to a scalar LP in the traces whose
optimum sits on `argmin_λ t_λ`. Measured over all six rows of
`a-K-via-lp-dual-full.witness.json`, survivors only: the argmin is **unique in
every row**, smallest gap 19.9 %, largest 110.8 %. Selected blocks (2,1), (2,1),
(3,3), (5,4), (5,4), (6,6) — the near-square two-row partition each time.

Precisely: the **block** is selected, the **operator** is not (any PSD `Φ_λ`
with the right trace is optimal). That is exactly the content the corpus's
physical reading wants — "which Wedderburn blocks the bound state saturates" —
and it does **not** contradict S4, which excludes selecting the *operator* `𝓑₃`
on the NF-indexed polyhedron.

Caveats kept explicit: the **reduction** was measured, not a solver run; the
lift `T = t·I` is an assumption; and `t_λ > 0` on survivors is measured over six
rows, not derived (recorded in `BlockSDPNondegeneracy.lean`'s docstring, since
that is the theorem's hypothesis and characters can in principle go negative).

**This raises the value of the O3′ compute**: authorised as a type fix, it may
also be a selection principle.
