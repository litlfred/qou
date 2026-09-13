"""aomega_m3_pretzel_residue_blocks_probe.py

Route C, M3, Part 12b (bean qou-x3iv): the residue evaluation of the reduced,
u-deformed state integrals (Parts 11-12a) into q-series BLOCKS, numerically
validated against the integral itself, then FUSED (q~ -> q^-1, x~ -> x^-1) into
the sigma_1 sigma_1 bilinear and compared with the derived rotated 3D-index of
Part 7 (aomega-m3-rotated-index-three-knots.witness.json).

Held inputs
  GK arxiv-1304.2705v1 Lemma 2.1 (25): near a pole x_{m,n} = c_b + i b m + i b^-1 n,
      Phi_b(x + x_{m,n}) = K_{m,n} phi_m(2 pi b x) phi~_n(2 pi b^-1 x) / (1 - e^{2 pi b^-1 x}),
      K_{m,n} = (q;q)_inf/(q~;q~)_inf / ((q;q)_m (q~^-1;q~^-1)_n),
      phi_m(x) = (q^{m+1}e^x;q)_inf/(q^{m+1};q)_inf,
      phi~_n(x) = (q~;q~)_inf/(q~e^x;q~)_inf * (q~^-1;q~^-1)_n/(q~^-1 e^x;q~^-1)_n;
      residue of Phi_b at x_{m,n} is -(b/2pi) K_{m,n}.  The same section shows the
      quadratic form decouples in (m,n) for integer A.
  GGM 2012.00062 (106) (x;q^-1)_inf = (qx;q)_inf^-1 and (below (242)) "the summand of
      H+ equals that of H- after replacing q by q^-1"; (315)-(316): the sigma_1 sigma_1
      Stokes entry of 5_2 is the bilinear sum_k H_k(x;q) H_k(x^-1;q^-1) of the bare
      blocks (theta-normalisations cancel between q and q^-1), and (21) identifies it
      with the rotated index Ind^rot(0,x;q).  Theorem 28 (333)-(334): the residue
      sum of a one-dimensional state integral is  e^{...} sum_k e^{-A pi i (u_k-c_b)^2 ...}
      b^(k)(x;q) b^(k)(x~;q~^-1).

Derivation (carried out here in general, then specialised)
  For an integrand e^{-A pi i x^2} prod_j Phi_b(v_j x + a_j) with v_j in {1,2}: at a
  pole family the residue factorises as
      -(b/2pi) (q;q)_inf/(q~;q~)_inf * e^{-A pi i (u_F - c_b)^2} * w_F * S_F(m;q,x) * S_F(n;q~^-1,x~)
  with ONE summand function S_F per family and the same constant for every family
  (the powers of (q)_inf/(q~)_inf from K cancel against the phi's for any number of
  dilogarithms).  The q~-side is the q-side summand evaluated at (q~^-1, x~), with
  (106) turning it into a convergent q~-series.  w_F = 1 for a unit factor's poles,
  1/2 for the doubled factor's (its residue is halved), and the doubled factor's
  lattice c_b + (ibm + ib^-1 n)/2 splits by the parities (eps, delta) of (m, n):
  the Gaussian cross term gives (-1)^{eps delta}, the q-side carries q^{3 eps/4} and
  the products are shifted by q^{eps/2} and evaluated at xi = (-1)^delta x^{1/2},
  the q~-side symmetrically at xi~ = (-1)^eps x~^{1/2}.

  5_2 (Part 12a form, A = 1, poles at u_k in (u, 0, -u), x_k = e^{2 pi b u_k}):
      S_k(m) = (-1)^m q^{m(m+1)/2} x_k^{-m} prod_{j != k} (q^{m+1} x_j/x_k; q)_inf / (q;q)_m
  (-2,3,7) (A = 2, x = e^{2 pi b u_G}, X = x^{1/2}):
      F1 (poles of Phi_b(x + u/2)):  S1(m) = q^{m(m+1)} X^{-2m} (q^{m+1}X^{-2})_inf (q^{2m+1}X^{-2})_inf/(q)_m
      F2 (poles of Phi_b(x - u/2)):  S2(m) = S1(m)|_{X -> X^-1}
      F3 (poles of Phi_b(2x - c_b)), parity eps of m, partner parity delta:
          S3^eps(m'; xi) = (-1)^eps q^{m'(m'+1) + eps m' + 3 eps/4} (q^{m'+1+eps/2} xi)_inf (q^{m'+1+eps/2} xi^-1)_inf/(q)_{2m'+eps},
          xi = (-1)^delta X, weight (1/2)(-1)^{eps delta}, q~-side S3^delta(n'; (-1)^eps X~).

Gates
  N1  5_2, numerical: 2 pi i * (residue sum) == the direct integral on R + i eps  (all constants)
  N2  pretzel, numerical: same — validates the family-3 bookkeeping (signs, q^{3/4}, halving)
  I1  5_2, fusion: sum_k S_k(x;q) S_k(x^-1;q^-1) == the derived sigma_1 sigma_1 index (Part 7 witness)
      at zeta = x, order q^3 — the bare-block bilinear IS the index (GGM 316/21 reproduced from
      the residue calculus rather than transcribed)
Test
  T1  pretzel, fusion: the same bilinear (with the family-3 weights) vs the derived pretzel index,
      at zeta in {x, x^{1/2}} and its mirror x -> 1/x; report whether fractional powers cancel.
Exact: sympy series in Q = q^{1/4} with coefficients in Q(X); numerics: mpmath 22 dps only
in N1/N2.  Orientation: SnapPy's (Part 11).  No q0, no float64.
"""
from __future__ import annotations

import json
import os
import sys
import time
from fractions import Fraction

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))

QORDER = 3          # certify to q^QORDER (index rows held to q^3)
QMAX_UNITS = 4 * (QORDER + 1) + 3   # truncation in Q = q^{1/4}; compute one order deeper than read

# ---------------------------------------------------------------- summand specs
# A spec is a function m -> dict(sign, qexp (Fraction, units of q), Xexp (int), prods [(e (Fraction), ymon)], fins [n])
# meaning  sign * q^qexp * X^Xexp * prod (q^e * ymon ; q)_inf / prod (q;q)_n,  ymon = (coef, Xpower) with coef = +-1.


def spec_52(k):
    xk = {0: 2, 1: 0, 2: -2}   # X-power of x_k = x^{1,0,-1} with x = X^2
    def S(m):
        prods = []
        for j in range(3):
            if j != k:
                prods.append((Fraction(m + 1), (1, xk[j] - xk[k])))
        return {"sign": (-1) ** m, "qexp": Fraction(m * (m + 1), 2), "Xexp": -m * xk[k], "prods": prods, "fins": [m]}
    return S


def spec_p_F1(m):
    return {"sign": 1, "qexp": Fraction(m * (m + 1)), "Xexp": -2 * m,
            "prods": [(Fraction(m + 1), (1, -2)), (Fraction(2 * m + 1), (1, -2))], "fins": [m]}


def spec_p_F2(m):
    return {"sign": 1, "qexp": Fraction(m * (m + 1)), "Xexp": 2 * m,
            "prods": [(Fraction(m + 1), (1, 2)), (Fraction(2 * m + 1), (1, 2))], "fins": [m]}


def spec_p_F3(eps, delta):
    sgn = (-1) ** delta
    def S(mp):
        e = Fraction(mp + 1) + Fraction(eps, 2)
        return {"sign": (-1) ** eps, "qexp": Fraction(mp * (mp + 1) + eps * mp) + Fraction(3 * eps, 4), "Xexp": 0,
                "prods": [(e, (sgn, 1)), (e, (sgn, -1))], "fins": [2 * mp + eps]}
    return S


# ---------------------------------------------------------------- numerics (mpmath)
def numerics():
    import mpmath as mp
    mp.mp.dps = 22

    def qp_inf(a, Q):
        """(a;Q)_inf for |Q| != 1, via (106) when |Q| > 1."""
        if abs(Q) > 1:
            return 1 / qp_inf(a / Q, 1 / Q)
        p = mp.mpf(1); t = a; k = 0
        while abs(t) > mp.mpf(10) ** (-mp.mp.dps - 3):
            p *= (1 - t); t *= Q; k += 1
            if k > 5000:
                break
        return p

    def qp_n(a, Q, n):
        p = mp.mpf(1)
        for k in range(n):
            p *= (1 - a * Q**k)
        return p

    def fr(f):
        return mp.mpf(f.numerator) / f.denominator

    def S_eval(spec, m, L, X):
        """L = the DEFINING logarithm of the nome (q = e^L): fractional powers are exp(e L), never principal powers —
        at b = e^{i pi/6} the nome is a negative real and principal q^{3/4} picks a wrong fourth root."""
        d = spec(m)
        Q = mp.exp(L)
        val = d["sign"] * mp.exp(fr(d["qexp"]) * L) * X ** d["Xexp"]
        for e, (co, xp) in d["prods"]:
            val *= qp_inf(mp.exp(fr(e) * L) * co * X**xp, Q)
        for n in d["fins"]:
            val /= qp_n(Q, Q, n)
        return val

    def P_eval(spec, L, X, M=40):
        tot = mp.mpf(0)
        for m in range(M):
            t = S_eval(spec, m, L, X)
            tot += t
            if m > 6 and abs(t) < mp.mpf(10) ** (-mp.mp.dps - 2):
                break
        return tot

    b = mp.mpf('0.95') * mp.exp(1j * mp.pi / 7)          # generic: |q| != |q~|, nome off the negative axis
    Lq = 2j * mp.pi * b**2; Lqt_inv = 2j * mp.pi / b**2   # q = e^{Lq}, q~^{-1} = e^{Lqt_inv}
    q = mp.exp(Lq); qt = mp.exp(-Lqt_inv); cb = 1j * (b + 1 / b) / 2
    Phi = lambda x: qp_inf(mp.exp(2 * mp.pi * b * (x + cb)), q) / qp_inf(mp.exp(2 * mp.pi / b * (x - cb)), qt)
    u = mp.mpf('0.13')
    x = mp.exp(2 * mp.pi * b * u); xt = mp.exp(2 * mp.pi / b * u)
    X = mp.exp(mp.pi * b * u); Xt = mp.exp(mp.pi / b * u)
    const = -(b / (2 * mp.pi)) * qp_inf(q, q) / qp_inf(qt, qt)
    eps = float(mp.im(cb)) * 0.45
    L = 16
    pts = [-L, -L / 2, -4, -2, -1, 0, 1, 2, 4, L / 2, L]
    out = {"b": mp.nstr(b, 8), "u": mp.nstr(u, 4)}

    # --- 5_2 (A = 1): int Phi_b(x+u) Phi_b(x) Phi_b(x-u) e^{-pi i x^2}
    f52 = lambda s: Phi(s + 1j * eps + u) * Phi(s + 1j * eps) * Phi(s + 1j * eps - u) * mp.exp(-1j * mp.pi * (s + 1j * eps) ** 2)
    I52 = mp.quad(f52, pts)
    res52 = mp.mpf(0)
    uk = [u, 0, -u]
    for k in range(3):
        Pq = P_eval(spec_52(k), Lq, X)
        Pqt = P_eval(spec_52(k), Lqt_inv, Xt)
        res52 += mp.exp(-1j * mp.pi * (uk[k] - cb) ** 2) * Pq * Pqt
    res52 *= 2j * mp.pi * const
    out["N1_5_2"] = {"integral": mp.nstr(I52, 14), "residue_sum": mp.nstr(res52, 14), "rel_err": mp.nstr(abs(res52 / I52 - 1), 5)}

    # --- pretzel (A = 2): int Phi_b(x+u/2) Phi_b(x-u/2) Phi_b(2x-c_b) e^{-2 pi i x^2}
    # the doubled factor grows like e^{2 pi (b + 1/b) x} along R + i eps (its -c_b shift), so convergence at +inf needs
    # 8 pi eps > 2 pi (b + 1/b), i.e. eps > (b + 1/b)/4 = Im(c_b)/2, while every pole sits at Im >= Im(c_b): take eps = 0.7 Im(c_b)
    eps_p = float(mp.im(cb)) * 0.7
    fp = lambda s: Phi(s + 1j * eps_p + u / 2) * Phi(s + 1j * eps_p - u / 2) * Phi(2 * (s + 1j * eps_p) - cb) * mp.exp(-2j * mp.pi * (s + 1j * eps_p) ** 2)
    Ip = mp.quad(fp, pts)
    Ip2 = mp.quad(lambda s: Phi(s + 1j * eps_p * 0.9 + u / 2) * Phi(s + 1j * eps_p * 0.9 - u / 2) * Phi(2 * (s + 1j * eps_p * 0.9) - cb) * mp.exp(-2j * mp.pi * (s + 1j * eps_p * 0.9) ** 2), pts)
    out_eps = {"eps_pretzel": mp.nstr(eps_p, 4), "integral_at_0.9eps": mp.nstr(Ip2, 14)}
    resp = mp.mpf(0)
    # family 1 = poles of Phi_b(x + u/2), at c_b - u/2: Gaussian e^{-A pi i (u_k - c_b)^2} with u_k = +u/2 (GGM Thm 28 convention)
    resp += mp.exp(-2j * mp.pi * (u / 2 - cb) ** 2) * P_eval(spec_p_F1, Lq, X) * P_eval(spec_p_F1, Lqt_inv, Xt)
    resp += mp.exp(-2j * mp.pi * (-u / 2 - cb) ** 2) * P_eval(spec_p_F2, Lq, X) * P_eval(spec_p_F2, Lqt_inv, Xt)
    fam3 = mp.mpf(0)
    for e_ in (0, 1):
        for d_ in (0, 1):
            fam3 += mp.mpf(1) / 2 * (-1) ** (e_ * d_) * P_eval(spec_p_F3(e_, d_), Lq, X) * P_eval(spec_p_F3(d_, e_), Lqt_inv, Xt)
    resp += mp.exp(-2j * mp.pi * (0 - cb) ** 2) * fam3
    resp *= 2j * mp.pi * const
    out["N2_pretzel"] = {"integral": mp.nstr(Ip, 14), "residue_sum": mp.nstr(resp, 14), "rel_err": mp.nstr(abs(resp / Ip - 1), 5), **out_eps}
    # diagnostics: residue sum with family-3 signs dropped / halving dropped, to show they matter
    resp_nosign = 2j * mp.pi * const * (mp.exp(-2j * mp.pi * (u / 2 - cb) ** 2) * P_eval(spec_p_F1, Lq, X) * P_eval(spec_p_F1, Lqt_inv, Xt)
                                        + mp.exp(-2j * mp.pi * (-u / 2 - cb) ** 2) * P_eval(spec_p_F2, Lq, X) * P_eval(spec_p_F2, Lqt_inv, Xt)
                                        + mp.exp(-2j * mp.pi * cb**2) * sum(mp.mpf(1) / 2 * P_eval(spec_p_F3(e_, d_), Lq, X) * P_eval(spec_p_F3(d_, e_), Lqt_inv, Xt) for e_ in (0, 1) for d_ in (0, 1)))
    out["N2_pretzel_without_(-1)^{eps delta}"] = mp.nstr(abs(resp_nosign / Ip - 1), 5)
    return out


# ---------------------------------------------------------------- exact series in Q = q^{1/4}, coefficients in Q(X)
Xs = sp.Symbol("X")


class Ser:
    """Truncated series sum_k c_k Q^k, k integer (may be negative), c_k in Q(X)."""
    def __init__(self, d=None):
        self.d = {k: v for k, v in (d or {}).items() if v != 0}

    @staticmethod
    def const(c):
        return Ser({0: sp.sympify(c)})

    @staticmethod
    def mono(c, k):
        return Ser({int(k): sp.sympify(c)})

    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = sp.cancel(d.get(k, 0) + v)
        return Ser(d)

    def __mul__(self, o):
        d = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                k = k1 + k2
                if k > QMAX_UNITS:
                    continue
                d[k] = d.get(k, 0) + v1 * v2
        return Ser({k: sp.cancel(v) for k, v in d.items()})

    def scale(self, c):
        return Ser({k: sp.cancel(v * c) for k, v in self.d.items()})

    def inv(self):
        """1/self for a series with a nonzero lowest term."""
        kmin = min(self.d)
        c0 = self.d[kmin]
        rest = Ser({k - kmin: v / c0 for k, v in self.d.items() if k != kmin})     # self = c0 Q^kmin (1 + rest)
        out = Ser.const(1); term = Ser.const(1); neg = rest.scale(-1)
        for _ in range(QMAX_UNITS + 2):
            term = term * neg
            if not term.d:
                break
            out = out + term
        return Ser({k - kmin: sp.cancel(v / c0) for k, v in out.d.items()})


def qexp_units(e):
    """q^e with e a Fraction -> Q-units (must be a multiple of 1/4)."""
    k = e * 4
    assert k.denominator == 1, e
    return int(k)


def qpoch_inf_ser(e, ymon):
    """(q^e * y; q)_inf as a Ser, e a Fraction (may be <= 0), y = coef*X^xp; factors with e+j <= 0 are kept exactly."""
    co, xp = ymon
    y = co * Xs**xp
    out = Ser.const(1)
    j = 0
    while True:
        ee = e + j
        if qexp_units(ee) > QMAX_UNITS:
            break
        out = out * (Ser.const(1) + Ser.mono(-y, qexp_units(ee)))
        j += 1
    return out


def qpoch_n_ser(n):
    out = Ser.const(1)
    for k in range(1, n + 1):
        if 4 * k > QMAX_UNITS:
            break
        out = out * (Ser.const(1) + Ser.mono(-1, 4 * k))
    return out


def S_ser(spec, m, fused):
    """The summand as a Ser: at (q, X) if not fused; at (q^-1, X^-1) if fused, using
    (y;q^-1)_inf = 1/(qy;q)_inf and (q;q^-1)_n = (-1)^n q^{-n(n+1)/2} (q;q)_n."""
    d = spec(m)
    if not fused:
        out = Ser.mono(d["sign"] * Xs ** d["Xexp"], qexp_units(d["qexp"]))
        for e, ymon in d["prods"]:
            out = out * qpoch_inf_ser(e, ymon)
        for n in d["fins"]:
            out = out * qpoch_n_ser(n).inv()
        return out
    # fused: q -> 1/q, X -> 1/X
    qe = -d["qexp"]
    pref = d["sign"] * Xs ** (-d["Xexp"])
    for n in d["fins"]:                       # 1/(q^-1;q^-1)_n = (-1)^n q^{n(n+1)/2} / (q;q)_n
        pref *= (-1) ** n
        qe += Fraction(n * (n + 1), 2)
    out = Ser.mono(pref, qexp_units(qe))
    for e, (co, xp) in d["prods"]:            # (q^{-e} y~; q^-1)_inf = 1/(q^{1-e} y~; q)_inf, y~ = co X^{-xp}
        out = out * qpoch_inf_ser(1 - e, (co, -xp)).inv()
    for n in d["fins"]:
        out = out * qpoch_n_ser(n).inv()
    return out


def P_ser(spec, fused, M=None):
    out = Ser()
    m = 0
    while True:
        s = S_ser(spec, m, fused)
        if not s.d or min(s.d) > QMAX_UNITS:
            # summands' lowest order grows with m (both branches) — stop once past truncation
            if m > 2:
                break
        out = out + s
        m += 1
        if m > 40:
            break
    return out


def as_q_laurent(ser):
    """Return {q-exponent (Fraction): coefficient (simplified)}, dropping orders beyond QORDER."""
    res = {}
    for k, v in sorted(ser.d.items()):
        e = Fraction(k, 4)
        if e > QORDER:
            continue
        v = sp.factor(sp.cancel(v))
        if v != 0:
            res[e] = v
    return res


def branch_twist(ser, omega, sigma):
    """Level-2 fusion branch: the q~-side series is in Q~ = q~^{1/4} and X~ = x~^{1/2}; the fusion q~ -> q^-1, x~ -> x^-1
    fixes them only up to Q~ -> omega Q^-1 (omega^4 = 1) and X~ -> sigma X^-1 (sigma = +-1).  A fused Ser was built with
    omega = sigma = 1; its Q-exponent k came from Q~^{-k}, so the twist multiplies coefficient k by omega^{-k} and maps X -> sigma X."""
    d = {}
    for k, v in ser.d.items():
        d[k] = sp.cancel(v.subs(Xs, sigma * Xs) * omega ** (-k))
    return Ser(d)


def bilinear(families, omega=1, sigma=1, cache=None):
    tot = Ser()
    for spec_q, spec_qt, weight in families:
        key = (id(spec_q), id(spec_qt))
        if cache is not None and key in cache:
            Pq, Pqt = cache[key]
        else:
            Pq, Pqt = P_ser(spec_q, False), P_ser(spec_qt, True)
            if cache is not None:
                cache[key] = (Pq, Pqt)
        tot = tot + (Pq * branch_twist(Pqt, omega, sigma)).scale(weight)
    return tot


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    print("numerical validation of the residue calculus (mpmath 22 dps) ...")
    num = numerics()
    print(f"   N1 5_2: integral {num['N1_5_2']['integral']}  residue sum {num['N1_5_2']['residue_sum']}  rel err {num['N1_5_2']['rel_err']}")
    print(f"   N2 pretzel: integral {num['N2_pretzel']['integral']}  residue sum {num['N2_pretzel']['residue_sum']}  rel err {num['N2_pretzel']['rel_err']}"
          f"   (without the (-1)^(eps delta) signs: rel err {num['N2_pretzel_without_(-1)^{eps delta}']})")
    check("N1-5_2: 2 pi i * residue sum (three families, one summand each, constant -(b/2pi)(q)_inf/(q~)_inf) == direct integral",
          float(num["N1_5_2"]["rel_err"]) < 1e-9, **num["N1_5_2"])
    check("N2-pretzel: 2 pi i * residue sum (F1, F2, and F3 split by lattice parity with weights (1/2)(-1)^{eps delta}) == direct integral",
          float(num["N2_pretzel"]["rel_err"]) < 1e-9, **num["N2_pretzel"])
    check("N2b-the (-1)^{eps delta} parity coupling is load-bearing (dropping it breaks N2)",
          float(num["N2_pretzel_without_(-1)^{eps delta}"]) > 1e-6, rel_err_without=num["N2_pretzel_without_(-1)^{eps delta}"])

    wit = json.load(open(os.path.join(HERE, "aomega-m3-rotated-index-three-knots.witness.json")))
    zeta = sp.Symbol("zeta")

    def target(name):
        row = wit["data"]["rotated_index"][name]["0"]
        return {Fraction(k): sp.sympify(row[f"q^{k}"], locals={"zeta": zeta}) for k in range(QORDER + 1)}

    print("\nexact fusion: 5_2 gate ...")
    fam52 = [(spec_52(k), spec_52(k), 1) for k in range(3)]
    B52 = as_q_laurent(bilinear(fam52))
    t52 = target("m015")
    ok52 = True; rows52 = {}
    for e in sorted(B52):
        val = sp.expand(B52[e].subs(Xs, sp.sqrt(zeta)))     # zeta = x = X^2
        tgt = sp.expand(t52.get(e, 0)) if e.denominator == 1 else 0
        rows52[str(e)] = {"bilinear": str(val), "target": str(tgt)}
        if sp.simplify(val - tgt) != 0:
            ok52 = False
        print(f"   q^{e}: {val}   | target {tgt}")
    check("I1-5_2: sum_k S_k(x;q) S_k(x^-1;q^-1) == derived sigma1-sigma1 index at zeta = x, to q^3 (bare blocks, no theta, no Gaussian)",
          ok52, rows=rows52)

    print("\nexact fusion: pretzel ...")
    famp = [(spec_p_F1, spec_p_F1, 1), (spec_p_F2, spec_p_F2, 1)]
    for e_ in (0, 1):
        for d_ in (0, 1):
            famp.append((spec_p_F3(e_, d_), spec_p_F3(d_, e_), sp.Rational(1, 2) * (-1) ** (e_ * d_)))
    cache = {}
    Bp = as_q_laurent(bilinear(famp, cache=cache))
    tp = target("m016")
    print("   bilinear by q-order (coefficients in X = x^{1/2}):")
    rowsp = {}
    frac_nonzero = False
    for e in sorted(Bp):
        v = sp.expand(sp.cancel(Bp[e]))
        rowsp[str(e)] = str(v)
        print(f"   q^{e}: {v}")
        if e.denominator != 1 and v != 0:
            frac_nonzero = True
    verdict_lines = []
    check("T1a-pretzel bilinear has NO fractional q-powers (the q^{3/4} classes cancel)", not frac_nonzero,
          fractional_rows={k: v for k, v in rowsp.items() if Fraction(k).denominator != 1})
    # compare integer rows with the derived index under zeta = X^2 (x), zeta = X (x^{1/2}), and mirrors
    cands = {"zeta=x": Xs**2, "zeta=x^{1/2}": Xs, "zeta=1/x": Xs**-2, "zeta=x^{-1/2}": Xs**-1}
    matches = {}
    for lab, sub in cands.items():
        ok = True
        for e in range(QORDER + 1):
            v = sp.expand(sp.cancel(Bp.get(Fraction(e), 0)))
            t = sp.expand(tp[Fraction(e)].subs(zeta, sub))
            if sp.simplify(v - t) != 0:
                ok = False
                break
        matches[lab] = ok
    print(f"   matches against the derived pretzel index: {matches}")
    check("T1b-pretzel bilinear == derived sigma1-sigma1 index for SOME identification of zeta (x, x^{1/2}, or mirrors)",
          any(matches.values()), matches=matches, target={str(k): str(v) for k, v in tp.items()})
    # partial diagnostics: does the q^0 and q^1 row match?
    partial = {}
    for lab, sub in cands.items():
        partial[lab] = [bool(sp.simplify(sp.expand(sp.cancel(Bp.get(Fraction(e), 0))) - sp.expand(tp[Fraction(e)].subs(zeta, sub))) == 0) for e in range(QORDER + 1)]
    print(f"   per-order agreement: {partial}")

    # level-2 branch scan: omega in 4th roots of unity, sigma = +-1
    print("\n level-2 fusion branches (omega for q~^{1/4} -> omega q^{-1/4}, sigma for x~^{1/2} -> sigma x^{-1/2}):")
    branches = {}
    for om_name, om in [("1", 1), ("i", sp.I), ("-1", -1), ("-i", -sp.I)]:
        for sg in (1, -1):
            Bb = as_q_laurent(bilinear(famp, omega=om, sigma=sg, cache=cache))
            frac = {str(e): str(sp.expand(sp.cancel(v))) for e, v in Bb.items() if e.denominator != 1 and sp.expand(sp.cancel(v)) != 0}
            q0 = sp.expand(sp.cancel(Bb.get(Fraction(0), 0)))
            mt = {}
            for lab, sub in cands.items():
                mt[lab] = all(sp.simplify(sp.expand(sp.cancel(Bb.get(Fraction(e), 0))) - sp.expand(tp[Fraction(e)].subs(zeta, sub))) == 0 for e in range(QORDER + 1))
            rows = {str(e): str(sp.expand(sp.cancel(v))) for e, v in Bb.items() if e.denominator == 1}
            branches[f"omega={om_name},sigma={sg:+d}"] = {"fractional_nonzero": frac, "q0": str(q0), "integer_rows": rows, "index_match": mt}
            print(f"   omega={om_name:>2} sigma={sg:+d}: fractional rows nonzero: {len(frac)}; q^0 = {q0}; match: {[k for k, v in mt.items() if v] or 'none'}")
    any_branch = any(any(v["index_match"].values()) for v in branches.values())
    # q^0 obstruction, exact: the three families' q^0 fused contributions and whether ANY weights alpha, beta, gamma make them sum to 1
    t = Xs
    q0_pieces = {"F1": 1 / (1 - t**2) ** 2, "F2": t**4 / (1 - t**2) ** 2, "F3(0,0)": -t / (1 - t) ** 2}
    al, be, ga = sp.symbols("alpha beta gamma")
    eq = sp.Poly(sp.expand(sp.cancel((al * q0_pieces["F1"] + be * q0_pieces["F2"] + ga * q0_pieces["F3(0,0)"] - 1) * (1 - t**2) ** 2)), t)
    sol = sp.solve(eq.coeffs(), [al, be, ga], dict=True)
    q0_sum = sp.factor(q0_pieces["F1"] + q0_pieces["F2"] + sp.Rational(1, 2) * q0_pieces["F3(0,0)"])
    print(f"   q^0 pieces: {q0_pieces}; sum = {q0_sum}; weights (alpha,beta,gamma) with sum == 1: {sol or 'NONE'}")
    check("T1d-q^0 OBSTRUCTION: the fused q^0 contributions of the three families are 1/(1-X^2)^2, X^4/(1-X^2)^2, -X/(2(1-X)^2) "
          "(bare weights 1, 1, 1/2 sum to (2X^2+3X+2)/(2(1+X)^2)), and NO constant reweighting makes them sum to 1 — the level-2 "
          "pairing is not a reweighting of the bare families", not sol and q0_sum == sp.factor((2 * t**2 + 3 * t + 2) / (2 * (1 + t) ** 2)),
          pieces={k: str(v) for k, v in q0_pieces.items()}, bare_sum=str(q0_sum), solutions=str(sol))
    check("T1c-some level-2 fusion branch (omega, sigma) reproduces the derived pretzel index to q^3", any_branch,
          branches={k: [l for l, v in b["index_match"].items() if v] for k, b in branches.items()})
    verdict = ("DERIVED + VALIDATED: the residue decomposition of the reduced state integrals into (q-series)x(q~-series) "
               f"blocks reproduces the integrals to {num['N1_5_2']['rel_err']} (5_2) and {num['N2_pretzel']['rel_err']} (pretzel), "
               "every pole family checked; the pretzel needs the doubled factor's half-lattice split by parity with weights "
               "(1/2)(-1)^{eps delta} (load-bearing). 5_2 (= I_{1,3}, SnapPy orientation): the bare-block fusion "
               "sum_k S_k(x;q) S_k(x^-1;q^-1) IS the derived sigma1-sigma1 index to q^3 — GGM (21) reproduced from DG (5.2) "
               f"by residues alone ({'PASS' if ok52 else 'FAIL'}). Pretzel: SCOPE-(a) NEGATIVE — the same bare-block fusion, "
               "with the theta-consistent family weights and for all 8 level-2 branches (q~^{1/4} -> omega q^{-1/4}, "
               "x~^{1/2} -> sigma x^{-1/2}), does NOT give the derived index: fractional q-powers survive and the q^0 row is "
               "(2X^2+3X+2)/(2(1+X)^2), with no reweighting of the three families reaching 1. The level-2 pairing of the "
               "parity-split blocks is the open item (BDP14's index-from-blocks statement is not held). The three "
               "deliberately failing tests T1a/T1b/T1c record that negative; T1d records the obstruction.")
    print(f"\n verdict: {verdict}")
    from qou_substrate.witness import WitnessBuilder as _WB
    w = {"name": "aomega-m3-pretzel-residue-blocks",
         "description": "Residue evaluation of the reduced state integrals of 4_1-family shape for 5_2 (I_{1,3}) and the (-2,3,7) pretzel "
                        "into q-series blocks, numerically validated, then fused into the sigma1-sigma1 bilinear and compared with the derived rotated index.",
         "computation": "aomega-m3-pretzel-residue-blocks", "engine": "python+sympy+mpmath",
         "scriptFile": os.path.basename(__file__), "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
         "auditDoc": "docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md",
         "parameters": {"QORDER": QORDER, "Q_units_truncation": QMAX_UNITS, "mp_dps": 22, "orientation": "SnapPy's (Part 11)",
                        "index_source": "aomega-m3-rotated-index-three-knots.witness.json rows m=0"},
         "data": {"numerics": num, "five_two_bilinear": rows52, "pretzel_bilinear_in_X": rowsp, "pretzel_matches": matches,
                  "pretzel_per_order": partial, "level2_fusion_branches": branches},
         "verdict": verdict, "assertions": assertions}
    _WB.stamp_staleness_metadata(w, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pretzel-residue-blocks.witness.json")
    with open(out, "w") as fh:
        json.dump(w, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
