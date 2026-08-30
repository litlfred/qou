---
# qou-ag0x
title: AME UNSAFE tail is 502 sites in 194 files, not 262/101 — the roadmap now measures it
status: todo
type: task
created_at: 2026-08-29T20:03:23Z
updated_at: 2026-08-30T04:05:00Z
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

---

## TARGET class drained (this branch)

The role classifier (2ce2597ac) split the UNSAFE tail into TARGET / INPUT /
REVIEW. TARGET is now drained: 109 literal sites in 53 producers read
`codata_constants`, and the triage reports

    SAFE     9 routes in  4 files   (unchanged -- pin fixtures, must stay literal)
    TARGET   0 sites  in  0 files   (was 109 in 53)
    INPUT    0 sites  in  0 files   (was 0 -- nothing was ever routable here)
    REVIEW 389 sites  in 140 files  (unchanged -- the tail that needs reading)

Twenty-seven distinct spellings of four binding energies and four atomic
masses collapsed onto nine constants. Largest value move 3.06e-6 relative
(2.224573 -> 2.2245662); smallest 1.9e-10.

The INPUT count is 0 both before and after, which is only worth stating
because the classifier's `--selftest` pins a positive INPUT case: the path
fires, it just has nothing to fire on. The calibration sites that do exist
(e.g. `binding_single_pipeline_comparison.py:255`, `alpha_D =
deut["B_AME_MeV"] / ell_bond`) read AME out of WITNESSES, not literals, so
the 3-cal blocker was never in this tail.

Left behind on purpose: the deuteron literal `2.22452`, 2.1e-5 from the
registry -- too far to be a rounding. See qou-e2cf.
