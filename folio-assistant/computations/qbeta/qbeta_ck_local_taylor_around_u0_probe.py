#!/usr/bin/env python3
"""qbeta_ck_local_taylor_around_u0_probe.py — extract c_k via local
Taylor of R(u) around u_0 (substrate), follow-up to PR #1875.

PR #1875's headline ("u-Taylor c_k STRUCTURALLY IMPOSSIBLE") only
holds at u=0 (the classical limit q=1) — the sqrt-branch obstruction.
At the SUBSTRATE u_0 ~ 0.00852, du/dt = 0.1398 is finite nonzero, so
the local series reversion IS well-defined. PR #1875's probe even
computes the local Taylor coefficients of tr_M in dv = u - u_0, but
then concludes the c_k can't be read off them. This is overstated.

This probe extracts c_2..c_8 via NONLINEAR MATCHING of the local
Taylor of R(u) := tr_M(trefoil)(q(u)) / [Q_A(q(u)) cos(alpha_eff(q(u)))]
against the ladder R(u) = Q_base * Prod_k(1 + c_k u^k).

**The method:**

  1. Compute the local Taylor of R(u) around u_0 to order N (= 8).
  2. Compute the local Taylor of log(R(u)/R(u_0)) around u_0.
  3. The ladder gives:
        log R(u) - log R(u_0) = sum_k [log(1+c_k u^k) - log(1+c_k u_0^k)]
     Expand each log around u = u_0; the n-th derivative at u_0 is a
     RATIONAL FUNCTION of u_0 and {c_k for k <= n}.
  4. Match Taylor coefficients order-by-order to solve for c_k (sympy
     nsolve on the resulting nonlinear system, starting from c_2 = -1
     and c_k near zero for k >= 3).

**The gate:** c_2 must come out close to -1 (PR #1786 canonical) for
the operator-Markov route to be confirmed as the c_k generating source.

**Honest caveat:** the local Taylor coefficients of tr_M grow rapidly
([dv^3] ~ 5e3, [dv^8] ~ -2e13 from PR #1875 probe output), suggesting
the local radius of convergence is small — likely a pole or branch
point near u_0. If the c_k system is ill-conditioned, this would be
the diagnostic.
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 50
import sympy as sp  # noqa: E402

from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-ck-local-taylor-around-u0-probe",
        engine="python+sympy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Extracts c_2..c_8 via local Taylor of R(u) around substrate "
        "u_0 ~ 0.00852 (where du/dt = 0.1398, NOT a branch point). "
        "Nonlinearly matches R(u_0+dv) against Q_base * Prod_k(1+c_k u^k). "
        "Gate: c_2 ~ -1 (PR #1786 canonical). Follow-up to PR #1875, "
        "which correctly proved u=0 ladder impossible but overstated "
        "the scope (u_0 ladder IS well-defined)."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    q = sp.Symbol("q", positive=True)

    print("=" * 78)
    print(" c_2..c_8 from local Taylor of R(u) around substrate u_0")
    print("=" * 78)
    print()

    # PR #1873 closed forms (validated)
    chi_3 = q ** 3
    chi_21 = sp.Integer(0)
    chi_111 = -1 / q ** 3

    # Wenzl weights y_lambda symbolic
    def to_q_expr(y):
        return y if isinstance(y, sp.Expr) else sp.sympify(y)

    y_3 = to_q_expr(y_lambda_wenzl_bridge_symbolic((3,)))
    y_21 = to_q_expr(y_lambda_wenzl_bridge_symbolic((2, 1)))
    y_111 = to_q_expr(y_lambda_wenzl_bridge_symbolic((1, 1, 1)))

    # Markov trace of trefoil
    tr_M = sp.simplify(y_3 * chi_3 + y_21 * chi_21 + y_111 * chi_111)

    # Substrate chain (PR #1786)
    h_qq = q - 1 / q
    z_qq = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
    alpha = (z_qq - 1) * h_qq / 2
    b_sub = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
    hbar = (q - 1) / q
    alpha_eff = alpha - b_sub * hbar ** 2 / 2
    u_q = b_sub * hbar ** 2
    Q_A_over_me = (2 * q + 1 - q ** 2) * (q + 1) / (2 * q ** 3)

    # The ratio R(q): the Q_β / [Q_A · cos(α_eff)] ladder target
    R_q = tr_M / (Q_A_over_me * sp.cos(alpha_eff))

    # Substrate point
    Q0_str = "1.1099785827513808075916690956107688798744991218736"
    q0_sp = sp.Float(Q0_str, 50)
    u0_val = sp.N(u_q.subs(q, q0_sp), 50)
    R_at_q0 = sp.N(R_q.subs(q, q0_sp), 50)

    print(f"  Substrate values (q_0 = {Q0_str[:25]}...):")
    print(f"    u_0      = {u0_val}")
    print(f"    R(u_0)   = {R_at_q0}")
    print(f"    tr_M(q_0)= {sp.N(tr_M.subs(q, q0_sp), 30)}")
    print()

    # Build local Taylor of R in t = q - q_0, then revert u(t) -> t(u-u_0)
    NMAX = 8
    NSERIES = NMAX + 2
    t = sp.Symbol("t")
    print(f"  Building local Taylor of R(q_0 + t) and u(q_0 + t) to order {NMAX+1}...")
    R_t_series = sp.series(R_q.subs(q, q0_sp + t), t, 0, NSERIES).removeO()
    u_t_series = sp.series(u_q.subs(q, q0_sp + t), t, 0, NSERIES).removeO()
    print(f"    done.")
    print()

    u0_const = u_t_series.subs(t, 0)
    a1 = u_t_series.coeff(t, 1)
    a1_mag = mp.fabs(mp.mpf(str(sp.N(a1, 50))))
    print(f"  u(q_0) const  = {sp.N(u0_const, 25)}")
    print(f"  du/dt at q_0  = {sp.N(a1, 25)}")
    print(f"  |a1| numeric  = {float(a1_mag):.3e}")
    if a1_mag < mp.mpf("1e-30"):
        print(f"  ✗ a1 effectively zero — local reversion not possible here.")
        return 0
    print()

    # Series reversion: t(dv) where dv = u - u_0
    print(f"  Reverting u(t) -> t(dv) where dv = u - u_0...")
    bs = [sp.Integer(0)] * (NSERIES + 2)
    bs[1] = 1 / a1
    dv = sp.Symbol("dv")
    du = sp.expand(u_t_series - u0_const)
    for n in range(2, NSERIES):
        t_pow = sum(bs[i] * dv ** i for i in range(1, n))
        comp = sp.series(sum(du.coeff(t, j) * t_pow ** j
                              for j in range(1, n + 1)),
                          dv, 0, n + 1).removeO()
        cn = comp.coeff(dv, n)
        bs[n] = sp.simplify(-cn / a1)
    t_of_dv = sum(bs[i] * dv ** i for i in range(1, NSERIES))
    print(f"    done.")
    print()

    # R(u_0 + dv) = R(q_0 + t(dv)), expand in dv
    print(f"  Composing R(q_0 + t(dv)) and expanding in dv to order {NMAX}...")
    R_dv = sp.series(R_t_series.subs(t, t_of_dv), dv, 0, NMAX + 1).removeO()
    R_dv_coeffs = [sp.N(R_dv.coeff(dv, k), 50) for k in range(NMAX + 1)]
    print()
    print(f"  R(u_0 + dv) local Taylor coefficients:")
    for k, c in enumerate(R_dv_coeffs):
        print(f"    [dv^{k}] = {sp.N(c, 18)}")
    print()

    # Convert R-coeffs to mpmath for the nonlinear solve
    R_taylor_mp = [mp.mpf(str(c)) for c in R_dv_coeffs]
    R0 = R_taylor_mp[0]
    u0_mp = mp.mpf(str(u0_val))
    print(f"  Working precision: dps = {mp.mp.dps}")
    print(f"  R(u_0) = R_taylor[0] = {R0}")
    print(f"  u_0    = {u0_mp}")
    print()

    # ---- Nonlinear matching ----
    # Ladder model: R(u) = Q_base * Prod_{k=2..NMAX} (1 + c_k * u^k)
    # log R(u) = log Q_base + sum_k log(1 + c_k * u^k)
    # n-th derivative of log R at u_0:
    #   d^n/du^n log R |_{u_0} = sum_k d^n/du^n log(1 + c_k * u^k) |_{u_0}
    # This = (n-th Taylor coeff of log R around u_0) * n!.
    # We'll match log R Taylor coefficients directly.
    #
    # Build log R(u_0+dv) Taylor symbolically in mpmath via R_taylor_mp.
    # Then for each candidate c-vector, compute the ladder Taylor and
    # solve via Newton iteration.

    def taylor_log_from_taylor(R_coeffs):
        """Given Taylor of R(u_0+dv) in dv, return Taylor of log R(u_0+dv)."""
        N = len(R_coeffs) - 1
        # log R(u_0+dv) = log(R0) + log(1 + sum_{k>=1} (R_k/R0) dv^k)
        ratios = [R_coeffs[k] / R_coeffs[0] for k in range(N + 1)]
        # Series of log(1 + x) where x = sum_{k>=1} ratios[k] dv^k
        log_coeffs = [mp.log(R_coeffs[0])] + [mp.mpf("0")] * N
        # We use the recursion: if f = log(1+x), then f' = x'/(1+x),
        # i.e. (1+x) f' = x'. Coefficients: for n >= 1,
        # n*log_n + sum_{j=1}^{n-1} (n-j)*ratios[j]*log_{n-j} = n*ratios[n]
        # i.e. log_n = ratios[n] - sum_{j=1}^{n-1} ((n-j)/n)*ratios[j]*log_{n-j}
        for n in range(1, N + 1):
            s = ratios[n]
            for j in range(1, n):
                s -= mp.mpf(n - j) / mp.mpf(n) * ratios[j] * log_coeffs[n - j]
            log_coeffs[n] = s
        return log_coeffs

    logR_taylor = taylor_log_from_taylor(R_taylor_mp)
    print(f"  log R(u_0 + dv) Taylor coefficients (mpmath):")
    for k, c in enumerate(logR_taylor):
        print(f"    [dv^{k}] = {mp.nstr(c, 18)}")
    print()

    # Ladder model log Taylor: log R(u) = log Q_base + sum_k log(1+c_k u^k)
    # At u = u_0 + dv:
    #   log(1+c_k (u_0+dv)^k) = log(1 + c_k * (u_0 + dv)^k)
    # Expand (u_0+dv)^k in dv: sum_{j=0..k} C(k,j) u_0^(k-j) dv^j
    # Then we have x_k(dv) = c_k * (u_0+dv)^k, and want log(1+x_k(dv)) Taylor.

    def ladder_log_taylor(c_vec, N):
        """Compute Taylor of log Prod_{k=2..K} (1+c_k (u_0+dv)^k) in dv to order N.
        c_vec[i] = c_{i+2}, i.e. c_vec = [c_2, c_3, ..., c_K]."""
        K = len(c_vec) + 1  # max c-index
        # Total log Taylor accumulator
        total = [mp.mpf("0")] * (N + 1)
        for k in range(2, K + 1):
            ck = c_vec[k - 2]
            # x_k(dv) = ck * (u_0 + dv)^k Taylor in dv to order N
            xk = [mp.mpf("0")] * (N + 1)
            for j in range(0, min(k, N) + 1):
                xk[j] = ck * mp.binomial(k, j) * u0_mp ** (k - j)
            # log(1+xk) Taylor (xk is already a Taylor in dv).
            # Use same recursion as above but for series 1 + xk:
            # f = log(1+x), f' = x'/(1+x), (1+x) f' = x'
            # n*f_n + sum_{j=1}^{n-1} (n-j) xk[j] f_{n-j} = n*xk[n]  if x_0=0
            # But xk[0] = ck * u_0^k may be NONZERO. So use general form:
            # f(dv) = log(1 + xk(dv))
            # Let g(dv) = 1 + xk(dv). f = log g.
            # g f' = g'. f_n = g'_n/g_0 - sum_{j=1}^{n-1} (j/n) f_j (g_{n-j}/g_0)?
            # Cleaner: let h = g/g_0 = 1 + h_tilde where h_tilde = (xk - xk[0])/(1+xk[0]).
            # Then log g = log g_0 + log h, and log h with h_tilde[0] = 0 uses
            # the simple recursion.
            g0 = mp.mpf("1") + xk[0]
            if abs(g0) < mp.mpf("1e-40"):
                raise ValueError(f"ladder degenerate at k={k}, c_k={ck}: 1+c_k*u_0^k ~ 0")
            h_tilde = [mp.mpf("0")] * (N + 1)
            for j in range(1, N + 1):
                h_tilde[j] = xk[j] / g0
            log_h = [mp.mpf("0")] * (N + 1)
            for n in range(1, N + 1):
                s = h_tilde[n]
                for jj in range(1, n):
                    s -= mp.mpf(n - jj) / mp.mpf(n) * h_tilde[jj] * log_h[n - jj]
                log_h[n] = s
            # add log g_0 to constant
            total[0] += mp.log(g0)
            for j in range(1, N + 1):
                total[j] += log_h[j]
        return total

    # ---- The matching system ----
    # Unknowns: log Q_base + c_2, c_3, ..., c_NMAX
    # Equations: log R Taylor coeffs at orders 0..NMAX (NMAX+1 equations)
    # Strategy: subtract Q_base from the constant. Then we have NMAX
    # unknowns (c_2..c_NMAX) and NMAX equations (orders 1..NMAX).

    def residuals(c_vec_list):
        """Residual = ladder_log_taylor[1..N] - logR_taylor[1..N] (skip order 0)."""
        c_vec = [mp.mpf(str(x)) for x in c_vec_list]
        try:
            ladder = ladder_log_taylor(c_vec, NMAX)
        except ValueError:
            return [mp.mpf("1e10")] * NMAX  # blown up
        return [ladder[j] - logR_taylor[j] for j in range(1, NMAX + 1)]

    # Initial guess: c_2 = -1, c_3..c_8 = 0
    c0 = [mp.mpf("-1.0")] + [mp.mpf("0.0")] * (NMAX - 2)
    print(f"  Initial guess: c_2 = -1, c_3..c_{NMAX} = 0")
    print(f"  Initial residuals (orders 1..{NMAX}):")
    init_res = residuals(c0)
    for j, r in enumerate(init_res):
        print(f"    order {j+1}: residual = {mp.nstr(r, 12)}")
    print()

    # Use mpmath findroot with Newton iteration
    print(f"  Running mpmath findroot (multidimensional Newton)...")
    try:
        sol = mp.findroot(residuals, c0, solver="mnewton", tol=mp.mpf("1e-30"),
                          maxsteps=100, verify=False)
        sol_list = [mp.mpf(str(sol[i])) for i in range(NMAX - 1)]
        print(f"  Solver converged.")
        print()
        print(f"  Extracted c_k:")
        for i, ck in enumerate(sol_list):
            print(f"    c_{i+2} = {mp.nstr(ck, 25)}")
        print()
        final_res = residuals(sol_list)
        print(f"  Final residuals:")
        for j, r in enumerate(final_res):
            print(f"    order {j+1}: residual = {mp.nstr(r, 12)}")
        print()
        max_res = max(mp.fabs(r) for r in final_res)
        print(f"  Max residual: {mp.nstr(max_res, 6)}")
        print()

        # Gate: c_2 = -1
        c2_extracted = sol_list[0]
        c2_canonical = mp.mpf("-1.0")
        c2_err = mp.fabs(c2_extracted - c2_canonical)
        c2_match = c2_err < mp.mpf("1e-6")

        print("=" * 78)
        print(" VERDICT")
        print("=" * 78)
        print()
        print(f"  c_2 gate (canonical = -1, PR #1786):")
        print(f"    extracted c_2 = {mp.nstr(c2_extracted, 20)}")
        print(f"    |c_2 - (-1)|  = {mp.nstr(c2_err, 12)}")
        print(f"    GATE: {'✓ PASS' if c2_match else '✗ FAIL'} "
              f"(threshold 1e-6)")
        print()

        if c2_match:
            print(f"  ✓ The local Taylor of R(u) around u_0 IS consistent")
            print(f"    with the canonical ladder Prod_k(1+c_k u^k); c_2 = -1")
            print(f"    confirms the operator-Markov route is the canonical")
            print(f"    c_k source.")
            print(f"  ✓ Extracted c_3..c_8 are NEW DATA — no prior canonical.")
            print(f"    Cross-anchor stability test (run at q_p vs q_μ) is the")
            print(f"    follow-up to verify per-anchor consistency.")
        else:
            print(f"  ✗ c_2 does NOT match the canonical -1 — diagnostic possibilities:")
            print(f"    (i)   Normalization mismatch (Q_base absorbs a q-dependent factor)")
            print(f"    (ii)  Local Taylor has limited radius (next pole near u_0)")
            print(f"    (iii) Ladder ansatz Prod_k(1+c_k u^k) needs an additional")
            print(f"          factor like the cos(alpha_eff) we've already divided")
            print(f"          out, or a phase / sign")
            print(f"    (iv)  Series reversion truncation error at order {NMAX}+1")

        builder.add_data("u_0", str(u0_mp))
        builder.add_data("R_at_u_0", str(R0))
        builder.add_data("R_taylor_around_u_0", [str(c) for c in R_taylor_mp])
        builder.add_data("logR_taylor_around_u_0", [str(c) for c in logR_taylor])
        builder.add_data("c_extracted", {f"c_{i+2}": str(c) for i, c in enumerate(sol_list)})
        builder.add_data("max_residual", str(max_res))
        builder.add_data("c_2_gate", {
            "extracted": str(c2_extracted),
            "canonical": "-1.0",
            "error": str(c2_err),
            "passed": bool(c2_match),
        })
        builder.add_assertion(
            "c_2_matches_canonical_minus_one",
            computed=1 if c2_match else 0,
            expected=1,
            tolerance=0,
            source=("Gate: the c_2 extracted from local Taylor of R(u) "
                    "around substrate u_0 must equal PR #1786's canonical "
                    "structural c_2 = -1 (from the (1-u^2) factor at N=2). "
                    "PASS confirms the operator-Markov route is the canonical "
                    "c_k generating source; FAIL diagnoses a normalization "
                    "mismatch or limited local radius of convergence."),
        )

    except Exception as exc:
        print(f"  Solver failed: {exc}")
        builder.add_data("solver_failure", str(exc))
        builder.add_assertion(
            "c_2_matches_canonical_minus_one",
            computed=0, expected=1, tolerance=0,
            source=f"Solver failed with: {exc}",
        )

    builder.save()
    print(f"  Witness: qbeta-ck-local-taylor-around-u0-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
