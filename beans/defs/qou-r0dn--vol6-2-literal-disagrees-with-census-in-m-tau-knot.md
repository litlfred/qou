---
# qou-r0dn
title: Vol(6_2) literal disagrees with census in m_tau_knot_prediction.py
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T15:03:20Z
updated_at: 2026-11-16T19:28:00Z
parent: qou-2002
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

## 2026-11-16 — Vol(6_2) Census Agreement & Volume Scaling Verified (PR #8169)

- **Lean 4 formalization** (`folio/quantum-observable-universe/lean/QOU/MassTheory/PlancherelNormalisationAndScaleBounds.lean`, `0` `sorry`):
  - `perKnotMass_ratio_and_rel_err`: proves that in `m(K) = m_e · (Vol(K)/ℏ_q²) · tr_M(K)`, the prediction ratio equals `V_sub / V_true` and the relative substitution error equals `(V_sub - V_true) / V_true` independently of `(m_e, ℏ_q, tr_M)`.
- **50-dps AST & numerical audit** (`computations/probes/plancherel_normalisation_and_scale_bounds_probe.py`, PR `litlfred/qou#8169`, head `32d6039de208cfa3dab898932c88023a55ef3267`):
  - Confirms `KNOT_VOL_TABLE['6_2']` in `computations/m_tau_knot_prediction.py` (`4.4008325161230461014`, rel err `9.36e-21`) and `VOL_6_2` in `computations/vol_density_deuteron_perknot_probe.py` (`4.40083251612304610144120386564`, rel err `0.0`) both match the 50-dps SnapPy census, and records the exact `-7.750034%` and `+1.055306e-7` shifts of the retired literals.
