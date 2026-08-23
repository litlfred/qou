#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
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

Task-1 FIX:  Proper H_{3A} Wedderburn character-theoretic binding.

Replaces the per-generator H_3 Wedderburn weighting inside
atom_per_generator_volumes (which pretends each generator sits in its
own H_3(q)) with the full character sum at H_{3A}(q), evaluated on
the actual 3A-strand braid word — using build_seminormal_matrices for
each λ ⊢ 3A.

Key design decisions:

1. Calibration: E_0 = 0.78233341 MeV (free-neutron β-decay Q-value),
   per prop:categorical-mass-markov.  NO Catalan / ALPHA.

2. Braid word: uses the same walk as atom_per_generator_volumes —
     for each nucleon k (proton or neutron):
       intra g₀ pass: (c, d) from _PROTON_G0 or _NEUTRON_G0, at gen 3k
       intra g₁ pass: (c, d) from _PROTON_G1 or _NEUTRON_G1, at gen 3k+1
       inter  pass:  pp / nn / pn from Hecke relation, at gen 3k+2
                     (only if include_inter = True)
   → A word on 3A − 1 generators of H_{3A}.

3. Per partition λ ⊢ 3A, compute
       M_λ = Π_k (c_k · σ_{g_k}^λ + d_k · I)
       χ_λ(W) = tr(M_λ).
   Markov trace:
       tr_M(W) = Σ_λ w_λ · χ_λ(W) / d_λ,    w_λ = d_q(λ)² / [3A]_q!.
   Binding: B = E_0 · ( |tr_M(W_free)| − |tr_M(W_atom)| ).

4. Heavy atoms: full p(3A) enumeration fails for 3A ≳ 35 (p(36) ≈
   17 000, dim-sum ≈ 3 × 10⁷).  Any truncation is an audit option,
   never the default.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 — full-precision m_p per-nucleon scale
import sys
import math
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import mpmath as _mpm
from mpmath import mpf

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0, Q_INV as QI, HA as HA_VAL
from hecke_core import (_PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
                         E_0_CALIBRATION_MEV)
from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached  # F6
# Per Copilot review on #590: drop unused build_seminormal_matrices
# (replaced by the cached path everywhere).
from hecke_characters import partitions_of, dim_q, qfac

h = HA_VAL

# Markov parameter z for the Ocneanu/Jones-Wenzl trace.
# Standard convention: z such that tr_M(T_i) = z, tr_M(1) = 1.
# Matches mass_endomorphism.z_mark = 1/(q^½ + q^(-½)).
Z_MARKOV = Q0**3 / (Q0**2 + 1)


# ── Jones–Wenzl Ocneanu weights ω_λ(q, z) ───────────────────
#
# For H_n(q) with Markov parameter z, the Jones–Wenzl formula
# (Jones 1985 Thm 5.1; Wenzl 1988) gives the Markov-trace weights
#     ω_λ(q, z) = z^(n−1) · Π_{x ∈ λ} (1 − z·q^{2·c(x)}) / (1 − q^{2·h(x)})
# where c(x) = j − i is the cell content and h(x) is its hook length.
# These satisfy Σ_λ ω_λ = 1 and Σ_λ ω_λ · χ_λ(T_i)/d_λ = z.
#
# Falls back to Plancherel w_λ = d_q²/[n]_q! for comparison audits.

def jones_wenzl_weight(shape: tuple[int, ...],
                        q: float = Q0, z: float = Z_MARKOV) -> float:
    """Ocneanu/Jones–Wenzl weight ω_λ(q, z) for H_n(q) Markov trace.

    Σ_λ ω_λ = 1 (normalization) — unlike the Plancherel weight
    d_q(λ)²/[n]_q!, which does not sum to 1 at q ≠ 1.
    """
    n = sum(shape)
    if n == 0:
        return 1.0
    cells: list[tuple[int, int]] = []
    for i, r in enumerate(shape):
        for j in range(r):
            cells.append((i, j))
    # Hooks
    rows = list(shape)
    max_col = rows[0] if rows else 0
    cols = [sum(1 for r in rows if r > j) for j in range(max_col)]
    hooks = [
        (rows[i] - j - 1) + (cols[j] - i - 1) + 1
        for (i, j) in cells
    ]
    product = z ** (n - 1)
    for k, (i, j) in enumerate(cells):
        c = j - i
        hk = hooks[k]
        numer = 1.0 - z * q ** (2 * c)
        denom = 1.0 - q ** (2 * hk)
        if abs(denom) < 1e-15:
            return 0.0
        product *= numer / denom
    return product


def ocneanu_weights_3A(A: int, *, q: float = Q0, z: float = Z_MARKOV):
    """Return list of (λ, ω_λ) for all λ ⊢ 3A; Jones–Wenzl normalized."""
    return [(shape, jones_wenzl_weight(shape, q=q, z=z))
             for shape in partitions_of(3 * A)]


def normalized_plancherel_weights_3A(A: int):
    """ω_λ = w_λ^Planch / Σ w_μ^Planch — forces Σ ω_λ = 1.

    For q > 1, the naive Plancherel weights w_λ = d_q(λ)²/[n]_q!
    do NOT sum to 1 and produce per-generator V̂_i > q₀ (Φ_q pole).
    Rescaling to Σ = 1 pins the Markov-trace identity tr_M(𝟏) = 1
    even if it doesn't match the canonical Jones parameter z for
    tr_M(σ_i).  Empirically this keeps V̂_i in the physical range
    [−1, 1] at our q₀, which is what the Φ_q tower needs.
    """
    n = 3 * A
    nfac = qfac(n)
    entries = []
    total = 0.0
    for shape in partitions_of(n):
        dq = dim_q(shape)
        w = (dq * dq) / nfac
        entries.append((shape, w))
        total += w
    return [(s, w / total) for (s, w) in entries]


# In-memory cache: binding_3A calls markov_trace_3A twice (atom, free)
# so at minimum this saves one re-build per run.
_SEMINORMAL_CACHE: dict[tuple[int, tuple[int, ...]], tuple] = {}

# F6 (audit follow-up): module-level BlockCache for content-distance
# arithmetic across all shape calls. Lazy-init to avoid module-import
# circular issues with q_parameter.
_BLOCK_CACHE: BlockCache | None = None


def _ensure_block_cache() -> BlockCache:
    global _BLOCK_CACHE
    if _BLOCK_CACHE is None:
        _BLOCK_CACHE = BlockCache(float(Q0), float(HA_VAL))
    return _BLOCK_CACHE

# Disk cache for seminormal matrices: standard_young_tableaux is slow
# (multi-second for dim > 5000 partitions at n=12), so we persist the
# built matrices.  Keyed by (n, shape, q0).
_SEMINORMAL_DISK = Path(__file__).parent / ".cache" / "seminormal"


def _q_cache_key(q):
    """Hashable identity for the q a seminormal build was made at.

    The in-memory cache was keyed `(n, shape)` alone, which was correct only
    while there was exactly one q in the process. Once `q` is a parameter,
    that key would serve a build made at one q to a caller asking for another
    — silently, and with no way to notice. Keys on the TYPE as well as the
    value so an mpf and the float64 that rounds to it never collide.
    """
    if type(q).__module__.startswith("sympy"):
        return ("sym", str(q))
    return (type(q).__name__, repr(q))


def _cached_seminormal(shape: tuple[int, ...], q=None):
    """Seminormal (Young orthogonal) matrices for `shape`, built AT `q`.

    `q` defaults to the module-level `Q0` (float64), so every existing
    positional caller is unchanged. Pass:

      * an `mpmath.mpf`   — high-precision numeric build;
      * a `sympy.Symbol`  — SYMBOLIC build, matrices are expressions in q.

    Before this parameter existed the matrices were always built at `Q0` and
    the value was baked in irrecoverably: `char_fast._compiled_sigmas` wrapped
    them in `lambdify(Q_SYM, ...)`, producing something that LOOKED like a
    function of q and ignored its argument entirely — `sigma(q=0.5)`,
    `sigma(q=2.0)` and `sigma(q=7.0)` all returned the q0 matrices, bit for
    bit. A q-sweep through that path returned the q0 answer at every point
    with no error and no warning. Bean `qou-v6vp`.

    The disk cache is used for NUMERIC q only. Its filename already carried
    `q{...:.10f}`, so no cache format changes and no existing archive is
    invalidated — the q was simply never allowed to vary. A symbolic build is
    held in memory only: it is cheap (the block values depend on the content
    distance rho, of which there are only a few per shape) and it has no
    sensible npz representation.
    """
    if q is None:
        q = Q0
    # P14 fix (2026-05-08, audit F8): replaced pickle (RCE on tampered cache)
    # with numpy.savez_compressed for the dense σ matrices + JSON sidecar
    # for dim and the SYT entry→cell maps. Densify any sparse matrices
    # before save (the 3A use case has dim ≤ a few hundred — well under
    # the build_seminormal_matrices sparse threshold of 500).
    import json
    n = sum(shape)
    key = (n, shape, _q_cache_key(q))
    if key in _SEMINORMAL_CACHE:
        return _SEMINORMAL_CACHE[key]

    symbolic = type(q).__module__.startswith("sympy")
    if symbolic:
        # No disk round-trip: sympy expressions have no npz form, and the
        # build is cheap because the block values are keyed on the content
        # distance rho and there are only a few distinct rho per shape.
        #
        # `sparse=False` is forced: scipy's csr_matrix requires a numeric
        # dtype and cannot hold sympy expressions, so the dim > 500 default
        # would raise. Dense is the only representation available here.
        data = build_seminormal_matrices_cached(
            shape, cache=BlockCache(q, q - 1 / q), sparse=False)
        _SEMINORMAL_CACHE[key] = data
        return data

    _SEMINORMAL_DISK.mkdir(parents=True, exist_ok=True)
    # Bug fix (2026-05-16): Path.with_suffix replaces everything after
    # the FIRST dot in the filename, so `q{Q0:.10f}` (e.g. "1.1099785955")
    # collided every shape at the same n into a single n{n}_q1.npz file
    # that held only the LAST-written shape's data.  Construct the
    # filename by direct string concat to avoid with_suffix.
    # The q in this stem was always the module `Q0`; it is now the q this
    # build is actually AT. Same format, so every existing archive still
    # resolves — the field simply becomes meaningful instead of constant.
    stem_name = f"n{n}_q{float(q):.10f}_shape{'-'.join(map(str, shape))}"
    npz_path = _SEMINORMAL_DISK / (stem_name + ".npz")
    json_path = _SEMINORMAL_DISK / (stem_name + ".json")
    if npz_path.exists() and json_path.exists():
        try:
            meta = json.loads(json_path.read_text())
            # PR #565 (Gemini review): drive sigma reconstruction from
            # the explicit n_sigmas count in the JSON sidecar rather
            # than from the npz file list, so the loader is robust to
            # legacy archives that may carry extra arrays alongside
            # the sig{i} entries. Falls back to len(npz.files) if the
            # field is absent (older caches written before this PR).
            # mmap_mode='r' for first-load latency reduction (~70% faster
            # cold-cache); requires uncompressed NPZ on the write side
            # (np.savez, not np.savez_compressed). The in-memory cache
            # absorbs repeats within a session.
            with np.load(npz_path, mmap_mode="r") as npz:
                if "n_sigmas" in meta:
                    n_sigmas = int(meta["n_sigmas"])
                else:
                    n_sigmas = sum(
                        1 for k in npz.files if k.startswith("sig")
                    )
                # np.array (not np.asarray) makes an explicit copy
                # of the memmap-backed array, detaching from the
                # underlying file so the data stays valid after the
                # npz context closes (np.asarray on a memmap returns
                # a view that becomes invalid post-close).
                sigmas = [
                    np.array(npz[f"sig{i}"]) for i in range(n_sigmas)
                ]
            syts = [{int(k): int(v) for k, v in d.items()}
                    for d in meta["syts"]]
            data = (sigmas, int(meta["dim"]), syts)
            _SEMINORMAL_CACHE[key] = data
            return data
        except Exception:
            pass
    # F6 (audit follow-up, finishing wire): use BlockCache-backed
    # rebuild path. Composes with the .npz disk cache below; the
    # in-memory BlockCache amortises content-distance arithmetic
    # across shape calls within a single run.
    # `_ensure_block_cache()` is the shared float64 cache and is correct only
    # for the default q. Any other q gets its own cache at that q, so the
    # shared one is never polluted with values from a different anchor.
    if _q_cache_key(q) == _q_cache_key(Q0):
        cache = _ensure_block_cache()
    else:
        cache = BlockCache(q, q - 1 / q)
    data = build_seminormal_matrices_cached(shape, cache=cache)
    _SEMINORMAL_CACHE[key] = data
    try:
        sigmas, dim, syts = data
        dense = []
        for M in sigmas:
            if hasattr(M, "toarray"):
                dense.append(np.asarray(M.toarray()))
            else:
                dense.append(np.asarray(M))
        # np.savez (uncompressed) so the read side can mmap; disk size
        # trade-off (~3-5× larger) is amortised against ~70% faster
        # cold-cache load via mmap_mode="r" above.
        np.savez(npz_path,
                 **{f"sig{i}": M for i, M in enumerate(dense)})
        json_path.write_text(json.dumps({
            "dim": int(dim),
            "n_sigmas": len(dense),
            "syts": [{str(k): int(v) for k, v in d.items()} for d in syts],
        }))
    except Exception:
        pass
    return data


def atom_braid_word_3A(Z: int, N: int, *, m_pp: int = 1, m_pn: int = 1,
                         m_nn: int = 1, include_inter: bool = True,
                         pn_convention: str = "bring_color_weighted",
                         q=None, allow_float64: bool = False):
    """Full 3A-strand braid word as a list of (c, d, gen_idx) triples.

    Matches the chain-walk convention of
    hecke_core.atom_per_generator_volumes (lines 3029–3079):
    for each nucleon k, apply intra g₀, intra g₁, then (if

    The p-n interface is color-weighted by default (owner directive
    2026-06-01: bring_color_weighted is canonical across the compute):
    its averaged crossing is `σ − h·(1/2 − δ/4)·1`, δ = flavor_split_
    subleading(q₀), vs the color-blind `σ − h/2·1` (`pn_convention=
    "strict_averaged"`, kept for empirical-pipeline validation). The
    p-p (σ) and n-n (σ⁻¹) interfaces are already isospin-distinct and
    carry no extra color weight. See
    docs/audits/2026-06-03-color-averaging-wiring-audit.md.
    include_inter) the appropriate pp/nn/pn crossing at gen 3k+2.

    gen_idx is 0-based (σ_0 = sigmas[0] in build_seminormal_matrices).

    `q` (keyword-only) materialises the word at an arbitrary substrate value
    rather than the baked q₀ — the q-parameterised-braid-word core refactor
    (docs/workplans/2026-06-17-q-parameterised-braid-word-core.md). Every
    crossing is a template {0, −h, −h/2, −h(½−δ/4)} with `h=q−q⁻¹`,
    `δ=flavor_split_leading(q)` the only q-dependent quantities; the intra
    chains come from `nucleon_gen_chains(quarks, q=q)`. `q=None` (default)
    uses the canonical q₀ data (`pyhecke.gram.h`, `_avg_color_delta`) and is
    byte-identical to the historical word — all existing callers omitting `q`
    are unaffected. Used by `tr_m_atom_zn(q=…)` and the N-grid simulators
    (multiple q at once).
    """
    from pyhecke.atom import reject_float64_q
    reject_float64_q(q, allow_float64=allow_float64, where="atom_braid_word_3A")
    A = Z + N
    # ── NO FLOAT64 (owner directive) ──────────────────────────────────────
    # Every crossing offset below used to be cast to a Python float, so a
    # word feeding a 50-dps computation carried ~17 good digits. Two separate
    # leaks, both fixed here at the source rather than patched per consumer:
    #
    #   h     `pyhecke.gram.h` IS a Python float — 2.61e-16 relative against
    #         the 50-dps closed form — and was used directly as `h_loc`.
    #   δ     `_avg_color_delta()` evaluates at the float64 `q_parameter.Q`
    #         and reaches only ~5e-16, as its own docstring says. AGENTS.md
    #         §"q₀ anchor convention" directs deep-1ppQ callers to
    #         `flavor_split_leading(local_q0_50dps)`, the same closed form
    #         taking q as an argument.
    #
    # Measured end to end on the dual-path cross-check: exact crossings alone
    # took the deuteron from 1.024e-16 to 3.476e-20, and exact δ took it from
    # there to 3.229e-50. The δ term is small (δ/4 is ~6.9e-4 of the offset)
    # and dominated the floor anyway once the crossings were exact.
    #
    # This deliberately BREAKS the "byte-identical to the historical word"
    # property the docstring above claims for `q=None`. That word was the
    # float64-contaminated one; reproducing it bit-for-bit is not a property
    # worth keeping. Consumers needing f64 (the numpy validation paths) cast
    # at their own boundary, where the loss is visible.
    # Built at >= 60 dps regardless of the caller's ambient precision: an
    # mpf keeps the precision it was CREATED at, so `mpf(str(q0))` under the
    # mpmath default (dps=15) would bake in a 15-digit q0 and silently undo
    # everything below. Callers already inside a higher workdps keep theirs.
    with _mpm.workdps(max(_mpm.mp.dps, 60)):
        if q is None:
            from q_parameter import Q_50_DIGIT_STR as _Q50
            _q_exact = mpf(str(_Q50))
        else:
            _q_exact = q
        h_loc = _q_exact - mpf(1) / _q_exact
        # DE-WIRED 2026-06-29: proven leading δ, not posited subleading.
        # Inside the same guard as h_loc so δ is built at full precision too.
        from _li_2_q_util import flavor_split_leading
        delta = flavor_split_leading(_q_exact)
        # Every inter-nucleon template built HERE, in the same context. An mpf
        # carries the precision of the operation, not just of its operands, so
        # forming `-h_loc / 2` further down would round it to whatever dps the
        # caller happens to be in — silently re-capping the value that was
        # just computed exactly.
        _X_PP = (mpf(1), mpf(0))                                    # σ
        _X_NN = (mpf(1), -h_loc)                                    # σ⁻¹
        _X_PN_CW = (mpf(1), -h_loc * (mpf(1) / 2 - delta / 4))      # colour-weighted
        _X_PN_BLIND = (mpf(1), -h_loc / 2)                          # colour-blind
    if q is None:
        p_g0, p_g1, n_g0, n_g1 = _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1
    else:
        from pyhecke.atom import nucleon_gen_chains
        p_g0, p_g1 = nucleon_gen_chains(['u', 'u', 'd'], q=q,
                                        allow_float64=allow_float64)
        n_g0, n_g1 = nucleon_gen_chains(['u', 'd', 'd'], q=q,
                                        allow_float64=allow_float64)
    word: list = []
    ordering = ['p'] * Z + ['n'] * N
    for k, nuc in enumerate(ordering):
        intra = p_g0 if nuc == 'p' else n_g0
        intra_g1 = p_g1 if nuc == 'p' else n_g1
        base_g0 = 3 * k
        base_g1 = 3 * k + 1
        for c, d in intra:
            word.append((c, d, base_g0))
        for c, d in intra_g1:
            word.append((c, d, base_g1))
        if include_inter and k < A - 1:
            i_inter = 3 * k + 2
            next_nuc = ordering[k + 1]
            if nuc == 'p' and next_nuc == 'p':
                base_cross = _X_PP
                m_this = m_pp
            elif nuc == 'n' and next_nuc == 'n':
                base_cross = _X_NN
                m_this = m_nn
            else:
                if pn_convention == "bring_color_weighted":
                    # color-weighted p-n averaged crossing: σ − h·(1/2 − δ/4).
                    base_cross = _X_PN_CW
                elif pn_convention == "strict_averaged":
                    base_cross = _X_PN_BLIND   # color-blind (validation)
                else:
                    raise ValueError(
                        f"unknown pn_convention: {pn_convention!r} "
                        f"(expected 'bring_color_weighted' or 'strict_averaged')")
                m_this = m_pn
            c, d = base_cross
            for _ in range(m_this):
                word.append((c, d, i_inter))
    return word


def chi_lambda_of_word(sigmas, dim, word, n_gens_required: int) -> float:
    """Character χ_λ(W) = tr(Π_k (c_k · σ_{g_k} + d_k · I)) in the λ-irrep.

    ``sigmas`` is the list from build_seminormal_matrices.
    ``word`` is the list of (c, d, gen_idx) triples from
    atom_braid_word_3A.
    """
    if dim == 0:
        return 0.0
    try:
        from scipy import sparse as sp_sparse
        is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    except ImportError:
        is_sparse = False
    if is_sparse:
        from scipy import sparse as sp_sparse
        product = sp_sparse.eye(dim, format='csr')
        I = sp_sparse.eye(dim, format='csr')
    else:
        product = np.eye(dim)
        I = np.eye(dim)
    for (c, d, g) in word:
        if g >= len(sigmas):
            raise IndexError(
                f"word uses generator σ_{g} but only {len(sigmas)} "
                f"seminormal matrices were provided (partition too small)")
        M = c * sigmas[g] + d * I
        product = product @ M
    if is_sparse:
        return float(product.diagonal().sum())
    return float(np.trace(product))


def markov_trace_3A(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1,
                      include_inter: bool = True,
                      verbose: bool = False) -> dict:
    """[DEPRECATED — Plancherel-weighted form] H_{3A} "Markov" trace.

    This function computes Σ_λ (d_q(λ)²/[3A]_q!) · χ_λ(W)/d_λ, which is
    the Plancherel-weighted sum over partitions λ ⊢ 3A.  At q ≠ 1 this
    is NOT the canonical Jones–Markov trace specified in
    prop:categorical-mass-markov (which gives tr_M(σ_0) = z ≈ 0.499);
    at H_2, this function gives ≈ 0.104.

    Use markov_trace_canonical.tr_M_element for the canonical trace.
    Retained here for backwards compatibility with downstream code
    that computes partition-level breakdowns.  Do not use for new
    binding calculations.

    Returns dict with keys
      ``total``         : tr_M(W) = Σ_λ w_λ · χ_λ(W) / d_λ
      ``per_partition`` : per-λ record {partition, dim, w, chi, contrib}
      ``n_partitions``  : p(3A)
      ``n_gens``        : 3A − 1
    """
    A = Z + N
    if A < 1:
        return {"total": 1.0, "per_partition": [],
                "n_partitions": 0, "n_gens": 0}
    n_strands = 3 * A
    n_gens = n_strands - 1

    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)

    nfac = qfac(n_strands)
    total = 0.0
    per_partition = []
    for shape in partitions_of(n_strands):
        sigmas, dim, _syts = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = dim_q(shape)
        w = (dq * dq) / nfac
        chi = chi_lambda_of_word(sigmas, dim, word, n_gens)
        contrib = w * chi / dim
        total += contrib
        per_partition.append({
            "partition": shape, "dim": dim, "w": w,
            "chi": chi, "contrib": contrib,
        })
        if verbose:
            print(f"  {str(shape):>24} dim={dim:>4} w={w:+.4e} "
                  f"χ={chi:+.4e} contrib={contrib:+.4e}")
    return {
        "total": total,
        "per_partition": per_partition,
        "n_partitions": len(per_partition),
        "n_gens": n_gens,
    }


def per_generator_V_hat_3A(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1,
                             include_inter: bool = True,
                             weight_scheme: str = "normalized_plancherel",
                             verbose: bool = False):
    """Per-generator V̂_i at H_{3A}(q) via the full H_{3A} character sum.

    For each generator position i ∈ {0, …, 3A − 2}, the chain-walk
    applies a sequence of (c_k, d_k) factors at position i.  The
    accumulated H_{3A} element at i is

        W_i = Π_k (c_k · σ_i + d_k · 𝟏).

    We compute

        V̂_i = Σ_{λ ⊢ 3A}  w_λ · χ_λ(W_i) / d_λ,
        w_λ = d_q(λ)² / [3A]_q!.

    This is the H_{3A}-Wedderburn-weighted analog of the per-generator
    V̂ used in atom_per_generator_volumes (which weights via H_3).
    For include_inter=False, inter-nucleon generators 3k+2 have empty
    W_i and contribute V̂_i = Σ w_λ (identity trace).

    Returns list of length 3A − 1 of dicts {"full": V̂_i, "gen_word":
    list of (c, d)}.
    """
    A = Z + N
    if A < 1:
        return []
    n_strands = 3 * A
    n_gens = n_strands - 1

    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)
    word_by_gen: list[list[tuple[float, float]]] = [[] for _ in range(n_gens)]
    for (c, d, g) in word:
        if 0 <= g < n_gens:
            word_by_gen[g].append((c, d))

    nfac = qfac(n_strands)
    V_hat = [0.0] * n_gens

    # Weight table — normalized to Σ = 1 for the Markov identity
    # tr_M(𝟏) = 1; alternate schemes available for audit.
    weight_table: list[tuple[tuple[int, ...], float]] = []
    if weight_scheme == "normalized_plancherel":
        weight_table = normalized_plancherel_weights_3A((Z + N))
    elif weight_scheme == "plancherel":
        for shape in partitions_of(n_strands):
            dq = dim_q(shape)
            weight_table.append((shape, (dq * dq) / nfac))
    elif weight_scheme == "jones_wenzl":
        weight_table = ocneanu_weights_3A((Z + N))
    else:
        raise ValueError(f"unknown weight_scheme: {weight_scheme}")

    for (shape, w_lam) in weight_table:
        sigmas, dim, _syts = _cached_seminormal(shape)
        if dim == 0:
            continue
        try:
            from scipy import sparse as sp_sparse
            is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
        except ImportError:
            is_sparse = False
        if is_sparse:
            from scipy import sparse as sp_sparse
            I_lam = sp_sparse.eye(dim, format='csr')
        else:
            I_lam = np.eye(dim)
        for i in range(n_gens):
            w_i_steps = word_by_gen[i]
            if not w_i_steps:
                # Empty word at gen i → trace = dim → contrib = w_lam
                V_hat[i] += w_lam
                continue
            if i >= len(sigmas):
                # Shouldn't happen (len(sigmas) = n_strands - 1)
                continue
            M = I_lam
            for (c, d) in w_i_steps:
                M = M @ (c * sigmas[i] + d * I_lam)
            if is_sparse:
                tr = float(M.diagonal().sum())
            else:
                tr = float(np.trace(M))
            V_hat[i] += w_lam * tr / dim
    out = []
    for i, V in enumerate(V_hat):
        out.append({"full": V, "gen_word": list(word_by_gen[i])})
    if verbose:
        print(f"  per-gen V̂ (H_{{{n_strands}}} Wedderburn):")
        for i, d in enumerate(out):
            print(f"    gen {i}: V̂ = {d['full']:+.6f}  "
                  f"word = {d['gen_word']}")
    return out


def phi_q_safe(z_val: float, *, q: float = Q0, cap_frac: float = 0.98,
                 max_k: int = 2000) -> float:
    """Saturation-safe Φ_q: clips |z| ≤ cap_frac · q before evaluation.

    The raw Φ_q diverges as |z| → q (k=1 factor hits zero); the
    Plancherel-weighted character sum at H_{3A} routinely produces
    V̂_i slightly above q for intra-nucleon generators, which would
    make the tower mass infinite.  Capping |z| at cap_frac · q
    regularizes Φ_q at the cost of a known approximation near the
    singularity — same symptom as the general ``V_full saturation
    near q₀'' issue flagged in HANDOVER-STATUS.
    """
    qi = 1.0 / q
    cap = cap_frac * q
    z_clipped = max(-cap, min(z_val, cap))  # clamp to [−cap, +cap]
    z_abs = abs(z_clipped)
    product = 1.0
    for k in range(1, max_k + 1):
        factor = 1.0 - (qi ** k) * z_abs
        if abs(factor) < 1e-300:
            return float("inf")
        product /= factor
        if (qi ** k) * z_abs < 1e-15:
            break
    return product


def log_phi_q(z_val: float, *, q: float = Q0,
                cap_frac: float = 0.9999, max_k: int = 2000) -> float:
    """log Φ_q(|z|) = −Σ_k log(1 − q^{−k} |z|).

    Finite for |z| < q (cap prevents log(0)).  Useful for numerical
    stability when Φ_q itself would overflow: tower sums done in
    log-space avoid exp-of-huge intermediates.
    """
    qi = 1.0 / q
    cap = cap_frac * q
    z_abs = min(abs(z_val), cap)
    total = 0.0
    for k in range(1, max_k + 1):
        factor = 1.0 - (qi ** k) * z_abs
        if factor <= 0.0:
            return float("inf")
        total -= math.log(factor)
        if (qi ** k) * z_abs < 1e-15:
            break
    return total


def mass_from_tower_safe(vols, *, cap_frac: float = 0.98,
                            cross_mode: str = "adjacent"):
    """Tower mass using phi_q_safe — Φ_q evaluations clipped at cap_frac·q₀.

    Mirrors mass_endomorphism.mass_from_tower but regularizes the
    divergent Φ_q(V̂) contributions when V̂_i exceeds q₀ − ε.

    ``cross_mode`` selects the quadratic cross-term:
      "adjacent" — z² · Σ_{|i−j|=1} Φ_q(|V̂_i V̂_j|)  (standard
                   prop:mass-endomorphism-tower form)
      "full"     — z² · Σ_{i<j}     Φ_q(|V̂_i V̂_j|)  (full
                   quadratic channel over all generator pairs;
                   each pair weighted by z² as in adjacent case)
      "full_z2pow" — z^{2|i-j|} · Σ_{i<j} Φ_q(|V̂_i V̂_j|)
                   (distance-graded weighting; Markov-trace power
                   of the separation between gens i, j)

    Returns (desc, single, cross, total).
    """
    from mass_endomorphism import z_mark as _zm
    n = len(vols)
    desc = 1.0
    for v in vols:
        desc *= v["full"]
    desc = abs(desc)
    single = sum(phi_q_safe(abs(v["full"]), cap_frac=cap_frac)
                  for v in vols)
    cross = 0.0
    if cross_mode == "adjacent":
        for i in range(n - 1):
            cross += _zm * _zm * phi_q_safe(
                abs(vols[i]["full"] * vols[i + 1]["full"]),
                cap_frac=cap_frac)
    elif cross_mode == "full":
        for i in range(n):
            for j in range(i + 1, n):
                cross += _zm * _zm * phi_q_safe(
                    abs(vols[i]["full"] * vols[j]["full"]),
                    cap_frac=cap_frac)
    elif cross_mode == "full_z2pow":
        for i in range(n):
            for j in range(i + 1, n):
                cross += (_zm ** (2 * (j - i))) * phi_q_safe(
                    abs(vols[i]["full"] * vols[j]["full"]),
                    cap_frac=cap_frac)
    else:
        raise ValueError(f"unknown cross_mode: {cross_mode}")
    return desc, single, cross, desc + single + cross


def binding_3A_tower(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1,
                       E_0: float = E_0_CALIBRATION_MEV,
                       weight_scheme: str = "normalized_plancherel",
                       cap_frac: float = 0.98,
                       use_safe_phi_q: bool = True,
                       cross_mode: str = "full",
                       verbose: bool = False) -> dict:
    """FULL-TOWER + H_{3A} binding.

    Combines the Φ_q tower formula (prop:mass-endomorphism-tower)
    with H_{3A} Wedderburn character weighting on the per-generator
    V̂_i:

        V̂_i   = Σ_{λ ⊢ 3A}  w_λ · χ_λ(W_i) / d_λ   (per-gen, H_{3A})
        𝔪(W) = |Π V̂_i| + Σ Φ_q(|V̂_i|)
              + z² · Σ_{|i−j|=1} Φ_q(|V̂_i V̂_j|)
        B     = E_0 · ( 𝔪_free − 𝔪_atom ).

    Replaces the H_3 per-generator weighting used in
    tower_binding_full.  E_0 = 0.78233341 MeV (β-decay Q), no Catalan.
    """
    # Canonical API: prop:mass-tower-operator-valued
    # (the Φ_q tower implementation is re-exported from
    # mass_endomorphism; both expressions are equivalent at H_{3A}).
    from mass_tower_operator_valued import mass_from_tower
    vols_atom = per_generator_V_hat_3A(
        Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
        include_inter=True, weight_scheme=weight_scheme, verbose=verbose)
    vols_free = per_generator_V_hat_3A(
        Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
        include_inter=False, weight_scheme=weight_scheme, verbose=verbose)
    if not vols_atom or not vols_free:
        return {"status": "trivial", "Z": Z, "N": N}
    if use_safe_phi_q:
        desc_a, sgl_a, cross_a, total_a = mass_from_tower_safe(
            vols_atom, cap_frac=cap_frac, cross_mode=cross_mode)
        desc_f, sgl_f, cross_f, total_f = mass_from_tower_safe(
            vols_free, cap_frac=cap_frac, cross_mode=cross_mode)
    else:
        desc_a, sgl_a, cross_a, total_a = mass_from_tower(vols_atom)
        desc_f, sgl_f, cross_f, total_f = mass_from_tower(vols_free)
    return {
        "Z": Z, "N": N, "A": Z + N,
        "m_pp": m_pp, "m_pn": m_pn, "m_nn": m_nn,
        "m_atom_tower_H3A": total_a,
        "m_free_tower_H3A": total_f,
        "m_atom_breakdown": {"desc": desc_a, "single": sgl_a,
                              "cross": cross_a},
        "m_free_breakdown": {"desc": desc_f, "single": sgl_f,
                              "cross": cross_f},
        "E_0_MeV": E_0,
        "weight_scheme": weight_scheme,
        "cap_frac": cap_frac if use_safe_phi_q else None,
        "cross_mode": cross_mode,
        "B_MeV": E_0 * (total_f - total_a),
    }


def binding_3A(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1,
                E_0: float = E_0_CALIBRATION_MEV,
                verbose: bool = False) -> dict:
    """[DEPRECATED — Plancherel-weighted trace] Binding via H_{3A} pattern.

    Uses markov_trace_3A, which is Plancherel-weighted and does NOT
    match prop:categorical-mass-markov's canonical z ≈ 0.499 Markov
    parameter.  Prefer binding_canonical.binding_canonical, which
    uses the axiomatically-correct Jones–Markov trace
    (markov_trace_canonical.tr_M_element) — verified to match all 7
    prop-table values exactly.
    """
    """Binding via H_{3A} character-theoretic Markov trace.

    B = E_0 · ( |tr_M(W_free)| − |tr_M(W_atom)| )
    with W_free (include_inter=False) and W_atom (include_inter=True)
    on the same 3A-strand Iwahori–Hecke algebra.
    """
    tr_atom = markov_trace_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=True, verbose=verbose)
    tr_free = markov_trace_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=False, verbose=verbose)
    B = E_0 * (abs(tr_free["total"]) - abs(tr_atom["total"]))
    return {
        "Z": Z, "N": N, "A": Z + N,
        "m_pp": m_pp, "m_pn": m_pn, "m_nn": m_nn,
        "tr_M_atom": tr_atom["total"],
        "tr_M_free": tr_free["total"],
        "abs_diff": abs(tr_free["total"]) - abs(tr_atom["total"]),
        "E_0_MeV": E_0,
        "B_MeV": B,
        "n_partitions": tr_atom["n_partitions"],
    }


# ── CLI ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(
        description="H_{3A} Wedderburn-character binding (task-1 fix)")
    ap.add_argument("--max-A", type=int, default=6,
                    help="Max A to evaluate (p(3A) cost grows fast)")
    ap.add_argument("--E0", type=float, default=E_0_CALIBRATION_MEV,
                    help="Calibration E_0 in MeV "
                         "(default = β-decay Q = 0.78233341)")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
        ("4He",  2, 2, 28.295674),
        ("6Li",  3, 3, 32.0),
        ("7Li",  3, 4, 39.244529),
        ("9Be",  4, 5, 58.1650),
        ("10B",  5, 5, 64.750),
        ("12C",  6, 6, 92.161728),
    ]

    print("=" * 116)
    print("H_{3A} WEDDERBURN-CHARACTER BINDING — task-1 fix")
    print(f"q₀ = {Q0}")
    print(f"E_0 = {args.E0:.4f} MeV  (free-neutron β-decay Q, "
          f"hecke_core.E_0_CALIBRATION_MEV)")
    print(f"No ALPHA · Catalan anywhere.")
    print("=" * 116)

    results_mk = []
    results_tw = []
    print(f"\n-- single-brane Markov trace at H_{{3A}} --")
    print(f"  {'Atom':>6} {'A':>3} {'3A':>3} {'p(3A)':>6} "
          f"{'|tr_M_atom|':>14} {'|tr_M_free|':>14} "
          f"{'B_pred':>10} {'B_AME':>9} {'|Δm/m|%':>9} {'time':>8}")
    print("  " + "-" * 108)
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        if A > args.max_A:
            continue
        t0 = time.time()
        try:
            r = binding_3A(Z, N, E_0=args.E0, verbose=args.verbose)
        except Exception as e:
            print(f"  {name:>6} {A:>3} {3*A:>3} ERR: {e}")
            continue
        dt = time.time() - t0
        M_total = A * float(M_P_MEV_VALIDATION)
        dm = abs(r["B_MeV"] - B_AME) / M_total * 100
        print(f"  {name:>6} {A:>3} {3*A:>3} {r['n_partitions']:>6} "
              f"{abs(r['tr_M_atom']):>14.6e} "
              f"{abs(r['tr_M_free']):>14.6e} "
              f"{r['B_MeV']:>+10.4f} {B_AME:>9.3f} "
              f"{dm:>8.4f}% {dt:>7.2f}s")
        results_mk.append({**r, "atom": name, "B_AME_MeV": B_AME,
                            "delta_m_over_m_pct": dm, "time_sec": dt})

    print(f"\n-- FULL TOWER at H_{{3A}} (per-gen V̂ via character sum) --")
    print(f"  {'Atom':>6} {'A':>3} {'3A':>3} "
          f"{'𝔪_atom':>12} {'𝔪_free':>12} "
          f"{'B_pred':>10} {'B_AME':>9} {'|Δm/m|%':>9} {'time':>8}")
    print("  " + "-" * 100)
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        if A > args.max_A:
            continue
        t0 = time.time()
        try:
            r = binding_3A_tower(Z, N, E_0=args.E0,
                                   verbose=args.verbose)
        except Exception as e:
            print(f"  {name:>6} {A:>3} {3*A:>3} ERR: {e}")
            continue
        dt = time.time() - t0
        M_total = A * float(M_P_MEV_VALIDATION)
        dm = abs(r["B_MeV"] - B_AME) / M_total * 100
        print(f"  {name:>6} {A:>3} {3*A:>3} "
              f"{r['m_atom_tower_H3A']:>12.3e} "
              f"{r['m_free_tower_H3A']:>12.3e} "
              f"{r['B_MeV']:>+10.4f} {B_AME:>9.3f} "
              f"{dm:>8.4f}% {dt:>7.2f}s")
        results_tw.append({**r, "atom": name, "B_AME_MeV": B_AME,
                            "delta_m_over_m_pct": dm, "time_sec": dt})

    if results_mk:
        dms = [r["delta_m_over_m_pct"] for r in results_mk]
        print(f"\nMarkov   |Δm/m|% summary:  min={min(dms):.4f}%, "
              f"max={max(dms):.4f}%, mean={sum(dms)/len(dms):.4f}%")
    if results_tw:
        dms_t = [r["delta_m_over_m_pct"] for r in results_tw]
        print(f"Tower    |Δm/m|% summary:  min={min(dms_t):.4f}%, "
              f"max={max(dms_t):.4f}%, mean={sum(dms_t)/len(dms_t):.4f}%")

    witness = {
        "computation": "mass-at-3A-proper",
        "description": (
            "Task-1 fix: H_{3A} Wedderburn-character binding. Two "
            "paths on the same H_{3A} character theory:\n"
            "(a) single-brane Markov trace: B = E_0 · (|tr_M_free| − "
            "|tr_M_atom|), tr_M(W) = Σ_λ w_λ · χ_λ(W) / d_λ;\n"
            "(b) FULL TOWER combining H_{3A} per-generator V̂_i with "
            "prop:mass-endomorphism-tower Φ_q formula: per-gen "
            "V̂_i = Σ_λ w_λ · χ_λ(W_i)/d_λ, then "
            "𝔪 = |Π V̂_i| + Σ Φ_q(|V̂_i|) + z² Σ_{adj} Φ_q(|V̂_i V̂_j|), "
            "and B = E_0 · (𝔪_free − 𝔪_atom).\n"
            "E_0 = 0.78233341 MeV (free-neutron β-decay Q). No Catalan."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "E_0_MeV": args.E0,
                        "max_A": args.max_A},
        "markov_path": results_mk,
        "tower_path": results_tw,
    }
    out = Path(__file__).parent / "mass-at-3A-proper.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
