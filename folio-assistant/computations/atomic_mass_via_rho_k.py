#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer of pre-computed |tr_M| witness; no symbolic-q polynomial in this layer.
"""Atomic mass via the categorical density ρ_K  (P4″ from PR #564).

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

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent

mp.mp.dps = 50

# ── Inputs (calibration anchors) — imported from codata_constants ──
# Centralised per Gemini review on PR #564: avoids duplicating these
# literals across atomic_braid_mass_table.py, atomic_tr_m_mpfr_50dps.py,
# rho_k_h3a_refinement.py, sigma_shell_from_beta_chain.py, etc.
import sys as _sys
_sys.path.insert(0, str(HERE))
from codata_constants import M_E_MEV, M_P_MEV, M_N_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

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
            d = json.loads(ext.read_text())
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
    legacy file being treated as mutable."""
    out: dict[str, mp.mpf] = {}

    # Legacy 5-atom witness (p, n, D, T, ³He).
    legacy = HERE / "atomic-tr-m-mpfr-50dps.witness.json"
    if legacy.exists():
        d = json.loads(legacy.read_text())
        for r in d.get("results", []):
            atom = r.get("atom")
            tr_str = r.get("tr_M_at_q0_50dps")
            if atom is None or tr_str is None:
                continue
            out[atom] = abs(mp.mpf(tr_str))

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
            d = json.loads(ext.read_text())
        except json.JSONDecodeError:
            continue
        for r in d.get("results", []):
            atom = r.get("atom")
            tr_str = r.get("tr_M_at_q0_50dps") or r.get("abs_tr_M_at_q0_50dps")
            if atom is None or tr_str is None:
                continue
            out[atom] = abs(mp.mpf(tr_str))
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
    print(f"    m_e = {mp.nstr(M_E_MEV, 8)} MeV (CODATA)")
    print(f"    m_p = {mp.nstr(M_P_MEV, 8)} MeV (CODATA, anchor 1)")
    print(f"    m_n = {mp.nstr(M_N_MEV, 8)} MeV (CODATA, anchor 2 via Q_β)")

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
            "tr_M_at_q0": str(abs_tr),
            "rho_K_leading_order": str(rho_K),
            "M_pred_MeV": str(M_pred),
            "M_codata_MeV": str(M_codata),
            "err_pct": str(err_pct),
            "binding_residual_MeV": str(binding),
        }
        if flag:
            row["tr_M_convention_status"] = flag
        rows.append(row)

    # ── Compare to legacy E_0-anchored predictions ─────────────
    legacy_path = HERE / "atomic-braid-mass-table.witness.json"
    legacy_compare = []
    if legacy_path.exists():
        legacy = json.loads(legacy_path.read_text())
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
                    "rho_K_err_pct": str(rho_err_f),
                    "legacy_E0_err_pct": str(legacy_err_f),
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
            "Calibration anchors: m_e (CODATA), m_p (CODATA), m_n (CODATA via "
            "Q_β = m_n - m_p - m_e). Reads |tr_M(K)| from "
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
            "m_e_MeV": str(M_E_MEV),
            "m_p_MeV": str(M_P_MEV),
            "m_n_MeV": str(M_N_MEV),
            "mpmath_dps": 50,
        },
        "data": {
            "rows": rows,
            "legacy_compare": legacy_compare,
        },
        "audit_reference": "AUDIT-DEEP-2026-05.md §3.3a (P4″)",
        "pr": "#564",
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
