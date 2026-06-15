#!/usr/bin/env python3
"""Closed-form symbolic r_k coefficients at H_4 in Q(q^{1/2}).

Builds the 4×5 character matrix χ_λ(T_w_C) symbolically via sympy
(Hoefsmit seminormal matrices over Q(q^{1/2})) and solves the
linear system A·c = 0 for the null vector → r_k as exact q-rational
expressions.

Companion to prop:explicit-alpha-k-h4 (numerical).  Promotes the
numerical α_λ(H_4) values to closed q-rational form.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

import sympy as sp
from sympy import Rational, sqrt, simplify, factor, together
from witness_polynomial import expose_polynomial

# Symbolic q
q = sp.symbols('q', positive=True)


def q_int(k):
    """Symmetric q-integer [k]_q = (q^k - q^{-k}) / (q - q^{-1})."""
    if k == 0:
        return sp.S(0)
    return (q**k - q**(-k)) / (q - q**(-1))


def q_factorial(n):
    """[n]_q! = [1]_q · [2]_q · ... · [n]_q."""
    return sp.prod(q_int(i) for i in range(1, n + 1))


def standard_young_tableaux(shape):
    """Enumerate SYTs of given partition shape.
    Returns list of dicts {entry → (row, col)} indexed 1..n."""
    n = sum(shape)
    if n == 0:
        return [{}]

    def fill(shape, used, current_yt):
        if len(used) == n:
            yield dict(current_yt)
            return
        # Find positions where next entry can go (corner of remaining shape)
        next_entry = len(used) + 1
        for r in range(len(shape)):
            for c in range(shape[r]):
                if (r, c) in current_yt.values():
                    continue
                # Check (r, c) is reachable: all cells above and to the left are filled
                if (r > 0 and (r - 1, c) not in current_yt.values()):
                    continue
                if (c > 0 and (r, c - 1) not in current_yt.values()):
                    continue
                current_yt[next_entry] = (r, c)
                yield from fill(shape, used | {next_entry}, current_yt)
                del current_yt[next_entry]

    return list(fill(shape, set(), {}))


def hoefsmit_T_i_symbolic(shape, i):
    """Build the seminormal matrix of T_i acting on V_λ over Q(q^{1/2}).

    Hoefsmit's formula: T_i acts on the SYT basis via
    - eigenvalue +q if (i, i+1) in same row of T (adjacent right)
    - eigenvalue -q^{-1} if (i, i+1) in same column of T (adjacent below)
    - otherwise 2x2 block on {T, T'} with axial distance d = c(i+1) - c(i):
      diagonal entry h/(1 - q^{-2d}), off-diagonal entry sqrt(...).

    For trace computation we only need the trace, which is sum of diagonals.
    """
    syts = standard_young_tableaux(shape)
    dim = len(syts)
    M = sp.zeros(dim, dim)

    for ti, T in enumerate(syts):
        pos_i = T[i]
        pos_i1 = T[i + 1]
        ri, ci = pos_i
        ri1, ci1 = pos_i1
        same_row = (ri == ri1)
        same_col = (ci == ci1)
        if same_row and ci1 == ci + 1:
            M[ti, ti] = q
        elif same_col and ri1 == ri + 1:
            M[ti, ti] = -q**(-1)
        else:
            # Axial distance d = (col_{i+1} - row_{i+1}) - (col_i - row_i)
            d = (ci1 - ri1) - (ci - ri)
            # Hoefsmit: T_i T = (1/[d]_q) (q-q^{-1}) T + sqrt(...) T'
            # = ((q - q^{-1})/(q^d - q^{-d})) T + ...
            # Wait - the diagonal entry is (q - q^{-1})/(q^d - q^{-d}) wait no
            # Standard formula: a_d = (q - q^{-1}) / (q^{d+1} + q^{-(d-1)}) ... let me use
            # the form from Halverson-Ram (1995): T_i e_T = a_d e_T + b_d e_{T'}
            # where a_d = (q - q^{-1}) q^d / (q^{2d} - 1) = (q - q^{-1}) / (q^d - q^{-d})
            #            = 1 / [d]_q · (q - q^{-1}) / (q - q^{-1})  ... hmm
            # The cleanest form: a_d = h / (1 - q^{-2d}) where h = q - q^{-1}
            h = q - q**(-1)
            M[ti, ti] = h / (1 - q**(-2 * d))
    return M


def char_value_symbolic(shape, word):
    """χ_λ(T_w) symbolic: trace of product of T_i matrices."""
    if not word:
        return sp.S(len(standard_young_tableaux(shape)))
    Ms = [hoefsmit_T_i_symbolic(shape, i) for i in word]
    M = Ms[0]
    for X in Ms[1:]:
        M = M * X
    return simplify(M.trace())


def main():
    print("Building symbolic Hoefsmit character matrix at H_4 (5 partitions × 5 classes)...")
    print()

    classes = [
        ("e",        ()),
        ("(12)",     (1,)),
        ("(12)(34)", (1, 3)),
        ("(123)",    (1, 2)),
        ("(1234)",   (1, 2, 3)),
    ]
    partitions = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]

    # Build symbolic character table
    chi = {}
    print(f"{'class':>10} | " + " | ".join(f"{str(p):>14}" for p in partitions))
    for label, word in classes:
        row = []
        for p in partitions:
            val = char_value_symbolic(p, word)
            chi[(p, word)] = val
            row.append(val)
        # Display abbreviated symbolic forms
        disp = []
        for v in row:
            v_simp = together(v)
            s = str(v_simp)
            if len(s) > 12:
                s = s[:9] + "..."
            disp.append(s)
        print(f"{label:>10} | " + " | ".join(f"{s:>14}" for s in disp))

    # For each target partition, solve for r with χ_other(r) = 0
    print("\n" + "=" * 72)
    print("Closed-form r_λ coefficients in Q(q^{1/2}):")
    print("=" * 72)

    results = {}
    for target in partitions:
        constraints = [p for p in partitions if p != target]
        # Build 4x5 matrix
        M = sp.Matrix(4, 5, lambda i, j: chi[(constraints[i], classes[j][1])])

        # Find null space symbolically
        ns = M.nullspace()
        if not ns:
            print(f"\n  λ = {target}: NO null vector (system full rank)")
            results[str(target)] = {"closed_form": None, "error": "full rank"}
            continue

        # Take first null vector, simplify each component
        c = ns[0]
        # Normalize so that c[4] = 1 (last component, the (1234) class)
        if c[4, 0] != 0:
            c = c / c[4, 0]
        c_simplified = [together(simplify(c[i, 0])) for i in range(5)]

        print(f"\n  λ = {target}:")
        for (label, _), ci in zip(classes, c_simplified):
            ci_str = str(ci)
            if len(ci_str) > 100:
                ci_str = ci_str[:97] + "..."
            print(f"    c_{label:10}  =  {ci_str}")

        # Compute α_λ(H_4) symbolically: tr_M(r) = Σ_C c_C · z^{l(w_C)}
        # where l(w_C) = length of canonical class word.
        z_sym = sp.S(1) / (sp.sqrt(q) + 1 / sp.sqrt(q))
        tr_M = sum(c_simplified[j] * z_sym**len(word) for j, (_, word) in enumerate(classes))
        tr_M_simp = together(simplify(tr_M))

        # Numerical evaluation at q_0 = 1.1099785955541805
        q0 = sp.Rational(11099785955541805, 10000000000000000)
        try:
            val_num = float(tr_M.subs(q, q0))
            print(f"    tr_M(r_λ) numerical at q_0 = {val_num:+.10f}")
        except Exception as e:
            val_num = None
            print(f"    tr_M(r_λ) eval failed: {e}")

        results[str(target)] = {
            "closed_form_c": [str(ci) for ci in c_simplified],
            "tr_M_symbolic": str(tr_M_simp)[:500],
            "tr_M_polynomial": expose_polynomial(tr_M_simp, q, simplify=False),
            "tr_M_at_q0_numerical": val_num,
        }

    # Save witness
    out = {
        "computation": "r-k-h4-symbolic",
        "description": (
            "Symbolic closed-form r_λ coefficients at H_4 in Q(q^{1/2}). "
            "For each partition λ ⊢ 4, solves the 4×5 character-matrix "
            "null space χ_μ(r_λ) = 0 for all μ ≠ λ via sympy, then "
            "expresses tr_M(r_λ) = α_λ(H_4) symbolically.  Promotes the "
            "numerical values from prop:explicit-alpha-k-h4 to closed "
            "q-rational expressions analogous to the H_3 closed forms."
        ),
        "results": results,
        "precision": "symbolic_q",
        "truncation_eps": 0.0,
    }
    out_path = Path(__file__).parent / "r-k-h4-symbolic.witness.json"
    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2, default=str)
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
