#!/usr/bin/env python3
"""Height-stratified Markov trace probe for D.

The Markov trace on H_n(q) under the Wenzl convention sums over
ALL partitions λ ⊢ n. The Schur-Weyl / Habiro convention restricts
to height ≤ 2 (= Jones polynomial, colored-Jones level 2).

This probe computes the partial sum at each height cap for D's atom
braid (n=6, 23 crossings).  Each level corresponds to a colored-Jones
contribution.  If the QOU multi-term mass formula corresponds to a
sum over colored-Jones levels, we'd see a structural pattern.

Output: probe-d-height-stratification.witness.json
"""
import sys
import json
from pathlib import Path
import numpy as np
from scipy import sparse as sp_sparse

# Reuse from-scratch Wenzl pipeline (already validated)
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "from_scratch"))

from hecke_characters import (
    partitions_of, build_seminormal_matrices, qfac, dim_q,
)
from canonical_braid_crossings import atom_canonical_crossings as atomic_braid_to_crossings
from chi_sym_alt_closed_form import chi_sym_closed_form, chi_alt_closed_form
from q_parameter import Q as Q0_FLOAT, HA
# F6 (PR follow-up #582): wire numerical-q Hoefsmit through BlockCache.
from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
_BLOCK_CACHE = BlockCache(Q0_FLOAT, HA)
from experimental_constants import M_E_MEV
import json as _json
from witness_base import WitnessBuilder

H_VAL = float(Q0_FLOAT - 1.0/Q0_FLOAT)


def chi_lambda_numeric(shape, crossings):
    sigmas, dim, _ = build_seminormal_matrices_cached(
        shape, cache=_BLOCK_CACHE,
    )
    if dim == 0:
        return 0.0, 0
    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    if is_sparse:
        I = sp_sparse.eye(dim, format='csr')
        prod = sp_sparse.eye(dim, format='csr')
    else:
        I = np.eye(dim)
        prod = np.eye(dim)
    d_for = {"sigma": 0.0, "sigma_inv": -H_VAL, "averaged": -H_VAL/2}
    for gen_idx, ct in crossings:
        M = sigmas[gen_idx] + d_for[ct]*I
        prod = prod @ M
    return (float(prod.diagonal().sum()) if is_sparse
            else float(np.trace(prod))), dim


def main():
    # D atom braid (Z=1, N=1, include_inter=True)
    n = 6
    braid = atomic_braid_to_crossings(1, 1, include_inter=True)
    print(f"D atom braid in B_6: {len(braid)} crossings on 6 strands")
    print()

    # Wenzl y_λ for n=6 from witness (cyclotomic Schur form)
    yw = json.load(open(Path(__file__).parent / "y-lambda-wenzl-witness.json"))
    wenzl_y = {tuple(w["partition"]): float(w["y_lambda_numeric"])
               for w in yw["tables_by_n"]["6"]["weights"]}

    sym = (6,); alt = (1,)*6
    nfac6 = qfac(6)

    # Compute χ_λ for each λ ⊢ 6
    print(f"{'λ':>14} {'h(λ)':>4} {'d_λ':>4} {'dim_q':>10} {'χ_λ':>10} "
          f"{'y_Wenzl':>10} {'contrib':>10}")
    print("-" * 80)

    rows = []
    by_height = {}
    for lam in partitions_of(n):
        if lam == sym:
            chi = chi_sym_closed_form(braid, Q0_FLOAT); d = 1
        elif lam == alt:
            chi = chi_alt_closed_form(braid, Q0_FLOAT); d = 1
        else:
            chi, d = chi_lambda_numeric(lam, braid)
        if d == 0: continue
        dq = float(dim_q(lam))
        yW = wenzl_y.get(lam, 0.0)
        contrib = yW * chi
        height = len(lam)
        by_height.setdefault(height, []).append((lam, contrib))
        print(f"  {str(lam):>12} {height:>4} {d:>4} {dq:>10.4f} "
              f"{chi:>10.4f} {yW:>10.4f} {contrib:>+10.4f}")
        rows.append({
            "lambda": list(lam), "height": height, "d_lambda": d,
            "dim_q": dq, "chi": chi, "y_wenzl": yW, "contrib": contrib,
        })

    print("-" * 80)
    total = sum(r["contrib"] for r in rows)
    print(f"  {'TOTAL Wenzl tr_M(D atom, H_6)':>52}              {total:>+10.6f}")
    print()

    # Stratify by height
    print("Height-stratified contributions (= colored-Jones decomposition):")
    print(f"{'height':>10} {'# parts':>8} {'sum contrib':>12} {'cum sum':>12}")
    print("-" * 50)
    cum = 0.0
    by_h_sums = {}
    for h in sorted(by_height.keys()):
        s = sum(c for _, c in by_height[h])
        cum += s
        by_h_sums[h] = (s, cum)
        print(f"  {h:>4}     {len(by_height[h]):>5}    "
              f"{s:>+10.6f}    {cum:>+10.6f}")
    print()

    print("KEY OBSERVATIONS:")
    print(f"  height=1 only (just (6)): {by_h_sums[1][0]:+.6f}")
    print(f"  height ≤ 2 (Jones-level): {by_h_sums[2][1]:+.6f}")
    print(f"  height ≤ 3 (colored-Jones at level 3):"
          f" {by_h_sums.get(3, (0,0))[1]:+.6f}")
    print(f"  height ≤ 6 (full Wenzl):  {total:+.6f}")
    print()
    # Compare to Habiro-polynomial path value
    print("CROSS-CHECKS:")
    print(f"  Wenzl tr_M (full)       = {total:+.6f}")
    print(f"  Habiro polynomial path  = +0.177437 (level-2 / Jones value)")
    print(f"  Wenzl height ≤ 2 sum    = {by_h_sums[2][1]:+.6f}")
    print()

    if abs(by_h_sums[2][1] - 0.177437) < 0.01:
        print("  ✓ Wenzl height-≤-2 partial sum CLOSE to Habiro/Jones value!")
    else:
        diff = by_h_sums[2][1] - 0.177437
        print(f"  Diff: {diff:+.6f} (Habiro normalisation ≠ Wenzl height-≤-2)")

    # B(D) under each interpretation
    M_E = M_E_MEV
    rho_D = 1
    B_AME = 2.224566
    print()
    print(f"Paper formula B = m_e · ρ · tr_M:")
    print(f"  ρ_D = {rho_D}")
    print(f"  full Wenzl       : B = {M_E*rho_D*total:>8.4f} MeV "
          f"(err {(M_E*rho_D*total - B_AME)/B_AME*100:+.1f}%)")
    print(f"  height ≤ 2 only  : B = {M_E*rho_D*by_h_sums[2][1]:>8.4f} MeV "
          f"(err {(M_E*rho_D*by_h_sums[2][1] - B_AME)/B_AME*100:+.1f}%)")

    # Save witness
    w = (
        WitnessBuilder("probe-d-height-stratification", engine="python")
        .set_description(
            "Height-stratified Markov trace for D's atom braid: splits "
            "the full Wenzl-Schur tr_M into per-height contributions, "
            "each corresponding to a colored-Jones-at-level-h piece. "
            "Per Schur duality, height-≤-(k+1) traces correspond to "
            "SU(k+1) projections; height-≤-2 = standard Jones polynomial."
        )
        .set_content_block("thm:knot-mass-formula-unified")
        .add_parameter("q_0", float(Q0_FLOAT))
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_data("rows", rows)
        .add_data("by_height_sums", {str(h): {"sum": s, "cum": c}
                                        for h, (s, c) in by_h_sums.items()})
        .add_data("total_wenzl", total)
        .add_data("habiro_polynomial_value", 0.177437)
        .add_caveat(
            "The Schur-Weyl 'Habiro polynomial' tr_M (=0.177437) uses "
            "Schur weights w_λ = s_λ(q,q⁻¹)/H_q(λ) which VANISH on "
            "partitions of height > 2. The Wenzl-Schur full Markov "
            "trace (=0.336821) sums over all partitions including "
            "height > 2. The difference is the colored-Jones tower "
            "structure beyond Jones level 2."
        )
    )
    out = w.save()
    print(f"\nWitness: {out.name}")


if __name__ == "__main__":
    main()
