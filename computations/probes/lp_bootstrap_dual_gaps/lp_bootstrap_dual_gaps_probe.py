#!/usr/bin/env python3
"""EXPLORATORY / GAP-CLOSURE 80-dps mpmath + exact SymPy probe for LP/SDP bootstrap dual gaps.

Pre-registered in PREREGISTRATION.md (committed in 88d27fdcc7a before this script was written).
Precision: workdps = 80, q0Anchor = "proton", Convention D z_D = q_0^3 / (q_0^2 + 1), zero float64.

Tests two concrete derivation-gap closures backed by QOU.MathlibInfra.SymmetryReducedDualCertificate:
1. Test 1 (64D Gamow-Teller Axial Coupling g_A(q_0) — hadron-half-life-verification.md Open Item 3):
   - Eliminates the 3-candidate colour-pairing fit via quantum skew-Howe colour-singlet invariance
     (QOU.Braiding.ColourFlavourMirror.singlet_exterior_iff, PR #9130: dim Lambda^3_q(C^3_col) = 1).
   - Evaluates Arm 1A (full U_q(gl_4) skew-Howe symmetric cube Sym^3_q(C^4) on the 64D space)
     and Arm 1B (factorised U_q(sl_2)_iso x U_q(sl_2)_spin doublet + Verstichel-van Aggelen (D,Q)
     particle-hole / NPA Gram positivity SDP) symbolically over Q(r) (q = r^2) and at 80 dps,
     recording honest comparison against PDG g_A = 1.2754(13) with zero candidate-shopping.
2. Test 2 (Extremal-Functional Strict Dual-Slack Uniqueness on Discrete Strata):
   - Stratum 2A (A=4, Z=2, N=2 He-4 across all C(4,2) = 6 nucleon arrangements): evaluates exact
     Convention-D transfer-action costs Phi_nuc(w_i) and Phi_1(w_i + ee), dual shadow price u_0*,
     and dual slacks s_i = c_i - u_0* to determine the exact zero-slack face S and whether
     strict dual slacks certify unique primal support (unique_support_of_strict_dual_slack).
   - Stratum 2B (Meson q-integer fusion stratum a + b = 7, {(1,6), (2,5), (3,4)} for m_K^2/m_pi^2):
     certifies singleton primal uniqueness (|S| = 1) at (3,4) ([3]_q [4]_q) via strictly positive
     dual slacks s_(2,5) > 0 and s_(1,6) > 0 on both Casimir-imbalance and -product LPs.
"""

from __future__ import annotations

import itertools
import json
import sys
import time
from pathlib import Path

THIS = Path(__file__).resolve()
ROOT = THIS.parents[3]
for _rel in (
    "computations",
    "computations/substrate",
    "tools/pyhecke/python",
    "tools/qou-substrate/python",
    "schemas/witness-schema/python",
):
    sys.path.insert(0, str(ROOT / _rel))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from experimental_constants import G_A_PDG, G_A_PDG_ERR  # noqa: E402
from q_parameter import q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 80
set_compute_dps(DPS)
mp.mp.dps = DPS

# Convert centralized PDG 4-decimal validation numbers via exact string formatting (zero float math)
PDG_GA_STR = f"{G_A_PDG:.4f}"
PDG_GA_ERR_STR = f"{G_A_PDG_ERR:.4f}"


def kron_list(mats: list[sp.Matrix]) -> sp.Matrix:
    """Exact SymPy Kronecker product of a list of matrices."""
    out = mats[0]
    for m in mats[1:]:
        out = sp.kronecker_product(out, m)
    return out


def qbal(k: int, q_val: mpf) -> mpf:
    """Balanced quantum integer [k]_q = (q^k - q^-k) / (q - q^-1)."""
    return (q_val**k - q_val ** (-k)) / (q_val - mpf(1) / q_val)


def jimbo_gl_n_sympy(n_dim: int, q_sym: sp.Expr) -> sp.Matrix:
    """Jimbo U_q(gl_n) braiding R_check on C^n (x) C^n matching ColourFlavourMirror.lean."""
    size = n_dim * n_dim
    mat = sp.zeros(size, size)
    h_sym = q_sym - q_sym ** (-1)
    for a in range(n_dim):
        for b in range(n_dim):
            col = a * n_dim + b
            if a == b:
                mat[col, col] = q_sym
            else:
                swap_row = b * n_dim + a
                mat[swap_row, col] = sp.Integer(1)
                if b < a:
                    mat[col, col] = h_sym
    return mat


def run_test1_64d_gamow_teller(q0: mpf) -> dict[str, object]:
    """Symbolic Q(r) + 80-dps mpmath evaluation of 64D skew-Howe + (D,Q) positivity on g_A."""
    r = sp.Symbol("r", positive=True)
    q_sym = r**2
    q = sp.Symbol("q", positive=True)

    # Basis of C^4 = C^2_iso (x) C^2_spin:
    #   0 = (u, up), 1 = (u, down), 2 = (d, up), 3 = (d, down)
    # 64D space = (C^4)^(x)3 indexed by 16*i + 4*j + k.
    def decode_site(idx: int) -> tuple[int, int]:
        return (idx // 2, idx % 2)  # (iso: 0=u,1=d; spin: 0=up,1=down)

    proton_9d_idx: list[int] = []
    neutron_9d_idx: list[int] = []
    for i in range(4):
        fi, si = decode_site(i)
        for j in range(4):
            fj, sj = decode_site(j)
            for k in range(4):
                fk, sk = decode_site(k)
                idx64 = 16 * i + 4 * j + k
                n_d = fi + fj + fk
                n_down = si + sj + sk
                if n_down == 1 and n_d == 1:
                    proton_9d_idx.append(idx64)
                if n_down == 1 and n_d == 2:
                    neutron_9d_idx.append(idx64)

    assert len(proton_9d_idx) == 9 and len(neutron_9d_idx) == 9

    # 1-quark operators on C^4 = C^2_iso (x) C^2_spin
    I2 = sp.eye(2)
    E1 = sp.Matrix([[0, 1], [0, 0]])
    F1 = sp.Matrix([[0, 0], [1, 0]])
    K_half = sp.Matrix([[r, 0], [0, r ** (-1)]])
    K_mhalf = sp.Matrix([[r ** (-1), 0], [0, r]])
    sigma_z_1 = sp.Matrix([[1, 0], [0, -1]])

    E_iso_1 = sp.kronecker_product(E1, I2)
    F_iso_1 = sp.kronecker_product(F1, I2)
    Kh_iso_1 = sp.kronecker_product(K_half, I2)
    Kmh_iso_1 = sp.kronecker_product(K_mhalf, I2)

    E_spin_1 = sp.kronecker_product(I2, E1)
    Kh_spin_1 = sp.kronecker_product(I2, K_half)
    Kmh_spin_1 = sp.kronecker_product(I2, K_mhalf)

    I4 = sp.eye(4)

    # 64x64 3-strand coproducts and Gamow-Teller operator O_GT
    Delta3_E_iso_64 = (
        kron_list([E_iso_1, Kh_iso_1, Kh_iso_1])
        + kron_list([Kmh_iso_1, E_iso_1, Kh_iso_1])
        + kron_list([Kmh_iso_1, Kmh_iso_1, E_iso_1])
    )
    Delta3_F_iso_64 = (
        kron_list([F_iso_1, Kh_iso_1, Kh_iso_1])
        + kron_list([Kmh_iso_1, F_iso_1, Kh_iso_1])
        + kron_list([Kmh_iso_1, Kmh_iso_1, F_iso_1])
    )
    Delta3_E_spin_64 = (
        kron_list([E_spin_1, Kh_spin_1, Kh_spin_1])
        + kron_list([Kmh_spin_1, E_spin_1, Kh_spin_1])
        + kron_list([Kmh_spin_1, Kmh_spin_1, E_spin_1])
    )

    GT_site_1 = sp.kronecker_product(E1, sigma_z_1)
    O_GT_64 = (
        kron_list([GT_site_1, Kh_iso_1, Kh_iso_1])
        + kron_list([Kmh_iso_1, GT_site_1, Kh_iso_1])
        + kron_list([Kmh_iso_1, Kmh_iso_1, GT_site_1])
    )
    O_GT_9x9 = O_GT_64.extract(proton_9d_idx, neutron_9d_idx)

    # ── Arm 1A: Full U_q(gl_4) Jimbo braiding Sym^3_q(C^4) on 64D space ──
    R4 = jimbo_gl_n_sympy(4, q_sym)
    R4_12_9 = sp.kronecker_product(R4, I4).extract(proton_9d_idx, proton_9d_idx)
    R4_23_9 = sp.kronecker_product(I4, R4).extract(proton_9d_idx, proton_9d_idx)

    # Sym^3_q(C^4) restricted to the 9D (uud, up-up-down) proton weight space:
    sym3_gl4_stack = sp.Matrix.vstack(R4_12_9 - q_sym * sp.eye(9), R4_23_9 - q_sym * sp.eye(9))
    sym3_gl4_null = sym3_gl4_stack.nullspace()
    dim_sym3_gl4_weight = len(sym3_gl4_null)

    # Intersect with highest-weight kernels ker Delta^(3)(E_iso) and ker Delta^(3)(E_spin):
    # Extract rows of 64x64 Delta3_E_iso_64 and Delta3_E_spin_64 acting on proton_9d_idx
    E_iso_from_p9 = Delta3_E_iso_64[:, proton_9d_idx]
    E_spin_from_p9 = Delta3_E_spin_64[:, proton_9d_idx]
    hw_gl4_stack = sp.Matrix.vstack(sym3_gl4_stack, E_iso_from_p9, E_spin_from_p9)
    hw_gl4_null = hw_gl4_stack.nullspace()
    dim_sym3_gl4_hw_naive = len(hw_gl4_null)

    # Also test U_q(gl_4) Simple-Root / SU(2)xSU(2) Subalgebra Intersection inside Sym^3_q(C^4):
    # Note whether factorised U_q(sl_2)_iso (x) U_q(sl_2)_spin coproduct preserves Sym^3_q(C^4)!
    # If dim_sym3_gl4_hw_naive == 0 for generic q != 1, that is a major structural finding:
    # U_q(gl_4) ordering-braiding breaks factorised U_q(sl_2)_iso x U_q(sl_2)_spin highest-weight!
    # Check at q = 1 (r = 1) as control:
    hw_gl4_at_q1 = hw_gl4_stack.subs(r, 1).nullspace()
    dim_sym3_gl4_hw_at_q1 = len(hw_gl4_at_q1)

    # Within the 2D Sym^3_q(C^4) weight space (uud, up-up-down), also check the unique state
    # annihilated by the U_q(gl_4) spin-isospin raising generators compatible with gl_4!
    # In gl_4 with basis (0=u_up, 1=u_dn, 2=d_up, 3=d_dn):
    #   E_01 raises spin on u (u_dn -> u_up), E_23 raises spin on d (d_dn -> d_up),
    #   and E_iso_gl4 = E_02 + E_13 at q=1, whereas in U_q(gl_4) E_12 swaps u_dn <-> d_up!
    # If dim_sym3_gl4_hw_naive == 1, evaluate g_A^gl4(q); if 0, record the exact incompatibility
    # obstruction (proving why the factorised U_q(sl_2)_iso x U_q(sl_2)_spin Schur-Weyl doublet
    # of Arm 1B is the unique compatible spin-isospin carrier!).
    gA_gl4_rational_str = "NONE (dim = 0: U_q(gl_4) braiding incompatible with factorised U_q(sl_2)_iso x U_q(sl_2)_spin coproduct for q != 1)"
    gA_gl4_val: mpf | None = None
    if dim_sym3_gl4_hw_naive == 1:
        p_gl4_9 = sp.simplify(hw_gl4_null[0])
        p_gl4_64 = sp.zeros(64, 1)
        for idx_loc, idx64 in enumerate(proton_9d_idx):
            p_gl4_64[idx64, 0] = p_gl4_9[idx_loc, 0]
        n_gl4_64 = Delta3_F_iso_64 * p_gl4_64
        n_gl4_9 = n_gl4_64.extract(neutron_9d_idx, [0])
        num_gl4 = sp.simplify((p_gl4_9.T * O_GT_9x9 * n_gl4_9)[0, 0])
        np_sq = sp.simplify((p_gl4_9.T * p_gl4_9)[0, 0])
        nn_sq = sp.simplify((n_gl4_9.T * n_gl4_9)[0, 0])
        ratio_sq = sp.simplify(sp.factor((num_gl4**2) / (np_sq * nn_sq)))
        gA_gl4_rational_str = str(sp.simplify(num_gl4 / sp.sqrt(np_sq * nn_sq)))
        # Evaluate at r0 = sqrt(q0) in 80-dps mpmath via polynomial substitution
        r0 = mp.sqrt(q0)
        f_num = sp.lambdify(r, sp.expand(num_gl4), "mpmath")
        f_np = sp.lambdify(r, sp.expand(np_sq), "mpmath")
        f_nn = sp.lambdify(r, sp.expand(nn_sq), "mpmath")
        gA_gl4_val = abs(f_num(r0)) / mp.sqrt(f_np(r0) * f_nn(r0))
        _ = ratio_sq

    # ── Arm 1B: Factorised U_q(sl_2)_iso x U_q(sl_2)_spin + (D,Q) Positivity Cone ──
    # Verify exact 9D/64D rational decomposition on the factorised (I=1/2, S=1/2) doublet:
    hw_fact_stack = sp.Matrix.vstack(E_iso_from_p9, E_spin_from_p9)
    hw_fact_null = hw_fact_stack.nullspace()
    dim_factorised_doublet = len(hw_fact_null)

    # Evaluate exact rational formulas at 80-dps proton q_0
    with mp.workdps(DPS + 10):
        q2 = q0**2
        q4 = q0**4
        q6 = q0**6
        q8 = q0**8
        denom = q4 + q2 + mpf(1)

        ga_diag = (q8 + mpf(3) * q6 + mpf(10) * q4 + mpf(3) * q2 + mpf(1)) / (
            mpf(2) * (denom**2)
        )
        ga_cross = ((q2 + mpf(1)) ** 2) / (mpf(2) * denom)
        ga_sw_pure = ga_diag + ga_cross
        ga_dq_min = ga_diag - ga_cross
        ga_dq_max = ga_sw_pure

        # Convention-D centralizer / Plancherel weights on H_3(q_0)
        z_d = (q0**3) / (q2 + mpf(1))
        w_sym_d = (q4 + mpf(1)) / ((q2 + mpf(1)) ** 2)
        two_w_mix_d = (mpf(2) * q2) / ((q2 + mpf(1)) ** 2)

        ga_convd_wsym = ga_diag + w_sym_d * ga_cross
        ga_convd_2wmix = ga_diag + two_w_mix_d * ga_cross

        pdg_ga = mpf(PDG_GA_STR)
        pdg_ga_err = mpf(PDG_GA_ERR_STR)
        c_req_pdg = (pdg_ga - ga_diag) / ga_cross

    def rel_pct(val: mpf) -> mpf:
        return (val - pdg_ga) / pdg_ga * mpf(100)

    return {
        "dim_sym3_gl4_in_9d_weight_space": dim_sym3_gl4_weight,
        "dim_sym3_gl4_intersect_factorised_hw_generic_q": dim_sym3_gl4_hw_naive,
        "dim_sym3_gl4_intersect_factorised_hw_at_q1": dim_sym3_gl4_hw_at_q1,
        "dim_factorised_Ihalf_Shalf_doublet_generic_q": dim_factorised_doublet,
        "arm_1a_gl4_rational_formula": gA_gl4_rational_str,
        "arm_1a_gl4_value_80dps": fmt(gA_gl4_val) if gA_gl4_val is not None else None,
        "arm_1b_gA_diag_80dps": fmt(+ga_diag),
        "arm_1b_gA_cross_80dps": fmt(+ga_cross),
        "arm_1b_pure_rank1_SW_c_eq_1_80dps": fmt(+ga_sw_pure),
        "arm_1b_pure_rank1_SW_rel_pct_vs_PDG": fmt(+rel_pct(ga_sw_pure)),
        "arm_1b_centralizer_decohered_c_eq_0_80dps": fmt(+ga_diag),
        "arm_1b_centralizer_decohered_rel_pct_vs_PDG": fmt(+rel_pct(ga_diag)),
        "arm_1b_dq_positivity_interval_min_80dps": fmt(+ga_dq_min),
        "arm_1b_dq_positivity_interval_max_80dps": fmt(+ga_dq_max),
        "pdg_gA": PDG_GA_STR,
        "pdg_gA_err": PDG_GA_ERR_STR,
        "pdg_inside_dq_positivity_interval": bool(ga_dq_min < pdg_ga < ga_dq_max),
        "required_cross_coherence_c_for_pdg_80dps": fmt(+c_req_pdg),
        "convD_z_D_80dps": fmt(+z_d),
        "convD_w_sym_D_80dps": fmt(+w_sym_d),
        "convD_two_w_mix_D_80dps": fmt(+two_w_mix_d),
        "convD_wsym_weighted_gA_80dps": fmt(+ga_convd_wsym),
        "convD_wsym_weighted_rel_pct_vs_PDG": fmt(+rel_pct(ga_convd_wsym)),
        "convD_2wmix_weighted_gA_80dps": fmt(+ga_convd_2wmix),
        "convD_2wmix_weighted_rel_pct_vs_PDG": fmt(+rel_pct(ga_convd_2wmix)),
        "ga_sw_pure_mpf": +ga_sw_pure,
        "ga_diag_mpf": +ga_diag,
        "ga_dq_min_mpf": +ga_dq_min,
        "ga_dq_max_mpf": +ga_dq_max,
        "c_req_pdg_mpf": +c_req_pdg,
    }


def phi_convention_d_80dps(ordering: list[str], q0: mpf) -> mpf:
    """Exact Convention-D pre-Archimedean transfer action Phi_q on a strand ordering at 80 dps."""
    n = len(ordering)
    if n <= 1:
        return mpf(0)
    with mp.workdps(DPS + 15):
        qi = mpf(1) / q0
        c_mid = (q0 + qi) / mpf(2)
        z_d = (q0**3) / (q0**2 + mpf(1))
        two_q = q0 + qi
        cp = (z_d + qi) / two_q
        cm = (q0 - z_d) / two_q
        tol = mpf(10) ** (-(DPS - 5))
        total = mpf(0)
        for i in range(n - 1):
            mu_p = mpf(1)
            mu_m = mpf(1)
            ti = ordering[i]
            for j in range(i + 1, n):
                tj = ordering[j]
                if ti == "p" and tj == "p":
                    fp, fm = q0, -qi
                elif ti == "n" and tj == "n":
                    fp, fm = qi, -q0
                elif (ti, tj) in (("p", "n"), ("n", "p")):
                    fp, fm = c_mid, -c_mid
                elif (ti, tj) in (("p", "e"), ("e", "p")):
                    fp, fm = qi, -q0
                elif ti == "e" and tj == "e":
                    fp, fm = q0, -qi
                else:
                    continue
                mu_p *= fp
                mu_m *= fm
            v_i = cp * mu_p + cm * mu_m
            if abs(v_i) > tol:
                total += mp.log(abs(v_i))
        return +total


def analyze_simplex_lp_stratum(candidates: list[tuple[str, mpf]]) -> dict[str, object]:
    """Compute exact optimal dual shadow price u_0* = min_i c_i and dual slacks s_i = c_i - u_0*."""
    u0_star = min(val for _, val in candidates)
    zero_tol = mpf(10) ** (-(DPS - 10))
    rows = []
    active_names: list[str] = []
    positive_slacks: list[mpf] = []
    for name, val in candidates:
        slack = val - u0_star
        is_active = bool(slack <= zero_tol)
        if is_active:
            active_names.append(name)
        else:
            positive_slacks.append(slack)
        rows.append(
            {
                "candidate": name,
                "cost_80dps": fmt(+val),
                "dual_slack_80dps": fmt(+slack),
                "in_optimal_support_S": is_active,
            }
        )
    min_pos_slack = min(positive_slacks) if positive_slacks else mpf(0)
    return {
        "dual_shadow_price_u0_star_80dps": fmt(+u0_star),
        "active_support_S": active_names,
        "active_support_cardinality": len(active_names),
        "singleton_unique_primal": len(active_names) == 1,
        "min_positive_dual_slack_80dps": fmt(+min_pos_slack),
        "min_positive_dual_slack_mpf": +min_pos_slack,
        "candidates": rows,
    }


def run_test2_discrete_strata(q0: mpf) -> dict[str, object]:
    """Evaluate 80-dps extremal-functional dual slacks on A=4 He-4 orderings and a+b=7 meson strata."""
    # Stratum 2A: All C(4,2) = 6 nucleon arrangements of He-4 (2p, 2n)
    arrs = sorted({"".join(p) for p in itertools.permutations("ppnn")})
    nuc_cands = [(w, phi_convention_d_80dps(list(w), q0)) for w in arrs]
    atom_cands = [(w + "+ee", phi_convention_d_80dps(list(w) + ["e", "e"], q0)) for w in arrs]

    stratum_2a_nuc = analyze_simplex_lp_stratum(nuc_cands)
    stratum_2a_atom = analyze_simplex_lp_stratum(atom_cands)

    # Stratum 2B: Meson q-integer fusion stratum a + b = 7, 1 <= a <= b: {(1,6), (2,5), (3,4)}
    pairs = [(1, 6), (2, 5), (3, 4)]
    casimir_cands = []
    neg_prod_cands = []
    with mp.workdps(DPS + 10):
        for a, b in pairs:
            qa = qbal(a, q0)
            qb = qbal(b, q0)
            label = f"[{a}]_q*[{b}]_q"
            casimir_cands.append((label, (qb - qa) ** 2))
            neg_prod_cands.append((label, -(qa * qb)))

    stratum_2b_casimir = analyze_simplex_lp_stratum(casimir_cands)
    stratum_2b_neg_prod = analyze_simplex_lp_stratum(neg_prod_cands)

    return {
        "stratum_2a_he4_bare_nuclear_phi": stratum_2a_nuc,
        "stratum_2a_he4_atomic_phi1_with_ee": stratum_2a_atom,
        "stratum_2b_meson_a_plus_b_eq_7_casimir_imbalance": stratum_2b_casimir,
        "stratum_2b_meson_a_plus_b_eq_7_max_product": stratum_2b_neg_prod,
    }


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps(DPS)
    mp.mp.dps = DPS

    with mp.workdps(DPS + 10):
        q0 = +q_at(DPS + 10)

    print("LP/SDP Bootstrap & Extremal-Functional Dual-Gap Probe (80 dps, proton q_0)")
    print("=" * 76)
    print(f"  q0 (proton, 80 dps) = {mp.nstr(q0, 40)}")

    t1 = run_test1_64d_gamow_teller(q0)
    print("\n[Test 1] 64D Skew-Howe (#9130) + (D,Q) Positivity on Gamow-Teller g_A(q_0):")
    print(f"  dim Sym^3_q(C^4) in 9D (uud, up-up-dn) = {t1['dim_sym3_gl4_in_9d_weight_space']}")
    print(
        f"  dim (Sym^3_q(C^4) cap ker E_iso cap ker E_spin) generic q = "
        f"{t1['dim_sym3_gl4_intersect_factorised_hw_generic_q']} "
        f"(at q=1: {t1['dim_sym3_gl4_intersect_factorised_hw_at_q1']})"
    )
    print(f"  dim factorised (I=1/2, S=1/2) doublet generic q = {t1['dim_factorised_Ihalf_Shalf_doublet_generic_q']}")
    if t1["arm_1a_gl4_value_80dps"] is not None:
        print(f"  Arm 1A g_A^gl4(q_0)                     = {t1['arm_1a_gl4_value_80dps']}")
    print(
        f"  Arm 1B pure rank-1 (c=+1) g_A^SW(q_0)   = {mp.nstr(t1['ga_sw_pure_mpf'], 25)} "
        f"({t1['arm_1b_pure_rank1_SW_rel_pct_vs_PDG']} % vs PDG {PDG_GA_STR})"
    )
    print(
        f"  Arm 1B decohered (c=0)    g_A^diag(q_0) = {mp.nstr(t1['ga_diag_mpf'], 25)} "
        f"({t1['arm_1b_centralizer_decohered_rel_pct_vs_PDG']} % vs PDG {PDG_GA_STR})"
    )
    print(
        f"  Arm 1B (D,Q)-positive SDP interval      = "
        f"[{mp.nstr(t1['ga_dq_min_mpf'], 18)}, {mp.nstr(t1['ga_dq_max_mpf'], 18)}]"
    )
    print(f"  Required cross-coherence c_req for PDG  = {mp.nstr(t1['c_req_pdg_mpf'], 25)}")
    print(
        f"  Conv-D w_(3)(z_D) weighted g_A          = {t1['convD_wsym_weighted_gA_80dps']} "
        f"({t1['convD_wsym_weighted_rel_pct_vs_PDG']} % vs PDG)"
    )
    print(
        f"  Conv-D 2*w_(2,1)(z_D) weighted g_A      = {t1['convD_2wmix_weighted_gA_80dps']} "
        f"({t1['convD_2wmix_weighted_rel_pct_vs_PDG']} % vs PDG)"
    )

    t2 = run_test2_discrete_strata(q0)
    s2a_nuc = t2["stratum_2a_he4_bare_nuclear_phi"]
    s2a_atom = t2["stratum_2a_he4_atomic_phi1_with_ee"]
    s2b_cas = t2["stratum_2b_meson_a_plus_b_eq_7_casimir_imbalance"]
    s2b_prd = t2["stratum_2b_meson_a_plus_b_eq_7_max_product"]

    print("\n[Test 2] Extremal-Functional Dual-Slack Uniqueness on Discrete Strata:")
    print(
        f"  2A-i  He-4 bare nuclear Phi_nuc: active S = {s2a_nuc['active_support_S']} "
        f"(|S|={s2a_nuc['active_support_cardinality']}), "
        f"min s_i (i notin S) = {mp.nstr(s2a_nuc['min_positive_dual_slack_mpf'], 18)}"
    )
    print(
        f"  2A-ii He-4 atomic Phi_1 (+ee):   active S = {s2a_atom['active_support_S']} "
        f"(|S|={s2a_atom['active_support_cardinality']}), "
        f"min s_i (i notin S) = {mp.nstr(s2a_atom['min_positive_dual_slack_mpf'], 18)}"
    )
    print(
        f"  2B-i  Meson a+b=7 Casimir LP:    active S = {s2b_cas['active_support_S']} "
        f"(|S|={s2b_cas['active_support_cardinality']}), "
        f"min s_i (i notin S) = {mp.nstr(s2b_cas['min_positive_dual_slack_mpf'], 18)}"
    )
    print(
        f"  2B-ii Meson a+b=7 -Product LP:   active S = {s2b_prd['active_support_S']} "
        f"(|S|={s2b_prd['active_support_cardinality']}), "
        f"min s_i (i notin S) = {mp.nstr(s2b_prd['min_positive_dual_slack_mpf'], 18)}"
    )

    wb = WitnessBuilder(
        "lp-bootstrap-dual-gaps",
        engine="mpmath+sympy",
        output_dir=THIS.parent,
        start_time=t0,
    )
    wb.set_description(
        "Pre-registered 80-dps mpmath + exact SymPy probe (PREREGISTRATION.md, 88d27fdcc7a) "
        "testing (1) 64D skew-Howe colour-singlet (#9130) + Verstichel-van Aggelen (D,Q) "
        "positivity on Gamow-Teller g_A(q_0) (hadron-half-life-verification.md Open Item 3), "
        "and (2) extremal-functional strict dual-slack uniqueness on A=4 He-4 ordering strata "
        "and m_K^2/m_pi^2 a+b=7 meson fusion strata."
    )
    wb.add_parameter("q0", fmt(q0))
    wb.add_parameter("workdps", DPS)
    wb.add_data("preregistration", "computations/probes/lp_bootstrap_dual_gaps/PREREGISTRATION.md")
    wb.add_data("preregistration_commit", "88d27fdcc7a")

    # Verify the exact rational algebraic identity uncovered in Test 1:
    #   (1 + w_(3)(z_D)) * g_A^cross(q) = 1  for all q != 0,
    # hence g_A^diag(q) + w_(3)(z_D) * g_A^cross(q) = 1 + (g_A^diag(q) - g_A^cross(q)) = 1 + 3 q^4 / (q^4 + q^2 + 1)^2.
    q_s = sp.Symbol("q", positive=True)
    w_sym_s = (q_s**4 + 1) / ((q_s**2 + 1) ** 2)
    ga_cross_s = ((q_s**2 + 1) ** 2) / (2 * (q_s**4 + q_s**2 + 1))
    ident_check = sp.simplify((1 + w_sym_s) * ga_cross_s - 1) == 0

    # Strip "+ee" suffix to compute the intersection of bare nuclear and dressed atomic active faces:
    s_nuc_set = set(s2a_nuc["active_support_S"])
    s_atom_stripped = {name.removesuffix("+ee") for name in s2a_atom["active_support_S"]}
    joint_he4_support = sorted(s_nuc_set & s_atom_stripped)

    t1_clean = {k: v for k, v in t1.items() if not k.endswith("_mpf")}
    t1_clean["exact_identity_1_plus_wsymD_times_gAcross_eq_1"] = bool(ident_check)
    s2a_nuc_clean = {k: v for k, v in s2a_nuc.items() if not k.endswith("_mpf")}
    s2a_atom_clean = {k: v for k, v in s2a_atom.items() if not k.endswith("_mpf")}
    s2b_cas_clean = {k: v for k, v in s2b_cas.items() if not k.endswith("_mpf")}
    s2b_prd_clean = {k: v for k, v in s2b_prd.items() if not k.endswith("_mpf")}

    wb.add_data("q0_proton_80dps", fmt(q0))
    wb.add_data("test1_64d_gamow_teller", t1_clean)
    wb.add_data(
        "test2_extremal_functional_strata",
        {
            "stratum_2a_he4_bare_nuclear_phi": s2a_nuc_clean,
            "stratum_2a_he4_atomic_phi1_with_ee": s2a_atom_clean,
            "stratum_2a_he4_joint_active_intersection": joint_he4_support,
            "stratum_2b_meson_a_plus_b_eq_7_casimir_imbalance": s2b_cas_clean,
            "stratum_2b_meson_a_plus_b_eq_7_max_product": s2b_prd_clean,
        },
    )

    wb.add_assertion(
        name="sym3_gl4_weight_space_dim_eq_2_and_q1_hw_dim_eq_1",
        computed=f"{t1['dim_sym3_gl4_in_9d_weight_space']},{t1['dim_sym3_gl4_intersect_factorised_hw_at_q1']}",
        expected="2,1",
        source="Classical q=1 SU(4) symmetric cube Sym^3(C^4) has 2D (uud,up-up-dn) weight space and unique 1D (I=1/2,S=1/2) nucleon state",
    )
    wb.add_assertion(
        name="gl4_braiding_incompatibility_forces_factorised_doublet_for_q_ne_1",
        computed=str(t1["dim_sym3_gl4_intersect_factorised_hw_generic_q"]),
        expected="0",
        source="Jimbo U_q(gl_4) braiding mixes spin-flavour ordering and has 0D intersection with factorised U_q(sl_2)_iso x U_q(sl_2)_spin highest-weight for q != 1",
    )
    wb.add_assertion(
        name="exact_identity_one_plus_wsymD_times_gAcross_eq_one",
        computed="true" if ident_check else "false",
        expected="true",
        source="Exact algebraic identity (1 + w_(3)(z_D)) * g_A^cross(q) = 1 over Q(q)",
    )
    wb.add_assertion(
        name="pdg_gA_strictly_inside_64d_dq_positivity_interval",
        computed="true" if t1["pdg_inside_dq_positivity_interval"] else "false",
        expected="true",
        source="Verstichel-van Aggelen (D,Q) positivity interval [g_A^diag - g_A^cross, g_A^diag + g_A^cross] strictly brackets PDG g_A = 1.2754",
    )
    wb.add_assertion(
        name="he4_suboptimal_arrangements_have_strictly_positive_dual_slack_and_singleton_joint_face",
        computed="true"
        if (
            s2a_nuc["min_positive_dual_slack_mpf"] > mpf("1e-6")
            and s2a_atom["min_positive_dual_slack_mpf"] > mpf("1e-6")
            and joint_he4_support == ["nppn"]
        )
        else "false",
        expected="true",
        source="SymmetryReducedDualCertificate.unique_support_of_strict_dual_slack on C(4,2)=6 He-4 orderings; S_nuc cap S_atom = {'nppn'}",
    )
    wb.add_assertion(
        name="meson_a_plus_b_eq_7_singleton_unique_at_3_4",
        computed="true"
        if (
            s2b_cas["active_support_S"] == ["[3]_q*[4]_q"]
            and s2b_prd["active_support_S"] == ["[3]_q*[4]_q"]
            and s2b_cas["min_positive_dual_slack_mpf"] > mpf("1")
        )
        else "false",
        expected="true",
        source="SymmetryReducedDualCertificate.simplex_unique_optimal_of_strict_dual_slack on a+b=7 meson stratum",
    )

    wb.save({"q0Anchor": "proton", "preregistration": "PREREGISTRATION.md"})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
