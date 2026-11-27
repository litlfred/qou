#!/usr/bin/env python3
"""
coulomb_radius_from_model_separation_probe.py — bean qou-usft, path 1 (owner card
2026-11-27, recommended option): a ³He Coulomb length from the MODEL's own binding,
not from r₀ = 1.2 fm and not from a selected coefficient on ℏc/m_π.

PRE-REGISTRATION (written before the first run; nothing below was tuned)
-----------------------------------------------------------------------
Corpus rule: every corpus length is a Compton inversion ℏc/mass
(docs/audits/2026-07-13-pion-radius-and-vol-to-radius-gaps.md, GAP 2(d)).
The measured fact behind this path (computations/coulomb_energy.py, qou-usft
block): light-nucleus size tracks BINDING, not nucleon count.

Inputs, all model values read from computations/mass-table-comprehensive.witness.json:
    m_p, m_n           model masses (m_p is a calibration input)
    B(²H), B(³H)       model binding (Q-CLT rows), NOT AME
Strong kernel charge-symmetric (mirror_nuclei_coulomb_systematics), so the model
³He strong binding equals B(³H); the proton separation of ³He → d + p is
    S = B(³H) − B(²H).
Mass scale of the bound tail:  κ = √(2 μ S) / ℏc,  μ = m_d m_p / (m_d + m_p),
m_d = m_p + m_n − B(²H). This is ℏc divided by a mass, so it obeys the corpus rule.

PRIMARY (the one number this probe reports as its result):
    zero-range d+p tail ψ ∝ e^{−κr}/r  ⇒  ⟨r²⟩ = 1/(2κ²),
    r_rms := 1/(√2 κ),  equivalent uniform sphere  R_u := √(5/3)·r_rms,
    ΔE_C(³He−³H) := (3/5)·α ħc·[2·1 − 0]/R_u .
🟨 FLAGGED CHOICE (owner instruction, relayed 2026-11-27): the step from the
tail length 1/κ to an rms radius (zero-range shape, and r measured as the d–p
separation rather than from the centre of charge) is a modelling CHOICE, not a
derivation. The two alternates below are reported so the size of that choice is
visible; they are NOT candidates for selection.

ALTERNATES (reported, never selected):
    (b) R_u := 1/κ                       (tail length used directly)
    (c) R_u := 1/κ₃, κ₃ = √(2 m_N B(³H))/ℏc   (three-body hyperradial tail)
CONTROL (comparison only): the primary formula with AME binding in place of the
model's, to separate "wrong shape" from "wrong binding".

Comparison target, used ONLY for the reported error, never as an input:
AME2020 ³He−³H binding split 0.7638 MeV.

Not wired to the scorecard (owner instruction). Scope (a): whatever it gives is a
statement about this construction alone.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
from _precision import set_compute_dps  # noqa: E402
from coulomb_energy import HBAR_C_MEV_FM, alpha_em_hbar_c_mev_fm  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
except ImportError:  # pragma: no cover
    WitnessBuilder = None

set_compute_dps()

AME_SPLIT_3HE_MEV = mp.mpf("0.76375488")  # comparison only (same value as the mirror witness)


def _rows():
    d = json.loads((COMP / "mass-table-comprehensive.witness.json").read_text())
    return {r["atom"]: r for r in d["data"]["rows"][:4]}


def coulomb_from_R(R):
    return mp.mpf(3) / 5 * alpha_em_hbar_c_mev_fm() * 2 / R


def radii(S, B3, m_p, m_n, B2):
    m_d = m_p + m_n - B2
    mu = m_d * m_p / (m_d + m_p)
    kappa = mp.sqrt(2 * mu * S) / HBAR_C_MEV_FM          # fm^-1
    r_rms = 1 / (mp.sqrt(2) * kappa)
    m_N = (m_p + m_n) / 2
    kappa3 = mp.sqrt(2 * m_N * B3) / HBAR_C_MEV_FM
    return {
        "kappa_fm_inv": kappa,
        "primary_R_u_fm": mp.sqrt(mp.mpf(5) / 3) * r_rms,
        "alt_b_R_u_fm": 1 / kappa,
        "alt_c_R_u_fm": 1 / kappa3,
    }


def main() -> int:
    rows = _rows()
    m_p = mp.mpf(rows["p"]["m_approx_MeV"])
    m_n = mp.mpf(rows["n"]["m_approx_MeV"])
    B2 = mp.mpf(rows["D"]["B_pred_MeV"])
    B3 = mp.mpf(rows["T"]["B_pred_MeV"])
    B2_ame = mp.mpf(rows["D"]["B_AME_MeV"])
    B3_ame = mp.mpf(rows["T"]["B_AME_MeV"])

    out = {}
    for tag, b2, b3 in (("model", B2, B3), ("control_AME", B2_ame, B3_ame)):
        S = b3 - b2
        rr = radii(S, b3, m_p, m_n, b2)
        res = {"S_MeV": S, **rr}
        for k in ("primary", "alt_b", "alt_c"):
            E = coulomb_from_R(rr[f"{k}_R_u_fm"])
            res[f"{k}_dEC_MeV"] = E
            res[f"{k}_rel_err"] = (E - AME_SPLIT_3HE_MEV) / AME_SPLIT_3HE_MEV
        out[tag] = res
        print(f"[{tag}] S = {mp.nstr(S, 8)} MeV, κ = {mp.nstr(rr['kappa_fm_inv'], 8)} fm⁻¹")
        for k in ("primary", "alt_b", "alt_c"):
            print(f"   {k:8s} R_u = {mp.nstr(rr[k + '_R_u_fm'], 6)} fm  ΔE_C = "
                  f"{mp.nstr(res[k + '_dEC_MeV'], 6)} MeV  err = {mp.nstr(100 * res[k + '_rel_err'], 4)} %")

    # reference: the current canonical λ̄_π·A^{1/3} value at A=3 (mirror witness)
    lam = HBAR_C_MEV_FM / mp.mpf("139.57039") * mp.cbrt(3)
    E_lam = coulomb_from_R(lam)
    print(f"[reference] λ̄_π·3^(1/3) = {mp.nstr(lam, 6)} fm  ΔE_C = {mp.nstr(E_lam, 6)} MeV  "
          f"err = {mp.nstr(100 * (E_lam - AME_SPLIT_3HE_MEV) / AME_SPLIT_3HE_MEV, 4)} %")

    if WitnessBuilder is not None:
        wb = WitnessBuilder("coulomb-radius-from-model-separation-probe", engine="mpmath")
        wb.set_description(
            "Bean qou-usft path 1: ³He Coulomb length from the model's own separation energy "
            "S = B_QOU(³H) − B_QOU(²H), κ = √(2μS)/ℏc. Primary: zero-range tail r_rms = 1/(√2κ), "
            "R_u = √(5/3) r_rms — the tail-to-rms step is a FLAGGED CHOICE, not derived. "
            "Alternates (b) 1/κ and (c) three-body 1/κ₃ shown for the size of that choice, never "
            "selected. Control uses AME binding. Not wired to the scorecard. Scope (a).")
        wb.add_data("results", out)
        wb.add_data("reference_lambda_pi_A13", {"R_u_fm": lam, "dEC_MeV": E_lam})
        wb.add_data("comparison_target_MeV", AME_SPLIT_3HE_MEV)
        wb.add_assertion(name="primary_is_positive_and_finite",
                         computed=str(int(out["model"]["primary_dEC_MeV"] > 0)),
                         expected="1", tolerance=0,
                         source="sanity only; no accuracy assertion (scope (a) probe)")
        wb.write(HERE / "coulomb-radius-from-model-separation-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
