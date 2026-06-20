#!/usr/bin/env python3
"""qbessel_rigorous_log_neumann_reduction.py
=============================================

The RIGOROUS integer-order coincidence propagator for the Reeb-flow binding
correction (qbk2), via REDUCTION OF ORDER -- resolving BOTH integer-order
singularities that the naive G_q=g1 g2/D suffered (PR #2547):
  * the simple pole at nu>=1 (Neumann resonance in the d_k series), and
  * the confluent double-root at nu=0 (dim=1 blocks; Casoratian->0).

Why reduction of order is resonance-free. The regular solution g1(w)=sum c_k w^k of
(☆) q^nu g(q^2 w) - (1+q^nu-w) g(qw) + g(w) = 0 is smooth in nu (no resonance). The
Casoratian of any two solutions obeys the q-Abel law a2 D(qw)=a0 D(w), i.e.
D(qw)=q^{-nu} D(w) => D(w)=w^{-nu} (normalisation C=1), a clean monomial -- NOT the
divergent d_k series. The SECOND solution is then recovered from g1 and D alone:

    g2(qw)/g1(qw) - g2(w)/g1(w) = D(w)/(g1(w) g1(qw)),

summed UP in w (q>1 => q^j w -> infinity, D=(q^j w)^{-nu} -> 0, terms vanish):

    g2(w) = - g1(w) * sum_{j>=0}  D(q^j w) / ( g1(q^j w) g1(q^{j+1} w) ).

This never touches the d_k recurrence, so it is FINITE at every integer nu (it IS the
genuine log-Neumann / confluent 2nd solution). The coincidence propagator is then the
same object the whole chain used, now finite:

    G_rig(w; nu) = g1(w) g2(w) / D(w) = g1(w) g2(w) w^{nu}.

SELF-CHECKS (catch construction errors):
  (Z1) g2 solves (☆):  L[g2] ~ 0.
  (Z2) Casoratian(g1,g2)(w) = w^{-nu}  (the reduction-of-order normalisation).

Then the deuteron correction delta_rig = sum_lambda [G_rig(w_atom) - G_rig(w_free)] at
the FORCED integer order nu=dim-1 (INCLUDING nu=0), x=theta (Reeb flow), w=q theta^2 --
compared to B(D)/m_e ~ 4.35, against #2547's PV (~1.27, dim>=2 only) and #2545's proxy
(6.16). No fit; nothing wired.
"""
from __future__ import annotations

import json
import math
import pathlib

from mpmath import mp, mpf, qp, fabs, acos, acosh

mp.dps = 50
Q0 = mpf("1.10997858")
QMU = mpf("1.110037")
B_DEU_OVER_ME = mpf("2.224573") / mpf("0.510999")
KSER = 70          # terms in g1
JSUM = 120         # terms in the reduction-of-order Jackson sum
HERE = pathlib.Path(__file__).resolve().parent
DEU = HERE.parent / "atom-chi-rust-d.witness.json"


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


def Dcas(w, nu):
    return w ** (-nu)                       # Casoratian, normalisation C=1


def g2(w, nu, q):
    """Reduction-of-order 2nd solution (resonance-free, finite at all integer nu)."""
    s = mpf(0)
    for j in range(JSUM):
        wj = q ** j * w
        s += Dcas(wj, nu) / (g1(wj, nu, q) * g1(q * wj, nu, q))
    return -g1(w, nu, q) * s


def G_rig(w, nu, q):
    return g1(w, nu, q) * g2(w, nu, q) / Dcas(w, nu)


def reeb_flow_length(r):
    return acos(r) if fabs(r) <= 1 else acosh(fabs(r))


def load(cfg):
    d = json.loads(DEU.read_text(encoding="utf-8"))
    return {tuple(e["partition"]): mpf(e["chi_lambda"]) for e in d["data"][cfg]["by_partition"]}


def main():
    print("Rigorous integer-order log-Neumann via reduction of order (resonance-free)")
    print("=" * 78)
    print(f"q_0={float(Q0)}; B(D)/m_e={float(B_DEU_OVER_ME):.4f}; K={KSER} J={JSUM}\n")

    # ---- self-checks (Z1) L[g2]=0 and (Z2) Casoratian=w^-nu ----
    def L(f, w, nu, q):
        return q ** nu * f(q * q * w, nu, q) - (1 + q ** nu - w) * f(q * w, nu, q) + f(w, nu, q)
    print("(Z) self-checks on sample (nu, w):")
    z_ok = True
    for nu, w in [(mpf(0), mpf("1.2")), (mpf(4), mpf("1.4")), (mpf(8), mpf("0.9")),
                  (mpf(15), mpf("1.6"))]:
        res = L(g2, w, nu, q=Q0)
        cas = g1(w, nu, Q0) * g2(Q0 * w, nu, Q0) - g1(Q0 * w, nu, Q0) * g2(w, nu, Q0)
        cas_err = fabs(cas - Dcas(w, nu))
        ok = fabs(res) < mpf("1e-20") and cas_err < mpf("1e-18")
        z_ok = z_ok and ok
        print(f"    nu={float(nu):>4} w={float(w)}:  L[g2]={mp.nstr(res,4):>11}  "
              f"|Cas - w^-nu|={mp.nstr(cas_err,4):>11}  G_rig={mp.nstr(G_rig(w,nu,Q0),7)}  "
              f"[{'ok' if ok else 'FAIL'}]")
    print(f"  (Z) all self-checks pass: {'YES' if z_ok else 'NO'}\n")

    # ---- forced integer-order correction over ALL deuteron blocks ----
    free, atom = load("free"), load("atom")

    def delta(q):
        tot = mpf(0)
        rows = []
        for lam in free:
            d = dim_sn(list(lam))
            nu = mpf(d - 1)                       # forced integer order, incl nu=0
            rf, ra = free[lam] / d, atom[lam] / d
            xf, xa = reeb_flow_length(rf), reeb_flow_length(ra)
            wf, wa = q * xf ** 2, q * xa ** 2
            dG = G_rig(wa, nu, q) - G_rig(wf, nu, q)
            tot += dG
            rows.append((lam, d, int(d - 1), dG))
        return tot, rows

    d0, rows = delta(Q0)
    dmu, _ = delta(QMU)
    print("forced integer-order correction (nu=dim-1, ALL blocks incl nu=0):")
    print(f"{'lambda':<15}{'dim':>5}{'nu':>4}{'dG_rig':>16}")
    for lam, d, nu, dG in sorted(rows, key=lambda r: r[1], reverse=True):
        print(f"{str(list(lam)):<15}{d:>5}{nu:>4}{mp.nstr(dG,8):>16}")

    absmax = max(fabs(r[3]) for r in rows)
    top = absmax / sum(fabs(r[3]) for r in rows)
    xanchor = fabs(dmu - d0) / (fabs(d0) + fabs(dmu)) if (d0 or dmu) else mpf(0)
    ratio = d0 / B_DEU_OVER_ME
    print(f"\n  delta_rig(q_0)           = {mp.nstr(d0, 8)}")
    print(f"  |delta_rig|/(B(D)/m_e)   = {mp.nstr(fabs(ratio), 6)}   (target ~1)")
    print(f"  cross-anchor spread      = {mp.nstr(xanchor, 4)}")
    print(f"  single-block domination  = {mp.nstr(top*100, 4)}%")

    print("\n--- VERDICT (rigorous, resonance-free, proxy-free; no fit) ---")
    print(f"  #2545 (nu+/-0.5 proxy):       ratio 6.16, swing 43%,  dom 64%")
    print(f"  #2547 (PV, dim>=2 only):      ratio 1.27,            dom 32%")
    print(f"  this (rigorous, ALL blocks):  ratio {mp.nstr(fabs(ratio),4)}, "
          f"dom {mp.nstr(top*100,3)}%, NO proxy, dim=1 INCLUDED")
    on_scale = mpf("0.1") < fabs(ratio) < mpf("10")
    forced_ok = z_ok and top < mpf("0.6") and xanchor < mpf("0.05")
    print()
    if not z_ok:
        print("  => SELF-CHECK FAILED: the reduction-of-order construction is not clean")
        print("     at these (nu,w); the number below is NOT trustworthy. Investigate.")
    elif on_scale and forced_ok:
        print(f"  => RIGOROUS + FORCED + PROXY-FREE: with both integer-order singularities")
        print(f"     resolved (reduction of order, no PV, dim=1 included), the Reeb-flow")
        print(f"     correction is {mp.nstr(fabs(ratio),4)}x the deuteron binding, cross-anchor")
        print(f"     stable ({mp.nstr(xanchor,3)}), un-dominated ({mp.nstr(top*100,3)}%). This is")
        print(f"     the genuine number -- the strongest evidence yet. Promote to: real y_lambda")
        print(f"     weights + bar-parity + the Lean lemma (Casoratian/reduction-of-order),")
        print(f"     then the cross-anchor gate across MORE isotopes (not just D).")
    else:
        print(f"  => RIGOROUS value {mp.nstr(fabs(ratio),4)}x (self-checks pass), but "
              f"{'off-scale' if not on_scale else 'dominated/anchor-unstable'}.")
        print("     Honest: the resonance-free construction is sound; the binding scale is")
        print(f"     {'not reached' if not on_scale else 'reached but the per-block sum is not robust'}.")
    print("\n  No fit; nothing wired; c_k/Delta_lambda cal-anchored. Matching B(D) by any")
    print("  tuned prefactor would be a fit -- the number above is the raw G_rig sum.")
    print("\nRIGOROUS TEST COMPLETE.")
    return 0 if z_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
