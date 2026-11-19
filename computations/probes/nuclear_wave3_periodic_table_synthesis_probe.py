#!/usr/bin/env python3
"""nuclear_wave3_periodic_table_synthesis_probe.py — 80-dps Wave-3 Full Periodic
Table Nuclear Binding Synthesis Probe (3,558 Nuclides, Zero Fitting, Zero Float64).

Companion synthesis probe unifying the Wave-3 nuclear formalizations in
`folio/quantum-observable-universe/lean/QOU/Nuclear/`:
  * `BallManifoldTriangulationAndSurfaceScaling.lean`
    (`namespace QOU.Nuclear.BallManifoldTriangulationAndSurfaceScaling`)
  * `H4FullTwistAlphaCellAndGroebnerBridge.lean`
    (`namespace QOU.Nuclear.H4FullTwistAlphaCellAndGroebnerBridge`)
  * `SpinOrbitShellClosureAndSymmetryEnergy.lean`
    (`namespace QOU.Nuclear.SpinOrbitShellClosureAndSymmetryEnergy`)
  * `SeniorityPairingAndHoyleTriadThreshold.lean`
    (`namespace QOU.Nuclear.SeniorityPairingAndHoyleTriadThreshold`)
  * `SimplicialCoulombGraphMetricDerivation.lean`
    (`namespace QOU.Nuclear.SimplicialCoulombGraphMetricDerivation`)

PURPOSE & STRICT ANTI-FITTING DISCIPLINE
----------------------------------------
Evaluates at 80 decimal places (with 95-dps internal working precision, zero
float64 intermediates, zero `math` module imports, zero empirical liquid-drop
coefficients, zero tuned multipliers) the parameter-free Wave-3 3D simplicial
nuclear binding Hamiltonian across all 3,558 AME2020 nuclides (`Z = 0..118`,
`A = 1..295`, 3,556 nuclides with `A >= 2`) loaded directly from the vendored
AME2020 table (`computations/data/ame2020.json` parsed with `parse_float=str`):

  `B_W3(Z, N) = B_simp^(3D)(A) - E_Pauli+SO(Z, N) + Delta_pair(Z, N) - E_C^(FCC)(Z, A)`

where every ingredient is derived purely from `(q_0, m_e)`:

1. **3D Compact-Ball Simplicial Manifold & FCC Lattice Complexes (`A = 1..295`)**:
   - **Wave-2 Baseline (`apollonian_3tree`)**:
     `(f_0, f_1, f_2, f_3) = (A, 3A - 6, 3A - 8, A - 3)` (`A >= 3`), all vertices
     on the boundary (`f_{0,bdry} = A`, `f_{0,int} = 0`, interior edge-cycle excess
     `c = f_3 - (A - 3) = 0`), underbinding heavy nuclei (`208Pb`, `238U`) by `-41%`
     on Convention-D `b2_log_D`.
   - **3D FCC Nearest-Neighbor Clique Ball (`fcc_3d_clique_ball`)**:
     Places `A` nucleons at discrete 3D face-centered cubic (FCC) lattice sites
     `(x, y, z) in Z^3` with `(x + y + z) % 2 == 0` ordered by squared Euclidean
     distance from the origin tetrahedral centroid `(1/2, 1/2, 1/2)` and counts all
     nearest-neighbor edges (`|u - v|^2 = 2`), triangles (`K_3`), and regular
     tetrahedra (`K_4`).
   - **Coordinate-Verified 3D Euclidean Freudenthal-Kuhn Lattice Ball (`kuhn_3d_lattice_ball`)**:
     Single-pass incremental 3D tetrahedral ball complex in `Z^3` starting from the
     unit-volume Kuhn simplex `{(0,0,0), (1,0,0), (1,1,0), (1,1,1)}` (`|det| = 1`,
     Euclidean volume `1/6`), attaching each new lattice vertex across strictly
     visible outward-oriented canonical Kuhn boundary triangles. Every complex for
     `A = 4..295` is an exact Dehn-Sommerville compact 3-ball manifold triangulation
     (`f_0 - f_1 + f_2 - f_3 = 1`, `f_{0,bdry} - f_{1,bdry} + f_{2,bdry} = 2`,
     `3 f_{2,bdry} = 2 f_{1,bdry}`, `4 f_3 = 2 f_2 - f_{2,bdry}`) with `O(A^{2/3})`
     surface scaling and buried interior vertices (`f_{0,int} = 20` at `208Pb`, `24` at `238U`).
   - **Close-Packed 3D Mackay Shell-Interpolated Simplicial Ball (`close_packed_3d_shell_ball`)**:
     Exact Mackay close-packed `k`-shell magic clusters (`A(k) = (10k^3 + 15k^2 + 11k + 3)/3`,
     `f_{0,bdry}(k) = 10k^2 + 2`, `f_3(k) = 20k^3`) with Dehn-Sommerville-exact integer
     interpolation between closed shells for every `A = 4..295`.

2. **2-Body (`b2_log_D`, `b2_Bor_D`, `b2_log_gg`) & 3-/4-Body (`H_3`, `H_4`) GPMT Cumulants**:
   - Evaluates parameter-free Convention-D logarithmic (`b2_log_D = E_0 * ln(1 / z_D)`
     where `z_D = q^3 / (q^2 + 1)`), Convention-D Borromean (`b2_Bor_D = E_0 * (tau_Bor^2 * (1 - z_D)
     + z_D^2 * (g(tau_Bor^2) - g(tau_Bor^2 * z_D)))` where `g(x) = -Li_2(-x; q, q^{-1})`),
     and Wave-2 conjectured (`b2_log_gg = E_0 * ln(1 / z_gg)` where `z_gg = z_D - h / 2`)
     2-body bonds,
   - `H_3` 3-body face weight `w_3 = +E_0 * mu3_gpmt = +E_0 / ([2]_q [3]_q) > 0`
     (`d_mod((1,1,1)) = -q^3 / ((q^2 + 1)(q^4 + q^2 + 1)) = -mu3_gpmt`),
   - Both the `H_3` tetrahedral exclusion weight `w_4^(H3) = -2 * w_3 < 0` and
     the exact 4-strand `H_4` GPMT modified-dimension cumulant
     `w_4^(H4) = E_0 * (-3 * d_mod_211 + d_mod_1111 - 4 * mu3_gpmt) < 0`.

3. **3D Pauli/Fermi Harmonic-Oscillator Promotion, Mayer-Jensen Spin-Orbit `(2j+1)`, & Symmetry Energy**:
   - Evaluates clean, non-double-counted Pauli/Fermi promotion branches:
     (a) `PauliCore`: Pauli-capped `(Z, N)` core (`A_core = 2 * min(Z, N)` in the 3D
         Kuhn ball or 3D close-packed shell ball plus `D = |N - Z|` maximal Pauli-legal
         degree-2 surface triangles `+2D` edges, `+D` triangles, `+0` tetrahedra),
     (b) `HO_Pure`: discrete 3D isotropic harmonic-oscillator shell promotion
         `E_kin_ho_pure(Z, N) = (N_osc_pure(Z) + N_osc_pure(N)) * E_0 * A^{-1/3}`
         (without any extra `- E_sym` subtraction, since separate `(Z, N)` Fermi spheres
         already include the Pauli isospin-asymmetry promotion),
     (c) `SymHO_FermiSym`: symmetric `Z = N = A/2` 3D harmonic-oscillator shell promotion
         `E_kin_ho_sym(A) = N_osc_sym(A) * E_0 * A^{-1/3}` combined with the parameter-free
         QOU Compton Fermi quadratic symmetry energy
         `E_sym(Z, N) = a_sym(q) * (N - Z)^2 / A` (`a_sym(q) = (m_e / (q - 1)^2) * z_D`),
   - Mayer-Jensen spin-orbit split single-particle filling across spectroscopic
     `(n_r, l, 2j)` subshells (`210` states covering all `Z <= 118, N <= 177`, reproducing
     exact magic closures `2, 8, 20, 28, 50, 82, 126, 184`) with parameter-free Reeb
     coupling `kappa_SO^(Reeb) = h * z_D / 2` and discrete `(q - 1)^2` coupling
     `kappa_SO^((q-1)^2) = (q - 1)^2`.

4. **Temperley-Lieb Seniority Pairing (`tlPairingGap`)**:
   - Seniority `v_p = Z % 2`, `v_n = N % 2` (`v = v_p + v_n in {0, 1, 2}`),
   - Primary Lean-faithful branches use the proved Temperley-Lieb singlet pairing gap
     `Delta_TL(q) = (1/2) * w_3(q) * [2]_q = E_0(q) / (2 * [3]_q)` (`0.68764544 MeV` at
     bare `E_0`) from `SeniorityPairingAndHoyleTriadThreshold.tlPairingGap`:
     `Delta_pair^(TL)(Z, N) = (1 - (v_p + v_n)) * Delta_TL(q)` (`+Delta_TL` for even-even,
     `0` for odd-`A`, `-Delta_TL` for odd-odd).
   - A secondary comparison branch (`W3_Shell_SymHO_FermiSym_H4_AsqrtPair_logD`) evaluates
     the empirical-style `A^{-1/2}` scaling `(1 - (v_p + v_n)) * b_2 / A^{1/2}` and is
     explicitly documented in `caveats`.

5. **3D FCC Proton-Pair Simplicial Coulomb Repulsion (`E_C^(FCC,sph)` & `E_C^(FCC,disc,sym)`)**:
   - Form-B Bring-Schwinger cubic `alpha_EM^{-1}(q)`,
   - Canonical pion-Compton bond length `l_bond = (3/2) * lambda_bar_pi = 2.12072540 fm`,
   - 3D FCC close-packing Wigner-Seitz radius constant
     `r_0^(FCC) = (3 / (4 * pi * sqrt(2)))^{1/3} * l_bond = 1.17206015 fm`,
   - Continuum 3D FCC spherical Coulomb repulsion
     `E_C^(FCC,sph)(Z, A) = (3/5) * Z(Z - 1) * alpha_EM * hbar * c / (r_0^(FCC) * A^{1/3})`,
   - Exact Lane-N4 (`SimplicialCoulombGraphMetricDerivation`) isospin-symmetrized discrete
     3D FCC proton-pair inverse-distance sum over the `A`-site 3D FCC cluster:
     `E_C^(FCC,disc,sym)(Z, A) = (alpha_EM * hbar * c / l_bond) * (Z(Z - 1) / (A(A - 1))) * S_FCC(A)`.

6. **Multi-Anchor Evaluation (`q_0` vs `q_2t` vs `q_muon`) & QOU-Derived `m_n - m_p` Beta-Stability**:
   - Evaluates at full 95-dps working precision across `q_0 = q_at(95)` (1-term proton pin),
     `q_2t = q_two_term_borromean_at(95)` (2-term Borromean proton pin where
     `M_p^{2t}(q_2t) = M_p^{QCD}(q_2t) + M_p^{QED,conn}(q_2t)` includes the connected
     4th-order Borromean `V^3` electromagnetic self-energy, shifting `q` by
     `delta_q_2t = q_2t - q_0 = +1.239950519e-8 > 0`, `+11.170941 ppb`), and
     `q_muon = q_muon_at(95)` (ideal muon pin), stamping top-level `"q0Anchor": "comparison"`.
   - Predicts the isobaric valley of beta-stability `Z_*(A)` using QOU's own parameter-free
     two-term nucleon mass splitting `(m_n - m_p)_QOU(q) = Q_beta^{N=2,2t}(q) + m_e`
     (via `q_beta_kashiwara_n2_two_term_mev(q=q)`), using the AME2020 empirical splitting
     strictly only to identify `Z_exp(A)` from the experimental AME2020 table.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "substrate") not in sys.path:
    sys.path.insert(0, str(ROOT / "substrate"))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402
import mpmath as mp  # noqa: E402

set_compute_dps(80)

from _li_2_q_util import li_2_q  # noqa: E402
from canonical_mass import (  # noqa: E402
    np_qed_splitting_borromean_conn_mev,
    proton_qed_self_energy_borromean_mev,
    two_term_lagrangian_proton_mass_mev,
)
from codata_constants import M_E_MEV  # noqa: E402
from coulomb_energy import (  # noqa: E402
    HBAR_C_MEV_FM,
    LAMBDA_BAR_PI_FM,
)
from derived_masses import q_beta_kashiwara_n2_two_term_mev  # noqa: E402
from q_parameter import (  # noqa: E402
    q_at,
    q_muon_at,
    q_two_term_borromean_at,
)
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402


# ── Pure-integer binomial coefficient (zero `import math`) ───────────────────
def _int_comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k_use = k if k <= n - k else n - k
    num = 1
    for i in range(k_use):
        num = (num * (n - i)) // (i + 1)
    return num


# ── 80-dps Substrate & Nuclear Constants for a Given Anchor `q` ──────────────
def _solve_bring_schwinger_form_b_alpha_inv(q_val: mp.mpf) -> mp.mpf:
    """Solve Form-B Bring-Schwinger cubic for `alpha_EM^{-1}(q)` at 95 dps."""
    with mp.workdps(95):
        q = mp.mpf(q_val)
        one = mp.mpf(1)
        h = q - one / q
        h2 = h ** 2
        q2 = q + one / q
        q9 = (q ** 9 - q ** (-9)) / h
        q10 = (q ** 10 - q ** (-10)) / h
        t_term = q * q9 * q10 + mp.mpf(2) / (mp.mpf(3) * mp.pi)
        h_term = q2 / (mp.mpf(8) * mp.pi)
        a = (-t_term + mp.sqrt(t_term * t_term + mp.mpf(4) * h_term)) / (
            mp.mpf(2) * h_term
        )
        for _ in range(35):
            fa = -h_term * h2 * (a ** 3) + h_term * (a ** 2) + t_term * a - one
            dfa = -mp.mpf(3) * h_term * h2 * (a ** 2) + mp.mpf(2) * h_term * a + t_term
            da = fa / dfa
            a -= da
            if abs(da) < mp.mpf(10) ** (-88):
                break
        return one / a


def _derive_substrate_constants_for_q(q_val: mp.mpf) -> dict[str, mp.mpf]:
    """Derive 80-dps substrate, GPMT, Pauli/spin-orbit, pairing, nucleon splitting, and FCC Coulomb constants."""
    with mp.workdps(95):
        q = mp.mpf(q_val)
        m_e = mp.mpf(str(M_E_MEV))
        qi = mp.mpf(1) / q
        h = q - qi
        hbar_q = (q - mp.mpf(1)) / q
        two_q = q + qi
        three_q = q * q + mp.mpf(1) + qi * qi
        four_q = (q ** 4 - qi ** 4) / h
        s_skein = mp.sqrt(q) - mp.mpf(1) / mp.sqrt(q)
        dim_q = three_q / (s_skein * s_skein)

        # Bare and tower-resummed Hecke level-0 energy scale E_0
        e0_bare = m_e / (q * (q - mp.mpf(1)))
        z_tower = mp.mpf(1) / (mp.mpf(1) - hbar_q ** 2)
        e0_tower = e0_bare * z_tower

        # Convention-D, Borromean, and gg 2-body dimensionless fugacities and bond channels
        z_d = (q ** 3) / (q ** 2 + mp.mpf(1))
        z_gg = z_d - h / mp.mpf(2)
        tau_bor = (mp.mpf(4) + h ** 2 - mp.mpf(3) * (h ** 4) - (h ** 6)) / (h ** 2 + mp.mpf(4))

        ln_inv_zd = mp.log(mp.mpf(1) / z_d)
        ln_inv_zgg = mp.log(mp.mpf(1) / z_gg)
        g_tau2 = -li_2_q(-(tau_bor * tau_bor), q, qi)
        g_tau2_zd = -li_2_q(-(tau_bor * tau_bor * z_d), q, qi)
        bor_dimless = (tau_bor ** 2) * (mp.mpf(1) - z_d) + (z_d ** 2) * (g_tau2 - g_tau2_zd)

        # 2-body bond channels
        b2_log_d = e0_bare * ln_inv_zd
        b2_bor_d = e0_bare * bor_dimless
        b2_log_gg = e0_bare * ln_inv_zgg

        b2_log_d_tow = e0_tower * ln_inv_zd
        b2_bor_d_tow = e0_tower * bor_dimless
        b2_log_gg_tow = e0_tower * ln_inv_zgg

        # 3-body and 4-body GPMT cumulants (H_3 and H_4)
        q2_1 = q ** 2 + mp.mpf(1)
        q4_1 = q ** 4 + mp.mpf(1)
        q4_2_1 = q ** 4 + q ** 2 + mp.mpf(1)
        h4_mod_denom = (q2_1 ** 3) * q4_1 * q4_2_1

        d_mod_111 = -(q ** 3) / (q2_1 * q4_2_1)
        d_mod_211 = -(q ** 3) * q4_2_1 / ((q2_1 ** 3) * q4_1)
        d_mod_1111 = (q ** 7) / h4_mod_denom

        mu3_gpmt = -d_mod_111
        mu4_gpmt_h3 = mp.mpf(2) * d_mod_111  # = -2 * mu3_gpmt
        s_row3_h4_4 = -mp.mpf(3) * d_mod_211 + d_mod_1111
        mu4_gpmt_h4 = s_row3_h4_4 - mp.mpf(4) * mu3_gpmt

        w3_gpmt = e0_bare * mu3_gpmt
        w4_gpmt_h3 = e0_bare * mu4_gpmt_h3
        w4_gpmt_h4 = e0_bare * mu4_gpmt_h4

        w3_gpmt_tow = e0_tower * mu3_gpmt
        w4_gpmt_h3_tow = e0_tower * mu4_gpmt_h3
        w4_gpmt_h4_tow = e0_tower * mu4_gpmt_h4

        # Compton / Fermi oscillator quantum & symmetry energy coefficient
        e_osc_compton = e0_bare / hbar_q  # m_e / (q - 1)^2
        a_sym_compton = e_osc_compton * z_d
        a_sym_hecke = e0_bare * z_d

        # Spin-orbit coupling constants (parameter-free candidates)
        kappa_so_q1_sq = (q - mp.mpf(1)) ** 2
        kappa_so_reeb = (h * z_d) / mp.mpf(2)

        # Proved Temperley-Lieb singlet pairing gap (SeniorityPairingAndHoyleTriadThreshold.tlPairingGap)
        delta_tl_univ = (mp.mpf(1) / mp.mpf(2)) * w3_gpmt * two_q
        delta_tl_univ_tow = (mp.mpf(1) / mp.mpf(2)) * w3_gpmt_tow * two_q

        # Form-B fine-structure constant and 3D FCC pion-Compton Coulomb geometry
        alpha_em_inv = _solve_bring_schwinger_form_b_alpha_inv(q)
        alpha_em = mp.mpf(1) / alpha_em_inv
        hbar_c = mp.mpf(str(HBAR_C_MEV_FM))
        e_charge_sq_mev_fm = alpha_em * hbar_c

        # Neutral pion reduced Compton wavelength and bond length l_bond = (3/2) * lambda_bar_pi
        lambda_pi_fm = mp.mpf(str(LAMBDA_BAR_PI_FM))
        m_pi_mev = hbar_c / lambda_pi_fm
        l_bond_fm = (mp.mpf(3) / mp.mpf(2)) * lambda_pi_fm
        fcc_ws_factor = (mp.mpf(3) / (mp.mpf(4) * mp.pi * mp.sqrt(mp.mpf(2)))) ** (
            mp.mpf(1) / mp.mpf(3)
        )
        r0_fcc_fm = fcc_ws_factor * l_bond_fm
        a_c_fcc_mev = (mp.mpf(3) / mp.mpf(5)) * (e_charge_sq_mev_fm / r0_fcc_fm)

        # Legacy Wave-2 continuum radius r_0 = l_bond_fm = (3/2) * lambda_bar_pi for reference comparison
        r0_legacy_fm = l_bond_fm
        a_c_legacy_mev = (mp.mpf(3) / mp.mpf(5)) * (e_charge_sq_mev_fm / r0_legacy_fm)

        # QOU parameter-free two-term nucleon mass splitting (m_n - m_p)_QOU(q)
        m_p_2t_mev = mp.mpf(str(two_term_lagrangian_proton_mass_mev(q=q)))
        m_p_qed_conn_mev = mp.mpf(str(proton_qed_self_energy_borromean_mev(k_weighted=False, q=q)))
        dm_np_qed_conn_mev = mp.mpf(str(np_qed_splitting_borromean_conn_mev(weighting="plain", q=q)))
        q_beta_2t_mev = mp.mpf(str(q_beta_kashiwara_n2_two_term_mev(q=q, weighting="plain")))
        delta_m_np_qou_mev = q_beta_2t_mev + m_e
        m_n_2t_mev = m_p_2t_mev + delta_m_np_qou_mev

        return {
            "q": q,
            "q_inv": qi,
            "h": h,
            "hbar_q": hbar_q,
            "two_q": two_q,
            "three_q": three_q,
            "four_q": four_q,
            "dim_q": dim_q,
            "E0_bare_MeV": e0_bare,
            "Z_tower": z_tower,
            "E0_tower_MeV": e0_tower,
            "z_D": z_d,
            "z_gg": z_gg,
            "tau_Bor": tau_bor,
            "ln_inv_zD": ln_inv_zd,
            "bor_dimless": bor_dimless,
            "ln_inv_zgg": ln_inv_zgg,
            "b2_log_D_MeV": b2_log_d,
            "b2_Bor_D_MeV": b2_bor_d,
            "b2_log_gg_MeV": b2_log_gg,
            "b2_log_D_tower_MeV": b2_log_d_tow,
            "b2_Bor_D_tower_MeV": b2_bor_d_tow,
            "b2_log_gg_tower_MeV": b2_log_gg_tow,
            "w3_GPMT_MeV": w3_gpmt,
            "w4_GPMT_H3_MeV": w4_gpmt_h3,
            "w4_GPMT_H4_MeV": w4_gpmt_h4,
            "w3_GPMT_tower_MeV": w3_gpmt_tow,
            "w4_GPMT_H3_tower_MeV": w4_gpmt_h3_tow,
            "w4_GPMT_H4_tower_MeV": w4_gpmt_h4_tow,
            "E_osc_compton_MeV": e_osc_compton,
            "a_sym_compton_MeV": a_sym_compton,
            "a_sym_hecke_MeV": a_sym_hecke,
            "kappa_SO_q1_sq": kappa_so_q1_sq,
            "kappa_SO_reeb": kappa_so_reeb,
            "delta_TL_univ_MeV": delta_tl_univ,
            "delta_TL_univ_tower_MeV": delta_tl_univ_tow,
            "alpha_em_inv_form_b": alpha_em_inv,
            "e_charge_sq_MeV_fm": e_charge_sq_mev_fm,
            "m_pi_substrate_MeV": m_pi_mev,
            "lambda_pi_fm": lambda_pi_fm,
            "l_bond_fm": l_bond_fm,
            "r0_fcc_fm": r0_fcc_fm,
            "a_C_fcc_MeV": a_c_fcc_mev,
            "a_C_legacy_lbond_MeV": a_c_legacy_mev,
            "M_p_2t_lagrangian_MeV": m_p_2t_mev,
            "M_p_QED_conn_borromean_V3_MeV": m_p_qed_conn_mev,
            "Delta_m_np_QED_conn_borromean_V3_MeV": dm_np_qed_conn_mev,
            "Q_beta_N2_two_term_MeV": q_beta_2t_mev,
            "delta_m_np_qou_MeV": delta_m_np_qou_mev,
            "M_n_2t_lagrangian_MeV": m_n_2t_mev,
        }


# ── 1. Wave-2 Baseline Complexes (`apollonian_3tree` & `pauli_triangle`) ─────
def apollonian_3tree_triangulation(a_val: int) -> dict[str, int]:
    """Apollonian 3-tree f-vector: all vertices on boundary (`f0_int = 0, c = 0`)."""
    if a_val <= 1:
        return {"f0": a_val, "f1": 0, "f2": 0, "f3": 0, "f0_bdry": a_val, "f1_bdry": 0, "f2_bdry": 0, "f0_int": 0, "cycle_excess_c": 0}
    if a_val == 2:
        return {"f0": 2, "f1": 1, "f2": 0, "f3": 0, "f0_bdry": 2, "f1_bdry": 1, "f2_bdry": 0, "f0_int": 0, "cycle_excess_c": 0}
    if a_val == 3:
        return {"f0": 3, "f1": 3, "f2": 1, "f3": 0, "f0_bdry": 3, "f1_bdry": 3, "f2_bdry": 1, "f0_int": 0, "cycle_excess_c": 0}
    return {
        "f0": a_val,
        "f1": 3 * a_val - 6,
        "f2": 3 * a_val - 8,
        "f3": a_val - 3,
        "f0_bdry": a_val,
        "f1_bdry": 3 * a_val - 6,
        "f2_bdry": 2 * a_val - 4,
        "f0_int": 0,
        "cycle_excess_c": 0,
    }


def pauli_capped_triangulation_from_table(
    base_table: list[dict[str, int | bool]],
    z_val: int,
    n_val: int,
) -> dict[str, int]:
    """Pauli-capped `(Z, N)` simplicial ball complex (`pauli_k4_balanced_isospin`):
    `A_core = 2 * min(Z, N)` forms `base_table[A_core]`, while `D = |N - Z|` excess
    majority nucleons attach via maximal Pauli-legal degree-2 mixed-isospin surface
    triangles (`+2D` edges, `+D` triangles, `+0` tetrahedra).
    """
    a_val = z_val + n_val
    m_min = z_val if z_val <= n_val else n_val
    a_core = 2 * m_min
    d_exc = abs(n_val - z_val)
    if a_core == 0:
        return {"f0": a_val, "f1": 0, "f2": 0, "f3": 0}
    t_core = base_table[a_core]
    if a_core >= 3:
        f1 = int(t_core["f1"]) + 2 * d_exc
        f2 = int(t_core["f2"]) + d_exc
        f3 = int(t_core["f3"])
    elif a_core == 2:
        f1 = (1 + 2 * d_exc) if d_exc >= 1 else 1
        f2 = d_exc
        f3 = 0
    else:
        f1 = 0
        f2 = 0
        f3 = 0
    return {"f0": a_val, "f1": f1, "f2": f2, "f3": f3}


# ── 2. 3D FCC Lattice Clique Complex & Discrete Pair Inverse-Distance Sum ────
def precompute_3d_fcc_clique_and_coulomb(max_a: int = 295) -> tuple[list[dict[str, int]], list[mp.mpf]]:
    """Precompute 3D FCC nearest-neighbor clique f-vectors for `A = 0..max_a`
    and exact 95-dps discrete pair inverse-distance sums `S_FCC(M)` for `M = 0..max_a`.

    FCC lattice sites `(x, y, z) in Z^3` with `(x + y + z) % 2 == 0` are ordered
    deterministically by squared Euclidean distance `(2x-1)^2 + (2y-1)^2 + (2z-1)^2`
    from the origin regular-tetrahedron centroid `(1/2, 1/2, 1/2)`.
    In Lane N4 (`SimplicialCoulombGraphMetricDerivation`), the isospin-symmetrized
    discrete 3D FCC proton-pair electrostatic energy on an `A`-site nuclear cluster is:
      `E_C_disc_sym(Z, A) = (alpha * hbar * c / l_bond) * (Z(Z - 1) / (A(A - 1))) * S_FCC(A)`.
    """
    pts: list[tuple[int, int, int, int, int]] = []
    for x in range(-6, 8):
        for y in range(-6, 8):
            for z in range(-6, 8):
                if (x + y + z) % 2 == 0:
                    dx = 2 * x - 1
                    dy = 2 * y - 1
                    dz = 2 * z - 1
                    r2 = dx * dx + dy * dy + dz * dz
                    l1 = abs(dx) + abs(dy) + abs(dz)
                    pts.append((r2, l1, x, y, z))
    pts.sort()
    coords = [(x, y, z) for _, _, x, y, z in pts[:max_a]]

    adj: list[set[int]] = [set() for _ in range(max_a)]
    fcc_table: list[dict[str, int]] = [
        {"f0": 0, "f1": 0, "f2": 0, "f3": 0},
    ]
    f1 = 0
    f2 = 0
    f3 = 0
    for i in range(max_a):
        xi, yi, zi = coords[i]
        nbrs: list[int] = []
        for j in range(i):
            xj, yj, zj = coords[j]
            d2 = (xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2
            if d2 == 2:
                nbrs.append(j)
                adj[i].add(j)
                adj[j].add(i)
        f1 += len(nbrs)
        nn = len(nbrs)
        for a_idx in range(nn):
            u = nbrs[a_idx]
            for b_idx in range(a_idx + 1, nn):
                v = nbrs[b_idx]
                if v in adj[u]:
                    f2 += 1
                    for c_idx in range(b_idx + 1, nn):
                        w = nbrs[c_idx]
                        if w in adj[u] and w in adj[v]:
                            f3 += 1
        fcc_table.append({"f0": i + 1, "f1": f1, "f2": f2, "f3": f3})

    # Precompute 95-dps inverse distances 1 / sqrt(d2 / 2) for all cluster sizes M = 0..max_a
    with mp.workdps(95):
        inv_sqrt_cache: dict[int, mp.mpf] = {}
        coulomb_pair_sums: list[mp.mpf] = [mp.mpf(0), mp.mpf(0)]
        running_sum = mp.mpf(0)
        for i in range(1, max_a):
            xi, yi, zi = coords[i]
            for j in range(i):
                xj, yj, zj = coords[j]
                d2 = (xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2
                if d2 not in inv_sqrt_cache:
                    # Nearest-neighbor FCC distance has d2 = 2 => normalized bond distance = 1
                    inv_sqrt_cache[d2] = mp.mpf(1) / mp.sqrt(mp.mpf(d2) / mp.mpf(2))
                running_sum += inv_sqrt_cache[d2]
            coulomb_pair_sums.append(running_sum)

    return fcc_table, coulomb_pair_sums


# ── 3. Coordinate-Verified 3D Euclidean Freudenthal-Kuhn Lattice Ball (`A = 1..295`) ──
def verify_compact_3ball_triangulation(t: dict[str, int]) -> bool:
    """Verify the 7 exact structural conditions of Lean `Compact3BallTriangulation`."""
    f0 = t["f0"]
    f1 = t["f1"]
    f2 = t["f2"]
    f3 = t["f3"]
    f0b = t["f0_bdry"]
    f1b = t["f1_bdry"]
    f2b = t["f2_bdry"]
    if f0 < 4 or f0b < 4 or f0b > f0 or f3 < 1:
        return False
    euler_ball = (f0 + f2) == (f1 + f3 + 1)
    euler_bdry = (f0b + f2b) == (f1b + 2)
    handshake_bdry = (3 * f2b) == (2 * f1b)
    handshake_cells = (4 * f3 + f2b) == (2 * f2)
    return euler_ball and euler_bdry and handshake_bdry and handshake_cells


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
    """True iff the 4 lattice points form a canonical Freudenthal-Kuhn 3-simplex of a unit cube."""
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


def precompute_3d_kuhn_lattice_balls(max_a: int = 295) -> list[dict[str, int | bool]]:
    """Single-pass coordinate-verified 3D Euclidean Freudenthal-Kuhn lattice ball
    triangulations for `A = 0..max_a`.
    """
    table: list[dict[str, int | bool]] = [
        {
            "f0": 0, "f1": 0, "f2": 0, "f3": 0,
            "f0_bdry": 0, "f1_bdry": 0, "f2_bdry": 0,
            "f0_int": 0, "cycle_excess_c": 0,
            "valid_Compact3BallTriangulation": False,
            "all_cells_canonical_kuhn": True,
        }
    ]
    for a_small in (1, 2, 3):
        t_sm = apollonian_3tree_triangulation(a_small)
        table.append({
            **t_sm,
            "valid_Compact3BallTriangulation": False,
            "all_cells_canonical_kuhn": True,
        })

    pts: list[tuple[int, int, int]] = []
    rad_bound = 6
    while len(pts) < max(max_a + 64, 500):
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

    def _orient_outward(a: int, b: int, c: int, op: int) -> tuple[int, int, int]:
        d_val = _int_det_3d(ordered_coords[a], ordered_coords[b], ordered_coords[c], ordered_coords[op])
        if d_val == 0:
            raise ValueError("Degenerate zero-determinant simplex encountered in 3D orientation.")
        return (a, b, c) if d_val < 0 else (a, c, b)

    tetrahedra: list[tuple[int, int, int, int]] = [(0, 1, 2, 3)]
    occupied_kuhn_keys: set[tuple[tuple[int, int, int], tuple[tuple[int, int, int], ...]]] = {
        _canonical_kuhn_key((ordered_coords[0], ordered_coords[1], ordered_coords[2], ordered_coords[3]))
    }
    edges_all: set[tuple[int, int]] = set()
    triangles_all: set[tuple[int, int, int]] = set()
    for a_i in range(4):
        for b_i in range(a_i + 1, 4):
            edges_all.add((a_i, b_i))
            for c_i in range(b_i + 1, 4):
                triangles_all.add((a_i, b_i, c_i))

    bdry_map: dict[frozenset[int], tuple[int, int, int]] = {}
    for a_i, b_i, c_i, op_i in [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 3, 1), (1, 2, 3, 0)]:
        bdry_map[frozenset((a_i, b_i, c_i))] = _orient_outward(a_i, b_i, c_i, op_i)

    def _record_current_state() -> dict[str, int | bool]:
        f0 = len(ordered_coords)
        f1 = len(edges_all)
        f2 = len(triangles_all)
        f3 = len(tetrahedra)
        bdry_verts: set[int] = set()
        bdry_edges: set[tuple[int, int]] = set()
        for a_i, b_i, c_i in bdry_map.values():
            bdry_verts.update((a_i, b_i, c_i))
            for u, v in ((a_i, b_i), (a_i, c_i), (b_i, c_i)):
                bdry_edges.add((u, v) if u < v else (v, u))
        f0_bdry = len(bdry_verts)
        f1_bdry = len(bdry_edges)
        f2_bdry = len(bdry_map)
        t_dict = {
            "f0": f0,
            "f1": f1,
            "f2": f2,
            "f3": f3,
            "f0_bdry": f0_bdry,
            "f1_bdry": f1_bdry,
            "f2_bdry": f2_bdry,
            "f0_int": f0 - f0_bdry,
            "cycle_excess_c": f3 - (f0 - 3),
        }
        is_valid = verify_compact_3ball_triangulation(t_dict)
        return {
            **t_dict,
            "valid_Compact3BallTriangulation": is_valid,
            "all_cells_canonical_kuhn": len(occupied_kuhn_keys) == f3,
        }

    table.append(_record_current_state())

    for v_idx in range(4, max_a):
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
            raise RuntimeError(f"No visible canonical Freudenthal-Kuhn vertex found at step {v_idx}.")
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
            new_tet = (t_sorted[0], t_sorted[1], t_sorted[2], t_sorted[3])
            tetrahedra.append(new_tet)
            occupied_kuhn_keys.add(
                _canonical_kuhn_key(
                    (
                        ordered_coords[new_tet[0]],
                        ordered_coords[new_tet[1]],
                        ordered_coords[new_tet[2]],
                        ordered_coords[new_tet[3]],
                    )
                )
            )
            for u in (a_i, b_i, c_i):
                edges_all.add((u, v_idx) if u < v_idx else (v_idx, u))
            for u, w in ((a_i, b_i), (a_i, c_i), (b_i, c_i)):
                tri_s = tuple(sorted((u, w, v_idx)))
                triangles_all.add((tri_s[0], tri_s[1], tri_s[2]))

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

        table.append(_record_current_state())

    return table


# ── 4. Close-Packed 3D Mackay Shell-Interpolated Simplicial Ball (`A = 1..295`) ──
def close_packed_f0(k: int) -> int:
    return (10 * (k ** 3) + 15 * (k ** 2) + 11 * k + 3) // 3


def close_packed_f0_bdry(k: int) -> int:
    return 10 * (k ** 2) + 2


def close_packed_f1_bdry(k: int) -> int:
    return 30 * (k ** 2)


def close_packed_f2_bdry(k: int) -> int:
    return 20 * (k ** 2)


def close_packed_f3(k: int) -> int:
    return 20 * (k ** 3)


def close_packed_f2(k: int) -> int:
    return 40 * (k ** 3) + 10 * (k ** 2)


def close_packed_f1(k: int) -> int:
    return (70 * (k ** 3) + 45 * (k ** 2) + 11 * k) // 3


def close_packed_3d_shell_ball_triangulation(a_val: int) -> dict[str, int | bool]:
    """Close-packed 3D shell-interpolated ball triangulation matching Lean `closePackedShellBall`."""
    if a_val <= 3:
        t_sm = apollonian_3tree_triangulation(a_val)
        return {**t_sm, "valid_Compact3BallTriangulation": False}
    if a_val == 4:
        return {
            "f0": 4, "f1": 6, "f2": 4, "f3": 1,
            "f0_bdry": 4, "f1_bdry": 6, "f2_bdry": 4,
            "f0_int": 0, "cycle_excess_c": 0,
            "valid_Compact3BallTriangulation": True,
        }
    if a_val < 13:
        steps = a_val - 4
        a_bdry = 4 + steps
        f3 = 1 + 2 * steps
    else:
        k = 1
        while close_packed_f0(k + 1) <= a_val:
            k += 1
        a_k = close_packed_f0(k)
        if a_val == a_k:
            a_bdry = close_packed_f0_bdry(k)
            f3 = close_packed_f3(k)
        else:
            a_next = close_packed_f0(k + 1)
            da_shell = a_next - a_k
            rem = a_val - a_k
            df3_shell = close_packed_f3(k + 1) - close_packed_f3(k)
            f3 = close_packed_f3(k) + (df3_shell * rem) // da_shell
            dbdry_shell = close_packed_f0_bdry(k + 1) - close_packed_f0_bdry(k)
            a_bdry = close_packed_f0_bdry(k) + (dbdry_shell * rem) // da_shell

    f1_bdry = 3 * a_bdry - 6
    f2_bdry = 2 * a_bdry - 4
    f2 = 2 * f3 + a_bdry - 2
    f1 = a_val + f3 + a_bdry - 3
    t_dict = {
        "f0": a_val,
        "f1": f1,
        "f2": f2,
        "f3": f3,
        "f0_bdry": a_bdry,
        "f1_bdry": f1_bdry,
        "f2_bdry": f2_bdry,
        "f0_int": a_val - a_bdry,
        "cycle_excess_c": f3 - (a_val - 3),
    }
    return {
        **t_dict,
        "valid_Compact3BallTriangulation": verify_compact_3ball_triangulation(t_dict),
    }


def precompute_3d_close_packed_shell_balls(max_a: int = 295) -> list[dict[str, int | bool]]:
    table: list[dict[str, int | bool]] = [
        {
            "f0": 0, "f1": 0, "f2": 0, "f3": 0,
            "f0_bdry": 0, "f1_bdry": 0, "f2_bdry": 0,
            "f0_int": 0, "cycle_excess_c": 0,
            "valid_Compact3BallTriangulation": False,
        }
    ]
    for a_val in range(1, max_a + 1):
        table.append(close_packed_3d_shell_ball_triangulation(a_val))
    return table


# ── 5. 3D Harmonic-Oscillator + Mayer-Jensen Spin-Orbit Subshell Table ───────
# Format: (label, N_osc, n_r, l, two_j, is_intruder_pushed_down_from_N_plus_1, magic_after_or_0)
# Covers cumulative nucleon capacity 210 >= max_N = 177 across all 3,558 AME2020 nuclides.
SPECTROSCOPIC_SUBSHELLS: list[tuple[str, int, int, int, int, bool, int]] = [
    # N_osc = 0 -> Magic 2
    ("1s_{1/2}", 0, 0, 0, 1, False, 2),
    # N_osc = 1 -> Magic 8
    ("1p_{3/2}", 1, 0, 1, 3, False, 0),
    ("1p_{1/2}", 1, 0, 1, 1, False, 8),
    # N_osc = 2 -> Magic 20
    ("1d_{5/2}", 2, 0, 2, 5, False, 0),
    ("2s_{1/2}", 2, 1, 0, 1, False, 0),
    ("1d_{3/2}", 2, 0, 2, 3, False, 20),
    # N_osc = 3: 1f_{7/2} -> Magic 28
    ("1f_{7/2}", 3, 0, 3, 7, False, 28),
    # N_osc = 3 remainder + 1g_{9/2} intruder from N_osc = 4 -> Magic 50
    ("2p_{3/2}", 3, 1, 1, 3, False, 0),
    ("1f_{5/2}", 3, 0, 3, 5, False, 0),
    ("2p_{1/2}", 3, 1, 1, 1, False, 0),
    ("1g_{9/2}", 4, 0, 4, 9, True, 50),
    # N_osc = 4 remainder + 1h_{11/2} intruder from N_osc = 5 -> Magic 82
    ("1g_{7/2}", 4, 0, 4, 7, False, 0),
    ("2d_{5/2}", 4, 1, 2, 5, False, 0),
    ("2d_{3/2}", 4, 1, 2, 3, False, 0),
    ("3s_{1/2}", 4, 2, 0, 1, False, 0),
    ("1h_{11/2}", 5, 0, 5, 11, True, 82),
    # N_osc = 5 remainder + 1i_{13/2} intruder from N_osc = 6 -> Magic 126
    ("1h_{9/2}", 5, 0, 5, 9, False, 0),
    ("2f_{7/2}", 5, 1, 3, 7, False, 0),
    ("2f_{5/2}", 5, 1, 3, 5, False, 0),
    ("3p_{3/2}", 5, 2, 1, 3, False, 0),
    ("3p_{1/2}", 5, 2, 1, 1, False, 0),
    ("1i_{13/2}", 6, 0, 6, 13, True, 126),
    # N_osc = 6 remainder + 1j_{15/2} intruder from N_osc = 7 -> Magic 184
    ("2g_{9/2}", 6, 1, 4, 9, False, 0),
    ("3d_{5/2}", 6, 2, 2, 5, False, 0),
    ("1i_{11/2}", 6, 0, 6, 11, False, 0),
    ("2g_{7/2}", 6, 1, 4, 7, False, 0),
    ("4s_{1/2}", 6, 3, 0, 1, False, 0),
    ("3d_{3/2}", 6, 2, 2, 3, False, 0),
    ("1j_{15/2}", 7, 0, 7, 15, True, 184),
    # Post-184 subshells covering up to 210 states (> max_N = 177)
    ("1j_{13/2}", 7, 0, 7, 13, False, 0),
    ("2h_{11/2}", 7, 1, 5, 11, False, 0),
]


def _two_l_dot_s_exact(l_val: int, two_j: int) -> int:
    """Return `2 * <l . s>` as an exact integer: `l` for `j = l + 1/2`, `-(l + 1)` for `j = l - 1/2`."""
    if l_val == 0:
        return 0
    if two_j == 2 * l_val + 1:
        return l_val
    if two_j == 2 * l_val - 1:
        return -(l_val + 1)
    raise ValueError(f"Invalid (l={l_val}, 2j={two_j})")


def precompute_spectroscopic_shell_tables() -> dict[str, list[int]]:
    """Precompute exact integer cumulative 3D harmonic-oscillator excitation quanta
    and spin-orbit `<2 l . s>` sums for nucleon numbers `M = 0..210`.
    """
    cum_n_osc: list[int] = [0]
    cum_two_ls: list[int] = [0]
    single_n_osc: list[int] = [0]
    single_two_ls: list[int] = [0]
    magic_closures: list[int] = []

    running_n = 0
    running_ls = 0
    cum_cap = 0
    for _label, n_osc, _nr, l_val, two_j, _intr, magic_tag in SPECTROSCOPIC_SUBSHELLS:
        deg = two_j + 1
        two_ls = _two_l_dot_s_exact(l_val, two_j)
        for _ in range(deg):
            running_n += n_osc
            running_ls += two_ls
            cum_n_osc.append(running_n)
            cum_two_ls.append(running_ls)
            single_n_osc.append(n_osc)
            single_two_ls.append(two_ls)
        cum_cap += deg
        if magic_tag > 0:
            if cum_cap != magic_tag:
                raise RuntimeError(f"Magic closure mismatch: got {cum_cap}, expected {magic_tag}")
            magic_closures.append(cum_cap)

    # Pure 3D isotropic HO degeneracy filling (without intruder reorder)
    ho_pure_cum_n_osc: list[int] = [0]
    running_ho_pure = 0
    for n_shell in range(8):
        deg_shell = (n_shell + 1) * (n_shell + 2)
        for _ in range(deg_shell):
            running_ho_pure += n_shell
            ho_pure_cum_n_osc.append(running_ho_pure)

    return {
        "cum_n_osc": cum_n_osc,
        "cum_two_ls": cum_two_ls,
        "single_n_osc": single_n_osc,
        "single_two_ls": single_two_ls,
        "ho_pure_cum_n_osc": ho_pure_cum_n_osc,
        "magic_closures": magic_closures,
    }


# ── 6. Load All 3,558 Nuclides Directly from Vendored `computations/data/ame2020.json` ──
def load_all_3558_nuclides_from_ame2020() -> tuple[list[dict[str, object]], mp.mpf]:
    """Load all 3,558 AME2020 nuclides directly from `computations/data/ame2020.json`
    using `parse_float=str` -> `mp.mpf` at 95 dps (zero float64 conversion, zero
    50-digit witness truncation), and extract the empirical AME2020 `(m_n - m_p)`
    mass difference strictly for the experimental `Z_exp(A)` comparator.
    """
    ame_path = ROOT / "data" / "ame2020.json"
    ame_obj = json.loads(ame_path.read_text(encoding="utf-8"), parse_float=str)
    nuclides: list[dict[str, object]] = []
    mass_excess_n_kev = mp.mpf(0)
    mass_excess_1h_kev = mp.mpf(0)

    with mp.workdps(95):
        m_e = mp.mpf(str(M_E_MEV))
        kilo = mp.mpf(1000)
        for entry in ame_obj["entries"]:
            z_val = int(entry["Z"])
            n_val = int(entry["N"])
            a_val = int(entry["A"])
            sym = str(entry["element"])
            me_kev = mp.mpf(str(entry["mass_excess_keV"]))
            if z_val == 0 and n_val == 1:
                mass_excess_n_kev = me_kev
            elif z_val == 1 and n_val == 0:
                mass_excess_1h_kev = me_kev

            if a_val <= 1:
                b_ame = mp.mpf(0)
                ba_ame = mp.mpf(0)
            else:
                ba_kev = mp.mpf(str(entry["binding_energy_per_A_keV"]))
                ba_ame = ba_kev / kilo
                b_ame = ba_ame * mp.mpf(a_val)

            nuclides.append({
                "Z": z_val,
                "N": n_val,
                "A": a_val,
                "symbol": sym,
                "nuclide": f"{a_val}{sym}",
                "B_AME_MeV": b_ame,
                "BA_AME_MeV": ba_ame,
                "mass_excess_AME_keV": me_kev,
            })

        # Nuclear mass difference (m_n - m_p)_AME = (Delta_n - Delta_{1H}) / 1000 + m_e
        delta_m_np_ame_mev = ((mass_excess_n_kev - mass_excess_1h_kev) / kilo) + m_e

    return nuclides, delta_m_np_ame_mev


# ── 7. Precomputed Fractional Powers `A^{-1/3}` and `A^{-1/2}` at 95 dps ─────
def precompute_a_powers(max_a: int = 295) -> tuple[list[mp.mpf], list[mp.mpf]]:
    """Precompute `A^{-1/3}` and `A^{-1/2}` at 95 dps for `A = 0..max_a`."""
    with mp.workdps(95):
        inv_a13: list[mp.mpf] = [mp.mpf(0)]
        inv_a12: list[mp.mpf] = [mp.mpf(0)]
        third = mp.mpf(1) / mp.mpf(3)
        for a_val in range(1, max_a + 1):
            a_mp = mp.mpf(a_val)
            inv_a13.append(mp.mpf(1) / (a_mp ** third))
            inv_a12.append(mp.mpf(1) / mp.sqrt(a_mp))
        return inv_a13, inv_a12


# ── 8. Evaluate Wave-2 & Wave-3 Parameter-Free Branches for Any Nuclide ──────
BRANCH_KEYS: list[str] = [
    "W2_3tree_logD_E0tower",
    "W2_3tree_logGG_E0tower",
    "W2_pauli_triangle_logGG_E0tower",
    "W3_FCC_Clique_H3_logD",
    "W3_FCC_Clique_H3_BorD",
    "W3_Kuhn_PauliCore_H4_logD",
    "W3_Kuhn_FermiSym_H4_logD",
    "W3_Kuhn_FermiSym_H4_BorD",
    "W3_Shell_PauliCore_H4_logD",
    "W3_Shell_HO_Pure_H4_logD",
    "W3_Shell_SymHO_FermiSym_H4_logD",
    "W3_Shell_SymHO_FermiSym_H4_BorD",
    "W3_Shell_SymHO_FermiSym_H4_DiscC_logD",
    "W3_Shell_SymHO_FermiSym_H4_AsqrtPair_logD",
]


def evaluate_nuclide_branches(
    z_val: int,
    n_val: int,
    c: dict[str, mp.mpf],
    t_3tree_table: list[dict[str, int | bool]],
    t_fcc: dict[str, int],
    t_kuhn_table: list[dict[str, int | bool]],
    t_shell_table: list[dict[str, int | bool]],
    shell_tabs: dict[str, list[int]],
    coulomb_pair_sums: list[mp.mpf],
    inv_a13: list[mp.mpf],
    inv_a12: list[mp.mpf],
) -> dict[str, mp.mpf]:
    """Evaluate Wave-2 and Wave-3 parameter-free nuclear binding energy branches at 95 dps."""
    with mp.workdps(95):
        a_val = z_val + n_val
        if a_val <= 1:
            zero = mp.mpf(0)
            return {k: zero for k in BRANCH_KEYS}

        t_3tree = t_3tree_table[a_val]
        t_kuhn = t_kuhn_table[a_val]
        t_shell = t_shell_table[a_val]

        a_mp = mp.mpf(a_val)
        ia13 = inv_a13[a_val]
        ia12 = inv_a12[a_val]
        zz1 = mp.mpf(z_val * (z_val - 1))

        # ── Coulomb repulsion channels ──
        # 1. Legacy Wave-2 continuum spherical Coulomb (r_0 = l_bond = 2.12072540 fm)
        e_c_legacy = c["a_C_legacy_lbond_MeV"] * zz1 * ia13
        # 2. Wave-3 3D FCC close-packed continuum spherical Coulomb (r_0^FCC = 1.17206015 fm)
        e_c_fcc_sph = c["a_C_fcc_MeV"] * zz1 * ia13
        # 3. Wave-3 exact Lane-N4 (SimplicialCoulombGraphMetricDerivation) isospin-symmetrized
        #    discrete 3D FCC proton-pair inverse-distance sum over the A-site 3D FCC cluster:
        #    E_C_disc_sym(Z, A) = (e^2 / l_bond) * (Z(Z - 1) / (A(A - 1))) * S_FCC(A)
        if z_val >= 2 and a_val >= 2:
            e_c_fcc_disc_sym = (
                (c["e_charge_sq_MeV_fm"] / c["l_bond_fm"])
                * (zz1 / mp.mpf(a_val * (a_val - 1)))
                * coulomb_pair_sums[a_val]
            )
        else:
            e_c_fcc_disc_sym = mp.mpf(0)

        # ── Temperley-Lieb seniority pairing (SeniorityPairingAndHoyleTriadThreshold.tlPairingGap) ──
        v_sen = (z_val % 2) + (n_val % 2)
        pair_sign = mp.mpf(1 - v_sen)  # +1 even-even, 0 odd-A, -1 odd-odd
        delta_pair_tl = pair_sign * c["delta_TL_univ_MeV"]
        # Secondary comparison pairing branch: +/- b2 / sqrt(A)
        delta_pair_asqrt_logd = pair_sign * c["b2_log_D_MeV"] * ia12

        # ── 3D Harmonic-Oscillator kinetic promotion, Spin-Orbit, & Fermi symmetry energy ──
        # (a) Pure 3D HO excitation quanta above 0s shell (zero unproved -3/4 CoM offset):
        #     N_ho_pure(Z, N) = ho_pure[Z] + ho_pure[N] (already includes Pauli (Z, N) asymmetry)
        ho_pure = shell_tabs["ho_pure_cum_n_osc"]
        n_ho_pure = ho_pure[z_val] + ho_pure[n_val]
        e_kin_ho_pure = mp.mpf(n_ho_pure) * c["E0_bare_MeV"] * ia13

        # (b) Symmetric Z = N = A/2 3D HO excitation quanta (zero (N - Z) asymmetry, so
        #     combining with -E_sym_compton(Z, N) does not double-count isospin asymmetry):
        m_half = a_val // 2
        if a_val % 2 == 0:
            n_ho_sym = 2 * ho_pure[m_half]
        else:
            n_ho_sym = ho_pure[m_half] + ho_pure[m_half + 1]
        e_kin_ho_sym = mp.mpf(n_ho_sym) * c["E0_bare_MeV"] * ia13

        # Spin-orbit subshell stabilization / gap shift (-kappa_SO * <2 l . s> * hbar * omega_q)
        cum_two_ls = shell_tabs["cum_two_ls"]
        total_two_ls = cum_two_ls[z_val] + cum_two_ls[n_val]
        e_so_shift_hecke = -c["kappa_SO_reeb"] * mp.mpf(total_two_ls) * c["E0_bare_MeV"] * ia13
        e_so_shift_compton = -c["kappa_SO_q1_sq"] * mp.mpf(total_two_ls) * c["E_osc_compton_MeV"] * ia13

        # Discrete Pauli shell-filling asymmetry E_fill(Z) + E_fill(N) - 2 E_fill(A/2)
        cum_n_osc = shell_tabs["cum_n_osc"]
        if a_val % 2 == 0:
            n_osc_sym = 2 * cum_n_osc[m_half]
            two_ls_sym = 2 * cum_two_ls[m_half]
        else:
            n_osc_sym = cum_n_osc[m_half] + cum_n_osc[m_half + 1]
            two_ls_sym = cum_two_ls[m_half] + cum_two_ls[m_half + 1]
        delta_n_osc_asym = (cum_n_osc[z_val] + cum_n_osc[n_val]) - n_osc_sym
        delta_two_ls_asym = total_two_ls - two_ls_sym
        e_pauli_so_asym = (
            mp.mpf(delta_n_osc_asym) - c["kappa_SO_q1_sq"] * mp.mpf(delta_two_ls_asym)
        ) * c["E_osc_compton_MeV"] * ia13

        # Parameter-free Compton Fermi quadratic symmetry energy a_sym * (N - Z)^2 / A
        nz_diff_sq = mp.mpf((n_val - z_val) ** 2)
        e_sym_compton = c["a_sym_compton_MeV"] * nz_diff_sq / a_mp

        # ── Wave-2 Baseline Branches (at E0_tower, legacy r_0 = l_bond Coulomb) ──
        f1_3t = mp.mpf(int(t_3tree["f1"]))
        f2_3t = mp.mpf(int(t_3tree["f2"]))
        f3_3t = mp.mpf(int(t_3tree["f3"]))
        w2_3tree_logd = (
            f1_3t * c["b2_log_D_tower_MeV"]
            + f2_3t * c["w3_GPMT_tower_MeV"]
            + f3_3t * c["w4_GPMT_H3_tower_MeV"]
            - e_c_legacy
        )
        w2_3tree_loggg = (
            f1_3t * c["b2_log_gg_tower_MeV"]
            + f2_3t * c["w3_GPMT_tower_MeV"]
            + f3_3t * c["w4_GPMT_H3_tower_MeV"]
            - e_c_legacy
        )
        t_pt = pauli_capped_triangulation_from_table(t_3tree_table, z_val, n_val)
        w2_pauli_tri_loggg = (
            mp.mpf(t_pt["f1"]) * c["b2_log_gg_tower_MeV"]
            + mp.mpf(t_pt["f2"]) * c["w3_GPMT_tower_MeV"]
            + mp.mpf(t_pt["f3"]) * c["w4_GPMT_H3_tower_MeV"]
            - e_c_legacy
        )

        # ── Wave-3 Family A: 3D FCC Nearest-Neighbor Clique Ball + H_3 GPMT + tlPairingGap ──
        f1_fcc = mp.mpf(t_fcc["f1"])
        f2_fcc = mp.mpf(t_fcc["f2"])
        f3_fcc = mp.mpf(t_fcc["f3"])
        b_fcc_h3_logd = (
            f1_fcc * c["b2_log_D_MeV"]
            + f2_fcc * c["w3_GPMT_MeV"]
            + f3_fcc * c["w4_GPMT_H3_MeV"]
            - e_pauli_so_asym
            + delta_pair_tl
            - e_c_fcc_sph
        )
        b_fcc_h3_bord = (
            f1_fcc * c["b2_Bor_D_MeV"]
            + f2_fcc * c["w3_GPMT_MeV"]
            + f3_fcc * c["w4_GPMT_H3_MeV"]
            - e_pauli_so_asym
            + delta_pair_tl
            - e_c_fcc_sph
        )

        # ── Wave-3 Family B: Coordinate-Verified 3D Kuhn Lattice Ball + H_4 GPMT + tlPairingGap ──
        # (B1) Pauli-capped core A_core = 2*min(Z,N) + D surface triangles (zero extra -E_sym)
        t_kuhn_pauli = pauli_capped_triangulation_from_table(t_kuhn_table, z_val, n_val)
        b_kuhn_pauli_h4_logd = (
            mp.mpf(t_kuhn_pauli["f1"]) * c["b2_log_D_MeV"]
            + mp.mpf(t_kuhn_pauli["f2"]) * c["w3_GPMT_MeV"]
            + mp.mpf(t_kuhn_pauli["f3"]) * c["w4_GPMT_H4_MeV"]
            - e_so_shift_hecke
            + delta_pair_tl
            - e_c_fcc_sph
        )
        # (B2) Full-A 3D Kuhn ball with Compton Fermi symmetry energy -E_sym_compton
        f1_kuhn = mp.mpf(int(t_kuhn["f1"]))
        f2_kuhn = mp.mpf(int(t_kuhn["f2"]))
        f3_kuhn = mp.mpf(int(t_kuhn["f3"]))
        b_kuhn_sym_h4_logd = (
            f1_kuhn * c["b2_log_D_MeV"]
            + f2_kuhn * c["w3_GPMT_MeV"]
            + f3_kuhn * c["w4_GPMT_H4_MeV"]
            - e_sym_compton
            - e_so_shift_hecke
            + delta_pair_tl
            - e_c_fcc_sph
        )
        b_kuhn_sym_h4_bord = (
            f1_kuhn * c["b2_Bor_D_MeV"]
            + f2_kuhn * c["w3_GPMT_MeV"]
            + f3_kuhn * c["w4_GPMT_H4_MeV"]
            - e_sym_compton
            - e_so_shift_hecke
            + delta_pair_tl
            - e_c_fcc_sph
        )

        # ── Wave-3 Family C: 3D Close-Packed Shell Ball + H_4 GPMT (Clean Non-Double-Counted Branches) ──
        # (C1) Pauli-capped shell ball + symmetric 3D HO promotion (zero extra -E_sym)
        t_shell_pauli = pauli_capped_triangulation_from_table(t_shell_table, z_val, n_val)
        b_shell_pauli_h4_logd = (
            mp.mpf(t_shell_pauli["f1"]) * c["b2_log_D_MeV"]
            + mp.mpf(t_shell_pauli["f2"]) * c["w3_GPMT_MeV"]
            + mp.mpf(t_shell_pauli["f3"]) * c["w4_GPMT_H4_MeV"]
            - e_kin_ho_sym
            - e_so_shift_hecke
            + delta_pair_tl
            - e_c_fcc_sph
        )
        # (C2) Full-A shell ball + pure (Z, N) 3D HO promotion E_kin_ho_pure(Z, N) (zero extra -E_sym)
        f1_sh = mp.mpf(int(t_shell["f1"]))
        f2_sh = mp.mpf(int(t_shell["f2"]))
        f3_sh = mp.mpf(int(t_shell["f3"]))
        b_shell_ho_pure_h4_logd = (
            f1_sh * c["b2_log_D_MeV"]
            + f2_sh * c["w3_GPMT_MeV"]
            + f3_sh * c["w4_GPMT_H4_MeV"]
            - e_kin_ho_pure
            - e_so_shift_hecke
            + delta_pair_tl
            - e_c_fcc_sph
        )
        # (C3) Full-A shell ball + symmetric 3D HO promotion E_kin_ho_sym(A) + Compton Fermi symmetry -E_sym_compton(Z, N)
        b_shell_symho_fermisym_h4_logd = (
            f1_sh * c["b2_log_D_MeV"]
            + f2_sh * c["w3_GPMT_MeV"]
            + f3_sh * c["w4_GPMT_H4_MeV"]
            - e_kin_ho_sym
            - e_sym_compton
            - e_so_shift_hecke
            + delta_pair_tl
            - e_c_fcc_sph
        )
        b_shell_symho_fermisym_h4_bord = (
            f1_sh * c["b2_Bor_D_MeV"]
            + f2_sh * c["w3_GPMT_MeV"]
            + f3_sh * c["w4_GPMT_H4_MeV"]
            - e_kin_ho_sym
            - e_sym_compton
            - e_so_shift_hecke
            + delta_pair_tl
            - e_c_fcc_sph
        )
        # (C4) Same with exact Lane-N4 isospin-symmetrized discrete 3D FCC Coulomb E_C_disc_sym(Z, A)
        b_shell_symho_fermisym_h4_discc_logd = (
            f1_sh * c["b2_log_D_MeV"]
            + f2_sh * c["w3_GPMT_MeV"]
            + f3_sh * c["w4_GPMT_H4_MeV"]
            - e_kin_ho_sym
            - e_sym_compton
            - e_so_shift_hecke
            + delta_pair_tl
            - e_c_fcc_disc_sym
        )
        # (C5) Secondary comparison branch with +/- b2 / sqrt(A) pairing instead of tlPairingGap
        b_shell_symho_fermisym_h4_asqrt_logd = (
            f1_sh * c["b2_log_D_MeV"]
            + f2_sh * c["w3_GPMT_MeV"]
            + f3_sh * c["w4_GPMT_H4_MeV"]
            - e_kin_ho_sym
            - e_sym_compton
            - e_so_shift_hecke
            + delta_pair_asqrt_logd
            - e_c_fcc_sph
        )

        return {
            "W2_3tree_logD_E0tower": w2_3tree_logd,
            "W2_3tree_logGG_E0tower": w2_3tree_loggg,
            "W2_pauli_triangle_logGG_E0tower": w2_pauli_tri_loggg,
            "W3_FCC_Clique_H3_logD": b_fcc_h3_logd,
            "W3_FCC_Clique_H3_BorD": b_fcc_h3_bord,
            "W3_Kuhn_PauliCore_H4_logD": b_kuhn_pauli_h4_logd,
            "W3_Kuhn_FermiSym_H4_logD": b_kuhn_sym_h4_logd,
            "W3_Kuhn_FermiSym_H4_BorD": b_kuhn_sym_h4_bord,
            "W3_Shell_PauliCore_H4_logD": b_shell_pauli_h4_logd,
            "W3_Shell_HO_Pure_H4_logD": b_shell_ho_pure_h4_logd,
            "W3_Shell_SymHO_FermiSym_H4_logD": b_shell_symho_fermisym_h4_logd,
            "W3_Shell_SymHO_FermiSym_H4_BorD": b_shell_symho_fermisym_h4_bord,
            "W3_Shell_SymHO_FermiSym_H4_DiscC_logD": b_shell_symho_fermisym_h4_discc_logd,
            "W3_Shell_SymHO_FermiSym_H4_AsqrtPair_logD": b_shell_symho_fermisym_h4_asqrt_logd,
            # Component breakdown fields for canonical benchmarks
            "_comp_E_C_legacy_lbond_MeV": e_c_legacy,
            "_comp_E_C_fcc_sph_MeV": e_c_fcc_sph,
            "_comp_E_C_fcc_disc_sym_MeV": e_c_fcc_disc_sym,
            "_comp_Delta_pair_TL_MeV": delta_pair_tl,
            "_comp_Delta_pair_Asqrt_logD_MeV": delta_pair_asqrt_logd,
            "_comp_E_kin_ho_pure_hecke_MeV": e_kin_ho_pure,
            "_comp_E_kin_ho_sym_hecke_MeV": e_kin_ho_sym,
            "_comp_E_so_shift_hecke_MeV": e_so_shift_hecke,
            "_comp_E_so_shift_compton_MeV": e_so_shift_compton,
            "_comp_E_pauli_so_asym_MeV": e_pauli_so_asym,
            "_comp_E_sym_compton_MeV": e_sym_compton,
        }


def _median_mpf(vals: list[mp.mpf]) -> mp.mpf:
    n_cnt = len(vals)
    if n_cnt == 0:
        return mp.mpf(0)
    s_vals = sorted(vals)
    mid = n_cnt // 2
    if n_cnt % 2 == 1:
        return s_vals[mid]
    return (s_vals[mid - 1] + s_vals[mid]) / mp.mpf(2)


def _compute_regime_stats(
    sq_errs: list[mp.mpf],
    abs_errs: list[mp.mpf],
    abs_rel_pcts: list[mp.mpf],
    signed_rel_pcts: list[mp.mpf],
) -> dict[str, str | int]:
    """Compute exact 80-dps `RMSE(B/A)`, `MAE(B/A)`, `median_abs_rel_err_pct`, and `median_signed_rel_err_pct`."""
    n_cnt = len(sq_errs)
    if n_cnt == 0:
        return {
            "count": 0,
            "rmse_BA_MeV": "0",
            "mae_BA_MeV": "0",
            "median_abs_rel_err_pct": "0",
            "median_signed_rel_err_pct": "0",
        }
    with mp.workdps(95):
        n_mp = mp.mpf(n_cnt)
        rmse = mp.sqrt(mp.fsum(sq_errs) / n_mp)
        mae = mp.fsum(abs_errs) / n_mp
        med_abs_rel = _median_mpf(abs_rel_pcts)
        med_signed_rel = _median_mpf(signed_rel_pcts)
        return {
            "count": n_cnt,
            "rmse_BA_MeV": fmt(rmse),
            "mae_BA_MeV": fmt(mae),
            "median_abs_rel_err_pct": fmt(med_abs_rel),
            "median_signed_rel_err_pct": fmt(med_signed_rel),
        }


CANONICAL_6_BENCHMARKS: list[tuple[str, int, int]] = [
    ("4He", 2, 2),
    ("12C", 6, 6),
    ("16O", 8, 8),
    ("56Fe", 26, 30),
    ("208Pb", 82, 126),
    ("238U", 92, 146),
]

HIGHLIGHT_A_VALUES: list[int] = [4, 12, 16, 40, 56, 120, 197, 208, 238]


def main() -> int:
    set_compute_dps(80)
    with mp.workdps(95):
        q_proton = q_at(95)
        q_2t = q_two_term_borromean_at(95)
        q_muon = q_muon_at(95)
        delta_q_2t = q_2t - q_proton

    c_p = _derive_substrate_constants_for_q(q_proton)
    c_2t = _derive_substrate_constants_for_q(q_2t)
    c_m = _derive_substrate_constants_for_q(q_muon)

    # Precompute all 3D simplicial complexes up to max_A = 295 in a single pass
    max_a = 295
    t_3tree_table: list[dict[str, int | bool]] = [
        apollonian_3tree_triangulation(a_i) for a_i in range(max_a + 1)  # type: ignore[misc]
    ]
    t_fcc_table, coulomb_pair_sums = precompute_3d_fcc_clique_and_coulomb(max_a=max_a)
    t_kuhn_table = precompute_3d_kuhn_lattice_balls(max_a=max_a)
    t_shell_table = precompute_3d_close_packed_shell_balls(max_a=max_a)
    shell_tabs = precompute_spectroscopic_shell_tables()
    inv_a13, inv_a12 = precompute_a_powers(max_a=max_a)

    # Load all 3,558 nuclides directly from computations/data/ame2020.json
    nuclides, delta_m_np_ame_mev = load_all_3558_nuclides_from_ame2020()

    wb = WitnessBuilder("nuclear-wave3-periodic-table-synthesis", engine="mpmath")
    wb.set_description(
        "80-dps Wave-3 full periodic table nuclear binding synthesis probe across all "
        "3,558 AME2020 nuclides (Z = 0..118, A = 1..295; 3,556 with A >= 2) loaded "
        "directly from computations/data/ame2020.json, unifying 3D compact-ball "
        "simplicial manifold triangulations (3D FCC nearest-neighbor clique ball, "
        "coordinate-verified 3D Freudenthal-Kuhn lattice ball, and 3D close-packed "
        "Mackay shell ball), H_3 and H_4 GPMT 3-/4-body cumulants, 3D harmonic-oscillator "
        "+ Mayer-Jensen spin-orbit (2j+1) shell closures, Compton Fermi symmetry energy, "
        "proved Temperley-Lieb seniority pairing (tlPairingGap), and 3D FCC proton-pair "
        "Coulomb repulsion (continuum spherical and Lane-N4 isospin-symmetrized discrete "
        "pair sum) across q_0 = q_at(95) (1-term proton pin), q_2t = q_two_term_borromean_at(95) "
        "(2-term Borromean V^3 QED proton pin), and q_muon = q_muon_at(95) (ideal muon pin). "
        "Zero fitted parameters, zero float64 intermediates."
    )
    wb.add_caveat(
        "Branch definitions and anti-double-counting discipline: "
        "(1) Primary Wave-3 branches use the Lean-proved Temperley-Lieb singlet pairing gap "
        "delta_TL_univ = (1/2) * w3_GPMT * [2]_q = E_0 / (2 * [3]_q) = 0.68764544 MeV "
        "(SeniorityPairingAndHoyleTriadThreshold.tlPairingGap); the single secondary branch "
        "W3_Shell_SymHO_FermiSym_H4_AsqrtPair_logD evaluates the empirical-style +/- b_2 / sqrt(A) "
        "scaling for comparison. "
        "(2) To avoid double-counting Pauli isospin asymmetry, W3_Shell_HO_Pure_H4_logD subtracts "
        "only the pure (Z, N) 3D harmonic-oscillator excitation energy E_kin_ho_pure(Z, N) = "
        "(N_osc_pure(Z) + N_osc_pure(N)) * E_0 * A^{-1/3} (with zero extra -E_sym_compton and zero "
        "unproved -3/4 CoM offset), whereas W3_Shell_SymHO_FermiSym_H4_logD/BorD/DiscC subtract the "
        "isospin-symmetric 3D HO baseline E_kin_ho_sym(A) = N_osc_sym(A) * E_0 * A^{-1/3} plus the "
        "parameter-free Compton Fermi symmetry energy E_sym_compton(Z, N) = a_sym * (N - Z)^2 / A. "
        "W3_Kuhn_PauliCore_H4_logD and W3_Shell_PauliCore_H4_logD enforce Pauli isospin balance "
        "combinatorially via the Pauli-capped complex (A_core = 2 * min(Z, N) + D surface triangles) "
        "with zero extra -E_sym_compton subtraction. "
        "(3) W3_Shell_SymHO_FermiSym_H4_DiscC_logD uses the exact Lane-N4 "
        "(SimplicialCoulombGraphMetricDerivation) isospin-symmetrized discrete 3D FCC Coulomb energy "
        "E_C_disc_sym(Z, A) = (alpha * hbar * c / l_bond) * (Z(Z - 1) / (A(A - 1))) * S_FCC(A). "
        "(4) Isobaric beta-stability predictions Z_*(A) use QOU's own parameter-free two-term "
        "nucleon mass splitting (m_n - m_p)_QOU(q) = Q_beta^{N=2,2t}(q) + m_e."
    )

    with mp.workdps(95):
        wb.add_data(
            "substrate_constants_by_anchor",
            {
                "proton_q0": {k: fmt(v) for k, v in c_p.items()},
                "two_term_borromean_q2t": {k: fmt(v) for k, v in c_2t.items()},
                "muon_q0": {k: fmt(v) for k, v in c_m.items()},
                "two_term_borromean_qed_shift_comparison": {
                    "q0_proton_1term": fmt(q_proton),
                    "q2t_two_term_borromean": fmt(q_2t),
                    "delta_q_2t_q2t_minus_q0": fmt(delta_q_2t),
                    "relative_shift_delta_q_2t_over_q0_ppb": fmt((delta_q_2t / q_proton) * mp.mpf(10 ** 9)),
                    "M_p_QED_conn_borromean_V3_at_q2t_MeV": fmt(c_2t["M_p_QED_conn_borromean_V3_MeV"]),
                    "delta_m_np_qou_at_q0_MeV": fmt(c_p["delta_m_np_qou_MeV"]),
                    "delta_m_np_qou_at_q2t_MeV": fmt(c_2t["delta_m_np_qou_MeV"]),
                    "delta_m_np_ame2020_comparator_MeV": fmt(delta_m_np_ame_mev),
                },
            },
        )

    # ── 1. Structural & Topological Verification of 3D Complexes Across A = 4..295 ──
    all_kuhn_valid_4_to_295 = all(
        bool(t_kuhn_table[a_i]["valid_Compact3BallTriangulation"])
        and bool(t_kuhn_table[a_i]["all_cells_canonical_kuhn"])
        for a_i in range(4, max_a + 1)
    )
    all_shell_valid_4_to_295 = all(
        bool(t_shell_table[a_i]["valid_Compact3BallTriangulation"])
        for a_i in range(4, max_a + 1)
    )
    all_3tree_valid_4_to_295 = all(
        verify_compact_3ball_triangulation(t_3tree_table[a_i])  # type: ignore[arg-type]
        for a_i in range(4, max_a + 1)
    )

    triangulation_highlights: list[dict[str, object]] = []
    for a_hi in HIGHLIGHT_A_VALUES:
        t3 = t_3tree_table[a_hi]
        tf = t_fcc_table[a_hi]
        tk = t_kuhn_table[a_hi]
        ts = t_shell_table[a_hi]
        triangulation_highlights.append({
            "A": a_hi,
            "apollonian_3tree": t3,
            "fcc_3d_clique_ball": tf,
            "kuhn_3d_lattice_ball": tk,
            "close_packed_3d_shell_ball": ts,
            "S_FCC_pair_inv_dist_sum": fmt(coulomb_pair_sums[a_hi]),
        })
    wb.add_data("triangulation_table_highlights", triangulation_highlights)

    # ── 2. Full 3,558-Nuclide Synthesis Loop Across Anchors & Mass Regimes ──
    nuclide_by_zn: dict[tuple[int, int], dict[str, object]] = {}
    for nuc in nuclides:
        nuclide_by_zn[(int(nuc["Z"]), int(nuc["N"]))] = nuc

    def _evaluate_full_table_for_anchor(c_anc: dict[str, mp.mpf]) -> dict[str, object]:
        with mp.workdps(95):
            regimes = [
                "all_A_ge_2",
                "light_A_lt_16",
                "medium_16_le_A_lt_100",
                "heavy_100_le_A_lt_200",
                "actinide_A_ge_200",
            ]
            sq_errs: dict[str, dict[str, list[mp.mpf]]] = {
                b_key: {r_key: [] for r_key in regimes} for b_key in BRANCH_KEYS
            }
            abs_errs: dict[str, dict[str, list[mp.mpf]]] = {
                b_key: {r_key: [] for r_key in regimes} for b_key in BRANCH_KEYS
            }
            abs_rel_pcts: dict[str, dict[str, list[mp.mpf]]] = {
                b_key: {r_key: [] for r_key in regimes} for b_key in BRANCH_KEYS
            }
            signed_rel_pcts: dict[str, dict[str, list[mp.mpf]]] = {
                b_key: {r_key: [] for r_key in regimes} for b_key in BRANCH_KEYS
            }

            pred_by_zn: dict[tuple[int, int], dict[str, mp.mpf]] = {}
            isobars: dict[int, list[dict[str, object]]] = {}

            for nuc in nuclides:
                z_val = int(nuc["Z"])
                n_val = int(nuc["N"])
                a_val = int(nuc["A"])
                b_ame = mp.mpf(nuc["B_AME_MeV"])
                ba_ame = mp.mpf(nuc["BA_AME_MeV"])

                br = evaluate_nuclide_branches(
                    z_val=z_val,
                    n_val=n_val,
                    c=c_anc,
                    t_3tree_table=t_3tree_table,
                    t_fcc=t_fcc_table[a_val],
                    t_kuhn_table=t_kuhn_table,
                    t_shell_table=t_shell_table,
                    shell_tabs=shell_tabs,
                    coulomb_pair_sums=coulomb_pair_sums,
                    inv_a13=inv_a13,
                    inv_a12=inv_a12,
                )
                pred_by_zn[(z_val, n_val)] = br

                if a_val not in isobars:
                    isobars[a_val] = []
                isobars[a_val].append({
                    "Z": z_val,
                    "N": n_val,
                    "A": a_val,
                    "B_AME_MeV": b_ame,
                    "branches": br,
                })

                if a_val < 2:
                    continue

                if a_val < 16:
                    r_sub = "light_A_lt_16"
                elif a_val < 100:
                    r_sub = "medium_16_le_A_lt_100"
                elif a_val < 200:
                    r_sub = "heavy_100_le_A_lt_200"
                else:
                    r_sub = "actinide_A_ge_200"

                a_mp = mp.mpf(a_val)
                for b_key in BRANCH_KEYS:
                    b_pred = br[b_key]
                    ba_pred = b_pred / a_mp
                    diff_ba = ba_pred - ba_ame
                    sq_e = diff_ba * diff_ba
                    abs_e = abs(diff_ba)
                    if b_ame > mp.mpf(0):
                        signed_rel_p = ((b_pred - b_ame) / b_ame) * mp.mpf(100)
                        abs_rel_p = abs(signed_rel_p)
                    else:
                        signed_rel_p = mp.mpf(0)
                        abs_rel_p = mp.mpf(0)
                    for r_target in ("all_A_ge_2", r_sub):
                        sq_errs[b_key][r_target].append(sq_e)
                        abs_errs[b_key][r_target].append(abs_e)
                        abs_rel_pcts[b_key][r_target].append(abs_rel_p)
                        signed_rel_pcts[b_key][r_target].append(signed_rel_p)

            regime_summary: dict[str, dict[str, dict[str, str | int]]] = {}
            for b_key in BRANCH_KEYS:
                regime_summary[b_key] = {}
                for r_key in regimes:
                    regime_summary[b_key][r_key] = _compute_regime_stats(
                        sq_errs[b_key][r_key],
                        abs_errs[b_key][r_key],
                        abs_rel_pcts[b_key][r_key],
                        signed_rel_pcts[b_key][r_key],
                    )

            # Canonical 6 benchmark rows
            bench_rows: list[dict[str, object]] = []
            for name, z_b, n_b in CANONICAL_6_BENCHMARKS:
                a_b = z_b + n_b
                nuc_b = nuclide_by_zn[(z_b, n_b)]
                b_ame = mp.mpf(nuc_b["B_AME_MeV"])
                ba_ame = mp.mpf(nuc_b["BA_AME_MeV"])
                br = pred_by_zn[(z_b, n_b)]
                a_mp = mp.mpf(a_b)

                branch_metrics: dict[str, dict[str, str]] = {}
                for b_key in BRANCH_KEYS:
                    bp = br[b_key]
                    delta = bp - b_ame
                    rel_pct = (delta / b_ame) * mp.mpf(100)
                    branch_metrics[b_key] = {
                        "B_pred_MeV": fmt(bp),
                        "BA_pred_MeV": fmt(bp / a_mp),
                        "delta_B_MeV": fmt(delta),
                        "delta_BA_MeV": fmt((bp / a_mp) - ba_ame),
                        "rel_err_pct": fmt(rel_pct),
                    }

                bench_rows.append({
                    "nuclide": name,
                    "Z": z_b,
                    "N": n_b,
                    "A": a_b,
                    "B_AME_MeV": fmt(b_ame),
                    "BA_AME_MeV": fmt(ba_ame),
                    "components_MeV": {
                        "E_C_legacy_lbond_MeV": fmt(br["_comp_E_C_legacy_lbond_MeV"]),
                        "E_C_fcc_sph_MeV": fmt(br["_comp_E_C_fcc_sph_MeV"]),
                        "E_C_fcc_disc_sym_MeV": fmt(br["_comp_E_C_fcc_disc_sym_MeV"]),
                        "Delta_pair_TL_MeV": fmt(br["_comp_Delta_pair_TL_MeV"]),
                        "Delta_pair_Asqrt_logD_MeV": fmt(br["_comp_Delta_pair_Asqrt_logD_MeV"]),
                        "E_kin_ho_pure_hecke_MeV": fmt(br["_comp_E_kin_ho_pure_hecke_MeV"]),
                        "E_kin_ho_sym_hecke_MeV": fmt(br["_comp_E_kin_ho_sym_hecke_MeV"]),
                        "E_so_shift_hecke_MeV": fmt(br["_comp_E_so_shift_hecke_MeV"]),
                        "E_so_shift_compton_MeV": fmt(br["_comp_E_so_shift_compton_MeV"]),
                        "E_pauli_so_asym_MeV": fmt(br["_comp_E_pauli_so_asym_MeV"]),
                        "E_sym_compton_MeV": fmt(br["_comp_E_sym_compton_MeV"]),
                    },
                    "branches": branch_metrics,
                })

            # Isobaric valley of beta-stability Z_*(A) for A = 4..238:
            # Predicted Z_*(A) maximizes B_pred(Z, A-Z) - (N - Z) * (m_n - m_p)_QOU(q_anc);
            # Experimental Z_exp(A) maximizes B_AME(Z, A-Z) - (N - Z) * (m_n - m_p)_AME.
            dm_np_qou = c_anc["delta_m_np_qou_MeV"]
            valley_branches = [
                "W3_Shell_SymHO_FermiSym_H4_logD",
                "W3_Shell_SymHO_FermiSym_H4_BorD",
                "W3_Shell_SymHO_FermiSym_H4_DiscC_logD",
                "W3_Shell_HO_Pure_H4_logD",
                "W3_Kuhn_FermiSym_H4_logD",
                "W3_FCC_Clique_H3_logD",
            ]
            valley_summary: dict[str, object] = {}
            for vb_key in valley_branches:
                abs_dz_list: list[int] = []
                exact_cnt = 0
                within_1_cnt = 0
                within_2_cnt = 0
                sample_isobars: list[dict[str, int]] = []
                for a_iso in range(4, 239):
                    iso_list = isobars.get(a_iso, [])
                    if not iso_list:
                        continue
                    best_exp = max(
                        iso_list,
                        key=lambda item: mp.mpf(item["B_AME_MeV"])
                        - mp.mpf(int(item["N"]) - int(item["Z"])) * delta_m_np_ame_mev,
                    )
                    best_pred = max(
                        iso_list,
                        key=lambda item: item["branches"][vb_key]  # type: ignore[index]
                        - mp.mpf(int(item["N"]) - int(item["Z"])) * dm_np_qou,
                    )
                    z_exp = int(best_exp["Z"])
                    z_pred = int(best_pred["Z"])
                    dz = abs(z_pred - z_exp)
                    abs_dz_list.append(dz)
                    if dz == 0:
                        exact_cnt += 1
                    if dz <= 1:
                        within_1_cnt += 1
                    if dz <= 2:
                        within_2_cnt += 1
                    if a_iso in HIGHLIGHT_A_VALUES:
                        sample_isobars.append({
                            "A": a_iso,
                            "Z_exp_beta_stable": z_exp,
                            "Z_pred_beta_stable": z_pred,
                            "delta_Z": z_pred - z_exp,
                        })
                n_iso = len(abs_dz_list)
                mae_z = mp.mpf(sum(abs_dz_list)) / mp.mpf(n_iso) if n_iso > 0 else mp.mpf(0)
                valley_summary[vb_key] = {
                    "isobar_count_A_4_to_238": n_iso,
                    "delta_m_np_qou_MeV": fmt(dm_np_qou),
                    "mae_abs_delta_Z": fmt(mae_z),
                    "exact_Z_match_count": exact_cnt,
                    "within_1_charge_unit_count": within_1_cnt,
                    "within_2_charge_units_count": within_2_cnt,
                    "within_2_charge_units_fraction": fmt(mp.mpf(within_2_cnt) / mp.mpf(n_iso)),
                    "highlight_isobars": sample_isobars,
                }

            return {
                "regime_summary": regime_summary,
                "canonical_6_benchmarks": bench_rows,
                "isobaric_beta_stability_valley": valley_summary,
                "_pred_by_zn": pred_by_zn,
            }

    eval_p = _evaluate_full_table_for_anchor(c_p)
    eval_2t = _evaluate_full_table_for_anchor(c_2t)
    eval_m = _evaluate_full_table_for_anchor(c_m)

    # ── 3. Magic Separation Energy Jumps Delta_{2n}(N) & Delta_{2p}(Z) ──
    single_n_osc = shell_tabs["single_n_osc"]
    single_two_ls = shell_tabs["single_two_ls"]

    def _magic_shell_gap_row(
        m_magic: int,
        z_rep: int,
        n_rep: int,
        kind: str,
        c_anc: dict[str, mp.mpf],
    ) -> dict[str, object]:
        with mp.workdps(95):
            a_rep = z_rep + n_rep
            ia13_rep = inv_a13[a_rep]
            n_below = single_n_osc[m_magic]
            ls_below = single_two_ls[m_magic]
            n_above = single_n_osc[m_magic + 1]
            ls_above = single_two_ls[m_magic + 1]

            gap_dimless_reeb = mp.mpf(n_above - n_below) - c_anc["kappa_SO_reeb"] * mp.mpf(ls_above - ls_below)
            gap_dimless_q1sq = mp.mpf(n_above - n_below) - c_anc["kappa_SO_q1_sq"] * mp.mpf(ls_above - ls_below)

            delta_2_shell_compton_reeb = mp.mpf(2) * gap_dimless_reeb * c_anc["E_osc_compton_MeV"] * ia13_rep
            delta_2_shell_compton_q1sq = mp.mpf(2) * gap_dimless_q1sq * c_anc["E_osc_compton_MeV"] * ia13_rep
            delta_2_shell_hecke_reeb = mp.mpf(2) * gap_dimless_reeb * c_anc["E0_bare_MeV"] * ia13_rep

            if kind == "neutron":
                b_m2 = mp.mpf(nuclide_by_zn[(z_rep, n_rep - 2)]["B_AME_MeV"])
                b_0 = mp.mpf(nuclide_by_zn[(z_rep, n_rep)]["B_AME_MeV"])
                b_p2 = mp.mpf(nuclide_by_zn[(z_rep, n_rep + 2)]["B_AME_MeV"])
            else:
                b_m2 = mp.mpf(nuclide_by_zn[(z_rep - 2, n_rep)]["B_AME_MeV"])
                b_0 = mp.mpf(nuclide_by_zn[(z_rep, n_rep)]["B_AME_MeV"])
                b_p2 = mp.mpf(nuclide_by_zn[(z_rep + 2, n_rep)]["B_AME_MeV"])
            s2_before_ame = b_0 - b_m2
            s2_after_ame = b_p2 - b_0
            delta_2_ame = s2_before_ame - s2_after_ame

            return {
                "kind": kind,
                "magic_number": m_magic,
                "representative_nuclide": f"{a_rep}{nuclide_by_zn[(z_rep, n_rep)]['symbol']}",
                "Z": z_rep,
                "N": n_rep,
                "A": a_rep,
                "N_osc_below": n_below,
                "two_l_dot_s_below": ls_below,
                "N_osc_above": n_above,
                "two_l_dot_s_above": ls_above,
                "gap_dimless_kappa_reeb": fmt(gap_dimless_reeb),
                "gap_dimless_kappa_q1_sq": fmt(gap_dimless_q1sq),
                "Delta_2_shell_compton_reeb_MeV": fmt(delta_2_shell_compton_reeb),
                "Delta_2_shell_compton_q1_sq_MeV": fmt(delta_2_shell_compton_q1sq),
                "Delta_2_shell_hecke_reeb_MeV": fmt(delta_2_shell_hecke_reeb),
                "S2_before_AME_MeV": fmt(s2_before_ame),
                "S2_after_AME_MeV": fmt(s2_after_ame),
                "Delta_2_AME_MeV": fmt(delta_2_ame),
                "strictly_positive_gap": bool(
                    gap_dimless_reeb > mp.mpf(0) and gap_dimless_q1sq > mp.mpf(0)
                ),
            }

    neutron_magic_reps = [
        (8, 8, 8),       # 16O
        (20, 20, 20),    # 40Ca
        (28, 20, 28),    # 48Ca
        (50, 38, 50),    # 88Sr
        (82, 50, 82),    # 132Sn
        (126, 82, 126),  # 208Pb
    ]
    proton_magic_reps = [
        (8, 8, 8),       # 16O
        (20, 20, 20),    # 40Ca
        (28, 28, 30),    # 58Ni
        (50, 50, 70),    # 120Sn
        (82, 82, 126),   # 208Pb
    ]

    magic_jumps_p: list[dict[str, object]] = []
    for n_mag, z_r, n_r in neutron_magic_reps:
        magic_jumps_p.append(_magic_shell_gap_row(n_mag, z_r, n_r, "neutron", c_p))
    for z_mag, z_r, n_r in proton_magic_reps:
        magic_jumps_p.append(_magic_shell_gap_row(z_mag, z_r, n_r, "proton", c_p))

    wb.add_data(
        "periodic_table_3558_regime_summary",
        {
            "proton_q0": eval_p["regime_summary"],
            "two_term_borromean_q2t": eval_2t["regime_summary"],
            "muon_q0": eval_m["regime_summary"],
        },
    )
    wb.add_data(
        "canonical_6_benchmarks",
        {
            "proton_q0": eval_p["canonical_6_benchmarks"],
            "two_term_borromean_q2t": eval_2t["canonical_6_benchmarks"],
            "muon_q0": eval_m["canonical_6_benchmarks"],
        },
    )
    wb.add_data(
        "isobaric_beta_stability_valley",
        {
            "proton_q0": eval_p["isobaric_beta_stability_valley"],
            "two_term_borromean_q2t": eval_2t["isobaric_beta_stability_valley"],
            "muon_q0": eval_m["isobaric_beta_stability_valley"],
        },
    )
    wb.add_data(
        "magic_separation_energy_jumps",
        {
            "mayer_jensen_magic_closures_verified": shell_tabs["magic_closures"],
            "proton_q0_magic_jumps": magic_jumps_p,
        },
    )

    # ── Console Report ────────────────────────────────────────────────────────
    print("=========================================================================================================================================")
    print("  80-dps Wave-3 Full Periodic Table Nuclear Binding Synthesis Probe (3,558 Nuclides, Zero Fitting, Zero Float64)")
    print("=========================================================================================================================================")
    print(
        f"  Anchors (95-dps): q0 (1-term proton) = {mp.nstr(q_proton, 22)} | "
        f"q2t (2-term Borromean V^3 QED) = {mp.nstr(q_2t, 22)} | "
        f"delta_q_2t = q2t - q0 = +{mp.nstr(delta_q_2t, 12)}"
    )
    print(
        f"  Constants @ q0: E0_bare = {mp.nstr(c_p['E0_bare_MeV'], 8)} MeV | "
        f"b2_log_D = {mp.nstr(c_p['b2_log_D_MeV'], 8)} MeV | "
        f"b2_Bor_D = {mp.nstr(c_p['b2_Bor_D_MeV'], 8)} MeV | "
        f"w3_GPMT = {mp.nstr(c_p['w3_GPMT_MeV'], 8)} MeV | "
        f"w4_H4 = {mp.nstr(c_p['w4_GPMT_H4_MeV'], 8)} MeV | "
        f"delta_TL = {mp.nstr(c_p['delta_TL_univ_MeV'], 8)} MeV"
    )
    print(
        f"  Pauli/SO, Coulomb & (m_n - m_p)_QOU @ q0: E_osc = {mp.nstr(c_p['E_osc_compton_MeV'], 8)} MeV | "
        f"a_sym = {mp.nstr(c_p['a_sym_compton_MeV'], 8)} MeV | "
        f"l_bond = {mp.nstr(c_p['l_bond_fm'], 8)} fm | "
        f"r0_FCC = {mp.nstr(c_p['r0_fcc_fm'], 8)} fm | "
        f"(m_n - m_p)_QOU = {mp.nstr(c_p['delta_m_np_qou_MeV'], 8)} MeV"
    )
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("  1. 6 Canonical Benchmark Nuclei @ q0 (MeV) [W2_3tree_logD vs W3_Kuhn_FermiSym_H4 vs W3_Shell_SymHO_FermiSym_H4 (logD & BorD)]:")
    hdr_b = (
        f"  {'Nucl':<6} {'Z':>3} {'N':>3} {'A':>3} | "
        f"{'B_AME':>9} | {'W2_3t_lD':>9} {'err%':>7} | "
        f"{'W3_Kuhn_lD':>10} {'err%':>7} | "
        f"{'W3_ShSym_lD':>11} {'err%':>7} | "
        f"{'W3_ShSym_BD':>11} {'err%':>7}"
    )
    print(hdr_b)
    print("  " + "-" * (len(hdr_b) - 2))
    for row_b in eval_p["canonical_6_benchmarks"]:  # type: ignore[union-attr]
        brs = row_b["branches"]  # type: ignore[index]
        print(
            f"  {row_b['nuclide']:<6} {row_b['Z']:>3} {row_b['N']:>3} {row_b['A']:>3} | "
            f"{mp.nstr(mp.mpf(row_b['B_AME_MeV']), 6):>9} | "
            f"{mp.nstr(mp.mpf(brs['W2_3tree_logD_E0tower']['B_pred_MeV']), 6):>9} "
            f"{mp.nstr(mp.mpf(brs['W2_3tree_logD_E0tower']['rel_err_pct']), 4):>6}% | "
            f"{mp.nstr(mp.mpf(brs['W3_Kuhn_FermiSym_H4_logD']['B_pred_MeV']), 6):>10} "
            f"{mp.nstr(mp.mpf(brs['W3_Kuhn_FermiSym_H4_logD']['rel_err_pct']), 4):>6}% | "
            f"{mp.nstr(mp.mpf(brs['W3_Shell_SymHO_FermiSym_H4_logD']['B_pred_MeV']), 6):>11} "
            f"{mp.nstr(mp.mpf(brs['W3_Shell_SymHO_FermiSym_H4_logD']['rel_err_pct']), 4):>6}% | "
            f"{mp.nstr(mp.mpf(brs['W3_Shell_SymHO_FermiSym_H4_BorD']['B_pred_MeV']), 6):>11} "
            f"{mp.nstr(mp.mpf(brs['W3_Shell_SymHO_FermiSym_H4_BorD']['rel_err_pct']), 4):>6}%"
        )

    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("  2. Full Periodic Table (3,556 Nuclides with A >= 2) B/A Error Summary @ q0 vs q2t:")
    hdr_s = (
        f"  {'Branch':<43} | "
        f"{'All RMSE':>8} {'All MAE':>8} {'Med|%|':>7} {'Med+-%':>8} | "
        f"{'Light|%|':>8} {'Med|%|':>7} {'Heavy|%|':>8} {'Actin|%|':>8} | "
        f"{'q2t|%|':>7}"
    )
    print(hdr_s)
    print("  " + "-" * (len(hdr_s) - 2))
    reg_p = eval_p["regime_summary"]  # type: ignore[assignment]
    reg_2t = eval_2t["regime_summary"]  # type: ignore[assignment]
    for b_key in BRANCH_KEYS:
        rp = reg_p[b_key]  # type: ignore[index]
        r2 = reg_2t[b_key]  # type: ignore[index]
        print(
            f"  {b_key:<43} | "
            f"{mp.nstr(mp.mpf(rp['all_A_ge_2']['rmse_BA_MeV']), 4):>8} "
            f"{mp.nstr(mp.mpf(rp['all_A_ge_2']['mae_BA_MeV']), 4):>8} "
            f"{mp.nstr(mp.mpf(rp['all_A_ge_2']['median_abs_rel_err_pct']), 4):>6}% "
            f"{mp.nstr(mp.mpf(rp['all_A_ge_2']['median_signed_rel_err_pct']), 4):>7}% | "
            f"{mp.nstr(mp.mpf(rp['light_A_lt_16']['median_abs_rel_err_pct']), 4):>7}% "
            f"{mp.nstr(mp.mpf(rp['medium_16_le_A_lt_100']['median_abs_rel_err_pct']), 4):>6}% "
            f"{mp.nstr(mp.mpf(rp['heavy_100_le_A_lt_200']['median_abs_rel_err_pct']), 4):>7}% "
            f"{mp.nstr(mp.mpf(rp['actinide_A_ge_200']['median_abs_rel_err_pct']), 4):>7}% | "
            f"{mp.nstr(mp.mpf(r2['all_A_ge_2']['median_abs_rel_err_pct']), 4):>6}%"
        )

    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    v_sh_ld = eval_p["isobaric_beta_stability_valley"]["W3_Shell_SymHO_FermiSym_H4_logD"]  # type: ignore[index]
    print(
        f"  3. Isobaric Valley of Beta-Stability (A = 4..238, {v_sh_ld['isobar_count_A_4_to_238']} isobars) "
        f"[W3_Shell_SymHO_FermiSym_H4_logD, QOU (m_n - m_p) = {mp.nstr(mp.mpf(v_sh_ld['delta_m_np_qou_MeV']), 7)} MeV]: "
        f"MAE(|Z_* - Z_exp|) = {mp.nstr(mp.mpf(v_sh_ld['mae_abs_delta_Z']), 4)} | "
        f"within |dZ|<=1: {v_sh_ld['within_1_charge_unit_count']}/{v_sh_ld['isobar_count_A_4_to_238']} | "
        f"within |dZ|<=2: {v_sh_ld['within_2_charge_units_count']}/{v_sh_ld['isobar_count_A_4_to_238']}"
    )

    # ── Purely Structural, Combinatorial & Manifold Assertions (Zero Proximity Gating) ──
    all_magic_gaps_positive = all(bool(row["strictly_positive_gap"]) for row in magic_jumps_p)
    all_3558_loaded = len(nuclides) == 3558
    magic_closures_exact = shell_tabs["magic_closures"] == [2, 8, 20, 28, 50, 82, 126, 184]
    fcc_coulomb_monotone = all(
        coulomb_pair_sums[a_i] < coulomb_pair_sums[a_i + 1]
        for a_i in range(1, max_a)
    )
    borromean_2t_shift_positive = (delta_q_2t > mp.mpf(0)) and (
        c_2t["M_p_QED_conn_borromean_V3_MeV"] > mp.mpf(0)
    )
    qou_np_splitting_positive = (
        c_p["delta_m_np_qou_MeV"] > mp.mpf(0)
        and c_2t["delta_m_np_qou_MeV"] > mp.mpf(0)
        and c_m["delta_m_np_qou_MeV"] > mp.mpf(0)
    )

    wb.add_assertion(
        name="all_3558_ame2020_nuclides_loaded_directly_from_vendored_ame2020_json",
        computed=str(len(nuclides)) if all_3558_loaded else "0",
        expected="3558",
        tolerance="0",
    )
    wb.add_assertion(
        name="kuhn_3d_lattice_balls_and_close_packed_shell_balls_satisfy_Compact3BallTriangulation_A_4_to_295",
        computed="1"
        if (all_kuhn_valid_4_to_295 and all_shell_valid_4_to_295 and all_3tree_valid_4_to_295)
        else "0",
        expected="1",
        tolerance="0",
    )
    wb.add_assertion(
        name="mayer_jensen_spin_orbit_subshells_reproduce_exact_magic_closures_2_8_20_28_50_82_126_184",
        computed="1" if magic_closures_exact else "0",
        expected="1",
        tolerance="0",
    )
    wb.add_assertion(
        name="all_magic_two_nucleon_spin_orbit_shell_gaps_strictly_positive",
        computed="1" if all_magic_gaps_positive else "0",
        expected="1",
        tolerance="0",
    )
    wb.add_assertion(
        name="discrete_3d_fcc_pair_coulomb_sum_strictly_monotone_A_1_to_295",
        computed="1" if fcc_coulomb_monotone else "0",
        expected="1",
        tolerance="0",
    )
    wb.add_assertion(
        name="two_term_borromean_v3_qed_q0_shift_and_qou_np_splitting_positive_and_finite",
        computed="1" if (borromean_2t_shift_positive and qou_np_splitting_positive) else "0",
        expected="1",
        tolerance="0",
    )

    out_path = wb.save(
        q0_comparison(
            muon=q_muon,
            proton=q_proton,
            reason=(
                "Evaluates the Wave-3 3,558-nuclide periodic table nuclear binding "
                "synthesis across the physical proton 1-term pin (q_0 = q_at(95)), the "
                "2-term Borromean V^3 QED proton pin (q_2t = q_two_term_borromean_at(95)), "
                "and the ideal muon pin (q_muon = q_muon_at(95)) for cross-anchor comparison."
            ),
            dps=80,
        )
    )
    print("\n  Saved 80-dps witness -> " + str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
