#!/usr/bin/env python3
import sys
from pathlib import Path
import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge

from _precision import set_compute_dps
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV
from qou_substrate.constants import q_at, q_muon_at

from canonical_braid_crossings import atom_canonical_crossings
from hecke_character_symbolic import q_character_on_braid_word
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic
from witness_base import WitnessBuilder

def main():
    set_compute_dps(60)
    q_p = q_at(60)
    q_m = q_muon_at(60)
    
    Q_BETA_CODATA = mp.mpf("0.78233341")
    Q_N2 = mp.mpf("0.782334410277840137760143636388")
    C3_TARGET = mp.mpf("-2.06934257711516783787971951725")
    
    q_sym = sp.Symbol("q", positive=True)
    p_crossings = atom_canonical_crossings(1, 0, include_inter=False)
    n_crossings = atom_canonical_crossings(0, 1, include_inter=False)
    
    blocks = [(3,), (2,1), (1,1,1)]
    delta_tr_sym = {}
    for lam in blocks:
        chi_p = q_character_on_braid_word(lam, p_crossings, q_sym)
        chi_n = q_character_on_braid_word(lam, n_crossings, q_sym)
        y_w = y_lambda_wenzl_bridge_symbolic(lam)
        q_pos = sp.Symbol("q", positive=True)
        y_w = y_w.subs(q_pos, q_sym)
        delta_tr_sym[lam] = sp.cancel(y_w * (chi_n - chi_p))

    vals_p = {}
    vals_m = {}
    total_p = mp.mpf(0)
    total_m = mp.mpf(0)
    for lam in blocks:
        vals_p[lam] = mp.mpf(str(delta_tr_sym[lam].subs(q_sym, q_p).evalf(60)))
        vals_m[lam] = mp.mpf(str(delta_tr_sym[lam].subs(q_sym, q_m).evalf(60)))
        total_p += vals_p[lam]
        total_m += vals_m[lam]
        
    print(f"Total at q_p: {total_p}")
    print(f"Total at q_m: {total_m}")
    
    print("\nFractions w_lambda = Delta tr_lambda / Total:")
    w_p = {lam: vals_p[lam] / total_p for lam in blocks}
    w_m = {lam: vals_m[lam] / total_m for lam in blocks}
    
    for lam in blocks:
        print(f"  {lam}: w_p = {w_p[lam]}, w_m = {w_m[lam]}")
        print(f"        diff = {w_m[lam] - w_p[lam]}")
        
    print("\nIf c_3_eff = sum_lambda w_lambda * c_3_lambda")
    
    builder = WitnessBuilder(
        "qbeta-multiblock-ck-lambda-probe",
        engine="python+mpmath",
    )
    builder.set_description("Test non-uniform per-λ c_k_λ ansatz vs empirical Q_β / Q_0")
    
    ansatze = [
        ("triv=c3, sign=c3, std=0", { (3,): C3_TARGET / (w_p[(3,)] + w_p[(1,1,1)]), (1,1,1): C3_TARGET / (w_p[(3,)] + w_p[(1,1,1)]), (2,1): 0 }),
        ("std only", { (2,1): C3_TARGET / w_p[(2,1)], (3,): 0, (1,1,1): 0 }),
        ("1-dim only", { (3,): C3_TARGET / w_p[(3,)], (1,1,1): C3_TARGET / w_p[(1,1,1)], (2,1): 0 }),
    ]
    
    results = []
    for name, c3_dict in ansatze:
        c3_eff_p = sum(w_p[lam] * c3_dict[lam] for lam in blocks)
        c3_eff_m = sum(w_m[lam] * c3_dict[lam] for lam in blocks)
        
        print(f"\nAnsatz: {name}")
        print(f"  c3_eff(q_p) = {c3_eff_p}")
        print(f"  c3_eff(q_m) = {c3_eff_m}")
        print(f"  swing       = {abs(c3_eff_m - c3_eff_p)}")
        
        results.append({
            "name": name,
            "c3_eff_qp": float(c3_eff_p),
            "c3_eff_qm": float(c3_eff_m),
            "swing": float(abs(c3_eff_m - c3_eff_p))
        })
        
    builder.add_data("fractions_qp", {str(k): float(v) for k, v in w_p.items()})
    builder.add_data("fractions_qm", {str(k): float(v) for k, v in w_m.items()})
    builder.add_data("ansatze", results)
    
    builder.save()
    print("✓ Witness: qbeta-multiblock-ck-lambda-probe.witness.json")

if __name__ == "__main__":
    main()
