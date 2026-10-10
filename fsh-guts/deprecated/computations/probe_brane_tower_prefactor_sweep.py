#!/usr/bin/env python3
# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""Brane-tower prefactor investigation — testing the ρ_q factor across atoms.

prop:mass-endomorphism-tower states:
    m(ρ) = ρ_q · Vol_q^tower(β),   ρ_q = 1/ℏ_q²

Then `B = m_e · m(ρ) at q_0` per prop:atom-knot-mass-derivation.

The symbolic-Wedderburn port `atom_per_generator_volumes_sym` produces
Vol_q^tower(β) ∈ ℤ[q^{1/2}, q^{-1/2}] cleanly. Numerically at q_0:

  atom      Vol_q^tower    m_e·Vol      m_e·ρ_q·Vol    AME-binding/mass
  proton    2.1785         1.11         113.4          938.27 (mass)
  neutron   1.9547         1.00         101.7          939.57 (mass)
  deuteron  3.8266         1.96         199.2          2.22 (binding)
  tritium   6.9279         3.54         360.6          8.48 (binding)
  ³He       7.6262         3.90         397.0          7.72 (binding)

Both `m_e·Vol` and `m_e·ρ_q·Vol` fail to reproduce free-nucleon
masses (938 MeV); the brane-tower clearly does NOT compute total
particle mass via either prefactor. Different physics is needed for
QCD-scale rest mass (probably outside this formula entirely).

For COMPOSITE-ATOM BINDING energies, `m_e·Vol_q^tower`:
- D : 1.96 / 2.22 = 88%   (−12% off)
- T : 3.54 / 8.48 = 42%   (−58% off)
- ³He: 3.90 / 7.72 = 50%  (−49% off)

So Vol_q^tower captures part — but not all — of the binding. This
is consistent with Vol_q^tower being the T2+T3 (brane-tower) terms
of the full multi-term formula:

    B = T1 (descended |tr_M|) + T2+T3 (brane tower)
        + T4 (Frobenius co-Casimir, ~1.28 MeV/nucleon)
        + T5 (chirality factor) + T6 (Habiro residue)

In which case the algebraic finite-Laurent form's contribution is
1-4 MeV per atom, and the remaining gap is what T1, T4, T5, T6
must supply.

CONCLUSION: the ρ_q prefactor in prop:mass-endomorphism-tower
is **wrong** when the goal is to extract MeV binding. Both the
prop's stated form (m_e·ρ_q·Vol = 200-400 MeV) and the
"no-ρ_q" alternative (m_e·Vol = 1-4 MeV) fall short of being a
complete binding formula by themselves. The algebraic Vol_q^tower
must be ONE of the multi-term components, not the complete
binding by itself.
"""
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


def vol_q_tower_at_q0(vols_full, q0):
    Vs = [float(v.subs(q, q0)) for v in vols_full]
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
    hbar_q = (q0 - 1) / q0
    rho_q = float(1 / hbar_q**2)

    atoms = [
        ("proton",   1, 0, "mass",    938.27208816),
        ("neutron",  0, 1, "mass",    939.56542052),
        ("deuteron", 1, 1, "binding", 2.22456612),
        ("tritium",  1, 2, "binding", 8.4817984),
        ("helium-3", 2, 1, "binding", 7.7180375),
    ]

    results = []
    print(f"q_0 = {float(q0):.10f}, ℏ_q = {float(hbar_q):.6f}, "
          f"ρ_q = 1/ℏ_q² = {rho_q:.4f}")
    print()
    print(f"{'atom':<12} {'Z':<2} {'N':<2} {'AME':<11} {'kind':<8} "
          f"{'Vol_q':<8} {'m_e·V':<8} {'m_e·ρ·V':<10} {'err(no ρ)':<12} {'err(ρ)':<10}")
    print("-" * 95)
    for label, Z, N, kind, ame in atoms:
        vols = atom_per_generator_volumes_sym(Z, N, include_inter=True)
        vol = vol_q_tower_at_q0([vd["full"] for vd in vols], q0)
        B_no_rho = m_e * vol
        B_with_rho = m_e * rho_q * vol
        err_no = (B_no_rho - ame) / ame * 100
        err_yes = (B_with_rho - ame) / ame * 100
        print(f"{label:<12} {Z:<2} {N:<2} {ame:<11.4f} {kind:<8} "
              f"{vol:<8.4f} {B_no_rho:<8.4f} {B_with_rho:<10.4f} "
              f"{err_no:<+12.2f}% {err_yes:<+10.0f}%")
        results.append({
            "atom": label, "Z": Z, "N": N, "kind": kind,
            "AME_value_MeV": ame,
            "Vol_q_tower_at_q0": vol,
            "m_e_x_Vol_MeV": B_no_rho,
            "m_e_x_rho_q_x_Vol_MeV": B_with_rho,
            "err_pct_no_rho": err_no,
            "err_pct_with_rho": err_yes,
        })

    print()
    print("Diagnosis:")
    print(" 1. m_e·ρ_q·Vol gives ~100-400 MeV per atom — too large for binding (2-8 MeV)")
    print("    and too small for QCD nucleon mass (938 MeV). Wrong scale either way.")
    print(" 2. m_e·Vol gives 1-4 MeV per atom — right magnitude for binding, but only")
    print("    matches D within −12 %; T and ³He are short by 50-58 %.")
    print(" 3. Conclusion: Vol_q^tower(β) is ONE component of binding (the T2+T3")
    print("    brane-tower), NOT the complete binding. The ρ_q prefactor in")
    print("    prop:mass-endomorphism-tower's stated formula is incorrect for")
    print("    extracting MeV binding directly.")
    print(" 4. Free-nucleon mass (938 MeV) is not produced by EITHER form — likely")
    print("    requires upstream physics not captured by Vol_q^tower alone.")

    from witness_base import WitnessBuilder
    w = (
        WitnessBuilder("brane-tower-prefactor-sweep", engine="sympy+mpmath")
        .set_description(
            "Tests the ρ_q prefactor in prop:mass-endomorphism-tower by "
            "computing m_e·Vol_q^tower and m_e·ρ_q·Vol_q^tower across "
            "p, n, D, T, ³He using the symbolic Wedderburn port."
        )
        .add_parameter("q_0", float(q0))
        .add_parameter("hbar_q", float(hbar_q))
        .add_parameter("rho_q", rho_q)
        .add_parameter("m_e_MeV", m_e)
        .add_data("results", results)
    )
    out_path = w.save()
    print(f"\n  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
