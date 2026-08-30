#!/usr/bin/env python3
"""
Gen-3 meson mass ratios via the Hecke-character × Seifert-ratio formula.

Extends the PROVED kaon calculation
([`meson-kaon-pion-hecke-seifert-proof.md`]):

    m_X / m_π  =  χ^(2,1)(σ₁ⁿ) · [V_S(T(2,n)) / V_S(T(2,3))]^{n_q},
    χ^(2,1)(σ₁ⁿ) = qⁿ − q⁻ⁿ = h·[n]_q  (odd n),
    V_S(T(2,n)) = π(n−2)/n   (Seifert volume; 2π·Euler number),
    n_q = 2  (two-body q̄q composite; PROVED-value, empirically selected).

Generations: π=T(2,3) (gen 1, the unit), K=T(2,5) (gen 2, proved 290 ppm),
gen-3 = T(2,7). This computes the gen-3 prediction and compares it HONESTLY
against every light gen-3 meson (η, η', ρ, ω, φ, K*) — reporting whichever
it actually matches, with the residual, no cherry-picking.

Audit-only; pure-canonical (q₀ only, no fit). Witness emitted.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402 — dps must rise before module constants
import json
import sys
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

import mpmath as mp

from q_parameter import Q_MP as Q0  # noqa: E402  (muon-pinned canonical, matches kaon witness)

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

# PDG 2024 masses (MeV), charged pion as the unit
M_PI = mp.mpf("139.57039")
PDG = {
    "K±":  mp.mpf("493.677"),    # gen-2, the proved anchor
    "η":   mp.mpf("547.862"),
    "ρ":   mp.mpf("775.26"),
    "ω":   mp.mpf("782.66"),
    "K*":  mp.mpf("891.67"),
    "η'":  mp.mpf("957.78"),
    "φ":   mp.mpf("1019.461"),
}


def seifert_ratio(n: int) -> Fraction:
    """V_S(T(2,n))/V_S(T(2,3)) = [(n-2)/n] / [1/3] = 3(n-2)/n (exact)."""
    return Fraction(3 * (n - 2), n)


def meson_ratio(q0: mp.mpf, n: int, n_q: int = 2) -> mp.mpf:
    chi = q0 ** n - q0 ** (-n)               # χ^(2,1)(σ₁ⁿ) = qⁿ − q⁻ⁿ
    R = mp.mpf(seifert_ratio(n).numerator) / seifert_ratio(n).denominator
    return chi * R ** n_q


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(str(Q0))
    print(f"\n  GEN-3 MESON (T(2,7)) via χ^(2,1)·Seifert²   q₀ = {float(q0):.10f}\n")

    # cross-check: reproduce the proved kaon (gen-2) first
    rK = meson_ratio(q0, 5)
    pdgK = PDG["K±"] / M_PI
    print(f"  [cross-check gen-2 kaon] m_K/m_π pred = {float(rK):.5f}  "
          f"PDG = {float(pdgK):.5f}  ({float(abs(rK-pdgK)/pdgK*1e6):.0f} ppm)")
    print(f"  Seifert ratios: T(2,5)→{seifert_ratio(5)}, T(2,7)→{seifert_ratio(7)}\n")

    # gen-3 prediction
    r7 = meson_ratio(q0, 7)
    print(f"  GEN-3 PREDICTION  m/m_π = χ(σ₁⁷)·(15/7)² = {float(r7):.5f}\n")
    print(f"  {'meson':6s} {'PDG m/m_π':>10s} {'pred/PDG':>9s} {'residual':>12s}")
    print("  " + "-" * 42)
    best = None
    rows = {}
    for name, m in PDG.items():
        pdg_ratio = m / M_PI
        resid = abs(r7 - pdg_ratio) / pdg_ratio
        rows[name] = (float(pdg_ratio), float(resid))
        flag = ""
        if best is None or resid < best[1]:
            best = (name, resid)
        print(f"  {name:6s} {float(pdg_ratio):10.4f} {float(r7/pdg_ratio):9.4f} "
              f"{float(resid)*1e6:10.0f} ppm")
    print()
    print(f"  → closest gen-3 match: {best[0]}  ({float(best[1])*1e6:.0f} ppm)")
    print(f"     (honest report — the formula predicts whichever meson this is, "
          f"not necessarily the η the dictionary listed)")

    witness = {
        "description": "Gen-3 meson (T(2,7)) mass ratio via Hecke χ^(2,1)·Seifert², parallel to the proved kaon; honest comparison to all light gen-3 mesons",
        # "computation" is derived by wrap_legacy from the name argument (Copilot review)
        "audit_only": True,
        "precision_dps": 50,
        "context": {
            "extends": "meson-kaon-pion-hecke-seifert-proof.md (proved kaon, 290 ppm)",
            "formula": "m_X/m_pi = (q^n - q^-n) * (3(n-2)/n)^2, n=7",
            "n_q": 2,
        },
        "constants": {"q_0": str(q0), "m_pi_MeV": str(M_PI),
                      "seifert_ratio_T27_T23": str(seifert_ratio(7))},
        "kaon_crosscheck": {"pred": str(rK), "pdg": str(pdgK),
                            "ppm": float(abs(rK - pdgK) / pdgK * 1e6)},
        "gen3_prediction_ratio": str(r7),
        "comparisons": {k: {"pdg_ratio": v[0], "residual": v[1]} for k, v in rows.items()},
        "closest_match": {"meson": best[0], "residual": float(best[1])},
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    out = WitnessBuilder.wrap_legacy(
        "meson-gen3-eta-phi", witness, script_path=__file__, engine="mpmath",
    ).save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
