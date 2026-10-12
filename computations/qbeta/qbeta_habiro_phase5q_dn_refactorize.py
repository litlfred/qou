#!/usr/bin/env python3
"""
qbeta_habiro_phase5q_dn_refactorize.py — Phase 5q canonical (D - n)
Habiro test for the Φ_8² strand-doubling factor.

DECISIVE STRUCTURAL TEST
========================

Background: PR #1579 (merged 57b5fa2d3a) found the (D - n) Habiro
factorization in the **Habiro-witness convention** (the deuteron is
computed via `markov_trace_symbolic(Z=1, N=1, include_inter=True)`,
giving tr_M(D, q_0) ≈ 0.3883) carries an explicit Φ_8² = (u^4 + 1)²
factor:

  Σ_m Δa_m(D - n) · (u; u)_m
    = -u · (u^4 + 1)² · P16a(u) · P16b(u) · P45(u)
    [habiro-witness convention, include_inter=True]

This was a key piece of evidence for a "strand-doubling" categorical
interpretation (4 strands × 2 nucleons → 8-fold cyclotomic).

CONVENTION ISSUE
----------------

The **Phase 5q canonical** closed form
([`closed_form_tau_M.py`](closed_form_tau_M.py)) computes the
deuteron as

  tr_M(𝓑_D, q) = tr_M^3(𝓑_p, q) · tr_M^3(𝓑_n, q) · z(q),
  z(q) = 1 / (q^{1/2} + q^{-1/2})

via the Phase 5l constit identity + Phase 5c.1 interface identity.
At q_0 this gives tr_M(D) ≈ 0.7281, twice the witness-convention
value. The two conventions differ structurally:

  - **Witness convention**: full 12-crossing deuteron braid through
    y_λ · χ_λ with all nucleon-nucleon interface crossings included.
  - **Phase 5q canonical**: the constit identity + Markov axiom; the
    deuteron is "two H_3 building blocks × the Markov bridge factor".

For the Φ_8² strand-doubling chain (Φ_4 → Φ_8 → Φ_16 → Φ_32) to be
**structural** rather than **convention-specific**, the factor must
appear in BOTH conventions. THIS PROBE TESTS THE CANONICAL SIDE.

🛑 THREE THINGS A READER OF THIS FILE NEEDS, AND NONE WAS STATED
=================================================================
Added 2026-10-10, bean `qou-bvk7`. Nothing below changes a number; all
three are labels on what is already here.

1. **"Convention" above means WHICH BRAID/IDENTITY, not C-vs-D, and the
   two axes are independent.** "Witness convention" vs "Phase 5q
   canonical" is the structural distinction documented above. Orthogonal
   to it is the **Markov parameter**, and on that axis the Phase 5q side
   below is **convention C**: `z(q) = 1 / (q^{1/2} + q^{-1/2})`, which is
   `√q/(q+1) = z_C = 0.4993203342` at `q₀` exactly. Owner ruling R1
   (2026-08-15) makes `z_D = q³/(q²+1) = 0.6126880371` canonical, so the
   word "canonical" in "Phase 5q canonical" is about the identity route
   and does **not** mean convention-canonical. That spelling is also one
   of the detector-blind C forms AGENTS.md lists, which is why
   `convention-c-producer-audit.py` does not flag this file.

2. **The `D` in `tr_M_D_q0_witness` is DEUTERON, not convention D.** Same
   for "(D − n)" and `Δa_m(D − n)` throughout. The witness field
   `data.numerical_q0_cross_check.tr_M_D_q0_witness = 0.3882864240747888`
   is the deuteron trace in the *witness* convention — and it is a
   **convention-C** value (under D the same quantity is ≈ 0.5751;
   `deuteron-real-sdp.witness.json` now records `0.5751722457697739`). A
   reader scanning field names for convention-D artifacts will read this
   one backwards.

3. **The committed witness CANNOT be refreshed, so its `allPassed: true`
   is unfalsifiable.** This probe refuses to run: `_qou_lnog_preflight`
   raises `AmDifferenceInvalid` from `require_am_differenceable` because
   the two witnesses' denominators differ, so `a_m` subtraction would
   build `d_X·t_X − d_Y·t_Y` rather than the pair difference (beans
   `qou-0ndb` / `qou-lnog`; the message names `trace_diff_numerator` as
   the correct route). That refusal is **correct** and is not a crash —
   but it means the C-frame value above is frozen and the recorded
   `allPassed` cannot be re-derived until `qou-lnog` lands. This is the
   `qou-2cof` lesson in its stronger form: a producer that cannot run
   cannot report drift, and here the producer is *right* not to run.

APPROACH
========

1. Parse tr_M(p, q) and tr_M(n, q) symbolically from
   `habiro-coefficients-atomic.witness.json` (these are convention-
   agnostic — single-nucleon traces).

2. Construct the **Phase 5q canonical D**:
       tr_M(D, q)_Phase5q := tr_M(p, q) · tr_M(n, q) · z(q)
   with z(q) = 1 / (sqrt(q) + 1/sqrt(q)).

3. Convert to a polynomial in u (q = u²), clearing denominators.

4. Apply the sequential cyclotomic-division algorithm from
   `habiro_coefficients_atomic.cyclotomic_expansion` to extract
   a_m(D)_Phase5q for m = 0, 1, 2, ...

5. Compute Δa_m(D - n) using a_m(n) from the same witness.

6. Form Σ_m Δa_m · (u; u)_m and **sympy.factor**.

7. Check whether (u^4 + 1)² = Φ_8² appears in the factorization.

VERDICT GATES
=============

- Φ_8² appears in BOTH conventions → strand-doubling is STRUCTURAL.
  The Φ_4 → Φ_8 → Φ_16 → Φ_32 chain unlocks; falsifiable predictions
  test ON.
- Φ_8² does NOT appear in canonical → strand-doubling is
  CONVENTION-SPECIFIC. The Φ_8 audit needs revision; Q_β's
  canonical input must be re-examined.

USAGE
-----
  python3 -u qbeta_habiro_phase5q_dn_refactorize.py 2>&1 | tee /tmp/phase5q_dn.log
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
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402

# 50-dps numerical specialization for q_0 cross-check
mp.mp.dps = 65


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def parse_tr_M_in_q(tr_M_str: str, q: sp.Symbol) -> sp.Expr:
    """Parse the 'tr_M_in_q' string from the witness as a sympy expr."""
    s = tr_M_str.replace("^", "**")
    return sp.sympify(s, locals={"q": q})


def expr_to_u_polynomial(expr_in_q: sp.Expr,
                         q: sp.Symbol,
                         u: sp.Symbol) -> tuple[sp.Expr, int, sp.Expr]:
    """Substitute q -> u² and clear u-denominators.

    Returns (p_in_u, shift, denom) such that
      p_in_u(u) = u^shift · denom(u) · expr_in_q(u²)

    is a polynomial in u with non-negative powers.
    """
    expr_u = sp.together(expr_in_q.subs(q, u ** 2))
    num, den = sp.fraction(expr_u)
    num = sp.expand(num)
    den = sp.expand(den)
    p_expanded = sp.expand(num)
    poly = sp.Poly(p_expanded, u)
    monoms = poly.monoms()
    if not monoms:
        return sp.Integer(0), 0, sp.expand(den)
    min_pow = min(int(m[0]) for m in monoms)
    shift = -min_pow if min_pow < 0 else 0
    p_shifted = sp.expand(p_expanded * u ** shift)
    return p_shifted, shift, sp.expand(den)


def cyclotomic_expansion(p_in_u: sp.Expr,
                         u: sp.Symbol,
                         max_m: int = 30) -> list[dict]:
    """Habiro / cyclotomic expansion p(u) = Σ_m a_m(u) · (u; u)_m
    via sequential polynomial division.
    """
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


def q_pochhammer(u: sp.Symbol, m: int) -> sp.Expr:
    """(u; u)_m = Π_{k=1..m} (1 - u^k)."""
    if m == 0:
        return sp.Integer(1)
    return sp.prod(1 - u ** k for k in range(1, m + 1))



# ── qou-lnog preflight ─────────────────────────────────────────────────────
# This script forms its pair difference by SUBTRACTING the two witnesses' a_m.
# That is valid only when their denominators agree, because a witness's a_m
# expand its own denominator-cleared numerator p = d*t (proved sorry-free in
# QOU/Habiro/MirrorPairNormalisation.lean). Whether it holds is a property of
# the CONVENTION, not of this file:
#
#     convention C   d_p = d_n = 4u^19(u^2+1)           IDENTICAL -> valid
#     convention D   d_p = 4u^18(u^4+1)^2, d_n = 4u^18   DIFFER   -> invalid
#
# So this script was CORRECT when its committed witness was produced (C) and is
# wrong under D with no edit in between. The preflight raises rather than let it
# emit a plausible polynomial that is not the pair's; porting to D means
# expanding trace_diff_numerator(tr_x, tr_y, sym) instead of differencing two
# expansions, which is a restructure this file has not had.
def _qou_lnog_preflight(tr_x, tr_y, label):
    from habiro_coefficients_atomic import require_am_differenceable
    require_am_differenceable(tr_x, tr_y, label=label)


def main() -> int:
    t0 = time.time()
    q = sp.Symbol("q", positive=True, real=True)
    u = sp.Symbol("u", positive=True, real=True)

    log("=" * 78)
    log("Phase 5q canonical (D - n) Habiro test — Φ_8² survival check")
    log("=" * 78)

    builder = WitnessBuilder(
        "qbeta-habiro-phase5q-dn-refactorize",
        engine="python+sympy",
    )
    builder.set_description(
        "Phase 5q canonical convention (D - n) Habiro factorization "
        "test. Constructs tr_M(D, q) = tr_M(p, q) · tr_M(n, q) · z(q) "
        "symbolically (via the Phase 5l constit + Phase 5c.1 Markov "
        "interface identities), extracts Habiro coefficients, and "
        "checks whether the Φ_8² = (u^4+1)² factor from the "
        "habiro-witness-convention (D - n) factorization (merged "
        "PR #1579) survives in the canonical convention."
    )
    builder.set_content_block("prop:neutron-qvalue-symbolic")

    # ─────────────────────────────────────────────────────────────────
    # Step 1: Parse tr_M(p) and tr_M(n) from the existing witness.
    # ─────────────────────────────────────────────────────────────────
    log("Step 1: Load tr_M(p, q) and tr_M(n, q) from witness")
    w_path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    w = builder.add_upstream(w_path)

    p_tr_str = w["results"]["p (proton, A=1)"]["tr_M_in_q"]
    n_tr_str = w["results"]["n (neutron, A=1)"]["tr_M_in_q"]
    # D - n, not n - p: the deuteron denominator differs from the nucleon one
    # under BOTH conventions, so this pair was never a_m-differenceable.
    _qou_lnog_preflight(w["results"]["D (deuteron, A=2)"]["tr_M_in_q"],
                        n_tr_str, "D - n")
    d_tr_str_witness = w["results"]["D (deuteron, A=2)"]["tr_M_in_q"]

    p_tr = parse_tr_M_in_q(p_tr_str, q)
    n_tr = parse_tr_M_in_q(n_tr_str, q)
    d_tr_witness = parse_tr_M_in_q(d_tr_str_witness, q)

    log(f"  tr_M(p, q) parsed (free symbols: {p_tr.free_symbols})")
    log(f"  tr_M(n, q) parsed (free symbols: {n_tr.free_symbols})")

    # Numerical cross-check at q_0.
    #   Route A: the tr_M_in_q STRING parsed by sympy and evaluated at q_0.
    #   Route B: tr_M_at_q0, the number the upstream producer wrote into the
    #            same witness through its own numeric path.
    # These lines used to print hard-coded "(expected ~1.0653062)" and
    # "(~0.9232333)" that nothing compared against — and both are now stale
    # by ~8% and ~7% because the witness moved to convention D. Compared
    # live, and asserted below.
    from q_parameter import q_at
    p_at_q0 = float(p_tr.subs(q, sp.Float(q_at(mp.mp.dps), 30)).evalf(30))
    n_at_q0 = float(n_tr.subs(q, sp.Float(q_at(mp.mp.dps), 30)).evalf(30))
    p_at_q0_witness = float(w["results"]["p (proton, A=1)"]["tr_M_at_q0"])
    n_at_q0_witness = float(w["results"]["n (neutron, A=1)"]["tr_M_at_q0"])
    # The comparison itself in mpf, off the witness's full-precision STRINGS
    # and a 40-digit sympy evaluation — not off the float64 prints below.
    _q0_mp = q_at(mp.mp.dps)
    trm_parse_gaps = []
    for _key, _expr in (("p (proton, A=1)", p_tr), ("n (neutron, A=1)", n_tr)):
        _route_a = mp.mpf(str(sp.N(_expr.subs(q, sp.Float(_q0_mp, 40)), 40)))
        _route_b = mp.mpf(w["results"][_key]["tr_M_at_q0"])
        trm_parse_gaps.append(abs(_route_a - _route_b))
    log(f"  tr_M(p, q_0) = {p_at_q0:.10f}  (witness tr_M_at_q0: "
        f"{p_at_q0_witness:.10f}, |Δ| = {mp.nstr(trm_parse_gaps[0], 3)})")
    log(f"  tr_M(n, q_0) = {n_at_q0:.10f}  (witness tr_M_at_q0: "
        f"{n_at_q0_witness:.10f}, |Δ| = {mp.nstr(trm_parse_gaps[1], 3)})")

    # ─────────────────────────────────────────────────────────────────
    # Step 2: Construct Phase 5q canonical D symbolically.
    #         tr_M(D, q)_Phase5q := tr_M(p, q) · tr_M(n, q) · z(q)
    #         z(q) = 1 / (sqrt(q) + 1/sqrt(q))
    # ─────────────────────────────────────────────────────────────────
    log("Step 2: Construct Phase 5q canonical tr_M(D, q) = p · n · z(q)")
    z_q = q**3 / (q**2 + 1)
    d_tr_phase5q = sp.together(p_tr * n_tr * z_q)
    log(f"  tr_M(D, q)_Phase5q symbolic form constructed")

    # Numerical cross-check
    z_at_q0 = float(z_q.subs(q, sp.Float(q_at(mp.mp.dps), 30)).evalf(30))
    d_at_q0_phase5q = float(d_tr_phase5q.subs(q, sp.Float(q_at(mp.mp.dps), 30)).evalf(30))
    d_at_q0_witness = float(d_tr_witness.subs(q, sp.Float(q_at(mp.mp.dps), 30)).evalf(30))
    ratio = d_at_q0_phase5q / d_at_q0_witness if d_at_q0_witness else float("inf")
    log(f"  z(q_0) = {z_at_q0:.10f}")
    log(f"  tr_M(D, q_0)_Phase5q  = {d_at_q0_phase5q:.10f}")
    log(f"  tr_M(D, q_0)_witness  = {d_at_q0_witness:.10f}")
    log(f"  ratio Phase5q/witness = {ratio:.10f}  "
        f"(expected ~1.875 for the convention shift)")

    builder.add_data("numerical_q0_cross_check", {
        "tr_M_p_q0": p_at_q0,
        "tr_M_n_q0": n_at_q0,
        "z_q0": z_at_q0,
        "tr_M_D_q0_phase5q": d_at_q0_phase5q,
        "tr_M_D_q0_witness": d_at_q0_witness,
        "ratio_phase5q_over_witness": ratio,
    })

    # ─────────────────────────────────────────────────────────────────
    # Step 3: Convert Phase 5q D to a polynomial in u.
    # ─────────────────────────────────────────────────────────────────
    log("Step 3: Convert tr_M(D, q)_Phase5q to a polynomial in u")
    p_u_phase5q, shift_phase5q, denom_phase5q = expr_to_u_polynomial(
        d_tr_phase5q, q, u
    )
    deg_p_phase5q = (int(sp.Poly(p_u_phase5q, u).degree())
                     if p_u_phase5q != 0 else 0)
    log(f"  Phase 5q D: deg p(u) = {deg_p_phase5q}, shift = u^{shift_phase5q}")
    log(f"  denom (in u): {sp.factor(denom_phase5q)}")

    builder.add_data("phase5q_D_u_polynomial", {
        "shift": shift_phase5q,
        "denom_in_u_factored": str(sp.factor(denom_phase5q)),
        "deg_p_u": deg_p_phase5q,
    })

    # ─────────────────────────────────────────────────────────────────
    # Step 4: Habiro / cyclotomic expansion of Phase 5q D.
    # ─────────────────────────────────────────────────────────────────
    log("Step 4: Habiro expansion of tr_M(D, q)_Phase5q in u")
    d_coeffs_phase5q = cyclotomic_expansion(p_u_phase5q, u, max_m=30)
    log(f"  → {len(d_coeffs_phase5q)} Habiro coefficients")
    for entry in d_coeffs_phase5q[:6]:
        log(f"    a_{entry['m']}(D)_Phase5q  deg = {entry['deg_a_m']}")
    if len(d_coeffs_phase5q) > 6:
        log(f"    ... ({len(d_coeffs_phase5q) - 6} more)")

    builder.add_data("phase5q_D_habiro_coefficients", [
        {"m": e["m"], "a_m": e["a_m"], "deg_a_m": e["deg_a_m"]}
        for e in d_coeffs_phase5q
    ])

    # ─────────────────────────────────────────────────────────────────
    # Step 5: Load a_m(n) from witness, compute Δa_m(D - n).
    # ─────────────────────────────────────────────────────────────────
    log("Step 5: Compute Δa_m(D - n) using witness a_m(n)")

    n_coeffs_witness = w["results"]["n (neutron, A=1)"]["habiro_coefficients"]
    n_coeffs_by_m: dict[int, sp.Expr] = {}
    for e in n_coeffs_witness:
        m = e["m"]
        a_m = sp.sympify(e["a_m"].replace("^", "**"), locals={"check_q": u})
        n_coeffs_by_m[m] = a_m

    d_coeffs_by_m: dict[int, sp.Expr] = {
        e["m"]: e["a_m_expr"] for e in d_coeffs_phase5q
    }

    max_m = max(max(n_coeffs_by_m.keys(), default=0),
                max(d_coeffs_by_m.keys(), default=0))
    log(f"  max_m (D Phase5q vs n witness) = {max_m}")

    delta_polys = []
    per_m = []
    for m in range(max_m + 1):
        d_m = d_coeffs_by_m.get(m, sp.Integer(0))
        n_m = n_coeffs_by_m.get(m, sp.Integer(0))
        delta = sp.expand(d_m - n_m)
        delta_polys.append(delta)
        per_m.append({
            "m": m,
            "delta": str(delta),
            "factored": str(sp.factor(delta)) if delta != 0 else "0",
            "is_zero": delta == 0,
        })
        log(f"  Δa_{m} (deg) = "
            f"{int(sp.Poly(delta, u).degree()) if delta != 0 else 0}, "
            f"is_zero={delta == 0}")

    builder.add_data("delta_am_per_m", per_m)

    # ─────────────────────────────────────────────────────────────────
    # Step 6: Σ_m Δa_m · (u; u)_m and sympy.factor.
    # ─────────────────────────────────────────────────────────────────
    log("Step 6: Σ Δa_m · (u; u)_m, then sympy.factor")
    habiro_sum = sp.Integer(0)
    for m, delta in enumerate(delta_polys):
        if delta != 0:
            habiro_sum += sp.expand(delta * q_pochhammer(u, m))
    log(f"  habiro_sum constructed; expanding...")
    habiro_sum = sp.expand(habiro_sum)
    log(f"  deg(habiro_sum) = "
        f"{int(sp.Poly(habiro_sum, u).degree()) if habiro_sum != 0 else 0}")

    log(f"  Factoring (this may take a minute)...")
    factored = sp.factor(habiro_sum)
    factored_str = str(factored)
    log(f"  Full factorization:")
    # Print in chunks for readability
    for i in range(0, len(factored_str), 200):
        log(f"    {factored_str[i:i+200]}")

    builder.add_data("habiro_sum_factored_phase5q", factored_str)

    # ─────────────────────────────────────────────────────────────────
    # Step 7: Test for Φ_8² = (u^4 + 1)² factor.
    # ─────────────────────────────────────────────────────────────────
    log("Step 7: Test for Φ_8 = u^4 + 1 factor in factorization")
    Phi8 = u ** 4 + 1
    Phi8_sq = Phi8 ** 2

    # Sympy factorization gives a Mul of factors; check for u^4+1 among them.
    if isinstance(factored, sp.Mul):
        factors_list = list(factored.args)
    elif factored == 0:
        factors_list = []
    else:
        factors_list = [factored]

    # Tally Φ_8 occurrences (including via Pow)
    phi8_count = 0
    other_factors = []
    for f in factors_list:
        if isinstance(f, sp.Pow):
            base, exp = f.base, f.exp
            if sp.simplify(base - Phi8) == 0:
                phi8_count += int(exp)
                continue
            other_factors.append((str(base), int(exp) if exp.is_Integer else str(exp)))
        elif sp.simplify(f - Phi8) == 0:
            phi8_count += 1
        else:
            other_factors.append((str(f), 1))

    # Also test divisibility directly — and carry it all the way to a
    # multiplicity, so it is a second ROUTE to phi8_count rather than a
    # weaker restatement of the first two powers. Route A above is
    # sympy's factorisation algorithm; this is repeated long division.
    phi8_mult_by_division = 0
    if habiro_sum != 0:
        _rest = habiro_sum
        while True:
            _quot, _rem = sp.div(_rest, Phi8, u)
            if _rem != 0:
                break
            phi8_mult_by_division += 1
            _rest = sp.expand(_quot)
            if _rest == 0:
                break
    phi8_divides = phi8_mult_by_division >= 1
    phi8_sq_divides = phi8_mult_by_division >= 2

    log(f"  Φ_8 divides habiro_sum: {phi8_divides}")
    log(f"  Φ_8² divides habiro_sum: {phi8_sq_divides}")
    log(f"  Φ_8 power in factorization (from sp.factor):     {phi8_count}")
    log(f"  Φ_8 power by repeated long division (route B):   {phi8_mult_by_division}")

    builder.add_data("phi8_survival_test", {
        "Phi8": str(Phi8),
        "phi8_divides_habiro_sum": phi8_divides,
        "phi8_sq_divides_habiro_sum": phi8_sq_divides,
        "phi8_power_in_factorization": phi8_count,
        "phi8_power_by_repeated_division": phi8_mult_by_division,
        "other_factors": [{"factor": fstr, "exponent": exp}
                          for fstr, exp in other_factors],
    })

    # ─────────────────────────────────────────────────────────────────
    # Verdict.
    # ─────────────────────────────────────────────────────────────────
    if phi8_count >= 2:
        verdict = (
            "PHI_8_SQUARED_SURVIVES: (u^4+1)^2 factor present in the "
            "Phase 5q canonical (D - n) Habiro factorization. "
            "Strand-doubling chain Φ_4 → Φ_8 → Φ_16 → Φ_32 is STRUCTURAL "
            "(convention-invariant); unlocks Φ_16/Φ_32 test."
        )
    elif phi8_count == 1:
        verdict = (
            "PHI_8_LINEAR_ONLY: (u^4+1) appears once but NOT squared "
            "in Phase 5q canonical convention. Strand-doubling "
            "interpretation needs revision — the squared form is "
            "specific to the habiro-witness convention "
            "(include_inter=True)."
        )
    else:
        verdict = (
            "PHI_8_ABSENT_IN_CANONICAL: (u^4+1) is NOT a factor of "
            "the Phase 5q canonical (D - n) Habiro sum. "
            "Strand-doubling chain is CONVENTION-SPECIFIC to the "
            "habiro-witness convention. The Φ_8 audit (PR #1579) "
            "needs a categorical revision; Q_β framework's canonical "
            "input must be re-examined."
        )

    log("")
    log("=" * 78)
    log(f"VERDICT: {verdict}")
    log("=" * 78)

    builder.add_data("verdict", verdict)
    builder.add_data("verdict_short",
                     "phi8_squared_survives" if phi8_count >= 2
                     else ("phi8_linear_only" if phi8_count == 1
                           else "phi8_absent_in_canonical"))

    # ── Was `phase5q_dn_refactorize_completed`, computed=1 / expected=1 ──
    # It named sympy.factor and asserted nothing about what came back. The
    # verdict gate here is a single integer, phi8_count, and it was read off
    # ONE algorithm with nothing to check it.

    # (1) The Φ_8 multiplicity, two routes.
    #     Route A: sympy's factorisation of the Habiro sum, tallying the
    #              exponent of (u⁴+1) across the returned Mul/Pow args.
    #     Route B: repeated sp.div by Φ_8, counting zero remainders until one
    #              is non-zero. Long division, never a factorisation.
    #     The verdict ("STRUCTURAL" vs "CONVENTION-SPECIFIC") turns entirely
    #     on this integer, so an sp.factor that returned an unexpected shape —
    #     the `isinstance(f, sp.Pow)` walk above silently mis-tallies anything
    #     it does not recognise — now separates the routes instead of setting
    #     the verdict on its own.
    builder.add_assertion(
        "phi8_multiplicity_two_routes_agree",
        computed=str(phi8_mult_by_division),
        expected=str(phi8_count),
        tolerance=0,
        unit="power of Φ_8 = u⁴+1 dividing Σ_m Δa_m·(u;u)_m",
        source=("Route A: exponent of (u⁴+1) tallied from sp.factor's output. "
                "Route B: repeated sp.div by Φ_8 counting zero remainders. "
                "The verdict gate reads Route A alone; this is what makes a "
                "mis-tally visible."),
    )

    # (2) The symbolic parse. Route A: the tr_M_in_q string sympified and
    #     evaluated at q_0. Route B: tr_M_at_q0, written into the same
    #     upstream witness by its producer's own numeric path. Everything
    #     downstream is built on Route A's parse of a STRING; nothing checked
    #     that the parse reproduced the number the string came from, which is
    #     exactly how the two stale "(expected ~1.0653…)" literals above
    #     survived a whole convention change.
    builder.add_data("tr_M_parse_cross_check", {
        "p_witness_tr_M_at_q0": w["results"]["p (proton, A=1)"]["tr_M_at_q0"],
        "n_witness_tr_M_at_q0": w["results"]["n (neutron, A=1)"]["tr_M_at_q0"],
        "p_abs_gap": mp.nstr(trm_parse_gaps[0], 6),
        "n_abs_gap": mp.nstr(trm_parse_gaps[1], 6),
    })
    builder.add_assertion(
        "tr_M_symbolic_parse_matches_witness_numeric",
        computed=mp.nstr(max(trm_parse_gaps), 12),
        expected="0",
        tolerance="1e-9",
        unit="max |tr_M(x, q_0) parsed − tr_M_at_q0 recorded| over x ∈ {p, n}",
        source=("Route A: sympify(tr_M_in_q).subs(q, q_0). Route B: the "
                "tr_M_at_q0 field the upstream producer recorded alongside it. "
                "Guards the string parse every later step depends on."),
    )
    builder.add_caveat(
        "Blocked, not run: the qou-lnog preflight raises AmDifferenceInvalid on "
        "the D−n leg before Step 1 finishes, because the deuteron and nucleon "
        "denominators differ under BOTH conventions — this pair was never "
        "a_m-differenceable. The two assertions above were exercised in situ "
        "with the preflight neutralised and both pass; the committed witness "
        "still carries the old `phase5q_dn_refactorize_completed` and cannot be "
        "regenerated until this file is ported to trace_diff_numerator."
    )
    builder.add_caveat(
        "Four hard-coded expectations in the log lines and docstring are stale, "
        "none of them ever compared to anything: 'tr_M(p, q_0) expected "
        "~1.0653062' and '~0.9232333' against the witness's own 1.1457597 and "
        "0.9877437; 'tr_M(D) ≈ 0.3883' against 0.5751722; and 'ratio "
        "Phase5q/witness expected ~1.875' against 1.2055. The p/n pair now "
        "prints live and is asserted against the witness's tr_M_at_q0; the "
        "deuteron pair is left as recorded since it is the object the "
        "qou-lnog preflight rejects."
    )

    elapsed = time.time() - t0
    log(f"\nTotal elapsed: {elapsed:.1f} s")
    builder.add_data("elapsed_seconds", elapsed)

    builder.save()
    log(f"✓ Witness saved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
