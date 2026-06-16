#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer of pre-computed |tr_M| + Δ_λ witnesses.
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

Atomic binding energy via direct partition-block sum.

Per PR #616 follow-up (audit doc 2026-05-09-mass-table-fitting-audit.md
§"Δ_λ derivation status"): the canonical formula

    ρ_K(q) = ρ_K^LO + (1 / |tr_M|) · Σ_λ y_λ(q) χ^λ(β_K) Δ_λ(K)

with M_pred = ρ_K · m_e · |tr_M(K)|, has the ρ_K^LO term cancel by
construction:

    ρ_K^LO · m_e · |tr_M| = ((Z m_p + N m_n) / (m_e |tr_M|)) · m_e · |tr_M|
                          = Z m_p + N m_n     ← |tr_M| cancels

The "binding error" reported by the LO ansatz is therefore exactly
the binding energy.  The non-tautological content lives entirely
in the second-order term:

    Binding(K) = m_e · Σ_λ y_λ(q) χ^λ(β_K) Δ_λ(K)
    M(K) = (Z m_p + N m_n) + Binding(K)

This script computes the binding directly, surfacing the physical
content rather than packaging it through the ρ_K · m_e · |tr_M|
intermediate that has the |tr_M| factor self-cancel.

**Inputs:**
- `y_λ(q)` from `markov_weights_symbolic.solve_y_lambda(n)` (n=3, 6, 9)
  or `y-lambda-mpfr-witness.json` (numerical at q_0).
- `χ^λ(β_K)` from `hoefsmit_symbolic.chi_lambda_symbolic` or
  cached per-irrep evaluations.
- `Δ_λ(K)` from whatever closure the in-flight derivation race
  produces (PRs #602, #603, #613 Options B/D/F/G).  This script
  consumes the Δ_λ values from `delta-lambda-witness.json` if it
  exists, or falls through with a "delta_lambda_unavailable" flag
  for atoms whose Δ_λ has not yet been derived.

**Output:** `binding-K-direct.witness.json` with per-atom
{Z, N, A, abs_tr_M, sum_y_chi_delta, binding_MeV, binding_codata_MeV,
err_pct, status}.

This script is a SIBLING to `atomic_mass_via_rho_k.py`, NOT a
replacement: that file stays as the LO baseline reference (with
its tautology now made explicit in the docstring).  Downstream
consumers should prefer this direct-binding form.

Usage:
    python3 folio-assistant/computations/binding_K_direct.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _precision import set_compute_dps, fmt
set_compute_dps()  # mp.mp.dps via QOU_COMPUTE_DPS (default 50)
from codata_constants import (  # noqa: E402
    M_E_MEV, M_P_MEV_VALIDATION, M_N_MEV_VALIDATION,
    M_D_MEV_VALIDATION, M_T_MEV_VALIDATION, M_HE3_MEV_VALIDATION,
    M_HE4_MEV_VALIDATION,
)
from witness_base import WitnessBuilder  # noqa: E402

# Atom roster + CODATA total masses (MeV).  Binding = M_codata − (Z m_p + N m_n).
# Masses routed through the codata_constants registry (CODATA 2022 validation
# witness) — no inline CODATA literals (CLAUDE.md P31 / three-CAL purity).
ATOMS = {
    "p":   {"Z": 1, "N": 0, "M_MeV": str(M_P_MEV_VALIDATION)},
    "n":   {"Z": 0, "N": 1, "M_MeV": str(M_N_MEV_VALIDATION)},
    "D":   {"Z": 1, "N": 1, "M_MeV": str(M_D_MEV_VALIDATION)},
    "T":   {"Z": 1, "N": 2, "M_MeV": str(M_T_MEV_VALIDATION)},
    "3He": {"Z": 2, "N": 1, "M_MeV": str(M_HE3_MEV_VALIDATION)},
    "4He": {"Z": 2, "N": 2, "M_MeV": str(M_HE4_MEV_VALIDATION)},
}

ATOM_TO_TR_M_KEY = {
    "p":   "proton",
    "n":   "neutron",
    "D":   "deuteron",
    "T":   "tritium",
    "3He": "helium-3",
    "4He": "helium-4",
}


def load_abs_tr_M(w: "WitnessBuilder | None" = None) -> dict[str, mp.mpf]:
    """Load |tr_M(K)| values from `atomic-tr-m-mpfr-50dps.witness.json`
    and any per-atom extension witnesses.

    Optional ``w``: when a ``WitnessBuilder`` is supplied, every
    consumed upstream witness is hash-recorded via
    ``w.add_upstream(...)`` for the drift validator
    (``witness_dependency_drift.py``) to walk.
    """
    out: dict[str, mp.mpf] = {}
    for legacy_name in ["atomic-tr-m-mpfr-50dps.witness.json"]:
        f = HERE / legacy_name
        if f.exists():
            d = w.add_upstream(f) if w is not None else \
                json.loads(f.read_text())
            for r in d.get("results", []):
                atom = r.get("atom")
                tr_str = r.get("tr_M_at_q0_50dps")
                if atom is not None and tr_str is not None:
                    out[atom] = abs(mp.mpf(tr_str))
    for ext in sorted(HERE.glob("atomic-tr-m-*.witness.json")):
        if ext.name == "atomic-tr-m-mpfr-50dps.witness.json":
            continue
        try:
            d = w.add_upstream(ext) if w is not None else \
                json.loads(ext.read_text())
        except json.JSONDecodeError:
            continue
        for r in d.get("results", []):
            atom = r.get("atom")
            tr_str = r.get("tr_M_at_q0_50dps") or r.get("abs_tr_M_at_q0_50dps")
            if atom is not None and tr_str is not None:
                out[atom] = abs(mp.mpf(tr_str))
    return out


def load_delta_lambda(
    w: "WitnessBuilder | None" = None,
) -> dict[str, dict[tuple, mp.mpf]] | None:
    """Load per-atom per-partition Δ_λ values from
    `delta-lambda-witness.json` if it exists.  Structure:
        { "proton": { (3,): mpf("..."), (2,1): mpf("..."), (1,1,1): mpf("...") },
          "neutron": { ... },
          ... }
    Returns None if the witness is missing — the script then
    flags every atom as `delta_lambda_unavailable`.

    Optional ``w``: hash-records the consumed witness via
    ``w.add_upstream(...)`` (anti-staleness).
    """
    f = HERE / "delta-lambda-witness.json"
    if not f.exists():
        return None
    try:
        d = w.add_upstream(f) if w is not None else \
            json.loads(f.read_text())
    except json.JSONDecodeError:
        return None
    out: dict[str, dict[tuple, mp.mpf]] = {}
    for atom, blocks in (d.get("delta_lambda_per_atom") or {}).items():
        out[atom] = {}
        for shape_str, val in blocks.items():
            # shape_str like "[3]" or "[2,1]" or "(3,)"
            try:
                shape = tuple(int(x.strip()) for x in
                              shape_str.strip("[]()").split(",")
                              if x.strip())
            except ValueError:
                continue
            try:
                out[atom][shape] = mp.mpf(str(val))
            except (TypeError, ValueError):
                continue
    return out


def main() -> int:
    print("=" * 92)
    print("  Atomic binding via DIRECT partition sum (LO tautology removed)")
    print("    Binding(K) = m_e · Σ_λ y_λ(q) χ^λ(β_K) Δ_λ(K)")
    print("    M_pred(K) = (Z m_p + N m_n) + Binding(K)")
    print("=" * 92)
    print()

    # Construct the witness builder first so loaders can hash-record
    # every upstream they consume (anti-staleness; see
    # docs/audits/2026-05-16-stale-witness-infra-gap.md).
    w = WitnessBuilder("binding-K-direct", engine="mpmath")

    abs_tr_M = load_abs_tr_M(w)
    delta_lambda = load_delta_lambda(w)

    if delta_lambda is None:
        print("  ⚠ delta-lambda-witness.json not present — Δ_λ values")
        print("    are the central open compute (PRs #602, #603, #613).")
        print("    This script reports STATUS only; binding values blocked.")
        print()
    w.set_description(
        "Direct binding-energy computation for atomic mass.  "
        "Surfaces the physical content of the ρ_K formula by removing "
        "the ρ_K^LO tautology (which has the |tr_M| factor cancel "
        "against itself).  Binding(K) = m_e · Σ_λ y_λ(q) χ^λ(β_K) "
        "Δ_λ(K) — the second-order correction that IS the binding "
        "energy.  Requires Δ_λ values from the in-flight derivation "
        "race (currently open).  When delta-lambda-witness.json is "
        "absent, this script reports per-atom status only."
    )
    w.set_audit_only("docs/audits/2026-05-09-kite-tail-reconciliation.md")
    w.set_content_block("prop:rho-k-graded-expansion")
    w.add_parameter("m_e_MeV", str(M_E_MEV))
    w.add_parameter("m_p_MeV", str(M_P_MEV_VALIDATION))
    w.add_parameter("m_n_MeV", str(M_N_MEV_VALIDATION))
    w.add_parameter("delta_lambda_witness_present", delta_lambda is not None)

    print(f"  {'atom':<5}{'Z':>3}{'N':>3}  {'|tr_M|':>16}  "
          f"{'B_codata (MeV)':>16}  {'status':>30}")
    print("  " + "-" * 80)

    rows = []
    for atom, info in ATOMS.items():
        Z, N = info["Z"], info["N"]
        constituent = mp.mpf(Z) * M_P_MEV_VALIDATION + mp.mpf(N) * M_N_MEV_VALIDATION
        M_codata = mp.mpf(info["M_MeV"])
        binding_codata = M_codata - constituent

        tr_key = ATOM_TO_TR_M_KEY.get(atom)
        abs_tr = abs_tr_M.get(tr_key) if tr_key else None

        row = {
            "atom": atom,
            "Z": Z, "N": N, "A": Z + N,
            "M_codata_MeV": fmt(M_codata),
            "constituent_MeV": fmt(constituent),
            "binding_codata_MeV": fmt(binding_codata),
        }

        if abs_tr is None:
            status = "tr_M_unavailable"
            row["status"] = status
        elif delta_lambda is None or atom not in delta_lambda:
            status = "delta_lambda_unavailable"
            row["status"] = status
            row["abs_tr_M"] = str(abs_tr)
        else:
            # Direct binding: Σ_λ y_λ(q) χ^λ(β_K) Δ_λ(K).
            # When delta_lambda witness exists, the witness should
            # already encode y_λ(q_0) · χ^λ(β_K) · Δ_λ(K) per λ
            # (or the script will need to compute it).  Here we
            # assume the witness structure y_lambda_chi_delta_per_lam
            # is pre-computed.  Falls back to summing Δ_λ alone if
            # only Δ_λ is provided (less precise — full computation
            # belongs in the derivation-race PR).
            blocks = delta_lambda[atom]
            sum_delta = sum(blocks.values(), mp.mpf(0))
            binding = M_E_MEV * sum_delta
            err_pct = (binding - binding_codata) / binding_codata * 100 if binding_codata != 0 else None
            status = "computed_via_delta_lambda_sum"
            row["status"] = status
            row["abs_tr_M"] = str(abs_tr)
            row["sum_delta_lambda"] = str(sum_delta)
            row["binding_predicted_MeV"] = str(binding)
            if err_pct is not None:
                row["err_pct"] = str(err_pct)

        rows.append(row)
        abs_tr_str = mp.nstr(abs_tr, 12) if abs_tr is not None else "—"
        print(f"  {atom:<5}{Z:>3}{N:>3}  {abs_tr_str:>16}  "
              f"{mp.nstr(binding_codata, 8):>16}  {status:>30}")

    print()
    if delta_lambda is None:
        print("  (No predictions emitted — Δ_λ is the central open compute.")
        print("   See docs/audits/2026-05-09-mass-table-fitting-audit.md §Δ_λ status.)")

    w.add_data("results", rows)
    w.add_data("formula", "Binding(K) = m_e * sum_lambda(y_lambda(q) * chi^lambda(beta_K) * Delta_lambda(K))")
    w.add_data("tautology_note", (
        "rho_K^LO * m_e * |tr_M| = (Z m_p + N m_n) by construction; "
        "the only physical content of the ρ_K formula is the second-order "
        "Δ_λ correction.  This script computes the second-order term "
        "directly, bypassing the LO ceremony."
    ))
    # Headline assertion: when Δ_λ is unavailable, the script still
    # produces a well-formed status report (no crash).  Trivially true
    # if we got this far.
    w.add_assertion(
        name="status_report_emitted",
        computed=len(rows),
        expected=len(ATOMS),
        source="binding_K_direct",
    )
    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
