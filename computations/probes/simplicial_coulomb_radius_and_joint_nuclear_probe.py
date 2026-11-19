#!/usr/bin/env python3
"""simplicial_coulomb_radius_and_joint_nuclear_probe.py — 80-dps First-Principles
Simplicial Discrete Proton-Pair Coulomb Sum, 3D FCC Packing Radius Transport
(`qou-usft` / `qou-mumr`), & Joint Wave-3 Nuclear Synthesis Benchmark
(Zero Fitting, Zero Float64).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/Nuclear/SimplicialCoulombGraphMetricDerivation.lean`
  (`namespace QOU.Nuclear.SimplicialCoulombGraphMetricDerivation`),
synthesizing Wave-3 Nuclear Lanes N1–N4:
  - N1: `QOU/Nuclear/BallManifoldTriangulationAndSurfaceScaling.lean`
        (3D close-packed compact-ball simplicial manifold triangulation & O(A^{2/3}) surface)
  - N2: `QOU/Nuclear/SpinOrbitShellClosureAndSymmetryEnergy.lean`
        (2j+1 Mayer-Jensen spin-orbit shell closures, discrete Pauli asymmetry & shell correction)
  - N3: `QOU/Nuclear/SeniorityPairingAndHoyleTriadThreshold.lean`
        (Temperley-Lieb seniority-0 Kramers pairing, 3-alpha Hoyle threshold, & actinide balance)
  - N4: `QOU/Nuclear/SimplicialCoulombGraphMetricDerivation.lean`
        (discrete 3D vertex-pair Coulomb sum & 3D FCC Voronoi packing radius transport)

DISCIPLINE:
  - 80-dps mpmath working precision (`DPS = 80`), zero `float64` intermediates, zero `math`/`numpy`.
  - Zero fitting: `r_0` and all strong/spin-orbit/pairing/Coulomb scales are evaluated strictly
    from parameter-free QOU substrate expressions across all four Compton bond-length candidates
    `ell_bond in {lambda_bar_pi, (3/2)*lambda_bar_pi, sqrt(3)*lambda_bar_pi, 2*lambda_bar_pi}`
    with Form-B Bring-Schwinger `alpha_EM^{corr}(q_2t)`, cross-checked across `q_proton` and
    `q_muon` (`"q0Anchor": "comparison"`).
"""
from __future__ import annotations

import json
import sys
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO_ROOT = COMPUTE_DIR.parent
for _p in (
    "tools/pyhecke/python",
    "tools/qou-substrate/python",
    "computations/substrate",
    "computations/alpha",
    "computations/probes",
    "computations",
):
    _full = str(REPO_ROOT / _p)
    if _full not in sys.path:
        sys.path.insert(0, _full)

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from mpmath import fabs, fsum, log, mpf, pi, sqrt  # noqa: E402

from _li_2_q_util import li_2_q  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from coulomb_energy import alpha_em_inv_bring_schwinger  # noqa: E402
from q_parameter import (  # noqa: E402
    Q_50_DIGIT_STR,
    q_at,
    q_muon_at,
    q_two_term_borromean_at,
)
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402

DPS = 80
set_compute_dps(DPS)
mp.mp.dps = DPS

HBAR_C_MEV_FM = mpf("197.3269804152")
M_PI_CHARGED_MEV = mpf("139.57039")
LAMBDA_BAR_PI_FM = HBAR_C_MEV_FM / M_PI_CHARGED_MEV


# =============================================================================
# § 0. Exact Integer & String-Parsed AME2020 Helpers (Zero Float64)
# =============================================================================

def _int_comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k_use = k if k <= n - k else n - k
    num = 1
    for i in range(1, k_use + 1):
        num = (num * (n - k_use + i)) // i
    return num


def _load_ame2020_exact() -> dict[tuple[int, int], dict[str, mpf]]:
    """Read vendored AME2020 table via `parse_float=str` + `Decimal` (zero float64)."""
    table_path = REPO_ROOT / "qou-mass" / "src" / "qou_mass" / "data" / "ame2020.json"
    raw = json.loads(table_path.read_text(encoding="utf-8"), parse_float=str)
    out: dict[tuple[int, int], dict[str, mpf]] = {}
    with mp.workdps(DPS):
        for e in raw["entries"]:
            z_i = int(e["Z"])
            a_i = int(e["A"])
            per_a_dec = Decimal(str(e["binding_energy_per_A_keV"]))
            tot_mev_dec = (per_a_dec * Decimal(a_i)) / Decimal(1000)
            unc_str = e.get("binding_energy_per_A_unc_keV")
            unc_dec = Decimal(str(unc_str)) if unc_str is not None else Decimal(0)
            sig_mev_dec = (unc_dec * Decimal(a_i)) / Decimal(1000)
            out[(z_i, a_i)] = {
                "B_AME_MeV": mpf(str(tot_mev_dec)),
                "sigma_AME_MeV": mpf(str(sig_mev_dec)),
            }
    return out


AME_EXACT = _load_ame2020_exact()


# =============================================================================
# § 1. 80-dps Substrate Constants & Form-B Bring-Schwinger Photon at q_2t, q_p, q_mu
# =============================================================================

def alpha_em_inv_form_b_80dps(q_val: mpf) -> mpf:
    """Pure 80-dps Newton solve of Form-B Bring-Schwinger cubic:
        -h^2 * H(q) * a^3 + H(q) * a^2 + T_EM(q) * a - 1 = 0,
    where T_EM(q) = q * [9]_q * [10]_q + 2/(3*pi), H(q) = [2]_q / (8*pi), h = q - q^{-1}.
    """
    with mp.workdps(DPS + 15):
        qx = mpf(q_val)
        h = qx - mpf(1) / qx
        q2 = qx + mpf(1) / qx
        q9 = (qx ** 9 - qx ** (-9)) / h
        q10 = (qx ** 10 - qx ** (-10)) / h
        t_em = qx * q9 * q10 + mpf(2) / (mpf(3) * pi)
        h_norm = q2 / (mpf(8) * pi)
        c_loop = h ** 2
        a = mpf(1) / t_em
        for _ in range(30):
            f_val = -c_loop * h_norm * (a ** 3) + h_norm * (a ** 2) + t_em * a - mpf(1)
            fp_val = -mpf(3) * c_loop * h_norm * (a ** 2) + mpf(2) * h_norm * a + t_em
            step = f_val / fp_val
            a -= step
            if fabs(step) < mpf("1e-90"):
                break
        res = mpf(1) / a
    return +res


def derive_substrate_at_q(q_val: mpf) -> dict[str, mpf]:
    """Derive all parameter-free QOU strong, spin-orbit, pairing, and EM constants at `q_val`."""
    with mp.workdps(DPS):
        q = mpf(q_val)
        qi = mpf(1) / q
        h = q - qi
        hbar_q = (q - mpf(1)) / q
        tower_resum = mpf(1) / (mpf(1) - hbar_q ** 2)
        me = mpf(str(M_E_MEV))

        e0_bare = me / (q * (q - mpf(1)))
        e0_inf = e0_bare * tower_resum

        z_d = (q ** 3) / (q ** 2 + mpf(1))
        z_gg = z_d - h / mpf(2)
        z_nn_chiral = z_d - h
        tau_bor = (mpf(4) + h ** 2 - mpf(3) * (h ** 4) - (h ** 6)) / (h ** 2 + mpf(4))

        b2_log_d_bare = e0_bare * log(mpf(1) / z_d)
        b2_log_d_inf = e0_inf * log(mpf(1) / z_d)
        b2_log_gg_bare = e0_bare * log(mpf(1) / z_gg)
        b2_log_gg_inf = e0_inf * log(mpf(1) / z_gg)

        g_tau2 = -li_2_q(-(tau_bor * tau_bor), q, qi)
        g_tau2_zd = -li_2_q(-(tau_bor * tau_bor * z_d), q, qi)
        g_tau2_znn = -li_2_q(-(tau_bor * tau_bor * z_nn_chiral), q, qi)
        b2_bor_pair = e0_bare * (z_d ** 2) * (g_tau2 - g_tau2_zd)
        b2_bor_d_bare = e0_bare * ((tau_bor ** 2) * (mpf(1) - z_d)) + b2_bor_pair

        # GPMT H_3 / H_4 modified-dimension cumulants
        q2_1 = q ** 2 + mpf(1)
        q4_1 = q ** 4 + mpf(1)
        q4_2_1 = q ** 4 + q ** 2 + mpf(1)
        h4_denom = (q2_1 ** 3) * q4_1 * q4_2_1

        d_mod_111 = -(q ** 3) / (q2_1 * q4_2_1)
        d_mod_211 = -(q ** 3) * q4_2_1 / ((q2_1 ** 3) * q4_1)
        d_mod_1111 = (q ** 7) / h4_denom

        mu3_gpmt = -d_mod_111
        s_row3_h4_4 = -mpf(3) * d_mod_211 + d_mod_1111
        mu4_gpmt_h4 = s_row3_h4_4 - mpf(4) * mu3_gpmt

        w3_bare = e0_bare * mu3_gpmt
        w4_bare = e0_bare * mu4_gpmt_h4
        w3_inf = e0_inf * mu3_gpmt
        w4_inf = e0_inf * mu4_gpmt_h4

        # N2: Spin-orbit coupling & Compton shell oscillator spacing
        kappa_so = h * z_d / mpf(2)
        e_osc_compton_bare = e0_bare / hbar_q
        a_sym_compton = e_osc_compton_bare * z_d

        # N3: Temperley-Lieb seniority-0 pairing gap (`SeniorityPairingAndHoyleTriadThreshold.tlPairingGap`):
        #   tlPairingGap(q, g_pair) = (1/2) * g_pair * [2]_q
        # At parameter-free 3-body cumulant coupling g_pair = w3_GPMT = E0 * mu3_GPMT = E0 / ([2]_q * [3]_q),
        # the [2]_q factor cancels identically: Delta_TL = (1/2) * w3_GPMT * [2]_q = E0 / (2 * [3]_q).
        q_int_2 = q + qi
        q_int_3 = q ** 2 + mpf(1) + mpf(1) / (q ** 2)
        delta_tl_bare = (w3_bare * q_int_2) / mpf(2)
        delta_tl_inf = (w3_inf * q_int_2) / mpf(2)
        delta_tl_closed_diff = fabs(delta_tl_bare - e0_bare / (mpf(2) * q_int_3)) + fabs(
            delta_tl_inf - e0_inf / (mpf(2) * q_int_3)
        )

        # N4: Form-B Bring-Schwinger photon & alpha_EM * hbar * c
        alpha_em_inv = alpha_em_inv_form_b_80dps(q)
        alpha_hbar_c = HBAR_C_MEV_FM / alpha_em_inv

        return {
            "q": q,
            "qi": qi,
            "q_int_2": q_int_2,
            "q_int_3": q_int_3,
            "h": h,
            "hbar_q": hbar_q,
            "tower_resum": tower_resum,
            "m_e_MeV": me,
            "E0_bare_MeV": e0_bare,
            "E0_inf_MeV": e0_inf,
            "z_D": z_d,
            "z_gg": z_gg,
            "z_nn_chiral": z_nn_chiral,
            "tau_Bor": tau_bor,
            "g_tau2": g_tau2,
            "g_tau2_zD": g_tau2_zd,
            "g_tau2_znn": g_tau2_znn,
            "b2_log_D_bare_MeV": b2_log_d_bare,
            "b2_log_D_inf_MeV": b2_log_d_inf,
            "b2_log_gg_bare_MeV": b2_log_gg_bare,
            "b2_log_gg_inf_MeV": b2_log_gg_inf,
            "b2_Bor_D_bare_MeV": b2_bor_d_bare,
            "mu3GPMT_H4": mu3_gpmt,
            "mu4GPMT_H4": mu4_gpmt_h4,
            "w3_bare_MeV": w3_bare,
            "w4_bare_MeV": w4_bare,
            "w3_inf_MeV": w3_inf,
            "w4_inf_MeV": w4_inf,
            "kappa_SO": kappa_so,
            "E_osc_compton_bare_MeV": e_osc_compton_bare,
            "a_sym_compton_MeV": a_sym_compton,
            "delta_TL_bare_MeV": delta_tl_bare,
            "delta_TL_inf_MeV": delta_tl_inf,
            "delta_TL_closed_form_diff": delta_tl_closed_diff,
            "alpha_em_inv_form_b": alpha_em_inv,
            "alpha_hbar_c_MeV_fm": alpha_hbar_c,
        }


def build_compton_bond_length_laws() -> dict[str, dict[str, mpf]]:
    """Four parameter-free QOU Compton bond-length candidates evaluated side-by-side."""
    with mp.workdps(DPS):
        c_fcc = (mpf(3) / (mpf(4) * pi * sqrt(mpf(2)))) ** (mpf(1) / mpf(3))
        laws_raw = [
            ("L1_lambda_pi", mpf(1), "1 * lambda_bar_pi"),
            ("L2_three_halves_lambda_pi", mpf(3) / mpf(2), "(3/2) * lambda_bar_pi"),
            ("L3_sqrt3_lambda_pi", sqrt(mpf(3)), "sqrt(3) * lambda_bar_pi"),
            ("L4_two_lambda_pi", mpf(2), "2 * lambda_bar_pi"),
        ]
        out: dict[str, dict[str, mpf]] = {}
        for key, mult, _desc in laws_raw:
            ell = mult * LAMBDA_BAR_PI_FM
            r0_fcc = c_fcc * ell
            out[key] = {
                "multiplier_on_lambda_pi": mult,
                "ell_bond_fm": ell,
                "r0_fcc_fm": r0_fcc,
                "voronoi_cell_vol_fm3": (ell ** 3) / sqrt(mpf(2)),
            }
        return out


# =============================================================================
# § 2. Deterministic 3D Simplicial / FCC Lattice Coordinates & Discrete Coulomb
# =============================================================================

def generate_fcc_tetrahedral_centered_sites(max_a: int = 250) -> list[tuple[int, int, int]]:
    """Generate integer FCC sites `(x, y, z)` (`(x + y + z) % 2 == 0`, physical unit-bond
    coordinate `(x, y, z) / sqrt(2)`) sorted deterministically by squared distance
    `(2x - 1)^2 + (2y - 1)^2 + (2z - 1)^2` from the central regular K_4 centroid `(1/2, 1/2, 1/2)`.
    - First 3 sites: unit-edge equilateral triangle (`3H`, `3He`).
    - First 4 sites: `(0,0,0), (0,1,1), (1,0,1), (1,1,0)` — exact unit-edge regular K_4 (`4He`).
    - First 16 sites: exact T_d-symmetric 4 + 12 shell (`16O`).
    """
    sites: list[tuple[int, int, int]] = []
    bound = 8
    while len(sites) < max_a + 32:
        sites.clear()
        for x in range(-bound, bound + 1):
            for y in range(-bound, bound + 1):
                for z in range(-bound, bound + 1):
                    if ((x + y + z) % 2) == 0:
                        sites.append((x, y, z))
        bound += 2
    sites.sort(
        key=lambda p: (
            (2 * p[0] - 1) ** 2 + (2 * p[1] - 1) ** 2 + (2 * p[2] - 1) ** 2,
            p[0] * p[0] + p[1] * p[1] + p[2] * p[2],
            abs(p[0]) + abs(p[1]) + abs(p[2]),
            p[0],
            p[1],
            p[2],
        )
    )
    return sites[:max_a]


FCC_SITES_MASTER = generate_fcc_tetrahedral_centered_sites(260)


def _build_inv_sqrt_cache(max_k: int = 400) -> list[mpf]:
    with mp.workdps(DPS + 10):
        cache = [mpf(0)]
        for k in range(1, max_k + 1):
            cache.append(mpf(1) / sqrt(mpf(k)))
    return [+v for v in cache]


INV_SQRT_CACHE = _build_inv_sqrt_cache(400)


def fcc_unit_inv_dist_matrix(coords: list[tuple[int, int, int]]) -> tuple[list[list[mpf]], dict[int, int]]:
    """Build exact 80-dps `A x A` unit-bond inverse-distance matrix `invDist[u][v]` for
    integer FCC coordinates `(x, y, z) / sqrt(2)`, plus exact integer shell histogram `k -> pair_count`
    where `k = ((dx)^2 + (dy)^2 + (dz)^2) // 2` (`d_unit = sqrt(k)`)."""
    a_cnt = len(coords)
    mat: list[list[mpf]] = [[mpf(0)] * a_cnt for _ in range(a_cnt)]
    hist: dict[int, int] = {}
    for u in range(a_cnt):
        xu, yu, zu = coords[u]
        for v in range(u + 1, a_cnt):
            xv, yv, zv = coords[v]
            dx = xu - xv
            dy = yu - yv
            dz = zu - zv
            k_sq = (dx * dx + dy * dy + dz * dz) // 2
            hist[k_sq] = hist.get(k_sq, 0) + 1
            val = INV_SQRT_CACHE[k_sq] if k_sq < len(INV_SQRT_CACHE) else (mpf(1) / sqrt(mpf(k_sq)))
            mat[u][v] = val
            mat[v][u] = val
    return mat, hist


def core_consistent_pauli_proton_occupancy(A: int, Z: int) -> list[bool]:
    """Core-consistent Pauli `(2p, 2n)` discrete proton occupancy (`sum = Z`) on `A` radially
    ordered 3D FCC lattice sites:
    - Let `N = A - Z`, `M_min = min(Z, N)`, and `A_core = 2 * M_min`.
    - Inside the balanced inner `A_core` radially ordered core sites `0 .. A_core - 1`, pairs
      `(p, n)` deterministically on `(2k, 2k + 1)` so `M_min` protons and `M_min` neutrons
      uniformly populate every radial shell of the `(2p, 2n)` core (`pauli_k4_balanced_isospin`).
    - For neutron-rich nuclei (`N > Z`), all `N - Z` outer skin sites `A_core .. A - 1` carry
      excess neutrons (`False`), matching the outer neutron skin of `pauli_capped_kuhn_ball` and
      `pauli_capped_shell_ball`.
    - For proton-rich nuclei (`Z > N`, e.g. high-Z mirror partners `3He..41Sc`), all `Z - N`
      excess valence protons occupy `A_core .. A - 1` (`True`) outside the identical `M_min`-proton
      core, eliminating core-vs-skin mirror inversion.
    """
    N = A - Z
    occ = [False] * A
    if Z <= 0:
        return occ
    if Z >= A:
        return [True] * A
    m_min = Z if Z <= N else N
    a_core = 2 * m_min
    for k in range(m_min):
        occ[2 * k] = True
    if Z > N:
        for idx in range(a_core, A):
            occ[idx] = True
    return occ


def thomson_conductor_skin_lower_bound_occupancy(inv_mat: list[list[mpf]], Z: int) -> list[bool]:
    """Diagnostic classical Thomson-conductor electrostatic lower-bound occupancy (`sum = Z`):
    unconstrained greedy minimum-potential placement segregates charges onto the outer surface
    shell like a metallic conductor (never used for nuclear ground-state binding; recorded solely
    as a rigorous electrostatic lower bound)."""
    a_cnt = len(inv_mat)
    occ = [False] * a_cnt
    if Z <= 0:
        return occ
    if Z >= a_cnt:
        return [True] * a_cnt
    row_totals = [fsum(inv_mat[u]) for u in range(a_cnt)]
    occ[0] = True
    pot_from_protons = [inv_mat[v][0] for v in range(a_cnt)]
    for _ in range(1, Z):
        best_v = -1
        best_pot = None
        for v in range(a_cnt):
            if occ[v]:
                continue
            cand_pot = pot_from_protons[v]
            if (
                best_v < 0
                or cand_pot < best_pot
                or (cand_pot == best_pot and row_totals[v] > row_totals[best_v])
            ):
                best_v = v
                best_pot = cand_pot
        occ[best_v] = True
        for v in range(a_cnt):
            if not occ[v]:
                pot_from_protons[v] = pot_from_protons[v] + inv_mat[v][best_v]
    return occ


def discrete_coulomb_unit_sum(inv_mat: list[list[mpf]], is_proton: list[bool]) -> mpf:
    """Exact evaluation of `(1/2) * sum_{u, v} p_u p_v invDist(u, v)` matching
    `SimplicialCoulombGraphMetricDerivation.discreteCoulombEnergy` at `alphaHbarC = 1`."""
    a_cnt = len(inv_mat)
    terms: list[mpf] = []
    for u in range(a_cnt):
        if not is_proton[u]:
            continue
        for v in range(u + 1, a_cnt):
            if is_proton[v]:
                terms.append(inv_mat[u][v])
    return fsum(terms)


def mirror_occupancy(is_proton: list[bool]) -> list[bool]:
    return [not b for b in is_proton]


def build_carbon12_equilateral_3alpha_cluster() -> dict[str, object]:
    """Explicit 3D C_3-symmetric equilateral 3-alpha (`3 x K_4`) coordinate realization
    in `(1/sqrt(2)) * Z^3`:
      T_0 = {(2,0,0), (3,1,0), (2,1,1), (3,0,1)},
      T_1 = C_3(T_0) = {(0,2,0), (0,3,1), (1,2,1), (1,3,0)},
      T_2 = C_3^2(T_0) = {(0,0,2), (1,0,3), (1,1,2), (0,1,3)}.
    Every intra-alpha edge has exact unit length 1, adjacent alpha-tetrahedra touch at
    exact unit bond length 1 (`(2,1,1)` to `(1,2,1)`), and C_3-symmetric `(2p, 2n)` occupancy
    places 2 protons per K_4 (`6` protons -> `3` intra-alpha pairs + `12` inter-alpha pairs = `15`).
    """
    t0 = [(2, 0, 0), (3, 1, 0), (2, 1, 1), (3, 0, 1)]
    t1 = [(z, x, y) for (x, y, z) in t0]
    t2 = [(y, z, x) for (x, y, z) in t0]
    coords = t0 + t1 + t2
    # C_3-symmetric Pauli-balanced (2p, 2n) per K_4: indices 0, 2 in each K_4 are protons
    is_p = [True, False, True, False] * 3
    inv_mat, hist = fcc_unit_inv_dist_matrix(coords)

    intra_all_unit = True
    for c_idx in range(3):
        base = 4 * c_idx
        for i in range(4):
            for j in range(i + 1, 4):
                if fabs(inv_mat[base + i][base + j] - mpf(1)) > mpf("1e-75"):
                    intra_all_unit = False

    intra_pp_terms: list[mpf] = []
    inter_pp_terms: list[mpf] = []
    for u in range(12):
        if not is_p[u]:
            continue
        for v in range(u + 1, 12):
            if not is_p[v]:
                continue
            if (u // 4) == (v // 4):
                intra_pp_terms.append(inv_mat[u][v])
            else:
                inter_pp_terms.append(inv_mat[u][v])

    s_intra = fsum(intra_pp_terms)
    s_inter = fsum(inter_pp_terms)
    s_total = discrete_coulomb_unit_sum(inv_mat, is_p)
    # Effective harmonic inter-alpha distance d_inter_eff = 12 / s_inter (in units of ell_bond)
    d_inter_eff = mpf(12) / s_inter

    # Also verify exact Lean theorem `carbon12_equilateral_three_alpha_coulomb` on idealized
    # two-scale `alphaClusterInvDist` with intraBond = 1, interDist = d_inter_eff:
    lean_two_scale_sum = mpf(3) / mpf(1) + mpf(12) / d_inter_eff
    lean_two_scale_diff = fabs(s_total - lean_two_scale_sum)

    return {
        "cluster_coords_scaled_sqrt2": coords,
        "intra_alpha_edges_all_unit_length": intra_all_unit,
        "proton_count_Z": sum(1 for b in is_p if b),
        "intra_alpha_proton_pairs": len(intra_pp_terms),
        "inter_alpha_proton_pairs": len(inter_pp_terms),
        "total_proton_pairs": len(intra_pp_terms) + len(inter_pp_terms),
        "unit_sum_intra": s_intra,
        "unit_sum_inter": s_inter,
        "unit_sum_total": s_total,
        "effective_inter_alpha_dist_over_ell_bond": d_inter_eff,
        "lean_two_scale_identity_diff": lean_two_scale_diff,
        "distance_shell_histogram": {str(k): v for k, v in sorted(hist.items())},
    }


# =============================================================================
# § 3. Wave-3 Strong Ball (N1) + Spin-Orbit Symmetry/Shell (N2) + Pairing (N3)
# =============================================================================

def close_packed_f0(k: int) -> int:
    return (10 * (k ** 3) + 15 * (k ** 2) + 11 * k + 3) // 3


def close_packed_f0_bdry(k: int) -> int:
    return 1 if k == 0 else (10 * (k ** 2) + 2)


def close_packed_f3(k: int) -> int:
    return 20 * (k ** 3)


def apollonian_3tree_f_vec(A: int) -> dict[str, int]:
    if A <= 1:
        return {"f0": A, "f1": 0, "f2": 0, "f3": 0, "f0_bdry": A, "f2_bdry": 0}
    if A == 2:
        return {"f0": 2, "f1": 1, "f2": 0, "f3": 0, "f0_bdry": 2, "f2_bdry": 0}
    if A == 3:
        return {"f0": 3, "f1": 3, "f2": 1, "f3": 0, "f0_bdry": 3, "f2_bdry": 1}
    return {
        "f0": A,
        "f1": 3 * A - 6,
        "f2": 3 * A - 8,
        "f3": A - 3,
        "f0_bdry": A,
        "f2_bdry": 2 * A - 4,
    }


def close_packed_shell_ball_f_vec(A: int) -> dict[str, int]:
    """Exact 3D close-packed shell-grown compact-ball triangulation from Lane N1
    (`BallManifoldTriangulationAndSurfaceScaling.lean`)."""
    if A <= 4:
        return apollonian_3tree_f_vec(A)
    if A < 13:
        steps = A - 4
        f0 = A
        f0_b = 4 + steps
        f3 = 1 + 2 * steps
        f2 = 2 * f3 + f0_b - 2
        f1 = f0 + f3 + f0_b - 3
        return {"f0": f0, "f1": f1, "f2": f2, "f3": f3, "f0_bdry": f0_b, "f2_bdry": 2 * f0_b - 4}
    k = 1
    while close_packed_f0(k + 1) <= A:
        k += 1
    a_k = close_packed_f0(k)
    if A == a_k:
        f0 = a_k
        f0_b = close_packed_f0_bdry(k)
        f3 = close_packed_f3(k)
    else:
        a_next = close_packed_f0(k + 1)
        da_shell = a_next - a_k
        rem = A - a_k
        f0 = A
        df3_shell = close_packed_f3(k + 1) - close_packed_f3(k)
        f3 = close_packed_f3(k) + (df3_shell * rem) // da_shell
        dbdry_shell = close_packed_f0_bdry(k + 1) - close_packed_f0_bdry(k)
        f0_b = close_packed_f0_bdry(k) + (dbdry_shell * rem) // da_shell
    f2 = 2 * f3 + f0_b - 2
    f1 = f0 + f3 + f0_b - 3
    return {"f0": f0, "f1": f1, "f2": f2, "f3": f3, "f0_bdry": f0_b, "f2_bdry": 2 * f0_b - 4}


def pauli_capped_shell_ball_f_vec(Z: int, N: int) -> dict[str, int]:
    """Pauli `(2p, 2n)` capped 3D close-packed shell ball from Lane N1:
    balanced core `A_core = 2 * min(Z, N)` forms `close_packed_shell_ball(A_core)`, while
    `D = |N - Z|` excess majority nucleons attach via maximal Pauli-legal degree-2 mixed-isospin
    triangles (`+2D` edges, `+D` triangles, `+0` tetrahedra, preserving `chi = 1`)."""
    A = Z + N
    base = close_packed_shell_ball_f_vec(A)
    if A <= 3 or Z == N:
        return base
    a_core = 2 * (Z if Z <= N else N)
    d_exc = A - a_core
    core_t = close_packed_shell_ball_f_vec(a_core)
    f0_b = core_t["f0_bdry"] + d_exc
    return {
        "f0": A,
        "f1": core_t["f1"] + 2 * d_exc,
        "f2": core_t["f2"] + d_exc,
        "f3": core_t["f3"],
        "f0_bdry": f0_b,
        "f2_bdry": 2 * f0_b - 4,
    }


def _int_det_3d(
    p0: tuple[int, int, int],
    p1: tuple[int, int, int],
    p2: tuple[int, int, int],
    p3: tuple[int, int, int],
) -> int:
    """Exact signed integer determinant `det([p1 - p0, p2 - p0, p3 - p0]) = 6 * SignedVolume`."""
    x1, y1, z1 = p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2]
    x2, y2, z2 = p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2]
    x3, y3, z3 = p3[0] - p0[0], p3[1] - p0[1], p3[2] - p0[2]
    return x1 * (y2 * z3 - y3 * z2) - y1 * (x2 * z3 - x3 * z2) + z1 * (x2 * y3 - x3 * y2)


def _is_canonical_kuhn_simplex(
    quad: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]],
) -> bool:
    """True iff the 4 lattice points form a canonical Freudenthal-Kuhn 3-simplex of a unit cube
    `[x0, x0+1] x [y0, y0+1] x [z0, z0+1]`, i.e., when sorted lexicographically `s0 < s1 < s2 < s3`,
    the 3 step vectors `s_{i+1} - s_i` are a permutation of `{(1,0,0), (0,1,0), (0,0,1)}`."""
    s = sorted(quad)
    steps = {
        (s[i + 1][0] - s[i][0], s[i + 1][1] - s[i][1], s[i + 1][2] - s[i][2])
        for i in range(3)
    }
    return steps == {(1, 0, 0), (0, 1, 0), (0, 0, 1)}


def _canonical_kuhn_key(
    quad: tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]],
) -> tuple[tuple[int, int, int], tuple[tuple[int, int, int], ...]]:
    """Unique `(base_corner_s0, step_permutation)` key of a canonical Freudenthal-Kuhn 3-simplex."""
    s = sorted(quad)
    steps = tuple(
        (s[i + 1][0] - s[i][0], s[i + 1][1] - s[i][1], s[i + 1][2] - s[i][2])
        for i in range(3)
    )
    return (s[0], steps)


_KUHN_BALL_CACHE: dict[int, dict[str, object]] = {}


def build_explicit_3d_kuhn_ball_complex(A: int) -> dict[str, object]:
    """Self-contained coordinate-verified 3D Euclidean Freudenthal-Kuhn lattice tetrahedral ball
    in `Z^3` (interior-disjoint geometric subcomplex of `K(Z^3)`):
    - Initializes at `A = 4` with the unit-volume Freudenthal-Kuhn 3-simplex
      `{(0,0,0), (1,0,0), (1,1,0), (1,1,1)}` (`|det| == 1`, volume `1/6`).
    - At each step `v_idx` (`4 <= v_idx < A`), pops the nearest unused lattice site `pt` with at
      least one strictly visible outward-oriented canonical Kuhn boundary triangle
      (`_int_det_3d(a, b, c, pt) > 0` and `_is_canonical_kuhn_simplex`), grows a topological disk
      patch of visible canonical Kuhn boundary faces (`deg 1`, `deg 2` ridge-cap, or `deg 3`
      pocket-bury), and attaches canonical Kuhn tetrahedra `(a, b, c, v_idx)`.
    - Explicitly verifies `|det([v1-v0, v2-v0, v3-v0])| == 1 > 0`, `_is_canonical_kuhn_simplex`,
      and distinct `(s0, step_permutation)` keys on 100% of 3-simplices (zero interior overlaps,
      exact union volume `f3 / 6`), manifold face incidence (`1` on boundary, `2` in interior),
      and genuine `O(A^{2/3})` boundary scaling (`f0_bdry = 188, f2_bdry = 372, f0_int = 20` at
      `A = 208`; `f0_bdry = 214, f2_bdry = 424, f0_int = 24` at `A = 238`).
    """
    if A in _KUHN_BALL_CACHE:
        return _KUHN_BALL_CACHE[A]

    pts: list[tuple[int, int, int]] = []
    rad_bound = 6
    while len(pts) < max(A + 64, 500):
        pts.clear()
        for x in range(-rad_bound, rad_bound + 1):
            for y in range(-rad_bound, rad_bound + 1):
                for z in range(-rad_bound, rad_bound + 1):
                    pts.append((x, y, z))
        rad_bound += 1

    pts.sort(
        key=lambda p: (
            (2 * p[0] - 1) ** 2 + (2 * p[1] - 1) ** 2 + (2 * p[2] - 1) ** 2,
            abs(2 * p[0] - 1) + abs(2 * p[1] - 1) + abs(2 * p[2] - 1),
            p[0],
            p[1],
            p[2],
        )
    )
    seed = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)]
    seed_set = set(seed)
    unused = [s for s in pts if s not in seed_set]
    ordered_coords = list(seed)

    if A <= 3:
        t_base = apollonian_3tree_f_vec(A)
        f1_b = 0 if A <= 1 else (1 if A == 2 else 3)
        res_small: dict[str, object] = {
            **t_base,
            "f1_bdry": f1_b,
            "f0_int": 0,
            "cycle_excess": 0,
            "min_abs_det": 1,
            "max_abs_det": 1,
            "total_six_mul_volume": 0,
            "all_cells_canonical_kuhn": True,
            "unique_kuhn_cells_eq_f3": True,
            "all_cells_strict_positive_volume": True,
            "all_interior_triangles_shared_by_two": True,
            "max_vertex_degree": max(0, A - 1),
        }
        _KUHN_BALL_CACHE[A] = res_small
        return res_small

    def _orient_outward(a: int, b: int, c: int, op: int) -> tuple[int, int, int]:
        d_val = _int_det_3d(ordered_coords[a], ordered_coords[b], ordered_coords[c], ordered_coords[op])
        if d_val == 0:
            raise ValueError("Degenerate zero-determinant 3-simplex in 3D orientation.")
        return (a, b, c) if d_val < 0 else (a, c, b)

    tetrahedra: list[tuple[int, int, int, int]] = [(0, 1, 2, 3)]
    bdry_map: dict[frozenset[int], tuple[int, int, int]] = {}
    for a_i, b_i, c_i, op_i in [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 3, 1), (1, 2, 3, 0)]:
        bdry_map[frozenset((a_i, b_i, c_i))] = _orient_outward(a_i, b_i, c_i, op_i)

    for v_idx in range(4, A):
        chosen_pos = -1
        vis: list[tuple[int, int, frozenset[int], tuple[int, int, int]]] = []
        for u_pos, cand_pt in enumerate(unused):
            cand_vis: list[tuple[int, int, frozenset[int], tuple[int, int, int]]] = []
            for fs, (a_i, b_i, c_i) in bdry_map.items():
                d_val = _int_det_3d(ordered_coords[a_i], ordered_coords[b_i], ordered_coords[c_i], cand_pt)
                if d_val > 0:
                    quad = (ordered_coords[a_i], ordered_coords[b_i], ordered_coords[c_i], cand_pt)
                    if _is_canonical_kuhn_simplex(quad):
                        dist2 = sum(
                            (ordered_coords[u][0] - cand_pt[0]) ** 2
                            + (ordered_coords[u][1] - cand_pt[1]) ** 2
                            + (ordered_coords[u][2] - cand_pt[2]) ** 2
                            for u in (a_i, b_i, c_i)
                        )
                        cand_vis.append((dist2, d_val, fs, (a_i, b_i, c_i)))
            if cand_vis:
                chosen_pos = u_pos
                vis = cand_vis
                break

        if chosen_pos < 0:
            raise ValueError(f"No visible canonical Freudenthal-Kuhn vertex found at step {v_idx}.")
        pt = unused.pop(chosen_pos)
        ordered_coords.append(pt)

        vis.sort(key=lambda x: (x[0], tuple(sorted(x[3]))))
        _, _, fs0, tri0 = vis[0]
        patch: list[tuple[frozenset[int], tuple[int, int, int]]] = [(fs0, tri0)]

        for _, _, fs_c, tri_c in vis[1:]:
            patch_verts: set[int] = set()
            patch_bdry_edges: set[frozenset[int]] = set()
            for _, (pa, pb, pc) in patch:
                patch_verts.update((pa, pb, pc))
                for e_f in (frozenset((pa, pb)), frozenset((pa, pc)), frozenset((pb, pc))):
                    if e_f in patch_bdry_edges:
                        patch_bdry_edges.remove(e_f)
                    else:
                        patch_bdry_edges.add(e_f)
            tri_edges = [
                frozenset((tri_c[0], tri_c[1])),
                frozenset((tri_c[0], tri_c[2])),
                frozenset((tri_c[1], tri_c[2])),
            ]
            shared_edges = [e_f for e_f in tri_edges if e_f in patch_bdry_edges]
            if len(shared_edges) == 1:
                opp_v = (set(tri_c) - set(shared_edges[0])).pop()
                if opp_v not in patch_verts:
                    patch.append((fs_c, tri_c))
            elif len(shared_edges) == 2:
                common_v = set(shared_edges[0]).intersection(shared_edges[1]).pop()
                deg_in_bdry = sum(1 for f_all in bdry_map if common_v in f_all)
                deg_in_patch = sum(1 for _, t_p in patch if common_v in t_p)
                if deg_in_bdry == deg_in_patch + 1 and len(bdry_map) > len(patch) + 1:
                    patch.append((fs_c, tri_c))

        for fs_p, (a_i, b_i, c_i) in patch:
            t_sorted = tuple(sorted((a_i, b_i, c_i, v_idx)))
            tetrahedra.append((t_sorted[0], t_sorted[1], t_sorted[2], t_sorted[3]))
            del bdry_map[fs_p]
            for na, nb, nc, nop in [
                (a_i, b_i, v_idx, c_i),
                (a_i, c_i, v_idx, b_i),
                (b_i, c_i, v_idx, a_i),
            ]:
                nfs = frozenset((na, nb, nc))
                if nfs in bdry_map:
                    del bdry_map[nfs]
                else:
                    bdry_map[nfs] = _orient_outward(na, nb, nc, nop)

    all_edges: set[tuple[int, int]] = set()
    tri_incidence_count: dict[tuple[int, int, int], int] = {}
    abs_dets: list[int] = []
    kuhn_flags: list[bool] = []
    unique_kuhn_keys: set[tuple[tuple[int, int, int], tuple[tuple[int, int, int], ...]]] = set()
    vertex_deg: dict[int, int] = {i: 0 for i in range(A)}

    for v0, v1, v2, v3 in tetrahedra:
        quad = (ordered_coords[v0], ordered_coords[v1], ordered_coords[v2], ordered_coords[v3])
        d_abs = abs(_int_det_3d(quad[0], quad[1], quad[2], quad[3]))
        abs_dets.append(d_abs)
        kuhn_flags.append(_is_canonical_kuhn_simplex(quad))
        unique_kuhn_keys.add(_canonical_kuhn_key(quad))
        all_edges.update([(v0, v1), (v0, v2), (v0, v3), (v1, v2), (v1, v3), (v2, v3)])
        for t_face in [(v0, v1, v2), (v0, v1, v3), (v0, v2, v3), (v1, v2, v3)]:
            tri_incidence_count[t_face] = tri_incidence_count.get(t_face, 0) + 1

    for u_i, v_i in all_edges:
        vertex_deg[u_i] += 1
        vertex_deg[v_i] += 1

    bdry_verts: set[int] = set()
    bdry_edges_final: set[tuple[int, int]] = set()
    for fs in bdry_map:
        a_i, b_i, c_i = sorted(fs)
        bdry_verts.update((a_i, b_i, c_i))
        bdry_edges_final.update([(a_i, b_i), (a_i, c_i), (b_i, c_i)])

    all_manifold_tris_ok = all(
        (cnt == 1 if frozenset(t_face) in bdry_map else cnt == 2)
        for t_face, cnt in tri_incidence_count.items()
    )

    f0 = A
    f1 = len(all_edges)
    f2 = len(tri_incidence_count)
    f3 = len(tetrahedra)
    f0_b = len(bdry_verts)
    f1_b = len(bdry_edges_final)
    f2_b = len(bdry_map)

    res: dict[str, object] = {
        "f0": f0,
        "f1": f1,
        "f2": f2,
        "f3": f3,
        "f0_bdry": f0_b,
        "f1_bdry": f1_b,
        "f2_bdry": f2_b,
        "f0_int": f0 - f0_b,
        "cycle_excess": f3 - (f0 - 3),
        "min_abs_det": min(abs_dets),
        "max_abs_det": max(abs_dets),
        "total_six_mul_volume": sum(abs_dets),
        "all_cells_canonical_kuhn": all(kuhn_flags),
        "unique_kuhn_cells_eq_f3": len(unique_kuhn_keys) == f3,
        "all_cells_strict_positive_volume": all(d == 1 for d in abs_dets),
        "all_interior_triangles_shared_by_two": all_manifold_tris_ok,
        "max_vertex_degree": max(vertex_deg.values()),
    }
    _KUHN_BALL_CACHE[A] = res
    return res


def verify_compact_3ball_triangulation(t: dict[str, object]) -> bool:
    """Verify Euler characteristic (`chi = 1` in bulk, `chi = 2` on `S^2` boundary for `A >= 4`)
    and Dehn-Sommerville incidence (`2 * f2 - f2_bdry == 4 * f3`, `2 * f1_bdry == 3 * f2_bdry`)."""
    f0 = int(t["f0"])
    f1 = int(t["f1"])
    f2 = int(t["f2"])
    f3 = int(t["f3"])
    f0_b = int(t["f0_bdry"])
    f2_b = int(t["f2_bdry"])
    f1_b = int(t.get("f1_bdry", 3 * f0_b - 6 if f0_b >= 4 else 0))
    if f0 <= 3:
        return (f0 - f1 + f2 - f3) == (1 if f0 >= 1 else 0)
    return (
        (f0 - f1 + f2 - f3 == 1)
        and (f0_b - f1_b + f2_b == 2)
        and (2 * f1_b == 3 * f2_b)
        and (2 * f2 - f2_b == 4 * f3)
        and (4 <= f0_b <= f0)
    )


def pauli_capped_kuhn_ball_f_vec(Z: int, N: int) -> dict[str, int]:
    """Pauli `(2p, 2n)` capped 3D Freudenthal-Kuhn lattice ball (`pauli_k4_balanced_isospin`):
    balanced core `A_core = 2 * min(Z, N)` forms `build_explicit_3d_kuhn_ball_complex(A_core)`,
    while `D = |N - Z|` excess majority nucleons attach via maximal Pauli-legal degree-2
    mixed-isospin triangles (`+2D` edges, `+D` triangles, `+0` tetrahedra, preserving `chi = 1`)."""
    A = Z + N
    base_t = build_explicit_3d_kuhn_ball_complex(A)
    if A <= 3 or Z == N:
        return {
            "f0": int(base_t["f0"]),
            "f1": int(base_t["f1"]),
            "f2": int(base_t["f2"]),
            "f3": int(base_t["f3"]),
            "f0_bdry": int(base_t["f0_bdry"]),
            "f1_bdry": int(base_t["f1_bdry"]),
            "f2_bdry": int(base_t["f2_bdry"]),
            "f0_int": int(base_t["f0_int"]),
            "A_core": A,
            "D_excess": 0,
        }
    a_core = 2 * (Z if Z <= N else N)
    d_exc = A - a_core
    core_t = build_explicit_3d_kuhn_ball_complex(a_core)
    f0_b = int(core_t["f0_bdry"]) + d_exc
    return {
        "f0": A,
        "f1": int(core_t["f1"]) + 2 * d_exc,
        "f2": int(core_t["f2"]) + d_exc,
        "f3": int(core_t["f3"]),
        "f0_bdry": f0_b,
        "f1_bdry": 3 * f0_b - 6,
        "f2_bdry": 2 * f0_b - 4,
        "f0_int": int(core_t["f0_int"]),
        "A_core": a_core,
        "D_excess": d_exc,
    }


def ho_excitation_quanta_3d(m_fermions: int) -> int:
    """Exact total 3D isotropic harmonic-oscillator shell excitation quanta
    `sum_{i=1}^{m_fermions} N_osc(i)` above the `1s` (`N_osc = 0`) ground shell for `m_fermions`
    identical spin-1/2 nucleons (`capacity(N_osc) = (N_osc + 1)*(N_osc + 2)`), matching Lane N1."""
    rem = m_fermions
    n_osc = 0
    total_quanta = 0
    while rem > 0:
        cap = (n_osc + 1) * (n_osc + 2)
        take = rem if rem <= cap else cap
        total_quanta += take * n_osc
        rem -= take
        n_osc += 1
    return total_quanta


SPECTROSCOPIC_SUBSHELLS: list[tuple[str, int, int, int, bool, int]] = [
    ("1s_{1/2}", 0, 0, 1, True, 2),
    ("1p_{3/2}", 1, 1, 3, True, 4),
    ("1p_{1/2}", 1, 1, 1, False, 2),
    ("1d_{5/2}", 2, 2, 5, True, 6),
    ("2s_{1/2}", 2, 0, 1, True, 2),
    ("1d_{3/2}", 2, 2, 3, False, 4),
    ("1f_{7/2}", 3, 3, 7, True, 8),
    ("2p_{3/2}", 3, 1, 3, True, 4),
    ("1f_{5/2}", 3, 3, 5, False, 6),
    ("2p_{1/2}", 3, 1, 1, False, 2),
    ("1g_{9/2}", 4, 4, 9, True, 10),
    ("1g_{7/2}", 4, 4, 7, False, 8),
    ("2d_{5/2}", 4, 2, 5, True, 6),
    ("2d_{3/2}", 4, 2, 3, False, 4),
    ("3s_{1/2}", 4, 0, 1, True, 2),
    ("1h_{11/2}", 5, 5, 11, True, 12),
    ("1h_{9/2}", 5, 5, 9, False, 10),
    ("2f_{7/2}", 5, 3, 7, True, 8),
    ("2f_{5/2}", 5, 3, 5, False, 6),
    ("3p_{3/2}", 5, 1, 3, True, 4),
    ("3p_{1/2}", 5, 1, 1, False, 2),
    ("1i_{13/2}", 6, 6, 13, True, 14),
    ("1i_{11/2}", 6, 6, 11, False, 12),
    ("2g_{9/2}", 6, 4, 9, True, 10),
    ("2g_{7/2}", 6, 4, 7, False, 8),
    ("3d_{5/2}", 6, 2, 5, True, 6),
    ("3d_{3/2}", 6, 2, 3, False, 4),
    ("4s_{1/2}", 6, 0, 1, True, 2),
    ("1j_{15/2}", 7, 7, 15, True, 16),
]


def build_spin_orbit_levels(kappa_so: mpf) -> list[mpf]:
    """Monotone single-particle dimensionless spin-orbit spectrum (`SpinOrbitShellClosureAndSymmetryEnergy.lean`)."""
    with mp.workdps(DPS):
        levels: list[mpf] = []
        for _lbl, n_osc, ell, _two_j, aligned_plus, deg in SPECTROSCOPIC_SUBSHELLS:
            eps_ho = mpf(n_osc) + mpf(3) / mpf(2)
            two_l_s = mpf(ell) if aligned_plus else -mpf(ell + 1)
            eps_so = eps_ho - kappa_so * two_l_s - (kappa_so ** 2) * mpf(ell * (ell + 1)) / mpf(2)
            for _ in range(deg):
                levels.append(eps_so)
        levels.sort()
        return levels


def smooth_weyl_fill_dimless(m_count: int) -> mpf:
    """Centered smooth 3D isotropic Weyl oscillator cumulative energy `E_smooth(M)`
    matching `nuclear_spin_orbit_shells_and_symmetry_probe._smooth_weyl_fill_dimless`:
    at exact oscillator closure `M = (u^3 - u)/3` (`u = K + 2`), `E_HO(M) = (3/4)*M*u`, while
    at mid-shell the discrete sum exceeds `(3/4)*M*u` by `+(1/8)*(u^2 - 1)`. Using
    `u_0 = (3*M)^{1/3}`, `u_Weyl = u_0 + 1/(3*u_0)`, and the mid-point shift `+(1/16)*(u_0^2 - 1)`
    centers `E_smooth(M) - E_fill_SO(M)` around zero so doubly-magic closures (`4He, 16O, 40Ca,
    208Pb`) exhibit strictly positive shell stabilization and mid-shells (`24Mg`) are negative."""
    if m_count <= 0:
        return mpf(0)
    m_mp = mpf(m_count)
    u_0 = (mpf(3) * m_mp) ** (mpf(1) / mpf(3))
    u_weyl = u_0 + mpf(1) / (mpf(3) * u_0)
    return (mpf(3) / mpf(4)) * m_mp * u_weyl + (mpf(1) / mpf(16)) * (u_0 ** 2 - mpf(1))


def spin_orbit_symmetry_and_shell_mev(sub: dict[str, mpf], levels: list[mpf], Z: int, N: int) -> dict[str, mpf]:
    """Compute parameter-free 3D Pauli/Fermi harmonic-oscillator kinetic promotion, discrete
    spin-orbit Pauli asymmetry penalty, quadratic Fermi symmetry energy, centered Weyl shell
    stabilization, and Temperley-Lieb seniority-0 pairing offset, with Hecke (`E0_bare`, `E0_inf`)
    and Compton (`E_osc_compton_bare = m_e / (q - 1)^2`) oscillator scales labeled explicitly."""
    with mp.workdps(DPS):
        A = Z + N
        a_third = mpf(A) ** (mpf(1) / mpf(3))
        hw_compton_bare = sub["E_osc_compton_bare_MeV"] / a_third
        hw_hecke_bare = sub["E0_bare_MeV"] / a_third
        hw_hecke_inf = sub["E0_inf_MeV"] / a_third

        n_ho_quanta = ho_excitation_quanta_3d(Z) + ho_excitation_quanta_3d(N)
        e_kin_ho_hecke_bare = mpf(n_ho_quanta) * hw_hecke_bare
        e_kin_ho_hecke_inf = mpf(n_ho_quanta) * hw_hecke_inf
        e_kin_ho_compton_bare = mpf(n_ho_quanta) * hw_compton_bare

        ez = fsum(levels[:Z])
        en = fsum(levels[:N])
        m_lo = A // 2
        m_hi = A - m_lo
        emid = (fsum(levels[:m_lo]) + fsum(levels[:m_hi])) / mpf(2)
        asym_dimless = ez + en - mpf(2) * emid
        e_sym_disc_compton = hw_compton_bare * asym_dimless
        e_sym_disc_hecke_bare = hw_hecke_bare * asym_dimless
        e_sym_quad_compton = sub["a_sym_compton_MeV"] * (mpf(N - Z) ** 2) / mpf(A)

        dz_shell = smooth_weyl_fill_dimless(Z) - ez
        dn_shell = smooth_weyl_fill_dimless(N) - en
        delta_shell_dimless = dz_shell + dn_shell
        delta_shell_hecke_bare = hw_hecke_bare * delta_shell_dimless
        delta_shell_hecke_inf = hw_hecke_inf * delta_shell_dimless
        delta_shell_compton_bare = hw_compton_bare * delta_shell_dimless

        # Temperley-Lieb seniority-0 pairing offset (`SeniorityPairingAndHoyleTriadThreshold.tlPairingGap`):
        # 0 for A < 4, +Delta_TL for even-even, 0 for odd-A, -Delta_TL for odd-odd (A >= 4)
        dp_bare = sub["delta_TL_bare_MeV"]
        dp_inf = sub["delta_TL_inf_MeV"]
        if A < 4:
            e_pair_bare = mpf(0)
            e_pair_inf = mpf(0)
        elif (Z % 2 == 0) and (N % 2 == 0):
            e_pair_bare = dp_bare
            e_pair_inf = dp_inf
        elif (Z % 2 == 1) and (N % 2 == 1):
            e_pair_bare = -dp_bare
            e_pair_inf = -dp_inf
        else:
            e_pair_bare = mpf(0)
            e_pair_inf = mpf(0)

        return {
            "N_ho_excitation_quanta": mpf(n_ho_quanta),
            "E_kin_ho_hecke_bare_MeV": e_kin_ho_hecke_bare,
            "E_kin_ho_hecke_inf_MeV": e_kin_ho_hecke_inf,
            "E_kin_ho_compton_bare_MeV": e_kin_ho_compton_bare,
            "E_sym_disc_compton_MeV": e_sym_disc_compton,
            "E_sym_disc_hecke_bare_MeV": e_sym_disc_hecke_bare,
            "E_sym_quad_compton_MeV": e_sym_quad_compton,
            "delta_shell_weyl_so_dimless": delta_shell_dimless,
            "delta_E_shell_hecke_bare_MeV": delta_shell_hecke_bare,
            "delta_E_shell_hecke_inf_MeV": delta_shell_hecke_inf,
            "delta_E_shell_compton_bare_MeV": delta_shell_compton_bare,
            "delta_E_pair_TL_bare_MeV": e_pair_bare,
            "delta_E_pair_TL_inf_MeV": e_pair_inf,
        }


# =============================================================================
# § 4. Benchmarks: 13 Nuclei (2H..238U), 7 Mirror Pairs, & alpha_cluster Retirement
# =============================================================================

BENCHMARK_NUCLEI: list[tuple[str, int, int]] = [
    ("2H", 1, 1),
    ("3H", 1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("12C", 6, 6),
    ("16O", 8, 8),
    ("24Mg", 12, 12),
    ("40Ca", 20, 20),
    ("56Fe", 26, 30),
    ("120Sn", 50, 70),
    ("197Au", 79, 118),
    ("208Pb", 82, 126),
    ("238U", 92, 146),
]

MIRROR_PAIRS: list[tuple[str, int, int, str, int, int]] = [
    ("3H", 1, 2, "3He", 2, 1),
    ("7Li", 3, 4, "7Be", 4, 3),
    ("11B", 5, 6, "11C", 6, 5),
    ("13C", 6, 7, "13N", 7, 6),
    ("15N", 7, 8, "15O", 8, 7),
    ("17O", 8, 9, "17F", 9, 8),
    ("41Ca", 20, 21, "41Sc", 21, 20),
]


def legacy_continuum_coulomb_mev(alpha_hbar_c: mpf, Z: int, A: int) -> mpf:
    if Z < 2 or A < 1:
        return mpf(0)
    r_sph = LAMBDA_BAR_PI_FM * (mpf(A) ** (mpf(1) / mpf(3)))
    return (mpf(3) / mpf(5)) * mpf(Z * (Z - 1)) * alpha_hbar_c / r_sph


def fcc_ball_continuum_coulomb_mev(alpha_hbar_c: mpf, r0_fcc_fm: mpf, Z: int, A: int) -> mpf:
    if Z < 2 or A < 1:
        return mpf(0)
    r_fcc = r0_fcc_fm * (mpf(A) ** (mpf(1) / mpf(3)))
    return (mpf(3) / mpf(5)) * mpf(Z * (Z - 1)) * alpha_hbar_c / r_fcc


def _err_dict(b_pred: mpf, b_ame: mpf, sig_ame: mpf) -> dict[str, str]:
    delta = b_pred - b_ame
    pct = (delta / b_ame) * mpf(100)
    esig = (delta / sig_ame) if sig_ame > mpf(0) else mpf(0)
    return {
        "B_pred_MeV": fmt(b_pred, DPS),
        "delta_MeV": fmt(delta, DPS),
        "err_pct": fmt(pct, 16),
        "err_sigma": fmt(esig, 16),
    }


def audit_alpha_cluster_recursion_retirement(
    sub_2t: dict[str, mpf],
    bond_laws: dict[str, dict[str, mpf]],
    levels_2t: list[mpf],
) -> dict[str, object]:
    """Verify that retiring `alpha_cluster_recursion.py` (`B(n*alpha) = n*B(4He) + C(n,2)*c_aa`)
    leaves zero regressions on live pipelines and eliminates the refuted O(A^2) pair blowup."""
    from alpha_cluster_recursion import C_ALPHA_ALPHA_MEV, alpha_cluster_binding

    alpha_nuclei = [
        ("4He", 2, 2),
        ("8Be", 4, 4),
        ("12C", 6, 6),
        ("16O", 8, 8),
        ("20Ne", 10, 10),
        ("24Mg", 12, 12),
        ("40Ca", 20, 20),
    ]
    ahc = sub_2t["alpha_hbar_c_MeV_fm"]
    ell_32 = bond_laws["L2_three_halves_lambda_pi"]["ell_bond_fm"]

    rows = []
    for name, Z, N in alpha_nuclei:
        A = Z + N
        n_a = A // 4
        b_ame = AME_EXACT[(Z, A)]["B_AME_MeV"]

        # Legacy O(n_alpha^2) alpha_cluster_recursion:
        if n_a == 1:
            from magic_A_formula import magic_A_binding
            b_old = mpf(str(magic_A_binding(2, 2)["B_pred_MeV"]))
        else:
            b_old = mpf(str(alpha_cluster_binding(Z, N)["B_pred_MeV"]))
        err_old_pct = (b_old - b_ame) / b_ame * mpf(100)

        # Bounded-degree Wave-3 (coordinate-verified 3D Kuhn ball + Convention-D b2_log_D + core-consistent discrete Coulomb at 3/2 lambda_pi)
        fb = build_explicit_3d_kuhn_ball_complex(A)
        b_strong_d = (
            mpf(int(fb["f1"])) * sub_2t["b2_log_D_bare_MeV"]
            + mpf(int(fb["f2"])) * sub_2t["w3_bare_MeV"]
            + mpf(int(fb["f3"])) * sub_2t["w4_bare_MeV"]
        )
        coords = FCC_SITES_MASTER[:A]
        inv_mat, dist_hist = fcc_unit_inv_dist_matrix(coords)
        occ_core = core_consistent_pauli_proton_occupancy(A, Z)
        ec_core_32 = (ahc / ell_32) * discrete_coulomb_unit_sum(inv_mat, occ_core)
        total_all_pairs_unit = fsum(
            mpf(cnt) * (INV_SQRT_CACHE[k_sq] if k_sq < len(INV_SQRT_CACHE) else (mpf(1) / sqrt(mpf(k_sq))))
            for k_sq, cnt in dist_hist.items()
        )
        ec_sym_32 = (ahc / ell_32) * (mpf(Z * (Z - 1)) / mpf(A * (A - 1))) * total_all_pairs_unit
        so_info = spin_orbit_symmetry_and_shell_mev(sub_2t, levels_2t, Z, N)
        b_wave3_sym = (
            b_strong_d
            + so_info["delta_E_shell_hecke_bare_MeV"]
            + so_info["delta_E_pair_TL_bare_MeV"]
            - ec_sym_32
        )
        b_wave3_core = (
            b_strong_d
            + so_info["delta_E_shell_hecke_bare_MeV"]
            + so_info["delta_E_pair_TL_bare_MeV"]
            - ec_core_32
        )
        err_wave3_sym_pct = (b_wave3_sym - b_ame) / b_ame * mpf(100)
        err_wave3_core_pct = (b_wave3_core - b_ame) / b_ame * mpf(100)

        rows.append({
            "nuclide": name,
            "Z": Z,
            "N": N,
            "A": A,
            "n_alpha": n_a,
            "legacy_all_pairs_count": _int_comb(n_a, 2),
            "bounded_3tree_alpha_edges": (9 * n_a - 6) if n_a >= 3 else (6 * n_a),
            "B_AME_MeV": fmt(b_ame, DPS),
            "B_legacy_alpha_recursion_MeV": fmt(b_old, DPS),
            "err_legacy_alpha_recursion_pct": fmt(err_old_pct, 16),
            "B_wave3_kuhn_ball_logD_discSym_MeV": fmt(b_wave3_sym, DPS),
            "err_wave3_kuhn_ball_logD_discSym_pct": fmt(err_wave3_sym_pct, 16),
            "B_wave3_kuhn_ball_logD_discCorePauli_MeV": fmt(b_wave3_core, DPS),
            "err_wave3_kuhn_ball_logD_discCorePauli_pct": fmt(err_wave3_core_pct, 16),
        })

    # Asymptotic A=200 (n_alpha=50) blowup check on legacy formula vs linear bounded-degree:
    b_4he_magic = mpf(str(rows[0]["B_legacy_alpha_recursion_MeV"]))
    c_aa = mpf(str(C_ALPHA_ALPHA_MEV))
    b_old_a200_per_a = (mpf(50) * b_4he_magic + mpf(_int_comb(50, 2)) * c_aa) / mpf(200)
    fb_200 = build_explicit_3d_kuhn_ball_complex(200)
    b_wave3_a200_strong_per_a = (
        mpf(int(fb_200["f1"])) * sub_2t["b2_log_D_bare_MeV"]
        + mpf(int(fb_200["f2"])) * sub_2t["w3_bare_MeV"]
        + mpf(int(fb_200["f3"])) * sub_2t["w4_bare_MeV"]
    ) / mpf(200)

    # Check live runtime imports in qou_mass and canonical_mass:
    api_src = (REPO_ROOT / "qou-mass" / "src" / "qou_mass" / "api.py").read_text(encoding="utf-8")
    cm_src = (REPO_ROOT / "computations" / "canonical_mass.py").read_text(encoding="utf-8")
    zero_live_facade_imports = (
        ("import alpha_cluster_recursion" not in api_src)
        and ("from alpha_cluster_recursion" not in api_src)
        and ("alpha_cluster_recursion" not in cm_src)
    )

    return {
        "zero_live_facade_imports_in_qou_mass_and_canonical_mass": zero_live_facade_imports,
        "a200_kuhn_ball_all_cells_strict_positive_volume": bool(fb_200["all_cells_strict_positive_volume"]),
        "legacy_a200_strong_B_over_A_MeV_blowup": fmt(b_old_a200_per_a, 20),
        "wave3_a200_strong_B_over_A_MeV_bounded": fmt(b_wave3_a200_strong_per_a, 20),
        "alpha_chain_comparison_rows": rows,
    }


def main() -> int:
    mp.mp.dps = DPS
    q_proton = q_at(DPS)
    q_muon = q_muon_at(DPS)
    q_2t = q_two_term_borromean_at(DPS)

    sub_2t = derive_substrate_at_q(q_2t)
    sub_proton = derive_substrate_at_q(q_proton)
    sub_muon = derive_substrate_at_q(q_muon)

    # Cross-check the 80-dps Form-B photon against `coulomb_energy.alpha_em_inv_bring_schwinger` at 80-dps q_proton
    ainv_mod_check = mpf(str(alpha_em_inv_bring_schwinger(q=q_proton)))
    ainv_mod_diff = fabs(sub_proton["alpha_em_inv_form_b"] - ainv_mod_check)
    tl_pairing_id_diff = (
        sub_2t["delta_TL_closed_form_diff"]
        + sub_proton["delta_TL_closed_form_diff"]
        + sub_muon["delta_TL_closed_form_diff"]
    )

    bond_laws = build_compton_bond_length_laws()
    c_fcc = (mpf(3) / (mpf(4) * pi * sqrt(mpf(2)))) ** (mpf(1) / mpf(3))
    eta_fcc = pi * sqrt(mpf(2)) / mpf(6)
    eta_fcc_sq_diff = fabs((eta_fcc ** 2) - (pi ** 2) / mpf(18))
    c_fcc_in_bounds = (mpf(11) / mpf(20) < c_fcc) and (c_fcc < mpf(14) / mpf(25))

    levels_2t = build_spin_orbit_levels(sub_2t["kappa_SO"])
    levels_proton = build_spin_orbit_levels(sub_proton["kappa_SO"])
    levels_muon = build_spin_orbit_levels(sub_muon["kappa_SO"])

    # Cross-check self-contained Kuhn ball builder against Lane N1 probe implementation:
    from nuclear_3d_ball_manifold_triangulation_probe import (
        build_explicit_3d_fcc_delone_ball_complex as _lane_n1_kuhn_ball,
    )

    # 1. Verify Carbon-12 equilateral 3-alpha cluster (`3 + 12 = 15` pairs) & O-16 (`4 + 24 = 28`)
    c12_3alpha = build_carbon12_equilateral_3alpha_cluster()
    ahc_2t = sub_2t["alpha_hbar_c_MeV_fm"]
    c12_3alpha_ec_by_law: dict[str, str] = {}
    for lkey, linfo in bond_laws.items():
        c12_3alpha_ec_by_law[lkey] = fmt(
            (ahc_2t / linfo["ell_bond_fm"]) * c12_3alpha["unit_sum_total"], DPS
        )

    # 2. Verify Lean continuum-sphere distortion cubes at A=3 (72/125) and A=4 (54/125)
    ell_ref = bond_laws["L1_lambda_pi"]["ell_bond_fm"]
    ec_disc_he3_l1 = ahc_2t / ell_ref
    ec_sph_he3_l1 = legacy_continuum_coulomb_mev(ahc_2t, 2, 3)
    ec_sph_he4_l1 = legacy_continuum_coulomb_mev(ahc_2t, 2, 4)
    distort_cube_a3_diff = fabs(((ec_sph_he3_l1 / ec_disc_he3_l1) ** 3) - (mpf(72) / mpf(125)))
    distort_cube_a4_diff = fabs(((ec_sph_he4_l1 / ec_disc_he3_l1) ** 3) - (mpf(54) / mpf(125)))

    # 3. Evaluate all 13 Benchmark Nuclei (2H .. 238U): Discrete Coulomb + FCC Sixth-Power + Joint Wave-3
    max_sixth_power_diff = mpf(0)
    he3_single_bond_diff = mpf(0)
    he4_single_bond_diff = mpf(0)
    z_le_1_zero_ok = True
    all_kuhn_positive_vol_ok = True
    all_kuhn_manifold_incidence_ok = True
    all_kuhn_compact_3ball_ok = True
    all_kuhn_surface_scaling_ok = True
    all_kuhn_lane_n1_match_ok = True
    doubly_magic_shell_signs_ok = True

    benchmark_rows: list[dict[str, object]] = []

    print("========================================================================================================================================")
    print("  Lane N4: 80-dps Simplicial Discrete Coulomb, 3D FCC Packing Radius, & Joint Wave-3 Nuclear Synthesis (Zero Fitting, Zero Float64)")
    print("========================================================================================================================================")
    print("  Form-B Bring-Schwinger 1/alpha_EM(q_2t) = " + mp.nstr(sub_2t["alpha_em_inv_form_b"], 18))
    print("  alpha_EM(q_2t)*hbar*c = " + mp.nstr(ahc_2t, 15) + " MeV*fm | lambda_bar_pi = " + mp.nstr(LAMBDA_BAR_PI_FM, 12) + " fm")
    print("  Delta_TL(q_2t, bare)  = " + mp.nstr(sub_2t["delta_TL_bare_MeV"], 12) + " MeV (= (1/2)*w3_GPMT*[2]_q = E0/(2*[3]_q))")
    print("  3D FCC packing constant c_FCC = (3/(4*pi*sqrt(2)))^(1/3) = " + mp.nstr(c_fcc, 15))
    for lkey, linfo in bond_laws.items():
        print(
            f"    {lkey:<28s}: ell_bond = {mp.nstr(linfo['ell_bond_fm'], 8):>10s} fm  ->  "
            f"r0_FCC = {mp.nstr(linfo['r0_fcc_fm'], 8):>10s} fm"
        )
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(
        f"{'Nucl':<6} {'Z':>3} {'N':>3} {'A':>3} | {'EC_sym(L2)':>10} {'EC_cPl(L2)':>10} {'EC_FCC(L2)':>10} | "
        f"{'B_AME':>8} {'KuhnSO(L2)':>10} {'ShStat(L2)':>10} {'ShHOKin(L2)':>11} {'PCap(L2)':>9}"
    )
    print("-" * 136)

    for name, Z, N in BENCHMARK_NUCLEI:
        A = Z + N
        b_ame = AME_EXACT[(Z, A)]["B_AME_MeV"]
        sig_ame = AME_EXACT[(Z, A)]["sigma_AME_MeV"]

        coords = FCC_SITES_MASTER[:A]
        inv_mat, dist_hist = fcc_unit_inv_dist_matrix(coords)

        # Primary physical discrete Coulomb evaluations:
        # (1) Isospin-symmetrized all-pairs projection Z(Z-1)/(A(A-1)) * sum_{u<v} 1/d_{uv}
        total_all_pairs_unit = fsum(
            mpf(cnt) * (INV_SQRT_CACHE[k_sq] if k_sq < len(INV_SQRT_CACHE) else (mpf(1) / sqrt(mpf(k_sq))))
            for k_sq, cnt in dist_hist.items()
        )
        s_unit_sym = (
            (mpf(Z * (Z - 1)) / mpf(A * (A - 1))) * total_all_pairs_unit
            if (Z >= 2 and A >= 2)
            else mpf(0)
        )
        # (2) Core-consistent Pauli `(2p, 2n)` radial occupancy (`A_core = 2*min(Z,N)` + outer skin)
        occ_core_pauli = core_consistent_pauli_proton_occupancy(A, Z)
        s_unit_core_pauli = discrete_coulomb_unit_sum(inv_mat, occ_core_pauli)

        # Diagnostic classical Thomson-conductor skin lower bound (never used in nuclear branches):
        occ_skin_lb = thomson_conductor_skin_lower_bound_occupancy(inv_mat, Z)
        s_unit_skin_lb = discrete_coulomb_unit_sum(inv_mat, occ_skin_lb)

        if Z <= 1 and (s_unit_sym != mpf(0) or s_unit_core_pauli != mpf(0) or s_unit_skin_lb != mpf(0)):
            z_le_1_zero_ok = False
        if name == "3He":
            he3_single_bond_diff = fabs(s_unit_core_pauli - mpf(1)) + fabs(s_unit_sym - mpf(1))
        if name == "4He":
            he4_single_bond_diff = fabs(s_unit_core_pauli - mpf(1)) + fabs(s_unit_sym - mpf(1))

        # Check FCC sixth-power polynomial identity `(4*pi)^2 * 2 * R_FCC^6 == 9 * ell_bond^6 * A^2`
        for linfo in bond_laws.values():
            ell_b = linfo["ell_bond_fm"]
            r_fcc_a = linfo["r0_fcc_fm"] * (mpf(A) ** (mpf(1) / mpf(3)))
            lhs6 = ((mpf(4) * pi) ** 2) * mpf(2) * (r_fcc_a ** 6)
            rhs6 = mpf(9) * (ell_b ** 6) * (mpf(A) ** 2)
            rel6 = fabs(lhs6 - rhs6) / rhs6
            if rel6 > max_sixth_power_diff:
                max_sixth_power_diff = rel6

        ec_legacy = legacy_continuum_coulomb_mev(ahc_2t, Z, A)
        coulomb_by_law: dict[str, dict[str, str]] = {}
        ec_sym_map: dict[str, mpf] = {}
        ec_core_pauli_map: dict[str, mpf] = {}
        for lkey, linfo in bond_laws.items():
            ell_b = linfo["ell_bond_fm"]
            ec_s = (ahc_2t / ell_b) * s_unit_sym
            ec_cp = (ahc_2t / ell_b) * s_unit_core_pauli
            ec_lb = (ahc_2t / ell_b) * s_unit_skin_lb
            ec_fcc = fcc_ball_continuum_coulomb_mev(ahc_2t, linfo["r0_fcc_fm"], Z, A)
            ec_sym_map[lkey] = ec_s
            ec_core_pauli_map[lkey] = ec_cp
            coulomb_by_law[lkey] = {
                "E_C_disc_sym_MeV": fmt(ec_s, DPS),
                "E_C_disc_core_pauli_MeV": fmt(ec_cp, DPS),
                "E_C_fcc_ball_MeV": fmt(ec_fcc, DPS),
                "thomson_conductor_skin_lower_bound_MeV": fmt(ec_lb, DPS),
                "delta_disc_sym_vs_legacy_sphere_MeV": fmt(ec_s - ec_legacy, 20),
                "delta_disc_core_pauli_vs_legacy_sphere_MeV": fmt(ec_cp - ec_legacy, 20),
            }

        # Coordinate-verified 3D Freudenthal-Kuhn tetrahedral ball + close-packed shell balls:
        f_3t = apollonian_3tree_f_vec(A)
        t_kuhn = build_explicit_3d_kuhn_ball_complex(A)
        t_kuhn_n1 = _lane_n1_kuhn_ball(A)
        f_kuhn_pcap = pauli_capped_kuhn_ball_f_vec(Z, N)
        f_ball = close_packed_shell_ball_f_vec(A)
        f_pcap = pauli_capped_shell_ball_f_vec(Z, N)

        all_kuhn_positive_vol_ok = (
            all_kuhn_positive_vol_ok
            and bool(t_kuhn["all_cells_strict_positive_volume"])
            and bool(t_kuhn["all_cells_canonical_kuhn"])
            and bool(t_kuhn["unique_kuhn_cells_eq_f3"])
            and (int(t_kuhn["min_abs_det"]) == 1)
            and (int(t_kuhn["max_abs_det"]) == 1)
        )
        all_kuhn_manifold_incidence_ok = all_kuhn_manifold_incidence_ok and bool(t_kuhn["all_interior_triangles_shared_by_two"])
        all_kuhn_compact_3ball_ok = all_kuhn_compact_3ball_ok and verify_compact_3ball_triangulation(t_kuhn) and verify_compact_3ball_triangulation(f_ball)
        if A >= 56:
            all_kuhn_surface_scaling_ok = all_kuhn_surface_scaling_ok and (int(t_kuhn["f0_int"]) > 0) and (int(t_kuhn["f0_bdry"]) < A)
        if name == "208Pb":
            all_kuhn_surface_scaling_ok = all_kuhn_surface_scaling_ok and (int(t_kuhn["f0_bdry"]) == 188) and (int(t_kuhn["f2_bdry"]) == 372)
        if name == "238U":
            all_kuhn_surface_scaling_ok = all_kuhn_surface_scaling_ok and (int(t_kuhn["f0_bdry"]) == 214) and (int(t_kuhn["f2_bdry"]) == 424)
        for k_chk in ("f0", "f1", "f2", "f3", "f0_bdry", "f1_bdry", "f2_bdry", "min_abs_det", "max_abs_det"):
            if int(t_kuhn[k_chk]) != int(t_kuhn_n1[k_chk]):
                all_kuhn_lane_n1_match_ok = False

        b_3t_gg_bare = (
            mpf(f_3t["f1"]) * sub_2t["b2_log_gg_bare_MeV"]
            + mpf(f_3t["f2"]) * sub_2t["w3_bare_MeV"]
            + mpf(f_3t["f3"]) * sub_2t["w4_bare_MeV"]
        )
        b_kuhn_logd_bare = (
            mpf(int(t_kuhn["f1"])) * sub_2t["b2_log_D_bare_MeV"]
            + mpf(int(t_kuhn["f2"])) * sub_2t["w3_bare_MeV"]
            + mpf(int(t_kuhn["f3"])) * sub_2t["w4_bare_MeV"]
        )
        b_kuhn_logd_inf = (
            mpf(int(t_kuhn["f1"])) * sub_2t["b2_log_D_inf_MeV"]
            + mpf(int(t_kuhn["f2"])) * sub_2t["w3_inf_MeV"]
            + mpf(int(t_kuhn["f3"])) * sub_2t["w4_inf_MeV"]
        )
        b_kuhn_pcap_logd_bare = (
            mpf(f_kuhn_pcap["f1"]) * sub_2t["b2_log_D_bare_MeV"]
            + mpf(f_kuhn_pcap["f2"]) * sub_2t["w3_bare_MeV"]
            + mpf(f_kuhn_pcap["f3"]) * sub_2t["w4_bare_MeV"]
        )
        b_ball_logd_bare = (
            mpf(f_ball["f1"]) * sub_2t["b2_log_D_bare_MeV"]
            + mpf(f_ball["f2"]) * sub_2t["w3_bare_MeV"]
            + mpf(f_ball["f3"]) * sub_2t["w4_bare_MeV"]
        )
        b_pcap_logd_bare = (
            mpf(f_pcap["f1"]) * sub_2t["b2_log_D_bare_MeV"]
            + mpf(f_pcap["f2"]) * sub_2t["w3_bare_MeV"]
            + mpf(f_pcap["f3"]) * sub_2t["w4_bare_MeV"]
        )

        # N2 + N3 Spin-Orbit Symmetry, Centered Weyl Shell Stabilization, HO Kinetic Promotion, & TL Pairing
        so_2t = spin_orbit_symmetry_and_shell_mev(sub_2t, levels_2t, Z, N)
        so_pr = spin_orbit_symmetry_and_shell_mev(sub_proton, levels_proton, Z, N)
        so_mu = spin_orbit_symmetry_and_shell_mev(sub_muon, levels_muon, Z, N)

        if name in ("4He", "16O", "40Ca", "208Pb"):
            doubly_magic_shell_signs_ok = doubly_magic_shell_signs_ok and (so_2t["delta_shell_weyl_so_dimless"] > mpf(0))
        if name == "24Mg":
            doubly_magic_shell_signs_ok = doubly_magic_shell_signs_ok and (so_2t["delta_shell_weyl_so_dimless"] < mpf(0))

        # Symmetric-core HO kinetic promotion (`2 * ho_excitation_quanta_3d(min(Z,N)) * hw_hecke_bare`)
        # for Pauli-capped complexes where `|N - Z|` asymmetry is already topologically penalized:
        m_core_min = Z if Z <= N else N
        e_kin_ho_sym_core_bare = (
            mpf(2 * ho_excitation_quanta_3d(m_core_min))
            * sub_2t["E0_bare_MeV"]
            / (mpf(A) ** (mpf(1) / mpf(3)))
        )

        # Legacy O(A^2) Borromean all-pairs baseline
        n_pp = max(Z - 1, 0)
        n_pn = 1 if (Z > 0 and N > 0) else 0
        n_nn = max(N - 1, 0)
        tr_f = sub_2t["tau_Bor"] ** A
        dtr = tr_f * (mpf(1) - (sub_2t["z_D"] ** (n_pp + n_pn)) * (sub_2t["z_nn_chiral"] ** n_nn))
        pair_bor = (
            mpf(_int_comb(Z, 2) + Z * N) * (sub_2t["g_tau2"] - sub_2t["g_tau2_zD"])
            + mpf(_int_comb(N, 2)) * (sub_2t["g_tau2"] - sub_2t["g_tau2_znn"])
        )
        b_legacy_bor_allpairs = sub_2t["E0_bare_MeV"] * (dtr + (sub_2t["z_D"] ** 2) * pair_bor)

        # Complete Joint Wave-3 Nuclear Synthesis Branches across all 4 Compton bond laws (zero fitting, zero double-counting)
        joint_branches: dict[str, dict[str, str]] = {
            "legacy_allpairs_borromean_O_A2": _err_dict(b_legacy_bor_allpairs, b_ame, sig_ame),
            "wave2_apollonian_3tree_gg_legacySphere": _err_dict(b_3t_gg_bare - ec_legacy, b_ame, sig_ame),
            "wave3_kuhn_3d_ball_logD_bare_discSO_legacySphere": _err_dict(
                b_kuhn_logd_bare
                - so_2t["E_sym_disc_compton_MeV"]
                + so_2t["delta_E_shell_hecke_bare_MeV"]
                + so_2t["delta_E_pair_TL_bare_MeV"]
                - ec_legacy,
                b_ame,
                sig_ame,
            ),
        }
        for lkey in bond_laws:
            for c_tag, ec_use in (("discSym", ec_sym_map[lkey]), ("discCorePauli", ec_core_pauli_map[lkey])):
                # 1. Coordinate-verified 3D Kuhn ball: static vs SO-symmetry/shell/pairing vs HO-kinetic vs Pauli-capped (zero double E_sym)
                b_kuhn_static = b_kuhn_logd_bare - ec_use
                b_kuhn_so_bare = (
                    b_kuhn_logd_bare
                    - so_2t["E_sym_disc_compton_MeV"]
                    + so_2t["delta_E_shell_hecke_bare_MeV"]
                    + so_2t["delta_E_pair_TL_bare_MeV"]
                    - ec_use
                )
                b_kuhn_so_inf = (
                    b_kuhn_logd_inf
                    - so_2t["E_sym_disc_compton_MeV"]
                    + so_2t["delta_E_shell_hecke_inf_MeV"]
                    + so_2t["delta_E_pair_TL_inf_MeV"]
                    - ec_use
                )
                b_kuhn_hokin = (
                    b_kuhn_logd_bare
                    - so_2t["E_kin_ho_hecke_bare_MeV"]
                    + so_2t["delta_E_shell_hecke_bare_MeV"]
                    + so_2t["delta_E_pair_TL_bare_MeV"]
                    - ec_use
                )
                # Pauli-capped Kuhn ball: NO `- E_sym_disc` (excess |N-Z| already penalized by +2D edges, +D triangles, +0 tetrahedra)
                b_kuhn_pcap = (
                    b_kuhn_pcap_logd_bare
                    + so_2t["delta_E_shell_hecke_bare_MeV"]
                    + so_2t["delta_E_pair_TL_bare_MeV"]
                    - ec_use
                )

                # 2. Honest 3D close-packed shell ball: BOTH static AND with repulsive 3D Pauli/Fermi HO kinetic promotion
                b_shell_static = b_ball_logd_bare - ec_use
                b_shell_hokin = (
                    b_ball_logd_bare
                    - so_2t["E_kin_ho_hecke_bare_MeV"]
                    - so_2t["E_sym_disc_compton_MeV"]
                    + so_2t["delta_E_shell_hecke_bare_MeV"]
                    + so_2t["delta_E_pair_TL_bare_MeV"]
                    - ec_use
                )
                b_shell_hokin_pure = (
                    b_ball_logd_bare
                    - so_2t["E_kin_ho_hecke_bare_MeV"]
                    + so_2t["delta_E_shell_hecke_bare_MeV"]
                    + so_2t["delta_E_pair_TL_bare_MeV"]
                    - ec_use
                )
                # 3. Pauli-capped 3D close-packed shell ball: NO `- E_sym_disc` (zero double-counting!)
                b_pcap_no_double_sym = (
                    b_pcap_logd_bare
                    + so_2t["delta_E_shell_hecke_bare_MeV"]
                    + so_2t["delta_E_pair_TL_bare_MeV"]
                    - ec_use
                )
                b_pcap_sym_core_hokin = (
                    b_pcap_logd_bare
                    - e_kin_ho_sym_core_bare
                    + so_2t["delta_E_shell_hecke_bare_MeV"]
                    + so_2t["delta_E_pair_TL_bare_MeV"]
                    - ec_use
                )
                # 4. Achiral gg 3-tree baseline + discrete SO symmetry/shell/pairing - discrete Coulomb
                b_w3_3tree_gg = (
                    b_3t_gg_bare
                    - so_2t["E_sym_disc_compton_MeV"]
                    + so_2t["delta_E_shell_hecke_bare_MeV"]
                    + so_2t["delta_E_pair_TL_bare_MeV"]
                    - ec_use
                )

                joint_branches[f"wave3_kuhn_3d_ball_logD_bare_static_{c_tag}_{lkey}"] = _err_dict(b_kuhn_static, b_ame, sig_ame)
                joint_branches[f"wave3_kuhn_3d_ball_logD_bare_discSO_{c_tag}_{lkey}"] = _err_dict(b_kuhn_so_bare, b_ame, sig_ame)
                joint_branches[f"wave3_kuhn_3d_ball_logD_tower_discSO_{c_tag}_{lkey}"] = _err_dict(b_kuhn_so_inf, b_ame, sig_ame)
                joint_branches[f"wave3_kuhn_3d_ball_logD_bare_hoKinHecke_{c_tag}_{lkey}"] = _err_dict(b_kuhn_hokin, b_ame, sig_ame)
                joint_branches[f"wave3_pauli_capped_kuhn_ball_logD_bare_noDoubleSym_{c_tag}_{lkey}"] = _err_dict(b_kuhn_pcap, b_ame, sig_ame)
                joint_branches[f"wave3_close_packed_shell_ball_logD_bare_static_{c_tag}_{lkey}"] = _err_dict(b_shell_static, b_ame, sig_ame)
                joint_branches[f"wave3_close_packed_shell_ball_logD_bare_hoKinHecke_pure_{c_tag}_{lkey}"] = _err_dict(b_shell_hokin_pure, b_ame, sig_ame)
                joint_branches[f"wave3_close_packed_shell_ball_logD_bare_hoKinHecke_discSO_{c_tag}_{lkey}"] = _err_dict(b_shell_hokin, b_ame, sig_ame)
                joint_branches[f"wave3_pauli_capped_shell_ball_logD_bare_noDoubleSym_{c_tag}_{lkey}"] = _err_dict(b_pcap_no_double_sym, b_ame, sig_ame)
                joint_branches[f"wave3_pauli_capped_shell_ball_logD_bare_coreHoKin_{c_tag}_{lkey}"] = _err_dict(b_pcap_sym_core_hokin, b_ame, sig_ame)
                joint_branches[f"wave3_3tree_gg_bare_discSO_{c_tag}_{lkey}"] = _err_dict(b_w3_3tree_gg, b_ame, sig_ame)

        # Cross-anchor (`q_proton` vs `q_muon` vs `q_2t`) check on `wave3_kuhn_3d_ball_logD_bare_discSO_discSym_L2_three_halves_lambda_pi`:
        ell_32 = bond_laws["L2_three_halves_lambda_pi"]["ell_bond_fm"]
        b_w3_2t = mpf(str(joint_branches["wave3_kuhn_3d_ball_logD_bare_discSO_discSym_L2_three_halves_lambda_pi"]["B_pred_MeV"]))
        b_w3_pr = (
            mpf(int(t_kuhn["f1"])) * sub_proton["b2_log_D_bare_MeV"]
            + mpf(int(t_kuhn["f2"])) * sub_proton["w3_bare_MeV"]
            + mpf(int(t_kuhn["f3"])) * sub_proton["w4_bare_MeV"]
            - so_pr["E_sym_disc_compton_MeV"]
            + so_pr["delta_E_shell_hecke_bare_MeV"]
            + so_pr["delta_E_pair_TL_bare_MeV"]
            - (sub_proton["alpha_hbar_c_MeV_fm"] / ell_32) * s_unit_sym
        )
        b_w3_mu = (
            mpf(int(t_kuhn["f1"])) * sub_muon["b2_log_D_bare_MeV"]
            + mpf(int(t_kuhn["f2"])) * sub_muon["w3_bare_MeV"]
            + mpf(int(t_kuhn["f3"])) * sub_muon["w4_bare_MeV"]
            - so_mu["E_sym_disc_compton_MeV"]
            + so_mu["delta_E_shell_hecke_bare_MeV"]
            + so_mu["delta_E_pair_TL_bare_MeV"]
            - (sub_muon["alpha_hbar_c_MeV_fm"] / ell_32) * s_unit_sym
        )

        b_disp_sh_stat = mpf(str(joint_branches["wave3_close_packed_shell_ball_logD_bare_static_discSym_L2_three_halves_lambda_pi"]["B_pred_MeV"]))
        b_disp_sh_ho = mpf(str(joint_branches["wave3_close_packed_shell_ball_logD_bare_hoKinHecke_discSO_discSym_L2_three_halves_lambda_pi"]["B_pred_MeV"]))
        b_disp_pcap_ho = mpf(str(joint_branches["wave3_pauli_capped_shell_ball_logD_bare_coreHoKin_discSym_L2_three_halves_lambda_pi"]["B_pred_MeV"]))
        ec_fcc_l2 = fcc_ball_continuum_coulomb_mev(ahc_2t, bond_laws["L2_three_halves_lambda_pi"]["r0_fcc_fm"], Z, A)

        print(
            f"{name:<6} {Z:>3} {N:>3} {A:>3} | "
            f"{mp.nstr(ec_sym_map['L2_three_halves_lambda_pi'], 6):>10} "
            f"{mp.nstr(ec_core_pauli_map['L2_three_halves_lambda_pi'], 6):>10} "
            f"{mp.nstr(ec_fcc_l2, 6):>10} | "
            f"{mp.nstr(b_ame, 6):>8} "
            f"{mp.nstr(b_w3_2t, 6):>10} "
            f"{mp.nstr(b_disp_sh_stat, 6):>10} "
            f"{mp.nstr(b_disp_sh_ho, 6):>11} "
            f"{mp.nstr(b_disp_pcap_ho, 6):>9}"
        )

        row_entry: dict[str, object] = {
            "nuclide": name,
            "Z": Z,
            "N": N,
            "A": A,
            "B_AME_MeV": fmt(b_ame, DPS),
            "sigma_AME_MeV": fmt(sig_ame, DPS),
            "unit_coulomb_pair_sum_sym": fmt(s_unit_sym, DPS),
            "unit_coulomb_pair_sum_core_pauli": fmt(s_unit_core_pauli, DPS),
            "thomson_conductor_skin_lower_bound_unit_sum": fmt(s_unit_skin_lb, DPS),
            "E_C_legacy_continuum_sphere_MeV": fmt(ec_legacy, DPS),
            "coulomb_by_bond_law_q2t": coulomb_by_law,
            "triangulations": {
                "explicit_3d_kuhn_ball": t_kuhn,
                "pauli_capped_3d_kuhn_ball": f_kuhn_pcap,
                "close_packed_3d_shell_ball": f_ball,
                "pauli_capped_3d_shell_ball": f_pcap,
            },
            "spin_orbit_and_pairing_terms_q2t": {
                **{k: fmt(v, DPS) for k, v in so_2t.items()},
                "E_kin_ho_sym_core_hecke_bare_MeV": fmt(e_kin_ho_sym_core_bare, DPS),
            },
            "cross_anchor_wave3_kuhn_logD_discSym_L2_MeV": {
                "q_2t_MeV": fmt(b_w3_2t, DPS),
                "q_proton_MeV": fmt(b_w3_pr, DPS),
                "q_muon_MeV": fmt(b_w3_mu, DPS),
                "proton_minus_muon_keV": fmt((b_w3_pr - b_w3_mu) * mpf(1000), 20),
                "q2t_minus_proton_keV": fmt((b_w3_2t - b_w3_pr) * mpf(1000), 20),
            },
            "joint_synthesis_branches": joint_branches,
        }
        if name == "12C":
            row_entry["carbon12_equilateral_3alpha_cluster_coulomb_MeV"] = c12_3alpha_ec_by_law
        benchmark_rows.append(row_entry)

    # 4. Evaluate all 7 Mirror Pairs (A = 3, 7, 11, 13, 15, 17, 41) & Verify Mirror Theorems
    max_mirror_potential_thm_diff = mpf(0)
    max_mirror_isometric_valence_thm_diff = mpf(0)
    max_joint_mirror_strong_cancel_diff = mpf(0)
    all_physical_mirror_shifts_positive = True
    mirror_rows: list[dict[str, object]] = []

    print("\n----------------------------------------------------------------------------------------------------------------------------------------")
    print("  Mirror-Nucleus Coulomb Displacement Benchmark (A = 3, 7, 11, 13, 15, 17, 41)")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(
        f"{'Pair':<11} {'A':>3} | {'dB_AME':>9} | {'dEC_oldSph':>10} {'dEC_sym(L2)':>12} "
        f"{'dEC_cPl(L2)':>12} {'dEC_val(L2)':>12} {'dEC_sym(rt3)':>12}"
    )
    print("-" * 102)

    for lo_nm, z_lo, n_lo, hi_nm, z_hi, n_hi in MIRROR_PAIRS:
        A = z_lo + n_lo
        b_lo = AME_EXACT[(z_lo, A)]["B_AME_MeV"]
        b_hi = AME_EXACT[(z_hi, A)]["B_AME_MeV"]
        db_ame = b_lo - b_hi

        coords = FCC_SITES_MASTER[:A]
        inv_mat, dist_hist = fcc_unit_inv_dist_matrix(coords)

        # (a) Core-consistent Pauli `(2p, 2n)` occupancy for low-Z (`Z_lo < N_lo`: excess neutron in outer skin)
        #     and high-Z (`Z_hi > N_hi`: excess valence proton in outer skin, identical `min(Z,N)` core protons!)
        occ_core_lo = core_consistent_pauli_proton_occupancy(A, z_lo)
        occ_core_hi = core_consistent_pauli_proton_occupancy(A, z_hi)
        s_core_lo = discrete_coulomb_unit_sum(inv_mat, occ_core_lo)
        s_core_hi = discrete_coulomb_unit_sum(inv_mat, occ_core_hi)
        ds_core_pauli = s_core_hi - s_core_lo

        # Verify Master Lean Theorem `discreteCoulomb_mirror_diff_vertexPotential` on `occ_core_hi` vs `mirrorOccupancy(occ_core_hi)`:
        # E_C(p) - E_C(p_bar) == (1/2) * sum_u (2*p_u - 1) * vertexPotential(u)
        occ_core_hi_bar = mirror_occupancy(occ_core_hi)
        ds_alg_mirror = s_core_hi - discrete_coulomb_unit_sum(inv_mat, occ_core_hi_bar)
        pot_rhs = mpf(0)
        for u in range(A):
            sigma_u = fsum(inv_mat[u])
            sign_u = mpf(1) if occ_core_hi[u] else -mpf(1)
            pot_rhs += sign_u * sigma_u
        pot_rhs = pot_rhs / mpf(2)
        thm_diff = fabs(ds_alg_mirror - pot_rhs)
        if thm_diff > max_mirror_potential_thm_diff:
            max_mirror_potential_thm_diff = thm_diff

        # (b) Verify Lean Theorem `discreteCoulomb_mirror_diff_isometric_valence` on inversion-symmetric
        # FCC complex centered at origin `(0,0,0)` (`vStar = (0,0,0)`, `pi(x,y,z) = (-x,-y,-z)`):
        inv_pairs: list[tuple[int, int, int]] = [(0, 0, 0)]
        seen_inv = {(0, 0, 0)}
        for cand in FCC_SITES_MASTER:
            if len(inv_pairs) >= A:
                break
            neg_c = (-cand[0], -cand[1], -cand[2])
            if cand not in seen_inv and neg_c not in seen_inv:
                inv_pairs.append(cand)
                inv_pairs.append(neg_c)
                seen_inv.add(cand)
                seen_inv.add(neg_c)
        inv_mat_sym, _ = fcc_unit_inv_dist_matrix(inv_pairs[:A])
        occ_sym_hi = [True] + [((idx % 2) == 0) for idx in range(A - 1)]
        occ_sym_lo = mirror_occupancy(occ_sym_hi)
        ds_sym_pair = discrete_coulomb_unit_sum(inv_mat_sym, occ_sym_hi) - discrete_coulomb_unit_sum(
            inv_mat_sym, occ_sym_lo
        )
        valence_pot_rhs = fsum(
            inv_mat_sym[0][u] for u in range(A) if occ_sym_hi[u]
        )
        val_diff = fabs(ds_sym_pair - valence_pot_rhs)
        if val_diff > max_mirror_isometric_valence_thm_diff:
            max_mirror_isometric_valence_thm_diff = val_diff

        # (c) Isospin-symmetrized all-pairs unit difference:
        total_all_pairs_unit = fsum(
            mpf(cnt) * (INV_SQRT_CACHE[k_sq] if k_sq < len(INV_SQRT_CACHE) else (mpf(1) / sqrt(mpf(k_sq))))
            for k_sq, cnt in dist_hist.items()
        )
        ds_isospin_avg = (
            mpf(z_hi * (z_hi - 1) - z_lo * (z_lo - 1)) / mpf(A * (A - 1))
        ) * total_all_pairs_unit

        if not (ds_isospin_avg > mpf(0) and ds_core_pauli > mpf(0) and ds_sym_pair > mpf(0)):
            all_physical_mirror_shifts_positive = False

        # Verify `joint_simplicial_net_mirror_split` cancellation of charge-symmetric strong core:
        fb_m = close_packed_shell_ball_f_vec(A)
        b_strong_m = (
            mpf(fb_m["f1"]) * sub_2t["b2_log_D_bare_MeV"]
            + mpf(fb_m["f2"]) * sub_2t["w3_bare_MeV"]
            + mpf(fb_m["f3"]) * sub_2t["w4_bare_MeV"]
        )
        ell_32 = bond_laws["L2_three_halves_lambda_pi"]["ell_bond_fm"]
        ec_hi_32 = (ahc_2t / ell_32) * s_core_hi
        ec_lo_32 = (ahc_2t / ell_32) * s_core_lo
        joint_cancel_diff = fabs(
            ((b_strong_m - ec_lo_32) - (b_strong_m - ec_hi_32)) - (ec_hi_32 - ec_lo_32)
        )
        if joint_cancel_diff > max_joint_mirror_strong_cancel_diff:
            max_joint_mirror_strong_cancel_diff = joint_cancel_diff

        dec_legacy = legacy_continuum_coulomb_mev(ahc_2t, z_hi, A) - legacy_continuum_coulomb_mev(
            ahc_2t, z_lo, A
        )
        by_law_mirror: dict[str, dict[str, str]] = {}
        dec_sym_print: dict[str, mpf] = {}
        dec_core_print: dict[str, mpf] = {}
        dec_val_print: dict[str, mpf] = {}
        for lkey, linfo in bond_laws.items():
            ell_b = linfo["ell_bond_fm"]
            dec_avg = (ahc_2t / ell_b) * ds_isospin_avg
            dec_cp = (ahc_2t / ell_b) * ds_core_pauli
            dec_val = (ahc_2t / ell_b) * ds_sym_pair
            dec_sym_print[lkey] = dec_avg
            dec_core_print[lkey] = dec_cp
            dec_val_print[lkey] = dec_val
            by_law_mirror[lkey] = {
                "dE_C_disc_sym_MeV": fmt(dec_avg, DPS),
                "dE_C_disc_sym_err_vs_AME_pct": fmt((dec_avg - db_ame) / db_ame * mpf(100), 16),
                "dE_C_disc_core_pauli_MeV": fmt(dec_cp, DPS),
                "dE_C_disc_core_pauli_err_vs_AME_pct": fmt((dec_cp - db_ame) / db_ame * mpf(100), 16),
                "dE_C_isometric_valence_MeV": fmt(dec_val, DPS),
                "dE_C_isometric_valence_err_vs_AME_pct": fmt((dec_val - db_ame) / db_ame * mpf(100), 16),
            }

        print(
            f"{lo_nm + '/' + hi_nm:<11} {A:>3} | {mp.nstr(db_ame, 6):>9} | "
            f"{mp.nstr(dec_legacy, 6):>10} "
            f"{mp.nstr(dec_sym_print['L2_three_halves_lambda_pi'], 6):>12} "
            f"{mp.nstr(dec_core_print['L2_three_halves_lambda_pi'], 6):>12} "
            f"{mp.nstr(dec_val_print['L2_three_halves_lambda_pi'], 6):>12} "
            f"{mp.nstr(dec_sym_print['L3_sqrt3_lambda_pi'], 6):>12}"
        )

        mirror_rows.append({
            "pair": f"{lo_nm}/{hi_nm}",
            "lo_nuclide": lo_nm,
            "Z_lo": z_lo,
            "N_lo": n_lo,
            "hi_nuclide": hi_nm,
            "Z_hi": z_hi,
            "N_hi": n_hi,
            "A": A,
            "dB_AME_MeV": fmt(db_ame, DPS),
            "dE_C_legacy_continuum_sphere_MeV": fmt(dec_legacy, DPS),
            "dE_C_legacy_err_vs_AME_pct": fmt((dec_legacy - db_ame) / db_ame * mpf(100), 16),
            "by_bond_law_q2t": by_law_mirror,
        })

    # 5. Audit retiring `alpha_cluster_recursion`
    alpha_retire_audit = audit_alpha_cluster_recursion_retirement(sub_2t, bond_laws, levels_2t)

    # 6. Build & Stamp Witness JSON (`q0Anchor: "comparison"`, zero raw floats)
    wb = WitnessBuilder("simplicial-coulomb-radius-and-joint-nuclear", engine="mpmath")
    wb.set_description(
        "80-dps parameter-free verification of SimplicialCoulombGraphMetricDerivation.lean "
        "(qou-usft, qou-mumr) and Joint Wave-3 Nuclear Synthesis (Lanes N1-N4): coordinate-verified "
        "3D Freudenthal-Kuhn tetrahedral balls (|det| >= 1 on 100% of 3-simplices, O(A^{2/3}) surface), "
        "static vs parameter-free 3D Pauli/Fermi harmonic-oscillator kinetic promotion, core-consistent "
        "and isospin-symmetrized discrete 3D proton-pair Coulomb sums across 13 benchmark nuclei "
        "(2H..238U) and 7 mirror pairs (A=3..41), centered Weyl shell stabilization, Temperley-Lieb "
        "pairing gap (tlPairingGap = E0/(2*[3]_q)), 3D FCC Voronoi packing radius transport across all "
        "4 Compton bond-length laws with Form-B Bring-Schwinger alpha_EM^{corr}(q_2t), cross-anchor "
        "comparison (q_proton, q_muon, q_2t), and alpha_cluster_recursion retirement audit."
    )
    wb.add_parameter("dps", DPS)
    wb.add_parameter("q_two_term_borromean_80dps", fmt(q_2t, DPS))
    wb.add_parameter("hbar_c_MeV_fm", fmt(HBAR_C_MEV_FM, 20))
    wb.add_parameter("lambda_bar_pi_fm", fmt(LAMBDA_BAR_PI_FM, DPS))

    wb.add_data(
        "substrate_and_photon_pins",
        {
            "q_two_term_borromean": {k: fmt(v, DPS) for k, v in sub_2t.items()},
            "q_proton": {k: fmt(v, DPS) for k, v in sub_proton.items()},
            "q_muon": {k: fmt(v, DPS) for k, v in sub_muon.items()},
            "form_b_module_crosscheck_diff": fmt(ainv_mod_diff, 20),
        },
    )
    wb.add_data(
        "fcc_packing_and_compton_bond_laws",
        {
            "c_fcc_dimensionless": fmt(c_fcc, DPS),
            "c_fcc_strictly_in_0_55_to_0_56": c_fcc_in_bounds,
            "eta_fcc_packing_fraction": fmt(eta_fcc, DPS),
            "eta_fcc_sq_minus_pi2_over_18_diff": fmt(eta_fcc_sq_diff, 20),
            "max_sixth_power_identity_rel_diff": fmt(max_sixth_power_diff, 20),
            "continuum_sphere_distortion_cube_A3_diff": fmt(distort_cube_a3_diff, 20),
            "continuum_sphere_distortion_cube_A4_diff": fmt(distort_cube_a4_diff, 20),
            "bond_length_laws": {
                k: {ik: fmt(iv, DPS) for ik, iv in v.items()} for k, v in bond_laws.items()
            },
        },
    )
    wb.add_data(
        "carbon12_equilateral_3alpha_cluster",
        {
            "intra_alpha_edges_all_unit_length": c12_3alpha["intra_alpha_edges_all_unit_length"],
            "proton_count_Z": c12_3alpha["proton_count_Z"],
            "intra_alpha_proton_pairs": c12_3alpha["intra_alpha_proton_pairs"],
            "inter_alpha_proton_pairs": c12_3alpha["inter_alpha_proton_pairs"],
            "total_proton_pairs": c12_3alpha["total_proton_pairs"],
            "unit_sum_intra": fmt(c12_3alpha["unit_sum_intra"], DPS),
            "unit_sum_inter": fmt(c12_3alpha["unit_sum_inter"], DPS),
            "unit_sum_total": fmt(c12_3alpha["unit_sum_total"], DPS),
            "effective_inter_alpha_dist_over_ell_bond": fmt(
                c12_3alpha["effective_inter_alpha_dist_over_ell_bond"], DPS
            ),
            "lean_two_scale_identity_diff": fmt(c12_3alpha["lean_two_scale_identity_diff"], 20),
            "coulomb_MeV_by_bond_law_q2t": c12_3alpha_ec_by_law,
            "distance_shell_histogram": c12_3alpha["distance_shell_histogram"],
        },
    )
    wb.add_data("benchmark_nuclei_2H_to_238U", benchmark_rows)
    wb.add_data("mirror_displacement_pairs_A3_to_A41", mirror_rows)
    wb.add_data("alpha_cluster_recursion_retirement_audit", alpha_retire_audit)

    tol_strict = "1e-70"

    wb.add_assertion(
        name="zero_self_interaction_for_Z_le_1_deuteron_and_triton",
        computed="1" if z_le_1_zero_ok else "0",
        expected="1",
        tolerance="0",
        source="SimplicialCoulombGraphMetricDerivation.discreteCoulomb_eq_zero_of_protonCount_le_one",
    )
    wb.add_assertion(
        name="regular_simplex_single_proton_bond_3He_and_pauli_K4_4He",
        computed=fmt(he3_single_bond_diff + he4_single_bond_diff, 20),
        expected="0",
        tolerance=tol_strict,
        source="SimplicialCoulombGraphMetricDerivation.pauli_k4_forced_single_proton_bond",
    )
    wb.add_assertion(
        name="continuum_sphere_distortion_cubes_72_over_125_and_54_over_125",
        computed=fmt(distort_cube_a3_diff + distort_cube_a4_diff, 20),
        expected="0",
        tolerance=tol_strict,
        source="SimplicialCoulombGraphMetricDerivation.continuum_sphere_distortion_A3_and_A4",
    )
    kuhn_all_ok = (
        all_kuhn_positive_vol_ok
        and all_kuhn_manifold_incidence_ok
        and all_kuhn_compact_3ball_ok
        and all_kuhn_surface_scaling_ok
        and all_kuhn_lane_n1_match_ok
        and bool(alpha_retire_audit["a200_kuhn_ball_all_cells_strict_positive_volume"])
    )
    wb.add_assertion(
        name="explicit_3d_kuhn_ball_strict_positive_volume_manifold_and_surface_scaling",
        computed="1" if kuhn_all_ok else "0",
        expected="1",
        tolerance="0",
        source="BallManifoldTriangulationAndSurfaceScaling.Compact3BallTriangulation + 3D det != 0 on 100% of 3-simplices",
    )
    wb.add_assertion(
        name="mirror_vertex_potential_and_isometric_valence_theorems_exact_A3_to_A41",
        computed=fmt(
            max_mirror_potential_thm_diff
            + max_mirror_isometric_valence_thm_diff
            + max_joint_mirror_strong_cancel_diff,
            20,
        ),
        expected="0",
        tolerance=tol_strict,
        source="SimplicialCoulombGraphMetricDerivation.discreteCoulomb_mirror_diff_vertexPotential",
    )
    wb.add_assertion(
        name="physical_mirror_coulomb_shifts_strictly_positive_all_pairs_A3_to_A41",
        computed="1" if all_physical_mirror_shifts_positive else "0",
        expected="1",
        tolerance="0",
        source="Core-consistent Pauli (2p,2n), isospin-symmetrized, and isometric-valence discrete mirror shifts > 0",
    )
    wb.add_assertion(
        name="centered_weyl_shell_stabilization_positive_at_doubly_magic_closures",
        computed="1" if doubly_magic_shell_signs_ok else "0",
        expected="1",
        tolerance="0",
        source="SpinOrbitShellClosureAndSymmetryEnergy centered Weyl vs Mayer-Jensen spin-orbit fill (4He, 16O, 40Ca, 208Pb > 0; 24Mg < 0)",
    )
    wb.add_assertion(
        name="temperley_lieb_pairing_gap_matches_lean_tlPairingGap_identity",
        computed=fmt(tl_pairing_id_diff, 20),
        expected="0",
        tolerance=tol_strict,
        source="SeniorityPairingAndHoyleTriadThreshold.tlPairingGap: (1/2)*w3_GPMT*[2]_q == E0/(2*[3]_q)",
    )
    wb.add_assertion(
        name="carbon12_equilateral_3alpha_pair_split_3_plus_12_eq_15_and_eval",
        computed=(
            f"{c12_3alpha['intra_alpha_proton_pairs']}+"
            f"{c12_3alpha['inter_alpha_proton_pairs']}="
            f"{c12_3alpha['total_proton_pairs']};"
            f"unit_intra={int(c12_3alpha['intra_alpha_edges_all_unit_length'])};"
            f"lean_ok={int(c12_3alpha['lean_two_scale_identity_diff'] < mpf('1e-70'))}"
        ),
        expected="3+12=15;unit_intra=1;lean_ok=1",
        tolerance="0",
        source="SimplicialCoulombGraphMetricDerivation.carbon12_equilateral_three_alpha_coulomb",
    )
    wb.add_assertion(
        name="fcc_packing_radius_sixth_power_polynomial_identity_all_benchmarks",
        computed=fmt(max_sixth_power_diff, 20),
        expected="0",
        tolerance="1e-68",
        source="SimplicialCoulombGraphMetricDerivation.fcc_packing_radius_sixth_power_identity",
    )
    wb.add_assertion(
        name="fcc_packing_constant_enclosure_0_55_to_0_56_and_kepler_fraction",
        computed="1" if (c_fcc_in_bounds and eta_fcc_sq_diff < mpf("1e-70")) else "0",
        expected="1",
        tolerance="0",
        source="SimplicialCoulombGraphMetricDerivation.fccPackingConst_bounds",
    )
    wb.add_assertion(
        name="form_b_bring_schwinger_photon_agrees_with_canonical_coulomb_module",
        computed=fmt(ainv_mod_diff, 20),
        expected="0",
        tolerance="1e-48",
        source="coulomb_energy.alpha_em_inv_bring_schwinger",
    )
    wb.add_assertion(
        name="retiring_alpha_cluster_recursion_leaves_zero_live_facade_regressions",
        computed="1" if alpha_retire_audit["zero_live_facade_imports_in_qou_mass_and_canonical_mass"] else "0",
        expected="1",
        tolerance="0",
        source="alpha_cluster_recursion retirement audit across 4He..40Ca and A=200",
    )

    out_path = wb.save(
        q0_comparison(
            muon=q_muon,
            proton=q_proton,
            reason=(
                "Evaluates discrete 3D simplicial proton-pair Coulomb repulsion, Form-B "
                "Bring-Schwinger alpha_EM^{corr}, and the Joint Wave-3 Nuclear Synthesis "
                "benchmark across both the proton and muon q0 pins alongside the two-term "
                "Borromean self-energy pin q_2t, reporting each pin under its own key."
            ),
        )
    )
    print("\n  Saved 80-dps witness -> " + str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
