#!/usr/bin/env python3
"""
Explicit α_k derivation at H_3 via Markov pairings on E_∞ classes.

Per prop:spectral-sequence-h3-explicit, the surviving E_∞ classes are:

  E_∞^{0,*}: [1]                            rank 1
  E_∞^{1,*}: [σ_1 - σ_2]                    rank 1 (Markov pairing = 0; needs higher op)
  E_∞^{2,*}: [σ_1σ_2 + σ_2σ_1]              rank 1
  E_∞^{3,*}: [σ_1σ_2σ_1]/d_2-image          rank ≤ 1 (Yang-Baxter quotient)

The α_k are extracted as the Markov pairings (via Hoefsmit characters
across all 3 partitions of n=3: (3), (2,1), (1,1,1)).

Computes explicitly:
  α_0 = tr_M([1]) / [normalization]
  α_1 = tr_M([σ_1-σ_2]) (vanishes — flag as "needs higher Hochschild op")
  α_2 = tr_M([σ_1σ_2 + σ_2σ_1]) / [normalization]  (expect z²)
  α_3 = tr_M([σ_1σ_2σ_1]) / [normalization]
"""
from __future__ import annotations
import json, sys, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
import numpy as np
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_characters import (
    build_seminormal_matrices, partitions_of, dim_q, qfac, q_int
)

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
m_e = mp.mpf("0.51099895")
h = Q0 - QI
z_mark = 1/(mp.sqrt(Q0) + 1/mp.sqrt(Q0))


def qint(n): return q_int(n)


# Build seminormal matrices for each partition of 3
print("=" * 100)
print("Explicit α_k at H_3 via Markov pairings on E_∞ classes")
print("=" * 100)
print(f"  q_0 = {float(Q0):.10f}, h = q - 1/q = {float(h):.6f}, z = 1/(√q + 1/√q) = {float(z_mark):.6f}")
print()

partition_data = {}
for shape in [(3,), (2, 1), (1, 1, 1)]:
    sigmas, d_lam, _ = build_seminormal_matrices(shape)
    # Convert sparse → dense for explicit matrix products
    if hasattr(sigmas[0], 'toarray'):
        sigmas_dense = [s.toarray() for s in sigmas]
    else:
        sigmas_dense = list(sigmas)
    d_q = float(dim_q(shape))
    print(f"  λ = {shape}:  dim = {d_lam}, dim_q = {d_q:.6f}")
    print(f"    σ_1: {sigmas_dense[0].tolist() if d_lam <= 2 else '...'}")
    print(f"    σ_2: {sigmas_dense[1].tolist() if d_lam <= 2 else '...'}")
    partition_data[shape] = {
        "sigmas": sigmas_dense,
        "dim": d_lam,
        "dim_q": d_q,
        "w_lambda": d_q * d_q / float(qfac(3))
    }
print()


# Markov trace of a Hecke element w (sum of monomials):
#   tr_M(w) = Σ_λ w_λ · χ_λ(w) / dim_q(V_λ) · (some normalization)
# Actually for the canonical Markov trace:
#   tr_M = Σ_λ w_λ · χ_λ(·) where w_λ · z^? are appropriate weights
#
# Let's just compute χ_λ(w) per partition (Hoefsmit), then form pairing.
def chi_lambda(w_matrices_per_partition, weights_in_basis):
    """
    Compute χ_λ(w) where w is a linear combination of basis elements.
    weights_in_basis is a dict {basis_element_name: coefficient}
    w_matrices_per_partition is the matrix representation of each basis
    element in irrep λ.
    """
    results = {}
    for shape in [(3,), (2, 1), (1, 1, 1)]:
        d = partition_data[shape]["dim"]
        sigmas = partition_data[shape]["sigmas"]
        # Build matrix sum
        M = np.zeros((d, d))
        for elem, coeff in weights_in_basis.items():
            if elem == "1":
                M_elem = np.eye(d)
            elif elem == "s1":
                M_elem = sigmas[0]
            elif elem == "s2":
                M_elem = sigmas[1]
            elif elem == "s1s2":
                M_elem = sigmas[0] @ sigmas[1]
            elif elem == "s2s1":
                M_elem = sigmas[1] @ sigmas[0]
            elif elem == "s1s2s1":
                M_elem = sigmas[0] @ sigmas[1] @ sigmas[0]
            else:
                continue
            M = M + coeff * M_elem
        results[shape] = float(np.trace(M))
    return results


# Markov trace pairing — sum over partitions weighted by w_λ · z^(n-1)
# For H_3, n=3, the Markov trace formula is:
#   tr_M(w) = Σ_λ w_λ · χ_λ(w)
# where w_λ are the Wedderburn weights.
# (Without the z^(n-1) scaling; this is per the spectral-sequence-h3-explicit
# convention.)
def Markov_trace(weights_in_basis):
    chis = chi_lambda(partition_data, weights_in_basis)
    tot = 0.0
    for shape in [(3,), (2, 1), (1, 1, 1)]:
        w = partition_data[shape]["w_lambda"]
        tot += w * chis[shape]
    return tot, chis


# Surviving E_∞ classes per spectral-sequence-h3-explicit
print("─" * 100)
print("E_∞ class Markov pairings:")
print("─" * 100)

# E_∞^{0,*}: [1]
trM_1, chis_1 = Markov_trace({"1": 1})
print(f"\n  E_∞^{{0,*}} = [1]")
print(f"    χ per λ:       {chis_1}")
print(f"    Σ w_λ · χ_λ([1]) = Σ w_λ · dim_q(V_λ)?  Got = {trM_1:.6f}")
print(f"    Compare to identity contribution = 1?")

# E_∞^{1,*}: [σ_1 - σ_2]
trM_minus, chis_minus = Markov_trace({"s1": 1, "s2": -1})
print(f"\n  E_∞^{{1,*}} = [σ_1 - σ_2]")
print(f"    χ per λ:       {chis_minus}")
print(f"    Markov pairing: {trM_minus:.6f}")
print(f"    EXPECTED: 0 (per prop:spectral-sequence-h3-explicit; vanishes)")

# E_∞^{2,*}: [σ_1σ_2 + σ_2σ_1]
trM_pair, chis_pair = Markov_trace({"s1s2": 1, "s2s1": 1})
print(f"\n  E_∞^{{2,*}} = [σ_1σ_2 + σ_2σ_1]")
print(f"    χ per λ:       {chis_pair}")
print(f"    Markov pairing: {trM_pair:.6f}")
print(f"    EXPECTED: 2z² = {float(2*z_mark**2):.6f}  (matches?)")

# E_∞^{3,*}: [σ_1σ_2σ_1] (after d_2 quotient)
trM_max, chis_max = Markov_trace({"s1s2s1": 1})
print(f"\n  E_∞^{{3,*}} = [σ_1σ_2σ_1] / d_2-image")
print(f"    χ per λ:       {chis_max}")
print(f"    Markov pairing: {trM_max:.6f}")
print(f"    Identifies α_3 (Term 6 jet-prefix) per E_∞ pairing.")

print()
print("─" * 100)
print("Extracted α_k structural prefactors at H_3:")
print("─" * 100)

# α_0 = pairing on identity normalized
# α_2 = pairing on symmetric pair / 2 (since pair has factor 2 from sym sum)
alpha_0 = trM_1
alpha_1 = trM_minus  # vanishes
alpha_2 = trM_pair / 2  # divide by 2 since [σ_1σ_2 + σ_2σ_1] is the symmetric sum
alpha_3 = trM_max

print(f"  α_0 = ⟨tr_M, [1]⟩                    = {alpha_0:.10f}")
print(f"  α_1 = ⟨tr_M, [σ_1-σ_2]⟩              = {alpha_1:.10f}  (vanishes; α_1 needs higher op)")
print(f"  α_2 = ⟨tr_M, [σ_1σ_2+σ_2σ_1]⟩ / 2    = {alpha_2:.10f}")
print(f"          vs z²                       = {float(z_mark**2):.10f}")
print(f"  α_3 = ⟨tr_M, [σ_1σ_2σ_1]⟩            = {alpha_3:.10f}")
print(f"          vs z³                       = {float(z_mark**3):.10f}")

# Check whether α_2 = z²
match_alpha_2_z2 = abs(alpha_2 - float(z_mark**2)) / float(z_mark**2)
print(f"\n  α_2 / z² ratio = {alpha_2 / float(z_mark**2):.6f}  (should be 1 if α_2 = z²)")

# Check α_3 = z³ hypothesis
match_alpha_3_z3 = abs(alpha_3 - float(z_mark**3)) / float(z_mark**3) if z_mark**3 != 0 else 1
print(f"  α_3 / z³ ratio = {alpha_3 / float(z_mark**3):.6f}  (z^k pattern test)")

# Save
out = {
    "computation": "explicit-alpha-k-h3",
    "description": ("Explicit α_k derivation at H_3 via direct Markov pairings on "
                    "the surviving E_∞ classes per prop:spectral-sequence-h3-explicit. "
                    "Computes Hoefsmit characters per partition, sums Wedderburn-weighted "
                    "to get Markov trace, then projects onto each E_∞ class."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "q_0": float(Q0),
    "z_markov": float(z_mark),
    "alpha_k_extracted": {
        "alpha_0": float(alpha_0),
        "alpha_1": float(alpha_1),
        "alpha_2": float(alpha_2),
        "alpha_3": float(alpha_3),
    },
    "alpha_k_z_power_pattern_test": {
        "z²": float(z_mark**2),
        "z³": float(z_mark**3),
        "alpha_2 / z²": float(alpha_2 / float(z_mark**2)) if z_mark**2 != 0 else None,
        "alpha_3 / z³": float(alpha_3 / float(z_mark**3)) if z_mark**3 != 0 else None,
    },
    "open": [
        "α_1 vanishes via direct Markov pairing — needs higher Hochschild operation (Gerstenhaber bracket)",
        "α_3 may be cohomologically rank-zero after d_2 (per spectral-sequence-h3-explicit); current value is direct Markov pairing without d_2 quotient applied"
    ]
}
out_path = Path(__file__).parent / "explicit-alpha-k-h3.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"\nWitness: {out_path}")
