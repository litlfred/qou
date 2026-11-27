#!/usr/bin/env python3
"""
Probe: Dynamic p-n occupancy beyond the static Z·N graph.
Evaluates the fractional occupancy weights needed to match AME, given the
owner-gated s5-so3 keystone W_lambda representations, addressing halo-D and magic-alpha.

Features the SU(4) conjugate partition combinatorial rule to deduce
the Hecke representation for any isotope (A, Z, N).
"""
import sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'substrate'))

from _precision import set_compute_dps
from q_parameter import Q_50_DIGIT_STR, Q_MP
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
)

def q_int(q, n):
    return (q**n - q**(-n)) / (q - mp.mpf('1')/q)

def q_fact(q, n):
    res = mp.mpf('1')
    for i in range(1, n + 1):
        res *= q_int(q, i)
    return res

def hook_lengths(lam):
    hooks = []
    # lam is a tuple like (3, 3, 3, 3)
    lam_conj = []
    for j in range(lam[0]):
        lam_conj.append(sum(1 for row in lam if row > j))
    
    for i, row in enumerate(lam):
        for j in range(row):
            h = (row - 1 - j) + (lam_conj[j] - 1 - i) + 1
            hooks.append(h)
    return hooks

def W_lambda(q, lam):
    n = sum(lam)
    hooks = hook_lengths(lam)
    prod_hooks_sq = mp.mpf('1')
    for h in hooks:
        prod_hooks_sq *= (q_int(q, h))**2
    return q_fact(q, n) / prod_hooks_sq

def get_ground_state_partition(Z, N, S):
    """
    Derives the SU(4) spin-flavor partition lam |- 3A for the ground state
    using exact quark pairing. S is the nuclear spin.
    """
    Nu = 2*Z + N
    Nd = Z + 2*N
    
    valid_partitions = []
    for u_up in range(Nu + 1):
        u_down = Nu - u_up
        for d_up in range(Nd + 1):
            d_down = Nd - d_up
            # Spin is |(u_up + d_up) - (u_down + d_down)| / 2
            # So difference is 2*S
            if abs((u_up + d_up) - (u_down + d_down)) == 2 * S:
                part = tuple(sorted([u_up, u_down, d_up, d_down], reverse=True))
                part = tuple(x for x in part if x > 0)
                if part not in valid_partitions:
                    valid_partitions.append(part)
                    
    # Return the most symmetric one (lowest max element, i.e., most rectangular)
    # This maximizes W_lambda.
    valid_partitions.sort(key=lambda p: (p[0], p))
    return valid_partitions[0] if valid_partitions else None

# E0 universal scale factor (MeV) - extracted from H_3 / Q_beta normalization
mp.mp.dps = max(50, mp.mp.dps)
E0 = mp.mpf('4.2045')

def evaluate_occupancy_gap(isotope, Z, N, S, ame_mev):
    q = Q_MP
    
    lam = get_ground_state_partition(Z, N, S)
    W_lam = W_lambda(q, lam)
    
    E_std_bond = mp.mpf('3.89')
    static_binding = (Z * N) * E_std_bond
    
    E_gate = E0 * mp.log(1 / W_lam)
    required_occupancy = ame_mev / E_gate
    
    return {
        "partition": lam,
        "W_lambda": float(W_lam),
        "E_gate_MeV": float(E_gate),
        "static_Z_N_binding": float(static_binding),
        "required_dynamic_occupancy": float(required_occupancy),
        "AME_MeV": ame_mev
    }

def main():
    set_compute_dps()
    
    isotopes = [
        ("2H", 1, 1, 1, AME_B_DEUTERON_MEV_VALIDATION),
        ("3H", 1, 2, 0.5, 8.481821),
        ("3He", 2, 1, 0.5, AME_B_HE3_MEV_VALIDATION),
        ("4He", 2, 2, 0, AME_B_HE4_MEV_VALIDATION)
    ]
    
    print("=========================================================")
    print(" SU(4) Generalized Dynamic p-n Occupancy Probe ")
    print("=========================================================")
    for (name, Z, N, S, ame) in isotopes:
        res = evaluate_occupancy_gap(name, Z, N, S, ame)
        print(f"\nIsotope {name} (Z={Z}, N={N}, S={S})")
        print(f"  Quarks: Nu={2*Z+N}, Nd={Z+2*N}")
        print(f"  Conjugate Partition λ ⊢ {3*(Z+N)} : {res['partition']}")
        print(f"  Plancherel Weight W_λ: {res['W_lambda']:.6f}")
        print(f"  E_gate (dynamic): {res['E_gate_MeV']:.4f} MeV")
        print(f"  AME: {res['AME_MeV']:.4f} MeV")
        print(f"  Static Z·N Binding: {res['static_Z_N_binding']:.4f} MeV")
        print(f"  => Dynamic Occupancy c_λ: {res['required_dynamic_occupancy']:.4f}")

if __name__ == "__main__":
    main()
