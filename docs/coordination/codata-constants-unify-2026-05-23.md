# Coordination Ledger: CODATA Constants Unification (2026-05-23)

## Goal
Upgrade `codata_constants.M_E_MEV` from 8 sig figs (0.51099895) to full CODATA-2022 precision (0.51099895069 / 11 sig figs) + auto-generate `cal-3-q-beta.witness.json` via `build_cal_3_q_beta_witness.py`.

**Primary PR:** #996 (M_E_MEV precision upgrade + CAL-3 witness generator)

## Scope Map

| PR | Axis | Relationship | Status |
|----|------|--------------|--------|
| #996 _(current)_ | compute | Primary | Open, just pushed (21:03 UTC) |
| #992 | canonical | Audit overlap (2 criteria may flag files) | Open, concurrent (20:03 UTC) |
| #999 | compute | Independent (witness pipeline, different engine) | Open (21:03 UTC) |
| #998 | compute | Independent (knot theory domain) | Open (21:01 UTC) |

## Overlaps Identified

### PR #996 ↔ PR #992: Canonical Audit Criteria

**Two criteria in PR #992 may interact with #996's changes:**

1. **`canonical-script-not-deprecated`** (PR #992, new criterion)
   - Flags imports of SUPERSEDED/DEPRECATED modules across 15 blocks
   - **#996 concern:** `codata_constants.py` import of M_E_MEV — not deprecated ✓

2. **`canonical-no-hardcoded-observable`** (PR #992, new criterion)
   - Flags hardcoded MeV/keV values with `=` instead of `≈`
   - **#996 concern:** M_E_MEV now sourced from `codata_2022_source` (source-of-truth pattern) — should pass ✓

**Verdict:** No blocking issues expected. Both criteria should pass on #996's files.

## Coordination Actions

- [x] **Post scope map** (this ledger) ✓
- [x] **Post coordination intent on #992** (sibling notice) — comment #4526520726 ✓
- [x] **Subscribe to PR #996 activity** (for review comments, CI changes) ✓
- [ ] **Await PR #992 canonical audit sweep results** — monitor if any findings on #996's files
- [ ] **Triage canonical findings if any** — accept/reject/escalate per protocol
- [ ] **Monitor both PRs for landing** — if #992 lands first, re-run canonical audit on #996; if #996 lands first, no action needed

## Dependencies

**None identified.** Both PRs modify independent code paths (compute vs. canonical) with no blocking relationships.

## Next Steps

1. Wait for `#992` audit sweep to complete (if running against full codebase, ~5–10 min)
2. If canonical findings flag #996's files → triage & respond
3. Both PRs can merge independently once CI passes

---

**Created by:** `local/coordinate` skill (2026-05-23 21:15 UTC)
**Session:** fff841a4-8f92-49ca-8b6b-aec4856ab2e2
