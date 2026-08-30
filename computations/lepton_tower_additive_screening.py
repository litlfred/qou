#!/usr/bin/env python3
"""Bean qou-htk4: the ADDITIVE bridge class is log-convex, hence excluded --
the last direction the multiplicative bend screen left open.

WHERE THIS SITS. `lepton_tower_bend_screening.py` screened the class

    m_w = C * g^w * f(w)^p

and said explicitly that an ADDITIVE interface term is outside it and not
screened at all. That was the last live shape on this bean. This script is
the numerical twin of the Lean that closes it
(`lepton_tower_log_convexity.lean`).

THE CLAIM. An additive bridge means the tower is a SUM OF GEOMETRIC MODES
-- a base term plus an interface term:

    x(w) = c g^w + d h^w,     c, d >= 0,  g, h > 0.

Such a tower is LOG-CONVEX. The Lagrange (sqrt-free Cauchy-Schwarz) identity

    x(w) x(w+4) - x(w+2)^2  =  c d g^w h^w (g^2 - h^2)^2  >=  0

gives bend = x(w+2)^2 / (x(w) x(w+4)) <= 1. The observed lepton bend is
m_mu^2/(m_e m_tau) = 12.295 -- log-CONCAVE, bending the other way. So no
such tower reproduces the lepton spectrum, for ANY coefficients and ANY
rates.

WHY THIS IS SHARPER THAN THE MULTIPLICATIVE SCREEN. That one ruled
candidates out by how large an exponent they would need (p = 64.9 for the
Markov trace, 8.72 at best) -- a judgement at the margin, and labelled as
one. This is a strict inequality with no free parameter left: bend <= 1
versus a measured 12.295.

WHAT THE PERFECT SQUARE ALSO SAYS. The deficit vanishes only when g = h
(one mode) or a coefficient vanishes. So the bend touches 1 ONLY in the
degenerate single-mode limits and is strictly below it otherwise: a second
positive mode never helps. It is NOT monotone in the second coefficient --
measured here, the bend dips to an interior minimum (~0.967 at d ~ 1 for
the q / 1-over-q pair) and returns to 1 as d -> infinity, where the second
mode takes over and the tower is again single-mode. An earlier draft of
this script asserted monotone worsening; that was wrong and the assertion
caught it. The correct statement is the bound plus its equality cases.

THE ONE SURVIVING SHAPE. Sign-indefinite combinations escape -- a
DIFFERENCE of exponentials can have a node, exactly as in
`lepton_continuant_positivity`. That is now the only shape left standing
across all three exclusions (linear readout, multiplicative, additive),
always by the same node mechanism. Demonstrated explicitly below rather
than left implicit, so the next candidate gets checked for it first.

q_0 CONVENTION. Experimental/proton pin (`q_parameter.Q_MP`) per the
2026-08-07 owner directive. No ideal-layer cache is read.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402

from mpmath import mp, mpf  # noqa: E402

# Shared, unit-tested maths (see test_lepton_tower_bend.py).
from lepton_tower_core import (  # noqa: E402
    BEND_TOL as TOL,
    M_E, M_MU, M_TAU,
    observed_lepton_bend,
    two_mode,
    two_mode_bend,
)

W = 3   # lepton windings 3, 5, 7


def bend_of(c, d, g, h, w=W):
    return two_mode_bend(c, d, g, h, w)


def main() -> None:
    set_compute_dps()
    q = mp.mpf(Q_MP)

    obs_bend = observed_lepton_bend()

    # --- (1) the Lagrange identity, verified against direct evaluation ----
    # x(w) x(w+4) - x(w+2)^2 = c d g^w h^w (g^2 - h^2)^2
    cases = [
        ("q and 1/q modes", mpf(1), mpf(1), q, 1 / q),
        ("q^2 and 1 modes", mpf(1), mpf(2), q**2, mpf(1)),
        ("equal rates g=h", mpf(3), mpf("0.5"), q, q),
        ("one mode only (d=0)", mpf(1), mpf(0), q, mpf(2)),
        ("wide split", mpf("0.01"), mpf(100), mpf("1.9"), mpf("0.3")),
        ("Vol(4_1)-like base", mpf(1), mpf("0.25"), mpf("206.77"), q),
    ]
    identity_err = mpf(0)
    rows = {}
    for name, c, d, g, h in cases:
        lhs = (two_mode(c, d, g, h, W) * two_mode(c, d, g, h, W + 4)
               - two_mode(c, d, g, h, W + 2) ** 2)
        rhs = c * d * g**W * h**W * (g**2 - h**2) ** 2
        identity_err = max(identity_err, abs(lhs - rhs))
        bd = bend_of(c, d, g, h)
        rows[name] = {
            "c": str(c), "d": str(d), "g": str(g), "h": str(h),
            "bend": str(bd),
            "bend_le_one": bool(bd <= 1),
            "deficit": str(lhs),
        }

    # --- (2) a sweep: no positive two-mode tower ever exceeds bend 1 ------
    max_bend = mpf(0)
    argmax = None
    n_checked = 0
    grid = [mpf(x) / 10 for x in range(1, 41)]          # rates 0.1 .. 4.0
    coeffs = [mpf("0.01"), mpf("0.5"), mpf(1), mpf(7), mpf(500)]
    for g in grid:
        for h in grid:
            for c in coeffs:
                for d in coeffs:
                    bd = bend_of(c, d, g, h)
                    n_checked += 1
                    if bd is not None and bd > max_bend:
                        max_bend, argmax = bd, (str(c), str(d), str(g), str(h))
    sweep_respects_bound = bool(max_bend <= 1 + TOL)

    # --- (3) equality cases: bend touches 1 ONLY when single-mode --------
    # Turning on a second positive mode never helps, but the effect is NOT
    # monotone: the bend dips to an interior minimum and returns to 1 as the
    # second mode takes over. Measure the shape rather than assume it.
    interior = []
    for d in (mpf(0), mpf("0.01"), mpf("0.1"), mpf(1), mpf(10), mpf(1000)):
        bd = bend_of(mpf(1), d, q, 1 / q)
        interior.append({"d": str(d), "bend": str(bd)})
    bends_seq = [mpf(r["bend"]) for r in interior]
    never_above_one = all(b <= 1 + TOL for b in bends_seq)
    # strictly interior minimum: both endpoints at 1, something below between
    has_interior_min = bool(
        bends_seq[0] >= 1 - TOL
        and bends_seq[-1] > min(bends_seq)
        and min(bends_seq) < 1 - mpf("1e-6")
    )

    # --- (4) the one surviving shape: OPPOSITE SIGNS have a node ---------
    # d < 0 breaks the Cauchy-Schwarz hypothesis and the bend is unbounded.
    # For (c, g, h) = (1, q, 1/q) the node sits at d = -q^(2w) = -q^6, since
    # x(w) = q^w + d q^-w vanishes there. Approach it from above.
    d_node = -(q**6)
    signed = []
    for frac in ("-1.5", "-1.8", "-1.86", "-1.87"):
        d = mpf(frac)
        bd = bend_of(mpf(1), d, q, 1 / q)
        signed.append({
            "d": str(d),
            "x_at_winding_3": str(two_mode(mpf(1), d, q, 1 / q, W)),
            "bend": (str(bd) if bd is not None else None),
        })
    signed_can_exceed = any(
        s["bend"] is not None and mpf(s["bend"]) > obs_bend for s in signed
    )

    results = {
        "observed_lepton_bend": {
            "definition": "m_mu^2 / (m_e * m_tau)",
            "value": str(obs_bend),
            "log_concave": True,
        },
        "lagrange_identity": {
            "formula": "x(w)x(w+4) - x(w+2)^2 = c d g^w h^w (g^2-h^2)^2",
            "max_abs_err": str(identity_err),
            "verified": identity_err < mpf("1e-40"),
            "lean_twin": "QOU.Archimedean.twoMode_log_convex",
        },
        "cases": rows,
        "positive_sweep": {
            "n_towers_checked": n_checked,
            "max_bend_found": str(max_bend),
            "argmax_c_d_g_h": argmax,
            "bound_respected": sweep_respects_bound,
            "excess_over_one": str(max_bend - 1),
            "tolerance": str(TOL),
            "reading": (
                "every positive two-mode tower has bend <= 1; the observed "
                "12.295 is out of reach by a factor of 12, not by a margin"
            ),
        },
        "equality_cases_and_shape": {
            "series": interior,
            "never_above_one": never_above_one,
            "has_interior_minimum": has_interior_min,
            "reading": (
                "the bend equals 1 ONLY in the degenerate single-mode limits "
                "(d -> 0 and d -> infinity) and is strictly below in "
                "between, with an interior minimum. So a second positive "
                "mode never helps -- but the effect is NOT monotone in d, "
                "which an earlier draft of this script wrongly asserted and "
                "this assertion caught."
            ),
        },
        "sign_indefinite_escape": {
            "node_location_in_d": str(d_node),
            "series": signed,
            "can_exceed_observed_bend": signed_can_exceed,
            "reading": (
                "a DIFFERENCE of exponentials has a node and its bend is "
                "unbounded -- the same escape that survives the linear-readout "
                "and multiplicative exclusions. This is now the ONLY shape "
                "left standing in this direction; check any future candidate "
                "for it first."
            ),
        },
        "verdict": (
            "The additive interface class is EXCLUDED for positive modes "
            "(scope-(b), on the Lagrange identity -- a strict inequality, "
            "not a plausibility judgement): every positive sum of two "
            "geometric modes is log-CONVEX with bend <= 1, while the lepton "
            "tower is log-CONCAVE at 12.295. Not claimed: more than two "
            "modes (same identity, symmetrised over pairs, not formalised), "
            "and sign-indefinite combinations, which escape via a node."
        ),
    }

    all_ok = (
        results["lagrange_identity"]["verified"]
        and sweep_respects_bound
        and never_above_one
        and has_interior_min
        and signed_can_exceed
        and obs_bend > 1
    )

    w = WitnessBuilder(
        "lepton-tower-additive-screening",
        _script_path=__file__,
    )
    w.set_description(
        "Bean qou-htk4. Closes the additive-interface direction the "
        "multiplicative bend screen left open: every positive sum of two "
        "geometric modes is log-convex (bend <= 1) by the Lagrange form of "
        "Cauchy-Schwarz, while the lepton tower is log-concave at 12.295."
    )
    w.set_content_block("prop:lepton-continuant-recurrence")
    w.add_parameter("q0_anchor", "experimental/proton (q_parameter.Q_MP)")
    w.add_parameter("q0", str(q))
    for k, v in results.items():
        w.add_data(k, v)
    w.add_data("all_checks_passed", all_ok)
    # `all_ok` was already computed as the conjunction of six checks and
    # already stored, but only as data — so the witness claimed
    # `allPassed: true` over an empty assertion list (bean `qou-srvu`).
    # Asserting it makes the exclusion this script exists to establish
    # testable. The Lagrange residual is asserted separately against
    # `1e-40`, the bound the file itself declares at the `verified` flag,
    # so a regression in the identity is distinguishable from a regression
    # in the bend inequalities.
    w.add_assertion(
        "lagrange_identity_matches_direct_evaluation",
        str(identity_err), "0", tolerance="1e-40",
        source=(
            "max |x(w)x(w+4) - x(w+2)^2 - c d g^w h^w (g^2-h^2)^2| over the "
            f"{len(cases)} declared cases"
        ),
    )
    w.add_assertion(
        "additive_two_mode_exclusion_all_checks",
        all_ok, True,
        source=(
            "lagrange_identity.verified AND sweep_respects_bound AND "
            "never_above_one AND has_interior_minimum AND "
            "sign_indefinite_escape.can_exceed_observed_bend AND "
            "observed lepton bend > 1"
        ),
    )
    w.add_caveat(
        "Scope-(b) covers POSITIVE two-mode sums only. More than two modes "
        "is not formalised (the Lagrange identity generalises by "
        "symmetrising over pairs, but that is not done here). "
        "Sign-indefinite combinations are NOT excluded and are demonstrated "
        "above to escape -- they remain the one open shape in this "
        "direction."
    )
    w.save()

    print(f"observed lepton bend        = {obs_bend}")
    print(f"Lagrange identity max err   = {identity_err}")
    print()
    print(f"{'case':26s} {'bend':>18s}  <=1")
    print("-" * 52)
    for name, r in rows.items():
        print(f"{name:26s} {r['bend'][:18]:>18s}  {r['bend_le_one']}")
    print()
    print(f"positive sweep: {n_checked} towers, max bend = {max_bend} "
          f"(bound respected = {sweep_respects_bound})")
    print(f"bend never above 1 = {never_above_one}; interior minimum = "
          f"{has_interior_min} (NOT monotone in d)")
    print(f"sign-indefinite can exceed observed bend        = {signed_can_exceed}")
    print(f"VERDICT: additive class EXCLUDED for positive modes "
          f"(all_checks_passed={all_ok})")


if __name__ == "__main__":
    main()
