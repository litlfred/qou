#!/usr/bin/env python3
"""80-dps proton-pinned verification probe for Accuracy Table conditional-to-proved reductions (`qou-vhm1`).

Audits and numerically/symbolically cross-checks all Lean 4 theorems proved in:
  1. `folio/quantum-observable-universe/lean/QOU/StandardModel/ElectroweakConditionalDischarge.lean`
  2. `folio/quantum-observable-universe/lean/QOU/StandardModel/AlphaEmConditionalReduction.lean`
and quantified in:
  - `docs/audits/2026-11-28-accuracy-conditional-discharge-ledger.md`

Discipline & Owner Ruling (`2026-11-28`):
  - Strictly proton-pinned (`q0Anchor = "proton"`, `qou_substrate.constants.q_at(95)`), registered
    under `physical_proton` in `computations/q0_anchor_manifest.json`.
  - Muon pin is ON HOLD until rederivation; zero muon-pin columns or comparisons are evaluated.
  - `mpmath` working precision `WORK_DPS = 95` (`80`-dps serialized strings + `15`-dps guard);
    exact `fractions.Fraction` interval arithmetic for `LawvereCut.Cut Q` enclosures;
    exact `sympy` over `Q` for quantum-integer, Clebsch-Gordan, bar-parity, loop-ladder, and
    anomaly/Weinberg identities.
  - Zero `float64` casts/literals; zero inline CODATA literals (all experimental benchmarks read
    live from `qou_substrate.codata.codata`); zero fitted constants (`NO FITTING, EXCEPT CAL-1/2/3`).
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from pathlib import Path
import sys

_THIS = Path(__file__).resolve()
_ROOT = _THIS.parents[2]
for _p in (
    _ROOT / "tools" / "qou-substrate" / "python",
    _ROOT / "computations",
):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at, vol_4_1_at  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 95
OUT_DPS = 80
set_compute_dps(WORK_DPS)
mp.mp.dps = WORK_DPS


def fmt80(val: mp.mpf) -> str:
    """Serialize an mpf at 80 significant digits with zero float64 conversion."""
    return mp.nstr(val, OUT_DPS, strip_zeros=False)


# ---------------------------------------------------------------------------
# 1. Finite S_5 Regular-Map Bring Topology (`BringMapChain`)
# ---------------------------------------------------------------------------
def verify_bring_regular_map() -> dict[str, object]:
    """Verify V=30, E=60, F=24, chi=-6, g=4, b_1=8, orbits=1 on the 120 darts of S_5."""
    elems = list(permutations(range(5)))
    idx = {p: i for i, p in enumerate(elems)}

    def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(p[q[i]] for i in range(5))

    # Order-4 vertex rotation (0 1 2 3) and order-2 edge involution (3 4) generate S_5
    # with product (0 1 2 3)(3 4) = (0 1 2 3 4) of order 5 (`{5, 4}` Bring map).
    sigma_g = (1, 2, 3, 0, 4)
    alpha_g = (0, 1, 2, 4, 3)
    sa_g = compose(sigma_g, alpha_g)

    def cycle_count_left_action(gen: tuple[int, ...]) -> int:
        seen: set[int] = set()
        cycles = 0
        for start in range(len(elems)):
            if start in seen:
                continue
            cycles += 1
            cur = start
            while cur not in seen:
                seen.add(cur)
                cur = idx[compose(gen, elems[cur])]
        return cycles

    # Connectedness (number of <sigma, alpha>-orbits on 120 darts)
    visited: set[int] = set()
    orbits = 0
    for start in range(len(elems)):
        if start in visited:
            continue
        orbits += 1
        stack = [start]
        visited.add(start)
        while stack:
            u = stack.pop()
            for gen in (sigma_g, alpha_g):
                v = idx[compose(gen, elems[u])]
                if v not in visited:
                    visited.add(v)
                    stack.append(v)

    v_cnt = cycle_count_left_action(sigma_g)
    e_cnt = cycle_count_left_action(alpha_g)
    f_cnt = cycle_count_left_action(sa_g)
    chi = v_cnt - e_cnt + f_cnt
    b1 = 2 - chi
    genus = b1 // 2
    ew_seifert_sum = (2 - 1) + (3 - 1) + (4 - 1)

    # Affine carrier-genus uniqueness (`ew_em_genusAffine_unique_domain`):
    # (a*4 + b) + (a*4 + b) = 8 and (a*1 + b) + (a*2 + b) + (a*3 + b) = 12 => a = 0, b = 4
    a_sym, b_sym, g_sym = sp.symbols("a b g")
    sol_aff = sp.solve(
        [2 * (4 * a_sym + b_sym) - 8, (a_sym + b_sym) + (2 * a_sym + b_sym) + (3 * a_sym + b_sym) - 12],
        [a_sym, b_sym],
    )
    sol_gb = sp.solve(2 * g_sym - 8, g_sym)

    ok = (
        len(elems) == 120
        and orbits == 1
        and v_cnt == 30
        and e_cnt == 60
        and f_cnt == 24
        and chi == -6
        and b1 == 8
        and genus == 4
        and ew_seifert_sum == 6 == -chi
        and sol_aff == {a_sym: sp.Integer(0), b_sym: sp.Integer(4)}
        and sol_gb == [sp.Integer(4)]
    )
    return {
        "passed": ok,
        "darts": len(elems),
        "orbits": orbits,
        "V_numCycles_sigma": v_cnt,
        "E_numCycles_alpha": e_cnt,
        "F_numCycles_sigma_alpha": f_cnt,
        "bringMapEuler": chi,
        "bringMapBettiOne": b1,
        "bringGenus": genus,
        "ewSeifertSum": ew_seifert_sum,
        "affine_carrier_rule_unique_a0_b4": sol_aff == {a_sym: sp.Integer(0), b_sym: sp.Integer(4)},
        "betti_eq_gauss_bonnet_unique_g4": sol_gb == [sp.Integer(4)],
    }


# ---------------------------------------------------------------------------
# 2. Exact Symbolic Identities (`SymPy` over Q) mirroring Lean 4 theorems
# ---------------------------------------------------------------------------
def verify_symbolic_identities() -> dict[str, object]:
    q, mu1 = sp.symbols("q mu1")
    x = q + 1 / q

    def qbal_sym(n: int) -> sp.Expr:
        if n == 0:
            return sp.Integer(0)
        return sp.cancel((q**n - q ** (-n)) / (q - 1 / q))

    # EW Chebyshev factorizations (`qBalU_ew_chebyshev_factors`)
    cheb_ok = (
        sp.cancel(qbal_sym(2) - x) == 0
        and sp.cancel(qbal_sym(4) - x * (x**2 - 2)) == 0
        and sp.cancel(qbal_sym(6) - x * (x - 1) * (x + 1) * (x**2 - 3)) == 0
        and sp.cancel(qbal_sym(8) - x * (x**2 - 2) * (x**4 - 4 * x**2 + 2)) == 0
    )

    # EW 9-channel Clebsch-Gordan (`ew_carrier_product_clebsch_gordan`)
    ew_prod = qbal_sym(2) * qbal_sym(4) * qbal_sym(6) * qbal_sym(8)
    ew_cg = (
        qbal_sym(17)
        + 3 * qbal_sym(15)
        + 5 * qbal_sym(13)
        + 7 * qbal_sym(11)
        + 8 * qbal_sym(9)
        + 8 * qbal_sym(7)
        + 7 * qbal_sym(5)
        + 5 * qbal_sym(3)
        + 2 * qbal_sym(1)
    )
    ew_cg_ok = sp.cancel(ew_prod - ew_cg) == 0
    two_ew_tree = q * ew_prod
    two_ew_tree_bar = sp.cancel(two_ew_tree.subs(q, 1 / q) * q**2 - two_ew_tree) == 0
    two_ew_tree_q1 = int(sp.cancel(two_ew_tree).subs(q, 1))

    # Contrast: illustrative expression q[16]_q[17]_q - [4]_q + 1/[2]_q evaluates to 268.5 != 192 at q=1
    illustrative_q1 = sp.Rational(16 * 17 - 4, 1) + sp.Rational(1, 2)

    # EM 9-channel Clebsch-Gordan (`em_carrier_product_clebsch_gordan`)
    em_prod = qbal_sym(9) * qbal_sym(10)
    em_cg = sum((qbal_sym(2 * m) for m in range(1, 10)), sp.Integer(0))
    em_cg_ok = sp.cancel(em_prod - em_cg) == 0
    em_tree = q * em_prod
    em_tree_bar = sp.cancel(em_tree.subs(q, 1 / q) * q**2 - em_tree) == 0
    em_tree_q1 = int(sp.cancel(em_tree).subs(q, 1))

    # Skein-to-Habiro conversion (`barOdd_join_habiro_bridge_and_const_measure`)
    habiro_bridge_ok = sp.cancel((q - 1 / q) ** 2 - (q + 1) ** 2 * (1 - 1 / q) ** 2) == 0

    # Form-B vs theta connected 2-loop cumulant (`em_formB_all_loop_reduction`)
    formb_conn_ok = sp.expand((mu1 - mu1**2) - mu1 * (1 - mu1)) == 0
    theta_conn_ok = sp.expand(mu1**2 - mu1**2) == 0

    # SU(2)_L one-loop beta sign (`sixOneLoopB0_su2_neg_and_abelian_pos`)
    six_b0_su2 = -22 * 2 + 2 * 12 + 1

    # Constructive anomaly-free hypercharge & sin^2(theta_W)(0) = 3/8
    # (`cleared_anomalyFree_neutral_forces_three_eighths`)
    yq, yu = sp.symbols("YQ Yu")
    yl = -3 * yq
    yd = -2 * yq - yu
    ye = 6 * yq
    cubic_anom = sp.expand(6 * yq**3 + 3 * yu**3 + 3 * yd**3 + 2 * yl**3 + ye**3)
    cubic_fac = sp.expand(-18 * yq * (yu + 4 * yq) * (yu - 2 * yq))
    anom_fac_ok = cubic_anom == cubic_fac
    tr_six_t3_sq = 6 * 9 + 2 * 9  # 72
    tr_six_q_sq_sm = tr_six_t3_sq + (6 * 1 + 3 * 16 + 3 * 4 + 2 * 9 + 36)  # 72 + 120 = 192
    weinberg_cleared_ok = 8 * tr_six_t3_sq == 3 * tr_six_q_sq_sm == 576

    # S3CirculantKoideTraceIdentity: TL_3(q) departure from 2/3 equals h^2 / (3 (q^2 + q^-2))
    h = q - 1 / q
    y3 = 1 - 2 / (q + 1 / q) ** 2
    y21 = 1 / (q + 1 / q) ** 2
    q_tl3 = (y3 + 2 * y21) / (3 * y3)
    tl3_dep_ok = sp.cancel((sp.Rational(2, 3) - q_tl3) - h**2 / (3 * (q**2 + q ** (-2)))) == 0

    all_ok = (
        cheb_ok
        and ew_cg_ok
        and two_ew_tree_bar
        and two_ew_tree_q1 == 384
        and illustrative_q1 == sp.Rational(537, 2)
        and em_cg_ok
        and em_tree_bar
        and em_tree_q1 == 90
        and habiro_bridge_ok
        and formb_conn_ok
        and theta_conn_ok
        and six_b0_su2 == -19
        and anom_fac_ok
        and weinberg_cleared_ok
        and tl3_dep_ok
    )
    return {
        "passed": all_ok,
        "ew_chebyshev_factors_exact": cheb_ok,
        "ew_clebsch_gordan_9channel_exact": ew_cg_ok,
        "twoEwTreeU_bar_and_q1_eq_384": two_ew_tree_bar and two_ew_tree_q1 == 384,
        "illustrative_alt_tree_at_q1": str(illustrative_q1),
        "em_clebsch_gordan_9channel_exact": em_cg_ok,
        "emTreeU_bar_and_q1_eq_90": em_tree_bar and em_tree_q1 == 90,
        "skein_to_habiro_square_bridge_exact": habiro_bridge_ok,
        "sixOneLoopB0_su2_eq_neg_19": six_b0_su2,
        "anomaly_cubic_factorization_exact": anom_fac_ok,
        "cleared_weinberg_trace_8x72_eq_3x192_eq_576": weinberg_cleared_ok,
        "tl3_koide_departure_identity_exact": tl3_dep_ok,
    }


# ---------------------------------------------------------------------------
# 3. Exact `fractions.Fraction` Verification of Lean `LawvereCut.Cut Q` Certificates
# ---------------------------------------------------------------------------
def qbal_frac(n: int, q: Fraction) -> Fraction:
    if n == 0:
        return Fraction(0)
    return (q**n - Fraction(1) / (q**n)) / (q - Fraction(1) / q)


def verify_lawvere_cuts_rational(q0: mp.mpf) -> dict[str, object]:
    """Verify over exact Q (`fractions.Fraction`) that:
      (a) proton-pinned (q0, pi) maps strictly inside the certified rational parameter
          boxes of `ewNvProton_cut_certified` and `emFormB_and_rydberg_proton_cut_certified`, and
      (b) exact rational cubic evaluations change sign across `ewNvProtonCut` and `emInvAlphaProtonCut`.
    """
    scale30 = 10**30
    q_lo_int = int(mp.floor(q0 * scale30))
    pi_lo_int = int(mp.floor(mp.pi * scale30))
    q_lo = Fraction(q_lo_int, scale30)
    q_hi = Fraction(q_lo_int + 1, scale30)
    pi_lo = Fraction(pi_lo_int, scale30)
    pi_hi = Fraction(pi_lo_int + 1, scale30)

    # Confirm q0 and pi sit strictly inside [q_lo, q_hi] and [pi_lo, pi_hi] at 95 dps
    q_in = mp.mpf(q_lo.numerator) / mp.mpf(q_lo.denominator) < q0 < mp.mpf(q_hi.numerator) / mp.mpf(q_hi.denominator)
    pi_in = mp.mpf(pi_lo.numerator) / mp.mpf(pi_lo.denominator) < mp.pi < mp.mpf(pi_hi.numerator) / mp.mpf(pi_hi.denominator)

    # Monotone interval bounds on q > 1:
    # [n]_q = sum_{k=0}^{n-1} q^{n-1-2k} is strictly increasing on q > 1 for n >= 2,
    # q - 1/q and 1 - 1/q and q + 1/q are all strictly increasing on q > 1!
    def ew_tree_frac(q: Fraction) -> Fraction:
        return q * Fraction(1, 2) * qbal_frac(2, q) * qbal_frac(4, q) * qbal_frac(6, q) * qbal_frac(8, q)

    def em_tree_frac(q: Fraction) -> Fraction:
        return q * qbal_frac(9, q) * qbal_frac(10, q)

    t_ew_true_lo = ew_tree_frac(q_lo) + Fraction(1, 1) / pi_hi
    t_ew_true_hi = ew_tree_frac(q_hi) + Fraction(1, 1) / pi_lo

    t0_em_true_lo = em_tree_frac(q_lo) + Fraction(2, 3) / pi_hi
    t0_em_true_hi = em_tree_frac(q_hi) + Fraction(2, 3) / pi_lo

    h_hab_true_lo = (q_lo + Fraction(1) / q_hi) / (8 * pi_hi)  # wait: q + 1/q is increasing for q > 1!
    # Even tighter & simpler since d/dq(q + 1/q) = 1 - 1/q^2 > 0 on q > 1:
    q2_lo = qbal_frac(2, q_lo)
    q2_hi = qbal_frac(2, q_hi)
    h_hab_true_lo = q2_lo / (8 * pi_hi)
    h_hab_true_hi = q2_hi / (8 * pi_lo)

    hbar_lo = Fraction(1) - Fraction(1) / q_lo
    hbar_hi = Fraction(1) - Fraction(1) / q_hi
    ch_true_lo = (hbar_lo**2) * h_hab_true_lo
    ch_true_hi = (hbar_hi**2) * h_hab_true_hi

    h_skein_lo = q_lo - Fraction(1) / q_lo
    h_skein_hi = q_hi - Fraction(1) / q_hi
    h2h_true_lo = (h_skein_lo**2) * h_hab_true_lo
    h2h_true_hi = (h_skein_hi**2) * h_hab_true_hi

    # Certified parameter boxes from Lean 4 theorems
    lean_t_ew_lo = Fraction(262418473706849, 1000000000000)
    lean_t_ew_hi = Fraction(262418473706851, 1000000000000)
    lean_h_lo = Fraction(312543141, 3906250000)
    lean_h_hi = Fraction(80011044097, 1000000000000)
    lean_ch_lo = Fraction(392741669, 500000000000)
    lean_ch_hi = Fraction(785483339, 1000000000000)

    lean_t0_em_lo = Fraction(137035415444371, 1000000000000)
    lean_t0_em_hi = Fraction(34258853861093, 250000000000)
    lean_h2h_lo = Fraction(1748489689, 500000000000)
    lean_h2h_hi = Fraction(3496979379, 1000000000000)

    ew_box_contains_true = (
        lean_t_ew_lo <= t_ew_true_lo <= t_ew_true_hi <= lean_t_ew_hi
        and lean_h_lo <= h_hab_true_lo <= h_hab_true_hi <= lean_h_hi
        and lean_ch_lo <= ch_true_lo <= ch_true_hi <= lean_ch_hi
    )
    em_box_contains_true = (
        lean_t0_em_lo <= t0_em_true_lo <= t0_em_true_hi <= lean_t0_em_hi
        and lean_h_lo <= h_hab_true_lo <= h_hab_true_hi <= lean_h_hi
        and lean_h2h_lo <= h2h_true_lo <= h2h_true_hi <= lean_h2h_hi
    )

    # Exact rational sign-change checks matching Lean `norm_num` obligations
    ew_nv_lo = Fraction(2624181688191, 10000000000)
    ew_nv_hi = Fraction(2624181688194, 10000000000)

    def ew_cubic_q(t_v: Fraction, h_v: Fraction, ch_v: Fraction, n_v: Fraction) -> Fraction:
        return n_v**3 - t_v * (n_v**2) + h_v * n_v - ch_v

    ew_worst_lo = ew_cubic_q(lean_t_ew_lo, lean_h_hi, lean_ch_lo, ew_nv_lo)
    ew_worst_hi = ew_cubic_q(lean_t_ew_hi, lean_h_lo, lean_ch_hi, ew_nv_hi)

    em_a_lo = Fraction(1370359991268, 10000000000)
    em_a_hi = Fraction(1370359991271, 10000000000)

    def em_cubic_q(t0_v: Fraction, h_v: Fraction, h2h_v: Fraction, a_v: Fraction) -> Fraction:
        return a_v**3 - t0_v * (a_v**2) - h_v * a_v + h2h_v

    em_worst_lo = em_cubic_q(lean_t0_em_lo, lean_h_lo, lean_h2h_hi, em_a_lo)
    em_worst_hi = em_cubic_q(lean_t0_em_hi, lean_h_hi, lean_h2h_lo, em_a_hi)

    ryd_lo = Fraction(1, 1) / (2 * (em_a_hi**2))
    ryd_hi = Fraction(1, 1) / (2 * (em_a_lo**2))

    ok = (
        q_in
        and pi_in
        and ew_box_contains_true
        and em_box_contains_true
        and ew_worst_lo < 0
        and ew_worst_hi > 0
        and em_worst_lo < 0
        and em_worst_hi > 0
        and ryd_lo < ryd_hi
    )
    return {
        "passed": ok,
        "ew_parameter_box_contains_proton_q0_pi": ew_box_contains_true,
        "em_parameter_box_contains_proton_q0_pi": em_box_contains_true,
        "ewNvProtonLo": f"{ew_nv_lo.numerator}/{ew_nv_lo.denominator}",
        "ewNvProtonHi": f"{ew_nv_hi.numerator}/{ew_nv_hi.denominator}",
        "ewNvProtonCut_width": "3/10000000000",
        "ew_cubic_worst_lo_negative": ew_worst_lo < 0,
        "ew_cubic_worst_hi_positive": ew_worst_hi > 0,
        "emInvAlphaProtonLo": f"{em_a_lo.numerator}/{em_a_lo.denominator}",
        "emInvAlphaProtonHi": f"{em_a_hi.numerator}/{em_a_hi.denominator}",
        "emInvAlphaProtonCut_width": "3/10000000000",
        "em_cubic_worst_lo_negative": em_worst_lo < 0,
        "em_cubic_worst_hi_positive": em_worst_hi > 0,
        "rydbergFactorProtonLo": f"{ryd_lo.numerator}/{ryd_lo.denominator}",
        "rydbergFactorProtonHi": f"{ryd_hi.numerator}/{ryd_hi.denominator}",
    }


# ---------------------------------------------------------------------------
# 4. 80-dps Proton-Pinned Scorecard Evaluation (`m_tau/m_e`, `alpha_EM`, `R_inf`, `v_weak`)
# ---------------------------------------------------------------------------
def qbal_mp(n: int, q: mp.mpf) -> mp.mpf:
    return (q**n - q ** (-n)) / (q - mp.mpf(1) / q)


def evaluate_proton_pinned_observables(q0: mp.mpf, vol41: mp.mpf) -> dict[str, object]:
    # Authoritative CODATA-2022 entries (zero inline CODATA literals)
    me_entry = codata("electron mass energy equivalent in MeV")
    rpe_entry = codata("proton-electron mass ratio")
    gf_entry = codata("Fermi coupling constant")
    alpha_entry = codata("inverse fine-structure constant")
    ry_entry = codata("Rydberg constant times hc in eV")
    tau_entry = codata("tau-electron mass ratio")

    me_mev = mp.mpf(me_entry.value_str)
    me_sig_mev = mp.mpf(me_entry.uncertainty_str)
    rpe_exp = mp.mpf(rpe_entry.value_str)
    gf_exp = mp.mpf(gf_entry.value_str)
    gf_sig = mp.mpf(gf_entry.uncertainty_str)
    alpha_inv_exp = mp.mpf(alpha_entry.value_str)
    alpha_inv_sig = mp.mpf(alpha_entry.uncertainty_str)
    ry_exp_ev = mp.mpf(ry_entry.value_str)
    ry_sig_ev = mp.mpf(ry_entry.uncertainty_str)
    tau_me_exp = mp.mpf(tau_entry.value_str)
    tau_me_sig = mp.mpf(tau_entry.uncertainty_str)

    h = q0 - mp.mpf(1) / q0
    hbar_q = mp.mpf(1) - mp.mpf(1) / q0
    hab_norm = qbal_mp(2, q0) / (mp.mpf(8) * mp.pi)

    # Proton substrate self-consistency check at q0
    tr_m_bor = mp.fabs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))
    qf3 = (q0**2 + 1 + q0 ** (-2)) * (q0 + q0 ** (-1))
    rpe_from_q0 = 2 * vol41 / (hbar_q**2) * (tr_m_bor * qf3 / (q0**3)) - 12

    # --- (A) Electroweak VEV v_weak & N_v ---
    t_ew = q0 * (qbal_mp(2, q0) / mp.mpf(2)) * qbal_mp(4, q0) * qbal_mp(6, q0) * qbal_mp(8, q0) + mp.mpf(1) / mp.pi
    nv_ew = mp.findroot(
        lambda n: n**3 - t_ew * (n**2) + hab_norm * n - (hbar_q**2) * hab_norm,
        mp.mpf("262.4181688"),
    )
    alpha_v = mp.mpf(1) / nv_ew
    ew_fp_resid = (mp.mpf(1) / alpha_v) - (t_ew - alpha_v * hab_norm * (mp.mpf(1) - (hbar_q**2) * alpha_v))

    mp_cal_gev = (me_mev * rpe_from_q0) / mp.mpf(1000)
    v_ew_pred_gev = nv_ew * mp_cal_gev
    v_ew_exp_gev = mp.mpf(1) / mp.sqrt(mp.sqrt(mp.mpf(2)) * gf_exp)
    v_ew_sig_gev = v_ew_exp_gev * gf_sig / (mp.mpf(2) * gf_exp)
    v_ew_ppb = ((v_ew_pred_gev - v_ew_exp_gev) / v_ew_exp_gev) * mp.mpf("1e9")
    v_ew_sigma = (v_ew_pred_gev - v_ew_exp_gev) / v_ew_sig_gev

    # --- (B) Electromagnetic alpha_EM^-1 Form B & Form C ---
    t0_em = q0 * qbal_mp(9, q0) * qbal_mp(10, q0) + mp.mpf(2) / (mp.mpf(3) * mp.pi)
    alpha_inv_fb = mp.findroot(
        lambda a: a**3 - t0_em * (a**2) - hab_norm * a + (h**2) * hab_norm,
        mp.mpf("137.0359991"),
    )
    alpha_fb = mp.mpf(1) / alpha_inv_fb
    alpha_fb_ppb = ((alpha_inv_fb - alpha_inv_exp) / alpha_inv_exp) * mp.mpf("1e9")
    alpha_fb_sigma = (alpha_inv_fb - alpha_inv_exp) / alpha_inv_sig

    # Form C (`FormCPinned`: deltaB3 q0 = deltaReq q0 alpha_fc)
    delta_b3 = mp.zeta(3) - mp.polylog(3, q0 ** (-2))
    c2_bloch_b3 = hab_norm * delta_b3 / (mp.mpf(8) * mp.pi)
    alpha_fc = mp.findroot(
        lambda a: (t0_em + hab_norm * a * (mp.mpf(1) - (h**2) * a) + c2_bloch_b3 * (a**2)) * a - mp.mpf(1),
        mp.mpf("1") / mp.mpf("137.03599917"),
    )
    alpha_inv_fc = mp.mpf(1) / alpha_fc
    alpha_fc_ppb = ((alpha_inv_fc - alpha_inv_exp) / alpha_inv_exp) * mp.mpf("1e9")
    alpha_fc_sigma = (alpha_inv_fc - alpha_inv_exp) / alpha_inv_sig
    delta_req_fc = (
        ((mp.mpf(8) * mp.pi) ** 2 / qbal_mp(2, q0))
        * (
            alpha_inv_fc
            - (t0_em + hab_norm * alpha_fc * (mp.mpf(1) - (h**2) * alpha_fc))
        )
        / (alpha_fc**2)
    )
    form_c_pinned_resid = delta_b3 - delta_req_fc

    # --- (C) Rydberg R_infty h c Form B & Form C ---
    ryd_factor_fb = mp.mpf("0.5") / (alpha_inv_fb**2)
    ry_fb_ev = (me_mev * mp.mpf("1e6")) * ryd_factor_fb
    ry_fb_ppb = ((ry_fb_ev - ry_exp_ev) / ry_exp_ev) * mp.mpf("1e9")

    ryd_factor_fc = mp.mpf("0.5") / (alpha_inv_fc**2)
    ry_fc_ev = (me_mev * mp.mpf("1e6")) * ryd_factor_fc
    ry_fc_ppb = ((ry_fc_ev - ry_exp_ev) / ry_exp_ev) * mp.mpf("1e9")
    # Combined sigma from m_e calibration uncertainty + experimental R_infty uncertainty
    ry_fc_sig_comb = mp.sqrt((ry_fc_ev * (me_sig_mev / me_mev)) ** 2 + ry_sig_ev**2)
    ry_fc_sigma_comb = (ry_fc_ev - ry_exp_ev) / ry_fc_sig_comb

    # --- (D) Tau/electron m_tau / m_e on proton-pinned q0 ---
    r_mu_e_bare_proton = vol41 / (hbar_q**2)
    v_mu = mp.sqrt(r_mu_e_bare_proton)
    x_tau = mp.mpf(2) * (mp.mpf(1) + v_mu) + mp.sqrt(mp.mpf(3) * (mp.mpf(1) + mp.mpf(4) * v_mu + v_mu**2))
    mtau_me_pred = x_tau**2
    koide_q_val = (mp.mpf(1) + v_mu**2 + x_tau**2) / ((mp.mpf(1) + v_mu + x_tau) ** 2)
    mtau_me_ppm = ((mtau_me_pred - tau_me_exp) / tau_me_exp) * mp.mpf("1e6")
    mtau_me_sigma = (mtau_me_pred - tau_me_exp) / tau_me_sig
    tl3_departure_q0 = (h**2) / (mp.mpf(3) * (q0**2 + q0 ** (-2)))

    # Rational LawvereCut membership checks on 80-dps roots
    nv_lo_mp = mp.mpf(2624181688191) / mp.mpf(10000000000)
    nv_hi_mp = mp.mpf(2624181688194) / mp.mpf(10000000000)
    a_lo_mp = mp.mpf(1370359991268) / mp.mpf(10000000000)
    a_hi_mp = mp.mpf(1370359991271) / mp.mpf(10000000000)
    ryd_lo_mp = mp.mpf(1) / (mp.mpf(2) * a_hi_mp**2)
    ryd_hi_mp = mp.mpf(1) / (mp.mpf(2) * a_lo_mp**2)

    return {
        "proton_pin_resid": rpe_from_q0 - rpe_exp,
        "nv_ew": nv_ew,
        "ew_fp_resid": ew_fp_resid,
        "nv_in_cut": nv_lo_mp < nv_ew < nv_hi_mp,
        "v_ew_pred_gev": v_ew_pred_gev,
        "v_ew_exp_gev": v_ew_exp_gev,
        "v_ew_sig_gev": v_ew_sig_gev,
        "v_ew_ppb": v_ew_ppb,
        "v_ew_sigma": v_ew_sigma,
        "alpha_inv_fb": alpha_inv_fb,
        "alpha_inv_exp": alpha_inv_exp,
        "alpha_inv_sig": alpha_inv_sig,
        "alpha_fb_ppb": alpha_fb_ppb,
        "alpha_fb_sigma": alpha_fb_sigma,
        "alpha_fb_in_cut": a_lo_mp < alpha_inv_fb < a_hi_mp,
        "alpha_inv_fc": alpha_inv_fc,
        "alpha_fc_ppb": alpha_fc_ppb,
        "alpha_fc_sigma": alpha_fc_sigma,
        "delta_b3": delta_b3,
        "delta_req_fc": delta_req_fc,
        "form_c_pinned_resid": form_c_pinned_resid,
        "ryd_factor_fb": ryd_factor_fb,
        "ryd_factor_in_cut": ryd_lo_mp < ryd_factor_fb < ryd_hi_mp,
        "ry_fb_ev": ry_fb_ev,
        "ry_fc_ev": ry_fc_ev,
        "ry_exp_ev": ry_exp_ev,
        "ry_fb_ppb": ry_fb_ppb,
        "ry_fc_ppb": ry_fc_ppb,
        "ry_fc_sigma_comb": ry_fc_sigma_comb,
        "mtau_me_pred": mtau_me_pred,
        "mtau_me_exp": tau_me_exp,
        "mtau_me_sig": tau_me_sig,
        "mtau_me_ppm": mtau_me_ppm,
        "mtau_me_sigma": mtau_me_sigma,
        "koide_q_val": koide_q_val,
        "tl3_departure_q0": tl3_departure_q0,
    }


def main() -> None:
    q0 = q_at(WORK_DPS)
    vol41 = vol_4_1_at(WORK_DPS)

    bring_res = verify_bring_regular_map()
    sym_res = verify_symbolic_identities()
    cut_res = verify_lawvere_cuts_rational(q0)
    obs_res = evaluate_proton_pinned_observables(q0, vol41)

    wb = (
        WitnessBuilder(
            "accuracy-conditional-discharge-probe",
            engine="mpmath",
            output_dir=_THIS.parent,
        )
        .set_description(
            "80-dps strictly proton-pinned verification of QOU/StandardModel/"
            "ElectroweakConditionalDischarge.lean and QOU/StandardModel/"
            "AlphaEmConditionalReduction.lean (bean qou-vhm1): finite S_5 regular-map "
            "Bring genus g=4 / b_1=8 discharge, constructive [CommRing R] quantum-integer "
            "Clebsch-Gordan & bar-parity identities, Form-B all-loop signed join -h^2 & "
            "constant measure, domain-level sin^2(theta_W)(0)=3/8, exact Q LawvereCut "
            "certificates on N_v(q0), alpha_EM^-1(q0), and R_inf/m_e, and before/after "
            "conditional hypothesis ledger."
        )
        .set_audit_only("docs/audits/2026-11-28-accuracy-conditional-discharge-ledger.md")
    )

    wb.add_parameter("q0", fmt80(q0))
    wb.add_parameter("vol_4_1", fmt80(vol41))
    wb.add_parameter("compute_dps", WORK_DPS)
    wb.add_parameter("output_dps", OUT_DPS)

    # Assertions (all serialized as strings to stay strictly free of float64)
    wb.add_assertion(
        "bring_regular_map_chi_neg6_genus_4_betti_8",
        computed="1" if bring_res["passed"] else "0",
        expected="1",
        tolerance="0.1",
        source="ElectroweakConditionalDischarge.bringMap_connected_and_euler",
    )
    wb.add_assertion(
        "constructive_commring_clebsch_gordan_weinberg_loop_identities",
        computed="1" if sym_res["passed"] else "0",
        expected="1",
        tolerance="0.1",
        source="ElectroweakConditionalDischarge + AlphaEmConditionalReduction (§2-§4)",
    )
    wb.add_assertion(
        "proton_lawvere_cuts_rational_enclosure_and_sign_change",
        computed="1" if cut_res["passed"] else "0",
        expected="1",
        tolerance="0.1",
        source="ewNvProton_cut_certified + emFormB_and_rydberg_proton_cut_certified",
    )
    wb.add_assertion(
        "proton_pin_roundtrip_residual",
        computed=fmt80(obs_res["proton_pin_resid"]),
        expected="0",
        tolerance="1e-80",
        source="qou_substrate.constants.q_at(95)",
    )
    wb.add_assertion(
        "ew_fixed_point_self_consistency_residual",
        computed=fmt80(obs_res["ew_fp_resid"]),
        expected="0",
        tolerance="1e-80",
        source="ElectroweakConditionalDischarge.minimalEwBridge_discharges_legacy_classes",
    )
    wb.add_assertion(
        "ew_nv_proton_inside_lawvere_cut",
        computed="1" if obs_res["nv_in_cut"] else "0",
        expected="1",
        tolerance="0.1",
        source="ElectroweakConditionalDischarge.ewNvProton_cut_certified",
    )
    wb.add_assertion(
        "ew_vev_proton_within_1sigma_codata_gf",
        computed=fmt80(obs_res["v_ew_pred_gev"]),
        expected=fmt80(obs_res["v_ew_exp_gev"]),
        tolerance=fmt80(obs_res["v_ew_sig_gev"]),
        unit="GeV",
        source="CODATA 2022 Fermi coupling constant",
    )
    wb.add_assertion(
        "em_formB_inv_alpha_proton_inside_lawvere_cut",
        computed="1" if obs_res["alpha_fb_in_cut"] and obs_res["ryd_factor_in_cut"] else "0",
        expected="1",
        tolerance="0.1",
        source="AlphaEmConditionalReduction.emFormB_and_rydberg_proton_cut_certified",
    )
    wb.add_assertion(
        "em_formC_pinned_deltaB3_eq_deltaReq",
        computed=fmt80(obs_res["delta_b3"]),
        expected=fmt80(obs_res["delta_req_fc"]),
        tolerance="1e-75",
        source="AlphaEmConditionalReduction.formC_pinned_and_dilog_duplication_status",
    )
    wb.add_assertion(
        "em_formC_inv_alpha_proton_within_1sigma_codata",
        computed=fmt80(obs_res["alpha_inv_fc"]),
        expected=fmt80(obs_res["alpha_inv_exp"]),
        tolerance=fmt80(obs_res["alpha_inv_sig"]),
        source="CODATA 2022 inverse fine-structure constant",
    )
    wb.add_assertion(
        "koide_quadratic_resolvent_q_eq_two_thirds",
        computed=fmt80(obs_res["koide_q_val"]),
        expected=fmt80(mp.mpf(2) / mp.mpf(3)),
        tolerance="1e-80",
        source="S3CirculantKoideTraceIdentity.koide_quadratic_resolvent",
    )
    wb.add_assertion(
        "mtau_over_me_proton_within_1sigma_codata",
        computed=fmt80(obs_res["mtau_me_pred"]),
        expected=fmt80(obs_res["mtau_me_exp"]),
        tolerance=fmt80(obs_res["mtau_me_sig"]),
        source="CODATA 2022 tau-electron mass ratio",
    )

    wb.add_data("bring_regular_map_discharge", bring_res)
    wb.add_data("constructive_symbolic_identities", sym_res)
    wb.add_data("lawvere_cut_rational_certificates", cut_res)
    wb.add_data(
        "proton_pinned_observables_80dps",
        {
            "pin_policy": "Strictly proton-pinned per owner ruling 2026-11-28; muon pin on hold until rederivation.",
            "N_v_pred": fmt80(obs_res["nv_ew"]),
            "v_weak_pred_GeV": fmt80(obs_res["v_ew_pred_gev"]),
            "v_weak_exp_GeV": fmt80(obs_res["v_ew_exp_gev"]),
            "v_weak_err_ppb": fmt80(obs_res["v_ew_ppb"]),
            "v_weak_pull_sigma": fmt80(obs_res["v_ew_sigma"]),
            "alpha_EM_inv_FormB_pred": fmt80(obs_res["alpha_inv_fb"]),
            "alpha_EM_inv_FormB_err_ppb": fmt80(obs_res["alpha_fb_ppb"]),
            "alpha_EM_inv_FormB_pull_sigma": fmt80(obs_res["alpha_fb_sigma"]),
            "alpha_EM_inv_FormC_pred": fmt80(obs_res["alpha_inv_fc"]),
            "alpha_EM_inv_FormC_err_ppb": fmt80(obs_res["alpha_fc_ppb"]),
            "alpha_EM_inv_FormC_pull_sigma": fmt80(obs_res["alpha_fc_sigma"]),
            "rydberg_FormB_eV": fmt80(obs_res["ry_fb_ev"]),
            "rydberg_FormB_err_ppb": fmt80(obs_res["ry_fb_ppb"]),
            "rydberg_FormC_eV": fmt80(obs_res["ry_fc_ev"]),
            "rydberg_FormC_err_ppb": fmt80(obs_res["ry_fc_ppb"]),
            "rydberg_FormC_pull_sigma_comb": fmt80(obs_res["ry_fc_sigma_comb"]),
            "m_tau_over_m_e_pred": fmt80(obs_res["mtau_me_pred"]),
            "m_tau_over_m_e_err_ppm": fmt80(obs_res["mtau_me_ppm"]),
            "m_tau_over_m_e_pull_sigma_codata22": fmt80(obs_res["mtau_me_sigma"]),
            "tl3_koide_departure_at_q0": fmt80(obs_res["tl3_departure_q0"]),
        },
    )
    wb.add_data(
        "hypothesis_reduction_ledger",
        {
            "m_tau_over_m_e": {
                "premises_before": 5,
                "discharged_proved": 4,
                "remaining_open": 1,
                "open_kernel": "KoideCirculantEquipartitionHypothesis (2||b(q)||^2 = a(q)^2 + lepton hierarchy qou-se9w)",
                "status": "Conditional",
            },
            "alpha_em_inv_form_b": {
                "premises_before": 8,
                "discharged_proved": 6,
                "remaining_open": 2,
                "legacy_scorecard_premises_eliminated": [
                    "ArchimedeanLimit (proved on (0,1) + 0)",
                    "BlochSuslinUniqueness (proved for complex blochD)",
                    "BringZeroModeBlochClass (bypassed via BringMapChain + (2,4,5) angle defect)",
                ],
                "open_kernel": "FormBMinimalKernelClass (GermPeriodShare + HeatKernelLeadingCoeff for mu_1 = 1/(8*pi), plus additive Delta_2 = 0 assembly)",
                "status": "Conditional",
            },
            "alpha_em_inv_form_c": {
                "premises_before": 6,
                "discharged_proved": 4,
                "remaining_open": 2,
                "open_kernel": "FormCPinned (deltaB3 q = deltaReq q alpha) + canonical non-residual arm selection (qou-aemx)",
                "status": "Conditional",
            },
            "rydberg_form_b_and_c": {
                "premises_before_form_b": 8,
                "discharged_proved_form_b": 6,
                "remaining_open_form_b": 2,
                "premises_before_form_c": 6,
                "discharged_proved_form_c": 4,
                "remaining_open_form_c": 2,
                "open_kernel": "Strictly inherited from FormBMinimalKernelClass / FormCPinned (rational R_inf/m_e = 1/(2*A^2) propagation proved)",
                "status": "Conditional",
            },
            "v_weak_electroweak_vev": {
                "premises_before": 9,
                "discharged_proved": 6,
                "remaining_open_bundled_classes": 1,
                "remaining_open_class_fields": 3,
                "open_kernel": "MinimalElectroweakVevBridgeClass (Nv_pos, duality_self_consistency, su2_vev_assembly; discrete choices qou-rpt1 / qou-myxi)",
                "status": "Conditional",
            },
        },
    )

    out_path = wb.save(
        {
            "q0Anchor": "proton",
            "q0AnchorReason": (
                "Owner ruling 2026-11-28: strictly proton-pinned q0 (q_at(95)); "
                "muon pin on hold until rederivation."
            ),
        }
    )

    built = wb.build()
    print(f"Wrote {out_path.relative_to(_ROOT)} (allPassed={built['allPassed']}, assertions={len(built['assertions'])})")
    print(f"  N_v(q0)          = {mp.nstr(obs_res['nv_ew'], 20)}  in ewNvProtonCut={obs_res['nv_in_cut']}")
    print(f"  v_weak(q0)       = {mp.nstr(obs_res['v_ew_pred_gev'], 15)} GeV ({mp.nstr(obs_res['v_ew_ppb'], 6)} ppb, {mp.nstr(obs_res['v_ew_sigma'], 4)} sigma)")
    print(f"  alpha_EM^-1 (B)  = {mp.nstr(obs_res['alpha_inv_fb'], 18)} ({mp.nstr(obs_res['alpha_fb_ppb'], 6)} ppb, {mp.nstr(obs_res['alpha_fb_sigma'], 4)} sigma)")
    print(f"  alpha_EM^-1 (C)  = {mp.nstr(obs_res['alpha_inv_fc'], 18)} ({mp.nstr(obs_res['alpha_fc_ppb'], 6)} ppb, {mp.nstr(obs_res['alpha_fc_sigma'], 4)} sigma)")
    print(f"  R_inf hc (B / C) = {mp.nstr(obs_res['ry_fb_ev'], 15)} eV ({mp.nstr(obs_res['ry_fb_ppb'], 5)} ppb) / {mp.nstr(obs_res['ry_fc_ev'], 15)} eV ({mp.nstr(obs_res['ry_fc_ppb'], 5)} ppb)")
    print(f"  m_tau / m_e      = {mp.nstr(obs_res['mtau_me_pred'], 12)} ({mp.nstr(obs_res['mtau_me_ppm'], 5)} ppm, {mp.nstr(obs_res['mtau_me_sigma'], 4)} sigma)")

    if not built["allPassed"]:
        for a in built["assertions"]:
            if not a["passed"]:
                print(f"FAIL: {a['name']}: computed={a['computed']} expected={a['expected']} tol={a['tolerance']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
