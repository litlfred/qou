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
    rational function from the Habiro witness.  If the proton-
    calibrated tr_M(neutron, q_0) lands within 1 % of CODATA, the
    −56 % gap was the Wedderburn-truncation phenomenon.  Otherwise
    the gap is elsewhere (T2/T3 brane-tower assembly, T4/T5/T6
    accounting, or brane-tower formulation itself).

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
from experimental_constants import M_P_MEV, M_N_MEV  # noqa: E402
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
    print(f"  m_p (CODATA) = {M_P_MEV} MeV")
    print(f"  m_n (CODATA) = {M_N_MEV} MeV")
    print()

    # H4: full Markov trace evaluation
    with mp.workdps(_DPS):
        tr_p = predict_h4_full_tr_M(habiro, "p (proton, A=1)")
        tr_n = predict_h4_full_tr_M(habiro, "n (neutron, A=1)")

        # Calibrate energy scale on the proton (single point, no fit).
        if tr_p == 0:
            print("  [ERROR] proton tr_M evaluated to 0 — cannot calibrate.")
            return 1

        E0 = mp.mpf(str(M_P_MEV)) / mp.fabs(tr_p)
        mp_pred = float(mp.fabs(tr_p) * E0)  # exact by construction
        mn_pred = float(mp.fabs(tr_n) * E0)

    err_n_pct = (mn_pred - M_N_MEV) / M_N_MEV * 100
    err_n_ppb = err_n_pct * 1e7

    print(f"  H4 — full tr_M(T_w, q_0) direct evaluation")
    print(f"    tr_M(proton, q_0)  = {mp.nstr(tr_p, 12)}")
    print(f"    tr_M(neutron, q_0) = {mp.nstr(tr_n, 12)}")
    print(f"    proton pred = {mp_pred:.6f} MeV  (CODATA {M_P_MEV})")
    print(f"    neutron pred = {mn_pred:.6f} MeV  (CODATA {M_N_MEV})")
    print(f"    neutron err = {err_n_pct:+.4f}%   ({err_n_ppb:+.4e} ppb)")
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
        rec = (f"H4 brings neutron err to {err_n_ppb:+.2e} ppb "
               f"(< {THRESHOLD_PPB:.0e} threshold). The −56% baseline "
               f"residual was Wedderburn-channel truncation; the full "
               f"symbolic tr_M evaluation at q_0 (which packages all "
               f"cyclotomic residues per prop:full-pole-structure-mass-trace) "
               f"reproduces CODATA. Promote: replace V_3term path with "
               f"direct tr_M evaluation, or extend V_3term to include "
               f"all Wedderburn blocks correctly weighted.")
    else:
        verdict = "h4_full_tr_M does NOT close the gap"
        rec = (f"H4 (full tr_M) gives neutron err = {err_n_ppb:+.2e} ppb, "
               f"still above {THRESHOLD_PPB:.0e}. The full pole structure "
               f"alone does not account for the gap; the residual must "
               f"live elsewhere — most likely in the assembly between "
               f"tr_M and the brane-tower (T1 vs T1+T2+T3 mismatch), "
               f"in Term 4/5/6 contributions not yet added, or in a "
               f"normalisation/sign convention discrepancy. Next probe: "
               f"compute T1+T4 (Frobenius co-Casimir) only (no brane "
               f"tower) and see if that lands closer to CODATA, "
               f"isolating the brane-tower contribution.")
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
            "truncation, no V_3term approximation. Tests whether the −56% "
            "neutron residual from round-1 (PR #452) was the cyclotomic-"
            "residue truncation phenomenon. Read-only investigation."
        )
        .set_content_block("prop:full-pole-structure-mass-trace")
        .add_parameter("q_0", Q0_FLOAT)
        .add_parameter("m_p_codata_MeV", M_P_MEV)
        .add_parameter("m_n_codata_MeV", M_N_MEV)
        .add_parameter("precision_dps", _DPS)
        .add_parameter("threshold_ppb", THRESHOLD_PPB)
        .add_data("h4_full_tr_M", {
            "tr_M_proton": mp.nstr(tr_p, _DPS),
            "tr_M_neutron": mp.nstr(tr_n, _DPS),
            "proton_pred_MeV": mp_pred,
            "neutron_pred_MeV": mn_pred,
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
        })
        .add_assertion(
            "proton_calibration_exact",
            computed=mp_pred,
            expected=M_P_MEV,
            tolerance=1e-6,
            source="single-point proton calibration (E0 = m_p / |tr_M(p)|)",
        )
    )
    out_path = w.save()
    print(f"  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
