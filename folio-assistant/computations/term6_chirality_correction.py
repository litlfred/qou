#!/usr/bin/env python3
"""
DERIVE THE O(H_A²) CORRECTION TO TERM 6 FROM THE PARTITION SPECTRUM.

Term 6 (proton residual, paper):
    T_6 = m_e · Σ_{λ⊢n} 1/dim_q V_λ
        = m_e · (2 + 1/[2]_q)  at n=3
        ≈ 1.276 MeV at q_0

Observed: Δm_{n-p} = 1.293 MeV. Gap: +0.017 MeV (1.3%).

User direction: derive the H_A^2 correction from the SAME partition
spectrum, via the alternating-channel chirality.

Hypothesis: the correct Term 6 is the χ-WEIGHTED sum:

    T_6_full = m_e · Σ_{λ⊢n} χ_λ(β) / dim_q V_λ

evaluated on the actual braid β (proton or neutron).

Under S-eigenvalue decomposition (prop:frobenius-s-classification),
(3) and (1,1,1) form a conjugate pair with χ_(3)(σ) = q,
χ_(1,1,1)(σ) = -q^{-1}.  The S-anti-invariant part of the
χ-weighted sum is m_e · H_A · (writhe-dependent factor).

Probe: for proton (β_p) and neutron (β_n) braids, compute
T_6_full(p), T_6_full(n), and check if the difference equals
Δm_{n-p}.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

import numpy as np
from scipy import sparse as sp_sparse

from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from hecke_characters import partitions_of, build_seminormal_matrices, dim_q

Q0 = mp.mpf(str(Q0_FLOAT)); QI = mp.mpf(1)/Q0
H_A = Q0 - QI
me = mp.mpf(str(M_E_MEV))
h_val = float(H_A)


def chi_lambda(shape, word):
    """χ^λ(braid word) via Hoefsmit seminormal."""
    sigmas, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return 0.0
    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    if is_sparse:
        product = sp_sparse.eye(dim, format='csr')
        I = sp_sparse.eye(dim, format='csr')
    else:
        product = np.eye(dim)
        I = np.eye(dim)
    for w in word:
        idx = abs(w) - 1
        if idx >= len(sigmas):
            continue
        if w > 0:
            M = sigmas[idx]
        else:
            M = sigmas[idx] - h_val * I
        product = product @ M
    if is_sparse:
        chi = float(product.diagonal().sum())
    else:
        chi = float(np.trace(product))
    return chi


def b3_braid_word():
    return [1, -2, 1, -2, 1, -2]


def nucleon_braid_word(quark_types):
    word = list(b3_braid_word())
    for i in range(3):
        for j in range(i + 1, 3):
            gen = min(i + 1, 2)
            t_i, t_j = quark_types[i], quark_types[j]
            if t_i == t_j == 'u':
                word.append(gen)
            elif t_i == t_j == 'd':
                word.append(-gen)
            else:
                word.append(gen)
    return word


def main():
    print("=" * 100)
    print("Term 6 chirality correction — character-weighted partition sum")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  m_e = {float(me):.6f} MeV")
    print(f"  H_A = q - q^-1 = {h_val:.6f}, H_A² = {h_val**2:.6f}")
    print()

    p_word = nucleon_braid_word(['u', 'u', 'd'])
    n_word = nucleon_braid_word(['u', 'd', 'd'])
    print(f"  Proton  braid word: {p_word}  (length {len(p_word)})")
    print(f"  Neutron braid word: {n_word}  (length {len(n_word)})")
    print()

    # For each partition of 3, evaluate χ on p and n braids
    print(f"  {'partition':<12} {'dim_q V_λ':>10} {'χ_λ(p)':>12} {'χ_λ(n)':>12} "
          f"{'χ_p/dim':>12} {'χ_n/dim':>12} {'Δχ/dim':>12}")
    sum_chi_p = mp.mpf(0)
    sum_chi_n = mp.mpf(0)
    for shape in partitions_of(3):
        shape_t = tuple(shape)
        dq = float(dim_q(shape_t))
        chi_p = chi_lambda(shape_t, p_word)
        chi_n = chi_lambda(shape_t, n_word)
        cp_d = chi_p / dq
        cn_d = chi_n / dq
        sum_chi_p += mp.mpf(str(cp_d))
        sum_chi_n += mp.mpf(str(cn_d))
        diff = cn_d - cp_d
        print(f"  {str(shape_t):<12} {dq:>10.4f} {chi_p:>+12.6f} {chi_n:>+12.6f} "
              f"{cp_d:>+12.6f} {cn_d:>+12.6f} {diff:>+12.6f}")

    print()
    print(f"  Sum_p = Σ_λ χ_λ(p)/dim_q  = {float(sum_chi_p):+.6f}")
    print(f"  Sum_n = Σ_λ χ_λ(n)/dim_q  = {float(sum_chi_n):+.6f}")
    print(f"  Δ = Sum_n - Sum_p          = {float(sum_chi_n - sum_chi_p):+.6f}")
    print()
    print(f"  m_e · Sum_p              = {float(me * sum_chi_p):+.6f} MeV")
    print(f"  m_e · Sum_n              = {float(me * sum_chi_n):+.6f} MeV")
    print(f"  m_e · (Sum_n - Sum_p)    = {float(me * (sum_chi_n - sum_chi_p)):+.6f} MeV")
    print(f"  CODATA Δm_{{n-p}}          = {M_N_MEV - M_P_MEV:+.6f} MeV")
    print(f"  m_e · Σ_3 (paper Term 6) = {float(me * (2 + 1/(Q0+QI))):+.6f} MeV")

    # Compare with Σ_3 = trace-based Term 6
    Sigma_3 = 2 + 1/(Q0 + QI)
    print()
    print(f"  Sum_p / Σ_3 = {float(sum_chi_p / Sigma_3):+.6f}")
    print(f"  Sum_n / Σ_3 = {float(sum_chi_n / Sigma_3):+.6f}")

    # H_A^2 chirality correction structure
    print()
    print(f"  H_A^2/2 = {h_val**2/2:.6f}")
    print(f"  m_e · H_A^2/2 = {float(me) * h_val**2 / 2:.6f} MeV")
    print(f"  Σ_3 + H_A^2/2 = {float(Sigma_3) + h_val**2/2:.6f}")
    print(f"  m_e · (Σ_3 + H_A^2/2) = {float(me) * (float(Sigma_3) + h_val**2/2):.6f} MeV")

    # Save witness
    witness = {
        'computation': 'term6-chirality-correction',
        'description': (
            'Generalization of Term 6 (proton residual) to character-'
            'weighted partition sum.  Evaluates Σ_λ χ_λ(β)/dim_q V_λ '
            'for proton and neutron braids; checks if the difference '
            'matches CODATA Δm_{n-p} = 1.293 MeV.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'sum_chi_p': float(sum_chi_p),
        'sum_chi_n': float(sum_chi_n),
        'sum_diff_MeV': float(me * (sum_chi_n - sum_chi_p)),
        'codata_delta_np': M_N_MEV - M_P_MEV,
    }
    out = Path(__file__).parent / "term6-chirality-correction.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
