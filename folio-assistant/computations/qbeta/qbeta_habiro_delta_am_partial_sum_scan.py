#!/usr/bin/env python3
"""
qbeta_habiro_delta_am_partial_sum_scan.py — Δa_m partial-sum cyclotomic scan
============================================================================

STRUCTURAL probe for the universal Φ_8 = (u^4+1) factor in atomic-step
Habiro elements.

For each atomic pair (D−n), (³He−D), (⁴He−³He), compute the partial
sums

   S_M(X−Y) = Σ_{m=0..M} Δa_m(X−Y) · (u; u)_m       (M = 0..M_max)

as integer polynomials in u = √q, factor each S_M via sympy.factor over
ℤ[u], and:

  1.  identify the smallest M for which Φ_8(u^2) = u^4 + 1 first
      divides S_M (let's call this M_first_Φ_8);
  2.  identify M_first_Φ_8²;
  3.  at M_first_Φ_8, isolate the Δa_m·(u;u)_m terms whose ALGEBRAIC
      INTERFERENCE produces the new (u^4+1) factor — concretely we
      compute Q(u) = S_M(u) / (u^4+1) and the marginal contribution
      ΔS_M − ΔS_{M-1} = Δa_M · (u;u)_M, then see which prior Δa_m
      terms combine with this marginal to yield the (u^4+1) factor;
  4.  cross-pair comparison: is the M-of-first-appearance the same
      across (D−n), (³He−D), (⁴He−³He)?

CONTEXT
=======

PR #1579 + #1618 established the universal Φ_8² across all three atomic
pairs and ruled out the naive mechanisms (strand-doubling Φ_{2^{k+1}},
z(q)² interface, m=8 Pochhammer boundary). The
[`docs/audits/2026-06-01-qbeta-habiro-phi8-squared-mechanism.md`]
prefix-sum table (Test 3) already reports:

  | Pair       | M_first_Φ_8 | M_first_Φ_8² |
  | (D − n)    | M = 7        | M = 12         |
  | (³He − D)  | M = 7        | M = 15         |
  | (⁴He − ³He)| M = 7        | M = 15         |

The M = 7 entry is PRE-Pochhammer-boundary (m=8 is where (u;u)_m first
acquires Φ_8). This proves the (u^4+1) factor lives in the Δa_m
algebraic interference itself. This script PINS the interference: it
exhibits Q(u) at M_first_Φ_8 and tabulates the Δa_m·(u;u)_m summands
to reveal which terms combine to produce the (u^4+1) factor.

DATA SOURCES
============

  - folio-assistant/computations/habiro-coefficients-atomic.witness.json
    (p, n, D; on main)
  - /tmp/he3.json, /tmp/he4.json — ³He, ⁴He, extracted from
    PR #1618 branch (claude/qbeta-habiro-followup-2026-06-01) since
    those witnesses are not yet on main. The probe falls back to
    looking for sibling-branch witnesses in `folio-assistant/computations/`
    if /tmp copies are missing.

USAGE
-----
  python3 -u qbeta_habiro_delta_am_partial_sum_scan.py 2>&1 \
      | tee /tmp/da_m_scan.log

OUTPUTS
-------
  folio-assistant/computations/qbeta-habiro-delta-am-partial-sum-scan.witness.json

Ref:
  docs/audits/2026-06-01-qbeta-habiro-phi8-squared-mechanism.md
  docs/coordination/2026-06-01-phi8-da-m-interference.md (Track 1)
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


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


# ────────────────────── Coefficient loader ─────────────────────────────────


def parse_coeffs(habiro_entries: list[dict], u: sp.Symbol) -> dict[int, sp.Poly]:
    """Parse the `habiro_coefficients` array (list of {m, a_m, ...}) into
    a dict of sympy.Poly in u with integer coefficients."""
    out: dict[int, sp.Poly] = {}
    for entry in habiro_entries:
        m = int(entry["m"])
        a_str = entry["a_m"]
        out[m] = sp.Poly(sp.sympify(a_str), u, domain="ZZ")
    return out


def load_atomic(u: sp.Symbol) -> dict[str, dict[int, sp.Poly]]:
    path = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    log(f"Loading atomic witness: {path.name}")
    data = json.loads(path.read_text())
    return {
        "p": parse_coeffs(
            data["results"]["p (proton, A=1)"]["habiro_coefficients"], u
        ),
        "n": parse_coeffs(
            data["results"]["n (neutron, A=1)"]["habiro_coefficients"], u
        ),
        "D": parse_coeffs(
            data["results"]["D (deuteron, A=2)"]["habiro_coefficients"], u
        ),
    }


def load_helium(u: sp.Symbol) -> dict[str, dict[int, sp.Poly]]:
    """Helium witnesses live on PR #1618 branch (not on main yet).
    We try /tmp first (extracted via `git show`), then a sibling-branch
    fallback inside folio-assistant/computations."""

    def _try(p: Path) -> dict | None:
        if p.exists():
            log(f"Loading helium witness: {p}")
            return json.loads(p.read_text())
        return None

    out: dict[str, dict[int, sp.Poly]] = {}
    for label, fname in (("He3", "habiro-coefficients-helium-3.witness.json"),
                         ("He4", "habiro-coefficients-helium-4.witness.json")):
        d = _try(Path(f"/tmp/{ 'he3.json' if label == 'He3' else 'he4.json'}"))
        if d is None:
            d = _try(HERE / fname)
        if d is None:
            raise FileNotFoundError(
                f"Cannot find helium witness for {label}: expected /tmp/"
                + ("he3.json" if label == "He3" else "he4.json")
                + " or "
                + str(HERE / fname)
            )
        out[label] = parse_coeffs(d["habiro_coefficients"], u)
    return out


# ───────────────────── q-Pochhammer (u; u)_m ───────────────────────────────


def pochhammer_uu(m: int, u: sp.Symbol) -> sp.Expr:
    """(u; u)_m = Π_{k=1..m} (1 - u^k), as an expanded polynomial in u."""
    out = sp.Integer(1)
    for k in range(1, m + 1):
        out = sp.expand(out * (1 - u**k))
    return out


# ─────────────────── Scan: cyclotomic content of S_M ───────────────────────


def divides_in_u(poly_expr: sp.Expr, divisor_expr: sp.Expr,
                 u: sp.Symbol) -> bool:
    """True iff `divisor_expr` divides `poly_expr` over ℚ[u]
    (equivalently ℤ[u] for monic divisors). Uses sympy.div."""
    if sp.simplify(poly_expr) == 0:
        return True
    q, r = sp.div(sp.expand(poly_expr), sp.expand(divisor_expr), u)
    return sp.simplify(r) == 0


def multiplicity_in_u(poly_expr: sp.Expr, divisor_expr: sp.Expr,
                      u: sp.Symbol, max_mult: int = 8) -> int:
    """Maximal k ≥ 0 such that divisor_expr^k divides poly_expr."""
    if sp.simplify(poly_expr) == 0:
        return max_mult  # by convention; we never actually call with 0
    current = sp.expand(poly_expr)
    k = 0
    while k < max_mult:
        q, r = sp.div(current, divisor_expr, u)
        if sp.simplify(r) != 0:
            break
        current = sp.expand(q)
        k += 1
    return k


def scan_pair(delta_a: dict[int, sp.Poly], pair_label: str,
              u: sp.Symbol) -> dict:
    """Compute S_M and the Φ_8 multiplicity for every M up to M_max."""
    log("=" * 78)
    log(f"  Pair: {pair_label}")
    log("=" * 78)

    phi4_of_u2 = u**4 + 1   # Φ_8(u) = u^4 + 1   (also written Φ_4(u^2))
    # Note: in this codebase the universal factor is referred to as both
    # "Φ_8" (root of unity ζ_8) and equivalently "Φ_4(u²) = u^4 + 1"
    # because we work in u-coordinates with q = u². The polynomial in
    # u is u^4 + 1.

    ms = sorted(delta_a.keys())
    M_max = max(ms)

    # Precompute (u;u)_m, one term Δa_m·(u;u)_m, and cumulative S_M
    pochs: dict[int, sp.Expr] = {}
    terms: dict[int, sp.Expr] = {}
    partial: dict[int, sp.Expr] = {}
    running = sp.Integer(0)
    for m in ms:
        pochs[m] = pochhammer_uu(m, u)
        am = delta_a[m].as_expr()
        terms[m] = sp.expand(am * pochs[m])
        running = sp.expand(running + terms[m])
        partial[m] = running

    # Multiplicity of Φ_8 = u^4 + 1 in each S_M
    log(" m | deg S_M |  Φ_8 mult | S_M factored (short)")
    log("---|---------|-----------|----------------------")
    rows = []
    M_first_phi8 = None
    M_first_phi8sq = None
    for m in ms:
        sm = partial[m]
        if sp.simplify(sm) == 0:
            mult = 0
            deg = -1
            factored = "0"
        else:
            mult = multiplicity_in_u(sm, phi4_of_u2, u, max_mult=4)
            deg = sp.Poly(sm, u).degree()
            factored = str(sp.factor(sm))
        if mult >= 1 and M_first_phi8 is None:
            M_first_phi8 = m
        if mult >= 2 and M_first_phi8sq is None:
            M_first_phi8sq = m
        # Trim the factored string for the log
        snippet = factored if len(factored) < 70 else factored[:67] + "..."
        log(f" {m:2d} | {deg:6d}  | {mult:7d}   | {snippet}")
        rows.append({
            "M": m,
            "deg_S_M": deg,
            "phi8_multiplicity": mult,
            "S_M_factored": factored,
            "S_M_factored_truncated_chars": len(factored),
        })

    log(f"\n  M_first_Φ_8  = {M_first_phi8}")
    log(f"  M_first_Φ_8² = {M_first_phi8sq}")

    # Direct algebraic identification at M_first_Φ_8
    boundary_info = {}
    if M_first_phi8 is not None:
        Mf = M_first_phi8
        Sm = partial[Mf]
        Sm_prev = partial[ms[ms.index(Mf) - 1]] if ms.index(Mf) > 0 else sp.Integer(0)
        # Compute Q(u) such that S_Mf = (u^4+1) · Q(u)
        Q, rem = sp.div(sp.expand(Sm), phi4_of_u2, u)
        assert sp.simplify(rem) == 0, (
            f"INTERNAL: S_Mf supposed to be divisible by Φ_8 at M={Mf}, "
            f"but remainder = {rem}"
        )
        # Marginal contribution at M=Mf
        marginal = terms[Mf]
        # Is marginal alone divisible by Φ_8? (almost always NO; the
        # Φ_8 factor is born from interference with prior partial sum)
        marginal_div_phi8 = divides_in_u(marginal, phi4_of_u2, u)
        prev_div_phi8 = (sp.simplify(Sm_prev) == 0) or divides_in_u(
            Sm_prev, phi4_of_u2, u
        )
        # The interference: Sm = Sm_prev + marginal, and BOTH are
        # individually NOT divisible by Φ_8, yet their sum IS.
        # The interference is a polynomial identity:
        #     Sm_prev ≡ -marginal  (mod Φ_8)
        # Equivalently their values at the 4 roots of u^4+1=0 are
        # equal-and-opposite.
        zeta8 = sp.exp(sp.I * sp.pi / 4)  # u = ζ_8 ⇒ u^4 = -1
        # Numerically check Sm_prev(ζ_8) and marginal(ζ_8); should
        # cancel exactly.
        Sm_prev_at_zeta8 = sp.simplify(Sm_prev.subs(u, zeta8))
        marginal_at_zeta8 = sp.simplify(marginal.subs(u, zeta8))
        sum_at_zeta8 = sp.simplify(Sm_prev_at_zeta8 + marginal_at_zeta8)

        # The "minimal cone" of contributors: find the smallest subset
        # {m_1, …, m_k} ⊆ {0,…,Mf} such that Σ_i Δa_{m_i}·(u;u)_{m_i}
        # is divisible by Φ_8. We use a greedy from the top: start
        # with {Mf} and add back terms in m-descending order until
        # divisibility holds.
        contributors = []
        partial_sum = sp.Integer(0)
        for m_idx in sorted(ms, reverse=True):
            if m_idx > Mf:
                continue
            partial_sum = sp.expand(partial_sum + terms[m_idx])
            contributors.append(m_idx)
            if (sp.simplify(partial_sum) != 0
                    and divides_in_u(partial_sum, phi4_of_u2, u)):
                break
        if not divides_in_u(partial_sum, phi4_of_u2, u):
            contributors = ms[:ms.index(Mf) + 1]  # fall back to all of them

        boundary_info = {
            "M_first_phi8": int(Mf),
            "S_M_at_first_phi8": str(sp.expand(Sm)),
            "S_M_factored": str(sp.factor(Sm)),
            "Q_u_quotient": str(sp.expand(Q)),
            "Q_u_factored": str(sp.factor(Q)),
            "marginal_term_Δa_M_uum": str(sp.expand(marginal)),
            "marginal_divisible_by_phi8": marginal_div_phi8,
            "prev_partial_S_Mminus1": str(sp.expand(Sm_prev)),
            "prev_partial_divisible_by_phi8": prev_div_phi8,
            "Sm_prev_at_u_eq_zeta8": str(Sm_prev_at_zeta8),
            "marginal_at_u_eq_zeta8": str(marginal_at_zeta8),
            "sum_at_u_eq_zeta8 (should be 0)": str(sum_at_zeta8),
            "minimal_top_down_contributors_m_set": sorted(contributors),
        }
        log("\n  At M = M_first_Φ_8 = %d:" % Mf)
        log(f"    S_M = (u^4+1) · Q(u)")
        Q_str = str(sp.expand(Q))
        log(f"    Q(u) = {Q_str if len(Q_str) < 200 else Q_str[:197] + '...'}")
        log(f"    Σ_prev divisible by Φ_8? {prev_div_phi8}")
        log(f"    marginal divisible by Φ_8? {marginal_div_phi8}")
        log(f"    Sm_prev(ζ_8) + marginal(ζ_8) = {sum_at_zeta8}")
        log(f"    minimal top-down contributors: {sorted(contributors)}")

    return {
        "pair": pair_label,
        "ms": ms,
        "M_max": M_max,
        "rows": rows,
        "M_first_phi8": M_first_phi8,
        "M_first_phi8_squared": M_first_phi8sq,
        "boundary_analysis": boundary_info,
    }


# ──────────────────────────── main ─────────────────────────────────────────


def main() -> int:
    u = sp.Symbol("u")
    t0 = time.perf_counter()

    builder = WitnessBuilder(
        "qbeta-habiro-delta-am-partial-sum-scan",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Δa_m partial-sum cyclotomic scan: for each atomic-step pair "
        "(D−n), (³He−D), (⁴He−³He), compute S_M = Σ_{m=0..M} Δa_m·(u;u)_m "
        "for M = 0..M_max as polynomials over ℤ[u], factor each S_M, "
        "record the multiplicity of Φ_8(u) = u^4 + 1 in S_M, and identify "
        "the smallest M for which Φ_8 (resp. Φ_8²) first divides S_M. "
        "At the M_first_Φ_8 boundary, compute Q(u) = S_M/(u^4+1) and "
        "isolate the interference between Σ_prev and the marginal "
        "Δa_M·(u;u)_M that produces the new (u^4+1) factor. Cross-pair "
        "comparison reveals whether M_first_Φ_8 is pair-invariant or "
        "pair-dependent."
    )
    builder.set_content_block("prop:full-pole-structure-mass-trace")

    atomic = load_atomic(u)
    helium = load_helium(u)

    # Build the three pair Δa_m maps.
    def make_delta(X: dict[int, sp.Poly],
                   Y: dict[int, sp.Poly]) -> dict[int, sp.Poly]:
        ms = sorted(set(X) | set(Y))
        out: dict[int, sp.Poly] = {}
        for m in ms:
            a_x = X.get(m, sp.Poly(0, u, domain="ZZ"))
            a_y = Y.get(m, sp.Poly(0, u, domain="ZZ"))
            delta = sp.Poly(a_x.as_expr() - a_y.as_expr(), u, domain="ZZ")
            out[m] = delta
        return out

    pairs = {
        "D_minus_n": make_delta(atomic["D"], atomic["n"]),
        "He3_minus_D": make_delta(helium["He3"], atomic["D"]),
        "He4_minus_He3": make_delta(helium["He4"], helium["He3"]),
    }

    results = {}
    for pair_label, delta in pairs.items():
        results[pair_label] = scan_pair(delta, pair_label, u)
        builder.add_data(pair_label, results[pair_label])

    # ─── Cross-pair comparison ─────────────────────────────────────────
    log("\n" + "=" * 78)
    log("  CROSS-PAIR M-OF-FIRST-APPEARANCE")
    log("=" * 78)
    log(" Pair          | M_first_Φ_8 | M_first_Φ_8² ")
    log("---------------|--------------|----------------")
    pair_table = {}
    for pair_label, r in results.items():
        log(f" {pair_label:13s} | {str(r['M_first_phi8']):12s} | {str(r['M_first_phi8_squared']):14s}")
        pair_table[pair_label] = {
            "M_first_phi8": r["M_first_phi8"],
            "M_first_phi8_squared": r["M_first_phi8_squared"],
        }

    # Pair-invariance: is M_first_Φ_8 the same across all three pairs?
    m_first_set = {r["M_first_phi8"] for r in results.values()}
    m_first_sq_set = {r["M_first_phi8_squared"] for r in results.values()}
    log(f"\n  M_first_Φ_8 set (across pairs): {sorted(m_first_set)}")
    log(f"  M_first_Φ_8² set (across pairs): {sorted(m_first_sq_set)}")

    universal = len(m_first_set) == 1
    universal_sq = len(m_first_sq_set) == 1
    log(f"\n  M_first_Φ_8  pair-invariant? {universal}")
    log(f"  M_first_Φ_8² pair-invariant? {universal_sq}")

    builder.add_data("cross_pair_summary", {
        "per_pair": pair_table,
        "M_first_phi8_set": sorted([x for x in m_first_set if x is not None]),
        "M_first_phi8_squared_set": sorted(
            [x for x in m_first_sq_set if x is not None]
        ),
        "M_first_phi8_universal_across_pairs": universal,
        "M_first_phi8_squared_universal_across_pairs": universal_sq,
    })

    # ─── Verdict ───────────────────────────────────────────────────────
    if universal and universal_sq:
        verdict = "UNIVERSAL: same M_first_Φ_8 AND M_first_Φ_8² across pairs"
    elif universal:
        verdict = (
            "Φ_8 pair-invariant, Φ_8² pair-dependent — single-cyclotomic "
            "interference is universal at fixed depth, but Φ_8² depth varies "
            "with helium-vs-deuteron complexity"
        )
    elif universal_sq:
        verdict = "Φ_8² pair-invariant, Φ_8 pair-dependent"
    else:
        verdict = "PAIR-DEPENDENT at both Φ_8 and Φ_8²"
    log(f"\n  VERDICT: {verdict}")
    builder.add_data("verdict", verdict)

    builder.add_assertion(
        "phi8_first_at_M_le_7_for_D_minus_n",
        computed=results["D_minus_n"]["M_first_phi8"] or -1,
        expected=7,
        tolerance=0,
        source="PR #1618 mechanism doc Test 3 prefix-sum table.",
    )
    builder.save()
    log("\n  ✓ Witness saved: qbeta-habiro-delta-am-partial-sum-scan.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
