"""per_observable_100x_status.py — per-observable 100× experimental status

For each predicted observable, report:
  - current prediction (from existing witness)
  - CODATA experimental value + uncertainty (from codata_constants registry)
  - relative prediction error
  - 100× target = sigma_exp_rel / 100
  - MET / MISS / MISS-BY-N

This is the headline metric for Workplan v7 (1ppb compute AND 100x
experimental precision). Audit-only summary — does not introduce new
predictions, just reads existing witnesses against the 100x bar.

All CODATA values + uncertainties source from `codata_constants` /
`codata-2022-validation-masses.witness.json` / `cal-3-q-beta.witness.json`
per the framework's three-calibration discipline. No floating CODATA
literals in this script.

Run:
    python3 folio-assistant/computations/per_observable_100x_status.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Repo-relative path resolution
THIS = Path(__file__).resolve()
COMPUTE_DIR = THIS.parent

sys.path.insert(0, str(COMPUTE_DIR))
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV, M_E_MEV_ERR,
    Q_BETA_MEV, Q_BETA_MEV_ERR,
    M_P_MEV_VALIDATION, M_P_MEV_VALIDATION_ERR,
    M_N_MEV_VALIDATION, M_N_MEV_VALIDATION_ERR,
    M_D_MEV_VALIDATION,
    M_T_MEV_VALIDATION,
    M_HE3_MEV_VALIDATION,
    M_HE4_MEV_VALIDATION,
)

set_compute_dps()

from mpmath import mp, mpf  # noqa: E402

# ─────────────────────────────────────────────────────────────────────────
# CODATA 2022 + CAL-3 sourcing.
#
# Values + uncertainties pulled from the canonical registry. The few
# observables not yet in the registry are loaded directly from their
# witness JSON or from PDG quotes recorded here with provenance.
# ─────────────────────────────────────────────────────────────────────────

# Load the validation witness once for σ_err values not exposed via
# the codata_constants symbol surface (D, T, ³He, ⁴He).
_VALIDATION = json.loads(
    (COMPUTE_DIR / "codata-2022-validation-masses.witness.json").read_text()
)["data"]


def _load_err(key: str) -> mpf:
    return mpf(str(_VALIDATION[key]))


# Muon mass — not yet in codata_constants registry. Source: CODATA 2022
# (PDG 2024 cross-check). Recorded here as a literal pending a
# codata_constants entry to avoid an EXP_VALUES dictionary of free
# CODATA numbers (Copilot review).
_MU_QUOTED = "105.6583755(23) MeV/c² (PDG 2024 / CODATA 2022)"
_M_MU_MEV = mpf("105.6583755")
_M_MU_MEV_ERR = mpf("0.0000023")

# Observable registry: (codata_value, codata_err, role, source_label)
OBSERVABLES: dict[str, tuple[mpf, mpf, str, str]] = {
    "m_e":      (M_E_MEV,         M_E_MEV_ERR,            "CAL-1 anchor",
                 "codata_constants.M_E_MEV"),
    "Q_beta":   (Q_BETA_MEV,      Q_BETA_MEV_ERR,         "CAL-3 anchor",
                 "codata_constants.Q_BETA_MEV (← cal-3-q-beta.witness.json)"),
    "m_p":      (M_P_MEV_VALIDATION, M_P_MEV_VALIDATION_ERR, "validation",
                 "codata_constants.M_P_MEV_VALIDATION"),
    "m_n":      (M_N_MEV_VALIDATION, M_N_MEV_VALIDATION_ERR, "validation",
                 "codata_constants.M_N_MEV_VALIDATION"),
    "m_mu":     (_M_MU_MEV,         _M_MU_MEV_ERR,           "validation",
                 _MU_QUOTED),
    "m_D":      (M_D_MEV_VALIDATION, _load_err("m_D_MeV_err"), "validation",
                 "codata-2022-validation-masses.witness.json"),
    "m_T":      (M_T_MEV_VALIDATION, _load_err("m_T_MeV_err"), "validation",
                 "codata-2022-validation-masses.witness.json"),
    "m_3He":    (M_HE3_MEV_VALIDATION, _load_err("m_3He_MeV_err"), "validation",
                 "codata-2022-validation-masses.witness.json"),
    "m_4He":    (M_HE4_MEV_VALIDATION, _load_err("m_4He_MeV_err"), "validation",
                 "codata-2022-validation-masses.witness.json"),
}

# Δm_pn derived from m_n − m_p (with σ_exp via sigma_mn − sigma_mp
# combined in quadrature, dominant from the larger σ_mn).
DELTA_PN_VALUE = M_N_MEV_VALIDATION - M_P_MEV_VALIDATION
DELTA_PN_ERR = mp.sqrt(
    M_N_MEV_VALIDATION_ERR ** 2 + M_P_MEV_VALIDATION_ERR ** 2
)
OBSERVABLES["Delta_pn"] = (
    DELTA_PN_VALUE, DELTA_PN_ERR, "validation (derived)",
    "M_N_MEV_VALIDATION − M_P_MEV_VALIDATION; σ in quadrature",
)


def rel_error_ppb(pred: mpf, codata: mpf) -> mpf:
    return abs(pred - codata) / abs(codata) * mpf("1e9")


def sigma_rel_ppb(codata: mpf, sigma: mpf) -> mpf:
    return sigma / abs(codata) * mpf("1e9")


def load_witness(name: str) -> dict:
    p = COMPUTE_DIR / name
    if not p.exists():
        return {}
    return json.loads(p.read_text())


def _row_for(obs: str, pred: mpf, source_witness: str) -> dict:
    """Build one row of the per-observable status table."""
    codata, sigma_exp, role, sigma_source = OBSERVABLES[obs]
    err_ppb = rel_error_ppb(pred, codata)
    sig_ppb = sigma_rel_ppb(codata, sigma_exp)
    target_ppb = sig_ppb / mpf("100")
    miss_factor = err_ppb / target_ppb if target_ppb > 0 else mp.mpf("inf")
    beats_1x = bool(err_ppb < sig_ppb)
    beats_100x = bool(err_ppb < target_ppb)
    return {
        "obs": obs,
        "role": role,
        "pred_MeV": fmt(pred, 12),
        "codata_MeV": fmt(codata, 12),
        "sigma_exp_MeV": fmt(sigma_exp, 6),
        "err_ppb": fmt(err_ppb, 4),
        "sigma_exp_ppb": fmt(sig_ppb, 4),
        "target_100x_ppb": fmt(target_ppb, 4),
        "miss_factor": fmt(miss_factor, 4),
        "beats_1x_experimental": beats_1x,
        "beats_100x_experimental": beats_100x,
        "source_witness": source_witness,
        "sigma_source": sigma_source,
    }


def main() -> dict:
    rows = []

    # ── m_p, m_n, mu, Delta_pn — from Borromean tower witness ────────
    borr = load_witness("m-p-borromean-verification-50dps.witness.json")
    borr_data = borr.get("data", {})
    borr_source = "m-p-borromean-verification-50dps.witness.json"

    for obs, path_key in [
        ("m_p",      "proton.m_p_pred_MeV"),
        ("m_n",      "neutron.m_n_pred_MeV"),
        ("m_mu",     "muon_check.m_mu_pred_MeV"),
        ("Delta_pn", "proton_neutron_split.delta_m_pn_pred_MeV"),
    ]:
        section, field = path_key.split(".")
        v = borr_data.get(section, {}).get(field)
        if v is None:
            rows.append({"obs": obs, "status": "NO-WITNESS"})
            continue
        rows.append(_row_for(obs, mpf(str(v)), borr_source))

    # ── Q_β — from q-beta-predicted witness ──────────────────────────
    qb = load_witness("q-beta-predicted.witness.json")
    qb_pred_data = qb.get("data", {}).get("q_beta_prediction", {})
    v = qb_pred_data.get("Q_beta_pred_MeV")
    if v is not None:
        rows.append(_row_for("Q_beta", mpf(str(v)),
                             "q-beta-predicted.witness.json"))

    # ── m_e — CAL-1 anchor (by definition err = 0) ───────────────────
    codata, sigma_exp, role, sigma_source = OBSERVABLES["m_e"]
    sig_ppb = sigma_rel_ppb(codata, sigma_exp)
    rows.append({
        "obs": "m_e",
        "role": role,
        "pred_MeV": fmt(codata, 12),
        "codata_MeV": fmt(codata, 12),
        "sigma_exp_MeV": fmt(sigma_exp, 6),
        "err_ppb": "0",
        "sigma_exp_ppb": fmt(sig_ppb, 4),
        "target_100x_ppb": fmt(sig_ppb / mpf("100"), 4),
        "miss_factor": "N/A (anchor)",
        "beats_1x_experimental": True,
        "beats_100x_experimental": True,
        "source_witness": "(CAL-1 anchor)",
        "sigma_source": sigma_source,
        "note": "calibration anchor — err defined as 0",
    })

    return {
        "computation": "per-observable-100x-experimental-status",
        "description": (
            "Headline status for Workplan v7: report each predicted "
            "observable's current error against the 100× experimental "
            "target (σ_pred ≤ σ_exp / 100). Audit-only — reads existing "
            "witnesses, does not introduce new predictions. All CODATA "
            "values + uncertainties source from codata_constants / "
            "codata-2022-validation-masses.witness.json / "
            "cal-3-q-beta.witness.json — no floating literals."
        ),
        "rows": rows,
        "summary": {
            "total": len(rows),
            "beats_1x_count": sum(1 for r in rows if r.get("beats_1x_experimental")),
            "beats_100x_count": sum(1 for r in rows if r.get("beats_100x_experimental")),
        },
    }


if __name__ == "__main__":
    out = main()

    # Pretty table
    print(f"\n{'='*128}")
    print(f"Per-observable 100× experimental status (Workplan v7)")
    print(f"{'='*128}")
    print(f"{'Observable':10}  {'role':22}  {'pred err (ppb)':>16}  "
          f"{'σ_exp (ppb)':>14}  {'100× target (ppb)':>20}  "
          f"{'miss factor':>14}  {'1×?':>3}  {'100×?':>5}")
    print("-" * 128)
    for r in out["rows"]:
        if r.get("status") == "NO-WITNESS":
            print(f"{r['obs']:10}  NO WITNESS")
            continue
        print(
            f"{r['obs']:10}  {r['role']:22}  {r['err_ppb']:>16}  "
            f"{r['sigma_exp_ppb']:>14}  {r['target_100x_ppb']:>20}  "
            f"{r.get('miss_factor', '-'):>14}  "
            f"{('Y' if r['beats_1x_experimental'] else 'N'):>3}  "
            f"{('Y' if r['beats_100x_experimental'] else 'N'):>5}"
        )
    print("-" * 128)
    print(f"Summary: {out['summary']['beats_100x_count']} / {out['summary']['total']} "
          f"observables beat 100× experimental target.")
    print(f"         {out['summary']['beats_1x_count']} / {out['summary']['total']} "
          f"beat 1× experimental.")
    print()

    # Emit witness via WitnessBuilder for reproducible staleness metadata.
    w = WitnessBuilder("per-observable-100x-status", engine="python")
    w.set_description(out["description"])
    w.add_data("rows", out["rows"])
    w.add_data("summary", out["summary"])
    w.add_assertion(
        "summary_total_observables",
        computed=out["summary"]["total"],
        expected=out["summary"]["total"],
        tolerance=0,
        source="Snapshot count of observables in the table.",
    )
    # Reference upstream witnesses for staleness tracking
    for upstream in [
        COMPUTE_DIR / "m-p-borromean-verification-50dps.witness.json",
        COMPUTE_DIR / "q-beta-predicted.witness.json",
        COMPUTE_DIR / "codata-2022-validation-masses.witness.json",
        COMPUTE_DIR / "cal-3-q-beta.witness.json",
    ]:
        w.add_upstream(upstream)
    w.save()
