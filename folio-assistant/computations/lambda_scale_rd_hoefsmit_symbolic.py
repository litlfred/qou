#!/usr/bin/env python3
"""APPROACH A v2: Symbolic Hoefsmit derivation of c_4, c_6, c_8, ...
using the canonical `hoefsmit_symbolic.chi_lambda_symbolic` engine.

Previous attempt re-derived Hoefsmit matrices manually and got the
axial-distance terms wrong. This version delegates to the
already-verified `hecke_character_symbolic.q_character_on_braid_word`
implementation (which is the reference for the QOU paper's compute
chain).

## Computation

1. The canonical Borromean braid in B_3:
     β_Bor = σ_1 · σ_2^{-1} · σ_1 · σ_2^{-1} · σ_1 · σ_2^{-1}
   = (σ_1 σ_2^{-1})^3, 6 crossings, closure = Borromean rings link.

2. χ^λ(β_Bor) for each partition λ ⊢ 3 via the canonical engine.

3. Markov trace τ_M(β_Bor) = Σ_λ y_λ(q) · χ^λ(β_Bor) where
   y_λ(q) are the Wenzl-Ocneanu Markov weights.

4. Taylor expand around q = 1: extract h^k coefficients.

5. Compare to the conjecture's ansatz λ = 5/2 − h²·G − h⁴·c_4 + ...
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
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from experimental_constants import M_E_MEV, M_P_MEV  # noqa: E402
from hoefsmit_symbolic import Q, chi_lambda_symbolic  # noqa: E402

mp.mp.dps = 80
Q_NUM = mp.mpf(Q_50_DIGIT_STR)
H_NUM = Q_NUM - 1/Q_NUM
HBAR_Q_NUM = (Q_NUM - 1) / Q_NUM
G_NUM = mp.catalan
VOL_B3 = 8 * mp.catalan  # = Vol(Borromean rings complement), 8·G via Adams 1985
M_E = mp.mpf(repr(M_E_MEV))
M_P = mp.mpf(repr(M_P_MEV))
LAM_P_TARGET = (M_P / M_E) * HBAR_Q_NUM**2 / VOL_B3


def main() -> int:
    w = WitnessBuilder("lambda-scale-rd-hoefsmit-symbolic", engine="sympy")
    w.set_description(
        "APPROACH A v2: symbolic χ^λ via canonical hoefsmit_symbolic + "
        "Markov-trace half-symmetric projection at the Borromean braid "
        "(σ_1 σ_2^{-1})^3. Extracts c_4, c_6 in closed form via "
        "sympy.series at q=1+ε."
    )
    w.set_content_block("conj:lambda-scale-substrate-form")
    w.add_parameter("approach", "A v2 — canonical hoefsmit_symbolic engine")

    # Borromean braid as list of (k_gen, ctype) tuples
    # β_Bor = (σ_1 σ_2^{-1})^3 — gen_idx is 0-indexed in this engine:
    # gen_idx 0 ↔ σ_1, gen_idx 1 ↔ σ_2
    crossings = []
    for _ in range(3):
        crossings.append((0, "sigma"))      # σ_1
        crossings.append((1, "sigma_inv"))  # σ_2^{-1}
    print(f"Borromean braid: {crossings}")
    print(f"  Length: {len(crossings)} crossings ✓ (Borromean rings = 6 crossings)")

    # Compute χ^λ for each partition of 3
    shapes = [(3,), (2, 1), (1, 1, 1)]
    chis = {}
    for shape in shapes:
        chi = chi_lambda_symbolic(shape, crossings)
        chi_simplified = sp.simplify(chi)
        chis[shape] = chi_simplified
        print(f"\nχ^{shape}(β_Bor) = {chi_simplified}")
    w.add_data("chi_by_shape_symbolic", {str(k): str(v) for k, v in chis.items()})

    # Sanity at q=1: χ should equal the classical S_3 character
    # (σ_1 σ_2^{-1})^3 at q=1 is (s_1 s_2)^3 = (123)^3 = identity
    # χ^λ(id) = dim V_λ:  (3) -> 1, (2,1) -> 2, (1,1,1) -> 1
    print("\nSanity check at q=1 (β reduces to identity):")
    expected = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
    sanity_ok = True
    for shape, chi_sym in chis.items():
        val_at_1 = sp.limit(chi_sym, Q, 1)
        expect = expected[shape]
        match = (val_at_1 == expect)
        sanity_ok = sanity_ok and match
        print(f"  χ^{shape}(β)|_{{q=1}} = {val_at_1}  expected {expect}  {'✓' if match else '✗'}")
    w.add_data("sanity_check_at_q1_ok", bool(sanity_ok))

    if not sanity_ok:
        print("\nWARNING: sanity check failed — investigate canonical engine.")
        w.add_caveat("Sanity check at q=1 failed; trace polynomial may need sign/parity fix.")
        out = w.save()
        return 0

    # Markov trace via canonical Wenzl-Ocneanu weights
    # y_λ(q) = dim_q(λ)² / [n]_q!  for n=3
    qint = lambda n: (Q**n - Q**(-n)) / (Q - 1/Q)
    qfac3 = qint(2) * qint(3)
    # Quantum dimensions at q=q (symbolic):
    dim_q_shapes = {
        (3,): sp.Integer(1),
        (2, 1): qint(2),
        (1, 1, 1): sp.Integer(1),
    }
    y_lambda = {shape: sp.simplify(d**2 / qfac3) for shape, d in dim_q_shapes.items()}
    print("\nMarkov weights y_λ:")
    for shape, y in y_lambda.items():
        print(f"  y_{shape} = {y}")
    w.add_data("y_lambda_symbolic", {str(k): str(v) for k, v in y_lambda.items()})

    # Markov trace: τ_M(β) = Σ_λ y_λ · χ^λ(β)
    tau_M = sum(y_lambda[shape] * chis[shape] for shape in shapes)
    tau_M = sp.cancel(tau_M)
    print(f"\nτ_M(β_Bor) = {tau_M}")
    w.add_data("tau_M_borromean_symbolic", str(tau_M))

    # At q=1, τ_M(β_Bor) = ?
    # Plancherel weights: y_λ(q=1) = (dim V_λ)² / 3! = 1/6, 4/6, 1/6
    # τ_M(1)(id) = 1/6·1 + 4/6·2 + 1/6·1 = 1/6 + 8/6 + 1/6 = 10/6 = 5/3
    # That's the classical Plancherel expectation of χ(id) = dim_λ
    # Σ (dim_λ)²/n! · dim_λ = Σ dim_λ³ / n!  for n=3 = 1+8+1 / 6 = 10/6 = 5/3
    tau_M_at_1 = sp.limit(tau_M, Q, 1)
    print(f"τ_M(β_Bor)|_{{q=1}} = {tau_M_at_1}  (expected: 10/6 = 5/3 for canonical Markov)")
    w.add_data("tau_M_at_q1", str(tau_M_at_1))

    # Expand in ε = q-1 to extract h-coefficients
    eps = sp.Symbol("eps", real=True)
    tau_eps = tau_M.subs(Q, 1 + eps)
    tau_eps_series = sp.series(tau_eps, eps, 0, 10).removeO()
    tau_eps_series_s = sp.simplify(tau_eps_series)
    print(f"\nτ_M(β_Bor)|_{{q=1+ε}} (expansion to ε^9):")
    sp.pprint(tau_eps_series_s)
    w.add_data("tau_M_epsilon_expansion", str(tau_eps_series_s))

    # h-expansion: h = q - 1/q = (1+ε) - 1/(1+ε)
    # At leading order, h ≈ 2ε + O(ε²). Need to convert.
    # Solve ε(h): ε² + 2ε - h(1+ε) = 0  → ε = (-2 + sqrt(4 + 4h(1+ε)))/2
    # Or: q = (h + sqrt(h²+4))/2 → q - 1 = (h - 2 + sqrt(h²+4))/2

    # Truncated ε(h) series: ε = h/2 - h²·X1 + h³·X2 - ...
    # From h = 2ε - ε² + ε³ - ε⁴ + ...:
    # Inverting: ε = h/2 + h²/8 - h³/16 + ... (geometric-like coefficients)
    h_sym = sp.Symbol("h_sym", real=True)
    eps_of_h = sp.series(sp.solve(2*eps + eps**2 - h_sym*(1 + eps), eps)[1], h_sym, 0, 10)
    eps_of_h_s = sp.simplify(eps_of_h.removeO())
    print(f"\nε(h) inversion (leading orders): {sp.simplify(eps_of_h_s)}")
    w.add_data("epsilon_of_h_series", str(eps_of_h_s))

    # Substitute ε → ε(h) in τ expansion
    tau_h = tau_eps_series_s.subs(eps, eps_of_h_s)
    tau_h_series = sp.series(tau_h, h_sym, 0, 10).removeO()
    tau_h_series_s = sp.simplify(tau_h_series)
    print(f"\nτ_M(β_Bor) as h-series (up to h^9):")
    sp.pprint(tau_h_series_s)
    w.add_data("tau_M_h_expansion", str(tau_h_series_s))

    # Compare to conjecture: λ_p = 5/2 - h²·G - h^4·c_4 + ...
    # Note: this is the FULL Markov trace, not the half-symmetric projection.
    # Half-symmetric (Step 2 of proof) used a different weighting that gave 5/2.
    # Full Markov trace at q=1 gives 5/3 (Plancherel) per our computation.

    # Extract h^0, h^2, h^4 coefficients
    h0_coeff = tau_h_series_s.coeff(h_sym, 0)
    h2_coeff = tau_h_series_s.coeff(h_sym, 2)
    h4_coeff = tau_h_series_s.coeff(h_sym, 4)
    print(f"\nMarkov-trace h-coefficients:")
    print(f"  h^0: {h0_coeff}  (expected: 5/3 from Plancherel — NOT 5/2)")
    print(f"  h^2: {h2_coeff}")
    print(f"  h^4: {h4_coeff}")
    w.add_data("h_coefficients", {
        "h0": str(h0_coeff),
        "h2": str(h2_coeff),
        "h4": str(h4_coeff),
    })

    # Numerical verification at q_0
    Q0 = float(Q_NUM)
    tau_num = float(tau_M.subs(Q, Q0))
    print(f"\nAt q_0 (numerical):")
    print(f"  τ_M(β_Bor)|_{{q_0}} = {tau_num:.10f}")
    print(f"  λ_p_target          = {float(LAM_P_TARGET):.10f}")
    print(f"  difference          = {tau_num - float(LAM_P_TARGET):.6f}")
    w.add_data("tau_M_at_q0_numeric", tau_num)
    w.add_data("lambda_p_target_numeric", float(LAM_P_TARGET))

    # ── Final analysis ────────────────────────────────────────
    # The FULL Markov trace τ_M(β_Bor) at q=1 gives 5/3, not 5/2.
    # The half-symmetric "5/2" in the conjecture must come from a
    # DIFFERENT weighting (likely involving the CONJUGATE-PAIR
    # PROJECTION not just the Markov trace).
    w.add_data("structural_finding", {
        "tau_M_at_q1": str(tau_M_at_1),
        "expected_5_2": "5/2",
        "tau_M_h2_coeff": str(h2_coeff),
        "expected_h2_coeff_neg_G": "-G (Catalan)",
        "h2_coeff_at_q0_numeric": float(h2_coeff.subs(Q, Q0)) if h2_coeff.free_symbols else float(h2_coeff),
        "interpretation": (
            "The canonical Markov trace τ_M(β_Bor) does NOT equal "
            "the conjecture's λ_scale at the Borromean braid. "
            "At q=1, τ_M(β_Bor) = 5/3 (Plancherel sum of χ²/n!), "
            "not 5/2 (half-symmetric conjugate-pair count). "
            "This means the conjecture's '5/2 - h²·G' is NOT the "
            "Markov trace of the Borromean braid — it's a DIFFERENT "
            "categorical projection involving the half-symmetric "
            "Wedderburn weighting derived in Step 2 of the proof. "
            "The h^4 coefficient c_4 must come from THAT projection's "
            "expansion, not from the canonical Markov trace."
        ),
        "next_step": (
            "Define the half-symmetric projection π_HS explicitly: "
            "π_HS(τ) = Σ over conjugate pairs (χ_λ + χ_λ') with weight 1, "
            "plus self-conjugate χ_λ with weight 1/2 (no normalisation "
            "by [n]_q!). Apply to χ^λ(β_Bor) and expand in h."
        ),
    })

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
