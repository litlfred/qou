#!/usr/bin/env python3
"""Pairwise-magnitude gap: WHERE is the leading-trace binding short, and is it uniform?

The structured-combiner result (PR #2630) isolated the A=3 binding gap to the
PAIRWISE (leading) trace, not the 3-body sign sector: with |chi| magnitude on the
pairwise part and the chirality sign on the 3-body correlation, B_struct still
underbinds ~40%. This probe decomposes that pairwise deficit, 0 fit:

  * per-bond pairwise binding  B_bond = E0 (g0 - g_bond)  with the |chi| combiner
    over the H_9 joint trace (Rust kernel), one bond at a time;
  * total model pairwise       B_pair = sum_bond B_bond;
  * pairwise TARGET            B_pair^tgt = B_AME - b3_empirical
                               (the share of the measured binding NOT attributable
                               to the connected 3-body cluster, b3 = B_AME - 3 B2);
  * deficit                    D = B_pair^tgt - B_pair, both absolute and per-bond.

Question: is D uniform across T (pnn) and 3He (ppn)? A uniform per-bond constant
deficit points at a missing NON-multiplicative (cooperative) enhancement common to
every bond -- the operator-valued branching combiner -- rather than a bond-type
(pp/pn/nn) specific correction. A bond-type-dependent D would instead point at the
per-interface factor (z / z-h / z-h/2). This is a diagnostic, not a closure.
"""
import sys
from pathlib import Path

import mpmath as mp

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "computations" / "probes"))
from chirality_weighted_3body_cluster_probe import (  # noqa: E402
    E0, AME, q0, atom_braid_word_3A, perblock, word_with,
)

B2 = mp.mpf("2.224566")  # deuteron, MeV


def main():
    print(f"E_0 = {float(E0):.4f} MeV   q0 = {float(q0):.6f}   B2 = {float(B2):.4f} MeV  (0 fit)\n")
    rows = []
    for name, (Z, N) in {"T": (1, 2), "3He": (2, 1)}.items():
        full = atom_braid_word_3A(Z, N, include_inter=True)
        free = [x for x in full if x[2] % 3 != 2]
        gens = sorted({x[2] for x in full if x[2] % 3 == 2})
        ame = AME[name]
        b3 = ame - 3 * B2                 # empirical connected 3-body share
        pair_tgt = ame - b3               # == 3*B2; the pairwise target
        g0 = perblock(free, "abs")
        per_bond = []
        for gi in gens:
            gb = perblock(word_with(full, free, [gi]), "abs")
            per_bond.append(E0 * (g0 - gb))
        b_pair = mp.fsum(per_bond)
        deficit = pair_tgt - b_pair
        n_bonds = len(gens)
        print(f"=== {name}  (AME B = {float(ame):.3f} MeV,  b3_emp = {float(b3):+.3f}) ===")
        for k, bb in enumerate(per_bond):
            print(f"    bond {k} (gen {gens[k]}):  B_bond = {float(bb):+.4f} MeV")
        print(f"    B_pair (model, {n_bonds} bonds) = {float(b_pair):+.4f} MeV")
        print(f"    B_pair target (= 3*B2)        = {float(pair_tgt):+.4f} MeV")
        print(f"    DEFICIT D                     = {float(deficit):+.4f} MeV  "
              f"({float(deficit / pair_tgt * 100):+.1f}%)")
        print(f"    per-bond deficit D / n_bonds  = {float(deficit / n_bonds):+.4f} MeV\n")
        rows.append({
            "atom": name,
            "B_AME_MeV": mp.nstr(ame, 8),
            "b3_emp_MeV": mp.nstr(b3, 8),
            "per_bond_MeV": [mp.nstr(b, 8) for b in per_bond],
            "B_pair_model_MeV": mp.nstr(b_pair, 8),
            "B_pair_target_MeV": mp.nstr(pair_tgt, 8),
            "deficit_MeV": mp.nstr(deficit, 8),
            "deficit_pct": mp.nstr(deficit / pair_tgt * 100, 6),
            "deficit_per_bond_MeV": mp.nstr(deficit / n_bonds, 8),
        })

    dT = mp.mpf(rows[0]["deficit_per_bond_MeV"])
    dHe = mp.mpf(rows[1]["deficit_per_bond_MeV"])
    spread = abs(dT - dHe) / ((abs(dT) + abs(dHe)) / 2) * 100
    print("UNIFORMITY CHECK (per-bond deficit):")
    print(f"    T   : {float(dT):+.4f} MeV/bond")
    print(f"    3He : {float(dHe):+.4f} MeV/bond")
    print(f"    relative spread = {float(spread):.1f}%")
    print("    -> small spread => uniform per-bond deficit => points at a cooperative")
    print("       (non-multiplicative) enhancement common to all bonds, NOT a")
    print("       bond-type (pp/pn/nn) specific per-interface-factor correction.")

    import json
    witness = {
        "computation": "pairwise-magnitude-gap-decomposition",
        "description": (
            "Per-bond decomposition of the A=3 pairwise (leading-trace) binding deficit "
            "vs the pairwise target 3*B2, |chi| combiner over the H_9 joint trace, 0 fit. "
            "Tests whether the deficit is uniform per-bond (=> missing cooperative "
            "enhancement) or bond-type dependent (=> per-interface-factor correction)."),
        "scriptFile": "computations/probes/pairwise_magnitude_gap_probe.py",
        "inputs": {"E0_MeV": mp.nstr(E0, 10), "q0": mp.nstr(q0, 12), "B2_MeV": mp.nstr(B2, 8),
                   "fit_params": 0},
        "data": {"rows": rows, "per_bond_deficit_spread_pct": mp.nstr(spread, 6)},
    }
    out = REPO / "computations" / "pairwise-magnitude-gap-decomposition.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwrote {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
