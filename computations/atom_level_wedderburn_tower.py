#!/usr/bin/env python3
"""
ATOM-LEVEL Wedderburn tower (λ ⊢ 3A, NOT per-generator H_3 projection).

⚠ SUPERSEDED for production tr_M (2026-06-15) — kept as a cross-check.
    This is the BRUTE-FORCE atom-level path: it materialises the full
    Hoefsmit seminormal V_λ for every λ ⊢ 3A (O(d_λ) per partition, with
    d_λ ~ 1.6×10⁷ at n=18 — the 3.6-year ⁶Li wall). The canonical
    production tr_M(β_atom) = Σ_λ y_λ χ^λ is now computed by the
    fine-Bratteli TRANSFER MATRIX (tr_m_atom_via_transfer.tr_m_atom_zn →
    chi_monotone_transfer), which is LOSSLESS (all p(3A) partitions, same
    convention, 50 dps) but NEVER forms a d_λ×d_λ matrix: ⁶Li in ~0.16 s
    vs this script's wall. binding_canonical and canonical_tr_m_via_
    branching both route through the transfer path. Use THIS script only
    as an independent d_λ-explicit cross-check of the transfer χ^λ on
    small A — do not wire it into a production binding pipeline.

Per user directive: use atom-level Wedderburn decomposition rather
than per-generator H_3 projection.  The atomic braid 𝒜 ∈ H_{3A}(q)
decomposes via Wedderburn at level 3A:

  H_{3A}(q) = ⊕_{λ ⊢ 3A} M_{f^λ}(R)

with weights w_λ = dim_q(λ)² / [3A]_q!.

For each λ:
  - Hoefsmit seminormal representation gives σ_i action on V_λ
  - χ^λ(𝒜) = trace of atomic braid in V_λ
  - tr_M(𝒜) = Σ_λ w_λ · χ^λ(𝒜) / f^λ

Atom-level brane tower (proposed):
  Term 2_atom = Σ_{λ ⊢ 3A} w_λ · Φ_q(|χ^λ(𝒜)| / f^λ)

GB filtration scaling: each λ has filtration level ℓ(λ) = height(λ)−1.
Sum weights by GB level, scaling by z^ℓ.

Witness: atom-level-wedderburn-tower.witness.json
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_characters import (
    partitions_of, build_seminormal_matrices, qfac, dim_q,
)
from hecke_character_symbolic import atomic_braid_to_crossings
from hecke_core import Phi_q
from syt_prefix_cache import (
    BlockCache,
    build_seminormal_matrices_cached,
)

# Shared BlockCache for P21 compute-audit compliance — avoids
# rebuilding Hoefsmit content-distance tables per shape at large n.
_BLOCK_CACHE = BlockCache(float(Q0_FLOAT),
                          float(Q0_FLOAT - 1.0 / Q0_FLOAT))


Q0 = Q_MP  # was f64 roundtrip


def chi_lambda_atom(shape, crossings):
    """χ^λ(atomic braid) via numerical Hoefsmit + crossing product."""
    sigmas, dim, _ = build_seminormal_matrices_cached(
        shape, cache=_BLOCK_CACHE)
    if dim == 0:
        return 0.0, 0
    from scipy import sparse as sp_sparse
    is_sp = sp_sparse.issparse(sigmas[0]) if sigmas else False
    I = sp_sparse.eye(dim, format='csr') if is_sp else np.eye(dim)
    prod = sp_sparse.eye(dim, format='csr') if is_sp else np.eye(dim)
    h_val = float(Q0_FLOAT) - 1.0 / float(Q0_FLOAT)
    d_for = {"sigma": 0.0, "sigma_inv": -h_val, "averaged": -h_val / 2}
    for gen_idx, ct in crossings:
        if gen_idx >= len(sigmas):
            raise IndexError
        M = sigmas[gen_idx] + d_for[ct] * I
        prod = prod @ M
    return (float(prod.diagonal().sum()) if is_sp
            else float(np.trace(prod))), dim


def height_level(partition):
    return len(partition) - 1


def atom_level_tower(Z, N, include_inter=True, with_phi_q=True):
    """Compute atom-level Wedderburn tower.
    Returns dict with descended trace, sum-of-Φ_q over partitions,
    and per-level breakdown by height."""
    A = Z + N
    k = 3 * A
    nfac = qfac(k)
    crossings = atomic_braid_to_crossings(Z, N, include_inter=include_inter)

    descended = 0.0
    phi_q_atom_sum = 0.0
    by_level = {}
    per_lambda = []

    for shape in partitions_of(k):
        chi, d = chi_lambda_atom(shape, crossings)
        if d == 0:
            continue
        d_q_val = float(dim_q(shape))
        w_lambda = d_q_val ** 2 / float(nfac)
        # Markov contribution
        mc = w_lambda * chi / d
        descended += mc
        # Brane tower (atom-level) candidate: Φ_q(|χ^λ|/d)
        if with_phi_q and abs(chi) > 1e-20:
            try:
                phi_arg = mp.mpf(abs(chi) / d)
                phi = float(Phi_q(phi_arg))
                if not (mp.isinf(phi) or mp.isnan(phi)):
                    phi_q_atom_sum += w_lambda * phi
            except Exception:
                pass
        lvl = height_level(shape)
        by_level.setdefault(lvl, {"count": 0, "sum_w_chi": 0.0,
                                    "sum_phi_q": 0.0})
        by_level[lvl]["count"] += 1
        by_level[lvl]["sum_w_chi"] += mc
        if with_phi_q and abs(chi) > 1e-20:
            try:
                phi = float(Phi_q(mp.mpf(chi / d)))
                if not (mp.isinf(phi) or mp.isnan(phi)):
                    by_level[lvl]["sum_phi_q"] += w_lambda * phi
            except Exception:
                pass
        per_lambda.append({
            "shape": shape, "level": lvl, "dim": d,
            "w_lambda": w_lambda, "chi_lambda": chi,
            "markov_contrib": mc,
        })

    return descended, phi_q_atom_sum, by_level, per_lambda


if __name__ == "__main__":
    import time
    start_time = time.monotonic()
    print("ATOM-LEVEL WEDDERBURN TOWER (λ ⊢ 3A)")
    print("=" * 80)
    print(f"q_0 = {float(Q0):.6f}")
    print()

    # Light isotopes through A = 4 (A = 5+ blocks hundreds of
    # partitions; run selectively via `ATOM_LEVEL_WITH_A5PLUS=1`).
    import os as _os
    ISOTOPES = [
        ("p", 1, 0, False),
        ("n", 0, 1, False),
        ("D atom", 1, 1, True),
        ("T atom", 1, 2, True),
        ("3He atom", 2, 1, True),
        ("4He atom", 2, 2, True),
    ]
    if _os.environ.get("ATOM_LEVEL_WITH_A5PLUS"):
        ISOTOPES.extend([
            ("6Li atom", 3, 3, True),
            ("7Li atom", 3, 4, True),
        ])

    results = {}
    for label, Z, N, include in ISOTOPES:
        A = Z + N
        k = 3 * A
        n_partitions = sum(1 for _ in partitions_of(k))
        t0 = time.time()
        try:
            desc, phi_sum, by_level, per_lam = atom_level_tower(
                Z, N, include_inter=include)
        except Exception as exc:
            print(f"  {label}: ERROR {type(exc).__name__}: {exc}")
            continue
        dt = time.time() - t0
        print(f"── {label} (A={A}, n={k}, p({k})={n_partitions}, "
              f"walltime {dt:.1f}s) ──")
        print(f"  descended tr_M(𝒜)              = {desc:+.6e}")
        print(f"  Σ_λ w_λ · Φ_q(|χ^λ|/dim)       = {phi_sum:+.6e}")
        print(f"  by GB level (height-1):")
        for lvl in sorted(by_level):
            info = by_level[lvl]
            print(f"    level {lvl}: count={info['count']:>3}, "
                  f"w·χ = {info['sum_w_chi']:+.4e}, "
                  f"w·Φ_q = {info['sum_phi_q']:+.4e}")
        results[label] = {
            "Z": Z, "N": N, "A": A,
            "n_partitions": n_partitions,
            "descended_tr_M": desc,
            "phi_q_atom_sum": phi_sum,
            "by_level": by_level,
            "walltime_sec": dt,
        }
        print()

    witness = {
        "computation": "atom-level-wedderburn-tower",
        "description": (
            "Atom-level Wedderburn decomposition (λ ⊢ 3A) with GB "
            "filtration level breakdown.  Per user directive: replaces "
            "per-generator H_3 projection with full H_{3A} channel sum.  "
            "Tests Σ_λ w_λ · Φ_q(|χ^λ(𝒜)|/dim) as atom-level brane "
            "tower candidate."
        ),
        "reference_blocks": [
            "prop:schur-weyl-mass-decomposition",
            "thm:frobenius-codim-universal",
            "thm:frobenius-antipode-unifies-chirality-and-tower",
            "prop:e-infinity-page-identifications",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(Q0_FLOAT),
            "level_heuristic": "len(λ) - 1 (diagram height - 1)",
        },
        "results": results,
    }
    # Wrap legacy payload via WitnessBuilder.wrap_legacy for provenance
    sys.path.insert(0, str(Path(__file__).parent))
    from witness_base import WitnessBuilder  # noqa: E402
    (WitnessBuilder
        .wrap_legacy("atom-level-wedderburn-tower", witness,
                     script_path=__file__, engine="python",
                     start_time=start_time)
        .save())
    out = Path(__file__).parent / "atom-level-wedderburn-tower.witness.json"
    print(f"\nWitness: {out}")
