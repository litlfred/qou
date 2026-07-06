#!/usr/bin/env python3
"""
F_Pauli^(A) — A-strand alternating trace, symbolic in q.

Computes F_Pauli = |tr_alt(NF)| / |net(NF)| where:
  tr_alt = Σ c_w × (-q⁻¹)^ℓ(w)
  net    = Σ c_w

All coefficients exact in ℤ[q^½, q^{-½}]. No numerical evaluation
until the final step.

Usage:
    cd computations
    python3 pauli-witness.py
"""

import sys
import sympy as sp
import json
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
from hecke_symbolic import (
    SymbolicHeckeDivision, SymbolicHeckeElement,
    q, q_inv, HA, C_PP, C_NN, C_MIX, D_MIX, D_NN,
)
from witness_polynomial import expose_polynomial

div = SymbolicHeckeDivision()
LN_Q = sp.log(q)

def build_nf(Z, N):
    types = ['p'] * Z + ['n'] * N
    A = Z + N
    elem = SymbolicHeckeElement.identity()
    for k in range(1, A):
        for i in range(k):
            ti, tk = types[i], types[k]
            if ti == 'p' and tk == 'p':
                cx = SymbolicHeckeElement({(i,): C_PP})
            elif ti == 'n' and tk == 'n':
                cx = SymbolicHeckeElement({(i,): C_NN, (): D_NN})
            else:
                cx = SymbolicHeckeElement({(i,): C_MIX, (): D_MIX})
            elem = elem * cx
            elem, _ = div.reduce(elem)
    return elem

def compute_pauli(elem):
    """Compute alternating trace and net, symbolic in q."""
    tr_alt = sp.Integer(0)
    tr_sym = sp.Integer(0)
    net = sp.Integer(0)

    for w, c in elem.terms.items():
        L = len(w)
        tr_alt += c * (-q_inv) ** L
        tr_sym += c * q ** L
        net += c

    return {
        'tr_alt': sp.expand(tr_alt),
        'tr_sym': sp.expand(tr_sym),
        'net': sp.expand(net),
    }

# ══════════════════════════════════════════════════════════════
# Main computation
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    q0 = _Q_CANONICAL

    nuclei = [
        ('D', 1, 1), ('3H', 1, 2), ('3He', 2, 1), ('4He', 2, 2),
        ('5Li', 3, 2), ('6Li', 3, 3), ('7Li', 3, 4),
    ]

    print("F_PAULI^(A) — SYMBOLIC IN q")
    print(f"tr_alt = Σ c_w × (-q⁻¹)^ℓ(w)")
    print(f"F_Pauli = |tr_alt| / |net|")
    print()

    witness = {
        'computation': 'pauli-witness',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'description': 'A-strand Pauli factor, symbolic in q',
        'nuclei': {},
    }

    for name, Z, N in nuclei:
        A = Z + N
        t0 = time.time()

        elem = build_nf(Z, N)
        p = compute_pauli(elem)

        tr_alt_factored = sp.factor(p['tr_alt'])
        net_factored = sp.factor(p['net'])

        # F_Pauli as symbolic expression
        F_sym = sp.simplify(sp.Abs(p['tr_alt']) / sp.Abs(p['net']))

        # Evaluate at q₀
        tr_alt_val = float(p['tr_alt'].subs(q, q0))
        net_val = float(p['net'].subs(q, q0))
        F_val = abs(tr_alt_val) / abs(net_val) if net_val != 0 else 0

        elapsed = time.time() - t0

        # Histogram
        hist = {}
        for w in elem.terms:
            hist[len(w)] = hist.get(len(w), 0) + 1
        max_L = max(hist.keys()) if hist else 0
        counts = [hist.get(L, 0) for L in range(max_L + 1)]
        pal = counts == counts[::-1]

        print(f"{name} N({Z},{N}): A={A}, {elem.n_terms()} terms, pal={'Y' if pal else 'N'}")
        print(f"  tr_alt = {tr_alt_factored}")
        print(f"  net    = {net_factored}")
        print(f"  F_Pauli(q₀) = {F_val:.6f}")
        print(f"  [{elapsed:.1f}s]")
        print()

        witness['nuclei'][name] = {
            'Z': Z, 'N': N, 'A': A,
            'terms': elem.n_terms(),
            'palindromic': pal,
            'histogram': counts,
            'tr_alt_symbolic': str(tr_alt_factored),
            'tr_alt_polynomial': expose_polynomial(p['tr_alt'], q),
            'net_symbolic': str(net_factored),
            'net_polynomial': expose_polynomial(p['net'], q),
            'tr_alt_at_q0': tr_alt_val,
            'net_at_q0': net_val,
            'F_Pauli_at_q0': F_val,
            'elapsed_s': round(elapsed, 1),
        }

    out = Path(__file__).parent / 'pauli-witness.json'
    with open(out, 'w') as f:
        json.dump(witness, f, indent=2, default=str)
    print(f"Witness: {out}")
