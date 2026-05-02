#!/usr/bin/env python3
"""Probe Term 4 (Frobenius co-Casimir) under all 6 conventions.

Decomposes the convention question into two axes:

  Axis 1 — scaling by atom A:
    (a) per-vortex:    Term4 = m_e · Σ_{λ⊢3} 1/dim_q(λ)            [1·FROB_N3]
    (b) per-A:         Term4 = A · m_e · Σ_{λ⊢3} 1/dim_q(λ)         [A·FROB_N3]
    (c) per-3A-Hecke:  Term4 = m_e · Σ_{λ⊢3A} 1/dim_q(λ)            [genuine H_{3A}]

  Axis 2 — Frobenius pairing τ underlying C_{dim_q}:
    (i)  Plancherel:    τ(p_λ) = dim_q(λ)·d_λ/[n]_q!
                        ⇒ C = Σ_λ [n]_q!/(dim_q²·d_λ)·p_λ
                        ⇒ τ(C) = Σ 1/dim_q(λ)
    (ii) Wenzl-Schur:   τ(p_λ) = y_λ
                        ⇒ C = Σ_λ 1/(dim_q·y_λ)·p_λ
                        ⇒ τ(C) = Σ 1/dim_q(λ)  (SAME by linearity!)

Surprise: axis 2 doesn't actually change τ(C) at the abstract level
because the per-block contribution 1/(dim_q·τ(p_λ))·τ(p_λ) telescopes
to 1/dim_q regardless of τ(p_λ).  So the Frobenius co-Casimir TRACE
is convention-independent.  Only axis 1 (the scaling) matters.

Output: probe-term4-conventions.witness.json
"""
import sys, json, time
from pathlib import Path
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401

sys.path.insert(0, str(Path(__file__).parent))
from murnaghan_nakayama import partitions_of, dim_specht, hook_lengths
from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV

q = sp.Symbol('q', positive=True, real=True)

def q_int_sym(k):
    if k == 0: return sp.Integer(0)
    if k == 1: return sp.Integer(1)
    return sp.expand((q**k - q**(-k)) / (q - q**(-1)))

def q_factorial_sym(n):
    r = sp.Integer(1)
    for k in range(1, n+1): r *= q_int_sym(k)
    return sp.simplify(r)

def q_dim_sym(partition):
    n = sum(partition)
    hooks = hook_lengths(partition)
    h = sp.Integer(1)
    for hk in hooks: h *= q_int_sym(hk)
    return sp.simplify(q_factorial_sym(n) / h)

def sigma_inv_dim_q(n):
    """Σ_{λ⊢n} 1/dim_q(λ)."""
    parts = partitions_of(n)
    s = sp.Integer(0)
    for lam in parts:
        s += sp.Integer(1) / q_dim_sym(lam)
    return sp.simplify(s)

if __name__ == "__main__":
    print("="*78)
    print("Term 4 convention probe — all 6 (axis1 × axis2) combos")
    print("="*78)
    print(f"q_0 = {Q0_FLOAT}")
    print(f"m_e = {M_E_MEV} MeV")
    print()

    # Σ_{λ⊢3A} 1/dim_q(λ) for A=1,2,3,4
    sigma_table = {}
    for A in (1, 2, 3, 4):
        n = 3*A
        t0 = time.time()
        s_sym = sigma_inv_dim_q(n)
        s_q0 = float(s_sym.subs(q, sp.Rational(int(Q0_FLOAT*10**16), 10**16)).evalf(30))
        dt = time.time() - t0
        sigma_table[A] = (s_sym, s_q0)
        print(f"  Σ_{{λ⊢{n}}} 1/dim_q(λ) = {sp.nsimplify(s_sym)}")
        print(f"    at q_0:             = {s_q0:.6f}  ({dt:.1f}s)")
    print()

    sigma_n3_q0 = sigma_table[1][1]
    FROB_N3 = M_E_MEV * sigma_n3_q0
    print(f"FROB_N3 = m_e · Σ_{{λ⊢3}} 1/dim_q(λ) = {FROB_N3:.6f} MeV")
    print()

    # Test on D, T, ³He, ⁴He
    ATOMS = [
        ("D",   2,  2.22457),
        ("T",   3,  8.48180),
        ("3He", 3,  7.71806),
        ("4He", 4, 28.29569),
    ]

    print(f"{'atom':>5} {'A':>2}  "
          f"{'(a) per-vortex':>17} {'(b) per-A':>15} {'(c) per-3A':>20}")
    print(f"{'':>5} {'':>2}  "
          f"{'1·FROB_N3':>17} {'A·FROB_N3':>15} "
          f"{'m_e·Σ_{λ⊢3A} 1/dim_q':>20}")
    print("-"*78)

    rows = []
    for name, A, B_AME in ATOMS:
        T4_pv  = FROB_N3                        # per-vortex
        T4_pA  = A * FROB_N3                    # per-A (current compute)
        T4_p3A = M_E_MEV * sigma_table[A][1]    # per-3A genuine Hecke
        print(f"  {name:>5} {A:>2}  "
              f"{T4_pv:>14.4f} MeV "
              f"{T4_pA:>12.4f} MeV "
              f"{T4_p3A:>17.4f} MeV")
        rows.append({
            "atom": name, "A": A,
            "B_AME_MeV": B_AME,
            "Term4_per_vortex_MeV": T4_pv,
            "Term4_per_A_MeV": T4_pA,
            "Term4_per_3A_genuine_MeV": T4_p3A,
            "sigma_inv_dim_q_at_q0_n3A": sigma_table[A][1],
        })

    print()
    print("CRITICAL FINDING:")
    print("  axis 2 (Plancherel vs Wenzl-Schur τ) does NOT change τ(C_{dim_q})")
    print("  because c_λ·τ(p_λ) = [1/(dim_q·τ(p_λ))]·τ(p_λ) = 1/dim_q regardless.")
    print("  Only axis 1 (per-vortex vs per-A vs per-3A) is a real choice.")
    print()
    print("Per-3A is the GENUINE algebraic statement (τ(C_{dim_q}^{H_{3A}}))")
    print("Per-A and per-vortex are POSTULATES not derivations.")

    out = {
        "computation": "probe-term4-conventions",
        "computedAt": "auto",
        "description": "Term 4 under per-vortex / per-A / per-3A scaling",
        "FROB_N3_MeV": FROB_N3,
        "sigma_inv_dim_q_at_q0": {
            "n=3":  sigma_table[1][1],
            "n=6":  sigma_table[2][1],
            "n=9":  sigma_table[3][1],
            "n=12": sigma_table[4][1],
        },
        "rows": rows,
    }
    out_path = Path(__file__).parent / "probe-term4-conventions.witness.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWitness: {out_path}")
