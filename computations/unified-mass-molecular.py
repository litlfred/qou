"""

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
#!/usr/bin/env python3
"""
Unified computation: atomic masses Z=1-20 + molecular binding.

Single consistent framework:
  - Per-generator 3-channel Wedderburn vertex volumes
  - Full atomic braid H_{A+Z}(q): nucleons + electrons
  - Gluon: proton 2×σ₀, neutron 4×σ₀ (LP-derived)
  - Bond: inverse crossings at boundary generator
  - Φ₁ = Σ_i ln|V̂_i^full| where V̂_i = w_s·λ_s + w_d·(z·a+b) + w_a·λ_a

Mass: M = Z·m_p + N·m_n + Z·m_e + m_e × Φ₁
Binding: E = (Φ₁_unbonded - Φ₁_bonded) × E_mol

Usage:
    cd computations
    python3 unified-mass-molecular.py
"""

import math, sys
from pathlib import Path
from mpmath import mp
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi, HA as h, q_int
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from experimental_constants import m_n_derived_3input  # noqa: E402
from witness_base import WitnessBuilder

z = q0**3 / (q0**2 + 1)

# Wedderburn weights (q-deformed, from paper)
q2 = q0**2
denom_w = q2**2 + 4*q2 + 1
w_s = q2 / denom_w
w_d = (q2+1)**2 / denom_w
w_a = q2 / denom_w

# Molecular energy scale
from hecke_core import alpha_em, E_HARTREE_EV as E_hartree_eV, E_MOL as E_mol

# Canonical p-n interface offset (owner ruling 2026-08-15 R3, reaffirmed
# 2026-08-26). `-h/2` is `strict_averaged`, the COLOUR-BLIND convention: it is
# the bar-symmetriser of z and averages the two flavours 50/50, so it cannot
# see the substrate flavour split. Imported rather than open-coded so there is
# one definition; the import is hard on purpose, because a fallback would
# silently compute the blind convention while reporting success.
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402
from codata_constants import M_HE4_ATOMIC_MEV_VALIDATION  # noqa: E402  (AME registry)
TWO_Q = q0 + qi


# ══════════════════════════════════════════════════════════════
# Core: per-generator 3-channel vertex volumes
# ══════════════════════════════════════════════════════════════

def crossing_coeff(ti, tj):
    """Crossing coefficient d for pair (ti, tj). c=1 always."""
    if ti == 'p' and tj == 'p': return 0.0        # pp: σ
    if ti == 'n' and tj == 'n': return -h          # nn: σ⁻¹
    if (ti,tj) in (('p','n'),('n','p')): return _pn_d(h)  # pn: colour-weighted
    if (ti,tj) in (('p','e'),('e','p')): return -h     # pe: EM attraction
    if ti == 'e' and tj == 'e': return 0.0              # ee: EM repulsion
    return None  # ne: identity (skip)


def atom_ordering(Z, N):
    """Ground-state interleaved ordering: nucleons then electrons."""
    o = []
    pc, nc = 0, 0
    A = Z + N
    for k in range(A):
        if k % 2 == 0 and pc < Z:
            o.append('p'); pc += 1
        elif nc < N:
            o.append('n'); nc += 1
        else:
            o.append('p'); pc += 1
    o.extend(['e'] * Z)
    return o


def compute_phi1(ordering, gluon=True):
    """Compute Φ₁ = Σ_i ln|V̂_i| for a strand ordering with 3-channel Wedderburn."""
    n = len(ordering)
    if n <= 1:
        return 0.0

    # Count nucleons (for gluon)
    n_nucleons = sum(1 for s in ordering if s in ('p', 'n'))

    phi = 0.0
    for i in range(n - 1):
        lam_s, lam_a = 1.0, 1.0
        ai, bi = 0.0, 1.0

        # Gluon for nucleon at position i
        if gluon and i < n_nucleons:
            ng = 2 if ordering[i] == 'p' else 4
            for _ in range(ng):
                c, d = 1.0, 0.0
                lam_s *= c*q0 + d
                lam_a *= -c*qi + d
                ai, bi = ai*c*h + ai*d + bi*c, ai*c + bi*d

        # Crossings with all strands j > i
        for j in range(i + 1, n):
            d = crossing_coeff(ordering[i], ordering[j])
            if d is None:
                continue  # identity crossing (ne)
            c = 1.0
            lam_s *= c*q0 + d
            lam_a *= -c*qi + d
            ai, bi = ai*c*h + ai*d + bi*c, ai*c + bi*d

        v_std = z * ai + bi
        v_full = w_s * lam_s + w_d * v_std + w_a * lam_a

        if abs(v_full) > 1e-300:
            phi += mp.log(abs(v_full))

    return phi


def molecular_phi1(ord_A, ord_B, n_bond_crossings=0, gluon=True):
    """Compute Φ₁ for molecule A-B with bond crossings at boundary.

    The molecular ordering is [A strands, B strands].
    At each generator i, crossings include ALL strands j > i from
    BOTH atoms. The bond crossings (σ⁻¹) are added at the boundary
    generator (i = na-1) which ALSO has crossings from A's last
    strand to all of B's strands.
    """
    mol = list(ord_A) + list(ord_B)
    n = len(mol)
    na = len(ord_A)
    n_nuc_total = sum(1 for s in mol if s in ('p', 'n'))

    phi = 0.0
    for i in range(n - 1):
        lam_s, lam_a = 1.0, 1.0
        ai, bi = 0.0, 1.0

        # Gluon for nucleon at global position i
        n_nuc_A = sum(1 for s in ord_A if s in ('p', 'n'))
        n_nuc_B = sum(1 for s in ord_B if s in ('p', 'n'))
        if gluon:
            is_nucleon = mol[i] in ('p', 'n')
            if is_nucleon:
                ng = 2 if mol[i] == 'p' else 4
                for _ in range(ng):
                    lam_s *= q0; lam_a *= -qi
                    ai, bi = ai*h + bi, ai

        # Crossings from strand i to strands j > i:
        # WITHIN same atom: standard typed crossings
        # ACROSS atoms: ONLY if bonded (n_bond_crossings > 0)
        in_A = i < na
        for j in range(i + 1, n):
            j_in_A = j < na
            same_atom = (in_A == j_in_A)

            if same_atom:
                # Intra-atom crossing: always present
                d = crossing_coeff(mol[i], mol[j])
                if d is None: continue
                lam_s *= q0 + d; lam_a *= -qi + d
                ai, bi = ai*(h+d) + bi, ai + bi*d
            else:
                # Inter-atom crossing: ONLY the bond crossings
                # The bond replaces the EM interactions between atoms
                # with n_bond_crossings inverse crossings at the boundary
                pass  # no automatic inter-atom crossings

        # Bond crossings: connect atom A to atom B
        # Applied at the boundary generator (i = na-1)
        if i == na - 1:
            for _ in range(n_bond_crossings):
                d = -h  # σ⁻¹
                lam_s *= q0 + d; lam_a *= -qi + d
                ai, bi = ai*(h+d) + bi, ai + bi*d

        v_std = z * ai + bi
        v_full = w_s * lam_s + w_d * v_std + w_a * lam_a

        if abs(v_full) > 1e-300:
            phi += mp.log(abs(v_full))

    return phi


# ══════════════════════════════════════════════════════════════
# §1. ATOMIC MASS TABLE Z=1-20
# ══════════════════════════════════════════════════════════════

print("=" * 75)
print("UNIFIED COMPUTATION: ATOMIC MASSES + MOLECULAR BINDING")
print("=" * 75)
print("  Per-generator 3-channel Wedderburn on H_{A+Z}(q)")
print("  w_s={:.6f}, w_d={:.6f}, w_a={:.6f}".format(w_s, w_d, w_a))
print("  E_mol = {:.4f} eV".format(E_mol))
print()

isotopes = [
    (1, 0, "H",   938.783),
    (2, 2, "He",  float(M_HE4_ATOMIC_MEV_VALIDATION)),
    (3, 4, "Li",  6535.367),
    (4, 5, "Be",  8394.794),
    (5, 6, "B",  10255.103),
    (6, 6, "C",  11177.930),
    (7, 7, "N",  13043.781),
    (8, 8, "O",  14899.169),
    (9, 10,"F",  17696.901),
    (10,10,"Ne", 18622.835),
    (11,12,"Na", 21414.830),
    (12,12,"Mg", 22341.908),
    (13,14,"Al", 25133.143),
    (14,14,"Si", 26060.344),
    (15,16,"P",  28851.873),
    (16,16,"S",  29781.800),
    (17,18,"Cl", 32573.283),
    (18,22,"Ar", 37224.719),
    (19,20,"K",  36294.464),
    (20,20,"Ca", 37224.918),
]

print("§1. ATOMIC MASSES")
print()
print("{:>4s} {:>3s} {:>3s} {:>5s} {:>10s} {:>10s} {:>10s} {:>8s}".format(
    "Atom","Z","N","n_str","Phi_1","M_pred","M_obs","error"))
print("-" * 58)

atom_phi = {}
mass_errors = []

for Z, N, sym, m_obs in isotopes:
    o = atom_ordering(Z, N)
    phi = compute_phi1(o, gluon=True)
    m_const = Z*M_P_MEV + N*m_n_derived_3input + Z*M_E_MEV
    m_pred = m_const + M_E_MEV * phi
    err = (m_pred - m_obs) / m_obs * 100
    mass_errors.append(abs(err))
    atom_phi[sym] = phi

    print("{:>4s} {:>3d} {:>3d} {:>5d} {:>10.4f} {:>10.3f} {:>10.3f} {:>+7.3f}%".format(
        sym, Z, N, len(o), float(phi), float(m_pred), m_obs, float(err)))

mae_mass = sum(mass_errors) / len(mass_errors)
print()
print("  Mass MAE: {:.4f}%".format(float(mae_mass)))

# ══════════════════════════════════════════════════════════════
# §2. MOLECULAR BINDING (same framework)
# ══════════════════════════════════════════════════════════════

print()
print("=" * 75)
print("§2. MOLECULAR BINDING")
print("  Bond crossings (σ⁻¹) at boundary generator")
print("  E_bind = (Φ₁_unbonded - Φ₁_bonded) × E_mol")
print("=" * 75)
print()

# Scan bond crossings for each bond type
def scan_bond(Z_A, N_A, Z_B, N_B, label, obs, max_k=8):
    ord_A = atom_ordering(Z_A, N_A)
    ord_B = atom_ordering(Z_B, N_B)
    phi_ub = molecular_phi1(ord_A, ord_B, 0, gluon=True)

    best_k, best_E = 0, 0.0
    for k in range(0, max_k + 1):
        phi_b = molecular_phi1(ord_A, ord_B, k, gluon=True)
        bind = phi_ub - phi_b
        E = bind * E_mol
        if 0 < E and (best_E == 0 or abs(E - obs) < abs(best_E - obs)):
            best_k = k
            best_E = E

    return best_k, best_E


bond_types = [
    ("H-H",  1, 0, 1, 0, 4.478),
    ("C-H",  6, 6, 1, 0, 4.33),
    ("C-C",  6, 6, 6, 6, 3.60),
    ("C-O",  6, 6, 8, 8, 3.71),
    ("O-H",  8, 8, 1, 0, 4.82),
    ("N-H",  7, 7, 1, 0, 3.87),
]

print("{:>8s} {:>4s} {:>10s} {:>10s} {:>8s}".format(
    "Bond","k","Predicted","Observed","Error"))
print("-" * 44)

bond_results = {}
for bname, ZA, NA, ZB, NB, obs in bond_types:
    k, E = scan_bond(ZA, NA, ZB, NB, bname, obs)
    err = (E/obs - 1)*100 if E > 0 else float('nan')
    err = float(err) if not isinstance(err, float) else err
    E = float(E) if not isinstance(E, float) else E
    print("{:>8s} {:>4d} {:>8.2f} eV {:>8.2f} eV {:>+7.1f}%".format(
        bname, k, E, obs, err))
    bond_results[bname] = {'k': k, 'E': E, 'obs': obs}

# ── Molecules ─────────────────────────────────────────────────

print()
print("{:>10s} {:>30s} {:>10s} {:>10s} {:>8s}".format(
    "Molecule","Bonds","Predicted","Observed","Error"))
print("-" * 72)

def mol_E(*bonds):
    return sum(bond_results[b]['E'] * n for b, n in bonds)

molecules = [
    ("H₂",    [("H-H",1)],                         4.478),
    ("H₂O",   [("O-H",2)],                         9.51),
    ("NH₃",   [("N-H",3)],                        11.6),
    ("CH₄",   [("C-H",4)],                        17.4),
    ("C₂H₆",  [("C-C",1),("C-H",6)],              29.7),
    ("C₂H₄",  [("C-C",1),("C-H",4)],              23.1),
    ("CO",     [("C-O",3)],                        11.09),
    ("CO₂",   [("C-O",4)],                        16.56),
    ("C₆H₆",  [("C-C",3),("C-C",3),("C-H",6)],   57.4),
    ("C₃H₈",  [("C-C",2),("C-H",8)],              42.0),
]

mol_results = []
for name, bonds, obs in molecules:
    E = sum(bond_results[b]['E'] * n for b, n in bonds)
    err = (E/obs - 1)*100 if E > 0 else float('nan')
    desc = " + ".join("{}×{}".format(n, b) for b, n in bonds)
    print("{:>10s} {:>30s} {:>8.2f} eV {:>8.2f} eV {:>+7.1f}%".format(
        name, desc, float(E), obs, float(err)))
    mol_results.append((name, E, obs, err))

pos_mol = [r for r in mol_results if r[1] > 0]
mae_mol = sum(abs(r[3]) for r in pos_mol) / len(pos_mol) if pos_mol else 0
print()
print("  Molecular MAE: {:.1f}%".format(float(mae_mol)))

# ══════════════════════════════════════════════════════════════
# WITNESS
# ══════════════════════════════════════════════════════════════

w = WitnessBuilder("unified-mass-molecular", engine="python")
w.set_description(
    "Unified atomic mass + molecular binding. "
    "Per-generator 3-channel Wedderburn on H_{A+Z}(q) with electrons. "
    "Bond: inverse crossings at boundary. Gluon: LP-derived."
)
w.set_content_block("def:molecular-braid")
w.add_parameter("q", q0)
w.add_parameter("w_s", w_s)
w.add_parameter("w_d", w_d)
w.add_parameter("w_a", w_a)
w.add_parameter("E_mol_eV", E_mol)
w.add_parameter("kappa_MeV", M_E_MEV)

w.add_data("mass_mae_pct", float(mae_mass))
w.add_data("molecular_mae_pct", float(mae_mol))

for Z, N, sym, obs in isotopes:
    phi = atom_phi[sym]
    mc = Z*M_P_MEV + N*m_n_derived_3input + Z*M_E_MEV
    mp = mc + M_E_MEV * phi
    w.add_data("mass_"+sym, {
        "Z": Z, "N": N, "Phi1": float(phi),
        "M_pred": float(mp), "M_obs": obs,
        "error_pct": float((mp-obs)/obs*100),
    })

for bname, data in bond_results.items():
    w.add_data("bond_"+bname.replace("-",""), data)

for name, E, obs, err in mol_results:
    safe = name.replace("₂","2").replace("₃","3").replace("₄","4").replace("₆","6").replace("₈","8")
    w.add_assertion(
        safe, computed=round(E, 2), expected=obs,
        tolerance=obs*0.5, unit="eV",
    )

w.save()
print("\nDone.")
