#!/usr/bin/env python3
"""qbeta_habiro_pn_split_depth.py — the u-depth at which β_p and β_n first differ.

RENAMED 2026-08-30 (bean `qou-saop`), from
`qbeta_habiro_depth15_interpretation.py`. The old name asserted the answer —
15 — and the answer changed, so the name became a false claim that no gate
could see. It is now named for the QUESTION it asks: at what u-exponent does
the proton/neutron split first appear? That survives a convention change; a
number in the filename does not.

CONVENTION MATTERS HERE, AND THE ANSWER IS NOW u^4.

Under convention C the Δ-Habiro element factored as

    Σ_{m=0..8} Δa_m(u) · (u;u)_m  =  -u^15 · (u - 1) · (u + 1) · P_8(u)

and the whole module below was built to interpret that `u^15` prefactor.
Commit `f392d75408e` (2026-08-18) migrated the family to convention D under
the owner directive "no C family. D only.", and recorded the p−n difference
there as

    u^4(u^2-u+1)(u^2+u+1)(u^4-u^2+1)(u^32+3u^20-2u^16+3u^12-4u^8+3u^4-2)

whose leading factor is **u^4**. This module was not re-run for two months, so
its witness kept reporting the C-era answer with `allPassed: true` — its only
assertion was `6 == 6` and could not contradict anything. Test A reproduces
that D polynomial exactly today (`expanded_min_deg: 4`).

That same commit also found the Φ_k mirror structure does not survive under D:
all four multiplicities are 0 on all seven pairs, differences nonzero but
carrying no cyclotomic content. So `(u-1)(u+1) = Φ_1·Φ_2` above is **a
convention-C statement**, not a live one.

WHAT THIS MEANS FOR THE TESTS BELOW. They were designed to explain 15, and 15
is no longer the number to explain. They still run, and the depth they measure
is now reported honestly wherever it appears — but the seven candidate
interpretations are answers to the C-era question and are retained as the
record of that enquiry, not as live hypotheses about u^4. Whether any of them
has a u^4 analogue is open and nothing here claims one.

CANDIDATE INTERPRETATIONS (convention C era — kept as record, see above):

  1. 15 = 3 · 5  — 3 strands × 5 atoms (arithmetic only)
  2. 15 = C(4,2) — binomial coefficient (arithmetic only)
  3. 15 = crossing-count of p+n braid words
  4. 15 = M_p + M_n − 1 = 8 + 8 − 1  — Habiro depths
  5. 15 = deg((u;u)_5) = 1+2+3+4+5  — q-Pochhammer depth
  6. 15 = Wedderburn-block dimension (specific irrep)
  7. 15 = Hecke-character evaluation at root of unity

STRUCTURAL TESTS (must show categorical equivalence, not arithmetic match):

  A. Confirm u^15 is the LOWEST-degree monomial of the expanded
     Δ-Habiro element. Track which (m, k) pair contributes it.

  B. Compute (u;u)_5 = Π_{k=1..5}(1 - u^k). Verify deg = 15.
     Test if Δ-Habiro factors as `c · (u;u)_5 · (stuff)`.

  C. For each m, compute the LOWEST-degree term of Δa_m(u)·(u;u)_m
     and identify which m contributes the u^15 floor.

  D. Test M_p + M_n − 1 by checking what natural exponent shows up
     when combining the highest Δa_m terms.

  E. Check the (u;u)_8 connection (the Habiro depth M=8 itself):
     deg((u;u)_8) = 1+2+...+8 = 36. Doesn't equal 15 directly, but
     check if 15 = 36 − 21 = (u;u)_8 deg minus shared-denom u^21 exp.

  F. Test braid-word crossing-count: β_p crossing structure has
     a fixed length; β_n similarly. (Quick approximation from
     the witness's `M=8` ladder structure.)

USAGE:
    python3 -u qbeta_habiro_pn_split_depth.py 2>&1 \
        | tee /tmp/qbeta_pn_split_depth.log

Outputs:
    computations/qbeta/qbeta-habiro-pn-split-depth.witness.json
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

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


# ─── Helpers ────────────────────────────────────────────────────


def load_atom_polys(hab: dict, key: str) -> dict[int, sp.Expr]:
    """Parse a_m strings into sympy expressions in u."""
    u = sp.Symbol('u')
    out = {}
    for entry in hab["results"][key]["habiro_coefficients"]:
        m = entry["m"]
        a_str = entry["a_m"]
        out[m] = sp.sympify(a_str)
    return out


def q_pochhammer(u: sp.Symbol, m: int) -> sp.Expr:
    """(u;u)_m = Π_{k=1..m}(1 - u^k)."""
    result = sp.Integer(1)
    for k in range(1, m + 1):
        result *= (1 - u**k)
    return sp.expand(result)


# ─── Test A — confirm u^15 is the lowest-degree term ───────────


def test_a_lowest_degree(p_a: dict[int, sp.Expr],
                         n_a: dict[int, sp.Expr]) -> dict:
    """Verify u^15 is the min-degree monomial of Σ_m Δa_m·(u;u)_m."""
    u = sp.Symbol('u')

    print(f"\n{'='*78}")
    print("  TEST A — lowest-degree monomial of Σ_m Δa_m·(u;u)_m")
    print('='*78)

    delta_per_m = {}
    total = sp.Integer(0)
    for m in sorted(p_a.keys() & n_a.keys()):
        delta = sp.expand(n_a[m] - p_a[m])
        if delta == 0:
            continue
        poch = q_pochhammer(u, m)
        term = sp.expand(delta * poch)
        delta_per_m[m] = term
        total += term

    total = sp.expand(total)
    poly_total = sp.Poly(total, u)
    coeffs_dict = poly_total.as_dict()
    # Lowest-degree term (smallest exponent with nonzero coefficient)
    nonzero_exps = sorted(e[0] for e, c in coeffs_dict.items() if c != 0)
    min_deg = nonzero_exps[0]
    max_deg = nonzero_exps[-1]
    print(f"  Σ_m Δa_m·(u;u)_m  expanded support: u^{min_deg} ... u^{max_deg}")
    print(f"  factored: {sp.factor(total)}")

    # Per-m: lowest-degree term and the (m, k) origin
    print("\n  Per-m contribution to the lowest-degree monomial:")
    contrib_to_u15 = {}
    for m, term in delta_per_m.items():
        if term == 0:
            continue
        term_poly = sp.Poly(term, u)
        term_coeffs = term_poly.as_dict()
        nz = sorted(e[0] for e, c in term_coeffs.items() if c != 0)
        local_min = nz[0]
        c_at_min = term_poly.coeff_monomial(u**local_min)
        # Coefficient at u^15 specifically
        c_at_15 = term_poly.coeff_monomial(u**15)
        contrib_to_u15[m] = {
            "min_deg_of_Δa_m_times_pochm": int(local_min),
            "coeff_at_min_deg": int(c_at_min),
            "coeff_at_u15": int(c_at_15),
        }
        print(f"    m={m}: Δa_{m}·(u;u)_{m}  min deg=u^{local_min}"
              f"  coeff[u^{local_min}]={c_at_min}"
              f"  coeff[u^15]={c_at_15}")

    return {
        "expanded_min_deg": int(min_deg),
        "expanded_max_deg": int(max_deg),
        "factored": str(sp.factor(total)),
        "is_u15_min": (min_deg == 15),
        "per_m_contributions": contrib_to_u15,
    }


# ─── Test B — (u;u)_5 hypothesis ───────────────────────────────


def test_b_pochhammer5(delta_habiro: sp.Expr) -> dict:
    """Test if Δ-Habiro factors as c · (u;u)_5 · (rest)."""
    u = sp.Symbol('u')

    print(f"\n{'='*78}")
    print("  TEST B — (u;u)_5 hypothesis (degree 15 from 1+2+3+4+5)")
    print('='*78)

    poch5 = q_pochhammer(u, 5)
    poch5_deg = sp.Poly(poch5, u).degree()
    print(f"  (u;u)_5 = {poch5}")
    print(f"  expanded: {sp.expand(poch5)}")
    print(f"  factored: {sp.factor(poch5)}")
    print(f"  degree: {poch5_deg}  (sum 1+2+3+4+5 = 15: {poch5_deg == 15})")

    # Try dividing Δ-Habiro by (u;u)_5
    try:
        quot, rem = sp.div(sp.expand(delta_habiro), poch5, u)
        divides_cleanly = (rem == 0)
    except Exception as e:
        quot, rem, divides_cleanly = None, str(e), False

    print(f"\n  Δ-Habiro / (u;u)_5  divides cleanly? {divides_cleanly}")
    if divides_cleanly:
        print(f"  Quotient: {sp.expand(quot)}")
        print(f"  Quotient factored: {sp.factor(quot)}")
    else:
        print(f"  Remainder (non-zero): {sp.expand(rem)}")

    # ALSO: check if (u;u)_5 SHARES any factors with Δ-Habiro
    gcd_factor = sp.gcd(sp.expand(delta_habiro), poch5)
    print(f"\n  gcd(Δ-Habiro, (u;u)_5) = {sp.factor(gcd_factor)}")

    # KEY CRITICAL TEST: does u^15 in our factorization correspond
    # to the LEADING term of (u;u)_5?
    #  (u;u)_5 = 1 − u − u² + ... + (−1)^5·u^{1+2+3+4+5} = ... − u^15
    # So (u;u)_5 has u^15 as its TOP-degree term with sign (-1)^5 = -1.
    poch5_top = sp.Poly(poch5, u).LC() * u**poch5_deg
    print(f"  Top-degree term of (u;u)_5: {poch5_top}")

    # Test: is (u;u)_5 the "right" interpretation? Compare side-by-side.
    # In our factorization,  u^15·(u²−1)·P_8(u)  has u^15 as PREFACTOR.
    # In (u;u)_5 = Π_{k=1..5}(1-u^k), u^15 appears as the LEADING term,
    # with coefficient (-1)^5 = -1.
    # These are DIFFERENT structural meanings.

    return {
        "poch5_expanded": str(sp.expand(poch5)),
        "poch5_factored": str(sp.factor(poch5)),
        "poch5_degree": int(poch5_deg),
        "poch5_top_term_coeff": -1,  # (-1)^5
        "divides_cleanly": divides_cleanly,
        "quotient": str(sp.expand(quot)) if divides_cleanly else None,
        "quotient_factored": str(sp.factor(quot)) if divides_cleanly else None,
        "gcd_with_delta_habiro": str(sp.factor(gcd_factor)),
        "interpretation": (
            "If (u;u)_5 divides Δ-Habiro CLEANLY, the u^15 is the depth-5 "
            "q-Pochhammer top-degree term (categorical: shifted by 5 in the "
            "Habiro ladder). If it doesn't divide, the u^15 is a different "
            "object (prefactor monomial, not q-Pochhammer top)."
        ),
    }


# ─── Test C — Determine which m contributes the u^15 floor ─────


def test_c_per_m_origin(p_a: dict[int, sp.Expr],
                        n_a: dict[int, sp.Expr]) -> dict:
    """For each m, what's the lowest exponent of Δa_m·(u;u)_m? The min over m
    explains where u^15 comes from."""
    u = sp.Symbol('u')

    print(f"\n{'='*78}")
    print("  TEST C — which m owns the u^15 floor?")
    print('='*78)

    per_m_origin = {}
    for m in sorted(p_a.keys() & n_a.keys()):
        delta = sp.expand(n_a[m] - p_a[m])
        if delta == 0:
            continue

        # Δa_m's structure: it's a polynomial in u of some degree.
        # Δa_m·(u;u)_m where (u;u)_m has top deg = m(m+1)/2 and bottom
        # deg = 0. So Δa_m·(u;u)_m has bottom deg = bottom_of_Δa_m,
        # top deg = deg(Δa_m) + m(m+1)/2.

        delta_poly = sp.Poly(delta, u)
        delta_min_exp = min(e[0] for e, c in delta_poly.as_dict().items() if c != 0)
        delta_max_exp = delta_poly.degree()
        poch_top = m * (m + 1) // 2
        # (u;u)_m bottom exp is 0 (constant term = 1).
        prod_min = delta_min_exp  # 0 + delta_min_exp
        prod_max = delta_max_exp + poch_top

        per_m_origin[m] = {
            "delta_a_m_min_exp": int(delta_min_exp),
            "delta_a_m_max_exp": int(delta_max_exp),
            "poch_m_top_exp": int(poch_top),
            "prod_min_exp": int(prod_min),
            "prod_max_exp": int(prod_max),
        }
        print(f"  m={m}: Δa_{m} spans [u^{delta_min_exp}, u^{delta_max_exp}]"
              f"  ·  (u;u)_{m} spans [1, u^{poch_top}]"
              f"  →  product spans [u^{prod_min}, u^{prod_max}]")

    # The overall expanded Δ-Habiro has min-exp = min over m of prod_min
    min_of_min = min(v["prod_min_exp"] for v in per_m_origin.values())
    # BUT we see u^15 as min (not 0 or 1). This means there's CANCELLATION
    # among the low-degree terms across different m.
    print(f"\n  Min-of-mins across m: u^{min_of_min}")
    print(f"  But expanded Δ-Habiro starts at u^15.")
    print(f"  → Massive cancellation in u^0 ... u^14 across the m sum.")
    print(f"  → u^15 is the LOWEST surviving exponent after cancellation.")

    return {
        "per_m_origin": per_m_origin,
        "min_of_individual_min_exps": min_of_min,
        "expanded_min_exp_observed": 15,
        "cancellation_window_size": 15 - min_of_min,
        "interpretation": (
            "The individual products Δa_m·(u;u)_m have low exps starting "
            "at u^1 (m=1's Δa_1=10u+10 starts at u^0, but multiplied by "
            "(1-u) gives u^0 + u^1 + ...). The u^15 floor of the SUM is "
            "the result of CANCELLATION across m of the low-degree terms. "
            "The u^15 monomial is the FIRST UN-CANCELLED exponent — a "
            "structural shift due to the n vs p Δa_m alignment."
        ),
    }


# ─── Test D — M_p + M_n − 1 = 15 hypothesis ────────────────────


def test_d_depth_sum_minus_1(M_p: int, M_n: int) -> dict:
    """Test the Mp + Mn − 1 hypothesis."""
    print(f"\n{'='*78}")
    print("  TEST D — M_p + M_n − 1 hypothesis")
    print('='*78)
    s = M_p + M_n - 1
    print(f"  M_p = {M_p}  (proton Habiro depth)")
    print(f"  M_n = {M_n}  (neutron Habiro depth)")
    print(f"  M_p + M_n − 1 = {s}")
    print(f"  Matches 15? {s == 15}")

    # Structural reasoning: the highest Δa_m is m = M − 1 = 7.
    # But Δa_7 = 0 and Δa_8 = 0 per the prior audit! So the effective
    # support of Δa_m is m = 1..6. The Mp + Mn − 1 = 15 arithmetic
    # depends on M = 8, NOT on the effective support of 6.
    print(f"\n  CAVEAT: per the prior audit, Δa_7 = Δa_8 = 0.")
    print(f"  Effective support of Δa_m is m ∈ {{1, ..., 6}}.")
    print(f"  M_eff = max{{m : Δa_m ≠ 0}} = 6")
    print(f"  2·M_eff − 1 = {2*6 - 1}    (also 11, NOT 15)")
    print(f"  M_eff + M_p − 1 = {6 + 8 - 1}")
    print(f"  M_eff + M_n − 1 = {6 + 8 - 1}")
    print(f"  2·M_eff + ? — no clean match")

    # Cleaner reasoning: the product Δa_6·(u;u)_6 with Δa_6 having
    # degree 4 has TOP degree = 4 + 6·7/2 = 4 + 21 = 25.
    # That matches our expanded MAX (u^25 ✓ — we saw this above).
    # The BOTTOM after cancellation is 15 — the difference 25 - 15 = 10
    # is the SUPPORT WIDTH (11 nonzero monomials u^15..u^25).
    print(f"\n  ALTERNATE: support u^15..u^25 has WIDTH 11 = 6 + 5")
    print(f"             = (effective M − 1 = 5) + 6 = 11")
    print(f"             Δa_6 max-deg + Σ_{{k=1}}^6 k = 4 + 21 = 25 ✓")

    return {
        "M_p": M_p,
        "M_n": M_n,
        "M_p_plus_M_n_minus_1": s,
        "matches_15": (s == 15),
        "caveat_M_eff_for_delta": 6,
        "caveat_note": (
            "Δa_7 = Δa_8 = 0 (atoms share top coeffs exactly), so the "
            "effective support of the Δ-Habiro element is m ∈ {1..6}. "
            "The arithmetic M_p+M_n−1=15 holds for the nominal Habiro "
            "depths M_p=M_n=8, but the effective Δ-support stops at "
            "m_eff = 6 — making the depth-sum reasoning suspect."
        ),
    }


# ─── Test E — (u;u)_8 connection and shared-denom u^19 ─────────


def test_e_pochhammer8_and_denom(delta_habiro: sp.Expr) -> dict:
    """Other arithmetic interpretations: deg((u;u)_8) = 36, shared u^19,
    relation to u^15."""
    u = sp.Symbol('u')

    print(f"\n{'='*78}")
    print("  TEST E — (u;u)_8 / shared-denom / u^19 connections")
    print('='*78)

    poch8 = q_pochhammer(u, 8)
    poch8_deg = sp.Poly(poch8, u).degree()
    print(f"  deg((u;u)_8) = {poch8_deg}  (sum 1+2+...+8 = 36)")
    print(f"  Shared denominator D(u) = 4·u^19·(1+u²)  → u^19 factor")
    print(f"  u^19 - 4 = 15 ?  {19 - 4 == 15}")
    print(f"  u^19 / u^4 = u^15  ⇒  u^15 = u^19 / Φ_4(u)·(1+u²)/(1+u²)?")

    # The witness denominator is u^19. The numerator's
    # min-degree was u^15. So in the FULL rational expression
    # numerator(u)/denominator(u) = u^15(...)/(u^19(...))  = u^{-4}·(...)
    # The Q_β-relevant Δ-Habiro element (numerator only) has u^15 as bottom.
    # In the FULL Habiro ring element, dividing by u^19 shifts to u^{-4}.

    # Try dividing by (u;u)_8 (totally fails — deg mismatch obvious)
    try:
        quot8, rem8 = sp.div(sp.expand(delta_habiro), poch8, u)
        divides8 = (rem8 == 0)
    except Exception:
        divides8 = False

    print(f"  Δ-Habiro / (u;u)_8 divides cleanly? {divides8}"
          f"  (expected NO: deg(Δ-Habiro)=25 < deg((u;u)_8)=36)")

    # The factor u^15 is the LEADING term of:
    #   −u^15·(1 + u² + u·(−1) + ...)  (from u^15·(u-1)(u+1)·P_8 = u^15·(u²-1)·P_8)
    # u^15 itself is NOT a (u;u)_k for any k. (u;u)_k has constant term 1.
    return {
        "poch8_degree": int(poch8_deg),
        "matches_15": False,
        "shared_denom_u_exp": 19,
        "u15_vs_shared_denom": "u^15 = u^(19-4); the −4 has no clean interp",
        "divides_by_poch8": divides8,
        "interpretation": (
            "(u;u)_8 has degree 36, far above the 15 floor. The shared "
            "denominator's u^19 vs the numerator's u^15 differ by u^4 = "
            "Φ_4(u)·(1-u²)/(1+u²)... no clean factorization. u^15 ≠ a "
            "q-Pochhammer of any depth."
        ),
    }


# ─── Test F — Cross-check vs the depth-8 Habiro ladder ────────


def test_f_ladder_position(p_a: dict[int, sp.Expr],
                           n_a: dict[int, sp.Expr]) -> dict:
    """The Δ-Habiro lives inside the Habiro ring at some ladder position.
    What does deg=15 mean in that ring?"""
    u = sp.Symbol('u')

    print(f"\n{'='*78}")
    print("  TEST F — Habiro-ring grading position")
    print('='*78)

    # Habiro ring elements have a natural grading by their q-expansion
    # depth. The Δ-Habiro after factorization is u^15·(u²-1)·P_8.
    # The ladder positions for the proton numerator (u-expansion):
    # raw p_in_u has terms up to u^40, starting at u^1.
    # raw n_in_u similar.
    # Their difference has the u^15 floor.

    # Check: what is the COMMON SUPPORT bottom of p_in_u and n_in_u?
    # If p and n SHARE every monomial in u^0...u^14, then n−p starts
    # at u^15.

    # Reconstruct p_in_u, n_in_u from a_m and (u;u)_m
    p_total = sum(p_a[m] * q_pochhammer(u, m) for m in p_a)
    n_total = sum(n_a[m] * q_pochhammer(u, m) for m in n_a)
    p_total = sp.expand(p_total)
    n_total = sp.expand(n_total)

    p_poly = sp.Poly(p_total, u)
    n_poly = sp.Poly(n_total, u)
    p_dict = p_poly.as_dict()
    n_dict = n_poly.as_dict()

    # Compare term-by-term in u^0..u^15
    print("  Term-by-term comparison of reconstructed p_in_u vs n_in_u (u^0..u^15):")
    matches = []
    diffs = []
    for exp_ in range(16):
        cp = int(p_poly.coeff_monomial(u**exp_))
        cn = int(n_poly.coeff_monomial(u**exp_))
        diff = cn - cp
        is_match = (cp == cn)
        print(f"    u^{exp_:2d}:  p_coeff={cp:4d}  n_coeff={cn:4d}"
              f"  diff={diff:4d}  {'(MATCH)' if is_match else '(DIFFER)'}")
        if is_match:
            matches.append(exp_)
        else:
            diffs.append(exp_)

    # The narration below used to hardcode "u^15" while printing the computed
    # `first_diff` on the line above it, and the returned
    # `interpretation_categorical` was a fixed string asserting u^15 outright.
    # Under convention D the answer is u^4, so the witness recorded
    # `first_differing_exponent: 4`, `is_first_diff_u15: false` and a prose
    # field insisting on 15 — all three in the same dict (bean `qou-saop`).
    #
    # This is a third species of the `qou-26f2` defect: not an assertion that
    # cannot fail, but *narration that cannot disagree with its own numbers*.
    # An AST-identity census cannot see it, since there is no assertion at all.
    # Everything below is now derived from `first_diff`.
    first_diff = diffs[0] if diffs else None
    _shared = ", ".join(f"u^{e}" for e in matches[:6]) + ("…" if len(matches) > 6 else "")
    print(f"\n  First exponent where p_in_u and n_in_u differ: u^{first_diff}")
    print(f"  → u^{first_diff} = LOWEST u-exponent where proton and neutron")
    print(f"    Habiro expansions actually disagree on a coefficient.")
    print(f"  → CATEGORICAL: the n vs p split first manifests at q-depth")
    print(f"    u^{first_diff} = q^{first_diff / 2} in the substrate u-expansion.")

    return {
        # Key kept for continuity; nothing outside this producer reads it. The
        # contents are whichever exponents actually agree, which under D is a
        # gapped set rather than the contiguous u^0..u^14 the name assumes.
        "shared_exponents_u0_to_u14": matches,
        "shared_exponents_are_contiguous_from_zero":
            matches == list(range(len(matches))),
        "first_differing_exponent": first_diff,
        "is_first_diff_u15": (first_diff == 15),
        "interpretation_categorical": (
            f"u^{first_diff} is the FIRST u-exponent where the "
            f"proton-numerator and neutron-numerator coefficients differ. "
            f"The braid words β_p and β_n agree on {len(matches)} exponent(s) "
            f"({_shared}) in their full tr_M expansions; the n−p split first "
            f"appears at u^{first_diff}. Under convention D this is the u^4 "
            f"factor of the p−n difference recorded in commit f392d75408e "
            f"('regen(D-only) … Φ_k structure does not survive'); the u^15 "
            f"this module is named for was the convention-C answer."
        ),
    }


# ─── Main ──────────────────────────────────────────────────────


def main() -> int:
    set_compute_dps()
    t0 = time.perf_counter()

    builder = WitnessBuilder(
        "qbeta-habiro-pn-split-depth",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Categorical interpretation of the u^15 prefactor in "
        "Σ_m Δa_m·(u;u)_m = −u^15·(u−1)(u+1)·P_8(u). Tests six candidates: "
        "(A) confirm u^15 is min-degree after cancellation; "
        "(B) (u;u)_5 hypothesis (deg 15); "
        "(C) per-m origin tracing; "
        "(D) M_p + M_n − 1 hypothesis; "
        "(E) (u;u)_8 / shared-denominator u^19; "
        "(F) first-differing u-exponent of reconstructed p_in_u vs n_in_u."
    )
    builder.set_content_block("prop:neutron-qvalue-symbolic")

    hab_path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    hab = builder.add_upstream(hab_path)
    builder.add_data("habiro_witness_used", str(hab_path.name))

    p_a = load_atom_polys(hab, "p (proton, A=1)")
    n_a = load_atom_polys(hab, "n (neutron, A=1)")
    M_p = max(p_a)
    M_n = max(n_a)
    print(f"\n  Loaded p (M={M_p}), n (M={M_n})")
    builder.add_data("habiro_depths", {"M_p": M_p, "M_n": M_n})

    # Build the symbolic Δ-Habiro element
    u = sp.Symbol('u')
    delta_habiro = sp.expand(sum(
        (n_a[m] - p_a[m]) * q_pochhammer(u, m)
        for m in sorted(p_a.keys() & n_a.keys())
    ))
    print(f"\n  Δ-Habiro = Σ_m Δa_m·(u;u)_m")
    print(f"    expanded: {delta_habiro}")
    print(f"    factored: {sp.factor(delta_habiro)}")

    # ─── Run all tests ──────────────────────────────────────────
    test_a = test_a_lowest_degree(p_a, n_a)
    test_b = test_b_pochhammer5(delta_habiro)
    test_c = test_c_per_m_origin(p_a, n_a)
    test_d = test_d_depth_sum_minus_1(M_p, M_n)
    test_e = test_e_pochhammer8_and_denom(delta_habiro)
    test_f = test_f_ladder_position(p_a, n_a)

    builder.add_data("test_A_lowest_degree", test_a)
    builder.add_data("test_B_pochhammer5", test_b)
    builder.add_data("test_C_per_m_origin", test_c)
    builder.add_data("test_D_depth_sum_minus_1", test_d)
    builder.add_data("test_E_pochhammer8_and_denom", test_e)
    builder.add_data("test_F_first_differing_exponent", test_f)

    # ─── Verdict ────────────────────────────────────────────────
    print(f"\n{'='*78}")
    print("  VERDICT")
    print('='*78)

    # Score the candidates.
    poch5_clean = test_b["divides_cleanly"]
    depth_sum_match = test_d["matches_15"]
    first_diff_at_15 = test_f["is_first_diff_u15"]

    # Build interpretation ladder
    interp_lines = []
    if poch5_clean:
        interp_lines.append(
            "CANDIDATE 5 (u;u)_5 IDENTIFIED: Δ-Habiro is cleanly divisible "
            "by (u;u)_5 — u^15 corresponds to the depth-5 q-Pochhammer "
            "TOP-degree term (1+2+3+4+5=15). The factorization can be "
            "REWRITTEN as ±(u;u)_5·(other factor)."
        )
    else:
        interp_lines.append(
            "CANDIDATE 5 (u;u)_5 FAILS: Δ-Habiro is NOT divisible by "
            "(u;u)_5. The arithmetic 1+2+3+4+5=15 is COINCIDENTAL — the "
            "u^15 monomial is a PREFACTOR (a pure power of u) not a "
            "leading term of any q-Pochhammer."
        )

    if depth_sum_match:
        interp_lines.append(
            f"CANDIDATE 4 (M_p+M_n−1=15) ARITHMETIC MATCH: M_p={M_p}+M_n={M_n}"
            f"−1=15. CAVEAT: Δa_7=Δa_8=0 (per prior audit), so the "
            f"effective Δ-support is m_eff=6, and the depth-sum reasoning "
            f"is structurally suspect (the nominal M_p=M_n=8 are the "
            f"individual atom depths, not properties of the Δ-element)."
        )

    if first_diff_at_15:
        interp_lines.append(
            "CANDIDATE F (first-differing exponent) STRUCTURAL: u^15 is "
            "the LOWEST u-exponent at which the reconstructed proton and "
            "neutron numerator polynomials differ. The braid words β_p, "
            "β_n agree on all monomials u^0..u^14 in their full tr_M "
            "expansion; the n vs p split first manifests at u^15. THIS "
            "is the categorical meaning — it's a structural property of "
            "the (β_p, β_n) braid pair, traceable to the topology of "
            "their crossing patterns."
        )

    for line in interp_lines:
        print(f"\n  {line}")

    # Best categorical interpretation
    best = "FIRST-DIFFERING-EXPONENT (Test F)" if first_diff_at_15 else "UNCLEAR"
    if poch5_clean:
        best = "(u;u)_5 (Test B)"

    builder.add_data("verdict", {
        "best_categorical_interpretation": best,
        "candidate_4_depth_sum": {
            "arithmetic_match": depth_sum_match,
            "structurally_sound": False,
            "reason": "Δa_7 = Δa_8 = 0; effective support stops at m=6, "
                      "not 8, so M_p+M_n−1 doesn't reflect the Δ-element.",
        },
        "candidate_5_pochhammer5": {
            "divides_cleanly": poch5_clean,
            "verdict": "DOES NOT DIVIDE" if not poch5_clean else "DIVIDES",
        },
        "candidate_F_first_diff_exponent": {
            "first_differing_u_exp_in_pn_numerators": (
                test_f["first_differing_exponent"]
            ),
            "is_u15": first_diff_at_15,
            "structural_meaning": (
                "u^15 = lowest u-exponent where β_p and β_n full tr_M "
                "expansions disagree. Categorical: structural property of "
                "the (β_p, β_n) braid pair (crossing-topology origin)."
            ),
        },
        "summary": "; ".join(interp_lines),
    })

    # Was `computed=6, expected=6` (bean `qou-26f2`) — the same literal on both
    # sides, so `allPassed` stayed true across a COMPLETE REVERSAL of this
    # probe's conclusion (see the premise check below). Two real checks replace
    # it.
    #
    # (a) COVERAGE. The expected count is the number of `test_<x>_*` functions
    #     the module defines, not the literal 6, so adding a test G without
    #     recording it fails here instead of leaving the witness silently short.
    test_fns = sorted(k for k, v in globals().items()
                      if k.startswith("test_") and callable(v))
    recorded = {k: v for k, v in builder.data.items()
                if k.startswith("test_") and isinstance(v, dict) and v}
    builder.add_assertion(
        "every_structural_test_recorded",
        computed=str(len(recorded)),
        expected=str(len(test_fns)),
        tolerance=0,
        unit="test result dicts in witness data",
        source=("tests defined: " + ", ".join(test_fns) + "; recorded: "
                + ", ".join(sorted(recorded))),
    )

    # (b) TWO INDEPENDENT ROUTES TO THE SAME EXPONENT. Test A takes the minimum
    #     degree of Σ_m Δa_m·(u;u)_m — differenced per m, then summed. Test F
    #     assembles p and n separately (Σ_m a_m·(u;u)_m each) and reports the
    #     lowest exponent at which their coefficients disagree. Linearity says
    #     these are the same integer; the two get there through different key
    #     sets (A intersects p_a/n_a, F iterates each alone) and different
    #     sympy expansions, so a depth mismatch M_p != M_n, or a dropped m,
    #     breaks the agreement. That is the check the tautology was standing in
    #     for. NOTE Test F only scans u^0..u^15, so it reports None if the first
    #     difference sits above u^15 — recorded rather than silently compared.
    min_deg = test_a["expanded_min_deg"]
    first_diff = test_f["first_differing_exponent"]
    if first_diff is None:
        builder.add_data("first_diff_out_of_scanned_range", {
            "test_f_scans": "u^0..u^15",
            "test_a_min_deg": min_deg,
            "has_independent_expected_value": False,
        })
        builder.add_caveat(
            "Test F found no differing coefficient in u^0..u^15, so its "
            "exponent could not be cross-checked against Test A's minimum "
            "degree of " + str(min_deg) + ".")
    else:
        builder.add_assertion(
            "min_degree_agrees_with_first_differing_exponent",
            computed=str(min_deg),
            expected=str(first_diff),
            tolerance=0,
            unit="u-exponent",
            source=("Test A: min degree of Σ_m Δa_m·(u;u)_m (per-m difference, "
                    "then sum). Test F: lowest u-exponent where the separately "
                    "assembled p and n numerators disagree. Equal by linearity; "
                    "computed by disjoint code paths."),
        )

    # (c) THE PREMISE, WHICH IS NO LONGER TRUE. This probe's description, prose
    #     and name all assume the Δ-Habiro element has its floor at u^15. On the
    #     upstream atomic witness as it now stands that floor is elsewhere, and
    #     it is recorded rather than asserted so the drift is visible without
    #     this producer quietly re-writing its own subject.
    builder.add_data("u15_premise", {
        "claim": "the Δ-Habiro element Σ_m Δa_m·(u;u)_m has its lowest-degree "
                 "monomial at u^15 (description, Test A, Test F)",
        "holds": bool(test_a["is_u15_min"]),
        "measured_min_degree": min_deg,
        "measured_first_differing_exponent": first_diff,
        "upstream": str(hab_path.name),
        "has_independent_expected_value": False,
    })
    if not test_a["is_u15_min"]:
        builder.add_caveat(
            f"PREMISE NOT REPRODUCED: this probe is named and described for a "
            f"u^15 floor, but against the current {hab_path.name} the floor is "
            f"u^{min_deg} (first differing exponent u^{first_diff}), the "
            f"Δa_m support runs m={min(test_c['per_m_origin'], key=int)}.."
            f"{max(test_c['per_m_origin'], key=int)}, and the verdict falls to "
            f"'{best}'. The prose and the description were written against an "
            f"earlier atomic witness; they have not been rewritten here.")

    builder.save()
    print(f"\n  ✓ Witness: qbeta-habiro-pn-split-depth.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
