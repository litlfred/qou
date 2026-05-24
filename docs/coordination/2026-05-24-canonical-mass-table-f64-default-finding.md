# Coordination — canonical_mass_table_extended.py default uses f64 (negative finding)

**Date:** 2026-05-24
**Status:** NEGATIVE FINDING — `laurent_q_rust` default in `canonical_mass_table_extended.py` operates at f64 precision, regressing the L1 50-dps floor (per `docs/precision-goals.md` + CLAUDE.md §Precision goals).
**Trigger:** PR #1064 (mass-table regen via pyhecke-native v0.9.0) tripped the witness-pipeline drift detector. Investigation revealed the precision regression below.

## TL;DR

Regenerating `canonical-mass-table-extended.witness.json` via the **default** method `laurent_q_rust` (the Tier 1.A path landed in PR #859 / refined through v0.9.0) produces `tr_M(β_p, q_0)` agreeing with the prior `markov_peel` (MPFR) baseline **only to digit 17** — i.e. at native f64 precision, not the 50-dps the field name claims.

```
field: tr_M_q0_canonical_50dps
  markov_peel (prior baseline, MPFR): 1.065306228592388759238723262727897372948
  laurent_q_rust  (new default,  f64): 1.065306228592389255153277569968066119334
                                                     ^─ diverges at 10^-17
```

`pyhecke_native` v0.9.0 exposes both `tr_m_atomic_mpfr` (`tr_m_atomic_mpfr_cached`) and the f64 surface. The dispatcher in `canonical_mass_table_extended.py compute_tr_m_canonical()` currently selects the f64 path; the witness `parameters` field correctly logs `"precision": "f64"`, but the data field naming (`tr_M_q0_canonical_50dps`) is misleading.

## What this PR does NOT do

- **Does not fix the script.** No production-pipeline change is being made here, per "WE NEED CANONICALLY DERIVED ONLY" + L1 50-dps floor. The fix is a separate canonical task.
- **Does not invalidate PR #1064.** That PR's empirical Tier 1.A speedup data (⁴He 1s, ⁵Li 6.2s, ⁶Li 68s, ⁷Li 693s) is real and reproducible; the data field naming + dispatch surface are the issue, not the Rust kernel.

## What this PR DOES

Records the finding in a stable coordination doc so the next agent can:
1. Switch the default in `compute_tr_m_canonical()` from the f64 `laurent_q_rust` path to `tr_m_atomic_mpfr` (or `tr_m_atomic_mpfr_cached`)
2. Re-run the full mass table; cross-check `tr_M(β_p, q_0)` matches the prior `markov_peel` baseline bit-for-bit at 50 dps
3. Either rename the witness field to reflect actual precision (if f64 is intentional for a non-canonical fast-path) or restore 50-dps and keep the existing field name

## Why this is a coordination doc, not an audit doc

Per CLAUDE.md §canonical-derivation discipline:
- Probes / explorations / spikes → `docs/audits/`
- Cross-PR / process / queue items → `docs/coordination/`

This is a **process** finding: the regen attempt's failure surfaced a script-level canonical-compliance gap. The fix lives in a separate focused PR; this doc just queues the work.

## Acceptance criteria for the follow-up fix

The follow-up PR must:
- [ ] Change `canonical_mass_table_extended.py compute_tr_m_canonical()` default for `--method laurent_q_rust` to dispatch through `tr_m_atomic_mpfr` (or its cached variant)
- [ ] `tr_M(β_p, q_0)` matches `1.065306228592388759238723262727897372948` to all 40 dps emitted in the witness (no f64 truncation at digit 17)
- [ ] Witness-pipeline drift detector passes (or: explicit field rename if the f64 path is retained as an opt-in alternative)
- [ ] Cross-check holds on the full p..⁷Li atom set

## Related work

- PR #859 (merged 2026-05-20) — landed Phase-2 Rust port (`tr_m_word_lq` recursion + MPFR path)
- PR #1064 (open, drift-detector RED) — the regen attempt that surfaced this finding
- PR #1063 (open) — Family A +2.89-3.86% gap audit (separate canonical-derivation issue)
- `docs/coordination/2026-05-22-tier-1a-rust-laurent-q.md` — original Tier 1.A coordination
- `docs/audits/2026-05-22-rust-laurent-q-reduce-results.md` — original Tier 1.A results

## Disposition of PR #1064

Per author direction (2026-05-24): **/prepare-merge auto**. The PR will run through the standard prepare-merge automation. If the drift detector continues to red-flag, that's expected — the finding (this doc) is the deliverable, and PR #1064 may be closed in favor of the follow-up fix PR.
