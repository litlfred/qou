#!/usr/bin/env python3
"""The V=4 repair clears the vertex bound — and then fails D1-c's OWN bar-ray
stipulation, 0 of 128.

# Ref: .beans/qou-q9ih--d1-route-c-m1-construct-the-qw-reproducing-34-bar.md
# Ref: computations/qbeta/dt_d1c_hecke_block_vertex_bound_probe.py
# Ref: folio/quantum-observable-universe/lean/QOU/QBeta/QuiverMirrorAutomorphismExcluded.lean

THE PROPOSAL BEING TESTED. `dt_d1c_hecke_block_vertex_bound_probe` showed the
per-ray stable count is capped by the vertex count `V`, so D1-c's
one-vertex-per-block reading (`H_3` has three blocks, `V = 3`, ceiling 3) cannot
reach the datum's 4. It proposed a repair from the corpus's own decomposition
`total = irreducible + abelian` (4_1 = 2+1, 5_2 = 3+1, 3_1 = 1+1): take the
vertex set to be the three blocks TOGETHER WITH the abelian connection, `V = 4`,
which clears the bound exactly. This tests it.

THE TEST IS NOT "does some V=4 quiver hit (4,3)". That is already answered YES
by `dt_d1a_small_quiver_two_ray_scan_probe` (64 of 74 quivers hit it) and is
vacuous. The content is D1-c's OWN structure, which it stipulates in two places:

  * vertices are the `H_3` blocks, so the BAR involution acts on them as
    partition conjugation — `(3) <-> (1^3)`, fixing `(2,1)`; the abelian vertex
    is bar-fixed. That is the permutation `sigma = (0 2)`, and it is not a free
    choice: `bar chi^(3)(Delta) = chi^(1^3)(Delta)` is exact and
    convention-free (qou-cds1 entry 15, on main).
  * "rays from the bar involution on stability" — so the two rays are
    `theta` and `sigma . theta`.

RESULT — a clean dichotomy, and it closes the repair.

    bar-symmetric quivers on the 4 vertices                        128
      admit (4,3) on SIGMA-RELATED rays (theta, sigma.theta)         0
      admit (4,3) on ARBITRARY two rays                            128

Every one of the 128 can produce counts 4 and 3 somewhere (achievable counts run
`[1,2,3,4]`) — and NOT ONE can produce them on a bar-related ray pair. The
counts at `theta` and `sigma . theta` are forced EQUAL, because `sigma` is a
symmetry of the quiver and therefore carries its stable spectrum at one ray onto
the spectrum at the other.

So the repair clears the counting bound and fails the structure. To reach `(4,3)`
one must give up either

  (a) bar-symmetry of the quiver — but then `sigma` is not an automorphism, and
      "the bar involution on stability" has no compatible action to be; or
  (b) the rays being bar-related — which is D1-c's own stipulation.

THIS IS THE MEASURED FORM OF A THEOREM THE BEAN ALREADY HAS.
`QuiverMirrorAutomorphismExcluded` (sorry-free) proves that any COUNT-INVARIANT
mirror implementation — a quiver automorphism among them — forces every readable
pair amphichiral, so `(4,3)` is unreachable. What is new here is not the
statement but that it is now checked on THE SPECIFIC vertex set the repair
proposes, where it was not obvious that the same obstruction would survive: the
repair was designed to clear a DIFFERENT bound (the vertex count) and does.

A SECOND STRUCTURAL FACT, measured in passing. Only 25 of the 128 bar-symmetric
quivers are acyclic, and NONE of those 25 carries an arrow between the two
conjugate blocks. The reason is immediate once seen: `sigma`-invariance sends
`0 -> 2` to `2 -> 0`, a 2-cycle. **Bar-symmetry forbids arrows between conjugate
Wedderburn blocks in any acyclic quiver** — so a bar-symmetric acyclic model can
never couple `(3)` to `(1^3)` directly.

NOT CLAIMED. That no `(Q,W)` reproduces the datum — `W = 0` throughout and a
potential can only cut further. That D1-c is dead: what is closed is the
blocks-plus-abelian repair UNDER D1-c's own bar-ray stipulation. That the
per-ray equality is proved here — it is measured, and the cited Lean theorem is
the proof of the general statement. Nothing derives `A_omega`; the datum stays
certified-imported. Scope-(a), nothing wired, no fit.

NO FLOAT64: integer and exact `Fraction` arithmetic; no floating point enters.
"""
from __future__ import annotations

import collections
import itertools
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

from witness_base import WitnessBuilder  # noqa: E402

N = 4
# 0 = block (3),  1 = block (2,1),  2 = block (1^3),  3 = the abelian connection.
VERTICES = ["(3)", "(2,1)", "(1,1,1)", "abelian"]
SIGMA = (2, 1, 0, 3)          # bar = partition conjugation, abelian fixed
DMAX, TMAX = 3, 3
TARGET = (4, 3)               # 5_2 and 4_1


def tits(m, d):
    v = sum(x * x for x in d)
    for i in range(N):
        for j in range(N):
            if m[i][j]:
                v -= m[i][j] * d[i] * d[j]
    return v


def real_roots(m):
    return [d for d in itertools.product(range(DMAX + 1), repeat=N)
            if any(d) and tits(m, d) == 1]


def slope_counts(roots, rootset, theta):
    mu = {d: Fraction(sum(t * x for t, x in zip(theta, d)), sum(d)) for d in roots}
    tally = {}
    for d in roots:
        if all(not (e != d and all(a <= b for a, b in zip(e, d)) and mu[e] >= mu[d])
               for e in rootset):
            tally[mu[d]] = tally.get(mu[d], 0) + 1
    return tally


def acyclic(m):
    indeg = collections.Counter()
    for i in range(N):
        for j in range(N):
            if m[i][j]:
                indeg[j] += 1
    q = [v for v in range(N) if indeg[v] == 0]
    seen = 0
    while q:
        v = q.pop()
        seen += 1
        for j in range(N):
            if m[v][j]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
    return seen == N


def bar_symmetric_quivers():
    """Arrow matrices invariant under the vertex permutation SIGMA."""
    pairs = [(i, j) for i in range(N) for j in range(N) if i != j]
    orbits, seen = [], set()
    for p in pairs:
        if p in seen:
            continue
        orb = {p, (SIGMA[p[0]], SIGMA[p[1]])}
        seen |= orb
        orbits.append(sorted(orb))
    for vals in itertools.product((0, 1), repeat=len(orbits)):
        m = [[0] * N for _ in range(N)]
        for orb, v in zip(orbits, vals):
            for (i, j) in orb:
                m[i][j] = v
        yield m, len(orbits)


def main() -> int:
    w = WitnessBuilder("dt-d1c-v4-blocks-plus-abelian-bar-ray", engine="python-int")
    w.set_description(
        "The V=4 blocks-plus-abelian repair clears the vertex bound but fails "
        "D1-c's own bar-ray stipulation: 0 of 128 bar-symmetric quivers give "
        "(4,3) on sigma-related rays, while all 128 give it on arbitrary rays."
    )
    ok = []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    check("the_repair_vertex_set_has_FOUR_vertices",
          len(VERTICES) == 4 and max(TARGET) == 4,
          "(3 H_3 blocks + the abelian connection; clears the per-ray ceiling "
          "that excluded V=3)")
    check("bar_acts_as_partition_conjugation_and_is_NOT_a_free_choice",
          SIGMA[0] == 2 and SIGMA[2] == 0 and SIGMA[1] == 1 and SIGMA[3] == 3,
          "((3) <-> (1^3), (2,1) fixed, abelian fixed — qou-cds1 entry 15 proves "
          "bar chi^(3)(Delta) = chi^(1^3)(Delta), exact and convention-free)")

    hits_sigma, hits_any, total, n_acyclic, acyclic_with_conj = 0, 0, 0, 0, 0
    all_counts = set()
    for m, n_orb in bar_symmetric_quivers():
        total += 1
        if acyclic(m):
            n_acyclic += 1
            if m[0][2] or m[2][0]:
                acyclic_with_conj += 1
        roots = real_roots(m)
        if not roots:
            continue
        rootset = set(roots)
        thetas = [t for t in itertools.product(range(-TMAX, TMAX + 1), repeat=N)
                  if any(t)]
        counts, sigma_hit = set(), False
        for th in thetas:
            sc = slope_counts(roots, rootset, th)
            a = {v for v in sc.values() if v}
            counts |= a
            if not sigma_hit:
                sth = tuple(th[SIGMA[i]] for i in range(N))
                b = {v for v in slope_counts(roots, rootset, sth).values() if v}
                if (TARGET[0] in a and TARGET[1] in b) or \
                   (TARGET[1] in a and TARGET[0] in b):
                    sigma_hit = True
        all_counts |= counts
        if sigma_hit:
            hits_sigma += 1
        if set(TARGET) <= counts:
            hits_any += 1

    print(f"\n  bar-symmetric quivers on the 4 vertices : {total}")
    print(f"    admit (4,3) on SIGMA-RELATED rays      : {hits_sigma}")
    print(f"    admit (4,3) on ARBITRARY two rays      : {hits_any}")
    print(f"    achievable per-ray counts overall      : {sorted(all_counts)}")
    print(f"    acyclic                                 : {n_acyclic}")
    print(f"    acyclic WITH a (3)<->(1^3) arrow        : {acyclic_with_conj}")

    check("on_ARBITRARY_rays_every_bar_symmetric_quiver_reaches_the_target",
          hits_any == total,
          f"({hits_any}/{total}) — so the vertex bound really is cleared, and "
          "'does some V=4 quiver hit (4,3)' is vacuous")
    check("on_BAR_RELATED_rays_NOT_ONE_of_them_does",
          hits_sigma == 0,
          f"({hits_sigma}/{total}) — sigma is a symmetry of the quiver, so it "
          "carries the stable spectrum at theta onto the spectrum at "
          "sigma.theta and the counts are forced EQUAL")
    check("so_the_repair_fails_D1c_s_OWN_stipulation",
          hits_any == total and hits_sigma == 0,
          "(clears the counting bound, fails the structure — to reach (4,3) one "
          "must give up either bar-symmetry of the quiver or bar-relatedness of "
          "the rays, and the latter is D1-c's own words)")
    check("bar_symmetry_FORBIDS_arrows_between_the_conjugate_blocks_when_acyclic",
          acyclic_with_conj == 0 and n_acyclic > 0,
          f"({n_acyclic} acyclic, {acyclic_with_conj} of them with a (3)<->(1^3) "
          "arrow) — sigma-invariance sends 0->2 to 2->0, a 2-cycle")

    w.add_data("vertex_set", {"vertices": VERTICES, "V": N,
                              "sigma": list(SIGMA),
                              "sigma_meaning": "bar = partition conjugation on "
                                               "H_3 blocks; abelian fixed"})
    w.add_data("result", {
        "bar_symmetric_quivers": total,
        "hits_on_sigma_related_rays": hits_sigma,
        "hits_on_arbitrary_rays": hits_any,
        "achievable_per_ray_counts": sorted(all_counts),
        "verdict": "the V=4 repair CLEARS the vertex bound and FAILS D1-c's "
                   "bar-ray stipulation",
    })
    w.add_data("acyclicity", {
        "acyclic": n_acyclic, "of_total": total,
        "acyclic_with_conjugate_block_arrow": acyclic_with_conj,
        "statement": "bar-symmetry forbids arrows between conjugate Wedderburn "
                     "blocks in any acyclic quiver, since sigma-invariance turns "
                     "0->2 into a 2-cycle with 2->0",
    })
    w.add_data("relation_to_the_landed_Lean", {
        "theorem": "QuiverMirrorAutomorphismExcluded (sorry-free): any "
                   "count-invariant mirror implementation forces every readable "
                   "pair amphichiral, so (4,3) is unreachable",
        "what_is_new_here": "not the statement but that it is checked on THE "
                            "SPECIFIC vertex set the repair proposes — the "
                            "repair was designed to clear a DIFFERENT bound (the "
                            "vertex count) and does, so it was not obvious the "
                            "same obstruction would survive",
    })
    w.add_data("scope", {
        "tier": "scope-(a)", "wired": False, "is_a_fit": False,
        "potential": "W = 0; a potential can only cut further",
        "closes": "the blocks-plus-abelian repair UNDER D1-c's own bar-ray "
                  "stipulation — not D1-c the route, and not every (Q,W)",
        "per_ray_equality_is": "measured here; the cited Lean theorem proves the "
                               "general statement",
    })

    passed = sum(ok)
    print(f"\n  {passed}/{len(ok)} checks passed")
    w.save()
    return 0 if passed == len(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
