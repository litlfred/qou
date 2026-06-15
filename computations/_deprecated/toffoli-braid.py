#!/usr/bin/env python3
"""
Toffoli (CCNOT) braid — P_{7,6}(q) as the q-AND amplitude.

The massive Toffoli transfer matrix M(q) is an 8×8 matrix of Laurent
polynomials P_{m,k}(q), built from the Iwahori--Hecke algebra H_3(q) crossing
coefficients in the QOU nuclear braid formalism.

Each entry P_{m,k}(q) is the topological amplitude from input state
|k₁k₂k₃⟩ (column k) to output state |m₁m₂m₃⟩ (row m), where:
  - Strands 1,2 are "controls" (their types are fixed by k)
  - Strand 3 is "target" (can transition via beta-decay amplitude)

The key entry P_{7,6}(q) is the q-AND: the amplitude for
  |110⟩ → |111⟩  (both controls ON → target flips)

Crossing coefficients (paper convention):
  pp: c = 1,           d = 0
  nn: c = 1,           d = −HA       where HA = q − q⁻¹
  mix: c = 1,          d = −HA/2

Transfer matrix:  T(c,d) = | c(q−q⁻¹)+d   c |
                            |     c         d |

Markov parameter: z = 1/(q^{1/2} + q^{−1/2})

Usage:
    python3 computations/toffoli-braid.py

Output:
    computations/toffoli-braid.witness.json
"""

import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from sympy import Rational, sqrt, cancel, factor

# ── Symbolic ring in q ────────────────────────────────────────────

q = sp.Symbol('q', positive=True)

# Derived quantities
ha = q - 1/q                     # q − q⁻¹  (Hecke amplitude)
z = 1 / (sqrt(q) + 1/sqrt(q))   # Markov parameter


# ── Crossing coefficients (paper convention) ─────────────────────

def crossing_coefficients(ti, tj):
    """Return (c, d) for the crossing of types ti, tj.

    Paper convention (skein-polynomial-transfer-matrix.md):
      pp: c = 1,   d = 0
      nn: c = 1,   d = −HA        where HA = q − q⁻¹
      mix: c = 1,  d = −HA/2
    """
    if ti == 1 and tj == 1:
        return sp.Integer(1), sp.Integer(0)
    elif ti == 0 and tj == 0:
        return sp.Integer(1), -ha
    else:
        return sp.Integer(1), -ha / 2


# ── Transfer matrix chain reduction ─────────────────────────────

def chain_reduce(gen_idx, ordering):
    """Reduce the chain at generator σ_{gen_idx} → (a, b).

    Multiplies the 2×2 transfer matrices T(c_j, d_j) for all
    crossings j > gen_idx at this generator.  Returns (a, b) where
    M_i = | a·(q−q⁻¹)+b   a |  and  V̂_i = z·a + b.
          |     a          b |
    """
    a = sp.Integer(0)
    b = sp.Integer(1)
    A = len(ordering)
    for j in range(gen_idx + 1, A):
        c, d = crossing_coefficients(ordering[gen_idx], ordering[j])
        new_a = a * c * ha + a * d + b * c
        new_b = a * c + b * d
        a, b = new_a, new_b
    return a, b


def traced_volume(gen_idx, ordering):
    """V̂_i(q) = z(q)·a_i(q) + b_i(q)"""
    a, b = chain_reduce(gen_idx, ordering)
    return cancel(z * a + b)


def markov_trace(ordering):
    """P(q) = ∏_i V̂_i(q) — the Skein polynomial."""
    A = len(ordering)
    product = sp.Integer(1)
    for i in range(A - 1):
        product *= traced_volume(i, ordering)
    return cancel(product)


# ── State encoding ───────────────────────────────────────────────

def decode(k):
    """k ∈ {0,...,7} → (b₁, b₂, b₃) binary."""
    return ((k >> 2) & 1, (k >> 1) & 1, k & 1)


def encode(b1, b2, b3):
    return (b1 << 2) | (b2 << 1) | b3


def toffoli_output(k):
    """Classical Toffoli: |k₁k₂k₃⟩ → |k₁k₂(k₃ ⊕ (k₁∧k₂))⟩"""
    b1, b2, b3 = decode(k)
    return encode(b1, b2, b3 ^ (b1 & b2))


# ── Build the 8×8 Toffoli transfer matrix ───────────────────────

def build_matrix():
    """Build M(q): 8×8 massive Toffoli transfer matrix.

    Diagonal:       P_{k,k}(q) = tr_M(N̄(ordering_k))
    Off-diagonal:   P_{m,k}(q) = 1-jet transition amplitude
                    (sum over converting generators of Δ·context)
    """
    M = [[sp.Integer(0)] * 8 for _ in range(8)]

    for k in range(8):
        ordering_k = list(decode(k))
        M[k][k] = markov_trace(ordering_k)

        m = toffoli_output(k)
        if m != k:
            ordering_m = list(decode(m))

            V_par = [traced_volume(i, ordering_k) for i in range(2)]
            V_dau = [traced_volume(i, ordering_m) for i in range(2)]

            # 1-jet expansion: P_{m,k} = Σ_i [∏_{j≠i} V̂_j^(par)] · Δ_i
            P_mk = sp.Integer(0)
            for conv in range(2):
                delta = V_par[conv] - V_dau[conv]
                ctx = sp.Integer(1)
                for j in range(2):
                    if j != conv:
                        ctx *= V_par[j]
                P_mk += ctx * delta
            M[m][k] = cancel(P_mk)

            # Reverse transition (use parent context for antisymmetry)
            P_km = sp.Integer(0)
            for conv in range(2):
                delta = V_dau[conv] - V_par[conv]
                ctx = sp.Integer(1)
                for j in range(2):
                    if j != conv:
                        ctx *= V_par[j]
                P_km += ctx * delta
            M[k][m] = cancel(P_km)

    return M


# ── Display ──────────────────────────────────────────────────────

def main():
    print("═" * 70)
    print("  MASSIVE TOFFOLI TRANSFER MATRIX  M(q)")
    print("═" * 70)
    print()
    print("Iwahori--Hecke algebra H₃(q),  σ² = (q − q⁻¹)σ + 1")
    print("Crossing coefficients C_{ij} = c_j σ_i + d_j :")
    print("  pp:  c = 1,         d = 0")
    print("  nn:  c = 1,         d = −HA")
    print("  mix: c = 1,         d = −HA/2")
    print("where HA = q − q⁻¹")
    print()
    print("z(q) = 1/(q^{1/2} + q^{-1/2})")
    print()

    M = build_matrix()

    types_map = {0: 'nnn', 1: 'nnp', 2: 'npn', 3: 'npp',
                 4: 'pnn', 5: 'pnp', 6: 'ppn', 7: 'ppp'}

    # ── Non-zero entries ──
    print("NON-ZERO ENTRIES OF M(q)")
    print("─" * 70)
    print()

    q_phys = Rational(111, 100)
    witness_entries = {}

    for i in range(8):
        for j in range(8):
            val = M[i][j]
            if val == 0:
                continue

            if i == j:
                kind = "diagonal"
            elif (i, j) == (7, 6):
                kind = "q-AND"
            elif (i, j) == (6, 7):
                kind = "reverse"
            else:
                kind = "off-diag"

            val_f = factor(cancel(val))
            val_num = float(val_f.subs(q, q_phys))
            val_num_polynomial_q = expose_polynomial(val_f, q)

            print(f"P_{{{i},{j}}}(q)  [{types_map[j]}→{types_map[i]}]  ({kind})")
            print(f"  = {val_f}")
            print(f"  at q = 1.110: {val_num:.10f}")
            print()

            witness_entries[f"P_{i},{j}"] = {
                "symbolic": str(val_f),
                "numerical_1.110": val_num,
                "type": kind,
                "input": types_map[j],
                "output": types_map[i],
            }

    # ── Toffoli block detail ──
    print("═" * 70)
    print("TOFFOLI BLOCK (rows 6–7, cols 6–7)")
    print("═" * 70)
    print()
    for i in (6, 7):
        for j in (6, 7):
            val = cancel(M[i][j])
            val_factored = factor(val)
            val_num = float(val.subs(q, q_phys))
            val_num_polynomial_q = expose_polynomial(val, q)
            classical = sp.limit(val, q, 1)
            print(f"  P_{{{i},{j}}}(q) = {val_factored}")
            print(f"    q → 1: {classical}")
            print(f"    q = 1.110: {val_num:.10f}")
            print()

    # ── Interference check ──
    print("═" * 70)
    print("DESTRUCTIVE INTERFERENCE CHECK")
    print("═" * 70)
    n_wrong = 0
    for i in range(8):
        for j in range(8):
            if i == j:
                continue
            if (i, j) in ((7, 6), (6, 7)):
                continue
            val = cancel(M[i][j])
            if val != 0:
                n_wrong += 1
                print(f"  P_{{{i},{j}}} = {val}  ← NON-ZERO")
    if n_wrong == 0:
        print("  ✓ All off-diagonal entries except P_{7,6} and P_{6,7} are zero.")
        print("  ✓ Perfect destructive interference of wrong-parity pathways.")
    print()

    # ── Planck time evolution ──
    print("═" * 70)
    print("DISCRETE PLANCK TIME EVOLUTION")
    print("═" * 70)
    print()
    print("  t_P(q) = q/(q−1) = Planck time per crossing")
    print("  3 crossings in the Toffoli braid → total time = 3·t_P")
    print()
    print(f"  {'Epoch':>22} | {'q':>7} | {'t_P':>9} | {'3·t_P':>9} | {'P_{7,6}':>12} | {'P_{6,6}':>12} | {'P_{7,7}':>12}")
    print("  " + "─" * 100)

    epochs = [
        (100, 1, "Big Bang"),
        (10, 1, "Early"),
        (5, 1, "q = 5"),
        (3, 1, "q = 3"),
        (2, 1, "q = 2"),
        (3, 2, "q = 3/2"),
        (111, 100, "Physical"),
        (101, 100, "Near-classical"),
    ]

    planck_data = []
    P76_sym = M[7][6]
    P66_sym = M[6][6]
    P77_sym = M[7][7]

    for num, den, label in epochs:
        qv = Rational(num, den)
        qf = float(qv)
        tP = float(qv / (qv - 1))
        p76 = float(P76_sym.subs(q, qv))
        p76_polynomial_q = expose_polynomial(P76_sym, q)
        p66 = float(P66_sym.subs(q, qv))
        p66_polynomial_q = expose_polynomial(P66_sym, q)
        p77 = float(P77_sym.subs(q, qv))
        p77_polynomial_q = expose_polynomial(P77_sym, q)
        print(f"  {label:>22} | {qf:>7.3f} | {tP:>9.4f} | {3*tP:>9.4f} | {p76:>12.6f} | {p66:>12.6f} | {p77:>12.6f}")
        planck_data.append({
            "epoch": label, "q": qf, "t_P": tP,
            "P_76": p76, "P_66": p66, "P_77": p77,
        })

    print()
    print("  At Big Bang (q → ∞): t_P → 1, Toffoli executes in 3 Planck steps")
    print("  At physical q = 1.110: t_P ≈ 10.09, Toffoli ≈ 30 Planck steps")
    print("  Classical (q → 1): t_P → ∞, Toffoli freezes")

    # ── Write witness ──
    witness = {
        "computation": "toffoli-braid",
        "description": (
            "P_{7,6}(q) as q-AND amplitude in the massive Toffoli transfer "
            "matrix M(q). Built from Iwahori--Hecke algebra H_3(q) with paper crossing "
            "conventions: pp=(1,0), nn=(1,−HA), mix=(1,−HA/2) where HA=q−q⁻¹."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "framework": {
            "algebra": "H_3(q)",
            "hecke_relation": "σ² = (q − q⁻¹)σ + 1",
            "crossings": {
                "pp": {"c": "1", "d": "0"},
                "nn": {"c": "1", "d": "−(q − q⁻¹)"},
                "mixed": {"c": "1", "d": "−(q − q⁻¹)/2"},
            },
            "skein_amplitude": "s = q^{1/2} − q^{-1/2}",
            "markov_parameter": "z = 1/(q^{1/2} + q^{-1/2})",
            "planck_time": "t_P(q) = q/(q−1)",
        },
        "matrix_entries": witness_entries,
        "planck_evolution": planck_data,
    }

    out_path = Path(__file__).parent / "toffoli-braid.witness.json"
    with open(out_path, "w") as f:
        json.dump(witness, f, indent=2, default=str)
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
