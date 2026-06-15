#!/usr/bin/env python3
"""Jones-Markov weights y_λ at H_12(q) — extension of alpha_k_jones_markov_h4.py.

Per author direction 2026-05-25 + sibling commit c70707397 H_3-vs-H_{3A}
legacy bug audit: 4He needs H_12 weights (3 strands × 4 nucleons = 12),
NOT H_3 weights as production currently uses.

## Method

77 partitions of 12 = 77 conjugacy classes of S_12 = 77 cycle types.

For each cycle type λ = (c_1, c_2, ..., c_r):
  - Build representative braid: concatenated cycles
      cycle (c_i) = σ_a σ_{a+1} ... σ_{a+c_i-2}  (c_i-1 generators)
      starting at a fresh strand offset
  - Total braid length = n − r where r = number of parts
  - Markov property:
      tr_M(cycle-type representative) = z^{n - r}

Linear system: 77 cycle-type braids × 77 partitions = 77×77 χ-matrix
(q-deformed character table of S_12). Invertible by Schur orthogonality.

  A · y = b
  A[i,j] = χ_{λ_j}(rep braid for cycle type λ_i, q)
  b[i] = z^{n - r(λ_i)}
  y[j] = y_{λ_j}  (Jones-Markov weight for partition λ_j)

## Why 4He needs H_12 (not H_3)

Per sibling audit, `pyhecke/atom.py:555-569` hardcodes H_3 weights for
all atoms. For 4He with A=4 nucleons × 3 color strands = 12 strands,
the correct algebra is H_12(q). Different y_λ distribution.

## Output

- Console: 77 y_λ values + verification (Σ y_λ · dim_λ = 1)
- Witness: alpha-k-jones-markov-h12.witness.json
- Cross-check: compute tr_M(β_⁴He) = Σ y_λ · χ_λ(β_⁴He) for the
  heuristic β_⁴He = 4·𝓑_3 disjoint, compare to multiplicative formula
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np
import pyhecke_native as pn
from sympy.utilities.iterables import partitions

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 30
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
q0_mpf = mp.mpf(json.load(Q_PIN.open())["derived_50_digit"]["q"])
q0_f64 = float(q0_mpf)
h_f64 = float(q0_mpf - 1 / q0_mpf)
z_mark = 1 / (mp.sqrt(q0_mpf) + 1 / mp.sqrt(q0_mpf))
z_f64 = float(z_mark)

N_STRANDS = 12

# Closed-form Borromean Markov trace (from pm_qm_pythagorean_identity.py)
def tr_M_borromean(h_val):
    h2 = h_val * h_val
    h4 = h2 * h2
    h6 = h4 * h2
    return (4 + h2 - 3 * h4 - h6) / (h2 + 4)


def partitions_of_descending(n: int) -> list[list[int]]:
    """All partitions of n as descending-sorted lists."""
    shapes = []
    for p in partitions(n):
        parts = sorted(p.items(), reverse=True)
        expanded = []
        for size, count in parts:
            expanded.extend([size] * count)
        shapes.append(expanded)
    return shapes


def cycle_type_braid(parts: list[int]) -> list[tuple[int, int]]:
    """Build a cycle-type representative braid.

    For parts = (c_1, c_2, ..., c_r), the representative is:
      cycle(c_1) on strands 1..c_1   (using gens 1..c_1-1)
      cycle(c_2) on strands c_1+1..c_1+c_2 (using gens c_1+1..c_1+c_2-1)
      etc.

    Each cycle (c_i) ↦ σ_a σ_{a+1} ... σ_{a+c_i-2}  (c_i-1 letters)

    Format: list of (sign, gen_1based) per pyhecke_native.chi_lambda_braid.
    """
    word = []
    offset = 0
    for c in parts:
        for k in range(c - 1):
            word.append((1, offset + 1 + k))
        offset += c  # next cycle starts after this one's strands
    return word


def main() -> int:
    n = N_STRANDS
    print("=" * 110)
    print(f"Jones-Markov weights y_λ at H_{n}(q) — extends alpha_k_jones_markov_h4.py to A=4 (4He)")
    print(f"  q_0 = {q0_f64:.10f}  h = {h_f64:.10f}  z = {z_f64:.10f}")
    print("=" * 110)
    print()

    shapes = partitions_of_descending(n)
    print(f"Partitions of {n}: {len(shapes)}")
    print()

    print(f"Building cycle-type representative braids for all {len(shapes)} partitions...")
    rep_braids = {tuple(sh): cycle_type_braid(sh) for sh in shapes}

    # RHS: tr_M(cycle-type rep) = z^{n - r}
    rhs = {tuple(sh): z_mark ** (n - len(sh)) for sh in shapes}

    print(f"Computing 77×77 χ-matrix via pyhecke_native.chi_lambda_braid...")
    t_start = time.time()
    # A[i, j] = χ_{λ_j}(rep_braid for λ_i)
    A = np.zeros((len(shapes), len(shapes)), dtype=np.float64)
    for i, row_lam in enumerate(shapes):
        word = rep_braids[tuple(row_lam)]
        for j, col_lam in enumerate(shapes):
            A[i, j] = pn.chi_lambda_braid(col_lam, word, q0_f64)
        if (i + 1) % 20 == 0:
            print(f"  row {i+1}/{len(shapes)}  ({time.time() - t_start:.1f}s)")
    elapsed = time.time() - t_start
    print(f"  χ-matrix built in {elapsed:.1f}s")
    print()

    # RHS as float vector
    b = np.array([float(rhs[tuple(sh)]) for sh in shapes])

    # Condition number
    cond = np.linalg.cond(A)
    print(f"  Condition number of χ-matrix: {cond:.3e}")
    if cond > 1e12:
        print(f"  ⚠ Poorly conditioned — results may be unstable")

    # Solve
    print(f"  Solving 77×77 linear system...")
    try:
        y = np.linalg.solve(A, b)
    except np.linalg.LinAlgError as e:
        print(f"  ✗ Singular: {e}")
        return 1

    # Verification: Σ y_λ · dim_λ should be ≈ 1 (Markov normalization on identity)
    dims = [int(pn.chi_lambda_braid(sh, [], q0_f64) + 0.5) for sh in shapes]
    sum_y_dim = sum(y[i] * dims[i] for i in range(len(shapes)))
    print(f"  Σ y_λ · dim_λ = {sum_y_dim:.10f}  (expected = 1.0)")
    print()

    # Print top y_λ by magnitude
    print("Top 10 partitions by |y_λ|:")
    print(f"  {'partition':>30}  {'dim S_λ':>9}  {'y_λ':>16}")
    y_sorted = sorted(zip(shapes, dims, y), key=lambda x: -abs(x[2]))
    for sh, d, yv in y_sorted[:10]:
        sh_str = "(" + ",".join(map(str, sh)) + ")"
        print(f"  {sh_str:>30}  {d:>9}  {yv:>+16.10f}")

    print("\nBottom 5 partitions by |y_λ|:")
    for sh, d, yv in y_sorted[-5:]:
        sh_str = "(" + ",".join(map(str, sh)) + ")"
        print(f"  {sh_str:>30}  {d:>9}  {yv:>+16.10f}")

    # Apply: compute tr_M(β_⁴He) = Σ y_λ · χ_λ(β_⁴He) for heuristic β = 4·𝓑_3
    print("\n=== Application: tr_M(β_⁴He) for heuristic 4·Borromean ===")
    # Build β_⁴He = 4 disjoint Borromean copies
    def borromean_on(base):
        s1, s2 = base, base + 1
        return [(1, s1), (-1, s2)] * 3
    beta_he4 = borromean_on(1) + borromean_on(4) + borromean_on(7) + borromean_on(10)
    chi_he4 = [pn.chi_lambda_braid(sh, beta_he4, q0_f64) for sh in shapes]
    tr_M_he4 = sum(y[i] * chi_he4[i] for i in range(len(shapes)))
    # Multiplicative formula
    tr_M_bor = float(tr_M_borromean(mp.mpf(h_f64)))
    tr_M_he4_mult = tr_M_bor ** 4
    print(f"  tr_M(β_𝓑_3) closed form at q_0       = {tr_M_bor:.10f}")
    print(f"  tr_M(β_⁴He) via Σ_λ y_λ·χ_λ (this)    = {tr_M_he4:.10f}")
    print(f"  tr_M(β_⁴He) multiplicative (4·𝓑_3)   = {tr_M_he4_mult:.10f}")
    print(f"  agreement: |Σ - mult| = {abs(tr_M_he4 - tr_M_he4_mult):.2e}")
    print()

    # Test against B(⁴He) AME
    print("=== Test 4: does this close the B(⁴He) gap? ===")
    m_e = float(mp.mpf("0.510998950"))
    vol_bor = float(8 * mp.catalan)
    B_AME = 28.2956912
    candidates = {
        "B_prod (2·m_e·A·8G, ν=2)": 2 * m_e * 4 * vol_bor,
        "m_e·A·8G·tr_M(β_⁴He)_H12": m_e * 4 * vol_bor * tr_M_he4,
        "2·m_e·A·8G·tr_M(β_⁴He)_H12": 2 * m_e * 4 * vol_bor * tr_M_he4,
    }
    print(f"  B_AME(⁴He) = {B_AME:.6f} MeV")
    for name, val in candidates.items():
        diff = (val - B_AME) / B_AME * 100
        print(f"  {name:<35} = {val:>9.4f} MeV  ({diff:+8.4f}%)")

    # Witness
    w = WitnessBuilder("alpha-k-jones-markov-h12", engine="python+pyhecke-native+numpy")
    w.set_description(
        "Jones-Markov weights y_λ at H_12(q) — full 77-partition atlas. "
        "Extends sibling alpha_k_jones_markov_h4.py to the algebra needed "
        "for 4He per the H_3-vs-H_{3A} legacy bug audit (commit c70707397). "
        "Builds 77 cycle-type representative braids, computes 77×77 q-Hecke "
        "character matrix via pyhecke_native.chi_lambda_braid, solves linear "
        "system from Markov-axiom RHS tr_M(rep) = z^{n-r}. Cross-checks "
        "tr_M(β_⁴He) via Σ y_λ · χ_λ vs the multiplicative formula "
        "tr_M(β_𝓑_3)^4 on 4 disjoint Borromean copies."
    )
    w.add_parameter("q_0_f64", q0_f64)
    w.add_parameter("z_mark_f64", z_f64)
    w.add_parameter("n_partitions", len(shapes))
    w.add_parameter("chi_matrix_condition_number", float(cond))
    w.add_parameter("sum_y_dim_check", float(sum_y_dim))
    w.add_parameter("elapsed_seconds", float(elapsed))
    w.add_parameter("tr_M_he4_via_y_lambda", float(tr_M_he4))
    w.add_parameter("tr_M_he4_multiplicative", float(tr_M_he4_mult))
    w.add_data("y_lambda_table", [
        {"partition": sh, "dim_S_lambda": d, "y_lambda": float(yv)}
        for sh, d, yv in zip(shapes, dims, y)
    ])
    w.add_data("candidate_B_4He_MeV", {n: float(v) for n, v in candidates.items()})
    w.add_data("B_4He_AME_MeV", B_AME)
    w.add_assertion(
        "all_77_y_lambda_computed",
        computed=len(y),
        expected=77,
        tolerance=0,
        unit="weights",
        source="77-partition linear system solve",
    )
    w.add_assertion(
        "markov_normalization_holds",
        computed=float(sum_y_dim),
        expected=1.0,
        tolerance=1e-6,
        unit="dimensionless",
        source="Σ y_λ · dim_λ on identity braid",
    )
    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
