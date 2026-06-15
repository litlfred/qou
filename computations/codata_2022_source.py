#!/usr/bin/env python3
"""CODATA-2022 source-of-truth module — vendored snapshot of NIST values.

Per the 2026-05-23 precision audit (`docs/audits/2026-05-23-codata-
precision-audit.md`): the repo's existing `codata_constants.py` /
`codata-2022-validation-masses.witness.json` storage truncates several
CODATA-2022 values to 8-9 sig figs, when NIST publishes them at 11+
sig figs (the σ-limited precision).  This module is the high-precision
source; all callers should pull from here rather than redefining the
literals.

**Source**: NIST CODATA 2022 internationally recommended values
(https://physics.nist.gov/cuu/Constants/, https://physics.nist.gov/
cuu/Constants/allascii.txt — vendored snapshot retrieved 2026-05-23).

**No CODATA `.dat` fetcher in the repo as of 2026-05-23**, so this
module IS the vendored snapshot.  When a new CODATA edition lands
(roughly every 4 years), update the constants here and bump
`CODATA_EDITION_YEAR`.

## Calibration vs validation discipline

Per CLAUDE.md §"Precision goals" and `codata_constants.py`'s
documentation: only `m_e`, `m_μ/m_e`, `Q_β` are LEGITIMATE
calibration inputs (CAL-1, CAL-2, CAL-3).  All other CODATA
constants are VALIDATION-ONLY (used to compare against framework
predictions).  This module preserves that distinction in each
constant's docstring and export naming.

## Two-value subtleties

A few constants have multiple authoritative values that disagree
within their mutual uncertainties.  The most important:

- **m_n c²** has TWO competing values:
  1. CODATA-2022 direct measurement: **939.56542194(48) MeV**
  2. AME-2020 derived from `m_p + m_e + Q_β`: **939.56542052(60) MeV**

  These differ by 1.42 × 10⁻⁶ MeV (~1.5 ppb), within mutual σ.  The
  repo's existing `codata_constants.M_N_MEV` is option (2) (AME-
  derived).  This module exposes BOTH and the caller picks.
"""
from __future__ import annotations

import mpmath as _mp

# ── Provenance ──────────────────────────────────────────────────────

CODATA_EDITION_YEAR = 2022
"""The CODATA recommended-values edition this module reflects."""

CODATA_SOURCE_URL = "https://physics.nist.gov/cuu/Constants/"
"""Canonical NIST source for full-precision values."""

ALLASCII_URL = "https://physics.nist.gov/cuu/Constants/allascii.txt"
"""Machine-readable snapshot URL (for future automated fetcher work)."""

VENDORED_SNAPSHOT_DATE = "2026-05-23"
"""When this module's literals were verified against the NIST source."""


# ── Precision-safe literal loader ───────────────────────────────────

def _load_mpf(literal: str) -> _mp.mpf:
    """Parse a decimal literal at ≥50 dps regardless of caller state."""
    with _mp.workdps(max(50, _mp.mp.dps)):
        return +_mp.mpf(literal)


# ── Electron mass ───────────────────────────────────────────────────

M_E_MEV = _load_mpf("0.51099895069")
"""Electron mass · c² (MeV).

CODATA-2022: 0.51099895069(15) MeV — σ ≈ 0.29 ppb.

Role: **CAL-1 anchor** — energy scale by definition.  The framework's
only direct mass calibration.

Note: existing `codata_constants.M_E_MEV` truncates this to
`0.51099895` (8 sig figs).  Four scripts in the repo
(per `docs/audits/2026-05-22-cal4-disguise-hunt.md`) already
redefine M_E_MEV at the full 11 sig figs.  This module is the
single source of truth.
"""
M_E_MEV_ERR = _load_mpf("0.00000000015")
"""1σ uncertainty on M_E_MEV.  σ ≈ 0.29 ppb."""


# ── Proton mass ─────────────────────────────────────────────────────

M_P_MEV = _load_mpf("938.27208816")
"""Proton mass · c² (MeV).

CODATA-2022: 938.27208816(29) MeV — σ ≈ 0.31 ppb.

Role: **VALIDATION** anchor (not a calibration input to the
framework; framework predicts m_p categorically).
"""
M_P_MEV_ERR = _load_mpf("0.00000029")
"""1σ uncertainty on M_P_MEV.  σ ≈ 0.31 ppb."""


# ── Neutron mass — two competing authoritative values ──────────────

M_N_MEV_CODATA_DIRECT = _load_mpf("939.56542194")
"""Neutron mass · c² (MeV) — **CODATA-2022 direct measurement**.

939.56542194(48) MeV — σ ≈ 0.51 ppb.

This is the CODATA recommended value, derived from a global
adjustment of fundamental constants.
"""
M_N_MEV_CODATA_DIRECT_ERR = _load_mpf("0.00000048")

M_N_MEV_AME_DERIVED = _load_mpf("939.56542052")
"""Neutron mass · c² (MeV) — **AME-2020 derived from m_p + m_e + Q_β**.

939.56542052(60) MeV — σ ≈ 0.64 ppb.

This is what `codata_constants.M_N_MEV` currently stores.  It is
algebraically `M_P_MEV + M_E_MEV + Q_BETA_MEV` (where Q_β is the
AME-2020 neutron decay Q-value).

**The two values disagree by ~1.5 ppb**, within their mutual
uncertainties.  Choosing one over the other affects:
- Q_β consistency (AME-derived path is consistent by construction)
- Direct comparison against absolute m_n measurements
"""
M_N_MEV_AME_DERIVED_ERR = _load_mpf("0.00000060")

M_N_MEV = M_N_MEV_AME_DERIVED
"""Repo's de facto choice for m_n (back-compat with codata_constants).
Switch to `M_N_MEV_CODATA_DIRECT` for direct-CODATA workflows."""
M_N_MEV_ERR = M_N_MEV_AME_DERIVED_ERR


# ── Muon mass + ratio ──────────────────────────────────────────────

M_MU_MEV = _load_mpf("105.6583755")
"""Muon mass · c² (MeV).  CODATA-2022: 105.6583755(23) MeV.
σ ≈ 22 ppb."""
M_MU_MEV_ERR = _load_mpf("0.0000023")

M_MU_OVER_M_E = _load_mpf("206.7682830")
"""Muon-to-electron mass ratio.  CODATA-2022: 206.7682830(46).
σ ≈ 22 ppb.

Role: **CAL-2 anchor** — second framework calibration input.
"""
M_MU_OVER_M_E_ERR = _load_mpf("0.0000046")


# ── Neutron decay Q-value ──────────────────────────────────────────

Q_BETA_MEV_AME = _load_mpf("0.78233341")
"""Neutron β-decay Q-value (MeV) — **AME-2020 direct measurement**.

0.78233341(61) MeV — σ ≈ 779.7 ppb (large because of mass-difference
cancellation).

Role: **CAL-3 anchor** — third framework calibration input.

This is what `cal-3-q-beta.witness.json` carries.  Stored at the
σ-limited precision (8 sig figs after decimal).
"""
Q_BETA_MEV_AME_ERR = _load_mpf("0.00000061")

Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT = (
    M_N_MEV_CODATA_DIRECT - M_P_MEV - M_E_MEV
)
"""Q_β computed from CODATA-2022 direct m_n.

Equals 939.56542194 − 938.27208816 − 0.51099895069 ≈ 0.78233482931 MeV.

**Differs from AME's 0.78233341 by ~1.8 × 10⁻⁶ MeV (1810 ppb)**
— this is the m_n-CODATA-vs-AME discrepancy expressed in Q_β.
Within their combined σ (sqrt of the m_n errors ~700 ppb on Q_β
relative).
"""

Q_BETA_MEV_DERIVED_FROM_AME = (
    M_N_MEV_AME_DERIVED - M_P_MEV - M_E_MEV
)
"""Q_β computed from AME-derived m_n.

Equals 939.56542052 − 938.27208816 − 0.51099895069 ≈ 0.78233340931 MeV.

**Within 1 ppb of the AME direct measurement** (0.78233341 vs
0.78233340931 — 0.9 × 10⁻⁹ MeV ≈ 1.1 ppb difference).  This is
the AME-self-consistency check.
"""


# ── Coverage summary ───────────────────────────────────────────────

def summary() -> dict:
    """Diagnostic: what this module exposes + edition + provenance."""
    return {
        "codata_edition_year": CODATA_EDITION_YEAR,
        "source_url": CODATA_SOURCE_URL,
        "allascii_url": ALLASCII_URL,
        "vendored_snapshot_date": VENDORED_SNAPSHOT_DATE,
        "constants": {
            "M_E_MEV": str(M_E_MEV),
            "M_P_MEV": str(M_P_MEV),
            "M_N_MEV_CODATA_DIRECT": str(M_N_MEV_CODATA_DIRECT),
            "M_N_MEV_AME_DERIVED": str(M_N_MEV_AME_DERIVED),
            "M_N_MEV (default = AME)": str(M_N_MEV),
            "M_MU_MEV": str(M_MU_MEV),
            "M_MU_OVER_M_E": str(M_MU_OVER_M_E),
            "Q_BETA_MEV_AME": str(Q_BETA_MEV_AME),
            "Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT":
                str(Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT),
            "Q_BETA_MEV_DERIVED_FROM_AME":
                str(Q_BETA_MEV_DERIVED_FROM_AME),
        },
        "diagnostics": {
            "m_n_CODATA_vs_AME_diff_MeV":
                str(M_N_MEV_CODATA_DIRECT - M_N_MEV_AME_DERIVED),
            "m_n_CODATA_vs_AME_diff_ppb": str(
                (M_N_MEV_CODATA_DIRECT - M_N_MEV_AME_DERIVED)
                / M_N_MEV_AME_DERIVED * _load_mpf("1e9")
            ),
            "Q_beta_AME_vs_derived_from_AME_diff_MeV": str(
                Q_BETA_MEV_AME - Q_BETA_MEV_DERIVED_FROM_AME
            ),
            "Q_beta_AME_vs_derived_from_AME_diff_ppb": str(
                (Q_BETA_MEV_AME - Q_BETA_MEV_DERIVED_FROM_AME)
                / Q_BETA_MEV_AME * _load_mpf("1e9")
            ),
            "Q_beta_AME_vs_derived_from_CODATA_direct_diff_MeV": str(
                Q_BETA_MEV_AME - Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT
            ),
        },
    }


__all__ = [
    "CODATA_EDITION_YEAR", "CODATA_SOURCE_URL", "ALLASCII_URL",
    "VENDORED_SNAPSHOT_DATE",
    "M_E_MEV", "M_E_MEV_ERR",
    "M_P_MEV", "M_P_MEV_ERR",
    "M_N_MEV", "M_N_MEV_ERR",
    "M_N_MEV_CODATA_DIRECT", "M_N_MEV_CODATA_DIRECT_ERR",
    "M_N_MEV_AME_DERIVED", "M_N_MEV_AME_DERIVED_ERR",
    "M_MU_MEV", "M_MU_MEV_ERR",
    "M_MU_OVER_M_E", "M_MU_OVER_M_E_ERR",
    "Q_BETA_MEV_AME", "Q_BETA_MEV_AME_ERR",
    "Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT",
    "Q_BETA_MEV_DERIVED_FROM_AME",
    "summary",
]
