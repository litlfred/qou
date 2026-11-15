"""Is the branch-point count 6 of the chi(A) = -6 chain FORCED, or merely IN RANGE?

Bean `qou-qhcr`.  Exact-arithmetic companion to the sorry-free Lean file
`QOU/BringsSurface/BranchPointSixNotForced.lean`; this probe re-derives the same
arithmetic by an independent route (rational orbifold Euler characteristics with
`fractions.Fraction`, rather than the cleared-denominator integer form the Lean
uses) so a slip in either is visible as a disagreement.

## The question

`ex:chi-minus-six-derivation` (`brings-surface/chi-minus-six-chain.md`) reaches
`chi(A) = -6` in eight steps.  Steps 1-4 and 6-8 are axiom consequences.  Step 5
-- "the Frobenius-Hopf structure forces the algebra to have exactly 6 branch
points in its geometric descent (from the S_3 subset S_5 orbits on the 6
Weierstrass points of Bring's surface)" -- is not, and the block says so.

AGENTS.md "Defined residual != derived decomposition" check 2 asks, of any such
feature: **is the value FORCED, or merely IN RANGE?**  That is what this probe
measures, on five candidate sources for the 6.

## What it decides

T1  How much Steps 3+4 constrain chi(A).                          -> infinite set
T2  Whether "six branch points" over P^1 fixes chi given degree.  -> genus 0..6
T3  Whether Bring's curve has 6 Weierstrass points.               -> no, 60
T4  Whether the torus-knot bracketing pair of                     -> every genus
    `EulerCharacteristicSix.lean` singles out g = 4.
T5  The ADE / finite-subgroup-of-SU(2) route: whether the         -> 6 is NOT an
    icosahedral case produces a 6 on P(V), and whether any           icosahedral
    single reading of "6" picks one ADE type.                        orbit size

Every number is an exact `int` or `Fraction`.  No float, no mpmath needed: the
whole computation is rational (AGENTS.md NO-FLOAT64 -- probes are not exempt).

Nothing here is fitted and nothing is wired.  The verdicts are scope-(a) or
scope-(b) per AGENTS.md "Before declaring refuted"; see `verdict` in the witness.

Sources for the classical inputs, all held in `library/`:
  * Braden & Disney-Hogg, "Bring's curve: old and new", Prop. 3.3 and the
    paragraph after it -- 60 Weierstrass points, Aut(B) = S_5 transitive,
    60 = 6 x 10.  `library/s40879-023-00706-0/sections/sec-008-31-weierstrass-points.md`
    (registered `[braden-disney-hogg-2022]`).
  * Laing & Singerman, "Transitivity on Weierstrass points", Ann. Acad. Sci.
    Fenn. Math. 37 (2012) Thm 15, quoted as Thm 3.4 of the above.
  * Klein, finite subgroups of SU(2) and their cone orders (`[klein1888]`).
"""

from __future__ import annotations

import sys
import time
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402


# --------------------------------------------------------------------------
# The ADE list, by the rotation group it covers in SO(3) = SU(2)/{+-1}.
# `dihedral n` is meant for n >= 2; D_1 is cyclic of order 2.
# --------------------------------------------------------------------------
def ade_families(cyclic_ns=(2, 3, 5, 7), dihedral_ns=(2, 3, 4, 5, 6, 7)):
    """(label, |rotation group|, cone orders) for every ADE family."""
    out = []
    for n in cyclic_ns:
        out.append((f"cyclic_{n}", n, (n, n)))
    for n in dihedral_ns:
        out.append((f"dihedral_{n}", 2 * n, (2, 2, n)))
    out.append(("tetrahedral_E6", 12, (2, 3, 3)))
    out.append(("octahedral_E7", 24, (2, 3, 4)))
    out.append(("icosahedral_E8", 60, (2, 3, 5)))
    return out


def exceptional_orbit_sizes(order: int, cones: tuple[int, ...]) -> list[int]:
    """Orbit over the cone point of order m has size |G|/m (exact integer)."""
    sizes = []
    for m in cones:
        assert order % m == 0, f"cone order {m} does not divide |G| = {order}"
        sizes.append(order // m)
    return sizes


def orbifold_euler_char(order: int, cones: tuple[int, ...]) -> Fraction:
    """chi_orb(P(V)/G) = 2 - sum_i (1 - 1/m_i).  Exact rational."""
    chi = Fraction(2)
    for m in cones:
        chi -= (1 - Fraction(1, m))
    return chi


def sylow_candidates(index_bound: int, p: int) -> list[int]:
    """n_p divides |G|/p and n_p = 1 (mod p).  Sylow's theorems, exact."""
    return [n for n in range(1, index_bound + 1)
            if index_bound % n == 0 and n % p == 1]


def euler_char(g: int) -> int:
    return 2 - 2 * g


def chi_of_cover(d: int, h: int, R: int) -> int:
    """Riemann-Hurwitz: chi(total) = d*(2 - 2h) - R, R the TOTAL ramification."""
    return d * (2 - 2 * h) - R


def seifert_rank_two(s: int) -> int:
    """rank H_1(Seifert(T_{2,s})) = (2-1)(s-1)/2 = (s-1)//2."""
    return (s - 1) // 2


def main() -> int:
    t0 = time.monotonic()
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append((name, bool(ok), detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")

    print("T1  How much do Steps 3+4 constrain chi(A)?")
    # Step 3: chi = 2 - 2g (Riemann-Roch).  Step 4: g >= 1.
    t1_admissible = [euler_char(g) for g in range(1, 21)]
    check("T1_admissible_set_is_even_nonpositive",
          all(c <= 0 and c % 2 == 0 for c in t1_admissible),
          f"g = 1..20 gives chi in {t1_admissible[:6]} ... (even, <= 0)")
    check("T1_minus_six_not_singled_out",
          -6 in t1_admissible and -4 in t1_admissible and -8 in t1_admissible,
          "-4, -6 and -8 are all admissible; Step 5 alone picks -6 "
          "out of a countably infinite set")

    print("\nT2  Does 'six branch points' over P^1 fix chi, given the degree?")
    # The corpus's own datum is a cover of P^1: brings-qou-4tuple.md:15 (degree 3,
    # six branch points) and brings-is-qou-verification.md:15 (degree 4, six branch
    # points, R = 14).  chi is fixed by the TOTAL RAMIFICATION R, not by b.
    d, b = 4, 6
    R_lo, R_hi = b, b * (d - 1)          # simple at every point .. total at every point
    t2_genus_range = sorted({(2 - chi_of_cover(d, 0, R)) // 2
                             for R in range(R_lo, R_hi + 1)
                             if chi_of_cover(d, 0, R) % 2 == 0})
    check("T2_six_points_degree_four_spans_genus_0_to_6",
          t2_genus_range == list(range(0, 7)),
          f"R in [{R_lo}, {R_hi}] gives genus {t2_genus_range} -- "
          "the branch COUNT alone determines nothing near g = 4")
    check("T2_corpus_R_is_what_gives_minus_six",
          chi_of_cover(4, 0, 14) == -6 and chi_of_cover(3, 0, 12) == -6,
          "chi = -6 needs R = 14 at d = 4 and R = 12 at d = 3; "
          "both corpus blocks are consistent only as different maps")

    print("\nT3  Does Bring's curve have 6 Weierstrass points?")
    # Non-hyperelliptic genus 4: all Weierstrass weights are 1, so the count is
    # the total weight g^3 - g.  Braden & Disney-Hogg Prop. 3.3.
    w_total = 4 ** 3 - 4
    check("T3_weierstrass_count_is_sixty",
          w_total == 60 and w_total != 6,
          f"g^3 - g at g = 4 is {w_total}, and Aut(B) = S_5 acts TRANSITIVELY "
          "on all of them -- so there is no set of six for an S_3 to act on")
    check("T3_sixty_splits_as_six_by_ten",
          w_total == 6 * 10,
          "60 = 6 x 10: six Weierstrass points fixed by each of the ten "
          "TRANSPOSITIONS in S_5 (same source, next paragraph) -- the real "
          "carrier of the 6 is an involution, not an S_3")
    # The repaired Step 5: degree-2 quotient by a transposition, 6 fixed points
    # (each contributing d - 1 = 1 to R), base genus 1.
    check("T3_transposition_quotient_gives_minus_six",
          chi_of_cover(2, 1, 6) == euler_char(4),
          "chi(B) = 2*chi(torus) - 6 = -6, so B/<tau> has genus 1 -- "
          "a coherent reading of Step 5, but still read off Bring")
    check("T3_ramification_six_not_forced_by_chi",
          chi_of_cover(2, 1, 6) == -6 and chi_of_cover(2, 2, 2) == -6
          and chi_of_cover(3, 2, 0) == -6,
          "(d,h,R) = (2,1,6), (2,2,2) and (3,2,0) all give -6: the 6 arrives "
          "with the choice of base genus, not from chi")

    print("\nT4  Does the torus-knot bracketing pair single out g = 4?")
    # EulerCharacteristicSix.lean: T_{2,9} must embed (rank 4 <= g), T_{2,11}
    # must not (rank 5 > g).  Correct arithmetic; but the SHAPE is generic.
    brackets = {g: (2 * g + 1, 2 * g + 3) for g in range(1, 13)}
    t4_ok = all(seifert_rank_two(lo) <= g and not seifert_rank_two(hi) <= g
                for g, (lo, hi) in brackets.items())
    check("T4_pair_brackets_every_genus", t4_ok,
          f"T_(2,2g+1)/T_(2,2g+3) brackets every g in 1..12; at g = 4 that pair "
          f"is {brackets[4]} -- exactly the corpus's (9, 11). The constraints "
          "restate the target rather than derive it")

    print("\nT5  The ADE route: does the icosahedral case produce a 6 on P(V)?")
    fams = ade_families()
    orbit_table = {}
    klein_ok = True
    for label, order, cones in fams:
        sizes = exceptional_orbit_sizes(order, cones)
        chi_orb = orbifold_euler_char(order, cones)
        # Klein's relation: chi_orb(P(V)/G) = 2/|G|, exactly.
        klein_ok = klein_ok and (chi_orb == Fraction(2, order))
        orbit_table[label] = {
            "rotation_order": order,
            "cone_orders": list(cones),
            "exceptional_orbit_sizes": sizes,
            "orbifold_euler_char": str(chi_orb),
            "contains_six": 6 in sizes,
        }
    check("T5_klein_relation_holds_for_every_family", klein_ok,
          "chi_orb = 2 - sum_i (1 - 1/m_i) = 2/|G| exactly for all "
          f"{len(fams)} families -- cross-checks every cone order and orbit size")

    ico = orbit_table["icosahedral_E8"]
    tet = orbit_table["tetrahedral_E6"]
    oct_ = orbit_table["octahedral_E7"]
    check("T5_six_is_NOT_an_icosahedral_orbit_size",
          not ico["contains_six"],
          f"icosahedral orbits are {ico['exceptional_orbit_sizes']} -- "
          "all >= 12, so no orbit reading of 'branch points on P(V)' "
          "can return 6 for E_8")
    check("T5_six_IS_a_tetrahedral_and_octahedral_orbit_size",
          tet["contains_six"] and oct_["contains_six"],
          f"tetrahedral {tet['exceptional_orbit_sizes']}, "
          f"octahedral {oct_['exceptional_orbit_sizes']} -- an orbit reading "
          "of 6 points AWAY from the icosahedral case")
    with_six = sorted(k for k, v in orbit_table.items() if v["contains_six"])
    check("T5_orbit_reading_does_not_pick_a_unique_type",
          len(with_six) > 1 and "icosahedral_E8" not in with_six,
          f"families with a 6-point exceptional orbit: {with_six}")

    # The Sylow reading: n_5(A_5) = 6 = |P^1(F_5)|.  Derived up to simplicity.
    syl5_a5 = sylow_candidates(60 // 5, 5)          # |A_5|/5 = 12 -> {1, 6}
    syl3_a4 = sylow_candidates(12 // 3, 3)          # |A_4|/3 = 4  -> {1, 4}
    syl3_s4 = sylow_candidates(24 // 3, 3)          # |S_4|/3 = 8  -> {1, 4}
    check("T5_sylow_arithmetic_leaves_two_candidates",
          syl5_a5 == [1, 6] and syl3_a4 == [1, 4] and syl3_s4 == [1, 4],
          f"n_5(A_5) in {syl5_a5}, n_3(A_4) in {syl3_a4}, n_3(S_4) in {syl3_s4}; "
          "simplicity of A_5 picks 6 -- that last input is cited, not derived")
    check("T5_sylow_and_orbit_readings_disagree",
          (6 in syl5_a5) and (not ico["contains_six"])
          and tet["contains_six"] and (6 not in syl3_a4),
          "on the icosahedral group the Sylow reading gives 6 and the orbit "
          "reading does not; on the tetrahedral group the orbit reading gives 6 "
          "and the Sylow reading does not. 6 is a property of the CHOSEN "
          "INVARIANT, not of the ADE type")

    # Genericity of 6 among A_5's natural integer invariants: is 6 special for
    # A_5, or does A_5 produce a 6 the way any group produces any small number?
    a5_invariants = {
        "irreducible_representation_dimensions": [1, 3, 3, 4, 5],
        "conjugacy_class_sizes": [1, 15, 20, 12, 12],
        "exceptional_orbit_sizes_on_P1": ico["exceptional_orbit_sizes"],
        "sylow_counts_p2_p3_p5": [5, 10, 6],
    }
    a5_all = [v for vals in a5_invariants.values() for v in vals]
    a5_sixes = [k for k, vals in a5_invariants.items() if 6 in vals]
    check("T5_six_occurs_once_among_A5_invariants",
          a5_sixes == ["sylow_counts_p2_p3_p5"],
          f"of {len(a5_all)} natural integer invariants of A_5, exactly "
          f"{a5_all.count(6)} equals 6, and it is n_5. So 6 is not generic for "
          "A_5 -- but it is also not selected by anything in the axioms")

    print("\nT6  The one narrowing that is not a read-off (Laing-Singerman).")
    # Thm 15: genus > 2 with g^3 - g Weierstrass points on which Aut is
    # transitive => Bring (g=4), Klein (g=3), or a genus-3 curve with Aut = S_4.
    ls_genera = [3, 4]
    ls_chi = [euler_char(g) for g in ls_genera]
    ls_aut_orders = {"bring_g4": 120, "klein_g3": 168, "s4_curve_g3": 24}
    check("T6_transitivity_narrows_chi_to_two_values",
          ls_chi == [-4, -6],
          f"homogeneity narrows chi(A) from the infinite set of T1 to {ls_chi}")
    order_five = {k: (v % 5 == 0) for k, v in ls_aut_orders.items()}
    check("T6_order_five_selects_bring",
          order_five == {"bring_g4": True, "klein_g3": False, "s4_curve_g3": False},
          "by Cauchy an order-5 automorphism exists iff 5 | |Aut|: "
          f"{ls_aut_orders} -- only the genus-4 case qualifies")

    all_passed = all(ok for _, ok, _ in checks)
    print(f"\n  {sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks passed")

    witness = {
        "name": "chi-branch-point-count-genericity",
        "description": (
            "Is the branch-point count 6 of the chi(A) = -6 chain FORCED or "
            "merely IN RANGE? Exact-rational genericity probe over five "
            "candidate sources, including the finite-subgroup/ADE route. "
            "Companion to the sorry-free Lean "
            "QOU/BringsSurface/BranchPointSixNotForced.lean."),
        "audit_only": True,
        "tier": ("exact structural probe (no fit, nothing wired; scope-(a)/(b) "
                 "framing per AGENTS.md)"),
        "bean": "qou-qhcr",
        "arithmetic": "exact int / fractions.Fraction throughout; no float64",
        "T1_step34_admissible_chi_g_1_to_20": t1_admissible,
        "T2_degree": d,
        "T2_branch_points": b,
        "T2_total_ramification_range": [R_lo, R_hi],
        "T2_genus_range_admitted": t2_genus_range,
        "T3_weierstrass_total_weight_genus_four": w_total,
        "T3_split": {"per_transposition": 6, "transpositions_in_S5": 10},
        "T3_repaired_step5": {
            "degree": 2, "base_genus": 1, "total_ramification": 6,
            "chi": chi_of_cover(2, 1, 6)},
        "T3_other_triples_giving_minus_six": [
            {"d": 2, "h": 2, "R": 2}, {"d": 3, "h": 2, "R": 0}],
        "T4_bracketing_pairs": {str(g): list(p) for g, p in brackets.items()},
        "T5_ade_orbit_table": orbit_table,
        "T5_families_with_six_point_orbit": with_six,
        "T5_sylow_candidates": {
            "n5_A5": syl5_a5, "n3_A4": syl3_a4, "n3_S4": syl3_s4},
        "T5_A5_natural_invariants": a5_invariants,
        "T6_transitivity_admissible_genera": ls_genera,
        "T6_transitivity_admissible_chi": ls_chi,
        "T6_aut_orders": ls_aut_orders,
        "T6_has_order_five_element": order_five,
        "checks": [{"name": n, "passed": ok, "detail": det}
                   for n, ok, det in checks],
        "allPassed": all_passed,
        "verdict": {
            "branch_point_count_six_derived": False,
            "ade_route_scope": (
                "scope-(b) for the SPECIFIC implication 'icosahedral type => six "
                "branch points on P(V)': the invariant is the orbit-size formula "
                "|G|/m_i and it is proved, and the icosahedral orbits are "
                "30/20/12. NOT a claim that no finite-group route can produce a "
                "6 -- three other ADE types do."),
            "finiteness_gap": (
                "su2_emergence_rank_forced constrains G only by 'unitary and "
                "det 1', which SU(2) itself satisfies. The ADE list classifies "
                "FINITE subgroups, so it does not apply to the object the axioms "
                "deliver. This is prior to the type question."),
            "sharpest_open_statement": (
                "Steps 3+4 pin chi(A) to the non-positive even integers and no "
                "further; every candidate source tested here either restates the "
                "target (torus-knot brackets, T4), reads it off Bring (Weierstrass "
                "/ transposition fixed points, T3), or fails to produce a 6 at all "
                "(ADE orbits, T5). The one hypothesis that narrows without naming "
                "6 is transitivity of Aut on the Weierstrass points, which gives "
                "chi in {-4, -6} (T6); separating those two needs an order-5 "
                "automorphism. Both are group-theoretic and neither is derived "
                "from the five QOU axioms."),
        },
    }
    # q0 anchor: this producer never reads q0. Every quantity is an integer or an
    # exact Fraction of integers (genus, branch counts, group orders, cone orders,
    # Sylow counts); no substrate parameter enters the import cone, so there is no
    # muon/proton layer to declare. `independent` is the producer-declared token
    # for exactly that state -- see computations/audits/q0_anchor_consistency_audit.py
    # (AGENTS.md q0-anchor convention rule 4, "say which pin you used").
    out = WitnessBuilder.wrap_legacy(
        "chi-branch-point-count-genericity", witness,
        script_path=__file__, engine="python", start_time=t0,
    ).save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "q0-free: the probe is exact integer / Fraction combinatorics "
            "(Euler characteristics, Riemann-Hurwitz, finite-rotation-group "
            "orbit and Sylow counts). No substrate parameter is read anywhere "
            "in the import cone, so neither the ideal-muon nor the "
            "physical-proton layer applies."),
    })
    print(f"  Witness: {out}  ({time.monotonic() - t0:.1f}s)")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
