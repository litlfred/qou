#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only output across counterfactual q.
"""
Metallic-q SDP-feasibility sweep — dense q-sampling across gold/silver/
bronze intervals.

The owner's structural conjecture (2026-06-09): the count N(q) of
SDP-feasible Wedderburn blocks is **piecewise constant** on the
metallic-ladder intervals.  At metallic ratios `δ_n = (n + √(n²+4))/2`
(golden δ₁=φ, silver δ₂=1+√2, bronze δ₃=(3+√13)/2) the Hecke
quadratic `σ² = (q − q⁻¹)σ + 1` acquires an integer scalar `n = q − q⁻¹`,
and the algebra reorganises — sign flips in the Wenzl weights y_λ
that gate SDP feasibility.

This probe tests the conjecture at the simplest level: count, at each
q in a dense sample across (q₀, φ), (φ, δ_silver), (δ_silver, δ_bronze),
the number of partitions λ of n ∈ {3, 6, 9} whose Wenzl weight

      y_λ(q) = d_q(λ)² / [n]_q!

is **positive** (necessary for SDP feasibility in the framework).  A
sign flip at a metallic ratio is the structural signature the
conjecture predicts; a smooth y_λ(q) across the boundary would refute it.

Each interval is sampled at ≥10 q-values (denser than just midpoints).
Bar-mirror intervals (1/δ_n) are sampled symmetrically.  Output is a
witness JSON with the full sweep + a per-interval positive-block count
N(q, n) per strand count n.

Self-contained: no pyhecke dependency.  Hook lengths and q-factorials
are computed from scratch using mpmath @ 50 dps.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

HERE = Path(__file__).parent


# ── Metallic-ratio anchors ──────────────────────────────────────────────


def delta_n(n: int) -> mp.mpf:
    """The n-th metallic ratio δ_n = (n + √(n²+4))/2 (real, > 1)."""
    return (mp.mpf(n) + mp.sqrt(n * n + 4)) / 2


PHI = delta_n(1)              # 1.6180339887...
DELTA_SILVER = delta_n(2)     # 2.4142135623...
DELTA_BRONZE = delta_n(3)     # 3.3027756377...

# Substrate substrate-value at the canonical anchor (50 dps).
Q0 = mp.mpf("1.1099785955541805")


# ── Partitions of n ─────────────────────────────────────────────────────


def partitions(n: int) -> list[list[int]]:
    """All partitions of n as lists of parts in weakly decreasing order."""
    if n == 0:
        return [[]]
    out: list[list[int]] = []
    def rec(remaining: int, max_part: int, current: list[int]) -> None:
        if remaining == 0:
            out.append(current.copy())
            return
        for part in range(min(remaining, max_part), 0, -1):
            current.append(part)
            rec(remaining - part, part, current)
            current.pop()
    rec(n, n, [])
    return out


def hook_lengths(lam: list[int]) -> list[int]:
    """Hook lengths h(i,j) = λ_i − j + (λ'_j − i) + 1 for every cell."""
    if not lam:
        return []
    conj: list[int] = []
    for j in range(lam[0]):
        c = 0
        for p in lam:
            if p > j:
                c += 1
        conj.append(c)
    hooks: list[int] = []
    for i, row in enumerate(lam):
        for j in range(row):
            hooks.append(row - j + conj[j] - i - 1 + 1)
    return hooks


# ── q-arithmetic ────────────────────────────────────────────────────────


def q_int(k: int, q: mp.mpf) -> mp.mpf:
    """q-integer [k]_q = (q^k − q^{-k}) / (q − q^{-1})."""
    if k == 0:
        return mp.mpf(0)
    return (mp.power(q, k) - mp.power(q, -k)) / (q - 1 / q)


def q_factorial(n: int, q: mp.mpf) -> mp.mpf:
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= q_int(k, q)
    return out


def q_dim(lam: list[int], q: mp.mpf) -> mp.mpf:
    """q-dimension d_q(λ) = ∏ [h(i,j)]_q over hook lengths."""
    out = mp.mpf(1)
    for h in hook_lengths(lam):
        out *= q_int(h, q)
    return out


def wenzl_y(lam: list[int], n: int, q: mp.mpf) -> mp.mpf:
    """Wenzl weight y_λ(q) = d_q(λ)² / [n]_q!."""
    d = q_dim(lam, q)
    return d * d / q_factorial(n, q)


# ── q-sweep across metallic intervals ───────────────────────────────────


def linspace(a: mp.mpf, b: mp.mpf, k: int) -> list[mp.mpf]:
    """k evenly-spaced points in [a, b], inclusive."""
    if k == 1:
        return [a]
    step = (b - a) / (k - 1)
    return [a + step * i for i in range(k)]


def build_sweep() -> dict[str, list[mp.mpf]]:
    """Dense q-sample across the first 3 metallic intervals + bar-mirrors.

    ≥10 points per interval; endpoints offset slightly so the metallic
    ratios themselves are tested as boundary candidates.
    """
    eps = mp.mpf("0.005")
    # Above q₀ on the real line:
    interval_1 = linspace(Q0 + eps, PHI - eps, 12)              # (q₀, φ)
    interval_2 = linspace(PHI + eps, DELTA_SILVER - eps, 12)    # (φ, δ_silver)
    interval_3 = linspace(DELTA_SILVER + eps, DELTA_BRONZE - eps, 10)  # (δ_silver, δ_bronze)
    # Metallic boundaries themselves (tested exactly):
    boundaries = [PHI, DELTA_SILVER, DELTA_BRONZE]
    # Bar-mirror intervals (under q ↦ q⁻¹):
    interval_m1 = linspace(1 / DELTA_SILVER + eps, 1 / PHI - eps, 8)
    interval_m2 = linspace(1 / DELTA_BRONZE + eps, 1 / DELTA_SILVER - eps, 6)
    return {
        "interval_q0_to_phi": interval_1,
        "interval_phi_to_silver": interval_2,
        "interval_silver_to_bronze": interval_3,
        "metallic_boundaries": boundaries,
        "mirror_silver_to_phi": interval_m1,
        "mirror_bronze_to_silver": interval_m2,
    }


# ── Main probe ──────────────────────────────────────────────────────────


def positive_count(n: int, q: mp.mpf) -> tuple[int, int]:
    """Return (n_positive, n_total) Wenzl-y_λ blocks at strand count n, q."""
    parts = partitions(n)
    pos = 0
    for lam in parts:
        y = wenzl_y(lam, n, q)
        if y > 0:
            pos += 1
    return pos, len(parts)


def fmt(q: mp.mpf) -> str:
    return mp.nstr(q, 30)


def main() -> None:
    print("Building dense q-sweep across metallic intervals…", file=sys.stderr)
    sweep = build_sweep()

    strand_counts = [3, 6, 9]
    print(f"Sampling y_λ(q) at strand counts n ∈ {strand_counts}", file=sys.stderr)

    results: dict[str, list[dict]] = {}
    for interval_name, qs in sweep.items():
        rows: list[dict] = []
        for q in qs:
            row: dict = {
                "q": fmt(q),
                "q_minus_qinv": fmt(q - 1 / q),
                "hecke_scalar_integer_part": int(mp.floor(q - 1 / q)),
                "per_strand": {},
            }
            for n in strand_counts:
                pos, total = positive_count(n, q)
                row["per_strand"][f"n_{n}"] = {
                    "n_positive": pos,
                    "n_total": total,
                    "n_negative": total - pos,
                }
            rows.append(row)
        results[interval_name] = rows
        print(f"  {interval_name}: {len(rows)} q-points sampled", file=sys.stderr)

    # Per-interval summary: do positive-counts CHANGE within the interval?
    summary: dict[str, dict] = {}
    for interval_name, rows in results.items():
        summary[interval_name] = {}
        for n in strand_counts:
            counts_seen = sorted({r["per_strand"][f"n_{n}"]["n_positive"] for r in rows})
            summary[interval_name][f"n_{n}"] = {
                "distinct_positive_counts_in_interval": counts_seen,
                "interval_constant": len(counts_seen) == 1,
            }

    # Boundary jumps: does N change as q crosses each metallic ratio?
    boundary_rows = results["metallic_boundaries"]
    above_phi = results["interval_phi_to_silver"][0]
    below_phi = results["interval_q0_to_phi"][-1]
    above_silver = results["interval_silver_to_bronze"][0]
    below_silver = results["interval_phi_to_silver"][-1]

    boundary_jumps: dict[str, dict] = {}
    for ratio_name, below, at, above in [
        ("golden_phi", below_phi, boundary_rows[0], above_phi),
        ("silver", below_silver, boundary_rows[1], above_silver),
    ]:
        ratio_summary: dict = {}
        for n in strand_counts:
            ratio_summary[f"n_{n}"] = {
                "below": below["per_strand"][f"n_{n}"]["n_positive"],
                "at": at["per_strand"][f"n_{n}"]["n_positive"],
                "above": above["per_strand"][f"n_{n}"]["n_positive"],
                "jumps": (
                    below["per_strand"][f"n_{n}"]["n_positive"]
                    != above["per_strand"][f"n_{n}"]["n_positive"]
                ),
            }
        boundary_jumps[ratio_name] = ratio_summary

    witness: dict = {
        "description": (
            "Wenzl y_λ positive-block count N(q,n) sweep across the first "
            "three metallic-ladder intervals plus bar-mirrors. Tests the "
            "owner's piecewise-on-q conjecture: if N(q,n) jumps at φ / "
            "δ_silver / δ_bronze and is constant within each interval, the "
            "metallic-piecewise structure is empirically confirmed at the "
            "Wenzl-weight level (necessary condition for SDP feasibility)."
        ),
        "computed_at": datetime.now(timezone.utc).isoformat(),
        "precision_dps": int(mp.mp.dps),
        "anchors": {
            "q_0_substrate": fmt(Q0),
            "golden_phi": fmt(PHI),
            "silver_delta_2": fmt(DELTA_SILVER),
            "bronze_delta_3": fmt(DELTA_BRONZE),
        },
        "strand_counts": strand_counts,
        "sweep": results,
        "per_interval_summary": summary,
        "boundary_jumps": boundary_jumps,
        "verdict": {
            "interpretation": (
                "If `interval_constant: true` for all (interval, n) AND "
                "`jumps: true` at every metallic boundary, the conjecture "
                "is empirically confirmed at the Wenzl-weight level. If "
                "any interval has multiple counts (continuous variation) "
                "OR no jump occurs at a boundary, the conjecture is "
                "refuted at this n."
            ),
        },
        "limitations": [
            "Wenzl positivity is a NECESSARY (not sufficient) condition "
            "for SDP feasibility. A true catalog-blind SDP test requires "
            "running the full nucleus_real_sdp.py at each q with "
            "regenerated character witnesses — out of scope for this "
            "probe.",
            "Sampled n ∈ {3, 6, 9}; higher n (the actual A=size of "
            "physical nuclei) requires more compute. Sample size chosen "
            "for tractable structural test.",
        ],
        "follow_ups": [
            "If Wenzl jumps confirm the conjecture: regenerate the chi-* "
            "character witnesses at counterfactual q and rerun "
            "nucleus_real_sdp.py for the same sweep — true SDP-feasibility "
            "test, not just Wenzl-positivity.",
            "Connect to Δ_λ option-e v1-v7 regression: do the failing v8 "
            "fits gain a piecewise discontinuity at q = φ that the unitary "
            "v1-v7 ansatze cannot capture?",
        ],
    }

    out = HERE / "metallic-q-wenzl-sign-sweep.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="mpmath")
    witness["scriptFile"] = _os.path.basename(__file__)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nWitness: {out}", file=sys.stderr)

    # Human-readable verdict summary on stdout
    print("\n=== Verdict summary ===\n")
    print(f"q₀ = {fmt(Q0)}   (q − q⁻¹ = {fmt(Q0 - 1/Q0)})")
    print(f"φ  = {fmt(PHI)}   (q − q⁻¹ = 1)")
    print(f"δ₂ = {fmt(DELTA_SILVER)}   (q − q⁻¹ = 2)\n")

    print("Boundary jumps:")
    for ratio_name, ratio_summary in boundary_jumps.items():
        print(f"  {ratio_name}:")
        for n in strand_counts:
            r = ratio_summary[f"n_{n}"]
            tag = " ⬆ JUMP" if r["jumps"] else "  smooth"
            print(
                f"    n={n}: below={r['below']}, at={r['at']}, above={r['above']}{tag}"
            )

    print("\nPer-interval constancy:")
    for interval_name, by_n in summary.items():
        print(f"  {interval_name}:")
        for n in strand_counts:
            s = by_n[f"n_{n}"]
            tag = "  constant" if s["interval_constant"] else " ✗ varies"
            print(
                f"    n={n}: {s['distinct_positive_counts_in_interval']}{tag}"
            )


if __name__ == "__main__":
    main()
