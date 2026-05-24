# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
Canonical Hecke algebra infrastructure for H₃(q).

Single source of truth for:
  - NF basis and multiplication (hm)
  - Gram matrix G
  - Frobenius check
  - Wedderburn-Artin weights
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
from fractions import Fraction
from q_parameter import Q as q0, Q_INV as qi, HA as h, q_int, E_CROSS

# ── pyhecke bootstrap (M2b inversion: Gram + NF moved to pyhecke.gram) ─
# Preferred: install pyhecke as a package (`pip install -e tools/pyhecke`)
# so this file's dependencies are explicit. Fallback: development mode
# where pyhecke lives on disk but isn't installed — probe-import once;
# on failure, add the source directory to sys.path and retry via the
# single unified import statement below.
#
# Gemini review r3106... flagged the earlier try/except that duplicated
# the entire import list. This refactor keeps the dev-mode fallback but
# avoids the duplicated symbol block: the sys.path patch runs only as
# a side-effect of a lightweight probe, then the authoritative import
# happens once.
try:
    import pyhecke.gram as _probe  # noqa: F401
except ImportError:
    import os as _os
    import sys as _sys
    _PYHECKE_PATH = _os.path.normpath(
        _os.path.join(_os.path.dirname(__file__), "..", "..", "tools", "pyhecke", "python")
    )
    if _os.path.isdir(_PYHECKE_PATH) and _PYHECKE_PATH not in _sys.path:
        _sys.path.insert(0, _PYHECKE_PATH)

from pyhecke.gram import (  # noqa: E402
    z, W_SYM, W_STD, W_ALT,
    NF_BASIS, NF_NAMES, TR_M,
    INV_TREFOIL_G0, INV_TREFOIL_G1,
    hm, hm_exact, nf_tr, nf_net,
    G, G_INV,
    _H_FRAC, _Z_FRAC, _TR_M_FRAC, _SYM_EIG_FRAC, _ALT_EIG_FRAC,
    _Q_FRAC, _QI_FRAC,
)

# ══════════════════════════════════════════════════════════════
# Constants (non-Gram; see pyhecke.gram for Gram/NF/Wedderburn)
# ══════════════════════════════════════════════════════════════

q2 = q0**2  # kept for local alpha_em derivation below

# Energy scales
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

# ── Fine structure constant ────────────────────────────────────────────────────
# α_EM enters the physics through THREE channels:
#   1. Coulomb term (term 3): uses HA·[6]_q·m_e, NOT α_EM.
#      The nuclear Coulomb interaction is encoded in the pp crossing eigenvalue.
#   2. Molecular binding: uses E_HARTREE = m_e·c²·α² → USES corrected α.
#   3. Half-lives: uses α_EM in Fermi phase space (Sommerfeld factor) → USES corrected α.
#
# Bare value (Hecke algebra projection, no CS correction).
# This is the multiplicative-chain identity from
# prop:alpha-em-shift-multiplicative-chain:
#   α_EM⁻¹ = q · [α_shift(T_{2,9})]_q · [α_shift(T_{3,5})]_q
#          = q · [9]_q · [10]_q
# where α_shift(T_{p,k}) = k(p-1) on V_{(1^p)} per
# prop:alpha-shift-torus-knot. Verified to 50 dps in
# folio-assistant/computations/alpha-em-shift-multiplicative-chain.witness.json
_bare_alpha_em = qi / (q_int(9) * q_int(10))
_bare_alpha_inv = q0 * q_int(9) * q_int(10)

# CS-corrected value with Gram matrix κ from J²(Bring's surface):
# 1/α = bare × (1 + c₁ + c₁²×κ) where:
#   c₁ = (CS₁+CS₂)·([2]_q/2)·ℏ_q²/bare  (J¹ correction)
#   κ = det(G_CS_classical)/det(G_CS_q)    (J² correction from Gram ratio)
#
# G_CS encodes the CS pairing of T_{2,9}∪T_{3,5} on Bring's surface:
#   Diagonal: CS + self-linking²/crossing²
#   Off-diagonal: mutual CS from linking number |2×5-3×9|=17
_CS_T29 = math.pi**2 * 10.0/9.0       # CS(T_{2,9}) = π²(m²-1)(n²-1)/(12mn)
_CS_T35 = math.pi**2 * 16.0/15.0      # CS(T_{3,5})
_hbar_q2 = (1.0 - qi)**2               # ℏ_q²
_n2 = q_int(2)
_c1 = (_CS_T29 + _CS_T35) * (_n2/2.0) * _hbar_q2 / _bare_alpha_inv

# Gram matrix of CS pairing (classical)
_sl = 8  # self-linking = (m-1)(n-1) for both T_{2,9} and T_{3,5}
_linking = 17  # |2×5-3×9|
_G_cl_11 = _CS_T29 + math.pi**2 * _sl**2 / (2*9)**2
_G_cl_22 = _CS_T35 + math.pi**2 * _sl**2 / (3*5)**2
_G_cl_12 = math.pi**2 * _linking**2 / (2*9 * 3*5)
_det_G_cl = _G_cl_11 * _G_cl_22 - _G_cl_12**2

# Gram matrix (q-deformed: replace m,n with [m],[n])
_linking_q = abs(_n2*q_int(5) - q_int(3)*q_int(9))
_CS_q_29 = math.pi**2 * (_n2**2-1)*(q_int(9)**2-1)/(12*_n2*q_int(9))
_CS_q_35 = math.pi**2 * (q_int(3)**2-1)*(q_int(5)**2-1)/(12*q_int(3)*q_int(5))
_sl_q_29 = (_n2-1)*(q_int(9)-1)
_sl_q_35 = (q_int(3)-1)*(q_int(5)-1)
_G_q_11 = _CS_q_29 + math.pi**2 * _sl_q_29**2 / (_n2*q_int(9))**2
_G_q_22 = _CS_q_35 + math.pi**2 * _sl_q_35**2 / (q_int(3)*q_int(5))**2
_G_q_12 = math.pi**2 * _linking_q**2 / (_n2*q_int(9) * q_int(3)*q_int(5))
_det_G_q = _G_q_11 * _G_q_22 - _G_q_12**2

_kappa_gram = _det_G_cl / _det_G_q  # J² self-dual damping factor

ALPHA_EM_INV_DERIVED = _bare_alpha_inv * (1.0 + _c1 + _c1**2 * _kappa_gram)
# = 137.035944 (55 ppb, 0.00004% error)

# Canonical α_EM: the CS-corrected value is physical
alpha_em = 1.0 / ALPHA_EM_INV_DERIVED
alpha_em_derived = alpha_em  # alias for backward compatibility

# Knot volumes — single source of truth (knot_volumes module,
# mpmath 50dps Clausen / SnapPy HP). See PR #781 knot-vol
# propagation; pre-refactor these literals were duplicated here
# AND in mass_table_ppb / magic_A_formula / low_isotope_binding_sweep.
from knot_volumes import (  # noqa: E402
    CATALAN_G,
    VOL_BORROMEAN,
    VOL_4_1 as VOL_FIGURE8,  # legacy alias preserved
)
ALPHA_BORROMEAN = M_E_MEV * VOL_BORROMEAN          # binding scale for Borromean-like nuclei
ALPHA_FIGURE8 = M_E_MEV * VOL_FIGURE8             # binding scale for figure-8-like nuclei
ALPHA = ALPHA_BORROMEAN                             # default (backward compat)

# ── Electron traced volume V̂_e (mass-tower formula) ──────────────
# Trefoil σ³ on 2 strands (1 generator), 3 crossings (c=1, d=0).
# V̂_e = W_SYM×q³ + W_STD×V_std + W_ALT×(-1/q)³
# where V_std = z·a+b from transfer matrix T(1,0)³.
# This is the SAME V̂ that gives m_p/m_e = 1870 in the mass-tower.
# B(D) = α × V̂_e (deuteron binding = Borromean scale × electron action).
# Reference: prop:mass-endomorphism-tower
_a_e, _b_e = 0.0, 1.0
for _ in range(3):
    _a_e, _b_e = _a_e * h + _b_e, _a_e
V_HAT_ELECTRON = W_SYM * q0**3 + W_STD * (z * _a_e + _b_e) + W_ALT * (-qi)**3

# ── Knot classification and Wedderburn-Artin modification ────────
# Each NF basis element lives at a jet level determined by word length:
#   J⁰: γ (length 0) → unknot, Vol=0, CS=0
#   J¹: σ₀, σ₁ (length 1) → unknot, Vol=0, CS=0
#   J²: L₊, L₋ (length 2) → Hopf link, torus, CS=π²/6
#   J³: e⁻ (length 3) → trefoil T₂₃, torus, CS=π²/3
#
# FIGURE-EIGHT BW MODIFICATION (Wedderburn-Artin theorem):
# The figure-eight 4₁ = σ₀σ₁⁻¹σ₀⁻¹σ₁ has character in the standard
# representation of H₃(q):
#   χ(4₁, [2,1]) = 2 - [3]_q = -1 - h²
# while the Borromean B₃ = (σ₀σ₁⁻¹)³ has χ(B₃, [2,1]) ≈ 2 (near-identity).
#
# The BW formula decomposes into Z-independent (bulk) and Z-dependent parts.
# For figure-eight nuclei (A=3), the Wedderburn-Artin channel decomposition
# gives two algebraic scaling factors:
#   a = 1 - h² = 4 - [3]_q     (bulk: volume, surface, asymmetry, pairing)
#   f = h·[2]_q = q² - q⁻²     (Z-dependent: Coulomb, exchange)
#
# These arise from the figure-eight character:
#   a = 1 - (q-q⁻¹)² = 2q⁻¹(q+q⁻¹) - q² - q⁻² captures the
#     amphicheiral (self-mirror) property of 4₁
#   f = (q-q⁻¹)(q+q⁻¹) = q² - q⁻² is the 2-crossing Skein amplitude
#     for the net chirality seen by Z-dependent interactions
#
# Nuclear systems by knot type:
#   A=2 (D):    satellite (mixed) → use ALPHA_BORROMEAN × correction
#   A=3 (³H,³He): figure-eight-like → use figure-eight BW modification
#   A=4 (⁴He):  Borromean-like → use standard BW
#   A≥5:        Borromean-like → use standard BW

# Figure-eight BW scaling factors (from Wedderburn-Artin channel decomposition)
# Three factors, one per structural component:
FIG8_A_BULK = 1.0 - h**2                # = 4 - [3]_q ≈ 0.956 (bulk: vol, surf, asym)
FIG8_F_COUL = z**2 * q_int(3) / q_int(2) # = z²[3]/[2] ≈ 0.377 (Coulomb)
FIG8_F_EXCH = z                           # = 1/(√q+1/√q) ≈ 0.499 (exchange)
# Character ratios for higher-level corrections (4₁ vs B₃):
FIG8_R_311 = -2 * h**2 / (6 - 2 * h**2 + 6 * h**2)  # [3,1,1] ratio ≈ -0.015
FIG8_R_32  = (-1 - 2*h**2) / (5 - 2*h**2 + 5*h**2)   # [3,2] ratio ≈ -0.218
FIG8_R_41  = (1 - h**2) / (4 - h**2 + 4*h**2)          # [4,1] ratio ≈ 0.239

# Molecular energy scales (use corrected α)
E_HARTREE_EV = 511000.0 * alpha_em**2  # Hartree energy (eV)
TWO_Q = q0 + qi
E_MOL = E_HARTREE_EV / TWO_Q**2  # molecular energy unit (eV)
KAPPA = M_E_MEV                    # nuclear binding scale (MeV)

# ── q-hook product (symbolic) and (2,2) coefficient at k=4 ─────
# For partition λ ⊢ n the q-hook product is H_q(λ) = ∏_{x∈λ} [h_x(λ)]_q,
# where h_x is the hook length at cell x. The Wedderburn weight is
# w_λ = d_q(λ)² / [n]_q!  with d_q(λ) = [n]_q! / H_q(λ), so
# w_λ × H_q(λ)² = [n]_q!.

# ── q-combinatorics primitives (M2-inverted to pyhecke.wedderburn) ──
# Per PR #1085 carve-out + this PR (2b Phase B "M2 inversion"), the
# 8 canonical q-combinatorics functions now live in
# `tools/pyhecke/python/pyhecke/wedderburn.py`. Re-export them here so
# every existing `from hecke_core import partition_dimension` (etc.)
# in the 22+ external consumer scripts continues to work unchanged.
#
# pyhecke is on sys.path via the bootstrap block at lines 38-47
# (same path used for `from pyhecke.gram import ...` above).
from pyhecke.wedderburn import (  # noqa: E402
    q_hook_product,
    q_factorial,
    partitions_of,
    partition_dimension,
    partition_conjugate,
    partition_is_self_conjugate,
    q_dimension,
    wedderburn_weight,
)

# Lazy partition table — eager compute takes ~30 s (~20,000 partitions
# up to K_GAUSSIAN_MAX=15 with q_hook_product, wedderburn_weight, etc.
# per partition). Materialise on first access via the module-level
# `_partition_table()` accessor below. Most downstream scripts never
# touch this list (only jet / spectral analyses do), so gating behind
# a lazy call saves 30 s on every fresh python that imports hecke_core.

_PARTITION_TABLE_CACHE: list[dict] | None = None



# NF basis, trace weights, bond operators, hm, hm_exact, nf_tr, nf_net,
# _hm_dict, _reduce_nf, _build_gram, G, G_INV, and the exact-rational
# (_*_FRAC) constants have been moved to pyhecke.gram (M2b inversion).
# They are re-imported at the top of this file so every existing name
# remains accessible at module scope for downstream callers.

# Identity NF: the trivial braid [1, 0, 0, 0, 0, 0]
_ID_NF = np.array([1.0, 0, 0, 0, 0, 0])


def build_atom_nf_exact(Z, N):
    """Build atom NF using EXACT Fraction arithmetic.

    IDENTICAL algorithm to build_atom_nf but with Fraction arithmetic.
    Crossing order: per-nucleon (B₃ interleaved + quarks + inter-nucleon
    with all previous), then electrons. Matches build_atom_nf exactly.

    Reference: prop:atomic-braid-mass
    """
    A = Z + N
    if A == 0:
        return [Fraction(1), Fraction(0), Fraction(0),
                Fraction(0), Fraction(0), Fraction(0)]

    F0 = Fraction(0)
    F1 = Fraction(1)
    Fh = _H_FRAC
    Fh2 = Fh / 2

    # Ground-state ordering (same as build_atom_nf)
    ordering = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p'); pc += 1
        else:
            ordering.append('n'); nc += 1

    nf = [Fraction(0)] * 6
    nf[0] = Fraction(1)

    for k in range(A):
        if ordering[k] == 'p':
            for _ in range(3):
                nf = hm_exact(nf, F1, F0, 0)
                nf = hm_exact(nf, F1, -Fh, 1)
            # Quark: (0,1)=uu→σ₀, (0,2)=ud→mixed, (1,2)=ud→mixed
            nf = hm_exact(nf, F1, F0, 0)      # uu
            nf = hm_exact(nf, F1, -Fh2, 0)    # ud mixed
            nf = hm_exact(nf, F1, -Fh2, 1)    # ud mixed
            # Gluon: 2 σ₀
            nf = hm_exact(nf, F1, F0, 0)
            nf = hm_exact(nf, F1, F0, 0)
        else:
            for _ in range(3):
                nf = hm_exact(nf, F1, F0, 0)
                nf = hm_exact(nf, F1, -Fh, 1)
            # Quark: (0,1)=ud→mixed, (0,2)=ud→mixed, (1,2)=dd→σ⁻¹
            nf = hm_exact(nf, F1, -Fh2, 0)
            nf = hm_exact(nf, F1, -Fh2, 0)
            nf = hm_exact(nf, F1, -Fh, 1)
            # Gluon: 2 σ₀
            nf = hm_exact(nf, F1, F0, 0)
            nf = hm_exact(nf, F1, F0, 0)

        # Inter-nucleon with all PREVIOUS nucleons (on gen 0)
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == 'p' and tj == 'p':
                nf = hm_exact(nf, F1, F0, 0)
            elif ti == 'n' and tj == 'n':
                nf = hm_exact(nf, F1, -Fh, 0)
            else:
                nf = hm_exact(nf, F1, -Fh2, 0)

    # Electrons on gen 1
    for _ in range(Z):
        nf = hm_exact(nf, F1, -Fh, 1)

    return nf


def nf_channel_exact(nf_frac):
    """Exact per-channel characters from Fraction NF.

    Returns (χ_sym, χ_std, χ_alt, tr_M) as Fractions.
    """
    chi_sym = sum(c * e for c, e in zip(nf_frac, _SYM_EIG_FRAC))
    chi_alt = sum(c * e for c, e in zip(nf_frac, _ALT_EIG_FRAC))
    tr_M = sum(c * e for c, e in zip(nf_frac, _TR_M_FRAC))

    # Wedderburn weights (exact)
    q2 = _Q_FRAC ** 2
    D = q2**2 + 4*q2 + 1
    w_sym = q2 / D
    w_std = (q2 + 1)**2 / D
    w_alt = q2 / D

    chi_std = (tr_M - w_sym * chi_sym - w_alt * chi_alt) / w_std
    return chi_sym, chi_std, chi_alt, tr_M


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

    Construction:
      1. Build each nucleon via build_nucleon_nf (B₃ + quark crossings)
      2. Compose nucleons in ground-state interleaved order
      3. Apply inter-nucleon crossings between each pair (i,j):
           pp: σ₀           (c=1, d=0)    — EM repulsion
           nn: σ₀⁻¹         (c=1, d=-h)   — nuclear attraction
           pn: ½(σ₀+σ₀⁻¹)  (c=1, d=-h/2) — symmetric nuclear
      4. Apply pe crossings for electrons (σ₁⁻¹ per electron)

    No separate gluon dressing — B₃ IS the gluon structure.
    Generator 0 for inter-nucleon crossings (strong force channel).
    Generator 1 for pe crossings (EM channel).
    """
    A = Z + N
    if A == 0:
        return [1.0, 0, 0, 0, 0, 0]

    # Build ground-state ordering: interleaved protons and neutrons
    ordering = []  # 'p' or 'n'
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p')
            pc += 1
        else:
            ordering.append('n')
            nc += 1

    # Start with identity
    nf = [1.0, 0, 0, 0, 0, 0]

    # Compose nucleon NFs sequentially
    for k in range(A):
        if ordering[k] == 'p':
            # B₃ confinement (3 interleaved σ₀, σ₁⁻¹)
            for _ in range(3):
                nf = hm(nf, 1, 0, 0)       # σ₀
                nf = hm(nf, 1, -h, 1)       # σ₁⁻¹
            # Quark crossings: (0,1)=uu→σ₀, (0,2)=ud→mixed, (1,2)=ud→mixed
            nf = hm(nf, 1, 0, 0)            # pair(0,1) uu → σ₀
            nf = hm(nf, 1, -h/2, 0)         # pair(0,2) ud → σ₀ mixed
            nf = hm(nf, 1, -h/2, 1)         # pair(1,2) ud → σ₁ mixed
            # Gluon self-coupling: 2 σ₀ (ILP-derived, prop:mass-endomorphism-tower)
            nf = hm(nf, 1, 0, 0)            # gluon 1
            nf = hm(nf, 1, 0, 0)            # gluon 2
        else:
            # B₃ confinement
            for _ in range(3):
                nf = hm(nf, 1, 0, 0)       # σ₀
                nf = hm(nf, 1, -h, 1)       # σ₁⁻¹
            # Quark crossings: (0,1)=ud→mixed, (0,2)=ud→mixed, (1,2)=dd→σ⁻¹
            nf = hm(nf, 1, -h/2, 0)         # pair(0,1) ud → σ₀ mixed
            nf = hm(nf, 1, -h/2, 0)         # pair(0,2) ud → σ₀ mixed
            nf = hm(nf, 1, -h, 1)           # pair(1,2) dd → σ₁⁻¹
            # Gluon self-coupling: 2 σ₀ (same as proton)
            nf = hm(nf, 1, 0, 0)            # gluon 1
            nf = hm(nf, 1, 0, 0)            # gluon 2

        # Inter-nucleon crossing with all PREVIOUS nucleons
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == 'p' and tj == 'p':
                nf = hm(nf, 1, 0, 0)        # pp: σ₀
            elif ti == 'n' and tj == 'n':
                nf = hm(nf, 1, -h, 0)       # nn: σ₀⁻¹
            else:
                nf = hm(nf, 1, -h/2, 0)     # pn/np: mixed

    # Electrons: pe crossing (EM channel, gen=1)
    for _ in range(Z):
        nf = hm(nf, 1, -h, 1)               # σ₁⁻¹

    return nf


# ══════════════════════════════════════════════════════════════
# Per-generator vertex volumes (3-channel Wedderburn-Artin)
# ══════════════════════════════════════════════════════════════

def vertex_volume(chain):
    """3-channel Wedderburn-Artin vertex volume from crossing chain.

    Each crossing (c, d) acts on the three irrep channels of H₃(q):
      symmetric:  eigenvalue cq + d
      standard:   traced volume z·a + b (from 2×2 transfer matrix)
      alternating: eigenvalue -cq⁻¹ + d

    Full volume = W_sym × λ_sym + W_std × V_std + W_alt × λ_alt.
    """
    a, b = 0.0, 1.0
    sp, ap = 1.0, 1.0
    for c, d in chain:
        a, b = a*c*h + a*d + b*c, a*c + b*d
        sp *= c*q0 + d
        ap *= -c*qi + d
    V_std = z * a + b
    return W_SYM * sp + W_STD * V_std + W_ALT * ap


def nucleon_gen_chains(quarks):
    """Per-generator crossing chains for one nucleon.

    Derives chains from the quark content, matching build_nucleon_nf:
      B₃ = (σ₀σ₁⁻¹)³ contributes to both gen 0 and gen 1
      Quark pairs: (0,1)→gen=0, (0,2)→gen=0, (1,2)→gen=1

    Returns (g0_chain, g1_chain) as lists of (c, d) tuples.
    """
    # B₃ confinement: (σ₀·σ₁⁻¹)³
    # gen 0 gets 3× σ₀ = (1, 0)
    # gen 1 gets 3× σ₁⁻¹ = (1, -h)
    g0 = [(1, 0)] * 3
    g1 = [(1, -h)] * 3

    # Quark pairwise crossings
    pairs = [(0, 1, 0), (0, 2, 0), (1, 2, 1)]  # (qi, qj, gen)
    for i, j, gen in pairs:
        qi_f, qj_f = quarks[i], quarks[j]
        if qi_f == qj_f == 'u':
            cd = (1, 0)       # σ
        elif qi_f == qj_f == 'd':
            cd = (1, -h)      # σ⁻¹
        else:
            cd = (1, -h/2)    # mixed
        if gen == 0:
            g0.append(cd)
        else:
            g1.append(cd)

    # Gluon self-coupling: 2 σ₀ per nucleon (ILP-derived)
    g0.append((1, 0))
    g0.append((1, 0))

    return g0, g1


# Precomputed per-generator chains for proton and neutron
_PROTON_G0, _PROTON_G1 = nucleon_gen_chains(['u', 'u', 'd'])
_NEUTRON_G0, _NEUTRON_G1 = nucleon_gen_chains(['u', 'd', 'd'])


def atom_gen_chains(Z, N):
    """Per-generator crossing chains for atom (Z, N).

    Builds the complete atomic braid crossing chains for generators
    σ₀ and σ₁, including:
      1. Intra-nucleon crossings (B₃ + quark pairs) — from nucleon_gen_chains
      2. Inter-nucleon crossings between ALL nucleon pairs — on gen 0
      3. Electron crossings (pe) — on gen 1

    Nucleon ordering: pp...nn (protons first, then neutrons).

    Inter-nucleon crossings (strong force, gen 0):
      pp: (1, 0)     — positive crossing
      nn: (1, -h)    — inverse crossing
      pn: (1, -h/2)  — mixed crossing

    Returns (g0_chain, g1_chain).
    """
    g0, g1 = [], []

    # Build nucleon ordering (interleaved, matching build_atom_nf)
    A = Z + N
    ordering = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p')
            pc += 1
        else:
            ordering.append('n')
            nc += 1

    # 1. Nucleon crossings + inter-nucleon (matching build_atom_nf order)
    # Each nucleon's intra-nucleon crossings, then inter-nucleon with ALL previous
    for k in range(A):
        nuc_type = ordering[k]
        if nuc_type == 'p':
            g0.extend(_PROTON_G0)
            g1.extend(_PROTON_G1)
        else:
            g0.extend(_NEUTRON_G0)
            g1.extend(_NEUTRON_G1)

        # Inter-nucleon crossings with all previous nucleons (gen 0)
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == 'p' and tj == 'p':
                g0.append((1, 0))       # pp: σ₀
            elif ti == 'n' and tj == 'n':
                g0.append((1, -h))      # nn: σ₀⁻¹
            else:
                g0.append((1, -h / 2))  # pn: mixed

    # 2. Electron crossings: pe = σ⁻¹ on gen 1
    for _ in range(Z):
        g1.append((1, -h))

    return g0, g1


def atom_V_full(Z, N):
    """Quark-level per-generator V̂_i^full for the mass-tower formula.

    Uses atom_gen_chains to get the FULL braid (B₃ × quarks +
    inter-nucleon + electrons), then computes the Wedderburn-weighted
    traced volume per generator:

      V̂_i^full = w_sym·λ_sym + w_std·V_std + w_alt·λ_alt

    For H₃(q), i ∈ {0, 1} (two generators).

    Returns (V0_full, V1_full) as floats.

    Reference: prop:mass-endomorphism-tower, thm:wedderburn-mass-formula
    """
    g0_chain, g1_chain = atom_gen_chains(Z, N)
    return _chain_V_full(g0_chain), _chain_V_full(g1_chain)


def _chain_V_full(chain):
    """Wedderburn-weighted traced volume from a crossing chain.

    chain: list of (c, d) tuples.
    Returns V̂^full = w_sym·λ_sym + w_std·V_std + w_alt·λ_alt.
    """
    lam_sym = 1.0
    for c, d in chain:
        lam_sym *= c * q0 + d

    lam_alt = 1.0
    for c, d in chain:
        lam_alt *= -c * qi + d

    M00, M01, M10, M11 = 1.0, 0.0, 0.0, 1.0
    for c, d in chain:
        t00 = c * h + d; t01 = c; t10 = c; t11 = d
        n00 = M00*t00 + M01*t10; n01 = M00*t01 + M01*t11
        n10 = M10*t00 + M11*t10; n11 = M10*t01 + M11*t11
        M00, M01, M10, M11 = n00, n01, n10, n11
    V_std = z * M10 + M11  # second row: [a,b] = [0,1] × M → (M₁₀, M₁₁)

    return W_SYM * lam_sym + W_STD * V_std + W_ALT * lam_alt


# ══════════════════════════════════════════════════════════════
# Molecular binding
# ══════════════════════════════════════════════════════════════

NOBLE_GAS_Z = [2, 10, 18, 36, 54, 86]


def valence_Z(Z):
    """Number of valence electrons (Z minus largest noble gas core).

    Noble gas cores have saturated Frobenius channels (Gx >> 0,
    LP dual shadow price = 0). Only valence electrons participate
    in molecular binding.
    """
    core = 0
    for z_ng in NOBLE_GAS_Z:
        if z_ng < Z:
            core = z_ng
    return Z - core


def _vertex_channels(chain):
    """Return (λ_sym, V_std, λ_alt) for a crossing chain.

    Evaluates each Wedderburn-Artin irrep channel separately:
      symmetric: ∏(c·q + d)      (1-dim, eigenvalue q per positive crossing)
      standard:  z·M₀₀ + M₁₀    (2-dim, transfer matrix product)
      alternating: ∏(-c·q⁻¹ + d) (1-dim, eigenvalue -q⁻¹ per positive crossing)
    """
    a, b = 0.0, 1.0
    sp, ap = 1.0, 1.0
    for c, d in chain:
        a, b = a * c * h + a * d + b * c, a * c + b * d
        sp *= c * q0 + d
        ap *= -c * qi + d
    V_std = z * a + b
    return sp, V_std, ap


def molecular_binding_nf(Z_A, N_A, Z_B, N_B, n_inv_trefoils=1):
    """Molecular binding via full Wedderburn-Artin decomposition.

    Evaluates each irrep's Skein polynomial separately, then weights:
      Φ_λ = Σᵢ |Δln|P_λ,i||    (per-irrep, per-generator binding)
      E = (W_sym·Φ_sym + W_std·Φ_std + W_alt·Φ_alt) × E_MOL

    This is the correct representation-theoretic approach: the Hecke
    algebra decomposes as a direct sum H₃(q) ≅ V_sym ⊕ V_std² ⊕ V_alt,
    and the binding acts independently on each block. The Wedderburn
    weights w_λ = dim_q(λ)²/[3]_q! are the LP shadow prices from
    the Frobenius positivity constraint (PR #360).

    For H-H: 4.55 eV (exp 4.478, 1.7% error).
    Bond ratios correct: double = 2×single, triple = 3×single.

    Returns (E_eV, binding_phi, phi_ub, phi_bond).
    """
    g0A, g1A = atom_gen_chains(Z_A, N_A)
    g0B, g1B = atom_gen_chains(Z_B, N_B)

    bond_g0 = INV_TREFOIL_G0 * n_inv_trefoils
    bond_g1 = INV_TREFOIL_G1 * n_inv_trefoils

    total_bind = 0.0
    phi_ub = 0.0
    phi_bond = 0.0

    for gA, gB, bg in [(g0A, g0B, bond_g0), (g1A, g1B, bond_g1)]:
        s_ub, v_ub, a_ub = _vertex_channels(gA + gB)
        s_bd, v_bd, a_bd = _vertex_channels(gA + bg + gB)

        # Per-irrep absolute binding
        bind_s = abs(math.log(abs(s_ub)) - math.log(abs(s_bd))) if abs(s_ub * s_bd) > 1e-300 else 0
        bind_v = abs(math.log(abs(v_ub)) - math.log(abs(v_bd))) if abs(v_ub * v_bd) > 1e-300 else 0
        bind_a = abs(math.log(abs(a_ub)) - math.log(abs(a_bd))) if abs(a_ub * a_bd) > 1e-300 else 0

        total_bind += W_SYM * bind_s + W_STD * bind_v + W_ALT * bind_a

        # Track phi for diagnostics
        V_ub = W_SYM * s_ub + W_STD * v_ub + W_ALT * a_ub
        V_bd = W_SYM * s_bd + W_STD * v_bd + W_ALT * a_bd
        if abs(V_ub) > 1e-300:
            phi_ub += math.log(abs(V_ub))
        if abs(V_bd) > 1e-300:
            phi_bond += math.log(abs(V_bd))

    E_eV = total_bind * E_MOL

    return E_eV, total_bind, phi_ub, phi_bond


def molecular_binding_frobenius(Z_A, N_A, Z_B, N_B, n_inv_trefoils=1):
    """Molecular binding from the Frobenius bilinear form.

    E_bond = ½ |x_A^T · G · Δ · x_B| × E_MOL

    where Δ = (T⁻¹)^n - I is the bond operator perturbation,
    and the ½ comes from Δ being symmetric (the bilinear form
    counts each bond from both A and B perspectives).

    For H-H: E = 4.295 eV (exp 4.478, 4.1% error).

    This is mathematically equivalent to the vertex volume approach
    for the standard representation channel. For atoms where the
    full NF is Frobenius-unstable (A > 3 generally), this falls
    back to molecular_binding_nf which uses per-generator vertex
    volumes (the standard representation, avoiding the indefinite
    Gram matrix).

    Returns (E_eV, raw_pairing).
    """
    nf_A = build_atom_nf(Z_A, N_A)
    nf_B = build_atom_nf(Z_B, N_B)

    stable_A, _, _ = check_frobenius(nf_A)
    stable_B, _, _ = check_frobenius(nf_B)

    if not (stable_A and stable_B):
        E, bind, _, _ = molecular_binding_nf(Z_A, N_A, Z_B, N_B, n_inv_trefoils)
        return E, bind

    import numpy as np
    M_Tinv = np.zeros((6, 6))
    for j in range(6):
        ej = [0.0] * 6
        ej[j] = 1.0
        result = list(ej)
        for _ in range(n_inv_trefoils):
            result = hm(result, 1, -h, 0)
            result = hm(result, 1, -h, 1)
            result = hm(result, 1, -h, 0)
        M_Tinv[:, j] = result
    Delta = M_Tinv - np.eye(6)

    pairing = float(np.array(nf_A) @ G @ Delta @ np.array(nf_B))
    E_eV = abs(pairing) * E_MOL / 2  # ½ from symmetric Δ

    return E_eV, pairing / 2


# ══════════════════════════════════════════════════════════════
# Mass computation
# ══════════════════════════════════════════════════════════════

# ── Categorical shell closure from witnessed per-partition computation ──
# Replaces the Gaussian. Uses δ²_even from shell-closure.witness.json.
# The shell signal EMERGES from the Hoefsmit seminormal character
# computation at k=3..12. No empirical magic numbers, no Gaussian.
#
# Reference: prop:magic-numbers-from-q

import json as _json
from pathlib import Path as _Path


# ══════════════════════════════════════════════════════════════
# Jet-filtered LP-dual iterative accumulator (with checkpoints)
# ══════════════════════════════════════════════════════════════

import json as _json
import os as _os


def atom_per_generator_volumes(Z, N, include_inter=True, crossings_per_pair=1,
                                m_pp=None, m_pn=None, m_nn=None):
    """Per-generator additive Wedderburn volumes V̂_i^full for the atom braid.

    If m_pp, m_pn, m_nn are given (ILP solution), use them per pair type.
    Otherwise fall back to uniform crossings_per_pair.

    Returns a list of length n_strands - 1 = 3A - 1 (atom case) or
    n_strands - 1 = 2A (free case) of dicts:
        [{"std": Vs, "sym": sp, "alt": ap, "full": Vf}, ...]
    indexed by generator position i = 0, 1, ..., len-1.

    These are the V̂_i^full feeding the tower formula
    (prop:mass-endomorphism-tower):
        𝔪(W) = |Π V̂_i| + Σ Φ_q(|V̂_i|)
              + z² Σ_{|i-j|=1} Φ_q(|V̂_i V̂_j|).

    Implementation: replays _step_chain_generic for each nucleon, but
    instead of tracking a single accumulated YSN matrix, accumulates
    per-generator (a, b, sp, ap) — the additive Wedderburn channel
    state.  Mirrors mass_endomorphism.additive_wedderburn_volumes
    extended to A-nucleon atoms.

    Parameters
    ----------
    Z, N : int
        Proton and neutron counts.
    include_inter : bool
        If True: full atom braid with pp/nn/pn inter-nucleon crossings.
        If False: free disconnected-tensor baseline.

    Returns
    -------
    list of dict, one per generator.
    """
    A = Z + N
    if A < 1:
        return []

    # Nucleon ordering (Z protons then N neutrons) — matches
    # atom_character_raw convention.
    ordering = ['p'] * Z + ['n'] * N

    # n_gens for the joint braid
    if include_inter:
        n_strands = 3 * A
        n_gens_total = n_strands - 1  # 3A - 1
    else:
        # Free baseline: per-nucleon disjoint blocks of 2 generators each
        n_gens_total = 2 * A

    # Per-generator accumulators (a, b for std; sp for sym; ap for alt)
    a_arr  = [0.0] * n_gens_total
    b_arr  = [1.0] * n_gens_total
    sp_arr = [1.0] * n_gens_total
    ap_arr = [1.0] * n_gens_total

    # Build the atom braid by walking the nucleon chain.  For each
    # nucleon k, the intra-nucleon crossings live on local gens; for
    # the joint braid, these are mapped to global gens 3k, 3k+1.
    # Inter-nucleon crossings (when include_inter) live on gen 3k+2,
    # connecting nucleon k with nucleon k+1.
    for k, nuc in enumerate(ordering):
        intra    = _PROTON_G0 if nuc == 'p' else _NEUTRON_G0
        intra_g1 = _PROTON_G1 if nuc == 'p' else _NEUTRON_G1
        if include_inter:
            base_g0 = 3 * k       # global gen for first intra slot
            base_g1 = 3 * k + 1   # global gen for second intra slot
        else:
            base_g0 = 2 * k
            base_g1 = 2 * k + 1
        # Intra-nucleon, first generator slot
        for c, d in intra:
            i = base_g0
            a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
            b_new = a_arr[i] * c + b_arr[i] * d
            a_arr[i] = a_new
            b_arr[i] = b_new
            sp_arr[i] *= c * q0 + d
            ap_arr[i] *= -c * qi + d
        # Intra-nucleon, second generator slot
        for c, d in intra_g1:
            i = base_g1
            a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
            b_new = a_arr[i] * c + b_arr[i] * d
            a_arr[i] = a_new
            b_arr[i] = b_new
            sp_arr[i] *= c * q0 + d
            ap_arr[i] *= -c * qi + d
        # Inter-nucleon crossings (only when include_inter and k < A-1)
        # crossings_per_pair: number of repetitions of the basic pair
        # crossing.  For ILP-stable pairs, this should be derived from
        # Frobenius positivity (currently a parameter; see witness).
        if include_inter and k < A - 1:
            i = 3 * k + 2  # global gen for inter-nucleon between k and k+1
            next_nuc = ordering[k + 1]
            if nuc == 'p' and next_nuc == 'p':
                base_cross = (1.0, 0.0)      # pp: σ
                m_this = m_pp if m_pp is not None else crossings_per_pair
            elif nuc == 'n' and next_nuc == 'n':
                base_cross = (1.0, -h)       # nn: σ⁻¹
                m_this = m_nn if m_nn is not None else crossings_per_pair
            else:
                base_cross = (1.0, -h / 2)   # pn: ½(σ + σ⁻¹)
                m_this = m_pn if m_pn is not None else crossings_per_pair
            pair_cross = [base_cross] * m_this
            for c, d in pair_cross:
                a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
                b_new = a_arr[i] * c + b_arr[i] * d
                a_arr[i] = a_new
                b_arr[i] = b_new
                sp_arr[i] *= c * q0 + d
                ap_arr[i] *= -c * qi + d

    # Build per-generator V̂_full from accumulators
    z_mark = 1.0 / (q0 ** 0.5 + qi ** 0.5)
    # Wedderburn weights (H_3 weights — same as mass_endomorphism.py)
    nf3 = q_int(2) * q_int(3) * q_int(1)  # [3]_q!  (with [1]_q = 1)
    # Use H_3 weights as in mass_endomorphism (1-dim sym, 2-dim std, 1-dim alt)
    # W_sym, W_std, W_alt computed from quantum dimensions
    qdim_sym = 1.0
    qdim_std = q_int(2)
    qdim_alt = 1.0
    nf3_val = q_int(1) * q_int(2) * q_int(3)
    w_sym = qdim_sym ** 2 / nf3_val
    w_std = qdim_std ** 2 / nf3_val
    w_alt = qdim_alt ** 2 / nf3_val
    wt = w_sym + w_std + w_alt
    w_sym /= wt
    w_std /= wt
    w_alt /= wt

    vols = []
    for i in range(n_gens_total):
        Vs = z_mark * a_arr[i] + b_arr[i]
        Vf = w_sym * sp_arr[i] + w_std * Vs + w_alt * ap_arr[i]
        vols.append({"std": Vs, "sym": sp_arr[i], "alt": ap_arr[i], "full": Vf})
    return vols


from experimental_constants import (  # noqa: E402
    Q_NEUTRON_MEV as _Q_NEUTRON_MEV,
    Q_NEUTRON_MEV_ERR as _Q_NEUTRON_MEV_ERR,
)

# Free-neutron β-decay Q-value, derived from CODATA 2022:
#   Q_β(n) = m_n - m_p - m_e = 0.78233341 ± 6.1×10⁻⁷ MeV
# Authoritative source: experimental_constants.Q_NEUTRON_MEV (computed
# from CODATA mass constituents, not hardcoded). Audited by
# `e0_calibration_audit.py`.
E_0_CALIBRATION_MEV     = _Q_NEUTRON_MEV
E_0_CALIBRATION_MEV_ERR = _Q_NEUTRON_MEV_ERR


def build_nucleon_nf(quarks):
    """Build a single nucleon NF from quark content.

    quarks: list of 'u' or 'd' characters, e.g. ['u','u','d'] for proton.

    Construction: nucleon = B₃ · crossings(quarks)
    where B₃ = (σ₀σ₁⁻¹)³ is the gluon field (Borromean confinement),
    and crossings encode flavor:
      uu → σ_gen (c=1, d=0)
      dd → σ_gen⁻¹ (c=1, d=-h)
      ud → ½(σ_gen + σ_gen⁻¹) (c=1, d=-h/2)

    Generator assignment: pair (i,j) uses gen = i (the lower quark index).
    For 3 quarks: (0,1)→gen=0, (0,2)→gen=0, (1,2)→gen=1.

    No separate gluon dressing — B₃ IS the gluon structure.
    """
    nf = [1.0, 0, 0, 0, 0, 0]
    # B₃ confinement: (σ₀·σ₁⁻¹)³
    for _ in range(3):
        nf = hm(nf, 1, 0, 0)       # σ₀
        nf = hm(nf, 1, -h, 1)      # σ₁⁻¹
    # Quark pairwise crossings: (0,1), (0,2), (1,2)
    pairs = [(0, 1), (0, 2), (1, 2)]
    for i, j in pairs:
        qi, qj = quarks[i], quarks[j]
        gen = i  # generator = lower index
        if qi == qj == 'u':
            nf = hm(nf, 1, 0, gen)       # σ_gen
        elif qi == qj == 'd':
            nf = hm(nf, 1, -h, gen)      # σ_gen⁻¹
        else:  # mixed u-d
            nf = hm(nf, 1, -h/2, gen)    # ½(σ + σ⁻¹)
    return nf


# Precomputed nucleon NFs
PROTON_NF = build_nucleon_nf(['u', 'u', 'd'])
NEUTRON_NF = build_nucleon_nf(['u', 'd', 'd'])


# ════════════════════════════════════════════════════════════════════
# Back-compat re-exports for the Phase-5 EXPLORATORY surface.
# Per docs/audits/2026-05-24-hecke-core-canonical-audit.md, these
# symbols have been carved out into `_deprecated/hecke_core_legacy.py`.
# This block keeps `from hecke_core import X` working for every X that
# was historically defined in this file, so the carve-out is a no-op
# for external importers.
#
# New code should `from _deprecated.hecke_core_legacy import X` (or
# better: not use these symbols at all — they are not on the canonical
# derivation chain). Removing this block is a Phase-B follow-up that
# requires updating the ~5 external importers listed in the legacy
# file's docstring.
# ════════════════════════════════════════════════════════════════════
from _deprecated.hecke_core_legacy import (  # noqa: E402, F401
    DELTA_22,
    D_Q_22,
    H_Q_22,
    K_GAUSSIAN_MAX,
    K_PARTITION_MAX,
    MAGIC_NUMBERS,
    S_REEB_PLANCK,
    W_22,
    Y_22,
    _CATEGORICAL_SHELL,
    _CHEBYSHEV_MAGIC,
    _LazyPartitionTable,
    _M22_S1,
    _M22_S2,
    _M22_S3,
    _PARTITION_TABLE,
    _YSN_ATTACHED,
    _alternating_ordering,
    _bc_22,
    _build_ysn_matrices,
    _chain_M22,
    _chebyshev_magic,
    _content_at,
    _contrib_single_partition,
    _count_syts_by_12_relation,
    _crossing_M22,
    _crossing_coeff,
    _crossing_in_partition,
    _diag_T1,
    _diag_T2,
    _ensure_ysn_attached,
    _identity,
    _jet_witness_path,
    _load_categorical_shell,
    _matmul2,
    _matmul_dim,
    _n4_fac_22,
    _off_22,
    _partition_table,
    _phi1_from_ordering,
    _phi1_nuclear,
    _q_exp,
    _q_gaussian_character_approx,
    _standard_tableaux,
    _step_chain_22,
    _step_chain_generic,
    _swap_tab,
    _trace_dim,
    atom_character_raw,
    atom_frobenius_norm_sq,
    atom_markov_trace,
    atom_mass,
    binding_energy,
    binding_from_frobenius_pairing,
    classify_nuclear_knot,
    compute_phi1_full,
    conjugate_pair_cross_term,
    free_nucleon_frobenius_norm_sq,
    knot_factor,
    lp_shadow_price,
    magic_proximity,
    partition_character_sigma1,
    partition_jet_depth,
    partition_spectral_log_rate,
    q_laplacian_eigenvalue,
    q_resolvent_weight,
    q_value_beta,
    sdp_cross_channel_contribution,
    unified_iterative_correction,
    unified_iterative_correction_jet,
)
