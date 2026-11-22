#!/usr/bin/env python3
"""he4_multi_gap_bond_probe.py -- bonds with >= 2 interface letters, both chiralities
(issue #8960).  Preregistration: preregistration.md (written first).

Lean (MassEndomorphism/MarkovTraceMultiGapBond.lean): with two gap letters and the piece
between them A C^(3), the atom trace is rank 1 in (x, y) unless A contains sigma_1 AND
C contains sigma_3 (towerTr_twoGap_outerLeft/Right_crossRatio); in that case a cable
term tr(P Q^ sigma_2 sigma_1 sigma_3 sigma_2) appears (towerTr_twoGap).

Exact Fractions, Markov trace at z_D, proton pin and q = 1.  No float; mpmath for
printing only.
"""
import datetime
import itertools
import json
import subprocess
import sys
import time
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[2]
sys.path.insert(0, str(_ROOT / "computations" / "probes" / "he4_bond_both_nucleons"))
import he4_bond_both_nucleons_probe as base  # noqa: E402  (sets its own sys.path)
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
import mpmath as mp  # noqa: E402

Markov = base.Markov
S3_WORDS = [[], [0], [1], [0, 1], [1, 0], [0, 1, 0]]


def bond(M, verts, chir):
    w = []
    for i in verts:
        if chir == "V":   # sigma_i sigma_{i+1}^-1
            w += [(F(1), F(0), i), (F(1), -M.h, i + 1)]
        else:             # mirror: sigma_i^-1 sigma_{i+1}
            w += [(F(1), -M.h, i), (F(1), F(0), i + 1)]
    return w


def letters(verts):
    return [g for i in verts for g in (i, i + 1)]


def structure(verts):
    L = letters(verts)
    pos = [k for k, g in enumerate(L) if g == 2]
    pieces = [L[pos[k] + 1:pos[k + 1]] for k in range(len(pos) - 1)]
    return len(pos), [{"left_inner": 1 in p, "right_inner": 3 in p, "piece": p} for p in pieces]


def basis_word(off, rw):
    return [(F(1), F(0), g + off) for g in rw]


def rank(mat):
    m = [row[:] for row in mat]; r = 0; nr, nc = len(m), len(m[0])
    for c in range(nc):
        piv = next((i for i in range(r, nr) if m[i][c] != 0), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        for i in range(nr):
            if i != r and m[i][c] != 0:
                f = m[i][c] / m[r][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        r += 1
    return r


def solve_left(mat, v):
    """x with x^T mat = v^T (exact; asserts consistency)."""
    n = len(mat)
    A = [[mat[i][j] for i in range(n)] + [v[j]] for j in range(n)]
    r = 0; piv = []
    for c in range(n):
        p = next((i for i in range(r, n) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        for i in range(n):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
    assert all(A[i][n] == 0 for i in range(r, n))
    x = [F(0)] * n
    for k, c in enumerate(piv):
        x[c] = A[k][n] / A[k][c]
    return x


def affine_c(mat, u, v):
    """If rank 2 and u in col space, v in row space: mu = c + l'(x) r'(y); return c."""
    if rank([mat[i] + [u[i]] for i in range(6)]) != 2 or rank(mat + [v]) != 2:
        return None
    x = solve_left(mat, v)
    return 1 / sum(a * b for a, b in zip(u, x))


def random_search(M, B, bx, by, freeB, mat, seed=1, N=40):
    """Exact search over random integer combinations of the T_w bases (no float)."""
    import random
    rnd = random.Random(seed)
    X = [[rnd.randint(-3, 3) for _ in range(6)] for _ in range(N)]
    Y = [[rnd.randint(-3, 3) for _ in range(6)] for _ in range(N)]
    def bil(T, x, y):
        return sum(x[i] * T[i][j] * y[j] for i in range(6) for j in range(6) if x[i] and y[j])
    mu = [[(bil(mat, X[i], Y[j]) / bil(freeB, X[i], Y[j])) if bil(freeB, X[i], Y[j]) != 0 else None
           for j in range(N)] for i in range(N)]
    G = [[m is not None and m > 1 for m in r] for r in mu]
    L = [[m is not None and 0 < m < 1 for m in r] for r in mu]
    hits = 0; ex = None
    for i1, i2 in itertools.permutations(range(N), 2):
        for j1, j2 in itertools.permutations(range(N), 2):
            if G[i1][j1] and G[i2][j2] and L[i1][j2] and L[i2][j1]:
                hits += 1
                if ex is None:
                    ex = {"x1": X[i1], "x2": X[i2], "y1": Y[j1], "y2": Y[j2],
                          "mu": {"pp": nstr(mu[i1][j1]), "pn": nstr(mu[i1][j2]),
                                 "np": nstr(mu[i2][j1]), "nn": nstr(mu[i2][j2])}}
    return hits, ex


def nstr(x):
    return mp.nstr(mp.mpf(x.numerator) / x.denominator, 15)


def pattern(mu):
    strong = mu["pn"] < 1 and mu["np"] < 1 and mu["pp"] > 1 and mu["nn"] > 1
    weak = (mu["pn"] < 1 or mu["np"] < 1) and mu["pp"] > 1 and mu["nn"] > 1
    return strong, weak


def run(q, label, do_rank):
    M = Markov(q)
    t0 = time.time()
    nuc = {(x, o): M.nucleon(x, o) for x in "pn" for o in (0, 3)}
    free = {x + y: M.tr_word(nuc[(x, 0)] + nuc[(y, 3)]) for x, y in itertools.product("pn", repeat=2)}
    bx = [basis_word(0, rw) for rw in S3_WORDS]
    by = [basis_word(3, rw) for rw in S3_WORDS]
    freeB = [[M.tr_word(a + b) for b in by] for a in bx] if do_rank else None
    words = [v for k in (1, 2, 3) for v in itertools.product(range(4), repeat=k)]
    out = {}
    for chir in ("V", "M"):
        rows = []
        for idx, verts in enumerate(words):
            B = bond(M, verts, chir)
            mu = {x + y: M.tr_word(nuc[(x, 0)] + nuc[(y, 3)] + B) / free[x + y]
                  for x, y in itertools.product("pn", repeat=2)}
            ngap, pieces = structure(verts)
            gs = set(letters(verts))
            both = bool(gs & {0, 1}) and bool(gs & {3, 4})
            cross = mu["pp"] * mu["nn"] == mu["pn"] * mu["np"]
            strong, weak = pattern(mu)
            row = {"verts": list(verts), "n_gap": ngap, "pieces": pieces, "both": both,
                   "mu": mu, "cross_ratio_holds": cross, "pattern": strong, "pattern_weak": weak}
            if do_rank and both and ngap >= 2:
                mat = [[M.tr_word(a + b + B) for b in by] for a in bx]
                row["bilinear_rank"] = rank(mat)
                if not cross:
                    hits = 0; example = None
                    for i1, i2 in itertools.permutations(range(6), 2):
                        for j1, j2 in itertools.permutations(range(6), 2):
                            fr = [freeB[i1][j1], freeB[i1][j2], freeB[i2][j1], freeB[i2][j2]]
                            if any(f == 0 for f in fr):
                                continue
                            m = {"pp": mat[i1][j1] / fr[0], "pn": mat[i1][j2] / fr[1],
                                 "np": mat[i2][j1] / fr[2], "nn": mat[i2][j2] / fr[3]}
                            if all(v > 0 for v in m.values()) and pattern(m)[0]:
                                hits += 1
                                if example is None:
                                    example = {"x": [S3_WORDS[i1], S3_WORDS[i2]],
                                               "y": [S3_WORDS[j1], S3_WORDS[j2]],
                                               "mu": {k: nstr(v) for k, v in m.items()}}
                    row["basis_pattern_hits"] = hits
                    row["basis_pattern_example"] = example
                    ux = [M.tr_word(a) for a in bx]; vy = [M.tr_word(b) for b in by]
                    c = affine_c(mat, ux, vy)
                    row["affine_c"] = None if c is None else nstr(c)
                    row["affine_c_le_half"] = None if c is None else bool(c <= F(1, 2))
                    rh, rex = random_search(M, B, bx, by, freeB, mat)
                    row["random_combo_pattern_hits"] = rh
                    row["random_combo_pattern_example"] = rex
            rows.append(row)
            if idx % 21 == 0:
                print(f"  [{label} {chir}] word {idx+1}/84  {time.time()-t0:.1f}s", flush=True)
        out[chir] = rows
    if do_rank:
        cable = [(F(1), F(0), 2), (F(1), F(0), 1), (F(1), F(0), 3), (F(1), F(0), 2)]
        out["cable_rank"] = rank([[M.tr_word(a + b + cable) for b in by] for a in bx])
        out["free_rank"] = rank(freeB)
    return out


def main():
    q0 = F(Q_50_DIGIT_STR)
    r0 = run(q0, "q0", True)
    r1 = run(F(1), "q=1", False)
    checks = []
    for chir in ("V", "M"):
        rows = r0[chir]
        two = [r for r in rows if r["both"] and r["n_gap"] == 2]
        outer = [r for r in two if not (r["pieces"][0]["left_inner"] and r["pieces"][0]["right_inner"])]
        checks.append((f"{chir}: n_gap=2, an inner letter absent -> cross-ratio exact "
                       "(towerTr_twoGap_outer*_crossRatio)", bool(outer) and all(r["cross_ratio_holds"] for r in outer)))
        checks.append((f"{chir}: n_gap<=1 'both' -> cross-ratio exact",
                       all(r["cross_ratio_holds"] for r in rows if r["both"] and r["n_gap"] <= 1)))
        checks.append((f"{chir}: n_gap=2 cross-ratio holds -> bilinear rank 1",
                       all(r["bilinear_rank"] == 1 for r in two if r["cross_ratio_holds"])))
        checks.append((f"{chir}: q=1 all four mu equal", all(len(set(r["mu"].values())) == 1 for r in r1[chir])))
        checks.append((f"{chir}: every mu > 0 at q0", all(v > 0 for r in rows for v in r["mu"].values())))
        # label swap p<->n: (pp,pn,np,nn) -> (nn,np,pn,pp); strong pattern invariant
        def sw(m): return {"pp": m["nn"], "pn": m["np"], "np": m["pn"], "nn": m["pp"]}
        checks.append((f"{chir}: strong pattern invariant under p<->n label swap",
                       all(pattern(r["mu"])[0] == pattern(sw(r["mu"]))[0] for r in rows)))
    checks.append(("free form has bilinear rank 1", r0["free_rank"] == 1))
    for chir in ("V", "M"):
        fl = [r for r in r0[chir] if r["both"] and not r["cross_ratio_holds"]]
        checks.append((f"{chir}: affine-form words (c <= 1/2): no combination hit "
                       "(consistent with not_pattern_of_affine_rankOne)",
                       all(r["random_combo_pattern_hits"] == 0 for r in fl if r["affine_c_le_half"])))
    summary = {}
    for chir in ("V", "M"):
        rows = r0[chir]
        fails = [r for r in rows if r["both"] and not r["cross_ratio_holds"]]
        summary[chir] = {
            "both": sum(r["both"] for r in rows),
            "both_ngap_ge2": sum(r["both"] and r["n_gap"] >= 2 for r in rows),
            "cross_ratio_fails": [r["verts"] for r in fails],
            "fails_ngap": [r["n_gap"] for r in fails],
            "fails_rank": [r["bilinear_rank"] for r in fails],
            "fails_basis_pattern_hits": [r["basis_pattern_hits"] for r in fails],
            "fails_affine_c": [r["affine_c"] for r in fails],
            "fails_random_combo_hits": [r["random_combo_pattern_hits"] for r in fails],
            "strong_pattern_words": [r["verts"] for r in rows if r["pattern"]],
            "weak_pattern_words": [r["verts"] for r in rows if r["pattern_weak"]],
        }
        print(f"\n  [{chir}] {json.dumps(summary[chir])}")
        for r in fails:
            m = r["mu"]
            print(f"   {str(r['verts']):10s} ngap={r['n_gap']} rank={r['bilinear_rank']} "
                  + " ".join(f"{k}={nstr(m[k])}" for k in ('pp', 'pn', 'np', 'nn'))
                  + f"  basis-hits={r['basis_pattern_hits']} c={r['affine_c']} "
                  f"combo-hits={r['random_combo_pattern_hits']}")
    print(f"  cable word sigma2 sigma1 sigma3 sigma2 bilinear rank: {r0['cable_rank']}")
    for n, p in checks:
        print(f"  [{'PASS' if p else 'FAIL'}] {n}")

    def ser(rows):
        o = []
        for r in rows:
            d = {k: v for k, v in r.items() if k != "mu"}
            d["mu"] = {k: nstr(v) for k, v in r["mu"].items()}
            o.append(d)
        return o
    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=_ROOT, capture_output=True,
                             text=True, check=True).stdout.strip()
    except Exception:
        sha = ""
    w = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "fractions",
        "scriptFile": Path(__file__).name,
        "commitSha": sha,
        "q0Anchor": "proton",
        "q0AnchorReason": "Fraction(Q_50_DIGIT_STR); convention D (z = q^3/(q^2+1))",
        "q0": Q_50_DIGIT_STR,
        "description": ("bonds of 1..3 vertices, two chiralities (V: s_i s_{i+1}^-1, M: s_i^-1 s_{i+1}), "
                        "appended to X Y^(3) in H_6; mu for pp,pn,np,nn; cross-ratio, exact bilinear "
                        "rank on the 6x6 T_w bases, pattern search. Preregistered."),
        "lean": [f"QOU.BraidKnot.HeckeFunctional.{t}" for t in (
            "towerTr_twoGap", "towerTr_twoGap_cable", "towerTr_twoGapBond_reduce",
            "towerTr_twoLetter_expand", "towerTr_twoGap_outerLeft", "towerTr_twoGap_outerRight",
            "towerTr_twoGap_outerLeft_crossRatio", "towerTr_twoGap_outerRight_crossRatio",
            "not_pattern_of_affine_rankOne")],
        "summary": summary,
        "cable_word_bilinear_rank": r0["cable_rank"],
        "free_bilinear_rank": r0["free_rank"],
        "rows_q0": {c: ser(r0[c]) for c in ("V", "M")},
        "rows_q1": {c: ser(r1[c]) for c in ("V", "M")},
        "assertions": [{"name": n, "passed": bool(p)} for n, p in checks],
        "allPassed": all(p for _, p in checks),
    }
    (_HERE / "he4-multi-gap-bond.witness.json").write_text(json.dumps(w, indent=1) + "\n")
    return 0 if w["allPassed"] else 1


if __name__ == "__main__":
    sys.exit(main())
