# DEPRECATION-CANDIDATE: Phase-5 exploratory surface, kept in place
# because 9 live importers (5 in folio-assistant/computations/ + 4 in
# tools/pyhecke/python/pyhecke/) still depend on its symbols. Revisit
# when the live importers are themselves retired or rewired to the
# canonical surface. Previously lived at _deprecated/hecke_core_legacy.py;
# moved out 2026-06-01 to match the existing 23-candidate convention
# (DEPRECATION-CANDIDATE banner in folio-assistant/computations/,
# not under _deprecated/).
"""hecke_core_legacy — Phase-5 EXPLORATORY surface of hecke_core.py.

Carved out per the canonical-vs-exploratory audit
(docs/audits/2026-05-24-hecke-core-canonical-audit.md).

Symbols here are NOT on the canonical derivation chain
(docs/canonical-derivation-cheat-sheet.md). They are kept for
reproducibility of historical Phase-5 results and for the
in-repo consumers that still import them.

**Direct importers** (folio-assistant/computations/):

  - sdp_cross_channel.py                  (_PARTITION_TABLE, _build_ysn_matrices,
                                            _content_at, _crossing_in_partition,
                                            _identity, _matmul_dim, _standard_tableaux,
                                            _step_chain_generic, _swap_tab,
                                            _trace_dim, atom_character_raw,
                                            lp_shadow_price, partition_jet_depth)
  - atomic_chirality_residue.py           (_step_chain_generic)
  - hadron_knot_table.py                  (binding_energy, classify_nuclear_knot)
  - phase3_triton_binding_convention_b.py (binding_from_frobenius_pairing)

**pyhecke delegation modules** (tools/pyhecke/python/pyhecke/, via the
sys.path bridge in `_legacy.py`):

  - pyhecke/partition.py  (lp_shadow_price, q_laplacian_eigenvalue,
                           q_resolvent_weight, partition_character_sigma1,
                           partition_spectral_log_rate)
  - pyhecke/trace.py      (atom_character_raw)
  - pyhecke/tower.py      (knot_factor)

For new code, use the canonical surface in `hecke_core.py` or the
matching pyhecke modules (gram, wedderburn, atom, molecular) instead.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
# ── Stdlib imports the moved code uses ──
# These were originally at hecke_core.py module-top (lines 1420-1421,
# 2233-2234). When the carve-out split the file, the moved functions
# (`unified_iterative_correction*`, `_jet_witness_path`,
# `_load_categorical_shell`) still reference them — so they live here
# now. All unconditional — function-call-time NameError if a function
# is called without the import being available (caught by PR #1085
# review).
import math
import json as _json
import os as _os
import sys as _sys
from pathlib import Path as _Path
from fractions import Fraction
import numpy as np

from q_parameter import Q as q0, Q_INV as qi, HA as h, q_int, E_CROSS

# pyhecke bootstrap (mirrors hecke_core.py) — note `_os` and `_sys`
# are already imported above unconditionally; this block only fixes
# sys.path if pyhecke isn't installed.
try:
    import pyhecke.gram as _probe  # noqa: F401
except ImportError:
    _PYHECKE_PATH = _os.path.normpath(
        _os.path.join(_os.path.dirname(__file__), "..", "..", "..", "tools", "pyhecke", "python")
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
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

# Module-level cache for `_partition_table` — was at hecke_core.py
# line 560 in the original; the carve-out missed it because the
# AST-driven script's LEGACY_CONSTANTS set listed only `_PARTITION_TABLE`
# (the lazy proxy), not its underlying cache. NameError on the first
# call to `_partition_table()` without this. Caught by PR #1085 review.
_PARTITION_TABLE_CACHE: list[dict] | None = None

# ── Canonical-surface imports ──
# This block MUST stay near the top of the file, before any module-level
# statement that evaluates a canonical function (e.g. the
# `H_Q_22 = q_hook_product((2, 2))` line below). Moving the import to
# the bottom would NameError at module load.
#
# Phase B cycle break (2026-05-24): the back-compat re-export block
# at the bottom of `hecke_core.py` has been REMOVED. The four downstream
# consumers that previously imported legacy symbols via `hecke_core`
# (sdp_cross_channel.py, atomic_chirality_residue.py, hadron_knot_table.py,
# phase3_triton_binding_convention_b.py) now import directly from
# `hecke_core_legacy`.
#
# Import direction is now one-way only:
#   `hecke_core_legacy` → `hecke_core` (canonical primitives)
#   `hecke_core` does NOT import from `hecke_core_legacy`.
#
# Direct imports `from hecke_core_legacy import X` are now safe —
# hecke_core is imported fresh, completes its initialisation (no
# recursion back into legacy), and legacy's `from hecke_core import
# (...)` block finds the canonical surface fully populated.
#
# (Path note: until 2026-06-01 this module lived at
#  `_deprecated/hecke_core_legacy.py`; importers used
#  `from _deprecated.hecke_core_legacy import X`. The file moved one
#  level up to match the DEPRECATION-CANDIDATE banner convention used
#  by the other 23 still-live deprecated scripts.)
#
# **Recommendation for new code**: do NOT import from this module.
# The exploratory surface is being deprecated in favour of the
# canonical chain in `hecke_core.py` + `pyhecke/`. See
# `docs/audits/2026-05-24-hecke-core-canonical-audit.md` for the
# canonical/exploratory classification.
from hecke_core import (  # noqa: E402
    # q-combinatorics seed
    q_factorial, q_hook_product, partitions_of, partition_dimension,
    partition_conjugate, partition_is_self_conjugate, q_dimension,
    wedderburn_weight,
    # NF + atom construction
    build_atom_nf_exact, nf_channel_exact, check_frobenius,
    build_atom_nf, vertex_volume, nucleon_gen_chains,
    _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
    atom_gen_chains, atom_V_full, _chain_V_full,
    # Molecular binding
    _vertex_channels, molecular_binding_nf, molecular_binding_frobenius,
    valence_Z,
    # Mass-tower
    atom_per_generator_volumes, build_nucleon_nf,
    PROTON_NF, NEUTRON_NF,
    # Cached / scalar constants the legacy code still references
    _ID_NF,
    q2,
    ALPHA_EM_INV_DERIVED, alpha_em, alpha_em_derived,
    ALPHA_BORROMEAN, ALPHA_FIGURE8, ALPHA,
    V_HAT_ELECTRON,
    FIG8_A_BULK, FIG8_F_COUL, FIG8_F_EXCH, FIG8_R_311, FIG8_R_32, FIG8_R_41,
    E_HARTREE_EV, TWO_Q, E_MOL, KAPPA,
    NOBLE_GAS_Z,
    E_0_CALIBRATION_MEV, E_0_CALIBRATION_MEV_ERR,
    CATALAN_G, VOL_BORROMEAN, VOL_FIGURE8,
)

# ════════════════════════════════════════════════════════════════════
# MOVED SYMBOLS — original source preserved verbatim from hecke_core.py
# ════════════════════════════════════════════════════════════════════



def classify_nuclear_knot(Z, N):
    """Classify the nuclear braid's knot type and return binding scale.

    Returns: (alpha_scale, knot_name, is_hyperbolic)
    """
    A = Z + N
    if A <= 1:
        return ALPHA_BORROMEAN, 'trivial', False
    elif A == 2:
        return ALPHA_BORROMEAN, 'satellite', False
    elif A == 3:
        return ALPHA_FIGURE8, 'figure-eight', True
    else:
        return ALPHA_BORROMEAN, 'Borromean', True


def partition_jet_depth(partition):
    """Jet depth of a Young diagram: max |content(□)| = max(λ_1 − 1, λ_1^T − 1).

    The content c(□) = col − row measures the diagonal distance of
    a cell.  The maximum |c| over cells equals the larger of
    (width − 1, height − 1), giving a conjugation-symmetric
    measure of "diagonal reach".

    Jet filtration correspondence:
      jet = 0: only (1) and empty — trivial, no braid structure
      jet = 1: (2), (1,1), (2,1), (2,2), (2,2,1), (2,1,1), ...
               — partitions fitting in a 2-column-or-2-row rectangle
               — "Hopf-like" complexity (J¹-J² in braid-length terms)
      jet = 2: adds (3), (3,1), (3,2), (3,1,1), (3,2,1), (3,3,1), ...
               — fits in 3-column-or-3-row rectangle
               — "trefoil-like" complexity (J³)
      ...

    This gives a DISCRETE hierarchy complementary to the continuous
    k-level partition enumeration: jet j ⊂ jet j+1.
    """
    if not partition:
        return 0
    width = partition[0]
    height = len(partition)
    return max(width - 1, height - 1)


def q_laplacian_eigenvalue(partition):
    """q-Laplacian eigenvalue on the λ-block of the Wedderburn
    decomposition (prop:q-heat-kernel-peter-weyl, def:q-heat-equation).

    From the Peter-Weyl spectral decomposition of the q-heat kernel
    (merged PR #368, prop:q-heat-kernel-peter-weyl):

        μ_λ(q) = ℏ_q² × Σ_{□ ∈ λ} [c(□)]_q × [c(□) + 1]_q

    where c(□) = col − row is the content of cell □, [k]_q is the
    symmetric q-integer, and ℏ_q = (q−1)/q is the quantum Planck
    constant.  This is the eigenvalue of the pure-spin piece
    (1 − q⁻¹)²Δ_ξ from the q-Laplacian three-term expansion
    (rem:q-laplacian-expansion); the classical-core piece q⁻²Δ acts
    on spatial modes and doesn't depend on λ, and Coriolis cross-terms
    vanish on Hecke-representation spaces by Schur's lemma.

    Derived via Jucys-Murphy q-Casimir (Ram's q-deformation):
    L_i · T = [c(T,i)]_q · T on SYTs; the Casimir sum
    Σ [c]_q[c+1]_q is the q-analogue of j(j+1) from the
    SU_q(2) representation (def:q-angular-momentum).

    Base-ring independent: formula is polynomial in q, q⁻¹ with
    integer coefficients, valid over any ring where q − 1 invertible.
    """
    lam = list(partition)
    if not lam:
        return 0.0
    # Jucys-Murphy Casimir: Σ [c]_q[c+1]_q (bare, no ℏ_q² prefactor).
    # The ℏ_q² = ((q−1)/q)² is the conversion factor to the SPIN piece
    # of the q-Laplacian (Δ_ξ eigenvalue = ℏ_q² × JM Casimir).  For
    # the Hecke algebra LP-dual problem, the bare JM Casimir is the
    # correct spectral operator — it measures the TOTAL partition
    # content including both spatial and spin pieces via the Jucys-Murphy
    # representation of the centre of H_n(q).
    casimir_sum = 0.0
    for i, li in enumerate(lam):
        for j in range(li):
            c = j - i
            casimir_sum += q_int(c) * q_int(c + 1)
    return casimir_sum


def q_resolvent_weight(partition, s=None):
    """Resolvent weight 1 / (μ_λ + s_*) derived from the q-Laplacian
    spectrum (def:categorical-laplace-transform).

    The categorical Laplace transform of the q-heat equation
    (def:q-heat-equation) gives ℒ[u](s) = (Δ̂_q + s)⁻¹ u_0 — the
    resolvent of the q-Laplacian.  On each λ-block this acts by a
    scalar:

        ρ_λ(s) = 1 / (μ_λ + s)

    where s is the spectral parameter conjugate to the Reeb-flow
    time t.  A canonical choice is the Planck step t_P(q) = q/(q−1)
    (def:q-heat-equation §"units of the Planck step"); then
    s_* = 1/t_P(q) = (q−1)/q has base-ring independent meaning
    (rem:substrate-radial-coordinate).

    This resolvent damping replaces the ad-hoc Kerov Plancherel
    multiplier: it is DERIVED from the q-heat spectrum rather than
    assumed from the q-hook walk's stationary measure.
    """
    if s is None:
        # Default: Planck-step Reeb time scale s_* = (q − 1) / q
        s = (q0 - 1.0) / q0
    mu = q_laplacian_eigenvalue(partition)
    return 1.0 / (mu + s)


def lp_shadow_price(partition):
    """LP-dual shadow price y_λ for the Frobenius positivity constraint
    of partition λ in the operator-selection LP at level k = |λ|.

    From prop:mass-coefficient-shadow-price:

        y_λ = w_λ / d_λ − y_0

    where y_0 = min_λ (w_λ / d_λ) = 1/[k]_q! is the dual variable of the
    normalisation constraint 1ᵀx = n_target, and d_λ = dim(λ) is the
    classical dimension (number of standard Young tableaux).

    The shadow price y_λ multiplies the categorical scale C_λ = m_e ·
    H_q(λ) to produce a per-partition binding contribution
    Δ B_λ = y_λ · C_λ · S_λ(Z, N, A) (BW formula factorisation).

    Reference: prop:mass-coefficient-shadow-price.
    """
    k = sum(partition)
    if k == 0:
        return 0.0
    w = wedderburn_weight(partition)
    d = partition_dimension(partition)
    # y_0 is the smallest of w_λ/d_λ across all partitions of k.
    # For the trivial (n) partition (sym): w = 1/[n]_q!, d = 1.
    # So y_0 = 1/[n]_q! (the LP normalisation dual).
    y_0 = 1.0 / q_factorial(k)
    return w / d - y_0


# Pre-compute all partitions of k = 2..K_PARTITION_MAX with q-hook,
# weight, dimension, shadow price.  K = 6 covers H₂..H₆ (24 partitions
# in total: 2 + 3 + 5 + 7 + 11) — enough to host every Wedderburn
# channel that contributes a BW term in the dedicated formulation
# (volume, surface, Coulomb, asymmetry, pairing, exchange, shell,
# hook, Wigner, form factor, pn correlation, [3,2,1] pn-invisible,
# [4,1,1]+[3,1,1,1] isospin, [4,2]+[2,2,1,1] codim-4 form factor).
# K_PARTITION_MAX is capped at 8 because empirical sweeps show the
# Empirical sweep with q-heat resolvent damping (post-PR #368) shows
# K = 6 is the OPTIMAL partition cutoff — extending to k = 7, 8, 9
# introduces sub-leading spectral modes that degrade accuracy (e.g.
# 40Ca: 0.001 at K=6 → 0.012 at K=9).  K = 3 is also very strong for
# light atoms.  The resolvent's built-in damping envelope does not
# benefit from further partitions — q-heat already absorbs higher-k
# contributions via (μ_λ + s)⁻¹ decay.
K_PARTITION_MAX = 11
# Metadata-only partitions reach up to K_GAUSSIAN_MAX for the
# q-Gaussian fallback (no YSN matrices built — just d_q, shadow_price,
# q_hook, Wedderburn weight which are cheap to compute for any k).
K_GAUSSIAN_MAX = 15

def _count_syts_by_12_relation(partition):
    """Count SYTs of shape λ by the position of the value 2 relative
    to 1: same row, same column, or neither (→ part of a 2×2 mixing
    block in YSN).  Returns (n_row, n_col, n_mix_pairs) where each
    mixing pair contributes 2 SYTs so n_row + n_col + 2·n_mix_pairs = d(λ).
    """
    n = sum(partition)
    if n < 2:
        return (0, 0, 0)
    shape = list(partition)
    counts = [0, 0, 0]  # row, col, mix

    def fill(tab, val, rem):
        if val > n:
            pos_1 = pos_2 = None
            for r, row in enumerate(tab):
                for c, v in enumerate(row):
                    if v == 1: pos_1 = (r, c)
                    if v == 2: pos_2 = (r, c)
            if pos_1[0] == pos_2[0]:
                counts[0] += 1
            elif pos_1[1] == pos_2[1]:
                counts[1] += 1
            else:
                counts[2] += 1
            return
        for r in range(len(shape)):
            if rem[r] == 0:
                continue
            col = len(tab[r])
            if r > 0 and col >= len(tab[r-1]):
                continue
            tab[r].append(val)
            rem[r] -= 1
            fill(tab, val + 1, rem)
            tab[r].pop()
            rem[r] += 1

    fill([[] for _ in shape], 1, list(shape))
    # Mixing tableaux come in pairs (T and its (1↔2)-swap)
    return (counts[0], counts[1], counts[2] // 2)


def partition_character_sigma1(partition):
    """Character χ_λ(σ_1) of the first Hecke generator in irrep λ.

    Derived from YSN eigenvalue structure:
        χ_λ(σ_1) = q · n_row + (-q⁻¹) · n_col + h · n_mix_pairs
    where n_row / n_col / n_mix_pairs are SYT counts by (1,2)-relation.
    """
    nr, nc, nm = _count_syts_by_12_relation(partition)
    return q0 * nr + (-qi) * nc + h * nm


def partition_spectral_log_rate(partition):
    """Average per-crossing log spectral rate for partition λ:
        ρ_λ = |χ_λ(σ_1)| / d(λ).
    The log of this, ln ρ_λ, is the LEADING rate at which a random
    braid word's trace in λ accumulates: ln|Tr M_λ(W_N)| ≈ ln d(λ) + N ln ρ_λ.
    (For partitions where ρ_λ < 1, the character ratio is less than
    unity and the trace shrinks exponentially — consistent with the
    partition being "far from the mean" in the Plancherel sense.)
    """
    d = partition_dimension(partition)
    if d == 0:
        return 0.0
    chi = partition_character_sigma1(partition)
    ratio = abs(chi) / d
    return math.log(ratio) if ratio > 0 else 0.0


# Canonical Reeb-time spectral parameter s_*.
# The Peter-Weyl formula (prop:q-heat-kernel-peter-weyl) gives
# u(t) = Σ d_λ exp(−μ_λ t) π_λ(u₀), and its Laplace transform
# ℒ[u](s) = Σ d_λ (μ_λ + s)⁻¹ π_λ(u₀) is the resolvent.
# The natural spectral parameter for the nuclear binding problem
# is s_* = (q−1)/q = ℏ_q (the quantum Planck constant), which is
# the natural scale at which the JM Casimir (μ_λ ∈ [2, 190] for
# k ≤ 9) provides O(1)–O(0.005) differentiation across the
# partition spectrum via ρ_λ = 1/(μ_λ + s_*).
S_REEB_PLANCK = (q0 - 1.0) / q0


def _partition_table() -> list[dict]:
    """Materialise _PARTITION_TABLE_CACHE on first access. ~30 s cold."""
    global _PARTITION_TABLE_CACHE
    if _PARTITION_TABLE_CACHE is not None:
        return _PARTITION_TABLE_CACHE
    table: list[dict] = []
    for _k in range(2, K_GAUSSIAN_MAX + 1):
        for _lam in partitions_of(_k):
            _Hq = q_hook_product(_lam)
            _w = wedderburn_weight(_lam)
            _d = partition_dimension(_lam)
            _y = lp_shadow_price(_lam)
            _kerov_scale = _w * _y * _Hq * M_E_MEV
            # Per-partition average log spectral rate (Perron-Frobenius proxy)
            _chi = partition_character_sigma1(_lam)
            _rho = abs(_chi) / _d if _d > 0 else 0.0
            _log_rho = math.log(_rho) if _rho > 1e-300 else -30.0
            # q-Laplacian eigenvalue and resolvent weight (def:q-heat-equation,
            # def:categorical-laplace-transform): categorical damping derived
            # from the q-heat spectrum rather than the Kerov Plancherel measure.
            _mu = q_laplacian_eigenvalue(_lam)
            _resolvent = 1.0 / (_mu + S_REEB_PLANCK) if (_mu + S_REEB_PLANCK) > 0 else 0.0
            # Resolvent-damped scale: m_e · H_q(λ) · y_λ · ρ_λ(s_*).
            # Replaces the ad-hoc Kerov multiplier w_λ with the categorically
            # derived resolvent of the q-Laplacian at Planck-step Reeb time.
            _resolvent_scale = _Hq * _y * _resolvent * M_E_MEV
            table.append({
                'partition': _lam,
                'k': _k,
                'jet': partition_jet_depth(_lam),
                'q_hook': _Hq,
                'wedderburn_weight': _w,
                'dim': _d,
                'shadow_price': _y,
                'kerov_plancherel': _w,
                'C_lambda_MeV': _Hq * M_E_MEV,
                'C_lambda_kerov_MeV': _kerov_scale,
                'chi_sigma1': _chi,
                'spectral_log_rate': _log_rho,
                'q_laplacian_eigenvalue': _mu,
                'resolvent_weight_planck': _resolvent,
                'C_lambda_resolvent_MeV': _resolvent_scale,
                # YSN matrices built only for k ≤ K_PARTITION_MAX.
                # For higher k, q-Gaussian fallback uses the metadata above.
                'has_ysn': _k <= K_PARTITION_MAX,
            })
    _PARTITION_TABLE_CACHE = table
    return table


class _LazyPartitionTable:
    """List-shaped proxy that materialises the partition table + its
    YSN matrices on first iteration / indexing / len. Keeps every
    existing `for e in _PARTITION_TABLE:` / `_PARTITION_TABLE[i]` /
    comprehension working unchanged — but pays the ~60 s cost only
    on first touch instead of unconditionally at module import.
    """

    __slots__ = ()

    def _data(self):
        # Lazy: build the base table, then attach YSN matrices once.
        _ensure_ysn_attached()
        return _partition_table()

    def __iter__(self):
        return iter(self._data())

    def __len__(self):
        return len(self._data())

    def __getitem__(self, key):
        return self._data()[key]

    def __contains__(self, item):
        return item in self._data()

    def __repr__(self):
        if _PARTITION_TABLE_CACHE is None:
            return "_LazyPartitionTable(<not yet materialised>)"
        return f"_LazyPartitionTable({len(_PARTITION_TABLE_CACHE)} entries)"


_PARTITION_TABLE = _LazyPartitionTable()

# (2,2) hook product = [3]·[2]²·[1] = [3]·[2]²
H_Q_22 = q_hook_product((2, 2))                   # = [3]·[2]² ≈ 12.31
DELTA_22 = H_Q_22 * M_E_MEV                       # = [3]·[2]²·m_e ≈ 6.29 MeV
# Wedderburn weight of (2,2): w = d_q²/[4]_q! where d_q = [4]_q!/H_q
_n4_fac_22 = q_int(2) * q_int(3) * q_int(4)       # [4]_q!
D_Q_22 = _n4_fac_22 / H_Q_22                       # d_q((2,2)) = [4]_q!/H_q ≈ 2.044
W_22 = D_Q_22**2 / _n4_fac_22                      # w_{(2,2)} = d_q²/[4]_q! ≈ 0.166
Y_22 = lp_shadow_price((2, 2))                     # LP-dual shadow price of (2,2)


def _q_exp(x, n_terms=20):
    """q-exponential exp_q(x) = Σ x^n / [n]_q!. Fully symbolic in q."""
    result = 1.0
    term = 1.0
    for n in range(1, n_terms + 1):
        term *= x / q_int(n)
        result += term
        if abs(term) < 1e-15:
            break
    return result


def _chebyshev_magic(max_z=150):
    """Derive magic number positions from Chebyshev recurrence in q.

    (σ⁻¹)^Z = c_Z·σ + d_Z where σ⁻¹ = σ - h.
    Recurrence: c_{n+1} = d_n, d_{n+1} = c_n - d_n·h.
    Magic Z = where γ(Z) = |c_Z/c_{Z-1}| has a LOCAL MINIMUM
    among even-Z values (extra pairing stability).

    All coefficients are polynomials in h = q - q⁻¹.
    """
    c, d = 0.0, 1.0
    prev_c = 1.0
    even_gammas = {}
    for Z in range(1, max_z + 1):
        c_new = d
        d_new = c - d * h
        c, d = c_new, d_new
        g = abs(c / prev_c) if abs(prev_c) > 1e-300 else 1.0
        if Z % 2 == 0:
            even_gammas[Z] = g
        prev_c = c

    # Magic = local minima of γ among even Z
    magic = set()
    even_zs = sorted(even_gammas.keys())
    for i in range(1, len(even_zs) - 1):
        z = even_zs[i]
        if (even_gammas[z] < even_gammas[even_zs[i-1]] and
                even_gammas[z] < even_gammas[even_zs[i+1]]):
            magic.add(z)
    # Z=2 is always magic (strongest pairing)
    magic.add(2)
    return sorted(magic)


# Chebyshev recurrence at k=2 derives {2, 8} from substrate q_0 alone.
_CHEBYSHEV_MAGIC = _chebyshev_magic()
# EMPIRICAL: {20, 28, 50, 82, 126} are the standard nuclear shell
# closures [mayer1949, satula1997]. They are NOT derived from the
# Chebyshev recurrence — they are imported from experimental nuclear
# data. The k=7 "binding trend break" confirmation is a consistency
# check, not a derivation. Per CAL-4 discipline: these values are
# CODATA-class inputs, not canonical predictions.
MAGIC_NUMBERS = [2, 8, 20, 28, 50, 82, 126]


def knot_factor(Z, N):
    """Per-nucleus knot factor from Frobenius norm deviation.

    a(N) = ∏(1 - εᵢ) where εᵢ is the Frobenius norm deviation
    per nucleon pair.

    A=2: dedicated (D uses mass-tower B=α×V̂_e, handled in binding_energy)
    A=3: 1-h² (figure-eight amphicheiral, from Fricke relation)
    A=4: (1-h²)² (double amphicheiral)
    A≥5: 1.0 (generic BW)

    The per-level character ratio (nucleus/free-nucleon product)
    and confined-state accumulation provide the categorical
    derivation path. Currently using the product formula for A≤4
    and generic for A≥5.

    Reference: prop:nuclear-knot-classification, prop:confined-knot-binding
    """
    A = Z + N
    if A <= 1: return 1.0
    elif A == 2: return 1.0  # D handled by dedicated formula in binding_energy
    elif A == 3: return 1.0 - h**2
    elif A == 4: return (1.0 - h**2)**2
    return 1.0


def _crossing_coeff(ti, tj):
    """Crossing coefficient d for strand pair (ti, tj). c=1 always.
    Returns None for identity crossings (ne)."""
    if ti == 'p' and tj == 'p': return 0.0
    if ti == 'n' and tj == 'n': return -h
    if (ti, tj) in (('p','n'), ('n','p')): return -h/2
    if (ti, tj) in (('p','e'), ('e','p')): return -h
    if ti == 'e' and tj == 'e': return 0.0
    return None  # ne: identity


def _phi1_from_ordering(ordering):
    """Compute Φ₁ = Σᵢ ln|V̂ᵢ| for a given strand ordering.

    Each strand i has a traced volume V̂ᵢ = z·M₀₀ + M₁₀ computed
    from the 2×2 transfer matrix product M = ∏ⱼ T(cⱼ, dⱼ) for all
    crossings with strands j > i.

    T(c,d) = [[c·h + d, c], [c, d]]  (Hecke transfer matrix)
    V̂ᵢ = z·M[0][0] + M[1][0]       (Markov-traced volume)
    """
    n = len(ordering)
    if n <= 1:
        return 0.0
    phi = 0.0
    for i in range(n - 1):
        # 2×2 transfer matrix product (start with identity)
        M00, M01, M10, M11 = 1.0, 0.0, 0.0, 1.0
        for j in range(i + 1, n):
            d = _crossing_coeff(ordering[i], ordering[j])
            if d is None:
                continue
            # T = [[h+d, 1], [1, d]]  (c=1 always)
            t00, t01, t10, t11 = h + d, 1.0, 1.0, d
            # M = M × T
            n00 = M00*t00 + M01*t10
            n01 = M00*t01 + M01*t11
            n10 = M10*t00 + M11*t10
            n11 = M10*t01 + M11*t11
            M00, M01, M10, M11 = n00, n01, n10, n11
        V = z * M10 + M11  # second row: [a,b]=[0,1]×M → (M₁₀, M₁₁)
        if abs(V) > 1e-300:
            phi += math.log(abs(V))
    return phi


def _alternating_ordering(Z, N):
    """Alternating nucleon ordering: p,n,p,n,... with extras at end.

    This is the ground-state seed used by braid-registry.py and matches
    the exhaustive search results for A≤15.
    """
    ordering = []
    pi, ni = 0, 0
    for k in range(Z + N):
        if pi < Z and (ni >= N or k % 2 == 0):
            ordering.append('p')
            pi += 1
        else:
            ordering.append('n')
            ni += 1
    return ordering


def _phi1_nuclear(Z, N):
    """Compute Φ₁ on nuclear strands only (no electrons).

    Uses alternating (pnpn...) ordering which matches the braid-registry
    ground-state search results. For A>14, tries ordering cache / Rust
    engine for optimized ordering.

    Justified by LP dual: electron channels are saturated in neutral
    atoms (shadow price = 0), so they don't contribute to the mass
    *difference*. The electron mass is in Δ_Mfree, not Φ₁.
    """
    A = Z + N
    if A <= 1:
        return 0.0

    # ── A=2 (Deuterium): dedicated formula ────────────────────
    # B(D) = α × V̂_e  where V̂_e is the electron's Wedderburn-weighted
    # traced volume from the trefoil σ₁³.
    # The pn crossing is mediated by the shared electron.
    # Reference: prop:mass-endomorphism-tower
    if A == 2:
        # V̂_e = w_sym × q³ + w_std × V_std + w_alt × (-1/q³)
        # For trefoil σ₁³ on 2 strands: 3 crossings, all (c=1, d=0) on gen 0.
        # V_std = z×M[0][0] + M[1][0] where M = T(1,0)³
        # T(1,0) = [[h, 1],[1, 0]] → T³ = specific matrix
        _t = [[h, 1.0], [1.0, 0.0]]
        _M = [[1.0, 0.0], [0.0, 1.0]]
        for _ in range(3):
            _M = [[_M[0][0]*_t[0][0]+_M[0][1]*_t[1][0],
                   _M[0][0]*_t[0][1]+_M[0][1]*_t[1][1]],
                  [_M[1][0]*_t[0][0]+_M[1][1]*_t[1][0],
                   _M[1][0]*_t[0][1]+_M[1][1]*_t[1][1]]]
        _V_std = z * _M[0][0] + _M[1][0]
        _V_e = W_SYM * q0**3 + W_STD * _V_std + W_ALT * (-qi**3)
        CATALAN_G = 0.915965594177219015054603514932
        _alpha = M_E_MEV * 8 * CATALAN_G
        return _alpha * abs(_V_e)

    # Try ordering cache first
    nuc_ordering = None
    try:
        from ordering_cache import get_ordering
        cached = get_ordering(Z, N)
        if cached:
            nuc_ordering = ['p' if x == 1 else 'n' for x in cached]
    except ImportError:
        pass

    if nuc_ordering is None:
        nuc_ordering = _alternating_ordering(Z, N)

    return _phi1_from_ordering(nuc_ordering)


def compute_phi1_full(Z, N):
    """Compute Φ₁ = Σᵢ ln|V̂ᵢ| from the transfer matrix chain.

    The full atomic braid includes nucleon AND electron strands.
    Crossing conventions:
      pp: (c=1, d=0)     — positive crossing (EM repulsion)
      nn: (c=1, d=-HA)   — inverse crossing (nuclear attraction)
      pn: (c=1, d=-HA/2) — mixed crossing (symmetric nuclear)
      pe: (c=1, d=-HA)   — proton-electron (EM attraction)
      ee: (c=1, d=0)     — electron-electron (EM repulsion)
      ne: skip            — neutron-electron (no interaction)

    Nucleon ordering for A ≤ 14: pp...nn (protons first).
    For A > 14: tries Rust hecke-engine for optimized ground-state
    ordering, falls back to pp...nn if unavailable.

    B₃ confinement justifies treating nucleons as atomic units
    (proved by confinement-lp.py via LP duality + Gram indefiniteness).
    """
    A = Z + N
    if A <= 1 and Z == 0:
        return 0.0

    # Nucleon ordering
    nuc_ordering = None
    if A > 14:
        # Try Rust engine for ground-state optimized ordering
        try:
            from hecke_rust_bridge import compute_nucleus, is_rust_available
            if is_rust_available():
                result = compute_nucleus(Z, N, timeout=30)
                if result and 'ordering_par' in result:
                    # Convert 0/1 ordering to p/n
                    nuc_ordering = ['p' if x == 1 else 'n'
                                    for x in result['ordering_par']]
        except ImportError:
            pass

    if nuc_ordering is None:
        nuc_ordering = _alternating_ordering(Z, N)

    # Full strand ordering: nucleons + electrons
    ordering = nuc_ordering + ['e'] * Z
    return _phi1_from_ordering(ordering)

def _load_categorical_shell():
    """Categorical shell from Chebyshev growth ratio γ(Z).

    f(Z) = 1/γ(Z), normalized by max.
    γ(Z) = |c_Z/c_{Z-1}| from (σ⁻¹)^Z = c_Z σ + d_Z.

    Recurrence: c_{n+1} = d_n, d_{n+1} = c_n - d_n·h, h = q−q⁻¹.
    All symbolic in q. No Gaussian, no empirical magic numbers.

    Reference: conj:q-integer-mass-formula, conj:shell-closure-nf-term-count
    """
    _h = q0 - qi
    c, d = 0.0, 1.0
    prev_c = 1.0
    inv_gamma = {}
    for Z in range(1, 200):
        c_new = d
        d_new = c - d * _h
        c, d = c_new, d_new
        g = abs(c / prev_c) if abs(prev_c) > 1e-300 else 1.0
        inv_gamma[Z] = 1.0 / g if g > 1e-300 else 0.0
        prev_c = c
    mx = max(inv_gamma.values())
    return {Z: v / mx for Z, v in inv_gamma.items()}


_CATEGORICAL_SHELL = _load_categorical_shell()


def magic_proximity(x, sigma=None):
    """Shell proximity from Chebyshev pairing ratio 1/γ(Z).

    Fully categorical: γ(Z) from the Hecke recurrence in q.
    No Gaussian, no empirical magic numbers.

    Reference: conj:q-integer-mass-formula
    """
    Z = int(round(x))
    if Z in _CATEGORICAL_SHELL:
        return _CATEGORICAL_SHELL[Z]
    return 0.0


# ══════════════════════════════════════════════════════════════
# Unified iterative (2,2) correction (replaces D + knot_factor + Wigner)
# ══════════════════════════════════════════════════════════════
#
# Categorical content (fully symbolic in q):
#
# • Energy scale.  The (2,2) ⊢ 4 q-hook product is
#       H_q((2,2)) = ∏_{x∈(2,2)} [h_x]_q = [3]·[2]·[2]·[1] = [3]·[2]²,
#   giving DELTA_22 = m_e · H_q((2,2)) ≈ 6.29 MeV.
#   EMPIRICAL COMPARISON (not a prediction): the experimental Wigner
#   shell-pairing scale is Δ_W ≈ 6.3 MeV [satula1997]. The ~0.2%
#   proximity is noted but not claimed as a structural derivation.
#
# • YSN matrices.  In the Young seminormal form of (2,2) (a 2-dim irrep
#   of H_4(q)) every Hecke generator σ_j has the same trace χ_{(2,2)}(σ)
#   = q − q⁻¹ = h.  We embed every crossing (c, d) acting between two
#   adjacent strands as M(c, d) = c · M_σ + d · I.  By the Kerov q-hook
#   walk [kerov1996], the trace of a chain of crossings in (2,2) is the
#   transition probability of the walk on the (2,2) cell of the Young
#   lattice; Féray–Méliot [feray-meliot2012] give the asymptotic
#   convergence rate O(1/√k).
#
# • Per-step accumulation.  At each step k, the crossings introduced by
#   adding nucleon k (intra-nucleon B₃·quark·gluon block, plus inter-
#   nucleon crossings with previous nucleons) form a chain whose YSN
#   matrix product M_22(step k) has character χ_22(step k).  The per-step
#   Wedderburn projection is w_{(2,2)} · χ_22(step k) / dim((2,2)),
#   i.e. the average eigenvalue of M_22 weighted by the (2,2) Wedderburn
#   weight.  Multiplying by DELTA_22 gives a MeV-valued contribution.
#
# • Restartability.  Each step is recorded as a witness row containing
#   (A, Z_k, N_k, nuc, χ_22, projection, cumulative).  Resuming the
#   accumulator from any A only requires the last row.
#
# Reference: prop:unified-iterative-correction.

# (2,2) YSN matrices for the three H_4(q) generators σ_1, σ_2, σ_3.
# Tableaux: T1 = [[1,2],[3,4]], T2 = [[1,3],[2,4]] (lex order).
#
# σ_1 swaps (1,2): T1 same row → eigenvalue q; T2 same column → -q⁻¹.
# σ_3 swaps (3,4): T1 same row → eigenvalue q; T2 same column → -q⁻¹.
# σ_2 swaps (2,3): mixes T1 ↔ T2 with axial-distance ρ = ±2.
#   diag = h / [ρ]_q,  off-diagonal = √(diag·(h-diag)+1).
#
# All entries are q-rational (computed from q₀ via q_int).
_M22_S1 = ((q0,    0.0    ),
           (0.0,   -qi    ))
_M22_S3 = ((q0,    0.0    ),
           (0.0,   -qi    ))
_diag_T1 = h / q_int(-2)                          # = -h/[2]_q
_diag_T2 = h - _diag_T1                            # h([2]_q+1)/[2]_q
_bc_22 = _diag_T1 * _diag_T2 + 1.0
_off_22 = math.sqrt(abs(_bc_22)) * (1.0 if _bc_22 > 0 else -1.0)
_M22_S2 = ((_diag_T1, _off_22),
           (_off_22,  _diag_T2))


def _matmul2(A, B):
    """Multiply two 2×2 matrices."""
    return ((A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]),
            (A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]))


def _crossing_M22(c, d, j):
    """Matrix of c·σ_j + d·I in the (2,2) representation, j ∈ {1,2,3}."""
    Mj = _M22_S1 if j == 1 else (_M22_S2 if j == 2 else _M22_S3)
    return ((c*Mj[0][0] + d, c*Mj[0][1]    ),
            (c*Mj[1][0],     c*Mj[1][1] + d))


def _chain_M22(chain):
    """YSN matrix product in (2,2) for a list of (c, d, j) crossings.

    A pure (c, d) tuple is interpreted as j = 1 (default generator).
    Returns the 2×2 matrix product.
    """
    M = ((1.0, 0.0), (0.0, 1.0))
    for entry in chain:
        if len(entry) == 2:
            c, d = entry
            j = 1
        else:
            c, d, j = entry
        M = _matmul2(M, _crossing_M22(c, d, j))
    return M


def _step_chain_22(nucleon_type, prev_types):
    """Crossing chain (in H_4 generators) for one NF-construction step.

    Returns a list of (c, d, j) tuples encoding the new crossings:
      • intra-nucleon block (B₃ + quark + gluon) — alternates σ_1, σ_2;
      • inter-nucleon crossings with all previous nucleons — uses σ_3.

    The choice of generator (1 vs 3 for the gen-0 block, 2 for the
    gen-1 block) reflects the two-generator H_3 structure embedded into
    H_4; (2,2) characters are independent of which σ_j we use because
    χ_{(2,2)}(σ_j) = h for all j.
    """
    chain = []
    intra = _PROTON_G0 if nucleon_type == 'p' else _NEUTRON_G0
    intra_g1 = _PROTON_G1 if nucleon_type == 'p' else _NEUTRON_G1
    for c, d in intra:
        chain.append((c, d, 1))
    for c, d in intra_g1:
        chain.append((c, d, 2))
    for ti in prev_types:
        if ti == 'p' and nucleon_type == 'p':
            chain.append((1.0, 0.0, 3))      # pp
        elif ti == 'n' and nucleon_type == 'n':
            chain.append((1.0, -h, 3))       # nn
        else:
            chain.append((1.0, -h / 2, 3))   # pn
    return chain


# ──────────────────────────────────────────────────────────────────
# Generic YSN matrices (Young seminormal form) for any partition λ
# ──────────────────────────────────────────────────────────────────
#
# A standard Young tableau of shape λ assigns 1, 2, …, |λ| to the
# cells of λ row-strictly increasing left-to-right and column-strictly
# increasing top-to-bottom.  In the YSN representation, the Hecke
# generator σ_k acts on each tableau T by:
#
#   • σ_k T = (q) T              if k, k+1 share a row;
#   • σ_k T = (-q⁻¹) T           if k, k+1 share a column;
#   • otherwise (different row, different col), 2×2 mixing block:
#         a_ρ = h / [ρ]_q,  a_{-ρ} = h - a_ρ,  b² = a_ρ a_{-ρ} + 1.
#
# All matrix entries are q-rational, evaluated numerically here using
# the substrate q₀.  The character χ_λ(σ_k) is independent of k
# (class function), so any embedding of crossings into σ_1, σ_2, …
# yields the same trace.

def _standard_tableaux(partition):
    """Enumerate standard Young tableaux of the given shape."""
    n = sum(partition)
    rows = list(partition)

    def fill(filled, val, remaining):
        if val > n:
            yield [list(r) for r in filled]
            return
        for r in range(len(rows)):
            if remaining[r] == 0:
                continue
            col = len(filled[r])
            if r > 0 and col >= len(filled[r - 1]):
                continue
            filled[r].append(val)
            remaining[r] -= 1
            yield from fill(filled, val + 1, remaining)
            filled[r].pop()
            remaining[r] += 1

    yield from fill([[] for _ in rows], 1, list(rows))


def _content_at(tab, val):
    """Return content c(val) = column − row for value val in tableau tab."""
    for r, row in enumerate(tab):
        for c, v in enumerate(row):
            if v == val:
                return c - r
    return None


def _swap_tab(tab, a, b):
    """Return tableau with a, b swapped — or None if result is invalid."""
    new = [list(r) for r in tab]
    pa = pb = None
    for r, row in enumerate(new):
        for c, v in enumerate(row):
            if v == a:
                pa = (r, c)
            if v == b:
                pb = (r, c)
    new[pa[0]][pa[1]] = b
    new[pb[0]][pb[1]] = a
    for row in new:
        if row != sorted(row):
            return None
    width = max(len(r) for r in new)
    for c in range(width):
        col = [new[r][c] for r in range(len(new)) if c < len(new[r])]
        if col != sorted(col):
            return None
    return new


def _build_ysn_matrices(partition, sparse_threshold=32):
    """Build YSN matrices for σ_1, …, σ_{n-1} of the given partition.

    For dim ≥ sparse_threshold, returns scipy.sparse.csr_matrix objects
    (each σ_j has at most 2·dim nonzeros: a diagonal entry plus
    2×2 mixing blocks, so sparsity ≈ 2/dim).
    For smaller dim, returns dense tuples (faster for small cases).

    All entries numerical (evaluated at q₀).
    """
    n = sum(partition)
    if n < 2:
        return []
    tabs = list(_standard_tableaux(partition))
    dim = len(tabs)
    if dim == 0:
        return []
    tab_index = {tuple(tuple(r) for r in T): i for i, T in enumerate(tabs)}

    use_sparse = dim >= sparse_threshold
    if use_sparse:
        from scipy.sparse import csr_matrix

    matrices = []
    for k in range(1, n):
        if use_sparse:
            rows, cols, vals = [], [], []
        else:
            M = [[0.0] * dim for _ in range(dim)]
        processed = set()
        for i, T in enumerate(tabs):
            if i in processed:
                continue
            ca = _content_at(T, k)
            cb = _content_at(T, k + 1)
            rho = cb - ca
            if rho == 0:
                continue
            same_row = any(k in row and (k + 1) in row for row in T)
            same_col = False
            width = max(len(r) for r in T)
            for c in range(width):
                col_vals = [T[r][c] for r in range(len(T)) if c < len(T[r])]
                if k in col_vals and (k + 1) in col_vals:
                    same_col = True
                    break
            if same_row:
                if use_sparse:
                    rows.append(i); cols.append(i); vals.append(q0)
                else:
                    M[i][i] = q0
                processed.add(i)
            elif same_col:
                if use_sparse:
                    rows.append(i); cols.append(i); vals.append(-qi)
                else:
                    M[i][i] = -qi
                processed.add(i)
            else:
                T_swapped = _swap_tab(T, k, k + 1)
                if T_swapped is None:
                    if use_sparse:
                        rows.append(i); cols.append(i)
                        vals.append(q0 if rho > 0 else -qi)
                    else:
                        M[i][i] = q0 if rho > 0 else -qi
                    processed.add(i)
                    continue
                key = tuple(tuple(r) for r in T_swapped)
                j = tab_index.get(key)
                if j is None:
                    if use_sparse:
                        rows.append(i); cols.append(i)
                        vals.append(q0 if rho > 0 else -qi)
                    else:
                        M[i][i] = q0 if rho > 0 else -qi
                    processed.add(i)
                    continue
                a_rho = h / q_int(rho)
                a_neg = h - a_rho
                bsq = a_rho * a_neg + 1.0
                off = math.sqrt(abs(bsq)) * (1.0 if bsq > 0 else -1.0)
                if use_sparse:
                    rows.extend([i, j, i, j])
                    cols.extend([i, j, j, i])
                    vals.extend([a_rho, a_neg, off, off])
                else:
                    M[i][i] = a_rho
                    M[j][j] = a_neg
                    M[i][j] = off
                    M[j][i] = off
                processed.add(i)
                processed.add(j)
        if use_sparse:
            matrices.append(csr_matrix((vals, (rows, cols)), shape=(dim, dim)))
        else:
            matrices.append(tuple(tuple(row) for row in M))
    return matrices


def _matmul_dim(A, B, dim):
    """Multiply two dim×dim matrices.  Uses numpy for dim ≥ 8 (significant
    speedup for higher Hecke levels)."""
    if dim >= 8:
        return np.asarray(A) @ np.asarray(B)
    out = [[0.0] * dim for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            s = 0.0
            for kk in range(dim):
                s += A[i][kk] * B[kk][j]
            out[i][j] = s
    return tuple(tuple(r) for r in out)


def _trace_dim(M, dim):
    if isinstance(M, np.ndarray):
        return float(np.trace(M))
    return sum(M[i][i] for i in range(dim))


def _identity(dim):
    if dim >= 8:
        return np.eye(dim)
    return tuple(tuple(1.0 if i == j else 0.0 for j in range(dim))
                 for i in range(dim))


def _crossing_in_partition(c, d, gen_index, sigmas, dim):
    """Matrix of c·σ_{gen} + d·I  in YSN representation of a partition."""
    sig = sigmas[gen_index]
    if dim >= 8:
        # Work in numpy for large dims
        sig_np = sig if isinstance(sig, np.ndarray) else np.asarray(sig)
        return c * sig_np + d * np.eye(dim)
    out = [[c * sig[i][j] + (d if i == j else 0.0) for j in range(dim)]
           for i in range(dim)]
    return tuple(tuple(r) for r in out)


# YSN-matrix attachment for every entry in _PARTITION_TABLE
# (k = 2..K_PARTITION_MAX).  Skipped if dim < 2 (no mixing structure →
# trivial trace).  For k > K_PARTITION_MAX we keep metadata-only
# entries (no YSN); the q-Gaussian fallback uses d_q / shadow_price /
# q_hook without needing matrices.
#
# This phase used to run eagerly at module import and cost ~30 s on
# top of the partition-table build. Now folded into a lazy helper so
# scripts that never touch _PARTITION_TABLE pay nothing.

_YSN_ATTACHED = False


def _ensure_ysn_attached():
    """Idempotent helper: attach YSN matrices + n_gens to each
    partition-table entry on first demand."""
    global _YSN_ATTACHED
    if _YSN_ATTACHED:
        return
    for _entry in _partition_table():
        if _entry['has_ysn']:
            _entry['ysn'] = _build_ysn_matrices(_entry['partition'])
        else:
            _entry['ysn'] = []
        _entry['n_gens'] = max(0, _entry['k'] - 1)
    _YSN_ATTACHED = True


def _step_chain_generic(nucleon_type, prev_types, n_gens, include_inter=True):
    """Crossing chain in the H_{n_gens+1}(q) generators σ_1, …, σ_{n_gens}
    for one NF-construction step.  Same chain content as `_step_chain_22`
    but the generator index cycles modulo `n_gens`, so any partition of
    size k = n_gens + 1 receives a full set of crossings.

    include_inter : bool (default True)
        If False, skip inter-nucleon crossings — gives the disconnected
        intra-nucleon braid segment used for the free-nucleon baseline.
    """
    chain = []
    intra = _PROTON_G0 if nucleon_type == 'p' else _NEUTRON_G0
    intra_g1 = _PROTON_G1 if nucleon_type == 'p' else _NEUTRON_G1
    g = 0
    for c, d in intra:
        chain.append((c, d, g % n_gens))
        g += 1
    for c, d in intra_g1:
        chain.append((c, d, g % n_gens))
        g += 1
    if include_inter:
        for ti in prev_types:
            if ti == 'p' and nucleon_type == 'p':
                chain.append((1.0, 0.0, g % n_gens))      # pp
            elif ti == 'n' and nucleon_type == 'n':
                chain.append((1.0, -h, g % n_gens))       # nn
            else:
                chain.append((1.0, -h / 2, g % n_gens))   # pn
            g += 1
    return chain


def _q_gaussian_character_approx(entry, n_crossings_at_step, step_idx):
    """Perron-Frobenius dominant-eigenvalue approximation to ln|Tr M_λ|.

    IMPORTANT NOTE — Bozejko-Speicher q-Gaussian does NOT apply here:

      The Bozejko-Speicher q-Gaussian [bozejko-speicher1991] requires
      |q| ≤ 1 for a convergent noncommutative distribution.  Our
      substrate q₀ ≈ 1.11 > 1, so the Touchard pair-partition moments
      T_n(q₀) = Σ_{π} q₀^{cr(π)} grow super-exponentially in n — NO
      well-defined q-Gaussian distribution exists at q > 1.
      Attempting to use Bozejko-Speicher at q₀ would conceptually
      misapply the framework.

    WHAT WE USE INSTEAD — Perron-Frobenius dominant eigenvalue:

      For any representation of the braid group, the trace of a long
      word W is dominated by the largest |eigenvalue| of the "mean"
      crossing matrix in that representation:
           ln|Tr M_λ(W_N)| ≈ ln d_q(λ) + N · ln|μ_λ|
      where μ_λ is the spectral radius of a typical crossing (c·σ+d·I)
      in the λ-irrep.  This is pure linear algebra (Perron-Frobenius
      theorem for positive operators) and is valid for any q > 0
      including q > 1.

      For the "average" inter-nucleon crossing (mix of pp, nn, pn):
        mean (c, d) ≈ (1, -h/2)
        eigenvalues of (σ - h/2 I) in 1-dim sym rep: q - h/2
        eigenvalues in alt rep: -q⁻¹ - h/2
        max |eigenvalue|: max(|q-h/2|, |q⁻¹+h/2|)

      For dim ≥ 2 irreps, the spectral radius is bounded by q (the
      largest eigenvalue of σ in sym is q; mixing blocks have
      eigenvalues between q and -q⁻¹).

      Féray-Méliot damping [2]_q^{−(k−3)} modulates how much weight
      higher-k partitions carry in the typical q-Plancherel spectrum.

    Working approximation (uses actual crossing count, exact d_q,
    spectral-radius-informed per-crossing rate, Féray-Méliot damping):

        ln|Tr M_λ(step)| ≈ ln d_q(λ)
                         + N(step) · [2]_q^{−(k−3)} · ln(q₀)

    where N(step) = 12·(step+1) + step·(step+1)/2, and ln(q₀) is
    the per-crossing log dominant eigenvalue (≈ 0.104).
    """
    k = entry['k']
    dim = entry['dim']
    n_intra = 12 * (step_idx + 1)
    n_inter = step_idx * (step_idx + 1) // 2
    N_total = n_intra + n_inter
    # Per-partition spectral log rate ρ_λ = |χ_λ(σ_1)| / d(λ)  —
    # computed from SYT counts without building the full YSN matrix.
    # See partition_spectral_log_rate for derivation.
    per_cross_log = entry.get('spectral_log_rate', math.log(q0))
    # Féray-Méliot damping relative to H₃(q) baseline
    damping = TWO_Q ** (-(k - 3)) if k > 3 else 1.0
    return math.log(dim) + N_total * damping * per_cross_log


def unified_iterative_correction(Z, N, return_per_step=False,
                                 k_max=K_PARTITION_MAX,
                                 k_exact=K_PARTITION_MAX):
    """Unified iterative correction via LP-dual shadow prices.

    A SINGLE consistent algorithm — no special cases for any A.
    Starts at A = 1 and accumulates a per-step contribution from
    EVERY partition λ ⊢ k for k = 2, …, k_max:

      ΔB_k(step) = m_e · H_q(λ) · y_λ ·
                   ( ln|Tr M_λ^{(0..step)}| − ln|Tr M_λ^{(0..step−1)}| )

    where:

      • H_q(λ) = ∏_{x∈λ} [h_x(λ)]_q is the q-hook product (the
        categorical scale C_λ = m_e · H_q(λ) generalises the (2,2)
        derivation of [3]·[2]² · m_e to every λ);
      • y_λ = w_λ/d_λ − 1/[k]_q! is the LP-dual shadow price of the
        Frobenius positivity constraint of λ
        (prop:mass-coefficient-shadow-price); shadow prices are the
        unique invariants that the operator-selection LP assigns to
        the partition basis;
      • M_λ^{(0..step)} is the running YSN matrix product across
        all steps so far, embedded into the Hecke generators
        σ_1, …, σ_{k-1} of H_k(q) (cyclic generator index keeps the
        embedding well-defined for any k);
      • the log-trace difference is the energy-additive accumulator
        (matches the `next_partition_levels` channel decomposition).

    Telescoping: total contribution per partition is
      B_λ = m_e · H_q(λ) · y_λ · ( ln|Tr M_λ^{(0..A)}| − ln d_λ ),
    summed over all enumerated partitions.

    The mechanism replaces — without any special-case branches — the
    dedicated D-binding formula (A = 2), the knot factor (A = 3, 4),
    the Wigner energy (k ≥ 5), and any further per-partition shadow
    contributions up to k_max.

    Parameters
    ----------
    Z, N : int
        Proton and neutron counts.
    return_per_step : bool
        If True, also return per-step witness rows.
    k_max : int
        Maximum Hecke level for partition enumeration (default
        K_PARTITION_MAX).  For k ≤ k_exact uses exact YSN matrices;
        for k_exact < k ≤ k_max falls back to a Bozejko-Speicher
        q-Gaussian approximation (labelled in per-step witness rows).
    k_exact : int
        Maximum Hecke level for EXACT (YSN matrix) evaluation.
        Partitions with k ≤ k_exact use explicit Young seminormal
        form matrix products; those with k_exact < k ≤ k_max use
        the q-Gaussian asymptotic approximation (cheap, less
        accurate).  Default = K_PARTITION_MAX (all exact up to the
        compiled partition table).

    Returns
    -------
    float (total correction, MeV) or
    (float, list-of-dicts) if return_per_step.

    References
    ----------
    Kerov 1996 (q-hook walk) [kerov1996],
    Féray–Méliot 2010 (q-Plancherel CLT) [feray-meliot2012],
    Satuła et al. 1997 (empirical Wigner energy) [satula1997],
    prop:mass-coefficient-shadow-price (LP dual = BW coefficient).
    """
    A = Z + N
    if A < 1:
        if return_per_step:
            return 0.0, []
        return 0.0

    # Ground-state ordering (matches build_atom_nf / atom_gen_chains).
    ordering = []
    pc, nc = 0, 0
    for kk in range(A):
        if (kk % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p'); pc += 1
        else:
            ordering.append('n'); nc += 1

    # Active partition entries: those with k ≤ k_max and dim ≥ 2 (1-dim
    # sym/alt reps have y_λ = 0 and contribute nothing).
    # ALL mixing partitions including (2,1) are kept because:
    #
    #   The accumulator computes (atom LP − free-nucleon baseline LP),
    #   which subtracts the per-nucleon intra-block projection.
    #   This makes the result a genuine BINDING correction — the
    #   categorical definition M_atom − Σ M_free_nucleon.
    # Partition active set.  Exact (YSN) evaluation for k ≤ k_exact;
    # q-Gaussian approximation for k_exact < k ≤ k_max.
    # Exact requires YSN matrices; q-Gaussian requires only mixing
    # partitions (dim ≥ 2) — metadata alone suffices.
    active_exact = [e for e in _PARTITION_TABLE
                    if e['k'] <= k_exact and e.get('has_ysn', False)
                    and len(e['ysn']) > 0]
    active_gaussian = [e for e in _PARTITION_TABLE
                       if k_exact < e['k'] <= k_max and e['dim'] >= 2]
    active = active_exact

    # ═══ TWO-PASS LP-DUAL WITH COMPLEMENTARY SLACKNESS ═════════
    #
    # Pass 1 (forward): accumulate running YSN matrix M_λ for every
    #   active partition through all A steps.  Record per-step
    #   log-traces and per-partition cumulative contributions.
    #
    # Pass 2 (gate): at the FINAL state, check the sign of the raw
    #   trace tr(M_λ(atom)).  By complementary slackness of the
    #   operator-selection LP (prop:mass-coefficient-shadow-price):
    #     y_λ* × ⟨Φ*, π_λ⟩_F = 0
    #   so y_λ* = 0 whenever the Frobenius constraint is SLACK
    #   (tr > 0).  Only partitions with TIGHT constraints (tr ≤ 0)
    #   contribute a nonzero shadow price.
    #
    # This is the per-atom LP dual: each atom's braid Φ(Z,N) has a
    # different set of tight partitions, so the correction is
    # atom-specific — exactly as the categorical LP predicts.
    #
    # Kerov-damped scale (same as before):
    #   C_λ^kerov = w_λ · y_λ · H_q(λ) · m_e

    # Detect sparse YSN matrices and import scipy lazily.
    try:
        from scipy.sparse import issparse as _issparse
    except ImportError:  # pragma: no cover
        _issparse = lambda x: False  # noqa: E731

    state = []
    for e in active:
        first = e['ysn'][0]
        sparse_sigmas = _issparse(first)
        dim = first.shape[0] if sparse_sigmas else len(first)
        if sparse_sigmas:
            # Running M is dense for fast sparse-× -dense multiplication
            M = np.eye(dim)
        else:
            M = _identity(dim)
        L0 = math.log(dim)
        # Resolvent-damped scale (def:q-heat-equation,
        # def:categorical-laplace-transform):
        #   C_λ = m_e · H_q(λ) · y_λ · ρ_λ(s_*)
        # where ρ_λ(s) = 1/(μ_λ + s) is the resolvent of the q-Laplacian
        # at Reeb-time spectral parameter s, μ_λ = Σ_{x∈λ} [c(x)]_q² is
        # the q-Casimir eigenvalue on the λ-block, and s_* = (q−1)/q
        # is the Planck-step Reeb frequency (1/t_P(q)).
        # This replaces the ad-hoc Kerov Plancherel multiplier with a
        # categorically-derived damping from the q-heat spectrum.
        scale = e['C_lambda_resolvent_MeV']
        state.append({
            'entry': e, 'dim': dim, 'M': M, 'log_norm': 0.0,
            'log_prev': L0, 'scale': scale, 'cumul_partition': 0.0,
            'sparse': sparse_sigmas,
        })

    per_step = []
    cumul_total = 0.0

    # ── Pass 1: forward accumulation ──────────────────────────
    for kk in range(A):
        nuc = ordering[kk]
        prev_types = ordering[:kk]

        step_delta_total = 0.0
        partitions_step = {}

        for s in state:
            entry = s['entry']
            dim = s['dim']
            sigmas = entry['ysn']
            n_gens = entry['n_gens']
            chain = _step_chain_generic(nuc, prev_types, n_gens)
            if s['sparse']:
                # For each crossing (c, d, gen), apply M ← M @ (c·σ_gen + d·I)
                # = c · (M @ σ_gen_sparse) + d · M.  Avoids materialising
                # the dense (c·σ + d·I) matrix at every crossing.
                # Cost: dense × sparse = O(dim · nnz) = O(dim²) vs
                # dense × dense = O(dim³).
                M_run = s['M']
                for c, d, gen in chain:
                    sig_sparse = sigmas[gen]
                    # scipy sparse: dense @ sparse returns dense ndarray,
                    # computed as a sparse BLAS operation in O(dim·nnz).
                    Msig = sig_sparse.T.dot(M_run.T).T  # = M_run @ sig_sparse
                    M_run = c * Msig + d * M_run
                s['M'] = M_run
            else:
                M_step = _identity(dim)
                for c, d, gen in chain:
                    M_cross = _crossing_in_partition(c, d, gen, sigmas, dim)
                    M_step = _matmul_dim(M_step, M_cross, dim)
                s['M'] = _matmul_dim(s['M'], M_step, dim)
            if isinstance(s['M'], np.ndarray):
                m_max = float(np.max(np.abs(s['M'])))
            else:
                m_max = 0.0
                for i in range(dim):
                    for j in range(dim):
                        if abs(s['M'][i][j]) > m_max:
                            m_max = abs(s['M'][i][j])
            if m_max > 1e80:
                if isinstance(s['M'], np.ndarray):
                    s['M'] = s['M'] / m_max
                else:
                    M_rescaled = [[s['M'][i][j] / m_max for j in range(dim)]
                                  for i in range(dim)]
                    s['M'] = tuple(tuple(r) for r in M_rescaled)
                s['log_norm'] += math.log(m_max)
            tr_run = _trace_dim(s['M'], dim)
            log_cur = (s['log_norm'] + math.log(abs(tr_run))
                       if abs(tr_run) > 1e-300 else s['log_prev'])
            raw_delta = s['scale'] * (log_cur - s['log_prev'])
            # LP complementary slackness is a FINAL-STATE condition:
            # y_λ* × tr(Φ_λ*) = 0 on the SOLVED LP.  The per-step
            # tightness filter would be a heuristic approximation of
            # this; experimentally it over-gates (k-instability).
            # Here we accumulate raw deltas at every step; the final
            # sign gate is applied in Pass 2 below.
            delta = raw_delta
            s['cumul_partition'] += delta
            s['log_prev'] = log_cur
            # Store raw trace sign for final-state complementary slackness.
            s['final_tr_sign'] = 1 if tr_run > 0 else -1
            step_delta_total += delta
            partitions_step[str(entry['partition'])] = {
                'log_trace': log_cur,
                'delta_MeV': delta,
            }

        # ── q-Gaussian fallback contribution (k_exact < k ≤ k_max) ──
        # Perron-Frobenius asymptotic approximation for partitions
        # beyond the explicit-YSN cutoff.  Each gives a cheap
        # per-step estimate (no matrix product required).
        #
        # Per-step tightness gate: sign of approximated trace.  The
        # approximation gives log_trace directly; the TRACE sign is
        # positive (trace ~ exp(log_trace)).  Positive trace ⇒ SLACK
        # Frobenius constraint ⇒ y_λ* = 0 by complementary slackness.
        # In this approximation the trace is always +ve, so by LP
        # duality the partition contributes ZERO at this step.
        # Below-threshold partitions (where the spectral rate is
        # NEGATIVE, |χ/d| < 1) have log_trace shrinking; their
        # "effective trace" approaches 0⁺ from above — still slack.
        #
        # Conclusion: the Perron-Frobenius q-Gaussian fallback
        # contributes 0 after the complementary slackness gate.
        # Extension to higher k via this approximation does NOT
        # generate non-zero corrections — it correctly predicts
        # that typical high-k partitions are SLACK and contribute
        # nothing in the LP-dual framework.
        gaussian_delta_total = 0.0
        for eg in active_gaussian:
            eg_info = eg
            log_trace_approx = _q_gaussian_character_approx(eg_info, None, kk)
            # By LP complementary slackness: tr > 0 ⇒ slack ⇒ y_λ* = 0
            # ⇒ delta = 0.  This is the categorically correct outcome
            # for partitions with no evidence of the Frobenius
            # constraint being tight at any step.
            delta_g = 0.0
            gaussian_delta_total += delta_g
            if return_per_step:
                partitions_step[str(eg['partition'])] = {
                    'log_trace': log_trace_approx,
                    'delta_MeV': delta_g,
                    'method': 'q_gaussian',
                }
        step_delta_total += gaussian_delta_total

        # Single accumulation to cumul_total per step (after exact + gaussian)
        cumul_total += step_delta_total

        if return_per_step:
            Z_k = sum(1 for x in ordering[:kk + 1] if x == 'p')
            N_k = (kk + 1) - Z_k
            per_step.append({
                'A': kk + 1, 'Z': Z_k, 'N': N_k, 'nuc': nuc,
                'delta_total_MeV': step_delta_total,
                'cumulative_MeV': cumul_total,
                'partitions': partitions_step,
                'n_exact_partitions': len(active_exact),
                'n_gaussian_partitions': len(active_gaussian),
            })

    # ── Pass 2: final-state complementary slackness gate ─────────
    # LP duality theorem: on the OPTIMAL primal-dual pair (Φ*, y*),
    #   y_λ* × ⟨Φ*, π_λ⟩_F = 0  for every partition λ.
    # So y_λ* > 0 only when the Frobenius constraint is TIGHT at the
    # atom's FINAL state, i.e. tr(M_λ(W_atom)) ≤ 0.  Partitions with
    # positive final trace are SLACK → y_λ* = 0 → zero contribution.
    # Replace cumul_total with the gated sum over tight partitions.
    gated_total = 0.0
    n_tight = 0
    for s in state:
        if s.get('final_tr_sign', 1) <= 0:
            gated_total += s['cumul_partition']
            n_tight += 1

    if return_per_step:
        if per_step:
            per_step[-1]['raw_total_MeV'] = cumul_total
            per_step[-1]['gated_total_MeV'] = gated_total
            per_step[-1]['n_active_exact'] = len(active_exact)
            per_step[-1]['n_active_gaussian'] = len(active_gaussian)
            per_step[-1]['n_tight_final'] = n_tight
            per_step[-1]['k_exact'] = k_exact
            per_step[-1]['k_max'] = k_max
        return gated_total, per_step
    return gated_total


def _jet_witness_path(Z, N, jet, witness_dir):
    """Witness file path for one (Z, N, jet) cell."""
    return _os.path.join(witness_dir,
                         f'unified_jet_Z{Z}_N{N}_j{jet}.json')


def atom_character_raw(Z, N, entry, include_inter=True):
    """Return the raw characters of the atom braid word in partition λ.

    Returns (chi_q_atom, log_norm, dim) where chi_q_atom × exp(log_norm)
    is the actual YSN trace Tr(M_λ(W_atom)) at q = q_0.
    Uses periodic rescaling to avoid overflow; caller reconstructs via
    log-trace = log|chi_q_atom| + log_norm.

    include_inter : bool (default True)
        If False, skip inter-nucleon crossings — gives the
        disconnected-tensor FREE NUCLEON baseline χ_λ(W_free).
        The resulting braid is the disconnected product of
        intra-nucleon blocks, corresponding to H_3(q)^⊗A ↪ H_{3A}(q).
    """
    try:
        from scipy.sparse import issparse as _issparse
    except ImportError:
        _issparse = lambda x: False
    A = Z + N
    if A < 1 or not entry.get('has_ysn') or not entry.get('ysn'):
        return (float(entry.get('dim', 1)), 0.0, int(entry.get('dim', 1)))

    ordering = []
    pc, nc = 0, 0
    for kk in range(A):
        if (kk % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p'); pc += 1
        else:
            ordering.append('n'); nc += 1
    sigmas = entry['ysn']
    n_gens = entry['n_gens']
    first = sigmas[0]
    sparse_sigmas = _issparse(first)
    dim = first.shape[0] if sparse_sigmas else len(first)
    M = np.eye(dim) if sparse_sigmas else _identity(dim)
    log_norm = 0.0
    for kkk in range(A):
        nuc = ordering[kkk]
        prev_types = ordering[:kkk]
        chain = _step_chain_generic(nuc, prev_types, n_gens, include_inter=include_inter)
        if sparse_sigmas:
            M_run = M
            for c, d, gen in chain:
                sig_sparse = sigmas[gen]
                Msig = sig_sparse.T.dot(M_run.T).T
                M_run = c * Msig + d * M_run
            M = M_run
        else:
            M_step = _identity(dim)
            for c, d, gen in chain:
                M_cross = _crossing_in_partition(c, d, gen, sigmas, dim)
                M_step = _matmul_dim(M_step, M_cross, dim)
            M = _matmul_dim(M, M_step, dim)
        if isinstance(M, np.ndarray):
            m_max = float(np.max(np.abs(M)))
        else:
            m_max = max(abs(M[i][j]) for i in range(dim) for j in range(dim))
        if m_max > 1e80:
            if isinstance(M, np.ndarray):
                M = M / m_max
            else:
                M = tuple(tuple(M[i][j]/m_max for j in range(dim))
                          for i in range(dim))
            log_norm += math.log(m_max)
    chi = _trace_dim(M, dim)
    return (float(chi), float(log_norm), int(dim))


def _contrib_single_partition(Z, N, entry):
    """Compute one partition's final LP-dual contribution for atom (Z,N).
    Returns (final_trace_sign, cumul_delta_MeV).
    Separate from the multi-partition accumulator so we can process
    partitions one at a time (needed for the jet-incremental loop).
    """
    try:
        from scipy.sparse import issparse as _issparse
    except ImportError:
        _issparse = lambda x: False

    A = Z + N
    if A < 1 or not entry.get('has_ysn') or not entry.get('ysn'):
        return (+1, 0.0)  # slack by default

    ordering = []
    pc, nc = 0, 0
    for kk in range(A):
        if (kk % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p'); pc += 1
        else:
            ordering.append('n'); nc += 1

    sigmas = entry['ysn']
    n_gens = entry['n_gens']
    first = sigmas[0]
    sparse_sigmas = _issparse(first)
    dim = first.shape[0] if sparse_sigmas else len(first)

    if sparse_sigmas:
        M = np.eye(dim)
    else:
        M = _identity(dim)

    log_norm = 0.0
    log_prev = math.log(dim)
    scale = entry['C_lambda_resolvent_MeV']
    cumul = 0.0
    tr_run = dim  # initial trace of identity

    for kkk in range(A):
        nuc = ordering[kkk]
        prev_types = ordering[:kkk]
        chain = _step_chain_generic(nuc, prev_types, n_gens)
        if sparse_sigmas:
            M_run = M
            for c, d, gen in chain:
                sig_sparse = sigmas[gen]
                Msig = sig_sparse.T.dot(M_run.T).T
                M_run = c * Msig + d * M_run
            M = M_run
        else:
            M_step = _identity(dim)
            for c, d, gen in chain:
                M_cross = _crossing_in_partition(c, d, gen, sigmas, dim)
                M_step = _matmul_dim(M_step, M_cross, dim)
            M = _matmul_dim(M, M_step, dim)

        if isinstance(M, np.ndarray):
            m_max = float(np.max(np.abs(M)))
        else:
            m_max = max(abs(M[i][j]) for i in range(dim) for j in range(dim))
        if m_max > 1e80:
            if isinstance(M, np.ndarray):
                M = M / m_max
            else:
                M = tuple(tuple(M[i][j]/m_max for j in range(dim))
                          for i in range(dim))
            log_norm += math.log(m_max)

        tr_run = _trace_dim(M, dim)
        if abs(tr_run) > 1e-300:
            log_cur = log_norm + math.log(abs(tr_run))
        else:
            log_cur = log_prev
        cumul += scale * (log_cur - log_prev)
        log_prev = log_cur

    final_tr_sign = +1 if tr_run > 0 else -1
    return (final_tr_sign, cumul)


def conjugate_pair_cross_term(Z, N, entry_lambda, entry_conj):
    """Cross-channel contribution from a conjugate pair (λ, λ').

    Derivation.  From the paired-sum identity (wigner-2-coefficient.md
    Step 1, ConfinedKnotBinding.lean paired_sum_identity):

      tr(σ_g^{(λ)}) + tr(σ_g^{(λ')}) = h · (d_λ + d_{λ'}) / 2   (generators)
      equivalently  tr(σ_g)/dim combined pair = h/2
                    when both partitions share the same generator scaling.

    Combined conjugate-pair scale (matches DELTA_FORMFACTOR, DELTA_411,
    DELTA_42 in the dedicated BW path):

      C_{λ,λ'} = h · [average q-hook · average shadow price · average
                 resolvent] · m_e

    The contribution is h times the AVERAGE of the two partition
    contributions — i.e., the "extra" coupling beyond the linear sum
    of y_λ · H_q(λ) and y_{λ'} · H_q(λ').  For SELF-CONJUGATE λ = λ',
    the factor is h/2 (Wigner-2 coefficient).

    Physical interpretation (figure-eight-branching-rule.md §5):
    conjugate pairs contribute FORM FACTOR corrections (Z²/A for
    (3,2)+(2,2,1)) or ISOSPIN corrections ((N−Z)² for
    (4,1,1)+(3,1,1,1)).  The `h` coupling is the q−q⁻¹ twist that
    converts the pair-sum of individual traces into a genuine
    cross-channel contribution.

    Implementation:
      - Compute log|Tr M_λ| and log|Tr M_{λ'}| via single-partition
        forward pass (re-using the same machinery)
      - Combine: cross_scale = h · √(H_q(λ) · H_q(λ')) · √(y_λ · y_{λ'})
                                · ρ(s_*) · m_e
                 where ρ uses the AVERAGE μ.
      - Final contribution: cross_scale · (log|Tr_λ| + log|Tr_{λ'}| - ln d_λ - ln d_{λ'})
    """
    hbar_like = float(h)  # h = q − q⁻¹
    tr_sign_l, cumul_l = _contrib_single_partition(Z, N, entry_lambda)
    tr_sign_c, cumul_c = _contrib_single_partition(Z, N, entry_conj)
    # Cross-scale: h × geometric mean of individual scales
    import math as _math
    scale_l = entry_lambda['C_lambda_resolvent_MeV']
    scale_c = entry_conj['C_lambda_resolvent_MeV']
    # Effective scale uses h × geometric mean; retains sign via log
    sign_l = 1 if scale_l >= 0 else -1
    sign_c = 1 if scale_c >= 0 else -1
    geom_mean = _math.sqrt(abs(scale_l * scale_c))
    cross_scale_mev = hbar_like * geom_mean * sign_l * sign_c
    # Cross contribution: h × (cumul_l + cumul_c) / 2 weighted by mean scale.
    # Equivalent expression: h × average of per-partition corrections.
    # Apply complementary slackness: at least ONE of the pair must be tight
    # for the cross term to contribute (conservative gate).
    tight_either = (tr_sign_l <= 0) or (tr_sign_c <= 0)
    if not tight_either:
        cross = 0.0
    else:
        # Average the two partition contributions, scaled by h relative to base
        # scale_l · cumul_l is already in MeV; convert to per-partition
        # log-trace diff then multiply by h · geometric scale
        sum_cumul = cumul_l + cumul_c
        cross = hbar_like * sum_cumul / 2.0
    return {
        'lambda': list(entry_lambda['partition']),
        'lambda_conj': list(entry_conj['partition']),
        'tr_sign_l': tr_sign_l,
        'tr_sign_c': tr_sign_c,
        'tight_either': tight_either,
        'cumul_l_MeV': cumul_l,
        'cumul_c_MeV': cumul_c,
        'cross_scale_MeV': cross_scale_mev,
        'cross_contribution_MeV': cross,
    }


def unified_iterative_correction_jet(Z, N, jet_max,
                                     witness_dir=None,
                                     resume=True,
                                     k_cap=None):
    """Jet-filtered iterative LP-dual accumulator with per-jet witnesses.

    Architecture:
      For j = 1, 2, ..., jet_max:
        Exact-jet partitions at j = {λ in _PARTITION_TABLE
                                     : jet(λ) = j, dim(λ) >= 2,
                                       k(λ) <= k_cap (or K_PARTITION_MAX)}
        For each such λ:
          Compute final LP-dual contribution for atom (Z, N)
          (YSN matrix product through all A steps, complementary
           slackness gate on final trace sign).
        Aggregate total_at_j = Σ_{λ tight, jet(λ) = j} contribution_λ.
        Save per-jet witness: list of partitions processed, their
        final trace signs, contributions, and total_at_j.

    Restart:
      If witness_dir is given and resume=True, existing per-jet
      witnesses are loaded (skipping recomputation).  This lets us
      pick up from any checkpoint j_star by running jet_max > j_star.

    Returns:
      (total, per_jet_summary) where total = Σ_{j ≤ jet_max} total_at_j
      and per_jet_summary[j] = {partitions, n_tight, total_MeV}.
    """
    if k_cap is None:
        k_cap = K_PARTITION_MAX

    total = 0.0
    per_jet = {}

    for j in range(1, jet_max + 1):
        # Try to load existing witness
        wpath = None
        if witness_dir is not None:
            _os.makedirs(witness_dir, exist_ok=True)
            wpath = _jet_witness_path(Z, N, j, witness_dir)
            if resume and _os.path.exists(wpath):
                with open(wpath, 'r') as f:
                    data = _json.load(f)
                per_jet[j] = {
                    'partitions': data['partitions'],
                    'n_tight': data['n_tight'],
                    'total_MeV': data['total_MeV'],
                }
                total += data['total_MeV']
                continue

        # Compute at this jet
        active_at_j = [e for e in _PARTITION_TABLE
                       if e.get('jet') == j
                       and e.get('dim', 0) >= 2
                       and e.get('k', 0) <= k_cap
                       and e.get('has_ysn', False)]

        parts_record = []
        cumul_by_partition = {}  # cache (tuple → (tr_sign, cumul))
        total_at_j_linear = 0.0
        n_tight = 0
        for entry in active_at_j:
            tr_sign, cumul = _contrib_single_partition(Z, N, entry)
            cumul_by_partition[tuple(entry['partition'])] = (tr_sign, cumul)
            tight = (tr_sign <= 0)
            gated = cumul if tight else 0.0
            if tight:
                n_tight += 1
                total_at_j_linear += gated
            parts_record.append({
                'partition': list(entry['partition']),
                'k': entry['k'],
                'dim': entry['dim'],
                'final_tr_sign': tr_sign,
                'tight': tight,
                'cumul_raw_MeV': cumul,
                'contribution_MeV': gated,
            })

        # Conjugate-pair cross terms (at same jet level; both in active_at_j
        # iff jet(λ) = jet(λ') = j, which holds because jet is conjugation-
        # symmetric).  Self-conjugate λ = λ' gets Wigner-2 h/2 coupling.
        pair_records = []
        total_at_j_cross = 0.0
        seen_pairs = set()
        hbar_like = float(h)
        for entry in active_at_j:
            lam = tuple(entry['partition'])
            conj = partition_conjugate(lam)
            if conj == lam:
                # Self-conjugate: Wigner-2 coefficient h/2 coupling.
                # tr(σ)/dim = h/2 ⇒ contribution scale ~ h/2 × cumul
                tr_sign, cumul = cumul_by_partition[lam]
                tight = (tr_sign <= 0)
                if tight:
                    cross = (hbar_like / 2.0) * cumul
                    total_at_j_cross += cross
                else:
                    cross = 0.0
                pair_records.append({
                    'lambda': list(lam),
                    'lambda_conj': list(conj),
                    'self_conjugate': True,
                    'coupling': 'h/2',
                    'tight': tight,
                    'cross_contribution_MeV': cross,
                })
            else:
                # Pair with conjugate — both must be in active set
                if conj not in cumul_by_partition:
                    continue
                pair_key = frozenset({lam, conj})
                if pair_key in seen_pairs:
                    continue
                seen_pairs.add(pair_key)
                tr_l, cumul_l = cumul_by_partition[lam]
                tr_c, cumul_c = cumul_by_partition[conj]
                tight_either = (tr_l <= 0) or (tr_c <= 0)
                # Pair-sum cross coupling via h identity:
                #   tr_σ_λ + tr_σ_λ' = h · (d_λ + d_λ')
                # Average contribution scaled by h:
                if tight_either:
                    cross = hbar_like * (cumul_l + cumul_c) / 2.0
                    total_at_j_cross += cross
                else:
                    cross = 0.0
                pair_records.append({
                    'lambda': list(lam),
                    'lambda_conj': list(conj),
                    'self_conjugate': False,
                    'coupling': 'h',
                    'tight_either': tight_either,
                    'cross_contribution_MeV': cross,
                })

        total_at_j = total_at_j_linear + total_at_j_cross

        per_jet[j] = {
            'partitions': parts_record,
            'pairs': pair_records,
            'n_tight': n_tight,
            'total_linear_MeV': total_at_j_linear,
            'total_cross_MeV': total_at_j_cross,
            'total_MeV': total_at_j,
        }
        total += total_at_j

        if wpath is not None:
            with open(wpath, 'w') as f:
                _json.dump({
                    'Z': Z, 'N': N, 'jet': j,
                    'k_cap': k_cap,
                    'partitions': parts_record,
                    'pairs': pair_records,
                    'n_tight': n_tight,
                    'total_linear_MeV': total_at_j_linear,
                    'total_cross_MeV': total_at_j_cross,
                    'total_MeV': total_at_j,
                }, f, indent=2, default=float)

    return total, per_jet


def atom_markov_trace(Z, N, k_cap=None, include_inter=True):
    """[DEPRECATED — Plancherel-weighted] "Markov" trace of atom braid.

    Computes Σ_λ (Plancherel-weight) · χ_λ(W)/d_λ.  At q ≠ 1 this is
    NOT the canonical Jones–Markov trace specified in
    prop:categorical-mass-markov (which gives tr_M(σ_0) = z ≈ 0.499).
    The Plancherel form gives ≈ 0.104 at q_0 — see the validity
    audit (rem:mass-endomorphism-tower-adjacency-audit).

    Use markov_trace_canonical.tr_M_element for the canonical
    axiomatic Markov trace that matches the prop's explicit table.

    Legacy form retained for existing callers; new code should route
    through binding_canonical.binding_canonical.

    Original docstring (Plancherel-specific):
    tr_M(W_atom) = Σ_λ w_λ · χ_λ(W_atom) / d_λ

    This is the CATEGORICAL MASS at a single brane level
    (prop:categorical-mass-markov, def:mass-identity): the categorical
    mass of the braid β representing the atom is exactly |tr_M(ρ(β))|.
    Yekutieli's 2D nonabelian Stokes theorem (Yekutieli 2015, Ch 5-6)
    identifies this with the multiplicative integral on SU(2) (or
    SU_q(2)).

    No prefactor tuning: the formula is dimensionally complete up to
    ONE archimedean calibration constant E_0 (the fibre functor
    τ: R → ℝ mapping categorical scalars to MeV).  Per
    prop:categorical-mass-markov: "To obtain physical masses in MeV,
    multiply by a calibration constant E_0, determined by matching one
    experimental value (e.g. the free neutron beta-decay Q-value)."

    Returns the (possibly complex) scalar tr_M(W_atom).

    include_inter : bool (default True)
        If False, returns the FREE-NUCLEON Markov trace (intra only).
    """
    import math as _math
    if k_cap is None:
        k_cap = K_PARTITION_MAX
    active = [e for e in _PARTITION_TABLE
              if e.get('k', 0) <= k_cap
              and e.get('dim', 0) >= 2
              and e.get('has_ysn', False)]
    # Include 1-dim (sym, alt) reps too — they contribute to Markov trace
    # even when they have y_λ = 0 in the LP.
    active_all = [e for e in _PARTITION_TABLE
                  if e.get('k', 0) <= k_cap
                  and e.get('has_ysn', False)]
    # Note: 1-dim reps have trivial YSN matrices (scalars) — already handled.
    chi_data = {}
    log_norms = {}
    for e in active_all:
        chi_q, ln, _d = atom_character_raw(Z, N, e,
                                           include_inter=include_inter)
        chi_data[tuple(e['partition'])] = (chi_q, ln, e)
        log_norms[tuple(e['partition'])] = ln
    if not log_norms:
        return 0.0
    max_ln = max(log_norms.values())
    trace = 0.0
    for lam, (chi_q, ln, entry) in chi_data.items():
        chi_eff = chi_q * _math.exp(ln - max_ln)
        d_l = entry['dim']
        w_l = entry['wedderburn_weight']
        # Linear Markov trace — NOT squared
        trace += w_l * chi_eff / d_l
    return trace


def atom_frobenius_norm_sq(Z, N, k_cap=None, include_inter=True):
    """Frobenius-norm squared of the atom braid word W_atom via Schur-Weyl:

        ||W||²_F = Σ_λ w_λ · |χ_λ(W) / d_λ|²

    where the sum is over Wedderburn blocks up to Hecke level k_cap.
    Uses the categorical self-duality of End_C(A) (rigid monoidal
    structure, fibre-functor rigidity).

    This scalar is the categorical measure of the atom braid's
    "size" — positive-definite, invariant under Markov moves,
    factorises over disconnected tensor products.

    Returns (norm_sq, per_partition_dict, log_norm_total).
    """
    import math as _math
    if k_cap is None:
        k_cap = K_PARTITION_MAX

    active = [e for e in _PARTITION_TABLE
              if e.get('k', 0) <= k_cap
              and e.get('dim', 0) >= 2
              and e.get('has_ysn', False)]

    per = {}
    # Compute chi_λ(W) for each active partition; rescale all to a
    # common log_norm to compare magnitudes.
    chi_data = {}
    log_norms = {}
    for e in active:
        chi_q, ln, _d = atom_character_raw(Z, N, e, include_inter=include_inter)
        chi_data[tuple(e['partition'])] = (chi_q, ln, e)
        log_norms[tuple(e['partition'])] = ln

    if not log_norms:
        return (0.0, {}, 0.0)

    max_ln = max(log_norms.values())
    norm_sq = 0.0
    for lam, (chi_q, ln, entry) in chi_data.items():
        # Rescaled χ to the common exponent max_ln
        chi_eff = chi_q * _math.exp(ln - max_ln)
        d_l = entry['dim']
        w_l = entry['wedderburn_weight']
        contrib = w_l * (chi_eff / d_l) ** 2
        per[str(lam)] = {
            'chi_rescaled': chi_eff,
            'dim': d_l,
            'weight': w_l,
            'contribution': contrib,
        }
        norm_sq += contrib
    return (norm_sq, per, max_ln)


def free_nucleon_frobenius_norm_sq(Z, N, k_cap=None):
    """Frobenius-norm squared of the free-nucleon baseline.

    "Free" means intra-nucleon crossings only — NO inter-nucleon
    crossings.  Disconnected tensor product W_nucleon_1 ⊗ ⋯
    ⊗ W_nucleon_A under the inclusion H_3(q)^⊗A ↪ H_{3A}(q).

    For the Frobenius norm in the Schur-Weyl formulation, the
    disconnected baseline is also the direct character sum over
    partitions, but computed on the braid word with inter-nucleon
    crossings REMOVED.  We compute this by running `atom_character_raw`
    on a modified entry where the crossing-chain omits inter-nucleon.

    Simpler approximation: compute χ_λ per nucleon separately and
    combine via branching-rule coefficients — for now, use the
    empirical simpler form: ||W_free||² = Σ_λ w_λ (i.e. the
    Wedderburn-trace identity normalization), which is the IDENTITY
    limit of the atom braid.

    TODO: proper tensor-product decomposition via H_3(q)^⊗A restriction.
    For now: ||W_free||² ≈ Σ_λ w_λ · 1 = 1 (Wedderburn trace identity).
    """
    norm_sq, _, _ = atom_frobenius_norm_sq(Z, N, k_cap, include_inter=False)
    return norm_sq
# Single calibration constant E_0 prescribed by prop:categorical-mass-markov
# as the dimensional bridge τ: R → ℝ from categorical mass to MeV.
# "To obtain physical masses in MeV, multiply by a calibration constant E_0,
#  determined by matching one experimental value (e.g. the free neutron
#  beta-decay Q-value)."


def binding_from_frobenius_pairing(Z, N, k_cap=None, *, canonical: bool = False):
    """Categorical binding via the mass-identity Markov trace formula.

        B_bulk(Z, N) = E_0 · ( |tr_M(W_free)| - |tr_M(W_atom)| )

    Derivation (prop:categorical-mass-markov, def:mass-identity):
    at a single brane level, the categorical mass of a braid β is
    m(β) = |tr_M(ρ(β))| — the absolute Markov trace.

    Trace selection:
      canonical=True  →  uses the axiomatic Jones-Markov trace
                         (markov_trace_canonical.tr_M_element) that
                         satisfies the Markov axioms and matches the
                         prop's explicit-values table exactly.
                         CORRECT per the prop.  Slow (>100s on D);
                         prohibitive on heavy atoms with current
                         implementation.
      canonical=False →  uses the LEGACY Plancherel-weighted form
                         Σ_λ w_λ · χ_λ(W)/d_λ (atom_markov_trace).
                         This is NOT the prop's Markov trace — it
                         gives tr_M(σ_0) ≈ 0.104 at q_0 instead of
                         z ≈ 0.499.  Retained as default for
                         backward compatibility with existing
                         witness data; migrate to canonical=True
                         when possible.

    Yekutieli's 2D nonabelian Stokes theorem (Yekutieli 2015) gives
    the Markov trace as the nonabelian multiplicative integral of
    the connection over the surface of the braid closure — a
    categorical action functional.  NO prefactor tuning.

    Note: categorical-mass-markov explicitly warns that single-level
    Markov trace does NOT reproduce mass ratios like m_μ/m_e ≈ 206.8;
    those require the FULL brane tower sum Σ ‖Φ_q(z_i)‖ over
    exceptional divisors.  Current implementation is single-level
    only.  Extension to the full tower sum is conj:mass-endomorphism.
    """
    if canonical:
        import sys as _sys
        from pathlib import Path as _Path
        _sys.path.insert(0, str(_Path(__file__).parent))
        from binding_canonical import binding_canonical as _canon
        r = _canon(Z, N, E_0=E_0_CALIBRATION_MEV)
        if r.get("status") != "solved":
            # Fall back to Plancherel on failure (e.g.
            # NotImplementedError for complex braid patterns).
            atom_tr = atom_markov_trace(Z, N, k_cap, include_inter=True)
            free_tr = atom_markov_trace(Z, N, k_cap, include_inter=False)
            return E_0_CALIBRATION_MEV * (abs(free_tr) - abs(atom_tr))
        return r["B_MeV"]
    # Legacy Plancherel path (default).
    atom_tr = atom_markov_trace(Z, N, k_cap, include_inter=True)
    free_tr = atom_markov_trace(Z, N, k_cap, include_inter=False)
    return E_0_CALIBRATION_MEV * (abs(free_tr) - abs(atom_tr))


def sdp_cross_channel_contribution(Z, N, k_cap=None, jet_max=None):
    """Compute SDP-derived cross-channel energy contribution (MeV).

    Runs the SDP with atom observables over all active conjugate pairs
    (both partitions at k ≤ k_cap, jet ≤ jet_max, both mixing).
    Each pair's coupling c_ij* contributes c_ij × m_e to the binding
    energy via the categorical identity

        ΔB_pair = m_e · |c_ij*|

    Self-conjugate partitions get the Wigner-2 h/2 contribution
    as the diagonal coupling.

    Returns total contribution (MeV) and per-pair breakdown.
    """
    if k_cap is None:
        k_cap = K_PARTITION_MAX
    try:
        from sdp_cross_channel import sdp_with_atom_observables
    except ImportError:
        return 0.0, []

    active = [e for e in _PARTITION_TABLE
              if e.get('k', 0) <= k_cap
              and e.get('dim', 0) >= 2
              and e.get('has_ysn', False)
              and (jet_max is None or e.get('jet', 0) <= jet_max)]

    # Build pair list (non-self-conjugate); self-conjugate handled via h/2
    pair_couplings = []
    self_conj_indices = []
    seen = set()
    h_val = float(h)
    name_to_idx = {tuple(e['partition']): i for i, e in enumerate(active)}
    for i, e in enumerate(active):
        lam = tuple(e['partition'])
        conj = partition_conjugate(lam)
        if conj == lam:
            self_conj_indices.append(i)
            continue
        if conj not in name_to_idx:
            continue
        j = name_to_idx[conj]
        key = frozenset({i, j})
        if key in seen:
            continue
        seen.add(key)
        pair_couplings.append((i, j, h_val))

    if not active:
        return 0.0, []

    sol = sdp_with_atom_observables(Z, N, active, pair_couplings)
    if sol.get('status') not in ('optimal', 'optimal_inaccurate'):
        return 0.0, []

    # Sum |c_ij| across pairs, scale by m_e
    total_mev = 0.0
    per_pair = []
    for cb in sol['cross_blocks']:
        c = cb['c_ij']
        contribution = M_E_MEV * abs(c)
        total_mev += contribution
        per_pair.append({
            'lambda_i': cb['lambda_i'],
            'lambda_j': cb['lambda_j'],
            'c_ij': c,
            'contribution_MeV': contribution,
        })

    # Self-conjugate h/2 contribution (Wigner-2)
    for i in self_conj_indices:
        e = active[i]
        mu = e['q_laplacian_eigenvalue']
        # Self-conj partition: effective coupling at Wigner-2 scale
        #   h/2 · w_λ · m_e (matches DELTA_W2 formula)
        w_lam = e['wedderburn_weight']
        contribution = M_E_MEV * w_lam * h_val / 2.0
        total_mev += contribution
        per_pair.append({
            'lambda_i': list(e['partition']),
            'lambda_j': list(e['partition']),
            'c_ij': h_val / 2.0,
            'self_conjugate': True,
            'contribution_MeV': contribution,
        })

    return total_mev, per_pair


def binding_energy(Z, N, *, sdp=True, frobenius=True):
    """Binding energy (MeV) via the categorical path.

    B = unified_iterative_correction(Z,N)                      [LP-dual shadow]
      + sdp_cross_channel_contribution(Z,N)    (if sdp)        [SDP couplings]
      + binding_from_frobenius_pairing(Z,N)    (if frobenius)  [Markov trace]

    Replaces the retired 11-term Bethe-Weizsäcker formula path.
    """
    A = Z + N
    if A <= 1:
        return 0.0
    B = unified_iterative_correction(Z, N)
    if sdp:
        sdp_contrib, _ = sdp_cross_channel_contribution(Z, N)
        B += sdp_contrib
    if frobenius:
        B += binding_from_frobenius_pairing(Z, N)
    return B


def q_value_beta(Z_parent, N_parent):
    """Q-value (MeV) for beta⁻ decay: (Z,N) → (Z+1,N-1) + e⁻ + ν̄_e.

    Transfer matrix on nuclear strands (no electrons):
        Q = E_× · μ₀ · |ΔΦ₁|
    where Φ₁ = Σᵢ ln|V̂ᵢ| computed over nucleon strands only.
    Uses pp..nn ordering; for A>14, tries Rust engine for
    ground-state optimized ordering.
    """
    Z_d, N_d = Z_parent + 1, N_parent - 1
    if N_parent <= 0:
        return 0.0

    # Transfer matrix on nuclear strands only (matches
    # all-nuclei-transfer-matrix.py which gives 9.5% for ¹⁴C)
    phi_parent = _phi1_nuclear(Z_parent, N_parent)
    phi_daughter = _phi1_nuclear(Z_d, N_d)
    delta_phi = phi_daughter - phi_parent
    mu_0 = M_E_MEV / (3.0 * E_CROSS)
    return E_CROSS * mu_0 * abs(delta_phi)


def atom_mass(Z, N):
    """Compute atomic mass (MeV) via transfer matrix.

        M = Z·m_p + N·m_n + Z·m_e + κ·Φ₁

    where Φ₁ = Σᵢ ln|V̂ᵢ| is the Skein polynomial log-volume summed
    over the atom's nucleon strands (zero-parameter, not BW).

    Returns (M_MeV, phi1).
    """
    M_const = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV
    phi = compute_phi1_full(Z, N)
    return M_const + KAPPA * phi, phi

