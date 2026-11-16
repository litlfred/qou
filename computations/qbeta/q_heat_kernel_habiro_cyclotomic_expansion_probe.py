#!/usr/bin/env python3
"""q_heat_kernel_habiro_cyclotomic_expansion_probe.py — Habiro / (q;q)_n cyclotomic-basis
expansion of the q-heat kernel and archimedean vs root-of-unity evaluation trichotomy.

Task: qou-8ex3 (Gap 8 under epic qou-10v9 / qou-avtq, owner ruling Q-10V9-4 = 1).
Lean companion: `QOU/QBeta/QHeatKernelHabiroExpansion.lean`.

Mathematical summary:
  1. Exact triangular change-of-basis between (1 - q)^m and the Habiro cyclotomic basis
     (q;q)_n = prod_{k=1}^n (1 - q^k):
     In terms of eps = 1 - q, 1 - q^k = eps * sum_{j=0}^{k-1} (1 - eps)^j, so
       (q;q)_n = sum_{m=n}^{n(n+1)/2} C_{n,m} * eps^m
     with lower-triangular diagonal entry C_{n,n} = n! != 0.
     Consequently, any formal power series F(q) = sum_{m >= 0} c_m * (1 - q)^m around q = 1
     has UNIQUELY determined Habiro coefficients a_n given by forward triangular elimination:
       a_0 = c_0,   a_n = (1 / n!) * (c_n - sum_{k=0}^{n-1} a_k * C_{k,n}).

  2. Exact symbolic Habiro coefficients a_n(alpha) of the heat-kernel factor
     K(q; alpha) = exp(-alpha * (q - 1)) = exp(alpha * (1 - q)) (with alpha = mu_lambda * s_*):
       a_0(alpha) = 1
       a_1(alpha) = alpha
       a_2(alpha) = alpha^2 / 4
       a_3(alpha) = alpha^2 * (2*alpha + 3) / 72
       a_4(alpha) = alpha^2 * (alpha + 3)^2 / 576
     For every truncation order N, sum_{n=0}^N a_n(alpha) * (q;q)_n matches the Taylor jet
     of exp(alpha * (1 - q)) to order O((1 - q)^{N+1}) with zero free parameters.

  3. Evaluation Trichotomy (bridging `HabiroEvaluationTrichotomy.lean`):
     - At an N-th root of unity q = zeta_N (q^N = 1): (q;q)_n = 0 for all n >= N, so the
       Habiro expansion terminates identically at n = N - 1:
         S_M(zeta_N; alpha) = S_N(zeta_N; alpha)  for all M >= N.
     - At the real archimedean substrate pin q_0 = 1.10997859... > 1:
       The growth threshold in `HabiroEvaluationTrichotomy` (`2 <= q_0^{n+1}`) is N_0 = 6
       (since q_0^6 = 1.8704 < 2 < q_0^7 = 2.0761). Thus |(q_0; q_0)_n| decreases up to
       n = 6 (minimum 0.002896) and then blows up super-exponentially like q_0^{n(n+1)/2}.
       The heat-kernel Habiro partial sum reaches its optimal truncation at N_* = 8
       (min error 6.347e-6) and then diverges to |term_30| = 6.414e10 at n = 30.
     - Under the RSZ q-Borel / reflection kernel rescale q_0^{-n(n+1)/2}:
         q_0^{-n(n+1)/2} * a_n(alpha) * (q_0; q_0)_n = (-1)^n * a_n(alpha) * (1/q_0; 1/q_0)_n,
       which removes the q_0^{n(n+1)/2} blow-up (at n = 30, |borel_term_30| = 5.443e-11).
"""
from __future__ import annotations

import datetime as _dt
from fractions import Fraction
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from _witness_q0_stamp import stamp_q0  # noqa: E402
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

# NO-FLOAT64 discipline: set compute dps before any mpf arithmetic.
set_compute_dps()
mp.mp.dps = 60

from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402

Q0_STR = _Q0_RESOLVED
Q0 = mp.mpf(Q0_STR)


def poly_mul_exact(p1: list[Fraction], p2: list[Fraction], max_deg: int) -> list[Fraction]:
    """Exact truncated polynomial multiplication in Q[eps] modulo eps^{max_deg + 1}."""
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
    """Compute the exact rational matrix C[n][m] where
    (q;q)_n = prod_{k=1}^n (1 - (1 - eps)^k) = sum_{m=0}^{n_max} C[n][m] * eps^m
    modulo eps^{n_max + 1}."""
    C: list[list[Fraction]] = []
    cur = [Fraction(0) for _ in range(n_max + 1)]
    cur[0] = Fraction(1)
    C.append(cur[:])

    # Precompute 1 - (1 - eps)^k in Q[eps]
    one_minus_eps = [Fraction(0) for _ in range(n_max + 1)]
    one_minus_eps[0] = Fraction(1)
    if n_max >= 1:
        one_minus_eps[1] = Fraction(-1)

    pow_1_minus_eps = [Fraction(0) for _ in range(n_max + 1)]
    pow_1_minus_eps[0] = Fraction(1)

    for k in range(1, n_max + 1):
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
    """Forward triangular solve for a_n in sum_{n=0}^N a_n * C[n][m] = c_eps[m]."""
    N = len(c_eps) - 1
    a = [Fraction(0) for _ in range(N + 1)]
    for m in range(N + 1):
        diag = C_mat[m][m]
        assert diag != 0, f"Zero diagonal C[{m}][{m}]"
        s = sum((a[k] * C_mat[k][m] for k in range(m)), Fraction(0))
        a[m] = (c_eps[m] - s) / diag
    return a


def qpoch_mp(q: mp.mpf | mp.mpc, n: int) -> mp.mpf | mp.mpc:
    """Exact 60-dps computation of (q;q)_n = prod_{k=1}^n (1 - q^k)."""
    out: mp.mpf | mp.mpc = mp.mpf(1)
    for k in range(1, n + 1):
        out = out * (1 - (q ** k))
    return out


def frac_to_mpf(f: Fraction) -> mp.mpf:
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)


def main() -> None:
    N_MAX = 30
    C_mat = qpoch_in_eps_coeffs(N_MAX)

    # 1. Verify lower-triangular structure C[n][m] = 0 for m < n and C[n][n] = n!
    fact = Fraction(1)
    for n in range(N_MAX + 1):
        if n > 0:
            fact *= n
        assert C_mat[n][n] == fact, f"Expected C[{n}][{n}] = {fact}, got {C_mat[n][n]}"
        for m in range(n):
            assert C_mat[n][m] == 0, f"Expected C[{n}][{m}] = 0, got {C_mat[n][m]}"

    # Verify explicit low-order polynomials in eps = 1 - q:
    # (q;q)_1 = eps
    # (q;q)_2 = 2*eps^2 - eps^3
    # (q;q)_3 = 6*eps^3 - 9*eps^4 + 5*eps^5 - eps^6
    assert C_mat[1][1] == 1 and C_mat[1][2] == 0
    assert C_mat[2][2] == 2 and C_mat[2][3] == -1 and C_mat[2][4] == 0
    assert (
        C_mat[3][3] == 6
        and C_mat[3][4] == -9
        and C_mat[3][5] == 5
        and C_mat[3][6] == -1
    )

    # 2. Compute exact rational Habiro coefficients a_n(alpha) for alpha = 1
    #    where F(q; alpha) = exp(alpha * (1 - q)) = sum_{m >= 0} (alpha^m / m!) * eps^m
    c_exp_alpha1: list[Fraction] = []
    f_m = Fraction(1)
    for m in range(N_MAX + 1):
        if m > 0:
            f_m *= m
        c_exp_alpha1.append(Fraction(1, 1) / f_m)

    a_alpha1 = solve_habiro_coeffs_from_eps_series(c_exp_alpha1, C_mat)
    # Check closed forms at alpha = 1:
    # a_0(1) = 1
    # a_1(1) = 1
    # a_2(1) = 1/4
    # a_3(1) = (2 + 3)/72 = 5/72
    # a_4(1) = 1 * 16 / 576 = 1/36
    assert a_alpha1[0] == Fraction(1, 1)
    assert a_alpha1[1] == Fraction(1, 1)
    assert a_alpha1[2] == Fraction(1, 4)
    assert a_alpha1[3] == Fraction(5, 72)
    assert a_alpha1[4] == Fraction(1, 36)

    # Also verify symbolic polynomial structure in alpha for n = 0..4 by solving at
    # alpha in {-10, -4, -2, 0, 1, 2, 4, 10} (the n=5 Wedderburn Casimir eigenvalues + 1):
    casimir_alphas = [-10, -4, -2, 0, 1, 2, 4, 10]
    casimir_rows = []
    for alpha_int in casimir_alphas:
        alpha_f = Fraction(alpha_int, 1)
        c_series: list[Fraction] = []
        fact_m = Fraction(1)
        for m in range(6):
            if m > 0:
                fact_m *= m
            c_series.append((alpha_f ** m) / fact_m)
        a_vec = solve_habiro_coeffs_from_eps_series(c_series, C_mat)
        # Check exact polynomial formulas:
        assert a_vec[0] == 1
        assert a_vec[1] == alpha_f
        assert a_vec[2] == (alpha_f ** 2) / 4
        assert a_vec[3] == (alpha_f ** 2) * (2 * alpha_f + 3) / 72
        assert a_vec[4] == (alpha_f ** 2) * ((alpha_f + 3) ** 2) / 576
        casimir_rows.append({
            "alpha": alpha_int,
            "a_0": str(a_vec[0]),
            "a_1": str(a_vec[1]),
            "a_2": str(a_vec[2]),
            "a_3": str(a_vec[3]),
            "a_4": str(a_vec[4]),
        })

    # 3. Verify root-of-unity exact truncation at q = zeta_N (N in {3, 5, 8})
    rou_rows = []
    for N_rou in (3, 5, 8):
        zeta = mp.exp(2 * mp.mpc(0, 1) * mp.pi / N_rou)
        s_N = sum(
            frac_to_mpf(a_alpha1[n]) * qpoch_mp(zeta, n) for n in range(N_rou)
        )
        s_N_plus_5 = sum(
            frac_to_mpf(a_alpha1[n]) * qpoch_mp(zeta, n) for n in range(N_rou + 5)
        )
        tail_diff = abs(s_N_plus_5 - s_N)
        assert tail_diff < mp.mpf("1e-55"), f"Root of unity tail non-zero: {tail_diff}"
        rou_rows.append({
            "N": N_rou,
            "partial_sum_N_re": fmt(mp.re(s_N)),
            "partial_sum_N_im": fmt(mp.im(s_N)),
            "tail_diff_N_to_N_plus_5": fmt(tail_diff),
        })

    # 4. Evaluate Habiro series at the real archimedean substrate pin q_0 > 1 (alpha = 1):
    #    Show optimal truncation N_* followed by super-exponential q_0^{n(n+1)/2} blow-up!
    eps0 = 1 - Q0
    exact_target_q0 = mp.exp(eps0)  # exp(-(q_0 - 1)) = exp(1 - q_0)
    qt = 1 / Q0

    arch_rows = []
    partial_sum = mp.mpf(0)
    min_err = mp.mpf("inf")
    opt_N = 0
    borel_partial_sum = mp.mpf(0)

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

        # q-Borel rescaled term: q_0^{-n(n+1)/2} * a_n * (q_0; q_0)_n = (-1)^n * a_n * (1/q_0; 1/q_0)_n
        borel_factor = Q0 ** (mp.mpf(n * (n + 1)) / 2)
        borel_term = term / borel_factor
        borel_rhs = ((-1) ** n) * a_mp * qp_qt
        assert abs(borel_term - borel_rhs) < mp.mpf("1e-52")
        borel_partial_sum += borel_term

        if n in (0, 1, 2, 3, 5, 8, 10, 12, 14, 16, 20, 25, 30):
            arch_rows.append({
                "n": n,
                "abs_a_n": fmt(abs(a_mp)),
                "abs_qpoch_q0": fmt(abs(qp_q0)),
                "abs_term": fmt(abs(term)),
                "partial_sum": fmt(partial_sum),
                "abs_error_vs_exp": fmt(err),
                "abs_borel_rescaled_term": fmt(abs(borel_term)),
            })

    # Verify asymptotic optimal truncation at q_0 followed by divergence at n = 30:
    err_at_30 = abs(partial_sum - exact_target_q0)
    term_at_30 = abs(frac_to_mpf(a_alpha1[30]) * qpoch_mp(Q0, 30))
    borel_term_at_30 = abs(
        frac_to_mpf(a_alpha1[30]) * qpoch_mp(qt, 30)
    )
    assert Q0 ** 6 < 2 and Q0 ** 7 > 2, "Expected N_0 = 6 turnaround threshold for 2 <= q_0^{n+1}"
    assert opt_N == 8 and min_err < mp.mpf("1e-5"), f"Expected opt_N=8, min_err < 1e-5, got {opt_N}, {min_err}"
    borehole_div = bool(term_at_30 > mp.mpf("1e10"))
    assert borehole_div, (
        f"Expected high-n blowup over optimal truncation: term_30={term_at_30}, min_err={min_err}"
    )
    assert borel_term_at_30 < mp.mpf("1e-10"), f"Expected Borel term < 1e-10, got {borel_term_at_30}"

    assertions = [
        {
            "name": "triangular_pochhammer_basis_verified",
            "passed": True,
            "detail": "C[n][m] = 0 for m < n and C[n][n] = n! verified exactly over Q for 0 <= n <= 30",
        },
        {
            "name": "symbolic_habiro_heat_kernel_polynomials_verified",
            "passed": True,
            "detail": (
                "a_0=1, a_1=alpha, a_2=alpha^2/4, a_3=alpha^2*(2*alpha+3)/72, "
                "a_4=alpha^2*(alpha+3)^2/576 verified across all n=5 Casimir eigenvalues"
            ),
        },
        {
            "name": "root_of_unity_exact_finite_truncation",
            "passed": all(mp.mpf(r["tail_diff_N_to_N_plus_5"]) < mp.mpf("1e-55") for r in rou_rows),
            "detail": "S_{N+5}(zeta_N) - S_N(zeta_N) = 0 to 60 dps for N in {3, 5, 8}",
        },
        {
            "name": "archimedean_q0_optimal_truncation_and_tail_growth",
            "passed": bool(opt_N == 8 and min_err < mp.mpf("1e-5") and borehole_div),
            "detail": (
                f"At q_0={mp.nstr(Q0, 12)} (turnaround N_0=6 where q_0^7=2.076>2), optimal truncation "
                f"N_*={opt_N} reaches error {mp.nstr(min_err, 6)}, while q_0^{{n(n+1)/2}} drives |term_30| up to {mp.nstr(term_at_30, 6)}"
            ),
        },
        {
            "name": "q_borel_reflection_regularization_converges",
            "passed": bool(borel_term_at_30 < mp.mpf("1e-10")),
            "detail": (
                f"q_0^{{-n(n+1)/2}} rescaled term at n=30 has magnitude {mp.nstr(borel_term_at_30, 6)} < 1e-10 "
                f"(21 orders of magnitude below unrescaled |term_30| = {mp.nstr(term_at_30, 6)})"
            ),
        },
    ]

    witness = {
        "computation": "q-heat-kernel-habiro-cyclotomic-expansion",
        "scriptFile": "q_heat_kernel_habiro_cyclotomic_expansion_probe.py",
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "bean": "qou-8ex3",
        "epic": "qou-10v9",
        "parent_epic": "qou-avtq",
        "engine": "exact Q polynomial algebra + 60-dps mpmath",
        "free_parameters": 0,
        "inputs": {
            "q0": Q0_STR,
            "q0_pin": "proton (experimental pin, resolved)",
            "inv_q0": fmt(qt),
            "eps0_one_minus_q0": fmt(eps0),
            "n_max": N_MAX,
            "casimir_alphas_n5": casimir_alphas,
            "arithmetic": f"Exact Q[eps] triangular elimination + mpmath at {mp.mp.dps} dps (no float64)",
        },
        "results": {
            "low_order_qpoch_in_eps": {
                "qPoch_0": "1",
                "qPoch_1": "eps",
                "qPoch_2": "2*eps^2 - eps^3",
                "qPoch_3": "6*eps^3 - 9*eps^4 + 5*eps^5 - eps^6",
            },
            "symbolic_habiro_coefficients_of_exp_alpha_eps": {
                "a_0": "1",
                "a_1": "alpha",
                "a_2": "alpha^2 / 4",
                "a_3": "alpha^2 * (2*alpha + 3) / 72",
                "a_4": "alpha^2 * (alpha + 3)^2 / 576",
            },
            "casimir_table_n5": casimir_rows,
            "root_of_unity_truncation_table": rou_rows,
            "archimedean_q0_evaluation": {
                "exact_exp_one_minus_q0": fmt(exact_target_q0),
                "optimal_truncation_N_star": opt_N,
                "min_truncation_error_at_q0": fmt(min_err),
                "abs_term_at_n30": fmt(term_at_30),
                "abs_error_at_n30": fmt(err_at_30),
                "q_borel_regularized_sum": fmt(borel_partial_sum),
                "q_borel_abs_term_at_n30": fmt(borel_term_at_30),
                "profile_rows": arch_rows,
            },
        },
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
        "verdict": (
            "EXACT TRIANGULAR HABIRO EXPANSION & ARCHIMEDEAN TRICHOTOMY VERIFIED: "
            "(1) Because (q;q)_n = n! * (1-q)^n + O((1-q)^{n+1}) is lower-triangular with "
            "non-zero diagonal n!, every formal power series around q=1 has uniquely determined "
            "Habiro coefficients a_n; for the heat kernel exp(-alpha*(q-1)), a_0=1, a_1=alpha, "
            "a_2=alpha^2/4, a_3=alpha^2*(2*alpha+3)/72, a_4=alpha^2*(alpha+3)^2/576. "
            "(2) At any primitive N-th root of unity zeta_N, (zeta_N;zeta_N)_n = 0 for all n >= N, "
            "so the Habiro expansion terminates identically at n = N - 1. "
            "(3) At the real archimedean substrate pin q_0 = 1.10997859... > 1, the reflection "
            "identity (q_0;q_0)_n = (-1)^n q_0^{n(n+1)/2} (1/q_0;1/q_0)_n injects the super-exponential "
            "factor q_0^{n(n+1)/2} (with turnaround threshold N_0 = 6 where q_0^7 = 2.076 > 2): "
            "the series reaches an optimal truncation accuracy of 6.35e-6 at N_* = 8 and then "
            "diverges super-exponentially to |term_30| = 6.414e10, whereas dividing by the RSZ q-Borel "
            "kernel q_0^{n(n+1)/2} maps termwise to the convergent bar-partner series (-1)^n a_n (1/q_0;1/q_0)_n "
            "(|borel_term_30| = 5.443e-11)."
        ),
        "lean": "QOU.QBeta.QHeatKernelHabiroExpansion",
        "wired": False,
    }

    stamp_q0(witness, __file__)

    out_path = os.path.join(
        os.path.dirname(__file__), "q-heat-kernel-habiro-cyclotomic-expansion.witness.json"
    )
    with open(out_path, "w", encoding="utf-8") as fh:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False
        )
        json.dump(witness, fh, indent=2)
        fh.write("\n")

    print(f"exact exp(1 - q_0) = {mp.nstr(exact_target_q0, 20)}")
    print(f"optimal truncation N_* = {opt_N}, min_err = {mp.nstr(min_err, 6)}")
    print(f"abs_term(n=30) = {mp.nstr(term_at_30, 6)}, borel_term(n=30) = {mp.nstr(borel_term_at_30, 6)}")
    print(f"wrote {out_path}")
    print("ALL ASSERTIONS PASS")


if __name__ == "__main__":
    main()
