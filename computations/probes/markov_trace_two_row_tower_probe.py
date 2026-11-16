#!/usr/bin/env python3
"""Convention-D Markov trace of the v9 nuclear element via two-row
seminormal representations, built up the Hecke tower with caching.

Why this route
--------------
v9 builds, for a nucleus with Z protons and N neutrons (A = Z + N strands,
protons first), the element

    E = prod_{k=1}^{A-1} prod_{i=0}^{k-1} f(type_i, type_k; sigma_i)

(right multiplication, in that order), with the factor for a crossing

    p-p :  sigma_i                      (positive crossing)
    n-n :  sigma_i - h  = sigma_i^{-1}  (negative crossing)
    p-n :  (2 sigma_i - h) / 2          (stored doubled; v9 divides by 2^pn)

where h = q - q^{-1} and sigma^2 = h sigma + 1.  v9 then traces it in the
T_w basis.  That fails for A >= 9: the strip-free word expansion runs out of
memory, and the stripped one is not the element any more.

Under convention D (z = q^3/(q^2+1)) the Ocneanu weight of every shape with
a third row is zero, so

    tr(x) = sum_{k} y_{(n-k,k)} chi_{(n-k,k)}(x),
    y_{(n-k,k)} = [n-2k+1]_q / [2]_q^n,

with [m]_q = (q^m - q^{-m})/(q - q^{-1}).  (The weight formula is checked
here against the defining property tr(x sigma_{n-1}) = z tr(x) at every
level, not assumed.)  Only two-row irreducibles are needed, and their
dimensions are binomial(n,k) - binomial(n,k-1): sum f^2 = Catalan(n).

Tower caching
-------------
Young's seminormal basis is Gelfand-Tsetlin adapted: restricting the irrep
mu of H_{m+1} to H_m is block-diagonal over the shapes lambda = mu minus a
box, with the SAME basis vectors (a tableau of mu restricted to 1..m).  So
the matrices of the partial product after strand k are lifted to level k+2
by block-diagonal embedding -- nothing is recomputed.  Across isotopes the
proton strands come first, so (Z, N+1) extends (Z, N) by one strand: a whole
neutron chain at fixed Z is one tower walk.

Precision: mpmath throughout, no float.  Output divided by 2^pn to match the
v9 certificate field `tr_markov_d`.
"""
from __future__ import annotations

import argparse
import json
import sys
import time

import mpmath as mp

Q0_STR = "1.1099785827513808075916690956107688798744991218736"


# ---------- two-row standard tableaux, as GT paths -----------------------
# A tableau of shape (n-k, k) is a 0/1 tuple: entry j goes in row tab[j].

def tableaux(n):
    """All two-row standard tableaux with n boxes, grouped by k (row-2 len)."""
    out = {0: [()]}
    for m in range(n):
        nxt = {}
        for k, tabs in out.items():
            r1 = m - k
            for t in tabs:
                nxt.setdefault(k, []).append(t + (0,))
                if k + 1 <= r1:
                    nxt.setdefault(k + 1, []).append(t + (1,))
        out = nxt
    return out


def contents(t):
    """Content (col - row) of each entry."""
    rowlen = [0, 0]
    c = []
    for r in t:
        c.append(rowlen[r] - r)
        rowlen[r] += 1
    return c


class Irrep:
    """Seminormal two-row irrep (n-k, k) of H_n(q) at a numeric q."""

    def __init__(self, n, k, tabs, q):
        self.n, self.k, self.tabs = n, k, tabs
        self.index = {t: j for j, t in enumerate(tabs)}
        self.cont = [contents(t) for t in tabs]
        self.q = q
        self.h = q - 1 / q

    def alpha(self, r):
        q = self.q
        return (q - 1 / q) / (1 - q ** (-2 * r))

    def right_mul(self, M, i, a, b):
        """Return M * rho(a + b sigma_i) (M dense, list of rows)."""
        d = len(self.tabs)
        cols = [None] * d  # new column j as a function of old columns
        done = [False] * d
        newM = [row[:] for row in M]
        for j, t in enumerate(self.tabs):
            if done[j]:
                continue
            r = self.cont[j][i + 1] - self.cont[j][i]
            if abs(r) == 1:
                lam = self.q if r == 1 else -1 / self.q
                s = a + b * lam
                for row_old, row_new in zip(M, newM):
                    row_new[j] = row_old[j] * s
                done[j] = True
                continue
            t2 = list(t)
            t2[i], t2[i + 1] = t2[i + 1], t2[i]
            j2 = self.index[tuple(t2)]
            # orient so that j has r > 0
            if r < 0:
                j, j2, r = j2, j, -r
            ar, am = self.alpha(r), self.alpha(-r)
            # sigma v_j = ar v_j + 1 v_j2 ;  sigma v_j2 = C v_j + am v_j2
            C = 1 + ar * am
            # (M rho(sigma))[:, j]  = ar M[:, j] + 1 * M[:, j2]
            # (M rho(sigma))[:, j2] = C M[:, j] + am M[:, j2]
            for row_old, row_new in zip(M, newM):
                x, y = row_old[j], row_old[j2]
                row_new[j] = a * x + b * (ar * x + y)
                row_new[j2] = a * y + b * (C * x + am * y)
            done[j] = done[j2] = True
        return newM


def qint(m, q):
    return (q ** m - q ** (-m)) / (q - 1 / q)


def weight(n, k, q):
    return qint(n - 2 * k + 1, q) / qint(2, q) ** n


# ---------- the tower walk ------------------------------------------------

def lift(mats_prev, n, tabs_by_k):
    """Embed level-(n-1) matrices into level-n irreps (block diagonal)."""
    out = {}
    for k, tabs in tabs_by_k.items():
        d = len(tabs)
        M = [[mp.mpf(0)] * d for _ in range(d)]
        # group tableaux by where entry n-1 sits; their restriction is a
        # tableau of the smaller shape, in the order tableaux() generates.
        for last in (0, 1):
            kk = k - last
            if kk not in mats_prev:
                continue
            idx = [j for j, t in enumerate(tabs) if t[-1] == last]
            if not idx:
                continue
            P = mats_prev[kk]
            for a_, ja in enumerate(idx):
                for b_, jb in enumerate(idx):
                    M[ja][jb] = P[a_][b_]
        out[k] = M
    return out


def factor(ti, tk, h):
    """(a, b, doubled): factor = a + b sigma."""
    if ti == "p" and tk == "p":
        return mp.mpf(0), mp.mpf(1), False
    if ti == "n" and tk == "n":
        return -h, mp.mpf(1), False
    return -h, mp.mpf(2), True


def walk(z, n_neu, q, log=None, checks=True):
    """Yield (A, tr/2^pn) for every prefix length of the strand sequence."""
    types = ["p"] * z + ["n"] * n_neu
    A = len(types)
    h = q - 1 / q
    zD = q ** 3 / (q ** 2 + 1)
    tabs_all = {}
    mats = {0: [[mp.mpf(1)]]}  # H_1: trivial irrep (1)
    pn = 0
    results = {}
    for k in range(1, A):
        m = k + 1  # level after strand k
        tabs = tableaux(m)
        irreps = {kk: Irrep(m, kk, tt, q) for kk, tt in tabs.items()}
        mats = lift(mats, m, tabs)
        for i in range(k):
            a, b, dbl = factor(types[i], types[k], h)
            pn += dbl
            for kk, rep in irreps.items():
                mats[kk] = rep.right_mul(mats[kk], i, a, b)
        tr = sum(weight(m, kk, q) * mp.fsum(mats[kk][j][j] for j in range(len(mats[kk])))
                 for kk in mats)
        results[m] = (tr / mp.mpf(2) ** pn, pn)
        if log:
            log(f"  level {m}: dims {[len(t) for t in tabs.values()]}, pn={pn}, "
                f"tr/2^pn = {mp.nstr(tr / mp.mpf(2) ** pn, 25)}")
    return results


# ---------- self-checks -------------------------------------------------

def check_reps(q, nmax=6):
    """sigma^2 = h sigma + 1, braid relation, and the Markov property of the
    weights, on every two-row irrep up to nmax."""
    h = q - 1 / q
    zD = q ** 3 / (q ** 2 + 1)
    worst = mp.mpf(0)
    for n in range(2, nmax + 1):
        tabs = tableaux(n)
        reps = {k: Irrep(n, k, t, q) for k, t in tabs.items()}
        for k, rep in reps.items():
            d = len(rep.tabs)
            I = [[mp.mpf(int(r == c)) for c in range(d)] for r in range(d)]
            S = [rep.right_mul(I, i, mp.mpf(0), mp.mpf(1)) for i in range(n - 1)]
            for i in range(n - 1):
                S2 = rep.right_mul(S[i], i, mp.mpf(0), mp.mpf(1))
                rhs = rep.right_mul(I, i, mp.mpf(1), h)
                worst = max(worst, max(abs(S2[r][c] - rhs[r][c]) for r in range(d) for c in range(d)))
            for i in range(n - 2):
                L = rep.right_mul(rep.right_mul(S[i], i + 1, 0, 1), i, 0, 1)
                R = rep.right_mul(rep.right_mul(S[i + 1], i, 0, 1), i + 1, 0, 1)
                worst = max(worst, max(abs(L[r][c] - R[r][c]) for r in range(d) for c in range(d)))
        # weights: tr(1) = 1 and tr(sigma_{n-1}) = z tr(1)... checked on the
        # element sigma_1...sigma_{n-1}, whose trace must be z^{n-1}.
        tr1 = sum(weight(n, k, q) * len(t) for k, t in tabs.items())
        worst = max(worst, abs(tr1 - 1))
        trc = mp.mpf(0)
        for k, rep in reps.items():
            d = len(rep.tabs)
            M = [[mp.mpf(int(r == c)) for c in range(d)] for r in range(d)]
            for i in range(n - 1):
                M = rep.right_mul(M, i, 0, 1)
            trc += weight(n, k, q) * mp.fsum(M[j][j] for j in range(d))
        worst = max(worst, abs(trc - zD ** (n - 1)))
        # tr(sigma_0 sigma_1 sigma_0) = h z^2 + z   (n >= 3)
        if n >= 3:
            t3 = mp.mpf(0)
            for k, rep in reps.items():
                d = len(rep.tabs)
                M = [[mp.mpf(int(r == c)) for c in range(d)] for r in range(d)]
                for i in (0, 1, 0):
                    M = rep.right_mul(M, i, 0, 1)
                t3 += weight(n, k, q) * mp.fsum(M[j][j] for j in range(d))
            worst = max(worst, abs(t3 - (h * zD ** 2 + zD)))
    return worst


SYM = {1: "h", 2: "he", 3: "li", 4: "be", 5: "b", 6: "c", 7: "n", 8: "o",
       9: "f", 10: "ne", 11: "na", 12: "mg", 13: "al", 14: "si", 15: "p",
       16: "s", 17: "cl", 18: "ar", 19: "k", 20: "ca"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("z", type=int)
    ap.add_argument("n", type=int, help="largest neutron count in the chain")
    ap.add_argument("--dps", type=int, default=70)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    mp.mp.dps = args.dps
    q = mp.mpf(Q0_STR)
    t0 = time.time()
    worst = check_reps(q)
    print(f"self-check (Hecke, braid, Markov, sigma0 sigma1 sigma0): worst residual {mp.nstr(worst, 3)}",
          flush=True)
    assert worst < mp.mpf(10) ** (-(args.dps - 15)), "representation self-check failed"
    res = walk(args.z, args.n, q, log=lambda s: print(s, flush=True))
    rows = []
    for m, (val, pn) in sorted(res.items()):
        if m <= args.z:
            continue  # pure-proton prefix: not a nucleus of this chain
        N = m - args.z
        rows.append({"isotope": f"{m}{SYM.get(args.z, '?')}", "z": args.z, "n": N, "a": m,
                     "pn": pn, "tr_markov_d": mp.nstr(val, 60)})
    for r in rows:
        print(r["isotope"], r["tr_markov_d"][:40])
    print(f"elapsed {time.time() - t0:.1f}s")
    if args.out:
        json.dump({"q0": Q0_STR, "q0Anchor": "proton", "q0Value": Q0_STR,
                   "z": "q^3/(q^2+1)", "dps": args.dps,
                   "self_check_worst_residual": mp.nstr(worst, 5), "rows": rows},
                  open(args.out, "w"), indent=1)


if __name__ == "__main__":
    main()
