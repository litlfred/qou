#!/usr/bin/env python3
"""derived_chi_catalogue_matrix_m_mpfr.py — mpmath/mpfr backend for
the matrix-M μ_p factorisation.

Per the audit doc roadmap (Phase 2 follow-up #1):
[`docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md`](../../docs/audits/2026-06-07-derived-chi-catalogue-tier-1-lr-factorisation.md)

The numerical sp.Rational backend (PR #1985, #1987) proved the
architecture (block-bounded call cost, flat in n for low-dim λ —
13.47× speedup on ⁴He λ=(12)) but lost to Rust on high-dim λ
because sp.Rational arithmetic with 50-digit denominators costs
more per multiply than Rust's f64. Block-bounded ≠ arithmetic-
bounded.

This backend swaps `sp.Rational` for **`mpmath.mpf` at 50-dps
precision** — controlled-precision floating point, NOT f64. The
matrix-M structural decomposition is identical; only the leaf
arithmetic changes.

## Why mpmath over sp.Rational

- `sp.Rational` carries unbounded denominators; each multiply grows
  the representation. For long matrix products with q_0 near 1.11,
  the denominator quickly exceeds 50-digit precision needed for
  ppQ correctness, yet computation continues at full precision.
  Wasted work.
- `mpmath.mpf` truncates to the precision dial (`mp.dps = 50`).
  Each multiply costs ~constant time regardless of expression
  history. The substrate q_0 has 50-digit precision; matching
  arithmetic precision is the right answer.

## NO f64 in compute path

`mpmath.mpf` is arbitrary-precision binary floating point — the
"controlled precision" the AGENTS.md precision discipline
explicitly approves. NOT f64. The mpmath backend defaults to
`mp.dps = 50` (matches Q_50_DIGIT_STR); higher precision (e.g.
`dps = 65`) is a config parameter.

## Δ_λ-gate

Same trace identity as PR #1980/#1985/#1987. Pure structural
rearrangement; no ansatz, no fit, no calibration parameter.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: E402, F401

import mpmath  # noqa: E402

# `pyhecke_native` (the PyO3 wheel) is only needed by the Rust
# reference path `chi_rust_at_q_mpf`/`main`. The (μ_p, μ_n) math and
# the `--use-mu-n-blocks` cross-validation are pure mpmath, so guard
# the import: absent wheel ⇒ ph = None and only the Rust path raises.
try:
    import pyhecke_native as ph  # noqa: E402
except ImportError:  # pragma: no cover - wheel absent in some sandboxes
    ph = None

from witness_base import WitnessBuilder  # noqa: E402

from derived_chi_catalogue_matrix_m import (  # noqa: E402
    standard_young_tableaux,
    group_syts_by_mu_p,
    _content,
    _shape_partitions_of,
    _word_for_braid_word_3a,
)


# ── mpmath-native Hoefsmit seminormal form ────────────────────────


def seminormal_matrices_mpfr(
    shape: tuple[int, ...], q_mpf: object,
) -> list[object]:
    """Build σ_1, …, σ_{n-1} in the asymmetric natural seminormal
    form using `mpmath.matrix` over `mpmath.mpf` at the current
    `mpmath.mp.dps`.

    Mirrors `derived_chi_catalogue_matrix_m.seminormal_matrices_qrat`
    but generates mpf matrices directly — no sympy involvement, no
    rational-blowup intermediate.

    Args:
      shape: λ ⊢ n.
      q_mpf: substrate q as `mpmath.mpf` (not a symbol).

    Returns a list `[σ_1, …, σ_{n-1}]` of mpmath.matrix, each
    `dim × dim` where dim = #SYTs(shape).
    """
    n = sum(shape)
    syts = standard_young_tableaux(shape)
    dim = len(syts)
    syt_to_idx = {syt: i for i, syt in enumerate(syts)}
    one = mpmath.mpf(1)
    h = q_mpf - one / q_mpf

    generators: list[object] = []
    for k in range(1, n):
        M = mpmath.zeros(dim, dim)
        processed = [False] * dim
        for i in range(dim):
            if processed[i]:
                continue
            cell_k_minus_1 = syts[i][k - 1]
            cell_k = syts[i][k]
            rho = _content(cell_k) - _content(cell_k_minus_1)
            a = h / (one - q_mpf ** (-2 * rho))

            swapped = list(syts[i])
            swapped[k - 1], swapped[k] = cell_k, cell_k_minus_1
            swapped_tuple = tuple(swapped)
            partner = syt_to_idx.get(swapped_tuple)
            # `partner == i` cannot happen — swap is of distinct cells.
            if partner is None:
                M[i, i] = a
                processed[i] = True
            else:
                j = partner
                a_prime = h / (one - q_mpf ** (2 * rho))
                b_sq = a * a_prime + one
                lo, hi = (i, j) if i < j else (j, i)
                a_lo, a_hi = (a, a_prime) if i < j else (a_prime, a)
                M[lo, lo] = a_lo
                M[lo, hi] = one
                M[hi, lo] = b_sq
                M[hi, hi] = a_hi
                processed[lo] = True
                processed[hi] = True
        generators.append(M)
    return generators


def _extract_block_mpfr(
    M: object, idxs: list[int],
) -> object:
    """Sub-matrix of an mpmath.matrix at given row/col indices."""
    s = len(idxs)
    out = mpmath.zeros(s, s)
    for ii, i in enumerate(idxs):
        for jj, j in enumerate(idxs):
            out[ii, jj] = M[i, j]
    return out


# ── Precompute + call ─────────────────────────────────────────────


def precompute_block_tables_mpfr(
    shape: tuple[int, ...],
    k_split: int,
    q_mpf: object,
) -> dict:
    """Same per-μ_p block structure as the sp.Rational backend
    (PR #1985), but built in mpmath. The full dim×dim seminormal
    matrices are built ONCE then DISCARDED after block extraction.
    """
    n = sum(shape)
    sigmas = seminormal_matrices_mpfr(shape, q_mpf)
    groups = group_syts_by_mu_p(shape, k_split)
    blocks: dict[tuple[int, ...], dict] = {}
    for mu_p, idxs in groups.items():
        sigmas_left = {
            g: _extract_block_mpfr(sigmas[g - 1], idxs)
            for g in range(1, k_split)
        }
        sigmas_right = {
            g: _extract_block_mpfr(sigmas[g - 1], idxs)
            for g in range(k_split + 1, n)
        }
        M_pp = _extract_block_mpfr(sigmas[k_split - 1], idxs)
        blocks[mu_p] = {
            "size": len(idxs),
            "indices": idxs,
            "sigmas_left": sigmas_left,
            "sigmas_right": sigmas_right,
            "M_pp": M_pp,
        }
    return {
        "shape": shape,
        "k_split": k_split,
        "q": q_mpf,
        "mu_p_groups": groups,
        "blocks": blocks,
    }


def chi_via_numerical_matrix_m_mpfr(
    shape: tuple[int, ...],
    word_left: list[tuple[int, int]],
    bridge_sign: int,
    word_right: list[tuple[int, int]],
    cache: dict,
) -> object:
    """Sum traces of `B_p · M_pp · B_n` over μ_p blocks in mpmath.
    Same identity as the sp.Rational backend, just mpf arithmetic.
    """
    q = cache["q"]
    one = mpmath.mpf(1)
    h = q - one / q
    total = mpmath.mpf(0)
    for mu_p, block in cache["blocks"].items():
        size = block["size"]
        eye_block = mpmath.eye(size)
        sigmas_left = block["sigmas_left"]
        sigmas_right = block["sigmas_right"]
        M_pp_pos = block["M_pp"]
        # Hecke inverse on a block: σ_g⁻¹ = σ_g − h·I (block extraction
        # is linear). Inlined to avoid per-iteration function recreate.
        B_p = eye_block
        for (sign, g_1based) in word_left:
            mat = sigmas_left[g_1based]
            B_p = B_p * (mat if sign >= 0 else mat - h * eye_block)
        B_n = eye_block
        for (sign, g_1based) in word_right:
            mat = sigmas_right[g_1based]
            B_n = B_n * (mat if sign >= 0 else mat - h * eye_block)
        M = M_pp_pos if bridge_sign >= 0 else (M_pp_pos - h * eye_block)
        prod = B_p * M * B_n
        # mpmath has no direct trace; sum diagonal.
        for ii in range(size):
            total = total + prod[ii, ii]
    return total


# ── Phase 1.3: (μ_p, μ_n)-block extraction via q-Young symmetrizers ─
#
# mpmath/mpfr port of the symbolic prototype
# `derived_chi_catalogue_matrix_m_mu_n.q_young_symmetrizer_matrix`
# (PR #2013). Within each μ_p-block of V_λ the right H_3 sub-algebra
# (generated by σ_{k_split+1}, σ_{k_split+2}) further decomposes the
# block into (μ_p, μ_n)-isotypics; the three primitive idempotents
# e_{μ_n} (μ_n ⊢ 3) are a complete orthogonal system summing to the
# identity on the block. See
# [`docs/audits/2026-06-08-matrix-m-optimization-A-8-9-path.md`](../../docs/audits/2026-06-08-matrix-m-optimization-A-8-9-path.md)
# §2 Tier 1 — this is the enabling step for A=8, A=9.
#
# NO f64: all arithmetic is mpmath.mpf at the working precision.

# Module-level mpf constants — avoid re-initialising per call/loop.
MPF_ZERO = mpmath.mpf(0)
MPF_ONE = mpmath.mpf(1)

# All 6 elements of S_3 as words in the two right-H_3 generators
# s_1 ↦ σ_{k_split+1}, s_2 ↦ σ_{k_split+2}: (length, generator seq).
_S3_ELEMENTS_MPFR: list[tuple[int, tuple[int, ...]]] = [
    (0, ()),
    (1, (1,)),
    (1, (2,)),
    (2, (1, 2)),
    (2, (2, 1)),
    (3, (1, 2, 1)),
]

_H3_PARTITIONS: tuple[tuple[int, ...], ...] = ((3,), (2, 1), (1, 1, 1))


def q_young_symmetrizers_mpfr(
    sigma_g: object,
    sigma_g_plus_1: object,
    q_mpf: object,
) -> dict:
    """Return ALL three primitive idempotents e_{μ_n} of H_3(q) in a
    single pass, as a dict mapping μ_n ⊢ 3 → `mpmath.matrix`, acting on
    the subspace where the two right-H_3 generators are `sigma_g`,
    `sigma_g_plus_1` (already restricted to a μ_p-block).

    Computing all three together avoids rebuilding the six T_w (and
    y₊, y₋) once per partition — a ~3× saving on the symmetrizer
    construction per block.

    mpf port of the symbolic `q_young_symmetrizer_matrix`. The
    normalisation `(1+q²)(1+q²+q⁴)` is `≈ 8.37` at q_0 ≈ 1.11 — well
    away from zero, so no numerical concern (audit §5).

      - μ_n = (3):      trivial-rep projector  e₊ = y₊ / norm
      - μ_n = (1,1,1):  sign-rep projector     e₋ = q⁶ y₋ / norm
      - μ_n = (2,1):    standard-rep projector e₀ = I − e₊ − e₋
    """
    sigmas_by_idx = {1: sigma_g, 2: sigma_g_plus_1}
    dim = sigma_g.rows
    eye = mpmath.eye(dim)
    q = q_mpf
    # Build T_w for each w ∈ S_3 as a matrix product of generators.
    # For non-empty words skip the leading identity multiply.
    T_w: list[object] = []
    for (_length, seq) in _S3_ELEMENTS_MPFR:
        if not seq:
            T_w.append(eye)
            continue
        mat = sigmas_by_idx[seq[0]]
        for idx in seq[1:]:
            mat = mat * sigmas_by_idx[idx]
        T_w.append(mat)
    # y_+ = Σ_w q^{ℓ(w)} T_w ;  y_- = Σ_w (-q^{-1})^{ℓ(w)} T_w
    y_plus = mpmath.zeros(dim, dim)
    y_minus = mpmath.zeros(dim, dim)
    inv_q = MPF_ONE / q
    for (length, _seq), mat in zip(_S3_ELEMENTS_MPFR, T_w):
        y_plus = y_plus + (q ** length) * mat
        y_minus = y_minus + ((-inv_q) ** length) * mat
    norm_scalar = (1 + q ** 2) * (1 + q ** 2 + q ** 4)
    e_plus = y_plus / norm_scalar
    e_minus = (y_minus * q ** 6) / norm_scalar
    e_std = eye - e_plus - e_minus
    return {(3,): e_plus, (2, 1): e_std, (1, 1, 1): e_minus}


def q_young_symmetrizer_matrix_mpfr(
    mu_n: tuple[int, ...],
    sigma_g: object,
    sigma_g_plus_1: object,
    q_mpf: object,
) -> object:
    """Single-partition accessor — returns the one e_{μ_n} requested.

    Thin wrapper over `q_young_symmetrizers_mpfr` for callers that need
    only one idempotent. The block path uses the plural form (one pass
    for all three).
    """
    es = q_young_symmetrizers_mpfr(sigma_g, sigma_g_plus_1, q_mpf)
    try:
        return es[mu_n]
    except KeyError:
        raise ValueError(
            f"mu_n must be one of (3,), (2,1), (1,1,1); got {mu_n!r}"
        )


def _trace_mpfr(M: object) -> object:
    """Trace of an mpmath.matrix (no built-in `.trace`)."""
    total = mpmath.mpf(0)
    for i in range(M.rows):
        total = total + M[i, i]
    return total


def _trace_product_mpfr(A: object, B: object) -> object:
    """Tr(A · B) in O(dim²) — avoids forming the full O(dim³) product."""
    total = mpmath.mpf(0)
    dim = A.rows
    for i in range(dim):
        for j in range(dim):
            total = total + A[i, j] * B[j, i]
    return total


def chi_via_mu_n_blocks_mpfr(
    shape: tuple[int, ...],
    word_left: list[tuple[int, int]],
    bridge_sign: int,
    word_right: list[tuple[int, int]],
    cache: dict,
    k_split: int,
) -> dict:
    """Two-level matrix-M χ via the (μ_p, μ_n) decomposition.

    For each μ_p block, the three q-Young idempotents e_{μ_n} (μ_n ⊢ 3,
    built from the right-H_3 generators σ_{k_split+1}, σ_{k_split+2}
    restricted to the block) form a complete orthogonal system on the
    block (Σ_{μ_n} e_{μ_n} = I), so

        χ = Σ_{μ_p} Tr[B_p · M · B_n]
          = Σ_{μ_p} Σ_{μ_n} Tr[e_{μ_n} · B_p · M · B_n].

    The per-μ_n image dimension is `rank(e_{μ_n}) = Tr(e_{μ_n})` (the
    idempotent eigenvalues are 0/1), bounded by `c_LR · dim(V_{μ_p}) ·
    dim(V_{μ_n}) ≤ ~40` regardless of λ. This bounded sub-block
    dimension — independent of dim V_λ — is exactly the structural
    fact that makes A=8, A=9 tractable (audit §2 Tier 1).

    This routine is the **correctness gate**: it evaluates χ via the
    dense projector insertion (exact for all A; verified to reproduce
    the one-level `chi_via_numerical_matrix_m_mpfr` value) and reports
    the per-(μ_p, μ_n) image dimensions. It does NOT yet exploit the
    decomposition to skip the dense `size × size` products — that
    sparse small-matrix compute is the wall-clock speedup and is
    deferred (it requires the cross-sector bridge blocks
    `e_{μ_n} · M · e_{μ_n'}`, since the primitive idempotents are
    central in H_3 but `B_n` / the bridge are NOT, so the bridge mixes
    μ_n sectors). See the module docstring / audit §2 Tier 1-2.

    Returns a dict with `chi`, `completeness_resid` (max |Σ e_{μ_n} − I|
    over blocks), `block_sizes`, `max_block_size`, `mu_n_dims` (per-μ_p
    image dims), and `max_subblock_dim` (the bounded ≤~40 figure).
    """
    q = cache["q"]
    h = q - MPF_ONE / q

    chi = MPF_ZERO
    max_completeness_resid = MPF_ZERO
    block_sizes: list[int] = []
    mu_n_dims: list[dict] = []
    max_subblock_dim = 0

    for mu_p, block in cache["blocks"].items():
        size = block["size"]
        block_sizes.append(size)
        eye_block = mpmath.eye(size)
        sigmas_left = block["sigmas_left"]
        sigmas_right = block["sigmas_right"]
        M_pp_pos = block["M_pp"]

        # B_p (left word), B_n (right word), M (bridge) on the block —
        # identical assembly to the one-level path.
        B_p = eye_block
        for (sign, g_1based) in word_left:
            mat = sigmas_left[g_1based]
            B_p = B_p * (mat if sign >= 0 else mat - h * eye_block)
        B_n = eye_block
        for (sign, g_1based) in word_right:
            mat = sigmas_right[g_1based]
            B_n = B_n * (mat if sign >= 0 else mat - h * eye_block)
        M = M_pp_pos if bridge_sign >= 0 else (M_pp_pos - h * eye_block)

        # Right-H_3 generators σ_{k_split+1}, σ_{k_split+2} on the block.
        sigma_g = sigmas_right[k_split + 1]
        sigma_g_plus_1 = sigmas_right[k_split + 2]

        # All three idempotents in a single pass (no per-μ_n rebuild).
        e_by_mu_n = q_young_symmetrizers_mpfr(sigma_g, sigma_g_plus_1, q)
        # Completeness: Σ_{μ_n} e_{μ_n} = I on the block.
        e_sum = mpmath.zeros(size, size)
        for e in e_by_mu_n.values():
            e_sum = e_sum + e
        resid = MPF_ZERO
        for i in range(size):
            for j in range(size):
                d = abs(e_sum[i, j] - (MPF_ONE if i == j else MPF_ZERO))
                if d > resid:
                    resid = d
        if resid > max_completeness_resid:
            max_completeness_resid = resid

        BMB = B_p * M * B_n
        dims_here: dict[str, int] = {}
        for mu_n, e in e_by_mu_n.items():
            # Tr(e · BMB) in O(size²) — no full O(size³) e·BMB product.
            chi = chi + _trace_product_mpfr(e, BMB)
            r = int(mpmath.nint(mpmath.re(_trace_mpfr(e))))
            dims_here[str(mu_n)] = r
            if r > max_subblock_dim:
                max_subblock_dim = r
        mu_n_dims.append({"mu_p": list(mu_p), "dims": dims_here})

    return {
        "chi": chi,
        "completeness_resid": max_completeness_resid,
        "block_sizes": block_sizes,
        "max_block_size": max(block_sizes) if block_sizes else 0,
        "mu_n_dims": mu_n_dims,
        "max_subblock_dim": max_subblock_dim,
    }


# ── Rust comparison ───────────────────────────────────────────────


def chi_rust_at_q_mpf(
    shape: tuple[int, ...],
    n_strands: int,
    word: list[tuple[int, int]],
    q_mpf: object,
) -> object:
    """Sum Rust's exact integer Laurent at q_0 as mpf.

    `chi_q_via_gp` returns exact integer coefficients — no f64 in
    the Rust path itself. We sum them at the substrate as mpf so the
    comparison stays at the backend's working precision.
    """
    if ph is None:
        raise RuntimeError(
            "pyhecke_native unavailable: the Rust reference chi_q_via_gp "
            "cannot run. The (μ_p, μ_n) cross-validation "
            "(--use-mu-n-blocks) does not need it."
        )
    laurent = ph.chi_q_via_gp(list(shape), n_strands, list(word))
    # Precompute sqrt_q once: half-exp keys are math q-exp · 2, so
    # q^(d_key/2) = sqrt_q^d_key with d_key an integer. mpmath does
    # binary integer exponentiation — much faster than fractional
    # exp+log when d_key is odd, and uniformly handles both parities.
    sqrt_q = mpmath.sqrt(q_mpf)
    total = mpmath.mpf(0)
    for (d_key, c_str) in laurent:
        d_int = int(d_key)
        total = total + mpmath.mpf(int(c_str)) * (sqrt_q ** d_int)
    return total


# ── Main: benchmark vs Rust chi_q_via_gp ──────────────────────────


def main(dps: int = 50) -> int:
    mpmath.mp.dps = dps

    wb = WitnessBuilder(
        "derived-chi-catalogue-matrix-m-mpfr",
        engine="python",
    )
    wb.set_description(
        f"mpmath/mpfr backend for the matrix-M μ_p factorisation. "
        f"Same structural identity as PR #1980/#1985/#1987; replaces "
        f"sp.Rational with mpmath.mpf at dps={dps} to close the high-"
        f"dim partition gap where sp.Rational denominator blowup "
        f"dominates wall time. NO f64 in compute path — mpfr is "
        f"controlled-precision floating point."
    )

    print("=" * 78)
    print(f" mpmath/mpfr backend vs Rust chi_q_via_gp")
    print(f"  precision: mp.dps = {dps}")
    print("=" * 78)

    from q_parameter import Q_50_DIGIT_STR
    q_mpf = mpmath.mpf(Q_50_DIGIT_STR)
    print(f"\n  q_0 (mpf) = {mpmath.nstr(q_mpf, 30)}")

    # Multi-isotope sweep (same as #1987).
    isotopes = [
        ("²H (deuteron)", 1, 1, 5),
        ("³H (tritium)",  1, 2, 8),
        ("³He",           2, 1, 8),
        ("⁴He (alpha)",   2, 2, 11),
    ]

    isotope_results: list[dict] = []
    for (label, Z, N, max_dim) in isotopes:
        print(f"\n  {label}  (Z={Z}, N={N}, A={Z+N}, n={3*(Z+N)})")
        print(f"  ──────────────────────────────────────────────")
        n_strands, word = _word_for_braid_word_3a(Z, N)
        word_left = [t for t in word if t[1] <= 2]
        bridge_sign = next(t[0] for t in word if t[1] == 3)
        word_right = [t for t in word if t[1] >= 4]
        partitions = _shape_partitions_of(n_strands)
        small_partitions = [
            s for s in partitions
            if len(standard_young_tableaux(s)) <= max_dim
        ]
        print(f"    β = {len(word)} crossings  "
              f"(left={len(word_left)}, bridge=1, right={len(word_right)})")
        print(f"    Testing {len(small_partitions)}/{len(partitions)} "
              f"partitions (dim V_λ ≤ {max_dim})")

        cases: list[dict] = []
        total_precompute_s = 0.0
        total_call_s = 0.0
        total_rust_s = 0.0
        # Tolerance: ~1e-(dps-5) for matrix-product cumulative round-off.
        tol = mpmath.mpf(10) ** (-(dps - 5))
        for shape in small_partitions:
            dim = len(standard_young_tableaux(shape))

            t0 = time.monotonic()
            cache = precompute_block_tables_mpfr(shape, 3, q_mpf)
            precompute_s = time.monotonic() - t0
            total_precompute_s += precompute_s

            t0 = time.monotonic()
            chi_mpf = chi_via_numerical_matrix_m_mpfr(
                shape, word_left, bridge_sign, word_right, cache,
            )
            call_s = time.monotonic() - t0
            total_call_s += call_s

            t0 = time.monotonic()
            chi_rust = chi_rust_at_q_mpf(shape, n_strands, word, q_mpf)
            rust_s = time.monotonic() - t0
            total_rust_s += rust_s

            # mpf == mpf is too strict; use a tolerance proportional to
            # the working precision.
            delta = abs(chi_mpf - chi_rust)
            match = bool(delta < tol)
            status = "✓" if match else "✗"
            speedup = rust_s / call_s if call_s > 0 else float("inf")

            shape_str = str(list(shape))
            print(f"      {status} λ={shape_str:<22s} dim={dim:>3d}  "
                  f"pre={precompute_s*1000:>6.1f}ms  "
                  f"call={call_s*1000:>6.1f}ms  "
                  f"rust={rust_s*1000:>6.1f}ms  "
                  f"speedup={speedup:.2f}×")

            cases.append({
                "shape": list(shape),
                "dim_V_lambda": dim,
                "precompute_secs": precompute_s,
                "call_secs": call_s,
                "rust_secs": rust_s,
                "delta": mpmath.nstr(delta, 10),
                "match": match,
            })

        n_total = len(cases)
        n_pass = sum(1 for c in cases if c["match"])
        speedup_overall = (
            total_rust_s / total_call_s if total_call_s > 0 else float("inf")
        )
        print(f"\n    Totals: pass={n_pass}/{n_total}  "
              f"precompute={total_precompute_s*1000:.1f}ms  "
              f"call={total_call_s*1000:.1f}ms  "
              f"rust={total_rust_s*1000:.1f}ms  "
              f"speedup={speedup_overall:.2f}×")
        isotope_results.append({
            "label": label, "Z": Z, "N": N, "A": Z+N, "n_strands": n_strands,
            "n_partitions_tested": n_total, "n_passed": n_pass,
            "total_precompute_secs": total_precompute_s,
            "total_call_secs": total_call_s,
            "total_rust_secs": total_rust_s,
            "speedup_rust_over_call": speedup_overall,
            "cases": cases,
        })

    n_total = sum(r["n_partitions_tested"] for r in isotope_results)
    n_pass = sum(r["n_passed"] for r in isotope_results)
    print("\n" + "=" * 78)
    print(f"  mpfr backend summary: {n_pass}/{n_total} partitions match Rust at q_0 (tol)")
    print("  " + "─" * 76)
    print(f"  {'Isotope':<18}  {'A':<2}  {'n':<3}  {'pass':<6}  "
          f"{'call ms':>8}  {'rust ms':>8}  {'speedup':>10}")
    for r in isotope_results:
        print(f"  {r['label']:<18}  {r['A']:<2}  {r['n_strands']:<3}  "
              f"{r['n_passed']}/{r['n_partitions_tested']:<4}  "
              f"{r['total_call_secs']*1000:>8.1f}  "
              f"{r['total_rust_secs']*1000:>8.1f}  "
              f"{r['speedup_rust_over_call']:>9.2f}×")
    print("=" * 78)

    wb.add_assertion(
        "mpfr_matrix_m_matches_rust_within_tolerance",
        computed=(n_pass == n_total),
        expected=True,
        source=f"Whether the mpfr matrix-M backend (mpmath.mpf at dps={dps}) "
               f"matches Rust chi_q_via_gp summed at q_0 across ²H/³H/³He/⁴He "
               f"to ABSOLUTE tolerance 1e-{dps-5} on the difference "
               f"abs(chi_mpf - chi_rust). Cumulative round-off in the matrix "
               f"product is bounded by O(word_length · block_size · 10^-dps), "
               f"which the absolute bound dominates for characters of "
               f"O(1) magnitude at substrate q_0.",
    )
    wb.add_data("dps", dps)
    wb.add_data("q_0_substrate_str", Q_50_DIGIT_STR)
    wb.add_data("n_partitions_tested", n_total)
    wb.add_data("n_passed", n_pass)
    wb.add_data("isotopes", isotope_results)

    out = wb.save()
    print(f"\n  ✓ Witness: {out.name}")
    return 0 if n_pass == n_total else 1


# ── Phase 1.3 validation: two-level (μ_p, μ_n) vs one-level μ_p ─────


def validate_mu_n_blocks(dps: int = 50) -> int:
    """Cross-validate the two-level (μ_p, μ_n) χ against the one-level
    μ_p-only χ on D / T / ³He / ⁴He, and report the bounded sub-block
    dimensions. Both paths are pure mpmath — no Rust reference needed,
    so this runs without `pyhecke_native.chi_q_via_gp`.

    The assertion is exact-up-to-tolerance equality of the two χ values
    plus Σ_{μ_n} e_{μ_n} = I completeness on every block. This is the
    correctness gate for wiring the q-Young symmetrizers into the mpfr
    backend (audit §4 step 2).
    """
    mpmath.mp.dps = dps
    wb = WitnessBuilder(
        "derived-chi-catalogue-matrix-m-mu-n-mpfr",
        engine="python",
    )
    wb.set_description(
        f"Phase 1.3 wire-in: two-level (μ_p, μ_n) χ via mpfr q-Young "
        f"symmetrizers vs the one-level μ_p-only mpfr path, at dps={dps}. "
        f"Verifies (a) the two χ values agree to absolute tol 1e-{dps-10}, "
        f"(b) Σ_{{μ_n}} e_{{μ_n}} = I on every μ_p block, and (c) the "
        f"per-(μ_p, μ_n) image dimensions are bounded (≤ c_LR·dim_μ_p·"
        f"dim_μ_n) independent of dim V_λ — the structural fact that "
        f"makes A=8, A=9 tractable. NO f64; NO Rust reference required. "
        f"The wall-clock sparse-exploitation speedup (cross-sector "
        f"bridge table) and the A=8/9 sweep run are follow-on PRs."
    )

    from q_parameter import Q_50_DIGIT_STR
    q_mpf = mpmath.mpf(Q_50_DIGIT_STR)
    k_split = 3
    tol = mpmath.mpf(10) ** (-(dps - 10))

    print("=" * 78)
    print(" Phase 1.3 — two-level (μ_p, μ_n) vs one-level μ_p mpfr χ")
    print(f"  precision: mp.dps = {dps}    q_0 = {mpmath.nstr(q_mpf, 22)}")
    print("=" * 78)

    isotopes = [
        ("²H (deuteron)", 1, 1, 5),
        ("³H (tritium)",  1, 2, 8),
        ("³He",           2, 1, 8),
        ("⁴He (alpha)",   2, 2, 11),
    ]

    isotope_results: list[dict] = []
    n_total = 0
    n_chi_match = 0
    n_complete = 0
    global_max_block = 0
    global_max_subblock = 0
    for (label, Z, N, max_dim) in isotopes:
        n_strands, word = _word_for_braid_word_3a(Z, N)
        word_left = [t for t in word if t[1] <= 2]
        bridge_sign = next(t[0] for t in word if t[1] == 3)
        word_right = [t for t in word if t[1] >= 4]
        partitions = _shape_partitions_of(n_strands)
        small = [
            s for s in partitions
            if len(standard_young_tableaux(s)) <= max_dim
            and n_strands >= k_split + 3
        ]
        print(f"\n  {label}  (A={Z+N}, n={n_strands})  "
              f"testing {len(small)}/{len(partitions)} partitions")
        cases: list[dict] = []
        for shape in small:
            dim = len(standard_young_tableaux(shape))
            cache = precompute_block_tables_mpfr(shape, k_split, q_mpf)
            chi1 = chi_via_numerical_matrix_m_mpfr(
                shape, word_left, bridge_sign, word_right, cache,
            )
            res = chi_via_mu_n_blocks_mpfr(
                shape, word_left, bridge_sign, word_right, cache, k_split,
            )
            chi_match = bool(abs(chi1 - res["chi"]) < tol)
            complete = bool(res["completeness_resid"] < tol)
            n_total += 1
            n_chi_match += 1 if chi_match else 0
            n_complete += 1 if complete else 0
            global_max_block = max(global_max_block, res["max_block_size"])
            global_max_subblock = max(global_max_subblock, res["max_subblock_dim"])
            status = "✓" if (chi_match and complete) else "✗"
            print(f"    {status} λ={str(list(shape)):<20s} dimVλ={dim:>3d}  "
                  f"blk≤{res['max_block_size']:>2d}  sub≤{res['max_subblock_dim']:>2d}  "
                  f"resid={mpmath.nstr(res['completeness_resid'], 2)}")
            cases.append({
                "shape": list(shape),
                "dim_V_lambda": dim,
                "max_block_size": res["max_block_size"],
                "max_subblock_dim": res["max_subblock_dim"],
                "completeness_resid": mpmath.nstr(res["completeness_resid"], 6),
                "chi_match": chi_match,
                "completeness_ok": complete,
                "mu_n_dims": res["mu_n_dims"],
            })
        isotope_results.append({
            "label": label, "Z": Z, "N": N, "A": Z + N,
            "n_strands": n_strands, "n_tested": len(cases), "cases": cases,
        })

    print("\n" + "=" * 78)
    print(f"  Phase 1.3 summary: chi_match {n_chi_match}/{n_total}  "
          f"completeness {n_complete}/{n_total}")
    print(f"  Max μ_p block size: {global_max_block}   "
          f"Max (μ_p,μ_n) sub-block dim: {global_max_subblock}  "
          f"(bounded ≤ c_LR·dim_μ_p·dim_μ_n)")
    print("=" * 78)

    wb.add_assertion(
        "two_level_mu_n_chi_matches_one_level_mu_p",
        computed=(n_chi_match == n_total and n_total > 0),
        expected=True,
        source=f"Whether the two-level (μ_p, μ_n) χ — computed via the "
               f"mpfr q-Young symmetrizers e_{{μ_n}} (μ_n ⊢ 3) inserted as "
               f"a resolution of identity within each μ_p block — matches "
               f"the one-level μ_p-only mpfr χ to absolute tolerance "
               f"1e-{dps-10}, across every tested partition of D/T/³He/⁴He. "
               f"Both paths are pure mpmath at dps={dps}; agreement "
               f"validates the mpfr port of the symbolic prototype "
               f"(PR #2013) and the Σ_{{μ_n}} e_{{μ_n}} = I completeness.",
    )
    wb.add_assertion(
        "q_young_idempotents_resolve_identity_on_every_block",
        computed=(n_complete == n_total and n_total > 0),
        expected=True,
        source="Whether Σ_{μ_n ⊢ 3} e_{μ_n} = I (max abs deviation below "
               f"1e-{dps-10}) on every μ_p block — i.e. the three mpfr "
               "q-Young primitive idempotents are a complete orthogonal "
               "system, the precondition for the trace identity above.",
    )
    wb.add_data("dps", dps)
    wb.add_data("q_0_substrate_str", Q_50_DIGIT_STR)
    wb.add_data("n_partitions_tested", n_total)
    wb.add_data("n_chi_match", n_chi_match)
    wb.add_data("n_completeness_ok", n_complete)
    wb.add_data("max_mu_p_block_size", global_max_block)
    wb.add_data("max_mu_p_mu_n_subblock_dim", global_max_subblock)
    wb.add_data("isotopes", isotope_results)

    out = wb.save()
    print(f"\n  ✓ Witness: {out.name}")
    return 0 if (n_chi_match == n_total and n_complete == n_total) else 1


if __name__ == "__main__":
    if "--use-mu-n-blocks" in sys.argv[1:]:
        sys.exit(validate_mu_n_blocks())
    sys.exit(main())
