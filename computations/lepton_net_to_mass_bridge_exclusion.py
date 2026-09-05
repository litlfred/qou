#!/usr/bin/env python3
"""Bean qou-lsp9: the net(T(2,n)) -> lepton mass map. VERDICT: the
multiplicative bridge class is excluded, and the exclusion is derived,
not fitted.

CONTEXT. `prop:lepton-continuant-recurrence` gives the Groebner-Shirshov
normal form of the lepton-tower braid T(2,n) = sigma_0^n in H_2(q),

    NF(sigma_0^n) = a_n * 1 + b_n * sigma_0,
    b_0 = 0, b_1 = 1, b_{n+1} = h b_n + b_{n-1},   h = q - 1/q,
    a_n = b_{n-1},   net(T(2,n)) = a_n + b_n = b_{n-1} + b_n.

The corpus assigns T(2,3), T(2,5), T(2,7) to e, mu, tau. Bean qou-lsp9
records that the net is NOT a mass: net ratios 1.2455 / 1.2408 against
observed 206.8 / 16.8, and asks for the missing bridge. The sibling
probe deliberately refused to patch it with a fitted scale factor.

THIS SCRIPT derives WHY no scale factor exists, rather than searching
for one (AGENTS.md formalize-first probe discipline: find the invariant
that prunes the class before running the wide search).

(1) CLOSED FORM. h = q - 1/q means x^2 - h x - 1 has roots q and -1/q,
    so the continuant has the Binet form

        b_n * (q + 1/q) = q^n - (-1)^n q^{-n}.

    Hence for odd n (the whole genus-admissible window {3,5,7,9}),

        net(n) = [ (q^{n-1} - q^{-(n-1)}) + (q^n + q^{-n}) ] / (q + 1/q).

    Sorry-free Lean twin: `QOU/Archimedean/lepton_continuant_binet.lean`
    (`morganVoyceBK_binet`, `netK_ratio_rigidity`).

(2) THE INVARIANT. net is asymptotically GEOMETRIC in the winding:

        net(n+2) / net(n) = q^2 * (1 + O(q^{-2n})).

    So log net is affine in n up to an EXPONENTIALLY DECAYING remainder.
    The observed lepton tower is log-CONCAVE: log-increments 5.332 then
    2.822, a factor 1.89 apart and falling.

(3) THE EXCLUSION. Take the whole multiplicative bridge class

        m_n = C * g^n * net(n)^p        (C, g, p free reals)

    -- every power law, every exponential-times-power, and the "missing
    scale factor" the bean asks for (p = 1, g = 1). Ratio rigidity:

        m_{n+2}/m_n = g^2 * (net(n+2)/net(n))^p,

    so the step-to-step variation of the mass ratio is carried ENTIRELY
    by the variation of the net ratio -- which is the O(q^{-2n})
    remainder, ~0.38% here. To reproduce the observed 12.3x drop between
    the two steps, p must absorb 12.3 out of 1.0038: p ~ 664, and then
    g^2 ~ 1e-61 to bring the magnitude back. The class does not fail by
    having no solution; it fails by requiring an exponentially
    fine-tuned exponent that fits a vanishing remainder, and p grows
    like q^{2n} for any further generation. That is the exclusion.

(4) STRUCTURAL DIAGNOSIS. T(2,n) are TORUS knots -- Seifert fibred, not
    hyperbolic, hyperbolic volume 0. The canonical mass route
    m = m_e * Vol(K) * rho(K) / hbar_q^2 therefore supplies NO
    generation dependence through the lepton's own identity knot. The
    corpus's own working muon mass uses Vol(4_1) -- the figure-eight
    HIGGS knot, a different and hyperbolic knot (CAL-2 proxy
    m_mu/m_e = Vol(4_1)/hbar_q^2). So in this framework mass enters
    through the Higgs-knot coupling, not through the lepton's torus
    knot, and the continuant net -- an amplitude of the torus braid's
    normal form -- is not the carrier of the mass. No scale factor can
    repair a quantity that is not carrying the observable.

HONEST SCOPE. Scope-(b) for the stated class ONLY: "m_n = C g^n net^p is
excluded" is backed by the proved Binet asymptotics (the invariant), not
by a failed search. Scope-(a) everywhere else: this does NOT show the
continuant is irrelevant to generation structure -- the divisibility
result (T(2,9) harmonic of T(2,3)) stands untouched, and a NON-
multiplicative bridge (an additive/interface term, or a Higgs-coupling
route where n enters through the linking of T(2,n) with 4_1 rather than
through net) is not excluded. What is closed is the bean's premise that
a scale factor is missing: it is not missing, it does not exist.

q_0 CONVENTION. Experimental/proton pin (`q_parameter.Q_MP`), per the
2026-08-07 owner directive that all new compute defaults to the
experimental anchor. No ideal-layer cache is read, so no layer
straddling is possible here.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402

from mpmath import mp, mpf, log  # noqa: E402
from codata_constants import M_E_MEV

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# CODATA / PDG lepton masses (MeV). Used only as the TARGET of the
# excluded map -- no constant here is fitted or tuned.
M_E = M_E_MEV
M_MU = mpf("105.6583755")
M_TAU = mpf("1776.86")


def morgan_voyce_b(n_max: int, h):
    """b_0..b_{n_max} evaluated at the substrate h (mpmath)."""
    b = [mpf(0), mpf(1)]
    for _ in range(2, n_max + 1):
        b.append(h * b[-1] + b[-2])
    return b


def main() -> None:
    set_compute_dps()
    q = mp.mpf(Q_MP)
    h = q - 1 / q

    N = 13
    b = morgan_voyce_b(N, h)
    net = {n: b[n - 1] + b[n] for n in range(1, N + 1)}

    # --- (1) Binet closed form, verified against the recurrence -------------
    def binet_b(n):
        return (q ** n - (-1) ** n * q ** (-n)) / (q + 1 / q)

    binet_max_err = max(abs(binet_b(n) - b[n]) for n in range(0, N + 1))

    # --- (2) net ratios vs the asymptotic q^2 -------------------------------
    q2 = q ** 2
    net_ratios = {}
    for n in (3, 5, 7, 9, 11):
        r = net[n + 2] / net[n]
        net_ratios[n] = {
            "ratio": str(r),
            "minus_q_squared": str(r - q2),
            "rel_excess_over_q2": str((r - q2) / q2),
        }

    # --- (3) the observed tower, and the exponent each step demands ---------
    obs_ratio_1 = M_MU / M_E          # e -> mu
    obs_ratio_2 = M_TAU / M_MU        # mu -> tau
    net_ratio_1 = net[5] / net[3]
    net_ratio_2 = net[7] / net[5]

    # A pure power law m = C * net^p (g = 1) needs one p per step:
    p_step_1 = log(obs_ratio_1) / log(net_ratio_1)
    p_step_2 = log(obs_ratio_2) / log(net_ratio_2)

    # The full class m = C g^n net^p has two ratio equations and two free
    # parameters (g^2, p), so it admits a unique solution -- the point is
    # what that solution looks like.
    p_fit = log(obs_ratio_1 / obs_ratio_2) / log(net_ratio_1 / net_ratio_2)
    g2_fit = obs_ratio_1 / net_ratio_1 ** p_fit

    # Round-trip: the fit is exact by construction; report it so the
    # degeneracy is visible rather than hidden behind a residual.
    check_1 = g2_fit * net_ratio_1 ** p_fit
    check_2 = g2_fit * net_ratio_2 ** p_fit

    # --- (4) log-concavity of the observed tower, log-linearity of net -----
    obs_log_increments = [str(log(obs_ratio_1)), str(log(obs_ratio_2))]
    net_log_increments = [str(log(net_ratio_1)), str(log(net_ratio_2))]

    results = {
        "binet_closed_form": {
            "formula": "b_n * (q + 1/q) = q^n - (-1)^n q^{-n}",
            "max_abs_err_vs_recurrence_n_0_to_13": str(binet_max_err),
            "verified": binet_max_err < mpf("1e-40"),
        },
        "net_ratio_vs_q_squared": {
            "q_squared": str(q2),
            "by_winding": net_ratios,
            "asymptotic_law": "net(n+2)/net(n) = q^2 (1 + O(q^{-2n}))",
        },
        "observed_tower": {
            "m_mu_over_m_e": str(obs_ratio_1),
            "m_tau_over_m_mu": str(obs_ratio_2),
            "ratio_of_ratios": str(obs_ratio_1 / obs_ratio_2),
            "log_increments": obs_log_increments,
            "log_concave": True,
        },
        "net_tower": {
            "net_5_over_net_3": str(net_ratio_1),
            "net_7_over_net_5": str(net_ratio_2),
            "ratio_of_ratios": str(net_ratio_1 / net_ratio_2),
            "log_increments": net_log_increments,
            "log_linear_to_exponentially_small_remainder": True,
        },
        "pure_power_law_p_per_step": {
            "p_from_e_to_mu": str(p_step_1),
            "p_from_mu_to_tau": str(p_step_2),
            "disagreement_factor": str(p_step_1 / p_step_2),
            "verdict": "no single p; a pure power law (g=1) is excluded",
        },
        "full_class_fit": {
            "class": "m_n = C * g^n * net(n)^p",
            "p_fit": str(p_fit),
            "g_squared_fit": str(g2_fit),
            "roundtrip_ratio_1": str(check_1),
            "roundtrip_ratio_2": str(check_2),
            "verdict": (
                "solvable but degenerate: p ~ 664 fits the 0.38% "
                "O(q^{-2n}) remainder of the net ratio, g^2 ~ 1e-61 "
                "restores the magnitude. Both parameters are "
                "exponentially fine-tuned and p grows like q^{2n} for "
                "any further generation -- not a physical map."
            ),
        },
        "structural_diagnosis": {
            "torus_knot_volume": 0,
            "note": (
                "T(2,n) are Seifert-fibred, not hyperbolic, so "
                "Vol(T(2,n)) = 0 and the canonical mass route "
                "m = m_e Vol(K) rho(K) / hbar_q^2 gives no generation "
                "dependence through the lepton's own identity knot. The "
                "corpus's working muon mass uses Vol(4_1) -- the "
                "hyperbolic Higgs knot -- so mass enters via the "
                "Higgs-knot coupling, not via the torus braid's "
                "normal-form amplitude."
            ),
        },
        "verdict": (
            "EXCLUDED (scope-(b) for the multiplicative class "
            "m_n = C g^n net(n)^p, on the proved Binet asymptotics). "
            "The bean's premise is wrong: the scale factor is not "
            "missing, it does not exist. Non-multiplicative bridges "
            "(additive interface term; Higgs-coupling route where n "
            "enters through linking with 4_1) are NOT excluded."
        ),
    }

    all_ok = (
        results["binet_closed_form"]["verified"]
        and p_step_1 / p_step_2 > mpf("1.5")
    )

    w = WitnessBuilder(
        "lepton-net-to-mass-bridge-exclusion",
        _script_path=__file__,
    )
    w.set_description(
        "Bean qou-lsp9. Derives the Binet closed form of the "
        "Morgan-Voyce continuant net(T(2,n)) and uses its log-linearity "
        "to exclude the whole multiplicative net -> lepton-mass bridge "
        "class m_n = C g^n net(n)^p."
    )
    w.set_content_block("prop:lepton-continuant-recurrence")
    w.add_parameter("q0_anchor", "experimental/proton (q_parameter.Q_MP)")
    w.add_parameter("q0", str(q))
    w.add_parameter("h", str(h))
    for k, v in results.items():
        w.add_data(k, v)
    w.add_data("all_checks_passed", all_ok)
    w.add_caveat(
        "Scope-(b) applies ONLY to the multiplicative class "
        "m_n = C g^n net(n)^p, and rests on the proved Binet "
        "asymptotics. Non-multiplicative bridges (an additive interface "
        "term; a Higgs-coupling route where n enters through linking "
        "with 4_1 rather than through net) are NOT excluded."
    )
    # ── Assertion (bean qou-srvu) ────────────────────────────────
    # This witness reported `allPassed: true` while asserting nothing.
    # The check already existed: `binet_max_err` is computed at line
    # ~131 and stored under a field literally named `verified`, using
    # this file's own 1e-40 — but nothing asserted it, so a consumer
    # reading `allPassed` could not see it fail.
    #
    # Not a self-comparison: `b[n]` comes from the Morgan-Voyce
    # RECURRENCE and `binet_b(n)` from the closed form
    # (q^n - (-1)^n q^-n)/(q + 1/q). A wrong closed form, a wrong sign
    # convention or an off-by-one in the recurrence all break it. The
    # exclusion argument this witness records reads the net values off
    # that closed form, so if it were wrong the whole conclusion would
    # be about a different sequence.
    w.add_assertion(
        "binet_closed_form_matches_recurrence",
        computed=mp.nstr(binet_max_err, 8),
        expected="0",
        tolerance="1e-40",
        source=(
            "max over n = 0..13 of |binet_b(n) - b[n]|; closed form vs "
            "Morgan-Voyce recurrence, two independent routes"
        ),
    )
    w.save()

    print(f"q_0 (proton pin) = {q}")
    print(f"h = q - 1/q      = {h}")
    print(f"Binet max err    = {binet_max_err}")
    print(f"net ratios       = {net_ratio_1}, {net_ratio_2}")
    print(f"q^2              = {q2}")
    print(f"observed ratios  = {obs_ratio_1}, {obs_ratio_2}")
    print(f"p per step       = {p_step_1}, {p_step_2}  (factor "
          f"{p_step_1 / p_step_2})")
    print(f"full-class fit   = p {p_fit}, g^2 {g2_fit}")
    print("VERDICT: multiplicative bridge class EXCLUDED "
          f"(all_checks_passed={all_ok})")


if __name__ == "__main__":
    main()
