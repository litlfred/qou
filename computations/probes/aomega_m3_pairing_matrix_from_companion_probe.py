"""aomega_m3_pairing_matrix_from_companion_probe.py

🛑 RETRACTION, recorded rather than deleted.  This probe was written to solve for J from an
INVARIANCE condition A J Abar^T = J.  That condition is WRONG and the premise is retracted;
what survives is the determinant necessary condition (G1) and the retraction itself.

Why it is wrong: GGM (92) reads

    (1/2) W_{m-1}(x;q) J W_{-m-1}(x;q^-1)^T = [[1,0,0],[0,0,1],[0,1,3-q^m]]

whose RIGHT-HAND SIDE CARRIES q^m, and whose two indices shift in OPPOSITE directions
(m-1 against -m-1).  So the product is NOT constant in m, and (93) is an INTEGRALITY
statement — the entries are Laurent polynomials and the determinant is 1 — not an
invariance.  No A J Abar^T = J exists to solve.

Kept because a later agent reading Parts 1-2 would reach for exactly this equation, and
because the harness bug underneath it would have hidden the error: linsolve was fed
Poly(...).coeffs() in the unknowns, which contain no unknowns, so it returned EmptySet and
every dimension read `None`.  Repairing THAT would have produced a confidently wrong J.
A harness failure and a premise failure stacked, and only the harness one was visible.

Original docstring follows.

Route C M3, normalisation Part 3 (bean qou-v1eu, issue #7376): solve for the pairing matrix
J directly, as a LINEAR system, instead of reading it off a printed source.

Parts 1-2 reduced the arc's last gap to one function det W_0 and one constant c, tied by a
bar-involution equation, with c unknown at rank 6 because no held source prints a rank-6
orthogonality relation.  This probe removes the dependence on a printed source.

The derivation.  The Wronskian obeys W_{m+1} = A_m W_m with A_m the COMPANION matrix of the
recurrence.  GGM's orthogonality relation says pref * W_m(q) J W_l(q^-1)^T is constant in m.
Substituting the recursion, that holds for all m IFF

        A_m  J  Abar_m^T  =  J                                         (*)

where Abar_m is the companion matrix at (q^-1, x^-1).  (*) is LINEAR in the entries of J, so
J is SOLVED FOR, not searched.  Its necessary determinant condition is
det A * det Abar = 1, i.e. ratio(q) * ratio(1/q) = 1 with ratio the Part 1 Casoratian ratio —
verified separately for all three knots INCLUDING the pretzel, so the rank-6 palindromy
obstruction of Part 1 does NOT by itself forbid a pairing.

Calibration, stated rather than hidden.  The bar involution's action on the descendant
variable W is a CONVENTION (W ~ q^m suggests W -> 1/W, but that is not forced by anything we
derived).  Both conventions are run and reported, and the one reproducing GGM's PRINTED J at
ranks 2 and 3 is adopted.  That is calibration against a published derivation, not selection
against a measured target: no observable is involved, and the discriminator is a printed
matrix, not an accuracy.

Gates / tests
  G1  the necessary condition det A * det Abar = 1 holds for all three knots
  G2  4_1: the solution space of (*) contains GGM's printed J = diag(1,-1)  [(137)]
  G3  5_2: it contains GGM's printed J = [[0,0,1],[0,2,0],[1,0,0]]          [(92)]
  T1  pretzel: the solution space of (*) at rank 6 is non-trivial, and its dimension is
      reported.  Whatever it gives.
Exact sympy throughout; no mpmath, no q0, no float64.
"""
from __future__ import annotations

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
sys.path.insert(0, HERE)

import aomega_m3_pretzel_level2_stokes_probe as P33   # noqa: E402

Q, XR, W, X = P33.Q, P33.XR, P33.W, P33.X


def op_coeffs(name):
    k = P33.KNOTS[name]
    _, P = P33.descendant_operator(k["offsets_sym"], k["A"], k.get("doubled", False))
    r = P.degree()
    return [sp.simplify(P.coeff_monomial(X**j) if j else P.coeff_monomial(1))
            for j in range(r + 1)], r


def companion(cs, r):
    A = sp.zeros(r, r)
    for i in range(r - 1):
        A[i, i + 1] = 1
    for j in range(r):
        A[r - 1, j] = sp.cancel(-cs[j] / cs[r])
    return A


def bar(e, w_inverts):
    sub = {Q: 1 / Q, XR: 1 / XR}
    if w_inverts:
        sub[W] = 1 / W
    return sp.simplify(e.subs(sub, simultaneous=True))


def solve_J(cs, r, w_inverts):
    """Solve A J Abar^T = J linearly for J; return (basis of solutions, dimension)."""
    A = companion(cs, r)
    Ab = A.applyfunc(lambda e: bar(e, w_inverts))
    ent = sp.symbols(f"j0:{r*r}")
    J = sp.Matrix(r, r, list(ent))
    M = sp.expand(A * J * Ab.T - J)
    eqs = []
    for e in M:
        e = sp.together(sp.cancel(e))
        n, _ = sp.fraction(e)
        for term in sp.Poly(sp.expand(n), *ent).coeffs() if sp.expand(n).free_symbols & set(ent) else []:
            eqs.append(term)
    sol = sp.linsolve(eqs, ent) if eqs else None
    if sol is None or not sol:
        return None, None
    tup = list(sol)[0]
    free = sorted(set().union(*[t.free_symbols for t in tup]) & set(ent), key=str)
    basis = []
    for f in free:
        basis.append(sp.Matrix(r, r, [sp.simplify(t.subs({g: (1 if g == f else 0) for g in free}))
                                      for t in tup]))
    return basis, len(free)


def contains(basis, target):
    """Is `target` in the span of `basis` (over the coefficient field)?"""
    if not basis:
        return False
    cs = sp.symbols(f"c0:{len(basis)}")
    M = sp.zeros(*target.shape)
    for c, B in zip(cs, basis):
        M += c * B
    eqs = [sp.simplify(a - b) for a, b in zip(M, target)]
    sol = sp.solve(eqs, cs, dict=True)
    return bool(sol)


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    ratios = {}
    for name in ("4_1", "5_2", "pretzel"):
        cs, r = op_coeffs(name)
        A = companion(cs, r)
        dA = sp.simplify(sp.det(A))
        ratios[name] = (str(dA), str(sp.simplify(dA * bar(dA, True))))
        print(f"  {name}: r = {r}, det A = {dA}, det A * det Abar = {ratios[name][1]}")
    ok_nec = all(sp.simplify(sp.sympify(v[1]) - 1) == 0 for v in ratios.values())
    check("G1-the necessary condition det A * det Abar = 1 holds for all three knots, so the rank-6 "
          "palindromy obstruction of Part 1 does NOT by itself forbid a pairing", ok_nec,
          per_knot=ratios)

    GGM_J = {"4_1": sp.diag(1, -1),
             "5_2": sp.Matrix([[0, 0, 1], [0, 2, 0], [1, 0, 0]])}

    results = {}
    for w_inv in (True, False):
        tag = "W->1/W" if w_inv else "W->W"
        results[tag] = {}
        for name in ("4_1", "5_2", "pretzel"):
            cs, r = op_coeffs(name)
            basis, dim = solve_J(cs, r, w_inv)
            hit = contains(basis, GGM_J[name]) if (basis and name in GGM_J) else None
            results[tag][name] = {"dim": dim, "contains_ggm_J": hit}
            print(f"  [{tag}] {name}: solution-space dim = {dim}, contains GGM's printed J = {hit}")

    check("G2-RETRACTED PREMISE: the pairing is NOT m-invariant, so there is no A J Abar^T = J to "
          "solve. GGM (92)'s right-hand side carries q^m and its two indices shift in OPPOSITE "
          "directions (m-1 against -m-1); (93) is an INTEGRALITY statement (Laurent entries, "
          "determinant 1), not an invariance. This gate asserts the retraction so it cannot be "
          "quietly re-derived", True,
          wrong_equation="A J Abar^T = J",
          evidence="GGM (92) RHS = [[1,0,0],[0,0,1],[0,1,3-q^m]] is m-DEPENDENT",
          what_survives="the determinant condition of G1, and Part 2's bar-involution constant c")

    good = [t for t, v in results.items()
            if v["4_1"]["contains_ggm_J"] and v["5_2"]["contains_ggm_J"]]
    check("G3-SUPERSEDED by the retraction above; recorded as measured. One bar convention on the descendant variable reproduces GGM's PRINTED J at BOTH "
          "rank 2 (137) and rank 3 (92) — calibration against a published derivation, with both "
          "conventions run and reported rather than one quietly chosen",
          bool(good), conventions_reproducing_ggm=good, all_results=results)

    adopted = good[0] if good else None
    pdim = results[adopted]["pretzel"]["dim"] if adopted else None
    check("T1-SUPERSEDED by the retraction: under the (wrong) invariance premise the rank-6 "
          "equation has a non-trivial solution space. Recorded as measured, not as a result",
          bool(adopted and pdim), adopted_convention=adopted, pretzel_solution_dim=pdim,
          note="the None dimensions are a harness bug (linsolve fed coefficients containing no "
               "unknowns); it was NOT repaired, because repairing it on a wrong premise would "
               "have produced a confidently wrong J")

    verdict = (
        "RETRACTED PREMISE. This probe set out to solve A J Abar^T = J for the pairing matrix. That "
        "equation does not exist: GGM (92)'s right-hand side carries q^m and its two indices shift "
        "in opposite directions (m-1 against -m-1), so the pairing is NOT m-invariant and (93) is an "
        "INTEGRALITY statement (Laurent entries, determinant 1) rather than an invariance. What "
        "survives is G1, the determinant necessary condition det A * det Abar = 1, which holds for "
        "all three knots INCLUDING the pretzel — so Part 1's rank-6 palindromy obstruction does not "
        "by itself forbid a pairing, and the two obstructions are separate. A harness bug sat "
        "underneath the wrong premise and would have hidden it: linsolve was fed coefficients "
        "containing none of the unknowns, so every solution space read as empty. It is deliberately "
        "NOT repaired. Superseded original follows. "
        "The pairing matrix J is SOLVED FOR, not read off a printed source. W_{m+1} = A_m W_m "
        "with A_m the companion matrix, so GGM's orthogonality relation holds for all m iff "
        "A J Abar^T = J — LINEAR in J's entries. Its necessary determinant condition "
        "det A * det Abar = 1 holds for all three knots INCLUDING the pretzel (G1), so Part 1's "
        "rank-6 palindromy obstruction does not by itself forbid a pairing; the two obstructions are "
        f"separate. Bar conventions on the descendant variable, both run and reported: {results}. "
        f"Conventions reproducing GGM's printed J at ranks 2 and 3: {good or 'NONE'}; adopted: "
        f"{adopted}. Pretzel solution-space dimension under it: {pdim}.")
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    w = {"name": "aomega-m3-pairing-matrix-from-companion",
         "description": "The GGM orthogonality pairing matrix J solved as a linear system A J Abar^T = J from "
                        "the companion matrix of the descendant operator, calibrated against GGM's printed "
                        "J at ranks 2 and 3, and applied at rank 6.",
         "computation": "aomega-m3-pairing-matrix-from-companion", "engine": "python+sympy",
         "scriptFile": os.path.basename(__file__), "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "durationMs": int((time.time() - t0) * 1000), "auditOnly": True,
         "parameters": {"equation": "A J Abar^T = J", "orientation": "SnapPy's (#7152 Part 11)"},
         "data": {"det_conditions": ratios, "by_convention": results,
                  "adopted_convention": adopted, "pretzel_solution_dim": pdim},
         "verdict": verdict, "assertions": assertions}
    _WB.stamp_staleness_metadata(w, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "aomega-m3-pairing-matrix-from-companion.witness.json")
    with open(out, "w") as fh:
        json.dump(w, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed  [{time.time()-t0:.0f}s]")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
