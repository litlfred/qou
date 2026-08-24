---
# qou-dld9
title: 'GAP: 12 producers compare results against a q0 reference at the OTHER anchor (11 are the tr_m_q_hecke defect exactly)'
status: todo
type: task
priority: normal
created_at: 2026-08-24T21:42:27Z
updated_at: 2026-08-24T21:43:01Z
---

## Provenance: the generalization of a defect found and fixed in PR #5723

`tr_m_q_hecke_seminormal` resolves PROTON (undeclared ⇒ runtime default) while
its `REF_WITNESS` was the base-name `atomic-tr-m-mpfr-50dps.witness.json`, which
is `ideal_muon`. A proton-pinned twin sat beside it, unread. Measured:

    atom       vs MUON ref     vs PROTON ref
    proton      7.8403e-8       4.67e-51
    deuteron    1.5143e-7       1.86e-50
    helium-3    2.5171e-7       3.31e-51

The two routes agree EXACTLY. The entire "~1e-7 methodological discrepancy" that
producer had reported for its whole existence was the 11.5 ppb mu-p q0 gap,
amplified ~n-fold because tr_M is a product over ~n crossings. I initially wrote
that residual up as REAL STRUCTURE and retracted it (PR #5723).

**It is not a one-off.** `computations/audits/reference_anchor_straddle_audit.py`
(new, in #5723) reports **120 straddles** corpus-wide, of which:

    11 producers read atomic-tr-m-mpfr-50dps.witness.json (muon) at the proton pin
       -- the SAME defect, with the SAME twin available and unread
    12 producers total are fixable TODAY because an anchor-matched twin exists

The 12:

    atomic_mass_via_rho_k                    markov/markov_trace_axiomatic_multi_atom
    atomic_tr_m_helium4                      probes/rho_f_categorical_probe
    binding_K_direct                         rho_k_h3a_refinement
    canonical_tr_m_three_path_comparison     sigma_shell_from_beta_chain
    cross_check_trM_wenzl_lr_1ppb            sweeps/paper_six_term_isotope_sweep
    deltalambda/rho_k_h3a_residual_decomposition   tr_m_jones_markov_cross_check

`cross_check_trM_wenzl_lr_1ppb` is worth reading first: a 1-ppb cross-check
measuring against the wrong layer cannot mean what its name says.

## CANDIDATES, NOT CONFIRMED DEFECTS

Each of the 12 needs reading before it is called a defect. A producer may
deliberately want the muon reference; the audit cannot see intent, only the
mismatch. The three known-deliberate cases (`atomic_tr_m_mpfr_50dps`,
`markov_peel_atomic_witness`, and now `tr_m_q_hecke_seminormal`) are already
separated out by the audit because they NAME BOTH TWINS -- that is the
discriminator, not the mismatch alone.

## Why nobody saw it, and why that predicts more

The producer computed in float64, whose error was the SAME ORDER as the straddle.
A wrong answer sitting under a noise floor of its own size is invisible to every
check that reads the number. It became legible only once the arithmetic went
exact (#5714 measured the kernel at ~14 digits; #5723 drained three consumers).
So the population at risk is precisely the one that cannot be found by looking at
results -- which is the argument for the detector rather than for spot fixes.

## Measurement discipline note: the first count was 214 and was the wrong question

Two unrelated things both present as "producer pin != reference pin":

  (1) the producer reads `q-pinning-50-digit.witness.json` to OBTAIN q0 -- that
      string IS the muon anchor's definition, so it COMPUTES AT MUON while
      `resolve_q0_anchor` reports the proton default. A mislabel, the documented
      `qou-aj91` class (~85 producers), already being fixed on the stamping side
      by PR #5699. It swamped the result 200:1.
  (2) the producer computes at its own pin and COMPARES ITS RESULT against a
      reference at the other pin -- this bean.

Only (2) is the question here. Anchor-defining sources and audit tooling (which
read witnesses AS DATA TO INSPECT) are excluded by name in the script, with the
reasoning recorded there. Reporting 214 would have buried 12 actionable rows
under 200 belonging to someone else's fix.
