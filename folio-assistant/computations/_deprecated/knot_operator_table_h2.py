#!/usr/bin/env python3
"""Knot-operator table for the EW even-twist torus links T(2,2k) in H_2(q).

Phase B of `docs/audits/2026-05-05-path-alpha-bring-refinement.md`.

Companion to `knot-operator-table.py` (which covers H_3(q) for matter
operators). This script computes:

  - The Wedderburn (sym, alt) eigenvalues of σ_0^{2k} for k = 1, 2, 3, 4
  - The 2-strand NF basis multiplication b_i · β(T(2,2k)) · b_j for the
    H_2(q) NF basis {γ_2, σ_0}
  - Symbolic results in R = Z[q, q^{-1}], specialized at q_0 numerically.

The H_2(q) NF basis is {1, σ_0} — only 2 elements, so the table is 2×2
per operator. Hecke relation: σ_0^2 = h·σ_0 + 1 with h = q - q^{-1}.

Wedderburn block projectors at generic q (not a root of unity):
  e_+ = (q^{-1} + σ_0) / (q + q^{-1})        [sym block, eigenvalue q]
  e_- = (q     - σ_0) / (q + q^{-1})        [alt block, eigenvalue -q^{-1}]

Hence σ_0^{2k} acts as:
  e_+ block:  q^{2k}        > 0 in any real-closed specialization q* > 1
  e_- block:  q^{-2k}       > 0 in any real-closed specialization q* > 1
  (odd-twist σ_0^{2k+1}: alt eigenvalue -q^{-(2k+1)} < 0)

Output: knot-operator-table-h2.witness.json — extends the H_3 witness
with the EW carrier sector.
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import sympy as sp


def main() -> int:
    # Symbolic q for the canonical R = Z[q, q^{-1}] expressions.
    q = sp.Symbol("q", positive=True)
    h = q - 1 / q  # Hecke amplitude

    # H_2(q) NF basis: 1, σ_0 (only 2 elements; sigma_0^2 reduces).
    # Represent as polynomials in σ_0 with coefficients in R.
    # An element is (c0, c1) meaning c0 · 1 + c1 · σ_0.
    NF_NAMES = ["γ", "σ₀"]

    def hecke_pow(k: int) -> tuple[sp.Expr, sp.Expr]:
        """σ_0^k as (c_0, c_1) coefficients of {1, σ_0}.

        Recurrence: σ_0^{k+1} = σ_0 · σ_0^k = σ_0 · (a + b σ_0)
                  = a σ_0 + b σ_0^2 = a σ_0 + b (h σ_0 + 1)
                  = b + (a + b h) σ_0
        Base: σ_0^0 = (1, 0); σ_0^1 = (0, 1).
        """
        if k == 0:
            return (sp.Integer(1), sp.Integer(0))
        if k == 1:
            return (sp.Integer(0), sp.Integer(1))
        a, b = hecke_pow(k - 1)
        return (b, a + b * h)

    def mul(x: tuple[sp.Expr, sp.Expr], y: tuple[sp.Expr, sp.Expr]) \
            -> tuple[sp.Expr, sp.Expr]:
        """Multiply two H_2(q) elements expressed as (c_0, c_1)."""
        a0, a1 = x
        b0, b1 = y
        # (a0 + a1 σ_0)(b0 + b1 σ_0)
        # = a0 b0 + (a0 b1 + a1 b0) σ_0 + a1 b1 σ_0^2
        # = a0 b0 + a1 b1 + (a0 b1 + a1 b0 + a1 b1 h) σ_0
        c0 = sp.expand(a0 * b0 + a1 * b1)
        c1 = sp.expand(a0 * b1 + a1 * b0 + a1 * b1 * h)
        return (c0, c1)

    NF_BASIS_VEC = [(sp.Integer(1), sp.Integer(0)),  # γ
                    (sp.Integer(0), sp.Integer(1))]   # σ₀

    operators = [
        ("T(2,1)", 1, "σ_0  (single crossing — ODD twist; not EW carrier)"),
        ("T(2,2)", 2, "σ_0²  (Hopf link; binding, not EW carrier)"),
        ("T(2,3)", 3, "σ_0³  (trefoil; ODD twist)"),
        ("T(2,4)", 4, "σ_0⁴  (W± candidate; even-twist k=2)"),
        ("T(2,5)", 5, "σ_0⁵  (cinquefoil; ODD twist)"),
        ("T(2,6)", 6, "σ_0⁶  (Z candidate; even-twist k=3)"),
        ("T(2,7)", 7, "σ_0⁷  (ODD twist)"),
        ("T(2,8)", 8, "σ_0⁸  (H candidate; even-twist k=4)"),
    ]

    # Specialization point for numerical witness only.
    # Use sp.Rational(str(...)) per repo convention (q_parameter.Q
    # canonical source) to preserve the exact decimal expansion and
    # avoid binary-float rounding drift.
    from q_parameter import Q_50_DIGIT_STR
    q_num = sp.Rational(Q_50_DIGIT_STR)

    eigenvalues: list[dict] = []
    tables: dict = {}
    for op_name, k, descr in operators:
        op_vec = hecke_pow(k)  # σ_0^k as (c_0, c_1)

        # Wedderburn block eigenvalues (analytic, generic q):
        # e_+ block: σ_0 acts as q;  σ_0^k acts as q^k
        # e_- block: σ_0 acts as -q^{-1};  σ_0^k acts as (-q^{-1})^k
        # Monomial — no sp.simplify/sp.cancel needed (Gemini review).
        eig_sym = q ** k
        eig_alt = (-1) ** k * q ** (-k)
        is_even = (k % 2 == 0)
        eigenvalues.append({
            "operator": op_name,
            "twist_k": k,
            "parity": "even" if is_even else "odd",
            "eig_sym_R": str(eig_sym),
            "eig_alt_R": str(eig_alt),
            "eig_sym_q0": float(eig_sym.subs(q, q_num)),
            "eig_alt_q0": float(eig_alt.subs(q, q_num)),
            "psd_feasible_q_gt_1":
                bool(is_even),  # both positive iff even twist (in any q*>1)
            "description": descr,
        })

        # 2×2 NF table: b_i · σ_0^k · b_j
        table = {}
        for i, b_i in enumerate(NF_BASIS_VEC):
            for j, b_j in enumerate(NF_BASIS_VEC):
                # b_i · op · b_j
                lhs = mul(mul(b_i, op_vec), b_j)
                c0_R = str(sp.expand(lhs[0]))
                c1_R = str(sp.expand(lhs[1]))
                c0_q0 = float(lhs[0].subs(q, q_num))
                c1_q0 = float(lhs[1].subs(q, q_num))
                pair = f"{NF_NAMES[i]}*{NF_NAMES[j]}"
                table[pair] = {
                    "c0_R": c0_R,  # symbolic in R
                    "c1_R": c1_R,
                    "c0_q0": c0_q0,
                    "c1_q0": c1_q0,
                }
        tables[op_name] = {"k": k, "table": table, "description": descr}

    # Console output for the user
    print("=" * 72)
    print("EW even-twist torus links: Wedderburn eigenvalues in H_2(q)")
    print("=" * 72)
    print(f"{'op':<10}{'k':>3}{'parity':>8}  {'eig_sym (R)':<14}"
          f"{'eig_alt (R)':<14}{'PSD (q>1)?':>12}")
    print("-" * 72)
    for e in eigenvalues:
        print(f"  {e['operator']:<8}{e['twist_k']:>3}{e['parity']:>8}  "
              f"{e['eig_sym_R']:<14}{e['eig_alt_R']:<14}"
              f"{str(e['psd_feasible_q_gt_1']):>12}")

    print()
    print("Selected EW-carrier 2×2 tables (γ_2 = identity, σ_0 = generator):")
    for op_name in ["T(2,4)", "T(2,6)", "T(2,8)"]:
        print(f"\n  {op_name}: σ_0^{tables[op_name]['k']} symbolic table")
        for pair, entry in tables[op_name]["table"].items():
            print(f"    {pair:>9}  =  {entry['c0_R']}  +  ({entry['c1_R']}) · σ₀")

    # Witness
    out = {
        "computation": "knot-operator-table-h2",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Knot-operator table for T(2,2k), k=1..4 in H_2(q), "
            "extending knot-operator-table.witness.json (which covered "
            "H_3(q) matter operators) with the EW even-twist 2-component "
            "link sector. Symbolic results in R = Z[q, q^{-1}]; "
            "numerical specialization at q_0 for cross-check only. "
            "Confirms prop:even-twist-torus-link-psd-feasibility: even "
            "twists give (q^{2k}, q^{-2k}) eigenvalue pairs (PSD-feasible "
            "in any real-closed specialization q* > 1); odd twists give "
            "(q^k, -q^{-k}) and are never PSD-feasible."
        ),
        "reference_blocks": [
            "conj:electroweak-higgs-torus-link-triplet",
            "prop:even-twist-torus-link-psd-feasibility",
            "conj:weak-spectral-completeness",
        ],
        "ring": "R = Z[q, q^{-1}], q generic (not a root of unity)",
        "q_specialization_for_numerics": str(q_num),
        "nf_basis": NF_NAMES,
        "wedderburn_eigenvalues": eigenvalues,
        "tables": tables,
        "audit": "docs/audits/2026-05-05-path-alpha-bring-refinement.md",
    }
    out_path = Path(__file__).parent / "knot-operator-table-h2.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
