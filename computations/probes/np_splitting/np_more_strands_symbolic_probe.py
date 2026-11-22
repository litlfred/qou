#!/usr/bin/env python3
"""Reachable pair terms on N > 6 strands, as identities in q (exact over Q(q)).

Symbolic companion of np_more_strands_probe.py, which computed the same quantities
at q = 111/100 and q = 7/5 only. Here every matrix entry is a polynomial in q with
integer coefficients (python-flint fmpz_poly), the span is computed over the field
Q(q) by fraction-free elimination, and the pair-term parameters come out as rational
functions of q. No float and no specialisation of q enters any computation.

Scaling. q*R and q*R^{-1} have polynomial entries, and K^{(x)N} times q^N does too.
A word of length L is therefore computed as q^L times its true matrix, and every
readout vector carries one scalar power of q. Spans over Q(q), and membership in
them, do not see a scalar per vector.

Readout. T_X(a, b) = Tr(K^{(x)N} Pi_ab C X), C = V_A^3 V_B^3, as in the numeric probe.
The vector (Delta E)_ab = T_X(a, b) / T_1(a, b), so a function f of the sector lies in
the Delta E span exactly when the vector T_1 * f lies in the T span. We work with the
T span (polynomial vectors) throughout.

Words. The readout is linear in X, so the span over all words of S_N equals the span
over a basis of the algebra the words generate in End(V^{(x)N}). For V two-dimensional
and generic q that algebra is the Temperley-Lieb quotient, and the images of T_w for w
fully commutative (321-avoiding) are a basis of it (Fan; Graham). So N = 8 needs the
1430 fully commutative words instead of 40320. The reduction is checked, not assumed,
at N = 6 and N = 7: there the probe also runs every word of S_N and compares the spans.

Run from the repo root:
  python3 -u computations/probes/np_splitting/np_more_strands_symbolic_probe.py [layout ...]
"""
import sys
import time

import flint
import sympy as sp

T0 = time.time()
Z = flint.fmpz_poly


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


LAYOUTS = {
    "L6": (6, (0, 1, 2), (3, 4, 5)),
    "L7s": (7, (0, 1, 2), (4, 5, 6)),
    "L7e": (7, (0, 1, 2), (3, 4, 5)),
    "L8s": (8, (0, 1, 2), (5, 6, 7)),
}

QS = sp.Symbol("q")
q = Z([0, 1])
ONE, ZERO = Z([1]), Z([0])


def to_sym(p):
    return sum(sp.Integer(int(c)) * QS ** k for k, c in enumerate(p.coeffs()))


# q*R and q*R^{-1} on the basis 00, 01, 10, 11 (Jimbo, off-diagonal block [[0,1],[1,h]])
RTq = [[q * q, ZERO, ZERO, ZERO], [ZERO, ZERO, q, ZERO], [ZERO, q, q * q - 1, ZERO], [ZERO, ZERO, ZERO, q * q]]
RIq = [[ONE, ZERO, ZERO, ZERO], [ZERO, -(q * q - 1), q, ZERO], [ZERO, q, ZERO, ZERO], [ZERO, ZERO, ZERO, ONE]]


class Span:
    """Row echelon basis over Q(q), rows are lists of fmpz_poly (fraction free)."""

    def __init__(self, m):
        self.m, self.rows, self.piv = m, [], []

    def reduce(self, v, track=False):
        v, mult = list(v), ONE
        for r, p in zip(self.rows, self.piv):
            if v[p] != 0:
                a, b = r[p], v[p]
                v = [a * x - b * y for x, y in zip(v, r)]
                mult = mult * a
                if not track:
                    v = self._prim(v)
        return (v, mult) if track else v

    @staticmethod
    def _prim(v):
        g = ZERO
        for x in v:
            if x != 0:
                g = x if g == 0 else g.gcd(x)
                if g.degree() == 0 and abs(int(g.coeffs()[0])) == 1:
                    return v
        if g == 0:
            return v
        return [x // g if x != 0 else ZERO for x in v]

    def add(self, v):
        v = self._prim(self.reduce(v))
        nz = [k for k, x in enumerate(v) if x != 0]
        if not nz:
            return False
        self.rows.append(v)
        self.piv.append(nz[0])
        return True


def fully_commutative(p):
    n = len(p)
    for j in range(1, n - 1):
        if any(p[i] > p[j] for i in range(j)) and any(p[k] < p[j] for k in range(j + 1, n)):
            return False
    return True


def run(layout, all_words=False):
    N, A, B = LAYOUTS[layout]
    Dim = 2 ** N

    def bits(s):
        return [(s >> (N - 1 - k)) & 1 for k in range(N)]

    def frombits(b):
        s = 0
        for x in b:
            s = 2 * s + x
        return s

    def two_site(i, R):
        M = {}
        for s in range(Dim):
            b = bits(s)
            col = 2 * b[i] + b[i + 1]
            for row in range(4):
                v = R[row][col]
                if v != 0:
                    nb = list(b)
                    nb[i], nb[i + 1] = row >> 1, row & 1
                    M.setdefault(frombits(nb), {})[s] = v
        return M

    def sp_mul(X, Y):
        C = {}
        for i, Xi in X.items():
            Ci = {}
            for k, a in Xi.items():
                Yk = Y.get(k)
                if not Yk:
                    continue
                for j, b in Yk.items():
                    Ci[j] = Ci[j] + a * b if j in Ci else a * b
            Ci = {j: v for j, v in Ci.items() if v != 0}
            if Ci:
                C[i] = Ci
        return C

    def eye():
        return {i: {i: ONE} for i in range(Dim)}

    GEN = {(i, inv): two_site(i, RIq if inv else RTq) for i in range(N - 1) for inv in (False, True)}
    a0, b0 = A[0], B[0]
    BASE = eye()
    for let in [(a0, False), (a0 + 1, True)] * 3 + [(b0, False), (b0 + 1, True)] * 3:
        BASE = sp_mul(BASE, GEN[let])
    KD = {s: q ** (2 * sum(1 for x in bits(s) if x == 0)) for s in range(Dim)}  # q^N K
    SECT = [(sum(1 for k in A if bits(s)[k] == 0) - 1, sum(1 for k in B if bits(s)[k] == 0) - 1)
            for s in range(Dim)]

    def readout(X):
        T = {}
        for s in range(Dim):
            row = BASE.get(s)
            if not row:
                continue
            d = ZERO
            for k, a in row.items():
                x = X.get(k, {}).get(s)
                if x is not None:
                    d += a * x
            if d != 0:
                T[SECT[s]] = T.get(SECT[s], ZERO) + KD[s] * d
        return T

    T1 = readout(eye())
    keys = sorted(k for k, v in T1.items() if v != 0)
    t1 = [T1[k] for k in keys]
    span = Span(len(keys))

    start = tuple(range(N))
    seen, frontier, count = {start}, [(start, eye())], 0
    while frontier:
        nxt = []
        for p, M in frontier:
            T = readout(M)
            span.add([T.get(k, ZERO) for k in keys])
            count += 1
            for i in range(N - 1):
                l = list(p)
                l[i], l[i + 1] = l[i + 1], l[i]
                t = tuple(l)
                if t in seen or not (all_words or fully_commutative(t)):
                    continue
                seen.add(t)
                nxt.append((t, sp_mul(M, GEN[(i, False)])))
        frontier = nxt
    dim = len(span.rows)
    kind = "all words" if all_words else "fully commutative words"
    log(f"{layout}: {count} {kind}, span dim over Q(q) {dim} of {len(keys)} sectors")

    # targets in T space: T_1 * f for f = 1, Q_a, Q_b, Q_a Q_b
    def target(f):
        return [t1[n] * int(f(k)) for n, k in enumerate(keys)]

    one_r = span.reduce(target(lambda k: 1))
    assert not any(x != 0 for x in one_r), "constant shift not reachable"
    free = [n for n in range(len(keys)) if n not in span.piv]

    def residual(f):
        v, mult = span.reduce(target(f), track=True)
        m = to_sym(mult)
        return [sp.cancel(to_sym(v[n]) / m) for n in free]

    rQ = residual(lambda k: k[0] * k[1])
    ra = residual(lambda k: k[0])
    rb = residual(lambda k: k[1])
    coulomb = all(x == 0 for x in rQ)
    out = {"layout": layout, "dim": dim, "words": count, "coulomb": coulomb}
    # pair term c + kappa*(Qa - beta)(Qb - alpha) = kappa*QaQb - kappa*alpha*Qa - kappa*beta*Qb + const;
    # columns of the 3 unknowns (kappa, kappa*alpha, kappa*beta)
    Mx = sp.Matrix([[rQ[i], -ra[i], -rb[i]] for i in range(len(free))]) if free else sp.zeros(0, 3)
    rank = Mx.rank(simplify=True) if free else 0
    out["rank"] = rank
    ns = Mx.nullspace(simplify=True) if free else [sp.eye(3)[:, j] for j in range(3)]
    if rank == 2:
        kv, kav, kbv = [sp.cancel(x) for x in ns[0]]
        al, be = sp.cancel(kav / kv), sp.cancel(kbv / kv)
        out.update(alpha=sp.factor(al), beta=sp.factor(be), sum=sp.cancel(al + be))
        log(f"  rank 2: alpha = {out['alpha']}, beta = {out['beta']}, alpha + beta = {out['sum']}")
    else:
        rel = [sp.factor(sp.cancel(x)) for x in Mx.rref(simplify=True)[0].tolist()[0]] if rank else []
        out["relation"] = rel
        log(f"  rank {rank}; relation on (kappa, kappa alpha, kappa beta): {rel}")
    log(f"  Coulomb form (Q_a Q_b alone, plus constants) reachable: {coulomb}")
    # closure of the Delta E span under (Q_a, Q_b) -> (1 - Q_b, 1 - Q_a)
    idx = {k: n for n, k in enumerate(keys)}
    closed = all((1 - k[1], 1 - k[0]) in idx for k in keys)
    if closed:
        # Delta E closure: u_k = r_{s(k)} * T1_k / T1_{s(k)}, cleared by the scalar prod_j T1_j
        def others(n):
            out = ONE
            for j, x in enumerate(t1):
                if j != n:
                    out = out * x
            return out
        oth = [others(n) for n in range(len(keys))]
        for r in span.rows:
            sw = []
            for n, k in enumerate(keys):
                m = idx[(1 - k[1], 1 - k[0])]
                sw.append(r[m] * t1[n] * oth[m])
            if any(x != 0 for x in span.reduce(sw)):
                closed = False
                break
    out["closed"] = closed
    log(f"  span closed under the sector involution: {closed}")

    # bar symmetry: Delta E span closed under v(Q_a, Q_b) -> bar(v(1 - Q_a, 1 - Q_b)), bar: q -> 1/q.
    # bar(p) = rev(p) / q^deg p with rev(p) = q^deg p * p(1/q). Entry k of the image, in T space:
    # T1_k * bar(r_m) / bar(T1_m) with m the flipped sector; cleared by q^S * prod_j rev(T1_j).
    def rev(p):
        return Z(list(reversed(p.coeffs())))

    flip = {k: (1 - k[0], 1 - k[1]) for k in keys}
    bar_closed = all(f in idx for f in flip.values())
    if bar_closed:
        rT = [rev(x) for x in t1]
        dT = [x.degree() for x in t1]
        prod_others = []
        for n in range(len(keys)):
            out_p = ONE
            for j, x in enumerate(rT):
                if j != n:
                    out_p = out_p * x
            prod_others.append(out_p)
        for r in span.rows:
            dr = [x.degree() if x != 0 else 0 for x in r]
            S = max(dr[m] - dT[m] for m in range(len(keys))) + 1
            u = []
            for n, k in enumerate(keys):
                m = idx[flip[k]]
                if r[m] == 0:
                    u.append(ZERO)
                    continue
                u.append(t1[n] * rev(r[m]) * q ** (S + dT[m] - dr[m]) * prod_others[m])
            if any(x != 0 for x in span.reduce(u)):
                bar_closed = False
                break
    out["bar_closed"] = bar_closed
    log(f"  span closed under the bar flip (q -> 1/q, Q -> 1 - Q in both blocks): {bar_closed}")
    if "alpha" in out:
        out["bar_alpha"] = sp.cancel(out["beta"] - out["alpha"].subs(QS, 1 / QS)) == 0
        log(f"  beta(q) = alpha(1/q): {out['bar_alpha']}")
    elif rank == 1 and out["relation"][0] == 1 and out["relation"][2] == 0:
        al = sp.cancel(-1 / out["relation"][1])
        out["bar_alpha"] = sp.cancel(al + al.subs(QS, 1 / QS) - 1) == 0
        log(f"  pinned alpha satisfies alpha(q) + alpha(1/q) = 1: {out['bar_alpha']}")
    return out


def main():
    lays = sys.argv[1:] or ["L6", "L7e", "L7s", "L8s"]
    res = {}
    for lay in lays:
        res[lay] = run(lay)
        if LAYOUTS[lay][0] <= 7:
            full = run(lay, all_words=True)
            same = full["dim"] == res[lay]["dim"] and full.get("alpha") == res[lay].get("alpha") \
                and full.get("relation") == res[lay].get("relation") and full["coulomb"] == res[lay]["coulomb"]
            log(f"  {lay}: fully commutative span agrees with the all-words span: {same}")
            assert same
    log("summary:")
    a6 = res.get("L6", {}).get("alpha")
    for lay, r in res.items():
        extra = ""
        if "alpha" in r:
            extra = f", alpha = {r['alpha']}, alpha + beta = {r['sum']}"
        else:
            extra = f", relation {r['relation']}"
            if a6 is not None and r["rank"] == 1 and r["relation"][0] == 1 and r["relation"][2] == 0:
                al = sp.cancel(-1 / r["relation"][1])
                extra += f"; forces alpha = {sp.factor(al)}, equal to the L6 alpha: {sp.cancel(al - a6) == 0}"
        log(f"  {lay}: dim {r['dim']}, rank {r['rank']}, closed {r['closed']}, bar-closed {r['bar_closed']}, "
            f"Coulomb {r['coulomb']}{extra}")
    log("done")


if __name__ == "__main__":
    main()
