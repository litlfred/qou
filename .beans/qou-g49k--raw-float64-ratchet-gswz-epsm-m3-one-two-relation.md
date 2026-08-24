---
# qou-g49k
title: 'raw-float64 ratchet: gswz_epsm_m3_one_two_relation_closure carries a wall-clock float'
status: completed
type: bug
priority: normal
created_at: 2026-08-19T18:14:44Z
updated_at: 2026-08-23T18:06:47Z
---

`witness_raw_float64_audit.py` reports `new_not_baselined: 0 -> 1` after
merging main into `claude/agent-pr-5168-merge-rhmf94`. The offender:

    computations/probes/gswz_epsm_m3_one_two_relation_closure.witness.json
    .result.pair_search.seconds = 10.3        (1 field)

Landed on main in `cec4adf0` ("epsm(w4gn): m=3 closed for one and two
relations"), provenance-refreshed in `964ccbb3`. **Not mine** — my branch
does not touch that path (`git diff --name-only origin/main...HEAD | grep
gswz` -> 0). Reported rather than absorbed.

## The field is a wall-clock duration, not a computed quantity

So no mathematics is corrupted by it, and the standing fix ("carry
mpmath.mpf from the source, serialize with `_precision.fmt`") is a poor
fit — there is no higher-precision source for a timing. The producer-side
fix is one line: `fmt(...)` it, or drop it (the schema already carries
`durationMs` at top level, which the auditor does not count).

## What I deliberately did NOT do

- **Not baselined.** The auditor says so explicitly: *"Do NOT add the file
  to the baseline to silence this."*
- **No timing carve-out added.** Both existing carve-outs
  (`LP_DUAL_F64_FIELDS`, `float64-integrator`) are owner decisions on the
  record and are written to be *deliberately narrow* — the integrator one
  even refuses to key on `tier: exploratory` precisely so it cannot widen
  into "ordinary f64 sloppiness". A "timings are exempt" class is the same
  kind of decision, on a shared audit script, for another agent's live
  file. Not mine to make unilaterally, and a wrong one here is the sort
  that quietly excuses real fields later.

## Owner call needed on which of these

1. Producer fix (one line, in whoever owns the ε_M probe).
2. A named, narrow timing carve-out in the auditor — but note it would
   have to distinguish a *duration* from a computed seconds-valued
   physical quantity (a lifetime, a decay time), which is exactly a
   channel this framework predicts. That is the reason to be careful, not
   a reason it cannot be done.
