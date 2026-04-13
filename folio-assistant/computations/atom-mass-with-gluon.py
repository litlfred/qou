#!/usr/bin/env python3
"""
Atom mass with LP-derived gluon crossings per nucleon.

Extends atom_mass_full_hecke.py by adding:
  - 2×σ₀ gluon per proton (integer LP optimal)
  - L₊→L₋ = σ₀σ₁σ₁σ₀ gluon per neutron (integer LP optimal)

These internal crossings are prepended to each nucleon's
per-generator vertex volume chain.
"""

import math, sys, json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0, Q_INV as QI0, HA as HA0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

# Numerical computation (not symbolic — for speed across Z=1-20)
q0 = Q0
qi0 = QI0
h = HA0
z = 1.0 / (q0**0.5 + qi0**0.5)

# Wedderburn weights
qint2 = (q0**2 - qi0**2) / h
nf3 = h * qint2 * ((q0**3 - qi0**3) / h)
ws = 1.0 / nf3; wd = qint2**2 / nf3; wa = 1.0 / nf3
wt = ws + wd + wa; ws /= wt; wd /= wt; wa /= wt

def crossing_coeffs(ti, tj):
    if ti == 1 and tj == 1: return (1.0, 0.0)        # pp → σ
    elif ti == 0 and tj == 0: return (1.0, -h)        # nn → σ⁻¹
    else: return (1.0, -h/2)                           # pn → mixed

# Gluon crossings (from integer LP):
# Proton: 2×σ₀ on gen 0 → [(1,0), (1,0)]
# Neutron: L₊→L₋ = σ₀σ₁·σ₁σ₀ → but this is in H₃(q) internal space.
# At nucleon level, the gluon manifests as additional effective crossings
# on the nucleon's generator chain.
#
# The proton's 2 gluon σ₀ crossings add to its interaction with neighbors.
# In the per-generator chain, these appear as 2 extra (1,0) crossings.
# The neutron's L₊L₋ adds 4 crossings, but they alternate generators.
# At nucleon level (single generator per pair), the effective contribution
# is 2 σ crossings (the L₊ part) + 2 σ⁻¹ crossings (inverted by L₋).
# Net effect: 2×(1,0) + 2×(1,-h) for neutron.
# But actually, L₊L₋ in the sym channel gives eigenvalue q²·q⁻² = 1,
# and in alt gives q⁻²·q² = 1. Only std channel is affected.

# SIMPLER MODEL: the gluon adds EFFECTIVE crossing strength to each
# nucleon's interactions. The proton gets a multiplicative boost of
# V̂_gluon_p per generator, the neutron gets V̂_gluon_n.

def gluon_boost_proton():
    """Vertex volume contribution from 2×σ₀ gluon crossings."""
    a, b = 0.0, 1.0
    sp_v, ap_v = 1.0, 1.0
    for c, d in [(1.0, 0.0), (1.0, 0.0)]:  # 2×σ₀
        a, b = a*c*h + a*d + b*c, a*c + b*d
        sp_v *= c*q0 + d
        ap_v *= -c*qi0 + d
    return ws*sp_v + wd*(z*a+b) + wa*ap_v

def gluon_boost_neutron():
    """Vertex volume from L₊→L₋ = σ₀σ₁σ₁σ₀ (4 crossings)."""
    # At nucleon level, these 4 crossings act on the generator chain
    # In std channel: product of 4 crossing matrices
    a, b = 0.0, 1.0
    sp_v, ap_v = 1.0, 1.0
    # L₊ = σ₀σ₁: two positive crossings
    # L₋ = σ₁σ₀: two more positive crossings
    # Both are positive σ crossings in the nucleon-level chain
    for c, d in [(1.0, 0.0)] * 4:
        a, b = a*c*h + a*d + b*c, a*c + b*d
        sp_v *= c*q0 + d
        ap_v *= -c*qi0 + d
    return ws*sp_v + wd*(z*a+b) + wa*ap_v

V_gluon_p = gluon_boost_proton()
V_gluon_n = gluon_boost_neutron()

print("ATOM MASS WITH LP-DERIVED GLUON CROSSINGS")
print("=" * 70)
print(f"  Gluon boost (proton, 2σ₀):  V̂_g = {V_gluon_p:.6f}")
print(f"  Gluon boost (neutron, 4σ):  V̂_g = {V_gluon_n:.6f}")
print()

def ground_state_ordering(Z, N):
    A = Z + N
    if A <= 1:
        return [1]*Z + [0]*N
    from itertools import combinations
    total = math.comb(A, Z)
    if total <= 5000:
        best = None
        best_cost = float('inf')
        base = [0]*A
        for positions in combinations(range(A), Z):
            ordering = list(base)
            for pos in positions: ordering[pos] = 1
            cost = sum(abs(ordering[i] - ordering[i+1]) for i in range(A-1))
            if cost < best_cost:
                best_cost = cost
                best = ordering
        return best
    else:
        ordering = []
        pi, ni = 0, 0
        for k in range(A):
            if pi < Z and (ni >= N or k % 2 == 0):
                ordering.append(1); pi += 1
            else:
                ordering.append(0); ni += 1
        return ordering

def compute_mass(Z, N, include_gluon=False):
    """Compute atomic mass via 3-channel Wedderburn."""
    ordering = ground_state_ordering(Z, N)
    A = Z + N

    # Per-generator vertex volumes
    vols_full = []
    for i in range(A - 1):
        a, b = 0.0, 1.0
        sp_v, ap_v = 1.0, 1.0

        # Gluon: prepend internal crossings for particle at strand i
        if include_gluon:
            if ordering[i] == 1:  # proton
                for c, d in [(1.0, 0.0)] * 2:  # 2×σ₀
                    a, b = a*c*h + a*d + b*c, a*c + b*d
                    sp_v *= c*q0 + d; ap_v *= -c*qi0 + d
            else:  # neutron
                for c, d in [(1.0, 0.0)] * 4:  # L₊L₋ effective
                    a, b = a*c*h + a*d + b*c, a*c + b*d
                    sp_v *= c*q0 + d; ap_v *= -c*qi0 + d

        # Inter-nucleon crossings (Garside staircase)
        for j in range(i + 1, A):
            c, d = crossing_coeffs(ordering[i], ordering[j])
            a, b = a*c*h + a*d + b*c, a*c + b*d
            sp_v *= c*q0 + d; ap_v *= -c*qi0 + d

        V_full = ws*sp_v + wd*(z*a+b) + wa*ap_v
        vols_full.append(V_full)

    # Skein mass from per-generator volumes
    # M = Z·m_p + N·m_n + Z·m_e + binding
    # binding = Σ ln|V̂_i|
    binding = sum(math.log(abs(v)) for v in vols_full if abs(v) > 1e-300)

    # The mass formula from atomic-braid-mass.md:
    # M = Z·m_p + N·m_n + Z·m_e + α·Σ ln|V̂_i^full|
    # where α is the binding energy scale

    # Use the existing calibration: kappa = m_e
    # The binding energy contribution is kappa × binding
    alpha = M_E_MEV  # energy scale = m_e

    M_constituents = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV
    M_total = M_constituents + alpha * binding

    return M_total, binding, vols_full, ordering

# AME2020 observed masses (MeV)
observed = {
    'H':  938.783, 'He': 3728.401, 'Li': 6535.367, 'Be': 8394.794,
    'B':  10255.103, 'C': 11177.930, 'N': 13043.781, 'O': 14899.169,
    'F':  17696.901, 'Ne': 18622.835, 'Na': 21414.830, 'Mg': 22341.908,
    'Al': 25133.143, 'Si': 26060.344, 'P': 28851.873, 'S': 29781.800,
    'Cl': 32573.283, 'Ar': 37224.719, 'K': 36294.464, 'Ca': 37224.918,
}

isotopes = [
    (1, 0, "H"), (2, 2, "He"), (3, 4, "Li"), (4, 5, "Be"),
    (5, 6, "B"), (6, 6, "C"), (7, 7, "N"), (8, 8, "O"),
    (9, 10, "F"), (10, 10, "Ne"), (11, 12, "Na"), (12, 12, "Mg"),
    (13, 14, "Al"), (14, 14, "Si"), (15, 16, "P"), (16, 16, "S"),
    (17, 18, "Cl"), (18, 22, "Ar"), (19, 20, "K"), (20, 20, "Ca"),
]

print(f"{'Atom':>4} {'Z':>3} {'N':>3} {'M_no_gluon':>12} {'M_gluon':>12} {'M_obs':>12} {'err_no':>8} {'err_gl':>8} {'improved':>9}")
print("-" * 80)

errs_no = []
errs_gl = []

for Z, N, sym in isotopes:
    M_no, _, _, _ = compute_mass(Z, N, include_gluon=False)
    M_gl, _, _, _ = compute_mass(Z, N, include_gluon=True)
    M_obs = observed.get(sym, 0)

    if M_obs > 0:
        err_no = (M_no - M_obs) / M_obs * 100
        err_gl = (M_gl - M_obs) / M_obs * 100
        improved = "✓" if abs(err_gl) < abs(err_no) else ""
        errs_no.append(abs(err_no))
        errs_gl.append(abs(err_gl))
        print(f"{sym:>4} {Z:>3} {N:>3} {M_no:>12.3f} {M_gl:>12.3f} {M_obs:>12.3f} {err_no:>+7.3f}% {err_gl:>+7.3f}% {improved:>9}")

print()
print(f"Mean |error| without gluon: {sum(errs_no)/len(errs_no):.4f}%")
print(f"Mean |error| with gluon:    {sum(errs_gl)/len(errs_gl):.4f}%")
