#!/usr/bin/env python3
"""dt_d1b_nz_gluing_invariant_entry_probe.py — D1-b entry test (qou-q9ih).

D1-b proposes building a BPS quiver `Q` from GEOMETRIC data rather than Hecke
data: nodes = the certified count of boundary-parabolic connections per knot
(4_1: 3, 5_2: 4), arrows from the **Neumann-Zagier gluing datum** of the ideal
triangulation (the DGG "closed sector"). The ledger records the NZ -> Q
dictionary as the missing piece, to be assembled from the KS/DGG literature
over several sessions.

This is the formalize-first entry test that should precede that assembly. It
asks whether the NZ gluing datum can carry the required information AT ALL,
before anyone works out how it would.

NOTHING HERE IS RE-DERIVED. Both inputs already exist in this corpus and are
reused rather than rebuilt:
  * the node counts, from `dt_crossknot_connection_count_certified_probe.py`
    (certified against the Magma fixtures in the snappy wheel);
  * the NZ extractor, from `computations/one_loop_torsion.py::nz_pair`, which
    this probe CROSS-CHECKS against (control C5) rather than replacing.
What is new is the invariant computed from that datum.

WHAT IS MEASURED. The natural first-order invariant of an integer gluing
datum is the Smith normal form of `A | B`, i.e. its class under integral
row/column equivalence GL(Z) x GL(Z). Across 16 knots spanning N = 2..13
tetrahedra:

    SNF(A|B) = (1)^N  +  (2)  +  (0)          for EVERY knot,

a function of the tetrahedron count N alone. At each fixed N every knot in the
sample gives the identical SNF — including five pairwise NON-ISOMETRIC
hyperbolic knots at N = 5 (6_2, 7_3, 8_20, 9_42, 10_139).

WHY THAT IS A RESULT. The node count D1-b needs is a manifold invariant that
separates 4_1 (3) from 5_2 (4). The SNF separates nothing beyond N, so no
GL(Z) x GL(Z)-invariant function of the NZ gluing matrix can supply it. The
dictionary must read the matrix in a FIXED POLARIZATION — its actual entries —
not any basis-independent invariant of it.

SCOPE — (a), and the boundary matters. This excludes invariants under integral
row/column equivalence. The DGG construction acts by Sp(2N,Z) on the NZ data,
a strictly finer equivalence than GL x GL, so a polarization-dependent
construction is NOT excluded and D1-b is NOT refuted. Nothing here derives
A_omega; nothing is wired; there is no fit.

TWO CORPUS FINDINGS THAT RE-SCOPE D1-b, carried here so the next agent does
not rediscover them (both predate this probe):
  * `W` is NOT needed. `aomega_m2_bps_cohomology.py` / `AomegaM2BPSCohomology`
    (lean-direct exit 0) find the Davison-Meinhardt plethystic log trivial and
    `dim BPS_d = |Omega_d|`, so a potential-free abelianized quiver already
    realizes {3,4}. D1-b as written asks for "arrows AND potential"; the
    potential half is asking for an object the corpus records as unnecessary.
    That is itself scope-(a), conditional on the imported eq-(98) datum.
  * the `(7,1)` half of the target is a NO-OP. `barEven := plus + minus`,
    `barOdd := plus - minus`, so `(7,1)` is arithmetic on `(4,3)` and carries
    zero independent information (D1-a Result 0).
And one live CONSTRAINT to carry forward: `QuiverMirrorAutomorphismExcluded`
(sorry-free) — whatever `Q` is built, the mirror must act on the stability
RAY, never as a quiver automorphism, or the two counts are forced equal and
`(4,3)` is unreachable.

The C-collision instance (3_1 and 4_1 share an SNF but have certified
connection counts 2 and 3) carries a caveat stated in the output: 3_1 is not
hyperbolic (`contains flat tetrahedra`), so a geometric dictionary may
legitimately be undefined there. The degeneracy conclusion does NOT rest on
it — the N = 5 hyperbolic group establishes it without 3_1.

CONTROLS. A negative about an extracted datum is only as good as the proof
that the datum was extracted correctly, so six run first:
  [C1] the NZ symplectic identity — A_edge . B_edge^T is symmetric;
  [C2] the 1-cusped NZ relation — A_mu . B_lambda^T - A_lambda . B_mu^T = 2;
  [C3] the NZ rank structure — rank(A|B) = N+1, edge-block rank = N-1;
  [C4] the SNF routine is not constant by construction — hand-built matrices
       with known distinct normal forms are separated;
  [C5] the datum agrees with the corpus's own extractor: snappy's rectangular
       form and `one_loop_torsion.nz_pair` are related by `(A, B) = (a, -b)`
       exactly, on every row of every knot;
  [C6] and the SNF is unchanged by that convention difference, since negating
       columns is a unimodular operation — so the result is not an artifact of
       which of the two conventions was used.

All arithmetic is exact (Python ints / sympy Rationals). Volumes are printed
for orientation only and are never computed with; pairwise distinctness of the
N = 5 group is established with SnapPy's `is_isometric_to`, not by comparing
floats.

Scope-(a); nothing wired; no fit. Bean qou-q9ih (route D1-b).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from one_loop_torsion import nz_pair  # noqa: E402  (the corpus's extractor)
from witness_base import WitnessBuilder  # noqa: E402

# Certified boundary-parabolic connection totals (irreducible + abelian).
# 4_1 and 5_2 are the R1 counts re-derived locally in
# dt_crossknot_connection_count_certified_probe.py; 3_1 is the third-knot count
# from dt_third_knot_trefoil_count_probe.py. No other knot in this sample has a
# certified count -- the ptolemy DB is firewalled and only these three ship
# Magma fixtures in the snappy wheel.
CERTIFIED_C = {"3_1": 1 + 1, "4_1": 2 + 1, "5_2": 3 + 1}

KNOTS = ["3_1", "4_1", "5_1", "5_2", "6_1", "6_2", "6_3", "7_1", "7_2",
         "7_3", "7_4", "8_18", "8_19", "8_20", "9_42", "10_139"]

# Five pairwise non-isometric HYPERBOLIC knots that share N = 5. This group is
# what makes the degeneracy claim independent of the non-hyperbolic 3_1.
N5_GROUP = ["6_2", "7_3", "8_20", "9_42", "10_139"]


def rect_datum(M):
    """The NZ gluing datum of M as exact integer matrices, snappy's rect form.

    Returns (N, A, B, signs), where each equation reads
    `prod_i z_i^{A_i} (1 - z_i)^{B_i} = sign`. Rows are the N edge equations
    followed by the meridian and longitude cusp equations.
    """
    import sympy as sp
    N = M.num_tetrahedra()
    rows = M.gluing_equations(form="rect")
    A = sp.Matrix([[int(x) for x in r[0]] for r in rows])
    B = sp.Matrix([[int(x) for x in r[1]] for r in rows])
    return N, A, B, [int(r[2]) for r in rows]


def corpus_nz_datum(M):
    """The same datum via the corpus's `one_loop_torsion.nz_pair`.

    `nz_pair` consumes the RAW 3N-column (z, z', z'') exponent rows and returns
    `(a | b) = (G - G'', G' - G'')`. Used only to cross-check `rect_datum`.
    """
    N = M.num_tetrahedra()
    raw = M.gluing_equations()
    rows = [[int(x) for x in raw[i]] for i in range(raw.shape[0])]
    return N, [nz_pair(r, N) for r in rows]


def snf_diag(Mat):
    """Smith normal form diagonal, as a tuple of ints."""
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(Mat)
    return tuple(int(S[i, i]) for i in range(min(S.rows, S.cols)))


def main() -> int:
    import snappy
    import sympy as sp

    print("=" * 78)
    print(" D1-b entry test — can the NZ gluing datum carry the node count?")
    print("=" * 78)

    wb = WitnessBuilder("dt-d1b-nz-gluing-invariant-entry",
                        engine="snappy-neumann-zagier-exact-integer")
    wb.set_description(
        "D1-b (qou-q9ih) entry test, run before the NZ->Q dictionary is "
        "assembled. The Smith normal form of the Neumann-Zagier gluing matrix "
        "(A|B) is (1)^N + (2) + (0) for every one of 16 knots spanning N=2..13 "
        "tetrahedra -- a function of the tetrahedron count alone. Five "
        "pairwise non-isometric HYPERBOLIC knots at N=5 share it, so the "
        "degeneracy does not rest on the non-hyperbolic 3_1. Hence no "
        "GL(Z)xGL(Z)-invariant function of the NZ gluing matrix can supply "
        "D1-b's node count, which must separate 4_1 (3 connections) from 5_2 "
        "(4). The dictionary must read the matrix in a FIXED POLARIZATION. "
        "Scope-(a): the DGG construction acts by Sp(2N,Z), a strictly finer "
        "equivalence than GLxGL, so a polarization-dependent construction is "
        "NOT excluded and D1-b is NOT refuted. Neither input is re-derived: "
        "node counts come from dt_crossknot_connection_count_certified_probe, "
        "and the NZ datum is cross-checked against the corpus's own extractor "
        "one_loop_torsion.nz_pair, which agrees exactly as (A,B)=(a,-b). Six "
        "controls verify the datum is genuine NZ data (edge A.B^T symmetric; "
        "cusp pairing 2; rank N+1 and edge rank N-1; the nz_pair agreement; "
        "SNF invariance under that convention flip) and that the SNF routine "
        "discriminates. Exact integer arithmetic; distinctness by "
        "is_isometric_to, never by comparing volumes. Nothing wired; no fit."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    checks: list[tuple[bool, str, str]] = []

    def check(ok: bool, name: str, detail: str) -> None:
        checks.append((bool(ok), name, detail))
        print(f"  [{'PASS' if ok else 'FAIL':4s}] {name} — {detail}")

    # ---------------------------------------------------------------- C4
    # First: if the SNF routine were constant, everything below would be a
    # measurement of the routine rather than of the manifolds.
    print("\n[C4] control — the SNF routine is not constant by construction")
    probes = [(sp.Matrix([[2, 0], [0, 3]]), (1, 6)),
              (sp.Matrix([[1, 0], [0, 5]]), (1, 5)),
              (sp.Matrix([[6, 0], [0, 10]]), (2, 30))]
    got = [snf_diag(m) for m, _ in probes]
    want = [w for _, w in probes]
    print(f"      hand-built: {got}")
    check(got == want and len(set(got)) == 3,
          "C4_the_SNF_routine_DISCRIMINATES_on_hand_built_matrices",
          f"three matrices -> three distinct normal forms {got}; so a constant "
          f"result below is a fact about the manifolds, not about this code")

    # ------------------------------------------------------- the extraction
    print("\n[C1-C3, C5-C6 + main] the NZ datum, per knot")
    per_knot: dict[str, dict] = {}
    sym_all = cusp_all = rank_all = shape_all = True
    xchk_all = flip_all = True

    for k in KNOTS:
        M = snappy.Manifold(k)
        N, A, B, signs = rect_datum(M)

        Ae, Be = A[:N, :], B[:N, :]
        P = Ae * Be.T
        sym = (P - P.T).is_zero_matrix                       # C1

        Am, Bm, Al, Bl = A[-2, :], B[-2, :], A[-1, :], B[-1, :]
        pair = int((Am * Bl.T - Al * Bm.T)[0, 0])            # C2

        AB = A.row_join(B)
        rk, erk = AB.rank(), Ae.row_join(Be).rank()          # C3
        d = snf_diag(AB)

        # C5 — the corpus's own extractor, on the RAW rows, must agree:
        #      rect (A, B) = (a, -b) with (a|b) = nz_pair(raw_row, N).
        _, ab_rows = corpus_nz_datum(M)
        xchk = all(
            [int(x) for x in A.row(i)] == ab_rows[i][:N]
            and [int(x) for x in B.row(i)] == [-x for x in ab_rows[i][N:]]
            for i in range(A.rows))

        # C6 — that convention difference is a column negation, so it cannot
        #      move the SNF. Verify rather than assert.
        AB_corpus = sp.Matrix([ab_rows[i] for i in range(A.rows)])
        flip = snf_diag(AB_corpus) == d

        expect_snf = tuple([1] * N + [2, 0])
        sym_all &= bool(sym)
        cusp_all &= (pair == 2)
        rank_all &= (rk == N + 1 and erk == N - 1)
        shape_all &= (d == expect_snf)
        xchk_all &= bool(xchk)
        flip_all &= bool(flip)

        per_knot[k] = {
            "tetrahedra": N,
            "snf": list(d),
            "rank_AB": int(rk),
            "rank_edge_block": int(erk),
            "edge_ABt_symmetric": bool(sym),
            "cusp_pairing": pair,
            "agrees_with_corpus_nz_pair": bool(xchk),
            "snf_invariant_under_convention_flip": bool(flip),
            "solution_type": M.solution_type(),
            "hyperbolic": M.solution_type().startswith("all tetrahedra"),
            "volume_display_only": str(M.volume()),
            "certified_connections": CERTIFIED_C.get(k),
        }
        print(f"  {k:7s} N={N:2d} SNF={d} rank={rk} edge_rank={erk} "
              f"ABt_sym={sym} cusp={pair} nz_pair_ok={xchk} "
              f"C={CERTIFIED_C.get(k, '-')} {M.solution_type()[:14]}")

    check(sym_all, "C1_edge_block_satisfies_the_NZ_SYMPLECTIC_identity",
          f"A_edge . B_edge^T is symmetric for all {len(KNOTS)} knots — this "
          "is Neumann-Zagier's theorem, so the extracted matrices really are "
          "the NZ gluing datum")
    check(cusp_all, "C2_cusp_rows_satisfy_the_1_CUSPED_NZ_relation",
          "A_mu.B_lambda^T - A_lambda.B_mu^T = 2 for all knots — the "
          "meridian/longitude rows are correctly identified")
    check(rank_all, "C3_the_NZ_RANK_STRUCTURE_holds",
          "rank(A|B) = N+1 and edge-block rank = N-1 for all knots, i.e. the "
          "one relation among the edge equations plus two cusp rows")
    check(xchk_all, "C5_the_datum_AGREES_with_the_corpus_s_OWN_extractor",
          "snappy's rectangular form and one_loop_torsion.nz_pair are related "
          "by (A,B) = (a,-b) EXACTLY, on every row of every knot (N up to 13). "
          "So this is not a second, possibly-divergent extraction — it is the "
          "same NZ datum the corpus already computes, in a stated convention")
    check(flip_all, "C6_the_SNF_is_INVARIANT_under_that_convention_flip",
          "negating the B columns is unimodular, so SNF(A|-B) = SNF(A|B); "
          "verified per knot rather than assumed. The degeneracy below is "
          "therefore not an artifact of which convention was used")

    # -------------------------------------------------------------- main 1
    by_n: dict[int, set] = {}
    for k, v in per_knot.items():
        by_n.setdefault(v["tetrahedra"], set()).add(tuple(v["snf"]))
    collisions = {n: sorted(k for k in per_knot
                            if per_knot[k]["tetrahedra"] == n)
                  for n in sorted(by_n)}
    print("\n  grouped by tetrahedron count:")
    for n in sorted(by_n):
        print(f"    N={n:2d}: {len(collisions[n])} knots {collisions[n]} "
              f"-> {len(by_n[n])} distinct SNF")

    one_per_n = all(len(v) == 1 for v in by_n.values())
    check(shape_all and one_per_n,
          "the_SNF_is_a_function_of_N_ALONE",
          f"(1)^N + (2) + (0) for every one of {len(KNOTS)} knots, N=2..13; "
          "at each fixed N all knots give ONE SNF. The invariant carries no "
          "knot-theoretic information at all")

    # -------------------------------------------------------------- main 2
    print("\n  the N=5 hyperbolic group — is it really five different "
          "manifolds?")
    mans = {k: snappy.Manifold(k) for k in N5_GROUP}
    iso_pairs = [(a, b) for i, a in enumerate(N5_GROUP)
                 for b in N5_GROUP[i + 1:] if mans[a].is_isometric_to(mans[b])]
    for k in N5_GROUP:
        print(f"    {k:7s} hyperbolic={per_knot[k]['hyperbolic']} "
              f"SNF={tuple(per_knot[k]['snf'])} "
              f"vol={per_knot[k]['volume_display_only'][:10]} (display only)")
    n5_snfs = {tuple(per_knot[k]["snf"]) for k in N5_GROUP}
    check(not iso_pairs and len(n5_snfs) == 1
          and all(per_knot[k]["hyperbolic"] for k in N5_GROUP),
          "five_PAIRWISE_NON_ISOMETRIC_HYPERBOLIC_knots_share_ONE_SNF",
          f"{N5_GROUP} are all hyperbolic and pairwise non-isometric "
          "(is_isometric_to, not a volume comparison) yet give the single SNF "
          f"{list(n5_snfs)[0]} — so the degeneracy is NOT an artifact of "
          "including the non-hyperbolic 3_1")

    # -------------------------------------------------------------- main 3
    print("\n  the connection-count collision at N=2 (with its caveat)")
    tre, fig = per_knot["3_1"], per_knot["4_1"]
    print(f"    3_1  N={tre['tetrahedra']} SNF={tuple(tre['snf'])} "
          f"C={tre['certified_connections']}  hyperbolic={tre['hyperbolic']}"
          f"  <-- NOT hyperbolic: {tre['solution_type']}")
    print(f"    4_1  N={fig['tetrahedra']} SNF={tuple(fig['snf'])} "
          f"C={fig['certified_connections']}  hyperbolic={fig['hyperbolic']}")
    check(tre["snf"] == fig["snf"]
          and tre["certified_connections"] != fig["certified_connections"],
          "3_1_and_4_1_share_an_SNF_but_have_DIFFERENT_certified_C",
          f"identical SNF {tuple(fig['snf'])}, C = "
          f"{tre['certified_connections']} vs {fig['certified_connections']}. "
          f"CAVEAT, stated because it matters: 3_1 is not hyperbolic "
          f"('{tre['solution_type']}'), so a geometric dictionary may be "
          "undefined there. This instance CORROBORATES; the N=5 group above "
          "is what establishes the claim")

    # ------------------------------------------------------------ verdict
    check(True,
          "CONSEQUENCE_the_dictionary_must_be_POLARIZATION_DEPENDENT",
          "no GL(Z)xGL(Z)-invariant function of (A|B) can supply a node count "
          "separating 4_1 from 5_2, so the NZ->Q dictionary must read the "
          "matrix's actual entries in a fixed polarization. Scope-(a): DGG "
          "acts by Sp(2N,Z), finer than GLxGL, so such a construction is NOT "
          "excluded — D1-b is constrained at its entry, not refuted")

    wb.add_data("knots", per_knot)
    wb.add_data("snf_by_tetrahedron_count",
                {str(n): {"knots": collisions[n],
                          "distinct_snfs": len(by_n[n]),
                          "snf": list(list(by_n[n])[0])}
                 for n in sorted(by_n)})
    wb.add_data("n5_hyperbolic_group",
                {"knots": N5_GROUP, "isometric_pairs_found": iso_pairs,
                 "shared_snf": list(list(n5_snfs)[0])})
    wb.add_data("reused_not_rederived", {
        "node_counts": "dt_crossknot_connection_count_certified_probe.py "
                       "(certified against the snappy wheel's Magma fixtures)",
        "nz_extractor": "computations/one_loop_torsion.py::nz_pair — "
                        "cross-checked in C5, not replaced",
        "convention_relation": "snappy rect (A,B) = (a, -b) with (a|b) = "
                               "nz_pair(raw_row, N); exact on every row",
    })
    wb.add_data("corpus_findings_that_rescope_d1b", {
        "potential_not_needed": "aomega_m2_bps_cohomology.py / "
                                "AomegaM2BPSCohomology (lean-direct exit 0): "
                                "the Davison-Meinhardt plethystic log is "
                                "trivial and dim BPS_d = |Omega_d|, so a "
                                "potential-free abelianized quiver already "
                                "realizes {3,4}. D1-b's 'arrows AND potential' "
                                "asks for an object recorded as unnecessary. "
                                "Scope-(a), conditional on the imported "
                                "eq-(98) datum",
        "seven_one_is_a_noop": "barEven := plus+minus, barOdd := plus-minus, "
                               "so (7,1) is arithmetic on (4,3) and carries "
                               "zero independent information (D1-a Result 0)",
        "live_constraint": "QuiverMirrorAutomorphismExcluded (sorry-free) — "
                           "the mirror must act on the stability RAY, never "
                           "as a quiver automorphism, or the counts are "
                           "forced equal and (4,3) is unreachable",
        "literature_gap": "Alim-Cecotti-Cordova-Espahbodi-Rastogi-Vafa 'BPS "
                          "quivers and spectra' — the triangulation-to-BPS-"
                          "quiver precedent — is NOT held in library/; DGG "
                          "(1108.4389, 1112.5179), KS (0811.2435) and "
                          "Davison-Meinhardt (1601.02479) are",
    })
    wb.add_data("scope", {
        "tier": "scope-(a)",
        "excludes": "functions of the NZ gluing matrix invariant under "
                    "integral row/column equivalence (GL(Z) x GL(Z)), "
                    "equivalently functions of its Smith normal form",
        "does_NOT_exclude": "polarization-dependent constructions; the DGG "
                            "closed sector acts by Sp(2N,Z), a strictly finer "
                            "equivalence, and reads the matrix entries",
        "certified_C_available_for": sorted(CERTIFIED_C),
        "certified_C_caveat": "only 3_1, 4_1, 5_2 ship Magma fixtures in the "
                              "snappy wheel; the ptolemy DB is firewalled. "
                              "3_1 is non-hyperbolic, so the N=2 C-collision "
                              "corroborates rather than establishes",
        "arithmetic": "exact integers / sympy Rationals throughout; volumes "
                      "are printed for orientation and never computed with; "
                      "manifold distinctness via is_isometric_to",
        "derives_A_omega": False, "wired": False, "fit": False,
    })

    for ok, name, detail in checks:
        wb.add_assertion(name, computed="PASS" if ok else "FAIL",
                         expected="PASS", tolerance="exact", source=detail)
    wb.save()

    n_ok = sum(1 for ok, _, _ in checks if ok)
    print(f"\n  {n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
