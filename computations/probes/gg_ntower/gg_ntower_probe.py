#!/usr/bin/env python3
"""gamma-gamma production climbing the strand-count tower (issue #7727).

Recipe: preregistration.md in this directory, committed (4544d19380) before
this script was written or run. Nothing here is ranked, selected, or compared
with Q_beta, CODATA, AME or any mass.

Element: W_k^(s) = V_{p_0} ... V_{p_{k-1}}, p_j = s*j (offset to start at 0),
vertex V_i = s_i s_{i+1}^-1 (primary) or U_i = s_i s_{i+1} (secondary), in
H_n(q), n = |s|(k-1)+3. Strands are closed from the top by the convention-D
Markov conditional expectation; reading 3 is tested at every level 3..n on the
blocks with y_lambda > 0 (at most two rows).

Arithmetic: exact over QQ(q) (sympy DomainMatrix); q0 values with mpmath at
60 dps. No float64.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for p in (ROOT / "computations", ROOT / "computations" / "markov",
          ROOT / "tools" / "qou-substrate" / "python"):
    sys.path.insert(0, str(p))

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 60
q, t = sp.symbols("q t", positive=True)
K = sp.QQ.frac_field(q)
Q0 = mp.mpf(Q_50_DIGIT_STR)
Q0_RAT = sp.Rational(Q_50_DIGIT_STR)
H = q - 1 / q
ZD = q**3 / (q**2 + 1)
NMAX = 9
T0 = time.time()


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# ---------------------------------------------------------------- tableaux
def two_row_shapes(n):
    return [(n - j, j) for j in range(n // 2 + 1)]


def syt(lam):
    """Standard tableaux of a two-row shape as tuples rows[i] (entry i+1)."""
    n = sum(lam)
    out = []

    def rec(rows, c0, c1):
        if len(rows) == n:
            out.append(tuple(rows))
            return
        if c0 < lam[0]:
            rec(rows + [0], c0 + 1, c1)
        if c1 < lam[1] and c1 < c0:
            rec(rows + [1], c0, c1 + 1)

    rec([], 0, 0)
    return out


def contents(T):
    c, cols = [], [0, 0]
    for r in T:
        c.append(cols[r] - r)
        cols[r] += 1
    return c


def a_r(r):
    return (q - 1 / q) / (1 - q ** (-2 * r))


class Rep:
    """Young seminormal representation of H_n(q) on a two-row shape."""

    def __init__(self, lam, flip=False):
        self.lam = lam
        self.n = sum(lam)
        self.basis = syt(lam)
        self.idx = {T: i for i, T in enumerate(self.basis)}
        d = len(self.basis)
        self.dim = d
        self.gen = []
        for i in range(self.n - 1):
            M = [[K.zero] * d for _ in range(d)]
            for T, a in self.idx.items():
                c = contents(T)
                r = c[i + 1] - c[i]
                M[a][a] = K.from_sympy(sp.cancel(a_r(r)))
                if abs(r) >= 2:
                    T2 = list(T)
                    T2[i], T2[i + 1] = T2[i + 1], T2[i]
                    b = self.idx[tuple(T2)]
                    # off-diagonal: coefficient 1 on the image of the tableau
                    # whose (i+1) sits in the lower row; product = a_r a_-r + 1
                    low = (T[i + 1] > T[i]) != flip
                    off = 1 if low else sp.cancel(a_r(r) * a_r(-r) + 1)
                    M[b][a] = K.from_sympy(sp.sympify(off))
            self.gen.append(DomainMatrix(M, (d, d), K))
        self.eye = DomainMatrix.eye(d, K)
        self.hm = DomainMatrix([[K.from_sympy(H)]], (1, 1), K)

    def letter(self, g, e):
        G = self.gen[g]
        if e == 1:
            return G
        return G - self.eye * K.from_sympy(H)  # s^-1 = s - h

    def word(self, letters):
        M = self.eye
        for g, e in letters:
            M = M * self.letter(g, e)
        return M


REPS = {}


def rep(lam, flip=False):
    key = (lam, flip)
    if key not in REPS:
        REPS[key] = Rep(lam, flip)
    return REPS[key]


def qint(m):
    return sum(q ** (m - 1 - 2 * i) for i in range(m))


def y_lambda(lam):
    n = sum(lam)
    return qint(lam[0] - lam[1] + 1) / qint(2) ** n


def tr(M):
    return sp.cancel(sum(K.to_sympy(M[i, i].element) for i in range(M.shape[0])))


# ------------------------------------------------- characters and closing
def level_chars(letters, n):
    """chi_mu(E_{n->m}(W)) for every level m=3..n and two-row mu |- m."""
    diag = {}
    for lam in two_row_shapes(n):
        R = rep(lam)
        M = R.word(letters)
        diag[lam] = [(T, K.to_sympy(M[i, i].element)) for i, T in enumerate(R.basis)]
    out = {}
    for m in range(3, n + 1):
        for mu in two_row_shapes(m):
            acc = sp.Integer(0)
            for lam, entries in diag.items():
                ratio = y_lambda(lam) / y_lambda(mu)
                s = sp.Integer(0)
                for T, v in entries:
                    if (m - sum(T[:m]), sum(T[:m])) == mu:
                        s += v
                acc += ratio * s
            out[(m, mu)] = sp.factor(sp.cancel(acc))
    return out


def sign_info(f):
    f = sp.cancel(f)
    if f == 0:
        return {"identically_zero": True, "at_q0": "0", "nonneg_on_(1,inf)": True,
                "roots_in_(1,2)": []}
    num, den = sp.fraction(sp.together(f))
    num, den = sp.Poly(sp.expand(num), q), sp.Poly(sp.expand(den), q)
    roots = []
    for P in (num, den):
        for r in sp.real_roots(P):
            if r > 1:
                roots.append(r)
    roots = sorted(set(roots), key=lambda r: sp.N(r, 30))
    pts = [sp.Integer(1)] + roots
    samples = [(pts[i] + pts[i + 1]) / 2 for i in range(len(pts) - 1)]
    samples.append(pts[-1] + 1)
    nonneg = all(sp.sign(sp.N(f.subs(q, x), 50)) >= 0 for x in samples)
    v = mp.mpf(sp.N(f.subs(q, Q0_RAT), 80).__str__())
    return {
        "identically_zero": False,
        "at_q0": mp.nstr(v, 25),
        "nonneg_at_q0": bool(v >= 0),
        "nonneg_on_(1,inf)": bool(nonneg),
        "roots_in_(1,2)": [mp.nstr(mp.mpf(str(sp.N(r, 40))), 20) for r in roots if r < 2],
    }


def h_order(f):
    """value at q=1 and leading order in t of f(1+t) - f(1)."""
    g = sp.cancel(f.subs(q, 1 + t))
    f1 = sp.cancel(g.subs(t, 0))
    d = sp.cancel(g - f1)
    if d == 0:
        return str(f1), None
    num, _ = sp.fraction(sp.together(d))
    P = sp.Poly(sp.expand(num), t)
    order = min(m[0] for m in P.monoms())
    return str(f1), int(order)


def element(s, k, vertex):
    pos = [s * j for j in range(k)]
    lo = min(pos)
    pos = [p - lo for p in pos]
    n = max(pos) + 3
    e2 = -1 if vertex == "V" else 1
    letters = []
    for p in pos:
        letters += [(p, 1), (p + 1, e2)]
    return n, letters


# ------------------------------------------------------------------ checks
def run_checks():
    checks = {}
    # C1 Hecke + braid relations, every two-row shape n<=9
    ok = True
    for n in range(3, NMAX + 1):
        for lam in two_row_shapes(n):
            R = rep(lam)
            for i in range(n - 1):
                G = R.gen[i]
                ok &= (G * G - G * K.from_sympy(H) - R.eye).is_zero_matrix
                if i + 1 < n - 1:
                    G2 = R.gen[i + 1]
                    ok &= (G * G2 * G - G2 * G * G2).is_zero_matrix
                for j in range(i + 2, n - 1):
                    G2 = R.gen[j]
                    ok &= (G * G2 - G2 * G).is_zero_matrix
    checks["C1_hecke_braid_relations"] = bool(ok)
    log(f"C1 {ok}")

    # C2 y_lambda against corpus; normalisation; tr(sigma) = z_D at n=2
    from markov_weights_symbolic import y_lambda_symbolic
    from hoefsmit_symbolic import Q as QC
    ok = True
    for n in range(3, 7):
        ys = y_lambda_symbolic(n)
        for lam, ex in ys.items():
            if len([x for x in lam if x > 0]) > 2:
                mine = 0
            else:
                lam2 = tuple(list(lam) + [0])[:2]
                mine = y_lambda(lam2)
            ok &= sp.simplify(sp.sympify(ex).subs(QC, q) - mine) == 0
        norm = sum(y_lambda(l) * len(syt(l)) for l in two_row_shapes(n))
        ok &= sp.simplify(norm - 1) == 0
    trs = sp.cancel(y_lambda((2, 0)) * q + y_lambda((1, 1)) * (-1 / q))
    ok &= sp.simplify(trs - ZD) == 0
    checks["C2_markov_weights"] = bool(ok)
    log(f"C2 {ok}")

    # C3 E(a)=a and E(a s_m b) = z ab on characters, m=3..5
    ok = True
    samples = [[(0, 1)], [(0, 1), (1, -1)], [(1, 1), (0, 1), (1, 1)], [(0, -1), (1, 1)]]
    for m in range(3, 6):
        for a in samples:
            for b in samples:
                ab = a + b
                x = a + [(m - 1, 1)] + b
                top = level_chars(x, m + 1)
                base = level_chars(ab, m)
                same = level_chars(ab, m + 1)
                for mu in two_row_shapes(m):
                    ok &= sp.simplify(top[(m, mu)] - ZD * base[(m, mu)]) == 0
                    ok &= sp.simplify(same[(m, mu)] - base[(m, mu)]) == 0
    checks["C3_conditional_expectation"] = bool(ok)
    log(f"C3 {ok}")

    # C4 s=0 reproduces the h-tower
    _, l3 = element(0, 3, "V")
    c = level_chars(l3, 3)
    ok = sp.simplify(c[(3, (2, 1))] - 2 + H**4 * (3 + H**2)) == 0
    surv = []
    for k in range(1, 7):
        _, lk = element(0, k, "V")
        ck = level_chars(lk, 3)
        if all(sign_info(ck[(3, mu)])["nonneg_at_q0"] if ck[(3, mu)] != 0 else True
               for mu in two_row_shapes(3)):
            surv.append(k)
    ok &= surv == [3, 6]
    checks["C4_h_tower_baseline"] = bool(ok)
    checks["C4_survivors_k_le_6"] = surv
    log(f"C4 {ok} survivors {surv}")

    # C5 s=+1 telescoping: W_k = s_0 s_k^-1
    ok = True
    for k in range(2, 6):
        n, lk = element(1, k, "V")
        a = level_chars(lk, n)
        b = level_chars([(0, 1), (k, -1)], n)
        ok &= all(sp.simplify(a[key] - b[key]) == 0 for key in a)
    checks["C5_staircase_telescopes"] = bool(ok)
    log(f"C5 {ok}")
    return checks


def main():
    checks = run_checks()
    SHIFTS = [0, 1, -1, 2, -2, 3]
    results = {}
    for vertex in ("V", "U"):
        for s in SHIFTS:
            k = 1
            while True:
                n, letters = element(s, k, vertex)
                if n > NMAX or (s == 0 and k > 6):
                    break
                if s == 0 and n == 3 and k > 6:
                    break
                log(f"{vertex} s={s:+d} k={k} n={n}")
                chars = level_chars(letters, n)
                rows = {}
                adm_levels = {}
                for (m, mu), f in chars.items():
                    si = sign_info(f)
                    v1, o = h_order(f)
                    rows[f"m={m} mu={mu}"] = {"chi": str(f), **si, "q1": v1, "t_order": o}
                    good = si["identically_zero"] or si["nonneg_at_q0"]
                    adm_levels[m] = adm_levels.get(m, True) and good
                results[f"{vertex} s={s:+d} k={k}"] = {
                    "vertex": vertex, "shift": s, "k": k, "n": n, "letters": letters,
                    "reading3_at_q0_by_level": adm_levels,
                    "admissible_every_level_at_q0": all(adm_levels.values()),
                    "admissible_top_level_at_q0": adm_levels[n],
                    "rows": rows,
                }
                if s == 0:
                    k += 1
                    continue
                k += 1
    out = {
        "recipe": "computations/probes/gg_ntower/preregistration.md (4544d19380)",
        "issue": 7727,
        "q0": Q_50_DIGIT_STR,
        "q0Anchor": "proton",
        "q0Value": Q_50_DIGIT_STR,
        "checks": checks,
        "results": results,
        "wall_seconds": int(time.time() - T0),
    }
    (HERE / "gg-ntower.witness.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    ok = all(v for k, v in checks.items() if isinstance(v, bool))
    log(f"checks {checks}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
