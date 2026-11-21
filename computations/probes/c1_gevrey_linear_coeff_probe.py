#!/usr/bin/env python3
"""C1 q-Gevrey linear coefficient: is B exactly 8?  (bean qou-z8me)

Pre-registered in docs/audits/2026-11-21-c1-gevrey-linear-coefficient.md §1
before this script was run.  Lean derivation:
QOU/Mathlib/C1GevreyLinearCoeff.lean (`c1_linear_coeff_of_nonneg_init`) gives

    B = (1 - log_q(q - 1/q)) / 2

for every q > 1 and every positive solution of [m+2]_q b_{m+2} = b_{m+1} + b_m.
This probe checks the prediction numerically.  mpmath only; no float anywhere.
"""
from __future__ import annotations

import json
import pathlib
import sys

import mpmath as mp

DPS = 300
N = 1000
QS = {
    "6/5": "6/5",
    "probe_q": "1.1099785827513808075916690956",
    "3/2": "3/2",
    "2": "2",
}
BRANCHES = [(1, 0), (0, 1), (1, 1)]


def q_int(n, q):
    return (q**n - q**(-n)) / (q - 1 / q)


def solution(b0, b1, q, n):
    b = [mp.mpf(b0), mp.mpf(b1)]
    for m in range(n - 2):
        b.append((b[m + 1] + b[m]) / q_int(m + 2, q))
    return b


def fit(ys, rows):
    return mp.lu_solve(mp.matrix(rows), mp.matrix(ys))


def main() -> int:
    mp.mp.dps = DPS
    out = {"dps": DPS, "N": N, "cases": [], "checks": {}}
    p1 = p2 = True
    worst_b = mp.mpf(0)
    worst_d = mp.mpf(0)
    q2_bpred = None
    for qname, qstr in QS.items():
        q = (mp.mpf(int(qstr.split("/")[0])) / int(qstr.split("/")[1])) if "/" in qstr else mp.mpf(qstr)
        lq = mp.log(q)
        b_pred = (1 - mp.log(q - 1 / q) / lq) / 2
        if qname == "2":
            q2_bpred = b_pred
        for br in BRANCHES:
            b = solution(*br, q, N)
            L = lambda m: -mp.log(b[m]) / lq  # noqa: E731  (all b_m > 0 for m >= 2)
            res = {}
            for wname, ms in (("early", [200, 300, 400]), ("late", [600, 700, 800])):
                A, B, C = fit([L(m) for m in ms], [[mp.mpf(m)**2, m, 1] for m in ms])
                res[wname] = {"A": mp.nstr(A, 25), "B": mp.nstr(B, 25), "C": mp.nstr(C, 15),
                              "B_minus_pred": mp.nstr(B - b_pred, 5)}
                if wname == "late":
                    dev = abs(B - b_pred)
                    worst_b = max(worst_b, dev)
                    if dev > mp.mpf("1e-15"):
                        p1 = False
            ms4 = [600, 700, 800, 900]
            A, B, D, C = fit([L(m) for m in ms4],
                             [[mp.mpf(m)**2, m, mp.log(m), 1] for m in ms4])
            worst_d = max(worst_d, abs(D))
            if abs(D) > mp.mpf("1e-15"):
                p2 = False
            # parity-free two-step radius: log_q xi_s = B + 1/4
            m = 800
            c = lambda j: b[j] * q**(mp.mpf(j) * (j - 1) / 4)  # noqa: E731
            logxi = mp.log(c(m) / c(m + 2)) / (2 * lq)
            out["cases"].append({
                "q": qname, "branch": list(br), "B_pred": mp.nstr(b_pred, 25),
                "windows": res, "logfit_D": mp.nstr(D, 5),
                "log_q_xi_two_step": mp.nstr(logxi, 25),
                "log_q_xi_minus_pred": mp.nstr(logxi - (b_pred + mp.mpf(1) / 4), 5),
            })
            print(f"q={qname:8s} br={br}  B_pred={mp.nstr(b_pred, 18)}  "
                  f"late B-pred={res['late']['B_minus_pred']}  "
                  f"early B-pred={res['early']['B_minus_pred']}  D={mp.nstr(D, 3)}")
    p3 = q2_bpred is not None and abs(q2_bpred - mp.mpf("0.2075")) < mp.mpf("1e-3")
    out["checks"] = {
        "P1_late_B_matches_pred_1e-15": p1, "worst_late_B_dev": mp.nstr(worst_b, 5),
        "P2_log_term_absent_1e-15": p2, "worst_log_D": mp.nstr(worst_d, 5),
        "P3_B_at_q2_is_0.2075": bool(p3), "B_at_q2": mp.nstr(q2_bpred, 20),
    }
    out["allPassed"] = bool(p1 and p2 and p3)
    # q0 stamp (q0 anchor ratchet). The identity is q-generic (Lean:
    # c1_linear_coeff_of_nonneg_init holds for every q > 1); the four q are
    # sample points. "probe_q" is a typed 29-digit truncation of the proton
    # pin, used as a sample point and not read from the substrate, so no
    # canonical q0Value applies.
    out["q0Anchor"] = "independent"
    out["q0AnchorReason"] = ("q-generic identity checked at four sample q "
                             "(6/5, a 29-digit truncation of the proton pin, "
                             "3/2, 2); the substrate pin q0 is never read")
    print(json.dumps(out["checks"], indent=1))
    path = pathlib.Path(__file__).with_name("c1-gevrey-linear-coeff.witness.json")
    path.write_text(json.dumps(out, indent=1) + "\n")
    return 0 if out["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
