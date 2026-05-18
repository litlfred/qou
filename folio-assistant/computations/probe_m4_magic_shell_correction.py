"""M4 mass table — add interface-type-resolved magic-shell correction.

Continues the Path-2 (mass-table closure) work after M3 demonstrated
the categorical Q_β chain closes to ppb but the mass residuals
remain at ~0.19% MAE (structural T1-T4 terms, not Q_β precision).

This probe tests whether adding the **interface-type-resolved
magic-shell coupling** correction (from PR #656's v6 probe,
`probe_interface_type_resolved_coupling.py`) closes the per-atom
residuals.

## Correction model

Per `prop:magic-shell-coupling-kappa` (audit doc on this
branch), the magic-shell coupling has structure:

  Δ_coupling(Z, N) ≈ [A−2]_q · E_0 · log(1/h) + (n_pp − n_nn) · κ · h · E_0

where:
  - n_pp = max(0, Z-1)   inter-nucleon pp interfaces
  - n_nn = max(0, N-1)   inter-nucleon nn interfaces
  - κ ≈ -1.07 MeV/excess (empirical slope from #656 v6 probe)

The expectation: ADD Δ_coupling to the binding energy, which
SUBTRACTS from M_pred. The Z↔N asymmetry term flips sign between
isospin mirrors (T vs ³He), exactly what's needed to fix the
+5 MeV / −7 MeV pattern in the M3 mass table.

## Caveats

- κ is empirical from the v6 probe (not yet categorically derived).
  Once the substrate-derivation for the asymmetry slope is wired
  (open work per #656), this becomes a categorical correction.
- The H7a piece [A−2]_q · E_0 · log(1/h) was refuted as a UNIVERSAL
  closure by PR #654's F2 probe — but it survives at the doubly-
  magic anchor. The interface-type-resolved formula is the
  candidate that addresses the Z↔N asymmetry.

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from paper_six_term_isotope_sweep import (  # noqa: E402
    assemble_per_derivation_weights,
)
from q_parameter import Q_MP, HA_MP  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION,
    M_D_MEV_VALIDATION, M_T_MEV_VALIDATION,
    M_HE3_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
)


M_CODATA_MEV = {
    "p":   float(M_P_MEV_VALIDATION),
    "n":   float(M_N_MEV_VALIDATION),
    "D":   float(M_D_MEV_VALIDATION),
    "T":   float(M_T_MEV_VALIDATION),
    "3He": float(M_HE3_MEV_VALIDATION),
    "4He": float(M_HE4_MEV_VALIDATION),
}


def q_bracket(n: int, q: mp.mpf) -> mp.mpf:
    """q-bracket [n]_q = (q^n - q^-n) / (q - q^-1)."""
    if n == 0:
        return mp.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def magic_shell_correction(Z: int, N: int,
                             kappa_per_excess: mp.mpf) -> mp.mpf:
    """Interface-type-resolved Δ_coupling(Z, N) in MeV.

    Two-component model:
      H7a:           [A−2]_q · E_0 · log(1/h)  (universal piece)
      Z↔N asym:      (n_pp − n_nn) · κ        (interface-resolved)

    κ is treated as an empirical scalar (units MeV) for now;
    in #656's v6 probe κ ≈ -1.07 MeV per unit excess.
    """
    q = Q_MP
    h = HA_MP
    m_e = mp.mpf(M_E_MEV)
    E0 = m_e / (q * (q - 1))
    log_inv_h = mp.log(1 / h)

    A = Z + N
    n_pp = max(0, Z - 1)
    n_nn = max(0, N - 1)
    iface_excess = n_pp - n_nn

    if A < 2:
        return mp.mpf(0)  # single nucleon — no inter-nucleon coupling

    h7a_piece = q_bracket(A - 2, q) * E0 * log_inv_h
    asymmetry_piece = mp.mpf(iface_excess) * kappa_per_excess

    return h7a_piece + asymmetry_piece


def main() -> int:
    mp.mp.dps = 50

    # κ ≈ -1.07 MeV/excess from PR #656 v6 probe.  Treated as empirical
    # input; substrate derivation is open work per the audit doc.
    KAPPA_EMP = mp.mpf("-1.0707907503265857")

    atoms = [
        ("p",   1, 0),
        ("n",   0, 1),
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
        ("4He", 2, 2),
    ]

    print("=" * 100)
    print("  M4 mass table — full N=4 chain Q_β + interface-type magic-shell correction")
    print("=" * 100)
    print()
    print(f"  κ (empirical from #656 v6) = {float(KAPPA_EMP):+.6f} MeV/excess")
    print()
    print(f"  {'iso':>5} {'Z':>2} {'N':>2} {'M_codata':>11} {'M_pred (n4)':>14} {'err ppm':>10} "
          f"{'Δ_coup MeV':>11} {'M_pred (M4)':>14} {'err ppm':>10}")
    print('  ' + '-' * 110)

    rows = []
    total_err_ppm_n4 = mp.mpf(0)
    total_err_ppm_m4 = mp.mpf(0)
    n_atoms = 0

    for label, Z, N in atoms:
        try:
            r = assemble_per_derivation_weights(Z, N, q_beta_source="full_chain_n4")
        except Exception as exc:
            print(f"  {label:>5}: FAILED ({type(exc).__name__}: {exc})")
            continue
        M_codata = M_CODATA_MEV[label]
        M_pred_n4 = float(r["M_predicted_MeV"])
        delta_coup = magic_shell_correction(Z, N, KAPPA_EMP)
        # Add Δ_coupling to binding → subtract from M_pred
        M_pred_m4 = M_pred_n4 - float(delta_coup)

        err_n4_ppm = (M_pred_n4 - M_codata) / M_codata * 1e6
        err_m4_ppm = (M_pred_m4 - M_codata) / M_codata * 1e6

        total_err_ppm_n4 += abs(mp.mpf(repr(err_n4_ppm)))
        total_err_ppm_m4 += abs(mp.mpf(repr(err_m4_ppm)))
        n_atoms += 1

        rows.append({
            "atom": label, "Z": Z, "N": N, "A": Z + N,
            "M_codata_MeV": M_codata,
            "M_pred_n4_MeV": M_pred_n4,
            "err_n4_ppm": err_n4_ppm,
            "delta_coupling_MeV": float(delta_coup),
            "M_pred_m4_MeV": M_pred_m4,
            "err_m4_ppm": err_m4_ppm,
            "improvement_factor": (
                float(abs(mp.mpf(repr(err_n4_ppm))) / abs(mp.mpf(repr(err_m4_ppm))))
                if abs(err_m4_ppm) > 1e-6 else None
            ),
        })

        print(
            f"  {label:>5} {Z:>2} {N:>2} {M_codata:>11.6f} {M_pred_n4:>14.6f} "
            f"{err_n4_ppm:>+9.1f} {float(delta_coup):>+10.4f} "
            f"{M_pred_m4:>14.6f} {err_m4_ppm:>+9.1f}"
        )

    mae_n4 = float(total_err_ppm_n4 / n_atoms)
    mae_m4 = float(total_err_ppm_m4 / n_atoms)
    improvement = mae_n4 / mae_m4 if mae_m4 > 0 else None

    print()
    print(f"  MAE N=4 (Q_β chain only):  {mae_n4:>10.1f} ppm  ({mae_n4 / 1e4:.4f}%)")
    print(f"  MAE M4 (+ magic-shell):    {mae_m4:>10.1f} ppm  ({mae_m4 / 1e4:.4f}%)")
    if improvement:
        print(f"  Improvement factor:        {improvement:>10.2f}×")

    builder = (
        WitnessBuilder("m4-magic-shell-correction-mass-table", engine="mpmath")
        .set_description(
            "M4 mass table: full N=4 categorical Q_β chain + "
            "interface-type-resolved magic-shell coupling correction "
            "(from PR #656 v6 probe). Tests whether adding the "
            "Δ_coupling(Z,N) = [A−2]_q·E_0·log(1/h) + (n_pp-n_nn)·κ "
            "correction closes the structural T/³He Z↔N asymmetry "
            "that the Q_β chain alone cannot reach (per M3 finding)."
        )
        .set_content_block("prop:magic-shell-coupling-kappa")
        .add_parameter("kappa_per_excess_MeV", float(KAPPA_EMP))
        .add_parameter("kappa_source", "empirical_from_pr656_v6")
        .add_data("rows", rows)
        .add_data("mae_n4_ppm", mae_n4)
        .add_data("mae_m4_ppm", mae_m4)
        .add_data("improvement_factor", improvement)
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
