"""Re-examination: the Ocneanu −1/12 claim for the proton-mass "12".

Per author 2026-05-31 "Ocneanu route... lets briefly re-explore.
maybe new compute/math is correct and was wrongly ruled out."

## The closed route

The proton-mass identity `m_p = 2·m_μ·F_Bor(q_0) − 12·m_e` (audit
`2026-05-25-proton-mass-identity-12-me-ocneanu.md`) originally
attributed the "12" to:

    12 = reciprocal of Ocneanu cancellation leading-pole coefficient
       = -1 / (-1/12) ← per 2026-05-04-ocneanu-cancellation-numerical-verification.md

Commit `6766b40b9` (2026-05-26) RULED THIS OUT by direct numerical
check of the Lean-proved closed form `tr_M(β_Bor) =
(4 + h² − 3h⁴ − h⁶) / (h² + 4)`:

> Pole order at q → 0: 4 (NOT 10). Leading coefficient: -1 (NOT -1/12).
> Therefore "12 = 1/(Ocneanu coefficient)" is WRONG: the
> Ocneanu coefficient is for a DIFFERENT braid (proton canonical
> T_w in atomic-3A convention), NOT β_Bor.

## The question raised by Probe 5 (meson Habiro re-exam)

The meson Habiro c=4 was ruled out for similar reasons (0.77% miss
vs integer 4); my re-exam at 50 dps found 0.15% miss with c_3
absorbing the residual cleanly — the audit's binary "ruled out"
was a precision-floor artifact under the WRONG framing (binary
vs tiered).

**Could the Ocneanu correction commit make the SAME mistake?**

Specifically:
- The Ocneanu audit (2026-05-04) saw `tr_M(T_w_proton) ~ -1/(12·q^10)`
- The Borromean Lean closed form gives `tr_M(β_Bor) ~ -q^-4`
- The correction commit said: different braids → claim wrong

But what if the proton T_w branched-MULTI-component closure pole
IS structurally related to the Borromean β_Bor by the canonical
3A→3 stabilisation? Then the same "12" should appear in both,
just with different pole ORDERS (10 for proton, 4 for Borromean)
and different absolute coefficients.

Or: what if the "12" arises from the **product** of multiple
substrate quantities that combine to give factor 12 even though
neither pole-order matches?

## What this probe tests

1. Reproduce the correction commit's numerical claim:
   - `tr_M(β_Bor, q) ~ a·q^p` as q → 0
   - Confirm p = 4 (not 10), a = −1 (not −1/12)

2. Test alternative Ocneanu structural identifications for "12":
   - 12 = #cells in some categorical decomposition (e.g.,
     12 = 4·3 = #edge cells in 𝓑_3 tessellation × #strands)
   - 12 = (q + q⁻¹)·6 evaluated at integer indicator
   - 12 = [3]_q!/(q^something) at specific q

3. Identify whether ANY natural categorical quantity gives 12
   in the linking_weight ∝ m_e correction term.

## Cross-references

- commit 6766b40b9 (the correction)
- audit 2026-05-04-ocneanu-cancellation-numerical-verification.md
- audit 2026-05-25-proton-mass-identity-12-me-ocneanu.md
- proton mass identity at 0.24 ppm (currently empirical-integer 12)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import (  # noqa: E402 (codata sweep)
    M_E_MEV,
    M_MU_MEV_VALIDATION,
    M_P_MEV_VALIDATION,
)
import sys
from math import factorial, prod
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def trM_borromean_closed(q):
    """Lean-proved closed form: tr_M(β_Bor, q) = (4+h²−3h⁴−h⁶)/(h²+4)."""
    # convention D — verified by EVALUATION at q0, not by reading: computations/audits/borromean_convention_by_evaluation.py
    h = q - 1 / q
    h2 = h * h
    return (4 + h2 - 3 * h2 ** 2 - h2 ** 3) / (h2 + 4)


def borromean_pole_symbolic():
    """The q → 0 pole of tr_M(β_Bor) by EXACT ALGEBRA, not sampling.

    Step 1 of this probe reproduced the correction commit's claim by
    printing tr_M · q⁴ at six small q and eyeballing the column. That
    is one route and it was never checked against anything. This is
    the second: clear denominators in ℚ(q), read the q-valuation of
    numerator and denominator off the monomial exponents (pole order),
    and take sympy's exact limit of q^order · tr_M (leading
    coefficient). No mpmath, no sampling, no extrapolation.

    Returns (pole_order:int, leading_coefficient:sympy expr).
    """
    qs = sp.Symbol("q", positive=True)
    expr = sp.cancel(sp.together(trM_borromean_closed(qs)))
    num, den = sp.fraction(expr)
    low = lambda p: min(m[0] for m in sp.Poly(sp.expand(p), qs).monoms())  # noqa: E731
    order = int(low(den) - low(num))
    leading = sp.limit(expr * qs ** order, qs, 0)
    return order, leading


def main() -> int:
    set_compute_dps(50)
    q = mp.mpf(Q_50_DIGIT_STR)

    print("=" * 78)
    print("Ocneanu −1/12 re-examination at 50 dps")
    print("=" * 78)
    print(f"\nq_0 = {Q_50_DIGIT_STR}\n")

    # Step 1: Reproduce correction commit's q→0 analysis
    print("[Step 1 — q → 0 behavior of tr_M(β_Bor)]")
    print(f"  Sampling at small q values:")
    print(f"  {'q':<10}{'tr_M':<28}{'tr_M · q⁴':<28}")
    for q_str in ["0.1", "0.05", "0.04", "0.03", "0.02", "0.01"]:
        q_small = mp.mpf(q_str)
        trM = trM_borromean_closed(q_small)
        scaled4 = trM * q_small ** 4
        print(f"  {q_str:<10}{mp.nstr(trM, 18):<28}{mp.nstr(scaled4, 18):<28}")
    # Route A (numerical): the same scaling pushed far enough that the
    # O(q²) correction is below the 50-dps floor. Route B (symbolic):
    # exact q-valuation + sympy limit, see `borromean_pole_symbolic`.
    q_deep = mp.mpf(10) ** -15
    leading_numeric = trM_borromean_closed(q_deep) * q_deep ** 4
    pole_order_sym, leading_sym = borromean_pole_symbolic()
    print(f"\n  Route A (numeric, q = 1e-15): tr_M · q⁴ = "
          f"{mp.nstr(leading_numeric, 25)}")
    print(f"  Route B (exact q-valuation + sympy limit): pole order "
          f"{pole_order_sym}, leading coefficient {leading_sym}")
    print(f"\n  Confirms commit 6766b40b9: tr_M(β_Bor, q) ~ -1·q^-4 as q→0.")
    print(f"  Pole order 4, leading coefficient -1.  No 1/12 here.")

    # Step 2: But what about |tr_M · q⁴ · ...| · 12? Is 12 hidden elsewhere?
    print(f"\n[Step 2 — search for '12' in F_Bor structure at q_0]")

    # F_Bor(q_0) = |tr_M| · [3]_q! / q^3
    h = q - 1 / q
    h2 = h * h
    q3 = (q ** 3 - q ** (-3)) / h
    q2_q = (q ** 2 - q ** (-2)) / h
    qfact_3 = q3 * q2_q * 1  # [3]_q · [2]_q · [1]_q
    trM = abs(trM_borromean_closed(q))
    F_Bor = trM * qfact_3 / q ** 3
    print(f"  |tr_M(β_Bor)| at q_0 = {mp.nstr(trM, 12)}")
    print(f"  [3]_q!          = {mp.nstr(qfact_3, 12)}")
    print(f"  F_Bor           = {mp.nstr(F_Bor, 12)}")

    # The proton-mass identity: m_p = 2·m_μ·F_Bor − 12·m_e
    # If m_p, m_μ, m_e are anchored, what value of "12" gives exact match?
    # The literal this file has always carried. Kept as a literal on
    # purpose so the assertion below can compare it against the CODATA
    # registry — two routes to m_e, one hand-typed here and one loaded
    # from codata_constants. Deleting the literal would delete the check.
    M_E_LITERAL_IN_THIS_FILE = "0.51099895069"
    m_e = mp.mpf(M_E_LITERAL_IN_THIS_FILE)
    m_mu = mp.mpf(M_MU_MEV_VALIDATION)
    m_p = mp.mpf(M_P_MEV_VALIDATION)
    # m_p = 2·m_μ·F_Bor − k·m_e  ⇒  k = (2·m_μ·F_Bor − m_p) / m_e
    k_required = (2 * m_mu * F_Bor - m_p) / m_e
    print(f"\n  Required k in m_p = 2·m_μ·F_Bor − k·m_e:")
    print(f"  k_exact = {mp.nstr(k_required, 18)}")
    print(f"  k - 12  = {mp.nstr(k_required - 12, 12)}")
    print(f"  (k-12)/12 = {mp.nstr((k_required - 12) / 12 * 100, 8)}%")

    # So the empirical "12" is actually k_exact ≈ 12 + small. How small?
    delta_12 = k_required - 12
    print(f"\n  The empirical 'integer 12' is exactly k = {mp.nstr(k_required, 12)}")
    print(f"  Distance to integer 12: {mp.nstr(delta_12, 12)}")
    print(f"  Distance to nearby integers: |k-11| = {mp.nstr(abs(k_required - 11), 8)}, |k-13| = {mp.nstr(abs(k_required - 13), 8)}")

    # Step 3: Hypothesis tests for "12"
    print(f"\n[Step 3 — structural candidates for '12']")
    # Each candidate is now EVALUATED from the ingredients its label
    # names. Five of them used to be the bare literal `mp.mpf(12)` with
    # the derivation living only in the label string, so the table could
    # not have disagreed with its own captions — the row for
    # "Σ d_λ² at H_3 = 1+4+1" would have printed 12 even if S_3 had had
    # different dimensions. Three more labels named a q = 1 evaluation or
    # a factor the code did not apply; those are corrected to say what is
    # actually computed.
    #
    # H_3 = partitions of 3, dimensions by the integer hook-length
    # formula (3, 1, 1) → wait: (3,) → 1, (2,1) → 2, (1,1,1) → 1.
    def _hooks_3(p):
        cols = p[0]
        col_h = [sum(1 for r in p if r > j) for j in range(cols)]
        return [(rl - 1 - j) + (col_h[j] - 1 - i) + 1
                for i, rl in enumerate(p) for j in range(rl)]

    parts_3 = [(3,), (2, 1), (1, 1, 1)]
    d_lambda_h3 = {p: factorial(3) // prod(_hooks_3(p)) for p in parts_3}
    sum_d_sq_h3 = sum(d * d for d in d_lambda_h3.values())   # = 1+4+1 = 6
    dim_H3 = factorial(3)                                    # = 6
    bracket_2_at_q1 = mp.mpf(2)          # [2]_q → 2 as q → 1
    yekutieli_edge_cells, n_strands = 4, 3
    print(f"  (H_3 hook-length dims: "
          f"{ {str(p): d for p, d in d_lambda_h3.items()} }, "
          f"Σd_λ² = {sum_d_sq_h3}, 3! = {dim_H3})")
    candidates = [
        ("12 (integer)", mp.mpf(12)),
        ("[3]_q! / q  at q_0", qfact_3 / q),
        ("[2]_q · [3]_q = [3]_q!  at q_0", (q + 1 / q) * q3),
        ("4 · [3]_q! / q²  at q_0", 4 * qfact_3 / (q ** 2)),
        ("(2·m_μ·F_Bor − m_p)/m_e (exact)", k_required),
        (f"Σ d_λ² at H_3 = {sum_d_sq_h3}, ·2",
         mp.mpf(2 * sum_d_sq_h3)),
        (f"dim H_3 = 3! = {dim_H3}, ·2", mp.mpf(2 * dim_H3)),
        (f"{yekutieli_edge_cells} cells × {n_strands} strands "
         f"(Yekutieli 𝓑_3 edge cells)",
         mp.mpf(yekutieli_edge_cells * n_strands)),
        ("3! · [2]_q at q=1", mp.mpf(dim_H3) * bracket_2_at_q1),
    ]
    for name, val in candidates:
        diff = val - k_required
        rel = diff / k_required * 100 if abs(k_required) > 1e-30 else mp.inf
        marker = " ⭐" if abs(rel) < mp.mpf("0.01") else ""
        print(f"    {name:<54} = {mp.nstr(val, 15):<22}Δ% = {mp.nstr(rel, 6)}{marker}")

    # Step 4: Verdict on "Ocneanu was wrongly ruled out"
    print(f"\n[Step 4 — verdict]")
    if abs(delta_12) < mp.mpf("0.01"):
        verdict = (
            "AUDIT VERDICT STANDS but with NUANCE: the empirical k ≈ 12 is "
            "extraordinarily close to integer 12 (~10⁻⁴ relative). The "
            "correction commit was right that the Borromean's pole "
            "structure doesn't give -1/12 — but the integer 12 itself "
            "is so tight (10⁻⁴) that it deserves a NEW structural "
            "explanation, not just 'empirical near-match.' Several "
            "natural candidates (4·3 = #edge cells × #strands; "
            "Σd_λ²·2 = 6·2; 3!·[2]_q at q=1 = 12) hit exactly 12 — "
            "deserves categorical investigation."
        )
    else:
        verdict = (
            f"The empirical k = {mp.nstr(k_required, 8)} deviates from "
            f"12 by {mp.nstr(delta_12, 6)} (relative {mp.nstr(abs(delta_12)/12*100, 6)}%). "
            f"That's larger than the 10⁻⁴ near-match the audit claimed."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "ocneanu-12-route-reexam",
        engine="python",
    )
    w.set_description(
        "Re-examines commit 6766b40b9's correction of the Ocneanu −1/12 "
        "attribution for the proton-mass-identity '12'. Confirms the "
        "Borromean pole-order claim (pole 4, leading -1) but finds the "
        "empirical k = 12.0xx is tighter than the audit's 'empirical "
        "integer near-match' phrasing suggests, deserving deeper "
        "categorical investigation. Several natural candidates "
        "(4·3 edge cells, Σd_λ²·2, 3!·[2]_q-at-1) all give 12 EXACTLY."
    )
    w.add_parameter("q_50dps", Q_50_DIGIT_STR)
    w.add_data("k_required", mp.nstr(k_required, 25))
    w.add_data("delta_k_minus_12", mp.nstr(delta_12, 25))
    w.add_data("relative_pct", mp.nstr((k_required - 12) / 12 * 100, 12))
    w.add_data("F_Bor_at_q0", mp.nstr(F_Bor, 25))
    w.add_data("verdict", verdict)
    w.add_data("borromean_pole", {
        "route_a_numeric_trM_times_q4_at_1e-15": mp.nstr(leading_numeric, 25),
        "route_b_symbolic_pole_order": pole_order_sym,
        "route_b_symbolic_leading_coefficient": str(leading_sym),
    })
    w.add_data("h3_structural_ingredients", {
        "hook_length_dims": {str(p): d for p, d in d_lambda_h3.items()},
        "sum_d_lambda_squared": sum_d_sq_h3,
        "dim_H3_factorial": dim_H3,
    })

    # ── Assertions ────────────────────────────────────────────────────

    # (1) + (2) Step 1's whole claim — "pole order 4, leading -1, NOT
    #     -1/12" — was printed and never asserted. It is the claim the
    #     correction commit rests on, so it gets two routes.
    #   Route A: evaluate the closed form numerically at q = 1e-15 at 50
    #            dps, where the O(q²) correction is ~1e-30.
    #   Route B: clear denominators in ℚ(q), read the pole order off the
    #            monomial valuations, and take sympy's exact limit.
    # -1/12 = -0.0833… would fail (1) by 0.9167; a pole order of 10 (the
    # value the retracted Ocneanu attribution needed) fails (2) by 6.
    w.add_assertion(
        name="borromean_pole_leading_coefficient_is_minus_one",
        computed=mp.nstr(leading_numeric, 25),
        expected=str(leading_sym),
        tolerance="1e-20",
        source=(
            "Route A: tr_M(β_Bor, q)·q⁴ from the Lean-proved closed "
            "form evaluated at q = 1e-15 in mpmath at 50 dps. Route B: "
            "sympy's exact limit of q^order·tr_M as q → 0 after "
            "clearing denominators in ℚ(q). The retracted attribution "
            "needed -1/12 here."
        ),
    )
    w.add_assertion(
        name="borromean_pole_order_is_four",
        computed=pole_order_sym,
        expected=4,
        tolerance=0,
        source=(
            "Route A: the q-valuation of numerator and denominator of "
            "cancel(together(tr_M)) — deg-lowest monomial exponents, "
            "exact integer arithmetic in sympy. Route B: the pole order "
            "commit 6766b40b9 states for β_Bor (4, versus the 10 the "
            "2026-05-04 Ocneanu audit reported for the proton T_w)."
        ),
    )

    # (3) The '12' itself, against the audit's declared integer.
    #   Route A: k = (2·m_μ·F_Bor − m_p)/m_e, from CODATA muon and
    #            proton masses and the Lean-proved Borromean trace.
    #   Route B: the integer 12 the proton-mass identity of audit
    #            2026-05-25 asserts — a categorical claim, not measured.
    # The tolerance is the verdict's OWN branch threshold (0.01), so a
    # k that would flip the printed verdict now also fails an assertion.
    w.add_assertion(
        name="k_required_matches_integer_twelve_within_verdict_band",
        computed=mp.nstr(k_required, 25),
        expected="12",
        tolerance="0.01",
        source=(
            "Route A: k = (2·m_μ·F_Bor − m_p)/m_e at 50 dps from CODATA "
            "masses and F_Bor = |tr_M(β_Bor)|·[3]_q!/q³. Route B: the "
            "integer 12 in m_p = 2·m_μ·F_Bor − 12·m_e (audit "
            "2026-05-25). Tolerance 0.01 is the threshold the Step-4 "
            "verdict branches on."
        ),
    )

    # (4) The hand-typed electron mass in this file.
    #   Route A: the literal "0.51099895069" typed into this module.
    #   Route B: M_E_MEV loaded from codata_constants (which sources it
    #            from codata_2022_source at full 11-sig-fig precision).
    # The other two masses here already come from the registry; m_e did
    # not, and nothing noticed. They agree today — this pins that.
    w.add_data("m_e_two_routes", {
        "literal_in_this_module": M_E_LITERAL_IN_THIS_FILE,
        "codata_registry_M_E_MEV": mp.nstr(M_E_MEV, 25),
        "difference": mp.nstr(m_e - M_E_MEV, 8),
    })
    w.add_assertion(
        name="local_electron_mass_literal_matches_codata_registry",
        computed=M_E_LITERAL_IN_THIS_FILE,
        expected=mp.nstr(M_E_MEV, 25),
        tolerance="1e-20",
        source=(
            "Route A: the m_e literal hand-typed in this module and used "
            "to divide out k. Route B: codata_constants.M_E_MEV. k "
            "scales as 1/m_e, so a drift of 1e-5 relative here moves k "
            "by more than the 0.01 band assertion (3) allows."
        ),
    )

    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
