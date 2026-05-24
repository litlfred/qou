"""M5 mass table — adds CATEGORICAL Coulomb correction E_C = Q·h·E_0.

The Coulomb correction is NOT an additional empirical term — it's
already derived categorically per [`def:coulomb-charge`](
content/quantum-observable-universe/braids-and-knots/coulomb-charge.md):

    E_cross(𝔥) = ½(n₊ + n₋)·(q + q⁻¹)  +  Q(𝔥)·(q − q⁻¹)
                  └── strong, symmetric ──┘    └── Coulomb, antisymmetric ──┘

where Q(𝔥) = ½(n₊ − n₋) is the writhe (signed crossing imbalance).

The ratio Coulomb/strong is `tanh(ln q_0) ≈ 0.0946` at q_0 — the
substrate antisymmetric component of crossing energy.

This probe extracts Q from each atom's canonical braid word and
computes the categorical Coulomb correction in MeV (scaled by
E_0 = m_e / (q(q-1)) — the substrate energy unit per #654 M1 doc).

## Why this is the right place to look

The M4 probe added an EMPIRICAL "interface-type" correction
(n_pp − n_nn) · κ from PR #656's v6 fit, which:
- Closed T residual (3p+2n type) — sign correct
- Broke ³He (2p+1n) — sign wrong

³He's Coulomb is repulsive (2 protons), reducing binding. The
categorical Q·h captures this directly without an empirical fit:
³He has Q = +4 (per the braid-word inspection), giving
E_C(³He) ≈ Q·h·E_0 ≈ 3.5 MeV.

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
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q_MP, HA_MP  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION,
    M_D_MEV_VALIDATION, M_T_MEV_VALIDATION,
    M_HE3_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
)


M_CODATA_MEV = {
    "p": float(M_P_MEV_VALIDATION),    "n": float(M_N_MEV_VALIDATION),
    "D": float(M_D_MEV_VALIDATION),    "T": float(M_T_MEV_VALIDATION),
    "3He": float(M_HE3_MEV_VALIDATION), "4He": float(M_HE4_MEV_VALIDATION),
}


def writhe_Q(Z: int, N: int) -> tuple[int, int, mp.mpf]:
    """Return (n_pos, n_neg, Q = ½(n_+ − n_-)) from the canonical braid word.

    Per `def:coulomb-charge`, the Coulomb charge of a knot composite
    is half the signed crossing imbalance. For QOU atom braid words
    (mass_at_3A_proper.atom_braid_word_3A), each crossing tuple
    (c, d, gen) represents `c · σ_gen + d · I`; pure crossings have:
      σ_i  : (1, 0)   → positive  → +1 to n₊
      σ_i⁻¹: (1, -h)  → negative  → +1 to n₋
    """
    word = atom_braid_word_3A(Z, N, include_inter=True)
    h_val = float(HA_MP)
    n_pos = sum(1 for c, d, _ in word
                if abs(d) < 1e-12 and abs(c - 1) < 1e-12)
    n_neg = sum(1 for c, d, _ in word
                if abs(d + h_val) < 1e-3 and abs(c - 1) < 1e-12)
    Q = mp.mpf("0.5") * (n_pos - n_neg)
    return n_pos, n_neg, Q


def main() -> int:
    mp.mp.dps = 50

    q = Q_MP
    h = HA_MP
    m_e = mp.mpf(M_E_MEV)
    E0 = m_e / (q * (q - 1))     # substrate energy unit (per M1 §3)
    coulomb_per_strong = h / (q + 1 / q)  # tanh(ln q_0) ≈ 0.0946

    atoms = [("p",1,0), ("n",0,1), ("D",1,1), ("T",1,2), ("3He",2,1), ("4He",2,2)]

    print("=" * 110)
    print("  M5 mass table — categorical Coulomb correction E_C = Q · h · E_0")
    print("=" * 110)
    print()
    print(f"  q_0 = {mp.nstr(q, 12)}")
    print(f"  h   = q - q⁻¹ = {mp.nstr(h, 12)}")
    print(f"  E_0 = m_e / (q(q-1)) = {mp.nstr(E0, 12)} MeV/Hecke-unit")
    print(f"  Coulomb/strong ratio = h/(q+q⁻¹) = tanh(ln q_0) = {mp.nstr(coulomb_per_strong, 8)}")
    print()
    print(f"  {'iso':>5} {'M_codata':>11} {'M_pred(n4)':>13} {'err ppm':>9} "
          f"{'n₊':>4} {'n₋':>4} {'Q':>5} {'E_C MeV':>9} "
          f"{'M_pred(M5)':>13} {'err M5 ppm':>11}")
    print('  ' + '-' * 110)

    rows = []
    mae_n4 = mp.mpf(0)
    mae_m5 = mp.mpf(0)
    for label, Z, N in atoms:
        try:
            r = assemble_per_derivation_weights(Z, N, q_beta_source="full_chain_n4")
        except Exception:
            continue
        M_codata = M_CODATA_MEV[label]
        M_pred_n4 = float(r["M_predicted_MeV"])
        n_pos, n_neg, Q = writhe_Q(Z, N)
        E_C = Q * h * E0  # categorical Coulomb contribution

        # Coulomb contribution to crossing energy is POSITIVE (additional
        # rest-mass energy from net positive writhe). So ADD E_C to M_pred.
        # (Equivalently: Coulomb REDUCES binding for positive Q.)
        M_pred_m5 = M_pred_n4 + float(E_C)

        err_n4 = (M_pred_n4 - M_codata) / M_codata * 1e6
        err_m5 = (M_pred_m5 - M_codata) / M_codata * 1e6

        mae_n4 += abs(mp.mpf(repr(err_n4)))
        mae_m5 += abs(mp.mpf(repr(err_m5)))

        rows.append({
            "atom": label, "Z": Z, "N": N, "A": Z + N,
            "M_codata_MeV": M_codata,
            "M_pred_n4_MeV": M_pred_n4,
            "err_n4_ppm": err_n4,
            "n_pos": n_pos, "n_neg": n_neg,
            "Q_writhe": float(Q),
            "E_Coulomb_MeV": float(E_C),
            "M_pred_m5_MeV": M_pred_m5,
            "err_m5_ppm": err_m5,
        })
        print(f"  {label:>5} {M_codata:>11.6f} {M_pred_n4:>13.6f} {err_n4:>+8.1f} "
              f"{n_pos:>4} {n_neg:>4} {float(Q):>+5.1f} {float(E_C):>+8.4f} "
              f"{M_pred_m5:>13.6f} {err_m5:>+10.1f}")

    mae_n4 = float(mae_n4 / len(rows))
    mae_m5 = float(mae_m5 / len(rows))
    print()
    print(f"  MAE (N=4 chain only): {mae_n4:.1f} ppm  ({mae_n4/1e4:.4f}%)")
    print(f"  MAE (+ E_C wired):    {mae_m5:.1f} ppm  ({mae_m5/1e4:.4f}%)")
    print(f"  Improvement factor:   {mae_n4/mae_m5 if mae_m5 > 0 else 0:.2f}×")

    builder = (
        WitnessBuilder("m5-categorical-coulomb-mass-table", engine="mpmath")
        .set_description(
            "M5 mass table: full N=4 categorical Q_β chain + "
            "categorical Coulomb correction E_C = Q·h·E_0 from "
            "def:coulomb-charge. The Coulomb piece is the "
            "antisymmetric component of crossing energy (writhe-"
            "weighted, ratio tanh(ln q_0) ≈ 0.0946 of the strong "
            "baseline). NO empirical fit — this is the categorical "
            "correction the M4 probe was missing for proton-rich "
            "atoms like ³He."
        )
        .set_content_block("def:coulomb-charge")
        .add_parameter("E0_MeV", float(E0))
        .add_parameter("h_value", float(h))
        .add_parameter("coulomb_to_strong_ratio", float(coulomb_per_strong))
        .add_data("rows", rows)
        .add_data("mae_n4_ppm", mae_n4)
        .add_data("mae_m5_ppm", mae_m5)
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
