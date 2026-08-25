---
# qou-ywee
title: raw-float64 ratchet counts wall-clock elapsed_sec as a precision finding
status: completed
type: bug
priority: normal
created_at: 2026-08-25T16:55:44Z
updated_at: 2026-08-25T19:49:04Z
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


## CORRECTION 2026-08-25 — my implementation was retracted; a sibling's is better

A sibling landed the same fix on main (`d9df357d69`, 42 fields in 19 witnesses)
while PR #5783 was open. **My 73-name frozenset is retracted, not merged.**

Theirs derives from `qou_substrate.witness._EPHEMERAL_META_FIELDS` — the list
that already DECLARES these names reserved for runtime metadata, guarded by
`test_ephemeral_mask_sync`. That mask holds 9 names, 5 durations; they carve
exactly those 5. It also fails CLOSED: an import error yields the empty set, so
the gate gets stricter, never looser.

Mine was hand-built from a corpus enumeration. Those 73 names are declared
reserved **nowhere**, so carving them asserted on my own authority that
`walltime_sec`, `rust_secs`, `time_sec` and 70 others are metadata — a wider
claim than any canonical source supports, in a hand-kept list that decays.

## FOLLOW-UP, properly scoped (the part still open)

Their 5 declared names cover **42** fields. The corpus carries **~495**
timing-shaped float fields; the other ~411 sit under undeclared names —
`walltime_sec` 99, `rust_secs` 46, `time_sec` 42, `compute_time_sec` 38,
`wall_sec` 36, `solve_time_s` 33, and ~65 more.

**The right home is `_EPHEMERAL_META_FIELDS` itself, not a second list in the
audit.** Extending a shared reserved-names mask is a wider change than this
bean and belongs with the module owning the declaration.

## THE GUARD THAT MUST SURVIVE ANY SUCH WIDENING

Six self-test cases landed (31 → 37). Measured: broadening the filter to
`/time|wall|_sec|elapsed|dur/` matches **84** distinct names, of which **19**
are physics or ratios, and excusing them removes **361 real float64 fields**
from the gate — including `y_times_chi` (177) and `y_times_chi_abs` (93), the
Frobenius pairing y_λ·χ_λ. `_times_` is MULTIPLICATION. The gate would stay
green while excusing the framework's central object. I wrote that regex first
and the corpus caught it.
