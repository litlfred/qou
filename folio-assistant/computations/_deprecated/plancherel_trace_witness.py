#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
Full Plancherel-weighted Markov trace for D, T, ³He, ⁴He.

No fitting.  Iteratively computes for each atom:

    tr_M(β_atom) = Σ_{λ ⊢ 3A} w_λ · χ_λ(β_atom) / d_λ
                   w_λ = d_q(λ)² / [3A]_q!         (Plancherel weight)

using the fast char_fast.chi_lambda_fast machinery.

Then tests the derivation:
    ρ_F_derived(K) = m_e · 8G · |tr_M(β)| / V_hyp(K)
    ρ_F_observed(K) = B_AME(K) / V_hyp(K)

Writes witness with per-atom per-partition contributions so the
Plancherel weights and characters are all published.  Iterative in
two senses: (1) looped over atoms, (2) accumulated over partitions
with a running partial-sum record for large-n convergence.
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

from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A
from char_fast import chi_lambda_fast
from q_parameter import Q as Q0

CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN_8G = 8.0 * CATALAN_G
M_E_MEV = 0.51099895
ALPHA_MEV = M_E_MEV * VOL_BORROMEAN_8G


ATOMS = [
    ("D",   1, 1,  2.22456612, 4.4008325161),             # V_hyp = Vol(6_2)
    ("T",   1, 2,  8.4817984,  8.28632),                  # Vol(8_11)
    ("3He", 2, 1,  7.7180375,  VOL_BORROMEAN_8G),         # Vol(Borromean)
    ("4He", 2, 2, 28.295674,   4 * VOL_BORROMEAN_8G),     # 4 disjoint Borromean
]


def run_atom(name: str, Z: int, N: int) -> dict:
    """Iteratively accumulate Plancherel-weighted Markov trace."""
    A = Z + N
    n = 3 * A
    word = atom_braid_word_3A(Z, N)
    parts = list(partitions_of(n))
    nfac_q0 = float(qfac(n))

    print(f"\n{'=' * 90}")
    print(f"  ATOM {name}: A={A}, n={n}, {len(parts)} partitions, "
          f"word length {len(word)}")
    print(f"  [{n}]_q! at q₀ = {nfac_q0:.4f}")
    print(f"{'=' * 90}")

    total = 0.0 + 0j
    per_partition = []
    t_start = time.time()

    # Sort partitions by dim (small first → fast feedback, large later)
    def _dim_key(shape):
        _, d, _ = _cached_seminormal(shape)
        return d
    parts_sorted = sorted(parts, key=_dim_key)

    print(f"\n  {'partition':<16} {'dim':>5} {'d_q(λ)':>10} "
          f"{'w_λ':>10} {'χ_λ(β)':>14} "
          f"{'contribution':>16} {'running Σ':>14}")

    for shape in parts_sorted:
        _, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = float(dim_q(shape))
        w_lam = (dq * dq) / nfac_q0
        chi = chi_lambda_fast(shape, word)
        contrib = w_lam * chi / dim
        total += contrib

        per_partition.append({
            "shape": list(shape),
            "dim": dim,
            "dim_q_q0": dq,
            "w_lambda": w_lam,
            "chi_re": chi.real, "chi_im": chi.imag,
            "contribution_re": contrib.real,
            "contribution_im": contrib.imag,
        })
        print(f"  {str(shape):<16} {dim:>5} {dq:>+10.4f} "
              f"{w_lam:>10.6f} "
              f"{chi.real:>+10.4f}{chi.imag:+.2e}j "
              f"{contrib.real:>+10.4e}{contrib.imag:+.2e}j "
              f"{total.real:>+10.5f}")

    t_total = time.time() - t_start
    print(f"\n  Total time: {t_total:.1f} s")
    print(f"  |tr_M(β_{name})| at q₀: {abs(total):.10f}")
    print(f"  Re(tr_M):                {total.real:+.10f}")

    return {
        "atom": name, "Z": Z, "N": N, "A": A, "n": n,
        "n_partitions": len(parts),
        "tr_M_re": total.real, "tr_M_im": total.imag,
        "abs_tr_M": abs(total),
        "time_sec": t_total,
        "per_partition": per_partition,
    }


if __name__ == "__main__":
    print("=" * 100)
    print("ITERATIVE PLANCHEREL MARKOV TRACE — full sum over λ ⊢ 3A")
    print(f"  q₀ = {Q0:.10f}")
    print(f"  α = m_e · 8G = {ALPHA_MEV:.6f} MeV")
    print("=" * 100)

    all_results = []
    for (name, Z, N, B_ame, V_hyp) in ATOMS:
        try:
            r = run_atom(name, Z, N)
            r["B_AME"] = B_ame
            r["V_hyp"] = V_hyp

            # Derived density: m(K) = m_e · 8G · |tr_M| gives total mass
            # in cat units.  Binding at AME scale:
            abs_tr = r["abs_tr_M"]
            r["m_derived_MeV"] = ALPHA_MEV * abs_tr
            r["rho_F_derived_MeV"] = ALPHA_MEV * abs_tr / V_hyp
            r["rho_F_observed_MeV"] = B_ame / V_hyp
            r["rho_ratio_der_over_obs"] = (r["rho_F_derived_MeV"]
                                              / r["rho_F_observed_MeV"])
            all_results.append(r)
        except Exception as e:
            print(f"\n  ERR on {name}: {type(e).__name__}: {str(e)[:100]}")

    # Summary
    print(f"\n{'=' * 100}")
    print("SUMMARY — derived (Plancherel) vs observed ρ_F")
    print("=" * 100)
    print(f"  {'atom':>4} {'|tr_M|':>12} {'α·|tr_M|':>14} "
          f"{'V_hyp':>10} {'ρ_F_der':>12} {'ρ_F_obs':>12} "
          f"{'ratio':>10}")
    for r in all_results:
        print(f"  {r['atom']:>4} {r['abs_tr_M']:>12.6f} "
              f"{r['m_derived_MeV']:>14.4f} {r['V_hyp']:>10.4f} "
              f"{r['rho_F_derived_MeV']:>12.5f} "
              f"{r['rho_F_observed_MeV']:>12.5f} "
              f"{r['rho_ratio_der_over_obs']:>10.5f}")

    # ρ_F_obs/nom deviations (for reference)
    print(f"\n{'=' * 100}")
    print("How derived ρ_F compares to the {m_e, 2m_e} dichotomy")
    print("=" * 100)
    nominal = {"D": M_E_MEV, "T": 2*M_E_MEV, "3He": 2*M_E_MEV, "4He": 2*M_E_MEV}
    print(f"  {'atom':>4} {'nominal':>10} "
          f"{'obs/nom-1 %':>14} {'der/nom-1 %':>14} "
          f"{'der/obs-1 %':>14}")
    for r in all_results:
        nom = nominal[r["atom"]]
        obs_dev = (r["rho_F_observed_MeV"] / nom - 1) * 100
        der_dev = (r["rho_F_derived_MeV"]  / nom - 1) * 100
        der_over_obs = (r["rho_F_derived_MeV"] / r["rho_F_observed_MeV"] - 1) * 100
        print(f"  {r['atom']:>4} {nom:>10.5f} "
              f"{obs_dev:>+13.3f}% {der_dev:>+13.3f}% "
              f"{der_over_obs:>+13.3f}%")

    # Witness
    witness = {
        "computation": "plancherel-trace-witness",
        "description": (
            "Full Plancherel-weighted Markov trace |tr_M(β_atom)| at "
            "q₀ computed iteratively for each atom over all partitions "
            "of n = 3A.  Uses fast sympy.lambdify-based character "
            "evaluator (char_fast.chi_lambda_fast).  Tests whether "
            "the derivation ρ_F_derived = m_e · 8G · |tr_M| / V_hyp "
            "matches ρ_F_observed = B_AME / V_hyp without fitting."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": Q0,
        "alpha_MeV": ALPHA_MEV,
        "atoms": all_results,
    }
    out = Path(__file__).parent / "plancherel-trace-witness.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
