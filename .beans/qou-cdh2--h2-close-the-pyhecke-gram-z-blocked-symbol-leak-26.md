---
# qou-cdh2
title: 'H2 (hygiene): close the pyhecke.gram.z blocked-symbol leak — 13 re-exporters + 13 consumers'
status: todo
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-16T02:17:29Z
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


---

## ⚠ PREMISE CORRECTION (2026-08-16, `qou-cdh1`) — READ BEFORE STARTING

**The 26 sites in this bean are not a convention-C leak.** They import
`pyhecke.gram.z`, and `gram.py:175` reads `z = q0 ** 3 / (q0 ** 2 + 1)` —
**convention D**. They re-export the *canonical* value. Verified against source,
not against the registry.

This bean and the audit's §3.1 inherit the premise from the registry's
`blocked_migrations[0]` row ("gram.py::z stays C by design"), which was **stale
when the audit was written**: commit `6086572c4` (2026-08-15) migrated `z` to D
*and* deleted `G_INV` outright — explicitly "not a rename" (`gram.py:20,91,401`),
the inverse now taken on the quotient `H₃/rad`. That commit **precedes** the
audit's own commit `c8796c283`; `git show c8796c283:tools/pyhecke/python/pyhecke/gram.py`
already carries the D line. The row has since been moved to
`resolved_migrations`, where the full correction is recorded under
`premise_correction`.

**What the real leak is.** Two consumers, on the 50-dps mpmath path this bean
does not name — `z_mp()`, `tr_m_mp()`, `tr_m_mp_strings()`, `gram_matrix_mp()`
are all still C:

```
computations/atom_dual_q0_mpfr_demo.py:47                  gram.tr_m_mp_strings()
computations/probes/qbeta_braid_nf_sdp_offset_probe.py:127,232   _gram.tr_m_mp()
```

Note which way the risk runs: the **float64** path is correct and the
**NO-FLOAT64** path is not, so the more precise answer is the wrong-convention
one. `R10` reports this split as a warning (waived, `intra_module_split_waivers`).

**The inventory keyed on the symbol name `z`, so it enumerated 26 sites of a D
value and could not see 2 sites of a C value under a different name** — a detector is
blind to the shape it keys on.

**Suggested re-scope:** this tranche is *unblocked* (its stated blocker `qou-cds2`
names a repair that already shipped) and its target is the two mpmath consumers,
not the 26 `z` re-exporters.
