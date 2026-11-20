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

LEVEL DISCIPLINE (AGENTS.md "Im(q) at fibre vs observable level"): the
Habiro element H(q,α) lives at the FIBRE / categorical level (pre-τ,
formal q), where Im is UNCONSTRAINED and the operative symmetry is the
bar INVOLUTION q↦q⁻¹ — NOT a reality assumption. q and α are kept formal
throughout the spectrum; the observable component is real ONLY at the
final archimedean q₀ evaluation. Forcing q or α real at the fibre level
would conflate the two levels (a registered audit flag).

This probe applies that machinery to H, exactly. Two structural
advantages over Q_β make α_EM a cleaner test:
  • [2]_q = q + q⁻¹ is a FIXED POINT of the bar involution (q↦q⁻¹
    invariant), so H is a bar fixed point — the clean charge-
    conjugation-symmetric sector PR #1602 said f must live in. (Q_β's
    Δtr_M is NOT a bar fixed point; it carries a bar-anti-invariant
    part to cancel.) This is an involution statement, not a reality one.
  • H is a Laurent POLYNOMIAL (no denominator), so it has NO poles —
    contrast Q_β's Δtr_M which had a genuine pole at ζ_4. H's
    root-of-unity spectrum is finite and exact.

WHAT THIS PROBE COMPUTES (exact symbolic; α FORMAL; no fitting):

  1. The root-of-unity spectrum H(ζ_d), ζ_d = e^{2πi/d}, exact in the
     cyclotomic field ℚ(ζ_d) with α a formal (Im-unconstrained) fibre
     parameter, for d = 1..8. These are the Fourier modes of σ_q on H.
  2. The special values: H(ζ_1) = 2 (classical α/(4π) leading term),
     H(ζ_2) = −2 (bar mode), H(ζ_4) = 0 (a ZERO — vs Q_β's pole).
  3. The exact Taylor coefficients c_k(α) in the ladder variable h
     (re-deriving the known recursion c_k = c_k^{[2]_q} − α·c_{k−2}^{[2]_q})
     and the q₀ truncation error — at the archimedean level, where the
     observable is real — confirming the established α_EM result.
  4. The bar-INVOLUTION check: H is exactly a bar fixed point (witness
     assertion), over the formal fibre variable (no reality assumed).

DISCIPLINE (AGENTS.md §7b, ck-tiered-not-binary): exact symbolic; no
fit; characterization of the α_EM Habiro element's q-difference
structure. The α_EM next-order DERIVED FORM is still open (per the
alpha-em ledger); this probe sharpens its modular target, it does not
close it. NOTE on h: here h = q−q⁻¹ is the α_EM Taylor basis (the
Hecke differential), distinct from both the spinor rate
\check{q}=q^{1/2} (= Habiro "u" in the literature) and the ladder
u_ladder=b·ℏ² (notation-collisions.md §\check{q}, §u).
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
import time
from pathlib import Path

import sympy as sp
import mpmath as mp
from mpmath import mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "70")
os.environ.setdefault("QOU_OUTPUT_DPS", "60")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(70)
mp.mp.dps = 70

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


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
        "ZERO — vs Q_β's pole), confirms H is a fixed point of the bar "
        "involution q↦q⁻¹ over the FORMAL fibre variable (the charge-"
        "conjugation-symmetric sector PR #1602 requires; not a reality "
        "assumption — reality enters only at the archimedean q₀ step), "
        "and reproduces the established h-Taylor recursion + q₀ truncation. "
        "Exact symbolic; sharpens the α_EM modular target, no closure of "
        "the open derived form."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    print("=" * 78)
    print(" α_EM q-DIFFERENCE FOURIER — Habiro element [2]_q·(1−h²α)")
    print("=" * 78)
    print()

    # FIBRE-LEVEL symbols: NO reality assumption. Per AGENTS.md "Im(q) at
    # fibre vs observable level", the Habiro element H(q,α) lives at the
    # fibre/categorical level (pre-τ, formal q), where Im is UNCONSTRAINED
    # and the relevant structure is the bar INVOLUTION q↦q⁻¹ — not a
    # reality constraint. The observable component is real ONLY at the
    # final archimedean (q₀) evaluation, applied there explicitly. Forcing
    # α real here would conflate the two levels (a registered audit flag).
    q = sp.Symbol("q")           # formal fibre variable, Im unconstrained
    alpha = sp.Symbol("alpha")   # fibre parameter, Im unconstrained
    h = q - 1 / q
    H = (q + 1 / q) * (1 - h ** 2 * alpha)
    print(f"  H(q,α) = [2]_q·(1−h²α) = {sp.expand(H)}")
    print()

    # ── 1. bar INVOLUTION: H is a fixed point (the structural object) ─
    # The relevant fibre-level structure is the bar INVOLUTION q↦q⁻¹ (the
    # framework/tower involution), NOT a reality assumption. H being a
    # fixed point of bar is an exact algebraic statement over the formal
    # (Im-unconstrained) fibre variable q — it holds whether or not q,α
    # are later evaluated to real archimedean values.
    H_bar = sp.cancel(H.subs(q, 1 / q))
    is_bar_fixed = sp.simplify(H_bar - H) == 0
    print(f"  BAR INVOLUTION (q↦q⁻¹): H(1/q) − H(q) = "
          f"{sp.simplify(H_bar - H)}  → fixed point = {is_bar_fixed}")
    print(f"    (the framework/tower involution structure; NOT a reality")
    print(f"     constraint. Contrast Q_β's Δtr_M, which was NOT a bar")
    print(f"     fixed point — it mixed bar-even/odd. H is the clean case.)")
    print()

    # ── 2. root-of-unity spectrum (Fourier modes of σ_q) ───────────
    # α is kept FORMAL (Im unconstrained) at the fibre level: the spectrum
    # is exact in the cyclotomic field ℚ(ζ_d), with α-coefficients that
    # are cyclotomic elements. Reality of the observable component is
    # imposed ONLY at the archimedean q₀ evaluation (§5), never here.
    def roots_eval(expr, d):
        z = sp.exp(sp.I * 2 * sp.pi / d)
        # collect in α (formal); simplify only the cyclotomic coefficients
        return sp.collect(sp.simplify(sp.expand(expr.subs(q, z))), alpha)
    print("  ROOT-OF-UNITY SPECTRUM H(ζ_d) (Fourier modes of σ_q; α FORMAL,")
    print("  exact in the cyclotomic field ℚ(ζ_d) — no reality imposed):")
    spectrum = []
    for d in range(1, 9):
        val = roots_eval(H, d)
        spectrum.append({"d": d, "H_symbolic_cyclotomic": str(val)})
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

    # ── 5. ARCHIMEDEAN (q₀) evaluation — reality imposed HERE ONLY ─
    # This is the observable level (post-τ functor): q₀ is real
    # (Im(q₀)=0, verified `lusztig_q_0_imaginary_part_zero`) and α is the
    # real CODATA fine-structure constant. The reality constraint belongs
    # to this archimedean step, NOT to the fibre-level spectrum above.
    q0 = Q_MP          # real archimedean substrate value
    h0 = q0 - 1 / q0
    al_cod = mpf("1") / mpf("137.035999084")   # real observable α
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
  • The α_EM Habiro element H = [2]_q·(1−h²α) is a FIXED POINT of the
    bar involution q↦q⁻¹ (the framework/tower involution structure) —
    an exact algebraic fact over the FORMAL fibre variable, with NO
    reality assumed. This is the clean charge-conjugation-symmetric
    sector PR #1602 said the Q_β scaling map f must occupy. α_EM is the
    "clean" case (a bar fixed point); Q_β's Δtr_M is NOT a bar fixed
    point — it carries a bar-anti-invariant part to be cancelled.

  • Root-of-unity spectrum (exact, α formal, in the cyclotomic field):
    H(ζ_1)=2 (classical α/4π leading), H(ζ_2)=−2, H(ζ_4)=0. The ζ_4
    ZERO is the structural counterpart of Q_β's ζ_4 POLE — dual modular
    nodes of the same q-difference machinery. The α-coefficients are
    cyclotomic elements (e.g. ζ_8 carries √2, ζ_5 carries √5).

  • LEVEL DISCIPLINE (per AGENTS.md Im(q) fibre-vs-observable): the
    spectrum lives at the FIBRE level (q,α formal, Im unconstrained;
    the involution q↦q⁻¹ is the operative symmetry). The observable
    component is real ONLY at the archimedean q₀ evaluation — where the
    h-recursion c_k = c_k^{{[2]_q}} − α·c_{{k−2}}^{{[2]_q}} gives the real
    α-linear rationals (q₀-stable, NOT the Q_β near-match flip-flop).

  • OPEN (unchanged): the α_EM next-order DERIVED form is still open
    (alpha-em ledger). This probe sharpens its modular target — any
    derivation of H must reproduce the H(ζ_4)=0 node and the bar-
    involution fixed-point structure — but does not close it. No fit.
    """)

    builder.add_data("habiro_element", {
        "H": "[2]_q·(1−h²α) = (q+q⁻¹)(1−(q−q⁻¹)²α)",
        "h_basis": "h = q − q⁻¹ (Hecke differential; distinct from Habiro "
                   "u=q^{1/2} and ladder u_ladder=b·ℏ²)",
        "is_bar_involution_fixed_point": bool(is_bar_fixed),
        "level_note": ("fibre-level: q,α formal (Im unconstrained), bar "
                       "involution q↦q⁻¹ is the structural object; reality "
                       "of observable component imposed ONLY at archimedean "
                       "q₀ evaluation. Per AGENTS.md Im(q) fibre-vs-observable."),
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
        "alpha_em_habiro_is_bar_involution_fixed_point",
        computed=1.0 if is_bar_fixed else 0.0,
        expected=1.0,
        tolerance=0.0,
        source=("H = [2]_q·(1−h²α) satisfies H(1/q) = H(q) exactly over the "
                "FORMAL fibre variable (no reality assumed) — it is a fixed "
                "point of the bar involution q↦q⁻¹ (the framework/tower "
                "involution structure). This is the clean charge-conjugation "
                "sector PR #1602 requires; reality enters only at q₀."),
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
