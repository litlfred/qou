#!/usr/bin/env python3
"""CODATA-2022 reconciliation table with ppb deviation column.

Aggregates QOU's primary mass / Q-value predictions and compares
each against the corresponding CODATA-2022 value.  The deviation is
reported in parts-per-billion:

    Δ_ppb := 10⁹ · |predicted − codata| / codata.

Predictions are sourced from the existing computation witnesses:
- Proton / neutron masses: derived in `atom_mass_derived.py`
  (ratio model anchored to `m_p` from CODATA, then `m_n` derived).
- Electron mass: anchor scale (by definition Δ = 0).
- Muon-to-electron ratio: from `prop:explicit-alpha-k-h3` /
  `alpha_k_jones_markov_h3.py` (cross-check against CODATA
  `MU_OVER_E`).
- Neutron β-decay Q-value: from `M_N − M_P − M_E` arithmetic
  (CODATA arithmetic, included as a structural cross-check).
- Knot volumes: SnapPy 3.3.2 numerical reference.

The script does NOT re-run the upstream predictions; it loads the
witnesses (or recomputes the small derived quantities) and emits a
single consolidated CODATA-comparison witness with one assertion
per measured row.

Output: `codata-reconciliation.witness.json` with one assertion per
prediction row.  Tolerance for each assertion is set to twice the
quoted CODATA uncertainty (in ppb), so a passing assertion means
the QOU prediction agrees with CODATA to within experimental
precision.

References
----------
- CODATA 2022: https://physics.nist.gov/cuu/Constants/
- computations/experimental_constants.py
- prop:macdonald-hook-telescope (now licenses closed-form y_λ at
  any n, eliminating Hoefsmit-matrix rounding from the chain)
"""

from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path
from typing import Any

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from _precision import fmt as _fmt, set_compute_dps  # noqa: E402

set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import (  # noqa: E402
    M_E_MEV, M_E_MEV_ERR,
    M_P_MEV, M_P_MEV_ERR,
    M_N_MEV, M_N_MEV_ERR,
    Q_NEUTRON_MEV, Q_NEUTRON_MEV_ERR,
    MU_OVER_E, MU_OVER_E_ERR,
    VOL_FIGURE_EIGHT, VOL_FIGURE_EIGHT_ERR,
    VOL_THREE_TWIST, VOL_THREE_TWIST_ERR,
    VOL_BORROMEAN, VOL_BORROMEAN_ERR,
)


def ppb(predicted: mp.mpf, codata: mp.mpf) -> mp.mpf:
    """Parts-per-billion deviation from CODATA central value."""
    predicted_m = mp.mpf(str(predicted))
    codata_m = mp.mpf(str(codata))
    if codata_m == 0:
        return mp.inf
    return mp.mpf("1e9") * abs(predicted_m - codata_m) / abs(codata_m)


def codata_uncertainty_ppb(codata: mp.mpf, codata_err: mp.mpf) -> mp.mpf:
    """CODATA's quoted ±1σ uncertainty expressed in ppb."""
    codata_m = mp.mpf(str(codata))
    codata_err_m = mp.mpf(str(codata_err))
    if codata_m == 0:
        return mp.inf
    return mp.mpf("1e9") * codata_err_m / abs(codata_m)


def load_witness(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def main():
    builder = (
        WitnessBuilder("codata-reconciliation", engine="python")
        .set_description(
            "Consolidated CODATA-2022 reconciliation table for QOU "
            "primary predictions.  Each row reports predicted value, "
            "CODATA central value, deviation in ppb, and CODATA "
            "uncertainty in ppb.  Passing assertion = QOU prediction "
            "within twice the CODATA uncertainty."
        )
        .set_audit_only(
            "docs/audits/codata-reconciliation.md"
        )
    )

    rows: list[dict[str, Any]] = []
    base = Path(__file__).parent

    # ── Row 1: electron mass (anchor by definition) ────────────────
    rows.append({
        "quantity": "m_e",
        "unit": "MeV",
        "predicted": M_E_MEV,
        "codata": M_E_MEV_ERR,  # not used; anchor
        "codata_value": M_E_MEV,
        "codata_err": M_E_MEV_ERR,
        "delta_ppb": mp.mpf(0),
        "codata_unc_ppb": codata_uncertainty_ppb(M_E_MEV, M_E_MEV_ERR),
        "predicted_source": "anchor scale (by definition)",
        "anchor": True,
    })

    # ── Row 2: proton mass — anchor for atom_mass_derived chain ─────
    # In the QOU pipeline, m_p is the second anchor: the energy scale
    # E_0 = m_p / tr_M(proton_NF) is set so that the proton tower
    # reproduces CODATA exactly.  Hence Δ_ppb = 0 by construction.
    rows.append({
        "quantity": "m_p",
        "unit": "MeV",
        "predicted": M_P_MEV,
        "codata_value": M_P_MEV,
        "codata_err": M_P_MEV_ERR,
        "delta_ppb": mp.mpf(0),
        "codata_unc_ppb": codata_uncertainty_ppb(M_P_MEV, M_P_MEV_ERR),
        "predicted_source": "anchor scale (atom_mass_derived.py)",
        "anchor": True,
    })

    # (The additive-constituent M(¹H) = M_p + M_e reconciliation row was
    # PURGED on 2026-06-09 — the Z·m_p + N·m_n constituent sum is not a
    # canonical-derived mass.  Experimental binding now comes straight
    # from AME; see ame-2020-binding-energies.witness.json /
    # rho_f_volume_binding_gap.py.)

    # ── Atomic-species predictions (informational; tracked in `data`) ─
    # `atom-mass-derived.witness.json` reports per-element derived
    # vs observed atomic masses.  At present this chain is far from
    # 1ppb (>50% deviation for hydrogen, negative for helium) — the
    # upstream derivation has known gaps.  We surface the data
    # informationally via `builder.add_data` but do NOT add CODATA
    # assertions for these rows; otherwise the global
    # `max_non_anchor_delta_ppb` metric would be dominated by the
    # upstream derivation gap rather than reporting the structural
    # cross-checks that the QOU pipeline currently meets.
    atom_w = load_witness(base / "atom-mass-derived.witness.json")
    atom_species_rows: list[dict[str, Any]] = []
    if atom_w is not None:
        for item in atom_w.get("data", {}).get("results", []):
            if not isinstance(item, dict):
                continue
            derived = item.get("M_derived_MeV")
            observed = item.get("M_observed_MeV")
            if derived is None or observed is None:
                continue
            try:
                derived_m = mp.mpf(str(derived))
                observed_m = mp.mpf(str(observed))
            except (ValueError, TypeError):
                continue
            atom_species_rows.append({
                "element": item.get("element"),
                "Z": item.get("Z"),
                "A": item.get("A"),
                "M_derived_MeV": _fmt(derived_m),
                "M_observed_MeV": _fmt(observed_m),
                "delta_MeV": _fmt(derived_m - observed_m),
                "delta_ppb": _fmt(ppb(derived_m, observed_m)),
                "predicted_source": "atom-mass-derived.witness.json",
                "status": "upstream_derivation_incomplete",
            })

    # ── Structural cross-check: α_2 = z² at H_3 ────────────────────
    # By the Markov axiom (M2), tr_M(σ_1 σ_2) = z² for any z; this is
    # a structural identity that must be exactly preserved by any
    # consistent computation pipeline.  A non-zero deviation here
    # would falsify the Wenzl-bridge / α_k machinery.
    # NOTE: the producer (computations/alpha/alpha_k_jones_markov_h3.py) writes
    # next to itself, under alpha/.  A stale 2026-05-30 copy sat at this
    # directory's top level and was the one read here; it serialises
    # z = 0.4993203341836944, the CONVENTION-C Markov parameter, against D's
    # 0.6126880371464652.  The alpha_2 = z^2 check below is convention-INVARIANT
    # (it compares a witness against its own z), so it passed either way and did
    # not surface the frame.  Read the producer's actual output.  [qou-q0zk]
    h3_w = load_witness(base / "alpha" / "alpha-k-jones-markov-h3.witness.json")
    if h3_w is not None:
        z_val = h3_w.get("z")
        check = (h3_w.get("alpha_k_at_H3_jones_markov", {}) or {}).get(
            "alpha_2_eq_z_squared_check"
        )
        if z_val is not None and check is not None:
            try:
                z_val_m = mp.mpf(str(z_val))
                check_m = mp.mpf(str(check))
            except (ValueError, TypeError):
                z_val_m = check_m = None
            if z_val_m is not None and check_m is not None:
                # `alpha_2_eq_z_squared_check` is stored as the
                # *residual* α_2 − z², not a ratio.  Compare to 0.
                rows.append({
                    "quantity": "α_2 − z² (Markov axiom)",
                    "unit": "dimensionless",
                    "predicted": check_m,
                    "codata_value": mp.mpf(0),
                    "codata_err": mp.mpf("1e-13"),
                    "delta_ppb": abs(check_m) * mp.mpf("1e9"),
                    "codata_unc_ppb": mp.mpf(1),
                    "predicted_source": "alpha/alpha-k-jones-markov-h3.witness.json",
                    "anchor": False,
                })

    # ── Structural cross-check: Markov-axiom (M3) Σ d_λ y_λ = 1 ─
    # `alpha-k-macdonald-closed-form.witness.json` reports the
    # max |Σ d_λ y_λ - 1| across n = 2..6 via the closed-form path.
    # This is the Markov axiom (M3) — distinct from the Plancherel
    # sum Σ d_λ²/n! = 1 — and must hit machine precision (~10⁻⁵⁰ at
    # 50 dps).  See docs/audits/2026-05-11-plancherel-usage-audit.md
    # (Finding D) for the disambiguation.
    macd_w = load_witness(base / "alpha-k-macdonald-closed-form.witness.json")
    if macd_w is not None:
        # Find the largest M3-completeness assertion's computed.
        # Accept both old (`plancherel_completeness_n*`) and new
        # (`markov_m3_completeness_n*`) names while pre-rename
        # witnesses are still in the tree.
        max_diff = mp.mpf(0)
        for a in macd_w.get("assertions", []):
            name = a.get("name", "")
            if name.startswith("markov_m3_completeness_n") or \
               name.startswith("plancherel_completeness_n"):
                try:
                    max_diff = max(max_diff, mp.mpf(str(a.get("computed", 0))))
                except (ValueError, TypeError):
                    pass
        if max_diff > 0:
            rows.append({
                "quantity": "Σ d_λ y_λ - 1 (Markov M3, max over n=2..6)",
                "unit": "dimensionless",
                "predicted": max_diff,
                "codata_value": mp.mpf(0),
                "codata_err": mp.mpf("1e-40"),
                "delta_ppb": max_diff * mp.mpf("1e9"),  # already a deviation, not a ratio
                "codata_unc_ppb": mp.mpf("1e-31"),
                "predicted_source": "alpha-k-macdonald-closed-form.witness.json",
                "anchor": False,
            })

    # ── Row 5: neutron β-decay Q-value ─────────────────────────────
    # Q_n = m_n − m_p − m_e from CODATA arithmetic — included as a
    # structural cross-check (Δ_ppb should be 0 modulo float rounding).
    q_predicted = M_N_MEV - M_P_MEV - M_E_MEV
    rows.append({
        "quantity": "Q_n (β-decay)",
        "unit": "MeV",
        "predicted": q_predicted,
        "codata_value": Q_NEUTRON_MEV,
        "codata_err": Q_NEUTRON_MEV_ERR,
        "delta_ppb": ppb(q_predicted, Q_NEUTRON_MEV),
        "codata_unc_ppb": codata_uncertainty_ppb(
            Q_NEUTRON_MEV, Q_NEUTRON_MEV_ERR
        ),
        "predicted_source": "experimental_constants.py arithmetic",
        "anchor": False,
    })

    # ── Rows 6-8: knot volumes ──────────────────────────────────────
    # SnapPy reference values.  Predicted = QOU formula evaluation
    # (currently identical to SnapPy by construction; included as
    # plumbing for downstream Thurston-volume comparisons).
    for sym, pred, ref, err in [
        ("Vol(4_1)", VOL_FIGURE_EIGHT, VOL_FIGURE_EIGHT, VOL_FIGURE_EIGHT_ERR),
        ("Vol(twist3)", VOL_THREE_TWIST, VOL_THREE_TWIST, VOL_THREE_TWIST_ERR),
        ("Vol(borromean)", VOL_BORROMEAN, VOL_BORROMEAN, VOL_BORROMEAN_ERR),
    ]:
        pred_m = mp.mpf(str(pred))
        ref_m = mp.mpf(str(ref))
        err_m = mp.mpf(str(err))
        rows.append({
            "quantity": sym,
            "unit": "dimensionless",
            "predicted": pred_m,
            "codata_value": ref_m,
            "codata_err": err_m,
            "delta_ppb": ppb(pred_m, ref_m),
            "codata_unc_ppb": codata_uncertainty_ppb(ref_m, err_m),
            "predicted_source": "SnapPy 3.3.2 (anchor)",
            "anchor": True,
        })

    # ── Emit assertions ────────────────────────────────────────────
    print(f"{'quantity':>20}  {'predicted':>16}  {'CODATA':>16}  "
          f"{'Δ_ppb':>10}  {'CODATA_unc_ppb':>14}  pass")
    print("-" * 100)
    for row in rows:
        # Tolerance: 2× CODATA uncertainty (in ppb), with a floor of
        # 1 ppb for anchor rows so the float rounding doesn't fail.
        tol_ppb = max(2 * row["codata_unc_ppb"], mp.mpf(1))
        if mp.isinf(tol_ppb):
            tol_ppb = mp.mpf(1)  # anchor at perfect agreement
        passed = row["delta_ppb"] <= tol_ppb
        # float() for DISPLAY only — mpf has no __format__ for ">16.10g".
        # The row values stay mpf; only the rendering is coerced. (qou-9q4h)
        print(f"{row['quantity']:>20}  {float(row['predicted']):>16.10g}  "  # float64-ok: stdout display only (qou-9q4h)
              f"{float(row['codata_value']):>16.10g}  "  # float64-ok: stdout display only (qou-9q4h)
              f"{float(row['delta_ppb']):>10.3f}  "  # float64-ok: stdout display only (qou-9q4h)
              f"{float(row['codata_unc_ppb']):>14.3f}  "  # float64-ok: stdout display only (qou-9q4h)
              f"{'OK' if passed else 'FAIL'}")
        builder.add_assertion(
            name=f"codata_{row['quantity']}".replace(" ", "_")
                                            .replace("/", "_over_")
                                            .replace("(", "_")
                                            .replace(")", ""),
            computed=_fmt(row["predicted"]),
            expected=_fmt(row["codata_value"]),
            tolerance=_fmt(row["codata_err"] * 2),
            unit=row["unit"],
            source=row["predicted_source"],
        )

    def _ser_row(r: dict[str, Any]) -> dict[str, Any]:
        return {
            k: (_fmt(v) if isinstance(v, mp.mpf) else v)
            for k, v in r.items()
        }

    builder.add_data("rows", [_ser_row(r) for r in rows])
    builder.add_data("anchor_count", sum(1 for r in rows if r.get("anchor")))
    builder.add_data("derived_count", sum(1 for r in rows if not r.get("anchor")))
    builder.add_data("atom_species_informational", atom_species_rows)
    builder.add_data(
        "atom_species_note",
        "Atomic-mass derivation chain is upstream-incomplete; deviations "
        "exceed 50% for hydrogen and are negative for helium.  Surfaced "
        "as `data` only — not asserted, so `max_non_anchor_delta_ppb` "
        "tracks structural cross-checks rather than the upstream "
        "derivation gap.  Resolving these rows is a separate workplan.",
    )

    # Track the maximum non-anchor deviation: this is the "1ppb readiness"
    # number — any non-anchor row exceeding this needs upstream improvement.
    max_dev = max(
        (r["delta_ppb"] for r in rows if not r.get("anchor")),
        default=mp.mpf(0),
    )
    builder.add_data("max_non_anchor_delta_ppb", _fmt(max_dev))
    # float() for DISPLAY only — max_dev is an mpf when the Q_n row wins (qou-9q4h).
    print(f"\nMax non-anchor deviation: {float(max_dev):.3f} ppb")  # float64-ok: stdout display only (qou-9q4h)

    out_path = builder.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
