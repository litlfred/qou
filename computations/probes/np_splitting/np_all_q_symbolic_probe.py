#!/usr/bin/env python3
"""The two measured-only items of audit §27A / §28, redone over the field Q(q).

Pre-registration: np_all_q_symbolic_preregistration.md (committed before this file).
Every entry is an exact rational function of q (python-flint fmpq_poly numerator/denominator).
No float and no numeric q anywhere in the computation; numeric q appear only in the final
cross-check against the committed numeric probes.

Run: python3 -u np_all_q_symbolic_probe.py 2>&1 | tee /tmp/np_all_q_symbolic.log
"""
import sys
import time
from fractions import Fraction

import flint

T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# ---------------------------------------------------------------- Q(q)
class RF:
    """Element of Q(q): num/den, den monic, gcd(num, den) = 1."""
    __slots__ = ("n", "d")

    def __init__(self, n, d=None):
        n = flint.fmpq_poly(n)
        d = flint.fmpq_poly(1) if d is None else flint.fmpq_poly(d)
        if n == 0:
            self.n, self.d = flint.fmpq_poly(0), flint.fmpq_poly(1)
            return
        g = n.gcd(d)
        if g != 1:
            n, d = n // g, d // g
        lc = d.coeffs()[-1]
        self.n, self.d = n / lc, d / lc

    def __add__(self, o):
        o = o if isinstance(o, RF) else RF(o)
        if self.d == o.d:
            return RF(self.n + o.n, self.d)
        return RF(self.n * o.d + o.n * self.d, self.d * o.d)

    __radd__ = __add__

    def __neg__(self):
        r = RF.__new__(RF)
        r.n, r.d = -self.n, self.d
        return r

    def __sub__(self, o):
        return self + (-(o if isinstance(o, RF) else RF(o)))

    def __rsub__(self, o):
        return RF(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, RF) else RF(o)
        if self.n == 0 or o.n == 0:
            return ZERO
        return RF(self.n * o.n, self.d * o.d)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = o if isinstance(o, RF) else RF(o)
        if o.n == 0:
            raise ZeroDivisionError
        return RF(self.n * o.d, self.d * o.n)

    def __rtruediv__(self, o):
        return RF(o) / self

    def iszero(self):
        return self.n == 0

    def __bool__(self):
        return self.n != 0

    def __eq__(self, o):
        o = o if isinstance(o, RF) else RF(o)
        return self.n * o.d == o.n * self.d

    def __hash__(self):
        return hash(str(self.n)) ^ hash(str(self.d))

    def at(self, x):
        x = flint.fmpq(x.numerator, x.denominator)
        return Fraction(str(self.n(x) / self.d(x)))

    def __repr__(self):
        return f"({self.n})/({self.d})" if self.d != 1 else f"{self.n}"


ZERO = RF(0)
ONE = RF(1)
Q = RF(flint.fmpq_poly([0, 1]))
QI = ONE / Q
H = Q - QI

N = 6
D = 2 ** N
RT = [[Q, ZERO, ZERO, ZERO], [ZERO, ZERO, ONE, ZERO], [ZERO, ONE, H, ZERO], [ZERO, ZERO, ZERO, Q]]
RI = [[QI, ZERO, ZERO, ZERO], [ZERO, -H, ONE, ZERO], [ZERO, ONE, ZERO, ZERO], [ZERO, ZERO, ZERO, QI]]


def bits(s):
    return [(s >> (N - 1 - k)) & 1 for k in range(N)]


def frombits(b):
    s = 0
    for x in b:
        s = 2 * s + x
    return s


# ---------------------------------------------------- sparse matrices: dict row -> dict col -> RF
def sp_eye():
    return {i: {i: ONE} for i in range(D)}


def sp_mul(A, B):
    C = {}
    for i, Ai in A.items():
        Ci = {}
        for k, a in Ai.items():
            Bk = B.get(k)
            if not Bk:
                continue
            for j, b in Bk.items():
                Ci[j] = Ci[j] + a * b if j in Ci else a * b
        Ci = {j: v for j, v in Ci.items() if v}
        if Ci:
            C[i] = Ci
    return C


def sp_add(terms):
    C = {}
    for c, M in terms:
        c = c if isinstance(c, RF) else RF(c)
        for i, Mi in M.items():
            Ci = C.setdefault(i, {})
            for j, v in Mi.items():
                w = c * v
                Ci[j] = Ci[j] + w if j in Ci else w
    return {i: {j: v for j, v in r.items() if v} for i, r in C.items() if any(v for v in r.values())}


def two_site(i, R):
    M = {}
    for s in range(D):
        b = bits(s)
        col = 2 * b[i] + b[i + 1]
        for row in range(4):
            v = R[row][col]
            if v:
                nb = list(b)
                nb[i], nb[i + 1] = row >> 1, row & 1
                M.setdefault(frombits(nb), {})[s] = v
    return M


def site_ops(sitemats):
    M = {}
    for s in range(D):
        b = bits(s)
        rows = [([], ONE)]
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
            t = frombits(pref)
            row = M.setdefault(t, {})
            row[s] = row[s] + c if s in row else c
    return M


def word(letters):
    M = sp_eye()
    for i, inv in letters:
        M = sp_mul(M, two_site(i, RI if inv else RT))
    return M


GEN = {(i, inv): two_site(i, RI if inv else RT) for i in range(N - 1) for inv in (False, True)}
CORE = [(0, False), (1, True)] * 3 + [(3, False), (4, True)] * 3
BASE = word(CORE)
KD = {}
for s in range(D):
    z = sum(1 for x in bits(s) if x == 0)
    KD[s] = RF(flint.fmpq_poly([0] * (2 * z) + [1])) / RF(flint.fmpq_poly([0] * N + [1]))  # q^(2z-6)


def charge(b, lo):
    return sum(1 for x in b[lo:lo + 3] if x == 0) - 1


def readout(X):
    """T_X(a, b) = Σ_s K(s) (BASE·X)_{ss} over states s with block charges (a, b)."""
    T = {}
    for s in range(D):
        row = BASE.get(s)
        if not row:
            continue
        d = ZERO
        for k, a in row.items():
            x = X.get(k, {}).get(s)
            if x:
                d = d + a * x
        if not d:
            continue
        b = bits(s)
        key = (charge(b, 0), charge(b, 3))
        T[key] = T[key] + KD[s] * d if key in T else KD[s] * d
    return T


# ---------------------------------------------------------------- linear algebra over Q(q)
class Echelon:
    def __init__(self, n):
        self.n, self.rows, self.piv = n, [], []
        self.pivvals = []

    def reduce(self, v):
        v = list(v)
        for r, p in zip(self.rows, self.piv):
            if v[p]:
                f = v[p]
                v = [a - f * b for a, b in zip(v, r)]
        return v

    def add(self, v):
        v = self.reduce(v)
        nz = [k for k, x in enumerate(v) if x]
        if not nz:
            return False
        p = nz[0]
        self.pivvals.append(v[p])
        inv = ONE / v[p]
        v = [x * inv for x in v]
        # keep reduced row echelon form
        newrows = []
        for r in self.rows:
            if r[p]:
                f = r[p]
                r = [a - f * b for a, b in zip(r, v)]
            newrows.append(r)
        self.rows = newrows + [v]
        self.piv = self.piv + [p]
        return True


def perm_words(n):
    """(word, parent index, letter) in BFS order; reduced words of positive letters."""
    start = tuple(range(n))
    seen = {start: 0}
    out = [([], None, None)]
    frontier = [start]
    while frontier:
        nxt = []
        for p in frontier:
            for i in range(n - 1):
                l = list(p)
                l[i], l[i + 1] = l[i + 1], l[i]
                t = tuple(l)
                if t not in seen:
                    seen[t] = len(out)
                    out.append((out[seen[p]][0] + [(i, False)], seen[p], (i, False)))
                    nxt.append(t)
        frontier = nxt
    return out


def part_27A():
    log("§27A: sector vectors of all 720 reduced words, over Q(q)")
    words = perm_words(6)
    assert len(words) == 720
    mats = {0: sp_eye()}
    T1 = readout(mats[0])
    keys = sorted(k for k, v in T1.items() if v)
    log(f"sectors with T_1 != 0: {len(keys)}")
    E = Echelon(len(keys))
    vecs = []
    # children of a word are built from the parent matrix; free a parent after its last child
    last_child = {}
    for idx, (_, par, _) in enumerate(words):
        if par is not None:
            last_child[par] = idx
    for idx, (w, par, let) in enumerate(words):
        if par is not None:
            mats[idx] = sp_mul(mats[par], GEN[let])
            if last_child.get(par) == idx:
                del mats[par]
        T = readout(mats[idx])
        v = [T.get(k, ZERO) for k in keys]
        vecs.append(v)
        E.add(v)
        if idx not in last_child:
            mats.pop(idx, None)
        if idx % 60 == 0:
            log(f"  word {idx}/720, span dim so far {len(E.rows)}")
    dim = len(E.rows)
    log(f"P1: dim of span over Q(q) = {dim} of {len(keys)}  (predicted 10)")
    allin = all(not any(E.reduce(v)) for v in vecs)
    log(f"  every one of the 720 vectors reduces to zero against the basis: {allin}")

    uT1 = [T1[k] for k in keys]
    uQ = [RF(k[0] * k[1]) * T1[k] for k in keys]
    ua = [RF(k[0]) * T1[k] for k in keys]
    ub = [RF(k[1]) * T1[k] for k in keys]
    rT1, rQ, ra, rb = (E.reduce(u) for u in (uT1, uQ, ua, ub))
    log(f"  T_1 in span: {not any(rT1)}")
    # unknowns (κ, a1, b1): κ·rQ − a1·ra − b1·rb = 0 (c is free because T_1 is in the span)
    cols = [rQ, [-x for x in ra], [-x for x in rb]]
    M = [[cols[j][i] for j in range(3)] for i in range(len(keys))]
    ME = Echelon(3)
    for row in M:
        ME.add(row)
    rk = len(ME.rows)
    log(f"  rank of the 16x3 system for (κ, κα, κβ): {rk}  (3 means only κ = α = β = 0)")
    sol = None
    if rk == 2:
        free = [j for j in range(3) if j not in ME.piv][0]
        x = [ZERO] * 3
        x[free] = ONE
        for r, p in zip(ME.rows, ME.piv):
            x[p] = -sum((r[j] * x[j] for j in range(3) if j != p), ZERO)
        kappa, a1, b1 = x
        assert all(not sum((M[i][j] * x[j] for j in range(3)), ZERO) for i in range(len(keys)))
        alpha, beta = a1 / kappa, b1 / kappa
        log(f"  α(q) = {alpha}")
        log(f"  β(q) = {beta}")
        s = alpha + beta - ONE
        log(f"P2: α + β − 1 = {s}  (predicted 0 in Q(q))")
        log(f"    Coulomb (α = β = 0) reachable: {(not alpha) and (not beta)}")
        for qq in (Fraction(111, 100), Fraction(7, 5)):
            log(f"    at q = {qq}: α = {alpha.at(qq)} ≈ (display) {float(alpha.at(qq)):.6f}, β ≈ {float(beta.at(qq)):.6f}")
        # bar involution q -> 1/q, done exactly on the rational function
        def barq(r):
            dn, dd = r.n.degree(), r.d.degree()
            # r(1/q) = q^-dn N~(q) / (q^-dd D~(q)) with N~, D~ the reversed polynomials
            nrev = flint.fmpq_poly(list(reversed(r.n.coeffs())))
            drev = flint.fmpq_poly(list(reversed(r.d.coeffs())))
            sh = RF(flint.fmpq_poly([0] * dd + [1])) / RF(flint.fmpq_poly([0] * dn + [1]))
            return RF(nrev, drev) * sh
        log(f"    β(q) = α(1/q) exactly: {beta == barq(alpha)}")
        sol = (alpha, beta)
        excl = [alpha.d] + [x.n for x in E.pivvals + ME.pivvals] + [x.d for x in E.pivvals + ME.pivvals] + [x for x in (kappa.n,)]
        test = [Fraction(111, 100), Fraction(7, 5), Fraction(2)]
        from qou_substrate.constants import Q_50_DIGIT_STR
        test.append(Fraction(Q_50_DIGIT_STR))
        for qq in test:
            fq = flint.fmpq(qq.numerator, qq.denominator)
            bad = [str(pl) for pl in excl if pl(fq) == 0]
            log(f"    exceptional at q = {str(qq)[:14]}…: {'none' if not bad else bad}")
        log(f"    α denominator (its roots are the q where the ray normalisation κ = 1 fails): {alpha.d}")
        for r in flint.fmpz_poly([int(c * alpha.d.denom()) for c in alpha.d.coeffs()]).complex_roots():
            z = r[0]
            if abs(z.imag) < 1e-30 and z.real > 0:
                log(f"      positive real root (display only): {z.real.str(10)}")
    dens = set()
    for r in E.rows:
        for x in r:
            if x:
                dens.add(str(x.d))
    log(f"  distinct denominators in the reduced basis: {len(dens)}")
    for dd in sorted(dens, key=len):
        log(f"    {dd}")
    return dim, allin, sol


def cop(x, sites, op):
    e = [[ZERO, ONE], [ZERO, ZERO]]
    f = [[ZERO, ZERO], [ONE, ZERO]]
    K = [[Q, ZERO], [ZERO, QI]]
    Ki = [[QI, ZERO], [ZERO, Q]]
    terms = []
    for idx, i in enumerate(sites):
        m = {i: e if x == "e" else f}
        before, after = sites[:idx], sites[idx + 1:]
        if x == "e":
            for j in (before if op else after):
                m[j] = K
        else:
            for j in (after if op else before):
                m[j] = Ki
        terms.append((ONE, site_ops(m)))
    return sp_add(terms)


def casimir(sites, op):
    K = [[Q, ZERO], [ZERO, QI]]
    Ki = [[QI, ZERO], [ZERO, Q]]
    E_ = cop("e", sites, op)
    F_ = cop("f", sites, op)
    Kp = site_ops({i: K for i in sites})
    Km = site_ops({i: Ki for i in sites})
    h2 = H * H
    return sp_add([(ONE, sp_mul(F_, E_)), (Q / h2, Kp), (QI / h2, Km)])


def part_28():
    log("§28: pp − nn over Q(q) for the U_q pair Casimir and the KZ monodromy")
    T1 = readout(sp_eye())
    A, B, AB = [0, 1, 2], [3, 4, 5], list(range(6))
    out = {}
    for op in (False, True):
        X = sp_add([(ONE, casimir(AB, op)), (-ONE, casimir(A, op)), (-ONE, casimir(B, op))])
        out[f"G-q(op={op})"] = X
    beta = word([(2, False), (1, False), (0, False), (3, False), (2, False), (1, False), (4, False), (3, False), (2, False)])
    out["M"] = sp_mul(beta, beta)
    res = {}
    for name, X in out.items():
        T = readout(X)
        dE = {k: T.get(k, ZERO) / v for k, v in T1.items() if v}
        pp, pn, np_, nn = (dE[k] for k in [(1, 1), (1, 0), (0, 1), (0, 0)])
        d = pp - nn
        I = pp - pn - np_ + nn
        log(f"  {name}: pp − nn = {d}")
        log(f"  {name}: pp − pn − np + nn = {I}")
        log(f"  {name}: pn − np = {pn - np_}")
        res[name] = (d, I, dE)
    return res


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "28"):
        r28 = part_28()
        okq = not r28["G-q(op=False)"][0]
        okm = not r28["M"][0]
        ctl = bool(r28["G-q(op=True)"][0])
        log(f"P3: pp = nn in Q(q): G-q {okq}, M {okm}; control G-q(op=True) pp ≠ nn: {ctl}")
        log(f"    G-q interaction equals q + 1/q: {r28['G-q(op=False)'][1] == Q + QI}")
    if which in ("all", "27"):
        part_27A()
    log("done")
