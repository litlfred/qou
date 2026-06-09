#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only astrophysical identification probe.
"""
φ-rung ↔ hyperon-onset identification under the shallow (Map C) q↔ρ map.

The q↔ρ calibration (`metallic_q_rho_calibration.py`) showed the golden
rung φ landing at 2.4–5.1 ρ₀ under the coral-tube map — the same band
where Λ hyperons appear in standard neutron-star physics ("hyperon
puzzle" literature: onset 2–3 ρ₀ with ΛN forces only; chiral models
span 1.9 ρ₀ to > 5 ρ₀) and where the corpus's own layered table puts
the hyperonic outer core.

Structure exploited here: under the power-law map q(ρ) = q₀(ρ/ρ₀)^α
anchored at q(ρ_c) = δ_silver, the RATIOS between rung densities are
anchor-independent:

    ρ_φ  = ρ_c^β,    β = ln(φ/q₀)  / ln(δ_silver/q₀) ≈ 0.485
    ρ_φ² = ρ_c^γ,    γ = ln(φ²/q₀) / ln(δ_silver/q₀) ≈ 1.104

So IDENTIFYING the φ rung with the hyperon onset pins the whole ladder:
ρ_onset → ρ_c (silver, the CFL / second-burst density) → ρ_φ² (gCFL
candidate) → |c_r| (the coral-tube scale that must produce this ρ_c).
The probe inverts the chain at onset = 2.0 / 2.5 / 3.0 ρ₀ and asks
whether the implied |c_r| is consistent with the corpus's coral-tube
transverse scale (~ proton radius … 1 fm).

No fitting: a one-parameter identification inverted against a
literature window, every other number derived.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

from metallic_q_rho_calibration import (
    PHI, Q0, RHO_0_FM3, RHO_0_GCM3, delta_n,
)

mp.mp.dps = 50
HERE = Path(__file__).parent

DELTA_S = delta_n(2)
SPACING_0 = RHO_0_FM3 ** mp.mpf("-1/3")  # inter-baryon spacing at ρ₀ [fm]

BETA = mp.log(PHI / Q0) / mp.log(DELTA_S / Q0)
GAMMA = mp.log(PHI * PHI / Q0) / mp.log(DELTA_S / Q0)

# literature window for Λ onset (see audit doc for sources)
ONSET_GRID = [mp.mpf("2.0"), mp.mpf("2.5"), mp.mpf("3.0")]
ONSET_WINDOW = ("1.9", "3.5")  # chiral-model span, ρ₀ units


def chain_from_onset(rho_phi: mp.mpf) -> dict:
    rho_c = rho_phi ** (1 / BETA)              # silver rung
    rho_phi2 = rho_c ** GAMMA                  # φ² rung
    c_r = SPACING_0 / rho_c ** mp.mpf("1/3")   # implied tube scale
    return {
        "phi_rung_rho0": mp.nstr(rho_phi, 6),
        "silver_rho0": mp.nstr(rho_c, 6),
        "phi2_rho0": mp.nstr(rho_phi2, 6),
        "silver_gcm3": mp.nstr(rho_c * RHO_0_GCM3, 5),
        "implied_c_r_fm": mp.nstr(c_r, 6),
    }


def main() -> None:
    rows = [chain_from_onset(x) for x in ONSET_GRID]

    # consistency checks (assertions, not fits)
    c_rs = [mp.mpf(r["implied_c_r_fm"]) for r in rows]
    assert all(mp.mpf("0.5") < c < mp.mpf("1.5") for c in c_rs), \
        "implied tube scale outside the fermi-scale sanity band"
    silvers = [mp.mpf(r["silver_rho0"]) for r in rows]
    assert all(mp.mpf(4) < v < mp.mpf(10) for v in silvers), \
        "silver placement left the proto-NS band unexpectedly"

    witness = {
        "description": (
            "φ-rung ↔ hyperon-onset identification under the Map C "
            "power-law q↔ρ map: anchor-independent rung-ratio "
            "exponents β (φ) and γ (φ²) relative to the silver anchor; "
            "the Λ-onset window 2–3 ρ₀ pins the coral-tube scale to "
            "|c_r| ≈ 0.87–1.14 fm (fermi-scale, bracketing 1 fm) and "
            "DERIVES silver at ≈ 4.2–9.6 ρ₀ (just above the heaviest "
            "known-pulsar central densities — proto-NS / second-burst "
            "territory) and φ² at ≈ 4.8–12.2 ρ₀."
        ),
        "computed_at": datetime.now(timezone.utc).isoformat(),
        "script": "metallic_phi_rung_hyperon_onset.py",
        "exponents": {
            "beta_phi": mp.nstr(BETA, 10),
            "gamma_phi2": mp.nstr(GAMMA, 10),
            "note": (
                "ρ_φ = ρ_c^β and ρ_φ² = ρ_c^γ hold for ANY anchor of "
                "the power-law map — the identification transfers the "
                "hyperon onset into a prediction of the silver and φ² "
                "densities with no extra freedom"
            ),
        },
        "lambda_onset_window_rho0": ONSET_WINDOW,
        "chains": rows,
        "consistency": {
            "implied_c_r_fermi_scale": True,
            "corpus_layered_table": (
                "conj:color-superconductivity-borromean places the "
                "hyperonic layer at ρ₀–2ρ₀ — adjacent to (slightly "
                "below) the literature onset; the φ-rung identification "
                "sits at the literature window, i.e. the corpus table's "
                "upper edge"
            ),
            "nicer_gate": (
                "derived silver 4.2–9.6 ρ₀ is ABOVE the inferred "
                "central densities of all known pulsars (≤ ~4 ρ₀ at "
                "68%) — no kink in current stars, second burst only in "
                "the heaviest proto-NS: consistent with both "
                "non-detections"
            ),
        },
        "limitations": [
            "identification probe: assumes the Map C power-law form "
            "and that the φ rung IS the hyperon onset; both are "
            "hypotheses, not corpus theorems",
            "Λ-onset window is model-dependent (1.9 ρ₀ to >5 ρ₀ across "
            "chiral parameterizations); grid 2.0/2.5/3.0 spans the "
            "standard ΛN-only band",
        ],
    }
    out = HERE / "metallic-phi-rung-hyperon-onset.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"Saved witness: {out}", file=sys.stderr)

    print(f"β(φ)={mp.nstr(BETA,6)}  γ(φ²)={mp.nstr(GAMMA,6)}")
    for x, r in zip(ONSET_GRID, rows):
        print(f"  onset {mp.nstr(x,3)} ρ0 → silver {r['silver_rho0']} ρ0, "
              f"φ² {r['phi2_rho0']} ρ0, |c_r| {r['implied_c_r_fm']} fm")


if __name__ == "__main__":
    main()
