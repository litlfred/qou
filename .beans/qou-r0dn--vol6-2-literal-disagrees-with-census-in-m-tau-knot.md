---
# qou-r0dn
title: Vol(6_2) literal disagrees with census in m_tau_knot_prediction.py
status: todo
type: task
created_at: 2026-08-21T15:03:20Z
updated_at: 2026-08-21T15:03:20Z
---

computations/m_tau_knot_prediction.py:91 carries `"6_2": "4.0597664956578801590"` in KNOT_VOL_TABLE. The canonical census value (computations/substrate/knot_volumes.py:144, SnapPy HP 50-dps) is 4.40083251612304610144... The literal is 7.75% low and agrees to 8 digits with 2*Vol(4_1) = 4.05976642..., suggesting a doubled-figure-eight substitution. Separate from the knot-identity question in qou-e5jf; this is a wrong number under a right name.

Also note computations/vol_density_deuteron_perknot_probe.py:39 carries 4.40083298054544839393, which diverges from the census value at the 8th significant digit.

Found while adjudicating qou-e5jf (PR #5350).
