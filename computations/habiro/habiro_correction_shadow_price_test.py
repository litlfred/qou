#!/usr/bin/env python3
"""Shadow-price test: are the Habiro correction coefficients LP/SDP duals?

The proton Habiro bridge has correction (1+ℏ²)(1−ℏ²/30)(1+ℏ²/1260).
We established R_alg(q) = bridge/Plancherel is ALGEBRAIC, but the
correction S = R_alg/(Vol/ℏ²) is transcendental.

This script tests whether the operator-selection LP/SDP shadow prices
y* for the proton at H₉ (A=3) reproduce the correction structure.

For a block-diagonal Frobenius Gram, the SDP M(x)=diag(Gx)≽0 is
provably LP-equivalent, so we use the LP solver and the duals ARE
the SDP shadow prices.

Test: do the shadow prices y*[λ] — or the active set, or a simple
combination — match the correction coefficients 1/30, 1/1260, or the
algebraic bridge R_alg?
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
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

import numpy as np
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402
except ImportError:
    from qou_substrate.constants import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402


def main():
    _t0 = time.perf_counter()
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    hbar_q = (q - 1) / q
    eps = hbar_q**2
    n = 9
    p_n = 30

    # Load the A=3 H₉ chi-cache (proton at H₉ = A=3)
    cache = record_upstream(_pb.witness_path("chi-tritium-h9-at-q0-50dps.witness.json", HERE), _UPSTREAM_RECORDS)
    data = cache.get("data", cache)
    by_part = data["by_partition"]
    # Keep substrate values at mpmath precision (flagged by
    # compute_no_mpf_to_float_cast — dropping the outer float()).
    tr_M = mp.mpf(data["tr_M_at_q0"])

    partitions = []
    y_lams = []
    chi_lams = []
    contribs = []
    for row in by_part:
        partitions.append(tuple(row["partition"]))
        y_lams.append(mp.mpf(row["y_lambda"]))
        chi_lams.append(mp.mpf(row["chi_lambda"]))
        contribs.append(mp.mpf(row["contribution"]))

    d = len(partitions)
    print("=" * 70)
    print("  Shadow-price test for Habiro correction (proton @ H₉, A=3)")
    print("=" * 70)
    print()
    print(f"  Partitions: {d}  (p(9) = {p_n})")
    print(f"  tr_M(A=3) = {mp.nstr(tr_M, 11)}")  # display only; mpf has no %f
    print()

    # ---------------------------------------------------------------
    # Operator-selection LP (= diagonal SDP):
    #   min Σ_λ |contrib_λ| x_λ   s.t. Σ contrib_λ x_λ = tr_M, Gx ≥ 0
    # Gram G = diag(|contrib|) → SDP M(x)=diag(Gx)≽0 ≡ LP.
    # ---------------------------------------------------------------
    t_vec = np.array([abs(c) for c in contribs], dtype=float)
    G = np.diag([abs(c) for c in contribs])
    n_target = tr_M

    # Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
    # whether the Rust binary happens to be built, so the same script
    # yields different numbers on different boxes. QOU_REQUIRE_CLARABEL=1
    # makes a missing binary an error rather than a changed answer.
    # Bean `qou/ftuv`.
    result = solve_operator_selection_lp(t_vec, G, n_target, backend="clarabel")
    rd = result.to_dict()

    y_star = rd["y_star"]
    y0_star = rd["y0_star"]
    active = rd.get("active_set", rd.get("active_constraints", []))

    print(f"  LP solved. Duality gap: {float(rd['duality_gap']):.2e}")
    print(f"  y0* (net shadow price): {float(y0_star):.10f}")
    print(f"  Active blocks: {len(active)} of {d}")
    print()

    # Print active blocks with shadow prices
    print(f"  {'Partition':<18s} {'y*[λ]':>14s} {'χ_λ':>10s} {'contrib':>12s}")
    print(f"  {'─'*18} {'─'*14} {'─'*10} {'─'*12}")
    for i in active:
        print(f"  {str(list(partitions[i])):<18s} {float(y_star[i]):>14.6f} "
              f"{float(chi_lams[i]):>10.4f} {float(contribs[i]):>12.6f}")
    print()

    # ---------------------------------------------------------------
    # Test: do shadow prices relate to the correction coefficients?
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  Comparison with Habiro correction coefficients")
    print("-" * 70)
    print()

    # The correction is S = (1+ℏ²)(1−ℏ²/30)(1+ℏ²/1260).
    # The shadow prices y* are the LP duals. Do any match 1/30, 1/1260?

    sum_y = sum(y_star)
    n_active = len(active)
    print(f"  Number of active blocks: {n_active}")
    print(f"  Σ y*[λ] = {float(sum_y):.10f}")
    print(f"  y0* = {float(y0_star):.10f}")
    print()
    print(f"  Correction targets:")
    print(f"    1/p(n) = 1/30 = {float(1/30):.10f}")
    print(f"    1/1260 = {float(1/1260):.10f}")
    print(f"    ℏ² = {float(eps):.10f}")
    print()

    # Check if the number of active blocks = 30 (all) or a subset
    if n_active == p_n:
        print(f"  ✓ ALL {p_n} blocks active → uniform block-averaging")
        print(f"    This WOULD support the 1/p(n) = 1/30 interpretation.")
    else:
        print(f"  ✗ Only {n_active}/{p_n} blocks active → NOT uniform.")
        print(f"    The 1/30 (block-averaging) interpretation is NOT")
        print(f"    supported by the shadow-price active set.")
    print()

    # Check if any shadow price or combination matches 1/30, 1/1260
    print(f"  Shadow-price value scan (looking for 1/30, 1/1260):")
    matches = []
    for i, y in enumerate(y_star):
        if abs(y) < 1e-12:
            continue
        for target, name in [(1/30, "1/30"), (1/1260, "1/1260"),
                             (float(eps), "ℏ²"), (1/p_n**2, "1/p(n)²")]:
            if abs(y - target) / max(target, 1e-12) < 0.01:
                matches.append((partitions[i], name, y))
    if matches:
        for lam, name, y in matches:
            print(f"    λ={list(lam)}: y*={float(y):.6f} ≈ {name}")
    else:
        print(f"    No shadow price matches 1/30, 1/1260, ℏ², or 1/p(n)².")
    print()

    # ---------------------------------------------------------------
    # The decisive test: R_alg is algebraic. Shadow prices are
    # algebraic (rational in trace data). Can R_alg = f(y*)?
    # But R_alg ≈ 208.73 and involves the proton Habiro coefficients,
    # NOT the tritium chi-cache. The shadow prices here are for the
    # A=3 mass selection, a DIFFERENT construction.
    # ---------------------------------------------------------------
    print("=" * 70)
    print("  VERDICT")
    print("=" * 70)
    print()
    print(f"  The operator-selection LP/SDP for the proton at H₉ selects")
    print(f"  {n_active} active Wedderburn blocks with shadow prices y*.")
    print()
    if n_active == p_n:
        verdict = "block-averaging-consistent"
        print(f"  All {p_n} blocks active — the 1/30 = 1/p(n) factor is")
        print(f"  CONSISTENT with uniform block-averaging (shadow-price-")
        print(f"  motivated), though the exact coefficient still requires")
        print(f"  the transcendental Vol(4₁) and remains a numerical fit.")
    else:
        verdict = "shadow-price-NOT-the-source"
        print(f"  Only {n_active} blocks active — the correction does NOT")
        print(f"  arise from a uniform shadow-price average. The 1/30 and")
        print(f"  1/1260 are NUMERICAL FITS, not LP/SDP shadow prices.")
    print()
    print(f"  Definitive reason: R_alg(q) is algebraic but S = R_alg/(Vol/ℏ²)")
    print(f"  inherits transcendental Vol(4₁). Shadow prices are algebraic,")
    print(f"  so they CANNOT equal S's coefficients. The most they could")
    print(f"  explain is the algebraic bridge R_alg itself.")
    print()

    # Build witness with FULL LP dual fields (per AGENTS.md LP/SDP rule)
    w = WitnessBuilder("habiro-correction-shadow-price-test", engine="python",
                       start_time=_t0)
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Tests whether the proton Habiro correction coefficients (1/30, "
        "1/1260) are LP/SDP shadow prices. Operator-selection LP at H₉ "
        f"(A=3) selects {n_active}/{p_n} active blocks. "
        f"Verdict: {verdict}."
    )
    w.set_audit_only("docs/audits/2026-05-28-habiro-product-correction-7ppm.md")
    # Required LP-dual fields
    # THE SHADOW PRICES ARE THE DELIVERABLE, so they ship with their full
    # precision, not just the f64 view. `solve_operator_selection_lp` already
    # returns a 50-dps companion for every dual it computes; reading only
    # `rd["y_star"]` and handing that to `add_data` threw those digits away at
    # the last step and put 34 raw float64 fields into the witness — for
    # quantities whose whole argument is that they are ALGEBRAIC and can be
    # compared against a transcendental. Bean `qou/ftuv`.
    #
    # `backend` rides along because a clarabel answer and a scipy-HiGHS answer
    # to this LP are not interchangeable, and a witness that does not say
    # which one produced it cannot be re-checked.
    w.add_data("y0_star", y0_star)
    w.add_data("y_star", y_star)
    for _k in ("y0_star_str", "y_star_str", "primal_obj_str",
               "dual_obj_str", "duality_gap_str"):
        _v = rd.get(_k)
        if _v is not None:
            w.add_data(_k, _v)
    if rd.get("backend") is not None:
        w.add_data("backend", rd["backend"])
    w.add_data("active_set", active)
    w.add_data("primal_obj", rd["primal_obj"])
    w.add_data("dual_obj", rd["dual_obj"])
    w.add_data("duality_gap", rd["duality_gap"])
    w.add_data("n_active", n_active)
    w.add_data("p_n", p_n)
    w.add_data("verdict", verdict)
    w.add_data("partitions", [list(p) for p in partitions])

    w.add_assertion("strong_duality",
                    computed=1 if rd["duality_gap"] < 1e-6 else 0,
                    expected=1, tolerance=0,
                    source="LP strong duality gap < 1e-6")
    w.add_assertion("shadow_price_verdict_recorded",
                    computed=1, expected=1, tolerance=0,
                    source=f"verdict={verdict}, {n_active}/{p_n} active")

    print(f"  Witness: {w.save()}")


if __name__ == "__main__":
    main()
