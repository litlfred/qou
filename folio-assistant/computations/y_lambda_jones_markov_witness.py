#!/usr/bin/env python3
"""
Jones–Markov weight enumeration for H_n(R, q) at q_0 — parameterised by n.

For each n ∈ {input list}, solves the linear system for the
Jones–Markov block-weights y_λ (one per partition λ ⊢ n) using
the constraints

    tr_M(w_μ) = z^{n - len(μ)}   for cycle-type representative w_μ,

with z = 1/(√q + 1/√q) the Markov parameter.

Output: y-lambda-jones-markov-witness.json — keyed by n.

Used by sibling branches verify-mass-computation-k0DaZ and
phase-b-heavy-rust-character-kernel for α_k coefficient derivations
at higher n (deuteron H_6, tritium / He-3 H_9, alpha He-4 H_12).

References:
- prop:alpha-k-derivation-procedure
- prop:spectral-sequence-h3-explicit (H_3 closed form)
- prop:plancherel-weight-boundedness
- prop:mass-tower-coefficient-stratification
"""
from __future__ import annotations

import json
import sys
import warnings
from datetime import datetime, timezone
from pathlib import Path

warnings.filterwarnings("ignore")

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
import mpmath as mp
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT
from hecke_characters import (
    build_seminormal_matrices,
    partitions_of,
)


Q0 = mp.mpf(str(Q0_FLOAT))
Z_MARK = 1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0))


def cycle_type_word(mu: tuple[int, ...]) -> list[int]:
    """Return a reduced word (list of generator indices, 1..n-1) realising
    a permutation of cycle type μ acting on n = sum(μ) strands.

    Cycle (m) on strands [s+1..s+m] is realised by σ_{s+1} σ_{s+2} ⋯ σ_{s+m-1}
    (m-1 generators).  Disjoint cycles concatenate.
    """
    word: list[int] = []
    s = 0
    for m in mu:
        for j in range(m - 1):
            word.append(s + j + 1)  # generator σ_{s+j+1}
        s += m
    return word


def chi_lambda_with_cache(
    sigmas: list[np.ndarray], d_lam: int, word: list[int]
) -> float:
    """Compute χ_λ(σ_{w_1} σ_{w_2} ⋯) given precomputed seminormal matrices."""
    M = np.eye(d_lam)
    for idx in word:
        M = M @ sigmas[idx - 1]
    return float(np.trace(M))


def solve_jones_markov_weights(n: int) -> dict:
    """Solve the linear system for y_λ at H_n(R, q)."""
    parts = list(partitions_of(n))
    p_n = len(parts)

    # Precompute seminormal matrices once per partition (densified).
    seminormal_cache: dict = {}
    for lam in parts:
        sigmas, d_lam, _ = build_seminormal_matrices(lam)
        if hasattr(sigmas[0], "toarray"):
            sigmas = [s.toarray() for s in sigmas]
        seminormal_cache[lam] = (sigmas, d_lam)

    # Build the χ-matrix: rows = test elements (cycle-type reps),
    # columns = partitions (unknowns y_λ).
    A = np.zeros((p_n, p_n))
    b = np.zeros(p_n)
    for i, mu in enumerate(parts):
        word = cycle_type_word(mu)
        b[i] = float(Z_MARK ** (n - len(mu)))
        for j, lam in enumerate(parts):
            sigmas, d_lam = seminormal_cache[lam]
            A[i, j] = chi_lambda_with_cache(sigmas, d_lam, word)

    y = np.linalg.solve(A, b)

    cond = float(np.linalg.cond(A))
    residual = float(np.max(np.abs(A @ y - b)))

    return {
        "n": n,
        "num_partitions": p_n,
        "q_0": float(Q0),
        "z_markov": float(Z_MARK),
        "weights": [
            {
                "partition": list(lam),
                "depth": max(0, len(lam) - 1),
                "y_lambda": float(y[j]),
            }
            for j, lam in enumerate(parts)
        ],
        "diagnostics": {
            "condition_number": cond,
            "linear_system_residual": residual,
        },
    }


def main(ns: list[int]) -> None:
    out_path = Path(__file__).parent / "y-lambda-jones-markov-witness.json"
    if out_path.exists():
        out = json.loads(out_path.read_text())
    else:
        out = {"tables_by_n": {}}
    out["description"] = (
        "Jones–Markov block-weights y_λ at H_n(R, q) for nuclear "
        "mass-tower α_k derivations.  Solves tr_M(w_μ) = z^{n-len(μ)} "
        "for cycle-type representatives w_μ ⊢ n.  Provides the per-n "
        "Markov-pairing weights used by sibling branches for "
        "structural α_k computation (no fitting)."
    )
    out["references"] = [
        "prop:alpha-k-derivation-procedure",
        "prop:spectral-sequence-h3-explicit",
        "prop:mass-tower-coefficient-stratification",
    ]
    out["generated_at_utc"] = datetime.now(timezone.utc).isoformat()
    out.setdefault("tables_by_n", {})
    for n in ns:
        print(f"Solving y_λ at H_{n}(R, q) ({len(list(partitions_of(n)))} partitions)...")
        out["tables_by_n"][str(n)] = solve_jones_markov_weights(n)
        diag = out["tables_by_n"][str(n)]["diagnostics"]
        print(
            f"  cond(A) = {diag['condition_number']:.2e}, "
            f"residual = {diag['linear_system_residual']:.2e}"
        )

    out_path.write_text(json.dumps(out, indent=2, default=float))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    # Default ladder: every n from 2 (two-strand EM coupling) up to 12
    # (alpha-He-4).  Nuclear ladder n = 3, 6, 9, 12 corresponds to single
    # nucleon, deuteron, tritium/He-3, He-4; intermediate n ∈ {4, 5, 7, 8,
    # 10, 11} cover knot crossings (figure-eight, 5_1, 5_2, 6_*, 7_*,
    # 8_*, ...) and torus-knot crossing-number cases.
    ns = [int(a) for a in sys.argv[1:]] or list(range(2, 13))
    main(ns)
