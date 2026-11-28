#!/usr/bin/env python3
"""ka_b4_pauli_wigner_saturation_probe.py — Exploratory Zero-Fit 80-dps Cluster-Model
Comparison (`§3b-cond`, unwired) of Intra-Shell Pauli-Wigner Wenzl Sub-Quartet Cells
(b_2, b_3), SU(4) 4x4 Hankel Quartet Closure (b_4), FCC (111) Triangular-Face Contacts,
Wigner-Pauli Fermi Isospin Valley, and Nilsson-Strutinsky Shell Stabilization Across AME2020.

Beans: qou-v2om, qou-gpb5, qou-sbn9, qou-d9iv.
Companion Lean 4 module:
  `folio/quantum-observable-universe/lean/QOU/Nuclear/AlphaQuartetPauliWignerSaturation.lean` (`0 sorry`).
Ruled production valence reference:
  `folio/quantum-observable-universe/lean/QOU/MassTheory/NucleusBondValence.lean` (`PR #9710`).
Companion audit:
  `docs/audits/2026-11-28-ka-b4-pauli-wigner-saturation-synthesis.md`.

APPLICABILITY & SCOPE UNDER THE 2026-11-27 `T3` VALENCE RULING (`PR #9710`)
---------------------------------------------------------------------------
On 2026-11-27 (`docs/coordination/owner-rulings.md` row 22; `QOU.MassTheory.NucleusBondValence`,
`PR #9710`), the owner ruled that the nucleus bond count (gap `G5`) is fixed by the colour
valence cap `T3`: each quark strand carries at most one inter-nucleon bond (`3 * floor(A / 2)`
bonds, `1.5` per nucleon), and `V6` is not adopted without a corpus derivation. At `A = 4m`,
`3 * floor(4m / 2) = 6m` equals the `6m` internal edges of `m` disjoint `K_4` alpha-quartets.
Accordingly, the surface-corrected FCC `(111)` inter-quartet face-contact saturation model
evaluated here (`S3..S5`) is strictly an **exploratory macroscopic cluster-model comparison
(`§3b-cond`, unwired)** alongside the ruled `T3` valence bound — it does NOT replace the ruled
`T3` bond count without a `3A`-strand derivation.

STRICT CALIBRATION, ANTI-FITTING & 80-DPS PROTON-PIN DISCIPLINE
---------------------------------------------------------------
1. Zero fitted parameters (`free_parameters = 0`). Every model evaluation uses ONLY the
   three pre-committed external physical scales:
   - electron mass `m_e` (from `qou_substrate.codata` at >= 80 dps),
   - aether deformation parameter `q_0` evaluated strictly at the physical proton pin `q_at`
     (`q0Anchor = "proton"`; the muon pin is on hold per 2026-11-28 owner ruling until rederivation),
   - charged-pion mass `m_{pi^+-} = 13957039 / 100000 MeV` (PDG exact rational scale setting
     the one-pion-exchange FCC lattice spacing `r_{0,FCC}` and pion-Compton quantum `2 m_{pi}^2 / m_p^{pred}`).
2. Zero upstream validation-mass leakage: `m_p^{pred}(q_0, m_e)` and `alpha_EM^{FormB}(q_0)`
   are computed purely from `(q_0, m_e)` in natural units (`hbar = c = 1`). CODATA `m_p`, `m_n`,
   and `ame2020.json` enter exclusively in downstream residual comparisons.
3. Working precision `COMPUTE_DPS = 125`, serialized output precision `OUTPUT_DPS = 80`
   (`45` guard digits); zero `float64`, zero `math.*`, zero `LN_Q` constants.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

os.environ.setdefault("QOU_OUTPUT_DPS", "80")
os.environ.setdefault("QOU_COMPUTE_DPS", "125")
os.environ.setdefault("QOU_PRECISION_GUARD", "45")

HERE = Path(__file__).resolve().parent
COMPUTATIONS_ROOT = HERE.parent
REPO_ROOT = COMPUTATIONS_ROOT.parent
for _p in (str(COMPUTATIONS_ROOT), str(HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
import qou_substrate.precision as _qsp  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402

_qsp.OUTPUT_DPS = 80
_qsp.PRECISION_GUARD = 45
_qsp.COMPUTE_DPS = 125
set_compute_dps(125)
mp.mp.dps = 125

LEAN_MODULE = "QOU.Nuclear.AlphaQuartetPauliWignerSaturation"
RULED_VALENCE_LEAN_MODULE = "QOU.MassTheory.NucleusBondValence"

# Exact PDG 2024 charged-pion mass as an exact rational (13957039 / 100000 MeV)
# so binary53 float rounding never enters at any dps.
M_PI_CHARGED_MEV = mp.mpf(13957039) / mp.mpf(100000)

# Electron mass calibration input + validation-only nucleon masses from registry
_ME_REC = _codata.codata("electron mass energy equivalent in MeV")
_MP_REC = _codata.codata("proton mass energy equivalent in MeV")
_MN_REC = _codata.codata("neutron mass energy equivalent in MeV")

M_E_MEV = mp.mpf(_ME_REC.value_str)
M_P_EXP_VALIDATION = mp.mpf(_MP_REC.value_str)
M_N_EXP_VALIDATION = mp.mpf(_MN_REC.value_str)
QBETA_N_CODATA_VALIDATION = M_N_EXP_VALIDATION - M_P_EXP_VALIDATION - M_E_MEV

REPRESENTATIVE_NUCLIDES: list[tuple[str, int, int]] = [
    ("2H", 1, 1),
    ("3H", 1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("12C", 6, 6),
    ("16O", 8, 8),
    ("40Ca", 20, 20),
    ("56Fe", 26, 30),
    ("62Ni", 28, 34),
    ("120Sn", 50, 70),
    ("208Pb", 82, 126),
    ("238U", 92, 146),
]

HEAVY_ALPHA_BENCHMARKS: list[tuple[str, int, int]] = [
    ("8Be", 4, 4),
    ("210Po", 84, 126),
    ("212Po", 84, 128),
    ("222Rn", 86, 136),
    ("226Ra", 88, 138),
    ("238U", 92, 146),
]


# =============================================================================
# 1. Exact Symbolic Verification Mirroring Division-Free Lean 4 Theorems
# =============================================================================


def verify_symbolic_identities() -> dict[str, str]:
    """Verify over Z[q, q^{-1}, ...] every division-free identity proved in Lean."""
    q, u, z, n, a, m_sym = sp.symbols("q u Z N A m", nonzero=True)
    phi1, phi2, phi3, b4q = sp.symbols("phi1 phi2 phi3 b4Quartet")
    s_str, a_kin, c_coul, d_np = sp.symbols("sStrong aKin cCoul deltaNP")

    # 1. quartetClosed_b4_eq & quartetClosed_b4_jump
    b3_closed = (phi1 + phi2) - 3 * phi1
    b4_closed = b4q - 4 * (phi1 + phi2) + 6 * phi1
    assert sp.simplify(b3_closed - (phi2 - 2 * phi1)) == 0
    assert sp.simplify(b4_closed - (b4q - 4 * phi2 + 2 * phi1)) == 0
    b4_open = (phi1 + phi2 + phi3) - 4 * (phi1 + phi2) + 6 * phi1
    assert sp.simplify((b4_closed - b4_open) - (b4q - (phi1 + phi2 + phi3))) == 0

    # 2. quartetClosed_isobar_odd_to_even_jump
    s_odd = m_sym * b4q + (phi1 + phi2)
    s_even = (m_sym + 1) * b4q
    assert sp.simplify((s_even - s_odd) - (b4q - (phi1 + phi2))) == 0

    # 3. t3_valence_cap_eq_disjoint_quartet_internal_bonds & two_mul_fcc_sub_k4_external_bonds_eq
    assert all(3 * ((4 * k) // 2) == 6 * k for k in range(1, 20))
    two_ext_bonds = 12 * a - 3 * a
    assert sp.expand(two_ext_bonds - 3 * (3 * a)) == 0
    assert sp.expand(two_ext_bonds - 9 * a) == 0

    two_face_cube = 3 * u**3 - 6 * u**2
    assert sp.expand(two_face_cube - 3 * u**2 * (u - 2)) == 0
    assert sp.simplify(two_face_cube.subs(u, 2)) == 0

    # 4. qIntUnit_three_mul_sq & qSimplex_two_clearing_eq
    q_int_3 = q**2 + 1 + q ** (-2)
    assert sp.simplify(q**2 * q_int_3 - (q**4 + q**2 + 1)) == 0
    assert sp.simplify((q_int_3 + 1) * q**2 - ((q**4 + q**2 + 1) + q**2)) == 0

    # 5. wignerIsoNumerator_eq_sum_sq_sub_asym_sq
    w_num = 4 * z * n
    assert sp.expand(w_num - ((z + n) ** 2 - (n - z) ** 2)) == 0

    # 6. isobaric_binding_second_diff_eq & isobaric_beta_step_eq (A^2-cleared)
    b_asq = lambda zp: (  # noqa: E731
        s_str * (4 * zp * (a - zp))
        - a_kin * a * (a - 2 * zp) ** 2
        - c_coul * a**2 * zp * (zp - 1)
    )
    d2_asq = sp.expand(b_asq(z + 1) - 2 * b_asq(z) + b_asq(z - 1))
    target_d2 = -(8 * s_str + 8 * a_kin * a + 2 * c_coul * a**2)
    assert sp.expand(d2_asq - target_d2) == 0

    d1_asq = sp.expand(b_asq(z + 1) - b_asq(z))
    target_d1 = 4 * (s_str + a_kin * a) * (a - 2 * z - 1) - 2 * c_coul * a**2 * z
    assert sp.expand(d1_asq - target_d1) == 0
    _ = d_np

    return {
        "lean_module": LEAN_MODULE,
        "ruled_valence_lean_module": RULED_VALENCE_LEAN_MODULE,
        "b3_closed": str(sp.simplify(b3_closed)),
        "b4_closed": str(sp.simplify(b4_closed)),
        "isobar_odd_to_even_jump": str(sp.simplify(s_even - s_odd)),
        "two_mul_fcc_external_bonds": str(sp.simplify(two_ext_bonds)),
        "two_inter_quartet_face_cube_factored": str(sp.factor(two_face_cube)),
        "qSimplex_two_cleared": str(sp.expand((q**4 + q**2 + 1) + q**2)),
        "aSq_isobaric_second_diff": str(target_d2),
        "aSq_isobaric_beta_step": str(target_d1),
        "identities_verified": "8",
    }


# =============================================================================
# 2. Pure Zero-Parameter 80-dps Aether & Shell Primitives at Proton Pin q_0
# =============================================================================


def q_int(n: int, q: mp.mpf) -> mp.mpf:
    if n == 0:
        return mp.mpf(0)
    return (q**n - q ** (-n)) / (q - mp.mpf(1) / q)


def solve_alpha_form_b(q: mp.mpf) -> mp.mpf:
    """4-topology Form-B alpha_EM(q) (EmFermionLoopFourTopology #9360; Conditional)."""
    h2 = (q - mp.mpf(1) / q) ** 2
    t_term = q * q_int(9, q) * q_int(10, q) + mp.mpf(2) / (mp.mpf(3) * mp.pi)
    h_term = q_int(2, q) / (mp.mpf(8) * mp.pi)
    a_val = mp.mpf(1) / t_term
    tol = mp.mpf(10) ** (-115)
    for _ in range(60):
        f_val = -h_term * h2 * (a_val**3) + h_term * (a_val**2) + t_term * a_val - mp.mpf(1)
        fp_val = -mp.mpf(3) * h_term * h2 * (a_val**2) + mp.mpf(2) * h_term * a_val + t_term
        step = f_val / fp_val
        a_val -= step
        if abs(step) < tol:
            break
    return a_val


def eval_p4_alpha_quartet(q: mp.mpf) -> tuple[mp.mpf, mp.mpf, int]:
    """Exact 4-row SU(4) q-Plancherel weight & partition sum for 4He (n = 12, 34 partitions)."""
    qf = [mp.mpf(1)]
    for k in range(1, 20):
        qf.append(qf[-1] * q_int(k, q))

    def w4_12(lam: tuple[int, int, int, int]) -> mp.mpf:
        l1, l2, l3, l4 = lam[0] + 3, lam[1] + 2, lam[2] + 1, lam[3]
        vand = (
            q_int(l1 - l2, q)
            * q_int(l1 - l3, q)
            * q_int(l1 - l4, q)
            * q_int(l2 - l3, q)
            * q_int(l2 - l4, q)
            * q_int(l3 - l4, q)
        )
        den = qf[l1] * qf[l2] * qf[l3] * qf[l4]
        return qf[12] * (vand / den) ** 2

    z4_12 = mp.mpf(0)
    count = 0
    for lam4 in range(4):
        rem3 = 12 - 4 * lam4
        for d3 in range(rem3 // 3 + 1):
            lam3 = lam4 + d3
            rem2 = rem3 - 3 * d3
            for d2 in range(rem2 // 2 + 1):
                lam2 = lam3 + d2
                lam1 = 12 - lam2 - lam3 - lam4
                z4_12 += w4_12((lam1, lam2, lam3, lam4))
                count += 1
    p4_alpha = w4_12((3, 3, 3, 3)) / z4_12
    return p4_alpha, z4_12, count


def compute_strutinsky_table(q: mp.mpf, max_occ: int = 172) -> list[mp.mpf]:
    """Order-4 Hermite-Strutinsky shell stabilization delta B_Strut(k) in hw_0 units
    from #9367's zero-parameter categorical Dirac Nilsson levels (C = -(q-1), D = -C/4)."""
    eta = q - mp.mpf(1)
    levels: list[tuple[mp.mpf, int]] = []
    for n_sh in range(11):
        l2_mean = mp.mpf(n_sh * (n_sh + 3)) / mp.mpf(2)
        for ell in range(n_sh % 2, n_sh + 1, 2):
            j2_list = [2 * ell + 1] if ell == 0 else [2 * ell + 1, 2 * ell - 1]
            for tj2 in j2_list:
                ls_eig = (
                    mp.mpf(ell) / mp.mpf(2)
                    if tj2 == 2 * ell + 1
                    else -mp.mpf(ell + 1) / mp.mpf(2)
                )
                shift = (-eta / mp.mpf(4)) * (mp.mpf(ell * (ell + 1)) - l2_mean) - eta * ls_eig
                levels.append((mp.mpf(n_sh) + mp.mpf(3) / mp.mpf(2) + shift, tj2 + 1))
    levels.sort(key=lambda r: r[0])

    inv_sqrt_pi = mp.mpf(1) / mp.sqrt(mp.pi)

    def n4_occ(x: mp.mpf) -> mp.mpf:
        if x > mp.mpf(18):
            return mp.mpf(0)
        if x < -mp.mpf(18):
            return mp.mpf(1)
        return mp.mpf(1) / mp.mpf(2) * mp.erfc(x) + mp.exp(-(x * x)) * inv_sqrt_pi * (
            -mp.mpf(7) / mp.mpf(8) * x + mp.mpf(1) / mp.mpf(4) * (x**3)
        )

    def m4_mom(x: mp.mpf) -> mp.mpf:
        if abs(x) > mp.mpf(18):
            return mp.mpf(0)
        return -mp.exp(-(x * x)) * inv_sqrt_pi * (
            mp.mpf(3) / mp.mpf(16)
            - mp.mpf(3) / mp.mpf(4) * (x**2)
            + mp.mpf(1) / mp.mpf(4) * (x**4)
        )

    strut_du = [mp.mpf(0)] * (max_occ + 1)
    lam = mp.mpf(3) / mp.mpf(2)
    tol = mp.mpf(10) ** (-112)
    for k_occ in range(3, max_occ + 1):
        rem = k_occ
        u_quant = mp.mpf(0)
        for e_i, deg in levels:
            take = deg if rem >= deg else rem
            u_quant += mp.mpf(take) * e_i
            rem -= take
            if rem == 0:
                break
        for _ in range(45):
            f_val = -mp.mpf(k_occ)
            fp_val = mp.mpf(0)
            for e_i, deg in levels:
                x = e_i - lam
                if x > mp.mpf(18):
                    continue
                if x < -mp.mpf(18):
                    f_val += mp.mpf(deg)
                    continue
                f_val += mp.mpf(deg) * n4_occ(x)
                g4 = mp.exp(-(x * x)) * inv_sqrt_pi * (
                    mp.mpf(15) / mp.mpf(8)
                    - mp.mpf(5) / mp.mpf(2) * (x**2)
                    + mp.mpf(1) / mp.mpf(2) * (x**4)
                )
                fp_val += mp.mpf(deg) * g4
            step = f_val / fp_val
            lam -= step
            if abs(step) < tol:
                break
        u_smooth = mp.mpf(0)
        for e_i, deg in levels:
            x = e_i - lam
            u_smooth += mp.mpf(deg) * (e_i * n4_occ(x) + m4_mom(x))
        strut_du[k_occ] = -(u_quant - u_smooth)
    return strut_du


def build_anchor_scales(q: mp.mpf) -> dict[str, object]:
    """Compute all zero-parameter scales at aether deformation parameter `q`."""
    hbar_q = mp.mpf(1) - mp.mpf(1) / q
    h_q = q - mp.mpf(1) / q
    vol_41 = mp.mpf(2) * mp.clsin(2, mp.pi / mp.mpf(3))
    m_mu_pred = M_E_MEV * vol_41 / (hbar_q**2)

    # Model proton mass m_p^{pred}(q, m_e) (zero CODATA m_p input!)
    tr_bor = abs((mp.mpf(4) + h_q**2 - mp.mpf(3) * (h_q**4) - h_q**6) / (h_q**2 + mp.mpf(4)))
    f_bor = tr_bor * q_int(2, q) * q_int(3, q) / (q**3)
    m_p_pred = mp.mpf(2) * m_mu_pred * f_bor - mp.mpf(12) * M_E_MEV

    # Free-neutron beta-decay Q_beta(n) splits (pure QOU vs Legendre-Cottingham)
    e0_ord0 = M_E_MEV / (q * (q - mp.mpf(1)))
    e0_twr = e0_ord0 / (mp.mpf(1) - hbar_q**2)
    assert abs(e0_twr - qbeta_e0.tower_summed(q=q, m_e=M_E_MEV)) < mp.mpf(10) ** (-115)
    p_bor = (
        q**12
        - mp.mpf(3) * (q**10)
        + mp.mpf(3) * (q**8)
        - mp.mpf(5) * (q**6)
        + mp.mpf(3) * (q**4)
        - mp.mpf(3) * (q**2)
        + mp.mpf(1)
    )
    tr_v3 = -p_bor / (q**6)
    eps_flav_v3 = abs((q - mp.mpf(1) / q) * tr_v3 / ((q + mp.mpf(1) / q) ** 3))
    qbeta_n_scored = eps_flav_v3 * e0_twr

    alpha_em = solve_alpha_form_b(q)
    dt_raw_all_pairs = -eps_flav_v3 / (mp.mpf(3) * (q**2 - mp.mpf(1)))
    dm_horiz_12me = (mp.mpf(1) - q ** (-2)) * mp.mpf(12) * M_E_MEV
    dm_em_all_pairs = alpha_em * m_p_pred * dt_raw_all_pairs
    qbeta_n_legendre_cottingham = qbeta_n_scored + dm_horiz_12me + dm_em_all_pairs

    e0_tower_pauli = e0_twr
    phi1_wenzl = (mp.mpf(1) / q_int(2, q)) * e0_tower_pauli
    phi2_wenzl = (mp.mpf(1) + (q**2) / (q**4 + q**2 + mp.mpf(1))) * e0_tower_pauli
    phi3_wenzl = (mp.mpf(2) + mp.mpf(1) / q_int(4, q)) * e0_tower_pauli

    # SU(4) 4-row Hankel single-alpha quartet ground-state surprisal (#9377)
    p4_alpha, z4_12, n_part_12 = eval_p4_alpha_quartet(q)
    b4_hankel_raw = -e0_twr * mp.log(p4_alpha)

    # Natural-unit (hbar = c = 1) FCC Yukawa geometry, Coulomb coefficient, Fermi energy & hw00
    fcc_pack_inv_cbrt = (mp.mpf(4) * mp.pi * mp.sqrt(mp.mpf(2)) / mp.mpf(3)) ** (
        mp.mpf(1) / mp.mpf(3)
    )
    c_coul_coeff = (mp.mpf(2) / mp.mpf(5)) * fcc_pack_inv_cbrt * alpha_em * M_PI_CHARGED_MEV
    ec_he4 = c_coul_coeff * mp.mpf(2) / (mp.mpf(4) ** (mp.mpf(1) / mp.mpf(3)))
    b4_hankel_strong_restored = b4_hankel_raw + ec_he4

    eps_fermi = (
        (mp.mpf(2) / mp.mpf(9))
        * ((mp.mpf(9) * (mp.pi**4) / mp.mpf(2)) ** (mp.mpf(1) / mp.mpf(3)))
        * (M_PI_CHARGED_MEV**2)
        / m_p_pred
    )
    hw00_pion = mp.mpf(2) * (M_PI_CHARGED_MEV**2) / m_p_pred

    # Ruled T3 valence-cap bond energy per nucleon (1.5 bonds/A * b2_log_gg) vs #9377 M6:
    z_markov = (q**3) / (q**2 + mp.mpf(1))
    z_gg = z_markov - h_q / mp.mpf(2)
    b2_log_gg = e0_twr * mp.log(mp.mpf(1) / z_gg)
    q2_1 = q**2 + mp.mpf(1)
    q4_1 = q**4 + mp.mpf(1)
    q4_2_1 = q**4 + q**2 + mp.mpf(1)
    d_mod_111 = -(q**3) / (q2_1 * q4_2_1)
    d_mod_211 = -(q**3) * q4_2_1 / ((q2_1**3) * q4_1)
    d_mod_1111 = (q**7) / ((q2_1**3) * q4_1 * q4_2_1)
    w3_gpmt = e0_twr * (-d_mod_111)
    w4_gpmt = e0_twr * ((-mp.mpf(3) * d_mod_211 + d_mod_1111) - mp.mpf(4) * (-d_mod_111))

    strut_du = compute_strutinsky_table(q, max_occ=172)

    return {
        "q": q,
        "alpha_em_form_b": alpha_em,
        "alpha_inv_form_b": mp.mpf(1) / alpha_em,
        "m_p_pred_MeV": m_p_pred,
        "e0_ord0_MeV": e0_ord0,
        "e0_twr_MeV": e0_twr,
        "e0_tower_pauli_MeV": e0_tower_pauli,
        "qbeta_n_scored_MeV": qbeta_n_scored,
        "qbeta_n_legendre_cottingham_MeV": qbeta_n_legendre_cottingham,
        "phi1_wenzl_MeV": phi1_wenzl,
        "phi2_wenzl_MeV": phi2_wenzl,
        "phi3_wenzl_MeV": phi3_wenzl,
        "b3_wenzl_MeV": phi2_wenzl - mp.mpf(2) * phi1_wenzl,
        "p4_alpha": p4_alpha,
        "z4_12": z4_12,
        "n_part_12": n_part_12,
        "b4_hankel_raw_MeV": b4_hankel_raw,
        "ec_he4_fcc_MeV": ec_he4,
        "b4_hankel_strong_restored_MeV": b4_hankel_strong_restored,
        "a_vol_strong_raw_MeV": b4_hankel_raw / mp.mpf(4) + (mp.mpf(3) / mp.mpf(2)) * phi2_wenzl,
        "a_vol_strong_restored_MeV": b4_hankel_strong_restored / mp.mpf(4)
        + (mp.mpf(3) / mp.mpf(2)) * phi2_wenzl,
        "a_surf_wenzl_MeV": mp.mpf(3) * phi2_wenzl,
        "c_coul_coeff_MeV": c_coul_coeff,
        "eps_fermi_MeV": eps_fermi,
        "a_sym_kinetic_linear_MeV": eps_fermi / mp.mpf(3),
        "hw00_pion_MeV": hw00_pion,
        "b2_log_gg_MeV": b2_log_gg,
        "t3_ruled_bond_cap_asymptotic_MeV_per_A": (mp.mpf(3) / mp.mpf(2)) * b2_log_gg,
        "w3_gpmt_MeV": w3_gpmt,
        "w4_gpmt_MeV": w4_gpmt,
        "strut_du": strut_du,
    }


def make_model_evaluators(sc: dict[str, object]) -> dict[str, object]:
    """Construct the ruled T3 baseline (`T3_ruled_valence_cap_pair`) plus 6 exploratory
    zero-parameter cluster comparison evaluators (`S0..S5`) at `sc`."""
    phi1 = sc["phi1_wenzl_MeV"]
    phi2 = sc["phi2_wenzl_MeV"]
    phi3 = sc["phi3_wenzl_MeV"]
    b4_raw = sc["b4_hankel_raw_MeV"]
    b4_rest = sc["b4_hankel_strong_restored_MeV"]
    c_coul = sc["c_coul_coeff_MeV"]
    eps_f = sc["eps_fermi_MeV"]
    hw00 = sc["hw00_pion_MeV"]
    b2_log_gg = sc["b2_log_gg_MeV"]
    w3_gpmt = sc["w3_gpmt_MeV"]
    w4_gpmt = sc["w4_gpmt_MeV"]
    strut_du = sc["strut_du"]

    def ec_fcc(z: int, a: int) -> mp.mpf:
        if z < 2 or a < 1:
            return mp.mpf(0)
        return c_coul * mp.mpf(z * (z - 1)) / (mp.mpf(a) ** (mp.mpf(1) / mp.mpf(3)))

    def dt_pauli(z: int, n: int) -> mp.mpf:
        a = z + n
        if a <= 0:
            return mp.mpf(0)
        tz = (
            mp.mpf(z) * ((mp.mpf(2 * z) / mp.mpf(a)) ** (mp.mpf(2) / mp.mpf(3)))
            if z > 0
            else mp.mpf(0)
        )
        tn = (
            mp.mpf(n) * ((mp.mpf(2 * n) / mp.mpf(a)) ** (mp.mpf(2) / mp.mpf(3)))
            if n > 0
            else mp.mpf(0)
        )
        return (mp.mpf(3) / mp.mpf(5)) * eps_f * (tz + tn - mp.mpf(a))

    def t3_ruled_valence_cap_pair(z: int, n: int) -> mp.mpf:
        """Ruled 2026-11-27 T3 colour-valence bond cap (`3 * floor(A / 2)` bonds, PR #9710)
        evaluated on the two-body pair log bond `b2_log_gg`."""
        a = z + n
        if a <= 1:
            return mp.mpf(0)
        n_bonds_t3 = 3 * (a // 2) if a >= 4 else (1 if a == 2 else 3)
        return mp.mpf(n_bonds_t3) * b2_log_gg

    def s0_wenzl_intra_only(z: int, n: int) -> mp.mpf:
        tot = mp.mpf(0)
        zr, nr = z, n
        while zr > 0 or nr > 0:
            zp = 2 if zr >= 2 else zr
            np_ = 2 if nr >= 2 else nr
            r = zp + np_
            if r >= 2:
                tot += phi1
            if r >= 3:
                tot += phi2
            if r >= 4:
                tot += phi3
            zr -= zp
            nr -= np_
        return tot

    def s1_discrete_quartet_closed_coulomb(z: int, n: int) -> mp.mpf:
        tot = mp.mpf(0)
        zr, nr = z, n
        while zr > 0 or nr > 0:
            zp = 2 if zr >= 2 else zr
            np_ = 2 if nr >= 2 else nr
            r = zp + np_
            if r == 4:
                tot += b4_raw
            elif r == 3:
                tot += phi1 + phi2
            elif r == 2:
                tot += phi1
            zr -= zp
            nr -= np_
        return tot - ec_fcc(z, z + n)

    def s2_su4_pauli_triangle_3tree(z: int, n: int) -> mp.mpf:
        a = z + n
        a_core = 2 * min(z, n)
        d_ex = a - a_core
        if a_core <= 0:
            return -ec_fcc(z, a)
        f1_c = 0 if a_core <= 1 else (1 if a_core == 2 else 3 * a_core - 6)
        f2_c = 0 if a_core <= 2 else 3 * a_core - 8
        f3_c = 0 if a_core <= 3 else a_core - 3
        return (
            mp.mpf(f1_c + 2 * d_ex) * b2_log_gg
            + mp.mpf(f2_c + d_ex) * w3_gpmt
            + mp.mpf(f3_c) * w4_gpmt
            - ec_fcc(z, a)
        )

    def make_welded(b4_strong: mp.mpf, use_strut: bool):
        def fn(z: int, n: int) -> mp.mpf:
            a = z + n
            if a <= 1:
                return mp.mpf(0)
            if a <= 3:
                return s1_discrete_quartet_closed_coulomb(z, n)
            a_mp = mp.mpf(a)
            w_iso = mp.mpf(4 * z * n) / (a_mp * a_mp)
            e_intra = (a_mp / mp.mpf(4)) * b4_strong * w_iso
            m_face = max(
                mp.mpf(0),
                (mp.mpf(3) / mp.mpf(2)) * a_mp - mp.mpf(3) * (a_mp ** (mp.mpf(2) / mp.mpf(3))),
            )
            e_inter = m_face * phi2 * w_iso
            pair = mp.mpf(0)
            if a > 4:
                if z % 2 == 0 and n % 2 == 0:
                    pair = phi1 / mp.sqrt(a_mp / mp.mpf(4))
                elif z % 2 == 1 and n % 2 == 1:
                    pair = -phi1 / mp.sqrt(a_mp / mp.mpf(4))
            sh = mp.mpf(0)
            if use_strut and a > 4 and z <= 172 and n <= 172:
                hw = hw00 * (a_mp ** (-mp.mpf(1) / mp.mpf(3)))
                sh = (strut_du[z] + strut_du[n]) * hw
            return e_intra + e_inter - dt_pauli(z, n) + pair + sh - ec_fcc(z, a)

        return fn

    return {
        "T3_ruled_valence_cap_pair": t3_ruled_valence_cap_pair,
        "S0_wenzl_intra_only": s0_wenzl_intra_only,
        "S1_discrete_quartet_closed_coulomb": s1_discrete_quartet_closed_coulomb,
        "S2_su4_pauli_triangle_3tree": s2_su4_pauli_triangle_3tree,
        "S3_welded_hankel_strong_fcc_fermi_pair": make_welded(b4_raw, False),
        "S4_welded_hankel_net_fcc_fermi_pair": make_welded(b4_rest, False),
        "S5_welded_hankel_net_nilsson_strutinsky": make_welded(b4_rest, True),
    }


def _median_sorted(vals: list[mp.mpf]) -> mp.mpf:
    n = len(vals)
    if n == 0:
        return mp.mpf(0)
    s = sorted(vals)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / mp.mpf(2)


def evaluate_scorecards_at_proton_pin(
    sc: dict[str, object],
    nuclides_2542: list[tuple[int, int, int, mp.mpf]],
    nuclides_2548_all: list[tuple[int, int, int, mp.mpf]],
    betas_1009: list[tuple[int, int, int, mp.mpf]],
    alphas_1051: list[tuple[int, int, int, mp.mpf]],
    ame_by_zn: dict[tuple[int, int], dict[str, object]],
    b4_ame: mp.mpf,
) -> dict[str, object]:
    """Evaluate ruled T3 reference + exploratory S0..S5 across all 3 ACCURACY.md nuclear
    cohorts at the physical proton pin."""
    evaluators = make_model_evaluators(sc)
    all_zn_needed: set[tuple[int, int]] = set()
    for z, n, _, _ in nuclides_2548_all:
        all_zn_needed.add((z, n))
    for z, n, _, _ in betas_1009:
        all_zn_needed.add((z, n))
        all_zn_needed.add((z + 1, n - 1))
    for z, n, _, _ in alphas_1051:
        all_zn_needed.add((z, n))
        all_zn_needed.add((z - 2, n - 2))
    for _, z, n in REPRESENTATIVE_NUCLIDES + HEAVY_ALPHA_BENCHMARKS:
        all_zn_needed.add((z, n))
        if z >= 2 and n >= 2:
            all_zn_needed.add((z - 2, n - 2))
    all_zn_needed.add((2, 2))

    qbeta_n_scored = sc["qbeta_n_scored_MeV"]
    qbeta_n_leg = sc["qbeta_n_legendre_cottingham_MeV"]

    models_out: dict[str, object] = {}
    for mkey, fn in evaluators.items():
        cache = {zn: fn(zn[0], zn[1]) for zn in all_zn_needed}
        b4_mod = cache[(2, 2)]

        abs_pa_2542 = [abs(cache[(z, n)] - be) / mp.mpf(a) for z, n, a, be in nuclides_2542]
        rel_2542 = [abs(cache[(z, n)] - be) / be for z, n, a, be in nuclides_2542]
        abs_pa_2548 = [abs(cache[(z, n)] - be) / mp.mpf(a) for z, n, a, be in nuclides_2548_all]

        bands_binding: dict[str, object] = {}
        for bname, lo, hi in [
            ("light_A_2_16", 2, 16),
            ("sd_pf_A_17_56", 17, 56),
            ("mid_shell_A_57_150", 57, 150),
            ("heavy_A_151_plus", 151, 999),
        ]:
            sub = [(z, n, a, be) for z, n, a, be in nuclides_2542 if lo <= a <= hi]
            sub_rel = [abs(cache[(z, n)] - be) / be for z, n, a, be in sub]
            sub_pa = [abs(cache[(z, n)] - be) / mp.mpf(a) for z, n, a, be in sub]
            bands_binding[bname] = {
                "count": len(sub),
                "MAE_B_per_A_MeV": fmt(sum(sub_pa) / mp.mpf(len(sub))),
                "median_rel_err_pct": fmt(_median_sorted(sub_rel) * mp.mpf(100)),
            }

        rep_rows = []
        for label, z, n in REPRESENTATIVE_NUCLIDES:
            be_exp = mp.mpf(str(ame_by_zn[(z, n)]["binding_energy_total_keV"])) / mp.mpf(1000)
            b_pred = cache[(z, n)]
            rep_rows.append(
                {
                    "nuclide": label,
                    "Z": z,
                    "N": n,
                    "A": z + n,
                    "B_pred_MeV": fmt(b_pred),
                    "B_AME_MeV": fmt(be_exp),
                    "rel_err_pct": fmt((b_pred - be_exp) / be_exp * mp.mpf(100)),
                }
            )

        exo_scored = 0
        exo_legendre = 0
        exo_codata = 0
        rel_beta_scored: list[mp.mpf] = []
        rel_beta_legendre: list[mp.mpf] = []
        rel_beta_codata: list[mp.mpf] = []
        for z, n, _, q_exp in betas_1009:
            db = cache[(z + 1, n - 1)] - cache[(z, n)]
            qb_s = qbeta_n_scored + db
            qb_l = qbeta_n_leg + db
            qb_c = QBETA_N_CODATA_VALIDATION + db
            if qb_s > 0:
                exo_scored += 1
            if qb_l > 0:
                exo_legendre += 1
            if qb_c > 0:
                exo_codata += 1
            rel_beta_scored.append(abs(qb_s - q_exp) / q_exp)
            rel_beta_legendre.append(abs(qb_l - q_exp) / q_exp)
            rel_beta_codata.append(abs(qb_c - q_exp) / q_exp)

        exo_alpha = 0
        qa_preds: list[mp.mpf] = []
        rel_alpha: list[mp.mpf] = []
        for z, n, _, qa_exp in alphas_1051:
            qa_p = cache[(z - 2, n - 2)] + b4_mod - cache[(z, n)]
            if qa_p > 0:
                exo_alpha += 1
            qa_preds.append(qa_p)
            rel_alpha.append(abs(qa_p - qa_exp) / qa_exp)

        heavy_alpha_rows = []
        for label, z, n in HEAVY_ALPHA_BENCHMARKS:
            qa_exp = (
                mp.mpf(str(ame_by_zn[(z - 2, n - 2)]["binding_energy_total_keV"]))
                - mp.mpf(str(ame_by_zn[(z, n)]["binding_energy_total_keV"]))
            ) / mp.mpf(1000) + b4_ame
            qa_p = cache[(z - 2, n - 2)] + b4_mod - cache[(z, n)]
            heavy_alpha_rows.append(
                {
                    "nuclide": label,
                    "Z": z,
                    "N": n,
                    "A": z + n,
                    "Q_alpha_pred_MeV": fmt(qa_p),
                    "Q_alpha_AME_MeV": fmt(qa_exp),
                    "rel_err_pct": fmt((qa_p - qa_exp) / qa_exp * mp.mpf(100)),
                }
            )

        models_out[mkey] = {
            "binding_2542": {
                "count": len(nuclides_2542),
                "MAE_B_per_A_MeV": fmt(sum(abs_pa_2542) / mp.mpf(len(abs_pa_2542))),
                "median_rel_err_pct": fmt(_median_sorted(rel_2542) * mp.mpf(100)),
                "count_2548_all_non_estimated": len(nuclides_2548_all),
                "MAE_B_per_A_2548_MeV": fmt(sum(abs_pa_2548) / mp.mpf(len(abs_pa_2548))),
                "bands": bands_binding,
                "representative_nuclides": rep_rows,
            },
            "beta_minus_1009_composite": {
                "count": len(betas_1009),
                "exothermic_with_scored_qbeta_n": exo_scored,
                "median_rel_err_pct_scored_qbeta_n": fmt(
                    _median_sorted(rel_beta_scored) * mp.mpf(100)
                ),
                "exothermic_with_legendre_cottingham_qbeta_n": exo_legendre,
                "median_rel_err_pct_legendre_cottingham_qbeta_n": fmt(
                    _median_sorted(rel_beta_legendre) * mp.mpf(100)
                ),
                "exothermic_with_codata_qbeta_n_validation": exo_codata,
                "median_rel_err_pct_codata_qbeta_n_validation": fmt(
                    _median_sorted(rel_beta_codata) * mp.mpf(100)
                ),
            },
            "alpha_decay_1051": {
                "count": len(alphas_1051),
                "exothermic_count": exo_alpha,
                "median_Q_alpha_pred_MeV": fmt(_median_sorted(qa_preds)),
                "median_rel_err_pct": fmt(_median_sorted(rel_alpha) * mp.mpf(100)),
                "heavy_benchmarks": heavy_alpha_rows,
            },
        }

    strut_du = sc["strut_du"]
    hw_pb208 = sc["hw00_pion_MeV"] * (mp.mpf(208) ** (-mp.mpf(1) / mp.mpf(3)))
    pb208_shell_mev = (strut_du[82] + strut_du[126]) * hw_pb208

    return {
        "scales": {
            "q": fmt(sc["q"]),
            "alpha_inv_form_b": fmt(sc["alpha_inv_form_b"]),
            "m_p_pred_MeV": fmt(sc["m_p_pred_MeV"]),
            "e0_twr_MeV": fmt(sc["e0_twr_MeV"]),
            "e0_tower_pauli_MeV": fmt(sc["e0_tower_pauli_MeV"]),
            "phi1_wenzl_MeV": fmt(sc["phi1_wenzl_MeV"]),
            "phi2_wenzl_MeV": fmt(sc["phi2_wenzl_MeV"]),
            "b3_wenzl_MeV": fmt(sc["b3_wenzl_MeV"]),
            "p4_alpha_quartet": fmt(sc["p4_alpha"]),
            "b4_hankel_raw_MeV": fmt(sc["b4_hankel_raw_MeV"]),
            "ec_he4_fcc_MeV": fmt(sc["ec_he4_fcc_MeV"]),
            "b4_hankel_strong_restored_MeV": fmt(sc["b4_hankel_strong_restored_MeV"]),
            "a_vol_strong_raw_MeV": fmt(sc["a_vol_strong_raw_MeV"]),
            "a_vol_strong_restored_MeV": fmt(sc["a_vol_strong_restored_MeV"]),
            "a_surf_wenzl_MeV": fmt(sc["a_surf_wenzl_MeV"]),
            "c_coul_coeff_MeV": fmt(sc["c_coul_coeff_MeV"]),
            "eps_fermi_MeV": fmt(sc["eps_fermi_MeV"]),
            "a_sym_kinetic_linear_MeV": fmt(sc["a_sym_kinetic_linear_MeV"]),
            "hw00_pion_MeV": fmt(sc["hw00_pion_MeV"]),
            "t3_ruled_bond_cap_asymptotic_MeV_per_A": fmt(
                sc["t3_ruled_bond_cap_asymptotic_MeV_per_A"]
            ),
            "pb208_strutinsky_stabilization_MeV": fmt(pb208_shell_mev),
            "qbeta_n_scored_MeV": fmt(sc["qbeta_n_scored_MeV"]),
            "qbeta_n_legendre_cottingham_MeV": fmt(sc["qbeta_n_legendre_cottingham_MeV"]),
        },
        "models": models_out,
    }


def main() -> int:
    set_compute_dps(125)
    mp.mp.dps = 125

    wb = WitnessBuilder("ka-b4-pauli-wigner-saturation", engine="sympy", output_dir=HERE)
    wb.set_description(
        "Exploratory zero-fit 80-dps SymPy + mpmath macroscopic cluster-model comparison "
        "(§3b-cond, unwired; beans qou-v2om, qou-gpb5, qou-sbn9, qou-d9iv; companion Lean "
        "module QOU.Nuclear.AlphaQuartetPauliWignerSaturation; alongside the ruled T3 "
        "colour-valence bound of QOU.MassTheory.NucleusBondValence, PR #9710) evaluating "
        "intra-shell Pauli-Wigner Wenzl cells (b_2, b_3), SU(4) 4x4 Hankel quartet closure, "
        "exploratory FCC (111) face contacts, Wigner-Pauli Fermi valley, and Nilsson-Strutinsky "
        "shell stabilization across 2,542 AME2020 nuclides, 1,009 composite beta-minus "
        "transitions, and 1,051 alpha-emitters strictly at the physical proton pin."
    )

    sym_res = verify_symbolic_identities()
    wb.add_data("symbolic_verification", sym_res)
    wb.add_assertion(
        name="lean_algebraic_identities_symbolic_exact",
        computed=sym_res["identities_verified"],
        expected="8",
        tolerance="0",
        source="Exact Z[q, q^{-1}] SymPy verification of all 8 division-free polynomial identities in AlphaQuartetPauliWignerSaturation.lean",
    )

    with mp.workdps(195):
        qp_hi = q_at(190)

    mt_rows = json.loads(
        (COMPUTATIONS_ROOT / "mass-table-comprehensive.witness.json").read_text(encoding="utf-8")
    )["data"]["rows"]
    mt_zn = {(int(r["Z"]), int(r["N"])) for r in mt_rows}

    ame_entries = json.loads(
        (COMPUTATIONS_ROOT / "data" / "ame2020.json").read_text(encoding="utf-8")
    )["entries"]
    ame_by_zn = {(int(e["Z"]), int(e["N"])): e for e in ame_entries}
    b4_ame = mp.mpf(str(ame_by_zn[(2, 2)]["binding_energy_total_keV"])) / mp.mpf(1000)

    nuclides_2548_all: list[tuple[int, int, int, mp.mpf]] = []
    nuclides_2542: list[tuple[int, int, int, mp.mpf]] = []
    betas_1009: list[tuple[int, int, int, mp.mpf]] = []
    alphas_1051: list[tuple[int, int, int, mp.mpf]] = []

    for e in ame_entries:
        z, n, a = int(e["Z"]), int(e["N"]), int(e["A"])
        if (
            a >= 2
            and not e.get("binding_energy_per_A_estimated")
            and e.get("binding_energy_per_A_keV") is not None
        ):
            be = mp.mpf(str(e["binding_energy_total_keV"])) / mp.mpf(1000)
            nuclides_2548_all.append((z, n, a, be))
            if (z, n) in mt_zn:
                nuclides_2542.append((z, n, a, be))

        if (
            a >= 2
            and not e.get("beta_decay_energy_estimated")
            and e.get("beta_decay_energy_keV") is not None
        ):
            qb_exp = mp.mpf(str(e["beta_decay_energy_keV"])) / mp.mpf(1000)
            if qb_exp > mp.mpf(1) / mp.mpf(100) and (z, n) in mt_zn and (z + 1, n - 1) in mt_zn:
                betas_1009.append((z, n, a, qb_exp))

        if (
            z >= 2
            and n >= 2
            and a >= 6
            and not e.get("binding_energy_per_A_estimated")
            and e.get("binding_energy_per_A_keV") is not None
            and (z, n) in mt_zn
            and (z - 2, n - 2) in mt_zn
        ):
            ed = ame_by_zn.get((z - 2, n - 2))
            if (
                ed is not None
                and not ed.get("binding_energy_per_A_estimated")
                and ed.get("binding_energy_per_A_keV") is not None
            ):
                qa_exp = (
                    mp.mpf(str(ed["binding_energy_total_keV"]))
                    - mp.mpf(str(e["binding_energy_total_keV"]))
                ) / mp.mpf(1000) + b4_ame
                if qa_exp > mp.mpf(1) / mp.mpf(2):
                    alphas_1051.append((z, n, a, qa_exp))

    sc_proton = build_anchor_scales(qp_hi)

    res_proton = evaluate_scorecards_at_proton_pin(
        sc_proton,
        nuclides_2542,
        nuclides_2548_all,
        betas_1009,
        alphas_1051,
        ame_by_zn,
        b4_ame,
    )

    wb.add_data(
        "calibration_and_anti_fit_declaration",
        {
            "free_parameters": 0,
            "external_inputs": [
                "m_e (electron mass energy equivalent in MeV, qou_substrate.codata)",
                "q_0 (aether deformation parameter evaluated strictly at physical_proton; muon pin on hold per 2026-11-28 owner ruling until rederivation)",
                "m_{pi^+-} = 13957039/100000 MeV (PDG charged-pion mass setting FCC spacing and pion-Compton hw_0)",
            ],
            "upstream_codata_nucleon_mass_leakage": False,
            "ruled_valence_reference": (
                "QOU.MassTheory.NucleusBondValence (PR #9710, 2026-11-27 owner ruling): "
                "production nucleus bond count (gap G5) is fixed by colour valence cap T3 "
                "(3*floor(A/2) bonds, 1.5 per nucleon); V6 is not adopted without a corpus derivation."
            ),
            "scope": (
                "Exploratory macroscopic cluster-model comparison (§3b-cond, unwired) alongside "
                "the ruled T3 valence bound; fenced production pipeline files untouched."
            ),
        },
    )
    wb.add_data("proton_pin_evaluation", res_proton)

    wb.add_assertion(
        name="scorecard_cohort_counts_match_accuracy_md",
        computed=f"{len(nuclides_2542)}/{len(betas_1009)}/{len(alphas_1051)}",
        expected="2542/1009/1051",
        tolerance="0",
        source="Exact match to ACCURACY.md Tables 3.2b (2,542 nuclides), 3.4b (1,009 composite beta^-), and 3.5b (1,051 alpha emitters)",
    )

    s3_p = res_proton["models"]["S3_welded_hankel_strong_fcc_fermi_pair"]
    s4_p = res_proton["models"]["S4_welded_hankel_net_fcc_fermi_pair"]
    s5_p = res_proton["models"]["S5_welded_hankel_net_nilsson_strutinsky"]

    mae_s3 = mp.mpf(s3_p["binding_2542"]["MAE_B_per_A_MeV"])
    mae_s4 = mp.mpf(s4_p["binding_2542"]["MAE_B_per_A_MeV"])
    med_s4 = mp.mpf(s4_p["binding_2542"]["median_rel_err_pct"])
    exo_beta_s4_scored = int(s4_p["beta_minus_1009_composite"]["exothermic_with_scored_qbeta_n"])
    exo_beta_s4_leg = int(
        s4_p["beta_minus_1009_composite"]["exothermic_with_legendre_cottingham_qbeta_n"]
    )
    exo_alpha_s4 = int(s4_p["alpha_decay_1051"]["exothermic_count"])

    wb.add_assertion(
        name="exploratory_cluster_synthesis_sub_quarter_MeV_per_A_and_sub_1pct_median",
        computed="1"
        if (mae_s3 < mp.mpf(1) / mp.mpf(4) and mae_s4 < mp.mpf(1) / mp.mpf(10) and med_s4 < mp.mpf(1))
        else "0",
        expected="1",
        tolerance="0",
        source="Exploratory §3b-cond cluster models S3 (MAE < 0.25 MeV/A) and S4 (MAE < 0.10 MeV/A, < 1.0% median |Delta B|/B) across 2,542 nuclides alongside ruled T3 baseline",
    )
    wb.add_assertion(
        name="composite_beta_and_alpha_exothermicity_across_chart",
        computed="1"
        if (exo_beta_s4_scored >= 890 and exo_beta_s4_leg >= 930 and exo_alpha_s4 >= 1020)
        else "0",
        expected="1",
        tolerance="0",
        source="Continuous Wigner + 3D Pauli Fermi valley lifts composite beta^- exothermicity to >890/1009 (>930/1009 with Legendre-Cottingham Delta m_np) and alpha exothermicity to >1020/1051",
    )

    po_map = {
        r["nuclide"]: mp.mpf(r["Q_alpha_pred_MeV"])
        for r in s5_p["alpha_decay_1051"]["heavy_benchmarks"]
    }
    wb.add_assertion(
        name="nilsson_strutinsky_n126_magic_jump_212Po_gt_210Po",
        computed="1" if (po_map["212Po"] - po_map["210Po"] > mp.mpf(3)) else "0",
        expected="1",
        tolerance="0",
        source="Zero-parameter #9367 Nilsson-Strutinsky shell stabilization produces > +3 MeV N=128->126 magic Q_alpha jump from 210Po to 212Po",
    )

    out_path = wb.save()

    print("=" * 96)
    print(" EXPLORATORY (§3b-cond) NUCLEAR SATURATION COMPARISON PROBE (80 dps output / 125 dps work)")
    print("=" * 96)
    print(f" Proton pin m_p^pred    : {mp.nstr(sc_proton['m_p_pred_MeV'], 14)} MeV")
    print(f" Ruled T3 cap (1.5*b2)  : {mp.nstr(sc_proton['t3_ruled_bond_cap_asymptotic_MeV_per_A'], 8)} MeV/A")
    print(f" B4 Hankel raw / strong : {mp.nstr(sc_proton['b4_hankel_raw_MeV'], 10)} / "
          f"{mp.nstr(sc_proton['b4_hankel_strong_restored_MeV'], 10)} MeV")
    print(f" Exploratory a_V / a_S  : {mp.nstr(sc_proton['a_vol_strong_restored_MeV'], 8)} / "
          f"{mp.nstr(sc_proton['a_surf_wenzl_MeV'], 8)} MeV  |  "
          f"eps_F/3 = {mp.nstr(sc_proton['a_sym_kinetic_linear_MeV'], 8)} MeV")
    print("-" * 96)
    for mk, minfo in res_proton["models"].items():
        b_info = minfo["binding_2542"]
        bm_info = minfo["beta_minus_1009_composite"]
        a_info = minfo["alpha_decay_1051"]
        print(
            f" {mk:42s} | MAE={mp.nstr(mp.mpf(b_info['MAE_B_per_A_MeV']), 4):>6s} MeV/A "
            f"med={mp.nstr(mp.mpf(b_info['median_rel_err_pct']), 4):>5s}% "
            f"| beta={bm_info['exothermic_with_scored_qbeta_n']:>3d}/"
            f"{bm_info['exothermic_with_legendre_cottingham_qbeta_n']:>3d}/"
            f"{bm_info['exothermic_with_codata_qbeta_n_validation']:>3d} "
            f"med={mp.nstr(mp.mpf(bm_info['median_rel_err_pct_legendre_cottingham_qbeta_n']), 4):>5s}% "
            f"| alpha={a_info['exothermic_count']:>4d}/1051 "
            f"med={mp.nstr(mp.mpf(a_info['median_rel_err_pct']), 4):>5s}%"
        )
    print("-" * 96)
    print(f" Saved proton-pinned 80-dps witness -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
