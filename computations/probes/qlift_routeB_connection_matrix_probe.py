#!/usr/bin/env python3
"""Route B: numeric 2x2 connection matrix between the C1 kernel and GGM eq 49.

Workplan step 3 (Stokes-matrix route) follow-up to the diagonal-gauge prune
docs/audits/2026-07-20-qlift-ggm-gauge-prune.md, which SCOPE-(b)-excluded all
diagonal gauges b_m = g_m(q) y_m but explicitly left non-diagonal 2x2 gauge
transforms live.  This probe measures the actual 2x2 gauge numerically.

Kernels (state vectors v_m = (b_m, b_{m+1})^T, u_m = (y_m, y_{m+1})^T):
  C1 (proved q-lift):   [m+2]_q b_{m+2} = b_{m+1} + b_m
        companion  P_m = [[0, 1], [1/[m+2]_q, 1/[m+2]_q]],   v_{m+1} = P_m v_m
  C2 (GGM eq 49, arXiv:2012.00062 p.14):  y_{m+1} = (2 - q^m) y_m - y_{m-1}
        i.e. y_{m+2} = (2 - q^{m+1}) y_{m+1} - y_m,
        companion  Q_m = [[0, 1], [-1, 2 - q^{m+1}]],        u_{m+1} = Q_m u_m
Note det Q_m = 1 exactly, so det Y_m = 1 for all m; all Y / Q inversions below
use the EXACT determinant via the adjugate (the naive numeric 2x2 determinant
is a huge*huge - huge*huge cancellation past ~1e60 dynamic range and is wrong
by construction-scale factors -- the first draft of this probe failed its own
sanity assert at q = 1.10998 for exactly that reason).

Construction.  Two independent solutions of each equation from independent
initial data (columns of B_0 = Y_0 = I, i.e. (1,0) and (0,1)); fundamental
matrices B_{m+1} = P_m B_m, Y_{m+1} = Q_m Y_m.  The candidate gauge is
A_m = B_m M Y_m^{-1} (M in GL_2 constant; every gauge intertwining the two
companion systems has this form).  We test M = I and one generic M for
robustness of the growth class.

(i) SANITY (holds by construction; asserted): A_{m+1} = P_m A_m Q_m^{-1},
    relative residual < 1e-45 at dps = 60.

(ii) KEY TEST -- growth class of the entries of A_m.  DISCRIMINATION
CRITERION (pre-stated).  Let L_m = log max_ij |(A_m)_ij| and, over a tail
window of m:
    d_est     = mean(L_{m+1} - L_m) / log q          (effective degree in x = q^m)
    gamma_est = mean(L_{m+2} - 2 L_{m+1} + L_m) / (2 log q)   (theta exponent)
  * |A_m| ~ polynomial of degree <= 2 in x = q^m  =>  L_m/m -> d*log q with
    |d| <= 2 and second difference -> 0:  |gamma_est| < 0.05 and |d_est| <= 2.5
    => RATIONAL-GAUGE-PLAUSIBLE at this q  (log|A|/m -> const * log q).
  * |A_m| ~ q^{gamma m^2} (theta / q-Gevrey type)  =>  log|A|/m^2 -> gamma*log q,
    i.e. nonzero second difference:  |gamma_est| >= 0.15  =>  THETA -- no
    rational gauge; the C1 <-> GGM identification needs a theta /
    q-Borel-Laplace factor (gamma_est > 0: q-Laplace/theta GROWTH factor;
    gamma_est < 0: q-Borel DECAY factor).
  * |gamma_est| < 0.05 but |d_est| > 2.5  =>  EXP-NONRATIONAL: degree-<=2
    rational gauge excluded numerically; plain-exponential growth of
    non-small rate (neither low-degree rational nor theta).
  * otherwise INDETERMINATE (report, no durable call).
Windows: m = 0..80 computed; the spec window [28, 38] is reported alongside
the asymptotic window [60, 78] (at q = 1.05, q^m only passes 2 at m ~ 14 and
the log_q[(q-1)^{-1}] ~ 62-per-factor transient pollutes m <= 40; the
asymptotic window is the classifier, the spec window is shown for comparison).

Newton-polygon expectation (stated up front, q > 1): C1's solutions decay
q-Gevrey-fast (two-step b_{m+2} ~ b_m/[m+2]_q => log_q|B| ~ -m^2/4), while
GGM eq 49's generic solution grows y_{m+2} ~ -q^{m+1} y_{m+1} =>
log_q|Y| ~ +m^2/2, and det Y_m = 1 makes |Y^{-1}| ~ |Y|.  Hence
A = B M Y^{-1} is expected THETA with gamma ~ -1/4 + 1/2 = +1/4 unless the
entries cancel miraculously -- the probe decides; the theta threshold 0.15
sits below the predicted 0.25 with margin.

All statements are SCOPE-(a): "this construction, at these q, shows this
growth" -- a numerical growth measurement, not a structural exclusion; the
only by-construction fact is sanity (i).  No AME data; no fit beyond the
pre-stated log-growth difference diagnostics above.

Run:  python3 -u computations/probes/qlift_routeB_connection_matrix_probe.py \
          2>&1 | tee /tmp/qlift-routeB.log
Emits: qlift_routeB_connection_matrix_probe.witness.json (same directory).
"""

import json
import os
from datetime import datetime, timezone

from mpmath import mp, mpf, log

mp.dps = 60

M_MAX = 80                       # m = 0..80 (spec window 0..40 contained)
Q_LIST = [mpf("0.9"), mpf("1.05"), mpf("1.10998")]
TAIL_SPEC = (28, 38)             # window named in the task spec (reported)
TAIL_ASYM = (60, 78)             # asymptotic window (classifier)
TOL_SANITY = mpf("1e-45")        # relative residual for the by-construction check
GAMMA_THETA = mpf("0.15")        # |gamma_est| >= this  => theta class
GAMMA_FLAT = mpf("0.05")         # |gamma_est| <  this  => no-curvature class
DEG_RATIONAL = mpf("2.5")        # |d_est| <= this (with flat gamma) => rational plausible

# generic constant M in GL_2 for the gauge-robustness re-run (A = B M Y^{-1})
M_GENERIC = [[mpf(2), mpf(1)], [mpf(1), mpf(1)]]        # det = 1


def qint(k, q):
    """[k]_q = (1 - q^k)/(1 - q)."""
    return (1 - q ** k) / (1 - q)


# ------------------------------------------------------------- 2x2 helpers
def mat_mul(X, Y):
    return [[X[0][0] * Y[0][0] + X[0][1] * Y[1][0],
             X[0][0] * Y[0][1] + X[0][1] * Y[1][1]],
            [X[1][0] * Y[0][0] + X[1][1] * Y[1][0],
             X[1][0] * Y[0][1] + X[1][1] * Y[1][1]]]


def mat_inv_exactdet(X, d):
    """Inverse via adjugate with EXACT known determinant d (avoids the
    catastrophic huge*huge - huge*huge cancellation of the numeric det)."""
    return [[X[1][1] / d, -X[0][1] / d], [-X[1][0] / d, X[0][0] / d]]


def mat_maxabs(X):
    return max(abs(X[i][j]) for i in range(2) for j in range(2))


def companions(m, q):
    """(P_m, Q_m) advancing C1 / C2 state vectors from index m to m+1.
    det P_m = -1/[m+2]_q, det Q_m = 1 (exact)."""
    inv = 1 / qint(m + 2, q)
    P = [[mpf(0), mpf(1)], [inv, inv]]
    Q = [[mpf(0), mpf(1)], [mpf(-1), 2 - q ** (m + 1)]]
    return P, Q


def fundamental_matrices(q):
    """B_m, Y_m for m = 0..M_MAX from B_0 = Y_0 = I.  det Y_m = 1 exactly."""
    B = [[[mpf(1), mpf(0)], [mpf(0), mpf(1)]]]
    Y = [[[mpf(1), mpf(0)], [mpf(0), mpf(1)]]]
    for m in range(M_MAX):
        P, Q = companions(m, q)
        B.append(mat_mul(P, B[m]))
        Y.append(mat_mul(Q, Y[m]))
    return B, Y


def growth_diagnostics(L, logq, tail):
    """(d_est, gamma_est) from first/second differences of L_m over tail."""
    lo, hi = tail
    d1 = [L[m + 1] - L[m] for m in range(lo, hi + 1)]
    d2 = [L[m + 2] - 2 * L[m + 1] + L[m] for m in range(lo, hi)]
    d_est = (sum(d1) / len(d1)) / logq
    gamma_est = (sum(d2) / len(d2)) / (2 * logq)
    return d_est, gamma_est


def classify(d_est, gamma_est):
    if abs(gamma_est) >= GAMMA_THETA:
        kind = ("THETA growth |A| ~ q^{+gamma m^2} -- needs q-Laplace/theta factor"
                if gamma_est > 0 else
                "THETA decay |A| ~ q^{gamma m^2} -- needs q-Borel factor")
        return "THETA", kind
    if abs(gamma_est) < GAMMA_FLAT:
        if abs(d_est) <= DEG_RATIONAL:
            return "RATIONAL-PLAUSIBLE", ("flat curvature, effective degree "
                                          "|d| <= 2.5 in x = q^m")
        return "EXP-NONRATIONAL", ("flat curvature but effective degree > 2.5 "
                                   "-- degree-<=2 rational gauge excluded "
                                   "numerically at this q")
    return "INDETERMINATE", "0.05 <= |gamma_est| < 0.15 -- no durable call"


def run_q(q):
    logq = log(q)
    B, Y = fundamental_matrices(q)

    out = {"q": mp.nstr(q, 8)}
    per_M = []
    for tag, M in (("I", None), ("generic", M_GENERIC)):
        A = []
        for m in range(M_MAX + 1):
            BM = B[m] if M is None else mat_mul(B[m], M)
            A.append(mat_mul(BM, mat_inv_exactdet(Y[m], mpf(1))))

        # (i) sanity: A_{m+1} = P_m A_m Q_m^{-1}  (by construction; det Q = 1)
        worst = mpf(0)
        for m in range(M_MAX):
            P, Q = companions(m, q)
            rhs = mat_mul(mat_mul(P, A[m]), mat_inv_exactdet(Q, mpf(1)))
            num = max(abs(A[m + 1][i][j] - rhs[i][j])
                      for i in range(2) for j in range(2))
            rel = num / mat_maxabs(A[m + 1])
            worst = max(worst, rel)
        assert worst < TOL_SANITY, f"sanity consistency failed: {mp.nstr(worst, 5)}"

        # (ii) growth of entries
        L = [log(mat_maxabs(A[m])) for m in range(M_MAX + 1)]
        d_spec, g_spec = growth_diagnostics(L, logq, TAIL_SPEC)
        d_est, gamma_est = growth_diagnostics(L, logq, TAIL_ASYM)
        cls, why = classify(d_est, gamma_est)

        # per-entry gamma (all four entries, asymptotic window)
        entry_gammas = []
        for i in range(2):
            for j in range(2):
                Le = [log(abs(A[m][i][j])) if A[m][i][j] != 0 else mpf(0)
                      for m in range(M_MAX + 1)]
                _, ge = growth_diagnostics(Le, logq, TAIL_ASYM)
                entry_gammas.append(mp.nstr(ge, 6))

        print(f"  q = {mp.nstr(q, 8):<10} M = {tag:<8} "
              f"sanity = {mp.nstr(worst, 3):<10} "
              f"spec[28,38]: d = {mp.nstr(d_spec, 5):<9} g = {mp.nstr(g_spec, 5):<9} "
              f"asym[60,78]: d = {mp.nstr(d_est, 5):<9} g = {mp.nstr(gamma_est, 5):<9} "
              f"=> {cls}")
        per_M.append({"M": tag, "sanity_max_rel_residual": mp.nstr(worst, 4),
                      "spec_window": {"tail": list(TAIL_SPEC),
                                      "d_est": mp.nstr(d_spec, 8),
                                      "gamma_est": mp.nstr(g_spec, 8)},
                      "asym_window": {"tail": list(TAIL_ASYM),
                                      "d_est": mp.nstr(d_est, 8),
                                      "gamma_est": mp.nstr(gamma_est, 8)},
                      "entry_gammas_asym": entry_gammas,
                      "class": cls, "why": why})
    out["runs"] = per_M
    out["class"] = per_M[0]["class"] if per_M[0]["class"] == per_M[1]["class"] \
        else f"MIXED({per_M[0]['class']}/{per_M[1]['class']})"
    return out


def main():
    print("== Route B: A_m = B_m M Y_m^{-1} connection matrix, C1 <-> GGM eq 49 ==")
    print(f"   dps = {mp.dps}, m = 0..{M_MAX}, windows spec{TAIL_SPEC} / "
          f"asym{TAIL_ASYM}; criterion: |gamma| >= 0.15 theta, "
          f"< 0.05 & |d| <= 2.5 rational\n")
    results = [run_q(q) for q in Q_LIST]

    qgt1 = [r for r in results if mpf(r["q"]) > 1]
    theta_qgt1 = all(r["class"] == "THETA" for r in qgt1)
    gammas = [mpf(r["runs"][0]["asym_window"]["gamma_est"]) for r in qgt1]

    if theta_qgt1:
        verdict = (
            "SCOPE-(a): at q > 1 (incl. substrate 1.10998) the connection matrix "
            "A_m = B_m M Y_m^{-1} shows THETA-class entry growth, gamma_est ~ "
            f"{mp.nstr(sum(gammas) / len(gammas), 4)} (|A_m| ~ q^{{gamma m^2}}; "
            "Newton-polygon prediction +1/4 from C1 q-Gevrey decay -1/4 times "
            "GGM growth +1/2), robust across two constant-M gauge choices. "
            "In this construction NO rational (degree-<=2 in q^m) gauge links "
            "C1 to GGM eq 49 at these q; the identification, if any, needs a "
            "theta / q-Borel-Laplace factor bridging the q-Gevrey order "
            "mismatch. Numerical growth measurement, not a structural "
            "exclusion; the conjecture-level status of the q-lift is unchanged.")
    else:
        verdict = ("SCOPE-(a): growth class at q > 1 is NOT uniformly theta -- "
                   "see per-q rows; re-examine before any durable claim.")
    print(f"\nVERDICT: {verdict}")

    witness = {
        "description": "Route B numeric connection matrix A_m = B_m M Y_m^{-1} "
                       "between the C1 kernel [m+2]_q b_{m+2} = b_{m+1} + b_m and "
                       "GGM eq-49 y_{m+1} = (2-q^m) y_m - y_{m-1}: sanity "
                       "intertwining A_{m+1} = P_m A_m Q_m^{-1} + entry growth "
                       "classification (rational-in-q^m vs theta q^{gamma m^2})",
        "computation": "mpmath dps=60; fundamental 2x2 solution matrices from "
                       "independent initial data (columns of I); exact-determinant "
                       "adjugate inverses (det Y_m = det Q_m = 1); tail first/second "
                       "differences of log max|A_m entries| normalized by log q; "
                       "pre-stated criterion |gamma|>=0.15 theta vs |gamma|<0.05 "
                       "and |d|<=2.5 rational-plausible; robustness across M = I "
                       "and one generic M in GL_2",
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "parameters": {"dps": mp.dps, "m_max": M_MAX,
                       "tail_window_spec": list(TAIL_SPEC),
                       "tail_window_asymptotic": list(TAIL_ASYM),
                       "q_values": [mp.nstr(q, 8) for q in Q_LIST],
                       "tol_sanity": "1e-45",
                       "gamma_theta_threshold": "0.15",
                       "gamma_flat_threshold": "0.05",
                       "degree_rational_threshold": "2.5",
                       "M_generic": [[2, 1], [1, 1]]},
        "results": {"per_q": results, "theta_at_q_gt_1": bool(theta_qgt1),
                    "verdict": verdict},
        "context": {
            "workplan": "docs/workplans/2026-07-20-qlift-borel-kernel-workplan.md "
                        "(step 3, Route B)",
            "audit_doc": "docs/audits/2026-07-20-qlift-ggm-gauge-prune.md "
                         "(diagonal prune; non-diagonal 2x2 left live -> this probe)",
            "ggm_source": "library/arxiv-2012.00062v3/2012.00062v3.pdf p.14 (eq 49)",
            "discipline": "scope-(a) vocabulary per AGENTS.md; pre-stated "
                          "discrimination criterion; no AME data; sanity check is "
                          "by-construction, growth class is the only measurement",
        },
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qlift_routeB_connection_matrix_probe.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"witness written: {out}")


if __name__ == "__main__":
    main()
