#!/usr/bin/env python3
"""
g_A from the Iwahori--Hecke algebra of the nucleon braid — witness computation.

The axial coupling g_A measures the ratio of axial to vector weak
matrix elements of the nucleon.  In the QOU, the proton is a
Borromean link of 3 quarks (uud), and the weak interaction is a
single Skein crossing change (d→u).

Physics:
  g_V = 1 (exact, CVC / Ward identity for SU_q(2))
  g_A = ratio of antisymmetric to symmetric Hecke traces at the
        converting generator

The computation evaluates the beta-decay matrix element in the
Iwahori--Hecke algebra H_3(q) using the standard (2-dimensional) and
trivial (1-dimensional) irreducible representations.

  - Trivial rep: σ_i → q  (symmetric/vector channel)
  - Sign rep: σ_i → -q⁻¹  (antisymmetric)
  - Standard rep: σ_i → 2×2 matrices  (mixed/axial channel)

The axial coupling is:
  g_A = tr_standard(β) / tr_trivial(β)

where β is the nucleon braid.

Target: g_A ≈ 1.2754 ± 0.0013 (PDG 2024)

Usage:
    python3 computations/borromean-axial-coupling.py

Output:
    computations/borromean-axial-coupling.witness.json
"""

import json
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import Q as q

# ══════════════════════════════════════════════════════════════════
# Iwahori--Hecke algebra H_3(q) — irreducible representations
# ══════════════════════════════════════════════════════════════════
#
# The Iwahori--Hecke algebra H_3(q) has 3 irreducible representations
# corresponding to partitions of 3:
#
#   (3)     → trivial (symmetric), dim 1: σ_i ↦ q
#   (1,1,1) → sign (antisymmetric), dim 1: σ_i ↦ -q⁻¹
#   (2,1)   → standard (mixed), dim 2:
#
# Standard rep matrices (Jones 1987):
#   σ₁ → [[ q,  0 ],
#          [ 1, -q⁻¹ ]]
#
#   σ₂ → [[ -q⁻¹,  q - q⁻¹ ],
#          [  0,     q       ]]

qi = 1.0 / q
ha = q - qi  # q - q⁻¹

# Standard representation matrices for σ₁, σ₂
def sigma1_std():
    """σ₁ in the standard (2,1) representation of H_3(q)."""
    return [[q, 0.0], [1.0, -qi]]

def sigma2_std():
    """σ₂ in the standard (2,1) representation of H_3(q)."""
    return [[-qi, ha], [0.0, q]]

def sigma1_inv_std():
    """σ₁⁻¹ in standard rep: σ⁻¹ = σ - (q - q⁻¹)."""
    s = sigma1_std()
    return [[s[0][0] - ha, s[0][1]], [s[1][0], s[1][1] - ha]]

def sigma2_inv_std():
    """σ₂⁻¹ in standard rep."""
    s = sigma2_std()
    return [[s[0][0] - ha, s[0][1]], [s[1][0], s[1][1] - ha]]

def mat_mul(A, B):
    """2×2 matrix multiplication."""
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]],
    ]

def mat_trace(A):
    """Trace of 2×2 matrix."""
    return A[0][0] + A[1][1]

def mat_id():
    """2×2 identity."""
    return [[1.0, 0.0], [0.0, 1.0]]

# ══════════════════════════════════════════════════════════════════
# Nucleon braid representations
# ══════════════════════════════════════════════════════════════════
#
# The proton (uud) has a 3-strand braid structure from the
# Borromean linking of the color tubes.  In the QOU, the nucleon
# braid in H_3(q) is the identity braid MODULATED by the
# crossing structure from the Borromean linking.
#
# The Borromean link introduces correlations between the 3 strands.
# In the Iwahori--Hecke algebra, the Borromean structure is encoded in the
# element:
#
#   β_Borr = σ₁ σ₂⁻¹ σ₁ σ₂⁻¹  (simplest Borromean-type braid)
#
# This is NOT the identity — the alternating σ₁ σ₂⁻¹ pattern
# creates the mutual linking that characterizes Borromean rings.

# Several candidate braid words for Borromean-type structure on 3 strands
braid_candidates = {
    "borr_simple": [("s1", 1), ("s2", -1), ("s1", 1), ("s2", -1)],
    "borr_full": [("s1", 1), ("s2", -1), ("s1", 1), ("s2", -1),
                  ("s1", 1), ("s2", -1)],
    "borr_sym": [("s1", 1), ("s2", -1), ("s1", -1), ("s2", 1)],
}


def evaluate_braid_std(braid_word):
    """Evaluate a braid word in the standard representation."""
    result = mat_id()
    for gen, exp in braid_word:
        if gen == "s1":
            mat = sigma1_std() if exp > 0 else sigma1_inv_std()
        else:
            mat = sigma2_std() if exp > 0 else sigma2_inv_std()
        for _ in range(abs(exp)):
            result = mat_mul(result, mat)
    return result


def evaluate_braid_triv(braid_word):
    """Evaluate a braid word in the trivial representation."""
    result = 1.0
    for gen, exp in braid_word:
        if exp > 0:
            result *= q ** abs(exp)
        else:
            result *= (-qi) ** abs(exp)
    return result


def evaluate_braid_sign(braid_word):
    """Evaluate a braid word in the sign representation."""
    result = 1.0
    for gen, exp in braid_word:
        if exp > 0:
            result *= (-qi) ** abs(exp)
        else:
            result *= q ** abs(exp)  # inverse in sign rep
    return result


# ══════════════════════════════════════════════════════════════════
# Axial coupling from the weak vertex
# ══════════════════════════════════════════════════════════════════
#
# The beta-decay operator changes one quark (d→u) at a specific
# strand.  In the Iwahori--Hecke algebra, this is a crossing change at
# the converting generator.
#
# The VECTOR matrix element uses the trivial representation:
#   M_V = tr_triv(β) (scalar, always = q^{writhe})
#
# The AXIAL matrix element uses the standard representation:
#   M_A = tr_std(β) (includes the spin-flip component)
#
# The ratio g_A/g_V is then:
#   g_A/g_V = |M_A| / |M_V| × (spin-isospin factor)
#
# For a free quark: g_A/g_V = 1
# For 3 quarks (naive quark model): g_A/g_V = 5/3
# For 3 quarks with Borromean topology: g_A/g_V = f(q)

# ── Naive quark model at q ──────────────────────────────────────
# Replace integers with q-integers:
# [n]_q = (q^n - q^{-n}) / (q - q^{-1})
def q_int(n):
    return (q**n - qi**n) / ha

three_q = q_int(3)
four_q = q_int(4)
five_q = q_int(5)

# Naive quark model: g_A = (4Δu + Δd)/3 where Δu=4/3, Δd=-1/3
# In q-deformed version, this becomes a q-integer ratio.
# But the Borromean topology MODIFIES this.

# ── Borromean correction ────────────────────────────────────────
# Evaluate all candidate braids
results = {}
for name, braid in braid_candidates.items():
    M_std = evaluate_braid_std(braid)
    tr_std_val = mat_trace(M_std)
    tr_triv_val = evaluate_braid_triv(braid)
    tr_sign_val = evaluate_braid_sign(braid)

    # The axial coupling involves the standard rep trace
    # normalized by the trivial rep trace
    ratio = abs(tr_std_val / tr_triv_val) if tr_triv_val != 0 else None

    results[name] = {
        "braid_word": str(braid),
        "tr_trivial": tr_triv_val,
        "tr_sign": tr_sign_val,
        "tr_standard": tr_std_val,
        "M_std_matrix": [[M_std[i][j] for j in range(2)] for i in range(2)],
        "ratio_std_over_triv": ratio,
    }

# ── Combined computation ────────────────────────────────────────
# The full g_A computation requires:
# 1. The nucleon braid (from Borromean topology)
# 2. The weak vertex operator (Hecke generator = crossing change at converting strand on 𝒮_p)
# 3. The matrix element in both vector and axial channels
# 4. The spin-isospin Clebsch-Gordan coefficient

# For the proton → neutron transition (p → n + e⁺ + ν):
# The converting quark is u → d at one of the two u strands.
# The matrix element involves σ at the converting generator.

# APPROACH: Use the Markov trace with the conversion operator
# The conversion operator in H_3(q) is σ_k (crossing change at strand k)
# For the proton with ordering [u, u, d]:
# Converting strand k=1 (first u → d):
# M_vector = tr_Markov(β_p · σ_1 · β_n⁻¹) in trivial rep
# M_axial = tr_Markov(β_p · σ_1 · β_n⁻¹) in standard rep

# With Borromean braid β = σ₁σ₂⁻¹σ₁σ₂⁻¹:
# The conversion operator at strand 1 is just σ₁
# So the full operator is β · σ₁ · β⁻¹ = Borromean conjugation of σ₁

beta_borr = [("s1", 1), ("s2", -1), ("s1", 1), ("s2", -1)]
beta_borr_inv = [("s2", 1), ("s1", -1), ("s2", 1), ("s1", -1)]
conversion_op = [("s1", 1)]  # crossing change at strand 1

# Full operator: β · σ₁ · β⁻¹
full_op = beta_borr + conversion_op + beta_borr_inv
M_full_std = evaluate_braid_std(full_op)
tr_full_std = mat_trace(M_full_std)
tr_full_triv = evaluate_braid_triv(full_op)

# The bare conversion (no Borromean structure):
M_bare_std = evaluate_braid_std(conversion_op)
tr_bare_std = mat_trace(M_bare_std)
tr_bare_triv = evaluate_braid_triv(conversion_op)

# Borromean suppression factor
suppression = abs(tr_full_std / tr_bare_std) if tr_bare_std != 0 else None

# The naive quark model gives g_A/g_V = 5/3.
# The Borromean topology modifies this by the suppression factor.
g_A_naive = 5.0 / 3.0
g_A_borromean = g_A_naive * suppression if suppression else None

# ══════════════════════════════════════════════════════════════════
# Assemble witness
# ══════════════════════════════════════════════════════════════════

witness = {
    "computation": "borromean-axial-coupling",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": (
        "Computation of g_A from the Iwahori--Hecke algebra H_3(q). "
        "The Borromean braid topology of the nucleon modifies the "
        "naive quark model prediction g_A = 5/3 by a suppression "
        "factor from the standard representation trace."
    ),
    "q": q,
    "target": {"g_A": 1.2754, "source": "PDG 2024"},
    "hecke_algebra": {
        "q_integers": {
            "[2]_q": q + qi,
            "[3]_q": three_q,
            "[4]_q": four_q,
            "[5]_q": five_q,
        },
        "naive_g_A": g_A_naive,
    },
    "braid_candidates": results,
    "borromean_conversion": {
        "full_operator": "β·σ₁·β⁻¹ where β = σ₁σ₂⁻¹σ₁σ₂⁻¹",
        "tr_standard_full": tr_full_std,
        "tr_trivial_full": tr_full_triv,
        "tr_standard_bare": tr_bare_std,
        "tr_trivial_bare": tr_bare_triv,
        "suppression_factor": suppression,
        "g_A_with_borromean": g_A_borromean,
    },
    "interpretation": (
        "The Borromean braid β = σ₁σ₂⁻¹σ₁σ₂⁻¹ in H_3(q) conjugates "
        "the conversion operator σ₁. The suppression factor is the "
        "ratio of the standard-rep trace (with Borromean) to the "
        "standard-rep trace (without). This modifies g_A from the "
        "naive 5/3 to a q-dependent value."
    ),
    "caveats": [
        "The exact Borromean braid word for the nucleon is model-dependent.",
        "Multiple candidate braids are evaluated above.",
        "The spin-isospin Clebsch-Gordan factor is taken from the naive "
        "quark model (5/3 = 4/3 + 1/3).",
        "A full computation requires the colored Markov trace, not just "
        "the standard representation.",
    ],
}

out_path = Path(__file__).parent / "borromean-axial-coupling.witness.json"
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2)

print(f"Witness written to {out_path}")
print(f"\nIwahori--Hecke algebra H_3(q) at q = {q}:")
print(f"  [2]_q = {q + qi:.6f}")
print(f"  [3]_q = {three_q:.6f}")
print(f"  [4]_q = {four_q:.6f}")
print(f"  [5]_q = {five_q:.6f}")
print(f"\nNaive quark model: g_A = {g_A_naive:.4f}")
print(f"\nBorromean braid results:")
for name, res in results.items():
    print(f"  {name}:")
    print(f"    tr_trivial = {res['tr_trivial']:.6f}")
    print(f"    tr_standard = {res['tr_standard']:.6f}")
    print(f"    |tr_std/tr_triv| = {res['ratio_std_over_triv']:.6f}")
print(f"\nConversion operator (β·σ₁·β⁻¹):")
print(f"  tr_std(bare σ₁) = {tr_bare_std:.6f}")
print(f"  tr_std(β·σ₁·β⁻¹) = {tr_full_std:.6f}")
print(f"  Suppression factor = {suppression:.6f}")
print(f"  g_A (Borromean) = {g_A_borromean:.4f}")
print(f"  g_A (target) = 1.2754")
print(f"  Ratio to target = {g_A_borromean / 1.2754:.4f}" if g_A_borromean else "  (computation failed)")
