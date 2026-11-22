#!/usr/bin/env python3
"""Two-block photon exchange: is the pair shift a charge-charge term?

Pre-registration: np_two_block_photon_exchange_preregistration.md (committed before this file).
Exact arithmetic only: sympy over Q(q); cross-checked with Fraction at q = 111/100 and 7/5.
"""
import itertools
from fractions import Fraction
import sympy as sp

N = 6


def rmat(q):
    h = q - 1 / q
    return [[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]]


def rinv(q):
    h = q - 1 / q
    return [[1 / q, 0, 0, 0], [0, -h, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1 / q]]


def bits(s):
    return [(s >> (N - 1 - k)) & 1 for k in range(N)]


def frombits(b):
    s = 0
    for x in b:
        s = 2 * s + x
    return s


def gen(i, inv, q, zero, one):
    """Sparse matrix (dict of dict) of σ_i^{±1} on (C^2)^{⊗N}."""
    R = rinv(q) if inv else rmat(q)
    M = {}
    for s in range(2 ** N):
        b = bits(s)
        col = 2 * b[i] + b[i + 1]
        for row in range(4):
            v = R[row][col]
            if v != 0:
                nb = list(b)
                nb[i], nb[i + 1] = row >> 1, row & 1
                M.setdefault(frombits(nb), {})[s] = v
    return M


def mul(A, B):
    C = {}
    for i, row in A.items():
        acc = {}
        for k, a in row.items():
            for j, b in B.get(k, {}).items():
                acc[j] = acc.get(j, 0) + a * b
        acc = {j: v for j, v in acc.items() if v != 0}
        if acc:
            C[i] = acc
    return C


def ident():
    return {s: {s: 1} for s in range(2 ** N)}


def word(letters, q):
    M = ident()
    for i, inv in letters:
        M = mul(M, gen(i, inv, q, 0, 1))
    return M


def charge(b, lo):
    return sum(1 for x in b[lo:lo + 3] if x == 0) - 1


def table(q, simp):
    V = [(0, False), (1, True)] * 3 + [(3, False), (4, True)] * 3
    base = word(V, q)
    Kd = {}
    for s in range(2 ** N):
        b = bits(s)
        z = sum(1 for x in b if x == 0)
        Kd[s] = q ** z * (1 / q) ** (N - z)
    inserts = {
        "1": [],
        "s2": [(2, False)],
        "s2^-1": [(2, True)],
        "s1 s2^-1": [(1, False), (2, True)],
        "s2 s3^-1": [(2, False), (3, True)],
        "s2^2": [(2, False), (2, False)],
        "s2^-2": [(2, True), (2, True)],
    }
    out = {}
    for name, X in inserts.items():
        W = mul(base, word(X, q))
        T = {}
        for s in range(2 ** N):
            d = W.get(s, {}).get(s, 0)
            if d == 0:
                continue
            b = bits(s)
            key = (charge(b, 0), charge(b, 3))
            T[key] = T.get(key, 0) + Kd[s] * d
        out[name] = {k: simp(v) for k, v in T.items()}
    return out


def analyse(tab, simp, label):
    Qs = [-1, 0, 1, 2]
    T1 = tab["1"]
    names = {1: "p", 0: "n", -1: "Δ-", 2: "Δ++"}
    print(f"\n===== {label} =====")
    verdicts = {}
    for name, T in tab.items():
        if name == "1":
            continue
        dE = {}
        for a in Qs:
            for b in Qs:
                t1 = T1.get((a, b), 0)
                if t1 == 0:
                    continue
                dE[(a, b)] = simp(T.get((a, b), 0) / t1)
        print(f"\n-- X = {name}")
        for a in Qs:
            print("   " + "  ".join(f"{names[a]}{names[b]}: {dE.get((a,b),'—')}" for b in Qs))
        # fit c + α Qa + β Qb + κ QaQb on all valid sectors (exact least residual via 4 pts, then check)
        c, al, be, ka = sp.symbols("c al be ka")
        eqs = [sp.Eq(c + al * a + be * b + ka * a * b, v) for (a, b), v in dE.items()]
        sol = sp.solve(eqs, [c, al, be, ka], dict=True)
        if not sol:
            v = "O4 (not affine-bilinear in charge)"
        else:
            s = {k: simp(x) for k, x in sol[0].items()}
            if s[ka] == 0:
                v = f"no bilinear term (κ=0); α={s[al]}, β={s[be]}"
            elif s[al] == 0 and s[be] == 0:
                v = f"O1 Coulomb form, κ = {s[ka]}"
            elif simp(s[al] + s[ka] / 2) == 0 and simp(s[be] + s[ka] / 2) == 0:
                v = f"O2 isospin form, κ_W = {simp(s[ka]/4)}"
            else:
                v = f"O3 affine-bilinear: α={s[al]}, β={s[be]}, κ={s[ka]}"
        # nucleon pairs only
        nuc = {k: dE[k] for k in [(1, 1), (1, 0), (0, 1), (0, 0)] if k in dE}
        pp, pn, np_, nn = (nuc.get(k) for k in [(1, 1), (1, 0), (0, 1), (0, 0)])
        nv = []
        if None not in (pp, pn, np_, nn):
            if simp(pn - nn) == 0 and simp(np_ - nn) == 0 and simp(pp - nn) != 0:
                nv.append("nucleons: Coulomb-like (pn = np = nn ≠ pp)")
            if simp(pp - nn) == 0 and simp(pn - pp) != 0:
                nv.append("nucleons: charge-symmetric (pp = nn ≠ pn)")
            nv.append(f"pp−pn−np+nn = {simp(pp - pn - np_ + nn)}")
        print("   verdict:", v)
        print("   " + "; ".join(nv))
        verdicts[name] = v
    return verdicts


if __name__ == "__main__":
    q = sp.symbols("q", positive=True)
    simp = lambda e: sp.factor(sp.cancel(e))
    vs = analyse(table(q, simp), simp, "symbolic Q(q)")
    for qq in (Fraction(111, 100), Fraction(7, 5)):
        vf = analyse(table(qq, lambda e: e), lambda e: Fraction(e) if not isinstance(e, sp.Basic) else sp.nsimplify(e),
                     f"q = {qq}")
    # Nucleon pairs at the proton pin (display only; exact rational functions evaluated at 50 digits).
    import mpmath as mp
    from qou_substrate.constants import Q_50_DIGIT_STR
    mp.mp.dps = 50
    q0 = sp.Rational(Q_50_DIGIT_STR)
    tab = table(q, simp)
    print("\n===== nucleon pairs at the proton q0 =====")
    for name, T in tab.items():
        if name == "1":
            continue
        d = {k: sp.cancel(T[k] / tab["1"][k]).subs(q, q0) for k in [(1, 1), (1, 0), (0, 1), (0, 0)]}
        pp, pn, np_, nn = (mp.mpf(sp.N(d[k], 50)) for k in [(1, 1), (1, 0), (0, 1), (0, 0)])
        I = pp - pn - np_ + nn
        print(f"{name:9s} pp={mp.nstr(pp,10)} pn={mp.nstr(pn,10)} np={mp.nstr(np_,10)} nn={mp.nstr(nn,10)} "
              f"I={mp.nstr(I,8)} (pp-nn)/I={mp.nstr((pp-nn)/I,6)} (pn-np)/I={mp.nstr((pn-np_)/I,6)}")
