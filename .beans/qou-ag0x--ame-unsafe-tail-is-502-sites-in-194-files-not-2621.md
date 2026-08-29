---
# qou-ag0x
title: AME UNSAFE tail is 502 sites in 194 files, not 262/101 — the roadmap now measures it
status: todo
type: task
created_at: 2026-08-29T20:03:23Z
updated_at: 2026-08-29T20:03:23Z
---

The SAFE (byte-exact, value-preserving) class is DRAINED as of 897caf93f —
11 routes, verified moved=0. What remains is the UNSAFE class, and it is
roughly double what the roadmap used to report.

    before the roadmap fix (37ccad0b6)   SAFE 18 / 13 files   UNSAFE 262 / 101 files
    after                                SAFE 20 / 15 files   UNSAFE 502 / 194 files

240 sites across 93 files were invisible because probes/ame_registry_routing_
triage.py globbed `computations/*.py` top level only, hiding probes/,
deltalambda/, phase5/ and sweeps/. Anyone who scoped this migration from the
old number was planning against a tail 48% smaller than it is.

WHY UNSAFE IS NOT A SWEEP
Routing a literal that is not byte-exact CHANGES A VALUE. Commit 03c25e8db
(owner: "ame data is in corpus") moved the canonical definition off
`binding_energy_total_keV` — derived, and computed in float64 by
vendor_ame2020.py — onto the quoted `binding_energy_per_A_keV`, so literals
that were byte-exact BEFORE that commit are now near-misses. They are STALE,
not mistyped, and the direction is settled by owner directive — but 194
producers re-run with per-witness verification is a migration, not a pass.

AND PART OF THE CLASS MUST NOT BE ROUTED AT ALL. Bean fvxq's triage: routing
a `_VALIDATION` constant into a prediction INPUT violates the 3-cal
discipline. These constants are comparison targets. Nothing in the roadmap
distinguishes input sites from target sites, so that classification is the
real prerequisite for planning the sweep — and it is the obvious next piece
of work here.

Also excluded deliberately: registry_witness_pin_validator.py is in the SAFE
list and must stay unrouted, because its literals are the fixtures it
validates the registry against.
