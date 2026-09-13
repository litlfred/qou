#!/usr/bin/env python3
"""Cross-check: the equation-only recovery of the 6 eliminated coordinates against
snappy's own canonical_representative bookkeeping.  Two independent routes, same point.

WHY THIS MATTERS, and it corrects the framing of my own producer.
ptolemy_class1_full_assignment.py recovers the six coordinates that
eliminate_fixed_ptolemys drops, using ONLY the un-eliminated Ptolemy equations and the
26 recorded coordinates -- a triangular fixed point, no library bookkeeping consulted.
I initially presented that as supplying data the corpus did not have.  It is not:

    snappy already has these values, in V.canonical_representative[nm] = (sign, u-power,
    canonical variable or the literal 1),

and ptolemy_duality_sigma_coboundary_test.expand_point -- the function that builds the
128-coordinate point feeding the MERGED #7092 verdict (main f7fee734c3) -- reads exactly
that table.  So the six were never missing.

What IS new is that nothing was checking them.  expand_point is a load-bearing input to
a merged headline, and snappy's (sign, u-power) for a NON-TRIVIAL generalized obstruction
class is precisely the bookkeeping most likely to carry a convention error -- the
identifications it returns elsewhere are the UNTWISTED ones, carrying only +-1.  An
independent derivation from the equations is therefore worth exactly as much as a
verification of that input, and that is what this reports.

THE TEST.  For each of the 6, compare
    snappy:  sign * u^(power mod 3) * (canonical variable, or 1)
    derived: the value in L6a4-c1-ptolemy-FULL.json
exactly in K = Q[T]/(f).  Note u^3 = 1, so a NEGATIVE recorded power is taken mod 3
rather than inverted -- doing it any other way raises rather than answering.

Exact in K throughout.  No floats, no tolerances -- the two values are equal or not.
"""
import json
import re
import sys
import warnings

warnings.filterwarnings('ignore')
import sympy as sp
import snappy

T = sp.Symbol('T')
SRC = 'computations/ptolemy/L6a4-c1-ptolemy-in-K.json'
FULL = 'computations/ptolemy/L6a4-c1-ptolemy-FULL.json'


def main():
    d = json.load(open(SRC))
    full = json.load(open(FULL))
    f = sp.expand(sp.sympify(d['field']['min_poly'].replace('t', 'T')))
    red = lambda e: sp.expand(sp.rem(sp.expand(e), f, T))
    g = lambda s: sp.expand(sp.sympify(re.sub(r'\bt\b', 'T', s)))
    u = g(d['ptolemy']['u'])
    assert red(u ** 2 + u + 1) == 0, "u is not a primitive cube root of unity"

    M = snappy.Manifold(d['manifold'])
    V = M.ptolemy_variety(3, obstruction_class=d['obstruction_class'],
                          eliminate_fixed_ptolemys=True)
    V0 = M.ptolemy_variety(3, obstruction_class=d['obstruction_class'])
    elim = sorted(set(V0.variables) - set(V.variables))
    print(f"eliminated by eliminate_fixed_ptolemys: {len(elim)} -> {elim}", flush=True)

    def tag(x):
        if x == 1:
            return '1'
        if red(x - u) == 0:
            return 'u'
        if red(x - red(u * u)) == 0:
            return 'u^2'
        return 'NOT a cube root of unity'

    print(f"\n{'coordinate':14s} {'snappy canonical_representative':30s} "
          f"{'derived':8s} agree?")
    allok = True
    for nm in elim:
        s, p, var = V.canonical_representative[nm]
        up = red(u ** (p % 3))              # u^3 = 1; a negative power is p mod 3
        snap = red(sp.Integer(s) * up) if var == 1 else \
            red(sp.Integer(s) * up * g(d['ptolemy'][var]))
        mine = red(g(full['ptolemy'][nm]))
        ok = red(snap - mine) == 0
        allok &= ok
        print(f"{nm:14s} (s={s}, u^{p % 3}, var={str(var):8s}) -> {tag(snap):8s} "
              f"{tag(mine):8s} {'YES' if ok else 'NO'}", flush=True)

    if allok:
        print(f"\nALL {len(elim)}/{len(elim)} AGREE, the u^2 on c_0012_1 included.")
        print("So snappy's canonical_representative twisting for this non-trivial")
        print("obstruction class is INDEPENDENTLY VERIFIED from the Ptolemy equations")
        print("alone -- and with it expand_point, hence the 128-coordinate point that")
        print("the merged #7092 verdict is computed on.")
        print("\nScope: this class, this point.  It verifies the INPUT to that verdict;")
        print("it says nothing about the verdict's own kernel argument.")
        return 0
    print("\nDISAGREEMENT -- the two routes give different values.  Since the derived")
    print("route satisfies all 39 un-eliminated equations exactly, a disagreement")
    print("would implicate snappy's bookkeeping and therefore expand_point.")
    return 1


if __name__ == '__main__':
    sys.exit(main())
