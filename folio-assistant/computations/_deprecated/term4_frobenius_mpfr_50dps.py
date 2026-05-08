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

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
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

    # Extend to n=7..11. For n ≤ 9 use the symbolic-then-substitute
    # path (still feasible with sp.cancel, completes in seconds). For
    # n ≥ 10 the symbolic q-hook product blows up combinatorially
    # (42 partitions at n=10, 56 at n=11; each needs a degree-O(n²)
    # rational reduction). Instead we substitute q=q_0 (mpf @ 50 dps)
    # at the per-hook level and sum mpf scalars — purely numeric, no
    # sympy reduction needed since each 1/dim_q(λ) is already a single
    # mpf number once q is fixed.
    q_mpf = mpf(q_str)
    _q_int_cache: dict = {}

    def q_int_mpf(k):
        if k in _q_int_cache:
            return _q_int_cache[k]
        v = mpf(0) if k == 0 else sum(q_mpf ** (k - 1 - 2 * i) for i in range(k))
        _q_int_cache[k] = v
        return v

    def dim_q_mpf(partition):
        n_local = sum(partition)
        hooks = []
        for i, rl in enumerate(partition):
            for j in range(rl):
                arm = rl - j - 1
                leg = sum(1 for r2 in range(i + 1, len(partition)) if partition[r2] > j)
                hooks.append(arm + leg + 1)
        num = mpf(1)
        for k in range(1, n_local + 1):
            num *= q_int_mpf(k)
        den = mpf(1)
        for h in hooks:
            den *= q_int_mpf(h)
        return num / den

    # All n ≥ 7 take the numeric-only path (substitute q=q_0 at the
    # per-hook level and sum mpf scalars). Memoized q_int_mpf makes this
    # ~milliseconds even for n=11 (56 partitions). Sympy reduction is
    # avoided because for our purposes the q-rational symbolic form is
    # not needed downstream — only the value at q_0 to 50 dps.
    for n in (7, 8, 9, 10, 11):
        at_q0_mpf = mpf(0)
        for lam in partitions_of(n):
            at_q0_mpf += mpf(1) / dim_q_mpf(lam)
        term4 = M_E_MEV * at_q0_mpf
        rows.append({
            "n": n,
            "total_symbolic": "(numeric path: q substituted at per-hook level)",
            "total_at_q0_50dps": str(at_q0_mpf),
            "term4_b_pred_mev_50dps": str(term4),
            "f64_baseline": None,
        })
        print(f"\n  === n={n} (numeric q=q_0) ===")
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
