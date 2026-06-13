#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical SDP-assembly infrastructure.
"""Shared per-nucleus real-SDP **assembly** layer.

The LP/SDP *solve* is already centralised in
[`lp_dual_solver.py`](lp_dual_solver.py) (CLAUDE.md §LP/SDP duals — first-class
infra). This module centralises the *assembly* that sits on top of it and was
duplicated across ~67 per-nucleus compute scripts (the `t_λ = y_λ·χ^λ` cost,
the Frobenius Gram diagonal, forbidden-block detection, the canonical
Markov-trace from the cache, and the canonical-vs-fitted production default).

Per-nucleus real SDP at `H_n` (`n = 3·A`):

    cost      t_λ = y_λ · χ^λ                  (per-partition mass-formula summand)
    Gram diag G_λλ = y_λ · dim S^λ = tr_M(P_λ) (Frobenius; indefinite at q_0)
    forbidden blocks: G_λλ < 0 (negative-norm channels — x_λ must be 0)

Design notes:

- **No Rust.** Pure NumPy + the canonical `lp_dual_solver`. The canonical
  Markov trace `Σ_ν y_ν χ^ν` is read from the `y-lambda-at-q0` witness cache
  (full-Hecke `y_ν`), never via `compute_tau_M_nucleon_H3` (which needs the
  `pyhecke_native` Rust wheel). This is the centralised form of the PR #2219
  correctness fix — no consumer should re-derive `tr_M` with the unweighted
  proxy `Σ_ν χ^ν`.
- **Canonical is the production default.** `CANONICAL_PRODUCTION_DEFAULT`
  names the no-fit encoding; `designate_production_default()` stamps the
  `production_default` flag so every nucleus inherits the canonical default
  by construction (owner directive 2026-06-13, recorded in #2219).
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import numpy as np

from murnaghan_nakayama import dim_specht  # shared hook-length dimension


def _solver():
    """Return the canonical LP/SDP operator-selection solvers, preferring the
    published `pyhecke` package and falling back to the in-repo module. Imported
    lazily so `build_cost_gram` / `tr_M_from_cache` work without the solver."""
    try:
        from pyhecke.lp_dual_solver import (
            solve_operator_selection_lp,
            solve_psd_operator_selection_sdp,
        )
    except ImportError:
        from lp_dual_solver import (
            solve_operator_selection_lp,
            solve_psd_operator_selection_sdp,
        )
    return solve_operator_selection_lp, solve_psd_operator_selection_sdp

# The canonical (substrate-derived, no-fit) per-nucleus encoding. Owner
# directive 2026-06-13: this is the production default; fitted / AME-equality
# encodings are validation-only. See deuteron_real_sdp.py and
# docs/audits/2026-06-13-wenzl-trace-normalization-prop-compute-mismatch.md.
CANONICAL_PRODUCTION_DEFAULT = "5_lr_branching_canonical"

# Default location of the full-Hecke y_λ(q_0) cache.
Y_LAMBDA_CACHE = Path(__file__).resolve().parent / "y-lambda-at-q0.witness.json"


def parse_partition(key: str) -> tuple[int, ...]:
    """'(3, 2, 1)' -> (3, 2, 1); '(3,)' -> (3,)."""
    return tuple(int(p) for p in key.strip("()").rstrip(",").split(",") if p.strip())


def pkey(part) -> str:
    """(3,) -> '(3,)' ; (2, 1) -> '(2, 1)' — the canonical partition-key string."""
    part = tuple(part)
    inner = ", ".join(str(x) for x in part)
    return "(" + inner + ("," if len(part) == 1 else "") + ")"


@dataclass
class CostGram:
    """Real per-nucleus SDP cost + Frobenius Gram, assembled from y_λ and χ^λ."""

    keys: list[str]
    parts: list[tuple[int, ...]]
    dims: list[int]
    y: np.ndarray            # Wenzl weights y_λ(q_0), aligned to keys
    chi: np.ndarray          # characters χ^λ(β), aligned to keys
    t: np.ndarray            # cost t_λ = y_λ · χ^λ
    frob_diag: np.ndarray    # Frobenius Gram diagonal G_λλ = y_λ · dim S^λ
    tr_M: float              # Σ_λ t_λ = tr_M(β)
    forbidden_blocks: list[str]   # blocks with G_λλ < 0 (negative-norm)

    @property
    def gram(self) -> np.ndarray:
        """The (diagonal) Frobenius Gram matrix diag(tr_M(P_λ))."""
        return np.diag(self.frob_diag)

    @property
    def indefinite(self) -> bool:
        return bool((self.frob_diag < 0).any())


def cost_gram_from_arrays(
    keys,
    parts,
    dims,
    y,
    chi,
    *,
    n: Optional[int] = None,
    tr_M_check: Optional[float] = None,
) -> CostGram:
    """Array-based core of the cost/Gram assembly.

    Builds a `CostGram` from already-resolved `keys`/`parts`/`dims` and the
    `y_λ`, `χ^λ` arrays — the form produced by schema-agnostic loaders such as
    `nucleus_real_sdp.load_cost`. `build_cost_gram` is the dict-based front
    that delegates here.
    """
    y = np.asarray(y, dtype=float)
    chi_v = np.asarray(chi, dtype=float)
    dims_list = [int(d) for d in dims]
    if n is not None:
        assert sum(d * d for d in dims_list) == math.factorial(n), (
            f"irrep dims do not close to {n}!"
        )
    t = y * chi_v
    frob_diag = y * np.array(dims_list, dtype=float)
    tr_M = float(t.sum())
    if tr_M_check is not None:
        rel = abs(tr_M - tr_M_check) / abs(tr_M_check)
        assert rel < 1e-9, f"tr_M mismatch vs witness: {rel:.2e}"
    keys_list = list(keys)
    forbidden = [keys_list[i] for i, g in enumerate(frob_diag) if g < 0.0]
    return CostGram(
        keys_list, list(parts), dims_list, y, chi_v, t, frob_diag, tr_M, forbidden
    )


def build_cost_gram(
    y_lambda: dict[str, float],
    chi: dict[str, float],
    *,
    n: Optional[int] = None,
    tr_M_check: Optional[float] = None,
) -> CostGram:
    """Assemble the real per-nucleus SDP cost + Frobenius Gram from `y_λ` and
    `χ^λ` dicts (keyed by partition string).

    Dict-based front for `cost_gram_from_arrays`; centralises the pattern
    duplicated across ~67 scripts: `t_λ = y_λ·χ^λ`, `G_λλ = y_λ·dim S^λ`,
    `tr_M = Σ_λ t_λ`. `n` enables the Burnside check `Σ_λ (dim S^λ)² = n!`;
    `tr_M_check` cross-checks the assembled trace (rel-err < 1e-9).
    """
    keys = list(y_lambda.keys())
    parts = [parse_partition(k) for k in keys]
    dims = [dim_specht(p) for p in parts]
    y = np.array([y_lambda[k] for k in keys], dtype=float)
    chi_v = np.array([chi[k] for k in keys], dtype=float)
    return cost_gram_from_arrays(keys, parts, dims, y, chi_v, n=n, tr_M_check=tr_M_check)


def solve_real_sdp(cg: CostGram, n_target: float) -> dict:
    """LP + SDP operator-selection solve through the canonical dual-emitting
    entry point. Returns `{'lp': ..., 'sdp': ...}` with primal + dual + gap
    (CLAUDE.md §LP/SDP duals)."""
    solve_lp, solve_sdp = _solver()
    G = cg.gram
    lp = solve_lp(cg.t, G, n_target)
    sdp = solve_sdp(cg.t, G, n_target)
    return {"lp": lp.to_dict(), "sdp": sdp.to_dict()}


def tr_M_from_cache(
    chi: dict[str, float],
    *,
    n: int,
    cache_path: Path = Y_LAMBDA_CACHE,
) -> float:
    """Canonical Markov trace `Σ_ν y_ν χ^ν` at `H_n`.

    `y_ν` are the full-Hecke Wenzl weights read from the `y-lambda-at-q0`
    cache (NO Rust); `chi` is the character map keyed by partition string.
    This is the centralised form of the PR #2219 fix — never use the
    unweighted proxy `Σ_ν χ^ν`, which deviates from the Markov trace at q≠1.
    """
    cache = json.loads(Path(cache_path).read_text())
    y_nu: dict[str, float] = {}

    def _collect(o):
        if isinstance(o, dict):
            if o.get("partition") and "y_at_q0_50dps" in o and sum(o["partition"]) == n:
                y_nu[pkey(o["partition"])] = float(o["y_at_q0_50dps"])
            for v in o.values():
                _collect(v)
        elif isinstance(o, list):
            for v in o:
                _collect(v)

    _collect(cache)
    missing = [k for k in chi if k not in y_nu]
    if missing:
        raise KeyError(
            f"tr_M_from_cache: no H_{n} y_ν in cache for {missing} "
            f"(have {sorted(y_nu)})"
        )
    return sum(y_nu[k] * chi[k] for k in chi)


def designate_production_default(
    methods: dict[str, dict],
    canonical_key: str = CANONICAL_PRODUCTION_DEFAULT,
) -> str:
    """Stamp `production_default` across an encoding dict: True on the
    canonical key, False on every other. Returns `canonical_key`.

    Centralises the owner directive 'canonical is default for production'
    so every per-nucleus script inherits it instead of re-deciding."""
    if canonical_key not in methods:
        raise KeyError(
            f"canonical encoding {canonical_key!r} not in methods "
            f"({sorted(methods)})"
        )
    for key, m in methods.items():
        if isinstance(m, dict):
            m["production_default"] = key == canonical_key
    return canonical_key


if __name__ == "__main__":
    # Self-test against the deuteron cost witness (the reference consumer).
    here = Path(__file__).resolve().parent
    data = json.loads((here / "deuteron-real-sdp-cost.witness.json").read_text()
                      )["data"] if (here / "deuteron-real-sdp-cost.witness.json").exists() else None
    print("nucleus_sdp_assembly: import OK;",
          "CANONICAL_PRODUCTION_DEFAULT =", CANONICAL_PRODUCTION_DEFAULT)
