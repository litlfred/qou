#!/usr/bin/env python3
"""
qbeta_habiro_phi8_squared_from_z_squared_probe.py — ALGEBRAIC VERIFICATION
==========================================================================

Test the hypothesis that the universal Φ_8² = (u^4+1)² factor observed
across all atomic-step Habiro element factorizations ((D−n), (³He−D),
(⁴He−³He)) arises **mechanically** from the z(q)² interface factor in
the Phase 5q closed forms — and NOT from a strand-doubling chain.

CONTEXT
=======

The Phase 5q closed forms all contain z(q)^k factors:
  - tr_M(D, q)  = τ_p · τ_n · z(q)^1
  - tr_M(³He, q) = τ_p² · τ_n · z(q)^2
  - tr_M(⁴He, q) = τ_p² · τ_n² · z(q)^2 · (z − h)(q)

where z(q) = 1/(√q + 1/√q) = u/(u² + 1) in terms of u = √q.

THE HYPOTHESIS GETS RESOLVED
============================

Sections 1-4 test directly. Section 5 issues verdict + identifies the
specific Habiro coefficient where Φ_8 first appears.

USAGE
-----
  python3 -u qbeta_habiro_phi8_squared_from_z_squared_probe.py 2>&1 \
      | tee /tmp/phi8_mechanism.log

Ref: docs/audits/2026-06-01-qbeta-habiro-strand-doubling-FALSIFIED.md
Ref: docs/audits/2026-06-01-qbeta-habiro-phase5q-dn-convention-test.md
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

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder, record_upstream  # noqa: E402
from habiro_coefficients_atomic import trace_diff_numerator as _trace_diff  # noqa: E402
from habiro_coefficients_atomic import cyclotomic_expansion as _cyc_expand  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from q_parameter import Q_MP as Q0  # noqa: E402
# The canonical serializer, NOT a canonical algorithm import: the primitives
# below stay a deliberate local mirror, but anything this probe writes as TEXT
# goes out in the canonical `u` (bean qou-0ndb). Today its `u` IS U_CANONICAL,
# so every string here is already right — by luck of the caller's variable
# name, which is precisely the property that failed four times in this family.
from habiro_coefficients_atomic import str_in_u  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# 50-dps for q₀ verification
set_compute_dps()


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# ───────── Algorithm primitives (mirror habiro_coefficients_atomic) ─────────

def to_u_polynomial(expr_in_q, q, u):
    """q → u², clear u-denominators. Returns (p_in_u, shift, denom_str)."""
    expr_u = sp.together(expr_in_q.subs(q, u ** 2))
    num, den = sp.fraction(expr_u)
    num = sp.expand(num)
    den = sp.expand(den)
    p_expanded = sp.expand(num)
    poly = sp.Poly(p_expanded, u)
    monoms = poly.monoms()
    if not monoms:
        return sp.Integer(0), 0, str_in_u(den, u)
    min_pow = min(int(m[0]) for m in monoms)
    shift = -min_pow if min_pow < 0 else 0
    p_shifted = sp.expand(p_expanded * u ** shift)
    return p_shifted, shift, str_in_u(sp.expand(den), u)


def cyclotomic_expansion(p_in_u, u, max_m=30):
    """Sequential Pochhammer division: p(u) = Σ a_m · (u;u)_m."""
    p = sp.Poly(sp.expand(p_in_u), u)
    coeffs = []
    current = p
    for m in range(max_m):
        if current.is_zero:
            break
        next_factor = sp.Poly(1 - u ** (m + 1), u)
        quotient, a_m = sp.div(current, next_factor, u)
        a_m_expr = a_m.as_expr()
        coeffs.append({
            "m": m,
            "a_m": str(a_m_expr),
            "a_m_expr": a_m_expr,
            "deg_a_m": int(a_m.degree()) if a_m_expr != 0 else 0,
        })
        current = quotient
    return coeffs


def q_pochhammer(u, m):
    """(u; u)_m = Π_{k=1..m} (1 − u^k)."""
    if m == 0:
        return sp.Integer(1)
    return sp.prod(1 - u ** k for k in range(1, m + 1))


def residue_mod_phi8(poly, u):
    """Residue of `poly` in ℚ[u]/(Φ_8) = ℚ[u]/(u⁴+1), as 4 coefficients.

    THE SECOND ROUTE. `cyclotomic_factor_count` below decides Φ_8 |
    S(u) by repeated polynomial LONG DIVISION (`sp.div`). This decides
    the same question without dividing anything: it folds the
    coefficient list of S using u⁴ = −1, so the coefficient of u^i
    lands on u^(i mod 4) with sign (−1)^(i//4). Φ_8 | S iff all four
    residues vanish.

    Because Φ_8 is irreducible over ℚ and Φ_8' = 4u³ is coprime to it,
    Φ_8² | S iff Φ_8 divides both S and S' — so the same fold applied
    to S' settles the SQUARE, which is the multiplicity this probe's
    whole verdict turns on.

    Takes and keeps `sp.Poly`: the Δa_m chains reach several hundred
    terms, and folding them as loose `Expr` builds Add/Mul trees deep
    enough to hit Python's recursion limit inside sympy's flattener.
    """
    p = poly if isinstance(poly, sp.Poly) else sp.Poly(sp.expand(poly), u)
    buckets = [[], [], [], []]
    for (i,), c in zip(p.monoms(), p.coeffs()):
        buckets[i % 4].append(c if (i // 4) % 2 == 0 else -c)
    return [sp.Add(*b) if b else sp.Integer(0) for b in buckets]


def phi8_power_via_root_test(expr, u, cap=3):
    """Φ_8-multiplicity of `expr` by the residue fold, capped at `cap`.

    Uses `residue_mod_phi8` on S, S', S'', … : Φ_8^k | S iff Φ_8
    divides the first k−1 derivatives as well (Φ_8 irreducible, Φ_8'
    coprime to Φ_8). No `sp.div` anywhere. Stays in `sp.Poly` so
    `.diff` is a coefficient shift rather than an expression rewrite.
    """
    p = expr if isinstance(expr, sp.Poly) else sp.Poly(sp.expand(expr), u)
    if p.is_zero:
        return 0
    power = 0
    for _ in range(cap):
        if any(c != 0 for c in residue_mod_phi8(p, u)):
            break
        power += 1
        p = p.diff(u)
        if p.is_zero:
            break
    return power


def cyclotomic_factor_count(expr, u, max_n=20):
    """For each n = 1..max_n, count how many times Φ_n(u) divides expr.

    Returns dict {n: power_of_Phi_n}.
    """
    counts = {}
    for n in range(1, max_n + 1):
        Phi_n = sp.cyclotomic_poly(n, u)
        current = sp.expand(expr)
        power = 0
        while True:
            quotient, rem = sp.div(current, Phi_n, u)
            if rem == 0:
                power += 1
                current = quotient
            else:
                break
        if power > 0:
            counts[n] = power
    return counts


# ───────── Section 1: Habiro expansion of z(q)^k alone ─────────

def habiro_of_z_pow_k(k, u, q, max_m=20):
    """Compute the Habiro expansion of z(q)^k = u^k/(u²+1)^k.

    Treats it as a STANDALONE trace (which is a category-theoretic
    abstraction — z(q) isn't itself a Markov trace, but we want to
    isolate its cyclotomic signature in the Habiro decomposition).
    """
    log(f"  --- z(q)^{k} Habiro decomposition ---")
    z = q**3 / (q**2 + 1)
    expr = sp.together(z ** k)
    p_u, shift, denom_str = to_u_polynomial(expr, q, u)
    log(f"    z(q)^{k} as p(u): deg = {sp.Poly(p_u, u).degree()}, "
        f"shift = u^{shift}, denom = {denom_str}")
    log(f"    p(u) = {sp.factor(p_u)}")

    coeffs = cyclotomic_expansion(p_u, u, max_m=max_m)
    log(f"    → {len(coeffs)} nonzero Habiro coefficients")
    for entry in coeffs[:12]:
        a_repr = entry["a_m"]
        if len(a_repr) > 80:
            a_repr = a_repr[:77] + "..."
        log(f"      a_{entry['m']} (deg {entry['deg_a_m']}) = {a_repr}")
    if len(coeffs) > 12:
        log(f"      ... ({len(coeffs) - 12} more)")

    # Reconstruct Σ a_m · (u;u)_m and factor
    habiro_sum = sp.Integer(0)
    for entry in coeffs:
        habiro_sum += sp.expand(entry["a_m_expr"] * q_pochhammer(u, entry["m"]))
    habiro_sum = sp.expand(habiro_sum)

    log(f"    deg(habiro_sum) = {sp.Poly(habiro_sum, u).degree() if habiro_sum != 0 else 0}")
    factored = sp.factor(habiro_sum)
    factored_str = str(factored)
    log(f"    Σ a_m · (u;u)_m = {factored_str[:200]}")
    if len(factored_str) > 200:
        log(f"      ...{len(factored_str)} chars total")

    cy_counts = cyclotomic_factor_count(habiro_sum, u, max_n=16)
    log(f"    Cyclotomic factor map: {cy_counts}")
    phi8_power = cy_counts.get(8, 0)
    phi8_root = phi8_power_via_root_test(habiro_sum, u)
    reconstructs = bool(sp.expand(habiro_sum - p_u) == 0)
    log(f"    Φ_8 power in habiro_sum: {phi8_power} "
        f"(division route) / {phi8_root} (residue-fold route)")
    log(f"    Σ a_m·(u;u)_m == p(u): {reconstructs}")

    return {
        "k": k,
        "p_in_u_factored": str_in_u(sp.factor(p_u), u),
        "shift": shift,
        "denom_in_u": denom_str,
        "num_coeffs": len(coeffs),
        "habiro_sum_factored": factored_str,
        "cyclotomic_counts": cy_counts,
        "phi8_power": phi8_power,
        "phi8_power_root_test": phi8_root,
        "reconstructs_input_polynomial": reconstructs,
    }


# ───────── Section 2: Pochhammer cyclotomic signature ─────────

def analyse_pochhammer_factors(u, max_m=20):
    """For each m, factor (u;u)_m and identify cyclotomic content.

    (u;u)_m = Π_{k=1..m} (1 − u^k) = (−1)^m · Π_{k=1..m} (u^k − 1)
            = (−1)^m · Π_{k=1..m} Π_{d|k} Φ_d(u)

    So (u;u)_m's Φ_d(u) power equals #{k in [1,m]: d|k} = ⌊m/d⌋.

    For Φ_8: ⌊m/8⌋, so Φ_8 power is 0 for m<8, 1 for m∈[8,15], 2 for m∈[16,23].
    """
    log("  --- Pochhammer cyclotomic decomposition ---")
    table = []
    for m in range(max_m + 1):
        poch = q_pochhammer(u, m)
        cy_counts = cyclotomic_factor_count(poch, u, max_n=20) if m > 0 else {}
        phi8_power = cy_counts.get(8, 0)
        # SECOND ROUTE to the same number: the docstring's counting
        # law. (u;u)_m = Π_{k≤m}(1−u^k) and 1−u^k = Π_{d|k} Φ_d, so
        # Φ_8's multiplicity is #{k ≤ m : 8 | k} = ⌊m/8⌋ — a divisor
        # count over the integers, with no polynomial in sight. The
        # docstring above states this law; nothing tested it.
        phi8_predicted = m // 8
        log(f"    (u;u)_{m}: Φ_8 power = {phi8_power} "
            f"(divided) / {phi8_predicted} (⌊m/8⌋)")
        table.append({"m": m, "cyclotomic_counts": cy_counts,
                      "phi8_power": phi8_power,
                      "phi8_power_floor_m_over_8": phi8_predicted})
    return table


# ───────── Section 3: z(q)^2 − z(q)^1 interference ─────────

def habiro_of_z_diff(u, q, max_m=20):
    """Compute Habiro expansion of z(q)^2 − z(q)^1 and z(q)^2 − z(q)^1·z(q)."""
    log("  --- z(q)² − z(q)¹ Habiro decomposition (interference test) ---")
    z = q**3 / (q**2 + 1)
    expr_diff = sp.together(z ** 2 - z)
    log(f"    z² − z = {sp.factor(expr_diff)}")
    p_u, shift, denom_str = to_u_polynomial(expr_diff, q, u)
    log(f"    p(u) (z² − z): deg = "
        f"{sp.Poly(p_u, u).degree() if p_u != 0 else 0}, "
        f"shift = u^{shift}, denom = {denom_str}")
    log(f"    p(u) factored = {sp.factor(p_u)}")

    coeffs = cyclotomic_expansion(p_u, u, max_m=max_m)
    log(f"    → {len(coeffs)} nonzero Habiro coefficients")

    habiro_sum = sp.Integer(0)
    for entry in coeffs:
        habiro_sum += sp.expand(entry["a_m_expr"] * q_pochhammer(u, entry["m"]))
    habiro_sum = sp.expand(habiro_sum)

    factored = sp.factor(habiro_sum)
    cy_counts = cyclotomic_factor_count(habiro_sum, u, max_n=16)
    log(f"    Σ a_m · (u;u)_m for (z²−z) = {str(factored)[:200]}")
    log(f"    Cyclotomic factor map: {cy_counts}")
    return {
        "diff_p_in_u": str_in_u(sp.factor(p_u), u),
        "habiro_sum_factored": str(factored),
        "cyclotomic_counts": cy_counts,
        "phi8_power": cy_counts.get(8, 0),
        "phi8_power_root_test": phi8_power_via_root_test(habiro_sum, u),
        "reconstructs_input_polynomial": bool(
            sp.expand(habiro_sum - p_u) == 0),
    }


# ───────── Section 4: Compute the *actual* Δa_m chains for D−n, ³He−D, ⁴He−³He ─────────

def extract_helium_witnesses(u):
    """Load existing helium-3, helium-4, atomic witnesses and recompute
    Δa_m factorizations to confirm the Φ_8² universal observation.

    Also locates the SMALLEST m for which Δa_m introduces a non-trivial
    contribution carrying Φ_8 — this pins where Φ_8 actually enters.
    """
    log("  --- Loading existing witnesses ---")
    atomic_path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    he3_path = _pb.witness_path("habiro-coefficients-helium-3.witness.json", HERE)
    he4_path = _pb.witness_path("habiro-coefficients-helium-4.witness.json", HERE)

    atomic = record_upstream(atomic_path, _UPSTREAM_RECORDS)
    he3 = record_upstream(he3_path, _UPSTREAM_RECORDS) if he3_path.exists() else None
    he4 = record_upstream(he4_path, _UPSTREAM_RECORDS) if he4_path.exists() else None

    # `parse_coeffs` lived here. It is gone with the a_m-differencing it fed:
    # its own docstring records that it had to map BOTH "u" and "check_q" to one
    # symbol precisely because the pairs below subtracted coefficients from two
    # differently-serialized witnesses. Differencing the traces instead removes
    # the subtraction, and with it the need for that reconciliation (qou-0ndb).

    # Carry the TRACES, not the a_m. A witness's a_m expand its own
    # DENOMINATOR-CLEARED numerator p = d*t, so Sum (a_m^X - a_m^Y)(u;u)_m
    # reconstructs d_X*t_X - d_Y*t_Y, which is proportional to the pair
    # difference t_X - t_Y only where the denominators agree at the evaluation
    # point. Proved sorry-free in QOU/Habiro/MirrorPairNormalisation.lean
    # (coeffDiff_at_coincidence: dX*t - dY*t = (dX - dY)*t), so a mismatch
    # contributes the denominator GAP times the common value and the cyclotomic
    # multiplicities read off it are not the pair's. Bean qou-0ndb.
    n_tr = atomic["results"]["n (neutron, A=1)"]["tr_M_in_q"]
    d_tr = atomic["results"]["D (deuteron, A=2)"]["tr_M_in_q"]

    pairs = []
    pairs.append(("(D − n)", d_tr, n_tr))

    if he3 is not None:
        pairs.append(("(³He − D)", he3["tr_M_in_q"], d_tr))
    if he4 is not None and he3 is not None:
        pairs.append(("(⁴He − ³He)", he4["tr_M_in_q"], he3["tr_M_in_q"]))

    results = []
    for label, big_tr, small_tr in pairs:
        log(f"\n  --- Δa_m {label} ---")
        # Habiro-expand the TRUE difference; M_first is defined on that
        # expansion, so the correct object is the expansion OF the difference,
        # not a difference of two expansions (qou-0ndb).
        diff = _trace_diff(big_tr, small_tr, u, label=label)
        big = {c["m"]: sp.sympify(c["a_m"], locals={"u": u})
               for c in _cyc_expand(diff, u)}
        small = {}
        max_m = max(big.keys(), default=0)

        # Track WHERE Φ_8 first enters: compute running prefix sums and
        # find smallest M such that Σ_{m=0..M} Δa_m·(u;u)_m carries Φ_8.
        first_phi8_m = None
        first_phi8_sq_m = None
        prefix_sum = sp.Integer(0)
        for m in range(max_m + 1):
            delta = sp.expand(big.get(m, sp.Integer(0))
                              - small.get(m, sp.Integer(0)))
            if delta != 0:
                prefix_sum += sp.expand(delta * q_pochhammer(u, m))
                prefix_sum = sp.expand(prefix_sum)
            # Check Φ_8 power of prefix sum
            Phi_8 = u ** 4 + 1
            current = prefix_sum
            phi8_pow = 0
            while True:
                quot, rem = sp.div(current, Phi_8, u)
                if rem == 0 and current != 0:
                    phi8_pow += 1
                    current = quot
                else:
                    break
            if phi8_pow >= 1 and first_phi8_m is None:
                first_phi8_m = m
            if phi8_pow >= 2 and first_phi8_sq_m is None:
                first_phi8_sq_m = m

        habiro_sum = prefix_sum  # Final sum (all m's added)
        factored = sp.factor(habiro_sum)
        cy_counts = cyclotomic_factor_count(habiro_sum, u, max_n=16)
        phi8_power = cy_counts.get(8, 0)
        phi8_root = phi8_power_via_root_test(habiro_sum, u, cap=4)
        log(f"    cyclotomic factor map: {cy_counts}")
        log(f"    Φ_8 power = {phi8_power} (division route) / "
            f"{phi8_root} (residue-fold route)")
        log(f"    First m for which prefix sum has Φ_8 ≥ 1: m = {first_phi8_m}")
        log(f"    First m for which prefix sum has Φ_8 ≥ 2: m = {first_phi8_sq_m}")
        log(f"    factored (first 200 chars): {str(factored)[:200]}")
        results.append({
            "pair": label,
            "cyclotomic_counts": cy_counts,
            "phi8_power": phi8_power,
            "phi8_power_root_test": phi8_root,
            "first_phi8_m": first_phi8_m,
            "first_phi8_sq_m": first_phi8_sq_m,
            "factored_excerpt": str(factored)[:400],
        })
    return results


# ───────── Section 5: Compare convention z(q)^k mechanism vs reality ─────────

def main() -> int:
    t0 = time.time()
    q = sp.Symbol("q", positive=True, real=True)
    u = sp.Symbol("u", positive=True, real=True)

    log("=" * 78)
    log("Φ_8² mechanism probe — z(q)² vs Pochhammer boundary vs other")
    log("=" * 78)

    builder = WitnessBuilder(
        "qbeta-habiro-phi8-squared-from-z-squared-probe",
        engine="python+sympy",
    )
    builder.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    builder.set_description(
        "Algebraic verification: tests whether the universal Φ_8² factor "
        "observed in atomic-step Δa_m Habiro factorizations arises "
        "mechanically from z(q)^k interface factors in Phase 5q closed "
        "forms, or from a different mechanism (e.g., the (u;u)_m=8 "
        "Pochhammer boundary). Computes Habiro decompositions of "
        "z(q)^k alone for k=1,2,3; analyses Φ_8 emergence in (u;u)_m "
        "factors; cross-checks against actual Δa_m factorizations and "
        "pins the first m for which Φ_8 enters."
    )
    builder.set_content_block("prop:neutron-qvalue-symbolic")

    # ─── Section 1: standalone z^k Habiro ────────────────────────────
    log("\n[1] Habiro decomposition of z(q)^k for k = 1, 2, 3")
    log("    z(q) = u/(u²+1) = u/Φ_4(u), so z(q)^k = u^k/Φ_4(u)^k")
    log("    The DENOMINATOR Φ_4(u)^k is cleared by `to_u_polynomial`,")
    log("    becoming part of the p(u) preamble.")
    z_k_results = {}
    for k in (1, 2, 3):
        z_k_results[k] = habiro_of_z_pow_k(k, u, q, max_m=16)

    builder.add_data("z_pow_k_habiro_results", {
        str(k): {
            "p_in_u_factored": v["p_in_u_factored"],
            "shift": v["shift"],
            "denom_in_u": v["denom_in_u"],
            "num_coeffs": v["num_coeffs"],
            "habiro_sum_factored": v["habiro_sum_factored"],
            "cyclotomic_counts": v["cyclotomic_counts"],
            "phi8_power": v["phi8_power"],
        }
        for k, v in z_k_results.items()
    })

    # ─── Section 2: Pochhammer cyclotomic ─────────────────────────────
    log("\n[2] Cyclotomic decomposition of (u;u)_m for m = 0, ..., 20")
    log("    1 − u^k = Π_{d|k} Φ_d(u), so (u;u)_m gathers Φ_d(u) with")
    log("    multiplicity #{k≤m : d|k} = ⌊m/d⌋.")
    poch_table = analyse_pochhammer_factors(u, max_m=20)
    builder.add_data("pochhammer_cyclotomic_table", poch_table)

    # ─── Section 3: z(q)^2 − z(q)^1 interference ──────────────────────
    log("\n[3] Habiro of z² − z (interference probe)")
    z_diff_result = habiro_of_z_diff(u, q, max_m=16)
    builder.add_data("z_diff_habiro_result", z_diff_result)

    # ─── Section 4: Real Δa_m chains ──────────────────────────────────
    log("\n[4] Actual Δa_m factorization Φ_8 counts (existing witnesses)")
    delta_results = extract_helium_witnesses(u)
    builder.add_data("actual_delta_am_phi8_counts", delta_results)

    # ─── Section 5: Verdict ───────────────────────────────────────────
    log("\n[5] Verdict — algebraic origin of Φ_8²")
    log("=" * 78)

    z2_phi8 = z_k_results[2]["phi8_power"]
    z3_phi8 = z_k_results[3]["phi8_power"]
    z1_phi8 = z_k_results[1]["phi8_power"]
    poch8_phi8 = next((row["phi8_power"] for row in poch_table if row["m"] == 8),
                     0)
    poch4_phi8 = next((row["phi8_power"] for row in poch_table if row["m"] == 4),
                     0)
    poch16_phi8 = next((row["phi8_power"] for row in poch_table if row["m"] == 16),
                     0)
    delta_phi8s = [r["phi8_power"] for r in delta_results]
    delta_first_phi8 = [r["first_phi8_m"] for r in delta_results]
    delta_first_phi8_sq = [r["first_phi8_sq_m"] for r in delta_results]

    log(f"  Φ_8 power in z(q)^1 Habiro sum:   {z1_phi8}")
    log(f"  Φ_8 power in z(q)^2 Habiro sum:   {z2_phi8}")
    log(f"  Φ_8 power in z(q)^3 Habiro sum:   {z3_phi8}")
    log(f"  Φ_8 power in (u;u)_4 alone:       {poch4_phi8}")
    log(f"  Φ_8 power in (u;u)_8 alone:       {poch8_phi8}")
    log(f"  Φ_8 power in (u;u)_16 alone:      {poch16_phi8}")
    log(f"  Φ_8 power in actual Δa_m chains:  {delta_phi8s}")
    log(f"  First m where prefix sum has Φ_8 ≥ 1: {delta_first_phi8}")
    log(f"  First m where prefix sum has Φ_8 ≥ 2: {delta_first_phi8_sq}")

    # Determine verdict
    if z2_phi8 == 2 and z3_phi8 == 2:
        verdict_short = "FROM_Z_SQUARED"
        verdict = (
            "FROM-Z-SQUARED: Φ_8² is the Habiro signature of the z(q)² "
            "factor itself. Both z(q)² and z(q)³ Habiro sums carry exactly "
            "Φ_8² as a cyclotomic factor."
        )
    elif z2_phi8 == 0 and z1_phi8 == 0 and poch8_phi8 >= 1:
        # z(q)^k alone gives NO cyclotomic content (just u^k).
        # Φ_8 emerges purely from the q-Pochhammer (1-u^8) factor at m=8
        # and onwards, weighted by the Habiro coefficients of the
        # actual tr_M.
        verdict_short = "FROM_POCHHAMMER_BOUNDARY"
        verdict = (
            "FROM-POCHHAMMER-BOUNDARY: z(q)^k ALONE carries NO cyclotomic "
            "content in its Habiro sum (Σ a_m·(u;u)_m = u^k, a monomial — "
            "the entire cyclotomic structure of z(q)^k is in the "
            "DENOMINATOR Φ_4(u)^k, which is cleared by to_u_polynomial). "
            "Φ_8 enters the Habiro sum mechanically only via (u;u)_m for "
            "m ≥ 8 (where 1−u^8 = Φ_1·Φ_2·Φ_4·Φ_8). The OBSERVED Φ_8² in "
            "Δa_m factorizations comes from the interaction of the actual "
            "tr_M(X)−tr_M(Y) Habiro coefficients with (u;u)_m factors at "
            "m ≥ 8, NOT from z(q)² itself."
        )
    elif z2_phi8 != z3_phi8:
        verdict_short = "Z_POWER_INDUCED_BUT_NOT_UNIVERSAL"
        verdict = (
            f"PARTIAL: Φ_8 power in z(q)^2 = {z2_phi8} ≠ Φ_8 power in z(q)^3 = {z3_phi8}. "
            "The z-factor mechanism is sensitive to the power k, not "
            "universally Φ_8² across atomic steps. Needs deeper analysis."
        )
    else:
        verdict_short = "MIXED_MECHANISM"
        verdict = (
            f"MIXED: z(q)^k contributes (z2_phi8 = {z2_phi8}) and Pochhammer "
            f"boundary contributes ((u;u)_8 has Φ_8^{poch8_phi8}). The "
            "observed Φ_8² in Δa_m arises from the interaction of both."
        )

    log("")
    log(f"VERDICT: {verdict_short}")
    log("")
    log(verdict)
    log("=" * 78)

    builder.add_data("verdict_short", verdict_short)
    builder.add_data("verdict", verdict)

    # ─── Numerical cross-check at q_0 ─────────────────────────────────
    log("\n[6] Numerical cross-check at q_0 (50 dps)")
    q0_mp = mp.mpf(str(Q0))
    u0_mp = mp.sqrt(q0_mp)
    z_at_q0 = q0_mp**3 / (q0_mp**2 + 1)
    log(f"  q_0 = {float(q0_mp):.16f}")
    log(f"  u_0 = √q_0 = {float(u0_mp):.16f}")
    log(f"  z(q_0) = {float(z_at_q0):.16f}")
    log(f"  z(q_0)² = {float(z_at_q0 ** 2):.16f}")
    # Φ_8 at u_0
    phi8_at_u0 = float(u0_mp ** 4 + 1)
    log(f"  Φ_8(u_0) = u_0^4 + 1 = {phi8_at_u0:.16f}")

    builder.add_data("numerical_q0", {
        "q_0": float(q0_mp),
        "u_0": float(u0_mp),
        "z_at_q0": float(z_at_q0),
        "z_sq_at_q0": float(z_at_q0 ** 2),
        "phi8_at_u0": phi8_at_u0,
    })

    # ── Assertions ────────────────────────────────────────────────────
    # Every Φ_8 count above comes out of ONE routine —
    # `cyclotomic_factor_count`, repeated `sp.div` by
    # `sp.cyclotomic_poly(n, u)`. The verdict is a comparison of those
    # counts, so the counts themselves need a second route, and so does
    # the Habiro expansion that produces the polynomials they act on.

    # (1) The expansion is an identity, not an approximation.
    #   Route A: `cyclotomic_expansion` peels a_m off by sequential
    #            division by (1 − u^(m+1)) and stops when the quotient
    #            is zero.
    #   Route B: the input p(u) itself. Σ a_m·(u;u)_m must reproduce it
    #            EXACTLY in ℤ[u]. Nothing in this probe had checked
    #            that, yet every cyclotomic count is taken on the
    #            reconstructed sum rather than on p(u).
    reconstruction_flags = (
        [v["reconstructs_input_polynomial"] for v in z_k_results.values()]
        + [z_diff_result["reconstructs_input_polynomial"]]
    )
    builder.add_data("habiro_reconstruction", {
        "checked": len(reconstruction_flags),
        "exact": sum(1 for f in reconstruction_flags if f),
    })
    builder.add_assertion(
        "habiro_expansion_reconstructs_input_polynomial",
        computed=sum(1 for f in reconstruction_flags if f),
        expected=len(reconstruction_flags),
        tolerance=0,
        source=(
            "Route A: Σ a_m·(u;u)_m rebuilt from the sequential "
            "Pochhammer division of `cyclotomic_expansion`, for "
            "z(q)^1, z(q)^2, z(q)^3 and z²−z. Route B: the "
            "denominator-cleared p(u) each expansion was given. "
            "Expanded difference must be identically 0 in ℤ[u]."
        ),
    )

    # (2) The Pochhammer counting law this module's own docstring
    #     states, tested instead of asserted in prose.
    #   Route A: `cyclotomic_factor_count` divides (u;u)_m by Φ_8(u)
    #            until there is a remainder.
    #   Route B: ⌊m/8⌋ — #{k ≤ m : 8 | k}, from 1−u^k = Π_{d|k} Φ_d.
    #            Integer divisor counting; no polynomial.
    poch_law_agree = sum(
        1 for row in poch_table
        if row["phi8_power"] == row["phi8_power_floor_m_over_8"]
    )
    builder.add_data("pochhammer_counting_law", {
        "rows": len(poch_table),
        "agreeing": poch_law_agree,
        "law": "Φ_8 multiplicity of (u;u)_m is #{k<=m : 8|k} = floor(m/8)",
    })
    builder.add_assertion(
        "pochhammer_phi8_multiplicity_matches_floor_m_over_8",
        computed=poch_law_agree,
        expected=len(poch_table),
        tolerance=0,
        source=(
            "Route A: repeated sp.div of (u;u)_m by cyclotomic_poly(8, "
            "u), m = 0..20. Route B: ⌊m/8⌋ from the divisor "
            "factorisation 1−u^k = Π_{d|k} Φ_d(u). The "
            "FROM-POCHHAMMER-BOUNDARY verdict is a statement about "
            "exactly this law."
        ),
    )

    # (3) Every Φ_8 multiplicity in the witness, by a second route.
    #   Route A: repeated long division by Φ_8 (`cyclotomic_factor_count`).
    #   Route B: `phi8_power_via_root_test` — reduce mod u⁴ = −1 by
    #            folding the coefficient list, and differentiate for the
    #            square. Never divides a polynomial.
    # This covers the three z(q)^k sums (the verdict's premise that they
    # carry NO Φ_8) and the three real Δa_m chains (the Φ_8² the probe
    # set out to explain).
    root_pairs = (
        [(v["phi8_power"], v["phi8_power_root_test"])
         for v in z_k_results.values()]
        + [(z_diff_result["phi8_power"], z_diff_result["phi8_power_root_test"])]
        + [(r["phi8_power"], r["phi8_power_root_test"]) for r in delta_results]
    )
    builder.add_data("phi8_two_routes", {
        "pairs_division_vs_root_fold": [list(p) for p in root_pairs],
        "agreeing": sum(1 for a, b in root_pairs if a == b),
    })
    builder.add_assertion(
        "phi8_multiplicity_agrees_with_residue_fold_route",
        computed=sum(1 for a, b in root_pairs if a == b),
        expected=len(root_pairs),
        tolerance=0,
        source=(
            "Route A: Φ_8-multiplicity by repeated sp.div. Route B: by "
            "reducing mod Φ_8 = u⁴+1 through a coefficient fold "
            "(u^i ↦ (−1)^(i//4)·u^(i mod 4)) and differentiating for "
            "higher multiplicity — Φ_8 is irreducible over ℚ and Φ_8' = "
            "4u³ is coprime to it, so Φ_8^k | S iff Φ_8 divides S and "
            "its first k−1 derivatives. Covers z(q)^1..3, z²−z and the "
            "three Δa_m chains."
        ),
    )

    # (4) The verdict's premise, stated as a number.
    #   FROM-POCHHAMMER-BOUNDARY is chosen only when z(q)^k alone
    #   carries no Φ_8. Route A: the measured multiplicities for
    #   k = 1, 2, 3. Route B: 0 — z(q)^k = u^(6k)/Φ_4(u)^k in u, so
    #   after `to_u_polynomial` clears the denominator the numerator is
    #   the monomial u^(6k), whose only cyclotomic factor is Φ_1-free.
    #   A monomial cannot be divisible by Φ_8.
    z_phi8_max = max(v["phi8_power"] for v in z_k_results.values())
    builder.add_assertion(
        "z_pow_k_habiro_sums_carry_no_phi8",
        computed=z_phi8_max,
        expected=0,
        tolerance=0,
        source=(
            "Route A: max Φ_8 multiplicity over the k = 1, 2, 3 Habiro "
            "sums, measured. Route B: 0, because z(q)^k in u is "
            "u^(6k)/Φ_4(u)^k and `to_u_polynomial` clears the "
            "denominator, leaving a monomial — which no cyclotomic "
            "polynomial of degree > 0 divides. If this is ever nonzero "
            "the verdict is not FROM-POCHHAMMER-BOUNDARY."
        ),
    )

    elapsed = time.time() - t0
    log(f"\nTotal elapsed: {elapsed:.1f} s")
    builder.add_data("elapsed_seconds", elapsed)

    builder.save()
    log(f"✓ Witness saved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
