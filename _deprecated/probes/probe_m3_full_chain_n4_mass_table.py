"""

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
"""

import sys; sys.path.insert(0, '/home/user/qou/computations')
import json
from paper_six_term_isotope_sweep import assemble_per_derivation_weights, q_beta_for_source
from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION, M_D_MEV_VALIDATION, M_T_MEV_VALIDATION, M_HE3_MEV_VALIDATION, M_HE4_MEV_VALIDATION

M_CODATA = {
    "p": float(M_P_MEV_VALIDATION), "n": float(M_N_MEV_VALIDATION),
    "D": float(M_D_MEV_VALIDATION), "T": float(M_T_MEV_VALIDATION),
    "3He": float(M_HE3_MEV_VALIDATION), "4He": float(M_HE4_MEV_VALIDATION),
}

atoms = [("p",1,0), ("n",0,1), ("D",1,1), ("T",1,2), ("3He",2,1), ("4He",2,2)]

print(f"Q_β (codata):        {q_beta_for_source('codata'):.10f} MeV")
print(f"Q_β (form_a_cos):    {q_beta_for_source('form_a_cos'):.10f} MeV")
print(f"Q_β (full_chain_n4): {q_beta_for_source('full_chain_n4'):.10f} MeV")
print()
print(f"{'iso':>5} {'M_codata':>10} {'M_pred (n4)':>15} {'err %':>9} {'err_n4 ppm':>12} {'M_pred (cos)':>13} {'err_cos ppm':>12}")
print('-' * 90)

rows = []
for label, Z, N in atoms:
    r_n4 = assemble_per_derivation_weights(Z, N, q_beta_source="full_chain_n4")
    r_cos = assemble_per_derivation_weights(Z, N, q_beta_source="form_a_cos")
    M_codata = M_CODATA[label]
    M_pred_n4 = float(r_n4['M_predicted_MeV'])
    M_pred_cos = float(r_cos['M_predicted_MeV'])
    err_n4_pct = (M_pred_n4 - M_codata) / M_codata * 100
    err_n4_ppm = (M_pred_n4 - M_codata) / M_codata * 1e6
    err_cos_ppm = (M_pred_cos - M_codata) / M_codata * 1e6
    rows.append({'iso': label, 'err_n4_ppm': err_n4_ppm})
    print(f"  {label:>5} {M_codata:>10.6f} {M_pred_n4:>15.6f} {err_n4_pct:>+8.3f}% {err_n4_ppm:>+10.1f} {M_pred_cos:>13.6f} {err_cos_ppm:>+10.1f}")

mae_pct = sum(abs(r['err_n4_ppm']) for r in rows) / len(rows) / 1e4
print()
print(f'MAE (full_chain_n4): {mae_pct:.4f}%   ({mae_pct*1e4:.1f} ppm)')

# Save witness
with open('/home/user/qou/computations/m3-full-chain-n4-mass-table.witness.json', 'w') as f:
    json.dump({
        "computation": "m3-full-chain-n4-mass-table",
        "description": "Per-derivation mass table with full N=4 categorical Q_β chain (c_2 = b², c_3 = -2, c_4 = b²+1/2).",
        "Q_beta_n4_MeV": q_beta_for_source('full_chain_n4'),
        "Q_beta_codata_MeV": q_beta_for_source('codata'),
        "rows": rows,
        "mae_pct": mae_pct,
    }, f, indent=2)
print("Witness emitted.")
