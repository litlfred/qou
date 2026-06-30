---
# j1hg
title: 'Integration: canonical watcher - over-count 3-input rollup'
status: todo
type: task
created_at: 2026-06-21T21:44:26Z
updated_at: 2026-06-21T21:44:26Z
---


## 2026-06-30 — audit refresh (canonical-watcher maintenance)
Re-ran `computations/audits/canonical_script_input_audit.py`. The committed
witness was STALE; the over-count backlog SHRANK since the 2026-06-22 triage:
  over_count_count        23 → 12   (11 of the 23 genuine cases resolved by
                                      sibling refactors / deprecation)
  canonical_3input_count  64 → 70
  vol_hyp_fitted_count   149 → 163
Refreshed `canonical-script-input-audit.witness.json` committed (pure static
regex — no mpmath/env-skew). Remaining 12 (atomic_mass_via_rho_k,
channel_product_mass, hecke_core_legacy, iterative_lp_dual_h6_deuteron,
per_knot_density_per_block_wiring, rho_k_h3a_{co_casimir,crystal,lp_dual,
refinement,wenzl_bridge}, …) are the OWNER-GATED value-changing refactor
(rewrite to m_n = m_p + Q_β + m_e, sequenced with the q₀-repin sweep z5vu) —
NOT a mechanical pass per docs/audits/2026-06-22-overcount-3input-triage.md.
