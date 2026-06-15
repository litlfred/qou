#!/usr/bin/env python3
"""Habiro normalization bridge: neutron cross-check.

Replicates the proton analysis (Pochhammer bridge + correction tower)
for the NEUTRON braid.  The proton bridge closes as:

    hab_A / tr_M  ≈  Plancherel × Vol/ℏ² × (1+ℏ²)(1−ℏ²/30)(1+ℏ²/1260)

closing from 9495 → 319 → 7.8 → 0.03 ppm.

Key question: is the correction pattern universal (same −1/30 second
factor, same ~1/1260 third factor) or braid-specific?
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


def eval_a_m(expr_str, u_val):
    """Evaluate a Habiro coefficient polynomial at u = u_val (u = \check{q} = q^{1/2}, spinor rate; "u" name per Habiro lit)."""
    ns = {"check_q": u_val, "__builtins__": {}}
    return mp.mpf(eval(expr_str, ns))


def poch_qq(m, q):
    """(q;q)_m = prod_{k=1}^{m} (1 - q^k)."""
    p = mp.mpf(1)
    for k in range(1, m + 1):
        p *= (1 - q**k)
    return p


def poch_uu(m, u):
    """(u;u)_m = prod_{k=1}^{m} (1 - u^k)."""
    p = mp.mpf(1)
    for k in range(1, m + 1):
        p *= (1 - u**k)
    return p


def main():
    _t0 = time.perf_counter()
    set_compute_dps()
    q = mp.mpf(Q_50_DIGIT_STR)
    u = mp.sqrt(q)
    hbar_q = (q - 1) / q
    eps = hbar_q**2
    n = 9
    p_n = 30  # p(9) = 30

    vol = vol_4_1_at(mp.mp.dps)

    # ------------------------------------------------------------------
    # Load coefficients
    # ------------------------------------------------------------------
    with open(_pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)) as f:
        data = json.load(f)

    neutron = data['results']['n (neutron, A=1)']
    proton  = data['results']['p (proton, A=1)']

    n_coeffs = neutron['habiro_coefficients']
    p_coeffs = proton['habiro_coefficients']

    # ------------------------------------------------------------------
    # Evaluate both conventions for the neutron
    # ------------------------------------------------------------------
    n_hab_A = mp.mpf(0)  # (q;q) convention
    n_hab_B = mp.mpf(0)  # (u;u) convention

    print("=" * 72)
    print("  Habiro neutron cross-check: Pochhammer bridge + correction tower")
    print("=" * 72)
    print()
    print(f"  q₀ = {mp.nstr(q, 15)}")
    print(f"  u₀ = √q₀ = {mp.nstr(u, 15)}")
    print(f"  ℏ² = (q-1)²/q² = {mp.nstr(eps, 15)}")
    print(f"  n = {n}, p(n) = {p_n}")
    print()

    # --- Neutron Habiro sums ---
    print("  NEUTRON Habiro coefficients:")
    print(f"  {'m':>2s}  {'a_m(u)':>12s}  {'(q;q)_m':>14s}  {'(u;u)_m':>14s}  {'ratio':>10s}")
    print(f"  {'─'*2}  {'─'*12}  {'─'*14}  {'─'*14}  {'─'*10}")

    for entry in n_coeffs:
        m = entry['m']
        a_val = eval_a_m(entry['a_m'], u)
        pA = poch_qq(m, q)
        pB = poch_uu(m, u)
        n_hab_A += a_val * pA
        n_hab_B += a_val * pB

        ratio = pA / pB if m > 0 else mp.mpf(1)
        print(f"  {m:>2d}  {float(a_val):>12.2f}  {float(pA):>14.6e}  {float(pB):>14.6e}  {float(ratio):>10.4f}")

    print()

    # --- Proton Habiro sums (for comparison) ---
    p_hab_A = mp.mpf(0)
    p_hab_B = mp.mpf(0)
    for entry in p_coeffs:
        m = entry['m']
        a_val = eval_a_m(entry['a_m'], u)
        p_hab_A += a_val * poch_qq(m, q)
        p_hab_B += a_val * poch_uu(m, u)

    # Denominators (same for both — 4u²¹ + 4u¹⁹)
    denom = 4 * u**21 + 4 * u**19

    n_tr_M = n_hab_B / denom
    p_tr_M = p_hab_B / denom

    print(f"  Neutron: Σ a_m·(q;q)_m  = {mp.nstr(n_hab_A, 20)}")
    print(f"  Neutron: Σ a_m·(u;u)_m  = {mp.nstr(n_hab_B, 20)}")
    print(f"  Neutron: tr_M            = {mp.nstr(n_tr_M, 20)}")
    print(f"  (witness tr_M_at_q0      = {neutron['tr_M_at_q0']})")
    print()
    print(f"  Proton:  Σ a_m·(q;q)_m  = {mp.nstr(p_hab_A, 20)}")
    print(f"  Proton:  tr_M            = {mp.nstr(p_tr_M, 20)}")
    print()

    # ------------------------------------------------------------------
    # Bridge ratio
    # ------------------------------------------------------------------
    n_bridge = n_hab_A / n_tr_M
    p_bridge = p_hab_A / p_tr_M

    print("-" * 72)
    print("  Bridge ratios")
    print("-" * 72)
    print()
    print(f"  Neutron bridge = hab_A / tr_M = {mp.nstr(n_bridge, 15)}")
    print(f"  Proton  bridge = hab_A / tr_M = {mp.nstr(p_bridge, 15)}")
    print(f"  Ratio (p/n)                   = {mp.nstr(p_bridge / n_bridge, 15)}")
    print()

    # ------------------------------------------------------------------
    # Predicted bridge: Plancherel × Vol/ℏ²
    # ------------------------------------------------------------------
    plancherel = mp.factorial(n) / q_factorial(n, q)
    vol_over_hsq = vol / eps

    n_pred_0 = n_tr_M * plancherel * vol_over_hsq
    p_pred_0 = p_tr_M * plancherel * vol_over_hsq

    n_ratio_0 = n_hab_A / n_pred_0 - 1
    p_ratio_0 = p_hab_A / p_pred_0 - 1

    print("-" * 72)
    print("  CORRECTION LADDER — side by side")
    print("-" * 72)
    print()
    print(f"  {'Stage':<45s} {'Neutron ppm':>12s}  {'Proton ppm':>12s}")
    print(f"  {'─'*45} {'─'*12}  {'─'*12}")

    # Level 0: bare
    n_S0 = n_hab_A / n_pred_0
    p_S0 = p_hab_A / p_pred_0
    print(f"  {'bare: tr_M × Plancherel × Vol/ℏ²':<45s} {float(n_S0-1)*1e6:>12.2f}  {float(p_S0-1)*1e6:>12.2f}")

    # Level 1: × (1 + ℏ²)
    n_pred_1 = n_pred_0 * (1 + eps)
    p_pred_1 = p_pred_0 * (1 + eps)
    n_S1 = n_hab_A / n_pred_1
    p_S1 = p_hab_A / p_pred_1
    print(f"  {'× (1 + ℏ²)':<45s} {float(n_S1-1)*1e6:>12.2f}  {float(p_S1-1)*1e6:>12.2f}")

    # Level 2: × (1 + ℏ²)(1 − ℏ²/30)
    n_pred_2 = n_pred_1 * (1 - eps / p_n)
    p_pred_2 = p_pred_1 * (1 - eps / p_n)
    n_S2 = n_hab_A / n_pred_2
    p_S2 = p_hab_A / p_pred_2
    print(f"  {'× (1 + ℏ²)(1 − ℏ²/30)':<45s} {float(n_S2-1)*1e6:>12.2f}  {float(p_S2-1)*1e6:>12.2f}")

    # Level 3: × (1 + ℏ²)(1 − ℏ²/30)(1 + ℏ²/1260)
    n_pred_3 = n_pred_2 * (1 + eps / 1260)
    p_pred_3 = p_pred_2 * (1 + eps / 1260)
    n_S3 = n_hab_A / n_pred_3
    p_S3 = p_hab_A / p_pred_3
    print(f"  {'× ...(1 + ℏ²/1260)':<45s} {float(n_S3-1)*1e6:>12.2f}  {float(p_S3-1)*1e6:>12.2f}")

    print()

    # ------------------------------------------------------------------
    # Extract braid-specific c₃
    # ------------------------------------------------------------------
    n_c3 = (n_S2 - 1) / eps
    p_c3 = (p_S2 - 1) / eps

    print("-" * 72)
    print("  Third-factor coefficient c₃ = (S₂ − 1) / ℏ²")
    print("-" * 72)
    print()
    print(f"  Neutron c₃ = {mp.nstr(n_c3, 15)}")
    print(f"  Proton  c₃ = {mp.nstr(p_c3, 15)}")
    print(f"  1/1260     = {mp.nstr(mp.mpf(1)/1260, 15)}")
    print()
    print(f"  Neutron: 1/c₃ = {mp.nstr(1/n_c3, 10)}")
    print(f"  Proton:  1/c₃ = {mp.nstr(1/p_c3, 10)}")
    print()

    # ------------------------------------------------------------------
    # Search for best third factor for the NEUTRON
    # ------------------------------------------------------------------
    print("-" * 72)
    print("  Exhaustive search for neutron third factor c₃")
    print("-" * 72)
    print()

    candidates = []

    # Simple rational scan
    for a in range(-10, 11):
        for b in range(-10, 11):
            for c_denom in [1, 2, 3, 4, 6, 8, 12, 24, 30, 60, 90, 120,
                            180, 270, 360, 540, 720, 900, 1260, 1800,
                            2520, 5040, 27000]:
                if c_denom == 0:
                    continue
                val = mp.mpf(a * n + b) / c_denom
                if abs(float(val)) > 0.01:
                    continue
                pred_try = n_pred_2 * (1 + val * eps)
                resid = n_hab_A / pred_try - 1
                ppm = abs(float(resid) * 1e6)
                if ppm < 5:
                    candidates.append((f"({a}n+{b})/{c_denom}", val, ppm, resid))

    # Special algebraic expressions
    special_vals = [
        ("1/p(n)²", mp.mpf(1) / p_n**2),
        ("1/(2·p(n)²)", mp.mpf(1) / (2 * p_n**2)),
        ("1/(n·p(n))", mp.mpf(1) / (n * p_n)),
        ("1/(n²·p(n))", mp.mpf(1) / (n**2 * p_n)),
        ("1/(n³)", mp.mpf(1) / n**3),
        ("1/1260", mp.mpf(1) / 1260),
        ("1/1200", mp.mpf(1) / 1200),
        ("1/1256", mp.mpf(1) / 1256),
        ("1/1350", mp.mpf(1) / 1350),
        ("1/[9]_q²", 1 / q_integer(9, q)**2),
        ("n/(p(n)²×2)", mp.mpf(n) / (2 * p_n**2)),
        ("n/(2·n·p(n))", mp.mpf(1) / (2 * p_n)),
        ("1/(n·p(n)²)", mp.mpf(1) / (n * p_n**2)),
        ("(n+1)/(n·p(n)²)", mp.mpf(n + 1) / (n * p_n**2)),
        ("(n-1)/(n·p(n)²)", mp.mpf(n - 1) / (n * p_n**2)),
    ]
    for name, val in special_vals:
        pred_try = n_pred_2 * (1 + val * eps)
        resid = n_hab_A / pred_try - 1
        ppm = abs(float(resid) * 1e6)
        candidates.append((name, val, ppm, resid))

    candidates.sort(key=lambda x: x[2])

    print(f"  {'Expression':<25s} {'Value':>14s} {'Residual':>10s}")
    print(f"  {'─'*25} {'─'*14} {'─'*10}")
    for name, val, ppm, resid in candidates[:20]:
        sign = "+" if float(resid) > 0 else "−"
        print(f"  {name:<25s} {mp.nstr(val, 8):>14s} {sign}{ppm:>8.4f} ppm")

    print()

    best_name = candidates[0][0] if candidates else "?"
    best_val  = candidates[0][1] if candidates else mp.mpf(0)
    best_ppm  = candidates[0][2] if candidates else 999

    # ------------------------------------------------------------------
    # PSLQ on neutron c₃
    # ------------------------------------------------------------------
    print("-" * 72)
    print("  PSLQ search for neutron c₃")
    print("-" * 72)
    print()

    basis = [
        mp.mpf(1),
        n_c3,
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
            terms = []
            for i, c in enumerate(rel):
                if c != 0:
                    terms.append(f"{c}·{labels[i]}")
            print(f"  PSLQ: " + " + ".join(terms) + " = 0")

            if rel[1] != 0:
                c3_exact = mp.mpf(0)
                for i, c in enumerate(rel):
                    if i != 1:
                        c3_exact -= mp.mpf(c) / rel[1] * basis[i]
                print(f"  → c₃ = {mp.nstr(c3_exact, 15)}")
                print(f"  Observed: {mp.nstr(n_c3, 15)}")
                delta = abs(float(c3_exact - n_c3))
                print(f"  Match: {delta*1e6:.6f} ppm")
        else:
            print("  PSLQ: no relation found")
    except Exception as e:
        print(f"  PSLQ: {e}")

    print()

    # ------------------------------------------------------------------
    # Universality test: do proton and neutron share the same −1/30?
    # ------------------------------------------------------------------
    print("=" * 72)
    print("  UNIVERSALITY TEST")
    print("=" * 72)
    print()

    # The −1/30 comes from p(n) = 30 for both (same n = 9).
    # The first factor (1+ℏ²) is universal by construction (Pochhammer
    # identity independent of braid word).
    # The key test is whether −1/30 works for neutron too.

    print(f"  Factor 1: (1 + ℏ²)")
    print(f"    Proton:  residual after ×(1+ℏ²) = {float(p_S1-1)*1e6:.2f} ppm")
    print(f"    Neutron: residual after ×(1+ℏ²) = {float(n_S1-1)*1e6:.2f} ppm")
    print(f"    Same sign: {(float(p_S1-1) > 0) == (float(n_S1-1) > 0)}")
    print()

    print(f"  Factor 2: (1 − ℏ²/30)  [p(n) = p(9) = 30]")
    print(f"    Proton:  residual after ×(1+ℏ²)(1−ℏ²/30) = {float(p_S2-1)*1e6:.4f} ppm")
    print(f"    Neutron: residual after ×(1+ℏ²)(1−ℏ²/30) = {float(n_S2-1)*1e6:.4f} ppm")
    same_sign_2 = (float(p_S2 - 1) > 0) == (float(n_S2 - 1) > 0)
    print(f"    Same sign: {same_sign_2}")
    print()

    # Compare c₃ values
    c3_ratio = n_c3 / p_c3
    print(f"  Factor 3 coefficient c₃:")
    print(f"    Proton  c₃ = {mp.nstr(p_c3, 12)}  (1/c₃ ≈ {mp.nstr(1/p_c3, 8)})")
    print(f"    Neutron c₃ = {mp.nstr(n_c3, 12)}  (1/c₃ ≈ {mp.nstr(1/n_c3, 8)})")
    print(f"    Ratio n/p  = {mp.nstr(c3_ratio, 10)}")
    print(f"    Proton best = 1/1260 at ~0.03 ppm, neutron best = {best_name} at {best_ppm:.4f} ppm")
    print()

    same_c3 = abs(float(c3_ratio) - 1) < 0.05  # within 5%
    universal = same_sign_2 and same_c3

    if universal:
        verdict = "UNIVERSAL — same correction pattern for proton and neutron"
    else:
        # Check if just c3 differs
        if same_sign_2 and not same_c3:
            verdict = "PARTIALLY UNIVERSAL — (1+ℏ²)(1−ℏ²/30) works for both; c₃ is braid-specific"
        else:
            verdict = "BRAID-SPECIFIC — correction factors differ between proton and neutron"

    print(f"  VERDICT: {verdict}")
    print()

    # ------------------------------------------------------------------
    # Summary ladder
    # ------------------------------------------------------------------
    print("=" * 72)
    print("  CORRECTION LADDER SUMMARY")
    print("=" * 72)
    print()

    n_levels = [
        ("bare", float(n_S0 - 1) * 1e6),
        ("× (1+ℏ²)", float(n_S1 - 1) * 1e6),
        ("× (1+ℏ²)(1−ℏ²/30)", float(n_S2 - 1) * 1e6),
        ("× (1+ℏ²)(1−ℏ²/30)(1+ℏ²/1260)", float(n_S3 - 1) * 1e6),
    ]
    if best_name != "1/1260":
        n_pred_best = n_pred_2 * (1 + best_val * eps)
        n_S_best = n_hab_A / n_pred_best
        n_levels.append((f"× ...(1+{best_name}·ℏ²)  [best]", float(n_S_best - 1) * 1e6))

    p_levels = [
        ("bare", float(p_S0 - 1) * 1e6),
        ("× (1+ℏ²)", float(p_S1 - 1) * 1e6),
        ("× (1+ℏ²)(1−ℏ²/30)", float(p_S2 - 1) * 1e6),
        ("× (1+ℏ²)(1−ℏ²/30)(1+ℏ²/1260)", float(p_S3 - 1) * 1e6),
    ]

    print(f"  NEUTRON:")
    for label, ppm in n_levels:
        print(f"    {label:<50s} → {ppm:>10.4f} ppm")
    print()
    print(f"  PROTON (reference):")
    for label, ppm in p_levels:
        print(f"    {label:<50s} → {ppm:>10.4f} ppm")
    print()

    # ------------------------------------------------------------------
    # Witness
    # ------------------------------------------------------------------
    w = WitnessBuilder("habiro-neutron-cross-check", engine="mpmath", start_time=_t0)
    w.set_description(
        f"Neutron Habiro bridge cross-check. Neutron hab_A = {mp.nstr(n_hab_A, 15)}, "
        f"tr_M = {mp.nstr(n_tr_M, 15)}. "
        f"Bridge = {mp.nstr(n_bridge, 12)}. "
        f"Ladder: {float(n_S0-1)*1e6:.0f} → {float(n_S1-1)*1e6:.0f} → "
        f"{float(n_S2-1)*1e6:.1f} → {float(n_S3-1)*1e6:.2f} ppm. "
        f"Verdict: {verdict}"
    )
    w.set_audit_only("docs/audits/2026-05-28-habiro-product-correction-7ppm.md")

    w.add_data("neutron", {
        "hab_A_qq": str(mp.nstr(n_hab_A, 20)),
        "hab_B_uu": str(mp.nstr(n_hab_B, 20)),
        "tr_M": str(mp.nstr(n_tr_M, 20)),
        "bridge_ratio": str(mp.nstr(n_bridge, 15)),
        "c3_observed": str(mp.nstr(n_c3, 15)),
        "c3_inv": str(mp.nstr(1 / n_c3, 10)),
        "best_c3_candidate": best_name,
        "best_c3_residual_ppm": best_ppm,
        "ladder_ppm": {
            "level_0_bare": float(n_S0 - 1) * 1e6,
            "level_1_1plus_eps": float(n_S1 - 1) * 1e6,
            "level_2_minus_eps_30": float(n_S2 - 1) * 1e6,
            "level_3_plus_eps_1260": float(n_S3 - 1) * 1e6,
        },
    })
    w.add_data("proton_reference", {
        "hab_A_qq": str(mp.nstr(p_hab_A, 20)),
        "tr_M": str(mp.nstr(p_tr_M, 20)),
        "bridge_ratio": str(mp.nstr(p_bridge, 15)),
        "c3_observed": str(mp.nstr(p_c3, 15)),
        "ladder_ppm": {
            "level_0_bare": float(p_S0 - 1) * 1e6,
            "level_1_1plus_eps": float(p_S1 - 1) * 1e6,
            "level_2_minus_eps_30": float(p_S2 - 1) * 1e6,
            "level_3_plus_eps_1260": float(p_S3 - 1) * 1e6,
        },
    })
    w.add_data("universality", {
        "factor_1_universal": True,
        "factor_2_minus_1_over_30": same_sign_2,
        "factor_3_c3_ratio_n_over_p": float(c3_ratio),
        "c3_within_5pct": same_c3,
        "verdict": verdict,
    })

    # The correction pattern is NOT universal: neutron does not close
    # with (1+ℏ²)(1−ℏ²/30). Assert what we actually found.
    w.add_assertion("proton_bridge_sub_10ppm",
                    computed=1 if abs(float(p_S2 - 1) * 1e6) < 10 else 0,
                    expected=1, tolerance=0,
                    source="Proton (1+ℏ²)(1−ℏ²/30) closes bridge to < 10 ppm (reference)")

    w.add_assertion("neutron_bridge_NOT_sub_10ppm",
                    computed=1 if abs(float(n_S2 - 1) * 1e6) > 100 else 0,
                    expected=1, tolerance=0,
                    source="Neutron (1+ℏ²)(1−ℏ²/30) does NOT close — confirms braid-specificity")

    w.add_assertion("correction_is_braid_specific",
                    computed=1 if abs(float(c3_ratio)) > 10 else 0,
                    expected=1, tolerance=0,
                    source="c₃ differs by >10× between proton and neutron — not universal")

    print(f"  Witness: {w.save()}")


if __name__ == "__main__":
    main()
