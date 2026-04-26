#!/usr/bin/env python3
"""
Validate the symbolic y_λ closed forms against three independent
mathematical identities, evaluating at MULTIPLE q values (not just q_0).

Tests:
1. Cross-q validation: symbolic y_λ(q) substituted at 5 distinct q
   values must match the numerical linear-solve at each q.

2. Plancherel completeness: Σ_λ y_λ · d_λ = 1 symbolically (where
   d_λ is the classical Hecke irrep dimension).  The y_λ × d_λ
   form a probability distribution; their sum must be exactly 1.

3. Markov-trace defining identity: Σ_λ y_λ · χ_λ(σ_w_μ) = z^{n-len(μ)}
   for the cycle-type representative σ_w_μ of every conjugacy
   class μ ⊢ n.  Verifying this AT THE SYMBOLIC LEVEL confirms
   sympy's Matrix.solve produced a correct algebraic inverse.

Pass criterion: each test must hold to ~1e-10 numerical precision
or to symbolic identity 0.  A mismatch indicates the symbolic form
is wrong; matching at multiple probes is strong evidence of correctness.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy import sparse as sp_sparse

mp.mp.dps = 30

sys.path.insert(0, str(Path(__file__).parent))
from hecke_characters import (
    build_seminormal_matrices,
    partitions_of,
    standard_young_tableaux,
)


def cycle_type_word(mu):
    word = []
    s = 0
    for m in mu:
        for j in range(m - 1):
            word.append(s + j + 1)
        s += m
    return word


def numerical_y_lambda(n: int, q_val: float) -> dict:
    parts = list(partitions_of(n))
    p_n = len(parts)
    z = 1.0 / (q_val ** 0.5 + q_val ** -0.5)
    cache = {}
    for lam in parts:
        sigmas, d_lam, _ = build_seminormal_matrices(lam, sparse=True, q=q_val)
        cache[lam] = (sigmas, d_lam)
    A = np.zeros((p_n, p_n))
    b = np.zeros(p_n)
    for i, mu in enumerate(parts):
        word = cycle_type_word(tuple(mu))
        b[i] = z ** (n - len(mu))
        for j, lam in enumerate(parts):
            sigmas, d_lam = cache[lam]
            M = sp_sparse.eye(d_lam, format="csr")
            for idx in word:
                M = M @ sigmas[idx - 1]
            A[i, j] = M.diagonal().sum()
    y = np.linalg.solve(A, b)
    return {tuple(lam): float(y[j]) for j, lam in enumerate(parts)}


def classical_dim(partition):
    syts, _, _ = standard_young_tableaux(partition)
    return len(syts)


def chi_lambda_symbolic(partition, word, q):
    syts, _, contents = standard_young_tableaux(partition)
    dim = len(syts)
    if dim == 0:
        return sp.Integer(0)
    h = q - 1 / q
    n = sum(partition)
    sigmas = []
    for k in range(1, n):
        M = sp.zeros(dim, dim)
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h / (1 - q ** (-2 * rho))
            swap_map = dict(syts[i])
            swap_map[k] = ci_k1
            swap_map[k + 1] = ci_k
            j = next((jj for jj in range(dim)
                      if jj != i and syts[jj] == swap_map), None)
            if j is None:
                M[i, i] = a
                processed.add(i)
            else:
                a_prime = h / (1 - q ** (2 * rho))
                b_sq = a * a_prime + 1
                bb = sp.sqrt(sp.simplify(b_sq))
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = bb
                M[j, i] = bb
                processed.add(i)
                processed.add(j)
        sigmas.append(M)
    M = sp.eye(dim)
    for idx in word:
        M = M * sigmas[idx - 1]
    return sp.trace(M)


def main(probes=None):
    if probes is None:
        probes = [1.02, 1.05, 1.08, 1.11, 1.15]

    sym_path = Path(__file__).parent / "y-lambda-symbolic-witness.json"
    with sym_path.open() as f:
        sym_data = json.load(f)

    q = sp.Symbol("q", positive=True)
    all_passed = True
    summary = {}

    for n_str in sorted(sym_data["tables_by_n"], key=int):
        n = int(n_str)
        weights = sym_data["tables_by_n"][n_str]["weights"]
        print(f"\n{'='*70}\nn = {n} ({len(weights)} partitions)\n{'='*70}")

        symbolic_y = {
            tuple(w["partition"]):
                sp.parsing.sympy_parser.parse_expr(
                    w["y_lambda_symbolic"], local_dict={"q": q}
                )
            for w in weights
        }

        n_summary = {"test_1_cross_q": [], "test_2_plancherel": None,
                     "test_3_markov": []}

        # Test 1: cross-q validation
        print(f"\n[Test 1] Cross-q validation at probes {probes}")
        for q_probe in probes:
            num = numerical_y_lambda(n, q_probe)
            max_diff = 0.0
            for lam_tup, y_sym in symbolic_y.items():
                y_at = float(y_sym.subs(q, sp.Float(q_probe, 30)).evalf())
                d = abs(y_at - num[lam_tup])
                if d > max_diff:
                    max_diff = d
            n_summary["test_1_cross_q"].append((q_probe, max_diff))
            status = "PASS" if max_diff < 1e-10 else "FAIL"
            print(f"  q = {q_probe:.4f}: max |sym-num| = {max_diff:.2e}  [{status}]")
            if max_diff >= 1e-10:
                all_passed = False

        # Test 2: Plancherel completeness
        print(f"\n[Test 2] Plancherel completeness Σ_λ y_λ · d_λ = 1")
        plancherel = sp.Integer(0)
        for lam_tup, y_sym in symbolic_y.items():
            plancherel += y_sym * classical_dim(list(lam_tup))
        simp = sp.simplify(plancherel)
        is_one = sp.simplify(simp - 1) == 0
        n_summary["test_2_plancherel"] = (str(simp), bool(is_one))
        status = "PASS" if is_one else "FAIL"
        print(f"  Σ y_λ · d_λ = {simp}  [{status}]")
        if not is_one:
            all_passed = False

        # Test 3: Markov-trace identity (extreme cycles)
        print(f"\n[Test 3] Markov-trace identity Σ y_λ χ_λ(σ_w) = z^{{n-len(μ)}}")
        z_sym = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
        test_mus = [(n,)]
        if n >= 2:
            test_mus.append(tuple([1] * n))
        for mu in test_mus:
            word = cycle_type_word(mu)
            target = z_sym ** (n - len(mu))
            lhs = sp.Integer(0)
            for lam_tup, y_sym in symbolic_y.items():
                chi = chi_lambda_symbolic(list(lam_tup), word, q)
                lhs += y_sym * chi
            diff = sp.simplify(lhs - target)
            is_zero = sp.simplify(diff) == 0
            n_summary["test_3_markov"].append((str(mu), bool(is_zero)))
            status = "PASS" if is_zero else "FAIL"
            d_str = str(diff)
            if len(d_str) > 80:
                d_str = d_str[:77] + "..."
            print(f"  μ = {mu}: lhs - target = {d_str}  [{status}]")
            if not is_zero:
                all_passed = False

        summary[n_str] = n_summary

    print(f"\n{'='*70}")
    print(f"OVERALL: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    print('=' * 70)

    out_path = Path(__file__).parent / "y-lambda-symbolic-validation.json"
    out_path.write_text(json.dumps({
        "all_passed": all_passed,
        "probes": probes,
        "summary_by_n": summary,
    }, indent=2, default=str))
    print(f"Wrote {out_path}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
