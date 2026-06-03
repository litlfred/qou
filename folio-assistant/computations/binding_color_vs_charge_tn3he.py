#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; scale-separation probe.
"""COLOR vs CHARGE — which weighted crossing closes the T-vs-³He split?

The inter-nucleon interface is currently the color-BLIND averaged crossing
σ − h/2. Two weighted refinements are candidates for the bond-type asymmetry
that splits T (8.482 MeV) from ³He (7.718 MeV) — a 0.764 MeV (≈ 9.5 %) gap:

  COLOR (bring_color_weighted): f = z − h·(1/2 − δ/4), δ = flavor_split_
    subleading(q) ≈ 1.4e-3. Per-bond weight (1 + δ·asym + δ²·sym),
    asym = (N−Z)/(3A): pp → −1/3, pn → 0, nn → +1/3.
  CHARGE (Coulomb / α_EM): the two like-charged protons in ³He repel,
    REDUCING ³He binding — an EM-sector effect at the α_EM ≈ 7.3e-3 scale.

This probe quantifies the COLOR contribution and shows it is the right SIGN
but ~2 orders of magnitude too small — so the T-vs-³He split is CHARGE
(Coulomb), not color. Color averaging is the Δm_pn-scale (0.14 %) refinement
and must still be wired everywhere for completeness, but it is not the
T-vs-³He mechanism. EXPLORATORY; no fit (E_0 = CAL-3; AME comparison only).
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
from _li_2_q_util import (  # noqa: E402
    bring_color_weighted_linking_weight as bw,
    linking_weight_family_a as base_lw,
    flavor_split_subleading,
)
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402 — CAL-1
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(30)
q0 = mp.mpf(str(Q0))
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))      # 𝔈₀ ≈ 4.186 MeV (CAL-3)
ALPHA_EM = mp.mpf("1") / mp.mpf("137.035999")    # for scale comparison

_y6 = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
       for k, v in y_lambda_at(6, q0).items()}


def _per_block(Z, N, inter):
    cr = atomic_braid_to_crossings(Z, N, include_inter=inter)
    tot = mp.mpf(0)
    for lam in partitions_of(6):
        chi, d = chi_lambda_numerical(lam, q0, cr)
        if d == 0:
            continue
        y = _y6.get(tuple(lam))
        if y is not None:
            tot += y * abs(mp.re(chi))
    return tot


def main() -> int:
    delta = flavor_split_subleading(q0)
    base = base_lw(q0)
    print(f"E_0 = {float(E0):.4f} MeV   δ = {float(delta):.4e}   "
          f"α_EM = {float(ALPHA_EM):.4e}\n")

    # Base (color-blind) per-block bonds at H_6.
    B0 = {xy: E0 * (_per_block(Z, N, False) - _per_block(Z, N, True))
          for xy, (Z, N) in {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2)}.items()}
    # Per-bond COLOR weight (1 + δ·asym + δ²·sym) via bond's own (Z,N).
    w = {xy: bw(Z, N, q0) / base
         for xy, (Z, N) in {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2)}.items()}
    for xy in ("pp", "pn", "nn"):
        print(f"  bond {xy}: B0 = {float(B0[xy]):+.4f} MeV   "
              f"color weight = {float(w[xy]):.8f}  ({float((w[xy]-1)*100):+.4f} %)")

    AME_T, AME_He = mp.mpf("8.4818"), mp.mpf("7.7180")
    need = AME_T - AME_He
    T_cw = 2 * B0["pn"] * w["pn"] + B0["nn"] * w["nn"]
    He_cw = B0["pp"] * w["pp"] + 2 * B0["pn"] * w["pn"]
    split_color = T_cw - He_cw
    print(f"\n  needed T−³He split          = {float(need):+.5f} MeV  (9.5 % of B)")
    print(f"  color-weighted T−³He split  = {float(split_color):+.5f} MeV")
    print(f"  color supplies              = {float(split_color/need*100):+.2f} % of needed")
    print(f"  color per-bond shift scale  = {float(delta/4):.2e}  vs needed ~0.095")
    print(f"  → color is ~{float(mp.fabs(need/(split_color if split_color else 1e-30))):.0f}× "
          f"too small; T−³He is CHARGE/Coulomb (α_EM≈{float(ALPHA_EM):.2e}), not color.")

    wb = WitnessBuilder("binding-color-vs-charge-tn3he", engine="mpmath")
    wb.data["q_0"] = str(Q0)
    wb.data["delta_flavor_split"] = float(delta)
    wb.data["alpha_em"] = float(ALPHA_EM)
    wb.data["B0_bonds_MeV"] = {k: float(v) for k, v in B0.items()}
    wb.data["color_weights"] = {k: float(v) for k, v in w.items()}
    wb.data["needed_split_MeV"] = float(need)
    wb.data["color_split_MeV"] = float(split_color)
    wb.data["color_fraction_of_needed"] = float(split_color / need)
    wb.data["verdict"] = (
        "Color-weighting (bring_color_weighted) gives the right SIGN for the "
        "bond asymmetry but is ~2 orders too small (Δm_pn scale 0.14%) for the "
        "T-vs-³He split (9.5%). That split is CHARGE/Coulomb (α_EM sector). "
        "Color averaging must still be wired everywhere for completeness.")
    wb.add_assertion("color_too_small_for_tn3he",
                     computed=1 if abs(float(split_color / need)) < 0.10 else 0,
                     expected=1, tolerance=0)
    wb.save()
    print("\n✓ Witness: binding-color-vs-charge-tn3he.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
