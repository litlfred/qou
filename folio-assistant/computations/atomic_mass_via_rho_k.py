#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer of pre-computed |tr_M| witness; no symbolic-q polynomial in this layer.
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Atomic mass via the categorical density ρ_K  (P4″ from PR #564).

⚠ **LO TAUTOLOGY NOTICE.**  The leading-order ρ_K^LO ansatz used here
is mathematically tautological: by construction, the |tr_M| factor
in `M(K) = ρ_K^LO · m_e · |tr_M(K)|` cancels against the |tr_M| in
the denominator of `ρ_K^LO = (Z m_p + N m_n) / (m_e |tr_M|)`,
producing back the constituent sum `Z m_p + N m_n` exactly.  The
"residuals" reported below are not predictions — they are the
actual binding energies (the framework's null prediction).

The non-tautological content lives entirely in the second-order
correction `Σ_λ y_λ(q) χ^λ(β_K) Δ_λ(K)` to ρ_K, equivalently
`Binding(K) = m_e · Σ_λ y_λ(q) χ^λ(β_K) Δ_λ(K)`.  See
[`binding_K_direct.py`](binding_K_direct.py) for the direct-binding
formulation that surfaces the physical content without the LO
ceremony, and audit doc
[`docs/audits/2026-05-09-mass-table-fitting-audit.md`](../../docs/audits/2026-05-09-mass-table-fitting-audit.md) §"Δ_λ status".

This script is retained as the LO baseline reference.  Downstream
consumers that want non-tautological binding predictions should use
`binding_K_direct.py` once Δ_λ values are derived (PRs #602, #603,
#613 are racing the Δ_λ derivation).

Per the resolved T6 unit-convention question
(`AUDIT-DEEP-2026-05.md` §3.3a; PR #564 `e578392b8`), the right
mass formula is

    M(K) = ρ_K · m_e · |tr_M(K)|                                    (*)

where ρ_K is the categorical density.  The leading-order ansatz

    ρ_K^{LO}(Z, N) = (Z · m_p + N · m_n) / (m_e · |tr_M(K)|)         (**)

reproduces atomic masses to ≤ 0.1 % residual on D, T, ³He
(verified live in `rho-k-leading-order-verification.witness.json`).
The 0.1 % residuals = the actual binding energies; this is a
restatement of the LO tautology, not a prediction.

This script is an **additive** alternative to
`atomic_braid_mass_table.py`.  Where the legacy script anchors a
single proton-only `E_0` and propagates errors of 8–54 % to other
atoms via a broken jet-knot a_k coupling, the ρ_K path computes a
per-atom density from CODATA constituent anchors (`m_p`, `m_n`)
and the recursive Markov trace `|tr_M(K)|`.  Both anchors are CAL
inputs in the spirit of the user's directive "I do NOT want to
derive Q_β" — `m_n` enters via `Q_β = m_n − m_p − m_e`.

The script consumes pre-computed `|tr_M(K)|` values from
`atomic-tr-m-mpfr-50dps.witness.json` so it does not need a sympy
runtime.  Atoms NOT covered by the witness fall through with a
clear "tr_M_unavailable" flag rather than fabricating a value.

Output: `atomic-mass-via-rho-k.witness.json`.  Structure mirrors
the legacy `atomic-braid-mass-table.witness.json` so downstream
diff/compare tooling can read both.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent

# ── Inputs (calibration anchors) — imported from codata_constants ──
# Centralised per Gemini review on PR #564: avoids duplicating these
# literals across atomic_braid_mass_table.py, atomic_tr_m_mpfr_50dps.py,
# rho_k_h3a_refinement.py, sigma_shell_from_beta_chain.py, etc.
import sys as _sys
_sys.path.insert(0, str(HERE))
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

from codata_constants import M_E_MEV, M_P_MEV, M_N_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import load_and_hash_upstream  # noqa: E402

# ── Substrate-pure nucleon anchors (break the CAL tautology) ────
#
# Per owner: "why proton tautology? should not be."
# atomic_mass_via_rho_k previously used CODATA m_p / m_n as CAL
# anchors via Q_β = m_n - m_p - m_e, which made M_pred(p) =
# m_p_CODATA and M_pred(n) = m_n_CODATA tautological (0 % residual
# = calibration, not derivation).
#
# As of PR #690 the substrate-pure predictions are the production
# default:
#
#   m_p_substrate  ← C2 inflection at d²A/da² = 0
#                     (probe_a_selection_criteria, merged)
#   m_n_substrate  ← m_p_substrate · (1 + (q-1)²·(1-q⁻⁴)·(1+ℏ_q³)/3)
#                     (prop:flavor-split-substrate, merged in #663;
#                      sub-leading (1+ℏ_q³) correction via centralized
#                      _li_2_q_util.flavor_split_subleading helper)
#
# Backwards compatibility: set the env var
#   LEGACY_CODATA_NUCLEON_ANCHORS=1
# to fall back to the CAL tautology (preserves the 0 % residual on
# p/n for downstream calibration-check consumers).
import os as _os  # noqa: E402

from _li_2_q_util import flavor_split_subleading as _flavor_split  # noqa: E402


# Module-level accumulator for upstream-witness hash records.
# Each call to ``_load_upstream(path)`` appends one entry; the
# accumulated list is emitted under ``data.upstream_witness_hashes``
# in the script's witness output (anti-staleness; see
# docs/audits/2026-05-16-stale-witness-infra-gap.md).
_UPSTREAM_HASHES: list[dict] = []
# Per-path memo so repeated reads of the same upstream witness only
# perform one sha256 + parse — `load_atomic_tr_m_status` and
# `load_atomic_tr_m` both iterate the same extension files (gemini
# #663 review: avoid the hundreds-of-redundant-I/O regression).
_UPSTREAM_CACHE: dict[str, dict] = {}


def _load_upstream(path: Path) -> dict:
    """Read an upstream witness file, record its hash, return the body.

    Cached per-path: the second and subsequent reads of the same
    file return the memoised body and append the same hash record
    only once — see ``_UPSTREAM_CACHE``.
    """
    key = str(path.resolve())
    if key in _UPSTREAM_CACHE:
        return _UPSTREAM_CACHE[key]
    body, hr = load_and_hash_upstream(path)
    _UPSTREAM_HASHES.append(hr)
    _UPSTREAM_CACHE[key] = body
    return body


def _load_substrate_m_p_MeV() -> mp.mpf:
    """Read C2-inflection m_p from the merged probe witness; fall back
    to the published value (938.9182 MeV at q_0) if the witness is
    absent or its schema is unexpected.

    m_p_pred is in MeV; the value is absolute and does NOT require
    E_0 scaling (gemini #690 documentation note).
    """
    c2_wit = _pb.witness_path("probe-a-selection-criteria.witness.json", HERE)
    if not c2_wit.exists():
        return mp.mpf("938.9182")
    # Load + hash so witness_dependency_drift catches changes to the
    # upstream C2 witness (Copilot review on PR #757).
    c2_body = _load_upstream(c2_wit)
    c2_data = c2_body.get("data", {})
    # Pin to the explicit C2 inflection criterion (`d2A/da2=0`) rather
    # than the moving `closest_to_post_hoc` summary — the latter could
    # shift if a new criterion was added that happened to match
    # `a_post_hoc` more closely (Copilot review on PR #757).
    criteria = c2_data.get("criteria_tested", [])
    c2_entry = next(
        (c for c in criteria if c.get("criterion", "").startswith("C2 d2A/da2=0")),
        None,
    )
    if c2_entry is None:
        # Fallback to the legacy summary if no explicit C2 row exists
        # (shouldn't happen on a normally-emitted witness).
        c2_entry = c2_data.get("closest_to_post_hoc") or {}
    return mp.mpf(str(c2_entry.get("m_p_pred") or "938.9182"))


# Module-level constants — always defined regardless of mode
# (gemini #690 Rule-2 fix: no scope-dependent NameError risk).
# Tight truthy parse (gemini #690 HIGH: empty string / "0" / "false"
# should NOT trigger legacy mode; only "1" / "true" / "yes" do).
_USE_LEGACY = _os.environ.get(
    "LEGACY_CODATA_NUCLEON_ANCHORS", ""
).strip().lower() in ("1", "true", "yes", "on")
if _USE_LEGACY:
    # CODATA tautology mode (back-compat).  M_P_MEV / M_N_MEV remain
    # the codata_constants values imported above.
    _NUCLEON_ANCHOR_SOURCE = (
        "CODATA (LEGACY CAL anchors via Q_β = m_n - m_p - m_e; "
        "M_pred(p), M_pred(n) tautological)"
    )
else:
    # Substrate-pure production mode (default).
    _Q = mp.mpf(Q_50_DIGIT_STR)
    _QI = 1 / _Q
    _m_p_substrate = _load_substrate_m_p_MeV()
    # Use the centralized flavor_split_subleading helper from
    # _li_2_q_util — single source of truth (gemini #690 review).
    _m_n_substrate = _m_p_substrate * (1 + _flavor_split(_Q, _QI))
    M_P_MEV = _m_p_substrate
    M_N_MEV = _m_n_substrate
    _NUCLEON_ANCHOR_SOURCE = (
        "substrate-pure (C2 inflection + prop:flavor-split-substrate "
        "with (1+ℏ_q³) sub-leading correction; no CODATA m_p / m_n input)"
    )

# ── CODATA reference data (kept identical to legacy table) ─────
ATOMS_CODATA = {
    "p":   {"Z": 1, "N": 0, "M_MeV": "938.27208816"},
    "n":   {"Z": 0, "N": 1, "M_MeV": "939.56542052"},
    "D":   {"Z": 1, "N": 1, "M_MeV": "1875.61294257"},
    "T":   {"Z": 1, "N": 2, "M_MeV": "2808.92113298"},
    "3He": {"Z": 2, "N": 1, "M_MeV": "2808.39160743"},
    "4He": {"Z": 2, "N": 2, "M_MeV": "3727.379378"},
    # Li isotopes — nuclear masses (no electrons), AME 2020.
    # |tr_M| not yet in the canonical witness: p(15)=176, p(18)=385,
    # p(21)=792 partitions exceed the hybrid 30-dps + float64 path's
    # session budget. Rows flag tr_M_unavailable until the parallel-y_λ
    # / full-50-dps mpmath path extends.
    "5Li": {"Z": 3, "N": 2, "M_MeV": "4667.61728"},
    "6Li": {"Z": 3, "N": 3, "M_MeV": "5601.51848"},
    "7Li": {"Z": 3, "N": 4, "M_MeV": "6533.83341"},
}

# Map legacy mass-table labels → atomic-tr-m-mpfr witness labels
ATOM_LABEL_TO_TR_M_KEY = {
    "p":   "proton",
    "n":   "neutron",
    "D":   "deuteron",
    "T":   "tritium",
    "3He": "helium-3",
    "4He": "helium-4",   # not yet in the witness; will be flagged
    "5Li": "lithium-5",  # tr_M deferred (n=15)
    "6Li": "lithium-6",  # tr_M deferred (n=18)
    "7Li": "lithium-7",  # tr_M deferred (n=21)
}


def load_atomic_tr_m_status() -> dict[str, str]:
    """Return atom → convention_status for any extension witness that
    declares one (e.g. ⁴He's DEPRECATED_DISJOINT placeholder). The mass
    formula is applied uniformly across all atoms — this is purely a
    metadata channel so the result table can flag reduced-confidence
    rows. Empty dict for atoms whose source witness is canonical."""
    out: dict[str, str] = {}
    for ext in sorted(HERE.glob("atomic-tr-m-*.witness.json")):
        if ext.name == "atomic-tr-m-mpfr-50dps.witness.json":
            continue
        try:
            d = _load_upstream(ext)
        except json.JSONDecodeError:
            continue
        status = str(d.get("convention_status", ""))
        if not status:
            continue
        for r in d.get("results", []):
            atom = r.get("atom")
            if atom is not None:
                out[atom] = status
    return out


def load_atomic_tr_m() -> dict[str, mp.mpf]:
    """Load |tr_M(K)| values from the legacy 50-dps witness *and*
    any per-atom extension witnesses (e.g. `atomic-tr-m-helium4`).

    Per-atom extension files are appended after the legacy file, so
    they can override or extend the 5-atom legacy table without the
    legacy file being treated as mutable.

    **Source selection (2026-05-11 migration)**: per the
    `QOU_T1_SOURCE` env var (default `model-b`):

      - `model-b`: prefer Model B SDP-canonical low-strand braid
        values from `probe-sdp-canonical-paper-formula.witness.json`
        (D, T, ³He covered); fall back to legacy for atoms not yet
        in the Model B witness (p, n, ⁴He).
      - `model-a`: use the legacy `atomic-tr-m-mpfr-50dps.witness.json`
        + extensions (the pre-migration default).
    """
    import os as _os
    src = _os.environ.get("QOU_T1_SOURCE", "model-b")
    out: dict[str, mp.mpf] = {}

    # 1. Legacy 5-atom witness (p, n, D, T, ³He) — load first as
    #    fallback layer (gets overwritten by Model B for D, T, ³He).
    legacy = _pb.witness_path("atomic-tr-m-mpfr-50dps.witness.json", HERE)
    if legacy.exists():
        d = _load_upstream(legacy)
        for r in d.get("results", []):
            atom = r.get("atom")
            tr_str = r.get("tr_M_at_q0_50dps")
            if atom is None or tr_str is None:
                continue
            out[atom] = abs(mp.mpf(tr_str))

    # 2. Model B (SDP-canonical low-strand) overlay, if enabled.
    if src == "model-b":
        model_b_witness = _pb.witness_path("probe-sdp-canonical-paper-formula.witness.json", HERE)
        if model_b_witness.exists():
            db = _load_upstream(model_b_witness)
            for atom_name, atom_data in db.get("data", {}).get("results", {}).items():
                tr_str = atom_data.get("tr_M_wenzl_schur")
                if tr_str is None:
                    continue
                out[atom_name] = abs(mp.mpf(str(tr_str)))

    # Per-atom extension witnesses: any file matching
    # `atomic-tr-m-*.witness.json` whose name is NOT the legacy one.
    #
    # The mass formula M(K) = ρ_K · m_e · |tr_M(K)| is applied
    # uniformly across all atoms — including atoms whose extension
    # witness carries `convention_status: DEPRECATED_*` (e.g. ⁴He's
    # disjoint-product placeholder pending the Rust-kernel canonical
    # H_12 compute). Single formula, no special case.
    #
    # The convention metadata is exposed separately via
    # `load_atomic_tr_m_status()` so the result table can flag
    # reduced-confidence rows; downstream consumers must check the
    # status if they care about provenance.
    for ext in sorted(HERE.glob("atomic-tr-m-*.witness.json")):
        if ext.name == "atomic-tr-m-mpfr-50dps.witness.json":
            continue
        try:
            d = _load_upstream(ext)
        except json.JSONDecodeError:
            continue
        for r in d.get("results", []):
            atom = r.get("atom")
            tr_str = r.get("tr_M_at_q0_50dps") or r.get("abs_tr_M_at_q0_50dps")
            if atom is None or tr_str is None:
                continue
            out[atom] = abs(mp.mpf(tr_str))

    # 4. Wenzl LR overlay — DISABLED 2026-05-17 after
    #    `cross_check_trM_wenzl_lr_1ppb.py` revealed ~80 % relative
    #    divergence vs Hoefsmit / markov_peel for D, T, ³He.
    #
    #    Root cause: the LR identity
    #      χ^λ(β_1 ⊗ β_2) = Σ_{μν} c^λ_{μν} · χ^μ(β_1) · χ^ν(β_2)
    #    applies to *tensor-product* (disjoint) braids only. The
    #    canonical atomic braid `atom_canonical_crossings(Z, N)` is
    #    NOT a tensor product — it includes inter-nucleon arc
    #    crossings (the "averaged" ctype). The LR consumer was
    #    computing |tr_M(β_p ⊗ β_n)| (disjoint product), not
    #    |tr_M(β_D)| (canonical deuteron with inter-nucleon arcs).
    #
    #    Re-enable only after the consumer is extended to handle
    #    non-tensor inter-nucleon braiding (the categorical Wenzl
    #    bridge per `hecke-branching-trace-decomposition.md`).
    #    Tracker: docs/audits/2026-05-17-1ppb-workplan-v4.md
    #    §"Wenzl LR consumer bug".
    return out


def rho_K_leading_order(Z: int, N: int, abs_tr_M: mp.mpf) -> mp.mpf:
    """ρ_K^{LO}(Z, N) = (Z·m_p + N·m_n) / (m_e·|tr_M(K)|)."""
    return (Z * M_P_MEV + N * M_N_MEV) / (M_E_MEV * abs_tr_M)


def predict_mass(Z: int, N: int, abs_tr_M: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """Return (M_pred, ρ_K^{LO})."""
    rho = rho_K_leading_order(Z, N, abs_tr_M)
    return rho * M_E_MEV * abs_tr_M, rho


def main() -> int:
    print("=" * 96)
    print("  Atomic mass via categorical density ρ_K  (P4″  / PR #564)")
    print("    M(K) = ρ_K · m_e · |tr_M(K)|")
    print("    ρ_K^LO = (Z·m_p + N·m_n) / (m_e · |tr_M(K)|)")
    print("=" * 96)

    tr_M_table = load_atomic_tr_m()
    tr_M_status = load_atomic_tr_m_status()
    if not tr_M_table:
        print("ERROR: atomic-tr-m-mpfr-50dps.witness.json missing or empty.")
        return 1
    print(f"\n  Loaded |tr_M| for {len(tr_M_table)} atoms: "
          f"{', '.join(sorted(tr_M_table))}")
    if tr_M_status:
        print(f"  convention flags (informational; formula applied uniformly):")
        for atom, st in sorted(tr_M_status.items()):
            print(f"    {atom}: {st[:80]}{'...' if len(st) > 80 else ''}")

    print(f"\n  Calibration anchors:")
    print(f"    m_e = {mp.nstr(M_E_MEV, 8)} MeV (CODATA, CAL-1 always)")
    print(f"    nucleon anchor source: {_NUCLEON_ANCHOR_SOURCE}")
    print(f"    m_p = {mp.nstr(M_P_MEV, 8)} MeV")
    print(f"    m_n = {mp.nstr(M_N_MEV, 8)} MeV")

    print(f"\n  {'atom':<5}{'Z':>2}{'N':>2}  "
          f"{'|tr_M|':>14}  {'ρ_K^LO':>14}  "
          f"{'M_pred (MeV)':>14}  {'M_codata (MeV)':>16}  "
          f"{'err %':>10}")
    print("  " + "-" * 92)

    rows = []
    for atom, info in ATOMS_CODATA.items():
        Z, N = info["Z"], info["N"]
        tr_key = ATOM_LABEL_TO_TR_M_KEY.get(atom)
        if tr_key is None or tr_key not in tr_M_table:
            print(f"  {atom:<5}{Z:>2}{N:>2}  "
                  f"{'(|tr_M| unavailable in witness — skipped)':>62}")
            rows.append({
                "atom": atom, "Z": Z, "N": N, "A": Z + N,
                "tr_M_unavailable": True,
                "M_codata_MeV": info["M_MeV"],
            })
            continue
        abs_tr = tr_M_table[tr_key]
        M_codata = mp.mpf(info["M_MeV"])
        M_pred, rho_K = predict_mass(Z, N, abs_tr)
        err_pct = (M_pred - M_codata) / M_codata * 100
        binding = abs(M_pred - M_codata)
        flag = tr_M_status.get(tr_key, "")
        flag_marker = " ⚠" if flag.startswith("DEPRECATED") else ""

        print(f"  {atom:<5}{Z:>2}{N:>2}  "
              f"{mp.nstr(abs_tr, 9):>14}  "
              f"{mp.nstr(rho_K, 9):>14}  "
              f"{mp.nstr(M_pred, 10):>14}  "
              f"{mp.nstr(M_codata, 10):>16}  "
              f"{mp.nstr(err_pct, 4):>9}%{flag_marker}")

        row = {
            "atom": atom, "Z": Z, "N": N, "A": Z + N,
            "tr_M_at_q0": fmt(abs_tr),
            "rho_K_leading_order": fmt(rho_K),
            "M_pred_MeV": fmt(M_pred),
            "M_codata_MeV": fmt(M_codata),
            "err_pct": fmt(err_pct),
            "binding_residual_MeV": fmt(binding),
        }
        if flag:
            row["tr_M_convention_status"] = flag
        rows.append(row)

    # Fix #5 (S2) — record shadow-price upstream so the LP-dual a_K
    # machinery shows in this script's dependency chain (sweep audit
    # docs/audits/2026-05-18-compute-integration-sweep.md).
    _shadow_price_path = HERE / "a-K-via-lp-dual-hecke-basis.witness.json"
    if _shadow_price_path.exists():
        _load_upstream(_shadow_price_path)

    # ── Compare to legacy E_0-anchored predictions ─────────────
    legacy_path = _pb.witness_path("atomic-braid-mass-table.witness.json", HERE)
    legacy_compare = []
    if legacy_path.exists():
        legacy = _load_upstream(legacy_path)
        # Legacy witness has either `data.rows` or `rows` at top level.
        legacy_rows = legacy.get("data", {}).get("rows") or legacy.get("rows") or []
        legacy_by_atom = {r.get("atom"): r for r in legacy_rows if r.get("atom")}
        print(f"\n  Side-by-side vs legacy E_0-anchored mass-table:")
        print(f"  {'atom':<5}  {'ρ_K err %':>10}  {'legacy err %':>14}  improvement")
        print("  " + "-" * 60)
        for r in rows:
            if r.get("tr_M_unavailable"):
                continue
            atom = r["atom"]
            if atom not in legacy_by_atom:
                continue
            legacy_err = legacy_by_atom[atom].get("err_pct")
            if legacy_err is None:
                continue
            try:
                legacy_err_f = float(legacy_err)
                rho_err_f = float(r["err_pct"])
                improvement = abs(legacy_err_f) / max(abs(rho_err_f), 1e-12)
                print(f"  {atom:<5}  {rho_err_f:>9.4f}%  {legacy_err_f:>13.4f}%  "
                      f"×{improvement:>9.1f}")
                legacy_compare.append({
                    "atom": atom,
                    "rho_K_err_pct": fmt(rho_err_f),
                    "legacy_E0_err_pct": fmt(legacy_err_f),
                    "improvement_factor": improvement,
                })
            except (TypeError, ValueError):
                continue

    # ── Witness output (via WitnessBuilder.wrap_legacy) ───────
    witness = {
        "computation": "atomic-mass-via-rho-k",
        "auditOnly": "AUDIT-DEEP-2026-05.md",
        "description": (
            "Atomic mass-table predictions using the resolved ρ_K assembly "
            "M(K) = ρ_K · m_e · |tr_M(K)| from PR #564 §3.3a "
            "(Options A + C: no additive T6, Mittag-Leffler complementarity). "
            f"Calibration anchors: m_e (CODATA, CAL-1); nucleon "
            f"anchors = {_NUCLEON_ANCHOR_SOURCE}. Reads |tr_M(K)| from "
            "atomic-tr-m-mpfr-50dps.witness.json. Atoms not in that witness "
            "are flagged tr_M_unavailable rather than fabricating values. "
            "Direct successor to atomic_braid_mass_table.py — see the "
            "side-by-side improvement_factor field."
        ),
        "engine": "mpmath",
        "scriptFile": "atomic_mass_via_rho_k.py",
        "scriptHash": None,  # will be filled by WitnessBuilder if/when wired
        "parameters": {
            "q0": Q_50_DIGIT_STR,
            "m_e_MeV": fmt(M_E_MEV),
            "m_p_MeV": fmt(M_P_MEV),
            "m_n_MeV": fmt(M_N_MEV),
            "mpmath_dps": 50,
        },
        "data": {
            "rows": rows,
            "legacy_compare": legacy_compare,
            # Anti-staleness: hashes of every upstream witness this
            # script consumed (drift validator walks this field).
            "upstream_witness_hashes": _UPSTREAM_HASHES,
        },
        "audit_reference": "AUDIT-DEEP-2026-05.md §3.3a (P4″)",
        "pr": "#564",
        # Fix #5 (sweep audit 2026-05-18) — declare the shadow-price
        # producer block in the dependency chain.
        "reference_blocks": [
            "prop:mass-coefficient-shadow-price",
        ],
    }
    from witness_base import WitnessBuilder
    out_path = (
        WitnessBuilder.wrap_legacy(
            "atomic-mass-via-rho-k",
            witness,
            script_path=__file__,
            engine="mpmath",
            output_dir=HERE,
        )
        .save()
    )
    print(f"\n  Wrote {out_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
