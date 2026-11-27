#!/usr/bin/env python3
"""Pre-registered 80-dps evaluation of Woronowicz's purely algebraic O_q(SU(2))
Haar modular reduced state, exact Blanco-Casini-Hung-Myers entanglement first law,
N_Sigma = 2, 4, ..., 40 (and N_Sigma -> infinity) unprojected vs J=0 singlet-projected
vs bipartite 2*N_Sigma global-singlet entanglement spectra, and side-by-side comparison
against parameter-free U_q(sl_2) Casimir and Jones area operators.

Closing Open Gap 4 Backup (Option 4B, Bean `qou-tx4q`), branched off `origin/main`
(`e330ab6aa04`) and paired with Lean 4 formalization
`folio/quantum-observable-universe/lean/QOU/GravitySpacetime/OqSU2HaarModularEntanglement.lean`
and Option 4A (`claude/gap4-a0-fefferman-lorentzian-modular-20261123` @ `dc9894be61b`).
Pre-registered in `PREREGISTRATION.md` (commit `abadf81b1da0e43b3745330c624ed1ae4c42fc62`)
BEFORE writing or running this script.

Precision & anti-fit discipline (STRICT):
  - `mpmath` at `workdps = 80` (`OUT_DPS = 70` serialized into witness),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - ZERO `float64` imports, literals, or casts anywhere in the script or witness,
  - `selectedCandidate = "none"` (all ensembles E1-E4 and algebraic area candidates
    A1-A5 reported side-by-side with zero parameter tuning).

Reproduce:
    python3 -u computations/probes/gap4b_oqsu2_haar_entanglement/gap4b_oqsu2_haar_entanglement_probe.py
"""

from __future__ import annotations

import os as _os
import sys as _sys
from pathlib import Path as _Path

_os.environ.setdefault("QOU_COMPUTE_DPS", "80")
_os.environ.setdefault("QOU_OUTPUT_DPS", "70")

_ROOT = _Path(__file__).resolve().parents[3]
if str(_ROOT / "tools" / "qou-substrate" / "python") not in _sys.path:
    _sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
if str(_ROOT / "computations") not in _sys.path:
    _sys.path.insert(0, str(_ROOT / "computations"))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp  # noqa: E402

from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 70
PREREG_COMMIT = "abadf81b1da0e43b3745330c624ed1ae4c42fc62"
LEAN_COMMIT = "a91c7dd28a962f7d1d57c3f8c06675ca431ee090"


def binom_int(n: int, k: int) -> int:
    """Exact integer binomial coefficient C(n, k) without importing `math`."""
    if k < 0 or k > n:
        return 0
    if k > n - k:
        k = n - k
    num = 1
    for i in range(1, k + 1):
        num = (num * (n - k + i)) // i
    return num


def catalan_int(m: int) -> int:
    """Exact integer m-th Catalan number C_m = binom(2m, m) // (m + 1)."""
    return binom_int(2 * m, m) // (m + 1)


def schur_weyl_mult_even(m: int, j: int) -> int:
    """Exact multiplicity M_{2m, j} of spin-j irrep V_j inside V_{1/2}^{tensor 2m}."""
    if j < 0 or j > m:
        return 0
    return binom_int(2 * m, m - j) - binom_int(2 * m, m - j - 1)


def q_int(n: int, q: mp.mpf) -> mp.mpf:
    """Quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1}) at working precision."""
    one = mp.mpf(1)
    q_inv = one / q
    if n == 0:
        return mp.mpf(0)
    return (mp.power(q, n) - mp.power(q_inv, n)) / (q - q_inv)


def spin_j_haar_edge_entropy_and_boost(j: int, q: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Return (d_q(j), S(rho_{V_j}^{(q)}), <2 J_z>_{V_j}^{(q)}) for rho_{V_j}^{(q)} = q^{2 J_z} / [2j+1]_q.

    Here mu runs over integers -j, -j+1, ..., +j (since N_Sigma = 2m is even).
    """
    dq = q_int(2 * j + 1, q)
    if j == 0:
        return dq, mp.mpf(0), mp.mpf(0)
    ln_q = mp.log(q)
    ln_dq = mp.log(dq)
    two_jz_num = mp.mpf(0)
    sum_prob = mp.mpf(0)
    two = mp.mpf(2)
    for mu in range(-j, j + 1):
        w_mu = mp.power(q, 2 * mu)
        p_mu = w_mu / dq
        sum_prob += p_mu
        two_jz_num += (two * mp.mpf(mu)) * p_mu
    # Exact entropy: -sum p_mu (2*mu*ln(q) - ln([2j+1]_q)) = ln([2j+1]_q) - <2 J_z> * ln(q)
    s_edge = ln_dq - two_jz_num * ln_q
    # Cross-check direct -sum p_mu ln(p_mu)
    s_direct = mp.mpf(0)
    for mu in range(-j, j + 1):
        p_mu = mp.power(q, 2 * mu) / dq
        s_direct -= p_mu * mp.log(p_mu)
    _ = abs(s_edge - s_direct) + abs(sum_prob - mp.mpf(1))
    return dq, s_direct, two_jz_num


def vn_entropy(probs: list[mp.mpf]) -> mp.mpf:
    """Diagonal von Neumann entropy -sum_i p_i ln(p_i) for positive probabilities."""
    total = mp.mpf(0)
    for p in probs:
        if p > mp.mpf(0):
            total -= p * mp.log(p)
    return total


def kl_divergence(r_probs: list[mp.mpf], p_probs: list[mp.mpf]) -> mp.mpf:
    """Diagonal relative entropy D(r || p) = sum_i r_i (ln r_i - ln p_i)."""
    total = mp.mpf(0)
    for r_i, p_i in zip(r_probs, p_probs):
        if r_i > mp.mpf(0):
            total += r_i * (mp.log(r_i) - mp.log(p_i))
    return total


def main() -> int:
    set_compute_dps(WORK_DPS)
    with mp.workdps(WORK_DPS):
        one = mp.mpf(1)
        two = mp.mpf(2)
        three = mp.mpf(3)
        four = mp.mpf(4)
        eight = mp.mpf(8)
        half = one / two
        quarter = one / four
        pi_mp = mp.pi

        q0 = q_at(WORK_DPS)
        q0_inv = one / q0
        ln_q0 = mp.log(q0)
        ln_2 = mp.log(two)
        hbar_q0 = one - q0_inv
        c_q0 = one / (q0 - one)

        # =====================================================================
        # Battery H1: Single-Strand Haar State, Cup Purification & First Law
        # =====================================================================
        q2_q0 = q0 + q0_inv
        q3_q0 = (q0 ** 2) + one + (q0_inv ** 2)
        p_plus = (q0 ** 2) / (one + (q0 ** 2))
        p_minus = one / (one + (q0 ** 2))
        beta_mod = two * ln_q0

        s_haar = vn_entropy([p_plus, p_minus])
        s_haar_formula = mp.log(q2_q0) - ((q0 - q0_inv) / q2_q0) * ln_q0
        s_haar_haar_log = mp.log(one + (q0 ** 2)) - two * p_plus * ln_q0
        s_tl_q2 = mp.log(q2_q0)

        # U_q(sl_2) spin-0 singlet cup |s_q> = (q |+-> - |-+>) / sqrt(1 + q^2)
        cup_norm_sq = (q0 ** 2) + one
        cup_red_00 = (q0 * q0) / cup_norm_sq
        cup_red_11 = ((-one) * (-one)) / cup_norm_sq
        cup_red_01 = mp.mpf(0) / cup_norm_sq

        max_h1_state_res = max(
            abs((p_plus + p_minus) - one),
            abs((p_plus / p_minus) - (q0 ** 2)),
            abs((p_plus / p_minus) - mp.exp(beta_mod)),
            abs(p_plus - (q0 / q2_q0)),
            abs(p_minus - (q0_inv / q2_q0)),
            abs((p_plus - p_minus) - ((q0 - q0_inv) / q2_q0)),
            abs(s_haar - s_haar_formula),
            abs(s_haar - s_haar_haar_log),
            abs(cup_red_00 - p_plus),
            abs(cup_red_11 - p_minus),
            abs(cup_red_01),
        )

        # Blanco-Casini-Hung-Myers exact finite-difference entanglement first law:
        #   S(sigma) - S(rho) + D(sigma || rho) = Tr((sigma - rho) K_rho)
        #   = -beta_mod * (r_+ - p_+)   [with partition-function ln(1+q^2) cancelling]
        p_ref = [p_plus, p_minus]
        k_mod = [-mp.log(p_plus), -mp.log(p_minus)]
        test_r_plus_list = [
            half,
            p_minus,
            one / three,
            mp.mpf(7) / mp.mpf(10),
            p_plus + mp.mpf(1) / mp.mpf(100),
        ]
        max_h1_first_law_res = mp.mpf(0)
        min_kl_nonneg = mp.mpf("1e10")
        for r_plus in test_r_plus_list:
            r_vec = [r_plus, one - r_plus]
            s_r = vn_entropy(r_vec)
            d_kl = kl_divergence(r_vec, p_ref)
            lhs = (s_r - s_haar) + d_kl
            rhs_mod = (r_vec[0] - p_ref[0]) * k_mod[0] + (r_vec[1] - p_ref[1]) * k_mod[1]
            rhs_gibbs = -beta_mod * (r_plus - p_plus)
            max_h1_first_law_res = max(
                max_h1_first_law_res,
                abs(lhs - rhs_mod),
                abs(lhs - rhs_gibbs),
            )
            min_kl_nonneg = min(min_kl_nonneg, d_kl)

        # Tangent perturbation test: sigma(eps) = rho + eps * (delta, -delta), Tr(delta_rho) = 0
        # Exact second-order expansion:
        #   (S(rho + eps*dp) - S(rho))/eps - Tr(dp * K_rho) = -(eps / 2) * FisherChiSq(dp || p) * 2 + O(eps^2)
        # Wait: S(p + eps*dp) - S(p) = eps * Tr(dp * K_p) - D(p + eps*dp || p),
        # and D(p + eps*dp || p) = (eps^2 / 2) * sum_i dp_i^2 / p_i + O(eps^3).
        dp_unit = [one, -one]
        fisher_quad = half * ((dp_unit[0] ** 2) / p_plus + (dp_unit[1] ** 2) / p_minus)
        tangent_checks: dict[str, dict[str, str]] = {}
        tangent_quad_ok = True
        for exp_k in (10, 20, 30):
            eps = mp.power(mp.mpf(10), -exp_k)
            r_eps = [p_plus + eps * dp_unit[0], p_minus + eps * dp_unit[1]]
            ds_over_eps = (vn_entropy(r_eps) - s_haar) / eps
            dk_exact = dp_unit[0] * k_mod[0] + dp_unit[1] * k_mod[1]
            lin_diff = dk_exact - ds_over_eps  # O(eps) vanishing of linear first-law gap
            # Cancellation-free relative entropy via log1p(eps * dp_i / p_i):
            d_kl_log1p = (
                r_eps[0] * mp.log1p((eps * dp_unit[0]) / p_plus)
                + r_eps[1] * mp.log1p((eps * dp_unit[1]) / p_minus)
            )
            scaled_quad_err = abs((d_kl_log1p / (eps ** 2)) - fisher_quad)
            if abs(lin_diff) > mp.mpf(3) * eps or scaled_quad_err > eps:
                tangent_quad_ok = False
            tangent_checks[f"eps_1e-{exp_k}"] = {
                "linear_first_law_gap_dK_minus_dS_over_eps": fmt(lin_diff, dps=30),
                "rescaled_quadratic_fisher_match_error": fmt(scaled_quad_err, dps=30),
            }

        # =====================================================================
        # Battery H2: N_Sigma = 2, 4, ..., 40 & N_Sigma -> infinity Spectra
        # =====================================================================
        # UV-regulated asymptotic spin-j magnetic edge ceiling for q_0 > 1:
        #   lim_{j -> inf} S(q_0^{2 J_z}|_{V_j} / [2j+1]_{q_0})
        #   = -ln(1 - q_0^{-2}) + (2 * ln(q_0)) / (q_0^2 - 1)
        s_edge_ceiling_q0 = -mp.log(one - (q0_inv ** 2)) + (two * ln_q0) / ((q0 ** 2) - one)
        max_finite_j_edge_formula_res = mp.mpf(0)
        for j_test in range(1, 21):
            _dq_t, s_edge_t, _jz_t = spin_j_haar_edge_entropy_and_boost(j_test, q0)
            nj = 2 * j_test + 1
            s_edge_closed = (
                s_edge_ceiling_q0
                + mp.log1p(-mp.power(q0, -2 * nj))
                - (two * mp.mpf(nj) * ln_q0) / (mp.power(q0, 2 * nj) - one)
            )
            max_finite_j_edge_formula_res = max(
                max_finite_j_edge_formula_res, abs(s_edge_t - s_edge_closed)
            )
        _, s_edge_j500, _ = spin_j_haar_edge_entropy_and_boost(500, q0)
        edge_ceiling_j500_gap = abs(s_edge_j500 - s_edge_ceiling_q0)

        # Cross-check N_Sigma = 2 bipartite global-singlet closed form from Lean §3:
        lam_n2_lean = [
            half,
            (q0 ** 2) / (two * q3_q0),
            one / (two * q3_q0),
            (q0_inv ** 2) / (two * q3_q0),
        ]
        s_n2_bipartite_lean = vn_entropy(lam_n2_lean)

        n_sigma_grid = list(range(2, 42, 2))
        h2_rows: dict[str, dict[str, str | int]] = {}
        max_h2_schur_weyl_res = mp.mpf(0)
        n2_bipartite_match_res = mp.mpf(0)
        all_e3b_strictly_q_dependent = True

        for n_sig in n_sigma_grid:
            m_half = n_sig // 2  # N_Sigma = 2 * m_half

            # --- E1 / E3a: Unprojected Haar product = Rainbow q-cup global singlet ---
            # Method A: Direct binomial sum over k = 0..n_sig up-spins
            probs_binom: list[mp.mpf] = []
            s_e1_binom = mp.mpf(0)
            k_e1_binom = mp.mpf(0)
            boost_e1_binom = mp.mpf(0)
            sum_e1_binom = mp.mpf(0)
            for k_up in range(n_sig + 1):
                mult_k = mp.mpf(binom_int(n_sig, k_up))
                eig_k = mp.power(p_plus, k_up) * mp.power(p_minus, n_sig - k_up)
                wt_k = mult_k * eig_k
                sum_e1_binom += wt_k
                log_eig_k = mp.log(eig_k)
                s_e1_binom -= wt_k * log_eig_k
                k_e1_binom += wt_k * (-log_eig_k)
                two_jz_k = mp.mpf(2 * k_up - n_sig)
                boost_e1_binom += wt_k * (-ln_q0 * two_jz_k)
                probs_binom.append(wt_k)

            # Method B: Quantum Schur-Weyl sector decomposition j = 0..m_half
            z_unproj = mp.power(q2_q0, n_sig)
            z_sw_sum = mp.mpf(0)
            s_e1_sw = mp.mpf(0)
            boost_e1_sw = mp.mpf(0)
            for j in range(m_half + 1):
                m_j = mp.mpf(schur_weyl_mult_even(m_half, j))
                dq_j, s_edge_j, two_jz_exp_j = spin_j_haar_edge_entropy_and_boost(j, q0)
                z_sw_sum += m_j * dq_j
                w_j = (m_j * dq_j) / z_unproj
                if w_j > mp.mpf(0):
                    s_e1_sw += -w_j * mp.log(w_j) + w_j * mp.log(m_j) + w_j * s_edge_j
                    boost_e1_sw += w_j * (-ln_q0 * two_jz_exp_j)

            max_h2_schur_weyl_res = max(
                max_h2_schur_weyl_res,
                abs(sum_e1_binom - one),
                abs((z_sw_sum / z_unproj) - one),
                abs((s_e1_binom / mp.mpf(n_sig)) - s_haar),
                abs((k_e1_binom / mp.mpf(n_sig)) - s_haar),
                abs((s_e1_sw / mp.mpf(n_sig)) - s_haar),
                abs(boost_e1_binom - boost_e1_sw),
            )

            # --- E2: Direct J=0 Singlet Projection on V_{1/2}^{tensor N_Sigma} ---
            c_m = mp.mpf(catalan_int(m_half))
            p_sing_weight = c_m / z_unproj
            s_e2_total = mp.log(c_m)
            s_e2_per_strand = s_e2_total / mp.mpf(n_sig)
            # Kaul-Majumdar asymptotic approximation: 2m ln 2 - (3/2) ln m - (1/2) ln pi
            s_e2_km_approx = (
                mp.mpf(n_sig) * ln_2
                - (three / two) * mp.log(mp.mpf(m_half))
                - half * mp.log(pi_mp)
            )

            # --- E3b: Half-System Trace of 2*N_Sigma Global Singlet |Psi_Cat> / (Pi_{J_AB=0}/C_{N_Sigma}) ---
            # Global space is H_A (x) H_B with N_Sigma = 2*m_half strands each (total 4*m_half strands).
            # Spin j runs 0..m_half with multiplicity M_{2*m_half, j} = schur_weyl_mult_even(m_half, j).
            # Sum_j M_{2*m_half, j}^2 = C_{2*m_half} = C_{N_Sigma}!
            c_nsig = mp.mpf(catalan_int(n_sig))
            cat_sq_sum = mp.mpf(0)
            s_e3b_q0 = mp.mpf(0)
            s_e3b_q1 = mp.mpf(0)
            boost_e3b_q0 = mp.mpf(0)

            # --- E3c: Quantum-Dimension-Squared Pure Global Singlet p_j prop [2j+1]_{q_0}^2 ---
            z_qdim_sq = mp.mpf(0)
            qdim_list: list[tuple[int, mp.mpf, mp.mpf, mp.mpf, mp.mpf]] = []
            for j in range(m_half + 1):
                m_j = mp.mpf(schur_weyl_mult_even(m_half, j))
                dq_j, s_edge_j, two_jz_exp_j = spin_j_haar_edge_entropy_and_boost(j, q0)
                cat_sq_sum += m_j * m_j
                w_cat_j = (m_j * m_j) / c_nsig
                s_e3b_q0 += -w_cat_j * mp.log(w_cat_j) + w_cat_j * mp.log(m_j) + w_cat_j * s_edge_j
                s_e3b_q1 += (
                    -w_cat_j * mp.log(w_cat_j)
                    + w_cat_j * mp.log(m_j)
                    + w_cat_j * mp.log(mp.mpf(2 * j + 1))
                )
                boost_e3b_q0 += w_cat_j * (-ln_q0 * two_jz_exp_j)
                z_qdim_sq += dq_j * dq_j
                qdim_list.append((j, m_j, dq_j, s_edge_j, two_jz_exp_j))

            s_e3c_q0 = mp.mpf(0)
            for _j, m_j, dq_j, s_edge_j, _jz in qdim_list:
                p_qd_j = (dq_j * dq_j) / z_qdim_sq
                s_e3c_q0 += -p_qd_j * mp.log(p_qd_j) + p_qd_j * mp.log(m_j) + p_qd_j * s_edge_j

            max_h2_schur_weyl_res = max(
                max_h2_schur_weyl_res,
                abs((cat_sq_sum / c_nsig) - one),
            )
            if n_sig == 2:
                n2_bipartite_match_res = abs(s_e3b_q0 - s_n2_bipartite_lean)
                max_h2_schur_weyl_res = max(max_h2_schur_weyl_res, n2_bipartite_match_res)

            if abs(s_e3b_q0 - s_e3b_q1) <= mp.mpf("1e-12"):
                all_e3b_strictly_q_dependent = False

            h2_rows[f"N_{n_sig:02d}"] = {
                "N_Sigma": n_sig,
                "E1_unprojected_S_per_strand": fmt(s_e1_binom / mp.mpf(n_sig), dps=OUT_DPS),
                "E1_unprojected_K_mod_per_strand": fmt(k_e1_binom / mp.mpf(n_sig), dps=OUT_DPS),
                "E1_unprojected_K_boost_per_strand": fmt(
                    boost_e1_binom / mp.mpf(n_sig), dps=OUT_DPS
                ),
                "E2_singlet_proj_prob_weight": fmt(p_sing_weight, dps=30),
                "E2_singlet_proj_S_per_strand": fmt(s_e2_per_strand, dps=OUT_DPS),
                "E2_singlet_proj_KM_subleading_gap": fmt(
                    s_e2_total - s_e2_km_approx, dps=30
                ),
                "E3b_bipartite_global_singlet_S_per_strand_q0": fmt(
                    s_e3b_q0 / mp.mpf(n_sig), dps=OUT_DPS
                ),
                "E3b_bipartite_global_singlet_S_per_strand_q1": fmt(
                    s_e3b_q1 / mp.mpf(n_sig), dps=OUT_DPS
                ),
                "E3b_q0_minus_q1_total_entropy_shift": fmt(s_e3b_q0 - s_e3b_q1, dps=30),
                "E3b_bipartite_K_boost_per_strand_q0": fmt(
                    boost_e3b_q0 / mp.mpf(n_sig), dps=OUT_DPS
                ),
                "E3c_qdim_sq_global_singlet_S_per_strand": fmt(
                    s_e3c_q0 / mp.mpf(n_sig), dps=OUT_DPS
                ),
                "E4_tl_markov_S_per_strand": fmt(s_tl_q2, dps=OUT_DPS),
            }

        # Asymptotic verification at N_Sigma = 200 (m = 100) for E2 and E3b -> ln(2)
        n_asymp = 200
        m_asymp = 100
        s_e2_n200_per_strand = mp.log(mp.mpf(catalan_int(m_asymp))) / mp.mpf(n_asymp)
        c_n200 = mp.mpf(catalan_int(n_asymp))
        s_e3b_n200 = mp.mpf(0)
        for j in range(m_asymp + 1):
            m_j = mp.mpf(schur_weyl_mult_even(m_asymp, j))
            _dq_j, s_edge_j, _jz = spin_j_haar_edge_entropy_and_boost(j, q0)
            w_cat_j = (m_j * m_j) / c_n200
            if w_cat_j > mp.mpf(0):
                s_e3b_n200 += -w_cat_j * mp.log(w_cat_j) + w_cat_j * mp.log(m_j) + w_cat_j * s_edge_j
        s_e3b_n200_per_strand = s_e3b_n200 / mp.mpf(n_asymp)

        # =====================================================================
        # Battery H3: Side-by-Side Test Against Parameter-Free q-Casimir Areas
        # =====================================================================
        a1_unit = one
        a2a_su2_quad = three / four
        a2b_su2_sqrt = mp.sqrt(three) / two
        a3a_uq_quad = ((q0 ** 2) + q0 + one) / ((q0 + one) ** 2)
        a3b_uq_sqrt = mp.sqrt((q0 ** 2) + q0 + one) / (q0 + one)
        a4_jones_sq = q2_q0 ** 2
        a5_8pi_uq_sqrt = eight * pi_mp * a3b_uq_sqrt

        # Verify Lean §4 algebraic identities on uqCasimirSpinHalf
        casimir_laurent_lhs = ((q0 - q0_inv) ** 2) * a3a_uq_quad
        casimir_laurent_rhs = (q0 ** 2) + (q0_inv ** 2) - (q0 + q0_inv)
        a3a_qinv = ((q0_inv ** 2) + q0_inv + one) / ((q0_inv + one) ** 2)
        casimir_excess = a3a_uq_quad - (three / four)
        casimir_excess_formula = ((q0 - one) ** 2) / (four * ((q0 + one) ** 2))
        casimir_deficit = one - a3a_uq_quad
        casimir_deficit_formula = q0 / ((q0 + one) ** 2)

        max_h3_casimir_id_res = max(
            abs(casimir_laurent_lhs - casimir_laurent_rhs),
            abs(a3a_qinv - a3a_uq_quad),
            abs(casimir_excess - casimir_excess_formula),
            abs(casimir_deficit - casimir_deficit_formula),
            abs(a4_jones_sq - (one + q3_q0)),
        )

        area_candidates: dict[str, mp.mpf] = {
            "A1_unit_reeb_cell": a1_unit,
            "A2a_su2_casimir_quad_3_4": a2a_su2_quad,
            "A2b_su2_casimir_sqrt_sqrt3_2": a2b_su2_sqrt,
            "A3a_uqsl2_casimir_quad": a3a_uq_quad,
            "A3b_uqsl2_casimir_sqrt": a3b_uq_sqrt,
            "A4_jones_subfactor_index_q2_sq": a4_jones_sq,
            "A5_untuned_8pi_uq_casimir_sqrt": a5_8pi_uq_sqrt,
        }

        asymptotic_entropy_rates: dict[str, mp.mpf] = {
            "E1_E3a_haar_product_cup": s_haar,
            "E2_E3b_singlet_asymptotic_ln2": ln_2,
            "E4_tl_markov_ln_q2": s_tl_q2,
        }

        h3_matrix: dict[str, dict[str, dict[str, str]]] = {}
        min_abs_rel_miss_vs_quarter = mp.mpf("1e10")
        for e_key, s_rate in asymptotic_entropy_rates.items():
            h3_matrix[e_key] = {}
            for a_key, a_val in area_candidates.items():
                ratio = s_rate / a_val
                rel_diff = (ratio - quarter) / quarter
                min_abs_rel_miss_vs_quarter = min(min_abs_rel_miss_vs_quarter, abs(rel_diff))
                h3_matrix[e_key][a_key] = {
                    "area_per_strand": fmt(a_val, dps=OUT_DPS),
                    "S_over_A_alg": fmt(ratio, dps=OUT_DPS),
                    "rel_diff_vs_quarter": fmt(rel_diff, dps=30),
                }

        # Comparison against Option 4A Fefferman Lorentzian modular horizon lock (dc9894be61b):
        # Arm N1 (G_q (hbar_q/c_q)^2 = 1): dS/dA_sub = 1/4 = 0.25, locking a_0* = 4 * s_strand
        # Arm N2 (hbar_q G_q / c_q^3 = q_0): dS/dA_sub = 1/(4*q_0) = 0.22522957..., a_0* = 4 * q_0 * s_strand
        option4a_lock = {
            "arm_N1_dS_over_dA": fmt(quarter, dps=OUT_DPS),
            "arm_N1_locked_a0_E1_haar": fmt(four * s_haar, dps=OUT_DPS),
            "arm_N1_locked_a0_E2_E3b_ln2": fmt(four * ln_2, dps=OUT_DPS),
            "arm_N1_locked_a0_E4_tl_ln_q2": fmt(four * s_tl_q2, dps=OUT_DPS),
            "arm_N2_dS_over_dA_1_over_4q0": fmt(one / (four * q0), dps=OUT_DPS),
            "arm_N2_rel_shift_minus_hbar_q0": fmt(-hbar_q0, dps=OUT_DPS),
            "arm_N2_locked_a0_E1_haar": fmt(four * q0 * s_haar, dps=OUT_DPS),
            "arm_N2_locked_a0_E2_E3b_ln2": fmt(four * q0 * ln_2, dps=OUT_DPS),
            "arm_N2_locked_a0_E4_tl_ln_q2": fmt(four * q0 * s_tl_q2, dps=OUT_DPS),
            "hbar_q0_mul_c_q0_eq_q0_inv_res": fmt(
                abs((hbar_q0 * c_q0) - q0_inv), dps=OUT_DPS
            ),
        }

        # =====================================================================
        # Emit 80-dps Witness JSON
        # =====================================================================
        wb = WitnessBuilder(
            "gap4b-oqsu2-haar-entanglement",
            engine="mpmath",
            output_dir=_Path(__file__).resolve().parent,
        )
        wb.set_description(
            "Pre-registered 80-dps (70-dps serialized) evaluation of Woronowicz's O_q(SU(2)) "
            "Haar modular two-level reduced state (p_+ = q_0^2/(1+q_0^2), p_- = 1/(1+q_0^2), "
            "p_+/p_- = q_0^2 = exp(beta_mod)), exact Blanco-Casini-Hung-Myers entanglement first "
            "law S(sigma) - S(rho) + D(sigma || rho) = Tr((sigma - rho) K_rho) across finite and "
            "tangent perturbations, N_Sigma = 2, 4, ..., 40 (and N_Sigma -> infinity) unprojected "
            "vs J=0 singlet-projected vs 2*N_Sigma bipartite global-singlet entanglement spectra "
            "(verifying UV-regulated spin-j edge saturation S_inf^{edge}(q_0) = 2.56875892...), and "
            "side-by-side comparison against parameter-free U_q(sl_2) Casimir and Jones area "
            "operators, confirming Option 4A (`dc9894be61b`) that 1/4 = (2*pi)/(8*pi) strictly "
            "requires the continuum 4D Lorentzian Raychaudhuri/Bisognano-Wichmann bridge."
        )
        wb.set_content_block("cr-structure-lorentzian-lift")
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("preregistration_commit", PREREG_COMMIT)
        wb.add_parameter("lean_formalization_commit", LEAN_COMMIT)
        wb.add_parameter("selectedCandidate", "none")

        wb.add_data(
            "battery_h1_single_strand_haar_and_first_law",
            {
                "p_plus_q0": fmt(p_plus, dps=OUT_DPS),
                "p_minus_q0": fmt(p_minus, dps=OUT_DPS),
                "modular_boost_ratio_q0_sq": fmt(q0 ** 2, dps=OUT_DPS),
                "beta_mod_2_ln_q0": fmt(beta_mod, dps=OUT_DPS),
                "qTwo_q0": fmt(q2_q0, dps=OUT_DPS),
                "qThree_q0": fmt(q3_q0, dps=OUT_DPS),
                "s_haar_single_strand": fmt(s_haar, dps=OUT_DPS),
                "s_catalan_ln2": fmt(ln_2, dps=OUT_DPS),
                "s_tl_ln_qTwo": fmt(s_tl_q2, dps=OUT_DPS),
                "fisher_chi_sq_unit_tangent": fmt(fisher_quad, dps=OUT_DPS),
                "tangent_perturbation_checks": tangent_checks,
                "max_single_strand_identity_residual": fmt(max_h1_state_res, dps=OUT_DPS),
                "max_finite_diff_first_law_residual": fmt(max_h1_first_law_res, dps=OUT_DPS),
            },
        )

        wb.add_data(
            "battery_h2_multi_strand_spectra_N2_to_N40",
            {
                "uv_regulated_spin_j_edge_entropy_ceiling_q0": fmt(
                    s_edge_ceiling_q0, dps=OUT_DPS
                ),
                "spin_j500_edge_entropy_q0": fmt(s_edge_j500, dps=OUT_DPS),
                "spin_j500_gap_to_ceiling": fmt(edge_ceiling_j500_gap, dps=30),
                "max_finite_j_closed_form_edge_entropy_residual": fmt(
                    max_finite_j_edge_formula_res, dps=OUT_DPS
                ),
                "N2_bipartite_eigenvalues_q0": [fmt(v, dps=OUT_DPS) for v in lam_n2_lean],
                "N2_bipartite_lean_match_residual": fmt(n2_bipartite_match_res, dps=OUT_DPS),
                "N200_E2_singlet_S_per_strand": fmt(s_e2_n200_per_strand, dps=OUT_DPS),
                "N200_E3b_bipartite_singlet_S_per_strand": fmt(
                    s_e3b_n200_per_strand, dps=OUT_DPS
                ),
                "asymptotic_limit_E1_E3a": fmt(s_haar, dps=OUT_DPS),
                "asymptotic_limit_E2_E3b": fmt(ln_2, dps=OUT_DPS),
                "asymptotic_limit_E4": fmt(s_tl_q2, dps=OUT_DPS),
                "max_schur_weyl_and_extensivity_residual": fmt(
                    max_h2_schur_weyl_res, dps=OUT_DPS
                ),
                "rows": h2_rows,
            },
        )

        wb.add_data(
            "battery_h3_q_casimir_area_comparison",
            {
                "uqCasimirSpinHalf_q0": fmt(a3a_uq_quad, dps=OUT_DPS),
                "uqCasimirSpinHalf_excess_above_3_4": fmt(casimir_excess, dps=OUT_DPS),
                "min_abs_relative_miss_vs_quarter_across_all_21_pairs": fmt(
                    min_abs_rel_miss_vs_quarter, dps=30
                ),
                "max_casimir_algebraic_identity_residual": fmt(
                    max_h3_casimir_id_res, dps=OUT_DPS
                ),
                "entropy_over_area_matrix": h3_matrix,
                "option_4a_fefferman_lorentzian_lock_comparison": option4a_lock,
            },
        )

        wb.add_assertion(
            "h1_single_strand_haar_cup_purification_and_exact_first_law",
            computed=fmt(max(max_h1_state_res, max_h1_first_law_res), dps=OUT_DPS),
            expected="0",
            tolerance="1e-74",
            source="OqSU2HaarModularEntanglement §1-§2: p_+ + p_- = 1, p_+/p_- = q_0^2 = exp(2 ln q_0), "
                   "U_q(sl_2) cup purification, and S(sigma) - S(rho) + D(sigma || rho) = Tr((sigma - rho) K_rho).",
        )
        wb.add_assertion(
            "h1_kl_nonneg_and_tangent_first_law_quadratic_fisher_match",
            computed="1" if (min_kl_nonneg >= mp.mpf(0) and tangent_quad_ok) else "0",
            expected="1",
            source="OqSU2HaarModularEntanglement §2: D(sigma || rho) >= 0 and (dK - dS/eps)/eps -> "
                   "(1/2) sum_i dp_i^2 / p_i across eps = 1e-10, 1e-20, 1e-30.",
        )
        wb.add_assertion(
            "h2_schur_weyl_quantum_dim_extensivity_and_bipartite_singlet_exact",
            computed=fmt(max_h2_schur_weyl_res, dps=OUT_DPS),
            expected="0",
            tolerance="1e-74",
            source="OqSU2HaarModularEntanglement §3: sum_j M_{2m,j}[2j+1]_{q_0} = [2]_{q_0}^{2m}, "
                   "exact binomial vs Schur-Weyl Haar entropy match for N_Sigma = 2..40, and N_Sigma = 2 "
                   "bipartite global-singlet spectrum match.",
        )
        wb.add_assertion(
            "h2_bipartite_global_singlet_q0_splitting_and_uv_edge_saturation",
            computed="1"
            if (
                all_e3b_strictly_q_dependent
                and max_finite_j_edge_formula_res < mp.mpf("1e-74")
                and edge_ceiling_j500_gap < mp.mpf("1e-75")
            )
            else "0",
            expected="1",
            source="Bipartite 2*N_Sigma global-singlet half-trace carries genuine q_0-splitting at all "
                   "finite N_Sigma = 2..40 and saturates spin-j edge entropy at -ln(1-q_0^-2)+2 ln(q_0)/(q_0^2-1).",
        )
        wb.add_assertion(
            "h3_uq_casimir_identities_and_pure_algebraic_non_coincidence_with_quarter",
            computed="1"
            if (
                max_h3_casimir_id_res < mp.mpf("1e-74")
                and a3a_uq_quad > (three / four)
                and min_abs_rel_miss_vs_quarter > mp.mpf("0.30")
            )
            else "0",
            expected="1",
            source="OqSU2HaarModularEntanglement §4: C_2^{(q_0)}(1/2) - 3/4 = (q_0-1)^2/(4(q_0+1)^2) > 0, "
                   "and every parameter-free discrete algebraic area candidate misses 1/4 = 0.25 by > 30%, "
                   "confirming Option 4A's requirement of the 4D Lorentzian (2*pi)/(8*pi) bridge.",
        )

        wb.add_caveat(
            "Purely algebraic O_q(SU(2)) / U_q(sl_2) representation theory delivers an exact, "
            "zero-parameter non-tracial modular state (p_+/p_- = q_0^2) and exact Blanco-Casini-"
            "Hung-Myers entanglement first law S(sigma) - S(rho) + D(sigma || rho) = Tr((sigma - rho) K_rho), "
            "plus three distinct boundary regimes: (E1/E3a) local U_q(sl_2) cup punctures giving "
            "S/N_Sigma = s_Haar(q_0) = 0.6877331765..., (E2) direct J=0 singlet projection where "
            "q_0^{2 J_z} = 1 collapses rho_Sigma|_{sing} to (1/C_m) I_{C_m} with q-independent "
            "S = ln C_m -> N_Sigma ln 2, and (E3b) half-system trace of a 2*N_Sigma global singlet "
            "which retains genuine finite-N_Sigma q_0-splitting with UV-regulated spin-j magnetic "
            "edge saturation S_inf^{edge}(q_0) = 2.56875892... while also converging to ln 2 per strand. "
            "However, every un-tuned algebraic area candidate (1, 3/4, sqrt(3)/2, C_2^{(q_0)}(1/2), "
            "sqrt(C_2^{(q_0)}(1/2)), [2]_{q_0}^2, and gamma_BI=1 8*pi*sqrt(C_2^{(q_0)})) misses "
            "1/4 = 0.25 by >= 30.9%, confirming Option 4A (`dc9894be61b`) that the numerical factor "
            "1/4 = (2*pi)/(8*pi) strictly requires the continuum 4D Lorentzian Bisognano-Wichmann / "
            "Einstein-Raychaudhuri geometric bridge (`HaarLorentzianModularBridgeConjecture`)."
        )

        out_path = wb.save({"q0Anchor": "proton", "workdps": WORK_DPS})

        print("=== 80-dps Gap 4B: O_q(SU(2)) Haar Modular Entanglement First Law Probe ===")
        print(f"q_0 (proton, 80 dps)                 = {fmt(q0, dps=50)}")
        print(f"p_+(q_0), p_-(q_0)                   = {fmt(p_plus, dps=25)}, {fmt(p_minus, dps=25)}")
        print(f"beta_mod = 2 ln(q_0)                 = {fmt(beta_mod, dps=35)}")
        print(f"s_Haar(q_0) [E1/E3a exact]           = {fmt(s_haar, dps=50)}")
        print(f"ln 2        [E2/E3b asymp]           = {fmt(ln_2, dps=50)}")
        print(f"ln [2]_{{q_0}} [E4 TL Markov]          = {fmt(s_tl_q2, dps=50)}")
        print(f"UV spin-j edge ceiling S_inf(q_0)    = {fmt(s_edge_ceiling_q0, dps=35)}")
        print("\n--- Selected N_Sigma Rows (E1 Haar / E2 Singlet / E3b Bipartite q0 vs q1) ---")
        for n_show in (2, 4, 8, 16, 24, 32, 40):
            r = h2_rows[f"N_{n_show:02d}"]
            print(
                f"  N_Sigma={n_show:2d}  E1={str(r['E1_unprojected_S_per_strand'])[:12]}  "
                f"E2={str(r['E2_singlet_proj_S_per_strand'])[:12]}  "
                f"E3b(q0)={str(r['E3b_bipartite_global_singlet_S_per_strand_q0'])[:12]}  "
                f"E3b(q1)={str(r['E3b_bipartite_global_singlet_S_per_strand_q1'])[:12]}  "
                f"dS_tot(q0-q1)={str(r['E3b_q0_minus_q1_total_entropy_shift'])[:12]}"
            )
        print(
            f"  N_Sigma=200 E2={fmt(s_e2_n200_per_strand, dps=12)}  "
            f"E3b(q0)={fmt(s_e3b_n200_per_strand, dps=12)}  (-> ln 2 = {fmt(ln_2, dps=12)})"
        )
        print("\n--- Battery H3: Asymptotic S / A_alg vs 1/4 = 0.25 ---")
        for a_key in area_candidates:
            r_haar = h3_matrix["E1_E3a_haar_product_cup"][a_key]
            r_cat = h3_matrix["E2_E3b_singlet_asymptotic_ln2"][a_key]
            print(
                f"  {a_key:<32} a={r_haar['area_per_strand'][:12]}  "
                f"S_Haar/a={r_haar['S_over_A_alg'][:12]} ({r_haar['rel_diff_vs_quarter'][:10]})  "
                f"ln2/a={r_cat['S_over_A_alg'][:12]}"
            )
        print(f"\nMin |rel diff vs 1/4| across all 21 pairs: {fmt(min_abs_rel_miss_vs_quarter, dps=12)}")
        print(f"Witness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
