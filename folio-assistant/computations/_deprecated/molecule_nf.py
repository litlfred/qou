"""
GS-reduced normal forms for molecules at Hecke level k.

Each molecule is specified by its atom content and bond topology.
The GS-reduced NF at level k is the molecule's "braid word" in
H_k(q), analogous to B₃ for nucleons at k=3.

Hierarchy:
  k=3: nucleon = B₃·quarks (6 basis, LP-confined)
  k=3: atom = nucleon^A · electrons (6 basis, Frobenius check)
  k=3: molecule = atom_A · bond · atom_B (6 basis, binding energy)
  k=k: molecule_NF_k = GS-reduced at level k (dim_k basis)

The LP confinement check at each level determines stability:
  - Frobenius positive (Gx ≥ 0): stable
  - Some Gx < 0: unstable (demand channels)
  - LP-confined: stable AND no proper sub-braid is stable

Named molecules store their bond topology and NF at each level
in a registry for reuse.

Usage:
    from molecule_nf import MoleculeRegistry, Molecule

    reg = MoleculeRegistry()
    h2o = reg.get("H2O")
    E = h2o.binding_energy(k=7)
    stable = h2o.is_lp_confined(k=5)

@module folio-assistant/computations/molecule_nf
"""

import json
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from level_k_binding import (
    LevelKEngine, bond_character_cached, seminormal_matrix,
    standard_young_tableaux, E_MOL
)
from q_parameter import Q as q0, Q_INV as qi, HA
from hoefsmit_witness import load_witness


# ══════════════════════════════════════════════════════════════
# Molecule specification
# ══════════════════════════════════════════════════════════════

@dataclass
class Atom:
    """An atom in a molecule."""
    symbol: str
    Z: int
    N: int

    @property
    def A(self):
        return self.Z + self.N

    def __repr__(self):
        return f"{self.symbol}(Z={self.Z},N={self.N})"


@dataclass
class Bond:
    """A bond between two atoms."""
    atom_a: int  # index into molecule's atom list
    atom_b: int
    order: int   # 1=single, 2=double, 3=triple

    def __repr__(self):
        return f"Bond({self.atom_a}-{self.atom_b}, order={self.order})"


@dataclass
class Molecule:
    """A molecule with atoms and bonds."""
    name: str
    formula: str
    atoms: list  # list of Atom
    bonds: list  # list of Bond
    _binding_cache: dict = field(default_factory=dict, repr=False)
    _confinement_cache: dict = field(default_factory=dict, repr=False)

    @property
    def n_atoms(self):
        return len(self.atoms)

    @property
    def n_bonds(self):
        return len(self.bonds)

    @property
    def total_bond_order(self):
        return sum(b.order for b in self.bonds)

    def binding_energy(self, k=3, engine=None):
        """Compute binding energy at Hecke level k.

        Uses the LP dual shadow prices at level k weighted by
        bond characters for each bond in the molecule.

        For a molecule with multiple bonds, the total binding is
        the sum of per-bond contributions (first approximation).
        Ring closure and resonance require the full cyclic
        braid computation.
        """
        if k in self._binding_cache:
            return self._binding_cache[k]

        if engine is None:
            engine = LevelKEngine(k_max=k)

        # Sum per-bond binding energies
        total_E = 0.0
        for bond in self.bonds:
            results = engine.molecular_binding(n_bonds=bond.order,
                                                k_range=range(k, k + 1))
            if k in results:
                total_E += results[k]

        self._binding_cache[k] = total_E
        return total_E

    def lp_confinement_check(self, k=3):
        """Check LP confinement at Hecke level k.

        For each partition λ ⊢ k:
          1. Compute the molecule's character χ_λ(mol)
          2. Check Frobenius positivity: w_λ · χ_λ ≥ 0

        A molecule is LP-confined if:
          - ALL partitions have non-negative weighted character
          - No proper sub-molecule (removing one bond) is also confined

        Returns dict with:
          stable: bool
          marginal_partitions: list of (shape, value) near zero
          demand_partitions: list of (shape, value) negative
        """
        if k in self._confinement_cache:
            return self._confinement_cache[k]

        witness = load_witness()
        level = witness['levels'].get(str(k), [])
        if not level:
            return {"stable": False, "reason": f"no data for k={k}"}

        # The molecule's total bond character is the product of
        # individual bond characters
        total_bond_order = self.total_bond_order

        results = {
            "stable": True,
            "k": k,
            "molecule": self.name,
            "marginal_partitions": [],
            "demand_partitions": [],
            "partition_values": [],
        }

        for entry in level:
            shape = tuple(entry['shape'])
            w_lambda = entry['w']
            dim_lambda = entry['dim']

            # Bond character for the full molecule
            chi, d = bond_character_cached(shape, total_bond_order)
            if d == 0:
                continue

            # Normalized character perturbation
            delta = chi / dim_lambda - 1.0
            value = w_lambda * delta

            results["partition_values"].append({
                "shape": shape,
                "w": w_lambda,
                "chi": chi,
                "dim": dim_lambda,
                "delta": delta,
                "value": value,
            })

            if value < -1e-10:
                results["stable"] = False
                results["demand_partitions"].append((shape, value))
            elif abs(value) < 1e-6:
                results["marginal_partitions"].append((shape, value))

        self._confinement_cache[k] = results
        return results

    def __repr__(self):
        return f"Molecule({self.name}, {self.formula}, {self.n_atoms} atoms, {self.n_bonds} bonds)"


# ══════════════════════════════════════════════════════════════
# Molecule registry with common molecules
# ══════════════════════════════════════════════════════════════

# Standard isotopes
H = Atom("H", 1, 0)
D = Atom("D", 1, 1)
He = Atom("He", 2, 2)
C = Atom("C", 6, 6)
N = Atom("N", 7, 7)
O = Atom("O", 8, 8)
F = Atom("F", 9, 10)
S = Atom("S", 16, 16)
Cl = Atom("Cl", 17, 18)


def _mol(name, formula, atoms, bonds):
    return Molecule(name=name, formula=formula,
                    atoms=[a for a in atoms],
                    bonds=[Bond(b[0], b[1], b[2]) for b in bonds])


# ── Diatomic molecules ───────────────────────────────────────

MOLECULES = {
    "H2": _mol("Hydrogen", "H₂", [H, H],
               [(0, 1, 1)]),

    "N2": _mol("Nitrogen", "N₂", [N, N],
               [(0, 1, 3)]),

    "O2": _mol("Oxygen", "O₂", [O, O],
               [(0, 1, 2)]),

    "HF": _mol("Hydrogen fluoride", "HF", [H, F],
               [(0, 1, 1)]),

    "HCl": _mol("Hydrogen chloride", "HCl", [H, Cl],
                [(0, 1, 1)]),

    "CO": _mol("Carbon monoxide", "CO", [C, O],
               [(0, 1, 3)]),

    # ── Triatomic ────────────────────────────────────────────

    "H2O": _mol("Water", "H₂O", [O, H, H],
                [(0, 1, 1), (0, 2, 1)]),

    "CO2": _mol("Carbon dioxide", "CO₂", [C, O, O],
                [(0, 1, 2), (0, 2, 2)]),

    "H2S": _mol("Hydrogen sulfide", "H₂S", [S, H, H],
                [(0, 1, 1), (0, 2, 1)]),

    # ── Organic basics ───────────────────────────────────────

    "CH4": _mol("Methane", "CH₄", [C, H, H, H, H],
                [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1)]),

    "C2H6": _mol("Ethane", "C₂H₆", [C, C, H, H, H, H, H, H],
                 [(0, 1, 1),  # C-C
                  (0, 2, 1), (0, 3, 1), (0, 4, 1),  # C₁-H
                  (1, 5, 1), (1, 6, 1), (1, 7, 1)]),  # C₂-H

    "C2H4": _mol("Ethylene", "C₂H₄", [C, C, H, H, H, H],
                 [(0, 1, 2),  # C=C
                  (0, 2, 1), (0, 3, 1),  # C₁-H
                  (1, 4, 1), (1, 5, 1)]),  # C₂-H

    "C2H2": _mol("Acetylene", "C₂H₂", [C, C, H, H],
                 [(0, 1, 3),  # C≡C
                  (0, 2, 1),  # C₁-H
                  (1, 3, 1)]),  # C₂-H

    # ── Ring molecules ───────────────────────────────────────

    "C6H6": _mol("Benzene", "C₆H₆",
                 [C, C, C, C, C, C, H, H, H, H, H, H],
                 [  # Kekulé: alternating single/double
                  (0, 1, 2), (1, 2, 1), (2, 3, 2),
                  (3, 4, 1), (4, 5, 2), (5, 0, 1),  # ring closure
                  # C-H bonds
                  (0, 6, 1), (1, 7, 1), (2, 8, 1),
                  (3, 9, 1), (4, 10, 1), (5, 11, 1)]),

    # ── Biological ───────────────────────────────────────────

    "NH3": _mol("Ammonia", "NH₃", [N, H, H, H],
                [(0, 1, 1), (0, 2, 1), (0, 3, 1)]),
}


class MoleculeRegistry:
    """Registry of named molecules with cached NF computations."""

    def __init__(self):
        self._molecules = dict(MOLECULES)
        self._engine = None

    def get(self, name: str) -> Optional[Molecule]:
        return self._molecules.get(name)

    def list_molecules(self):
        for name, mol in sorted(self._molecules.items()):
            print(f"  {name:>8s}: {mol.formula:>8s}  "
                  f"{mol.n_atoms} atoms, {mol.n_bonds} bonds, "
                  f"total order = {mol.total_bond_order}")

    def engine(self, k_max=10):
        if self._engine is None or self._engine.k_max < k_max:
            self._engine = LevelKEngine(k_max=k_max)
        return self._engine

    def binding_table(self, k=3):
        """Compute binding energy for all molecules at level k."""
        eng = self.engine(k)
        results = []
        for name, mol in sorted(self._molecules.items()):
            E = mol.binding_energy(k=k, engine=eng)
            results.append((name, mol.formula, mol.total_bond_order, E))
        return results

    def confinement_scan(self, k=3):
        """Check LP confinement for all molecules at level k."""
        results = []
        for name, mol in sorted(self._molecules.items()):
            check = mol.lp_confinement_check(k=k)
            results.append((name, mol.formula, check["stable"],
                            len(check.get("demand_partitions", [])),
                            len(check.get("marginal_partitions", []))))
        return results


# ══════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    reg = MoleculeRegistry()

    print("=== Molecule Registry ===")
    reg.list_molecules()
    print()

    # Binding energies at k=3
    print("=== Binding energies (k=3) ===")
    print(f"{'Mol':>8s} {'Formula':>8s} {'order':>5s} {'E(eV)':>8s}")
    print("-" * 35)
    for name, formula, order, E in reg.binding_table(k=3):
        print(f"{name:>8s} {formula:>8s} {order:>5d} {E:>8.2f}")
    print()

    # LP confinement scan at k=3..7
    for k in [3, 5, 7]:
        print(f"=== LP confinement scan (k={k}) ===")
        print(f"{'Mol':>8s} {'Formula':>8s} {'stable':>6s} {'demand':>6s} {'marginal':>8s}")
        print("-" * 42)
        for name, formula, stable, n_demand, n_marginal in reg.confinement_scan(k=k):
            print(f"{name:>8s} {formula:>8s} {'YES' if stable else 'NO':>6s} "
                  f"{n_demand:>6d} {n_marginal:>8d}")
        print()

    # Save witness
    from witness_base import WitnessBuilder
    w = WitnessBuilder("molecule-registry", engine="python")
    w.set_description(
        "Molecule registry with binding energies and LP confinement "
        "checks at Hecke levels k=3..7. Named molecules include "
        "diatomic, triatomic, organic, and ring structures."
    )
    w.add_parameter("n_molecules", len(MOLECULES))
    w.add_data("binding_k3",
               {n: {"formula": f, "order": o, "E_eV": round(E, 4)}
                for n, f, o, E in reg.binding_table(k=3)})
    w.add_data("confinement_k3",
               {n: {"formula": f, "stable": s, "demand": d, "marginal": m}
                for n, f, s, d, m in reg.confinement_scan(k=3)})
    w.save()
