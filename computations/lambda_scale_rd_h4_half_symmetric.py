#!/usr/bin/env python3
"""Option 1: H_4 symbolic Hoefsmit + half-symmetric projection π_HS.

Per the proof's Step 1 claim, the proton's natural Markov-stabilised
Hecke level is H_4(q), not H_3(q). At H_4, the canonical Borromean
braid β_Bor ∈ B_3 is lifted to B_4 via σ_3 attachment:
  β_stab = β_Bor · σ_3 ∈ B_4

The five Wedderburn blocks of H_4 are indexed by partitions of 4:
  (4), (3,1), (2,2), (2,1,1), (1,1,1,1)
with dimensions 1, 3, 2, 3, 1 (sum = 10 = 2·5, so the half-symmetric
count = 5/2 at q=1 follows from averaging).

The half-symmetric projection π_HS that matches 5/2 at identity is:
  π_HS(τ) = (1/4) · Σ_λ χ^λ(β)
           = (1/4) · [χ_(4) + χ_(3,1) + χ_(2,2) + χ_(2,1,1) + χ_(1,1,1,1)]

At identity (β = e): (1/4)·(1+3+2+3+1) = 10/4 = 5/2 ✓

This script computes π_HS(β_stab) symbolically and expands in h to
extract c_0, c_2, c_4, ... and compare to the conjecture's ansatz.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from experimental_constants import M_E_MEV, M_P_MEV  # noqa: E402
from hoefsmit_symbolic import Q, chi_lambda_symbolic  # noqa: E402

mp.mp.dps = 80
Q_NUM = Q_MP
H_NUM = Q_NUM - 1/Q_NUM
HBAR_Q_NUM = (Q_NUM - 1) / Q_NUM
G_NUM = mp.catalan
VOL_B3 = 8 * mp.catalan  # = Vol(Borromean rings complement), 8·G via Adams 1985
M_E = mp.mpf(M_E_MEV)
M_P = mp.mpf(M_P_MEV)
LAM_P_TARGET = (M_P / M_E) * HBAR_Q_NUM**2 / VOL_B3


def main() -> int:
    w = WitnessBuilder("lambda-scale-rd-h4-half-symmetric", engine="sympy")
    w.set_description(
        "Option 1: H_4 symbolic Hoefsmit + half-symmetric projection. "
        "Computes π_HS(β_stab) = (1/4) Σ_λ χ^λ(β_stab) symbolically "
        "for β_stab = β_Bor · σ_3 ∈ B_4 (Markov-stabilised Borromean "
        "braid). Expands in h to test λ_scale = 5/2 - h²·G - h⁴·c_4 ansatz."
    )
    w.set_content_block("conj:lambda-scale-substrate-form")

    # Markov-stabilised Borromean braid in B_4:
    # β_stab = β_Bor · σ_3 = (σ_1 σ_2^{-1})^3 · σ_3
    # gen_idx: σ_1 = 0, σ_2 = 1, σ_3 = 2 (0-indexed)
    crossings = []
    for _ in range(3):
        crossings.append((0, "sigma"))      # σ_1
        crossings.append((1, "sigma_inv"))  # σ_2^{-1}
    crossings.append((2, "sigma"))          # σ_3 (Markov stabilisation)
    print(f"Markov-stabilised Borromean braid in B_4: {crossings}")
    print(f"  Length: {len(crossings)} crossings")

    # Compute χ^λ for each partition of 4
    shapes = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    chis = {}
    for shape in shapes:
        print(f"\nComputing χ^{shape}(β_stab) ... ", end="", flush=True)
        chi = chi_lambda_symbolic(shape, crossings)
        chi_simplified = sp.simplify(chi)
        chis[shape] = chi_simplified
        print(f"done")
        print(f"  χ^{shape} = {chi_simplified}")
    w.add_data("chi_by_shape_symbolic_H4_stab", {str(k): str(v) for k, v in chis.items()})

    # Sanity at q=1: identity at H_4 should be dim V_λ
    # β_stab at q=1: (s_1 s_2)^3 · s_3 = id · s_3 = s_3 = (34)
    # χ_λ((34)) is the character of a transposition in S_4 standard rep
    # For S_4 reps:
    #   (4) trivial: χ((34)) = 1
    #   (3,1) standard: χ((34)) = +1  (3·(-1)+3·1 / 6 transpositions... let me think)
    #   (2,2): χ((34)) = 0
    #   (2,1,1): χ((34)) = -1 (sign × standard combo)
    #   (1,1,1,1) sign: χ((34)) = -1
    print("\nSanity check at q=1 (β_stab → (34) ∈ S_4):")
    expected = {(4,): 1, (3, 1): 1, (2, 2): 0, (2, 1, 1): -1, (1, 1, 1, 1): -1}
    for shape, chi_sym in chis.items():
        val_at_1 = sp.limit(chi_sym, Q, 1)
        expect = expected[shape]
        match = (val_at_1 == expect)
        print(f"  χ^{shape}((34)) = {val_at_1}  expected {expect}  {'✓' if match else '✗'}")
    w.add_data("sanity_check_at_q1", {
        str(shape): {"got": str(sp.limit(chi, Q, 1)), "expected": expected[shape]}
        for shape, chi in chis.items()
    })

    # Half-symmetric projection π_HS = (1/4) · Σ_λ χ^λ(β)
    pi_HS = sp.Rational(1, 4) * sum(chis[shape] for shape in shapes)
    pi_HS = sp.cancel(pi_HS)
    print(f"\nπ_HS(β_stab) = (1/4) Σ_λ χ^λ:")
    print(f"  = {pi_HS}")
    w.add_data("pi_HS_borromean_stab_symbolic", str(pi_HS))

    pi_HS_at_1 = sp.limit(pi_HS, Q, 1)
    print(f"\nπ_HS|_{{q=1}} = {pi_HS_at_1}  (target: 5/2)")
    w.add_data("pi_HS_at_q1", str(pi_HS_at_1))

    # Expand π_HS in ε = q-1
    eps = sp.Symbol("eps", real=True)
    pi_HS_eps = pi_HS.subs(Q, 1 + eps)
    pi_HS_eps_series = sp.series(pi_HS_eps, eps, 0, 10).removeO()
    print(f"\nπ_HS|_{{q=1+ε}} (Taylor in ε):")
    sp.pprint(sp.simplify(pi_HS_eps_series))

    # Convert to h-series
    h_sym = sp.Symbol("h_sym", real=True)
    eps_of_h = sp.solve(2*eps + eps**2 - h_sym*(1 + eps), eps)[1]
    eps_of_h_series = sp.series(eps_of_h, h_sym, 0, 10).removeO()
    pi_HS_h = pi_HS_eps_series.subs(eps, eps_of_h_series)
    pi_HS_h_series = sp.series(pi_HS_h, h_sym, 0, 10).removeO()
    pi_HS_h_series_s = sp.simplify(pi_HS_h_series)
    print(f"\nπ_HS as h-series (up to h^9):")
    sp.pprint(pi_HS_h_series_s)
    w.add_data("pi_HS_h_expansion", str(pi_HS_h_series_s))

    # Extract coefficients
    h0 = pi_HS_h_series_s.coeff(h_sym, 0)
    h2 = pi_HS_h_series_s.coeff(h_sym, 2)
    h4 = pi_HS_h_series_s.coeff(h_sym, 4)
    h6 = pi_HS_h_series_s.coeff(h_sym, 6)
    print(f"\nπ_HS h-coefficients:")
    print(f"  h^0: {h0}  (target: 5/2)")
    print(f"  h^2: {h2}  (target: -G ≈ -0.9160)")
    print(f"  h^4: {h4}  (would be -c_4 ≈ -0.00691)")
    print(f"  h^6: {h6}")
    w.add_data("h_coefficients", {
        "h0": str(h0), "h2": str(h2), "h4": str(h4), "h6": str(h6),
    })

    # Numerical comparison at q_0
    Q0 = float(Q_NUM)
    h0_num = float(h0) if h0.is_number else float(h0.subs(Q, Q0))
    h2_num = float(h2) if h2.is_number else float(h2.subs(Q, Q0))
    h4_num = float(h4) if h4.is_number else float(h4.subs(Q, Q0))
    print(f"\nNumerical at q_0:")
    print(f"  h^0 coefficient: {h0_num}")
    print(f"  h^2 coefficient: {h2_num} (vs -G = {-float(G_NUM):.10f})")
    print(f"  h^4 coefficient: {h4_num}")

    pi_HS_at_q0 = float(pi_HS.subs(Q, Q0))
    print(f"\nπ_HS(β_stab)|_{{q_0}} = {pi_HS_at_q0}")
    print(f"λ_p_target            = {float(LAM_P_TARGET)}")
    print(f"difference            = {pi_HS_at_q0 - float(LAM_P_TARGET):.6e}")
    w.add_data("pi_HS_at_q0_numeric", pi_HS_at_q0)
    w.add_data("lambda_p_target_numeric", float(LAM_P_TARGET))

    # Status
    h0_match = (h0_num == 2.5) or abs(h0_num - 2.5) < 1e-10
    h2_match_minus_G = abs(h2_num - (-float(G_NUM))) < 0.01

    w.add_data("conjecture_validation", {
        "h0_equals_5_over_2": bool(h0_match),
        "h2_equals_minus_G_within_1pct": bool(h2_match_minus_G),
        "h4_value_at_q0": h4_num,
        "interpretation": (
            "If h0=5/2 AND h2=-G validate, the conjecture is structurally "
            "verified and h4 gives c_4 in closed q-rational form (extends "
            "automatically to all higher c_2k via the same series)."
        ),
    })

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
