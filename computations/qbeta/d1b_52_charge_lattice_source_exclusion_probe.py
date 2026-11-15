#!/usr/bin/env python3
"""d1b_52_charge_lattice_source_exclusion_probe.py — qou-rutm: the 5_2 charge
lattice is NOT sourceable from the held knots-quivers literature, and the
exclusion is structural.

The rung `qou-rutm` opened as "source a charge lattice for the 5_2 flavour". The
corpus-grep for it lands on two held sources, and the honest answer is a
NEGATIVE with a proved invariant behind it.

═══ WHAT THE CORPUS HOLDS ═══

Two documents in `library/` carry the knots-quivers correspondence:

  arxiv-1707.02991v1       Kucharski-Reineke-Stosic-Sulkowski, "BPS states,
                           knots and quivers" -- the correspondence itself.
                           Explicit quiver worked for the TREFOIL only
                           (its section 3 is titled "Example -- trefoil knot").

  physrevd108106023        Singh et al., "Knot-quiver correspondence for double
                           twist knots", Phys. Rev. D 108, 106023 (2023).
                           Explicit quiver matrices for a FAMILY.

The second is the promising one, and it is already cited in this corpus at
`conj:stokes-dt-bps-bridge` (beans qou-bk77 / qou-qu53 / qou-48dw).

═══ THE FAMILY IT COVERS, AND WHY 5_2 IS NOT IN IT ═══

The paper parametrises double twist knots as `K(p,-m)` for positive integers
`p, m`, and gives (its eq (5), section II.A) the family's Alexander polynomial
in ONE parameter:

    Delta_{K(p,-m)}(x) = 1 - (p*m) * X,        X = (1-x)^2 / x

That single formula is the whole obstruction. Evaluate at `x = -1`:

    X(-1) = (1-(-1))^2 / (-1) = 4 / (-1) = -4
    Delta(-1) = 1 + 4*p*m

and the knot determinant is `det(K) = |Delta(-1)|`, so

    **every member of the family has det = 1 + 4*p*m == 1 (mod 4).**

`5_2` has determinant **7**, and `7 == 3 (mod 4)`. So `5_2` is not `K(p,-m)`
for ANY positive integers `p, m`.

This is a **scope-(b) structural exclusion**, not a scope-(a) "we looked and did
not find it": the invariant is the knot determinant mod 4, it is cited, and it
rules out the entire two-parameter family at once rather than the finitely many
members the paper happens to tabulate. The same argument excludes `3_1` (det 3)
and `7_2` (det 11) -- consistent with the paper's own worked twist-knot list
being `4_1, 6_1, 8_1` (dets 5, 9, 13) and never the odd-index twist knots.

═══ THE FORMULA IS CONFIRMED BY THE PAPER'S OWN KNOT LIST ═══

`det = 1 + 4*p*m` is not taken on trust. Every knot the paper names, with the
`(p,m)` it assigns, reproduces its measured determinant exactly (C4 below):

    K(1,-1) = 4_1    pm=1 -> 5    measured 5
    K(2,-1) = 6_1    pm=2 -> 9    measured 9
    K(3,-1) = 8_1    pm=3 -> 13   measured 13
    K(2,-2) = 8_3    pm=4 -> 17   measured 17
    K(3,-2) = 10_3   pm=6 -> 25   measured 25

Five for five, from a formula fitted to none of them.

═══ THE GUARD, AND IT IS THE IMPORTANT PART ═══

Even a sourced 5_2 quiver would NOT be eq (98). Both held sources build
**symmetric** quivers -- KRSS section 2 ("known for symmetric quivers, i.e. such
that ..."), and the double-twist paper's introduction states it outright
("quivers are symmetric quivers. That is, C(K) ..."). GGM eq (98) is
**antisymmetric**. A symmetric integral form and an antisymmetric one are
different objects; matching them would be the same category error this arc has
already hit at least seven times, most recently reading a matrix's SIZE as its
RANK (#6643).

So the rung's target is not merely unsourced -- the obvious source would be the
wrong object even if it existed.

═══ PREDICTIONS, RECORDED BEFORE MEASURING ═══

  P1  the determinant routine, calibrated on 8 knots of known determinant,
      reproduces all 8
  P2  every knot the paper names has det == 1 (mod 4)
  P3  5_2 has det == 3 (mod 4), hence is excluded
  P4  the 1+4pm formula reproduces all five named (p,m) assignments

Exact integer arithmetic throughout (Fraction-based Gaussian elimination on
integer Seifert matrices); no floats.
"""
from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

LIB = REPO / "library"
DOC_DT = "physrevd108106023"           # double twist knots
DOC_KRSS = "arxiv-1707.02991v1"        # BPS states, knots and quivers

# The paper's own (p, m) -> knot assignments, read from its Table I and
# section III worked examples.
PAPER_FAMILY = {
    "4_1": (1, 1),
    "6_1": (2, 1),
    "8_1": (3, 1),
    "8_3": (2, 2),
    "10_3": (3, 2),
}

# Independently-known determinants, used ONLY to calibrate the routine.
KNOWN_DET = {
    "3_1": 3, "4_1": 5, "5_2": 7, "6_1": 9,
    "7_2": 11, "8_1": 13, "8_3": 17, "10_3": 25,
}


def det_exact(M):
    """Exact determinant by fraction-free-ish Gaussian elimination over Q."""
    n = len(M)
    A = [[Fraction(x) for x in row] for row in M]
    d = Fraction(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            d = -d
        d *= A[c][c]
        inv = A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / inv
            if f:
                A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return d


def knot_determinant(name):
    """|det(V + V^T)| from a Seifert matrix -- exact integers."""
    import spherogram
    V = spherogram.Link(name).seifert_matrix()
    n = len(V)
    S = [[V[i][j] + V[j][i] for j in range(n)] for i in range(n)]
    d = det_exact(S)
    assert d.denominator == 1, f"{name}: non-integral determinant {d}"
    return abs(d.numerator)


def family_det(p, m):
    """det = |Delta(-1)| for K(p,-m), from the paper's eq (5)."""
    return 1 + 4 * p * m


def grep_doc(doc_id, pattern):
    """Count matching lines across a library document's section text."""
    root = LIB / doc_id / "sections"
    if not root.is_dir():
        return None
    rx = re.compile(pattern, re.I)
    hits = []
    for f in sorted(root.glob("*.md")):
        for i, line in enumerate(f.read_text(errors="replace").splitlines(), 1):
            if rx.search(line):
                hits.append(f"{f.name}:{i}")
    return hits


def main():
    checks = []
    print(__doc__.split("═══ PREDICTIONS")[0].rstrip())

    # ── C1: both sources are actually held ──────────────────────────────
    held = {d: (LIB / d / "sections").is_dir() for d in (DOC_DT, DOC_KRSS)}
    ok = all(held.values())
    print("\n  ── C1: both knots-quivers sources are held ──")
    for d, h in held.items():
        print(f"     {d:<24} sections/ present: {h}")
    checks.append((ok, "both_sources_held",
                   "physrevd108106023 (double twist knots) and arxiv-1707.02991v1 "
                   "(KRSS) both have ingested section text, so the corpus-grep "
                   "path 5 can see them"))

    # ── C2: the determinant routine is calibrated ───────────────────────
    dets = {k: knot_determinant(k) for k in KNOWN_DET}
    hits = [(k, dets[k], KNOWN_DET[k]) for k in KNOWN_DET]
    ok = all(a == b for _, a, b in hits)
    print("\n  ── C2: determinant routine calibrated on 8 known knots (P1) ──")
    print("     knot    det  known  match")
    for k, a, b in hits:
        print(f"     {k:<6} {a:>4} {b:>6}  {a == b}")
    checks.append((ok, "determinant_routine_calibrated",
                   f"|det(V+V^T)| from exact integer Seifert matrices reproduces "
                   f"all {len(hits)} independently-known determinants; the routine "
                   "is measuring what it claims to before it is used on anything"))

    # ── C3: the family formula reproduces every named assignment ────────
    print("\n  ── C3: 1+4pm reproduces the paper's own five knots (P4) ──")
    print("     knot     (p,m)  1+4pm  measured  match")
    rows = []
    for k, (p, m) in PAPER_FAMILY.items():
        pred, meas = family_det(p, m), dets[k]
        rows.append((k, p, m, pred, meas))
        print(f"     {k:<7} ({p},{m})  {pred:>5}  {meas:>8}  {pred == meas}")
    ok = all(pred == meas for _, _, _, pred, meas in rows)
    checks.append((ok, "family_formula_confirmed",
                   "the paper's eq (5) Alexander form gives det = |Delta(-1)| = "
                   "1+4pm; all five of its own named (p,m) assignments reproduce "
                   "their measured determinants exactly, from a formula fitted to "
                   "none of them"))

    # ── C4: every family member is 1 mod 4 ──────────────────────────────
    residues = sorted({family_det(p, m) % 4
                       for p in range(1, 40) for m in range(1, 40)})
    ok = residues == [1]
    print("\n  ── C4: the whole family is det == 1 (mod 4) (P2) ──")
    print(f"     residues of 1+4pm over 1<=p,m<=39: {residues}")
    print("     (algebraically immediate: 1+4pm == 1 mod 4 for every integer pm)")
    checks.append((ok, "family_is_one_mod_four",
                   "det = 1+4pm is congruent to 1 mod 4 for EVERY positive p,m -- "
                   "so this rules out the entire two-parameter family, not merely "
                   "the finitely many members the paper tabulates"))

    # ── C5: 5_2 is excluded — scope (b) ─────────────────────────────────
    d52 = dets["5_2"]
    ok = d52 % 4 == 3
    print("\n  ── C5: 5_2 is EXCLUDED from K(p,-m) — scope (b) (P3) ──")
    print(f"     det(5_2) = {d52},  {d52} mod 4 = {d52 % 4}")
    print("     the family admits only 1 mod 4, so no (p,m) gives 5_2.")
    print("     invariant cited: the knot determinant mod 4.")
    others = {k: dets[k] for k in ("3_1", "7_2")}
    print(f"     same argument excludes {others} (both 3 mod 4)")
    checks.append((ok, "five_two_structurally_excluded",
                   f"det(5_2) = {d52} == 3 (mod 4) while every K(p,-m) has det == "
                   "1 (mod 4). SCOPE (b): a proved invariant (determinant mod 4) "
                   "excludes the whole family, not a search that came up empty. "
                   "3_1 (3) and 7_2 (11) fall the same way, matching the paper's "
                   "worked twist-knot list being 4_1/6_1/8_1 and never the "
                   "odd-index twist knots"))

    # ── C6: KRSS works only the trefoil ─────────────────────────────────
    tref = grep_doc(DOC_KRSS, r"trefoil")
    five2 = grep_doc(DOC_KRSS, r"5[_ ]?2\b") or []
    ok = len(tref) > 0 and len(five2) == 0
    print("\n  ── C6: KRSS gives an explicit quiver for the trefoil only ──")
    print(f"     'trefoil' lines: {len(tref)}   '5_2' lines: {len(five2)}")
    print("     its section 3 is titled 'Example -- trefoil knot'")
    checks.append((ok, "krss_covers_trefoil_only",
                   f"{len(tref)} 'trefoil' hits and {len(five2)} '5_2' hits in "
                   "arxiv-1707.02991v1 section text; the correspondence paper "
                   "works one explicit example and it is not this knot"))

    # ── C7: the guard — symmetric vs antisymmetric ──────────────────────
    sym_dt = grep_doc(DOC_DT, r"quivers are symmetric quivers")
    sym_krss = grep_doc(DOC_KRSS, r"known for symmetric quivers")
    ok = len(sym_dt) > 0 and len(sym_krss) > 0
    print("\n  ── C7: even a sourced quiver would NOT be eq (98) ──")
    print(f"     'quivers are symmetric quivers'  in {DOC_DT}: {sym_dt}")
    print(f"     'known for symmetric quivers'    in {DOC_KRSS}: {sym_krss}")
    print("     GGM eq (98) is ANTISYMMETRIC. A symmetric integral form and an")
    print("     antisymmetric one are different objects. Identifying them would")
    print("     be the same category error as reading a matrix's SIZE as its")
    print("     RANK (#6643) -- the failure this arc keeps hitting.")
    checks.append((ok, "symmetric_vs_antisymmetric_guard",
                   "both held sources state in their own words that their quivers "
                   "are SYMMETRIC; eq (98) is ANTISYMMETRIC. So the rung's target "
                   "is not merely unsourced -- the obvious source would be the "
                   "wrong object even if it existed"))

    wb = WitnessBuilder("d1b-52-charge-lattice-source-exclusion",
                        engine="exact-integer-seifert-determinant-plus-corpus-grep")
    wb.set_description(
        "qou-rutm. The rung asked for a charge lattice for the 5_2 flavour. "
        "ANSWER: it is NOT sourceable from the held knots-quivers literature, and "
        "the exclusion is STRUCTURAL rather than a failed search. The corpus holds "
        "two knots-quivers sources: KRSS (arxiv-1707.02991v1), which works the "
        "trefoil only, and Singh et al. (physrevd108106023), which gives explicit "
        "symmetric quiver matrices for the double twist family K(p,-m). That "
        "family's Alexander polynomial is Delta = 1 - pm*(1-x)^2/x (its eq (5)), so "
        "det = |Delta(-1)| = 1+4pm == 1 (mod 4) for every positive p,m. det(5_2) = "
        "7 == 3 (mod 4), so 5_2 is in no member of the family -- SCOPE (b), "
        "invariant cited (determinant mod 4), excluding the whole two-parameter "
        "family rather than the tabulated members. The formula is confirmed by the "
        "paper's own five named (p,m) assignments, all reproduced exactly. GUARD: "
        "both sources build SYMMETRIC quivers and eq (98) is ANTISYMMETRIC, so a "
        "sourced 5_2 quiver would be the wrong object anyway.")
    wb.add_data("sources_held", held)
    wb.add_data("determinants_measured", dets)
    wb.add_data("determinant_calibration", {
        "method": "|det(V + V^T)| with V an exact integer Seifert matrix from "
                  "spherogram, determinant by Fraction-based elimination",
        "known_values": KNOWN_DET,
        "matches": sum(1 for k in KNOWN_DET if dets[k] == KNOWN_DET[k]),
        "of": len(KNOWN_DET),
        "why_calibrated_first": "the routine is verified against independently "
                                "known values BEFORE any conclusion rests on it",
    })
    wb.add_data("family", {
        "parametrisation": "K(p,-m), positive integers p,m",
        "alexander_form": "Delta(x) = 1 - p*m*(1-x)^2/x   [paper eq (5)]",
        "determinant_form": "det = |Delta(-1)| = 1 + 4*p*m",
        "named_assignments": {k: {"p": p, "m": m, "predicted_det": family_det(p, m),
                                  "measured_det": dets[k]}
                              for k, (p, m) in PAPER_FAMILY.items()},
        "residue_class": "1 (mod 4), for every positive p,m",
    })
    wb.add_data("exclusion", {
        "knot": "5_2",
        "determinant": d52,
        "residue_mod_4": d52 % 4,
        "family_residue_mod_4": 1,
        "verdict": "5_2 is not K(p,-m) for any positive integers p,m",
        "scope": "(b) structural exclusion",
        "invariant_cited": "knot determinant mod 4",
        "why_b_and_not_a": "the argument rules out the entire two-parameter "
                           "family from an invariant, not the finitely many "
                           "members that happen to be tabulated",
        "also_excluded": {k: dets[k] for k in ("3_1", "7_2")},
        "consistency_check": "the paper's worked twist-knot list is 4_1/6_1/8_1 "
                             "(dets 5/9/13, all 1 mod 4) and never the odd-index "
                             "twist knots -- exactly what this predicts",
    })
    wb.add_data("guard_symmetric_vs_antisymmetric", {
        "held_sources_build": "SYMMETRIC quivers (both say so in their own words)",
        "ggm_eq_98_is": "ANTISYMMETRIC",
        "consequence": "a sourced 5_2 quiver would not be eq (98); the two are "
                       "different objects, not two presentations of one",
        "failure_class": "matching an object by shape rather than by structure -- "
                         "the class that produced the merged 'eq (98) is rank 3' "
                         "error (a matrix SIZE read as a RANK), corrected in #6643",
    })
    wb.add_data("what_this_does_not_settle", {
        "not_claimed": "that no 5_2 quiver exists anywhere in the literature",
        "measured_scope": "the two knots-quivers documents THIS corpus holds",
        "disconfirmation": "an explicit 5_2 quiver matrix from any source would "
                           "settle the sourcing question -- but C7 stands "
                           "regardless, since it would still be symmetric",
        "open": "whether the A_omega/Route-C programme needs a charge lattice at "
                "all once eq (98)'s radical is known to be the mirror-symmetric "
                "direction (#6676)",
    })
    wb.add_data("scope", {
        "tier": "one scope-(b) exclusion (C5) + calibration (C2) + corpus "
                "measurement (C1, C6, C7)",
        "arithmetic": "exact integers and Fractions; no floats",
        "derives_A_omega": False, "wired": False, "fit": False,
    })
    for ok_, name, detail in checks:
        wb.add_assertion(name, computed="PASS" if ok_ else "FAIL",
                         expected="PASS", tolerance="exact", source=detail)
    wb.save(extra={"q0Anchor": "independent", "q0AnchorReason": (
            "structural exclusion over exact Fractions and a text scan of library sections; q0 is never read")})

    n_ok = sum(1 for ok_, _, _ in checks if ok_)
    print(f"\n  {n_ok}/{len(checks)} checks passed")
    return 0 if n_ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
