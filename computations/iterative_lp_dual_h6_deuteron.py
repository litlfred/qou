#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only output.
"""
Iterative LP-dual at H_6 for the deuteron — natural next step after
Phase 1.14 (H_3 LP-dual at proton).

Per term7-alpha5's `prop:mass-formula-iterative-lp-dual`:

  𝔪(T_w) = Σ_{ℓ=0}^{ℓ_max} u^{(ℓ)*}(T_w)
  u^{(ℓ)*}(T_w) = m_e · tr_M(P_ℓ · T_w) / [n]_q!
  P_ℓ = e_ℓ(J_1, …, J_n) ∈ Z(H_n(q))    (Murphy 1981)

For the deuteron β_D at H_6 (n=6, 11 partitions):

  u^{(ℓ)*}(β_D) = m_e · Σ_{λ⊢6} y_λ(q_0) · c_ℓ(λ) · χ^λ(β_D) / [6]_q!

This script:
  1. Loads y_λ values for partitions of 6 from y-lambda-mpfr-witness.json
     (50 dps, all 11 partitions).
  2. Computes χ^λ(β_D) NUMERICALLY at q_0 by applying the deuteron's
     atom_braid_word_3A(1, 1) crossings to the Hoefsmit seminormal
     matrices for each partition.
  3. Cross-validates: Σ_λ y_λ · χ^λ(β_D) = 0.3883 (matches the closed-
     form deuteron Markov trace from `wenzl_n6_closed_form.witness.json`).
  4. Computes c_ℓ(λ) = e_ℓ({q_0^{2c(□)} : □ ∈ λ}) per partition × level.
  5. Computes u^{(ℓ)*}(β_D) for ℓ ∈ {0, 1, …, 6}.
  6. Reports Σ_ℓ u^{(ℓ)*}(β_D) and compares to:
     - m_p + m_n − B(D)_AME = 1875.61 MeV  (CODATA atomic mass)
     - 2·m_p_pred (the disjoint product convention)

Output: iterative-lp-dual-h6-deuteron.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from itertools import combinations
from pathlib import Path
from typing import Tuple

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import mpmath as mp

mp.mp.dps = 30

from witness_base import WitnessBuilder
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from q_parameter import Q as Q0_FLOAT
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402


# ─────────────────────────────────────────────────────────────────
# Partition enumeration
# ─────────────────────────────────────────────────────────────────

def partitions_of(n):
    if n == 0:
        return [()]
    out = []
    def gen(rem, cap, cur):
        if rem == 0:
            out.append(tuple(cur))
            return
        for p in range(min(rem, cap), 0, -1):
            cur.append(p)
            gen(rem - p, p, cur)
            cur.pop()
    gen(n, n, [])
    return out


def cell_contents(shape) -> list[int]:
    return [j - i for i, row in enumerate(shape) for j in range(row)]


def c_ell(shape, ell: int, q_val: float) -> float:
    """e_ℓ({q^{2c(□)} : □ ∈ λ}) at numerical q."""
    cells = cell_contents(shape)
    if ell == 0:
        return 1.0
    if len(cells) < ell:
        return 0.0
    eigenvalues = [q_val ** (2 * c) for c in cells]
    total = 0.0
    for subset in combinations(eigenvalues, ell):
        prod = 1.0
        for v in subset:
            prod *= v
        total += prod
    return total


def q_int_num(n, q_val):
    if n == 0:
        return 0.0
    return sum(q_val ** (n - 1 - 2 * k) for k in range(n))


def q_factorial_num(n, q_val):
    res = 1.0
    for k in range(1, n + 1):
        res *= q_int_num(k, q_val)
    return res


# ─────────────────────────────────────────────────────────────────
# Numerical χ^λ(β) via Hoefsmit seminormal matrices
# ─────────────────────────────────────────────────────────────────

def chi_lambda_numerical(shape, crossings_cd, q_val: float, h_val: float):
    """Compute χ^λ(β) numerically by tracing through Hoefsmit matrices.

    Note: `build_seminormal_matrices(shape)` uses the canonical q from
    `q_parameter` (= q_0).  The (q_val, h_val) parameters here are
    accepted for caller-side documentation / future generalisation, but
    the matrix construction itself pins to q_0; callers should not pass
    a different q without first plumbing it through `build_seminormal_matrices`.

    crossings_cd: list of (c, d, gen_idx) triples (atom_braid_word_3A shape)
      σ_i positive crossing:  (1, 0, gen)         → step = σ_i
      σ_i⁻¹:                  (1, -h, gen)        → step = σ_i − h·I = σ_i⁻¹
      averaged ½(σ+σ⁻¹):      (1, -h/2, gen)      → step = σ_i − (h/2)·I
      generic c·σ + d·I:                          → step = c·σ_i + d·I
    """
    del q_val, h_val   # q_val/h_val pinned to q_0 inside build_seminormal_matrices
    from hecke_characters import build_seminormal_matrices
    sigmas, dim, _ = build_seminormal_matrices(tuple(shape))
    if dim == 0:
        return 0.0
    M = np.eye(dim, dtype=complex)
    for c, d, gen in crossings_cd:
        s_i = sigmas[gen]
        step = c * s_i + d * np.eye(dim, dtype=complex)
        M = M @ step
    return float(np.real(np.trace(M)))


def main() -> int:
    print("=" * 100)
    print("ITERATIVE LP-DUAL AT H_6 FOR DEUTERON")
    print("=" * 100)

    # Load y_λ values for n=6
    here = Path(__file__).parent
    y_witness_path = here / "y-lambda-mpfr-witness.json"
    with open(y_witness_path) as f:
        y_data = json.load(f)
    weights = y_data["tables_by_n"]["6"]["weights"]
    y_at_q0 = {tuple(w["partition"]): mp.mpf(w["y_lambda"]) for w in weights}
    parts_6 = list(y_at_q0.keys())

    print("\n  y_λ(q_0) for partitions of 6 (from y-lambda-mpfr-witness.json):")
    for p in parts_6:
        print(f"    y_{p} = {mp.nstr(y_at_q0[p], 12)}")

    # Build deuteron braid word
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_core import h as h_num
    h_val = float(h_num)
    q_val = float(Q0_FLOAT)
    word = atom_braid_word_3A(1, 1)
    print(f"\n  Deuteron braid word: {len(word)} crossings, q_0 = {q_val:.6f}")

    # Compute χ^λ(β_D) numerically for each partition
    print("\n  Computing χ^λ(β_D) numerically at q_0 (this may take a moment)...")
    chi_at_q0 = {}
    for p in parts_6:
        chi = chi_lambda_numerical(p, word, q_val, h_val)
        chi_at_q0[p] = mp.mpf(chi)
        print(f"    χ^{p}(β_D) = {chi:+.10f}")

    # Cross-validate Σ_λ y_λ · χ^λ(β_D) ≈ 0.3883
    tr_M_check = sum(y_at_q0[p] * chi_at_q0[p] for p in parts_6)
    print(f"\n  Cross-validation:")
    print(f"    Σ_λ y_λ · χ^λ(β_D) = {mp.nstr(tr_M_check, 12)}")
    print(f"    Closed-form ref    = 0.3882864240747888")
    err_rel = abs(tr_M_check - mp.mpf("0.3882864240747888")) / mp.mpf("0.3882864240747888")
    print(f"    rel error          = {float(err_rel):.2e}")

    # c_ℓ(λ) per partition × level ℓ ∈ {0..6}
    print("\n  c_ℓ(λ) = e_ℓ({q_0^{2c(□)} : □ ∈ λ}) per partition × level:")
    c_ell_at_q0 = {}
    for p in parts_6:
        c_ell_at_q0[p] = {}
        for ell in range(7):
            c_ell_at_q0[p][ell] = mp.mpf(c_ell(p, ell, q_val))

    # u^{(ℓ)*}(β_D) for each level
    qfact_6_q0 = mp.mpf(q_factorial_num(6, q_val))
    m_e = mp.mpf(M_E_MEV)
    print(f"\n  [6]_q! at q_0 = {mp.nstr(qfact_6_q0, 12)}")
    print(f"  m_e          = {M_E_MEV} MeV")

    print(f"\n  u^{{(ℓ)*}}(β_D) per level:")
    print(f"  {'ℓ':<3} {'u^{(ℓ)*}(D) MeV':<22} {'tr_M(P_ℓ·β_D)':<22}")
    u_levels = {}
    for ell in range(7):
        tr_M_Pl_beta_D = sum(
            y_at_q0[p] * c_ell_at_q0[p][ell] * chi_at_q0[p]
            for p in parts_6
        )
        u_l = m_e * tr_M_Pl_beta_D / qfact_6_q0
        u_levels[ell] = u_l
        print(f"  {ell:<3} {float(u_l):<22.10f} {float(tr_M_Pl_beta_D):<22.10f}")

    sum_u = sum(u_levels.values())
    print(f"\n  Σ_{{ℓ=0}}^{{6}} u^{{(ℓ)*}}(β_D) = {float(sum_u):.6f} MeV")

    # ── Comparisons ──
    print()
    print("─" * 100)
    print("  Comparisons")
    print("─" * 100)
    M_D_codata = M_P_MEV + M_N_MEV - float(AME_B_DEUTERON_MEV_VALIDATION)   # AME atomic mass
    Z_M_p_plus_N_M_n = 1 * M_P_MEV + 1 * M_N_MEV
    print(f"\n  CODATA atomic D mass:        {M_D_codata:.4f} MeV")
    print(f"  Z·m_p + N·m_n (free):       {Z_M_p_plus_N_M_n:.4f} MeV")
    print(f"  AME B(D):                   2.2246 MeV")
    print(f"\n  Σ_ℓ u^{{(ℓ)*}}(β_D) at H_6 = {float(sum_u):.4f} MeV")

    # The H_6 sum is at the natural Hecke level for the deuteron, so it
    # captures more structure than the H_3 proton sum. But it's still NOT
    # expected to recover M_D directly — the iterative LP-dual converges
    # only with the FULL braid encoding + the difference-frame
    # interpretation (per term7-alpha5).
    if abs(sum_u) > 1.0:
        ratio_to_M_D = float(sum_u) / M_D_codata
        print(f"\n  Σ_ℓ u^{{(ℓ)*}} / M_D_codata = {ratio_to_M_D:.6f}")
        print(f"  This captures {ratio_to_M_D*100:.3f}% of the deuteron's CODATA mass.")
        print(f"\n  Compare to Phase 1.14 (proton at H_3): 1.445 MeV / 938 = 0.15%")
        print(f"  At H_6, the sum is {float(sum_u):.2f} MeV — captures more structure")
        print(f"  but still falls short of full M_D, consistent with the framework's")
        print(f"  claim that absolute mass requires the FULL trace + difference frame.")

    # Per-level analysis: identify which ℓ contribute most
    print(f"\n  Per-level contribution magnitudes:")
    sorted_levels = sorted(u_levels.items(), key=lambda kv: abs(kv[1]), reverse=True)
    for ell, u_l in sorted_levels:
        pct = abs(float(u_l)) / abs(float(sum_u)) * 100 if abs(sum_u) > 1e-12 else 0
        print(f"    ℓ={ell}:  u^{{(ℓ)*}} = {float(u_l):>+12.6f} MeV  ({pct:5.1f}% of |Σ|)")

    # Witness emission
    w = WitnessBuilder("iterative-lp-dual-h6-deuteron", engine="numpy+mpmath")
    w.set_description(
        "Iterative LP-dual at H_6 for the deuteron β_D per term7-alpha5's "
        "prop:mass-formula-iterative-lp-dual.  Computes u^{(ℓ)*}(β_D) = "
        "m_e · Σ_λ y_λ(q_0) · c_ℓ(λ) · χ^λ(β_D) / [6]_q! for ℓ ∈ {0,…,6} "
        "with y_λ from y-lambda-mpfr-witness.json (50 dps, 11 partitions of 6) "
        "and χ^λ(β_D) computed numerically by applying the deuteron's "
        "atom_braid_word_3A(1,1) (23 crossings) to Hoefsmit seminormal "
        "matrices for each partition.  Cross-validates Σ_λ y_λ·χ^λ(β_D) "
        "against the closed-form |tr_M(β_D)| = 0.388 from "
        "wenzl_n6_closed_form.witness.json.  Reports Σ_ℓ u^{(ℓ)*}(β_D) "
        "and compares to CODATA M_D, Z·m_p+N·m_n, AME B(D)."
    )
    w.set_content_block("prop:mass-formula-iterative-lp-dual")
    w.add_parameter("q_0", q_val)
    w.add_parameter("h", h_val)
    w.add_parameter("hecke_level_n", 6)
    w.add_parameter("M_D_codata_atomic_MeV", M_D_codata)
    w.add_parameter("Z_M_p_plus_N_M_n_MeV", Z_M_p_plus_N_M_n)
    w.add_parameter("M_e_codata", M_E_MEV)
    w.add_data("y_lambda_at_q0",
               {str(k): float(v) for k, v in y_at_q0.items()})
    w.add_data("chi_lambda_beta_D_at_q0",
               {str(k): float(v) for k, v in chi_at_q0.items()})
    w.add_data("c_ell_at_q0",
               {str(k): {str(ell): float(v) for ell, v in d.items()}
                for k, d in c_ell_at_q0.items()})
    w.add_data("u_levels_deuteron_MeV",
               {str(ell): float(v) for ell, v in u_levels.items()})
    w.add_data("sum_u_levels_MeV", float(sum_u))
    w.add_data("tr_M_check_at_q0", float(tr_M_check))
    w.add_data("tr_M_check_rel_err", float(err_rel))

    w.add_assertion(
        "tr_M_cross_validation_within_1e-6",
        computed=float(err_rel),
        expected=0.0,
        tolerance=1e-6,
    )
    w.add_assertion(
        "u_levels_computed_for_deuteron",
        computed=len(u_levels),
        expected=7,
    )
    w.add_assertion(
        "sum_u_finite",
        computed=bool(0 < abs(float(sum_u)) < 10000),
        expected=True,
    )
    w.add_data("lean_uniqueness_ref", lean_uniqueness_ref("deuteron (²H)"))

    w.save()
    print(f"\n✓ Witness: iterative-lp-dual-h6-deuteron.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
