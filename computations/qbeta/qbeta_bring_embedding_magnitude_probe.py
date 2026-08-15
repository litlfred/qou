#!/usr/bin/env python3
"""qbeta_bring_embedding_magnitude_probe.py — does a Bring-genus-4 period / X5
weight of the w²(4₁) vs w³(Borromean) embeddings, EVALUATED AT q₀, reproduce the
S-channel magnitude |S_proton/S_muon| ≈ 4.075?

Owner method redirect (2026-08-01), sharpened: *"we should be doing ALL geom
embedded in Bring's and EVALUATED AT q_0."* The [W] winding-lattice probe split
one geometry into two mismatched quadratic orders — geodesic on the cusp torus
(ℤ[√3], disc-12) for the winding, disc-5 golden parity grafted on for the sign.
The sign came out clean (2/2, `qbeta_disc5_parity_probe`) but the MAGNITUDE
MISSED, and cusp-lattice ratio-matching is a fit trap ([D4]: 1833 chance pairs).
Redirect: embed the WHOLE geometry into Bring's genus-4 curve (whose intrinsic
automorphism structure IS the disc-5 golden order) and let the `4.075` magnitude
fall out of a Bring period / X5-weight ratio of the w² vs w³ embeddings, EVALUATED
at the substrate modulus q₀ ≈ 1.10998 — NOT a cusp-lattice G-value.

This probe is derive-then-check with NO tuning. It (a) pins down what the observed
`4.075` actually IS, (b) computes EVERY natural forced Bring-intrinsic-at-q₀ period
/ weight ratio and reports each miss transparently (anti-cherry-pick), and (c)
identifies the structural obstruction the route hits.

RESULT PREVIEW (honest negative — a WIN per the discipline):
  * The observed magnitude is NOT a period. It is the anchor-offset ratio
        |S_p/S_m| = |(q_p − q*)/(q_m − q*)|,   q* = the S-channel zero crossing,
    verified to 6 digits ([A1]). S straddles a near-zero over the ~1.3e-8 q gap
    between the muon-pin and proton-pin anchors (dS/dq ≈ 3.8e6, hypersensitive):
    the muon anchor sits 2.5e-9 ABOVE q*, the proton anchor 1.0e-8 BELOW it, and
    4.075 = 1.0e-8 / 2.5e-9. This is q-ANCHOR ARITHMETIC (where the two pins fall
    relative to the S-root), not a knot-embedding period.
  * NO forced Bring-genus-4 period is pinned to the w²/w³ embeddings ([A2]):
    - the X5/Z5 weight is CATEGORICAL, unit-modulus — `x5-bring-weight-geometric-
      content.md`: "categorical, not a morphism of curves … U(1) phase tube".
      |ζ₅⁻³|/|ζ₅⁻²| = 1. A phase, structurally not a magnitude.
    - the SW periods `a_D^{(n)}` (`sw-period-residue-sum.lean`,
      `jet-sw-tau-decomposition.lean`) are ABSTRACT ℂ-valued fields with no
      numeric realisation, and jet degree n is a Reeb/vertical order, NOT the
      braid winding power.
    - the only FORCED numeric period of these two knots is the hyperbolic complex
      volume Vol(4₁)=2·Cl₂(π/3), Vol(Bor)=8G; its ratio 3.610 is q₀-independent and
      misses 4.075 by 11.4% ([A3]).
  * STRUCTURAL WALL ([A4]): a period "evaluated at q₀" is by construction a SMOOTH
    function of q₀; between the two anchors (Δq ≈ 1.3e-8) any smooth q₀-period
    changes by O(1e-9) — a factor ≈ 1, never 4.075. So "all-Bring, evaluated at
    q₀" cannot produce this magnitude; the magnitude lives in the near-zero-
    crossing structure of S (a property of the c₃/Vol₄₁ function's root location
    vs the anchors), not in any q₀-evaluated period. This is the SP1 smoothness
    wall restated in the Bring frame.

Assertions are the FACTS (offset-ratio identity, unit-modulus X5 weight, forced-
volume miss, smooth-period-at-both-anchors ≈ 1). NOTHING is asserted to equal
4.075 — no period is adopted, no instance fabricated, no c_k wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(60):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))       # Vol(4₁) = 2·Cl₂(π/3), forced period
    VOL_BOR = +(8 * mp.catalan)                  # Vol(Borromean) = 8G, forced period

# canonical braid words (corpus `fundamental-knots-operator-basis`,
# `winding-parity-sign-transport`): powers of w = σ₁σ₂⁻¹.
#   muon  ↔ 4₁       = w²  (winding n = 2)
#   proton↔ Borromean L6a4 = w³  (winding n = 3)
N_MUON, N_PROTON = 2, 3
PERSUASIVE = mp.mpf("0.1")   # % miss below which a match would be evidential


def S(q):
    """The S-channel quantity of the redirect: c₃-target shifted by Vol(4₁)."""
    return c3_target_at(q, QCOD, ME) + VOL41


def main() -> int:
    print("=" * 80)
    print(" BRING-EMBEDDING MAGNITUDE: is |S_p/S_m|≈4.075 a q₀-evaluated Bring period?")
    print("=" * 80)

    q_pr, q_mu = q_at(60), q_muon_at(60)
    S_mu, S_pr = S(q_mu), S(q_pr)
    obs = abs(S_pr / S_mu)
    lnq0 = mp.log(q_pr)
    hbar_q = (q_pr - 1) / q_pr
    print(f"\n substrate: q₀(proton) = {mp.nstr(q_pr,16)}   ln q₀ = {mp.nstr(lnq0,10)}")
    print(f"            q₀(muon)   = {mp.nstr(q_mu,16)}   ℏ_q  = {mp.nstr(hbar_q,10)}")
    print(f"            q-gap = {mp.nstr(q_pr-q_mu,6)} (rel {mp.nstr(abs(q_pr-q_mu)/q_pr,4)})")
    print(f" observed:  S_muon = {mp.nstr(S_mu,9)} (+)   S_proton = {mp.nstr(S_pr,9)} (−)")
    print(f"            |S_proton/S_muon| = {mp.nstr(obs,12)}   ← the magnitude to explain")

    # ---- [A1] the magnitude IS the anchor-offset ratio near the S-zero --------
    print("\n [A1] what the magnitude actually IS: the anchor-offset ratio near S=0")
    dSdq = (S_pr - S_mu) / (q_pr - q_mu)
    q_star = mp.findroot(S, (q_pr + q_mu) / 2)     # the S-channel zero crossing
    off_ratio = (q_pr - q_star) / (q_mu - q_star)
    a1_resid = abs(S_pr / S_mu - off_ratio) / abs(S_pr / S_mu)
    print(f"      dS/dq ≈ {mp.nstr(dSdq,6)}  (hypersensitive: the ~1e-8 q-gap is amplified)")
    print(f"      S-zero crossing  q* = {mp.nstr(q_star,16)}")
    print(f"        muon anchor is {mp.nstr(q_mu-q_star,5)} from q* (ABOVE, S>0)")
    print(f"        proton anchor is {mp.nstr(q_pr-q_star,5)} from q* (BELOW, S<0)")
    print(f"      (q_p−q*)/(q_m−q*) = {mp.nstr(off_ratio,12)}   vs  S_p/S_m = {mp.nstr(S_pr/S_mu,12)}")
    print(f"      ⇒ magnitude = ratio of anchor offsets from the S-root; residual {mp.nstr(a1_resid,4)}")
    print("        (nonzero only through the tiny local curvature of S). This is q-ANCHOR")
    print("        arithmetic — where the two pins fall vs the S-root — NOT a Bring period.")
    a1 = a1_resid < mp.mpf("1e-5")

    # ---- [A2] the X5 / Z5 weight is a unit-modulus phase, not a magnitude -----
    print("\n [A2] X5 / Z5 weight of the embeddings is CATEGORICAL (unit-modulus phase)")
    zeta5 = mp.e ** (2j * mp.pi / 5)
    w_mu = abs(zeta5 ** (-N_MUON))       # |ζ₅⁻²|
    w_pr = abs(zeta5 ** (-N_PROTON))     # |ζ₅⁻³|
    x5_ratio = w_pr / w_mu
    print(f"      |ζ₅^-2| = {mp.nstr(w_mu,6)}   |ζ₅^-3| = {mp.nstr(w_pr,6)}   ratio = {mp.nstr(x5_ratio,6)}")
    print("      corpus (`x5-bring-weight-geometric-content.md`): the identification x^k↦w₁^k is")
    print("      \"categorical, not a morphism of curves … a single U(1) phase tube\". A phase")
    print("      has unit modulus ⇒ the X5 weight ratio is 1, structurally NOT a magnitude source.")
    a2 = abs(x5_ratio - 1) < mp.mpf("1e-40")

    # ---- [A3] the only FORCED numeric period: hyperbolic volume — misses ------
    print("\n [A3] forced Bring-intrinsic-at-q₀ period / weight battery (report ALL, no cherry-pick)")
    rho0 = lnq0                                  # substrate boost rapidity = ln q₀
    rho5 = mp.log((1 + mp.sqrt(5)) / 2)          # golden fundamental rapidity = ln φ
    phi = (1 + mp.sqrt(5)) / 2

    def rr(v):   # % miss vs the observed magnitude
        return abs(v - obs) / obs * 100

    candidates = {
        # -- the only genuinely FORCED numeric period of these two knots --------
        "Vol(Bor)/Vol(4₁) = 8G / 2·Cl₂(π/3)  [forced, q₀-indep]": VOL_BOR / VOL41,
        "mass ratio m(Bor)/m(4₁) [= Vol ratio; ρ,ℏ_q cancel]": VOL_BOR / VOL41,
        # -- X5 categorical weight (unit modulus) ------------------------------
        "|ζ₅^-3| / |ζ₅^-2|  [X5 phase, U(1)]": x5_ratio,
        # -- golden boost EVALUATED AT q₀ (rapidity ln q₀), w³ vs w² ------------
        "sinh(3·ln q₀)/sinh(2·ln q₀)": mp.sinh(3 * rho0) / mp.sinh(2 * rho0),
        "cosh(3·ln q₀)/cosh(2·ln q₀)": mp.cosh(3 * rho0) / mp.cosh(2 * rho0),
        "q₀³ / q₀² = q₀  [pure boost, evaluated at q₀]": q_pr,
        # -- golden fundamental-rapidity boosts (ln φ), w³ vs w² ---------------
        "sinh(3·lnφ)/sinh(2·lnφ)": mp.sinh(3 * rho5) / mp.sinh(2 * rho5),
        "cosh(3·lnφ)/cosh(2·lnφ)": mp.cosh(3 * rho5) / mp.cosh(2 * rho5),
        "φ³ / φ² = φ  [golden unit boost]": phi,
        "φ³  [golden, n=3]": phi ** 3,
        # -- Lucas / Fibonacci (golden bar-split integer sequences) ------------
        "L₃/L₂ = 4/3  [golden barEven]": mp.mpf(4) / 3,
        "F₃·√5 / (F₂·√5) = 2  [golden barOdd]": mp.mpf(2),
    }
    best_k, best_m = None, None
    for k, v in candidates.items():
        m = rr(v)
        tag = "  ← FORCED period" if k.startswith("Vol(Bor)") else ""
        print(f"      {k:52s} = {mp.nstr(v,8):>10}  miss {mp.nstr(m,4):>7}%{tag}")
        if best_m is None or m < best_m:
            best_k, best_m = k, m
    print(f"      best of battery: {best_k}  at {mp.nstr(best_m,4)}%  (≫ {mp.nstr(PERSUASIVE,2)}% persuasive)")
    print("      the one FORCED numeric period (hyperbolic volume ratio 3.610) misses by 11.4%;")
    print("      every q₀-evaluated boost candidate sits at ~1.0–1.5 (small rapidity ln q₀≈0.104).")
    a3 = best_m > PERSUASIVE      # nothing lands near the evidential threshold

    # ---- [A4] the structural wall: a q₀-period is ≈ identical at both anchors --
    print("\n [A4] structural wall — a q₀-EVALUATED period is smooth ⇒ ≈ identical at both anchors")
    # take a representative smooth q₀-period (the golden boost) and evaluate the
    # SAME w³/w² datum at each anchor: the two values differ by O(1e-9), not ×4.
    def boost_ratio(q):
        r = mp.log(q)
        return mp.sinh(3 * r) / mp.sinh(2 * r)
    p_mu, p_pr = boost_ratio(q_mu), boost_ratio(q_pr)
    anchor_spread = abs(p_pr - p_mu) / abs(p_mu)
    print(f"      period(w³/w²) at muon q₀  = {mp.nstr(p_mu,14)}")
    print(f"      period(w³/w²) at proton q₀= {mp.nstr(p_pr,14)}")
    print(f"      relative spread across the two anchors = {mp.nstr(anchor_spread,4)}  (≈ 1e-9)")
    print("      A smooth q₀-period changes by ~1e-9 between the pins, i.e. a factor ≈ 1 — it")
    print("      CANNOT produce a factor 4.075. The magnitude requires the near-zero crossing")
    print("      of S ([A1]), which is where the anchors fall vs the S-root, not a period.")
    print("      (This is the SP1 smoothness wall of the coordination doc, restated on Bring.)")
    a4 = anchor_spread < mp.mpf("1e-6")

    # ---- verdict --------------------------------------------------------------
    print("\n" + "=" * 80)
    print(" VERDICT: honest NEGATIVE (a WIN). The owner's Bring-embedding route, taken")
    print(" literally, does not resolve the magnitude — and the probe shows WHY:")
    print("   • 4.075 is the anchor-offset ratio near an S-zero (q-anchor arithmetic), not")
    print("     a period [A1].")
    print("   • The corpus pins NO unique q₀-evaluated Bring period to the w²/w³ embeddings:")
    print("     X5 weight is a U(1) phase [A2]; SW periods are abstract & uncomputed and jet")
    print("     degree ≠ winding power; the sole forced numeric period (hyperbolic volume)")
    print("     misses 11.4% [A3].")
    print("   • Any q₀-evaluated period is smooth ⇒ ≈ identical at the two anchors [A4]; it")
    print("     structurally cannot be a factor-4 hypersensitive ratio.")
    print(" No period adopted, no instance fabricated, no c_k wired. Magnitude stays OPEN.")
    print("=" * 80)

    wb = WitnessBuilder("qbeta-bring-embedding-magnitude", engine="mpmath")
    wb.set_description(
        "Bring-embedding magnitude probe (#4473 redirect, owner 2026-08-01, sharpened "
        "'all geom embedded in Bring's and EVALUATED AT q₀'): does a Bring-genus-4 period / "
        "X5 weight of the w²(4₁, muon) vs w³(Borromean, proton) embeddings, evaluated at the "
        "substrate q₀≈1.10998, reproduce |S_proton/S_muon|≈4.075? HONEST NEGATIVE (a win). "
        "[A1] The observed magnitude is the anchor-offset ratio |(q_p−q*)/(q_m−q*)| where q* "
        "is the S-channel zero crossing (verified to 6 digits): S is hypersensitive (dS/dq≈3.8e6) "
        "and straddles a near-zero over the ~1.3e-8 muon-pin↔proton-pin q-gap — the muon anchor "
        "sits 2.5e-9 above q*, the proton 1.0e-8 below, and 4.075=1.0e-8/2.5e-9. This is q-anchor "
        "arithmetic, NOT a knot-embedding period. [A2] The X5/Z5 weight is categorical/unit-modulus "
        "('categorical, not a morphism of curves … U(1) phase tube', x5-bring-weight-geometric-"
        "content.md): |ζ₅⁻³|/|ζ₅⁻²|=1, a phase not a magnitude. [A3] The SW periods a_D^(n) "
        "(sw-period-residue-sum.lean, jet-sw-tau-decomposition.lean) are abstract ℂ fields with no "
        "numeric realisation and jet degree≠winding power; the only FORCED numeric period of the two "
        "knots is the hyperbolic complex volume ratio 8G/(2·Cl₂(π/3))=3.610, q₀-independent, missing 4.075 "
        "by 11.4%; every q₀-evaluated boost candidate (sinh/cosh at ln q₀ or ln φ, φ^n, Lucas/Fib) "
        "misses by ≫0.1%. [A4] Structural wall: a q₀-evaluated period is smooth ⇒ its w³/w² value is "
        "identical at the two anchors to ~1e-9 (a factor≈1), so it cannot be a factor-4 hypersensitive "
        "ratio — the magnitude lives in the S near-zero crossing, not in any period (SP1 smoothness "
        "wall restated on Bring). No period adopted, no instance fabricated, no c_k wired; magnitude OPEN.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("bring_embedding_magnitude_readout", {
        "observed_magnitude": mp.nstr(obs, 12),
        "anchor_offset_ratio_identity": (
            f"|S_p/S_m|={mp.nstr(obs,10)} = |(q_p−q*)/(q_m−q*)|={mp.nstr(abs(off_ratio),10)}; "
            f"q*={mp.nstr(q_star,16)} the S-zero; residual {mp.nstr(a1_resid,4)} (local curvature)"),
        "dS_dq_hypersensitivity": mp.nstr(dSdq, 6),
        "x5_weight_ratio": f"|ζ₅⁻³|/|ζ₅⁻²| = {mp.nstr(x5_ratio,6)} (categorical U(1) phase, not a magnitude)",
        "forced_volume_period_ratio": f"8G/(2·Cl₂(π/3)) = {mp.nstr(VOL_BOR/VOL41,10)} (misses 4.075 by {mp.nstr(rr(VOL_BOR/VOL41),4)}%)",
        "best_candidate_miss": f"{best_k} at {mp.nstr(best_m,4)}%",
        "smooth_period_anchor_spread": f"{mp.nstr(anchor_spread,4)} (≈1e-9; a q₀-period is ≈identical at both pins)",
        "sw_periods_status": "abstract ℂ fields (sw-period-residue-sum.lean); no numeric realisation; jet degree ≠ braid winding power",
        "verdict": (
            "HONEST NEGATIVE: the magnitude is an anchor-offset ratio near an S-zero (q-anchor "
            "arithmetic), not a Bring period; the corpus pins no unique q₀-evaluated Bring period to "
            "the w²/w³ embeddings (X5 weight is a U(1) phase, SW periods abstract, only-forced volume "
            "ratio misses 11.4%); and any smooth q₀-period is ≈identical at the two anchors so cannot "
            "supply a factor-4 hypersensitive ratio. Magnitude OPEN; nothing adopted or wired."),
        "missing_to_pin_a_period": (
            "a canonical HOMOLOGY CLASS / cycle on Bring's genus-4 Jacobian for each of w²(4₁) and "
            "w³(Borromean) — the corpus only guarantees EXISTENCE of the embedding via the genus bound "
            "g(K)≤4 (embeddability-closure.lean), not a specific period-carrying cycle; and a numeric "
            "realisation of the abstract SW periods a_D^(n). Without these, any period ratio requires a "
            "FREE choice of cycle/winding — the dense-fit resource the [D4] discipline forbids."),
    })
    wb.add_assertion("magnitude_is_anchor_offset_ratio_not_period", str(bool(a1)), "True")
    wb.add_assertion("x5_weight_is_unit_modulus_phase", str(bool(a2)), "True")
    wb.add_assertion("forced_volume_period_misses_gt_0p1pct", str(bool(a3)), "True")
    wb.add_assertion("smooth_q0_period_identical_at_both_anchors", str(bool(a4)), "True")
    wb.save()
    print("\nwitness → qbeta-bring-embedding-magnitude.witness.json")
    ok = all([a1, a2, a3, a4])
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
