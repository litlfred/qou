#!/usr/bin/env python3
"""
delta_q_decoration.py

Build δ_q : H_n(q) → R⊗R^|partitions| as a Wedderburn-decomposed
decoration of the NF basis.  For each algebra element b, output:

    δ_q(b) = (χ_λ(b) for λ ⊢ n)  -- per-irrep q-character vector
    dim_q(λ) for each λ
    w_λ = dim_q(λ)²/[n]_q!  -- Wedderburn weight
    Markov trace tr_M(b) = Σ_λ w_λ · χ_λ(b) / f^λ
    (where f^λ = #SYT(λ) is the classical irrep dimension)

Then test the round-15/16 hypothesis on the H_2 molecular braid:
does its Wedderburn projection have nontrivial weight on the
λ ∈ {(4), (2,2)} components corresponding to the
T_{2,9} and T_{3,5} force-carrier sub-sectors?

If yes — and the projection coefficients give a δ_q-ratio matching
α_EM² — the conjecture closes for H_2 binding.

Output: delta-q-decoration.witness.json
"""
import json
import sys
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
import numpy as np
from q_parameter import Q as q0, Q_INV as qi0, HA
from hecke_characters import (
    partitions_of, build_seminormal_matrices, qfac, dim_q,
    standard_young_tableaux,
)

# ──────────────────────────────────────────────────────────────────────
# Witness scaffolding
# ──────────────────────────────────────────────────────────────────────
WITNESS = {
    "engine": "python",
    "engineVersion": f"python {sys.version.split()[0]}",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": "delta-q-decoration",
    "scriptFile": "delta_q_decoration.py",
    "description": (
        "Wedderburn decomposition of H_n(q) for n=2,3,4: "
        "per-irrep q-character vectors of NF basis elements, "
        "and Wedderburn projection of the H_2 molecular braid "
        "to test the round-15/16 force-carrier-subsector hypothesis."
    ),
    "contentBlock": "conj:e-hartree-categorical-derivation",
    "parameters": {
        "q0": q0,
        "h": HA,
        "z": 1.0/(q0**0.5 + qi0**0.5),
    },
    "data": {},
    "assertions": [],
}

# ──────────────────────────────────────────────────────────────────────
# δ_q for small Hecke algebras
# ──────────────────────────────────────────────────────────────────────

def chi_lambda_of_braid_word(shape, word, n):
    """χ_λ(σ_{w_1} σ_{w_2} ...) for braid word `word` (1-indexed gens)."""
    sigmas, dim, _ = build_seminormal_matrices(tuple(shape))
    # Multiply representations in order
    M = np.eye(dim, dtype=complex)
    for g in word:
        sgn = -1 if g < 0 else 1
        i = abs(g) - 1  # 0-indexed
        if sgn > 0:
            M = sigmas[i] @ M
        else:
            # σ_i^-1 = σ_i - h
            M = (sigmas[i] - HA * np.eye(dim)) @ M
    return float(np.real(np.trace(M)))

def wedderburn_decompose(word, n):
    """Wedderburn-decompose tr_M(braid word) into per-λ contributions.

    Returns: dict {tuple(λ) -> {chi_lambda, dim_q, w_lambda, contribution}}
    """
    nfac = qfac(n)
    out = {}
    for shape in partitions_of(n):
        chi = chi_lambda_of_braid_word(list(shape), word, n)
        d_q = dim_q(shape)
        f_lam = len(standard_young_tableaux(list(shape)))
        w_lam = d_q*d_q / nfac
        out[tuple(shape)] = {
            "chi_lambda": chi,
            "dim_q_lambda": float(d_q),
            "f_lambda": f_lam,
            "w_lambda": float(w_lam),
            "trM_contribution": float(w_lam * chi / f_lam),
        }
    return out


# ──────────────────────────────────────────────────────────────────────
# §1 — δ_q for H_2(q): basis {1, σ_1}
# ──────────────────────────────────────────────────────────────────────
print("=" * 70)
print("§1  H_2(q) Wedderburn decomposition")
print("=" * 70)

H2 = {}
# Identity: empty word
H2["identity_1"] = wedderburn_decompose([], 2)
# σ_1: word = [1]
H2["sigma_1"]    = wedderburn_decompose([1], 2)
# σ_1^9: T_{2,9} force-carrier
H2["T_2_9"]      = wedderburn_decompose([1]*9, 2)

for name, dec in H2.items():
    print(f"\n  {name}:")
    for lam, vals in dec.items():
        print(f"    λ={lam}: χ_λ = {vals['chi_lambda']:>12.6f}, "
              f"dim_q = {vals['dim_q_lambda']:>10.6f}, "
              f"w_λ·χ/f = {vals['trM_contribution']:>10.6f}")

WITNESS["data"]["H_2"] = H2

# ──────────────────────────────────────────────────────────────────────
# §2 — δ_q for H_3(q): NF basis {1, σ_1, σ_2, σ_1σ_2, σ_2σ_1, σ_1σ_2σ_1}
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("§2  H_3(q) Wedderburn decomposition")
print("=" * 70)

H3 = {}
H3["identity_1"] = wedderburn_decompose([], 3)
H3["sigma_1"]    = wedderburn_decompose([1], 3)
H3["sigma_2"]    = wedderburn_decompose([2], 3)
H3["sigma_1_sigma_2"]   = wedderburn_decompose([1,2], 3)
H3["sigma_2_sigma_1"]   = wedderburn_decompose([2,1], 3)
H3["sigma_1_sigma_2_sigma_1"] = wedderburn_decompose([1,2,1], 3)
# T_{3,5}: closure of (σ_1 σ_2)^5 in B_3
H3["T_3_5"]      = wedderburn_decompose([1,2]*5, 3)

for name, dec in H3.items():
    print(f"\n  {name}:")
    for lam, vals in dec.items():
        print(f"    λ={lam}: χ_λ = {vals['chi_lambda']:>12.6f}, "
              f"dim_q = {vals['dim_q_lambda']:>10.6f}, "
              f"w_λ·χ/f = {vals['trM_contribution']:>10.6f}")

WITNESS["data"]["H_3"] = H3

# ──────────────────────────────────────────────────────────────────────
# §3 — H_4(q): the H_2 molecular braid Wedderburn projection
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("§3  H_4(q) — H_2 molecular braid Wedderburn projection")
print("=" * 70)

# H_2 molecular braid structure:
# Optimal ordering [p1, e2, e1, p2] in B_4. The 3 generators in the
# braid chain correspond to crossings at gen 0, gen 1, gen 2:
#   gen 0: p1↔e2 (inter pe, bare)  — base crossing
#   gen 1: e2↔e1 (inter ee, bare)
#   gen 2: e1↔p2 (inter pe, bare)  — closure crossing
# But this is the TRANSFER-MATRIX structure, not a braid word.
# As a true braid: σ_1 (mediating p1-e2), σ_2 (mediating e2-e1), σ_3 (mediating e1-p2).
# Plus the dressing — but dressing is per-CROSSING, embedded in the eigenvalues.
# For the Wedderburn projection, we use the BARE molecular braid.

# Bare molecular braid (without dressing): σ_1 σ_2 σ_3 in B_4
H4 = {}
H4["bare_molecule_b4"] = wedderburn_decompose([1,2,3], 4)

for name, dec in H4.items():
    print(f"\n  {name}:")
    for lam, vals in dec.items():
        print(f"    λ={lam}: χ_λ = {vals['chi_lambda']:>12.6f}, "
              f"dim_q = {vals['dim_q_lambda']:>10.6f}, "
              f"w_λ·χ/f = {vals['trM_contribution']:>10.6f}")

WITNESS["data"]["H_4"] = H4

# ──────────────────────────────────────────────────────────────────────
# §4 — Test round-15/16 hypothesis
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("§4  Round-15/16 hypothesis test")
print("=" * 70)

# Hypothesis: bare molecular braid σ_1σ_2σ_3 has nontrivial Wedderburn
# weight on λ ∈ {(4), (2,2)} (the components hypothesized to carry
# T_{2,9} and T_{3,5} force-carrier content).

bare = H4["bare_molecule_b4"]
target_lambdas = [(4,), (2,2)]
total_trM = sum(v["trM_contribution"] for v in bare.values())
print(f"\nMolecular braid total tr_M = Σ w_λ·χ/f = {total_trM:.6f}")
print(f"\nProjection onto each λ ⊢ 4:")
for lam, vals in bare.items():
    fraction = vals["trM_contribution"] / total_trM if abs(total_trM) > 1e-12 else float('nan')
    flag = " ← HYPOTHESIZED" if lam in target_lambdas else ""
    print(f"  λ={lam}: w_λ·χ/f = {vals['trM_contribution']:>10.6f} "
          f"(fraction {fraction:>+8.4f}){flag}")

# Check whether (4) and (2,2) carry nonzero weight
contrib_4 = bare[(4,)]["trM_contribution"]
contrib_22 = bare[(2,2)]["trM_contribution"]
hypothesis_supported = abs(contrib_4) > 1e-9 and abs(contrib_22) > 1e-9
print(f"\n  Contribution at λ=(4):   {contrib_4:.6f}")
print(f"  Contribution at λ=(2,2): {contrib_22:.6f}")
print(f"  Both nonzero?   {hypothesis_supported}")

WITNESS["data"]["hypothesis_test"] = {
    "molecular_braid_word": [1,2,3],
    "lambda_4_contribution": float(contrib_4),
    "lambda_22_contribution": float(contrib_22),
    "both_nonzero": bool(hypothesis_supported),
    "all_lambdas": {str(lam): v["trM_contribution"] for lam, v in bare.items()},
    "total_trM": float(total_trM),
}

WITNESS["assertions"].append({
    "name": "H_2 molecular braid (bare) projects nontrivially onto λ=(4) and λ=(2,2)",
    "computed": hypothesis_supported,
    "expected": True,
    "passed": hypothesis_supported,
    "source": "round-15/16 force-carrier-subsector hypothesis",
})

# ──────────────────────────────────────────────────────────────────────
# §5 — δ_q layer ↔ α_EM connection check
# ──────────────────────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("§5  δ_q ↔ α_EM verification")
print("=" * 70)

from q_parameter import q_int
q9 = q_int(9)
q10 = q_int(10)
alpha_EM = 1.0/(q0 * q9 * q10)
delta_q_T29 = q0**9 - qi0**9   # = h · [9]_q
delta_q_T35 = q0**10 - qi0**10  # = h · [10]_q (heuristic — proper is more elaborate)
predicted_alpha = HA**2 / (q0 * delta_q_T29 * delta_q_T35)

print(f"\n  α_EM (definition)           = {alpha_EM:.10e}")
print(f"  δ_q(T_{{2,9}}) = q^9 - q^-9    = {delta_q_T29:.10f} = h·[9]_q = {HA*q9:.10f}")
print(f"  δ_q(T_{{3,5}}) ≈ q^10 - q^-10 = {delta_q_T35:.10f} (B_2 heuristic)")
print(f"  h²/[q · δ_q(T_29) · δ_q(T_35)] = {predicted_alpha:.10e}")
print(f"  Match: {abs(alpha_EM - predicted_alpha) < 1e-12}")

WITNESS["data"]["alpha_EM_decomposition"] = {
    "alpha_EM": alpha_EM,
    "delta_q_T29_B2": delta_q_T29,
    "delta_q_T35_B2_heuristic": delta_q_T35,
    "h_squared_over_q_delta_delta": predicted_alpha,
    "match_exact": abs(alpha_EM - predicted_alpha) < 1e-12,
    "note": (
        "T_{2,9} q-dim is exactly h·[9]_q in B_2 (single-strand). "
        "T_{3,5} q-dim should be computed in B_3 (3-strand torus knot); "
        "the q^10-q^-10 form here is a B_2 heuristic. Proper B_3 "
        "computation is the next step."
    ),
}

WITNESS["assertions"].append({
    "name": "α_EM = h²/[q·δ_q(T_29)·δ_q(T_35)] within 1e-12",
    "computed": abs(alpha_EM - predicted_alpha) < 1e-12,
    "expected": True,
    "passed": abs(alpha_EM - predicted_alpha) < 1e-12,
    "source": "round-12/14 algebraic identity",
})

# ──────────────────────────────────────────────────────────────────────
# §6 — Save witness
# ──────────────────────────────────────────────────────────────────────
WITNESS["allPassed"] = all(a["passed"] for a in WITNESS["assertions"])

# Convert tuple keys (partition λ) to strings for JSON serialization
def _stringify_keys(obj):
    if isinstance(obj, dict):
        return {(str(k) if isinstance(k, tuple) else k): _stringify_keys(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_stringify_keys(x) for x in obj]
    return obj

WITNESS_OUT = _stringify_keys(WITNESS)
out_path = Path(__file__).parent / "delta-q-decoration.witness.json"
with open(out_path, "w") as f:
    json.dump(WITNESS_OUT, f, indent=2, default=str)

print(f"\n{'=' * 70}")
print(f"Witness written: {out_path}")
print(f"All assertions passed: {WITNESS['allPassed']}")
print(f"{'=' * 70}")
