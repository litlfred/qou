---
# qou-lk7v
title: The rho-k co-casimir witness gained a raw float64 (3 -> 4) in the convention-D cascade
status: completed
type: task
priority: normal
created_at: 2026-08-16T11:27:45Z
updated_at: 2026-08-16T13:06:43Z
---

Found while wiring sigma_all_evaluator (PR #5199). NOT mine: git status shows the file untouched on my branch; it landed 2026-08-10 in 506ac91350 'witness: convention-D cascade, producers 41-44'.

witness_raw_float64_audit --strict:
  REGRESSED - these witnesses gained raw float64:
         3 -> 4       computations/rho-k-co-casimir-extended.witness.json

It is the only REGRESSED entry in the corpus. Fix at the producer (carry the
value as mpmath.mpf from its source and serialize with _precision.fmt); do NOT
widen raw-float64-baseline.json. Left for the convention-D cascade owner rather
than fixed inline -- different domain, and that cascade has an active sibling.

RESOLVED 2026-08-16. Not fixed by reformatting the wall-clock field — the prior audit (docs/audits/2026-08-15-rho-k-co-casimir-stale-convention-c-needs-d-refresh.md) had already root-caused it as stale convention C and called the surgical fix wrong. Regenerated the witness: uniformly convention D, 0 raw floats, REGRESSED 0 corpus-wide.

That audit's DEFERRAL was misdiagnosed and is corrected in place: the blocker was the producer's memory guard (14.8GiB wanted vs 14.9 free), not compute time. With gmpy2 installed every atom is FASTER here than on the origin machine (helium-4 734s vs 2533s recorded); --workers 1 completes it.
