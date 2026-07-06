#!/usr/bin/env python3
"""
qbeta_habiro_all_10_pairs_phi8_universality.py — Φ_8 universality across all 10 pair-differences
================================================================================================

STRUCTURAL probe extending PR #1625 Track 1 from 3 atomic-step pairs to ALL
10 distinct pair-differences among the 5 canonical atoms {p, n, D, ³He, ⁴He}.

PREDICTION
==========

The level-2 SU(2) Wenzl annihilator at q = ζ_8 acts on the Markov-trace
decomposition of any canonical braid word. This forces a linear relation
on EACH tr_M(β_K); differencing two such constraints still yields a linear
relation that produces the Φ_8(u) = u^4 + 1 cancellation at M = 7 in the
prefix-sum scan.

Prediction: M_first_Φ_8 = 7 for ALL 10 pairs (X − Y), X, Y ∈ {p, n, D, ³He, ⁴He}.

PAIRS
=====

5 choose 2 = 10 pairs:

   1.  n − p         (isospin doublet; tested at PR #1579 — (u−1)(u+1)=Φ_1·Φ_2 factor)
   2.  D − p         (A=2 vs A=1, Z-fixed)
   3.  D − n         (A=2 vs A=1, N-fixed) — TESTED M=7 ✓ in PR #1625 Track 1
   4.  ³He − p       (A=3 vs A=1)
   5.  ³He − n       (A=3 vs A=1)
   6.  ³He − D       (A=3 vs A=2) — TESTED M=7 ✓ in PR #1625 Track 1
   7.  ⁴He − p       (A=4 vs A=1)
   8.  ⁴He − n       (A=4 vs A=1)
   9.  ⁴He − D       (A=4 vs A=2)
  10.  ⁴He − ³He     (A=4 vs A=3) — TESTED M=7 ✓ in PR #1625 Track 1

For each pair, we compute Δa_m = a_m(X) − a_m(Y), then

   S_M(X−Y) = Σ_{m=0..M} Δa_m(X−Y) · (u; u)_m       (M = 0..M_max)

as integer polynomials in u, factor each S_M via sympy.factor over ℤ[u],
identify the smallest M for which Φ_8(u) = u^4 + 1 first divides S_M,
and additionally identify Φ_8² boundary if reached.

For (n − p) we ALSO scan Φ_1·Φ_2 = u² − 1 multiplicity to verify that
the PR #1579 isospin-doublet factor coexists with (or replaces) the
universal Φ_8.

DATA SOURCES
============

  - computations/habiro-coefficients-atomic.witness.json
    (p, n, D)
  - /tmp/he3.json, /tmp/he4.json (helium from PR #1618 branch)

USAGE
-----
  python3 -u qbeta_habiro_all_10_pairs_phi8_universality.py 2>&1 \
      | tee /tmp/all_10_pairs_phi8.log

OUTPUTS
-------
  computations/qbeta-habiro-all-10-pairs-phi8-universality.witness.json

Ref:
  docs/audits/2026-06-01-qbeta-habiro-all-10-pairs-phi8-universality.md
  PR #1625 Track 1 (qbeta_habiro_delta_am_partial_sum_scan.py)
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
import itertools
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
    out: dict[str, dict[int, sp.Poly]] = {}
    for label, fname in (("He3", "/tmp/he3.json"), ("He4", "/tmp/he4.json")):
        p = Path(fname)
        if not p.exists():
            raise FileNotFoundError(f"Cannot find helium witness for {label}: {p}")
        log(f"Loading helium witness: {p}")
        d = json.loads(p.read_text())
        out[label] = parse_coeffs(d["habiro_coefficients"], u)
    return out


# ───────────────────── q-Pochhammer (u; u)_m ───────────────────────────────


def pochhammer_uu(m: int, u: sp.Symbol) -> sp.Expr:
    """(u; u)_m = Π_{k=1..m} (1 - u^k)."""
    out = sp.Integer(1)
    for k in range(1, m + 1):
        out = sp.expand(out * (1 - u**k))
    return out


# ─────────────────── Scan: cyclotomic content of S_M ───────────────────────


def divides_in_u(poly_expr: sp.Expr, divisor_expr: sp.Expr,
                 u: sp.Symbol) -> bool:
    if sp.simplify(poly_expr) == 0:
        return True
    q, r = sp.div(sp.expand(poly_expr), sp.expand(divisor_expr), u)
    return sp.simplify(r) == 0


def multiplicity_in_u(poly_expr: sp.Expr, divisor_expr: sp.Expr,
                      u: sp.Symbol, max_mult: int = 4) -> int:
    if sp.simplify(poly_expr) == 0:
        return max_mult
    current = sp.expand(poly_expr)
    k = 0
    while k < max_mult:
        q, r = sp.div(current, divisor_expr, u)
        if sp.simplify(r) != 0:
            break
        current = sp.expand(q)
        k += 1
    return k


def make_delta(X: dict[int, sp.Poly], Y: dict[int, sp.Poly],
               u: sp.Symbol) -> dict[int, sp.Poly]:
    """Δa_m = a_m(X) − a_m(Y) on the COMMON range only (min of M_max(X), M_max(Y))."""
    M_common = min(max(X), max(Y))
    out: dict[int, sp.Poly] = {}
    for m in range(M_common + 1):
        a_x = X.get(m, sp.Poly(0, u, domain="ZZ"))
        a_y = Y.get(m, sp.Poly(0, u, domain="ZZ"))
        delta = sp.Poly(a_x.as_expr() - a_y.as_expr(), u, domain="ZZ")
        out[m] = delta
    return out


def scan_pair(delta_a: dict[int, sp.Poly], pair_label: str, u: sp.Symbol,
              also_scan_phi1phi2: bool = False) -> dict:
    log("=" * 78)
    log(f"  Pair: {pair_label}")
    log("=" * 78)

    phi8 = u**4 + 1               # Φ_8(u)
    phi1phi2 = u**2 - 1           # Φ_1 · Φ_2 = (u-1)(u+1)

    ms = sorted(delta_a.keys())
    M_max = max(ms)

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

    log(" M | deg S_M | Φ_8 mult | (u²−1) mult | S_M factored (short)")
    log("---|---------|----------|-------------|-----------------------")
    rows = []
    M_first_phi8 = None
    M_first_phi8sq = None
    M_first_phi1phi2 = None
    for m in ms:
        sm = partial[m]
        if sp.simplify(sm) == 0:
            mult_phi8 = 0
            mult_phi1phi2 = 0
            deg = -1
            factored = "0"
        else:
            mult_phi8 = multiplicity_in_u(sm, phi8, u, max_mult=4)
            mult_phi1phi2 = (multiplicity_in_u(sm, phi1phi2, u, max_mult=4)
                             if also_scan_phi1phi2 else -1)
            deg = sp.Poly(sm, u).degree()
            factored = str(sp.factor(sm))
        if mult_phi8 >= 1 and M_first_phi8 is None:
            M_first_phi8 = m
        if mult_phi8 >= 2 and M_first_phi8sq is None:
            M_first_phi8sq = m
        if (also_scan_phi1phi2 and mult_phi1phi2 >= 1
                and M_first_phi1phi2 is None):
            M_first_phi1phi2 = m
        snippet = factored if len(factored) < 60 else factored[:57] + "..."
        log(f" {m:2d} | {deg:6d}  | {mult_phi8:6d}   | {(str(mult_phi1phi2) if also_scan_phi1phi2 else '   −'):9s}  | {snippet}")
        rows.append({
            "M": m,
            "deg_S_M": deg,
            "phi8_multiplicity": mult_phi8,
            "phi1phi2_multiplicity": (mult_phi1phi2 if also_scan_phi1phi2 else None),
            "S_M_factored": factored,
        })

    log(f"\n  M_first_Φ_8     = {M_first_phi8}")
    log(f"  M_first_Φ_8²    = {M_first_phi8sq}")
    if also_scan_phi1phi2:
        log(f"  M_first_(u²−1) = {M_first_phi1phi2}")

    # Boundary analysis at M_first_Φ_8 (if reached)
    boundary_info = {}
    if M_first_phi8 is not None:
        Mf = M_first_phi8
        Sm = partial[Mf]
        Sm_prev = (partial[ms[ms.index(Mf) - 1]]
                   if ms.index(Mf) > 0 else sp.Integer(0))
        Q, rem = sp.div(sp.expand(Sm), phi8, u)
        assert sp.simplify(rem) == 0, (
            f"INTERNAL: S_Mf supposed divisible by Φ_8 at M={Mf}, rem={rem}"
        )
        marginal = terms[Mf]
        marginal_div_phi8 = divides_in_u(marginal, phi8, u)
        prev_div_phi8 = (sp.simplify(Sm_prev) == 0) or divides_in_u(
            Sm_prev, phi8, u
        )
        zeta8 = sp.exp(sp.I * sp.pi / 4)
        Sm_prev_at_zeta8 = sp.simplify(Sm_prev.subs(u, zeta8))
        marginal_at_zeta8 = sp.simplify(marginal.subs(u, zeta8))
        sum_at_zeta8 = sp.simplify(Sm_prev_at_zeta8 + marginal_at_zeta8)
        boundary_info = {
            "M_first_phi8": int(Mf),
            "Q_u_factored": str(sp.factor(Q)),
            "marginal_divisible_by_phi8": marginal_div_phi8,
            "prev_partial_divisible_by_phi8": prev_div_phi8,
            "Sm_prev_at_u_eq_zeta8": str(Sm_prev_at_zeta8),
            "marginal_at_u_eq_zeta8": str(marginal_at_zeta8),
            "sum_at_u_eq_zeta8 (should be 0)": str(sum_at_zeta8),
        }
        log(f"\n  At M = M_first_Φ_8 = {Mf}:")
        log(f"    Σ_prev(ζ_8) + marginal(ζ_8) = {sum_at_zeta8}")

    return {
        "pair": pair_label,
        "ms": ms,
        "M_max": M_max,
        "rows": rows,
        "M_first_phi8": M_first_phi8,
        "M_first_phi8_squared": M_first_phi8sq,
        "M_first_phi1phi2": (M_first_phi1phi2 if also_scan_phi1phi2 else None),
        "boundary_analysis": boundary_info,
    }


# ──────────────────────────── main ─────────────────────────────────────────


def main() -> int:
    u = sp.Symbol("u")
    t0 = time.perf_counter()

    builder = WitnessBuilder(
        "qbeta-habiro-all-10-pairs-phi8-universality",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Φ_8 universality probe across ALL 10 distinct pair-differences "
        "(X − Y) with X, Y ∈ {p, n, D, ³He, ⁴He}. For each pair, compute "
        "Δa_m = a_m(X) − a_m(Y), build the prefix sums S_M = Σ_{m=0..M} "
        "Δa_m·(u;u)_m, factor over ℤ[u], and identify M_first_Φ_8 — the "
        "smallest M at which Φ_8(u) = u^4 + 1 first divides S_M. "
        "Prediction (per PR #1625 Track 1 + Wenzl-annihilator mechanism): "
        "M_first_Φ_8 = 7 universally. The (n − p) isospin-doublet pair "
        "additionally scans (u²−1) = Φ_1·Φ_2 multiplicity to verify "
        "coexistence with the PR #1579 doublet factor."
    )
    builder.set_content_block("prop:full-pole-structure-mass-trace")

    atomic = load_atomic(u)
    helium = load_helium(u)
    all_atoms = {
        "p": atomic["p"],
        "n": atomic["n"],
        "D": atomic["D"],
        "He3": helium["He3"],
        "He4": helium["He4"],
    }
    M_max_per = {k: max(v) for k, v in all_atoms.items()}
    log(f"  M_max per atom: {M_max_per}")

    # All ordered pairs (X, Y) with X > Y in a canonical ordering, so we
    # get 10 unordered pairs. We use the mass-ordered list (p, n, D, He3, He4).
    order = ["p", "n", "D", "He3", "He4"]
    pairs: list[tuple[str, str]] = []
    for j in range(len(order)):
        for i in range(j):
            # (X, Y) = (order[j], order[i]) = larger − smaller
            pairs.append((order[j], order[i]))
    assert len(pairs) == 10, f"expected 10 pairs, got {len(pairs)}"

    log(f"  Scanning {len(pairs)} pairs: {pairs}")

    results = {}
    for X, Y in pairs:
        pair_label = f"{X}_minus_{Y}"
        delta = make_delta(all_atoms[X], all_atoms[Y], u)
        # For (n − p) ALSO scan (u²−1)
        also = (X == "n" and Y == "p") or (X == "p" and Y == "n")
        # Our canonical order produces (n, p) i.e. n − p
        r = scan_pair(delta, pair_label, u, also_scan_phi1phi2=also)
        r["M_common"] = max(delta)
        results[pair_label] = r
        builder.add_data(pair_label, r)

    # ─── Cross-pair comparison ─────────────────────────────────────────
    log("\n" + "=" * 78)
    log("  CROSS-PAIR M-OF-FIRST-APPEARANCE (Φ_8 universality test)")
    log("=" * 78)
    log(" Pair          | M_common | M_first_Φ_8 | M_first_Φ_8² ")
    log("---------------|----------|-------------|---------------")
    pair_table = {}
    for pair_label, r in results.items():
        log(f" {pair_label:13s} | {str(r['M_common']):7s}  | "
            f"{str(r['M_first_phi8']):11s} | "
            f"{str(r['M_first_phi8_squared']):13s}")
        pair_table[pair_label] = {
            "M_common": r["M_common"],
            "M_first_phi8": r["M_first_phi8"],
            "M_first_phi8_squared": r["M_first_phi8_squared"],
            "M_first_phi1phi2": r["M_first_phi1phi2"],
        }

    # Universality of M_first_Φ_8
    m_first_set = {r["M_first_phi8"] for r in results.values()
                   if r["M_first_phi8"] is not None}
    pairs_no_phi8 = [p for p, r in results.items()
                     if r["M_first_phi8"] is None]
    log(f"\n  M_first_Φ_8 set (across pairs that reach it): {sorted(m_first_set)}")
    if pairs_no_phi8:
        log(f"  Pairs WITHOUT Φ_8 in available range: {pairs_no_phi8}")

    universal = (len(m_first_set) == 1 and m_first_set == {7})
    log(f"\n  Universal {{M_first_Φ_8}} == {{7}} (across all 10 pairs)?  "
        f"{universal}")

    # Special (n − p) report
    np_pair = results.get("n_minus_p")
    np_summary = {}
    if np_pair is not None:
        np_summary = {
            "M_first_phi8": np_pair["M_first_phi8"],
            "M_first_phi8_squared": np_pair["M_first_phi8_squared"],
            "M_first_phi1phi2": np_pair["M_first_phi1phi2"],
            "M_common": np_pair["M_common"],
        }
        log("\n" + "=" * 78)
        log("  (n − p) SPECIAL CASE — isospin doublet")
        log("=" * 78)
        log(f"  M_common         = {np_pair['M_common']}")
        log(f"  M_first_Φ_8      = {np_pair['M_first_phi8']}")
        log(f"  M_first_Φ_8²     = {np_pair['M_first_phi8_squared']}")
        log(f"  M_first_(u²−1)  = {np_pair['M_first_phi1phi2']}")
        if (np_pair["M_first_phi8"] == 7
                and np_pair["M_first_phi1phi2"] is not None):
            log("  → Φ_8 appears at M=7 ALONGSIDE (u²−1)=Φ_1·Φ_2 factor → "
                "ORTHOGONAL structural features (doublet + Wenzl)")
        elif np_pair["M_first_phi8"] is None:
            log("  → Φ_8 NOT seen in (n−p) within available range — "
                "Wenzl annihilator possibly suppressed by isospin coupling")
        elif np_pair["M_first_phi8"] != 7:
            log(f"  → Φ_8 appears at M={np_pair['M_first_phi8']} ≠ 7 — "
                "isospin-doublet pair has DIFFERENT depth than other pairs")

    builder.add_data("cross_pair_summary", {
        "per_pair": pair_table,
        "M_first_phi8_set": sorted(m_first_set),
        "pairs_without_phi8_in_range": pairs_no_phi8,
        "universal_phi8_at_M7_across_10_pairs": universal,
        "n_minus_p_special_case": np_summary,
    })

    # ─── Verdict ───────────────────────────────────────────────────────
    if universal:
        verdict = "CONFIRMED: M_first_Φ_8 = 7 universally across all 10 pairs"
    elif (len(m_first_set) == 1
          and not pairs_no_phi8):
        verdict = (
            f"PARTIAL: M_first_Φ_8 universal at {sorted(m_first_set)[0]} (NOT 7)"
        )
    elif pairs_no_phi8:
        verdict = (
            f"PARTIAL: {len(pairs - set(pairs_no_phi8))}/10 pairs hit "
            f"M_first_Φ_8 ∈ {sorted(m_first_set)}; pairs without Φ_8 in range: "
            f"{pairs_no_phi8} (M_common may be < 7)"
        )
    else:
        verdict = (
            f"PAIR-DEPENDENT: M_first_Φ_8 ∈ {sorted(m_first_set)} "
            f"varies across pairs"
        )
    log(f"\n  VERDICT: {verdict}")
    builder.add_data("verdict", verdict)

    builder.add_assertion(
        "phi8_universal_M7_across_all_10_pairs",
        computed=int(universal),
        expected=1,
        tolerance=0,
        source="PR #1625 Track 1 mechanism doc; level-2 SU(2) Wenzl annihilator.",
    )
    builder.save()
    log("\n  ✓ Witness saved: qbeta-habiro-all-10-pairs-phi8-universality.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
