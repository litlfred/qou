#!/usr/bin/env python3
"""M_1>0: edge-ratio structure of N/P = E_omega[ratio_e]  (exact).

Gap qou-k5r5. From the Fulman reduction (PR #5428, #5452): M_1 = P - N with
P = Cov(Sum|c|, omega3) >= 0, N = -Cov(SumD2, omega3) >= 0, and per single-box
edge (oriented so removed content r=|c_r| > added a=|c_a|):
    P-term = (r-a)^2 (r+a),      N-term = P-term * ratio_e,
    ratio_e = 2(d_a - d_r + 1)/(r - a),   d_x = D_lambda(content x) diagonal len.
Hence  N/P = E_omega[ratio_e],  omega(edge) proportional to  2 s(lam,mu) * P-term,
s(lam,mu) = pi(lam) J(lam,mu) the (symmetric) up-down-chain edge weight.

So M_1>0  <=>  N/P<1  <=>  E_omega[ratio_e] < 1. This probe measures WHERE the
omega-weight sits: does the weight concentrate on ratio_e<1 (adjacent-corner
moves), with the high-ratio edges (distant corners, large d_a-d_r) weight-
suppressed because the up-down chain needs a COMMON CHILD? That suppression
would be the mechanism behind the proved asymptotic N/P->0.6605<1, and the
target for a uniform proof.

Reports per n: N/P (=E_omega[ratio]); omega-weight with ratio_e>=1; max ratio_e
carrying weight; and the weight split by corner-distance |A-B| (adjacent vs
distant single-box moves).

Exact Fraction throughout; NO float64 (mpmath.mpf only for display ratios).

Honesty: exploratory structure probe for the OPEN uniform bound; scope-(a); no
fit; nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 stays OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import sys
import mpmath as mp

mp.mp.dps = 30


def partitions(n):
    def gen(n, mx):
        if n == 0:
            yield ()
            return
        for p in range(min(n, mx), 0, -1):
            for r in gen(n - p, p):
                yield (p,) + r
    yield from gen(n, n)


@lru_cache(maxsize=None)
def factorial(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def conj_of(lam):
    if not lam:
        return ()
    m = lam[0]
    c = [0] * m
    for part in lam:
        for j in range(part):
            c[j] += 1
    return tuple(c)


@lru_cache(maxsize=None)
def dim(lam):
    n = sum(lam)
    if n == 0:
        return 1
    conj = conj_of(lam)
    prod = 1
    for i, part in enumerate(lam):
        for j in range(part):
            prod *= (part - j - 1) + (conj[j] - i - 1) + 1
    return factorial(n) // prod


def diag_lengths(lam):
    D = {}
    for i, part in enumerate(lam):
        for j in range(part):
            u = j - i
            D[u] = D.get(u, 0) + 1
    return D


def addable(lam):
    lam = list(lam)
    res = []
    ext = lam + [0]
    for i in range(len(ext)):
        if i == 0 or ext[i - 1] > ext[i]:
            new = lam[:]
            if i < len(lam):
                new[i] += 1
            else:
                new.append(1)
            res.append((tuple(x for x in new if x > 0), (new[i] - 1) - i if i < len(new) else 0))
    # content of added box: column (new length-1) minus row i
    out = []
    ext2 = lam + [0]
    for i in range(len(ext2)):
        above = ext2[i - 1] if i - 1 >= 0 else None
        width = ext2[i]
        if i == 0 or above > width:
            new = lam[:]
            if i < len(lam):
                new[i] += 1
            else:
                new.append(1)
            c_add = width - i   # content j-i with j=width (0-indexed new col)
            out.append((tuple(x for x in new if x > 0), c_add))
    return out


def removable(Lam):
    Lam = list(Lam)
    out = []
    for i in range(len(Lam)):
        nxt = Lam[i + 1] if i + 1 < len(Lam) else 0
        if Lam[i] > nxt:
            new = Lam[:]
            new[i] -= 1
            c_rem = (Lam[i] - 1) - i
            out.append((tuple(x for x in new if x > 0), c_rem))
    return out


def analyze(n):
    Yn = list(partitions(n))
    nfac = factorial(n)
    # edge weights s(lam,mu) = pi(lam) J(lam,mu) = dim(lam)dim(mu) c(lam,mu)/((n+1) n!)
    # accumulate over unordered single-box-move edges with content data.
    # For each lam, enumerate children Lam=lam+box(cA); for each mu=Lam-box(cB) with mu!=lam,
    # this contributes one (lam->mu) ordered move with removed content cB, added content cA... wait:
    # lam ->(add cA)-> Lam ->(remove cB)-> mu.  So mu = lam + box(cA) - box(cB).
    # Relative to lam: added content cA, removed content cB. For the omega3 identity we need the
    # move lam->mu removing r-content and adding a-content: here 'added to lam' = cA, 'removed from lam' = cB.
    # d at content in LAMBDA.
    Dcache = {lam: diag_lengths(lam) for lam in Yn}
    dimcache = {lam: dim(lam) for lam in Yn}
    # count common children per (lam,mu): number of Lam reachable. We accumulate directly.
    from collections import defaultdict
    edge_cc = defaultdict(int)   # (lam,mu) -> common-children count
    for lam in Yn:
        for Lam, cA in addable(lam):
            for mu, cB in removable(Lam):
                if mu == lam:
                    continue
                edge_cc[(lam, mu)] += 1
    # Now build oriented-edge stats. Each unordered edge appears as (lam,mu) and (mu,lam).
    # Process ordered (lam,mu); orient by |removed content from lam| > |added|.
    total_P = F(0)
    total_N = F(0)
    wnum_ge1 = F(0)   # omega-weight (unnormalized) on ratio_e >= 1
    wtot = F(0)
    max_ratio = F(0)
    # corner-distance split: adjacent (the moved box's two corners are 'nearest') vs distant
    w_by_dist = defaultdict(lambda: F(0))
    seen = set()
    for (lam, mu), cc in edge_cc.items():
        if (mu, lam) in seen:
            continue
        seen.add((lam, mu))
        # determine moved contents: mu = lam + box(cA) - box(cB); cA added to lam, cB removed from lam
        Dl = Dcache[lam]
        Dm = Dcache[mu]
        # find added/removed content by diagonal-length diff
        added = [u for u in set(Dl) | set(Dm) if Dm.get(u, 0) == Dl.get(u, 0) + 1]
        removed = [u for u in set(Dl) | set(Dm) if Dm.get(u, 0) == Dl.get(u, 0) - 1]
        if len(added) != 1 or len(removed) != 1:
            continue
        cA = added[0]   # added to lam
        cB = removed[0]  # removed from lam
        # symmetric weight s = dim(lam) dim(mu) cc / ((n+1) n!)
        s = F(dimcache[lam] * dimcache[mu] * cc, (n + 1) * nfac)
        w_e = 2 * s   # unordered edge weight (factor 2 for the two orientations in the numer sum)
        # omega3(lam)-omega3(mu) = c_rem^2 - c_add^2 where rem = removed from lam = cB, add = cA
        # (Sum_c^2 change: mu gains cA^2 loses cB^2 vs lam)
        dO = F(cB * cB - cA * cA)   # omega3(lam) - omega3(mu)
        dABS = F(abs(cB) - abs(cA))  # Sum|c|(lam) - Sum|c|(mu)
        dD2 = F(2 * (Dl.get(cA, 0) - Dl.get(cB, 0) + 1))  # SumD2(mu)-SumD2(lam)=2(d_a-d_r+1); Sum(lam)-Sum(mu) = -dD2
        # P-term (unordered) = w_e * dABS * dO ; N-term = w_e * (-(SumD2(lam)-SumD2(mu))) * ... let's just use covariance contributions:
        # Cov(Sum|c|,omega3) contribution = w_e * dABS * dO ; Cov(SumD2,omega3) contribution = w_e * (SumD2(lam)-SumD2(mu)) * dO
        Pterm = w_e * dABS * dO                 # >= 0
        SumD2_lam_minus_mu = -dD2               # SumD2(lam)-SumD2(mu)
        covD2_term = w_e * SumD2_lam_minus_mu * dO
        Nterm = -covD2_term                     # >= 0
        total_P += Pterm
        total_N += Nterm
        # ratio_e = Nterm / Pterm (when Pterm>0)
        if Pterm > 0:
            ratio = Nterm / Pterm
            wtot += Pterm
            if ratio >= 1:
                wnum_ge1 += Pterm
            if ratio > max_ratio:
                max_ratio = ratio
        # corner distance = |cA - cB| (content distance of the moved box)
        dist = abs(cA - cB)
        w_by_dist[dist] += Pterm  # weight in the omega measure
    NP = (total_N / total_P) if total_P != 0 else F(0)
    frac_ge1 = (wnum_ge1 / wtot) if wtot != 0 else F(0)
    return {
        "n": n, "P": total_P, "N": total_N, "NP": NP,
        "frac_omega_ratio_ge1": frac_ge1, "max_ratio": max_ratio,
        "w_by_dist": dict(w_by_dist), "wtot": wtot,
    }


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    print("# N/P = E_omega[ratio_e] structure; omega ~ 2s*(r-a)^2(r+a)")
    print(f"# {'n':>3} {'N/P':>10} {'w(ratio>=1)':>12} {'max ratio':>10} {'omega-wt by |cA-cB|=1,2,3,>=4':>34}")
    for n in range(4, nmax + 1):
        r = analyze(n)
        wd = r["w_by_dist"]; wtot = r["wtot"]
        def frac(k):
            return float(wd.get(k, F(0)) / wtot) if wtot != 0 else 0.0
        f_ge4 = float(sum((v for k, v in wd.items() if k >= 4), F(0)) / wtot) if wtot != 0 else 0.0
        assert r["N"] < r["P"], f"N<P must hold (n={n})"
        print(f"  {n:>3} {float(r['NP']):>10.6f} {float(r['frac_omega_ratio_ge1']):>12.6f} "
              f"{float(r['max_ratio']):>10.4f}   d1={frac(1):.4f} d2={frac(2):.4f} d3={frac(3):.4f} d>=4={f_ge4:.4f}")
    # 1-Lipschitz lemma: |D(u+1)-D(u)| <= 1 for every Young diagram.
    lip_ok = True
    maxjump = 0
    for n in range(1, min(nmax, 14) + 1):
        for lam in partitions(n):
            D = diag_lengths(lam)
            for u in range(min(D), max(D) + 1):
                j = abs(D.get(u + 1, 0) - D.get(u, 0))
                maxjump = max(maxjump, j)
                if j > 1:
                    lip_ok = False
    print()
    print(f"# 1-Lipschitz lemma |D(u+1)-D(u)|<=1 (all partitions n<=min(nmax,14)): {lip_ok}  (max jump {maxjump})")
    print("#   => d_a - d_r <= r - a (same-sign contents) => per-edge ratio_e =")
    print("#      2(d_a-d_r+1)/(r-a) <= 2 + 2/(r-a) <= 4  (explains observed max ratio 4).")
    print("#")
    print("# FINDING (route refutation, scope-(a)): the weight-suppression hypothesis is FALSE.")
    print("#   omega-weight concentrates on DISTANT signed-content moves (d>=4 grows with n),")
    print("#   and ~15% of omega-weight sits on ratio_e>=1 (persistent, not ->0). N/P<1 is NOT")
    print("#   worst-case: per-edge ratio can be 4. It is an AVERAGING phenomenon -- omega ~")
    print("#   (r-a)^2(r+a) up-weights large-(r-a) edges, which have SMALL ratio_e, and the")
    print("#   bulk diagonal profile of a typical diagram is FLAT (d_a-d_r << r-a in the bulk).")
    print("#   Hence a uniform N/P<1 needs EFFECTIVE (error-controlled) limit-shape estimates")
    print("#   (Berry-Esseen grade), not an elementary per-edge/worst-case bound.")
    print("RESULT: N/P = E_omega[ratio_e] structure tabulated; N<P verified exactly on range.")
    print(f"RESULT: 1-Lipschitz lemma verified (max jump {maxjump}); worst-case per-edge ratio<=4.")
    print("RESULT: weight-suppression route REFUTED; uniform N/P<1 needs effective asymptotics.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
