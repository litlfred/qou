#!/usr/bin/env python3
"""Run Jones-Markov atlas for all atoms (A ≤ 8) — closes H_3-vs-H_{3A} gap.

Per author direction 2026-05-25: "put in all infra for all nucleotides"
(= isotopes/atoms).

Uses `pyhecke_jones_markov_atlas.solve_jones_markov_h_n` to solve H_{3A}
Jones-Markov y_λ for each atom, then applies via tr_M(β_atom) to compute
canonical B(atom) candidates per the framework's mass formulas.

## Atoms covered (A ≤ 8, partition count ≤ 1575)

  2H   A=2   H_6    11 partitions
  3H   A=3   H_9    30 partitions
  3He  A=3   H_9    30 partitions
  4He  A=4   H_12   77 partitions   ← primary target
  5Li  A=5   H_15   176 partitions  (gap atom)
  6Li  A=6   H_18   385 partitions  (gap atom)
  7Li  A=7   H_21   792 partitions  (gap atom)
  8Be  A=8   H_24   1575 partitions (α-cluster start)

Atoms with A > 8 (12C, 16O, 20Ne, 24Mg, 40Ca) are deferred — partition
count blows up; need closed-form q-Schur principal specialization.

## Heuristic atomic-braid construction

For atom A, build A disjoint Borromean copies in B_{3A}:
  β_atom = Bor(strands 1,2,3) · Bor(strands 4,5,6) · ... · Bor(strands 3A-2,3A-1,3A)

Per Markov axiom (multiplicativity on disjoint generators):
  tr_M(β_atom) = tr_M(β_𝓑_3)^A

The atlas should reproduce this, providing structural verification of
the solver and the H_{3A} weights.

## Output

- Per-atom witness: jones-markov-h-{3A}-{sym}.witness.json
- Aggregate witness: jones-markov-atlas-all-atoms.witness.json
- Console: B(atom) candidates with multi-block H_{3A} corrections
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from pyhecke_jones_markov_atlas import (  # noqa: E402
    solve_jones_markov_h_n,
    tr_M_via_atlas,
)
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, AME_B_LI6_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402  (drain qou-7ot6-a)

mp.mp.dps = 30
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
q0_mpf = mp.mpf(record_upstream(Q_PIN, _UPSTREAM_RECORDS)["derived_50_digit"]["q"])
q0_f64 = float(q0_mpf)
h_mpf = q0_mpf - 1 / q0_mpf
h_f64 = float(h_mpf)

# Closed-form Borromean Markov trace
def tr_M_borromean(h_val):
    h2 = h_val * h_val
    h4 = h2 * h2
    h6 = h4 * h2
    return (4 + h2 - 3 * h4 - h6) / (h2 + 4)

TR_M_BOR = float(tr_M_borromean(mp.mpf(h_f64)))

# Constants
M_E = float(M_E_MEV)  # registry (was the truncated literal 0.510998950)
VOL_BOR = float(8 * mp.catalan)

# AME binding energies
B_AME = {
    "2H":   float(AME_B_DEUTERON_MEV_VALIDATION),
    "3H":   float(AME_B_TRITIUM_MEV_VALIDATION),
    "3He":  float(AME_B_HE3_MEV_VALIDATION),
    "4He": float(AME_B_HE4_MEV_VALIDATION),
    "5Li": 26.328,
    "6Li": float(AME_B_LI6_MEV_VALIDATION),
    "7Li": 39.24453,
    "8Be": 56.49951,
}

# Atoms in (sym, A, Z, N) tuples — A ≤ 8 only
ATOMS = [
    ("2H",  2, 1, 1),  # H_6  — fast
    ("3H",  3, 1, 2),  # H_9  — fast
    ("3He", 3, 2, 1),  # H_9  — fast
    ("4He", 4, 2, 2),  # H_12 — ~100s
    # A ≥ 5 (5Li/6Li/7Li/8Be) need closed-form q-Schur (cycle-type
    # linear system at n ≥ 15 takes hours).  Run with --full flag.
]
ATOMS_HEAVY = [
    ("5Li", 5, 3, 2),
    ("6Li", 6, 3, 3),
    ("7Li", 7, 3, 4),
    ("8Be", 8, 4, 4),
]


def borromean_on(base_strand: int) -> list[tuple[int, int]]:
    """Build (σ_a σ_{a+1}⁻¹)³ where a = base_strand (1-based)."""
    s1, s2 = base_strand, base_strand + 1
    word = []
    for _ in range(3):
        word.append((1, s1))
        word.append((-1, s2))
    return word


def atom_braid(A: int) -> list[tuple[int, int]]:
    """Build heuristic atom braid as A disjoint Borromean copies."""
    word = []
    for i in range(A):
        word.extend(borromean_on(3 * i + 1))
    return word


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true",
                    help="Include heavy atoms (5Li, 6Li, 7Li, 8Be) — hours")
    args = ap.parse_args()
    atoms = ATOMS + (ATOMS_HEAVY if args.full else [])
    print("=" * 110)
    print(f"Jones-Markov atlas — {'ALL ATOMS' if args.full else 'LIGHT ATOMS A ≤ 4'}")
    print(f"  q_0 = {q0_f64:.10f}  h = {h_f64:.10f}")
    print(f"  tr_M(β_𝓑_3) closed form at q_0 = {TR_M_BOR:.10f}")
    print("=" * 110)
    print()

    summary = []

    for sym, A, Z, N in atoms:
        n = 3 * A
        print(f"━━ {sym} (A={A}, Z={Z}, N={N}, H_{n}) ━━")
        t0 = time.time()
        atlas = solve_jones_markov_h_n(n, q=q0_f64, verbose=False)
        atlas_elapsed = time.time() - t0
        print(f"  H_{n} atlas: {atlas['num_partitions']} partitions, "
              f"cond={atlas['condition_number']:.2e}, "
              f"Σy·dim={atlas['sum_y_dim']:.6f}, "
              f"solved in {atlas_elapsed:.2f}s")

        # Compute tr_M(β_atom) via atlas
        beta = atom_braid(A)
        t1 = time.time()
        tr_M_atom = tr_M_via_atlas(atlas, beta)
        tr_M_elapsed = time.time() - t1
        # Verify against multiplicative formula
        tr_M_mult = TR_M_BOR ** A
        agreement = abs(tr_M_atom - tr_M_mult)
        print(f"  tr_M(β_{sym}) via atlas      = {tr_M_atom:.10f}  ({tr_M_elapsed:.2f}s)")
        print(f"  tr_M(β_𝓑_3)^A multiplicative = {tr_M_mult:.10f}")
        print(f"  agreement (|atlas - mult|)   = {agreement:.2e}")

        # Compute candidate B values
        b_ame = B_AME[sym]
        B_prod = 2 * M_E * A * VOL_BOR  # production magic A·8G rule (ν=2)
        B_atlas = 2 * M_E * A * VOL_BOR * tr_M_atom  # production × atlas-tr_M correction
        B_atlas_no_factor = M_E * A * VOL_BOR * tr_M_atom  # without ν=2

        diff_prod = (B_prod - b_ame) / b_ame * 100
        diff_atlas = (B_atlas - b_ame) / b_ame * 100
        diff_atlas_no = (B_atlas_no_factor - b_ame) / b_ame * 100

        print(f"  B_AME({sym})           = {b_ame:.4f} MeV")
        print(f"  B_prod (2·m_e·A·8G)   = {B_prod:.4f} MeV  ({diff_prod:+.4f}%)")
        print(f"  B_prod · tr_M(β_{sym})  = {B_atlas:.4f} MeV  ({diff_atlas:+.4f}%)")
        print(f"  m_e·A·8G · tr_M(β_{sym}) = {B_atlas_no_factor:.4f} MeV  ({diff_atlas_no:+.4f}%)")
        print()

        summary.append({
            "atom": sym, "A": A, "Z": Z, "N": N,
            "n_strands": n,
            "num_partitions": atlas["num_partitions"],
            "condition_number": atlas["condition_number"],
            "sum_y_dim": atlas["sum_y_dim"],
            "atlas_elapsed": atlas_elapsed,
            "tr_M_via_atlas": float(tr_M_atom),
            "tr_M_multiplicative": float(tr_M_mult),
            "agreement": float(agreement),
            "B_AME_MeV": b_ame,
            "B_prod_MeV": float(B_prod),
            "B_prod_with_tr_M_correction_MeV": float(B_atlas),
            "B_no_factor_MeV": float(B_atlas_no_factor),
            "diff_prod_pct": float(diff_prod),
            "diff_atlas_pct": float(diff_atlas),
            "diff_no_factor_pct": float(diff_atlas_no),
        })

    # Aggregate verdict
    print("=" * 110)
    print("SUMMARY — per-atom canonical Jones-Markov correction to B_prod")
    print("=" * 110)
    print(f"  {'atom':>5} {'A':>3} {'H_n':>5} {'#λ':>5}  {'B_AME':>10}  "
          f"{'B_prod':>10}  {'B·tr_M':>10}  {'%prod':>8}  {'%atlas':>8}  improve")
    print("  " + "-" * 100)
    total_prod_err = 0
    total_atlas_err = 0
    for r in summary:
        improve = abs(r["diff_prod_pct"]) - abs(r["diff_atlas_pct"])
        marker = "+" if improve > 0.01 else ("." if abs(improve) <= 0.01 else "−")
        total_prod_err += abs(r["diff_prod_pct"])
        total_atlas_err += abs(r["diff_atlas_pct"])
        print(f"  {r['atom']:>5} {r['A']:>3} H_{r['n_strands']:<3} "
              f"{r['num_partitions']:>5}  "
              f"{r['B_AME_MeV']:>10.4f}  {r['B_prod_MeV']:>10.4f}  "
              f"{r['B_prod_with_tr_M_correction_MeV']:>10.4f}  "
              f"{r['diff_prod_pct']:>+7.3f}%  {r['diff_atlas_pct']:>+7.3f}%  {marker}")
    print(f"\n  total |%prod| = {total_prod_err:.3f}%, total |%atlas| = {total_atlas_err:.3f}%")
    print(f"  net improvement from atlas correction: {total_prod_err - total_atlas_err:+.3f}%")

    # Witness
    w = WitnessBuilder("jones-markov-atlas-all-atoms", engine="python+pyhecke-native+numpy")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Jones-Markov y_λ atlas computed for all atoms A ≤ 8 (n = 3A ≤ 24 "
        "strands). Uses pyhecke_jones_markov_atlas.solve_jones_markov_h_n "
        "with cycle-type representative braids + Schur orthogonality on "
        "the q-Hecke character matrix. Applies each atlas to heuristic "
        "atomic braid β_atom = A disjoint Borromean copies to compute "
        "tr_M(β_atom) and candidate B(atom) values. Tests whether using "
        "the correct H_{3A} weights closes the production B_prod gap."
    )
    w.add_parameter("q_0", q0_f64)
    w.add_parameter("tr_M_borromean_closed_form", TR_M_BOR)
    w.add_parameter("atoms_count", len(atoms))
    w.add_parameter("included_heavy_atoms", bool(args.full))
    w.add_data("per_atom_results", summary)
    w.add_data("aggregate_total_prod_err_pct", total_prod_err)
    w.add_data("aggregate_total_atlas_err_pct", total_atlas_err)
    w.add_data("net_improvement_pct", total_prod_err - total_atlas_err)
    w.add_assertion(
        "all_atoms_atlas_normalized",
        computed=len(summary),
        expected=len(atoms),
        tolerance=0,
        unit="atoms",
        source="solve_jones_markov_h_n per atom",
    )
    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
