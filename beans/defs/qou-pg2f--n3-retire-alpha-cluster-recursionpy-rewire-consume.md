---
# qou-pg2f
title: 'N3 [Retire alpha_cluster_recursion.py & Rewire Consumers]: Excise Non-Lean 64 m_e G + Vol(7^2_1) Cluster Recursion & Wire Lean-Backed Simplicial/H_4 Compute'
status: todo
type: task
priority: high
created_at: 2026-11-19T09:36:33Z
updated_at: 2026-11-19T09:36:33Z
parent: qou-8ffl
---

Parent Epic: `qou-8ffl`. Coordinates with `qou-yd54` and depends on `N1` + `N2`.

## Scope (Lane N3 — Retire Dead-Exploratory `alpha_cluster_recursion.py` & Rewire Live Importers)

1. **Retire `computations/alpha/alpha_cluster_recursion.py`:**
   - `alpha-cluster-recursion.witness.json` was already deprecated to `fsh-guts/deprecated/computations/` in PR #554 (`dead-exploratory`), because `B(n alpha) = n * (2 m_e * 4 * 8G) + C(n, 2) * m_e * Vol(7^2_1)` relies on an unproved `magic-A` heuristic and an ad-hoc all-pairs Whitehead-link `Vol(7^2_1)` coupling (`O(N_alpha^2)` blowup and wrong `^8Be` bound sign).
   - Audit every live importer of `alpha_cluster_recursion.py` and `magic_A_formula.py` (`b_over_a_v5_unified.py`, `canonical_isotope_witness.py`, `mass_binding_dashboard.py`, `atlas_render_canonical_table.py`, etc.).
2. **Rewire Consumers to Lean-Backed Multi-Crossing Simplicial / `H_4(q_2t)` + GPMT Compute:**
   - Replace `alpha_cluster_recursion` imports with the `N1`/`N2` Lean-backed parameter-free `H_4(q_2t)` + GPMT + transfer-matrix Gröbner–Shirshov facade, move `alpha_cluster_recursion.py` out of active production paths, and verify `0` float64 and `0` broken witness dependencies.
