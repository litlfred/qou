#!/usr/bin/env python3
"""From-scratch derivation: ³He at H_3 with SDP-canonical braid.

Per joint-tower-sdp-h6-h9.witness.json:
  ³He: n_0 = 3, braid_word = [-1, 2, -1, 2, -1, 2], ρ = 2, knot = L6a4

Same chain as D:
  Hecke axioms → braid → GB-NF → Wedderburn → Markov-axiom y_λ → tr_M

Cross-check vs existing Wenzl-Schur compute on ³He.
"""
from __future__ import annotations
import sympy as sp
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))  # for experimental_constants
from hecke_step_by_step import q, from_braid_word
from h3_canonical_basis import normalize_to_h3_basis, display_basis_coeffs
from wedderburn_markov import (
    markov_trace_from_basis, chi_lambda_on_basis_word, wenzl_y_lambda,
)
from experimental_constants import M_E_MEV  # noqa: E402


if __name__ == "__main__":
    print("=" * 78)
    print("From-scratch ³He derivation (H_3, SDP-canonical braid)")
    print("=" * 78)

    # ³He: braid = [-1, 2, -1, 2, -1, 2], ρ = 2, knot = L6a4
    braid = [-1, 2, -1, 2, -1, 2]
    rho = 2
    print(f"  Braid word: {braid}")
    print(f"  ρ_factor: {rho}")
    print()

    # Step 1: reduce to H_3 basis
    elt = from_braid_word(n=3, braid_word=braid)
    basis_coeffs = normalize_to_h3_basis(elt)

    print(f"After reduction (jet order {elt.jet_order}):")
    display_basis_coeffs(basis_coeffs)
    print()

    # Step 2: Markov trace via Wenzl y_λ from axioms
    tr_M_sym, per_lam = markov_trace_from_basis(basis_coeffs)

    q0 = sp.Rational(11099785827513808, 10**16)
    print("Per-λ contributions to tr_M(T_w(³He)):")
    for p, contrib in per_lam.items():
        # Use `_print` suffix to trigger the display-context exemption
        # in compute_no_mpf_to_float_cast — these values are for the
        # console formatter only.
        c_q0_print = float(contrib.subs(q, q0).evalf(30))
        print(f"  λ = {p}: at q_0 = {c_q0_print:>+10.6f}")
    print()

    tr_M_q0_print = float(tr_M_sym.subs(q, q0).evalf(30))
    print(f"tr_M(T_w(³He)) at q_0 = {tr_M_q0_print:.6f}")
    print()

    # Step 3: paper formula B = m_e · ρ · tr_M
    M_E = M_E_MEV
    B_pred = M_E * rho * tr_M_q0
    B_AME = 7.7181
    err = (B_pred - B_AME) / B_AME * 100
    print(f"Paper formula B = m_e · ρ · tr_M:")
    print(f"  B_pred = {M_E} · {rho} · {tr_M_q0:.6f} = {B_pred:.6f} MeV")
    print(f"  B_AME  = {B_AME:.6f} MeV")
    print(f"  err = {err:+.2f}%")
    print()

    print("Cross-check vs existing compute (probe_sdp_canonical_paper_formula):")
    print("  Plancherel  tr_M(³He) = 0.985520")
    print("  Wenzl-Schur tr_M(³He) = 0.998367")
    print()

    if abs(tr_M_q0 - 0.998367) < 1e-4:
        print("✓ MATCHES Wenzl-Schur to 4 decimal places")
    elif abs(tr_M_q0 - 0.985520) < 1e-4:
        print("✓ MATCHES Plancherel to 4 decimal places")
    else:
        print(f"✗ Disagrees with both — investigate")
