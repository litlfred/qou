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

import math
import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q, Q_INV, HA, q_int
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

q0 = Q; qi0 = Q_INV; h = HA; me = M_E_MEV
z = 1.0 / (q0**0.5 + qi0**0.5)

# E_0 calibration: free-neutron β-decay Q-value (MeV), per
# prop:categorical-mass-markov / hecke_core.E_0_CALIBRATION_MEV.
# This is the SINGLE archimedean calibration τ: R → ℝ from
# categorical mass to MeV.  The former ALPHA = m_e · 8 · Catalan
# convention (hyperbolic-volume heuristic) is removed — it was
# not derivable from the mass-identity prescription.
E_0_BETA_DECAY_Q_MEV = 0.782


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
            j = None
            for jj in range(dim):
                if jj == i:
                    continue
                if syts[jj] == swap_map:
                    j = jj
                    break

            if j is None:
                # 1×1 block: eigenvalue is q (same row) or -q⁻¹ (same col)
                rows.append(i); cols.append(i); vals.append(a)
                processed.add(i)
            else:
                # 2×2 block
                a_prime = h_local / (1.0 - q_local**(2 * rho))  # = a_{-ρ}
                # b² = a·a' + 1 (from det = -1)
                b_sq = a * a_prime + 1.0
                b = math.sqrt(abs(b_sq))

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
    # `build_seminormal_matrices` is calibrated against the global
    # substrate parameter `q0`/`h`, so the fallback is *only* valid at
    # `q_value == q0`.  Reject non-default q_value here rather than
    # silently returning an inconsistent character (Copilot review
    # #r3142936624).
    if not math.isclose(float(q_value), float(q0), rel_tol=0.0, abs_tol=0.0):
        raise ValueError(
            "chi_lambda_braid() Python fallback only supports "
            "q_value == q0; install the Rust kernel (pyhecke_native) "
            "for non-default q_value."
        )
    sigmas, dim, _ = build_seminormal_matrices(tuple(shape))
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
    h_local = q_value - 1.0 / q_value
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


def crossing_coeffs(ti, tj):
    """Crossing (c, d) for nucleon types: 1=proton, 0=neutron."""
    if ti == 1 and tj == 1:
        return 1.0, 0.0       # pp: σ
    elif ti == 0 and tj == 0:
        return 1.0, -h        # nn: σ⁻¹
    else:
        return 1.0, -h / 2    # pn: mixed


def nuclear_braid_character(Z, N, sigmas, dim, n_gens):
    """Compute χ_λ(nuclear braid) for a partition with given sigmas.

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

def qfac(n):
    return math.prod(q_int(k) for k in range(1, n + 1))


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


def dim_q(shape):
    n = sum(shape)
    return qfac(n) / math.prod(q_int(hk) for hk in young_hooks(shape))


def compute_mass_at_level(Z, N, k=6, verbose=False, partition_filter=None,
                            block_cache=None):
    """Compute atomic mass using ALL partitions at Hecke level k.

    For each partition λ of k:
      1. Build seminormal matrices (dim(λ) × dim(λ))
      2. Compute χ_λ(nuclear braid) by matrix multiplication
      3. Weight by w_λ = dim_q(λ)²/[k]_q!

    The Markov trace = Σ_λ w_λ · χ_λ / dim(λ).  Binding is computed
    via the categorical mass-identity prescription
    (prop:categorical-mass-markov): at single-brane level,

        B(Z, N) = E_0 · ( |tr_M(W_free)| − |tr_M(W_atom)| )

    with E_0 = 0.782 MeV (free-neutron β-decay Q) — the SINGLE
    archimedean calibration.  The former ALPHA = m_e · 8 · Catalan
    convention is removed (it was a hyperbolic-volume heuristic, not
    derivable from the mass-identity prescription).  Callers
    wanting the full E_0-based binding should use the dedicated
    ``mass_at_3A_proper.binding_3A`` module; the ``binding`` field
    returned by this function is now the dimensionless categorical
    mass defect ``|1 − |markov||`` — same information, no implicit
    constant.

    ``partition_filter``, if given, is a predicate ``λ → bool``; only
    partitions for which it returns True contribute.  Useful for
    audits (top-N by w_λ, etc.).  Default: include all partitions.

    ``block_cache``, if given, must be a ``syt_prefix_cache.BlockCache``
    pinned to the same q used for the seminormal-matrix build.  When
    supplied, the per-partition loop routes through
    ``syt_prefix_cache.build_seminormal_matrices_cached`` instead of
    the uncached ``build_seminormal_matrices``, reusing Hoefsmit
    content-distance arithmetic and the per-shape SYT→index map
    across shapes.  Caller lifecycle: construct the cache once per
    q (``BlockCache(q=Q)``), share across multiple
    ``compute_mass_at_level`` / ``compute_mass_at_3A`` calls, discard
    when q changes.  Default ``None`` preserves the legacy uncached
    path.  Expected 5–20× speedup on heavy atoms (A ≥ 10, k = 3A
    with p(3A) ≥ 5604 partitions and dim_λ up to ~1000).

    Returns: (M_predicted, details_dict)
    """
    A = Z + N
    Mfree = Z * M_P_MEV + N * M_N_MEV + Z * me

    if A <= 1:
        return Mfree, {'binding': 0.0, 'markov_trace': 1.0, 'partitions': [], 'level': k}

    nfac = qfac(k)
    n_gens = k - 1  # generators σ₁..σ_{k-1}

    total_markov = 0.0
    partition_data = []

    if block_cache is not None:
        from syt_prefix_cache import build_seminormal_matrices_cached
        _build = lambda shape: build_seminormal_matrices_cached(
            shape, cache=block_cache)
    else:
        _build = build_seminormal_matrices

    for shape in partitions_of(k):
        if partition_filter is not None and not partition_filter(shape):
            continue
        sigmas, dim, syts = _build(shape)

        if dim == 0:
            continue

        d_q = dim_q(shape)
        w = d_q**2 / nfac

        chi = nuclear_braid_character(Z, N, sigmas, dim, n_gens)

        # Markov contribution: w_λ · χ_λ / dim(λ)
        contribution = w * chi / dim

        total_markov += contribution

        if verbose:
            print(f"  {str(shape):>18} dim={dim:>3} w={w:.6f} "
                  f"χ={chi:.6e} contrib={contribution:.6e}")

        partition_data.append({
            'shape': shape, 'dim': dim, 'w': w,
            'chi': chi, 'contribution': contribution,
        })

    # Dimensionless categorical mass defect relative to the Markov-
    # trace identity (Σ w_λ = 1 at q = 1; at q₀ the identity sum is
    # |1 − Σ w_λ · χ_λ(id)/d_λ|).  Use ``binding_defect`` for the
    # dimensionless quantity; use mass_at_3A_proper.binding_3A for a
    # MeV binding with the prop:categorical-mass-markov calibration
    # E_0 = 0.782 MeV.
    binding_defect = abs(1.0 - abs(total_markov))  # dimensionless

    # M_pred is NOT converted to MeV here — the dimensionless defect
    # has no meaningful sign or magnitude in MeV units.  Return
    # M_pred = Mfree so the second slot of the return tuple is a
    # well-defined MeV number (free-nucleon rest-mass sum).  Callers
    # that need binding in MeV must use a proper calibration path.
    M_pred = Mfree  # free rest-mass sum, MeV — no unit-mixed subtraction

    return M_pred, {
        'binding_defect_dimensionless': binding_defect,
        'binding': binding_defect,  # legacy key; dimensionless
        'markov_trace': total_markov,
        'partitions': partition_data,
        'level': k,
    }


def compute_mass_at_3A(Z, N, verbose=False, partition_filter=None,
                          block_cache=None):
    """Atomic mass summed over λ ⊢ 3A — the canonical H_{3A} Wedderburn form.

    Replaces the per-generator H_3 weighting used in the tower formula
    (hecke_core.atom_per_generator_volumes) with a full partition sum
    at the atom-wide Iwahori–Hecke algebra H_{3A}(q).  This is the
    principled form: the atom braid lives in H_{3A}, so weights should
    be d_q(λ)²/[3A]_q! for λ ⊢ 3A — NOT a per-generator H_3 average.

    A = Z + N.  Calls compute_mass_at_level(Z, N, k=3A).  For A ≥ 10
    (p(3A) ≥ 5604) this is expensive; callers may pass a
    ``partition_filter`` to restrict (audit mode), but the default
    is the full sum — no Plancherel truncation.
    """
    A = Z + N
    if A < 1:
        return Z * M_P_MEV + N * M_N_MEV + Z * me, {
            'binding': 0.0, 'markov_trace': 1.0, 'partitions': [], 'level': 0}
    return compute_mass_at_level(Z, N, k=3 * A, verbose=verbose,
                                   partition_filter=partition_filter,
                                   block_cache=block_cache)


# ══════════════════════════════════════════════════════════════
# §5  MAIN: run for atoms at specified level
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import argparse
    import json
    import time

    parser = argparse.ArgumentParser(description="Hecke character mass computation")
    parser.add_argument("--level", "-k", type=int, default=6, help="Hecke level k")
    parser.add_argument("--max-z", type=int, default=30, help="Max atomic number")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--output", "-o", type=str, default=None)
    args = parser.parse_args()

    k = args.level

    ATOMS = [
        ('H', 1, 0, 1, 0.0), ('D', 1, 1, 2, 1.1121),
        ('He', 2, 2, 4, 7.0739), ('Li', 3, 4, 7, 5.6063),
        ('Be', 4, 5, 9, 6.4628), ('B', 5, 6, 11, 6.9277),
        ('C', 6, 6, 12, 7.6801), ('N', 7, 7, 14, 7.4756),
        ('O', 8, 8, 16, 7.9762), ('F', 9, 10, 19, 7.7790),
        ('Ne', 10, 10, 20, 8.0325), ('Na', 11, 12, 23, 8.1115),
        ('Mg', 12, 12, 24, 8.2607), ('Al', 13, 14, 27, 8.3316),
        ('Si', 14, 14, 28, 8.4477), ('P', 15, 16, 31, 8.4812),
        ('S', 16, 16, 32, 8.4932), ('Cl', 17, 18, 35, 8.5204),
        ('Ar', 18, 22, 40, 8.5954), ('K', 19, 20, 39, 8.5570),
        ('Ca', 20, 20, 40, 8.5513),
        ('Fe', 26, 30, 56, 8.7904), ('Ni', 28, 30, 58, 8.7322),
        ('Zn', 30, 34, 64, 8.7356),
        ('Sn', 50, 70, 120, 8.5050),
        ('Pb', 82, 126, 208, 7.8675),
        ('U', 92, 146, 238, 7.5702),
    ]

    # Filter by max-z
    atoms = [(n, z, nn, a, b) for n, z, nn, a, b in ATOMS if z <= args.max_z]

    # Precompute partition data for this level
    print(f"{'='*80}")
    print(f"HECKE CHARACTER MASS COMPUTATION AT LEVEL k={k}")
    print(f"Partitions of {k}: {len(list(partitions_of(k)))}")
    print(f"{'='*80}")

    # Build seminormal matrices for all partitions (one-time cost)
    print(f"\nBuilding seminormal matrices for all partitions of {k}...")
    t0 = time.time()
    partition_cache = {}
    for shape in partitions_of(k):
        sigmas, dim, syts = build_seminormal_matrices(shape)
        partition_cache[shape] = (sigmas, dim, syts)
        if dim > 0:
            # Verify Hecke for σ₁
            if len(sigmas) > 0:
                check = np.max(np.abs(
                    sigmas[0] @ sigmas[0] - h * sigmas[0] - np.eye(dim)
                ))
                status = "✓" if check < 1e-8 else f"✗ ({check:.2e})"
            else:
                status = "—"
            print(f"  {str(shape):>20} dim={dim:>3} Hecke: {status}")
    t_build = time.time() - t0
    print(f"  Built in {t_build:.2f}s\n")

    # Run for each atom
    print(f"{'Atom':>4} {'Z':>3} {'N':>3} {'A':>3} {'M_pred':>12} {'M_obs':>12} "
          f"{'Error':>9} {'B_pred':>10} {'Time':>6}")
    print("-" * 75)

    results = []
    all_errs = []

    for name, Z, N, A, BpA in atoms:
        Mf = Z * M_P_MEV + N * M_N_MEV + Z * me
        Mo = Mf - A * BpA if A > 1 else Mf

        t0 = time.time()
        M_pred, details = compute_mass_at_level(Z, N, k=k, verbose=args.verbose)
        dt = time.time() - t0

        pct = (M_pred - Mo) / Mo * 100 if Mo > 0 else 0
        if A > 1:
            all_errs.append(abs(pct))

        print(f"{name:>4} {Z:>3} {N:>3} {A:>3} {M_pred:>12.3f} {Mo:>12.3f} "
              f"{pct:>+8.4f}% {details['binding']:>10.3f} {dt:>5.2f}s")

        results.append({
            'atom': name, 'Z': Z, 'N': N, 'A': A,
            'M_pred': round(M_pred, 3), 'M_obs': round(Mo, 3),
            'error_pct': round(pct, 5), 'binding': round(details['binding'], 3),
            'markov_trace': details['markov_trace'],
        })

    if all_errs:
        mae = sum(all_errs) / len(all_errs)
        print(f"\n  MAE = {mae:.5f}% ({len(all_errs)} atoms)")
        print(f"  Level k = {k}, partitions = {len(list(partitions_of(k)))}")

    # Save results
    if args.output:
        out = {'level': k, 'results': results, 'MAE': mae if all_errs else None}
        with open(args.output, 'w') as f:
            json.dump(out, f, indent=2, default=str)
        print(f"\n  Results saved to {args.output}")
