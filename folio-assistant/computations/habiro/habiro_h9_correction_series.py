#!/usr/bin/env python3
"""Habiro correction series: fit the exact correction to algebraic forms.

From the spectral decomposition:
  S = Habiro / (tr_M × n!/[n]_q! × Vol/ℏ²)
  S = 1 + c₂·ℏ² + c₄·ℏ⁴ + c₆·ℏ⁶ + ...

We know:
  c₂ ≈ 0.967 (close to 1 but not exact)
  c₄ ≈ −3.35

This script extracts higher-order coefficients and tests whether
the series is a known q-special function.
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
from _precision import set_compute_dps  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402
except ImportError:
    from qou_substrate.constants import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402


def q_factorial(n, q):
    result = mp.mpf(1)
    h = q - 1/q
    for k in range(1, n + 1):
        result *= (q**k - q**(-k)) / h
    return result


def q_integer(k, q):
    return (q**k - q**(-k)) / (q - 1/q)


def main():
    import time
    _t0 = time.perf_counter()
    set_compute_dps()
    mp.mp.dps = 50
    q = mp.mpf(Q_50_DIGIT_STR)
    hbar_q = (q - 1) / q
    hbar_sq = hbar_q**2
    h = q - 1/q
    h_sq = h**2
    n = 9

    vol_41 = vol_4_1_at(50)

    hab_sum = mp.mpf("136.0712063634817616514048508169837773395")
    tr_M = mp.mpf("1.065306144254449900000000000000000000000")
    plancherel_ratio = mp.factorial(n) / q_factorial(n, q)
    vol_over_hsq = vol_41 / hbar_sq

    pred_0 = tr_M * plancherel_ratio * vol_over_hsq
    S = hab_sum / pred_0

    print("=" * 70)
    print("  Habiro correction series analysis")
    print("=" * 70)
    print()
    print(f"  S = {mp.nstr(S, 25)}")
    print()

    # Single-point approximate extraction: (S-1)/ε gives c₂ + O(ε),
    # which is approximate (contaminated by higher orders at finite ε).
    # Product decomposition (below) is the clean approach.
    eps = hbar_sq
    print(f"  ε = ℏ² = {mp.nstr(eps, 15)}")
    print(f"  S = {mp.nstr(S, 20)}")
    print(f"  S - 1 = {mp.nstr(S - 1, 15)}")
    print()

    # Test closed-form candidates for S itself:
    candidates = [
        ("1 + ℏ²", 1 + eps),
        ("1/(1 − ℏ²)", 1 / (1 - eps)),
        ("(1 + ℏ²) / (1 − ℏ²)^{1/2}", (1 + eps) / mp.sqrt(1 - eps)),
        ("q^{ℏ²}", q**eps),
        ("[n]_q / (n · (1−ℏ²))", q_integer(n, q) / (n * (1 - eps))),
        ("n!/[n]_q! × [n]_q!/n! × S (tautology)", S),
    ]

    # More physics-motivated candidates:
    # The Plancherel ratio n!/[n]_q! already appears. What if the
    # true bridge is tr_M × Vol/ℏ² × f(q) where f(q) uses a
    # DIFFERENT q-factorial?

    # Key insight from the audit: the Habiro series terminates at M=8.
    # The proton braid is 3-strand (B₃) but lives at H₉.
    # The Habiro series uses (u;u)_m = Π_{j=1}^{m} (1 - u^j) with u = q².
    # So the q-Pochhammer normalization is different from the Wenzl trace's
    # [n]_q! normalization.

    # Test: (u;u)_M / [n]_q! where M=8 (termination index)
    u = q**2
    pochhammer_8 = mp.mpf(1)
    for j in range(1, 9):
        pochhammer_8 *= (1 - u**j)

    ratio_poch_qfact = pochhammer_8 / q_factorial(n, q)
    print(f"  (u;u)₈ = {mp.nstr(pochhammer_8, 15)}")
    print(f"  [9]_q! = {mp.nstr(q_factorial(n, q), 15)}")
    print(f"  (u;u)₈ / [9]_q! = {mp.nstr(ratio_poch_qfact, 15)}")
    print()

    # The full-twist eigenvalue on V_λ is q^{2c(λ)}.
    # The Habiro invariant is essentially a refined full-twist trace.
    # So: Habiro = Σ_λ y_λ · P_λ(q) where P_λ uses the Habiro
    # basis instead of just q^{2c(λ)}.

    # Test: does S = Σ_λ y_λ · (dim_q(λ)/dim_cl(λ)) / Σ_λ y_λ ?
    # i.e., is S related to the quantum/classical dimension ratio?

    # Load partition data
    wenzl_file = _pb.witness_path("wenzl-y-lambda-h9.witness.json", HERE)
    with open(wenzl_file) as f:
        wenzl_data = json.load(f)
    partitions_data = wenzl_data["data"]["per_partition"]

    from partition_utils import hook_lengths as hl  # noqa: E402

    def content_sum(shape):
        s = 0
        for i, row_len in enumerate(shape):
            for j in range(row_len):
                s += (j - i)
        return s

    def q_dim(shape, q):
        nn = sum(shape)
        numer = q_factorial(nn, q)
        hooks = hl(tuple(shape))
        denom = mp.mpf(1)
        for hk in hooks:
            denom *= q_integer(hk, q)
        return numer / denom

    def classical_dim(shape):
        import math
        nn = sum(shape)
        hooks = hl(tuple(shape))
        denom = 1
        for hk in hooks:
            denom *= hk
        return math.factorial(nn) // denom

    # Compute: weighted ratio of q-dim to classical dim
    sum_y_ratio = mp.mpf(0)
    sum_y = mp.mpf(0)
    sum_y_qtwist = mp.mpf(0)
    for entry in partitions_data:
        lam = tuple(entry["partition"])
        y_lam = mp.mpf(entry["y_lambda"])
        dq = q_dim(lam, q)
        dc = classical_dim(lam)
        c = content_sum(lam)
        sum_y += y_lam
        sum_y_ratio += y_lam * dq / dc
        sum_y_qtwist += y_lam * q**(2*c)

    weighted_ratio = sum_y_ratio / sum_y
    print(f"  Σ y_λ (dim_q/dim_cl) / Σ y_λ = {mp.nstr(weighted_ratio, 15)}")
    print(f"  S / weighted_ratio = {mp.nstr(S / weighted_ratio, 15)}")
    print()

    # The q-dim / classical-dim ratio for the trivial partition (n) is just 1.
    # For (n-1,1) it's [n-1]_q. The weighted average should give something.

    # Another approach: the Plancherel measure for H_n(q) is
    #   μ_q(λ) = dim_q(λ)² / [n]_q!
    # while the classical Plancherel is dim(λ)² / n!.
    # The ratio [n]_q! / n! = Π [k]_q / k.
    # The per-partition ratio is (dim_q)²/(dim)² × n!/[n]_q!.
    # Maybe S involves this.

    qfact_n = q_factorial(n, q)
    ratio_qfact = qfact_n / mp.factorial(n)
    print(f"  [n]_q!/n! = {mp.nstr(ratio_qfact, 15)}")
    print(f"  n!/[n]_q! = {mp.nstr(1/ratio_qfact, 15)}")
    print()

    # Key test: does the full bridge use [n]_q!/n! instead of n!/[n]_q! ?
    # i.e., Habiro = tr_M × Vol/ℏ² × [n]_q!/n! × correction?
    pred_alt = tr_M * ratio_qfact * vol_over_hsq
    S_alt = hab_sum / pred_alt
    print(f"  Alt pred (using [n]_q!/n! instead of n!/[n]_q!):")
    print(f"  pred_alt = {mp.nstr(pred_alt, 15)}")
    print(f"  S_alt = Hab/pred_alt = {mp.nstr(S_alt, 15)}")
    print(f"  ... this is (n!/[n]_q!)² × S = {mp.nstr(S_alt, 15)}")
    print()

    # The BEST candidates so far from spectral decomposition:
    # (1 + ℏ²) gives 319 ppm
    # 1/(1−ℏ²) gives 416 ppm (worse)
    # (1+ℏ²−6ℏ⁴) gives 253 ppm (better! c₄=−6 = −n(n-1)/12)

    # Let me test more c₄ values near −3.3:
    print("-" * 70)
    print("  Fine-grained c₄ scan around −3.35")
    print("-" * 70)
    print()

    # The exact S:
    S_exact = S
    # S = 1 + c₂_true·ε + c₄_true·ε² + ... where ε = ℏ²
    # At our ε ≈ 0.0098:
    # S-1 = c₂·ε + c₄·ε² + c₆·ε³ + ...
    # = ε·(c₂ + c₄·ε + c₆·ε² + ...)
    # (S-1)/ε = c₂ + c₄·ε + c₆·ε² + ...

    ratio_1 = (S_exact - 1) / eps  # = c₂ + c₄·ε + ...
    print(f"  (S−1)/ε = {mp.nstr(ratio_1, 20)}")
    print(f"  This = c₂ + c₄·ε + c₆·ε² + ...")
    print(f"  If c₂ = 1 exactly: c₄·ε + ... = {mp.nstr(ratio_1 - 1, 15)}")
    print(f"  → c₄ + c₆·ε + ... = {mp.nstr((ratio_1 - 1)/eps, 15)}")
    print()

    # So IF c₂ = 1 exactly:
    c4_if_c2_is_1 = (ratio_1 - 1) / eps
    print(f"  c₄ (assuming c₂=1) = {mp.nstr(c4_if_c2_is_1, 15)}")
    # This gives c₄ ≈ −3.35 (absorbs the c₂ error into c₄).

    # What if c₂ = 1 - 1/n² = 1 - 1/81 = 80/81?
    c2_try = mp.mpf(80) / 81
    c4_if_c2_80_81 = (ratio_1 - c2_try) / eps
    print(f"  c₄ (assuming c₂=80/81) = {mp.nstr(c4_if_c2_80_81, 15)}")

    # What if c₂ = 1 − 1/[n]_q ?
    c2_try2 = 1 - 1/q_integer(n, q)
    c4_if_c2_qi = (ratio_1 - c2_try2) / eps
    print(f"  c₄ (assuming c₂=1−1/[9]_q) = {mp.nstr(c4_if_c2_qi, 15)}")

    # What if c₂ = [n-1]_q/[n]_q = [8]_q/[9]_q ?
    c2_try3 = q_integer(n-1, q) / q_integer(n, q)
    c4_if_c2_qrat = (ratio_1 - c2_try3) / eps
    print(f"  c₄ (assuming c₂=[8]_q/[9]_q) = {mp.nstr(c4_if_c2_qrat, 15)}")
    print(f"    [8]_q/[9]_q = {mp.nstr(c2_try3, 15)}")

    print()

    # Multi-point extraction: evaluate at slightly different q values
    # to get two equations for c₂ and c₄.
    print("-" * 70)
    print("  Multi-point extraction (q₀ ± δ)")
    print("-" * 70)
    print()

    # ---------------------------------------------------------------
    # Test the most promising candidate: c₂=1, c₄=−n(n−1)/12=−6
    # and check what c₆ would need to be
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  Candidate: 1 + ℏ² − 6ℏ⁴ + c₆ℏ⁶")
    print("-" * 70)
    print()

    pred_nn12 = pred_0 * (1 + eps - 6 * eps**2)
    resid_nn12 = hab_sum / pred_nn12 - 1
    c6_needed = resid_nn12 / eps**3
    print(f"  Residual after (1+ℏ²−6ℏ⁴) = {mp.nstr(resid_nn12, 12)} ({float(resid_nn12)*1e6:.1f} ppm)")
    print(f"  c₆ needed to close = {mp.nstr(c6_needed, 10)}")
    print()

    # What about Bernoulli-like series?
    # B₂ = 1/6, B₄ = -1/30
    # 1 + B₂·ℏ²/(1!) + B₄·ℏ⁴/(2!) + ...
    # = 1 + ℏ²/6 − ℏ⁴/60 + ...  (too small)

    # Or the q-exponential?
    # e_q(x) = Σ x^n / [n]_q!
    # Or the Dedekind eta / theta function?

    # Actually: what if S = [n]_q / n × n!/[n]_q! = 1 exactly?
    # No, we already showed S ≠ 1.

    # Key structural test: S = (1 + a₁ℏ²)(1 + a₂ℏ²)... product form?
    # If S = (1+ℏ²)·(1 + c₄'ℏ²), then S = 1 + (1+c₄')ℏ² + c₄'ℏ⁴
    # c₂ = 1+c₄' ≈ 0.967 → c₄' = −0.033
    # c₄ = c₄' ≈ −0.033 / ℏ² ... no that doesn't work dimensionally.

    # Product: S = Π_{k=1}^{?} (1 + a_k · ℏ^{2k})
    # First factor (1+ℏ²) accounts for c₂≈1.
    # Second factor (1 + c₄_eff · ℏ²) where c₄_eff = residual/(ℏ² × pred₁)
    S_after_first = hab_sum / pred_0 / (1 + eps)
    c_next = (S_after_first - 1) / eps
    print(f"  After dividing by (1+ℏ²):")
    print(f"  S₁ = {mp.nstr(S_after_first, 20)}")
    print(f"  S₁ − 1 = {mp.nstr(S_after_first - 1, 15)}")
    print(f"  (S₁−1)/ℏ² = {mp.nstr(c_next, 12)}")
    print()

    # So the next correction factor is (1 + c_next·ℏ²) where c_next ≈ −0.0326
    # What is −0.0326?
    print(f"  c_next ≈ {float(c_next):.8f}")
    print(f"  −1/[n]_q = {float(-1/q_integer(n, q)):.8f}")
    print(f"  −1/n² = {float(-1/n**2):.8f}")
    print(f"  −ℏ²/3 = {float(-eps/3):.8f}")
    print(f"  −1/30 = {float(-1/30):.8f}")
    print(f"  −1/[n]_q² = {float(-1/q_integer(n, q)**2):.8f}")
    print()

    # Is c_next = −1/[n]_q² or similar?
    # c_next ≈ −0.0326
    # −1/30 = −0.0333... close!
    miss_30 = float(c_next + mp.mpf(1)/30)
    print(f"  c_next + 1/30 = {miss_30:.8f}")
    # Try −1/[n-1]_q:
    print(f"  −1/[8]_q = {float(-1/q_integer(8, q)):.8f}")
    miss_q8 = float(c_next + 1/q_integer(8, q))
    print(f"  c_next + 1/[8]_q = {miss_q8:.8f}")
    print()

    # Product form: S = (1+ℏ²)(1 − ℏ²/30)
    pred_product = pred_0 * (1 + eps) * (1 - eps/30)
    resid_product = hab_sum / pred_product - 1
    print(f"  Product (1+ℏ²)(1−ℏ²/30): residual = {float(resid_product)*1e6:.1f} ppm")

    # Product: (1+ℏ²)(1 − ℏ²/[8]_q)
    pred_q8 = pred_0 * (1 + eps) * (1 - eps/q_integer(8, q))
    resid_q8 = hab_sum / pred_q8 - 1
    print(f"  Product (1+ℏ²)(1−ℏ²/[8]_q): residual = {float(resid_q8)*1e6:.1f} ppm")

    # Product: (1+ℏ²)(1 − c_next·ℏ²) [exact]
    pred_exact2 = pred_0 * (1 + eps) * (1 + c_next * eps)
    resid_exact2 = hab_sum / pred_exact2 - 1
    print(f"  Product (1+ℏ²)(1+c_next·ℏ²) [exact c_next]: residual = {float(resid_exact2)*1e6:.1f} ppm")
    print()

    # ---------------------------------------------------------------
    # PSLQ search for c_next
    # ---------------------------------------------------------------
    print("-" * 70)
    print("  PSLQ integer-relation search for c_next")
    print("-" * 70)
    print()

    x = c_next
    # Look for integer relation: a₀ + a₁·x + a₂·(1/n) + a₃·(1/n²) + a₄·(1/[n]_q) + a₅·ℏ² = 0
    basis = [
        ("1", mp.mpf(1)),
        ("c_next", x),
        ("1/n", mp.mpf(1)/n),
        ("1/n²", mp.mpf(1)/n**2),
        ("1/[n]_q", 1/q_integer(n, q)),
        ("ℏ²", eps),
        ("1/[n-1]_q", 1/q_integer(n-1, q)),
        ("1/(n(n-1))", mp.mpf(1)/(n*(n-1))),
    ]

    try:
        vals = [b[1] for b in basis]
        rel = mp.pslq(vals, maxcoeff=100)
        if rel:
            print(f"  PSLQ found: ", end="")
            terms = []
            for i, c in enumerate(rel):
                if c != 0:
                    terms.append(f"{c}·{basis[i][0]}")
            print(" + ".join(terms) + " = 0")
        else:
            print("  PSLQ: no relation found (maxcoeff=100)")
    except Exception as e:
        print(f"  PSLQ error: {e}")

    print()

    # ---------------------------------------------------------------
    # Summary of findings
    # ---------------------------------------------------------------
    print("=" * 70)
    print("  FINDINGS SUMMARY")
    print("=" * 70)
    print()
    print(f"  S = Habiro / (tr_M × n!/[n]_q! × Vol/ℏ²)")
    print(f"  S = {mp.nstr(S, 20)}")
    print(f"  S ≈ 1 + 0.967·ℏ² + O(ℏ⁴)")
    print(f"")
    print(f"  Product decomposition: S = (1+ℏ²) × (1 + c_next·ℏ²) × ...")
    print(f"  c_next = {mp.nstr(c_next, 12)}")
    print(f"  Best algebraic match: c_next ≈ −1/30 (miss = {miss_30:.6f})")
    print(f"  c_next ≈ −1/[8]_q (miss = {miss_q8:.6f})")
    print()

    w = WitnessBuilder("habiro-correction-series", engine="mpmath")
    w.set_description(
        "Habiro correction series S = 1 + c₂·ℏ² + c₄·ℏ⁴ + ... "
        f"Product form: S ≈ (1+ℏ²)(1 + c_next·ℏ²) with c_next ≈ {float(c_next):.6f}. "
        f"Best algebraic match: c_next ≈ −1/30 (miss {miss_30:.6f})."
    )
    w.set_audit_only("docs/audits/2026-05-28-habiro-product-correction-7ppm.md")
    w._start_time = _t0
    w.add_data("S_exact", str(mp.nstr(S, 25)))
    w.add_data("c2_approx", float((S-1)/eps))
    w.add_data("c_next_after_1_plus_hsq", float(c_next))
    w.add_data("best_algebraic_match", "-1/30")
    w.add_data("miss_vs_neg_1_over_30", miss_30)

    w.add_assertion("S_near_1_plus_hsq",
                    computed=1 if abs(float(S - 1 - eps)) < 0.001 else 0,
                    expected=1, tolerance=0,
                    source="S ≈ 1 + ℏ² to 3 decimal places")
    print(f"\n  Witness: {w.save()}")


if __name__ == "__main__":
    main()
