#!/usr/bin/env python3
"""Extract an EXACT Ptolemy point for any (manifold, obstruction class). (qou-qjhc)

The duality arc -- sigma_b(rho) conjugate to rho^{-T} in GL(3,K), untwisted, at every point
of the L6a4 class-1 variety -- runs on ONE manifold because only one exact point existed in
the repo.  ptolemy_second_manifold_cost.py measured why that was never the real obstacle:
the class-2 wall is a VARIABLE-COUNT wall (27 vs 7), and small manifolds solve in about a
second.  This producer is the missing piece -- it turns (manifold, class) into an exact
point in a number field, in the same shape as L6a4-c1-ptolemy-in-K.json.

THE METHOD.  Take snappy's Ptolemy equations; adjoin `T - (linear form in the variables)`
for a primitive element T; eliminate the variables to get T's eliminant; factor it.  Each
irreducible factor is ONE Galois-conjugacy class of points.  For each, pin the component by
adjoining that factor, take a LEX Groebner basis with T SMALLEST, and read every coordinate
off as `reduce(v, G)` -- its normal form, a polynomial in T alone.  That is exactly the
shape the arc's probes consume.

TWO TRAPS, BOTH MEASURED ON m004 CLASS 1 RATHER THAN ANTICIPATED:

  1. THE RAW IDEAL HAS DEGENERATE COMPONENTS.  Ptolemy coordinates must be NON-ZERO to
     define a representation, and snappy's equations as handed over do not saturate the
     zero locus away.  m004 class 1 splits into two components of degree 2, and one of them
     has SIX OF SEVEN COORDINATES EQUAL TO ZERO.  It is not a representation, it satisfies
     every equation, and it even carries a valid cube root of unity (u = T/7 with
     u^2+u+1 = 0) -- so `u` being correct is NOT evidence a component is genuine.  A
     component with any zero coordinate is discarded here, and the count is reported rather
     than silently dropped.
  2. THE ELIMINANT IS NOT THE FIELD.  Its degree is the total degree of the scheme, which
     is the sum over components.  Reading it as `[K:Q]` overstates the field whenever there
     is more than one component -- m004's eliminant is degree 4 while its genuine field is
     degree 2.

VALIDATION, before anything is written: every coordinate non-zero; `u^2 + u + 1 = 0` modulo
the minimal polynomial; and the minimal polynomial irreducible over Q.  The relator gate --
that the matrices really form a PGL(3) representation -- is left to the consumer, which
runs it against snappy's own evaluator rather than against this file's arithmetic.

Exact throughout: Singular over Q for elimination and normal forms, sympy for
factorisation.  No floats.
"""
import argparse
import json
import pathlib
import subprocess
import tempfile
import warnings

import sympy as sp

warnings.filterwarnings('ignore')
import snappy  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
T = sp.Symbol('T')
t = sp.Symbol('t')


def sing(script, timeout=900):
    """Run Singular; the scratch file goes to a temp dir, never into the repo."""
    with tempfile.TemporaryDirectory() as td:
        p = pathlib.Path(td) / 's.sing'
        p.write_text(script)
        r = subprocess.run(['Singular', '-q', '--no-warn', str(p)],
                           capture_output=True, text=True, timeout=timeout)
        return r.stdout


def extract(name, cls, verbose=True):
    M = snappy.Manifold(name)
    V = M.ptolemy_variety(3, obstruction_class=cls, eliminate_fixed_ptolemys=True)
    eqs = [str(e) for e in V.equations]
    vrs = [str(v) for v in V.variables]
    if verbose:
        print(f"{name} class {cls}: {len(vrs)} variables, {len(eqs)} equations")

    lin = "+".join(f"{i + 1}*{v}" for i, v in enumerate(vrs))
    out = sing(f'ring r=0,({",".join(vrs)},T),dp;\n'
               f'ideal I={",".join(eqs)},T-({lin});\n'
               f'ideal E=eliminate(I,{"*".join(vrs)});\n"E:";E[1];\nquit;\n')
    lines = [l.strip() for l in out.splitlines() if l.strip()]
    if not lines or lines[-1] == 'E:':
        raise RuntimeError("elimination produced no eliminant")
    elim = sp.Poly(sp.sympify(lines[-1].replace('^', '**')), T)
    if verbose:
        print(f"   eliminant degree {elim.degree()} (the SCHEME degree, not [K:Q])")

    comps = []
    for h, _mult in sp.factor_list(elim.as_expr())[1]:
        hp = sp.Poly(h, T)
        if hp.degree() < 1:
            continue
        hs = str(sp.expand(h)).replace('**', '^')
        body = "\n".join(f'"{v}:"; reduce({v},G);' for v in vrs)
        # stdfglm, NOT std: the ideal is ZERO-DIMENSIONAL, so FGLM converts a cheap
        # degrevlex basis into the lex one we need.  A direct lex std on 11 variables
        # (5_2 class 1) did not finish in 10 minutes, while the SAME system solves in
        # 0.4 s under degrevlex -- the cost was the ORDERING, not the system.
        out = sing(f'ring r=0,({",".join(vrs)},T),lp;\n'
                   f'ideal I={",".join(eqs)},T-({lin}),{hs};\n'
                   f'ideal G;\n'
                   f'if (dim(std(I))==0) {{ G=stdfglm(I); }} else {{ G=std(I); }}\n'
                   f'{body}\nquit;\n')
        L = [l.strip() for l in out.splitlines() if l.strip()]
        co = {}
        for i, l in enumerate(L):
            if l.endswith(':') and l[:-1] in vrs and i + 1 < len(L):
                co[l[:-1]] = L[i + 1]
        if len(co) != len(vrs):
            continue
        zeros = [v for v, c in co.items() if c.strip() == '0']
        rec = {'min_poly_T': str(sp.expand(h)), 'field_degree': hp.degree(),
               'irreducible_over_Q': bool(hp.is_irreducible),
               'discriminant': str(sp.discriminant(hp)),
               'zero_coordinates': zeros, 'n_zero': len(zeros),
               'degenerate': bool(zeros), 'coords': co}
        # u must be a primitive cube root of unity -- necessary, NOT sufficient (trap 1)
        if 'u' in co and co['u'].strip() != '0':
            ue = sp.sympify(co['u'].replace('^', '**'))
            rec['u_is_cube_root'] = bool(
                sp.rem(sp.Poly(sp.expand(ue ** 2 + ue + 1), T), hp).as_expr() == 0)
        else:
            rec['u_is_cube_root'] = False
        comps.append(rec)
        if verbose:
            tag = f"DEGENERATE ({len(zeros)}/{len(vrs)} coords zero)" if zeros else "GENUINE"
            print(f"   component: min poly {rec['min_poly_T']}  deg {hp.degree()}  "
                  f"disc {rec['discriminant']}  -> {tag}")
    return {'manifold': name, 'obstruction_class': cls,
            'variables': vrs, 'n_equations': len(eqs),
            'eliminant_degree': elim.degree(), 'components': comps}


def to_point_json(name, cls, rec):
    """One genuine component -> the shape the arc's probes consume (generator named `t`)."""
    co = {v: str(sp.sympify(c.replace('^', '**')).subs(T, t)) for v, c in rec['coords'].items()}
    return {'manifold': name, 'obstruction_class': cls,
            'field': {'generator': 't',
                      'min_poly': str(sp.expand(sp.sympify(rec['min_poly_T']).subs(T, t))),
                      'degree': rec['field_degree'],
                      'irreducible_over_Q': rec['irreducible_over_Q'],
                      'discriminant': rec['discriminant']},
            'provenance': {'producer': 'ptolemy_exact_point.py',
                           'method': 'primitive element + lex GB, coordinates as normal forms',
                           'degenerate_components_discarded': None},
            'ptolemy': co}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('manifold')
    ap.add_argument('obstruction_class', type=int)
    ap.add_argument('--write', action='store_true', help='write the point JSON')
    a = ap.parse_args()

    res = extract(a.manifold, a.obstruction_class)
    genuine = [c for c in res['components'] if not c['degenerate']]
    degen = [c for c in res['components'] if c['degenerate']]
    print(f"\n   components: {len(res['components'])}  "
          f"genuine {len(genuine)}  degenerate (discarded) {len(degen)}")
    if not genuine:
        print("   NO GENUINE COMPONENT -- every component has a zero coordinate")
        raise SystemExit(1)
    for g in genuine:
        assert g['u_is_cube_root'], "genuine component without a valid cube root of unity"
        assert g['irreducible_over_Q'], "min poly reducible"
    if len(genuine) > 1:
        print(f"   NOTE: {len(genuine)} genuine components -- the variety is NOT a single "
              f"Galois orbit, so a per-point result does not upgrade to 'for all x' for free")
    g = genuine[0]
    print(f"\n   chosen: K = Q[t]/({g['min_poly_T']}), degree {g['field_degree']}, "
          f"disc {g['discriminant']}")
    pj = to_point_json(a.manifold, a.obstruction_class, g)
    pj['provenance']['degenerate_components_discarded'] = len(degen)
    pj['provenance']['genuine_components'] = len(genuine)
    stem = f"{a.manifold}-c{a.obstruction_class}"
    (HERE / f'{stem}-exact-components.json').write_text(json.dumps(res, indent=1) + "\n")
    if a.write:
        (HERE / f'{stem}-ptolemy-in-K.json').write_text(json.dumps(pj, indent=1) + "\n")
        print(f"   point -> {HERE / f'{stem}-ptolemy-in-K.json'}")
    print(f"   components -> {HERE / f'{stem}-exact-components.json'}")
