#!/usr/bin/env python3
"""qbeta_qnnq_theta_is_im_u_probe.py — ϑ_K is not a search target: the corpus
already DEFINES it, and the definition collides with a proved theorem.

THE DERIVATIONAL MOVE. Nine measured readings across four SDP probes failed to
supply ϑ_K, and continuing to enumerate readings is fitting-by-search. The
disciplined alternative is to ask what ϑ_K IS, from the channel's own
definition. The corpus answers it directly.

`QOU/QBeta/DeltaLambdaT5Assembly.lean` (`s_channel_at_substrate`):

    S(q₀) = A_ω · κ · (Re²u(q₀) − Im²u(q₀)),
    Re(u(q₀)) = ln q₀   (proved: meridian_holonomy_boost)
    ϑ_K       = Im(u(q₀))                                          (*)

and `QOU/QBeta/PhiBSArgumentIdentification.lean` documents the class field as
`u : ℝ → ℂ`, "the substrate → deformation map u(q₀) (LOG MERIDIAN HOLONOMY)".

So ϑ_K is the imaginary part of the meridian log-holonomy. The `ln²q₀ − ϑ²`
shape is just `Re²u − Im²u`. Nothing needed searching.

THE COLLISION. `QOU/Knot/FigureEightDeformedMeridianWinding.lean` proves,
sorry-free, that the SUBSTRATE-MATCHED Murakami meridian datum is

    u = N·t − 2πi·k,     t = ln q₀,  k ∈ ℤ₊     ⇒   Im u = −2πk.       (**)

Combining (*) and (**): **ϑ_K is quantized in units of 2π.** That is a
derivation-side constraint on ϑ, wholly independent of A_ω — exactly what the
arc has lacked. It is also testable against the A-free curve.

WHAT THIS PROBE CHECKS:
  D1  the quantized values ϑ = 2πk against the A-free curve
      (L − ϑ_μ²)/(L − ϑ_p²) = S_μ/S_p = r, L = ln²q₀, r < 0.
  D2  the k = 0 case, where ϑ vanishes at BOTH anchors.
  D3  the coincidence guard (see below).

THE COINCIDENCE GUARD (D3), stated so a later agent does not "discover" it.
The (k_μ, k_p) = (1, 2) row gives |ratio| = 0.2499 against |r| = 0.24539 — 1.9%
apart, which looks like a hit. It is not. In the small-L limit the ratio tends
to k_μ²/k_p² = 1/4 EXACTLY, and |r| merely happens to lie near 1/4. The sign is
also wrong: r < 0 requires the pair to straddle ln q₀, and with both ϑ > ln q₀
both factors are negative, forcing a positive ratio. Sign failure and straddle
failure are the same failure here, and neither is rescuable by choosing k.

Scope (STRICT). This derives no value of A_ω and proposes no ϑ. It reads two
corpus objects and reports that their conjunction is testable and fails. The
conclusion is a FORK, not a refutation of either object — see the verdict.

Run: python3 -u computations/probes/qbeta_qnnq_theta_is_im_u_probe.py \
       2>&1 | tee /tmp/qbeta_theta_is_im_u.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()

S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
Q0 = mp.mpf(Q_50_DIGIT_STR)


def main() -> int:
    print("=" * 78)
    print(" ϑ_K = Im(u) — the corpus already defines it, and it is quantized")
    print("=" * 78)

    lnq = mp.log(Q0)
    L = lnq**2
    r = S_MUON / S_PROTON
    print(f"\n  ln q₀ = {mp.nstr(lnq, 12)}   L = {mp.nstr(L, 12)}")
    print(f"  r = S_μ/S_p = {mp.nstr(r, 12)}   (r < 0 ⇒ the pair MUST straddle ln q₀)")
    print(f"  quantum 2π = {mp.nstr(2 * mp.pi, 12)}   — {mp.nstr(2 * mp.pi / lnq, 6)}× "
          f"larger than ln q₀")

    rows = []
    print(f"\n[D1] ϑ = 2πk from the proved meridian quantization Im u = −2πk:")
    print(f"    {'k_μ':>4} {'k_p':>4} {'ϑ_μ':>13} {'ϑ_p':>13} {'straddle':>9} "
          f"{'ratio':>15} {'|off|':>10}")
    for km in (0, 1):
        for kp in (1, 2, 3):
            tm, tp = 2 * mp.pi * km, 2 * mp.pi * kp
            straddle = bool(tm < lnq < tp)
            den = L - tp**2
            rr = (L - tm**2) / den if den != 0 else None
            off = abs(r / rr) if rr not in (None, 0) else None
            rows.append({"k_mu": km, "k_p": kp,
                         "theta_mu": mp.nstr(tm, 12), "theta_p": mp.nstr(tp, 12),
                         "straddles": straddle,
                         "ratio": mp.nstr(rr, 12) if rr is not None else None,
                         "factor_off": mp.nstr(off, 8) if off is not None else None,
                         "matches_r": bool(rr is not None
                                           and abs(rr - r) < mp.mpf("1e-3"))})
            print(f"    {km:>4} {kp:>4} {mp.nstr(tm, 8):>13} {mp.nstr(tp, 8):>13} "
                  f"{str(straddle):>9} {mp.nstr(rr, 10):>15} "
                  f"{mp.nstr(off, 6) if off else '-':>10}")

    straddlers = [x for x in rows if x["straddles"]]
    any_hit = any(x["matches_r"] for x in rows)
    best_off = min((mp.mpf(x["factor_off"]) for x in straddlers
                    if x["factor_off"]), default=None)

    # ---- D2: the k = 0 case kills itself on the measured sign flip ----
    print(f"\n[D2] k_μ = k_p = 0 ⇒ ϑ = 0 at BOTH anchors ⇒ "
          f"S = A_ω·κ·ln²q₀ > 0 for both.")
    print(f"     But the measured leaks have OPPOSITE signs "
          f"(S_μ = {mp.nstr(S_MUON, 8)} > 0 > S_p = {mp.nstr(S_PROTON, 8)}).")
    print(f"     So the common-k=0 solution is excluded by the data, not by a fit.")

    # ---- D3: the coincidence guard ----
    tm1, tp2 = 2 * mp.pi, 4 * mp.pi
    rr12 = (L - tm1**2) / (L - tp2**2)
    limit = mp.mpf(1) / 4
    print(f"\n[D3] COINCIDENCE GUARD. The (k_μ,k_p) = (1,2) row gives "
          f"|ratio| = {mp.nstr(abs(rr12), 8)} vs |r| = {mp.nstr(abs(r), 8)} "
          f"({mp.nstr(abs(abs(rr12) - abs(r)) / abs(r) * 100, 3)}% apart).")
    print(f"     NOT a hit: as L → 0 the ratio → k_μ²/k_p² = "
          f"{mp.nstr(limit, 6)} EXACTLY, and |r| merely lies near ¼. The sign is "
          f"wrong too — r < 0 needs straddling, and with both ϑ > ln q₀ both "
          f"factors are negative, forcing a POSITIVE ratio.")

    verdict = (
        "ϑ_K WAS NEVER A SEARCH TARGET — THE CORPUS DEFINES IT. "
        "DeltaLambdaT5Assembly's `s_channel_at_substrate` gives "
        "S = A_omega*kappa*(Re^2 u - Im^2 u) with Re u = ln q0 proved, so "
        "theta_K = Im(u(q0)), the imaginary part of the LOG MERIDIAN HOLONOMY "
        "(the class field's own documentation). The ln^2 q0 - theta^2 shape is "
        "just Re^2 u - Im^2 u. Nine measured readings were spent hunting a "
        "quantity that was already defined two files away. "
        "AND THE DEFINITION IS TESTABLE, because FigureEightDeformedMeridianWinding "
        "PROVES sorry-free that the substrate-matched meridian is "
        "u = N*t - 2*pi*i*k, hence Im u = -2*pi*k: theta_K is QUANTIZED in units "
        "of 2*pi. That is a derivation-side constraint on theta wholly "
        "independent of A_omega — the first the arc has had. "
        "IT FAILS, and cleanly. The k_mu = 0 rows are the FIRST readings in this "
        "entire arc to pass the straddling necessary condition that all nine "
        f"measured readings failed — and they then miss the A-free ratio by "
        f">= {mp.nstr(best_off, 6) if best_off else 'n/a'}x. The common k = 0 "
        "solution is excluded independently: it forces theta = 0 at BOTH anchors, "
        "so S has the same sign at both, contradicting the MEASURED sign flip. "
        "THE CONCLUSION IS A FORK, NOT A REFUTATION of either object: either "
        "(a) the T5 channel's u is NOT the substrate-matched Murakami meridian "
        "despite the two carrying identical documentation — in which case T5's "
        "'log meridian holonomy' wording is misleading and theta needs a stated "
        "alternative definition; or (b) the T4-inverted theta values are "
        "incompatible with the proved meridian quantization. Both branches are "
        "cheap to settle and either one is worth more than another reading. "
        "Scope (a): nothing here refutes the Murakami theorem (proved) or the T5 "
        "assembly (proved); it reports that their CONJUNCTION is falsifiable and "
        "false. No A_omega derived, no theta proposed, nothing wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-qnnq-theta-is-im-u", engine="mpmath")
    wb.set_description(
        "The derivational move for qou-qnnq. theta_K is not a search target: "
        "DeltaLambdaT5Assembly defines it as Im(u(q0)), the imaginary part of "
        "the log meridian holonomy. FigureEightDeformedMeridianWinding proves "
        "sorry-free that the substrate-matched meridian has Im u = -2*pi*k, so "
        "theta_K is quantized in units of 2*pi — a derivation-side constraint "
        "independent of A_omega. Tested against the A-free curve: the k_mu = 0 "
        "rows are the first readings in the arc to pass the straddling "
        "necessary condition, then miss the ratio by >= 890x; common k = 0 is "
        "excluded by the measured sign flip. Conclusion is a FORK — either the "
        "T5 u is not the Murakami meridian, or the T4 thetas are incompatible "
        "with the proved quantization. Includes a coincidence guard against the "
        "(1,2) row's spurious 1.9% magnitude agreement. Nothing fitted.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("theta_definition",
                "theta_K = Im(u(q0)) per DeltaLambdaT5Assembly.s_channel_at_substrate; "
                "u is the log meridian holonomy per SDeformedVolumeChannel.u")
    wb.add_data("quantization",
                "Im u = -2*pi*k for the substrate-matched Murakami meridian "
                "(FigureEightDeformedMeridianWinding, sorry-free)")
    wb.add_data("D1_quantized_rows", rows)
    wb.add_data("D2_common_k_zero_excluded_by_sign_flip", True)
    wb.add_data("D3_coincidence_guard", {
        "row": "(k_mu,k_p)=(1,2)",
        "abs_ratio": mp.nstr(abs(rr12), 12),
        "abs_r": mp.nstr(abs(r), 12),
        "small_L_limit": "k_mu^2/k_p^2 = 1/4 exactly",
        "why_not_a_hit": "the agreement is with 1/4, which the ratio tends to "
                         "identically as L -> 0; |r| merely lies near 1/4. The "
                         "sign is also wrong, and sign failure == straddle "
                         "failure here."})
    wb.add_data("any_reading_matches_r", bool(any_hit))
    wb.add_data("verdict", verdict)
    wb.add_assertion("quantized_theta_fails_the_a_free_curve",
                     computed=0.0 if any_hit else 1.0, expected=1.0,
                     tolerance=0.5,
                     source="no (k_mu, k_p) row reproduces r = S_mu/S_p within 1e-3")
    wb.add_assertion("some_quantized_row_straddles",
                     computed=1.0 if straddlers else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="the k_mu = 0 rows satisfy theta_mu < ln q0 < theta_p — "
                            "the necessary condition every measured reading failed")
    wb.save()
    print("  witness -> computations/probes/qbeta-qnnq-theta-is-im-u.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
