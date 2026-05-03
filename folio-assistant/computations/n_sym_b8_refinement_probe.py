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
        ("q^(1/12)", q ** mpmath.mpf("1") / 12),
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

    if matches:
        print(f"Closed-form matches at <1e-3:  {matches}")
    else:
        print("No clean closed form at <1e-3 found in this candidate set.")
        print("Next step (research): higher-order corrections (q-Plancherel weights,")
        print("Hochschild cup-product 2-cocycle); see hochschild_h3.py.")

    out = {
        "computation": "n-sym-b8-refinement-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "W-2 candidate (b8) refinement: search for K(q) such that "
            "K(q_0) · [3]_q · [4]_q^3 = N_sym(q_0).  Tests 17 candidate "
            "small q-rational corrections; reports best fit."
        ),
        "q_0_dps": 100,
        "q_0": mpmath.nstr(q, 50),
        "N_sym_target": mpmath.nstr(N_SYM_TARGET, 25),
        "b8_base": mpmath.nstr(base, 25),
        "K_target": mpmath.nstr(K_target, 25),
        "rows": rows,
        "best": best["name"],
        "best_full_N_sym": best["full_N_sym"],
        "best_rel_err": best["rel_err_full"],
    }
    out_path = Path(__file__).parent / "n-sym-b8-refinement-probe.witness.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
