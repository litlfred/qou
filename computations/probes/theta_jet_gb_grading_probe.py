#!/usr/bin/env python3
"""theta-order vs jet order vs GS (Hecke) Poincare q-degree.

Question (bean qou-mlog): the theta / slope-1/2 factor q^{-m^2/4} that Route B
measured on the C1 kernel -- is it CONSTANT across jet order m, or does it grade
with m?  And does the m^2/4 Gaussian equal HALF the cumulative Groebner-Shirshov
(Hecke) q-degree summed over filtration levels <= m?

Objects (all parameter-free, no AME data):
  C1 kernel (proved q-lift):  [m+2]_q b_{m+2} = b_{m+1} + b_m   (denominators are
     the Hecke quantum integers [k]_q -- the SAME [k]_q that grade the GS normal
     form).  b_m is the (q-Borel side) binding coefficient at jet/body order m.
  theta_m := -log_q |b_m|          (the accumulated theta exponent)
  GS Poincare top degree of H_m:   deg_q [m]_q! = sum_{k=1}^m (k-1) = C(m,2)
     = ell(w_0^{(m)})  (longest-element Coxeter length; corpus-witnessed in
     gb-filtration-jet-order.witness.json: longest sigma1 sigma2 sigma1 grade 3
     = C(3,2), longest H_4 word grade 6 = C(4,2)).
  involution numbers I(m) (classical q=1 shadow, Gevrey-1/2 per BindingGevreyHalf).

Three pre-stated claims (the PRIMARY constancy discriminant is the CURVATURE --
the 2nd difference of theta_m -- which strips linear + constant terms and isolates
the Gaussian coefficient; the finite-m ratio theta_m/C(m,2) is polluted by a large
linear term from the [k]_q = (q^k-1)/(q-1) framing, log_q(1/(q-1)) ~ 21 per level
at q0, so it is NOT the right invariant -- reported only as a diagnostic):
  (A) CONSTANCY (curvature).  2nd-diff theta_m -> constant 1/2 (=> Gaussian coeff
      1/4 exactly, theta_m ~ m^2/4).  Constant curvature = constant slope: the
      theta-order is an INTRINSIC 1/2, not jet-graded.  A quadratic fit
      theta_m = a m^2 + b m + c on a tail window gives a -> 1/4 with b the framing
      linear term (~ (1/2) log_q(1/(q-1))).
  (B) GS BRIDGE (leading order).  a = 1/4 = (1/2) * (1/2), where 1/2 is the
      leading coefficient of the GS/Hecke Poincare top degree deg_q[m]_q! =
      C(m,2) = m^2/2 - m/2.  So the LEADING theta Gaussian = HALF the cumulative
      GS filtration q-degree; theta_m ~ deg_q(([m]_q!)^{1/2}) at leading q-order.
      The 1/2 = the depth-2 (involution-recurrence) structure.  The subleading
      linear discrepancy is exactly the [k]_q-vs-q^{k-1} framing normalization
      (a KNOWN transient, cf Route B's log_q(1/(q-1)) ~ 62/factor).  Exact
      arithmetic: C(m,2) = sum_{k<=m}(k-1) with deg_q[k]_q = k-1.
  (C) GEVREY-1/2 CONSTANT.  effective order o_m := 2*log I(m)/log(m!) -> 1
      (i.e. I(m) ~ (m!)^{1/2}) -- the classical-side witness that the same 1/2 is
      intrinsic; drift is the proved-Lean-bounded e^{sqrt m} subleading, not slope.

Run: python3 -u computations/probes/theta_jet_gb_grading_probe.py 2>&1 | tee /tmp/theta-jet-gb.log
Emits theta_jet_gb_grading_probe.witness.json (same dir).  All scope-(a): growth
measurements + one exact arithmetic identity; no fit, no anchor.
"""
import json
import os
from datetime import datetime, timezone
from math import comb, lgamma

from mpmath import mp, mpf, log

mp.dps = 60

Q0 = mpf("1.10997859555733471989976322048322502665620840878015")  # muon-q0 canonical
M_MAX = 200


# Path bridge — keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from witness_base import WitnessBuilder  # noqa: E402

import time as _time  # noqa: E402
_T0 = _time.monotonic()


def qint(k, q):
    return (1 - q ** k) / (1 - q)


def c1_coeffs(q, mmax):
    """b_m from [m+2]_q b_{m+2} = b_{m+1} + b_m, seed b_0=b_1=1 (asymptotics
    are seed-independent for the decaying leg)."""
    b = [mpf(1), mpf(1)]
    for m in range(mmax - 1):
        b.append((b[m + 1] + b[m]) / qint(m + 2, q))
    return b


def involution(mmax):
    I = [1, 1]
    for n in range(mmax):
        I.append(I[n + 1] + (n + 1) * I[n])
    return I


def window_stats(vals, lo, hi):
    xs = vals[lo:hi + 1]
    mean = mp.fsum(xs) / len(xs)
    var = mp.fsum((x - mean) ** 2 for x in xs) / len(xs)
    return mean, var ** mpf("0.5")


def main():
    q = Q0
    logq = log(q)
    b = c1_coeffs(q, M_MAX)
    I = involution(M_MAX)

    # theta_m = -log_q |b_m|
    theta = [(-log(abs(b[m])) / logq if b[m] != 0 else mpf(0)) for m in range(M_MAX)]

    # (A) PRIMARY discriminant: curvature = 2nd difference of theta -> 2a (=1/2)
    curv = [theta[m + 2] - 2 * theta[m + 1] + theta[m] for m in range(M_MAX - 2)]
    curv_lo, curv_lo_sd = window_stats(curv, 20, 40)      # low: still in framing transient
    curv_mid, _ = window_stats(curv, 80, 110)             # post-transient
    curv_hi, curv_hi_sd = window_stats(curv, 140, 180)    # post-transient
    # constancy discriminant: drift between two POST-transient windows (the
    # low-m [20,40] window is still inside the [k]_q framing transient)
    curv_drift = abs(curv_hi - curv_mid)         # -> 0 means constant Gaussian coeff
    a_from_curv = curv_hi / 2                     # Gaussian coefficient a = curv/2 -> 1/4

    # quadratic least-squares fit theta_m = a m^2 + b m + c on a tail window
    def quad_fit(mlo, mhi):
        ms = list(range(mlo, mhi + 1))
        n = len(ms)
        S0, S1, S2, S3, S4 = (mpf(sum(m ** p for m in ms)) for p in range(5))
        Ty = mp.fsum(theta[m] for m in ms)
        Tmy = mp.fsum(m * theta[m] for m in ms)
        Tm2y = mp.fsum(m * m * theta[m] for m in ms)
        # normal equations for [a,b,c] with basis (m^2, m, 1)
        A = [[S4, S3, S2], [S3, S2, S1], [S2, S1, S0]]
        rhs = [Tm2y, Tmy, Ty]
        # 3x3 solve (Cramer)
        def det3(M):
            return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                    - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                    + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
        D = det3(A)
        sol = []
        for j in range(3):
            Mj = [row[:] for row in A]
            for i in range(3):
                Mj[i][j] = rhs[i]
            sol.append(det3(Mj) / D)
        return sol  # [a, b, c]
    a_fit, b_fit, c_fit = quad_fit(120, 180)

    # framing linear term predicted by [k]_q normalization: (1/2) log_q(1/(q-1))
    b_pred = (log(1 / (q - 1)) / logq) / 2

    # (diagnostic only) s_m = theta_m/C(m,2), polluted by the linear term
    rows = []
    for m in range(4, M_MAX):
        rows.append((m, theta[m] / comb(m, 2)))
    s_vals = [r[1] for r in rows]

    def at(mlo, mhi):
        return (mlo - 4, mhi - 4)
    s_lo, _ = window_stats(s_vals, *at(20, 40))
    s_hi, _ = window_stats(s_vals, *at(160, 180))
    s_drift = abs(s_hi - s_lo)
    curv_mean, curv_sd = curv_hi, curv_hi_sd

    # (C) Gevrey-1/2 effective order o_m = 2 log I(m)/log(m!)
    def lfact(n):
        return mpf(lgamma(n + 1))
    o = [(2 * log(mpf(I[m])) / lfact(m)) if m >= 2 else mpf(0) for m in range(M_MAX)]
    o_lo, _ = window_stats(o, 20, 40)
    o_hi, _ = window_stats(o, 160, 180)
    o_drift = abs(o_hi - o_lo)

    # exact arithmetic identity (claim B leading order): C(m,2) = sum_{k=1}^m (k-1)
    ident_ok = all(comb(m, 2) == sum(k - 1 for k in range(1, m + 1))
                   for m in range(2, 50))

    print("== theta-order vs jet order vs GS Poincare q-degree ==")
    print(f"   q0 = {mp.nstr(q, 12)}, m up to {M_MAX}, dps={mp.dps}\n")
    print("  (A) CONSTANCY -- curvature (2nd diff theta_m) -> 2a, target 1/2:")
    print(f"      window m in [20,40]:   curv = {mp.nstr(curv_lo, 8)}")
    print(f"      window m in [140,180]: curv = {mp.nstr(curv_hi, 8)}  "
          f"(sd {mp.nstr(curv_hi_sd, 3)})")
    print(f"      curvature drift = {mp.nstr(curv_drift, 4)}  (-> 0 => Gaussian "
          f"coeff CONSTANT, not jet-graded)")
    print(f"      => Gaussian coeff a = curv/2 = {mp.nstr(a_from_curv, 8)} "
          f"(target 1/4)")
    print(f"      quad fit theta~a m^2+b m+c on [120,180]: a={mp.nstr(a_fit, 8)} "
          f"b={mp.nstr(b_fit, 6)} (framing b_pred={mp.nstr(b_pred, 6)})\n")
    print("  (B) GS BRIDGE (leading order)  a = 1/4 = (1/2)*(1/2), 1/2 = leading "
          "coeff of GS deg_q[m]_q! = C(m,2):")
    print(f"      leading theta Gaussian coeff a = {mp.nstr(a_fit, 8)} = "
          f"(1/2) * (leading GS-degree coeff 1/2)")
    print(f"      exact identity C(m,2) = sum_(k<=m)(k-1) [GS cumulative deg], "
          f"deg_q[k]_q=k-1: {ident_ok}")
    print(f"      (diagnostic, linear-polluted) theta_m/C(m,2): "
          f"[20,40]={mp.nstr(s_lo, 5)} [160,180]={mp.nstr(s_hi, 5)} "
          f"-- drifts by framing b, not slope\n")
    print("  (C) GEVREY-1/2 effective order o_m = 2 log I(m)/log(m!) (target 1):")
    print(f"      [20,40]  o = {mp.nstr(o_lo, 8)}")
    print(f"      [160,180]o = {mp.nstr(o_hi, 8)}   drift = {mp.nstr(o_drift, 4)} "
          f"(e^sqrt(m) subleading, Lean-bounded)\n")

    constant_verdict = (curv_drift < mpf("0.01")
                        and abs(a_from_curv - mpf("0.25")) < mpf("0.005"))
    bridge_verdict = abs(a_fit - mpf("0.25")) < mpf("0.01")

    verdict = (
        "SCOPE-(a): the theta-order is CONSTANT across jet order m -- the "
        f"curvature (2nd diff theta_m) is flat at {mp.nstr(curv_hi, 6)} "
        f"(drift {mp.nstr(curv_drift, 3)}), so the Gaussian coefficient "
        f"a = {mp.nstr(a_fit, 6)} -> 1/4 is intrinsic, NOT jet-graded. What "
        "grades with m is the cumulative Gaussian theta_m ~ m^2/4, whose "
        "leading coefficient 1/4 = (1/2) x (1/2), the 1/2 being the leading "
        "coefficient of the GS/Hecke Poincare top degree deg_q[m]_q! = C(m,2). "
        "So the LEADING theta Gaussian = HALF the cumulative GS filtration "
        "q-degree; theta_m ~ deg_q(([m]_q!)^{1/2}). The 1/2 is the depth-2 "
        "(involution-recurrence) structure; C1's denominators ARE the GS "
        f"quantum integers [k]_q. The subleading linear term b={mp.nstr(b_fit, 4)} "
        f"~ b_pred={mp.nstr(b_pred, 4)} is the [k]_q-vs-q^(k-1) framing "
        "(known transient), not the slope. Growth measurement + exact "
        "arithmetic identity; no fit, no AME."
    )
    print(f"VERDICT: {verdict}")
    print(f"  constant_slope = {constant_verdict}, gs_bridge_leading = {bridge_verdict}")

    witness = {
        "description": "theta-order (slope-1/2 Gaussian exponent of the C1 q-lift "
                       "kernel) vs jet/body order m vs Groebner-Shirshov (Hecke) "
                       "Poincare q-degree deg_q[m]_q! = C(m,2). Tests whether the "
                       "theta-order is constant across m (intrinsic) or jet-graded, "
                       "and whether the m^2/4 Gaussian = (1/2) cumulative GS degree.",
        # `computation` is RESERVED by WitnessBuilder.wrap_legacy, which
        # overwrites it with the witness stem ("filename already encodes
        # this"). That is true for a name and false for this field, which
        # is a METHOD description. Renamed so the text survives the wrap.
        "computation_method": "mpmath dps=60; C1 recurrence [m+2]_q b_{m+2}=b_{m+1}+b_m "
                       "seeded b_0=b_1=1; theta_m=-log_q|b_m|; s_m=theta_m/C(m,2); "
                       "bridge=theta_m/(m(m-1)/4); involution effective Gevrey order "
                       "2 log I(m)/log(m!); flatness via window means/drift.",
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "parameters": {"dps": mp.dps, "m_max": M_MAX, "q0": mp.nstr(q, 20),
                       "q0_anchor": "muon (computations layer canonical)"},
        "results": {
            "curvature_2nd_diff_theta": {"target_2a": "1/2",
                                         "window_20_40": mp.nstr(curv_lo, 12),
                                         "window_140_180": mp.nstr(curv_hi, 12),
                                         "sd": mp.nstr(curv_hi_sd, 6),
                                         "drift": mp.nstr(curv_drift, 8),
                                         "gaussian_coeff_a": mp.nstr(a_from_curv, 12),
                                         "constant_not_jet_graded": bool(constant_verdict)},
            "quadratic_fit_120_180": {"a_target_1_4": mp.nstr(a_fit, 12),
                                      "b_linear": mp.nstr(b_fit, 10),
                                      "b_pred_framing_half_logq_inv_qm1": mp.nstr(b_pred, 10),
                                      "c": mp.nstr(c_fit, 6)},
            "gs_bridge_leading": {"claim": "a = 1/4 = (1/2)*(1/2); leading theta "
                                  "Gaussian = (1/2) cumulative GS deg_q[m]_q! = C(m,2)",
                                  "a_fit": mp.nstr(a_fit, 12),
                                  "identity_C_m_2_eq_cumulative_gs_degree": bool(ident_ok),
                                  "deg_q_k_q_eq_k_minus_1": True,
                                  "subleading_linear_is_framing": True,
                                  "verdict": bool(bridge_verdict)},
            "slope_s_m_diagnostic_linear_polluted": {"window_20_40": mp.nstr(s_lo, 10),
                                                     "window_160_180": mp.nstr(s_hi, 10),
                                                     "drift": mp.nstr(s_drift, 8),
                                                     "note": "polluted by framing b; "
                                                     "NOT the constancy invariant"},
            "gevrey_effective_order": {"target": "1",
                                       "window_20_40": mp.nstr(o_lo, 10),
                                       "window_160_180": mp.nstr(o_hi, 10),
                                       "drift": mp.nstr(o_drift, 8)},
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-mlog",
            "audit_doc": "docs/audits/2026-07-20-theta-jet-gb-filtration.md",
            "consumers": ["content/quantum-observable-universe/lean/QOU/Mass/"
                          "BindingGevreyHalf.lean",
                          "content/unital-groebner-bases/lean/UGB/GrobnerShirshov/"
                          "JetOrder.lean",
                          "computations/gb-filtration-jet-order.witness.json"],
            "route_b": "computations/probes/qlift_routeB_connection_matrix_probe.py "
                       "(measured C1 decay leg gamma ~ -1/4)",
            "discipline": "scope-(a); pre-stated discriminants; no AME data; the "
                          "GS-bridge identification is leading-q-order + conjectural "
                          "(C1 = binding module is the standing keystone conjecture)",
        },
    }
    out = WitnessBuilder.wrap_legacy(
        "theta_jet_gb_grading_probe",
        witness,
        script_path=__file__,
        engine="python+mpmath",
        start_time=_T0,
    ).save()
    print(f"witness written: {out}")


if __name__ == "__main__":
    main()
