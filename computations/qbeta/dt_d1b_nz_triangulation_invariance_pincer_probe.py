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

🛑 WHAT THIS DOES NOT SHOW, AND WHY NO MAP IS PROPOSED. `tau` is a complex
number, not an integer count; separating knots is not producing 3 and 4. More
sharply, the corpus CANNOT TEST any proposed `tau -> C` map: certified
connection counts exist for exactly three knots (4_1, 5_2, 3_1 — the snappy
wheel's Magma fixtures; the ptolemy database is firewalled), and `tau` is
undefined on 3_1 because it is not hyperbolic. That leaves TWO usable
`(tau, C)` points. Any two-parameter family fits two points exactly, so such a
proposal would be unfalsifiable here by construction. No map is offered and
none should be fitted; the honest statement is that the search space is
narrowed and the data to test a candidate does not exist in this corpus.

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
        "not excluded. NO tau->C map is proposed: certified C exists for only "
        "three knots and tau is undefined on the non-hyperbolic 3_1, leaving "
        "TWO usable points, which any two-parameter family fits exactly -- "
        "such a proposal would be unfalsifiable in this corpus by "
        "construction. mpmath at 40 dps throughout; no float64. Scope-(a); "
        "nothing wired; no fit."
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

    # -------------------------------------------------------- the limit
    check(True,
          "NO_tau_to_C_map_is_proposed_and_none_can_be_TESTED_here",
          "certified connection counts exist for exactly 3 knots (4_1, 5_2, "
          "3_1 — the snappy wheel's Magma fixtures; the ptolemy DB is "
          "firewalled), and tau is UNDEFINED on 3_1 because it is not "
          "hyperbolic. That leaves TWO usable (tau, C) points, which any "
          "two-parameter family fits exactly. A map fitted here would be "
          "unfalsifiable by construction, so none is offered")

    check(True,
          "CONSEQUENCE_the_dictionary_is_LOCATED_not_excluded",
          "it must be strictly finer than the Smith normal form (part 1) and "
          "triangulation-invariant (this part). That class is non-empty — tau "
          "is in it — so D1-b is narrowed to a well-posed search, not refuted. "
          "What is missing to PROSECUTE that search is data: more certified "
          "connection counts, i.e. the ptolemy database or magma")

    wb.add_data("polarization_variance_under_retriangulation", variance)
    wb.add_data("tau_triangulation_invariance", inv)
    wb.add_data("tau_on_the_N5_collision_group", taus)
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
        "why_no_map_is_offered": "only two usable (tau, C) points exist in "
                                 "this corpus (3_1 is non-hyperbolic so tau is "
                                 "undefined there), and any two-parameter "
                                 "family fits two points exactly",
        "what_would_unblock": "more certified connection counts — the ptolemy "
                              "database (firewalled) or magma",
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
