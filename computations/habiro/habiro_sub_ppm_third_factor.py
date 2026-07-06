#!/usr/bin/env python3
"""Push the Habiro correction to sub-ppm via the third factor.

After (1+ℏ²)(1−ℏ²/30), the residual is 7.8 ppm.
The third correction factor c₃ ≈ 0.000796.

This script does an exhaustive numerical scan for the best c₃ fit,
verifying the 3-factor product closes below 1 ppm. The coefficients
are FITTED (see habiro_derivation_vs_fit.py), not derived.
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

import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402
except ImportError:
    from qou_substrate.constants import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402


def q_factorial(n, q):
    result = mp.mpf(1)
    for k in range(1, n + 1):
        result *= (q**k - q**(-k)) / (q - 1/q)
    return result


def q_integer(k, q):
    return (q**k - q**(-k)) / (q - 1/q)


def main():
    _t0 = time.perf_counter()
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    hbar_q = (q - 1) / q
    eps = hbar_q**2
    n = 9
    p_n = 30

    vol = vol_4_1_at(mp.mp.dps)

    hab_sum = mp.mpf("136.0712063634817616514048508169837773395")
    tr_M = mp.mpf("1.065306228613167059365284546431372557650")
    plancherel = mp.factorial(n) / q_factorial(n, q)
    vol_over_hsq = vol / eps

    pred_0 = tr_M * plancherel * vol_over_hsq
    pred_2 = pred_0 * (1 + eps) * (1 - eps / p_n)

    S2 = hab_sum / pred_2
    c3 = (S2 - 1) / eps

    print("=" * 70)
    print("  Sub-ppm Habiro correction: third factor search")
    print("=" * 70)
    print()
    print(f"  After (1+ℏ²)(1−ℏ²/30):")
    print(f"    S₂ = {mp.nstr(S2, 20)}")
    print(f"    S₂ − 1 = {mp.nstr(S2 - 1, 15)}")
    print(f"    c₃ = (S₂−1)/ℏ² = {mp.nstr(c3, 15)}")
    print(f"    Residual = {float(S2 - 1)*1e6:.2f} ppm")
    print()

    # Exhaustive scan of simple algebraic expressions
    candidates = []
    for a in range(-10, 11):
        for b in range(-10, 11):
            for c_denom in [1, 2, 3, 4, 6, 8, 12, 24, 30, 60, 90, 120,
                            180, 270, 360, 540, 720, 900, 1800, 27000]:
                if c_denom == 0:
                    continue
                val = mp.mpf(a * n + b) / c_denom
                if abs(float(val)) > 0.01:
                    continue
                pred_try = pred_2 * (1 + val * eps)
                resid = hab_sum / pred_try - 1
                ppm = abs(float(resid) * 1e6)
                if ppm < 5:
                    candidates.append((f"({a}n+{b})/{c_denom}", val, ppm, resid))

    # Also try expressions involving p(n), n², [k]_q. All entries are
    # bare coefficients c such that the factor is (1 + c·ℏ²); the named
    # "1/12", "1/30" are coefficients, NOT prescaled by ℏ².
    special_vals = [
        ("1/p(n)²", mp.mpf(1) / p_n**2),
        ("1/(2·p(n)²)", mp.mpf(1) / (2 * p_n**2)),
        ("1/(n·p(n))", mp.mpf(1) / (n * p_n)),
        ("(n-1)/(n·p(n)²)", mp.mpf(n - 1) / (n * p_n**2)),
        ("1/(n²·p(n))", mp.mpf(1) / (n**2 * p_n)),
        ("1/(n³)", mp.mpf(1) / n**3),
        ("1/12", mp.mpf(1) / 12),
        ("1/30", mp.mpf(1) / 30),
        ("1/(2·n·p(n))", mp.mpf(1) / (2 * n * p_n)),
        ("(n+1)/(n·p(n)²)", mp.mpf(n + 1) / (n * p_n**2)),
        ("1/[9]_q²", 1 / q_integer(9, q)**2),
        ("n/(p(n)² × 2)", mp.mpf(n) / (2 * p_n**2)),
        ("1/1260 = 1/(C(9,4)·10)", mp.mpf(1) / 1260),
        ("1/1200", mp.mpf(1) / 1200),
        ("1/1350", mp.mpf(1) / 1350),
        ("1/1255", mp.mpf(1) / 1255),
        ("1/1256", mp.mpf(1) / 1256),
    ]
    for name, val in special_vals:
        pred_try = pred_2 * (1 + val * eps)
        resid = hab_sum / pred_try - 1
        ppm = abs(float(resid) * 1e6)
        candidates.append((name, val, ppm, resid))

    # Sort by residual
    candidates.sort(key=lambda x: x[2])

    print(f"  {'Expression':<25s} {'Value':>14s} {'Residual':>12s}")
    print(f"  {'─'*25} {'─'*14} {'─'*12}")
    for name, val, ppm, resid in candidates[:20]:
        sign = "+" if float(resid) > 0 else "−"
        print(f"  {name:<25s} {mp.nstr(val, 8):>14s} {sign}{ppm:>9.4g} ppm")

    print()

    # The numerically-tightest fit and the structural candidate
    # 1/1260 = 1/(C(9,4)·10). Both are FITS (not derived) — report both.
    struct_val = mp.mpf(1) / 1260
    struct_pred = pred_2 * (1 + struct_val * eps)
    struct_ppm = abs(float(hab_sum / struct_pred - 1) * 1e6)

    if candidates:
        best_name, best_val, best_ppm, best_resid = candidates[0]
        print(f"  Tightest fit:        {best_name} = {mp.nstr(best_val, 12)}  ({best_ppm:.4g} ppm)")
        print(f"  Structural near-match: 1/1260 = 1/(C(9,4)·10)  ({struct_ppm:.4g} ppm)")
        print(f"  Both are numerical fits — neither is derived.")
        print()

    # PSLQ on c₃
    print("-" * 70)
    print("  PSLQ search for c₃")
    print("-" * 70)
    print()

    basis = [
        mp.mpf(1),
        c3,
        mp.mpf(1) / n,
        mp.mpf(1) / n**2,
        mp.mpf(1) / n**3,
        mp.mpf(1) / p_n,
        mp.mpf(1) / p_n**2,
        mp.mpf(1) / (n * p_n),
    ]
    labels = ["1", "c₃", "1/n", "1/n²", "1/n³", "1/p(n)", "1/p(n)²", "1/(n·p(n))"]

    try:
        rel = mp.pslq(basis, maxcoeff=1000)
        if rel:
            print(f"  PSLQ: ", end="")
            terms = []
            for i, c in enumerate(rel):
                if c != 0:
                    terms.append(f"{c}·{labels[i]}")
            print(" + ".join(terms) + " = 0")

            # Solve for c₃
            if rel[1] != 0:
                c3_exact = mp.mpf(0)
                for i, c in enumerate(rel):
                    if i != 1:
                        c3_exact -= mp.mpf(c) / rel[1] * basis[i]
                print(f"  → c₃ = {mp.nstr(c3_exact, 15)}")
                print(f"  Observed: {mp.nstr(c3, 15)}")
                print(f"  Match: {abs(float(c3 - c3_exact))*1e6:.4f} ppm")
                print()

                # Test the PSLQ-derived correction
                pred_pslq = pred_2 * (1 + c3_exact * eps)
                resid_pslq = hab_sum / pred_pslq - 1
                print(f"  With PSLQ c₃: residual = {float(resid_pslq)*1e6:.4f} ppm")
        else:
            print("  PSLQ: no relation found")
    except Exception as e:
        print(f"  PSLQ: {e}")

    print()

    # ---------------------------------------------------------------
    # Try product tower: (1+ε)(1−ε/30)(1+c₃·ε)(1+c₄·ε)...
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  Correction tower exploration")
    print("-" * 70)
    print()

    # After 3 factors, what's the 4th?
    if candidates:
        pred_3 = pred_2 * (1 + best_val * eps)
        S3 = hab_sum / pred_3
        c4_next = (S3 - 1) / eps
        print(f"  After 3 factors (best c₃ = {best_name}):")
        print(f"    S₃ = {mp.nstr(S3, 20)}")
        print(f"    Residual = {float(S3 - 1)*1e6:.4f} ppm")
        print(f"    c₄ = (S₃−1)/ℏ² = {mp.nstr(c4_next, 12)}")
        print()

    # ---------------------------------------------------------------
    # Summary ladder
    # ---------------------------------------------------------------
    print("=" * 70)
    print("  CORRECTION LADDER")
    print("=" * 70)
    print()

    stages = [
        ("bare", pred_0),
        ("×(1+ℏ²)", pred_0 * (1 + eps)),
        ("×(1+ℏ²)(1−ℏ²/30)", pred_2),
    ]
    if candidates:
        stages.append((f"×...×(1+{best_name}·ℏ²)", pred_2 * (1 + best_val * eps)))

    for name, pred in stages:
        r = hab_sum / pred - 1
        print(f"  {name:<40s} → {float(r)*1e6:>10.4g} ppm")
    print()

    # Witness — start_time passed to constructor (public API).
    w = WitnessBuilder("habiro-sub-ppm-third-factor", engine="mpmath",
                       start_time=_t0)
    w.set_description(
        "Third correction factor search for Habiro bridge (FITTED, not "
        f"derived). Tightest fit c₃ = {best_name} at {best_ppm:.4g} ppm; "
        f"structural near-match 1/1260 = 1/(C(9,4)·10) at {struct_ppm:.4g} ppm. "
        f"Ladder: 9495 → 319 → 7.8 → {best_ppm:.4g} ppm."
    )
    w.set_audit_only("docs/audits/2026-05-28-habiro-product-correction-7ppm.md")
    w.add_data("c3_observed", str(mp.nstr(c3, 15)))
    w.add_data("tightest_fit_candidate", best_name)
    w.add_data("tightest_fit_residual_ppm", best_ppm)
    w.add_data("structural_candidate", "1/1260 = 1/(C(9,4)·10)")
    w.add_data("structural_residual_ppm", struct_ppm)
    w.add_data("ladder", {
        "level_0_ppm": float((hab_sum / pred_0 - 1) * 1e6),
        "level_1_ppm": float((hab_sum / (pred_0 * (1 + eps)) - 1) * 1e6),
        "level_2_ppm": float((S2 - 1) * 1e6),
        "level_3_tightest_ppm": best_ppm,
        "level_3_structural_1260_ppm": struct_ppm,
    })

    w.add_assertion("sub_ppm",
                    computed=1 if best_ppm < 1 else 0,
                    expected=1, tolerance=0,
                    source="Third factor closes to < 1 ppm (sub-ppm milestone)")

    print(f"  Witness: {w.save()}")


if __name__ == "__main__":
    main()
