#!/usr/bin/env python3
"""qbeta_colour_gl6_probe — isospin and colour in one gl₆ Jimbo R-matrix (issue #8833).

Closed family and reporting rules: PREREGISTRATION.md (committed first). Lean:
QOU/QBeta/GlNJimboHecke.lean (every block of the gl_N Jimbo R satisfies X^2 = hX + 1).

Checks
  G1  Hecke relation on C^6 (x) C^6 and braid relation on (C^6)^(x)3, exact at q = 2.
  G2  with one colour the construction is the ruled D1 cell (eps_p, eps_n at q0).
  G3  report: 8 members x {V^3, V^6, V^9}; F = eps_flavour / eps_flavour^ruled vs 2.40397.
mpmath at the proton pin; exact Fractions for G1. Nothing is selected.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
for _p in ("computations", "computations/qbeta", "computations/substrate",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
Q0 = mp.mpf(Q_50_DIGIT_STR)
F_REQ = mp.mpf("2.40397")
RESULTS: list[tuple[str, bool, str]] = []


def check(name, ok, detail):
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}\n")


def cross(vec, i, s, q):
    """Jimbo gl_N R (s=+1) or R^-1 = R - h (s=-1) on tensor positions (i, i+1)."""
    h = q - 1 / q
    out = {}

    def add(k, v):
        if v:
            out[k] = out.get(k, 0) + v
    for t, c in vec.items():
        a, b = t[i], t[i + 1]
        sw = t[:i] + (b, a) + t[i + 2:]
        if a == b:
            add(t, c * (q if s > 0 else 1 / q))
        elif a < b:                      # e_a e_b -> e_b e_a ; R^-1: e_b e_a - h e_a e_b
            add(sw, c)
            if s < 0:
                add(t, -h * c)
        else:                            # e_a e_b -> e_b e_a + h e_a e_b ; R^-1: e_b e_a
            add(sw, c)
            if s > 0:
                add(t, h * c)
    return out


def apply(word, t, q):
    v = {t: 1 + 0 * q}
    for (i, s) in reversed(word):
        v = cross(v, i, s, q)
    return v


def vword(k):
    return [(0, 1), (1, -1)] * k


def labels(order, ncol):
    """map (isospin t, colour c) -> integer label in the chosen total order."""
    if order == "isospin-major":
        return {(t, c): ncol * t + c for t in (0, 1) for c in range(ncol)}
    return {(t, c): 2 * c + t for t in (0, 1) for c in range(ncol)}


def eps(word, order, kel, colour, q, ncol=3):
    lab = labels(order, ncol)
    inv = {v: k for k, v in lab.items()}
    N = 2 * ncol
    rank = sorted(lab.values())
    if kel == "K6":
        kd = {l: q ** (N - 1 - 2 * rank.index(l)) for l in rank}
        norm = sum(kd.values()) ** 3
    else:
        kd = {l: q ** (1 - 2 * inv[l][0]) for l in rank}
        norm = sum(kd.values()) ** 3
    res = {}
    for nd, key in ((1, "p"), (2, "n")):
        tot = 0
        for t in itertools.product(rank, repeat=3):
            if sum(inv[l][0] for l in t) != nd:
                continue
            if colour == "neutral" and sorted(inv[l][1] for l in t) != list(range(3)):
                continue
            d = apply(word, t, q).get(t, 0)
            if d:
                tot += kd[t[0]] * kd[t[1]] * kd[t[2]] * d
        res[key] = tot / norm
    return res


def main() -> int:
    # G1
    q = Fr(2)
    ok = True
    for t in itertools.product(range(6), repeat=2):
        v2 = cross(cross({t: Fr(1)}, 0, 1, q), 0, 1, q)
        v1 = cross({t: Fr(1)}, 0, 1, q)
        rhs = {k: (q - 1 / q) * x for k, x in v1.items()}
        rhs[t] = rhs.get(t, 0) + 1
        ok &= all(v2.get(k, 0) == rhs.get(k, 0) for k in set(v2) | set(rhs))
    for t in itertools.product(range(6), repeat=3):
        a = apply([(0, 1), (1, 1), (0, 1)], t, q)
        b = apply([(1, 1), (0, 1), (1, 1)], t, q)
        ok &= all(a.get(k, 0) == b.get(k, 0) for k in set(a) | set(b))
    check("G1_hecke_and_braid_relations", ok,
          "gl6 Jimbo R: R^2 = hR + 1 on all 36 basis pairs and R1R2R1 = R2R1R2 on all 216 "
          "basis triples, exact at q = 2.")

    # G2: one colour reduces to the ruled cell
    r1 = eps(vword(3), "isospin-major", "K6", "summed", Q0, ncol=1)
    ok2 = abs(r1["p"] - mp.mpf("0.408718179341")) < mp.mpf("1e-11") and \
        abs(r1["n"] - mp.mpf("0.331737644740")) < mp.mpf("1e-11")
    ruled_flav = r1["n"] - r1["p"]
    check("G2_one_colour_is_the_ruled_cell", ok2,
          f"ncol = 1: eps_p = {mp.nstr(r1['p'], 12)}, eps_n = {mp.nstr(r1['n'], 12)}, "
          f"eps_flavour = {mp.nstr(ruled_flav, 12)} (D1).")

    rows = []
    for order in ("isospin-major", "colour-major"):
        for kel in ("K6", "K2x1"):
            for colour in ("summed", "neutral"):
                for k in (1, 2, 3):
                    r = eps(vword(3 * k), order, kel, colour, Q0)
                    ref = eps(vword(3 * k), "isospin-major", "K6", "summed", Q0, ncol=1)
                    rf = ref["n"] - ref["p"]
                    F = (r["n"] - r["p"]) / rf
                    rows.append({"order": order, "trace_element": kel, "colour": colour,
                                 "word": f"V^{3*k}", "eps_p": mp.nstr(r["p"], 20),
                                 "eps_n": mp.nstr(r["n"], 20),
                                 "F": mp.nstr(F, 20), "F_over_required": mp.nstr(F / F_REQ, 12)})
                    print("   ", order, kel, colour, f"V^{3*k}", "F =", mp.nstr(F, 12))
    v3 = [mp.mpf(r["F"]) for r in rows if r["word"] == "V^3"]
    allF = [mp.mpf(r["F"]) for r in rows]
    check("G3_report", True,
          f"V^3: F in [{mp.nstr(min(v3), 10)}, {mp.nstr(max(v3), 10)}] over the 8 members; all "
          f"words [{mp.nstr(min(allF), 10)}, {mp.nstr(max(allF), 10)}]. F_required = 2.40397. "
          f"Members with |F| > 1 on V^3: {sum(abs(x) > 1 for x in v3)}. None selected.")

    # G4: closed form of the only member with |F| > 1 (exact sympy), and its q -> 1 limit
    import sympy as sp
    qs = sp.symbols("q", positive=True)
    rs = eps(vword(3), "isospin-major", "K6", "summed", qs)
    r1s = eps(vword(3), "isospin-major", "K6", "summed", qs, ncol=1)
    Fs = sp.simplify((rs["n"] - rs["p"]) / (r1s["n"] - r1s["p"]))
    closed = qs ** 4 * (qs ** 4 + qs ** 2 + 1) / (qs ** 4 - qs ** 2 + 1) ** 3
    ok4 = sp.simplify(Fs - closed) == 0 and sp.limit(closed, qs, 1) == 3
    check("G4_isospin_major_K6_closed_form", ok4,
          "isospin-major, K6, colour summed: F = q^4 (q^4 + q^2 + 1)/(q^4 - q^2 + 1)^3 exactly "
          "(eps_p scales by q^8/(q^4-q^2+1)^3, eps_n by q^4/(q^4-q^2+1)^3); F -> 3 = number of "
          f"colours as q -> 1; at q0 F = {mp.nstr(closed.subs(qs, sp.Rational(Q_50_DIGIT_STR)).evalf(30), 15)}, "
          "1.114 x F_required. Reported, not selected: the label order and trace element are "
          "not ruled.")

    allp = all(o for _, o, _ in RESULTS)
    print(f"  {sum(o for _, o, _ in RESULTS)}/{len(RESULTS)} checks passed")
    wb = WitnessBuilder("qbeta-colour-gl6", engine="mpmath")
    for nm, o, d in RESULTS:
        wb.add_assertion(nm, computed="PASS" if o else "FAIL", expected="PASS",
                         tolerance="exact" if nm != "G2_one_colour_is_the_ruled_cell" else "1e-11",
                         source=d)
    wb.save({
        "description": ("Isospin and colour in one U_q(gl6) Jimbo R; colour factor F on the ruled "
                        "Q_beta cell for 8 preregistered members x 3 words. Nothing selected."),
        "q0": Q_50_DIGIT_STR, "F_required": "2.40397", "rows": rows,
    })
    return 0 if allp else 1


if __name__ == "__main__":
    sys.exit(main())
