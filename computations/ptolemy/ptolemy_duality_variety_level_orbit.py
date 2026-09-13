#!/usr/bin/env python3
"""Is `D = sigma_b modulo gauge` an identity on the WHOLE L6a4 class-1 variety?  (bean qou-qjhc)

WHAT IS OPEN, AND WHY THIS IS THE NEXT STEP.  #7092 established, exactly in
K = Q[T]/(f), that at the class-1 Ptolemy point x the two maps to P^{-c} -- duality
D (rho -> rho^{-T}, realised by the dual decoration g* = (v1 x v2, v1 x v3, v2 x v3))
and the Galois transport sigma_b -- differ by a PGL(3) decoration gauge, while sigma_a
does not.  That producer's own SCOPE paragraph says what it does not give:

    "A 'yes' here is a point-level fact about the class-1 point ... It is not an
     identity of maps on the variety"

This probe closes exactly that gap, and only that gap.

THE LEVER, which is structural rather than computational.  Three facts already in the
corpus line up:

  * the class-1 saturated ideal is ZERO-DIMENSIONAL OF DEGREE 4 over Q, with `u` carried
    as a VARIABLE (L6a4-c1-sweep.json: 13 variables including u, both mod p and in
    characteristic zero, degrees agree);
  * f is IRREDUCIBLE over Q of degree 4, and the Ptolemy field equals the trace field
    with span_dimension 4 (L6a4-c1-irreducibility.json, L6a4-c1-trace-field.json) -- so
    x generates K and its Galois orbit has 4 DISTINCT points;
  * Gal(K/Q) = Z/2 x Z/2 = {1, sigma_a, sigma_b, tau}, ABELIAN (#7092).

Four distinct orbit points inside a degree-4 variety leaves no room: the orbit IS the
variety.  So a property that (i) holds at x and (ii) is Galois-equivariant holds at every
point of the variety -- and `D` is built from a relabelling, 3x3 determinants and an
inverse, all of which commute with any field automorphism.  Hence:

    D(sigma x) = sigma(D x) = sigma(sigma_b x) = sigma_b(sigma x)

the last step using that the group is ABELIAN.  Nothing here is numerical.

THE PREDICTION, WRITTEN DOWN BEFORE THE RUN.  If the reasoning is right, the 4 x 2
verdict table is constant down each column:

    sigma_b: COBOUNDARY at all four points        sigma_a: NOT at any of the four

This is falsifiable in both directions and the run is the test, not an illustration.  A
column that is not constant refutes the equivariance argument -- which would mean either
D is not Q-rational on this data or the gauge is not Galois-stable, and either would be
the more interesting outcome.

WHY THIS IS A MEASUREMENT AND NOT A RESTATEMENT.  The argument above could be wrong in
ways the algebra hides: `expand_point` carries u-powers from snappy's
canonical_representative, so conjugating a coordinate vector is not obviously the same as
conjugating the point; and the coboundary verdict is decided on an INTEGER kernel, where
a Galois-moved ratio could in principle fail a root-of-unity relation that the original
passed.  So every leg is measured rather than assumed:

  G1  the four conjugate vectors are PAIRWISE DISTINCT  (orbit size 4 = degree 4, so the
      orbit exhausts the variety -- this is what lets a point-level fact generalise)
  G2  each conjugate is a GENUINE VARIETY POINT: all 32 GGZ (5.2) per-tetrahedron
      relations, and all 128 face identifications at its own cube root sigma(u2)
  G3  EQUIVARIANCE OF D, measured coordinate-wise on all 128:  D(sigma Y) = sigma(D Y).
      This is the load-bearing leg and it is checked, not argued
  G4  CALIBRATION: the identity row must reproduce #7092's published verdicts exactly
      (sigma_b coboundary, sigma_a not).  Without this every other row is unvalidated
  G5  REFUTATION CONTROL: the sigma_a column must come out NO.  A table of all-YES would
      mean the test cannot fail and decides nothing

ANSATZ.  Ansatz B (the 128 x 6 decoration torus, snappy's
_ptolemy_equations_action_by_decoration_change) is the actual gauge group of the variety
and is the only one tested here.  The scalar sub-ansatz needs no separate run: the
nesting theorem QOU.Eightfold.GaugeAnsatzNesting (sorry-free; A_SCALAR[:,k] =
A_TORUS[:,(0,k)] + A_TORUS[:,(1,k)] exactly over Z on all 128 non-vertex rows) gives
scalar-coboundary => torus-coboundary, so a torus NO forces a scalar NO.  Where the torus
says YES the scalar question is strictly stronger and is already answered NO at x by
#7092.

SCOPE.  A "yes" across the table is an identity of maps ON THE CLASS-1 VARIETY of this
one manifold: D and sigma_b agree modulo gauge at every point of it.  It is NOT a
statement about other obstruction classes, other manifolds, or the Ptolemy-to-
representation direction; whether rho -> rho^{-T} INDUCES sigma_b on representations
remains the open content of bean qou-qjhc, and rule 13a keeps that bean open.

EXACTNESS.  All arithmetic in K: polynomials over Q reduced mod f, inverses by sympy's
exact `invert`.  No floats, no tolerances anywhere.  An element is 1 or it is not.
"""
import contextlib
import io
import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
os.chdir(HERE)

# Importing the #7092 producer runs its whole verified pipeline -- the duality formulas
# checked on 25 random exact SL(3) decorations, the point checked against GGZ (5.2), the
# sigma checked to be automorphisms inverting zeta_3.  Reusing it means this probe cannot
# disagree with it through a re-implementation.  Its own witness write is suppressed:
# re-emitting a sibling's witness would churn provenance for no new content.
_SIB = HERE / 'ptolemy-duality-sigma-coboundary-test.witness.json'
_saved = _SIB.read_bytes() if _SIB.exists() else None
_t0 = time.time()
_buf = io.StringIO()
with contextlib.redirect_stdout(_buf):
    import ptolemy_duality_sigma_coboundary_test as base
if _saved is not None:
    # The import re-ran the sibling producer, which rewrites its own witness.  Every
    # mathematical field comes back byte-identical (verified 2026-09-13 across a changed
    # environment, mpmath 1.3.0 -> 1.4.1); only computedAt / commitSha / durationMs move.
    # AGENTS.md: those are informational provenance and are never to be refreshed as a
    # side effect, so the file is restored exactly.
    _SIB.write_bytes(_saved)
print(f"imported the #7092 producer (its full pipeline re-ran) in {time.time()-_t0:.1f}s;"
      f" its witness restored byte-for-byte")

import sympy as sp

K, kmul, kinv, kstr = base.K, base.kmul, base.kinv, base.kstr
sig_apply, act_names = base.sig_apply, base.act_names
T, X, u1, u2 = base.T, base.X, base.u1, base.u2

# ---------------------------------------------------------------- the Galois group
_comp = lambda g, h: K(g.subs(T, h)).as_expr()
SA, SB = base.SIGMA['sigma_a'], base.SIGMA['sigma_b']
GAL = {'id': T, 'sigma_a': SA, 'sigma_b': SB, 'tau': _comp(SA, SB)}
ORDER = ['id', 'sigma_a', 'sigma_b', 'tau']

def conj(P, g):
    return {nm: sig_apply(P[nm], g) for nm in act_names}

PTS = {g: conj(X, GAL[g]) for g in ORDER}
assert all(K(PTS['id'][nm] - X[nm]).is_zero for nm in act_names), "identity moved the point"

report = {'probe': 'ptolemy_duality_variety_level_orbit', 'manifold': 'L6a4',
          'obstruction_class': 1, 'guards': {}, 'table': {}}

# ------------------------------------------------------------- G1: orbit is size 4
distinct = True
for i, a in enumerate(ORDER):
    for b in ORDER[i + 1:]:
        if all(K(PTS[a][nm] - PTS[b][nm]).is_zero for nm in act_names):
            distinct = False
            print(f"G1 FAIL: conjugates {a} and {b} coincide")
print(f"G1 four conjugates pairwise distinct: {distinct}"
      f"   -> orbit size {'4' if distinct else '<4'}; variety degree 4 (L6a4-c1-sweep.json),"
      f" so the orbit {'IS' if distinct else 'is NOT'} the whole variety")
report['guards']['G1_orbit_size_4_equals_degree'] = distinct
assert distinct, "orbit smaller than 4: the generalisation step does not apply"

# --------------------------------------------- G2: each conjugate is a variety point
for g in ORDER:
    ug = sig_apply(u2, GAL[g])
    at_u2 = 'u2' if K(ug - u2).is_zero else 'u1'
    bad_rel = base.ptolemy_relation_failures(PTS[g])
    bad_id = base.identification_failures(PTS[g], ug)
    ok = not bad_rel and not bad_id
    print(f"G2 {g:8s}: GGZ(5.2) failures {len(bad_rel)}/32, identification failures "
          f"{len(bad_id)}/128 at its own cube root {at_u2}  -> {'variety point' if ok else 'NOT A POINT'}")
    report['guards'].setdefault('G2_variety_point', {})[g] = {
        'cube_root': at_u2, 'ggz_failures': len(bad_rel), 'identification_failures': len(bad_id)}
    assert ok, f"conjugate {g} is not a point of the variety"

# ------------------------------------------- G3: equivariance of D (load-bearing)
DX = base.dual_point(X)
equivariant = {}
for g in ORDER:
    lhs = base.dual_point(PTS[g])                    # D(sigma x)
    rhs = conj(DX, GAL[g])                           # sigma(D x)
    bad = [nm for nm in act_names if not K(lhs[nm] - rhs[nm]).is_zero]
    equivariant[g] = len(bad)
    print(f"G3 {g:8s}: D(sigma x) vs sigma(D x) -- {128 - len(bad)}/128 coordinates agree exactly in K")
report['guards']['G3_D_equivariance_disagreeing_coordinates'] = equivariant
assert all(v == 0 for v in equivariant.values()), "D is NOT Galois-equivariant on this data"

# ------------------------------------------------------- the 4 x 2 verdict table
print("\n=== 4 x 2 table: is sigma(y)/D(y) a coboundary of the decoration torus? ===")
for g in ORDER:
    Y = PTS[g]
    DY = base.dual_point(Y)
    report['table'][g] = {}
    for snm in ('sigma_a', 'sigma_b'):
        ratio = {nm: kmul(sig_apply(Y[nm], base.SIGMA[snm]), kinv(DY[nm])) for nm in act_names}
        with contextlib.redirect_stdout(io.StringIO()):
            out, gauge = base.coboundary_test(
                f'{g}|{snm}', base.A_TORUS, base.TORUS_COLS, act_names, ratio)
        # NOT `gauge is not None`.  In the index-3 case coboundary_test returns a second
        # value of None when w = r(3 e_0) has no cube root in K -- that encodes "the PGL(3)
        # gauge element does not LIFT to a diagonal SL(3) matrix", NOT "there is no gauge
        # element".  Reading that None as the verdict conflates the two, and the #7092
        # producer's own answer at x is precisely the case where they differ.  The
        # coboundary question is decided by the INTEGER KERNEL: r is a coboundary on the
        # row lattice iff every kernel relation has product exactly 1.
        fail = out.get('kernel_relations_failing', 0)
        is_cob = (fail == 0)
        lifts = bool(out.get('w_is_cube_in_K', gauge is not None))
        verdict = ('NOT a coboundary' if not is_cob
                   else 'coboundary (SL3 lift)' if lifts
                   else 'coboundary (PGL3 only)')
        print(f"   point {g:8s}  {snm}: {verdict:24s} ({fail} of {out['kernel_rank']} kernel relations fail)")
        report['table'][g][snm] = {'verdict': verdict, 'is_coboundary': is_cob,
                                   'sl3_lift_exists': lifts if is_cob else None,
                                   'w_eq_r_of_3e0': out.get('w_eq_r_of_3e0'),
                                   'kernel_relations_failing': fail,
                                   'kernel_rank': out['kernel_rank'],
                                   'producer_verdict': out.get('verdict')}

# ------------------------------------------------ G4 calibration, G5 refutation ctrl
idrow = report['table']['id']
calib = (idrow['sigma_b']['is_coboundary'] is True
         and idrow['sigma_b']['sl3_lift_exists'] is False
         and idrow['sigma_a']['is_coboundary'] is False)
print(f"\nG4 calibration -- identity row reproduces #7092 exactly (sigma_b: coboundary of the"
      f" PGL(3) torus with NO SL(3) lift; sigma_a: not a coboundary): {calib}")
report['guards']['G4_identity_row_reproduces_7092'] = calib
assert calib, "harness does not reproduce the published point-level result; table is void"

ctrl = all(report['table'][g]['sigma_a']['is_coboundary'] is False for g in ORDER)
print(f"G5 refutation control -- sigma_a column is NO everywhere (the test CAN fail): {ctrl}")
report['guards']['G5_sigma_a_column_all_no'] = ctrl

# ------------- the SL(3)-lift obstruction transports too (cross-check of PR #7273)
# w = r(3 e_0) is the element whose cube-root-ness decides the SL(3) lift.  Under the
# orbit it must move by Galois, w(sigma x) = sigma(w(x)); PR #7273 measured independently,
# by descent to the quadratic subfields, that sigma_a FIXES w (w lies in Fix(sigma_a) =
# Q(sqrt(-15))).  Those two facts together force w to take exactly TWO values across the
# four points, constant on the cosets of {1, sigma_a}.  Checked here from the orbit side,
# which shares no machinery with the subfield route.
ws = {g: report['table'][g]['sigma_b']['w_eq_r_of_3e0'] for g in ORDER}
w_transports = all(
    K(sp.sympify(ws[g]) - sig_apply(K(sp.sympify(ws['id'])), GAL[g]).as_expr()).is_zero
    for g in ORDER)
n_distinct_w = len(set(ws.values()))
cosets_ok = ws['id'] == ws['sigma_a'] and ws['sigma_b'] == ws['tau'] and ws['id'] != ws['sigma_b']
print(f"\nw = r(3 e_0) transports by Galois, w(sigma x) = sigma(w(x)): {w_transports}")
print(f"   distinct values across the 4 points: {n_distinct_w} "
      f"(constant on cosets of the stabiliser {{1, sigma_a}}: {cosets_ok})")
print(f"   -> independently reproduces PR #7273 section 4 (sigma_a fixes w; w in Q(sqrt(-15)))")
report['w_transport'] = {'transports_by_galois': w_transports,
                         'distinct_values': n_distinct_w,
                         'constant_on_cosets_of_stab_sigma_a': cosets_ok,
                         'values': ws,
                         'cross_check_of': 'PR #7273 section 4 (w in Fix(sigma_a) = Q(sqrt(-15)))'}

const_b = len({report['table'][g]['sigma_b']['verdict'] for g in ORDER}) == 1
const_a = len({report['table'][g]['sigma_a']['verdict'] for g in ORDER}) == 1
print(f"\ncolumns constant down the orbit:  sigma_b {const_b}   sigma_a {const_a}")
report['prediction_held'] = bool(const_a and const_b and calib and ctrl)
report['verdict'] = (
    "D = sigma_b modulo the PGL(3) decoration gauge at EVERY point of the L6a4 class-1 "
    "variety (4 of 4), and D != sigma_a modulo any gauge at every point"
    if report['prediction_held'] else
    "PREDICTION FAILED -- the verdict is not constant down the Galois orbit; see the table")
print("\nVERDICT: " + report['verdict'])

out_path = HERE / 'L6a4-c1-duality-variety-level.json'
out_path.write_text(json.dumps(report, indent=1) + "\n")
print(f"\nreport -> {out_path}")
