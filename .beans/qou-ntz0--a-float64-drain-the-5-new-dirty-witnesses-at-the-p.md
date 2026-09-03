---
# qou-ntz0
title: 'A (float64): drain the 5 NEW dirty witnesses at the producer (96 fields)'
status: completed
type: task
priority: normal
created_at: 2026-08-25T16:31:28Z
updated_at: 2026-08-25T18:27:50Z
---

## SUPERSEDED 2026-08-25 — a sibling landed the same drain on main first

Reopened from completed to record the correction. This bean's work did NOT land:
main's 147aeb66c / e1114b1b2 / a97d415bd drained the same four float64 witnesses
and migrated the same pauli_young hand-copy while PR #5767 was open. The merge
took THEIRS on all ten conflicting files, correctly — theirs evaluates F_q(1) at
the exact classical Young form (mine used an eps=1e-30 offset), verified the
ninths to 22 digits and found them conjugation-symmetric, and separated the pin
question from the precision question instead of moving both at once.

Also dropped my `young_seminormal.seminormal_sigma_symmetric` — main's
`hecke_characters.build_seminormal_matrices_mp` is the same object placed better.

WHAT SURVIVES as measurement, independent of whose code landed:
- '5 NEW dirty witnesses' was 4 defects + 1 false positive (`elapsed_sec`,
  a wall-clock timing; bean qou-ywee).
- The 258k headline is not a drain target: 224,863 are integral-valued floats.
- Four producers hardcoded the MUON literal, one labelled it proton-pinned —
  the stamp and the arithmetic are independently settable.
