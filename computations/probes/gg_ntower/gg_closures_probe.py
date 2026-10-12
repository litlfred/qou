#!/usr/bin/env python3
"""gamma-gamma climbing placements under three closures (follow-up to #7733).

Recipe: closures_preregistration.md in this directory, committed before this
script was run. Nothing here is ranked, selected, or compared with Q_beta,
CODATA, AME or any mass.

Reuses the exact QQ(q) Young seminormal machinery of gg_ntower_probe.py
(two-row shapes, convention-D Markov weights, top-strand conditional
expectation). Adds:

  * BOTTOM closure: close the lowest strand, E_bot(a s_0 b) = z ab for
    a, b in <s_1..s_{m-1}>. Computed as top closure of the flipped word
    s_i -> s_{n-2-i}; the flip is conjugation by T_{w0}, so characters of the
    closed element are unchanged by the final identification (check K2).
  * PLAT / pair closure: see closures_preregistration.md section 3.

Arithmetic: exact over QQ(q) (sympy); q0 values with mpmath at 60 dps.
No float64.
"""
from __future__ import annotations

import itertools
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gg_ntower_probe as g  # noqa: E402

q, t = g.q, g.t
ZD = g.ZD
NMAX = 9
T0 = time.time()
mp.mp.dps = 60


def log(msg):
    print(f"[{time.time() - T0:7.1f}s] {msg}", flush=True)


# ---------------------------------------------------------------- closures
def flip(letters, n):
    return [(n - 2 - i, e) for i, e in letters]


_CACHE = {}


def chars_top(letters, n):
    key = (tuple(map(tuple, letters)), n)
    if key not in _CACHE:
        _CACHE[key] = g.level_chars([tuple(x) for x in letters], n)
    return _CACHE[key]


def chars_bottom(letters, n):
    return chars_top(flip(letters, n), n)


# ------------------------------------------------- q = 1 permutation model
def perm_of(letters, n):
    """Permutation (as tuple image) of the word at q = 1, left-to-right product
    acting on strand positions; sigma_i^{+-1} -> transposition (i, i+1)."""
    p = list(range(n))
    for i, _ in letters:
        p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def close_points(p, closed):
    """Contract the points in `closed` out of permutation p (q=1, z=1/2).
    Returns (weight, permutation on the remaining points, relabelled)."""
    p = dict(enumerate(p))
    w = Fraction(1)
    for c in closed:
        if p[c] == c:
            del p[c]
            continue
        w /= 2
        pre = next(a for a, b in p.items() if b == c)
        p[pre] = p[c]
        del p[c]
    keep = sorted(p)
    rel = {a: i for i, a in enumerate(keep)}
    return w, tuple(rel[p[a]] for a in keep)


S3_CHI21 = {"id": 2, "trans": 0, "cyc": -1}


def chi21_s3(perm):
    fixed = sum(1 for i, a in enumerate(perm) if i == a)
    return {3: 2, 1: 0, 0: -1}[fixed]


def q1_level3(letters, n, mode):
    p = perm_of(letters, n)
    closed = list(range(n - 1, 2, -1)) if mode == "top" else list(range(0, n - 3))
    w, pr = close_points(p, closed)
    return w, pr, w * chi21_s3(pr)


# ------------------------------------------------------------- sign helper
def sign_info(f):
    """Exact sign of a rational function on (1, inf) via Sturm counts;
    roots isolated only if a count is nonzero."""
    f = sp.cancel(f)
    if f == 0:
        return {"identically_zero": True, "at_q0": "0", "nonneg_at_q0": True,
                "nonneg_on_(1,inf)": True, "roots_gt_1": []}
    num, den = sp.fraction(sp.together(f))
    num, den = sp.Poly(sp.expand(num), q), sp.Poly(sp.expand(den), q)
    roots = []
    for P in (num, den):
        if P.degree() > 0 and P.count_roots(1, None) - (1 if P.eval(1) == 0 else 0) > 0:
            roots += [r for r in sp.real_roots(P) if r > 1]
    roots = sorted(set(roots), key=lambda r: sp.N(r, 30))
    pts = [sp.Integer(1)] + roots
    samples = [(pts[i] + pts[i + 1]) / 2 for i in range(len(pts) - 1)] + [pts[-1] + 1]
    nonneg = all(sp.sign(sp.N(f.subs(q, x), 50)) >= 0 for x in samples)
    v = mp.mpf(str(sp.N(f.subs(q, g.Q0_RAT), 80)))
    return {"identically_zero": False, "at_q0": mp.nstr(v, 25),
            "nonneg_at_q0": bool(v >= 0), "nonneg_on_(1,inf)": bool(nonneg),
            "roots_gt_1": [mp.nstr(mp.mpf(str(sp.N(r, 40))), 20) for r in roots]}


def jones(R, i):
    K = g.K
    return (R.eye * K.from_sympy(q) - R.gen[i]) * K.from_sympy(1 / (q + 1 / q))


def chars_pair(letters, n):
    """chi_mu(Phi^j(W)) = chi_{mu+(j,j)}(W e_{n-1} e_{n-3} ... e_{n-2j+1}),
    levels m = n - 2j >= 2."""
    out = {}
    mats = {}
    for lam in g.two_row_shapes(n):
        R = g.rep(lam)
        mats[lam] = (R, R.word(letters))
    j = 0
    while n - 2 * j >= 2:
        m = n - 2 * j
        for mu in g.two_row_shapes(m):
            lam = (mu[0] + j, mu[1] + j)
            R, M = mats[lam]
            P = M
            for r in range(j):
                P = P * jones(R, n - 2 - 2 * r)
            out[(m, mu)] = sp.factor(g.tr(P))
        j += 1
    return out


def chars_pair_bottom(letters, n):
    return chars_pair(flip(letters, n), n)


CLOSURES = {"top": chars_top, "bottom": chars_bottom,
            "pair": chars_pair, "pair_bottom": chars_pair_bottom}


def h_order(f):
    return g.h_order(f)


# ------------------------------------------------------------------ checks
def run_checks():
    checks = {}
    wit = json.loads((HERE / "gg-ntower.witness.json").read_text())["results"]

    # K1 top reproduces #7733 witness exactly
    ok, cnt = True, 0
    for key, e in wit.items():
        n, letters = e["n"], [tuple(x) for x in e["letters"]]
        c = chars_top(letters, n)
        log(f"K1 {key}")
        for (m, mu), f in c.items():
            ref = sp.sympify(e["rows"][f"m={m} mu={mu}"]["chi"], locals={"q": q})
            ok &= sp.cancel(f - ref) == 0
            cnt += 1
    checks["K1_top_reproduces_7733"] = bool(ok)
    checks["K1_count"] = cnt
    log(f"K1 {ok} ({cnt} characters)")

    # K2 top level equal for W and flip(W)
    ok = True
    for key, e in wit.items():
        n, letters = e["n"], [tuple(x) for x in e["letters"]]
        a, b = chars_top(letters, n), chars_bottom(letters, n)
        for mu in g.two_row_shapes(n):
            ok &= sp.cancel(a[(n, mu)] - b[(n, mu)]) == 0
    checks["K2_flip_inner_top_level"] = bool(ok)
    log(f"K2 {ok}")

    # K3 q=1 permutation model, level 3, top and bottom
    ok = True
    for key, e in wit.items():
        n, letters = e["n"], [tuple(x) for x in e["letters"]]
        for mode, fn in (("top", chars_top), ("bottom", chars_bottom)):
            c = fn(letters, n)[(3, (2, 1))]
            w, pr, val = q1_level3(letters, n, mode)
            ok &= sp.cancel(c.subs(q, 1) - sp.Rational(val.numerator, val.denominator)) == 0
    checks["K3_q1_permutation_model"] = bool(ok)
    log(f"K3 {ok}")

    # K4 chi_{mu+(1,1)}(y e_m) = chi_mu(E(y)), y in H_m placed in H_{m+1}
    ok = True
    samples = [[(0, 1)], [(0, 1), (1, -1)], [(1, 1), (0, 1), (1, 1)],
               [(0, -1), (1, 1), (0, 1)], [(1, -1), (0, -1)]]
    for m in range(3, 6):
        ext = samples + [[(m - 2, 1), (0, -1)], [(m - 2, -1), (m - 3, 1), (m - 2, 1)]]
        for y in ext:
            Ey = chars_top(y, m)
            for mu in g.two_row_shapes(m - 1):
                lam = (mu[0] + 1, mu[1] + 1)
                R = g.rep(lam)
                lhs = g.tr(R.word(y) * jones(R, m - 1))
                ok &= sp.cancel(lhs - Ey[(m - 1, mu)]) == 0
    checks["K4_jones_absorption_on_characters"] = bool(ok)
    log(f"K4 {ok}")
    return checks


V_RATIO = sp.cancel(-(q**4 - q**2 + 1) / q**2)   # chi_(2,1)/chi_(3) of one V
U_RATIO = None


def single_vertex_ratio(vertex):
    letters = [(0, 1), (1, -1 if vertex == "V" else 1)]
    c = chars_top(letters, 3)
    return sp.cancel(c[(3, (2, 1))] / c[(3, (3, 0))])


def main():
    checks = run_checks()
    ratio = {v: single_vertex_ratio(v) for v in ("V", "U")}
    SHIFTS = [0, 1, -1, 2, -2, 3]
    results = {}
    for vertex in ("V", "U"):
        for s in SHIFTS:
            k = 1
            while True:
                n, letters = g.element(s, k, vertex)
                if n > NMAX or (s == 0 and k > 6):
                    break
                row = {"vertex": vertex, "shift": s, "k": k, "n": n,
                       "letters": letters, "closures": {}}
                for name, fn in CLOSURES.items():
                    chars = fn(letters, n)
                    levels, rows = {}, {}
                    for (m, mu), f in chars.items():
                        si = sign_info(f)
                        v1, o = h_order(f)
                        rows[f"m={m} mu={mu}"] = {"chi": str(f), **si, "q1": v1, "t_order": o}
                        good = si["identically_zero"] or si["nonneg_at_q0"]
                        levels[m] = levels.get(m, True) and good
                    verdict_levels = {m: v for m, v in levels.items() if m >= 3}
                    low = min(verdict_levels)
                    c3 = chars.get((low, (low, 0)))
                    c21 = chars.get((low, (low - 1, 1)))
                    prop = None
                    if low == 3 and c3 is not None and c3 != 0:
                        prop = bool(sp.cancel(c21 / c3 - ratio[vertex]) == 0
                                    and sign_info(c3)["nonneg_on_(1,inf)"])
                    row["closures"][name] = {
                        "reading3_by_level_at_q0": levels,
                        "admissible": all(verdict_levels.values()),
                        "failing_levels": sorted(m for m, v in verdict_levels.items() if not v),
                        "lowest_level": low,
                        "level3_proportional_to_single_vertex": prop,
                        "rows": rows,
                    }
                verdicts = {nm: c["admissible"] for nm, c in row["closures"].items()}
                row["verdicts_agree"] = len(set(verdicts.values())) == 1
                results[f"{vertex} s={s:+d} k={k}"] = row
                log(f"{vertex} s={s:+d} k={k} n={n} {verdicts}")
                k += 1
    out = {
        "recipe": "computations/probes/gg_ntower/closures_preregistration.md (152a15575e)",
        "follows": "PR #7733, issue #7727",
        "q0": g.Q_50_DIGIT_STR,
        "checks": checks,
        "single_vertex_ratio_chi21_over_chi3": {v: str(r) for v, r in ratio.items()},
        "results": results,
        "wall_seconds": int(time.time() - T0),
    }
    (HERE / "gg-closures.witness.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    ok = all(v for v in checks.values() if isinstance(v, bool))
    log(f"checks {checks}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
