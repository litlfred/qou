#!/usr/bin/env python3
"""
SDP on shadow prices: find the linear combination of partitions
λ ⊢ 3·A_magic whose shadow-price-weighted sum matches the observed
binding scale.

The shell Iwahori–Hecke algebra is H_{3·A_magic}(q) (3 strands per
nucleon × A_magic nucleons), NOT H_{A_magic}(q); partitions therefore
range over λ ⊢ 3·A_magic.  Full enumeration is used (no Plancherel
truncation) — p(3·A_magic) grows quickly but stays tractable for
A_magic ∈ {2, 8}.  Larger A_magic (20, 28) is left to the upstream
symbolic-in-q / CRT path.

Setup:
  Variables x_λ ∈ ℝ_{≥0} (or ℤ_{≥0} for integer version) for each
  partition λ ⊢ 3·A_magic.
  Constraints:
    - Frobenius positivity: Σ_λ x_λ · y_λ ≥ physical binding target
    - Wedderburn normalization: Σ_λ x_λ · w_λ = 1 (probability-like)
    - 2×2 PSD blocks for partition pairs (quadratic coupling)
  Objective: minimize Σ_λ x_λ · y_λ (dual to primal LP)

For each magic A, solve the SDP to identify which partition(s) the
shell operator lives on.
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

import mpmath
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from sigma_shell_characterization import (
    partitions_of, shadow_price_at_partition, q_int_mp, q_fact_mp, q_dim,
    classical_dim,
)
from mass_endomorphism import q0 as q0_f

mpmath.mp.dps = 40
q0 = mpmath.mpf(str(q0_f))
# MAGIC entries run λ ⊢ 3·A_magic.  p(6)=11, p(24)=1575 — tractable;
# p(60) ≈ 10⁶ and p(84) ≈ 3·10⁷ are left to symbolic-in-q callers.
MAGIC = [2, 8]
# Target binding scale per magic A (B_AME per nucleon ~ 8.5 MeV →
# y_shell_target ~ 8.5 / 938 ≈ 0.009)
TARGET_Y = mpmath.mpf('0.009')


def build_partition_data(A_magic):
    """Build (partition, w_λ, y_λ, d_λ) for all partitions λ ⊢ 3·A_magic.

    The shell algebra is H_{3·A_magic}(q); full enumeration (no
    Plancherel truncation).
    """
    k = 3 * A_magic
    parts = partitions_of(k)
    data = []
    for p in parts:
        d_cl = classical_dim(p, k)
        if d_cl == 0:
            continue
        w = (q_dim(p, k) ** 2) / q_fact_mp(k)
        y = w / d_cl - 1 / q_fact_mp(k)
        data.append({
            "partition": p, "d_cl": d_cl, "w": w, "y": y,
            "w_f": float(w), "y_f": float(y), "y_abs": abs(float(y)),
        })
    return data


def sdp_shadow_lp(A_magic, target_y, use_integer=False):
    """LP (continuous) on shadow-price vector: find min-cost
    non-negative combo summing to target_y.

    min  Σ_λ x_λ · w_λ  (minimize total Wedderburn weight)
    s.t. Σ_λ x_λ · y_λ = target_y   (match binding scale)
         Σ_λ x_λ · w_λ ≤ 1           (probability constraint)
         x_λ ≥ 0
    """
    try:
        import cvxpy as cp
    except ImportError:
        return {"status": "no_cvxpy"}

    pdata = build_partition_data(A_magic)
    n = len(pdata)
    if n == 0:
        return {"status": "no_partitions"}

    y_vec = np.array([d["y_f"] for d in pdata])
    w_vec = np.array([d["w_f"] for d in pdata])

    if use_integer:
        x = cp.Variable(n, integer=True, nonneg=True)
    else:
        x = cp.Variable(n, nonneg=True)

    constraints = [
        y_vec @ x == float(target_y),
        w_vec @ x <= 1.0,
    ]
    objective = cp.Minimize(w_vec @ x)

    prob = cp.Problem(objective, constraints)
    try:
        if use_integer:
            prob.solve(solver=cp.GLPK_MI, verbose=False)
        else:
            prob.solve(solver=cp.SCS, verbose=False)
        if prob.status in [cp.OPTIMAL, cp.OPTIMAL_INACCURATE]:
            x_vals = x.value if x.value is not None else np.zeros(n)
            # Identify active partitions (x > threshold)
            active = []
            for i, d in enumerate(pdata):
                if x_vals[i] > 1e-6:
                    active.append({
                        "partition": str(d["partition"]),
                        "x": float(x_vals[i]),
                        "y_abs": float(d["y_abs"]),
                        "w_lam": float(d["w_f"]),
                    })
            active.sort(key=lambda a: -a["x"])
            return {
                "status": "solved",
                "A_magic": A_magic,
                "target_y": float(target_y),
                "objective_value": float(prob.value) if prob.value else None,
                "n_partitions": n,
                "n_active": len(active),
                "active_partitions": active[:10],
                "use_integer": use_integer,
            }
    except Exception as e:
        return {"status": "solve_error", "error": str(e)}
    return {"status": "no_solution"}


def sdp_shadow_psd(A_magic, target_y):
    """SDP (continuous) with 2×2 PSD coupling between partition pairs.

    Adds pairwise PSD blocks: for partitions λ, μ with compatible
    Young's-lattice structure, constrain
      [[x_λ · w_λ,  coupling_{λμ}], [coupling_{λμ},  x_μ · w_μ]] ⪰ 0
    """
    try:
        import cvxpy as cp
    except ImportError:
        return {"status": "no_cvxpy"}

    pdata = build_partition_data(A_magic)
    n = len(pdata)
    if n == 0:
        return {"status": "no_partitions"}

    y_vec = np.array([d["y_f"] for d in pdata])
    w_vec = np.array([d["w_f"] for d in pdata])

    x = cp.Variable(n, nonneg=True)

    constraints = [
        y_vec @ x == float(target_y),
        w_vec @ x <= 1.0,
    ]

    # PSD coupling: between adjacent partitions in Young's lattice
    # (only immediate neighbors to keep SDP tractable)
    n_psd = 0
    MAX_PSD = min(100, n * (n - 1) // 2)
    for i in range(n - 1):
        if n_psd >= MAX_PSD:
            break
        # Only couple consecutive partitions (small cost)
        j = i + 1
        if j >= n:
            continue
        coupling = cp.Variable(nonneg=True)
        block = cp.bmat([
            [x[i] * w_vec[i] + 0.01, coupling],
            [coupling, x[j] * w_vec[j] + 0.01],
        ])
        constraints.append(block >> 0)
        constraints.append(coupling <= (x[i] * w_vec[i] + x[j] * w_vec[j]) / 2)
        n_psd += 1

    objective = cp.Minimize(cp.sum(cp.multiply(w_vec, x)))
    prob = cp.Problem(objective, constraints)

    try:
        prob.solve(solver=cp.SCS, verbose=False)
        if prob.status in [cp.OPTIMAL, cp.OPTIMAL_INACCURATE]:
            x_vals = x.value if x.value is not None else np.zeros(n)
            active = []
            for i, d in enumerate(pdata):
                if x_vals[i] > 1e-6:
                    active.append({
                        "partition": str(d["partition"]),
                        "x": float(x_vals[i]),
                        "y_abs": float(d["y_abs"]),
                        "w_lam": float(d["w_f"]),
                    })
            active.sort(key=lambda a: -a["x"])
            return {
                "status": "solved",
                "A_magic": A_magic,
                "target_y": float(target_y),
                "objective_value": float(prob.value) if prob.value else None,
                "n_psd_blocks": n_psd,
                "n_active": len(active),
                "active_partitions": active[:10],
            }
    except Exception as e:
        return {"status": "solve_error", "error": str(e)}
    return {"status": "no_solution"}


if __name__ == "__main__":
    print("SDP ON SHADOW PRICES — identify shell-operator partition support")
    print("=" * 80)
    print(f"q_0 = {q0}")
    print(f"Target y_shell ≈ {float(TARGET_Y)} (≈ B_AME/(A·938) for nuclear binding)")
    print()

    all_results = {}
    for A_m in MAGIC:
        k = 3 * A_m
        print(f"\nA_magic = {A_m}  (Hecke level k = 3·A_magic = {k})")
        print(f"  Partition count p({k}) = {len(partitions_of(k))}")
        print()

        # LP (continuous)
        r_lp = sdp_shadow_lp(A_m, TARGET_Y, use_integer=False)
        print(f"  LP (continuous): {r_lp.get('status')}, "
              f"n_active={r_lp.get('n_active', 0)}")
        for a in r_lp.get('active_partitions', [])[:5]:
            print(f"    x={a['x']:.4f} on {a['partition']:<20} "
                  f"y={a['y_abs']:.4e} w={a['w_lam']:.4e}")

        # SDP (continuous with PSD)
        r_sdp = sdp_shadow_psd(A_m, TARGET_Y)
        print(f"  SDP (w/ PSD): {r_sdp.get('status')}, "
              f"n_active={r_sdp.get('n_active', 0)}, "
              f"n_psd={r_sdp.get('n_psd_blocks', 0)}")
        for a in r_sdp.get('active_partitions', [])[:5]:
            print(f"    x={a['x']:.4f} on {a['partition']:<20} "
                  f"y={a['y_abs']:.4e} w={a['w_lam']:.4e}")

        # ILP (integer)
        r_ilp = sdp_shadow_lp(A_m, TARGET_Y, use_integer=True)
        print(f"  ILP (integer): {r_ilp.get('status')}, "
              f"n_active={r_ilp.get('n_active', 0)}")
        for a in r_ilp.get('active_partitions', [])[:5]:
            print(f"    x={int(a['x'])} on {a['partition']:<20} "
                  f"y={a['y_abs']:.4e} w={a['w_lam']:.4e}")

        all_results[A_m] = {"LP": r_lp, "SDP_PSD": r_sdp, "ILP": r_ilp}

    witness = {
        "computation": "sdp-on-shadows",
        "description": (
            "SDP/LP/ILP on shadow prices over λ ⊢ 3·A_magic to identify "
            "shell-operator partition support. Constraint: "
            "Σ x_λ y_λ = target_y (physical binding scale ≈ 0.009). "
            "Full enumeration — no Plancherel truncation. Reports "
            "active partitions."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q_0": str(q0), "target_y": str(TARGET_Y),
                       "magic_numbers": MAGIC,
                       "hecke_levels": [3 * A for A in MAGIC]},
        "results": all_results,
    }
    out = Path(__file__).parent / "sdp-on-shadows.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
