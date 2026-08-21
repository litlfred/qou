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
| CAL-1 | m_e                  | M_E_MEV              | electron mass (Penning trap); W-plane scale (DOF of H¹=2W) |
| CAL-2 | m_μ (→ q₀)           | (in q_parameter.py)  | muon mass (CODATA); fixes q₀ via m_μ/m_e = Vol(4_1)/ℏ_q²; W-plane modulus (DOF of H¹=2W). Phys-obs may anchor q₀ on the more-precise proton ratio m_p/m_e (live q_at, re-pin 2026-05-28) — precision substitution, not a change to canonical CAL-2 |
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
from codata_2022_source import (  # noqa: E402
    M_E_MEV,
    M_E_MEV_ERR,
    U_MEV as _U_MEV_CODATA2022,
    U_MEV_ERR as _U_MEV_CODATA2022_ERR,
)


# ── Precision-safe parser for in-module literals (bean me3r) ────
# Bare `mp.mpf("...")` at module import time parses at the caller's
# current mp.dps (often the 15-dps default), silently truncating the
# constant's binary representation. `_mpf50` forces ≥50 dps parsing
# (mirrors `_load_mpf` and `codata_2022_source._load_mpf`) so a routed
# import is bit-identical at any consumer precision ≤ 50 dps.
def _mpf50(literal: str) -> mp.mpf:
    with mp.workdps(max(50, mp.mp.dps)):
        return +mp.mpf(literal)

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
# The deuteron mass was already in the validation witness with full CODATA
# provenance; only the facade line was missing, so consumers hand-typed it
# (knot-particle-generation.py carried the CODATA-2018 1875.61294257).
# Drain qou-7ot6-a.
M_DEUTERON_MEV_VALIDATION = _load_mpf(_VALIDATION_WITNESS, "data.m_D_MeV")
M_HE3_MEV_VALIDATION = _load_mpf(_VALIDATION_WITNESS, "data.m_3He_MeV")
M_HE4_MEV_VALIDATION = _load_mpf(_VALIDATION_WITNESS, "data.m_4He_MeV")

# ── Hydrogen-1 atomic mass + Rydberg energy ─────────────────────
# Added per Copilot review on PR #757 — centralise the literals
# previously hardcoded in `probe_h1_substrate_closure`,
# `hydrogen_step_by_step`, and `hydrogen_qshuffle_compound`.
# These are pure validation/comparison targets, never CAL inputs.
# Source: CODATA 2018 / PDG 2022 atomic-mass tables.
M_H1_MEV_VALIDATION = _mpf50("938.7830731")
RYDBERG_eV_VALIDATION = _mpf50("13.605693")

# ── AME 2020 atomic binding energies (validation-only) ──────────
# Added 2026-05-24 per the canonical-iw P31 follow-up: scripts like
# `binding_canonical.py` previously hardcoded these AME values
# (2.22452, 8.481798, 7.71804, 28.295674) inline in their __main__
# print loops. The values are AME 2020 binding energies, used ONLY
# for comparison against framework predictions (`err = pred - AME_B_*`).
# Per AGENTS.md three-calibration discipline, importing these as
# upstream inputs to mass / binding compute is an opt-out from CAL
# (and is flagged by canonical-iw + production-vs-exploratory-discipline).
#
# Naming convention: `_VALIDATION` suffix marks these as
# comparison-only (mirrors `M_P_MEV_VALIDATION`, `M_H1_MEV_VALIDATION`,
# `RYDBERG_eV_VALIDATION` above). Importing without the suffix would
# be unambiguous since these are AME constants, but the suffix makes
# the validation-only role explicit at every call site.
#
# SINGLE SOURCE OF TRUTH (write-once): the binding/atomic-mass values are
# NOT copied here — they are read directly, by (Z, A), from the vendored
# AME2020 evaluation `qou-mass/src/qou_mass/data/ame2020.json` (Huang/Wang/
# Kondev/Audi/Naimi, Chinese Physics C 45 (2021) 030002). This eliminates the
# hand-maintained `ame-2020-binding-energies.witness.json` (whose manual entry
# had drifted on ⁵Li/⁷Li/⁹Be) and any divergence between the registry and the
# in-script literals — each number lives in exactly one place.
def _find_ame2020() -> Path:
    """Locate `ame2020.json` in either layout this module runs under.

    The path used to be written once, as
    `_WITNESS_DIR.parent / "qou-mass" / "src" / "qou_mass" / "data"`, which
    is a LAYERING INVERSION: `computations/` (the compute layer) reaching by
    repo-relative path into `qou-mass/` (the package layer) that vendors it.
    In-repo it resolves; vendored into the wheel, `_WITNESS_DIR` is
    `qou_mass/` and the same expression produces
    `.../qou-mass/src/qou-mass/src/qou_mass/data/ame2020.json` — the repo
    segment appearing twice — so every AME lookup died with
    FileNotFoundError. That is the last thing blocking a live
    `qou_mass.canonical_braid()`.

    Candidates are ordered in-repo first, since that is the hot path and the
    only one where a wrong answer would be silent. Nothing here changes WHICH
    file is read in the repo; it only lets the vendored copy find its own.
    """
    here = Path(__file__).resolve()
    candidates = (
        # in-repo: computations/substrate/ -> repo root -> the package's data
        _WITNESS_DIR.parent / "qou-mass" / "src" / "qou_mass" / "data" / "ame2020.json",
        # vendored: _internal/ -> qou_mass/data/
        here.parent.parent / "data" / "ame2020.json",
        # vendored, flat-package fallback
        here.parent.parent / "ame2020.json",
    )
    for cand in candidates:
        if cand.exists():
            return cand
    # Raise with every path tried. The old failure named one path that looked
    # plausible and was simply wrong, which is the slowest kind to diagnose.
    tried = "\n  ".join(str(c) for c in candidates)
    raise FileNotFoundError(
        f"ame2020.json not found in any known layout; tried:\n  {tried}"
    )


_AME2020_JSON = _find_ame2020()


def _ame2020() -> dict:
    if _AME2020_JSON not in _WITNESS_CACHE:
        with _AME2020_JSON.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        data["_index"] = {(e["Z"], e["A"]): e for e in data["entries"]}  # O(1) lookup
        _WITNESS_CACHE[_AME2020_JSON] = data
    return _WITNESS_CACHE[_AME2020_JSON]


def _ame_entry(Z: int, A: int) -> dict:
    return _ame2020()["_index"][(Z, A)]


# u→MeV conversion (bean me3r, 2026-06-30): sourced from the CODATA-2022
# module rather than scraped from the vendored AME2020 metadata note.
# The AME2020 metadata carries the CODATA-**2018** value 931.49410242;
# this registry now uses the CODATA-**2022** value 931.49410372(29) so the
# conversion matches the codata_2022_source edition (M_E/M_P/M_N etc.).
# The two differ by ~1.4 ppb (within mutual σ) and feed only the
# `*_ATOMIC_*_VALIDATION` comparison masses; AME binding energies come
# from `binding_energy_total_keV` directly and are unaffected. Verify:
#   assert "931.49410242" in _ame2020()["_metadata"]["units"]["atomic_mass_micro_u"]
_U_MEV = _U_MEV_CODATA2022

# Public alias for the atomic-mass-unit → MeV conversion (CODATA-2022).
# Consumers import this rather than re-typing the 931.494… literal
# (beans 46ke / me3r / ce18).
U_MEV = _U_MEV
U_MEV_ERR = _U_MEV_CODATA2022_ERR


def _ame_binding_mev(Z: int, A: int) -> mp.mpf:
    """Total nuclear binding energy (MeV) read from vendored AME2020.

    The whole expression (parse + division) runs inside `workdps(≥50)` so the
    arithmetic, not just the string parse, is high-precision (Gemini review)."""
    with mp.workdps(max(50, mp.mp.dps)):
        return +(mp.mpf(str(_ame_entry(Z, A)["binding_energy_total_keV"])) / 1000)


def _ame_atomic_mev(Z: int, A: int) -> mp.mpf:
    """Neutral-atom mass (MeV) read from vendored AME2020 (atomic_mass_micro_u·u).

    Whole expression in `workdps(≥50)` so the multiplications are high-precision
    (Gemini review), not just the literal parse."""
    with mp.workdps(max(50, mp.mp.dps)):
        return +(mp.mpf(str(_ame_entry(Z, A)["atomic_mass_micro_u"]))
                 * mp.mpf("1e-6") * _U_MEV)


def ame_binding_mev(Z: int, A: int) -> mp.mpf:
    """Public accessor for the vendored AME2020 total binding energy (MeV).

    The named `AME_B_*_MEV_VALIDATION` constants below cover only the seven
    light nuclides that happened to be needed when they were added.  Consumers
    working over a *table* of nuclides (mass sweeps, binding ladders) need the
    same source for arbitrary `(Z, A)`, and without a public entry point they
    hand-type the rest -- which is exactly how `mass_table_ppb.py` ended up with
    eleven typed literals sitting up to 1.6e-5 away from this table, in the same
    column as five registry-derived values.

    Same data, same precision, same `workdps` as the constants: this is an
    alias for `_ame_binding_mev`, not a second source.
    """
    return _ame_binding_mev(Z, A)


AME_B_DEUTERON_MEV_VALIDATION = _ame_binding_mev(1, 2)
AME_B_TRITIUM_MEV_VALIDATION = _ame_binding_mev(1, 3)
AME_B_HE3_MEV_VALIDATION = _ame_binding_mev(2, 3)
AME_B_HE4_MEV_VALIDATION = _ame_binding_mev(2, 4)
AME_B_LI5_MEV_VALIDATION = _ame_binding_mev(3, 5)
AME_B_LI6_MEV_VALIDATION = _ame_binding_mev(3, 6)
AME_B_LI7_MEV_VALIDATION = _ame_binding_mev(3, 7)

# ── PDG 2024 meson masses (validation-only) ───────────────────
# Added 2026-05-26 per meson knot-dictionary probe (PR #1292).
# These are comparison targets for meson-sector predictions, NOT
# calibration inputs. Source: PDG 2024 Review of Particle Physics.
M_PI_PM_MEV_VALIDATION = _mpf50("139.57039")     # ± 0.00018 MeV (1.3 ppb)
M_PI_0_MEV_VALIDATION  = _mpf50("134.9768")      # ± 0.0005 MeV (3.7 ppm)
M_K_PM_MEV_VALIDATION  = _mpf50("493.677")       # ± 0.013 MeV (26 ppm)
M_K_0_MEV_VALIDATION   = _mpf50("497.611")       # ± 0.013 MeV (26 ppm)
M_MU_MEV_VALIDATION    = _mpf50("105.6583755")   # ± 0.0000023 MeV (22 ppb)

# ── Neutral-atom atomic masses (validation-only) ──────────────
# Added 2026-06-21 (bean fvxq class-4): single canonical source for
# the atomic (neutral-atom, electrons included) masses used as
# absolute-mass comparison targets in tower_isotope_absolute.py.
# These are ATOMIC masses (≠ the nuclear M_*_MEV_VALIDATION above,
# which differ by ≈ Z·m_e); never calibration inputs. Read by (Z, A)
# from the same vendored AME2020 file (full evaluation precision —
# supersedes the prior 5–6 dp in-script literals).
M_D_ATOMIC_MEV_VALIDATION   = _ame_atomic_mev(1, 2)    # ²H  (deuterium atom)
M_T_ATOMIC_MEV_VALIDATION   = _ame_atomic_mev(1, 3)    # ³H  (tritium atom)
M_HE3_ATOMIC_MEV_VALIDATION = _ame_atomic_mev(2, 3)    # ³He atom
M_HE4_ATOMIC_MEV_VALIDATION = _ame_atomic_mev(2, 4)    # ⁴He atom
M_LI6_ATOMIC_MEV_VALIDATION = _ame_atomic_mev(3, 6)    # ⁶Li atom
M_C12_ATOMIC_MEV_VALIDATION = _ame_atomic_mev(6, 12)   # ¹²C atom

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
    # Vendored-AME accessor for nuclides with no named constant below
    "ame_binding_mev",
    # Legitimate calibration inputs (CAL-1) + derived cross-check (Q_β)
    "M_E_MEV", "M_E_MEV_ERR",
    "U_MEV", "U_MEV_ERR",  # atomic-mass-unit → MeV (CODATA-2022, from codata_2022_source)
    "Q_BETA_MEV", "Q_BETA_MEV_ERR",  # derived from CAL-1+CAL-2; kept for cross-check
    # Validation-only experimental values (loaded from witness)
    "M_P_MEV_VALIDATION", "M_P_MEV_VALIDATION_ERR",
    "M_N_MEV_VALIDATION", "M_N_MEV_VALIDATION_ERR",
    "M_D_MEV_VALIDATION",
    "M_T_MEV_VALIDATION",
    "M_HE3_MEV_VALIDATION",
    "M_HE4_MEV_VALIDATION",
]
