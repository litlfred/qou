#!/usr/bin/env python3
"""alpha_em_two_term_q0_pull_probe.py — why the two-term proton pin makes alpha_em worse.

Owner question (Carl, 2026-11-20): "why did the two-term make the fine structure
constant worse?"  Draft PR #8554 re-pins q0 through the two-term proton identity
    m_p/m_e = 2 Vol(4_1)/hbar_q^2 * F_Bor(q) - 12 + |tr_conn(p,V^3)|(q),
    tr_conn = -2 (q^2-1)^4 (q^4+q^2+1) / (27 q^6),
which moves q0 by about +11.17 ppb (onto the muon pin) and moves the form-B
alpha_em^-1 residual from about -0.37 ppb to about +76 ppb.

This probe MEASURES; it selects nothing.  For every alpha_em construction live in
the corpus it reports: the value at each of the three q0 pins, the log-slope
d ln(1/alpha)/d ln q, the q at which the construction equals CODATA, and the
implied q-uncertainty.  It also measures the three-way q0 picture (m_p/m_e one-term,
alpha_em, m_mu/m_e) and the size of the self-energy the muon relation would need
to agree with the one-term proton pin.  That last number is a DIAGNOSTIC: nothing
here proposes or wires a term of that size.

mpmath end to end (70 dps); float() only inside display.  No witness emitted:
the numbers are recorded in docs/audits/2026-11-20-alpha-em-two-term-q0-pull.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: F401, E402
from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 70
PPB = mp.mpf(10) ** 9

VOL41 = 2 * mp.clsin(2, mp.pi / 3)            # 2 Cl2(pi/3) = 6 Lambda(pi/3)


def _c(name):
    r = _codata.codata(name)
    return mp.mpf(r.value_str), mp.mpf(r.uncertainty_str)


MP_ME, MP_ME_U = _c("proton-electron mass ratio")
MMU_ME, MMU_ME_U = _c("muon-electron mass ratio")
AINV, AINV_U = _c("inverse fine-structure constant")


def qn(n, q):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def hbar(q):
    return 1 - 1 / q


# ---------------------------------------------------------------- the three identities
def F_Bor(q):
    h = q - 1 / q
    tr = abs((4 + h ** 2 - 3 * h ** 4 - h ** 6) / (h ** 2 + 4))
    return tr * qn(3, q) * qn(2, q) / q ** 3


def mp_one_term(q):
    return 2 * VOL41 / hbar(q) ** 2 * F_Bor(q) - 12


def tr_conn(q):
    return -2 * (q ** 2 - 1) ** 4 * (q ** 4 + q ** 2 + 1) / (27 * q ** 6)


def mp_two_term(q):
    return mp_one_term(q) + abs(tr_conn(q))


def mmu_model(q):
    return VOL41 / hbar(q) ** 2


# ---------------------------------------------------------------- the alpha_em constructions
def alpha_formB(q):
    """alpha_em_schwinger_ladder_probe form B: 1/alpha = T + alpha H (1 - h^2 alpha)."""
    h2 = (q - 1 / q) ** 2
    T = q * qn(9, q) * qn(10, q) + mp.mpf(8) / (12 * mp.pi)
    H = qn(2, q) / (8 * mp.pi)
    a = 1 / T
    for _ in range(200):                       # fixed point; contraction ~1e-5
        a_new = 1 / (T + a * H * (1 - h2 * a))
        if abs(a_new - a) < mp.mpf(10) ** (-mp.mp.dps + 5):
            a = a_new
            break
        a = a_new
    return 1 / a


def alpha_formA(q):
    """form A: alpha^2 H + alpha T - 1 = 0 (no Schwinger factor)."""
    T = q * qn(9, q) * qn(10, q) + mp.mpf(8) / (12 * mp.pi)
    H = qn(2, q) / (8 * mp.pi)
    a = (-T + mp.sqrt(T * T + 4 * H)) / (2 * H)
    return 1 / a


def kappa_gram(q):
    """meson_em_sinh_closed_form._alpha_em_inv_derived kappa = det G_cl / det G_q."""
    pi = mp.pi
    cs_29 = pi ** 2 * mp.mpf(10) / 9
    cs_35 = pi ** 2 * mp.mpf(16) / 15
    n2 = qn(2, q)
    sl, lk = 8, 17
    g11 = cs_29 + pi ** 2 * sl ** 2 / mp.mpf(18) ** 2
    g22 = cs_35 + pi ** 2 * sl ** 2 / mp.mpf(15) ** 2
    g12 = pi ** 2 * lk ** 2 / (mp.mpf(18) * 15)
    det_cl = g11 * g22 - g12 ** 2
    lk_q = abs(n2 * qn(5, q) - qn(3, q) * qn(9, q))
    q9, q3, q5 = qn(9, q), qn(3, q), qn(5, q)
    gq11 = pi ** 2 * (n2 ** 2 - 1) * (q9 ** 2 - 1) / (12 * n2 * q9) + pi ** 2 * ((n2 - 1) * (q9 - 1)) ** 2 / (n2 * q9) ** 2
    gq22 = pi ** 2 * (q3 ** 2 - 1) * (q5 ** 2 - 1) / (12 * q3 * q5) + pi ** 2 * ((q3 - 1) * (q5 - 1)) ** 2 / (q3 * q5) ** 2
    gq12 = pi ** 2 * lk_q ** 2 / (n2 * q9 * q3 * q5)
    det_q = gq11 * gq22 - gq12 ** 2
    return det_cl / det_q


def cs_first_order(q):
    """bare * c1 = (CS(T29)+CS(T35)) * [2]_q/2 * hbar_q^2 — the CS tower's additive term."""
    return mp.pi ** 2 * (mp.mpf(10) / 9 + mp.mpf(16) / 15) * qn(2, q) / 2 * hbar(q) ** 2


def alpha_cs_tower(q):
    bare = q * qn(9, q) * qn(10, q)
    c1 = cs_first_order(q) / bare
    return bare * (1 + c1 / (1 - c1 * kappa_gram(q)))


def alpha_pslq45(q):
    """45 [3]_q (1 + d + 8 q d^2), d = hbar^4 [5]_q — RULED OUT in the corpus as a PSLQ fit."""
    d = hbar(q) ** 4 * qn(5, q)
    return 45 * qn(3, q) * (1 + d + 8 * q * d ** 2)


def alpha_bare(q):
    return q * qn(9, q) * qn(10, q)


FORMS = {
    "B_schwinger": alpha_formB,
    "A_quadratic": alpha_formA,
    "CS_tower_exact": alpha_cs_tower,
    "PSLQ_45_3q": alpha_pslq45,
    "bare_q9_10": alpha_bare,
}


# ---------------------------------------------------------------- helpers
def solve(f, target, q0):
    return mp.findroot(lambda q: f(q) - target, q0)


def dlog(f, q):
    return q * mp.diff(f, q) / f(q)


def ppb(x, ref):
    return (x - ref) / ref * PPB


def s(x, n=12):
    return mp.nstr(x, n)


def main() -> int:
    checks = []
    q_ref = mp.mpf(Q_50_DIGIT_STR)
    q1 = solve(mp_one_term, MP_ME, q_ref)
    q2 = solve(mp_two_term, MP_ME, q1)
    qmu = solve(mmu_model, MMU_ME, q1)
    pins = {"one_term_proton": q1, "two_term_proton": q2, "muon": qmu}

    print("== pins (re-derived here, 70 dps)")
    for k, v in pins.items():
        print(f"  {k:17s} {mp.nstr(v, 40)}   {s(ppb(v, q1), 8):>14s} ppb vs one-term")
    # one-term re-derivation must reproduce the substrate pin to its 50 digits
    ok = abs(q1 - q_ref) < mp.mpf("1e-48")
    checks.append(("one_term_pin_reproduces_substrate", ok))
    q2_pr = mp.mpf("1.10997859515088599908756520359868262121410348054121621148890")
    checks.append(("two_term_pin_reproduces_PR8554", abs(q2 - q2_pr) < mp.mpf("1e-55")))

    # sigma on q from each mass determination
    sl_mp1 = dlog(mp_one_term, q1)
    sl_mp2 = dlog(mp_two_term, q2)
    sl_mu = dlog(mmu_model, qmu)
    sq_mp = (MP_ME_U / MP_ME) / abs(sl_mp1) * PPB
    sq_mu = (MMU_ME_U / MMU_ME) / abs(sl_mu) * PPB
    sa_rel = AINV_U / AINV * PPB
    print("\n== mass-relation slopes d ln(ratio)/d ln q and implied sigma(q)")
    print(f"  m_p/m_e one-term slope {s(sl_mp1)}  two-term {s(sl_mp2)}  sigma_q {s(sq_mp,6)} ppb")
    print(f"  m_mu/m_e slope         {s(sl_mu)}  (= -2/(q-1) = {s(-2/(qmu-1))})  sigma_q {s(sq_mu,6)} ppb")
    print(f"  alpha^-1 CODATA rel sigma {s(sa_rel,6)} ppb")

    print("\n== alpha_em^-1 constructions")
    rows = {}
    for name, f in FORMS.items():
        vals = {k: f(v) for k, v in pins.items()}
        res = {k: ppb(vals[k], AINV) for k in pins}
        sl = dlog(f, q1)
        qs = solve(f, AINV, q1)
        sq = sa_rel / abs(sl)
        rows[name] = dict(vals=vals, res=res, slope=sl, qstar=qs, sigq=sq)
        print(f"  [{name}]  slope d ln(1/a)/d ln q = {s(sl,10)}")
        for k in pins:
            print(f"     at {k:17s} 1/a = {s(vals[k],16)}   resid {s(res[k],8):>14s} ppb  ({s(res[k]/sa_rel,6)} sigma_a)")
        print(f"     q* (=CODATA) = {mp.nstr(qs,30)}")
        for k, v in pins.items():
            d = ppb(qs, v)
            print(f"        q* - {k:17s} = {s(d,8):>12s} ppb  = {s(d/sq,6):>10s} x sigma_q(alpha)={s(sq,4)} ppb")

    # linearity check of the owner-quoted figure: resid(q2) ~ resid(q1) + slope * shift
    B = rows["B_schwinger"]
    shift = ppb(q2, q1)
    lin = B["res"]["one_term_proton"] + B["slope"] * shift
    print(f"\n== linear account (form B): {s(B['res']['one_term_proton'],6)} + {s(B['slope'],6)} x {s(shift,8)}"
          f" = {s(lin,8)} ppb  vs exact {s(B['res']['two_term_proton'],8)} ppb")
    checks.append(("formB_two_term_resid_is_slope_times_shift",
                   abs(lin - B["res"]["two_term_proton"]) < mp.mpf("0.05")))

    # why the slope is ~7: d ln [n]_q / d ln q = n coth(n lam) - coth(lam)
    lam = mp.log(q1)
    d9 = 9 * mp.coth(9 * lam) - mp.coth(lam)
    d10 = 10 * mp.coth(10 * lam) - mp.coth(lam)
    print("\n== anatomy of the bare slope (exact): 1 + dln[9]/dlnq + dln[10]/dlnq")
    print(f"  lam = ln q = {s(lam)};  dln[9] = {s(d9)}  ((n^2-1)lam/3 = {s(80*lam/3)})")
    print(f"  dln[10] = {s(d10)}  ((n^2-1)lam/3 = {s(99*lam/3)});  total {s(1+d9+d10)} vs mp.diff {s(rows['bare_q9_10']['slope'])}")
    checks.append(("bare_slope_anatomy", abs(1 + d9 + d10 - rows["bare_q9_10"]["slope"]) < mp.mpf("1e-40")))

    # form B vs CS tower: their first-order additive terms are different functions of q
    print("\n== form B additive 8/(12 pi) vs CS tower additive pi^2 (98/45) [2]_q/2 hbar_q^2")
    for qq in (q1, mp.mpf("1.05"), mp.mpf("1.2")):
        a, b = mp.mpf(8) / (12 * mp.pi), cs_first_order(qq)
        print(f"  q={s(qq,8)}:  8/(12pi)={s(a,14)}  CS={s(b,14)}  rel gap {s((b-a)/a,6)}")
    print(f"  form B alpha-order term alpha*H at q1 = {s(qn(2,q1)/(8*mp.pi)/rows['B_schwinger']['vals']['one_term_proton'],10)}")
    c1 = cs_first_order(q1) / alpha_bare(q1)
    k = kappa_gram(q1)
    print(f"  CS tower second-order term bare*c1^2*kappa at q1 = {s(alpha_bare(q1)*c1**2*k,10)};  kappa_gram(q1) = {s(k,14)}")
    checks.append(("formB_and_CS_first_order_differ_off_q0",
                   abs(cs_first_order(mp.mpf("1.2")) - mp.mpf(8) / (12 * mp.pi)) > mp.mpf("0.1")))

    # three-way q picture
    print("\n== three determinations of q0 (pairwise, ppb and sigma in quadrature)")
    det = {"m_p one-term": (q1, sq_mp), "m_p two-term": (q2, sq_mp),
           "alpha form B": (B["qstar"], B["sigq"]), "m_mu": (qmu, sq_mu)}
    keys = list(det)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            (a, sa), (b, sb) = det[keys[i]], det[keys[j]]
            g = ppb(b, a)
            sig = mp.sqrt(sa ** 2 + sb ** 2)
            print(f"  {keys[j]:13s} - {keys[i]:13s} = {s(g,8):>12s} ppb  ({s(g/sig,6)} sigma)")

    # diagnostic: muon self-energy needed for m_mu to agree at the one-term proton pin
    need = MMU_ME / mmu_model(q1) - 1
    aem = 1 / AINV
    print("\n== DIAGNOSTIC ONLY: multiplicative correction the muon relation needs at q(one-term)")
    print(f"  delta_mu = {s(need*PPB,10)} ppb ;  /(alpha/pi) = {s(need/(aem/mp.pi),8)} ;  /alpha^2 = {s(need/aem**2,8)}"
          f" ;  /hbar_q^2 = {s(need/hbar(q1)**2,8)}")
    print("  (sizes only; no candidate is chosen here)")

    print("\n== checks")
    allok = True
    for n, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {n}")
        allok &= bool(ok)
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
