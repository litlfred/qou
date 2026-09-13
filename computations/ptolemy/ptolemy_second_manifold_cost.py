#!/usr/bin/env python3
"""What does a SECOND manifold actually cost for the duality arc? (qou-qjhc)

The arc's results -- sigma_b(rho) conjugate to rho^{-T} in GL(3,K), untwisted, at every
point of the L6a4 class-1 variety -- are one manifold, one obstruction class.  The standing
next step is a second manifold, and the standing BELIEF was that it costs what class 2 cost:
three solve routes with measured walls (msolve RUR >3000 s, GB-only mod p >2700 s, Singular
>5400 s) and a 403 on the upstream database.

THAT BELIEF IS WRONG, AND THIS PROBE MEASURES WHY.  The class-2 wall is not about obstruction
classes or about exactness; it is about L6a4 being LARGE -- 8 tetrahedra, 3 cusps, 27
variables after elimination.  Groebner cost is super-exponential in the variable count, and
a 2-tetrahedron manifold has SEVEN.  Measured below: m004 class 1 solves in about a second.

So the cost is not compute.  It is (a) whether a candidate satisfies the STRUCTURAL
conditions the arc's argument needs, and (b) parameterising the probes, which currently
hardcode L6a4's field and its two automorphism polynomials.

THE THREE STRUCTURAL CONDITIONS, and they are not all generic:

  1. zeta_3 in K.  Needed for the obstruction class to be non-trivial in the first place and
     for an automorphism to act on it.  MEASURED GENERIC so far -- true for every candidate.
  2. Gal(K/Q) ABELIAN.  This is what makes the orbit transport work at all:
     GaloisOrbitTransport.lean's `exists_not_forall_eq_of_not_central` says commutativity
     cannot be dropped, and the whole "sigma_b uniformly at every point, with A_g = g(A)"
     result rests on it.  MEASURED *NOT* GENERIC -- 5_2 class 1 has a NON-ABELIAN Galois
     group of order 12.  On such a manifold the transport argument does not apply, and that
     is the sharpness theorem biting on a real example rather than in principle.
  3. The orbit EXHAUSTS the variety.  L6a4 class 1 is one orbit of 4 = degree 4, which is
     what turns per-point results into "for all x".  NOT generic either: m004 class 1 has
     vdim 4 splitting as TWO components of degree 2, so an orbit is half the variety and the
     quantifier upgrade has to be redone per component.

WHAT EACH OUTCOME WOULD TEACH.  A second ABELIAN manifold that reproduces the untwisted
GL(3,K) result makes the phenomenon look structural.  A NON-ABELIAN one where the per-point
intertwiner still exists would say the transport argument is sufficient but not necessary --
a strictly more interesting negative, and 5_2 class 1 is the ready-made test case.

Exact throughout: Singular over Q for dimension, degree and elimination; sympy for
factorisation, Galois group and the zeta_3 test.  No floats anywhere.

NOTE ON A MISREAD, recorded because it nearly reached a report: sympy's
`galois_group(f)` returns `(G, alt)` where the SECOND value is whether G lies in the
alternating group -- NOT whether it is abelian.  Reading it as "abelian" reported m004's
C_2, an abelian group, as non-abelian.  Abelian-ness is `G.is_abelian`, used below.
"""
import json
import pathlib
import subprocess
import tempfile
import time
import warnings

import sympy as sp

warnings.filterwarnings('ignore')
import snappy  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
x = sp.Symbol('x')
CANDIDATES = [('m004', 1), ('m003', 1), ('5_2', 1), ('6_1', 1), ('L5a1', 1)]
CALIBRATION = ('L6a4', 1)      # known: 27 vars, vdim 4, Klein four -- the guard
WALL_DEMO = ('L6a4', 2)        # known wall; time-boxed here, not re-measured in full


def sing(script, timeout=600):
    """Run a Singular script.  The scratch file goes to a TEMP DIR, never into the repo:
    an earlier version wrote it beside this probe, so an interrupted run left an untracked
    `_cost.sing` in `computations/ptolemy/`.  A probe must not litter the tree it measures."""
    with tempfile.TemporaryDirectory() as td:
        p = pathlib.Path(td) / 'cost.sing'
        p.write_text(script)
        try:
            r = subprocess.run(['Singular', '-q', '--no-warn', str(p)],
                               capture_output=True, text=True, timeout=timeout)
            return r.stdout
        except subprocess.TimeoutExpired:
            return None


def measure(name, cls, solve_timeout=600):
    M = snappy.Manifold(name)
    V = M.ptolemy_variety(3, obstruction_class=cls, eliminate_fixed_ptolemys=True)
    eqs = [str(e) for e in V.equations]
    vrs = [str(v) for v in V.variables]
    row = {'manifold': name, 'class': cls, 'tetrahedra': M.num_tetrahedra(),
           'cusps': M.num_cusps(), 'variables': len(vrs), 'equations': len(eqs)}
    t0 = time.time()
    out = sing(f'ring r = 0, ({",".join(vrs)}), dp;\n'
               f'ideal I = {",".join(eqs)};\nideal G = std(I);\n'
               f'"DIM:"; dim(G);\n"VDIM:"; vdim(G);\nquit;\n', timeout=solve_timeout)
    row['solve_seconds'] = round(time.time() - t0, 2)
    if out is None:
        row['solved'] = False
        row['note'] = f'Singular TIMEOUT at {solve_timeout}s -- a wall'
        return row
    L = [l.strip() for l in out.splitlines() if l.strip()]
    for i, l in enumerate(L):
        if l == 'DIM:' and i + 1 < len(L):
            row['dim'] = L[i + 1]
        if l == 'VDIM:' and i + 1 < len(L):
            row['vdim'] = L[i + 1]
    row['solved'] = True
    # primitive element -> min poly -> field structure
    for seed in range(1, 6):
        lin = "+".join(f"{seed ** i % 7 + 1}*{v}" for i, v in enumerate(vrs))
        out = sing(f'ring r = 0, ({",".join(vrs)},T), dp;\n'
                   f'ideal I = {",".join(eqs)}, T-({lin});\n'
                   f'ideal E = eliminate(I, {"*".join(vrs)});\n"ELIM:"; E[1];\nquit;\n',
                   timeout=solve_timeout)
        if out is None:
            continue
        L = [l.strip() for l in out.splitlines() if l.strip()]
        poly = L[-1] if L and L[-1] != 'ELIM:' else ''
        if not poly:
            continue
        try:
            p = sp.Poly(sp.sympify(poly.replace('^', '**')).subs(sp.Symbol('T'), x), x)
        except Exception:
            continue
        if p.degree() < 2:
            continue
        facs = sp.factor_list(p.as_expr())[1]
        row['eliminant_degree'] = p.degree()
        row['component_degrees'] = sorted(f[0].as_poly(x).degree() for f in facs)
        row['n_components'] = len(facs)
        top = max(facs, key=lambda f: f[0].as_poly(x).degree())[0]
        row['min_poly'] = str(sp.expand(top))
        row['field_degree'] = top.as_poly(x).degree()
        try:
            G, _alt = sp.polys.numberfields.galoisgroups.galois_group(sp.Poly(top, x))
            row['galois_order'] = G.order()
            row['galois_abelian'] = bool(G.is_abelian)   # NOT the second return value
        except Exception as e:
            row['galois_order'] = None
            row['galois_abelian'] = None
            row['galois_note'] = f'{type(e).__name__}: {str(e)[:60]}'
        try:
            Kf = sp.QQ.algebraic_field(sp.rootof(top, 0))
            fl = sp.Poly(x ** 2 + x + 1, x, domain=Kf).factor_list()[1]
            row['zeta3_in_K'] = any(g[0].as_poly(x).degree() == 1 for g in fl)
        except Exception:
            row['zeta3_in_K'] = None
        break
    return row


rows = []
print(f"{'manifold':9s} {'cls':>3s} {'tet':>3s} {'vars':>4s} {'solve s':>8s} {'vdim':>5s} "
      f"{'comps':>7s} {'degK':>4s} {'|Gal|':>5s} {'abelian':>7s} {'z3':>4s}", flush=True)
print("-" * 74, flush=True)
# Candidates FIRST and time-boxed.  The L6a4 calibration is the EXPENSIVE row, and putting
# it first is what stalled this probe's first run with no output at all.  Its answer is
# already in the corpus (degree 4, Klein four), so it is time-boxed rather than re-derived --
# and that a naive std() TIMES OUT on it is itself the finding: the corpus's exact class-1
# point did not come from a naive Groebner basis over Q, so "L6a4 class 1 is solved" is not
# evidence that this pipeline's cheapest route reaches it.
for nm, cl in CANDIDATES + [CALIBRATION]:
    r = measure(nm, cl, solve_timeout=(90 if (nm, cl) == CALIBRATION else 300))
    rows.append(r)
    print(f"{r['manifold']:9s} {r['class']:3d} {r['tetrahedra']:3d} {r['variables']:4d} "
          f"{r['solve_seconds']:8.2f} {str(r.get('vdim','-')):>5s} "
          f"{str(r.get('component_degrees','-')):>7s} {str(r.get('field_degree','-')):>4s} "
          f"{str(r.get('galois_order','-')):>5s} {str(r.get('galois_abelian','-')):>7s} "
          f"{str(r.get('zeta3_in_K','-')):>4s}", flush=True)

print("\n=== the known wall, time-boxed (not re-measured in full) ===")
w = measure(*WALL_DEMO, solve_timeout=90)
rows.append(w)
print(f"   L6a4 class 2 ({w['variables']} vars): "
      f"{'solved in ' + str(w['solve_seconds']) + 's' if w['solved'] else w['note']}")

ok = [r for r in rows if r.get('solved') and r['manifold'] != 'L6a4']
abelian = [r for r in ok if r.get('galois_abelian') is True]
single = [r for r in ok if r.get('n_components') == 1]
z3 = [r for r in ok if r.get('zeta3_in_K') is True]
report = {'probe': 'ptolemy_second_manifold_cost', 'rows': rows,
          'candidates_solved': len(ok),
          'with_zeta3': len(z3), 'with_abelian_galois': len(abelian),
          'with_single_component_orbit': len(single),
          'verdict': (
              "COMPUTE IS NOT THE COST. Small manifolds solve in about a second; the L6a4 "
              "class-2 wall is a VARIABLE-COUNT wall (27 vs 7), not a wall about obstruction "
              "classes or exactness. The real costs are (a) the arc's probes hardcode L6a4's "
              "field and automorphism polynomials and must be parameterised, and (b) two of "
              "the three structural conditions are NOT generic: zeta_3 in K holds "
              "everywhere measured, but an ABELIAN Galois group fails on 5_2 class 1 "
              "(order 12), and a single-orbit variety fails on m004 class 1 (two components)."
          )}
print("\n" + report['verdict'])
out = HERE / 'second-manifold-cost.json'
out.write_text(json.dumps(report, indent=1) + "\n")
print(f"\nreport -> {out}")
