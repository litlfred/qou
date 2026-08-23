---
# qou-geqa
title: '24 producers on main cannot complete: 14 crash, 10 exceed 240s'
status: todo
type: task
created_at: 2026-08-23T20:16:11Z
updated_at: 2026-08-23T20:16:11Z
---



## What was measured

Found while running the substantive census (PR #5577): a git-baselined sweep of
all **152** producers behind self-stale witnesses. 128 completed. The other
**24 (16 %) could not run to completion at all** and were excluded from the rate.

This is a stronger defect class than a drifted number. A producer that cannot
run can never regenerate its witness, so that witness is frozen at whatever it
last emitted — and nothing in the corpus currently surfaces the condition. The
staleness audits read witnesses; they never execute producers.

## CRASHED (14) — non-zero exit

    computations/alpha_em_b2_bring_period_matrix_probe.py
    computations/hadron_knot_table.py
    computations/lepton_tower_probe_1_cinquefoil_muon.py
    computations/low_isotope_mass_table.py
    computations/per_irrep_pole_atom.py
    computations/probes/h6_deuteron_free_word_chi_lambda_probe.py
    computations/probes/pentagon_rt_torus_knot_higgs_probe.py
    computations/probes/per_knot_density_borromean_q_locality_probe.py
    computations/probes/qbeta_braid_nf_sdp_offset_probe.py
    computations/probes/qbeta_habiro_element_probe.py
    computations/probes/su4_1111_markov_trace_probe.py
    computations/qbeta/qbeta_habiro_phase5q_dn_refactorize.py
    computations/rho_k_h3a_refinement.py
    computations/substrate/lever1_habiro_element_fit.py

## TIMEOUT (10) — exceeded 240 s

    computations/atom_mass_derived.py
    computations/bar_pairing_binding_observable.py
    computations/binding_depth_stratified.py
    computations/chi_4he_binding_lossless.py
    computations/chi_at_q_inv_via_native_mpfr.py
    computations/delta_lambda_v_hat_z_transfer_phase5d_4.py
    computations/gram_transfer_quadratic.py
    computations/probes/ground_state_ordering_a3_probe.py
    computations/probes/ksel2id_sw_identification_probe.py
    computations/qbeta/qbeta_c4even_exact_sseries_probe.py

Timeout is a budget artifact, not necessarily a defect: some of these are
legitimately long-compute (`qou-mnrd` records one producer that ran two hours
without finishing). Re-run them with a real budget before calling any of them
broken. The 14 crashes are the actionable half.

## Next step

`computations/witness_producer_executes_audit.py` (on main via #4960) is the
right tool — it exists precisely for "can this producer still produce its
witness?". This bean hands it 14 concrete instances rather than a sweep to
discover them.

## Do not

Do not "fix" a crash by regenerating its witness in this container. Several of
these touch the q0 anchor machinery, and an environment-stamped regeneration is
how a container fingerprint gets written into the corpus — see the reverted
witnesses in #5333.
