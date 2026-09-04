#!/usr/bin/env python3
"""The third-knot DT test, RUN — the trefoil's boundary-parabolic connection
count is 2, and it corroborates without discriminating.

# Ref: .beans/qou-q9ih--d1-route-c-m1-construct-the-qw-reproducing-34-bar.md
# Ref: computations/qbeta/dt_crossknot_connection_count_certified_probe.py
# Ref: content/quantum-observable-universe/lean/QOU/QBeta/AdjointIndexSetM3.lean

WHAT WAS OPEN. `dt_crossknot_connection_count_certified_probe` certifies the
#boundary-parabolic-connections counts for 4_1 (3) and 5_2 (4) by processing
Magma primary-decomposition fixtures shipped inside the SnapPy wheel. Its own
docstring, and the witness it writes, record the third-knot test as BLOCKED:

    "6_1 has no bundled data -- the third-knot test for
     dtMax = recursionOrder + 1 remains open (needs the ptolemy DB or magma)"

and bean `qou-q9ih` D1-f lists as a named unblocker:

    "(3) a 6_1 (or 3_1) DT spectrum -> the third-knot falsification target"

THE BLOCKER IS ONLY TRUE OF 6_1. `3_1__sl2_c0` and `3_1__sl2_c1` ARE bundled in
the same directory, and D1-f names 3_1 as an acceptable target. No ptolemy DB,
no Magma, no network: the test was runnable from the installed wheel.

THE RESULT (this probe, method identical to the certified probe's):

    knot   c0 orbits   c1 orbits / degrees / field        irred  + abelian = TOTAL
    3_1        0        1 / [1] / Q                         1        1        2
    4_1        0        1 / [2] / x^2 - x + 1               2        1        3      CONTROL
    5_2        0        1 / [3] / x^3 + 2*x^2 + 3*x + 1     3        1        4      CONTROL

Both controls reproduce the committed witness exactly, so the method is the
corpus's and not a new one.

WHAT IT DOES AND DOES NOT SETTLE. Three candidate readings of the datum were on
the table, and ALL THREE predict 2 for the trefoil:

    total = crossing number - 1          3 - 1 = 2
    total = deg(trace field) + 1         1 + 1 = 2      (3_1's field is Q)
    total = full A-polynomial L-degree   2              (the corpus's R1)

So the third point does not separate THOSE three. Reporting it as "the
third-knot test passed" without that sentence would over-read it -- which is
exactly the `#4534 two-knot-linear-fit guard` the bean raises against a
2-integer target.

BUT IT DOES DISCRIMINATE, AGAINST A FOURTH READING THAT WAS NOT ON THE LIST --
and this is the load-bearing half. The adversarial alternative to the whole R1
identification is that the count tracks the COMPUTATION's presentation rather
than the knot: the triangulation. That reading fits BOTH original points exactly
and is killed by the trefoil.

    knot   tets   crossings   MEASURED   crossing-1   tets+1
    3_1      2        3           2          2         3   <-- FAILS by 1
    4_1      2        4           3          3         3       fits
    5_2      3        5           4          4         4       fits

`tets + 1` is NOT a strawman: SnapPy triangulates 4_1 with 2 tetrahedra and 5_2
with 3, so on the corpus's two knots it is INDISTINGUISHABLE from `crossing - 1`.
The trefoil separates them because 3_1 has the SAME tetrahedron count as 4_1 and
one fewer crossing. This matters more than the three readings above, because the
triangulation is NOT canonical -- had the count tracked it, the R1 reading would
have been an artifact of how the manifold was presented to Magma rather than a
fact about the knot.

I first wrote that this test "discriminates nothing". That was wrong: I had not
put the triangulation reading on the list, and it is the one an adversarial
referee reaches for first.

WHAT IT DOES BUY, stated precisely. The datum moves from TWO points to THREE:
counts (2, 3, 4) at crossing numbers (3, 4, 5), and irreducible parts (1, 2, 3)
equal to the trace-field degrees (1, 2, 3). A one-parameter core+extra family
(`AdjointIndexSetM3.knot_independent_core_forces_unit_remainder`) fits two
points by construction; a third collinear point is one genuine spare constraint
that it passed. That is weak evidence, and it is more than none.

WHAT WOULD DISCRIMINATE, AND WHY IT IS NOT DONE HERE. The rules
`crossing - 2` and `trace-field degree` agree on all three knots and must
diverge on some knot, since neither controls the other in general. Separating
them needs either
  (a) trace-field degrees for further knots -- `M.trace_field_gens()` raises
      `SageNotAvailable` in this container (SnapPy outside Sage), or
  (b) ptolemy data for a fourth KNOT -- not bundled.
Both are recorded as still-open rather than guessed at.

INSPECTED AND EXCLUDED, so it is not mistaken for a fourth point:
`DT_mcbbiceaibjklmdfgh__sl2_c0..c7` is also bundled and is tempting, but it
identifies as **L13a5175** -- a 3-component LINK with 3 cusps, not a knot in
S^3. Its abelian count is not 1 and its 26 irreducible points across two
non-empty obstruction classes are not comparable to the knot family. Not used.

SCOPE CAVEAT: 3_1 is a TORUS knot, not hyperbolic (volume 0). The ptolemy
variety and the A-polynomial are defined regardless, so the count and the R1
reading are meaningful; but the "geometric component" reasoning that motivates
the hyperbolic cases does not apply, and its single Galois orbit is rational
(field Q) rather than a genuine trace field. Scope-(a), nothing wired, no fit.

NO FLOAT64: the quantities here are integers and number-field degrees; no
floating-point arithmetic enters.
"""
from __future__ import annotations

import bz2
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

from witness_base import WitnessBuilder  # noqa: E402

# (irreducible, abelian, total) the certified probe committed for the controls,
# plus the trefoil prediction shared by all three candidate readings.
EXPECT = {
    "3_1": {"degrees": [1], "irreducible": 1, "abelian": 1, "total": 2},
    "4_1": {"degrees": [2], "irreducible": 2, "abelian": 1, "total": 3},
    "5_2": {"degrees": [3], "irreducible": 3, "abelian": 1, "total": 4},
}
CROSSINGS = {"3_1": 3, "4_1": 4, "5_2": 5}


def _degree(nf) -> int:
    """Degree of a solution's number field; None means the rationals."""
    if nf is None:
        return 1
    try:
        return int(nf.poldegree())
    except Exception:
        try:
            return int(nf.degree())
        except Exception:
            return 1


def main() -> int:
    import snappy.ptolemy
    from snappy.ptolemy import processMagmaFile

    data_dir = Path(snappy.ptolemy.__file__).parent / "testing_files"

    w = WitnessBuilder("dt-third-knot-trefoil-count", engine="snappy-ptolemy")
    w.set_description(
        "The third-knot DT test the corpus recorded as blocked, run: 3_1's "
        "bundled sl2 fixtures give 1 irreducible + 1 abelian = 2 connections, "
        "with 4_1 and 5_2 reproducing the committed controls. The three listed "
        "readings all predict 2, but the trefoil DOES kill a fourth — that the "
        "count tracks the non-canonical triangulation, which fits both original "
        "knots exactly."
    )
    ok = []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    print(f"  fixtures: {data_dir}")
    check("the_trefoil_sl2_fixtures_ARE_bundled",
          (data_dir / "3_1__sl2_c0.magma_out.bz2").exists()
          and (data_dir / "3_1__sl2_c1.magma_out.bz2").exists(),
          "(so the 'needs the ptolemy DB or magma' blocker was true of 6_1 only)")

    rows = {}
    for knot in ("3_1", "4_1", "5_2"):
        irred, per_class = 0, []
        for c in (0, 1):
            f = data_dir / f"{knot}__sl2_c{c}.magma_out.bz2"
            text = bz2.open(f, "rt", encoding="utf-8", errors="replace").read()
            sols = processMagmaFile.solutions_from_magma(text)
            degs, fields = [], []
            for s in sols:
                nf = getattr(s, "number_field", lambda: None)()
                degs.append(_degree(nf))
                fields.append(str(nf) if nf is not None else "Q")
            irred += sum(degs)
            per_class.append({"obstruction_class": c, "orbits": len(sols),
                              "degrees": degs, "fields": fields})
        total = irred + 1
        rows[knot] = {"per_class": per_class, "irreducible": irred,
                      "abelian": 1, "total": total,
                      "crossing_number": CROSSINGS[knot]}
        e = EXPECT[knot]
        print(f"    {knot}: irreducible {irred} + abelian 1 = TOTAL {total}"
              f"   (expected {e['total']})")
        check(f"{knot}_reproduces_the_expected_total",
              total == e["total"] and irred == e["irreducible"],
              "CONTROL — matches the committed certified witness"
              if knot in ("4_1", "5_2") else "the new third point")

    check("the_two_controls_match_the_COMMITTED_certified_witness",
          rows["4_1"]["total"] == 3 and rows["5_2"]["total"] == 4,
          "(so the method here is the corpus's, not a new one)")

    # The three candidate readings, all of which predict 2 for the trefoil.
    t = rows["3_1"]["total"]
    predictions = {
        "crossing_number_minus_1": CROSSINGS["3_1"] - 1,
        "trace_field_degree_plus_1": rows["3_1"]["per_class"][1]["degrees"][0] + 1,
        "full_A_polynomial_L_degree_R1": 2,
    }
    check("the_three_listed_readings_are_NOT_separated_by_the_trefoil",
          all(v == t for v in predictions.values()),
          f"(all predict {t}) — these three are not separated by the third knot")

    # The FOURTH reading, and the one the trefoil DOES kill: that the count
    # tracks the TRIANGULATION rather than the knot. It fits both original
    # points exactly, since SnapPy triangulates 4_1 with 2 tetrahedra and 5_2
    # with 3. The trefoil separates them: same tetrahedron count as 4_1, one
    # fewer crossing.
    import snappy
    tets = {kk: snappy.Manifold(kk).num_tetrahedra()
            for kk in ("3_1", "4_1", "5_2")}
    print("\n  the triangulation reading (tets + 1), which the trefoil KILLS:")
    print(f"    {'knot':<6}{'tets':>5}{'cross':>7}{'measured':>10}"
          f"{'crossing-1':>12}{'tets+1':>8}")
    for kk in ("3_1", "4_1", "5_2"):
        print(f"    {kk:<6}{tets[kk]:>5}{CROSSINGS[kk]:>7}"
              f"{rows[kk]['total']:>10}{CROSSINGS[kk] - 1:>12}{tets[kk] + 1:>8}")
    check("the_triangulation_reading_fits_BOTH_original_knots",
          tets["4_1"] + 1 == rows["4_1"]["total"]
          and tets["5_2"] + 1 == rows["5_2"]["total"],
          "(so on the corpus's two knots it is INDISTINGUISHABLE from "
          "crossing-1 — not a strawman)")
    check("the_TREFOIL_KILLS_the_triangulation_reading",
          tets["3_1"] + 1 != rows["3_1"]["total"],
          f"(tets+1 = {tets['3_1'] + 1} vs measured {rows['3_1']['total']}) — "
          "the adversarial alternative to R1 is that the count tracks the "
          "non-canonical PRESENTATION, not the knot. It does not.")

    check("the_datum_is_now_THREE_collinear_points_not_two",
          [rows[k]["total"] for k in ("3_1", "4_1", "5_2")] == [2, 3, 4]
          and [rows[k]["irreducible"] for k in ("3_1", "4_1", "5_2")] == [1, 2, 3],
          "(one genuine spare constraint on the one-parameter core+extra family, "
          "which it passed — weak evidence, and more than none)")

    w.add_data("knots", rows)
    w.add_data("candidate_readings", {
        "measured_trefoil_total": t,
        "predictions": predictions,
        "verdict": "the three listed readings all agree at 3_1, so the "
                   "third knot does not separate them; it kills a "
                   "FOURTH, the triangulation reading — see below",
    })
    w.add_data("triangulation_reading_EXCLUDED", {
        "reading": "total = number of tetrahedra + 1",
        "why_it_matters": "the adversarial alternative to the R1 identification "
                          "— that the count tracks the computation's "
                          "PRESENTATION rather than the knot. The triangulation "
                          "is not canonical, so had the count tracked it, R1 "
                          "would be an artifact.",
        "tets": tets,
        "fits_4_1": True, "fits_5_2": True, "fails_3_1": True,
        "note": "indistinguishable from crossing-1 on the corpus's two knots; "
                "separated by the trefoil, which shares 4_1's tetrahedron count "
                "and has one fewer crossing. THIS is what the third knot buys.",
    })
    w.add_data("what_would_discriminate", {
        "rules_that_must_diverge": "crossing_number - 2  vs  trace_field_degree "
                                   "(equal on all three knots here; neither "
                                   "controls the other in general)",
        "route_a_blocked": "trace-field degrees for further knots — "
                           "M.trace_field_gens() raises SageNotAvailable "
                           "(SnapPy outside Sage in this container)",
        "route_b_blocked": "ptolemy data for a fourth KNOT — not bundled; 6_1 "
                           "(= m032) has no fixture",
        "status": "both recorded as open, neither guessed at",
    })
    w.add_data("inspected_and_excluded", {
        "DT_mcbbiceaibjklmdfgh": "identifies as L13a5175 — a 3-component LINK "
                                 "with 3 cusps, not a knot in S^3. Its abelian "
                                 "count is not 1 and its 26 irreducible points "
                                 "across obstruction classes c4 (degree 15) and "
                                 "c5 (degree 11) are not comparable to the knot "
                                 "family. NOT used as a fourth point.",
        "m019_m135_s000_t00000_v0000": "census manifolds; identify() returns "
                                       "only themselves, i.e. not knot "
                                       "complements in the standard tables.",
    })
    w.add_data("scope", {
        "tier": "scope-(a)", "wired": False, "is_a_fit": False,
        "caveat_3_1_not_hyperbolic": "3_1 is a torus knot, volume 0. The "
                                     "ptolemy variety and the A-polynomial are "
                                     "defined regardless, so the count and the "
                                     "R1 reading are meaningful; but the "
                                     "geometric-component reasoning motivating "
                                     "the hyperbolic cases does not apply, and "
                                     "its single orbit is rational (Q) rather "
                                     "than a genuine trace field.",
    })

    passed = sum(ok)
    print(f"\n  {passed}/{len(ok)} checks passed")
    w.save()
    return 0 if passed == len(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
