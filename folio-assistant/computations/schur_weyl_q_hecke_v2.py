#!/usr/bin/env python3
"""
P2.2c — q-deformed Hecke character on atomic braids (with per-crossing (c, d)).

Replaces the chi_lambda_braid path (which only takes (sign, gen)
braid words and so cannot distinguish proton from neutron) with a
proper per-crossing-coefficient evaluation:

    χ^λ_q(W_atomic) = tr_λ ( Π_i (c_i · σ_{g_i} + d_i · I) )

where (c_i, d_i, g_i) are read from `mass_endomorphism.proton_cross`
/ `neutron_cross` (intra-nucleon) and the inter-nucleon coupling
table.

This recovers the proton-vs-neutron distinction at the character
level: proton and neutron sub-braids share the same braid word
structure but differ in their (c, d) coefficients. With the
proper Hecke-element evaluation, χ^λ_q(W_p) ≠ χ^λ_q(W_n).

Witness: docs/audits/2026-05-01-p2-2c-q-hecke-v2.witness.json
"""
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import mpmath
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from hecke_characters import build_seminormal_matrices, dim_q, qfac
from mass_endomorphism import proton_cross, neutron_cross
from schur_weyl_mpmath import length_le_2_partitions_of
from q_parameter import Q as Q0_FLOAT


def build_atomic_crossings_with_coeffs(Z, N, include_inter=True,
                                        m_pp=1, m_pn=1, m_nn=1, q_val=None):
    """Build atomic braid as list of (c, d, gen_0based) per crossing.

    Each entry represents a Hecke-algebra factor `c·σ_g + d·I`.
    Distinguishes proton from neutron via the (c, d) values.

    Returns (crossings_list, n_strands).
    """
    if q_val is None:
        q_val = Q0_FLOAT
    h = q_val - 1 / q_val
    A = Z + N
    nucleon_types = ['p'] * Z + ['n'] * N
    n_strands = 3 * A

    crossings = []
    for k, nt in enumerate(nucleon_types):
        src = proton_cross if nt == 'p' else neutron_cross
        # Intra-nucleon gen 0 = position 3k
        for c, d in src.get(0, []):
            crossings.append((float(c), float(d), 3 * k))
        # Intra-nucleon gen 1 = position 3k+1
        for c, d in src.get(1, []):
            crossings.append((float(c), float(d), 3 * k + 1))
    if include_inter:
        for k in range(A - 1):
            pair = (nucleon_types[k], nucleon_types[k + 1])
            if pair == ('p', 'p'):
                base = (1.0, 0.0); m_this = m_pp
            elif pair == ('n', 'n'):
                base = (1.0, -h); m_this = m_nn
            else:  # pn / np
                base = (1.0, -h / 2); m_this = m_pn
            c_base, d_base = base
            for _ in range(m_this):
                crossings.append((c_base, d_base, 3 * k + 2))
    return crossings, n_strands


def chi_lambda_atomic(shape, Z, N, q_val=None, *,
                      include_inter=True, m_pp=1, m_pn=1, m_nn=1):
    """χ^λ(atomic braid) at q = q_val via Hoefsmit seminormal matrices.

    Each crossing is c·σ_g + d·I; multiplied through the braid.
    Returns trace as float.
    """
    if q_val is None:
        q_val = Q0_FLOAT
    n_strands = 3 * (Z + N)
    n_gens = n_strands - 1

    # Build seminormal matrices for σ_1, ..., σ_{n_strands-1}
    # Note: build_seminormal_matrices uses 0-based indexing internally
    sigmas, dim, _syts = build_seminormal_matrices(shape, q=q_val)
    if dim == 0:
        return 0.0

    crossings, _ns = build_atomic_crossings_with_coeffs(
        Z, N, include_inter=include_inter,
        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn, q_val=q_val,
    )

    # P2.2c-12C: prefer the Rust kernel pyhecke_native.chi_q_atomic
    # when available — it's MUCH faster than the Python paths for
    # large partition dimensions.
    try:
        import pyhecke_native
        # Convert crossings (c, d, gen_0based) → (c, d, gen_1based) for Rust
        factors = [(float(c), float(d), int(g) + 1) for c, d, g in crossings]
        return float(pyhecke_native.chi_q_atomic(list(shape), factors, float(q_val)))
    except (ImportError, AttributeError):
        # Fallback to Python paths if pyhecke_native unavailable
        pass

    # ── Python fallbacks (only when pyhecke_native isn't installed) ──
    from scipy import sparse as sp_sparse
    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False

    if not is_sparse:
        # Small-dim path: dense matrix product is fastest
        I = np.eye(dim)
        product = np.eye(dim)
        for c, d, g in crossings:
            if g >= len(sigmas):
                continue
            M = c * sigmas[g] + d * I
            product = product @ M
        return float(np.trace(product))

    # Large-dim path: sparse trace via iterative vector products
    from sparse_trace_of_product import sparse_trace_of_product
    I_sp = sp_sparse.eye(dim, format='csr')
    factors = []
    for c, d, g in crossings:
        if g >= len(sigmas):
            continue
        if d == 0.0:
            M = c * sigmas[g]
        elif c == 0.0:
            M = d * I_sp
        else:
            M = (c * sigmas[g]) + (d * I_sp)
        if not sp_sparse.isspmatrix_csr(M):
            M = M.tocsr()
        factors.append(M)
    return sparse_trace_of_product(factors, dim)


def markov_trace_q_hecke_atomic(Z, N, *, q_val=None, precision=50,
                                 include_inter=True, dim_cap=None):
    """tr_M(W_atomic) at q = q_val via Schur-Weyl × q-Hecke character.

    Σ_{λ ⊢ 3A, len(λ) ≤ 2, dim(λ) ≤ dim_cap} w_λ(q) · χ^λ_q(W_atomic) / dim(λ)

    Note: divides by dim(λ) per the Markov-trace normalisation
    (matches `compute_mass_at_level`).

    Args:
        dim_cap: skip partitions with dim_λ > dim_cap (truncation).
            None = no cap (default; appropriate for A ≤ 4). At A=12+,
            length-≤-2 partition dims grow to >1e6; pass dim_cap=10000
            for tractable computation. Truncation is acceptable
            because the per-braid framework needs only a handful of
            light-partition contributions for splitting.
    """
    if q_val is None:
        q_val = Q0_FLOAT
    mpmath.mp.dps = precision
    q = mpmath.mpf(str(q_val))

    A = Z + N
    n_strands = 3 * A
    nfac = qfac(n_strands)

    total = mpmath.mpf(0)
    partitions_used = []
    skipped = []
    from murnaghan_nakayama import dim_specht
    # Use mpmath-based dim_q / qfac to avoid float64 overflow at A ≥ ~16
    from schur_weyl_mpmath import q_factorial_mp, schur_weyl_weight_mp
    q_mp = mpmath.mpf(str(q_val))
    nfac_mp = q_factorial_mp(n_strands, q_mp)
    for lam in length_le_2_partitions_of(n_strands):
        # Dim cap (truncation for large A)
        d_classical = dim_specht(lam)
        if dim_cap is not None and d_classical > dim_cap:
            skipped.append({"partition": list(lam), "dim": d_classical, "reason": "dim_cap"})
            continue
        # Build w_λ via mpmath (overflow-safe at high A)
        w_mp = schur_weyl_weight_mp(lam, q_mp)
        if w_mp == 0:
            continue
        w_f = w_mp  # mpmath, used in contrib below
        # χ^λ_q on the atomic braid
        chi = chi_lambda_atomic(lam, Z, N, q_val=float(q_val),
                                 include_inter=include_inter)
        if chi == 0:
            continue
        contrib = w_f * mpmath.mpf(chi) / mpmath.mpf(d_classical)
        total += contrib
        partitions_used.append({
            "partition": list(lam),
            "w_lambda_q": float(w_f),
            "chi_q": float(chi),
            "dim_lambda": d_classical,
            "contribution": str(contrib),
        })
    return total, partitions_used


# ─── Witness + comparison ─────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 80)
    print("P2.2c v2 — q-deformed Hecke character on atomic braids (with (c,d))")
    print("=" * 80)
    print(f"q_0 = {Q0_FLOAT}")

    # 1. Verify proton vs neutron sub-braid traces are now different
    print("\n=== Per-nucleon traces (single nucleon = H_3 sub-braid) ===")
    for nt, Z, N in [("proton", 1, 0), ("neutron", 0, 1)]:
        try:
            t0 = time.time()
            total, parts = markov_trace_q_hecke_atomic(Z, N, include_inter=False)
            t = time.time() - t0
            print(f"  {nt}: |tr_M| = {abs(total)}  ({len(parts)} parts, {t*1000:.1f}ms)")
        except Exception as e:
            print(f"  {nt}: ERROR {type(e).__name__}: {str(e)[:80]}")

    # 2. Atomic-braid traces for D / 3He / 3H / 4He
    print("\n=== Atomic braid traces ===")
    ATOMS = [("D", 1, 1), ("3He", 2, 1), ("3H", 1, 2), ("4He", 2, 2)]
    results = []
    for name, Z, N in ATOMS:
        print(f"\n--- {name} (Z={Z}, N={N}, A={Z+N}) ---")
        try:
            t0 = time.time()
            total, parts = markov_trace_q_hecke_atomic(Z, N, include_inter=True)
            t = time.time() - t0
            mag = abs(total)
            print(f"  |Σ_λ w_λ χ^λ_q / dim_λ| = {mag}")
            print(f"  {len(parts)} non-zero partitions, {t:.3f}s")
            results.append({
                "atom": name, "Z": Z, "N": N, "A": Z + N,
                "abs_value_at_q0": str(mag),
                "n_partitions": len(parts),
                "time_seconds": t,
                "partitions": parts[:10],  # cap for readability
            })
        except Exception as e:
            import traceback; traceback.print_exc()
            results.append({"atom": name, "error": str(e)})

    # 3. ³He vs ³H splitting
    he3 = next((r for r in results if r.get("atom") == "3He"), None)
    h3 = next((r for r in results if r.get("atom") == "3H"), None)
    splitting_info = None
    if he3 and h3 and "abs_value_at_q0" in he3 and "abs_value_at_q0" in h3:
        v_he3 = mpmath.mpf(he3["abs_value_at_q0"])
        v_h3 = mpmath.mpf(h3["abs_value_at_q0"])
        diff = v_he3 - v_h3
        rel = abs(diff) / max(abs(v_he3), abs(v_h3)) if max(abs(v_he3), abs(v_h3)) > 0 else None
        print(f"\n=== ³He vs ³H splitting (q-Hecke v2 with (c, d)) ===")
        print(f"  3He: {v_he3}")
        print(f"  3H : {v_h3}")
        print(f"  diff: {diff}")
        if rel is not None:
            print(f"  relative: {rel}")
        if abs(diff) > mpmath.mpf("1e-10"):
            print(f"  ✅ SPLITTING DETECTED — q-Hecke + (c,d) distinguishes 3He from 3H")
        else:
            print(f"  🔴 still identical or below numerical noise")
        splitting_info = {
            "3He_value": str(v_he3),
            "3H_value": str(v_h3),
            "diff": str(diff),
            "rel_diff": str(rel) if rel is not None else None,
        }

    witness = {
        "audit": "P2.2c v2 — q-deformed Hecke character on atomic braids with (c, d)",
        "generated": datetime.now(timezone.utc).isoformat(),
        "q_0": str(Q0_FLOAT),
        "atoms": results,
        "splitting": splitting_info,
        "interpretation": (
            "Each crossing in the atomic braid is c·σ_g + d·I; (c, d) "
            "distinguishes proton from neutron. χ^λ_q evaluates as a "
            "matrix-product trace through the atomic braid using "
            "Hoefsmit seminormal matrices for σ_g."
        ),
    }
    out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-01-p2-2c-q-hecke-v2.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
