#!/usr/bin/env python3
"""H_6: does the BAND reading change what the confinement SDP selects at the
INTERFACE -- the one place it still could?

`band_vertex_h3_frobenius_selector_probe.py` (8/8) closed pick B's H_3 leg as a
negative: all six band gamma-gamma vertices in `H_3` are one conjugacy class, so
reading 3 selects the same `beta_Bor` the Artin vertex gives.  That argument is
local to `H_3` and says nothing about `H_6`, where the INTER-NUCLEON bond lives
and where a band can join two strands in DIFFERENT nucleon blocks -- exactly the
move the Artin reading cannot make.  This probe measures that.

## Setup

Strands `0..5`, nucleon blocks `{0,1,2}` and `{3,4,5}` (the contiguous layout).
`H_6` has `C(6,2) = 15` BKL bands `a_(t,s)`; a band gamma-gamma vertex is an
ordered pair of distinct bands sharing exactly one strand, `a b^-1`.  **Nine** of
the fifteen bands cross the interface (`3 x 3`, one strand from each block), and
only ONE of those is an Artin generator (`a_(3,2) = sigma_2`) -- so eight of the
nine join non-adjacent nucleon strands, which is precisely the move the Artin
reading cannot make.

The Artin reading admits exactly one interface vertex,
`G = sigma_2 sigma_3^-1 = a_(3,2) a_(4,3)^-1`, and `qou-ales` step 6 measured
that reading 3 selects `G^3`.

## The selection rule

Owner ruling 2026-09-12: reading 3, Frobenius positivity -- `chi_lambda(w) >= 0`
on every block with `y_lambda > 0`.  Under convention D the two-row truncation
puts `y > 0` on exactly `(6), (5,1), (4,2), (3,3)` (verified, CHECK 1), so those
four blocks decide and the other seven are silent.

Readings 1 and 2 are recorded alongside per the owner's "keep 1 2 for later".

## What is measured

1. `y_lambda > 0` on exactly the four two-row blocks (CHECK 1).
2. The 15 bands, which six cross the interface, and that only `a_(3,2)` among
   them is an Artin generator (CHECK 2).
3. That `a_(3,2) a_(4,3)^-1` reproduces `sigma_2 sigma_3^-1` as a matrix on every
   deciding block (CHECK 3) -- the anchor to `qou-ales` step 6.
4. Every band gamma-gamma vertex, its character vector, and its reading-3
   feasible set over `k = 1..10` (CHECK 4-6).
5. **The question this probe exists for:** whether any INTER-BLOCK band vertex
   -- one whose bands join non-adjacent nucleon strands -- has a feasible set or
   a minimal survivor DIFFERENT from the Artin interface vertex's (CHECK 7).

## Scope

Whatever the answer, it is scope (a): one algebra (`H_6`, i.e. `A = 2`), one
pin, one reading.  A negative here does NOT structurally exclude the band
reading at higher `A`; it measures that the enlargement buys nothing where the
interface actually lives.

NOT claimed: which reading the physics means; any binding number; anything about
`A >= 3` or the eleven-letter nucleon words.

mpmath at 60 dps end to end, proton pin.  Writes no witness, runs no producer,
reads no AME/CODATA/census.
"""
from __future__ import annotations

import sys
import time
from itertools import combinations
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/substrate", "computations/hecke", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

DPS = 60
set_compute_dps(DPS)
TOL = mp.mpf("1e-40")
KMAX = 10
BLOCK_OF = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1}


def s_(i):
    return (mp.mpf(1), mp.mpf(0), i)


def sinv_(i, h):
    return (mp.mpf(1), -h, i)


def band(lo, hi, h):
    left = [s_(j) for j in range(hi - 1, lo, -1)]
    right = [sinv_(j, h) for j in range(lo + 1, hi)]
    return left + [s_(lo)] + right


def band_inv(lo, hi, h):
    left = [s_(j) for j in range(hi - 1, lo, -1)]
    right = [sinv_(j, h) for j in range(lo + 1, hi)]
    return left + [sinv_(lo, h)] + right


def word_image(sigmas, dim, word):
    M = mp.eye(dim)
    I = mp.eye(dim)
    for c, d, g in word:
        M = M * (c * sigmas[g] + d * I)
    return M


def trace(M, dim):
    return mp.fsum(M[i, i] for i in range(dim))


def main() -> int:
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        if not ok:
            failures.append(name)

    t0 = time.time()
    q = Q_MP
    h = q - 1 / q
    print("=" * 78)
    print("H_6 interface: does the BAND reading change what the SDP selects?")
    print("=" * 78)
    print(f"  proton pin q = {mp.nstr(q, 22)}   h^2 = {mp.nstr(h * h, 16)}")

    # ---- CHECK 1: convention-D support
    parts6 = [(6,), (5, 1), (4, 2), (3, 3), (4, 1, 1), (3, 2, 1),
              (2, 2, 2), (3, 1, 1, 1), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1,) * 6]
    y6 = y_lambda_su_n(6, q, 2)
    deciding = [lam for lam in parts6 if y6[lam] > TOL]
    print("\n[1] convention-D weights")
    for lam in parts6:
        flag = "  <- decides" if y6[lam] > TOL else ""
        print(f"    y_{str(lam):<16} = {mp.nstr(y6[lam], 12):>16}{flag}")
    check("y > 0 on exactly the four two-row blocks",
          set(deciding) == {(6,), (5, 1), (4, 2), (3, 3)},
          f"{len(deciding)} deciding of {len(parts6)}; the other seven are silent")

    cache = BlockCacheMP(q, h)
    blocks = {}
    for lam in deciding:
        sig, dim, _ = seminormal_matrices_mp(lam, cache=cache)
        blocks[lam] = (sig, dim)
    print(f"    block dims: " + ", ".join(f"{lam}:{blocks[lam][1]}" for lam in deciding))

    # ---- CHECK 2: the bands, and which cross the interface
    print("\n[2] the 15 bands of H_6")
    bands = {}
    for lo, hi in combinations(range(6), 2):
        bands[(lo, hi)] = band(lo, hi, h)
    interface = [(lo, hi) for (lo, hi) in bands if BLOCK_OF[lo] != BLOCK_OF[hi]]
    artin_bands = [(lo, hi) for (lo, hi) in bands if hi == lo + 1]
    print(f"    total {len(bands)};  crossing the interface: {len(interface)} -> {interface}")
    print(f"    Artin generators among them: "
          f"{[b for b in interface if b in artin_bands]}")
    check("exactly nine bands cross the interface (3 strands x 3 strands)",
          len(interface) == 9,
          "|block 0| * |block 1| = 3*3; this assertion read 'six' on the first run "
          "and was my arithmetic, not the corpus's")
    check("exactly ONE of them is an Artin generator, a_(3,2) = sigma_2",
          [b for b in interface if b in artin_bands] == [(2, 3)],
          "the other eight join non-adjacent nucleon strands -- the move Artin cannot make")

    # ---- CHECK 3: anchor to qou-ales step 6
    G_band = band(2, 3, h) + band_inv(3, 4, h)
    G_artin = [s_(2), sinv_(3, h)]
    dev = mp.mpf(0)
    for lam in deciding:
        sig, dim = blocks[lam]
        dev = max(dev, mp.norm(word_image(sig, dim, G_band) - word_image(sig, dim, G_artin)))
    check("a_(3,2) a_(4,3)^-1 == sigma_2 sigma_3^-1 on every deciding block",
          dev < TOL, f"max dev {mp.nstr(dev, 3)}  (anchors to qou-ales step 6)")

    # ---- CHECK 4-6: every band vertex
    print("\n[4-6] every band gamma-gamma vertex (bands sharing exactly one strand)")
    verts = []
    for b1, b2 in combinations(bands, 2):
        shared = set(b1) & set(b2)
        if len(shared) != 1:
            continue
        for a, b in ((b1, b2), (b2, b1)):
            word = band(*a, h) + band_inv(*b, h)
            spans = {BLOCK_OF[x] for x in set(a) | set(b)}
            verts.append({
                "name": f"a{a} a{b}^-1",
                "word": word,
                "inter": len(spans) > 1,
                "nonadj": not (a[1] == a[0] + 1 and b[1] == b[0] + 1),
                "artin_len": len(word),
            })
    print(f"    {len(verts)} vertices; {sum(v['inter'] for v in verts)} span both nucleon "
          f"blocks; {sum(v['nonadj'] for v in verts)} use a non-adjacent band")
    check("the vertex count is 120 (6 strands x C(5,2) pairs x 2 orderings)",
          len(verts) == 120, f"{len(verts)}")

    print(f"    evaluating {len(verts)} vertices x {KMAX} powers x {len(deciding)} blocks ...")
    for n, v in enumerate(verts):
        chis = {lam: [] for lam in deciding}
        feas = []
        mats = {}
        for lam in deciding:
            sig, dim = blocks[lam]
            mats[lam] = word_image(sig, dim, v["word"])
        cur = {lam: mp.eye(blocks[lam][1]) for lam in deciding}
        for k in range(1, KMAX + 1):
            ok = True
            for lam in deciding:
                cur[lam] = cur[lam] * mats[lam]
                c = trace(cur[lam], blocks[lam][1])
                chis[lam].append(c)
                if not (c >= -TOL):
                    ok = False
            if ok:
                feas.append(k)
        v["feasible"] = feas
        v["charvec"] = tuple(mp.nstr(chis[lam][0], 12) for lam in deciding)
        if (n + 1) % 30 == 0:
            print(f"      {n + 1}/{len(verts)}  elapsed {time.time() - t0:.1f}s")

    artin_v = next(v for v in verts if v["name"] == "a(2, 3) a(3, 4)^-1")
    print(f"\n    Artin interface vertex  {artin_v['name']}: feasible {artin_v['feasible']}")
    check("the Artin interface vertex is feasible iff 3 | k",
          artin_v["feasible"] == [3, 6, 9],
          f"{artin_v['feasible']}   (qou-ales step 6/7: interfaceSelected_three)")

    # ADVERSARIAL: equal characters must come from DISTINCT matrices, or the
    # word construction is broken and "all 120 agree" is a bug, not a finding.
    sig42, dim42 = blocks[(4, 2)]
    mat_sigs = {}
    for v in verts:
        M = word_image(sig42, dim42, v["word"])
        key = tuple(mp.nstr(M[i, j], 10) for i in range(dim42) for j in range(dim42))
        mat_sigs.setdefault(key, []).append(v["name"])
    check("the 120 vertices give MANY distinct matrices on block (4,2)",
          len(mat_sigs) > 1,
          f"{len(mat_sigs)} distinct matrices -- so equal characters are conjugacy, "
          "not a construction that collapsed every word to the same element")
    check("and their words are genuinely distinct",
          len({tuple((str(c), str(d), g) for c, d, g in v["word"]) for v in verts}) == 120,
          "120 distinct words")

    classes = {}
    for v in verts:
        classes.setdefault(v["charvec"], []).append(v["name"])
    print(f"\n    distinct character vectors among the {len(verts)} vertices: {len(classes)}")
    for cv, names in sorted(classes.items(), key=lambda kv: -len(kv[1])):
        print(f"      {len(names):>3} vertices  chi = {cv}")

    # ---- CHECK 7: the question
    print("\n[7] does any INTER-BLOCK band vertex select differently?")
    feas_sets = {}
    for v in verts:
        feas_sets.setdefault(tuple(v["feasible"]), []).append(v)
    print(f"    distinct feasible sets: {len(feas_sets)}")
    for fs, vs in sorted(feas_sets.items(), key=lambda kv: -len(kv[1])):
        n_inter = sum(x["inter"] for x in vs)
        print(f"      {len(vs):>3} vertices ({n_inter} inter-block)  feasible = {list(fs)}")
        if len(vs) <= 6:
            for x in vs:
                print(f"          {x['name']}")
    differing = [v for v in verts if v["feasible"] != artin_v["feasible"]]
    check("no band vertex has a feasible set differing from the Artin interface vertex's",
          not differing,
          f"{len(differing)} differ" if differing else "all 120 agree")
    minima = {min(v["feasible"]) for v in verts if v["feasible"]}
    check("the minimal non-trivial survivor is 3 for every band vertex",
          minima == {3}, f"minima observed: {sorted(minima)}")

    # cost, both ways
    inter_v = [v for v in verts if v["inter"] and v["feasible"]]
    best_artin = min(v["artin_len"] * min(v["feasible"]) for v in inter_v)
    check("under ARTIN cost the cheapest inter-block survivor is the Artin one",
          artin_v["artin_len"] * 3 == best_artin,
          f"cost {best_artin} = G^3's six letters; band cost ties all of them at 6")

    print(f"\n{'=' * 78}")
    print(f"{checks - len(failures)}/{checks} checks passed   wall {time.time() - t0:.1f}s")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    print("=" * 78)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
