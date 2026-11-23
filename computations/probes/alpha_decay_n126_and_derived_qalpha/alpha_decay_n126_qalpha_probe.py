#!/usr/bin/env python3
"""80-dps evaluation of zero-parameter Gamow-Gurney-Condon alpha-decay tunneling,
magic N=126 (210Po) cluster preformation (Mayer-Jensen seniority overlap vs
Perdew-Parr / Goeppert-Mayer shell-kink WKB attenuation), and internally derived
Q_alpha^{QOU} benchmark + Geiger-Nuttall Q-sensitivity.

Bean `qou-i2jl`. Pre-registered in `PREREGISTRATION.md` (commit `3004225fb9c`)
BEFORE evaluating any candidate N=126 preformation factor or derived Q_alpha^{QOU}
half-life against experiment.

Historical credits:
  - Hans Geiger & John Mitchell Nuttall (1911), Phil. Mag. 22, 613
  - George Gamow (1928), Z. Phys. 51, 204
  - Ronald W. Gurney & Edward U. Condon (1928), Nature 122, 439
  - Maria Goeppert Mayer (1949), Phys. Rev. 75, 1969
  - Otto Haxel, J. Hans D. Jensen & Hans E. Suess (1949), Phys. Rev. 75, 1766
  - John P. Perdew, Robert G. Parr, Mel Levy & Jose L. Balduz Jr. (1982),
    Phys. Rev. Lett. 49, 1691

Precision & anti-fit discipline:
  - `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - Form-B Bring-Schwinger `alpha_q` (`1/alpha_q = 137.035999127...`, ZERO CODATA alpha_EM),
  - CAL-1 `m_e`, CAL-3 `m_{pi+-} = 139.57039 MeV` (`r_pi = hbar*c/m_pi`, `r_0^{FCC}`),
  - zero `float64` imports, literals, or casts (`parse_float=str`), zero parameter fitting.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT / "tools" / "qou-substrate" / "python") not in sys.path:
    sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
if str(_ROOT / "computations") not in sys.path:
    sys.path.insert(0, str(_ROOT / "computations"))

import mpmath as mp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)

AME_JSON_PATH = _ROOT / "computations" / "data" / "ame2020.json"
M_PI_CHARGED_MEV = mp.mpf("139.57039")

# Ground-state experimental alpha-emitter half-lives from NUBASE2020
# (F. G. Kondev et al., Chinese Phys. C 45, 030001 (2021)), stored as exact
# decimal string factors (value_str, unit_seconds_str, label).
NUBASE2020_ALPHA_EMITTERS: list[tuple[str, int, int, str, str, str]] = [
    ("8Be", 4, 8, "81.9e-18", "1", "81.9 as (resonance)"),
    ("212Po", 84, 212, "294.4e-9", "1", "294.4 ns (open shell, N=128)"),
    ("214Po", 84, 214, "163.6e-6", "1", "163.6 us (open shell, N=130)"),
    ("222Rn", 86, 222, "3.8215", "86400", "3.8215 d (open shell, N=136)"),
    ("210Po", 84, 210, "138.3763", "86400", "138.3763 d (magic N=126)"),
    ("226Ra", 88, 226, "1600", "31557600", "1600 y (open shell, N=138)"),
    ("238U", 92, 238, "4.468e9", "31557600", "4.468 Gy (open shell, N=146)"),
]


def solve_form_b_alpha_inv(q_val: mp.mpf) -> mp.mpf:
    """Solve QOU Form-B Bring-Schwinger cubic for `alpha_EM^{-1}(q)` at 85 dps."""
    with mp.workdps(85):
        q = mp.mpf(q_val)
        one = mp.mpf(1)
        h = q - one / q
        h2 = h * h
        two_q = q + one / q
        q9 = (q ** 9 - q ** (-9)) / h
        q10 = (q ** 10 - q ** (-10)) / h
        t_term = q * q9 * q10 + mp.mpf(2) / (mp.mpf(3) * mp.pi)
        h_term = two_q / (mp.mpf(8) * mp.pi)
        a = (-t_term + mp.sqrt(t_term * t_term + mp.mpf(4) * h_term)) / (
            mp.mpf(2) * h_term
        )
        for _ in range(35):
            fa = -h_term * h2 * (a ** 3) + h_term * (a ** 2) + t_term * a - one
            dfa = (
                -mp.mpf(3) * h_term * h2 * (a ** 2)
                + mp.mpf(2) * h_term * a
                + t_term
            )
            da = fa / dfa
            a -= da
            if abs(da) < mp.mpf(10) ** (-80):
                break
        return one / a


def load_ame2020_by_za(path: Path) -> dict[tuple[int, int], dict[str, str]]:
    """Load AME2020 entries with `parse_float=str` so zero Python floats are built."""
    raw = json.loads(path.read_text(encoding="utf-8"), parse_float=str)
    by_za: dict[tuple[int, int], dict[str, str]] = {}
    for entry in raw["entries"]:
        z_val = int(entry["Z"])
        a_val = int(entry["A"])
        by_za[(z_val, a_val)] = {
            "element": str(entry["element"]),
            "mass_excess_keV": str(entry["mass_excess_keV"]),
            "binding_energy_total_keV": str(entry["binding_energy_total_keV"]),
        }
    return by_za


def gamow_wkb_half_life_s(
    z_d: int,
    a_d: int,
    q_alpha_mev: mp.mpf,
    mu_mev: mp.mpf,
    r0_fcc_fm: mp.mpf,
    alpha_q: mp.mpf,
    hbar_c_mev_fm: mp.mpf,
    c_fm_s: mp.mpf,
) -> dict[str, mp.mpf] | None:
    """Compute zero-parameter Gamow-Gurney-Condon WKB half-life (if sub-barrier)."""
    one = mp.mpf(1)
    two = mp.mpf(2)
    four = mp.mpf(4)
    if q_alpha_mev <= mp.mpf(0):
        return None
    r_touch_fm = r0_fcc_fm * (mp.cbrt(mp.mpf(a_d)) + mp.cbrt(four))
    r_turn_fm = two * mp.mpf(z_d) * alpha_q * hbar_c_mev_fm / q_alpha_mev
    x_ratio = r_touch_fm / r_turn_fm
    if x_ratio >= one:
        return None
    g_exp = (
        (mp.sqrt(two * mu_mev * q_alpha_mev) / hbar_c_mev_fm)
        * r_turn_fm
        * (mp.acos(mp.sqrt(x_ratio)) - mp.sqrt(x_ratio * (one - x_ratio)))
    )
    v_rel_fm_s = mp.sqrt(two * q_alpha_mev / mu_mev) * c_fm_s
    nu_assault_hz = v_rel_fm_s / (two * r_touch_fm)
    t_half_s = (mp.log(two) / nu_assault_hz) * mp.exp(two * g_exp)
    return {
        "R_touch_fm": r_touch_fm,
        "R_turn_fm": r_turn_fm,
        "x_ratio": x_ratio,
        "two_G": two * g_exp,
        "nu_assault_Hz": nu_assault_hz,
        "T_half_s": t_half_s,
    }


def log10_t_sensitivity_dex_per_mev(
    z_d: int,
    a_d: int,
    q_alpha_mev: mp.mpf,
    mu_mev: mp.mpf,
    r0_fcc_fm: mp.mpf,
    alpha_q: mp.mpf,
    hbar_c_mev_fm: mp.mpf,
    c_fm_s: mp.mpf,
) -> mp.mpf:
    """Exact derivative d(log10 T_{1/2}^{WKB}) / dQ_alpha [dex / MeV] via 80-dps central step."""
    eps = mp.mpf("1e-25")
    hi = gamow_wkb_half_life_s(
        z_d, a_d, q_alpha_mev + eps, mu_mev, r0_fcc_fm, alpha_q, hbar_c_mev_fm, c_fm_s
    )
    lo = gamow_wkb_half_life_s(
        z_d, a_d, q_alpha_mev - eps, mu_mev, r0_fcc_fm, alpha_q, hbar_c_mev_fm, c_fm_s
    )
    assert hi is not None and lo is not None
    return (mp.log10(hi["T_half_s"]) - mp.log10(lo["T_half_s"])) / (mp.mpf(2) * eps)


def qou_periodic_table_bindings_mev(
    z: int,
    n: int,
    q0: mp.mpf,
    e0_mev: mp.mpf,
    alpha_q: mp.mpf,
    hbar_c_mev_fm: mp.mpf,
    r_pi_fm: mp.mpf,
    r0_fcc_fm: mp.mpf,
) -> dict[str, mp.mpf]:
    """Evaluate all three pre-registered zero-parameter QOU heavy-nucleus binding forms:
      - H1: L4_qclt_periodic_table (`canonical_isotope_witness.py`: A-1 chain + CAL-3 Coulomb)
      - H2_std: 3D FCC k=12 + (111) facet surface deficit + STANDARD_MAP TL bonds - FCC Coulomb
      - H2_pauli: 3D FCC k=12 + (111) facet surface deficit + PAULI_MAP (pn-only) TL bonds - FCC Coulomb
    """
    one = mp.mpf(1)
    two = mp.mpf(2)
    three = mp.mpf(3)
    five = mp.mpf(5)
    a = z + n
    a_mp = mp.mpf(a)
    z_mp = mp.mpf(z)
    n_mp = mp.mpf(n)

    # Convention-D Hecke standard-channel values (`channel_binding.py`)
    h0 = q0 - one / q0
    z_d = (q0 ** 3) / (q0 * q0 + one)
    f_pp_std = z_d
    f_pn_std = z_d - h0 / two
    f_nn_std = z_d - h0

    l_pp = mp.log(one / f_pp_std)
    l_pn = mp.log(one / f_pn_std)
    l_nn = mp.log(one / f_nn_std)

    n_pp = z_mp * (z_mp - one) / two
    n_pn = z_mp * n_mp
    n_nn = n_mp * (n_mp - one) / two
    n_tot = a_mp * (a_mp - one) / two

    mean_l_std = (n_pp * l_pp + n_pn * l_pn + n_nn * l_nn) / n_tot
    frac_pn = n_pn / n_tot

    # H1: L4_qclt (`canonical_isotope_witness.py`: (A - 1) strong minus CAL-3 r_pi Coulomb)
    b_strong_l4 = e0_mev * (a_mp - one) * mean_l_std
    ec_cal3 = (three / five) * z_mp * (z_mp - one) * alpha_q * hbar_c_mev_fm / (
        r_pi_fm * mp.cbrt(a_mp)
    )
    b_h1_l4 = b_strong_l4 - ec_cal3

    # H2: 3D FCC k = 12 interior, (111) facet k' = 9, c = 3 -> M_FCC(A) = 6 A - (9/2) A^{2/3}
    # (`coordination_surface_deficit_probe.py`: a_S / a_V = 3 * (1 - 9/12) = 3/4)
    m_fcc_contacts = mp.mpf(6) * a_mp - (mp.mpf(9) / two) * (a_mp ** (two / three))
    ec_fcc = (three / five) * z_mp * (z_mp - one) * alpha_q * hbar_c_mev_fm / (
        r0_fcc_fm * mp.cbrt(a_mp)
    )

    b_h2_fcc_std = e0_mev * m_fcc_contacts * mean_l_std - ec_fcc
    b_h2_fcc_pauli = e0_mev * m_fcc_contacts * frac_pn * l_pn - ec_fcc

    return {
        "H1_L4_qclt_MeV": b_h1_l4,
        "H2_FCC_k12_std_MeV": b_h2_fcc_std,
        "H2_FCC_k12_pauli_MeV": b_h2_fcc_pauli,
    }


def main() -> int:
    with mp.workdps(WORK_DPS):
        q0 = q_at(dps=WORK_DPS)
        one = mp.mpf(1)
        two = mp.mpf(2)
        three = mp.mpf(3)
        four = mp.mpf(4)

        h_j_s = codata("Planck constant").value
        hbar_j_s = h_j_s / (two * mp.pi)
        c_m_s = codata("speed of light in vacuum").value
        e_c = codata("elementary charge").value
        hbar_c_mev_fm = (hbar_j_s * c_m_s / (e_c * mp.mpf("1e6"))) * mp.mpf("1e15")
        c_fm_s = c_m_s * mp.mpf("1e15")

        m_e_mev = codata("electron mass energy equivalent in mev").value
        m_p_mev = codata("proton mass energy equivalent in mev").value
        m_n_mev = codata("neutron mass energy equivalent in mev").value
        u_mev = codata("atomic mass constant energy equivalent in mev").value

        alpha_q_inv = solve_form_b_alpha_inv(q0)
        alpha_q = one / alpha_q_inv
        hbar_q = one - one / q0
        e0_mev = m_e_mev / (q0 * (q0 - one))
        eosc_mev = m_e_mev / ((q0 - one) ** 2)

        r_pi_fm = hbar_c_mev_fm / M_PI_CHARGED_MEV
        l_bond_fm = (three / two) * r_pi_fm
        r0_fcc_fm = mp.cbrt(three / (four * mp.pi * mp.sqrt(two))) * l_bond_fm

        # Zero-parameter 4He magic-A binding B_alpha^{QOU} = 2 * m_e * 4 * 8G = 64 m_e G
        b_alpha_qou_mev = mp.mpf(64) * m_e_mev * mp.catalan

        ame_by_za = load_ame2020_by_za(AME_JSON_PATH)
        ea_entry = ame_by_za[(2, 4)]
        b_alpha_ame_mev = mp.mpf(ea_entry["binding_energy_total_keV"]) * mp.mpf("1e-3")
        delta_alpha_mev = mp.mpf(ea_entry["mass_excess_keV"]) * mp.mpf("1e-3")
        m_alpha_nuc_mev = four * u_mev + delta_alpha_mev - two * m_e_mev

        # ── Part A: Baseline Open-Shell vs Magic N=126 WKB Benchmark ──────────
        baseline_rows: list[dict[str, str]] = []
        open_heavy_abs_dex_unscreened: list[mp.mpf] = []
        open_heavy_abs_dex_screened: list[mp.mpf] = []
        po210_wkb_s = mp.mpf(0)
        po210_exp_s = mp.mpf(0)
        po210_s_alpha_emp = mp.mpf(0)
        po210_mu_alpha_d_mev = mp.mpf(0)
        u238_q0_ext_abs_dex = mp.mpf(0)
        u238_q0_vs_q1_shift_dex = mp.mpf(0)

        for name, z_p, a_p, hl_val_str, hl_unit_str, note in NUBASE2020_ALPHA_EMITTERS:
            z_d = z_p - 2
            a_d = a_p - 4
            ep = ame_by_za[(z_p, a_p)]
            ed = ame_by_za[(z_d, a_d)]

            # Exact Q_alpha identity check: mass excesses vs binding energies
            q_from_me = (
                mp.mpf(ep["mass_excess_keV"])
                - mp.mpf(ed["mass_excess_keV"])
                - mp.mpf(ea_entry["mass_excess_keV"])
            ) * mp.mpf("1e-3")
            q_from_b = (
                mp.mpf(ed["binding_energy_total_keV"])
                + mp.mpf(ea_entry["binding_energy_total_keV"])
                - mp.mpf(ep["binding_energy_total_keV"])
            ) * mp.mpf("1e-3")
            # AME2020 stores rounded keV strings; they agree to < 2e-5 MeV
            assert abs(q_from_me - q_from_b) < mp.mpf("5e-5")
            q_exp_mev = q_from_me

            z_mpf = mp.mpf(z_p)
            de_screen_mev = (
                mp.mpf("65.3") * (z_mpf ** (mp.mpf(7) / mp.mpf(5)))
                - mp.mpf(80) * (z_mpf ** (mp.mpf(2) / mp.mpf(5)))
            ) * mp.mpf("1e-6")
            q_scr_mev = q_exp_mev + de_screen_mev if z_p >= 80 else q_exp_mev

            m_d_nuc_mev = (
                mp.mpf(a_d) * u_mev
                + mp.mpf(ed["mass_excess_keV"]) * mp.mpf("1e-3")
                - mp.mpf(z_d) * m_e_mev
            )
            mu_mev = (m_d_nuc_mev * m_alpha_nuc_mev) / (m_d_nuc_mev + m_alpha_nuc_mev)

            wkb_unscr = gamow_wkb_half_life_s(
                z_d, a_d, q_exp_mev, mu_mev, r0_fcc_fm, alpha_q, hbar_c_mev_fm, c_fm_s
            )
            wkb_scr = gamow_wkb_half_life_s(
                z_d, a_d, q_scr_mev, mu_mev, r0_fcc_fm, alpha_q, hbar_c_mev_fm, c_fm_s
            )
            assert wkb_unscr is not None and wkb_scr is not None

            t_exp_s = mp.mpf(hl_val_str) * mp.mpf(hl_unit_str)
            dex_err = mp.log10(wkb_unscr["T_half_s"] / t_exp_s)
            dex_scr_err = mp.log10(wkb_scr["T_half_s"] / t_exp_s)
            s_alpha = wkb_unscr["T_half_s"] / t_exp_s

            if z_p >= 80 and name != "210Po":
                open_heavy_abs_dex_unscreened.append(abs(dex_err))
                open_heavy_abs_dex_screened.append(abs(dex_scr_err))
            if name == "210Po":
                po210_wkb_s = wkb_unscr["T_half_s"]
                po210_exp_s = t_exp_s
                po210_s_alpha_emp = s_alpha
                po210_mu_alpha_d_mev = mu_mev
            if name == "238U":
                t_ext_q0_s = (mp.log(two) / wkb_unscr["nu_assault_Hz"]) * mp.exp(
                    wkb_unscr["two_G"] / q0
                )
                u238_q0_vs_q1_shift_dex = mp.log10(t_ext_q0_s / wkb_unscr["T_half_s"])
                u238_q0_ext_abs_dex = abs(mp.log10(t_ext_q0_s / t_exp_s))

            baseline_rows.append(
                {
                    "nuclide": name,
                    "Z": str(z_p),
                    "N": str(a_p - z_p),
                    "A": str(a_p),
                    "regime": note,
                    "Q_alpha_AME_MeV": fmt(q_exp_mev, dps=20),
                    "R_touch_FCC_fm": fmt(wkb_unscr["R_touch_fm"], dps=20),
                    "R_turn_fm": fmt(wkb_unscr["R_turn_fm"], dps=20),
                    "two_G_WKB": fmt(wkb_unscr["two_G"], dps=20),
                    "T_half_exp_s": fmt(t_exp_s, dps=15),
                    "T_half_WKB_s": fmt(wkb_unscr["T_half_s"], dps=15),
                    "log10_T_WKB_over_T_exp_dex": fmt(dex_err, dps=12),
                    "log10_T_WKB_screened_over_T_exp_dex": fmt(dex_scr_err, dps=12),
                    "S_alpha_empirical": fmt(s_alpha, dps=15),
                }
            )

        # ── Part B: Pre-Registered Zero-Parameter N=126 Preformation Mechanisms ─
        # Mechanism B1: Mayer-Jensen seniority / pair-degeneracy overlaps
        # 210Po: pi(1h_{9/2})^2 (2j_p + 1 = 10) x nu(3p_{1/2})^{-2} (2j_{n,<} + 1 = 2)
        # 212Po: pi(1h_{9/2})^2 (2j_p + 1 = 10) x nu(2g_{9/2})^2   (2j_{n,>} + 1 = 10)
        deg_p_1h9_2 = mp.mpf(10)
        deg_n_3p1_2 = mp.mpf(2)
        deg_n_2g9_2 = mp.mpf(10)

        s_mj_proton = one / deg_p_1h9_2  # 1/10 = 0.1
        s_mj_neutron_ratio = deg_n_3p1_2 / deg_n_2g9_2  # 2/10 = 0.2
        s_mj_joint = one / (deg_p_1h9_2 * deg_n_3p1_2)  # 1/20 = 0.05

        po210_t_mj_joint_s = po210_wkb_s / s_mj_joint
        po210_mj_joint_dex_err = mp.log10(po210_t_mj_joint_s / po210_exp_s)
        s_mj_joint_dex_diff = mp.log10(s_mj_joint / po210_s_alpha_emp)

        # Mechanism B2: Perdew-Parr / Goeppert-Mayer shell-kink internal WKB attenuation
        # across CAL-3 pion-Compton cluster formation length r_pi = hbar*c / m_{pi+-}
        hbar_omega_210_mev = eosc_mev / mp.cbrt(mp.mpf(210))
        gap_g1_ho_mev = hbar_omega_210_mev
        gap_g2_so_qou_mev = mp.mpf(13) * hbar_q * hbar_omega_210_mev  # l=6 1i_{13/2}: 2l+1 = 13

        # Empirical Perdew-Parr S_{2n} jump across N=126 in Po (Z=84):
        # S_{2n}(84,126) = B(210Po) - B(208Po), S_{2n}(84,128) = B(212Po) - B(210Po)
        b_208po = mp.mpf(ame_by_za[(84, 208)]["binding_energy_total_keV"]) * mp.mpf("1e-3")
        b_210po = mp.mpf(ame_by_za[(84, 210)]["binding_energy_total_keV"]) * mp.mpf("1e-3")
        b_212po = mp.mpf(ame_by_za[(84, 212)]["binding_energy_total_keV"]) * mp.mpf("1e-3")
        s2n_126_mev = b_210po - b_208po
        s2n_128_mev = b_212po - b_210po
        gap_g3_perdew_parr_ame_mev = s2n_126_mev - s2n_128_mev

        # Internal reduced masses M1 (intra-alpha 2n-2p pair) and M2 (alpha-206Pb)
        mu_m1_2n_2p_mev = (two * m_n_mev * two * m_p_mev) / (two * m_n_mev + two * m_p_mev)
        mu_m2_alpha_d_mev = po210_mu_alpha_d_mev

        gaps_dict = {
            "G1_QOU_HO_1quantum": gap_g1_ho_mev,
            "G2_QOU_MJ_1i13_2_spin_orbit": gap_g2_so_qou_mev,
            "G3_AME2020_Perdew_Parr_S2n_kink": gap_g3_perdew_parr_ame_mev,
        }
        mus_dict = {
            "M1_intra_alpha_2n_2p": mu_m1_2n_2p_mev,
            "M2_alpha_206Pb": mu_m2_alpha_d_mev,
        }

        kink_wkb_grid: dict[str, dict[str, str]] = {}
        for g_key, g_val in gaps_dict.items():
            for m_key, m_val in mus_dict.items():
                cell_key = f"{g_key}__{m_key}"
                two_k_rpi = two * mp.sqrt(two * m_val * g_val) * r_pi_fm / hbar_c_mev_fm
                s_kink = mp.exp(-two_k_rpi)
                t_corr_s = po210_wkb_s / s_kink
                kink_wkb_grid[cell_key] = {
                    "Delta_shell_MeV": fmt(g_val, dps=20),
                    "mu_int_MeV": fmt(m_val, dps=20),
                    "two_kappa_r_pi": fmt(two_k_rpi, dps=20),
                    "S_alpha_kink": fmt(s_kink, dps=20),
                    "log10_S_kink_over_S_emp_dex": fmt(mp.log10(s_kink / po210_s_alpha_emp), dps=12),
                    "T_half_corrected_s": fmt(t_corr_s, dps=15),
                    "log10_T_corr_over_T_exp_dex": fmt(mp.log10(t_corr_s / po210_exp_s), dps=12),
                }

        # ── Part C: Derived Q_alpha^{QOU} vs Q_alpha^{AME} & Sensitivity ──────
        derived_qalpha_rows: list[dict[str, object]] = []
        for name, z_p, a_p, hl_val_str, hl_unit_str, note in NUBASE2020_ALPHA_EMITTERS:
            if z_p < 80:
                continue
            n_p = a_p - z_p
            z_d = z_p - 2
            n_d = n_p - 2
            a_d = a_p - 4
            ep = ame_by_za[(z_p, a_p)]
            ed = ame_by_za[(z_d, a_d)]
            q_exp_mev = (
                mp.mpf(ep["mass_excess_keV"])
                - mp.mpf(ed["mass_excess_keV"])
                - mp.mpf(ea_entry["mass_excess_keV"])
            ) * mp.mpf("1e-3")
            m_d_nuc_mev = (
                mp.mpf(a_d) * u_mev
                + mp.mpf(ed["mass_excess_keV"]) * mp.mpf("1e-3")
                - mp.mpf(z_d) * m_e_mev
            )
            mu_mev = (m_d_nuc_mev * m_alpha_nuc_mev) / (m_d_nuc_mev + m_alpha_nuc_mev)
            t_exp_s = mp.mpf(hl_val_str) * mp.mpf(hl_unit_str)

            sens_dex_per_mev = log10_t_sensitivity_dex_per_mev(
                z_d, a_d, q_exp_mev, mu_mev, r0_fcc_fm, alpha_q, hbar_c_mev_fm, c_fm_s
            )

            bp = qou_periodic_table_bindings_mev(
                z_p, n_p, q0, e0_mev, alpha_q, hbar_c_mev_fm, r_pi_fm, r0_fcc_fm
            )
            bd = qou_periodic_table_bindings_mev(
                z_d, n_d, q0, e0_mev, alpha_q, hbar_c_mev_fm, r_pi_fm, r0_fcc_fm
            )

            models_eval: dict[str, dict[str, str | bool | None]] = {}
            for m_label, b_key in (
                ("H1_L4_qclt", "H1_L4_qclt_MeV"),
                ("H2_FCC_k12_std", "H2_FCC_k12_std_MeV"),
                ("H2_FCC_k12_pauli", "H2_FCC_k12_pauli_MeV"),
            ):
                q_pred_mev = bd[b_key] + b_alpha_qou_mev - bp[b_key]
                dq_mev = q_pred_mev - q_exp_mev
                wkb_pred = gamow_wkb_half_life_s(
                    z_d, a_d, q_pred_mev, mu_mev, r0_fcc_fm, alpha_q, hbar_c_mev_fm, c_fm_s
                )
                if wkb_pred is not None:
                    t_pred_str = fmt(wkb_pred["T_half_s"], dps=15)
                    dex_vs_exp_str = fmt(mp.log10(wkb_pred["T_half_s"] / t_exp_s), dps=12)
                    subbarrier = True
                else:
                    t_pred_str = None
                    dex_vs_exp_str = None
                    subbarrier = False
                models_eval[m_label] = {
                    "B_parent_QOU_MeV": fmt(bp[b_key], dps=15),
                    "B_daughter_QOU_MeV": fmt(bd[b_key], dps=15),
                    "Q_alpha_QOU_MeV": fmt(q_pred_mev, dps=15),
                    "delta_Q_alpha_MeV": fmt(dq_mev, dps=15),
                    "linearised_delta_log10_T_dex": fmt(sens_dex_per_mev * dq_mev, dps=12),
                    "subbarrier_tunneling_regime": subbarrier,
                    "T_half_WKB_at_Q_QOU_s": t_pred_str,
                    "log10_T_QOU_over_T_exp_dex": dex_vs_exp_str,
                }

            derived_qalpha_rows.append(
                {
                    "nuclide": name,
                    "Z": str(z_p),
                    "N": str(n_p),
                    "A": str(a_p),
                    "Q_alpha_AME_MeV": fmt(q_exp_mev, dps=15),
                    "B_parent_AME_MeV": fmt(
                        mp.mpf(ep["binding_energy_total_keV"]) * mp.mpf("1e-3"), dps=15
                    ),
                    "B_daughter_AME_MeV": fmt(
                        mp.mpf(ed["binding_energy_total_keV"]) * mp.mpf("1e-3"), dps=15
                    ),
                    "d_log10_T_d_Qalpha_dex_per_MeV": fmt(sens_dex_per_mev, dps=15),
                    "models": models_eval,
                }
            )

        # Print transparent 80-dps summary
        print("=== qou-i2jl: Alpha-Decay, N=126 S_alpha Preformation & Derived Q_alpha (80 dps) ===")
        print(f"  q0 (proton pin)          = {fmt(q0, dps=30)}")
        print(f"  1/alpha_q (Form B)       = {fmt(alpha_q_inv, dps=20)}")
        print(f"  r_pi (CAL-3) [fm]        = {fmt(r_pi_fm, dps=20)}")
        print(f"  r0_FCC [fm]              = {fmt(r0_fcc_fm, dps=20)}")
        print(f"  E0(q0) / E_osc(q0) [MeV] = {fmt(e0_mev, dps=12)} / {fmt(eosc_mev, dps=12)}")
        print(f"  B_alpha QOU vs AME [MeV] = {fmt(b_alpha_qou_mev, dps=12)} vs {fmt(b_alpha_ame_mev, dps=12)}")
        print(
            f"  Open-shell heavy |dex|   = [{fmt(min(open_heavy_abs_dex_unscreened), dps=6)}, "
            f"{fmt(max(open_heavy_abs_dex_unscreened), dps=6)}] unscreened"
        )
        print(f"  210Po empirical S_alpha  = {fmt(po210_s_alpha_emp, dps=12)}")
        print()
        print("  -- Mechanism B1 (Mayer-Jensen combinatorial seniority / pair overlaps) --")
        print(f"    S_MJ^(pi)      1h_9/2^2          = {fmt(s_mj_proton, dps=10)}")
        print(f"    S_MJ^(nu-rat)  3p_1/2 / 2g_9/2   = {fmt(s_mj_neutron_ratio, dps=10)}")
        print(
            f"    S_MJ^(pi*nu)   1/(10*2) = 1/20   = {fmt(s_mj_joint, dps=10)} "
            f"(dex diff vs emp = {fmt(s_mj_joint_dex_diff, dps=6)}, "
            f"210Po T_1/2 err = {fmt(po210_mj_joint_dex_err, dps=6)} dex)"
        )
        print()
        print("  -- Mechanism B2 (Perdew-Parr / Goeppert-Mayer shell-kink WKB across r_pi) --")
        print(f"    hbar*omega_QOU(210)              = {fmt(hbar_omega_210_mev, dps=10)} MeV")
        print(f"    G2 QOU 1i_13/2 spin-orbit        = {fmt(gap_g2_so_qou_mev, dps=10)} MeV")
        print(f"    G3 AME2020 S_2n(126)-S_2n(128)   = {fmt(gap_g3_perdew_parr_ame_mev, dps=10)} MeV")
        for cell_key, cell in kink_wkb_grid.items():
            print(
                f"    {cell_key:<54} S_kink = {cell['S_alpha_kink'][:12]:<12} "
                f"dex_err(S) = {cell['log10_S_kink_over_S_emp_dex']}"
            )
        print()
        print("  -- Part C: Internally Derived Q_alpha^{QOU} vs AME2020 & Sensitivity --")
        for row in derived_qalpha_rows:
            nm = row["nuclide"]
            qa = row["Q_alpha_AME_MeV"][:8]
            sens = row["d_log10_T_d_Qalpha_dex_per_MeV"][:9]
            q_l4 = row["models"]["H1_L4_qclt"]["Q_alpha_QOU_MeV"][:9]
            q_fstd = row["models"]["H2_FCC_k12_std"]["Q_alpha_QOU_MeV"][:9]
            q_fpau = row["models"]["H2_FCC_k12_pauli"]["Q_alpha_QOU_MeV"][:9]
            dex_fstd = row["models"]["H2_FCC_k12_std"]["log10_T_QOU_over_T_exp_dex"]
            dex_fpau = row["models"]["H2_FCC_k12_pauli"]["log10_T_QOU_over_T_exp_dex"]
            print(
                f"    {nm:<6} Q_AME={qa} MeV  d(log10T)/dQ={sens} dex/MeV | "
                f"Q_L4={q_l4}  Q_FCC(std)={q_fstd} (dex={str(dex_fstd)[:8]})  "
                f"Q_FCC(pauli)={q_fpau} (dex={str(dex_fpau)[:8]})"
            )

        # Strict assertions on exact reproducible invariants
        assert min(open_heavy_abs_dex_unscreened) > mp.mpf("0.13")
        assert max(open_heavy_abs_dex_unscreened) < mp.mpf("0.41")
        assert abs(po210_s_alpha_emp - mp.mpf("0.05530")) < mp.mpf("1e-4")
        assert abs(s_mj_joint - mp.mpf("0.05")) < mp.mpf("1e-75")
        assert abs(po210_mj_joint_dex_err) < mp.mpf("0.05")

        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "80-dps (50-dps serialized) evaluation of zero-parameter Gamow-Gurney-Condon "
            "alpha-decay half-lives (open-shell 0.14-0.40 dex vs magic N=126 210Po "
            "S_alpha = 0.05530), side-by-side zero-parameter tests of Mayer-Jensen "
            "1h_{9/2}^2 x 3p_{1/2}^{-2} seniority overlap (1/20 = 0.0500, +0.0438 dex) "
            "and Perdew-Parr / Goeppert-Mayer shell-kink internal WKB attenuation across "
            "r_pi, plus honest derived-Q_alpha^{QOU} benchmark and d(log10 T_{1/2})/dQ_alpha "
            "sensitivity across heavy alpha emitters (Bean qou-i2jl)."
        )
        wb.set_content_block("prop:alpha-decay-gamow-tunneling")
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("alpha_EM_inv_FormB", fmt(alpha_q_inv, dps=OUT_DPS))
        wb.add_parameter("r_pi_CAL3_fm", fmt(r_pi_fm, dps=OUT_DPS))
        wb.add_parameter("r0_FCC_fm", fmt(r0_fcc_fm, dps=OUT_DPS))
        wb.add_parameter("E0_MeV", fmt(e0_mev, dps=OUT_DPS))
        wb.add_parameter("E_osc_MeV", fmt(eosc_mev, dps=OUT_DPS))
        wb.add_parameter("B_alpha_QOU_MeV", fmt(b_alpha_qou_mev, dps=OUT_DPS))

        wb.add_data(
            "part_a_baseline_gamow_emitters",
            {
                "emitters": baseline_rows,
                "open_shell_heavy_abs_dex_range_unscreened": [
                    fmt(min(open_heavy_abs_dex_unscreened), dps=12),
                    fmt(max(open_heavy_abs_dex_unscreened), dps=12),
                ],
                "open_shell_heavy_abs_dex_range_screened": [
                    fmt(min(open_heavy_abs_dex_screened), dps=12),
                    fmt(max(open_heavy_abs_dex_screened), dps=12),
                ],
                "Po210_empirical_S_alpha": fmt(po210_s_alpha_emp, dps=20),
                "U238_exterior_q0_vs_q1_shift_dex": fmt(u238_q0_vs_q1_shift_dex, dps=20),
                "U238_exterior_q0_abs_miss_dex": fmt(u238_q0_ext_abs_dex, dps=20),
            },
        )
        wb.add_data(
            "part_b_n126_preformation_mechanisms",
            {
                "mayer_jensen_combinatorial": {
                    "proton_1h9_2_degeneracy": "10",
                    "neutron_closed_3p1_2_degeneracy": "2",
                    "neutron_open_2g9_2_degeneracy": "10",
                    "S_MJ_proton_1_over_10": fmt(s_mj_proton, dps=OUT_DPS),
                    "S_MJ_neutron_ratio_2_over_10": fmt(s_mj_neutron_ratio, dps=OUT_DPS),
                    "S_MJ_joint_1_over_20": fmt(s_mj_joint, dps=OUT_DPS),
                    "log10_S_MJ_joint_over_S_emp_dex": fmt(s_mj_joint_dex_diff, dps=15),
                    "Po210_T_half_with_S_MJ_joint_s": fmt(po210_t_mj_joint_s, dps=15),
                    "Po210_T_half_S_MJ_joint_dex_err": fmt(po210_mj_joint_dex_err, dps=15),
                },
                "perdew_parr_shell_kink_wkb": {
                    "hbar_omega_QOU_210_MeV": fmt(hbar_omega_210_mev, dps=20),
                    "G1_QOU_HO_1quantum_MeV": fmt(gap_g1_ho_mev, dps=20),
                    "G2_QOU_MJ_1i13_2_spin_orbit_MeV": fmt(gap_g2_so_qou_mev, dps=20),
                    "S2n_Po210_N126_AME_MeV": fmt(s2n_126_mev, dps=15),
                    "S2n_Po212_N128_AME_MeV": fmt(s2n_128_mev, dps=15),
                    "G3_AME2020_Perdew_Parr_S2n_kink_MeV": fmt(
                        gap_g3_perdew_parr_ame_mev, dps=15
                    ),
                    "grid_3x2": kink_wkb_grid,
                },
            },
        )
        wb.add_data(
            "part_c_derived_qalpha_benchmark",
            {
                "B_alpha_QOU_magicA_MeV": fmt(b_alpha_qou_mev, dps=20),
                "B_alpha_AME2020_MeV": fmt(b_alpha_ame_mev, dps=20),
                "heavy_emitters": derived_qalpha_rows,
            },
        )

        wb.add_assertion(
            "open_shell_heavy_gamow_accuracy_under_0p41_dex",
            fmt(max(open_heavy_abs_dex_unscreened), dps=12),
            "0.399",
            "2e-2",
            source="Zero-parameter Gamow-Gurney-Condon WKB with Form-B alpha_q and r_0^{FCC}",
        )
        wb.add_assertion(
            "Po210_magic_N126_empirical_S_alpha",
            fmt(po210_s_alpha_emp, dps=10),
            "0.05530",
            "1e-4",
            source="NUBASE2020 + AME2020 WKB ratio at magic N=126",
        )
        wb.add_assertion(
            "mayer_jensen_1h9_2_x_3p1_2_joint_overlap_matches_Po210_within_0p05_dex",
            fmt(abs(po210_mj_joint_dex_err), dps=10),
            "0.0438",
            "1e-2",
            source="S_MJ^(pi*nu) = 1/((2*9/2+1)*(2*1/2+1)) = 1/20 = 0.05 vs 0.05530",
        )

        wb.add_caveat(
            "Because |d(log10 T_{1/2})/dQ_alpha| is ~3 to 8.5 dex/MeV across heavy alpha "
            "emitters, sub-dex half-life accuracy from internally predicted Q_alpha^{QOU} "
            "requires ~0.05 MeV relative mass-difference precision (~30 ppm of total B); "
            "smooth macroscopic FCC+TL / q-CLT binding laws without exact shell-closure "
            "terms miss Q_alpha by several MeV and shift log10 T_{1/2} by many dex."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
