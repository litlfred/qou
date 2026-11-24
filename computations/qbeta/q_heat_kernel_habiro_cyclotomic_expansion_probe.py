#!/usr/bin/env python3
"""q_heat_kernel_habiro_cyclotomic_expansion_probe.py — Habiro / (q;q)_n cyclotomic-basis
expansion of the q-heat kernel and archimedean vs root-of-unity evaluation trichotomy.

Task: qou-8ex3 (salvaged from PR #8144).
Lean companion: `QOU/QBeta/QHeatKernelHabiroExpansion.lean`.
Precision: 80-dps mpmath + exact rational Q[eps] elimination, zero float64, zero fitting.
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction
from pathlib import Path

THIS = Path(__file__).resolve()
ROOT = THIS.parents[2]
for _rel in (
    "computations",
    "computations/substrate",
    "tools/qou-substrate/python",
    "schemas/witness-schema/python",
):
    if str(ROOT / _rel) not in sys.path:
        sys.path.insert(0, str(ROOT / _rel))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

DPS = 80
set_compute_dps(DPS)
mp.mp.dps = DPS

Q0_STR = Q_50_DIGIT_STR
Q0 = mp.mpf(Q0_STR)


def poly_mul_exact(
    p1: list[Fraction], p2: list[Fraction], max_deg: int
) -> list[Fraction]:
    out = [Fraction(0) for _ in range(max_deg + 1)]
    for i, c1 in enumerate(p1):
        if c1 == 0 or i > max_deg:
            continue
        for j, c2 in enumerate(p2):
            if c2 == 0 or i + j > max_deg:
                continue
            out[i + j] += c1 * c2
    return out


def qpoch_in_eps_coeffs(n_max: int) -> list[list[Fraction]]:
    C: list[list[Fraction]] = []
    cur = [Fraction(0) for _ in range(n_max + 1)]
    cur[0] = Fraction(1)
    C.append(cur[:])

    one_minus_eps = [Fraction(0) for _ in range(n_max + 1)]
    one_minus_eps[0] = Fraction(1)
    if n_max >= 1:
        one_minus_eps[1] = Fraction(-1)

    pow_1_minus_eps = [Fraction(0) for _ in range(n_max + 1)]
    pow_1_minus_eps[0] = Fraction(1)

    for _k in range(1, n_max + 1):
        pow_1_minus_eps = poly_mul_exact(pow_1_minus_eps, one_minus_eps, n_max)
        factor_k = [Fraction(0) for _ in range(n_max + 1)]
        factor_k[0] = Fraction(1) - pow_1_minus_eps[0]
        for m in range(1, n_max + 1):
            factor_k[m] = -pow_1_minus_eps[m]
        cur = poly_mul_exact(cur, factor_k, n_max)
        C.append(cur[:])
    return C


def solve_habiro_coeffs_from_eps_series(
    c_eps: list[Fraction], C_mat: list[list[Fraction]]
) -> list[Fraction]:
    N = len(c_eps) - 1
    a = [Fraction(0) for _ in range(N + 1)]
    for m in range(N + 1):
        diag = C_mat[m][m]
        assert diag != 0
        s = sum((a[k] * C_mat[k][m] for k in range(m)), Fraction(0))
        a[m] = (c_eps[m] - s) / diag
    return a


def qpoch_mp(q: mp.mpf | mp.mpc, n: int) -> mp.mpf | mp.mpc:
    out: mp.mpf | mp.mpc = mp.mpf(1)
    for k in range(1, n + 1):
        out = out * (1 - (q**k))
    return out


def frac_to_mpf(f: Fraction) -> mp.mpf:
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)


def main() -> int:
    t0 = time.time()
    set_compute_dps(DPS)
    mp.mp.dps = DPS

    N_MAX = 30
    C_mat = qpoch_in_eps_coeffs(N_MAX)

    tri_ok = True
    fact = Fraction(1)
    for n in range(N_MAX + 1):
        if n > 0:
            fact *= n
        if C_mat[n][n] != fact or any(C_mat[n][m] != 0 for m in range(n)):
            tri_ok = False

    c_exp_alpha1: list[Fraction] = []
    f_m = Fraction(1)
    for m in range(N_MAX + 1):
        if m > 0:
            f_m *= m
        c_exp_alpha1.append(Fraction(1, 1) / f_m)

    a_alpha1 = solve_habiro_coeffs_from_eps_series(c_exp_alpha1, C_mat)
    casimir_alphas = [-10, -4, -2, 0, 1, 2, 4, 10]
    poly_ok = True
    for alpha_int in casimir_alphas:
        alpha_f = Fraction(alpha_int, 1)
        c_series: list[Fraction] = []
        fact_m = Fraction(1)
        for m in range(6):
            if m > 0:
                fact_m *= m
            c_series.append((alpha_f**m) / fact_m)
        a_vec = solve_habiro_coeffs_from_eps_series(c_series, C_mat)
        if not (
            a_vec[0] == 1
            and a_vec[1] == alpha_f
            and a_vec[2] == (alpha_f**2) / 4
            and a_vec[3] == (alpha_f**2) * (2 * alpha_f + 3) / 72
            and a_vec[4] == (alpha_f**2) * ((alpha_f + 3) ** 2) / 576
        ):
            poly_ok = False

    rou_ok = True
    for N_rou in (3, 5, 8):
        zeta = mp.exp(2 * mp.mpc(0, 1) * mp.pi / N_rou)
        s_N = sum(frac_to_mpf(a_alpha1[n]) * qpoch_mp(zeta, n) for n in range(N_rou))
        s_N_plus_5 = sum(
            frac_to_mpf(a_alpha1[n]) * qpoch_mp(zeta, n) for n in range(N_rou + 5)
        )
        if abs(s_N_plus_5 - s_N) >= mp.mpf("1e-70"):
            rou_ok = False

    eps0 = 1 - Q0
    exact_target_q0 = mp.exp(eps0)
    qt = 1 / Q0

    partial_sum = mp.mpf(0)
    min_err = mp.mpf("inf")
    opt_N = 0
    borel_ok = True

    for n in range(N_MAX + 1):
        qp_q0 = qpoch_mp(Q0, n)
        qp_qt = qpoch_mp(qt, n)
        a_mp = frac_to_mpf(a_alpha1[n])
        term = a_mp * qp_q0
        partial_sum += term
        err = abs(partial_sum - exact_target_q0)
        if err < min_err:
            min_err = err
            opt_N = n
        borel_factor = Q0 ** (mp.mpf(n * (n + 1)) / 2)
        borel_term = term / borel_factor
        borel_rhs = ((-1) ** n) * a_mp * qp_qt
        if abs(borel_term - borel_rhs) >= mp.mpf("1e-65"):
            borel_ok = False

    term_at_30 = abs(frac_to_mpf(a_alpha1[30]) * qpoch_mp(Q0, 30))
    borel_term_at_30 = abs(frac_to_mpf(a_alpha1[30]) * qpoch_mp(qt, 30))

    wb = WitnessBuilder(
        "q-heat-kernel-habiro-cyclotomic-expansion",
        engine="mpmath",
        output_dir=THIS.parent,
        start_time=t0,
    )
    wb.set_description(
        "80-dps mpmath + exact Q[eps] verification of the Habiro cyclotomic-basis "
        "expansion of exp(-alpha*(q-1)), root-of-unity finite termination, and "
        "archimedean q_0 > 1 optimal truncation vs q-Borel reflection regularization (qou-8ex3)."
    )
    wb.add_parameter("workdps", DPS)
    wb.add_parameter("q0", Q0_STR)
    wb.add_data(
        "archimedean_evaluation",
        {
            "exact_exp_one_minus_q0": fmt(exact_target_q0, 50),
            "optimal_truncation_N_star": opt_N,
            "min_truncation_error_at_q0": fmt(min_err, 30),
            "abs_term_at_n30": fmt(term_at_30, 30),
            "q_borel_abs_term_at_n30": fmt(borel_term_at_30, 30),
        },
    )

    wb.add_assertion(
        "triangular_pochhammer_and_symbolic_habiro_polynomials",
        computed=bool(tri_ok and poly_ok),
        expected=True,
        source="QOU.QBeta.QHeatKernelHabiroExpansion.triangular_solve_order3_unique",
    )
    wb.add_assertion(
        "root_of_unity_exact_finite_truncation",
        computed=rou_ok,
        expected=True,
        source="QOU.QBeta.QHeatKernelHabiroExpansion.habiroPartialSum_eq_of_pow_eq_one",
    )
    wb.add_assertion(
        "archimedean_q0_optimal_truncation_and_tail_growth",
        computed=bool(
            Q0**6 < 2
            and Q0**7 > 2
            and opt_N == 8
            and min_err < mp.mpf("1e-5")
            and term_at_30 > mp.mpf("1e10")
        ),
        expected=True,
        source="QOU.QBeta.QHeatKernelHabiroExpansion.habiroTerm_abs_ge_of_one_lt",
    )
    wb.add_assertion(
        "q_borel_reflection_regularization_converges",
        computed=bool(borel_ok and borel_term_at_30 < mp.mpf("1e-10")),
        expected=True,
        source="QOU.QBeta.QHeatKernelHabiroExpansion.habiroTerm_reflection",
    )

    out_path = wb.save({"q0Anchor": "proton", "q0Value": Q0_STR})
    print(f"Saved witness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
