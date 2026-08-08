#!/usr/bin/env python3
"""
qbeta_c3_barodd_sleak_probe.py — extract the bar-ODD S-leak of c₃ at both
anchors, and characterize it as the precise open target.

c₃ splits (parity-chirality dictionary, PR #3474/#3487) into a solved bar-EVEN
part `−Vol(4₁)` (real, amphichiral 4₁ face) and an anchor-swinging bar-ODD part
`S = c₃ + Vol(4₁)` (the CAL-2 S-leak, Subgoal-2). This probe reports S at the
muon and proton anchors from the committed anchor-blind witness, and shows S
*sign-flips* between two q₀>1 anchors ⇒ it crosses zero (a substrate value where
c₃ is purely bar-even). The anchor-blind claim formula's odd part is a *fixed*
positive constant, so it structurally cannot reproduce the flip.

This is a MEASUREMENT, not a fit or a c_k proposal (registry untouched; no
wiring; flip-flop guard §8 respected). It hands any future Φ_b (modular-double,
bar-odd decay face) derivation the exact numbers it must reproduce.

Companion audit: docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md.
Source: computations/qbeta/qbeta-c3-keystone-anchor-blind.witness.json.
"""
from __future__ import annotations

import sys
import pathlib
from pathlib import Path

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401, E402

import json  # noqa: E402

from mpmath import mp, mpf  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

_WITNESS = (Path(__file__).resolve().parent
            / "qbeta-c3-keystone-anchor-blind.witness.json")

# The upstream anchor-blind witness stores these as 12-significant-digit
# STRINGS from an mpmath+sympy computation. This probe used to `float()` them,
# print 8 digits, and emit no witness at all — so every consumer of S_muon /
# S_proton (qbeta_t4_stokes3_crux_probe, qbeta_braid_nf_sdp_offset_probe, the
# Ohtsuki rung script, and several Lean docstrings) hand-copied a 6-digit
# truncation of a printout. There was no artifact to read instead. Bean
# qou-t0rf; the certificate flagged the copies as untraceable literals.
INPUT_SIG_DIGITS = 12


def main() -> None:
    set_compute_dps()
    r = json.loads(_WITNESS.read_text(encoding="utf-8"))["result"]
    vol = mpf(r["Vol_4_1"])
    c3 = {"muon": mpf(r["c3_muon"]), "proton": mpf(r["c3_proton"])}
    claim = {"muon": mpf(r["claim_muon"]), "proton": mpf(r["claim_proton"])}

    print(f"Vol(4₁) = {mp.nstr(vol, 12)}  (bar-EVEN part of c₃, "
          "= −Vol(4₁); solved, anchor-stable)\n")
    S = {a: c3[a] + vol for a in c3}              # bar-ODD S-leak
    claimS = {a: claim[a] + vol for a in claim}   # claim formula's odd part
    print("bar-ODD S-leak  S = c₃ + Vol(4₁):")
    for a in ("muon", "proton"):
        print(f"  {a:7s}: c₃ = {mp.nstr(c3[a], 12):>15}   "
              f"S = {mp.nstr(S[a], 9):>13}   "
              f"(claim odd part {mp.nstr(claimS[a], 9)})")

    print(f"\n  S sign-flips (HARD, two measured values): "
          f"S(muon) {mp.nstr(S['muon'], 6)} > 0 > "
          f"{mp.nstr(S['proton'], 6)} = S(proton)")
    # Zero-crossing is an INFERENCE: IF S(q₀) is continuous (IVT), a zero exists
    # between the anchors; the fraction below is a LINEAR-interpolation estimate
    # of its location, not a computed q*.
    frac = S["muon"] / (S["muon"] - S["proton"])
    print(f"  ⇒ if S(q₀) is continuous, S has a zero between the anchors")
    print(f"    (~{mp.nstr(frac * 100, 3)}% along muon→proton under "
          "LINEAR S-interpolation) — a q*")
    print(f"     where c₃ = −Vol(4₁) exactly (purely bar-even)")
    print(f"  S(proton)/S(muon) = {mp.nstr(S['proton'] / S['muon'], 5)}")
    print(f"  claim odd part is fixed ({mp.nstr(claimS['muon'], 6)}) — "
          "anchor-blind, CANNOT sign-flip.")

    print("\nDiagnosis: bar-EVEN −Vol(4₁) is the compact-Φ_q / real MASS face")
    print("(T1, this session's QOU.MathlibExt.QuantumDilogarithm backbone).")
    print("The bar-ODD S is the Φ_b modular-double / DECAY face (T3, deferred) —")
    print("its sign-flip + zero-crossing is a Φ_b fingerprint, not a compact-Φ_q formula.")

    # ── how many digits of S are real ────────────────────────────────────
    # S = c₃ + Vol(4₁) is a difference of two numbers that agree to their
    # first two digits (−2.0202… vs +2.0299…), so it is CATASTROPHIC
    # CANCELLATION and S carries fewer significant digits than its inputs.
    # Nobody downstream recorded that. With inputs good to
    # INPUT_SIG_DIGITS significant figures, the absolute error is
    # ~|c₃|·10^-(d-1), and S's relative error is that divided by |S|:
    #
    #     digits(S) ≈ INPUT_SIG_DIGITS − log10(|c₃| / |S|)
    #
    # ~2.3 decades of magnitude are lost at the muon anchor and ~1.7 at the
    # proton one, so 12-digit inputs yield ~9-10 digit S values — and the
    # literal `+0.00968298` that four consumers hand-copied is 6.
    sig = {}
    for a in ("muon", "proton"):
        lost = mp.log10(abs(c3[a]) / abs(S[a]))
        sig[a] = int(mp.floor(INPUT_SIG_DIGITS - lost))
    n_sig = min(sig.values())
    print(f"\nprecision: inputs carry {INPUT_SIG_DIGITS} sig digits; the "
          f"c₃ + Vol cancellation costs")
    print(f"  {mp.nstr(mp.log10(abs(c3['muon']) / abs(S['muon'])), 3)} decades "
          f"(muon) / "
          f"{mp.nstr(mp.log10(abs(c3['proton']) / abs(S['proton'])), 3)} "
          f"decades (proton), leaving {n_sig} — reported below.")

    wb = WitnessBuilder("qbeta-c3-barodd-sleak", engine="mpmath")
    wb.set_description(
        "CANONICAL SOURCE for the bar-odd S-leak anchor values "
        "S = c_3 + Vol(4_1), which QOU/QBeta/SLeakZeroCrossing.lean, "
        "MonodromyDatumRigidity.lean and CompleteStructureExclusion.lean cite "
        "and which at least four Python probes had hand-copied as bare "
        "6-digit literals. This probe previously emitted NO witness, so there "
        "was nothing to read instead — the copies were the only carrier. It "
        "also computed in float64 despite 12-digit string inputs. Both fixed: "
        "mpmath throughout, and the values are published here with the digit "
        "count the c_3 + Vol(4_1) cancellation actually supports. Derives "
        "nothing new; it is the same computation, sourced.")
    wb.add_data("upstream", str(_WITNESS.name))
    wb.add_data("Vol_4_1", mp.nstr(vol, INPUT_SIG_DIGITS))
    wb.add_data("c3", {a: mp.nstr(c3[a], INPUT_SIG_DIGITS) for a in c3})
    wb.add_data("S_leak", {a: mp.nstr(S[a], n_sig) for a in S})
    wb.add_data("S_leak_claim_odd_part",
                {a: mp.nstr(claimS[a], n_sig) for a in claimS})
    wb.add_data("precision", {
        "input_sig_digits": INPUT_SIG_DIGITS,
        "decades_lost_to_cancellation": {
            a: mp.nstr(mp.log10(abs(c3[a]) / abs(S[a])), 4)
            for a in c3},
        "reported_sig_digits": n_sig,
        "why": ("S = c_3 + Vol(4_1) subtracts two quantities agreeing to "
                "their first two digits, so S carries fewer significant "
                "figures than its inputs. Reporting S at the inputs' 12 "
                "digits would be fake precision; the 6-digit literal the "
                "consumers copied is the opposite error."),
    })
    wb.add_data("sign_flip", {
        "S_muon_positive": bool(S["muon"] > 0),
        "S_proton_negative": bool(S["proton"] < 0),
        "ratio_S_proton_over_S_muon": mp.nstr(S["proton"] / S["muon"], 6),
        "linear_interp_zero_fraction": mp.nstr(frac, 6),
        "scope": ("the zero-crossing is an INFERENCE from continuity (IVT), "
                  "and the fraction is a linear-interpolation estimate of its "
                  "location, not a computed q*"),
    })
    wb.add_assertion("S_sign_flips_across_anchors",
                     computed="1" if (S["muon"] > 0 > S["proton"]) else "0",
                     expected="1", tolerance="0.5",
                     source="S(muon) > 0 > S(proton) — two measured values, "
                            "the input to sleak_zero_between_anchors")
    wb.add_assertion("claim_odd_part_cannot_sign_flip",
                     computed="1" if (claimS["muon"] * claimS["proton"] > 0)
                              else "0",
                     expected="1", tolerance="0.5",
                     source="the claim formula's odd part is anchor-blind and "
                            "keeps one sign, which is what excludes it")
    out = wb.save()
    print(f"witness -> {out.name}")


if __name__ == "__main__":
    main()
