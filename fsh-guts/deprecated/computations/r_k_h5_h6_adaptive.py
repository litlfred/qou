#!/usr/bin/env python3
"""Numeric r_λ extraction at H_n with adaptive gauge selection.

Replaces r_k_h5_h6_numeric.py: tries each of the p(n) possible gauges
(set c[k] = 1 for each k = 0, ..., p(n)-1) and picks the one with the
smallest |c|_∞.  This handles the (2,2)-self-conjugate-style degeneracies
where the c[last]=1 gauge happens to pick a near-zero direction → divergent.

For each partition λ ⊢ n, the resulting r_λ satisfies χ_μ(r_λ) = 0 for
all μ ≠ λ, with α_λ(H_n) = tr_M(r_λ) finite.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import numpy as np
import mpmath as mp

mp.mp.dps = 30
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT
from hecke_characters import build_seminormal_matrices

q = mp.mpf(repr(Q0_FLOAT))
qi = 1 / q
z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def char_value(shape, word):
    sigmas, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return mp.mpf(0)
    if hasattr(sigmas[0], 'toarray'):
        sigmas = [s.toarray() for s in sigmas]
    if not word:
        return mp.mpf(dim)
    M = sigmas[word[0] - 1].copy()
    for k in word[1:]:
        M = M @ sigmas[k - 1]
    # Accumulate trace as mpf to preserve precision (avoid double float cast).
    trace_real = mp.mpf(0)
    for i in range(M.shape[0]):
        trace_real += mp.mpf(repr(M[i, i].real))
    return trace_real


def markov_trace_word(word):
    if not word:
        return mp.mpf(1)
    if word[-1] == max(word):
        return z * markov_trace_word(word[:-1])
    max_idx = word.index(max(word))
    rotated = word[max_idx + 1:] + word[:max_idx + 1]
    if rotated[-1] == max(word):
        return z * markov_trace_word(rotated[:-1])
    raise ValueError(f"Cannot reduce: {word}")


def conjugacy_classes(n):
    if n == 4:
        return [
            ("e",         ()),     ("(12)",      (1,)),
            ("(12)(34)",  (1, 3)), ("(123)",     (1, 2)),
            ("(1234)",    (1, 2, 3)),
        ]
    if n == 5:
        return [
            ("e",            ()),       ("(12)",         (1,)),
            ("(12)(34)",     (1, 3)),   ("(123)",        (1, 2)),
            ("(123)(45)",    (1, 2, 4)),("(1234)",       (1, 2, 3)),
            ("(12345)",      (1, 2, 3, 4)),
        ]
    if n == 6:
        return [
            ("e",              ()),       ("(12)",           (1,)),
            ("(12)(34)",       (1, 3)),   ("(12)(34)(56)",   (1, 3, 5)),
            ("(123)",          (1, 2)),   ("(123)(45)",      (1, 2, 4)),
            ("(123)(456)",     (1, 2, 4, 5)),
            ("(1234)",         (1, 2, 3)),("(1234)(56)",     (1, 2, 3, 5)),
            ("(12345)",        (1, 2, 3, 4)),
            ("(123456)",       (1, 2, 3, 4, 5)),
        ]
    raise ValueError(f"n={n}")


def partitions_of(n):
    if n == 0: return [()]
    def gen(rem, mxp):
        if rem == 0: yield (); return
        for p in range(min(mxp, rem), 0, -1):
            for rest in gen(rem - p, p):
                yield (p,) + rest
    return list(gen(n, n))


def solve_with_best_gauge(constraint_rows, p_n):
    """Try every gauge (c[k]=1 for k=0..p_n-1), return c with smallest |c|_∞.

    Each constraint_row is a row of the (p_n - 1) x p_n matrix.
    Returns (c_list, max_abs_c) or (None, ∞) if all gauges singular.
    """
    A = mp.matrix(p_n - 1, p_n)
    for i, row in enumerate(constraint_rows):
        for j, v in enumerate(row):
            A[i, j] = v

    best_c = None
    best_max = mp.inf
    for free_k in range(p_n):
        idx_other = [j for j in range(p_n) if j != free_k]
        A_sub = mp.matrix(p_n - 1, p_n - 1)
        b = mp.matrix(p_n - 1, 1)
        for i in range(p_n - 1):
            for j_pos, j in enumerate(idx_other):
                A_sub[i, j_pos] = A[i, j]
            b[i, 0] = -A[i, free_k]
        try:
            c_solved = mp.lu_solve(A_sub, b)
            c = [mp.mpf(0)] * p_n
            for j_pos, j in enumerate(idx_other):
                c[j] = c_solved[j_pos, 0]
            c[free_k] = mp.mpf(1)
            max_c = max(abs(ci) for ci in c)
            if max_c < best_max:
                best_max = max_c
                best_c = c
        except Exception:
            continue
    return best_c, best_max


def extract(n):
    classes = conjugacy_classes(n)
    parts = partitions_of(n)
    p_n = len(parts)
    print(f"\n{'='*72}")
    print(f"H_{n}: {p_n} partitions × {len(classes)} classes (adaptive gauge)")
    print(f"{'='*72}\n")

    print("Tabulating Hoefsmit characters...", flush=True)
    table = {}
    for p in parts:
        for label, word in classes:
            table[(p, word)] = char_value(p, word)

    # Sanity check
    with open(Path(__file__).parent / "y-lambda-jones-markov-witness.json") as f:
        W = json.load(f)
    y_n = {tuple(w["partition"]): mp.mpf(str(w["y_lambda"]))
           for w in W["tables_by_n"][str(n)]["weights"]}
    max_diff = max(abs(markov_trace_word(w) - sum(y_n[p] * table[(p, w)] for p in parts))
                   for _, w in classes)
    print(f"Sanity max |Δ|: {float(max_diff):.2e}\n")

    print(f"{'partition':>16} {'depth':>5} {'gauge|c|_∞':>12} {'α_λ(H_n)':>16}")
    results = {}
    for target in parts:
        constraints = [p for p in parts if p != target]
        rows = [[table[(p, w)] for _, w in classes] for p in constraints]
        c, max_c = solve_with_best_gauge(rows, p_n)
        if c is None:
            print(f"{str(target):>16} {len(target)-1:>5}  ALL GAUGES SINGULAR")
            continue
        # NORMALIZE so that |c|_∞ = 1 (canonical scale).  This makes α_λ
        # gauge-invariant up to overall sign.
        c = [ci / max_c for ci in c]
        tr = sum(ci * markov_trace_word(w)
                 for ci, (_, w) in zip(c, classes))
        results[str(target)] = {
            "depth": len(target) - 1,
            "coefficients": [float(ci) for ci in c],
            "alpha": float(tr),
            "raw_gauge_max": float(max_c),
        }
        print(f"{str(target):>16} {len(target)-1:>5}  {float(max_c):>12.4f}"
              f" {float(tr):>+16.10f}")

    return results


def main():
    out = {
        "computation": "r-k-h5-h6-adaptive",
        "description": (
            "Numeric α_λ(H_n) for n=5, 6 with adaptive gauge selection: "
            "for each partition, try every possible gauge c[k]=1 and pick "
            "the one minimising |c|_∞.  Then renormalize so |c|_∞ = 1 "
            "(canonical scale).  This resolves the gauge degeneracies "
            "that affected non-hook shapes in r_k_h5_h6_numeric.py."
        ),
        "q_0": float(q),
        "by_n": {},
        "precision": "f64_numeric_fallback",
        "truncation_eps": 0.0,
    }
    for n in [5, 6]:
        res = extract(n)
        if res:
            out["by_n"][str(n)] = res

    with open(Path(__file__).parent / "r-k-h5-h6-adaptive.witness.json", "w") as fp:
        json.dump(out, fp, indent=2, default=str)
    print(f"\nWitness saved.")


if __name__ == "__main__":
    main()
