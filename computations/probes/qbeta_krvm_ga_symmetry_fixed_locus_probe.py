#!/usr/bin/env python3
"""qbeta_krvm_ga_symmetry_fixed_locus_probe.py — bean qou-krvm: the coordinate
symmetry group of each anchor's generalised-angle polytope, and its fixed locus.

WHY. `SymmetricOptimum.optima_coincide` (PR #4513, sorry-free) explains the
measured `||x_geom - x_LP|| ~ 1e-16` at both anchors, but its hypotheses were
never discharged for the actual manifolds. Bean qou-krvm lists them; (i) is
"the polytope is stable under a symmetry group acting linearly" and (ii) is
"the symmetric point is UNIQUE". This probe settles (i) and (ii) for both
anchors, exactly, in rational arithmetic.

THE RESULT IS AN ASYMMETRY THE BEAN DID NOT ANTICIPATE.

    m004 (4_1, muon)     |Sym| = 4     fixed locus = a LINE   -> (ii) FALSE
    L6a4 (Borromean, p)  |Sym| = 16    fixed locus = a POINT  -> (ii) TRUE

So the two anchors are NOT explained the same way:

  * For **L6a4** the hypotheses (i)+(ii) both hold, and the unique symmetric
    point is exactly the regular ideal OCTAHEDRON point (angles 1/4, 1/4, 1/2
    per tetrahedron). `symmetric_point_optimal` applies directly: the vanishing
    offset at the proton anchor is forced by symmetry ALONE.

  * For **m004** it is not. The fixed locus is the line
    (t, 1-2t, t, 1-2t, t, t), so symmetry cuts 3 dimensions to 1 but does not
    pin the point; the Casson-Rivin objective has to finish the job on that
    line, where min(t, 1-2t) is uniquely maximised at t = 1/3 (the regular
    ideal TETRAHEDRON). Proved sorry-free in QOU/Knot/M004AngleStructure.lean.

METHOD (exact, no floats).
  * Constraint data via the corpus's own `gluing` / `ga_equalities`
    (borromean_angle_structure_lp_probe) on SnapPy's triangulations — the same
    system the LP was solved against, not re-derived.
  * m004 (6 vars): EXHAUSTIVE search over all 720 coordinate permutations, so
    the order-4 group is complete, not a lucky subgroup.
  * L6a4 (24 vars): 24! is infeasible, so candidates come from label-preserving
    automorphisms of the bipartite variable-constraint graph (edge label =
    coefficient, constraint node typed by RHS so tet rows cannot map to edge
    rows). Every candidate is then VERIFIED against the algebra by comparing
    rref of the augmented system — the graph is a candidate generator, never
    the authority.
  * Invariance test: {Ax=b} is sigma-invariant iff rref([A P | b]) == rref([A | b]).
  * Fixed locus: adjoin x_i - x_{sigma(i)} = 0 for every group element and solve
    exactly (sympy Rational). Free-parameter count 0 <=> unique symmetric point.

SCOPE (STRICT). This derives no value of A_omega and proposes no theta. It
reports two structural facts about the polytopes and nothing is wired. The
positivity constraints are permutation-invariant, so they play no role in the
symmetry determination and are not imposed here.

Run: python3 -u computations/probes/qbeta_krvm_ga_symmetry_fixed_locus_probe.py \
       2>&1 | tee /tmp/qbeta_krvm_ga_symmetry.log
"""
from __future__ import annotations

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

ANCHORS = [("muon", "m004", "4_1 figure-eight"),
           ("proton", "L6a4", "Borromean rings")]


def constraints(snappy, name):
    from borromean_angle_structure_lp_probe import gluing, ga_equalities
    _M, N, _r, edge_rows, _cusp = gluing(snappy, name)
    A, b = ga_equalities(N, edge_rows)
    return N, A, b


def _rref_aug(Am, bm):
    return Am.row_join(bm).rref()[0]


def symmetries(A, b, n, exhaustive):
    """Coordinate permutations preserving {Ax = b}, verified algebraically."""
    from sympy import Matrix
    Am, bm = Matrix(A), Matrix(b)
    ref = _rref_aug(Am, bm)

    def preserves(s):
        P = Matrix([[1 if s[i] == j else 0 for j in range(n)] for i in range(n)])
        return _rref_aug(Am * P, bm) == ref

    if exhaustive:
        cands = itertools.permutations(range(n))
    else:
        import networkx as nx
        from networkx.algorithms import isomorphism
        G = nx.Graph()
        for j in range(n):
            G.add_node(("v", j), kind="var")
        for i, rhs in enumerate(b):
            G.add_node(("c", i), kind=f"con{rhs}")
        for i, row in enumerate(A):
            for j, co in enumerate(row):
                if co:
                    G.add_edge(("c", i), ("v", j), w=int(co))
        gm = isomorphism.GraphMatcher(
            G, G,
            node_match=isomorphism.categorical_node_match("kind", None),
            edge_match=isomorphism.categorical_edge_match("w", None))
        cands = {tuple(a[("v", j)][1] for j in range(n))
                 for a in gm.isomorphisms_iter()}
    return sorted(s for s in cands if preserves(s))


def fixed_locus(A, b, n, syms):
    """Exact fixed locus of the group inside {Ax=b}: (free-param count, a point)."""
    from sympy import Matrix
    rows, rhs = [list(r) for r in A], list(b)
    for s in syms:
        for i in range(n):
            if s[i] != i:
                rr = [0] * n
                rr[i] = 1
                rr[s[i]] -= 1
                rows.append(rr)
                rhs.append(0)
    Fa, Fb = Matrix(rows), Matrix(rhs)
    sol, params = Fa.gauss_jordan_solve(Fb)
    pt = sol.subs({p: 0 for p in params})
    return len(params), [str(x) for x in pt]


def main() -> int:
    import snappy

    out = {}
    for anchor, name, desc in ANCHORS:
        N, A, b = constraints(snappy, name)
        n = 3 * N
        exhaustive = n <= 9
        syms = symmetries(A, b, n, exhaustive)
        free, pt = fixed_locus(A, b, n, syms)
        out[anchor] = {
            "manifold": name, "description": desc, "tetrahedra": N,
            "variables": n, "constraints": len(A),
            "search": "exhaustive over all coordinate permutations" if exhaustive
                      else "graph-automorphism candidates, each verified algebraically",
            "symmetry_order": len(syms),
            "generators_sample": [list(s) for s in syms[:4]],
            "fixed_locus_free_params": free,
            "fixed_locus_is_unique_point": free == 0,
            "fixed_point": pt,
        }
        print(f"\n═══ {anchor}: {name} ({desc})")
        print(f"    {n} vars, {len(A)} constraints, {N} tetrahedra")
        print(f"    |Sym| = {len(syms)}   ({out[anchor]['search']})")
        print(f"    fixed-locus free params = {free}"
              f"  →  {'UNIQUE symmetric point' if free == 0 else 'NOT unique'}")
        print(f"    fixed point = {pt}")

    m, p = out["muon"], out["proton"]
    verdict = (
        "THE TWO ANCHORS ARE NOT EXPLAINED THE SAME WAY. Bean qou-krvm's "
        "hypothesis (ii) — 'the symmetric point is UNIQUE' — is FALSE for the "
        f"muon anchor and TRUE for the proton anchor. m004 has |Sym| = "
        f"{m['symmetry_order']} with a {m['fixed_locus_free_params']}-parameter "
        "fixed locus (a LINE), so symmetry cuts 3 dimensions to 1 but does not "
        "pin the point; the Casson-Rivin objective finishes on that line, where "
        "min(t, 1-2t) is uniquely maximised at t = 1/3, the regular ideal "
        "TETRAHEDRON (proved sorry-free, QOU/Knot/M004AngleStructure.lean). "
        f"L6a4 has |Sym| = {p['symmetry_order']} with a UNIQUE symmetric point, "
        "exactly the regular ideal OCTAHEDRON point (1/4, 1/4, 1/2 per tet), so "
        "there (i) and (ii) both hold and `symmetric_point_optimal` applies "
        "directly — the vanishing offset at the proton anchor is forced by "
        "SYMMETRY ALONE. Exact rational arithmetic throughout; the m004 group is "
        "complete (exhaustive over all 720 permutations) and every L6a4 "
        "graph-automorphism candidate was verified against the algebra. Scope "
        "(a): no A_omega derived, no theta proposed, nothing wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-krvm-ga-symmetry-fixed-locus", engine="sympy")
    wb.set_description(
        "Bean qou-krvm hypotheses (i) and (ii) for both anchors' generalised-angle "
        "polytopes, in exact rational arithmetic. (i) holds for both. (ii) is "
        "FALSE for m004 (fixed locus is a line) and TRUE for L6a4 (unique "
        "symmetric point = the regular ideal octahedron point). So the proton "
        "anchor's vanishing offset is forced by symmetry alone, while the muon "
        "anchor needs the Casson-Rivin objective on the fixed line. Constraint "
        "data via the corpus's own gluing/ga_equalities on SnapPy. Nothing wired.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("anchors", out)
    wb.add_data("hypothesis_ii_holds", {"muon": m["fixed_locus_is_unique_point"],
                                        "proton": p["fixed_locus_is_unique_point"]})
    wb.add_data("method", "rref of augmented system for invariance; adjoin "
                          "x_i - x_sigma(i) = 0 for the fixed locus; sympy Rational")
    wb.add_data("verdict", verdict)
    wb.add_assertion("m004_symmetry_group_nontrivial",
                     computed=str(m["symmetry_order"]), expected="4",
                     tolerance="0.5",
                     source="exhaustive over all 720 coordinate permutations")
    wb.add_assertion("m004_symmetric_point_NOT_unique_hypothesis_ii_fails",
                     computed="0" if m["fixed_locus_is_unique_point"] else "1",
                     expected="1", tolerance="0.5",
                     source="fixed locus is the line (t, 1-2t, t, 1-2t, t, t)")
    wb.add_assertion("L6a4_symmetric_point_IS_unique_hypothesis_ii_holds",
                     computed="1" if p["fixed_locus_is_unique_point"] else "0",
                     expected="1", tolerance="0.5",
                     source="fixed locus is the single regular ideal octahedron "
                            "point (1/4, 1/4, 1/2 per tetrahedron)")
    wb.save()
    print("  witness -> computations/probes/"
          "qbeta-krvm-ga-symmetry-fixed-locus.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
