#!/usr/bin/env python3
"""
All molecules via per-generator 3-channel Wedderburn vertex volumes.

Bond operator = inverse trefoil T(2,3)⁻¹ = σ₀⁻¹σ₁⁻¹σ₀⁻¹
  → gen 0 gets: (1,-h), (1,-h)
  → gen 1 gets: (1,-h)

Each bond is one inverse trefoil inserted between the atoms.
Multiple bonds = multiple trefoils (independent channels for σ/π).

Molecules: H₂, CO (triple), CO₂ (2×double), CH₄, C₆H₆

Usage:
    cd computations
    python3 molecular-vertex-volume.py
"""

import math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int
from witness_base import WitnessBuilder

z = 1.0/(q0**0.5+qi0**0.5)

# Wedderburn weights (corrected: dim_std = [2]_q)
def qint(k): return (q0**k - qi0**k) / h
nf3 = qint(1)*qint(2)*qint(3)
dim_std = qint(2)
w_sym_raw = 1.0 / nf3
w_std_raw = dim_std**2 / nf3
w_alt_raw = 1.0 / nf3
w_total = w_sym_raw + w_std_raw + w_alt_raw
w_sym = w_sym_raw / w_total
w_std = w_std_raw / w_total
w_alt = w_alt_raw / w_total

TWO_Q = q0 + qi0
from hecke_core import alpha_em, E_MOL as E_mol


def vertex_volume(crossings):
    """V̂_full = w_sym·λ_sym + w_std·(z·a+b) + w_alt·λ_alt"""
    a, b = 0.0, 1.0
    sp_val, ap_val = 1.0, 1.0
    for c, d in crossings:
        a, b = a*c*h + a*d + b*c, a*c + b*d
        sp_val *= c*q0 + d
        ap_val *= -c*qi0 + d
    V_std = z*a + b
    return w_sym*sp_val + w_std*V_std + w_alt*ap_val


def Phi1(vols):
    return sum(math.log(abs(v)) for v in vols if abs(v) > 1e-300)


# ══════════════════════════════════════════════════════════════
# Per-generator crossing lists for each atom
# ══════════════════════════════════════════════════════════════
# Proton (11 crossings):
#   Gen 0: 3×σ₀(B₃) + uu(σ₀) + 2×σ₀(gluon) + ud_mixed(σ₀) = 7
#   Gen 1: 3×σ₁⁻¹(B₃) + ud_mixed(σ₁) + pe(σ₁⁻¹) = 5
#
# Neutron (13 crossings):
#   Gen 0: 3×σ₀(B₃) + ud_mixed(σ₀) + σ₀(L₊) + σ₀(L₋) + ud_mixed(σ₀) = 7
#   Gen 1: 3×σ₁⁻¹(B₃) + dd(σ₁⁻¹) + σ₁(L₊) + σ₁(L₋) = 6
#   (no pe for neutron — electrons attach to protons)

PROTON_GEN0 = [(1,0)]*3 + [(1,0)] + [(1,0)]*2 + [(1,-h/2)]
PROTON_GEN1 = [(1,-h)]*3 + [(1,-h/2)] + [(1,-h)]  # last is pe

NEUTRON_GEN0 = [(1,0)]*3 + [(1,-h/2)] + [(1,0)] + [(1,0)] + [(1,-h/2)]
NEUTRON_GEN1 = [(1,-h)]*3 + [(1,-h)] + [(1,0)] + [(1,0)]

# Inverse trefoil bond: σ₀⁻¹σ₁⁻¹σ₀⁻¹
BOND_GEN0 = [(1,-h), (1,-h)]   # two σ₀⁻¹ crossings
BOND_GEN1 = [(1,-h)]           # one σ₁⁻¹ crossing


def atom_crossings(Z, N):
    """Build per-generator crossing lists for atom (Z, N).
    Nucleons interleaved (p,n,p,n,...), then Z electrons (pe on gen 1)."""
    gen0, gen1 = [], []
    pc, nc = 0, 0
    for k in range(Z + N):
        is_p = (k % 2 == 0 and pc < Z) or nc >= N
        if is_p:
            gen0.extend(PROTON_GEN0[:-1])  # proton gen0 without the ud(mixed) at end
            gen0.append((1, -h/2))          # ud mixed on gen 0
            gen1.extend([(1,-h)]*3 + [(1,-h/2)])  # B₃ gen1 + ud mixed
            pc += 1
        else:
            gen0.extend(NEUTRON_GEN0)
            gen1.extend(NEUTRON_GEN1)
            nc += 1
    # Electrons: each pe = σ₁⁻¹ on gen 1
    for _ in range(Z):
        gen1.append((1, -h))
    return gen0, gen1


def compute_molecule(atoms, bonds, label):
    """Compute molecular binding.

    atoms: list of (Z, N) for each atom
    bonds: list of (i, j, order) — bond between atom i and j with given order

    Per-generator crossings: concatenate all atoms' crossings + bond crossings
    inserted between atoms.
    """
    # Build per-atom crossing lists
    atom_gen0 = []
    atom_gen1 = []
    for Z, N in atoms:
        g0, g1 = atom_crossings(Z, N)
        atom_gen0.append(g0)
        atom_gen1.append(g1)

    # Unbonded: just concatenate all atoms
    ub_gen0 = []
    ub_gen1 = []
    for g0 in atom_gen0: ub_gen0.extend(g0)
    for g1 in atom_gen1: ub_gen1.extend(g1)
    V0_ub = vertex_volume(ub_gen0)
    V1_ub = vertex_volume(ub_gen1)
    Phi_ub = Phi1([V0_ub, V1_ub])

    # Bonded: insert bond crossings between atoms
    # For simplicity: lay out atoms in order, insert bonds between consecutive atoms
    # Each bond of order k inserts k inverse trefoils
    bond_gen0 = []
    bond_gen1 = []

    # Build the full chain: atom0 + bonds(0,1) + atom1 + bonds(1,2) + atom2 + ...
    full_gen0 = []
    full_gen1 = []

    for idx, (Z, N) in enumerate(atoms):
        full_gen0.extend(atom_gen0[idx])
        full_gen1.extend(atom_gen1[idx])

        # Add bonds FROM this atom to the next
        for i, j, order in bonds:
            if i == idx:
                for _ in range(order):
                    full_gen0.extend(BOND_GEN0)
                    full_gen1.extend(BOND_GEN1)

    V0_bond = vertex_volume(full_gen0)
    V1_bond = vertex_volume(full_gen1)
    Phi_bond = Phi1([V0_bond, V1_bond])

    bind = Phi_ub - Phi_bond
    E = bind * E_mol

    return Phi_ub, Phi_bond, bind, E, V0_ub, V1_ub, V0_bond, V1_bond


# ══════════════════════════════════════════════════════════════
# Compute all molecules
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("MOLECULAR BINDING: 3-CHANNEL VERTEX VOLUMES + INVERSE TREFOIL")
print("=" * 70)
print("  w_sym={:.4f}, w_std={:.4f}, w_alt={:.4f}".format(w_sym, w_std, w_alt))
print("  E_mol = {:.4f} eV".format(E_mol))
print("  Bond = T(2,3)⁻¹ = σ₀⁻¹σ₁⁻¹σ₀⁻¹ per bond channel")
print()

molecules = [
    ("H₂",   [(1,0), (1,0)],           [(0,1,1)],           4.478),
    ("CO",    [(6,6), (8,8)],           [(0,1,3)],           11.09),
    ("CO₂",  [(8,8), (6,6), (8,8)],    [(0,1,2), (1,2,2)],  16.56),
    ("CH₄",  [(6,6), (1,0), (1,0), (1,0), (1,0)],
             [(0,1,1), (0,2,1), (0,3,1), (0,4,1)],          17.9),
    ("C₂H₆", [(6,6), (6,6), (1,0), (1,0), (1,0), (1,0), (1,0), (1,0)],
              [(0,1,1), (0,2,1), (0,3,1), (0,4,1), (1,5,1), (1,6,1), (1,7,1)],
              30.0),  # ~30 eV atomisation
    ("C₆H₆", [(6,6)]*6 + [(1,0)]*6,
              # 6 C-C σ bonds (ring) + 3 C-C π bonds + 6 C-H bonds
              [(0,1,1), (1,2,1), (2,3,1), (3,4,1), (4,5,1), (5,0,1),  # C-C σ ring
               (0,1,1), (2,3,1), (4,5,1),  # C-C π (3 extra bonds)
               (0,6,1), (1,7,1), (2,8,1), (3,9,1), (4,10,1), (5,11,1)],  # C-H
              57.4),
]

print("{:>8s} {:>5s} {:>12s} {:>12s} {:>10s} {:>10s} {:>8s}".format(
    "Mol", "bonds", "Phi_ub", "Phi_bond", "binding", "E(eV)", "error"))
print("-" * 70)

results = []
for name, atoms, bonds, obs in molecules:
    n_bonds = sum(order for _, _, order in bonds)
    Phi_ub, Phi_bond, bind, E, V0u, V1u, V0b, V1b = compute_molecule(atoms, bonds, name)
    err = (E/obs - 1)*100 if obs > 0 and E > 0 else float('nan')

    print("{:>8s} {:>5d} {:>12.4f} {:>12.4f} {:>10.6f} {:>10.4f} {:>+7.1f}%".format(
        name, n_bonds, Phi_ub, Phi_bond, bind, E, err))

    results.append({
        'name': name, 'n_bonds': n_bonds,
        'Phi_ub': Phi_ub, 'Phi_bond': Phi_bond,
        'bind': bind, 'E': E, 'obs': obs, 'err': err,
        'V0_ub': V0u, 'V1_ub': V1u, 'V0_bond': V0b, 'V1_bond': V1b,
    })

print()
print("=" * 70)
print("DETAIL")
print("=" * 70)
for r in results:
    print()
    print("  {} ({} bonds):".format(r['name'], r['n_bonds']))
    print("    Unbonded: V̂₀={:.4f}, V̂₁={:.4f}, Φ₁={:.4f}".format(
        r['V0_ub'], r['V1_ub'], r['Phi_ub']))
    print("    Bonded:   V̂₀={:.4f}, V̂₁={:.4f}, Φ₁={:.4f}".format(
        r['V0_bond'], r['V1_bond'], r['Phi_bond']))
    print("    Binding = {:.6f}, E = {:.4f} eV (obs {:.2f}, err {:+.1f}%)".format(
        r['bind'], r['E'], r['obs'], r['err']))

print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print("  {:>8s} {:>10s} {:>10s} {:>8s}".format("Mol", "Predicted", "Observed", "Error"))
print("  " + "-" * 40)
for r in results:
    print("  {:>8s} {:>8.2f} eV {:>8.2f} eV {:>+7.1f}%".format(
        r['name'], r['E'], r['obs'], r['err']))
print()
print("  All predictions use ZERO fitted parameters.")
print("  Bond operator = inverse trefoil T(2,3)⁻¹")
print("  Energy scale = E_hartree / [2]_q²")

# ── Witness ───────────────────────────────────────────────────
w = WitnessBuilder("molecular-vertex-volume", engine="python")
w.set_description(
    "Molecular binding via per-generator 3-channel Wedderburn vertex volumes. "
    "Bond operator = inverse trefoil T(2,3)⁻¹. Zero fitted parameters."
)
w.set_content_block("def:molecular-braid")
w.add_parameter("q", q0)
w.add_parameter("E_mol_eV", E_mol)
w.add_parameter("bond_operator", "inverse trefoil sigma_0_inv sigma_1_inv sigma_0_inv")

for r in results:
    w.add_assertion(
        "{} binding".format(r['name']),
        computed=round(r['E'], 2),
        expected=r['obs'],
        tolerance=r['obs'] * 0.5,
        unit="eV",
        source="3-channel vertex volume + inverse trefoil",
    )
    w.add_data(r['name'], {
        'n_bonds': r['n_bonds'],
        'E_eV': r['E'], 'obs_eV': r['obs'],
        'error_pct': r['err'],
    })

w.save()
print("\nDone.")
