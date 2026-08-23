"""qbeta_sdp_normalization_zero_probe — task 2 of kernel deepening.

Tests the #1823-scope INTERPRETIVE synthesis (explicitly flagged "NOT yet
derived"): is the residue-A pole at `u_substrate` a **zero of the SDP
normalization `Q_A·cos α_eff`**?

The compute defines (qbeta_decay_sdp_full_ck.py):
    Q_A·cos α_eff = Q_N2 / N2,   N2 = 1 - b²·ℏ_q⁴ = 1 - u²,   u = b·ℏ_q².
So as a function of `u`:
    * a ZERO of `Q_A·cos` requires `Q_N2 = 0` (its numerator);
    * a POLE of `Q_A·cos` is the zero of `N2 = 1 - u²`, i.e. `u = ±1`.

The ladder object is `R(u) = Q_β / (Q_A·cos) = Q_AME·(1-u²)/Q_N2`, whose pole
(if any, as a u-function) would sit where `Q_N2 = 0`. The probe checks whether
ANY of these singularities lands at `u_substrate ≈ 0.0085` — the established
residue-A pole location (radius of convergence = u_substrate, PR #1713/#1727).

EXPECTED (honest pre-registration): the `N2` pole is at `u = ±1`, ~117× farther
than `u_substrate`; `Q_A·cos(u_substrate) ≠ 0`. So the *literal* SDP-cos-factor
does NOT singularize at u_substrate — which would REFUTE the literal synthesis
and localise the pole to the c_k Habiro-ladder structure (the geometric growth
ratio `c_{k+1}/c_k → 1/u_substrate`), not the cos-correction normalization.

Diagnostic-only; no fitting; no production wiring.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

set_compute_dps()

HERE = Path(__file__).resolve().parent


def main() -> int:
    print("=" * 78)
    print("Q_β SDP-normalization zero probe — is the pole a zero of Q_A·cos α_eff?")
    print("=" * 78)

    src = HERE.parent / "q-beta-operator-valued-N3.witness.json"
    data = record_upstream(src, _UPSTREAM_RECORDS)["data"]
    b = mp.mpf(str(data["hoefsmit_b"]))
    hbar_q_sq = mp.mpf(str(data["hbar_q_sq"]))
    Q_N2 = mp.mpf(str(data["Q_N2"]))
    Q_AME = mp.mpf(str(data["Q_AME"]))

    u_sub = b * hbar_q_sq
    N2 = 1 - u_sub ** 2                      # = 1 - b²ℏ_q⁴
    Q_A_cos = Q_N2 / N2
    R = Q_AME / Q_A_cos

    print(f"\n  u_substrate = b·ℏ_q²       = {mp.nstr(u_sub, 12)}")
    print(f"  N2 = 1 - u²                = {mp.nstr(N2, 14)}")
    print(f"  Q_N2 (SDP norm numerator)  = {mp.nstr(Q_N2, 14)}")
    print(f"  Q_A·cos α_eff = Q_N2/N2    = {mp.nstr(Q_A_cos, 14)}")
    print(f"  R = Q_β/(Q_A·cos)          = {mp.nstr(R, 16)}")

    # ── Singularity-location tests ──────────────────────────────────────
    # 1. Pole of Q_A·cos = zero of N2 = 1 - u²  ⇒  u = ±1.
    pole_u = mp.mpf(1)                       # nearest |u| with N2 = 0
    pole_dist = abs(pole_u - u_sub)
    pole_ratio = pole_dist / u_sub
    print(f"\n--- Singularity of the SDP cos-factor (N2 = 1 - u²) ---")
    print(f"  N2 = 0 at u = ±1; distance to u_substrate = {mp.nstr(pole_dist, 8)} "
          f"= {mp.nstr(pole_ratio, 6)}× u_substrate")
    print(f"  ⇒ the N2 pole is ~{mp.nstr(pole_ratio, 4)}× farther than the "
          f"residue-A pole location.")

    # 2. Is Q_A·cos (or its numerator Q_N2) zero at u_substrate? No.
    qacos_near_zero = abs(Q_A_cos) < mp.mpf("1e-6")
    qn2_near_zero = abs(Q_N2) < mp.mpf("1e-6")
    print(f"\n--- Is Q_A·cos α_eff (or Q_N2) ≈ 0 at u_substrate? ---")
    print(f"  Q_A·cos(u_substrate) = {mp.nstr(Q_A_cos, 10)}  → ≈0? {qacos_near_zero}")
    print(f"  Q_N2(u_substrate)    = {mp.nstr(Q_N2, 10)}  → ≈0? {qn2_near_zero}")

    # ── Verdict ─────────────────────────────────────────────────────────
    refuted = (not qacos_near_zero) and (pole_ratio > mp.mpf("10"))
    print("\n" + "=" * 78)
    print("VERDICT (task 2):")
    if refuted:
        print("  • SDP-cos-factor-zero synthesis REFUTED in its LITERAL form.")
        print(f"    Q_A·cos α_eff = Q_N2/(1-u²) is smooth and nonzero at "
              f"u_substrate;")
        print(f"    its only singularity (N2=0 at u=±1) is ~{mp.nstr(pole_ratio,4)}× "
              f"farther.")
        print("  • So the u_substrate pole is NOT the Q_A·cos α_eff normalization")
        print("    zero — it is INTRINSIC to the c_k Habiro ladder (the geometric")
        print("    growth c_{k+1}/c_k → 1/u_substrate, PR #1713). This narrows the")
        print("    keystone: the pole lives in Q_N2's deeper Habiro structure /")
        print("    the c_11+ extraction, not the documented cos-correction factor.")
        print("  • Refines the #1823 'SDP shadow-price' synthesis (which was")
        print("    flagged NOT-yet-derived): the literal cos-factor reading is out.")
    else:
        print("  • Q_A·cos α_eff DOES approach zero near u_substrate — synthesis")
        print("    SUPPORTED; cross-anchor + derive before any claim.")
    print()

    w = WitnessBuilder("qbeta-sdp-normalization-zero-probe", engine="mpmath")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        f"Task-2 (kernel deepening): tests whether the residue-A pole at "
        f"u_substrate is a zero of the SDP normalization Q_A·cos α_eff = "
        f"Q_N2/(1-u²). Result: REFUTED in literal form — Q_A·cos(u_substrate) = "
        f"{mp.nstr(Q_A_cos,6)} ≠ 0, and its only singularity (N2=0 at u=±1) is "
        f"~{mp.nstr(pole_ratio,4)}× farther than u_substrate. So the pole is "
        f"INTRINSIC to the c_k Habiro ladder (radius = u_substrate, PR #1713), "
        f"not the cos-correction factor. Refines the #1823 SDP-shadow-price "
        f"synthesis (flagged not-yet-derived): the literal cos-factor reading is "
        f"out; the keystone is Q_N2's deeper Habiro structure / c_11+. "
        f"Diagnostic-only."
    )
    w.add_data("u_substrate", mp.nstr(u_sub, 30))
    w.add_data("N2", mp.nstr(N2, 30))
    w.add_data("Q_N2", mp.nstr(Q_N2, 30))
    w.add_data("Q_A_cos", mp.nstr(Q_A_cos, 30))
    w.add_data("cos_factor_pole_u", "±1 (N2 = 1 - u² = 0)")
    w.add_data("pole_distance_over_u_substrate", mp.nstr(pole_ratio, 8))
    w.add_data("Q_A_cos_zero_at_u_substrate", str(bool(qacos_near_zero)))
    w.add_assertion(
        name="sdp_cos_factor_singular_at_u_substrate",
        computed=bool(not refuted), expected=False, tolerance=0,
        source="The literal SDP normalization Q_A·cos α_eff = Q_N2/(1-u²) has no "
               "zero/pole at u_substrate (smooth, nonzero; N2 pole at u=±1 is "
               "~117× farther). The pole is intrinsic to the c_k Habiro ladder, "
               "not the cos-factor. Expected False (synthesis refuted in literal "
               "form).",
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
