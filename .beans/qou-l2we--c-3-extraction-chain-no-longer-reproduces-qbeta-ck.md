---
# qou-l2we
title: 'c_3 extraction chain no longer reproduces qbeta-ck-cache: off by 972 against a 1e-8 tolerance'
status: todo
type: bug
priority: high
created_at: 2026-08-30T16:12:03Z
updated_at: 2026-08-30T16:12:03Z
---

Surfaced 2026-08-30 by fixing `qou-ya1e`. This producer had been unrunnable, so
the regression was invisible rather than absent.

## The failure

`computations/probes/qbeta_ck_basis_constrained_pslq.py`, once it could run
again:

```
name       extraction_chain_reproduces_cache_c3
computed   972.3622884795565
expected   0.0
tolerance  1e-08
passed     False
source     same chain + same Q_codata + same q0 as qbeta-ck-cache.witness.json
```

`allPassed` True → **False**. Its previous witness was computed **2026-07-11**;
the producer has been dying at the save ever since (the `qou-ya1e` stamp import),
so nothing re-ran it and nothing noticed.

## Not caused by the repair

The only change to that file is a 4-line `sys.path` / `_path_bridge` preamble —
verified in `a5851c9e5`. It cannot move a number. The chain drifted from its
cache at some point in the last ~7 weeks and this is the first run since.

972 against a 1e-8 tolerance is not precision drift. Something structural moved:
a convention change, a pin change, or the cache itself.

## Todo

- [ ] Diff `qbeta-ck-cache.witness.json`'s history against the extraction
      chain's inputs over 2026-07-11 → now and find what moved.
- [ ] Check the convention-D propagation (2026-08-09/10) first — it is the
      largest structural change in that window and it is known to have moved
      other qbeta results by tens of percent.
- [ ] Decide which side is right: the cache or the chain. Do NOT retune the
      tolerance to make it pass.

## Related

`qou-s2no` (same cluster: `qbeta-decay-sdp-extended-ck` publishes all-null c_k
because no rung resolves). Whether these share a root cause is unestablished —
do not assume it.
