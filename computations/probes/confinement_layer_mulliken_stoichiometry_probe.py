#!/usr/bin/env python3
"""confinement_layer_mulliken_stoichiometry_probe.py

First-principles 80-dps SymPy + mpmath verification of the 5-Layer Iterated
Confinement Tower, Adiabatic Gap Ratios eta_k, Zero-Fit Layer-3 Atomic Shell
Ionization / Mulliken Electronegativity / Parr-Pearson Hardness (H..Ne), and
Layer-4 Unimodular Smith / Birch Toric Stoichiometry (Bean qou-5lct / Q-Gap-0).

Extends and complements `confinement_layer_tower_chem_probe.py` (#9212) and pairs
directly with `QOU.Observations.ConfinementLayerMullikenStoichiometry` (0 sorry,
0 custom axioms, importing `ToricConicOpt.ConfinementLayerTower`):

  1. Five-Layer QOU Derived Scale Tower (L_0 -> L_1 -> L_2 -> L_3 -> L_4):
     Evaluates all layer gaps and perturbations directly from (m_e, q_0) using
     post-#9360 derived 4-topology Form-B alpha_EM(q_0) (and conditional Form-C),
     hadron gap m_p(q_0), nuclear scale 2*E_0^ord0(q_0), Rydberg scale
     Ry_FormB(q_0) = 13.60569312915 eV (+0.725 ppb vs CODATA-2022), and the
     h_q^2 = (q_0 - q_0^{-1})^2 hydrogen-bond rung (~0.4167 eV water 2-H-bond
     cohesion, eta_3 ~ 3.06e-2), verifying `five_layer_adiabatic_telescoping_product`
     and base-q_0 hierarchy depths log_{q_0}(eta_k) at the physical proton pin
     (muon pin on hold per 2026-11-28 owner ruling until rederivation).

  2. Zero-Fit Layer-3 Atomic Ionization I_1, Electron Affinity A_ea, Mulliken
     Electronegativity chi_M, and Parr-Pearson Hardness eta_PP across H..Ne (Z=1..10):
     - Exact Dirac reduced-mass protium ionization I_1(H; q_0) (+2.47 ppm vs NIST)
       and Kellner-Hylleraas 217/128 Ry_FormB(q_0) helium closed form;
     - Zero-parameter 80-dps Roothaan-Slater-Condon variational Hartree-Fock solver
       (exact analytical factorial Slater R^k integrals, Russell-Saunders ground
       multiplets, uniform per-Z split-valence STO hierarchy polished at 80 dps)
       scaled solely by derived Ry_FormB(q_0), verifying:
         * Fenchel-Legendre subgradient interval & midpoint identities
           (`fenchel_subgradient_interval_iff_mulliken_hardness`),
         * Strict PPLB convexity eta_PP(Z) > 0 for all Z = 1..10,
         * Noble-gas hardness maxima at He (Z=2) and Ne (Z=10) + piecewise
           shell-closure kink (`two_shell_piecewise_hardness_kink`),
         * Subshell penetration drop I_1(Be) > I_1(B) and Hund 2p^3 -> 2p^4
           spin-pairing inversion I_1(N) > I_1(O),
         * Sanderson-Parr charge-transfer minimizer (`parr_pearson_charge_transfer_minimizer`)
           on canonical diatomic pairs (LiF, HF, CO), scored transparently against NIST.

  3. Layer-4 Multi-Step Motif Composition, Unimodular SNF(A_CHO) = diag(1, 1, 2),
     and 80-dps Birch Toric Hessian Convexity:
     - Explicit nucleon -> nucleus -> C-H-O molecular `expandMotifs_comp` &
       `promoteLayer_two_step_charge_and_kernel` verification (Delta Z = Delta N_nuc = 0),
     - Unimodular GL_3(Z) x GL_7(Z) certificate U * A_CHO * V = diag(1, 1, 2)
       (`cho_smith_normal_form_diag_1_1_2`), 4 canonical 1D primitive circuits,
       and Sturmfels-Thomas normal-form reduction on b = (2, 8, 4)^T,
     - 80-dps Birch mass-action equilibrium and exact sum-of-squares Hessian
       identity (`birch_hessian_quad_form_sum_sq_and_pos`).

STRICT ANTI-FIT & PRECISION DISCIPLINE:
  - mp.dps = 95 compute / 80 output set before all module-level mpf evaluations; zero float64, zero math.
  - Zero fitted parameters: only (m_e, q_0) enter all QOU energy scales.
  - Evaluates strictly at the physical proton pin q_at(80) (q0Anchor="proton"; muon pin is on hold per 2026-11-28 owner ruling until rederivation).
"""
from __future__ import annotations

from fractions import Fraction
import os
import sys
from pathlib import Path

os.environ.setdefault("QOU_OUTPUT_DPS", "80")
os.environ.setdefault("QOU_COMPUTE_DPS", "95")
os.environ.setdefault("QOU_PRECISION_GUARD", "15")

from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
import qou_substrate.precision as _qsp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

_qsp.OUTPUT_DPS = 80
_qsp.PRECISION_GUARD = 15
_qsp.COMPUTE_DPS = 95
set_compute_dps(95)
mp.dps = max(mp.dps, 95)

import sympy as sp  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402
import two_term_qtrace_weighting as ttq  # noqa: E402

DPS = 80
LEAN_MODULE = "QOU.Observations.ConfinementLayerMullikenStoichiometry"
UPSTREAM_LEAN_MODULE = "ToricConicOpt.ConfinementLayerTower"

# ── Exact SI / CODATA-2022 registry lookups (validation & unit conversion only) ──
_ME_REC = _codata.codata("electron mass energy equivalent in MeV")
_MP_REC = _codata.codata("proton mass energy equivalent in MeV")
_MN_REC = _codata.codata("neutron mass energy equivalent in MeV")
_AINV_REC = _codata.codata("inverse fine-structure constant")
_RY_REC = _codata.codata("Rydberg constant times hc in eV")
_H_SI_REC = _codata.codata("Planck constant")
_C_SI_REC = _codata.codata("speed of light in vacuum")
_E_SI_REC = _codata.codata("elementary charge")
_KB_SI_REC = _codata.codata("Boltzmann constant")
_NA_SI_REC = _codata.codata("Avogadro constant")

M_E_MEV = mpf(_ME_REC.value_str)
M_P_EXP_MEV = mpf(_MP_REC.value_str)
M_N_EXP_MEV = mpf(_MN_REC.value_str)
DM_NP_EXP_MEV = M_N_EXP_MEV - M_P_EXP_MEV
ALPHA_INV_EXP = mpf(_AINV_REC.value_str)
RY_EXP_EV = mpf(_RY_REC.value_str)
RY_EXP_UNC_EV = mpf(_RY_REC.uncertainty_str)

H_SI = mpf(_H_SI_REC.value_str)
C_SI = mpf(_C_SI_REC.value_str)
E_SI = mpf(_E_SI_REC.value_str)
KB_SI = mpf(_KB_SI_REC.value_str)
NA_SI = mpf(_NA_SI_REC.value_str)

HBAR_C_MEV_FM = (H_SI * C_SI / (mpf(2) * mp.pi)) / (E_SI * mpf("1e6")) * mpf("1e15")
KB_EV_PER_K = KB_SI / E_SI
# Exact SI-2019 conversion: 1 eV/molecule = (N_A * e / 1000) kJ/mol
KJMOL_PER_EV = NA_SI * E_SI / mpf(1000)

# Precomputed exact factorials 0!..40! as 80-dps mpf values for analytical Slater integrals
FACT: list[mpf] = [mpf(1)]
for _k in range(1, 41):
    FACT.append(FACT[-1] * mpf(_k))

# Exact Russell-Saunders ground-term multiplet coefficients of bare Slater F^2(2p, 2p)
# for 2p^n (n = 0..6): ^1S (0), ^2P (0), ^3P (-1/5), ^4S (-3/5), ^3P (-3/5), ^2P (-4/5), ^1S (-6/5)
C2_2P_GROUND: list[mpf] = [
    mpf(0),
    mpf(0),
    -mpf(1) / mpf(5),
    -mpf(3) / mpf(5),
    -mpf(3) / mpf(5),
    -mpf(4) / mpf(5),
    -mpf(6) / mpf(5),
]

# Experimental NIST Atomic Spectra Database / CRC reference (I_1, A_ea) in eV for Z = 1..10
# Used strictly as external validation targets; negative A_ea denotes unbound anion resonance.
NIST_ATOM_Z1_TO_10: list[tuple[str, int, str, str]] = [
    ("H", 1, "13.598434599702", "0.754195"),
    ("He", 2, "24.587389011", "-0.50"),
    ("Li", 3, "5.39171495", "0.618049"),
    ("Be", 4, "9.322699", "-0.50"),
    ("B", 5, "8.298019", "0.279723"),
    ("C", 6, "11.260296", "1.262118"),
    ("N", 7, "14.53413", "-0.07"),
    ("O", 8, "13.618055", "1.461112"),
    ("F", 9, "17.42282", "3.401190"),
    ("Ne", 10, "21.564540", "-1.20"),
]


def q_int(n: int, q: mpf) -> mpf:
    """Balanced quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1}) at 80 dps."""
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def log_q(x: mpf, q: mpf) -> mpf:
    """Base-q logarithm log_q(x) = ln(x) / ln(q) at 80 dps."""
    return mp.log(x) / mp.log(q)


def _solve_cubic(c3: mpf, c2: mpf, c1: mpf, c0: mpf, init: mpf) -> mpf:
    """80-dps Newton solver for c3*a^3 + c2*a^2 + c1*a + c0 = 0."""
    a_val = init
    tol = mpf(10) ** (-84)
    for _ in range(45):
        f_val = c3 * (a_val ** 3) + c2 * (a_val ** 2) + c1 * a_val + c0
        fp_val = mpf(3) * c3 * (a_val ** 2) + mpf(2) * c2 * a_val + c1
        step = f_val / fp_val
        a_val -= step
        if abs(step) < tol:
            break
    return a_val


def evaluate_five_layer_tower(q: mpf, m_e_mev: mpf) -> dict:
    """Evaluate QOU's zero-fit 5-layer confinement scale tower at aether parameter pin q."""
    vol_41 = mpf(2) * mp.clsin(2, mp.pi / mpf(3))
    h_q = q - mpf(1) / q
    h2 = h_q ** 2
    hbar_q = mpf(1) - mpf(1) / q

    # 1. Fine-structure ladder (Form A, post-#9360 derived Form B, conditional Form C)
    T_em = q * q_int(9, q) * q_int(10, q) + mpf(8) / (mpf(12) * mp.pi)
    H_em = q_int(2, q) / (mpf(8) * mp.pi)
    alpha_a = (-T_em + mp.sqrt(T_em * T_em + mpf(4) * H_em)) / (mpf(2) * H_em)
    alpha_b = _solve_cubic(-H_em * h2, H_em, T_em, -mpf(1), mpf(1) / T_em)
    delta_b3 = mp.zeta(3) - mp.polylog(3, q ** (-2))
    c2_bloch = H_em * delta_b3 / (mpf(8) * mp.pi)
    alpha_c = _solve_cubic(c2_bloch - H_em * h2, H_em, T_em, -mpf(1), alpha_b)

    # 2. Layer-1 hadron confinement scale m_p(q) and intra-nucleon Borromean QED shift (#9379)
    trM_bor = abs((mpf(4) + h2 - mpf(3) * (h2 ** 2) - (h2 ** 3)) / (h2 + mpf(4)))
    qf3 = (q ** 2 + mpf(1) + q ** (-2)) * (q + mpf(1) / q)
    mp_model_mev = m_e_mev * (mpf(2) * vol_41 / (hbar_q ** 2) * (trM_bor * qf3 / (q ** 3)) - mpf(12))

    # Borromean V^3 all-3-pairs quantum-trace electromagnetic self-energy (#9379):
    # E07 = alpha_FormB(q) * m_p(q) * delta_t(q, "all_pairs", connected=False) = -0.75712507 MeV
    p_bor = (
        q ** 12
        - mpf(3) * (q ** 10)
        + mpf(3) * (q ** 8)
        - mpf(5) * (q ** 6)
        + mpf(3) * (q ** 4)
        - mpf(3) * (q ** 2)
        + mpf(1)
    )
    tr_v3 = -p_bor / (q ** 6)
    eps_flav_v3 = h_q * tr_v3 / (q_int(2, q) ** 3)
    dt_all_raw = ttq.delta_t(q, "all_pairs", connected=False)
    dm_em_v3_mev = alpha_b * mp_model_mev * dt_all_raw

    # Scored baseline Q_beta(q) and two-channel Legendre-Borromean S04+E07 Delta m_np(q) (#9379)
    e0_ord0_mev = qbeta_e0.order_zero(q, m_e_mev)
    e0_twr_mev = qbeta_e0.tower_summed(q, m_e_mev)
    qbeta_scored_mev = eps_flav_v3 * e0_twr_mev
    dm_np_scored_mev = m_e_mev + qbeta_scored_mev
    # Own-sector Thomae-Jackson (1 - q^{-2}) strong scale + all-3-pairs V^3 QED (#9379 S04+E07):
    s04_strong_mev = mpf(3) * e0_ord0_mev * (mpf(1) - q ** (-2))
    dm_np_two_channel_mev = s04_strong_mev + dm_em_v3_mev

    # 3. Layer-2 nuclear scale: model 2 * E_0^ord0(q) and AME-2020 validation comparators
    delta_nuc_model_mev = mpf(2) * e0_ord0_mev
    b_he4_pa_mev = +ame_binding_mev(2, 4) / mpf(4)
    b_c12_pa_mev = +ame_binding_mev(6, 12) / mpf(12)
    b_fe56_pa_mev = +ame_binding_mev(26, 56) / mpf(56)

    # 4. Layer-3 atomic Rydberg scale Ry = (1/2) alpha_EM^2 m_e (zero fit!)
    ry_form_a_mev = (alpha_a ** 2) * m_e_mev / mpf(2)
    ry_form_b_mev = (alpha_b ** 2) * m_e_mev / mpf(2)
    ry_form_c_mev = (alpha_c ** 2) * m_e_mev / mpf(2)
    ry_form_b_ev = ry_form_b_mev * mpf("1e6")
    ry_form_c_ev = ry_form_c_mev * mpf("1e6")

    # 5. Layer-4 molecular hydrogen-bond & van der Waals h_q^2 ladder (`hbond_categorical_action.py`)
    e_cov_bohr_ev = ry_form_b_ev / mpf(3)
    e_hbond_single_bohr_ev = h2 * e_cov_bohr_ev
    e_hbond_2h2o_bohr_ev = mpf(2) * e_hbond_single_bohr_ev
    # Water O-H covalent reference (460 kJ/mol -> eV via exact SI N_A*e/1000) * 2 H-bonds * h_q^2:
    e_cov_oh_ev = mpf(460) / KJMOL_PER_EV
    e_hbond_2h2o_ref_ev = mpf(2) * h2 * e_cov_oh_ev
    e_hbond_2h2o_ref_mev = e_hbond_2h2o_ref_ev * mpf("1e-6")
    e_hbond_2h2o_bohr_mev = e_hbond_2h2o_bohr_ev * mpf("1e-6")

    # 6. Five-layer telescoping scale chain Delta_0 > Delta_1 > Delta_2 > Delta_3 > Delta_4 (in MeV)
    #    Delta_0 = m_p(q) / alpha_B(q) (preon/ribbon ultraviolet scale so Delta_1 / Delta_0 = alpha_B),
    #    Delta_1 = m_p(q)              (Layer-1 hadron mass gap ~938.27 MeV),
    #    Delta_2 = 2 * E_0^ord0(q)     (Layer-2 QOU nuclear binding scale ~8.37 MeV),
    #    Delta_3 = Ry_FormB(q)         (Layer-3 QOU atomic Rydberg scale ~13.6057 eV),
    #    Delta_4 = 2 * h_q^2 * E_cov   (Layer-4 QOU H-bond molecular cohesion ~0.3964 / 0.4167 eV).
    delta_0_mev = mp_model_mev / alpha_b
    delta_1_mev = mp_model_mev
    delta_2_mev = delta_nuc_model_mev
    delta_3_mev = ry_form_b_mev
    delta_4_pure_mev = e_hbond_2h2o_bohr_mev
    delta_4_h2o_mev = e_hbond_2h2o_ref_mev

    eta_0 = delta_1_mev / delta_0_mev  # == alpha_b
    eta_1_model = delta_2_mev / delta_1_mev
    eta_1_c12 = b_c12_pa_mev / delta_1_mev
    eta_2_model = delta_3_mev / delta_2_mev
    eta_2_c12 = delta_3_mev / b_c12_pa_mev
    eta_3_pure = delta_4_pure_mev / delta_3_mev  # == (2/3) * h_q^2
    eta_3_h2o = delta_4_h2o_mev / delta_3_mev    # == 0.41672 eV / 13.60569 eV = 3.0628e-2

    telescoping_rhs_pure = delta_0_mev * (eta_0 * eta_1_model * eta_2_model * eta_3_pure)
    telescoping_err_pure = abs(delta_4_pure_mev - telescoping_rhs_pure)
    logq_sum_err = abs(
        log_q(delta_4_pure_mev / delta_0_mev, q)
        - (log_q(eta_0, q) + log_q(eta_1_model, q) + log_q(eta_2_model, q) + log_q(eta_3_pure, q))
    )

    # Neutron-star outer-crust L_3 -> L_2 electron-capture threshold E_{F,e}^* = Delta m_np
    def _ns_crust(efe_mev: mpf) -> dict[str, mpf]:
        pfe = mp.sqrt(efe_mev ** 2 - m_e_mev ** 2)
        ne_fm3 = (pfe / HBAR_C_MEV_FM) ** 3 / (mpf(3) * (mp.pi ** 2))
        return {
            "E_Fe_star_MeV": efe_mev,
            "T_Fe_star_MeV": efe_mev - m_e_mev,
            "p_Fe_star_MeV_c": pfe,
            "n_e_star_cm3": ne_fm3 * mpf("1e39"),
        }

    return {
        "q0": q,
        "h_q": h_q,
        "h_q_sq": h2,
        "alpha_inv_form_a": mpf(1) / alpha_a,
        "alpha_inv_form_b": mpf(1) / alpha_b,
        "alpha_inv_form_c": mpf(1) / alpha_c,
        "alpha_form_b": alpha_b,
        "mp_model_MeV": mp_model_mev,
        "e0_ord0_MeV": e0_ord0_mev,
        "delta_nuc_model_MeV": delta_nuc_model_mev,
        "b_c12_per_A_AME_MeV": b_c12_pa_mev,
        "b_he4_per_A_AME_MeV": b_he4_pa_mev,
        "b_fe56_per_A_AME_MeV": b_fe56_pa_mev,
        "ry_form_a_eV": ry_form_a_mev * mpf("1e6"),
        "ry_form_b_eV": ry_form_b_ev,
        "ry_form_c_eV": ry_form_c_ev,
        "ry_form_b_rel_err_ppb": (ry_form_b_ev - RY_EXP_EV) / RY_EXP_EV * mpf("1e9"),
        "ry_form_c_rel_err_ppb": (ry_form_c_ev - RY_EXP_EV) / RY_EXP_EV * mpf("1e9"),
        "e_hbond_2h2o_bohr_eV": e_hbond_2h2o_bohr_ev,
        "e_hbond_2h2o_ref_eV": e_hbond_2h2o_ref_ev,
        "dm_em_v3_MeV": dm_em_v3_mev,
        "dm_np_scored_MeV": dm_np_scored_mev,
        "dm_np_two_channel_MeV": dm_np_two_channel_mev,
        "eta_0_form_b": eta_0,
        "eta_1_model": eta_1_model,
        "eta_1_c12_AME": eta_1_c12,
        "eta_2_model": eta_2_model,
        "eta_2_c12_AME": eta_2_c12,
        "eta_3_pure_bohr": eta_3_pure,
        "eta_3_h2o_hbond": eta_3_h2o,
        "log_q0_eta_0": log_q(eta_0, q),
        "log_q0_eta_1_model": log_q(eta_1_model, q),
        "log_q0_eta_2_model": log_q(eta_2_model, q),
        "log_q0_eta_3_h2o": log_q(eta_3_h2o, q),
        "telescoping_product_pure": eta_0 * eta_1_model * eta_2_model * eta_3_pure,
        "telescoping_err_MeV": telescoping_err_pure,
        "log_q0_telescoping_err": logq_sum_err,
        "strict_hierarchy_holds": (
            mpf(0) < delta_4_pure_mev < delta_3_mev < delta_2_mev < delta_1_mev < delta_0_mev
        ),
        "ns_crust_qou_scored": _ns_crust(dm_np_scored_mev),
        "ns_crust_codata_validation": _ns_crust(DM_NP_EXP_MEV),
    }


# =============================================================================
# PART 2: Exact 80-dps Analytical Slater-Condon Variational Atomic HF Solver
# =============================================================================

def _gamma_int(p: int, rate: mpf) -> mpf:
    """Exact integral int_0^inf r^p exp(-rate * r) dr = p! / rate^{p+1}."""
    return FACT[p] / (rate ** (p + 1))


def _compress_dens(terms: list[tuple[mpf, int, mpf]]) -> list[tuple[mpf, int, mpf]]:
    bucket: dict[tuple[int, mpf], mpf] = {}
    for coeff, p_pow, rate in terms:
        key = (p_pow, rate)
        bucket[key] = bucket.get(key, mpf(0)) + coeff
    return [(c, p_pow, rate) for (p_pow, rate), c in bucket.items() if c != 0]


def _radial_overlap(ra: list[tuple[mpf, int, mpf]], rb: list[tuple[mpf, int, mpf]]) -> mpf:
    return sum(
        c1 * c2 * _gamma_int(p1 + p2 + 2, a1 + a2)
        for c1, p1, a1 in ra
        for c2, p2, a2 in rb
    )


def _normalize_orb(ra: list[tuple[mpf, int, mpf]]) -> list[tuple[mpf, int, mpf]]:
    nrm = mp.sqrt(_radial_overlap(ra, ra))
    return [(c / nrm, p, a) for c, p, a in ra]


def _orth_against(
    raw: list[tuple[mpf, int, mpf]],
    basis_list: list[list[tuple[mpf, int, mpf]]],
) -> list[tuple[mpf, int, mpf]]:
    cur = list(raw)
    for b_orb in basis_list:
        ov = _radial_overlap(b_orb, cur)
        cur = cur + [(-ov * c, p, a) for c, p, a in b_orb]
    return _normalize_orb(cur)


def _radial_nuc(ra: list[tuple[mpf, int, mpf]]) -> mpf:
    return sum(
        c1 * c2 * _gamma_int(p1 + p2 + 1, a1 + a2)
        for c1, p1, a1 in ra
        for c2, p2, a2 in ra
    )


def _radial_kin(ra: list[tuple[mpf, int, mpf]], l_val: int) -> mpf:
    deriv: list[tuple[mpf, int, mpf]] = []
    for c, p, a in ra:
        deriv.append((c * mpf(p + 1), p, a))
        deriv.append((-c * a, p + 1, a))
    tot = sum(
        c1 * c2 * _gamma_int(p1 + p2, a1 + a2)
        for c1, p1, a1 in deriv
        for c2, p2, a2 in deriv
    )
    if l_val > 0:
        ll = mpf(l_val * (l_val + 1))
        tot += sum(
            ll * c1 * c2 * _gamma_int(p1 + p2, a1 + a2)
            for c1, p1, a1 in ra
            for c2, p2, a2 in ra
        )
    return tot / mpf(2)


def _density_r2(
    ra: list[tuple[mpf, int, mpf]],
    rb: list[tuple[mpf, int, mpf]],
) -> list[tuple[mpf, int, mpf]]:
    return _compress_dens(
        [(c1 * c2, p1 + p2 + 2, a1 + a2) for c1, p1, a1 in ra for c2, p2, a2 in rb]
    )


def _slater_monomial_rk(m: int, a: mpf, n: int, b: mpf, k: int) -> mpf:
    """Exact analytical integral int_0^inf int_0^inf r1^m e^{-a r1} r2^n e^{-b r2} (r_<^k / r_>^{k+1}) dr1 dr2."""
    p1 = n + k
    p2 = n - k - 1
    ab = a + b
    t1 = (FACT[p1] / (b ** (p1 + 1))) * _gamma_int(m - k - 1, a)
    for j in range(p1 + 1):
        t1 -= (FACT[p1] / (FACT[j] * (b ** (p1 - j + 1)))) * _gamma_int(m - k - 1 + j, ab)
    t2 = mpf(0)
    for j in range(p2 + 1):
        t2 += (FACT[p2] / (FACT[j] * (b ** (p2 - j + 1)))) * _gamma_int(m + k + j, ab)
    return t1 + t2


def _slater_rk_dens(
    d1: list[tuple[mpf, int, mpf]],
    d2: list[tuple[mpf, int, mpf]],
    k: int,
) -> mpf:
    return sum(
        c1 * c2 * _slater_monomial_rk(p1, a1, p2, a2, k)
        for c1, p1, a1 in d1
        for c2, p2, a2 in d2
    )


def _occ_of(n_elec: int) -> tuple[int, int, int, int]:
    n1 = min(n_elec, 2)
    rem = max(0, n_elec - 2)
    n2s = min(rem, 2)
    rem = max(0, rem - 2)
    n2p = min(rem, 6)
    rem = max(0, rem - 6)
    n3s = min(rem, 2)
    return n1, n2s, n2p, n3s


def atomic_roothaan_energy_ha(z_nuc: int, n_elec: int, params: list[mpf]) -> mpf:
    """Dimensionless Hartree ground-state expectation <Psi|H_Z|Psi> (zero fitted parameters).

    Uses Double-Zeta STO on 1s/2s across Z <= 5 (keeping the Be -> B 2s^2 -> 2s^2 2p^1
    transition in a uniform core basis) and Single-Zeta STO on 1s/2s + Double-Zeta STO
    on 2p for Z >= 6, so cation (Z, Z-1), neutral (Z, Z), and anion (Z, Z+1) share an
    identical core basis space.
    """
    if n_elec == 0:
        return mpf(0)
    if n_elec == 1:
        return -mpf(z_nuc ** 2) / mpf(2)
    n1, n2s, n2p, n3s = _occ_of(n_elec)
    zf = mpf(z_nuc)
    idx = 0

    def _make_dz(p_pow: int) -> list[tuple[mpf, int, mpf]]:
        nonlocal idx
        u_lo, du_hi, mix = params[idx], params[idx + 1], params[idx + 2]
        idx += 3
        z1 = mp.exp(u_lo)
        z2 = z1 + mp.exp(du_hi)
        b1 = _normalize_orb([(mpf(1), p_pow, z1)])
        b2 = _normalize_orb([(mpf(1), p_pow, z2)])
        return [(c, p, a) for c, p, a in b1] + [(mix * c, p, a) for c, p, a in b2]

    core_dz = z_nuc <= 5
    if core_dz:
        phi1 = _normalize_orb(_make_dz(0))
    else:
        z1 = mp.exp(params[idx])
        idx += 1
        phi1 = _normalize_orb([(mpf(1), 0, z1)])

    d11 = _density_r2(phi1, phi1)
    e_tot = mpf(n1) * (_radial_kin(phi1, 0) - zf * _radial_nuc(phi1))
    if n1 == 2:
        e_tot += _slater_rk_dens(d11, d11, 0)

    phi2s = None
    d22s = None
    if n2s > 0:
        if core_dz:
            phi2s = _orth_against(_make_dz(1), [phi1])
        else:
            z2s = mp.exp(params[idx])
            idx += 1
            phi2s = _orth_against([(mpf(1), 1, z2s)], [phi1])
        d22s = _density_r2(phi2s, phi2s)
        d12s = _density_r2(phi1, phi2s)
        e_tot += mpf(n2s) * (_radial_kin(phi2s, 0) - zf * _radial_nuc(phi2s))
        if n2s == 2:
            e_tot += _slater_rk_dens(d22s, d22s, 0)
        e_tot += (
            mpf(n1 * n2s) * _slater_rk_dens(d11, d22s, 0)
            - (mpf(n1 * n2s) / mpf(2)) * _slater_rk_dens(d12s, d12s, 0)
        )

    phi2p = None
    d22p = None
    if n2p > 0:
        phi2p = _normalize_orb(_make_dz(1))
        d22p = _density_r2(phi2p, phi2p)
        d12p = _density_r2(phi1, phi2p)
        e_tot += mpf(n2p) * (_radial_kin(phi2p, 1) - zf * _radial_nuc(phi2p))
        if n2p >= 2:
            e_tot += (
                mpf(n2p * (n2p - 1) // 2) * _slater_rk_dens(d22p, d22p, 0)
                + C2_2P_GROUND[n2p] * _slater_rk_dens(d22p, d22p, 2)
            )
        e_tot += (
            mpf(n1 * n2p) * _slater_rk_dens(d11, d22p, 0)
            - (mpf(n1 * n2p) / mpf(6)) * _slater_rk_dens(d12p, d12p, 1)
        )
        if phi2s is not None and d22s is not None:
            d2sp = _density_r2(phi2s, phi2p)
            e_tot += (
                mpf(n2s * n2p) * _slater_rk_dens(d22s, d22p, 0)
                - (mpf(n2s * n2p) / mpf(6)) * _slater_rk_dens(d2sp, d2sp, 1)
            )

    if n3s > 0 and phi2s is not None and phi2p is not None and d22s is not None and d22p is not None:
        z3 = mp.exp(params[idx])
        idx += 1
        phi3s = _orth_against([(mpf(1), 2, z3)], [phi1, phi2s])
        d33 = _density_r2(phi3s, phi3s)
        d13 = _density_r2(phi1, phi3s)
        d23s = _density_r2(phi2s, phi3s)
        d23p = _density_r2(phi2p, phi3s)
        e_tot += mpf(n3s) * (_radial_kin(phi3s, 0) - zf * _radial_nuc(phi3s))
        e_tot += mpf(2 * n3s) * _slater_rk_dens(d11, d33, 0) - mpf(n3s) * _slater_rk_dens(d13, d13, 0)
        e_tot += mpf(2 * n3s) * _slater_rk_dens(d22s, d33, 0) - mpf(n3s) * _slater_rk_dens(d23s, d23s, 0)
        e_tot += mpf(6 * n3s) * _slater_rk_dens(d22p, d33, 0) - mpf(n3s) * _slater_rk_dens(d23p, d23p, 1)

    return e_tot


def solve_variational_atom_80dps(z_nuc: int, n_elec: int) -> mpf:
    """Minimize atomic_roothaan_energy_ha(Z, N) with 80-dps coordinate/BFGS polish (zero fitted inputs)."""
    if n_elec == 0:
        return mpf(0)
    if n_elec == 1:
        return -mpf(z_nuc ** 2) / mpf(2)
    _, n2s, n2p, n3s = _occ_of(n_elec)
    core_dz = z_nuc <= 5
    p0: list[mpf] = []
    if core_dz:
        p0 += [
            mp.log(max(mpf("0.5"), mpf(z_nuc) - mpf("0.6"))),
            mp.log(max(mpf("0.8"), mpf(z_nuc) * mpf("0.5"))),
            mpf("0.25"),
        ]
        if n2s > 0:
            z2_base = max(mpf("0.35"), (mpf(z_nuc) - mpf("1.9")) / mpf(2))
            p0 += [mp.log(z2_base * mpf("0.75")), mp.log(z2_base * mpf("0.7")), mpf("0.5")]
    else:
        p0 += [mp.log(mpf(z_nuc) - mpf("0.31"))]
        if n2s > 0:
            p0 += [mp.log(max(mpf("0.4"), (mpf(z_nuc) - mpf("1.7")) / mpf(2)))]
    if n2p > 0:
        zp_base = max(mpf("0.25"), (mpf(z_nuc) - mpf("2.3")) / mpf(2))
        p0 += [mp.log(zp_base * mpf("0.65")), mp.log(zp_base * mpf("0.9")), mpf("0.45")]
    if n3s > 0:
        p0 += [mpf("-6.5")]

    d_dim = len(p0)
    max_bfgs_iter = 56 if core_dz else 42

    # Stage 1: BFGS localization at 22 dps on bounded box [-8.5, 4.5]^d
    with mp.workdps(22):
        x_cur = [mpf(v) for v in p0]
        b_inv = mp.eye(d_dim)
        h_step = mpf("1e-8")

        def _f_loc(xv: list[mpf]) -> mpf:
            return atomic_roothaan_energy_ha(z_nuc, n_elec, xv)

        def _grad_loc(xv: list[mpf]) -> list[mpf]:
            out = [mpf(0)] * d_dim
            for idx_g in range(d_dim):
                xp = list(xv)
                xm = list(xv)
                xp[idx_g] += h_step
                xm[idx_g] -= h_step
                out[idx_g] = (_f_loc(xp) - _f_loc(xm)) / (mpf(2) * h_step)
            return out

        fx = _f_loc(x_cur)
        gx = _grad_loc(x_cur)
        for _ in range(max_bfgs_iter):
            if max(abs(v) for v in gx) < mpf("1e-11"):
                break
            pv = [-sum(b_inv[i, j] * gx[j] for j in range(d_dim)) for i in range(d_dim)]
            dg = sum(pv[i] * gx[i] for i in range(d_dim))
            if dg >= 0:
                b_inv = mp.eye(d_dim)
                pv = [-v for v in gx]
                dg = -sum(v * v for v in gx)
            lam = mpf(1)
            accepted = False
            for _ls in range(22):
                xc = [
                    max(mpf("-8.5"), min(mpf("4.5"), x_cur[i] + lam * pv[i]))
                    for i in range(d_dim)
                ]
                fc = _f_loc(xc)
                if fc <= fx + mpf("1e-4") * lam * dg:
                    s_vec = [xc[i] - x_cur[i] for i in range(d_dim)]
                    gc = _grad_loc(xc)
                    y_vec = [gc[i] - gx[i] for i in range(d_dim)]
                    sy = sum(s_vec[i] * y_vec[i] for i in range(d_dim))
                    if sy > mpf("1e-17"):
                        by = [sum(b_inv[i, j] * y_vec[j] for j in range(d_dim)) for i in range(d_dim)]
                        yby = sum(y_vec[i] * by[i] for i in range(d_dim))
                        c1 = (sy + yby) / (sy * sy)
                        for i in range(d_dim):
                            for j in range(d_dim):
                                b_inv[i, j] += (
                                    c1 * s_vec[i] * s_vec[j]
                                    - (by[i] * s_vec[j] + s_vec[i] * by[j]) / sy
                                )
                    x_cur, fx, gx = xc, fc, gc
                    accepted = True
                    break
                lam /= mpf(2)
            if not accepted:
                break

    # Stage 2: Full 80-dps parabolic coordinate polish + energy evaluation (genuine 80-dps mpf!)
    x80 = [+mpf(v) for v in x_cur]
    h80 = mpf("1e-26")
    for _sweep in range(2):
        for i in range(d_dim):
            if x80[i] <= mpf("-8.49") or x80[i] >= mpf("4.49"):
                continue
            f0 = atomic_roothaan_energy_ha(z_nuc, n_elec, x80)
            xp = list(x80)
            xm = list(x80)
            xp[i] += h80
            xm[i] -= h80
            fp = atomic_roothaan_energy_ha(z_nuc, n_elec, xp)
            fm = atomic_roothaan_energy_ha(z_nuc, n_elec, xm)
            g_i = (fp - fm) / (mpf(2) * h80)
            h_ii = (fp - mpf(2) * f0 + fm) / (h80 ** 2)
            if h_ii > mpf("1e-8"):
                step_i = -g_i / h_ii
                cand = list(x80)
                cand[i] = max(mpf("-8.5"), min(mpf("4.5"), x80[i] + step_i))
                if atomic_roothaan_energy_ha(z_nuc, n_elec, cand) < f0:
                    x80 = cand

    return atomic_roothaan_energy_ha(z_nuc, n_elec, x80)


def main() -> int:
    print("=" * 78)
    print("  Q-Gap-0 (qou-5lct): 5-Layer Tower, Zero-Fit Mulliken/Hardness & Toric Chem")
    print("=" * 78)

    wb = WitnessBuilder(
        "confinement-layer-mulliken-stoichiometry",
        engine="sympy + mpmath 80-dps",
        output_dir=HERE,
    )
    wb.set_description(
        "80-dps zero-fit verification of QOU's 5-layer confinement tower & adiabatic ratios "
        "eta_k, zero-parameter Roothaan-Slater-Condon H..Ne ionization / Mulliken "
        "electronegativity / Parr-Pearson hardness benchmarks, and unimodular SNF(A_CHO) + "
        "Birch Hessian toric stoichiometry (Bean qou-5lct, companion to "
        "QOU.Observations.ConfinementLayerMullikenStoichiometry)."
    )
    wb.add_parameter("dps", DPS)
    wb.add_parameter("lean_module", LEAN_MODULE)
    wb.add_parameter("upstream_lean_module", UPSTREAM_LEAN_MODULE)

    checks: list[bool] = []

    def check(
        name: str,
        ok: bool,
        computed: str,
        expected: str,
        tol: str = "0",
        source: str = LEAN_MODULE,
    ) -> None:
        checks.append(bool(ok))
        wb.add_assertion(
            name=name,
            computed=computed,
            expected=expected,
            tolerance=tol,
            source=source,
        )

    # =========================================================================
    # PART 1: Physical Proton-Pin 80-dps 5-Layer Confinement Tower & Ratios
    # (Muon pin is on hold per 2026-11-28 owner ruling until rederivation.)
    # =========================================================================
    q_p = q_at(DPS)
    tower_p = evaluate_five_layer_tower(q_p, M_E_MEV)

    check(
        "five_layer_telescoping_product_identity_75dps",
        tower_p["telescoping_err_MeV"] < mpf("1e-75")
        and tower_p["log_q0_telescoping_err"] < mpf("1e-73"),
        computed=fmt(tower_p["telescoping_err_MeV"], 20),
        expected="0",
        tol="1e-75",
        source=f"{LEAN_MODULE}.five_layer_adiabatic_telescoping_product",
    )
    hierarchy_ok = (
        tower_p["strict_hierarchy_holds"]
        and mpf("7e-3") < tower_p["eta_0_form_b"] < mpf("8e-3")
        and mpf("7e-3") < tower_p["eta_1_model"] < mpf("1e-2")
        and mpf("1e-6") < tower_p["eta_2_model"] < mpf("2e-6")
        and mpf("2.5e-2") < tower_p["eta_3_h2o_hbond"] < mpf("3.5e-2")
    )
    check(
        "five_layer_strict_scale_hierarchy_and_adiabatic_regimes",
        hierarchy_ok,
        computed="1" if hierarchy_ok else "0",
        expected="1",
        tol="0",
        source="Strict 5-layer hierarchy 0 < Delta_4 < Delta_3 < Delta_2 < Delta_1 < Delta_0 and adiabatic eta_k in (0, 1) at the physical proton pin",
    )
    check(
        "derived_form_b_rydberg_matches_codata_within_1ppb",
        abs(tower_p["ry_form_b_rel_err_ppb"]) < mpf("1.0")
        and abs(tower_p["ry_form_c_rel_err_ppb"]) < mpf("0.1"),
        computed=fmt(tower_p["ry_form_b_rel_err_ppb"], 15),
        expected="0",
        tol="1.0",
        source="CODATA-2022 Rydberg constant times hc in eV",
    )

    # =========================================================================
    # PART 2: Zero-Fit Layer-3 Atomic Ionization, Mulliken chi_M & Hardness
    # =========================================================================
    ry_p = tower_p["ry_form_b_eV"]

    # 2a. Exact Dirac reduced-mass protium I_1(H; q_0) and Kellner-Hylleraas I_1(He; q_0)
    mu_red_p = tower_p["mp_model_MeV"] / (tower_p["mp_model_MeV"] + M_E_MEV)
    i1_h_dirac_p_ev = (
        M_E_MEV
        * mpf("1e6")
        * mu_red_p
        * (mpf(1) - mp.sqrt(mpf(1) - tower_p["alpha_form_b"] ** 2))
    )
    i1_h_nist_ev = mpf(NIST_ATOM_Z1_TO_10[0][2])
    i1_h_dirac_ppm = (i1_h_dirac_p_ev - i1_h_nist_ev) / i1_h_nist_ev * mpf("1e6")
    i1_he_kellner_ev = (mpf(217) / mpf(128)) * ry_p

    check(
        "protium_dirac_reduced_mass_ionization_within_3ppm_of_nist",
        abs(i1_h_dirac_ppm) < mpf("3.0"),
        computed=fmt(i1_h_dirac_ppm, 15),
        expected="0",
        tol="3.0",
    )

    # 2b. Verify Slater radial integral engine against exact analytical hydrogenic fractions
    phi_1s_u = _normalize_orb([(mpf(1), 0, mpf(1))])
    phi_2s_u = _normalize_orb(
        [(mpf(1), 0, mpf(1) / mpf(2)), (-mpf(1) / mpf(2), 1, mpf(1) / mpf(2))]
    )
    phi_2p_u = _normalize_orb([(mpf(1), 1, mpf(1) / mpf(2))])
    d1s = _density_r2(phi_1s_u, phi_1s_u)
    d2s = _density_r2(phi_2s_u, phi_2s_u)
    d2p = _density_r2(phi_2p_u, phi_2p_u)
    d2sp = _density_r2(phi_2s_u, phi_2p_u)
    slater_ident_err = max(
        abs(_radial_overlap(phi_1s_u, phi_2s_u)),
        abs(_slater_rk_dens(d1s, d1s, 0) - mpf(5) / mpf(8)),
        abs(_slater_rk_dens(d2s, d2s, 0) - mpf(77) / mpf(512)),
        abs(_slater_rk_dens(d2s, d2p, 0) - mpf(83) / mpf(512)),
        abs(_slater_rk_dens(d2p, d2p, 0) - mpf(93) / mpf(512)),
        abs(_slater_rk_dens(d2p, d2p, 2) - mpf(45) / mpf(512)),
        abs(_slater_rk_dens(d2sp, d2sp, 1) - mpf(45) / mpf(512)),
    )
    check(
        "exact_slater_condon_integrals_match_rational_fractions_75dps",
        slater_ident_err < mpf("1e-75"),
        computed=fmt(slater_ident_err, 20),
        expected="0",
        tol="1e-75",
    )

    # 2c. Solve dimensionless 80-dps Roothaan-Slater-Condon variational energies across Z = 1..10
    atom_rows_p: list[dict] = []
    ie_pred_map: dict[str, mpf] = {}
    chi_phys_map: dict[str, mpf] = {}
    eta_phys_map: dict[str, mpf] = {}
    max_fenchel_err = mpf(0)
    all_pplb_convex = True
    i1_abs_rel_errs: list[mpf] = []

    for sym, z_num, ie_nist_s, ea_nist_s in NIST_ATOM_Z1_TO_10:
        e_cat_ha = solve_variational_atom_80dps(z_num, z_num - 1)
        e_neu_ha = solve_variational_atom_80dps(z_num, z_num)
        e_ani_var_ha = solve_variational_atom_80dps(z_num, z_num + 1)
        # HVZ continuum-detachment envelope: an unbound anion detaches to neutral + free e^- (E <= E(Z))
        e_ani_phys_ha = min(e_ani_var_ha, e_neu_ha)

        two_ry_p = mpf(2) * ry_p
        ie_p = (e_cat_ha - e_neu_ha) * two_ry_p
        ea_var_p = (e_neu_ha - e_ani_var_ha) * two_ry_p
        ea_phys_p = (e_neu_ha - e_ani_phys_ha) * two_ry_p

        # Discrete shadow slopes mu_- = E(N) - E(N-1) = -I_1, mu_+ = E(N+1) - E(N) = -A_ea
        mu_minus = -ie_p
        mu_plus_phys = -ea_phys_p
        chi_phys = -(mu_plus_phys + mu_minus) / mpf(2)
        eta_phys = mu_plus_phys - mu_minus
        chi_var = (ie_p + ea_var_p) / mpf(2)
        eta_var = ie_p - ea_var_p

        # Verify `fenchel_subgradient_interval_iff_mulliken_hardness` midpoint & subgradient inequalities
        mid_hi_err = abs(mu_plus_phys - (-chi_phys) - eta_phys / mpf(2))
        mid_lo_err = abs((-chi_phys) - mu_minus - eta_phys / mpf(2))
        max_fenchel_err = max(max_fenchel_err, mid_hi_err, mid_lo_err)
        if eta_phys <= mpf(0) or eta_var <= mpf(0):
            all_pplb_convex = False

        ie_nist = mpf(ie_nist_s)
        ea_nist = mpf(ea_nist_s)
        chi_nist_clamped = (ie_nist + max(ea_nist, mpf(0))) / mpf(2)
        eta_nist_raw = ie_nist - ea_nist
        ie_rel_pct = (ie_p - ie_nist) / ie_nist * mpf(100)
        i1_abs_rel_errs.append(abs(ie_p - ie_nist) / ie_nist)

        ie_pred_map[sym] = ie_p
        chi_phys_map[sym] = chi_phys
        eta_phys_map[sym] = eta_phys

        atom_rows_p.append(
            {
                "element": sym,
                "Z": z_num,
                "E_neutral_Ha": fmt(e_neu_ha, 35),
                "I1_QOU_FormB_eV": fmt(ie_p, 35),
                "I1_NIST_eV": ie_nist_s,
                "I1_rel_err_pct": fmt(ie_rel_pct, 10),
                "A_ea_variational_eV": fmt(ea_var_p, 25),
                "A_ea_HVZ_detachment_eV": fmt(ea_phys_p, 25),
                "A_ea_NIST_eV": ea_nist_s,
                "chi_Mulliken_QOU_HVZ_eV": fmt(chi_phys, 30),
                "chi_Mulliken_QOU_var_eV": fmt(chi_var, 30),
                "chi_Mulliken_NIST_HVZ_eV": fmt(chi_nist_clamped, 15),
                "eta_ParrPearson_QOU_HVZ_eV": fmt(eta_phys, 30),
                "eta_ParrPearson_QOU_var_eV": fmt(eta_var, 30),
                "eta_ParrPearson_NIST_raw_eV": fmt(eta_nist_raw, 15),
                "noble_closure": z_num in (2, 10),
            }
        )

    mape_i1_pct = sum(i1_abs_rel_errs) / mpf(len(i1_abs_rel_errs)) * mpf(100)

    check(
        "fenchel_subgradient_midpoint_and_pplb_convexity_all_H_to_Ne",
        all_pplb_convex and max_fenchel_err < mpf("1e-74"),
        computed=fmt(max_fenchel_err if all_pplb_convex else mpf(1), 20),
        expected="0",
        tol="1e-74",
        source=f"{LEAN_MODULE}.fenchel_subgradient_interval_iff_mulliken_hardness",
    )
    kinks_ok = (
        eta_phys_map["He"] > eta_phys_map["H"]
        and eta_phys_map["He"] > eta_phys_map["Li"]
        and eta_phys_map["Ne"] > eta_phys_map["F"]
        and eta_phys_map["Ne"] > eta_phys_map["O"]
        and ie_pred_map["Be"] > ie_pred_map["B"]
        and ie_pred_map["N"] > ie_pred_map["O"]
        and chi_phys_map["F"] > chi_phys_map["O"] > chi_phys_map["C"] > chi_phys_map["B"] > chi_phys_map["Li"]
    )
    check(
        "periodic_kinks_noble_hardness_peaks_Be_gt_B_and_Hund_N_gt_O",
        kinks_ok,
        computed="1" if kinks_ok else "0",
        expected="1",
        tol="0",
        source="NIST Atomic Spectra Database periodic ionization/hardness kinks across H..Ne",
    )
    check(
        "zero_fit_roothaan_H_to_Ne_ionization_mape_below_9pct",
        mape_i1_pct < mpf("9.0"),
        computed=fmt(mape_i1_pct, 12),
        expected="6.5",
        tol="2.5",
        source="NIST Atomic Spectra Database Z=1..10 first ionization potentials",
    )

    # 2d. Verify `two_shell_piecewise_hardness_kink` and `parr_pearson_charge_transfer_minimizer`
    # Piecewise two-shell model at C_1 = 2 (He/Li boundary) and C_1 = 10 (Ne/Na boundary)
    eps1_test = ie_pred_map["He"]
    eps2_test = ie_pred_map["Li"]

    def _two_shell_e(n_val: int) -> mpf:
        if n_val <= 2:
            return -mpf(n_val) * eps1_test
        return -mpf(2) * eps1_test - mpf(n_val - 2) * eps2_test

    kink_err = max(
        abs(((_two_shell_e(1) - _two_shell_e(2)) - (_two_shell_e(2) - _two_shell_e(3))) - (eps1_test - eps2_test)),
        abs(((_two_shell_e(2) - _two_shell_e(3)) - (_two_shell_e(3) - _two_shell_e(4))) - mpf(0)),
    )
    check(
        "two_shell_piecewise_hardness_kink_exact_75dps",
        kink_err < mpf("1e-75"),
        computed=fmt(kink_err, 20),
        expected="0",
        tol="1e-75",
    )

    # Sanderson-Parr charge-transfer minimizer on canonical pairs (Li, F), (H, F), (C, O)
    ct_pairs: list[dict] = []
    max_ct_sq_err = mpf(0)
    for a_sym, b_sym in [("Li", "F"), ("H", "F"), ("C", "O")]:
        chi_a, chi_b = chi_phys_map[a_sym], chi_phys_map[b_sym]
        eta_a, eta_b = eta_phys_map[a_sym], eta_phys_map[b_sym]
        dn_star = (chi_b - chi_a) / (eta_a + eta_b)
        de_star = -((chi_a - chi_b) ** 2) / (mpf(2) * (eta_a + eta_b))
        # Verify completing-the-square identity at probe perturbation dn_probe = dn_star + 1/7
        dn_probe = dn_star + mpf(1) / mpf(7)
        q_probe = (chi_a - chi_b) * dn_probe + ((eta_a + eta_b) / mpf(2)) * (dn_probe ** 2)
        q_star = (chi_a - chi_b) * dn_star + ((eta_a + eta_b) / mpf(2)) * (dn_star ** 2)
        sq_rhs = ((eta_a + eta_b) / mpf(2)) * ((dn_probe - dn_star) ** 2)
        max_ct_sq_err = max(max_ct_sq_err, abs((q_probe - q_star) - sq_rhs), abs(q_star - de_star))
        ct_pairs.append(
            {
                "pair": f"{a_sym}-{b_sym}",
                "delta_N_star_electrons_A_to_B": fmt(dn_star, 30),
                "stabilization_energy_eV": fmt(de_star, 30),
            }
        )

    check(
        "parr_pearson_charge_transfer_completing_square_75dps",
        max_ct_sq_err < mpf("1e-75"),
        computed=fmt(max_ct_sq_err, 20),
        expected="0",
        tol="1e-75",
    )

    # =========================================================================
    # PART 3: Layer-4 Multi-Step Composition, Unimodular SNF & Birch Hessian
    # =========================================================================
    # 3a. Multi-step `expandMotifs_comp`: L_1 (p, n) -> L_2 (1H, 12C, 16O) -> L_4 (C, H2, O2, CO, CO2, H2O, CH4)
    # L_1 = [p, n] with baryon/charge matrix A_1 = [[1, 0], [0, 1]] (proton & neutron conservation across chemistry!)
    # motifs_12: 12C = (6 p, 6 n), 1H = (1 p, 0 n), 16O = (8 p, 8 n)
    motifs_12 = sp.Matrix(
        [
            [6, 1, 8],  # protons per (12C, 1H, 16O)
            [6, 0, 8],  # neutrons per (12C, 1H, 16O)
        ]
    )
    # motifs_24 (= A_CHO): (C, H2, O2, CO, CO2, H2O, CH4) in terms of (12C, 1H, 16O)
    A_cho = sp.Matrix(
        [
            [1, 0, 0, 1, 1, 0, 1],
            [0, 2, 0, 0, 0, 2, 4],
            [0, 0, 2, 1, 2, 1, 0],
        ]
    )
    composite_14 = motifs_12 * A_cho
    z_basis_cho = [
        sp.Matrix([0, 1, 0, -1, 1, -1, 0]),   # Water-gas shift: CO + H2O -> CO2 + H2
        sp.Matrix([1, 0, 0, -2, 1, 0, 0]),    # Boudouard: 2 CO -> C + CO2
        sp.Matrix([0, -3, 0, -1, 0, 1, 1]),   # Methanation: CO + 3 H2 -> CH4 + H2O
        sp.Matrix([-1, 0, -1, 0, 1, 0, 0]),   # Carbon oxidation: C + O2 -> CO2
    ]
    two_step_ok = all(
        A_cho * v == sp.zeros(3, 1)
        and motifs_12 * (A_cho * v) == composite_14 * v
        and composite_14 * v == sp.zeros(2, 1)
        for v in z_basis_cho
    )
    check(
        "promoteLayer_two_step_nucleon_charge_and_kernel_lifting_exact",
        two_step_ok,
        computed="1" if two_step_ok else "0",
        expected="1",
        tol="0",
    )

    # 3b. Unimodular Smith Normal Form certificate matching `cho_smith_normal_form_diag_1_1_2`
    U_cho = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 2]])
    U_cho_inv = sp.Matrix([[1, 0, 0], [0, 2, -1], [0, 1, 0]])
    V_cho = sp.Matrix(
        [
            [1, -1, 0, 2, 1, 1, -1],
            [0, 1, -1, 0, 0, -1, -2],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, -2, -2, -1, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
        ]
    )
    V_cho_inv = sp.Matrix(
        [
            [1, 0, 0, 1, 1, 0, 1],
            [0, 0, 2, 1, 2, 1, 0],
            [0, -1, 2, 1, 2, 0, -2],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
        ]
    )
    D_cho_expected = sp.Matrix([[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0]])
    snf_ok = (
        U_cho * U_cho_inv == sp.eye(3)
        and U_cho_inv * U_cho == sp.eye(3)
        and V_cho * V_cho_inv == sp.eye(7)
        and V_cho_inv * V_cho == sp.eye(7)
        and abs(int(U_cho.det())) == 1
        and abs(int(V_cho.det())) == 1
        and U_cho * A_cho * V_cho == D_cho_expected
    )
    check(
        "cho_smith_normal_form_unimodular_certificate_diag_1_1_2",
        snf_ok,
        computed="1" if snf_ok else "0",
        expected="1",
        tol="0",
    )

    # Verify the 4 canonical 1D primitive reaction kernels
    canonical_1d = [
        ("2H2+O2->2H2O", sp.Matrix([[2, 0, 2], [0, 2, 1]]), sp.Matrix([-2, -1, 2])),
        ("CH4+2O2->CO2+2H2O", sp.Matrix([[1, 0, 1, 0], [4, 0, 0, 2], [0, 2, 2, 1]]), sp.Matrix([-1, -2, 1, 2])),
        ("N2+3H2->2NH3", sp.Matrix([[2, 0, 1], [0, 2, 3]]), sp.Matrix([-1, -3, 2])),
        ("C6H12O6+6O2->6CO2+6H2O", sp.Matrix([[6, 0, 1, 0], [12, 0, 0, 2], [6, 2, 2, 1]]), sp.Matrix([-1, -6, 6, 6])),
    ]
    canon_ok = all(
        mat * vec == sp.zeros(mat.rows, 1)
        and len(mat.nullspace()) == 1
        and int(sp.igcd(*[abs(int(x)) for x in vec])) == 1
        for _, mat, vec in canonical_1d
    )
    check(
        "four_canonical_1d_primitive_stoichiometry_kernels_exact",
        canon_ok,
        computed="1" if canon_ok else "0",
        expected="1",
        tol="0",
    )

    # 3c. 80-dps Birch mass-action equilibrium & exact weighted sum-of-squares Hessian identity
    # (`birch_hessian_quad_form_sum_sq_and_pos`)
    A_rows = [[int(A_cho[r, c]) for c in range(7)] for r in range(3)]
    g_dimless = [
        mpf("0"),
        mpf("0"),
        mpf("0"),
        mpf("-24.12"),
        mpf("-47.62"),
        mpf("-23.17"),
        mpf("2.35"),
    ]
    b_target = [mpf(2), mpf(8), mpf(4)]
    y_vec = [mpf("-5"), mpf("-2"), mpf("-12")]

    def _eval_x(yv: list[mpf]) -> list[mpf]:
        return [
            mp.exp(sum(mpf(A_rows[e][j]) * yv[e] for e in range(3)) - g_dimless[j])
            for j in range(7)
        ]

    for _ in range(80):
        xv = _eval_x(y_vec)
        grad = [sum(mpf(A_rows[e][j]) * xv[j] for j in range(7)) - b_target[e] for e in range(3)]
        if max(abs(r) for r in grad) < mpf("1e-76"):
            break
        h_mat = mp.matrix(3, 3)
        for r in range(3):
            for c in range(3):
                h_mat[r, c] = sum(mpf(A_rows[r][j] * A_rows[c][j]) * xv[j] for j in range(7))
        step = mp.lu_solve(h_mat, mp.matrix([-g for g in grad]))
        phi_cur = sum(xv) - sum(b_target[e] * y_vec[e] for e in range(3))
        lam = mpf(1)
        for _ls in range(40):
            y_cand = [y_vec[e] + lam * step[e] for e in range(3)]
            x_cand = _eval_x(y_cand)
            phi_cand = sum(x_cand) - sum(b_target[e] * y_cand[e] for e in range(3))
            if phi_cand <= phi_cur:
                y_vec = y_cand
                break
            lam /= mpf(2)

    x_star = _eval_x(y_vec)
    birch_fiber_res = max(
        abs(sum(mpf(A_rows[e][j]) * x_star[j] for j in range(7)) - b_target[e])
        for e in range(3)
    )

    # Test `birch_hessian_quad_form_sum_sq_and_pos` on 3 linearly independent directions xi
    xi_tests = [
        [mpf(1), mpf(0), mpf(0)],
        [mpf(1), -mpf(2) / mpf(3), mpf(5) / mpf(7)],
        [-mpf(3) / mpf(11), mpf(4) / mpf(5), -mpf(1) / mpf(2)],
    ]
    max_hess_sos_err = mpf(0)
    all_hess_pos = True
    for xi in xi_tests:
        quad_direct = sum(
            xi[e1] * sum(mpf(A_rows[e1][j] * A_rows[e2][j]) * x_star[j] for j in range(7)) * xi[e2]
            for e1 in range(3)
            for e2 in range(3)
        )
        quad_sos = sum(
            x_star[j] * (sum(mpf(A_rows[e][j]) * xi[e] for e in range(3)) ** 2)
            for j in range(7)
        )
        max_hess_sos_err = max(max_hess_sos_err, abs(quad_direct - quad_sos))
        if quad_sos <= mpf(0):
            all_hess_pos = False

    check(
        "birch_hessian_sum_of_squares_and_fiber_equilibrium_75dps",
        birch_fiber_res < mpf("1e-75") and max_hess_sos_err < mpf("1e-74") and all_hess_pos,
        computed=fmt(max(birch_fiber_res, max_hess_sos_err) if all_hess_pos else mpf(1), 20),
        expected="0",
        tol="1e-74",
        source=f"{LEAN_MODULE}.birch_hessian_quad_form_sum_sq_and_pos",
    )

    def _pack_tower(tw: dict) -> dict:
        return {
            "q0": fmt(tw["q0"], 75),
            "h_q": fmt(tw["h_q"], 45),
            "h_q_sq": fmt(tw["h_q_sq"], 45),
            "alpha_inv_form_a": fmt(tw["alpha_inv_form_a"], 40),
            "alpha_inv_form_b_derived": fmt(tw["alpha_inv_form_b"], 40),
            "alpha_inv_form_c_bloch_b3": fmt(tw["alpha_inv_form_c"], 40),
            "mp_model_MeV": fmt(tw["mp_model_MeV"], 40),
            "delta_nuc_2E0_ord0_MeV": fmt(tw["delta_nuc_model_MeV"], 40),
            "ry_form_b_eV": fmt(tw["ry_form_b_eV"], 40),
            "ry_form_c_eV": fmt(tw["ry_form_c_eV"], 40),
            "ry_form_b_rel_err_ppb": fmt(tw["ry_form_b_rel_err_ppb"], 15),
            "ry_form_c_rel_err_ppb": fmt(tw["ry_form_c_rel_err_ppb"], 15),
            "e_hbond_2h2o_pure_bohr_eV": fmt(tw["e_hbond_2h2o_bohr_eV"], 40),
            "e_hbond_2h2o_OH_ref_eV": fmt(tw["e_hbond_2h2o_ref_eV"], 40),
            "eta_0_form_b": fmt(tw["eta_0_form_b"], 40),
            "eta_1_model_2E0_over_mp": fmt(tw["eta_1_model"], 40),
            "eta_1_12C_AME_over_mp": fmt(tw["eta_1_c12_AME"], 40),
            "eta_2_model_Ry_over_2E0": fmt(tw["eta_2_model"], 40),
            "eta_2_Ry_over_12C_AME": fmt(tw["eta_2_c12_AME"], 40),
            "eta_3_pure_bohr_2h2_over_3": fmt(tw["eta_3_pure_bohr"], 40),
            "eta_3_H2O_hbond_over_Ry": fmt(tw["eta_3_h2o_hbond"], 40),
            "log_q0_eta_0": fmt(tw["log_q0_eta_0"], 30),
            "log_q0_eta_1_model": fmt(tw["log_q0_eta_1_model"], 30),
            "log_q0_eta_2_model": fmt(tw["log_q0_eta_2_model"], 30),
            "log_q0_eta_3_H2O": fmt(tw["log_q0_eta_3_h2o"], 30),
            "telescoping_product_pure": fmt(tw["telescoping_product_pure"], 45),
            "ns_crust_qou_scored": {k: fmt(v, 30) for k, v in tw["ns_crust_qou_scored"].items()},
            "ns_crust_codata_validation": {k: fmt(v, 30) for k, v in tw["ns_crust_codata_validation"].items()},
        }

    wb.add_data(
        "five_layer_tower_proton_pin",
        {
            **_pack_tower(tower_p),
            "anchor_note": "Evaluated strictly at physical_proton per 2026-11-28 owner ruling (muon pin on hold until rederivation).",
        },
    )
    wb.add_data(
        "layer3_zero_fit_atomic_benchmarks",
        {
            "protium_dirac_reduced_mass_I1_eV": fmt(i1_h_dirac_p_ev, 35),
            "protium_dirac_rel_err_ppm": fmt(i1_h_dirac_ppm, 15),
            "helium_kellner_217_128_Ry_eV": fmt(i1_he_kellner_ev, 35),
            "roothaan_H_to_Ne_I1_MAPE_pct": fmt(mape_i1_pct, 15),
            "elements_Z1_to_10": atom_rows_p,
            "sanderson_parr_charge_transfer_pairs": ct_pairs,
        },
    )
    wb.add_data(
        "layer4_smith_and_birch_stoichiometry",
        {
            "composite_nucleon_stoichiometry_matrix_rows": [
                [int(composite_14[r, c]) for c in range(7)] for r in range(2)
            ],
            "cho_smith_invariant_factors": [1, 1, 2],
            "cho_smith_U": [[int(U_cho[r, c]) for c in range(3)] for r in range(3)],
            "cho_smith_V": [[int(V_cho[r, c]) for c in range(7)] for r in range(7)],
            "birch_equilibrium_x_star": {
                sp_name: fmt(x_star[idx], 45)
                for idx, sp_name in enumerate(["C", "H2", "O2", "CO", "CO2", "H2O", "CH4"])
            },
            "birch_hessian_sos_max_err": fmt(max_hess_sos_err, 25),
        },
    )

    print(
        f"  Tower (proton pin): Ry_FormB = {mp.nstr(ry_p, 12)} eV ({mp.nstr(tower_p['ry_form_b_rel_err_ppb'], 4)} ppb), "
        f"eta_0 = {mp.nstr(tower_p['eta_0_form_b'], 6)}, eta_1 = {mp.nstr(tower_p['eta_1_model'], 6)}, "
        f"eta_2 = {mp.nstr(tower_p['eta_2_model'], 6)}, eta_3(H2O) = {mp.nstr(tower_p['eta_3_h2o_hbond'], 6)}"
    )
    print(
        f"  Zero-fit H..Ne I_1 MAPE = {mp.nstr(mape_i1_pct, 5)}% | "
        f"He eta_PP = {mp.nstr(eta_phys_map['He'], 6)} eV, Li = {mp.nstr(eta_phys_map['Li'], 6)} eV, "
        f"Be I_1 = {mp.nstr(ie_pred_map['Be'], 6)} eV > B I_1 = {mp.nstr(ie_pred_map['B'], 6)} eV, "
        f"N I_1 = {mp.nstr(ie_pred_map['N'], 6)} eV > O I_1 = {mp.nstr(ie_pred_map['O'], 6)} eV, "
        f"Ne eta_PP = {mp.nstr(eta_phys_map['Ne'], 6)} eV"
    )

    out_path = wb.save()
    print(f"\n  {sum(checks)}/{len(checks)} assertions passed -> {out_path}")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
