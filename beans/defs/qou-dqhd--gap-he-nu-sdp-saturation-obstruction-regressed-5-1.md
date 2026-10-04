---
# qou-dqhd
title: 'GAP: he-nu-sdp-saturation-obstruction regressed 5 -> 11 raw float64 on main'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:21:50Z
updated_at: 2026-10-04T15:20:05Z
---

Found while running the mandated gate for bean qou-srvu (slice A), 2026-08-30.

`python3 computations/witness_raw_float64_audit.py` reports, on every run
across this branch:

    NEW dirty witnesses            : 0
    REGRESSED (count increased)    : 1
           5 -> 11      computations/he-nu-sdp-saturation-obstruction.witness.json

NOT caused by this branch, and that is measured rather than assumed:
  - the file is not in slice A (`grep -c` against /tmp/dispatch/srvu-a.txt = 0);
  - `git status --short` on it is empty at every point in the branch;
  - the same 5 -> 11 appears on the first gate run, before any producer here
    had been re-run.

So it is pre-existing on origin/main and belongs to whoever owns that
producer. Raised separately because the raw-float64 ratchet is supposed to
be drainable-only and a standing REGRESSED entry masks the next real one:
any future agent running this gate will see a non-zero REGRESSED count and
has to re-derive that it is not theirs, exactly as I did.

Recommended: identify the producer, re-run it, and confirm whether the 6 new
raw float64 fields are a genuine precision loss or a serialization change.



## Reasons for Scrapping

Duplicate of `qou-4pmk` (work-plan reorganisation 2026-10-04). Evidence: [M] same regression: he-nu-sdp-saturation-obstruction raw float64 5->11, same day
Content is untouched; only this work item is closed.
