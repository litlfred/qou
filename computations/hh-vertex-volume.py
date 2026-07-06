#!/usr/bin/env python3
"""
H₂ binding via per-generator 3-channel Wedderburn vertex volumes.

Uses the FULL decomposition from symbolic-atom-builder.py:
  V̂_i^full = w_sym · λ_i^sym + w_std · V̂_i^std + w_alt · λ_i^alt

where:
  sym channel:  λ_i^sym = ∏_j (c_j·q + d_j)      (eigenvalue q)
  std channel:  V̂_i^std = z·a + b                  (2×2 chain)
  alt channel:  λ_i^alt = ∏_j (-c_j/q + d_j)      (eigenvalue -q⁻¹)

Φ₁ = Σ_i ln|V̂_i^full|

The per-generator crossing list is built from:
  Gen 0: all σ₀ crossings from both atoms + bond operator
  Gen 1: all σ₁ crossings from both atoms + bond operator

Usage:
    cd computations
    python3 hh-vertex-volume.py
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math, sys
from pathlib import Path
from mpmath import mp
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int
from witness_base import WitnessBuilder

z = 1.0/(q0**0.5+qi0**0.5)

# Wedderburn weights (corrected)
def qint(k):
    return (q0**k - qi0**k) / h
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

print("=" * 70)
print("H₂ BINDING: PER-GENERATOR 3-CHANNEL WEDDERBURN VERTEX VOLUMES")
print("=" * 70)
print("  w_sym = {:.6f}, w_std = {:.6f}, w_alt = {:.6f}".format(w_sym, w_std, w_alt))
print("  E_mol = {:.4f} eV".format(E_mol))
print()


def vertex_volume(crossings):
    """Compute V̂_full from a list of (c, d) crossings at one generator.

    Three channels tracked simultaneously:
      sym:  ∏(c·q + d)         eigenvalue q for each σ
      std:  2×2 chain → z·a+b  standard representation
      alt:  ∏(-c/q + d)        eigenvalue -q⁻¹ for each σ
    """
    a, b = 0.0, 1.0
    sp_val, ap_val = 1.0, 1.0
    for c, d in crossings:
        # Standard channel: 2×2 matrix chain
        a, b = a*c*h + a*d + b*c, a*c + b*d
        # Symmetric channel: eigenvalue q
        sp_val *= c*q0 + d
        # Alternating channel: eigenvalue -q⁻¹
        ap_val *= -c*qi0 + d
    V_std = z*a + b
    V_full = w_sym*sp_val + w_std*V_std + w_alt*ap_val
    return V_full, sp_val, V_std, ap_val


def Phi1_from_volumes(vols):
    """Φ₁ = Σ ln|V̂_i|"""
    return sum(mp.log(abs(v)) for v in vols if abs(v) > 1e-300)


# ══════════════════════════════════════════════════════════════
# Build per-generator crossing lists for H atom
# ══════════════════════════════════════════════════════════════
# Proton (11 crossings):
#   B₃ = (σ₀σ₁⁻¹)³: gen 0 gets 3×(1,0), gen 1 gets 3×(1,-h)
#   uu(σ₀): gen 0 gets (1,0)
#   ud(σ₁ mixed): gen 1 gets (1,-h/2)
#   2×gluon(σ₀): gen 0 gets 2×(1,0)
#   ud(σ₀ mixed): gen 0 gets (1,-h/2)
#
# Electron: pe = σ₁⁻¹: gen 1 gets (1,-h)

H_gen0 = [(1,0)]*3 + [(1,0)] + [(1,0)]*2 + [(1,-h/2)]  # 7 crossings
H_gen1 = [(1,-h)]*3 + [(1,-h/2)] + [(1,-h)]             # 5 crossings (3 B₃ + 1 ud + 1 pe)

print("H atom per-generator crossings:")
print("  Gen 0 ({} crossings): {}".format(len(H_gen0),
    ", ".join("({},{})".format(c, "0" if d==0 else "-h/2" if abs(d+h/2)<1e-10 else "-h") for c,d in H_gen0)))
print("  Gen 1 ({} crossings): {}".format(len(H_gen1),
    ", ".join("({},{})".format(c, "0" if d==0 else "-h/2" if abs(d+h/2)<1e-10 else "-h") for c,d in H_gen1)))

V0_H, sp0_H, std0_H, ap0_H = vertex_volume(H_gen0)
V1_H, sp1_H, std1_H, ap1_H = vertex_volume(H_gen1)

print("  V̂₀(H) = {:.6f}  (sym={:.6f}, std={:.6f}, alt={:.6f})".format(
    V0_H, sp0_H, std0_H, ap0_H))
print("  V̂₁(H) = {:.6f}  (sym={:.6f}, std={:.6f}, alt={:.6f})".format(
    V1_H, sp1_H, std1_H, ap1_H))
Phi_H = Phi1_from_volumes([V0_H, V1_H])
print("  Φ₁(H) = ln|V̂₀| + ln|V̂₁| = {:.6f}".format(float(Phi_H)))
print()

# ══════════════════════════════════════════════════════════════
# H × H unbonded: crossing lists concatenated
# ══════════════════════════════════════════════════════════════
# Gen 0: H₁ gen0 + H₂ gen0
# Gen 1: H₁ gen1 + H₂ gen1

HH_gen0 = H_gen0 + H_gen0  # 14 crossings
HH_gen1 = H_gen1 + H_gen1  # 10 crossings

V0_ub, _, _, _ = vertex_volume(HH_gen0)
V1_ub, _, _, _ = vertex_volume(HH_gen1)
Phi_ub = Phi1_from_volumes([V0_ub, V1_ub])

print("H × H unbonded:")
print("  V̂₀ = {:.6f}, V̂₁ = {:.6f}".format(V0_ub, V1_ub))
print("  Φ₁(unbonded) = {:.6f}".format(float(Phi_ub)))
print()

# ══════════════════════════════════════════════════════════════
# H × [bond operator] × H
# The bond operator inserts crossings BETWEEN the two atoms.
# Gen 0 bond crossings go into the gen 0 chain.
# Gen 1 bond crossings go into the gen 1 chain.
# ══════════════════════════════════════════════════════════════

def compute_H2_bond(bond_gen0, bond_gen1, label):
    """Compute H₂ with bond operator crossings inserted between atoms.

    bond_gen0: list of (c,d) for bond crossings on generator 0
    bond_gen1: list of (c,d) for bond crossings on generator 1
    """
    gen0 = H_gen0 + bond_gen0 + H_gen0
    gen1 = H_gen1 + bond_gen1 + H_gen1

    V0, sp0, std0, ap0 = vertex_volume(gen0)
    V1, sp1, std1, ap1 = vertex_volume(gen1)
    Phi = Phi1_from_volumes([V0, V1])
    bind = Phi_ub - Phi
    E = bind * E_mol

    print("  " + label)
    print("    Gen 0: {} crossings, V̂₀ = {:.6f}".format(len(gen0), V0))
    print("      sym={:.6f}, std={:.6f}, alt={:.6f}".format(sp0, std0, ap0))
    print("    Gen 1: {} crossings, V̂₁ = {:.6f}".format(len(gen1), V1))
    print("      sym={:.6f}, std={:.6f}, alt={:.6f}".format(sp1, std1, ap1))
    print("    Φ₁ = {:.6f}, binding = {:.6f}, E = {:.4f} eV".format(float(Phi), float(bind), float(E)))
    return V0, V1, Phi, bind, E


print("=" * 70)
print("BOND OPERATORS (per-generator 3-channel)")
print("=" * 70)
print()

# Inverse trefoil σ₀⁻¹σ₁⁻¹σ₀⁻¹:
#   σ₀⁻¹ → gen 0: (1, -h)
#   σ₁⁻¹ → gen 1: (1, -h)
#   σ₀⁻¹ → gen 0: (1, -h)
compute_H2_bond([(1,-h), (1,-h)], [(1,-h)], "Inverse trefoil T(2,3)⁻¹ = σ₀⁻¹σ₁⁻¹σ₀⁻¹")
print()

# Hopf link (σ₁⁻¹)²:
#   Both on gen 1
compute_H2_bond([], [(1,-h), (1,-h)], "Hopf link (σ₁⁻¹)²")
print()

# (σ₁⁻¹)³ NOT trefoil:
#   All on gen 1
compute_H2_bond([], [(1,-h), (1,-h), (1,-h)], "(σ₁⁻¹)³ (all gen 1, NOT trefoil)")
print()

# Positive trefoil σ₀σ₁σ₀:
compute_H2_bond([(1,0), (1,0)], [(1,0)], "Positive trefoil T(2,3) = σ₀σ₁σ₀")
print()

# Mixed: σ₁⁻¹σ₀⁻¹σ₁⁻¹ (same as inverse trefoil by YB)
compute_H2_bond([(1,-h)], [(1,-h), (1,-h)], "σ₁⁻¹σ₀⁻¹σ₁⁻¹ (= T⁻¹ by Yang-Baxter)")
print()

# Single σ₁⁻¹
compute_H2_bond([], [(1,-h)], "Single σ₁⁻¹")
print()

# Single σ₀⁻¹
compute_H2_bond([(1,-h)], [], "Single σ₀⁻¹")
print()

# σ₀⁻¹σ₀⁻¹ (Hopf on gen 0)
compute_H2_bond([(1,-h),(1,-h)], [], "Hopf (σ₀⁻¹)²")
print()

# σ₀⁻¹σ₁⁻¹ (one on each gen)
compute_H2_bond([(1,-h)], [(1,-h)], "σ₀⁻¹σ₁⁻¹ (one per gen)")
print()

# σ₁⁻¹σ₀⁻¹σ₀⁻¹σ₁⁻¹ (palindromic, 4 crossings)
compute_H2_bond([(1,-h),(1,-h)], [(1,-h),(1,-h)], "σ₁⁻¹σ₀⁻¹σ₀⁻¹σ₁⁻¹ (palindromic)")
print()

# ══════════════════════════════════════════════════════════════
# Summary
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("COMPARISON: NF trace vs 3-channel vertex volume")
print("=" * 70)
print()
print("  The NF trace method (previous scripts) computes:")
print("    Φ₁ = ln|tr_M(NF)|  (single number from 6-vector)")
print()
print("  The vertex volume method computes:")
print("    Φ₁ = Σ_i ln|w_sym·λ_i^sym + w_std·V̂_i^std + w_alt·λ_i^alt|")
print("    (per-generator, 3 channels)")
print()
print("  These are DIFFERENT because the vertex volume decomposes")
print("  into per-generator contributions, while the NF trace is")
print("  a single global trace.")
print()
print("  Observed D_0(H₂) = 4.478 eV")

# Witness
w = WitnessBuilder("hh-vertex-volume", engine="python")
w.set_description(
    "H₂ binding via per-generator 3-channel Wedderburn vertex volumes. "
    "V̂_full = w_sym·λ_sym + w_std·(z·a+b) + w_alt·λ_alt per generator."
)
w.set_content_block("def:h2-molecular-braid")
w.add_parameter("q", q0)
w.add_parameter("w_sym", w_sym)
w.add_parameter("w_std", w_std)
w.add_parameter("w_alt", w_alt)
w.add_parameter("E_mol_eV", E_mol)
w.add_data("H_gen0_n_crossings", len(H_gen0))
w.add_data("H_gen1_n_crossings", len(H_gen1))
w.add_data("Phi_H_isolated", float(Phi_H))
w.add_data("Phi_HH_unbonded", float(Phi_ub))
w.save()
print("\nDone.")
