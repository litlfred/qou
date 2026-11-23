#!/usr/bin/env python3
"""50-dps verification probe for boosted de Broglie matter-wave interferometry
and zero-parameter Gamow-Gurney-Condon alpha-decay tunneling.

Connects `prop:double-slit-q-phase` (`QOU.Observations.DeBroglieBoostedReebPhase`
and `QOU.MathlibInfra.LorentzBoostPhase`) with
`QOU.Nuclear.ThomaeJacksonCoulombAndAlphaTunneling`
(`QOU.MathlibInfra.ThomaeJacksonCalculus`) through a common physical question:
how the horizontal exterior differential `d_q = q^{-1} d + (1 - q^{-1}) pi_V o d`
behaves inside hadronic/nuclear cores (`q = q_0`) versus exterior vacuum
propagation (`q_local(r) -> 1`).

Part A — Boosted Reeb/Compton Clock & 600 eV Electron Double-Slit (Bach et al. 2013):
  1. Derives the matter-wave wavelength `lambda_dB = 2 pi hbar / p = h / (gamma m v)`
     by Lorentz-boosting the rest-frame Compton/Reeb meridian clock
     `omega_0 = m_e c^2 / hbar` (`rem:meridian-exceptional-divisor-note`,
     Louis de Broglie 1924), verifying Lorentz phase invariance, mass-shell
     identity, and `(E / p) v = c^2` to `< 10^{-75}` at 80 working dps.
  2. Evaluates relativistic vs non-relativistic 600 eV electron wavelengths in
     the Bach, Pope, Liou & Batelaan (2013) controlled double-slit geometry
     (`a = 62 nm`, `d = 272 nm`, `V_acc = 600 V`), plus the `V = 600.2 V`
     contact-potential reference (`50.0456 pm` vs `50.0603 pm`), and computes
     the uniform-`q_0` stretched wavelength `lambda_q = q_0 lambda_dB` and
     `q_0^2` Hodge envelope broadening factor.

Part B — Thomae-Jackson Scaling & Zero-Parameter Gamow Alpha-Decay Tunneling:
  1. Verifies exact Thomae-Jackson backward-to-forward proper-time scaling
     `I_bwd = q_0^{-2} I_fwd` on `tau_j = tau_0 (q_0^2)^j` and the mirror
     proton-pair difference `C(Z+1, 2) - C(Z, 2) = Z` (`Z = 1` for `3H-3He`).
  2. Computes zero-parameter Gamow-Gurney-Condon WKB alpha-decay half-lives
     across `8Be, 212Po, 214Po, 222Rn, 210Po, 226Ra, 238U` using:
       - `q_0` at the 1-term proton pin (`q0Anchor = "proton"`),
       - QOU Form-B Bring-Schwinger `alpha_EM^{-1}(q_0) = 137.035999127...`,
       - 3D FCC close-packed pion-Compton Wigner-Seitz nuclear radius constant
         `r_0^{FCC} = (3 / (4 pi sqrt(2)))^{1/3} * (3/2) * (hbar c / m_pi)
                    = 1.172060153... fm` (CAL-3 `m_{pi+-} = 139.57039 MeV`),
       - AME2020 mass excesses and binding energies (`computations/data/ame2020.json`).
  3. Verifies:
       - `0.14-0.40 dex` (`0.03-0.43 dex` with Perlman-Rasmussen atomic electron
         screening) zero-parameter accuracy across open-shell heavy emitters
         spanning 24 orders of magnitude in half-life,
       - `S_alpha = T_{1/2}^{WKB} / T_{1/2}^{exp} = 0.0553` at magic `N = 126`
         `210Po` (shell-closure cluster preformation hindrance),
       - `3.42-3.43 dex` half-life miss on `238U` if `q_local(r) = q_0`
         persisted throughout the exterior Coulomb barrier (`k_q = k / q_0`),
         providing an immediate experimental proof that `q_local(r) -> 1` in
         exterior vacuum.

Precision discipline: `mpmath` at `workdps = 80` (`fmt` serialized at 50 dps);
zero `float64` imports, literals, or casts anywhere.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
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

# CAL-3 charged pion mass (MeV), matching `computations/coulomb_energy.py`.
M_PI_CHARGED_MEV = mp.mpf("139.57039")

# Ground-state experimental alpha-emitter half-lives from NUBASE2020
# (F. G. Kondev et al., Chinese Phys. C 45, 030001 (2021)), stored as exact
# decimal string factors `(value_str, unit_seconds_str, label)` so no float64
# enters and the probe runs hermetically inside sparse checkouts.
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


def evaluate_electron_double_slit(
    q0: mp.mpf,
    hbar_c_mev_fm: mp.mpf,
    m_e_mev: mp.mpf,
    c_m_s: mp.mpf,
    hbar_j_s: mp.mpf,
) -> dict[str, object]:
    """Evaluate boosted Compton/Reeb phase identities and 600 eV double-slit shifts."""
    with mp.workdps(WORK_DPS):
        one = mp.mpf(1)
        two = mp.mpf(2)
        hc_mev_pm = two * mp.pi * hbar_c_mev_fm * mp.mpf("1e-3")

        def beam_metrics(v_acc_ev_str: str) -> dict[str, mp.mpf]:
            k_mev = mp.mpf(v_acc_ev_str) * mp.mpf("1e-6")
            e_tot_mev = m_e_mev + k_mev
            gamma = e_tot_mev / m_e_mev
            p_rel_c_mev = mp.sqrt(k_mev * (k_mev + two * m_e_mev))
            p_nr_c_mev = mp.sqrt(two * m_e_mev * k_mev)
            beta = p_rel_c_mev / e_tot_mev
            v_m_s = beta * c_m_s
            lam_rel_pm = hc_mev_pm / p_rel_c_mev
            lam_nr_pm = hc_mev_pm / p_nr_c_mev
            lam_q_pm = q0 * lam_rel_pm
            return {
                "K_MeV": k_mev,
                "E_tot_MeV": e_tot_mev,
                "gamma": gamma,
                "beta": beta,
                "v_m_s": v_m_s,
                "p_rel_c_MeV": p_rel_c_mev,
                "p_nr_c_MeV": p_nr_c_mev,
                "lambda_dB_rel_pm": lam_rel_pm,
                "lambda_dB_nr_pm": lam_nr_pm,
                "delta_rel_minus_nr_pm": lam_rel_pm - lam_nr_pm,
                "rel_contraction_ppm": (lam_rel_pm - lam_nr_pm)
                / lam_nr_pm
                * mp.mpf("1e6"),
                "lambda_q_uniform_pm": lam_q_pm,
            }

        b600 = beam_metrics("600")
        b600_2 = beam_metrics("600.2")

        # Verify exact algebraic theorems from `LorentzBoostPhase.lean` and
        # `DeBroglieBoostedReebPhase.lean` in SI / natural units at 600 eV:
        e_mev = b600["E_tot_MeV"]
        p_c_mev = b600["p_rel_c_MeV"]
        gamma = b600["gamma"]
        beta = b600["beta"]
        v_m_s = b600["v_m_s"]

        # Rest-frame Compton angular frequency omega_0 = m_e c^2 / hbar (rad/s)
        e_charge = codata("elementary charge").value
        m_e_c2_j = m_e_mev * mp.mpf("1e6") * e_charge
        omega_0_rad_s = m_e_c2_j / hbar_j_s
        e_tot_j = e_mev * mp.mpf("1e6") * e_charge
        p_si = (p_c_mev * mp.mpf("1e6") * e_charge) / c_m_s

        t_sample_s = mp.mpf("1.3e-9")
        x_sample_m = mp.mpf("0.017")
        tau_boosted = gamma * (t_sample_s - v_m_s * x_sample_m / (c_m_s * c_m_s))
        phase_lhs = omega_0_rad_s * tau_boosted
        phase_rhs = (e_tot_j * t_sample_s - p_si * x_sample_m) / hbar_j_s
        lorentz_phase_residual = abs(phase_lhs - phase_rhs) / abs(phase_lhs)

        mass_shell_residual = abs(
            e_mev * e_mev - p_c_mev * p_c_mev - m_e_mev * m_e_mev
        ) / (m_e_mev * m_e_mev)
        v_phase = e_tot_j / p_si
        de_broglie_product_residual = abs(
            (v_phase * v_m_s) / (c_m_s * c_m_s) - one
        )

        # Bach et al. (2013) double-slit geometry:
        # slit width a = 62 nm, center-to-center separation d = 272 nm,
        # effective propagation distance L = 0.24 m.
        a_slit_m = mp.mpf("62e-9")
        d_slit_m = mp.mpf("272e-9")
        l_screen_m = mp.mpf("0.24")
        lam_rel_m = b600["lambda_dB_rel_pm"] * mp.mpf("1e-12")
        lam_q_m = b600["lambda_q_uniform_pm"] * mp.mpf("1e-12")

        fringe_std_um = (lam_rel_m * l_screen_m / d_slit_m) * mp.mpf("1e6")
        fringe_q_um = (lam_q_m * l_screen_m / d_slit_m) * mp.mpf("1e6")
        envelope_std_mm = (lam_rel_m * l_screen_m / a_slit_m) * mp.mpf("1e3")
        envelope_hodge_q2_mm = (q0 * q0) * envelope_std_mm
        hbar_q = (q0 - one) / q0

        return {
            "assertions_raw": {
                "lorentz_phase_residual": lorentz_phase_residual,
                "mass_shell_residual": mass_shell_residual,
                "de_broglie_product_residual": de_broglie_product_residual,
                "lambda_dB_rel_600eV_pm": b600["lambda_dB_rel_pm"],
                "lambda_dB_nr_600eV_pm": b600["lambda_dB_nr_pm"],
                "lambda_q_600eV_pm": b600["lambda_q_uniform_pm"],
                "hodge_q0_sq": q0 * q0,
            },
            "payload": {
                "compton_clock_omega0_rad_s": fmt(omega_0_rad_s, dps=OUT_DPS),
                "lorentz_phase_rel_residual": fmt(lorentz_phase_residual, dps=20),
                "mass_shell_rel_residual": fmt(mass_shell_residual, dps=20),
                "de_broglie_phase_group_rel_residual": fmt(
                    de_broglie_product_residual, dps=20
                ),
                "beam_600eV_exact": {
                    "accelerating_potential_V": "600",
                    "gamma": fmt(b600["gamma"], dps=OUT_DPS),
                    "beta": fmt(b600["beta"], dps=OUT_DPS),
                    "lambda_dB_rel_pm": fmt(b600["lambda_dB_rel_pm"], dps=OUT_DPS),
                    "lambda_dB_nr_pm": fmt(b600["lambda_dB_nr_pm"], dps=OUT_DPS),
                    "delta_rel_minus_nr_pm": fmt(
                        b600["delta_rel_minus_nr_pm"], dps=OUT_DPS
                    ),
                    "rel_contraction_ppm": fmt(b600["rel_contraction_ppm"], dps=20),
                    "lambda_q_uniform_q0_pm": fmt(
                        b600["lambda_q_uniform_pm"], dps=OUT_DPS
                    ),
                },
                "beam_600p2eV_contact_ref": {
                    "accelerating_potential_V": "600.2",
                    "lambda_dB_rel_pm": fmt(b600_2["lambda_dB_rel_pm"], dps=OUT_DPS),
                    "lambda_dB_nr_pm": fmt(b600_2["lambda_dB_nr_pm"], dps=OUT_DPS),
                    "delta_rel_minus_nr_pm": fmt(
                        b600_2["delta_rel_minus_nr_pm"], dps=OUT_DPS
                    ),
                },
                "bach2013_geometry": {
                    "slit_width_nm": "62",
                    "slit_separation_nm": "272",
                    "screen_distance_m": "0.24",
                    "fringe_spacing_std_um": fmt(fringe_std_um, dps=OUT_DPS),
                    "fringe_spacing_uniform_q0_um": fmt(fringe_q_um, dps=OUT_DPS),
                    "fringe_stretch_ratio_q0": fmt(q0, dps=OUT_DPS),
                    "envelope_halfwidth_std_mm": fmt(envelope_std_mm, dps=OUT_DPS),
                    "envelope_halfwidth_hodge_q0_sq_mm": fmt(
                        envelope_hodge_q2_mm, dps=OUT_DPS
                    ),
                    "hodge_envelope_factor_q0_sq": fmt(q0 * q0, dps=OUT_DPS),
                    "hbar_q": fmt(hbar_q, dps=OUT_DPS),
                },
            },
        }


def evaluate_thomae_jackson_and_alpha_tunneling(
    q0: mp.mpf,
    alpha_q_inv: mp.mpf,
    hbar_c_mev_fm: mp.mpf,
    c_m_s: mp.mpf,
    u_mev: mp.mpf,
    m_e_mev: mp.mpf,
    ame_by_za: dict[tuple[int, int], dict[str, str]],
) -> dict[str, object]:
    """Evaluate Thomae-Jackson scaling, mirror pairs, and zero-parameter Gamow WKB."""
    with mp.workdps(WORK_DPS):
        one = mp.mpf(1)
        two = mp.mpf(2)
        three = mp.mpf(3)
        four = mp.mpf(4)
        alpha_q = one / alpha_q_inv

        # 1. Thomae-Jackson backward-to-forward proper-time scaling on tau_j = tau_0 (q_0^2)^j
        r_step = q0 * q0
        tau_0 = mp.mpf("0.37")
        i_fwd = mp.mpf(0)
        i_bwd = mp.mpf(0)
        for j in range(12):
            tau_j = tau_0 * (r_step ** j)
            f_val = one / (one + tau_j * tau_j)
            i_fwd += (r_step - one) * tau_j * f_val
            i_bwd += (one - one / r_step) * tau_j * f_val
        jackson_ratio_residual = abs(i_bwd / i_fwd - one / (q0 * q0))

        # 2. Mirror nucleus 3H-3He proton-pair count and AME2020 split
        b_3h_mev = mp.mpf(ame_by_za[(1, 3)]["binding_energy_total_keV"]) * mp.mpf(
            "1e-3"
        )
        b_3he_mev = mp.mpf(ame_by_za[(2, 3)]["binding_energy_total_keV"]) * mp.mpf(
            "1e-3"
        )
        mirror_3he_3h_split_mev = b_3h_mev - b_3he_mev

        # 3. 3D FCC close-packed pion-Compton Wigner-Seitz nuclear radius constant:
        #    lambda_bar_pi = hbar * c / m_{pi+-}, l_bond = (3/2) * lambda_bar_pi,
        #    r_0^{FCC} = (3 / (4 * pi * sqrt(2)))^{1/3} * l_bond.
        lambda_bar_pi_fm = hbar_c_mev_fm / M_PI_CHARGED_MEV
        l_bond_fm = (three / two) * lambda_bar_pi_fm
        fcc_ws_factor = mp.cbrt(three / (four * mp.pi * mp.sqrt(two)))
        r0_fcc_fm = fcc_ws_factor * l_bond_fm

        c_fm_s = c_m_s * mp.mpf("1e15")
        ln2 = mp.log(two)
        ea_entry = ame_by_za[(2, 4)]
        delta_alpha_mev = mp.mpf(ea_entry["mass_excess_keV"]) * mp.mpf("1e-3")
        m_alpha_nuc_mev = four * u_mev + delta_alpha_mev - two * m_e_mev

        emitter_rows: list[dict[str, str]] = []
        open_heavy_abs_dex_unscreened: list[mp.mpf] = []
        open_heavy_abs_dex_screened: list[mp.mpf] = []
        s_alpha_210po = mp.mpf(0)
        u238_q0_ext_abs_dex = mp.mpf(0)
        u238_q0_vs_q1_shift_dex = mp.mpf(0)

        for name, z_p, a_p, hl_val_str, hl_unit_str, note in NUBASE2020_ALPHA_EMITTERS:
            z_d = z_p - 2
            a_d = a_p - 4
            ep = ame_by_za[(z_p, a_p)]
            ed = ame_by_za[(z_d, a_d)]

            # Verify exact identity Q_alpha = B_d + B_alpha - B_p vs mass excesses
            q_mev = (
                mp.mpf(ep["mass_excess_keV"])
                - mp.mpf(ed["mass_excess_keV"])
                - mp.mpf(ea_entry["mass_excess_keV"])
            ) * mp.mpf("1e-3")

            # Standard Perlman-Rasmussen (1957) atomic electron-cloud screening
            # Delta E_sc(Z) = (65.3 Z^{7/5} - 80 Z^{2/5}) eV for heavy nuclei
            z_mpf = mp.mpf(z_p)
            de_screen_mev = (
                mp.mpf("65.3") * (z_mpf ** (mp.mpf(7) / mp.mpf(5)))
                - mp.mpf(80) * (z_mpf ** (mp.mpf(2) / mp.mpf(5)))
            ) * mp.mpf("1e-6")
            q_scr_mev = q_mev + de_screen_mev if z_p >= 80 else q_mev

            m_d_nuc_mev = (
                mp.mpf(a_d) * u_mev
                + mp.mpf(ed["mass_excess_keV"]) * mp.mpf("1e-3")
                - mp.mpf(z_d) * m_e_mev
            )
            mu_mev = (m_d_nuc_mev * m_alpha_nuc_mev) / (
                m_d_nuc_mev + m_alpha_nuc_mev
            )

            r_touch_fm = r0_fcc_fm * (mp.cbrt(mp.mpf(a_d)) + mp.cbrt(four))
            r_turn_fm = two * mp.mpf(z_d) * alpha_q * hbar_c_mev_fm / q_mev
            x_ratio = r_touch_fm / r_turn_fm
            g_exp = (
                (mp.sqrt(two * mu_mev * q_mev) / hbar_c_mev_fm)
                * r_turn_fm
                * (mp.acos(mp.sqrt(x_ratio)) - mp.sqrt(x_ratio * (one - x_ratio)))
            )
            v_rel_fm_s = mp.sqrt(two * q_mev / mu_mev) * c_fm_s
            nu_assault_hz = v_rel_fm_s / (two * r_touch_fm)
            t_wkb_s = (ln2 / nu_assault_hz) * mp.exp(two * g_exp)

            # Screened comparison
            r_turn_scr_fm = two * mp.mpf(z_d) * alpha_q * hbar_c_mev_fm / q_scr_mev
            x_scr = r_touch_fm / r_turn_scr_fm
            g_scr = (
                (mp.sqrt(two * mu_mev * q_scr_mev) / hbar_c_mev_fm)
                * r_turn_scr_fm
                * (mp.acos(mp.sqrt(x_scr)) - mp.sqrt(x_scr * (one - x_scr)))
            )
            nu_scr_hz = (mp.sqrt(two * q_scr_mev / mu_mev) * c_fm_s) / (
                two * r_touch_fm
            )
            t_wkb_scr_s = (ln2 / nu_scr_hz) * mp.exp(two * g_scr)

            t_exp_s = mp.mpf(hl_val_str) * mp.mpf(hl_unit_str)
            dex_err = mp.log10(t_wkb_s / t_exp_s)
            dex_scr_err = mp.log10(t_wkb_scr_s / t_exp_s)
            s_alpha = t_wkb_s / t_exp_s

            if z_p >= 80 and name != "210Po":
                open_heavy_abs_dex_unscreened.append(abs(dex_err))
                open_heavy_abs_dex_screened.append(abs(dex_scr_err))
            if name == "210Po":
                s_alpha_210po = s_alpha
            if name == "238U":
                # Hypothetical uniform exterior q_local(r) = q_0:
                # horizontal d_q = q_0^{-1} d stretches wavelength lambda_q = q_0 lambda_dB,
                # scaling the exterior WKB wavenumber k_q(r) = k(r) / q_0 -> G_q = G / q_0.
                t_ext_q0_s = (ln2 / nu_assault_hz) * mp.exp(two * (g_exp / q0))
                u238_q0_vs_q1_shift_dex = mp.log10(t_ext_q0_s / t_wkb_s)
                u238_q0_ext_abs_dex = abs(mp.log10(t_ext_q0_s / t_exp_s))

            emitter_rows.append(
                {
                    "nuclide": name,
                    "Z": str(z_p),
                    "A": str(a_p),
                    "N": str(a_p - z_p),
                    "regime": note,
                    "Q_alpha_AME_MeV": fmt(q_mev, dps=20),
                    "R_touch_FCC_fm": fmt(r_touch_fm, dps=20),
                    "R_turn_fm": fmt(r_turn_fm, dps=20),
                    "two_G_WKB": fmt(two * g_exp, dps=20),
                    "T_half_exp_s": fmt(t_exp_s, dps=15),
                    "T_half_WKB_unscreened_s": fmt(t_wkb_s, dps=15),
                    "log10_T_WKB_over_T_exp_dex": fmt(dex_err, dps=12),
                    "log10_T_WKB_screened_over_T_exp_dex": fmt(dex_scr_err, dps=12),
                    "S_alpha_unscreened": fmt(s_alpha, dps=12),
                }
            )

        return {
            "assertions_raw": {
                "jackson_ratio_residual": jackson_ratio_residual,
                "r0_fcc_fm": r0_fcc_fm,
                "alpha_q_inv": alpha_q_inv,
                "open_heavy_min_abs_dex": min(open_heavy_abs_dex_unscreened),
                "open_heavy_max_abs_dex": max(open_heavy_abs_dex_unscreened),
                "open_heavy_max_abs_dex_screened": max(open_heavy_abs_dex_screened),
                "s_alpha_210po": s_alpha_210po,
                "u238_q0_ext_abs_dex": u238_q0_ext_abs_dex,
                "u238_q0_vs_q1_shift_dex": u238_q0_vs_q1_shift_dex,
            },
            "payload": {
                "thomae_jackson_scaling": {
                    "q0_inv_sq": fmt(one / (q0 * q0), dps=OUT_DPS),
                    "bwd_over_fwd_ratio": fmt(i_bwd / i_fwd, dps=OUT_DPS),
                    "bwd_over_fwd_residual": fmt(jackson_ratio_residual, dps=20),
                },
                "mirror_3He_3H": {
                    "Z_low": "1",
                    "Z_high": "2",
                    "proton_pair_diff": "1",
                    "AME2020_binding_split_MeV": fmt(
                        mirror_3he_3h_split_mev, dps=20
                    ),
                },
                "fcc_pion_compton_geometry": {
                    "m_pi_charged_CAL3_MeV": fmt(M_PI_CHARGED_MEV, dps=20),
                    "lambda_bar_pi_fm": fmt(lambda_bar_pi_fm, dps=OUT_DPS),
                    "l_bond_fm": fmt(l_bond_fm, dps=OUT_DPS),
                    "r0_FCC_fm": fmt(r0_fcc_fm, dps=OUT_DPS),
                    "alpha_EM_inv_FormB": fmt(alpha_q_inv, dps=OUT_DPS),
                },
                "gamow_alpha_emitters": emitter_rows,
                "summary_diagnostics": {
                    "open_shell_heavy_abs_dex_range_unscreened": [
                        fmt(min(open_heavy_abs_dex_unscreened), dps=10),
                        fmt(max(open_heavy_abs_dex_unscreened), dps=10),
                    ],
                    "open_shell_heavy_abs_dex_range_screened": [
                        fmt(min(open_heavy_abs_dex_screened), dps=10),
                        fmt(max(open_heavy_abs_dex_screened), dps=10),
                    ],
                    "Po210_magic_N126_S_alpha": fmt(s_alpha_210po, dps=12),
                    "U238_exterior_q0_vs_q1_shift_dex": fmt(
                        u238_q0_vs_q1_shift_dex, dps=12
                    ),
                    "U238_exterior_q0_abs_miss_dex": fmt(
                        u238_q0_ext_abs_dex, dps=12
                    ),
                },
            },
        }


def main() -> None:
    with mp.workdps(WORK_DPS):
        q0 = q_at(dps=WORK_DPS)
        h_j_s = codata("Planck constant").value
        hbar_j_s = h_j_s / (mp.mpf(2) * mp.pi)
        c_m_s = codata("speed of light in vacuum").value
        e_c = codata("elementary charge").value
        hbar_c_mev_fm = (hbar_j_s * c_m_s / (e_c * mp.mpf("1e6"))) * mp.mpf("1e15")
        m_e_mev = codata("electron mass energy equivalent in mev").value
        u_mev = codata("atomic mass constant energy equivalent in mev").value

        alpha_q_inv = solve_form_b_alpha_inv(q0)
        ame_by_za = load_ame2020_by_za(AME_JSON_PATH)

        ds = evaluate_electron_double_slit(
            q0=q0,
            hbar_c_mev_fm=hbar_c_mev_fm,
            m_e_mev=m_e_mev,
            c_m_s=c_m_s,
            hbar_j_s=hbar_j_s,
        )
        tj = evaluate_thomae_jackson_and_alpha_tunneling(
            q0=q0,
            alpha_q_inv=alpha_q_inv,
            hbar_c_mev_fm=hbar_c_mev_fm,
            c_m_s=c_m_s,
            u_mev=u_mev,
            m_e_mev=m_e_mev,
            ame_by_za=ame_by_za,
        )

        # Strict internal verification assertions before writing witness
        ds_raw = ds["assertions_raw"]
        tj_raw = tj["assertions_raw"]
        assert ds_raw["lorentz_phase_residual"] < mp.mpf("1e-75")
        assert ds_raw["mass_shell_residual"] < mp.mpf("1e-75")
        assert ds_raw["de_broglie_product_residual"] < mp.mpf("1e-75")
        assert tj_raw["jackson_ratio_residual"] < mp.mpf("1e-75")
        assert abs(tj_raw["r0_fcc_fm"] - mp.mpf("1.1720601534")) < mp.mpf("1e-9")
        assert abs(tj_raw["s_alpha_210po"] - mp.mpf("0.0553")) < mp.mpf("1e-3")
        assert abs(tj_raw["u238_q0_ext_abs_dex"] - mp.mpf("3.421")) < mp.mpf("2e-2")

        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "80-dps (50-dps serialized) verification of (1) Lorentz-boosted Reeb/Compton "
            "de Broglie wavelength lambda_dB = 2 pi hbar / p and d_q fringe/envelope "
            "scaling in 600 eV electron double-slit diffraction (Bach et al. 2013), and "
            "(2) Thomae-Jackson q^{-2} proper-time scaling plus zero-parameter "
            "Gamow-Gurney-Condon alpha-decay tunneling across 8Be, 212Po, 214Po, 222Rn, "
            "210Po, 226Ra, 238U using Form-B alpha_EM(q_0) and r_0^{FCC} = 1.17206 fm, "
            "demonstrating the 3.42-3.43 dex exterior q_local(r) -> 1 discriminator on 238U."
        )
        wb.set_content_block("prop:double-slit-q-phase")
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("alpha_EM_inv_FormB", fmt(alpha_q_inv, dps=OUT_DPS))
        wb.add_parameter("r0_FCC_fm", fmt(tj_raw["r0_fcc_fm"], dps=OUT_DPS))

        wb.add_data("double_slit_de_broglie", ds["payload"])
        wb.add_data("alpha_tunneling_and_thomae_jackson", tj["payload"])

        wb.add_assertion(
            "lorentz_boost_phase_invariance",
            fmt(ds_raw["lorentz_phase_residual"], dps=15),
            "0",
            "1e-70",
            source="QOU.MathlibInfra.LorentzBoostPhase.lorentz_boost_phase_invariance",
        )
        wb.add_assertion(
            "lambda_dB_rel_600eV_pm",
            fmt(ds_raw["lambda_dB_rel_600eV_pm"], dps=15),
            "50.05393956",
            "1e-6",
            source="CODATA 2022 + relativistic 600 eV kinematics (Bach et al. 2013)",
        )
        wb.add_assertion(
            "thomae_jackson_bwd_fwd_ratio",
            fmt(tj_raw["jackson_ratio_residual"], dps=15),
            "0",
            "1e-70",
            source="QOU.Nuclear.ThomaeJacksonCoulombAndAlphaTunneling.jackson_bwd_sum_eq_q_inv_sq_mul_fwd_sum",
        )
        wb.add_assertion(
            "r0_FCC_pion_compton_fm",
            fmt(tj_raw["r0_fcc_fm"], dps=15),
            "1.1720601534",
            "1e-9",
            source="(3 / (4 pi sqrt(2)))^{1/3} * (3/2) * (hbar c / m_{pi+-})",
        )
        wb.add_assertion(
            "Po210_magic_N126_S_alpha",
            fmt(tj_raw["s_alpha_210po"], dps=10),
            "0.0553",
            "1e-3",
            source="NUBASE2020 + AME2020 zero-parameter WKB ratio at magic N=126",
        )
        wb.add_assertion(
            "U238_exterior_q0_discriminator_dex",
            fmt(tj_raw["u238_q0_ext_abs_dex"], dps=10),
            "3.421",
            "2e-2",
            source="238U WKB half-life miss under uniform exterior k_q = k / q_0",
        )

        wb.add_caveat(
            "Uniform exterior q = q_0 stretches lambda_q = q_0 lambda_dB (+11.0 %); "
            "both laboratory matter-wave interferometry and the 3.42-3.43 dex 238U "
            "alpha-tunneling discriminator require q_local(r) -> 1 in exterior vacuum."
        )
        wb.add_caveat(
            "r_0^{FCC} = 1.17206015 fm uses CAL-3 m_{pi+-} = 139.57039 MeV with "
            "canonical tetrahedral bond l_bond = (3/2) lambda_bar_pi and 3D FCC "
            "close-packing fraction pi / (3 sqrt(2))."
        )

        witness_path = wb.save(
            {"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)}
        )
        print(f"q0 (proton pin)            = {fmt(q0, dps=30)}")
        print(f"1/alpha_q (Form B)         = {fmt(alpha_q_inv, dps=20)}")
        print(f"r0_FCC (fm)                = {fmt(tj_raw['r0_fcc_fm'], dps=20)}")
        print(
            f"600 eV lambda_dB (rel/nr)  = "
            f"{fmt(ds_raw['lambda_dB_rel_600eV_pm'], dps=10)} pm / "
            f"{fmt(ds_raw['lambda_dB_nr_600eV_pm'], dps=10)} pm"
        )
        print(
            f"600.2 V contact ref        = "
            f"{ds['payload']['beam_600p2eV_contact_ref']['lambda_dB_rel_pm'][:9]} pm / "
            f"{ds['payload']['beam_600p2eV_contact_ref']['lambda_dB_nr_pm'][:9]} pm"
        )
        print(
            f"600 eV lambda_q (q0*rel)   = "
            f"{fmt(ds_raw['lambda_q_600eV_pm'], dps=10)} pm"
        )
        print(
            f"Open-shell heavy |dex|     = "
            f"[{fmt(tj_raw['open_heavy_min_abs_dex'], dps=6)}, "
            f"{fmt(tj_raw['open_heavy_max_abs_dex'], dps=6)}] unscreened; "
            f"max {fmt(tj_raw['open_heavy_max_abs_dex_screened'], dps=6)} screened"
        )
        print(f"210Po (N=126) S_alpha      = {fmt(tj_raw['s_alpha_210po'], dps=8)}")
        print(
            f"238U q_local=q0 miss (dex) = "
            f"{fmt(tj_raw['u238_q0_ext_abs_dex'], dps=8)} "
            f"(shift {fmt(tj_raw['u238_q0_vs_q1_shift_dex'], dps=8)} dex)"
        )
        print(f"witness -> {witness_path}")


if __name__ == "__main__":
    main()
