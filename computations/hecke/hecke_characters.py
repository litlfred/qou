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
from mpmath import mp, mpf as _mpf_type, mpc as _mpc_type


class SeminormalPrecisionLoss(ValueError):
    """Raised when `build_seminormal_matrices` is handed an mpmath `q`.

    A REFUSAL, NOT A CRASH. The float64 builder would truncate the argument to
    a double without saying so, which is the defect bean `qou-8xb1` records --
    the caller asked for precision, got a double, and got no signal. Refusing
    turns a silently wrong number into a visible error naming the exact twin,
    `build_seminormal_matrices_mp`.

    Subclasses `ValueError` to match the corpus idiom for a domain guard
    (cf. `habiro_coefficients_atomic.AmDifferenceInvalid`), which AGENTS.md
    cites as the reason a traceback is not by itself evidence of a defect: an
    exception type the corpus defines for exactly this case is the guard
    working, not the producer failing.
    """


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
from qou_substrate.constants import Q as Q0_PROTON  # noqa: E402 — anchor-independent proton pin (qou-6p3b Tranche C)
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

    # DISPATCH ON THE OPERAND (bean qou-8xb1): an mpmath `q` gets exact
    # arithmetic, a float gets the float64 path, and the decision follows the
    # VALUE rather than a flag. Same shape `qou-d8gq` landed for the sibling
    # builder in pyhecke (`dtype=_value_dtype(vals)`), for the same reason.
    #
    # This function used to coerce here (`float(q)`) and was float64 all the
    # way down: it computed the axial-distance entries in float, reached for
    # mp.sqrt and threw the precision away, and returned np.zeros(). An `mpf`
    # handed in came back as a double with NO signal -- measured at shape
    # (3,2,1), dim 16, output was BIT-IDENTICAL to passing the f64 value. An
    # earlier revision of this branch merely raised on that input; refusing is
    # better than lying, but the caller still could not get what it asked for.
    # Now it can.
    #
    # `str`, `Fraction` and plain numerics keep coercing -- the #1861 rationale
    # further down records that callers legitimately pass them, and a string is
    # not a request for precision. Only the mpmath types dispatch, because only
    # for those is the downcast unambiguously wrong.
    if isinstance(q, _mpc_type):
        # Dispatching mpc here would be worse than useless: the exact twin is
        # real-only (`q_local = q if isinstance(q, mp.mpf) else mp.mpf(str(q))`
        # stringifies, and mpf("(1.11 + 0.0j)") dies with an opaque
        # "invalid literal for int()" from inside mpmath). An earlier revision
        # of this branch routed mpc there and produced exactly that traceback.
        #
        # A complex q is a legitimate FIBRE-level object (AGENTS.md separates
        # the fibre, where Im(q) is unconstrained, from the archimedean
        # evaluation, where Im(q_0) = 0). So this is a missing capability, not
        # a forbidden input, and it says so.
        raise SeminormalPrecisionLoss(
            "build_seminormal_matrices() was handed a complex q "
            f"({type(q).__name__}); the exact seminormal builder is real-only, "
            "so there is no exact path to dispatch to. Complex q is a "
            "fibre-level object and supporting it is unimplemented, not "
            "refused. Pass an mpf for the exact real path. Bean qou-8xb1."
        )
    if isinstance(q, _mpf_type):
        if sparse:
            # scipy.sparse rejects dtype=object, so an exact matrix cannot be
            # returned in CSR form. Refusing beats silently handing back a
            # float64 sparse matrix, which is the defect this dispatch exists
            # to remove. (Same boundary AGENTS.md records for su4_1111.)
            raise SeminormalPrecisionLoss(
                "build_seminormal_matrices(sparse=True) cannot carry an "
                f"mpmath q: scipy.sparse has no dtype for {type(q).__name__}. "
                "Pass sparse=False for the exact dense path, or float(q) if "
                "float64 is genuinely what you want. Bean qou-8xb1."
            )
        return build_seminormal_matrices_mp(shape, q)

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


def build_seminormal_matrices_mp(shape, q):
    """Exact-arithmetic twin of `build_seminormal_matrices` (mpmath, no float64).

    WHY THIS EXISTS
    ---------------
    `build_seminormal_matrices` above computes in float64: it coerces its
    argument, computes the axial-distance entries in float, reaches for
    `mp.sqrt` and throws the precision away (`b = float(mp.sqrt(...))`), and
    returns `np.zeros((dim, dim))`, i.e. float64 storage.

    UPDATED 2026-08-25 (bean qou-8xb1): it no longer SILENTLY downcasts an
    `mpf` -- it dispatches here instead, so a caller asking for exact
    arithmetic now gets it through the ordinary entry point. This function
    remains the implementation and the explicit way to ask.

    Its float64 path is still the DEFAULT (`q=None`, and the ~64 callers that
    pass a float), and deliberately so. Flipping the default would be a false
    fix, measured: numpy silently re-truncates `mp.matrix` back to float64 in
    most operations --

        np.trace(sigma)             -> float64
        np.abs(sigma)**2            -> float64
        np.eye(d) @ sigma           -> float64
        np.sum(np.abs(sigma)**2)    -> float64
        sigma @ sigma (mpmath's @)  -> mpf, preserved

    -- so callers handed exact matrices would go on producing float64 results
    while LOOKING exact, which is strictly worse than the honest float64 they
    get now. That last one matters: `np.sum(np.abs(M)**2)` is exactly what the
    deuteron probe's `fro2` computed. Exactness has to be carried by the
    consumer, not merely handed to it, which is why opting in per-consumer is
    the right shape.

    That makes it a library-level float64 entry point, which is why draining a
    probe that calls it is not a probe-local fix. Per AGENTS.md ("a float64
    input poisons the whole result") the honest options are an exact route or
    an unanswered question — so this is the exact route, added ALONGSIDE rather
    than in place of the float64 builder. Nothing above is modified and no
    existing caller changes behaviour; drains of the other 63 can adopt this
    incrementally.

    THE q -> 1 LIMIT IS EXACT HERE, NOT A FINITE DIFFERENCE
    -------------------------------------------------------
    Callers wanting the classical (q = 1) rep have been passing `q = 1 + 1e-7`,
    because `a = h/(1 - q^-2rho)` is 0/0 at q = 1. In float64 that ratio is
    formed from two quantities of size ~1e-7 each carrying ~1e-16 of absolute
    error, so it retains only ~9 significant digits.

    The limit is elementary and needs no epsilon. With q = 1 + eps:
    h = q - 1/q ~ 2*eps and 1 - q^(-2*rho) ~ 2*rho*eps, so

        a -> 1/rho,   a' -> -1/rho,   b^2 = a*a' + 1 -> 1 - 1/rho^2,

    which is exactly Young's classical seminormal form. `q=1` is therefore
    handled as its own branch and is exact, not approached.

    Returns (sigmas, dim, syts) with sigmas a list of `mp.matrix`, matching the
    float64 builder's shape and index conventions exactly.
    """
    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], dim, syts

    q_local = q if isinstance(q, mp.mpf) else mp.mpf(str(q))
    exact_one = (q_local == 1)
    h_local = None if exact_one else q_local - 1 / q_local

    syt_index = {tuple(sorted(t.items())): idx for idx, t in enumerate(syts)}
    sigmas = []

    for k in range(1, n):
        M = mp.zeros(dim, dim)
        processed = set()

        for i in range(dim):
            if i in processed:
                continue

            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]

            if exact_one:
                a = mp.mpf(1) / rho
                a_prime = -a
            else:
                a = h_local / (1 - q_local ** (-2 * rho))
                a_prime = h_local / (1 - q_local ** (2 * rho))

            swap_map = dict(syts[i])
            swap_map[k] = ci_k1
            swap_map[k + 1] = ci_k

            j = syt_index.get(tuple(sorted(swap_map.items())))
            if j == i:
                j = None

            if j is None:
                M[i, i] = a
                processed.add(i)
            else:
                b = mp.sqrt(abs(a * a_prime + 1))
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = b
                M[j, i] = b
                processed.add(i)
                processed.add(j)

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
      - "symbolic" / "symbolic_q"                → exact symbolic in q

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
            "symbolic" / "symbolic_q"    → EXACT symbolic in q (sympy)
        return_precision: if True, return `(value, precision_tag)`;
            if False (default), return value only.

    Defaults to `f64` for backward compatibility — but downstream code
    that records witnesses MUST pass `precision="mpfr_50dps"` (or
    higher) to satisfy the "no approximations" directive, OR record
    the returned `precision` tag in the witness JSON.

    Returns the character.  For `f64`: returns `float`. For `mpfr_*`:
    returns a string of the decimal expansion (caller may parse via
    `mpmath.mpf`).  For `symbolic_q`: a **sympy expression** in
    `hecke_characters_symbolic.q` — a rational function, not a number and not
    a string, so substituting a value stays the caller's explicit decision.
    Passing `q_value` alongside `precision='symbolic_q'` is an error rather
    than being silently ignored.

    `word` accepts both shapes in use in this repo: the signed
    `[(sign, gen_1based), ...]` above, and — on the symbolic path only, for
    now — the typed `[(c, d, gen_0based)]` form of `chi_all_lambda`, in which
    a crossing is the algebra element `c*sigma_g + d`.
    """
    tag, dps = _parse_precision(precision)

    # The symbolic branch is handled BEFORE `q_value` is defaulted, because
    # "the caller passed no q" and "the caller passed q0" mean different things
    # here and the default would erase the distinction.
    if tag == PRECISION_SYMBOLIC_Q:
        if q_value is not None:
            raise ValueError(
                "precision='symbolic_q' evaluates in a free symbol q, so a "
                "q_value has nothing to bind to. Substitute yourself — "
                "`chi_lambda_braid(shape, word, precision='symbolic_q')"
                ".subs(hecke_characters_symbolic.q, <value>)` — so the "
                "precision loss happens where you can see it, or ask for "
                "precision='mpfr_50dps' to get a number directly."
            )
        from hecke_characters_symbolic import chi_lambda_braid_symbolic
        value = chi_lambda_braid_symbolic(shape, word)
        return (value, PRECISION_SYMBOLIC_Q) if return_precision else value

    if q_value is None:
        q_value = float(q0)

    # Normalize word.
    word_marshalled = [
        (1 if (s == '+' or s == 1 or s is True) else -1, int(g))
        for s, g in word
    ]

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


# Canonical p-n interface offset, bound once at this module's q0. Imported
# rather than open-coded so there is a single definition of the convention
# across pyhecke (Layer 2b) and computations (Layer 3); the import is
# deliberately hard, because a fallback to -h/2 would silently compute the
# colour-blind convention while reporting success.
from pyhecke.constants import (  # noqa: E402
    PN_CONVENTION as _PN_CONVENTION,
    pn_interface_offset as _pn_interface_offset,
)

D_PN = _pn_interface_offset(q0)


def crossing_coeffs(ti, tj):
    """Crossing (c, d) for nucleon types: 1=proton, 0=neutron.

    The mixed (p-n) branch carries the COLOUR-WEIGHTED offset `D_PN`, not
    `-h/2`. `-h/2` is `strict_averaged`, which is the bar-symmetriser of z
    and is colour-BLIND: it averages the two flavours 50/50 and so cannot
    see the substrate flavour split. Canonical per the owner ruling of
    2026-08-15 (R3), reaffirmed 2026-08-26.

    This is the INTER-nucleon crossing only. The INTRA-nucleon quark-level
    averaged crossings elsewhere in this module keep `sigma - (h/2)*1`;
    nothing here establishes what convention a u-d crossing should carry.
    """
    if ti == 1 and tj == 1:
        return 1.0, 0.0       # pp: σ
    elif ti == 0 and tj == 0:
        return 1.0, -h        # nn: σ⁻¹
    else:
        return 1.0, D_PN      # pn: mixed, colour-weighted


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
    # Association order MIRRORS the module-level `q_int`, which is
    # `(Q**n - Q_INV**n) / HA` over PRECOMPUTED reciprocal and h. Computing
    # `q**(-k)` and `q - 1/q` inline instead is the same mathematics but a
    # different float64 rounding path: measured, it moved `binding_3A` by
    # 1.7e-16 to 3.2e-16 relative — 1 to 1.5 ULP. That is the floor of the
    # arithmetic and not a semantic change, but a witness diff cannot tell the
    # difference, so threading a q would have shown up as "fields moved" across
    # the whole migration. Binding the reciprocal once makes the explicit path
    # bit-identical to the default when `q` IS the module q. Bean qou-6p3b.
    qi = 1 / q
    h = q - qi
    return (q ** k - qi ** k) / h


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
        return qfac(n, Q0_PROTON) / math.prod(q_int(hk) for hk in young_hooks(shape))
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


def hook_length_dim_lambda(shape):
    """Exact integer Specht-module dimension `f^λ = n! / ∏ hook(c)` via the
    hook-length formula (`specht_dim(shape)`). Provided under both names so
    callers importing `hook_length_dim_lambda` or `specht_dim` resolve identically
    (bean qou-2cz1)."""
    return specht_dim(shape)


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
