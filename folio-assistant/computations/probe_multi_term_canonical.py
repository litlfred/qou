#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""Full multi-term mass formula with canonical components — D, T, ³He.

Assembles each term from its canonical source:
  T1 (descended, m_e·|tr_M|): canonical tr_M loaded from registry
    for {p, n, D} via {p,n,D}-tr-M-q0.derivation.json (PR #473);
    T and ³He values are taken from from_scratch/derive_t_h5.py
    and derive_he3.py outputs (= 0.012889, 0.998367) until those
    atoms are added to the derivation-chain registry as well.
  T2+T3 (brane tower): Vol_q^tower algebraic (from symbolic port
    in atom_per_generator_volumes_sym.py)
  T4 (Frobenius co-Casimir): m_e · (2 + 1/[2]_q) per-vortex (n=3)
  T5 (BW chirality): mass-formula-6term witness's
    term5_bw_chirality_binding column (Plancherel-derived; flagged
    in description as caveat)
  T6 (Habiro residue): 0 (placeholder)

Output: `multi-term-canonical-assembly.witness.json`
"""
from __future__ import annotations
import json
import sys
from itertools import combinations
from pathlib import Path

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from atom_per_generator_volumes_sym import (  # noqa: E402
    atom_per_generator_volumes_sym, q, z_sym,
)
from q_parameter import Q as Q0_FLOAT  # noqa: E402

m_e = 0.5109989461

# Canonical tr_M from the derivation-chain registry (PR #473).
# Note: T and ³He do not yet have registry files, but T's value is
# documented in derive_t_h5.py and from_scratch/ (= 0.012889).
# ³He's canonical comes from `from_scratch/derive_he3.py`.
def load_canonical_tr_M():
    tr = {}
    for atom_short, label in [("p", "proton"), ("n", "neutron"), ("D", "deuteron")]:
        path = HERE / f"{atom_short}-tr-M-q0.derivation.json"
        tr[label] = float(json.loads(path.read_text())["target_value"])
    # T and He3 — from from_scratch/ pipeline outputs (not yet registered)
    tr["tritium"] = 0.012889  # from from_scratch/derive_t_h5.py
    tr["helium-3"] = 0.998367  # from from_scratch/derive_he3.py
    return tr


def vol_q_tower_at_q0(Z, N, q0):
    """Algebraic Vol_q^tower(β) at q_0 via symbolic Wedderburn port."""
    vols = atom_per_generator_volumes_sym(Z, N, include_inter=True)
    Vs = [float(vd["full"].subs(q, q0)) for vd in vols]
    z0 = float(z_sym.subs(q, q0))
    n = len(Vs)
    prod = 1.0
    for v in Vs:
        prod *= v
    single = z0 * sum(Vs)
    pair = z0**2 * sum(Vs[i]*Vs[j] for i, j in combinations(range(n), 2))
    return abs(prod) + single + pair


def main() -> int:
    q0 = sp.Rational(str(Q0_FLOAT))
    tr_M = load_canonical_tr_M()

    # T4 (Frobenius co-Casimir, n=3): m_e · (2 + 1/[2]_q)
    inv_2q = 1 / (q0 + 1/q0)
    T4_pervortex = m_e * (2 + float(inv_2q))

    # T5 from existing 6-term witness (Plancherel-convention; caveat)
    w_6term = json.loads((HERE / "mass-formula-6term.witness.json").read_text())
    T5 = {label: w_6term["rows"][label]["term5_bw_chirality_binding"]
          for label in ["D", "T", "3He"]}

    print("=" * 100)
    print("Multi-term mass formula — canonical assembly")
    print("=" * 100)
    print(f"  q_0 = {float(q0):.10f}")
    print(f"  m_e = {m_e}")
    print(f"  T4 (Frobenius co-Casimir, n=3) = m_e·(2+1/[2]_q) = {T4_pervortex:.6f} MeV")
    print()

    atoms = [
        ("D",   "deuteron", 1, 1, 2.22456612, 1),  # ρ=1 per ℓ≤1 rule
        ("T",   "tritium",  1, 2, 8.4817984,  1),
        ("3He", "helium-3", 2, 1, 7.7180375,  1),
    ]

    print(f"  {'atom':<4} {'tr_M':<10} {'Vol_q':<8} {'T1':<9} {'T2+T3':<9} "
          f"{'T4':<7} {'T5':<10} {'B_naive':<9} {'AME':<8} {'err %':<8}")
    print("  " + "-" * 95)

    results = []
    for short, full_name, Z, N, ame, rho in atoms:
        tr_atom = tr_M[full_name]
        T1 = m_e * rho * abs(tr_atom)
        Vol_q = vol_q_tower_at_q0(Z, N, q0)
        T23 = m_e * Vol_q  # interpret Vol_q^tower as dimensionless, scale by m_e
        T4 = T4_pervortex
        T5_val = T5[short]
        T6 = 0.0

        B_naive = T1 + T23 + T4 + T5_val + T6
        err = (B_naive - ame) / ame * 100

        print(f"  {short:<4} {tr_atom:<10.4f} {Vol_q:<8.3f} "
              f"{T1:<9.4f} {T23:<9.4f} {T4:<7.4f} {T5_val:<+10.4f} "
              f"{B_naive:<9.4f} {ame:<8.4f} {err:<+8.2f}")
        results.append({
            "atom": full_name, "Z": Z, "N": N, "rho": rho,
            "canonical_tr_M": tr_atom,
            "Vol_q_tower": Vol_q,
            "T1_descended_MeV": T1,
            "T2_T3_brane_MeV": T23,
            "T4_frobenius_MeV": T4,
            "T5_chirality_MeV": T5_val,
            "T6_habiro_MeV": T6,
            "B_naive_sum_MeV": B_naive,
            "AME_binding_MeV": ame,
            "err_pct": err,
        })
    print()

    # Also try a more nuanced assembly: maybe T1 = E_0·trace_deficit + T4 +T5
    # (the compute heuristic) and add Vol_q to test if it narrows the gap
    print("  Alternative: T1 swapped to compute heuristic (E_0·|tr_M^free - tr_M^atom|):")
    print(f"  {'atom':<4} {'T1_def':<10} {'T2+T3':<9} {'T4':<7} {'T5':<10} "
          f"{'B':<9} {'AME':<8} {'err %':<8}")
    print("  " + "-" * 75)

    # E_0 from proton calibration
    m_p_AME = 938.27208816
    tr_p = tr_M["proton"]
    E_0 = m_p_AME / tr_p

    for short, full_name, Z, N, ame, rho in atoms:
        # T1 deficit: E_0 · |tr_M^free - tr_M^atom|
        # We don't have free vs atom canonical tr_M for atoms; approximate
        # T1_def by (Z·tr_p + N·tr_n) - tr_atom
        tr_p_v = tr_M["proton"]
        tr_n_v = tr_M["neutron"]
        tr_atom_v = tr_M[full_name]
        deficit = abs(Z * tr_p_v + N * tr_n_v - tr_atom_v)
        T1_def = E_0 * deficit  # in MeV via proton calibration
        Vol_q = vol_q_tower_at_q0(Z, N, q0)
        T23 = m_e * Vol_q
        T4 = T4_pervortex
        T5_val = T5[short]
        B = T1_def + T23 + T4 + T5_val
        err = (B - ame) / ame * 100
        print(f"  {short:<4} {T1_def:<10.2f} {T23:<9.4f} {T4:<7.4f} {T5_val:<+10.4f} "
              f"{B:<9.2f} {ame:<8.4f} {err:<+8.2f}%")

    from witness_base import WitnessBuilder
    w = (
        WitnessBuilder("multi-term-canonical-assembly", engine="sympy+mpmath")
        .set_description(
            "Full multi-term mass formula (T1+T2+T3+T4+T5+T6) assembled "
            "from canonical sources: T1 from canonical tr_M registry "
            "(p, n, D from PR #473), T2+T3 from algebraic Vol_q^tower "
            "(symbolic Wedderburn port), T4 from m_e·(2+1/[2]_q), T5 "
            "from existing 6-term witness (Plancherel-derived; caveat), "
            "T6=0 placeholder."
        )
        .add_parameter("q_0", float(q0))
        .add_parameter("m_e_MeV", m_e)
        .add_parameter("T4_pervortex_MeV", T4_pervortex)
        .add_data("results", results)
    )
    out_path = w.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
