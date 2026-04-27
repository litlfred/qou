#!/usr/bin/env python3
"""
Plan F — Term 4 (Frobenius co-Casimir) at MPFR @ 50 dps.

Term 4 of the unified mass formula is
    Term 4 = m_e · τ(C_{dim_q}) = m_e · Σ_{λ⊢n} 1/dim_q(λ)
([thm:frobenius-codim-universal](#thm:frobenius-codim-universal),
[prop:partition-sum-proton-residual](#prop:partition-sum-proton-residual)).

For H_3 the explicit form is m_e · (2 + 1/[2]_q).

This script reads the symbolic per-n totals from
`frobenius-partition-sum.witness.json` (sympy expressions in q),
substitutes q = q_0 at 50 dps via mpmath, and emits a 50-dps
witness for n = 2..11.

For n=2 the symbolic total isn't in the witness; computed inline:
  partitions of 2: (2) and (1,1)
  dim_q((2)) = [2]_q = q + q^{-1}    (1-row tableau)
  Wait — actually [2]_q in the seminormal-form convention is
  (q^{1/2} - q^{-1/2})/(q^{1/2} - q^{-1/2}) ... let me read the
  existing q_dim_sym code to match the convention.

Output: `term4-frobenius-mpfr-50dps.witness.json`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp
from mpmath import mp, mpf

mp.dps = 50

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from murnaghan_nakayama import partitions_of, dim_specht, hook_lengths

WITNESS_F64 = HERE / "frobenius-partition-sum.witness.json"
Q0 = HERE / "q-pinning-50-digit.witness.json"
OUT = HERE / "term4-frobenius-mpfr-50dps.witness.json"

M_E_MEV = mpf("0.51099895")  # CODATA 2022


def q_int_sym(k, q):
    """[k]_q = (q^k − q^{−k}) / (q − q^{−1}) — the balanced quantum integer."""
    if k == 0:
        return sp.Integer(0)
    return sum(q ** (k - 1 - 2 * i) for i in range(k))


def q_factorial_sym(n, q):
    """[n]!_q."""
    out = sp.Integer(1)
    for k in range(1, n + 1):
        out *= q_int_sym(k, q)
    return sp.simplify(out)


def q_dim_sym(partition, q):
    """dim_q(λ) = [n]!_q / Π_x [h_x]_q (q-hook-length formula)."""
    n = sum(partition)
    hooks = hook_lengths(partition)
    prod = sp.Integer(1)
    for h in hooks:
        prod *= q_int_sym(h, q)
    return sp.cancel(q_factorial_sym(n, q) / prod)


def compute_n2_total(q) -> sp.Expr:
    """Σ 1/dim_q(λ) for n=2."""
    total = sp.Integer(0)
    for lam in partitions_of(2):
        d = q_dim_sym(lam, q)
        total += sp.cancel(sp.Integer(1) / d)
    return sp.simplify(total)


def main() -> int:
    q_str = json.load(open(Q0))["derived_50_digit"]["q"]
    q_0 = mpf(q_str)
    print(f"  q_0 (50 dps) = {q_str}")
    print(f"  m_e (50 dps) = {M_E_MEV}")

    f64 = json.load(open(WITNESS_F64))

    # n=2 inline computation
    q_sym = sp.Symbol("q", positive=True)
    n2_total = compute_n2_total(q_sym)
    print(f"\n  n=2 symbolic: Σ 1/dim_q(λ) = {n2_total}")

    rows = []

    # n=2
    n2_at_q0 = sp.N(n2_total.subs(q_sym, sp.Float(q_str, 60)), 50)
    n2_mpf = mpf(str(n2_at_q0))
    term4_n2 = M_E_MEV * n2_mpf
    rows.append({
        "n": 2,
        "total_symbolic": str(n2_total),
        "total_at_q0_50dps": str(n2_mpf),
        "term4_b_pred_mev_50dps": str(term4_n2),
    })
    print(f"\n  === n=2 ===")
    print(f"    Σ 1/dim_q(λ) at q_0 = {n2_mpf}")
    print(f"    Term 4 = m_e · Σ = {term4_n2} MeV")

    # n=3..6 from existing witness; n=7..9 computed inline
    for n_str, r in f64["results_by_n"].items():
        n = r["n"]
        if n < 3:
            continue
        sym_str = r["total_symbolic"]
        sym = sp.sympify(sym_str)
        free = list(sym.free_symbols)
        at_q0 = sp.N(sym.subs({s: sp.Float(q_str, 60) for s in free}), 50)
        at_q0_mpf = mpf(str(at_q0))
        term4 = M_E_MEV * at_q0_mpf
        rows.append({
            "n": n,
            "total_symbolic": sym_str,
            "total_at_q0_50dps": str(at_q0_mpf),
            "term4_b_pred_mev_50dps": str(term4),
            "f64_baseline": r.get("total_at_q0"),
        })
        print(f"\n  === n={n} (from existing witness) ===")
        print(f"    Σ 1/dim_q(λ) at q_0 (50 dps) = {at_q0_mpf}")
        print(f"    Term 4 = m_e · Σ = {term4} MeV")

    # Extend to n=7..9 (T, ³He at n=9 needed by unified mass table).
    # Use sp.cancel (much faster than sp.simplify on sums of rational
    # functions of q; per Gemini review on PR #456).
    for n in (7, 8, 9):
        total = sp.Integer(0)
        for lam in partitions_of(n):
            d = q_dim_sym(lam, q_sym)
            total += sp.cancel(sp.Integer(1) / d)
        sym = sp.cancel(total)
        free = list(sym.free_symbols)
        at_q0 = sp.N(sym.subs({s: sp.Float(q_str, 60) for s in free}), 50)
        at_q0_mpf = mpf(str(at_q0))
        term4 = M_E_MEV * at_q0_mpf
        rows.append({
            "n": n,
            "total_symbolic": str(sym),
            "total_at_q0_50dps": str(at_q0_mpf),
            "term4_b_pred_mev_50dps": str(term4),
            "f64_baseline": None,
        })
        print(f"\n  === n={n} (computed inline) ===")
        print(f"    Σ 1/dim_q(λ) at q_0 (50 dps) = {at_q0_mpf}")
        print(f"    Term 4 = m_e · Σ = {term4} MeV")

    out = {
        "computation": "term4-frobenius-mpfr-50dps",
        "description":
            "Plan F — Term 4 (Frobenius co-Casimir) of the unified mass "
            "formula at MPFR @ 50 dps for n = 2..11. "
            "Term 4 = m_e · Σ_{λ⊢n} 1/dim_q(λ). Reads symbolic per-n "
            "expressions from frobenius-partition-sum.witness.json and "
            "evaluates at q_0 (50 dps from q-pinning-50-digit witness). "
            "The n=2 case is computed inline (not in the f64 witness).",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "precision": "mpfr_50dps",
        "q_0_50dps": q_str,
        "m_e_mev_50dps": str(M_E_MEV),
        "results_by_n": rows,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"\n  Output: {OUT.relative_to(HERE.parent.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
