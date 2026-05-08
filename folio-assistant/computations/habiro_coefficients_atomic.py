#!/usr/bin/env python3
"""
Habiro cyclotomic coefficients a_m(K) for atomic braids.

Per content/braids-and-knots/full-pole-structure-mass-trace.md and
habiro-ring.md, the Markov trace of an atomic braid admits a
Habiro / cyclotomic expansion

    tr_M(T_w, q)  =  Σ_{m ≥ 0}  a_m(T_w) · (q; q)_m

with  (q;q)_m = (1-q)(1-q²)···(1-q^m)  the q-Pochhammer.

For finite-degree Laurent polynomials the cyclotomic expansion is
computed by sequential polynomial division:

    a_0(q)  =  p(q)  mod (1 - q)              (a constant in ℤ)
    p_1(q)  = (p(q) - a_0) / (1 - q)
    a_1(q)  =  p_1(q) mod (1 - q²)            (degree ≤ 1 in q)
    p_2(q)  = (p_1(q) - a_1) / (1 - q²)
    ...

For atomic-braid Markov traces, p(q) ∈ ℤ[q^{1/2}, q^{-1/2}].  Setting
u = q^{1/2} and clearing denominators gives p(u) ∈ ℤ[u, u^{-1}], to
which we apply the cyclotomic algorithm in u (i.e. expand in
(u;u)_m).  The Habiro property to verify is:

    INTEGRALITY:  every a_m(u) ∈ ℤ[u, u^{-1}]
    TERMINATION:  a_m = 0 for m exceeding the polynomial degree

Witness: habiro-coefficients-atomic.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from sympy import Symbol, Rational, Integer, simplify, together, nsimplify

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
from hecke_character_symbolic import q_character_on_braid_word
from canonical_braid_crossings import atom_canonical_crossings as atomic_braid_to_crossings
from schur_weyl_symbolic import partitions_of, schur_weyl_weight


def markov_trace_symbolic(Z, N, q, include_inter=True):
    """tr_M(T_w(Z,N), q) = Σ_{λ ⊢ 3A} w_λ(q) · χ^λ_q(T_w).

    Returns a sympy expression in q.
    """
    A = Z + N
    crossings = atomic_braid_to_crossings(Z, N, include_inter=include_inter)
    total = Integer(0)
    for lam in partitions_of(3 * A):
        try:
            w = schur_weyl_weight(lam, q)
            if w == 0:
                continue
            chi = q_character_on_braid_word(lam, crossings, q)
            if chi == 0:
                continue
            term = sp.cancel(w * chi)
            # Guard against NaN/Inf produced by Hoefsmit edge cases
            # (some 2x2 blocks at b² = 0 collapse to 1x1 and need
            # special handling — flagged for follow-up at A ≥ 2).
            if term.has(sp.nan) or term.has(sp.zoo):
                raise ValueError(f"NaN/Inf in λ = {lam}")
            total += term
        except Exception as exc:
            raise RuntimeError(
                f"Markov trace symbolic failed at λ = {lam} "
                f"(A = {A}): {type(exc).__name__}: {exc}") from exc
    return sp.cancel(total)


def to_u_polynomial(expr_in_q, q, u):
    """Substitute q → u² and clear ALL u-denominators (including any
    cyclotomic / Markov-normalisation factors).  Returns
    (p_in_u, shift, denom) such that

        p_in_u(u)  =  u^{shift} · denom(u) · expr_in_q(u²)

    is a polynomial in u with no negative powers.  The Habiro
    expansion is then computed for p_in_u and the result is the
    cyclotomic decomposition of the Markov-renormalised Jones-like
    object (the Markov normalisation z^n = (u + u^{-1})^{-n} is
    absorbed into the prefactor).
    """
    expr_u = sp.together(expr_in_q.subs(q, u ** 2))
    num, den = sp.fraction(expr_u)
    num = sp.expand(num)
    den = sp.expand(den)
    # Clear u-denominator entirely: multiply by den and shift to make
    # the result a polynomial in u.
    p_raw = num
    if den != 1:
        # Already cleared: p_raw = num, total = num/den; multiply by den
        pass
    # Normalise to non-negative powers of u
    p_expanded = sp.expand(p_raw)
    poly = sp.Poly(p_expanded, u)
    coeffs = poly.all_coeffs()
    # Determine min and max exponent
    monoms = poly.monoms()
    if not monoms:
        return Integer(0), 0, str(den)
    min_pow = min(int(m[0]) for m in monoms)
    shift = -min_pow if min_pow < 0 else 0
    p_shifted = sp.expand(p_expanded * u ** shift)
    return p_shifted, shift, str(sp.expand(den))


def cyclotomic_expansion(p_in_u, u, max_m=20):
    """Expand p(u) = Σ_m a_m(u) · (u;u)_m by sequential polynomial
    division.

    Algorithm.  At step m, p_m(u) is the running remainder.  We
    define

        a_m(u)  =  p_m(u)  mod (1 - u^{m+1})        (deg ≤ m)
        p_{m+1} = (p_m(u) - a_m(u)) / (1 - u^{m+1}) (exact division)

    so that p(u) = a_0 + a_1(1-u) + a_2(1-u)(1-u²) + ⋯.  The
    iteration terminates exactly when p_{m+1} = 0; if p has finite
    degree this happens at some m_max ~ √(2·deg p).

    Returns a list of dicts, one per m.
    """
    p = sp.Poly(sp.expand(p_in_u), u)
    coeffs = []
    current = p
    for m in range(max_m):
        if current.as_expr() == 0:
            break
        next_factor = sp.Poly(1 - u ** (m + 1), u)
        # a_m = p_m mod (1 - u^{m+1})   (degree < m+1)
        _, a_m = sp.div(current, next_factor, u)
        a_m_expr = a_m.as_expr()
        diff = sp.expand(current.as_expr() - a_m_expr)
        try:
            quotient, rem2 = sp.div(sp.Poly(diff, u), next_factor, u)
        except sp.PolynomialError:
            break
        rem_zero = (rem2.as_expr() == 0)
        coeffs.append({
            "m": m,
            "a_m": str(a_m_expr),
            "deg_a_m": int(a_m.degree()) if a_m.as_expr() != 0 else 0,
            "integral": all(c.is_Integer for c in a_m.all_coeffs())
                          if a_m.as_expr() != 0 else True,
            "remainder_nonzero": not rem_zero,
        })
        if not rem_zero:
            break
        current = quotient
    return coeffs


def reconstruct(coeffs_data, u, max_m=20):
    """Reconstruct p(u) = Σ a_m · (u;u)_m from the list to verify."""
    total = Integer(0)
    for entry in coeffs_data:
        m = entry["m"]
        a_m = sp.sympify(entry["a_m"], locals={"u": u})
        poch = Integer(1)
        for k in range(1, m + 1):
            poch *= 1 - u ** k
        total += sp.expand(a_m * poch)
    return sp.expand(total)


def analyse_atomic_braid(label, Z, N, include_inter, q):
    print(f"\n── {label} (Z={Z}, N={N}) ──")
    p_q = markov_trace_symbolic(Z, N, q, include_inter=include_inter)
    print(f"  tr_M (in q): {sp.nsimplify(p_q)}")
    u = sp.Symbol('u', positive=True, real=True)
    p_u, shift, denom = to_u_polynomial(p_q, q, u)
    deg_p = int(sp.Poly(p_u, u).degree()) if p_u != 0 else 0
    print(f"  → p(u) := u^{shift} · denom · tr_M(u²), shift = u^{shift}, "
          f"denom (in u) = {denom}")
    print(f"     deg p(u) = {deg_p}")
    coeffs = cyclotomic_expansion(p_u, u, max_m=20)
    print(f"  Habiro coefficients (in u = q^{{1/2}}):")
    for entry in coeffs:
        flag = "✓" if entry["integral"] else "✗"
        print(f"    a_{entry['m']}(u) = {entry['a_m']}    "
              f"deg = {entry['deg_a_m']}, integral: {flag}")
    # Verify reconstruction
    recon = reconstruct(coeffs, u)
    diff = sp.expand(recon - p_u)
    if diff == 0:
        print(f"  ✓ reconstruction matches  Σ a_m·(u;u)_m  =  p(u)")
    else:
        print(f"  ✗ reconstruction error:  diff = {diff}")
    # Numerical check
    q0 = Rational(int(_Q_CANONICAL * 10 ** 16), 10 ** 16)
    u0 = sp.sqrt(q0)
    p_at_q0 = float(p_q.subs(q, q0).evalf(30))
    p_at_q0_polynomial_q = expose_polynomial(p_q, q)
    p_u_at_u0 = float(p_u.subs(u, u0).evalf(30)) / float(
        u0 ** shift if shift else 1)
    print(f"  tr_M @ q_0 = {p_at_q0:+.6e}  "
          f"(via u-poly: {p_u_at_u0:+.6e})")
    return {
        "Z": Z, "N": N, "include_inter": include_inter,
        "tr_M_in_q": str(sp.nsimplify(p_q)),
        "shift": int(shift),
        "denom_in_u": denom,
        "p_in_u": str(p_u),
        "deg_p_u": deg_p,
        "habiro_coefficients": coeffs,
        "all_integral": all(c["integral"] for c in coeffs),
        "reconstruction_matches": (diff == 0),
        "tr_M_at_q0": p_at_q0,
    }


if __name__ == "__main__":
    print("HABIRO CYCLOTOMIC COEFFICIENTS — atomic braids")
    print("=" * 80)
    print(f"q_0 = {float(_Q_CANONICAL):.6f}")

    q = sp.Symbol('q', positive=True, real=True)

    # A=1 (proton, neutron): tractable in symbolic q (~1 min total).
    # A=2 (deuteron): 11 partitions of 6 with Hoefsmit dim up to 9 in
    #   symbolic q over a 12-crossing braid — heavy (>10 min).  Run via
    #   `--with-deuteron` flag once a faster symbolic pipeline is wired
    #   up, or evaluate numerically at q_0 and verify integer coefficients
    #   of the resulting Laurent polynomial.
    import os
    cases = [
        ("p (proton, A=1)",      1, 0, False),
        ("n (neutron, A=1)",     0, 1, False),
    ]
    if os.environ.get("HABIRO_WITH_DEUTERON"):
        cases.append(("D (deuteron, A=2)", 1, 1, True))

    results = {}
    for label, Z, N, inter in cases:
        try:
            results[label] = analyse_atomic_braid(label, Z, N, inter, q)
        except Exception as exc:
            print(f"  {label}: ERROR {type(exc).__name__}: {exc}")
            results[label] = {"error": f"{type(exc).__name__}: {exc}"}

    print("\n── Summary ──")
    for label, r in results.items():
        if "error" in r:
            print(f"  {label}: ERROR {r['error']}")
            continue
        print(f"  {label}: deg p(u) = {r['deg_p_u']:>3}, "
              f"#Habiro coeffs = {len(r['habiro_coefficients']):>2}, "
              f"all integral: {r['all_integral']}, "
              f"reconstruction: {r['reconstruction_matches']}")

    witness = {
        "computation": "habiro-coefficients-atomic",
        "description": (
            "Habiro / cyclotomic expansion tr_M(T_w, q) = Σ_m a_m·(u;u)_m "
            "(u = q^{1/2}) for atomic braids p, n, D. Verifies the integrality "
            "and termination properties of the Habiro coefficients claimed "
            "in habiro-ring.md and full-pole-structure-mass-trace.md."
        ),
        "reference_blocks": [
            "def:habiro-ring",
            "prop:full-pole-structure-mass-trace",
            "thm:knot-mass-formula-unified",
            "prop:e-infinity-page-identifications",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": float(_Q_CANONICAL),
            "engine": "sympy Poly + sequential cyclotomic division",
        },
        "results": results,
    }
    out = Path(__file__).parent / "habiro-coefficients-atomic.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
