# mass-table `m_e` re-pin (precision follow-up)

Author-approved follow-up to the I9 flag in #2262. `mass_table_l1_full_crosscheck`
and `mass_table_ppb` use a truncated 8-sig `m_e` as a derivation **input**; routing
to the full-precision `M_E_MEV` registry value shifts results ~1.35e-9 rel — *above*
the 10⁻¹⁵ L1 floor, so this is a **precision improvement** (removes truncation error).

## Discipline (CLAUDE.md §Precision goals — STRICT)
- Route the two mass-table scripts' `m_e` input to `M_E_MEV` (qou-substrate/pyhecke registry).
- Re-run BOTH dashboards and report deltas; **do not regress either leg**:
  - L1: `folio-assistant/computations/onepb-status-dashboard.witness.json`
  - L2: `folio-assistant/computations/per-observable-100x-status.witness.json`
- Mark the two `mass_table_*` I9 queue items resolved.
