#!/usr/bin/env python3
"""From-scratch derivation: T (³H tritium) at H_5 with SDP-canonical braid.

Per joint-tower-sdp-h6-h9.witness.json:
  T: n_0 = 5
  braid_word = [-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2]
  ρ = 2
  knot = 8_11

H_5 has 7 partitions:
  (5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1,1,1,1,1)
with dimensions 1, 4, 5, 6, 5, 4, 1.

Derivation chain (no library reuse):
  1. Hoefsmit σ_i^λ for each λ ⊢ 5 — from hoefsmit_general.py
  2. χ_λ(T_w(T)) = trace(matrix product) — from hoefsmit_general.py
  3. Wenzl y_λ via Markov axioms — from wenzl_y_axiomatic.py
  4. tr_M = Σ_λ y_λ · χ_λ
  5. B(T) = m_e · ρ · tr_M — paper formula
"""
from __future__ import annotations
import sympy as sp
import sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))  # for experimental_constants
from hoefsmit_general import (
    q, partitions_of, chi_lambda_braid, chi_lambda_braid_numeric,
)
from wenzl_y_axiomatic import derive_wenzl_y
from experimental_constants import M_E_MEV  # noqa: E402


if __name__ == "__main__":
    print("=" * 78)
    print("From-scratch T at H_5 — SDP-canonical braid")
    print("=" * 78)

    # T's SDP-canonical braid in B_5
    braid = [-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2]
    rho = 2
    n = 5
    print(f"  Braid word: {braid}")
    print(f"  ρ_factor: {rho}")
    print(f"  n_0 = {n}, knot = 8_11")
    print()

    # Step 1: derive Wenzl y_λ for H_5 via Markov axioms (numerical at q_0
    # to keep H_5 tractable; symbolic solve over 7 q-rationals is slow)
    print("─" * 78)
    print("Step 1: Wenzl y_λ via Markov axioms (H_5, numerical at q_0)")
    print("─" * 78)
    q0 = sp.Rational(11099785827513808, 10**16)
    t0 = time.time()
    y_lambda = derive_wenzl_y(n, numerical=True, q_value=q0)
    if y_lambda is None:
        print("FATAL: Wenzl y_λ derivation failed (system singular)")
        sys.exit(1)
    print(f"  ({time.time() - t0:.1f}s)")

    print("\n  Wenzl y_λ at q_0:")
    for lam, y in y_lambda.items():
        print(f"    y_{lam} = {y:>+10.6f}")
    print()

    # Step 2: χ_λ on T's braid for each partition
    print("─" * 78)
    print("Step 2: χ_λ(T_w(T)) via Hoefsmit matrices for each λ ⊢ 5")
    print("─" * 78)
    chi_at_q0 = {}
    for lam in partitions_of(n):
        t0 = time.time()
        chi_q0 = chi_lambda_braid_numeric(lam, braid, q0)
        chi_at_q0[lam] = chi_q0
        print(f"  λ={lam}: χ_λ(T_w(T)) at q_0 = {chi_q0:>+10.6f}  "
              f"({time.time() - t0:.1f}s)")
    print()

    # Step 3: Markov trace
    print("─" * 78)
    print("Step 3: tr_M(T_w(T)) = Σ_λ y_λ · χ_λ(T_w(T))")
    print("─" * 78)
    tr_M_q0 = 0.0
    for lam in partitions_of(n):
        y_q0 = y_lambda[lam]   # already numerical
        contrib = y_q0 * chi_at_q0[lam]
        tr_M_q0 += contrib
        print(f"  λ={lam}: y={y_q0:>+9.5f} · χ={chi_at_q0[lam]:>+9.5f} "
              f"= {contrib:>+9.5f}")
    print(f"\n  Total: tr_M(T_w(T)) at q_0 = {tr_M_q0:.6f}")
    print()

    # Step 4: paper formula
    print("─" * 78)
    print("Step 4: Paper formula B = m_e · ρ · tr_M(T_w)")
    print("─" * 78)
    M_E = M_E_MEV
    B_pred = M_E * rho * tr_M_q0
    B_AME = 8.481798
    err = (B_pred - B_AME) / B_AME * 100
    print(f"  B_pred = {M_E} · {rho} · {tr_M_q0:.6f} = {B_pred:.6f} MeV")
    print(f"  B_AME  = {B_AME:.6f} MeV")
    print(f"  err = {err:+.2f}%")
    print()

    print("Cross-check: existing compute (probe_sdp_canonical_paper_formula):")
    print("  Plancherel  tr_M(T_w(T)) = -0.000995")
    print("  Wenzl-Schur tr_M(T_w(T)) =  0.012889")
    print(f"  From-scratch              =  {tr_M_q0:.6f}")
    if abs(tr_M_q0 - 0.012889) < 1e-3:
        print("  ✓ MATCHES Wenzl-Schur to 3 decimal places")
    elif abs(tr_M_q0 + 0.000995) < 1e-3:
        print("  ✓ MATCHES Plancherel to 3 decimal places")
    else:
        print(f"  ✗ Discrepancy of {abs(tr_M_q0 - 0.012889):.6f} from Wenzl-Schur")
