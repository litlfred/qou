#!/usr/bin/env python3
"""Six-strand neutral selection: route C step 1 of bean qou-cds1 (owner pick 2026-11-27).

Grammar. The ruled photon on strands (i, i+1, i+2) is
    gamma_i = 1 + phi0 s_i + phi1 s_{i+1} + phi01 s_i s_{i+1}^-1,   i = 0..3,
so the non-identity blocks on six strands are s_0..s_4 and V_i = s_i s_{i+1}^-1, i = 0..3.
A term of a product of photons is a concatenation of blocks.

Step 1 (structure, no compute). Term-by-term linking neutrality (owner 2026-11-21/25) forces
writhe 0 (QOU.MassTheory.ClimbingFamilyNeutralExclusion.writhe_eq_zero_of_neutral, four
strands; the same pair-count argument on six). Every s_i block has writhe 1 and every V_i
writhe 0, so a neutral term is a word in the V_i only.

Step 2 (this probe). Enumerate V-words of length 1..KMAX, free-reduce, keep the
linking-neutral ones, and apply reading 3 (Frobenius positivity: chi_lambda(w) >= 0 on every
block with y_lambda > 0; under convention D those are the two-row lambda |- 6). Characters are
evaluated EXACTLY (Fraction) in the Young seminormal representations of gg_ntower_probe, at the
proton-pinned q0 and, as a robustness check, at q = 11/10 and 23/20.

Output: the surviving words, by length. No magnitude is computed, compared or selected.
"""
import itertools
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "gg_ntower"))
import gg_ntower_probe as g  # noqa: E402
import sympy as sp  # noqa: E402

N = 6
KMAX = 6
QS = {"q0": g.Q0_RAT, "11/10": sp.Rational(11, 10), "23/20": sp.Rational(23, 20)}
SHAPES = g.two_row_shapes(N)  # (6),(5,1),(4,2),(3,3)
T0 = time.time()


def V(i):
    return [(i, 1), (i + 1, -1)]


def reduce_word(w):
    out = []
    for x in w:
        if out and out[-1][0] == x[0] and out[-1][1] == -x[1]:
            out.pop()
        else:
            out.append(x)
    return tuple(out)


def components(word):
    pos = list(range(N))
    for i, _ in word:
        pos[i], pos[i + 1] = pos[i + 1], pos[i]
    end = {lab: k for k, lab in enumerate(pos)}
    comp, seen = {}, set()
    for s in range(N):
        if s in seen:
            continue
        cyc, x = [], s
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = end[x]
        for x in cyc:
            comp[x] = min(cyc)
    return comp


def neutral(word):
    comp = components(word)
    pos = list(range(N))
    counts = {}
    for i, e in word:
        key = tuple(sorted((comp[pos[i]], comp[pos[i + 1]])))
        counts[key] = counts.get(key, 0) + e
        pos[i], pos[i + 1] = pos[i + 1], pos[i]
    return all(v == 0 for v in counts.values())


def frac(x):
    x = sp.Rational(x)
    return Fraction(int(x.p), int(x.q))


def mats_at(qv):
    """Generator and inverse matrices of each two-row block, as Fraction lists, at q = qv."""
    out = {}
    for lam in SHAPES:
        R = g.rep(lam)
        d = R.dim
        gens, invs = [], []
        hval = frac(qv - 1 / qv)
        for G in R.gen:
            M = [[frac(sp.cancel(g.K.to_sympy(G[a, b].element)).subs(g.q, qv)) for b in range(d)]
                 for a in range(d)]
            gens.append(M)
            invs.append([[M[a][b] - (hval if a == b else 0) for b in range(d)] for a in range(d)])
        out[lam] = (d, gens, invs)
    return out


def char(block, word):
    d, gens, invs = block
    M = [[Fraction(int(a == b)) for b in range(d)] for a in range(d)]
    for i, e in word:
        L = gens[i] if e == 1 else invs[i]
        M = [[sum(M[a][k] * L[k][b] for k in range(d)) for b in range(d)] for a in range(d)]
    return sum(M[a][a] for a in range(d))


def main():
    mats = {k: mats_at(v) for k, v in QS.items()}
    # sanity: Hecke relation s^2 = h s + 1 holds in every block at q0
    seen, rows = set(), []
    n_terms = n_neutral = 0
    for k in range(1, KMAX + 1):
        for idx in itertools.product(range(4), repeat=k):
            n_terms += 1
            w = reduce_word([x for i in idx for x in V(i)])
            if w in seen:
                continue
            seen.add(w)
            if not neutral(w):
                continue
            n_neutral += 1
            chis = {qk: {str(lam): char(mats[qk][lam], w) for lam in SHAPES} for qk in QS}
            ok = {qk: all(c >= 0 for c in chis[qk].values()) for qk in QS}
            rows.append({
                "V_indices": list(idx), "k": k, "reduced": [list(x) for x in w],
                "crossings": len(w),
                "reading3_q0": ok["q0"], "reading3_11/10": ok["11/10"],
                "reading3_23/20": ok["23/20"],
                "chi_q0_sign": {s: (1 if c > 0 else (-1 if c < 0 else 0))
                                for s, c in chis["q0"].items()},
            })
        print(f"[{time.time() - T0:6.1f}s] k={k} distinct={len(seen)} neutral={n_neutral}",
              flush=True)
    surv = [r for r in rows if r["reading3_q0"]]
    robust = [r for r in surv if r["reading3_11/10"] and r["reading3_23/20"]]
    min_cross = min((r["crossings"] for r in surv if r["crossings"] > 0), default=None)
    summary = {
        "terms_enumerated": n_terms,
        "distinct_reduced_words": len(seen),
        "neutral": n_neutral,
        "reading3_survivors_at_q0": len(surv),
        "survivors_also_at_11/10_and_23/20": len(robust),
        "min_nonzero_crossings_among_survivors": min_cross,
        "minimal_survivors": [r for r in surv if r["crossings"] == min_cross],
        "survivors_by_crossings": {},
    }
    for r in surv:
        summary["survivors_by_crossings"].setdefault(r["crossings"], 0)
        summary["survivors_by_crossings"][r["crossings"]] += 1
    out = {
        "computation": "six-strand-neutral-selection",
        "scriptFile": Path(__file__).name,
        "kind": "enumeration + exact filter (Fraction); no magnitude, no comparison, no selection by value",
        "beans": ["qou-cds1", "qou-4f8t"],
        "q0Anchor": "proton",
        "q0AnchorReason": "reading-3 signs evaluated at the proton-pinned q0 (Q_50_DIGIT_STR); "
                          "11/10 and 23/20 are robustness points",
        "markov_convention": "D (two-row blocks only)",
        "grammar": "blocks s_0..s_4, V_i = s_i s_{i+1}^-1 (i=0..3); neutral => V-words only",
        "KMAX": KMAX,
        "summary": summary,
        "rows": rows,
    }
    (HERE / "six-strand-neutral-selection.witness.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: v for k, v in summary.items() if k != "minimal_survivors"}, indent=1))
    for r in summary["minimal_survivors"][:20]:
        print("  minimal survivor V", r["V_indices"], "reduced", r["reduced"])


if __name__ == "__main__":
    main()
