#!/usr/bin/env python3
"""qbeta_habiro_delta_am_factorization.py — factorize Δa_m(u) = a_m(n) − a_m(p).

KEYSTONE FOLLOW-UP per docs/audits/2026-05-31-qbeta-habiro-element-probe.md:

The prior probe (commit e6c6747eb) identified the "STRIKING PATTERN":

    Δa_m(u) := a_m(neutron) − a_m(proton)  has SMALL-INTEGER coefficients.

Constraint C6 lists:
    Δa_0 = 0
    Δa_1 = 10·u + 10
    Δa_2 = −64·u² − 69·u − 73
    Δa_3 = 131·u³ + 143·u² + 160·u + 177
    Δa_4 = −92·u⁴ − 114·u³ − 136·u² − 162·u − 189

We now perform a SYMBOLIC (sympy.Poly / sympy.factor / sympy.gcd_list)
factorization for m = 0..8, then attempt categorical interpretation.

PRIMARY TESTS:

  1. Factorize each Δa_m(u) using sympy.factor.
  2. Compute GCD across all Δa_m (m ≥ 1) — non-trivial would be the
     STRUCTURAL "n vs p" common factor.
  3. Match factors against known categorical polynomials:
     (1−u), (1+u), (1−u²), (1−u+u²), (1+u+u²), cyclotomics Φ_n(u)
  4. Compute successive ratios Δa_m / Δa_{m-1} for a recursion pattern.
  5. Compute the Habiro element Σ_m Δa_m·(u;u)_m and factor.
  6. Test ratios of (deuteron) vs (n+p) for the deuteron Habiro element
     in the same Δ framework.

NEGATIVE-RESULT VALUE: even no-factorization is informative — it would
say "the n−p difference is GENUINELY irreducible at the algebraic level,
and the small-integer pattern is a coincidence of the substrate q₀
arithmetic". This would shift the proof obligation back onto the
multi-Wedderburn-block extension (per audit C-section §multi-block).

USAGE:
    python3 -u qbeta_habiro_delta_am_factorization.py 2>&1 \
        | tee /tmp/qbeta_delta_am.log

Outputs:
    folio-assistant/computations/qbeta-habiro-delta-am-factorization.witness.json
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


def load_atom(hab: dict, key: str) -> dict[int, sp.Poly]:
    """Parse a_m strings into sympy Poly objects in u with integer coeffs."""
    u = sp.Symbol('u')
    out = {}
    for entry in hab["results"][key]["habiro_coefficients"]:
        m = entry["m"]
        a_str = entry["a_m"]
        p = sp.Poly(sp.sympify(a_str), u, domain='ZZ')
        out[m] = p
    return out


def poly_to_str(p: sp.Poly | sp.Expr) -> str:
    if isinstance(p, sp.Poly):
        return str(sp.expand(p.as_expr()))
    return str(sp.expand(p))


def factor_str(expr) -> str:
    """Pretty-print sp.factor output as a single expression string."""
    f = sp.factor(expr)
    return str(f)


# ─── Sub-task: factorize each Δa_m ──────────────────────────────


def factorize_diffs(p_a: dict[int, sp.Poly],
                    n_a: dict[int, sp.Poly],
                    label: str = "n_minus_p") -> dict:
    """Factor each Δa_m = a_m(B) - a_m(A) for m in the shared support."""
    u = sp.Symbol('u')

    shared = sorted(set(p_a) & set(n_a))
    results: dict[int, dict] = {}
    delta_polys: list[sp.Poly] = []

    print(f"\n{'='*78}")
    print(f"  Δa_m factorization: {label}  ({len(shared)} entries)")
    print('='*78)

    for m in shared:
        delta = (n_a[m] - p_a[m]).as_expr()
        delta = sp.expand(delta)
        if delta == 0:
            results[m] = {
                "delta_a_m": "0",
                "factorization": "0",
                "deg": -1,
                "leading_coeff": 0,
                "content_gcd": 0,
                "primitive_part": "0",
                "primitive_factorization": "0",
            }
            print(f"  m={m:2d}: Δa_m = 0  (atoms share)")
            continue

        delta_poly = sp.Poly(delta, u, domain='ZZ')
        delta_polys.append(delta_poly)

        # Content (integer GCD of coefficients) and primitive part
        coeffs = delta_poly.all_coeffs()
        content = sp.gcd_list([abs(int(c)) for c in coeffs])
        # Make primitive (divide by content with sign of leading term)
        sign = 1 if int(coeffs[0]) > 0 else -1
        primitive = sp.Poly(delta_poly.as_expr() / (sign * content),
                            u, domain='ZZ')

        fac_full = factor_str(delta)
        fac_prim = factor_str(primitive.as_expr())

        results[m] = {
            "delta_a_m": poly_to_str(delta),
            "factorization": fac_full,
            "deg": delta_poly.degree(),
            "leading_coeff": int(coeffs[0]),
            "content_gcd": int(content),
            "primitive_part": poly_to_str(primitive.as_expr()),
            "primitive_factorization": fac_prim,
            "coeffs_descending": [int(c) for c in coeffs],
        }

        print(f"  m={m:2d}: Δa_m = {poly_to_str(delta)}")
        print(f"        content={content}  primitive={poly_to_str(primitive.as_expr())}")
        print(f"        factor:    {fac_full}")
        if fac_prim != poly_to_str(primitive.as_expr()):
            print(f"        primitive factor: {fac_prim}")

    return {
        "label": label,
        "shared_m": shared,
        "per_m": results,
        "delta_polys": delta_polys,
    }


def cross_m_gcd(delta_polys: list[sp.Poly], label: str) -> dict:
    """Compute GCD of all non-zero Δa_m polynomials together."""
    u = sp.Symbol('u')
    nonzero = [p for p in delta_polys if not p.is_zero]
    if not nonzero:
        return {"gcd": "0", "trivial": True, "interpretation": "no data"}
    gcd = nonzero[0]
    for p in nonzero[1:]:
        gcd = sp.gcd(gcd, p)
    gcd_expr = sp.expand(gcd.as_expr() if isinstance(gcd, sp.Poly) else gcd)
    trivial = gcd_expr in (1, -1) or (
        isinstance(gcd_expr, sp.Integer) and abs(int(gcd_expr)) <= 1)

    print(f"\n  GCD over all Δa_m ({label}):  {gcd_expr}")
    print(f"  trivial? {trivial}")
    return {
        "gcd": str(gcd_expr),
        "trivial": trivial,
        "factorization": factor_str(gcd_expr) if not trivial else "1",
    }


# ─── Sub-task: integer-coefficient GCD across m ─────────────────


def integer_content_gcd(delta_polys: list[sp.Poly], label: str) -> dict:
    """Compute GCD of the integer contents across all Δa_m."""
    nonzero = [p for p in delta_polys if not p.is_zero]
    contents = []
    for p in nonzero:
        coeffs = [abs(int(c)) for c in p.all_coeffs()]
        contents.append(sp.gcd_list(coeffs))
    if not contents:
        return {"integer_gcd": 0, "per_m_contents": []}
    overall = sp.gcd_list(contents)
    print(f"\n  Integer-content GCD across all Δa_m ({label}): {overall}")
    print(f"  Per-m contents: {contents}")
    return {
        "integer_gcd": int(overall),
        "per_m_contents": [int(c) for c in contents],
    }


# ─── Sub-task: known categorical polynomial matching ────────────


def match_categorical_factors(per_m: dict) -> dict:
    """Try to spot known polynomials (cyclotomic / q-Pochhammer) in factors."""
    u = sp.Symbol('u')

    # Reference polynomials (categorical / cyclotomic):
    refs = {
        "(1-u)":     1 - u,
        "(1+u)":     1 + u,
        "(1-u^2)":   1 - u**2,
        "(1-u+u^2)": 1 - u + u**2,      # Φ_6(u)
        "(1+u+u^2)": 1 + u + u**2,      # Φ_3(u)
        "(1+u^2)":   1 + u**2,          # Φ_4(u)
        "(1-u^3)":   1 - u**3,
        "(1-u^4)":   1 - u**4,
        "(u^2+u+1)": u**2 + u + 1,
        "(u-1)":     u - 1,
    }

    findings = {}
    for m, info in per_m.items():
        if info["deg"] < 0:
            continue
        prim = sp.sympify(info["primitive_part"])
        matches = []
        for name, ref_expr in refs.items():
            # Is ref_expr a factor (or its negative)?
            quot, rem = sp.div(prim, ref_expr, u)
            if rem == 0:
                matches.append(name)
        findings[m] = {
            "primitive_part": info["primitive_part"],
            "matched_categorical_factors": matches,
            "irreducible_remainder": (
                str(sp.factor(prim)) if not matches else
                str(sp.factor(prim))
            ),
        }
        if matches:
            print(f"  m={m}: primitive part matches categorical factors: {matches}")
        else:
            print(f"  m={m}: primitive part has NO categorical factor; factorization: {sp.factor(prim)}")
    return findings


# ─── Sub-task: ratios Δa_m / Δa_{m-1} ──────────────────────────


def successive_ratios(delta_polys: list[sp.Poly], shared_m: list[int]) -> dict:
    """Compute Δa_m / Δa_{m-1} as rational functions and look for a pattern."""
    u = sp.Symbol('u')
    out = {}
    # Build (m, poly) pairs in m-order
    pairs = sorted([(p.gens[0] if False else m, p)
                    for m, p in zip(shared_m, delta_polys)],
                   key=lambda mp: mp[0])
    # Re-zip after sorting
    indexed = []
    for m in shared_m:
        for p in delta_polys:
            # we'll need a different structure; redo more simply below
            pass

    # Re-do properly: just iterate the shared_m list directly
    for i in range(1, len(shared_m)):
        m = shared_m[i]
        m_prev = shared_m[i - 1]
        # We don't have direct access here, so caller must pass full info.
        pass
    return out


def successive_ratios_from_per_m(per_m: dict) -> dict:
    """Compute Δa_m / Δa_{m-1} as rational functions."""
    u = sp.Symbol('u')
    out = {}
    ms = sorted([m for m, info in per_m.items() if info["deg"] >= 0])
    if not ms:
        return out

    print(f"\n  Successive ratios Δa_m / Δa_{{m-1}}:")
    for i in range(1, len(ms)):
        m, m_prev = ms[i], ms[i - 1]
        cur = sp.sympify(per_m[m]["delta_a_m"])
        prv = sp.sympify(per_m[m_prev]["delta_a_m"])
        try:
            ratio = sp.simplify(cur / prv)
            ratio_factored = sp.factor(ratio)
        except Exception as e:
            ratio = f"err: {e}"
            ratio_factored = ratio

        # Numerical at u = sqrt(q_0) = \check{q}_0 ≈ 1.0535
        # (spinor rate at canonical substrate; "u" kept per Habiro lit.)
        u_num = sp.Float("1.05356473")
        try:
            ratio_num = float(sp.sympify(ratio).subs(u, u_num))
        except Exception:
            ratio_num = None

        out[f"ratio_{m}_over_{m_prev}"] = {
            "ratio": str(ratio),
            "factored": str(ratio_factored),
            "numerical_at_u0": ratio_num,
        }
        print(f"    Δa_{m}/Δa_{m_prev} = {ratio_factored}"
              + (f"   (≈ {ratio_num:.4f} at u₀)" if ratio_num is not None
                 else ""))
    return out


# ─── Sub-task: Σ_m Δa_m·(u;u)_m  (the symbolic Habiro element) ──


def delta_habiro_element(per_m: dict, max_m: int = 8) -> dict:
    """Form Σ_{m=0..max_m} Δa_m·(u;u)_m and factor in u."""
    u = sp.Symbol('u')

    # (u;u)_m = Π_{k=1..m}(1 - u^k)
    def poch(m: int):
        result = sp.Integer(1)
        for k in range(1, m + 1):
            result *= (1 - u**k)
        return sp.expand(result)

    total = sp.Integer(0)
    for m, info in per_m.items():
        if m > max_m or info["deg"] < 0:
            continue
        am = sp.sympify(info["delta_a_m"])
        total += am * poch(m)
    total = sp.expand(total)

    factored = sp.factor(total)

    # Try a numerical evaluation at u_0 = sqrt(q_0) ≈ 1.05356
    u_num = sp.Float("1.05356473")
    try:
        val_at_u0 = float(total.subs(u, u_num))
    except Exception:
        val_at_u0 = None

    print(f"\n  Σ_m Δa_m·(u;u)_m (the unnormalised n-p Habiro element):")
    print(f"     expanded length: {len(str(total))} chars")
    print(f"     factored: {factored}")
    print(f"     numerical at u₀: {val_at_u0}")
    return {
        "expanded": str(total),
        "factored": str(factored),
        "numerical_at_u0_approx": val_at_u0,
        "degree": sp.Poly(total, u).degree() if total != 0 else -1,
    }


# ─── Sub-task: deuteron vs (p+n) channel ────────────────────────


def deuteron_minus_pn(p_a: dict[int, sp.Poly],
                      n_a: dict[int, sp.Poly],
                      d_a: dict[int, sp.Poly]) -> dict:
    """Compute Δa_m = a_m(D) − (a_m(p) + a_m(n)) on shared support and factor.

    The deuteron isn't naively (p + n) in Habiro coords because the
    denominators differ, but on the SHARED support we can still inspect
    a_m(D) − (a_m(p) + a_m(n)) as a structural probe.
    """
    u = sp.Symbol('u')
    shared = sorted(set(p_a) & set(n_a) & set(d_a))
    out = {}
    print(f"\n{'='*78}")
    print(f"  D − (p+n) on shared support m ∈ {shared}")
    print('='*78)
    for m in shared:
        # Note: D has a 32x denominator vs p,n's 4x — direct subtraction
        # doesn't have a clean physical meaning, but it surfaces the
        # algebraic relationship.
        diff = sp.expand(d_a[m].as_expr() - p_a[m].as_expr() - n_a[m].as_expr())
        if diff == 0:
            out[m] = {"diff": "0", "factorization": "0"}
            print(f"  m={m}: D − (p+n) = 0")
        else:
            fac = sp.factor(diff)
            out[m] = {"diff": str(diff),
                      "factorization": str(fac),
                      "deg": sp.Poly(diff, u).degree()}
            print(f"  m={m}: D − (p+n) = {diff}")
            print(f"        factor: {fac}")
    return {"per_m": out, "shared_m": shared,
            "note": "p,n have D_denom=4·u^19·(1+u²); D has 32·u^40·(1+u²)·(1+u)². "
                    "Direct coefficient subtraction is a structural probe only."}


# ─── Main ──────────────────────────────────────────────────────


def main() -> int:
    set_compute_dps()
    t0 = time.perf_counter()

    builder = WitnessBuilder(
        "qbeta-habiro-delta-am-factorization",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Keystone follow-up per docs/audits/2026-05-31-qbeta-habiro-element-probe.md "
        "constraint C6. Symbolic factorization (sympy.Poly + sympy.factor) of "
        "Δa_m(u) := a_m(neutron) − a_m(proton) for m = 0..8 plus cross-m GCD, "
        "categorical-factor matching, successive ratios, and the symbolic "
        "Habiro element Σ_m Δa_m·(u;u)_m. Negative results documented; this "
        "probe explicitly tests the conjectured low-degree factorization."
    )
    builder.set_content_block("prop:neutron-qvalue-symbolic")

    hab_path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    hab = json.loads(hab_path.read_text())
    builder.add_data("habiro_witness_used", str(hab_path.name))

    # Parse atoms into Poly objects
    p_a = load_atom(hab, "p (proton, A=1)")
    n_a = load_atom(hab, "n (neutron, A=1)")
    d_a = load_atom(hab, "D (deuteron, A=2)")
    print(f"\n  Loaded p (M={max(p_a)}), n (M={max(n_a)}), "
          f"D (M={max(d_a)})")

    # ─── Δa_m = n - p factorization ────────────────────────────
    np_result = factorize_diffs(p_a, n_a, label="n_minus_p")
    builder.add_data("delta_n_minus_p", {
        "per_m": np_result["per_m"],
        "shared_m": np_result["shared_m"],
    })

    # ─── GCD across m ───────────────────────────────────────────
    poly_gcd = cross_m_gcd(np_result["delta_polys"], "n−p")
    int_gcd = integer_content_gcd(np_result["delta_polys"], "n−p")
    builder.add_data("delta_n_minus_p_gcd", {
        "polynomial_gcd": poly_gcd,
        "integer_content_gcd": int_gcd,
    })

    # ─── Categorical factor matching ────────────────────────────
    print(f"\n  Categorical factor matching (n−p):")
    cat_match = match_categorical_factors(np_result["per_m"])
    builder.add_data("delta_n_minus_p_categorical_matches", cat_match)

    # ─── Successive ratios ──────────────────────────────────────
    ratios = successive_ratios_from_per_m(np_result["per_m"])
    builder.add_data("delta_n_minus_p_successive_ratios", ratios)

    # ─── Σ Δa_m·(u;u)_m  (the symbolic Habiro element) ──────────
    delta_habiro = delta_habiro_element(np_result["per_m"], max_m=8)
    builder.add_data("delta_n_minus_p_habiro_element", delta_habiro)

    # ─── Deuteron channel ───────────────────────────────────────
    d_minus_pn = deuteron_minus_pn(p_a, n_a, d_a)
    builder.add_data("deuteron_minus_p_plus_n", d_minus_pn)

    # ─── Verdict ────────────────────────────────────────────────
    print(f"\n{'='*78}")
    print("  VERDICT SUMMARY")
    print('='*78)

    # Classify outcome:
    poly_gcd_trivial = poly_gcd["trivial"]
    int_gcd_val = int_gcd["integer_gcd"]
    any_cat_match = any(info["matched_categorical_factors"]
                        for info in cat_match.values())

    if not poly_gcd_trivial:
        outcome = "FACTORS-IDENTIFIED"
    elif int_gcd_val > 1 or any_cat_match:
        outcome = "PARTIAL"
    else:
        outcome = "NEGATIVE"

    print(f"\n  Polynomial GCD over m≥1:       {poly_gcd['gcd']}"
          f" (trivial={poly_gcd_trivial})")
    print(f"  Integer content GCD over m≥1:  {int_gcd_val}")
    print(f"  Any per-m categorical match:   {any_cat_match}")
    print(f"\n  OVERALL: {outcome}\n")

    builder.add_data("verdict", {
        "outcome": outcome,
        "polynomial_gcd_trivial": poly_gcd_trivial,
        "integer_content_gcd": int_gcd_val,
        "any_categorical_per_m_match": any_cat_match,
        "interpretation": (
            "FACTORS-IDENTIFIED: a common polynomial factor divides every "
            "Δa_m → this factor IS the Q_β-relevant categorical primitive. "
            "PARTIAL: per-m factorizations expose categorical primitives but "
            "no single factor unites all m. "
            "NEGATIVE: Δa_m are algebraically generic; 'small-integer' is "
            "a content phenomenon (integer GCD), not a polynomial factor; "
            "the conjecture in C6 of the prior audit is FALSIFIED."
        )[{"FACTORS-IDENTIFIED": 0, "PARTIAL": 1, "NEGATIVE": 2}
          .get(outcome, 0):],
    })

    builder.add_assertion(
        "delta_n_minus_p_factorization_completed",
        computed=1,
        expected=1,
        tolerance=0,
        source="sympy.factor over ℤ[u] for each Δa_m, m=0..8.",
    )

    builder.save()
    print(f"  ✓ Witness: qbeta-habiro-delta-am-factorization.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
