#!/usr/bin/env python3
"""
kummer_reflection_zeta5.py — Kummer reflection formula verification at ζ_5.

Verifies, at 50 decimal digits via mpmath, the closed-form identity

    Im Li_3(ζ_5) = S_3(2π/5) = 4π³ / 125

obtained from the **Kummer reflection formula** for Li_3 (Lewin,
"Polylogarithms and Associated Functions", Eq. 6.10):

    Li_3(z) - Li_3(1/z) = -log³(-z) / 6 - π² log(-z) / 6.

For z = ζ_5 = exp(2πi/5):
  - LHS = 2i · Im Li_3(ζ_5) = 2i · S_3(2π/5)
  - RHS uses log(-ζ_5) = -3iπ/5 (principal branch on (-π, π])
  - Computation: RHS = 8iπ³/125
  - Hence S_3(2π/5) = 4π³/125 — a Tate-rational depth-3 number.

**Significance for B1**: this closed form means the imaginary part
of Li_3(ζ_5) is Tate-rational (lies in the (2πi)^3 · ℚ-line of
P_3), and projects to zero under the Beilinson regulator quotient
P_3 → P_3 / (Tate). Thus only the real part Cl_3(2π/5) carries
genuinely new depth-3 information for the keystone B1.

Output: kummer-reflection-zeta5.witness.json next to this file.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import time
from datetime import datetime, timezone

from mpmath import mp, mpf, mpc, pi, exp, polylog, im, re, log
from mpmath import fabs as mpabs

from witness_base import WitnessBuilder

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()


def main() -> None:
    # Capture start time BEFORE the heavy computation so the
    # witness's `durationMs` reflects real runtime (Copilot PR #635
    # review: `WitnessBuilder` constructed only at save would record
    # near-zero duration).
    start = time.monotonic()

    # ── Inputs ────────────────────────────────────────────────────
    ZETA_5 = exp(mpc(0, 1) * 2 * pi / mpf(5))

    # ── Direct computation of Im Li_3(ζ_5) ──────────────────────
    LI_3_ZETA_5 = polylog(3, ZETA_5)
    S_3_DIRECT = im(LI_3_ZETA_5)

    # ── Closed-form computation: 4 π³ / 125 ─────────────────────
    S_3_CLOSED_FORM = 4 * pi ** 3 / mpf(125)

    # ── Kummer reflection: independent path via the formula ─────
    # log(-ζ_5) = log(exp(i(2π/5 + π))) — principal branch:
    # arg = 2π/5 + π = 7π/5 > π, subtract 2π → -3π/5.
    LOG_NEG_ZETA5 = mpc(0, -3 * pi / mpf(5))

    # RHS of Kummer: -log³(-z)/6 - π² log(-z)/6
    RHS_KUMMER = (
        -LOG_NEG_ZETA5 ** 3 / mpf(6)
        - pi ** 2 * LOG_NEG_ZETA5 / mpf(6)
    )

    # LHS of Kummer: Li_3(z) - Li_3(1/z) = 2i · Im Li_3(z)
    LHS_KUMMER = LI_3_ZETA_5 - polylog(3, 1 / ZETA_5)

    KUMMER_RESIDUAL = mpabs(LHS_KUMMER - RHS_KUMMER)

    # ── Closed-form vs direct cross-check ───────────────────────
    CLOSED_VS_DIRECT_RESIDUAL = mpabs(S_3_DIRECT - S_3_CLOSED_FORM)

    print("=" * 72)
    print("Kummer reflection at ζ_5 — depth-3 imaginary-part closed form")
    print("=" * 72)
    print(f"ζ_5 = exp(2πi/5)")
    print(f"   = {ZETA_5}")
    print()
    print(f"Direct: Im Li_3(ζ_5)           = {S_3_DIRECT}")
    print(f"Closed form: 4π³ / 125         = {S_3_CLOSED_FORM}")
    print(f"Closed-vs-direct residual      = {CLOSED_VS_DIRECT_RESIDUAL}")
    print(f"residual < 1e-40               = "
          f"{float(CLOSED_VS_DIRECT_RESIDUAL) < 1e-40}")
    print()
    print(f"Kummer reflection formula check:")
    print(f"  log(-ζ_5) [principal]        = {LOG_NEG_ZETA5}")
    print(f"  LHS = Li_3(ζ_5) - Li_3(ζ_5⁻¹) = {LHS_KUMMER}")
    print(f"  RHS = -log³(-z)/6 - π²log(-z)/6 = {RHS_KUMMER}")
    print(f"  residual = |LHS - RHS|        = {KUMMER_RESIDUAL}")
    print(f"  residual < 1e-40              = "
          f"{float(KUMMER_RESIDUAL) < 1e-40}")
    print()
    print("Interpretation:")
    print("  Im Li_3(ζ_5) = 4π³/125 — Tate-rational, lives in")
    print("  (2πi)³ · ℚ ⊂ Tate(3). Projects to ZERO under the")
    print("  Beilinson regulator quotient P_3 → P_3/Tate.")
    print()
    print("  Hence only Re Li_3(ζ_5) = Cl_3(2π/5) ≈ 0.18937...")
    print("  carries genuinely new depth-3 information for B1's")
    print("  Bring trilog row.")

    witness = {
        "computation": "kummer-reflection-zeta5",
        "description": (
            "Verification at 50 decimal digits of the Kummer "
            "reflection formula Li_3(z) - Li_3(1/z) = -log³(-z)/6 "
            "- π²log(-z)/6 evaluated at z = ζ_5 = exp(2πi/5). "
            "Yields the closed form Im Li_3(ζ_5) = 4π³/125 — a "
            "Tate-rational depth-3 number, projecting to zero "
            "under the Beilinson regulator quotient. Sharpening "
            "of conj:bring-trilog-depth-3-witness: only the real "
            "part Cl_3(2π/5) is the genuinely new depth-3 element."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "precision_decimal_digits": mp.dps,
        "input": {
            "z": "ζ_5 = exp(2πi/5)",
            "z_str": str(ZETA_5),
        },
        "closed_form": {
            "expression": "4 π³ / 125",
            "value_str": str(S_3_CLOSED_FORM),
            "tate_class": "Tate(3) = (2πi)³ · ℚ",
        },
        "direct_polylog": {
            "expression": "Im Li_3(ζ_5)",
            "value_str": str(S_3_DIRECT),
            "method": "mpmath.polylog at 50 dps",
        },
        "closed_vs_direct_residual": str(CLOSED_VS_DIRECT_RESIDUAL),
        "closed_vs_direct_below_1e_40":
            float(CLOSED_VS_DIRECT_RESIDUAL) < 1e-40,
        "kummer_formula_check": {
            "log_neg_zeta5_principal_str": str(LOG_NEG_ZETA5),
            "lhs_str": str(LHS_KUMMER),
            "rhs_str": str(RHS_KUMMER),
            "residual_str": str(KUMMER_RESIDUAL),
            "residual_below_1e_40": float(KUMMER_RESIDUAL) < 1e-40,
        },
        "interpretation": (
            "Im Li_3(ζ_5) is Tate-rational (4π³/125), in (2πi)³·ℚ. "
            "Under Beilinson's regulator quotient P_3 → P_3/Tate, "
            "this component vanishes. Only Re Li_3(ζ_5) = Cl_3(2π/5) "
            "≈ 0.18937 carries genuinely new depth-3 information. "
            "Reduces the 2-dim Bring trilog content to the single "
            "real-part component for the regulator image."
        ),
        "consequence_for_b1": (
            "The 2-dim K_5^ind(Q(ζ_5)) ⊗ Q (Borel rank 2) has its "
            "Beilinson regulator image generated by Re Li_3(ζ_5^k) "
            "for k = 1, 2 (one independent value mod orbit-sum, "
            "with conjugate pair Re Li_3(ζ_5^4) = Re Li_3(ζ_5)). "
            "Dim 2 confirmed by Galois-orbit + reality constraint."
        ),
    }
    # WitnessBuilder.wrap_legacy preserves on-disk layout while adding
    # canonical metadata (scriptHash, commitSha, computedAt, etc.).
    # Override `_start_time` with the main() entry time so `durationMs`
    # reflects the real compute runtime, not just the save step
    # (Copilot PR #635 review).
    builder = WitnessBuilder.wrap_legacy(
        "kummer-reflection-zeta5",
        witness,
        script_path=__file__,
        engine="mpmath",
        start_time=start,
    )
    out = builder.save()
    print(f"\nwitness: {out}")


if __name__ == "__main__":
    main()
