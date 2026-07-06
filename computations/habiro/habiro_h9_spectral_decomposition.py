#!/usr/bin/env python3
"""H₉ spectral decomposition of the Habiro normalization residual.

The Habiro normalization bridge is:
    Habiro ≈ tr_M × (n!/[n]_q!) × (Vol(4₁)/ℏ²) × (1 + ℏ²)

at 319 ppm (n=9, proton). The remaining residual lives at ℏ⁴ order
with coefficient c₄ ≈ −3.31.

This script decomposes the residual across all 30 partitions λ ⊢ 9
using the Wenzl y_λ weights. The Markov trace is:
    tr_M = Σ_λ y_λ · χ_λ(w)

The Habiro expansion sees the FULL representation theory while the
Markov trace only sees the y_λ-weighted characters. The difference
between Habiro and tr_M × (Plancherel × Vol/ℏ²) must be traceable
to the per-partition content sums c(λ) = Σ_{(i,j)∈λ} (j-i).

Key structural hypothesis: the ℏ⁴ correction is
    c₄ = Σ_λ y_λ · f(c(λ), dim_q(λ))
for some universal function f determined by the H₉ representation
theory — not a braid-specific fit.
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
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from partition_utils import hook_lengths, conjugate_partition  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402
except ImportError:
    from qou_substrate.constants import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402


def content_sum(shape):
    """Content sum c(λ) = Σ_{(i,j)∈λ} (j - i)."""
    s = 0
    for i, row_len in enumerate(shape):
        for j in range(row_len):
            s += (j - i)
    return s


def q_factorial(n, q):
    """[n]_q! = Π_{k=1}^{n} [k]_q where [k]_q = (q^k - q^{-k})/(q - q^{-1})."""
    result = mp.mpf(1)
    h = q - 1/q
    for k in range(1, n + 1):
        qk = (q**k - q**(-k)) / h
        result *= qk
    return result


def q_integer(k, q):
    """[k]_q = (q^k - q^{-k}) / (q - q^{-1})."""
    return (q**k - q**(-k)) / (q - 1/q)


def q_dim(shape, q):
    """q-dimension dim_q(V_λ) = [n]_q! / Π_{cells} [h(i,j)]_q."""
    n = sum(shape)
    numer = q_factorial(n, q)
    hooks = hook_lengths(tuple(shape))
    denom = mp.mpf(1)
    for hk in hooks:
        denom *= q_integer(hk, q)
    return numer / denom


def classical_dim(shape):
    """Classical dimension dim(V_λ) = n! / Π_{cells} h(i,j)."""
    import math
    n = sum(shape)
    hooks = hook_lengths(tuple(shape))
    denom = 1
    for hk in hooks:
        denom *= hk
    return math.factorial(n) // denom


def main():
    import time
    _t0 = time.perf_counter()
    set_compute_dps()
    mp.mp.dps = 50
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1/q
    hbar_q = (q - 1) / q
    hbar_sq = hbar_q**2

    vol_41 = vol_4_1_at(50)
    n = 9

    # Load Wenzl y_λ weights
    wenzl_file = _pb.witness_path("wenzl-y-lambda-h9.witness.json", HERE)
    with open(wenzl_file) as f:
        wenzl_data = json.load(f)

    partitions_data = wenzl_data["data"]["per_partition"]

    # Known values
    hab_sum = mp.mpf("136.0712063634817616514048508169837773395")
    tr_M = mp.mpf("1.065306228613167059365284546431372557650")
    plancherel_ratio = mp.factorial(n) / q_factorial(n, q)
    vol_over_hsq = vol_41 / hbar_sq

    # The bridge prediction at each order
    pred_0 = tr_M * plancherel_ratio * vol_over_hsq  # 0th order (9495 ppm)
    pred_1 = pred_0 * (1 + hbar_sq)                   # 1st correction (319 ppm)

    residual_0 = hab_sum / pred_0 - 1
    residual_1 = hab_sum / pred_1 - 1

    print("=" * 70)
    print("  H₉ Spectral Decomposition of Habiro Normalization Residual")
    print("=" * 70)
    print()
    print(f"  Habiro sum:          {mp.nstr(hab_sum, 20)}")
    print(f"  tr_M (proton H₉):   {mp.nstr(tr_M, 20)}")
    print(f"  n!/[n]_q!:           {mp.nstr(plancherel_ratio, 15)}")
    print(f"  Vol(4₁)/ℏ²:         {mp.nstr(vol_over_hsq, 15)}")
    print(f"  ℏ² = ((q-1)/q)²:    {mp.nstr(hbar_sq, 15)}")
    print(f"  h = q - q⁻¹:        {mp.nstr(h, 15)}")
    print()
    print(f"  Pred (no corr):      {mp.nstr(pred_0, 15)}")
    print(f"  Residual₀:          {mp.nstr(residual_0, 10)} ({float(residual_0)*1e6:.1f} ppm)")
    print(f"  Pred (1+ℏ²):        {mp.nstr(pred_1, 15)}")
    print(f"  Residual₁:          {mp.nstr(residual_1, 10)} ({float(residual_1)*1e6:.1f} ppm)")
    print()

    # ---------------------------------------------------------------
    # Per-partition decomposition
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  Per-partition spectral decomposition")
    print("-" * 70)
    print()

    total_y = mp.mpf(0)
    total_y_c = mp.mpf(0)
    total_y_csq = mp.mpf(0)
    total_y_c3 = mp.mpf(0)
    total_y_c4 = mp.mpf(0)
    total_y_dim_q = mp.mpf(0)
    total_y_dim_cl = mp.mpf(0)

    partition_records = []

    for entry in partitions_data:
        lam = tuple(entry["partition"])
        y_lam = mp.mpf(entry["y_lambda"])
        c_lam = content_sum(lam)
        dim_q_lam = q_dim(lam, q)
        dim_cl_lam = classical_dim(lam)
        conj = conjugate_partition(lam)
        is_self_conj = (lam == conj)

        total_y += y_lam
        total_y_c += y_lam * c_lam
        total_y_csq += y_lam * c_lam**2
        total_y_c3 += y_lam * c_lam**3
        total_y_c4 += y_lam * c_lam**4
        total_y_dim_q += y_lam * dim_q_lam
        total_y_dim_cl += y_lam * dim_cl_lam

        partition_records.append({
            "partition": list(lam),
            "y_lambda": str(mp.nstr(y_lam, 20)),
            "content_sum": c_lam,
            "dim_q": str(mp.nstr(dim_q_lam, 15)),
            "dim_classical": dim_cl_lam,
            "self_conjugate": is_self_conj,
            "y_times_c": str(mp.nstr(y_lam * c_lam, 15)),
            "y_times_c_sq": str(mp.nstr(y_lam * c_lam**2, 15)),
        })

    # Print top partitions by |y_λ|
    sorted_parts = sorted(partition_records,
                          key=lambda r: abs(float(r["y_lambda"])),
                          reverse=True)

    print(f"  {'Partition':<20s} {'y_λ':>14s} {'c(λ)':>6s} {'dim_q':>10s} {'dim_cl':>7s} {'SC':>3s}")
    print(f"  {'─'*20} {'─'*14} {'─'*6} {'─'*10} {'─'*7} {'─'*3}")
    for r in sorted_parts[:15]:
        sc = "✓" if r["self_conjugate"] else ""
        print(f"  {str(r['partition']):<20s} {float(r['y_lambda']):>14.8f} {r['content_sum']:>6d} "
              f"{float(r['dim_q']):>10.2f} {r['dim_classical']:>7d} {sc:>3s}")
    print(f"  ... ({len(sorted_parts)} total partitions)")
    print()

    # ---------------------------------------------------------------
    # Moment analysis: Σ y_λ c(λ)^k
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  Moment analysis: M_k = Σ_λ y_λ · c(λ)^k")
    print("-" * 70)
    print()
    print(f"  M₀ = Σ y_λ           = {mp.nstr(total_y, 15)}")
    print(f"  M₁ = Σ y_λ c(λ)      = {mp.nstr(total_y_c, 15)}")
    print(f"  M₂ = Σ y_λ c(λ)²     = {mp.nstr(total_y_csq, 15)}")
    print(f"  M₃ = Σ y_λ c(λ)³     = {mp.nstr(total_y_c3, 15)}")
    print(f"  M₄ = Σ y_λ c(λ)⁴     = {mp.nstr(total_y_c4, 15)}")
    print()

    # The full twist Ω_n acts on V_λ by q^{2c(λ)}, so these moments
    # appear in the Taylor expansion of <Ω_n>_tr = Σ y_λ q^{2c(λ)}.
    # At q = e^{h/2}, q^{2c} = e^{h·c}, so the moments are:
    #   <Ω>_tr = M₀ + h·M₁ + h²/2·M₂ + h³/6·M₃ + h⁴/24·M₄ + ...

    full_twist_trace = mp.mpf(0)
    for entry in partitions_data:
        lam = tuple(entry["partition"])
        y_lam = mp.mpf(entry["y_lambda"])
        c_lam = content_sum(lam)
        full_twist_trace += y_lam * q**(2 * c_lam)

    print(f"  Full-twist trace Σ y_λ q^{{2c(λ)}} = {mp.nstr(full_twist_trace, 20)}")
    print(f"  tr_M (direct) =                      {mp.nstr(tr_M, 20)}")
    print(f"  Full-twist / tr_M =                  {mp.nstr(full_twist_trace / tr_M, 15)}")
    print()

    # ---------------------------------------------------------------
    # Key ratio: dim_q-weighted vs Plancherel-weighted sums
    # ---------------------------------------------------------------
    # The Plancherel ratio n!/[n]_q! can be rewritten per-partition:
    #   n!/[n]_q! = Σ_λ (dim_cl(λ)² / n!) × ([n]_q! / dim_q(λ)) / Σ_λ (y_λ dim_q(λ) / [n]_q!)
    # ... but simpler: the Plancherel measure is dim_cl² / n!
    # while the Wenzl measure is y_λ ∝ dim_q · (something).

    print("-" * 70)
    print("  Plancherel vs Wenzl comparison")
    print("-" * 70)
    print()
    print(f"  Σ y_λ · dim_q(λ)     = {mp.nstr(total_y_dim_q, 15)}")
    print(f"  Σ y_λ · dim_cl(λ)    = {mp.nstr(total_y_dim_cl, 15)}")
    print(f"  [n]_q! (n=9)         = {mp.nstr(q_factorial(n, q), 15)}")
    print(f"  n! = 9!              = {mp.factorial(n)}")
    print()

    # ---------------------------------------------------------------
    # Try to identify the ℏ⁴ coefficient structurally
    # ---------------------------------------------------------------
    # The residual after (1+ℏ²) is:
    #   R = Habiro/(pred₀·(1+ℏ²)) - 1 ≈ c₄·ℏ⁴ + O(ℏ⁶)
    #   c₄ = R / ℏ⁴

    c4_empirical = residual_1 / hbar_sq**2
    print("-" * 70)
    print("  ℏ⁴ coefficient identification")
    print("-" * 70)
    print()
    print(f"  c₄ = residual / ℏ⁴ = {mp.nstr(c4_empirical, 12)}")
    print()

    # Candidate structural expressions for c₄:
    candidates = [
        ("−M₂/M₀", -total_y_csq / total_y),
        ("−M₂/(2·M₀)", -total_y_csq / (2 * total_y)),
        ("−M₂·ℏ²/M₀ (redundant?)", -total_y_csq * hbar_sq / total_y),
        ("M₁²/M₀² − M₂/M₀", (total_y_c/total_y)**2 - total_y_csq/total_y),
        ("−(M₂ − M₁²/M₀)/M₀ (variance)", -(total_y_csq - total_y_c**2/total_y)/total_y),
        ("[n]_q/[n-1]_q − 1", q_integer(n, q)/q_integer(n-1, q) - 1),
        ("−n(n-1)/12", mp.mpf(-n*(n-1))/12),
        ("−(n²-1)/12", mp.mpf(-(n**2-1))/12),
        ("c₄ itself (decimal)", c4_empirical),
    ]

    print(f"  {'Candidate expression':<35s} {'Value':>15s} {'c₄−cand':>12s}")
    print(f"  {'─'*35} {'─'*15} {'─'*12}")
    best_match = None
    best_miss = mp.mpf(1e10)
    for name, val in candidates:
        miss = float(c4_empirical - val)
        if abs(miss) < abs(float(best_miss)):
            best_miss = miss
            best_match = name
        print(f"  {name:<35s} {mp.nstr(val, 10):>15s} {miss:>12.6f}")

    print()
    print(f"  Best match: {best_match}  (miss = {float(best_miss):.6f})")
    print()

    # ---------------------------------------------------------------
    # Try the Habiro / full-twist connection
    # ---------------------------------------------------------------
    # If Habiro_sum = tr_M × (n!/[n]_q!) × (Vol/ℏ²) × Σ_{k≥0} c_k ℏ^{2k}
    # Then the correction series is the ratio:
    #   S = Habiro / (tr_M × Plancherel × Vol/ℏ²)

    S = hab_sum / pred_0
    print("-" * 70)
    print("  Correction series S = Habiro / prediction₀")
    print("-" * 70)
    print()
    print(f"  S = {mp.nstr(S, 20)}")
    print(f"  S - 1 = {mp.nstr(S - 1, 15)} (= c₂·ℏ² + c₄·ℏ⁴ + ...)")
    print()

    # Extract c₂ coefficient
    c2 = (S - 1) / hbar_sq
    print(f"  c₂ = (S-1)/ℏ² = {mp.nstr(c2, 15)}")
    print(f"  c₂ ≈ 1?  miss = {float(c2 - 1):.8f}")
    print()

    # After subtracting 1·ℏ²: residual at ℏ⁴
    S2 = S - 1 - hbar_sq
    c4_from_series = S2 / hbar_sq**2
    print(f"  After subtracting ℏ²: S₂ = {mp.nstr(S2, 15)}")
    print(f"  c₄ = S₂/ℏ⁴ = {mp.nstr(c4_from_series, 12)}")
    print()

    # Try ℏ⁴ correction with c₄ = -n(n-1)/12
    c4_try = -mp.mpf(n * (n - 1)) / 12
    pred_2 = pred_0 * (1 + hbar_sq + c4_try * hbar_sq**2)
    residual_2 = hab_sum / pred_2 - 1
    print(f"  Try c₄ = −n(n−1)/12 = {mp.nstr(c4_try, 10)}")
    print(f"  Prediction₂ = pred₀ × (1 + ℏ² − 6ℏ⁴)")
    print(f"  Residual₂ = {mp.nstr(residual_2, 10)} ({float(residual_2)*1e6:.1f} ppm)")
    print()

    # Try c₄ = −(n²−1)/12
    c4_try2 = -mp.mpf(n**2 - 1) / 12
    pred_3 = pred_0 * (1 + hbar_sq + c4_try2 * hbar_sq**2)
    residual_3 = hab_sum / pred_3 - 1
    print(f"  Try c₄ = −(n²−1)/12 = {mp.nstr(c4_try2, 10)}")
    print(f"  Residual₃ = {mp.nstr(residual_3, 10)} ({float(residual_3)*1e6:.1f} ppm)")
    print()

    # Try c₄ from variance of content sum
    var_c = (total_y_csq - total_y_c**2 / total_y) / total_y
    c4_var = -var_c
    pred_4 = pred_0 * (1 + hbar_sq + c4_var * hbar_sq**2)
    residual_4 = hab_sum / pred_4 - 1
    print(f"  Try c₄ = −Var(c) = {mp.nstr(c4_var, 10)}")
    print(f"  Residual₄ = {mp.nstr(residual_4, 10)} ({float(residual_4)*1e6:.1f} ppm)")
    print()

    # Try ℏ²·c₂ pattern: (1+ℏ²)² = 1 + 2ℏ² + ℏ⁴
    pred_sq = pred_0 * (1 + hbar_sq)**2
    residual_sq = hab_sum / pred_sq - 1
    print(f"  Try (1+ℏ²)²: c₂=2, c₄=1")
    print(f"  Residual_sq = {mp.nstr(residual_sq, 10)} ({float(residual_sq)*1e6:.1f} ppm)")
    print()

    # Try 1/(1-ℏ²) = 1 + ℏ² + ℏ⁴ + ℏ⁶ + ...
    pred_geom = pred_0 / (1 - hbar_sq)
    residual_geom = hab_sum / pred_geom - 1
    print(f"  Try 1/(1−ℏ²): geometric series")
    print(f"  Residual_geom = {mp.nstr(residual_geom, 10)} ({float(residual_geom)*1e6:.1f} ppm)")
    print()

    # Try 1/(1-ℏ²)^(1/2)
    pred_sqrt_geom = pred_0 / mp.sqrt(1 - hbar_sq)
    residual_sqrt_geom = hab_sum / pred_sqrt_geom - 1
    print(f"  Try 1/√(1−ℏ²):")
    print(f"  Residual_sqrt = {mp.nstr(residual_sqrt_geom, 10)} ({float(residual_sqrt_geom)*1e6:.1f} ppm)")
    print()

    # Try [n]_q / n (the q-integer correction for n=9)
    qn_over_n = q_integer(n, q) / n
    pred_qn = pred_0 * qn_over_n
    residual_qn = hab_sum / pred_qn - 1
    print(f"  Try [n]_q/n = [9]_q/9 = {mp.nstr(qn_over_n, 12)}")
    print(f"  Residual_qn = {mp.nstr(residual_qn, 10)} ({float(residual_qn)*1e6:.1f} ppm)")
    print()

    # ---------------------------------------------------------------
    # The big test: q^{c(proton_partition)} correction
    # ---------------------------------------------------------------
    # The proton dominant partition at H₉ should be (6,3) or (5,3,1)
    # or similar. If c₄ relates to the content sum of the dominant
    # partition...
    print("-" * 70)
    print("  Dominant partition analysis")
    print("-" * 70)
    print()

    for r in sorted_parts[:5]:
        lam = tuple(r["partition"])
        c = r["content_sum"]
        y = float(r["y_lambda"])
        frac = y / float(total_y)
        print(f"  λ={str(list(lam)):<16s}  y_λ={y:>12.8f}  c(λ)={c:>4d}  "
              f"y/Σy = {frac:.4f}  q^{{2c}} = {float(q**(2*c)):>12.4f}")

    print()

    # ---------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------
    print("=" * 70)
    print("  SUMMARY")
    print("=" * 70)
    print()
    print(f"  Habiro normalization bridge: 3-level correction ladder")
    print(f"")
    print(f"  Level 0: tr_M × (n!/[n]_q!) × (Vol/ℏ²)           → {float(residual_0)*1e6:>8.1f} ppm")
    print(f"  Level 1: × (1 + ℏ²)                               → {float(residual_1)*1e6:>8.1f} ppm")
    print(f"  Level 2a: × (1 + ℏ²)²                             → {float(residual_sq)*1e6:>8.1f} ppm")
    print(f"  Level 2b: × 1/(1−ℏ²)                              → {float(residual_geom)*1e6:>8.1f} ppm")
    print(f"  Level 2c: × 1/√(1−ℏ²)                             → {float(residual_sqrt_geom)*1e6:>8.1f} ppm")
    print(f"  Level 2d: × [9]_q/9                                → {float(residual_qn)*1e6:>8.1f} ppm")
    print(f"  Level 2e: × (1+ℏ²−n(n−1)/12·ℏ⁴)                  → {float(residual_2)*1e6:>8.1f} ppm")
    print(f"  Level 2f: × (1+ℏ²−Var(c)·ℏ⁴)                     → {float(residual_4)*1e6:>8.1f} ppm")
    print()
    print(f"  Empirical c₄ = {mp.nstr(c4_from_series, 12)}")
    print(f"  Target: find structural c₄ that closes to < 50 ppm")
    print()

    w = WitnessBuilder("habiro-h9-spectral-decomposition", engine="mpmath")
    w.set_description(
        "H₉ spectral decomposition of Habiro normalization residual (319 ppm). "
        "Decomposes per-partition content sums, moments M_k = Σ y_λ c(λ)^k, "
        "and tests structural candidates for the ℏ⁴ coefficient c₄ ≈ −3.31."
    )
    w.set_audit_only("docs/audits/2026-05-28-habiro-product-correction-7ppm.md")
    w._start_time = _t0
    w.add_data("n", 9)
    w.add_data("num_partitions", 30)
    w.add_data("residual_0_ppm", float(residual_0) * 1e6)
    w.add_data("residual_1_ppm", float(residual_1) * 1e6)
    w.add_data("c4_empirical", str(mp.nstr(c4_from_series, 15)))
    w.add_data("moments", {
        "M0": str(mp.nstr(total_y, 15)),
        "M1": str(mp.nstr(total_y_c, 15)),
        "M2": str(mp.nstr(total_y_csq, 15)),
        "M3": str(mp.nstr(total_y_c3, 15)),
        "M4": str(mp.nstr(total_y_c4, 15)),
    })
    w.add_data("correction_ladder", {
        "level_0_ppm": float(residual_0) * 1e6,
        "level_1_1_plus_hsq_ppm": float(residual_1) * 1e6,
        "level_2a_1_plus_hsq_sq_ppm": float(residual_sq) * 1e6,
        "level_2b_geom_series_ppm": float(residual_geom) * 1e6,
        "level_2c_sqrt_geom_ppm": float(residual_sqrt_geom) * 1e6,
        "level_2d_q9_over_9_ppm": float(residual_qn) * 1e6,
    })
    w.add_data("partition_records", partition_records[:10])

    w.add_assertion("residual_0_is_9500ppm",
                    computed=1 if abs(float(residual_0)*1e6 - 9495) < 100 else 0,
                    expected=1, tolerance=0,
                    source="Habiro/pred₀ − 1 ≈ 9495 ppm")
    w.add_assertion("residual_1_is_319ppm",
                    computed=1 if abs(abs(float(residual_1)*1e6) - 319) < 50 else 0,
                    expected=1, tolerance=0,
                    source="|Habiro/pred₁ − 1| ≈ 319 ppm after (1+ℏ²)")

    print(f"\n  Witness: {w.save()}")


if __name__ == "__main__":
    main()
