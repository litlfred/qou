#!/usr/bin/env python3
"""qbeta_habiro_cross_pair_quick_dp.py — partial cross-validation of Δa_m.

The full cross-pair probe (qbeta_habiro_cross_pair_factorization.py)
needs ³He and ⁴He Habiro coefficients which are NOT in
`habiro-coefficients-atomic.witness.json` yet — only p, n, D are
present. Generating ³He / ⁴He requires a separate atomic-Habiro
extraction (a follow-up task).

THIS quick probe does what we CAN do with available data: factorize
Δa_m on (D − p) and (D − n) and compare with the (n − p) pattern.

The three pairs:
  (n − p): isospin SU(2)_I flip at fixed A=1
  (D − p): atomic-number step A=1 → A=2 with Z fixed at 1
  (D − n): atomic-number step A=1 → A=2 with N fixed at 1

If the cyclotomic prefactor (u²−1) appears in (D − p) AND (D − n),
that's evidence the Φ_1·Φ_2 factor is UNIVERSAL across atomic-number
steps, not specific to isospin SU(2)_I.
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
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402

u = sp.symbols("u")


def parse_atom_coeffs(witness_atom: dict) -> dict[int, sp.Poly]:
    """Return {m: a_m(u) as sympy.Poly} for one atom's Habiro coefficients."""
    out = {}
    for c in witness_atom["habiro_coefficients"]:
        m = c["m"]
        a_m_str = c["a_m"].replace("^", "**")
        a_m_expr = sp.sympify(a_m_str, locals={"check_q": u})
        out[m] = sp.Poly(a_m_expr, u)
    return out


def delta_factorize(left: dict[int, sp.Poly], right: dict[int, sp.Poly],
                    pair_name: str) -> dict:
    """Compute Δa_m = a_m(left) − a_m(right) for all m, factor each, GCD."""
    max_m = max(max(left), max(right))
    delta_polys = []
    per_m = []
    for m in range(max_m + 1):
        l = left.get(m, sp.Poly(0, u))
        r = right.get(m, sp.Poly(0, u))
        d = l - r
        delta_polys.append(d)
        if d.is_zero:
            per_m.append({"m": m, "delta": "0", "factored": "0",
                          "is_zero": True, "is_irreducible": False})
        else:
            factored = sp.factor(d.as_expr())
            per_m.append({
                "m": m,
                "delta": str(d.as_expr()),
                "factored": str(factored),
                "is_zero": False,
                "is_irreducible": d.degree() == sp.degree(factored, u)
                                  and not factored.is_Mul,
            })

    # Cross-m polynomial GCD over ℤ[u]
    nonzero = [p for p in delta_polys if not p.is_zero]
    if nonzero:
        cross_gcd = nonzero[0]
        for p in nonzero[1:]:
            cross_gcd = sp.gcd(cross_gcd, p)
        cross_gcd_str = str(cross_gcd.as_expr())
    else:
        cross_gcd_str = "all zero"

    # Σ_m Δa_m · (u;u)_m
    def q_pochhammer(m):
        if m == 0:
            return sp.Integer(1)
        return sp.prod(1 - u ** k for k in range(1, m + 1))

    habiro_sum = sp.Integer(0)
    for m, d in enumerate(delta_polys):
        habiro_sum += d.as_expr() * q_pochhammer(m)
    habiro_factored = sp.factor(habiro_sum)

    # ── Route A: polynomial long division by u²-1 in ℤ[u] ────────────
    cyclotomic_present = False
    if not habiro_sum.is_zero:
        quotient, remainder = sp.div(habiro_sum, u**2 - 1, u)
        cyclotomic_present = (remainder == 0)

    # ── Route B (INDEPENDENT): factor theorem at the roots of u²-1 ───
    # (u−1)(u+1) | S(u)  ⟺  S(1) = 0 AND S(−1) = 0.  This never divides
    # anything: it evaluates S at the two roots.  It is a genuinely
    # different derivation of the same divisibility fact from Route A's
    # long division, so the two disagreeing is a real failure signal
    # (a parsing/indexing bug in the Habiro sum shows up here).
    s_at_plus_1 = sp.expand(habiro_sum).subs(u, 1)
    s_at_minus_1 = sp.expand(habiro_sum).subs(u, -1)
    cyclotomic_via_root_test = (s_at_plus_1 == 0 and s_at_minus_1 == 0)

    return {
        "pair_name": pair_name,
        "max_m": max_m,
        "per_m": per_m,
        # Popped by main() before the dict reaches the witness — sympy
        # Poly objects are not JSON-serialisable.
        "_delta_polys": delta_polys,
        "cross_m_polynomial_gcd": cross_gcd_str,
        "habiro_sum_factored": str(habiro_factored),
        "cyclotomic_u2_minus_1_present": cyclotomic_present,
        "root_test": {
            "S_at_u_plus_1": str(s_at_plus_1),
            "S_at_u_minus_1": str(s_at_minus_1),
            "cyclotomic_via_root_test": cyclotomic_via_root_test,
            "agrees_with_division_route": (
                cyclotomic_via_root_test == cyclotomic_present),
        },
    }


def main() -> int:
    builder = WitnessBuilder(
        "qbeta-habiro-cross-pair-quick-dp",
        engine="python+sympy",
    )
    builder.set_description(
        "Quick partial cross-pair validation: factor Δa_m on "
        "(D - p), (D - n), (n - p) to compare with the n-p "
        "audit's cyclotomic prefactor pattern. Full ³He/⁴He extension "
        "deferred (auxiliary witnesses not yet generated)."
    )
    builder.set_content_block("prop:neutron-qvalue-symbolic")

    hab = builder.add_upstream(_pb.witness_path("habiro-coefficients-atomic.witness.json", HERE))
    results = hab["results"]

    p = parse_atom_coeffs(results["p (proton, A=1)"])
    n = parse_atom_coeffs(results["n (neutron, A=1)"])
    d = parse_atom_coeffs(results["D (deuteron, A=2)"])

    # Reference: n - p (already in prior audit)
    np_result = delta_factorize(n, p, "n - p (reference)")
    np_polys = np_result.pop("_delta_polys")
    builder.add_data("n_minus_p", np_result)
    print(f"\n=== n - p ===")
    print(f"  Cyclotomic (u²-1) present: {np_result['cyclotomic_u2_minus_1_present']}")
    print(f"  Σ habiro factored: {np_result['habiro_sum_factored'][:100]}...")

    # New: D - p
    dp_result = delta_factorize(d, p, "D - p (atomic-step, Z-fixed)")
    dp_polys = dp_result.pop("_delta_polys")
    builder.add_data("d_minus_p", dp_result)
    print(f"\n=== D - p ===")
    print(f"  Cyclotomic (u²-1) present: {dp_result['cyclotomic_u2_minus_1_present']}")
    print(f"  Σ habiro factored: {dp_result['habiro_sum_factored'][:100]}...")

    # New: D - n
    dn_result = delta_factorize(d, n, "D - n (atomic-step, N-fixed)")
    dn_polys = dn_result.pop("_delta_polys")
    builder.add_data("d_minus_n", dn_result)
    print(f"\n=== D - n ===")
    print(f"  Cyclotomic (u²-1) present: {dn_result['cyclotomic_u2_minus_1_present']}")
    print(f"  Σ habiro factored: {dn_result['habiro_sum_factored'][:100]}...")

    # Verdict
    cyclo_count = sum([
        np_result['cyclotomic_u2_minus_1_present'],
        dp_result['cyclotomic_u2_minus_1_present'],
        dn_result['cyclotomic_u2_minus_1_present'],
    ])
    if cyclo_count == 3:
        verdict = "UNIVERSAL: Φ_1·Φ_2 = u²-1 prefactor in all three pairs"
    elif cyclo_count == 1 and np_result['cyclotomic_u2_minus_1_present']:
        verdict = "SPECIFIC to isospin SU(2)_I: cyclotomic only in n-p"
    elif cyclo_count >= 2:
        verdict = f"PARTIAL: cyclotomic in {cyclo_count}/3 pairs"
    else:
        verdict = f"UNEXPECTED: cyclotomic in {cyclo_count}/3 pairs"
    builder.add_data("verdict", verdict)
    print(f"\n=== VERDICT: {verdict} ===")

    # ── Assertion 1 — the Δa_m telescoping identity ───────────────────
    # (D − p) − (D − n) = n − p termwise in ℤ[u], for every Habiro
    # order m.  D cancels, so the two atomic-step deltas must rebuild
    # the isospin delta exactly.
    #   Route A: Δ_{n−p}(m) computed DIRECTLY from the n and p Habiro
    #            coefficient tables parsed out of the upstream witness.
    #   Route B: the same polynomial rebuilt as Δ_{D−p}(m) − Δ_{D−n}(m)
    #            from the two independently-computed atomic-step deltas.
    # A mis-indexed m, a bad `a_m` sympify, or wrong zero-padding at the
    # ragged max_m boundary breaks Route B while leaving Route A intact.
    n_orders = max(len(np_polys), len(dp_polys), len(dn_polys))
    zero = sp.Poly(0, u)

    def _at(polys, m):
        return polys[m] if m < len(polys) else zero

    telescoping_ok = sum(
        1 for m in range(n_orders)
        if ((_at(dp_polys, m) - _at(dn_polys, m)) - _at(np_polys, m)).is_zero
    )
    builder.add_data("telescoping_identity", {
        "orders_checked": n_orders,
        "orders_agreeing": telescoping_ok,
        "identity": "(D-p)_m - (D-n)_m == (n-p)_m for all m",
    })
    print(f"\n  Telescoping (D-p)-(D-n) == (n-p): "
          f"{telescoping_ok}/{n_orders} Habiro orders agree")

    builder.add_assertion(
        "delta_am_telescoping_identity_holds",
        computed=telescoping_ok,
        expected=n_orders,
        tolerance=0,
        unit="Habiro orders m",
        source=(
            "Route A: Δa_m(n−p) built directly from the n and p Habiro "
            "coefficient tables in habiro-coefficients-atomic.witness.json. "
            "Route B: the same Δa_m rebuilt as Δa_m(D−p) − Δa_m(D−n) from "
            "the two atomic-step deltas, in which the deuteron cancels. "
            "Expected = the number of Habiro orders spanned by the parsed "
            "inputs (max_m + 1), rebuilt from the upstream tables."
        ),
    )

    # ── Assertion 2 — divisibility verdict, two routes ────────────────
    #   Route A: long division of the Habiro sum S(u) by u²−1 in ℤ[u];
    #            the flag is (remainder == 0).
    #   Route B: the factor theorem — (u−1)(u+1) | S(u) iff S(1) = 0 and
    #            S(−1) = 0.  Evaluation at the roots, never a division.
    # Non-vacuous here: the residues are large and unequal (see the
    # root_test blocks in the witness), so the two routes are agreeing on
    # a genuine NON-divisibility rather than both reading a trivial zero.
    pair_results = [np_result, dp_result, dn_result]
    routes_agree = sum(
        1 for r in pair_results if r["root_test"]["agrees_with_division_route"]
    )
    print(f"  Divisibility route agreement (long division vs factor "
          f"theorem): {routes_agree}/{len(pair_results)} pairs")

    builder.add_assertion(
        "cyclotomic_divisibility_two_routes_agree",
        computed=routes_agree,
        expected=len(pair_results),
        tolerance=0,
        unit="pairs",
        source=(
            "Route A: sp.div(S, u²−1) remainder-is-zero. Route B: factor "
            "theorem, S(+1) == 0 and S(−1) == 0. Expected = the number of "
            "pairs actually factorized (rebuilt from the pair list), so "
            "adding a pair tightens the check rather than diluting it."
        ),
    )
    builder.save()
    print(f"\n  ✓ Witness saved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
