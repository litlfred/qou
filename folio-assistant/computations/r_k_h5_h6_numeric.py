#!/usr/bin/env python3
"""Numerical r_λ extraction at H_5 and H_6.

Builds the (p(n)-1) × p(n) Hoefsmit character matrix using the existing
hecke_characters.build_seminormal_matrices, then solves for the
Wedderburn-orthogonal r_λ at each partition λ ⊢ n.

Outputs α_λ(H_n) = tr_M(r_λ) evaluated at q_0.

Companion to prop:explicit-alpha-k-h4 — extends the same procedure to
H_5 (7 conjugacy classes) and H_6 (11 classes).
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import numpy as np
import mpmath as mp

mp.mp.dps = 30
# NOTE (alpha-fsc-audit, 2026-04-28): observed numerical instability at
# certain partitions of H_5 ((3,2), (2,2,1)) and H_6 ((4,2), (3,3),
# (3,2,1), (2,2,2)) — α_λ values explode to ~10¹⁵ where they should be
# small. Bumping mp.mp.dps from 30 → 50 does NOT fix the instability;
# the y_λ consistency check (Δ < 6e-17) confirms y_λ themselves are
# accurate. Root cause: the script's Wedderburn-orthogonal r_λ
# computation uses numpy linalg (float64) internally, regardless of
# mpmath dps. The fix requires migrating the r_λ matrix solve to
# mpmath linear algebra (mp.lu_solve / mp.matrix). Filed as a follow-up
# in docs/alpha-fsc-audit.md §"Open work".
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT
from hecke_characters import build_seminormal_matrices

q = mp.mpf(repr(Q0_FLOAT))
qi = 1 / q
z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def char_value(shape, word_indices):
    """χ_λ(T_w) via numpy matrix product of seminormal matrices."""
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
    return mp.mpf(repr(float(np.trace(M).real)))


def markov_trace_word(word):
    """Markov-trace of T_w via reduction (universal for class reps)."""
    # Length-based: tr_M(T_{linear word σ_1...σ_k}) = z^k
    # σ_1σ_3 disjoint: z²; σ_1σ_3σ_? mixed...
    L = len(word)
    if not word:
        return mp.mpf(1)
    # Disjoint cycles factor: σ_1σ_3, σ_1σ_3σ_2σ_4, etc.
    # We use the Markov axiom: tr_M(x · σ_n) = z · tr_M(x) for x in H_n
    # So for any word ending in σ_k where k = max generator, peel off:
    if word[-1] == max(word):
        return z * markov_trace_word(word[:-1])
    # Otherwise braid-equivalent to one ending in max — use cyclicity
    max_idx = word.index(max(word))
    # Cyclic shift: place max at end
    rotated = word[max_idx + 1:] + word[:max_idx + 1]
    if rotated[-1] == max(word):
        return z * markov_trace_word(rotated[:-1])
    # Fallback: should not happen for class reps we use
    raise ValueError(f"Cannot reduce: {word}")


def conjugacy_classes(n):
    """Canonical conjugacy classes of S_n with reduced-word reps."""
    if n == 4:
        return [
            ("e",         ()),
            ("(12)",      (1,)),
            ("(12)(34)",  (1, 3)),
            ("(123)",     (1, 2)),
            ("(1234)",    (1, 2, 3)),
        ]
    if n == 5:
        return [
            ("e",            ()),
            ("(12)",         (1,)),
            ("(12)(34)",     (1, 3)),
            ("(123)",        (1, 2)),
            ("(123)(45)",    (1, 2, 4)),
            ("(1234)",       (1, 2, 3)),
            ("(12345)",      (1, 2, 3, 4)),
        ]
    if n == 6:
        return [
            ("e",              ()),
            ("(12)",           (1,)),
            ("(12)(34)",       (1, 3)),
            ("(12)(34)(56)",   (1, 3, 5)),
            ("(123)",          (1, 2)),
            ("(123)(45)",      (1, 2, 4)),
            ("(123)(456)",     (1, 2, 4, 5)),
            ("(1234)",         (1, 2, 3)),
            ("(1234)(56)",     (1, 2, 3, 5)),
            ("(12345)",        (1, 2, 3, 4)),
            ("(123456)",       (1, 2, 3, 4, 5)),
        ]
    raise ValueError(f"n={n} not yet enumerated")


def partitions_of(n):
    """All partitions of n in standard (largest-first) order."""
    if n == 0: return [()]
    def gen(rem, mxp):
        if rem == 0: yield (); return
        for p in range(min(mxp, rem), 0, -1):
            for rest in gen(rem - p, p):
                yield (p,) + rest
    return list(gen(n, n))


def depth(p):
    return len(p) - 1


def extract_r_k_at_h_n(n):
    """Compute α_λ(H_n) for every λ ⊢ n via Wedderburn-orthogonal r_λ."""
    classes = conjugacy_classes(n)
    parts = partitions_of(n)
    p_n = len(parts)
    print(f"\n{'='*72}")
    print(f"H_{n}: {p_n} partitions, {len(classes)} conjugacy classes")
    print(f"{'='*72}\n")

    # Tabulate characters
    print("Tabulating Hoefsmit characters...", flush=True)
    table = {}
    for label, word in classes:
        for p in parts:
            table[(p, word)] = char_value(p, word)

    # Verify sanity: tr_M(T_w_C) = Σ_λ y_λ · χ_λ(T_w_C)
    with open(Path(__file__).parent / "y-lambda-jones-markov-witness.json") as f:
        W = json.load(f)
    y_n = {tuple(w["partition"]): mp.mpf(str(w["y_lambda"]))
           for w in W["tables_by_n"][str(n)]["weights"]}

    print(f"\nSanity check: tr_M(T_w) = Σ_λ y_λ · χ_λ(T_w):")
    max_diff = mp.mpf(0)
    for label, word in classes:
        direct = markov_trace_word(word)
        recon = sum(y_n[p] * table[(p, word)] for p in parts)
        diff = abs(direct - recon)
        max_diff = max(max_diff, diff)
        print(f"  {label:20}  Δ = {float(diff):+.2e}")
    print(f"  Max |Δ| = {float(max_diff):.2e}")
    if max_diff > mp.mpf("1e-10"):
        print(f"  WARNING: sanity check failed (>1e-10), aborting.")
        return None

    # For each partition, solve for r_λ
    print(f"\nPer-partition α_λ(H_{n}):")
    print(f"{'partition':>16} {'depth':>5} {'α_λ(H_n) at q_0':>20}")
    results = {}
    for target in parts:
        constraints = [p for p in parts if p != target]
        # Build (p_n - 1) x p_n system
        A = mp.matrix(p_n - 1, p_n)
        for i, p in enumerate(constraints):
            for j, (_, word) in enumerate(classes):
                A[i, j] = table[(p, word)]

        # Solve A · c = 0 with c[last] = 1 gauge
        A_sub = mp.matrix(p_n - 1, p_n - 1)
        b = mp.matrix(p_n - 1, 1)
        for i in range(p_n - 1):
            for j in range(p_n - 1):
                A_sub[i, j] = A[i, j]
            b[i, 0] = -A[i, p_n - 1]
        try:
            c_first = mp.lu_solve(A_sub, b)
            c = [c_first[i, 0] for i in range(p_n - 1)] + [mp.mpf(1)]
        except Exception:
            # Try alternative gauge (set c[0] = 1 instead)
            try:
                A_sub2 = mp.matrix(p_n - 1, p_n - 1)
                b2 = mp.matrix(p_n - 1, 1)
                for i in range(p_n - 1):
                    for j in range(1, p_n):
                        A_sub2[i, j - 1] = A[i, j]
                    b2[i, 0] = -A[i, 0]
                c_alt = mp.lu_solve(A_sub2, b2)
                c = [mp.mpf(1)] + [c_alt[i, 0] for i in range(p_n - 1)]
            except Exception as e:
                print(f"  {str(target):>16} {depth(target):>5}  FAILED ({e})")
                continue

        tr = sum(ci * markov_trace_word(word)
                 for ci, (_, word) in zip(c, classes))
        results[str(target)] = {
            "depth": depth(target),
            "coefficients": [float(ci) for ci in c],
            "alpha": float(tr),
        }
        print(f"{str(target):>16} {depth(target):>5}  {float(tr):+20.10f}")

    return results


def main():
    out = {
        "computation": "r-k-h5-h6-numeric",
        "description": (
            "Numerical α_λ(H_n) extraction for n=5, 6 via the same "
            "Wedderburn-orthogonal class-function procedure as H_4. "
            "Hoefsmit characters via build_seminormal_matrices; "
            "consistency verified by tr_M = Σ y_λ χ_λ identity."
        ),
        "q_0": float(q),
        "by_n": {},
        "precision": "f64_numeric_fallback",
        "truncation_eps": 0.0,
    }
    for n in [5, 6]:
        res = extract_r_k_at_h_n(n)
        if res:
            out["by_n"][str(n)] = res

    out_path = Path(__file__).parent / "r-k-h5-h6-numeric.witness.json"
    with open(out_path, "w") as fp:
        json.dump(out, fp, indent=2, default=str)
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
