#!/usr/bin/env python3
"""
H₂ binding on the FULL (A-1)-generator tower.

Uses the same transfer matrix chain as all-nuclei-transfer-matrix.py:
  - A-1 generators for each atom (one per nucleon pair)
  - Each generator: chain product of 2×2 T(c,d) matrices
  - V̂_i = z·M₁₁ + M₂₁ (Markov trace per generator)
  - Φ₁ = Σ ln|V̂_i|

For H₂ molecular braid:
  - H₁: A=1 → 0 nucleon generators, 1 pe generator
  - Bond: inverse trefoil crossings
  - H₂: A=1 → 0 nucleon generators, 1 pe generator

But H has only 1 nucleon (proton) — there's only the pe crossing.
The "full tower" for H is trivially small.

For C-H: C has A=12 → 11 nucleon generators + pe generators.
The bond crossings insert at the generator BETWEEN the two atoms.

Using 3-channel Wedderburn vertex volumes at each generator.

Usage:
    cd computations
    python3 h2-full-tower.py
"""

import math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int

z = 1.0/(q0**0.5+qi0**0.5)

# Wedderburn weights
def qintv(k): return (q0**k - qi0**k) / h
nf3 = qintv(1)*qintv(2)*qintv(3)
dim_std = qintv(2)
w_s=1.0/nf3; w_d=dim_std**2/nf3; w_a=1.0/nf3
wt=w_s+w_d+w_a; w_s/=wt; w_d/=wt; w_a/=wt
E_mol = 511000.0*(qi0/(q_int(9)*q_int(10)))**2/(q0+qi0)**2


def crossing_coeffs(ti, tj):
    """Nuclear crossing coefficients. ti, tj: 'p' or 'n'."""
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    elif ti == 'n' and tj == 'n': return 1.0, -h
    else: return 1.0, -h/2


def vertex_volume_3ch(crossing_list):
    """3-channel Wedderburn vertex volume from crossing chain at one generator."""
    a, b = 0.0, 1.0
    sp, ap = 1.0, 1.0
    for c, d in crossing_list:
        a, b = a*c*h + a*d + b*c, a*c + b*d
        sp *= c*q0 + d
        ap *= -c*qi0 + d
    V_std = z*a + b
    return w_s*sp + w_d*V_std + w_a*ap


def ground_state_ordering(Z, N):
    """Interleaved nucleon ordering for minimum Φ₁."""
    ordering = []
    pc, nc = 0, 0
    A = Z + N
    for k in range(A):
        if k % 2 == 0 and pc < Z:
            ordering.append('p'); pc += 1
        elif nc < N:
            ordering.append('n'); nc += 1
        else:
            ordering.append('p'); pc += 1
    return ordering


def atom_generator_chains(Z, N, include_gluon=True, include_electrons=True):
    """Build per-generator crossing chains for atom (Z, N).

    Returns list of crossing chains, one per generator.
    Generator i: all crossings between strand i and strands j > i.

    For nucleons: Z protons + N neutrons in ground state ordering.
    Gluon: 2 extra σ crossings per proton, 4 per neutron.
    Electrons: Z pe crossings (σ⁻¹) appended after nucleons.
    """
    A = Z + N
    ordering = ground_state_ordering(Z, N)

    # Total strands: A nucleons + Z electrons
    n_strands = A + Z

    # Build strand types
    strand_types = list(ordering) + ['e'] * Z

    # Per-generator crossing chains
    # Generator i: crossings between strand i and all j > i
    chains = []
    for i in range(n_strands - 1):
        chain = []

        # Gluon crossings for nucleon at position i
        if include_gluon and i < A:
            if strand_types[i] == 'p':
                chain.extend([(1, 0), (1, 0)])  # 2×σ gluon for proton
            else:
                chain.extend([(1, 0)] * 4)      # L₊L₋ gluon for neutron

        for j in range(i + 1, n_strands):
            ti, tj = strand_types[i], strand_types[j]

            if ti in ('p', 'n') and tj in ('p', 'n'):
                # Nuclear crossing
                c, d = crossing_coeffs(ti, tj)
                chain.append((c, d))
            elif (ti in ('p', 'n') and tj == 'e') or (ti == 'e' and tj in ('p', 'n')):
                if ti == 'p' or tj == 'p':
                    # pe crossing: EM attraction (σ⁻¹)
                    chain.append((1, -h))
                else:
                    # ne crossing: identity (skip)
                    pass
            elif ti == 'e' and tj == 'e':
                # ee crossing: EM repulsion (σ)
                chain.append((1, 0))

        if chain:
            chains.append(chain)

    return chains


def Phi1_from_chains(chains):
    """Compute Φ₁ = Σ ln|V̂_i| from per-generator crossing chains."""
    total = 0.0
    for chain in chains:
        V = vertex_volume_3ch(chain)
        if abs(V) > 1e-300:
            total += math.log(abs(V))
    return total


def molecular_Phi1(Z_A, N_A, Z_B, N_B, bond_crossings):
    """Compute Φ₁ for molecule A-B with bond crossings between them.

    The molecular generator chain is:
      [atom A generators] + [bond generator] + [atom B generators]

    The bond crossings create a new generator between the two atoms.
    """
    chains_A = atom_generator_chains(Z_A, N_A)
    chains_B = atom_generator_chains(Z_B, N_B)

    # Bond: new generator(s) between atoms
    # The bond crossings form one or more generators
    mol_chains = list(chains_A)
    if bond_crossings:
        mol_chains.append(bond_crossings)
    mol_chains.extend(chains_B)

    return Phi1_from_chains(mol_chains)


# ══════════════════════════════════════════════════════════════
# Compute
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("FULL (A-1)-GENERATOR TOWER: MOLECULAR BINDING")
print("=" * 70)
print("  3-channel Wedderburn vertex volumes per generator")
print("  E_mol = {:.4f} eV".format(E_mol))
print()

# H atom
chains_H = atom_generator_chains(1, 0)
Phi_H = Phi1_from_chains(chains_H)
print("H atom: {} generators, Φ₁ = {:.6f}".format(len(chains_H), Phi_H))
for i, ch in enumerate(chains_H):
    V = vertex_volume_3ch(ch)
    print("  gen {}: {} crossings, V̂ = {:.6f}".format(i, len(ch), V))
print()

# C atom
chains_C = atom_generator_chains(6, 6)
Phi_C = Phi1_from_chains(chains_C)
print("C atom: {} generators, Φ₁ = {:.6f}".format(len(chains_C), Phi_C))
print()

# O atom
chains_O = atom_generator_chains(8, 8)
Phi_O = Phi1_from_chains(chains_O)
print("O atom: {} generators, Φ₁ = {:.6f}".format(len(chains_O), Phi_O))
print()

# ── H₂ with inverse trefoil bond ─────────────────────────────
print("=" * 70)
print("H₂: inverse trefoil bond on full tower")
print("=" * 70)

# Unbonded: H + H (separate chains)
Phi_HH_ub = Phi_H + Phi_H  # separate atoms = sum of Φ₁
# Actually for molecular product, we should concatenate the chains
Phi_HH_concat = Phi1_from_chains(chains_H + chains_H)

# Bonded: H + bond + H
# Inverse trefoil: σ₀⁻¹σ₁⁻¹σ₀⁻¹
# On the (A-1)-generator tower, this inserts as crossings on the
# bond generator between the two atoms.
# For H₃(q): σ₀⁻¹ = (1,-h) on gen 0, σ₁⁻¹ = (1,-h) on gen 1
# But on the full tower, these are crossings at the new generator
# connecting the two atoms. The inverse trefoil inserts 3 crossings.
inv_trefoil_bond = [(1, -h), (1, -h), (1, -h)]  # 3 inverse crossings on bond generator

Phi_H2_bonded = molecular_Phi1(1, 0, 1, 0, inv_trefoil_bond)
bind_H2 = Phi_HH_concat - Phi_H2_bonded
E_H2 = bind_H2 * E_mol

print("  Φ₁(H+H concat) = {:.6f}".format(Phi_HH_concat))
print("  Φ₁(H₂ bonded)  = {:.6f}".format(Phi_H2_bonded))
print("  binding = {:.6f}".format(bind_H2))
print("  E = {:.4f} eV (obs 4.478)".format(E_H2))
if E_H2 > 0:
    print("  error: {:+.1f}%".format((E_H2/4.478-1)*100))
print()

# Scan different bond crossing counts
print("Scan: k inverse crossings on bond generator")
print("{:>4s} {:>12s} {:>10s} {:>10s}".format("k", "Phi_bond", "E(eV)", "error"))
print("-" * 40)

for k in range(0, 10):
    bond = [(1, -h)] * k
    Phi_b = molecular_Phi1(1, 0, 1, 0, bond)
    bind = Phi_HH_concat - Phi_b
    E = bind * E_mol
    err = (E/4.478-1)*100 if E > 0 else float('nan')
    m = " <--" if abs(err) < 10 and E > 0 else ""
    print("{:>4d} {:>12.6f} {:>10.4f} {:>+9.1f}%{}".format(k, Phi_b, E, err, m))

# ── C-H on full tower ────────────────────────────────────────
print()
print("=" * 70)
print("C-H: full tower")
print("=" * 70)

Phi_CH_concat = Phi1_from_chains(chains_C + chains_H)
print("  Φ₁(C+H concat) = {:.6f}".format(Phi_CH_concat))

print("{:>4s} {:>12s} {:>10s} {:>10s}".format("k", "Phi_bond", "E(eV)", "error"))
print("-" * 40)

for k in range(0, 15):
    bond = [(1, -h)] * k
    Phi_b = molecular_Phi1(6, 6, 1, 0, bond)
    bind = Phi_CH_concat - Phi_b
    E = bind * E_mol
    err = (E/4.33-1)*100 if E > 0 else float('nan')
    m = " <--" if abs(err) < 10 and E > 0 else ""
    print("{:>4d} {:>12.6f} {:>10.4f} {:>+9.1f}%{}".format(k, Phi_b, E, err, m))

# ── C-C on full tower ────────────────────────────────────────
print()
print("=" * 70)
print("C-C: full tower")
print("=" * 70)

Phi_CC_concat = Phi1_from_chains(chains_C + chains_C)
print("  Φ₁(C+C concat) = {:.6f}".format(Phi_CC_concat))

print("{:>4s} {:>12s} {:>10s} {:>10s}".format("k", "Phi_bond", "E(eV)", "error"))
print("-" * 40)

for k in range(0, 15):
    bond = [(1, -h)] * k
    Phi_b = molecular_Phi1(6, 6, 6, 6, bond)
    bind = Phi_CC_concat - Phi_b
    E = bind * E_mol
    err = (E/3.60-1)*100 if E > 0 else float('nan')
    m = " <--" if abs(err) < 10 and E > 0 else ""
    print("{:>4d} {:>12.6f} {:>10.4f} {:>+9.1f}%{}".format(k, Phi_b, E, err, m))

print()
print("Done.")
