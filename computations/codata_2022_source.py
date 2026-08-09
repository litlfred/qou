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

Per AGENTS.md §"Precision goals" and `codata_constants.py`'s
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

⚠ **MISLABELLED VINTAGE — this is the CODATA-2018 value, not 2022.**
Corrected label 2026-08-09 (PR #4860, bean `qou-2an8`). The *value* is
unchanged, deliberately: see "why the value is not changed here" below.

**Proof it is not 2022** — this module's `M_E_MEV` and the pin anchor
`qou_substrate.constants.MASS_RATIO_P_E` are both genuine 2022, and the
three are algebraically over-determined::

    M_E_MEV * MASS_RATIO_P_E  =  938.27208942732424736394 MeV
    M_P_MEV                   =  938.27208816            MeV
    residual                  =  +1.3507 ppb  =  127x the last printed digit

Within a single CODATA adjustment these are one correlated least-squares
output (the MeV-valued m_p is derived downstream of m_e and the ratio), so a
same-edition triple agrees to its last printed digit. 127x is not rounding.

An independent observable confirms *which* member is stale: `m_p + m_e + Q_β`
must reproduce `M_N_MEV_CODATA_DIRECT` (genuine 2022). The ratio-derived
proton lands at 0.32σ of it; this stored value misses by 2.96σ.

**Why the value is not changed here.** The true CODATA-2022 digits could not
be verified — physics.nist.gov is egress-blocked in the authoring sandbox —
and writing a *derived* number into a file whose stated purpose is to be a
"vendored snapshot of NIST values" would reintroduce exactly the provenance
defect this note documents. Use `M_P_MEV_RATIO_CONSISTENT` below when you
need an internally consistent proton; swap this literal only against a
verified NIST 2022 quote (bean `qou-if87`).

Role: **VALIDATION** anchor (not a calibration input to the
framework; framework predicts m_p categorically).
"""
M_P_MEV_ERR = _load_mpf("0.00000029")
"""1σ uncertainty on M_P_MEV.  σ ≈ 0.31 ppb."""

def _mass_ratio_p_e():
    """The m_p/m_e pin anchor, SOURCED — never re-typed here.

    Deliberately imported rather than copied: a local literal would make this
    module a fourth registry for the same quantity, which is the defect class
    this file now documents. ``qou_substrate.constants`` imports only ``math``,
    so there is no cycle. The ``MASS_RATIO_P_E_STR`` decimal string is
    preferred over the f64 ``MASS_RATIO_P_E`` so no precision is lost.

    Returns ``None`` rather than raising if ``qou_substrate`` is unavailable.
    This module is imported by ~234 consumers that never touch the triple; an
    ImportError here would break every one of them to serve a diagnostic.
    """
    import sys as _s
    from pathlib import Path as _P
    try:
        _pkg = _P(__file__).resolve().parent.parent / "tools" / "qou-substrate" / "python"
        if _pkg.is_dir() and str(_pkg) not in _s.path:
            _s.path.insert(0, str(_pkg))
        from qou_substrate.constants import MASS_RATIO_P_E_STR
        return _load_mpf(MASS_RATIO_P_E_STR)
    except Exception:  # noqa: BLE001 — diagnostic only; never break importers
        return None


MASS_RATIO_P_E = _mass_ratio_p_e()
"""m_p/m_e — re-exported from ``qou_substrate.constants`` (the pin anchor).

Present so the triple this module documents can be checked without the caller
having to reach into two packages. It is a re-export, **not** a second copy.
"""

M_P_MEV_RATIO_CONSISTENT = (
    M_E_MEV * MASS_RATIO_P_E if MASS_RATIO_P_E is not None else None
)
"""Proton mass · c² (MeV) — **DERIVED, not vendored.**

`M_E_MEV × (m_p/m_e)`, i.e. the proton implied by this module's 2022
electron mass and the 2022 pin anchor `MASS_RATIO_P_E`. Use this wherever a
proton consistent with the rest of the 2022 registry is required.

Not a NIST quote: it is a product of two NIST quotes, so it may differ from
the published CODATA-2022 m_p by up to one unit in the 11th significant
figure (~0.01 ppb) from NIST's own rounding — 30x below the σ below, and
135x below the 1.35 ppb inconsistency it exists to avoid.
"""
M_P_MEV_RATIO_CONSISTENT_ERR = _load_mpf("0.00000028")
"""1σ on M_P_MEV_RATIO_CONSISTENT, from σ(m_e)/m_e = 0.29 ppb and
σ(ratio)/ratio = 0.06 ppb in quadrature ⇒ ≈ 0.30 ppb."""


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

⚠ **The ~1.5 ppb disagreement is now explained** (2026-08-09, PR #4860):
this AME-derived value is built on `M_P_MEV`, which is a mislabelled
CODATA-2018 proton (see its docstring). Rebuilt on
`M_P_MEV_RATIO_CONSISTENT` the AME path lands within **0.32σ** of
`M_N_MEV_CODATA_DIRECT` instead of 2.96σ — i.e. the two "competing
authoritative values" largely stop competing. Consequence for consumers:
**this value is NOT an independent neutron measurement** — it is
`M_P_MEV + M_E_MEV + Q_BETA_MEV_AME` by construction, so scoring a
prediction against it double-counts whatever is already in the proton and
Q_β. Prefer `M_N_MEV_CODATA_DIRECT` for accuracy scoring.
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


# ── Atomic mass unit → MeV conversion ──────────────────────────────

U_MEV = _load_mpf("931.49410372")
"""Atomic mass constant energy equivalent m_u·c² (MeV).

CODATA-2022: **931.49410372(29) MeV** — σ ≈ 0.31 ppb.

Role: **VALIDATION** conversion (u → MeV) for AME atomic-mass tables.

⚠ **Edition note (2026-06-30).** This is the CODATA-**2022** value. The
prior registry value `931.49410242` (scraped from the vendored AME2020
metadata note) is the CODATA-**2018** edition; the two differ by
`1.30 × 10⁻⁶ MeV` (~1.4 ppb), within mutual σ. `codata_constants.U_MEV`
now sources from here so the conversion matches this module's edition.
Used only to convert AME `atomic_mass_micro_u` → MeV for validation
comparison; binding energies come from AME `binding_energy_total_keV`
directly and are unaffected.
"""
U_MEV_ERR = _load_mpf("0.00000029")
"""1σ uncertainty on U_MEV.  σ ≈ 0.31 ppb."""


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
            "U_MEV": str(U_MEV),
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


def triple_consistency_ppb():
    """Residual of the over-determined (m_e, m_p/m_e, m_p) triple, in ppb.

    Any two of the three fix the third, so a same-edition triple returns ~0
    (bounded by the printed granularity of ``M_P_MEV``, ~0.011 ppb). A large
    return value means the registries have drifted apart in vintage.

    Returns a positive number when ``M_P_MEV`` is SMALLER than the proton
    implied by ``M_E_MEV × MASS_RATIO_P_E``. Currently ≈ +1.3507 ppb — the
    known 2018/2022 straddle documented on ``M_P_MEV``.
    """
    if M_P_MEV_RATIO_CONSISTENT is None:
        raise RuntimeError(
            "cannot check the registry triple: qou_substrate is not importable, "
            "so the m_p/m_e pin anchor could not be sourced. Install/point at "
            "tools/qou-substrate/python."
        )
    return (M_P_MEV_RATIO_CONSISTENT - M_P_MEV) / M_P_MEV * _load_mpf("1e9")


#: Residual accepted by :func:`assert_triple_consistent` while the known
#: 2018/2022 straddle on ``M_P_MEV`` remains unfixed (bean ``qou-if87``).
#: Tighten to ~0.05 once that literal is corrected against a verified quote.
KNOWN_TRIPLE_RESIDUAL_PPB = 1.4


def assert_triple_consistent(tolerance_ppb=None):
    """Raise if the registry triple has drifted beyond the accepted residual.

    A regression guard for the defect class found in PR #4860: a registry
    that is exactly representable, correctly typed and precise to 11 figures,
    yet from the wrong CODATA edition — invisible to every float64 / precision
    audit in the repo, because nothing here is imprecise.

    Deliberately asserts against a *known-residual ceiling* rather than zero:
    asserting zero today would simply fail, and a guard that is expected to
    fail teaches readers to ignore it.
    """
    tol = _load_mpf(str(KNOWN_TRIPLE_RESIDUAL_PPB if tolerance_ppb is None
                        else tolerance_ppb))
    resid = triple_consistency_ppb()
    if abs(resid) > tol:
        raise AssertionError(
            f"CODATA registry triple inconsistent by {resid} ppb "
            f"(ceiling {tol} ppb). Either a registry drifted vintage, or "
            f"M_P_MEV was corrected and this ceiling should be tightened. "
            f"See M_P_MEV's docstring and bean qou-if87."
        )
    return resid


__all__ = [
    "CODATA_EDITION_YEAR", "CODATA_SOURCE_URL", "ALLASCII_URL",
    "VENDORED_SNAPSHOT_DATE",
    "M_E_MEV", "M_E_MEV_ERR",
    "M_P_MEV", "M_P_MEV_ERR",
    "M_P_MEV_RATIO_CONSISTENT", "M_P_MEV_RATIO_CONSISTENT_ERR",
    "MASS_RATIO_P_E",
    "triple_consistency_ppb", "assert_triple_consistent",
    "KNOWN_TRIPLE_RESIDUAL_PPB",
    "M_N_MEV", "M_N_MEV_ERR",
    "M_N_MEV_CODATA_DIRECT", "M_N_MEV_CODATA_DIRECT_ERR",
    "M_N_MEV_AME_DERIVED", "M_N_MEV_AME_DERIVED_ERR",
    "M_MU_MEV", "M_MU_MEV_ERR",
    "M_MU_OVER_M_E", "M_MU_OVER_M_E_ERR",
    "U_MEV", "U_MEV_ERR",
    "Q_BETA_MEV_AME", "Q_BETA_MEV_AME_ERR",
    "Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT",
    "Q_BETA_MEV_DERIVED_FROM_AME",
    "summary",
]
