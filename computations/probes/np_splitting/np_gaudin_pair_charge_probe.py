#!/usr/bin/env python3
"""Gaudin / KZ pair coupling between two nucleon blocks: is it a Coulomb term?

Pre-registration: np_gaudin_pair_charge_preregistration.md (committed before this file).
Exact arithmetic only: Fraction at q = 111/100, 7/5, 2 and at the proton q0 as an exact rational.
"""
from fractions import Fraction as F
import itertools

N = 6
D = 2 ** N


def bits(s):
    return [(s >> (N - 1 - k)) & 1 for k in range(N)]


def frombits(b):
    s = 0
    for x in b:
        s = 2 * s + x
    return s


def zeros():
    return [[F(0)] * D for _ in range(D)]


def eye():
    M = zeros()
    for i in range(D):
        M[i][i] = F(1)
    return M


def mul(A, B):
    C = zeros()
    for i in range(D):
        Ai = A[i]
        Ci = C[i]
        for k in range(D):
            a = Ai[k]
            if a:
                Bk = B[k]
                for j in range(D):
                    b = Bk[j]
                    if b:
                        Ci[j] += a * b
    return C


def add(*Ms, coeffs=None):
    coeffs = coeffs or [1] * len(Ms)
    C = zeros()
    for M, c in zip(Ms, coeffs):
        for i in range(D):
            for j in range(D):
                if M[i][j]:
                    C[i][j] += c * M[i][j]
    return C


def site_ops(sitemats):
    """Tensor product of 2x2 matrices given per site (dict site->2x2, identity elsewhere)."""
    M = zeros()
    for s in range(D):
        b = bits(s)
        # column s; build rows
        rows = [([], F(1))]
        for k in range(N):
            m = sitemats.get(k)
            new = []
            for pref, c in rows:
                if m is None:
                    new.append((pref + [b[k]], c))
                else:
                    for r in range(2):
                        v = m[r][b[k]]
                        if v:
                            new.append((pref + [r], c * v))
            rows = new
        for pref, c in rows:
            M[frombits(pref)][s] += c
    return M


def two_site(i, R):
    """4x4 R on sites (i, i+1)."""
    M = zeros()
    for s in range(D):
        b = bits(s)
        col = 2 * b[i] + b[i + 1]
        for row in range(4):
            v = R[row][col]
            if v:
                nb = list(b)
                nb[i], nb[i + 1] = row >> 1, row & 1
                M[frombits(nb)][s] += v
    return M


def setup(q):
    h = q - 1 / q
    Rt = [[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]]
    Ri = [[1 / q, 0, 0, 0], [0, -h, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1 / q]]
    Rt = [[F(x) for x in r] for r in Rt]
    Ri = [[F(x) for x in r] for r in Ri]
    e = [[0, 1], [0, 0]]
    f = [[0, 0], [1, 0]]
    K = [[q, 0], [0, 1 / q]]
    Ki = [[1 / q, 0], [0, q]]
    hm = [[1, 0], [0, -1]]
    I2 = [[1, 0], [0, 1]]
    E11 = [[1, 0], [0, 0]]
    return dict(q=q, h=h, Rt=Rt, Ri=Ri, e=e, f=f, K=K, Ki=Ki, hm=hm, I2=I2, E11=E11)


def word(S, letters):
    M = eye()
    for i, inv in letters:
        M = mul(M, two_site(i, S["Ri"] if inv else S["Rt"]))
    return M


def cop(S, x, sites, op):
    """Coproduct of e or f over the given ordered sites.
    op=False: Δe = e⊗K + 1⊗e, Δf = f⊗1 + K^-1⊗f.  op=True: the opposite coproduct."""
    terms = []
    for idx, i in enumerate(sites):
        m = {i: S[x]}
        before, after = sites[:idx], sites[idx + 1:]
        if x == "e":
            for j in (before if op else after):
                m[j] = S["K"]
        else:
            for j in (after if op else before):
                m[j] = S["Ki"]
        terms.append(site_ops(m))
    return add(*terms)


def Kop(S, sites):
    return site_ops({i: S["K"] for i in sites}), site_ops({i: S["Ki"] for i in sites})


def casimir(S, sites, op):
    q, h = S["q"], S["h"]
    E = cop(S, "e", sites, op)
    Fm = cop(S, "f", sites, op)
    Kp, Km = Kop(S, sites)
    return add(mul(Fm, E), Kp, Km, coeffs=[1, q / h ** 2, (1 / q) / h ** 2])


def commutes(A, B):
    AB, BA = mul(A, B), mul(B, A)
    return all(AB[i][j] == BA[i][j] for i in range(D) for j in range(D))


def charge(b, lo):
    return sum(1 for x in b[lo:lo + 3] if x == 0) - 1


def readout(S, base, Kd, X):
    W = mul(base, X)
    T = {}
    for s in range(D):
        d = W[s][s]
        if d == 0:
            continue
        b = bits(s)
        key = (charge(b, 0), charge(b, 3))
        T[key] = T.get(key, 0) + Kd[s] * d
    return T


def solve4(pts):
    """Fit c + al Qa + be Qb + ka QaQb exactly on all points; None if inconsistent."""
    import sympy as sp
    c, al, be, ka = sp.symbols("c al be ka")
    eqs = [sp.Eq(c + al * a + be * b + ka * a * b, sp.Rational(v.numerator, v.denominator)) for (a, b), v in pts.items()]
    sol = sp.solve(eqs, [c, al, be, ka], dict=True)
    return sol[0] if sol else None


def classify(dE):
    import sympy as sp
    s = solve4(dE)
    if s is None:
        return "O4 (not affine-bilinear in Q)", None
    c, al, be, ka = (s.get(sp.Symbol(n), 0) for n in ("c", "al", "be", "ka"))
    if ka == 0:
        return f"κ = 0: c={c}, α={al}, β={be}", s
    if al == 0 and be == 0:
        return f"O1 Coulomb, κ={ka}", s
    if al + ka / 2 == 0 and be + ka / 2 == 0:
        return f"O2 isospin, κ_W={ka/4}", s
    return f"O3 affine-bilinear: (Qa-{-be/ka})(Qb-{-al/ka})·{ka} + const;  α'+β' = {(-be-al)/ka}", s


def run(q, label, full=True):
    """full=False (the 50-digit q0): skip the centrality check and print exact differences only when small."""
    S = setup(q)
    print(f"\n========== {label} ==========")
    A, B, AB = [0, 1, 2], [3, 4, 5], list(range(6))
    # which coproduct commutes with the Jimbo braiding?
    R01 = two_site(0, S["Rt"])
    for op in (False, True):
        ok = commutes(R01, cop(S, "e", [0, 1], op)) and commutes(R01, cop(S, "f", [0, 1], op))
        print(f"coproduct op={op}: commutes with Ř on sites 0,1: {ok}")
    V = [(0, False), (1, True)] * 3 + [(3, False), (4, True)] * 3
    base = word(S, V)
    Kd = {}
    for s in range(D):
        z = sum(1 for x in bits(s) if x == 0)
        Kd[s] = q ** z * (1 / q) ** (N - z)
    T1 = readout(S, base, Kd, eye())
    X = {}
    hh = add(*[site_ops({i: S["hm"], j: S["hm"]}) for i in A for j in B])
    ef = add(*[site_ops({i: S["e"], j: S["f"]}) for i in A for j in B])
    fe = add(*[site_ops({i: S["f"], j: S["e"]}) for i in A for j in B])
    X["G-sl2"] = add(hh, ef, fe, coeffs=[F(1, 2), 1, 1])
    X["G-cartan"] = hh
    P = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
    # P_ij for non-adjacent sites: build via site_ops of Σ E_ab⊗E_ba
    Eab = {(a, b): [[1 if (r, c) == (a, b) else 0 for c in range(2)] for r in range(2)] for a in range(2) for b in range(2)}
    X["G-gl2"] = add(*[site_ops({i: Eab[(a, b)], j: Eab[(b, a)]}) for i in A for j in B for a in range(2) for b in range(2)])
    qc = [[F(2, 3), 0], [0, F(-1, 3)]]
    X["QQ"] = add(*[site_ops({i: qc, j: qc}) for i in A for j in B])
    for op in (False, True):
        CAB, CA, CB = casimir(S, AB, op), casimir(S, A, op), casimir(S, B, op)
        if full:
            EAB = cop(S, "e", AB, op)
            print(f"  C_AB central (op={op}): {commutes(CAB, EAB)}")
        X[f"G-q(op={op})"] = add(CAB, CA, CB, coeffs=[1, -1, -1])
    beta = word(S, [(2, False), (1, False), (0, False), (3, False), (2, False), (1, False), (4, False), (3, False), (2, False)])
    X["M"] = mul(beta, beta)
    out = {}
    for name, Xm in X.items():
        T = readout(S, base, Kd, Xm)
        dE = {k: T.get(k, 0) / v for k, v in T1.items()}
        v, s = classify(dE)
        nuc = [dE[k] for k in [(1, 1), (1, 0), (0, 1), (0, 0)]]
        pp, pn, np_, nn = nuc
        print(f"\n-- X = {name}: {v}")
        print(f"   pp={float(pp):.10g} pn={float(pn):.10g} np={float(np_):.10g} nn={float(nn):.10g}  (display only)")
        print(f"   exact: pp-nn = {pp-nn};  pp-pn-np+nn = {pp-pn-np_+nn}" if full else f"   exact: pp-nn == 0: {pp == nn};  pp-pn-np+nn == q+1/q: {pp-pn-np_+nn == q + 1/q}")
        out[name] = (v, dE)
    return out


if __name__ == "__main__":
    for qq in (F(111, 100), F(7, 5), F(2)):
        run(qq, f"q = {qq}")
    from qou_substrate.constants import Q_50_DIGIT_STR
    q0 = F(Q_50_DIGIT_STR)
    run(q0, "proton q0 (exact rational of the 50-digit pin)", full=False)
