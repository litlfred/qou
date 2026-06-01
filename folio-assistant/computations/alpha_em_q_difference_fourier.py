#!/usr/bin/env python3
"""alpha_em_q_difference_fourier.py — apply the Q_β q-difference /
root-of-unity / Fourier machinery (PRs #1593/#1602/#1622) to the α_EM
Habiro element [2]_q·(1−h²α), to expose its exact modular structure and
sharpen the α_EM next-order accuracy.

WHY THIS PROBE (highest-confidence transfer of the q-difference view).

PR #1511 (merged) established that the α_EM next-order factor is the
HABIRO ELEMENT
    H(q,α) = [2]_q · (1 − h²α) = (q + q⁻¹)·(1 − (q−q⁻¹)²·α),
whose Taylor coefficients in h = q−q⁻¹ are exact rationals linear in α
(alpha_em_habiro_taylor_investigation.py). But that script did the
TAYLOR analysis only — it never applied the q-difference / Fourier /
root-of-unity machinery that PRs #1593/#1602/#1622 developed for Q_β.

This probe applies that machinery to H, exactly. Two structural
advantages over Q_β make α_EM a cleaner test:
  • [2]_q = q + q⁻¹ is MANIFESTLY bar-symmetric (q↦q⁻¹ invariant), so H
    is PURELY bar-even — the charge-conjugation-symmetric (physical)
    sector PR #1602 said f must live in. No bar-even extraction needed.
  • H is a Laurent POLYNOMIAL (no denominator), so it has NO poles —
    contrast Q_β's Δtr_M which had a genuine pole at ζ_4. H's
    root-of-unity spectrum is finite and exact.

WHAT THIS PROBE COMPUTES (exact symbolic; no fitting):

  1. The root-of-unity spectrum H(ζ_d), ζ_d = e^{2πi/d}, as exact
     complex numbers (rectangular form), for d = 1..8. These are the
     Fourier modes of the q-difference shift σ_q acting on H.
  2. The special values: H(ζ_1) = 2 (classical α/(4π) leading term),
     H(ζ_2) = −2 (bar mode), H(ζ_4) = 0 (a ZERO — vs Q_β's pole).
  3. The exact Taylor coefficients c_k(α) in the ladder variable h
     (re-deriving the known recursion c_k = c_k^{[2]_q} − α·c_{k−2}^{[2]_q})
     and the q₀ truncation error — to confirm the q-difference view
     reproduces the established α_EM result.
  4. The bar-symmetry check: H is exactly bar-even (witness assertion).

DISCIPLINE (CLAUDE.md §7b, ck-tiered-not-binary): exact symbolic; no
fit; characterization of the α_EM Habiro element's q-difference
structure. The α_EM next-order DERIVED FORM is still open (per the
alpha-em ledger); this probe sharpens its modular target, it does not
close it. NOTE on h: here h = q−q⁻¹ is the α_EM Taylor basis (the
Hecke differential), distinct from both Habiro u=q^{1/2} and ladder
u_ladder=b·ℏ² (notation-collisions.md).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import sympy as sp
import mpmath as mp
from mpmath import mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "70")
os.environ.setdefault("QOU_OUTPUT_DPS", "60")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(70)
mp.mp.dps = 70

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "alpha-em-q-difference-fourier",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Apply the Q_β q-difference / root-of-unity / Fourier machinery "
        "(PRs #1593/#1602/#1622) to the α_EM Habiro element H = [2]_q·"
        "(1−h²α) = (q+q⁻¹)(1−(q−q⁻¹)²α). Computes the exact root-of-unity "
        "spectrum H(ζ_d) (the Fourier modes of σ_q), the special values "
        "H(ζ_1)=2 (classical α/4π), H(ζ_2)=−2 (bar mode), H(ζ_4)=0 (a "
        "ZERO — vs Q_β's pole), confirms H is exactly bar-even (purely "
        "the charge-conjugation-symmetric sector PR #1602 requires), and "
        "reproduces the established h-Taylor recursion + q₀ truncation. "
        "Exact symbolic; sharpens the α_EM modular target, no closure of "
        "the open derived form."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    print("=" * 78)
    print(" α_EM q-DIFFERENCE FOURIER — Habiro element [2]_q·(1−h²α)")
    print("=" * 78)
    print()

    q = sp.Symbol("q", positive=True)
    alpha = sp.Symbol("alpha", real=True, positive=True)
    h = q - 1 / q
    H = (q + 1 / q) * (1 - h ** 2 * alpha)
    print(f"  H(q,α) = [2]_q·(1−h²α) = {sp.expand(H)}")
    print()

    # ── 1. bar-symmetry: H is exactly bar-even ─────────────────────
    H_bar = sp.cancel(H.subs(q, 1 / q))
    is_bar_even = sp.simplify(H_bar - H) == 0
    print(f"  BAR-SYMMETRY: H(1/q) − H(q) = {sp.simplify(H_bar - H)}  "
          f"→ bar-even (physical) = {is_bar_even}")
    print(f"    (contrast Q_β's Δtr_M, which mixed bar-even/odd; H is "
          f"PURELY bar-even —\n     the sector PR #1602 said f must live in.)")
    print()

    # ── 2. root-of-unity spectrum (Fourier modes of σ_q) ───────────
    def roots_eval(expr, d):
        z = sp.exp(sp.I * 2 * sp.pi / d)
        val = expr.subs(q, z)
        # rectangular complex simplification
        val = sp.simplify(sp.expand_complex(sp.simplify(val)))
        return val
    print("  ROOT-OF-UNITY SPECTRUM H(ζ_d) (Fourier modes of σ_q):")
    spectrum = []
    for d in range(1, 9):
        val = roots_eval(H, d)
        # numeric (at α = CODATA) for a clean readout
        al_cod = sp.Rational("1", "137") * 0 + sp.nsimplify(
            mpf("1") / mpf("137.035999084"), rational=True)
        valn = complex(sp.N(val.subs(alpha, al_cod), 30))
        spectrum.append({
            "d": d, "H_symbolic": str(val),
            "H_at_alpha_codata": f"{valn.real:.8f}{valn.imag:+.8f}j",
        })
        print(f"    ζ_{d}:  H = {val}")
    print()

    # ── 3. special values ──────────────────────────────────────────
    H_z1 = roots_eval(H, 1)
    H_z2 = roots_eval(H, 2)
    H_z4 = roots_eval(H, 4)
    print("  SPECIAL VALUES (the q-difference fixed points):")
    print(f"    H(ζ_1) = H(q=1)  = {H_z1}   (classical → α/(4π) leading)")
    print(f"    H(ζ_2) = H(q=−1) = {H_z2}   (bar / charge-conj mode)")
    print(f"    H(ζ_4) = H(q=i)  = {H_z4}   (ZERO — α_EM's modular node;")
    print(f"                                  Q_β had a POLE at ζ_4)")
    print()

    # ── 4. h-Taylor coefficients (reproduce established recursion) ─
    hsym = sp.Symbol("h")
    bra2_h = sp.sqrt(4 + hsym ** 2)            # [2]_q = √(4+h²)
    H_h = bra2_h * (1 - hsym ** 2 * alpha)
    H_h_series = sp.series(H_h, hsym, 0, 9).removeO()
    ck = {n: sp.simplify(sp.expand(H_h_series).coeff(hsym, n))
          for n in [0, 2, 4, 6, 8]}
    print("  h-TAYLOR COEFFICIENTS c_k(α) (ladder basis h = q−q⁻¹):")
    for n in [0, 2, 4, 6, 8]:
        print(f"    c_{n}(α) = {ck[n]}")
    recursion_ok = sp.simplify(
        ck[2] - (sp.Rational(1, 4) - 2 * alpha)) == 0
    print(f"    recursion c_2 = 1/4 − 2α holds: {recursion_ok}")
    print()

    # ── 5. q₀ truncation accuracy ──────────────────────────────────
    q0 = mpf(Q_50_DIGIT_STR)
    h0 = q0 - 1 / q0
    al_cod = mpf("1") / mpf("137.035999084")
    H_exact = (q0 + 1 / q0) * (1 - h0 ** 2 * al_cod)
    H_trunc = mpf(0)
    for n in [0, 2, 4, 6, 8]:
        c = ck[n].subs(alpha, sp.nsimplify(al_cod, rational=True))
        c_num = mpf(int(c.p)) / mpf(int(c.q)) if c.is_Rational else mpf(str(c))
        H_trunc += c_num * h0 ** n
    trunc_err = abs(H_exact - H_trunc) / abs(H_exact)
    print(f"  q₀ TRUNCATION (k≤8): exact H = {mp.nstr(H_exact,16)}, "
          f"trunc = {mp.nstr(H_trunc,16)}")
    print(f"    relative truncation error = {mp.nstr(trunc_err,4)} "
          f"(each rung buys ~{float(-mp.log10(h0**2)):.1f} digits)")
    print()

    print("=" * 78)
    print(" FINDING (α_EM q-difference — exact; sharpens the modular target)")
    print("=" * 78)
    print(f"""
  • The α_EM Habiro element H = [2]_q·(1−h²α) is PURELY bar-even
    (q↦q⁻¹ invariant) — it already lives entirely in the charge-
    conjugation-symmetric sector PR #1602 said the Q_β scaling map f
    must occupy. α_EM is the "clean" case; Q_β is the same machinery
    with a bar-odd contamination to cancel.

  • Root-of-unity spectrum (exact): H(ζ_1)=2 (classical α/4π leading),
    H(ζ_2)=−2 (bar mode), H(ζ_4)=0. The ζ_4 ZERO is the structural
    counterpart of Q_β's ζ_4 POLE — α_EM's modular node vs Q_β's
    modular singularity. Same q-difference machinery, dual special
    value.

  • H is a Laurent polynomial (no poles) → its q-difference structure
    is finite and exact; the h-Taylor recursion c_k = c_k^{{[2]_q}} −
    α·c_{{k−2}}^{{[2]_q}} is the mode generator, q₀-stable (the c_k are
    α-linear rationals, not q₀-dependent near-matches like Q_β's).

  • OPEN (unchanged): the α_EM next-order DERIVED form is still open
    (alpha-em ledger). This probe sharpens its modular target — any
    derivation of H must reproduce the H(ζ_4)=0 node and the bar-even
    structure — but does not close it. No fitted form.
    """)

    builder.add_data("habiro_element", {
        "H": "[2]_q·(1−h²α) = (q+q⁻¹)(1−(q−q⁻¹)²α)",
        "h_basis": "h = q − q⁻¹ (Hecke differential; distinct from Habiro "
                   "u=q^{1/2} and ladder u_ladder=b·ℏ²)",
        "is_bar_even_exact": bool(is_bar_even),
    })
    builder.add_data("root_of_unity_spectrum", spectrum)
    builder.add_data("special_values", {
        "H_zeta1": str(H_z1), "H_zeta2": str(H_z2), "H_zeta4": str(H_z4),
        "zeta4_is_zero": bool(sp.simplify(H_z4) == 0),
        "contrast_with_qbeta": ("α_EM has a ZERO at ζ_4; Q_β had a POLE "
                                "at ζ_4 (PR #1622) — dual modular nodes"),
    })
    builder.add_data("h_taylor_coefficients", {
        f"c_{n}": str(ck[n]) for n in [0, 2, 4, 6, 8]})
    builder.add_data("q0_truncation", {
        "exact": mp.nstr(H_exact, 20),
        "truncated_k8": mp.nstr(H_trunc, 20),
        "relative_error": mp.nstr(trunc_err, 8),
    })
    builder.add_data("interpretation", {
        "alpha_em_is_clean_bar_even_case": True,
        "qbeta_is_same_machinery_with_bar_odd_to_cancel": True,
        "open": "α_EM next-order derived form (alpha-em ledger) — modular "
                "target sharpened (H(ζ_4)=0 node), not closed",
        "no_fitted_form_proposed": True,
    })
    builder.add_assertion(
        "alpha_em_habiro_is_exactly_bar_even",
        computed=1.0 if is_bar_even else 0.0,
        expected=1.0,
        tolerance=0.0,
        source=("H = [2]_q·(1−h²α) satisfies H(1/q) = H(q) exactly — it is "
                "purely bar-even (charge-conjugation-symmetric), the sector "
                "PR #1602 requires of the Q_β scaling map f."),
    )
    builder.add_assertion(
        "alpha_em_habiro_zero_at_zeta4",
        computed=1.0 if sp.simplify(H_z4) == 0 else 0.0,
        expected=1.0,
        tolerance=0.0,
        source=("H(ζ_4) = H(q=i) = 0 exactly — α_EM's modular node, the "
                "dual of Q_β's ζ_4 pole (PR #1622)."),
    )
    builder.save()
    print("\n  Witness: alpha-em-q-difference-fourier.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
