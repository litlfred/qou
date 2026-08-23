
# Path bridge (subdirectory refactor — Phase 6, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
del _sys, _Path

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
    import sys as _sys
    from pathlib import Path as _PPath
    # SEARCH upward for the pyhecke checkout rather than counting `..`s. A
    # fixed count cannot be right for both layouts this file lives in:
    #   computations/substrate/hecke_core.py            -> tools/ is 2 up
    #   qou-mass/src/qou_mass/_internal/hecke_core.py   -> tools/ is 4 up
    # (the vendor sync copies this file verbatim into a flatter tree). The
    # hardcoded `../..` resolved to `qou-mass/src/tools/...` there, so
    # `is_dir()` was False and the fallback silently never fired in the
    # vendored layout -- masked in-repo because `_path_bridge` puts pyhecke
    # on sys.path first, and the sync STRIPS that import. Bean qou-rug0.
    _PYHECKE_PATH = None
    for _anc in _PPath(__file__).resolve().parents:
        _cand = _anc / "tools" / "pyhecke" / "python"
        if _cand.is_dir():
            _PYHECKE_PATH = str(_cand)
            break
    if _PYHECKE_PATH is not None and _PYHECKE_PATH not in _sys.path:
        _sys.path.insert(0, _PYHECKE_PATH)

from pyhecke.gram import (  # noqa: E402
    z, W_SYM, W_STD, W_ALT,
    NF_BASIS, NF_NAMES, TR_M,
    INV_TREFOIL_G0, INV_TREFOIL_G1,
    hm, hm_exact, nf_tr, nf_net,
    # `G_INV` is gone under convention D — the form is singular, so the 6x6
    # inverse does not exist. `G_PINV` is the inverse on the quotient
    # H_3(q)/rad, and `RADICAL` is the null direction it quotients by.
    G, G_PINV, RADICAL,
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
# Phase-B cycle break (2026-05-24).
#
# The Phase-5 EXPLORATORY surface (was the `from hecke_core_legacy
# import (...)` re-export block here) has been removed.  External
# consumers that still use the exploratory symbols import them
# directly from `hecke_core_legacy` now — see that module's top
# docstring for the full list and `docs/audits/
# 2026-05-24-hecke-core-canonical-audit.md` for the canonical-vs-
# exploratory classification.
#
# This module imports nothing from `hecke_core_legacy` — the import
# cycle documented in the legacy file's top docstring is fully broken.
# `hecke_core_legacy.py` still imports canonical symbols from
# `hecke_core` (one-way), which is safe because `hecke_core` is fully
# initialised by the time any consumer imports the legacy module.
#
# (hecke_core_legacy.py lived under `_deprecated/` until 2026-06-01;
#  it was moved one level up to match the existing DEPRECATION-CANDIDATE
#  convention used by the 23 other still-live deprecated scripts.)
# ════════════════════════════════════════════════════════════════════

# ── Back-compat aliases for mass_endomorphism consumers ──────────
w_sym = W_SYM
w_std = W_STD
w_alt = W_ALT

from functools import lru_cache  # noqa: E402


@lru_cache(maxsize=4096)
def Phi_q(z_val, max_k=2000):
    """Quantum dilogarithm Phi_q(z) = prod_{k>=1} (1 - q^{-k} z)^{-1} (float64)."""
    if abs(z_val) >= q0:
        return float("inf")
    product = 1.0
    qi_pow = qi
    for _ in range(max_k):
        term = qi_pow * z_val
        factor = 1.0 - term
        if abs(factor) < 1e-300:
            return float("inf")
        product /= factor
        if abs(term) < 1e-15:
            break
        qi_pow *= qi
    return product

