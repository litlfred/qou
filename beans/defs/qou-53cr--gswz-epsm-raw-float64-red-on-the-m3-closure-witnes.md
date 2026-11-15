---
# qou-53cr
title: 'gswz-epsm: raw-float64 red on the m3 closure witness (wall-clock timing)'
status: completed
type: task
priority: normal
created_at: 2026-08-19T13:49:31Z
updated_at: 2026-08-19T13:54:31Z
---

## Fixed 2026-08-19 — a wall-clock timing, not physics

The single raw float64 was `.result.pair_search.seconds = 10.3` --
`round(elapsed, 1)`, a wall-clock timing.

The corpus convention for timing fields is a formatted STRING, set by
4e126c6f41 (35 timing fields across 28 producers). The SIBLING probe
gswz_epsm_descent_m4to24_probe.py already follows it and documents the reason
in a comment. This producer simply missed that sweep, which is why it was the
one witness in the arc still flagged NEW-dirty. Matched the convention rather
than inventing a duration_ms shape -- checking the sibling first is what
prevented that.

Ratchet: NEW dirty 1 -> 0, REGRESSED 0, drained +3,638 fields. All blocking
precision gates green.

The only non-ephemeral value that moved is the timing itself (10.3 -> "13.5",
machine-dependent by nature); every mathematical field is byte-identical.

No consumers of pair_search.seconds anywhere in the corpus (grepped .py/.ts/.md).
