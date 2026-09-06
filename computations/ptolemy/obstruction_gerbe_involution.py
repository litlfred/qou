#!/usr/bin/env python3
"""The obstruction classes of L6a4 are a Z/3-GERBE group, and snappy's list is its
quotient by the duality involution.  MEASURED here; the consequence is stated separately
because it rests on one step this script does NOT verify.

WHAT IS MEASURED (all four checks below, reproducibly):

  H^2(M, dM; Z/3) = (Z/3)^3 -- order 27, one factor per cusp, M having 3 cusps.
  snappy lists 14 obstruction classes, and they are exactly the ORBITS of c -> -c:
  one fixed point (the trivial class) plus 26/2 = 13 antipodal pairs.

  The evidence is that no nontrivial listed class has its negative also listed, and
  that the listed set together with its negatives is closed under addition mod 3 --
  so the union is a group, of order exactly 27.

WHY THIS MATTERS FOR THE Sym^2 GATE, and the step that is NOT verified here.

  The gate asks whether a boundary-unipotent PGL(3,C) representation can be Sym^2 of
  an SL(2) representation.  Any such Sym^2 is SELF-DUAL.  Now IF duality negates the
  obstruction class -- if the class of rho^* is -c, which is the expected behaviour
  since duality inverts the central mu_3 -- then a self-dual representation needs

      c = -c   =>   2c = 0   =>   c = 0,

  because 2 is invertible mod 3.  Only the TRIVIAL class could then carry a self-dual
  representation, and every class 1-13 would pass the Sym^2 gate STRUCTURALLY, with no
  Groebner basis at all.

  THAT CONDITIONAL IS THE WHOLE VALUE, AND ITS ANTECEDENT IS UNVERIFIED.  This script
  establishes the group and the involution; it does NOT establish that duality acts as
  c -> -c.  Do not report the consequence as a result until that step is proved or
  found in the literature (Garoufalidis-Thurston-Zickert is the place to look).

  One consistency check is available and it passes: class 1 was computed the expensive
  way and found to be COMPLEX TYPE, i.e. not self-dual -- exactly what the argument
  predicts for a class with c != 0.  That is corroboration, not proof: a single
  agreeing instance would also be produced by chance.
"""
import warnings
warnings.filterwarnings('ignore')
import snappy

N = 3


def classes(name='L6a4'):
    M = snappy.Manifold(name)
    V = [tuple(M.ptolemy_variety(N, obstruction_class=k, eliminate_fixed_ptolemys=True)
               ._obstruction_class.H2_class) for k in range(14)]
    return M, V


def neg(c):
    return tuple((-x) % N for x in c)


def add(a, b):
    return tuple((x + y) % N for x, y in zip(a, b))


def main():
    M, V = classes()
    trivial = V[0]
    checks = []

    checks.append(("all listed classes distinct", len(set(V)) == len(V), f"{len(set(V))} of {len(V)}"))

    self_neg = [k for k, c in enumerate(V) if c != trivial and neg(c) in V]
    checks.append(("no nontrivial class has its negative also listed", not self_neg,
                   "none" if not self_neg else f"classes {self_neg}"))

    closure = set(V) | {neg(c) for c in V}
    checks.append(("list union its negatives has order 27", len(closure) == 27, str(len(closure))))

    closed = all(add(a, b) in closure for a in closure for b in closure)
    checks.append(("that union is closed under addition mod 3", closed, "group" if closed else "NOT a group"))

    checks.append(("group order matches one Z/3 per cusp", len(closure) == N ** M.num_cusps(),
                   f"3^{M.num_cusps()} = {N ** M.num_cusps()}"))

    fixed = [c for c in closure if c == neg(c)]
    checks.append(("the involution has exactly one fixed point", len(fixed) == 1,
                   f"{len(fixed)} fixed"))

    for label, ok, detail in checks:
        print(f"  [{'ok' if ok else 'FAIL'}] {label}: {detail}")
    good = all(ok for _, ok, _ in checks)
    print(f"\n{'ALL CHECKS PASS' if good else 'CHECKS FAILED'} -- "
          f"H^2 = (Z/3)^{M.num_cusps()}, snappy's {len(V)} classes are its orbits under c -> -c")
    print("\nNOT ESTABLISHED HERE: that duality acts as c -> -c.  The Sym^2 consequence")
    print("is conditional on that step; see this file's docstring.")
    return 0 if good else 1


if __name__ == '__main__':
    raise SystemExit(main())
