"""qbeta-ladder-phase-from-wedderburn-weights — what `α` is, against the real weights.

Bean `qou-q2oa` (parent `qou-cdx1`, tranche `qou-cds1`).

## The object

`α = (z − 1)·h/2`, `h = q − q⁻¹`, is the N=1 rung's cosine argument in the
Q_β precision ladder (`qbeta_d_frame_ladder_structure_probe.cos_arg` returns
`α − u/2`) and, per that probe's assertion A1, the ONLY place a Markov-trace
convention enters the entire ladder.  `QOU.QBeta.phaseTwice z h = (z−1)*h`
carries it in Lean.

## What was retracted

PR #5187 read `α = −h/4 − (h/2)·y₍₂,₁₎` off the instance `(z, 1/2−z, z)`.
That instance satisfies only the normalisation and fails the other two Markov
conditions (PR #5185), so `1/2 − z` is not `y₍₂,₁₎`.  The relation was a
change of variable off a false identity: setting `y₍₂,₁₎ := 1/2 − z` gives
`z = 1/2 − y₍₂,₁₎` and substituting into `(z−1)h/2` returns exactly
`−h/4 − (h/2)y₍₂,₁₎`.  Check A0 below reproduces that algebra so the
provenance of the retracted formula is on the record, not folklore.

## What this probe establishes

A1  The corpus's own D-frame weights are the two-variable Schur measure:
    `y_λ = s_λ(1,Q)/(1+Q)^n`, `Q = q²`, zero for `ℓ(λ) > 2`.  Checked
    against `schur_principal_mpmath.y_lambda_at_q0_mpmath` (the LIVE closed
    form — never the muon-serving cache) for n = 2..9.

A2  `2·χ_λ(σ₁) − h·f^λ = [2]_q·χ^λ(τ)` for every λ, where `χ^λ(τ)` is the
    ORDINARY S_n character at a transposition.  Exact over ℚ(q).  This is
    where the bar-odd `h` cancels: σ₁ has eigenvalues `q` (mult m₊) and
    `−q⁻¹` (mult m₋) on V_λ, so `χ_λ(σ₁) = q·m₊ − q⁻¹·m₋` and the
    combination collapses to `[2]_q·(m₊ − m₋) = [2]_q·χ^λ(τ)`.

A3  Hence, from the Markov conditions alone (ANY convention):
        2z − h = [2]_q · Ξ_n,      Ξ_n := Σ_λ χ^λ(τ)·y_λ.
    and therefore, via `phaseTwice_projected_eq_loopMean`,
        α = (h/4)·( [2]_q·Ξ_n + h − 2 ).

A4  `Ξ_n = (1+Q²)/(1+Q)²` — INDEPENDENT OF n.  Frobenius: `Σ_λ χ^λ(μ)s_λ =
    p_μ`, and a transposition is `μ = (2,1^{n−2})`, so the numerator is
    `p_2(1,Q)·p_1(1,Q)^{n−2} = (1+Q²)(1+Q)^{n−2}` against the normaliser
    `(1+Q)^n`.  Verified exactly for n = 2..9.

A5  **`α` is NOT a function of the weights.**  Structural exclusion with a
    named proved invariant (bar-parity), not a numerical near-miss:
    every D-frame weight is bar-EVEN (`markovWeightsD_y21_barEven`,
    `markovWeightsD_y3_barEven`), so any function of the weights is bar-even;
    but `α + bar α = h²/2` with `α ≠ h²/4`, so `α` is not.  The witness that
    `α ≠ h²/4` is `2z_D − h − 2 ≠ 0`, i.e. `q⁴ − 2q³ − 2q + 1 ≠ 0`.

A6  The affine-in-`y₍₂,₁₎` SHAPE does not survive.  With `y₍₃₎ = 1 − 2y₍₂,₁₎`
    at n=3 the phase reads `α = (h/4)([2]_q + h − 2) − (h[2]_q/2)·y₍₂,₁₎`,
    which looks affine — but `y₍₂,₁₎ = 1/[2]_q²` exactly, so `[2]_q =
    y₍₂,₁₎^{−1/2}` and the "coefficient" is itself a function of `y`.
    Written in `y` alone the phase carries half-integer powers:
        α = (h/4)(y^{−1/2} + h − 2) − (h/2)·y^{1/2}.
    The retracted formula's affine shape was an artifact of the bogus
    instance, in which `y₍₂,₁₎ := 1/2 − z` is affine in `z` BY CONSTRUCTION.

## ANTI-FIT

Nothing here inverts an experimental Q_β.  Production `c₃` is
`(Q_codata/Q_N2 − 1)/u³` — a CODATA inversion, a fit in every convention —
and is neither used nor computed.  Every number below is a value of an exact
rational function of `q` at the substrate pin; change the experimental Q_β
and not one of them moves.  No `c_k` is extracted, no tier moves, no value is
wired.

## Scope

The ansatz `α = (z−1)h/2` is ASSERTED upstream, not derived here (the Lean
docstring calls it "the asserted phase").  What A3/A4 derive is what that
ansatz EQUALS in terms of the weights — not the ansatz itself.  Every `c_k`
conclusion in the corpus remains convention-C-frame and un-re-derived under D
(bean `qou-cds1`); this probe touches none of them.

Pin: PROTON / experimental (`q₀ ≈ 1.1099785827513808`), 2026-08-07 owner
directive.  q₀ is taken from the package constant
`qou_substrate.constants.Q_50_DIGIT_STR`, never from a witness, and the LIVE
`y_lambda_at_q0_mpmath` is used rather than `wedderburn_jones_markov.
y_lambda_at`, which silently serves a muon-built cache when handed
`q_parameter.Q`.  No float64 enters any serialized value.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "computations" / "substrate"))

mp.mp.dps = 65

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from schur_principal_mpmath import (  # noqa: E402
    y_lambda_at_q0_mpmath, partitions_of, _f_lambda, hooks_and_contents,
)

Q0 = mp.mpf(Q_50_DIGIT_STR)
NMAX = 9

q = sp.symbols("q", positive=True)
Qs = q**2                      # Q = q²  (Wenzl variable under D)
h_sym = q - 1 / q              # h  = q − q⁻¹
two_q = q + 1 / q              # [2]_q
zD_sym = q**3 / (q**2 + 1)     # convention D Markov parameter

# q₀ as an exact sympy Float at working precision, for evaluation only.
Q0_SP = sp.Float(str(Q0), 60)


def at0(e: sp.Expr) -> mp.mpf:
    """Evaluate an exact rational function of q at the proton pin.

    The expression is exact; only the final substitution is numeric, and it
    is carried in 60-digit sympy Float → mpmath.mpf.  No float64 anywhere.
    """
    return mp.mpf(str(sp.N(e.subs(q, Q0_SP), 60)))


# ── ordinary S_n character at a transposition ────────────────────────────
def chi_transposition(lam: tuple[int, ...]) -> Fraction:
    """χ^λ(τ) for τ a transposition, via the content formula

        χ^λ(τ)/f^λ = (2/(n(n−1))) · Σ_{x∈λ} c(x).

    Exact in Fraction; the result is always an integer.
    """
    n = sum(lam)
    if n < 2:
        raise ValueError("transposition needs n >= 2")
    _, cs = hooks_and_contents(lam)
    val = Fraction(_f_lambda(lam) * 2 * sum(cs), n * (n - 1))
    assert val.denominator == 1, (lam, val)
    return val


def schur_1_Q(lam: tuple[int, ...]) -> sp.Expr:
    """s_λ(1, Q) exactly: `Q^{λ₂}·(1 + Q + … + Q^{λ₁−λ₂})` for two-row λ,
    and 0 for ℓ(λ) > 2 (the SU(2) row cap at Wenzl level r = 2)."""
    if len(lam) > 2:
        return sp.Integer(0)
    a = lam[0]
    b = lam[1] if len(lam) > 1 else 0
    return Qs**b * sum(Qs**k for k in range(a - b + 1))


def y_symbolic(n: int) -> dict[tuple[int, ...], sp.Expr]:
    """y_λ = s_λ(1,Q) / (1+Q)^n, exact over ℚ(q)."""
    return {
        lam: sp.cancel(sp.together(schur_1_Q(lam) / (1 + Qs) ** n))
        for lam in partitions_of(n)
    }


def chi_hecke_sigma1(lam: tuple[int, ...]) -> sp.Expr:
    """χ_λ(σ₁) on the Hecke irrep V_λ.

    σ₁ acts with eigenvalues `q` (multiplicity m₊) and `−q⁻¹` (multiplicity
    m₋), m₊ + m₋ = f^λ.  The pair is fixed by  m₊ − m₋ = χ^λ(τ)  (the q → 1
    specialisation, where σ₁ ↦ the transposition), so

        χ_λ(σ₁) = q·m₊ − q⁻¹·m₋.
    """
    f = _f_lambda(lam)
    d = int(chi_transposition(lam))
    m_plus = sp.Rational(f + d, 2)
    m_minus = sp.Rational(f - d, 2)
    return q * m_plus - m_minus / q


def zero(e: sp.Expr) -> bool:
    return sp.simplify(sp.together(sp.cancel(e))) == 0


def main() -> int:
    res: dict = {"checks": {}}
    ok = True

    # ── A0 · provenance of the RETRACTED relation ────────────────────────
    y_bogus = sp.Rational(1, 2) - zD_sym
    alpha_from_bogus = ((sp.Rational(1, 2) - y_bogus) - 1) * h_sym / 2
    retracted = -h_sym / 4 - (h_sym / 2) * y_bogus
    a0 = zero(alpha_from_bogus - retracted)
    yb = {(3,): zD_sym, (2, 1): y_bogus, (1, 1, 1): zD_sym}
    bogus_norm = zero(sum(_f_lambda(l) * v for l, v in yb.items()) - 1)
    bogus_sigma = zero(
        sum(chi_hecke_sigma1(l) * v for l, v in yb.items()) - zD_sym)
    res["checks"]["A0_retracted_is_change_of_variable"] = bool(a0)
    res["checks"]["A0_bogus_satisfies_normalisation"] = bool(bogus_norm)
    res["checks"]["A0_bogus_fails_sigma1_condition"] = bool(not bogus_sigma)
    ok &= a0 and bogus_norm and (not bogus_sigma)
    print(f"A0  retracted formula = change of variable off bogus instance: {a0}")
    print(f"A0  bogus instance: normalisation OK = {bogus_norm}, "
          f"sigma1-condition FAILS = {not bogus_sigma}")

    # A0b.  The retracted formula was TAUTOLOGICAL, not numerically wrong.
    # Fed its own bogus `y`, it returns alpha exactly (that is what a0 says),
    # so no arithmetic check could ever have caught it — only checking the
    # defining conditions could.  It diverges only when fed the REAL weight.
    y21_real = sp.cancel(sp.together(q**2 / (q**2 + 1) ** 2))
    retracted_on_real_y = -h_sym / 4 - (h_sym / 2) * y21_real
    alpha_true = (zD_sym - 1) * h_sym / 2
    a0b = not zero(retracted_on_real_y - alpha_true)
    res["checks"]["A0b_retracted_diverges_on_real_weight"] = bool(a0b)
    ok &= a0b
    print(f"A0b retracted formula is TAUTOLOGICAL on its own bogus y "
          f"(returns alpha exactly); it diverges only on the REAL "
          f"y_(2,1): {a0b}")

    # ── A1 · corpus weights ARE the two-variable Schur measure ───────────
    a1_max = mp.mpf(0)
    for n in range(2, NMAX + 1):
        live = y_lambda_at_q0_mpmath(n, Q0)
        sym = y_symbolic(n)
        for lam in partitions_of(n):
            a1_max = max(a1_max, abs(live[lam] - at0(sym[lam])))
    a1 = a1_max < mp.mpf(10) ** -45
    res["checks"]["A1_weights_are_schur_measure"] = bool(a1)
    res["A1_max_abs_dev"] = mp.nstr(a1_max, 6)
    ok &= a1
    print(f"A1  y_lam == s_lam(1,Q)/(1+Q)^n for n=2..{NMAX}: {a1} "
          f"(max dev {mp.nstr(a1_max, 4)})")

    # ── A2 · the character collapse ──────────────────────────────────────
    a2 = True
    for n in range(2, NMAX + 1):
        for lam in partitions_of(n):
            lhs = 2 * chi_hecke_sigma1(lam) - h_sym * _f_lambda(lam)
            rhs = two_q * int(chi_transposition(lam))
            if not zero(lhs - rhs):
                a2 = False
                print(f"A2  FAIL at {lam}")
    res["checks"]["A2_chi_collapse"] = bool(a2)
    ok &= a2
    print(f"A2  2*chi_lam(s1) - h*f^lam = [2]_q*chi^lam(tau), n=2..{NMAX}: {a2}")

    # ── A3/A4 · the loop-mean identity and n-independence of Ξ ───────────
    xi_target = (1 + Qs**2) / (1 + Qs) ** 2
    a3 = a4 = True
    for n in range(2, NMAX + 1):
        sym = y_symbolic(n)
        if not zero(sum(chi_hecke_sigma1(l) * v for l, v in sym.items())
                    - zD_sym):
            a3 = False
            print(f"A3  sigma1-condition FAILS at n={n}")
        xi = sum(int(chi_transposition(l)) * v for l, v in sym.items())
        if not zero(xi - xi_target):
            a4 = False
            print(f"A4  Xi_n != (1+Q^2)/(1+Q)^2 at n={n}")
        if not zero(2 * zD_sym - h_sym - two_q * xi):
            a3 = False
            print(f"A3  loop-mean identity FAILS at n={n}")
    res["checks"]["A3_loop_mean_identity"] = bool(a3)
    res["checks"]["A4_xi_independent_of_n"] = bool(a4)
    ok &= a3 and a4
    print(f"A3  2*z_D - h = [2]_q*Xi_n  for n=2..{NMAX}: {a3}")
    print(f"A4  Xi_n = (1+Q^2)/(1+Q)^2, independent of n, n=2..{NMAX}: {a4}")

    alpha_asserted = (zD_sym - 1) * h_sym / 2
    alpha_derived = (h_sym / 4) * (two_q * xi_target + h_sym - 2)
    a3b = zero(alpha_asserted - alpha_derived)
    res["checks"]["A3_alpha_closed_form"] = bool(a3b)
    ok &= a3b
    print(f"A3  alpha = (h/4)([2]_q*Xi + h - 2) matches (z_D-1)h/2: {a3b}")

    # ── A5 · α is NOT a function of the weights (bar-parity exclusion) ───
    alpha_bar = alpha_asserted.subs(q, 1 / q)
    a5_anom = zero(alpha_asserted + alpha_bar - h_sym**2 / 2)
    a5_even = True
    for n in range(2, NMAX + 1):
        for lam, v in y_symbolic(n).items():
            if not zero(v.subs(q, 1 / q) - v):
                a5_even = False
                print(f"A5  weight NOT bar-even at {lam}")
    wit = sp.cancel(sp.together(2 * zD_sym - h_sym - 2))
    a5_wit = zero(sp.numer(wit) - (q**4 - 2 * q**3 - 2 * q + 1))
    wit_at_q0 = at0(q**4 - 2 * q**3 - 2 * q + 1)
    a5 = (a5_anom and a5_even and a5_wit
          and abs(wit_at_q0) > mp.mpf(10) ** -40)
    res["checks"]["A5_alpha_not_weight_determined"] = bool(a5)
    res["A5_nonvanishing_witness_at_q0"] = mp.nstr(wit_at_q0, 20)
    ok &= a5
    print(f"A5  alpha + bar(alpha) = h^2/2: {a5_anom}; weights bar-even: "
          f"{a5_even}")
    print(f"A5  alpha != h^2/4 witness q^4-2q^3-2q+1 = "
          f"{mp.nstr(wit_at_q0, 12)} != 0: {a5}")

    # ── A6 · the affine shape does not survive ───────────────────────────
    y21 = y_symbolic(3)[(2, 1)]
    a6_recip = zero(y21 - 1 / two_q**2)
    coeff_true = sp.cancel(sp.together(-h_sym * two_q / 2))
    coeff_retracted = -h_sym / 2
    a6_diff = not zero(coeff_true - coeff_retracted)
    a6_ratio = zero(sp.cancel(sp.together(coeff_true / coeff_retracted))
                    - two_q)
    a6 = a6_recip and a6_diff and a6_ratio
    res["checks"]["A6_shape_does_not_survive"] = bool(a6)
    ok &= a6
    print(f"A6  y_(2,1) = 1/[2]_q^2 exactly: {a6_recip} => the y-coefficient "
          f"is itself a function of y (half-integer powers)")
    print(f"A6  true y_(2,1)-coefficient / retracted = [2]_q: {a6_ratio} "
          f"(retracted dropped exactly one factor of [2]_q)")

    # ── values at the proton pin (exact rational functions, no fit) ──────
    vals = {
        "q0_proton_pin": mp.nstr(Q0, 20),
        "h": mp.nstr(at0(h_sym), 20),
        "two_q": mp.nstr(at0(two_q), 20),
        "z_D": mp.nstr(at0(zD_sym), 20),
        "Xi_all_n": mp.nstr(at0(xi_target), 20),
        "y_3_n3": mp.nstr(at0(y_symbolic(3)[(3,)]), 20),
        "y_21_n3": mp.nstr(at0(y21), 20),
        "alpha_D": mp.nstr(at0(alpha_asserted), 20),
        "alpha_retracted_formula_on_its_own_bogus_y":
            mp.nstr(at0(retracted), 20),
        "alpha_retracted_formula_on_the_REAL_y21":
            mp.nstr(at0(retracted_on_real_y), 20),
        "alpha_bar_even_part_hsq_over_4": mp.nstr(at0(h_sym**2 / 4), 20),
        # Xi is convention-dependent; the D value above is not universal.
        "Xi_convention_C_HISTORICAL_for_contrast":
            mp.nstr(at0((2 * sp.sqrt(q) / (1 + q) - h_sym) / two_q), 20),
    }
    res["values_at_proton_pin"] = vals
    print("\n  values at the proton pin (exact rational functions of q):")
    for k, v in vals.items():
        print(f"    {k:38s} {v}")
    print("\n  Xi = (1+Q^2)/(1+Q)^2 is the SAME for every n >= 2.")
    print("  y_(3)(n=3) coincides with Xi only at n=3, because "
          "[4]_Q = (1+Q)(1+Q^2).")

    res["verdict"] = "all-checks-pass" if ok else "FAILED"
    print(f"\nverdict: {res['verdict']}")
    out = Path(__file__).with_name(
        "qbeta-ladder-phase-from-wedderburn-weights.json")
    out.write_text(json.dumps(res, indent=2) + "\n")
    print(f"wrote {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
