#!/usr/bin/env python3
"""Every load-bearing number the `qou-cds1` terminus rests on, recomputed from
one independent route — plus the standing/withdrawn ledger, as assertions.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md
# Ref: computations/qbeta/qbeta_d_frame_terminus_probe.py            (Step 14)
# Ref: computations/qbeta/qbeta_block_bar_defect_conjugation_probe.py (entry 15)
# Ref: computations/qbeta/qbeta_n1_constant_two_anchor_filter_probe.py (entry 16)

WHY THIS EXISTS. The `qou-cds1` bean is ~4760 lines across 16 numbered entries
and 14 numbered steps, and it carries FOUR withdrawals — Step 10's "the block is
a ruling" (withdrawn by Step 13), entry 13 (withdrawn by entry 14), a Step-13
correction that did not propagate (fixed in Step 14b), and entry 12's framing of
the `K` blocker (corrected by entry 16). A reader arriving cold cannot tell what
still stands, and the arc's own history is of recorded figures going stale.

So this is deliberately NOT a summary document. It recomputes each standing
number from a THIRD independent route — a 3x3 Markov solve over the H_3 block
characters, built here rather than imported from the probes it checks — and
asserts it. If an anchor moves, CODATA updates, or a producer changes, this
fails instead of quietly disagreeing with prose.

WHAT IS CHECKED, and against what.

  The Ocneanu weights, symbolically:
      y_(3)(z_D)   = (q^4+1)/(q^2+1)^2        Step 14's `g`
      y_(1^3)(z_D) = 0                         the two-row cap at z_D
      y_(3)(q)     = 1                         the augmentation root
      y_(1^3)(q)   = 0                         the cap's other root
      admissible set = exactly {q, z_D}        qou-06wh, proved complete
      chi^(2,1)(Delta) = 0  identically        Step 9

  The terminus arithmetic (proton pin):
      g(q0)        = 0.505404226504
      data wants   = 0.8891258104              short by x1.75923699046
      z_required   = 0.998500302563            Step 10, re-solved here

  Entry 15, per-block bar-defect under the two bar conditions:
      bar-even (C): z-DEPENDENT, sum 0 for every such z
      full-bar (D): z-FREE, sum h^2 for every such z

WHAT IS NOT CHECKED, and why. Step 14's `chi` leg quotes a required element
ratio `a_(2,1)/a_(3) = 1.5516573513` for a HYPOTHETICAL decay element. Its
definition is not fixed by anything this probe can rebuild without guessing at
it, so it is deliberately omitted rather than reproduced from a number. Step
14's `K` (the trace -> MeV scale) is likewise an enumeration result, not a
closed form, and cannot be recomputed here.

🛑 `K` IS OVERLOADED IN THIS ARC — see entry 16b. Step 14's `K` is the
trace -> MeV scale OUTSIDE the Hecke trace (verdict NEGATIVE, enumerated).
Entries 10c/12/16's `K(delta)` is the N=1 factor's multiplicative constant with
`K(0) = 1`, numerically ~1 (verdict FREE, then filtered but undetermined).
Neither verdict transfers.

SCOPE. This asserts what the arc already established; it derives nothing new and
proposes no `c_k`. Its value is that a future disagreement between the prose and
the mathematics surfaces as a FAILING ASSERTION rather than as a stale sentence.
L2 unchanged at 1279 ppb.

🛑 AND IT HAS ALREADY EARNED THAT, ON ITSELF. Written against the arc at Step 14,
this probe sat in review while Steps 15-28 landed on `main` (2026-08-31) and moved
the open question materially — Step 26 EXCLUDES the phase at 3e11 sigma rather
than leaving it unfound. All 13 assertions still pass against that advanced
corpus, because they are about `y_lambda`, the two-row cap, `chi^(2,1)(Delta)`
and the two bar conditions, none of which those steps touch. The prose around
them did go stale, and is restated from `main` in the `open` data block rather
than left at Step 14. That is the intended failure mode working: the numbers held
and the narrative had to be re-fetched.

NO FLOAT64: sympy exact symbolic; mpmath mpf at 50 dps for the reported
numerics only.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    BASIS, L, LEFT, N, ONE, R, basis_vec, h, length, net, q, reg_char,
)

set_compute_dps(50)

Z = sp.Symbol("z")
ZB = sp.Symbol("zbar")
Z_D = q ** 3 / (q ** 2 + 1)
LABELS = ["(3)", "(2,1)", "(1,1,1)"]
TERMINUS_WITNESS = HERE / "qbeta-d-frame-terminus.witness.json"

# Step 14's decay-channel demand, READ FROM ITS WITNESS at full precision, not
# quoted from the prose. The bean rounds it to 0.8891258104 (10 sig figs), and
# that rounding alone moves the z_required root by ~4e-11 — enough to fail an
# 11-digit check against Step 10 and look like a disagreement. Reading the
# source also makes this probe track the anchor instead of a transcription.
def _g_required():
    import json
    return mp.mpf(json.loads(TERMINUS_WITNESS.read_text())["data"]["g_required"])


def main() -> int:
    w = WitnessBuilder("qbeta-cds1-terminus-status", engine="sympy+mpmath")
    w.set_description(
        "Every load-bearing number of the qou-cds1 terminus recomputed from an "
        "independent 3x3 Markov solve, plus the standing/withdrawn ledger as "
        "assertions, so that prose drifting from the mathematics fails a check "
        "rather than going quietly stale."
    )
    ok = []

    def check(name, passed, note=""):
        ok.append(bool(passed))
        w.add_assertion(name, computed="1" if passed else "0",
                        expected="1", tolerance="0")
        print(f"  [{'PASS' if passed else 'FAIL'}] {name} {note}")

    # ---- characters and weights, built here, not imported -------------------
    def chi3(v):
        return sp.simplify(sum(v[i] * q ** length(BASIS[i]) for i in range(N)))

    def chi111(v):
        return sp.simplify(sum(v[i] * (-1 / q) ** length(BASIS[i]) for i in range(N)))

    def chi21(v):
        return sp.simplify((reg_char(v) - chi3(v) - chi111(v)) / 2)

    CHI = [chi3, chi21, chi111]

    # TR[5] = z(hz+1), the sigma_0 sigma_1 sigma_0 Markov weight — NOT z^3.
    # docs/audits/2026-05-19-trm5-markov-bug.md; three live files carried the
    # wrong form as recently as this arc.
    TR = [sp.Integer(1), Z, Z, Z ** 2, Z ** 2, Z * (h * Z + 1)]
    yv = sp.symbols("y0 y1 y2")
    solY = sp.solve([sp.Eq(sum(yv[k] * CHI[k](basis_vec(i)) for k in range(3)),
                           TR[i]) for i in (0, 1, 3)], yv, dict=True)
    check("the_3x3_Markov_solve_is_unique", len(solY) == 1)
    Y = [sp.simplify(sp.factor(solY[0][yv[k]])) for k in range(3)]
    check("weights_reproduce_the_trace_on_the_REMAINING_basis_elements_CONTROL",
          all(sp.simplify(sum(Y[k] * CHI[k](basis_vec(i)) for k in range(3))
                          - TR[i]) == 0 for i in (2, 4, 5)))

    # ---- STANDS: the weights at both admissible roots -----------------------
    g_closed = (q ** 4 + 1) / (q ** 2 + 1) ** 2
    check("g_equals_y3_at_zD_equals_q4plus1_over_q2plus1_squared",
          sp.simplify(Y[0].subs(Z, Z_D) - g_closed) == 0,
          "(Step 14's g, symbolic difference exactly 0)")
    check("y_1cubed_vanishes_at_zD", sp.simplify(Y[2].subs(Z, Z_D)) == 0)
    check("y_3_equals_ONE_at_the_augmentation_root_z_eq_q",
          sp.simplify(Y[0].subs(Z, q) - 1) == 0)
    check("y_1cubed_vanishes_at_z_eq_q", sp.simplify(Y[2].subs(Z, q)) == 0)

    roots = sp.solve(sp.numer(sp.together(Y[2])), Z)
    check("the_admissible_set_is_EXACTLY_q_and_zD",
          len(roots) == 2
          and any(sp.simplify(r - q) == 0 for r in roots)
          and any(sp.simplify(r - Z_D) == 0 for r in roots),
          "(qou-06wh's completeness, re-derived)")

    # ---- STANDS: Step 9, the phase is blind to the 2-dim block --------------
    proton = sp.simplify(L[0] * (L[1] - (h / 2) * ONE) * basis_vec(0))
    neutron = sp.simplify((L[0] - (h / 2) * ONE) * (L[1] - h * ONE) * basis_vec(0))
    delta = sp.expand(neutron - proton)
    check("chi_2_1_of_Delta_vanishes_IDENTICALLY",
          sp.simplify(chi21(delta)) == 0, "(Step 9)")

    # ---- STANDS: the terminus arithmetic ------------------------------------
    q0 = Q_MP

    def ev(e):
        return sp.lambdify(q, e, "mpmath")(q0)

    g0 = ev(g_closed)
    g_want = _g_required()
    ratio = g_want / g0
    check("g_at_q0_is_0_505404226504", abs(g0 - mp.mpf("0.505404226504")) < mp.mpf("1e-11"),
          f"({mp.nstr(g0, 12)})")
    check("the_decay_channel_is_short_by_1_75923699046",
          abs(ratio - mp.mpf("1.75923699046")) < mp.mpf("1e-10"),
          f"({mp.nstr(ratio, 12)} — a DOF that does not exist, not a failed search)")

    # Step 10's z_required, re-solved rather than quoted. Lambdify in BOTH
    # variables and pass the mpf q0 straight through: substituting q0 as a
    # sympy Float first costs ~4e-11 on the root, which is a precision artifact
    # of the substitution and not a disagreement with Step 10.
    gz = sp.lambdify((q, Z), Y[0] - Y[2], "mpmath")
    z_req = mp.findroot(lambda t: gz(q0, t) - g_want, mp.mpf("0.9985"))
    check("z_required_re_solves_to_0_998500302563",
          abs(z_req - mp.mpf("0.998500302563")) < mp.mpf("1e-11"),
          f"({mp.nstr(z_req, 12)} — Step 10, and EXCLUDED by the derived cap)")

    # ---- STANDS: entry 15, the two bar conditions differ in kind ------------
    comms = [LEFT[i] * basis_vec(j) - LEFT[j] * basis_vec(i)
             for i in range(N) for j in range(N)]
    cb = sp.Matrix.hstack(*comms).columnspace()
    zc = [sp.Matrix.vstack(sp.simplify(L[0] * basis_vec(i) - R[0] * basis_vec(i)),
                           sp.simplify(L[1] * basis_vec(i) - R[1] * basis_vec(i)))
          for i in range(N)]
    centre = sp.Matrix.hstack(*zc).nullspace()
    P = sp.Matrix.hstack(*(list(centre) + list(cb)))
    coords = sp.simplify(P.solve(delta))
    dZv = sp.simplify(sum((coords[i] * centre[i] for i in range(3)), sp.zeros(N, 1)))
    dCv = sp.simplify(delta - dZv)
    chi_d = [sp.simplify(sp.factor(f(delta))) for f in CHI]
    av = sp.symbols("a0 a1 a2")
    sol = sp.solve([sp.Eq(sum(av[k] * CHI[k](v) for k in range(3)), net(v))
                    for v in centre], av, dict=True)
    A = [sp.simplify(sp.factor(sol[0][av[k]])) for k in range(3)]
    floor = sp.factor(sp.simplify(net(dCv)))

    def BAR(e):
        return sp.simplify(sp.together(sp.sympify(e).subs({q: 1 / q, Z: ZB},
                                                          simultaneous=True)))

    B = [sp.simplify((A[k] - Y[k]) * chi_d[k]) for k in range(3)]
    d = [sp.simplify(sp.factor(BAR(B[k]) + B[k])) for k in range(3)]
    dfl = sp.simplify(BAR(floor) + floor)
    dC_ = [sp.simplify(x.subs({ZB: Z})) for x in d]
    dD_ = [sp.simplify(sp.factor(x.subs({ZB: Z - h}))) for x in d]
    check("bar_even_C_block_defects_are_z_dependent_and_sum_to_ZERO_for_every_such_z",
          (Z in dC_[0].free_symbols)
          and sp.simplify(sum(dC_) + dfl.subs({ZB: Z})) == 0,
          "(entry 15: C's bar-oddness is a CANCELLATION between blocks)")
    check("full_bar_D_block_defects_are_z_FREE_and_sum_to_h_squared_for_every_such_z",
          all(Z not in x.free_symbols for x in dD_)
          and sp.simplify(sum(dD_) + dfl.subs({ZB: Z - h}) - h ** 2) == 0,
          "(entry 15: no z in the full-bar class changes the D defect)")

    # ---- the ledger, recorded as data ---------------------------------------
    w.add_data("stands", [
        {"claim": "g = y_(3)(z_D) = (q^4+1)/(q^2+1)^2", "source": "Step 14",
         "verified_here": True, "route": "independent 3x3 Markov solve"},
        {"claim": "admissible set is exactly {q, z_D}", "source": "qou-06wh",
         "verified_here": True, "route": "roots of numer(y_(1^3))"},
        {"claim": "chi^(2,1)(Delta) = 0 identically", "source": "Step 9",
         "verified_here": True},
        {"claim": "decay channel short by x1.75923699046", "source": "Step 14",
         "verified_here": True},
        {"claim": "z_required = 0.998500302563, and it is EXCLUDED",
         "source": "Step 10 + Step 13", "verified_here": True,
         "route": "re-solved, not quoted"},
        {"claim": "the two bar conditions differ in KIND (C z-dependent and "
                  "cancelling; D z-free and summing to h^2)",
         "source": "entry 15", "verified_here": True},
        {"claim": "the two-row cap is DERIVED (2-dim mass fibre => Lambda^3_q V = 0)",
         "source": "Step 13, QOU/BraidsAndKnots/FibreDimensionForcesTL.lean "
                   "(NOTE the path: BraidsAndKnots, not QBeta)",
         "verified_here": False,
         "why_not": "a Lean result; this probe is Python and cannot check it",
         "verified_separately": {
             "when": "2026-08-31", "how": "lean-direct + #print axioms",
             "result": "exit 0; all five theorems depend on "
                       "[propext, Classical.choice, Quot.sound] only — NO sorryAx. "
                       "Zero sorry / axiom / native_decide in the file.",
             "declarations": ["qNumber_shift_identity",
                              "ocneanu_param_eq_of_fibre_qdim",
                              "ocneanu_param_of_two_dim_fibre",
                              "threeRow_eq_zero_of_jones_ocneanu",
                              "twoDimFibre_pins_h3_weights"],
             "caveat": "verified by an agent this session, NOT by this probe — "
                       "re-verify with lean-direct if the file changes",
         }},
    ])
    w.add_data("withdrawn", [
        {"claim": "the (1^3) block cap is a RULING", "withdrawn_by": "Step 13",
         "replacement": "the cap is DERIVED"},
        {"claim": "K(delta) is fixed by the entry-2 bar-midpoint rule",
         "withdrawn_by": "entry 14",
         "replacement": "the rule FAILS the N=2 slot by 25.9 %; K free again"},
        {"claim": "the K blocker is the 59694 ppb gap BETWEEN the candidates",
         "withdrawn_by": "entry 16",
         "replacement": "both candidates miss the required VALUE by MORE than "
                        "that gap (281380 / 221686 ppb)"},
    ])
    # 🛑 SUPERSEDED IN PART. This probe was written against the arc at Step 14.
    # Steps 15-28 landed on `main` on 2026-08-31 while it was in review and moved
    # the open question materially. Every ASSERTION above survives untouched —
    # they are about y_lambda, the two-row cap, chi^(2,1)(Delta) and the two bar
    # conditions, none of which those steps touch, and all 13 still pass against
    # the advanced corpus. What changed is the STATUS below, so it is restated
    # from `main` rather than left at Step 14.
    w.add_data("open", [
        {"item": "a derivation of the ladder phase alpha",
         "status_at_step_14": "the z direction closed from three independent "
                              "sides (trace weight, bar parity, anchors); the "
                              "cos form closed (Steps 7-8, entry 15); the "
                              "amplitude route fenced (qou-i2ir C16/C17/C18 + a "
                              "structural one-scale/two-target refutation).",
         "SUPERSEDED_BY": "Steps 15-28 (2026-08-31). The phase is no longer "
                          "merely unfound: Step 26 EXCLUDES it at 3e11 sigma, "
                          "having shown symbolically in q that the discriminant "
                          "curves are genus 0 (short) and genus 8 (long) — "
                          "NEVER genus 1, so there is no elliptic source and no "
                          "tower of them. Step 17 adds that the cosine is "
                          "UNFALSIFIABLE (phase yes, cosine no) and that the "
                          "only surviving justification would be a KZ/"
                          "Kohno-Drinfeld holonomy, which nothing supplies. "
                          "Step 24 closes both eigenphase readings: the Hecke "
                          "tower repeats the H_3 spectrum and cannot add to it.",
         "my_earlier_wording_was_wrong": "'no route is known to be open' "
                                         "describes a search that has not "
                                         "found one. Step 26 is an EXCLUSION. "
                                         "Different epistemic state; do not "
                                         "quote the weaker form."},
        {"item": "selecting the product generator rho in c_{k+1} = rho*c_k",
         "note": "PR #6282: the place IS named (QBetaSingleHabiroGenerator, "
                 "open with no instance) and the parity IS derived "
                 "(bar-INVARIANT, not bar-odd). What is missing is a SELECTOR. "
                 "That PR corrected two of its own three proposed gates — "
                 "parity is a class FILTER admitting the entire symmetric "
                 "q-integer family at once, and the Hankel condition "
                 "c_2*c_4 = c_3^2 is VACUOUS for rank-1 candidates. The "
                 "survivors TEST a candidate once you have one; they do not "
                 "PRODUCE one. The gap is a source, not a test.",
         "distinct_from": "the N=1 slot, which entries 10-10d DO answer "
                          "(M = cos(a_D - h^2/4)*cos(h^2/4), Lean-proved). "
                          "Different slot; do not read one as the other."},
        {"item": "K(delta)", "note": "free function; filtered but not determined"},
    ])
    w.add_data("corroborates_a_sibling_result", {
        "sibling": "Step 17 — the only surviving justification for the cosine "
                   "is a KZ/Kohno-Drinfeld holonomy, and nothing supplies one.",
        "this_arc_measured_the_same_thing_from_the_other_side": "entry 15 "
            "(merged, on main): bar DOES act as Kohno-Drinfeld partition "
            "conjugation on the block CHARACTERS (bar chi^(3) = chi^(1^3), "
            "exact, convention-free) but NOT on the Markov weights — every "
            "residual carries the single factor (z + zbar), so the weights are "
            "conjugation-equivariant iff z is bar-ODD, which neither convention "
            "is. Independent evidence for Step 17's claim.",
        "note": "both landed 2026-08-31, so neither cites the other. Recorded "
                "here so the connection is not lost.",
    })
    w.add_data("symbol_collision", {
        "symbol": "K",
        "step14": "trace -> MeV scale, outside the Hecke trace; verdict NEGATIVE",
        "entries_10c_12_16": "N=1 factor's multiplicative constant, K(0)=1, ~1; "
                             "verdict FREE then filtered-but-undetermined",
        "note": "neither verdict transfers; see entry 16b",
    })
    w.add_data("q0_anchor", {"pin": "physical_proton",
                             "registered_in": "computations/q0_anchor_manifest.json"})
    w.add_data("scope", {"tier": "scope-(a)", "derives_nothing_new": True,
                         "c_k_produced": False, "q_beta_ppb": 1279})

    passed = sum(ok)
    print(f"\n  {passed}/{len(ok)} checks passed")
    w.save()
    return 0 if passed == len(ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
