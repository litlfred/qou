#!/usr/bin/env python3
"""delta_lambda_extended_tower.py
Extracts the extended Delta_lambda tower from mass-table-ppb.witness.json.
This includes both the canonical short tower and the alpha-cluster tower.
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE.parent / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder
from qou_substrate.constants import q_at

SRC = HERE / "mass-table-ppb.witness.json"

def main() -> int:
    t0 = time.monotonic()
    q0 = float(q_at(30))
    lnq = math.log(q0)
    
    payload = json.loads(SRC.read_text())
    if "data" in payload and "rows" in payload["data"]:
        rows_in = payload["data"]["rows"]
    else:
        rows_in = payload.get("rows", [])

    rows = []
    for r in rows_in:
        pred_val = r.get("B_pred_MeV")
        ame_val = r.get("B_AME_MeV")
        
        if pred_val is None or ame_val is None:
            continue
            
        B_pred = float(pred_val)
        B_ame = float(ame_val)
        A = int(r["A"])
        sym = r.get("sym", f"{A}?")
        
        if B_pred == 0:
            continue
            
        delta = B_ame / B_pred
        x = math.log(delta) / lnq
        law = 10 * A - 5
        
        rows.append({
            "atom": sym, "Z": r["Z"], "N": r["N"], "A": A,
            "B_AME_MeV": B_ame,
            "B_pred_MeV": B_pred,
            "Delta_lambda": round(delta, 6),
            "log_q0_Delta": round(x, 4),
            "law_10A_minus_5": law,
            "deviation_from_law": round(x - law, 4),
        })

    w = WitnessBuilder("delta-lambda-extended-tower", engine="python", start_time=t0)
    w.set_description("Extended tower extracted from mass-table-ppb.witness.json.")
    w.add_data("q0", q0)
    w.add_data("rows", rows)
    out = w.save()
    
    print(f"{'atom':>5} {'A':>2} {'Δ_λ':>10} {'log_q0':>8} {'10A−5':>6} {'dev':>6}")
    for r in rows:
        print(f"{r['atom']:>5} {r['A']:>2} {r['Delta_lambda']:>10.4f} "
              f"{r['log_q0_Delta']:>8.2f} {r['law_10A_minus_5']:>6} "
              f"{r['deviation_from_law']:>+6.2f}")
              
    print("\nAlpha-Cluster Tower Recurrence Analysis (A=4, 8, 12, 16, 20, 24, 40):")
    alpha_atoms = ["4He", "8Be", "12C", "16O", "20Ne", "24Mg", "40Ca"]
    alpha_dict = {r["atom"]: r["Delta_lambda"] for r in rows if r["atom"] in alpha_atoms}
    
    for i in range(1, len(alpha_atoms) - 1):
        prev = alpha_atoms[i-1]
        curr = alpha_atoms[i]
        nxt = alpha_atoms[i+1]
        if prev in alpha_dict and curr in alpha_dict and nxt in alpha_dict:
            b_nu = (alpha_dict[nxt] + alpha_dict[prev]) / alpha_dict[curr]
            print(f"  {curr:4s} (ν={i+1}): b = ({alpha_dict[nxt]:.4f} + {alpha_dict[prev]:.4f}) / {alpha_dict[curr]:.4f} = {b_nu:.4f}")

    print(f"\nWitness: {out.name}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
