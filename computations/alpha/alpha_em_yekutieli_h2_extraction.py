#!/usr/bin/env python3
"""
alpha_em_yekutieli_h2_extraction.py — derive α_EM at higher order via
the Yekutieli non-abelian-Stokes route on the FSC torus knots
T(2,9) + T(3,5). (Derive-or-refute; no AME fit.)

CONTEXT. The framework's α_EM⁻¹ = q·[9]_q·[10]_q (`prop:em-coupling-bring-
zero-mode`) is a simple q-bracket ansatz that lands at ~137.0 — about
500 ppm off CODATA 137.035999084. Per the canonical derivation chain
(C → Yekutieli non-abelian Stokes → Hecke → Markov trace), the exact
object is the Markov-trace product, with two key structural features:

  1. T(2,9) = σ₁⁹ in B₂ — single generator. CBH commutator [σ₁,σ₁] = 0,
     so the surface-Stokes h² correction VANISHES for T(2,9). Its
     Markov trace is exact at leading order.

  2. T(3,5) = (σ₁σ₂)⁵ in B₃ — two alternating generators, with the
     central-full-twist factorisation
        (σ₁σ₂)⁵ = Δ₃²·(σ₁σ₂)²  ,  Δ₃²|_λ = q^{c(λ)} I.
     On the standard rep (2,1), c=0 so Δ₃²=I, meaning (σ₁σ₂)³ = I on
     (2,1). Eigenvalues of (σ₁σ₂) on (2,1) are cube roots of unity
     (ω, ω̄ — INDEPENDENT of q), so χ_(2,1)((σ₁σ₂)⁵) = −1 EXACTLY at
     every q. This is a q-independent piece the simple [10]_q ANSATZ
     omits.

WHAT THIS PROBE DOES (derive-or-refute):

  A. Evaluate the framework's bare ansatz q·[9]_q·[10]_q at q₀ to full
     precision; compare to CODATA.

  B. Evaluate the canonical exact Markov-trace form:
       α_EM⁻¹_exact ∝ q · tr_M(T(2,9)) · tr_M(T(3,5))
     using Wenzl y_λ solved from the Markov axioms at H_2 / H_3 and the
     central-full-twist factorisation for T(3,5). Per the structural
     insight, T(3,5)'s contribution carries the q-independent (2,1)
     middle term that [10]_q omits.

  C. Report the residual against CODATA for both forms. Honest derive-
     or-refute — no tower fit, no Habiro extrapolation.

The Yekutieli h² extraction analog (CBH commutator) for T(2,9) is
trivially zero (single generator). For T(3,5), the h² content is
already captured by the exact Markov trace (which is a closed-form
rational function in q, exact at all orders).
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

import sys
from pathlib import Path

from mpmath import mp, mpf, sqrt, fabs

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


def main():
    set_compute_dps()
    wb = WitnessBuilder("alpha-em-yekutieli-h2-extraction", engine="mpmath")

    q = Q_MP
    h = q - 1 / q
    qbra = lambda n: (q**n - q**(-n)) / (q - q**(-1))  # noqa: E731
    z = q**3 / (q**2 + 1)                    # Markov z parameter

    CODATA_alpha_inv = mpf("137.035999084")            # CODATA 2018

    print("=" * 72)
    print(" α_EM⁻¹ via canonical T(2,9) + T(3,5) Markov-trace product")
    print("=" * 72)
    print(f"  q₀ = {float(q):.10f}   h = {float(h):.6f}   z = {float(z):.6f}")
    print(f"  CODATA α⁻¹ = {float(CODATA_alpha_inv):.9f}\n")

    # ─── A. Framework's bare ansatz ──────────────────────────────────────
    bra9 = qbra(9)
    bra10 = qbra(10)
    alpha_inv_ansatz = q * bra9 * bra10
    err_ansatz = (alpha_inv_ansatz - CODATA_alpha_inv) / CODATA_alpha_inv
    print("[A] Bare ansatz  α⁻¹ = q·[9]_q·[10]_q")
    print(f"    [9]_q = {float(bra9):.6f}   [10]_q = {float(bra10):.6f}")
    print(f"    α⁻¹ = {float(alpha_inv_ansatz):.6f}    "
          f"residual = {float(err_ansatz) * 1e6:+.1f} ppm")

    # ─── B. Canonical exact Markov-trace form ────────────────────────────
    # H₂(q) Wenzl y from Markov axioms:
    #   y_(2) + y_(1,1) = z              [tr_M(1, H₂) = z]
    #   q·y_(2) − q⁻¹·y_(1,1) = z        [tr_M(σ₁, H₂) = z]
    y_H2_triv = z * (q + 1) / (q**2 + 1)
    y_H2_sign = z * q * (q - 1) / (q**2 + 1)

    # T(2,9) = σ₁⁹ in H₂:  tr_M(σ₁⁹) = y_(2)·q⁹ + y_(1,1)·(−q⁻¹)⁹
    #                                 = y_(2)·q⁹ − y_(1,1)·q⁻⁹    (9 odd)
    trM_T29 = y_H2_triv * q**9 - y_H2_sign * q**(-9)

    # H₃(q) Wenzl y from Markov axioms on {1, σ₁, σ₁σ₂}:
    #   (I)    y_(3) + 2·y_(21) + y_(111) = z²                  [tr_M(1)]
    #   (II)   q·y_(3) + h·y_(21) − q⁻¹·y_(111) = z²            [tr_M(σ₁)]
    #   (III)  q²·y_(3) − y_(21) + q⁻²·y_(111) = z²             [tr_M(σ₁σ₂)]
    # χ_(2,1)(σ₁σ₂) = −1 (q-indep): on (2,1), (σ₁σ₂)³ = Δ₃² acts as 1 because
    # content sum c(2,1) = 0, so eigenvalues of σ₁σ₂ are non-trivial cube
    # roots of unity ω,ω², whose sum is −1. (h-row was a length-2 mis-derivation.)
    from mpmath import matrix, lu_solve
    A = matrix([
        [1, 2, 1],
        [q, h, -1 / q],
        [q**2, -1, 1 / q**2],
    ])
    b = matrix([z**2, z**2, z**2])
    y = lu_solve(A, b)
    y_H3_triv, y_H3_std, y_H3_sign = y[0], y[1], y[2]

    print(f"\n    Wenzl y(H₂):   y_(2) = {float(y_H2_triv):.6f}   "
          f"y_(1,1) = {float(y_H2_sign):.6f}")
    print(f"    Wenzl y(H₃):   y_(3) = {float(y_H3_triv):.6f}   "
          f"y_(2,1) = {float(y_H3_std):.6f}   "
          f"y_(1,1,1) = {float(y_H3_sign):.6f}")

    # T(3,5) = (σ₁σ₂)⁵ in H₃, length 10 (= |Δ₃²|=6 + |(σ₁σ₂)²|=4):
    #   χ_(3)((σ₁σ₂)⁵)     = q⁶ · q⁴ = q¹⁰    (trivial: each σ→q, 10 generators)
    #   χ_(2,1)((σ₁σ₂)⁵)   = 1·(−1) = −1      (cube-root-of-unity; q-INDEP)
    #   χ_(1,1,1)((σ₁σ₂)⁵) = q⁻⁶·q⁻⁴ = q⁻¹⁰   (sign: each σ→−q⁻¹, (−)¹⁰=+1)
    trM_T35 = y_H3_triv * q**10 + y_H3_std * (-1) + y_H3_sign * q**(-10)

    print(f"\n[B] Canonical exact Markov traces")
    print(f"    tr_M(T(2,9)) = {float(trM_T29):.6f}     "
          f"(vs [9]_q = {float(bra9):.6f})")
    print(f"    tr_M(T(3,5)) = {float(trM_T35):.6f}     "
          f"(vs [10]_q = {float(bra10):.6f})")

    # The framework formula is q · [factor for T29] · [factor for T35].
    # To compare apples-to-apples we evaluate the exact product:
    alpha_inv_exact = q * trM_T29 * trM_T35
    err_exact = (alpha_inv_exact - CODATA_alpha_inv) / CODATA_alpha_inv
    print(f"    q · tr_M(T29) · tr_M(T35) = {float(alpha_inv_exact):.6f}    "
          f"residual = {float(err_exact) * 1e6:+.1f} ppm")

    # ─── C. Comparison and Yekutieli h² status ───────────────────────────
    print("\n[C] Comparison vs CODATA  (α⁻¹ = 137.035 999 084)")
    print(f"    Bare ansatz       : {float(err_ansatz) * 1e6:+.1f} ppm")
    print(f"    Exact Markov prod : {float(err_exact) * 1e6:+.1f} ppm")
    print()
    print("Yekutieli h² extraction status:")
    print("  • T(2,9) = σ₁⁹: single generator → [σ₁,σ₁] = 0, "
          "CBH h² VANISHES (zero contribution).")
    print("  • T(3,5) = (σ₁σ₂)⁵: alternating two-generator. The CBH h² "
          "content is already INSIDE the closed-form tr_M(T(3,5)) above —")
    print("    Hecke traces are exact at all orders in h, so there is no")
    print("    separate h^k tower to extract beyond the closed-form trace.")
    print()
    print("Honest read:")
    if abs(err_exact) < abs(err_ansatz) * 0.5:
        print("  ✓ Exact Markov product closes more of the gap than the bare")
        print("    ansatz — the (2,1) cube-root-of-unity term is the missing")
        print("    structural piece.")
    elif abs(err_exact) > abs(err_ansatz):
        print("  ✗ Exact Markov product is FURTHER from CODATA than the bare")
        print("    ansatz — meaning q·[n]_q·[n+1]_q is a different identification")
        print("    of α_EM (not the bare trace product), and the residual")
        print("    is structural to the [n]_q-ansatz itself, not to a missing")
        print("    h² correction. Closing 500 ppm needs a different layer")
        print("    (Habiro at root of unity, or a re-identification of the")
        print("    α_EM categorical object).")
    else:
        print("  ≈ Exact Markov product and bare ansatz agree at the residual")
        print("    level — the (2,1) middle term is a small perturbation.")

    # ── Witness ──────────────────────────────────────────────────────────
    wb.set_description(
        "Derive-or-refute: does the exact Markov-trace product for the FSC "
        "torus knots T(2,9) and T(3,5) close the ~500 ppm α_EM residual "
        "left by the bare q·[9]_q·[10]_q ansatz? Yekutieli h² extraction: "
        "T(2,9) vanishes (single generator); T(3,5)'s h² content is already "
        "in the closed-form Markov trace via central-full-twist factorisation "
        "(Δ₃² = I on (2,1), eigenvalues of σ₁σ₂ are cube roots of unity → "
        "χ_(2,1)((σ₁σ₂)⁵) = −1 EXACTLY, independent of q). No fit; no fitting."
    )
    wb.add_data("inputs", {
        "q0": mp.nstr(q, 30),
        "CODATA_alpha_inv": "137.035999084",
    })
    wb.add_data("bare_ansatz", {
        "formula": "q · [9]_q · [10]_q",
        "value": mp.nstr(alpha_inv_ansatz, 12),
        "residual_ppm": float(err_ansatz * 1e6),
    })
    wb.add_data("canonical_exact", {
        "formula": "q · tr_M(T(2,9), Wenzl-H₂) · tr_M(T(3,5), Wenzl-H₃)",
        "trM_T29": mp.nstr(trM_T29, 12),
        "trM_T35": mp.nstr(trM_T35, 12),
        "value": mp.nstr(alpha_inv_exact, 12),
        "residual_ppm": float(err_exact * 1e6),
    })
    wb.add_data("yekutieli_h2_status", {
        "T29": "vanishes (single generator, [σ₁,σ₁]=0)",
        "T35": "captured by closed-form Markov trace; the (2,1) "
               "cube-root-of-unity contribution is the q-independent piece",
        "structural_insight": "Δ₃²|_(2,1) = I ⇒ (σ₁σ₂)³|_(2,1) = I ⇒ "
                              "χ_(2,1)((σ₁σ₂)⁵) = ω+ω̄ = −1 ∀q",
    })
    wb.add_assertion(
        "framework_ansatz_residual_pinned",
        computed=round(float(err_ansatz * 1e6), 1),
        expected=-1552.7,
        tolerance=2.0,
        source="Bare q·[9]_q·[10]_q at full precision (q₀=1.10998…) lands at "
               "α⁻¹=136.8232, residual −1552.7 ppm vs CODATA 137.035999084. "
               "Yekutieli h² extraction does NOT close this: T(2,9) vanishes, "
               "T(3,5) is already exact in the closed-form Markov trace, and "
               "the Markov-trace product itself is ~10⁶ ppm off — so the "
               "[n]_q ansatz is NOT the bare Markov trace, and the residual "
               "is structural to the [n]_q identification, not a missing "
               "h² term.",
    )
    wb.save()


if __name__ == "__main__":
    main()
