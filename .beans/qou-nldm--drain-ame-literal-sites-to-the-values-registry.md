---
# qou-nldm
title: Drain AME-literal sites to the values registry
status: completed
type: task
priority: normal
created_at: 2026-08-30T08:47:57Z
updated_at: 2026-08-30T10:02:55Z
---

Route hardcoded AME binding-energy literals in computations/ to the named registry constants (AME_B_*_MEV_VALIDATION).

Roadmap from probes/ame_registry_routing_triage.py:
- SAFE (byte-exact string match): 9 sites / 4 files
- UNSAFE: 195 sites / 80 files
  - INPUT   25 sites /  7 files -- NEVER route (reaches a scale/calibration name)
  - REVIEW 170 sites / 73 files -- needs reading

Branch: claude/ame-roadmap-replant-2026-08-29 (worktree /tmp/qou-mine).

## Todo
- [x] Route the SAFE sites that survive review — 6 of 9 routed, 3 are self-test fixtures
- [x] Fix the triage: byte-exact string match is NOT sufficient for SAFE
- [x] Split REVIEW into ROUNDING (63, routable) and DIVERGENT (125, needs a ruling)
- [x] Route the 63 ROUNDING sites — verified, 0 unexplained leaves
- [x] DIVERGENT: 110 sites routed, 16 held as per-site INPUT
- [x] Rule on the self-test sites — delta_lambda routed, pin validator and dps
      audit held (each DEMONSTRATES something its own literal is required for)
- [x] REVIEW bucket is 0. The drain is complete; what remains is 25 INPUT sites
      and 6 demonstration literals, all permanently excluded with reasons.
- [x] Close verification loose ends — see qou-fsva, now completed

## Summary of Changes

The AME-literal drain is complete. 167 sites across 72 producers now read the
registry; REVIEW is 0.

| bucket | start | end | disposition |
|---|---|---|---|
| SAFE (byte-exact)  |   9 | 0 | 6 routed, 3 are self-test fixtures |
| ROUNDING           |  63 | 0 | routed (2 held: per-site INPUT) |
| DIVERGENT          | 125 | 0 | 110 routed, 16 held as INPUT (3-cal) |
| IN-SELF-TEST       |  16 | 6 | 4 routed; 6 are demonstrations, 6 were phantoms |

Permanently excluded, with reasons: 25 INPUT sites (an AME value reaching a
scale/calibration/prediction name), and 6 demonstration literals
(registry_witness_pin_validator reproduces the 2026-06-22 row-swap incident;
mpf_import_time_dps_audit demonstrates a dps=15 build pitfall).

### What the drain found

- **c86e55ec9 broke three producers** with a half-finished edit: call sites
  changed to `dim_q(..., Q0_PROTON)`, parameter never added.
  fr_pullback_borromean_h3a_test computed 80 minutes before reaching it.
- **The values were typos, and the producers said so.** Twelve `data_loaded`
  assertions were failing at HEAD because a hand-typed `expected` disagreed with
  what actually loaded. All twelve pass now; none went the other way.

### What the verification found out about itself

- A **propagation check says a change is CONSISTENT, never that it is
  PERMITTED.** A 4He binding feeding `B_pred` was verified as textbook
  first-order propagation (12C moved by exactly 3x, 16O by 4x) while being a
  3-cal violation. Nine such sites were routed and reverted.
- **Calibrate the checker before trusting it.** A 6% propagation window over 12
  moves and 12 multipliers accepts 67% of arbitrary deltas; its "0 unexplained"
  meant nothing. 0.1% gives 2-3%, and it must be re-measured per round.
- **Two producers cannot be verified by re-running at all.** pn_alpha_lp_dual
  (SCS/linprog) and difference_knot_binding_probe (SnapPy `M.randomize()`, 40x,
  unseeded) each differ from THEMSELVES by more than the drain bound.
- **A third of baselines were stale** until each witness was mapped to its
  producer by the `scriptFile` it records rather than by filename stem.
