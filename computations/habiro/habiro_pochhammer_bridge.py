#!/usr/bin/env python3
"""Habiro Pochhammer bridge: (q;q)_m vs (u;u)_m conventions.

The Habiro sum 136.07 uses (q;q)_m = Π(1−q^k) convention.
The Markov trace tr_M = 1.065 uses (u;u)_m = Π(1−u^k) convention
(where u=√q), and divides by 4u²¹+4u¹⁹.

The ratio 136.07/1.065 = 127.73 is the Pochhammer bridge:
  Π_{k=1}^{M} (q;q)_m / (u;u)_m × ... normalization

The product correction (1+ℏ²)(1−ℏ²/30) at 7.8 ppm describes this
bridge in terms of the Plancherel ratio and Vol(4₁).

This script verifies the Pochhammer convention difference is the
source of the 127.73 ratio, and tests whether the (1+ℏ²)(1−ℏ²/30)
correction follows algebraically from the convention change.
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
import time

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


def main():
    _t0 = time.perf_counter()
    set_compute_dps()
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    u = mp.sqrt(q)  # spinor rate \check{q} = q^{1/2} (Habiro lit: u)
    hbar_q = (q - 1) / q
    eps = hbar_q**2
    n = 9

    vol = vol_4_1_at(50)

    # Load Habiro coefficients
    with open(_pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)) as f:
        data = json.load(f)
    proton = data['results']['p (proton, A=1)']

    coeffs_raw = proton['habiro_coefficients']

    def eval_a_m(expr_str, u_val):
        ns = {"check_q": u_val, "__builtins__": {}}
        return mp.mpf(eval(expr_str, ns))

    # Convention A: (q;q)_m = Π_{k=1}^{m} (1 - q^k) [the 136.07 convention]
    def poch_qq(m):
        p = mp.mpf(1)
        for k in range(1, m + 1):
            p *= (1 - q**k)
        return p

    # Convention B: (u;u)_m = Π_{k=1}^{m} (1 - u^k) [the tr_M numerator]
    def poch_uu(m):
        p = mp.mpf(1)
        for k in range(1, m + 1):
            p *= (1 - u**k)
        return p

    # Evaluate both conventions
    hab_A = mp.mpf(0)  # (q;q) convention
    hab_B = mp.mpf(0)  # (u;u) convention

    print("=" * 70)
    print("  Habiro Pochhammer bridge")
    print("=" * 70)
    print()
    print(f"  q₀ = {mp.nstr(q, 15)}")
    print(f"  u₀ = √q₀ = {mp.nstr(u, 15)}")
    print()

    print(f"  {'m':>2s}  {'a_m(u)':>12s}  {'(q;q)_m':>14s}  {'(u;u)_m':>14s}  {'ratio':>10s}")
    print(f"  {'─'*2}  {'─'*12}  {'─'*14}  {'─'*14}  {'─'*10}")

    for entry in coeffs_raw:
        m = entry['m']
        a_val = eval_a_m(entry['a_m'], u)
        pA = poch_qq(m)
        pB = poch_uu(m)
        hab_A += a_val * pA
        hab_B += a_val * pB

        ratio = pA / pB if m > 0 else mp.mpf(1)
        print(f"  {m:>2d}  {float(a_val):>12.2f}  {float(pA):>14.6e}  {float(pB):>14.6e}  {float(ratio):>10.4f}")

    print()

    # The denominator for tr_M
    denom = 4 * u**21 + 4 * u**19
    tr_M = hab_B / denom

    print(f"  Convention A: Σ a_m · (q;q)_m     = {mp.nstr(hab_A, 20)}")
    print(f"  Convention B: Σ a_m · (u;u)_m     = {mp.nstr(hab_B, 20)}")
    print(f"  Denom 4u²¹+4u¹⁹                  = {mp.nstr(denom, 15)}")
    print(f"  tr_M = conv_B / denom             = {mp.nstr(tr_M, 20)}")
    print()

    bridge = hab_A / tr_M
    print(f"  Bridge ratio = conv_A / tr_M      = {mp.nstr(bridge, 15)}")
    print(f"  = hab_A × denom / hab_B           = {mp.nstr(hab_A * denom / hab_B, 15)}")
    print()

    # The bridge prediction
    plancherel = mp.factorial(n) / q_factorial(n, q)
    vol_over_hsq = vol / eps
    pred = plancherel * vol_over_hsq * (1 + eps) * (1 - eps/30)
    residual = bridge / pred - 1

    print(f"  Predicted bridge = Plancherel × Vol/ℏ² × (1+ℏ²)(1−ℏ²/30)")
    print(f"    = {mp.nstr(pred, 15)}")
    print(f"  Residual = {mp.nstr(residual, 10)} ({float(residual)*1e6:.1f} ppm)")
    print()

    # ---------------------------------------------------------------
    # Algebraic analysis: why does (q;q)_m / (u;u)_m × denom give
    # the Plancherel × Vol × correction?
    # ---------------------------------------------------------------
    # (q;q)_m / (u;u)_m = Π_{k=1}^{m} (1-q^k) / (1-u^k)
    #                   = Π_{k=1}^{m} (1+u^k) since (1-q^k)=(1-u^{2k})=(1-u^k)(1+u^k)
    print("-" * 70)
    print("  Algebraic decomposition: (q;q)_m / (u;u)_m = Π(1+u^k)")
    print("-" * 70)
    print()

    # This is the key insight!
    # (1-q^k) = (1-u^{2k}) = (1-u^k)(1+u^k)
    # So (q;q)_m = (u;u)_m × Π_{k=1}^m (1+u^k)
    # Therefore: hab_A = Σ a_m · (u;u)_m · Π_{k=1}^m (1+u^k)
    # And: hab_A / hab_B = weighted average of Π(1+u^k) over the
    # Habiro coefficients.

    # Verify: compute Π(1+u^k) for each m
    product_ratio = mp.mpf(1)
    for k in range(1, 9):
        product_ratio *= (1 + u**k)
        verify = poch_qq(k) / poch_uu(k)
        print(f"  m={k}: Π_{{j=1}}^{k} (1+u^j) = {mp.nstr(product_ratio, 12):>16s}  "
              f"(q;q)_{k}/(u;u)_{k} = {mp.nstr(verify, 12):>16s}  "
              f"match: {abs(float(product_ratio - verify)) < 1e-40}")

    print()

    # The full bridge is:
    # bridge = hab_A / tr_M = hab_A × denom / hab_B
    # = denom × (Σ a_m·(u;u)_m·Π(1+u^k)) / (Σ a_m·(u;u)_m)
    # = denom × <Π(1+u^k)>_{Habiro}

    # where <·>_{Habiro} is the Habiro-weighted average.
    # The Habiro weights are a_m · (u;u)_m.

    # Compute the weighted average
    total_weight = mp.mpf(0)
    weighted_sum = mp.mpf(0)
    for entry in coeffs_raw:
        m = entry['m']
        a_val = eval_a_m(entry['a_m'], u)
        w_m = a_val * poch_uu(m)
        prod_m = mp.mpf(1)
        for k in range(1, m + 1):
            prod_m *= (1 + u**k)
        total_weight += w_m
        weighted_sum += w_m * prod_m

    avg_product = weighted_sum / total_weight
    print(f"  <Π(1+u^k)>_{{Habiro}} = {mp.nstr(avg_product, 15)}")
    print(f"  hab_A / hab_B = {mp.nstr(hab_A / hab_B, 15)}")
    print(f"  Match: {abs(float(avg_product - hab_A/hab_B)) < 1e-30}")
    print()

    # So: bridge = denom × avg_product = 4u¹⁹(u²+1) × <Π(1+u^k)>
    bridge_from_avg = denom * avg_product
    print(f"  bridge = denom × <Π(1+u^k)> = {mp.nstr(bridge_from_avg, 15)}")
    print(f"  bridge (direct)              = {mp.nstr(bridge, 15)}")
    print()

    # And we want this to equal Plancherel × Vol/ℏ² × (1+ε)(1-ε/30):
    print(f"  bridge / (Plancherel × Vol/ℏ²) = {mp.nstr(bridge / (plancherel * vol_over_hsq), 15)}")
    print(f"  (1+ε)(1−ε/30)                 = {mp.nstr((1+eps)*(1-eps/30), 15)}")
    print(f"  Residual: {float(bridge / (plancherel * vol_over_hsq) - (1+eps)*(1-eps/30))*1e6:.1f} ppm")
    print()

    # ---------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------
    print("=" * 70)
    print("  SUMMARY")
    print("=" * 70)
    print()
    print("  The 'Habiro sum' 136.07 uses (q;q)_m = Π(1−q^k).")
    print("  The Markov trace 1.065 uses (u;u)_m = Π(1−u^k) with u=√q,")
    print("  divided by denom = 4u²¹+4u¹⁹.")
    print()
    print("  Since (1−q^k) = (1−u^k)(1+u^k), the ratio is:")
    print("    hab_A / hab_B = <Π_{k=1}^m (1+u^k)>_{Habiro}")
    print()
    print("  The full bridge = denom × <Π(1+u^k)>")
    print(f"                  = {mp.nstr(bridge, 10)}")
    print(f"                  ≈ n!/[n]_q! × Vol/ℏ² × (1+ℏ²)(1−ℏ²/30)")
    print(f"                    to {abs(float(residual)*1e6):.1f} ppm")
    print()

    w = WitnessBuilder("habiro-pochhammer-bridge", engine="mpmath")
    w._start_time = _t0
    w.set_description(
        "Habiro Pochhammer bridge: the 136.07/1.065 ratio comes from "
        "(q;q)_m vs (u;u)_m convention difference, where "
        "(1−q^k) = (1−u^k)(1+u^k). The bridge = denom × <Π(1+u^k)>_Habiro "
        "≈ Plancherel × Vol/ℏ² × (1+ℏ²)(1−ℏ²/30) at 7.8 ppm."
    )
    w.set_audit_only("docs/audits/2026-05-28-habiro-product-correction-7ppm.md")
    w.add_data("hab_A_qq_convention", str(mp.nstr(hab_A, 20)))
    w.add_data("hab_B_uu_convention", str(mp.nstr(hab_B, 20)))
    w.add_data("tr_M", str(mp.nstr(tr_M, 20)))
    w.add_data("bridge_ratio", str(mp.nstr(bridge, 15)))
    w.add_data("avg_1_plus_uk", str(mp.nstr(avg_product, 15)))
    w.add_data("residual_ppm", float(residual) * 1e6)
    w.add_data("key_identity", "(1-q^k) = (1-u^k)(1+u^k), u=√q")

    w.add_assertion("bridge_at_7_8ppm",
                    computed=1 if abs(float(residual)*1e6) < 10 else 0,
                    expected=1, tolerance=0,
                    source="bridge ≈ Plancherel × Vol/ℏ² × (1+ℏ²)(1−ℏ²/30) at <10 ppm")

    print(f"  Witness: {w.save()}")


if __name__ == "__main__":
    main()
