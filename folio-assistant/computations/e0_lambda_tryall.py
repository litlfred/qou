#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""e0_lambda_tryall.py — falsification harness for 5 substrate-derived E_0^λ maps.

CONTEXT (read docs/audits/2026-06-01-e0-lambda-tryall-results.md):

The entire L2-Subgoal-1 gap reduces to ONE missing object: a PARAMETER-FREE
map  χ^λ(K) → M_λ(K)  giving substrate-derived per-block energies E_0^λ (MeV).
The binding operator K is substrate-fixable (PR #1598), its substrate content
is its character χ^λ(K) (dimensionless); the mass formula needs the per-block
MASS-functor component M_λ(K) (MeV). χ^λ does NOT determine M_λ.

The ONLY existing χ^λ→M_λ map is the DEPRECATED LSQ fit
`_deprecated/per_block_phi_q.py::fit_three_E0` — a 3-parameter least-squares
fit of (E_0^sym, E_0^std, E_0^alt) to {e⁻, p, n}. Those fitted values are the
FALSIFICATION ANCHORS: a substrate-derived candidate must reproduce them with
ZERO free parameters.

This harness tests 5 candidate constructions of E_0^λ, ALL from cached
substrate data (q₀, χ^λ, y_λ, dim_q, contents, ribbon twist, seminormal
eigenphases) — NEVER from B_AME or the fit:

  1. Archimedean per-block       (m_e·Geom_full restricted to block λ)
  2. q-dimension                 (E_0^λ ∝ dim_q(λ); variants hook-content, dim_q²)
  3. Option-E ρ_w at energy level (per-vertex energy functional, not plain trace)
  4. Casimir                     (quadratic Casimir = content-sum Σ c(box))
  5. Ribbon twist θ_λ            (ribbon eigenvalue q^{2·content-sum})

For each candidate we emit raw computed E_0^λ vs anchor, residual, and verdict:
  PASS       — reproduces all 3 anchors, zero free parameters
  LATENT-FIT — needs ≥1 tuned parameter
  FAIL       — wrong even with a global scale

HARD DISCIPLINE: anchors are the falsification test, not fit targets. No tuning
to {e⁻,p,n} or B_AME. Report raw matches/misses honestly. If all 5 fail,
report that — do not escalate to a 6th fit (the Δ_λ gate already killed six).

@module folio-assistant/computations/e0_lambda_tryall
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def main() -> int:
    # Scaffold — candidates implemented per-commit below.
    print("[e0_tryall] scaffold; candidates land per-commit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
