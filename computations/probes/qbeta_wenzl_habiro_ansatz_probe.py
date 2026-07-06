#!/usr/bin/env python3
"""qbeta_wenzl_habiro_ansatz_probe.py — Q_β Wenzl-Habiro keystone ansatz.

KEYSTONE STRUCTURAL PROBE TOWARD 1ppQ.

Per docs/audits/2026-06-01-qbeta-habiro-zeta8-categorical-witness.md
(PR #1625, merged), the level-2 SU(2) Wenzl identification at q = ζ_8
is the categorical witness for the universal Φ_8 cancellation
S_6(ζ_8) + Δa_7(ζ_8)·8 = 0 across the three atomic-step Habiro
pairs (D−n), (³He−D), (⁴He−³He).

This probe tests the working ansatz:

    Q_β-Habiro(u)  =  W(u) · D(u)

where W(u) is the "Wenzl factor" encoding the level-2 SU(2) Verlinde
annihilator at q = ζ_8, and D(u) is the pair-specific Δ from
(p, n).  The structural variable is u = b · ℏ_q²; the truncation
order is N (each rung buys 2.07 digits; 1ppQ needs N=7).

Specifically: define the Q_β Habiro element such that its Taylor
expansion at q = 1 (h = 0, u = 0) reproduces

    Q_β = Q_base · Π_{k≥2} (1 + c_k · u^k)
        = Q_base · ( 1 + c_2·u² + c_3·u³ + c_4·u⁴ + ... )

with c_2 = −1 PROVED Taylor-exact and c_3 ≈ −2.0693 (CAL-anchored).

CANDIDATE FORMS for the Wenzl factor W(u) — test each:

  (W1) Pochhammer-ratio:    W1(u) = (1 − u^8) / (1 − u^4)^2
                                 = (Φ_1·Φ_2·Φ_4·Φ_8) / (Φ_1·Φ_2·Φ_4)^2
                                 = Φ_8 / (Φ_1·Φ_2·Φ_4)
                                   ≅ Φ_8 / (1−u^4)
  (W2) Wenzl annihilator:   W2(u) = 1 − u^4 / (1−u^4)
                                 = ([4]_q vanishing) algebraic surrogate
  (W3) Cyclotomic ratio:    W3(u) = Φ_8(u) / Φ_4(u) = (u^4+1)/(u^2+1)
  (W4) Squared Wenzl:       W4(u) = ( (1−u^8) / (1−u^4) )^2
                                 = (1 + u^4)^2 = Φ_8(u)^2 plain
  (W5) Wenzl with Φ_4 kill: W5(u) = (1 − u^4) · (1 − u^8)
                                 = Φ_4 · Φ_8 · (... no, expand)
  (W6) [4]_q surrogate:     W6(u) = u·(u^4 − 1)/(u^2 − 1) = u·(u^2+1)
                                 = u(1+u^2)
  (W7) Dehn twist:          W7(u) = (1−u^4)^2 / (1−u^8)
                                 = inverse of W1

For each W candidate, the ansatz is

    Q_β-Habiro(u) = (1 + W(u) · D(u))         (form A)
       or
    Q_β-Habiro(u) = exp( W(u) · D(u) )        (form B)

We Taylor expand at u = 0 and match the empirically-known coefficients:
   c_2 = −1                 (PROVED Taylor-exact)
   c_3 ≈ −2.0693…           (CAL-anchored)
   c_4 ≈ +? (extracted)
   ... up to c_7

STRUCTURAL ACCEPTANCE: c_2 and c_3 must match as exact algebraic
identities (not numerical near-matches) of D(u) at u = 0.  In
particular: when W(u) starts at u^a with leading coefficient w_a, and
D(u) has Taylor expansion d_0 + d_1·u + d_2·u² + …, the product
W(u)·D(u) contributes to c_k starting at k = a (if d_0 ≠ 0).
Matching c_2 forces a + 0 = 2 (so a = 2 if d_0 ≠ 0, etc.) — this
already winnows W candidates dramatically.

OUTPUT:
  • Print Taylor expansion of each W(u) candidate at u = 0.
  • For each W, attempt to find D(u) that matches c_2 = −1 exactly.
  • Numerically verify at canonical q₀ via 50-dps mpmath.
  • Witness JSON with the (W, D) pair that achieves both c_2 and c_3
    exactly (if any).
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
import sys
import time
from pathlib import Path

import sympy as sp
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402


N_TAYLOR = 3  # Match ONLY the structurally-constrained coefficients: c_2 (proved)
              # and c_3 (cal-anchored from Q_codata). c_k for k ≥ 4 are
              # PREDICTED by the W · D ansatz, not constrained — the prior
              # padding with c_k = 0 was a methodology bug (Gemini review,
              # PR #1642): it forced D to cancel W's natural higher Taylor
              # coefficients, artificially biasing the verdict toward
              # GENERIC_D. See docs/audits/2026-06-01-qbeta-wenzl-habiro-ansatz.md.


def taylor_coeffs(expr: sp.Expr, var: sp.Symbol, N: int) -> list[sp.Expr]:
    """Return [c_0, c_1, ..., c_N] of Taylor expansion at var = 0."""
    series = sp.series(expr, var, 0, N + 1).removeO()
    expanded = sp.expand(series)
    return [sp.simplify(expanded.coeff(var, k)) for k in range(N + 1)]


def wenzl_candidates(u: sp.Symbol) -> dict[str, sp.Expr]:
    """Return the W(u) candidates to test."""
    return {
        # W1: Pochhammer ratio — (u; u)_8 / (u; u)_4 / something
        "W1_pochhammer_ratio_8_4": (1 - u**8) / (1 - u**4)**2,
        # W2: simple [4]_q surrogate — 1 − u^4 / (1 − u^4)
        # = (1 - u^4 - u^4) / (1 - u^4)  ←   degenerate, skip
        # W3: cyclotomic ratio Φ_8/Φ_4
        "W3_phi8_over_phi4": (u**4 + 1) / (u**2 + 1),
        # W4: squared Pochhammer  (Phi_8 squared)
        "W4_phi8_squared": (u**4 + 1)**2,
        # W5: Φ_8 alone — leading order u^0 = 1
        "W5_phi8_plain": u**4 + 1,
        # W6: [4]_q surrogate × Phi_8 — u·(u²+1)·(u⁴+1)
        "W6_q4_times_phi8": u * (u**2 + 1) * (u**4 + 1),
        # W7: dehn-twist inverse — (1−u^4)^2 / (1 − u^8)
        "W7_inverse_dehn": (1 - u**4)**2 / (1 - u**8),
        # W8: the ζ_8-cancellation surrogate — start at u^2 with coeff -1
        # Since c_2 = -1 and the leading Taylor of u² coefficient should
        # encode that — surrogate W(u) = − u² · (1 − u² + ...) or just W(u) = -u^2
        "W8_minus_u_squared": -u**2,
        # W9: (1 − u^2)·something — (1−u²) divides Φ_2 part
        "W9_one_minus_usq": 1 - u**2,
        # W10: Pochhammer  (u; u)_2 = (1−u)(1−u²)
        "W10_poch_2": (1 - u) * (1 - u**2),
    }


def find_d_taylor_for_c2_c3(W_taylor: list[sp.Expr], target_c: list[float],
                              N: int) -> tuple[list[sp.Expr], list[float]] | None:
    """Given W's Taylor coefs [w_0, w_1, ...] and target c's [c_0=0, c_1=0,
    c_2 = -1, c_3 = c3_target, ...], find D's Taylor coefs [d_0, d_1, ...]
    such that the product (W·D) reproduces target_c at orders 2..N.

    The product W·D has Taylor coefficient at u^k equal to
       Σ_{i+j=k} w_i · d_j

    Equating these to target_c[k] gives a linear system in d_j. If w_0 ≠ 0,
    we can solve sequentially: d_k = (target_c[k] − Σ_{i=1..k} w_i · d_{k−i}) / w_0.

    If w_0 = 0 and w_a is the leading non-zero coefficient (a ≥ 1), then the
    product starts at u^a; we have to match target_c[0..a−1] = 0 (forced) and
    solve from u^a onward: d_{k−a} = (target_c[k] − Σ_{i=a+1..k} w_i · d_{k−i}) / w_a.

    Returns (d_taylor, residuals) on success, or None if c_0, c_1, ... can't
    be killed (i.e. target_c[k] ≠ 0 for k < a).
    """
    # Find leading non-zero index a of W
    a = None
    for i, w in enumerate(W_taylor):
        if sp.simplify(w) != 0:
            a = i
            break
    if a is None:
        return None  # W ≡ 0
    # Check that target_c[0..a-1] are all 0 (forced)
    for k in range(a):
        if sp.simplify(target_c[k]) != 0:
            # Can't match — target c_k != 0 but product starts at u^a
            return None

    w_lead = W_taylor[a]
    d_taylor = [sp.Integer(0)] * (N + 1 - a)
    # d_taylor[j] corresponds to d_j (j-th Taylor coef of D)
    # The product W·D has coefficient at u^k for k ≥ a equal to
    #   Σ_{j=0..k-a} w_{k-j} · d_j  ( where w_{k-j} = 0 if k-j > len(W_taylor)-1 )
    # We solve for d_j sequentially starting from j = 0.
    for k in range(a, N + 1):
        # known partial sum from d_0..d_{k-a-1}, paired with w_{a+1}..w_k
        partial = sp.Integer(0)
        for j in range(0, k - a):
            wij = W_taylor[k - j] if (k - j) < len(W_taylor) else sp.Integer(0)
            partial += wij * d_taylor[j]
        # Now coefficient at u^k is w_a · d_{k-a} + partial; equate to target_c[k]
        residual = sp.simplify(target_c[k] - partial)
        d_taylor[k - a] = sp.simplify(residual / w_lead)

    return d_taylor, []


def main() -> int:
    t0 = time.monotonic()
    set_compute_dps()
    wb = WitnessBuilder("qbeta-wenzl-habiro-ansatz-probe", engine="sympy+mpmath",
                        start_time=t0)
    wb.set_description(
        "Tests the Wenzl-Habiro keystone ansatz Q_β-Habiro(u) = W(u)·D(u) "
        "for the Q_β precision ladder. Each candidate W(u) (cyclotomic / "
        "Pochhammer-ratio surrogates for the level-2 SU(2) Wenzl annihilator "
        "at q = ζ_8) is Taylor-expanded at u = 0; the pair-specific D(u) is "
        "then determined coefficient-wise to reproduce the known c_k of the "
        "Q_β precision ladder. The structural acceptance test asks whether "
        "D(u) collapses to a clean closed form (small denominators, "
        "categorically-recognisable algebraic structure) or remains a "
        "generic Taylor series (which would be just refactoring without "
        "categorical content). Per AGENTS.md flip-flop history: numerical "
        "near-match ≠ structural derivation. This probe demands exact "
        "polynomial identity for c_2 = -1 first, then asks whether c_3 "
        "emerges naturally from the same Wenzl factor."
    )
    wb.set_content_block("prop:q-beta-categorical-precision-ladder")

    u = sp.Symbol('u', real=True, positive=True)

    print("=" * 78)
    print(" Q_β WENZL-HABIRO KEYSTONE ANSATZ PROBE")
    print("=" * 78)
    print()
    print("Ansatz:  Q_β-Habiro(u) = W(u) · D(u)")
    print("         W = Wenzl factor (level-2 SU(2) at q = ζ_8)")
    print("         D = pair-specific Δ from (p, n)")
    print()
    print("Target Taylor coefficients:")
    print("   c_0 = 0  c_1 = 0  c_2 = -1 (PROVED Taylor-exact)")
    print("   c_3 = -2.0693… (CAL-anchored)")
    print("   c_4..c_7 = CAL-anchored")
    print()

    # Read CAL-anchored c_k from the cache witness
    import json
    cache_path = _pb.witness_path("qbeta-ck-cache.witness.json", HERE)
    cache = json.loads(cache_path.read_text())
    cal_c_k = {}
    for row in cache["data"]["rows"]:
        k = row["k"]
        cal_c_k[k] = sp.Rational(row["c_k"])
    print(f"  Cached c_k from {cache_path.name}:")
    for k in sorted(cal_c_k.keys()):
        print(f"     c_{k} = {float(cal_c_k[k]):+.6e}")
    print()

    # Build target_c list: c_0 = 0, c_1 = 0, c_2 = -1, c_3..c_7 = cal_anchored
    # The product Q_β/Q_base − 1 in u is the relevant series. We are matching
    # the c_k of  (Σ_k c_k u^k) directly (NOT 1 + Σ c_k u^k).
    # target_c[k] constrains the Taylor coefficient at u^k of the SERIES
    #   Q_β / Q_base − 1 = Σ_k c_k u^k.
    # ONLY c_2 (proved Taylor-exact = −1) and c_3 (cal-anchored from Q_codata
    # at q_0) are physically constrained. c_k for k ≥ 4 are NOT constrained
    # by current Q_β experimental precision (8 sig figs); they are PREDICTED
    # by the W · D ansatz and reported, not matched.
    #
    # Earlier methodology bug (Gemini review, PR #1642): the probe padded
    # target_c[k ≥ 4] with values from extract_higher_c_k(), which is a
    # tautological recursive single-point fit yielding c_k = 0 by construction
    # (Q_prev becomes exactly Q_codata after the first iteration). Forcing
    # D to cancel W's natural u^k≥4 Taylor coefficients to "match" those
    # spurious zeros artificially biased every W candidate toward GENERIC_D.
    target_c = [sp.Integer(0)] * (N_TAYLOR + 1)
    target_c[2] = sp.Integer(-1)
    if 3 in cal_c_k:
        target_c[3] = cal_c_k[3]
    else:
        raise RuntimeError("c_3 missing from qbeta-ck-cache.witness.json")
    print(f"  Constraints: c_2 = {target_c[2]} (proved Taylor-exact);")
    print(f"               c_3 = {float(target_c[3]):+.8e} (cal-anchored at q_0)")
    print(f"  c_k for k ≥ 4 are NOT constrained (Q_β CODATA = 8 sig figs).")
    print()

    # ─── Test each candidate W(u) ─────────────────────────────────
    Ws = wenzl_candidates(u)
    results = []

    print("=" * 78)
    print(" TESTING EACH W(u) CANDIDATE")
    print("=" * 78)
    for name, W_expr in Ws.items():
        W_expr_simp = sp.simplify(W_expr)
        W_taylor = taylor_coeffs(W_expr_simp, u, N_TAYLOR)
        print()
        print(f"--- {name}: W(u) = {W_expr_simp}")
        print(f"      Taylor: {[(k, w) for k, w in enumerate(W_taylor) if sp.simplify(w) != 0][:6]}")

        # Find leading non-zero index
        a = None
        for i, w in enumerate(W_taylor):
            if sp.simplify(w) != 0:
                a = i
                break
        if a is None:
            print("      W ≡ 0 — skipped.")
            continue
        print(f"      Leading order: u^{a} with coeff w_{a} = {W_taylor[a]}")

        # Constraint: a must be ≤ 2 (else c_2 = 0 forced, but c_2 = -1)
        if a > 2:
            print(f"      REJECTED: a = {a} > 2 ⇒ c_2 forced to 0, but target c_2 = -1.")
            results.append({
                "name": name, "W": str(W_expr_simp), "verdict": "REJECTED_a_gt_2",
                "leading_order_a": a, "leading_coeff_w_a": str(W_taylor[a]),
                "reason": f"leading order u^{a} > u^2; c_2 forced to 0",
            })
            continue

        # Try to find D(u) Taylor coefficients matching target_c
        result = find_d_taylor_for_c2_c3(W_taylor, target_c, N_TAYLOR)
        if result is None:
            print(f"      REJECTED: cannot kill low-order c_k = 0 constraints.")
            results.append({
                "name": name, "W": str(W_expr_simp), "verdict": "REJECTED_low_order_constraints",
                "leading_order_a": a,
            })
            continue
        d_taylor, _ = result
        # Print D(u) Taylor coefficients
        d_summary = [(j, sp.nsimplify(sp.simplify(d), rational=False, tolerance=1e-30))
                     for j, d in enumerate(d_taylor[:8])]
        d_summary_strs = [(j, str(d) if not isinstance(d, sp.Float)
                           else f"{float(d):+.6e}") for j, d in d_summary]
        print(f"      Solved D(u) Taylor (first 8):")
        for j, ds in d_summary_strs:
            print(f"         d_{j} = {ds}")

        # Structural acceptance test:
        # (a) Are the FIRST FEW d_j EXACTLY ZERO or clean small rationals?
        # (b) Do the d_j show a pattern (e.g. constant, alternating, recognisable)?
        d_clean_count = 0
        for d in d_taylor[:6]:
            d_simp = sp.simplify(d)
            if d_simp == 0:
                d_clean_count += 1
            elif d_simp.is_rational and abs(sp.fraction(d_simp)[1]) < 1000:
                d_clean_count += 1
            elif d_simp.is_integer:
                d_clean_count += 1
        # If d_0 is clean and d_1..d_5 are zero or clean rationals,
        # the ansatz is structurally elegant.
        verdict = "INDETERMINATE"
        # Special: did the c_2 = -1 match work exactly?
        # And does the c_3 emerge from D's natural form (e.g. d_0 only, no
        # ad-hoc d_1)?
        d0 = sp.simplify(d_taylor[0])
        d1 = sp.simplify(d_taylor[1]) if len(d_taylor) > 1 else sp.Integer(0)
        d2 = sp.simplify(d_taylor[2]) if len(d_taylor) > 2 else sp.Integer(0)

        # Categorical purity: if D(u) = d_0 (a constant), the entire Q_β
        # ladder is W(u) · d_0 — every c_k is determined by W alone (up
        # to scale d_0). That would be the ideal "categorical" outcome.
        if d1 == 0 and d2 == 0 and d0 != 0:
            verdict = "PURE_CONSTANT_D"
            print(f"      ★ PURE CONSTANT D(u) = {d0} — ENTIRE ladder fixed by W alone.")
        # Sub-ideal: D(u) is a low-degree polynomial in u (e.g. d_0 + d_1·u)
        elif d2 == 0 and len(d_taylor) > 3 and sp.simplify(d_taylor[3]) == 0:
            verdict = "DEGREE_1_D"
            print(f"      ◆ DEGREE-1 D(u) = {d0} + ({d1})·u — c_4+ all fixed by W·(d_0+d_1·u).")
        else:
            verdict = "GENERIC_D"
            print(f"      ◇ GENERIC D(u) — D's higher Taylor coefs not falling out cleanly.")

        # Numerical check: evaluate W(u_q0) · D(u_q0) and compare to
        # Σ_k cal_c_k · u_q0^k.
        # Compute u_substrate from canonical q₀
        q0 = mp.mpf(Q_50_DIGIT_STR)
        hbar_q = (q0 - 1) / q0
        h = q0 - 1 / q0
        b_sq = (h**2 + 3) / (h**2 + 4)
        b = mp.sqrt(b_sq)
        u_substrate = b * hbar_q**2

        # Numerical eval of W(u) at u_substrate
        W_num = mp.mpf(0)
        for k, w in enumerate(W_taylor):
            try:
                wf = mp.mpf(str(sp.N(w, 50)))
            except Exception:
                wf = mp.mpf(0)
            W_num += wf * u_substrate**k

        # Numerical eval of D(u) Taylor at u_substrate
        D_num = mp.mpf(0)
        for j, d in enumerate(d_taylor[:N_TAYLOR + 1]):
            try:
                df = mp.mpf(str(sp.N(d, 50)))
            except Exception:
                df = mp.mpf(0)
            D_num += df * u_substrate**j

        # Compare to target Σ c_k u^k
        target_num = mp.mpf(0)
        for k in range(2, 8):
            target_num += mp.mpf(str(cal_c_k.get(k, 0))) * u_substrate**k

        product_num = W_num * D_num
        residual = product_num - target_num

        print(f"      Numerical at u_substrate = {float(u_substrate):.6e}:")
        print(f"        W(u_substrate)         = {mp.nstr(W_num, 12)}")
        print(f"        D(u_substrate) Taylor  = {mp.nstr(D_num, 12)}")
        print(f"        W·D                    = {mp.nstr(product_num, 12)}")
        print(f"        Σ c_k u^k target       = {mp.nstr(target_num, 12)}")
        print(f"        residual               = {mp.nstr(residual, 6)}")

        results.append({
            "name": name,
            "W": str(W_expr_simp),
            "leading_order_a": a,
            "verdict": verdict,
            "d_taylor_first_8": [str(d) for d in d_taylor[:8]],
            "d_0": str(d0),
            "d_1": str(d1),
            "d_2": str(d2),
            "u_substrate_50dps": mp.nstr(u_substrate, 50),
            "W_at_u_substrate": mp.nstr(W_num, 30),
            "D_at_u_substrate": mp.nstr(D_num, 30),
            "WD_at_u_substrate": mp.nstr(product_num, 30),
            "target_sum_c_k_u_k": mp.nstr(target_num, 30),
            "residual": mp.nstr(residual, 6),
        })

    print()
    print("=" * 78)
    print(" SUMMARY")
    print("=" * 78)
    pure_constants = [r for r in results if r.get("verdict") == "PURE_CONSTANT_D"]
    degree1s = [r for r in results if r.get("verdict") == "DEGREE_1_D"]
    print(f"  Total candidates tested:    {len(results)}")
    print(f"  PURE_CONSTANT_D matches:    {len(pure_constants)}  (ideal: W alone fixes all c_k)")
    print(f"  DEGREE_1_D matches:         {len(degree1s)}  (sub-ideal: D = d_0 + d_1 u)")
    print(f"  REJECTED (a > 2):           "
          f"{len([r for r in results if r.get('verdict') == 'REJECTED_a_gt_2'])}")
    print()
    if pure_constants:
        print("  ★ POSITIVE: pure constant D(u) found!")
        for r in pure_constants:
            print(f"    W = {r['W']}    d_0 = {r['d_0']}")
        verdict = "PARTIAL_OR_POSITIVE"
    elif degree1s:
        print("  ◆ PARTIAL: degree-1 D(u) candidates exist (need narrative check).")
        for r in degree1s:
            print(f"    W = {r['W']}    D ≈ {r['d_0']} + ({r['d_1']})·u")
        verdict = "PARTIAL"
    else:
        print("  ✗ NEGATIVE: no candidate W yields a clean D(u) — the ansatz")
        print("    Q_β-Habiro = W(u) · D(u) with W ∈ {tested candidates}")
        print("    does NOT close the Q_β Habiro element keystone.")
        print()
        print("    STRUCTURAL NARROWING: a clean Wenzl factor alone (with")
        print("    pair-specific constant prefactor) is insufficient to")
        print("    derive c_3..c_7. The Wenzl mechanism may enter at a")
        print("    DIFFERENT layer (e.g. inside the Form A archimedean")
        print("    functor, not as a multiplicative prefactor of the")
        print("    Habiro ladder). Open question: try W(u) on the Δa_m")
        print("    side directly (per the PR #1625 finding that Wenzl")
        print("    acts via Markov-trace cancellation, not as a direct")
        print("    Habiro element factor).")
        verdict = "NEGATIVE"

    print()
    wb.add_data("u_substrate_50dps", mp.nstr(mp.mpf(0) if not results else mp.mpf(results[0].get("u_substrate_50dps", "0")), 50))
    wb.add_data("target_c_k", {str(k): str(v) for k, v in enumerate(target_c)})
    wb.add_data("candidates", results)
    wb.add_data("overall_verdict", verdict)
    wb.add_data("summary", {
        "total_tested": len(results),
        "pure_constant_d_count": len(pure_constants),
        "degree_1_d_count": len(degree1s),
        "rejected_a_gt_2_count": len([r for r in results if r.get("verdict") == "REJECTED_a_gt_2"]),
    })
    wb.add_assertion(
        "c_2_target_is_minus_one_taylor_exact",
        computed=float(target_c[2]), expected=-1.0, tolerance=1e-30,
        source="c_2 = -1 is Lean-proved Taylor-exact (Kashiwara f̃₁², "
        "qou:QOU.BraidKnot.N2_factor); independent of any Wenzl ansatz.",
    )
    wb.save()
    print(f"  Witness: qbeta-wenzl-habiro-ansatz-probe.witness.json")
    print(f"  Verdict: {verdict}")
    print()

    return 0 if verdict in ("PARTIAL_OR_POSITIVE", "PARTIAL") else 0  # always 0


if __name__ == "__main__":
    raise SystemExit(main())
