---
# qou-ywee
title: raw-float64 ratchet counts wall-clock elapsed_sec as a precision finding
status: completed
type: bug
priority: normal
created_at: 2026-08-25T16:55:44Z
updated_at: 2026-08-25T19:40:38Z
---

## CLOSED 2026-08-25 (PR #5783)

Fixed as a CLASSIFICATION, not a baseline widening — a fourth bucket beside
integral-valued floats, counted and reported on the console and in the witness
(`wall_clock_carved_out_fields` / `_by_file` / `_field_names`).

453 fields across 97 witnesses; 40 witnesses were dirty ONLY because of timings.
Buckets stay disjoint (deprecated-f64 carve-out 97 -> 91, the 6 being timings).

**The finding worth keeping:** an exact-name frozenset is MANDATORY here. The
obvious regex /time|elapsed|wall|_sec$/ matches `y_times_chi` — 177 fields, the
Frobenius pairing y_λ·χ_λ — because `_times_` is multiplication. A pattern-based
carve-out would have excused the framework's central object from the precision
gate. I wrote that regex first; the corpus caught it. All of those names are now
self-test cases that must still count (24 -> 34 cases).
