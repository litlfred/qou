#!/usr/bin/env python3
"""qbeta_weber_parabolic_cylinder_probe.py
Fits the continuum Weber (Parabolic Cylinder) ODE limit to the empirical c_k ladder.
F''(u) + (A + B u + C u^2)F(u) = 0
"""
from __future__ import annotations
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge
del _sys, _Path, _bridge

import sys
import os
import time
from pathlib import Path

os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps
set_compute_dps(65)
import sympy as sp
import mpmath as mp
mp.mp.dps = 65

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "hecke"))

try:
    import qou_substrate.constants as qs
except ImportError:
    sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))
    import qou_substrate.constants as qs

from witness_base import WitnessBuilder

def main():
    t0 = time.monotonic()
    
    # Empirical targets
    c0 = mp.mpf("1.0")
    c1 = mp.mpf("0.0")
    c2 = mp.mpf("-1.0")
    c3 = mp.mpf("-2.02161553125628729290")
    
    # Notice from older audits: c_4 is below the extraction precision floor,
    # but was estimated around ~ -0.97 to -1.13 in various fits.
    c4_est = mp.mpf("-1.0") 
    
    builder = WitnessBuilder(
        "qbeta-weber-parabolic-cylinder-probe",
        engine="python+sympy",
        start_time=t0
    )
    builder.set_description(
        "Fits the parameters of the Weber/Parabolic Cylinder ODE limit "
        "F''(u) + (A + B u + C u^2)F(u) = 0 to the empirical ladder c_k."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")
    
    print("="*78)
    print(" Parabolic Cylinder / Weber ODE continuum limit probe ")
    print("="*78)
    
    print("\n1. Deriving parameters from strictly resolved k<=3 ladder:")
    print("   ODE: F'' + (A + Bu + Cu^2)F = 0")
    print("   Recurrence: c_{k+2} = -(A c_k + B c_{k-1} + C c_{k-2}) / ((k+1)(k+2))")
    
    # k=0: c_2 = -A c_0 / 2 => A = -2 c_2 / c_0
    A = -2 * c2 / c0
    print(f"   k=0 -> A = {A} (Exact match to Δχ_(2,1) = -2 invariant magnitude)")
    
    # k=1: c_3 = -(A c_1 + B c_0) / 6 => B = -6 c_3
    B = -6 * c3
    print(f"   k=1 -> B = {B} (Provides odd-rung coupling)")
    
    # k=2: c_4 = -(A c_2 + B c_1 + C c_0) / 12 => 12 c_4 = A - C => C = A - 12 c_4
    C = A - 12 * c4_est
    print(f"\n2. Extrapolating to k=4 (c_4 sits below precision floor, ~ -1.0):")
    print(f"   k=2 -> C = A - 12 c_4 = {C} (Harmonic oscillator potential z^2 term)")
    
    builder.add_data("empirical_c2", str(c2))
    builder.add_data("empirical_c3", str(c3))
    builder.add_data("fitted_A", str(A))
    builder.add_data("fitted_B", str(B))
    builder.add_data("implied_C_if_c4_is_minus1", str(C))
    
    builder.save()
    return 0

if __name__ == "__main__":
    sys.exit(main())
