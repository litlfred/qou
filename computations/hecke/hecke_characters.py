#!/usr/bin/env python3
"""
Hecke character engine: compute χ_λ(braid_word) for any partition λ
at any level k, using seminormal representation matrices.

The engine builds EXACT representation matrices in the seminormal
basis for each partition of n, then multiplies crossing matrices
through the nuclear braid word and takes the trace.

This gives the FULL k-point character — all correlation orders
included automatically. No truncation, no approximation.

Architecture:
  1. Enumerate standard Young tableaux for partition λ
  2. Build seminormal matrices for σ₁..σ_{n-1} (exact in q₀)
  3. For each nuclear crossing (c·σ_gen + d), build the crossing matrix
  4. Multiply ALL crossing matrices → braid matrix in irrep λ
  5. Take trace → χ_λ(nuclear braid)
  6. Weight by w_λ = dim_q(λ)²/[n]_q! → partition contribution to binding

Usage:
    from hecke_characters import compute_mass_at_level
    M_pred, details = compute_mass_at_level(Z, N, k=6)
"""


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import math
import numpy as np
import sys
from pathlib import Path
from mpmath import mp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q, Q_INV, HA, q_int, Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

q0 = Q; qi0 = Q_INV; h = HA; me = M_E_MEV
z = q0**3 / (q0**2 + 1)

# E_0 calibration: free-neutron β-decay Q-value (MeV), per
# prop:categorical-mass-markov / hecke_core.E_0_CALIBRATION_MEV.
# This is the SINGLE archimedean calibration τ: R → ℝ from
# categorical mass to MeV.  The former ALPHA = m_e · 8 · Catalan
# convention (hyperbolic-volume heuristic) is removed — it was
# not derivable from the mass-identity prescription.
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402
E_0_BETA_DECAY_Q_MEV = Q_NEUTRON_MEV  # CODATA: 0.78233341 ± 6.1e-7 MeV


# ══════════════════════════════════════════════════════════════
# §1  STANDARD YOUNG TABLEAUX
# ══════════════════════════════════════════════════════════════

def partitions_of(n):
    """Generate all partitions of n."""
    if n == 0:
        yield ()
        return
    def g(n, mx):
        if n == 0:
            yield ()
            return
        for i in range(min(n, mx), 0, -1):
            for r in g(n - i, i):
                yield (i,) + r
    yield from g(n, n)


def young_diagram_cells(shape):
    """Return list of (row, col) cells for the Young diagram."""
    cells = []
    for i, ri in enumerate(shape):
        for j in range(ri):
            cells.append((i, j))
    return cells


def standard_young_tableaux(shape):
    """Generate all SYT of given shape.
    Returns list of dicts: {entry: cell_index}."""
    n = sum(shape)
    cells = young_diagram_cells(shape)
    contents = [c - r for r, c in cells]
    nc = len(cells)

    results = []

    def _fill(entry, filled, cell_available):
        if entry > n:
            results.append(dict(filled))
            return
        for ci in range(nc):
            if not cell_available[ci]:
                continue
            r, c = cells[ci]
            # Must be leftmost available in its row and topmost in its column
            if c > 0:
                # Cell to the left must be filled
                left_ci = None
                for k, (rr, cc) in enumerate(cells):
                    if rr == r and cc == c - 1:
                        left_ci = k
                        break
                if left_ci is not None and cell_available[left_ci]:
                    continue  # left neighbor not yet filled
            if r > 0:
                # Cell above must be filled
                above_ci = None
                for k, (rr, cc) in enumerate(cells):
                    if rr == r - 1 and cc == c:
                        above_ci = k
                        break
                if above_ci is not None and cell_available[above_ci]:
                    continue  # above neighbor not yet filled
            # Place entry here
            filled[entry] = ci
            cell_available[ci] = False
            _fill(entry + 1, filled, cell_available)
            del filled[entry]
            cell_available[ci] = True

    _fill(1, {}, [True] * nc)
    return results, cells, contents


# ══════════════════════════════════════════════════════════════
# §2  SEMINORMAL REPRESENTATION MATRICES
# ══════════════════════════════════════════════════════════════

def build_seminormal_matrices(shape, sparse=None, q=None):
    """Build representation matrices for σ₁..σ_{n-1} in the
    seminormal basis for partition `shape`.

    Returns: list of numpy/scipy arrays [σ₁, σ₂, ..., σ_{n-1}]
             (0-indexed: sigmas[0] = σ₁)

    If `q` is supplied, build matrices at that q (override).  Otherwise
    the module-level default `q0` from `q_parameter.py` is used.  The
    override path enables CRT-style multi-q probing for q-rational
    reconstruction (see prop:alpha-k-derivation-procedure
    §"CRT-style q-rational reconstruction").

    If sparse=True (or sparse=None and dim > 500), uses scipy sparse
    CSR matrices. Each Hoefsmit matrix has at most 2 nonzeros per row
    (block-diagonal with 1×1 and 2×2 blocks), so sparse format gives
    ~dim/2 × memory savings.
    """
    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)

    if dim == 0:
        return [], dim, syts

    # Resolve q (override or module default).  Derive amplitude h locally.
    q_local = float(q0) if q is None else float(q)
    h_local = q_local - 1.0 / q_local

    use_sparse = sparse if sparse is not None else (dim > 500)

    sigmas = []

    # O(1) swap-partner lookup (the former linear scan made construction
    # O(n·dim²) — the wall at dim ≳ 2·10⁴, e.g. n = 15 blocks). Depends only
    # on `syts`, so build it once outside the per-generator loop.
    syt_index = {tuple(sorted(t.items())): idx for idx, t in enumerate(syts)}

    for k in range(1, n):  # generator σ_k swaps entries k and k+1
        rows, cols, vals = [], [], []
        processed = set()

        for i in range(dim):
            if i in processed:
                continue

            # Axial distance: content(cell of k+1) - content(cell of k)
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]

            # Diagonal element: a_ρ = h/(1-q^{-2ρ})
            a = h_local / (1.0 - q_local**(-2 * rho))

            # Find swap partner: swap entries k and k+1
            swap_map = dict(syts[i])
            swap_map[k] = ci_k1
            swap_map[k + 1] = ci_k

            # Check if swap gives valid SYT
            j = syt_index.get(tuple(sorted(swap_map.items())))
            if j == i:
                j = None

            if j is None:
                # 1×1 block: eigenvalue is q (same row) or -q⁻¹ (same col)
                rows.append(i); cols.append(i); vals.append(a)
                processed.add(i)
            else:
                # 2×2 block
                a_prime = h_local / (1.0 - q_local**(2 * rho))  # = a_{-ρ}
                # b² = a·a' + 1 (from det = -1)
                b_sq = a * a_prime + 1.0
                b = float(mp.sqrt(abs(b_sq)))

                rows.extend([i, j, i, j])
                cols.extend([i, j, j, i])
                vals.extend([a, a_prime, b, b])

                processed.add(i)
                processed.add(j)

        if use_sparse:
            from scipy import sparse as sp_sparse
            M = sp_sparse.csr_matrix((vals, (rows, cols)), shape=(dim, dim))
        else:
            M = np.zeros((dim, dim))
            for r, c, v in zip(rows, cols, vals):
                M[r, c] = v

        sigmas.append(M)

    return sigmas, dim, syts


# ══════════════════════════════════════════════════════════════
# §3  NUCLEAR BRAID CHARACTER
# ══════════════════════════════════════════════════════════════

# Optional Rust acceleration: pyhecke_native.chi_lambda_braid is
# 50–100× faster than the pure-Python seminormal multiplication for
# n ≥ 9.  Falls back transparently to Python if the wheel isn't
# installed (CI without the Rust toolchain, or fresh checkout
# without `maturin build`).
try:
    import pyhecke_native as _pyn
    _RUST_CHI_AVAILABLE = True
except ImportError:
    _pyn = None
    _RUST_CHI_AVAILABLE = False


# Precision-tag registry — every character / mass / binding result
# downstream is required to carry one of these tags.  See the user
# directive: "no fittings, short cuts, approx — symbolic in q or
# high precision > 50 — keep track of which".
PRECISION_F64_FALLBACK = "f64_numeric_fallback"
PRECISION_MPFR_50DPS = "mpfr_50dps"
PRECISION_SYMBOLIC_Q = "symbolic_q"
PRECISION_TAGS = {PRECISION_F64_FALLBACK, PRECISION_MPFR_50DPS, PRECISION_SYMBOLIC_Q}


def _parse_precision(precision):
    """Normalize a `precision` arg to a canonical tag.

    Accepts:
      - "f64" / "fast" / "f64_numeric_fallback"  → f64 (16 dps, fast)
      - "mpfr" / "exact" / int N (≥ 50)          → mpfr at N dps (default 50)
      - "symbolic" / "symbolic_q"                → symbolic (deferred)

    Returns `(canonical_tag, dps_or_None)`.
    """
    if precision is None or precision == "f64" or precision == "fast" \
            or precision == PRECISION_F64_FALLBACK:
        return (PRECISION_F64_FALLBACK, None)
    if precision == "mpfr" or precision == "exact" or precision == PRECISION_MPFR_50DPS:
        return (PRECISION_MPFR_50DPS, 50)
    if isinstance(precision, int) and precision >= 50:
        return (f"mpfr_{precision}dps", precision)
    if isinstance(precision, str) and precision.startswith("mpfr_") and precision.endswith("dps"):
        try:
            dps = int(precision[5:-3])
            return (precision, dps)
        except ValueError:
            pass
    if precision == "symbolic" or precision == PRECISION_SYMBOLIC_Q:
        return (PRECISION_SYMBOLIC_Q, None)
    raise ValueError(
        f"Unrecognized precision tag: {precision!r}. "
        f"Use one of: 'f64', 'mpfr', 'mpfr_50dps', int >= 50, or 'symbolic'."
    )


def chi_lambda_braid(shape, word, q_value=None, precision=None,
                     return_precision=False):
    """Character `χ_λ(β)` of a Hecke braid word at parameter `q`.

    Args:
        shape: partition `λ ⊢ n` as tuple/list of descending parts.
        word: braid word as `[(sign, generator_1based), ...]`,
              `sign ∈ {+1, -1}` or `'+'/'-'`,
              `generator ∈ {1, ..., n-1}`.
        q_value: Hecke parameter (default: substrate `q₀ = Q`).
        precision: one of:
            None / "f64" / "fast"        → f64 (~16 dps), fast Rust kernel
            "mpfr" / "mpfr_50dps" / 50  → mpfr at 50 dps, exact (no f64 round)
            "mpfr_<N>dps" / int N≥50    → mpfr at N dps
            "symbolic" / "symbolic_q"    → symbolic in q (NotImplementedError; F3)
        return_precision: if True, return `(value, precision_tag)`;
            if False (default), return value only.

    Defaults to `f64` for backward compatibility — but downstream code
    that records witnesses MUST pass `precision="mpfr_50dps"` (or
    higher) to satisfy the "no approximations" directive, OR record
    the returned `precision` tag in the witness JSON.

    Returns the character.  For `f64`: returns `float`. For `mpfr_*`:
    returns a string of the decimal expansion (caller may parse via
    `mpmath.mpf`).  For `symbolic_q`: not yet implemented (raises).
    """
    if q_value is None:
        q_value = float(q0)
    tag, dps = _parse_precision(precision)

    # Normalize word.
    word_marshalled = [
        (1 if (s == '+' or s == 1 or s is True) else -1, int(g))
        for s, g in word
    ]

    if tag == PRECISION_SYMBOLIC_Q:
        raise NotImplementedError(
            "symbolic-in-q character evaluation is deferred to F3 "
            "(Murnaghan–Nakayama / Ram–Wenzl recursion in Rust). "
            "For now use precision='mpfr_50dps' for exact evaluation."
        )

    if tag.startswith("mpfr_"):
        if not _RUST_CHI_AVAILABLE:
            raise NotImplementedError(
                f"precision={tag} requires the Rust kernel "
                "(pyhecke_native). Install via `maturin build` in "
                "tools/pyhecke-native/."
            )
        # Preserve full precision in q_value: if caller passes a string
        # like "1.10998", route it directly to mpfr without going through
        # f64 (which would lose precision to ~16 dps).
        if isinstance(q_value, str):
            q_str = q_value
        else:
            # f64 → string at f64-equivalent precision (caller chose
            # to pass a float — implicit acceptance of f64 boundary loss).
            q_str = format(float(q_value), f".{(dps or 50) + 5}g")
        result = _pyn.chi_lambda_braid_mpfr(
            list(shape), word_marshalled, q_str, dps or 50
        )
        return (result, tag) if return_precision else result

    # Default: f64 fast path.
    if _RUST_CHI_AVAILABLE:
        value = _pyn.chi_lambda_braid(
            list(shape), word_marshalled, float(q_value)
        )
        return (value, PRECISION_F64_FALLBACK) if return_precision else value

    # Python fallback: build seminormal matrices and multiply.
    # `build_seminormal_matrices` accepts a `q=` override (resolves
    # `q_local = q_value if q is not None else q0`); pass the caller's
    # q_value through so the fallback supports arbitrary q (cross-anchor
    # q-stability probes, q-rational reconstruction per
    # prop:alpha-k-derivation-procedure §"CRT-style q-rational
    # reconstruction").
    #
    # Normalize q_value to float ONCE here, and use q_f consistently in
    # both the q= override AND the h_local computation below — so
    # callers passing mpmath / str / numeric types don't break NumPy
    # dtype handling further down (per Copilot review on PR #1861).
    q_f = float(q_value)
    sigmas, dim, _ = build_seminormal_matrices(tuple(shape), q=q_f)
    if dim == 0:
        return 0.0
    from scipy import sparse as sp_sparse
    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False
    if is_sparse:
        product = sp_sparse.eye(dim, format='csr')
        I = sp_sparse.eye(dim, format='csr')
    else:
        product = np.eye(dim)
        I = np.eye(dim)
    h_local = q_f - 1.0 / q_f
    for sign, gen in word_marshalled:
        idx = gen - 1
        if idx < 0 or idx >= len(sigmas):
            continue
        if sign > 0:
            M = sigmas[idx]
        else:
            M = sigmas[idx] - h_local * I
        product = product @ M
    if is_sparse:
        return float(product.diagonal().sum())
    return float(np.trace(product))


def chi_lambda_braid_mpf(shape, signed_word, q_value=None, dps=None):
    """Full-precision χ_λ(β) as an ``mpmath.mpf`` via the mpfr Rust kernel.

    Single chokepoint for the ``mpf → decimal-string → mpfr → mpf``
    marshalling so the HOMFLY Ocneanu engine
    (``homfly_ocneanu_trace._chi``) and the 1ppb cross-check χ-anchor
    (``cross_check_trM_1ppb``) do not each re-implement the precision-tag
    and guard-digit pattern.

    Args:
        shape: partition ``λ ⊢ n`` (tuple/list of descending parts).
        signed_word: braid word as a flat list of **signed** 1-based
            generators (e.g. ``[1, -2, 1]``); marshalled to
            ``chi_lambda_braid``'s ``(sign, generator)`` form internally.
        q_value: Hecke parameter — ``mpf`` / ``float`` / ``str`` /
            ``None`` (→ substrate ``q₀`` as the canonical 50-digit string
            ``Q_50_DIGIT_STR``). A string is passed through verbatim (full
            precision); an ``mpf`` is rendered to ``dps + 5`` guard digits.
            **Avoid passing a Python ``float``** for the substrate value:
            the module-level ``q0`` is a float64, so ``q0`` and
            ``float(q0)`` only carry ~16 digits and would cap the mpfr
            path — pass ``Q_50_DIGIT_STR`` (or an ``mpf`` built from it).
        dps: target precision; default ``max(50, current mpmath dps)``.

    Returns an ``mpmath.mpf``. Note ``mp.mpf`` *rounds* the kernel's
    decimal string to the current working precision — it is deterministic
    at ``dps``, not an exact real. The string/precision-tag construction
    is O(dps) and negligible beside the kernel's matrix evaluation, so it
    is recomputed per call rather than cached.
    """
    if dps is None:
        dps = max(50, mp.dps)
    if q_value is None:
        # Default to the canonical high-precision substrate string, NOT the
        # module-level float64 `q0` (which would silently cap the mpfr path).
        q_value = Q_50_DIGIT_STR
    q_str = (q_value if isinstance(q_value, str)
             else mp.nstr(mp.mpf(q_value), dps + 5, strip_zeros=False))
    hc = [(1, g) if g > 0 else (-1, -g) for g in signed_word]
    return mp.mpf(chi_lambda_braid(list(shape), hc,
                                   q_value=q_str, precision=f"mpfr_{dps}dps"))


def chi_lambdas_braid(shapes, word, q_value=None, precision=None):
    """**Batch variant of `chi_lambda_braid`** — single PyO3 crossing for
    a list of partitions, all evaluated on the same braid word at the
    same parameter `q`.

    Args mirror `chi_lambda_braid` but take a *list* of `shapes` and
    return a list of characters in the same order.

    Backed by `pyhecke_native.chi_lambdas_braid` (f64) or
    `chi_lambdas_braid_mpfr` (MPFR-50dps).  Both are rayon-parallel
    over partitions on the Rust side — substantially faster than
    Python-level `for shape in shapes: chi_lambda_braid(...)` because
    it (a) saves N-1 PyO3 boundary crossings, (b) shares the
    word-marshalling work, and (c) gets work-stealing parallelism.

    Tier 1 of the `ffi-roundtrip-audit` skill catalogues 5 sites
    where this batch form replaces the per-shape loop (F-A pattern);
    see `.claude/skills/local/ffi-roundtrip-audit.md`.
    """
    if q_value is None:
        q_value = float(q0)
    tag, dps = _parse_precision(precision)

    word_marshalled = [
        (1 if (s == '+' or s == 1 or s is True) else -1, int(g))
        for s, g in word
    ]

    if tag == PRECISION_SYMBOLIC_Q:
        raise NotImplementedError(
            "symbolic-in-q character evaluation is deferred to F3."
        )

    shapes_list = [list(s) for s in shapes]

    if tag.startswith("mpfr_"):
        if not _RUST_CHI_AVAILABLE:
            raise NotImplementedError(
                f"precision={tag} requires the Rust kernel "
                "(pyhecke_native).  Install via `maturin build` in "
                "tools/pyhecke-native/."
            )
        if isinstance(q_value, str):
            q_str = q_value
        else:
            q_str = format(float(q_value), f".{(dps or 50) + 5}g")
        return _pyn.chi_lambdas_braid_mpfr(
            shapes_list, word_marshalled, q_str, dps or 50
        )

    # f64 path.
    if _RUST_CHI_AVAILABLE:
        return _pyn.chi_lambdas_braid(
            shapes_list, word_marshalled, float(q_value)
        )

    # Python fallback (slow): loop the singular path.
    return [
        chi_lambda_braid(s, word, q_value=q_value, precision=precision)
        for s in shapes_list
    ]


def crossing_coeffs(ti, tj):
    """Crossing (c, d) for nucleon types: 1=proton, 0=neutron."""
    if ti == 1 and tj == 1:
        return 1.0, 0.0       # pp: σ
    elif ti == 0 and tj == 0:
        return 1.0, -h        # nn: σ⁻¹
    else:
        return 1.0, -h / 2    # pn: mixed


def nuclear_braid_character(Z, N, sigmas, dim, n_gens):
    """Compute χ_λ(INTER-nucleon braid) for a partition with given sigmas.

    **IMPORTANT**: This function computes only the INTER-nucleon
    crossings (pairs of nucleons crossing each other). For A=1
    (single nucleon), there are no inter-nucleon crossings, so this
    returns dim(V_λ) — the trace of the identity matrix.

    The INTRA-nucleon crossings (quark-level structure within a
    single nucleon, including averaged crossings I = σ − (h/2)·1
    that encode quark flavour) are computed by the PIPELINE path:
      atom_braid_word_3A → canonical_braid_crossings →
      light_isotope_sweep.tr_M_at_q0

    For the FULL character (intra + inter), use the pipeline path.
    This function is a building block for A ≥ 2 computations where
    the inter-nucleon crossings are multiplied AFTER the
    intra-nucleon ones.

    The nuclear braid for A nucleons has crossings between all pairs.
    Each crossing at generator g with coefficients (c, d) gives
    matrix c·σ_g + d·I in the representation.

    We multiply ALL crossing matrices and take the trace.

    Generator assignment: for crossing between nucleons i and j (i<j),
    use generator g = (i + j) mod n_gens (cycling through available gens).
    """
    A = Z + N
    if A <= 1 or dim == 0:
        return float(dim)

    # Ground state ordering: interleaved p, n
    ordering = []
    pc, nc_ = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc_ >= N:
            ordering.append(1)
            pc += 1
        else:
            ordering.append(0)
            nc_ += 1

    # Accumulate product of crossing matrices
    # Handle both dense (numpy) and sparse (scipy) matrices
    from scipy import sparse as sp_sparse
    is_sparse = sp_sparse.issparse(sigmas[0]) if sigmas else False

    if is_sparse:
        product = sp_sparse.eye(dim, format='csr')
        I = sp_sparse.eye(dim, format='csr')
    else:
        product = np.eye(dim)
        I = np.eye(dim)

    for i in range(A - 1):
        for j in range(i + 1, A):
            c, d = crossing_coeffs(ordering[i], ordering[j])
            # Generator index (0-based): cycle through available generators
            g = (i + j) % n_gens
            M = c * sigmas[g] + d * I
            product = product @ M

    if is_sparse:
        return float(product.diagonal().sum())
    return np.trace(product)


# ══════════════════════════════════════════════════════════════
# §4  MASS AT LEVEL k
# ══════════════════════════════════════════════════════════════

def _q_int_at(k, q):
    """`[k]_q = (q^k - q^-k)/(q - q^-1)` at an EXPLICIT q.

    The module-level `q_int` closes over `q_parameter.Q` — the SHIM's Q, which
    the shim rebinds to muon when the running process's argv stem is listed in
    `q0_anchor_manifest.json::ideal_muon`. So every q-integer here is a function
    of the ENTRY POINT unless the caller names its q (bean qou-wee5).
    """
    h = q - 1 / q
    return (q ** k - q ** (-k)) / h


def qfac(n, q=None):
    """`[n]_q!`. `q=None` keeps the historical module-level q — see the note on
    `_q_int_at` for why that tracks the entry point, and pass `q` explicitly if
    your result must not."""
    if q is None:
        return math.prod(q_int(k) for k in range(1, n + 1))
    return math.prod(_q_int_at(k, q) for k in range(1, n + 1))


def young_hooks(shape):
    cells = young_diagram_cells(shape)
    rows = list(shape)
    max_col = rows[0] if rows else 0
    cols = [sum(1 for r in rows if r > j) for j in range(max_col)]
    hooks = []
    for r, c in cells:
        hook = (rows[r] - c - 1) + (cols[c] - r - 1) + 1
        hooks.append(hook)
    return hooks


def dim_q(shape, q=None):
    """`d_q(λ)` by the q-hook-length formula. `q=None` keeps the historical
    module-level q; pass `q` explicitly to pin the anchor (bean qou-wee5)."""
    n = sum(shape)
    if q is None:
        return qfac(n) / math.prod(q_int(hk) for hk in young_hooks(shape))
    return qfac(n, q) / math.prod(_q_int_at(hk, q) for hk in young_hooks(shape))


def specht_dim(shape):
    """Integer Specht-module dimension `f^λ = #SYT(λ) = n! / ∏ hook(c)`
    (hook-length formula) — the `q → 1` specialisation of `dim_q`.

    Centralised here (next to `young_hooks` / `dim_q`, reusing the single
    `young_hooks` implementation) so binding / observe-last consumers share
    one hook-length routine instead of re-deriving it (Gemini review, PR
    #2408). Accepts any iterable partition (tuple or list)."""
    n = sum(shape)
    d = math.factorial(n)
    for hk in young_hooks(shape):
        d //= hk
    return d


# ════════════════════════════════════════════════════════════════════
# v3 mass functions removed 2026-05-03 — see audit
#   docs/audits/2026-05-03-categorical-mass-divergence-audit.md
#
# `compute_mass_at_level` and `compute_mass_at_3A` evaluated a different
# braid (nucleon-strand, A strands) than the canonical atom_braid_word_3A
# (3A quark strands), giving Markov-trace values that disagreed with the
# Hoefsmit+Wenzl bridge by orders of magnitude (e.g., D: 1.3e-17 vs
# canonical 0.388).  Their predictions only matched data because Mfree
# dominates atomic mass (1000× the binding); the categorical part
# saturated at a near-constant ~0.78 MeV.
#
# The singular canonical 6-term mass formula is
# `paper_six_term_isotope_sweep.py`.  Utilities (partitions_of, qfac,
# young_hooks, dim_q, build_seminormal_matrices, chi_lambda_braid,
# nuclear_braid_character, crossing_coeffs) remain available above.
# ════════════════════════════════════════════════════════════════════
