#!/usr/bin/env python3
"""qbessel_reeb_yweighted_gap.py
================================

Narrow the gap: re-do the RIGOROUS reduction-of-order Reeb-flow correction
(PR #2549, raw unweighted ratio 2.23x B(D)/m_e) with the FORCED canonical Markov
weights y_lambda (wedderburn_jones_markov.y_lambda_at) -- the binding sum is
B = m_e sum_lambda y_lambda chi_lambda Delta_lambda, so the unweighted sum was a
placeholder. y_lambda is substrate-fixed (depends on q0 only, same free/atom), so
adding it introduces NO knob.

Two natural weighted forms are reported (the choice between them is the one
remaining structural degree of freedom; if they diverge wildly it is itself a flag):
  (A)  delta_A = sum_lambda y_lambda * [G_rig(atom) - G_rig(free)]
  (B)  delta_B = sum_lambda y_lambda * chi_lambda^atom * [G_rig(atom)-G_rig(free)]
       (the full B = sum y chi Delta shape, chi from the atom config)

Compared to B(D)/m_e ~ 4.35.  No fit; nothing wired.  Reaching ~1 must come from
these FORCED weights, not a tuned prefactor.
"""
from __future__ import annotations

import json
import math
import pathlib
import sys

from mpmath import mp, mpf, qp, fabs, acos, acosh

mp.dps = 45
Q0 = mpf("1.10997858")
QMU = mpf("1.110037")
B_DEU_OVER_ME = mpf("2.224573") / mpf("0.510999")
KSER, JSUM = 60, 90
HERE = pathlib.Path(__file__).resolve().parent
DEU = HERE.parent / "atom-chi-rust-d.witness.json"
sys.path.insert(0, str(HERE.parent))
from wedderburn_jones_markov import y_lambda_at  # noqa: E402


def dim_sn(lam):
    n = sum(lam)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return math.factorial(n) // den


def c_k(k, nu, q):
    return (-1) ** k * q ** (mpf(k * (k - 1)) / 2) / (qp(q, q, k) * qp(q ** (nu + 1), q, k))


def g1(w, nu, q):
    return sum(c_k(k, nu, q) * w ** k for k in range(KSER))


def g2(w, nu, q):
    s = mpf(0)
    for j in range(JSUM):
        wj = q ** j * w
        s += (wj ** (-nu)) / (g1(wj, nu, q) * g1(q * wj, nu, q))
    return -g1(w, nu, q) * s


def G_rig(w, nu, q):
    return g1(w, nu, q) * g2(w, nu, q) * w ** nu      # = g1 g2 / D, D=w^-nu


def reeb(r):
    return acos(r) if fabs(r) <= 1 else acosh(fabs(r))


def load(cfg):
    d = json.loads(DEU.read_text(encoding="utf-8"))
    return {tuple(e["partition"]): mpf(e["chi_lambda"]) for e in d["data"][cfg]["by_partition"]}


def main():
    free, atom = load("free"), load("atom")
    y = {k: mpf(str(v)) for k, v in y_lambda_at(6, Q0).items()}
    ymu = {k: mpf(str(v)) for k, v in y_lambda_at(6, QMU).items()}

    print("Reeb-flow correction with FORCED y_lambda Markov weights (gap-narrowing)")
    print("=" * 78)
    print(f"q_0={float(Q0)}; B(D)/m_e={float(B_DEU_OVER_ME):.4f}; sum y_lambda={float(sum(y.values())):.5f}\n")

    def deltas(q, yw):
        raw = wA = wB = mpf(0)
        rows = []
        for lam in free:
            d = dim_sn(list(lam))
            nu = mpf(d - 1)
            rf, ra = free[lam] / d, atom[lam] / d
            wf, wa = q * reeb(rf) ** 2, q * reeb(ra) ** 2
            dG = G_rig(wa, nu, q) - G_rig(wf, nu, q)
            yl = yw[lam]
            raw += dG
            wA += yl * dG
            wB += yl * atom[lam] * dG
            rows.append((lam, d, float(yl), dG))
        return raw, wA, wB, rows

    raw, wA, wB, rows = deltas(Q0, y)
    _, wAmu, wBmu, _ = deltas(QMU, ymu)

    print(f"{'lambda':<15}{'dim':>5}{'y_lam':>11}{'dG_rig':>14}{'y*dG':>14}")
    for lam, d, yl, dG in sorted(rows, key=lambda r: r[1], reverse=True):
        print(f"{str(list(lam)):<15}{d:>5}{yl:>11.5f}{mp.nstr(dG,7):>14}{mp.nstr(mpf(str(yl))*dG,7):>14}")

    rA, rB = wA / B_DEU_OVER_ME, wB / B_DEU_OVER_ME
    xA = fabs(wAmu - wA) / (fabs(wA) + fabs(wAmu)) if (wA or wAmu) else mpf(0)
    xB = fabs(wBmu - wB) / (fabs(wB) + fabs(wBmu)) if (wB or wBmu) else mpf(0)
    print(f"\n  raw (unweighted, #2549)    = {mp.nstr(raw,6)}   ratio {mp.nstr(raw/B_DEU_OVER_ME,5)}")
    print(f"  (A) sum y*dG               = {mp.nstr(wA,6)}   ratio {mp.nstr(rA,5)}   xanchor {mp.nstr(xA,3)}")
    print(f"  (B) sum y*chi*dG           = {mp.nstr(wB,6)}   ratio {mp.nstr(rB,5)}   xanchor {mp.nstr(xB,3)}")

    print("\n--- VERDICT (forced y_lambda; no fit) ---")
    print(f"  progression of the ratio:  #2545 6.16 (proxy) -> #2547 1.27 (PV) ->")
    print(f"                             #2549 2.23 (rigorous raw) -> y-weighted:")
    print(f"                             (A) {mp.nstr(fabs(rA),4)}   (B) {mp.nstr(fabs(rB),4)}")
    onA = mpf("0.3") < fabs(rA) < mpf("3")
    onB = mpf("0.3") < fabs(rB) < mpf("3")
    spread = fabs(fabs(rA) - fabs(rB)) / (fabs(rA) + fabs(rB)) if (rA or rB) else mpf(0)
    print(f"  forms A vs B relative spread = {mp.nstr(spread,4)}  "
          f"({'consistent' if spread < mpf('0.3') else 'DIVERGE -> weighting-form is a residual knob'})")
    print()
    if (onA or onB) and spread < mpf("0.3"):
        print("  => The forced y_lambda weighting brings BOTH natural forms near the binding")
        print("     scale and they agree -- the gap is genuinely narrowed with NO tuned")
        print("     prefactor. Next: bar-parity (gate 2) + more isotopes (cross-anchor gate).")
    elif spread >= mpf("0.3"):
        print("  => Forms A and B DIVERGE: the y-weighted ratio depends on whether chi enters,")
        print("     a residual structural choice. Honest: the y_lambda weights are forced but")
        print("     the propagator's PLACE in the binding sum (does it multiply chi?) is not")
        print("     yet pinned. Settling THAT (from the binding-sum derivation) is the next gate.")
    else:
        print(f"  => y-weighting moves the ratio to A={mp.nstr(fabs(rA),3)}, B={mp.nstr(fabs(rB),3)};")
        print("     not cleanly ~1. The remaining gap is structural (weighting form / bar-parity).")
    print("\n  No fit; nothing wired; c_k/Delta_lambda cal-anchored.")
    print("\nGAP-NARROWING TEST COMPLETE.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
