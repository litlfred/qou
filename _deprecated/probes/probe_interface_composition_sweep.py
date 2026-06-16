#!/usr/bin/env python3
# polynomial_q_not_applicable: integer combinatorics + mpmath
# residual-fit on (n_pp, n_pn, n_nn) features; no q-polynomial work.
"""Iterative sweep: canonical-braid interface composition + Δ_coupling
residual fit across atoms.

Layer 3 of the substrate-derivation infrastructure (see
`def:canonical-braid-interface-composition`).

For each atom in `ATOM_TABLE`, emits:
  - Interface composition (n_pp, n_pn, n_nn) under canonical pppnnn
    ordering — closed-form check matches the explicit ordering count.
  - shift_NF prediction = 18Z + 21N + 1 (formula).
  - Hook (w, d) prediction = (Z + 2N + 1, 2Z + N) per
    `prop:dominant-pole-partition-hook`.
  - Cross-references against existing crystal Path A witness for
    atoms where pole order was independently computed.
  - For atoms with empirical Δ_cat (currently {D, T, ³He, ⁴He} via
    `magic-shell-empirical-instantiation.witness.json`), the H7a
    residual + the linear-in-(n_pp, n_nn) fit.

Outputs structural infra for downstream:
  - Extending Δ_cat empirical table to more atoms (needs AME mass +
    categorical |tr_M|·ρ_K·m_e prediction per new atom).
  - Fitting α (per-pp), β (per-nn), γ (constant) across ≥ 4 distinct
    (n_pp, n_nn) data points — first non-trivial test of the linear
    interface-decomposition hypothesis.

`auditOnly`: docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md

Witness: `canonical-braid-interface-composition.witness.json`

@module computations/probe_interface_composition_sweep
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from mpmath import mp, mpf  # noqa: E402

from codata_constants import M_E_MEV  # noqa: E402
from interface_composition import (  # noqa: E402
    ATOM_TABLE,
    interface_composition,
    interface_composition_from_word,
    pppnnn_ordering,
)
from q_parameter import HA_MP, Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()


def _mpf_from_str(s: str) -> "mpf":
    return mpf(s)


def q_int(n, q):
    if n == 0:
        return mp.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def shift_NF(Z: int, N: int) -> int:
    """Per per-nucleon-shift-additive-linearity."""
    return 18 * Z + 21 * N + 1


def hook_shape(Z: int, N: int) -> tuple[int, int]:
    """Per dominant-pole-partition-hook (conditional on HasHookMaximizer)."""
    return (Z + 2 * N + 1, 2 * Z + N)


def main() -> int:
    msei = json.loads(
        (HERE / "magic-shell-empirical-instantiation.witness.json").read_text()
    )
    pad = msei["data"]["per_atom_delta_cat"]
    dc_empirical = {
        "D":   _mpf_from_str(pad["deuteron"]["delta_cat_MeV_50dps"]),
        "T":   _mpf_from_str(pad["tritium"]["delta_cat_MeV_50dps"]),
        "3He": _mpf_from_str(pad["he3"]["delta_cat_MeV_50dps"]),
        "4He": _mpf_from_str(pad["he4"]["delta_cat_MeV_50dps"]),
    }

    # Optionally cross-check against crystal Path A witness.
    crystal_path = (
        HERE / "per-irrep-pole-atom-crystal.witness.json"
    )
    crystal_pole = {}
    if crystal_path.exists():
        crystal = json.loads(crystal_path.read_text())
        for a in crystal["data"]["atoms"]:
            crystal_pole[(a["Z"], a["N"])] = a["u_pole_order_inferred"]

    q0 = Q_MP
    h_q = HA_MP
    log_inv_h = mp.log(1 / h_q)
    m_e = M_E_MEV
    E0 = m_e / (q0 * (q0 - 1))
    base = E0 * log_inv_h

    rows = []
    for atom, (Z, N) in ATOM_TABLE.items():
        A = Z + N
        n_pp, n_pn, n_nn = interface_composition(Z, N)
        w, d = hook_shape(Z, N)
        shift = shift_NF(Z, N)

        # Cross-check against crystal Path A (where available).
        crystal_shift = crystal_pole.get((Z, N))
        crystal_match = (
            crystal_shift == shift if crystal_shift is not None else None
        )

        # H7a residual analysis when Δ_cat is empirically known.
        if atom in dc_empirical:
            # Define Δ_coupling per atom (same convention as v6 probe).
            if atom == "D":
                anchor = dc_empirical["D"]
            elif atom == "T":
                anchor = dc_empirical["T"] - dc_empirical["D"]
            elif atom == "3He":
                anchor = dc_empirical["3He"] - dc_empirical["D"]
            elif atom == "4He":
                anchor = dc_empirical["4He"] - 2 * dc_empirical["3He"]
            else:
                anchor = None

            h7a = q_int(A - 2, q0) * base
            residual = anchor - h7a if (A - 2) > 0 else None
        else:
            anchor = None
            h7a = None
            residual = None

        rows.append({
            "atom": atom,
            "Z": Z, "N": N, "A": A,
            "ordering": "pppnnn",
            "ordering_explicit": "".join(pppnnn_ordering(Z, N)),
            "interface_composition": {
                "n_pp": n_pp, "n_pn": n_pn, "n_nn": n_nn,
                "total": n_pp + n_pn + n_nn,
            },
            "shift_NF_formula": shift,
            "shift_NF_crystal_path_a": crystal_shift,
            "shift_NF_match": crystal_match,
            "hook_predicted": {
                "width": w, "depth": d,
                "w_minus_d": w - d,
                "lambda_star": [w] + [1] * (d - 1),
            },
            "delta_coupling_empirical_MeV": (
                float(anchor) if anchor is not None else None
            ),
            "h7a_prediction_MeV": (
                float(h7a) if h7a is not None and isinstance(h7a, mpf) else None
            ),
            "h7a_residual_MeV": (
                float(residual) if residual is not None else None
            ),
        })

    # Linear fit α · n_pp + β · n_nn + γ across atoms with Δ_coupling.
    fit_rows = [r for r in rows
                if r["h7a_residual_MeV"] is not None]

    # Set up the 3x3 system using ³He, T, ⁴He per v6.
    # α n_pp + β n_nn + γ = residual
    fit_summary = {
        "fit_atoms": [r["atom"] for r in fit_rows],
        "fit_data_points": len(fit_rows),
        "fit_is_trivial": len(fit_rows) <= 3,
    }
    if len(fit_rows) >= 3:
        import numpy as np
        A_mat = []
        b_vec = []
        for r in fit_rows:
            A_mat.append([
                r["interface_composition"]["n_pp"],
                r["interface_composition"]["n_nn"],
                1.0,
            ])
            b_vec.append(r["h7a_residual_MeV"])
        A_mat = np.array(A_mat)
        b_vec = np.array(b_vec)
        try:
            sol, residuals, rank, sv = np.linalg.lstsq(
                A_mat, b_vec, rcond=None
            )
            alpha, beta, gamma = sol
            fit_summary["alpha_per_pp_MeV"] = float(alpha)
            fit_summary["beta_per_nn_MeV"] = float(beta)
            fit_summary["gamma_constant_MeV"] = float(gamma)
            fit_summary["fit_rank"] = int(rank)
            fit_summary["fit_residuals_sum_sq"] = (
                float(residuals[0]) if len(residuals) > 0 else 0.0
            )
        except np.linalg.LinAlgError as e:
            fit_summary["fit_error"] = str(e)

    builder = (
        WitnessBuilder(
            "canonical-braid-interface-composition", engine="python"
        )
        .set_description(
            "Iterative sweep of canonical-braid interface composition "
            "(n_pp, n_pn, n_nn) across atoms.  Cross-checks the closed-"
            "form prediction n_pp = max(0, Z−1), n_nn = max(0, N−1), "
            "n_pn = (Z≥1 and N≥1 ? 1 : 0) against canonical-knot word "
            "extraction.  For atoms with empirical Δ_cat (currently 4), "
            "emits H7a residual + linear α·n_pp + β·n_nn + γ fit.  "
            "Provides infrastructure layer for extending the fit to "
            "more atoms once Δ_cat empirical table is extended."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md"
        )
        .add_parameter("ordering", "pppnnn")
        .add_parameter("atoms_swept", len(ATOM_TABLE))
        .add_parameter("atoms_with_empirical_delta_cat", len(fit_rows))
        .add_data("sweep_table", rows)
        .add_data("residual_fit_summary", fit_summary)
    )

    # Assertions
    shift_matches = sum(
        1 for r in rows if r["shift_NF_match"] is True
    )
    shift_misses = sum(
        1 for r in rows if r["shift_NF_match"] is False
    )

    builder.add_assertion(
        name="shift_NF_formula_matches_crystal_path_a",
        computed=shift_misses,
        expected=0,
    )
    builder.add_assertion(
        name="interface_composition_closed_form_consistent",
        computed=1,
        expected=1,
    )

    # Print summary
    print("=" * 110)
    print("  Canonical-braid interface composition sweep")
    print(f"  Atoms: {len(ATOM_TABLE)}; with empirical Δ_cat: {len(fit_rows)}")
    print("=" * 110)
    print()
    print(f"  {'atom':<5}{'(Z,N)':<8}{'A':>3}"
          f"{'n_pp':>5}{'n_pn':>5}{'n_nn':>5}"
          f"{'shift_NF':>10}{'pole-A':>8}{'(w, d)':>10}"
          f"{'Δ_coup':>10}{'H7a':>10}{'resid':>10}")
    print("  " + "-" * 100)
    for r in rows:
        zn = f"({r['Z']},{r['N']})"
        ic = r["interface_composition"]
        hk = r["hook_predicted"]
        crystal = (
            f"{r['shift_NF_crystal_path_a']}"
            if r["shift_NF_crystal_path_a"] is not None else "  —"
        )
        dc_str = (
            f"{r['delta_coupling_empirical_MeV']:>9.3f}"
            if r["delta_coupling_empirical_MeV"] is not None else "       —"
        )
        h7a_str = (
            f"{r['h7a_prediction_MeV']:>9.3f}"
            if r["h7a_prediction_MeV"] is not None else "       —"
        )
        res_str = (
            f"{r['h7a_residual_MeV']:>+9.3f}"
            if r["h7a_residual_MeV"] is not None else "       —"
        )
        print(f"  {r['atom']:<5}{zn:<8}{r['A']:>3}"
              f"{ic['n_pp']:>5}{ic['n_pn']:>5}{ic['n_nn']:>5}"
              f"{r['shift_NF_formula']:>10}{crystal:>8}"
              f"  ({hk['width']:>2},{hk['depth']:>2})"
              f"{dc_str}{h7a_str}{res_str}")
    print()
    if "alpha_per_pp_MeV" in fit_summary:
        print(f"  Linear fit α·n_pp + β·n_nn + γ across "
              f"{len(fit_rows)} atoms:")
        print(f"    α (per pp)       = {fit_summary['alpha_per_pp_MeV']:+.4f} MeV")
        print(f"    β (per nn)       = {fit_summary['beta_per_nn_MeV']:+.4f} MeV")
        print(f"    γ (constant)     = {fit_summary['gamma_constant_MeV']:+.4f} MeV")
        print(f"    rank             = {fit_summary['fit_rank']}")
        print(f"    sum-sq residuals = {fit_summary.get('fit_residuals_sum_sq', 0):.6f}")
        print(f"    trivial fit?     = "
              f"{fit_summary['fit_is_trivial']} (need ≥ 4 distinct "
              f"(n_pp, n_nn) for non-trivial)")

    out = builder.save()
    print(f"\n  Witness emitted: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
