#!/usr/bin/env python3
"""qbeta_c3_swing_gate_probe.py — A3: the swing-difference gate (resolved filter).

Post-O2 (docs/audits/2026-08-14-aomega-to-S-bridge-refuted-O2-negative.md;
registry §9d) the individual `S_leak` anchor values sit under a ±1.262 CAL-3
band, so the diagonal-crossing gate's two-sided sign conditions are
CONDITIONAL. The one RESOLVED observable is the swing

    ΔS := S(muon) − S(proton) = c₃(muon) − c₃(proton)  (Vol(4₁) cancels),

resolved because the CAL-3 error is common-mode. This probe DERIVES the
resolved gate that replaces the conditional one as the primary filter on
candidate `u(q₀)` maps under the corrected NZ leading form
`Im 𝔙 = κ(Re²u − Im²u)`, `κ = √3/4`:

    GATE (A3):  (Re²u−Im²u)|_muon − (Re²u−Im²u)|_proton = ΔS/κ = 4·ΔS/√3.

What is computed (no fit; scope-(a); nothing wired):
  [1] ΔS from `c3_target_at` at both anchors (the same deterministic path the
      udeform constraint probe uses), checked against the O2 value 0.0491423421.
  [2] COMMON-MODE CANCELLATION DERIVED, not asserted: perturb the Q_β input by
      ±δ and measure the induced shift in each S individually vs in ΔS. The
      individual shifts are O(δ/u³) (the CAL-3 amplification); the ΔS shift is
      suppressed by ~7 orders (it enters only through the anchor-dependence of
      the 1/u³ prefactor).
  [3] The gate constant Δ_quad := 4·ΔS/√3, emitted for candidate-map filters.

DISCIPLINE. The swing is a FILTER, not a target: registry §9d pins it as
circular (μ–p tension × dc₃/dq; bean qou-6y1p scrapped). A candidate u(q₀)
map FAILING this gate is excluded (scope-(a)); a map PASSING it is merely
not-excluded — passing derives nothing. The conditional sign/diagonal gate
(`signflip_requires_diagonal_cross`) remains recorded as the secondary,
conditional-on-flip criterion.

Beans: qou-z0bd (A3) / ledger qou-gbuz. Companion: registry §9d (qou-9jem).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

set_compute_dps()  # mp.mp.dps = COMPUTE_DPS (70)

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
# O2 probe value (±7.6e-7 band). It was 0.0491423421 at the CODATA-2018 muon
# pin; the CODATA-2022 pin (fca08de7d2) moves S(muon), and so the swing, by
# 3.399e-4, which is what turned swing_matches_o2 red (2026-10-10 follow-up,
# bean qou-cds1). Live value, as also recorded in
# qbeta-c3-crossanchor-swing-provenance.witness.json.
SWING_O2 = mp.mpf("0.0494822652")
KAPPA = mp.sqrt(3) / 4


def S_of(q, qbeta):
    """S_leak(q) = c₃(q) + Vol(4₁); Vol(4₁) cancels in differences."""
    with mp.workdps(70):
        vol41 = +(2 * mp.clsin(2, mp.pi / 3))
    return c3_target_at(q, qbeta, ME) + vol41


def main() -> int:
    print("=" * 78)
    print(" A3 — the swing-difference gate: resolved filter for candidate u(q₀) maps")
    print("=" * 78)

    qp, qm = q_at(60), q_muon_at(60)

    wb = WitnessBuilder("qbeta-c3-swing-gate", engine="mpmath")
    wb.set_description(
        "A3 swing-difference gate (post-O2): the resolved observable is the "
        "swing dS = S(muon)-S(proton) = c3(muon)-c3(proton) (Vol(4_1) and the "
        "CAL-3 common-mode error cancel). Derives the resolved gate "
        "(Re^2u-Im^2u)|_mu - (Re^2u-Im^2u)|_p = 4*dS/sqrt(3) replacing the "
        "conditional two-sided sign gate as the PRIMARY candidate-map filter "
        "under the corrected NZ leading form. Common-mode cancellation is "
        "measured (perturb Q_beta by +/-delta: individual shifts are CAL-3-"
        "amplified, swing shift suppressed by orders). The swing is a FILTER "
        "not a target (registry 9d: circular, mu-p tension x dc3/dq). "
        "Scope-(a); no fit; no c_k wired; conditional diagonal gate kept as "
        "secondary."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    # [1] the swing, derived
    Sm, Sp = S_of(qm, QCOD), S_of(qp, QCOD)
    swing = Sm - Sp
    err_vs_o2 = mp.fabs(swing - SWING_O2)
    print(f"\n[1] S(muon)={mp.nstr(Sm, 10)}  S(proton)={mp.nstr(Sp, 10)}")
    print(f"    swing = {mp.nstr(swing, 12)}   (O2: {mp.nstr(SWING_O2, 10)}, |Δ|={float(err_vs_o2):.2e})")

    # [2] common-mode cancellation, measured
    delta = QCOD * mp.mpf("1e-6")   # 1 ppm Q_beta input perturbation
    Sm_d, Sp_d = S_of(qm, QCOD + delta), S_of(qp, QCOD + delta)
    shift_mu, shift_pr = mp.fabs(Sm_d - Sm), mp.fabs(Sp_d - Sp)
    shift_swing = mp.fabs((Sm_d - Sp_d) - swing)
    supp_mu = float(shift_swing / shift_mu) if shift_mu > 0 else 0.0
    print(f"\n[2] Q_β perturbed by 1 ppm: |δS(muon)|={mp.nstr(shift_mu, 6)}  "
          f"|δS(proton)|={mp.nstr(shift_pr, 6)}")
    print(f"    |δ(swing)| = {mp.nstr(shift_swing, 6)}   suppression vs individual: "
          f"{supp_mu:.3e}")

    # [3] the gate constant
    dquad = swing / KAPPA
    print(f"\n[3] GATE: (Re²u−Im²u)|_μ − (Re²u−Im²u)|_p = 4·ΔS/√3 = {mp.nstr(dquad, 12)}")
    print("    (filter only: failing excludes a candidate map; passing derives nothing)")

    wb.add_data("anchors", {"q_muon": mp.nstr(qm, 30), "q_proton": mp.nstr(qp, 30)})
    wb.add_data("swing", {"S_muon": mp.nstr(Sm, 15), "S_proton": mp.nstr(Sp, 15),
                          "swing": mp.nstr(swing, 15), "o2_reference": mp.nstr(SWING_O2, 12)})
    wb.add_data("gate", {"delta_quad_required": mp.nstr(dquad, 15),
                         "kappa": "sqrt(3)/4 (corrected NZ leading form)",
                         "role": "primary resolved filter; conditional diagonal gate secondary"})
    wb.add_data("discipline", {
        "swing_is_filter_not_target": "registry 9d: swing = mu-p tension x dc3/dq (circular)",
        "individual_S_band": "+/-1.262 CAL-3 (O2); sign conditions conditional"})
    # Strings keep the values out of float64 (drained convention, qou-t0rf).
    wb.add_assertion("swing_matches_o2",
                     computed=mp.nstr(err_vs_o2, 15), expected="0", tolerance="1e-6",
                     source="swing from c3_target_at at both anchors vs O2 probe value")
    wb.add_assertion("common_mode_cancellation",
                     computed=mp.nstr(shift_swing / shift_mu, 15), expected="0",
                     tolerance="1e-4",
                     source="1 ppm Q_beta perturbation: swing shift / individual shift << 1")
    wb.add_assertion("gate_constant_positive",
                     computed="1" if dquad > 0 else "0", expected="1", tolerance="0.5",
                     source="4*swing/sqrt(3) > 0 (muon-minus-proton orientation)")
    wb.save()

    ok = err_vs_o2 < mp.mpf("1e-6") and supp_mu < 1e-4
    print(f"\n  RESULT: {'GATE DERIVED (all checks pass)' if ok else 'CHECK FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
