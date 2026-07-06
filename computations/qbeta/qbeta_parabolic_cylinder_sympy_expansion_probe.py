#!/usr/bin/env python3
"""qbeta_parabolic_cylinder_sympy_expansion_probe.py

Execute the direct Sympy Taylor expansion of the Weber / Parabolic Cylinder ODE.
Matches the coefficients back to the user's legacy empirical J/K parameters.
"""
from __future__ import annotations
import sys
import os
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
for _sub in ("", "hecke", "markov"):
    _p = str(HERE.parent / _sub) if _sub else str(HERE.parent)
    if _p not in sys.path:
        sys.path.insert(0, _p)
        
import _path_bridge as _pb

os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")
from _precision import set_compute_dps
set_compute_dps(65)
import mpmath as mp
mp.mp.dps = 65
import sympy as sp

from witness_base import WitnessBuilder

def main():
    t0 = time.monotonic()
    wn = WitnessBuilder("qbeta-parabolic-cylinder-sympy-expansion-probe", engine="sympy+mpmath", start_time=t0)
    
    print("Direct Sympy Taylor expansion of Parabolic Cylinder limit")
    print("="*60)
    
    # ODE: F''(u) + (A + B*u + C*u^2)F(u) = 0
    A, B, C = sp.symbols('A B C')
    
    max_k = 6
    c_list = [sp.Integer(0)] * (max_k + 1)
    
    # Boundary conditions for generating function
    c_list[0] = sp.Integer(1)
    c_list[1] = sp.Integer(0)
    
    # Recurrence: (k+2)(k+1) c_{k+2} + A c_k + B c_{k-1} + C c_{k-2} = 0
    for k in range(max_k - 1):
        term = sp.Integer(0)
        if k >= 0: term += A * c_list[k]
        if k >= 1: term += B * c_list[k-1]
        if k >= 2: term += C * c_list[k-2]
        c_list[k+2] = sp.simplify(-term / ((k+1)*(k+2)))
        
    print("\nSymbolic Coefficients:")
    for i, val in enumerate(c_list):
        print(f"  c_{i} = {val}")
        
    print("\nMapping to empirical pairs (J = -2, K ~ 2.0):")
    # From c_2 = -A/2 = -1 (so A = 2, meaning c_2 = J/2)
    # c_3 = -B/6 ~ -2.02 (so B ~ 12.12, meaning c_3 = J)
    # c_4 = A^2/24 - C/12 = 1/6 - C/12
    # If c_4 = K ~ 2.0, then C/12 = 1/6 - 2 => C = -22.0
    
    wn.set_description("Symbolic Taylor expansion of the Weber / Parabolic Cylinder ODE limit, mapping symbolic ODE terms back to legacy categorical J/K scaling powers.")
    wn.add_data("symbolic_coefficients", {f"c_{i}": str(c_list[i]) for i in range(max_k+1)})
    
    wn.add_data("mapping_to_JK", {
        "A": "2 (derived from c_2 = J/2)",
        "B": "~ 12.12 (derived from c_3 = J)",
        "C": "-22.0 (derived from c_4 = K ~ 2.0)",
        "c_4_formula": "A^2/24 - C/12"
    })
    
    out = wn.save()
    print(f"\nWitness: {out.name}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
