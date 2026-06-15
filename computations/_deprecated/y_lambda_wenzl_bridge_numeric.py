#!/usr/bin/env python3
"""Wenzl-bridge y_λ — numeric mpmath version (bypasses sympy symbolic).

Bypasses both bottlenecks of the prior scripts:
  • y_lambda_mpfr_witness.py — needs 462x462 MPFR matmul (>45min at n=12)
  • y_lambda_wenzl_bridge_extended.py — sp.simplify recursion error at n>12

Strategy: evaluate the Schur principal-specialization closed form
*numerically* in mpmath at q=q_0 directly — no symbolic
simplification, no matrix multiplication. The Wenzl-bridge formula

  y_λ(q) = s_λ(1, Q, Q², ..., Q^{r-1}) / Σ_µ d_µ s_µ(...)

with Q = q² and r solved from the bridge equation
q·z = Q^r (1-Q)/(1-Q^r), z = 1/(q^{1/2} + q^{-1/2}), evaluates to

  X := Q^r = qz / (1 - Q + qz),
  s_λ = Q^{n(λ)} · Π_{cells (i,j)} (1 - Q^{r+c(x)}) / (1 - Q^{h(x)})

where n(λ) = Σ i · λ_i (over rows), c(x) = j-i (content), h(x) is
the cell's hook length. With X = Q^r known numerically, write
Q^{r+c} = X · Q^c, so the formula is *purely arithmetic* in Q and X.

Output: y-lambda-wenzl-bridge-numeric-witness.json with tables_by_n
for n = 2..18 at 50 dps, plus FROB-FILTER signatures (p_n, q_n) for
each.
"""
from __future__ import annotations
import json, sys
from datetime import datetime, timezone
from pathlib import Path
import mpmath
mpmath.mp.dps = 50

from math import factorial as _fact

q0_str = "1.10997859555418051695830018898879867637876138498395"
q = mpmath.mpf(q0_str)
Q = q * q
z = 1 / (mpmath.sqrt(q) + 1 / mpmath.sqrt(q))
qz = q * z
X = qz / (1 - Q + qz)   # X = Q^r
print(f"q  = {mpmath.nstr(q, 12)}")
print(f"Q  = q² = {mpmath.nstr(Q, 12)}")
print(f"qz = {mpmath.nstr(qz, 12)}")
print(f"X  = Q^r = qz/(1 - Q + qz) = {mpmath.nstr(X, 12)}")
print()


def f_lambda(p):
    n = sum(p)
    cols = max(p) if p else 0
    conj = [sum(1 for r in p if r > j) for j in range(cols)]
    hp = 1
    for i, rl in enumerate(p):
        for j in range(rl):
            arm = rl - j - 1
            leg = conj[j] - i - 1
            hp *= arm + leg + 1
    return _fact(n) // hp


def n_partition(lam):
    return sum(i * li for i, li in enumerate(lam))


def hooks_contents(lam):
    hs, cs = [], []
    rows = len(lam)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hs.append(arm + leg + 1)
            cs.append(j - i)
    return hs, cs


def schur_principal_numeric(lam):
    """s_λ(1, Q, ..., Q^{r-1}) at q=q_0, using X = Q^r.

    s_λ = Q^{n(λ)} · Π (1 - X · Q^c) / (1 - Q^h)
    """
    hs, cs = hooks_contents(lam)
    num = mpmath.mpf(1)
    den = mpmath.mpf(1)
    for h, c in zip(hs, cs):
        num *= (1 - X * Q**c)
        den *= (1 - Q**h)
    return Q**n_partition(lam) * num / den


def partitions(n, max_part=None):
    if max_part is None: max_part = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def main():
    out_path = Path(__file__).parent / "y-lambda-wenzl-bridge-numeric-witness.json"
    tables_by_n = {}
    signature_table = []

    print(f"{'n':>3} {'p(n)':>5} {'time':>8} {'p_n':>15} {'q_n':>15} {'%neg':>7} {'q>p?':>5}")
    print("-" * 70)
    import time
    for n in range(2, 19):
        t0 = time.time()
        # Compute s_λ for each partition + sum to get Z
        s_values = {}
        for lam in partitions(n):
            s_values[lam] = schur_principal_numeric(lam)
        Z = sum(f_lambda(lam) * s_values[lam] for lam in s_values)
        # y_λ = s_λ · f_λ / Z (with the f_λ weight built in to match the
        # paper's normalization where Σ f_λ y_λ = 1 at the Markov-trace level)
        # Actually y_λ = s_λ / Z (per the original script). Verify by checking
        # Markov-trace normalization: Σ y_λ · f_λ should equal Σ f_λ · s_λ / Z = 1. ✓
        weights = []
        pos_f2 = 0; neg_f2 = 0; pos = 0; neg = 0
        for lam in s_values:
            yl = s_values[lam] / Z
            f = f_lambda(lam)
            yl_float = float(yl)
            # Sign-of mpmath: precision-adaptive, no hardcoded threshold.
            sign = '+' if yl > 0 else ('-' if yl < 0 else '0')
            weights.append({
                "partition": list(lam),
                "y_lambda_numeric": mpmath.nstr(yl, 30),
                "y_lambda_float": yl_float,
                "f_lambda": f,
                "sign": sign,
            })
            if yl > 0:
                pos_f2 += f*f; pos += 1
            elif yl < 0:
                neg_f2 += f*f; neg += 1
        elapsed = time.time() - t0
        n_parts = len(s_values)
        pct_neg = 100 * neg_f2 / (pos_f2 + neg_f2) if (pos_f2 + neg_f2) > 0 else 0
        flag = 'YES' if neg_f2 > pos_f2 else 'no'
        print(f"{n:>3} {n_parts:>5} {elapsed:>7.2f}s {pos_f2:>15} {neg_f2:>15} {pct_neg:>6.2f}% {flag:>5}")
        tables_by_n[str(n)] = {
            "n": n,
            "num_partitions": n_parts,
            "weights": weights,
            "signature": {
                "pos_f_squared": pos_f2,
                "neg_f_squared": neg_f2,
                "pos_count": pos,
                "neg_count": neg,
                "pct_neg": pct_neg,
            },
        }
        signature_table.append({
            "n": n,
            "A": n // 3 if n % 3 == 0 else None,
            "p_n": pos_f2,
            "q_n": neg_f2,
            "pct_neg": pct_neg,
            "q_dominant": neg_f2 > pos_f2,
        })

    witness = {
        "computation": "y-lambda-wenzl-bridge-numeric",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Numeric mpmath evaluation of y_λ via the Wenzl-bridge "
            "Schur principal-specialization closed form. Bypasses both "
            "sympy symbolic recursion error and Rust-MPFR matmul cost. "
            "Covers n=2..18 with FROB-FILTER signatures per A=n/3."
        ),
        "q0": q0_str,
        "Q_eq_qsq": mpmath.nstr(Q, 30),
        "X_eq_Qr": mpmath.nstr(X, 30),
        "precision_dps": mpmath.mp.dps,
        "tables_by_n": tables_by_n,
        "frob_filter_signature_table": signature_table,
        "interpretation": (
            "p_n = Σ f_λ² over y_λ(q_0) > 0 partitions; q_n = same for "
            "y_λ < 0. The FROB-FILTER conjecture predicts that the "
            "atomic-number A_** at which Σ_FP becomes mandatory "
            "(witnessed empirically at A=6 in branching-qvalues.witness.json) "
            "corresponds to the smallest A with q_{3A} dominantly exceeding "
            "p_{3A}."
        ),
    }
    with open(out_path, "w") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n→ wrote {out_path}")


if __name__ == "__main__":
    main()
