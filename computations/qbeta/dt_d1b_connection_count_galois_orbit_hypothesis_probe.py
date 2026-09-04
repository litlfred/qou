#!/usr/bin/env python3
"""dt_d1b_connection_count_galois_orbit_hypothesis_probe.py — qou-q9ih D1-b.

The D1-b ledger's standing conclusion is that what the route needs is **a
hypothesis stated before looking**, not more data: six offline `(tau, C)` points
exist, and searching functional forms across them and reporting the winner would
be a fit. This probe states one, states what it predicts, and then measures.

═══ THE HYPOTHESIS, WRITTEN BEFORE THE MEASUREMENT ═══

Where the certified counts actually come from is a clue that has not been
followed. `dt_crossknot_connection_count_certified_probe.py` obtains `C_irr` by
summing **Galois-orbit degrees** of the ptolemy variety — 4_1 gives one orbit of
degree 2, 5_2 one orbit of degree 3 — and those degrees are the degrees of the
number fields the representations are defined over. The geometric
representation lives in the trace field. So:

    **H.** The irreducible boundary-parabolic PSL(2,C) representations of a
    1-cusped hyperbolic manifold form a SINGLE Galois orbit — they are the
    Galois conjugates of the geometric representation — so
    `C_irr = [trace field : Q]`.

**Why H matters more than a curve fit.** If it holds, D1-b's node count is
**arithmetic** — a field degree — and neither the NZ gluing datum nor the 1-loop
`tau` is where the dictionary should read. That would redirect the route rather
than advance it along its current line. If it fails, the way it fails says what
the count is made of instead.

**MY PREDICTION, recorded so I can be wrong in public: H FAILS, at `m135`.**
`m135` carries **eight** obstruction classes and `C_irr = 8`. An obstruction
class is a `H^2(M, dM; Z/2)` invariant of a representation, and the Galois
action does not move a representation between obstruction classes — so
representations in different classes cannot be Galois conjugates, and eight
inhabited classes cannot be one orbit. If that is right, `C_irr` is a **sum over
obstruction classes** of orbit degrees, and the number of inhabited classes is
part of the answer rather than a bookkeeping detail.

**What is and is not an independent test.** 4_1 and 5_2 were already known to be
single-orbit from the certified probe, so they are NOT independent evidence for
H — they are what suggested it. The four census manifolds bundled in the snappy
wheel (`m135`, `s000`, `t00000`, `v0000`) are the actual test, and I have not
looked at their orbit structure.

═══ SCOPE ═══

Scope-(a). This measures the orbit structure of the ptolemy variety over the
fixtures the snappy wheel ships; the ptolemy database is firewalled (403 on
CONNECT, re-verified), so those seven manifolds are the whole offline dataset.
Four are census manifolds, not knots in S^3 — valid for testing H, and NOT
automatically valid as D1-b nodes, which is D1-b's own stipulation.

The abelian `(L-1)` convention is established for knots in S^3 and does not
carry over to a census manifold, so everything here is the **irreducible**
count, never the total.

Nothing is wired, nothing is fitted, and `A_omega` remains underived.

CONTROLS. The parse must be shown to be reading real orbit structure rather
than manufacturing it:
  [C1] the recomputed `C_irr` for 4_1 and 5_2 must reproduce the committed
       certified witness exactly (2 and 3) — if the orbit parse were wrong the
       sums would not match a number arrived at independently;
  [C2] the recorded trace-field degrees (2 for 4_1, 3 for 5_2) must appear as
       the orbit degrees, which is the internal consistency check the certified
       probe already relies on;
  [C3] obstruction classes with **zero** solutions must be counted as zero
       orbits, not silently skipped — otherwise "one orbit" is an artifact of
       dropping empty classes.

Bean qou-q9ih (route D1-b).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

# Every manifold the snappy wheel ships an sl2 ptolemy fixture for.
FIXTURES = ["3_1", "4_1", "5_2", "m135", "s000", "t00000", "v0000"]

# Known independently, from the committed certified witness. Used as CONTROLS,
# not as evidence for H — these two are what suggested H in the first place.
CERTIFIED_IRR = {"4_1": 2, "5_2": 3}
CERTIFIED_DEGREES = {"4_1": [2], "5_2": [3]}


def orbit_structure(name):
    """Per-obstruction-class Galois orbit degrees, from the bundled fixtures.

    Returns None when no fixture exists. An obstruction class with no solutions
    contributes an explicit empty list, never a skipped entry (control C3).
    """
    import bz2
    import re
    import snappy.ptolemy as pm
    from snappy.ptolemy import processMagmaFile

    d = Path(pm.__file__).parent / "testing_files"
    pat = re.compile(rf"{re.escape(name)}__sl2_c(\d+)\.magma_out\.bz2$")
    files = sorted((int(m.group(1)), f) for f in d.iterdir()
                   for m in [pat.match(f.name)] if m)
    if not files:
        return None
    per_class = {}
    for idx, f in files:
        sols = processMagmaFile.solutions_from_magma(
            bz2.open(f, "rt").read(), numerical=False)
        degs = []
        for s in sols.flatten():
            nf = s.number_field()
            if nf is None:
                degs.append(1)
            else:
                try:
                    degs.append(int(nf.poldegree()))
                except Exception:
                    degs.append(int(nf.degree()))
        per_class[idx] = degs           # [] when the class is empty — C3
    return per_class


def main() -> int:
    import snappy

    print("=" * 78)
    print(" D1-b — is the connection count a SINGLE Galois orbit?")
    print("=" * 78)
    print("  H: irreducible boundary-parabolic reps form ONE Galois orbit,")
    print("     so C_irr = [trace field : Q].")
    print("  MY PREDICTION (recorded before measuring): H FAILS at m135.\n")

    wb = WitnessBuilder("dt-d1b-connection-count-galois-orbit-hypothesis",
                        engine="snappy-ptolemy-magma-fixtures-exact")
    wb.set_description(
        "qou-q9ih D1-b. The ledger's conclusion was that the route needs a "
        "HYPOTHESIS stated before looking, not more data. This states one: H, "
        "that the irreducible boundary-parabolic PSL(2,C) reps of a 1-cusped "
        "hyperbolic manifold form a SINGLE Galois orbit (the conjugates of the "
        "geometric rep), so C_irr = [trace field : Q]. If H held, D1-b's node "
        "count would be ARITHMETIC -- a field degree -- and neither the NZ "
        "gluing datum nor the 1-loop tau would be where the dictionary reads, "
        "which redirects the route rather than advancing it. A prediction was "
        "recorded before measuring: H FAILS at m135, because an obstruction "
        "class is an H^2(M,dM;Z/2) invariant that the Galois action cannot "
        "move a rep across, so eight inhabited classes cannot be one orbit. "
        "4_1 and 5_2 are NOT independent evidence (they are what suggested H); "
        "the four bundled census manifolds are the test. Scope-(a): the "
        "ptolemy DB is firewalled, so the seven wheel fixtures are the whole "
        "offline dataset; four are census manifolds, valid for testing H and "
        "not automatically valid as D1-b nodes. Irreducible counts only -- the "
        "abelian (L-1) convention does not carry to a census manifold. "
        "Nothing wired; no fit."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    checks: list[tuple[bool, str, str]] = []

    def check(ok, name, detail):
        checks.append((bool(ok), name, detail))
        print(f"  [{'PASS' if ok else 'FAIL':4s}] {name} — {detail}")

    rows = {}
    for name in FIXTURES:
        per_class = orbit_structure(name)
        if per_class is None:
            continue
        try:
            M = snappy.Manifold(name)
            hyp = M.solution_type().startswith("all tetrahedra")
            cusps, tets = M.num_cusps(), M.num_tetrahedra()
            sol = M.solution_type()
        except Exception as exc:
            hyp, cusps, tets, sol = False, None, None, f"load failed: {exc}"
        orbits = [d for degs in per_class.values() for d in degs]
        rows[name] = {
            "per_obstruction_class": {str(k): v for k, v in per_class.items()},
            "classes_total": len(per_class),
            "classes_inhabited": sum(1 for v in per_class.values() if v),
            "orbits_total": len(orbits),
            "orbit_degrees": sorted(orbits, reverse=True),
            "C_irr": sum(orbits),
            "single_orbit": len(orbits) == 1,
            "hyperbolic": hyp, "cusps": cusps, "tetrahedra": tets,
            "solution_type": sol,
        }
        print(f"  {name:8s} classes {len(per_class):2d} "
              f"(inhabited {rows[name]['classes_inhabited']:2d})  "
              f"orbits {len(orbits):2d}  degrees {rows[name]['orbit_degrees']}"
              f"  C_irr {sum(orbits):2d}  hyp={hyp}")

    print()
    # ---------------------------------------------------------------- C1/C2
    c1 = all(rows[k]["C_irr"] == v for k, v in CERTIFIED_IRR.items())
    check(c1, "C1_recomputed_C_irr_REPRODUCES_the_certified_witness",
          f"4_1 -> {rows['4_1']['C_irr']} (expect 2), 5_2 -> "
          f"{rows['5_2']['C_irr']} (expect 3). The certified number was "
          "arrived at independently, so a wrong orbit parse would not sum to it")
    c2 = all(rows[k]["orbit_degrees"] == v for k, v in CERTIFIED_DEGREES.items())
    check(c2, "C2_the_orbit_DEGREES_are_the_known_trace_field_degrees",
          f"4_1 {rows['4_1']['orbit_degrees']} (Q(sqrt(-3)), degree 2), 5_2 "
          f"{rows['5_2']['orbit_degrees']} (cubic trace field)")
    empties = {k: rows[k]["classes_total"] - rows[k]["classes_inhabited"]
               for k in rows}
    check(any(v > 0 for v in empties.values()),
          "C3_EMPTY_obstruction_classes_are_counted_not_skipped",
          f"empty-class counts per manifold {empties}; at least one manifold "
          "has an empty class, so 'one orbit' cannot be an artifact of "
          "dropping empties")

    # ---------------------------------------------------------------- H
    hyp_rows = {k: v for k, v in rows.items() if v["hyperbolic"]}
    single = sorted(k for k, v in hyp_rows.items() if v["single_orbit"])
    multi = sorted(k for k, v in hyp_rows.items() if not v["single_orbit"])
    print(f"\n  single-orbit: {single}")
    print(f"  multi-orbit : {multi}")

    h_holds = not multi
    check(True, "H_IS_TESTED_AND_THE_VERDICT_IS_RECORDED_EITHER_WAY",
          f"H {'HOLDS' if h_holds else 'FAILS'} on the hyperbolic fixtures: "
          f"{len(single)} single-orbit {single}, {len(multi)} multi-orbit "
          f"{multi}")

    m135_multi = "m135" in multi
    verdict = ("CORRECT" if m135_multi else
               "WRONG — recorded as such rather than quietly restated")
    check(True, "MY_PREDICTION_was_" + ("CORRECT" if m135_multi else "WRONG"),
          f"I predicted H would fail at m135. m135 has "
          f"{rows['m135']['orbits_total']} orbits with degrees "
          f"{rows['m135']['orbit_degrees']} across "
          f"{rows['m135']['classes_inhabited']} inhabited classes, so the "
          f"prediction was {verdict}")

    # what the count is made of, whichever way H went
    if multi:
        detail = ("C_irr is NOT a single field degree. It is a SUM over "
                  "obstruction classes of orbit degrees, so the number of "
                  "INHABITED obstruction classes is part of the answer: "
                  + ", ".join(f"{k} = {'+'.join(str(d) for d in rows[k]['orbit_degrees'])}"
                              f" over {rows[k]['classes_inhabited']} classes"
                              for k in multi)
                  + ". A D1-b dictionary reading only the trace field cannot "
                    "produce it; it needs the obstruction-class grading too")
    else:
        detail = ("every hyperbolic fixture is single-orbit, so C_irr = "
                  "[trace field : Q] on this sample. That makes the node count "
                  "ARITHMETIC and points D1-b at the trace field rather than "
                  "at the NZ datum or tau")
    check(True, "WHAT_THE_COUNT_IS_MADE_OF", detail)

    check(True, "SCOPE_this_does_not_derive_A_omega",
          "seven fixtures, four of them census manifolds rather than knots in "
          "S^3; irreducible counts only; the ptolemy DB stays firewalled so "
          "this sample cannot be enlarged offline. Nothing wired, no fit")

    wb.add_data("manifolds", rows)
    wb.add_data("hypothesis", {
        "statement": "irreducible boundary-parabolic PSL(2,C) reps form a "
                     "single Galois orbit, so C_irr = [trace field : Q]",
        "stated_before_measurement": True,
        "prediction_recorded": "H fails at m135 — obstruction class is an "
                               "H^2(M,dM;Z/2) invariant the Galois action "
                               "cannot cross, so 8 inhabited classes cannot "
                               "be one orbit",
        "verdict": "HOLDS" if h_holds else "FAILS",
        "prediction_was": "CORRECT" if m135_multi else "WRONG",
        "not_independent_evidence": ["4_1", "5_2"],
        "independent_test_set": ["m135", "s000", "t00000", "v0000"],
    })
    wb.add_data("scope", {
        "tier": "scope-(a)",
        "dataset": "the seven sl2 ptolemy fixtures bundled in the snappy "
                   "wheel; the ptolemy DB is firewalled (403 on CONNECT)",
        "census_caveat": "m135/s000/t00000/v0000 are census manifolds, not "
                         "knots in S^3 — valid for testing H, not "
                         "automatically valid as D1-b nodes",
        "abelian_convention": "irreducible counts only; the (L-1) abelian "
                              "convention is established for knots in S^3 and "
                              "does not carry over",
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
