#!/usr/bin/env python3
"""
Exact derivation of ρ(λ, A) — three tasks:

Task 1: Compute ρ(std, 3) via pair-term evaluation for T and 3He.
        Predicted schematic:
          ρ ≈ 1 - z²·ln|Φ_q(V̂_0 V̂_1)| / Σ ln|Φ_q(V̂_i)|
        Compare to empirical 0.07 (T), 0.25 (3He).

Task 2: Structure the doubly-magic enhancement ρ(std, 4) = 1.77
        conjecture — compute the std characters for 4He via
        seminormal matrices and look for the resonance signature.

Task 3: Extend to all H_4 irreps using seminormal matrices from
        mass_at_3A_proper._cached_seminormal. Compute per-gen
        characters and binding contributions for 4He to see
        if sub-leading irreps (3,1), (2,2), (2,1,1) contribute
        to the AME match.
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
from mass_at_3A_proper import _cached_seminormal

q_sym = sp.Symbol('q', positive=True)
HA_sym = q_sym - 1 / q_sym
z_sym = 1 / (sp.sqrt(q_sym) + 1 / sp.sqrt(q_sym))

qint2 = (q0**2 - qi0**2) / (q0 - qi0)
W_SYM = 1.0 / (qint2**2 + 2)
W_STD = qint2**2 / (qint2**2 + 2)
W_ALT = W_SYM
z_markov = 1.0 / (math.sqrt(q0) + 1.0 / math.sqrt(q0))


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


def crossing_coeffs(ti, tj):
    h = q0 - qi0
    if ti == 1 and tj == 1:
        return (1.0, 0.0)
    elif ti == 0 and tj == 0:
        return (1.0, -h)
    else:
        return (1.0, -h / 2.0)


def per_gen_volumes_std_A3(gen_idx, ordering):
    """At A=3, return V̂_std as a scalar for a single generator's
    transfer chain."""
    h = q0 - qi0
    z = z_markov
    a, b = 0.0, 1.0
    A = len(ordering)
    gluon_count = 2 if ordering[gen_idx] == 1 else 4
    for _ in range(gluon_count):
        c, d = 1.0, 0.0
        a, b = a * c * h + a * d + b * c, a * c + b * d
    for j in range(gen_idx + 1, A):
        c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
        a, b = a * c * h + a * d + b * c, a * c + b * d
    return z * a + b


def ground_state(Z, N):
    o = []; pi = ni = 0
    for _ in range(Z + N):
        if pi < Z and (ni >= N or pi / max(Z, 1) <= ni / max(N, 1)):
            o.append(1); pi += 1
        else:
            o.append(0); ni += 1
    return o


# ══════════════════════════════════════════════════════════════
# TASK 1: Exact ρ(std, 3) via pair term
# ══════════════════════════════════════════════════════════════

def rho_std_A3(Z, N):
    """Compute schematic ρ(std, 3) = 1 - pair_term/singleton_sum."""
    A = Z + N
    if A != 3:
        return None
    ordering = ground_state(Z, N)
    V_0 = per_gen_volumes_std_A3(0, ordering)
    V_1 = per_gen_volumes_std_A3(1, ordering)
    singleton_sum = ln_phi_q(abs(V_0)) + ln_phi_q(abs(V_1))
    pair_term = z_markov**2 * ln_phi_q(abs(V_0 * V_1))
    rho_schematic = 1.0 - pair_term / singleton_sum if singleton_sum != 0 else None
    return {
        "V_0": V_0, "V_1": V_1, "V_0_times_V_1": V_0 * V_1,
        "ln_Phi_V_0": ln_phi_q(abs(V_0)),
        "ln_Phi_V_1": ln_phi_q(abs(V_1)),
        "singleton_sum": singleton_sum,
        "pair_term": pair_term,
        "z_markov_sq": z_markov**2,
        "rho_schematic": rho_schematic,
    }


# ══════════════════════════════════════════════════════════════
# TASK 3: Seminormal matrices for all H_4 irreps
# ══════════════════════════════════════════════════════════════

def atom_braid_word_H_A(Z, N, ordering):
    """Build the H_A(q) Hecke element for the atom.
    Returns a list of (c, d, gen_idx) tuples."""
    A = len(ordering)
    h = q0 - qi0
    word = []
    for gen_idx in range(A - 1):
        # Gluon at gen_idx
        gluon_count = 2 if ordering[gen_idx] == 1 else 4
        for _ in range(gluon_count):
            word.append((1.0, 0.0, gen_idx))
        # Inter-nucleon crossings from gen_idx to later (at gen_idx)
        for j in range(gen_idx + 1, A):
            c, d = crossing_coeffs(ordering[gen_idx], ordering[j])
            word.append((c, d, gen_idx))
    return word


def character_in_irrep(word, shape, A):
    """Character of a Hecke word in the irrep indexed by `shape`."""
    try:
        sigmas, dim, _ = _cached_seminormal(tuple(shape))
    except Exception as e:
        return None, None
    if dim == 0:
        return None, None
    # Build matrix product
    from scipy.sparse import issparse, eye as speye
    sparse = bool(sigmas) and issparse(sigmas[0])
    if sparse:
        prod = speye(dim, format='csr')
        I = speye(dim, format='csr')
    else:
        prod = np.eye(dim)
        I = np.eye(dim)
    for (c, d, gen) in word:
        if gen >= len(sigmas):
            continue
        prod = prod @ (c * sigmas[gen] + d * I)
    if sparse:
        chi = float(prod.diagonal().sum())
    else:
        chi = float(np.trace(prod))
    return chi, dim


def hook_length(partition, i, j):
    row = partition[i]
    arm = row - 1 - j
    leg = 0
    for k in range(i + 1, len(partition)):
        if partition[k] > j:
            leg += 1
        else:
            break
    return arm + leg + 1


def q_int(n):
    if n == 0:
        return 0.0
    return (q0**n - q0**(-n)) / (q0 - qi0)


def dim_q(partition):
    n = sum(partition)
    numerator = 1.0
    for k in range(1, n + 1):
        numerator *= q_int(k)
    denominator = 1.0
    for i in range(len(partition)):
        for j in range(partition[i]):
            denominator *= q_int(hook_length(partition, i, j))
    return numerator / denominator


def B_H4_all_irreps(Z, N):
    """For 4He (or any A=4), compute contribution from each of
    5 irreps using seminormal matrices. Report per-irrep B."""
    A = Z + N
    if A != 4:
        return None
    ordering = ground_state(Z, N)
    word = atom_braid_word_H_A(Z, N, ordering)
    parts = list(partitions_of(A))
    dims_sq_list = [dim_q(list(p))**2 for p in parts]
    total_dims_sq = sum(dims_sq_list)
    weights = [d / total_dims_sq for d in dims_sq_list]

    contribs = []
    for idx, p in enumerate(parts):
        chi, dim = character_in_irrep(word, list(p), A)
        if chi is None:
            contribs.append({"partition": str(tuple(p)), "error": "no seminormal"})
            continue
        V_lambda = chi / dim  # average per-dim character
        B_contrib = weights[idx] * M_E_MEV * ln_phi_q(abs(V_lambda))
        contribs.append({
            "partition": str(tuple(p)),
            "dim_q_squared": dims_sq_list[idx],
            "weight": weights[idx],
            "dim": dim,
            "chi_full": chi,
            "V_lambda_avg": V_lambda,
            "ln_Phi_V_lambda": ln_phi_q(abs(V_lambda)),
            "B_contrib_MeV": B_contrib,
        })
    return {
        "A": A, "Z": Z, "N": N,
        "contribs": contribs,
        "total_dims_sq": total_dims_sq,
        "B_total_from_partitions": sum(
            c.get("B_contrib_MeV", 0) for c in contribs),
    }


AME = {"T": 8.481798, "3He": 7.718058, "4He": 28.295674}


if __name__ == "__main__":
    print("=" * 125)
    print("ρ(λ, A) EXACT DERIVATION")
    print("=" * 125)

    # Task 1: ρ(std, 3) schematic for T, 3He
    print("\n--- TASK 1: ρ(std, 3) schematic via pair-term ---")
    print(f"  z_markov^2 = {z_markov**2:.6f}")
    results_task1 = {}
    for name, Z, N in [("T", 1, 2), ("3He", 2, 1)]:
        r = rho_std_A3(Z, N)
        print(f"\n  {name} (Z={Z}, N={N}):")
        print(f"    V^std_0 = {r['V_0']:+.6f}")
        print(f"    V^std_1 = {r['V_1']:+.6f}")
        print(f"    V_0 · V_1 = {r['V_0_times_V_1']:+.6f}")
        print(f"    ln|Phi_q(V_0)| = {r['ln_Phi_V_0']:.4f}")
        print(f"    ln|Phi_q(V_1)| = {r['ln_Phi_V_1']:.4f}")
        print(f"    singleton sum = {r['singleton_sum']:.4f}")
        print(f"    pair term z^2·ln|Phi_q(V_0·V_1)| = {r['pair_term']:.4f}")
        print(f"    rho_schematic = 1 - pair/singleton = {r['rho_schematic']:+.4f}")
        empirical = 0.0655 if name == "T" else 0.2464
        print(f"    empirical ρ(std, 3) = {empirical:+.4f}")
        results_task1[name] = r

    # Task 3: Seminormal-matrix all-irreps at 4He
    print("\n\n--- TASK 3: 4He per-irrep contribution via seminormal ---")
    r4 = B_H4_all_irreps(2, 2)
    if r4:
        print(f"  Total dims_q^2 = {r4['total_dims_sq']:.4f}")
        print(f"  {'partition':>15} {'dim':>4} {'weight':>8} "
              f"{'V_λ_avg':>10} {'ln|Φ_q|':>10} {'B_contrib':>12}")
        print("  " + "-" * 75)
        for c in r4["contribs"]:
            if "error" in c:
                print(f"  {c['partition']:>15}  ERR")
                continue
            print(f"  {c['partition']:>15} {c['dim']:>4} "
                  f"{c['weight']:>8.4f} "
                  f"{c['V_lambda_avg']:>+10.4f} {c['ln_Phi_V_lambda']:>10.4f} "
                  f"{c['B_contrib_MeV']:>+12.4f}")
        print(f"\n  B_total from all 5 irreps (seminormal): "
              f"{r4['B_total_from_partitions']:+.4f} MeV")
        print(f"  AME 4He = {AME['4He']}")
        err = abs(r4['B_total_from_partitions'] - AME['4He']) / (4*938.272) * 100
        print(f"  err = {err:.4f}%")

    # Task 2: Doubly-magic enhancement structure
    print("\n\n--- TASK 2: Doubly-magic ρ(std, 4) = 1.77 structural analysis ---")
    print(f"  At A=4, std = (3, 1). dim_q((3,1)) = [3]_q = {q_int(3):.6f}")
    print(f"  At A=4, other 3 multi-dim irreps: (2,2), (2,1,1)")
    print(f"    dim_q((2,2)) = {dim_q([2,2]):.4f}")
    print(f"    dim_q((2,1,1)) = {dim_q([2,1,1]):.4f}")
    print(f"  If std resonance = ratio of (empirical ρ)/(theoretical ρ=1):")
    print(f"    1.77 / 1 = 1.77 boost")
    print(f"  Conjecture: at doubly-magic, the (3,1) matrix R-factor")
    print(f"  violates the 1+O(ℏ_q²) bound due to shell-closure resonance.")

    out = Path(__file__).parent / "rho-exact-derivation.witness.json"
    out.write_text(json.dumps({
        "computation": "rho-exact-derivation",
        "description": "Tasks 1, 2, 3: derivation of ρ(λ, A).",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "task1_rho_std_A3": {k: {kk: float(vv) if isinstance(vv, (int, float)) else vv
                                      for kk, vv in v.items()}
                                   for k, v in results_task1.items()},
        "task3_A4_all_irreps": r4 if r4 else {},
    }, indent=2, default=str))
    print(f"\nWitness: {out}")
