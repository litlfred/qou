"""
Canonical Hecke algebra infrastructure for H₃(q).

Single source of truth for:
  - NF basis and multiplication (hm)
  - Gram matrix G
  - Frobenius check
  - Wedderburn weights
  - Atom construction (nucleons + gluon + electrons)
  - Molecular binding (atom × bond × atom)
  - Per-generator vertex volumes (3-channel)
  - Energy scales (nuclear κ, molecular E_mol)

All computations should import from here.

Usage:
    from hecke_core import *
"""

import math
import numpy as np
from q_parameter import Q as q0, Q_INV as qi, HA as h, q_int

# ══════════════════════════════════════════════════════════════
# Constants
# ══════════════════════════════════════════════════════════════

z = 1.0 / (q0**0.5 + qi**0.5)

# Wedderburn weights for H₃(q) (q-deformed, from paper)
q2 = q0**2
_denom_w = q2**2 + 4*q2 + 1
W_SYM = q2 / _denom_w
W_STD = (q2 + 1)**2 / _denom_w
W_ALT = q2 / _denom_w

# Energy scales
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

alpha_em = qi / (q_int(9) * q_int(10))
E_HARTREE_EV = 511000.0 * alpha_em**2
TWO_Q = q0 + qi
E_MOL = E_HARTREE_EV / TWO_Q**2  # molecular energy unit (eV)
KAPPA = M_E_MEV                    # nuclear binding scale (MeV)

# NF basis
NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)]
NF_NAMES = ['γ', 'σ₀', 'σ₁', 'L₊', 'L₋', 'e⁻']
TR_M = np.array([1.0, z, z, z**2, z**2, z**3])

# Crossing coefficients for per-generator chain
PROTON_G0 = [(1,0)]*3 + [(1,0)] + [(1,0)]*2 + [(1,-h/2)]     # 7 crossings
PROTON_G1 = [(1,-h)]*3 + [(1,-h/2)]                            # 4 crossings
NEUTRON_G0 = [(1,0)]*3 + [(1,-h/2)] + [(1,0)] + [(1,0)] + [(1,-h/2)]  # 7
NEUTRON_G1 = [(1,-h)]*3 + [(1,-h)] + [(1,0)] + [(1,0)]        # 6
PE = (1, -h)  # electron pe crossing on gen 1

# Bond operators
INV_TREFOIL_G0 = [(1,-h), (1,-h)]  # σ₀⁻¹σ₀⁻¹
INV_TREFOIL_G1 = [(1,-h)]          # σ₁⁻¹


# ══════════════════════════════════════════════════════════════
# NF multiplication in H₃(q)
# ══════════════════════════════════════════════════════════════

def hm(nf, c, d, gen):
    """Multiply NF element by (c·σ_gen + d·I). Returns new NF."""
    r = [0.0]*6
    if gen == 0:
        tables = [
            (0, [(1,c),(0,d)]),
            (1, [(1,c*h),(0,c),(1,d)]),
            (2, [(3,c),(2,d)]),
            (3, [(3,c*h),(2,c),(3,d)]),
            (4, [(5,c),(4,d)]),
            (5, [(5,c*h),(4,c),(5,d)]),
        ]
    else:
        tables = [
            (0, [(2,c),(0,d)]),
            (1, [(4,c),(1,d)]),
            (2, [(2,c*h),(0,c),(2,d)]),
            (3, [(5,c),(3,d)]),
            (4, [(4,c*h),(1,c),(4,d)]),
            (5, [(5,c*h),(3,c),(5,d)]),
        ]
    for si, tgts in tables:
        if abs(nf[si]) < 1e-15:
            continue
        for ti, co in tgts:
            r[ti] += nf[si] * co
    return r


def nf_tr(nf):
    """Markov trace of NF element."""
    return sum(nf[i] * TR_M[i] for i in range(6))


def nf_net(nf):
    """Net (sum of NF coefficients)."""
    return sum(nf)


# ══════════════════════════════════════════════════════════════
# Gram matrix
# ══════════════════════════════════════════════════════════════

def _hm_dict(t1, t2):
    r = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            r[w] = r.get(w, 0.0) + c1 * c2
    return {w: c for w, c in r.items() if abs(c) > 1e-15}


def _reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            for p in range(len(word) - 1):
                if word[p] == word[p + 1]:
                    i = word[p]
                    pre, suf = word[:p], word[p + 2:]
                    new[pre+(i,)+suf] = new.get(pre+(i,)+suf, 0) + coeff * h
                    new[pre+suf] = new.get(pre+suf, 0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for p in range(len(word) - 2):
                a, b, c = word[p], word[p+1], word[p+2]
                if a == c and abs(a - b) == 1:
                    nt = (b, a, b)
                    if nt < (a, b, a):
                        nw = word[:p] + nt + word[p+3:]
                        new[nw] = new.get(nw, 0) + coeff
                        done = changed = True
                        break
            if not done:
                new[word] = new.get(word, 0) + coeff
        terms = {w: c for w, c in new.items() if abs(c) > 1e-15}
    return terms


def _build_gram():
    G = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            prod = _hm_dict({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0})
            nf = _reduce_nf(prod)
            vec = np.array([nf.get(b, 0.0) for b in NF_BASIS])
            G[i, j] = sum(vec[k] * TR_M[k] for k in range(6))
    return G


G = _build_gram()
G_INV = np.linalg.inv(G)


def check_frobenius(nf):
    """Check Frobenius positivity G·x ≥ 0. Returns (stable, Gx, violations)."""
    x = np.array(nf)
    Gx = G @ x
    violations = [(NF_NAMES[i], Gx[i]) for i in range(6) if Gx[i] < -1e-10]
    return len(violations) == 0, Gx, violations


# ══════════════════════════════════════════════════════════════
# Atom construction
# ══════════════════════════════════════════════════════════════

def build_atom_nf(Z, N):
    """Build atom NF via Hecke multiplication.

    B₃ confinement + typed quark crossings + gluon per nucleon + pe per electron.
    Nucleons interleaved (ground state ordering).
    """
    nf = [1.0, 0, 0, 0, 0, 0]
    pc, nc = 0, 0
    for k in range(Z + N):
        is_p = (k % 2 == 0 and pc < Z) or nc >= N
        if is_p:
            # Proton: B₃ + quarks + gluon
            for _ in range(3):
                nf = hm(nf, 1, 0, 0)
                nf = hm(nf, 1, -h, 1)
            nf = hm(nf, 1, 0, 0)       # uu
            nf = hm(nf, 1, -h/2, 1)    # ud
            nf = hm(nf, 1, -h/2, 0)    # ud
            nf = hm(nf, 1, 0, 0)       # gluon σ₀
            nf = hm(nf, 1, 0, 0)       # gluon σ₀
            pc += 1
        else:
            # Neutron: B₃ + quarks + L₊L₋ gluon
            for _ in range(3):
                nf = hm(nf, 1, 0, 0)
                nf = hm(nf, 1, -h, 1)
            nf = hm(nf, 1, 0, 0)       # ud
            nf = hm(nf, 1, -h/2, 1)    # dd
            nf = hm(nf, 1, -h/2, 0)    # ud
            for _ in range(4):
                nf = hm(nf, 1, 0, 0)   # L₊L₋ gluon
            nc += 1
    # Electrons
    for _ in range(Z):
        nf = hm(nf, 1, -h, 1)  # pe crossing
    return nf


def apply_atom_nf(nf, Z, N):
    """Apply atom crossings to an existing NF (for molecular products)."""
    pc, nc = 0, 0
    for k in range(Z + N):
        is_p = (k % 2 == 0 and pc < Z) or nc >= N
        if is_p:
            for _ in range(3):
                nf = hm(nf, 1, 0, 0)
                nf = hm(nf, 1, -h, 1)
            nf = hm(nf, 1, 0, 0)
            nf = hm(nf, 1, -h/2, 1)
            nf = hm(nf, 1, -h/2, 0)
            nf = hm(nf, 1, 0, 0)
            nf = hm(nf, 1, 0, 0)
            pc += 1
        else:
            for _ in range(3):
                nf = hm(nf, 1, 0, 0)
                nf = hm(nf, 1, -h, 1)
            nf = hm(nf, 1, 0, 0)
            nf = hm(nf, 1, -h/2, 1)
            nf = hm(nf, 1, -h/2, 0)
            for _ in range(4):
                nf = hm(nf, 1, 0, 0)
            nc += 1
    for _ in range(Z):
        nf = hm(nf, 1, -h, 1)
    return nf


def apply_inv_trefoil(nf):
    """Apply inverse trefoil T(2,3)⁻¹ = σ₀⁻¹σ₁⁻¹σ₀⁻¹."""
    nf = hm(nf, 1, -h, 0)
    nf = hm(nf, 1, -h, 1)
    nf = hm(nf, 1, -h, 0)
    return nf


# ══════════════════════════════════════════════════════════════
# Per-generator vertex volumes (3-channel)
# ══════════════════════════════════════════════════════════════

def crossing_coeff(ti, tj):
    """Crossing coefficient d for strand pair (ti, tj). c=1 always.
    Returns None for identity crossings (ne)."""
    if ti == 'p' and tj == 'p': return 0.0
    if ti == 'n' and tj == 'n': return -h
    if (ti, tj) in (('p','n'), ('n','p')): return -h/2
    if (ti, tj) in (('p','e'), ('e','p')): return -h
    if ti == 'e' and tj == 'e': return 0.0
    return None  # ne: identity


def atom_ordering(Z, N):
    """Ground-state interleaved ordering: nucleons then electrons."""
    o = []
    pc, nc = 0, 0
    for k in range(Z + N):
        if k % 2 == 0 and pc < Z:
            o.append('p'); pc += 1
        elif nc < N:
            o.append('n'); nc += 1
        else:
            o.append('p'); pc += 1
    o.extend(['e'] * Z)
    return o


def vertex_volume(chain):
    """3-channel Wedderburn vertex volume from crossing chain."""
    a, b = 0.0, 1.0
    sp, ap = 1.0, 1.0
    for c, d in chain:
        a, b = a*c*h + a*d + b*c, a*c + b*d
        sp *= c*q0 + d
        ap *= -c*qi + d
    V_std = z * a + b
    return W_SYM * sp + W_STD * V_std + W_ALT * ap


def atom_gen_chains(Z, N):
    """Per-generator crossing chains for atom (Z, N).
    Returns (g0_chain, g1_chain)."""
    g0, g1 = [], []
    pc, nc = 0, 0
    for k in range(Z + N):
        is_p = (k % 2 == 0 and pc < Z) or nc >= N
        if is_p:
            g0.extend(PROTON_G0)
            g1.extend(PROTON_G1)
            pc += 1
        else:
            g0.extend(NEUTRON_G0)
            g1.extend(NEUTRON_G1)
            nc += 1
    for _ in range(Z):
        g1.append(PE)
    return g0, g1


def compute_phi1_vv(Z, N):
    """Compute Φ₁ = ln|V̂₀| + ln|V̂₁| from per-generator vertex volumes."""
    g0, g1 = atom_gen_chains(Z, N)
    V0 = vertex_volume(g0)
    V1 = vertex_volume(g1)
    phi = 0.0
    if abs(V0) > 1e-300:
        phi += math.log(abs(V0))
    if abs(V1) > 1e-300:
        phi += math.log(abs(V1))
    return phi


def compute_phi1_full(Z, N):
    """Compute Φ₁ using full atom ordering with per-generator chain.

    Each generator i: gluon + crossings with ALL strands j > i.
    This is the transfer matrix chain from all-nuclei-transfer-matrix.py,
    extended to include electrons.
    """
    ordering = atom_ordering(Z, N)
    n = len(ordering)
    n_nuc = Z + N
    if n <= 1:
        return 0.0

    phi = 0.0
    for i in range(n - 1):
        lam_s, lam_a = 1.0, 1.0
        ai, bi = 0.0, 1.0

        # Gluon for nucleon at position i
        if i < n_nuc:
            ng = 2 if ordering[i] == 'p' else 4
            for _ in range(ng):
                lam_s *= q0
                lam_a *= -qi
                ai, bi = ai*h + bi, ai

        # Crossings with all strands j > i
        for j in range(i + 1, n):
            d = crossing_coeff(ordering[i], ordering[j])
            if d is None:
                continue
            lam_s *= q0 + d
            lam_a *= -qi + d
            ai, bi = ai*(h+d) + bi, ai + bi*d

        v_std = z * ai + bi
        v_full = W_SYM * lam_s + W_STD * v_std + W_ALT * lam_a

        if abs(v_full) > 1e-300:
            phi += math.log(abs(v_full))

    return phi


# ══════════════════════════════════════════════════════════════
# Molecular binding
# ══════════════════════════════════════════════════════════════

def molecular_binding_nf(Z_A, N_A, Z_B, N_B, n_inv_trefoils=1):
    """Compute molecular binding energy using NF multiplication.

    mol = A × (inv_trefoil)^k × B
    binding = ln|tr(A×B)| - ln|tr(mol)|
    E = binding × E_MOL (eV)
    """
    nf_A = build_atom_nf(Z_A, N_A)

    # Unbonded: A × B
    nf_ub = apply_atom_nf(list(nf_A), Z_B, N_B)
    tr_ub = nf_tr(nf_ub)

    # Bonded: A × T⁻¹ᵏ × B
    nf_bond = list(nf_A)
    for _ in range(n_inv_trefoils):
        nf_bond = apply_inv_trefoil(nf_bond)
    nf_bond = apply_atom_nf(nf_bond, Z_B, N_B)
    tr_bond = nf_tr(nf_bond)

    if abs(tr_ub) < 1e-300 or abs(tr_bond) < 1e-300:
        return 0.0, 0.0, tr_ub, tr_bond

    phi_ub = math.log(abs(tr_ub))
    phi_bond = math.log(abs(tr_bond))
    binding = phi_ub - phi_bond
    E_eV = binding * E_MOL

    return E_eV, binding, tr_ub, tr_bond


def molecular_binding_vv(Z_A, N_A, Z_B, N_B, bond_g0=None, bond_g1=None):
    """Compute molecular binding using per-generator vertex volumes.

    gen 0: A_g0 + bond_g0 + B_g0
    gen 1: A_g1 + bond_g1 + B_g1
    """
    g0A, g1A = atom_gen_chains(Z_A, N_A)
    g0B, g1B = atom_gen_chains(Z_B, N_B)

    if bond_g0 is None:
        bond_g0 = INV_TREFOIL_G0
    if bond_g1 is None:
        bond_g1 = INV_TREFOIL_G1

    phi_ub = math.log(abs(vertex_volume(g0A + g0B))) + \
             math.log(abs(vertex_volume(g1A + g1B)))
    phi_bond = math.log(abs(vertex_volume(g0A + bond_g0 + g0B))) + \
               math.log(abs(vertex_volume(g1A + bond_g1 + g1B)))

    binding = phi_ub - phi_bond
    return binding * E_MOL, binding


# ══════════════════════════════════════════════════════════════
# Mass computation
# ══════════════════════════════════════════════════════════════

def atom_mass(Z, N):
    """Compute atomic mass (MeV).

    M = Z×m_p + N×m_n + Z×m_e + κ×Φ₁
    where Φ₁ = per-generator sum over full ordering.
    """
    M_const = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV
    phi = compute_phi1_full(Z, N)
    return M_const + KAPPA * phi, phi
