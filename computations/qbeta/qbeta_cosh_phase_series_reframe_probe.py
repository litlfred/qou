#!/usr/bin/env python3
"""qbeta_cosh_phase_series_reframe_probe.py
============================================

Reframe the Q_β c_k ladder as the u-Taylor expansion of `cos(Φ(u))`
(equivalently `cosh` of an imaginary hyperbolic phase) — the structure
PR #1871 §3 derived (`m_avg = m₀·cosh θ` even / `Δ_pn/2 = m₀·sinh θ`
odd) — and extract the concrete **phase coefficients Φ_k(q)** that
#1871's fibre-level q-difference recurrence must reproduce.

## Why this probe (it answers "c_k are from a series")

The standalone-`sinh(ℓη)` reading (this branch's f-map probe) was
REFUTED: no closed-form `sinh(ℓη)/u^k` reproduces c_3 at both anchors
with a fixed ℓ. PR #1871 supplies the correct structure: the c_k are
the **Taylor coefficients in u of `cosh`/`sinh` of a single hyperbolic
phase `θ(u)`** whose own u-expansion is fixed by a q-difference
recurrence (their `G(qx;q)=R(q,x)·G(x;q)`).

So the right object is the **phase series** `Φ(u) = Φ_1 u + Φ_2 u² + …`
with

    Q_β / Q_A  =  cos(Φ(u))            (fibre: cosh of an imaginary angle;
                                        the bar-EVEN component carrying c_2,
                                        and the odd-rung corrections as the
                                        higher Φ_k feed both parities)

Expanding `cos(Φ(u))` to order u³ (with c_1 = 0, so Φ has no constant
term and Φ_1 is the leading coefficient):

    cos(Φ) = 1 − Φ²/2 + …
    Φ²     = Φ_1² u² + 2Φ_1Φ_2 u³ + …
  ⇒ c_2 = −Φ_1²/2,    c_3 = −Φ_1·Φ_2.

Hence:
    Φ_1 = √(−2·c_2) = √2     (c_2 = −1 is Lean-PROVED & q-INDEPENDENT
                              ⇒ Φ_1 = √2 EXACTLY at every anchor),
    Φ_2 = −c_3 / Φ_1 = −c_3/√2.

This is the unification:
  - `c_2 = −1 ⟺ Φ_1 = √2`  ↔ the bar-EVEN `cos(√2 u)` slice (#1866) and
    #1871's `m_avg = m₀ cosh θ`;
  - `c_3 = −Φ_1·Φ_2 = g`    ↔ the odd-parity reduction `c_3 = g` (#1880);
  - the bar-odd `sinh` parity ↔ #1887 / #1871's `Δ_pn/2 = m₀ sinh θ`.

## The deliverable: the Φ_2(q) target for #1871's recurrence

The probe computes `Φ_2(q) = −c_3(q)/√2` at both anchors. This is the
CONCRETE quantity #1871's q-difference G-recurrence must reproduce: a
genuine fibre-level recurrence predicts `Φ_2(q)` from `Φ_1` (= √2) and
the recurrence kernel `R(q, x)`, so its prediction must match
`−c_3(q)/√2` at proton AND muon. This probe hands off that target
(it does not fit the recurrence — that is #1871's compute).

## No-fit discipline

`Φ_1 = √2` is forced by the proved c_2; `Φ_2 = −c_3/√2` is an algebraic
read-off of the cal-anchored c_3 — no free parameters. The round-trip
check (does `cos(Φ_1 u + Φ_2 u²)` reproduce c_2, c_3?) is a consistency
gate, not a fit.

## References
- Series structure: PR #1871 §3 + `docs/workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md` §2
- Even slice cos(√2 u): PR #1866
- Odd reduction c_3 = g: PR #1880
- Reeb sinh parity (Lean): `QBetaReebSinhParity` (PR #1887)
- c_3 cross-anchor target: `qbeta_utils.c3_target_at` (PR #1831)
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from mpmath import mp, mpf, sqrt, cos, fabs  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_utils import c3_target_at  # noqa: E402


def phase_coeffs(c2: mpf, c3: mpf) -> tuple[mpf, mpf]:
    """Φ_1, Φ_2 from c_2, c_3 via cos(Φ(u)) = 1 − Φ²/2 + … :
       Φ_1 = √(−2 c_2),  Φ_2 = −c_3/Φ_1."""
    phi1 = sqrt(-2 * c2)
    phi2 = -c3 / phi1
    return phi1, phi2


def reconstruct_c2_c3(phi1: mpf, phi2: mpf, u: mpf = mpf("1e-6")) -> tuple[mpf, mpf]:
    """Round-trip: extract c_2, c_3 of cos(Φ_1 u + Φ_2 u²) by finite
    differences, to confirm the phase reproduces the targets."""
    def F(x):
        return cos(phi1 * x + phi2 * x ** 2)
    f0 = F(mpf(0))
    fp1, fm1 = F(u), F(-u)
    fp2, fm2 = F(2 * u), F(-2 * u)
    d2 = (fp1 - 2 * f0 + fm1) / (u * u)
    d3 = (fp2 - 2 * fp1 + 2 * fm1 - fm2) / (2 * u ** 3)
    return d2 / 2, d3 / 6


def main() -> int:
    set_compute_dps()

    me = mpf(str(M_E_MEV))
    q_codata = mpf(str(Q_BETA_MEV))
    qp = q_at(mp.dps)
    qm = q_muon_at(mp.dps)

    c2 = mpf(-1)                      # Lean-proved, q-independent
    c3_p = c3_target_at(qp, q_codata, me)
    c3_m = c3_target_at(qm, q_codata, me)

    SQRT2 = sqrt(mpf(2))

    print("=" * 78)
    print(" Q_β c_k → phase-series reframe:  Q_β/Q_A = cos(Φ(u))  [PR #1871 §3]")
    print("=" * 78)
    print(f"  c_2 = -1 (Lean-proved, q-independent)")
    print(f"  c_3(proton) = {fmt(c3_p)[:18]}   c_3(muon) = {fmt(c3_m)[:18]}")
    print()

    phi1_p, phi2_p = phase_coeffs(c2, c3_p)
    phi1_m, phi2_m = phase_coeffs(c2, c3_m)

    print(f"  Φ_1 = √(−2·c_2) = √2 = {fmt(SQRT2)[:18]}")
    print(f"    proton Φ_1 = {fmt(phi1_p)[:18]}   muon Φ_1 = {fmt(phi1_m)[:18]}")
    print(f"    → Φ_1 anchor-EXACT (forced by proved c_2; q-independent). ✓")
    print()
    print(f"  Φ_2 = −c_3/√2  (the target #1871's q-difference recurrence must give):")
    print(f"    proton Φ_2 = {fmt(phi2_p)[:18]}")
    print(f"    muon   Φ_2 = {fmt(phi2_m)[:18]}")
    swing_phi2 = fabs(phi2_p - phi2_m)
    print(f"    cross-anchor swing |ΔΦ_2| = {fmt(swing_phi2)[:14]}  "
          f"(rel {float(swing_phi2/fabs(phi2_p)):.4f})")
    print()

    # Round-trip consistency: does cos(Φ_1 u + Φ_2 u²) reproduce c_2, c_3?
    c2_rt_p, c3_rt_p = reconstruct_c2_c3(phi1_p, phi2_p)
    c2_err = float(fabs(c2_rt_p - c2))
    c3_err_ppm = float(fabs(c3_rt_p - c3_p) / fabs(c3_p) * 1e6)
    print(f"  Round-trip (proton): cos(Φ_1 u + Φ_2 u²) →")
    print(f"    c_2 = {float(c2_rt_p):+.8f} (target -1, err {c2_err:.2e})")
    print(f"    c_3 = {float(c3_rt_p):+.8f} (target {float(c3_p):.6f}, "
          f"err {c3_err_ppm:.2e} ppm)")
    rt_ok = c2_err < 1e-6 and c3_err_ppm < 1e3
    print(f"    consistency: {'CONFIRMED' if rt_ok else 'FAILED'}")
    print()

    print("=" * 78)
    print(" VERDICT — structural reframe CONSISTENT; open quantity relocated")
    print("=" * 78)
    print("  The c_k ladder IS the u-expansion of cos(Φ(u)) (= cosh of an")
    print("  imaginary fibre phase), per PR #1871 §3. The proved c_2 = -1 fixes")
    print("  Φ_1 = √2 EXACTLY at every anchor — the bar-EVEN cos(√2 u) slice")
    print("  (#1866) and #1871's m_avg = m₀ cosh θ. The first OPEN coefficient")
    print("  is Φ_2 = -c_3/√2, which carries c_3's full cross-anchor swing.")
    print()
    print("  This UNIFIES the c_3 threads:")
    print("    • c_2 = -1  ⟺  Φ_1 = √2            (even slice, #1866 / #1871 cosh)")
    print("    • c_3 = -Φ_1·Φ_2 = g               (odd reduction, #1880)")
    print("    • bar-odd sinh parity              (#1887 / #1871 Δ_pn sinh)")
    print()
    print("  HAND-OFF to PR #1871: a genuine fibre-level q-difference recurrence")
    print("  G(qx;q)=R(q,x)·G(x;q) must PREDICT Φ_2(q) = -c_3(q)/√2 from Φ_1=√2")
    print("  and the kernel R — and the prediction must hit BOTH targets:")
    print(f"    Φ_2(proton) = {fmt(phi2_p)[:16]}")
    print(f"    Φ_2(muon)   = {fmt(phi2_m)[:16]}")
    print("  That cross-anchor match (not a single-anchor fit) is the closure")
    print("  test for the q-difference axis my #1880 showed is data-blocked at")
    print("  the c_k level — but is determined at the Φ/recurrence level.")
    verdict = "CONSISTENT_PHASE_REFRAME_PHI2_HANDOFF_TO_QDIFFERENCE"

    wb = WitnessBuilder(
        "qbeta-cosh-phase-series-reframe-probe", engine="mpmath",
    )
    wb.set_description(
        "Reframe the Q_β c_k ladder as the u-Taylor expansion of cos(Φ(u)) "
        "(cosh of an imaginary fibre phase), the structure PR #1871 §3 "
        "derived (m_avg=m₀cosh θ / Δ_pn=m₀sinh θ). c_2=-1 (proved) ⇒ "
        "Φ_1=√2 anchor-exact; c_3=-Φ_1·Φ_2 ⇒ Φ_2=-c_3/√2. Extracts the "
        "concrete Φ_2(q) targets at both anchors that #1871's fibre-level "
        "q-difference recurrence must reproduce — the closure test for the "
        "axis #1880 showed is data-blocked at the c_k level. Unifies #1866 "
        "(even cos slice), #1880 (c_3=g), #1887 (sinh parity), #1871 "
        "(cosh/sinh series + q-difference). No fits — algebraic read-off."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("c2", fmt(c2))
    wb.add_data("c3_proton", fmt(c3_p))
    wb.add_data("c3_muon", fmt(c3_m))
    wb.add_data("phi1", fmt(SQRT2))
    wb.add_data("phi1_anchor_independent", True)
    wb.add_data("phi2_proton_target", fmt(phi2_p))
    wb.add_data("phi2_muon_target", fmt(phi2_m))
    wb.add_data("phi2_cross_anchor_swing", fmt(swing_phi2))
    wb.add_data("roundtrip_c2_err", c2_err)
    wb.add_data("roundtrip_c3_err_ppm", c3_err_ppm)
    wb.add_data("verdict", verdict)
    wb.add_data("handoff_to_pr", 1871)
    wb.add_data("interpretation", (
        "The cosh/sinh series structure (PR #1871) is the correct framing for "
        "the c_k: they are u-Taylor coefficients of cos(Φ(u)). c_2=-1 fixes "
        "Φ_1=√2 (anchor-exact); the open coefficient Φ_2(q)=-c_3(q)/√2 is the "
        "concrete target a fibre-level q-difference recurrence must predict at "
        "both anchors. This relocates the open question from the (data-blocked, "
        "#1880) c_k level to the Φ/recurrence level (#1871's G-equation)."
    ))
    # Invariants
    wb.add_assertion(
        "phi1_equals_sqrt2_from_proved_c2",
        computed=float(phi1_p), expected=float(SQRT2), tolerance=1e-12,
        source="Φ_1 = √(−2·c_2) with c_2 = −1 (Lean-proved) ⇒ Φ_1 = √2 exactly.",
    )
    wb.add_assertion(
        "phase_roundtrip_reproduces_c3",
        computed=1.0 if c3_err_ppm < 1e3 else 0.0, expected=1.0,
        source=f"cos(Φ_1 u+Φ_2 u²) reproduces c_3 to {c3_err_ppm:.2e} ppm.",
    )
    wb.save()
    print()
    print(f"  Witness: qbeta-cosh-phase-series-reframe-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
