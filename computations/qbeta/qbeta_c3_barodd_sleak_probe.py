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

import json
from pathlib import Path

_WITNESS = (Path(__file__).resolve().parent
            / "qbeta-c3-keystone-anchor-blind.witness.json")


def main() -> None:
    r = json.loads(_WITNESS.read_text(encoding="utf-8"))["result"]
    vol = float(r["Vol_4_1"])
    c3 = {"muon": float(r["c3_muon"]), "proton": float(r["c3_proton"])}
    claim = {"muon": float(r["claim_muon"]), "proton": float(r["claim_proton"])}

    print(f"Vol(4₁) = {vol:.8f}  (bar-EVEN part of c₃, = −Vol(4₁); solved, anchor-stable)\n")
    S = {a: c3[a] + vol for a in c3}              # bar-ODD S-leak
    claimS = {a: claim[a] + vol for a in claim}   # claim formula's odd part
    print("bar-ODD S-leak  S = c₃ + Vol(4₁):")
    for a in ("muon", "proton"):
        print(f"  {a:7s}: c₃ = {c3[a]:+.8f}   S = {S[a]:+.8f}   (claim odd part {claimS[a]:+.8f})")

    print(f"\n  S sign-flips (HARD, two measured values): "
          f"S(muon) {S['muon']:+.6f} > 0 > {S['proton']:+.6f} = S(proton)")
    # Zero-crossing is an INFERENCE: IF S(q₀) is continuous (IVT), a zero exists
    # between the anchors; the fraction below is a LINEAR-interpolation estimate
    # of its location, not a computed q*.
    frac = S["muon"] / (S["muon"] - S["proton"])
    print(f"  ⇒ if S(q₀) is continuous, S has a zero between the anchors")
    print(f"    (~{frac*100:.1f}% along muon→proton under LINEAR S-interpolation) — a q*")
    print(f"     where c₃ = −Vol(4₁) exactly (purely bar-even)")
    print(f"  S(proton)/S(muon) = {S['proton']/S['muon']:+.4f}")
    print(f"  claim odd part is fixed (+{claimS['muon']:.5f}) — anchor-blind, CANNOT sign-flip.")

    print("\nDiagnosis: bar-EVEN −Vol(4₁) is the compact-Φ_q / real MASS face")
    print("(T1, this session's QOU.MathlibExt.QuantumDilogarithm backbone).")
    print("The bar-ODD S is the Φ_b modular-double / DECAY face (T3, deferred) —")
    print("its sign-flip + zero-crossing is a Φ_b fingerprint, not a compact-Φ_q formula.")


if __name__ == "__main__":
    main()
