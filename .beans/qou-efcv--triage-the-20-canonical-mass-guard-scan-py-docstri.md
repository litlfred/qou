---
# qou-efcv
title: Triage the ~20 canonical-mass guard --scan-py docstring hits, then wire it on by default
status: completed
type: task
priority: normal
created_at: 2026-08-08T21:05:39Z
updated_at: 2026-08-08T22:43:31Z
---


Follow-on from PR #4822, which added `--scan-py` to
[`computations/canonical_mass_status_guard.py`](../computations/canonical_mass_status_guard.py)
and left it **opt-in**.

## Why opt-in rather than on

The pass is verified to catch what it was built for (the pre-fix
`mass_table_comprehensive.py` docstring; clean on the corrected one). But it
currently raises **20** further hits that nobody has read. Turning it on by
default would flip a green guard red on an untriaged list, which is precisely
how a guard gets ignored — the same reasoning the guard already applies to the
dated doc archive.

## The work

Classify each hit below into one of:

1. **stale live-status claim** → fix the docstring (as #4822 did for
   `mass_table_comprehensive.py`);
2. **legitimate §3 research / verification / deprecated-module self-description**
   → add to `ALLOWLIST_SUBSTR`, or extend `NEGATED` / `COUNTERFACTUAL` if the
   phrasing generalises (preferred — allowlisting a whole file blinds the guard
   to *future* staleness in it);
3. **out of scope** → tighten `PY_EXCLUDED_DIR_PARTS`.

Then flip `--scan-py` on by default and wire it into CI.

Several are likely (2) on sight — the 2026-07-05 migration audit already
classified `_li_2_q_util.py`, `mass_vol_density.py`,
`m_p_borromean_verification_50dps.py`, `entanglement_emitted_energy.py`,
`volume_def_reconcile.py`, `per_knot_mass_table_demonstration.py`,
`vol_density_per_block_wiring.py` and `e0_lambda_tryall.py` as guardrail-§3
permitted. **Do not rubber-stamp them from that audit alone** — it inventoried
*call sites*, and this is a different surface. Read each docstring.

## Current hit list (2026-08-08)

- `computations/_li_2_q_util.py`:477 —  nucleon mass m_avg, and is +2.89 % high.  The correction is the
- `computations/audit_delta_S_chain.py`:26 —  m_n/m_e = (Vol(ℬ_3)/ℏ_q²) · λ_scale_n + S(n)
- `computations/audit_delta_S_chain.py`:27 —  m_p/m_e = (Vol(ℬ_3)/ℏ_q²) · λ_scale_p + S(p)
- `computations/borromean_binding_recompute.py`:5 —  no m_e·Vol(𝓑₃)): every nucleus AND every nucleon mass flows from the same
- `computations/borromean_volume_propagation_to_m_p.py`:20 —  If true → swapping in the correct Vol(𝓑₃) closes m_p entirely.
- `computations/entanglement_emitted_energy.py`:15 —  Quantification. The proton mass is m_p = m_e · (Vol(𝓑₃)/ℏ_q²) · LW(q), where
- `computations/gamma_gamma_pair_production_decomposition.py`:212 —  m_p = m_e · (Vol(𝓑₃)/ℏ_q²) · linking_weight_exact
- `computations/lambda_scale_rd4_k_p_search.py`:5 —  so that `m_p/m_e = Vol(K_p)/ℏ_q²` directly (no λ_scale, no Skein).
- `computations/lambda_scale_refinement_h4_correction_bring.py`:35 —  (a) canonical Wedderburn alone:         m_p ≈ 965 MeV  (+2.89%)
- `computations/m_p_borromean_verification_50dps.py`:32 —  m_n^pred ≈ 966.71 MeV      (vs CODATA 939.57, ~2.9 % off)
- `computations/m_p_borromean_verification_50dps.py`:110 —  (prop:flavor-split-substrate) then assigns m_p ≈ 965.4, m_n ≈ 966.7
- `computations/m_p_borromean_verification_50dps.py`:111 —  (both +2.89 %), with the SPLIT ratio Δm/M_N matched to ~305 ppm.
- `computations/m_qclt_approx.py`:22 —  The per-nucleon mass `m_e · vol_density_borromean` carries the **+2.89 %
- `computations/mass_per_knot_density.py`:126 —  reading taken literally gives m_p ≈ 406 MeV (−56.7%); production's
- `computations/mass_vol_density.py`:133 —  reading taken literally gives m_p ≈ 406 MeV (−56.7%); production's
- `computations/per_knot_density_per_block_wiring.py`:38 —  of the +2.89 % m_p gap — RAW.  No tuning to m_p or B_AME.
- `computations/qbeta/qbeta_ck_truncation_order_analysis.py`:17 —  3.47% m_p-pin swing, 2.98% cross-anchor
- `computations/skein_proton_canonical.py`:11 —  m_p = m_e · [Vol(𝓑₃)/ℏ_q² · λ_p_scale + S(p)]
- `computations/vol_density_per_block_wiring.py`:38 —  of the +2.89 % m_p gap — RAW.  No tuning to m_p or B_AME.
- `computations/yekutieli_volume_join.py`:11 —  Production (m_p path):   m = m_e · Vol(𝓑₃)/ℏ_q² · linking_weight

Regenerate with: `python3 computations/canonical_mass_status_guard.py --scan-py`

## 2026-08-08 — triaged; pass is ON by default (PR #4826)

All 20 hits read and classified. **9 were stale live-status claims and were
fixed**; **11 cleared by rule**, never by `ALLOWLIST_SUBSTR` — an allowlist
entry blinds the guard to *future* staleness in that file, which is the
opposite of what this pass is for.

**Fixed (stale):** `entanglement_emitted_energy` (flat "The proton mass is
m_e·(Vol(𝓑₃)/ℏ_q²)·LW"), `m_p_borromean_verification_50dps` (×3 — now carries
a 2026-06-24 supersession banner), `mass_vol_density` + `mass_per_knot_density`
("production's near-correct m_p comes from the global scalar" — it does not,
and λ_A ≈ 2.46 is the CODATA-implied fit), `skein_proton_canonical`,
`yekutieli_volume_join` ("Production (m_p path)"), plus two the detector now
clears but that were stale on reading: `lambda_scale_refinement_h4_correction_bring`
("framework canonical predictions are … 965 MeV") and
`borromean_volume_propagation_to_m_p` (calling a zero-importer deprecated
script "the production script").

**Cleared by five rules,** each from the docstring that motivated it:
`SUMMARY_SCOPE` (EXPLORATORY / DEPRECATED / counterfactual marker in the
summary governs what is under it — restricted to *scope* markers, not all of
`NEGATED`, so "derive or refute the 2.38× bridge" does not grant blanket
immunity); `no <deprecated-token>` as an absence disclaimer; `NAMES_THE_GAP`
(**.py only** — the 2026-08-01 prose recurrence said "2.89% Vol·ρ gap" *as*
the status, so this rule must never reach the .md pass); `audit_`/`probe_`/
`sweep_` filename prefixes, matching the existing directory exclusion; and
`m_p-pin` out of `MASS_CONTEXT`, since there it names the q₀ anchor.

Locked in by `computations/canonical_mass_status_guard_test.py` — fixture-driven,
including the verbatim pre-fix `mass_table_comprehensive` docstring as the
must-stay-red control (a live-tree test would pass by construction).

**Remaining, deliberately not done:**

- **CI wiring.** No workflow runs this guard, and repo CI auto-triggers are
  disabled (AGENTS.md), so there is nowhere to wire it right now.
- **`--strict` is 2 hits short**, both `docs/precision-goals.md` ("m_avg: 2.89 %
  bare", "+2.89% open gap"). Both are *correct*, carefully-qualified prose.
  Clearing them means loosening the .md pass — the guard's primary surface, and
  the one where the recurrence actually happened. Buying green that way is the
  wrong trade; it needs its own decision.

Separately, the triage turned up a live compute defect that no guard can see:
`qou-7loj` (the canonical mass table's nucleon rows are read out of the
deprecated Vol·ρ witness, +2.89 %).
