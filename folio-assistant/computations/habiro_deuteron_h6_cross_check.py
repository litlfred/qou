#!/usr/bin/env python3
"""Habiro correction tower for the DEUTERON at H_6 (n=6, p(6)=11).

Cross-checks whether the proton pattern
    (1+ℏ²)(1−ℏ²/p(n))
is universal — i.e. whether the deuteron at H_6 uses p(6)=11 the
same way the proton at H_9 uses p(9)=30.

Steps:
  1. Load deuteron Habiro coefficients from the atomic witness.
  2. Compute hab_A (q;q convention) and hab_B (u;u convention).
  3. Compute bridge = hab_A × denom / hab_B (deuteron Markov denominator).
  4. Test (1+ℏ²)(1−ℏ²/11) and search for best second/third factors.
  5. Report whether p(n) universality holds.
"""
from __future__ import annotations
import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402
except ImportError:
    from qou_substrate.constants import Q_50_DIGIT_STR, vol_4_1_at  # noqa: E402


def q_factorial(n, q):
    """[n]_q! = Π_{k=1}^{n} [k]_q."""
    result = mp.mpf(1)
    for k in range(1, n + 1):
        result *= (q**k - q**(-k)) / (q - 1/q)
    return result


def q_integer(k, q):
    """[k]_q = (q^k − q^{-k}) / (q − q^{-1})."""
    return (q**k - q**(-k)) / (q - 1/q)


def poch_qq(m, q):
    """(q;q)_m = Π_{k=1}^{m} (1 − q^k)."""
    p = mp.mpf(1)
    for k in range(1, m + 1):
        p *= (1 - q**k)
    return p


def poch_uu(m, u):
    """(u;u)_m = Π_{k=1}^{m} (1 − u^k)."""
    p = mp.mpf(1)
    for k in range(1, m + 1):
        p *= (1 - u**k)
    return p


def eval_poly_u(expr_str, u_val):
    """Evaluate a polynomial expression string in u at u_val."""
    ns = {"u": u_val, "__builtins__": {}}
    return mp.mpf(eval(expr_str, ns))  # noqa: S307


def main():
    _t0 = time.perf_counter()
    set_compute_dps()
    mp.mp.dps = 50

    q = mp.mpf(Q_50_DIGIT_STR)
    u = mp.sqrt(q)
    hbar_q = (q - 1) / q
    eps = hbar_q**2

    n = 6          # Hecke level for deuteron
    p_n = 11       # p(6) = number of partitions of 6

    vol = vol_4_1_at(50)

    # ------------------------------------------------------------------
    # 1. Load deuteron coefficients
    # ------------------------------------------------------------------
    with open(HERE / "habiro-coefficients-atomic.witness.json") as f:
        data = json.load(f)
    deut = data["results"]["D (deuteron, A=2)"]
    coeffs = deut["habiro_coefficients"]
    denom_expr = deut["denom_in_u"]
    tr_M_stored = mp.mpf(str(deut["tr_M_at_q0"]))

    # ------------------------------------------------------------------
    # 2. Compute hab_A (q;q) and hab_B (u;u)
    # ------------------------------------------------------------------
    hab_A = mp.mpf(0)
    hab_B = mp.mpf(0)

    print("=" * 70)
    print("  Deuteron Habiro correction tower — H₆ cross-check")
    print("=" * 70)
    print()
    print(f"  q₀  = {mp.nstr(q, 15)}")
    print(f"  u₀  = √q₀ = {mp.nstr(u, 15)}")
    print(f"  ℏ²  = {mp.nstr(eps, 15)}")
    print(f"  n   = {n}   (Hecke level)")
    print(f"  p(n)= {p_n}  (partitions of {n})")
    print()

    print(f"  {'m':>2s}  {'a_m(u₀)':>14s}  {'(q;q)_m':>14s}  {'(u;u)_m':>14s}")
    print(f"  {'─'*2}  {'─'*14}  {'─'*14}  {'─'*14}")

    for entry in coeffs:
        m = entry["m"]
        a_val = eval_poly_u(entry["a_m"], u)
        pA = poch_qq(m, q)
        pB = poch_uu(m, u)
        hab_A += a_val * pA
        hab_B += a_val * pB
        print(f"  {m:>2d}  {float(a_val):>14.2f}  {float(pA):>14.6e}  {float(pB):>14.6e}")

    print()

    # ------------------------------------------------------------------
    # 3. Compute bridge = hab_A × denom / hab_B
    # ------------------------------------------------------------------
    denom = eval_poly_u(denom_expr, u)
    tr_M = hab_B / denom

    print(f"  hab_A (q;q convention)  = {mp.nstr(hab_A, 20)}")
    print(f"  hab_B (u;u convention)  = {mp.nstr(hab_B, 20)}")
    print(f"  denom_in_u             = {mp.nstr(denom, 15)}")
    print(f"  tr_M = hab_B / denom   = {mp.nstr(tr_M, 15)}")
    print(f"  tr_M (stored witness)  = {mp.nstr(tr_M_stored, 15)}")
    print()

    bridge = hab_A * denom / hab_B
    print(f"  bridge = hab_A × denom / hab_B = {mp.nstr(bridge, 15)}")
    print()

    # Plancherel and Vol/ℏ² components
    plancherel = mp.factorial(n) / q_factorial(n, q)
    vol_over_hsq = vol / eps

    pred_bare = tr_M * plancherel * vol_over_hsq
    resid_bare = hab_A / pred_bare - 1

    print(f"  Plancherel = n!/[n]_q! = {mp.nstr(plancherel, 15)}")
    print(f"  Vol(4₁)/ℏ²            = {mp.nstr(vol_over_hsq, 15)}")
    print(f"  pred_bare = tr_M × Plancherel × Vol/ℏ²")
    print(f"            = {mp.nstr(pred_bare, 15)}")
    print(f"  bare residual = {float(resid_bare)*1e6:.1f} ppm")
    print()

    # ------------------------------------------------------------------
    # 4. Test (1+ℏ²)(1−ℏ²/p(6)) = (1+ℏ²)(1−ℏ²/11)
    # ------------------------------------------------------------------
    print("-" * 70)
    print("  Testing p(n) universality: (1+ℏ²)(1−ℏ²/11)")
    print("-" * 70)
    print()

    pred_1 = pred_bare * (1 + eps)
    resid_1 = hab_A / pred_1 - 1
    print(f"  After (1+ℏ²):           residual = {float(resid_1)*1e6:.2f} ppm")

    pred_2 = pred_1 * (1 - eps / p_n)
    resid_2 = hab_A / pred_2 - 1
    print(f"  After (1+ℏ²)(1−ℏ²/11):  residual = {float(resid_2)*1e6:.2f} ppm")
    print()

    # Compare with proton pattern
    print(f"  Proton   (n=9): (1+ℏ²)(1−ℏ²/30) → 7.8 ppm")
    print(f"  Deuteron (n=6): (1+ℏ²)(1−ℏ²/11) → {abs(float(resid_2)*1e6):.2f} ppm")
    print()

    # ------------------------------------------------------------------
    # 5. Search for best second and third factors
    # ------------------------------------------------------------------
    print("-" * 70)
    print("  Exhaustive search: best second factor (1−ℏ²/X)")
    print("-" * 70)
    print()

    # Scan second factor: (1+ℏ²)(1−ℏ²/X) for many X
    second_candidates = []
    for denom_x in range(2, 200):
        pred_try = pred_1 * (1 - eps / denom_x)
        resid_try = hab_A / pred_try - 1
        ppm = abs(float(resid_try) * 1e6)
        second_candidates.append((denom_x, ppm, float(resid_try) * 1e6))

    second_candidates.sort(key=lambda x: x[1])

    print(f"  {'X':>5s}  {'Residual':>12s}  {'Note':>15s}")
    print(f"  {'─'*5}  {'─'*12}  {'─'*15}")
    for x, ppm, raw in second_candidates[:15]:
        sign = "+" if raw > 0 else "−"
        note = " ← p(6)" if x == 11 else ""
        print(f"  {x:>5d}  {sign}{ppm:>10.2f} ppm  {note}")

    best_x = second_candidates[0][0]
    print()
    print(f"  Best X = {best_x}")
    rank_p6 = next(i for i, (x, _, _) in enumerate(second_candidates) if x == p_n) + 1
    print(f"  p(6) = 11 ranks #{rank_p6} among integer denominators")
    print()

    # Use the best second factor for the third-factor search
    pred_2_best = pred_1 * (1 - eps / best_x)
    S2_best = hab_A / pred_2_best
    c3_obs = (S2_best - 1) / eps

    # Also compute c3 from the p(n) second factor
    S2_pn = hab_A / pred_2
    c3_pn = (S2_pn - 1) / eps

    print("-" * 70)
    print("  Third factor search (after p(n) second factor)")
    print("-" * 70)
    print()
    print(f"  c₃ = (S₂−1)/ℏ² = {mp.nstr(c3_pn, 15)}")
    print()

    # Scan simple third factors
    third_candidates = []
    for a in range(-10, 11):
        for b in range(-10, 11):
            for c_d in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20,
                        22, 24, 30, 33, 44, 55, 60, 66, 77, 88, 99, 110,
                        120, 121, 132, 180, 220, 330, 360, 440, 660, 720,
                        990, 1260, 1320]:
                val = mp.mpf(a * n + b) / c_d
                if abs(float(val)) > 0.02:
                    continue
                pred_try = pred_2 * (1 + val * eps)
                resid = hab_A / pred_try - 1
                ppm = abs(float(resid) * 1e6)
                if ppm < 10:
                    third_candidates.append((f"({a}·{n}+{b})/{c_d}", val, ppm, resid))

    # Also try algebraic expressions involving p(n), n², etc.
    special_vals = [
        ("1/p(n)²", mp.mpf(1) / p_n**2),
        ("1/(2·p(n)²)", mp.mpf(1) / (2 * p_n**2)),
        ("1/(n·p(n))", mp.mpf(1) / (n * p_n)),
        ("(n-1)/(n·p(n)²)", mp.mpf(n - 1) / (n * p_n**2)),
        ("1/(n²·p(n))", mp.mpf(1) / (n**2 * p_n)),
        ("1/(n³)", mp.mpf(1) / n**3),
        ("1/(n²)", mp.mpf(1) / n**2),
        ("1/(2·n·p(n))", mp.mpf(1) / (2 * n * p_n)),
        ("(n+1)/(n·p(n)²)", mp.mpf(n + 1) / (n * p_n**2)),
        ("1/[6]_q²", 1 / q_integer(6, q)**2),
        ("1/(p(n)·[n]_q)", 1 / (p_n * q_integer(n, q))),
        ("n/(2·p(n)²)", mp.mpf(n) / (2 * p_n**2)),
    ]
    for name, val in special_vals:
        pred_try = pred_2 * (1 + val * eps)
        resid = hab_A / pred_try - 1
        ppm = abs(float(resid) * 1e6)
        third_candidates.append((name, val, ppm, resid))

    third_candidates.sort(key=lambda x: x[2])

    print(f"  {'Expression':<25s} {'Value':>14s} {'Residual':>10s}")
    print(f"  {'─'*25} {'─'*14} {'─'*10}")
    for name, val, ppm, resid in third_candidates[:20]:
        sign = "+" if float(resid) > 0 else "−"
        print(f"  {name:<25s} {mp.nstr(val, 8):>14s} {sign}{ppm:>8.3f} ppm")

    print()

    # PSLQ on c₃
    print("-" * 70)
    print("  PSLQ search for c₃ (deuteron)")
    print("-" * 70)
    print()

    basis = [
        mp.mpf(1),
        c3_pn,
        mp.mpf(1) / n,
        mp.mpf(1) / n**2,
        mp.mpf(1) / n**3,
        mp.mpf(1) / p_n,
        mp.mpf(1) / p_n**2,
        mp.mpf(1) / (n * p_n),
    ]
    labels = ["1", "c₃", "1/n", "1/n²", "1/n³", "1/p(n)", "1/p(n)²", "1/(n·p(n))"]

    pslq_result_str = None
    try:
        rel = mp.pslq(basis, maxcoeff=2000)
        if rel:
            terms = []
            for i, c in enumerate(rel):
                if c != 0:
                    terms.append(f"{c}·{labels[i]}")
            pslq_result_str = " + ".join(terms) + " = 0"
            print(f"  PSLQ: {pslq_result_str}")

            if rel[1] != 0:
                c3_exact = mp.mpf(0)
                for i, c in enumerate(rel):
                    if i != 1:
                        c3_exact -= mp.mpf(c) / rel[1] * basis[i]
                print(f"  → c₃ = {mp.nstr(c3_exact, 15)}")
                print(f"  Observed: {mp.nstr(c3_pn, 15)}")
                print(f"  Match: {abs(float(c3_pn - c3_exact))*1e6:.4f} ppm")
        else:
            print("  PSLQ: no relation found")
            pslq_result_str = "no relation found"
    except Exception as e:
        print(f"  PSLQ: {e}")
        pslq_result_str = f"error: {e}"

    print()

    # ------------------------------------------------------------------
    # 6. Correction ladder summary
    # ------------------------------------------------------------------
    print("=" * 70)
    print("  CORRECTION LADDER — DEUTERON")
    print("=" * 70)
    print()

    best_c3 = third_candidates[0] if third_candidates else None

    stages = [
        ("bare (tr_M × Plancherel × Vol/ℏ²)", pred_bare),
        ("×(1+ℏ²)", pred_1),
        (f"×(1+ℏ²)(1−ℏ²/{p_n})  [p({n})={p_n}]", pred_2),
    ]
    if best_c3:
        stages.append(
            (f"×...×(1+{best_c3[0]}·ℏ²)", pred_2 * (1 + best_c3[1] * eps))
        )

    for name, pred in stages:
        r = hab_A / pred - 1
        print(f"  {name:<45s} → {float(r)*1e6:>10.2f} ppm")
    print()

    # ------------------------------------------------------------------
    # Universality assessment
    # ------------------------------------------------------------------
    print("=" * 70)
    print("  p(n) UNIVERSALITY ASSESSMENT")
    print("=" * 70)
    print()

    # Compare patterns
    print(f"  Proton   H₉:  (1+ℏ²)(1−ℏ²/p(9))  p(9)=30")
    print(f"    bare → first factor → second factor → third factor")
    print(f"    9495 → −319 → 7.8 → 0.002 ppm  [c₃ = 1/1260]")
    print()
    print(f"  Deuteron H₆:  (1+ℏ²)(1−ℏ²/p(6))  p(6)=11")
    deut_bare_ppm = float(resid_bare) * 1e6
    deut_f1_ppm = float(resid_1) * 1e6
    deut_f2_ppm = float(resid_2) * 1e6
    best_c3_ppm = best_c3[2] if best_c3 else float('inf')
    best_c3_name = best_c3[0] if best_c3 else "N/A"
    print(f"    {deut_bare_ppm:.1f} → {deut_f1_ppm:.2f} → {deut_f2_ppm:.2f}"
          f" → {best_c3_ppm:.3f} ppm  [c₃ = {best_c3_name}]")
    print()

    # Is p(n) the best integer denominator?
    is_pn_best = (best_x == p_n)
    is_pn_top3 = rank_p6 <= 3
    print(f"  Is p(n) the best integer denominator?  {'YES' if is_pn_best else 'NO'}"
          f"  (rank #{rank_p6})")
    if is_pn_best:
        print(f"  → p(n) universality CONFIRMED for the deuteron")
    elif is_pn_top3:
        print(f"  → p(n) is near-optimal (rank #{rank_p6}), pattern plausibly universal")
    else:
        print(f"  → p(n) is rank #{rank_p6}; best X={best_x}.")
        print(f"    Pattern may be proton-specific or require A-dependent correction.")
    print()

    # ------------------------------------------------------------------
    # Witness
    # ------------------------------------------------------------------
    w = WitnessBuilder("habiro-deuteron-h6-cross-check", engine="mpmath")
    w._start_time = _t0
    w.set_description(
        f"Deuteron Habiro correction tower at H_{n} (n={n}, p({n})={p_n}). "
        f"Tests whether the proton pattern (1+ℏ²)(1−ℏ²/p(n)) is universal. "
        f"Ladder: {deut_bare_ppm:.0f} → {deut_f1_ppm:.1f} → {deut_f2_ppm:.1f}"
        f" → {best_c3_ppm:.3f} ppm. "
        f"p({n})={p_n} ranks #{rank_p6} among integer denominators."
    )
    w.add_data("isotope", "deuteron")
    w.add_data("hecke_level", n)
    w.add_data("partition_number", p_n)
    w.add_data("hab_A_qq", str(mp.nstr(hab_A, 20)))
    w.add_data("hab_B_uu", str(mp.nstr(hab_B, 20)))
    w.add_data("denom_in_u_evaluated", str(mp.nstr(denom, 15)))
    w.add_data("tr_M_computed", str(mp.nstr(tr_M, 15)))
    w.add_data("tr_M_stored", str(mp.nstr(tr_M_stored, 15)))
    w.add_data("bridge", str(mp.nstr(bridge, 15)))
    w.add_data("ladder", {
        "bare_ppm": deut_bare_ppm,
        "after_1_plus_eps_ppm": deut_f1_ppm,
        "after_pn_factor_ppm": deut_f2_ppm,
        "after_third_factor_ppm": best_c3_ppm,
        "third_factor_expression": best_c3_name,
    })
    w.add_data("pn_rank_among_integers", rank_p6)
    w.add_data("best_integer_denominator", best_x)
    w.add_data("c3_observed", str(mp.nstr(c3_pn, 15)))
    w.add_data("pslq_result", pslq_result_str)
    w.add_data("proton_comparison", {
        "proton_n": 9,
        "proton_pn": 30,
        "proton_ladder_ppm": [9495, -319, 7.8, 0.002],
        "proton_c3": "1/1260",
    })

    w.add_assertion("first_factor_improves",
                    computed=1 if abs(deut_f1_ppm) < abs(deut_bare_ppm) else 0,
                    expected=1, tolerance=0,
                    source="(1+ℏ²) improves bare prediction")
    w.add_assertion("pn_factor_improves",
                    computed=1 if abs(deut_f2_ppm) < abs(deut_f1_ppm) else 0,
                    expected=1, tolerance=0,
                    source=f"(1−ℏ²/{p_n}) further improves after (1+ℏ²)")
    w.add_assertion("pn_in_top5",
                    computed=1 if rank_p6 <= 5 else 0,
                    expected=1, tolerance=0,
                    source=f"p({n})={p_n} is among top-5 integer denominators")

    witness_path = w.save()
    print(f"  Witness: {witness_path}")


if __name__ == "__main__":
    main()
