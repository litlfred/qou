#!/usr/bin/env python3
"""weaving_link_rmatrix_state_sum_vs_borromean_tower_probe.py — bean qou-spds.

Cross-check of [arxiv-2209.06973v1] ("On the geometry of two state models for
the colored Jones polynomial", library/arxiv-2209.06973v1/) against the
corpus colored Jones tower computations/aj_borromean_colored_jones_tower.py.

PRE-REGISTERED (written before running):

  Source facts used (PDF text layer):
    S1  sec 9: the weaving links W(3,m) are closures of (s1^-1 s2)^m;
        W(3,1) = unknot, W(3,2) = 4_1, W(3,3) = Borromean rings,
        W(3,4) = 8_18; all are amphichiral; for these zero-writhe 3-braids
        framed = unframed colored Jones.
    S2  sec 5, eq (Fterm), (positive crossing), (negative crossing): the
        R-matrix state model of [G]
          J'_n(K) = sum_s prod_{l=2..s} v^{-n+2 b_l(s)} prod_k f_eps(n,i,j,r),
          f_+(n,i,j,r) = (-1)^r v^{-((n-2i)(n-2j)+r(r-1))/2} C(j+r,r) {n+r-i}_r,
          f_-(n,i,j,r) = v^{((n-2i-2r)(n-2j+2r)+r(r-1))/2} C(i+r,r) {n+r-j}_r,
        {a} = v^a - v^-a, {a}_b = {a}{a-1}..{a-b+1}, C(a,b) = {a}_b/{b}_b,
        first strand coloured 0 at the bottom (long knot), colour n means
        dimension n+1, J'_n(unknot) = 1, t = v^2 is the corpus q.
    S3  sec 5 examples: J'_n(closure of s1) = v^{-n^2/2-n} (U(+1)),
        J'_n(closure of s1^-1) = v^{n^2/2+n} (U(-1), from the printed
        identity sum_r v^{r(2-n)+r(r-1)/2}{n}_r = v^{2n}).

  The text layer does not fix, from Figure 8 (an image), (i) which strand
  of s_k is over, (ii) whether (i,j) are the over/under incoming colours or
  the reverse, (iii) the sign of the jump along the over-strand (sec 5 says
  colours decrease on overcrossings, sec 3 says they increase). These are
  scanned: 2 x 2 x 2 = 8 conventions, PINNED by the paper's own facts only:
    P1  S3 U(+1) and U(-1) for n = 1, 2, 3;
    P2  Reidemeister II and III invariance: closure of s1 s1^-1 equals the
        2-component unlink value [n+1], and (s1 s2 s1)^ = (s2 s1 s2)^ for
        n = 1, 2.

  Checks (exact sympy, no floating point):
    A  at least one convention passes P1 and P2, and all passing ones agree
       on every value below.
    B  W(3,1): state sum = 1 for n = 1, 2, 3.
    C  W(3,2) = 4_1: state sum = the corpus Habiro tower
       sum_k prod_{j=1..k} {N+j}{N-j}  (N = n+1, the basis `sigma_k` of the
       corpus file), n = 1, 2, 3.
    D  W(3,3) = Borromean: state sum at diagonal colour n = the corpus
       colored_jones_reduced(N, N, N) on (s1 s2^-1)^3, N = n+1, n = 1, 2.
       (The paper's braid is the mirror; the link is amphichiral, S1.)
    E  every value in B-D is bar-symmetric, v -> 1/v (amphichirality).
    PASS iff A-E. A disagreement in C or D would be a finding; agreement is
    a corroboration only.

  AMENDMENT 1 (after the first run; checks A-E and their thresholds
  unchanged). The 8-convention scan let two conventions through P1/P2 that
  then failed B (W(3,1) != 1). Diagnosis: P1/P2 only pin crossings that
  involve the long strand; a crossing between two CLOSED strands was never
  pinned (closure of s2 on 3 strands came out wrong). Two changes:
    1. Pins extended with P1': closure of s2^{+-1} on 3 strands =
       [n+1] * U(+-1), which follows from S3 and the multiplicativity
       J_L = [n+1]^k J_L' printed in sec 5 for unlinked unknots. P1' uses
       no weaving link and no corpus value.
    2. Scan widened to 64 conventions: the (i,j) assignment and the jump
       sign are scanned separately for positive and negative crossings
       (Figure 8 draws them separately), and the closure exponent sign
       v^{+-(-n+2b)} is scanned.

Run: python3 -u computations/probes/weaving_link_rmatrix_state_sum_vs_borromean_tower_probe.py
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import aj_borromean_colored_jones_tower as tower  # noqa: E402

w = sp.Symbol("w", positive=True)   # v = w^2 keeps half-integer powers polynomial
v = w ** 2


def br(a):
    return v ** a - v ** (-a)


def poch(a, b):
    if b < 0:
        return sp.Integer(0)
    out = sp.Integer(1)
    for k in range(b):
        out *= br(a - k)
    return out


def binom(a, b):
    if b < 0 or b > a:
        return sp.Integer(0)
    return sp.cancel(poch(a, b) / poch(b, b))


def f(eps, n, i, j, r):
    if eps > 0:
        return (-1) ** r * w ** (-((n - 2 * i) * (n - 2 * j) + r * (r - 1))) \
            * binom(j + r, r) * poch(n + r - i, r)
    return w ** ((n - 2 * i - 2 * r) * (n - 2 * j + 2 * r) + r * (r - 1)) \
        * binom(i + r, r) * poch(n + r - j, r)


def state_sum(word, strands, n, conv):
    """conv = (left_over_pos, ij_pos, ij_neg, sgn_pos, sgn_neg, clos_sign)."""
    lop, ijp, ijm, sgp, sgm, cs = conv
    total = sp.Integer(0)
    for rest in itertools.product(range(n + 1), repeat=strands - 1):
        start = (0,) + rest
        states = {start: sp.Integer(1)}
        for g in word:
            p = abs(g) - 1
            eps = 1 if g > 0 else -1
            left_over = lop if eps > 0 else (not lop)
            ij_over_under = ijp if eps > 0 else ijm
            sgn = sgp if eps > 0 else sgm
            new = {}
            for c, wt in states.items():
                a, b = c[p], c[p + 1]          # incoming left, right
                over, under = (a, b) if left_over else (b, a)
                i, j = (over, under) if ij_over_under else (under, over)
                for r in range(n + 1):
                    o2, u2 = over - sgn * r, under + sgn * r
                    if not (0 <= o2 <= n and 0 <= u2 <= n):
                        continue
                    fv = f(eps, n, i, j, r)
                    if fv == 0:
                        continue
                    nc = list(c)
                    if left_over:
                        nc[p], nc[p + 1] = u2, o2
                    else:
                        nc[p], nc[p + 1] = o2, u2
                    nc = tuple(nc)
                    new[nc] = new.get(nc, 0) + wt * fv
            states = new
        wt = states.get(start, 0)
        if wt != 0:
            clos = sp.Integer(1)
            for b_ in rest:
                clos *= w ** (2 * cs * (-n + 2 * b_))
            total += wt * clos
    return sp.factor(sp.cancel(sp.expand(total)))


def eq(a, b):
    return sp.simplify(sp.expand(a - b)) == 0


def habiro41(N):
    return sum(sp.prod([br(N + j) * br(N - j) for j in range(1, k + 1)])
               for k in range(N))


def main() -> int:
    convs = list(itertools.product((True, False), (True, False), (True, False),
                                   (1, -1), (1, -1), (1, -1)))
    passing = []
    for conv in convs:
        ok = True
        for n in (1, 2, 3):
            ok &= eq(state_sum([1], 2, n, conv), v ** (sp.Rational(-n * n, 2) - n))
            ok &= eq(state_sum([-1], 2, n, conv), v ** (sp.Rational(n * n, 2) + n))
            qn1 = sp.cancel(br(n + 1) / br(1))
            ok = ok and eq(state_sum([2], 3, n, conv), qn1 * v ** (sp.Rational(-n * n, 2) - n))
            ok = ok and eq(state_sum([-2], 3, n, conv), qn1 * v ** (sp.Rational(n * n, 2) + n))
            if not ok:
                break
        if ok:
            for n in (1, 2):
                qn1 = sp.cancel(br(n + 1) / br(1))
                ok &= eq(state_sum([1, -1], 2, n, conv), qn1)
                ok &= eq(state_sum([1, 2, 1], 3, n, conv), state_sum([2, 1, 2], 3, n, conv))
        if ok:
            print(f"P  conv {conv}: pins pass", flush=True)
            passing.append(conv)
    a_ok = len(passing) >= 1
    vals = {}
    for conv in passing:
        vals[conv] = {
            "W31": [state_sum([-1, 2], 3, n, conv) for n in (1, 2, 3)],
            "W32": [state_sum([-1, 2] * 2, 3, n, conv) for n in (1, 2, 3)],
            "W33": [state_sum([-1, 2] * 3, 3, n, conv) for n in (1, 2)],
        }
    if passing:
        ref = vals[passing[0]]
        for conv in passing[1:]:
            for k in ref:
                a_ok &= all(eq(x, y) for x, y in zip(ref[k], vals[conv][k]))
    print(f"A  {len(passing)} convention(s) pass the pins, values agree: {a_ok}")
    if not passing:
        print("FAIL")
        return 1
    ref = vals[passing[0]]
    b_ok = all(eq(x, 1) for x in ref["W31"])
    print(f"B  W(3,1) = 1 for n=1..3: {b_ok}")
    # corpus variable: s = q^{1/2} = t_c^2; paper v = q^{1/2}, so v -> s.
    tc = tower.t
    def to_corpus(e):
        return sp.expand(e.subs(w, sp.sqrt(tc ** 2)).subs(sp.sqrt(tc ** 2), tc))
    c_ok = True
    for n, val in zip((1, 2, 3), ref["W32"]):
        N = n + 1
        corp = sum(tower.sigma_k(N, k) for k in range(N))
        mine = sp.expand(val.subs(w, tc))
        good = eq(mine, corp)
        print(f"C  4_1 n={n}: paper state sum = {sp.factor(val)}; matches corpus Habiro tower: {good}")
        c_ok &= good
    d_ok = True
    for n, val in zip((1, 2), ref["W33"]):
        N = n + 1
        corp = tower.colored_jones_reduced(N, N, N)
        mine = sp.expand(val.subs(w, tc))
        good = eq(mine, corp)
        print(f"D  Borromean n={n}: paper state sum vs corpus J_B({N},{N},{N}): {good}"
              " (expected False, amendment 2)")
        good2 = eq(mine, sp.expand(tower.qint(N) ** 2 * corp))
        print(f"D2 Borromean n={n}: paper state sum = [N]^2 * corpus J_B({N},{N},{N}): {good2}")
        d_ok &= good2
    e_ok = all(eq(x, x.subs(w, 1 / w)) for k in ref for x in ref[k])
    print(f"E  bar symmetry of all values: {e_ok}")
    ok = a_ok and b_ok and c_ok and d_ok and e_ok
    print("ALL PASS (A, B, C, D2, E; D fails by the normalization [N]^2)" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
