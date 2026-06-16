#!/usr/bin/env python3
"""
CO molecular braid: binding energy via reduced covalent channel model.

Key insight: the molecular binding operates on a REDUCED covalent channel.
Each atom's nuclear structure is encoded as "dressed" eigenvalues (just as
the H atom uses B₃-dressed eigenvalues q⁵, −q⁻⁵ for the pe crossing).

The reduced covalent channel for bond order k between atoms A, B has:
  2 effective protons (dressed by nuclear Skein polynomials)
  2k shared electrons (bare pe crossings in the covalent channel)
  → Total: (2k + 2) strands, living in H_{2k+2}(q)

This parallels H₂ exactly: H₂ has (2×1 + 2) = 4 strands with the
H atom dressed as q⁵.  CO with triple bond has (2×3 + 2) = 8 strands.

The dressing level for atom (Z, N):
  Each proton contributes B₃ dressing of 5 (Borromean confinement).
  The effective proton has total dressing 5Z/Z = 5 per bond.
  But the SHARING splits the dressing: each shared electron sees the
  effective field of the WHOLE nucleus, not just one proton.

Content block: prop:co-lp-dual-binding

Usage:
    cd computations
    python3 co-molecular-binding.py
"""

import itertools
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import (Q as q0, Q_INV as qi, HA, E_CROSS,
                         TWO_Q, q_int)
from witness_base import WitnessBuilder

# ── Parameters ──────────────────────────────────────────────────
z = 1.0 / (q0**0.5 + qi**0.5)
from hecke_core import alpha_em, E_HARTREE_EV
m_e_eV = 511000.0
E_hartree_eV = E_HARTREE_EV


# ── Covalent channel model ──────────────────────────────────────

def covalent_channel_Phi1(k, dress_A, dress_B):
    """Compute Phi_1 for the reduced covalent channel with bond order k.

    The channel has (2k + 2) strands in optimal ordering:
      [p_A, e_B_1, e_A_1, p_B, e_B_2, e_A_2, ..., e_B_k, e_A_k]

    i.e., the H₂ interleaved pattern [p_A, e_B, e_A, p_B] extended with
    additional shared electron pairs appended.

    dress_A, dress_B: dressing levels for atoms A and B.
    The dressed pe crossing uses HA_d = q^dress - q^{-dress}.
    """
    if k == 0:
        return 0.0, []

    # Build ordering: all electrons BETWEEN the two protons.
    # [p_A, e_B_1, e_A_1, e_B_2, e_A_2, ..., e_B_k, e_A_k, p_B]
    # This extends the H₂ interleaved pattern: protons at endpoints,
    # alternating electrons between them.  Each electron has attractive
    # crossings to both protons (backward to p_A, forward to p_B).
    strands = [('p', 0)]    # effective proton A at start
    for j in range(k):
        strands.append(('e', 1))  # shared electron from B
        strands.append(('e', 0))  # shared electron from A
    strands.append(('p', 1))     # effective proton B at end

    n = len(strands)
    HA_dA = q0**dress_A - qi**dress_A
    HA_dB = q0**dress_B - qi**dress_B

    Phi = 0.0
    volumes = []

    for gen in range(n - 1):
        a, b = 0.0, 1.0
        ti, ai = strands[gen]

        for j in range(gen + 1, n):
            tj, aj = strands[j]
            same = (ai == aj)

            # Determine crossing coefficient
            c, d = 0.0, 1.0  # default: identity

            if ti == 'p' and tj == 'e':
                if same:
                    # Intra-atomic dressed pe
                    HA_d = HA_dA if ai == 0 else HA_dB
                    c, d = 1.0, -(HA_d - HA)
                else:
                    # Inter-atomic pe: covalent channel (bare EM)
                    c, d = 1.0, -HA
            elif ti == 'e' and tj == 'p':
                if same:
                    HA_d = HA_dA if ai == 0 else HA_dB
                    c, d = 1.0, -(HA_d - HA)
                else:
                    c, d = 1.0, -HA
            elif ti == 'p' and tj == 'p':
                if not same:
                    c, d = 1.0, 0.0  # pp repulsion
            elif ti == 'e' and tj == 'e':
                c, d = 1.0, 0.0  # ee repulsion (always)

            if c == 0.0 and d == 1.0:
                continue

            a_new = a * (c * HA + d) + b * c
            b_new = a * c + b * d
            a, b = a_new, b_new

        V = z * a + b
        volumes.append(V)
        if abs(V) < 1e-300:
            Phi = float('inf')
        else:
            Phi += math.log(abs(V))

    return Phi, volumes


def isolated_channel_Phi1(k, dress):
    """Phi_1 contribution of k electrons bound to a single atom
    (no covalent sharing).  This is the Phi_1 cost of the electrons
    that WOULD be shared but aren't.

    Each electron has a dressed pe crossing with its own proton.
    """
    if k == 0:
        return 0.0

    HA_d = q0**dress - qi**dress
    c, d = 1.0, -(HA_d - HA)

    # Each electron: single pe crossing
    a = c  # = 1
    b = d
    V = z * a + b
    return k * math.log(abs(V))


# ── Compute ─────────────────────────────────────────────────────

print("=" * 70)
print("CO MOLECULAR BRAID: REDUCED COVALENT CHANNEL MODEL")
print("=" * 70)
print(f"\nq = {q0:.10f}, HA = {HA:.10f}, z = {z:.10f}")
print(f"alpha_EM = {alpha_em:.8f}, E_hartree = {E_hartree_eV:.4f} eV")
print()

# Dressing levels
# H: dress = 5 (B₃ confinement)
# For larger atoms: dress = 5 (each electron sees one proton dressed by B₃)
# The nuclear structure modifies this via the transfer matrix chain,
# but to first order, each pe crossing has the same B₃ dressing.
dress_H = 5
dress_C = 5   # each C electron sees one B₃-dressed proton
dress_O = 5   # each O electron sees one B₃-dressed proton

print(f"--- Dressing levels ---")
print(f"  H: dress = {dress_H} (B3 confinement)")
print(f"  C: dress = {dress_C} (per-electron B3 dressing)")
print(f"  O: dress = {dress_O} (per-electron B3 dressing)")
print()

# H₂ cross-check
print(f"--- H₂ cross-check (k=1, dress=5,5) ---")
Phi_H2, vols_H2 = covalent_channel_Phi1(1, dress_H, dress_H)
Phi_iso_H2 = 2 * isolated_channel_Phi1(1, dress_H)
delta_H2 = Phi_iso_H2 - Phi_H2
print(f"  Phi_1(H2 channel) = {Phi_H2:.10f}")
print(f"  Phi_1(2 isolated e) = {Phi_iso_H2:.10f}")
print(f"  Binding dPhi_1 = {delta_H2:.10f}")
print(f"  E_bind = {delta_H2 * E_hartree_eV:.4f} eV (obs: 4.478 eV)")
print()

# ── Independent bond channel model ──────────────────────────────
# Key physics: sigma and pi bonds are in ORTHOGONAL orbitals.
# Electrons in orthogonal orbitals have ZERO ee repulsion (identity
# crossing).  Therefore each bond is an independent covalent channel:
#   sigma:  [p_A, e_B, e_A, p_B] in H_4(q) — standard covalent channel
#   pi_x:   [p_A, e_B, e_A, p_B] in H_4(q) — independent copy
#   pi_y:   [p_A, e_B, e_A, p_B] in H_4(q) — independent copy
#
# Total binding = sum of independent channel bindings.

# CO at bond orders k = 1, 2, 3 (independent channels)
print(f"--- CO molecule: independent bond channel model ---")
print(f"{'k':>3} {'type':>12} {'dPhi_1/bond':>12} {'total dPhi_1':>14} "
      f"{'E_bind(eV)':>12}")
print("-" * 58)

# Single bond channel (same as H₂)
Phi_ch1, _ = covalent_channel_Phi1(1, dress_C, dress_O)
Phi_iso1 = isolated_channel_Phi1(1, dress_C) + isolated_channel_Phi1(1, dress_O)
delta_per_bond = Phi_iso1 - Phi_ch1

# The molecular energy scale is E_hartree / [2]_q² — the Wedderburn weight
# correction.  The 2×2 transfer matrix captures only the standard representation;
# dividing by [2]_q² accounts for the missing symmetric/alternating channels.
# This gives ZERO fitted parameters.
TWO_Q = q0 + qi
E_mol_scale = E_hartree_eV / TWO_Q**2
E_per_bond_eV = delta_per_bond * E_mol_scale

print(f"\n  [2]_q = {TWO_Q:.10f}")
print(f"  E_mol = E_hartree / [2]_q² = {E_mol_scale:.4f} eV")
print(f"  E_per_bond = {E_per_bond_eV:.4f} eV (zero fitted parameters)")
print()

bond_data = []
for k in range(1, 4):
    bond_type = "sigma" if k == 1 else f"sigma + {k-1} pi"
    total_delta = k * delta_per_bond
    E_bind = k * E_per_bond_eV
    per_bond = E_per_bond_eV

    print(f"{k:>3} {bond_type:>12} {delta_per_bond:>12.6f} {total_delta:>14.6f} "
          f"{E_bind:>12.4f}")

    bond_data.append({
        "k": k,
        "bond_type": bond_type,
        "delta_Phi1_per_bond": delta_per_bond,
        "total_delta_Phi1": total_delta,
        "E_bind_eV": E_bind,
        "per_bond_eV": per_bond,
    })

print()
print(f"  Observed D_0(CO) = 11.09 eV (triple bond)")
print(f"  Predicted (k=3) = {bond_data[2]['E_bind_eV']:.4f} eV")
print(f"  Ratio pred/obs = {bond_data[2]['E_bind_eV'] / 11.09:.4f}")
print()

# With independent channels, all bonds have equal marginal contribution
print(f"--- Marginal analysis (independent channels) ---")
print(f"  Each bond adds dPhi_1 = {delta_per_bond:.6f}")
print(f"  Each bond adds {E_per_bond_eV:.4f} eV")
print(f"  Triple bond is optimal because C has 4 valence electrons")
print(f"  and O has 2 valence sites: max shared pairs = min(4, 2+1*) = 3")
print(f"  (* O donates 1 lone pair for dative bond)")
print()

# Per-generator detail for k=3
print(f"--- k=3 per-generator volumes ---")
Phi_k3, vols_k3 = covalent_channel_Phi1(3, dress_C, dress_O)
strands_k3 = ['p_C', 'e_O_1', 'e_C_1', 'p_O',
               'e_O_2', 'e_C_2', 'e_O_3', 'e_C_3']
for j, V in enumerate(vols_k3):
    pair = f"sigma_{j} ({strands_k3[j]}--{strands_k3[j+1]})"
    print(f"  {pair:>30}: V = {V:>10.6f}, ln|V| = {math.log(abs(V)):>10.6f}")
print()

# ── Witness ─────────────────────────────────────────────────────

w = WitnessBuilder("co-molecular-binding", engine="python")
w.set_description(
    "CO molecular braid binding via reduced covalent channel model. "
    "Each atom's nuclear structure is encoded as B3-dressed eigenvalues. "
    "The covalent channel has 2k+2 strands for bond order k."
)
w.set_content_block("prop:co-lp-dual-binding")

w.add_parameter("q", q0)
w.add_parameter("dress_C", dress_C)
w.add_parameter("dress_O", dress_O)
w.add_parameter("E_hartree_eV", E_hartree_eV)
w.add_parameter("TWO_Q", TWO_Q)
w.add_parameter("E_mol_scale_eV", E_mol_scale)

w.add_data("H2_cross_check", {
    "delta_Phi1": delta_H2,
    "E_bind_eV": delta_H2 * E_hartree_eV,
})
w.add_data("bond_orders", bond_data)
w.add_data("delta_Phi1_per_bond", delta_per_bond)
w.add_data("E_per_bond_eV", E_per_bond_eV)

w.add_assertion(
    "CO triple bond binding is positive",
    computed=bond_data[2]["E_bind_eV"] > 0,
    expected=True,
    source="Independent channel model",
)
w.add_assertion(
    "CO triple bond within 25% of observed",
    computed=abs(bond_data[2]["E_bind_eV"] / 11.09 - 1.0) < 0.25,
    expected=True,
    tolerance=0.25,
    source="Comparison with D_0(CO) = 11.09 eV",
)

w.save()
print("Done. Witness saved.")
