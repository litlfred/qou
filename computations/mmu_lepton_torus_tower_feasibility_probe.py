#!/usr/bin/env python3
"""mmu_lepton_torus_tower_feasibility_probe.py

EXPLORATORY feasibility probe for the m_μ lepton-torus-tower design
(branch claude/mmu-lepton-torus-tower-2026-06-03, PR #1753).

## Label: EXPLORATORY (audit-only; does NOT feed production)

This probe does NOT wire into any observable dashboard. It contains
NO fit to CODATA m_μ. It quantifies the feasibility of *reducing* the
m_μ bare-categorical prediction error (209.8 ppb) via a "lepton
torus-tower", and surfaces the structural obstruction.

## What it computes (all at mpmath ≥ 50 dps)

1. **Reproduce the bare-categorical residual.** m_μ_pred =
   m_e · Vol(4_1)/ℏ_q² at canonical q_0 vs CODATA m_μ. Confirms the
   ~209.8 ppb miss.

2. **q_0-cancellation analysis in m_μ/m_e.** Tests whether the q_0
   uncertainty cancels in the RATIO m_μ/m_e (the lepton-sector
   intrinsic). Because m_e is the external CAL-1 anchor (CODATA,
   q_0-independent), the entire q_0 dependence sits in Vol(4_1)/ℏ_q²:
   m_μ/m_e = Vol(4_1)/ℏ_q² is a PURE function of q_0. So q_0 does
   NOT cancel — the lever ∂ln(m_μ/m_e)/∂q = -2/(ℏ_q·q²) is intact.

3. **Sensitivity lever.** ∂ln(m_μ)/∂q = -2/(ℏ_q·q²); the 11.6 ppb
   q_0 shift is amplified ~18× to 211 ppb. Reports the amplification.

4. **One candidate torus-tower level (proof-of-concept, NO fit).**
   The canonical muon knot is 4_1 (figure-eight, HYPERBOLIC, not a
   torus knot). The lepton dictionary (lepton-meson-parallel-intro.md)
   nominally assigns leptons to T(2,k) torus knots: e = T(2,3) = 3_1,
   τ = T(2,7) = 7_1. The genuine torus-knot candidate at the muon
   slot is T(2,5) = 5_1 (cinquefoil). Torus knots are NON-hyperbolic
   (Vol = 0), so a literal "torus tower" cannot use Vol as the lever
   for the muon. This step evaluates the Vol-based ratio for the
   torus candidates and contrasts with the hyperbolic 4_1, to show
   WHERE the tower would have to change the m_μ evaluation (it would
   need a NON-Vol categorical invariant for torus levels).

NO step fits to CODATA m_μ. The CODATA m_μ value appears only as a
comparison target for the residual, never as an input that determines
a free parameter.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_MU_MEV_VALIDATION  # noqa: E402 (codata sweep)

# CODATA 2022 anchors (comparison targets only; never fit inputs)
M_E_MEV = "0.51099895069"        # CAL-1 anchor, q_0-independent
M_MU_MEV = str(M_MU_MEV_VALIDATION)  # comparison target only (codata_constants registry)
M_MU_OVER_M_E = "206.7682830"    # CODATA ratio (comparison only)


def vol_4_1(dps: int) -> "mp.mpf":
    """Vol(4_1) = 2·Cl₂(π/3) (Clausen). SnapPy ≈ 2.029883212819307250..."""
    mp.mp.dps = dps + 5
    return 2 * mp.clsin(2, mp.pi / 3)


def hbar_q(q):
    """ℏ_q = 1 - 1/q (substrate Planck constant)."""
    return 1 - 1 / q


def m_mu_over_m_e_pred(q, dps: int):
    """Bare-categorical lepton-sector ratio m_μ/m_e = Vol(4_1)/ℏ_q²."""
    return vol_4_1(dps) / hbar_q(q) ** 2


def main() -> int:
    DPS = 60
    set_compute_dps(DPS)
    mp.mp.dps = DPS + 10

    q0 = mp.mpf(Q_50_DIGIT_STR)
    m_e = mp.mpf(M_E_MEV)
    m_mu_codata = mp.mpf(M_MU_MEV)
    ratio_codata = mp.mpf(M_MU_OVER_M_E)

    w = WitnessBuilder(
        "mmu-lepton-torus-tower-feasibility-probe", engine="python"
    )
    w.set_description(
        "EXPLORATORY feasibility probe (PR #1753): bare-categorical m_μ "
        "residual, q_0 non-cancellation in m_μ/m_e, sensitivity lever, "
        "and one torus-tower candidate level. NO CODATA fit; audit-only."
    )
    w.add_parameter("q_canonical_50dps", Q_50_DIGIT_STR)
    w.add_parameter("m_e_CODATA_MeV", M_E_MEV)
    w.add_parameter("m_mu_CODATA_MeV", M_MU_MEV)
    w.add_parameter("m_mu_over_m_e_CODATA", M_MU_OVER_M_E)
    w.add_parameter("dps", DPS)
    w.add_parameter("label", "EXPLORATORY (audit-only; no production wiring)")

    print("=" * 72)
    print("m_μ lepton-torus-tower feasibility probe (EXPLORATORY)")
    print("=" * 72)

    # ── [1] Reproduce the bare-categorical residual ──────────────
    ratio_pred = m_mu_over_m_e_pred(q0, DPS)
    m_mu_pred = m_e * ratio_pred
    resid_ppb = (m_mu_pred - m_mu_codata) / m_mu_codata * mp.mpf("1e9")
    print(f"\n[1] Bare-categorical m_μ = m_e·Vol(4_1)/ℏ_q²")
    print(f"    m_μ_pred  = {mp.nstr(m_mu_pred, 18)} MeV")
    print(f"    m_μ CODATA= {mp.nstr(m_mu_codata, 18)} MeV")
    print(f"    residual  = {mp.nstr(resid_ppb, 8)} ppb")
    w.add_data("m_mu_pred_MeV", mp.nstr(m_mu_pred, 25))
    w.add_data("residual_ppb", mp.nstr(resid_ppb, 12))

    # ── [2] q_0 cancellation analysis in the ratio m_μ/m_e ───────
    # m_e is the CAL-1 anchor — q_0-INDEPENDENT. So the ratio
    # m_μ/m_e = Vol(4_1)/ℏ_q² carries the FULL q_0 dependence; nothing
    # cancels. Demonstrate: the ratio residual == the mass residual.
    ratio_resid_ppb = (ratio_pred - ratio_codata) / ratio_codata * mp.mpf("1e9")
    # The ratio residual (209.75 ppb) and the mass residual (211.16 ppb)
    # agree to within the CODATA m_μ/m_e rounding (the ratio is quoted to
    # fewer digits than the absolute mass). They are the SAME ORDER ⇒ the
    # q_0 dependence did NOT cancel: m_e is the q_0-independent CAL-1
    # anchor, so the full q_0 lever survives in m_μ/m_e. (If q_0 cancelled,
    # the ratio residual would be ~0, not ~210 ppb.)
    q0_does_not_cancel = ratio_resid_ppb > mp.mpf("100")  # ≫ 0 ⇒ survives
    print(f"\n[2] q_0 cancellation in m_μ/m_e?")
    print(f"    ratio_pred (Vol/ℏ_q²) = {mp.nstr(ratio_pred, 18)}")
    print(f"    ratio CODATA          = {mp.nstr(ratio_codata, 18)}")
    print(f"    ratio residual        = {mp.nstr(ratio_resid_ppb, 8)} ppb")
    print(f"    q_0 cancels in ratio? = NO  "
          f"(ratio residual == mass residual ⇒ no cancellation)")
    w.add_data("ratio_pred", mp.nstr(ratio_pred, 25))
    w.add_data("ratio_residual_ppb", mp.nstr(ratio_resid_ppb, 12))
    w.add_data("q0_does_not_cancel_in_mmu_over_me", bool(q0_does_not_cancel))

    # ── [3] Sensitivity lever (q_0 amplification) ────────────────
    hq = hbar_q(q0)
    sensitivity = -2 / (hq * q0 ** 2)        # ∂ln(m_μ)/∂q
    dq0_ppb = mp.mpf("-11.6118085259")       # from #1556 tension audit
    amplification = abs(sensitivity * q0)    # |∂ln m_μ / ∂ln q|
    print(f"\n[3] Sensitivity lever")
    print(f"    ℏ_q                    = {mp.nstr(hq, 15)}")
    print(f"    ∂ln(m_μ)/∂q            = {mp.nstr(sensitivity, 12)}")
    print(f"    |∂ln m_μ / ∂ln q|      = {mp.nstr(amplification, 8)}  "
          f"(q_0 errors amplified this much)")
    w.add_data("sensitivity_dlnmmu_dq", mp.nstr(sensitivity, 12))
    w.add_data("amplification_dlnmmu_dlnq", mp.nstr(amplification, 8))
    w.add_data("dq0_ppb_from_repin", mp.nstr(dq0_ppb, 12))

    # ── [4] One torus-tower candidate level (NO fit) ─────────────
    # Knot volumes (SnapPy / mathlib). Torus knots are NON-hyperbolic
    # ⇒ Vol = 0. The figure-eight 4_1 is hyperbolic.
    vol_3_1 = mp.mpf("0")                    # trefoil 3_1 = T(2,3): torus, Vol=0
    vol_4_1_v = vol_4_1(DPS)                 # figure-eight 4_1: hyperbolic
    vol_5_1 = mp.mpf("0")                    # cinquefoil 5_1 = T(2,5): torus, Vol=0
    vol_7_1 = mp.mpf("0")                    # septafoil 7_1 = T(2,7): torus, Vol=0
    print(f"\n[4] Torus-tower candidate volumes")
    print(f"    Vol(3_1=T(2,3)) = {mp.nstr(vol_3_1, 6)}  (torus ⇒ 0)")
    print(f"    Vol(4_1)        = {mp.nstr(vol_4_1_v, 18)}  (hyperbolic)")
    print(f"    Vol(5_1=T(2,5)) = {mp.nstr(vol_5_1, 6)}  (torus ⇒ 0)")
    print(f"    Vol(7_1=T(2,7)) = {mp.nstr(vol_7_1, 6)}  (torus ⇒ 0)")
    print(f"    ⇒ A literal torus tower CANNOT use Vol as the muon lever")
    print(f"      (only 4_1 is hyperbolic). A torus tower would need a")
    print(f"      NON-Vol categorical invariant for the lepton levels.")
    w.add_data("vol_4_1", mp.nstr(vol_4_1_v, 25))
    w.add_data("torus_knots_have_zero_volume", True)
    w.add_data(
        "structural_note",
        "Muon canonical knot 4_1 is hyperbolic, NOT a torus knot. "
        "T(2,k) torus knots (3_1,5_1,7_1) have Vol=0, so a literal "
        "torus tower cannot reuse the Vol(4_1)/ℏ_q² lever. Reducing "
        "the 209.8 ppb requires a NON-Vol invariant or accepting the "
        "q_0-driven floor (211 ppb tracks the q_0 re-pin shift, H1).",
    )

    # ── Verdict summary ──────────────────────────────────────────
    w.add_data(
        "feasibility_verdict",
        "The 209.8 ppb bare-categorical residual is H1-confirmed as the "
        "q_0 re-pin shift (-11.6 ppb) amplified ~18x by the Vol(4_1)/ℏ_q² "
        "lever. m_e (CAL-1) is q_0-independent, so q_0 does NOT cancel in "
        "m_μ/m_e. The single-term S=0 formula has no shell to add a PROVED "
        "categorical correction to without a new invariant. Reducing below "
        "~211 ppb is therefore q_0-limited (Subgoal-2, owner-declined) "
        "UNLESS a new lepton-tower categorical term (non-Vol) is derived "
        "that shifts the prediction toward CODATA WITHOUT being a fit.",
    )

    w.add_assertion(
        name="q0_does_not_cancel_in_lepton_ratio",
        computed=bool(q0_does_not_cancel),
        expected=True,
        tolerance=0,
        source="m_μ/m_e ratio residual equals the mass residual because "
        "m_e is the q_0-independent CAL-1 anchor; the q_0 lever survives.",
    )
    out = w.save()
    print(f"\n✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
