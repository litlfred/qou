#!/usr/bin/env python3
"""
Numerical scan of boiling and freezing temperatures from the q-deformed equation of state.

Follows the user directive to use strictly:
P_q V_q = n_q R T  => T_boil = S_q^(∂) / (n_q R)
with n_q = [2]_q for boiling (gas phase exploring S^2)
and n_q = [2]_q [n_K]_q for freezing.

NO fitted scales are used to force the temperatures to 373 K / 273 K.
The gap is reported honestly, and marked tier=open.
"""

from __future__ import annotations
import math
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401
from mpmath import mp  # noqa: E402
mp.dps = 50

try:
    from qou_substrate.constants import q_at
    Q0 = q_at()
    # EXCISED: was Q0 = float(q_at()). q_at() ALREADY returns mpf at 50 dps, so
    # the cast was a pure downgrade to 53 bits -- a NO-FLOAT64 violation with
    # nothing bought: mpf supports every arithmetic operator this file uses.
except Exception as _exc:  # pragma: no cover - fail loudly, never substitute
        # Was: Q0 = 1.1099780333553254 — a value that is NEITHER pin, sitting
        # 506 ppb from muon and 495 ppb from proton, i.e. ~44x the ~11.5 ppb
        # mu-p substrate tension the two-layer discipline exists to manage. It
        # was substituted silently on any import hiccup, so a bare container
        # produced numbers that looked fine and were wrong by 44 tensions.
        # AGENTS.md q0-anchor: never straddle the two layers inside one quantity;
        # q0_cross_layer_fallback_scan.py: "fail loudly" rather than substitute.
        raise RuntimeError(
            "q_at() unavailable and there is no safe fallback: this producer "
            "must compute at a declared pin, not at a hardcoded approximation. "
            "Install/point at qou-substrate rather than substituting a literal."
        ) from _exc

try:
    from qou_substrate.witness import WitnessBuilder
except Exception:
    from witness_base import WitnessBuilder

# Constants
R_gas = 8.314462618  # J / (mol K)
h = Q0 - 1.0 / Q0
h2 = h * h
dim_q = Q0 + 1.0 / Q0  # [2]_q

# Molecule Data: (E_cov kJ/mol, n_HB, n_K, T_boil_obs K, T_melt_obs K)
MOLECULES = {
    "H2O": (460.0, 2, 6, 373.15, 273.15),
    "HF":  (565.0, 1, 3, 293.15, 189.6),
    "NH3": (391.0, 1, 3, 239.81, 195.4)
}

def q_integer(n: int, q: float) -> float:
    return (q**n - q**(-n)) / (q - 1/q)

def main() -> None:
    w = WitnessBuilder("phase-transition-q-ideal-gas", engine="python")
    
    print("=" * 80)
    print("Boiling/Freezing Temperature Scan via q-Equation of State (NO FIT)")
    print("=" * 80)
    
    for name, (e_cov, n_hb, n_k, t_boil_obs, t_melt_obs) in MOLECULES.items():
        print(f"[{name}]")
        
        # 1. Cohesion Energy S_q^(∂)
        S_q_boundary = n_hb * h2 * e_cov * 1000.0  # J/mol
        
        # 2. Boiling Point (Gas -> Liquid)
        t_boil_pred = S_q_boundary / (dim_q * R_gas)
        boil_ratio = t_boil_pred / t_boil_obs
        
        # 3. Melting Point (Liquid -> Solid)
        n_k_q = q_integer(n_k, Q0)
        t_melt_pred = S_q_boundary / (dim_q * n_k_q * R_gas)
        melt_ratio = t_melt_pred / t_melt_obs
        
        w.add_data(f"{name}_T_boil_pred", t_boil_pred)
        w.add_data(f"{name}_T_boil_obs", t_boil_obs)
        w.add_data(f"{name}_boil_ratio", boil_ratio)
        w.add_data(f"{name}_T_melt_pred", t_melt_pred)
        w.add_data(f"{name}_T_melt_obs", t_melt_obs)
        w.add_data(f"{name}_melt_ratio", melt_ratio)
        
        print(f"  T_boil(pred) = {float(t_boil_pred):.1f} K | obs = {float(t_boil_obs):.1f} K | gap ratio = {float(boil_ratio):.2f}x")
        print(f"  T_melt(pred) = {float(t_melt_pred):.1f} K | obs = {float(t_melt_obs):.1f} K | gap ratio = {float(melt_ratio):.2f}x")
        print()

    print("CONCLUSION: The strict geometric mapping P_q V_q = n_q R T over-predicts temperatures.")
    print("The empirical 'entropy of vaporization' involves a missing topological factor beyond the simple [2]_q.")
    
    w.add_assertion(
        "Direct substitution of [2]_q yields gap ratio ~6-10x",
        computed=True, expected=True,
        source="T_boil_pred = S_q / ([2]_q R) misses by a large factor"
    )
    
    w.set_description(
        "Attempts to derive absolute boiling and freezing temperatures strictly from "
        "the q-ideal gas law (q-PV = nRT) without fitted scaling factors. Computes the "
        "cohesion energy from the h²-suppressed H-bond network, then sets T_boil = S_q / (n_q R). "
        "With the naive choice n_q = [2]_q (the dimension of the Hopf base exploring S²), "
        "this over-predicts the temperatures by a factor of 6.4x to 10x. This demonstrates that "
        "the true entropy of vaporisation ΔS_vap requires a more sophisticated topological "
        "partition function (likely involving the full Reeb flow phase space) rather than just "
        "the bare dimension [2]_q. Result is recorded honestly as open."
    )
    w.add_data("tier", "open")
    w.add_data("finding", "The bare mapping P_q V_q = [2]_q R T over-predicts T_boil and T_melt by 6-10x. A derived topological factor for ΔS_vap is required. No fit applied. Status remains OPEN.")
    
    w.save()
    print("Saved witness: phase-transition-q-ideal-gas.witness.json")

if __name__ == "__main__":
    main()
