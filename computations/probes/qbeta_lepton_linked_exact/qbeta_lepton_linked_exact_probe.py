#!/usr/bin/env python3
"""Exact linked-word lepton traces against the window (ε_n, ε_p); see PREREGISTRATION.md.

Crossing action copied from computations/probes/qbeta_gg_lepton_pair (PR #8836): Jimbo R with
eigenvalues q, −1/q, K = diag(q, 1/q). Arithmetic is exact Laurent polynomials in q.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
mp.mp.dps = 50
Q0 = mp.mpf("1.1099785827513808")  # proton pin (qou_substrate.constants.Q), display only


class LP:
    """Laurent polynomial in q with integer coefficients."""
    __slots__ = ("d",)

    def __init__(self, d=None):
        self.d = {k: v for k, v in (d or {}).items() if v}

    @staticmethod
    def c(x):
        return x if isinstance(x, LP) else LP({0: x})

    def __add__(self, o):
        o = LP.c(o); d = dict(self.d)
        for k, v in o.d.items():
            d[k] = d.get(k, 0) + v
        return LP(d)
    __radd__ = __add__

    def __neg__(self):
        return LP({k: -v for k, v in self.d.items()})

    def __sub__(self, o):
        return self + (-LP.c(o))

    def __mul__(self, o):
        o = LP.c(o); d = defaultdict(int)
        for a, x in self.d.items():
            for b, y in o.d.items():
                d[a + b] += x * y
        return LP(d)
    __rmul__ = __mul__

    def __bool__(self):
        return bool(self.d)


Q = LP({1: 1}); QI = LP({-1: 1}); H = Q - QI


def vertex(i):
    return [(i, +1), (i + 1, -1)]


def gg_word(vs):
    return [c for i in vs for c in vertex(i)]


def apply_crossing(vec, n, i, s):
    out = {}

    def add(k, v):
        if v:
            out[k] = out.get(k, LP()) + v
    sh = n - 2 - i
    for b, c in vec.items():
        x, y = (b >> (sh + 1)) & 1, (b >> sh) & 1
        base = b & ~(3 << sh)
        sw = base | (y << (sh + 1)) | (x << sh)
        if x == y:
            add(b, c * (Q if s > 0 else QI))
        elif (x, y) == (0, 1):
            add(sw, c)
            if s < 0:
                add(b, -H * c)
        else:
            add(sw, c)
            if s > 0:
                add(b, H * c)
    return out


def obs_trace(word, n, obs):
    tot = LP()
    for b in range(2 ** n):
        if not obs(b):
            continue
        v = {b: LP({0: 1})}
        for (i, s) in reversed(word):
            v = apply_crossing(v, n, i, s)
        if v.get(b):
            tot = tot + LP({n - 2 * bin(b).count("1"): 1}) * v[b]
    return tot


def main():
    data = json.load(open(HERE / "linked_classes.json"))
    q, t = sp.symbols("q", positive=True), sp.symbols("t")
    P = q**12 - 3*q**10 + 3*q**8 - 5*q**6 + 3*q**4 - 3*q**2 + 1
    D2 = q + 1/q
    eP = q*(-P/q**6)/D2**3
    eN = eP/q**2
    beta = gg_word((0, 0, 0)); n = 9
    obs = lambda b: bin(b >> 6).count("1") == 1  # noqa: E731
    rows, checks = [], []
    for c in data["classes"]:
        lv = [int(s) - 3 for s in c["lepton"].split("V")[1:]]
        X = [int(s) for s in c["junction"].split("V")[1:]] if c["junction"] else []
        W = gg_word(X) + beta + [(i + 3, s) for (i, s) in gg_word(lv)]
        assert sum(s for _, s in W) == 0
        T = obs_trace(W, n, obs)
        x = sum(v * q**k for k, v in T.d.items()) / D2**7
        xq0 = sp.lambdify(q, x, "mpmath")(Q0)
        checks.append((f"{c['kind']} {c['x_hat_q0_prefix']}: reproduces #8836 at q0",
                       abs(xq0 - mp.mpf(c["x_hat_q0_prefix"])) < mp.mpf("1e-9")))
        x1 = sp.limit(x, q, 1)
        g = sp.together(eN - x) if c["kind"] == "e-nubar" else sp.together(x - eP)
        num = sp.fraction(sp.factor(g))[0]
        poly = sp.Poly(sp.expand(num.subs(q, 1 + t)), t)
        rts = [r for r in sp.real_roots(poly) if 0 < r <= sp.Rational(3, 20)]
        mid = sp.sign(g.subs(q, sp.Rational(21, 20)))
        outside_all = (len(rts) == 0 and mid > 0)
        enter = None
        if rts:
            r0 = min(rts)
            enter = {"window_entry_or_exit_q": mp.nstr(1 + mp.mpf(sp.N(r0, 40)), 15)}
        rows.append({**c, "x_at_q1": str(x1), "x_q0": mp.nstr(xq0, 15),
                     "outside_window_on_(1,23/20]": bool(outside_all), **(enter or {})})
    for d, ok in checks:
        if not ok:
            print("FAIL", d)
    e_ok = all(r["outside_window_on_(1,23/20]"] for r in rows if r["kind"] == "e-nubar")
    m_in = [r for r in rows if r["kind"] == "mirror" and not r["outside_window_on_(1,23/20]"]]
    print(f"reproduce q0 values: {sum(o for _, o in checks)}/{len(checks)}")
    print(f"e-nubar: all {sum(r['kind']=='e-nubar' for r in rows)} classes below eps_n on the "
          f"whole range: {e_ok}")
    print(f"x_hat(1) values: {sorted(set(r['x_at_q1'] for r in rows))}")
    for r in m_in:
        print(f"mirror class enters the window for part of the range: x(q0) = {r['x_q0']}, "
              f"words {r['words_in_class']}, lepton {r['lepton']}, junction {r['junction']}, "
              f"boundary q = {r.get('window_entry_or_exit_q')}")
    out = {"description": "Exact linked-word lepton traces vs the window (eps_n, eps_p), all q "
                          "in (1, 23/20]. Exact Laurent arithmetic; exact real-root isolation.",
           "q0Anchor": "proton", "rows": rows,
           "summary": {"e_nubar_all_outside": e_ok,
                       "mirror_classes_entering_window": len(m_in),
                       "mirror_words_entering_window": sum(r["words_in_class"] for r in m_in)}}
    (HERE / "qbeta-lepton-linked-exact.witness.json").write_text(json.dumps(out, indent=1) + "\n")
    return 0 if all(o for _, o in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
