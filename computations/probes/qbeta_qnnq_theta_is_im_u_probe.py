#!/usr/bin/env python3
"""qbeta_qnnq_theta_is_im_u_probe.py — ϑ_K is not a search target: the corpus
already DEFINES it, and the definition collides with a proved theorem.

THE DERIVATIONAL MOVE. Nine measured readings across four SDP probes failed to
supply ϑ_K, and continuing to enumerate readings is fitting-by-search. The
disciplined alternative is to ask what ϑ_K IS, from the channel's own
definition. The corpus answers it directly.

`QOU/QBeta/DeltaLambdaT5Assembly.lean` (`s_channel_at_substrate`):

    S(q₀) = A_ω · κ · (Re²u(q₀) − Im²u(q₀)),
    Re(u(q₀)) = ln q₀   (HYPOTHESIS `hRe`, NOT proved — see the correction below)
    ϑ_K       = Im(u(q₀))                                          (*)

CORRECTION (bean qou-5nze, settled after this probe was written). Two claims in
the original version of this docstring were wrong, and both are fixed here:

  (i)  `Re(u(q₀)) = ln q₀` was attributed to a lemma `meridian_holonomy_boost`.
       NO SUCH DECLARATION EXISTS anywhere in the corpus. It is an undischarged
       hypothesis of `s_channel_at_substrate`. The attribution originated in the
       T5 module docstring and was copied here and into the bean.

  (ii) (*) and (**) below were combined as if compatible. They are not: the
       meridian's real part is `N·t`, not `t`, so combining them silently sets
       N = 1 — the one-dimensional colouring, at which the coloured Jones is
       identically 1 and the deformed volume conjecture (an N → ∞ statement)
       is empty.

The fork this probe opened is now CLOSED, in favour of branch (a): the two `u`
are different objects. `SDeformedVolumeChannel` has ZERO instances in the corpus
and constrains `u` not at all — proved sorry-free in
`QOU/QBeta/ChannelMeridianIdentification.lean` (`channelFree`), which also
carries the N = 1 obstruction and the sign-flip refutation.

The numerical D1/D2/D3 results below STAND as computed; what changed is their
reading. They do not test "the corpus definition of ϑ_K" — there is no such
definition — they test the CONJUNCTION of the channel with the Murakami
identification, and that conjunction is what fails.

and `QOU/QBeta/PhiBSArgumentIdentification.lean` documents the class field as
`u : ℝ → ℂ`, "the substrate → deformation map u(q₀) (LOG MERIDIAN HOLONOMY)".

That WORDING is what suggested ϑ_K is the imaginary part of a meridian
log-holonomy. The wording is all there is: the class's only axiom is
`S_eq`, and it places no condition on `u` whatever (`channelFree`). The
`ln²q₀ − ϑ²` shape is just `Re²u − Im²u` under the assumed `hRe`.

THE COLLISION. `QOU/Knot/FigureEightDeformedMeridianWinding.lean` proves,
sorry-free, that the SUBSTRATE-MATCHED Murakami meridian datum is

    u = N·t − 2πi·k,     t = ln q₀,  k ∈ ℤ₊     ⇒   Im u = −2πk.       (**)

IF the channel's `u` were this meridian, ϑ_K would be quantized in units of 2π —
a derivation-side constraint wholly independent of A_ω, which is exactly what
the arc has lacked, and which is testable against the A-free curve. That IF is
the hypothesis under test here; per (ii) above it already costs N = 1.

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

Scope (STRICT), scope-(a) per AGENTS.md §"Before declaring refuted". This
derives no value of A_ω and proposes no ϑ. It reads two corpus objects and
reports that their CONJUNCTION fails; both objects stand on their own. The
probe originally left this as a fork; the fork is now settled in favour of
branch (a) by Lean reading, and the surviving open question is definitional —
`ϑ_K` has no stated definition in the corpus, only a docstring phrase.

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
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

set_compute_dps()

S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
Q0 = Q_MP


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
        "theta_K HAS NO CORPUS DEFINITION — ONLY A DOCSTRING PHRASE. "
        "This probe originally read DeltaLambdaT5Assembly's "
        "`s_channel_at_substrate` as DEFINING theta_K = Im(u(q0)) with "
        "'Re u = ln q0 proved'. Both halves were wrong, and the bean qou-5nze "
        "Lean reading has now settled it: (i) the cited lemma "
        "`meridian_holonomy_boost` DOES NOT EXIST anywhere in the corpus — "
        "`hRe` is an undischarged HYPOTHESIS of that theorem; and (ii) "
        "`SDeformedVolumeChannel` has ZERO instances and constrains `u` not at "
        "all, its only axiom being S_eq. 'Log meridian holonomy' is a docstring "
        "phrase attached to a free class field, not a definition. "
        "WHAT THE NUMBERS BELOW ACTUALLY TEST is the CONJUNCTION of that channel "
        "with the substrate-matched Murakami meridian of "
        "FigureEightDeformedMeridianWinding (u = N*t - 2*pi*i*k, Im u = -2*pi*k, "
        "proved sorry-free), which WOULD quantize theta in units of 2*pi — a "
        "derivation-side constraint independent of A_omega, the first the arc has "
        "had. THE CONJUNCTION FAILS, three ways, none of them a fit. "
        "First, it costs the degenerate colour: the meridian's real part is N*t, "
        "not t, so `hRe` forces N = 1, at which the coloured Jones is identically "
        "1 and the deformed volume conjecture (an N -> infinity statement) is "
        "empty. Second, the k_mu = 0 rows are the FIRST readings in this entire "
        "arc to pass the straddling necessary condition that all nine measured "
        f"readings failed — and they then miss the A-free ratio by "
        f">= {mp.nstr(best_off, 6) if best_off else 'n/a'}x. Third, the common "
        "k = 0 solution is excluded independently: it forces theta = 0 at BOTH "
        "anchors, so S has the same sign at both, contradicting the MEASURED sign "
        "flip. All three are Lean-proved sorry-free in "
        "QOU/QBeta/ChannelMeridianIdentification.lean. "
        "SCOPE (a): nothing here refutes the Murakami theorem or the T5 assembly "
        "— both stand; what is excluded is their CONJUNCTION. The surviving open "
        "question is DEFINITIONAL, and better posed than the search it replaces: "
        "theta_K needs a stated definition before any reading can be tested "
        "against it. No A_omega derived, no theta proposed, nothing wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-qnnq-theta-is-im-u", engine="mpmath")
    wb.set_description(
        "The derivational move for qou-qnnq, with its own premise corrected. "
        "theta_K has NO corpus definition: SDeformedVolumeChannel has zero "
        "instances and constrains its field u not at all, and the T5 docstring's "
        "'Re u = ln q0 (proved: meridian_holonomy_boost)' cites a lemma that does "
        "not exist — hRe is an undischarged hypothesis (bean qou-5nze). What is "
        "tested here is the CONJUNCTION of that channel with the substrate-matched "
        "Murakami meridian (Im u = -2*pi*k, proved sorry-free), which would "
        "quantize theta in units of 2*pi. It fails three ways: it forces the "
        "degenerate colour N = 1 (the meridian's real part is N*t, not t); the "
        "k_mu = 0 rows pass the straddling condition — a first for this arc — then "
        "miss the A-free ratio by >= 890x; and common k = 0 is excluded by the "
        "measured sign flip. All three proved sorry-free in "
        "QOU/QBeta/ChannelMeridianIdentification.lean. Scope (a): both source "
        "objects stand; only their conjunction is excluded. Includes a coincidence "
        "guard against the (1,2) row's spurious 1.9% magnitude agreement. "
        "Nothing fitted.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("theta_definition",
                "NONE. theta_K = Im(u(q0)) holds only under the undischarged "
                "hypothesis hIm of DeltaLambdaT5Assembly.s_channel_at_substrate; "
                "SDeformedVolumeChannel.u is a free class field (zero instances "
                "in the corpus, only axiom S_eq), so 'log meridian holonomy' is "
                "a docstring phrase, not a definition. Proved: "
                "QOU.QBeta.ChannelMeridianIdentification.channelFree")
    wb.add_data("hRe_citation_is_phantom",
                "DeltaLambdaT5Assembly cited `meridian_holonomy_boost` for "
                "Re u = ln q0; no such declaration exists in the corpus "
                "(bean qou-5nze). Corrected in this PR.")
    wb.add_data("quantization",
                "Im u = -2*pi*k for the substrate-matched Murakami meridian "
                "(FigureEightDeformedMeridianWinding, sorry-free) — applies to "
                "THAT meridian, not to the channel's unconstrained u")
    wb.add_data("identification_forces_trivial_colour",
                "Re(meridian) = N*t, so hRe : Re u = ln q0 forces N = 1, the "
                "colouring at which the coloured Jones is identically 1. Proved: "
                "QOU.QBeta.ChannelMeridianIdentification.color_eq_one_of_re_eq_log")
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
                     computed="0" if any_hit else "1", expected="1",
                     tolerance="0.5",
                     source="no (k_mu, k_p) row reproduces r = S_mu/S_p within 1e-3")
    wb.add_assertion("some_quantized_row_straddles",
                     computed="1" if straddlers else "0", expected="1",
                     tolerance="0.5",
                     source="the k_mu = 0 rows satisfy theta_mu < ln q0 < theta_p — "
                            "the necessary condition every measured reading failed")
    wb.save()
    print("  witness -> computations/probes/qbeta-qnnq-theta-is-im-u.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
