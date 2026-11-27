#!/usr/bin/env python3
"""Counterexample to the six-strand "multiple of 3" rule (bean qou-cds1).

The rule under test (audit 2026-11-27-cds1-six-strand-neutral-selection, finding 1, measured
for words of at most six vertices): every linking-neutral V-word that passes reading 3 uses
each vertex V_i = s_i s_{i+1}^-1 a multiple of 3 times.

This probe checks the ten-vertex word W = (V_0 V_2)^5 (twenty crossings), whose vertex counts
are (5, 0, 5, 0), and its mirror (V_1 V_3)^5.

  1. W is a pure braid (its permutation is the identity), so the closure has six components.
  2. W is linking-neutral (every pairwise signed crossing count is 0), using the probe's own
     `neutral` and an independent strand-tracking count.
  3. For each two-row shape lambda |- 6 the character chi_lambda(W) is computed EXACTLY as a
     Laurent polynomial in q: exact Fraction evaluation in the Young seminormal blocks of
     gg_ntower_probe at 2n+1 rational points, Lagrange interpolation, and a check at an
     extra point. (chi is a Laurent polynomial of q-degree at most n = 20.)
  4. Reading 3 is read off at q0 (the proton pin of gg_ntower_probe), 11/10 and 23/20, and
     the first sign change above q = 1 is isolated by exact rational intervals.

No magnitude is compared to anything measured; q0 enters only as the point at which the
existing selection rule is evaluated, exactly as in the neutral-selection probe.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import six_strand_neutral_selection_probe as P  # noqa: E402
import sympy as sp  # noqa: E402

q = sp.symbols("q")
CHECK_PT = sp.Rational(7, 3)


def word(idx):
    return P.reduce_word([x for i in idx for x in P.V(i)])


def perm(w):
    p = list(range(P.N))
    for i, _ in w:
        p[i], p[i + 1] = p[i + 1], p[i]
    return p


def pair_counts(w):
    pos, out = list(range(P.N)), {}
    for i, e in w:
        key = tuple(sorted((pos[i], pos[i + 1])))
        out[key] = out.get(key, 0) + e
        pos[i], pos[i + 1] = pos[i + 1], pos[i]
    return out


def rat(x):
    return sp.Rational(x.numerator, x.denominator)


def char_poly(w, mats_cache):
    n = len(w)
    pts = [sp.Rational(k + 2, k + 1) for k in range(2 * n + 1)]
    out = {}
    for lam in P.SHAPES:
        vals = [rat(P.char(mats_cache[v][lam], w)) * v**n for v in pts]
        num = sp.expand(sp.interpolate(list(zip(pts, vals)), q))  # q^n * chi
        chi = sp.expand(num / q**n)
        assert rat(P.char(mats_cache[CHECK_PT][lam], w)) == chi.subs(q, CHECK_PT)
        out[lam] = (chi, num)
    return out


def main():
    words = {"(V0 V2)^5": (0, 2) * 5, "(V1 V3)^5": (1, 3) * 5}
    need = set()
    for idx in words.values():
        n = len(word(idx))
        need |= {sp.Rational(k + 2, k + 1) for k in range(2 * n + 1)}
    need |= {CHECK_PT}
    mats_cache = {v: P.mats_at(v) for v in sorted(need)}
    evals = {k: P.mats_at(v) for k, v in P.QS.items()}
    report = {}
    for name, idx in words.items():
        w = word(idx)
        counts = [idx.count(i) for i in range(4)]
        polys = char_poly(w, mats_cache)
        rows = {}
        first_root = None
        for lam, (chi, num) in polys.items():
            signs = {qk: int(sp.sign(rat(P.char(evals[qk][lam], w)))) for qk in P.QS}
            ivs = [iv for iv in sp.Poly(num, q).intervals(eps=sp.Rational(1, 10**6)) if iv[0][0] >= 1]
            ivs = [(sp.Rational(a), sp.Rational(b)) for (a, b), _ in ivs]
            lo = min(ivs, key=lambda t: t[0]) if ivs else None
            if lo and (first_root is None or lo[0] < first_root[0]):
                first_root = lo
            rows[str(lam)] = {
                "chi_laurent": str(chi),
                "chi_at_q_eq_1": str(chi.subs(q, 1)),
                "sign_at": signs,
                "roots_above_1_isolating_intervals": [[str(a), str(b)] for a, b in ivs],
            }
        passes = {qk: all(r["sign_at"][qk] >= 0 for r in rows.values()) for qk in P.QS}
        report[name] = {
            "V_indices": list(idx), "vertex_counts": counts,
            "counts_mod_3": [c % 3 for c in counts],
            "crossings": len(w), "permutation": perm(w),
            "pure": perm(w) == list(range(P.N)),
            "neutral_probe": P.neutral(w),
            "pair_counts_independent": {f"{a}-{b}": v for (a, b), v in pair_counts(w).items()},
            "reading3_pass": passes,
            "first_sign_change_above_1_in": [str(first_root[0]), str(first_root[1])] if first_root else None,
            "characters": rows,
        }
        assert report[name]["pure"] and report[name]["neutral_probe"]
        assert all(v == 0 for v in pair_counts(w).values())
        print(name, "counts", counts, "pure", True, "neutral", True, "reading3", passes,
              "first sign change in", report[name]["first_sign_change_above_1_in"])
    out = {
        "computation": "six-strand-mod3-counterexample",
        "scriptFile": Path(__file__).name,
        "kind": "exact (Fraction + rational interpolation); no magnitude, no comparison",
        "beans": ["qou-cds1"],
        "q0Anchor": "proton",
        "q0AnchorReason": "reading 3 is evaluated at the same points as "
                          "six_strand_neutral_selection_probe (q0, 11/10, 23/20)",
        "claim_tested": "neutral + reading 3 => every V_i count = 0 mod 3",
        "verdict": "false at ten vertices: (V0 V2)^5 and (V1 V3)^5 are pure, neutral and pass "
                   "reading 3 at all three q, with counts 5",
        "words": report,
    }
    (HERE / "six-strand-mod3-counterexample.witness.json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
