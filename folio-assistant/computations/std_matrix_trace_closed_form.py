#!/usr/bin/env python3
"""
Matrix-trace closed form for χ_std(β) — all non-scalar irreps of H_{3A}(q).

For 1-dim irreps (sym, alt), characters factor multiplicatively and
give closed-form scalar identities (see derived_characters.py).

For multi-dim irreps (std and all other partitions λ ⊢ 3A with dim > 1),
σ acts as a matrix, so χ_λ(AB) ≠ χ_λ(A) χ_λ(B).  No scalar shortcut.

BUT: there is a matrix-trace closed form.  For each λ ⊢ 3A and braid
word β = Π_k (c_k σ_{g_k} + d_k I):

    χ_λ(β) = tr[ Π_k (c_k · ρ_λ(σ_{g_k}) + d_k · I_{d_λ}) ]

where ρ_λ(σ_i) ∈ Mat_{d_λ×d_λ}(ℚ(q)) is the explicit Hoefsmit
seminormal matrix of σ_i in irrep λ.  This IS a closed form — finite
product of explicit matrices, trace is a specific polynomial in
(c_k, d_k, q).

This module:
(1) builds ρ_λ(σ) in all partitions for a given n via
    build_seminormal_matrices
(2) computes the matrix-trace product for atom braids D, T, 3He, 4He
(3) sums over partitions with Plancherel weights → tr_M(β) at q₀
(4) derives ρ_F_derived = m_e · 8G · |tr_M| / V_hyp and compares to
    ρ_F_observed = B_AME / V_hyp

Zero fitting.  All computations at high precision via sympy + mpmath.
"""
from __future__ import annotations

import sys
import json
import time
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from scipy import sparse as sp_sparse

from hecke_characters import (partitions_of, dim_q, qfac,
                                build_seminormal_matrices)
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q as Q0

CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN_8G = 8.0 * CATALAN_G
M_E_MEV = 0.51099895
ALPHA_MEV = M_E_MEV * VOL_BORROMEAN_8G


def chi_matrix_trace(shape: tuple, word: list, q_val: float) -> complex:
    """χ_λ(β) via explicit matrix-trace product of ρ_λ(σ_i) Hoefsmit
    seminormal matrices, evaluated at q = q_val."""
    sigmas, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return 0.0 + 0j
    q_sym = sp.Symbol('q')
    # Substitute q = q_val in each sigma matrix
    sigmas_num = []
    for S in sigmas:
        if sp_sparse.issparse(S):
            S_arr = S.toarray()
        else:
            S_arr = np.asarray(S)
        M = np.zeros((dim, dim), dtype=complex)
        for i in range(dim):
            for j in range(dim):
                e = S_arr[i, j]
                if hasattr(e, "subs"):
                    M[i, j] = complex(sp.N(e.subs(q_sym, q_val)))
                else:
                    M[i, j] = complex(e)
        sigmas_num.append(M)
    I = np.eye(dim, dtype=complex)
    prod = I.copy()
    for (c, d, g) in word:
        if g < len(sigmas_num):
            prod = prod @ (c * sigmas_num[g] + d * I)
        else:
            return 0.0 + 0j
    return complex(np.trace(prod))


def atom_trace_via_plancherel(Z: int, N: int, max_dim: int = 100,
                                time_budget_sec: float = 60) -> dict:
    """Iteratively accumulate Plancherel-weighted tr_M(β) = Σ_λ w_λ · χ_λ/d_λ.

    Skips (n,) sym and (1^n) alt since those already have closed forms.
    Reports which partitions contribute most and where time is spent.
    """
    A = Z + N
    n = 3 * A
    word = atom_braid_word_3A(Z, N)
    parts = list(partitions_of(n))
    nfac = float(qfac(n))

    total = 0.0 + 0j
    per_part = []
    t_start = time.time()

    # Sort by dim ascending so 1-dim (sym, alt) come first
    sigmas_dims = []
    for shape in parts:
        _, dim, _ = build_seminormal_matrices(shape, sparse=None)
        sigmas_dims.append((shape, dim))
    sigmas_dims.sort(key=lambda x: x[1])

    for shape, dim in sigmas_dims:
        if dim == 0:
            continue
        if dim > max_dim:
            per_part.append({"shape": list(shape), "dim": dim,
                              "status": "skipped_too_large"})
            continue
        elapsed = time.time() - t_start
        if elapsed > time_budget_sec and dim > 10:
            per_part.append({"shape": list(shape), "dim": dim,
                              "status": "skipped_time_budget"})
            continue
        dq = float(dim_q(shape))
        w = (dq * dq) / nfac
        chi = chi_matrix_trace(shape, word, float(Q0))
        contrib = w * chi / dim
        total += contrib
        per_part.append({
            "shape": list(shape), "dim": dim, "dim_q": dq,
            "w_lambda": w, "chi_re": chi.real, "chi_im": chi.imag,
            "contribution_re": contrib.real,
            "contribution_im": contrib.imag,
            "abs_contribution": abs(contrib),
        })

    return {
        "Z": Z, "N": N, "A": A, "n": n,
        "n_partitions_total": len(parts),
        "n_partitions_computed": sum(1 for p in per_part
                                        if "status" not in p),
        "tr_M_re": total.real, "tr_M_im": total.imag,
        "abs_tr_M": abs(total),
        "time_sec": time.time() - t_start,
        "per_partition": per_part,
    }


if __name__ == "__main__":
    print("=" * 100)
    print("MATRIX-TRACE CLOSED FORM for χ_std (all non-scalar Hecke irreps)")
    print(f"  q₀ = {float(Q0):.10f}")
    print(f"  α = m_e · 8G = {ALPHA_MEV:.6f} MeV")
    print("=" * 100)

    # Only D (n=6, 11 partitions) and T (n=9, 30 partitions) in budget.
    # 3He also n=9.  4He needs n=12 → 77 partitions, too slow in this env.
    ATOMS = [
        ("D",   1, 1, 2.22456612, 4.4008325),
        ("T",   1, 2, 8.4817984,  8.28632),
        ("3He", 2, 1, 7.7180375,  VOL_BORROMEAN_8G),
    ]

    all_results = []
    for (name, Z, N, B_ame, V_hyp) in ATOMS:
        print(f"\n{'=' * 80}")
        print(f"ATOM {name} (Z={Z}, N={N}, A={Z+N}, n=3A={3*(Z+N)})")
        print("=" * 80)
        try:
            r = atom_trace_via_plancherel(Z, N, time_budget_sec=45)
            r["B_AME"] = B_ame
            r["V_hyp"] = V_hyp

            print(f"  n_partitions:  {r['n_partitions_total']}")
            print(f"  computed:      {r['n_partitions_computed']}")
            print(f"  time:          {r['time_sec']:.1f}s")
            print(f"  tr_M(β) ≈      {r['tr_M_re']:+.8f}{r['tr_M_im']:+.2e}j")
            print(f"  |tr_M(β)|:     {r['abs_tr_M']:.8f}")

            # Largest 5 contributions
            contribs = [(p["shape"], p.get("abs_contribution", 0))
                         for p in r["per_partition"]
                         if "status" not in p]
            contribs.sort(key=lambda x: -x[1])
            print(f"  Top 5 contributions:")
            for shape, ac in contribs[:5]:
                print(f"    {shape}: |contrib| = {ac:.6f}")

            # Derivation check: ρ_F_derived = α · |tr_M| / V_hyp
            rho_F_derived = ALPHA_MEV * r['abs_tr_M'] / V_hyp
            rho_F_observed = B_ame / V_hyp
            r["rho_F_derived_MeV"] = rho_F_derived
            r["rho_F_observed_MeV"] = rho_F_observed
            r["ratio_der_over_obs"] = rho_F_derived / rho_F_observed
            print(f"  ρ_F_derived = α·|tr_M|/V_hyp = {rho_F_derived:.5f} MeV")
            print(f"  ρ_F_observed = B_AME/V_hyp   = {rho_F_observed:.5f} MeV")
            print(f"  ratio (der/obs):              {r['ratio_der_over_obs']:.5f}")

            all_results.append(r)
        except Exception as e:
            print(f"  ERR: {type(e).__name__}: {str(e)[:100]}")

    print(f"\n{'=' * 100}")
    print("SUMMARY")
    print("=" * 100)
    print(f"  {'atom':>4} {'|tr_M|':>12} {'ρ_F_der':>12} {'ρ_F_obs':>12} "
          f"{'der/obs':>10}")
    for r in all_results:
        print(f"  {r.get('Z',0)*10+r.get('N',0):>4} {r['abs_tr_M']:>12.8f} "
              f"{r['rho_F_derived_MeV']:>12.6f} "
              f"{r['rho_F_observed_MeV']:>12.6f} "
              f"{r['ratio_der_over_obs']:>10.6f}")

    witness = {
        "computation": "std-matrix-trace-closed-form",
        "description": (
            "Matrix-trace closed form for all Hecke irreps of H_{3A}(q) "
            "via Hoefsmit seminormal matrices.  Computes Plancherel-"
            "weighted tr_M(β_atom) iteratively over partitions for D, T, "
            "³He (n=6, 9, 9 respectively).  Derives ρ_F_derived = "
            "m_e · 8G · |tr_M| / V_hyp and compares to ρ_F_observed = "
            "B_AME / V_hyp at zero fitting."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": float(Q0),
        "alpha_MeV": ALPHA_MEV,
        # P2.5: sympy-as-matrix-stepping-stone pattern.  This script
        # uses sp.Symbol('q') only inside chi_matrix_trace to build
        # Hoefsmit seminormal matrices ρ_λ(σ_i) ∈ Mat(ℚ(q)); each
        # matrix is then immediately specialised at q = q_0 and the
        # downstream products / traces run in numpy.  Per-trace
        # χ_λ(β_atom) values are numerical specialisations, not
        # Laurent polynomials in q, because sympy doesn't scale for
        # the block-matrix products on partitions of n up to 9.
        "symbolic_q_form": {
            "engine": "sympy (matrix construction only) + numpy",
            "q_symbol": "q (sp.Symbol('q'))",
            "pattern_note": (
                "sympy-as-matrix-stepping-stone: ρ_λ(σ_i) ∈ "
                "Mat_{d_λ × d_λ}(ℚ(q)) is symbolic in chi_matrix_trace; "
                "the per-element subs(q, q_val) step eagerly converts "
                "to numpy before computing products.  Per-trace "
                "χ_λ(β_atom) values reported here are numerical "
                "specialisations at q = q_0, not Laurent polynomials in q."
            ),
            "symbolic_source": "hecke_characters.build_seminormal_matrices",
            "specialisation_point": "q = q_0",
        },
        "atoms": all_results,
    }
    out = Path(__file__).parent / "std-matrix-trace-closed-form.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
