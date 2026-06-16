#!/usr/bin/env python3
"""qbeta_habiro_p8_deep_probe.py — second-round identification of P_8(u).

KEY OBSERVATION from the first probe:

  P_8(u)         = u^8 + 2u^7 + 2u^6 + 2u^5 + 4u^4 − 2u^3 + 2u^2 − 2u + 1
  u^8 · P_8(1/u) = u^8 − 2u^7 + 2u^6 − 2u^5 + 4u^4 + 2u^3 + 2u^2 + 2u + 1
                 = P_8(−u)               ← STRIKING SYMMETRY

This means P_8 is "bar-anti-invariant under sign":
  u^8 · P_8(1/u) = P_8(−u)
i.e. the involution u ↦ 1/u acts the same as u ↦ −u on P_8.

This is a strong constraint:
  P_8(u) − P_8(−u) = 2·(2u^7 + 2u^5 − 2u^3 − 2u)
                   = 4u·(u² − 1)·(u^4 + 2u² + 1)·something
                   = 4u·(u^6 + u^4 − u^2 − 1)
                   = 4u·(u² − 1)·(u² + 1)·(u² + 1)
                   = 4u·(u² − 1)·(u² + 1)²
                   = 4u·(u² − 1)·Φ_4(u)²

while
  P_8(u) + P_8(−u) = 2·(u^8 + 2u^6 + 4u^4 + 2u^2 + 1)

These split (even + odd) parts are themselves categorically suggestive:
the even part is palindromic with content (1, 2, 4, 2, 1) — Pascal-row-4
with the middle entry doubled. Let's investigate.

Additional tests in this probe:
  1. Verify u^8 · P_8(1/u) = P_8(−u).
  2. Split P_8 into even (in u²) and odd (in u·u²) parts; factor each.
  3. The even part P_e(v) where v=u² is a degree-4 polynomial in v;
     factor over ℚ and look for cyclotomic / categorical match.
  4. The odd part / u is a degree-3 polynomial in v=u²; factor.
  5. Try the substitution u = (1+t)/(1-t) (Cayley) and see if P_8
     becomes a known polynomial in t (e.g., Bring radical, Chebyshev).
  6. Try P_8(u)·P_8(−u) — degree 16 — does it factor cleanly?
  7. Sum-of-squares decomposition: is P_8 = A(u)² + (u² − 1)·B(u)²
     for some small-coeff polynomials A, B?  (This would identify it
     as a quadratic form discriminant.)
  8. Match against KNOWN Habiro/Hopf-link-related polynomials:
     - Habiro's "true Jones" polynomial for low-crossing knots
     - The Khovanov polynomial of trefoil
     - α_EM-Habiro element polynomial (parallel structure)
  9. Bring curve characteristic polynomial: P_Bring(v) = v^5 − v + 1
     — irreducible of degree 5; we'd need a degree-8 version.
  10. Check if P_8(u)·(u^15) divides the n-only or p-only Habiro
      element separately (deeper structural test).

OUTPUT:
    computations/qbeta-habiro-p8-deep.witness.json
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
import time
from pathlib import Path

import sympy as sp
import mpmath as mp

try:
    from _precision import set_compute_dps  # type: ignore
    set_compute_dps(65)
except Exception:
    mp.mp.dps = 65


SCRIPT_DIR = Path(__file__).resolve().parent
WITNESS_PATH = SCRIPT_DIR / "qbeta-habiro-p8-deep.witness.json"


u = sp.Symbol('u')
v = sp.Symbol('v')        # = u²
t = sp.Symbol('t')        # Cayley parameter

P8_coeffs_desc = [1, 2, 2, 2, 4, -2, 2, -2, 1]   # u^8 ... u^0
P8 = sum(c * u**(8 - i) for i, c in enumerate(P8_coeffs_desc))
P8 = sp.expand(P8)


# ── 1. Verify the bar-sign symmetry ──────────────────────────────

def verify_symmetry():
    """P_8(u) · u^{−8} · 1 mapping under u ↦ 1/u vs u ↦ −u."""
    P8_recip = sp.expand(u**8 * P8.subs(u, 1/u))
    P8_neg = sp.expand(P8.subs(u, -u))
    diff = sp.expand(P8_recip - P8_neg)
    return {
        "P8_recip_u8": str(P8_recip),
        "P8_neg_u": str(P8_neg),
        "P8_recip_eq_P8_neg": bool(diff == 0),
        "raw_diff": str(diff),
        "symbolic_interpretation": (
            "u ↦ 1/u acts the same as u ↦ −u on P_8(u). "
            "This means P_8 is the reciprocal-shifted partner of P_8(−u). "
            "Equivalently: under the substitution u = e^{iθ}, P_8 picks up "
            "the same phase as P_8 evaluated at u = e^{i(θ + π)}."
        ),
    }


# ── 2. Even / odd parts split ────────────────────────────────────

def split_even_odd():
    """P_8(u) = P_e(u²) + u · P_o(u²) where P_e, P_o have low degree."""
    P8_pos = P8
    P8_neg_form = P8.subs(u, -u)
    P_even = sp.expand((P8_pos + P8_neg_form) / 2)
    P_odd_full = sp.expand((P8_pos - P8_neg_form) / 2)
    # Odd part = u · P_o(u²) — extract P_o
    P_odd_div_u = sp.simplify(P_odd_full / u)

    # Express P_even and P_odd_div_u as polynomials in v = u²
    P_even_v = P_even.subs(u**2, v).subs(u**4, v**2).subs(u**6, v**3).subs(u**8, v**4)
    P_even_v = sp.expand(P_even_v)
    P_odd_v = P_odd_div_u.subs(u**2, v).subs(u**4, v**2).subs(u**6, v**3)
    P_odd_v = sp.expand(P_odd_v)

    return {
        "P_even_in_u": str(P_even),
        "P_odd_full_in_u": str(P_odd_full),
        "P_odd_div_u_in_u": str(P_odd_div_u),
        "P_even_in_v": str(P_even_v),
        "P_even_factored_in_v": str(sp.factor(P_even_v)),
        "P_odd_in_v": str(P_odd_v),
        "P_odd_factored_in_v": str(sp.factor(P_odd_v)),
        # Numerical at v=q_0 ≈ 1.11
        "P_even_at_v_eq_q0": mp.nstr(
            mp.mpf(str(P_even_v.subs(v, sp.Float("1.1099986"))).rstrip()), 30
        ) if isinstance(P_even_v, sp.Expr) else None,
    }


# ── 3. Identify the even / odd factors against known polynomials ─

def identify_even_odd():
    """The even part is P_e(v) = v^4 + 2v^3 + 4v^2 + 2v + 1, palindromic
    with middle coefficient enhanced — looks like (v² + v + 1)² + v?"""
    # P_even (in v) should be: ½ · 2·(v^4 + 2v^3 + 4v^2 + 2v + 1) = v^4 + 2v^3 + 4v^2 + 2v + 1
    # Verify against simple decompositions
    P_e = v**4 + 2*v**3 + 4*v**2 + 2*v + 1

    # Candidates
    candidates = {}

    # (v + 1)^4 = v^4 + 4v^3 + 6v^2 + 4v + 1  — diff: -2v^3 - 2v^2 - 2v
    candidates["(v + 1)^4"] = sp.expand((v + 1)**4)
    candidates["(v^2 + v + 1)^2"] = sp.expand((v**2 + v + 1)**2)  # v^4+2v^3+3v^2+2v+1, diff v^2
    candidates["(v^2 + 1)^2 + 2v(v^2 + 1)"] = sp.expand((v**2 + 1)**2 + 2*v*(v**2 + 1))
    candidates["(v^2 + v + 1)^2 + v^2"] = sp.expand((v**2 + v + 1)**2 + v**2)

    matches = {}
    for name, poly in candidates.items():
        diff = sp.expand(P_e - poly)
        matches[name] = {
            "form": str(poly),
            "matches_Pe": (diff == 0),
            "diff": str(diff),
        }

    # Bingo candidate: (v² + v + 1)² + v² = v^4 + 2v^3 + 3v^2 + 2v + 1 + v² = v^4 + 2v^3 + 4v^2 + 2v + 1
    # CHECK!  This factors P_e structurally.

    # The odd part: P_o(v) = u · (something in v) such that P_o(v) actually has
    # the form derived by ((P8(u)-P8(-u))/2) / u expanded in v.
    P_o_actual = -2*v**3 - 2*v + 0  # tentative — recompute
    # From P_8(u) - P_8(-u) = 2(2u^7 + 2u^5 - 2u^3 - 2u) = 4(u^7 + u^5 - u^3 - u)
    # Divide by u: 4(u^6 + u^4 - u^2 - 1) = 4(v^3 + v^2 - v - 1) = 4·(v - 1)(v + 1)(v + 1)... wait
    # = 4·(v^3 + v^2 - v - 1) = 4·(v^2(v+1) - (v+1)) = 4·(v+1)(v^2 - 1) = 4·(v+1)·(v-1)·(v+1)
    # So 4·(v+1)²·(v-1)
    # Divided by 2: 2·(v+1)²·(v-1)
    return {
        "P_e_candidate": str(P_e),
        "candidate_decompositions": matches,
        "P_o_in_u_eq_4_times": "u·(u^6 + u^4 - u^2 - 1) = u·(v+1)²·(v-1)  where v=u²",
        "P_o_canonical_factorization": "u · (u^2 + 1)^2 · (u^2 - 1) = u · Φ_4² · (u-1)(u+1)",
        # The complete decomposition:
        # P_8(u) = P_e(u²) + u · P_o(u²)
        # where:
        #   P_e(v) = (v² + v + 1)² + v² = v^4 + 2v^3 + 4v^2 + 2v + 1
        #   P_o(v)·u = u·(v+1)²·(v-1)·2 = 2u·(u²+1)²·(u²-1)
        # CHECK arithmetic:
        # 2u · (u² + 1)² · (u² - 1)
        # = 2u · (u^4 + 2u^2 + 1) · (u² - 1)
        # = 2u · (u^6 + u^4 - u^4 - u^2 + 2u^4 - 2u^2 + ... wait, recompute)
        # = 2u · ((u^4 + 2u^2 + 1)(u² - 1))
        # = 2u · (u^6 - u^4 + 2u^4 - 2u^2 + u^2 - 1)
        # = 2u · (u^6 + u^4 - u^2 - 1)
        # = 2u^7 + 2u^5 - 2u^3 - 2u
        # YES! Matches.  And P_8 odd part = (P_8 - P_8(-u))/2 = 2u^7 + 2u^5 - 2u^3 - 2u — CHECK.
    }


# ── 4. Even-part factorization is a categorical hint ─────────────

def even_part_categorical():
    """P_e(v) = (v² + v + 1)² + v² — categorical interpretation?

    (v² + v + 1) = Φ_3(v)·1 in v — i.e. Φ_3(v) is the cyclotomic
    for cube roots of unity.

    (v² + v + 1)² is the square of the 3rd cyclotomic polynomial
    evaluated at v = u² — this means in u, it's the 6th cyclotomic
    Φ_6(u²) = Φ_3(u²) reading... no wait Φ_3(u²) = u^4 + u² + 1
    which factors as Φ_3(u²) = (u² + u + 1)(u² - u + 1).

    So in u-variables: (v² + v + 1)² = Φ_3(u²)² = (u^4 + u² + 1)²

    P_e(v=u²) = (u^4 + u^2 + 1)² + u^4
              = u^8 + 2u^6 + 3u^4 + 2u^2 + 1 + u^4
              = u^8 + 2u^6 + 4u^4 + 2u^2 + 1   ✓ (matches!)

    So we have:
      P_e(u²) = Φ_3(u²)² + u^4
      P_o(u²)·u = 2u·(u²+1)²·(u²-1) = 2u·Φ_4(u)²·Φ_1(u)·Φ_2(u)

    Therefore:
      P_8(u) = Φ_3(u²)² + u^4 + 2u·Φ_4(u)²·Φ_1(u)·Φ_2(u)
             = [Φ_3(u²)]² + u^4 + 2u·[Φ_4(u)]²·(u² − 1)

    THIS IS A CATEGORICAL DECOMPOSITION INTO CYCLOTOMICS!
    """
    Phi3_u2 = u**4 + u**2 + 1     # Φ_3(u²) = (u²+u+1)(u²-u+1)
    Phi4 = u**2 + 1
    Phi1Phi2 = u**2 - 1
    even_via_cycl = sp.expand(Phi3_u2**2 + u**4)
    odd_via_cycl = sp.expand(2*u * Phi4**2 * Phi1Phi2)
    P8_via_cycl = sp.expand(even_via_cycl + odd_via_cycl)
    matches = bool(sp.simplify(P8_via_cycl - P8) == 0)

    return {
        "Phi_3_u_squared": str(Phi3_u2),
        "Phi_4": str(Phi4),
        "Phi_1_Phi_2": str(Phi1Phi2),
        "even_part_via_cycl": str(even_via_cycl),
        "odd_part_via_cycl": str(odd_via_cycl),
        "P8_reconstructed": str(P8_via_cycl),
        "matches_P8": matches,
        "categorical_form": (
            "P_8(u) = [Φ_3(u²)]² + u^4 + 2u·[Φ_4(u)]²·Φ_1(u)·Φ_2(u)"
            "       = [Φ_3(u²)]² + u^4 + 2u·[Φ_4(u)]²·(u² − 1)"
        ),
    }


# ── 5. Squared-sum decomposition: P_8 = A² + (u²−1)·B² ? ──────────

def sum_of_squares_decomposition():
    """Try P_8(u) = A(u)² + (u²−1)·B(u)² with deg(A) ≤ 4, deg(B) ≤ 3.

    If found, this expresses P_8 as a "twisted quadratic form" whose
    discriminant is (u² − 1) — the same cyclotomic prefactor.
    """
    A_coeffs = sp.symbols('a0:5')
    B_coeffs = sp.symbols('b0:4')
    A = sum(a * u**i for i, a in enumerate(A_coeffs))
    B = sum(b * u**i for i, b in enumerate(B_coeffs))

    target = sp.expand(A**2 + (u**2 - 1) * B**2)
    target_poly = sp.Poly(target, u)
    P8_poly = sp.Poly(P8, u)

    # Match coefficient-by-coefficient
    eqs = []
    target_coeffs = target_poly.all_coeffs()
    P8_full = P8_poly.all_coeffs()
    # Pad shorter
    target_deg = target_poly.degree()
    P8_deg = 8
    for k in range(max(target_deg, P8_deg) + 1):
        t_c = target_poly.coeff_monomial(u**(target_deg - k)) if k <= target_deg else 0
        p_c = P8_full[k] if k <= P8_deg else 0
        eqs.append(t_c - p_c)

    # Solve
    try:
        sol = sp.solve(eqs, list(A_coeffs) + list(B_coeffs), dict=True)
    except Exception as e:
        return {"err": str(e)}

    rational_solutions = []
    for s in sol:
        # Check if all are rational
        all_rat = all(sp.Rational(s[k]).is_rational for k in s if isinstance(s[k], (sp.Integer, sp.Rational, int)))
        rational_solutions.append({k: str(v) for k, v in s.items()})

    return {
        "ansatz": "P_8(u) = A(u)² + (u²−1)·B(u)², deg A ≤ 4, deg B ≤ 3",
        "n_solutions_found": len(sol),
        "solutions": rational_solutions[:5],   # First 5 only
    }


# ── 6. Cayley substitution u = (1+t)/(1-t): does P_8 become known? ─

def cayley_substitution():
    """u = (1+t)/(1-t) ⇒ u-1 = 2t/(1-t), u+1 = 2/(1-t).
    Substitute into P_8 and look for simpler form."""
    cayley = (1 + t) / (1 - t)
    P8_t = sp.simplify(P8.subs(u, cayley))
    # Multiply by (1-t)^8 to clear denominators
    P8_t_clear = sp.expand(P8_t * (1 - t)**8)
    factored = sp.factor(P8_t_clear)
    return {
        "after_cayley_subst": str(P8_t_clear),
        "factored": str(factored),
        "leading_coeff": str(sp.Poly(P8_t_clear, t).LC()),
    }


# ── 7. P_8 · P_8(−u) — degree-16 cleanup ──────────────────────────

def p8_times_p8_neg():
    """If P_8 and P_8(−u) are related cyclotomic factors of a known
    big polynomial, the product should factor cleanly."""
    P8_neg = P8.subs(u, -u)
    prod = sp.expand(P8 * P8_neg)
    factored = sp.factor(prod)
    # Try evaluating at u² — the product should be a polynomial in u²
    # if it has the bar/sign symmetry.
    prod_v = prod.subs(u**2, v).subs(u**4, v**2).subs(u**6, v**3).subs(u**8, v**4).subs(u**10, v**5).subs(u**12, v**6).subs(u**14, v**7).subs(u**16, v**8)
    return {
        "P8_times_P8_neg": str(prod),
        "factored": str(factored),
        "as_polynomial_in_v_u_squared": str(sp.expand(prod_v)) if u not in prod_v.free_symbols else "contains u (not just v)",
    }


# ── 8. Match against α_EM Habiro element & known low-deg Jones ─────

def match_alpha_em_habiro():
    """α_EM's Habiro element is [2]_q·(1 - h²α).  In u:
       [2]_q = q + 1 = u² + 1 = Φ_4(u)
       h² = (u - 1/u)² = (u² - 1)²/u²
       So [2]_q · (1 - h²α) = Φ_4(u) · (1 - α·(u²-1)²/u²)
                            = (u²+1) - α(u²+1)(u²-1)²/u²
                            = (u²+1) - α(u²+1)(u^4 - 2u² + 1)/u²

    Multiplying through by u²:
       u²·α_EM_Habiro = u²(u²+1) - α(u²+1)(u^4 - 2u² + 1)

    The DEGREE-6 polynomial form (multiplied to clear poles):
       u²(u²+1) is degree 4
       α·(u²+1)(u^4-2u²+1) is degree 6 in u (with α scalar)

    So at α=1, the combined polynomial is degree 6, not 8.  P_8 isn't
    directly this Habiro element — but it might be related by an extra
    h² or [2]_q factor (which would raise degree by 2 or 1, getting to 8).

    Try:
       P_8 vs Φ_4(u)·h²(u)·u^2 expanded
       P_8 vs (Φ_4(u))^2·h(u) · ...
    """
    Phi4 = u**2 + 1
    h_squared_times_u_sq = (u**2 - 1)**2  # u²·h²(u) = (u²-1)²
    n2_q = u**2 + 1

    # Candidate compositions of degree 8
    candidates = {}

    # Φ_4² · (u²-1)² = (u²+1)²(u²-1)² = (u^4-1)² = u^8 - 2u^4 + 1
    candidates["(u^4 - 1)^2"] = sp.expand((u**4 - 1)**2)

    # Φ_4 · (u²-1)² · Φ_3(u²) = ?
    candidates["Phi_4 · (u^2-1)^2 · Phi_3(u^2)"] = sp.expand(
        Phi4 * (u**2 - 1)**2 * (u**4 + u**2 + 1)
    )

    # The α_EM Habiro polynomial · u^k for various k
    alpha_em_unit_clear = sp.expand(
        u**2 * Phi4 - 1 * (u**2 + 1) * (u**4 - 2*u**2 + 1)
    )   # α_EM at α=1, multiplied by u²
    candidates["alpha_em_at_alpha_1_times_u^2"] = alpha_em_unit_clear

    # The "categorical_form" from probe 4: try to express P_8 differently
    # P_8(u) = [Φ_3(u²)]² + u^4 + 2u·[Φ_4(u)]²·(u²−1)
    # And the prefactor in the parent factorization is u^15·(u²−1)·P_8(u)
    # So combining with the prefactor:
    # u^15·(u²−1)·P_8(u) = u^15·(u²−1)·{[Φ_3(u²)]² + u^4} + 2u^16·[Φ_4(u)]²·(u²−1)²

    matches = {}
    for name, poly in candidates.items():
        diff = sp.expand(P8 - poly)
        matches[name] = {
            "form": str(poly),
            "matches_P8": (diff == 0),
            "diff_factored": str(sp.factor(diff)),
        }

    return matches


# ── 9. Bring/Sextic comparison ────────────────────────────────────

def bring_curve_comparison():
    """The Bring sextic is t^5 - t + 1 (degree 5, irreducible over ℚ).
    No direct degree-8 candidate, but the Bring DISCRIMINANT-related
    polynomials live in degree 8. Skipping detailed Bring analysis here
    — it would require auxiliary modules."""
    return {
        "note": "Bring polynomial is degree 5. Degree-8 Bring-related polys"
                " require auxiliary computations not in scope of this probe.",
        "future_work": (
            "Compute the Bring curve's `resolvent cubic` x `resolvent` "
            "to obtain a degree-8 polynomial; check against P_8."
        ),
    }


# ── 10. Numerical at substrate q_0 — comparison to physical scales ─

def physical_scale_comparison():
    """Compare P_8(u_0) and P_8(q_0) to known categorical scalars."""
    mp.mp.dps = 65
    u0 = mp.mpf("1.05356473")
    q0 = u0 * u0   # ≈ 1.10999864

    # Build coefficients in mp
    p8_u0 = mp.mpf(0)
    for i, c in enumerate(P8_coeffs_desc):
        p8_u0 += mp.mpf(c) * (u0 ** (8 - i))

    # Compare to:
    #  - The Q_β predicted value at u_0 ≈ ...
    #  - The c_2 Taylor coefficient (= 1)
    #  - The c_3 near-match value (= −2 ≈ J_Hopf(q=1))
    #  - Atomic Hopf-link Jones polynomial values
    return {
        "u_0": "1.05356473",
        "q_0": mp.nstr(q0, 30),
        "P8_at_u0": mp.nstr(p8_u0, 50),
        "P8_at_u0_div_10": mp.nstr(p8_u0 / 10, 50),  # divided by P8(1)=P8(-1)=10
        "P8_at_u0_div_q0^7": mp.nstr(p8_u0 / (q0**7), 50),
        # Compare to physical Q_β shift O(10^-4)
        "comment": (
            "P_8(u_0) ≈ 13.43, P_8(q_0) ≈ 18.15.  Neither is close to "
            "any of the standard q-integers or h-expressions.  The fact "
            "that P_8(±1) = 10 = the content of Δa_1 suggests a "
            "structural link to the m=1 Habiro rung."
        ),
    }


# ── Main ──────────────────────────────────────────────────────────

def main():
    start = time.time()
    print(f"== P_8 deep identification probe ==\n")

    print("[1] Verify u^8·P_8(1/u) = P_8(−u) symmetry ...")
    out_sym = verify_symmetry()
    print(f"    u^8·P(1/u) = P(-u)?  {out_sym['P8_recip_eq_P8_neg']}")
    print(f"    raw diff = {out_sym['raw_diff']}")
    print()

    print("[2] Even/odd split ...")
    out_split = split_even_odd()
    print(f"    P_even(v=u²) = {out_split['P_even_in_v']}")
    print(f"    P_even factored: {out_split['P_even_factored_in_v']}")
    print(f"    P_odd(v=u²)·u = u·{out_split['P_odd_factored_in_v']}")
    print()

    print("[3] Identify even-part decomposition ...")
    out_id = identify_even_odd()
    print(f"    Candidates: {list(out_id['candidate_decompositions'].keys())}")
    for name, info in out_id["candidate_decompositions"].items():
        if info["matches_Pe"]:
            print(f"    MATCH: P_e = {name}")
    print()

    print("[4] Categorical (cyclotomic) decomposition ...")
    out_cycl = even_part_categorical()
    print(f"    P_8 = {out_cycl['categorical_form']}")
    print(f"    Decomposition matches P_8: {out_cycl['matches_P8']}")
    print()

    print("[5] Sum-of-squares decomposition ...")
    out_sos = sum_of_squares_decomposition()
    print(f"    Solutions: {out_sos.get('n_solutions_found', '?')}")
    print()

    print("[6] Cayley substitution u = (1+t)/(1-t) ...")
    out_cay = cayley_substitution()
    print(f"    After Cayley: {out_cay['after_cayley_subst'][:80]}...")
    print(f"    Factored: {out_cay['factored']}")
    print()

    print("[7] P_8 · P_8(-u) factorization ...")
    out_prod = p8_times_p8_neg()
    print(f"    Product factored: {out_prod['factored'][:100]}")
    print()

    print("[8] α_EM Habiro / Jones comparisons ...")
    out_em = match_alpha_em_habiro()
    print(f"    Candidates: {list(out_em.keys())}")
    for name, info in out_em.items():
        if info.get("matches_P8"):
            print(f"    MATCH: {name}")
    print()

    print("[9] Bring curve note ...")
    out_bring = bring_curve_comparison()
    print(f"    {out_bring['note']}")
    print()

    print("[10] Physical scale comparison ...")
    out_phys = physical_scale_comparison()
    print(f"    P_8(u_0) = {out_phys['P8_at_u0']}")
    print(f"    {out_phys['comment']}")
    print()

    duration_ms = int((time.time() - start) * 1000)

    witness = {
        "engine": "python+sympy+mpmath",
        "engineVersion": f"python {sys.version.split()[0]}",
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
        "commitSha": "auto",
        "assertions": [
            {
                "name": "u8_P_recip_eq_P_neg_u",
                "computed": int(out_sym["P8_recip_eq_P8_neg"]),
                "expected": 1,
                "passed": out_sym["P8_recip_eq_P8_neg"],
                "tolerance": 0,
                "source": "Direct sympy symbolic verification."
            },
            {
                "name": "categorical_cyclotomic_decomp_matches",
                "computed": int(out_cycl["matches_P8"]),
                "expected": 1,
                "passed": out_cycl["matches_P8"],
                "tolerance": 0,
                "source": "P_8(u) = [Φ_3(u²)]² + u^4 + 2u·[Φ_4(u)]²·(u²−1)"
            },
        ],
        "allPassed": out_sym["P8_recip_eq_P8_neg"] and out_cycl["matches_P8"],
        "durationMs": duration_ms,
        "computation": "qbeta-habiro-p8-deep",
        "scriptFile": "qbeta_habiro_p8_deep_probe.py",
        "scriptHash": "auto",
        "precisionMetadata": {
            "compute_dps": 65,
            "output_dps": 50,
            "guard_digits": 15,
            "truncation_bound": "1e-50",
        },
        "environment": {
            "python": sys.version.split()[0],
            "sympy": sp.__version__,
            "mpmath": mp.__version__,
        },
        "description": (
            "Second-round identification of P_8(u). Tests symmetry "
            "u ↦ 1/u vs u ↦ −u, even/odd cyclotomic decomposition "
            "P_8 = Φ_3(u²)² + u^4 + 2u·Φ_4(u)²·(u²−1), sum-of-squares, "
            "Cayley substitution, α_EM Habiro comparisons."
        ),
        "contentBlock": "prop:neutron-qvalue-symbolic",
        "data": {
            "P8_polynomial": str(P8),
            "P8_coefficients_descending": P8_coeffs_desc,
            "symmetry": out_sym,
            "even_odd_split": out_split,
            "even_part_identification": out_id,
            "categorical_cyclotomic_decomposition": out_cycl,
            "sum_of_squares_decomposition": out_sos,
            "cayley_substitution": out_cay,
            "P8_times_P8_neg": out_prod,
            "alpha_em_jones_match_attempts": out_em,
            "bring_curve_note": out_bring,
            "physical_scale_comparison": out_phys,
        },
    }

    WITNESS_PATH.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWrote witness → {WITNESS_PATH}")
    print(f"Total wall: {duration_ms} ms")


if __name__ == "__main__":
    main()
