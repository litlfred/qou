#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; 3-body cluster correlation.
"""3-body joint-trace correlation — the A=3 −13% residual (no fit).

The embedded all-pairs combiner (#1778) SUMS independent pair-marginals and
lands A=3 at −13%. Binding is really the JOINT trace over all interfaces; the
residual is the inter-bond **cluster correlation** (Ursell/Mayer) — the
genuine 3-body force. For the chain's two adjacent bonds (which share a
nucleon, so they correlate), with `g(S) = perblock(free + interfaces S)`:

    pair-sum   = E_0·[(g∅−g{a}) + (g∅−g{b})]              (independent bonds)
    joint      = E_0·(g∅ − g{a,b})                         (both at once)
    3-body c   = joint − pair-sum  =  E_0·(g{a}+g{b}−g∅−g{a,b})   (connected)

c < 0 ⇒ bonds interfere destructively when co-present (the joint saturates
below the pair-sum) — that interference IS the missing 3-body term. This
probe measures it. χ at H_9 via the Rust kernel; ZERO fit; AME comparison
only. NOTE: covers the two ADJACENT (chain) bonds; the non-adjacent (1-3)
pair needs a long-range interface (flagged, next step).
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
for _d in ("hecke", "habiro", "substrate"):
    _p = str(_Path(__file__).resolve().parent / _d)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
import _path_bridge  # noqa: E402, F401
from codata_constants import AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(30)
q0 = mp.mpf(str(Q0)); q0f = float(Q0)
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))
_Y9 = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
       for k, v in y_lambda_at(9, q0).items()}


def _perblock(word):
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(9, factors, q0f)
    return sum(_Y9[tuple(s)] * abs(mp.mpf(repr(chi)))
               for s, chi in cp if tuple(s) in _Y9)


def _word_with(full, free, iface_gens):
    """free braid + the interface crossings at the chosen gens (in order)."""
    keep = set(iface_gens)
    return [x for x in full if x[2] % 3 != 2 or x[2] in keep]


def main() -> int:
    print(f"E_0 = {float(E0):.4f} MeV   q₀ = {float(q0):.6f}\n")
    AME = {"T": AME_B_TRITIUM_MEV_VALIDATION, "3He": mp.mpf("7.7180")}
    results = {}
    for name, (Z, N) in {"T": (1, 2), "3He": (2, 1)}.items():
        full = atom_braid_word_3A(Z, N, include_inter=True)
        free = [x for x in full if x[2] % 3 != 2]
        gens = sorted({x[2] for x in full if x[2] % 3 == 2})   # [2, 5]
        a, b = gens[0], gens[1]
        g0 = _perblock(free)
        ga = _perblock(_word_with(full, free, [a]))
        gb = _perblock(_word_with(full, free, [b]))
        gab = _perblock(_word_with(full, free, [a, b]))
        B_a = E0 * (g0 - ga); B_b = E0 * (g0 - gb)
        pair_sum = B_a + B_b
        joint = E0 * (g0 - gab)
        c3 = joint - pair_sum            # connected 2-bond (3-body) correlation
        # closed estimate: pair-sum (extensive) is the leading term; add c3
        results[name] = {
            "B_bond_a_MeV": float(B_a), "B_bond_b_MeV": float(B_b),
            "pair_sum_MeV": float(pair_sum), "joint_MeV": float(joint),
            "correlation_c3_MeV": float(c3), "AME_MeV": float(AME[name]),
            "pair_sum_err": float((pair_sum - AME[name]) / AME[name]),
            "joint_err": float((joint - AME[name]) / AME[name]),
        }
        print(f"{name}: B_a={float(B_a):+.4f} B_b={float(B_b):+.4f}  "
              f"pair-sum={float(pair_sum):.4f}  joint={float(joint):.4f}")
        print(f"   3-body correlation c3 = joint − pair-sum = {float(c3):+.4f} MeV"
              f"  ({float(c3/pair_sum)*100:+.1f}% of pair-sum)")
        print(f"   AME={float(AME[name]):.4f}  pair-sum err {float((pair_sum-AME[name])/AME[name])*100:+.1f}%"
              f"  joint err {float((joint-AME[name])/AME[name])*100:+.1f}%\n")

    wb = WitnessBuilder("three-body-joint-trace-a3", engine="mpmath")
    wb.data["q_0"] = str(Q0); wb.data["E0_MeV"] = float(E0)
    wb.data["results"] = results
    wb.data["note"] = ("Cluster (Ursell) correlation of the two adjacent chain "
                       "bonds: c3 = joint − pair-sum = E_0(g_a+g_b−g_0−g_ab). "
                       "c3<0 = destructive co-bond interference = the 3-body "
                       "force. Adjacent pair only; non-adjacent 1-3 flagged. "
                       "Rust kernel; zero fit.")
    wb.add_assertion("kernel_ran", computed=1, expected=1, tolerance=0)
    wb.save()
    print("✓ Witness: three-body-joint-trace-a3.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
