#!/usr/bin/env python3
"""Orbits of the icosahedral action on the admissible chirality units `u` (bean qou-wqto).

Preregistration (fixed BEFORE this ran):
    docs/audits/2026-11-15-bring-s5-distinguished-unit-preregistration.md

Under the labelled ASSUMPTION (H-ico) that A5 acts on the model cone
`BringCone = Quaternion` by left multiplication by the binary icosahedral group 2I,
`QOU/BringConeIcosahedral.lean :: leftMul_conj_chiralGammaU` shows the induced action on
the admissible units `u` (pure unit quaternions, a 2-sphere) is conjugation u -> g u g*.
This probe computes, in EXACT arithmetic over Q(sqrt5) (pairs of Fractions, no float):

  * 2I as the closure of two explicit icosians; |2I| = 120, image in SO(3) = 60;
  * that i and j lie in 2I (the Lean R0 lemma uses them);
  * rule R0: points of S^2 fixed by every rotation;
  * rules R1-R3: the directions with nontrivial stabiliser (rotation axes), their orbits,
    stabiliser orders;
  * the preregistered antipode test: is -u in the A5-orbit of u?
  * that the Galois-conjugate embedding (sqrt5 -> -sqrt5) has a different character, so
    the two icosahedral 3-dim representations are inequivalent.

No selection rule here is chosen by anything chirality, Q_beta or mass related; the
script reads no data. Exit status 1 on any failed check.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F


# ---- Q(sqrt5): x = (a, b) means a + b*sqrt5 -------------------------------------------
def kadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def kneg(x):
    return (-x[0], -x[1])


def kmul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def kgal(x):
    return (x[0], -x[1])


def ksign(x):
    """Exact sign of a + b*sqrt5."""
    a, b = x
    if b == 0:
        return (a > 0) - (a < 0)
    if a == 0:
        return (b > 0) - (b < 0)
    if (a > 0) == (b > 0):
        return 1 if a > 0 else -1
    # opposite signs: compare a^2 with 5 b^2
    if a * a > 5 * b * b:
        return 1 if a > 0 else -1
    if a * a < 5 * b * b:
        return 1 if b > 0 else -1
    return 0


ZERO = (F(0), F(0))
ONE = (F(1), F(0))
HALF = (F(1, 2), F(0))
PHI = (F(1, 2), F(1, 2))          # (1 + sqrt5)/2
PHI_INV = (F(-1, 2), F(1, 2))     # phi - 1


# ---- quaternions over Q(sqrt5): (re, i, j, k) ------------------------------------------
def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    s = lambda *xs: _sum(xs)
    return (
        s(kmul(a1, a2), kneg(kmul(b1, b2)), kneg(kmul(c1, c2)), kneg(kmul(d1, d2))),
        s(kmul(a1, b2), kmul(b1, a2), kmul(c1, d2), kneg(kmul(d1, c2))),
        s(kmul(a1, c2), kneg(kmul(b1, d2)), kmul(c1, a2), kmul(d1, b2)),
        s(kmul(a1, d2), kmul(b1, c2), kneg(kmul(c1, b2)), kmul(d1, a2)),
    )


def _sum(xs):
    r = ZERO
    for x in xs:
        r = kadd(r, x)
    return r


def qstar(p):
    return (p[0], kneg(p[1]), kneg(p[2]), kneg(p[3]))


def qneg(p):
    return tuple(kneg(x) for x in p)


def qnorm(p):
    return _sum(kmul(x, x) for x in p)


def qgal(p):
    return tuple(kgal(x) for x in p)


def conj(g, v):
    return qmul(qmul(g, v), qstar(g))


def closure(gens):
    elems = {(ONE, ZERO, ZERO, ZERO)}
    frontier = list(elems)
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = qmul(x, g)
                if y not in elems:
                    elems.add(y)
                    nxt.append(y)
        frontier = nxt
    return elems


def same_ray(v, w):
    """v = lam * w with lam > 0, for pure quaternions (exact)."""
    a = v[1:]
    b = w[1:]
    cross = (
        kadd(kmul(a[1], b[2]), kneg(kmul(a[2], b[1]))),
        kadd(kmul(a[2], b[0]), kneg(kmul(a[0], b[2]))),
        kadd(kmul(a[0], b[1]), kneg(kmul(a[1], b[0]))),
    )
    dot = _sum(kmul(x, y) for x, y in zip(a, b))
    return all(c == ZERO for c in cross) and ksign(dot) > 0


def main() -> int:
    fails = []

    def check(name, ok, detail=""):
        print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    s = (HALF, HALF, HALF, HALF)                          # (1+i+j+k)/2
    t = (kmul(HALF, PHI), kmul(HALF, PHI_INV), HALF, ZERO)  # (phi + phi^-1 i + j)/2
    check("generators are unit icosians", qnorm(s) == ONE and qnorm(t) == ONE)

    G = closure([s, t])
    check("|2I| = 120", len(G) == 120, f"got {len(G)}")
    qi = (ZERO, ONE, ZERO, ZERO)
    qj = (ZERO, ZERO, ONE, ZERO)
    check("i, j in 2I", qi in G and qj in G)

    # rotations: g ~ -g
    rots = []
    seen = set()
    for g in G:
        if g in seen:
            continue
        seen.add(g)
        seen.add(qneg(g))
        rots.append(g)
    check("|image in SO(3)| = 60", len(rots) == 60, f"got {len(rots)}")

    # R0: global fixed points. A fixed direction would be fixed by conj by i and j;
    # verified symbolically in Lean; here: intersect the fixed lines of all rotations.
    nontriv = [g for g in rots if g[1:] != (ZERO, ZERO, ZERO)]  # drop the identity (+1 or -1)
    axes = []
    for g in nontriv:
        v = (ZERO,) + g[1:]
        for w in (v, qneg(v)):
            if not any(same_ray(w, a) for a in axes):
                axes.append(w)
    common = [a for a in axes if all(same_ray(conj(g, a), a) for g in rots)]
    check("R0: no direction fixed by all 60 rotations", len(common) == 0,
          f"{len(common)} common fixed directions")

    # orbits of the axis directions (points with nontrivial stabiliser)
    remaining = list(axes)
    orbits = []
    while remaining:
        a = remaining.pop()
        orb = [a]
        for g in rots:
            b = conj(g, a)
            if not any(same_ray(b, c) for c in orb):
                orb.append(b)
        remaining = [r for r in remaining if not any(same_ray(r, c) for c in orb)]
        orbits.append(orb)

    summary = []
    for orb in orbits:
        a = orb[0]
        stab = sum(1 for g in rots if same_ray(conj(g, a), a))
        neg_in_orbit = any(same_ray(qneg(a), c) for c in orb)
        flippers = sum(1 for g in rots if same_ray(conj(g, a), qneg(a)))
        summary.append((len(orb), stab, neg_in_orbit, flippers))
    summary.sort()
    for size, stab, neg, fl in summary:
        print(f"  orbit size {size:2d}  stabiliser {stab}  axes {size // 2:2d}  "
              f"-u in orbit: {neg}  rotations u->-u: {fl}")
    check("exceptional orbits are 12/20/30 with stabilisers 5/3/2",
          [(o[0], o[1]) for o in summary] == [(12, 5), (20, 3), (30, 2)], str(summary))
    check("every exceptional orbit is closed under u -> -u by an A5 rotation",
          all(o[2] and o[3] > 0 for o in summary))
    check("R1/R3: unique orbit of maximal stabiliser = 12 vertex directions",
          [o[0] for o in summary if o[1] == max(x[1] for x in summary)] == [12])
    check("orbit-stabiliser", all(o[0] * o[1] == 60 for o in summary))

    # Galois conjugate embedding: character chi(g) = trace = 4 re(g)^2 - 1
    def chi(g):
        return kadd(kmul((F(4), F(0)), kmul(g[0], g[0])), kneg(ONE))
    chars = {chi(g) for g in rots}
    gal_chars = {chi(qgal(g)) for g in rots}
    irr = [c for c in chars if c[1] != 0]
    check("character has irrational values (order-5 classes)", len(irr) > 0, str(sorted(irr)))
    Gg = closure([qgal(s), qgal(t)])
    check("Galois-conjugate generators also give a group of order 120", len(Gg) == 120)
    # inequivalence: on the same abstract element (g and its Galois image correspond),
    # chi(sigma g) = sigma(chi(g)) != chi(g) when chi(g) is irrational.
    differs = any(chi(qgal(g)) != chi(g) for g in rots)
    check("the two embeddings have different characters on corresponding elements", differs)
    print(f"character values (embedding): {sorted(chars)}")
    print(f"character values (conjugate): {sorted(gal_chars)}")

    print("FAILED:" if fails else "ALL CHECKS PASS", fails if fails else "")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
