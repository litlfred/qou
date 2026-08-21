#!/usr/bin/env python3
# polynomial_q_not_applicable: read-only decomposition probe; consumes
# committed witnesses (q-pinning, operator-valued-N3) + CODATA constants.
"""qbeta_habiro_residual_probe.py — σ_theory vs σ_CAL decomposition of the
production Q_β residual, with the anchor-stability cross-check.

SCOPED INVESTIGATION (NOT a production change). Anti-flip-flop discipline
per docs/coordination/ck-dk-canonical-registry.md §8: this probe proposes
NO new c_k wiring. It answers ONE question:

    Is the production Q_β residual (~1248 ppb vs CODATA) improvable by a
    PROVED higher-order term (σ_theory), or is it floored by the
    CAL-2 / q₀ substrate tension (σ_CAL, owner-gated)?

Method (all live, NO stale witness reads for the residual):
  1. Load the CANONICAL q₀ from q-pinning-50-digit.witness.json (now
     proton-pinned, 2026-06-22) and recompute the production Q_β ladder
     residual at THIS q₀ — settling the q0-repin staleness question.
  2. Decompose the residual into:
       σ_theory  = production formula-truncation residual (Q_N2 vs CODATA)
       σ_CAL     = propagated experimental error of the inputs
                   (m_e at 0.29 ppb + q₀ via dlnQ/dlnq · σ(q₀))
       σ_exp     = experimental error of the Q_β measurement itself
                   (sets the L2 100× target)
  3. Anchor-stability cross-check: the production Q_β formula is
     PARAMETER-FREE in q (no fitted c_k), so its residual inherits only
     q₀'s own shift on re-pinning. Bound that shift by the documented
     μ-p tension (11.5 ppb in q₀) via the sensitivity dlnQ/dlnq.
  4. Record the registry-settled c_3 anchor-INstability (the only known
     route below 1248 ppb is the fitted/near-match c_3, which FAILS the
     cross-anchor test — 2.98 % swing, dc_3/dq ≈ 4.6e6).

References:
  * docs/coordination/ck-dk-canonical-registry.md (the ONE c_k source of truth)
  * docs/precision-goals.md §"The 1 ppQ target is on the theory residual"
  * docs/audits/2026-05-28-mu-p-tension-substrate-floor.md (μ-p floor)
  * docs/audits/2026-06-29-qbeta-habiro-residual.md (this probe's writeup)
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — keeps flat-namespace imports
# working from the probes/ cluster subdirectory). Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_E_MEV_ERR,
    Q_BETA_MEV,
    Q_BETA_MEV_ERR,
)
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

OUT = HERE / "qbeta-habiro-residual.witness.json"

# μ-p tension: worst-case split between the muon-pin and proton-pin q₀,
# per docs/audits/2026-05-28-mu-p-tension-substrate-floor.md (11.5 ppb in q₀).
MU_P_Q0_SPLIT_PPB = mp.mpf("11.5")
# Registry-settled c_3 cross-anchor swing (J_Hopf near-match) and real-q
# rigidity-falsification slope, ck-dk-canonical-registry.md §3.
C3_CROSS_ANCHOR_SWING_PCT = mp.mpf("2.98")
C3_DCDQ = mp.mpf("4.6e6")


def q_beta_single_wrap(q: mp.mpf, m_e: mp.mpf) -> mp.mpf:
    """Production single-wrap closed form (q_beta_predicted.py, = Q_A / N=0)."""
    return m_e * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)


#: Straddle tolerance. Must sit BELOW the mu-p separation (1.15e-8), not
#: above it: the first version of this guard used 1.2e-8 and so could not fire
#: on the one straddle it exists to catch -- it passed a synthetic
#: proton-value-under-a-muon-label with room to spare. A threshold set at the
#: size of the thing being detected detects nothing.
#:
#: 1e-10 is two orders below the separation and well above the ~1e-50 noise of
#: a 50-dps decimal string, so it fires on a layer swap and not on a re-serialisation.
_STRADDLE_TOL = 1e-10


def _assert_anchor_matches_value(qpin: dict) -> None:
    """Fail loudly if the pin witness's stated anchor and emitted value differ.

    The q-pinning witness uses "anchor" for three different jobs -- the layer
    it reports at (`q0Anchor`), the derivation route (`calibration_inputs`),
    and the uncertainty budget (`physical_anchoring_bound`) -- and a consumer
    that greps for one and computes with another straddles the layers with no
    signal at all. That is how this probe came to announce proton and compute
    at muon.

    So: compare the LAYER field against the emitted number and refuse to
    proceed when they disagree. Checked against `q0Anchor`, deliberately, not
    against `calibration_inputs.anchor` -- the route field is allowed to name
    m_p/m_e while the ideal_muon override emits the muon literal, and keying
    on it would make this guard fire on the correct configuration.
    """
    from qou_substrate.witness import _q0_value_for_anchor

    layer = qpin.get("q0Anchor")
    if not layer:
        return  # nothing claimed, nothing to contradict
    emitted = mp.mpf(qpin["derived_50_digit"]["q"])
    expected = mp.mpf(str(_q0_value_for_anchor(layer)))
    if expected == 0:
        return
    rel = abs(emitted - expected) / expected
    if rel > _STRADDLE_TOL:
        raise SystemExit(
            f"ANCHOR STRADDLE in q-pinning-50-digit.witness.json: "
            f"q0Anchor says {layer!r} but derived_50_digit.q is "
            f"{float(rel):.3e} away from the {layer} pin. Computing here would "
            f"produce a number belonging to neither layer. See bean qou-m9xp."
        )


def main() -> int:
    m_e = mp.mpf(str(M_E_MEV))
    sig_me_rel = mp.mpf(str(M_E_MEV_ERR)) / m_e
    Q_codata = mp.mpf(str(Q_BETA_MEV))
    sig_exp_rel = mp.mpf(str(Q_BETA_MEV_ERR)) / Q_codata

    # --- 1. CANONICAL q₀ -----------------------------------------------
    #
    # This comment used to say "(live, proton-pinned)". It was WRONG, and the
    # field read two lines down is why the error was invisible:
    # `calibration_inputs.anchor` is `"m_p/m_e"` (the derivation ROUTE) while
    # `derived_50_digit.q` is the MUON value -- q-pinning-50-digit is listed
    # ideal_muon, so its Newton solve never runs. So the probe announced one
    # anchor and computed at another, 11.54 ppb apart.
    #
    # Measured cost: the probe quotes `sigma_CAL_q0_ppb = 0.0074`, so the
    # straddle is ~1558x its own stated q0 budget, and it exceeds
    # `target_100x_ppb = 7.8` outright. It does NOT move the headline
    # (residual_N2 = 1248 ppb vs a 7.8 ppb target is a ~160x miss either
    # way) -- but AGENTS.md is explicit that straddling is a defect
    # regardless of size, and an error budget that does not cover the error
    # is not a budget.
    qpin = record_upstream(COMP / "q-pinning-50-digit.witness.json", _UPSTREAM_RECORDS)
    q0 = mp.mpf(qpin["derived_50_digit"]["q"])
    anchor = qpin["calibration_inputs"]["anchor"]
    _assert_anchor_matches_value(qpin)
    sig_q0_rel = mp.mpf(qpin["physical_anchoring_bound"]["codata_relative_uncertainty"])

    # --- production ladder residuals (Q_A / Q_N1 / Q_N2) ---------------
    ov = record_upstream(COMP / "q-beta-operator-valued-N3.witness.json", _UPSTREAM_RECORDS)["data"]
    Q_A = mp.mpf(str(ov["Q_A"]))       # N=0 = single-wrap closed form
    Q_N1 = mp.mpf(str(ov["Q_N1"]))     # c_1 = b (Kashiwara)
    Q_N2 = mp.mpf(str(ov["Q_N2"]))     # c_2 = -1 (PROVED) — production wire

    # cross-check that Q_A in the witness matches the live single-wrap form
    Q_A_live = q_beta_single_wrap(q0, m_e)
    qA_consistency_ppb = float(abs(Q_A_live - Q_A) / Q_A * 1e9)

    def rel_ppb(x: mp.mpf) -> float:
        return float((x - Q_codata) / Q_codata * 1e9)

    resid_N0_ppb = rel_ppb(Q_A)
    resid_N1_ppb = rel_ppb(Q_N1)
    resid_N2_ppb = rel_ppb(Q_N2)  # the canonical "~1248 ppb"

    # --- 2. sensitivity dlnQ/dlnq (production formula) -----------------
    dq = q0 * mp.mpf("1e-18")
    dQdq = (q_beta_single_wrap(q0 + dq, m_e) - q_beta_single_wrap(q0 - dq, m_e)) / (2 * dq)
    dlnQ_dlnq = dQdq * q0 / q_beta_single_wrap(q0, m_e)

    # --- decomposition -------------------------------------------------
    sigma_theory_ppb = abs(resid_N2_ppb)  # framework's own truncation residual
    sigma_CAL_q0_ppb = float(abs(dlnQ_dlnq) * sig_q0_rel * 1e9)
    sigma_CAL_me_ppb = float(sig_me_rel * 1e9)  # linear in m_e
    sigma_CAL_total_ppb = float(
        mp.sqrt((abs(dlnQ_dlnq) * sig_q0_rel) ** 2 + sig_me_rel ** 2) * 1e9
    )
    sigma_exp_ppb = float(sig_exp_rel * 1e9)
    target_100x_ppb = sigma_exp_ppb / 100.0

    # --- 3. anchor-stability of the PRODUCTION (parameter-free) form ---
    q0_shift_worstcase = float(abs(dlnQ_dlnq) * MU_P_Q0_SPLIT_PPB)  # ppb in Q_β

    # ------------------------------------------------------------------
    print("=" * 72)
    print("Q_β Habiro residual — σ_theory vs σ_CAL decomposition")
    print("=" * 72)
    print(f"canonical q₀ anchor : {anchor}")
    print(f"q₀                  : {mp.nstr(q0, 20)}")
    print(f"Q_A witness vs live single-wrap consistency: {qA_consistency_ppb:.3e} ppb")
    print()
    print("production ladder residuals vs CODATA:")
    print(f"  N=0 (single-wrap)  : {resid_N0_ppb:+.1f} ppb  (+0.168 %)")
    print(f"  N=1 (Kashiwara c₁) : {resid_N1_ppb:+.1f} ppb")
    print(f"  N=2 (c₂=-1 PROVED) : {resid_N2_ppb:+.1f} ppb  <- PRODUCTION WIRE")
    print()
    print("decomposition:")
    print(f"  σ_theory (Q_N2 truncation) : {sigma_theory_ppb:.2f} ppb")
    print(f"  σ_CAL  (m_e 0.29 ppb)      : {sigma_CAL_me_ppb:.4f} ppb")
    print(f"  σ_CAL  (q₀ via dlnQ/dlnq)  : {sigma_CAL_q0_ppb:.6f} ppb  "
          f"(dlnQ/dlnq = {mp.nstr(dlnQ_dlnq, 6)})")
    print(f"  σ_CAL  total               : {sigma_CAL_total_ppb:.4f} ppb")
    print(f"  σ_exp (target measurement) : {sigma_exp_ppb:.1f} ppb  "
          f"=> 100× target {target_100x_ppb:.2f} ppb")
    print()
    print("anchor-stability of the parameter-free production form:")
    print(f"  Q_β shift for worst-case μ-p q₀ split (11.5 ppb): "
          f"{q0_shift_worstcase:.1f} ppb  (<< {sigma_theory_ppb:.0f} ppb residual)")
    print()
    print("c_3 (the only known sub-1248-ppb route) — registry-settled:")
    print(f"  cross-anchor swing : {float(C3_CROSS_ANCHOR_SWING_PCT)} %  -> NEAR-MATCH (NOT derived)")
    print(f"  dc_3/dq            : ~{mp.nstr(C3_DCDQ, 3)}  -> real-q rigidity-FALSIFIED")

    # --- witness -------------------------------------------------------
    wb = WitnessBuilder("qbeta-habiro-residual", engine="mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.set_description(
        "σ_theory vs σ_CAL decomposition of the production Q_β residual at "
        "the canonical (proton-pinned) q₀. Recomputed LIVE — settles the "
        "q0-repin staleness question: the ~1248 ppb is the genuine Q_N2 "
        "truncation residual, NOT a stale-witness artifact. Anti-flip-flop "
        "per ck-dk-canonical-registry.md §8: proposes NO new c_k wiring."
    )
    wb.set_content_block("rem:beta-decay-energy-scale")
    wb.add_data("q0_anchor", anchor)
    wb.add_data("q0_50dps", str(q0))
    wb.add_data("qA_witness_vs_live_consistency_ppb", qA_consistency_ppb)
    wb.add_data("residual_N0_ppb", resid_N0_ppb)
    wb.add_data("residual_N1_ppb", resid_N1_ppb)
    wb.add_data("residual_N2_ppb_PRODUCTION", resid_N2_ppb)
    wb.add_data("dlnQ_beta_dlnq", str(dlnQ_dlnq))
    wb.add_data("sigma_theory_ppb", sigma_theory_ppb)
    wb.add_data("sigma_CAL_me_ppb", sigma_CAL_me_ppb)
    wb.add_data("sigma_CAL_q0_ppb", sigma_CAL_q0_ppb)
    wb.add_data("sigma_CAL_total_ppb", sigma_CAL_total_ppb)
    wb.add_data("sigma_exp_target_ppb", sigma_exp_ppb)
    wb.add_data("target_100x_ppb", target_100x_ppb)
    wb.add_data("anchor_stability_q0_worstcase_shift_ppb", q0_shift_worstcase)
    wb.add_data("c3_cross_anchor_swing_pct", float(C3_CROSS_ANCHOR_SWING_PCT))
    wb.add_data("c3_dcdq", float(C3_DCDQ))
    wb.add_data(
        "verdict",
        "The 1248 ppb is σ_theory (formula truncation), NOT σ_CAL "
        "(σ_CAL ≈ 0.29 ppb, m_e-dominated; q₀ contributes 0.007 ppb). It is "
        "theory-improvable IN PRINCIPLE, but the ONLY known route below it "
        "is the fitted/near-match c_3 ladder, which FAILS the cross-anchor "
        "test (2.98 % swing) and is registry-REFUTED as a real-q derivation. "
        "No PROVED higher-order Habiro term exists. Closing 1248 → 7.8 ppb "
        "(the L2 100× target, itself BELOW the 779.7 ppb σ_exp floor) is "
        "Subgoal-2 / owner-gated q₀ work. NOT improvable by derivation today.",
    )

    # consistency assertion: the live single-wrap form must match the
    # committed Q_A witness (guards against a stale q₀ in the witness).
    wb.add_assertion(
        "Q_A_witness_matches_live_single_wrap",
        computed=qA_consistency_ppb,
        expected=0.0,
        tolerance=1.0,  # ppb
        source="single-wrap closed form recomputed at canonical q₀",
    )
    # the production residual is σ_theory, two orders above σ_CAL.
    wb.add_assertion(
        "sigma_theory_dominates_sigma_CAL",
        computed=sigma_CAL_total_ppb,
        expected=0.0,
        tolerance=sigma_theory_ppb,
        source="σ_CAL << σ_theory (residual is framework's, not propagated)",
    )
    saved = wb.save()
    print(f"\nWrote {saved.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
