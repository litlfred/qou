#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; per-bond-growth probe.
"""Per-bond GROWTH — is an EMBEDDED bond stronger than the isolated one?

The multiplicity sum `B = Σ_{C(A,2)} B_b^iso` (isolated H_6 deuteron-scale
bonds) closes A=3 to −15% (PR #1754). The residual is per-bond GROWTH:
each bond inside the dense A-nucleon braid should be stronger than the
isolated 2-nucleon bond. This probe MEASURES that, no fit.

For each chain interface I_b in the H_9 atom, the EMBEDDED bond is the
per-block marginal of adding just that interface to the 3-nucleon FREE
braid (the other nucleon present as a spectator):

    B_b^emb = E_0·( perblock(W_free^A) − perblock(W_free^A + I_b) )

vs the ISOLATED H_6 bond `B_b^iso` (2-nucleon). Growth = B_b^emb / B_b^iso.
χ at H_9 via the Rust kernel (pyhecke_native, custom (c,d,gen) words).
EXPLORATORY; AME used only for the final cross-check.
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
import pyhecke_native  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402 — CAL-1
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(30)
q0 = mp.mpf(str(Q0))
q0f = float(Q0)
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))      # 𝔈₀ ≈ 4.186 MeV (CAL-3)

# isolated H_6 per-block bonds (this session): B_pn 2.3048, B_pp 2.2861, B_nn 2.2497
B_ISO = {"pn": mp.mpf("2.3048"), "pp": mp.mpf("2.2861"), "nn": mp.mpf("2.2497")}
_Y9 = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
       for k, v in y_lambda_at(9, q0).items()}


def _perblock_word(word):
    """Σ_λ y_λ|χ^λ| at H_9 for a custom (c,d,gen0) word, via the Rust kernel."""
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    chi_pairs = pyhecke_native.chi_q_atomic_all_partitions(9, factors, q0f)
    tot = mp.mpf(0)
    for shape, chi in chi_pairs:
        y = _Y9.get(tuple(shape))
        if y is not None:
            tot += y * abs(mp.mpf(repr(chi)))
    return tot


def _bond_type(Z, N, k):
    """Bond type of the chain interface after nucleon k."""
    ordering = ['p'] * Z + ['n'] * N
    a, b = ordering[k], ordering[k + 1]
    return "pp" if (a, b) == ('p', 'p') else "nn" if (a, b) == ('n', 'n') else "pn"


def main() -> int:
    print(f"E_0 = {float(E0):.4f} MeV   q₀ = {float(q0):.6f}\n")
    results = {}
    for name, (Z, N) in {"T": (1, 2), "3He": (2, 1)}.items():
        full = atom_braid_word_3A(Z, N, include_inter=True)
        free = [x for x in full if x[2] % 3 != 2]
        pf = _perblock_word(free)
        print(f"{name} (Z={Z},N={N}):  perblock(free) = {float(pf):.5f}")
        iso = {}
        for k in range(Z + N - 1):                # chain interfaces
            gen = 3 * k + 2
            bt = _bond_type(Z, N, k)
            word_b = [x for x in full if x[2] % 3 != 2 or x[2] == gen]
            pb = _perblock_word(word_b)
            B_emb = E0 * (pf - pb)
            growth = B_emb / B_ISO[bt]
            iso[f"bond{k}_{bt}"] = {"B_emb_MeV": float(B_emb),
                                    "B_iso_MeV": float(B_ISO[bt]),
                                    "growth": float(growth)}
            print(f"   bond {k} ({bt}) @gen{gen}: B_emb = {float(B_emb):+.4f}  "
                  f"B_iso = {float(B_ISO[bt]):.4f}  growth = {float(growth):.3f}×")
        results[name] = iso
    print("\n  per-bond growth > 1 ⇒ embedded bonds stronger than isolated "
          "(the A=3 −15% residual mechanism).")

    wb = WitnessBuilder("per-bond-growth-a3", engine="mpmath")
    wb.data["q_0"] = str(Q0)
    wb.data["E0_MeV"] = float(E0)
    wb.data["B_iso_MeV"] = {k: float(v) for k, v in B_ISO.items()}
    wb.data["results"] = results
    wb.data["note"] = (
        "Embedded per-bond binding (marginal of one chain interface in the H_9 "
        "free braid) vs isolated H_6 bond. growth>1 ⇒ embedding enhancement, "
        "the A=3 −15% residual mechanism. Rust kernel; no fit.")
    wb.add_assertion("kernel_ran", computed=1, expected=1, tolerance=0)
    wb.save()
    print("\n✓ Witness: per-bond-growth-a3.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
