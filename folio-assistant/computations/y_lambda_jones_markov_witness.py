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

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_characters import (
    build_seminormal_matrices,
    partitions_of,
)


Q0 = Q_MP  # was f64 roundtrip
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


def chi_lambda_with_cache(sigmas, d_lam: int, word: list[int]) -> float:
    """Compute χ_λ(σ_{w_1} σ_{w_2} ⋯) given precomputed seminormal matrices.

    Works for both dense numpy arrays and scipy sparse matrices (sparse
    is preferred for large d_λ to keep memory feasible at n ≥ 11)."""
    is_sparse = hasattr(sigmas[0], "toarray")
    if is_sparse:
        from scipy import sparse as sp_sparse
        M = sp_sparse.eye(d_lam, format="csr")
        for idx in word:
            M = M @ sigmas[idx - 1]
        return float(M.diagonal().sum())
    M = np.eye(d_lam)
    for idx in word:
        M = M @ sigmas[idx - 1]
    return float(np.trace(M))


# CRT-style probe points bracketing q_0 ≈ 1.1097, used for
# Vandermonde reconstruction of y_λ as q-rational functions.
PROBE_QS: list[float] = [1.02, 1.05, 1.08, 1.11, 1.15]


def _solve_at_q(parts: list[tuple[int, ...]], q_val: float, n: int) -> dict:
    """Solve the y_λ linear system at a specific q value, using the
    q-parameterised seminormal builder (override path)."""
    z = 1.0 / (q_val ** 0.5 + q_val ** -0.5)
    p_n = len(parts)
    seminormal_cache: dict = {}
    for lam in parts:
        sigmas, d_lam, _ = build_seminormal_matrices(lam, sparse=True, q=q_val)
        seminormal_cache[lam] = (sigmas, d_lam)
    A = np.zeros((p_n, p_n))
    b = np.zeros(p_n)
    for i, mu in enumerate(parts):
        word = cycle_type_word(mu)
        b[i] = z ** (n - len(mu))
        for j, lam in enumerate(parts):
            sigmas, d_lam = seminormal_cache[lam]
            A[i, j] = chi_lambda_with_cache(sigmas, d_lam, word)
    y = np.linalg.solve(A, b)
    return {
        "q": q_val,
        "z": z,
        "y": [float(v) for v in y],
        "cond": float(np.linalg.cond(A)),
        "residual": float(np.max(np.abs(A @ y - b))),
    }


def solve_jones_markov_weights(n: int, do_crt_probes: bool = True) -> dict:
    """Solve the linear system for y_λ at H_n(R, q) at q_0; if
    `do_crt_probes` is true, also evaluate at PROBE_QS for q-rational
    reconstruction by downstream consumers."""
    parts = list(partitions_of(n))
    p_n = len(parts)

    # Canonical q_0 evaluation
    canonical = _solve_at_q(parts, float(Q0), n)

    probes: list[dict] = []
    if do_crt_probes and n <= 10:
        # CRT probes only for n ≤ 10: rebuilding seminormal matrices at
        # each q is O(p(n) · max d_λ²); n ≥ 11 sees d_λ explode (≥ 200).
        for q_probe in PROBE_QS:
            if abs(q_probe - float(Q0)) < 1e-6:
                continue
            try:
                probes.append(_solve_at_q(parts, q_probe, n))
            except np.linalg.LinAlgError:
                pass

    return {
        "n": n,
        "num_partitions": p_n,
        "q_0": float(Q0),
        "z_markov": float(Z_MARK),
        "weights": [
            {
                "partition": list(lam),
                "depth": max(0, len(lam) - 1),
                "y_lambda": canonical["y"][j],
            }
            for j, lam in enumerate(parts)
        ],
        "crt_probes": probes,
        "diagnostics": {
            "condition_number": canonical["cond"],
            "linear_system_residual": canonical["residual"],
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
    out["computedAt"] = datetime.now(timezone.utc).isoformat()
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
