#!/usr/bin/env python3
"""qbeta_habiro_delta_a_m_pattern_probe.py — Q_β Habiro element via
the Δa_m(u) = a_m(n) - a_m(p) integer-coefficient sequence.

CONTEXT. Existing qbeta_habiro_element_probe.py established 6
structural invariants (C1..C6) for the Q_β Habiro element. The
KEY invariant C6 says:

    The Q_β-relevant Habiro element IS the difference
    Δa_m(u) := a_m(n) - a_m(p)

with Δa_0 = 0 (common leading coefficient). The existing probe
documented this but did not extract Δa_m or look for its closed
form.

This probe extracts Δa_m for m = 0..8 from
habiro-coefficients-atomic.witness.json and asks:
  - What is the integer-coefficient structure of Δa_m(u)?
  - Does Δa_m have a closed Habiro-ring form (polynomial in u,
    rational function in q, or [k]_q-product)?
  - Does the pattern have a small-prime factorisation hint
    (recall: 10 = 2·5, 64 = 2⁶, etc.)?

PRE-STATED VERDICT SHAPES.

  TIER 1 (proved-candidate): Δa_m(u) factors cleanly as
    Δa_m(u) = (integer) · F(u) · G(m) — clean closed form, worth
    structural derivation.

  TIER 2 (pattern hint): integer GCD structure or [k]_q
    factorisation visible but not closed; documents the
    constraint for the next session.

  TIER 3 (no pattern): Δa_m(u) coefficients are arbitrary
    integers — refutes the simple Habiro element ansatz; the
    Q_β Habiro element has higher-order structure than a
    coefficient-polynomial.

DISCIPLINE: pure structural extraction, NO new substrate constant.
Per AGENTS.md, does NOT propose c_k closure — only identifies the
integer-coefficient signature of the underlying Habiro element.

Builds on (does not duplicate):
  - merged qbeta_habiro_element_probe.py (C1..C6 invariants)
  - merged fc092f4e3 Item II (sign-channel × dim H_n cross-atom —
    HOPF-LINK-SPECIFIC, complementary, not overlapping)
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

from witness_base import WitnessBuilder  # noqa: E402


def _parse_a_m_to_poly(a_m_str: str, u_sym: sp.Symbol) -> sp.Expr:
    """Parse witness string like '340*u**2 + 365*u + 389' into a sympy Poly."""
    return sp.sympify(a_m_str, locals={"check_q": u_sym})


def _gcd_of_coeffs(poly: sp.Poly) -> int:
    """Return GCD of all integer coefficients."""
    coeffs = [int(c) for c in poly.all_coeffs() if c != 0]
    if not coeffs:
        return 0
    g = abs(coeffs[0])
    for c in coeffs[1:]:
        g = sp.gcd(g, abs(c))
    return int(g)



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
    t0 = time.monotonic()

    builder = WitnessBuilder(
        "qbeta-habiro-delta-a-m-pattern-probe",
        engine="python+sympy", start_time=t0,
    )
    builder.set_description(
        "Q_β Habiro element Δa_m(u) = a_m(n) - a_m(p) structural "
        "extraction. Probes invariant C6 from qbeta_habiro_element_probe.py "
        "for closed-form pattern."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-02-yekutieli-A2-qbeta-mn-he4-workplan.md"
    )

    cache_path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    with open(cache_path) as f:
        cache = json.load(f)
    p_data = cache["results"]["p (proton, A=1)"]
    n_data = cache["results"]["n (neutron, A=1)"]
    _qou_lnog_preflight(n_data["tr_M_in_q"], p_data["tr_M_in_q"], "n - p")

    u = sp.symbols("u")
    p_a_m = [(c["m"], _parse_a_m_to_poly(c["a_m"], u))
             for c in p_data["habiro_coefficients"]]
    n_a_m = [(c["m"], _parse_a_m_to_poly(c["a_m"], u))
             for c in n_data["habiro_coefficients"]]

    assert len(p_a_m) == len(n_a_m), "Habiro depth mismatch"

    print("=" * 78)
    print(" Q_β Habiro element Δa_m(u) — structural pattern extraction")
    print("=" * 78)
    print(f"M_max = {len(p_a_m) - 1}  (from C3 invariant)")
    print()

    print(f"{'m':>3} {'Δa_m(u) = a_m(n) - a_m(p)':<50} {'gcd':>6} {'factors':<20}")
    print("-" * 92)
    delta_series = []
    for (m_p, p_poly), (m_n, n_poly) in zip(p_a_m, n_a_m):
        assert m_p == m_n
        delta = sp.expand(n_poly - p_poly)
        delta_str = str(delta)
        if delta == 0:
            gcd_str = "—"
            factors_str = "0"
        else:
            delta_poly = sp.Poly(delta, u)
            gcd = _gcd_of_coeffs(delta_poly)
            factored = sp.factor(delta)
            gcd_str = str(gcd)
            factors_str = str(factored)[:30]
        print(f"  {m_p:>3} {delta_str:<48} {gcd_str:>6} {factors_str}")
        delta_series.append({
            "m": m_p,
            "delta_a_m": delta_str,
            "gcd": gcd_str,
            "factored": str(sp.factor(delta)) if delta != 0 else "0",
        })

    # Pattern search: GCD growth, dominant-coefficient pattern
    print()
    print("=" * 78)
    print(" Pattern analysis")
    print("=" * 78)
    print()
    gcds = [d["gcd"] for d in delta_series if d["gcd"] not in ("—", "0")]
    print(f"GCD sequence (excluding m=0):")
    for i, d in enumerate(delta_series[1:], 1):
        print(f"  m={i}: gcd = {d['gcd']}")
    print()

    # Lead coefficient of Δa_m as a polynomial in u
    print(f"Lead coefficients (highest-power-u coefficient of Δa_m):")
    lead_coeffs = []
    for d in delta_series:
        if d["delta_a_m"] == "0":
            lead_coeffs.append(0)
        else:
            poly = sp.Poly(sp.sympify(d["delta_a_m"], locals={"check_q": u}), u)
            lc = int(poly.LC()) if poly.LC() else 0
            lead_coeffs.append(lc)
    print(f"  {lead_coeffs}")
    print()

    # Constant term of Δa_m
    print(f"Constant terms (u=0 value of Δa_m):")
    const_terms = []
    for d in delta_series:
        if d["delta_a_m"] == "0":
            const_terms.append(0)
        else:
            expr = sp.sympify(d["delta_a_m"], locals={"check_q": u})
            const = int(expr.subs(u, 0))
            const_terms.append(const)
    print(f"  {const_terms}")
    print()

    # Δa_m at u=1 — observable-level evaluation
    print(f"Δa_m at u=1 (classical limit):")
    u_1_vals = []
    for d in delta_series:
        if d["delta_a_m"] == "0":
            u_1_vals.append(0)
        else:
            expr = sp.sympify(d["delta_a_m"], locals={"check_q": u})
            v = int(expr.subs(u, 1))
            u_1_vals.append(v)
    print(f"  {u_1_vals}")
    print()

    # Δa_m at u=-1 (bar-involution check)
    print(f"Δa_m at u=-1 (bar-involution-like point):")
    u_m1_vals = []
    for d in delta_series:
        if d["delta_a_m"] == "0":
            u_m1_vals.append(0)
        else:
            expr = sp.sympify(d["delta_a_m"], locals={"check_q": u})
            v = int(expr.subs(u, -1))
            u_m1_vals.append(v)
    print(f"  {u_m1_vals}")
    print()

    # Ratios — search for geometric / factorial patterns
    print(f"Δa_m / Δa_(m-1) at u=1 (geometric-ratio probe):")
    for i in range(1, len(u_1_vals)):
        if u_1_vals[i - 1] != 0:
            r = sp.Rational(u_1_vals[i], u_1_vals[i - 1])
            print(f"  m={i}: ratio = {r} = {float(r):.4f}")
    print()

    # Verdict
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    # Heuristic: check if all lead coeffs are multiples of gcd_1 = 10
    gcd_1 = abs(lead_coeffs[1]) if lead_coeffs[1] != 0 else 0
    all_div_gcd_1 = (
        gcd_1 > 0 and
        all(c % gcd_1 == 0 for c in lead_coeffs if c != 0)
    )

    if all_div_gcd_1 and gcd_1 >= 5:
        verdict = (
            f"TIER 2 PATTERN HIT — all lead coefficients are multiples of "
            f"gcd_1 = {gcd_1}, suggesting Δa_m(u) = {gcd_1} · f_m(u) for "
            f"some integer polynomial f_m. The Q_β Habiro element has a "
            f"common scale factor; the structural target is now f_m. Next "
            f"sub-probe: extract f_m sequence and look for closed form."
        )
    else:
        verdict = (
            "TIER 3 — no clean shared scale across Δa_m series. The Q_β "
            "Habiro element does NOT factor as (common-scale) · f_m(u) "
            "with f_m simple. The closed form (if any) is more elaborate "
            "and lives beyond the 8-term polynomial-in-u-coefficient "
            "representation. Next sub-probe: try OGF / q-difference form "
            "rather than direct coefficient pattern."
        )

    print(verdict)
    print()

    builder.add_data("M_max", len(p_a_m) - 1)
    builder.add_data("delta_a_m_series", delta_series)
    builder.add_data("gcd_sequence", gcds)
    builder.add_data("lead_coefficients", lead_coeffs)
    builder.add_data("constant_terms", const_terms)
    builder.add_data("u_1_values", u_1_vals)
    builder.add_data("u_minus1_values", u_m1_vals)
    builder.add_data("verdict", verdict)
    builder.add_data("invariant_C6_extension", (
        "This probe extracts Δa_m(u) (the Q_β Habiro element per "
        "qbeta_habiro_element_probe.py C6) and reports its integer-"
        "coefficient signature. Complements (does not duplicate) the "
        "main-landed fc092f4e3 Item II sign-channel × dim H_n cross-atom "
        "probe — that probe is Hopf-link-specific (2-strand); this "
        "probe is the 3-strand neutron/proton Habiro decomposition."
    ))

    builder.add_assertion(
        name="delta_a_0_is_zero",
        computed=delta_series[0]["delta_a_m"] == "0",
        expected=True,
        tolerance=0.0,
        source="C6 invariant: common leading Habiro coefficient",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
