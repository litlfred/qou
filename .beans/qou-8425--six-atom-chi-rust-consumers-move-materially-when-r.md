---
# qou-8425
title: Six atom-chi-rust consumers move MATERIALLY when re-run — 3He goes null, one value moves 27x
status: todo
type: task
created_at: 2026-08-31T04:55:55Z
updated_at: 2026-08-31T04:55:55Z
---


Found 2026-08-31 draining `qou-4idm`. **Nothing here is committed** — all six
witnesses were reverted; only the ten precision-level ones were banked
(`e3ccfc9a4`).

## What happened

Sixteen producers read all four `atom-chi-rust-{d,t,3he,4he}.witness.json` and
had not been re-run since those upstreams were fixed on **2026-08-19**
(`fix(qou-chib): the two chi backends do agree`). All sixteen re-ran cleanly,
exit 0, ~1 s each. Ten moved at precision level. **Six moved materially:**

    27.8x   binding-rotation-phase-lead        + 11 values became NULL
     2.26   probe-content-energy-signed-phase
     1.00   binding-heat-kernel-weight-probe
     0.69   frobenius-gram-delta-lambda
     0.61   derive-binding-per-block-archimedean
     0.32   derive-binding-bond-sum

## The worst one, in detail

`binding-rotation-phase-lead.witness.json`, `data.d0_strong_channel.per_atom`:

    D     rho_full  14.669  -> 177.422      rho_d0_strong  16.7979 -> 484.458
    T     rho_full  18.3455 ->  46.8987     rho_d0_strong  19.9307 ->  52.9645
    3He   rho_full  18.6516 ->  None        rho_d0_strong  19.201  ->  None

³He going null is the same shape as the `qou-s2no` c_k nulls: the producer
guards with `mp.nstr(rho, 6) if rho else None`, so a zero silently becomes a
null rather than an error.

## ⚠️ The lesson, which is the reusable part

**`allPassed` did not flip on ANY of the sixteen** — including the one where
³He went null and a value moved 27x. Every producer exited 0. A drain is
therefore *not* safe merely because the producers run clean and the assertions
stay green; those signals were all present here and all uninformative.

The magnitude of the value change is the signal. Anything above ~1e-4 relative,
or any new null, needs a human/domain look before it lands.

## What is actually being asked

Was the 2026-08-19 chi-backend fix *supposed* to move these by 30x, or do these
six consumers have a latent defect that the old (wrong) upstream happened to
mask? Both are consistent with the evidence I have. Deciding needs someone who
knows what `rho_d0_strong` should be.

Until then these six stay stale — which is a known, recorded staleness rather
than an unexamined 30x change in a committed witness.
