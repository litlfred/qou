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
# Constants (non-Gram; M2-inverted to pyhecke.constants)
# ══════════════════════════════════════════════════════════════
#
# Per this PR (FINAL 2b Phase B M2 inversion), the α-EM derivation
# block + knot-volume scales + V_HAT_ELECTRON + FIG8 constants +
# molecular energy scales + E_0 calibration now live in
# `tools/pyhecke/python/pyhecke/constants.py`. Re-export them here
# so every existing `from hecke_core import alpha_em` (etc.) in
# external consumer scripts continues to work unchanged.
#
# After this PR, hecke_core.py is a pure back-compat shim — the
# canonical surface is 100% pyhecke-owned.
from pyhecke.constants import (  # noqa: E402
    q2,
    ALPHA_EM_INV_DERIVED, alpha_em, alpha_em_derived,
    ALPHA_BORROMEAN, ALPHA_FIGURE8, ALPHA,
    CATALAN_G, VOL_BORROMEAN, VOL_FIGURE8,
    V_HAT_ELECTRON,
    FIG8_A_BULK, FIG8_F_COUL, FIG8_F_EXCH,
    FIG8_R_311, FIG8_R_32, FIG8_R_41,
    E_HARTREE_EV, TWO_Q, E_MOL, KAPPA,
    M_E_MEV, M_P_MEV, M_N_MEV,
)

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


# E_0 calibration — M2-inverted to pyhecke.constants.
from pyhecke.constants import (  # noqa: E402
    E_0_CALIBRATION_MEV,
    E_0_CALIBRATION_MEV_ERR,
)


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
