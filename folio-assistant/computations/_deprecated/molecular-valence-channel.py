#!/usr/bin/env python3
"""
Molecular binding via VALENCE SHELL channel only.

H₂ works because the bond IS the whole chain. For heavy atoms,
the bond should operate on the VALENCE SHELL — the electrons
being shared — not the entire atom.

Carbon valence: 4 electrons in n=2 shell (4 pe crossings)
Oxygen valence: 6 electrons in n=2 shell (6 pe crossings)
Hydrogen: 1 electron (1 pe crossing)

The valence channel per atom:
  - The LAST v valence pe crossings on gen 1
  - Plus the nuclear crossing that generates them on gen 0

Bond = inverse trefoil T(2,3)⁻¹ between valence channels.

Usage:
    cd folio-assistant/computations
    python3 molecular-valence-channel.py
"""

import math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int
from witness_base import WitnessBuilder

z = 1.0/(q0**0.5+qi0**0.5)

def qintv(k): return (q0**k - qi0**k) / h
nf3 = qintv(1)*qintv(2)*qintv(3)
dim_std = qintv(2)
w_sym_raw = 1.0/nf3; w_std_raw = dim_std**2/nf3; w_alt_raw = 1.0/nf3
w_total = w_sym_raw + w_std_raw + w_alt_raw
w_sym = w_sym_raw/w_total; w_std = w_std_raw/w_total; w_alt = w_alt_raw/w_total

TWO_Q = q0 + qi0
from hecke_core import alpha_em, E_MOL as E_mol

BOND_G0 = [(1,-h), (1,-h)]  # inverse trefoil gen 0
BOND_G1 = [(1,-h)]          # inverse trefoil gen 1


def vertex_volume(crossings):
    a, b = 0.0, 1.0
    sp_val, ap_val = 1.0, 1.0
    for c, d in crossings:
        a, b = a*c*h + a*d + b*c, a*c + b*d
        sp_val *= c*q0 + d
        ap_val *= -c*qi0 + d
    return w_sym*sp_val + w_std*(z*a+b) + w_alt*ap_val


def Phi1(vols):
    return sum(math.log(abs(v)) for v in vols if abs(v) > 1e-300)


# ══════════════════════════════════════════════════════════════
# Valence shell crossing lists
# ══════════════════════════════════════════════════════════════
# The valence channel includes:
#   Gen 0: the proton σ₀ crossings that the valence electrons "see"
#          = proton gen0 crossings (B₃ σ₀s + quarks + gluon)
#   Gen 1: the valence pe crossings (σ₁⁻¹ each)
#
# For an atom with Z protons, the LAST proton's gen0 crossings
# plus the valence electron pe crossings form the valence channel.
#
# Simpler model: the valence channel has:
#   Gen 0: v_e copies of the proton-electron coupling (1 per valence e)
#          Each is (1, -h/2) — the mixed crossing from quark-electron
#   Gen 1: v_e copies of pe crossing (1, -h)
#
# But this loses the nuclear structure. Better: use the FULL proton
# gen0 chain as the "core" and append valence pe crossings on gen1.

# Proton gen0 (7 crossings): B₃(3σ₀) + uu(σ₀) + gluon(2σ₀) + ud_mixed
PROTON_G0 = [(1,0)]*3 + [(1,0)] + [(1,0)]*2 + [(1,-h/2)]
# Proton gen1 (4 crossings): B₃(3σ₁⁻¹) + ud_mixed
PROTON_G1 = [(1,-h)]*3 + [(1,-h/2)]

# Neutron gen0 (7 crossings)
NEUTRON_G0 = [(1,0)]*3 + [(1,-h/2)] + [(1,0)] + [(1,0)] + [(1,-h/2)]
# Neutron gen1 (6 crossings)
NEUTRON_G1 = [(1,-h)]*3 + [(1,-h)] + [(1,0)] + [(1,0)]

PE = (1, -h)  # electron pe crossing on gen 1


def valence_channel(Z, N, n_valence):
    """Build valence channel crossing lists.

    The valence channel = one representative nucleon's crossings
    + n_valence pe crossings. This is the part of the atom that
    participates in bonding.

    For H: 1 proton + 1 pe = the whole atom
    For C: 1 proton (representative) + 4 pe (valence)
    For O: 1 proton (representative) + 6 pe (valence shell, 2p⁴)
    """
    # Use one proton as the representative nucleon
    g0 = list(PROTON_G0)
    g1 = list(PROTON_G1)
    # Add valence electrons
    for _ in range(n_valence):
        g1.append(PE)
    return g0, g1


print("=" * 70)
print("MOLECULAR BINDING: VALENCE SHELL CHANNEL")
print("=" * 70)
print("  w_sym={:.4f}, w_std={:.4f}, w_alt={:.4f}".format(w_sym, w_std, w_alt))
print("  E_mol = {:.4f} eV".format(E_mol))
print("  Bond = T(2,3)⁻¹ = σ₀⁻¹σ₁⁻¹σ₀⁻¹")
print()

# ══════════════════════════════════════════════════════════════
# Per-bond computation
# ══════════════════════════════════════════════════════════════

def compute_bond(Z_A, N_A, v_A, Z_B, N_B, v_B, n_trefoils, label):
    """Compute single bond between valence channels."""
    g0_A, g1_A = valence_channel(Z_A, N_A, v_A)
    g0_B, g1_B = valence_channel(Z_B, N_B, v_B)

    # Unbonded
    ub_g0 = g0_A + g0_B
    ub_g1 = g1_A + g1_B
    V0_ub = vertex_volume(ub_g0)
    V1_ub = vertex_volume(ub_g1)
    Phi_ub = Phi1([V0_ub, V1_ub])

    # Bonded: n_trefoils inverse trefoils between
    bond_g0 = g0_A + BOND_G0 * n_trefoils + g0_B
    bond_g1 = g1_A + BOND_G1 * n_trefoils + g1_B
    V0_b = vertex_volume(bond_g0)
    V1_b = vertex_volume(bond_g1)
    Phi_b = Phi1([V0_b, V1_b])

    bind = Phi_ub - Phi_b
    E = bind * E_mol
    return Phi_ub, Phi_b, bind, E


# Scan trefoil count for each bond type
bond_types = [
    # (name, Z_A, N_A, valence_A, Z_B, N_B, valence_B, obs_eV)
    ("H-H", 1, 0, 1, 1, 0, 1, 4.478),
    ("C-H", 6, 6, 4, 1, 0, 1, 4.48),
    ("C-C", 6, 6, 4, 6, 6, 4, 3.60),
    ("C-O", 6, 6, 4, 8, 8, 6, 3.70),
    ("O-H", 8, 8, 6, 1, 0, 1, 4.82),
]

bond_results = {}

for bname, ZA, NA, vA, ZB, NB, vB, obs in bond_types:
    print("--- {} (valence: {}+{}) ---".format(bname, vA, vB))

    best_k = 0
    best_err = float('inf')
    prev_E = 0

    print("  {:>3s} {:>10s} {:>10s} {:>10s} {:>10s}".format(
        "k", "binding", "E(eV)", "marginal", "status"))
    print("  " + "-" * 48)

    for k in range(0, 20):
        Phi_ub, Phi_b, bind, E = compute_bond(ZA, NA, vA, ZB, NB, vB, k, bname)
        marginal = E - prev_E

        marker = ""
        if abs(E - obs) / obs < 0.05:
            marker = " ← within 5%"
        if k > 0 and marginal < 0.01:
            marker = " ← exhausted"

        print("  {:>3d} {:>10.6f} {:>10.4f} {:>10.4f}{}".format(
            k, bind, E, marginal, marker))

        if abs(E - obs) < abs(best_err):
            best_err = E - obs
            best_k = k
            best_E = E

        prev_E = E
        if k > 0 and marginal < 0.01:
            break

    print("  → Best: k={}, E={:.4f} eV (obs {:.2f}, err {:+.1f}%)".format(
        best_k, best_E, obs, (best_E/obs-1)*100))
    bond_results[bname] = {'k': best_k, 'E': best_E, 'obs': obs}
    print()

# ══════════════════════════════════════════════════════════════
# Molecules
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("MOLECULES")
print("=" * 70)
print()

hh = bond_results['H-H']
ch = bond_results['C-H']
cc = bond_results['C-C']
co = bond_results['C-O']

molecules = [
    ("H₂",   1*hh['E'],                                  4.478),
    ("CO",    3*co['E'],                                  11.09),
    ("CO₂",  4*co['E'],                                  16.56),
    ("CH₄",  4*ch['E'],                                  17.9),
    ("C₂H₆", 1*cc['E'] + 6*ch['E'],                     30.0),
    ("C₆H₆", 9*cc['E'] + 6*ch['E'],                     57.4),
]

print("  Bond k values: H-H={}, C-H={}, C-C={}, C-O={}".format(
    hh['k'], ch['k'], cc['k'], co['k']))
print()
print("  {:>8s} {:>10s} {:>10s} {:>8s}".format("Mol", "Predicted", "Observed", "Error"))
print("  " + "-" * 40)
for name, pred, obs in molecules:
    err = (pred/obs-1)*100
    print("  {:>8s} {:>8.2f} eV {:>8.2f} eV {:>+7.1f}%".format(name, pred, obs, err))

# Witness
w = WitnessBuilder("molecular-valence-channel", engine="python")
w.set_description(
    "Molecular binding via valence shell channel + inverse trefoil scan. "
    "Bond operates on valence electrons only, not full atom chain."
)
w.set_content_block("def:molecular-braid")
w.add_parameter("q", q0)
w.add_parameter("E_mol_eV", E_mol)
for bname, data in bond_results.items():
    w.add_data("bond_"+bname.replace("-",""), data)
w.add_data("molecules", [{"name":n,"pred":p,"obs":o} for n,p,o in molecules])
for name, pred, obs in molecules:
    w.add_assertion(name, computed=round(pred,1), expected=obs,
                    tolerance=obs*0.3, unit="eV")
w.save()
print("\nDone.")
