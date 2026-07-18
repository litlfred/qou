#!/usr/bin/env python3
"""bring_hauptmodul_gate_probe.py — the Γ₀(5) hauptmodul gate t₅(τ₀) = −10.

Witness for uploaded-papers audit idea A2
(docs/audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md) and the Lean
arithmetic lock QOU/Archimedean/BringHauptmodulGate.lean.

Bring's modulus τ₀ is fixed by j(τ₀) = −121945/32, j(5τ₀) = −25/2
(Braden–Disney-Hogg arXiv:2208.13692 §2.2, BDH22; Braden–Northover SIGMA 8
(2012) 065 corrected labelling), and Riera–Rodríguez 1992 Thm 1 shows the
residual gauge on the modulus is Γ₀(5) — so the invariant coordinate is the
genus-0 hauptmodul t₅(τ) = (η(τ)/η(5τ))⁶ of X₀(5), tied to j by the classical
level-5 relation j = (t² + 250t + 3125)³ / t⁵.

This probe verifies, honestly and with no fit:

  (a) EXACT (sympy Rational): t = −10 is a root of
      (t² + 250t + 3125)³ + (121945/32)·t⁵ = 0
      (equivalently 32·(t² + 250t + 3125)³ + 121945·t⁵ = 0 over ℤ), and the
      Fricke companion 5³/(−10) = −25/2 = j(5τ₀).

  (b) NUMERIC (mpmath): the η-quotient t₅(τ₀) = (η(τ₀)/η(5τ₀))⁶ at BDH22's
      published τ₀ = −0.5 + 0.186676i lands on −10. τ₀ is printed to 6 d.p.
      only, so the achievable residual is set by the τ₀ truncation, NOT by
      compute precision: |dt₅/dτ| ≈ 43 at τ₀, and the truncation error in
      Im τ₀ is ≤ 5e-7, so the expected residual scale is ~1e-5..1e-4
      (observed ≈ 2e-5 in the sweep). Asserted at tolerance 1e-3; the residual
      is recorded in the witness. Cross-check: 1728·kleinj(τ₀) ≈ −121945/32
      at the same truncation-limited scale.

Nothing here is wired to production; audit-only witness (scope: coordination /
survey, tier of the parent audit).
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02). Keeps
# flat-namespace imports (`from witness_base import …`) working from the
# `probes/` cluster subdirectory. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from fractions import Fraction  # noqa: E402

from mpmath import mp, mpc, mpf, exp, pi, kleinj  # noqa: E402
from sympy import Integer, Rational  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def dedekind_eta(tau):
    """η(τ) = q^{1/24} ∏_{n≥1} (1 − qⁿ), q = e^{2πiτ}. Direct product — |q| < 1
    and the product converges geometrically; 400 terms is far beyond 50 dps for
    Im τ ≥ 0.18."""
    q = exp(2j * pi * tau)
    prod = mpc(1)
    for n in range(1, 401):
        prod *= 1 - q**n
    return exp(2j * pi * tau / 24) * prod


def main():
    set_compute_dps()
    wb = WitnessBuilder("bring-hauptmodul-gate-probe", engine="mpmath")

    # ── (a) exact arithmetic (sympy Rational — no floats) ──────────────────
    t = Integer(-10)
    j_tau0 = Rational(-121945, 32)
    sextic = (t**2 + 250 * t + 3125) ** 3 + Rational(121945, 32) * t**5
    sextic_int = 32 * (t**2 + 250 * t + 3125) ** 3 + 121945 * t**5
    fricke = Rational(5**3, 1) / t  # 125 / (−10)
    j_from_t = ((t**2 + 250 * t + 3125) ** 3) / t**5

    assert sextic == 0, f"sextic at t=-10 is {sextic}, not 0"
    assert sextic_int == 0, f"integer-cleared sextic at t=-10 is {sextic_int}, not 0"
    assert fricke == Rational(-25, 2), f"Fricke 5^3/t = {fricke} != -25/2"
    assert j_from_t == j_tau0, f"(t^2+250t+3125)^3/t^5 = {j_from_t} != -121945/32"

    # ── (b) numeric η-quotient at BDH22's published τ₀ (6 d.p.) ────────────
    tau0 = mpc(mpf("-0.5"), mpf("0.186676"))  # BDH22 §2.2 (6 d.p. print)
    t5 = (dedekind_eta(tau0) / dedekind_eta(5 * tau0)) ** 6
    resid = abs(t5 - (-10))
    # residual budget: |dt₅/dτ| ≈ 43 at τ₀ × ≤5e-7 truncation ⇒ ~1e-5..1e-4
    TOL = 1e-3
    assert resid < TOL, f"|t5(tau0) + 10| = {resid} >= {TOL}"
    assert abs(t5.imag) < TOL, f"Im t5(tau0) = {t5.imag} not ~0"

    # cross-check: j(τ₀) via Klein j (mpmath kleinj = j/1728)
    j_num = 1728 * kleinj(tau0)
    j_resid = abs(j_num - mpf(Fraction(-121945, 32).numerator) / 32)
    assert j_resid < 1.0, f"|j(tau0) + 121945/32| = {j_resid} too large"

    print("(a) EXACT: sextic(−10) = 0; 32-cleared = 0; 5³/(−10) = −25/2;"
          " (t²+250t+3125)³/t⁵|₋₁₀ = −121945/32  ✓")
    print(f"(b) NUMERIC at τ₀ = −0.5+0.186676i (6 d.p. BDH22):")
    print(f"    t₅(τ₀) = {mp.nstr(t5, 10)}   |t₅+10| = {mp.nstr(mpf(resid), 4)}"
          f"  (expected ~1e-5..1e-4 from 6-d.p. τ₀ truncation)")
    print(f"    1728·kleinj(τ₀) = {mp.nstr(j_num, 10)}  vs −121945/32 = −3810.78125"
          f"   |Δ| = {mp.nstr(mpf(j_resid), 4)}")

    # ── witness ────────────────────────────────────────────────────────────
    wb.set_description(
        "Γ₀(5) hauptmodul gate t₅(τ₀) = −10 for Bring's modulus (uploaded-papers "
        "audit idea A2). Exact: t = −10 is a root of (t²+250t+3125)³ + "
        "(121945/32)t⁵ (sympy Rational; equivalently 32·(…)³ + 121945·t⁵ = 0 "
        "over ℤ), with Fricke companion 5³/(−10) = −25/2 = j(5τ₀). Numeric: the "
        "η-quotient (η(τ₀)/η(5τ₀))⁶ at BDH22's 6-d.p. τ₀ = −0.5+0.186676i lands "
        "on −10 to the τ₀-truncation scale. Lean arithmetic lock: "
        "QOU/Archimedean/BringHauptmodulGate.lean. Gate framing: any q₀ ↦ τ "
        "dictionary is physical only through Γ₀(5)-invariants (RR92 Thm 1) and "
        "must land on the class t₅ = −10 — discrete pass/fail, no precision "
        "search. Audit-only; nothing wired."
    )
    wb.set_audit_only("docs/audits/2026-07-18-uploaded-papers-binding-mass-gap-ideas.md")
    wb.add_data("inputs", {
        "tau0": "-0.5 + 0.186676i (BDH22 §2.2, 6 d.p. print; transcendental)",
        "j_tau0_exact": "-121945/32",
        "j_5tau0_exact": "-25/2",
        "level5_modular_relation": "j = (t^2 + 250t + 3125)^3 / t^5,  t = (eta(tau)/eta(5tau))^6",
    })
    wb.add_data("numeric", {
        "t5_at_tau0": mp.nstr(t5, 12),
        "abs_residual_t5_plus_10": mp.nstr(mpf(resid), 6),
        "expected_residual_scale": "~1e-5..1e-4 (|dt5/dtau| ~ 43 x <=5e-7 tau0 truncation)",
        "j_via_kleinj": mp.nstr(j_num, 12),
        "abs_residual_j": mp.nstr(mpf(j_resid), 6),
    })
    wb.add_caveat(
        "tau0 itself is transcendental (Schneider); only its Γ₀(5)-invariants "
        "(t₅ = −10, the j-pair) are exact. The numeric leg is truncation-limited "
        "by the 6-d.p. published tau0, not by compute precision."
    )
    wb.add_assertion(
        "sextic_root_exact",
        computed=str(sextic),
        expected="0",
        tolerance=0,
        source="sympy Rational: (t²+250t+3125)³ + (121945/32)t⁵ at t = −10 "
               "(and 32-cleared integer form) — exact zero.",
    )
    wb.add_assertion(
        "fricke_companion_exact",
        computed=str(fricke),
        expected="-25/2",
        tolerance=0,
        source="5³/t₅(τ₀) = 125/(−10) = −25/2 = j(5τ₀) (BDH22 corrected labelling).",
    )
    wb.add_assertion(
        "eta_quotient_lands_on_minus_10",
        computed=float(resid),
        expected=0.0,
        tolerance=1e-3,
        source="|(η(τ₀)/η(5τ₀))⁶ + 10| at the 6-d.p. BDH22 τ₀; residual is "
               "τ₀-truncation-limited (~2e-5 observed).",
    )
    wb.save()
    print("witness saved; all assertions passed.")


if __name__ == "__main__":
    main()
