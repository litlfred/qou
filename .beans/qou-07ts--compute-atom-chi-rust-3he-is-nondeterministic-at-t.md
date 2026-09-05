---
# qou-07ts
title: 'compute_atom_chi_rust 3He is nondeterministic at the 50th digit: 4 distinct outputs in 8 runs'
status: todo
type: task
priority: normal
created_at: 2026-09-05T08:33:29Z
updated_at: 2026-09-05T08:34:06Z
---

Found 2026-09-05 while doing attribution for `qou-t0wm` on PR #6772 — running
a producer unmodified first, to separate its own drift from my change.

## The measurement

`computations/compute_atom_chi_rust.py 3He`, eight consecutive runs, same
container, same commit, nothing else running. Fingerprint is sha256 over all
60 `chi_lambda` strings in `data`:

    run 1  0e723a390d08d66b
    run 2  df749d8a9420cf5f
    run 3  9a05864ca978a5d0   <- the committed value
    run 4  e2254b24be9b03af
    run 5  9a05864ca978a5d0
    run 6  e2254b24be9b03af
    run 7  9a05864ca978a5d0
    run 8  9a05864ca978a5d0

**Four distinct outputs in eight runs.** Not a two-state flip. The committed
value is the modal one (4/8), which is presumably why this has survived.

The differences are one unit in the last place of the 50-dps strings, e.g.
`-5.3650940574330408741460866992442460653231992028901` →
`…8900`. Two independent instances were seen before this sweep, hours apart.

**`D` and `T` are stable** across the same runs — 0 chi_lambda diff lines
every time. So it is not simply "MPFR is loose"; it is specific, and 3He is
not even the largest case (T has the same `n_partitions` = 30).

## Why it matters, and what it does NOT threaten

It does **not** threaten L1 (1 ppQ = 1e-15) or any physics claim. A wobble at
the 50th significant digit is 35 orders below the precision target.

What it damages is **attribution**, which is exactly the discipline AGENTS.md
asks every agent to run before claiming a witness moved:

> the producer was run unmodified first and reproduced byte-identically

That sentence is unavailable for this producer, and an agent who runs it once
before and once after their change will see a spurious diff and may attribute
it to themselves. **I nearly did**, twice: the first instance looked like it
had to be mine (an unmodified control did not reproduce it), and only a
repeated-run test showed otherwise.

Note also that this is the **canonical** tier. The producer's own description
contrasts it with `--f64`: *"MPFR (default) … at 50 dps (canonical tier);
`--f64` is the preview tier only (owner ruling 2026-06-09: no f64 on the
canonical path)"*.

## The corpus already has a checker, and it does not reach here

`computations/witness-reproducibility-check.witness.json` does precisely this
test — snapshot, re-run, compare — and its word for the failure is **drift**.
It currently reports `{"pass": 5, "drift": 4, "skip": 2}`.

But its scope is **11 scripts**: ten `build_*_chain.py` plus one audit. It does
not cover `compute_atom_chi_rust.py`, or any producer outside that set. So the
class is known and this instance is not — the gap is coverage, roughly 11 of
~3000 producers.

Distinct from `qou-coyy`, which is about that same checker reporting
`allPassed: true` over its own four recorded drift failures. That is a
reporting defect; this is a coverage gap plus a new instance.

## What would close this

1. **Find the source.** Likely candidates, none tested: thread scheduling or a
   parallel reduction order inside
   `pyhecke_native.chi_lambda_all_partitions_mpfr`; an accumulation order that
   depends on hash iteration; an uninitialised-precision path. Determining
   which needs someone who can read the Rust.
2. **Widen the reproducibility checker** beyond its 11 builders, or at least
   add the `compute_atom_chi_*` family. That is the cheaper half and would
   turn this from folklore into a reported status.
3. **Until then, say so in the producer's docstring**, so the next agent doing
   attribution does not lose an hour to it as I did.

Not claimed: that the other atoms are safe. D and T were stable over ~12 runs
each; 4He costs 21 minutes and was run once, so it is simply unmeasured.
