"""aomega_m3_pretzel_remainder_from_ptolemy_probe.py

Route C, milestone M3 (qou-m3ad Part 4 -> Part 6): the THIRD knot's H_floor inputs
derived in-sandbox.  qou-m3ad Part 4 transcribed Garoufalidis-Zagier §2.1 for the
(-2,3,7) pretzel knot: P_K has seven elements -- the trivial representation, three
from the trace field Q(xi) (disc -23, shared with 5_2) and three from the totally
real cubic Q(eta), eta^3 + eta^2 - 2 eta - 1 = 0 (disc 49) -- so |P_K| = 7,
real embeddings 4, one complex pair, H_floor remainder 4.  The bean's NEXT STEP
said the pretzel count is "a PREDICTION, not a check" and that the ptolemy
database is firewalled (403).  It is, but the ptolemy VARIETY is tiny and can be
solved here:

  SnapPy 3.3.2: Manifold('m016') = K12n242 = (-2,3,7) = Culler's K3_1, 3 tetrahedra.
  M.ptolemy_variety(2, obstruction_class='all') -> 2 obstruction classes, each
  3 Ptolemy variables and 4 equations.  sympy Groebner (lex) reduces each to a
  single cubic in one coordinate:
    class 1:  c^3 - c - 1 = 0          (disc -23)   <- Q(xi), the 5_2 field
    class 0:  c^3 + 4c^2 + 3c - 1 = 0  (disc  49)   <- totally real; Q(eta)
  (the c = 0 factor is excluded: Ptolemy coordinates are nonzero).

Boundary-unipotent SL(2,C) representations of a knot complement are exactly the
nontrivial elements of GZ's P_K (the boundary-parabolic ones), one per solution of
the Ptolemy varieties over all obstruction classes.  So the counts, the fields and
the signatures are DERIVED here from a held triangulation plus exact algebra, and
the H_floor rule is checked on its third knot rather than assumed.  Cross-checks:
Culler's census A_{K3_1} (library/A_census.tgz) has geometric L-degree 6, so R1's
full count is 7; the class-0 cubic is Q(eta) up to the substitution recorded below;
the class-1 cubic is the derived 5_2 shape cubic in -c.

Exact throughout (sympy over Q; Sturm counts for the real roots).  Audit-only,
scope-(a).  What this does NOT do: it does not give the pretzel's q->0 Stokes
matrix (no held source has it; GGM 2012.00062 note its level is 2), so the
one-sided H_Ad test of qou-m3ad item 1 is still not runnable; and it does not
separate H_Ad from H_floor (core 3 under both).
"""
from __future__ import annotations

import json
import os
import sys
import tarfile
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))
CENSUS = os.path.join(ROOT, "library", "A_census.tgz")


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    import snappy
    x = sp.symbols("x")
    M = snappy.Manifold("m016")
    ident = [str(s) for s in M.identify()]
    print(f"[0] SnapPy {snappy.__version__}: m016 -> {ident}, {M.num_tetrahedra()} tetrahedra")
    check("m016-is-K12n242-and-K3_1", any(s.startswith("K12n242") for s in ident)
          and any(s.startswith("K3_1") for s in ident), identify=ident)

    Vs = M.ptolemy_variety(2, obstruction_class="all")
    print(f"[1] ptolemy varieties N=2: {len(Vs)} obstruction classes")
    components = []
    for i, v in enumerate(Vs):
        names = [str(n) for n in v.variables]
        syms = sp.symbols(names)
        loc = dict(zip(names, syms))
        eqs = [sp.sympify(str(e).replace("^", "**"), locals=loc) for e in v.equations]
        G = sp.groebner(eqs, *syms, order="lex")
        last = G.exprs[-1]
        # strip the c = 0 factor (Ptolemy coordinates are nonzero)
        fac = [f for f, m in sp.factor_list(last)[1] if sp.Poly(f, syms[-1]).degree() > 1]
        assert len(fac) == 1, fac
        cubic = sp.Poly(fac[0], syms[-1])
        cub = sp.Poly(cubic.as_expr().subs(syms[-1], x), x)
        r1 = len(sp.real_roots(cub))
        r2 = (cub.degree() - r1) // 2
        disc = int(sp.discriminant(cub.as_expr(), x))
        print(f"    class {i}: vars {names}; Groebner -> {cub.as_expr()} = 0, disc {disc}, "
              f"irreducible {cub.is_irreducible}, real roots {r1}, complex pairs {r2}")
        components.append(dict(cls=i, cubic=str(cub.as_expr()), disc=disc, r1=r1, r2=r2,
                               degree=cub.degree(), irreducible=bool(cub.is_irreducible)))
    check("two-components-both-irreducible-cubics",
          len(components) == 2 and all(c["degree"] == 3 and c["irreducible"] for c in components))
    discs = sorted(c["disc"] for c in components)
    check("discriminants-are-minus23-and-49 (Q(xi) and Q(eta) of GZ §2.1)", discs == [-23, 49], discs=discs)

    # identify the fields with GZ's generators
    geo = [c for c in components if c["disc"] == -23][0]
    real = [c for c in components if c["disc"] == 49][0]
    theta = sp.Poly(sp.sympify(geo["cubic"]).subs(x, -x), x)   # c = -theta
    check("disc-minus23-component-is-the-derived-5_2-shape-cubic-in-minus-c",
          sp.expand(theta.as_expr() - (x**3 - x + 1)) == 0 or sp.expand(theta.as_expr() + (x**3 - x + 1)) == 0,
          cubic=geo["cubic"])
    eta_poly = x**3 + x**2 - 2 * x - 1
    # Q(eta) = Q(2cos(2pi/7)); the class-0 cubic generates the same field iff its roots are in Q(eta):
    # test by factoring the class-0 cubic over Q(eta).
    K = sp.QQ.algebraic_field(sp.CRootOf(eta_poly, 0))
    f0 = sp.Poly(sp.sympify(real["cubic"]), x, domain=K)
    splits = all(g.degree() == 1 for g, _ in f0.factor_list()[1])
    check("disc-49-component-splits-over-Q(eta), eta^3+eta^2-2eta-1=0 (GZ's field)", splits,
          cubic=real["cubic"], factors=str(f0.factor_list()))

    n_nonabelian = sum(c["degree"] for c in components)
    r1_tot = sum(c["r1"] for c in components)
    r2_tot = sum(c["r2"] for c in components)
    pk = 1 + n_nonabelian
    remainder = pk - 3
    print(f"[2] |P_K| = 1 + {n_nonabelian} = {pk}; real embeddings {r1_tot}, complex pairs {r2_tot}; "
          f"H_floor remainder |P_K| - 3 = {remainder}")
    check("pk-size-seven", pk == 7)
    check("real-embeddings-four-complex-pairs-one (AdjointIndexSetM3.realEmbeddings / complexPairs pretzel237)",
          r1_tot == 4 and r2_tot == 1)
    check("floor-remainder-four-equals-real-plus-2(pairs-1)", remainder == 4 and remainder == r1_tot + 2 * (r2_tot - 1))

    # Culler's A-polynomial: geometric L-degree 6 -> R1 count 7
    L, Mv = sp.symbols("L M")
    with tarfile.open(CENSUS) as tf:
        txt = tf.extractfile("apolys/K3_1.apoly").read().decode()
    body = txt.split(":=", 1)[1].strip().rstrip(";").replace("^", "**")
    A = sp.expand(sp.sympify(body, locals={"L": L, "M": Mv}))
    ldeg = sp.Poly(A, L).degree()
    irr = len(sp.factor_list(A)[1]) == 1
    print(f"[3] Culler A_{{K3_1}}: geometric L-degree {ldeg}, irreducible over Q: {irr}; "
          f"A(L,1) = {sp.factor(A.subs(Mv, 1))}")
    check("culler-K3_1-L-degree-6-so-R1-count-7-matches-|P_K|", ldeg == 6 and ldeg + 1 == pk)
    check("culler-K3_1-irreducible-one-curve-carries-both-fields", irr)

    verdict = (
        "The (-2,3,7) pretzel's H_floor inputs are DERIVED in-sandbox: SnapPy's census m016 "
        "(= K12n242 = K3_1) has two N=2 ptolemy obstruction classes whose Groebner bases are the "
        "cubics c^3-c-1 (disc -23, the 5_2 field Q(xi), one real root) and c^3+4c^2+3c-1 (disc 49, "
        "splits over Q(eta), three real roots). So |P_K| = 7, real embeddings 4, one complex pair, "
        "remainder 4 -- GZ §2.1's table reproduced from a held triangulation and exact algebra, and "
        "R1's count 7 confirmed by Culler's L-degree 6. Part 4's 'prediction 7' is now a check. "
        "Not separated: H_Ad vs H_floor (core 3 under both). Not obtained: the pretzel's q->0 "
        "Stokes matrix (level 2 per GGM; no held source), so qou-m3ad item 1 stays open."
    )
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    witness = {
        "name": "aomega-m3-pretzel-remainder-from-ptolemy",
        "description": "H_floor's inputs for the (-2,3,7) pretzel derived from SnapPy's m016 ptolemy "
                       "varieties (sympy Groebner): |P_K| = 7, real embeddings 4, remainder 4.",
        "computation": "aomega-m3-pretzel-remainder-from-ptolemy",
        "engine": "python+snappy+sympy",
        "scriptFile": os.path.basename(__file__),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "durationMs": int((time.time() - t0) * 1000),
        "auditOnly": True,
        "auditDoc": "docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md",
        "parameters": {"snappy_version": snappy.__version__, "manifold": "m016", "N": 2,
                       "census_tarball": "library/A_census.tgz"},
        "data": {"components": components, "pk_size": pk, "real_embeddings": r1_tot,
                 "complex_pairs": r2_tot, "floor_remainder": remainder,
                 "culler_K3_1_L_degree": ldeg, "culler_K3_1_irreducible": irr},
        "verdict": verdict,
        "assertions": assertions,
    }
    _WB.stamp_staleness_metadata(witness, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pretzel-remainder-from-ptolemy.witness.json")
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
