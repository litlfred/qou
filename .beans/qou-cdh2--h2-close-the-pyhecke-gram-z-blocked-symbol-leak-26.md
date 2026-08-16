---
# qou-cdh2
title: 'H2 (hygiene): close the pyhecke.gram.z blocked-symbol leak — 13 re-exporters + 13 consumers'
status: todo
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-15T00:00:00Z
---

Parent: `qou-cdx1`. **Blocked on `qou-cds2`** — decide what `pyhecke.gram.z`
becomes before containing it.

## Measured (`scripts/convention-c-producer-audit.py`, AST-verified, 2026-08-15)

The registry exempts the convention-C `z` **inside its module**
(`tools/pyhecke/python/pyhecke/gram.py`). Nothing kept it there.

**13 modules re-export it; 13 further consumers import it from them.**

```
computations/confinement-operator-selection.py:30      -> _PG_Z
computations/gram-matrix-dual.py:40                    -> z
computations/h2o_angle_activeset_gb.py:40              -> z
computations/h2o_angle_gb_truncation_inverse.py:47     -> z
computations/h2o_bond_angle_magnitude_vsepr.py:61      -> z
computations/h2o_bond_angle_shift_phi1.py:70           -> z
computations/hecke_core_legacy.py:75                   -> z
computations/jet_knot_invariants.py:42                 -> z
computations/molecular-frobenius-lp.py:43              -> _PG_Z
computations/pn_alpha_lp_dual.py:60                    -> _PG_Z
computations/substrate/hecke_core.py:61                -> z
computations/vhat_per_crossing_chain.py:63             -> z
qou-mass/src/qou_mass/_internal/hecke_core.py:60       -> z
```

`--list` gives the 13 downstream consumers.

## Hazard

`qou-mass/src/qou_mass/_internal/` is **generated** by
`scripts/sync-qou-mass-vendor.py`. Never hand-edit it; it moves when
`computations/substrate/hecke_core.py` moves. Run `--check` after.

## Why hygiene

Containment only — the symbol's *value* does not change in this tranche. What
changes is that the registry exemption starts meaning what it says, so the
producer audit's "blocked by design" count stops understating reach.
