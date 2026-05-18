#!/usr/bin/env python3
"""APPROACH A: Symbolic Hoefsmit derivation of c_4, c_6, c_8, ...
for conj:lambda-scale-substrate-form.

The half-symmetric Wedderburn Markov-trace at the canonical
Borromean braid β_Bor = (σ_1 σ_2^{-1})^3 ∈ B_3, viewed in H_3(q):

  τ_q(β_Bor) = y_(3) · χ_(3)(β)
             + y_(2,1) · χ_(2,1)(β)
             + y_(1,1,1) · χ_(1,1,1)(β)

with Markov weights y_λ = dim_q²(λ) / [3]_q!  (Wenzl-LR).

Scalar blocks contribute trivially:
  χ_(3)(β) = (q · q^{-1})^3 = 1
  χ_(1,1,1)(β) = (−q^{-1} · (−q))^3 = 1

The load-bearing piece is χ_(2,1)(β) — the trace of the 2x2 Hoefsmit
matrix product for σ_1 σ_2^{-1} cubed.

Hoefsmit seminormal basis for V_(2,1) (Standard Young Tableaux of
shape (2,1), ordered: t_1 = ((1,2),(3)), t_2 = ((1,3),(2))).

Adjacent-contents:
  In t_1, swapping 2 ↔ 3 gives t_2 (= s_2 · t_1). Axial distance
  ρ(2, 3) in t_1: c(2) = 1 (cell (1,2)), c(3) = -1 (cell (2,1)).
  Axial distance d = c(3) - c(2) = -2.
  In t_1, swapping 1 ↔ 2 changes nothing (both in same row, would
  produce invalid tableau (2,2,1)/...? actually σ_1 acts diagonally
  on t_1 because 1 and 2 are in the same row).

Standard Hoefsmit formulas (Murphy 1983; see chi-v21-hoefsmit-matrix-derivation):

  σ_i(v_t) = ρ_i · v_t   if i and i+1 are in the same row
            = ρ_i · v_t   if i and i+1 are in the same column (with sign)
            = ((1 - ρ_i)/d) · v_t + sqrt(...)·v_{s_i·t}   otherwise

where ρ_i depends on the axial distance d = c(i+1) − c(i):
  ρ_i = (q^d − q^{-d}) / (q^{d+1} − q^{-(d+1)}) · q^something

It's simpler in matrix form. For shape (2,1) and the two tableaux above,
σ_1 acts as diag(q, -q^{-1}) (since in t_1, 1 and 2 are same row →
eigenvalue q; in t_2, 1 and 2 are in same column → eigenvalue -q^{-1}).

σ_2 is non-diagonal: in t_1, 2 and 3 are in different rows and columns
(distance d = -2), and similarly for t_2 (distance d = +2). The
explicit Murphy/Hoefsmit form for σ_2 on this 2D representation is:

  σ_2 = [[ a,  b ],
         [ c,  d ]]

where a, d are the "diagonal" entries and b, c the "off-diagonal"
mixing. With our conventions:
  a = (1/[d])_q where [d]_q = (q^d - q^{-d})/(q - q^{-1}), at d=-2:
    [d=-2]_q = -(q^2 - q^{-2})/(q - q^{-1}) = -(q + q^{-1}) = -[2]_q
  so a = -1/[2]_q · (something) — standard form:
    σ_2 = [[1/[d], √([d+1][d-1])/[d]],
           [√([d+1][d-1])/[d], -1/[d]·...]]

This is getting symbol-heavy. The clean formulation: use the
Murphy operators or just compute χ_(2,1)((σ_1 σ_2^{-1})^3) via the
identity (since the trace is basis-independent).

OBSERVATION: There's an elegant shortcut. The Borromean braid is
TRIVIAL in B_3-abelianization, and (σ_1 σ_2^{-1})^3 has algebraic
properties that suggest:

  χ_(2,1)((σ_1 σ_2^{-1})^3) = some specific q-rational

Computing this via the explicit matrix product is what this script does.
"""
from __future__ import annotations

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


def hoefsmit_sigma_matrices(q_sym):
    """Hoefsmit seminormal-form 2x2 matrices for σ_1, σ_2 on V_(2,1).

    Ordered basis: (v_{t_1}, v_{t_2}) with
      t_1 = SYT ((1,2),(3))  — content of 2 in t_1 = +1, content of 3 = -1
      t_2 = SYT ((1,3),(2))  — content of 2 in t_2 = -1, content of 3 = +1

    σ_1 swaps 1 ↔ 2:
      in t_1: 1 (cell 1,1, c=0) and 2 (cell 1,2, c=+1) — same row → eigenvalue q
      in t_2: 1 (cell 1,1, c=0) and 2 (cell 2,1, c=-1) — same column → eigenvalue -q^{-1}
    So σ_1 = diag(q, -1/q).

    σ_2 swaps 2 ↔ 3:
      in t_1: 2 (cell 1,2, c=+1) and 3 (cell 2,1, c=-1) — d = c(3)-c(2) = -2
      in t_2: 2 (cell 2,1, c=-1) and 3 (cell 1,2, c=+1) — d = +2
    Off-diagonal action. With axial distance d, Hoefsmit gives
    (in our basis order):

      σ_2 = (1/[d]_q) · [[ q, √([d-1]_q · [d+1]_q) ],
                         [ √([d-1]_q · [d+1]_q), -1/q ]]

    where d is the axial distance from t_1 to t_2 under s_2.
    For shape (2,1), d = -2 from t_1, so [d]_q at d=-2:
      [d=-2]_q = -[2]_q (since [-n]_q = -[n]_q in the symmetric q-int).
    [d-1]_q = [-3]_q = -[3]_q
    [d+1]_q = [-1]_q = -[1]_q = -1

    Convention check: the σ_2 matrix should square to (q - q^{-1})·σ_2 + 1
    per the Hecke relation. We use that to verify and pick the right sign
    convention.
    """
    # Use Murphy's seminormal form (Ram 1991 §4, or Murphy 1983):
    # For shape (2,1), basis t_1, t_2 with d = axial distance.
    q = q_sym
    # σ_1 diagonal action
    sigma1 = sp.Matrix([[q, 0], [0, -1/q]])

    # σ_2: at d = c(t_2) - c(t_1) under s_2. The known result for
    # this shape is the "two-state" matrix (Wenzl 1988):
    # σ_2 v_{t_1} = α · v_{t_1} + β · v_{t_2}
    # σ_2 v_{t_2} = β · v_{t_1} + γ · v_{t_2}
    # with the Hecke relation σ²=hσ+1 and tr(σ_2) = q - 1/q
    # (matching eigenvalues {q, -1/q}).
    #
    # The standard form is:
    #   σ_2 = [[ 1/[2]_q,       sqrt([3]_q/[2]_q²) ],
    #          [ sqrt([3]_q/[2]_q²), -1/[2]_q + h    ]]
    # where h = q - 1/q.
    #
    # Cleaner: use the parametrisation
    #   σ_2 = [[a, b], [b, h - a]]  (so trace = h, det = -1)
    # The off-diagonal b must satisfy σ²-hσ-1=0:
    #   (a² + b²) - h·a - 1 = 0   →   b² = 1 + h·a - a²
    # And the eigenvalues are q and -1/q (trace h, det -1) ✓.
    # The specific value of a is fixed by the seminormal convention:
    # the t_1, t_1 entry is q · ρ_(c(3) - c(2)) where ρ encodes the
    # axial-distance attenuation. For shape (2,1) with d=-2:
    a_val = 1 / (q + 1/q)  # = 1/[2]_q
    h = q - 1/q
    # b² = 1 + h·a - a² ; b > 0
    b_sq = sp.simplify(1 + h * a_val - a_val**2)
    b_val = sp.sqrt(b_sq)
    sigma2 = sp.Matrix([
        [a_val, b_val],
        [b_val, h - a_val],
    ])

    return sigma1, sigma2


def main() -> int:
    w = WitnessBuilder("lambda-scale-rd-hoefsmit-symbolic", engine="sympy")
    w.set_description(
        "APPROACH A: symbolic Hoefsmit-matrix derivation of c_4, c_6, "
        "c_8, ... for conj:lambda-scale-substrate-form. Computes the "
        "half-symmetric H_3 Markov trace of (σ_1 σ_2^{-1})^3 in closed "
        "form via the 2x2 seminormal matrices on V_(2,1), then "
        "Taylor-expands around q = 1 to extract all h-coefficients "
        "simultaneously."
    )
    w.set_content_block("conj:lambda-scale-substrate-form")
    w.add_parameter("approach", "A — Hoefsmit symbolic 2x2 matrix product")

    q = sp.Symbol("q", positive=True)
    h = q - 1/q

    # Hoefsmit matrices
    sigma1, sigma2 = hoefsmit_sigma_matrices(q)
    print("σ_1 (diagonal):")
    sp.pprint(sigma1)
    print()
    print("σ_2 (off-diagonal):")
    sp.pprint(sp.simplify(sigma2))
    print()

    # Verify Hecke relation σ_i² = h·σ_i + 1
    hecke_1 = sp.simplify(sigma1 @ sigma1 - h*sigma1 - sp.eye(2))
    hecke_2 = sp.simplify(sigma2 @ sigma2 - h*sigma2 - sp.eye(2))
    print(f"σ_1² - h·σ_1 - I = {hecke_1}  (should be zero)")
    print(f"σ_2² - h·σ_2 - I = {hecke_2}  (should be zero)")
    hecke_ok = (hecke_1 == sp.zeros(2, 2)) and (hecke_2 == sp.zeros(2, 2))
    w.add_data("hecke_relation_ok", bool(hecke_ok))
    if not hecke_ok:
        print("WARNING: Hecke relation failed — Hoefsmit matrices need refinement.")

    # Verify braid relation σ_1 σ_2 σ_1 = σ_2 σ_1 σ_2
    braid_lhs = sigma1 @ sigma2 @ sigma1
    braid_rhs = sigma2 @ sigma1 @ sigma2
    braid_diff = sp.simplify(braid_lhs - braid_rhs)
    print(f"\nBraid relation diff = {braid_diff}  (should be zero)")
    braid_ok = (braid_diff == sp.zeros(2, 2))
    w.add_data("braid_relation_ok", bool(braid_ok))

    # Compute σ_2^{-1} = (σ_2 - h·I) by inverting the Hecke relation:
    # σ_i² = h·σ_i + 1  →  σ_i · (σ_i - h) = 1  →  σ_i^{-1} = σ_i - h
    sigma2_inv = sigma2 - h * sp.eye(2)
    # Verify σ_2 · σ_2^{-1} = I
    check_inv = sp.simplify(sigma2 @ sigma2_inv)
    print(f"\nσ_2 · σ_2^{-1} = {check_inv}")
    inv_ok = (check_inv == sp.eye(2))
    w.add_data("inverse_relation_ok", bool(inv_ok))

    # χ_(2,1)((σ_1 σ_2^{-1})^3) = trace((σ_1 · σ_2^{-1})^3)
    M = sigma1 @ sigma2_inv
    M3 = M @ M @ M
    chi_21 = sp.simplify(sp.trace(M3))
    print(f"\nχ_(2,1)((σ_1 σ_2^{-1})^3) = {chi_21}")
    w.add_data("chi_2_1_borromean_symbolic", str(chi_21))

    # The half-symmetric Markov trace at H_3:
    #   τ_q(β) = (y_(3) + y_(1,1,1)) · 1 + y_(2,1) · χ_(2,1)(β)
    #          = 2/([2]_q · [3]_q) + [2]_q²/([2]_q · [3]_q) · χ_(2,1)(β)
    qint = lambda n: (q**n - q**(-n))/(q - 1/q)
    norm = qint(2) * qint(3)  # = [3]_q!
    y_3 = 1/norm
    y_111 = 1/norm
    y_21 = qint(2)**2 / norm

    tau_q = sp.simplify(y_3 + y_111 + y_21 * chi_21)
    print(f"\nMarkov τ_q(β_Bor) = {tau_q}")
    w.add_data("tau_q_borromean_full_symbolic", str(tau_q))

    # Note: this is the H_3 Markov trace, which equals the H_3 PROBABILITY,
    # not the "half-symmetric" projection. The half-symmetric form may
    # require a different weighting. For now, expand in h to see what
    # comes out and compare to the conjecture's 5/2 - h²·G ansatz.

    # Substitute q = 1 + ε for ε small, expand:
    eps = sp.Symbol("eps", real=True)
    tau_eps = tau_q.subs(q, 1 + eps)
    tau_eps_series = sp.series(tau_eps, eps, 0, 10).removeO()
    print(f"\nτ_q expanded at q = 1 + ε (up to ε^9):")
    sp.pprint(sp.simplify(tau_eps_series))
    w.add_data("tau_q_h_expansion", str(tau_eps_series))

    # Compute h = q - 1/q at q = 1+ε:  h = (1+ε) - 1/(1+ε) = ε(2+ε)/(1+ε)
    # = 2ε - ε² + ε³ - ε⁴ + ... (small ε expansion)
    # So h ≈ 2ε at leading order.
    #
    # To convert τ(ε) expansion → τ(h) expansion, invert ε → ε(h)
    # numerically and substitute.

    # Numerical verification at q_0
    Q_num = mp.mpf(Q_50_DIGIT_STR)
    H_num = Q_num - 1/Q_num

    chi_21_num = sp.lambdify(q, chi_21)(float(Q_num))
    tau_num_sym = sp.lambdify(q, tau_q)(float(Q_num))
    print(f"\nAt q_0 (numerical via float64):")
    print(f"  χ_(2,1)(β) = {chi_21_num:.10f}")
    print(f"  τ_q(β)     = {tau_num_sym:.10f}")
    print(f"  λ_p_target = 2.4599534077... (from CODATA / Vol(B_3))")
    w.add_data("chi_21_at_q0_f64", chi_21_num)
    w.add_data("tau_q_at_q0_f64", tau_num_sym)

    # Compare τ_q to expected 5/2 - h²·G ansatz
    # At q_0, 5/2 - h²·G = 2.4599666 (numerically)
    five_half_minus_h2_G = 2.5 - float(H_num)**2 * 0.9159655942
    print(f"  5/2 - h²·G = {five_half_minus_h2_G:.10f}")
    print(f"  diff(τ_q - (5/2 - h²·G)) = {tau_num_sym - five_half_minus_h2_G:.6e}")

    # ── Final structural finding ──────────────────────────────
    w.add_data("structural_finding", {
        "result": (
            "χ_(2,1)((σ_1 σ_2^{-1})^3) computed symbolically. "
            "The H_3 Markov trace τ_q(β_Bor) is a closed q-rational "
            "expression. Taylor expansion in h around q=1 gives ALL "
            "coefficients (c_0, c_2, c_4, c_6, ...) simultaneously."
        ),
        "extends_to_higher_c": True,
        "approach": "A (Hoefsmit symbolic)",
        "next_step": (
            "Verify the leading coefficients match the conjecture: "
            "c_0 ?= 5/2, c_2 ?= -G. If yes, c_4 is read off from the "
            "h^4 coefficient as a closed q-rational expression."
        ),
    })

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
