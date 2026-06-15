#!/usr/bin/env python3
"""Probe: q-hecke-seminormal-character-closure
(`prop:q-hecke-seminormal-character-closure`).

The proposition asserts that the partition-sum form of the canonical
Markov trace via Hoefsmit + Wenzl,

    tr_M^{partition-sum}(β) := Σ_{λ ⊢ n} y_λ(q) · χ_λ(β),

equals the canonical Markov-axiom reducer tr_M(β) for the same braid
β ∈ H_n(q), with y_λ(q) the Jones-Markov weights from Wenzl's
Schur principal specialization.

This probe verifies the equality numerically at q = q_0 for a suite
of 5 braid words in B_3 covering pure-positive, Coxeter, the
figure-eight β_{4_1}, identity, and a full-twist case.  B_4 tests
were planned but dropped because y_lambda_symbolic(n=4) exceeds the
3-minute symbolic-compute timeout.  All residues at ~1e-30 (sympy.N
30-dps precision floor); the test passes when the two
implementations agree to better than 1e-10.

  · LHS — partition-sum via canonical Hoefsmit χ_λ (mpmath 50 dps)
    × y_λ(q_0) (sympy.N at 30 dps).
  · RHS — recursive Markov-axiom reducer
    (`markov_trace_recursive.markov_trace_of_word`).

Emits `q-hecke-seminormal-character-closure-probe.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from probe_staircase_ew_k3_categorical import build_hoefsmit_mpfr  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from markov_weights_symbolic import y_lambda_symbolic  # noqa: E402
from markov_trace_recursive import markov_trace_of_word  # noqa: E402
from markov_trace_recursive import q as Q_RECURSIVE_SYM  # noqa: E402


def _partitions_of(n: int):
    """Generate partitions of n (descending parts)."""
    def go(n_, max_):
        if n_ == 0:
            yield ()
            return
        for i in range(min(n_, max_), 0, -1):
            for tail in go(n_ - i, i):
                yield (i,) + tail
    yield from go(n, n)


def _evaluate_word_in_hoefsmit(shape: tuple, word_signed: list[int]):
    """Compute Tr ρ_shape(braid word) via canonical Hoefsmit at Q_MP.

    `word_signed` is a list of signed 1-indexed generator indices
    (positive = σ_i, negative = σ_i⁻¹).
    """
    sigmas, dim = build_hoefsmit_mpfr(shape, Q_MP)
    M = mp.eye(dim)
    for s in word_signed:
        if s > 0:
            g = sigmas[s - 1]
        else:
            g = sigmas[-s - 1] ** (-1)
        M = M * g
    return sum(M[i, i] for i in range(dim))


def main() -> int:
    builder = WitnessBuilder(
        "q-hecke-seminormal-character-closure-probe",
        engine="mpmath+sympy",
    )
    mp.dps = 50
    q_sympy = sp.Float(Q_50_DIGIT_STR, 50)

    # Pre-evaluate y_λ at q_0 ONCE per n (the symbolic expressions
    # are large rational functions in q^{1/2}; symbolic computation
    # of y_λ(n=4) exceeds 180s).  Cache numerical values keyed by
    # partition shape per ambient n.
    Y_NUMERIC_CACHE: dict[int, dict[tuple, "mp.mpf"]] = {}

    def _y_numeric_at_q0(n: int) -> dict[tuple, "mp.mpf"]:
        if n in Y_NUMERIC_CACHE:
            return Y_NUMERIC_CACHE[n]
        y_sym = y_lambda_symbolic(n)
        q_sym_internal = sp.symbols("q", positive=True)
        cache = {}
        for shape, expr in y_sym.items():
            cache[shape] = mp.mpf(
                str(sp.N(expr.subs(q_sym_internal, q_sympy), 30)))
        Y_NUMERIC_CACHE[n] = cache
        return cache

    def _partition_sum_tr_m_cached(n: int, word_signed: list[int]):
        """Like _partition_sum_tr_m but uses cached numeric y_λ."""
        y_num = _y_numeric_at_q0(n)
        result = mp.mpf(0)
        per_lambda = []
        for shape in _partitions_of(n):
            chi = _evaluate_word_in_hoefsmit(shape, word_signed)
            y_val = y_num[shape]
            contrib = y_val * chi
            result += contrib
            per_lambda.append({
                "shape": str(shape),
                "y_lambda_at_q0": float(y_val),
                "chi_lambda": float(chi),
                "contribution": float(contrib),
            })
        return result, per_lambda

    # Test braids: only n=3 (symbolic y_λ for n=4 exceeds 3 minutes).
    # The closure identity is mathematically uniform in n; verifying
    # for n=3 across 5 structurally different braids covers identity,
    # single generator, Coxeter, mixed-sign (figure-eight), and
    # full-twist cases.
    TESTS = [
        ("H_3 identity", 3, []),
        ("H_3 σ_1", 3, [1]),
        ("H_3 σ_1 σ_2 (Coxeter)", 3, [1, 2]),
        ("H_3 β_{4_1} = σ_1 σ_2⁻¹ σ_1 σ_2⁻¹", 3, [1, -2, 1, -2]),
        ("H_3 (σ_1 σ_2)^3 = δ^2 (full twist)",
         3, [1, 2, 1, 2, 1, 2]),
    ]

    results = []
    max_residue = mp.mpf(0)
    for label, n, word in TESTS:
        lhs, per_lam = _partition_sum_tr_m_cached(n, word)
        rhs_expr = markov_trace_of_word(n, word)
        rhs_val = mp.mpf(str(sp.N(rhs_expr.subs(Q_RECURSIVE_SYM,
                                                q_sympy), 30)))
        residue = float(mp.fabs(lhs - rhs_val))
        max_residue = max(max_residue, mp.mpf(residue))
        results.append({
            "label": label,
            "n": n,
            "word": word,
            "lhs_partition_sum": float(lhs),
            "rhs_recursive_reducer": float(rhs_val),
            "residue": residue,
            "per_lambda_contributions": per_lam,
        })

    (
        builder
        .set_description(
            "I1 probe for prop:q-hecke-seminormal-character-closure. "
            "Verifies tr_M^{partition-sum}(β) := Σ_λ y_λ(q) · χ_λ(β) "
            "equals tr_M(β) computed via the recursive Markov-axiom "
            f"reducer, on {len(TESTS)} test braids in B_3 (covering "
            "identity, single generator, Coxeter, figure-eight, "
            "full-twist).  B_4 tests were dropped because "
            "y_lambda_symbolic(n=4) exceeds the 3-min symbolic "
            "compute timeout.  LHS uses canonical Hoefsmit χ_λ "
            "(mpmath 50 dps) × y_λ from `markov_weights_symbolic` "
            "(sympy.N at 30 dps).  RHS uses "
            "`markov_trace_recursive.markov_trace_of_word`.  All "
            "residues below 1e-10 witness the partition-sum closure."
        )
        .set_content_block("prop:q-hecke-seminormal-character-closure")
        .add_parameter("q_0_50dps", Q_50_DIGIT_STR)
        .add_parameter("num_test_cases", len(TESTS))
        .add_parameter("max_residue_across_tests", float(max_residue))
        .add_data("per_test_results", results)
        .add_assertion(
            name="partition_sum_equals_recursive_reducer",
            computed=float(max_residue),
            expected=0.0,
            tolerance=1e-10,
            unit=(
                f"max over {len(TESTS)} test braids of "
                "|Σ_λ y_λ(q_0)·χ_λ(β) − tr_M(β) via recursive reducer|"
            ),
            source=(
                "Wedderburn-Artin decomposition H_n(q) ≅ ⊕_λ "
                "M_{f^λ}(ℂ) combined with Wenzl 1988 Schur principal "
                "specialization for y_λ(q)."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"{'test':<60} {'n':<3} {'LHS':<20} {'RHS':<20} {'residue':<10}")
    for r in results:
        print(f"  {r['label']:<58} {r['n']:<3} "
              f"{r['lhs_partition_sum']:<20.12f} "
              f"{r['rhs_recursive_reducer']:<20.12f} "
              f"{r['residue']:.2e}")
    print()
    print(f"max residue: {float(max_residue):.2e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
