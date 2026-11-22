# DEPRECATION-CANDIDATE: Phase-5 exploratory surface, kept in place
# because 9 live importers (5 in computations/ + 4 in
# tools/pyhecke/python/pyhecke/) still depend on its symbols. Revisit
# when the live importers are themselves retired or rewired to the
# canonical surface. Previously lived at _deprecated/hecke_core_legacy.py;
# moved out 2026-06-01 to match the existing 23-candidate convention
# (DEPRECATION-CANDIDATE banner in computations/,
# not under _deprecated/).
"""hecke_core_legacy — Phase-5 EXPLORATORY surface of hecke_core.py.

Carved out per the canonical-vs-exploratory audit
(docs/audits/2026-05-24-hecke-core-canonical-audit.md).

Symbols here are NOT on the canonical derivation chain
(docs/canonical-derivation-cheat-sheet.md). They are kept for
reproducibility of historical Phase-5 results and for the
in-repo consumers that still import them.

**Direct importers** (computations/):

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
import math  # float64-ok: integer math.factorial and legacy boundary helpers
import json as _json
import os as _os
import sys as _sys
from pathlib import Path as _Path
from fractions import Fraction
import numpy as np  # float64-ok: object-dtype arrays and Clarabel/scipy SDP interface

from q_parameter import Q as q0, Q_INV as qi, HA as h, q_int, E_CROSS
# EXACT twins of q0/qi/h.  The float64 names above stay for the many
# call sites that are display or float-domain; the seminormal builder
# uses ONLY these (AGENTS.md: never compute in float).
from q_parameter import Q_MP as _Q_MP, Q_INV_MP as _QI_MP, HA_MP as _H_MP
from mpmath import mp as _mp


# ── Exact q-integer (owner directive 2026-09-12, "excise float64") ────
# `q_int` imported above is FLOAT64: `q_parameter.Q` is a Python float and
# `q_int(n) = (Q**n - Q_INV**n) / HA` is float arithmetic end to end.  Every
# quantity built out of it is float64-valued no matter what type it carries --
# `q_hook_product` and `q_factorial` return `mpf` and accumulate
# `mp.mpf(1) * q_int(k)`, which is a float64 number in mpf clothing.
#
# `_q_int_mp` is the same symmetric bracket over `_Q_MP`, the module's single
# mpf q -- the SAME constant the seminormal builder uses.  Deliberately the
# same one rather than a fresh `q_at(dps)` solve: a character and the YSN
# matrices it is the character OF must be evaluated at one q, and two mpf q's
# in one table is a straddle even at 1e-52.
#
# `_Q_MP` carries the 50 digits of `Q_50_DIGIT_STR`, so it is a ~1e-52 ceiling
# on a COMPUTE_DPS = 70 compute -- BELOW `OUTPUT_DPS = 60`, i.e. a value
# serialized at 60 digits from it has ~8 padded digits.  That is a real
# residual and it is recorded, not fixed here (bean `qou-oiz3`); it is 36
# orders of magnitude tighter than the float64 path it replaces.
#
# NOT `_Q_FRAC` from `pyhecke.gram`: that is the engine's rational `1.11`
# (3 significant figures, measured 1.93e-5 from the anchor) and exists for
# exact-rational Hecke reduction, not for numerics.
def _q_int_mp(n: int):
    """Symmetric quantum integer [n]_q = (q^n − q^−n)/(q − q^−1) in mpmath
    arithmetic at the ambient working precision.

    The mpf twin of the float64 `q_int`.  Defined for every integer n
    including 0 and negatives ([0]_q = 0, [−n]_q = −[n]_q), which the
    q-Laplacian needs: the content c(□) = col − row runs negative.

    Carries no memo: mpmath rounds to the AMBIENT `mp.dps`, so a cached
    value computed under one working precision would be silently reused
    under another -- the defect `unified_iterative_correction`'s own
    `workdps` wrapper exists to stop.
    """
    return (_Q_MP ** n - _QI_MP ** n) / _H_MP


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
    # `G_INV` is gone under convention D — the form is singular, so the 6x6
    # inverse does not exist. `G_PINV` is the inverse on the quotient
    # H_3(q)/rad, and `RADICAL` is the null direction it quotients by.
    G, G_PINV, RADICAL,
    _H_FRAC, _Z_FRAC, _TR_M_FRAC, _SYM_EIG_FRAC, _ALT_EIG_FRAC,
    _Q_FRAC, _QI_FRAC,
)
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from experimental_constants import m_n_derived_3input  # noqa: E402

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

# Canonical p-n interface offset (owner ruling 2026-08-15 R3, reaffirmed
# 2026-08-26): `bring_color_weighted`. Imported, not open-coded, so there is
# one definition; the import is hard on purpose because a fallback would
# compute the COLOUR-BLIND convention while reporting success.
#
# CORRECTED 2026-09-07. This comment read "`-h/2` is `strict_averaged`, the
# COLOUR-BLIND convention" as though that were what R3 made canonical. R3 made
# `bring_color_weighted` canonical, and `strict_averaged` is the blind one the
# next sentence warns about — so the note named the wrong convention as the
# ruling's outcome. Measured, live: `pyhecke.constants.PN_CONVENTION` is
# `bring_color_weighted`, and the two are NOT interchangeable at this q0 —
# `_pn_d(h) = -0.10445824776972631` against `-h/2 = -0.10453014939781966`,
# 6.9e-4 relative apart, which is 12 orders of magnitude above the framework's
# 1 ppQ L1 target. Do not "simplify" `_pn_d(h)` to `-h/2`.
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402

#: Working digits for every EXACT crossing coefficient in this module — both
#: the inter-nucleon offsets below and the decimal strings `_lp_kernel_steps`
#: hands the Rust kernel.  50 to match `Q_50_DIGIT_STR` and the `prec` the
#: kernel is asked for, plus the repo's usual 10-digit guard so a coefficient
#: is never rounded AT the precision it is about to be used at.
_EXACT_COEFF_DPS = 60

# EXACT inter-nucleon crossing offsets.
#
# The float64 twins `-h` and `_pn_d(h)` are what `_step_chain_22` and
# `_step_chain_generic` used until 2026-09-07 (bean `qou-sv7h`, finding 4),
# while the INTRA-nucleon tables `_PROTON_G1` / `_NEUTRON_G1` have carried
# exact `mpf` throughout.  So a single matrix product mixed 50-dps intra
# crossings with 16-digit inter crossings — the layer straddle AGENTS.md
# forbids ("a float64 input poisons the whole result"), inside one product.
#
# The `workdps` is not decoration: mpmath rounds every operation to the
# AMBIENT working precision, which is 15 dps in a bare import of this module.
# `_pn_d(_H_MP)` evaluated outside this block inverts h to q and takes a square
# root, and every one of those steps would round back to 15 digits —
# reintroducing inside the offset exactly the narrowing the exact twin exists
# to avoid.
with _mp.workdps(_EXACT_COEFF_DPS):
    _NN_D_MP = -_H_MP           # nn crossing offset (−ℏ_q)
    _PN_D_MP = _pn_d(_H_MP)     # pn crossing offset (bring_color_weighted)

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

        μ_λ(q) = Σ_{□ ∈ λ} [c(□)]_q × [c(□) + 1]_q

    where c(□) = col − row is the content of cell □ and [k]_q is the
    SYMMETRIC q-integer (q^k − q^−k)/(q − q^−1).  No ℏ_q² prefactor.

    DERIVED (2026-11-16, issue #8091; docs/audits/
    2026-11-16-binding-reeb-holonomy-laplacian.md).  This is the block
    eigenvalue of the Reeb-holonomy Laplacian
        (q − q⁻¹)⁻² Σ_k (q·L_k + q⁻¹·L_k⁻¹ − (q + q⁻¹)),
    with L_k the relative full twist (Lean:
    QOU.BraidKnot.Hecke.reebLaplacianB_smul_of_weight,
    fullTwistB_succ_eq_mul_jmRawB; centrality
    QOU.SchurWeyl.contentCasimir_comm_σ).  The Reeb part of Δ_q enters
    with weight (q⁻¹ + ℏ_q)² = 1, not ℏ_q²: on a mode with no horizontal
    derivative d_q and δ_q reduce to d and δ.  So the bare sum below is
    the derived value; the paper's former ℏ_q² and Jackson integers were
    corrected to match it.  No number changed in this function.

    PRECISION (2026-09-12, owner directive "excise float64"; bean
    `qou-oiz3`).  This accumulated `casimir_sum = 0.0` over the FLOAT64
    `q_int`, so μ_λ carried 53 bits.  It is now `_q_int_mp` end to end and
    returns an `mpf`.  The measured move on the resolvent scale
    C_λ = m_e·H_q(λ)·y_λ·ρ_λ(s_*) is at most 3.55646e-16 relative over the
    31 contributing blocks at k ≤ 7 -- the floor of the arithmetic it
    replaces, which is a bound on the damage and NOT evidence the old path
    was correctly rounded.  See PR #7237 / bean `qou-t6be`, which found this
    and deliberately left it.
    """
    lam = list(partition)
    if not lam:
        return _mp.mpf(0)
    # Reeb-holonomy Laplacian eigenvalue: Σ [c]_q[c+1]_q, symmetric integers,
    # no ℏ_q² (derived; see the docstring).
    casimir_sum = _mp.mpf(0)
    for i, li in enumerate(lam):
        for j in range(li):
            c = j - i
            casimir_sum += _q_int_mp(c) * _q_int_mp(c + 1)
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

    PRECISION (2026-09-12, "excise float64"): `s` defaulted to the float64
    `(q0 - 1.0)/q0` and the quotient was a float64 `1.0 / (mu + s)`.  Both
    are now mpf; a caller-supplied `s` is promoted with `mpf(str(s))` so a
    float64 argument is carried at the value it states rather than at its
    binary tail.
    """
    if s is None:
        # Default: Planck-step Reeb time scale s_* = (q − 1) / q
        s = S_REEB_PLANCK
    elif not isinstance(s, _mp.mpf):
        s = _mp.mpf(str(s))
    mu = q_laplacian_eigenvalue(partition)
    return 1 / (mu + s)


def lp_shadow_price(partition):
    """Per-partition weight y_λ used by the binding accumulator at level
    k = |λ|.  NAMED for the LP shadow price; it is not one.

        y_λ = w_λ / d_λ − y_0,   y_0 = min_λ (w_λ / d_λ) = 1/[k]_q!

    with d_λ = dim(λ), the classical dimension (number of standard Young
    tableaux).

    CORRECTED 2026-09-05 (owner ruling; PR #6752).  This docstring said y_0
    "is the dual variable of the normalisation constraint 1ᵀx = n_target".
    That is false, in two independent ways:

      * This function solves no program.  It evaluates a closed form.  The
        subtrahend 1/[k]_q! is exactly min_λ(w_λ/d_λ) — a normalisation of
        the weights, not a dual variable of anything.

      * The actual net-constraint dual of prop:operator-selection-lp is
        IDENTICALLY ZERO, for every n_target, at every n and q.  The NF
        basis contains the identity, so the first Frobenius row IS the
        objective vector; the program minimises t·x subject to t·x ≥ 0, so
        its optimal value is 0 and strong duality forces y_0* = 0.  Proved
        in the content block (commit 6b7d2ec4a8) and in Lean
        (`y_0_eq_zero_of_radical`); confirmed by every committed solve.
        Measured here, y_0 runs 0.497 at k=2 to 1.56e-4 at k=7 — never 0,
        so it cannot be that dual under any reading.

    What the term DOES do, measured at k = 2..7: subtracting min_λ(w_λ/d_λ)
    zeroes exactly the two one-dimensional blocks (k) and (1^k) — the
    trivial and sign representations — and nothing else.  Note those are
    precisely the blocks where a SCALAR dual would be well-typed at all;
    for d_λ > 1 the Frobenius dual is a d_λ × d_λ matrix.  It is also not
    needed for non-negativity: w_λ/d_λ > 0 already.

    Consumers should read this as a weighting choice with a measured
    effect, not as a priced constraint.  The replacement program is
    tracked as O3′ (block SDP on the radical quotient); nothing here is
    changed by that work.
    See docs/proposals/2026-09-05-operator-selection-objective-replacement.md
    and beans qou-sv7h / qou-8na1.

    The shadow price y_λ multiplies the categorical scale C_λ = m_e ·
    H_q(λ) to produce a per-partition binding contribution
    Δ B_λ = y_λ · C_λ · S_λ(Z, N, A) (BW formula factorisation).

    Reference: prop:mass-coefficient-shadow-price.
    """
    k = sum(partition)
    if k == 0:
        return _mp.mpf(0)
    d = partition_dimension(partition)
    if d == 1:
        # For the two one-dimensional blocks (k,) and (1^k) of H_k(q),
        # H_q(λ) == [k]_q! identically, so d_q(λ) == 1 and w_λ / d_λ == 1/[k]_q! == y_0
        # is an exact algebraic identity (bean qou-f2pf). Evaluating
        # (q_factorial(k)/q_hook_product(λ))**2 / q_factorial(k) - 1/q_factorial(k)
        # left a ~4.3e-19 1-ulp residue on 6 of the 20 one-dimensional blocks
        # (k = 6, 7, 9) where q_hook_product multiplied [k]_q..[1]_q in reverse order.
        return _mp.mpf(0)
    w = wedderburn_weight(partition)
    # y_0 is the smallest of w_λ/d_λ across all partitions of k.
    # For the trivial (n) partition (sym): w = 1/[n]_q!, d = 1.
    # So y_0 = 1/[n]_q!.  NOT the LP normalisation dual — that one is
    # identically 0 (see this function's docstring).  It is a weight
    # normalisation whose measured effect is to zero (k) and (1^k).
    y_0 = _mp.mpf(1) / q_factorial(k)
    return w / d - y_0


# Pre-compute all partitions of k = 2..K_PARTITION_MAX with q-hook,
# weight, dimension, shadow price.  The live cap is 11, one line below,
# and every production call site passes it as the default: :1724/:1725,
# :1750/:1751 (the two accumulator signatures) and :2727, :2901, :2949,
# :3090 (`k_cap = K_PARTITION_MAX`).  That is
# sum_{k=2}^{11} p(k) = 193 partitions.
#
# REWRITTEN 2026-09-12 (bean `qou-xkjt`).  What stood here named THREE
# different values for this one constant and got its own arithmetic wrong:
#
#   - "K = 6 covers H2..H6 (24 partitions in total: 2 + 3 + 5 + 7 + 11)"
#     — that sum is 28, not 24.  (Those are p(2..6); at the live cap it is
#     193.)  Both sums verified by direct computation.
#   - "K_PARTITION_MAX is capped at 8 because empirical sweeps show the"
#     — a sentence truncated mid-clause, with no verb.
#   - "Empirical sweep with q-heat resolvent damping (post-PR #368) shows
#     K = 6 is the OPTIMAL partition cutoff — extending to k = 7, 8, 9
#     introduces sub-leading spectral modes that degrade accuracy (e.g.
#     40Ca: 0.001 at K=6 -> 0.012 at K=9)."
#   - and `K_PARTITION_MAX = 11`.
#
# THE SWEEP WAS RUN, IT RECOMMENDED 6, AND 6 WAS NOT ADOPTED.  Measured:
# no production caller truncates at 6.  The only live `k=6` call sites are
# `probes/uic_per_block_log_valley_scan_probe.py:167-168`, which pass
# `k_max=6` and `k_max=11` side by side precisely to COMPARE them, and
# `_deprecated/heavy_atom_opts.py:280` (a different parameter).  The
# accuracy figures the old text cited ("40Ca: 0.001 at K=6 -> 0.012 at
# K=9") appear nowhere else in the tree — no witness, no producer, no
# audit.  Comment-only.
#
# RECORD IT AS THE HONEST NEGATIVE IT IS.  "Sweeping a discrete parameter
# for accuracy" is named verbatim as fitting in AGENTS.md "NO FITTING,
# EXCEPT CAL-1/2/3", and accuracy is explicitly not the ranking criterion
# there.  So the correct reading of the sweep is: a cutoff selected
# against the data was measured to be more accurate, and was REJECTED in
# favour of the full compiled partition set.  That is the discipline
# working, not a fit — but the old wording read as an endorsement, and an
# agent running the anti-fit audit reported a live fit in the binding
# compute on the strength of it.
#
# The channel inventory the old text listed (volume, surface, Coulomb,
# asymmetry, pairing, exchange, shell, hook, Wigner, form factor, pn
# correlation, [3,2,1] pn-invisible, [4,1,1]+[3,1,1,1] isospin,
# [4,2]+[2,2,1,1] codim-4 form factor) is retained: those are the
# Wedderburn channels that carry a BW term, and they live at k <= 6.  At
# the live cap of 11 they are a subset of what is enumerated, not the
# whole of it.
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

    CLOSED FORM (replaced a factorial enumeration, 2026-09-05, bean
    `qou-i7ju` / `qou-r4w5`).  This used to enumerate every SYT of shape λ
    — f^λ of them — to obtain these counts.

    WHERE THIS ACTUALLY HELPS, measured (and it is NOT the low-A atoms —
    do not read this as unblocking the table on its own):

        atom        A   n=3A   partitions   total SYTs enumerated   max f^λ
        deuterium   2      6           11                      76        16
        ⁴He         4     12           77                 140,152     7,700
        ⁷Li         7     21          792     119,952,692,896  1,118,939,184

    The old enumeration over ALL partitions of n = 6 costs 0.0002 s, so
    deuterium is untouched by this change and its cost lies elsewhere
    (`qou-r4w5`, `qou-sv7h`).  At n = 21 it is 1.2e11 tableaux — not slow
    but impossible.  This removes an ABSOLUTE wall at high A; it is
    necessary, not sufficient, for the 19-atom table to finish.

    Two facts make the enumeration unnecessary, both verified exhaustively
    against the old code on every partition of n = 1..10 (138 partitions,
    0 mismatches) in `probes/syt_12_relation_closed_form_probe.py`:

    * **`n_mix` is structurally 0.**  In a standard Young tableau entries
      increase along rows and columns, so 1 occupies (0,0) and 2 must take
      an addable cell of the one-cell shape — (0,1) or (1,0).  "Neither"
      cannot occur.  (The old `fill` enforced exactly this, then spent
      f^λ steps discovering it.)
    * **The surviving two counts are closed-form.**  With f = f^λ from the
      hook-length formula and `Sum_c` the sum of contents c(i,j) = j − i,
      the q = 1 eigenvalues of the generator are +1 (row) and −1 (column),
      so `n_row − n_col` is the symmetric-group character on a
      transposition — the classical content result
      `χ^λ((12)) = f · Sum_c / C(n,2)`.  With `n_row + n_col = f`:

          n_row = f · (1 + Sum_c / C(n,2)) / 2
          n_col = f · (1 − Sum_c / C(n,2)) / 2

    Exact integer arithmetic throughout; `Fraction` guards the division so
    a non-integral result raises rather than silently rounding.
    """
    n = sum(partition)
    if n < 2:
        return (0, 0, 0)

    # f^λ by the hook-length formula
    conj = [sum(1 for row in partition if row > j) for j in range(partition[0])]
    denom = 1
    for i, row in enumerate(partition):
        for j in range(row):
            denom *= (row - j) + (conj[j] - i) - 1
    f_lambda = math.factorial(n) // denom

    # Σ contents, c(i,j) = j − i
    sum_c = sum(j - i for i, row in enumerate(partition) for j in range(row))

    ratio = Fraction(sum_c, math.comb(n, 2))
    n_row = Fraction(f_lambda) * (1 + ratio) / 2
    n_col = Fraction(f_lambda) * (1 - ratio) / 2
    if n_row.denominator != 1 or n_col.denominator != 1:
        raise ArithmeticError(
            f"_count_syts_by_12_relation: non-integral counts for {partition} "
            f"(n_row={n_row}, n_col={n_col}) — the closed form's hypotheses "
            f"do not hold here; do not round."
        )
    return (int(n_row), int(n_col), 0)


def partition_character_sigma1(partition):
    """Character χ_λ(σ_1) of the first Hecke generator in irrep λ.

    Derived from YSN eigenvalue structure:
        χ_λ(σ_1) = q · n_row + (-q⁻¹) · n_col + h · n_mix_pairs
    where n_row / n_col / n_mix_pairs are SYT counts by (1,2)-relation.

    PRECISION (2026-09-12, "excise float64"): the SYT counts are exact
    integers (`_count_syts_by_12_relation` guards them with `Fraction`), and
    this then multiplied them by the float64 `q0` / `qi` / `h`, throwing the
    exactness away in the last line.  Now over `_Q_MP` / `_QI_MP` / `_H_MP`.
    """
    nr, nc, nm = _count_syts_by_12_relation(partition)
    return _Q_MP * nr + (-_QI_MP) * nc + _H_MP * nm


def partition_spectral_log_rate(partition):
    """Average per-crossing log spectral rate for partition λ:
        ρ_λ = |χ_λ(σ_1)| / d(λ).
    The log of this, ln ρ_λ, is the LEADING rate at which a random
    braid word's trace in λ accumulates: ln|Tr M_λ(W_N)| ≈ ln d(λ) + N ln ρ_λ.
    (For partitions where ρ_λ < 1, the character ratio is less than
    unity and the trace shrinks exponentially — consistent with the
    partition being "far from the mean" in the Plancherel sense.)

    PRECISION (2026-09-12, "excise float64"): `math.log` returns a Python
    float WHATEVER it is handed, so this narrowed an mpf ratio to 53 bits in
    its last line.  `_exact_log` instead, which carries its own `workdps` --
    the ambient `mp.dps` is 15 in a bare import of this module, so a bare
    `mp.log` would trade a float64 narrowing for a 15-digit one.
    """
    d = partition_dimension(partition)
    if d == 0:
        return _mp.mpf(0)
    chi = partition_character_sigma1(partition)
    ratio = abs(chi) / d
    return _exact_log(ratio) if ratio > 0 else _mp.mpf(0)


# Canonical Reeb-time spectral parameter s_*.
# The Peter-Weyl formula (prop:q-heat-kernel-peter-weyl) gives
# u(t) = Σ d_λ exp(−μ_λ t) π_λ(u₀), and its Laplace transform
# ℒ[u](s) = Σ d_λ (μ_λ + s)⁻¹ π_λ(u₀) is the resolvent.
# The natural spectral parameter for the nuclear binding problem
# is s_* = (q−1)/q = ℏ_q (the quantum Planck constant), which is
# the natural scale at which the JM Casimir (μ_λ ∈ [2, 190] for
# k ≤ 9) provides O(1)–O(0.005) differentiation across the
# partition spectrum via ρ_λ = 1/(μ_λ + s_*).
#
# PRECISION (2026-09-12, owner directive "excise float64"; bean `qou-oiz3`).
# This read `(q0 - 1.0) / q0` over the FLOAT64 `q0`, so the spectral
# parameter of every resolvent weight carried 53 bits.  Over `_Q_MP` the
# value moves 1.99757e-16 relative -- the float64 floor, so it BOUNDS the
# damage and is not evidence the old constant was correctly rounded.
#
# The explicit `workdps` is load-bearing and not decoration: this line runs at
# MODULE IMPORT, where the ambient `mp.dps` is mpmath's default 15, so a bare
# mpf quotient here would trade a float64 constant for a 15-digit one and buy
# nothing.  Same reason `_exact_log` carries one.
with _mp.workdps(_EXACT_COEFF_DPS):
    S_REEB_PLANCK = +((_Q_MP - 1) / _Q_MP)


def _partition_table() -> list[dict]:
    """Materialise _PARTITION_TABLE_CACHE on first access. ~30 s cold.

    PRECISION (2026-09-12, "excise float64"; bean `qou-oiz3`).  The body is
    wrapped in `workdps(COMPUTE_DPS)` for a reason that is specific to a
    CACHE: mpmath rounds every operation to the AMBIENT `mp.dps`, which is 15
    in a bare import of this module, and this table is built ONCE and reused
    for the life of the process.  So the precision of every mpf in it was a
    function of WHO TOUCHED IT FIRST -- 70 digits when
    `unified_iterative_correction` got there first (it has its own `workdps`),
    15 when any other consumer did, and no signal either way.  That is not a
    hypothetical: `_ensure_ysn_attached` and eight probes reach
    `_PARTITION_TABLE` outside any precision context.
    """
    global _PARTITION_TABLE_CACHE
    if _PARTITION_TABLE_CACHE is not None:
        return _PARTITION_TABLE_CACHE
    from _precision import COMPUTE_DPS as _CDPS
    with _mp.workdps(_CDPS):
        return _partition_table_exact()


def _partition_table_exact() -> list[dict]:
    global _PARTITION_TABLE_CACHE
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
            _rho = abs(_chi) / _d if _d > 0 else _mp.mpf(0)
            # `_exact_log`, not `math.log`: `math.log` returns a Python float
            # WHATEVER it is handed, so on an mpf it discards every digit past
            # the 16th (see `_exact_log`'s docstring).  The -30 floor is the
            # table's own sentinel for an unrepresentably small rate and is
            # deliberately NOT a computed log.
            _log_rho = _exact_log(_rho) if _rho > 1e-300 else _mp.mpf(-30)
            # q-Laplacian eigenvalue and resolvent weight (def:q-heat-equation,
            # def:categorical-laplace-transform): categorical damping derived
            # from the q-heat spectrum rather than the Kerov Plancherel measure.
            _mu = q_laplacian_eigenvalue(_lam)
            _resolvent = (1 / (_mu + S_REEB_PLANCK)
                          if (_mu + S_REEB_PLANCK) > 0 else _mp.mpf(0))
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
Y_22 = lp_shadow_price((2, 2))                     # per-partition weight of (2,2)


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
        # V̂_e = V_std, the convention-D Markov trace (was the w_sym/w_std/w_alt mixture)
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
        # Convention D (owner, 2026-11-18): the Markov trace of a*sigma+b is z*a+b.
        _V_e = _V_std
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
    # Exact coefficients, matching the intra tables above (see `_NN_D_MP`).
    for ti in prev_types:
        if ti == 'p' and nucleon_type == 'p':
            chain.append((1, 0, 3))          # pp
        elif ti == 'n' and nucleon_type == 'n':
            chain.append((1, _NN_D_MP, 3))   # nn
        else:
            chain.append((1, _PN_D_MP, 3))   # pn
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
# (class function).
#
# 🛑 THAT DOES NOT EXTEND TO A WORD, and this comment said it did until
# 2026-09-12 (bean `qou-w6x3`).  It read: "…so any embedding of crossings into
# σ_1, σ_2, … yields the same trace."  The premise is true — all σ_k are
# conjugate — and the conclusion is false, because χ is a class function on the
# GROUP, not a function of the multiset of letters: χ_λ(σ_1 σ_2) ≠ χ_λ(σ_1 σ_3)
# in general, since σ_1 σ_2 and σ_1 σ_3 are not conjugate.
#
# Measured, at the one place both embeddings of the binding word exist.  The
# deuteron word under the fixed-H_k embedding and under the 3A embedding are
# the SAME 23 letters in the SAME H_6, with the same (c, d) offsets, differing
# only in which generator each letter is assigned to.  χ^λ then differs on 9 of
# the 11 partitions of 6 — max relative 1.43, and λ = [5,1] goes −0.827 →
# +3.216, a sign change.  Only the two 1-dimensional irreps are blind to the
# embedding (ρ(σ_i) = q resp. −q⁻¹ independent of i, so χ = Π(q + d)).
# `computations/probes/binding_word_3A_reembedding_probe.py`, 18/18.
#
# Why this mattered: the sentence, read at face value, says a re-embedding is
# free.  It is not — it is a re-derivation, and every recorded binding number
# would move.  `docs/audits/2026-09-12-binding-word-3A-reembedding.md`.
#
# `_step_chain_22`'s docstring above makes the NARROW version of this claim,
# for λ = (2,2) only, and that one is TRUE — but for a stronger reason than it
# gives.  In λ = (2,2) the matrices ρ(σ_1) and ρ(σ_3) are EQUAL (both
# diag(q, −q⁻¹)), so σ_1 ↔ σ_3 may be substituted inside any word.  Equal
# characters of single generators would not have sufficed.

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


class _ExactCOO:
    """A sparse sigma whose entries are EXACT (`mpmath.mpf`), not float64.

    scipy's sparse containers are float64 by construction and their kernels
    reject `dtype=object`, so an exact seminormal family cannot be carried in
    a `csr_matrix` at all.  This holds the same COO triple the consumers
    already densify against, with `mpf` values.

    Deliberately NOT a scipy type: `scipy.sparse.issparse` must return False
    for it, so a consumer cannot route it into a float64 BLAS call.
    """

    __slots__ = ("row", "col", "data", "shape")

    def __init__(self, row, col, data, shape):
        self.row, self.col, self.data, self.shape = row, col, data, shape

    def tocoo(self):
        return self

    @property
    def nnz(self):
        return len(self.data)


def _is_sparse_sigma(x):
    """True for the sparse sigma carrier, which is `_ExactCOO` alone.

    This tested `scipy.sparse.issparse(x)` as well until 2026-09-11.  That
    arm was unreachable, and it is removed rather than kept as a defensive
    check: a guard against a state the code cannot enter reads to the next
    author as evidence that it can.

    Three facts close it, and all three are needed:

    1. `_build_ysn_matrices_exact` emits `_ExactCOO` or a dense tuple of
       `mpf`, and nothing else — #6794 changed the sparse emit precisely
       because `csr_matrix` is float64 and cannot hold an `mpf`.
    2. `csr_matrix(` is CALLED nowhere in this file.
    3. `entry['ysn']` is assigned in exactly one place
       (`_ensure_ysn_attached`), from `_build_ysn_matrices`; all three
       dispatch sites read `entry['ysn']` and none takes a sigma family as
       a parameter, so no caller can inject one.

    MEASURED over the whole `_PARTITION_TABLE`, every sigma rather than
    `[0]` of each family: **1528 matrices — 408 dense tuples, 1120
    `_ExactCOO`, 0 scipy, 0 carrying `.toarray`.**

    The 25 other `csr_matrix` sites under `computations/` build their own
    matrices in their own modules and never reach this dispatch.
    """
    return isinstance(x, _ExactCOO)


def _build_ysn_matrices(partition, sparse_threshold=32):
    """Exact seminormal matrices, computed at the canonical working precision.

    Thin wrapper: the arithmetic below is `mpf`, but mpmath rounds every
    operation to the AMBIENT `mp.dps`, which is **15** in a bare import of
    this module -- exactly float64's significand.  Carrying mpf at dps 15
    would buy nothing (the `mp.dps` no-op defect).  `_precision.COMPUTE_DPS`
    is the corpus-wide value; `workdps` restores the caller's setting on exit,
    so importing this module still sets no global precision.
    """
    from _precision import COMPUTE_DPS as _CDPS
    with _mp.workdps(_CDPS):
        return _build_ysn_matrices_exact(partition, sparse_threshold)


def _build_ysn_matrices_exact(partition, sparse_threshold=32):
    """Build YSN matrices for σ_1, …, σ_{n-1} of the given partition.

    For dim ≥ sparse_threshold, returns `_ExactCOO` objects (each σ_j has
    at most 2·dim nonzeros: a diagonal entry plus 2×2 mixing blocks, so
    sparsity ≈ 2/dim). For smaller dim, returns dense tuples of `mpf`
    (faster for small cases).

    This said "returns scipy.sparse.csr_matrix objects" until 2026-09-05.
    PR #6794 changed the emit to `_ExactCOO` — csr_matrix is float64 and
    cannot hold these values — and left the docstring describing the
    behaviour it had replaced. It is corrected rather than deleted because
    the same slip is what the whole `_ExactCOO` change exists to prevent:
    a label that agrees with its own history instead of with its body.

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

    matrices = []
    for k in range(1, n):
        if use_sparse:
            rows, cols, vals = [], [], []
        else:
            M = [[_mp.mpf(0)] * dim for _ in range(dim)]
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
                    rows.append(i); cols.append(i); vals.append(_Q_MP)
                else:
                    M[i][i] = _Q_MP
                processed.add(i)
            elif same_col:
                if use_sparse:
                    rows.append(i); cols.append(i); vals.append(-_QI_MP)
                else:
                    M[i][i] = -_QI_MP
                processed.add(i)
            else:
                T_swapped = _swap_tab(T, k, k + 1)
                if T_swapped is None:
                    if use_sparse:
                        rows.append(i); cols.append(i)
                        vals.append(_Q_MP if rho > 0 else -_QI_MP)
                    else:
                        M[i][i] = _Q_MP if rho > 0 else -_QI_MP
                    processed.add(i)
                    continue
                key = tuple(tuple(r) for r in T_swapped)
                j = tab_index.get(key)
                if j is None:
                    if use_sparse:
                        rows.append(i); cols.append(i)
                        vals.append(_Q_MP if rho > 0 else -_QI_MP)
                    else:
                        M[i][i] = _Q_MP if rho > 0 else -_QI_MP
                    processed.add(i)
                    continue
                # Hoefsmit/Young seminormal diagonal entry at axial
                # distance rho.  h / q_int(rho) was WRONG: it satisfies the
                # quadratic relation (trace h, det -1) but violates the BRAID
                # relation, so the family was not a representation of H_n(q)
                # -- constant defect 0.7315 on every partition
                # (docs/audits/2026-08-31-ysn-matrices-are-not-a-representation.md,
                # bean qou-4m9u).  Identified against the Rust MPFR reference
                # pyhecke_native.seminormal_matrices_mpfr: 37/37 generators
                # over 9 partitions agree to 4e-51, where h/q_int(rho) agreed
                # on only the 11 with no mixing block.  At rho = -2 this is
                # -1/(q(q^2+1)), the value qou-4m9u derived symbolically; at
                # rho = +2 it is q^3/(q^2+1) = z_D, the convention-D Markov
                # parameter.
                # EXACT throughout: _H_MP / _Q_MP are mpf, so a_rho, a_neg,
                # bsq and off are mpf.  `math.sqrt` is float64 and would
                # truncate `off` to 53 bits -- use mp.sqrt.
                a_rho = _H_MP / (_mp.mpf(1) - _Q_MP ** (-2 * rho))
                a_neg = _H_MP - a_rho
                # det = -1  =>  b^2 = a(h-a) + 1.  This was already correct.
                bsq = a_rho * a_neg + _mp.mpf(1)
                off = _mp.sqrt(abs(bsq)) * (_mp.mpf(1) if bsq > 0 else _mp.mpf(-1))
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
            # `csr_matrix` is float64 and cannot hold these mpf values.
            matrices.append(_ExactCOO(rows, cols, vals, (dim, dim)))
        else:
            matrices.append(tuple(tuple(row) for row in M))
    return matrices


# ── Rust LP-accumulator kernel (qou-sv7h) ───────────────────────────────
# `pyhecke_native.lp_accumulator_step_traces_mpfr` performs the per-partition
# chain accumulation entirely in Rust at MPFR precision, building its seminormal
# matrices via `seminormal_matrices_mpfr` -- the family that satisfies the braid
# relation (the Python `_build_ysn_matrices` family does NOT; see
# docs/audits/2026-08-31-ysn-matrices-are-not-a-representation.md and
# computations/audits/ysn_braid_relation_audit.py).
#
# Verified against a pure-mpmath reference on the SAME matrices to 7.09e-48:
# computations/audits/lp_accumulator_kernel_gate.py.
#
# Optional by design: a bare container has no pyhecke_native, and this module
# must still import there. When absent the original Python path runs unchanged.
try:                                                    # pragma: no cover
    import pyhecke_native as _PHN
    _HAS_LP_KERNEL = hasattr(_PHN, "lp_accumulator_step_traces_mpfr")
    # Keep WHY, not just whether.  The bool below collapses three distinct
    # situations into one, and the fallback warning used to report the middle
    # one unconditionally -- telling a caller to rebuild a wheel that is
    # already correct.  See `_warn_if_kernel_absent`.
    _KERNEL_ABSENCE = None if _HAS_LP_KERNEL else "stale-wheel"
except ImportError:                                     # pragma: no cover
    _PHN = None
    _HAS_LP_KERNEL = False
    _KERNEL_ABSENCE = "not-installed"


_FALLBACK_WARNED = False


def _warn_if_kernel_absent():
    """Say, once per process, that this run is on the fallback matrices.

    🛑 This docstring read "that this run is on braid-violating matrices" until
    2026-09-12, and the message it introduces says the opposite one line down:
    since PR #6708 the `_build_ysn_matrices` family DOES satisfy the braid
    relation (`audits/ysn_braid_relation_audit.py` exits 0).  The summary line
    is what a reader skims, so it asserted a defect the body retracts.

    When `_HAS_LP_KERNEL` is False the accumulator falls back to matrices from
    `_build_ysn_matrices`. The fallback exists so this module still imports in a
    bare container and must stay; this warning makes the silent case audible.

    🛑 THE BRAID-VIOLATION CLAIM THIS DOCSTRING CARRIED IS FALSE AS OF PR #6708
    (corrected 2026-09-05). It read "`ysn_braid_relation_audit.py` proves that
    family VIOLATES the braid relation: it is not a representation of H_n(q)".
    #6708 fixed the builder (`a_rho = h/(1 - q^(-2 rho))`, braid defect
    0.7315 -> 7.5e-17) and that audit now EXITS 0, with the Python family in the
    same precision class as the Rust one. Anyone re-deriving the claim from this
    text would be re-deriving a retired defect.

    THE 17.3 % IS NOT DELETED -- IT IS RE-SCOPED. As recorded (bean `qou-i7ju`),
    deuterium, same call, same commit, same q0:

        kernel live      binding_energy(1,1) = -7.271102125     942 s
        fallback         binding_energy(1,1) = -8.52811254141  22607 s

    That was measured against the PRE-#6708 fallback, i.e. against the
    braid-violating family, which is the mechanism it was attributed to and
    which no longer exists. Whether any gap remains AT `binding_energy` is
    UNMEASURED -- its fallback arm is 6.3 h, so it was not re-run here.

    What WAS re-measured 2026-09-05, on the accumulator inside it
    (`unified_iterative_correction(1, 1)`, both arms live, k_exact = k_max):

        k=4..7   kernel and fallback agree to 0.000e+00
        k=8      1.348e-16                 (fallback  14.54 s vs kernel 0.26 s)
        k=9      0.000e+00                 (fallback 106.35 s vs kernel 2.20 s)

    So at the accumulator the two arms now agree to the arithmetic floor, and
    the speed gap is the surviving reason to prefer the kernel -- 56x at k=8
    and 48x at k=9 on this quantity, against the docstring's 24x on
    `binding_energy`. Those are different quantities; do not quote one as the
    other. Production is k_max = 11, which neither arm was run to here.

    Do not read the agreement above as proof the families are interchangeable.
    `ysn_trace_blindness_probe.py` shows the TRACE cannot see a braid defect at
    all -- Tr(ABA) - Tr(BAB) = Tr(B) - Tr(A) = 0 from the quadratic relation
    alone -- so trace agreement is weak evidence about matrices. It is the
    braid audit, not this table, that establishes the fallback is a
    representation.

    The remaining trap is that
    the module IMPORTS fine — `pyhecke_native` 0.9.0 is installed and exports 58
    names, and the one the guard needs is not among them. So checking
    `import pyhecke_native` tells you nothing; the guard tests the FUNCTION.

    `lp_accumulator_kernel_gate.py` cannot catch this either, by design: it holds
    the matrices fixed and verifies only the recurrence (to 7.09e-48). The
    divergence is in WHICH matrices enter it.

    Not a refusal. Whether a bare container should be allowed to compute a
    binding energy at all is a behavioural decision for the owner / `qou-sv7h`;
    this only makes the silent case audible.
    """
    global _FALLBACK_WARNED
    if _HAS_LP_KERNEL or _FALLBACK_WARNED:
        return
    _FALLBACK_WARNED = True
    # Report the cause we actually established, never a guess.  `_HAS_LP_KERNEL`
    # being False has three causes and this function can only distinguish them
    # via `_KERNEL_ABSENCE`, recorded at import.  A caller that sets the flag
    # False by hand (an A/B arm, a regression probe) leaves it None, and the
    # old text then told that caller to rebuild an already-correct wheel.
    _cause = {
        "not-installed": "pyhecke_native is NOT INSTALLED",
        "stale-wheel": ("pyhecke_native is installed but does NOT export "
                        "lp_accumulator_step_traces_mpfr (stale wheel)"),
    }.get(_KERNEL_ABSENCE,
          "the LP kernel was DISABLED BY THE CALLER (pyhecke_native itself is "
          "fine; nothing needs rebuilding)")
    _fix = ("*** Fix: cd tools/pyhecke-native && maturin build --release && pip "
            "install --force-reinstall --no-deps target/wheels/*.whl\n"
            "*** (pyhecke-native is not on PyPI, so a default container has a "
            "stale wheel.)\n") if _KERNEL_ABSENCE else ""
    print(
        f"\n*** WARNING: the LP accumulator kernel is not in use -- {_cause}.\n"
        "*** Falling back to _build_ysn_matrices. Since PR #6708 that family "
        "DOES satisfy\n"
        "*** the braid relation (audits/ysn_braid_relation_audit.py exits 0), "
        "and at the\n"
        "*** accumulator the two arms agree to <=1.3e-16 for k<=9 -- but it is "
        "~50x slower,\n"
        "*** and the recorded 17.3 % gap at binding_energy(1,1) has NOT been "
        "re-measured\n"
        "*** since #6708 (its fallback arm is 6.3 h). Prefer the kernel; treat "
        "a witness\n"
        "*** from this run as unverified rather than as wrong.\n"
        + _fix,
        file=_sys.stderr,
    )


def _lp_kernel_steps(partition, chains):
    """Per-step (trace, log_norm) for one partition, computed in Rust.

    Returns None when the kernel is unavailable, so callers fall back.

    Coefficients cross the boundary as decimal STRINGS, serialized explicitly
    at `_EXACT_COEFF_DPS`.

    The explicit `workdps` is load-bearing and this docstring used to be FALSE
    without it.  `str(mpf)` renders at the AMBIENT `mp.dps`, which is **15** in
    a bare import of this module (nothing here raises it), so the exact 50-dps
    intra-nucleon coefficients — the ones `_PROTON_G1` / `_NEUTRON_G1` carry as
    `mpf` precisely so they are not float64 — were being truncated to 14-15
    significant digits on the way in, i.e. to LESS than float64, while this
    docstring claimed "nothing narrows to f64".  Measured on the live path
    (`unified_iterative_correction(1, 1, k_exact=4)`, kernel available):

        str(_PROTON_G1[0][1])  '-0.209060298795639'            15 sig digits
        exact                  -0.2090602987956393154308462131296749438598

    The kernel is then asked for 50-dps MPFR arithmetic over 15-digit inputs.

    This fix DOES move the output, and by more than the float64 floor.  A
    three-way run on `unified_iterative_correction(1, 1, ·)` — pre-fix, this
    fix alone, and this fix plus the exact `_NN_D_MP` / `_PN_D_MP` coefficients
    — separates the two, each arm in its own process:

        k_exact=4   truncating -0.08955968305895065
                    full       -0.08955968305895065     rel 0
        k_exact=5   truncating -0.7335499391634722
                    full       -0.7335499391634975      rel 3.45e-14

    So the truncation is invisible at k_exact=4 and worth 3.4e-14 relative at
    k_exact=5 — about 150x the float64 floor, and above the framework's 1 ppQ
    (1e-15) L1 target.  It grows with the partition set, which is what a
    15-digit input truncation amplified through longer products should do, so
    do NOT read the k=4 null as evidence this is cosmetic.

    [2026-09-12, bean `qou-21oc`: the four figures in that table are the GATED
    return; the Pass-2 sign gate has since been dropped and the ungated values
    are -0.412212192245027 (k=4) and -1.2268740026260945 (k=5).  The FINDING is
    unaffected -- it is a relative comparison between two arms of the same run,
    and both arms move identically under the gate drop.  The absolute values are
    kept as the record of what was measured.]

    It is still not the BINDING constraint on this producer's accuracy:
    `unified_iterative_correction` narrows to float64 inside its own
    accumulation loop (`math.log(abs(tr_run))`, see the note on
    `binding_energy`'s return) and returns a Python float.  That narrowing is
    downstream of this one and is tracked separately.

    MEMOISED (2026-10-13, branch claude/binding-energy-profile-2026-10-13).
    `binding_energy` asks the kernel
    the SAME question up to three times per partition: the accumulator here,
    then `atom_character_raw(include_inter=True)` from the SDP leg and again
    from the Frobenius leg -- identical `(partition, chains)`, so an identical
    payload.  The kernel is deterministic (measured: three calls on (4,3,2,1)
    returned byte-identical strings), so the repeat calls bought nothing.
    The cache stores the kernel's raw DECIMAL STRINGS, keyed on the full
    serialized payload plus the q₀ string and the MPFR precision, and the
    `mpf` conversion below runs on every call exactly as before -- so a hit
    is byte-identical to a miss whatever the caller's ambient `mp.dps`.  It
    deliberately does NOT cache mpf values: a cached mpf carries the dps of
    whoever built it first (see `_partition_table`'s note).
    """
    if not _HAS_LP_KERNEL:
        return None
    from mpmath import mp as _mp
    from q_parameter import Q_50_DIGIT_STR as _Q50
    with _mp.workdps(_EXACT_COEFF_DPS):
        payload = [[(str(c), str(d), g) for c, d, g in ch] for ch in chains]
    key = (tuple(partition),
           tuple(tuple(step) for step in payload), _Q50, 50)
    out = _LP_KERNEL_MEMO.get(key)
    if out is None:
        out = _PHN.lp_accumulator_step_traces_mpfr(
            list(partition), payload, _Q50, 50)
        out = tuple((str(t), str(l)) for (t, l) in out)
        if len(_LP_KERNEL_MEMO) >= _LP_KERNEL_MEMO_MAX:
            _LP_KERNEL_MEMO.pop(next(iter(_LP_KERNEL_MEMO)))
        _LP_KERNEL_MEMO[key] = out
    return [(_mp.mpf(t), _mp.mpf(l)) for (t, l) in out]


# Raw kernel output (decimal strings), keyed on the exact serialized request.
# Bounded FIFO: one atom touches at most 2 x (partitions <= K_PARTITION_MAX)
# keys (inter on / off), so 4096 covers a whole binding_energy call with room.
_LP_KERNEL_MEMO: dict = {}
_LP_KERNEL_MEMO_MAX = 4096


def _exact_log(x):
    """`log|x|` without narrowing to float64, at `_EXACT_COEFF_DPS`.

    `math.log` returns a Python float WHATEVER it is handed, so calling it on
    an `mpf` silently discards every digit past the 16th.  Inside an
    accumulator that is worse than a single narrowing: the loop feeds
    `log_cur` back through `log_prev` at every step, so the truncation
    compounds over the whole trajectory.

    The explicit `workdps` matters for the same reason it does at the Rust
    boundary: mpmath computes at the AMBIENT precision, which is 15 dps in a
    bare import of this module, so a bare `mp.log` would trade a float64
    narrowing for a 15-digit one and buy nothing.
    """
    with _mp.workdps(_EXACT_COEFF_DPS):
        return _mp.log(_mp.mpf(x))


def _matmul_dim(A, B, dim):
    """Multiply two dim×dim matrices.  Uses numpy for dim ≥ 8.

    "Significant speedup for higher Hecke levels" is what this said; the real
    figure is 7-18 %, and the threshold is worth keeping for that rather than
    for anything dramatic.  Object dtype has no BLAS, so numpy here is an
    elementwise Python loop with less interpreter overhead, not a kernel.

    Measured 2026-09-07, best-of-7, mpf entries, against the actual else-branch
    below (python 3.11.15, numpy 2.4.6, mpmath 1.4.1):

        dim=8   numpy  1.10 ms   loop  1.34 ms   0.82x
        dim=12  numpy  3.89 ms   loop  4.37 ms   0.89x
        dim=16  numpy  9.50 ms   loop 10.65 ms   0.89x
        dim=24  numpy 32.54 ms   loop 34.96 ms   0.93x

    This does NOT reproduce finding 5 of bean `qou-sv7h`, which recorded the
    numpy branch as 31 % SLOWER at dim 16 (0.0126 s vs 0.0096 s) and called the
    threshold a pessimization.  Scope-limited negative: the claim does not
    reproduce in this container at these library versions, which is not the
    same as it having been wrong when it was taken — the arm that moved is
    numpy's (12.6 -> 9.5 ms), so a version difference is the leading candidate
    and was not isolated.  Re-measure before acting on either figure.
    """
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
    """Trace, at whatever precision the matrix carries.

    The `float()` that used to wrap `np.trace` truncated an exact (mpf)
    trace to 53 bits -- measured 2026-09-05: every trace on the A=2 path
    is `mpf`, and since #6794 the matrices carry 167 significand bits.
    Each of the three other call sites casts at its own public boundary
    (`float(chi)`), so widening the return here loses nothing and stops
    the accumulator's log from being fed a float64 value.
    """
    if isinstance(M, np.ndarray):
        return np.trace(M)
    return sum(M[i][i] for i in range(dim))


def _identity(dim):
    if dim >= 8:
        return np.eye(dim)
    return tuple(tuple(1.0 if i == j else 0.0 for j in range(dim))
                 for i in range(dim))


def _crossing_in_partition(c, d, gen_index, sigmas, dim):
    """Matrix of c·σ_{gen} + d·I  in YSN representation of a partition."""
    sig = sigmas[gen_index]
    # A `.toarray()` densify stood here for a scipy sparse sigma.  No carrier
    # in this module has that method (measured: 0 of 1528), and all three
    # callers are in the DENSE arm of their dispatch, so `sig` is a tuple.
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
        # Exact coefficients, matching the intra tables above (see `_NN_D_MP`).
        for ti in prev_types:
            if ti == 'p' and nucleon_type == 'p':
                chain.append((1, 0, g % n_gens))          # pp
            elif ti == 'n' and nucleon_type == 'n':
                chain.append((1, _NN_D_MP, g % n_gens))   # nn
            else:
                chain.append((1, _PN_D_MP, g % n_gens))   # pn
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
                                 k_exact=K_PARTITION_MAX, as_mpf=False):
    """Run the accumulator at the canonical working precision.

    MEASURED 2026-09-05 (qou-sv7h): PR #6794 made `_build_ysn_matrices`
    exact -- a sigma entry carries **167 significand bits** where float64
    has 53 -- and this function then threw that away on the first
    multiply, because mpmath rounds every operation to the AMBIENT
    `mp.dps`, which is **15** in a bare import of this module.  Measured
    on one entry: `v*v` keeps 53 bits at ambient dps and 234 bits inside
    `workdps(COMPUTE_DPS)`, a relative difference of 2.57e-17 per
    operation; compounded over the accumulation the RESULT moved
    8.3e-15 / 4.1e-15 / 2.9e-15 at k_exact = 5 / 6 / 7.

    Same defect as the one #6794 fixed, one level up: an exact input
    multiplied at float64 precision is a float64 computation.  This is
    the builder's wrapper applied to its consumer.
    """
    from _precision import COMPUTE_DPS as _CDPS
    with _mp.workdps(_CDPS):
        return _unified_iterative_correction_exact(
            Z, N, return_per_step=return_per_step,
            k_max=k_max, k_exact=k_exact, as_mpf=as_mpf)


def _unified_iterative_correction_exact(Z, N, return_per_step=False,
                                        k_max=K_PARTITION_MAX,
                                        k_exact=K_PARTITION_MAX, as_mpf=False):
    """Unified iterative correction over per-partition weights.

    NAMING CORRECTED 2026-09-05 (owner ruling; PR #6752).  This read
    "via LP-dual shadow prices".  The weights y_λ are not LP duals --
    see `lp_shadow_price` above for the two independent reasons.

    A SINGLE consistent algorithm — no special cases for any A.
    Starts at A = 1 and accumulates a per-step contribution from
    EVERY partition λ ⊢ k for k = 2, …, k_max:

      ΔB_k(step) = m_e · H_q(λ) · y_λ ·
                   ( ln|Tr M_λ^{(0..step)}| − ln|Tr M_λ^{(0..step−1)}| )

    where:

      • H_q(λ) = ∏_{x∈λ} [h_x(λ)]_q is the q-hook product (the
        categorical scale C_λ = m_e · H_q(λ) generalises the (2,2)
        derivation of [3]·[2]² · m_e to every λ);
      • y_λ = w_λ/d_λ − 1/[k]_q! is a closed-form per-partition
        weight, named for prop:mass-coefficient-shadow-price but not
        computed from any program.  The clause that stood here —
        "shadow prices are the unique invariants that the
        operator-selection LP assigns to the partition basis" — is
        false twice over: that LP indexes its constraints by NF basis
        element (n! of them, not p(n)), and its minimiser set is a
        POSITIVE-DIMENSIONAL face, so it assigns nothing uniquely.
        Proved in the content block, commit 6b7d2ec4a8;
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

        Because that default EQUALS `k_max`, the q-Gaussian tier is
        UNREACHABLE unless a caller passes a smaller `k_exact`: the
        window `k_exact < k ≤ k_max` is empty, so `active_gaussian`
        is [].  Measured 2026-09-07, confirming finding 6 of bean
        `qou-sv7h`:

            defaults (k_exact = k_max = K_PARTITION_MAX = 11)   0 partitions
            k_exact=4                                         169 partitions
            k_exact=5                                         164 partitions
            k_exact=6                                         155 partitions

        So every default run is fully exact and pays for it, and the
        `_q_gaussian_character_approx` branch below is dead code on
        that path.  This is a note, not a defect: exact-everywhere is
        the correct default for a producer.  What it means in practice
        is that the tier is untested by any default run — do not read
        a green default run as evidence the approximation works.

    Returns
    -------
    float (total correction, MeV) or
    (float, list-of-dicts) if return_per_step.

    🛑 THE RETURN VALUE CHANGED ON 2026-09-12 (owner ruling, bean
    `qou-21oc`; PR #7251).  Until then this function returned a GATED sum
    admitting only partitions with `final_tr_sign <= 0`, on a
    complementary-slackness argument that is now REFUTED sorry-free.  It
    now returns the UNGATED sum over every enumerated partition.

    🛑 QUOTE THE TIER.  This quantity is STRONGLY `k_exact`-dependent -- ²H
    ungated spans 43x across the tiers -- so a bare figure is meaningless:

        k_exact   atom   gated (before)         ungated (after)        factor
        -------   ----   --------------------   --------------------   ------
           4      ²H     -0.0895596830589507    -0.412212192245027      4.603
           4      ⁴He    -0.0805867484776914    -0.2742397716174        3.403
           5      ²H     -0.7335499391634978    -1.2268740026260945     1.672
           6      ²H     -1.3656848170878801    -2.251131977321312      1.648
           6      ⁴He    -0.8387490758934286    -1.448199112790757      1.727
        11 = DEFAULT ²H  -9.14773623102088     -17.6908290020795        1.934
        11 = DEFAULT ⁴He -8.20155846836239     -15.9926510049258        1.950

    The PRODUCTION number is the last two rows.  The widely-quoted "4.6x /
    3.4x" is the `k_exact = 4` tier and is 2.4x too large for the default;
    the gate's grip LOOSENS as the partition set grows (22 % of the
    magnitude admitted at k_exact = 4, 52 % at the default).  Wall cost at
    the default: 425.5 s for ²H, 1165.1 s for ⁴He.

    THIS IS NOT AN ACCURACY IMPROVEMENT.  At ²H the AME2020 binding is
    +2.2246 MeV, so both the old and the new number have the WRONG SIGN,
    and the new one is further from AME.  The drop removes a selection
    step whose only justification is disproved; see the Pass-2 block for
    the four mismatches and the scope-(b) invariant.  The historical gated
    sum is still reported, as
    `per_step[-1]['gated_total_DISPROVED_SELECTION_MeV']`.

    References
    ----------
    Kerov 1996 (q-hook walk) [kerov1996],
    Féray–Méliot 2010 (q-Plancherel CLT) [feray-meliot2012],
    Satuła et al. 1997 (empirical Wigner energy) [satula1997],
    prop:mass-coefficient-shadow-price (LP dual = BW coefficient).
    """
    _warn_if_kernel_absent()
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

    # NOTE (2026-09-07, bean `qou-sv7h`): `k_max` does not affect the return
    # value. `k_max = k_exact` empties `active_gaussian`; results are
    # byte-identical either way —
    #
    #     A=2 k=4   gauss=169 -> -0.08955968305895068   gauss=0 -> same
    #     A=2 k=5   gauss=164 -> -0.7335499391634976    gauss=0 -> same
    #     A=4 k=4   gauss=169 -> -0.08058674847769143   gauss=0 -> same
    #
    # — because `delta_g` in the Gaussian loop below is a HARDCODED 0.0.  Its
    # justification WAS complementary slackness; that argument is refuted
    # sorry-free (PR #7251) and the zeroing is now asserted-not-derived, bean
    # `qou-ai7v` — see the banner at the Gaussian loop.  The BEHAVIOUR is
    # unchanged, so this note's conclusion stands: raising `k_max` buys
    # `log_trace` values for the per-step rows and nothing else.
    #
    # [2026-09-12, bean `qou-21oc`: the three figures above are the GATED
    # return; ungated they are -0.412212192245027 (A=2 k=4),
    # -1.2268740026260945 (A=2 k=5) and -0.2742397716174 (A=4 k=4).  The
    # byte-identical gauss=169 vs gauss=0 finding is unaffected — both arms
    # move identically.]
    #
    # RETRACTION, same day. This note first read "the Gaussian contribution is
    # computed and DISCARDED", on the theory that `state` excludes Gaussian
    # partitions so Pass 2 drops their contribution. The measurement above was
    # right and the mechanism was wrong: there is no contribution to drop.
    # I inferred the mechanism from the two totals' definitions without reading
    # the twenty lines that set `delta_g`, and the byte-identical results are
    # equally consistent with either story — which is exactly why a measurement
    # that matches your hypothesis is not evidence for its mechanism.
    #
    # The disagreement between the per-step rows and the return value is real,
    # but it is RAW-vs-GATED and has nothing to do with this tier. See the
    # `cumulative_ungated_MeV` note at the per-step append below.

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

    state = []
    for e in active:
        first = e['ysn'][0]
        sparse_sigmas = _is_sparse_sigma(first)
        dim = first.shape[0] if sparse_sigmas else len(first)
        if sparse_sigmas:
            # Running M is dense for fast sparse-× -dense multiplication
            M = np.eye(dim)
        else:
            M = _identity(dim)
        L0 = _exact_log(dim)
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
            'entry': e, 'dim': dim, 'M': M, 'log_norm': _mp.mpf(0),
            'log_prev': L0, 'scale': scale, 'cumul_partition': _mp.mpf(0),
            'sparse': sparse_sigmas,
        })

    per_step = []
    cumul_total = _mp.mpf(0)

    # Precompute every partition's per-step (trace, log_norm) in Rust, once.
    # This replaces ONLY the matrix maintenance; every line of the accumulation
    # below -- raw_delta, cumul_partition, final_tr_sign -- and the whole of
    # Pass 2's complementary-slackness gate are untouched. That distinction is
    # the point: a reimplementation of this function drops Pass 2 and is wrong
    # by a factor of ~4.6 (measured), which is why the kernel is wired in here
    # rather than around.
    for s in state:
        s['kernel_steps'] = None
        if _HAS_LP_KERNEL:
            _ng = s['entry']['n_gens']
            _chains = [_step_chain_generic(ordering[_k], ordering[:_k], _ng)
                       for _k in range(A)]
            s['kernel_steps'] = _lp_kernel_steps(s['entry']['partition'], _chains)

    # ── Pass 1: forward accumulation ──────────────────────────
    for kk in range(A):
        nuc = ordering[kk]
        prev_types = ordering[:kk]

        step_delta_total = _mp.mpf(0)
        partitions_step = {}

        for s in state:
            entry = s['entry']
            dim = s['dim']
            sigmas = entry['ysn']
            n_gens = entry['n_gens']
            chain = _step_chain_generic(nuc, prev_types, n_gens)
            # The sparse path dispatches to scipy's compiled kernels, which
            # are float64-only: `sig_sparse.dot(M)` raises "no supported
            # conversion for types: (dtype('float64'), dtype('O'))" the moment
            # M carries mpf.  scipy is RIGHT to refuse -- the only way to
            # satisfy it is to throw the exact coefficients away.  numpy's `@`
            # (the dense path below) DOES support object dtype, since it falls
            # back to elementwise Python arithmetic rather than BLAS, so an
            # exact chain routes there and keeps its precision.
            #
            # Decided BEFORE the loop, deliberately: M starts float64 and only
            # becomes object after the first crossing multiplies it by an mpf
            # coefficient, so a per-iteration dtype test would take the sparse
            # path once and then crash on the second crossing.
            # NOTE (2026-08-31, qou-sv7h): the guard used to be
            #     if s['sparse'] and not exact_chain:
            # and `exact_chain` is True for EVERY physical chain -- measured over
            # every (nucleon, prev_types, n_gens) combination. The coefficient
            # histogram is ('int','int') 132, ('int','mpf') 132, ('float','float')
            # 48: the mpf are genuine 50-dps values AND `c` is the Python int 1,
            # which is not a float. So `not exact_chain` was never true, and BOTH
            # branches below were dead -- including the COO object accumulator
            # written specifically for the exact case. Every partition, up to
            # dim 2310, fell through to the O(dim^3) dense path.
            #
            # The dtype test below already dispatches correctly per iteration
            # (float64 -> scipy sparse BLAS; object -> COO over sigma's nonzeros,
            # both O(dim*nnz)), so the outer exactness test was not only wrong,
            # it was redundant. Value-equality verified against the pre-fix
            # result at k_exact = 4..8 (k=8 carries 12 sparse partitions).
            if s.get('kernel_steps') is not None:
                # Rust supplied this partition's whole trajectory up front:
                # the trace and accumulated log-norm for every step, including
                # the same `max|M| > 1e80` rescale applied below. The matrix
                # itself is never materialised in Python.
                _kernel_hit = True
                tr_run, s['log_norm'] = s['kernel_steps'][kk]
            elif s['sparse']:
                _kernel_hit = False
                # For each crossing (c, d, gen), apply M ← M @ (c·σ_gen + d·I)
                # = c · (M @ σ_gen_sparse) + d · M.  Avoids materialising
                # the dense (c·σ + d·I) matrix at every crossing.
                # Cost: dense × sparse = O(dim · nnz) = O(dim²) vs
                # dense × dense = O(dim³).
                M_run = s['M']
                _sig_coo = {}   # gen -> (row, col, data) of σ, for the object path
                for c, d, gen in chain:
                    sig_sparse = sigmas[gen]
                    # The scipy path is a FLOAT64 optimisation. `_PROTON_G1` /
                    # `_NEUTRON_G1` carry `d = -h` as an `mpf` (correctly — it
                    # is ℏ_q), so the first such crossing promotes `M_run` to
                    # dtype object and scipy then raises
                    #   TypeError: no supported conversion for types:
                    #              (dtype('float64'), dtype('O'))
                    # which is why this producer had been dead: its witness is
                    # from 2026-06-17 and the script has changed since.
                    # Densify and multiply with object arithmetic rather than
                    # coercing c/d to float — that would silently discard the
                    # precision the mpf exists to carry (AGENTS.md: never
                    # compute in float). The densified σ is cached per
                    # generator, so the COO decomposition is done once per generator.
                    # Dispatch on SIGMA, not on M_run: M_run starts as
                    # np.eye (float64), so keying on it would send the FIRST
                    # crossing of an exact sigma into a scipy float64 call.
                    # Keep the SPARSITY, lose only the BLAS. Densifying σ
                    # and doing `M_run @ sig_d` is O(dim³) in object
                    # arithmetic and does not finish — measured, >10 min on
                    # the A=2 atom alone. Accumulating over σ's nonzeros is
                    # O(dim·nnz), the same complexity the float64 branch
                    # used to get from sparse BLAS.
                    #
                    # Unconditional since 2026-09-11.  The `else` here was the
                    # scipy sparse-BLAS arm, guarded by a predicate that asked
                    # whether sigma carries `mpf` (`_sigma_is_exact`, itself
                    # removed with this change — the guards were its only
                    # callers).  Every sparse carrier IS exact, 1120 of 1120,
                    # so the guard was always true and the arm never ran —
                    # instrumented, 184 hits on this branch and 0 on the other.
                    coo = _sig_coo.get(gen)
                    if coo is None:
                        m = sig_sparse.tocoo()
                        coo = (m.row, m.col, m.data)
                        _sig_coo[gen] = coo
                    rows_i, cols_j, vals = coo
                    # object dtype: a float64 Msig would truncate mpf.
                    Msig = np.zeros(M_run.shape, dtype=object)
                    for i, j, v in zip(rows_i, cols_j, vals):
                        Msig[:, j] += M_run[:, i] * v
                    M_run = c * Msig + d * M_run
                s['M'] = M_run
            else:
                _kernel_hit = False
                M_step = _identity(dim)
                for c, d, gen in chain:
                    M_cross = _crossing_in_partition(c, d, gen, sigmas, dim)
                    M_step = _matmul_dim(M_step, M_cross, dim)
                s['M'] = _matmul_dim(s['M'], M_step, dim)
            if _kernel_hit:
                m_max = _mp.mpf(0)   # the rescale already happened in Rust
            elif isinstance(s['M'], np.ndarray):
                # `float(np.max(...))` truncated an exact max to 53 bits and
                # then divided the whole matrix by it -- a float64 rescale of
                # exact entries.  Take the max in the matrix's own arithmetic.
                m_max = max(abs(x) for x in s['M'].flat) if s['M'].size else _mp.mpf(0)
            else:
                m_max = _mp.mpf(0)
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
                s['log_norm'] += _exact_log(m_max)
            if not _kernel_hit:
                tr_run = _trace_dim(s['M'], dim)
            # `_exact_log`, not `math.log`: this value is fed back through
            # `log_prev` on the next step, so a float64 narrowing here
            # compounds over the trajectory rather than rounding once.
            log_cur = (s['log_norm'] + _exact_log(abs(tr_run))
                       if abs(tr_run) > 1e-300 else s['log_prev'])
            raw_delta = s['scale'] * (log_cur - s['log_prev'])
            # This comment used to read: "LP complementary slackness is a
            # FINAL-STATE condition: y_λ* × tr(Φ_λ*) = 0 on the SOLVED LP.
            # The per-step tightness filter would be a heuristic approximation
            # of this; ... the final sign gate is applied in Pass 2 below."
            #
            # CORRECTED 2026-09-12 (bean `qou-21oc`; PR #7251).  There is no
            # final sign gate any more, and the complementary-slackness
            # justification for the one that used to be here is REFUTED
            # sorry-free -- see the Pass-2 block below for the four
            # mismatches and the scope-(b) invariant.  Every partition's
            # accumulated delta now reaches the total.
            delta = raw_delta
            s['cumul_partition'] += delta
            s['log_prev'] = log_cur
            # Final trace sign: retained as DIAGNOSTIC data only.  It is a
            # real property of the atom's final state and is reported in
            # `per_step`; it is no longer an admission filter on the sum.
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
        # 🛑 THE ZEROING BELOW IS ASSERTED, NOT DERIVED (2026-09-12).
        #
        # This block used to justify `delta_g = 0.0` by the SAME
        # complementary-slackness argument the Pass-2 sign gate used
        # ("positive trace ⇒ SLACK Frobenius constraint ⇒ y_λ* = 0 by
        # complementary slackness ... the categorically correct outcome").
        # That argument is refuted sorry-free in
        # `QOU.MassTheory.UICGateNotFromComplementarySlackness` (PR #7251) --
        # see the Pass-2 block below for the four mismatches -- so the
        # justification stated here is GONE, and the zeroing is now an
        # unexplained modelling choice inherited from it.
        #
        # It has NOT been changed here, deliberately.  Dropping it is a
        # behaviour change with no derived replacement: the q-Gaussian tier
        # is a Perron-Frobenius ASYMPTOTIC approximation that supplies a
        # `log_trace` and no matrix, so there is no derived rule saying what
        # its contribution should be, and inventing one to move the number
        # would be selection, not derivation.  Tracked as bean `qou-ai7v`.
        #
        # Consequence for a reader: the fallback tier contributes exactly
        # zero to every total this function returns, at every k in
        # (k_exact, k_max].  Do not read that zero as a derived prediction
        # that high-k partitions are negligible.
        gaussian_delta_total = _mp.mpf(0)
        for eg in active_gaussian:
            eg_info = eg
            log_trace_approx = _q_gaussian_character_approx(eg_info, None, kk)
            # Asserted zero -- see the banner above.  `log_trace_approx` IS
            # computed and IS reported in `per_step`, so the diagnostic is
            # not lost; only its contribution to the sum is stipulated.
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
            # `cumulative_ungated_MeV`, NOT `cumulative_MeV` (renamed
            # 2026-09-07, bean `qou-sv7h`).
            #
            # UPDATED 2026-09-12 (bean `qou-21oc`): this running total and the
            # function's return value now AGREE at the last row, because the
            # Pass-2 sign gate has been removed.  The rename is kept: the name
            # still says truthfully what the field is, and the field's whole
            # history is that it once differed from the return by 3.4-4.6x
            # at k_exact=4 -- and by 1.93x at the k_exact=11 PRODUCTION
            # DEFAULT, which is the number a reader of the production path
            # needs (²H -9.14773623102088 -> -17.6908290020795, 94 of 193
            # blocks admitted; ⁴He -8.20155846836239 -> -15.9926510049258,
            # 90 of 193).  The full tier table is in the docstring above;
            # NEVER quote this quantity without its k_exact.
            #
            # The measurement that motivated the rename, at k_exact=4, is
            # preserved here because it is the size of the change this file
            # just made:
            #
            #     A=2   ungated -0.412212192245027    then-returned -0.0895596830589507
            #           4 of 10 exact partitions "tight" at the final state
            #     A=4   ungated -0.2742397716174      then-returned -0.0805867484776914
            #           2 of 10 "tight"
            #
            # The ungated value is now what is returned in both rows.  Note it
            # is NOT closer to AME: at A=2 the AME binding is +2.2246 MeV and
            # the ungated total is -0.4122 MeV at k_exact=4 (-17.69 MeV at the
            # production default), still wrong in sign at every tier and
            # FURTHER from AME than the gated value was.  Dropping the gate
            # buys honesty, not accuracy (AGENTS.md "NO FITTING").
            #
            # Safe to rename: measured on `main`, this key had ZERO consumers.
            # `probe_9b_manybody_expansion.py` writes a `cumulative_MeV` of its
            # own into its own witness and never reads this one.
            per_step.append({
                'A': kk + 1, 'Z': Z_k, 'N': N_k, 'nuc': nuc,
                'delta_total_MeV': step_delta_total,
                'cumulative_ungated_MeV': cumul_total,
                'partitions': partitions_step,
                'n_exact_partitions': len(active_exact),
                'n_gaussian_partitions': len(active_gaussian),
            })

    # ── Pass 2: the final-state sign gate is GONE (2026-09-12) ───────
    #
    # WHAT USED TO BE HERE.  A gate that admitted a Wedderburn block to the
    # sum only when `final_tr_sign <= 0`:
    #
    #     if s.get('final_tr_sign', 1) <= 0:
    #         gated_total += s['cumul_partition']
    #
    # justified in this comment by LP complementary slackness -- "on the
    # OPTIMAL primal-dual pair (Φ*, y*), y_λ* × ⟨Φ*, π_λ⟩_F = 0 ... so
    # y_λ* > 0 only when the Frobenius constraint is TIGHT at the atom's
    # FINAL state, i.e. tr(M_λ(W_atom)) ≤ 0."  The function returned that
    # gated sum.
    #
    # WHY IT IS GONE.  That justification is REFUTED, sorry-free, in
    # `QOU.MassTheory.UICGateNotFromComplementarySlackness` (PR #7251, 8
    # declarations, `#print axioms` clean).  The LP it invokes exists --
    # `prop:operator-selection-lp`, `QOU.ParticleInteractions.
    # operator_selection_lp` -- and complementary slackness on it does not
    # give this gate, by four independent mismatches:
    #
    #   1. INDEX SET.  LP constraints are indexed by NF basis elements
    #      (d = n!); the gate is indexed by partitions (p(n)).  At n = 3
    #      that is 6 against 3.
    #   2. ARGUMENT.  CS constrains `(Gx*)_i`, a function of the operator
    #      being SELECTED.  The gate reads `t_λ = tr(M_λ(W_atom))`, an
    #      INPUT, which enters the LP only as a cost coefficient.
    #   3. DIRECTION.  `IsFeasible` demands `0 ≤ (Gx)_i`, so on any feasible
    #      point `≤ 0` and `= 0` are the same predicate: a sign gate there
    #      IS the tightness gate, keeping only blocks at exactly zero --
    #      while this producer kept 4 of 10 at ²H.
    #   4. NO UNIQUE OPTIMUM.  The minimiser set is a positive-dimensional
    #      face, so "the OPTIMAL primal-dual pair" names no unique object.
    #
    # A partition-indexed repair is excluded scope (b).  INVARIANT: primal
    # feasibility of the Frobenius constraints plus orthogonality of the
    # Wedderburn projectors.  The projectors are orthogonal idempotents, so
    # `G_{λμ} = tr_M(P_λ P_μ) = δ_{λμ} tr_M(P_λ)` is diagonal, CS decouples
    # to `s_λ · G_{λλ} · x_λ = 0`, and the atom's traces never appear.
    # Independent of n, q and trace convention.
    #
    # See also `lp_shadow_price` (:328) -- an owner-ruled correction of
    # 2026-09-05 (PR #6752) already states that this module's `y_λ` are NOT
    # LP duals and that the net-constraint dual `y_0*` is identically zero.
    # That ruling landed at the site carrying the offending NAME and never
    # reached the reasoning here, ~1 900 lines down; one file asserted both
    # for a week.
    #
    # One refinement of that ruling, from #7251 and worth not losing:
    # `y_0* = 0` is BASIS-DEPENDENT.  It holds for the NF-basis instance,
    # whose cost vector IS a Gram row; the block-indexed instance measures
    # `y_0* = 0.0346905` (²H) and `0.0129979` (⁴He).  The version that
    # applies to `lp_shadow_price` is the NF one, so that ruling stands as
    # written -- but do not quote "the dual is identically zero" of an
    # arbitrary instance.
    #
    # WHAT THIS BUYS, STATED PLAINLY.  Not accuracy.  At ²H the AME binding
    # is +2.2246 MeV; the ungated total is -0.4122 MeV, wrong in sign, as
    # the gated -0.0896 MeV also was.  What it buys is that the producer now
    # reports what its functional actually gives, instead of a subset chosen
    # by a rule nobody can derive.  Per AGENTS.md "NO FITTING": a documented
    # honest miss is a result; a more accurate selected route is worth less
    # than a less accurate derived one.  DO NOT reinstate this gate, and do
    # not look for a replacement selection that restores the old numbers --
    # that is selection against the target.
    #
    # Owner ruling 2026-09-12 (bean `qou-21oc`).  #7237 independently marks
    # the gate asserted-not-derived in the content block.
    #
    # The gated sum is still COMPUTED and reported, under a name that says
    # what it is, so the historical number stays reproducible and any
    # consumer that wants it must now say out loud that it wants it.
    gated_total_DISPROVED_SELECTION = _mp.mpf(0)
    n_tight = 0
    for s in state:
        if s.get('final_tr_sign', 1) <= 0:
            gated_total_DISPROVED_SELECTION += s['cumul_partition']
            n_tight += 1

    if return_per_step:
        if per_step:
            per_step[-1]['raw_total_MeV'] = cumul_total
            # `gated_total_MeV` is RENAMED, not merely deprecated: a neutral
            # name on a disproved selection is what let it be read as the
            # answer.  Two consumers on `main` read the old key
            # (`probes/where_the_a_dependence_is_lost_probe.py:182`,
            # `probes/uic_per_block_log_valley_scan_probe.py:134`); both are
            # updated in the same commit.
            per_step[-1]['gated_total_DISPROVED_SELECTION_MeV'] = \
                gated_total_DISPROVED_SELECTION
            per_step[-1]['n_active_exact'] = len(active_exact)
            per_step[-1]['n_active_gaussian'] = len(active_gaussian)
            per_step[-1]['n_tight_final'] = n_tight
            per_step[-1]['k_exact'] = k_exact
            per_step[-1]['k_max'] = k_max
        if as_mpf:
            return cumul_total, per_step
        return float(cumul_total), per_step  # float64-ok: public return boundary after mpf accumulation
    # float, as this function has always returned -- the cast is at the public
    # boundary, and NOW that is true.  The note that stood here said the
    # accumulation "keeps its precision ... because math.log already narrows
    # inside the loop", which states the defect and then draws the opposite
    # conclusion from it: a log that narrows inside the loop is exactly what
    # stops the accumulation keeping anything.  Every log on this path goes
    # through `_exact_log` as of 2026-09-07.
    # `as_mpf=True` skips the cast for callers that serialize with
    # `_precision.fmt` (binding_energy(as_mpf=True), hadron_knot_table).
    if as_mpf:
        return cumul_total
    return float(cumul_total)  # float64-ok: public return boundary after mpf accumulation


def _jet_witness_path(Z, N, jet, witness_dir):
    """Witness file path for one (Z, N, jet) cell."""
    return _os.path.join(witness_dir,
                         f'unified_jet_Z{Z}_N{N}_j{jet}.json')


def atom_character_raw(Z, N, entry, include_inter=True):
    """Raw characters of the atom braid word in partition λ, at the
    canonical working precision.

    Same reason as `unified_iterative_correction`'s wrapper: mpmath
    rounds to the AMBIENT `mp.dps`, which is 15 on a bare import, so
    without this the exact seminormal matrices are multiplied at
    float64 precision.  Measured: switching this function's `math.log`
    to `mp.log` alone moved nothing (0.00e+00 on four partitions),
    because at dps 15 the two agree -- the precision context is what
    the type change needs to be worth anything.
    """
    from _precision import COMPUTE_DPS as _CDPS
    with _mp.workdps(_CDPS):
        return _atom_character_raw_exact(Z, N, entry, include_inter=include_inter)


def _atom_character_raw_exact(Z, N, entry, include_inter=True):
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
    A = Z + N
    if A < 1 or not entry.get('has_ysn') or not entry.get('ysn'):
        return (float(entry.get('dim', 1)), 0.0, int(entry.get('dim', 1)))  # float64-ok: legacy public tuple contract

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
    sparse_sigmas = _is_sparse_sigma(first)
    dim = first.shape[0] if sparse_sigmas else len(first)
    M = np.eye(dim) if sparse_sigmas else _identity(dim)
    log_norm = _mp.mpf(0)
    # Rust LP-accumulator kernel (qou-sv7h). Same recurrence, same rescale, at
    # MPFR precision over the braid-satisfying seminormal family. Only the FINAL
    # step's trace and log-norm are returned by this function, so take the last.
    _ks = _lp_kernel_steps(entry['partition'], [
        _step_chain_generic(ordering[_k], ordering[:_k], n_gens,
                            include_inter=include_inter)
        for _k in range(A)])
    if _ks:
        _tr, _ln = _ks[-1]
        return (float(_tr), float(_ln), int(dim))  # float64-ok: legacy public tuple contract after MPFR kernel
    for kkk in range(A):
        nuc = ordering[kkk]
        prev_types = ordering[:kkk]
        chain = _step_chain_generic(nuc, prev_types, n_gens, include_inter=include_inter)
        if sparse_sigmas:
            # Object-dtype fallback (qou-w2vy, 2026-08-31). scipy's sparse
            # kernels are float64-only, so `sig_sparse.dot(M)` raises
            #   TypeError: no supported conversion for types:
            #              (dtype('float64'), dtype('O'))
            # the moment an mpf coefficient promotes M_run to dtype object --
            # which every physical chain does, since _PROTON_G1/_NEUTRON_G1
            # carry d = -h as an mpf. scipy is RIGHT to refuse: the only way to
            # satisfy it is to discard the exact coefficients.
            #
            # This is the SAME fix da645cf0f32 applied to
            # unified_iterative_correction; this loop was left behind, and the
            # crash went unnoticed because binding_energy calls that function
            # FIRST and it never returns for A >= 2, so control never reached
            # here. Accumulating over sigma's nonzeros is O(dim*nnz) -- the same
            # complexity the float64 branch gets from sparse BLAS -- and the
            # densified COO is cached per generator.
            M_run = M
            _sig_coo = {}
            for c, d, gen in chain:
                sig_sparse = sigmas[gen]
                # Unconditional since 2026-09-11 -- see the note in
                # `unified_iterative_correction`.  The scipy sparse-BLAS
                # `else` that stood here was unreachable: every sparse
                # carrier is `_ExactCOO`, so the guard never failed.
                coo = _sig_coo.get(gen)
                if coo is None:
                    _m = sig_sparse.tocoo()
                    coo = (_m.row, _m.col, _m.data)
                    _sig_coo[gen] = coo
                rows_i, cols_j, vals = coo
                # object dtype: a float64 Msig would truncate mpf.
                Msig = np.zeros(M_run.shape, dtype=object)
                for i, j, v in zip(rows_i, cols_j, vals):
                    Msig[:, j] += M_run[:, i] * v
                M_run = c * Msig + d * M_run
            M = M_run
        else:
            M_step = _identity(dim)
            for c, d, gen in chain:
                M_cross = _crossing_in_partition(c, d, gen, sigmas, dim)
                M_step = _matmul_dim(M_step, M_cross, dim)
            M = _matmul_dim(M, M_step, dim)
        if isinstance(M, np.ndarray):
            m_max = max(abs(x) for x in M.flat)
        else:
            m_max = max(abs(M[i][j]) for i in range(dim) for j in range(dim))
        if m_max > 1e80:
            if isinstance(M, np.ndarray):
                M = M / m_max
            else:
                M = tuple(tuple(M[i][j]/m_max for j in range(dim))
                          for i in range(dim))
            log_norm += _exact_log(m_max)
    chi = _trace_dim(M, dim)
    return (float(chi), float(log_norm), int(dim))  # float64-ok: legacy public tuple contract after mpf accumulation


def _contrib_single_partition(Z, N, entry):
    """One partition's LP-dual contribution, at the canonical working
    precision (see `atom_character_raw` for why the context, not just
    the log type, is what matters)."""
    from _precision import COMPUTE_DPS as _CDPS
    with _mp.workdps(_CDPS):
        return _contrib_single_partition_exact(Z, N, entry)


def _contrib_single_partition_exact(Z, N, entry):
    """Compute one partition's final LP-dual contribution for atom (Z,N).
    Returns (final_trace_sign, cumul_delta_MeV).
    Separate from the multi-partition accumulator so we can process
    partitions one at a time (needed for the jet-incremental loop).
    """

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
    sparse_sigmas = _is_sparse_sigma(first)
    dim = first.shape[0] if sparse_sigmas else len(first)

    if sparse_sigmas:
        M = np.eye(dim)
    else:
        M = _identity(dim)

    log_norm = _mp.mpf(0)
    log_prev = _exact_log(dim)
    scale = entry['C_lambda_resolvent_MeV']
    cumul = _mp.mpf(0)
    tr_run = dim  # initial trace of identity

    # Rust LP-accumulator kernel (qou-sv7h).  This is the SAME wiring
    # `unified_iterative_correction` (line ~1913) and `atom_character_raw`
    # (line ~2243) already carry; this was the one consumer of the three that
    # never got it, which is why #6807 measured it making 25 `_matmul_dim`
    # calls per partition against 0 for the other two.  Exactly the shape of
    # the note two blocks down: "this loop was left behind".
    #
    # `_lp_kernel_steps` returns the trace and the CUMULATIVE log-norm for
    # every step, with the same `max|M| > 1e80` rescale the Python loop below
    # applies, so `M` is never materialised here at all.
    #
    # As in `unified_iterative_correction`, the kernel replaces ONLY the matrix
    # maintenance.  Every line of the accumulation -- `log_cur`, the
    # `scale * (log_cur - log_prev)` delta, `final_tr_sign` -- is the Python
    # below, unchanged and shared.
    _ks = _lp_kernel_steps(entry['partition'], [
        _step_chain_generic(ordering[_k], ordering[:_k], n_gens)
        for _k in range(A)])
    if _ks:
        for _tr, _ln in _ks:
            tr_run = _tr
            log_cur = (_ln + _exact_log(abs(_tr)) if abs(_tr) > 1e-300
                       else log_prev)
            cumul += scale * (log_cur - log_prev)
            log_prev = log_cur
        return (+1 if tr_run > 0 else -1, cumul)

    for kkk in range(A):
        nuc = ordering[kkk]
        prev_types = ordering[:kkk]
        chain = _step_chain_generic(nuc, prev_types, n_gens)
        if sparse_sigmas:
            # Object-dtype fallback (qou-w2vy, 2026-08-31). scipy's sparse
            # kernels are float64-only, so `sig_sparse.dot(M)` raises
            #   TypeError: no supported conversion for types:
            #              (dtype('float64'), dtype('O'))
            # the moment an mpf coefficient promotes M_run to dtype object --
            # which every physical chain does, since _PROTON_G1/_NEUTRON_G1
            # carry d = -h as an mpf. scipy is RIGHT to refuse: the only way to
            # satisfy it is to discard the exact coefficients.
            #
            # This is the SAME fix da645cf0f32 applied to
            # unified_iterative_correction; this loop was left behind, and the
            # crash went unnoticed because binding_energy calls that function
            # FIRST and it never returns for A >= 2, so control never reached
            # here. Accumulating over sigma's nonzeros is O(dim*nnz) -- the same
            # complexity the float64 branch gets from sparse BLAS -- and the
            # densified COO is cached per generator.
            M_run = M
            _sig_coo = {}
            for c, d, gen in chain:
                sig_sparse = sigmas[gen]
                # Unconditional since 2026-09-11 -- see the note in
                # `unified_iterative_correction`.  The scipy sparse-BLAS
                # `else` that stood here was unreachable: every sparse
                # carrier is `_ExactCOO`, so the guard never failed.
                coo = _sig_coo.get(gen)
                if coo is None:
                    _m = sig_sparse.tocoo()
                    coo = (_m.row, _m.col, _m.data)
                    _sig_coo[gen] = coo
                rows_i, cols_j, vals = coo
                # object dtype: a float64 Msig would truncate mpf.
                Msig = np.zeros(M_run.shape, dtype=object)
                for i, j, v in zip(rows_i, cols_j, vals):
                    Msig[:, j] += M_run[:, i] * v
                M_run = c * Msig + d * M_run
            M = M_run
        else:
            M_step = _identity(dim)
            for c, d, gen in chain:
                M_cross = _crossing_in_partition(c, d, gen, sigmas, dim)
                M_step = _matmul_dim(M_step, M_cross, dim)
            M = _matmul_dim(M, M_step, dim)

        if isinstance(M, np.ndarray):
            m_max = max(abs(x) for x in M.flat)
        else:
            m_max = max(abs(M[i][j]) for i in range(dim) for j in range(dim))
        if m_max > 1e80:
            if isinstance(M, np.ndarray):
                M = M / m_max
            else:
                M = tuple(tuple(M[i][j]/m_max for j in range(dim))
                          for i in range(dim))
            log_norm += _exact_log(m_max)

        tr_run = _trace_dim(M, dim)
        if abs(tr_run) > 1e-300:
            log_cur = log_norm + _exact_log(abs(tr_run))
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
    # PRECISION (2026-09-12, "excise float64"): this read `float(h)` --
    # AGENTS.md's banned pattern verbatim (`hf = float(G.h)` followed by
    # arithmetic against it is a computation, not a display).  `h` is already
    # the float64 `q0 - qi`, so the cast was a no-op and the arithmetic was
    # the defect.  `_H_MP` is the mpf twin the module already imports.
    hbar_like = _H_MP  # h = q − q⁻¹
    tr_sign_l, cumul_l = _contrib_single_partition(Z, N, entry_lambda)
    tr_sign_c, cumul_c = _contrib_single_partition(Z, N, entry_conj)
    # Cross-scale: h × geometric mean of individual scales
    scale_l = entry_lambda['C_lambda_resolvent_MeV']
    scale_c = entry_conj['C_lambda_resolvent_MeV']
    # Effective scale uses h × geometric mean; retains sign via log
    sign_l = 1 if scale_l >= 0 else -1
    sign_c = 1 if scale_c >= 0 else -1
    # `mp.sqrt`, not `math.sqrt`: the latter returns a Python float WHATEVER
    # it is handed, so it narrowed an mpf MeV scale to 53 bits here.
    geom_mean = _mp.sqrt(abs(scale_l * scale_c))
    cross_scale_mev = hbar_like * geom_mean * sign_l * sign_c
    # Cross contribution: h × (cumul_l + cumul_c) / 2 weighted by mean scale.
    # Equivalent expression: h × average of per-partition corrections.
    # Apply complementary slackness: at least ONE of the pair must be tight
    # for the cross term to contribute (conservative gate).
    tight_either = (tr_sign_l <= 0) or (tr_sign_c <= 0)
    if not tight_either:
        cross = _mp.mpf(0)
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

    🛑 THIS FUNCTION STILL CARRIES THE DISPROVED SIGN GATE (2026-09-12).
    `tight = (tr_sign <= 0)` below, and the conjugate-pair cross terms
    gated on it, are the same selection that was removed from
    `unified_iterative_correction`, on the same complementary-slackness
    argument, which is refuted sorry-free in
    `QOU.MassTheory.UICGateNotFromComplementarySlackness` (PR #7251).

    It was NOT changed in that pass because this function has **zero code
    callers** anywhere in the tree (measured 2026-09-12; classified
    EXPLORATORY with "no canonical caller" in
    `docs/audits/2026-05-24-hecke-core-canonical-audit.md` row 63), so
    changing it would move no published number while costing a re-run
    nobody consumes.  Do not read the gate's survival here as evidence it
    is justified.  Tracked as bean `qou-px38`.

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
        total_at_j_cross = _mp.mpf(0)
        seen_pairs = set()
        # PRECISION (2026-09-12, "excise float64"): `float(h)` followed by
        # arithmetic is AGENTS.md's banned pattern; `_H_MP` is the mpf twin.
        hbar_like = _H_MP
        for entry in active_at_j:
            lam = tuple(entry['partition'])
            conj = partition_conjugate(lam)
            if conj == lam:
                # Self-conjugate: Wigner-2 coefficient h/2 coupling.
                # tr(σ)/dim = h/2 ⇒ contribution scale ~ h/2 × cumul
                tr_sign, cumul = cumul_by_partition[lam]
                tight = (tr_sign <= 0)
                if tight:
                    cross = (hbar_like / 2) * cumul
                    total_at_j_cross += cross
                else:
                    cross = _mp.mpf(0)
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
                    cross = hbar_like * (cumul_l + cumul_c) / 2
                    total_at_j_cross += cross
                else:
                    cross = _mp.mpf(0)
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
    audit (`mass-endomorphism-tower-adjacency-audit` -- RETIRED, never existed
    as a block; record in docs/audits/2026-10-11-retired-label-records.md §C).

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
    trace = _mp.mpf(0)
    for lam, (chi_q, ln, entry) in chi_data.items():
        # `mp.exp`, not `math.exp`: `ln` is an mpf log-norm carried out of
        # `atom_character_raw`'s `workdps(COMPUTE_DPS)` block, and `math.exp`
        # returns a Python float WHATEVER it is handed -- so this rescale
        # narrowed every partition's character to 53 bits, on the
        # `binding_from_frobenius_pairing` leg of `binding_energy`.
        # (2026-09-12, "excise float64"; bean `qou-oiz3`.)
        chi_eff = chi_q * _mp.exp(ln - max_ln)
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
    norm_sq = _mp.mpf(0)
    for lam, (chi_q, ln, entry) in chi_data.items():
        # Rescaled χ to the common exponent max_ln
        # `mp.exp`, not `math.exp`: `ln` is an mpf log-norm carried out of
        # `atom_character_raw`'s `workdps(COMPUTE_DPS)` block, and `math.exp`
        # returns a Python float WHATEVER it is handed -- so this rescale
        # narrowed every partition's character to 53 bits, on the
        # `binding_from_frobenius_pairing` leg of `binding_energy`.
        # (2026-09-12, "excise float64"; bean `qou-oiz3`.)
        chi_eff = chi_q * _mp.exp(ln - max_ln)
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


def sdp_cross_channel_contribution(Z, N, k_cap=None, jet_max=None, *, as_mpf=False):
    """Compute SDP-derived cross-channel energy contribution (MeV).

    Runs the SDP with atom observables over all active conjugate pairs
    (both partitions at k ≤ k_cap, jet ≤ jet_max, both mixing).
    Each pair's coupling c_ij* contributes c_ij × m_e to the binding
    energy via the categorical identity

        ΔB_pair = m_e · |c_ij*|

    Self-conjugate partitions get the Wigner-2 h/2 contribution
    as the diagonal coupling.

    Returns total contribution (MeV) and per-pair breakdown.

    `as_mpf=True` accumulates in mpf. The self-conjugate h/2 terms are then
    exact algebra at the working precision (`_H_MP`, mpf `M_E_MEV`, mpf
    Wedderburn weight). The cross-block couplings `c_ij` are the output of a
    float64 conic solver (cvxpy / SCS), but each is pinned by a hard equality
    constraint (`c_ij == target_c`) in a problem that is always feasible and
    bounded, so its exact value is the closed form. Under as_mpf that closed
    form (`c_ij_exact`, computed in mpf by `sdp_with_atom_observables`) is
    used, and no solver digit reaches the total. The solver still runs; its
    status gates the term exactly as before.
    """
    zero = _mp.mpf(0) if as_mpf else 0.0
    if k_cap is None:
        k_cap = K_PARTITION_MAX
    try:
        from sdp_cross_channel import sdp_with_atom_observables
    except ImportError:
        return zero, []

    active = [e for e in _PARTITION_TABLE
              if e.get('k', 0) <= k_cap
              and e.get('dim', 0) >= 2
              and e.get('has_ysn', False)
              and (jet_max is None or e.get('jet', 0) <= jet_max)]

    # Build pair list (non-self-conjugate); self-conjugate handled via h/2
    pair_couplings = []
    self_conj_indices = []
    seen = set()
    h_val = float(h)  # float64-ok: Clarabel SDP solver float64 input
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
        return zero, []

    sol = sdp_with_atom_observables(Z, N, active, pair_couplings)
    if sol.get('status') not in ('optimal', 'optimal_inaccurate'):
        return zero, []

    # Sum |c_ij| across pairs, scale by m_e
    total_mev = zero
    per_pair = []
    for cb in sol['cross_blocks']:
        c = cb['c_ij']
        if as_mpf:
            # c_ij is fixed by a hard equality in the SDP, so its exact value
            # is the closed form `c_ij_exact` (mpf), not the SCS iterate.
            c = cb['c_ij_exact']
        contribution = M_E_MEV * abs(c)
        total_mev += contribution
        per_pair.append({
            'lambda_i': cb['lambda_i'],
            'lambda_j': cb['lambda_j'],
            'c_ij': c,
            'contribution_MeV': contribution,
            'solver_limited': not as_mpf,
        })

    # Self-conjugate h/2 contribution (Wigner-2): exact algebra, so under
    # as_mpf it uses the mpf h rather than the float64 solver input h_val.
    h_term = _H_MP if as_mpf else h_val
    for i in self_conj_indices:
        e = active[i]
        mu = e['q_laplacian_eigenvalue']
        # Self-conj partition: effective coupling at Wigner-2 scale
        #   h/2 · w_λ · m_e (matches DELTA_W2 formula)
        w_lam = e['wedderburn_weight']
        contribution = M_E_MEV * w_lam * h_term / 2
        total_mev += contribution
        per_pair.append({
            'lambda_i': list(e['partition']),
            'lambda_j': list(e['partition']),
            'c_ij': h_term / 2,
            'self_conjugate': True,
            'contribution_MeV': contribution,
        })

    return total_mev, per_pair


def binding_energy(Z, N, *, sdp=True, frobenius=True, as_mpf=False, parts=None):
    """Binding energy (MeV) via the categorical path.

    `as_mpf=True` returns the accumulated value as `mpf` instead of casting it
    to the public float contract below, for callers that serialize with
    `_precision.fmt`. The default is unchanged.

    B = unified_iterative_correction(Z,N)                      [LP-dual shadow]
      + sdp_cross_channel_contribution(Z,N)    (if sdp)        [SDP couplings]
      + binding_from_frobenius_pairing(Z,N)    (if frobenius)  [Markov trace]

    Replaces the retired 11-term Bethe-Weizsäcker formula path.
    """
    _warn_if_kernel_absent()
    A = Z + N
    if A <= 1:
        return _mp.mpf(0) if as_mpf else 0.0
    B = unified_iterative_correction(Z, N, as_mpf=as_mpf)
    if parts is not None:
        parts['lp_shadow_MeV'] = B
    if sdp:
        sdp_contrib, per_pair = sdp_cross_channel_contribution(Z, N, as_mpf=as_mpf)
        B += sdp_contrib
        if parts is not None:
            parts['sdp_MeV'] = sdp_contrib
            parts['sdp_solver_limited_MeV'] = sum(
                (p['contribution_MeV'] for p in per_pair if p.get('solver_limited')),
                _mp.mpf(0) if as_mpf else 0.0)
    if frobenius:
        fp = binding_from_frobenius_pairing(Z, N)
        B += fp
        if parts is not None:
            parts['frobenius_MeV'] = fp
    # Public contract is a float, and has always been. The Rust kernel makes the
    # accumulator carry mpf internally, and an mpf reaching a witness raises
    # `TypeError: Object of type mpf is not JSON serializable` at
    # `hadron_knot_table.py`'s `round(B, 4)` (Copilot, #6427 — verified).
    #
    # The cast belongs HERE, not at the kernel boundary as suggested: coercing
    # the kernel's output would discard the 50-dps the kernel exists to carry,
    # through the whole accumulation. Casting at the public return keeps the
    # precision everywhere it can still be used.
    #
    # The note that stood here said the cast "costs nothing measurable either
    # way" because `log_cur = s['log_norm'] + math.log(abs(tr_run))` already
    # narrowed to float64 inside the accumulator, so this path was
    # "float64-limited well upstream of here".  That was true when written and
    # is FALSE now: the narrowing it describes is fixed — `_exact_log` at the
    # three accumulator sites, plus the `workdps(COMPUTE_DPS)` wrapper that
    # stops the ambient dps 15 undoing it.  So this cast is now the ONLY
    # narrowing on the path, and it costs whatever the accumulation carried,
    # which is measured in the hundreds of significand bits rather than 53.
    # It stays because the public contract is a float (bean `qou-sv7h`).
    if as_mpf:
        return B
    return float(B)  # float64-ok: public return boundary after mpf accumulation


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
    M_const = Z * M_P_MEV + N * m_n_derived_3input + Z * M_E_MEV
    phi = compute_phi1_full(Z, N)
    return M_const + KAPPA * phi, phi

