"""per_observable_100x_status.py — per-observable 100× experimental status

For each predicted observable, report:
  - current prediction (from existing witness)
  - CODATA experimental value + uncertainty
  - relative prediction error
  - 100× target = sigma_exp_rel / 100
  - MET / MISS / MISS-BY-N

This is the headline metric for Workplan v7 (1ppb compute AND 100x
experimental precision). Audit-only summary — does not introduce new
predictions, just reads existing witnesses against the 100x bar.

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
REPO_ROOT = COMPUTE_DIR.parent.parent

sys.path.insert(0, str(COMPUTE_DIR))
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

from mpmath import mp, mpf  # noqa: E402

# ─────────────────────────────────────────────────────────────────────────
# CODATA 2022 experimental values + uncertainties (consistent with
# codata_constants.py).
# ─────────────────────────────────────────────────────────────────────────
EXP_VALUES = {
    # absolute masses
    "m_p":      (mpf("938.27208816"),    mpf("0.00000029")),     # MeV
    "m_n":      (mpf("939.56542052"),    mpf("0.00000054")),     # MeV
    "m_e":      (mpf("0.51099895"),      mpf("0.00000000015")),  # MeV (CAL-1)
    "m_mu":     (mpf("105.6583755"),     mpf("0.0000023")),      # MeV
    "m_D":      (mpf("1875.61294257"),   mpf("0.00000057")),     # MeV
    "m_T":      (mpf("2808.92113298"),   mpf("0.00000085")),     # MeV
    "m_3He":    (mpf("2808.39160743"),   mpf("0.00000085")),     # MeV
    "m_4He":    (mpf("3727.37941"),      mpf("0.00000023")),     # MeV
    # derived
    "Q_beta":   (mpf("0.78232"),         mpf("0.00050")),         # MeV (CAL-3)
    "Delta_pn": (mpf("1.29333236"),      mpf("0.00000051")),      # MeV
}


def rel_error_ppb(pred: mpf, codata: mpf) -> mpf:
    return abs(pred - codata) / abs(codata) * mpf("1e9")


def sigma_rel_ppb(codata: mpf, sigma: mpf) -> mpf:
    return sigma / abs(codata) * mpf("1e9")


def load_witness(name: str) -> dict:
    p = COMPUTE_DIR / name
    if not p.exists():
        return {}
    return json.loads(p.read_text())


def main() -> dict:
    rows = []

    # ── m_p, m_n, mu, Delta_pn — from Borromean tower witness ────────
    borr = load_witness("m-p-borromean-verification-50dps.witness.json")
    borr_data = borr.get("data", {})
    borr_witness = (REPO_ROOT.relative_to(REPO_ROOT)
                    / "folio-assistant/computations/m-p-borromean-verification-50dps.witness.json"
                    ).as_posix()

    for obs, key in [
        ("m_p",      "proton.m_p_pred_MeV"),
        ("m_n",      "neutron.m_n_pred_MeV"),
        ("m_mu",     "muon_check.m_mu_pred_MeV"),
        ("Delta_pn", "proton_neutron_split.delta_m_pn_pred_MeV"),
    ]:
        section, field = key.split(".")
        v = borr_data.get(section, {}).get(field)
        if v is None:
            rows.append({"obs": obs, "status": "NO-WITNESS"})
            continue
        pred = mpf(str(v))
        codata, sigma_exp = EXP_VALUES[obs]
        err_ppb = rel_error_ppb(pred, codata)
        sig_ppb = sigma_rel_ppb(codata, sigma_exp)
        target_ppb = sig_ppb / mpf("100")
        miss_factor = err_ppb / target_ppb
        beats_1x = bool(err_ppb < sig_ppb)
        beats_100x = bool(err_ppb < target_ppb)
        rows.append({
            "obs": obs,
            "pred_MeV": fmt(pred, 12),
            "codata_MeV": fmt(codata, 12),
            "err_ppb": fmt(err_ppb, 4),
            "sigma_exp_ppb": fmt(sig_ppb, 4),
            "target_100x_ppb": fmt(target_ppb, 4),
            "miss_factor": fmt(miss_factor, 4),
            "beats_1x_experimental": beats_1x,
            "beats_100x_experimental": beats_100x,
            "source_witness": "m-p-borromean-verification-50dps.witness.json",
        })

    # ── Q_β — from q-beta-predicted witness ──────────────────────────
    qb = load_witness("q-beta-predicted.witness.json")
    qb_pred_data = qb.get("data", {}).get("q_beta_prediction", {})
    v = qb_pred_data.get("Q_beta_pred_MeV")
    if v is not None:
        pred = mpf(str(v))
        codata, sigma_exp = EXP_VALUES["Q_beta"]
        err_ppb = rel_error_ppb(pred, codata)
        sig_ppb = sigma_rel_ppb(codata, sigma_exp)
        target_ppb = sig_ppb / mpf("100")
        miss_factor = err_ppb / target_ppb
        rows.append({
            "obs": "Q_beta",
            "pred_MeV": fmt(pred, 12),
            "codata_MeV": fmt(codata, 12),
            "err_ppb": fmt(err_ppb, 4),
            "sigma_exp_ppb": fmt(sig_ppb, 4),
            "target_100x_ppb": fmt(target_ppb, 4),
            "miss_factor": fmt(miss_factor, 4),
            "beats_1x_experimental": bool(err_ppb < sig_ppb),
            "beats_100x_experimental": bool(err_ppb < target_ppb),
            "source_witness": "q-beta-predicted.witness.json",
        })

    # ── m_e — CAL-1 anchor (by definition err = 0) ───────────────────
    codata, sigma_exp = EXP_VALUES["m_e"]
    sig_ppb = sigma_rel_ppb(codata, sigma_exp)
    rows.append({
        "obs": "m_e",
        "pred_MeV": fmt(codata, 12),
        "codata_MeV": fmt(codata, 12),
        "err_ppb": "0",
        "sigma_exp_ppb": fmt(sig_ppb, 4),
        "target_100x_ppb": fmt(sig_ppb / mpf("100"), 4),
        "miss_factor": "N/A (anchor)",
        "beats_1x_experimental": True,
        "beats_100x_experimental": True,
        "source_witness": "(CAL-1 anchor)",
        "note": "calibration anchor — err defined as 0",
    })

    return {
        "computation": "per-observable-100x-experimental-status",
        "description": (
            "Headline status for Workplan v7: report each predicted "
            "observable's current error against the 100× experimental "
            "target (σ_pred ≤ σ_exp / 100). Audit-only — reads existing "
            "witnesses, does not introduce new predictions."
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
    print(f"\n{'='*120}")
    print(f"Per-observable 100× experimental status (Workplan v7)")
    print(f"{'='*120}")
    print(f"{'Observable':10}  {'pred err (ppb)':>16}  {'σ_exp (ppb)':>14}  "
          f"{'100× target (ppb)':>20}  {'miss factor':>14}  {'beats 1×?':>10}  {'beats 100×?':>11}")
    print("-" * 120)
    for r in out["rows"]:
        if r.get("status") == "NO-WITNESS":
            print(f"{r['obs']:10}  NO WITNESS")
            continue
        print(
            f"{r['obs']:10}  {r['err_ppb']:>16}  {r['sigma_exp_ppb']:>14}  "
            f"{r['target_100x_ppb']:>20}  {r.get('miss_factor', '-'):>14}  "
            f"{('Y' if r['beats_1x_experimental'] else 'N'):>10}  "
            f"{('Y' if r['beats_100x_experimental'] else 'N'):>11}"
        )
    print("-" * 120)
    print(f"Summary: {out['summary']['beats_100x_count']} / {out['summary']['total']} "
          f"observables beat 100× experimental target.")
    print(f"         {out['summary']['beats_1x_count']} / {out['summary']['total']} "
          f"beat 1× experimental.")
    print()
