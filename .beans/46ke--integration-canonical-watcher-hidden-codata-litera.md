---
# 46ke
title: 'Integration: canonical watcher - hidden codata literals rollup (53 scripts)'
status: todo
type: task
created_at: 2026-06-21T21:44:26Z
updated_at: 2026-06-21T21:44:26Z
---


## 2026-06-22 — PR #2606 (branch claude/tender-wright-oyyyky)
Routed 3 high-value production scripts off hardcoded CODATA literals:
- meson_mass_from_hecke.py (7 literals → registry; output bit-identical)
- beta-decay-from-q.py (m_e/m_e_err → M_E_MEV/M_E_MEV_ERR; output unchanged)
- canonical_isotope_witness.py (u→MeV → new public U_MEV export; identical)
Added public U_MEV alias + __all__ entry to codata_constants.py.
Deferred: option_e_*/probe_*/delta_lambda_* probe tail (low value);
docstring/narrative-print false positives (canonical_tower, derive_m_n,
free-neutron-decay) left alone.

## 2026-06-23 — coordination (branch claude/cool-johnson-t1wveh)
Sibling branch `claude/codata-46ke-rollup-2026-06-22` is ACTIVELY
draining this bean (last seen: "batch 7 — ³He/D/T/⁴He AME binding
literals"). To avoid double-routing:
- Already routed by me (PR #2606, see above): meson + beta-decay +
  isotope-witness production scripts, plus the public U_MEV export.
- Owned by the sibling now: the AME-binding literal sweep
  (³He/D/T/⁴He and the rest of the AME batches).
- Remaining unclaimed tail: the `option_e_*/probe_*/delta_lambda_*`
  exploratory scripts (low value — diminishing returns).
Handing the remaining production sweep to the sibling; not picking up
further 46ke work from this branch to prevent collisions.
