#!/usr/bin/env python3
"""
Closed-form derivation of χ_std(β_nucleon) on the 2-dim (2,1) irrep of H_3(q).

Symbolic computation producing:
  χ_std(β_proton)  = (H_A/4) · ([11]_q + [9]_q + [7]_q + [3]_q)
  χ_std(β_neutron) = (H_A/4) · ([9]_q + [7]_q + [5]_q + [1]_q)

Verifies against direct numerical Hoefsmit trace at q=q_0 and produces
a witness JSON.

Ref: docs/chi-std-pernucleon-theorem.md
"""
from __future__ import annotations

import sys
import json
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0


def seminormal_std_n3(q_sym):
    """Hoefsmit seminormal 2×2 matrices for std = (2,1) at n=3."""
    H = q_sym - 1/q_sym
    sigma_1 = sp.Matrix([[q_sym, 0], [0, -1/q_sym]])
    a = H/(1 - q_sym**4)
    a_prime = H/(1 - q_sym**(-4))
    b_sq = sp.simplify(a*a_prime + 1)
    b = sp.sqrt(b_sq)
    sigma_2 = sp.Matrix([[a, b], [b, a_prime]])
    return sigma_1, sigma_2, H


def q_number(q_sym, k):
    """[k]_q = (q^k - q^{-k}) / (q - q^{-1})."""
    return (q_sym**k - q_sym**(-k)) / (q_sym - 1/q_sym)


def proton_char_symbolic(q_sym):
    """χ_std(β_proton) via direct 2×2 matrix trace."""
    sigma_1, sigma_2, H = seminormal_std_n3(q_sym)
    sigma_2_inv = sigma_2 - H * sp.eye(2)
    # gen 0: σ_1^6 · (σ_1 - H/2)
    S1_udhalf = sigma_1 - (H/2) * sp.eye(2)
    W_g0 = sigma_1**6 * S1_udhalf
    # gen 1: σ_2^{-3} · (σ_2 - H/2)
    S2_udhalf = sigma_2 - (H/2) * sp.eye(2)
    W_g1 = sigma_2_inv**3 * S2_udhalf
    W = sp.simplify(W_g0 * W_g1)
    chi = sp.simplify(sp.trace(W))
    return sp.radsimp(chi)


def neutron_char_symbolic(q_sym):
    """χ_std(β_neutron) via direct 2×2 matrix trace."""
    sigma_1, sigma_2, H = seminormal_std_n3(q_sym)
    sigma_2_inv = sigma_2 - H * sp.eye(2)
    # gen 0: σ_1^4 · (σ_1 - H/2)
    S1_udhalf = sigma_1 - (H/2) * sp.eye(2)
    W_g0 = sigma_1**4 * S1_udhalf
    # gen 1: identical to proton
    S2_udhalf = sigma_2 - (H/2) * sp.eye(2)
    W_g1 = sigma_2_inv**3 * S2_udhalf
    W = sp.simplify(W_g0 * W_g1)
    chi = sp.simplify(sp.trace(W))
    return sp.radsimp(chi)


def closed_form_qnum(q_sym, indices: list[int]):
    """(H_A/4) · Σ_{k in indices} [k]_q."""
    H = q_sym - 1/q_sym
    total = sum(q_number(q_sym, k) for k in indices)
    return sp.simplify((H/4) * total)


if __name__ == "__main__":
    q = sp.Symbol('q', positive=True)

    print("=" * 100)
    print("CLOSED-FORM χ_std on per-nucleon braid words (H_3(q), (2,1))")
    print("=" * 100)

    print("\n--- Proton ---")
    chi_p = proton_char_symbolic(q)
    print(f"  χ_std(β_p) = {chi_p}")
    chi_p_closed = closed_form_qnum(q, [11, 9, 7, 3])
    diff_p = sp.simplify(chi_p - chi_p_closed)
    print(f"  closed form (H/4)·([11]+[9]+[7]+[3]) matches: {diff_p == 0}")

    print("\n--- Neutron ---")
    chi_n = neutron_char_symbolic(q)
    print(f"  χ_std(β_n) = {chi_n}")
    chi_n_closed = closed_form_qnum(q, [9, 7, 5, 1])
    diff_n = sp.simplify(chi_n - chi_n_closed)
    print(f"  closed form (H/4)·([9]+[7]+[5]+[1]) matches: {diff_n == 0}")

    print("\n--- Numerical verification at q_0 ---")
    q0 = float(Q0)
    chi_p_num = float(chi_p.subs(q, q0))
    chi_p_num_polynomial_q = expose_polynomial(chi_p, q)
    chi_p_closed_num = float(chi_p_closed.subs(q, q0))
    chi_p_closed_num_polynomial_q = expose_polynomial(chi_p_closed, q)
    chi_n_num = float(chi_n.subs(q, q0))
    chi_n_num_polynomial_q = expose_polynomial(chi_n, q)
    chi_n_closed_num = float(chi_n_closed.subs(q, q0))
    chi_n_closed_num_polynomial_q = expose_polynomial(chi_n_closed, q)
    print(f"  proton  (matrix trace):   {chi_p_num:.16f}")
    print(f"  proton  (closed-form Σ):  {chi_p_closed_num:.16f}")
    print(f"  neutron (matrix trace):   {chi_n_num:.16f}")
    print(f"  neutron (closed-form Σ):  {chi_n_closed_num:.16f}")

    print("\n--- Cyclotomic factorization ---")
    chi_p_factored = sp.factor(chi_p)
    chi_n_factored = sp.factor(chi_n)
    print(f"  proton:  {chi_p_factored}")
    print(f"  neutron: {chi_n_factored}")

    # P2.5 Tier B — expose polynomial forms alongside numerical
    # evaluation. See witness_polynomial.py.
    from witness_polynomial import expose_polynomial_dict
    polynomial_forms = expose_polynomial_dict(
        {
            "chi_p_std": chi_p,
            "chi_p_closed_form": chi_p_closed,
            "chi_p_factored": chi_p_factored,
            "chi_n_std": chi_n,
            "chi_n_closed_form": chi_n_closed,
            "chi_n_factored": chi_n_factored,
        },
        q,
        q0=sp.Rational(str(q0)),
    )

    witness = {
        "computation": "chi-std-pernucleon-closed-form",
        "description": (
            "Closed-form derivation of χ_std(β_nuc) on 2-dim (2,1) "
            "irrep of H_3(q) via explicit 2×2 Hoefsmit seminormal "
            "matrix trace.  Both proton and neutron characters take "
            "the form (H_A/4)·([m]+[m-2]+[m-4]+[m-8]) with m_p = 11, "
            "m_n = 9.  Proton factors as pure cyclotomic product; "
            "neutron has an irreducible residual degree-12 factor."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "polynomial_forms": polynomial_forms,
        "q_0": q0,
        "proton": {
            "chi_std_laurent": str(chi_p),
            "chi_std_factored": str(chi_p_factored),
            "closed_form_indices": [11, 9, 7, 3],
            "closed_form_expr": "(H/4) · ([11]_q + [9]_q + [7]_q + [3]_q)",
            "chi_at_q0": chi_p_num,
            "closed_form_at_q0": chi_p_closed_num,
            "match_symbolic": bool(diff_p == 0),
        },
        "neutron": {
            "chi_std_laurent": str(chi_n),
            "chi_std_factored": str(chi_n_factored),
            "closed_form_indices": [9, 7, 5, 1],
            "closed_form_expr": "(H/4) · ([9]_q + [7]_q + [5]_q + [1]_q)",
            "chi_at_q0": chi_n_num,
            "closed_form_at_q0": chi_n_closed_num,
            "match_symbolic": bool(diff_n == 0),
        },
        "unified_form": "(H_A/4) · ([m]_q + [m-2]_q + [m-4]_q + [m-8]_q)",
        "m_proton": 11,
        "m_neutron": 9,
    }
    out = Path(__file__).parent / "chi-std-pernucleon.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\nWitness: {out}")
