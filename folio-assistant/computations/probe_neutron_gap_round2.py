#!/usr/bin/env python3
"""Neutron-gap probes — Sprint B follow-up, round 2.

Round 1 (`probe_neutron_gap.py`, PR #452) tested three single-channel
modifications to V_3term (H1: λ_alt sign; H2: [2]_q std weight; H3:
chirality as Term-5 factor) and returned a null result: none closed
the −56% neutron residual below 1 %; smallest residual was H2 at
≈ −25 %.

Round 2 reframes per `prop:full-pole-structure-mass-trace`: the full
Markov trace is

    tr_M(T_w, q_0) = tr_M^entire(T_w, q_0)
                     + Σ_{n≥2} Σ_{gcd(j,n)=1} r_n^(j)(T_w) / (q_0 − ζ_n^(j))

and the dominant-pole approximation captures only ~9.1 / Σ_n 1/|q_0 − ζ_n^(j)|
of the kernel weight.  *"For atoms in regime (2) or (3) it fails at
the percent level — consistent with the observed 5–20 % discrepancies
on ⁴He through ⁴⁰Ca."*

This probe directly evaluates the **full** symbolic Markov trace
`tr_M(T_w, q)` at `q = q_0` — no truncation, no Wedderburn-channel
approximation, just the rational function in q from the Habiro
expansion (committed in `habiro-coefficients-atomic.witness.json`).

H4: full tr_M(T_w, q_0) via direct evaluation of the symbolic
    rational function from the Habiro witness, combined with the
    substrate-derived energy scale
    `E_0 = m_e / (q_0 · (q_0 - 1))` (canonical Planck-tick form per
    `prop:three-calibration-inputs`).  Uses **only** CAL-1 + CAL-2
    + CAL-3 (no proton-mass calibration): the proton prediction is
    `|tr_M(p, q_0)| · E_0` and the neutron prediction follows the
    three-calibration chain
    `m_n = m_p + Q_β + m_e`.

**Workplan-0b Bucket D rewire (PR #759):** previously this script
calibrated `E_0 = m_p (CODATA) / |tr_M(p)|`, introducing m_p as a
fourth empirical input. Replaced with the canonical Planck-tick
substrate form to surface the structural agreement (or gap) without
proton calibration.

Output: `neutron-gap-probes-round2.witness.json`
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import json
import sympy as sp
import mpmath as mp

from q_parameter import Q as Q0_FLOAT  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    Q_BETA_MEV,
    M_P_MEV_VALIDATION,
    M_N_MEV_VALIDATION,
)
from witness_base import WitnessBuilder  # noqa: E402

_DPS = 50
HABIRO_WITNESS = HERE / "habiro-coefficients-atomic.witness.json"


def eval_tr_M_symbolic(tr_M_in_q_str: str, q0_mp) -> mp.mpf:
    """Parse the sympy expression for `tr_M(T_w, q)` from the Habiro
    witness and evaluate at `q = q0_mp` in 50-dps mpmath.

    The witness stores the trace as a rational function p(q)/denom(q);
    sympy parses it directly and we substitute q = q0 then evaluate
    at mpmath precision."""
    q = sp.Symbol('q')
    expr = sp.sympify(tr_M_in_q_str, locals={'q': q})
    # Evaluate at q = q0 with 50-digit precision
    val = expr.subs(q, q0_mp).evalf(_DPS)
    # Convert sympy's internal Float (which uses mpmath under the hood)
    # to a true mp.mpf so downstream arithmetic stays in mpmath.
    return mp.mpf(str(val))


def predict_h4_full_tr_M(habiro_data, particle_key: str):
    """H4: evaluate the FULL symbolic tr_M at q_0 — no truncation."""
    e = habiro_data["results"][particle_key]
    tr_M_str = e["tr_M_in_q"]
    with mp.workdps(_DPS):
        q0 = mp.mpf(str(Q0_FLOAT))
        tr_M_val = eval_tr_M_symbolic(tr_M_str, q0)
    return tr_M_val


def main() -> int:
    with open(HABIRO_WITNESS) as f:
        habiro = json.load(f)

    print("=" * 100)
    print("NEUTRON-GAP PROBES — ROUND 2 (full tr_M at q_0, no Wedderburn truncation)")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  m_e (CAL-1)          = {mp.nstr(M_E_MEV, 10)} MeV")
    print(f"  Q_beta (CAL-3)       = {mp.nstr(Q_BETA_MEV, 10)} MeV")
    print(f"  m_p (validation)     = {mp.nstr(M_P_MEV_VALIDATION, 10)} MeV  (comparison target only)")
    print(f"  m_n (validation)     = {mp.nstr(M_N_MEV_VALIDATION, 10)} MeV  (comparison target only)")
    print()

    # H4: full Markov trace evaluation with substrate-derived E_0.
    with mp.workdps(_DPS):
        q0 = mp.mpf(str(Q0_FLOAT))
        tr_p = predict_h4_full_tr_M(habiro, "p (proton, A=1)")
        tr_n = predict_h4_full_tr_M(habiro, "n (neutron, A=1)")

        if tr_p == 0:
            print("  [ERROR] proton tr_M evaluated to 0 — cannot evaluate.")
            return 1

        # Substrate-derived Planck-tick energy scale: E_0 = m_e / (q_0·(q_0-1))
        # Per `prop:three-calibration-inputs` line 52. CAL-1 + CAL-2 only.
        E0 = M_E_MEV / (q0 * (q0 - 1))
        mp_pred = float(mp.fabs(tr_p) * E0)
        # Three-calibration neutron chain: m_n = m_p + Q_β + m_e
        mn_pred = float(mp.mpf(str(mp_pred)) + Q_BETA_MEV + M_E_MEV)

    m_p_val = float(M_P_MEV_VALIDATION)
    m_n_val = float(M_N_MEV_VALIDATION)
    err_p_pct = (mp_pred - m_p_val) / m_p_val * 100
    err_p_ppb = err_p_pct * 1e7
    err_n_pct = (mn_pred - m_n_val) / m_n_val * 100
    err_n_ppb = err_n_pct * 1e7
    E0_MeV = float(E0)

    print(f"  H4 — full tr_M(T_w, q_0) · substrate-derived E_0")
    print(f"    E_0^(N=0) = m_e / (q_0(q_0-1)) = {E0_MeV:.6f} MeV  (CAL-1 + CAL-2)")
    print(f"    tr_M(proton, q_0)  = {mp.nstr(tr_p, 12)}")
    print(f"    tr_M(neutron, q_0) = {mp.nstr(tr_n, 12)}")
    print(f"    proton  pred = {mp_pred:.6f} MeV  (validation {m_p_val})")
    print(f"      err = {err_p_pct:+.4f}%   ({err_p_ppb:+.4e} ppb)")
    print(f"    neutron pred = {mn_pred:.6f} MeV  (validation {m_n_val})")
    print(f"      err = {err_n_pct:+.4f}%   ({err_n_ppb:+.4e} ppb)")
    print(f"      [via three-calibration chain: m_n = m_p + Q_beta + m_e]")
    print()

    # Round-1 baseline reminder
    BASELINE_NEUTRON_PCT = -56.17
    BASELINE_NEUTRON_PPB = -5.6173e8
    print(f"  Round-1 baseline (3-term V_3term + brane tower): "
          f"neutron err = {BASELINE_NEUTRON_PCT:+.2f}%  ({BASELINE_NEUTRON_PPB:+.4e} ppb)")
    print(f"  H4 vs baseline: |H4|/|baseline| = "
          f"{abs(err_n_ppb)/abs(BASELINE_NEUTRON_PPB):.4f}")
    print()

    THRESHOLD_PPB = 1e7  # < 1%
    closed = abs(err_n_ppb) < THRESHOLD_PPB
    if closed:
        verdict = "h4_full_tr_M closes the gap"
        rec = (f"H4 with substrate-derived E_0 brings neutron err to "
               f"{err_n_ppb:+.2e} ppb (< {THRESHOLD_PPB:.0e}). The −56% "
               f"baseline residual was Wedderburn-channel truncation; "
               f"the full symbolic tr_M evaluation at q_0 (packaging "
               f"all cyclotomic residues per "
               f"prop:full-pole-structure-mass-trace) reproduces the "
               f"validation mass within 1 % when paired with the "
               f"canonical Planck-tick E_0 = m_e/(q_0(q_0-1)).")
    else:
        # tr_M(p) ≈ 1.065 from the Habiro witness is normalised to
        # what would pair with E_0 ≈ 881 MeV (the implicit value the
        # previous proton-calibrated form was using), not the
        # substrate-derived Planck-tick E_0 ≈ 4.186 MeV. The previous
        # script absorbed this factor-of-~210 scale mismatch into
        # the calibration tautology m_p = m_p.
        implicit_E0_calibrated = float(mp.fabs(tr_p)) and m_p_val / float(mp.fabs(tr_p))
        verdict = "h4_full_tr_M does NOT close the gap"
        rec = (f"H4 with substrate-derived E_0 gives proton err "
               f"{err_p_ppb:+.2e} ppb, neutron err {err_n_ppb:+.2e} ppb "
               f"(threshold {THRESHOLD_PPB:.0e}). Structural finding: "
               f"tr_M(p, q_0) ≈ {float(mp.fabs(tr_p)):.3f} from the Habiro "
               f"witness is normalised at a scale where the implicit "
               f"E_0_calibrated ≈ {implicit_E0_calibrated:.1f} MeV would match "
               f"m_p, NOT the substrate-derived Planck-tick "
               f"E_0^(N=0) ≈ {E0_MeV:.3f} MeV. The previous proton-calibrated "
               f"form (E_0 = m_p / |tr_M(p)|) absorbed this "
               f"~{(implicit_E0_calibrated/E0_MeV):.0f}x scale discrepancy into "
               f"the calibration tautology m_p = m_p. The mismatch lives in "
               f"either the Habiro tr_M normalisation convention, missing "
               f"brane-tower factors, or in the link between tr_M and "
               f"the substrate Planck-tick scale.")
    print(f"  VERDICT: {verdict}")
    print(f"  RECOMMENDATION: {rec}")
    print()

    # Emit witness via WitnessBuilder (schema-conformant)
    w = (
        WitnessBuilder("neutron-gap-probes-round2", engine="mpmath")
        .set_description(
            "Round-2 neutron-gap probe per prop:full-pole-structure-mass-trace. "
            "Evaluates the FULL symbolic Markov trace tr_M(T_w, q_0) directly "
            "from the Habiro-coefficients witness — no Wedderburn-channel "
            "truncation, no V_3term approximation. Pairs the full tr_M with "
            "the substrate-derived Planck-tick energy scale "
            "E_0 = m_e / (q_0 · (q_0 - 1)) (CAL-1 + CAL-2 only) and the "
            "three-calibration neutron chain m_n = m_p + Q_β + m_e. No "
            "proton-mass calibration: m_p_validation / m_n_validation are "
            "comparison targets only. Workplan-0b Bucket D rewire (PR #759)."
        )
        .set_content_block("prop:full-pole-structure-mass-trace")
        .add_parameter("q_0", Q0_FLOAT)
        .add_parameter("m_e_MeV_CAL1", float(M_E_MEV))
        .add_parameter("Q_beta_MeV_CAL3", float(Q_BETA_MEV))
        .add_parameter("m_p_MeV_validation", float(M_P_MEV_VALIDATION))
        .add_parameter("m_n_MeV_validation", float(M_N_MEV_VALIDATION))
        .add_parameter("E0_substrate_MeV", E0_MeV)
        .add_parameter("precision_dps", _DPS)
        .add_parameter("threshold_ppb", THRESHOLD_PPB)
        # P2.5 marker — script substitutes q_0 numerically before
        # producing output; the symbolic q form is read directly
        # from habiro-coefficients-atomic.witness.json (the upstream
        # symbolic witness). Polynomial exposure does not apply here.
        .add_data("polynomial_q_not_applicable", True)
        .add_data("calibration_inputs_used", {
            "CAL-1": "m_e (M_E_MEV)",
            "CAL-2": "q_0 (from q_parameter.Q)",
            "CAL-3": "Q_beta (Q_BETA_MEV)",
            "uses_m_p_as_calibration": False,
            "uses_m_n_as_calibration": False,
        })
        .add_data("h4_full_tr_M", {
            "tr_M_proton": mp.nstr(tr_p, _DPS),
            "tr_M_neutron": mp.nstr(tr_n, _DPS),
            "E0_form": "E_0^(N=0) = m_e / (q_0 · (q_0 - 1))",
            "E0_MeV": E0_MeV,
            "proton_pred_MeV": mp_pred,
            "neutron_pred_MeV": mn_pred,
            "neutron_chain": "m_n_pred = m_p_pred + Q_beta + m_e",
            "proton_err_pct": err_p_pct,
            "proton_err_ppb": err_p_ppb,
            "neutron_err_pct": err_n_pct,
            "neutron_err_ppb": err_n_ppb,
        })
        .add_data("baseline_round1", {
            "neutron_err_pct": BASELINE_NEUTRON_PCT,
            "neutron_err_ppb": BASELINE_NEUTRON_PPB,
            "source": "PR #452 (probe_neutron_gap.py baseline = 3-term V_3term + brane tower)",
        })
        .add_data("verdict", verdict)
        .add_data("recommendation", rec)
        .add_data("attestation", {
            "used_fitting": False,
            "used_root_find": False,
            "used_volume": False,
            "modifies_baseline_alpha_blend_tower_py": False,
            "uses_habiro_witness_directly": True,
            "uses_proton_mass_calibration": False,
        })
        .add_assertion(
            "proton_pred_within_threshold",
            computed=abs(err_p_ppb),
            expected=0.0,
            tolerance=THRESHOLD_PPB,
            source=(
                "substrate-derived E_0 prediction (CAL-1 + CAL-2 only) "
                "compared against m_p_validation"
            ),
        )
    )
    out_path = w.save()
    print(f"  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
