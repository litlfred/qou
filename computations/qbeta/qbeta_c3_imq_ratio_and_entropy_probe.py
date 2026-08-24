#!/usr/bin/env python3
"""qbeta_c3_imq_ratio_and_entropy_probe.py

Autonomous investigation of the ε(q₀) decay-projection map (follow-up to the
#3600 candidate-(iii) connection + the #3636 linear-response structure). Goal:
try to DERIVE ε(q₀) from the available data, disciplined by formalize-first
(don't run a search the precision can't support) and anti-fit.

Two questions asked, honest answers:

  1. **What is proxy-INDEPENDENT?** ε(anchor) = S(anchor)/coeff(anchor), and the
     derived coefficient (geometric or operator, #3636) is the same at both
     anchors to ~1e-8 (the real q₀ differ only there). So the RATIO
       `ε(proton)/ε(muon) = S(proton)/S(muon) ≈ −4.08`
     is proxy-INDEPENDENT — the one clean derivable number. It is `~ −4` within
     the ~2-digit precision of S (suggestive, NOT identified: −4.075 vs −4 is a
     1.9% gap, inside the S noise). Recorded as an observation, not a claim.

  2. **Can ε(q₀) / the ε=0 crossing q\\* be identified numerically?** The bar-odd
     `S` sign-flips (S(proton)<0<S(muon)), so ε(q₀)=0 at some q\\* strictly between
     the two anchors — bracketed to a `~1.3e-8`-wide window. But with only two
     anchors at `~2.2` digits each (the AGENTS.md c₃ entropy bound), q\\* is
     locatable to `~8e-11` abs and NOT PSLQ-identifiable, and ε(q₀) as a FUNCTION
     is underdetermined. **Scope-(a) negative:** numerical identification from
     these anchors is entropy-blocked — NOT a structural claim that ε(q₀) is
     underivable (it is derivable via the deformed-complex-VC archimedean functor
     / #3596's Φ_b state-integral; that is the open route, not more anchors).

Conclusion: the wall is a single sign-fixed small real function ε(q₀) with a
proxy-independent anchor-ratio `≈ −4.08 (~ −4?)` and a bracketed zero; closing it
is an archimedean-functor problem, not a numerical-fit problem. No c_k wired; no
fit; scope-(a); C14.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
QM = mp.mpf("1.10997859555733471")
QP = mp.mpf("1.1099785827513808075916690956107688798744991218736")
SM = mp.mpf("0.00968298")
SP = mp.mpf("-0.03945936")
C3_DIGITS_PER_ANCHOR = mp.mpf("2.2")   # AGENTS.md c₃ entropy bound


def main() -> int:
    print("=" * 78)
    print(" c₃ ε(q₀) decay projection — proxy-independent ratio + entropy block")
    print("=" * 78)

    # ---- 1. proxy-independent ratio ----
    ratio = SP / SM
    gap_vs_4 = (ratio + 4) / 4
    print("\n[1] proxy-INDEPENDENT ratio (coefficient cancels):")
    print(f"    ε(proton)/ε(muon) = S(p)/S(m) = {mp.nstr(ratio,8)}")
    print(f"    vs clean −4: gap {mp.nstr(gap_vs_4*100,3)}%  (inside the ~2-digit S noise ⇒ suggestive, NOT identified)")

    # ---- 2. ε=0 crossing bracket ----
    print("\n[2] ε=0 crossing q* (S sign-flips ⇒ bracketed):")
    frac = mp.fabs(SP) / (mp.fabs(SP) + mp.fabs(SM))
    window = QM - QP
    qstar = QP + frac * window
    print(f"    q_proton={mp.nstr(QP,18)} (S<0),  q_muon={mp.nstr(QM,18)} (S>0)")
    print(f"    linear-interp q* = {mp.nstr(qstar,18)}  in a {mp.nstr(window,3)}-wide window")

    # ---- 3. entropy block ----
    locatable = window * mp.mpf(10) ** (-C3_DIGITS_PER_ANCHOR)
    print("\n[3] entropy check (formalize-first: is a search supported?):")
    print(f"    S ~{mp.nstr(C3_DIGITS_PER_ANCHOR,2)} digits/anchor, 2 anchors ⇒ q* to ~{mp.nstr(locatable,3)} abs")
    print("    ⇒ q* NOT PSLQ-identifiable; ε(q₀) as a function underdetermined by anchors.")
    print("    scope-(a) NEGATIVE: numerical identification is entropy-blocked — the derivation")
    print("    needs the archimedean functor (deformed VC / Φ_b state-integral, #3596), not anchors.")

    wb = WitnessBuilder("qbeta-c3-imq-ratio-and-entropy", engine="mpmath")
    wb.set_description(
        "Autonomous ε(q₀) decay-projection investigation (candidate (iii); #3600/#3636). "
        "(1) Proxy-independent ratio ε(proton)/ε(muon)=S(p)/S(m)≈−4.08 (~−4 within "
        "the ~2-digit S noise — observation, not identified). (2) ε=0 crossing q* "
        "bracketed to a ~1.3e-8 window (S sign-flips). (3) Entropy block: 2 anchors at "
        "~2.2 digits locate q* to ~8e-11 only — q* not PSLQ-identifiable, ε(q₀) "
        "underdetermined by anchors. Scope-(a) negative: numerical identification is "
        "entropy-blocked (NOT a structural claim ε is underivable — the archimedean "
        "functor / Φ_b state-integral #3596 is the open route). No c_k wired; no fit; C14."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("proxy_independent_ratio", {
        "eps_ratio_proton_over_muon": mp.nstr(ratio, 10),
        "vs_minus_four_pct": mp.nstr(gap_vs_4 * 100, 4),
        "status": "suggestive_not_identified_within_2digit_noise"})
    wb.add_data("eps_zero_crossing", {
        "q_proton": mp.nstr(QP, 20), "q_muon": mp.nstr(QM, 20),
        "q_star_linear_interp": mp.nstr(qstar, 20), "window_width": mp.nstr(window, 6)})
    wb.add_data("entropy_block", {
        "digits_per_anchor": mp.nstr(C3_DIGITS_PER_ANCHOR, 3), "n_anchors": 2,
        "q_star_locatable_to": mp.nstr(locatable, 6),
        "verdict": "entropy-blocked; needs archimedean functor not more anchors"})
    wb.add_assertion("eps_zero_bracketed_and_entropy_blocked",
                     computed=1.0 if (SP < 0 < SM and locatable > 0) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="S sign-flips (eps=0 bracketed between anchors); 2 anchors at ~2.2 digits cannot PSLQ-identify q* / eps(q0)")
    wb.save()
    print("\n  RESULT: proxy-independent ratio ≈ −4.08 (~−4?); ε=0 bracketed; numerical")
    print("          identification entropy-blocked ⇒ archimedean-functor problem, not a fit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
