#!/usr/bin/env python3
"""γγ LR-embed at H_6 — extending H_3 PSD scan to deuteron.

Per probe_gamma_gamma_h3_psd_scan.py the B_3 cube
σ_0 σ_1⁻¹ σ_0 σ_1⁻¹ σ_0 σ_1⁻¹ is uniquely PSD-feasible at H_3 among
12 γγ-style candidates.

This script extends the test to H_6 (deuteron strand count) by
running the FULL atom braid for D = (Z=1, N=1) — proton ⊗ neutron
disconnected tensor + 1 inter-nucleon ud-half crossing — and
checking PSD-feasibility on each Wedderburn block of H_6.

The atom braid is built by atomic_braid_to_crossings (already
canonical in light_isotope_sweep.py). For D, this yields the
LR-embedded structure: B_3 cube ⊗ B_3 cube + 1 inter pn-boundary
ud-half (per chi-sym-alt theorem n_ud(D) = 5 = 2·2 + 1).

PSD test: for each partition λ ⊢ 6 (11 partitions total), build
the ρ_λ(β_D) matrix at q_0 via Hoefsmit seminormal, check
positive-semidefiniteness of the symmetric part.

If all 11 blocks are PSD: the LR-embedding preserves PSD-feasibility
(B_3 cube structure carries up). If any block is not PSD: the inter-
nucleon piece breaks PSD at H_6, suggesting an additional structural
constraint is needed at the atom level.

NO Vol_hyp.  NO census.  Pure mpmath at 50 dps via
chi_lambda_numeric (which uses np internally — f64).

Output: probe-gamma-gamma-lr-embed-h6.witness.json
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import M_E_MEV
from hecke_character_symbolic import atomic_braid_to_crossings
from light_isotope_sweep import partitions_of, dim_q, H_VAL
from q_parameter import Q as Q_0
from witness_base import WitnessBuilder
# F6 (PR #582): wire numerical-q Hoefsmit through BlockCache.
from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached

# Crossing-type → d for ρ_λ matrix construction (per
# light_isotope_sweep.chi_lambda_numeric)
D_FOR = {"sigma": 0.0, "sigma_inv": -H_VAL, "averaged": -H_VAL / 2}
_BLOCK_CACHE = BlockCache(float(Q_0), H_VAL)


def chi_lambda_with_psd_check(shape, crossings, scipy_sparse=None):
    """Build ρ_λ(β) and report (chi, eigvals_sym, psd_or_close)."""
    sigmas, dim, _ = build_seminormal_matrices_cached(
        shape, cache=_BLOCK_CACHE,
    )
    if dim == 0:
        return None
    is_sparse = False
    try:
        from scipy import sparse as sp_sparse
        is_sparse = sp_sparse.issparse(sigmas[0])
    except ImportError:
        pass
    if is_sparse:
        I = sp_sparse.eye(dim, format='csr')
        product = sp_sparse.eye(dim, format='csr')
    else:
        I = np.eye(dim)
        product = np.eye(dim)
    for gen_idx, cross_type in crossings:
        if gen_idx < 0 or gen_idx >= len(sigmas):
            return None
        M = sigmas[gen_idx] + D_FOR[cross_type] * I
        product = product @ M
    if is_sparse:
        product_dense = product.toarray()
    else:
        product_dense = product
    chi = float(np.trace(product_dense))
    # PSD check on symmetric part
    M_sym = (product_dense + product_dense.T) / 2.0
    eigvals = np.linalg.eigvalsh(M_sym)
    psd = bool(eigvals.min() >= -1e-9)
    return {
        "shape": list(shape),
        "dim": dim,
        "chi_lambda": chi,
        "eigvals_sym_min": float(eigvals.min()),
        "eigvals_sym_max": float(eigvals.max()),
        "eigvals_sym_count_negative": int((eigvals < -1e-9).sum()),
        "psd_or_close": psd,
    }


def main():
    print("=" * 78)
    print("γγ LR-embed at H_6 — deuteron PSD-feasibility scan")
    print("=" * 78)
    print(f"  q_0 = {Q_0}")
    print()

    # Build deuteron atom braid (Z=1, N=1, with inter-nucleon)
    crossings = atomic_braid_to_crossings(Z=1, N=1, include_inter=True)
    print(f"  Deuteron atom braid: {len(crossings)} total crossings")
    print(f"  (B_3 confinement × 2 + intra ud-halves × 2 + inter ud-half × 1)")
    print()

    # Iterate partitions of 6
    n = 6
    n_partitions = sum(1 for _ in partitions_of(n))
    print(f"  H_{n}: {n_partitions} partitions")
    print(f"  {'partition':<14} {'dim':>4} {'χ':>10} {'min eig':>10} "
          f"{'max eig':>10} {'#neg':>5} {'PSD':>5}")
    print("  " + "-" * 70)

    rows = []
    psd_count = 0
    for shape in partitions_of(n):
        t0 = time.time()
        try:
            result = chi_lambda_with_psd_check(shape, crossings)
        except Exception as exc:
            print(f"  {str(list(shape)):<14} ERROR: {exc}")
            continue
        if result is None:
            continue
        elapsed = time.time() - t0
        marker = "✓" if result["psd_or_close"] else "✗"
        if result["psd_or_close"]:
            psd_count += 1
        result["walltime_sec"] = elapsed
        rows.append(result)
        print(f"  {str(result['shape']):<14} {result['dim']:>4} "
              f"{result['chi_lambda']:>10.4f} "
              f"{result['eigvals_sym_min']:>10.4f} "
              f"{result['eigvals_sym_max']:>10.4f} "
              f"{result['eigvals_sym_count_negative']:>5} "
              f"{marker:>5}")

    print()
    print(f"  PSD-feasible partitions: {psd_count} / {len(rows)}")
    if psd_count == len(rows):
        print("  ✓ FULL PSD: B_3 cube LR-embeds cleanly to H_6 — deuteron's")
        print("    inter-nucleon piece preserves PSD across all 11 partitions.")
    else:
        print("  ✗ NOT FULL PSD: some partitions have negative eigenvalues.")
        print("    LR-embedding does NOT auto-preserve PSD; inter-nucleon")
        print("    crossing breaks PSD at the atom level (H_6).")
    print()

    # Build witness
    w = (
        WitnessBuilder("probe-gamma-gamma-lr-embed-h6", engine="python+numpy")
        .set_description(
            "Foreground γγ LR-embed test at H_6 (deuteron). Builds the "
            "deuteron atom braid via atomic_braid_to_crossings(Z=1, N=1) "
            "and checks PSD-feasibility on every Wedderburn block of H_6 "
            "via Hoefsmit seminormal matrices at q_0. Tests whether the "
            "B_3 cube's H_3 PSD-feasibility (per probe_gamma_gamma_h3_"
            "psd_scan.py) carries up to H_6 via LR-embedding."
        )
        .set_content_block("rem:photon-channel-wedderburn-chain")
        .add_parameter("q_0", Q_0)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("n_strands_H6", 6)
        .add_data("rows", rows)
        .add_data("psd_count", psd_count)
        .add_data("partitions_total", len(rows))
        .add_data("full_psd", psd_count == len(rows))
        .add_caveat(
            "Uses chi_lambda_numeric (numpy/f64); not MPFR. The PSD "
            "test is on the SYMMETRIC PART of ρ_λ(β); full Hermitian "
            "test would require eigenvalues of (M + M*)/2 in complex."
        )
        .add_caveat(
            "PSD-feasibility is necessary but not sufficient for "
            "categorical canonicality; an ADDITIONAL constraint (e.g., "
            "minimal tr_M complement, or matching to physical mass "
            "scale) is needed to uniquely pick canonical T_w(D)."
        )
    )
    out_path = w.save()
    print(f"Witness: {out_path.name}")


if __name__ == "__main__":
    main()
