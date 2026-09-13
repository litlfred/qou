"""aomega_m3_pretzel_nz_rank_one_probe.py

Route C, M3, Part 10 (bean qou-x3iv): is the (-2,3,7) pretzel's state integral
one-dimensional, and if so of what SHAPE — derived from a held prescription and
SnapPy's triangulation, not guessed.

Held inputs:
  DG arxiv-1202.6268v2 (2.3)-(2.8): gluing matrices (G, G', G'') from the ideal
    triangulation; the Neumann-Zagier matrices for the first N-1 edges plus the
    meridian, with Z' eliminated by Z + Z' + Z'' = i pi:
        A_ij = G_ij - G'_ij,   B_ij = G''_ij - G'_ij,
        nu_i = 2 - sum_j G'_ij (edges),  nu_N = -sum_j G'_{N+1,j} (meridian);
    (2.9) A B^T = B A^T; Lemma A.3: a quad type with det B != 0 always exists.
  DG (5.2): the state integral is  int d^N Z  exp[(1/hbar)( ... + 1/2 Z . B^{-1}A Z )]
    prod_i psi_hbar(Z_i),  so the Gaussian coupling between tetrahedra is the
    SYMMETRIC matrix B^{-1}A.  If B^{-1}A = c v v^T has RANK ONE, a
    Hubbard-Stratonovich transform on the single direction v reduces the N-dim
    integral to ONE dimension in which tetrahedron i enters as the Fourier
    transform of psi at v_i times the auxiliary variable — i.e. a one-dimensional
    integral of quantum dilogarithms Phi_b(v_i t + shift_i) (DG (C.18), (C.25):
    the S-type generator acts by Fourier transform and the transform of the
    quantum dilogarithm is again a quantum dilogarithm times a Gaussian).
  SnapPy gluing_equations() docstring: rows  a b c  d e f ...  meaning
    a log z0 + b log(1/(1-z0)) + c log((z0-1)/z0) + ..., i.e. INTERLEAVED
    (z, z', z'') per tetrahedron; cusp rows (meridian, longitude) at the bottom.
  Quad-type change = cyclic relabelling (Z,Z',Z'') -> (Z',Z'',Z) per tetrahedron.

What is computed (exact integers / rationals, no floats):
  for K in {4_1 = m004, 5_2 = m015, (-2,3,7) = m016 = K12n242}, for every quad
  choice (3^N): (A, B, nu); det B; when det B != 0 the rank of B^{-1}A, its
  symmetry (the (2.9) check), and for rank one the factorisation c v v^T with v
  primitive integer.

Gates (derived structure must match the two knots whose one-dimensional state
integrals are printed in held text):
  G1  4_1: some quad gives rank one with v = (1,1), c = 1     — GK I_{1,2}: two Phi_b's
      of one variable, A = 1 = 1/c.
  G2  5_2: some quad gives rank one with v = (1,1,1), c = 1/2 — GK I_{2,3} / GGM
      (240): three Phi_b's of one variable, A = 2 = 1/c.
Test:
  T1  m016: some quad gives rank one (=> the pretzel's state integral IS
      one-dimensional); report v and c.  The RESULT is v = (1,1,2), c = 1/4: three
      quantum dilogarithms of ONE variable, one of them at DOUBLED argument.  That
      is outside both the GK I_{A,B} family and GGM's Z_{A,r} (all unit
      coefficients) — consistent with (a) the sister refutation (Part 9: every
      unit-coefficient member with the 5_2 configuration gives 5_2's index) and (b)
      GGM 2012.00062 §1.5's statement that the pretzel has level 2 (the doubled
      argument halves the pole spacing of that factor => q^{1/2}).
Scope: this fixes the SHAPE of the pretzel's one-dimensional integral (which
tetrahedron enters at which multiple of the auxiliary variable, and the Gaussian
coefficient).  The exact linear shifts and prefactor (from nu, the flattening f,
and the Fourier-transform constants) are the next step (Part 11), and the residue
evaluation to q-series blocks certified against the derived index (#7101 witness
via GGM eq 19) is the step after.  No q0, no float, no fit.
"""
from __future__ import annotations

import itertools
import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))

KNOTS = [("m004", "4_1", (1, 1), sp.Integer(1)),
         ("m015", "5_2", (1, 1, 1), sp.Rational(1, 2)),
         ("m016", "(-2,3,7) = K12n242", None, None)]


def rows_of(G):
    try:
        return [[int(v) for v in row] for row in G]
    except TypeError:
        return [[int(v) for v in row] for row in G.list()]


def nz_datum(Gm, n, quad):
    """DG (2.7)-(2.8) from SnapPy's interleaved log-form matrix, for a quad choice."""
    cols = lambda k: [3 * i + k for i in range(n)]
    Gz, Gzp, Gzpp = sp.zeros(n + 2, n), sp.zeros(n + 2, n), sp.zeros(n + 2, n)
    for i in range(n):
        s = quad[i]
        Gz[:, i] = Gm[:, cols(s % 3)[i]]
        Gzp[:, i] = Gm[:, cols((s + 1) % 3)[i]]
        Gzpp[:, i] = Gm[:, cols((s + 2) % 3)[i]]
    rows = list(range(n - 1)) + [n]                      # first N-1 edges + meridian
    A = (Gz - Gzp)[rows, :]
    B = (Gzpp - Gzp)[rows, :]
    nu = sp.Matrix([2 - sum(Gzp[i, :]) for i in range(n - 1)] + [-sum(Gzp[n, :])])
    return A, B, nu


def rank_one_factor(Q):
    n = Q.shape[0]
    col = [j for j in range(n) if any(Q[:, j])][0]
    v = Q[:, col] / Q[col, col]
    g = sp.gcd([sp.nsimplify(x) for x in v])
    v = (v / g).applyfunc(sp.nsimplify)
    c = sp.nsimplify(Q[col, col] / (v[col] ** 2))
    assert Q == c * v * v.T
    return c, v


def main():
    t0 = time.time()
    import snappy
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    results = {}
    for name, label, v_expect, c_expect in KNOTS:
        M = snappy.Manifold(name)
        n = M.num_tetrahedra()
        Gm = sp.Matrix(rows_of(M.gluing_equations()))
        print(f"\n== {name} = {label}: N = {n} tetrahedra, {M.solution_type()}")
        table = {}
        rank_one = []
        all_symplectic = True
        for quad in itertools.product(range(3), repeat=n):
            A, B, nu = nz_datum(Gm, n, quad)
            all_symplectic &= (A * B.T == B * A.T)
            d = B.det()
            if d == 0:
                table["singular"] = table.get("singular", 0) + 1
                continue
            Q = B.inv() * A
            r = Q.rank()
            key = f"rank{r}" + ("" if Q == Q.T else "-ASYM")
            table[key] = table.get(key, 0) + 1
            if r == 1:
                c, v = rank_one_factor(Q)
                rank_one.append({"quad": list(quad), "A": [[int(x) for x in r] for r in A.tolist()], "B": [[int(x) for x in r] for r in B.tolist()], "nu": [int(x) for x in nu.T.tolist()[0]],
                                 "detB": int(d), "c": str(c), "v": [int(x) for x in v],
                                 "Binv_nu": [str(x) for x in (B.inv() * nu)]})
        print(f"   quad table: {table}; (2.9) A B^T = B A^T for every quad: {all_symplectic}")
        for r1 in rank_one:
            print(f"   RANK ONE at quad {r1['quad']}: B^-1 A = {r1['c']} v v^T, v = {r1['v']}, det B = {r1['detB']}, "
                  f"A = {r1['A']}, B = {r1['B']}, nu = {r1['nu']}, B^-1 nu = {r1['Binv_nu']}")
        results[name] = {"label": label, "N": n, "quad_table": table, "symplectic_all_quads": bool(all_symplectic),
                         "rank_one": rank_one}
        check(f"{name}-(2.9)-symplectic-identity-holds-for-all-{3**n}-quad-choices", all_symplectic)
        if v_expect is not None:
            hit = [r1 for r1 in rank_one if tuple(r1["v"]) == v_expect and sp.nsimplify(r1["c"]) == c_expect]
            check(f"{name}-rank-one-quad-exists-with-v={v_expect}-c={c_expect} (GK/GGM one-dimensional form, A = 1/c)",
                  bool(hit), found=[[r["quad"], r["v"], r["c"]] for r in rank_one])
        else:
            check(f"{name}-rank-one-quad-EXISTS (the pretzel state integral is one-dimensional)", bool(rank_one),
                  found=[[r["quad"], r["v"], r["c"]] for r in rank_one])
            if rank_one:
                vs = sorted(set(tuple(r["v"]) for r in rank_one))
                check("m016-rank-one-factor-vector-is-(1,1,2) — one quantum dilogarithm at DOUBLED argument (level 2), "
                      "outside the unit-coefficient GK/GGM families", vs == [(1, 1, 2)], vectors=[list(v) for v in vs],
                      c=[r["c"] for r in rank_one])
                check("m016-exactly-one-quad-choice-is-rank-one (as for 5_2)", len(rank_one) == 1, count=len(rank_one))

    verdict = ("DERIVED (DG 2.7 + SnapPy): the pretzel's NZ Gaussian B^-1 A is rank one for exactly one quad "
               "choice, with factor vector v = (1,1,2) and c = 1/4, against v = (1,1,1), c = 1/2 for 5_2 and "
               "v = (1,1), c = 1 for 4_1 (both gates reproduce the printed one-dimensional forms, A = 1/c). So the "
               "pretzel's state integral IS one-dimensional — three quantum dilogarithms of one variable, one at "
               "doubled argument — which is outside the unit-coefficient GK I_{A,B} / GGM Z_{A,r} families. That "
               "is why the (1,3) sister candidate failed (Part 9) and matches GGM's 'level 2'. Next: the exact "
               "shifts and prefactor (nu, flattening, Fourier constants), then residues -> q-series blocks -> "
               "certification against the derived index via GGM eq 19.")
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    w = {
        "name": "aomega-m3-pretzel-nz-rank-one",
        "description": "Rank of the Neumann-Zagier Gaussian B^-1 A (DG 1202.6268 eq 2.7) over all quad choices for "
                       "4_1, 5_2 and (-2,3,7) from SnapPy; the pretzel is rank one with factor vector (1,1,2).",
        "computation": "aomega-m3-pretzel-nz-rank-one", "engine": "python+snappy",
        "scriptFile": os.path.basename(__file__),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
        "auditDoc": "docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md",
        "parameters": {"snappy_version": snappy.__version__, "row_choice": "first N-1 edges + meridian (DG 2.7)",
                       "column_convention": "SnapPy interleaved (z, z', z'') per tetrahedron (docstring)",
                       "quad_change": "cyclic relabelling per tetrahedron, all 3^N enumerated"},
        "data": results, "verdict": verdict, "assertions": assertions,
    }
    _WB.stamp_staleness_metadata(w, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pretzel-nz-rank-one.witness.json")
    with open(out, "w") as fh:
        json.dump(w, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
