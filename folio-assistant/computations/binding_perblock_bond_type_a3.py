#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; per-block typed bond sum.
"""DERIVATION — per-block typed inter-nucleon multiplicity sum (0 fit).

Extends the sibling's extensive bond sum
(`claude/binding-extensive-bond-sum-2026-06-02`, PR-level) from the SCALAR
|tr_M| convention to the OBSERVE-PER-BLOCK convention `Σ_λ y_λ|χ^λ|` — the
piece that sibling deferred ("needs the Rust per-partition χ kernel"). The
per-block convention is the one that closes the deuteron at +3.6 % (vs
scalar +12 %), so it is the right base for the bond sum.

## The inter-nucleon multiplicity structure

The canonical braid is a CHAIN (A−1 adjacent interfaces), but nuclear
binding is the EXTENSIVE sum over all C(A,2) nucleon pairs. Counting the
full pair multiplicity — not the chain — is what supplies the ~3× the
deuteron that the single collective trace was missing (the −60 % A=3
deficit). Typed by isospin:

    B(K) = n_pp·B_pp + n_pn·B_pn + n_nn·B_nn ,
    n_pp = C(Z,2),  n_pn = Z·N,  n_nn = C(N,2),   (Σ = C(A,2))

    B_xy = E_0·( Σ_λ y_λ|χ^λ(W_free^{xy})| − Σ_λ y_λ|χ^λ(W_atom^{xy})| )

with each bond type's 2-nucleon sub-braid at H_6 (fast): pn=(1,1)=deuteron
(derived base, +3.6 %), pp=(2,0)=diproton, nn=(0,2)=dineutron. E_0 =
m_e/(q₀(q₀−1)) ≈ 4.186 MeV (calibration-fixed, CAL-3). ZERO fit; AME used
only for the final comparison.

Expected: A=3 lands near the bond-count residual (~−15 %), with B_nn vs B_pp
setting the T-vs-³He split; ⁴He stays low (it is magic/Borromean, not
pairwise — separate structure). The residual isolates the OPEN per-bond
GROWTH (each bond embedded in the denser A-nucleon braid).
"""
from __future__ import annotations

import sys as _sys
from math import comb
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

# Bond types as 2-nucleon (Z,N) sub-braids, all at H_6.
BOND_ZN = {"pn": (1, 1), "pp": (2, 0), "nn": (0, 2)}
ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
AME = {"D": "2.2245662", "T": "8.4818", "3He": "7.7180", "4He": "28.29566"}

_ydict = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
          for k, v in y_lambda_at(6, q0).items()}


def _per_block(Z, N, inter):
    """Σ_λ y_λ|Re χ^λ| over the 2-nucleon braid at H_6."""
    cr = atomic_braid_to_crossings(Z, N, include_inter=inter)
    tot = mp.mpf(0)
    for lam in partitions_of(6):
        chi, d = chi_lambda_numerical(lam, q0, cr)
        if d == 0:
            continue
        y = _ydict.get(tuple(lam))
        if y is None:
            continue
        tot += y * abs(mp.re(chi))
    return tot


def main() -> int:
    print(f"E_0 = {float(E0):.4f} MeV   q₀ = {float(q0):.6f}\n")
    B = {}
    for xy, (Z, N) in BOND_ZN.items():
        B[xy] = E0 * (_per_block(Z, N, False) - _per_block(Z, N, True))
        print(f"  derived bond B_{xy} = {float(B[xy]):+.4f} MeV   (H_6, per-block)")
    print()
    print(f"{'iso':<5}{'(pp,pn,nn)':<13}{'B_pred':<10}{'AME':<10}{'err%':<8}")
    results = {"bonds_MeV": {k: float(v) for k, v in B.items()}}
    iso_out = {}
    for name, (Z, N) in ZN.items():
        npp, npn, nnn = comb(Z, 2), Z * N, comb(N, 2)
        Bp = npp * B["pp"] + npn * B["pn"] + nnn * B["nn"]
        A = mp.mpf(AME[name])
        err = (Bp - A) / A
        iso_out[name] = {"n_pp": npp, "n_pn": npn, "n_nn": nnn,
                         "B_pred_MeV": float(Bp), "AME_MeV": float(A),
                         "err": float(err)}
        print(f"{name:<5}({npp},{npn},{nnn}){'':<{13-len(f'({npp},{npn},{nnn})')}}"
              f"{float(Bp):<10.4f}{float(A):<10.4f}{float(err)*100:<+8.1f}")
    results["isotopes"] = iso_out
    print(f"\n  B_nn vs B_pp (T-vs-³He split): "
          f"{'B_nn>B_pp ✓' if B['nn'] > B['pp'] else 'B_nn<B_pp'}  "
          f"(AME: T 8.48 > ³He 7.72)")

    wb = WitnessBuilder("binding-perblock-bond-type-a3", engine="mpmath")
    wb.data["q_0"] = str(Q0)
    wb.data["E0_MeV"] = float(E0)
    wb.data["results"] = results
    wb.data["formula"] = "B = n_pp·B_pp + n_pn·B_pn + n_nn·B_nn (per-block, C(A,2) multiplicity)"
    wb.data["note"] = (
        "Per-block (observe-per-block) typed bond sum — extends the sibling "
        "extensive-bond-sum from scalar to per-block. Inter-nucleon "
        "multiplicity = C(A,2). Zero fit; ⁴He is magic/Borromean (separate). "
        "Residual isolates the open per-bond GROWTH.")
    wb.add_assertion("deuteron_recovers_perblock_bond",
                     computed=abs(iso_out["D"]["err"]), expected=0.0,
                     tolerance=0.05)
    wb.save()
    print("\n✓ Witness: binding-perblock-bond-type-a3.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
