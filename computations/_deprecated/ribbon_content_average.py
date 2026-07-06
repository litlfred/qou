#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
Compute ⟨c(λ)⟩_β for the deuteron atomic braid at H_6(q).

Per prop:chirality-writhe-ribbon-derivation, chirality factor is

    a_K(β) = 1 + w(β) · ⟨c(λ)⟩_β · h + O(h²)

where
    ⟨c(λ)⟩_β = Σ_λ w_λ · χ^λ(β) · c(λ) / Σ_λ w_λ · χ^λ(β)

with w_λ = dim_q(λ)²/[n]_q!, χ^λ the Hecke character of β via
Hoefsmit, and c(λ) = Σ_{x ∈ λ} (col(x) - row(x)).

Target: verify for D (A=2, n=6) that a_D ≈ 1 + h.

Writhe of atomic braid β_D:
  - proton word (H_3 slice): 7 crossings at gen 0 + 4 at gen 1
    = 7σ + 4σ⁻¹? Need to count positive vs negative.
    From proton_cross: all (c=1, d=0) = σ positive or (c=1, d=-h/2)
    = averaged.  Let me count exactly.
  - neutron word (H_3 slice): similar.
  - pn inter-nucleon: 1 crossing.

Writhe for atomic braid is the NET sum (positive - negative).
Averaged crossings contribute 0 to writhe.

Witness: ribbon-content-average.witness.json
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


def content_sum(partition):
    """c(λ) = Σ_{x ∈ λ} (col(x) - row(x))."""
    total = 0
    for r, row_len in enumerate(partition):
        for c in range(row_len):
            total += (c - r)
    return total


def writhe_of_atomic_braid(Z, N, include_inter=True):
    """Compute writhe of atomic braid = # σ - # σ^{-1}.
    Averaged crossings (½(σ + σ⁻¹)) contribute 0 to writhe."""
    crossings = atomic_braid_to_crossings(Z, N, include_inter)
    pos, neg, avg = 0, 0, 0
    for _, ct in crossings:
        if ct == "sigma":
            pos += 1
        elif ct == "sigma_inv":
            neg += 1
        else:
            avg += 1
    return pos - neg, pos, neg, avg


def chi_lambda_numeric(shape, crossings):
    sigmas, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return 0.0, 0
    is_sp = sp_sparse.issparse(sigmas[0]) if sigmas else False
    I = sp_sparse.eye(dim, format='csr') if is_sp else np.eye(dim)
    product = sp_sparse.eye(dim, format='csr') if is_sp else np.eye(dim)
    h_val = float(Q0 - 1.0 / Q0)
    d_for = {"sigma": 0.0, "sigma_inv": -h_val, "averaged": -h_val / 2}
    for gi, ct in crossings:
        if gi >= len(sigmas):
            raise IndexError
        M = sigmas[gi] + d_for[ct] * I
        product = product @ M
    return (float(product.diagonal().sum()) if is_sp
            else float(np.trace(product))), dim


def content_average(Z, N, include_inter=True):
    A = Z + N
    k = 3 * A
    nfac = qfac(k)
    crossings = atomic_braid_to_crossings(Z, N, include_inter)

    numerator = 0.0    # Σ w_λ · χ^λ · c(λ)
    denominator = 0.0  # Σ w_λ · χ^λ
    per_lam = []
    for shape in partitions_of(k):
        chi, d = chi_lambda_numeric(shape, crossings)
        if d == 0:
            continue
        d_q_val = float(dim_q(shape))
        w = d_q_val ** 2 / float(nfac)
        c = content_sum(shape)
        numerator += w * chi * c
        denominator += w * chi
        per_lam.append({
            "shape": shape, "c_lambda": c, "dim": d,
            "w_lambda": w, "chi_lambda": chi,
            "w_chi": w * chi,
            "w_chi_c": w * chi * c,
        })
    c_avg = numerator / denominator if denominator != 0 else 0.0
    return c_avg, numerator, denominator, per_lam


if __name__ == "__main__":
    print("RIBBON CONTENT AVERAGE ⟨c(λ)⟩_β FOR DEUTERON ATOMIC BRAID")
    print("=" * 80)
    print(f"q_0 = {Q0}")
    h_val = float(Q0 - 1.0 / Q0)
    print(f"h = q - q⁻¹ = {h_val:.6f}")
    print()

    for label, Z, N, include in [
        ("p free (A=1)",   1, 0, False),
        ("n free (A=1)",   0, 1, False),
        ("D atom (A=2)",   1, 1, True),
        ("D free (A=2)",   1, 1, False),
    ]:
        print(f"── {label} ──")
        w_net, p, n, avg = writhe_of_atomic_braid(Z, N, include)
        print(f"  writhe counts: {p} positive, {n} negative, {avg} averaged")
        print(f"  NET writhe w(β) = {w_net}")
        c_avg, num, den, per_lam = content_average(Z, N, include)
        print(f"  Σ w_λ · χ^λ · c(λ) = {num:+.6e}")
        print(f"  Σ w_λ · χ^λ       = {den:+.6e}")
        print(f"  ⟨c(λ)⟩_β          = {c_avg:+.6f}")
        if w_net != 0:
            a_K_leading = 1 + w_net * c_avg * h_val
            print(f"  predicted a_K = 1 + w · ⟨c⟩ · h = "
                  f"1 + {w_net}·{c_avg:.4f}·{h_val:.4f} "
                  f"= {a_K_leading:.4f}")
            print(f"  paper's D factor (1 + h) = {1 + h_val:.4f}")
        # Top contributors
        per_lam.sort(key=lambda x: -abs(x["w_chi_c"]))
        print(f"  top 5 contributors to Σ w_λ χ^λ c(λ):")
        for e in per_lam[:5]:
            print(f"    λ={e['shape']!s:<22} c={e['c_lambda']:+3d} "
                  f"w_χ={e['w_chi']:+.3e} w_χ·c={e['w_chi_c']:+.3e}")
        print()

    # Witness
    results = {}
    for label, Z, N, include in [
        ("p_free", 1, 0, False), ("n_free", 0, 1, False),
        ("D_atom", 1, 1, True), ("D_free", 1, 1, False),
    ]:
        w_net, p, n, avg = writhe_of_atomic_braid(Z, N, include)
        c_avg, num, den, per_lam = content_average(Z, N, include)
        results[label] = {
            "Z": Z, "N": N, "include_inter": include,
            "writhe_net": w_net, "writhe_pos": p, "writhe_neg": n,
            "writhe_avg": avg,
            "content_average_c": c_avg,
            "num_Σ_wχc": num, "den_Σ_wχ": den,
            "predicted_a_K_leading": 1 + w_net * c_avg * h_val,
            "per_lambda": per_lam,
        }

    witness = {
        "computation": "ribbon-content-average",
        "description": (
            "Computes ⟨c(λ)⟩_β for atomic braids at H_{3A}(q), "
            "needed for the chirality-writhe-ribbon derivation "
            "(prop:chirality-writhe-ribbon-derivation). Verifies "
            "whether a_K = 1 + w(β)·⟨c⟩·h matches paper's assignment "
            "(e.g., 1+h for D)."
        ),
        "reference_blocks": [
            "prop:chirality-writhe-ribbon-derivation",
            "prop:chirality-from-frobenius-self-pairing",
            "prop:figure-eight-bw-coefficients",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(Q0), "h": h_val,
            "paper_D_chirality_factor": 1 + h_val,
        },
        "results": results,
    }
    out = Path(__file__).parent / "ribbon-content-average.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"Witness: {out}")
