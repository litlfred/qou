#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; derived-Coulomb probe.
"""DERIVED Coulomb contribution to the T-vs-³He split — no fit.

The ³H−³He binding split (0.764 MeV ≈ 9.5%) is the Coulomb repulsion of
³He's two protons. The color-weighted crossing is ~22× too small for it
(docs/audits/2026-06-03-color-vs-charge-crossing-tn3he.md); the split is
CHARGE/EM. This probe applies the **already-derived** categorical Coulomb
structure — `def:coulomb-charge` (`coulomb-charge.lean`):

    E_cross = (1/2)(n₊+n₋)(q+q⁻¹) [strong] + Q·(q−q⁻¹) [Coulomb],
    Q_pp = (n₊−n₋)/2 = +1 for two protons (repulsive),
    Coulomb/strong ratio = tanh(ln q₀)   (q₀-only, derived).

So the derived pp-Coulomb reduction of ³He binding is
`tanh(ln q₀)·B_pp` — ZERO fit (Q from def:coulomb-charge, ratio from q₀,
B_pp the per-block pp strong bond). AME is used only for the final
comparison.

VERDICT (this probe): the derived Coulomb covers ~31% of the split (vs
color's 4.5%) — right sign, right order, 3.2× short. The remaining 3.2×
is the OPEN per-interface EM-linking / nuclear-geometry normalization (the
categorical two-like-charge brane-pairing invariant is not yet defined; a
concrete close beyond this would be a CAL-4 fit to 0.76 MeV). EXPLORATORY.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
for _d in ("hecke", "habiro", "substrate"):
    _p = str(_Path(__file__).resolve().parent / _d)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from habiro_coefficients_interpolate import (  # noqa: E402
    chi_lambda_numerical, atomic_braid_to_crossings,
)
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from schur_weyl_symbolic import partitions_of  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402 — CAL-1
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(30)
q0 = mp.mpf(str(Q0))
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))      # 𝔈₀ ≈ 4.186 MeV (CAL-3)


def _per_block(Z, N, inter):
    """Σ_λ y_λ|Re χ^λ| over the 2-nucleon braid at H_6."""
    ydict = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
             for k, v in y_lambda_at(6, q0).items()}
    cr = atomic_braid_to_crossings(Z, N, include_inter=inter)
    tot = mp.mpf(0)
    for lam in partitions_of(6):
        chi, d = chi_lambda_numerical(lam, q0, cr)
        if d == 0:
            continue
        y = ydict.get(tuple(lam))
        if y is not None:
            tot += y * abs(mp.re(chi))
    return tot


def main() -> int:
    # pp strong bond (per-block, H_6 diproton); Q_pp = +1 (def:coulomb-charge)
    B_pp = E0 * (_per_block(2, 0, False) - _per_block(2, 0, True))
    ratio = mp.tanh(mp.log(q0))                  # derived Coulomb/strong ratio
    dHe = ratio * B_pp                           # ³He pp-Coulomb reduction
    need = mp.mpf("0.7638")                       # AME ³H−³He split

    print(f"E_0 = {float(E0):.4f} MeV   q₀ = {float(q0):.6f}")
    print(f"derived Coulomb/strong ratio tanh(ln q₀) = {float(ratio):.5f}")
    print(f"pp strong bond B_pp = {float(B_pp):.4f} MeV   (Q_pp = +1)")
    print(f"derived pp-Coulomb ³He reduction = {float(dHe):.4f} MeV")
    print(f"AME T−³He split = {float(need):.4f} MeV")
    print(f"derived covers {float(dHe/need*100):.1f}% (vs color 4.5%); "
          f"remaining {float(need/dHe):.2f}× = open EM-linking normalization")

    wb = WitnessBuilder("charge-coulomb-tn3he-derived", engine="mpmath")
    wb.data["q_0"] = str(Q0)
    wb.data["coulomb_strong_ratio_tanh_ln_q0"] = float(ratio)
    wb.data["B_pp_strong_MeV"] = float(B_pp)
    wb.data["Q_pp"] = 1
    wb.data["derived_coulomb_dHe_MeV"] = float(dHe)
    wb.data["ame_split_MeV"] = float(need)
    wb.data["fraction_of_split_covered"] = float(dHe / need)
    wb.data["remaining_factor"] = float(need / dHe)
    wb.data["verdict"] = (
        "Derived categorical Coulomb (def:coulomb-charge, tanh(ln q₀), Q_pp=+1, "
        "no fit) covers ~31% of the T-³He split (vs color 4.5%) — right sign + "
        "order, 3.2× short. Remaining 3.2× = OPEN per-interface EM-linking / "
        "nuclear-geometry normalization (would be CAL-4 if fitted).")
    wb.add_assertion("derived_coulomb_right_order",
                     computed=1 if 0.1 < float(dHe / need) < 1.0 else 0,
                     expected=1, tolerance=0)
    wb.save()
    print("\n✓ Witness: charge-coulomb-tn3he-derived.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
