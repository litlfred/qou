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

# ── Atom-builder primitives (M2-inverted to pyhecke.atom) ──
# Per this PR (2b Phase B, stacked on #1118 + #1121), the 11 atom
# builder functions + 6 constants (_ID_NF, _PROTON_G0/G1,
# _NEUTRON_G0/G1, PROTON_NF, NEUTRON_NF) now live in
# `tools/pyhecke/python/pyhecke/atom.py`. Re-export them here so
# every existing `from hecke_core import build_atom_nf` (etc.) in
# external consumer scripts continues to work unchanged.
from pyhecke.atom import (  # noqa: E402
    _ID_NF,
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    PROTON_NF, NEUTRON_NF,
    build_atom_nf_exact, nf_channel_exact, check_frobenius,
    build_atom_nf, vertex_volume, nucleon_gen_chains,
    atom_gen_chains, atom_V_full, _chain_V_full,
    atom_per_generator_volumes, build_nucleon_nf,
)


# Lazy partition table — eager compute takes ~30 s (~20,000 partitions
# up to K_GAUSSIAN_MAX=15 with q_hook_product, wedderburn_weight, etc.
# per partition). Materialise on first access via the module-level
# `_partition_table()` accessor below. Most downstream scripts never
# touch this list (only jet / spectral analyses do), so gating behind
# a lazy call saves 30 s on every fresh python that imports hecke_core.

_PARTITION_TABLE_CACHE: list[dict] | None = None


# ══════════════════════════════════════════════════════════════
# Molecular binding
# ══════════════════════════════════════════════════════════════

# ── Molecular binding primitives (M2-inverted to pyhecke.molecular) ──
# Per this PR (2b Phase B "M2 inversion"), the 4 molecular binding
# functions + NOBLE_GAS_Z constant now live in
# `tools/pyhecke/python/pyhecke/molecular.py`. Re-export them here so
# every existing `from hecke_core import molecular_binding_nf` (etc.)
# in external consumer scripts continues to work unchanged. Same
# bootstrap path as wedderburn (pyhecke is on sys.path via the block
# at lines 38-47).
#
# Note: pyhecke.molecular still imports atom_gen_chains + build_atom_nf
# + check_frobenius from hecke_core (those atom-builder symbols are
# the next M2 inversion target).
from pyhecke.molecular import (  # noqa: E402
    NOBLE_GAS_Z,
    valence_Z,
    _vertex_channels,
    molecular_binding_nf,
    molecular_binding_frobenius,
)


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
