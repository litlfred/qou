---
# qou-mtx9
title: the chi bottleneck is the Geck-Pfeiffer reduction, it scales with WORD LENGTH, and a batched entry point already exists unused in 9 producers
status: todo
type: task
priority: normal
created_at: 2026-08-26T07:11:37Z
updated_at: 2026-08-26T07:45:16Z
---

## Where the time actually goes

Not Python, not mpmath. The wrapper `chi_rust_at_q_mpf` calls Rust for an
exact integer Laurent and sums ~1-40 terms with binary exponentiation —
microseconds. All the cost is inside `chi_q_via_gp`, in the
**Geck-Pfeiffer reduction**: the search for minimal-length class
representatives via cyclic-shift completion.

**The driver is WORD LENGTH, not n.** Measured:

    n=6  |word|=5    0.00s      n=8  |word|=7     0.00s
    n=6  |word|=10   0.00s      n=8  |word|=14    >15 min, did not finish

Doubling the word at fixed n crossed from instant to intractable.
`block_swap_binding` runs 8 words of ~47 letters at n=12, and called the
per-shape entry point 77 times per word.

Caveat: that probe word is every generator in ascending order, repeated,
which is plausibly adversarial for a minimal-length search. The cliff is
real; its position on production words is not measured.

## The fix already exists in the bindings

`chi_lambdas_via_gp(shapes, n, word)` is registered in
`tools/pyhecke-native/src/lib.rs` and does **one** GP reduction for all
shapes. Its own docstring states the case:

> The GP reduction is the expensive part (depends only on `(n, word)`,
> not on `λ`); sharing it across the partition loop gives ~O(p(n))x
> speedup vs calling `chi_q_via_gp` per partition.

At n = 12 that is up to **77x**. Measured adoption: **6 producers use the
batched call; 22 use the per-shape one, 12 of them inside a partition
loop** — repeating an identical reduction once per shape for a result
that provably does not depend on the shape.

Composes with the two-row cap (`qou-e9le`): pass 7 shapes, not 77, to a
single reduction.

## The stale warning that keeps producers on the slow path

`computations/deltalambda/he4_binding_k_stage2_probe.py` carries:

> ⚠ GP KERNEL BUG ... `chi_lambdas_via_gp` returns WRONG characters on
> some plain braid words ... All GP-based results must be validated per
> word-class against the seminormal engine **until the Rust bug is
> fixed** (bean filed).

**The bug is fixed and that bean is completed** (`qou-b2ie`). Verified
directly against the warning's own minimal reproducer,
`[(1,6),(1,7),(-1,9),(1,8),(-1,7)]` at H12, with pyhecke_native 0.9.0:

    chi_[12](repro) = 1.1099785827513808076
    q^writhe        = 1.1099785827513808076    (writhe = 1)
    match to 40+ digits, in 0.000s

The historic wrong value was 0.7926. `qou-b2ie` also landed a **guard**:
the GP path now panics on trivial-rep disagreement rather than returning
silently-wrong, and `chi_gp_trivial_rep_consistent` is exported as a free
pre-check. So batching cannot quietly produce bad characters.

That warning should be dated and retired — it is a live instruction to
avoid the fast path for a reason that no longer holds.

## Scope of the conversion — 9 producers, not 12

Three of the twelve loop-callers must be left alone: the per-shape call
is the *subject* of the measurement, and converting them would destroy
what they measure.

    LEAVE   derived_chi_catalogue_matrix_m_multi_a_benchmark   BENCHMARK
    LEAVE   derived_chi_catalogue_rust_gp_crosscheck           CROSSCHECK
    LEAVE   derived_chi_catalogue_production_wire_demo         DEMO

    CONVERT block_swap_binding                  (done, this bean)
            chi_4he_via_rust_lossless
            chi_via_rust_lossless
            chi_at_q0_via_matrix_m_mpfr
            derived_chi_catalogue_matrix_m_mpfr
            derived_chi_catalogue_matrix_m
            derived_chi_catalogue_matrix_m_numerical
            derived_chi_catalogue_bridge_factor_deuteron
            derived_chi_catalogue_consumer_q0

Six of the nine have committed witnesses, so each conversion needs its
witness diffed against the committed baseline, not just an exit-0.


## CORRECTION — "scales with WORD LENGTH, not n" is too simple, and lever 3 is dead

Two measurements landed after that claim, and they pull in opposite
directions. Both are real; the one-line summary was not.

### Length matters steeply — WITHIN a family

Measured on this producer's own words at n = 12, batched + two-row pruned:

    id       |word| = 47      ~60 s for the row (two tr_M calls)
    swap_p   |word| = 56      > 470 s and still running

**Nine more letters cost roughly 8x.** So within a family of structurally
similar words the growth is steep, and the `swap_pn` word (65 letters)
should be worse again.

### But structure dominates ACROSS families

My benchmark's probe word — every generator 1..n-1 in ascending order,
repeated twice — did **not finish in 15 minutes at n = 8 with 14
letters**. This producer's 47-letter word at n = 12 completes in ~30 s
per call. A production word **3x longer at higher n is >30x faster.**

So the probe word is pathological, more severely than the caveat I
attached to it allowed. The GP reduction's cost is a function of how far
the word sits from a minimal-length class representative — which
correlates with length inside a family and not at all across families.
Do not quote the n=8/14-letter figure as a length scaling law; it is a
worst case for the search, not a point on a curve.

### Lever 3 (word shortening by free reduction) is DEAD

Measured — every word is already freely reduced, zero headroom:

    id       atom  47 -> 47      free  44 -> 44
    swap_p   atom  56 -> 56      free  53 -> 53
    swap_n   atom  56 -> 56      free  53 -> 53
    swap_pn  atom  65 -> 65      free  62 -> 62

No adjacent `sigma_i sigma_i^-1` pairs anywhere, including at the
junction where `w_atom + beta` is concatenated. Free reduction cannot
shorten these words at all, so the third optimisation I proposed does not
exist. Anything that shortens them has to use braid relations, not free
cancellation — a real search, not a scan.

### What this means for the batching result

Batching removes the **x77** on reduction COUNT. It does nothing about
the per-reduction cost, which is the steep term. So the honest projection
for this producer is that it may still exceed its budget on the longest
row — and if it does, that is the finding: the partition loop was never
the dominant cost, one GP reduction on a 65-letter word is.


## RESOLVED — and the fix is NOT batching. It is the wrong engine.

`block_swap_binding`, measured end to end:

    TIMEOUT at 25 s, 180 s (twice), 900 s      original (77 per-shape GP calls)
    TIMEOUT at 1800 s                          batched GP + two-row prune
    5 SECONDS, exit 0, assertion passes        SEMINORMAL + two-row prune

So the recommendation in the first half of this bean was wrong. Batching
removes the x77 on how many minimal-length searches you run; it cannot
help the search itself, and the search is the whole cost. Measured with
the SAME seven shapes and the same batched call shape:

    |word|      GP                     seminormal
      47        0.12 s                   1.26 s
      56        > 90 s (unfinished)      1.56 s
      65        —                        2.12 s

GP wins on short words and then falls off a cliff. The seminormal route
is ~linear and has none. This producer's words are 47-65 letters, so all
but the shortest sit past the cliff — it was timing out while doing
nothing wrong.

**Correctness, checked before switching.** The two engines are
independent implementations. On this producer's own words they agree to
the 50-dps floor: `W_atom` rel **2.6e-50**, `W_free` rel **5.4e-50**.

**The two-row prune is exact, verified numerically as well as in Lean.**
7 shapes vs all 77 through the identical call, same word:

    tr_M   7 two-row shapes : 2.89958832139990569
    tr_M  all 77 shapes     : 2.89958832139990569
    difference              : 0.0   (exactly)

Largest >2-row contribution `|y*chi|` = 9.7e-72. The Lean said zero; the
arithmetic agrees.

**Note the two levers are separable and BOTH are needed.** Seminormal
alone is not the answer: `chi_lambda_all_partitions_mpfr` — the
all-77-shapes seminormal entry point — ran for **over 15 minutes without
finishing** on the same word, because n = 12 includes blocks of dimension
2310. It is seminormal RESTRICTED to the two-row shapes that is fast.
Any conversion of the other producers must carry both halves.

## What this makes newly measurable — a 45th stale witness

`block-swap-binding.witness.json` (committed 2026-06-22) could never be
checked, because the producer could not run. At 5 s it can. Every
substantive field moved:

    atom_traces/id        0.885616920  ->  2.899589970    3.3x
    atom_traces/swap_pn   0.189970763  ->  3.267857280     17x
    free_traces/swap_pn   0.353734913  ->  5.529478284   15.6x
    S_atom                0.535257897  ->  1.062554528
    S_free                0.374220678  ->  0.690782618
    binding_signal        -0.357903009 ->  -0.430606035    20%

`binding_signal_log_Sfree_over_Satom` is this producer's headline result
and it moves 20 %. The drift is upstream, not from the engine swap —
established by the two checks above (engines agree to 1e-50; prune is
exact to 0.0).

**The refreshed witness is deliberately NOT committed.** A re-run
establishes non-reproduction, not correctness, and a 20 % move on a
producer's headline scientific number is not something to land silently
at the end of a session. Someone should decide which value is right.

## Revised recommendation for the remaining producers

Do NOT batch-convert the other eight to GP. The triage question per
producer is **word length**, not shape count:

  * words comfortably under the cliff -> GP is fine and faster
  * words at or past it -> seminormal, restricted to the two-row shapes

The cliff sits somewhere between 47 and 56 letters at n = 12 on this
word family, and its position is a property of the word's distance from
a minimal-length representative, not of length alone (see the correction
above). Measure per producer; do not inherit this boundary.
