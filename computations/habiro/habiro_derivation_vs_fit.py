#!/usr/bin/env python3
"""Symbolic derivation: exact bridge(q) as rational function.

The bridge = hab_A(u) × denom(u) / hab_B(u) is a RATIONAL function of
u = √q. We compute it exactly in SymPy, then extract the Taylor
coefficients of bridge(q) / Plancherel(q) to see if the correction
factors 29/30, −1/30, 1/1260 emerge algebraically.

Key question: is S = bridge / (Plancherel × Vol/ℏ²) a clean rational
function of ℏ², or does it inherently involve Vol(4₁)?
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
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

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR, Q_MP, vol_4_1_at  # noqa: E402
except ImportError:
    from qou_substrate.constants import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402


def main():
    _t0 = time.perf_counter()

    u = sp.Symbol('u', positive=True)
    q = u**2

    # ---------------------------------------------------------------
    # Exact Habiro coefficients a_m(u) ∈ ℤ[u]
    # ---------------------------------------------------------------
    a_m_list = [
        sp.Integer(4),
        -74*u - 74,
        340*u**2 + 365*u + 389,
        -711*u**3 - 789*u**2 - 872*u - 959,
        788*u**4 + 901*u**3 + 1029*u**2 + 1172*u + 1328,
        -466*u**5 - 559*u**4 - 660*u**3 - 781*u**2 - 918*u - 1078,
        133*u**6 + 167*u**5 + 212*u**4 + 264*u**3 + 328*u**2 + 402*u + 494,
        -12*u**7 - 17*u**6 - 24*u**5 - 34*u**4 - 48*u**3 - 63*u**2 - 84*u - 110,
        u**4 + 2*u**3 + 3*u**2 + 5*u + 7,
    ]

    # ---------------------------------------------------------------
    # Compute hab_A = Σ a_m(u) · (q;q)_m = Σ a_m(u) · Π_{k=1}^m (1-q^k)
    # and   hab_B = Σ a_m(u) · (u;u)_m = Σ a_m(u) · Π_{k=1}^m (1-u^k)
    # as exact polynomials in u.
    # ---------------------------------------------------------------
    print("Computing exact polynomials hab_A(u) and hab_B(u)...")

    hab_A = sp.Integer(0)
    hab_B = sp.Integer(0)

    for m, a_m in enumerate(a_m_list):
        # (q;q)_m = Π_{k=1}^m (1 - u^{2k})
        poch_A = sp.Integer(1)
        for k in range(1, m + 1):
            poch_A *= (1 - u**(2*k))

        # (u;u)_m = Π_{k=1}^m (1 - u^k)
        poch_B = sp.Integer(1)
        for k in range(1, m + 1):
            poch_B *= (1 - u**k)

        hab_A += sp.expand(a_m * poch_A)
        hab_B += sp.expand(a_m * poch_B)

    hab_A = sp.expand(hab_A)
    hab_B = sp.expand(hab_B)

    # denom = 4u²¹ + 4u¹⁹ = 4u¹⁹(u² + 1)
    denom = 4*u**21 + 4*u**19

    print(f"  deg(hab_A) = {sp.degree(hab_A, u)}")
    print(f"  deg(hab_B) = {sp.degree(hab_B, u)}")
    print(f"  deg(denom) = {sp.degree(denom, u)}")
    print()

    # tr_M = hab_B / denom (this should = p(u)/denom from the witness)
    # bridge = hab_A / tr_M = hab_A × denom / hab_B

    # ---------------------------------------------------------------
    # The bridge ratio: hab_A / hab_B (rational function of u)
    # ---------------------------------------------------------------
    # bridge_unnorm = hab_A / hab_B = <Π(1+u^k)>_Hab
    # This should be a polynomial (not a rational function!) because
    # (q;q)_m = (u;u)_m × Π(1+u^k), so each term's ratio is Π(1+u^k).

    # Actually: hab_A = Σ a_m · (u;u)_m · Π(1+u^k)
    # This is NOT hab_B × (single polynomial) because different m values
    # have different Π(1+u^k) products. So hab_A / hab_B is genuinely
    # a rational function.

    # Build as a single fraction. sp.together (not sp.cancel — P15) is
    # enough here: hab_A and hab_B are already expanded polynomials, so
    # the reported degrees are pre-cancellation upper bounds. Numerical
    # evaluation via .subs is exact regardless of cancellation.
    print("Computing bridge ratio hab_A/hab_B...")
    ratio_sym = sp.together(hab_A / hab_B)
    numer, denom_ratio = sp.fraction(ratio_sym)
    print(f"  Ratio = P(u)/Q(u)  (pre-cancellation degrees)")
    print(f"  deg(P) = {sp.degree(numer, u)}")
    print(f"  deg(Q) = {sp.degree(denom_ratio, u)}")
    print()

    # ---------------------------------------------------------------
    # Evaluate at q₀ to get numerical bridge
    # ---------------------------------------------------------------
    set_compute_dps()
    q0 = Q_MP
    u0 = mp.sqrt(q0)
    vol = vol_4_1_at(mp.mp.dps)
    hbar_q = (q0 - 1) / q0
    eps = hbar_q**2
    n = 9

    bridge_num = float(ratio_sym.subs(u, float(u0)))
    print(f"  Bridge at q₀: {bridge_num:.10f}")
    print(f"  Expected: 5.616... (= hab_A/hab_B)")
    print()

    # The FULL bridge including denom:
    # full_bridge = hab_A × denom / hab_B = bridge × denom
    full_bridge_sym = sp.together(hab_A * (4*u**21 + 4*u**19) / hab_B)
    full_bridge_num = float(full_bridge_sym.subs(u, float(u0)))
    print(f"  Full bridge (×denom) at q₀: {full_bridge_num:.10f}")
    print(f"  Expected: 127.73")
    print()

    # ---------------------------------------------------------------
    # Plancherel = n!/[n]_q! as exact rational function of u
    # [k]_q = (q^k - q^{-k})/(q - q^{-1}) = (u^{2k} - u^{-2k})/(u^2 - u^{-2})
    # ---------------------------------------------------------------
    def q_int_sym(k):
        return (u**(2*k) - u**(-2*k)) / (u**2 - u**(-2))

    qfact_sym = sp.Integer(1)
    for k in range(1, n + 1):
        qfact_sym *= q_int_sym(k)

    plancherel_sym = sp.factorial(n) / qfact_sym

    # Simplify: multiply through by u^{appropriate power} to clear denominators
    # [k]_q = (u^{2k} - u^{-2k})/(u² - u^{-2})
    # Numerator of [k]_q × u^{2k} = u^{4k} - 1
    # Denominator of [k]_q × u² = u⁴ - 1
    # This gets messy. Let's just evaluate numerically.

    plancherel_num = float(plancherel_sym.subs(u, float(u0)))
    print(f"  Plancherel n!/[n]_q! at q₀: {plancherel_num:.10f}")
    print(f"  Expected: 0.6119...")
    print()

    # ---------------------------------------------------------------
    # R(q) = full_bridge / Plancherel = Vol/ℏ² × S
    # ---------------------------------------------------------------
    R_num = full_bridge_num / plancherel_num
    vol_over_hsq = float(vol / eps)
    S_num = R_num / vol_over_hsq

    print(f"  R = full_bridge / Plancherel = {R_num:.10f}")
    print(f"  Vol/ℏ² = {vol_over_hsq:.10f}")
    print(f"  S = R / (Vol/ℏ²) = {S_num:.15f}")
    print()

    # ---------------------------------------------------------------
    # Key test: is R(q) / (q²/(q-1)²) = Vol × S(q) a clean function?
    # R × ℏ² = R × (q-1)²/q² = Vol × S
    # So S = R × (q-1)² / (q² × Vol)
    # ---------------------------------------------------------------
    # R is algebraic, (q-1)²/q² is algebraic, Vol is transcendental.
    # So S = (algebraic) / Vol is inherently transcendental.
    # The coefficients 29/30 and 1/1260 encode Vol's value at q₀.

    R_times_hsq = R_num * float(eps)
    print(f"  R × ℏ² = {R_times_hsq:.15f}")
    print(f"  Vol(4₁) = {float(vol):.15f}")
    print(f"  R × ℏ² / Vol = S = {R_times_hsq / float(vol):.15f}")
    print()

    # ---------------------------------------------------------------
    # HOWEVER: the Markov trace identity says m_μ/m_e = Vol/ℏ².
    # So Vol/ℏ² is FIXED by CAL-2 to be the muon-electron mass ratio
    # (CODATA; carried via the registry, not hard-coded here).
    # The correction S is then:
    #   S = R(q₀) / (m_μ/m_e)
    # where R(q₀) is the algebraic bridge/Plancherel evaluated at q₀.
    # q₀ itself is determined by Vol/ℏ² = m_μ/m_e.
    #
    # So the question becomes: is S a clean function of the RATIO
    # Vol/ℏ² (i.e., of m_μ/m_e) rather than of Vol and ℏ² separately?
    # ---------------------------------------------------------------

    # Let's try a different decomposition. Define:
    #   R_alg(q) = full_bridge(q) / Plancherel(q)  [algebraic in q]
    #   μ = Vol/ℏ²(q)  [the muon ratio, also determines q via CAL-2]
    # Then S = R_alg / μ.
    #
    # If R_alg has a Taylor expansion R_alg = μ·(1 + c₂ε + c₄ε² + ...)
    # then S = 1 + c₂ε + c₄ε² + ... and the c_k are determined by
    # the Taylor expansion of R_alg(q) divided by Vol/ℏ²(q).
    #
    # Since both R_alg and ℏ² are algebraic in q, R_alg × ℏ² is algebraic.
    # And R_alg × ℏ² = Vol × S. So Vol × S(q) is an algebraic function of q.
    # The Taylor coefficients of Vol × S are rational in q.

    # Compute R_alg × ℏ² = full_bridge × ℏ² / Plancherel exactly.
    # ℏ² = (q-1)²/q² = (u²-1)²/u⁴

    hsq_sym = (u**2 - 1)**2 / u**4
    R_hsq_sym = sp.together(full_bridge_sym * hsq_sym / plancherel_sym)
    R_hsq_numer, R_hsq_denom = sp.fraction(R_hsq_sym)

    print("  R_alg × ℏ² = algebraic function of u (pre-cancellation degrees)")
    print(f"  deg(numer) = {sp.degree(R_hsq_numer, u)}")
    print(f"  deg(denom) = {sp.degree(R_hsq_denom, u)}")

    R_hsq_at_q0 = float(R_hsq_sym.subs(u, float(u0)))
    print(f"  R_alg × ℏ² at q₀ = {R_hsq_at_q0:.15f}")
    print(f"  Vol(4₁) = {float(vol):.15f}")
    print(f"  R_alg × ℏ² / Vol = S = {R_hsq_at_q0 / float(vol):.15f}")
    print()

    # ---------------------------------------------------------------
    # The correction S(q) = R_alg(q) × ℏ²(q) / Vol
    # The Taylor coefficients of S in ℏ² are:
    #   S = 1 + c₂ε + c₄ε² + ...  where ε = ℏ²
    # This means: R_alg × ε / Vol = 1 + c₂ε + ...
    # Or: R_alg / Vol = 1/ε + c₂ + c₄ε + ...
    # Or: R_alg = (Vol/ε)(1 + c₂ε + c₄ε² + ...)
    #           = Vol/ε + c₂·Vol + c₄·Vol·ε + ...
    #
    # Since R_alg is algebraic and Vol is transcendental,
    # the only way for R_alg to equal Vol × (series in ε) is if
    # Vol appears as a factor of R_alg. But R_alg is a rational
    # function of q — it CANNOT contain Vol.
    #
    # CONCLUSION: S is NOT a clean algebraic correction.
    # The "correction" absorbs the mismatch between the algebraic
    # bridge and the transcendental Vol(4₁)/ℏ². The coefficients
    # 29/30 and 1/1260 are NUMERICAL artifacts of evaluating at q₀,
    # not algebraic identities.
    # ---------------------------------------------------------------

    print("=" * 70)
    print("  CONCLUSION")
    print("=" * 70)
    print()
    print("  R_alg(q) = bridge(q)/Plancherel(q) is ALGEBRAIC in q.")
    print("  Vol(4₁)/ℏ² is TRANSCENDENTAL (Bloch-Wigner dilog).")
    print("  S = R_alg / (Vol/ℏ²) inherits transcendental dependence.")
    print()
    print("  The coefficients c₂=29/30 and c₃=1/1260 are NUMERICAL")
    print("  artifacts of evaluating at q₀ ≈ 1.10998, not algebraic")
    print("  identities. They CANNOT be derived from representation")
    print("  theory alone — they encode the specific value of Vol(4₁).")
    print()
    print("  WHAT IS DERIVED:")
    print("  1. The Pochhammer factorisation (1-q^k) = (1-u^k)(1+u^k)")
    print("  2. The bridge = ⟨Π(1+u^k)⟩_Hab (exact weighted average)")
    print("  3. R_alg(q) as an exact rational function of q")
    print()
    print("  WHAT IS FITTED:")
    print("  4. S = R_alg / (Vol/ℏ²) ≈ (1+ε)(1-ε/30)(1+ε/1260)")
    print("  5. The coefficients 29/30, -1/30, 1/1260")
    print()

    elapsed = time.perf_counter() - _t0

    w = WitnessBuilder("habiro-derivation-vs-fit-analysis", engine="sympy",
                       start_time=_t0)
    w.set_description(
        "Symbolic analysis of Habiro correction: the bridge R_alg(q) is "
        "algebraic but S = R_alg/(Vol/ℏ²) is transcendental. The third-"
        "factor coefficient is fitted: tightest numerical fit 1/1256, "
        "structural near-match 1/1260 = 1/(C(9,4)·10). Neither is derived."
    )
    w.set_audit_only("docs/audits/2026-05-28-habiro-product-correction-7ppm.md")
    w.add_data("R_alg_deg_numer", int(sp.degree(R_hsq_numer, u)))
    w.add_data("R_alg_deg_denom", int(sp.degree(R_hsq_denom, u)))
    w.add_data("derived", ["Pochhammer factorisation", "bridge = ⟨Π(1+u^k)⟩", "R_alg(q) exact"])
    w.add_data("fitted", ["S correction", "c₂=29/30", "c₃ tightest=1/1256", "c₃ structural=1/1260"])
    w.add_data("reason", "Vol(4₁) is transcendental; S = R_alg/(Vol/ℏ²) inherits it")

    # Was `computed=1, expected=1` (bean `qou-26f2`) — the same literal on both
    # sides, so it recorded `passed:true` whatever `R_hsq_sym` turned out to be.
    # This analysis's whole conclusion is the CONTRAST between an algebraic
    # R_alg and a transcendental Vol(4₁), so "R_alg is algebraic" is its
    # load-bearing half, and it is directly checkable two ways.
    #
    # (1) STRUCTURAL. Numerator and denominator must each be a polynomial in u
    #     with rational coefficients and no other free symbol. A Vol, a π or a
    #     dilogarithm leaking in through `full_bridge_sym` or `plancherel_sym`
    #     shows up here and nowhere else in this script.
    _parts = {"numer": R_hsq_numer, "denom": R_hsq_denom}
    algebraic_parts = sum(
        1 for e in _parts.values()
        if e.is_polynomial(u) and e.free_symbols <= {u}
        and all(c.is_Rational for c in sp.Poly(e, u).coeffs())
    )
    w.add_assertion(
        "R_alg_numer_and_denom_are_rational_polynomials_in_u",
        computed=str(algebraic_parts),
        expected=str(len(_parts)),
        tolerance=0,
        unit="of {numerator, denominator} polynomial in u over ℚ",
        source=("R_alg × ℏ² = together(bridge · ℏ² / Plancherel); degrees "
                f"{int(sp.degree(R_hsq_numer, u))} / "
                f"{int(sp.degree(R_hsq_denom, u))}. Free symbols must be {{u}} "
                "alone and every coefficient rational."),
    )
    # (2) INDEPENDENT ROUTE — a rational function over ℚ maps ℚ into ℚ. Evaluate
    #     the ratio itself (not its parts) at a rational u and check the value
    #     is an exact Rational. That goes through substitution and cancellation
    #     rather than sympy's polynomial predicates, so it still fails on a
    #     transcendental factor that `is_polynomial` happened to accept.
    _u_test = sp.Rational(1, 2)
    _val = sp.cancel(R_hsq_sym.subs(u, _u_test))
    w.add_data("R_alg_hsq_at_u_one_half", str(_val))
    w.add_assertion(
        "R_alg_is_rational_valued_at_rational_u",
        computed=str(int(bool(_val.is_Rational))),
        expected="1",
        tolerance=0,
        unit="1 if R_alg×ℏ² at u = 1/2 is an exact rational",
        source=("an algebraic function with rational coefficients maps ℚ → ℚ; "
                "Vol(4₁)/ℏ², the transcendental half of the contrast this "
                "analysis draws, does not. Value recorded in data."),
    )

    print(f"  Elapsed: {elapsed:.1f}s")
    print(f"  Witness: {w.save()}")


if __name__ == "__main__":
    main()
