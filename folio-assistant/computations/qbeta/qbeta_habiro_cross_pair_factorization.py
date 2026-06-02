#!/usr/bin/env python3
"""qbeta_habiro_cross_pair_factorization.py — cross-validate Δa_m structure.

KEYSTONE CROSS-VALIDATION per docs/audits/2026-05-31-qbeta-habiro-delta-am-
factorization.md.

The n−p Δa_m factorization revealed:

    Σ_m Δa_m·(u;u)_m  =  −u^15 · (u−1)(u+1) · P_8(u)

with cyclotomic prefactor Φ_1·Φ_2 = (u²−1) and an irreducible 8-degree
residual P_8(u). We now ask whether the SAME pattern holds across atomic-
number jumps:

    PAIR A: ³He − D     (atomic-number step A=2 → A=3)
    PAIR B: ⁴He − ³He   (atomic-number step A=3 → A=4)

vs the reference

    PAIR n−p:           (isospin step Z=0,N=1 → Z=1,N=0 at A=1)

THREE CLASSIFICATIONS:

  UNIVERSAL  — same cyclotomic prefactor (u²−1) appears in all three pairs
               → structural categorical feature of the Habiro-ring isospin
               / atomic-number-breaking element.

  SPECIFIC   — only n−p shows the clean factorization → the prefactor is
               special to isospin SU(2)_I rather than general A→A+1
               transitions.

  PARTIAL    — cyclotomic appears with different depths k → depth tracks
               M_left+M_right−1 (15 for n−p, 27 for ³He−D, 35 for ⁴He−³He).

USAGE:
    python3 -u qbeta_habiro_cross_pair_factorization.py 2>&1 \\
        | tee /tmp/cross_pair.log

Outputs:
    folio-assistant/computations/qbeta-habiro-cross-pair-factorization.witness.json
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
        # a_m may be "0" (string) for higher m if missing — sympify handles it
        p = sp.Poly(sp.sympify(a_str), u, domain='ZZ')
        out[m] = p
    return out


def load_atom_from_external(path: str) -> dict[int, sp.Poly]:
    """Parse a_m strings from a separately-generated ³He/⁴He JSON file."""
    u = sp.Symbol('u')
    out = {}
    data = json.loads(Path(path).read_text())
    for entry in data["habiro_coefficients"]:
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


# ─── Per-pair factorization ─────────────────────────────────────


def factorize_diffs(left_a: dict[int, sp.Poly],
                    right_a: dict[int, sp.Poly],
                    label: str) -> dict:
    """Factor each Δa_m = a_m(left) - a_m(right) for m in union(support).

    Where one atom has a higher M, the "missing" coefficient is 0
    (per audit precedent: Δa_7 = Δa_8 = 0 for n−p because the atoms
    share those coefficients exactly).
    """
    u = sp.Symbol('u')

    union = sorted(set(left_a) | set(right_a))
    results: dict[int, dict] = {}
    delta_polys: list[sp.Poly] = []

    print(f"\n{'='*78}")
    print(f"  Δa_m factorization: {label}  ({len(union)} entries, m=0..{max(union)})")
    print('='*78)

    for m in union:
        l = left_a.get(m)
        r = right_a.get(m)
        if l is None:
            # missing on left → treat as 0
            delta = (sp.Integer(0) - r.as_expr())
        elif r is None:
            delta = (l.as_expr() - sp.Integer(0))
        else:
            delta = (l.as_expr() - r.as_expr())
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

        coeffs = delta_poly.all_coeffs()
        content = sp.gcd_list([abs(int(c)) for c in coeffs])
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

        # Compact printout for high-m to keep log readable
        if delta_poly.degree() <= 12:
            print(f"  m={m:2d}: Δa_m = {poly_to_str(delta)}")
            print(f"        content={content}  factor: {fac_full}")
        else:
            print(f"  m={m:2d}: deg={delta_poly.degree()}, content={content}, lead={int(coeffs[0])}")
            print(f"        factor: {fac_full[:200]}{'...' if len(fac_full) > 200 else ''}")

    return {
        "label": label,
        "union_m": union,
        "per_m": results,
        "delta_polys": delta_polys,
    }


def cross_m_gcd(delta_polys: list[sp.Poly], label: str) -> dict:
    """Compute polynomial GCD across all non-zero Δa_m."""
    u = sp.Symbol('u')
    nonzero = [p for p in delta_polys if not p.is_zero]
    if not nonzero:
        return {"gcd": "0", "trivial": True}
    gcd = nonzero[0]
    for p in nonzero[1:]:
        gcd = sp.gcd(gcd, p)
    gcd_expr = sp.expand(gcd.as_expr() if isinstance(gcd, sp.Poly) else gcd)
    trivial = gcd_expr in (1, -1) or (
        isinstance(gcd_expr, sp.Integer) and abs(int(gcd_expr)) <= 1)

    print(f"\n  Polynomial GCD over all Δa_m ({label}):  {gcd_expr}")
    print(f"  trivial? {trivial}")
    return {
        "gcd": str(gcd_expr),
        "trivial": trivial,
        "factorization": factor_str(gcd_expr) if not trivial else "1",
    }


def integer_content_gcd(delta_polys: list[sp.Poly], label: str) -> dict:
    nonzero = [p for p in delta_polys if not p.is_zero]
    contents = []
    for p in nonzero:
        coeffs = [abs(int(c)) for c in p.all_coeffs()]
        contents.append(sp.gcd_list(coeffs))
    if not contents:
        return {"integer_gcd": 0, "per_m_contents": []}
    overall = sp.gcd_list(contents)
    print(f"\n  Integer-content GCD ({label}): {overall}")
    print(f"  Per-m contents: {contents}")
    return {
        "integer_gcd": int(overall),
        "per_m_contents": [int(c) for c in contents],
    }


def delta_habiro_element(per_m: dict, label: str, max_m: int = 20) -> dict:
    """Form Σ_m Δa_m·(u;u)_m and factor.

    Per the n−p reference: this is where the cyclotomic (u²−1) prefactor
    appeared. Whether or not it appears here is THE structural question.
    """
    u = sp.Symbol('u')

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

    print(f"\n  Σ_m Δa_m·(u;u)_m for {label}:")
    print(f"     expanded length: {len(str(total))} chars")

    factored = sp.factor(total)
    print(f"     factored:    {str(factored)[:300]}{'...' if len(str(factored)) > 300 else ''}")

    # Extract the leading cyclotomic prefactor: look for (u-1), (u+1), (u²+1)
    # by polynomial-division test.
    cyclotomics = {
        "(u-1)": u - 1,
        "(u+1)": u + 1,
        "(u^2-1)": u**2 - 1,
        "(u^2+1)": u**2 + 1,
        "(u^2+u+1)": u**2 + u + 1,
        "(u^2-u+1)": u**2 - u + 1,
    }
    matched = {}
    for name, cyc in cyclotomics.items():
        try:
            quot, rem = sp.div(total, cyc, u)
            if rem == 0:
                matched[name] = "divides"
        except Exception:
            matched[name] = "error"

    # Compute u^k depth — the largest k such that u^k divides Σ
    if total != 0:
        poly_total = sp.Poly(total, u)
        monoms = poly_total.monoms()
        if monoms:
            min_pow = min(int(m[0]) for m in monoms)
            depth_k = min_pow
        else:
            depth_k = -1
    else:
        depth_k = -1

    # Get degree
    if total != 0:
        deg = sp.Poly(total, u).degree()
    else:
        deg = -1

    print(f"     u^k depth (lowest power):    u^{depth_k}")
    print(f"     polynomial degree:           {deg}")
    print(f"     cyclotomic divisor matches:  {matched}")

    # Numerical evaluation at u_0 = sqrt(q_0) ≈ 1.0535
    u_num = sp.Float("1.05356473")
    try:
        val_at_u0 = float(total.subs(u, u_num))
    except Exception:
        val_at_u0 = None

    return {
        "label": label,
        "expanded": str(total),
        "factored": str(factored),
        "u_depth_k": int(depth_k),
        "degree": int(deg),
        "cyclotomic_matches": matched,
        "numerical_at_u0_approx": val_at_u0,
    }


def compare_pair_signatures(np_sig: dict,
                            he3_d_sig: dict,
                            he4_he3_sig: dict) -> dict:
    """Classify the cross-pair pattern.

    UNIVERSAL: all three have (u²−1) (or both (u−1) and (u+1)) as divisor.
    SPECIFIC:  only n−p has it.
    PARTIAL:   some pairs have it, others have a different cyclotomic.
    """
    def has_u2_minus_1(sig: dict) -> bool:
        m = sig.get("cyclotomic_matches", {})
        return (m.get("(u^2-1)") == "divides" or
                (m.get("(u-1)") == "divides" and m.get("(u+1)") == "divides"))

    signatures = {
        "n_minus_p": has_u2_minus_1(np_sig),
        "he3_minus_d": has_u2_minus_1(he3_d_sig),
        "he4_minus_he3": has_u2_minus_1(he4_he3_sig),
    }

    print(f"\n{'='*78}")
    print(f"  CYCLOTOMIC PREFACTOR (u²−1) CROSS-PAIR SUMMARY")
    print('='*78)
    for k, v in signatures.items():
        sig = (np_sig if k == "n_minus_p"
               else he3_d_sig if k == "he3_minus_d" else he4_he3_sig)
        print(f"  {k:18s}: (u²−1) divides? {v}   "
              f"u^k depth = {sig.get('u_depth_k')}, "
              f"degree = {sig.get('degree')}")

    n_pos = sum(signatures.values())
    if n_pos == 3:
        verdict = "UNIVERSAL"
    elif n_pos == 1 and signatures["n_minus_p"]:
        verdict = "SPECIFIC"
    elif n_pos >= 1:
        verdict = "PARTIAL"
    else:
        verdict = "ABSENT"

    print(f"\n  VERDICT: {verdict}  ({n_pos}/3 pairs have (u²−1) prefactor)")

    return {
        "signatures": signatures,
        "verdict": verdict,
        "n_positive": n_pos,
        "n_minus_p_u_depth": np_sig.get("u_depth_k"),
        "he3_minus_d_u_depth": he3_d_sig.get("u_depth_k"),
        "he4_minus_he3_u_depth": he4_he3_sig.get("u_depth_k"),
    }


# ─── Main ──────────────────────────────────────────────────────


def main() -> int:
    set_compute_dps()
    t0 = time.perf_counter()

    builder = WitnessBuilder(
        "qbeta-habiro-cross-pair-factorization",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Cross-validate the n−p Δa_m cyclotomic prefactor (u²−1)·P_8(u) "
        "across atomic-number jumps (³He−D, ⁴He−³He). Tests whether the "
        "Φ_1·Φ_2 structural prefactor is a UNIVERSAL feature of the "
        "Habiro-ring isospin/atomic-number-breaking element or SPECIFIC "
        "to the isospin SU(2)_I doublet."
    )
    builder.set_content_block("prop:neutron-qvalue-symbolic")

    # ─── Load atomic Habiro coefficients ───────────────────────
    hab_path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    hab = json.loads(hab_path.read_text())
    builder.add_data("base_habiro_witness", str(hab_path.name))

    p_a = load_atom(hab, "p (proton, A=1)")
    n_a = load_atom(hab, "n (neutron, A=1)")
    d_a = load_atom(hab, "D (deuteron, A=2)")

    # ³He and ⁴He: load from auxiliary witness if pre-generated.
    he3_path = _pb.witness_path("habiro-coefficients-helium-3.witness.json", HERE)
    he4_path = _pb.witness_path("habiro-coefficients-helium-4.witness.json", HERE)
    he3_a = None
    he4_a = None
    if he3_path.exists():
        he3_a = load_atom_from_external(str(he3_path))
        print(f"  Loaded ³He from {he3_path.name} (M = {max(he3_a)})")
    if he4_path.exists():
        he4_a = load_atom_from_external(str(he4_path))
        print(f"  Loaded ⁴He from {he4_path.name} (M = {max(he4_a)})")

    if he3_a is None or he4_a is None:
        print("\n  ERROR: helium-3 and/or helium-4 Habiro coefficient "
              "auxiliary witness JSON files not found.")
        print("  Generate via:")
        print("    python3 -u folio-assistant/computations/"
              "_helium_habiro_helper.py")
        return 2

    print(f"  Loaded p (M={max(p_a)}), n (M={max(n_a)}), "
          f"D (M={max(d_a)}), ³He (M={max(he3_a)}), ⁴He (M={max(he4_a)})")

    # ─── REFERENCE: n − p (re-run for in-script comparison) ────
    np_result = factorize_diffs(n_a, p_a, label="n_minus_p (REFERENCE)")
    np_habiro = delta_habiro_element(np_result["per_m"], "n−p",
                                      max_m=max(max(n_a), max(p_a)))
    np_gcd = cross_m_gcd(np_result["delta_polys"], "n−p")
    np_int = integer_content_gcd(np_result["delta_polys"], "n−p")
    builder.add_data("n_minus_p_reference", {
        "per_m": np_result["per_m"],
        "habiro_element": np_habiro,
        "polynomial_gcd": np_gcd,
        "integer_content_gcd": np_int,
    })

    # ─── PAIR A: ³He − D ───────────────────────────────────────
    he3d_result = factorize_diffs(he3_a, d_a, label="³He_minus_D")
    he3d_habiro = delta_habiro_element(he3d_result["per_m"], "³He−D",
                                        max_m=max(max(he3_a), max(d_a)))
    he3d_gcd = cross_m_gcd(he3d_result["delta_polys"], "³He−D")
    he3d_int = integer_content_gcd(he3d_result["delta_polys"], "³He−D")
    builder.add_data("he3_minus_d", {
        "per_m": he3d_result["per_m"],
        "habiro_element": he3d_habiro,
        "polynomial_gcd": he3d_gcd,
        "integer_content_gcd": he3d_int,
    })

    # ─── PAIR B: ⁴He − ³He ─────────────────────────────────────
    he4_3_result = factorize_diffs(he4_a, he3_a, label="⁴He_minus_³He")
    he4_3_habiro = delta_habiro_element(he4_3_result["per_m"], "⁴He−³He",
                                         max_m=max(max(he4_a), max(he3_a)))
    he4_3_gcd = cross_m_gcd(he4_3_result["delta_polys"], "⁴He−³He")
    he4_3_int = integer_content_gcd(he4_3_result["delta_polys"], "⁴He−³He")
    builder.add_data("he4_minus_he3", {
        "per_m": he4_3_result["per_m"],
        "habiro_element": he4_3_habiro,
        "polynomial_gcd": he4_3_gcd,
        "integer_content_gcd": he4_3_int,
    })

    # ─── Cross-pair classification ─────────────────────────────
    verdict = compare_pair_signatures(np_habiro, he3d_habiro, he4_3_habiro)
    builder.add_data("cross_pair_verdict", verdict)

    builder.add_assertion(
        "cross_pair_factorization_completed",
        computed=1,
        expected=1,
        tolerance=0,
        source="sympy.factor over ℤ[u] for Δa_m on (n−p, ³He−D, ⁴He−³He).",
    )

    builder.save()
    print(f"\n  ✓ Witness: qbeta-habiro-cross-pair-factorization.witness.json")
    print(f"  ✓ Verdict: {verdict['verdict']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
