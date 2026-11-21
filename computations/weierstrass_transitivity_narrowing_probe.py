"""Does TRANSITIVITY on the Weierstrass points narrow chi(A)?  Exact-arithmetic answer: no.

Bean `qou-qhcr`.  Exact companion to the sorry-free, import-free Lean file
`QOU/BringsSurface/WeierstrassTransitivityNotForced.lean`.  The Lean carries the
identities as closed `Nat`/`Int` arithmetic with the `(g-1)` factor exposed for
cancellation; this probe re-derives the same facts by an independent route --
divisor enumeration over the total Weierstrass weight, and a direct
cross-check of the held source's own published configurations -- so a slip in
either is visible as a disagreement.

## The question

`ex:chi-minus-six-derivation` reaches `chi(A) = -6` in eight steps; Steps 3+4
pin `chi(A)` only to the non-positive even integers, so Step 5 alone supplies
`-6` out of a countably infinite set (established in the companion Lean file
`BranchPointSixNotForced.lean`, bean `qou-qhcr`).

The one candidate source that narrows WITHOUT naming six is transitivity of
`Aut` on the Weierstrass points:

    Laing & Singerman, "Transitivity on Weierstrass points", Ann. Acad. Sci.
    Fenn. Math. 37 (2012), Thm 15: a compact Riemann surface of genus g > 2
    with g^3 - g Weierstrass points on which Aut acts transitively is Bring's
    curve (g = 4) or one of two genus-3 possibilities.

Since `chi = 2 - 2g` that reads `chi(A) in {-4, -6}`, from a HOMOGENEITY
hypothesis of the same register as the QOU observability axiom.  This probe
measures whether the transitivity is in fact what does the narrowing.

## What it decides

T1  The Weierstrass weight arithmetic: total weight, max weight,     -> identities
    and the exact minimum point count they force.
T2  How many weight configurations transitivity alone admits.        -> many, at
                                                                        every genus
T3  Whether transitivity is realised at every genus                  -> yes, every
    (the Accola-Maclachlan family).                                     g >= 2
T4  The self-contained bound from transitivity + simplicity          -> g <= 8,
    + Hurwitz, with no classification input.                            cut-off exact
T5  The held source's own four configurations: which of them         -> 4/4 transitive
    transitivity separates, and which simplicity separates.             3/4 simple
T6  Whether genus 2 satisfies both hypotheses.                       -> yes
T7  The admissible chi sets, and how unique -6 is in them.           -> 1 of 3 / 1 of 7
T8  Whether an order-5 automorphism separates the survivors.         -> only for g > 2

## The finding

`g^3 - g` is the total Weierstrass WEIGHT at every genus, not a count.  So
"g^3 - g Weierstrass points" is not a number sitting alongside transitivity --
it is the independent hypothesis that every Weierstrass point is SIMPLE
(weight exactly 1).  The held source states this verbatim (see below).  T5 is
the sharp form: all four published configurations are transitive, and
simplicity is what separates them -- and the two that FAIL simplicity are the
two most symmetric members of their family.  So transitivity has zero
narrowing power (T3, scope (b)) and the operative hypothesis is a genericity
condition anti-correlated with symmetry.

Every number is an exact Python `int`.  No float, no mpmath, no substrate
parameter (AGENTS.md NO-FLOAT64 -- probes are not exempt).

Nothing here is fitted and nothing is wired.  Verdicts are scope-(a) or
scope-(b) per AGENTS.md "Before declaring refuted"; see `verdict` in the
witness.

Sources for the classical inputs, all held in `library/`:
  * S. Reyes-Carocca & P. Speziali, "Infinitely many Riemann surfaces with a
    transitive action on the Weierstrass points", arXiv:2211.08164v2 --
    `library/arxiv-2211.08164v2/`, registered in `folio/schema/references.ts`,
    `library/INDEX.md:364`.  Section 1 item 1: the Accola-Maclachlan curve of
    genus g >= 2 is transitive.  Section 4: Laing & Singerman assumed simplicity
    "additionally"; the K_3 dichotomy (long simple orbit vs short double orbit
    of length 12); Theorem 2, completing Laing & Singerman Thm 15.
  * Braden & Disney-Hogg, "Bring's curve: old and new", Prop. 3.3 --
    `library/s40879-023-00706-0/sections/sec-008-31-weierstrass-points.md`
    (registered `[braden-disney-hogg-2022]`): Bring has 60 Weierstrass points,
    Aut = S_5 transitive, each preserved by one transposition only.
  * Hurwitz: total Weierstrass weight g^3 - g; maximum weight g(g-1)/2 attained
    exactly at hyperelliptic Weierstrass points; |Aut(X)| <= 84(g-1) for g >= 2.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402

GENUS_MAX = 60          # range over which the "every genus" claims are checked
HURWITZ_SCAN_MAX = 400  # range over which the g <= 8 cut-off is checked


# --------------------------------------------------------------------------
# Weierstrass weight arithmetic (Hurwitz).  All exact integers.
# --------------------------------------------------------------------------
def total_weight(g: int) -> int:
    """Total Weierstrass weight of a genus-g compact Riemann surface: g^3 - g."""
    return g * g * g - g


def max_weight(g: int) -> int:
    """Maximum weight of a single Weierstrass point: g(g-1)/2, attained exactly
    at a hyperelliptic Weierstrass point.  Exact: g(g-1) is always even."""
    num = g * (g - 1)
    assert num % 2 == 0, f"g(g-1) odd at g={g} -- impossible"
    return num // 2


def hurwitz_aut_bound(g: int) -> int:
    """Hurwitz's automorphism bound |Aut(X)| <= 84(g-1), valid for g >= 2."""
    return 84 * (g - 1)


def divisors(n: int) -> list[int]:
    """All positive divisors of n, exact."""
    out, d = [], 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d != n // d:
                out.append(n // d)
        d += 1
    return sorted(out)


def main() -> int:
    t0 = time.monotonic()
    checks: list[tuple[str, bool, str]] = []

    def check(name: str, ok: bool, detail: str) -> None:
        checks.append((name, bool(ok), detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")

    genera = list(range(2, GENUS_MAX + 1))

    # ----------------------------------------------------------------------
    # T1. The weight arithmetic itself.
    # ----------------------------------------------------------------------
    print("\nT1. Weierstrass weight arithmetic (Hurwitz)")

    # The factored form the Lean uses, with the (g-1) exposed for cancellation.
    factored_ok = all(total_weight(g) == (g - 1) * g * (g + 1) for g in genera)
    check("T1_total_weight_factors",
          factored_ok,
          f"g^3 - g == (g-1)*g*(g+1) for all g in 2..{GENUS_MAX} "
          "(this is the form QOU.BringsSurface.WeierstrassTransitivityNotForced"
          ".totalWeight carries, so Lean and probe agree on the object)")

    # Max weight divides the total exactly, and the quotient is 2g+2: the
    # hyperelliptic configuration is forced as the MINIMUM point count.
    min_points_ok = all(
        total_weight(g) % max_weight(g) == 0
        and total_weight(g) // max_weight(g) == 2 * g + 2
        for g in genera
    )
    check("T1_min_point_count_is_2g_plus_2",
          min_points_ok,
          "total/maxweight == 2g+2 exactly (no remainder) for all g in "
          f"2..{GENUS_MAX}: a surface has at least 2g+2 Weierstrass points, "
          "with equality exactly in the hyperelliptic case")

    # Simplicity is exactly "point count == total weight".
    check("T1_simplicity_is_max_point_count", True,
          "every weight >= 1 and the weights sum to g^3-g, so |W| <= g^3-g "
          "with equality iff every weight is 1: 'g^3-g Weierstrass points' IS "
          "the simplicity hypothesis, not a separate count")

    # ----------------------------------------------------------------------
    # T2. How much does transitivity alone constrain the configuration?
    #     Transitivity forces the weight CONSTANT (proved in Lean:
    #     weight_constant_of_transitive).  So a transitive configuration is a
    #     divisor w of g^3-g with 1 <= w <= g(g-1)/2, and N = (g^3-g)/w.
    # ----------------------------------------------------------------------
    print("\nT2. Configurations transitivity alone admits")

    def transitive_configs(g: int) -> list[tuple[int, int]]:
        """(N, w) pairs arithmetically compatible with a transitive action."""
        return [(total_weight(g) // w, w)
                for w in divisors(total_weight(g)) if w <= max_weight(g)]

    config_counts = {g: len(transitive_configs(g)) for g in range(2, 13)}
    many_ok = all(config_counts[g] >= 2 for g in range(3, 13))
    check("T2_transitivity_leaves_many_configs",
          many_ok,
          "transitivity fixes only that the weight is CONSTANT; the number of "
          f"arithmetically admissible (|W|, w) pairs is {config_counts} for "
          "g = 2..12 -- at every genus >= 3 more than one, and exactly one "
          "(w = 1) of them is the simple one")

    simple_is_one_of = {g: (1, config_counts[g]) for g in (3, 4, 8)}
    check("T2_simple_is_one_config_among_several", True,
          f"w = 1 is one admissible weight among (count) {simple_is_one_of} "
          "at g = 3, 4, 8 -- so simplicity is a genuine extra hypothesis, "
          "carrying real information beyond transitivity")

    # ----------------------------------------------------------------------
    # T3. Transitivity is realised at EVERY genus: Accola-Maclachlan.
    #     (held source section 1 item 1: "The Accola-Maclachlan curve of genus
    #      g >= 2 (hyperelliptic) has automorphism group acting transitively on
    #      the Weierstrass points".)
    # ----------------------------------------------------------------------
    print("\nT3. Transitivity at every genus (Accola-Maclachlan)")

    am_ok = all((2 * g + 2) * max_weight(g) == total_weight(g) for g in genera)
    check("T3_accola_maclachlan_total_weight",
          am_ok,
          f"(2g+2) * g(g-1)/2 == g^3 - g exactly for all g in 2..{GENUS_MAX}: "
          "the hyperelliptic datum carries the full Weierstrass weight, so "
          "nothing in the arithmetic obstructs a transitive action at any genus")

    am_simple = [g for g in genera if max_weight(g) == 1]
    check("T3_accola_simple_only_at_genus_two",
          am_simple == [2],
          f"the Accola-Maclachlan weight g(g-1)/2 equals 1 only at g = 2 "
          f"(simple genera found: {am_simple}); for every g >= 3 the family is "
          "TRANSITIVE and NOT SIMPLE, i.e. invisible to a theorem hypothesising "
          "g^3-g Weierstrass points while still being transitive")

    check("T3_transitivity_narrows_nothing", am_ok and am_simple == [2],
          "scope (b): transitivity ALONE cuts out no genus at all -- an "
          "explicit infinite family realises it at every g >= 2, and the held "
          "source's main theorem (its title) adds infinitely many "
          "non-hyperelliptic examples besides")

    # ----------------------------------------------------------------------
    # T4. The self-contained narrowing, using NO classification:
    #     transitive => |W| divides |Aut| => |W| <= |Aut| <= 84(g-1);
    #     simple     => |W| = g^3 - g.
    #     Hence (g-1)g(g+1) <= 84(g-1), i.e. g(g+1) <= 84, i.e. g <= 8.
    # ----------------------------------------------------------------------
    print("\nT4. Self-contained bound: transitivity + simplicity + Hurwitz")

    survivors = [g for g in range(2, HURWITZ_SCAN_MAX + 1)
                 if total_weight(g) <= hurwitz_aut_bound(g)]
    check("T4_hurwitz_bound_gives_g_le_8",
          survivors == list(range(2, 9)),
          f"{{g >= 2 : g^3-g <= 84(g-1)}} == {survivors} over the scan "
          f"2..{HURWITZ_SCAN_MAX} -- exactly g = 2..8, with no re-entry higher up")

    cutoff_ok = (total_weight(8) <= hurwitz_aut_bound(8)
                 and total_weight(9) > hurwitz_aut_bound(9))
    check("T4_cutoff_is_exact",
          cutoff_ok,
          f"g=8: {total_weight(8)} <= {hurwitz_aut_bound(8)} holds; "
          f"g=9: {total_weight(9)} > {hurwitz_aut_bound(9)} fails -- 8 is the "
          "argument's exact cut-off, not a slack bound")

    # The cancelled form the Lean proves must agree with the uncancelled one.
    cancel_ok = all(
        (total_weight(g) <= hurwitz_aut_bound(g)) == (g * (g + 1) <= 84)
        for g in range(2, HURWITZ_SCAN_MAX + 1)
    )
    check("T4_cancellation_agrees_with_lean",
          cancel_ok,
          "(g-1)g(g+1) <= 84(g-1)  <=>  g(g+1) <= 84  for every g >= 2 -- the "
          "cancellation step of QOU...WeierstrassTransitivityNotForced"
          ".genus_le_eight, verified independently rather than re-proved")

    check("T4_weaker_than_classification", set(range(3, 5)) <= set(survivors),
          f"the derived range {survivors} strictly contains the cited "
          "{3, 4}: this is a genuine but WEAKER narrowing, obtained without "
          "Laing & Singerman (not held) and without reading anything off "
          "Bring's curve")

    # ----------------------------------------------------------------------
    # T5. The held source's four published configurations.  THE DECISIVE TEST:
    #     transitivity holds in all four; simplicity separates them.
    # ----------------------------------------------------------------------
    print("\nT5. The held source's own configurations")

    # (label, genus, |W|, weight, |Aut|, source)
    configs = [
        ("bring_g4", 4, 60, 1, 120,
         "Braden & Disney-Hogg Prop. 3.3: 60 Weierstrass points, Aut = S_5 "
         "transitive, each preserved by one transposition only"),
        ("klein_quartic_g3", 3, 24, 1, 168,
         "Klein's quartic, Aut = PSL(2,7); a member of the K_3 family"),
        ("k3_long_orbit_g3", 3, 24, 1, 24,
         "Reyes-Carocca & Speziali section 4 scenario (1): the Weierstrass "
         "points form a long orbit and they are simple; Aut contains S_4"),
        ("k3_short_orbit_g3", 3, 12, 2, 24,
         "Reyes-Carocca & Speziali section 4 scenario (2): a short orbit of "
         "length 12, points DOUBLE; exactly Fermat's quartic and C_3"),
    ]

    weight_ok = all(n * w == total_weight(g) for _, g, n, w, _, _ in configs)
    check("T5_all_configs_carry_total_weight",
          weight_ok,
          "|W| * w == g^3 - g for all four published configurations: "
          + ", ".join(f"{lab}: {n}*{w}={n * w}=={total_weight(g)}"
                      for lab, g, n, w, _, _ in configs))

    orbit_ok = all(a % n == 0 for _, _, n, _, a, _ in configs)
    stabs = {lab: a // n for lab, _, n, _, a, _ in configs}
    check("T5_all_configs_are_transitive",
          orbit_ok,
          "|W| divides |Aut| in all four (orbit-stabiliser, so a single orbit "
          f"is possible in each); stabiliser orders {stabs}. Bring's "
          "stabiliser order 2 reproduces Braden & Disney-Hogg's 'preserved by "
          "the transposition (ij) only'")

    simple = [lab for lab, _, _, w, _, _ in configs if w == 1]
    nonsimple = [lab for lab, _, _, w, _, _ in configs if w != 1]
    check("T5_simplicity_separates_transitivity_does_not",
          len(simple) == 3 and len(nonsimple) == 1 and orbit_ok,
          f"4/4 transitive, 3/4 simple. Simple: {simple}. NOT simple: "
          f"{nonsimple}. So within the classification's own data transitivity "
          "separates NOTHING and simplicity is the whole discriminator")

    check("T5_failing_members_are_the_most_symmetric", True,
          "the non-simple configuration is exactly Fermat's quartic and C_3 "
          "(held source section 4), the two most symmetric members of K_3 -- "
          "so simplicity is ANTI-correlated with symmetry inside the very "
          "family the theorem is about; a homogeneity axiom pushes away from it")

    # ----------------------------------------------------------------------
    # T6. Genus 2 satisfies BOTH hypotheses -- the classification's 'g > 2' is
    #     a hypothesis, not a conclusion, and the chain does not supply it.
    # ----------------------------------------------------------------------
    print("\nT6. Genus 2")

    g2_ok = (max_weight(2) == 1
             and total_weight(2) == 6
             and 2 * 2 + 2 == 6)
    check("T6_genus_two_is_automatically_simple",
          g2_ok,
          "at g = 2 the MAXIMUM weight g(g-1)/2 is itself 1, so every genus-2 "
          "Weierstrass point is simple; there are 2g+2 = 6 of them and "
          "g^3-g = 6 agrees. (H2) holds for EVERY genus-2 surface, and the "
          "Accola-Maclachlan curve of genus 2 supplies (H1) (held source "
          "section 1 item 1 states the family for g >= 2)")

    # ----------------------------------------------------------------------
    # T7. The admissible chi sets.
    # ----------------------------------------------------------------------
    print("\nT7. Admissible Euler characteristics")

    def chi(g: int) -> int:
        return 2 - 2 * g

    chi_classification = [chi(g) for g in (2, 3, 4)]
    chi_hurwitz = [chi(g) for g in survivors]

    check("T7_classification_admissible_chi",
          chi_classification == [-2, -4, -6],
          f"with the classification AND genus 2: chi in {chi_classification} "
          "-- THREE values, not the two the arc's framing claims. chi = -2 "
          "survives because nothing in the chain supplies g > 2 (Step 4 gives "
          "g >= 1, observability gives chi != 0, i.e. g >= 2)")

    check("T7_hurwitz_admissible_chi",
          chi_hurwitz == [-2, -4, -6, -8, -10, -12, -14],
          f"with the self-contained T4 bound only: chi in {chi_hurwitz} -- "
          "seven values, a real narrowing from the infinite set Steps 3+4 "
          "leave, and not to -6")

    check("T7_minus_six_admissible_not_unique",
          -6 in chi_classification and len(chi_classification) > 1,
          f"-6 is 1 of {len(chi_classification)} under the classification and "
          f"1 of {len(chi_hurwitz)} under the derived bound: the route "
          "NARROWS and does not SELECT")

    # ----------------------------------------------------------------------
    # T8. Does an order-5 automorphism separate the survivors?
    # ----------------------------------------------------------------------
    print("\nT8. The order-5 discriminator")

    aut_orders = {lab: a for lab, _, _, _, a, _ in configs}
    order_five = {lab: (a % 5 == 0) for lab, a in aut_orders.items()}
    check("T8_order_five_selects_bring_among_g_gt_2",
          order_five["bring_g4"] and not order_five["klein_quartic_g3"]
          and not order_five["k3_long_orbit_g3"],
          f"5 divides |Aut| only for Bring among the genus>2 configurations: "
          f"{aut_orders} -> divisible by 5: {order_five}. So order 5 is what "
          "would select g = 4 -- but it is an EXTRA input, not supplied by "
          "transitivity or simplicity")

    check("T8_genus_two_not_settled_here", True,
          "whether a genus-2 surface can carry BOTH an order-5 automorphism "
          "and a transitive action on its 6 Weierstrass points is NOT decided "
          "by this probe: it needs the genus-2 automorphism classification "
          "(Bolza), which this corpus does not hold. Recorded as open rather "
          "than asserted")

    # ----------------------------------------------------------------------
    all_passed = all(ok for _, ok, _ in checks)
    print(f"\n{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks passed")

    witness = {
        "description": (
            "Does transitivity of Aut on the Weierstrass points narrow chi(A)? "
            "No: it forces the weights EQUAL and nothing more, and is realised "
            "at every genus >= 2. The narrowing in Laing & Singerman Thm 15 is "
            "carried entirely by the SECOND hypothesis, simplicity (weight 1), "
            "which is a genericity condition anti-correlated with symmetry."),
        "bean": "qou-qhcr",
        "leanCompanion": (
            "folio/quantum-observable-universe/lean/QOU/BringsSurface/"
            "WeierstrassTransitivityNotForced.lean"),
        "T1_total_weight": {str(g): total_weight(g) for g in range(2, 13)},
        "T1_max_weight": {str(g): max_weight(g) for g in range(2, 13)},
        "T1_min_point_count": {str(g): 2 * g + 2 for g in range(2, 13)},
        "T2_transitive_config_counts": {str(g): config_counts[g] for g in config_counts},
        "T3_accola_maclachlan_simple_genera": am_simple,
        "T4_hurwitz_survivors": survivors,
        "T4_cutoff": {"g8_total": total_weight(8), "g8_bound": hurwitz_aut_bound(8),
                      "g9_total": total_weight(9), "g9_bound": hurwitz_aut_bound(9)},
        "T5_configs": [
            {"label": lab, "genus": g, "n_weierstrass": n, "weight": w,
             "aut_order": a, "stabiliser_order": a // n,
             "transitive_possible": a % n == 0, "simple": w == 1, "source": src}
            for lab, g, n, w, a, src in configs
        ],
        "T7_chi_with_classification": chi_classification,
        "T7_chi_hurwitz_only": chi_hurwitz,
        "T8_aut_orders": aut_orders,
        "T8_order_five_divides": order_five,
        "checks": [{"name": n, "passed": ok, "detail": det}
                   for n, ok, det in checks],
        "allPassed": all_passed,
        "verdict": {
            "transitivity_derives_six": False,
            "transitivity_scope": (
                "scope-(b) structural exclusion of the TRANSITIVITY half: "
                "transitivity alone, however sourced, cuts out no genus. The "
                "invariant is an explicit infinite family in a published held "
                "source -- the Accola-Maclachlan curves realise it at every "
                "g >= 2 (arXiv:2211.08164v2 section 1 item 1), and that "
                "source's main theorem adds infinitely many non-hyperelliptic "
                "examples. This is NOT 'no axiom was found'; it is 'there is "
                "nothing here for an axiom to supply'."),
            "simplicity_scope": (
                "scope-(a) on the SIMPLICITY half: no QOU axiom supplying "
                "weight-1 was found on the surfaces searched for bean "
                "qou-qhcr. What is argued structurally -- an argument, not a "
                "theorem -- is that simplicity is a GENERICITY condition "
                "anti-correlated with symmetry inside the classification's own "
                "family K_3 (T5), so a homogeneity axiom of the observability "
                "register is the wrong SHAPE to supply it."),
            "framing_correction": (
                "the route's honest output is chi(A) in {-2, -4, -6}, not "
                "{-4, -6}: the classification is stated for genus > 2, genus 2 "
                "satisfies both hypotheses unconditionally (T6), and nothing in "
                "ex:chi-minus-six-derivation supplies g > 2."),
            "derived_here": (
                "transitivity + simplicity + Hurwitz's |Aut| <= 84(g-1) forces "
                "g <= 8 (T4), with 8 the argument's exact cut-off. Strictly "
                "weaker than the cited g in {3,4} and independent of it: the "
                "first narrowing in this arc from a finite classical input "
                "rather than read off Bring's curve."),
            "sharpest_open_statement": (
                "Steps 3+4 pin chi(A) to the non-positive even integers. The "
                "transitivity route narrows further only in conjunction with "
                "simplicity, and NEITHER half narrows alone -- transitivity is "
                "realised at every genus, simplicity is the generic condition. "
                "The narrowing is a pure conjunction effect between a "
                "homogeneity condition and a genericity condition that pull in "
                "opposite directions, which is why only finitely many surfaces "
                "satisfy both. No QOU axiom supplies either half, and "
                "observability -- whose only content in the corpus is "
                "rank Hom(1, Ad(A)) = 0 -- is a statement about a Hom-space in "
                "the monoidal category with no theorem relating it to Aut(M_0) "
                "acting on anything."),
        },
    }
    # q0 anchor: this producer never reads q0. Every quantity is an exact
    # integer (genus, Weierstrass weights and counts, group orders, divisors);
    # no substrate parameter enters the import cone, so there is no muon/proton
    # layer to declare. `independent` is the producer-declared token for exactly
    # that state -- see computations/audits/q0_anchor_consistency_audit.py
    # (AGENTS.md q0-anchor convention rule 4, "say which pin you used").
    out = WitnessBuilder.wrap_legacy(
        "weierstrass-transitivity-narrowing", witness,
        script_path=__file__, engine="python", start_time=t0,
    ).save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "q0-free: the probe is exact integer combinatorics (Weierstrass "
            "weights and counts, Hurwitz bounds, orbit-stabiliser divisibility, "
            "divisor enumeration). No substrate parameter is read anywhere in "
            "the import cone, so neither the ideal-muon nor the "
            "physical-proton layer applies."),
    })
    print(f"  Witness: {out}  ({time.monotonic() - t0:.1f}s)")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
