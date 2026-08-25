#!/usr/bin/env python3
"""Route D: formal q-Borel transform of the C1 kernel vs GGM eq 49.

Companion to docs/audits/2026-07-20-qlift-routeD-qborel-transform.md (the
by-hand derivation lives there); this probe only verifies the displayed
identities numerically.  Formalize-first; no scan, no fit, no AME data.

Kernels (three-term windows aligned at index m):
  C1 (proved q-lift, c(q)=1):   [m+1]_q b_{m+1} = b_m + b_{m-1}
  GGM eq 49 (arXiv:2012.00062): y_{m+1} - (2 - q^m) y_m + y_{m-1} = 0.

CONVENTION (RSZ, library/arxiv-0903.0853v3/0903.0853v3.pdf Definition 2.3.3, |q| > 1): the
level-1 formal q-Borel transform is the theta-kernel coefficient map
f_n -> f_n * q^{-n(n-1)/2}.  RSZ 1.2.1 notes kernels are not canonical; the
q-exponential variant divides by (q;q)_n.  All variants and directions are
diagonal weights y_m = w_m b_m, so the conclusion is convention-independent.

DERIVED (audit doc sections 1-3, verified here):
  B  (w_m = q^{-m(m-1)/2}):  [m+1]_q q^m    y_{m+1} = y_m + q^{-(m-1)} y_{m-1}
  L  (w_m = q^{+m(m-1)/2}):  [m+1]_q q^{-m} y_{m+1} = y_m + q^{m-1}   y_{m-1}
  L' (w_m = (q;q)_m):        y_{m+1} = (1-q) y_m + (1-q)(1-q^m) y_{m-1}
  Diagonal-gauge invariant of A_m y_{m+1} + B_m y_m + C_m y_{m-1} = 0:
      I_m = C_m A_{m-1} / (B_m B_{m-1})        (complete for the class)
  I_m^{C1} = -[m]_q  (ALL four presentations -- the transform cannot move it)
  I_m^{GGM} = 1/((2-q^m)(2-q^{m-1}))
  Residual operator after best diagonal alignment:
      (K_C1,gauged - K_GGM) y = -Cm_res * y_{m-1},
      Cm_res = [m]_q (2-q^{m-1})(2-q^m) + 1   (the prune-doc consistency
      residual; GGM form on a gauged-C1 solution evaluates to +Cm_res*y_{m-1}).

KILL CRITERION (pre-stated): diagonal closure iff
max_{m>=2} |I_m^{C1} - I_m^{GGM}| < 1e-40 for all tested q.  Observed
|Delta_m| >> 0 => the formal q-Borel route is CLOSED negatively (scope-(b),
invariant cited: exact I_m mismatch); NOT excluded: the analytic summation
step (Borel-plane continuation + discrete q-Laplace, RSZ ch. 5), 2x2 gauges,
Moebius-of-solution maps, inhomogeneous shifts.

Run:  python3 -u computations/probes/qlift_routeD_qborel_transform_probe.py \
          2>&1 | tee /tmp/qlift-routeD-qborel.log
Emits: qlift_routeD_qborel_transform_probe.witness.json (same directory).
"""

import json
import os
from datetime import datetime, timezone

from mpmath import mp, mpf
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

TOL_KILL = mpf("1e-40")   # pre-stated closure threshold
TOL_ID = mpf("1e-45")     # exact-identity verification tolerance
M_MAX = 15
Q_LIST = [mpf("0.9"), mpf("1.05"), mpf("1.10998")]


def qint(k, q):
    """[k]_q = (1 - q^k)/(1 - q)."""
    return (1 - q ** k) / (1 - q)


def qfact(n, q):
    out = mpf(1)
    for k in range(1, n + 1):
        out *= qint(k, q)
    return out


def qpoch(n, q):
    """(q;q)_n = prod_{k=1..n} (1 - q^k)."""
    out = mpf(1)
    for k in range(1, n + 1):
        out *= (1 - q ** k)
    return out


def b_sequence(nmax, q):
    """Proved C1 solution: b_n = I_q(n)/[n]_q!, I_q(n+2)=I_q(n+1)+[n+1]_q I_q(n)."""
    I = [mpf(1), mpf(1)]
    for n in range(nmax - 1):
        I.append(I[n + 1] + qint(n + 1, q) * I[n])
    return [I[n] / qfact(n, q) for n in range(nmax + 1)]


def theta_w(m, q):
    """RSZ theta-Borel weight w_m = q^{-m(m-1)/2}."""
    return q ** (-mpf(m * (m - 1)) / 2)


# The four C1 kernel presentations as (A_m, B_m, C_m) coefficient functions
# of the window index m: A_m y_{m+1} + B_m y_m + C_m y_{m-1} = 0.
def coeffs_orig(m, q):
    return (qint(m + 1, q), mpf(-1), mpf(-1))


def coeffs_thetaB(m, q):
    return (qint(m + 1, q) * q ** m, mpf(-1), -q ** (-(m - 1)))


def coeffs_thetaL(m, q):
    return (qint(m + 1, q) * q ** (-m), mpf(-1), -q ** (m - 1))


def coeffs_qexpL(m, q):
    return (mpf(1), -(1 - q), -(1 - q) * (1 - q ** m))


KERNELS = [("orig", coeffs_orig, lambda m, q: mpf(1)),
           ("theta_B", coeffs_thetaB, theta_w),
           ("theta_L", coeffs_thetaL, lambda m, q: 1 / theta_w(m, q)),
           ("qexp_L", coeffs_qexpL, lambda m, q: qpoch(m, q))]


def invariant(coeffs, m, q):
    """I_m = C_m A_{m-1} / (B_m B_{m-1}), m >= 2."""
    A1, B1, C1 = coeffs(m, q)
    A0, B0, _ = coeffs(m - 1, q)
    return (C1 * A0) / (B1 * B0)


def cm_res(m, q):
    """Prune-doc consistency residual Cm_res = [m]_q(2-q^{m-1})(2-q^m) + 1."""
    return qint(m, q) * (2 - q ** (m - 1)) * (2 - q ** m) + 1


# ---------------------------------------------------------------- V1
def v1_transformed_kernels():
    print("== V1: transformed kernels (B, L, L') hold exactly on b_n = I_q(n)/[n]_q! ==")
    rows = []
    ok_all = True
    for q in Q_LIST:
        b = b_sequence(M_MAX + 2, q)
        worst = {}
        for name, coeffs, weight in KERNELS[1:]:
            y = [b[m] * weight(m, q) for m in range(M_MAX + 2)]
            w = mpf(0)
            for m in range(1, M_MAX + 1):
                A, B, C = coeffs(m, q)
                res = A * y[m + 1] + B * y[m] + C * y[m - 1]
                scale = max(abs(A * y[m + 1]), abs(B * y[m]), abs(C * y[m - 1]))
                w = max(w, abs(res) / scale)
            worst[name] = w
            ok_all = ok_all and w < TOL_ID
        print(f"  q = {mp.nstr(q, 8):<10} max rel residual: " +
              "  ".join(f"{k} = {mp.nstr(v, 3)}" for k, v in worst.items()))
        rows.append({"q": mp.nstr(q, 8),
                     **{k: mp.nstr(v, 3) for k, v in worst.items()}})
    print(f"  => {'all three transformed kernels EXACT (< 1e-45)' if ok_all else 'IDENTITY FAILS -- derivation wrong!'}\n")
    return {"rows": rows, "ok": ok_all}


# ---------------------------------------------------------------- V2
def v2_invariant_unmoved():
    print("== V2: I_m from all four presentations equals -[m]_q (transform moves nothing) ==")
    rows = []
    ok_all = True
    for q in Q_LIST:
        worst = mpf(0)
        for m in range(2, M_MAX + 1):
            target = -qint(m, q)
            for name, coeffs, _ in KERNELS:
                dev = abs(invariant(coeffs, m, q) - target) / abs(target)
                worst = max(worst, dev)
        ok = worst < TOL_ID
        ok_all = ok_all and ok
        print(f"  q = {mp.nstr(q, 8):<10} max rel deviation of I_m from -[m]_q "
              f"over 4 kernels: {mp.nstr(worst, 3)}")
        rows.append({"q": mp.nstr(q, 8), "max_rel_dev": mp.nstr(worst, 3)})
    print(f"  => {'I_m invariant under every q-Borel variant' if ok_all else 'INVARIANCE FAILS -- derivation wrong!'}\n")
    return {"rows": rows, "ok": ok_all}


# ---------------------------------------------------------------- V3
def v3_mismatch():
    print("== V3: Delta_m = I_m^C1 - I_m^GGM = -[m]_q - 1/((2-q^m)(2-q^{m-1})) ==")
    rows = []
    closed = False
    for q in Q_LIST:
        vals = [abs(-qint(m, q) - 1 / ((2 - q ** m) * (2 - q ** (m - 1))))
                for m in range(2, M_MAX + 1)]
        dmin, dmax = min(vals), max(vals)
        if dmax < TOL_KILL:
            closed = True
        print(f"  q = {mp.nstr(q, 8):<10} min|Delta_m| = {mp.nstr(dmin, 4):<12} "
              f"max|Delta_m| = {mp.nstr(dmax, 4):<12} "
              f"{'DIAGONAL CLOSURE' if dmax < TOL_KILL else 'mismatch at every m'}")
        rows.append({"q": mp.nstr(q, 8), "min_abs_Delta": mp.nstr(dmin, 4),
                     "max_abs_Delta": mp.nstr(dmax, 4)})
    verdict = ("DIAGONAL CLOSURE (derivation wrong!)" if closed else
               "invariant mismatch at every m >= 2, every q -- formal q-Borel "
               "route closed negatively")
    print(f"  => {verdict}\n")
    return {"rows": rows, "closed": closed, "verdict": verdict}


# ---------------------------------------------------------------- V4
def v4_residual_operator():
    print("== V4: GGM form on the (A)-gauged theta-B solution equals Cm_res * y_{m-1} ==")
    rows = []
    ok_all = True
    for q in Q_LIST:
        b = b_sequence(M_MAX + 2, q)
        y = [b[m] * theta_w(m, q) for m in range(M_MAX + 2)]
        # gauge (A) on the theta-B kernel: monic P_m = -1/([m+1]_q q^m);
        # rho_m = g_m/g_{m+1} = -(2-q^m)/P_m = (2-q^m) [m+1]_q q^m.
        g = [mpf(1)]
        for m in range(M_MAX + 1):
            g.append(g[m] / ((2 - q ** m) * qint(m + 1, q) * q ** m))
        yt = [y[m] / g[m] for m in range(M_MAX + 2)]
        worst_id = mpf(0)
        min_c = mpf("inf")
        for m in range(1, M_MAX + 1):
            ggm = yt[m + 1] - (2 - q ** m) * yt[m] + yt[m - 1]
            pred = cm_res(m, q) * yt[m - 1]
            worst_id = max(worst_id, abs(ggm - pred) / max(abs(ggm), abs(pred)))
            min_c = min(min_c, abs(cm_res(m, q)))
        ok = worst_id < TOL_ID and min_c > mpf("0.5")
        ok_all = ok_all and ok
        print(f"  q = {mp.nstr(q, 8):<10} identity rel dev = {mp.nstr(worst_id, 3):<12} "
              f"min|Cm_res| = {mp.nstr(min_c, 4)}")
        rows.append({"q": mp.nstr(q, 8), "identity_rel_dev": mp.nstr(worst_id, 3),
                     "min_abs_Cm_res": mp.nstr(min_c, 4)})
    print(f"  => {'residual operator = Cm_res * y_(m-1) EXACT; never small' if ok_all else 'IDENTITY FAILS -- derivation wrong!'}\n")
    return {"rows": rows, "ok": ok_all}


def main():
    v1 = v1_transformed_kernels()
    v2 = v2_invariant_unmoved()
    v3 = v3_mismatch()
    v4 = v4_residual_operator()

    pruned = v1["ok"] and v2["ok"] and (not v3["closed"]) and v4["ok"]
    verdict = (
        "STILL DISTINCT -- formal q-Borel route CLOSED negatively (scope-(b)): "
        "every formal q-Borel/q-Laplace variant (RSZ theta kernel per Def "
        "2.3.3 of 0903.0853, or q-exponential (q;q)_n kernel, either "
        "direction) is a diagonal coefficient weight, and the complete "
        "diagonal-gauge invariant I_m = C_m A_{m-1}/(B_m B_{m-1}) is "
        "-[m]_q for C1 in all four presentations vs 1/((2-q^m)(2-q^{m-1})) "
        "for GGM eq 49 -- exact algebraic mismatch (the prune-doc consistency "
        "condition), verified |Delta_m| >> 0 at q in {0.9, 1.05, 1.10998}, "
        "m <= 15.  Residual operator after best diagonal alignment: "
        "-Cm_res * y_{m-1} with Cm_res = [m]_q(2-q^{m-1})(2-q^m) + 1.  "
        "NOT excluded: the analytic q-Borel-Laplace summation step "
        "(Borel-plane continuation + discrete q-Laplace, RSZ ch. 5), "
        "non-diagonal 2x2 gauges, Moebius-of-solution maps, inhomogeneous "
        "shifts -- the Stokes-matrix route stays live."
        if pruned else
        "PROBE INCONSISTENT WITH DERIVATION -- re-examine the algebra before "
        "any durable claim.")
    print("VERDICT:", verdict)

    witness = {
        "description": "Route D: formal q-Borel transform (RSZ Def 2.3.3 theta "
                       "kernel + (q;q)_n variant, both directions) applied to "
                       "the C1 kernel [m+1]_q b_{m+1} = b_m + b_{m-1}, compared "
                       "to GGM eq-49 up to diagonal gauge via the complete "
                       "invariant I_m = C_m A_{m-1}/(B_m B_{m-1})",
        "computation": "mpmath dps=50; V1 transformed-kernel identities on the "
                       "proved solution b_n = I_q(n)/[n]_q!; V2 invariance of "
                       "I_m (= -[m]_q) across all four presentations; V3 "
                       "mismatch Delta_m vs GGM; V4 residual-operator identity "
                       "Cm_res * y_{m-1}",
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "parameters": {"dps": mp.dps, "tol_kill": "1e-40", "tol_identity": "1e-45",
                       "m_max": M_MAX, "q_values": [mp.nstr(q, 8) for q in Q_LIST]},
        "derivation": {
            "convention": "RSZ 0903.0853v3 Definition 2.3.3 (level 1, |q|>1): "
                          "B_{q,1}: f_n -> f_n q^{-n(n-1)/2} (theta kernel); "
                          "q-exponential variant f_n -> f_n/(q;q)_n per RSZ 1.2.1",
            "kernel_theta_B": "[m+1]_q q^m y_{m+1} = y_m + q^{-(m-1)} y_{m-1}",
            "kernel_theta_L": "[m+1]_q q^{-m} y_{m+1} = y_m + q^{m-1} y_{m-1}",
            "kernel_qexp_L": "y_{m+1} = (1-q) y_m + (1-q)(1-q^m) y_{m-1}",
            "invariant": "I_m = C_m A_{m-1}/(B_m B_{m-1}); complete for "
                         "diagonal gauges; I^C1 = -[m]_q, "
                         "I^GGM = 1/((2-q^m)(2-q^{m-1}))",
            "residual_operator": "(K_C1,gauged - K_GGM) y = -Cm_res y_{m-1}, "
                                 "Cm_res = [m]_q(2-q^{m-1})(2-q^m) + 1",
        },
        "results": {"v1_transformed_kernels": v1, "v2_invariant_unmoved": v2,
                    "v3_mismatch": v3, "v4_residual_operator": v4,
                    "pruned": pruned, "verdict": verdict},
        "context": {
            "workplan": "docs/workplans/2026-07-20-qlift-borel-kernel-workplan.md (step 3, Route D)",
            "audit_doc": "docs/audits/2026-07-20-qlift-routeD-qborel-transform.md",
            "prior_prune": "computations/probes/qlift_ggm_diagonal_gauge_prune_probe.py "
                           "(diagonal-gauge scope-(b) exclusion; this probe shows the "
                           "formal q-Borel transform lies INSIDE that class and "
                           "re-derives the exclusion via the gauge invariant)",
            "rsz_source": "library/arxiv-0903.0853v3/0903.0853v3.pdf Def 2.3.3 p.23 + 1.2.1 (kernel choices)",
            "ggm_source": "library/arxiv-2012.00062v3/2012.00062v3.pdf p.14 (eq 49)",
            "discipline": "formalize-first (all identities derived by hand in the "
                          "audit doc before running); scope-(a)/(b) per AGENTS.md; "
                          "no AME data; anti-fit",
        },
    }
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "qlift_routeD_qborel_transform_probe.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"witness written: {out}")


if __name__ == "__main__":
    main()
