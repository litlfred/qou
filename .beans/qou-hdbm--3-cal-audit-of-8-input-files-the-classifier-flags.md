---
# qou-hdbm
title: '3-cal audit: of 8 INPUT files the classifier flags, 3 are genuine, 1 is a judgement call, 4 are false positives'
status: todo
type: task
created_at: 2026-08-30T07:19:16Z
updated_at: 2026-08-30T07:19:16Z
---


The alias/unpacking closures (ee596db88, 0060157d4) gave the AME roadmap an
INPUT class where it had reported zero. "NEVER route" is a strong claim, so
every flagged file was read rather than counted. The classifier is deliberately
conservative — it prefers a false INPUT to a missed one — and that is exactly
what the reading shows.

## GENUINE — the AME value is BUILT FROM, not compared against

  probes/binding_mayer_linked_cluster_probe.py:91
      b2   = AME["D"]                  # the measured deuteron binding
      pred = comb(A[k], 2) * b2        # predicts T/3He/4He from it
      ...  vs AME[k]
      Honestly labelled ("pure-pairwise prediction, b2 from deuteron"), and
      still an INPUT: one measurement is the model's two-body parameter.

  probe_volume_wedderburn_delta_lambda.py:202
      num   = sum(S[a] * (isotopes[a][2] / M_E_MEV) for a in isotopes)
      scale = num / den
      B_pred = M_E_MEV * scale * S[atom]
      The file says it itself: "for dimensionless rules, fit ONE global scale
      across ALL isotopes (least-squares on B/m_e) — labelled 1-param". A scale
      fitted to the measurement and multiplied back into a prediction of it.

  sweeps/low_isotope_binding_sweep.py:153
      B = n_α · B(⁴He) + C(n_α, 2) · c_αα
      The measured ⁴He binding is a building block of the prediction for every
      heavier α-chain nuclide, which are then compared against AME.

## JUDGEMENT — an identity, not a fit

  log_delta_full_mass_subtract.py:180
      B_pred = mp_full[atom] - Z * mp_full["p"] - N * mp_full["n"]
      Binding from atomic masses by subtraction. Formally the AME value is on
      the prediction side; physically this is the definition of binding energy,
      not a calibration. Whoever owns the 3-cal discipline should say which it
      counts as — the classifier cannot.

## FALSE POSITIVES — prediction and measurement merely sit together

  fr_pullback_k3_test.py:318          B_pred = mp.mpf(r["B_MeV"]) where r comes
                                      from compute_atom_binding_fr(); AME is
                                      only B_emp in the ratio below it.
  per_atom_rho_deviation.py:136       b_pred = rho_struct * M_E_MEV * vol_eff,
                                      and rho_struct is a structural INTEGER.
                                      AME enters only via rho_tru, a comparison.
  sweeps/paper_six_term_isotope_sweep.py:1044
                                      M_pred is built from E_0 and Hecke terms;
                                      the AME literals are the M_codata column
                                      the error is measured against.
  wedderburn_table_binding_recast.py:104
                                      `pred, obs = mp.mpf(mpred), mp.mpf(mobs)`
                                      — taint crossed the tuple. FIXED in the
                                      classifier; the file now routes as TARGET
                                      and is drained.

## What this means for the count

The headline "25 sites in 7 files, never route" is the conservative machine
answer and should stay that way — the classifier must not be tuned to agree
with this reading, because the reading is what the classifier is for. But
anyone planning work off the number should know the real 3-cal exposure is
three files, plus one that needs an owner's call.
