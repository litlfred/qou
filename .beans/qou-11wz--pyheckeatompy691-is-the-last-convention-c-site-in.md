---
# qou-11wz
title: pyhecke/atom.py:691 is the last convention-C site in the producer layer — and it reaches the mass table
status: todo
type: task
created_at: 2026-08-16T11:18:21Z
updated_at: 2026-08-16T11:18:21Z
---

Parent: qou-cdx1. Surfaced by qou-2ixd's producer-audit bucket split; left open
by qou-cdh2 and qou-cds2, both of which closed around it.

## The site

    tools/pyhecke/python/pyhecke/atom.py:691   z_mark = 1.0 / (q0 ** 0.5 + qi ** 0.5)
                                        :713   Vs = z_mark * a_arr[i] + b_arr[i]

Convention C, float64, live, inside `atom_per_generator_volumes(Z, N, ...)`.
It is in `pyhecke.atom` — a DIFFERENT module from `pyhecke.gram`, which is why
`intra_module_split_waivers` never covered it and why the blanket
"tools/pyhecke — unexplained" bucket hid it behind gram.py's three until the
audit's buckets were split.

After qou-cds2 migrated the gram mpmath path, this is the **only** actionable
convention-C site left in the producer layer: `convention-c-producer-audit.py`
reports `1 site / 1 file`, ACTIONABLE.

## Why it was not migrated with the rest — measured blast radius

Unlike the gram mpmath path (4 consumers, all probes/demos), this reaches
production. Live callers, excluding `_deprecated/`:

    computations/mass_table_comprehensive.py:337
    computations/brane_tower_isospin_diagnosis.py:177
    computations/li2q_fbor_expansion_probe.py:174
    computations/probes/adjacent_vs_full_probe.py:276,278,287

Live witnesses naming the path:

    computations/pyhecke-h3-vs-h3a-impact-comparison.witness.json
    computations/hecke-core-symbolic-migration.witness.json
    computations/vhat-per-crossing-chain.witness.json
    computations/p2-5-symbolic-q-audit.witness.json
    computations/rho-k-graded-atomic-mass.witness.json

And it reaches the SHIPPED package: `gram.py` exports the function in `__all__`
(:501) and falls back to this Python implementation (:888-891), which
`hecke_core.py:138` and the generated `qou-mass/src/qou_mass/_internal/hecke_core.py`
both import.

## Two gates before touching it

1. **The native/Python pair is the qou-j6il shape.** `gram.py:888-891` dispatches
   to `pyhecke_native` and falls back to this. qou-j6il was the trap where the
   installed .so returned `markov_z(q0) = 0.4993203341836945` (C) while its Rust
   source read D. Compare both implementations at q0 BEFORE migrating either, or
   you will migrate one arm of a pair and not know it.
2. **Order the cascade.** qou-eea0's lesson: producers read each other's
   witnesses, so a stale upstream propagates into a freshly-migrated downstream
   and the downstream output looks clean. Five live witnesses here, at least one
   (`rho-k-graded-atomic-mass`) in the mass chain.

## Why this needs sign-off rather than a hygiene pass

It moves mass-table numbers. The 2026-08-15 ruling makes D canonical, so the
DIRECTION is not in question — but the binding channel already got worse on
aggregate under D (mean |err| 37.39% -> 43.85%, recorded in the ruling audit as
the anti-fit discipline working as designed), and a mass-table movement should
be measured and reported deliberately, not arrive as a side effect.
