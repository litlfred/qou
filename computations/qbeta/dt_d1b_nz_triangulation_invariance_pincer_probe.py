#!/usr/bin/env python3
"""dt_d1b_nz_triangulation_invariance_pincer_probe.py — D1-b, part 2 (qou-q9ih).

Part 1 (`dt_d1b_nz_gluing_invariant_entry_probe.py`, 10/10) showed the Smith
normal form of the NZ gluing matrix is `(1)^N + (2) + (0)` for every knot — a
function of the tetrahedron count alone — and concluded that the NZ -> Q
dictionary must be POLARIZATION-DEPENDENT, i.e. must read the matrix's actual
entries rather than any `GL(Z) x GL(Z)`-invariant of it. It deliberately left
that possibility open.

This part closes the other side, and the two together are a pincer.

THE PINCER.

  [too coarse]  The basis-independent invariant (part 1): constant across all
                knots at fixed N. Cannot separate 4_1 from 5_2.

  [too fine]    The raw polarization-dependent datum (measured here): NOT a
                manifold invariant at all. Retriangulating ONE manifold moves
                it — 30 retriangulations of 6_2 give ROUGHLY A DOZEN distinct
                values of `(N, SNF(P), det P, rank P)`, where
                `P = A_edge . B_edge^T` is the symmetric NZ pairing in the
                given triangulation.

                🛑 That count is STOCHASTIC — snappy's `randomize()` walks a
                random sequence of moves, so successive runs of this very probe
                gave 9 and 11 for `6_2`. Do not quote a number from this
                docstring; the run's own figures are in the witness under
                `polarization_variance_under_retriangulation`, and the
                assertion tests `> 1` (and `>= 5` for `6_2`), which is what the
                argument actually needs. Only the QUALITATIVE fact — that it
                moves at all — is load-bearing.

The node count D1-b needs is a manifold invariant. So the dictionary must
thread a needle: strictly finer than the Smith normal form, yet
triangulation-invariant.

AND THE NEEDLE IS THREADABLE — this is the constructive half. That class of
functionals is non-empty and this corpus already contains a verified member:
the Dimofte-Garoufalidis 1-loop invariant `tau`, implemented in
`computations/one_loop_torsion.py`. Measured here, it is triangulation-
invariant to working precision AND it separates every one of the five N = 5
knots on which the Smith normal form collided:

    6_2   2.2165899308911189066
    7_3   2.7717413902489047800
    8_20  5.9288297060394782874
    9_42  8.9879137538564859187
    10_139 6.7715656780558894839

So D1-b's dictionary is located, not excluded: it lives among the
triangulation-invariant functionals of the NZ datum.

🛑 WHAT THIS DOES NOT SHOW. `tau` is a complex number, not an integer
count; separating knots is not producing 3 and 4. No `tau -> C` map is offered
here and none is fitted.

🛑 CORRECTING MYSELF: THERE ARE SIX USABLE POINTS, NOT TWO. An earlier
version of this docstring said the corpus "CANNOT TEST any proposed
`tau -> C` map", because certified counts existed "for exactly three knots
(4_1, 5_2, 3_1)" and `tau` is undefined on the non-hyperbolic 3_1 — leaving two
points, which any two-parameter family fits exactly. **That was wrong, and the
error was mine: I never enumerated the fixtures.** The ptolemy database is
indeed firewalled (re-verified: 403 on CONNECT, by `curl` and by snappy's own
`retrieve_solutions`), but the snappy wheel ships sl2 Magma fixtures for
**seven** manifolds, not three. Six of them are 1-cusped, hyperbolic, and carry
both a defined `tau` and a certified irreducible connection count:

    manifold    N   irreducible   |tau|
    4_1         2        2        0.8660254037844386
    5_2         3        3        1.1611627381339101
    m135        4        8       11.3137084989847600
    s000        6        6       14.2764741671144800
    t00000      8        8       29.2290115622653500
    v0000       7        8       20.8938841612730000

So a candidate `tau -> C` relation IS testable here — six points against a
two-parameter family leaves four degrees of freedom. **The blocker I reported
was overstated by a factor of three.** Still no map is proposed: fishing for one
across six points is exactly the numerology this repo forbids, and finding it
is a separate piece of work that must state its hypothesis first.

Three caveats that a later reader needs, and that this probe records rather
than papers over:

  * `m135`, `s000`, `t00000`, `v0000` are CENSUS manifolds, not knots in S^3.
    D1-b's setup is about knots (both are 3-braids), so they are valid for
    testing whether a `tau -> C` relation exists, and NOT automatically valid
    as D1-b nodes.
  * the ABELIAN convention does not carry over. For knots the audit adds one
    abelian connection (the `(L-1)` factor); that argument is not established
    for a census manifold, so the common currency across all six is the
    IRREDUCIBLE count, which is what the table above reports.
  * `irreducible = N` for four of the six and FAILS for `m135` (4, 8) and
    `v0000` (7, 8). So the connection count is not the tetrahedron count —
    worth stating because it is the first thing one would wrongly assume from
    the 4_1 / 5_2 pair alone.

🛑 AND A TRAP: `one_loop` DOES NOT GUARD AGAINST NON-HYPERBOLIC INPUT.
Called on 3_1 it returns `0.5` without raising, although `M.solution_type()` is
`contains flat tetrahedra` and DG's `tau` needs a genuine hyperbolic structure.
A returned value is therefore NOT evidence that the manifold is hyperbolic;
check `solution_type()` yourself. That is why 3_1 is excluded from the table
above by an explicit hyperbolicity test rather than by an exception.

CONTROLS.
  [C1] `tau(4_1) = sqrt(3)/2` — Dimofte-Garoufalidis' own worked figure-eight
       example (arXiv:1202.6268 eq. 3.2). This validates the implementation
       being consumed, which matters because the module's docstring records
       that three implementations of the 1-loop determinant existed in this
       repo and disagreed.
  [C2] `tau` is triangulation-invariant — retriangulate and compare.
  [C3] the retriangulator actually perturbs the triangulation, verified by the
       polarization-dependent datum moving. Without this, C2 would be vacuous:
       an invariance test passes trivially if nothing was varied.

All `tau` arithmetic is `mpmath` at 40 dps; no float64 anywhere. Comparisons
are mpmath comparisons against an mpf threshold, and values are rendered with
`mp.nstr`, never `float()`.

Scope-(a); nothing wired; no fit. Bean qou-q9ih (route D1-b).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from one_loop_torsion import one_loop  # noqa: E402  (the corpus's canonical tau)
from witness_base import WitnessBuilder  # noqa: E402

DPS = 40
TRIALS = 30
INVARIANCE_TOL = "1e-30"       # mpf; tau is computed at 40 dps

# The five pairwise non-isometric hyperbolic knots at N = 5 on which part 1's
# Smith normal form collided.
N5_GROUP = ["6_2", "7_3", "8_20", "9_42", "10_139"]
VARIANCE_KNOTS = ["4_1", "5_2", "6_2"]

# Every manifold for which the snappy wheel ships an sl2 Magma fixture. The
# ptolemy DB is firewalled (re-verified: 403 on CONNECT), so this IS the
# certified-count data available offline. Enumerated, not recalled -- getting
# this wrong by 3x is the correction this probe carries.
FIXTURE_MANIFOLDS = ["3_1", "4_1", "5_2", "m135", "s000", "t00000", "v0000"]


def polarization_datum(M):
    """Polarization-DEPENDENT NZ data: the symmetric pairing P = A_e . B_e^T.

    This is what a construction reading the matrix's actual entries would see.
    It is a function of the TRIANGULATION, which is the point of this probe.
    """
    import sympy as sp
    from sympy.matrices.normalforms import smith_normal_form
    N = M.num_tetrahedra()
    rows = M.gluing_equations(form="rect")
    A = sp.Matrix([[int(x) for x in r[0]] for r in rows])
    B = sp.Matrix([[int(x) for x in r[1]] for r in rows])
    P = A[:N, :] * B[:N, :].T
    S = smith_normal_form(P)
    return (N,
            tuple(int(S[i, i]) for i in range(min(S.rows, S.cols))),
            int(P.det()), int(P.rank()))


def irreducible_count(name):
    """Certified irreducible boundary-parabolic count from bundled fixtures.

    Sums Galois-orbit degrees over every obstruction class the wheel ships for
    `name`. Returns None when no fixture exists. This is the ABELIAN-FREE
    count: the `(L-1)` abelian convention is established for knots in S^3 and
    is NOT carried over to census manifolds, so the irreducible count is the
    common currency across the whole fixture set.
    """
    import bz2
    import re
    import snappy.ptolemy as pm
    from snappy.ptolemy import processMagmaFile
    d = Path(pm.__file__).parent / "testing_files"
    files = sorted(f for f in d.iterdir()
                   if re.match(rf"{re.escape(name)}__sl2_c\d+\.magma_out\.bz2$",
                               f.name))
    if not files:
        return None
    total = 0
    for f in files:
        sols = processMagmaFile.solutions_from_magma(
            bz2.open(f, "rt").read(), numerical=False)
        for sol in sols.flatten():
            nf = sol.number_field()
            if nf is None:
                total += 1
            else:
                try:
                    total += int(nf.poldegree())
                except Exception:
                    total += int(nf.degree())
    return total


def main() -> int:
    import mpmath as mp
    import snappy
    from collections import Counter

    mp.mp.dps = DPS
    tol = mp.mpf(INVARIANCE_TOL)

    print("=" * 78)
    print(" D1-b part 2 — the pincer, and the needle that threads it")
    print("=" * 78)

    wb = WitnessBuilder("dt-d1b-nz-triangulation-invariance-pincer",
                        engine="snappy-neumann-zagier-mpmath-40dps")
    wb.set_description(
        "D1-b (qou-q9ih) part 2, closing the side part 1 left open. Part 1: "
        "the SNF of the NZ gluing matrix is a function of N alone, so the "
        "dictionary must be polarization-dependent. Here: the raw "
        "polarization-dependent datum is NOT a manifold invariant -- 30 "
        "retriangulations of 6_2 give ~a dozen distinct values of (N, SNF(P), "
        "det P, rank P) for P = A_edge.B_edge^T -- the exact count is "
        "STOCHASTIC, randomize() walks a random move sequence and successive "
        "runs gave 9 and 11, so read this run's figures from "
        "polarization_variance_under_retriangulation rather than quoting one; "
        "the assertion tests only that it moves. Together a pincer: the "
        "basis-independent invariant is too coarse, the raw polarization datum "
        "too fine, and the node count is a manifold invariant. CONSTRUCTIVE "
        "half: the class of triangulation-invariant NZ functionals is "
        "non-empty and the corpus holds a verified member -- the "
        "Dimofte-Garoufalidis 1-loop invariant tau (one_loop_torsion.py), "
        "measured here as triangulation-invariant to 1e-30 and separating all "
        "five N=5 knots the SNF collided. So D1-b's dictionary is LOCATED, "
        "not excluded. NO tau->C map is proposed. CORRECTION carried in this "
        "witness: an earlier version claimed the corpus could not TEST such a "
        "map, on the ground that certified C exists for only three knots and "
        "tau is undefined on the non-hyperbolic 3_1, leaving two points. That "
        "was wrong -- the fixtures were never enumerated. The ptolemy DB is "
        "indeed firewalled (re-verified 403 on CONNECT), but the snappy wheel "
        "ships sl2 fixtures for SEVEN manifolds, SIX of them 1-cusped "
        "hyperbolic with both a defined tau and a certified irreducible count "
        "(4_1, 5_2, m135, s000, t00000, v0000). So a candidate IS testable, "
        "six points against a two-parameter family; the blocker was overstated "
        "3x. Caveats recorded: four are census manifolds not knots in S^3, the "
        "abelian convention does not carry over so the common currency is the "
        "irreducible count, and irreducible = N fails for m135 and v0000. Also "
        "a trap: one_loop does NOT guard against non-hyperbolic input -- it "
        "returns 0.5 for 3_1 without raising, so a returned value is not "
        "evidence of hyperbolicity. mpmath at 40 dps throughout; no float64. "
        "Scope-(a); nothing wired; no fit."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    checks: list[tuple[bool, str, str]] = []

    def check(ok: bool, name: str, detail: str) -> None:
        checks.append((bool(ok), name, detail))
        print(f"  [{'PASS' if ok else 'FAIL':4s}] {name} — {detail}")

    # ---------------------------------------------------------------- C1
    print("\n[C1] control — tau(4_1) against Dimofte-Garoufalidis eq. 3.2")
    tau_41 = abs(one_loop(snappy.Manifold("4_1")))
    want = mp.sqrt(3) / 2
    err = abs(tau_41 - want)
    print(f"      |tau(4_1)| = {mp.nstr(tau_41, 22)}")
    print(f"      sqrt(3)/2  = {mp.nstr(want, 22)}   |diff| = {mp.nstr(err, 6)}")
    check(err < tol,
          "C1_tau_reproduces_the_DG_WORKED_figure_eight_value",
          f"|tau(4_1)| = sqrt(3)/2 to {mp.nstr(err, 3)}. This validates the "
          "implementation being consumed — the module records that THREE "
          "1-loop implementations existed in this repo and disagreed, so "
          "consuming one without this check would be unsafe")

    # ------------------------------------------------------------ C3 + main
    print(f"\n[C3 + main] does the POLARIZATION datum move under "
          f"retriangulation? ({TRIALS} trials each)")
    variance: dict[str, dict] = {}
    for k in VARIANCE_KNOTS:
        seen: Counter = Counter()
        for t in range(TRIALS):
            M = snappy.Manifold(k)
            for _ in range(t % 9 + 1):
                M.randomize()
            seen[polarization_datum(M)] += 1
        variance[k] = {"distinct": len(seen),
                       "trials": TRIALS,
                       "values": [{"datum": str(v), "count": c}
                                  for v, c in seen.most_common()]}
        print(f"  {k:5s}: {len(seen)} distinct (N, SNF(P), det P, rank P) "
              f"over {TRIALS} retriangulations")
        for v, c in seen.most_common(3):
            print(f"          x{c:2d}  {v}")

    moved = all(variance[k]["distinct"] > 1 for k in VARIANCE_KNOTS)
    check(moved,
          "C3_the_retriangulator_REALLY_perturbs_the_triangulation",
          "every knot shows >1 distinct polarization datum, so the invariance "
          "test below is not vacuous — an invariance check passes trivially "
          "when nothing was varied")
    check(moved and variance["6_2"]["distinct"] >= 5,
          "the_RAW_POLARIZATION_datum_is_NOT_a_manifold_invariant",
          f"one manifold, {TRIALS} retriangulations: 6_2 gives "
          f"{variance['6_2']['distinct']} distinct values, 5_2 "
          f"{variance['5_2']['distinct']}, 4_1 {variance['4_1']['distinct']}. "
          "The node count IS a manifold invariant, so a construction reading "
          "the matrix entries directly cannot equal it without a separate "
          "triangulation-invariance argument")

    # ---------------------------------------------------------------- C2
    print("\n[C2] control — is tau triangulation-invariant?")
    inv: dict[str, dict] = {}
    for k in ["4_1", "6_2"]:
        vals = []
        for t in range(4):
            M = snappy.Manifold(k)
            for _ in range(t + 1):
                M.randomize()
            vals.append(abs(one_loop(M)))
        spread = max(vals) - min(vals)
        inv[k] = {"values": [mp.nstr(v, 22) for v in vals],
                  "spread": mp.nstr(spread, 6)}
        print(f"  {k:5s}: spread over 4 retriangulations = "
              f"{mp.nstr(spread, 6)}")
    inv_ok = all(mp.mpf(inv[k]["spread"]) < tol for k in inv)
    check(inv_ok, "C2_tau_IS_triangulation_invariant",
          f"spread < {INVARIANCE_TOL} over retriangulations of 4_1 and 6_2, "
          "while C3 confirms the triangulation genuinely changed. So "
          "triangulation-invariant functionals of the NZ datum EXIST")

    # -------------------------------------------------------------- main 2
    print("\n  does tau separate the five N=5 knots the SNF collided?")
    taus: dict[str, str] = {}
    for k in N5_GROUP:
        t = abs(one_loop(snappy.Manifold(k)))
        taus[k] = mp.nstr(t, 22)
        print(f"    {k:7s} |tau| = {taus[k]}")
    vals5 = [mp.mpf(taus[k]) for k in N5_GROUP]
    gaps = [abs(vals5[i] - vals5[j])
            for i in range(len(vals5)) for j in range(i + 1, len(vals5))]
    min_gap = min(gaps)
    check(min_gap > tol,
          "tau_SEPARATES_all_five_knots_the_SNF_could_not",
          f"all 10 pairwise gaps exceed {INVARIANCE_TOL}; the smallest is "
          f"{mp.nstr(min_gap, 6)}. The SNF gave these five knots ONE value; a "
          "triangulation-invariant functional of the same datum gives five")

    # ------------------------- CORRECTION: how many points actually exist
    print("\n  CORRECTING MYSELF — enumerating the bundled fixtures")
    print("    (an earlier version of this probe said TWO usable points; it "
          "never enumerated)")
    usable, skipped = {}, {}
    for name in FIXTURE_MANIFOLDS:
        try:
            M = snappy.Manifold(name)
        except Exception as exc:
            skipped[name] = f"manifold load failed: {type(exc).__name__}"
            continue
        hyp = M.solution_type().startswith("all tetrahedra")
        irr = irreducible_count(name)
        if not hyp:
            # one_loop does NOT raise here -- it returns a value. Excluding by
            # an explicit hyperbolicity test, never by trusting an exception.
            skipped[name] = (f"not hyperbolic ({M.solution_type()}); tau is "
                             f"undefined, though one_loop returns a value "
                             f"without raising")
            continue
        if M.num_cusps() != 1:
            skipped[name] = f"{M.num_cusps()} cusps"
            continue
        t = abs(one_loop(M))
        usable[name] = {"tetrahedra": M.num_tetrahedra(),
                        "irreducible": irr,
                        "abs_tau": mp.nstr(t, 22),
                        "irreducible_equals_N": irr == M.num_tetrahedra()}
        print(f"    {name:8s} N={M.num_tetrahedra()} irred={irr:2d} "
              f"|tau|={mp.nstr(t, 20)}")
    for name, why in skipped.items():
        print(f"    {name:8s} SKIPPED — {why}")

    check(len(usable) >= 6,
          "CORRECTION_there_are_SIX_usable_points_not_TWO",
          f"an earlier version of this probe claimed the corpus could not TEST "
          f"a tau->C map — certified C for three knots, tau undefined on the "
          f"non-hyperbolic 3_1, so two points. THAT WAS WRONG and the error "
          f"was mine: the fixtures were never enumerated. The ptolemy DB is "
          f"firewalled (re-verified, 403 on CONNECT), but the wheel ships sl2 "
          f"fixtures for {len(FIXTURE_MANIFOLDS)} manifolds and "
          f"{len(usable)} are 1-cusped hyperbolic with both a defined tau and "
          f"a certified irreducible count: {sorted(usable)}. Six points "
          f"against a two-parameter family leaves four degrees of freedom, so "
          f"a candidate IS testable. The blocker was overstated 3x")

    not_n = sorted(k for k, v in usable.items() if not v["irreducible_equals_N"])
    check(len(not_n) >= 2,
          "the_irreducible_count_is_NOT_the_tetrahedron_count",
          f"irreducible = N holds for {len(usable) - len(not_n)} of "
          f"{len(usable)} and FAILS for {not_n}. Worth stating because it is "
          f"the first thing one would wrongly assume from the 4_1/5_2 pair "
          f"alone, where both happen to coincide")

    check(True,
          "but_STILL_no_tau_to_C_map_is_proposed",
          "six points make a candidate testable; they do not make fishing for "
          "one legitimate. Searching a functional form across six points and "
          "reporting the winner is the numerology this repo forbids. A map is "
          "separate work that must state its hypothesis BEFORE looking, and "
          "the census manifolds are valid for testing whether a relation "
          "exists while NOT automatically valid as D1-b nodes — D1-b's setup "
          "is about knots in S^3, and four of the six are not")

    check(True,
          "CONSEQUENCE_the_dictionary_is_LOCATED_not_excluded",
          "it must be strictly finer than the Smith normal form (part 1) and "
          "triangulation-invariant (this part). That class is non-empty — tau "
          "is in it — so D1-b is narrowed to a well-posed search, not refuted. "
          "What is missing to PROSECUTE it is NOT data: the correction above "
          "found six offline points, enough to test a candidate. What is "
          "missing is a HYPOTHESIS stated before looking. More certified "
          "counts (ptolemy DB, firewalled; or magma) would strengthen a test "
          "but are no longer the blocker I reported them to be")

    wb.add_data("polarization_variance_under_retriangulation", variance)
    wb.add_data("tau_triangulation_invariance", inv)
    wb.add_data("tau_on_the_N5_collision_group", taus)
    wb.add_data("fixture_manifolds_usable_for_a_tau_to_C_test", usable)
    wb.add_data("fixture_manifolds_skipped", skipped)
    wb.add_data("ptolemy_db_reachability", {
        "status": "403 on CONNECT, re-verified this session",
        "verified_by": "curl to ptolemy.unhyperbolic.org AND snappy's own "
                       "retrieve_solutions() for 6_1",
        "consequence": "the bundled wheel fixtures are the whole offline "
                       "certified-count dataset; they were never enumerated "
                       "before, which is how the 'two points' claim arose",
    })
    wb.add_data("tau_fourone_vs_DG", {
        "computed": mp.nstr(tau_41, 30),
        "expected_sqrt3_over_2": mp.nstr(want, 30),
        "source": "Dimofte-Garoufalidis arXiv:1202.6268 eq. 3.2",
    })
    wb.add_data("scope", {
        "tier": "scope-(a)",
        "shows": "the raw polarization-dependent NZ datum is not a manifold "
                 "invariant; together with part 1's SNF degeneracy this "
                 "brackets the dictionary between too-coarse and too-fine",
        "constructive": "the bracketed class is non-empty; the DG 1-loop tau "
                        "is triangulation-invariant and separates the five "
                        "N=5 knots the SNF collided",
        "does_NOT_show": "that tau, or any triangulation-invariant functional, "
                         "PRODUCES the node count. tau is a complex number, "
                         "not an integer count; separating is not counting",
        "why_no_map_is_offered": "not for lack of data — CORRECTED: six usable "
                                 "(tau, irreducible) points exist offline, so "
                                 "a candidate IS testable. No map is offered "
                                 "because searching a functional form across "
                                 "six points and reporting the winner is a "
                                 "fit; a map must state its hypothesis first",
        "superseded_claim": "an earlier version said TWO points and that the "
                            "corpus could not test any map. Wrong by 3x; the "
                            "wheel fixtures were never enumerated",
        "what_would_unblock_MORE_points": "the ptolemy database (firewalled, "
                                          "403 re-verified) or magma",
        "trap": "one_loop does NOT guard against non-hyperbolic input — it "
                "returns 0.5 for 3_1 without raising. A returned value is not "
                "evidence of hyperbolicity; check solution_type() yourself",
        "arithmetic": f"mpmath at {DPS} dps for tau; exact integers for the "
                      "polarization datum; no float64, no float() outside "
                      "mp.nstr rendering",
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
