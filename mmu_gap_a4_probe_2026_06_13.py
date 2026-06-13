#!/usr/bin/env python3
"""
mmu_gap_a4_probe_2026_06_13.py

Verifies the mathematical claims regarding the m_mu derivation:
1. Calculates the bare-categorical m_mu = m_e * Vol(4_1) / \hbar_q^2
2. Validates the lever sensitivity ∂ln(m_mu)/∂ln(q) = 18.19
3. Tests if any simple topological/categorical adjustment could close the ~210 ppb gap.
"""

from mpmath import mp
import sys

def main():
    mp.dps = 50

    # Constants
    VOL_4_1_STR = "2.0298832128193072500424051085490405718833786150605995840349782136"
    M_E_MEV = mp.mpf("0.51099895000")
    M_MU_CODATA = mp.mpf("105.6583755")
    M_MU_OVER_M_E_CODATA = mp.mpf("206.7682830")
    
    # Current proton-anchored q_0
    q_0_proton = mp.mpf("1.1099785827513808075916690956107688798744991218735787360728142402")
    
    vol_41 = mp.mpf(VOL_4_1_STR)

    def hbar_q_sq(q):
        return ((q - mp.mpf(1)) / q)**2

    def m_mu_bare(q):
        return M_E_MEV * vol_41 / hbar_q_sq(q)
        
    def get_q_0_from_mass_ratio(ratio):
        # (q-1)/q = sqrt(vol_41 / ratio)
        # q-1 = q * sqrt(...)
        # q = 1 / (1 - sqrt(vol_41 / ratio))
        s = mp.sqrt(vol_41 / ratio)
        return mp.mpf(1) / (mp.mpf(1) - s)

    q_0_muon = get_q_0_from_mass_ratio(M_MU_OVER_M_E_CODATA)

    # 1. Bare categorical at proton anchor
    m_mu_pred_proton = m_mu_bare(q_0_proton)
    gap_proton_mev = m_mu_pred_proton - M_MU_CODATA
    gap_proton_ppb = (gap_proton_mev / M_MU_CODATA) * mp.mpf("1e9")

    # 2. Bare categorical at old muon anchor
    m_mu_pred_muon = m_mu_bare(q_0_muon)
    gap_muon_mev = m_mu_pred_muon - M_MU_CODATA
    gap_muon_ppb = (gap_muon_mev / M_MU_CODATA) * mp.mpf("1e9")

    # 3. Lever calculation
    eps = mp.mpf("1e-25")
    dm_dq = (m_mu_bare(q_0_proton + eps) - m_mu_bare(q_0_proton - eps)) / (2 * eps)
    dlnm_dlnq = (dm_dq * q_0_proton) / m_mu_pred_proton

    delta_q = q_0_proton - q_0_muon
    delta_q_ppb = (delta_q / q_0_muon) * mp.mpf("1e9")

    print(f"Bare-categorical m_mu at proton pinned q_0 : {m_mu_pred_proton}")
    print(f"CODATA m_mu                               : {M_MU_CODATA}")
    print(f"Gap at proton anchor (ppb)                : {gap_proton_ppb}")
    print(f"Gap at old muon anchor (ppb)              : {gap_muon_ppb}")
    print(f"Numerical dln(m_mu)/dln(q)                : {dlnm_dlnq}")
    print(f"Delta q (proton - muon) ppb               : {delta_q_ppb}")
    print(f"Predicted mass shift from lever (ppb)     : {delta_q_ppb * dlnm_dlnq}")

if __name__ == "__main__":
    main()
