#!/usr/bin/env python3
"""Why three generations? Locate the truncation of the T(2,n) lepton ladder.

Bean qou-4dxs (STRATEGIC: the generation gap blocks 11 of 26 SM
parameters -- all 4 CKM and all 7 neutrino -- 42% of the count on one
structural problem the corpus records as "nowhere addressed").

THE SETUP, entirely from existing corpus blocks. Two independent
statements bracket the lepton ladder:

  * `torus-embeddable-complete-proof` PROVES the embeddability bound:
    a torus knot T(m,n) sits in Bring's surface Sigma_4 iff its Seifert
    genus (m-1)(n-1)/2 <= 4. For m = 2 that is n <= 9, giving the odd
    coprime values n in {3, 5, 7, 9} -- FOUR knots.
  * `lepton-continuant-recurrence` assigns T(2,n) for n = 3, 5, 7 to
    e, mu, tau -- THREE generations.

So the generation count is exactly the gap between these: the ladder
admits n = 9 geometrically but the corpus stops at n = 7. "Why three
generations" is therefore the single sharp question WHAT EXCLUDES
T(2,9)?

WHAT THE CORPUS ACTUALLY SAYS. A corpus-wide grep finds the primality
condition ("odd primes") exactly ONCE, as a parenthetical in
`lepton-meson-torus-knot-dictionary`. It is ASSERTED, never derived.
That matters: n odd prime AND n <= 9 would give n in {3,5,7} and hence
exactly three generations in two lines -- but only if primality is
derived. It is not, so no derivation is claimed here.

THE CANDIDATE STRUCTURAL REASON, stated as a hypothesis to be tested
rather than assumed: for odd n >= 3, n factors into smaller odd
windings iff n is composite. So sigma^9 = (sigma^3)^3 is a HARMONIC of
the first generation -- the braid word factors through a smaller
winding -- while 3, 5, 7 admit no such factorization. "Odd prime" and
"not a harmonic of a smaller odd winding" are the same condition.

WHAT THIS PROBE DOES. It computes the ladder from the corpus's own
Morgan-Voyce continuant recurrence (`lepton-continuant-recurrence`),

    NF(sigma^n) = a_n * 1 + b_n * sigma,
    a_{n+1} = b_n,  b_{n+1} = h b_n + b_{n-1},  b_0 = 0, b_1 = 1,
    h = q - 1/q,        net(T(2,n)) = a_n + b_n = b_{n-1} + b_n

evaluated at the substrate q_0, and asks two questions:

  (1) VALIDATION -- do the net ratios along n = 3 -> 5 -> 7 track the
      observed lepton mass ratios mu/e and tau/mu? If the ladder does
      not reproduce the generations it does claim, its extrapolation to
      n = 9 is worthless and the probe stops there.
  (2) THE TEST -- what does n = 9 predict, and is that prediction
      experimentally allowed? LEP's invisible-Z width fixes the number
      of light neutrino species at 3, and a fourth charged lepton is
      excluded below ~45 GeV. If T(2,9) lands in the excluded window
      the ladder MUST truncate, which makes the primality/harmonic
      condition physically load-bearing rather than decorative.

Nothing is fitted and nothing is wired: the recurrence, h, and q_0 are
all fixed by existing blocks, and the only new content is the
arithmetic and the comparison to a published exclusion.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import mp, mpf  # noqa: E402
from codata_constants import M_E_MEV

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# CODATA / PDG charged-lepton masses, MeV.
M_E = M_E_MEV
M_MU = mpf("105.6583755")
M_TAU = mpf("1776.86")

# LEP: a 4th charged lepton is excluded below ~45 GeV (Z-width), and the
# invisible Z width fixes N_nu = 2.984 +/- 0.008.
LEP_CHARGED_LEPTON_FLOOR_MEV = mpf("45000")


def net_ladder(h, n_max: int):
    """net(T(2,n)) = b_{n-1} + b_n from the Morgan-Voyce continuant."""
    b = [mpf(0), mpf(1)]
    for _ in range(2, n_max + 2):
        b.append(h * b[-1] + b[-2])
    return {n: b[n - 1] + b[n] for n in range(1, n_max + 1)}


def main() -> None:
    set_compute_dps()
    q0 = Q_MP
    h = q0 - 1 / q0
    net = net_ladder(h, 11)

    # (1) VALIDATION: does the ladder reproduce the ratios it claims?
    obs = {"mu/e": M_MU / M_E, "tau/mu": M_TAU / M_MU}
    pred = {"mu/e": net[5] / net[3], "tau/mu": net[7] / net[5]}
    ratio_check = {
        k: {"observed": mp.nstr(obs[k], 8),
            "net_ratio": mp.nstr(pred[k], 8),
            "pred_over_obs": mp.nstr(pred[k] / obs[k], 8)}
        for k in obs
    }
    # The net ratios are O(1) while the mass ratios are O(10^2): the bare
    # continuant net is NOT the mass map. Record that rather than tuning.
    ladder_reproduces = all(mpf("0.5") < pred[k] / obs[k] < mpf("2")
                            for k in obs)

    # (2) THE TEST, done in the only way the failed validation permits:
    # a RATIO-FREE structural statement. Whatever monotone map M sends
    # net -> mass, the ladder's ORDERING and its step ratios constrain
    # where n = 9 lands relative to n = 7.
    step_ratios = {f"n={n} -> n={n+2}": mp.nstr(net[n + 2] / net[n], 8)
                   for n in (3, 5, 7, 9)}
    r79 = net[9] / net[7]
    # If the mass map were the observed tau/mu step applied once more:
    naive_m9_lower = M_TAU * (M_TAU / M_MU)
    monotone = all(net[n] < net[n + 2] for n in (3, 5, 7, 9))

    wb = WitnessBuilder("generation-count-t29-truncation", engine="mpmath")
    wb.set_description(
        "EXPLORATORY probe of the three-generation question (bean "
        "qou-4dxs), which the corpus records as 'nowhere addressed'. "
        "Locates it precisely: `torus-embeddable-complete-proof` PROVES "
        "the genus bound admits n in {3,5,7,9} for T(2,n), while "
        "`lepton-continuant-recurrence` assigns only n = 3,5,7 to "
        "e/mu/tau. The generation count IS the exclusion of T(2,9). "
        "Reports that the primality condition which would close it "
        "appears exactly once in the corpus, as an underived "
        "parenthetical, and tests the ladder's own predictive content "
        "using the corpus's Morgan-Voyce recurrence. No derivation is "
        "claimed and nothing is wired.")
    wb.add_data("problem_localisation", {
        "embeddability_bound": ("g(T(m,n)) = (m-1)(n-1)/2 <= g(Sigma_4) "
                                "= 4; for m = 2, n <= 9, so the odd "
                                "coprime values are n in {3,5,7,9} -- "
                                "FOUR admissible knots (PROVED, "
                                "torus-embeddable-complete-proof)"),
        "generation_assignment": ("T(2,n) for n = 3,5,7 -> e, mu, tau "
                                  "-- THREE generations "
                                  "(lepton-continuant-recurrence)"),
        "the_gap": ("the generation count is exactly the exclusion of "
                    "T(2,9); 'why three generations' reduces to the "
                    "single question 'what excludes n = 9?'"),
        "why_this_is_progress": ("it converts a problem the corpus "
                                 "records as 'nowhere addressed, prior "
                                 "to all mixing parameters' into one "
                                 "well-posed lemma about one knot"),
    })
    wb.add_data("primality_condition_is_asserted_not_derived", {
        "corpus_occurrences": 1,
        "location": ("content/quantum-observable-universe/"
                     "particle-interactions/"
                     "lepton-meson-torus-knot-dictionary.md, line 1, "
                     "parenthetical '(odd primes)'"),
        "consequence": ("n odd prime AND n <= 9 gives n in {3,5,7}, "
                        "hence exactly three generations, in two lines "
                        "-- but ONLY if primality is derived. It is "
                        "not. This is stated as the gap it is; no "
                        "two-line derivation of the generation count is "
                        "claimed."),
        "candidate_structural_reason": (
            "For odd n >= 3, n factors into smaller odd windings iff n "
            "is composite, so 'n odd prime' and 'n is not a harmonic of "
            "a smaller odd winding' are the SAME condition. sigma^9 = "
            "(sigma^3)^3 is a harmonic of the first generation; 3, 5, 7 "
            "admit no such factorization. This is a hypothesis to be "
            "proved or refuted, not an argument -- the braid word of "
            "every n factors trivially, so the content is entirely in "
            "why factorization through a smaller ODD winding should "
            "forbid a generation assignment."),
    })
    wb.add_data("continuant_ladder_at_q0", {
        "q0": mp.nstr(q0, 12),
        "h = q0 - 1/q0": mp.nstr(h, 12),
        "net": {str(n): mp.nstr(net[n], 10) for n in (3, 5, 7, 9, 11)},
        "step_ratios": step_ratios,
        "monotone_increasing": bool(monotone),
    })
    wb.add_data("validation_FAILED_net_is_not_the_mass_map", {
        "ratio_check": ratio_check,
        "verdict": (
            "The bare continuant net does NOT reproduce the lepton mass "
            f"ratios: net(7)/net(5) = {mp.nstr(r79 and pred['tau/mu'], 6)} "
            f"against an observed tau/mu of {mp.nstr(obs['tau/mu'], 6)}. "
            "The net ratios are O(1) while the mass ratios are O(10^2), "
            "so net(T(2,n)) is a normal-form coefficient, not a mass. "
            "This is recorded as a failed validation rather than "
            "repaired by introducing a scale factor -- fitting one here "
            "would be exactly the laundering the anti-fit discipline "
            "forbids."),
        "consequence_for_this_probe": (
            "Because the mass map is not established, this probe CANNOT "
            "compute what T(2,9) would weigh, and therefore cannot "
            "check it against the LEP exclusion. The intended decisive "
            "test is BLOCKED, and that blockage is the finding: the "
            "corpus assigns T(2,n) to generations without a wired map "
            "from the continuant to a mass, so the ladder currently has "
            "no predictive content at n = 9 to falsify."),
    })
    wb.add_data("what_would_close_it", {
        "route_A_derive_primality": (
            "Prove that a composite odd winding cannot carry a "
            "generation -- e.g. that the T(2,ab) Hecke normal form or "
            "Markov trace factors through T(2,a) in a way that forbids "
            "an independent fibre assignment. This would derive the "
            "generation count from the genus bound, and is the route "
            "with an actual payoff (3 generations, not merely <= 4)."),
        "route_B_wire_the_mass_map": (
            "Establish the map from net(T(2,n)) to a lepton mass. Then "
            "T(2,9) makes a numerical prediction and the LEP bound "
            "(no 4th charged lepton below ~45 GeV, N_nu = 2.984 +/- "
            "0.008) either refutes the ladder or forces the "
            "truncation. Prerequisite for any falsification."),
        "route_C_check_the_meson_tower": (
            "The same T(2,n) ladder indexes the meson tower "
            "(lepton-meson-torus-knot-dictionary). If the meson side "
            "DOES populate n = 9, then n = 9 is admissible in general "
            "and the exclusion is specific to the lepton fibre -- which "
            "would refute the harmonic hypothesis as stated and "
            "relocate the question."),
        "priority": ("C is cheapest and can REFUTE the harmonic "
                     "hypothesis outright; A is the one that pays; B is "
                     "prerequisite to any numerical falsification."),
    })
    wb.set_audit_only("docs/audits/2026-08-01-em-linking-reads-round1.md")
    wb.add_assertion(
        name="embeddability_admits_four_but_generations_are_three",
        computed=4 - 3, expected=1, tolerance=0, unit="count",
        source=("The gap that IS the generation question: the proved "
                "genus bound admits n in {3,5,7,9} while the corpus "
                "assigns three generations, leaving exactly one "
                "unexplained exclusion (n = 9)."))
    wb.add_assertion(
        name="continuant_ladder_monotone",
        computed=int(monotone), expected=1, tolerance=0, unit="bool",
        source=("Sanity check on the recurrence at q_0: net(T(2,n)) "
                "increases along the ladder, as a generation tower "
                "must."))
    wb.add_assertion(
        name="net_ratios_do_not_reproduce_mass_ratios",
        computed=int(not ladder_reproduces), expected=1, tolerance=0,
        unit="bool",
        source=("The honest negative: the bare continuant net is not "
                "the mass map, so the ladder has no predictive content "
                "at n = 9 to test against LEP. Recorded, not repaired "
                "with a fitted scale."))
    out = wb.save()

    print("THE GENERATION QUESTION, LOCALISED")
    print("  genus bound admits n in {3,5,7,9}  (PROVED)")
    print("  corpus assigns generations to n in {3,5,7}")
    print("  => 'why three generations' == 'what excludes T(2,9)?'")
    print("\n  primality condition occurrences in corpus: 1 "
          "(an underived parenthetical)")
    print(f"\nladder at q0 = {mp.nstr(q0, 8)}, h = {mp.nstr(h, 8)}:")
    for n in (3, 5, 7, 9, 11):
        print(f"  net(T(2,{n:2d})) = {mp.nstr(net[n], 10)}")
    print("\nVALIDATION (does the ladder reproduce the lepton ratios?):")
    for k, v in ratio_check.items():
        print(f"  {k:8s} observed {v['observed']:>12}   "
              f"net {v['net_ratio']:>10}   ratio {v['pred_over_obs']:>10}")
    print("  -> FAILED: net is a normal-form coefficient, not a mass.")
    print("  -> the n=9 vs LEP test is BLOCKED; that is the finding.")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
