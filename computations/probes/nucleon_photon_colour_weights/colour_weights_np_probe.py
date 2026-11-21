#!/usr/bin/env python3
"""Do the photon's colour weights separate the neutron from the proton?  (bean qou-99qc)

Pre-registered in PREREGISTRATION.md (same directory) before any number here was computed.

Photon (def:photon, owner ruling): gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^{-1} in H_3(q).
Pair product normal form: QOU.QuarkState.pairNFChiral_eq (Lean, sorry-free); basis
[1, s0, s1, L- = s1 s0, L+ = s0 s1, e = s0 s1 s0].

What this probe measures (exact sympy where possible, mpmath at 70 dps otherwise, no float64):
  1. the solution set of gamma(phi) gamma(psi) = beta_Bor (PR #8634) at the #8634 control
     values h = 1/2, 2/9 and at the proton pin q0; real vs non-real points;
  2. for every element built by the rules R-pt, R-maj, R-free (PREREGISTRATION.md):
     chi_(3), chi_(2,1), chi_(1^3); one-term quantum trace T1 = Tr(K^{(x)3} rho(X))/[2]^3;
     D1=A split eps_p, eps_n; label C eps_C; scored two-term covariant all-pairs connected
     term; adjacent connected insertion (LABELLED, non-covariant, not scored);
     reading-3 feasibility (convention D: y_(1^3) = 0, so chi_(3) >= 0 and chi_(2,1) >= 0);
  3. q -> 1 order of every non-zero n - p difference, by continuation of the solution
     branches in q.

Writes nucleon-photon-colour-weights-np.witness.json next to this file.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for p in (ROOT / "tools" / "qou-substrate" / "python", ROOT / "computations"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from qou_substrate.constants import Q_50_DIGIT_STR  # proton pin (owner directive 2026-08-07)

mp.mp.dps = 70
TOL = mp.mpf(10) ** -45

# ── symbolic setup ────────────────────────────────────────────────────────────────────────────
q, h, x, y, A0s, B1s = sp.symbols("q h x y a0 b1")


def pair(a0, a1, a2, b0, b1, b2, h):
    """NF(gamma(a) gamma(b)) = QOU.QuarkState.pairNFChiral_eq."""
    return [1 + a0*b0 + a1*b1 - h*(a0*b2 + a2*b0) + h**2*a2*b2,
            a0 + b0 + h*a0*b0 + a2*b1 - h*(a2 + b2) - h**2*(a0*b2 + a2*b0) + h**3*a2*b2,
            a1 + b1 + h*a1*b1 + a0*b2 - h*a2*b2,
            a1*b0 + a2*b2 - h*a1*b2,
            a2 + b2 + a0*b1 + h*a0*b2 - h**2*a2*b2,
            a2*b0 + a1*b2]


def bor(h):
    """NF(beta_Bor) = PhotonColourWeights.borromeanNF (#8634)."""
    return [1 - h**4, -h**3 - h**5, h**3, -h**2, h**2 + h**4, 0]


def photon_nf(a0, a1, a2, h):
    """NF(gamma(a)) = QOU.QuarkState.photon_eq: [1, a0 - h a2, a1, 0, a2, 0]."""
    return [1, a0 - h*a2, a1, 0, a2, 0]


# characters on the NF basis (exact in q; h = q - 1/q)
def chi3(v, q):
    return v[0] + q*(v[1] + v[2]) + q**2*(v[3] + v[4]) + q**3*v[5]


def chi111(v, q):
    qi = 1/q
    return v[0] - qi*(v[1] + v[2]) + qi**2*(v[3] + v[4]) - qi**3*v[5]


def _mat(rows):
    return sp.Matrix(rows)


def rho21(q):
    """Reduced Burau (2,1) rep of PhotonPairNormalForm.rho: s0 -> rA, s1 -> rB."""
    rA = _mat([[q, -1/q], [0, -1/q]])
    rB = _mat([[-1/q, 0], [-q, q]])
    return rA, rB


def wp_mats(q):
    """sigma_0, sigma_1 on W_p (NucleonWeightSpaceTraces.A1, A2; 1-based sigma_1, sigma_2)."""
    A1 = _mat([[q, 0, 0], [0, 0, 1], [0, 1, q - 1/q]])
    A2 = _mat([[0, 1, 0], [1, q - 1/q, 0], [0, 0, q]])
    return A1, A2


def wn_mats(q):
    B1 = _mat([[0, 1, 0], [1, q - 1/q, 0], [0, 0, q]])
    B2 = _mat([[q, 0, 0], [0, 0, 1], [0, 1, q - 1/q]])
    return B1, B2


def nf_basis_mats(X0, X1):
    I = sp.eye(X0.shape[0])
    return [I, X0, X1, X1*X0, X0*X1, X0*X1*X0]


def nf_to_mat(v, basis):
    M = sp.zeros(*basis[0].shape)
    for c, B in zip(v, basis):
        M += c*B
    return M


Q12p = sp.diag(sp.Rational(4, 9), sp.Rational(-2, 9), sp.Rational(-2, 9))
Q23p = sp.diag(sp.Rational(-2, 9), sp.Rational(-2, 9), sp.Rational(4, 9))
Q13p = sp.diag(sp.Rational(-2, 9), sp.Rational(4, 9), sp.Rational(-2, 9))
Q12n = sp.diag(sp.Rational(-2, 9), sp.Rational(-2, 9), sp.Rational(1, 9))
Q23n = sp.diag(sp.Rational(1, 9), sp.Rational(-2, 9), sp.Rational(-2, 9))
Q13n = sp.diag(sp.Rational(-2, 9), sp.Rational(1, 9), sp.Rational(-2, 9))


def symbolic_checks() -> dict:
    """Exact identities behind P2, P3, P4 (each asserted)."""
    out = {}
    rA, rB = rho21(q)
    b21 = nf_basis_mats(rA, rB)
    chi21_basis = [sp.simplify(B.trace()) for B in b21]
    out["chi21_on_NF_basis"] = [str(c) for c in chi21_basis]
    hq = q - 1/q
    A1, A2 = wp_mats(q)
    B1, B2 = wn_mats(q)
    bp, bn = nf_basis_mats(A1, A2), nf_basis_mats(B1, B2)
    e = [[1 if i == j else 0 for i in range(6)] for j in range(6)]
    for j in range(6):
        trp = sp.simplify(nf_to_mat(e[j], bp).trace())
        trn = sp.simplify(nf_to_mat(e[j], bn).trace())
        c3 = chi3(e[j], q)
        assert sp.simplify(trp - (c3 + chi21_basis[j])) == 0, j
        assert sp.simplify(trn - (c3 + chi21_basis[j])) == 0, j
        # Q_pair is scalar: connected all-pairs = 0 for every element (P3)
        Mp, Mn = nf_to_mat(e[j], bp), nf_to_mat(e[j], bn)
        assert sp.simplify(((Q12p + Q23p + Q13p)*Mp).trace()) == 0
        assert sp.simplify(((Q12n + Q23n + Q13n)*Mn).trace() + Mn.trace()/3) == 0
    out["tr_W_p = tr_W_n = chi3 + chi21 on all six NF basis elements"] = True
    out["all-pairs connected term = 0 on all six NF basis elements (so on every element)"] = True
    # one photon: characters depend on (phi0, phi1) only through phi0 + phi1 (P4)
    p0, p1, p01 = sp.symbols("phi0 phi1 phi01")
    v = photon_nf(p0, p1, p01, hq)
    c3 = sp.expand(sp.simplify(chi3(v, q)))
    c21 = sp.expand(sp.simplify(sum(c*b for c, b in zip(v, chi21_basis))))
    s = sp.symbols("s")
    for expr in (c3, c21):
        assert sp.simplify(expr.subs(p1, s - p0) - expr.subs({p0: 0, p1: s})) == 0
    out["chi3(photon)"] = str(sp.factor(c3))
    out["chi21(photon)"] = str(sp.factor(c21))
    # pair product: characters and the swap (cyclicity, P2)
    a = sp.symbols("a0:3")
    b = sp.symbols("b0:3")
    vab = pair(*a, *b, hq)
    vba = pair(*b, *a, hq)
    for f in (lambda w: chi3(w, q), lambda w: sum(c*bb for c, bb in zip(w, chi21_basis)),
              lambda w: chi111(w, q)):
        assert sp.simplify(sp.expand(f(vab) - f(vba))) == 0
    out["characters of gamma(a)gamma(b) symmetric under a <-> b"] = True
    out["NF(gamma(a)gamma(b)) - NF(gamma(b)gamma(a))"] = [str(sp.factor(sp.expand(u - w)))
                                                           for u, w in zip(vab, vba)]
    # one-term quantum trace = Ocneanu at z_D on a single generator (control)
    zD = q**3/(q**2 + 1)
    T1_s0 = ((q**3 + q**-3)*chi3(e[1], q) + q*(chi3(e[1], q) + chi21_basis[1])
             + (1/q)*(chi3(e[1], q) + chi21_basis[1]))/(q + 1/q)**3
    assert sp.simplify(T1_s0 - zD) == 0
    out["T1(sigma_0) = z_D"] = True
    return out


# ── the solution set (PR #8634 method, h symbolic resultant) ──────────────────────────────────
def _setup_elimination():
    a1, a2 = x, y
    N = a2**2 - h*a1*a2 - a1**2
    b0 = h**2*a1/N
    b2 = -h**2*a2/N
    E = [e - t for e, t in zip(pair(A0s, a1, a2, b0, B1s, b2, h), bor(h))]
    sol = sp.solve([E[0], E[2]], [A0s, B1s], dict=True)[0]
    A0, B1 = sol[A0s], sol[B1s]
    e1 = sp.expand(sp.numer(sp.together(E[1].subs({A0s: A0, B1s: B1}))))
    e4 = sp.expand(sp.numer(sp.together(E[4].subs({A0s: A0, B1s: B1}))))
    r = sp.factor(sp.resultant(e1, e4, y))
    return dict(N=N, b0=b0, b2=b2, A0=A0, B1=B1, e1=e1, e4=e4, r=r)


ELIM = _setup_elimination()


def solve_points(hv: mp.mpf) -> list[list[mp.mpc]]:
    """All points (phi | psi) at h = hv, verified on the six original equations (< TOL)."""
    sols: list[list] = []
    fac = sp.factor_list(ELIM["r"], x)[1]
    e1, e4 = ELIM["e1"], ELIM["e4"]
    f4 = sp.lambdify((x, y, h), e4, "mpmath")
    fN = sp.lambdify((x, y, h), ELIM["N"], "mpmath")
    fv = sp.lambdify((x, y, h), [ELIM["A0"], x, y, ELIM["b0"], ELIM["B1"], ELIM["b2"]], "mpmath")
    e1y = sp.Poly(e1, y).all_coeffs()
    e1y_f = [sp.lambdify((x, h), c, "mpmath") for c in e1y]
    for f, _ in fac:
        P = sp.Poly(f, x)
        if P.degree() < 1:
            continue
        cs = [sp.lambdify(h, c, "mpmath")(hv) for c in P.all_coeffs()]
        while cs and abs(cs[0]) < TOL:
            cs = cs[1:]
        if len(cs) < 2:
            continue
        for xr in mp.polyroots(cs, maxsteps=2000, extraprec=400):
            cy = [c(xr, hv) for c in e1y_f]
            while cy and abs(cy[0]) < TOL:
                cy = cy[1:]
            if len(cy) < 2:
                continue
            for yr in mp.polyroots(cy, maxsteps=2000, extraprec=400):
                if abs(f4(xr, yr, hv)) > mp.mpf(10)**-35 or abs(fN(xr, yr, hv)) < mp.mpf(10)**-35:
                    continue
                try:
                    v = [mp.mpc(t) for t in fv(xr, yr, hv)]
                except ZeroDivisionError:
                    continue
                res = max(abs(a - b) for a, b in zip(pair(*v, hv), bor(hv)))
                if res > mp.mpf(10)**-40:
                    continue
                if all(max(abs(p - w) for p, w in zip(v, s)) > mp.mpf(10)**-25 for s in sols):
                    sols.append(v)
    sols.sort(key=lambda v: (mp.nstr(mp.re(v[1]), 20), mp.nstr(mp.re(v[2]), 20),
                             mp.nstr(mp.im(v[1]), 20)))
    return sols


def is_real(v) -> bool:
    return all(abs(mp.im(t)) < mp.mpf(10)**-40 for t in v)


# ── functionals on an NF vector at numeric q ─────────────────────────────────────────────────
def numeric_basis(qv):
    def num(M):
        return mp.matrix([[mp.mpf(sp.N(M[i, j].subs(q, sp.Float(mp.nstr(qv, 75), 80)), 80))
                           for j in range(M.shape[1])] for i in range(M.shape[0])])
    return num


def mats(qv):
    hv = qv - 1/qv
    A1 = mp.matrix([[qv, 0, 0], [0, 0, 1], [0, 1, hv]])
    A2 = mp.matrix([[0, 1, 0], [1, hv, 0], [0, 0, qv]])
    rA = mp.matrix([[qv, -1/qv], [0, -1/qv]])
    rB = mp.matrix([[-1/qv, 0], [-qv, qv]])
    return A1, A2, A2, A1, rA, rB  # W_n: sigma_0 -> B1 = A2, sigma_1 -> B2 = A1


def to_mat(v, X0, X1):
    n = X0.rows
    I = mp.eye(n)
    basis = [I, X0, X1, X1*X0, X0*X1, X0*X1*X0]
    M = mp.zeros(n, n)
    for c, B in zip(v, basis):
        M += c*B
    return M


def tr(M):
    return sum(M[i, i] for i in range(M.rows))


def diag(*d):
    M = mp.zeros(len(d), len(d))
    for i, t in enumerate(d):
        M[i, i] = mp.mpf(t)
    return M


QADJp = diag(mp.mpf(2)/9, mp.mpf(-4)/9, mp.mpf(2)/9)
QADJn = diag(mp.mpf(-1)/9, mp.mpf(-4)/9, mp.mpf(-1)/9)
QALLp = diag(0, 0, 0)
QALLn = diag(mp.mpf(-1)/3, mp.mpf(-1)/3, mp.mpf(-1)/3)


def functionals(v, qv) -> dict:
    """Every pre-registered functional of the NF element v at q = qv."""
    A1, A2, B1, B2, rA, rB = mats(qv)
    Mp, Mn = to_mat(v, A1, A2), to_mat(v, B1, B2)
    c3 = chi3(v, qv)
    c21 = tr(to_mat(v, rA, rB))
    c111 = chi111(v, qv)
    q2 = qv + 1/qv
    d3 = q2**3
    eps_p = qv*tr(Mp)/d3
    eps_n = tr(Mn)/(qv*d3)
    T1 = ((qv**3 + qv**-3)*c3 + qv*tr(Mp) + tr(Mn)/qv)/d3
    y3 = (qv**2 + 1)**2/(qv**4 + 4*qv**2 + 1)
    epsC = y3*c3 + (1 - y3)/2*c21
    allp_conn_p = qv*tr(QALLp*Mp)/d3
    allp_conn_n = (tr(QALLn*Mn) + tr(Mn)/3)/(qv*d3)
    adj_conn_p = qv*tr(QADJp*Mp)/d3
    adj_conn_n = (tr(QADJn*Mn) + mp.mpf(2)/9*tr(Mn))/(qv*d3)
    return dict(chi3=c3, chi21=c21, chi111=c111, trWp=tr(Mp), trWn=tr(Mn), eps_p=eps_p,
                eps_n=eps_n, T1=T1, epsC=epsC, allpairs_conn_p=allp_conn_p,
                allpairs_conn_n=allp_conn_n, adj_conn_p=adj_conn_p, adj_conn_n=adj_conn_n)


def reading3(F) -> str:
    c3, c21 = F["chi3"], F["chi21"]
    if abs(mp.im(c3)) > mp.mpf(10)**-40 or abs(mp.im(c21)) > mp.mpf(10)**-40:
        return "not real (reading 3 undefined)"
    ok = mp.re(c3) >= 0 and mp.re(c21) >= 0
    return "feasible" if ok else "infeasible"


def s(z, n=25):
    z = mp.mpc(z)
    if abs(mp.im(z)) < mp.mpf(10)**-40:
        return mp.nstr(mp.re(z), n)
    return mp.nstr(z, n)


def element_record(v, qv) -> dict:
    F = functionals(v, qv)
    rec = {k: s(val) for k, val in F.items()}
    rec["reading3_D"] = reading3(F)
    rec["NF"] = [s(t, 20) for t in v]
    return rec


# ── q -> 1 order of a difference along continued branches ────────────────────────────────────
def continue_points(q_from: mp.mpf, q_to: mp.mpf, start: list, steps: int = 40):
    """Track each point from q_from to q_to by nearest-neighbour matching (geometric steps in q-1)."""
    tracks = [[(q_from, p)] for p in start]
    t0, t1 = mp.log(q_from - 1), mp.log(q_to - 1)
    for k in range(1, steps + 1):
        qk = 1 + mp.exp(t0 + (t1 - t0)*k/steps)
        hk = qk - 1/qk
        pts = solve_points(hk)
        if len(pts) != len(tracks):
            raise RuntimeError(f"point count changed to {len(pts)} at q = {mp.nstr(qk, 12)}")
        hprev = tracks[0][-1][0] - 1/tracks[0][-1][0]
        used = set()
        for tr_ in tracks:
            prev = [c/hprev for c in tr_[-1][1]]   # h-normalised: the points shrink like h as q -> 1
            order = sorted(range(len(pts)),
                           key=lambda i: max(abs(a/hk - b) for a, b in zip(pts[i], prev)))
            i = next(i for i in order if i not in used)
            used.add(i)
            tr_.append((qk, pts[i]))
    return tracks


def order_estimate(vals: list[tuple]) -> str:
    """Slope of log|f| against log(q-1) on the last two points (exact zero reported as such)."""
    (qa, fa), (qb, fb) = vals[-2], vals[-1]
    if abs(fa) < mp.mpf(10)**-50 and abs(fb) < mp.mpf(10)**-50:
        return "identically 0 (|f| < 1e-50 at both)"
    return mp.nstr(mp.log(abs(fb)/abs(fa))/mp.log((qb - 1)/(qa - 1)), 6)


def main() -> int:
    out: dict = {"q0Anchor": "proton", "q0Value": Q_50_DIGIT_STR,
                 "scriptFile": "computations/probes/nucleon_photon_colour_weights/colour_weights_np_probe.py",
                 "engine": "sympy (exact) + mpmath 70 dps",
                 "bean": "qou-99qc", "preregistration": "PREREGISTRATION.md",
                 "photon": "gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^-1 (def:photon)",
                 "dps": mp.mp.dps}
    out["symbolic"] = symbolic_checks()
    out["resultant_factors_in_phi1"] = [str(f) for f, _ in sp.factor_list(ELIM["r"], x)[1]]

    # control: #8634 counts
    ctrl = {}
    for hv in (mp.mpf(1)/2, mp.mpf(2)/9):
        pts = solve_points(hv)
        ctrl[mp.nstr(hv, 6)] = {"count": len(pts), "real": sum(is_real(p) for p in pts)}
    out["control_8634"] = ctrl

    q0 = mp.mpf(Q_50_DIGIT_STR)
    h0 = q0 - 1/q0
    pts = solve_points(h0)
    out["q0"] = mp.nstr(q0, 50)
    out["points_at_q0"] = [{"phi": [s(t) for t in p[:3]], "psi": [s(t) for t in p[3:]],
                            "real": is_real(p),
                            "phi0+phi1": s(p[0] + p[1]), "psi0+psi1": s(p[3] + p[4]),
                            "is_borromean_pair": all(abs(t) < TOL for t in (p[0], p[1], p[3], p[4]))}
                           for p in pts]
    n = len(pts)
    photons = []
    for i, p in enumerate(pts):
        photons.append((f"P{i}.phi", p[:3]))
        photons.append((f"P{i}.psi", p[3:]))

    def prod(a, b, hv):
        return pair(*a, *b, hv)

    borr = bor(h0)
    # R-pt: every point multiplies to beta_Bor
    rpt = []
    for i, p in enumerate(pts):
        v = prod(p[:3], p[3:], h0)
        rpt.append(max(abs(a - b) for a, b in zip(v, borr)))
    out["R_pt"] = {"max |NF(point product) - NF(beta_Bor)| over all points": s(max(rpt), 5),
                   "consequence": "X_n = X_p = beta_Bor for all 64 (i, j); every functional agrees",
                   "beta_Bor": element_record(borr, q0)}
    # R-maj: X_p = gamma(w_u) gamma(w_d), X_n = gamma(w_d) gamma(w_u)
    rmaj = []
    maxchar = mp.mpf(0)
    for (lu, wu) in photons:
        for (ld, wd) in photons:
            if lu >= ld:
                continue
            Xp, Xn = prod(wu, wd, h0), prod(wd, wu, h0)
            Fp, Fn = functionals(Xp, q0), functionals(Xn, q0)
            dchar = max(abs(Fn[k] - Fp[k]) for k in ("chi3", "chi21", "chi111"))
            maxchar = max(maxchar, dchar)
            delem = max(abs(a - b) for a, b in zip(Xp, Xn))
            rmaj.append({
                "w_u": lu, "w_d": ld,
                "X_n == X_p": bool(delem < TOL),
                "n-p: eps_n(X_n) - eps_p(X_p)": s(Fn["eps_n"] - Fp["eps_p"]),
                "n-p: T1": s(Fn["T1"] - Fp["T1"]),
                "n-p: epsC": s(Fn["epsC"] - Fp["epsC"]),
                "n-p: two-term all-pairs connected (SCORED)": s(Fn["allpairs_conn_n"] - Fp["allpairs_conn_p"]),
                "n-p: adjacent connected (LABELLED comparison)": s(Fn["adj_conn_n"] - Fp["adj_conn_p"]),
                "reading3_p": reading3(Fp), "reading3_n": reading3(Fn),
            })
    out["R_maj"] = {"max |character difference| over all pairs": s(maxchar, 5),
                    "pairs": rmaj}
    # R-free: all products, characters + reading 3
    rfree = []
    for (la, wa) in photons:
        for (lb, wb) in photons:
            X = prod(wa, wb, h0)
            F = functionals(X, q0)
            rfree.append({"left": la, "right": lb,
                          "equals_beta_Bor": bool(max(abs(a - b) for a, b in zip(X, borr)) < TOL),
                          "chi3": s(F["chi3"], 15), "chi21": s(F["chi21"], 15),
                          "T1": s(F["T1"], 15), "eps_p": s(F["eps_p"], 15),
                          "eps_n": s(F["eps_n"], 15), "epsC": s(F["epsC"], 15),
                          "allpairs_conn_p": s(F["allpairs_conn_p"], 5),
                          "allpairs_conn_n": s(F["allpairs_conn_n"], 5),
                          "reading3_D": reading3(F)})
    out["R_free"] = rfree
    out["R_free_summary"] = {
        "products": len(rfree),
        "equal_beta_Bor": sum(r["equals_beta_Bor"] for r in rfree),
        "reading3_feasible": sum(r["reading3_D"] == "feasible" for r in rfree),
        "reading3_infeasible": sum(r["reading3_D"] == "infeasible" for r in rfree),
        "reading3_undefined_nonreal": sum(r["reading3_D"].startswith("not real") for r in rfree),
        "max_|allpairs_conn|": s(max(max(abs(mp.mpc(r["allpairs_conn_p"])), abs(mp.mpc(r["allpairs_conn_n"])))
                                     for r in rfree), 5),
    }
    # q -> 1 order of the R-maj adjacent difference, real points only
    tracks = continue_points(q0, 1 + mp.mpf(10)**-4, pts, steps=160)
    orders = []
    for (lu, wu) in photons:
        for (ld, wd) in photons:
            if lu >= ld:
                continue
            iu, cu = int(lu[1:].split(".")[0]), lu.split(".")[1]
            idd, cd = int(ld[1:].split(".")[0]), ld.split(".")[1]
            vals = []
            for k in (-2, -1):
                qk, pu = tracks[iu][k]
                _, pd = tracks[idd][k]
                hk = qk - 1/qk
                wuk = pu[:3] if cu == "phi" else pu[3:]
                wdk = pd[:3] if cd == "phi" else pd[3:]
                Fp = functionals(prod(wuk, wdk, hk), qk)
                Fn = functionals(prod(wdk, wuk, hk), qk)
                vals.append((qk, Fn["adj_conn_n"] - Fp["adj_conn_p"],
                             max(abs(a - b) for a, b in zip(prod(wuk, wdk, hk), prod(wdk, wuk, hk))),
                             Fp["T1"] - functionals(bor(hk), qk)["T1"]))
            orders.append({"w_u": lu, "w_d": ld,
                           "adjacent n-p order in (q-1)": order_estimate([(a, b) for a, b, _, _ in vals]),
                           "element |X_n - X_p| order in (q-1)": order_estimate([(a, c) for a, _, c, _ in vals]),
                           "T1(X_p) - T1(beta_Bor) order in (q-1)": order_estimate([(a, d) for a, _, _, d in vals])})
    out["R_maj_adjacent_q_to_1_order"] = orders
    out["track_endpoints_q"] = mp.nstr(tracks[0][-1][0], 10)
    out["track_endpoint_points"] = [{"phi": [s(t, 12) for t in tr_[-1][1][:3]],
                                     "psi": [s(t, 12) for t in tr_[-1][1][3:]]} for tr_ in tracks]

    path = HERE / "nucleon-photon-colour-weights-np.witness.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps({k: out[k] for k in ("control_8634", "R_free_summary")}, indent=1))
    print("points at q0:")
    for r in out["points_at_q0"]:
        print(" ", r)
    print("R_pt:", out["R_pt"]["max |NF(point product) - NF(beta_Bor)| over all points"])
    print("R_maj max char diff:", out["R_maj"]["max |character difference| over all pairs"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
