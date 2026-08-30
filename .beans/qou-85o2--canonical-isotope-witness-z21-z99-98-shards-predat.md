---
# qou-85o2
title: canonical-isotope-witness Z21-Z99 (98 shards) predate the C-excision; a spot re-run moved 2.19x and the cause is NOT isolated
status: todo
type: bug
priority: normal
created_at: 2026-08-30T08:08:03Z
updated_at: 2026-08-30T08:08:50Z
---

Surfaced by the qou-zzwm survey. Filed separately because the cause is NOT
isolated and it must not be reported as convention drift.

THE OBSERVATION: computations/ canonical-isotope-witness-Z*.json split cleanly
across the C-excision commit a24fdac8a1 (2026-08-24T11:04) in the symbolic
Hecke core:
    Z00..Z20  computedAt 2026-08-24T14:40  -- AFTER  (regenerated)
    Z21..Z99  computedAt 2026-08-23T17:15  -- BEFORE (98 shards, not regenerated)
Declared by content/.../appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md.
They carry layer "L4-qclt-colour-weighted" -> channel_binding, which is
z-dependent, so the boundary is at least suspicious.

WHY IT IS NOT (YET) A CONVENTION FINDING -- this is the load-bearing part.
A spot re-run of Z=26, N=19 gives qclt_binding = 120.70 MeV against the
recorded 55.088 MeV: a factor of 2.19. The survey that found this had PREDICTED
a move of x0.73 from the log-ratio of f_pn(std) between the two conventions
(0.3948 C vs 0.5082 D). 2.19 is not 0.73, and not its inverse. So convention
alone does NOT explain the gap, and something else moved in that producer's
cone as well.

Reporting it as "98 stale convention-C shards" would be the exact error class
AGENTS.md warns about: a topic match plus a plausible mechanism, asserted
without the arithmetic agreeing.

NEXT STEP, in order:
  1. Reproduce Z=26,N=19 twice more to confirm 120.70 is stable (one run is
     not a measurement).
  2. Bisect the producer's import cone across 2026-08-23..24 to find what ELSE
     changed. witness_import_cone_staleness_audit.py exists for exactly this --
     a producer's own source can be byte-stable while a module it calls moved.
  3. ONLY THEN decide whether regenerating the 98 shards is the fix, and say
     which change actually moved the number.

Do not mass-regenerate first and diagnose after: 98 shards regenerated on an
unexplained 2.19x would bake in whatever the unidentified second cause is.
