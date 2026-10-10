#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
Deuteron (²H) binding energy from first principles — NUMERICAL pipeline.

Uses the established numerical Hoefsmit in hecke_characters.py (which
handles the 2×2 block b² sign with sqrt(abs(b²)) — symbolic-sympy path
blew up on b² < 0 for larger partitions at q_0).

    tr_M(T_w) = Σ_{λ ⊢ 3A} w_λ(q_0) · χ^λ_q(T_w)/dim(λ)

with:
  w_λ(q)      = dim_q(λ)² / [3A]_q!       (numerical at q_0)
  χ^λ_q(T_w)  = Tr(Π ρ_λ(T_{σ_{i_k}^{±1}}))   (numerical at q_0)
  T_w = atomic_braid_word(Z, N, include_inter) — the actual paper
         convention (proton_cross, neutron_cross, inter-nucleon pn)

This uses the paper's atomic-braid convention (same as
atomic_braid_to_crossings in hecke_character_symbolic.py), NOT the
pair-graph convention of hecke_characters.nuclear_braid_character.
We assemble the product explicitly from the atomic braid word.

TODO (next iteration): replace with symbolic-in-q pipeline.
The A=1 proof-of-concept in hecke_character_symbolic.py kept
q as sympy.Symbol but blew up at A ≥ 2 due to sign of b² in
the 2×2 Hoefsmit blocks.  Path forward: either (i) track b²
symbolically without taking sqrt until the final trace, using
b² · Matrix[[0,1],[1,0]] as a formal off-diagonal piece, or
(ii) switch to the Ocneanu-Wenzl seminormal basis which is
manifestly real-algebraic on the unitary locus.

Witness: deuteron-first-principles.witness.json
"""
import json
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
from scipy import sparse as sp_sparse

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
from hecke_characters import (
    partitions_of,
    build_seminormal_matrices,
    qfac,
    dim_q,
)
from hecke_character_symbolic import atomic_braid_to_crossings


def chi_lambda_on_atomic_braid(shape, crossings, q_val, h_val):
    """Evaluate χ^λ_q(T_w) numerically for the atomic braid word.

    crossings is a list of (gen_idx, cross_type) where cross_type
    ∈ {"sigma", "sigma_inv", "averaged"}.

    Returns the trace of the product matrix.
    """
    sigmas, dim, _syts = build_seminormal_matrices(shape)
    if dim == 0:
        return 0.0, 0

    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    if is_sparse:
        I = sp_sparse.eye(dim, format='csr')
        product = sp_sparse.eye(dim, format='csr')
    else:
        I = np.eye(dim)
        product = np.eye(dim)

    # d value for each cross_type
    d_for = {
        "sigma": 0.0,
        "sigma_inv": -h_val,
        "averaged": -h_val / 2,
    }

    for gen_idx, cross_type in crossings:
        if gen_idx < 0 or gen_idx >= len(sigmas):
            raise IndexError(f"gen_idx {gen_idx} out of range "
                             f"(n_gens={len(sigmas)}) for shape {shape}")
        sigma = sigmas[gen_idx]
        d_val = d_for[cross_type]
        M = sigma + d_val * I
        product = product @ M

    if is_sparse:
        chi = float(product.diagonal().sum())
    else:
        chi = float(np.trace(product))
    return chi, dim


def mass_trace_at_q0(Z, N, include_inter=True):
    """Full tr_M(T_w) = Σ_{λ ⊢ 3A} w_λ · χ^λ_q(T_w) / dim(λ) at q_0.

    Returns (total, per_lambda_list).
    """
    A = Z + N
    k = 3 * A
    nfac = qfac(k)
    crossings = atomic_braid_to_crossings(Z, N, include_inter)
    h_val = float(_Q_CANONICAL - 1.0 / _Q_CANONICAL)

    total = 0.0
    per_lambda = []
    for shape in partitions_of(k):
        t0 = time.time()
        chi, dim = chi_lambda_on_atomic_braid(shape, crossings,
                                              _Q_CANONICAL, h_val)
        if dim == 0:
            continue
        d_q = dim_q(shape)
        w = float(d_q ** 2 / nfac)
        contrib = w * chi / dim
        total += contrib
        per_lambda.append({
            "shape": shape,
            "dim": dim,
            "w_lambda": w,
            "chi_lambda": chi,
            "contribution": contrib,
            "walltime_sec": time.time() - t0,
        })
    return total, per_lambda


if __name__ == "__main__":
    print("DEUTERON (²H) BINDING — first principles, numerical H_{3A} pipeline")
    print("=" * 80)
    print(f"q_0 = {_Q_CANONICAL}")
    print("Engine: hecke_characters.build_seminormal_matrices (numerical Hoefsmit)")
    print("Braid convention: atomic_braid_to_crossings (proton_cross/neutron_cross/inter)\n")

    # ─── A=1 calibration (β-decay) ──────────────────────────────
    print("[1/3] A=1 β-decay calibration (free p, free n, no inter crossings)")
    print("-" * 76)
    t = time.time()
    tr_p, p_lam = mass_trace_at_q0(1, 0, include_inter=False)
    tr_n, n_lam = mass_trace_at_q0(0, 1, include_inter=False)
    print(f"  |tr_M(p)| @ q_0 = {abs(tr_p):.6e}  "
          f"({sum(l['walltime_sec'] for l in p_lam):.2f}s over "
          f"{len(p_lam)} partitions)")
    print(f"  |tr_M(n)| @ q_0 = {abs(tr_n):.6e}  "
          f"({sum(l['walltime_sec'] for l in n_lam):.2f}s over "
          f"{len(n_lam)} partitions)")
    Q_cat = tr_n - tr_p
    if abs(Q_cat) < 1e-12:
        print("  ERROR: Q_cat = 0 (calibration fails)")
        sys.exit(1)
    from experimental_constants import Q_NEUTRON_MEV
    E_0 = float(Q_NEUTRON_MEV) / abs(Q_cat)
    print(f"  Q_cat           = {Q_cat:+.6e}")
    print(f"  E_0             = {E_0:.6f} MeV/cat.unit")

    # ─── A=2 deuteron ───────────────────────────────────────────
    print(f"\n[2/3] A=2 deuteron (1p + 1n on 6 strands, 11 partitions of 6)")
    print("-" * 76)

    print("  Free (include_inter=False):")
    t = time.time()
    tr_D_free, free_lam = mass_trace_at_q0(1, 1, include_inter=False)
    print(f"    walltime: {time.time() - t:.2f}s")
    print(f"    λ-contributions:")
    for e in sorted(free_lam, key=lambda x: -abs(x['contribution']))[:6]:
        print(f"      λ={e['shape']!s:<18} dim={e['dim']:>3}  "
              f"w={e['w_lambda']:.4e}  χ={e['chi_lambda']:+.4e}  "
              f"contrib={e['contribution']:+.4e}")
    print(f"    |tr_M(free)| @ q_0 = {abs(tr_D_free):.6e}")

    print("\n  Atom (include_inter=True, 1 pn crossing):")
    t = time.time()
    tr_D_atom, atom_lam = mass_trace_at_q0(1, 1, include_inter=True)
    print(f"    walltime: {time.time() - t:.2f}s")
    print(f"    λ-contributions:")
    for e in sorted(atom_lam, key=lambda x: -abs(x['contribution']))[:6]:
        print(f"      λ={e['shape']!s:<18} dim={e['dim']:>3}  "
              f"w={e['w_lambda']:.4e}  χ={e['chi_lambda']:+.4e}  "
              f"contrib={e['contribution']:+.4e}")
    print(f"    |tr_M(atom)| @ q_0 = {abs(tr_D_atom):.6e}")

    # ─── Binding prediction ─────────────────────────────────────
    print(f"\n[3/3] Deuteron binding")
    print("-" * 76)
    B_cat = abs(tr_D_free) - abs(tr_D_atom)
    B_MeV = E_0 * abs(B_cat)
    B_AME = 2.22457
    rel_err = (B_MeV - B_AME) / B_AME * 100
    M_total = 2 * 938.272
    dm = abs(B_MeV - B_AME) / M_total * 100
    print(f"  |tr_M(free)| − |tr_M(atom)|  = {B_cat:+.6e}")
    print(f"  B_pred = E_0 · |ΔtrM|         = {B_MeV:+.6f} MeV")
    print(f"  B_AME (²H)                    = {B_AME:.6f} MeV")
    print(f"  relative error                = {rel_err:+.4f}%")
    print(f"  |Δm/m|%                       = {dm:+.6f}%")

    witness = {
        "computation": "deuteron-first-principles",
        "description": (
            "Deuteron (²H) binding from first principles.  Full "
            "Σ_{λ ⊢ 6} w_λ · χ^λ_q(T_w) / dim(λ) using the paper's "
            "atomic-braid convention (atomic_braid_to_crossings) with "
            "the numerical Hoefsmit pipeline from hecke_characters.py. "
            "β-decay calibration: E_0 = 0.782 MeV / |tr_M(n) − tr_M(p)|. "
            "Three inputs only: E_0, q_0, m_e (dimensional scale)."
        ),
        "reference_blocks": [
            "prop:schur-weyl-mass-decomposition",
            "rem:q-character-closes-parity-gap",
            "prop:categorical-mass-markov",
        ],
        "method": {
            "engine": "numerical Hoefsmit (hecke_characters.build_seminormal_matrices)",
            "braid_convention": "atomic_braid_to_crossings (proton_cross/neutron_cross/inter)",
            "note": (
                "Symbolic-in-q variant (hecke_character_symbolic.py) "
                "worked at A=1 but blew up at A ≥ 2 due to sign of b² "
                "in 2×2 Hoefsmit blocks.  Numerical pipeline uses "
                "sqrt(abs(b²)) as established convention.  TODO: "
                "reformulate symbolic Hoefsmit to avoid sqrt issue."
            ),
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": str(float(_Q_CANONICAL)),
            "E_0_MeV": E_0,
        },
        "A1_calibration": {
            "tr_p_q0": abs(tr_p),
            "tr_n_q0": abs(tr_n),
            "Q_cat": Q_cat,
            "E_0_cat_MeV": E_0,
        },
        "deuteron": {
            "n_partitions": len(free_lam),
            "tr_free_q0": abs(tr_D_free),
            "tr_atom_q0": abs(tr_D_atom),
            "B_pred_MeV": B_MeV,
            "B_AME_MeV": B_AME,
            "relative_error_pct": rel_err,
            "delta_m_over_m_pct": dm,
            "free_per_lambda": free_lam,
            "atom_per_lambda": atom_lam,
        },
    }
    out = Path(__file__).parent / "deuteron-first-principles.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
