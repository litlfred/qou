#!/usr/bin/env python3
"""Generalized torus-knot Markov trace via q-Schur closed form on H_N(q).

Per author direction 2026-05-25:
  - "refactored to call pn.trace_weights_n_q_schur(2, q) for deduplication"
  - "can we generalize what we have already"

Generalizes `torus_knot_markov_trace_closed_form.py` from H_2-only
(T(2, k)) to ARBITRARY H_N (T(N, k)) via the new Rust upstream
`pn.trace_weights_n_q_schur(N, q)` (PR #1256, commit 4059af433).

## What this script does

For each (N, k) in a target catalogue:

  1. Get q-Schur Plancherel weights y_λ on H_N(q) (closed form, instant)
  2. Build the T(N, k) braid word in B_N: (σ_1 σ_2 ... σ_{N-1})^{k}
  3. Compute χ_λ(braid) per partition λ ⊢ N via pn.chi_lambda_braid
  4. Markov trace: tr_M(T(N, k)) = Σ_λ y_λ · χ_λ(braid)
  5. h-expansion via mpmath polynomial fit

## Cross-check at H_2 (T(2, k))

Reproduces the H_2-hardcoded values from sibling commit `5418678c8`:
  y_(2) = q / [2]_q,  y_(1,1) = q⁻¹ / [2]_q

## Trace convention

q-Schur convention: tr(σ_i) = h = q − q⁻¹. This is the convention used
by the framework's torus-knot work (sibling T(2,k) script + Higgs/Z/W±
identifications), NOT the Wenzl Jones-Markov convention (tr(σ_i) = z)
used by the Borromean mass formula.

## What this script generalizes

Originally H_2 only:
  σ_1^k closure → tr_M(σ_1^k) = y_(2) · q^k + y_(1,1) · (-q⁻¹)^k

Now arbitrary H_N:
  (σ_1 σ_2 ... σ_{N-1})^k closure → tr_M(T(N, k)) = Σ_λ y_λ_q_schur(N) · χ_λ(braid)

H_3 examples: T(3, 4) trefoil twist, T(3, 5) cinquefoil torus knot.
H_4+ examples: T(4, 5), T(5, 6) — higher torus knots.

## Output

- `torus-knot-markov-trace-generalized.witness.json` — per-(N, k)
  tr_M values + h-expansion coefficients.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import mpmath as mp
import pyhecke_native as pn

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Q_0 = Q_MP
Q_0_F64 = float(Q_0)


def torus_knot_braid_word(N: int, k: int) -> list[tuple[int, int]]:
    """Build the standard torus-knot/link T(N, k) braid word in B_N.

    T(N, k) closure: (σ_1 σ_2 ... σ_{N-1})^k = N·(N-1)·...·1 cycles
    composed k times.

    Returns list of (sign, gen_1based) pairs.
    """
    base = [(1, i + 1) for i in range(N - 1)]
    return base * k


def trM_torus_knot(N: int, k: int, q_f64: float = Q_0_F64) -> float:
    """tr_M(T(N, k)) via q-Schur closed-form y_λ + chi_lambda_braid.

    Closed form for y_λ on H_N(q) from PR #1256:
      y_λ(q) = q^{content_sum(λ)} / [N]_q!

    Markov trace:
      tr_M(T(N, k)) = Σ_λ y_λ · χ_λ(braid)

    Uses Rust upstream pn.trace_weights_n_q_schur + pn.chi_lambdas_braid.
    """
    shapes = pn.partitions_of(N)
    y_lambda = pn.trace_weights_n_q_schur(N, q_f64)
    word = torus_knot_braid_word(N, k)
    chi_vals = pn.chi_lambdas_braid(shapes, word, q_f64)
    return sum(y_lambda[i] * chi_vals[i] for i in range(len(shapes)))


def h_expansion_via_fit(N: int, k: int, max_order: int = 6) -> list[float]:
    """Fit polynomial in h to tr_M(T(N, k)) over multiple q samples."""
    n_samples = max_order + 2
    h_samples = [mp.mpf("0.005") * (i + 1) for i in range(n_samples)]

    tr_values = []
    for h_val in h_samples:
        # q = (h + sqrt(h² + 4)) / 2
        q_mpf = (h_val + mp.sqrt(h_val * h_val + 4)) / 2
        q_f = float(q_mpf)
        tr = trM_torus_knot(N, k, q_f)
        tr_values.append(tr)

    # Fit polynomial in h
    h_vec = [float(h) for h in h_samples]
    # Vandermonde matrix [h^0, h^1, ..., h^max_order]
    import numpy as np
    V = np.array([[h**j for j in range(max_order + 1)] for h in h_vec])
    coefs, *_ = np.linalg.lstsq(V, np.array(tr_values), rcond=None)
    return [float(c) for c in coefs]


def main() -> int:
    print("=" * 100)
    print("Generalized torus-knot Markov trace via q-Schur closed form")
    print(f"  q_0 = {Q_0_F64:.10f}    h_0 = {Q_0_F64 - 1/Q_0_F64:.10f}")
    print("=" * 100)
    print()

    # Target catalogue: H_2 (W±/Z/H), H_3 (trefoil family), H_4 (5-strand)
    targets = [
        # H_2 (= sibling 5418678c8 catalogue)
        (2, 4, "T(2,4) = W±"),
        (2, 6, "T(2,6) = Z"),
        (2, 8, "T(2,8) = Higgs"),
        (2, 3, "T(2,3) = trefoil"),
        # H_3
        (3, 2, "T(3,2) = trefoil (= T(2,3) for SnapPy)"),
        (3, 4, "T(3,4)"),
        (3, 5, "T(3,5) = cinquefoil"),
        # H_4
        (4, 3, "T(4,3)"),
        (4, 5, "T(4,5)"),
    ]

    results = []
    for N, k, label in targets:
        print(f"━━ T({N}, {k}) — {label} ━━")
        tr = trM_torus_knot(N, k, Q_0_F64)
        h_coefs = h_expansion_via_fit(N, k, max_order=6)
        print(f"  tr_M(T({N},{k})) at q_0 = {tr:.10f}")
        print(f"  h-expansion: {' + '.join(f'{c:+.4f}·h^{j}' for j, c in enumerate(h_coefs) if abs(c) > 1e-4)}")
        results.append({
            "N": N, "k": k, "label": label,
            "tr_M_at_q0": float(tr),
            "h_expansion": h_coefs,
        })
        print()

    # Cross-check: H_2 results should match sibling 5418678c8 hardcoded values
    print("=== H_2 cross-check (sibling 5418678c8 hardcode reproduction) ===")
    qi = 1 / Q_0_F64
    sq_2_q = Q_0_F64 + qi
    for k in [3, 4, 6, 8]:
        y_2 = Q_0_F64 / sq_2_q
        y_11 = qi / sq_2_q
        sign = (-1) ** k
        tr_hardcode = y_2 * Q_0_F64 ** k + y_11 * sign * qi ** k
        tr_generic = trM_torus_knot(2, k, Q_0_F64)
        diff = abs(tr_hardcode - tr_generic)
        print(f"  T(2,{k}): hardcode={tr_hardcode:.10f}, generic={tr_generic:.10f}, |diff|={diff:.2e}")

    # Witness
    w = WitnessBuilder("torus-knot-markov-trace-generalized", engine="python+pyhecke-native")
    w.set_description(
        "Generalized torus-knot Markov trace via q-Schur closed-form weights "
        "(PR #1256 trace_weights_n_q_schur). Extends sibling commit 5418678c8 "
        "from H_2 only (T(2,k) for W/Z/H) to arbitrary H_N (T(N,k) for any N≥2). "
        "Uses Rust upstream pn.trace_weights_n_q_schur(N, q) + pn.chi_lambda_braid "
        "directly — no LP, no hardcoded y_λ values. q-Schur convention with "
        "tr(σ_i) = h = q - q⁻¹."
    )
    w.add_parameter("q_0", Q_0_F64)
    w.add_parameter("trace_convention", "q-Schur (tr(σ_i) = h = q - q⁻¹)")
    w.add_parameter(
        "upstream_function",
        "pn.trace_weights_n_q_schur(N, q) — PR #1256 commit 4059af433",
    )
    w.add_data("per_torus_knot_results", results)

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
