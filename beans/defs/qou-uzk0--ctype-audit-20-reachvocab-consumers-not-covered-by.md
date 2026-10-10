---
# qou-uzk0
title: 'ctype audit: 20 REACH+VOCAB consumers not covered by test_ctype_consumer_coverage'
status: completed
type: task
priority: normal
created_at: 2026-08-14T19:41:55Z
updated_at: 2026-08-14T20:07:06Z
parent: qou-1295
---

DONE. 43 files carrying a ctype literal triaged on two axes (reachable / private vocabulary). 20 reachable-with-vocabulary; 16 defects repaired across 3 commits on PR #5029.

Silent (4): spectral_coordinates_all_atoms (else: M=eye DELETED the interface, 199.44% on the affected generator), per_irrep_pole_atom (count + cemetery summary), build_atomic_braid_recipe_d_chain (false DERIVED breakdown, 4 prose sites + 1 structured field), hoefsmit_symbolic __main__ (latent).
Crashing (10): per_nucleon_shift_derivation (LIVE at import), canonical_tr_m_via_branching, rho_w_crystal_vertex_trace, ocneanu_cancellation_derivation, wenzl_a3_cross_check, wenzl_a3_combiner_end_to_end, wenzl_lr_convention_adapter (x2 sites), option_e_isospin_probe, light_isotope_sweep.
Inverted (1): habiro_coefficients_interpolate applied the COLOUR-WEIGHTED value under the colour-BLIND key.
Late (2, found by the new Part C): d_u_closed_form_proof (n_avg_inter identically 0), homflypt_operator_valued_probe.

STRUCTURAL FINDING: test_ctype_consumer_coverage Part B exempts any file importing canonical_braid_crossings. All 16 defects were in that exempted population -- the guard was blind to exactly the group it protects. Part C added.

d_for_ctype grew a keyword-only delta= for q-symbolic callers (taking the cached q0 delta in a symbolic module is a layer straddle).

Spun out: qou-nmva (recipe literals uncross-checked), qou-hy6q (qou-mass fork stale). qou-gdtb item 1 (representation) untouched and still open.
