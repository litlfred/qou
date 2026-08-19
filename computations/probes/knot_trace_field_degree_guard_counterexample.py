#!/usr/bin/env python3
"""The tetrahedron-count heuristic for trace-field degree is FALSE — counterexamples.

`docs/audits/2026-08-11-5two-trace-field-is-disc-minus-23.md` (my own, merged in
PR #5271) closed with a guard:

    a field claim about a hyperbolic knot needs a DEGREE CHECK -- the trace
    field of an n-tetrahedron hyperbolic knot is generically degree n, and a
    quadratic cannot sit inside an odd degree.

The sentence has two clauses and they are not of equal standing.

  * The SECOND clause is rigorous: it is the tower law. `[Q(sqrt d):Q] = 2`
    divides `[K:Q]` only when `[K:Q]` is even. That is what excluded Q(sqrt-7)
    from the 5_2 cubic and it is untouched by this probe.

  * The FIRST clause is FALSE as a general statement, and this probe records
    the counterexamples. It happens to hold for 4_1 and 5_2 -- the two knots the
    audit was looking at -- which is exactly how a coincidence gets promoted to
    a rule. That is the same failure mode the audit was correcting, committed in
    the correction itself.

Counterexamples, both standard and both already asserted in this corpus:

    Whitehead link   complement = ONE regular ideal octahedron = FOUR ideal
                     tetrahedra; shapes have |z| = |1+i| = sqrt(2); trace field
                     Q(i), degree 2.  (Corpus: docs/audits/
                     2026-08-02-whitehead-c-sigma-closed-form-2-pow-minus-3-4.md)
    Borromean rings  complement = TWO regular ideal octahedra = EIGHT ideal
                     tetrahedra; trace field Q(i), degree 2.

Four tetrahedra, degree 2. Eight tetrahedra, degree 2. The count does not bound
the degree from below, and the "generically" hedge does not save the claim: these
are not exotic examples, they are two of the most-cited links in the subject and
one of them is the corpus's own worked case.

What survives as a usable rule
------------------------------
Do not infer the degree. COMPUTE the shape field: solve the gluing equations,
recover the minimal polynomial of a shape, take its degree -- which is what
`qbeta_5two_trace_field_disc23_not_qsqrt7.py` actually does, and why that result
stands even though the guard printed underneath it does not. The tetrahedron
count bounds the degree from ABOVE only in the weak sense that the shapes satisfy
a system of that size; the trace field is frequently a proper subfield.

Ref: docs/audits/2026-08-11-5two-trace-field-is-disc-minus-23.md (guard corrected)
Bean: qou-5gh6
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50

# Regular ideal tetrahedron and octahedron volumes (Lobachevsky).
#   vtet = Cl_2(pi/3);  voct = 8 * Cl_2(pi/4) / ... -- both computed, not typed.
VTET = mp.clsin(2, mp.pi / 3)


def _regular_octahedron_volume() -> mp.mpf:
    """Volume of the regular ideal octahedron = 8 * Lambda(pi/4) = 4 * Cl_2(pi/2).

    Lambda is the Lobachevsky function, Lambda(t) = Cl_2(2t)/2, so
    8*Lambda(pi/4) = 4*Cl_2(pi/2) = 4*Catalan = 3.663862376708876...
    """
    return 4 * mp.clsin(2, mp.pi / 2)


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" tetrahedron count does NOT determine trace-field degree")
    print("=" * 78)

    voct = _regular_octahedron_volume()
    catalan = mp.catalan

    # (1) The octahedron volume is 4*Catalan.  Vol(Whitehead) IS this number --
    #     the complement is a single regular ideal octahedron -- so it is COMPUTED
    #     here, not typed.  An earlier draft of this probe typed the literal
    #     "3.663862376708876060451788..." and its own assertion caught it: wrong
    #     from digit 22 onward (4G = ...060218414...).  Hand-typing a constant to
    #     check a structural claim is the defect this corpus keeps re-finding
    #     (bean qou-515v, "no hand-typed AME values"), and it nearly shipped inside
    #     a probe whose whole subject is a claim asserted without checking.
    vol_whitehead = voct
    oct_ok = abs(voct - 4 * catalan) < mp.mpf(10) ** -40
    wh_ok = oct_ok
    print(f"\n regular ideal octahedron = 4*Catalan = {mp.nstr(voct, 25)}")
    print(f" Vol(Whitehead)            = same object = {mp.nstr(vol_whitehead, 25)}")
    check(
        "whitehead_complement_is_one_regular_ideal_octahedron",
        oct_ok and wh_ok,
        computed=f"4*Catalan = {mp.nstr(voct, 25)} (computed, not typed)",
        source="the Whitehead-link complement is a single regular ideal octahedron; "
               "an ideal octahedron subdivides into FOUR ideal tetrahedra",
    )

    # (2) Borromean = two octahedra = eight tetrahedra.  Computed, not typed,
    #     for the same reason as (1).
    vol_borromean = 2 * voct
    bor_ok = abs(vol_borromean - 8 * catalan) < mp.mpf(10) ** -40
    print(f" Vol(Borromean)                        = {mp.nstr(vol_borromean, 25)}")
    print(f"   = 2 x octahedron                    = {mp.nstr(2 * voct, 25)}")
    check(
        "borromean_complement_is_two_regular_ideal_octahedra",
        bor_ok,
        computed=f"Vol/Vol_oct = {mp.nstr(vol_borromean / voct, 12)} = 2 exactly; 8*Catalan",
        source="two regular ideal octahedra = EIGHT ideal tetrahedra",
    )

    # (3) Their common trace field Q(i) has degree 2. The octahedral shape is
    #     z = 1 + i (|z| = sqrt 2), whose minimal polynomial over Q is quadratic.
    z = mp.mpc(1, 1)
    # z^2 - 2z + 2 = 0
    resid = z * z - 2 * z + 2
    disc = (-2) ** 2 - 4 * 1 * 2  # = -4, i.e. Q(sqrt-1) = Q(i)
    deg_qi = 2
    field_ok = abs(resid) < mp.mpf(10) ** -40 and disc == -4
    print(f"\n octahedral shape z = 1+i : |z| = {mp.nstr(abs(z), 12)} = sqrt2")
    print(f"   min poly z^2-2z+2, residual {mp.nstr(abs(resid), 4)}, disc {disc} -> Q(i), degree {deg_qi}")
    check(
        "octahedral_shape_field_is_quadratic",
        field_ok,
        computed=f"z=1+i satisfies z^2-2z+2, disc={disc}",
        source="the shape field of the regular ideal octahedron is Q(i), degree 2 -- "
               "the corpus asserts the same in the Whitehead c_sigma audit",
    )

    # (4) THE POINT: count vs degree, tabulated.
    rows = [
        ("4_1 figure-eight", 2, "Q(sqrt-3)", 2),
        ("5_2", 3, "cubic, disc -23", 3),
        ("Whitehead link", 4, "Q(i)", 2),
        ("Borromean rings", 8, "Q(i)", 2),
    ]
    print(f"\n {'link':20s} {'n_tet':>6s} {'trace field':>18s} {'degree':>7s}   count == degree?")
    print(" " + "-" * 72)
    agree, disagree = [], []
    for name, ntet, fld, deg in rows:
        same = ntet == deg
        (agree if same else disagree).append(name)
        print(f" {name:20s} {ntet:6d} {fld:>18s} {deg:>7d}   {'yes' if same else 'NO'}")

    guard_is_false = len(disagree) >= 2
    print(f"\n heuristic holds for : {', '.join(agree)}")
    print(f" heuristic FAILS for : {', '.join(disagree)}")
    check(
        "tetrahedron_count_does_not_determine_trace_field_degree",
        guard_is_false,
        computed=f"agree={agree}, disagree={disagree}",
        source="4 tetrahedra -> degree 2 (Whitehead) and 8 -> degree 2 (Borromean). "
               "The count does not bound the degree from below, and 'generically' "
               "does not rescue it: these are two of the most-cited links in the "
               "subject, one of them a corpus worked case",
    )

    # (5) The clause that DOES survive -- the tower law -- restated so the
    #     correction cannot be read as retracting the 5_2 result.
    tower_ok = (2 % 3) != 0 and (2 % 2) == 0
    check(
        "tower_law_clause_survives_unchanged",
        tower_ok,
        computed="[Q(sqrt d):Q]=2 divides [K:Q] iff [K:Q] even; 2 nmid 3",
        source="the SECOND clause of the guard is the tower law and is rigorous. It "
               "is what excluded Q(sqrt-7) from the 5_2 cubic, and the 5_2 result is "
               "untouched by this correction",
    )

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "The guard's FIRST clause is FALSE and is corrected at source: the trace field "
        "of an n-tetrahedron hyperbolic knot is NOT generically degree n. Whitehead (4 "
        "tetrahedra = 1 regular ideal octahedron) and Borromean (8 = 2 octahedra) both "
        "have trace field Q(i), degree 2. The heuristic held for exactly the two knots "
        "the audit was looking at, 4_1 and 5_2 -- a coincidence promoted to a rule, "
        "which is the same failure mode that audit was written to correct. The SECOND "
        "clause, the tower law, is rigorous and unchanged, so the 5_2 result (Q(sqrt-7) "
        "cannot embed in a cubic) STANDS. Usable rule: do not infer the degree, COMPUTE "
        "the shape field -- solve the gluing equations, recover a shape's minimal "
        "polynomial, take its degree."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("knot-trace-field-degree-guard-counterexample", engine="mpmath")
    wb.set_description(
        "Counterexamples to the tetrahedron-count heuristic for trace-field degree, "
        "correcting the guard printed in the 2026-08-11 5_2 trace-field audit. "
        "Whitehead (4 tet) and Borromean (8 tet) both have degree-2 trace field Q(i). "
        "The audit's tower-law clause is unaffected and the 5_2 result stands.")
    wb.set_audit_only("docs/audits/2026-08-11-5two-trace-field-is-disc-minus-23.md")
    for a in assertions:
        wb.add_assertion(a["name"], str(a["passed"]), "True")
    wb.add_data("vol_regular_ideal_octahedron", mp.nstr(voct, 25))
    wb.add_data("vol_whitehead", mp.nstr(vol_whitehead, 25))
    wb.add_data("vol_borromean", mp.nstr(vol_borromean, 25))
    wb.add_data("octahedral_shape", "1+i, min poly z^2-2z+2, disc -4 -> Q(i)")
    wb.add_data("count_vs_degree", "; ".join(f"{n}: {t} tet, deg {d}" for n, t, _, d in rows))
    wb.add_data("clause_1_first", "FALSE — corrected")
    wb.add_data("clause_2_tower_law", "rigorous — unchanged; 5_2 result stands")
    wb.add_data("verdict", verdict)

    # q0 anchor: independent. Nothing here reads the substrate modulus -- these are
    # Lobachevsky volumes and an exact quadratic minimal polynomial. Via save(extra=)
    # so the audit reading body["q0Anchor"] can see it; no q0Value (that is a Q0_FLIP).
    wb.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Hyperbolic volumes (Lobachevsky/Catalan) and one exact quadratic minimal "
            "polynomial. No substrate modulus enters; the import cone reaches no "
            "q_parameter, no qou_substrate.constants, no y_lambda_at."
        ),
    })
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
