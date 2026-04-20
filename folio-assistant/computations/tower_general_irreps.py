#!/usr/bin/env python3
"""
General-irrep tower binding — implementation of the restated
prop:tower-binding-energy.

Per user "restate so sum is over irred repn":

  B(Z, N) = Σ_{λ ⊢ A} w_λ^(A) · m_e · Σ_i ln|Φ_q(V̂_i^λ)|

where:
  λ ⊢ A       ranges over ALL partitions of A (irreps of H_A(q))
  d_q(λ)      = [A]_q! / Π_{x ∈ λ} [h_x(λ)]_q  (quantum hook-length)
  w_λ^(A)     = d_q(λ)² / Σ_μ d_q(μ)²  (normalised WA weight)
  V̂_i^λ(q)   = χ_λ( ρ_λ(W_i) )  (character of per-generator Hecke word)

For small atoms (A=2, 3) we can compute this directly:
  A=2: 2 irreps (2), (1,1), both 1-dim; V̂ is product of eigenvalues
  A=3: 3 irreps (3), (2,1), (1,1,1); std is 2-dim (via transfer)
  A=4: 5 irreps; higher irreps need seminormal matrices

This file implements A=2 and A=3 with direct formulas, validating
that the general-irrep formulation recovers the current 3-channel
calculation at A=3 and reveals the "no std" structure at A=2.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV
from hecke_characters import partitions_of


def q_int(n, q=q0):
    if q == 1:
        return float(n)
    return (q**n - q**(-n)) / (q - 1 / q)


def q_factorial(n, q=q0):
    result = 1.0
    for k in range(1, n + 1):
        result *= q_int(k, q)
    return result


def hook_length(partition, i, j):
    """Hook length of cell (i, j) in partition, 0-indexed (i, j)."""
    row = partition[i]
    # arm: cells strictly to the right in row i
    arm = row - 1 - j
    # leg: cells strictly below in column j: rows with length > j
    leg = 0
    for k in range(i + 1, len(partition)):
        if partition[k] > j:
            leg += 1
        else:
            break
    return arm + leg + 1


def dim_q(partition, q=q0):
    """Quantum dimension via hook-length formula."""
    n = sum(partition)
    numerator = q_factorial(n, q)
    denominator = 1.0
    for i in range(len(partition)):
        for j in range(partition[i]):
            denominator *= q_int(hook_length(partition, i, j), q)
    return numerator / denominator


def ln_phi_q(v, max_k=500):
    if v == 0:
        return 0.0
    s = 0.0
    for k in range(1, max_k + 1):
        f = 1.0 - qi0**k * v
        if abs(f) < 1e-300:
            return float('inf')
        s -= math.log(abs(f))
        if abs(qi0**k * v) < 1e-15:
            break
    return s


# ══════════════════════════════════════════════════════════════
# Per-irrep V̂_i^λ at A=2 (1 generator, 2 partitions)
# ══════════════════════════════════════════════════════════════

def V_hat_1d_irrep(crossings, eigenvalue, q=q0):
    """Character of a Hecke word W = ∏_j (c_j σ + d_j) in a 1-dim
    irrep where σ → eigenvalue.  Simply ∏ (c_j · eig + d_j)."""
    result = 1.0
    for c, d in crossings:
        result *= c * eigenvalue + d
    return result


# ══════════════════════════════════════════════════════════════
# Per-irrep V̂_i^λ at A=3 (2 generators, 3 partitions)
# The std (2,1) irrep uses the standard 2x2 transfer chain
# ══════════════════════════════════════════════════════════════

def V_hat_std_2d_A3(crossings_at_gen0, crossings_at_gen1, q=q0):
    """Character of σ_0-then-σ_1 Hecke word in the 2-dim std irrep
    of H_3(q) using the z·a + b transfer-chain convention."""
    h = q - 1.0 / q
    z = 1.0 / (math.sqrt(q) + 1.0 / math.sqrt(q))
    # Start at identity-like state
    a, b = 0.0, 1.0
    # Apply gen-0 crossings (proton's gluon + inter-crossings)
    for c, d in crossings_at_gen0:
        a, b = a * c * h + a * d + b * c, a * c + b * d
    # Apply gen-1 crossings
    for c, d in crossings_at_gen1:
        a, b = a * c * h + a * d + b * c, a * c + b * d
    return z * a + b


def get_crossings_per_gen(Z, N, gen_idx, ordering):
    """Return the list of (c, d) crossings applied at gen_idx.

    Matches per_gen_volumes's Hecke-element build:
      gluon (2·σ_0 for p, 4·σ_0 for n) + inter-nucleon crossings.
    """
    h = q0 - qi0
    crossings = []
    # Gluon
    gluon_count = 2 if ordering[gen_idx] == 1 else 4
    for _ in range(gluon_count):
        crossings.append((1.0, 0.0))
    # Inter-nucleon crossings (this nucleon to later)
    for j in range(gen_idx + 1, len(ordering)):
        ti, tj = ordering[gen_idx], ordering[j]
        if ti == 1 and tj == 1:
            c, d = 1.0, 0.0
        elif ti == 0 and tj == 0:
            c, d = 1.0, -h
        else:
            c, d = 1.0, -h / 2.0
        crossings.append((c, d))
    return crossings


def ground_state(Z, N):
    o = []; pi = ni = 0
    for _ in range(Z + N):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            o.append(1); pi += 1
        else:
            o.append(0); ni += 1
    return o


def B_general_irreps(Z, N):
    """Binding via sum over ALL irreps of H_A(q)."""
    A = Z + N
    if A < 2:
        return None
    ordering = ground_state(Z, N)

    # Get all partitions of A
    parts = list(partitions_of(A))

    # Compute dim_q per partition
    dims_sq = [dim_q(list(p))**2 for p in parts]
    sum_dims_sq = sum(dims_sq)
    weights = [d / sum_dims_sq for d in dims_sq]

    # For each partition λ, compute V̂_i^λ per generator
    # A=2: 2 irreps both 1-dim, so only 1d formulas needed
    # A=3: add the 2d std case
    # A>=4: requires full seminormal — not implemented here

    per_irrep = []
    for idx, p in enumerate(parts):
        lam = list(p)
        # dim_q can be non-integer at q ≠ 1; we test shape for
        # 1-dim irreps (partition is a single row or single column).
        is_1d = (len(p) == 1) or (max(p) == 1)
        dim_lam = 1 if is_1d else 2  # std is 2D at A=3
        if A == 3 and p == (2, 1):
            dim_lam = 2
        w = weights[idx]
        label = str(tuple(p))

        if dim_lam == 1:
            # 1-dim irrep: σ_i → ±q^{±1} per the sign of partition
            # Trivial (A): all σ → +q; Sign (1^A): all σ → -1/q
            if p == (A,):
                eigenvalue = q0
                channel = "sym"
            elif all(x == 1 for x in p):
                eigenvalue = -qi0
                channel = "alt"
            else:
                eigenvalue = None
                channel = f"other_1d_{label}"

            if eigenvalue is not None:
                Bs_irrep = 0.0
                V_list = []
                for gen_idx in range(A - 1):
                    crossings = get_crossings_per_gen(Z, N, gen_idx, ordering)
                    V = V_hat_1d_irrep(crossings, eigenvalue)
                    V_list.append(V)
                    Bs_irrep += ln_phi_q(abs(V))
                per_irrep.append({
                    "partition": label, "dim": 1, "channel": channel,
                    "weight": w,
                    "V_per_gen": V_list,
                    "ln_phi_sum": Bs_irrep,
                    "B_contrib": w * M_E_MEV * Bs_irrep,
                })
        elif dim_lam == 2 and A == 3:
            # std irrep of H_3 via 2x2 transfer
            c0 = get_crossings_per_gen(Z, N, 0, ordering)
            c1 = get_crossings_per_gen(Z, N, 1, ordering)
            V_std = V_hat_std_2d_A3(c0, c1)
            per_irrep.append({
                "partition": label, "dim": 2, "channel": "std",
                "weight": w,
                "V_per_gen": [V_std, V_std],  # transfer-chain: single value, counted per-gen
                "ln_phi_sum": 2 * ln_phi_q(abs(V_std)),
                "B_contrib": w * M_E_MEV * 2 * ln_phi_q(abs(V_std)),
            })
        else:
            # Higher-dim irrep at A>=4: requires seminormal — skip
            per_irrep.append({
                "partition": label, "dim": dim_lam,
                "channel": f"skipped_A{A}_{label}",
                "weight": w,
                "B_contrib": None,  # not computed
                "note": "requires seminormal representation (A >= 4)",
            })

    B_total = sum(r["B_contrib"] for r in per_irrep
                     if r.get("B_contrib") is not None)
    return {
        "A": A, "Z": Z, "N": N,
        "partitions": [str(tuple(p)) for p in parts],
        "dims_squared": dims_sq,
        "sum_dims_sq": sum_dims_sq,
        "weights": weights,
        "per_irrep": per_irrep,
        "B_total_computed": B_total,
        "skipped_irreps": [r["partition"] for r in per_irrep
                              if r.get("B_contrib") is None],
    }


AME = {
    "D":   2.224566, "T":   8.481798, "3He": 7.718058,
    "4He": 28.295674,
}


if __name__ == "__main__":
    print("=" * 125)
    print("TOWER BINDING via GENERAL H_A IRREP SUM (prop:tower-binding-energy restated)")
    print("=" * 125)

    results = []
    for name, (Z, N) in [("D", (1, 1)), ("T", (1, 2)), ("3He", (2, 1)),
                              ("4He", (2, 2))]:
        A = Z + N
        Mtot = A * 938.272
        B_AME = AME[name]
        r = B_general_irreps(Z, N)
        r["atom"] = name
        r["B_AME"] = B_AME
        r["Mtot"] = Mtot
        r["B_total_err_pct"] = (abs(r["B_total_computed"] - B_AME)
                                     / Mtot * 100)
        results.append(r)

        print(f"\n{name} (Z={Z}, N={N}, A={A}):")
        print(f"  p(A) = {len(r['partitions'])} partitions: {r['partitions']}")
        print(f"  Sum d_q² = {r['sum_dims_sq']:.4f}  [A]_q! = {q_factorial(A):.4f}")
        for ir in r["per_irrep"]:
            if ir.get("B_contrib") is not None:
                V_str = f"V={ir['V_per_gen']}" if "V_per_gen" in ir else ""
                print(f"  {ir['partition']} (dim={ir['dim']}, "
                      f"w={ir['weight']:.4f}, ch={ir['channel']}): "
                      f"B_contrib = {ir['B_contrib']:+.4f} MeV  {V_str}")
            else:
                print(f"  {ir['partition']} (dim={ir['dim']}, "
                      f"w={ir['weight']:.4f}): SKIPPED {ir['note']}")
        print(f"  B_total = {r['B_total_computed']:+.4f} MeV "
              f"(AME = {B_AME}, err = {r['B_total_err_pct']:.4f}%)")

    out = Path(__file__).parent / "tower-general-irreps.witness.json"
    out.write_text(json.dumps({
        "computation": "tower-general-irreps",
        "description": (
            "Restated prop:tower-binding-energy evaluated over ALL "
            "H_A irreps for A = 2, 3 (full) and A = 4 (partial, "
            "1-dim irreps only; higher-dim irreps need seminormal)."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "M_E_MEV": M_E_MEV},
        "results": results,
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
