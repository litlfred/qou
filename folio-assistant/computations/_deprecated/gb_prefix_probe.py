#!/usr/bin/env python3
"""
GB-filtration-indexed prefix probe for Term 6.

Per prop:jet-prefix-gb-filtration, the atomic braid prefix is

    β_k^GS := σ_{k-3}(T_w) ∈ J^{k-3}(q) / J^{k-2}(q)

projecting onto the k-th GB filtration stratum rather than a
geometric cutoff.  This script approximates the filtration
projection numerically by using the confinement-level sort of
partitions at H_{3A}.

Approach:
  1. For each isotope, enumerate partitions λ ⊢ 3A.
  2. Sort partitions by "filtration level" ℓ(λ) =
     (rows - 1) + (max-col - 1) — a rough approximation
     to confinement level based on diagram height/width.
  3. At each level k, compute the numerator/denominator:
        num_k = Σ_{λ: ℓ(λ)=k} w_λ · χ^λ(β)
        den_k = Σ_{λ: ℓ(λ)=k} w_λ · dim(Res^{H_k}_{H_3} V_λ)
  4. Compute a_k = num_k / den_k per level.
  5. Product ∏_k a_k gives the Term 6 candidate.

Compares against:
  - Upstream's failed conventions (nucleon-cumulative, strand-cum,
    gen-bounded)
  - The target: paper's BW+χ binding predictions

Witness: gb-prefix-probe.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
from scipy import sparse as sp_sparse

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0
from hecke_characters import (
    partitions_of, build_seminormal_matrices, qfac, dim_q,
)
from hecke_character_symbolic import atomic_braid_to_crossings


def gb_filtration_level(partition):
    """Approximate filtration level: rows-1 + (max_col-1).

    For n=3: (3)→0+2=2, (2,1)→1+1=2, (1,1,1)→2+0=2. All same.
    Need finer — try rows·max_col/p_sum.

    Alternative: level = # distinct row lengths (more topological).
    For (3)→1, (2,1)→2, (1,1,1)→1. Differentiates.

    Cleanest: level = (# rows) - 1 (height of diagram).
    For (3)→0, (2,1)→1, (1,1,1)→2. Matches §2 of prop.
    """
    return len(partition) - 1


def chi_lambda_numeric(shape, crossings):
    """χ^λ(T_w) via numerical Hoefsmit."""
    sigmas, dim, _syts = build_seminormal_matrices(shape)
    if dim == 0:
        return 0.0, 0
    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    I = sp_sparse.eye(dim, format='csr') if is_sparse else np.eye(dim)
    product = sp_sparse.eye(dim, format='csr') if is_sparse else np.eye(dim)
    h_val = float(Q0 - 1.0 / Q0)
    d_for = {"sigma": 0.0, "sigma_inv": -h_val, "averaged": -h_val / 2}
    for gen_idx, cross_type in crossings:
        if gen_idx >= len(sigmas):
            raise IndexError(f"gen {gen_idx} ≥ {len(sigmas)}")
        M = sigmas[gen_idx] + d_for[cross_type] * I
        product = product @ M
    chi = float(product.diagonal().sum()) if is_sparse else float(np.trace(product))
    return chi, dim


def gb_prefix_product(Z, N, include_inter=True):
    """Compute Π_k a_k where a_k = num_k/den_k with filtration-indexed sum."""
    A = Z + N
    k = 3 * A
    crossings = atomic_braid_to_crossings(Z, N, include_inter)
    nfac = qfac(k)

    # Group partitions by filtration level
    by_level = {}
    for shape in partitions_of(k):
        lvl = gb_filtration_level(shape)
        by_level.setdefault(lvl, []).append(shape)

    # Per level: sum w_λ χ^λ for all λ at that level
    per_level = []
    a_product = 1.0
    for lvl in sorted(by_level):
        num_lvl = 0.0
        den_lvl = 0.0
        for shape in by_level[lvl]:
            chi, d = chi_lambda_numeric(shape, crossings)
            if d == 0:
                continue
            d_q_val = float(dim_q(shape))
            w = d_q_val ** 2 / float(nfac)
            num_lvl += w * chi
            # Restriction dim: Res^{H_k}_{H_3}(V_λ) classically has
            # dimension = dim(λ) (just the classical dimension).
            den_lvl += w * d
        a_k = num_lvl / den_lvl if den_lvl != 0 else 0.0
        per_level.append({
            "level": lvl,
            "partitions": [str(s) for s in by_level[lvl]],
            "num_k": num_lvl,
            "den_k": den_lvl,
            "a_k": a_k,
        })
        if abs(a_k) > 1e-15:
            a_product *= a_k
    return a_product, per_level


if __name__ == "__main__":
    print("GB-FILTRATION-INDEXED PREFIX PROBE")
    print("=" * 80)
    print(f"q_0 = {Q0}")
    print(f"Level heuristic: ℓ(λ) = len(λ) - 1 (# rows - 1)")
    print()

    ISOTOPES = [("p", 1, 0), ("n", 0, 1), ("D", 1, 1), ("T", 1, 2),
                ("3He", 2, 1)]
    rows = []
    for label, Z, N in ISOTOPES:
        A = Z + N
        k = 3 * A
        print(f"── {label} (A={A}, n={k}) ──")
        if A == 1:
            a_free_prod, free_levels = gb_prefix_product(Z, N, include_inter=False)
            a_atom_prod = a_free_prod  # no atom structure at A=1
        else:
            a_free_prod, free_levels = gb_prefix_product(Z, N, include_inter=False)
            a_atom_prod, atom_levels = gb_prefix_product(Z, N, include_inter=True)

        print(f"  free prod Π a_k = {a_free_prod:+.6e}")
        if A >= 2:
            print(f"  atom prod Π a_k = {a_atom_prod:+.6e}")
            print(f"  ratio free/atom = {a_free_prod/a_atom_prod:+.4e}"
                  if a_atom_prod != 0 else "  atom = 0")

        print(f"  free per-level (top 3 by |a_k|):")
        sorted_levels = sorted(free_levels, key=lambda x: -abs(x['a_k']))[:3]
        for lvl in sorted_levels:
            print(f"    ℓ={lvl['level']}: num={lvl['num_k']:+.3e} "
                  f"den={lvl['den_k']:+.3e} a_k={lvl['a_k']:+.3e}")

        rows.append({
            "isotope": label, "Z": Z, "N": N, "A": A, "k": k,
            "a_free_product": a_free_prod,
            "a_atom_product": a_atom_prod if A >= 2 else a_free_prod,
            "free_per_level": free_levels,
        })
        print()

    witness = {
        "computation": "gb-prefix-probe",
        "description": (
            "GB-filtration-indexed prefix product for Term 6. "
            "Groups partitions λ ⊢ 3A by confinement-filtration "
            "level ℓ(λ) = (len λ) - 1, computes per-level a_k = "
            "Σ w_λ χ^λ(β) / Σ w_λ dim(λ), takes the product over "
            "levels. Tests whether this algebraically-natural prefix "
            "reproduces a structure matching paper's BW+χ bindings."
        ),
        "reference_blocks": [
            "prop:jet-prefix-gb-filtration",
            "prop:spectral-sequence-h3-explicit",
            "prop:e-infinity-page-identifications",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(Q0),
            "filtration_level_heuristic": "len(lambda) - 1",
        },
        "rows": rows,
    }
    out = Path(__file__).parent / "gb-prefix-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"Witness: {out}")
