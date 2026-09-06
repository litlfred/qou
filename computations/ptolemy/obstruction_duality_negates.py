#!/usr/bin/env python3
"""Duality NEGATES the Ptolemy obstruction class -- derived, not cited -- and that
retires the Sym^2 gate for every nontrivial class of L6a4 without any Groebner basis.

THE DERIVATION (elementary; this is why no further paper was needed).

Let rho : Gamma -> PGL(n,C), and choose set-theoretic lifts rho~(g) in SL(n,C).  The
obstruction 2-cocycle is defined by

    rho~(g) rho~(h) = c(g,h) . rho~(gh),        c(g,h) in mu_n,

and its class [c] in H^2(Gamma; Z/n) is the obstruction to lifting rho to SL(n,C).

The dual representation is rho*(g) = rho(g)^{-T}.  Take rho~*(g) := rho~(g)^{-T}, which
is a legitimate lift since det(A^{-T}) = 1/det(A) = 1.  Then, using (AB)^T = B^T A^T,

    rho~*(g) rho~*(h) = (rho~(g)^{-1})^T (rho~(h)^{-1})^T
                      = ( rho~(h)^{-1} rho~(g)^{-1} )^T
                      = ( (rho~(g) rho~(h))^{-1} )^T
                      = ( c(g,h) rho~(gh) )^{-T}
                      = c(g,h)^{-1} . rho~*(gh)

since c(g,h) is a scalar.  Hence c* = c^{-1}, i.e.

    [rho*] = -[rho]   in H^2(Gamma; Z/n).                                    (*)

THE CONSEQUENCE.  Any Sym^2 of an SL(2,C) representation is SELF-DUAL (SL(2) reps are
symplectic, so Sym^2 is orthogonal).  The obstruction class is invariant under
conjugation, so rho isomorphic to rho* forces [rho] = [rho*], which with (*) gives

    c = -c   =>   2c = 0   =>   c = 0        (2 is invertible mod 3).

So at N = 3 ONLY THE TRIVIAL CLASS can carry a self-dual representation, and every
nontrivial class is barred from containing a Sym^2 -- structurally, with no Groebner
basis, no RUR, and no round trip.

For L6a4 that is classes 1 through 13: the whole remaining sweep, retired for the
purpose of the Sym^2 gate.

THREE CAVEATS, STATED BECAUSE THEY ARE WHERE THIS COULD FAIL.

  1. RELATIVE vs ABSOLUTE.  The derivation above is for group cohomology
     H^2(Gamma; mu_n).  The Ptolemy obstruction is the decorated / relative class in
     H^2(M, dM; Z/n).  The argument is expected to carry over -- duality acts the same
     way on the boundary data -- but this script does NOT prove the relative statement,
     and that is the one gap between this and a theorem.
  2. BOUNDARY-UNIPOTENCE is preserved: the inverse-transpose of a unipotent is
     unipotent, so rho* is again boundary-unipotent and lands in the same Ptolemy setting.
  3. WHAT IT DOES NOT SAY.  It bars Sym^2 and every other self-dual form.  It says
     NOTHING about whether a nontrivial class is non-empty, what its dimension or degree
     is, or whether its representations are irreducible.  Those still need the compute.

CONSISTENCY, measured: class 1 was computed the expensive way and found COMPLEX TYPE,
i.e. not self-dual -- exactly what (*) predicts for c != 0.  One agreeing instance is
corroboration, not proof of the general claim.
"""
import warnings
warnings.filterwarnings('ignore')
import snappy

N = 3


def main():
    M = snappy.Manifold('L6a4')
    V = [tuple(M.ptolemy_variety(N, obstruction_class=k, eliminate_fixed_ptolemys=True)
               ._obstruction_class.H2_class) for k in range(14)]
    neg = lambda c: tuple((-x) % N for x in c)

    fixed = [k for k, c in enumerate(V) if c == neg(c)]
    trivial = [k for k, c in enumerate(V) if all(x == 0 for x in c)]

    checks = [
        ("exactly one class is fixed by c -> -c", len(fixed) == 1, f"class {fixed}"),
        ("that fixed class is the trivial one", fixed == trivial, f"fixed={fixed} trivial={trivial}"),
        ("so 13 of 14 classes are barred from self-duality",
         len([k for k in range(14) if k not in fixed]) == 13,
         f"{len([k for k in range(14) if k not in fixed])} barred"),
    ]
    for label, ok, detail in checks:
        print(f"  [{'ok' if ok else 'FAIL'}] {label}: {detail}")

    good = all(ok for _, ok, _ in checks)
    print(f"\n{'ALL CHECKS PASS' if good else 'CHECKS FAILED'}")
    print("CONCLUSION (modulo caveat 1, the relative-cohomology step):")
    print("  L6a4 obstruction classes 1-13 cannot carry a self-dual representation,")
    print("  hence cannot contain Sym^2 of an SL(2,C) representation.  The Sym^2 gate")
    print("  passes for all of them with NO Groebner computation.")
    print("  It says nothing about their non-emptiness, dimension or degree.")
    return 0 if good else 1


if __name__ == '__main__':
    raise SystemExit(main())
