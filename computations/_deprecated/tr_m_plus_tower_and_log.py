#!/usr/bin/env python3
"""
Two derivation paths for ρ_F from the matrix-trace machinery:

APPROACH 1 — Multi-brane tower:
    m(K) = |tr_M(β)| + Σ_{n=1}^∞ ℏ_q^{2n} · tower^{(n)}
    ρ_F = m_e · 8G · m(K) / V_hyp(K)
    tower^{(n)} = Markov-stab lift at level n of the per-gen V̂

APPROACH 2 — Per-irrep log:
    B = Σ_λ w_λ · m_e · ln|Φ_q(χ_λ(β)/d_λ)|     (paper's tower-binding-energy)
    ρ_F_effective = B / V_hyp

Uses the matrix-trace witness already produced by
std_matrix_trace_closed_form.py.  No new char computations.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0, HBAR_Q_SQ
from mass_endomorphism import Phi_q
from canonical_plus_multibrane import (lift_V_markov, tower_mass_level,
                                           per_gen_V_hat_aggregated)

CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN_8G = 8.0 * CATALAN_G
M_E_MEV = 0.51099895
ALPHA_MEV = M_E_MEV * VOL_BORROMEAN_8G

# From std_matrix_trace_closed_form.witness.json
TR_M_PLANCHEREL = {
    "D":   0.00540032,
    "T":   0.00474272,
    "3He": 0.00597657,
}

ATOMS = [
    ("D",   1, 1, 2.22456612, 4.4008325),
    ("T",   1, 2, 8.4817984,  8.28632),
    ("3He", 2, 1, 7.7180375,  VOL_BORROMEAN_8G),
]


def approach_1_multi_brane(Z: int, N: int, n_levels: int = 4):
    """ρ_F from tr_M + Σ ℏ_q^{2n} · tower^(n) using existing machinery."""
    V_atom = per_gen_V_hat_aggregated(Z, N, include_inter=True)
    V_free = per_gen_V_hat_aggregated(Z, N, include_inter=False)
    tower_total = 0.0
    per_level = []
    for n in range(1, n_levels + 1):
        V_a_n = lift_V_markov(V_atom, n)
        V_f_n = lift_V_markov(V_free, n)
        m_a_n = tower_mass_level(V_a_n, pair_mode="full")
        m_f_n = tower_mass_level(V_f_n, pair_mode="full")
        delta_n = m_f_n - m_a_n
        scale_n = HBAR_Q_SQ ** n
        term = scale_n * delta_n
        tower_total += term
        per_level.append({
            "level": n, "hbar_q_2n": scale_n,
            "delta_n": delta_n, "contrib": term,
        })
    name = {(1,1):"D", (1,2):"T", (2,1):"3He", (2,2):"4He"}.get((Z,N),"?")
    tr_m_atom = TR_M_PLANCHEREL.get(name, 0.0)
    m_cat = tr_m_atom + tower_total
    return {
        "tr_M_atom": tr_m_atom,
        "tower_contrib_cat": tower_total,
        "m_cat_total": m_cat,
        "per_level": per_level,
    }


def approach_2_per_irrep_log(Z: int, N: int):
    """ρ_F from Σ_λ w_λ · m_e · ln|Φ_q(χ_λ/d_λ)| per paper's tower-
    binding-energy.  Uses per-partition characters from the matrix-trace
    witness."""
    witness_path = (Path(__file__).parent
                     / "std-matrix-trace-closed-form.witness.json")
    if not witness_path.exists():
        return {"status": "no_witness"}
    w = json.loads(witness_path.read_text())
    name = {(1,1):"D", (1,2):"T", (2,1):"3He"}.get((Z,N), "?")
    atom_entry = next((a for a in w["atoms"]
                        if a.get("Z") == Z and a.get("N") == N), None)
    if atom_entry is None:
        return {"status": "atom_not_in_witness"}

    # Σ_λ w_λ · ln|Φ_q(χ_λ/d_λ)|
    total = 0.0
    per_partition = []
    cap_frac = 0.995
    q_cap = float(Q0) * cap_frac
    for p in atom_entry["per_partition"]:
        if "status" in p:
            continue
        dim = p["dim"]
        w_lam = p["w_lambda"]
        chi_abs = abs(complex(p["chi_re"], p["chi_im"]))
        if dim == 0:
            continue
        v = chi_abs / dim            # χ_λ/d_λ ∈ trace-per-unit
        a = min(abs(v), q_cap)
        try:
            phi = Phi_q(a)
            if phi > 0 and math.isfinite(phi):
                contrib = w_lam * math.log(phi)
                total += contrib
                per_partition.append({
                    "shape": p["shape"], "w_lambda": w_lam,
                    "chi_over_d": v, "phi_q": phi,
                    "ln_phi": math.log(phi),
                    "contribution": contrib,
                })
        except Exception:
            pass
    return {
        "sum_w_lam_ln_phi": total,
        "B_MeV": M_E_MEV * total,
        "per_partition": per_partition,
    }


if __name__ == "__main__":
    print("=" * 100)
    print("TWO DERIVATION PATHS using matrix-trace |tr_M(β)|")
    print(f"  α = m_e · 8G = {ALPHA_MEV:.6f} MeV")
    print("=" * 100)

    print(f"\n{'-' * 100}")
    print("APPROACH 1: m(K) = |tr_M(β)| + Σ ℏ_q^{2n} · tower^(n)")
    print(f"{'-' * 100}")
    print(f"  {'atom':>4} {'|tr_M|':>10} {'tower':>10} {'m_cat':>10} "
          f"{'α·m/V_hyp':>12} {'B_AME/V':>10} {'ratio':>8}")
    results_1 = []
    for (name, Z, N, B_ame, V_hyp) in ATOMS:
        r = approach_1_multi_brane(Z, N, n_levels=4)
        rho_derived = ALPHA_MEV * r["m_cat_total"] / V_hyp
        rho_observed = B_ame / V_hyp
        ratio = rho_derived / rho_observed if rho_observed else float("nan")
        print(f"  {name:>4} {r['tr_M_atom']:>10.5f} "
              f"{r['tower_contrib_cat']:>+10.4f} "
              f"{r['m_cat_total']:>+10.4f} "
              f"{rho_derived:>12.5f} {rho_observed:>10.5f} "
              f"{ratio:>8.4f}")
        r.update({"atom": name, "Z": Z, "N": N, "B_AME": B_ame,
                   "V_hyp": V_hyp,
                   "rho_derived": rho_derived,
                   "rho_observed": rho_observed,
                   "ratio": ratio})
        results_1.append(r)

    print(f"\n{'-' * 100}")
    print("APPROACH 2: B = Σ_λ w_λ · m_e · ln|Φ_q(χ_λ/d_λ)|")
    print(f"{'-' * 100}")
    print(f"  {'atom':>4} {'Σ w·ln|Φ|':>14} {'B_pred (MeV)':>14} "
          f"{'B_AME (MeV)':>14} {'err %':>10}")
    results_2 = []
    for (name, Z, N, B_ame, V_hyp) in ATOMS:
        r = approach_2_per_irrep_log(Z, N)
        if r.get("status"):
            print(f"  {name:>4} err: {r['status']}")
            continue
        B_pred = r["B_MeV"]
        err = (B_pred - B_ame) / B_ame * 100 if B_ame else float("nan")
        print(f"  {name:>4} {r['sum_w_lam_ln_phi']:>+14.6f} "
              f"{B_pred:>+14.4f} {B_ame:>14.4f} {err:>+9.3f}%")
        r.update({"atom": name, "Z": Z, "N": N, "B_AME": B_ame,
                   "err_pct": err})
        results_2.append(r)

    witness = {
        "computation": "tr-m-plus-tower-and-log",
        "description": (
            "Two candidate derivations for ρ_F using matrix-trace "
            "|tr_M(β)| from std_matrix_trace_closed_form:\n"
            "(1) Multi-brane: m = |tr_M| + Σ ℏ_q^{2n}·tower^(n)\n"
            "(2) Per-irrep log: B = Σ_λ w_λ·m_e·ln|Φ_q(χ_λ/d_λ)|\n"
            "No fitting.  Tests whether either reproduces B_AME."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "alpha_MeV": ALPHA_MEV,
        "tr_m_plancherel_inputs": TR_M_PLANCHEREL,
        "approach_1_multi_brane": results_1,
        "approach_2_per_irrep_log": results_2,
    }
    out = Path(__file__).parent / "tr-m-plus-tower-and-log.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
