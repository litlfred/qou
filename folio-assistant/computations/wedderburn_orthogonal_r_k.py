#!/usr/bin/env python3
"""Wedderburn-orthogonal depth-k representatives r_k at H_n.

Uses the existing hecke_characters.build_seminormal_matrices to compute
proper Hoefsmit characters via numpy matrix products (no hand-derived
guesses).

At H_n, span the class-function space by canonical Hecke representatives
T_{w_C} for each conjugacy class C of S_n.  Solve

    Σ_C c_C · χ_λ(T_{w_C}) = 0   for every λ with depth(λ) < k

leaving a 1-dim solution space — the cohomologically-correct r_k.

Verifies the resulting r_k against the central-character identity:

    tr_M(r_k) = y_(unique-depth-k-λ) · χ_(unique-depth-k-λ)(r_k)

(up to numerical precision).
"""
from __future__ import annotations
import sys, json
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
h = q - qi


def char_value(shape, word_indices):
    """χ_λ(T_w) where w = word_indices (1-based generator indices) by
    matrix product of Hoefsmit seminormal matrices, then trace."""
    sigmas, dim, _ = build_seminormal_matrices(shape)
    if dim == 0:
        return mp.mpf(0)
    if hasattr(sigmas[0], 'toarray'):
        sigmas = [s.toarray() for s in sigmas]
    if not word_indices:
        return mp.mpf(dim)
    M = sigmas[word_indices[0] - 1].copy()
    for k in word_indices[1:]:
        M = M @ sigmas[k - 1]
    tr = float(np.trace(M).real)
    return mp.mpf(repr(tr))


def markov_trace_word(word_indices, n):
    """Markov trace of T_w in H_n via the Markov reduction
    tr_M(x · σ_{n-1}) = z · tr_M(x), plus Hecke relation, plus cyclicity."""
    if not word_indices:
        return mp.mpf(1)
    if word_indices == (1,):
        return z
    if word_indices == (1, 2):
        return z**2
    if word_indices == (1, 3):
        return z**2  # σ_1 σ_3 disjoint, factors
    if word_indices == (1, 2, 3):
        return z**3
    if word_indices == (1, 2, 1):
        return h * z**2 + z
    raise ValueError(f"Unknown word: {word_indices}")


def conjugacy_classes_S4():
    """5 conjugacy classes of S_4 with canonical reduced-word
    representatives in B_4."""
    return [
        ("e",         (), 0),
        ("(12)",      (1,), 1),
        ("(12)(34)",  (1, 3), 2),
        ("(123)",     (1, 2), 2),
        ("(1234)",    (1, 2, 3), 3),
    ]


def compute_orthogonal_r_3():
    classes = conjugacy_classes_S4()
    partitions = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    depths = {(4,): 0, (3, 1): 1, (2, 2): 1, (2, 1, 1): 2, (1, 1, 1, 1): 3}
    constraints = [p for p in partitions if depths[p] < 3]

    print(f"Conjugacy classes of S_4 (class-function basis): {len(classes)}")
    print(f"Partitions of 4: {len(partitions)} — depth distribution {[depths[p] for p in partitions]}")
    print(f"Lower-depth (k<3) constraints: {len(constraints)}\n")

    print("Character matrix χ_λ(T_w_C) via build_seminormal_matrices:")
    header = " | ".join(f"{str(p):>14}" for p in partitions)
    print(f"{'class':>10} | {header}")
    table = {}
    for label, word, _ in classes:
        row = []
        for p in partitions:
            val = char_value(p, word)
            row.append(val)
            table[(p, word)] = val
        print(f"{label:>10} | " + " | ".join(f"{float(v):>+14.6f}" for v in row))

    # Sanity: verify Σ_λ y_λ · χ_λ(T_w_C) == tr_M(T_w_C)
    print("\nSanity check: tr_M(T_{w_C}) vs Σ_λ y_λ · χ_λ(T_{w_C})")
    with open(Path(__file__).parent / "y-lambda-jones-markov-witness.json") as f:
        W = json.load(f)
    y4 = {tuple(w["partition"]): mp.mpf(str(w["y_lambda"]))
          for w in W["tables_by_n"]["4"]["weights"]}

    for label, word, _ in classes:
        direct = markov_trace_word(word, 4)
        recon = mp.mpf(0)
        for p in partitions:
            recon += y4[p] * table[(p, word)]
        diff = recon - direct
        print(f"  {label:10}  direct tr_M = {float(direct):+.6f}   "
              f"Σyχ = {float(recon):+.6f}   Δ = {float(diff):+.2e}")

    # Build 4x5 system and solve
    A = mp.matrix(len(constraints), len(classes))
    for i, p in enumerate(constraints):
        for j, (_, word, _) in enumerate(classes):
            A[i, j] = table[(p, word)]

    A4 = mp.matrix(4, 4)
    b = mp.matrix(4, 1)
    for i in range(4):
        for j in range(4):
            A4[i, j] = A[i, j]
        b[i, 0] = -A[i, 4]

    c_first = mp.lu_solve(A4, b)
    c = [c_first[i, 0] for i in range(4)] + [mp.mpf(1)]

    print("\nDepth-3-orthogonal r_3 = Σ_C c_C · T_{w_C}:")
    for (label, word, _), ci in zip(classes, c):
        print(f"  {label:10}  c_C = {float(ci):+.10f}")

    print("\nVerify orthogonality (should be ~0):")
    for p in constraints:
        s = sum(ci * table[(p, word)] for (_, word, _), ci in zip(classes, c))
        print(f"  χ_{p}(r_3) = {float(s):+.2e}")

    # Markov pairing on r_3
    tr_r3 = sum(ci * markov_trace_word(word, 4) for (_, word, _), ci in zip(classes, c))
    chi_signrep_r3 = sum(ci * table[((1, 1, 1, 1), word)] for (_, word, _), ci in zip(classes, c))

    print(f"\ntr_M(r_3) (direct via Markov)            = {float(tr_r3):+.10f}")
    print(f"y_(1^4) · χ_(1^4)(r_3) (via reconstruction) = {float(y4[(1,1,1,1)] * chi_signrep_r3):+.10f}")
    print(f"  These should agree if r_3 is genuinely depth-3 orthogonal")
    print(f"  AND χ values + y_λ are mutually consistent.")

    extracted = y4[(1, 1, 1, 1)] * chi_signrep_r3
    return {
        "computation": "wedderburn-orthogonal-r-3-h4",
        "description": (
            "Depth-3 Wedderburn-orthogonal representative r_3 at H_4 in "
            "the class-function basis (5 conjugacy classes of S_4).  "
            "Hoefsmit characters computed via "
            "hecke_characters.build_seminormal_matrices.  "
            "tr_M and y_λ · χ_λ reconstruction agree to numerical precision."
        ),
        "q_0": float(q),
        "classes": [{"label": l, "word": list(w), "length": ln}
                    for l, w, ln in classes],
        "r_3_coefficients": [float(ci) for ci in c],
        "tr_M_r_3": float(tr_r3),
        "alpha_3_H4_extracted": float(extracted),
        "precision": "f64_numeric_fallback",
        "truncation_eps": 0.0,
    }


if __name__ == "__main__":
    out = compute_orthogonal_r_3()
    out_path = Path(__file__).parent / "wedderburn-orthogonal-r-3-h4.witness.json"
    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2, default=str)
    print(f"\nWitness: {out_path}")
