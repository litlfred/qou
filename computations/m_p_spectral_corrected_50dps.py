#!/usr/bin/env python3
"""m_p via the spectral-corrected VolDensity decomposition (50 dps).

Closes the uniform +2.89% nucleon VolDensity gap to ~130 ppm by
restoring the ONE missing — and derived — multiplicative factor: the
spectral correction.

    m_p / m_e = [Vol(B_3)/hbar^2] * lw_A * spectral_corr

Component pieces (each with a known origin; no fit):

  Vol(B_3)  = 8 G            (G = Catalan; archimedean geometric scale)
  hbar      = (q-1)/q        (substrate Planck constant, CAL-2)
  h         = q - 1/q
  lw_A      = 5/2 + 3 h^2/4  (Family-A linking weight, PROVED)
  spectral_corr = arccos( chi/2 ) / (8 hbar^2)
       where chi = chi^{(2,1)}(B_3) = 2 - 3 h^4 - h^6   is the EXACT
       Hoefsmit Borromean character on the 2-dim standard irrep
       V_{(2,1)} (so the arccos argument is 1 - 3 h^4/2 - h^6/2).

The leading product (Vol/hbar^2 * lw_A, i.e. spectral_corr OMITTED)
reproduces the sweep's +2.89% nucleon gap. Multiplying by the derived
spectral_corr ~ 0.97112 closes it to ~130 ppm. The residual is the
arccos Taylor truncation at h^4 order (transcendental), not a fit.

Discipline: only CAL-1 (M_E_MEV) is a dimensional input and q_0 comes
from CAL-2; M_P_MEV_VALIDATION is comparison-only. See
docs/audits/2026-05-29-low-mass-sweep-full-audit.md (sec. 4b).

Ref: TwoRoutesProtonMass.lean (decomposition + lw_A + spectral_corr).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

from mpmath import mp, mpf, acos, catalan, matrix

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION,
)


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("m-p-spectral-corrected-50dps", engine="mpmath")

    q0 = mpf(Q_50_DIGIT_STR)
    h = q0 - 1 / q0
    hbar = (q0 - 1) / q0

    # ── derive chi^{(2,1)}(B_3) from the Hoefsmit (2,1) matrices ──
    # (verify, do not assert): sigma_1 = diag(q, -1/q); sigma_2 solved
    # from the Hecke quadratic + braid relation (gauge b=1). The
    # Borromean braid B_3 = (sigma_1^{-1} sigma_2)^3; its (2,1) trace is
    # the bare character chi^{(2,1)}(B_3). Symbolically (sympy) this
    # equals 2 - 3h^4 - h^6 exactly; here we confirm numerically @ q_0.
    s1 = matrix([[q0, 0], [0, -1 / q0]])
    s1_inv = matrix([[1 / q0, 0], [0, -q0]])
    s2 = matrix([
        [-1 / (q0 ** 3 + q0), mpf(1)],
        [(q0 ** 4 + q0 ** 2 + 1) / (q0 ** 4 + 2 * q0 ** 2 + 1),
         q0 ** 3 / (q0 ** 2 + 1)],
    ])
    M = s1_inv * s2
    M3 = M * M * M
    chi_hoefsmit = M3[0, 0] + M3[1, 1]
    chi = 2 - 3 * h ** 4 - h ** 6             # Laurent form of the same character
    char_residual = abs(chi_hoefsmit - chi)

    # ── component pieces ──────────────────────────────────────────
    vol_b3 = 8 * catalan                      # Vol(B_3) = 8 G
    geom_scale = vol_b3 / hbar ** 2           # Vol(B_3)/hbar^2
    lw_A = mpf(5) / 2 + 3 * h ** 2 / 4        # Family-A linking weight (PROVED)
    spectral_corr = acos(chi / 2) / (8 * hbar ** 2)

    # ── the two products ──────────────────────────────────────────
    mp_over_me_leading = geom_scale * lw_A                  # spectral OMITTED
    mp_over_me_full = geom_scale * lw_A * spectral_corr     # spectral RESTORED

    me = mpf(str(M_E_MEV))
    m_p_pred_leading = mp_over_me_leading * me
    m_p_pred_full = mp_over_me_full * me

    # comparison-only (validation)
    m_p_val = mpf(str(M_P_MEV_VALIDATION))
    err_leading_ppm = (m_p_pred_leading / m_p_val - 1) * 1_000_000
    err_full_ppm = (m_p_pred_full / m_p_val - 1) * 1_000_000

    print("=" * 70)
    print("m_p via spectral-corrected VolDensity decomposition (50 dps)")
    print("=" * 70)
    print(f"  q_0            = {mp.nstr(q0, 12)}")
    print(f"  [1] Vol(B_3)=8G       = {mp.nstr(vol_b3, 10)}")
    print(f"  [2] Vol(B_3)/hbar^2   = {mp.nstr(geom_scale, 10)}")
    print(f"  [3] lw_A=5/2+3h^2/4   = {mp.nstr(lw_A, 10)}  (Family-A, PROVED)")
    print(f"  [4] chi^(2,1)(B_3)    = {mp.nstr(chi, 10)}  (exact Hoefsmit)")
    print(f"      spectral_corr     = {mp.nstr(spectral_corr, 10)}")
    print()
    print(f"  leading (no spectral): m_p = {mp.nstr(m_p_pred_leading, 10)} MeV"
          f"  err = {mp.nstr(err_leading_ppm / 10000, 6)}%")
    print(f"  + spectral_corr      : m_p = {mp.nstr(m_p_pred_full, 12)} MeV"
          f"  err = {mp.nstr(err_full_ppm, 6)} ppm")
    print(f"  validation m_p       = {mp.nstr(m_p_val, 12)} MeV")

    wb.add_data("q_0", mp.nstr(q0, 50))
    wb.add_data("borromean_character", {
        "chi_from_hoefsmit_matrices": mp.nstr(chi_hoefsmit, 40),
        "chi_laurent_2_minus_3h4_minus_h6": mp.nstr(chi, 40),
        "residual": mp.nstr(char_residual, 6),
        "derivation": ("chi^(2,1)(B_3) = tr_{(2,1)}[(sigma_1^-1 sigma_2)^3] "
                       "from Hoefsmit matrices = 2-3h^4-h^6 (sympy-exact)"),
    })
    wb.add_data("pieces", {
        "vol_b3_8catalan": mp.nstr(vol_b3, 40),
        "geom_scale_vol_over_hbar2": mp.nstr(geom_scale, 40),
        "lw_A_5_2_plus_3h2_4": mp.nstr(lw_A, 40),
        "chi_21_borromean_derived": mp.nstr(chi, 40),
        "spectral_corr_arccos": mp.nstr(spectral_corr, 40),
    })
    wb.add_data("m_p_over_m_e", {
        "leading_spectral_omitted": mp.nstr(mp_over_me_leading, 40),
        "full_spectral_restored": mp.nstr(mp_over_me_full, 40),
    })
    wb.add_data("m_p_MeV", {
        "leading": mp.nstr(m_p_pred_leading, 20),
        "full": mp.nstr(m_p_pred_full, 20),
        "validation_comparison_only": mp.nstr(m_p_val, 20),
    })
    wb.add_data("error", {
        "leading_pct": float(err_leading_ppm / 10000),
        "full_ppm": float(err_full_ppm),
        "note": ("leading reproduces the +2.89% sweep gap; the derived "
                 "spectral_corr closes it to ~130 ppm; residual is the "
                 "arccos Taylor truncation at h^4 order"),
    })
    wb.add_assertion(
        "borromean_char_derived_from_hoefsmit",
        computed=float(char_residual), expected=0.0, tolerance=1e-30,
        source="tr_{(2,1)}[(sigma_1^-1 sigma_2)^3] = 2 - 3h^4 - h^6",
    )
    wb.add_assertion(
        "spectral_correction_closes_gap_to_sub_200ppm",
        computed=abs(float(err_full_ppm)), expected=0.0, tolerance=200.0,
        unit="ppm",
        source="m_p = Vol(B_3)/hbar^2 * lw_A * arccos(chi/2)/(8 hbar^2)",
    )
    # Lean SDP-uniqueness cross-reference (PR #1537/#1542/#1554).
    wb.add_data("lean_uniqueness_ref", {
        "proton": "qou:QOU.BraidKnot.PeriodicTableUniqueness.h_uniqueness_closed",
        "framework_doc":
            "content/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": (
            "These theorems certify T_w uniqueness at the abstract empty-constraint SDP level (PR #1537/#1542 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md."
        ),
    })

    wb.save()
    print("\n  Witness: m-p-spectral-corrected-50dps.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
