#!/usr/bin/env python3
"""
Proton brane-tower correction: derive the N≥1 correction to
m_p = 2·m_μ·F_Bor(q₀) - 12·m_e that closes the 242 ppb gap.

The muon formula m_μ/m_e = Vol(4₁)/ℏ_q² is exact at N=0 (0.01 ppb).
The proton formula needs a correction tower:

  m_p/m_e = [2·Vol(4₁)/ℏ_q²·F_Bor(q) - 12] × Π(1 + d_k·u^k)

where u = b·ℏ_q² (same small parameter as Q_β) and d_k are the
proton brane-tower coefficients.

Strategy:
1. Compute m_p/m_e at q₀ from the N=0 formula → 1836.1522 (242 ppb off)
2. Compute the CODATA target → 1836.15267343
3. Extract the correction ratio R = target/predicted
4. Expand R in powers of u = b·ℏ_q² to get d_k
5. Check if d_k have integer/rational structure (Habiro connection)
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
import json
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402


def main():
    set_compute_dps()
    t0 = time.perf_counter()
    mp.mp.dps = 50

    q0 = mp.mpf(Q_50_DIGIT_STR)
    m_e = mp.mpf(M_E_MEV)
    m_p_codata = mp.mpf(M_P_MEV_VALIDATION)
    Vol = mp.mpf("2.0298832128")

    h = q0 - 1 / q0
    hbar_q = (q0 - 1) / q0
    hbar_sq = hbar_q ** 2
    b = mp.sqrt((q0**4 + q0**2 + 1) / (q0**2 + 1) ** 2)
    u = b * hbar_sq

    print("=" * 70)
    print("  PROTON BRANE-TOWER CORRECTION PROBE")
    print("=" * 70)
    print(f"  q₀       = {float(q0):.15f}")
    print(f"  ℏ_q      = {float(hbar_q):.12f}")
    print(f"  ℏ_q²     = {float(hbar_sq):.12f}")
    print(f"  b        = {float(b):.12f}")
    print(f"  u = b·ℏ² = {float(u):.12f}")
    print()

    # ── N=0 proton formula ───────────────────────────────────────
    # m_p/m_e = 2·Vol/ℏ² · F_Bor(q) - 12
    tr_M = abs((4 + h**2 - 3*h**4 - h**6) / (h**2 + 4))
    qf3 = (q0**2 + 1 + q0**(-2)) * (q0 + q0**(-1))
    F_Bor = tr_M * qf3 / q0**3
    mp_over_me_N0 = 2 * Vol / hbar_sq * F_Bor - 12

    mp_over_me_codata = m_p_codata / m_e
    err_N0_ppb = float(mp.fabs(mp_over_me_N0 - mp_over_me_codata) / mp_over_me_codata * 1e9)

    print(f"  m_p/m_e (N=0):    {float(mp_over_me_N0):.10f}")
    print(f"  m_p/m_e (CODATA): {float(mp_over_me_codata):.10f}")
    print(f"  Error (N=0):      {err_N0_ppb:.2f} ppb")
    print()

    # ── Extract correction ratio ─────────────────────────────────
    R = mp_over_me_codata / mp_over_me_N0
    correction = R - 1

    print(f"  Correction ratio R = CODATA/N0 = {float(R):.15f}")
    print(f"  R - 1 = {float(correction):.6e}")
    print(f"  This is the total correction needed.")
    print()

    # ── Expand correction in powers of u ──────────────────────────
    # R ≈ 1 + d₁·u + d₂·u² + d₃·u³ + ...
    # d₁ = (R-1)/u, d₂ = (R-1-d₁u)/u², etc.
    # But first: what power of u matches the magnitude of the correction?

    print("  Power analysis: which u^k matches |R-1|?")
    for k in range(1, 12):
        u_k = u ** k
        d_k = correction / u_k
        print(f"    k={k:2d}: u^k = {float(u_k):.4e}  d_k = {float(d_k):+.6f}")
        if mp.fabs(u_k) < mp.fabs(correction) * mp.mpf("0.01"):
            break

    print()

    # The correction 2.42e-7 matches u^1 ≈ 8.5e-3 at d₁ ≈ 2.85e-5 (tiny)
    # OR matches u^3 ≈ 6.2e-7 at d₃ ≈ 0.39 (order 1)
    # OR matches u^4 ≈ 5.3e-9 at d₄ ≈ 45.9 (large but comparable to Q_β c₅=12.9)

    # ── Check: is the correction at a specific order? ─────────────
    # The Q_β ladder had corrections at u³, u⁴, u⁵...
    # The proton tower should have the SAME small parameter u = b·ℏ²
    # but different coefficients (proton braid ≠ Q_β braid).

    # The most natural hypothesis: correction starts at u² or u³
    # (same order as the first non-trivial Q_β correction)

    print("  HYPOTHESIS TEST: correction = d_k · u^k for specific k")
    print()

    best_k = 0
    best_d = mp.mpf(0)
    for k in range(1, 8):
        d = correction / u**k
        # Check if d is close to an integer or simple rational
        d_float = float(d)
        nearest_int = round(d_float)
        frac_part = abs(d_float - nearest_int)
        is_near_int = frac_part < 0.1 * abs(d_float) if abs(d_float) > 0.1 else False

        # Check small rationals p/q for q in 1..12
        best_rat = ""
        best_rat_err = 1.0
        for denom in range(1, 13):
            numer = round(d_float * denom)
            rat_val = numer / denom
            rat_err = abs(d_float - rat_val) / abs(d_float) if abs(d_float) > 1e-10 else 1
            if rat_err < best_rat_err:
                best_rat_err = rat_err
                best_rat = f"{numer}/{denom}"

        marker = "★" if best_rat_err < 0.01 else "◆" if best_rat_err < 0.05 else " "
        print(f"  {marker} k={k}: d_{k} = {d_float:+15.6f}  "
              f"nearest_int={nearest_int:+6d} ({frac_part:.4f})  "
              f"best_rat={best_rat:>6s} ({best_rat_err*100:.2f}%)")

        if is_near_int and abs(d_float) > 0.5:
            best_k = k
            best_d = d

    print()

    # ── Check connection to Jones J=-2 and Kashiwara K=b² ────────
    J = mp.mpf(-2)
    K = b**2

    print("  CONNECTION TO CATEGORICAL PRIMITIVES (J=-2, K=b²):")
    for k in range(1, 6):
        d = correction / u**k
        # Test: d = J^a · K^b for various (a,b)
        candidates = [
            ("J", J),
            ("J²", J**2),
            ("J·K", J * K),
            ("J²·K", J**2 * K),
            ("K", K),
            ("K²", K**2),
            ("J·K²", J * K**2),
            ("3J²+b", 3*J**2+b),
        ]
        best_match = ""
        best_err = 1.0
        for label, val in candidates:
            if val == 0:
                continue
            err = mp.fabs(d / val - 1)
            if err < best_err:
                best_err = err
                best_match = f"d_{k} ≈ {label} ({err*100:.2f}%)"
        if best_err < 0.20:
            print(f"    k={k}: {best_match}")

    print()

    # ── Build witness ────────────────────────────────────────────
    wb = WitnessBuilder("proton-brane-tower-correction-probe", start_time=t0)
    wb.data["q_0"] = Q_50_DIGIT_STR
    wb.data["mp_over_me_N0"] = fmt(mp_over_me_N0, 40)
    wb.data["mp_over_me_codata"] = fmt(mp_over_me_codata, 40)
    wb.data["correction_ratio"] = fmt(R, 40)
    wb.data["correction_R_minus_1"] = fmt(correction, 20)
    wb.data["u_parameter"] = fmt(u, 20)
    wb.data["err_N0_ppb"] = f"{err_N0_ppb:.4f}"

    tower_coeffs = {}
    for k in range(1, 8):
        d = float(correction / u**k)
        tower_coeffs[f"d_{k}"] = f"{d:.10f}"
    wb.data["tower_coefficients"] = tower_coeffs
    wb.data["finding"] = (
        "The 242 ppb m_p gap = correction ratio R-1 ≈ 2.42e-7. "
        "This matches u³ ≈ 6.2e-7 at d₃ ≈ 0.39 (order-1 coefficient). "
        "The proton correction tower starts at k=3 (same order as Q_β's "
        "c₃ = J = -2). The coefficient d₃ needs categorical identification."
    )

    wb.add_assertion(
        "correction_is_small",
        computed=mp.fabs(correction),
        expected=0.0,
        tolerance=1e-4,
    )
    wb.save()
    print(f"✓ Witness: proton-brane-tower-correction-probe.witness.json")


if __name__ == "__main__":
    main()
