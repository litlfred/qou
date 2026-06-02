#!/usr/bin/env python3
"""
cl3_zeta5_orbit_sum.py — Cl_3(2π/5) + Cl_3(4π/5) = -(12/25) ζ(3).

Verifies, at 50 decimal digits via mpmath, the orbit-sum identity

    Cl_3(2π/5) + Cl_3(4π/5)  =  -(12/25) · ζ(3)

derived from:

  - The classical multiplication formula (5th-roots-of-unity case):
        Σ_{k=1..4} Li_3(ζ_5^k) = (5^{-2} - 1) · ζ(3) = -(24/25) · ζ(3)
  - Reality + Cl_3 evenness + Cl_3(2π - θ) = Cl_3(θ):
        Re side gives 2 (Cl_3(2π/5) + Cl_3(4π/5)) = -(24/25) ζ(3)

**Significance for B1**: combined with round 10's
Im Li_3(ζ_5) = 4π³/125 (Tate-rational), this further reduces the
2-dim Bring trilog content. The 2-dim Borel-rank space for
K_5^ind(Q(ζ_5)) ⊗ Q decomposes as:

  - 1 dim: ζ(3)-line (Tate-trace from K_5(Z); already external,
           classical depth-3 period)
  - 1 dim: Cl_3(2π/5) - Cl_3(4π/5) (the "antisymmetric" combination
           under the ζ_5 ↔ ζ_5^2 Galois automorphism — the
           genuinely-new depth-3 generator)

So the SHARP open content at depth 3 over Q(ζ_5) is just **one**
real number: Cl_3(2π/5) - Cl_3(4π/5) ≈ 0.18937 - (-0.766) ≈ 0.955.

Output: cl3-zeta5-orbit-sum.witness.json next to this file.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import time
from datetime import datetime, timezone

from mpmath import mp, mpf, mpc, pi, exp, polylog, re, im, zeta
from mpmath import fabs as mpabs

from witness_base import WitnessBuilder

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()


def main() -> None:
    # Capture start time BEFORE the heavy computation so the witness's
    # `durationMs` reflects real runtime (Copilot PR #635 review).
    start = time.monotonic()

    # ── inputs ────────────────────────────────────────────────────
    ZETA_5 = exp(mpc(0, 1) * 2 * pi / mpf(5))
    ZETA_5_SQ = ZETA_5 ** 2

    # ── compute Cl_3(2π/5) and Cl_3(4π/5) directly ──────────────
    CL_3_2PI5 = re(polylog(3, ZETA_5))
    CL_3_4PI5 = re(polylog(3, ZETA_5_SQ))

    # ── orbit sum identity: 2 (Cl_3(2π/5) + Cl_3(4π/5)) = -24 ζ(3) / 25
    ZETA_3 = zeta(3)
    PREDICTED_ORBIT_SUM = -mpf(12) * ZETA_3 / mpf(25)

    ACTUAL_ORBIT_SUM = CL_3_2PI5 + CL_3_4PI5
    ORBIT_SUM_RESIDUAL = mpabs(ACTUAL_ORBIT_SUM - PREDICTED_ORBIT_SUM)

    # ── antisymmetric (genuinely-new depth-3) generator ─────────
    CL_3_DIFFERENCE = CL_3_2PI5 - CL_3_4PI5

    print("=" * 72)
    print("Cl_3 orbit-sum identity at ζ_5 — depth-3 reduction")
    print("=" * 72)
    print(f"Cl_3(2π/5) = Re Li_3(ζ_5)        = {CL_3_2PI5}")
    print(f"Cl_3(4π/5) = Re Li_3(ζ_5²)       = {CL_3_4PI5}")
    print()
    print(f"Sum (actual):  Cl_3(2π/5) + Cl_3(4π/5) = {ACTUAL_ORBIT_SUM}")
    print(f"Predicted: -(12/25) · ζ(3)             = {PREDICTED_ORBIT_SUM}")
    print(f"Residual                                = {ORBIT_SUM_RESIDUAL}")
    print(f"Residual < 1e-40                       = "
          f"{float(ORBIT_SUM_RESIDUAL) < 1e-40}")
    print()
    print(f"Antisymmetric (genuinely-new depth-3 generator):")
    print(f"  Cl_3(2π/5) - Cl_3(4π/5) = {CL_3_DIFFERENCE}")
    print()
    print("Interpretation:")
    print("  2-dim K_5^ind(Q(ζ_5)) ⊗ Q (Borel rank 2) splits as:")
    print("    (a) ζ(3)-line: 1-dim, classical (Apéry's constant)")
    print("    (b) Cl_3(2π/5) - Cl_3(4π/5)-line: 1-dim, genuinely")
    print("        new depth-3 element for B1 over Q(ζ_5).")
    print()
    print("  Sharp open content at depth 3 over Q(ζ_5):")
    print("    JUST ONE real number ≈ 0.955.")

    witness = {
        "computation": "cl3-zeta5-orbit-sum",
        "description": (
            "Verification at 50 decimal digits of the orbit-sum "
            "identity Cl_3(2π/5) + Cl_3(4π/5) = -(12/25) ζ(3), "
            "derived from the multiplication formula Σ Li_3(ζ_5^k) "
            "= -(24/25) ζ(3) restricted to real parts. Together "
            "with prop:bring-trilog-imaginary-tate-rational (round "
            "10), reduces the 2-dim Bring trilog content to: "
            "ζ(3)-line (classical) ⊕ Cl_3(2π/5)-Cl_3(4π/5) "
            "(genuinely new, 1 real number)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "precision_decimal_digits": mp.dps,
        "cl_3_values": {
            "cl_3_2pi_5": str(CL_3_2PI5),
            "cl_3_4pi_5": str(CL_3_4PI5),
        },
        "orbit_sum_identity": {
            "claim": "Cl_3(2π/5) + Cl_3(4π/5) = -(12/25) · ζ(3)",
            "actual_str": str(ACTUAL_ORBIT_SUM),
            "predicted_str": str(PREDICTED_ORBIT_SUM),
            "residual_str": str(ORBIT_SUM_RESIDUAL),
            "residual_below_1e_40": float(ORBIT_SUM_RESIDUAL) < 1e-40,
        },
        "zeta_3_str": str(ZETA_3),
        "antisymmetric_generator": {
            "expression": "Cl_3(2π/5) - Cl_3(4π/5)",
            "value_str": str(CL_3_DIFFERENCE),
            "interpretation": (
                "The genuinely-new depth-3 element for B1 over "
                "Q(ζ_5). Lives in P_3 / (P_2 + ζ(3)·Q + Tate)."
            ),
        },
        "borel_rank_2_decomposition": {
            "tate_dim": 1,
            "tate_generator": "ζ(3) (or equivalently the orbit-sum)",
            "new_dim": 1,
            "new_generator": "Cl_3(2π/5) - Cl_3(4π/5)",
            "total_dim": 2,
            "matches_borel_rank": True,
        },
        "sharp_open_content_at_depth_3_over_zeta5": (
            "ONE real number: Cl_3(2π/5) - Cl_3(4π/5) ≈ 0.955. "
            "Whether this admits a closed form modulo lower-weight "
            "stuff is open (no Goncharov/Bloch-Suslin reduction "
            "beyond round 10's reflection-formula result)."
        ),
    }
    # WitnessBuilder.wrap_legacy preserves on-disk layout while adding
    # canonical metadata (scriptHash, commitSha, computedAt, etc.).
    # `_start_time` override captures real compute runtime per
    # Copilot PR #635 review.
    builder = WitnessBuilder.wrap_legacy(
        "cl3-zeta5-orbit-sum",
        witness,
        script_path=__file__,
        engine="mpmath",
        start_time=start,
    )
    out = builder.save()
    print(f"\nwitness: {out}")


if __name__ == "__main__":
    main()
