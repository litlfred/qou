#!/usr/bin/env python3
# DEPRECATION-CANDIDATE: witness was moved to fsh-guts/deprecated/computations/ in PR #554 (dead-exploratory).
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

from codata_constants import (
    AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    M_P_MEV_VALIDATION  # noqa: E402 — full-precision m_p per-nucleon scale,
)
import os
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
# QI / HA_VAL come from the PROTON package constants, not the shim. The shim
# rebinds its whole derived family (HA, Q_INV, HBAR_Q, LN_Q, E_CROSS, …) when
# the entry-point stem is manifest-listed, so importing any of them here made
# this module's `h = q − q⁻¹` a function of whoever is __main__ (bean qou-wee5).
from qou_substrate.constants import Q_INV as QI, HA as HA_VAL  # noqa: E402
# ANCHOR-INDEPENDENT proton q0. `q_parameter.Q` above is the SHIM's Q, which the
# shim REBINDS to the muon value when the running process's argv stem is listed
# in `q0_anchor_manifest.json::ideal_muon` (or QOU_Q0_ANCHOR=ideal). That makes
# it a function of the ENTRY POINT, not of this module — which is how a probe
# that never references the manifest moved 113 ppb when a stem was added to it
# (bean `qou-wee5`). `qou_substrate.constants.Q` is not rebound: measured under
# QOU_Q0_ANCHOR=ideal, the shim gives 1.1099785955573347 while this gives
# 1.1099785827513808. Use THIS for anything that must not track its caller.
from qou_substrate.constants import (  # noqa: E402
    Q as Q0_PROTON, HA as HA_PROTON,
)
from hecke_core import (_PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
                         E_0_CALIBRATION_MEV)
from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached  # F6
# Per Copilot review on #590: drop unused build_seminormal_matrices
# (replaced by the cached path everywhere).
from hecke_characters import partitions_of, dim_q, qfac

h = HA_VAL

# Canonical-q₀ intra words, one per `intra_order`, built on first use. The
# `_PROTON_G0`/`_NEUTRON_G0` constants above are the same letters bucketed by
# generator; they cannot express the interleaving, which is the whole point of
# `nucleon_word_letters` (bean `qou-hu1f`). Cached for the same reason those
# constants are: `nucleon_gen_chains` rebuilds at 60 dps on every call.
_NUCLEON_WORDS_Q0: dict = {}


def _nucleon_words_q0(intra_order: str):
    """`(proton_word, neutron_word)` at the canonical q₀, memoised per order."""
    if intra_order not in _NUCLEON_WORDS_Q0:
        from pyhecke.atom import nucleon_word_letters
        _NUCLEON_WORDS_Q0[intra_order] = (
            nucleon_word_letters(['u', 'u', 'd'], intra_order=intra_order),
            nucleon_word_letters(['u', 'd', 'd'], intra_order=intra_order),
        )
    return _NUCLEON_WORDS_Q0[intra_order]


# Markov parameter z for the Ocneanu trace: z such that tr_M(sigma_i) = z,
# tr_M(1) = 1.  This is q^3/(q^2+1) — CONVENTION D, canonical per the owner
# ruling of 2026-08-15.
#
# The comment here previously read "Matches mass_endomorphism.z_mark =
# 1/(q^1/2 + q^-1/2)", which is convention C and is NOT what the line below
# computes (0.4993 vs 0.6127 at the live q0, a 23% gap).  Same declared-vs-actual
# mismatch as `computations/ocneanu_weights.py` (bean qou-pc7l); the code is
# right and the prose was stale.  Corrected 2026-08-23.
Z_MARKOV = Q0_PROTON**3 / (Q0_PROTON**2 + 1)


# ── Jones–Wenzl Ocneanu weights ω_λ(q, z) ───────────────────
#
# For H_n(q) with Markov parameter z, the Jones–Wenzl formula
# (Jones 1985 Thm 5.1; Wenzl 1988) gives the Markov-trace weights
#     ω_λ(q, z) = z^(n−1) · Π_{x ∈ λ} (1 − z·q^{2·c(x)}) / (1 − q^{2·h(x)})
# where c(x) = j − i is the cell content and h(x) is its hook length.
# These satisfy Σ_λ d_λ ω_λ = 1 and Σ_λ ω_λ · χ_λ(σ_i) = z.
#
# Falls back to Plancherel w_λ = d_q²/[n]_q! for comparison audits.

def jones_wenzl_weight(shape: tuple[int, ...],
                        q=None, z=None):
    """Ocneanu/Markov weight w_lam(q, z) for the H_n(q) Markov trace.

        w_lam = prod_{(i,j) in lam} [ q^{2i}(q^2 - 1 - q z) + q^{2j+1} z ]
                / prod_{(i,j) in lam} [ q^{2 h(i,j)} - 1 ]

    Normalisation is  **sum_lam d_lam w_lam = 1**  (the identity's character in
    block lam is d_lam), NOT sum_lam w_lam = 1.

    CORRECTED 2026-08-23 (bean qou-bsec).  The previous body was

        z^{n-1} * prod (1 - z q^{2c}) / (1 - q^{2h})

    with a docstring claiming `sum_lam w_lam = 1`.  Both were wrong.  Measured in
    exact rational arithmetic at the live q0 and convention-D z, the old formula
    gave sum_lam d_lam w_lam = -1.205 (n=3), 0.377 (n=6), -0.0549 (n=9) — not 1,
    and NEGATIVE at two of the three, so the functional it defined was not even a
    positive trace.  It also failed to reproduce the Lean-proved n=3 weights
    `QOU.SchurWeyl.HeckeMarkov3.markovWeight0/1/2` under any of 160 convention
    combinations (`computations/schurweyl/ocneanu_weight_validation.py`).

    The formula above was derived from the Markov defining conditions in exact
    Q(q,z) (`computations/schurweyl/ocneanu_weight_general_n.py`) and is
    Lean-proved against those n=3 weights, plus the n=3 and n=4 normalisations,
    in `QOU/SchurWeyl/OcneanuWeightMarkov3.lean`.

    Carried in `mpmath.mpf` end to end per AGENTS.md NO-FLOAT64; returns `mpf`.

    Superseding note (merge with main, 2026-08-23).  main landed a docstring-only
    correction on this same function, recording that the OLD body was a failed
    guess — measured over all lam |- 3A via `ocneanu_weights_3A`, its total came
    to -0.8230 / +0.0547 / -0.0009 at A = 1, 2, 3 against Plancherel's 1.0000 —
    and noting that `ocneanu_weights.py::omega_lambda_formula_guess` carries the
    same wrong hook-content shape under its own FAILED GUESS docstring.  That
    diagnosis is right and those measurements stand.  Its prescription — use the
    p(n) x p(n) linear inversion `omega_lambda_via_inversion` instead, because
    the closed form has to be guessed — is what this change supersedes: the
    formula above was DERIVED from the Markov defining conditions, not guessed,
    and agrees with the inversion route to the limit of that path's float64
    arithmetic (1.5e-16).  The inversion remains the general fallback and keeps
    its own feasibility ceiling.
    """
    n = sum(shape)
    if n == 0:
        return mpf(1)
    # Default to the mpf proton pin, and derive z in mpf from that same q.
    # The defaults used to be the float64 `Q0_PROTON` / `Z_MARKOV`, so the
    # returned mpf carried only a double's worth of q, and the normalisation
    # sum_lam d_lam w_lam = 1 held only to ~1e-16 (bean qou-bsec).
    if q is None:
        from qou_substrate.constants import Q_MP as _q_mp
        qm = _q_mp
    else:
        qm = q if isinstance(q, mpf) else mpf(q)
    if z is None:
        zm = qm ** 3 / (qm ** 2 + 1)
    else:
        zm = z if isinstance(z, mpf) else mpf(z)
    cells: list[tuple[int, int]] = []
    for i, r in enumerate(shape):
        for j in range(r):
            cells.append((i, j))
    rows = list(shape)
    max_col = rows[0] if rows else 0
    cols = [sum(1 for r in rows if r > j) for j in range(max_col)]
    hooks = [
        (rows[i] - j - 1) + (cols[j] - i - 1) + 1
        for (i, j) in cells
    ]
    numer = mpf(1)
    denom = mpf(1)
    for idx, (i, j) in enumerate(cells):
        numer *= qm ** (2 * i) * (qm ** 2 - 1 - qm * zm) + qm ** (2 * j + 1) * zm
        denom *= qm ** (2 * hooks[idx]) - 1
    if denom == 0:
        return mpf(0)
    return numer / denom


def ocneanu_weights_3A(A: int, *, q=None, z=None):
    """Return list of (λ, ω_λ) for all λ ⊢ 3A; Jones–Wenzl normalized."""
    return [(shape, jones_wenzl_weight(shape, q=q, z=z))
             for shape in partitions_of(3 * A)]


def normalized_plancherel_weights_3A(A: int, q=None):
    """ω_λ = w_λ^Planch / Σ w_μ^Planch — forces Σ ω_λ = 1.

    For q > 1, the naive Plancherel weights w_λ = d_q(λ)²/[n]_q!
    do NOT sum to 1 and produce per-generator V̂_i > q₀ (Φ_q pole).
    Rescaling to Σ = 1 pins the Markov-trace identity tr_M(𝟏) = 1
    even if it doesn't match the canonical Jones parameter z for
    tr_M(σ_i).  Empirically this keeps V̂_i in the physical range
    [−1, 1] at our q₀, which is what the Φ_q tower needs.
    """
    n = 3 * A
    nfac = qfac(n, q)
    entries = []
    total = 0.0
    for shape in partitions_of(n):
        dq = dim_q(shape, q)
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


#: Build the seminormal matrices at full mpf precision instead of float64.
#:
#: `BlockCache(float(Q0), float(HA_VAL))` is named verbatim in
#: `f64_into_mpmath_audit`'s own prose as the shape that "seeds a cache with
#: doubles". Every seminormal entry therefore descends from a binary64 q, and
#: the whole H_{3A} character sum is capped at 53 bits — while the braid word
#: it multiplies against has been mpf since `efcaf79ed`, so the products leave
#: BLAS for dtype=object anyway. Measured: 642x slower at dim=162, carrying
#: float64 information. Worst of both (bean qou-d8gq).
#:
#: OFF BY DEFAULT, and deliberately so. Turning it on changes every value this
#: module produces beyond digit ~16 and costs the full 642x, so it is not a
#: change to make silently on behalf of ~20 consumers. It exists so the
#: correct-and-slow path can be MEASURED — which is what the A-dependence
#: question needs (bean qou-2tuv) — and so the choice between it and a declared
#: float64 tier is made on numbers rather than on principle alone.
_H3A_MPF = os.environ.get("QOU_H3A_MPF", "0") in ("1", "true", "yes")


def _q_pair():
    """(q, h) at the precision this run is configured for.

    `set_compute_dps()` FIRST, and it is not optional. Without it mpmath sits
    at its default `mp.dps = 15` / `mp.prec = 53`, so every mpf built here —
    and every product of them — carries exactly 53 bits. The first version of
    this flag did that: it built `dtype=object` arrays of mpf, paid the full
    642x object-matmul cost, and returned values with a 52-bit mantissa that
    compared EQUAL to their own float64 round-trip. mpf-typed, float64-valued.

    That is the laundering pattern `pyhecke.atom.reject_float64_q` is written to
    catch ("an mpf whose VALUE is a float64's decimal expansion"), and shipping
    it under a flag named QOU_H3A_MPF would have been worse than not having the
    flag: it would have let a caller believe the precision question was
    answered. Caught by an adversarial review of this diff, not by a gate.
    """
    if _H3A_MPF:
        from _precision import set_compute_dps
        set_compute_dps()
        from q_parameter import Q_MP as _q_mp, HA_MP as _h_mp
        return _q_mp, _h_mp
    return float(Q0_PROTON), float(HA_PROTON)


def _ensure_block_cache() -> BlockCache:
    global _BLOCK_CACHE
    if _BLOCK_CACHE is None:
        _BLOCK_CACHE = BlockCache(*_q_pair())
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


def _cached_seminormal(shape: tuple[int, ...], q):
    """Seminormal (Young orthogonal) matrices for `shape`, built AT `q`.

    `q` is REQUIRED (bean `qou-wee5`, 2026-08-24). It used to default to the
    module-level `Q0` — the shim's `Q`, which the shim rebinds to muon when the
    entry-point stem is manifest-listed. A defaulted `q` therefore silently
    picked an anchor from whoever happened to be `__main__`, three modules up.
    Callers that want the experimental pin pass `Q0_PROTON`, which is not
    rebound. Pass:

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
    # Two independent fixes to this stem, both kept.
    #
    # main: the q here was always the module `Q0`; it is now the q this build is
    # actually AT. Same format, so every existing archive still resolves — the
    # field simply becomes meaningful instead of constant.
    #
    # this branch: `_mpf` in the stem, because the cache is keyed on q to 10 dp,
    # which CANNOT distinguish an f64 build from an mpf one (they agree to far
    # more than 10 dp). Without the suffix, flipping QOU_H3A_MPF would silently
    # load the truncated float64 .npz and report it as full precision — the exact
    # class of error that flag exists to remove. The two are orthogonal: one names
    # WHICH q, the other names AT WHAT PRECISION.
    _prec_tag = "_mpf" if _H3A_MPF else ""
    stem_name = f"n{n}_q{float(q):.10f}{_prec_tag}_shape{'-'.join(map(str, shape))}"
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
    if _q_cache_key(q) == _q_cache_key(Q0_PROTON):
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
                         intra_order: str = "borromean",
                         ordering: list | None = None,
                         q=None, allow_float64: bool = False):
    """Full 3A-strand word as a list of (c, d, gen_idx) triples.

    ⚠ INTRA ORDERING CHANGED 2026-09-05 (bean `qou-hu1f`; owner ruling). Each
    nucleon's **confinement core** — the six letters `nucleon_gen_chains`
    comments as `(σ₀·σ₁⁻¹)³` — used to be laid down grouped, three `σ₀` and then,
    seven letters later, three `σ₁⁻¹`. `σ₀` and `σ₁` are adjacent and do not
    commute, so that is a different element of `H₃(q)` from the alternating word
    the comment names, and only the alternating one is `β_Bor` (matched to
    `5e-60` against the Lean closed form `(4 + h² − 3h⁴ − h⁶)/(h² + 4)`). The
    core is now alternating.

    **This does NOT make the returned block `β_Bor`, or a braid.** The block is
    eleven letters per nucleon, two of them averaged (`σ − (h/2)·1`), which is
    outside the image of `ρ : B_n → H_n(q)` — see the MISNOMER note below, which
    is unchanged and still governs. Its `|tr_M|` is `1.145759692457300870`
    grouped and `0.629328402202921918` alternating, against `0.998562163836787266`
    for the bare six-letter `β_Bor`; none of the three coincide and none was
    expected to. Only the ordering of six letters inside the block changed.

    **What moved and what could not.** Log-ratio quantities could not move:
    `tr_M(W_atom)/tr_M(W_free)` is identical under both orderings to `~1e-60`
    at `A = 2, 3, 4` and equals `∏ᵢ(z + dᵢ)` under both, because connected-sum
    multiplicativity is blind to letter order inside a summand — so `L` and the
    three bond constants are untouched. **Absolute** traces moved, by `3.785×`
    (`2H`), `7.868×` (`3H`), `6.891×` (`3He`), `14.325×` (`4He`), and
    `binding_canonical`'s difference route moved with them by the same factor.
    Pass `intra_order="grouped"` to reproduce the absolute numbers as they
    stood IMMEDIATELY BEFORE 2026-09-05. Probe:
    `the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe.py`.

    🛑 **NOT "any pre-2026-09-05 absolute number" — that is what this line said
    until 2026-09-13, and it is measurably too strong** (bean `qou-5c64`).
    Grouped reproduces the state just before the ruling; it does NOT reproduce
    arbitrary earlier states, because at least one further change sits further
    back. Measured on the deuteron at a fixed q, against
    `binding-canonical.witness.json` as committed on **2026-06-15** (recovered
    at full 50 dps from its own `commitSha 0fa83306db2a`):

        intra-ordering, grouped/borromean   free 3.784816689   atom 3.784816689
        residual,       grouped/2026-06-15  free 1.15067303    atom 1.481039152

    The ordering factor reproduces the `3.785 (2H)` recorded three lines up to
    ten digits, which is what makes the residual trustworthy rather than a
    measurement artefact.

    **The residual decomposes exactly, and the pieces are worth having here.**
    Over D / T / ³He / ⁴He, the free residual factorises per nucleon and the
    bond residual per bond type — both to well below the data's own floor
    (1e-50 and 5.6e-12 respectively, the latter being June's ordering-invariance
    floor, not a model failure):

        per nucleon   proton 1.075521518      neutron 1.069874485
        per bond      p-p 1.227044031   p-n 1.287106862   n-n 1.390572916

    **The p-p bond IS the Markov parameter `z`.** Isolated as
    `r(³He)/r(D)` with `r = tr_M(W_atom)/tr_M(W_free)`, it is
    `0.61268805054558909984` today — `z_D = q³/(q²+1)` to **3.2e-51** — and
    `0.49932034618370936279` in June — `z_C = 1/(√q + 1/√q)` to 2.4e-8, the
    residue being the q₀ anchor. So its residual is `z_D/z_C`, i.e. the
    **convention C→D excision, carried by `z` itself.**

    🛑 **Do not read "the C→D `y_lambda_at` swap is a no-op" as "C→D does not
    affect this."** Both are true and they are different statements: the two
    `y_lambda_at` implementations do agree at `n = 6`, and the convention still
    arrives through `z`, which never goes through that function. An earlier
    version of this note listed C→D among the causes *ruled out* on the strength
    of the `y_lambda_at` test alone; that was an absence-of-evidence error and
    is retracted (bean `qou-5c64`).

    **And the OTHER TWO bonds' `d` are unchanged too, so the whole bond side is
    pure C→D.** Backing `d = bond - z` out against each side's OWN `z`:

        p-p   d_now  0                      d_June  1.2e-8      (i.e. 0)
        p-n   d_now -0.10445825933572413    d_June -0.10445817736543710
        n-n   d_now -0.20906032198987946    d_June -0.20906030963839083   (= -h)

    all three agree to the ~1e-7 anchor floor, and `(z_D + d)/(z_C + d)` with `d`
    held fixed predicts every measured bond residual to 2e-7. The p-n `d` is
    `-h(1/2 - δ/4)` with `δ = flavor_split_leading(q) = 0.0013757112` today and
    `0.0013772796` implied by the June witness — a 0.11 % gap, which is the
    anchor, not a change.

    🛑 **So the δ de-wire of 2026-06-29 (`9928f3f4a79`) does NOT move this
    witness**, and an earlier version of this note claimed it did, with
    "δ = -2.16772 as of 2026-06-15". That number came from subtracting `z_D`
    from June's bond when June was on `z_C`; it is an artefact of mixing the two
    conventions and is retracted (bean `qou-5c64`). The `2.9e-16` confirmation
    quoted alongside it was real but was of the *today* side only — a check on
    one side of a comparison, reported as confirming the comparison.

    Genuinely ruled out, each by direct substitution at fixed q: the q₀ anchor
    (3.9e-8), the `pn_convention` *flag* (a no-op on the free trace by
    construction, 2e-4 on the atom trace), the `m_pp/m_pn/m_nn` multiplicities
    (unchanged), and the δ de-wire (above). **Still open: only the two
    per-nucleon free factors**, proton `1.075521518` and neutron `1.069874485`.

    ⚠ NAME IS A MISNOMER — this does NOT return a braid word (2026-08-25, PR #5765).
    A rename was considered and rejected: 685 call sites across 382 files. So the
    name stays and this docstring carries the correction.

    Each triple `(c, d, g)` denotes the HECKE ELEMENT `c*sigma_g + d*1`, not a braid
    generator. The letters OUTSIDE the image of rho are exactly the AVERAGED ones,
    `d in {-h/2, -h(1/2 - delta/4)}` -- NOT merely the `d != 0` ones. Under this
    module's convention `sigma^-1 = sigma - h`, a `d == -h` letter IS a braid
    generator (it is sigma^-1), as the next sentence's identity itself says. Measured
    on 2H: of 23 letters, 11 are `d = 0` (sigma) and 7 are `d = -h` (sigma^-1), so 18
    are braid generators and 5 are not -- and 5 = 2A + 1, the count this docstring
    gives below. Getting this wrong invalidates the wrong objects: under a `d == 0`
    rule the figure-eight `(s1 s2^-1)^2` -- the muon carrier, a genuine hyperbolic
    LINK the mass law reads Vol from -- would read as "not a braid word".
    The averaged interfaces are EXACTLY weight-1 averages over crossing sign:

        sigma - (h/2)*1          == (sigma + sigma^-1)/2
        sigma - h*(1/2 - d/4)*1  == (1/2 + d/4)*sigma + (1/2 - d/4)*sigma^-1

    There are `2A + 1` such non-braid letters (two per nucleon, from its two `ud`
    pairs, plus one per interface). So the returned object lies in `H_n(q)` and is
    NOT in the image of `rho : B_n -> H_n(q)`.

    WHAT FOLLOWS, and why it matters:

      * `tr_M` of this object IS well defined -- the Markov trace is a linear
        functional on all of `H_n(q)` and needs no closure. Every binding number
        computed from it stands.
      * But there is NO SINGLE LINK behind it. By linearity `tr_M` here is a
        weighted sum of `2^(2A+1)` link invariants (32 for 2H), not the invariant
        of one link.
      * So NO TOPOLOGICAL quantity may be read off it -- not a volume, not a
        crossing number, not a genus. Those are not linear and linearity is the
        only thing transporting the sum.

    Measured: all 32 branch closures for 2H are non-hyperbolic (each branch braid
    is monotone, so its closure is a connected sum of (2,k) torus links; verified
    32/32 against SnapPy deconnect_sum). Vol = 0 for every one.
    See docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md and
    content/.../braids-and-knots/markov-disambiguation.md.

    ⚠ THE PARAGRAPH ABOVE DESCRIBES THE GROUPED WORD AND IS STALE FOR THE LIVE
    ONE (measured 2026-09-07, bean `qou-m6gp`). The 2026-09-05 alternating core
    `(σ₀σ₁⁻¹)³` is NOT monotone, so the monotone ⇒ #T(2,k) ⇒ Vol = 0 argument no
    longer applies. Re-measured with SnapPy 3.3.2 on the live word: every
    per-nucleon 3-strand branch closure is a HYPERBOLIC 2-component link —
    proton branches L9n10 (9.9665), L11a252 (16.1911), L7a6 (4.7495), L9a21
    (11.9429); neutron branches L11a252, L9a21 ×2, L11n202 (8.1957); all
    geometric solutions, census-identified. What survives unchanged is the
    connected-sum structure: each interface is a single letter, so every atom
    branch closure is the connected sum of its A nucleon pieces (800/800
    branches over ²H/³H/³He/⁴He decompose into exactly A summands), hence
    Vol(atom) − Vol(free) ≡ 0 by additivity of simplicial volume while the
    absolute branch volumes are 12.9–64.8 rather than 0. The "no single link
    behind the object" conclusion above is untouched. Producer:
    computations/probes/binding_volume_difference_probe.py.

    Matches the chain-walk convention of
    hecke_core.atom_per_generator_volumes (lines 3029–3079):
    for each nucleon k, apply intra g₀, intra g₁, then (if

    The p-n interface is color-weighted by default (owner directive
    2026-06-01: bring_color_weighted is canonical across the compute):
    its averaged crossing is `σ − h·(1/2 − δ/4)·1`, δ =
    flavor_split_leading(q₀), vs the color-blind `σ − h/2·1` (`pn_convention=
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

    **D1 — what this models, and what it is refuted by** (owner ruling on
    `docs/coordination/2026-09-05-owner-gated-bean-triage.md`, 2026-09-13).

    This is the **NUCLEUS**: a linear chain, `A-1` interfaces, `12A-1` letters,
    no electrons. Its sibling `pyhecke.gram.build_atom_nf` is the **ATOM**: all
    pairs, `11A + C(A,2) + Z` letters, including `Z` electron crossings.
    **They model different objects and disagree silently.** Neither is selected
    as correct, because both topologies are refuted:

    * the chain here is excluded by
      `QOU.MassTheory.ChainBondOrderDependence.orderIndependent_iff` -- the chain
      bond sum is arrangement-invariant only when `L_pp = L_pn = L_nn`, and a
      nucleus has no arrangement;
    * the all-pairs complete graph is excluded structurally by
      `QOU.Mass.CoordinationSaturation` -- `B/A = eps*(A-1)/2` is unbounded, so
      it has no plateau, while saturation is observed.

    Bean `t7qv` RESULT 4 measures all-pairs as roughly halving the A-scaling
    error (2H/3He +40.0% against this chain's +73.5%) -- but **RESULT 5 refutes a
    one-parameter falloff outright** (`f = +2.030` from A-scaling against
    `f = -0.697` from the mirror; one of them is negative). So all-pairs is the
    better of two refuted topologies, and quoting RESULT 4 without RESULT 5
    sells a preference between refuted options as a result.

    **Consumers.** This chain feeds `binding_canonical` (imported at
    `binding_canonical.py:91`, called at `:174` and `:579`). The all-pairs
    sibling is the one that reaches the paper, via
    `all_nuclides_sdp_admissibility.py` -> `nuclear-interactions/demand-stability`.

    The topology question stays open under bean `qou-brng`.
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
    # The intra word is built AS A WORD (`nucleon_word_letters`), not as two
    # per-generator chains concatenated. Writing all of `g0` then all of `g1`
    # emits `σ₀³σ₁⁻³`, and σ₀/σ₁ are adjacent, so that is a DIFFERENT element
    # of H₃ from the `(σ₀σ₁⁻¹)³` its source comment names — 82 % away at q₀,
    # and only the interleaved one is β_Bor (Lean closed form, 5e-60).
    # `intra_order="grouped"` reproduces the pre-2026-09-05 word.
    from pyhecke.atom import nucleon_word_letters
    if q is None:
        # Same role the `_PROTON_G0`/`_NEUTRON_G0` constants played: keep the
        # canonical-q₀ path off the 60-dps rebuild on every call.
        p_w, n_w = _nucleon_words_q0(intra_order)
    else:
        p_w = nucleon_word_letters(['u', 'u', 'd'], q=q, intra_order=intra_order,
                                   allow_float64=allow_float64)
        n_w = nucleon_word_letters(['u', 'd', 'd'], q=q, intra_order=intra_order,
                                   allow_float64=allow_float64)
    word: list = []
    # `ordering` is the INTER-nucleon sequence. Default `None` reproduces the
    # sorted `p…p n…n` this function has always built, so every existing caller
    # is unaffected — asserted, not assumed, by
    # `computations/probes/atom_word_explicit_ordering_probe.py`.
    #
    # Why it is a parameter at all: the corpus records that the character ratio
    # is blind to INTRA-nucleon letter order (this function's own docstring, and
    # `the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe`). That
    # says nothing about the inter-nucleon sequence, and until now no unsorted
    # sequence could be built at all, so the bond model's per-interface product
    # had never been tested on one. Hand-building such a word is exactly what
    # this arc's history warns against; parameterising the canonical builder is
    # the alternative.
    if ordering is None:
        ordering = ['p'] * Z + ['n'] * N
    else:
        ordering = list(ordering)
        if sorted(ordering) != sorted(['p'] * Z + ['n'] * N):
            raise ValueError(
                f"ordering {ordering!r} does not have the content (Z={Z}, N={N}); "
                "it must be a permutation of ['p']*Z + ['n']*N")
    for k, nuc in enumerate(ordering):
        base_g0 = 3 * k
        for c, d, off in (p_w if nuc == 'p' else n_w):
            word.append((c, d, base_g0 + off))
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

    **This is a float64 kernel, and the return annotation is the contract.**
    ``build_seminormal_matrices`` fills a numpy array or a scipy sparse
    matrix, and both branches below end in ``float(...)``, so no caller has
    ever received more than 53 bits from here. The word coefficients are
    therefore coerced to ``float`` on the way in, which loses nothing the
    return type was not already discarding — and without it an ``mpf``
    coefficient CRASHES the sparse branch outright:

        c * <csr_matrix>  ->  _mul_scalar  ->  dtype object
        ValueError: scipy.sparse does not support dtype object

    The dense branch did not crash; it silently built an object-dtype array
    and ran the whole product in Python-level mpf arithmetic, at 53-bit
    inputs, for no gain.  So the two branches disagreed on the same input,
    one loudly and one expensively.

    If you need χ_λ at true precision, this is not the function — see
    ``hecke_characters.chi_lambda_braid_mpf``.  Note that at A = 4 the
    largest irrep is f^λ = 4158, i.e. ~7.2e10 mpf operations per matrix
    multiply, so that route is not a drop-in for the A ≥ 4 producers.
    """
    if dim == 0:
        return 0.0
    word = [(float(c), float(d), g) for (c, d, g) in word]
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

    # Both storage formats go through the structured path; it reads the
    # generators' nonzeros, not their container.
    #
    # The sparse branch was additionally BROKEN, not merely slow: for large n
    # `build_seminormal_matrices` returns scipy sparse matrices, and 11 of the
    # 23 letters in the A=2 word carry an `mpmath.mpf` coefficient, so
    # `d * I` raised "scipy.sparse does not support dtype object". That is why
    # ⁴He (n = 12) produced nothing from `alpha_5_lp_dual_crystal.py` — the
    # caller wraps `per_atom_lp` in `except Exception: continue`, so the
    # heaviest atom was dropped in silence rather than reported. Bean
    # `qou/ftuv`.
    return _chi_of_word_structured(sigmas, dim, word)


def _chi_of_word_structured(sigmas, dim, word) -> float:
    """`tr(Π_k (c_k·σ_{g_k} + d_k·I))` in O(|word|·dim²) instead of O(|word|·dim³).

    The generic form multiplied a dense `dim × dim` product by a dense
    `dim × dim` matrix for every letter — `dim³` per letter. A Hoefsmit
    seminormal generator is nowhere near a general matrix: it is diagonal plus
    off-diagonal entries with **at most two nonzeros per column**, one of which
    is the diagonal. So each column of the product takes its own scaling plus a
    contribution from exactly ONE other column, which is a `dim²` update.

    Verified across 48 generators spanning six partitions before relying on it,
    and re-checked per generator below rather than assumed — a wrong structural
    assumption here would silently drop a term.

    That is an asymptotic change, not a constant: at `dim = 7700` (λ ⊢ 12, the
    ⁴He stratum) the old form needed ~4.6e11 flops per letter where this needs
    ~5.9e7. `alpha_5_lp_dual_crystal.py` was not hanging — it was doing dim³
    work per letter, three q-values deep. Bean `qou/ftuv`.

    Falls back to the dense product for any generator that violates the
    structure, so correctness never depends on the assumption holding.
    """
    try:
        from scipy import sparse as _sp
    except ImportError:
        _sp = None

    split = []
    for S in sigmas:
        if _sp is not None and _sp.issparse(S):
            coo = S.tocoo()
            ii = coo.row.astype(np.int64)
            jj = coo.col.astype(np.int64)
            vals = np.asarray(coo.data, dtype=np.float64)
        else:
            A = np.asarray(S, dtype=np.float64)
            ii, jj = np.nonzero(A)
            vals = A[ii, jj]
        on_diag = ii == jj
        diag = np.zeros(dim, dtype=np.float64)
        diag[jj[on_diag]] = vals[on_diag]
        io, jo = ii[~on_diag], jj[~on_diag]
        if len(np.unique(jo)) != len(jo):
            return _chi_of_word_dense(sigmas, dim, word)
        split.append((diag, io, jo, vals[~on_diag]))

    # Work on the transpose: row j of PT is column j of the product, so every
    # update is contiguous.
    PT = np.ascontiguousarray(np.eye(dim))
    for (c, d, g) in word:
        # `c` and `d` arrive as a mix of int and mpmath.mpf — 11 of the 23
        # letters in the A=2 word carry an mpf `d`. Multiplying a float64
        # seminormal matrix by an mpf promoted the whole product to
        # **object dtype**, so every `product @ M` ran as a Python-level
        # object matmul. That, not dim³ float work, is what made this slow:
        # 0.025 s per letter on a 27×27 matrix.
        #
        # Coercing to float64 is consistent with what this path already
        # claims to be — the docstring of
        # `global_wedderburn_sum_q_hecke_seminormal` calls it "χ^λ_q via
        # Hoefsmit seminormal matrices at q_val (numerical, float64)", and
        # `build_seminormal_matrices` returns float64. The mpf coefficients
        # were carrying extra digits on top of f64 inputs, which is precision
        # in the accumulator only.
        cf = float(c)
        df = float(d)
        diag, io, jo, vo = split[g]
        tmp = PT[io] * (cf * vo)[:, None] if len(io) else None
        PT *= (df + cf * diag)[:, None]
        if tmp is not None:
            PT[jo] += tmp
    return float(np.trace(PT))


def _chi_of_word_dense(sigmas, dim, word) -> float:
    """Generic dense fallback — `dim³` per letter, used only when a generator
    does not have the one-off-diagonal-per-column structure."""
    product = np.eye(dim)
    I = np.eye(dim)
    for (c, d, g) in word:
        S = sigmas[g]
        A = S.toarray() if hasattr(S, "toarray") else np.asarray(S)
        product = product @ (float(c) * np.asarray(A, dtype=np.float64)
                             + float(d) * I)
    return float(np.trace(product))


def markov_trace_3A(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1, q=None,
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

    nfac = qfac(n_strands, q)
    total = 0.0
    per_partition = []
    for shape in partitions_of(n_strands):
        sigmas, dim, _syts = _cached_seminormal(shape, Q0_PROTON)
        if dim == 0:
            continue
        dq = dim_q(shape, q)
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


def per_generator_V_hat_3A(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1, q=None,
                             include_inter: bool = True,
                             weight_scheme: str = "jones_wenzl",  # convention D, owner 2026-11-18
                             # Switched to "jones_wenzl" (convention D) on owner
                             # instruction 2026-11-18. The earlier finding that this
                             # scheme's weights "do not sum to 1" was right for the old
                             # weight formula (replaced 2026-08-23, qou-bsec) and for
                             # the w*chi/d collapse below, which this change also fixes.
                             # With both fixed, V_hat_i = z*a_i + b_i, the Markov trace
                             # of the generator's word, which can exceed the Phi_q pole
                             # cap (1.087779). That is the qou-2tuv pole problem and it
                             # is still open.
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

    nfac = qfac(n_strands, q)
    # Under QOU_H3A_MPF the accumulator must NOT start as a float: `0.0 + mpf`
    # is fine, but `float(np.trace(M))` two lines down would still truncate the
    # mpf trace, so building the matrices at mpf would buy nothing. Both are
    # conditioned on the flag; the f64 path is byte-identical to before.
    V_hat = [(mpf(0) if _H3A_MPF else 0.0)] * n_gens

    # Weight table — normalized to Σ = 1 for the Markov identity
    # tr_M(𝟏) = 1; alternate schemes available for audit.
    weight_table: list[tuple[tuple[int, ...], float]] = []
    if weight_scheme == "normalized_plancherel":
        weight_table = normalized_plancherel_weights_3A((Z + N))
    elif weight_scheme == "plancherel":
        for shape in partitions_of(n_strands):
            dq = dim_q(shape, q)
            weight_table.append((shape, (dq * dq) / nfac))
    elif weight_scheme == "jones_wenzl":
        weight_table = ocneanu_weights_3A((Z + N))
    else:
        raise ValueError(f"unknown weight_scheme: {weight_scheme}")

    # Per-generator SCALAR collapse, replacing a per-λ matrix product.
    #
    # Every factor accumulated at generator i is a polynomial in the SAME
    # σ_i, so the factors commute, and σ_i obeys the Hecke quadratic relation
    # σ² = (q − q⁻¹)σ + 1. Measured against the built matrices rather than
    # assumed: max|σ² − ((q−q⁻¹)σ + 1)| = 6.661e-16 for (3,2,1) and
    # (4,3,1,1), while the (q−1)σ + q alternative misses by 1.992e-01;
    # eigenvalues are [−q⁻¹, q] = [−0.90091828, 1.10997858].
    #
    # So Π_k (c_k σ_i + d_k · 1) = α_i σ_i + β_i · 1 with (α, β) built by a
    # scalar recursion, and χ_λ of it is α · tr σ_i^λ + β · dim λ — a diagonal
    # sum, O(dim), no matmul at any point.
    #
    # This is what makes A ≥ 3 tractable, and the reason is dtype, not dim³:
    # the word's coefficients are a MIX of int and mpf (19 of the 35 steps at
    # A=3 carry one, and every generator hits one by step 0-4), so
    # `c * sigmas[i] + d * I_lam` promoted the float64 seminormal matrix to
    # dtype=object and each `M @ ...` ran as a Python-level loop — ~6e7 mpf
    # mul+add per word-step sweep over λ ⊢ 9. Same defect ca8a629034 fixed in
    # chi_lambda_of_word; that fix did not reach THIS function. Measured here:
    # A=2 0.577s → 0.0009s, A=3 >20 min → 0.1 s, values unchanged to 9.107e-16.
    #
    # δ is taken at Q0_PROTON, NOT at the `q` parameter, because the matrices
    # below are built at Q0_PROTON — the relation has to hold for the matrices
    # actually in hand or the collapse is inconsistent with them. That the
    # weight table above already honours `q` while `_cached_seminormal` does
    # not is pre-existing and is left alone here.
    _delta = Q0_PROTON - 1.0 / Q0_PROTON
    _alpha_beta = []
    for i in range(n_gens):
        _a, _b = 0, 1                      # identity: 0·σ + 1·1
        for (c, d) in word_by_gen[i]:
            _a, _b = _a * c * _delta + _a * d + _b * c, _a * c + _b * d
        _alpha_beta.append((_a, _b))

    for (shape, w_lam) in weight_table:
        sigmas, dim, _syts = _cached_seminormal(shape, Q0_PROTON)
        if dim == 0:
            continue
        try:
            from scipy import sparse as sp_sparse
            is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
        except ImportError:
            is_sparse = False
        for i in range(n_gens):
            w_i_steps = word_by_gen[i]
            if not w_i_steps:
                # Empty word at gen i → trace = dim → contrib = w_lam (or
                # d_lam * w_lam under jones_wenzl, see the collapse below)
                V_hat[i] += w_lam * dim if weight_scheme == "jones_wenzl" else w_lam
                continue
            if i >= len(sigmas):
                # Shouldn't happen (len(sigmas) = n_strands - 1)
                continue
            _a, _b = _alpha_beta[i]
            if is_sparse:
                _s = sigmas[i].diagonal().sum()
            else:
                _s = np.trace(sigmas[i])
            _t = _a * _s + _b * dim
            tr = _t if _H3A_MPF else float(_t)
            # jones_wenzl weights are normalised by sum_lam d_lam w_lam = 1, so
            # the Markov trace is sum_lam w_lam * chi_lam, NOT w_lam * chi_lam / d_lam.
            # The old /dim here is what made that scheme "not sum to 1".
            if weight_scheme == "jones_wenzl":
                V_hat[i] += w_lam * tr
            else:
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


def phi_q_safe(z_val: float, *, q: float = Q0_PROTON, cap_frac: float = 0.98,
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


def log_phi_q(z_val: float, *, q: float = Q0_PROTON,
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


#: Cached (q, q^-1) for the Li_2^q tower term, loaded once from the canonical
#: pinning witness.
_LI2Q_Q_CACHE: tuple | None = None   # (dps, q, q_inv)


def tower_term_li2q(v_abs: float) -> "mpmath.mpf":
    """Lean-mandated per-generator tower term: ``towerTerm q V = -Li_2^q(-|V|)``.

    This is `QOU.BraidKnot.QuantumDilogarithm.towerTerm`, the form the Lean
    class `HasCorrectedMassEndomorphismTower` requires of any consumer of the
    mass-endomorphism tower ("should assert `f = towerTerm`, not `f = phi_q`.
    The latter is the historical pathological form preserved only as a
    diagnostic").

    Lean proves these are genuinely different functions, not two spellings of
    one: `phi_q_ne_li2_q` refutes the historical identity claim
    `Phi_q(z) = -Li_2^q(-z)` by counter-example at z = 0, where Phi_q is the
    empty PRODUCT (1) and -Li_2^q(-0) is the empty SUM (0). No `sorry`.

    Note the minus signs: outside AND on the argument. The negative argument is
    what makes the series alternate and converge; the positive-argument form
    diverges here because |V_hat| can exceed 1.
    """
    global _LI2Q_Q_CACHE
    import mpmath as _mp
    from _li_2_q_util import li_2_q, load_q_50dps
    # Built at >= COMPUTE_DPS regardless of the caller's ambient precision, for the
    # reason `_q_h_at_precision` gives above: an mpf keeps the precision it was
    # CREATED at, so loading q under the mpmath default (dps = 15) would bake in
    # a 15-digit q and silently undo everything below. It matters twice here --
    # `li_2_q` also sets its own truncation from the ambient dps
    # (`eps = 10**(5 - mp.dps)`), so at the default it would stop the series at
    # 1e-10 and hand back an mpf-typed, float64-valued answer. That is the exact
    # "precision theatre" this module already carries a warning about.
    # Callers already inside a higher workdps keep theirs.
    from _precision import COMPUTE_DPS
    with _mp.workdps(max(_mp.mp.dps, COMPUTE_DPS)):
        dps = _mp.mp.dps
        if _LI2Q_Q_CACHE is None or _LI2Q_Q_CACHE[0] != dps:
            q, q_inv, _z = load_q_50dps()
            _LI2Q_Q_CACHE = (dps, q, q_inv)
        _, q, q_inv = _LI2Q_Q_CACHE
        # Returns mpf, NOT float. `mpf(v_abs)` on a Python float is exact -- it
        # takes the binary64 value verbatim, no decimal round-trip -- so nothing
        # is lost on the way in and nothing is truncated on the way out. The sums
        # in `mass_from_tower_safe` promote to mpf on contact, which is the
        # point: a downcast here would cap the whole tower at 53 bits.
        return -li_2_q(-abs(_mp.mpf(v_abs)), q, q_inv)


def _tower_spec(term: str, cap_frac: float):
    """Resolve the archimedean specialisation function by name.

    ``"tower_term"`` -> `tower_term_li2q`  (Lean-mandated, DEFAULT)
    ``"phi_q"``      -> `phi_q_safe`       (historical; MASS context only --
                        absolute masses and ratios, per `_li_2_q_util`'s rule
                        that Li_2^q is canonical for BINDING context)
    """
    if term == "tower_term":
        return tower_term_li2q
    if term == "phi_q":
        return lambda x: phi_q_safe(x, cap_frac=cap_frac)
    raise ValueError(f"unknown term: {term!r} (want 'tower_term' or 'phi_q')")


def mass_from_tower_safe(vols, *, cap_frac: float = 0.98,
                            cross_mode: str = "adjacent",
                            term: str = "tower_term"):
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
    _spec = _tower_spec(term, cap_frac)
    n = len(vols)
    desc = 1.0
    for v in vols:
        desc *= v["full"]
    desc = abs(desc)
    single = sum(_spec(abs(v["full"])) for v in vols)
    cross = 0.0
    if cross_mode == "adjacent":
        for i in range(n - 1):
            cross += _zm * _zm * _spec(
                abs(vols[i]["full"] * vols[i + 1]["full"]))
    elif cross_mode == "full":
        for i in range(n):
            for j in range(i + 1, n):
                cross += _zm * _zm * _spec(
                    abs(vols[i]["full"] * vols[j]["full"]))
    elif cross_mode == "full_z2pow":
        for i in range(n):
            for j in range(i + 1, n):
                cross += (_zm ** (2 * (j - i))) * _spec(
                    abs(vols[i]["full"] * vols[j]["full"]))
    else:
        raise ValueError(f"unknown cross_mode: {cross_mode}")
    return desc, single, cross, desc + single + cross


def binding_3A_tower(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1, q=None,
                       E_0: float = E_0_CALIBRATION_MEV,
                       weight_scheme: str = "jones_wenzl",  # convention D, owner 2026-11-18
                       cap_frac: float = 0.98,
                       use_safe_phi_q: bool = True,
                       cross_mode: str = "full",
                       verbose: bool = False,
                       term: str = "tower_term") -> dict:
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
        Z, N, q=q, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
        include_inter=True, weight_scheme=weight_scheme, verbose=verbose)
    vols_free = per_generator_V_hat_3A(
        Z, N, q=q, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
        include_inter=False, weight_scheme=weight_scheme, verbose=verbose)
    if not vols_atom or not vols_free:
        return {"status": "trivial", "Z": Z, "N": N}
    if use_safe_phi_q:
        desc_a, sgl_a, cross_a, total_a = mass_from_tower_safe(
            vols_atom, cap_frac=cap_frac, cross_mode=cross_mode,
            term=term)
        desc_f, sgl_f, cross_f, total_f = mass_from_tower_safe(
            vols_free, cap_frac=cap_frac, cross_mode=cross_mode,
            term=term)
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


def binding_3A(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1, q=None,
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
    tr_atom = markov_trace_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn, q=q,
                                include_inter=True, verbose=verbose)
    tr_free = markov_trace_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn, q=q,
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
        ("3He",  2, 1,  AME_B_HE3_MEV_VALIDATION),
        ("4He",  2, 2, AME_B_HE4_MEV_VALIDATION),
        ("6Li",  3, 3, 32.0),
        ("7Li",  3, 4, 39.244529),
        ("9Be",  4, 5, 58.1650),
        ("10B",  5, 5, 64.750),
        ("12C",  6, 6, 92.161728),
    ]

    print("=" * 116)
    print("H_{3A} WEDDERBURN-CHARACTER BINDING — task-1 fix")
    print(f"q₀ = {Q0_PROTON}")
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
        "parameters": {"q0": Q0_PROTON, "E_0_MeV": args.E0,
                        "max_A": args.max_A},
        "markov_path": results_mk,
        "tower_path": results_tw,
    }
    out = Path(__file__).parent / "mass-at-3A-proper.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
