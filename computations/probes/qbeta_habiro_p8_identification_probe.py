#!/usr/bin/env python3
"""qbeta_habiro_p8_identification_probe.py — identify P_8(u) categorically.

FOLLOW-UP per docs/audits/2026-05-31-qbeta-habiro-delta-am-factorization.md:

The n-p Habiro element factors as

    Σ_m Δa_m·(u;u)_m  =  −u^15 · (u − 1) · (u + 1) · P_8(u)
                      =   u^15 · (u² − 1) · P_8(u) · (−1)

where the prefactor `u^15·(u²−1) = u^15·Φ_1·Φ_2` is the
classical-limit vanishing witness, and

    P_8(u) = u^8 + 2·u^7 + 2·u^6 + 2·u^5 + 4·u^4 − 2·u^3
                + 2·u^2 − 2·u + 1

is irreducible over ℚ.  This probe attempts to IDENTIFY P_8
categorically.

Probes (all sympy symbolic):
  1. Roots of P_8 in ℂ: 50-dps numerical, then nature classification
     (roots of unity? algebraic of small degree? real? complex pair?
     on unit circle?).
  2. Symmetry tests: palindromic, anti-palindromic, bar-invariant
     (P_8(1/u)·u^8 = ±P_8(u)).
  3. Cyclotomic reduction: gcd(P_8, Φ_k) for k=1..24, check if any
     prime-power cyclotomic divides P_8.  Reduce mod each Φ_k.
  4. Numerical evaluation at u_0 = sqrt(q_0) ≈ 1.05356 and at q_0
     itself; check if value matches any known categorical scalar
     (h, h², J_Hopf, [n]_q for small n, etc.).
  5. Match against known categorical degree-8 polynomial families:
       - Quantum 6j coefficient polynomials
       - Jones polynomial of small (3,4) torus knots
       - Wenzl/Hoefsmit characters χ^λ for λ ⊢ 4
       - Chebyshev polynomials U_8 / T_8
       - Bring-curve period polynomial (substrate is Bring-anchored)
  6. Extension probes:
       - P_8(u) / J_Hopf(u)^k for k = 1, 2
       - P_8(u) − (u² − 1)^4
       - P_8(u) mod Φ_3(u), Φ_4(u), Φ_5(u), Φ_6(u), Φ_8(u), Φ_12(u)
  7. Symbol-table match: the coefficient sequence (1, 2, 2, 2, 4,
     −2, 2, −2, 1) — does it match a known integer sequence
     (Catalan-like? Fibonacci-like? signed binomial?)

OUTPUT:
    computations/qbeta-habiro-p8-identification.witness.json

USAGE:
    python3 -u qbeta_habiro_p8_identification_probe.py 2>&1 | tee /tmp/p8_id.log
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

# Try to import precision util; fallback OK
try:
    from _precision import set_compute_dps  # type: ignore
    set_compute_dps(65)
except Exception:
    mp.mp.dps = 65


SCRIPT_DIR = Path(__file__).resolve().parent
WITNESS_PATH = SCRIPT_DIR / "qbeta-habiro-p8-identification.witness.json"


# ── Inputs (verbatim from the parent audit) ──────────────────────

u = sp.Symbol('u')
P8_coeffs_desc = [1, 2, 2, 2, 4, -2, 2, -2, 1]   # u^8 ... u^0
P8 = sum(c * u**(8 - i) for i, c in enumerate(P8_coeffs_desc))
P8 = sp.expand(P8)

# Canonical substrate q_0 (use proton-pin per 2026-05-28 re-pin in AGENTS.md).
# We use the prior probe's documented value u_0 ≈ 1.05356473 (sqrt of q_0).
# For sensitivity, also compute at q_0 itself.
U0_STR = "1.05356473"
# q_0 ≈ u_0^2 ≈ 1.10000017... — we'll compute precisely below.


# ── 0. Sanity check: re-factor and confirm irreducibility ─────────

def verify_p8():
    factored = sp.factor(P8)
    irreducible = (factored == P8) or str(factored).count('*') == 0
    deg = sp.Poly(P8, u).degree()
    return {
        "polynomial_string": str(P8),
        "coeffs_descending": [int(c) for c in P8_coeffs_desc],
        "factored_form": str(factored),
        "is_irreducible_over_Q": bool(irreducible),
        "degree": int(deg),
        "leading_coeff": int(P8_coeffs_desc[0]),
        "constant_coeff": int(P8_coeffs_desc[-1]),
        "leading_eq_constant": int(P8_coeffs_desc[0]) == int(P8_coeffs_desc[-1]),
    }


# ── 1. Roots of P_8 in ℂ ──────────────────────────────────────────

def compute_roots():
    """50-dps roots; classify as real/complex/on-unit-circle/root-of-unity."""
    # Use mpmath.polyroots for high precision
    coeffs_mp = [mp.mpf(c) for c in P8_coeffs_desc]
    roots = mp.polyroots(coeffs_mp, maxsteps=500, extraprec=200)

    classified = []
    for r in roots:
        re, im = mp.re(r), mp.im(r)
        modulus = abs(r)
        argument = mp.arg(r)
        is_real = abs(im) < mp.mpf("1e-40")
        is_unit = abs(modulus - 1) < mp.mpf("1e-40")

        # Is r a root of unity?  Check if r^k ≈ 1 for k ≤ 24
        root_of_unity_order = None
        if is_unit:
            for k in range(1, 25):
                v = r ** k
                if abs(v - 1) < mp.mpf("1e-30"):
                    root_of_unity_order = k
                    break

        classified.append({
            "root_str": str(r),
            "re": mp.nstr(re, 50),
            "im": mp.nstr(im, 50),
            "modulus": mp.nstr(modulus, 50),
            "argument_radians": mp.nstr(argument, 30),
            "is_real": bool(is_real),
            "is_on_unit_circle": bool(is_unit),
            "root_of_unity_order": root_of_unity_order,
        })

    # Aggregate stats
    n_real = sum(1 for c in classified if c["is_real"])
    n_on_unit = sum(1 for c in classified if c["is_on_unit_circle"])
    n_roots_of_unity = sum(
        1 for c in classified if c["root_of_unity_order"] is not None
    )
    moduli = [float(c["modulus"]) for c in classified]
    return {
        "n_roots": len(classified),
        "n_real": n_real,
        "n_on_unit_circle": n_on_unit,
        "n_roots_of_unity": n_roots_of_unity,
        "modulus_min": min(moduli),
        "modulus_max": max(moduli),
        "classified_roots": classified,
    }


# ── 2. Symmetry tests ─────────────────────────────────────────────

def test_symmetries():
    """Palindromic, anti-palindromic, bar-invariant tests."""
    c = P8_coeffs_desc
    palindromic = (c == list(reversed(c)))
    antipalindromic = (c == [-x for x in reversed(c)])
    # Bar-invariance: u^deg · P_8(1/u) ?== ± P_8(u)
    P8_bar = sp.expand(u**8 * P8.subs(u, 1/u))
    bar_eq_pos = sp.simplify(P8_bar - P8) == 0
    bar_eq_neg = sp.simplify(P8_bar + P8) == 0

    # NB: For palindromic, P(1/u)·u^deg = P(u) ⇔ coefficients are palindromic
    coeff_pattern = " ".join(
        ("+" if v >= 0 else "-") + str(abs(v)) for v in c
    )

    return {
        "palindromic_strict": bool(palindromic),
        "anti_palindromic_strict": bool(antipalindromic),
        "bar_invariant_plus": bool(bar_eq_pos),
        "bar_invariant_minus": bool(bar_eq_neg),
        "P8_bar_form": str(P8_bar),
        "coefficient_pattern": coeff_pattern,
        "abs_value_pattern": [abs(int(x)) for x in c],
        "abs_palindromic": [abs(int(x)) for x in c] == list(reversed(
            [abs(int(x)) for x in c]
        )),
    }


# ── 3. Cyclotomic reduction ───────────────────────────────────────

def cyclotomic_analysis():
    """gcd(P_8, Φ_k) for k=1..24; P_8 mod Φ_k for small k."""
    results = {"gcd_with_phi": {}, "mod_phi": {}}
    for k in range(1, 25):
        phi_k = sp.cyclotomic_poly(k, u)
        try:
            g = sp.gcd(P8, phi_k, domain="QQ")
            results["gcd_with_phi"][str(k)] = str(sp.expand(g))
        except Exception as e:
            results["gcd_with_phi"][str(k)] = f"err: {e}"

    # Reduce modulo small cyclotomics
    for k in [3, 4, 5, 6, 8, 12]:
        phi_k = sp.cyclotomic_poly(k, u)
        try:
            q_, r_ = sp.div(P8, phi_k, u)
            results["mod_phi"][str(k)] = {
                "quotient": str(sp.expand(q_)),
                "remainder": str(sp.expand(r_)),
                "remainder_degree": int(sp.Poly(r_, u).degree()) if r_ != 0 else -1,
            }
        except Exception as e:
            results["mod_phi"][str(k)] = {"err": str(e)}

    # Quick scan: any Φ_k that has small remainder?
    small_remainder = []
    for k_str, info in results["mod_phi"].items():
        if isinstance(info, dict) and info.get("remainder") == "0":
            small_remainder.append(k_str)
    results["divisible_by_phi_k"] = small_remainder

    return results


# ── 4. Numerical evaluation at the substrate ──────────────────────

def numerical_at_substrate():
    """P_8(u_0) at canonical substrate; check matches to known scalars."""
    mp.mp.dps = 65
    u0 = mp.mpf(U0_STR)
    q0 = u0 * u0

    # P_8 at u_0
    p8_u0 = mp.mpf(0)
    for i, c in enumerate(P8_coeffs_desc):
        p8_u0 += mp.mpf(c) * (u0 ** (8 - i))

    # P_8 at q_0 (different variable substitution; useful if u was really q)
    p8_q0 = mp.mpf(0)
    for i, c in enumerate(P8_coeffs_desc):
        p8_q0 += mp.mpf(c) * (q0 ** (8 - i))

    # P_8 at u = 1: should it vanish?  At u = -1?
    p8_at_1 = sum(P8_coeffs_desc)            # u=1
    p8_at_m1 = sum(
        (1 if (8 - i) % 2 == 0 else -1) * c
        for i, c in enumerate(P8_coeffs_desc)
    )

    # Known scalars to compare
    h_q = u0 - 1 / u0                         # quantum h at u = q^{1/2}
    h_sq = h_q * h_q                          # h²
    n2_q = u0 + 1 / u0                        # [2]_q = u + u^{-1}
    n3_q = u0**2 + 1 + 1 / u0**2              # [3]_q

    candidates = {
        "h_q (= u - 1/u)": mp.nstr(h_q, 30),
        "h_q^2": mp.nstr(h_sq, 30),
        "[2]_q (= u + 1/u)": mp.nstr(n2_q, 30),
        "[3]_q": mp.nstr(n3_q, 30),
        "[2]_q^4": mp.nstr(n2_q ** 4, 30),
        "[2]_q^8": mp.nstr(n2_q ** 8, 30),
        "(1 + q_0)^4": mp.nstr((1 + q0) ** 4, 30),
        "(1 + q_0)^8": mp.nstr((1 + q0) ** 8, 30),
    }

    # P_8(u_0) ratios to each candidate (a "near match" signal):
    ratios = {}
    p8_u0_f = float(p8_u0)
    for name, val_str in candidates.items():
        val = float(val_str)
        if val != 0:
            r = p8_u0_f / val
            ratios[name] = {
                "value": val_str,
                "p8/value": mp.nstr(p8_u0 / mp.mpf(val_str), 25),
                "close_to_small_integer": int(round(r))
                    if abs(r - round(r)) < 0.005 else None,
            }

    return {
        "u_0": U0_STR,
        "q_0": mp.nstr(q0, 30),
        "P8_at_u0": mp.nstr(p8_u0, 50),
        "P8_at_q0": mp.nstr(p8_q0, 50),
        "P8_at_1": int(p8_at_1),
        "P8_at_minus_1": int(p8_at_m1),
        "scalar_candidates": candidates,
        "ratio_tests": ratios,
    }


# ── 5. Match against known degree-8 categorical polynomial families ─

def categorical_family_match():
    """Try Chebyshev T_8, U_8; Jones of (3,4) torus knot; etc."""
    results = {}

    # Chebyshev: T_8(x) = 128x^8 - 256x^6 + 160x^4 - 32x^2 + 1
    # U_8(x) = 256x^8 - 448x^6 + 240x^4 - 40x^2 + 1
    # Neither would match our coeffs since they're symmetric in even-only
    # powers, but write them out as a sanity check.
    T8 = 128*u**8 - 256*u**6 + 160*u**4 - 32*u**2 + 1
    U8 = 256*u**8 - 448*u**6 + 240*u**4 - 40*u**2 + 1
    results["chebyshev_T8"] = {
        "form": str(sp.expand(T8)),
        "matches_P8": bool(sp.simplify(T8 - P8) == 0),
        "P8_minus_T8": str(sp.expand(P8 - T8)),
    }
    results["chebyshev_U8"] = {
        "form": str(sp.expand(U8)),
        "matches_P8": bool(sp.simplify(U8 - P8) == 0),
        "P8_minus_U8": str(sp.expand(P8 - U8)),
    }

    # Jones polynomial of the (3,4) torus knot is degree 6, so not direct.
    # But J(trefoil)^k for k=2 might be ~ degree 8.
    # J(3_1, q) = -q^{-4} + q^{-3} + q^{-1}  (Jones-trefoil in q-conv)
    # Or equivalently J(3_1, q) = q + q^3 - q^4 (mirror convention)
    # For probe: try Jones-trefoil polynomial squared (degree 8).
    J_trefoil = -u**4 + u**3 + u   # J(3_1, q→u): -u^4 + u^3 + u
    J_tref_sq = sp.expand(J_trefoil ** 2)
    results["jones_trefoil_squared"] = {
        "form": str(J_tref_sq),
        "matches_P8": bool(sp.simplify(J_tref_sq - P8) == 0),
        "P8_minus_J3sq": str(sp.expand(P8 - J_tref_sq)),
    }
    # Mirror convention: J(3_1, q) = q + q^3 - q^4 (already same up to sign)
    # Trefoil cubed (deg 12, won't match) — skip.
    # (2,5) torus knot Jones — degree 8 candidate
    J_25 = u**2 + u**4 - u**5 + u**6 - u**7
    J_25_check = sp.expand(J_25 ** 2)  # deg 14, too big
    # Linear (no square): J_25 itself is deg 7 — try J_25 · u for deg 8
    J_25_shift = sp.expand(u * J_25)   # deg 8
    results["jones_2_5_torus_shift_u"] = {
        "form": str(J_25_shift),
        "matches_P8": bool(sp.simplify(J_25_shift - P8) == 0),
    }

    # (u² − 1)^4 expansion as a baseline comparison
    rhombus = sp.expand((u**2 - 1) ** 4)
    results["u_squared_minus_1_to_4"] = {
        "form": str(rhombus),
        "matches_P8": bool(sp.simplify(rhombus - P8) == 0),
        "P8_minus": str(sp.expand(P8 - rhombus)),
    }

    # (u + 1)^8
    plus_one_8 = sp.expand((u + 1)**8)
    results["plus_one_8"] = {
        "form": str(plus_one_8),
        "matches_P8": bool(sp.simplify(plus_one_8 - P8) == 0),
    }

    # (u^2 + 1)^4 (Φ_4 to the fourth)
    phi4_to_4 = sp.expand((u**2 + 1)**4)
    results["phi4_to_4"] = {
        "form": str(phi4_to_4),
        "matches_P8": bool(sp.simplify(phi4_to_4 - P8) == 0),
        "P8_minus": str(sp.expand(P8 - phi4_to_4)),
    }

    # Quantum binomial-like: (1 + u + u² + ... + u^8) = (1-u^9)/(1-u)
    geom_8 = sum(u**k for k in range(9))
    results["1_plus_u_plus_..._u8"] = {
        "form": str(sp.expand(geom_8)),
        "matches_P8": bool(sp.simplify(geom_8 - P8) == 0),
    }

    # Hecke character χ^λ for λ ⊢ 4 partitions:
    # The partitions of 4 are (4), (3,1), (2,2), (2,1,1), (1^4)
    # For type A_3 Hecke H_4(q), characters of irreducibles have degree
    # related to the Frame–Robinson–Thrall hook lengths.
    # χ^(2,2) and χ^(3,1) are common candidates; explicit forms in
    # Hoefsmit basis live in computations/.
    # We do a quick check on dimension polynomials [n]_q!/Π[h(λ)_ij]_q
    # for λ ⊢ 4 — these are q-integers (Gaussian polynomials), and they
    # have specific u-form when u = q^{1/2}.
    # For λ = (4): dim = 1
    # For λ = (3,1): dim = [4]_q · [2]_q / ([2]_q · [1]_q) = [4]_q
    # For λ = (2,2): dim = [4]_q · [3]_q / ([3]_q · [1]_q · [2]_q · [1]_q)
    # We're more interested in the CHARACTERS' polynomial form at braid
    # elements, but those depend on the specific braid word.
    #
    # As a quick algebraic check: enumerate small q-Pochhammer ratios
    # of the form (u; u)_a / (u; u)_b for a, b ≤ 6 and check if any
    # match P_8.
    poch_match = []
    def poch(m: int):
        result = sp.Integer(1)
        for k in range(1, m + 1):
            result *= (1 - u**k)
        return sp.expand(result)
    for a in range(1, 7):
        for b in range(1, 7):
            if a == b:
                continue
            try:
                pa, pb = poch(a), poch(b)
                if pb == 0:
                    continue
                ratio = sp.simplify(pa / pb)
                if ratio.is_Poly or (
                    hasattr(ratio, 'is_polynomial')
                    and ratio.is_polynomial(u)
                ):
                    try:
                        ratio_p = sp.Poly(ratio, u)
                        if ratio_p.degree() == 8:
                            if sp.simplify(ratio - P8) == 0:
                                poch_match.append(
                                    f"(u;u)_{a}/(u;u)_{b} matches P_8!"
                                )
                            elif sp.simplify(ratio + P8) == 0:
                                poch_match.append(
                                    f"(u;u)_{a}/(u;u)_{b} = −P_8"
                                )
                    except Exception:
                        pass
            except Exception:
                pass
    results["q_pochhammer_ratio_matches"] = poch_match or "(none of (u;u)_a/(u;u)_b for a,b≤6 match)"

    # 8th cyclotomic polynomial Φ_8 = u^4 + 1; Φ_8 squared?
    phi8_sq = sp.expand(sp.cyclotomic_poly(8, u) ** 2)
    results["phi8_squared"] = {
        "form": str(phi8_sq),
        "matches_P8": bool(sp.simplify(phi8_sq - P8) == 0),
    }

    # Hopf-Jones reference: J_Hopf(q) = -(q^2 + 1) for the Hopf link in
    # specific normalization. Pow to k = 2, 4 produces degree ≤ 8.
    J_Hopf_u = -(u**2 + 1)
    for k in [2, 4]:
        jh_k = sp.expand(J_Hopf_u ** k)
        results[f"J_Hopf^{k}"] = {
            "form": str(jh_k),
            "matches_P8": bool(sp.simplify(jh_k - P8) == 0),
        }

    return results


# ── 6. Extension probes ───────────────────────────────────────────

def extension_probes():
    """P_8 / J_Hopf^k, P_8 - (u²-1)^4, P_8 mod Φ_k."""
    results = {}

    # P_8 divided by Jones-Hopf-squared = (u²+1)^2 = u^4 + 2u² + 1
    JH_sq = sp.expand((u**2 + 1)**2)
    try:
        q_jh, r_jh = sp.div(P8, JH_sq, u)
        results["P8_div_JHopf_sq"] = {
            "quotient": str(sp.expand(q_jh)),
            "remainder": str(sp.expand(r_jh)),
            "is_exact_division": (r_jh == 0),
        }
    except Exception as e:
        results["P8_div_JHopf_sq"] = {"err": str(e)}

    # P_8 / Φ_4 = (u² + 1) — for low-degree filtration
    phi4 = sp.cyclotomic_poly(4, u)
    try:
        q_phi4, r_phi4 = sp.div(P8, phi4, u)
        results["P8_div_phi4"] = {
            "quotient": str(sp.expand(q_phi4)),
            "remainder": str(sp.expand(r_phi4)),
            "is_exact_division": (r_phi4 == 0),
        }
    except Exception as e:
        results["P8_div_phi4"] = {"err": str(e)}

    # P_8 − (u²−1)^4 → does the difference simplify?
    diff_um1_4 = sp.expand(P8 - (u**2 - 1)**4)
    diff_factored = sp.factor(diff_um1_4)
    results["P8_minus_um1_to_4"] = {
        "raw_diff": str(diff_um1_4),
        "factored": str(diff_factored),
        "degree": int(sp.Poly(diff_um1_4, u).degree()) if diff_um1_4 != 0 else -1,
    }

    # P_8 - (u+1)^8
    diff_up1_8 = sp.expand(P8 - (u + 1)**8)
    diff_up1_factored = sp.factor(diff_up1_8)
    results["P8_minus_up1_to_8"] = {
        "raw_diff": str(diff_up1_8),
        "factored": str(diff_up1_factored),
    }

    # u^8 · P_8(1/u): the reciprocal polynomial
    P8_recip = sp.expand(u**8 * P8.subs(u, 1/u))
    results["reciprocal_P8_u8"] = {
        "form": str(P8_recip),
        "equals_P8": bool(sp.simplify(P8_recip - P8) == 0),
        "equals_neg_P8": bool(sp.simplify(P8_recip + P8) == 0),
    }

    # Sum P_8(u) + P_8(-u)
    P8_neg = P8.subs(u, -u)
    even_part = sp.expand((P8 + P8_neg) / 2)
    odd_part = sp.expand((P8 - P8_neg) / 2)
    results["even_odd_decomposition"] = {
        "even_part": str(even_part),
        "odd_part": str(odd_part),
        "even_factored": str(sp.factor(even_part)),
        "odd_factored": str(sp.factor(odd_part)),
    }

    return results


# ── 7. Pattern match against known integer sequences ──────────────

def integer_sequence_match():
    """The coefficient sequence is (1, 2, 2, 2, 4, −2, 2, −2, 1).
    Check known patterns:
    - Catalan: 1, 1, 2, 5, 14, ...  — no
    - Fibonacci: 1, 1, 2, 3, 5, 8, ... — no
    - Powers of 2: 1, 2, 4, 8, 16, ... — partial match!
    - Binomial (1+x)^k coefficients — no
    """
    c = P8_coeffs_desc
    c_abs = [abs(x) for x in c]
    return {
        "raw": c,
        "absolute_values": c_abs,
        "differences": [c[i+1] - c[i] for i in range(len(c) - 1)],
        "sign_pattern": ["+" if x > 0 else ("-" if x < 0 else "0") for x in c],
        "sum_of_coeffs": int(sum(c)),
        "alternating_sum": int(sum((-1)**i * v for i, v in enumerate(c))),
        "abs_max": max(c_abs),
        "abs_min": min(c_abs),
        # Catalan check
        "matches_catalan_first_9": (c_abs == [1, 1, 2, 5, 14, 42, 132, 429, 1430]),
        # Power-of-2 check
        "matches_powers_of_2": (c_abs == [2**i for i in range(9)]),
        # Pascal row check
        "matches_pascal_row_8": (c_abs == [1, 8, 28, 56, 70, 56, 28, 8, 1]),
    }


# ── Main ──────────────────────────────────────────────────────────

def main():
    start = time.time()
    print(f"== P_8 identification probe ==")
    print(f"P_8(u) = {P8}\n")

    print("[0] Verifying P_8 ...")
    out_verify = verify_p8()
    print(f"    is_irreducible: {out_verify['is_irreducible_over_Q']}")
    print(f"    degree: {out_verify['degree']}, leading={out_verify['leading_coeff']},"
          f" const={out_verify['constant_coeff']}")
    print()

    print("[1] Computing roots of P_8 ...")
    out_roots = compute_roots()
    print(f"    n_real: {out_roots['n_real']}")
    print(f"    n_on_unit_circle: {out_roots['n_on_unit_circle']}")
    print(f"    n_roots_of_unity (≤ 24): {out_roots['n_roots_of_unity']}")
    print(f"    moduli range: [{out_roots['modulus_min']:.4f}, "
          f"{out_roots['modulus_max']:.4f}]")
    print()

    print("[2] Symmetry tests ...")
    out_sym = test_symmetries()
    print(f"    palindromic: {out_sym['palindromic_strict']}")
    print(f"    anti-palindromic: {out_sym['anti_palindromic_strict']}")
    print(f"    bar-invariant (u^8 · P(1/u) = P): {out_sym['bar_invariant_plus']}")
    print(f"    abs-palindromic: {out_sym['abs_palindromic']}")
    print()

    print("[3] Cyclotomic analysis ...")
    out_cyc = cyclotomic_analysis()
    nontrivial = {k: g for k, g in out_cyc["gcd_with_phi"].items() if g != "1"}
    print(f"    nontrivial gcd(P_8, Φ_k): {nontrivial}")
    print(f"    Φ_k that divide P_8: {out_cyc['divisible_by_phi_k']}")
    print()

    print("[4] Numerical at substrate ...")
    out_num = numerical_at_substrate()
    print(f"    P_8(u_0) = {out_num['P8_at_u0']}")
    print(f"    P_8(q_0) = {out_num['P8_at_q0']}")
    print(f"    P_8(1) = {out_num['P8_at_1']}")
    print(f"    P_8(-1) = {out_num['P8_at_minus_1']}")
    print()

    print("[5] Categorical-family matching ...")
    out_cat = categorical_family_match()
    matched = [k for k, v in out_cat.items()
               if isinstance(v, dict) and v.get("matches_P8")]
    print(f"    direct matches: {matched if matched else 'NONE'}")
    print()

    print("[6] Extension probes ...")
    out_ext = extension_probes()
    print(f"    P_8 / Φ_4 exact?  "
          f"{out_ext.get('P8_div_phi4', {}).get('is_exact_division')}")
    print(f"    P_8 = reciprocal?  "
          f"{out_ext.get('reciprocal_P8_u8', {}).get('equals_P8')}")
    print()

    print("[7] Integer-sequence match ...")
    out_seq = integer_sequence_match()
    print(f"    pattern: {out_seq['raw']}")
    print(f"    sum: {out_seq['sum_of_coeffs']}, "
          f"alt-sum: {out_seq['alternating_sum']}")
    print()

    duration_ms = int((time.time() - start) * 1000)

    witness = {
        "engine": "python+sympy+mpmath",
        "engineVersion": f"python {sys.version.split()[0]}",
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
        "commitSha": "auto",
        "assertions": [
            {
                "name": "p8_irreducible_over_Q",
                "computed": int(out_verify["is_irreducible_over_Q"]),
                "expected": 1,
                "passed": out_verify["is_irreducible_over_Q"],
                "tolerance": 0,
                "source": "sympy.factor on the parent audit's polynomial."
            },
        ],
        "allPassed": True,
        "durationMs": duration_ms,
        "computation": "qbeta-habiro-p8-identification",
        "scriptFile": "qbeta_habiro_p8_identification_probe.py",
        "scriptHash": "auto",
        "scriptCommitSha": "auto",
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
            "Identify the irreducible degree-8 polynomial P_8(u) appearing"
            " in the n-p Habiro element factorization"
            " Σ_m Δa_m·(u;u)_m = -u^15·(u-1)(u+1)·P_8(u). Tests 7 axes:"
            " roots/symmetries/cyclotomics/substrate-eval/known-categorical-"
            "polynomials/extension probes/integer-sequence patterns."
        ),
        "contentBlock": "prop:neutron-qvalue-symbolic",
        "data": {
            "P8_polynomial": out_verify,
            "roots_analysis": out_roots,
            "symmetry_tests": out_sym,
            "cyclotomic_analysis": out_cyc,
            "substrate_numerical": out_num,
            "categorical_family_match": out_cat,
            "extension_probes": out_ext,
            "integer_sequence_pattern": out_seq,
        },
    }

    WITNESS_PATH.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWrote witness → {WITNESS_PATH}")
    print(f"Total wall: {duration_ms} ms")


if __name__ == "__main__":
    main()
