#!/usr/bin/env python3


# polynomial_q_not_applicable: constants module; no q-polynomial logic.
"""CODATA / AME constants module — split into legitimate calibration
inputs and validation-only literals, and loaded from witness JSONs
rather than hardcoded.

═══════════════════════════════════════════════════════════════════
 CALIBRATION DISCIPLINE  (per content/quantum-observable-universe/
 particle-interactions/meson-scale-independence.md)
═══════════════════════════════════════════════════════════════════

The QOU framework admits **exactly three** external calibration
inputs — each associated with a physical measurement (mass or
decay width). Beyond these three, no further empirical, fitting,
or numerological input is permitted; every other mass, Q-value,
and binding energy in the paper is a prediction.

| ID    | Observable            | Module export        | Measurement / Source                      |
|-------|----------------------|----------------------|------------------------------------------|
| CAL-1 | m_e                  | M_E_MEV              | electron mass (Penning trap); H⁰ W-plane scale |
| CAL-2 | m_μ/m_e (→ q₀)       | (in q_parameter.py)  | muon–electron mass ratio (CODATA); H¹ W-plane modulus. Phys-obs may anchor q₀ on the more-precise proton ratio m_p/m_e (live q_at, re-pin 2026-05-28) — precision substitution, not a change to canonical CAL-2 |
| CAL-3 | m_π                  | M_PI_PM_MEV_VALIDATION | charged-pion mass (PDG); orthogonal Vol(Hopf)=0 meson class. Q_β (neutron β-decay 𝔇_β) is DERIVED from CAL-1+CAL-2, not a calibration |

`m_p`, `m_n`, `m_D`, `m_T`, `m_3He`, `m_4He` are **predictions** of
the framework. They are exposed below for **validation only** —
import them when comparing categorical predictions against AME /
CODATA experimental values, NEVER as upstream inputs to a mass
prediction. They live in
`codata-2022-validation-masses.witness.json`.

Scripts that consume `M_P_MEV` / `M_N_MEV` / etc. as inputs to a
mass / binding-energy prediction violate the three-calibration
discipline and inflate the apparent calibration count from 3 → 4+.
The neutron-gap probes (round 3, witness
`neutron-gap-probes-round3.witness.json`) explicitly diagnosed this
violation and recommend the correct chain:

    m_p_pred = |tr_M(p, q_0)| · E_0
    m_n_pred = m_p_pred + Q_β_derived + m_e (Q_β derived from CAL-1+CAL-2)
    m_K_pred = (Z·m_p + N·m_n)_pred + Binding(K)

The script-side migration to the categorical chain is tracked as
Workplan 0b in
`docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md`.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 6, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import warnings
from pathlib import Path

import mpmath as mp

# ── Witness JSON loader ─────────────────────────────────────────
_WITNESS_DIR = Path(__file__).resolve().parent.parent  # was: .parent (pre-Phase-6 — substrate moved into substrate/, added .parent to reach root)
_VALIDATION_WITNESS = _WITNESS_DIR / "codata-2022-validation-masses.witness.json"
_CAL3_WITNESS = _WITNESS_DIR / "cal-3-q-beta.witness.json"

# Cache for parsed JSON content keyed by witness Path so repeated
# _load_mpf calls on the same file don't re-parse.
_WITNESS_CACHE: dict = {}


def _load_mpf(witness_path: Path, dotted_key: str) -> mp.mpf:
    """Load an mpmath mpf from a witness JSON at a dotted key path.

    Witness values are stored as strings to preserve precision through
    JSON round-trip; mp.mpf parses them at the active dps. Per-path
    JSON parses are cached in `_WITNESS_CACHE` to avoid redundant I/O
    when this module loads multiple values from the same witness.
    """
    if witness_path not in _WITNESS_CACHE:
        with witness_path.open("r", encoding="utf-8") as fh:
            _WITNESS_CACHE[witness_path] = json.load(fh)
    cursor = _WITNESS_CACHE[witness_path]
    for segment in dotted_key.split("."):
        cursor = cursor[segment]
    if not isinstance(cursor, str):
        raise TypeError(
            f"Witness {witness_path.name}:{dotted_key} must be string for "
            f"precision-safe mpmath parsing; got {type(cursor).__name__}."
        )
    # Force ≥50 dps parsing regardless of caller's current mp.dps so
    # the module-level constants don't silently truncate to a low-
    # precision default at import time. Caller's dps is restored on
    # exit (per Copilot review note).
    with mp.workdps(max(50, mp.mp.dps)):
        return +mp.mpf(cursor)  # unary `+` to force re-rounding at workdps


# ── CAL-1: electron mass (legitimate calibration input) ─────────
# Source of truth: codata_2022_source.M_E_MEV (full 11-sig-fig
# CODATA-2022 value 0.51099895069(15) MeV).  Prior hardcoded
# literal was 0.51099895 (8 sig figs, truncated by 3).  Per the
# 2026-05-23 precision-pipeline audit (docs/audits/2026-05-23-
# codata-precision-audit.md), 4+ scripts were already redefining
# M_E_MEV at the full precision — this import unifies them.
from codata_2022_source import M_E_MEV, M_E_MEV_ERR  # noqa: E402

# ── Q_β: DERIVED from CAL-1 + CAL-2 (cross-check, NOT independent) ─
# Q_β = m_e·|q₀²−2q₀−1|·(q₀+1)/(2q₀³) ≈ 0.784 MeV (0.17% miss).
# Historically listed as CAL-3 but is redundant with CAL-2.
# Retained as a validation cross-check. CAL-3 is now m_π (see above).
Q_BETA_MEV = _load_mpf(_CAL3_WITNESS, "data.Q_beta_n_MeV")
Q_BETA_MEV_ERR = _load_mpf(_CAL3_WITNESS, "data.Q_beta_n_MeV_err")

# ════════════════════════════════════════════════════════════════
# VALIDATION-ONLY CODATA literals — DO NOT USE AS PREDICTION INPUTS
# ════════════════════════════════════════════════════════════════
# Loaded from codata-2022-validation-masses.witness.json. These are
# the experimental values the framework predicts. Importing them as
# upstream inputs to any mass / binding script silently inflates the
# calibration count beyond the pre-approved 3 (CAL-1/2/3). Use only
# for downstream comparison: `err = pred - M_X_VALIDATION`.

M_P_MEV_VALIDATION = _load_mpf(_VALIDATION_WITNESS, "data.m_p_MeV")
M_P_MEV_VALIDATION_ERR = _load_mpf(_VALIDATION_WITNESS, "data.m_p_MeV_err")

M_N_MEV_VALIDATION = _load_mpf(_VALIDATION_WITNESS, "data.m_n_MeV")
M_N_MEV_VALIDATION_ERR = _load_mpf(_VALIDATION_WITNESS, "data.m_n_MeV_err")

M_D_MEV_VALIDATION = _load_mpf(_VALIDATION_WITNESS, "data.m_D_MeV")
M_T_MEV_VALIDATION = _load_mpf(_VALIDATION_WITNESS, "data.m_T_MeV")
M_HE3_MEV_VALIDATION = _load_mpf(_VALIDATION_WITNESS, "data.m_3He_MeV")
M_HE4_MEV_VALIDATION = _load_mpf(_VALIDATION_WITNESS, "data.m_4He_MeV")

# ── Hydrogen-1 atomic mass + Rydberg energy ─────────────────────
# Added per Copilot review on PR #757 — centralise the literals
# previously hardcoded in `probe_h1_substrate_closure`,
# `hydrogen_step_by_step`, and `hydrogen_qshuffle_compound`.
# These are pure validation/comparison targets, never CAL inputs.
# Source: CODATA 2018 / PDG 2022 atomic-mass tables.
M_H1_MEV_VALIDATION = mp.mpf("938.7830731")
RYDBERG_eV_VALIDATION = mp.mpf("13.605693")

# ── AME 2020 atomic binding energies (validation-only) ──────────
# Added 2026-05-24 per the canonical-iw P31 follow-up: scripts like
# `binding_canonical.py` previously hardcoded these AME values
# (2.22452, 8.481798, 7.71804, 28.295674) inline in their __main__
# print loops. The values are AME 2020 binding energies, used ONLY
# for comparison against framework predictions (`err = pred - AME_B_*`).
# Per CLAUDE.md three-calibration discipline, importing these as
# upstream inputs to mass / binding compute is an opt-out from CAL
# (and is flagged by canonical-iw + production-vs-exploratory-discipline).
#
# Naming convention: `_VALIDATION` suffix marks these as
# comparison-only (mirrors `M_P_MEV_VALIDATION`, `M_H1_MEV_VALIDATION`,
# `RYDBERG_eV_VALIDATION` above). Importing without the suffix would
# be unambiguous since these are AME constants, but the suffix makes
# the validation-only role explicit at every call site.
#
# Source witness:
# `ame-2020-binding-energies.witness.json` (committed alongside).
# Original data: Wang, M. et al., "The AME 2020 atomic mass
# evaluation", Chinese Physics C 45.3 (2021) 030003.
_AME_BINDING_WITNESS = _WITNESS_DIR / "ame-2020-binding-energies.witness.json"

AME_B_DEUTERON_MEV_VALIDATION = _load_mpf(_AME_BINDING_WITNESS, "data.B_deuteron_MeV")
AME_B_TRITIUM_MEV_VALIDATION = _load_mpf(_AME_BINDING_WITNESS, "data.B_tritium_MeV")
AME_B_HE3_MEV_VALIDATION = _load_mpf(_AME_BINDING_WITNESS, "data.B_he3_MeV")
AME_B_HE4_MEV_VALIDATION = _load_mpf(_AME_BINDING_WITNESS, "data.B_he4_MeV")
AME_B_LI5_MEV_VALIDATION = _load_mpf(_AME_BINDING_WITNESS, "data.B_li5_MeV")
AME_B_LI6_MEV_VALIDATION = _load_mpf(_AME_BINDING_WITNESS, "data.B_li6_MeV")
AME_B_LI7_MEV_VALIDATION = _load_mpf(_AME_BINDING_WITNESS, "data.B_li7_MeV")

# ── PDG 2024 meson masses (validation-only) ───────────────────
# Added 2026-05-26 per meson knot-dictionary probe (PR #1292).
# These are comparison targets for meson-sector predictions, NOT
# calibration inputs. Source: PDG 2024 Review of Particle Physics.
M_PI_PM_MEV_VALIDATION = mp.mpf("139.57039")     # ± 0.00018 MeV (1.3 ppb)
M_PI_0_MEV_VALIDATION  = mp.mpf("134.9768")      # ± 0.0005 MeV (3.7 ppm)
M_K_PM_MEV_VALIDATION  = mp.mpf("493.677")       # ± 0.013 MeV (26 ppm)
M_K_0_MEV_VALIDATION   = mp.mpf("497.611")       # ± 0.013 MeV (26 ppm)
M_MU_MEV_VALIDATION    = mp.mpf("105.6583755")   # ± 0.0000023 MeV (22 ppb)

# ── Internal consistency check (Q_β derived vs CODATA m_n − m_p − m_e) ─
# Q_β is derived from CAL-1 + CAL-2; this check verifies it agrees
# with (m_n − m_p − m_e) within combined CODATA σ.
_q_beta_from_codata_check = (
    M_N_MEV_VALIDATION - M_P_MEV_VALIDATION - M_E_MEV
)
_q_beta_residual = abs(Q_BETA_MEV - _q_beta_from_codata_check)
_q_beta_combined_err = mp.sqrt(
    M_N_MEV_VALIDATION_ERR ** 2
    + M_P_MEV_VALIDATION_ERR ** 2
    + M_E_MEV_ERR ** 2
    + Q_BETA_MEV_ERR ** 2
)
if _q_beta_residual > 5 * _q_beta_combined_err:
    warnings.warn(
        f"Q_β consistency check failed: |Q_β - (m_n - m_p - m_e)| = "
        f"{float(_q_beta_residual):.3e} MeV exceeds 5× combined CODATA σ "
        f"({float(_q_beta_combined_err):.3e} MeV). Verify CODATA refresh "
        f"in codata-2022-validation-masses.witness.json + "
        f"cal-3-q-beta.witness.json.",
        stacklevel=2,
    )

# ════════════════════════════════════════════════════════════════
# DEPRECATED ALIASES — emit DeprecationWarning on import
# ════════════════════════════════════════════════════════════════
# The pre-2026-05-10 names `M_P_MEV`, `M_N_MEV`, `M_D_MEV`, … were
# imported by ~30 scripts as if they were calibration inputs. They
# remain accessible for one release cycle to avoid breaking imports,
# but each access emits a DeprecationWarning naming the migration
# target. New code MUST import the `_VALIDATION` suffix and only for
# comparison purposes (never as prediction inputs).

_DEPRECATED_ALIASES = {
    "M_P_MEV": "M_P_MEV_VALIDATION",
    "M_N_MEV": "M_N_MEV_VALIDATION",
    "M_D_MEV": "M_D_MEV_VALIDATION",
    "M_T_MEV": "M_T_MEV_VALIDATION",
    "M_HE3_MEV": "M_HE3_MEV_VALIDATION",
    "M_HE4_MEV": "M_HE4_MEV_VALIDATION",
    "M_P_MEV_ERR": "M_P_MEV_VALIDATION_ERR",
    "M_N_MEV_ERR": "M_N_MEV_VALIDATION_ERR",
}


def __getattr__(name: str):
    if name in _DEPRECATED_ALIASES:
        target = _DEPRECATED_ALIASES[name]
        warnings.warn(
            f"`{name}` is deprecated and violates the three-calibration "
            f"discipline (CAL-1/2/3 only). Import `{target}` instead, and "
            f"use it ONLY for validation/comparison — never as an upstream "
            f"input to a mass / binding prediction. See "
            f"three-calibration-inputs.md and "
            f"docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md.",
            DeprecationWarning,
            stacklevel=2,
        )
        return globals()[target]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    # Legitimate calibration inputs (CAL-1) + derived cross-check (Q_β)
    "M_E_MEV", "M_E_MEV_ERR",
    "Q_BETA_MEV", "Q_BETA_MEV_ERR",  # derived from CAL-1+CAL-2; kept for cross-check
    # Validation-only experimental values (loaded from witness)
    "M_P_MEV_VALIDATION", "M_P_MEV_VALIDATION_ERR",
    "M_N_MEV_VALIDATION", "M_N_MEV_VALIDATION_ERR",
    "M_D_MEV_VALIDATION",
    "M_T_MEV_VALIDATION",
    "M_HE3_MEV_VALIDATION",
    "M_HE4_MEV_VALIDATION",
]
