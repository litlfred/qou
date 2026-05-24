#!/usr/bin/env python3
"""Strategy G (alternative to D, from agent brief
`docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`):
direct evaluation of known closed-form Skein-family polynomials of
the Borromean link 𝓑_3 at q_0, with no PSLQ.

Hypothesis under test:

    λ_scale  =  some closed-form expression in
                {V(𝓑_3)(q_0), Q(𝓑_3)(q_0), HOMFLYPT(𝓑_3)(q_0; or)}

These three polynomials have well-known closed forms:

  Jones polynomial of 𝓑_3 (Kauffman bracket normalisation):
    V(𝓑_3, t) = -t^{-3} + 3·t^{-2} - 2·t^{-1} + 4 - 2·t + 3·t^2 - t^3
    (Borromean rings; e.g. Murasugi "Knot Theory and Its Applications".)

  Kauffman bracket via Skein:
    ⟨𝓑_3⟩(A) — standard recursive evaluation in A = t^{-1/4}.

  HOMFLYPT polynomial of 𝓑_3 (a, z):
    P(𝓑_3; a, z) — multi-variable Skein invariant; here we evaluate
    at the SU_q(N) specialisation a = q^{N-1}, z = q - q^{-1}, with
    N = 2 (Jones limit) and N = 3 (cross-check).

We evaluate each at q = q_0 ≈ 1.110 and check if any direct value,
or any small-integer linear combination, equals λ_p = 2.4599527869.

No PSLQ — these are categorical invariants of 𝓑_3 with KNOWN closed
forms; the test is just whether one of them equals the target.

Per brief, this is a low-cost structural check that complements
Strategy A/B (Li_2^q / Φ_q PSLQ) and Strategy D (LP/SDP on 𝓑_p)
without overlapping their search spaces.
"""
from __future__ import annotations
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 80


def jones_borromean_at_t(t_val: mp.mpf) -> mp.mpf:
    """V(𝓑_3, t) = -t^{-3} + 3·t^{-2} - 2·t^{-1} + 4 - 2·t + 3·t^2 - t^3.

    Standard Borromean Jones polynomial; symmetric under t ↔ t^{-1}
    (mirror-symmetric 3-component link). Reference: Murasugi
    "Knot Theory and Its Applications" §10.6.
    """
    t = t_val
    return (
        -t ** (-3)
        + 3 * t ** (-2)
        - 2 * t ** (-1)
        + 4
        - 2 * t
        + 3 * t ** 2
        - t ** 3
    )


def kauffman_bracket_borromean_at_A(A_val: mp.mpf) -> mp.mpf:
    """Kauffman bracket ⟨𝓑_3⟩(A) via writhe-normalised Jones.

    Bracket-to-Jones bridge:  V(L, t) = (-A)^(-3·w(L)) · ⟨L⟩  at  t = A^{-4}.
    Borromean has writhe 0 in its standard 6-crossing alternating diagram,
    so ⟨𝓑_3⟩(A) = V(𝓑_3, A^{-4}).
    """
    return jones_borromean_at_t(A_val ** (-4))


def homflypt_borromean_at_az(a_val: mp.mpf, z_val: mp.mpf) -> mp.mpf:
    """P(𝓑_3; a, z) — closed form.

    For the alternating 6-crossing standard diagram, the HOMFLYPT
    polynomial of the Borromean link is (Lickorish-Millett 1986):
      P(𝓑_3; a, z) =
        (a^4 + a^{-4}) · (z^4 - 4·z^2 + 4)
        + (2·z^4 - 8·z^2 + 6)·(a^2 + a^{-2})
        + (z^6 - 7·z^4 + 12·z^2 - 6)
    (multi-variable Skein; the Jones specialisation a = t^{-1} and
    z = t^{1/2} - t^{-1/2} recovers V(𝓑_3, t) up to normalisation.)
    """
    a = a_val
    z = z_val
    return (
        (a ** 4 + a ** (-4)) * (z ** 4 - 4 * z ** 2 + 4)
        + (2 * z ** 4 - 8 * z ** 2 + 6) * (a ** 2 + a ** (-2))
        + (z ** 6 - 7 * z ** 4 + 12 * z ** 2 - 6)
    )


def main() -> int:
    w = WitnessBuilder(
        "lambda-scale-alt-g-skein-polynomial-direct",
        engine="mpmath",
    )
    w.set_description(
        "Strategy G: direct evaluation of closed-form Skein-family "
        "polynomials of 𝓑_3 — Jones V, Kauffman ⟨·⟩, HOMFLYPT P — at "
        "q_0, check if any natural combination yields λ_p = 2.4599527869. "
        "No PSLQ; structural test complementary to Strategies A/B/D."
    )
    w.set_content_block("conj:borromean-baryon-mass-formula")
    w.add_parameter("dps", 80)

    Q0 = mp.mpf(Q_50_DIGIT_STR)
    HBAR = (Q0 - 1) / Q0
    VOL_B3 = 8 * mp.catalan

    target = mp.mpf("2.4599527869")
    print(f"q_0           = {mp.nstr(Q0, 20)}")
    print(f"target λ_p    = {mp.nstr(target, 20)}")
    print(f"Vol(𝓑_3)/ℏ_q² = {mp.nstr(VOL_B3 / HBAR**2, 14)}")
    print()

    candidates: dict[str, mp.mpf] = {}

    # 1. Jones at q_0 directly
    V_at_q = jones_borromean_at_t(Q0)
    candidates["V(𝓑_3, q_0)"] = V_at_q
    print(f"V(𝓑_3, q_0)               = {mp.nstr(V_at_q, 16)}")

    # 2. Jones at q_0² (sometimes the relevant substitution)
    V_at_qsq = jones_borromean_at_t(Q0 ** 2)
    candidates["V(𝓑_3, q_0²)"] = V_at_qsq
    print(f"V(𝓑_3, q_0²)              = {mp.nstr(V_at_qsq, 16)}")

    # 3. Jones at q_0^{1/2}
    V_at_qhalf = jones_borromean_at_t(mp.sqrt(Q0))
    candidates["V(𝓑_3, sqrt q_0)"] = V_at_qhalf
    print(f"V(𝓑_3, √q_0)              = {mp.nstr(V_at_qhalf, 16)}")

    # 4. Kauffman bracket at A = q_0^{1/2}
    A_val = mp.sqrt(Q0)
    K = kauffman_bracket_borromean_at_A(A_val)
    candidates["<𝓑_3>(q_0^{1/2})"] = K
    print(f"⟨𝓑_3⟩(q_0^{{1/2}})         = {mp.nstr(K, 16)}")

    # 5. HOMFLYPT at SU_q(2) substitution: a = q^{-1}, z = q - q^{-1}
    z_val = Q0 - 1 / Q0
    P_su2 = homflypt_borromean_at_az(Q0 ** (-1), z_val)
    candidates["P_HOMFLYPT(𝓑_3, q_0^-1, q_0 - q_0^-1)"] = P_su2
    print(f"P(𝓑_3, q_0^-1, q_0-q_0^-1) = {mp.nstr(P_su2, 16)}  (SU(2))")

    # 6. HOMFLYPT at SU_q(3) substitution: a = q, z = q - q^{-1}
    P_su3 = homflypt_borromean_at_az(Q0, z_val)
    candidates["P_HOMFLYPT(𝓑_3, q_0, q_0 - q_0^-1)"] = P_su3
    print(f"P(𝓑_3, q_0, q_0-q_0^-1)    = {mp.nstr(P_su3, 16)}  (SU(3))")

    # 7. Suggestive ratios from V
    print()
    print("Suggestive ratios + roots:")
    cube_root_V = mp.cbrt(V_at_q)
    candidates["V(𝓑_3, q_0)^{1/3}"] = cube_root_V
    print(f"V(𝓑_3, q_0)^{{1/3}}        = {mp.nstr(cube_root_V, 16)}")

    sqrt_V_qsq = mp.sqrt(V_at_qsq)
    candidates["sqrt V(𝓑_3, q_0²)"] = sqrt_V_qsq
    print(f"√V(𝓑_3, q_0²)             = {mp.nstr(sqrt_V_qsq, 16)}")

    five_over_two_minus_K = mp.mpf("2.5") - HBAR ** 2 * K
    candidates["5/2 - ℏ_q² · <𝓑_3>"] = five_over_two_minus_K
    print(f"5/2 - ℏ_q² · ⟨𝓑_3⟩         = {mp.nstr(five_over_two_minus_K, 16)}")

    # 8. Scoring
    print()
    print("Distance to target λ_p:")
    print(f"{'name':50s} {'value':18s} {'|rel diff|':>10s}")
    print("-" * 80)
    scored = []
    for name, val in candidates.items():
        rel = abs(val - target) / target
        scored.append((rel, name, val))
        print(f"{name:50s} {mp.nstr(val, 12):18s} {mp.nstr(rel, 4):>10s}")

    scored.sort(key=lambda r: r[0])
    print()
    best_rel, best_name, best_val = scored[0]
    print(f"BEST: {best_name} = {mp.nstr(best_val, 14)}")
    print(f"  rel diff to target = {mp.nstr(best_rel, 6)}")
    print()
    match_thresh = mp.mpf("1e-6")
    if best_rel < match_thresh:
        verdict = "MATCH-1ppm"
    elif best_rel < mp.mpf("1e-4"):
        verdict = "CLOSE (<100 ppm)"
    elif best_rel < mp.mpf("0.01"):
        verdict = "WEAK-SIGNAL (<1%)"
    else:
        verdict = "FAR (>1%)"
    print(f"VERDICT: {verdict}")
    if not verdict.startswith("MATCH"):
        print(
            "  -> Strategy G FAILS as a single-polynomial identity; the "
            "Skein-family polynomials of 𝓑_3 evaluated at q_0 (or at "
            "standard substitutions) do not directly yield λ_p."
        )

    single_poly_match = bool(best_rel < match_thresh)
    single_poly_falsified = int(not single_poly_match)

    w.add_data("candidates", {k: mp.nstr(v, 20) for k, v in candidates.items()})
    w.add_data("best_candidate_name", best_name)
    w.add_data("best_candidate_value", mp.nstr(best_val, 30))
    w.add_data("best_candidate_rel_diff", mp.nstr(best_rel, 20))
    w.add_data("target_lambda_p", mp.nstr(target, 30))
    w.add_data("verdict", verdict)

    # Per repo convention (cf. probe_phiq_n_star_rule.py): falsification
    # probes assert the refutation so the witness `allPassed` stays true
    # and audit dashboards don't classify the expected-negative result as
    # a regression. Strategy G's hypothesis ("a single Borromean Skein
    # polynomial value at q_0 = λ_scale") is expected to be falsified at
    # 1 ppm; the assertion passes iff no candidate lands within 1 ppm.
    w.add_assertion(
        "strategy_g_single_polynomial_identity_falsified_at_1ppm",
        computed=single_poly_falsified,
        expected=1,
        tolerance=None,
        source=(
            "Direct evaluation of Borromean Jones / Kauffman / HOMFLYPT "
            "closed forms at q_0; passes when no single value lands "
            "within 1 ppm of λ_p."
        ),
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
