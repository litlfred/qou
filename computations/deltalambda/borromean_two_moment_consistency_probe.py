#!/usr/bin/env python3
"""borromean_two_moment_consistency_probe.py — the two-moment cross-check the
Borromean/Brunnian Δ_λ magnitude lead was missing.

CONTEXT (0-fit, all inputs upstream). The Δ_λ residual-moment closure identifies
the A-body irreducible residual moment μ_A (forward AME−model, #4320) with the
A-component Brunnian cluster c_A = E₀·(1−τ_{L_A}) at the ρ_F-matched cabled level:
  A=3: Borromean 3-cluster at H₉ (three width-3 cables) — #4360 (sign), #4364
       (magnitude near-miss: c₃ = +0.297 MeV = 0.63× μ₃, O(h⁴), 0-fit).
  A=4: genuine 4-Brunnian [[A₀₁,A₁₂],A₂₃] at H₁₂ (four width-3 cables) —
       a4_h12_brunnian_deficit_measure_probe.py (sign: τ_L₄>1 ⇒ c₄<0, O(h⁶)).
Each isotope's SIGN is derived (μ₃>0 / μ₄<0, the Milnor parity law (−1)^{A−1}).

THE MISSING TEST. The μ₃ near-miss (0.63×) was reported as a "LEAD" on a SINGLE
moment. A single moment matched to 0.6× is weak evidence. The decisive check is
whether the SAME 0-fit framing reproduces BOTH moments at a CONSISTENT fraction —
a two-moment cross-check no prior probe ran. This probe does it, reading both
derived cluster values (0-fit) from their committed witnesses and comparing the
fractions c_A/μ_A and the A-scaling.

RESULT (0-fit, from the committed witnesses).
  f₃ = c₃(H₉)/μ₃  = +0.297 / +0.4708 = 0.63×   (1.6× short)
  f₄ = c₄(H₁₂)/μ₄ = −0.0582 / −4.591 = 0.0127× (~79× short)
  ⇒ the two magnitude fractions are INCONSISTENT by ~50×.
  A-TREND IS BACKWARDS: the physical residual moments GROW with A
  (|μ₄/μ₃| = 9.75×) while the Brunnian clusters SHRINK (|c₄/c₃| = 0.20×) —
  because the 4-link is O(h⁶) vs the 3-link's O(h⁴), i.e. MORE h-suppressed.

CONCLUSION (scope-(a), STRICT honesty). The signs are derived at both A (Milnor
parity holds), but the Brunnian-cluster = residual-moment identification FAILS the
two-moment magnitude consistency test badly: it reproduces μ₃ to 0.63× and μ₄ to
only 0.0127×, and gets the A-scaling QUALITATIVELY WRONG (clusters shrink where
the data grows). The extra O(h²) suppression per Brunnian order is intrinsic to
the topology (first Milnor invariant at length A ⇒ O(h^{2(A−1)})), so it cannot be
tuned away without a fit. This DOWNGRADES the μ₃ 0.63× near-miss from a "lead"
toward a likely coincidence: a framework that matches one moment to 0.6× but the
next to 0.01×, with the A-trend inverted, is not capturing the magnitude physics.
The SIGN leg (Milnor parity) stands; the MAGNITUDE identification does not survive
the second moment. No fit; μ_A never inverted; nothing wired.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _pb  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def _load(name, *keys):
    with open(HERE / name, encoding="utf-8") as fh:
        d = json.load(fh)
    for k in keys:
        d = d[k]
    return d


def main() -> int:
    # μ_A targets + c_A(cabled) — both 0-fit, read from the committed A=4 witness
    a4 = _load("a4-h12-brunnian-deficit-measure.witness.json", "results")
    mu3 = mp.mpf(a4["a4_residual_target"]["mu3"])
    mu4 = mp.mpf(a4["a4_residual_target"]["mu4"])
    c4_h12 = mp.mpf(a4["a4_brunnian_cabled_h12"]["c4_MeV"])
    ord4 = mp.mpf(a4["a4_brunnian_base_n4"]["leading_milnor_order"])
    # c₃(H₉) from the A=3 magnitude-lift witness (#4364)
    a3 = _load("borromean-h9-magnitude-lift.witness.json", "results")
    c3_h9 = mp.mpf(a3["atom_dressed_mean"]["c3_mean_MeV"])
    ord3 = mp.mpf(a3["h_order_diagnostic"]["fitted_leading_exponent"])

    f3 = c3_h9 / mu3
    f4 = c4_h12 / mu4
    inconsistency = max(f3, f4) / min(f3, f4)          # ratio of the two fractions
    moment_trend = abs(mu4 / mu3)                       # data: grows
    cluster_trend = abs(c4_h12 / c3_h9)                 # framework: shrinks
    trend_backwards = cluster_trend < 1 < moment_trend

    # DECOMPOSE the inconsistency: intrinsic h-order (framework's OWN prediction) vs
    # the residual coefficient-scaling gap. Brunnian A-link ⇒ leading O(h^{2(A−1)})
    # (first Milnor at length A), so ĉ_A := c_A/h^{2(A−1)} is the order-normalized
    # cabling coefficient. The h-order part is a PROVED topological prediction; the
    # coefficient part is what a derived (W_λ / tower) route must additionally supply.
    h = mp.mpf(_load("a4-h12-brunnian-deficit-measure.witness.json", "parameters")["h"])
    ch3 = c3_h9 / h ** 4                                # order-normalized A=3 coeff
    ch4 = abs(c4_h12) / h ** 6                          # order-normalized A=4 coeff
    coeff_growth = ch4 / ch3                            # framework coeff growth
    coeff_gap = moment_trend / coeff_growth            # residual after removing h-order
    h_order_factor = 1 / h ** 2                         # intrinsic per-order suppression
    # structural: h<1 ⇒ clusters VANISH with A while moments grow ⇒ id excluded beyond one A
    h_suppressed_structural = h < 1

    print(f"  μ₃={mp.nstr(mu3,6)}  c₃(H₉)={mp.nstr(c3_h9,6)}  f₃=c₃/μ₃={mp.nstr(f3,5)}  (order h^{mp.nstr(ord3,3)})", flush=True)
    print(f"  μ₄={mp.nstr(mu4,6)}  c₄(H₁₂)={mp.nstr(c4_h12,6)}  f₄=c₄/μ₄={mp.nstr(f4,5)}  (order h^{mp.nstr(ord4,3)})", flush=True)
    print(f"  two-moment fraction inconsistency f₃/f₄ = {mp.nstr(inconsistency,5)}×", flush=True)
    print(f"  A-trend: |μ₄/μ₃|={mp.nstr(moment_trend,4)} (data GROWS)  vs  |c₄/c₃|={mp.nstr(cluster_trend,4)} (framework SHRINKS)  → backwards: {trend_backwards}", flush=True)
    print(f"  DECOMPOSITION: intrinsic h-order 1/h²={mp.nstr(h_order_factor,4)}× (framework's OWN O(h^2(A-1)) prediction)", flush=True)
    print(f"    order-normalized coeff growth ĉ₄/ĉ₃={mp.nstr(coeff_growth,4)} vs moment {mp.nstr(moment_trend,4)} ⇒ residual COEFFICIENT gap {mp.nstr(coeff_gap,4)}×", flush=True)
    print(f"  STRUCTURAL: clusters ~ h^(2(A-1)), h={mp.nstr(h,4)}<1 ⇒ VANISH with A while moments grow ⇒ id holds at most one A: {h_suppressed_structural}", flush=True)

    signs_ok = (c3_h9 > 0 and mu3 > 0) and (c4_h12 < 0 and mu4 < 0)
    fractions_inconsistent = inconsistency > mp.mpf("10")   # ~50× here
    orders_differ = abs(ord4 - ord3) > mp.mpf("1")          # h⁶ vs h⁴
    coeff_gap_persists = coeff_gap > mp.mpf("1.5")          # ~2.17× after removing h-order

    assertions = [
        ("signs_derived_both_moments_milnor_parity", bool(signs_ok)),
        ("two_moment_fractions_inconsistent", bool(fractions_inconsistent)),
        ("A_trend_backwards_clusters_shrink_moments_grow", bool(trend_backwards)),
        ("brunnian_order_grows_h4_to_h6", bool(orders_differ)),
        ("coefficient_scaling_gap_persists_after_order_norm", bool(coeff_gap_persists)),
        ("clusters_h_suppressed_structural_incompatibility", bool(h_suppressed_structural)),
    ]

    verdict = (
        f"TWO-MOMENT CROSS-CHECK FAILS — the Borromean/Brunnian magnitude identification does "
        f"NOT survive the second moment (scope-(a), 0-fit). SIGNS derived at both A (Milnor "
        f"parity (−1)^{{A−1}}: μ₃>0, μ₄<0). But the SAME framing gives f₃=c₃/μ₃={mp.nstr(f3,4)} "
        f"(0.63×, the near-miss) and f₄=c₄/μ₄={mp.nstr(f4,4)} (~79× short) — INCONSISTENT by "
        f"{mp.nstr(inconsistency,4)}×. The A-trend is BACKWARDS: the physical residual moments "
        f"GROW (|μ₄/μ₃|={mp.nstr(moment_trend,4)}) while the Brunnian clusters SHRINK "
        f"(|c₄/c₃|={mp.nstr(cluster_trend,4)}), because the 4-link is O(h⁶) vs the 3-link's "
        f"O(h⁴) — intrinsic topological suppression (first Milnor at length A ⇒ O(h^{{2(A−1)}})), "
        f"un-tunable without a fit. DECOMPOSITION: the {mp.nstr(inconsistency,4)}× splits into "
        f"the intrinsic h-order 1/h²={mp.nstr(h_order_factor,4)}× (the framework's OWN proved "
        f"O(h^{{2(A−1)}}) prediction) × a residual coefficient-scaling gap {mp.nstr(coeff_gap,4)}× "
        f"(order-normalized coeff growth ĉ₄/ĉ₃={mp.nstr(coeff_growth,4)} vs the moment "
        f"{mp.nstr(moment_trend,4)}). STRUCTURAL: since h={mp.nstr(h,4)}<1, the clusters "
        f"c_A~h^{{2(A−1)}} VANISH as A grows while the moments grow — so the identification c_A=μ_A "
        f"can hold at most at ONE A and is structurally excluded as a magnitude closure for the "
        f"sequence. CONCLUSION: this DOWNGRADES the μ₃ 0.63× 'near-miss' toward a coincidence. The "
        f"SIGN leg (Milnor parity) stands; the MAGNITUDE identification does not. No fit; μ_A never "
        f"inverted; nothing wired."
    )
    print("\nVERDICT:", verdict, flush=True)

    wb = WitnessBuilder("borromean-two-moment-consistency", engine="mpmath")
    wb.set_description(
        "Two-moment cross-check of the Borromean/Brunnian Δ_λ magnitude identification (0-fit, "
        "from committed witnesses). Signs derived at both A (Milnor parity), but the same framing "
        "gives c₃/μ₃=0.63× and c₄/μ₄=0.0127× — inconsistent ~50×, with the A-trend backwards "
        "(clusters shrink O(h⁴)→O(h⁶) where the data grows). Downgrades the μ₃ near-miss toward "
        "coincidence; the magnitude identification fails the second moment. No fit; nothing wired.")
    wb.set_audit_only("docs/audits/2026-08-01-deltalambda-borromean-two-moment-consistency.md")
    for name, passed in assertions:
        wb.add_assertion(name, str(passed), "True")
    wb.add_data("mu3", mp.nstr(mu3, 10)); wb.add_data("c3_H9_MeV", mp.nstr(c3_h9, 10))
    wb.add_data("mu4", mp.nstr(mu4, 10)); wb.add_data("c4_H12_MeV", mp.nstr(c4_h12, 10))
    wb.add_data("fraction_c3_over_mu3", mp.nstr(f3, 10))
    wb.add_data("fraction_c4_over_mu4", mp.nstr(f4, 10))
    wb.add_data("two_moment_inconsistency_factor", mp.nstr(inconsistency, 8))
    wb.add_data("moment_trend_mu4_over_mu3", mp.nstr(moment_trend, 8))
    wb.add_data("cluster_trend_c4_over_c3", mp.nstr(cluster_trend, 8))
    wb.add_data("h", mp.nstr(h, 10))
    wb.add_data("intrinsic_h_order_factor_1_over_h2", mp.nstr(h_order_factor, 8))
    wb.add_data("order_normalized_coeff_growth", mp.nstr(coeff_growth, 8))
    wb.add_data("residual_coefficient_scaling_gap", mp.nstr(coeff_gap, 8))
    wb.add_data("order_h_A3", mp.nstr(ord3, 5)); wb.add_data("order_h_A4", mp.nstr(ord4, 5))
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if all(p for _, p in assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
