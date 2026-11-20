---
# qou-07ts
title: 'compute_atom_chi_rust 3He is nondeterministic at the 50th digit: 4 distinct outputs in 8 runs'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T08:33:29Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
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


---

## 2026-09-05, later: 4He is nondeterministic too — the "unmeasured" caveat resolves the wrong way

This bean originally said *"4He costs 21 minutes and was run once, so it is
simply unmeasured"*. It has now been re-run, and it wobbles.

**Measured**, one re-run against the committed witness, producer diff
comment-only so nothing in the source changed:

    chi_lambda values      154 total
    moved                    4  (2.6 %)

Each by exactly one unit in the last decimal place of the 50-dps string —
three down, one up:

      1.3324670695047317581719299734538231951319133898682  ->  ...681
     -6.1493408410039581656739678815748871446717776464091  ->  ...090
    532.26390734569385307344345076726294286328451841452    ->  ...451
    995.38207963430477298589219373442229918107243023194    ->  ...195

`n_partitions` is unchanged at 77 = p(12).

**So the defect is not specific to 3He.** Standing tally of what has been
observed, with sample sizes, because they are very uneven:

| atom | runs | outcome |
|---|---|---|
| D | ~12 | stable |
| T | ~12 | stable |
| ³He | 8 | **4 distinct outputs** |
| ⁴He | 2 | **moved on the second** |

D and T are the small cases (`n_partitions` 11 and 30); ³He and ⁴He are the two
that wobble. But T also has `n_partitions` = 30, equal to ³He, so **size alone
does not separate the stable from the unstable** — which was true before and
is worth restating now that the sample is bigger.

**Rate is not established for ⁴He.** One re-run is one re-run; 2.6 % of values
moving in that single pair says nothing about how many distinct outputs exist.
Establishing that costs 21 minutes per sample and has not been spent.

**What this changes for the closing conditions above:** item 2 (widen the
reproducibility checker) gets more valuable, not less — the affected set is at
least two producers' worth of output, and the checker's eleven-script scope
still reaches neither.

## Extension from qou-wdij (PR #6864) — 3H wobbles too, and the trace does not

Re-measured the SAME kernel function through a DIFFERENT entry path
(`chi_general_word.chi_all_lambda_general` -> `pyhecke_native.chi_lambda_all_partitions_mpfr`,
i.e. not via `compute_atom_chi_rust`), 8 runs each, sha256 over the 50-digit chi
strings:

    3He   4 distinct fingerprints in 8    <- reproduces this bean exactly
    3H    2 distinct fingerprints in 8    <- this bean recorded T as STABLE

So the finding is **not specific to 3He or to that producer**. 3H shows it too,
just more rarely — a 1-in-8 event is easy to miss in a smaller sample, which is
presumably why D and T read as stable here. Reported as an extension on more
draws, not a contradiction.

**Magnitude, which this bean did not quantify:**

    max |d chi| across 8 runs   1.00229e-50   (~1 ulp at 50 dps)
    max relative                7.46451e-50
    spread in tr_M              EXACTLY 0.0

The per-partition characters wobble at the last serialized digit; the
y_lambda-weighted trace **does not move at all**. That sharpens this bean's
'does not threaten L1 or any physics claim' from an order-of-magnitude argument
into a measured zero at the observable level — while leaving the attribution
damage exactly as stated, since it is the per-chi strings a witness diff compares.

Standing checks now live in
`computations/probes/nonmonotone_atom_trace_kernel_route_probe.py` (19/19):
the wobble stays ~1 ulp, and it does not reach tr_M. Deliberately NOT a
fingerprint-count assertion — the wobble is stochastic (2 in 8 vs 4 in 8), so
asserting 'unstable' would itself be flaky.

## Implementation & Witness Progress (PR #8269)
- Branch: `qou-10v9-07ts-324i-49vn-4pdh-5mxd` (`7a961cf268c0cf36c3f70fd39f92645c16c9a30a`), PR: `litlfred/qou#8269`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/ChiRustNondeterminismOverrideBlindnessChiCacheStalenessQmpDigitCapAndMagnusFarCommutativity.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/chi_rust_nondeterminism_override_blindness_chi_cache_staleness_qmp_digit_cap_and_magnus_far_commutativity_probe.py` -> `computations/probes/chi-rust-nondeterminism-override-blindness-chi-cache-staleness-qmp-digit-cap-and-magnus-far-commutativity.witness.json` (`allPassed: true`, `scriptCommitSha: e7b85e53d7a8855337daf870617a2e9a6b0acc11`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8269, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-05: "beans(qou-07ts): 4He wobbles too — the 'unmeasured' caveat resolves the wrong way"). The work may be partly or fully done. Read the bean before you close it.
