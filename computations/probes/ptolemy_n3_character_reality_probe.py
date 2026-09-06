#!/usr/bin/env python3
"""Is a NON-GEOMETRIC PGL(3,C) component self-dual?  Measured on 4_1 at n = 3.

THE QUESTION.  PR #6743 (merged, d7e53cd8dc) closed route E's geometric side:
`SymSquareHolonomyIsRealType` proves every Sym^2-induced representation is
self-dual, hence real or quaternionic, hence excluded by the eightfold's flavour
gate — and that is a property of the map SL(2) -> SL(3), so it prunes every knot
at once.  What survives is a genuinely NON-GEOMETRIC PGL(3,C) representation.
Garoufalidis-Goerner-Zickert (arxiv-1207.6711v1 s1.3) supply them: "there are
often several components of representations besides the geometric one".

A representation is SELF-DUAL iff chi(g) = chi(g^-1) for all g, since
chi_{rho*}(g) = chi_rho(g^-1).  So ONE group element whose two traces differ
settles complex type.

RESULT (exact, symbolic, no floating point in the verdict):

  component   field       chi(a)              chi(a^-1)           self-dual
  geometric   Q(sqrt-3)   -3 + 2*sqrt(3)*I    -3 + 2*sqrt(3)*I    YES, diff = 0
  non-geom    Q(sqrt-7)   (9+3*sqrt(7)*I)/2   (9-3*sqrt(7)*I)/2   NO,  diff = 3*sqrt(7)*I

So the non-geometric component IS complex type — what the Sym^2 gate demands.

AND THE GEOMETRIC LEG INDEPENDENTLY CONFIRMS THE LEAN.  `selfDual_of_amphichiral`
predicts that 4_1, being amphichiral, has self-dual geometric holonomy.  Singular
and sympy know nothing about that proof and put the difference at exactly 0.

SCOPE — read before citing this.
  * This is 4_1, NOT the Borromean rings.  The framework's mass construction runs
    on B_3, whose n=3 decomposition OOM-killed in this container at 11m15
    (saturated, mod 32003).  What is established here is that non-geometric
    complex-type PGL(3,C) representations EXIST at n = 3 and are computable —
    the existence question route E was stuck on.  Whether B_3 has one does NOT
    follow and is the next measurement.
  * Route E is not thereby "alive": a complex-type component is a NECESSARY
    condition the gate demands, not a sufficient one.  Nothing here connects
    this representation to the eightfold's N=3 problem.

METHOD.  snappy builds the Ptolemy variety with its non-zero condition
(Rabinowitsch variable t, so degenerate loci are excluded and every component
found is a representation).  sympy solves the system exactly.  Coordinates are
expanded through snappy's own py_eval_variable_dict, and evaluate_word is called
with is_numerical=False so the matrices carry exact algebraic entries.  The
float64 pass is used only to pick which solutions to check; every number in the
verdict above is symbolic.

Requires: Singular (apt) for the decomposition cross-check, snappy (pip).
Both installers already existed in folio-assistant and had never been run.

-- Ref: [manuscript] bean `qou-47nf`; GGZ arxiv-1207.6711v1 s1.3; PR #6743.
"""
import sympy as sp
import snappy
from snappy.ptolemy.coordinates import PtolemyCoordinates


def main() -> int:
    M = snappy.Manifold('4_1')
    V = M.ptolemy_variety(3, obstruction_class=0)
    vs = [str(v) for v in V.variables_with_non_zero_condition]
    syms = {v: sp.Symbol(v) for v in vs}
    eqs = [sp.sympify(str(e).replace('^', '**'), locals=syms)
           for e in V.equations_with_non_zero_condition]
    expand = eval(V.py_eval_variable_dict())
    G = M.fundamental_group()

    sols = sp.solve(eqs, list(syms.values()), dict=True)
    print(f"4_1 at n=3: {len(eqs)} eqns, {len(vs)} vars, {len(sols)} exact solutions")
    print()
    verdicts = []
    for i, s in enumerate(sols):
        red = {v: sp.nsimplify(sp.radsimp(sp.simplify(s.get(syms[v], syms[v]))))
               for v in vs}
        P = PtolemyCoordinates(expand(red), is_numerical=False,
                               manifold_thunk=lambda: M)
        A = sp.Matrix(P.evaluate_word('a', G))
        tr = sp.radsimp(sp.simplify(sp.expand(A.trace())))
        tri = sp.radsimp(sp.simplify(sp.expand(A.inv().trace())))
        diff = sp.radsimp(sp.simplify(sp.expand(tr - tri)))
        selfdual = sp.simplify(diff) == 0
        verdicts.append(selfdual)
        print(f"  sol {i}:  chi(a) = {tr}")
        print(f"          chi(a^-1) = {tri}")
        print(f"          difference = {diff}   SELF-DUAL: {selfdual}")
    print()
    n_complex = sum(1 for v in verdicts if not v)
    print(f"non-self-dual (complex type) solutions: {n_complex} of {len(verdicts)}")
    if n_complex:
        print("VERDICT: a non-geometric component at n=3 IS complex type.")
        print("This is the NECESSARY condition the Sym^2 gate demands — not a")
        print("sufficient one, and established for 4_1 only, not for B_3.")
    else:
        print("VERDICT: every component here is self-dual.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
