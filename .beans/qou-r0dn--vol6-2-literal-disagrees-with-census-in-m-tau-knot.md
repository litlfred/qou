---
# qou-r0dn
title: Vol(6_2) literal disagrees with census in m_tau_knot_prediction.py
status: todo
type: task
priority: normal
created_at: 2026-08-21T15:03:20Z
updated_at: 2026-08-21T15:30:44Z
---

computations/m_tau_knot_prediction.py:91 carries `"6_2": "4.0597664956578801590"` in KNOT_VOL_TABLE. The canonical census value (computations/substrate/knot_volumes.py:144, SnapPy HP 50-dps) is 4.40083251612304610144... The literal is 7.75% low and agrees to 8 digits with 2*Vol(4_1) = 4.05976642..., suggesting a doubled-figure-eight substitution. Separate from the knot-identity question in qou-e5jf; this is a wrong number under a right name.

Also note computations/vol_density_deuteron_perknot_probe.py:39 carries 4.40083298054544839393, which diverges from the census value at the 8th significant digit.

Found while adjudicating qou-e5jf (PR #5350).



SHARPENED (2026-08-21, second agent, re-verified from the tree):

The -7.75% disagreement with the census value is MEASURED and is what makes this bean actionable. Exact figures:

  literal (m_tau_knot_prediction.py:91)  4.059766495657880159
  census (substrate/knot_volumes.py:144) 4.40083251612304610144
  relative                               -7.75003 %

  probe literal (vol_density_deuteron_perknot_probe.py:39)  4.40083298054544839393
  relative to census                                        +1.05531e-7

The 'doubled figure-eight' reading is a HYPOTHESIS about provenance, not an identity, and should not be upgraded to one:

  2*Vol(4_1)   4.0597664256386145
  literal      4.059766495657880159
  difference   7.00193e-8   (relative 1.72471e-8)

The literal differs from 2*Vol(4_1) in the 9th significant figure. It agrees to 8 digits, which is suggestive of a substitution but does not establish one. Provenance: undetermined.
