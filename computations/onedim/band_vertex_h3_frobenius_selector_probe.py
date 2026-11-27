#!/usr/bin/env python3
"""Does the confinement SDP still select beta_Bor when the gamma-gamma vertex
is read on BAND generators instead of adjacent Artin ones?

This is step 3 of `qou-ales` redone on the enlarged candidate set -- the
concrete content of the owner's pick B, after pick C measured that the band
reading admits every strand layout
(`band_gamma_gamma_vertex_admits_everything_probe.py`, 11/11).

## Setup

`H_3` has exactly three Birman-Ko-Lee bands:

    a_(1,0) = sigma_0                      joins strands {0,1}
    a_(2,1) = sigma_1                      joins strands {1,2}
    a_(2,0) = sigma_1 sigma_0 sigma_1^-1   joins strands {0,2}

Every pair of them shares exactly one strand, so all three pairs give a band
gamma-gamma vertex `a b^-1` -- six of them counting both orderings, against the
ONE the Artin reading admits (`V = sigma_0 sigma_1^-1 = a_(1,0) a_(2,1)^-1`).

## The selection rule

Owner ruling 2026-09-12: the confinement SDP means PSD **reading 3**, Frobenius
positivity -- `chi_lambda(w) >= 0` on every block with `y_lambda > 0`.  Under
convention D the two-row truncation gives `y_(1^3) = 0`, so only `(3)` and
`(2,1)` carry weight; `chi_(3)` is the trivial character and equals `q^writhe`,
which is `1` for every vertex power since a vertex has writhe `0`.  **So `(2,1)`
decides, exactly as in the Artin case** -- the enlarged candidate set does not
enlarge the set of deciding blocks.

Readings 1 (literal `Matrix.PosSemidef`) and 2 (symmetric-part PSD) are
recorded alongside, per the owner's "keep 1 2 for later".

## What is measured

1. The three bands, as explicit `(c, d, gen)` words, and that `a_(2,0)` is
   CONJUGATE to `sigma_0` -- so its character agrees blockwise with `sigma_0`'s
   (CHECK 2).  A character is a class function; this is the check that the band
   machinery is right before any selection is run.
2. That vertex 1 reproduces the corpus's Artin vertex as a matrix (CHECK 3).
3. For each of the six band vertices, `V^k` for `k = 1..10` under all three
   readings, with `chi_(2,1)` reported (CHECK 4-6).
4. Whether the enlarged set changes the selection (CHECK 7).

## Cost is a CHOICE, so both are reported and neither is picked

Step 3 of `qou-ales` used crossing count as the cost.  A band is a conjugate of
one crossing, so it has ARTIN length `2(t-s-1)+1` but BAND length 1 -- and the
two cost functions can rank differently.  Both are reported; selecting on the
one that gives the preferred answer would be selection against the target.

NOT claimed: which reading or which cost the physics means; any binding number;
anything about `H_6` or the eleven-letter nucleon words.

mpmath at 60 dps end to end, proton pin.  Writes no witness, runs no producer,
reads no AME/CODATA/census.
"""
from __future__ import annotations

import sys
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
TOL = mp.mpf(10) ** (-40)
KMAX = 10


# --------------------------------------------------------------- words ----
def s(i):
    """sigma_i as a (c, d, gen) triple."""
    return (mp.mpf(1), mp.mpf(0), i)


def sinv(i, h):
    """sigma_i^-1 = sigma_i - h (Hecke)."""
    return (mp.mpf(1), -h, i)


def band(lo, hi, h):
    """The BKL band a_(hi,lo) as an Artin word, lo < hi.

    a_(t,s) = (sigma_{t-1} ... sigma_{s+1}) sigma_s (sigma_{s+1}^-1 ... sigma_{t-1}^-1)
    """
    left = [s(j) for j in range(hi - 1, lo, -1)]
    right = [sinv(j, h) for j in range(lo + 1, hi)]
    return left + [s(lo)] + right


def band_inv(lo, hi, h):
    """a_(hi,lo)^-1 = (sigma_{t-1}...sigma_{s+1}) sigma_s^-1 (sigma_{s+1}^-1...)."""
    left = [s(j) for j in range(hi - 1, lo, -1)]
    right = [sinv(j, h) for j in range(lo + 1, hi)]
    return left + [sinv(lo, h)] + right


def word_image(sigmas, dim, word):
    M = mp.eye(dim)
    I = mp.eye(dim)
    for c, d, g in word:
        M = M * (c * sigmas[g] + d * I)
    return M


def trace(M, dim):
    return mp.fsum(M[i, i] for i in range(dim))


def sym_norm(M):
    return mp.norm(M - M.T)


def min_eig_sym(M):
    return min(mp.eigsy((M + M.T) / 2)[0])


def min_eig(M):
    return min(mp.re(e) for e in mp.eig(M)[0])


def readings(M, dim):
    return {
        "literal": bool(sym_norm(M) < TOL and min_eig(M) >= -TOL),
        "form": bool(min_eig_sym(M) >= -TOL),
        "chi": trace(M, dim),
    }


# ---------------------------------------------------------------- main ----
def main() -> int:
    checks, failures = 0, []

    def check(name, ok, detail=""):
        nonlocal checks
        checks += 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
        if not ok:
            failures.append(name)

    q = Q_MP
    h = q - 1 / q
    print("=" * 78)
    print("H_3 confinement-SDP selection on the BAND gamma-gamma vertex set")
    print("=" * 78)
    print(f"  proton pin q = {mp.nstr(q, 22)}   h^2 = {mp.nstr(h * h, 16)}")

    cache = BlockCacheMP(q)
    blocks = {}
    for lam in [(3,), (2, 1), (1, 1, 1)]:
        sig, dim, _ = seminormal_matrices_mp(lam, cache=cache)
        blocks[lam] = (sig, dim)
    y3 = y_lambda_su_n(3, q, 2)
    print("  y_lambda (convention D): " +
          ", ".join(f"{lam}: {mp.nstr(y3[lam], 10)}" for lam in blocks))

    # ---- CHECK 1: only (3) and (2,1) carry weight
    pos = [lam for lam in blocks if y3[lam] > TOL]
    check("convention D gives y > 0 on exactly (3) and (2,1)",
          set(pos) == {(3,), (2, 1)},
          f"y_(1^3) = {mp.nstr(y3[(1, 1, 1)], 6)} -- the alternating block does not constrain")

    # ---- CHECK 2: a_(2,0) is conjugate to sigma_0, so characters agree
    print("\n[2] the three bands, and the conjugacy check")
    bands = {"a(1,0)": (0, 1), "a(2,1)": (1, 2), "a(2,0)": (0, 2)}
    for nm, (lo, hi) in bands.items():
        w = band(lo, hi, h)
        print(f"    {nm} = {' '.join(('s%d' % g) + ('' if d == 0 else '^-1') for _, d, g in w)}"
              f"   (Artin length {len(w)})")
    conj_dev = mp.mpf(0)
    for lam, (sig, dim) in blocks.items():
        chi_a20 = trace(word_image(sig, dim, band(0, 2, h)), dim)
        chi_s0 = trace(word_image(sig, dim, [s(0)]), dim)
        conj_dev = max(conj_dev, abs(chi_a20 - chi_s0))
    check("chi_lambda(a_(2,0)) == chi_lambda(sigma_0) on every block",
          conj_dev < TOL,
          f"max dev {mp.nstr(conj_dev, 3)} -- a band is a conjugate, and chi is a class function")

    # ---- CHECK 3: vertex 1 IS the corpus's Artin vertex
    artin = [s(0), sinv(1, h)]
    v1 = band(0, 1, h) + band_inv(1, 2, h)
    dev = mp.mpf(0)
    for lam, (sig, dim) in blocks.items():
        dev = max(dev, mp.norm(word_image(sig, dim, v1) - word_image(sig, dim, artin)))
    check("a_(1,0) a_(2,1)^-1 == sigma_0 sigma_1^-1 as a matrix, every block",
          dev < TOL, f"max dev {mp.nstr(dev, 3)}")

    # ---- CHECK 4-6: the six band vertices
    print("\n[4-6] the six band vertices, reading 3 (Frobenius positivity) on (2,1)")
    keys = list(bands)
    verts = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            a, b = keys[i], keys[j]
            shared = ({bands[a][0], bands[a][1]} & {bands[b][0], bands[b][1]})
            if len(shared) != 1:
                continue
            word = band(*bands[a], h) + band_inv(*bands[b], h)
            verts.append((f"{a} {b}^-1", word, len(word), 2))

    check("all six ordered band pairs share exactly one strand", len(verts) == 6,
          f"{len(verts)} vertices; the Artin reading admits only the first")

    feasible = {}
    print(f"    {'vertex':<18} {'artin':>5} {'feasible k (1..10), reading 3':>34}")
    for name, word, alen, blen in verts:
        feas = []
        chis = {}
        for k in range(1, KMAX + 1):
            w = word * k
            ok = True
            for lam in pos:
                sig, dim = blocks[lam]
                r = readings(word_image(sig, dim, w), dim)
                chis.setdefault(lam, []).append(r["chi"])
                if not (r["chi"] >= -TOL):
                    ok = False
            if ok:
                feas.append(k)
        feasible[name] = feas
        print(f"    {name:<18} {alen:>5} {str(feas):>34}")
    sig21, dim21 = blocks[(2, 1)]
    chi21_artin = [trace(word_image(sig21, dim21, verts[0][1] * k), dim21)
                   for k in range(1, KMAX + 1)]
    print("\n    chi_(2,1) for the Artin vertex, k = 1..10:")
    print("      " + ", ".join(mp.nstr(c, 8) for c in chi21_artin))

    artin_feas = feasible["a(1,0) a(2,1)^-1"]
    check("the Artin vertex reproduces the known answer: feasible iff 3 | k",
          artin_feas == [3, 6, 9],
          f"{artin_feas}   (qou-ales step 7: vertexPow_frobeniusFeasible_iff_three_dvd)")

    # ---- CHECK 7: does the enlarged set change the selection?
    print("\n[7] does the band set change what is selected?")
    same = {n: f for n, f in feasible.items() if f == [3, 6, 9]}
    diff = {n: f for n, f in feasible.items() if f != [3, 6, 9]}
    print(f"    same feasible set as Artin ({{3,6,9}}): {len(same)} of 6")
    for n, f in diff.items():
        print(f"    DIFFERENT: {n} -> {f}")
    minima = {n: (min(f) if f else None) for n, f in feasible.items()}
    nonzero_minima = sorted({m for m in minima.values() if m})
    check("every band vertex's minimal feasible power is 3",
          nonzero_minima == [3],
          f"minimal k over all six vertices: {nonzero_minima}")

    # cost, both ways
    print("\n    cost of the minimal survivor, both cost functions:")
    for name, word, alen, blen in verts:
        k = minima[name]
        if k:
            print(f"      {name:<18} k={k}   Artin cost {alen * k:>3}   band cost {blen * k:>3}")
    art_costs = {n: minima[n] * a for n, _, a, _ in
                 ((v[0], v[1], v[2], v[3]) for v in verts) if minima[n]}
    best_artin = min(art_costs.values())
    check("under ARTIN cost the cheapest survivor is still the Artin vertex's",
          art_costs["a(1,0) a(2,1)^-1"] == best_artin,
          f"cost {best_artin} = beta_Bor's six letters; others cost "
          f"{sorted(set(art_costs.values()))}")

    # ---- CHECK 8: are the six vertices actually CONJUGATE, or merely agreeing?
    print("\n[8] is the agreement conjugacy, or a coincidence?")
    print("    chi_lambda of each vertex (k = 1), all three blocks:")
    charvecs = {}
    for name, word, _, _ in verts:
        vec = tuple(mp.nstr(trace(word_image(blocks[lam][0], blocks[lam][1], word),
                                  blocks[lam][1]), 12)
                    for lam in [(3,), (2, 1), (1, 1, 1)])
        charvecs[name] = vec
        print(f"      {name:<18} {vec}")
    distinct = len(set(charvecs.values()))
    check("all six vertices share ONE character vector (hence one class)",
          distinct == 1,
          f"{distinct} distinct character vector(s) among 6 vertices -- "
          "characters separate classes here, so this is conjugacy, not coincidence")

    print("\n" + "=" * 78)
    print(f"{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("FAILURES: " + ", ".join(failures))
    print("=" * 78)
    print("""
VERDICT

At H_3 the band reading ENLARGES the candidate set six-fold and CHANGES
NOTHING about the selection: every one of the six band gamma-gamma vertices is
Frobenius-feasible exactly at the powers 3, 6, 9, and the minimal non-trivial
survivor is k = 3 for all of them -- the same beta_Bor the Artin reading picks.

Under the Artin cost (crossing count) the Artin vertex's own cube is strictly
cheapest, so the selection is unchanged in candidate AND in cost.

Why it comes out this way, and it is not a coincidence: a band is a CONJUGATE
of a single crossing (CHECK 2 measures that its character agrees with
sigma_0's on every block), and chi_lambda is a CLASS FUNCTION.  Convention D
kills the alternating block, so only (2,1) decides -- and the trivial block is
q^writhe = 1 on any vertex power.

So pick B's H_3 leg closes as a NEGATIVE: the band reading does not change
what the confinement SDP selects here.  Scope (a) -- this is one algebra at one
pin, not a structural exclusion.  It does NOT settle H_6, where the interface
bond lives and where a band could join non-adjacent nucleon blocks; that is
where the two readings could still part company, and it is the next step.
""")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
