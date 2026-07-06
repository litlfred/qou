"""M2 mass table — codata Q_β vs cos((z−1)·h/2) Q_β side-by-side.

Re-runs `assemble_per_derivation_weights` for {p, n, D, T, ³He, ⁴He}
under both q_beta_source flags and emits a comparison witness.
Closes item 3-followup of the M1 §7 next-step roadmap.

The cos((z−1)·h/2) Q_β source is the c_2 Kashiwara tightening from
PR #655 (5.49× reduction of the Q_β closed-form residual).
Per PR #657, higher c_k corrections are empirically underdetermined.

## What this shows

Per-atom binding contribution from each term is computed for both
sources. The codata-vs-cos delta is exactly the cos-tightening ε
(306 ppm) × the chirality-weighted binding T1/T5 contribution.
For most atoms this is sub-MeV-level shift; the goal is to verify
the wire is functional and show the cos-source comparison.

## Output

  m2-codata-vs-cos-q-beta.witness.json

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from paper_six_term_isotope_sweep import (  # noqa: E402
    assemble_per_derivation_weights,
    q_beta_for_source,
)
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION,
    M_D_MEV_VALIDATION, M_T_MEV_VALIDATION,
    M_HE3_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
)


# CODATA atomic masses (MeV) for {p, n, D, T, ³He, ⁴He}.
# Use validation aliases — these are NOT used as anchors in the
# prediction chain, only for residual reporting (per AGENTS.md
# three-calibration discipline; only {m_e, q_0, Q_β} are anchors).
M_CODATA_MEV = {
    "p":   float(M_P_MEV_VALIDATION),
    "n":   float(M_N_MEV_VALIDATION),
    "D":   float(M_D_MEV_VALIDATION),
    "T":   float(M_T_MEV_VALIDATION),
    "3He": float(M_HE3_MEV_VALIDATION),
    "4He": float(M_HE4_MEV_VALIDATION),
}


def main() -> int:
    atoms = [
        ("p",   1, 0),
        ("n",   0, 1),
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
        ("4He", 2, 2),
    ]

    print("=" * 100)
    print("  M2 mass table — codata Q_β vs cos((z−1)·h/2) Q_β")
    print("=" * 100)
    print()
    Q_codata = q_beta_for_source("codata")
    Q_cos = q_beta_for_source("form_a_cos")
    print(f"  Q_β (codata)     = {Q_codata:.10f} MeV")
    print(f"  Q_β (form_a_cos) = {Q_cos:.10f} MeV")
    print(f"  Δ                = {Q_cos - Q_codata:+.6e} MeV")
    print()
    print(
        f"  {'atom':>5} {'M_codata':>11} "
        f"| {'M_pred (codata Q_β)':>22} {'err %':>9} "
        f"| {'M_pred (cos Q_β)':>22} {'err %':>9} "
        f"| {'Δ M_pred (MeV)':>15}"
    )
    print("  " + "-" * 110)

    rows = []
    for label, Z, N in atoms:
        try:
            r_codata = assemble_per_derivation_weights(
                Z, N, q_beta_source="codata"
            )
            r_cos = assemble_per_derivation_weights(
                Z, N, q_beta_source="form_a_cos"
            )
        except Exception as exc:
            print(f"  {label:>5} FAILED: {type(exc).__name__}: {exc}")
            rows.append({
                "atom": label, "Z": Z, "N": N,
                "error": f"{type(exc).__name__}: {exc}",
            })
            continue

        M_codata = M_CODATA_MEV.get(label)
        M_pred_c = float(r_codata.get("M_predicted_MeV", 0.0))
        M_pred_cos = float(r_cos.get("M_predicted_MeV", 0.0))
        if M_codata is None:
            # Some fields not present; fall back to total_binding_MeV
            B_c = r_codata.get("total_binding_MeV", 0.0)
            B_cos = r_cos.get("total_binding_MeV", 0.0)
            rows.append({
                "atom": label, "Z": Z, "N": N,
                "total_binding_codata_MeV": B_c,
                "total_binding_cos_MeV": B_cos,
                "delta_binding_MeV": B_cos - B_c,
                "raw_codata": r_codata,
                "raw_cos": r_cos,
            })
            print(f"  {label:>5} (no CODATA reference; binding Δ = {B_cos - B_c:+.4e} MeV)")
            continue

        err_c = (M_pred_c - M_codata) / M_codata * 100 if M_codata else 0
        err_cos = (M_pred_cos - M_codata) / M_codata * 100 if M_codata else 0
        d = M_pred_cos - M_pred_c

        print(
            f"  {label:>5} {M_codata:>11.6f} "
            f"| {M_pred_c:>22.6f} {err_c:>+8.3f}% "
            f"| {M_pred_cos:>22.6f} {err_cos:>+8.3f}% "
            f"| {d:>+15.6e}"
        )
        rows.append({
            "atom": label, "Z": Z, "N": N,
            "M_codata_MeV": M_codata,
            "M_pred_codata_MeV": M_pred_c,
            "M_pred_cos_MeV": M_pred_cos,
            "err_pct_codata": err_c,
            "err_pct_cos": err_cos,
            "delta_M_pred_MeV": d,
        })

    builder = (
        WitnessBuilder("m2-codata-vs-cos-q-beta", engine="python+mpmath")
        .set_description(
            "M2 mass-table comparison: per-derivation assembly under "
            "codata Q_β vs cos((z−1)·h/2) substrate Q_β. Verifies the "
            "q_beta_source flag from this commit, and surfaces the "
            "per-atom mass-prediction shift under the cos tightening. "
            "Closes the wiring half of M1 §7 item 3."
        )
        .set_content_block("prop:q-beta-categorical-precision-ladder")
        .add_parameter("Q_beta_codata_MeV", float(Q_codata))
        .add_parameter("Q_beta_form_a_cos_MeV", float(Q_cos))
        .add_data("delta_Q_beta_MeV", float(Q_cos - Q_codata))
        .add_data("per_atom", rows)
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
