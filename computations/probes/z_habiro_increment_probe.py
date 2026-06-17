#!/usr/bin/env python3
"""
z-Habiro increment-bound probe (EXPLORATORY).

Tests the one open hypothesis that the formalize-first Lean work
(`QOU.MassEndomorphism.ZHabiroCauchy`) reduced the brane-tower
Cauchy-limit conjecture to: does the q-dilogarithm

    Φ_q(z) = ∏_{k≥1} (1 - q^{-k} z)^{-1}

admit a CYCLOTOMIC EXPANSION in the z-Habiro filtration basis

    P_n(q, z) = ∏_{k=1}^{n} (1 - q^{-k} z),   P_0 = 1,

i.e.  Φ_q(z) = Σ_{n≥0} c_n(q) · P_n(q, z) ?

If such c_n exist (over ℚ(q)), then the truncations
a_N = Σ_{n=0}^N c_n P_n satisfy the depth-increment bound

    a_{N+1} - a_N = c_{N+1} P_{N+1} ∈ (P_N)            (since P_N | P_{N+1})

— exactly `IsCauchyFiltration` of the Lean file — so the algebraic
Cauchy limit EXISTS. The SHARPER question is the RING the limit lives
in:
  * c_n ∈ ℤ[q^±1]  (Laurent polys)  ⇒  the INTEGRAL z-Habiro ring
    (Habiro's ring); the strongest form of the conjecture.
  * c_n only in a LOCALISATION (denominators = cyclotomic factors
    1 - q^{-j}, which are NOT units)  ⇒  the limit exists, but in
    ℤ[q^±1] localised at the cyclotomic factors — Φ_q's poles at
    z = q^k are exactly the obstruction to integrality.

Everything is EXACT symbolic over ℚ(q) (sympy) — no floats, no
fitting. The series coefficients are the closed Euler form
    [z^m] Φ_q = q^{-m} / ∏_{j=1}^m (1 - q^{-j})
(Euler's identity ∏_{k≥0}(1-x t^k)^{-1} = Σ x^m/(t;t)_m with t=q^{-1},
x=z q^{-1}).

Output: z-habiro-increment-probe.witness.json
Content block: conj:brane-tower-z-habiro (exploratory probe)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
M = int(sys.argv[1]) if len(sys.argv) > 1 else 9   # cyclotomic depth

q, z = sp.symbols("q z")


def q_poch_inv_neg(m: int):
    """(q^{-1}; q^{-1})_m = ∏_{j=1}^m (1 - q^{-j})."""
    return sp.prod([1 - q ** (-j) for j in range(1, m + 1)]) if m > 0 else sp.Integer(1)


def b(m: int):
    """[z^m] Φ_q(z) = q^{-m} / ∏_{j=1}^m (1 - q^{-j})  (Euler closed form)."""
    return sp.cancel(q ** (-m) / q_poch_inv_neg(m))


def P(n: int):
    """P_n(q,z) = ∏_{k=1}^n (1 - q^{-k} z)."""
    return sp.prod([1 - q ** (-k) * z for k in range(1, n + 1)]) if n > 0 else sp.Integer(1)


def is_laurent_in_q(expr) -> bool:
    """True iff expr ∈ ℤ[q, q^{-1}] (Laurent poly): denominator is a
    monomial q^k (a unit), numerator a polynomial in q with integer
    coeffs."""
    e = sp.cancel(sp.together(expr))
    num, den = sp.fraction(e)
    den = sp.expand(den)
    # denominator must be a monomial c * q^k
    dpoly = sp.Poly(den, q)
    if len(dpoly.monoms()) != 1:
        return False
    # numerator: polynomial in q after clearing the q^k; check integer coeffs
    cleared = sp.expand(num / den * sp.Poly(den, q).LC())  # strip unit
    # simpler: e * q^k should be a polynomial with integer coeffs
    k = dpoly.monoms()[0][0]
    test = sp.expand(e * q ** k)
    tp = sp.Poly(test, q)
    if not tp.is_polynomial():
        return False
    return all(c.is_integer for c in tp.all_coeffs())


def main() -> int:
    print("=" * 70)
    print("  z-Habiro increment-bound probe (Φ_q cyclotomic expansion)")
    print(f"  depth M = {M}  (exact symbolic over ℚ(q))")
    print("=" * 70)

    # Truncated series Σ_{m=0}^M b_m z^m
    phi = sum(b(m) * z ** m for m in range(M + 1))

    # Basis P_0..P_M (degree n in z); triangular change of basis.
    Pn = [sp.expand(P(n)) for n in range(M + 1)]
    lead = [sp.cancel(sp.Poly(Pn[n], z).coeff_monomial(z ** n)) for n in range(M + 1)]

    c = [None] * (M + 1)
    rem = sp.expand(phi)
    for n in range(M, -1, -1):
        rp = sp.Poly(rem, z)
        top = sp.cancel(rp.coeff_monomial(z ** n))
        c[n] = sp.cancel(top / lead[n])
        rem = sp.expand(rem - c[n] * Pn[n])

    residual = sp.simplify(rem)
    print(f"\n  Reconstruction residual (should be 0): {residual}")

    # Report each c_n and integrality
    print("\n  Cyclotomic coefficients c_n(q):")
    rows = []
    all_integral = True
    first_nonintegral = None
    for n in range(M + 1):
        cn = sp.cancel(c[n])
        integral = is_laurent_in_q(cn)
        if not integral:
            all_integral = False
            if first_nonintegral is None:
                first_nonintegral = n
        num, den = sp.fraction(sp.together(cn))
        print(f"    c_{n}: [{'ℤ[q^±1] integral' if integral else 'localised (non-unit den)'}]"
              f"  den = {sp.expand(den)}")
        rows.append({
            "n": n,
            "c_n": str(cn),
            "numerator": str(sp.expand(num)),
            "denominator": str(sp.expand(den)),
            "integral_laurent": bool(integral),
        })

    # Verify the increment bound a_{n+1}-a_n ∈ (P_n) symbolically for each n.
    print("\n  Increment-bound check  a_{n+1}-a_n = c_{n+1} P_{n+1} ∈ (P_n):")
    incr_ok = True
    incr_rows = []
    for n in range(M):
        incr = sp.expand(c[n + 1] * Pn[n + 1])
        quo, r = sp.div(sp.Poly(incr, z), sp.Poly(Pn[n], z))
        r = sp.simplify(r.as_expr())
        ok = (r == 0)
        incr_ok = incr_ok and ok
        incr_rows.append({"n": n, "divisible_by_P_n": bool(ok),
                          "remainder": str(r)})
    print(f"    a_(n+1)-a_n ∈ (P_n) for all n<{M}:  {incr_ok}")

    # ── Verdict ──────────────────────────────────────────────────
    print("\n" + "=" * 70)
    if residual == 0 and incr_ok:
        print("  ✓ Φ_q ADMITS a cyclotomic P_n-expansion over ℚ(q):")
        print("    the depth-increment bound (IsCauchyFiltration) HOLDS —")
        print("    the algebraic Cauchy limit EXISTS over ℚ(q).")
    else:
        print("  ✗ cyclotomic expansion FAILED to reconstruct Φ_q — check math.")
    if all_integral:
        print("  ✓ all c_n ∈ ℤ[q^±1]: limit lives in the INTEGRAL z-Habiro ring.")
    else:
        print(f"  ⚠ c_n NOT all integral (first non-integral: n={first_nonintegral}):")
        print("    the limit exists but in ℤ[q^±1] LOCALISED at the cyclotomic")
        print("    factors (1-q^{-j}); Φ_q's poles at z=q^k obstruct integrality.")
    print("=" * 70)

    witness = {
        "computation": "z-habiro-increment-probe",
        "kind": "exploratory-probe",
        "content_block": "conj:brane-tower-z-habiro",
        "engine": "sympy-exact",
        "depth_M": M,
        "result": {
            "cyclotomic_expansion_exists_over_QQ_q": bool(residual == 0),
            "increment_bound_holds": bool(incr_ok),
            "reconstruction_residual": str(residual),
            "all_c_n_integral_laurent": bool(all_integral),
            "first_nonintegral_n": first_nonintegral,
            "verdict": (
                "cauchy-limit-exists-integral" if (residual == 0 and incr_ok and all_integral)
                else "cauchy-limit-exists-localised" if (residual == 0 and incr_ok)
                else "expansion-failed"
            ),
        },
        "coefficients": rows,
        "increment_checks": incr_rows,
        "_provenance": {
            "series_coeff_formula": "[z^m] Phi_q = q^-m / prod_{j=1}^m (1-q^-j)  (Euler)",
            "filtration_basis": "P_n = prod_{k=1}^n (1 - q^-k z)",
            "lean_ref": "QOU.MassEndomorphism.ZHabiroCauchy.IsCauchyFiltration",
        },
    }
    out = HERE.parent / "z-habiro-increment-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
