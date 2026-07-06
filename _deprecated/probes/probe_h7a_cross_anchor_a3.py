"""F2 — H7a cross-anchor probe at A = 3 (³He = D + p, T = D + n).

Forward step from `docs/audits/2026-05-15-three-pr-integration.md` §F2.
Tests whether the H7a finding from PR #645

    Δ_coupling(Z, N) ≈ [A − 2]_q · E_0 · log(1/h(q_0))

(which closes the (2, 2) doubly-magic anchor to +0.169 %) generalises
to A = 3 by computing the analogous one-step magic-shell anchor and
comparing.

## Decomposition convention

For (2, 2) ⁴He, PR #645 sets the anchor as

    Δ_coupling(2, 2) := Δ_cat(⁴He) − 2 · Δ_cat(³He)

i.e., the *non-additivity gap* of ⁴He vs two ³He. The natural one-step
analogue at A = 3 is

    Δ_coupling(2, 1) := Δ_cat(³He) − Δ_cat(D) − Δ_cat(p)
    Δ_coupling(1, 2) := Δ_cat(T)   − Δ_cat(D) − Δ_cat(n)

i.e., ³He / T as a *bound state* of (D + extra nucleon).

## Predicted ratio under H7a

    H7a(A) = [A − 2]_q · E_0 · log(1/h(q_0))
    [0]_q = 0     ⇒ H7a(A=2)  = 0
    [1]_q = 1     ⇒ H7a(A=3)  = E_0 · log(1/h)         ≈ 6.55 MeV
    [2]_q ≈ 2.011 ⇒ H7a(A=4) ≈ 2.011 · E_0 · log(1/h)  ≈ 13.17 MeV

If H7a holds at A = 3, both (2, 1) and (1, 2) anchors should equal
E_0 · log(1/h) at q_0; the T ↔ ³He spin involution should leave them
identical.

Three-cal discipline note: this script does NOT fit Δ_coupling to AME.
The Δ_cat inputs are read from `magic-shell-empirical-instantiation.
witness.json` (computed from {q_0, m_e, m_p, m_n, Q_β}); the H7a
prediction uses only {q_0, m_e}. Output is a comparison witness, not
a calibration.

Run:
    python computations/probe_h7a_cross_anchor_a3.py

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # CODATA-2022 full precision


def _mpf_from_str(s: str) -> mp.mpf:
    return mp.mpf(s)


def main() -> int:
    # ── Inputs from PR #644's empirical-instantiation witness ────────
    msei_path = HERE / "magic-shell-empirical-instantiation.witness.json"
    with msei_path.open() as f:
        msei = json.load(f)
    pad = msei["data"]["per_atom_delta_cat"]
    dc = {
        atom: _mpf_from_str(pad[atom_key]["delta_cat_MeV_50dps"])
        for atom, atom_key in (
            ("proton", "proton"),
            ("neutron", "neutron"),
            ("D", "deuteron"),
            ("T", "tritium"),
            ("He3", "he3"),
            ("He4", "he4"),
        )
    }

    # ── Substrate at 50 dps ──────────────────────────────────────────
    # Canonical 50-dps q_0 (CAL-2) from q_parameter.Q_50_DIGIT_STR.
    q0 = mp.mpf(Q_50_DIGIT_STR)
    m_e = M_E_MEV  # from codata_constants
    e0 = m_e / (q0 * (q0 - 1))
    t_h = q0 - 1 / q0  # Hecke deformation h
    f_h = mp.log(1 / t_h)

    # ── Anchors ──────────────────────────────────────────────────────
    anchor_22 = dc["He4"] - 2 * dc["He3"]
    anchor_21 = dc["He3"] - dc["D"] - dc["proton"]
    anchor_12 = dc["T"] - dc["D"] - dc["neutron"]

    # ── H7a predictions ──────────────────────────────────────────────
    def q_int(n: int) -> mp.mpf:
        if n == 0:
            return mp.mpf(0)
        return (q0 ** n - q0 ** (-n)) / (q0 - 1 / q0)

    h7a_a3 = q_int(1) * e0 * f_h  # [1]_q = 1
    h7a_a4 = q_int(2) * e0 * f_h  # [2]_q = q + q⁻¹

    def gap_pct(actual: mp.mpf, pred: mp.mpf) -> mp.mpf:
        return 100 * (pred - actual) / actual

    # ── Build witness ────────────────────────────────────────────────
    builder = (
        WitnessBuilder("h7a-cross-anchor-a3-probe", engine="mpmath")
        .set_description(
            "F2 forward step from #644⊕#645⊕#652 three-PR integration: "
            "test whether H7a's [A−2]_q · E_0 · log(1/h) closed form "
            "generalises from the (2,2) doubly-magic anchor to the A=3 "
            "anchors (³He = D+p) and (1,2) (T = D+n). Diagnostic — NOT "
            "a fit (three-cal discipline)."
        )
        .set_content_block("conj:magic-shell-stabilization")
        .add_parameter("mp_dps", mp.mp.dps)
        .add_parameter(
            "delta_cat_source",
            "magic-shell-empirical-instantiation.witness.json#per_atom_delta_cat",
        )
        .add_parameter("q_0_50dps", mp.nstr(q0, 50))
        .add_parameter("E_0_MeV_50dps", mp.nstr(e0, 50))
        .add_parameter("h_50dps", mp.nstr(t_h, 50))
        .add_parameter("log_one_over_h_50dps", mp.nstr(f_h, 50))
        .add_parameter("q_int_1", mp.nstr(q_int(1), 50))
        .add_parameter("q_int_2", mp.nstr(q_int(2), 50))
        .add_data(
            "delta_cat_inputs_MeV_50dps",
            {atom: mp.nstr(v, 50) for atom, v in dc.items()},
        )
        .add_data(
            "anchor_22_doubly_magic",
            {
                "Z": 2, "N": 2, "A": 4,
                "decomposition": "Δ_cat(⁴He) − 2·Δ_cat(³He)",
                "value_MeV_50dps": mp.nstr(anchor_22, 50),
                "H7a_prediction_MeV_50dps": mp.nstr(h7a_a4, 50),
                "gap_pct_50dps": mp.nstr(gap_pct(anchor_22, h7a_a4), 12),
            },
        )
        .add_data(
            "anchor_21_he3_eq_d_plus_p",
            {
                "Z": 2, "N": 1, "A": 3,
                "decomposition": "Δ_cat(³He) − Δ_cat(D) − Δ_cat(p)",
                "value_MeV_50dps": mp.nstr(anchor_21, 50),
                "H7a_prediction_MeV_50dps": mp.nstr(h7a_a3, 50),
                "gap_pct_50dps": mp.nstr(gap_pct(anchor_21, h7a_a3), 12),
            },
        )
        .add_data(
            "anchor_12_t_eq_d_plus_n",
            {
                "Z": 1, "N": 2, "A": 3,
                "decomposition": "Δ_cat(T) − Δ_cat(D) − Δ_cat(n)",
                "value_MeV_50dps": mp.nstr(anchor_12, 50),
                "H7a_prediction_MeV_50dps": mp.nstr(h7a_a3, 50),
                "gap_pct_50dps": mp.nstr(gap_pct(anchor_12, h7a_a3), 12),
            },
        )
        .add_data(
            "z_n_asymmetry_a3",
            {
                "description": (
                    "Under H7a's [A−2]_q · E_0 · log(1/h), the (2,1) and "
                    "(1,2) anchors must be identical — H7a depends only on "
                    "A, not on (Z, N) separately. Any non-zero "
                    "ratio_minus_one signals that H7a is missing a Z↔N-"
                    "symmetry-breaking term (or that the decomposition "
                    "convention itself is non-trivial)."
                ),
                "anchor_21_minus_anchor_12_MeV": mp.nstr(
                    anchor_21 - anchor_12, 50
                ),
                "ratio_21_over_12": mp.nstr(anchor_21 / anchor_12, 50),
                "ratio_minus_one_pct": mp.nstr(
                    100 * (anchor_21 / anchor_12 - 1), 12
                ),
            },
        )
        .add_caveat(
            "H7a's quantum-integer prefactor [A−2]_q is Z↔N-symmetric by "
            "construction (depends only on A). The A=3 anchors are NOT "
            "Z↔N-symmetric (T = mirror of ³He but the bound-state "
            "spectra differ via Q_β-encoded charge structure). This "
            "probe verifies the magnitude of the asymmetry against the "
            "H7a baseline."
        )
        .add_caveat(
            "Three-cal discipline: the Δ_cat inputs depend on m_e (CAL-1), "
            "q_0 (CAL-2), and Q_β (CAL-3) only. No Δ_coupling AME fit."
        )
    )

    # ── Assertions (diagnostic only — no pass/fail closure claim) ────
    builder.add_assertion(
        name="h7a_a4_gap_pct",
        computed=float(gap_pct(anchor_22, h7a_a4)),
        expected=0.169,
        tolerance=0.05,
        unit="percent",
        source="anchor_22_doubly_magic.gap_pct vs PR #645 H7a finding",
    )
    builder.add_assertion(
        name="h7a_a3_z_n_asymmetry_pct",
        computed=float(100 * (anchor_21 / anchor_12 - 1)),
        expected=0.0,
        tolerance=0.5,
        unit="percent",
        source=(
            "If H7a is universal, (2,1) and (1,2) anchors must agree "
            "(both depend only on A=3). Asymmetry > 0.5% refutes "
            "naive universality."
        ),
    )

    # ── Emit ─────────────────────────────────────────────────────────
    out_path = builder.save()

    print(f"=== H7a cross-anchor probe at A = 3 ===")
    print(f"Anchor (2,2) ⁴He − 2·³He = {mp.nstr(anchor_22, 12)} MeV")
    print(f"  H7a (A=4)              = {mp.nstr(h7a_a4, 12)} MeV")
    print(f"  gap                    = {mp.nstr(gap_pct(anchor_22, h7a_a4), 8)} %")
    print()
    print(f"Anchor (2,1) ³He = D + p = {mp.nstr(anchor_21, 12)} MeV")
    print(f"  H7a (A=3)              = {mp.nstr(h7a_a3, 12)} MeV")
    print(f"  gap                    = {mp.nstr(gap_pct(anchor_21, h7a_a3), 8)} %")
    print()
    print(f"Anchor (1,2) T  = D + n  = {mp.nstr(anchor_12, 12)} MeV")
    print(f"  H7a (A=3)              = {mp.nstr(h7a_a3, 12)} MeV")
    print(f"  gap                    = {mp.nstr(gap_pct(anchor_12, h7a_a3), 8)} %")
    print()
    asy = 100 * (anchor_21 / anchor_12 - 1)
    print(f"Z↔N asymmetry: (anchor_21 − anchor_12)/anchor_12 = {mp.nstr(asy, 8)} %")
    print()
    print(f"Witness emitted: {out_path}")

    all_passed = all(a.passed for a in builder.assertions)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
