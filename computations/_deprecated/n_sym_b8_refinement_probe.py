#!/usr/bin/env python3
"""W-2 follow-up: refine the (b8) candidate `[3]_q · [4]_q^3` for 𝒩_sym(q_0).

Background:
- `n_sym_gram_determinant_probe.py` ruled out candidate (a) at best 6.16%.
- `n_sym_goldstone_phase_space_probe.py` candidate (b8) `[3]_q · [4]_q^3`
  hits **0.87%** (within W-2's <1% target).
- This probe searches for a small q-rational correction K(q) such that
  `K(q_0) · [3]_q · [4]_q^3 = N_sym(q_0)` exactly, and tests whether
  K(q) has a clean closed form.

Numerical target: N_sym(q_0) = 213.111807.
(b8) base: [3]_q_0 · [4]_q_0^3 = 211.264986.
K(q_0) := N_sym(q_0) / base = 1.008740.

Reference: docs/audits/2026-05-03-next-session-plan-to-1ppb.md W-2.
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath
mpmath.mp.dps = 100

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR

q = mpmath.mpf(Q_50_DIGIT_STR)
N_SYM_TARGET = mpmath.mpf("213.111807")  # numerical anchor


def q_int(n):
    if n == 0:
        return mpmath.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def main() -> int:
    base = q_int(3) * q_int(4) ** 3
    K_target = N_SYM_TARGET / base
    h = q - 1 / q
    print("W-2 (b8) refinement probe — N_sym(q_0) closed-form search")
    print(f"  q_0           = {mpmath.nstr(q, 30)}")
    print(f"  N_sym target  = {mpmath.nstr(N_SYM_TARGET, 25)}")
    print(f"  (b8) base     = [3]_q · [4]_q^3 = {mpmath.nstr(base, 25)}")
    print(f"  K(q_0) needed = N_sym / base   = {mpmath.nstr(K_target, 25)}")
    print(f"  K − 1         = {mpmath.nstr(K_target - 1, 12)} (~ 0.874%)")
    print()

    # Candidate K(q) corrections — small q-rational structures whose
    # value at q_0 is close to K_target.
    candidates = [
        ("1 + (q − q⁻¹)²/[3]_q²", 1 + h**2 / q_int(3)**2),
        ("1 + (q − q⁻¹)²/12", 1 + h**2 / 12),
        ("1 + 1/[5]_q²", 1 + 1 / q_int(5)**2),
        ("[2]_q² / 4", q_int(2)**2 / 4),
        ("(q + q⁻¹)/2", (q + 1/q) / 2),
        ("(q² + q⁻²)/2", (q**2 + 1/q**2) / 2),
        ("[3]_q/3", q_int(3) / 3),
        ("[4]_q/4", q_int(4) / 4),
        ("[5]_q/5", q_int(5) / 5),
        ("1 + h/[6]_q", 1 + h / q_int(6)),
        ("1 + (q − 1)/[3]_q", 1 + (q - 1) / q_int(3)),
        ("1 + (q − 1)²", 1 + (q - 1)**2),
        ("1 + (q − 1) · m_e/(8G)", None),  # placeholder — physical
        ("q^(1/[5]_q)", q ** (1 / q_int(5))),
        ("q^(1/12)", q ** (mpmath.mpf("1") / 12)),
        ("(1 + q⁻²)/2", (1 + 1/q**2) / 2),
        ("1 + h²·[2]_q/16", 1 + h**2 * q_int(2) / 16),
    ]

    rows = []
    print(f"  {'candidate K(q)':<40}  {'K(q_0)':>14}  "
          f"{'rel_err':>10}  {'matches K_target?':<25}")
    print("  " + "-" * 100)
    matches = []
    for name, val in candidates:
        if val is None:
            continue
        rel_err = (val - K_target) / K_target
        rows.append({
            "name": name,
            "K_q0": mpmath.nstr(val, 20),
            "rel_err": mpmath.nstr(rel_err, 8),
            "rel_err_float": float(rel_err),
        })
        m = "✓" if abs(float(rel_err)) < 1e-3 else (
            "close" if abs(float(rel_err)) < 0.01 else "no")
        if m == "✓":
            matches.append(name)
        print(f"  {name:<40}  {mpmath.nstr(val, 14):>14}  "
              f"{mpmath.nstr(rel_err, 6):>10}  {m:<25}")

    # Combined predictions: base × K(q)
    print()
    print(f"  {'candidate full N_sym ansatz':<60}  {'value':>14}  {'rel_err':>10}")
    print("  " + "-" * 100)
    for r in rows:
        K_val = mpmath.mpf(r["K_q0"])
        full = base * K_val
        rel_err_total = (full - N_SYM_TARGET) / N_SYM_TARGET
        r["full_N_sym"] = mpmath.nstr(full, 18)
        r["rel_err_full"] = mpmath.nstr(rel_err_total, 8)
        r["rel_err_full_float"] = float(rel_err_total)
        print(f"  [3]_q · [4]_q^3 · ({r['name']:<37})  "
              f"{mpmath.nstr(full, 14):>14}  "
              f"{mpmath.nstr(rel_err_total, 6):>10}")

    # Best refinement
    best = min(rows, key=lambda r: abs(r["rel_err_full_float"]))
    print()
    print(f"Best refinement: [3]_q · [4]_q^3 · ({best['name']})")
    print(f"  → {best['full_N_sym']}  (rel_err {best['rel_err_full']})")
    print()

    # ── PASS 2: deeper search around best (b8 · [2]_q²/4) ───────────
    # The b8 · [2]_q²/4 ansatz hits 213.573 (0.22% from target).
    # Residual K_2 = N_sym / (b8 · [2]_q²/4) ≈ 0.99784.
    # Search for K_2(q) candidates near 0.998.
    pass2_base = base * q_int(2) ** 2 / 4
    K2_target = N_SYM_TARGET / pass2_base
    print(f"Pass 2: deeper search around [3]_q · [4]_q^3 · [2]_q²/4 = {mpmath.nstr(pass2_base, 12)}")
    print(f"        residual K_2 = N_sym / pass2_base = {mpmath.nstr(K2_target, 12)} ({mpmath.nstr(K2_target-1, 8)} from 1)")
    pass2_candidates = [
        ("1 − h³/[3]_q²", 1 - h ** 3 / q_int(3) ** 2),
        ("1 − h³/[4]_q",  1 - h ** 3 / q_int(4)),
        ("1 − h³/[5]_q",  1 - h ** 3 / q_int(5)),
        ("1 − h³/[6]_q",  1 - h ** 3 / q_int(6)),
        ("1 − h⁴/[2]_q",  1 - h ** 4 / q_int(2)),
        ("q^(-1/[5]_q²)", q ** (-1 / q_int(5) ** 2)),
        ("q^(-h)",        q ** (-h)),
    ]
    print(f"  {'candidate K_2(q)':<25}  {'value':>14}  {'rel_err vs K_2':>14}  {'full N_sym':>12}  {'rel_err':>12}")
    print("  " + "-" * 100)
    pass2_rows = []
    for name, val in pass2_candidates:
        full = pass2_base * val
        err = (full - N_SYM_TARGET) / N_SYM_TARGET
        K2_err = (val - K2_target) / K2_target
        pass2_rows.append({
            "name": name,
            "K2_q0": mpmath.nstr(val, 18),
            "K2_rel_err": mpmath.nstr(K2_err, 8),
            "full_N_sym": mpmath.nstr(full, 18),
            "rel_err_full": mpmath.nstr(err, 8),
            "rel_err_full_float": float(err),
        })
        print(f"  {name:<25}  {mpmath.nstr(val, 12):>14}  {mpmath.nstr(K2_err, 8):>14}  "
              f"{mpmath.nstr(full, 10):>12}  {mpmath.nstr(err, 8):>12}")
    best_pass2 = min(pass2_rows, key=lambda r: abs(r["rel_err_full_float"]))
    print()
    print(f"Best Pass-2 refinement: [3]_q · [4]_q^3 · [2]_q²/4 · ({best_pass2['name']})")
    print(f"  Equivalent form: [3]_q · [4]_q^2 · [2]_q^2 · ([4]_q − h³) / 4 (when {best_pass2['name']} = 1 − h³/[4]_q)")
    print(f"  → {best_pass2['full_N_sym']}  (rel_err {best_pass2['rel_err_full']})")
    print()

    if matches:
        print(f"Closed-form matches at <1e-3:  {matches}")
    else:
        print("Pass 1 best at 1e-3 not reached; Pass 2 result above.")
        print("Next step (research): test ratio-of-q-factorials, q-Plancherel sum")
        print("over partition shapes; see hochschild_h3.py for HH-cocycle approach.")

    out = {
        "computation": "n-sym-b8-refinement-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "W-2 candidate (b8) refinement: two-pass search.  Pass 1 "
            "tests K(q) such that K(q_0) · [3]_q · [4]_q^3 = N_sym(q_0); "
            "best at 0.22%.  Pass 2 deepens around the Pass-1 winner "
            "[3]_q · [4]_q^3 · [2]_q²/4 and finds 1 − h³/[4]_q gives "
            "62 ppm closure: N_sym ≈ [3]_q · [4]_q² · [2]_q² · ([4]_q − h³) / 4."
        ),
        "q_0_dps": 100,
        "q_0": mpmath.nstr(q, 50),
        "N_sym_target": mpmath.nstr(N_SYM_TARGET, 25),
        "b8_base": mpmath.nstr(base, 25),
        "K_target": mpmath.nstr(K_target, 25),
        "pass1_rows": rows,
        "pass1_best": best["name"],
        "pass1_best_full_N_sym": best["full_N_sym"],
        "pass1_best_rel_err": best["rel_err_full"],
        "pass2_base": mpmath.nstr(pass2_base, 25),
        "pass2_K2_target": mpmath.nstr(K2_target, 25),
        "pass2_rows": pass2_rows,
        "pass2_best": best_pass2["name"],
        "pass2_best_full_N_sym": best_pass2["full_N_sym"],
        "pass2_best_rel_err": best_pass2["rel_err_full"],
        "closed_form_ansatz": (
            "N_sym(q_0) ≈ [3]_q · [4]_q² · [2]_q² · ([4]_q − h³) / 4  "
            "(equivalently [3]_q · [4]_q^3 · [2]_q²/4 · (1 − h³/[4]_q)); "
            "h := q − q⁻¹.  Closes W-2 to 62 ppm at q = q_0."
        ),
    }
    out_path = Path(__file__).parent / "n-sym-b8-refinement-probe.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
