---
# qou-pin3
title: 'alpha_5_lp_dual_crystal: regeneration picks a DIFFERENT optimal LP dual vertex — excluded from the tnjb batch'
status: todo
type: task
priority: normal
created_at: 2026-08-08T20:05:00Z
updated_at: 2026-08-08T20:05:00Z
---

Held out of the 2026-08-08 `tnjb` stale-stamp migration, deliberately, and
reverted after the value audit caught it.

## What happened

`alpha-5-lp-dual-crystal.witness.json` is stamped `muon` while its producer
resolves proton, so it was a legitimate tnjb candidate. But regenerating it here
changed **24 LP solution entries** that are not explained by the anchor:

```
data.at_q0_per_stratum.ht6.per_atom.2.lp.y_star.2    0.0 -> 0.020749613956537
data.at_q0_per_stratum.ht6.per_atom.1.lp.y_star.2    0.0 -> 0.000764070473307
data.at_q0_per_stratum.ht6.per_atom.0.lp.y_star.0    0.0 -> 0.000097401828163
...plus ~21 entries at 1e-13 .. 1e-17 (solver tolerance noise)
```

An ~11.5 ppb q₀ move cannot take a dual coordinate from exactly `0.0` to
`0.0207`. What it looks like is a **degenerate LP with multiple optimal dual
solutions**, where the solver landed on a different vertex.

## Why that is plausible here specifically

This producer was the one `REVERT-fail` in the first tnjb pass —
`ModuleNotFoundError: No module named 'pyhecke'`. It only became runnable after
`pyhecke` was put on the path and `clarabel` + a freshly built
`pyhecke-native 0.9.0` were installed in this container. So the committed
witness and my regeneration were produced by **different solver stacks**, and
the difference shows up exactly where a degenerate LP would show it.

## Why it was excluded rather than committed

AGENTS.md §"LP / SDP duals — first-class infra (do not skip)" treats these duals
as load-bearing, not incidental output. Folding a changed dual vertex into an
*anchor* migration would bury a substantive change inside a bookkeeping one —
and the `y_star` values are precisely the shadow prices downstream consumers
read.

Both the witness revert and the manifest entry were undone, so the file is back
to `UNDETERMINED` rather than sitting as a `DECL_MISMATCH`. `allPassed` did not
regress in the regenerated version — this is not a failure, it is an
*unexplained-by-the-stated-cause* change, which is a different and worse thing
to commit silently.

## Next step for whoever picks this up

1. Confirm the LP is degenerate at these strata (multiple optimal duals) — if
   so, the vertex choice is solver-dependent and the witness needs either a
   deterministic tie-break or a recorded solver fingerprint.
2. Decide whether `y_star` consumers depend on the specific vertex. If they do,
   a vertex change is a real downstream event and must not ride in on any sweep.
3. Only then re-run it for the anchor, with the dual change reported separately
   from the q₀ change.
