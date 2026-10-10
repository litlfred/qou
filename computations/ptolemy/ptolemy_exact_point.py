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


def _primitive_forms(vrs):
    """Candidate primitive elements, cheapest-looking first.  Elimination cost varies by
    orders of magnitude across these, and the first that returns wins."""
    n = len(vrs)
    yield "+".join(f"{i + 1}*{v}" for i, v in enumerate(vrs))
    for m in (7, 5, 11, 3):
        yield "+".join(f"{(m ** i) % m + 1}*{v}" for i, v in enumerate(vrs))
    for m in (7, 5):
        yield "+".join(f"{(i * i) % m + 1}*{v}" for i, v in enumerate(vrs))
    yield "+".join(f"{v}" for v in vrs)
    for k in range(min(n, 4)):
        yield vrs[k]


def sing(script, timeout=900):
    """Run Singular; the scratch file goes to a temp dir, never into the repo."""
    with tempfile.TemporaryDirectory() as td:
        p = pathlib.Path(td) / 's.sing'
        p.write_text(script)
        try:
            r = subprocess.run(['Singular', '-q', '--no-warn', str(p)],
                               capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            return None          # the caller decides: try another form, or report the wall
        return r.stdout


def _coords_via_normal_forms(vrs, eqs, lin, h, nf_timeout):
    """Coordinates from DEGREVLEX normal forms alone -- no lex Groebner basis.

    The old route asked Singular for a LEX basis of (eqs, T - lin, h) in a
    12-variable ring over Q.  Lex is where rational coefficients explode, and
    `stdfglm` does not avoid that: FGLM makes the lex basis cheaper to REACH,
    it still has to build it.  Measured on `5_2` class 1 that reached
    7.9 GB RSS at 717 s and returned nothing.

    Nothing here needs the lex basis.  What a component needs is each
    coordinate as a polynomial in T, and when T is a primitive element the
    shape lemma says {1, T, ..., T^(d-1)} already spans the component ring.
    So reduce T^i and each v to degrevlex normal forms -- cheap -- and solve
    the one small exact linear system that expresses v over that basis.

    Returns (coords | None, status).  A failure is NAMED, never silent:
    OUT_OF_SPAN means the shape lemma does not apply here (T is not
    separating, or the component is non-reduced), which is a real fact about
    the geometry and the caller should fall back rather than fudge.
    """
    d = sp.Poly(h, T).degree()
    hs = str(sp.expand(h)).replace('**', '^')
    body = "".join(f'"P{i}:"; reduce(T^{i},G);\n' for i in range(d))
    body += "".join(f'"V{v}:"; reduce({v},G);\n' for v in vrs)
    out = sing(f'ring r=0,({",".join(vrs)},T),dp;\n'
               f'ideal I={",".join(eqs)},T-({lin}),{hs};\n'
               f'ideal G=std(I);\n"VDIM:"; vdim(G);\n{body}quit;\n',
               timeout=nf_timeout)
    if out is None:
        return None, 'TIMEOUT'
    L = [l.strip() for l in out.splitlines() if l.strip()]
    blk = {}
    for i, l in enumerate(L):
        if l.endswith(':') and i + 1 < len(L):
            blk[l[:-1]] = L[i + 1]
    if any(f'P{i}' not in blk for i in range(d)) or any(f'V{v}' not in blk for v in vrs):
        return None, 'INCOMPLETE_OUTPUT'
    syms = [sp.Symbol(v) for v in vrs] + [T]
    basis = [sp.Poly(sp.expand(sp.sympify(blk[f'P{i}'].replace('^', '**'))), *syms)
             for i in range(d)]
    mons = sorted(set().union(*(set(b.monoms()) for b in basis)))
    M = sp.Matrix([[b.coeff_monomial(m) for b in basis] for m in mons])
    coords = {}
    for v in vrs:
        w = sp.Poly(sp.expand(sp.sympify(blk[f'V{v}'].replace('^', '**'))), *syms)
        if set(w.monoms()) - set(mons):
            return None, f'OUT_OF_SPAN:{v}'
        b = sp.Matrix([w.coeff_monomial(m) for m in mons])
        sol = M.solve(b) if M.rows == M.cols else M.solve_least_squares(b)
        if sp.expand(M * sol - b) != sp.zeros(M.rows, 1):
            return None, f'INCONSISTENT:{v}'
        coords[v] = str(sp.expand(sum(sol[i] * T ** i for i in range(d))))
    return coords, 'OK'


def _verify_coords(vrs, eqs, coords, h):
    """Back-substitute the coordinates into the Ptolemy equations mod h(T).

    NEITHER route verified its own output before this was added -- both
    trusted Singular's normal forms and wrote the point out.  This is the
    check that makes a component's coordinates a measurement rather than a
    report: every defining equation must vanish in Q[T]/(h).
    """
    hp = sp.Poly(h, T)
    sub = {sp.Symbol(v): sp.sympify(c.replace('^', '**')) for v, c in coords.items()}
    for e in eqs:
        r = sp.expand(sp.sympify(e.replace('^', '**')).subs(sub))
        if r == 0:
            continue
        if sp.rem(sp.Poly(r, T), hp).as_expr() != 0:
            return False
    return True


def extract(name, cls, verbose=True, elim_timeout=240, nf_timeout=900):
    M = snappy.Manifold(name)
    V = M.ptolemy_variety(3, obstruction_class=cls, eliminate_fixed_ptolemys=True)
    eqs = [str(e) for e in V.equations]
    vrs = [str(v) for v in V.variables]
    if verbose:
        print(f"{name} class {cls}: {len(vrs)} variables, {len(eqs)} equations")

    # TRY SEVERAL PRIMITIVE ELEMENTS, each on its own budget.  A bad linear form can cost
    # orders of magnitude more than a good one, so advancing on timeout is worth having.
    #
    # DO NOT re-tell the story this guard was first committed with.  That commit said `5_2`
    # class 1 walled at 900 s on the coefficients 1..11 and that a DIFFERENT form fixed it.
    # Re-measured on a quiet container: form #1 -- the one that "walled" -- completes that
    # elimination in 45.3 s, and the command is byte-identical to the one that ran for 900 s.
    # The container had been running TWO concurrent `lake build` invocations of the same two
    # heavy Lean modules (~4 GB RSS each) beside Singular, with 161 MB of 16 GB free.  The
    # wall was memory contention, and it was attributed to the mathematics.  No measurement
    # here shows any form beating #1 on `5_2`; the ad-hoc run that "returned in seconds" was
    # confounded the same way, in the other direction.
    #
    # So: never quote a Singular timing from this container without saying what else was
    # running.  This guard is cheap insurance, not a fix for a diagnosed problem.
    elim, lin, tried = None, None, 0
    for lin_try in _primitive_forms(vrs):
        tried += 1
        if verbose:
            print(f"   [stage 1/2] eliminating, primitive element #{tried} "
                  f"(budget {elim_timeout}s) ...", flush=True)
        out = sing(f'ring r=0,({",".join(vrs)},T),dp;\n'
                   f'ideal I={",".join(eqs)},T-({lin_try});\n'
                   f'ideal E=eliminate(I,{"*".join(vrs)});\n"E:";E[1];\nquit;\n',
                   timeout=elim_timeout)
        if out is None:
            continue                                  # this form timed out; try the next
        lines = [l.strip() for l in out.splitlines() if l.strip()]
        if not lines or lines[-1] == 'E:':
            continue
        try:
            cand = sp.Poly(sp.sympify(lines[-1].replace('^', '**')), T)
        except Exception:
            continue
        if cand.degree() >= 1:
            elim, lin = cand, lin_try
            break
    if elim is None:
        raise RuntimeError(f"no primitive element produced an eliminant in {tried} attempts "
                           f"at {elim_timeout}s each -- raise --elim-timeout or add forms")
    if verbose:
        print(f"   primitive element #{tried} worked", flush=True)
    if verbose:
        print(f"   eliminant degree {elim.degree()} (the SCHEME degree, not [K:Q])")

    comps, walled = [], []
    for h, _mult in sp.factor_list(elim.as_expr())[1]:
        hp = sp.Poly(h, T)
        if hp.degree() < 1:
            continue
        # LEX-FREE ROUTE FIRST.  See _coords_via_normal_forms: the lex basis the
        # old route builds is the whole cost, and nothing downstream needs it.
        nf_coords, nf_status = _coords_via_normal_forms(vrs, eqs, lin, h, nf_timeout)
        if nf_coords is not None and _verify_coords(vrs, eqs, nf_coords, h):
            co, route = nf_coords, 'normal-form'
        else:
            co, route = None, f'lex-fallback(after {nf_status})'
        if co is None:
            # FALLBACK: the historical lex route.  Kept because the lex-free route
            # is only valid where the shape lemma applies -- if T fails to separate
            # the component, OUT_OF_SPAN fires and this is the honest answer, at
            # its own (large) cost.  stdfglm makes the lex basis cheaper to reach
            # but still builds it, which is why this walls where the other does not.
            hs = str(sp.expand(h)).replace('**', '^')
            body = "\n".join(f'"{v}:"; reduce({v},G);' for v in vrs)
            out = sing(f'ring r=0,({",".join(vrs)},T),lp;\n'
                       f'ideal I={",".join(eqs)},T-({lin}),{hs};\n'
                       f'ideal G;\n'
                       f'if (dim(std(I))==0) {{ G=stdfglm(I); }} else {{ G=std(I); }}\n'
                       f'{body}\nquit;\n', timeout=nf_timeout)
            # sing() returns None on timeout.  Report the wall rather than crashing
            # on it: a stage-2 wall used to surface as `AttributeError: 'NoneType'
            # object has no attribute 'splitlines'`, an opaque traceback in place of
            # the one fact worth reporting -- which component, at which budget.
            if out is None:
                walled.append({'min_poly_T': str(sp.expand(h)), 'degree': hp.degree(),
                               'budget_s': nf_timeout, 'after': route})
                if verbose:
                    print(f"   component: min poly {sp.expand(h)}  deg {hp.degree()}  "
                          f"-> NORMAL-FORM WALL at {nf_timeout}s ({route})", flush=True)
                continue
            L = [l.strip() for l in out.splitlines() if l.strip()]
            co = {}
            for i, l in enumerate(L):
                if l.endswith(':') and l[:-1] in vrs and i + 1 < len(L):
                    co[l[:-1]] = L[i + 1]
            if len(co) != len(vrs):
                continue
        zeros = [v for v, c in co.items() if c.strip() == '0']
        rec = {'stage2_route': route,
               'equations_verified': bool(_verify_coords(vrs, eqs, co, h)),
               'min_poly_T': str(sp.expand(h)), 'field_degree': hp.degree(),
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
            'eliminant_degree': elim.degree(), 'components': comps,
            'normal_form_walled': walled, 'nf_timeout_s': nf_timeout}


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
                           # route-accurate: the default path builds NO lex basis.
                           # Do not restore the old 'primitive element + lex GB'
                           # wording -- it described this file while the file was
                           # produced by the lex-free route.
                           'method': f"primitive element + {rec.get('stage2_route', 'unknown')} "
                                     f"coordinates, back-substitution verified="
                                     f"{rec.get('equations_verified')}",
                           'degenerate_components_discarded': None},
            'ptolemy': co}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('manifold')
    ap.add_argument('obstruction_class', type=int)
    ap.add_argument('--write', action='store_true', help='write the point JSON')
    ap.add_argument('--elim-timeout', type=int, default=240,
                    help='per-primitive-element budget for the elimination step')
    ap.add_argument('--nf-timeout', type=int, default=900,
                    help='per-component budget for the lex-GB / normal-form step')
    a = ap.parse_args()

    res = extract(a.manifold, a.obstruction_class, elim_timeout=a.elim_timeout,
                  nf_timeout=a.nf_timeout)
    genuine = [c for c in res['components'] if not c['degenerate']]
    degen = [c for c in res['components'] if c['degenerate']]
    print(f"\n   components: {len(res['components'])}  "
          f"genuine {len(genuine)}  degenerate (discarded) {len(degen)}")
    if res['normal_form_walled']:
        print(f"   normal-form WALLED on {len(res['normal_form_walled'])} component(s) "
              f"at {res['nf_timeout_s']}s -- raise --nf-timeout; NOT a property of the "
              f"manifold until re-run on a quiet box (see the stage-1 comment)")
    if not genuine:
        print("   NO GENUINE COMPONENT -- every component has a zero coordinate")
        raise SystemExit(1)
    for g in genuine:
        assert g['u_is_cube_root'], "genuine component without a valid cube root of unity"
        assert g['irreducible_over_Q'], "min poly reducible"
    if len(genuine) > 1:
        print(f"   NOTE: {len(genuine)} genuine components -- the variety is NOT a single "
              f"Galois orbit, so a per-point result does not upgrade to 'for all x' for free")
    stem = f"{a.manifold}-c{a.obstruction_class}"
    (HERE / f'{stem}-exact-components.json').write_text(json.dumps(res, indent=1) + "\n")

    # ONE POINT FILE PER GENUINE ORBIT.  This used to write `genuine[0]` only --
    # directly under the NOTE above saying the variety is not a single Galois
    # orbit.  The producer diagnosed the multi-orbit case and then emitted data
    # that could only describe one of them, so every downstream consumer saw a
    # one-orbit variety no matter what was measured.  `5_2` class 1 is the case
    # that exposed it: two genuine orbits, degrees 4 and 6, and only the deg-4
    # one reachable.  A per-orbit result cannot be pooled across orbits, so the
    # orbits have to be separately addressable to be separately testable.
    for idx, g in enumerate(genuine):
        pj = to_point_json(a.manifold, a.obstruction_class, g)
        pj['provenance']['degenerate_components_discarded'] = len(degen)
        pj['provenance']['genuine_components'] = len(genuine)
        pj['provenance']['orbit_index'] = idx
        label = "chosen" if idx == 0 else f"orbit {idx}"
        print(f"\n   {label}: K = Q[t]/({g['min_poly_T']}), degree {g['field_degree']}, "
              f"disc {g['discriminant']}")
        if not a.write:
            continue
        # orbit 0 keeps the historical unsuffixed name so existing consumers and
        # the committed L6a4 / m004 artifacts do not move.
        names = [f'{stem}-ptolemy-in-K.json'] if idx == 0 else []
        names.append(f'{stem}-orbit{idx}-ptolemy-in-K.json')
        for n in names:
            (HERE / n).write_text(json.dumps(pj, indent=1) + "\n")
            print(f"   point -> {HERE / n}")
    print(f"   components -> {HERE / f'{stem}-exact-components.json'}")
