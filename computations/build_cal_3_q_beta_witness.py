#!/usr/bin/env python3
"""Generator for the Q_β calibration witness (cal-3-q-beta.witness.json).

Replaces the prior hand-authored witness with a script-generated one
sourced from `codata_2022_source`.  Per the 2026-05-23 CODATA
precision-pipeline audit recommendation #4: "Replace
cal-3-q-beta.witness.json storage with a generator from
codata_2022_source.py — eliminates the chance of the witness drifting
from CODATA when an edition update lands."

The witness structure and downstream-consumer list are preserved
verbatim from the prior hand-authored version.

CALIBRATION LABEL — this is CAL-2, not CAL-3
--------------------------------------------
The witness *stem* is `cal-3-q-beta` for historical reasons and is NOT
renamed here (it has its own blast radius).  But the label is wrong and
the corpus fixes it: per AGENTS.md's canonical derivation-chain table and
the owner ruling of 2026-06-26, Q_β is the numerical **proxy for CAL-2**
(the neutron β-decay width, `Q_β = ℏ/𝔇_β`).  **CAL-3 is the pion decay
width `𝔇_π`, whose proxy is `m_π`.**  Every label this producer writes now
says CAL-2; `calibration_id` has no programmatic reader in the repo (two
writers, zero readers), so the correction moves no consumer.

DATASET — CODATA-2022 registry, not the AME-2020 direct value
-------------------------------------------------------------
🟧 OWNER RULING 2026-11-20 (verbatim: "CODATA 2022"), answering the
decision PR #7205 staged (bean `qou-0e2p`).  This producer derives Q_β from the CODATA-2022 registry rather than reading the
AME-2020 direct literal.  Both determinations are in the corpus:

    AME-2020 direct        Q_BETA_MEV_AME      = 0.78233341(61)
    CODATA-2022 registry   Δ_np − m_e          = 0.78233355931(38)

They differ by **+190.85 ppb = +0.208 σ** — statistically
indistinguishable, so this is NOT an accuracy choice and must not be
made on which gives a better residual (AGENTS.md §"NO FITTING, EXCEPT
CAL-1/2/3": accuracy is a diagnostic, never a tie-breaker).  It is a
**dataset-consistency** choice: CAL-1's `m_e` is already served from
`codata.py` at CODATA 2022, so sourcing this one from AME-2020 straddles
two experimental datasets inside one calibration triple — the exact
inconsistency the owner's 2026-08-22 muon-pin ruling excluded, in its
own words, *"CAL-1, CAL-2 and CAL-3 must come from one experimental
dataset."*

ROUTE — Δ_np − m_e, deliberately not m_n − m_p − m_e
----------------------------------------------------
Q_β is derived from `M_N_MINUS_P_MEV`, the registry's own directly
adjusted *neutron-proton mass difference energy equivalent*, minus `m_e`.
That route never touches the stored proton — which matters, because
`docs/audits/2026-08-09-codata-registry-vintage-straddle.md` found the
vendored proton to be the stale member of a mixed-vintage snapshot.  The
alternative route `M_N_MEV_CODATA_DIRECT − M_P_MEV − M_E_MEV` gives the
identical number (they agree to ~1e-49 at 50 dps) and is asserted below as a
cross-check, so the choice of route is verified rather than assumed.

🛑 WHAT THIS COSTS — the consistency check becomes CIRCULAR
------------------------------------------------------------
`codata_constants` carries an internal check that Q_β agrees with
`m_n − m_p − m_e` from the validation witness, with the comment "Q_β is
derived from CAL-1 + CAL-2; this check verifies it agrees ... within
combined CODATA σ".  Under AME-2020 that was a genuine — if weak —
independent comparison of two datasets: residual **1.4931e-7 MeV
(190.85 ppb, 0.22 σ)**.  Under the registry route the two sides are the
same quantity, so the residual collapses to **~1e-49** and the check is
**0 by construction**.

That is a real loss of an independent cross-check, it is a cost of this
change, and PR #7164 §5 did not name it.  It is not a reason to prefer
either option by itself — the check was only ever 0.22 σ, i.e. it had
almost no power to detect anything — but a reader must not mistake the
new ~1e-49 for evidence of improved accuracy.  It is a tautology.  If
the registry route is adopted, that check should be re-pointed at
something genuinely independent (the AME value, now carried alongside as
`Q_beta_n_MeV_ame2020`) or retired, rather than left reporting 1e-17 and
reading as a strong pass.

PRECISION NOTE (2026-11-20).  PR #7205 recorded the two routes as
agreeing "to 7.4e-17".  That figure was binary53 rounding: the
module-level subtractions in `codata_2022_source` and the check in
`codata_constants` ran at the import-time default of 15 dps across a
cancellation from ~939.57 MeV to ~0.78 MeV.  Both now subtract inside
`workdps(50)`, and the routes agree to ~1e-49.

MEASURED DOWNSTREAM MOVE (re-measured 2026-11-20 on main, proton pin)
----------------------------------------------------------------------
L2 dashboard (`per_observable_100x_status.py`): `Q_beta` is the only row
that moves, and only through its experimental sigma.  `codata_MeV`
0.78233341 -> 0.78233355931, `sigma_exp_ppb` 779.7 -> 485.7,
`target_100x_ppb` 7.797 -> 4.857, `miss_factor` 2.139e7 -> 3.434e7.  The
residual `err_ppb` stays 1.668e8 at the printed precision: the ruled
z_D-base prediction misses by -16.7 %, against which a 191 ppb move of
the target is invisible.  Headline unchanged: 1/6 scoreable.

The miss factor gets WORSE because the registry is the more precise
determination (sigma 3.8e-7 vs 6.1e-7), so its own 100x target tightens.
That is an outcome, not a reason; neither the residual nor the miss
factor may choose a dataset (AGENTS.md, NO FITTING).

Convention-C quantities, recorded by `qbeta_cal2_proxy_dataset_delta_probe.py`
and still C-frame (the c_k ladder has not been re-derived under D, bean
qou-cds1): c_3 -2.0693425771 -> -1.7604548585, and the `c_3 ~ -2`
near-match goes 3.4671 % -> 11.9773 %.  The probe's own "L2 dashboard"
section reports the retired N=2 C-frame base (1278.58 ppb, 164.0x); it is
NOT what the dashboard scores today.

-- Ref: [leitner2026] beans qou-0e2p, qou-cds1; PRs #7205, #7164, #4860
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from mpmath import mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_2022_source import (  # noqa: E402
    M_E_MEV,
    M_N_MINUS_P_MEV,
    M_N_MINUS_P_MEV_ERR,
    Q_BETA_MEV_AME,
    Q_BETA_MEV_AME_ERR,
    Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT,
)


def main() -> int:
    # Q_β from the CODATA-2022 registry: the directly adjusted
    # neutron-proton mass-difference energy equivalent, minus m_e.
    # mpf end to end -- these come out of `_load_mpf`, so no float64
    # enters here (AGENTS.md NO-FLOAT64).
    with mp.workdps(50):
        q_beta = +(M_N_MINUS_P_MEV - M_E_MEV)
    q_beta_err = M_N_MINUS_P_MEV_ERR

    # Cross-check the other registry route (m_n_direct - m_p - m_e).
    # Verifying rather than assuming that the route choice is immaterial:
    # this is what establishes that the value does not inherit the stale
    # proton of the 2026-08-09 vintage straddle.
    route_gap = abs(q_beta - Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT)
    if route_gap > 1e-12:
        raise SystemExit(
            "REFUSING: the two CODATA-2022 routes to Q_beta disagree by "
            f"{route_gap} MeV (> 1e-12). (Delta_np - m_e) and "
            "(m_n_direct - m_p - m_e) must agree; if they do not, one of "
            "the registry entries has moved and the CAL-2 proxy cannot be "
            "derived until that is resolved. Do not paper over this by "
            "picking a route."
        )

    # Separation from the AME-2020 determination, recorded so a reader can
    # see the size of the dataset choice without re-deriving it.
    with mp.workdps(50):
        ame_gap_ppb = (q_beta - Q_BETA_MEV_AME) / Q_BETA_MEV_AME * 10 ** 9

    # engine must be a witness-schema enum value; the CODATA-2022
    # provenance is recorded as a parameter below.
    w = WitnessBuilder("cal-3-q-beta", engine="python")
    w.add_parameter(
        "source",
        "CODATA 2022 registry: neutron-proton mass difference energy "
        "equivalent (1.29333251(38) MeV) minus m_e.",
    )
    w.set_description(
        "CAL-2 proxy: free-neutron β-decay Q-value Q_β(n), derived from "
        "the CODATA-2022 registry as (m_n − m_p) − m_e. Per the QOU "
        "three-calibration discipline "
        "(folio/quantum-observable-universe/braids-and-knots/"
        "three-calibration-inputs.md), Q_β(n) is the numerical proxy for "
        "CAL-2, the neutron β-decay width 𝔇_β with Q_β = ℏ/𝔇_β — NOT "
        "CAL-3, which is the pion decay width 𝔇_π with proxy m_π (owner "
        "ruling 2026-06-26; the witness stem 'cal-3-q-beta' is historical "
        "and is kept only to avoid a rename blast radius). It fixes the "
        "hadronic energy scale E_0 via E_0 = Q_β(n) / |Δ(net)|, where "
        "Δ(net) = h(h-2)/2 is the symbolic NF difference between neutron "
        "and proton braids. This witness exists so codata_constants.py "
        "loads the value from a source-of-truth JSON instead of "
        "hardcoding it. DATASET (owner ruling 2026-11-20, \"CODATA 2022\"; "
        "bean qou-0e2p / PR #7205): sourced from the CODATA-2022 registry "
        "rather than the AME-2020 direct value 0.78233341(61), so that "
        "CAL-1, CAL-2 and CAL-3 come from one experimental dataset. The "
        "two determinations differ by +190.85 ppb = +0.208 σ — "
        "statistically indistinguishable, so this is a dataset-"
        "consistency choice and NOT an accuracy claim; the residual "
        "direction is an outcome, never a reason."
    )
    w.set_content_block("def:three-calibration-discipline")
    w.set_audit_only("docs/audits/2026-05-10-1ppb-workplan-update.md")

    w.add_parameter("calibration_id", "CAL-2")
    w.add_parameter(
        "calibration_id_note",
        "Q_β is the CAL-2 proxy (CAL-2 = 𝔇_β, the neutron β-decay width, "
        "Q_β = ℏ/𝔇_β). CAL-3 is 𝔇_π with proxy m_π. This witness read "
        "'CAL-3' until 2026-11-20 on main (PR #7205 first corrected it on 2026-09-12 but never merged); the stem is historical, the label was "
        "simply wrong against AGENTS.md's canonical table.",
    )
    w.add_parameter(
        "role",
        "Hadronic energy scale E_0 via E_0 = Q_β(n) / |Δ(net)|",
    )
    w.add_parameter(
        "data_source",
        "CODATA-2022 neutron-proton mass difference energy equivalent "
        "1.29333251(38) MeV, minus m_e = 0.51099895069 MeV. Sourced from "
        "codata_2022_source.M_N_MINUS_P_MEV − M_E_MEV, and cross-checked "
        "against M_N_MEV_CODATA_DIRECT − M_P_MEV − M_E_MEV (agree to "
        "~1e-49 at 50 dps). Was codata_2022_source.Q_BETA_MEV_AME (AME-2020 "
        "direct, 0.78233341(61)) until 2026-11-20.",
    )
    w.add_parameter(
        "uncertainty_convention",
        "one-sigma combined standard uncertainty, k=1",
    )
    w.add_parameter("units", "MeV")

    w.add_data("Q_beta_n_MeV", str(q_beta))
    w.add_data("Q_beta_n_MeV_err", str(q_beta_err))
    w.add_data(
        "Q_beta_n_MeV_quoted",
        "0.78233355931(38) MeV (CODATA 2022: (m_n − m_p) − m_e)",
    )
    # The superseded determination, kept beside the live one so a reader
    # can see the dataset choice in the witness itself.
    w.add_data("Q_beta_n_MeV_ame2020", str(Q_BETA_MEV_AME))
    w.add_data("Q_beta_n_MeV_ame2020_err", str(Q_BETA_MEV_AME_ERR))
    w.add_data("codata2022_minus_ame2020_ppb", mp.nstr(ame_gap_ppb, 30))
    w.add_data("dataset", "CODATA 2022")
    w.add_data(
        "consistency_check_is_now_circular",
        "codata_constants checks Q_beta against m_n - m_p - m_e. Under "
        "AME-2020 that residual was 1.4931e-7 MeV (190.85 ppb, 0.22 "
        "sigma) -- a genuine cross-dataset comparison. Under this "
        "CODATA-2022 route the two sides are the same quantity, so it is "
        "~1e-49, i.e. ZERO BY CONSTRUCTION. Do not read that as improved "
        "accuracy; the check has lost its (already slight) independence "
        "and should be re-pointed at Q_beta_n_MeV_ame2020 or retired.",
    )
    w.add_data("decay_channel", "n → p + e⁻ + ν̄_e")
    w.add_data("downstream_consumers", [
        "codata_constants.Q_BETA_MEV",
        "E_0_MeV anchor in canonical-mass-table.witness.json",
        "free_neutron_decay.py NF-coefficient extraction",
        "c_alpha_from_Q_beta_trace.py β-chain α-cluster derivation",
        "neutron-gap-probes-round3.witness.json 3-input mass split: "
        "m_n_pred = m_p_pred + Q_β + m_e",
    ])

    out = w.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
