#!/usr/bin/env python3
"""qbeta_habiro_multiblock_canonical_y_lambda_probe.py

Execute the full multi-block trace expansion using the CANONICAL Wenzl weights
(which involve √q). This addresses the open work from the 1ppQ ledger.
"""
from __future__ import annotations
import sys
from pathlib import Path
import os
import time

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
from qbeta_c3_multiblock_recursion_attack import per_block_chi_diff
from markov_weights_symbolic import solve_y_lambda

def evalq(expr, qval):
    q_sym = sp.Symbol("q", positive=True)
    val = sp.N(expr.subs(q_sym, sp.Float(mp.nstr(qval, 65), 65)), 65)
    return mp.mpf(str(sp.re(val)))

def main():
    t0 = time.monotonic()
    wn = WitnessBuilder("qbeta-habiro-multiblock-canonical-y-lambda-probe", engine="sympy+mpmath", start_time=t0)
    
    q_sym = sp.Symbol("q", positive=True)
    w = sp.Symbol("w")
    
    print("Full Multiblock Habiro trace expansion (Canonical y_λ)")
    print("="*60)
    
    chi = per_block_chi_diff(q_sym)
    # The canonical weights contain z, which is defined as:
    # z = sqrt(q)/(1+q) or q/(1+q)^2 etc.
    # markov_weights_symbolic.solve_y_lambda(3) handles this.
    yL = solve_y_lambda(3)
    
    print("\nStep 1: Canonical Δτ_M(q) = Σ y_λ · χ_λ(Δ_T_β)")
    delta_tau_M = sum(yL[L] * chi[L] for L in [(3,), (2, 1), (1, 1, 1)])
    delta_tau_M = sp.cancel(delta_tau_M)
    print(f"  Δτ_M(q) = {delta_tau_M}")
    
    # Check swing at anchors
    from q_parameter import Q_50_DIGIT_STR, q_muon_at
    q_proton = sp.Rational(Q_50_DIGIT_STR)
    q_muon = sp.Rational(str(q_muon_at(50)))
    
    dt_proton = sp.N(delta_tau_M.subs(q_sym, q_proton), 60)
    dt_muon = sp.N(delta_tau_M.subs(q_sym, q_muon), 60)
    
    print(f"\n  q_proton = {sp.N(q_proton, 18)}")
    print(f"  q_muon   = {sp.N(q_muon, 18)}")
    print(f"  Δτ_M(q_proton) = {dt_proton}")
    print(f"  Δτ_M(q_muon)   = {dt_muon}")
    
    swing = abs(dt_proton - dt_muon)
    print(f"  swing = |Δτ_M(p) − Δτ_M(μ)| = {swing}")
    
    wn.set_description("Full multiblock exact Habiro expansion with canonical Wenzl weights (contains √q).")
    wn.add_data("delta_tau_M_symbolic", str(delta_tau_M))
    wn.add_data("delta_tau_M_q_proton", str(dt_proton))
    wn.add_data("delta_tau_M_q_muon", str(dt_muon))
    wn.add_data("cross_anchor_swing", str(swing))
    
    out = wn.save()
    print(f"\nWitness: {out.name}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
