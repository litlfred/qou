# NOT archimedean_by_design. This file used to carry that marker, reading
#   "the LP/SDP solve and the Gram matrix assembly are float64 by necessity
#   (scipy.optimize.linprog + numpy.linalg)". The necessity was real when it
#   was written and is now gone: the Gram/supply assembly runs in mpmath via
#   `hoefsmit_mpmath` (#5264), the solve goes to the Clarabel-MPFR backend
#   over decimal strings, and deliverable B's eigensolve is `mp.eig`. numpy
#   is no longer imported at all. The marker is an agent-facing convention
#   with no script reading it, so a stale one is pure misdirection — it would
#   have gone on excusing float64 here long after the reason expired.
#   Bean qou-q7f1; owner directive "no f64 path".
"""Wedderburn pair-volume LP/SDP wiring for the EW-sector + alt-Δ_I
Weinberg-angle probe.

Two deliverables in one witness:

(A) WIRE  wedderburn_pair_volumes into prop:knot-operator-lp-selection.
    Concrete numerical instance: solve the LP/SDP-dual program for the
    EW-sector operator selection with Wedderburn pair amplitudes
    |V̂_i V̂_j|_Wedd as the supply matrix.  Report primal_obj, dual_obj,
    y_0_star, y_star, active_set per AGENTS.md "LP/SDP duals —
    first-class infra" mandate.

(B) TRY  to close the 2.19% Weinberg gap by extending the Δ_I word
    space.  The (3,2,1) max+/2nd-max+ = 1.78 reading on
    Δ_I^minimal = σ_2 σ_4 σ_2 was 2.19% off CODATA cot θ_W = 1.823.
    Test ~10 alternative Δ_I words and report the best ratio +
    associated structural signature.

Witness output: wedderburn-lp-ew-wiring.witness.json (with LP duals
to satisfy lp_dual_witness_validator).
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from functools import lru_cache
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
import mpmath as mp  # noqa: E402
from _precision import COMPUTE_DPS, fmt  # noqa: E402

#: Working precision for the whole pipeline: the package's COMPUTE_DPS.
#:
#: WAS a hardcoded 50, reasoning that 50 dps "matches the substrate constant
#: `Q_50_DIGIT_STR`". That is true of the INPUT and wrong about the output:
#: `_precision` serializes at OUTPUT_DPS = 60 with 10 guard digits, so a
#: 50-dps computation wrote 10 unbacked digits into every value in the
#: witness. Harmless to any consumer reading 50 digits, but it is precisely
#: the tail that made the sparse rewrite below look like it changed answers —
#: reassociating a sum moves the first unbacked digit, and there were ten of
#: them on display.
#:
#: Computing at COMPUTE_DPS (70) backs every serialized digit. It was not a
#: realistic option while the producer took 46 min; the sparse assembly makes
#: it free (21 s), which is the useful kind of thing a speed-up buys.
_MP_DPS = COMPUTE_DPS


def _as_strings(x):
    """mpf scalar / vector / matrix -> full-precision decimal string(s).

    The marshalling format the MPFR solver accepts, and the only one that
    reaches it without an f64 hop: `repr(float(v))` would put the truncation
    back exactly where the port removed it.
    """
    if isinstance(x, list):
        return [_as_strings(v) for v in x]
    return mp.nstr(x, _MP_DPS)


def _mpf_or(v, default):
    """Decimal string / number -> mpf, with a default when absent.

    The serialization port turned several witness fields into decimal strings
    to keep them out of float64, and every downstream COMPARISON on them has
    to move with the type. Two did not, and the first was found the expensive
    way: `r.get("duality_gap", float("inf")) < 1e-6` raised TypeError after
    the entire H_9 compute had already finished.
    """
    if v is None:
        return default
    return mp.mpf(str(v))


def _nonzeros(M, dim: int) -> dict:
    """``{(i, j): value}`` for the nonzero entries of an ``mp.matrix``.

    mpmath already stores a matrix as a dict of its nonzeros, so the fast path
    reads that directly. It is a name-mangled private attribute, hence the
    O(dim^2) fallback: if a future mpmath renames it the result stays correct
    and only the speed regresses, which is the right way round for a private
    attribute this useful.
    """
    data = getattr(M, "_matrix__data", None)
    if data is None:
        return {(i, j): M[i, j] for i in range(dim) for j in range(dim)
                if M[i, j] != 0}
    return {k: v for k, v in data.items() if v != 0}


def _sparse_product(A_nz: dict, B_nz: dict) -> dict:
    """Nonzeros of ``A.B`` from the nonzeros of A and B.

    The pair matrices ``M_k = sigma_i . sigma_j`` were built with mpmath's
    ``*``, which is a DENSE O(dim^3) matmul — 840 of them per atom (30
    partitions x 28 pairs), at dim up to 216. Sparse contraction of the outer
    trace alone therefore fixed the smaller half: the products are ~420M mpf
    operations against the traces' ~147M.

    At 1.13% density the product costs ``sum_j nnz(A[:,j]) * nnz(B[j,:])``
    instead of dim^3. Same construction as the trace: seminormal form is
    sparse, and nothing here is an approximation — the arithmetic is
    identical, only the zeros are skipped.
    """
    brow: dict = {}
    for (j, k), v in B_nz.items():
        brow.setdefault(j, []).append((k, v))
    out: dict = {}
    for (i, j), a in A_nz.items():
        row = brow.get(j)
        if not row:
            continue
        for k, b in row:
            key = (i, k)
            prev = out.get(key)
            out[key] = a * b if prev is None else prev + a * b
    return {k: v for k, v in out.items() if v != 0}


def _mp_trace_of_product(A, B, dim: int):
    """tr(A.B) as ``sum_ij A[i,j]*B[j,i]`` -- O(dim^2), never forming A.B.

    The diagonal of a matrix product needs only the row-column contraction, so
    building the full product to take its trace does dim^3 work for a dim^2
    answer. In numpy that waste was invisible; in mpmath it is the difference
    between a session and a day. Measured over the partitions of 9, with 28
    pairs and 406 pair-pair traces:

        forming the products : 434 * sum(dim^3) = 2.59e10 mpf ops
        contracting instead  :  28 * sum(dim^3) + 406 * sum(dim^2) = 1.82e9
                               (sum(dim^2) over partitions of n is n! = 362880)

    a 14.2x reduction. The 28 pair matrices M_k = sigma_i.sigma_j are still
    formed, because G contracts them against each other; only the outer trace
    is contracted rather than multiplied.

    SPARSE. The two bounds above are both O(dim^2) in the contraction, and
    that is 128x more work than the matrices contain. Measured over the
    partitions of 9: the Hoefsmit generator matrices are 1.13% dense (1.56
    nonzeros per ROW), and a pair product sigma_i.sigma_j is 0.78% dense --
    366 nonzeros in the 216x216 block, against 46656 index pairs the dense
    loop walks. Seminormal form is sparse by construction; nothing here
    needed to be discovered, only used.

    So iterate the nonzeros instead. tr(A.B) = tr(B.A), so it is valid to
    walk whichever side has fewer.

    Accepts an ``mp.matrix`` or an already-extracted ``{(i, j): value}``
    dict, which lets `_full_wedderburn_gram` extract each pair matrix ONCE
    and reuse it across every pair-pair combination rather than per trace.
    """
    a = A if isinstance(A, dict) else _nonzeros(A, dim)
    b = B if isinstance(B, dict) else _nonzeros(B, dim)
    if len(b) < len(a):
        a, b = b, a          # tr(A.B) = tr(B.A)
    acc = mp.mpf(0)
    for (i, j), v in a.items():
        w = b.get((j, i))
        if w is not None:
            acc += v * w
    return acc


def _mp_trace(M, dim: int):
    """tr(M) for an ``mp.matrix``, staying in mpf.

    `mp.matrix` has no `.trace()`; summing the diagonal explicitly keeps the
    value an `mpf`. Do NOT reach for `float(np.trace(...))` here — that was the
    old path, and it discarded 34 of the 50 digits the inputs carry.
    """
    acc = mp.mpf(0)
    for i in range(dim):
        acc += M[i, i]
    return acc
from wedderburn_pair_volumes import wedderburn_pair_volumes  # noqa: E402
from hecke_character_symbolic import _hoefsmit_build  # noqa: E402
from lp_dual_solver import (  # noqa: E402
    PROVENANCE_STR_FIELDS,
    provenance,
    solve_operator_selection_lp,
)
from partition_utils import hook_lengths  # noqa: E402


@lru_cache(maxsize=None)
def _hoefsmit_mp_matrices(n: int, q_str: str) -> dict:
    """Hoefsmit generator matrices ``M^λ_g`` in **mpmath**, for every
    partition ``λ ⊢ n`` and every generator ``g ∈ {0, …, n-2}``.

    Returns ``{λ: {"matrices": [M_0, M_1, …], "y": y_λ(q_0), "dim": d}}``
    with each ``M_g`` an ``mp.matrix`` and ``y_λ`` an ``mpf``.

    PORTED FROM FLOAT64 (owner directive "no f64 path", bean qou-q7f1). The
    previous version took ``q0_value: float`` — the 50-dps substrate constant
    truncated to f64 at the door — built ``np.float64`` matrices, and returned
    an f64 ``y_λ``. Everything downstream inherited that, so the LP saw 16
    digits no matter what the witness said. The construction now runs end to
    end in mpmath via ``hoefsmit_mpmath`` (landed on main in #5264), whose
    docstring records why a shortcut is not available: the numpy fast path is
    float64 *by construction* — ``BlockCache`` uses ``math.sqrt`` against a
    fixed ``1e-15`` degeneracy threshold — so handing it an ``mpf`` q does not
    make it exact; numpy coerces on contact.

    MEMOISED on ``(n, q_str)``. The sweep called this again for the
    headline atom with identical arguments — triton is both the headline
    and a sweep entry — so the H_9 build ran twice. The existing
    ``hoefsmit_cache=`` parameter reuses a cache WITHIN one atom (supply
    vector + Gram); it does nothing ACROSS the headline/sweep boundary,
    which is where the duplication was. Pure function of its arguments,
    and callers only read traces, so nothing mutates the cached matrices.

    MEASURED IN ISOLATION: the H_9 build is 2.77 s cold, 0.003 ms memoised.
    So this saves ~2.8 s. Keep it — it is free and correct — but it is not
    a performance fix.

    TWO WRONG CLAIMS PRECEDED THAT NUMBER, both mine, and the second is the
    instructive one. First I said the duplicated build "dominated the wall
    clock: 28 min becomes ~14", inferred from which step the progress line
    narrates. Then I "corrected" that to "55.7 min -> 46.3 min, saving 9.4
    min (17%)" from a before/after of two full runs — but those ran with
    different background load (I had crosschecks and audits going during
    the first), so 9.4 min of it was noise and ~3 s was the change. A
    before/after wall-clock comparison is not a measurement unless the load
    is controlled; timing the function directly is.

    WHERE THE TIME ACTUALLY GOES, per atom at n=9 (one process, so the
    ratio holds even if absolute numbers carry load):

        build   2.9 s     supply  19.9 s     gram  1390.9 s  (98.4%)

    i.e. 406 pair-pair traces at 3.43 s each. That is the only thing worth
    optimising here, and `_mp_trace_of_product` below now does it sparsely.

    The caller then evaluates Markov traces of arbitrary 4-letter
    words via three matrix multiplications + one trace + sum over
    ``λ`` — orders of magnitude faster than the per-word
    ``tr_M_via_wenzl_bridge_mpfr`` mpfr assembly when many words
    share the same ``n``.
    """
    from hecke_character_symbolic import partitions_of  # noqa: E402
    from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402

    # y_λ(q) = (q − q⁻¹)^(n − ℓ(λ)) · ∏_{x ∈ λ} [h_x(λ)]_q⁻¹
    # (canonical Plancherel weight on the Hecke algebra at q), in mpf.
    with mp.workdps(_MP_DPS):
        q = mp.mpf(q_str)
        qi = 1 / q

        def q_int(k: int):
            if k == 0:
                return mp.mpf(0)
            return (q ** k - qi ** k) / (q - qi)

        cache = BlockCacheMP(q)
        out = {}
        for shape in partitions_of(n):
            mats, dim, _ = seminormal_matrices_mp(list(shape), cache=cache)
            if dim == 0:
                continue
            ell = len(shape)
            prefactor = (q - qi) ** (n - ell)
            denom = mp.mpf(1)
            for h in hook_lengths(shape):
                denom *= q_int(h)
            out[tuple(shape)] = {"matrices": mats,
                                 "y": +(prefactor / denom),
                                 "dim": dim}
        return out


def _klr_positive_supply_vector(
    pairs: list,
    n_strands: int,
    q_str: str,
    *,
    hoefsmit_cache: dict | None = None,
) -> list:
    """KLR-positive supply vector ``t_k = tr_M(σ_i σ_j)`` per pair.

    Replaces the signed `pair["full"]` matrix-entry sum used on PR
    #618 with the genuine pair Markov trace
    ``Σ_λ y_λ(q) · χ_λ(σ_i σ_j)`` evaluated in H_(3·A).  By KLR
    positivity (operators in the canonical-basis cone are non-
    negative at q > 0; cf. Kashiwara-Saito, Brundan-Kleshchev), this
    vector is non-negative for every pair and the LP
    ``min ⟨t, x⟩ s.t. Σx = n_target, Gx ≥ 0, x ≥ -M`` is bounded
    for every atom.

    Re-uses the same Hoefsmit cache as ``_full_wedderburn_gram`` to
    avoid recomputing per-partition matrices.

    Parameters
    ----------
    pairs
        Pair list (only ``i`` / ``j`` indices consumed).
    n_strands
        Hecke algebra rank ``n = 3·A``.
    q_str
        ``q_0`` as 50-dps decimal string.
    hoefsmit_cache
        Optional precomputed cache from ``_hoefsmit_f64_matrices``;
        built on demand if ``None``.

    Returns
    -------
    list[mpmath.mpf]
        Real ``(n_pairs,)`` vector of pair Markov traces.
    """
    if hoefsmit_cache is None:
        hoefsmit_cache = _hoefsmit_mp_matrices(n_strands, q_str)
    with mp.workdps(_MP_DPS):
        t = []
        for p in pairs:
            i, j = p["i"], p["j"]
            acc = mp.mpf(0)
            for shape, info in hoefsmit_cache.items():
                mats = info["matrices"]
                # tr(sigma_i . sigma_j) without forming the product
                acc += info["y"] * _mp_trace_of_product(
                    mats[i], mats[j], info["dim"])
            t.append(+acc)
        return t


def _full_wedderburn_gram(
    pairs: list,
    n_strands: int,
    q_str: str,
    *,
    eps: float = 1e-9,
    hoefsmit_cache: dict | None = None,
):
    """Full H_n Wedderburn Frobenius Gram on the pair-operator algebra.

    For each pair ``(i, j)`` of generators in the atom braid, treat
    the Hecke element ``σ_i · σ_j ∈ H_n(q)`` as the basis vector for
    that pair.  The Frobenius inner product on H_n via the Markov
    trace is::

        G_{(i,j),(i',j')}
            = ⟨σ_i σ_j, σ_{i'} σ_{j'}⟩_{tr_M}
            = Σ_λ⊢n  y_λ(q) · χ_λ(σ_i σ_j σ_{i'} σ_{j'})

    where ``y_λ`` are the canonical Plancherel weights on H_n(q) and
    ``χ_λ`` is the Hoefsmit character on the Wedderburn block ``λ``.

    This is the genuine off-diagonal Wedderburn coupling — no
    diagonal-only proxy, no rank-3 H_3-channel projection — and is
    full-rank generically (modulo bar-involution kernel).

    Implementation: pre-computes f64 Hoefsmit generator matrices once
    per partition, then evaluates each pair-pair Markov trace as a
    chain of three matrix multiplications + trace summed over ``λ``.
    Symmetric in ``(k, k')`` by cyclicity of the trace, so only the
    upper triangle is computed.  Caller may pass an externally-built
    ``hoefsmit_cache`` to share work across atoms with the same
    ``n_strands``.

    Parameters
    ----------
    pairs
        Pair-amplitude list from ``wedderburn_pair_volumes`` (only
        the ``i`` and ``j`` indices are consumed).
    n_strands
        Hecke algebra rank ``n = 3·A`` for the atom.
    q_str
        ``q_0`` as a 50-dps decimal string (used to reconstruct an
        f64 working value for the Hoefsmit matrices).
    eps
        Tikhonov regularisation added to the diagonal so
        ``solve_operator_selection_lp`` sees a strictly PSD matrix.
    hoefsmit_cache
        Optional precomputed cache from ``_hoefsmit_f64_matrices``.
        If ``None``, built on demand.

    Returns
    -------
    list[list[mpmath.mpf]]
        Real ``(n_pairs, n_pairs)`` Gram matrix.
    """
    n_pairs = len(pairs)
    if hoefsmit_cache is None:
        hoefsmit_cache = _hoefsmit_mp_matrices(n_strands, q_str)

    # Pre-compute the σ_i σ_j matrix per pair per partition.  This
    # turns the pair-pair Markov trace into a single matrix product
    # + trace per λ (factor-of-2 speed-up over recomputing).
    with mp.workdps(_MP_DPS):
        pair_mats_per_lambda: dict[tuple, list] = {}
        for shape, info in hoefsmit_cache.items():
            mats = info["matrices"]
            # Extract the nonzeros once per (lambda, pair). The dense loop
            # this replaces re-walked dim^2 index pairs for every one of the
            # n_pairs*(n_pairs+1)/2 combinations; there are only n_pairs
            # matrices to extract.
            # Sparse throughout: extract each GENERATOR's nonzeros once, then
            # build every pair product sparsely. The dense `mats[i] * mats[j]`
            # this replaces was O(dim^3) and ran 840 times per atom.
            gen_nz = [_nonzeros(M, info["dim"]) for M in mats]
            pair_mats_per_lambda[shape] = [
                _sparse_product(gen_nz[p["i"]], gen_nz[p["j"]]) for p in pairs
            ]

        G = [[mp.mpf(0)] * n_pairs for _ in range(n_pairs)]
        eps_mp = mp.mpf(eps)
        for k in range(n_pairs):
            for kp in range(k, n_pairs):
                val = mp.mpf(0)
                for shape, info in hoefsmit_cache.items():
                    # χ_λ(σ_i σ_j σ_{i'} σ_{j'}) = tr(M_ij^λ · M_i'j'^λ)
                    val += info["y"] * _mp_trace_of_product(
                        pair_mats_per_lambda[shape][k],
                        pair_mats_per_lambda[shape][kp], info["dim"])
                G[k][kp] = +val
                G[kp][k] = +val
        for k in range(n_pairs):
            G[k][k] = +(G[k][k] + eps_mp)
        return G


def beta_ew_word(delta_I):
    """β_EW(Δ_I) = σ_1^4 · Δ_I · σ_3^6 · Δ_I · σ_5^8 · Δ_I."""
    return [0]*4 + delta_I + [2]*6 + delta_I + [4]*8 + delta_I


def beta_matrix_at_q0(shape, q_str, word):
    """Build β_EW matrix on V_λ at q_0, in **mpmath** at 50 dps.

    PORTED FROM FLOAT64 (owner directive "no f64 path", bean qou-q7f1).
    The previous version elaborated the Hoefsmit generators to
    ``np.complex128`` "once up front" and multiplied in numpy, then fed
    ``np.linalg.eigvals``. That truncated the 50-dps substrate constant at
    the first ``np.array(...)`` call, so every ``ratio`` and ``rel_err``
    this probe reported carried 16 digits regardless of what the witness
    claimed — the last 31 raw float64 fields in the witness were all
    downstream of this one line.

    "It is only a percent-level probe" is not an exemption (AGENTS.md
    §PROBES ARE NOT EXEMPT): a probe conclusion is an *argument* that gets
    written into a bean and a PR body, where nothing re-derives it.

    The mpmath-native ``seminormal_matrices_mp`` (main #5264) replaces the
    sympy ``_hoefsmit_build`` + numpy round trip (this file's last caller of
    either), so no coercion point
    remains. Measured cost on V_(3,2,1) (dim 16, 27-letter word): the
    eigensolve is ~1 s per candidate, 14 candidates — the numpy path was
    never the bottleneck this docstring claimed it was.
    """
    from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402

    with mp.workdps(_MP_DPS):
        matrices, dim, _ = seminormal_matrices_mp(
            list(shape), cache=BlockCacheMP(mp.mpf(q_str)))
        if dim == 0:
            return None, 0
        M = mp.eye(dim)
        for gen_idx in word:
            M = M * matrices[gen_idx]
        return M, dim


def compute_321_max_plus_ratio(q_str, delta_I):
    """For β_EW(Δ_I) on V_(3,2,1), return max+/2nd-max+ eigenvalue ratio.

    Real parts of the spectrum, as before — the Hoefsmit seminormal form is
    real at real q, so ``mp.eig`` returns a numerically-real spectrum and
    ``.real`` discards only the residual imaginary part.
    """
    word = beta_ew_word(delta_I)
    M, dim = beta_matrix_at_q0((3, 2, 1), q_str, word)
    if M is None:
        return None, []
    with mp.workdps(_MP_DPS):
        eigs = [mp.mpmathify(e).real for e in mp.eig(M, left=False,
                                                     right=False)]
        pos = sorted(e for e in eigs if e > 0)
        if len(pos) < 2:
            return None, eigs
        return +(pos[-1] / pos[-2]), eigs


def main() -> int:
    # Recorded as a witness parameter only — every compute path below takes
    # the 50-dps STRING directly, so nothing elaborates through sympy.
    q_0 = sp.Float(Q_50_DIGIT_STR, 50)
    print(f"Wedderburn LP/SDP-EW wiring + alt-Δ_I Weinberg probe")
    print(f"  q_0 ≈ {mp.nstr(mp.mpf(Q_50_DIGIT_STR), 12)}")
    print()

    # ── (A) LP/SDP wiring with Wedderburn pair volumes ──────────
    print("=" * 72)
    print("(A) LP/SDP-dual program for EW-sector operator selection")
    print("=" * 72)
    # Test multiple atoms to exercise the LP at varying #pair counts.
    # Maximum strand count (n=3·A) we attempt the *full* Wedderburn
    # Gram for in this script; atoms beyond this skip with a clearly-
    # labelled `deferred_compute_budget` status (the math is well-
    # defined, but the sympy-based `_hoefsmit_build` precomputation
    # for p(12)=77 partitions × 11 generators at H_12 dim ≤ 462
    # exceeds reasonable session budget without the optional Rust
    # mpfr kernel `pyhecke_native`).  See audit doc § "Compute
    # budget for headline atom" for the open-frontier follow-up.
    MAX_FULL_GRAM_N = 9
    lp_results_per_atom = []
    atoms_to_test = [
        ("proton",   1, 0),
        ("neutron",  0, 1),
        ("deuteron", 1, 1),
        ("triton",   1, 2),
        ("helium-4", 2, 2),
    ]
    # Choose the heaviest *computable* atom as the headline (so the
    # primary LP solve in this run produces concrete numbers rather
    # than a `deferred` placeholder).
    headline_idx = max(
        (i for i, (_, Za, Na) in enumerate(atoms_to_test)
         if 3 * (Za + Na) <= MAX_FULL_GRAM_N),
        default=0,
    )
    Z, N = atoms_to_test[headline_idx][1], atoms_to_test[headline_idx][2]
    pairs = wedderburn_pair_volumes(Z, N, include_inter=True,
                                    crossings_per_pair=1)
    print(f"  Headline atom: {atoms_to_test[headline_idx][0]} (Z={Z}, N={N})")
    print(f"  # pair amplitudes: {len(pairs)}")

    # Build the LP for operator selection per `solve_operator_selection_lp`:
    #   primal:  min ⟨t, x⟩
    #            s.t.  Σ x_i = n_target          (net constraint)
    #                  G x ≥ 0                    (Frobenius-positivity)
    #                  x_i ≥ -M                   (large-M lower bound)
    #
    #   dual:    max  n_target · y_0 - M · Σ z_i
    #            s.t.  G^T y + z = t,  y ≥ 0,  z ≥ 0
    #            (y_0_star = shadow price of net constraint;
    #             y_star    = shadow prices of Frobenius positivity rows;
    #             active_set = indices i with y_star[i] > tol — the
    #                          *saturated* positivity constraints, i.e.
    #                          channels where the primal x_k is at the
    #                          boundary and the dual is binding.)
    #
    # For the EW-sector wiring: each basis element b_k corresponds to
    # the Hecke element σ_i σ_j ∈ H_(3·A)(q) for pair (i, j).  We use:
    #   t_k = tr_M(σ_i σ_j) = Σ_λ y_λ · χ_λ(σ_i σ_j)
    #         (KLR-positive pair Markov trace; non-negative for every
    #          pair by KLR positivity on the canonical-basis cone —
    #          replaces PR #618's signed pair["full"] matrix-entry
    #          sum, which was a setup error.  See audit doc §0.)
    #   G_{kk'} = tr_M(σ_i σ_j σ_{i'} σ_{j'})
    #           = Σ_λ y_λ · χ_λ(σ_i σ_j σ_{i'} σ_{j'})
    #         (full Wedderburn Frobenius Gram on the pair-operator
    #          algebra; see `_full_wedderburn_gram`).
    n_pairs = len(pairs)
    n_strands_headline = 3 * (Z + N)
    print(f"  Pre-computing H_{n_strands_headline} Hoefsmit matrices for "
          f"{n_pairs} pairs ({n_pairs} pair Markov traces + "
          f"{n_pairs * (n_pairs + 1) // 2} unique pair-pair traces; "
          f"shared Hoefsmit cache)...")
    # No `float(...)` of the substrate constant. It used to be truncated to
    # f64 here and at two more sites; the 50-dps string now goes straight in.
    hoefsmit_cache_h = _hoefsmit_mp_matrices(n_strands_headline,
                                             Q_50_DIGIT_STR)
    t = _klr_positive_supply_vector(
        pairs, n_strands_headline, Q_50_DIGIT_STR,
        hoefsmit_cache=hoefsmit_cache_h,
    )
    # Sanity check: KLR positivity says t ≥ 0.  Tiny negative
    # numerical noise is tolerated; a substantive negative entry is
    # a bug or a non-canonical-basis pair (would need separate
    # investigation).
    if min(t) < mp.mpf("-1e-9"):
        print(f"  WARN: KLR positivity violation — min(t) = {mp.nstr(min(t), 4)}")
    # Keep the legacy signed matrix-entry sum for diff/comparison — in mpf.
    # The sweep's copy of this line was ported and the headline's was not,
    # which is its own small lesson: a duplicated expression only gets half
    # ported when you fix the one the traceback names.
    with mp.workdps(_MP_DPS):
        t_legacy_matrix_entries = [mp.mpf(str(p["full"])) for p in pairs]
    G = _full_wedderburn_gram(
        pairs, n_strands_headline, Q_50_DIGIT_STR,
        hoefsmit_cache=hoefsmit_cache_h,
    )
    # Total target: half the sum of available KLR-positive amplitudes
    # (loose constraint to ensure feasibility).
    with mp.workdps(_MP_DPS):
        n_target = +(mp.fsum(t) / 2)
    print(f"  t (KLR pair Markov traces, top 3): "
          f"{[mp.nstr(v, 12) for v in t[:3]]}")
    print(f"  t.min = {mp.nstr(min(t), 6)}, t.max = {mp.nstr(max(t), 6)}")
    print(f"  legacy(matrix-entry) t.min = "
          f"{mp.nstr(min(t_legacy_matrix_entries), 6)}, "
          f"t.max = {mp.nstr(max(t_legacy_matrix_entries), 6)}")
    print(f"  G shape: ({len(G)}, {len(G[0])}), "
          f"n_target = {mp.nstr(n_target, 12)}")
    # M_bound=0 enforces x ≥ 0 (operator coefficients are non-negative,
    # the natural interpretation of "operator selection" in
    # prop:knot-operator-lp-selection).  With KLR-positive t and x ≥ 0
    # the LP is bounded for every atom and strong duality holds; the
    # default M_bound=1e6 in `solve_operator_selection_lp` is intended
    # for problems with signed coefficients (not this case).
    # CLARABEL-MPFR, not scipy. The pin used to read "Pin scipy:
    # committed-witness producer -> byte-deterministic", and determinism is a
    # real requirement — but scipy/HiGHS is float64, so pinning it truncated
    # the 50-dps Gram at the solver door and made the mpmath port above
    # pointless. The MPFR backend is equally deterministic and takes decimal
    # STRINGS, so nothing crosses as f64. Its equivalence to scipy is
    # cross-checked in clarabel_lp_crosscheck.py (13/13, worst 2.00e-12), and
    # the solve certifies itself oracle-free in
    # lp_dual_kkt_residual_50dps.py. Bean qou-q7f1.
    res = solve_operator_selection_lp(
        _as_strings(t), _as_strings(G), mp.nstr(n_target, _MP_DPS),
        M_bound="0", backend="clarabel")
    res_dict = res.to_dict()

    # Also run LP for each atom in atoms_to_test (sweep)
    for atom_name, Za, Na in atoms_to_test:
        n_strands_a = 3 * (Za + Na)
        if n_strands_a > MAX_FULL_GRAM_N:
            # Skip with explicit deferred status — math is well-defined
            # but Hoefsmit precomputation at H_n exceeds session budget
            # without the Rust mpfr kernel.
            lp_results_per_atom.append({
                "atom": atom_name, "Z": Za, "N": Na,
                "n_strands": n_strands_a,
                "deferred_compute_budget": (
                    f"H_{n_strands_a} sympy Hoefsmit precomputation "
                    f"(p({n_strands_a}) partitions × {n_strands_a - 1} "
                    "generators) exceeds session budget without "
                    "pyhecke_native. Re-run with the Rust kernel "
                    "installed to lift this restriction."
                ),
            })
            continue
        try:
            ps = wedderburn_pair_volumes(Za, Na, include_inter=True,
                                         crossings_per_pair=1)
        except Exception as e:
            lp_results_per_atom.append({
                "atom": atom_name, "Z": Za, "N": Na,
                "error": f"{type(e).__name__}: {e}",
            })
            continue
        npairs_a = len(ps)
        if npairs_a == 0:
            lp_results_per_atom.append({
                "atom": atom_name, "Z": Za, "N": Na,
                "n_pairs": 0, "skipped": "no pairs",
            })
            continue
        # Reuse Hoefsmit cache for both supply vector + Gram.
        cache_a = _hoefsmit_mp_matrices(n_strands_a, Q_50_DIGIT_STR)
        ta = _klr_positive_supply_vector(
            ps, n_strands_a, Q_50_DIGIT_STR, hoefsmit_cache=cache_a
        )
        # `full` comes from wedderburn_pair_volumes; keep it in mpf rather
        # than round-tripping the pair amplitudes through a numpy f64 array.
        with mp.workdps(_MP_DPS):
            ta_legacy = [mp.mpf(str(p["full"])) for p in ps]
        Ga = _full_wedderburn_gram(
            ps, n_strands_a, Q_50_DIGIT_STR, hoefsmit_cache=cache_a
        )
        with mp.workdps(_MP_DPS):
            ntarget_a = +(mp.fsum(ta) / 2)
        try:
            ra = solve_operator_selection_lp(
                _as_strings(ta), _as_strings(Ga),
                mp.nstr(ntarget_a, _MP_DPS),
                M_bound="0", backend="clarabel"
            ).to_dict()
        except Exception as e:
            lp_results_per_atom.append({
                "atom": atom_name, "Z": Za, "N": Na,
                "n_pairs": npairs_a,
                "error": f"{type(e).__name__}: {e}",
            })
            continue
        lp_results_per_atom.append({
            "atom": atom_name, "Z": Za, "N": Na,
            "n_pairs": npairs_a,
            "n_strands": n_strands_a,
            # Serialize as strings, not floats. `ta` is now a list of mpf, so
            # `ta.min()` would not even resolve — but the deeper point is that
            # `float(...)` here would put back at the witness door exactly the
            # truncation this port removed upstream. The solver's own `*_str`
            # keys carry the MPFR decimals; prefer them over the f64 twins.
            "t_min_klr": fmt(min(ta)),
            "t_max_klr": fmt(max(ta)),
            "t_legacy_matrix_entries_min": fmt(min(ta_legacy)),
            "t_legacy_matrix_entries_max": fmt(max(ta_legacy)),
            "primal_obj": ra.get("primal_obj_str") or fmt(ra["primal_obj"]),
            "dual_obj": ra.get("dual_obj_str") or fmt(ra["dual_obj"]),
            "duality_gap": (ra.get("duality_gap_str")
                            or fmt(ra["duality_gap"])),
            "y0_star": ra.get("y0_star_str") or fmt(ra["y0_star"]),
            "n_active": len(ra.get("active_set", [])),
            "n_target": fmt(ntarget_a),
            # `ra` is already a to_dict(); carry its provenance + `*_str`
            # through the formatting above rather than dropping them.
            **{k: v for k, v in ra.items()
               if k in ("backend", "precision_bits")
               or k in PROVENANCE_STR_FIELDS},
        })
        print(f"    {atom_name:<12} (Z={Za}, N={Na}): pairs={npairs_a}, "
              f"primal={mp.nstr(mp.mpf(str(ra['primal_obj'])), 8)}, "
              f"y_0={mp.nstr(mp.mpf(str(ra['y0_star'])), 8)}")
    print(f"  LP solve:")
    print(f"    primal_obj = {res_dict['primal_obj']:.6f}")
    print(f"    dual_obj   = {res_dict['dual_obj']:.6f}")
    print(f"    duality_gap= {res_dict['duality_gap']:.3e}")
    print(f"    y_0_star (shadow price of net constraint) = "
          f"{res_dict['y0_star']:.6f}")
    n_active = len(res_dict.get("active_set", []))
    print(f"    # active channels = {n_active}")
    print()

    # ── (B) Alt-Δ_I Weinberg probe ──────────────────────────────
    print("=" * 72)
    print("(B) Alternative Δ_I words to close the 2.19% Weinberg gap")
    print("=" * 72)
    # sin²θ_W = 0.23129 (PDG) is an EXACT rational input; the old code
    # wrapped the exact sympy surd in `float(...)`, throwing away 34 digits
    # before the comparison it feeds.
    with mp.workdps(_MP_DPS):
        _s2w = mp.mpf(23129) / 100000
        cot_codata = +(mp.sqrt(1 - _s2w) / mp.sqrt(_s2w))
    print(f"  CODATA cot θ_W = {mp.nstr(cot_codata, 12)}")
    print()

    # Candidate Δ_I words — all use generators σ_2 (idx 1) and σ_4 (idx 3)
    delta_candidates = [
        ("σ_2 σ_4 σ_2 (minimal, baseline)", [1, 3, 1]),
        ("σ_4 σ_2 σ_4 (mirror)",            [3, 1, 3]),
        ("σ_2 σ_4",                          [1, 3]),
        ("σ_4 σ_2",                          [3, 1]),
        ("σ_2² σ_4²",                       [1, 1, 3, 3]),
        ("σ_4² σ_2²",                       [3, 3, 1, 1]),
        ("σ_2 σ_4² σ_2",                    [1, 3, 3, 1]),
        ("σ_4 σ_2² σ_4",                    [3, 1, 1, 3]),
        ("σ_2 σ_4 σ_2 σ_4",                  [1, 3, 1, 3]),
        ("σ_4 σ_2 σ_4 σ_2",                  [3, 1, 3, 1]),
        ("σ_2 σ_4 σ_2 σ_4 σ_2",             [1, 3, 1, 3, 1]),
        ("σ_2 (single)",                    [1]),
        ("σ_4 (single)",                    [3]),
        ("(empty Δ_I = trivial)",           []),
    ]

    results = []
    for name, delta in delta_candidates:
        t0 = time.time()
        try:
            ratio, eigs = compute_321_max_plus_ratio(Q_50_DIGIT_STR, delta)
        except Exception as e:
            print(f"  {name:<35} FAILED ({type(e).__name__}: {e})")
            continue
        elapsed = time.time() - t0
        if ratio is None:
            print(f"  {name:<35} (insufficient + eigvals)")
            continue
        with mp.workdps(_MP_DPS):
            rel_err = +(abs(ratio - cot_codata) / cot_codata)
        flag = ("★" if rel_err < mp.mpf("0.001")
                else "✓" if rel_err < mp.mpf("0.01")
                else "·" if rel_err < mp.mpf("0.05") else " ")
        print(f"  {flag} {name:<35} ratio = {mp.nstr(ratio, 8):>12s}  "
              f"rel_err = {mp.nstr(rel_err * 100, 4):>8s}%  ({elapsed:.2f}s)")
        results.append({
            "delta_I_name": name,
            "delta_I_word": delta,
            "ratio": fmt(ratio),
            "rel_err": fmt(rel_err),
            "_ratio_mp": ratio,        # popped before serialization
            "_rel_err_mp": rel_err,
        })

    print()
    # Order on the mpf twin, never on the serialized string: decimal string
    # comparison would rank "1e-3" above "9e-4".
    best = min(results, key=lambda r: r["_rel_err_mp"])
    best_rel_err = best["_rel_err_mp"]
    print(f"Best Δ_I (3,2,1)max+/2nd-max+ vs CODATA cot θ_W:")
    print(f"  {best['delta_I_name']}")
    print(f"  Δ_I word: {best['delta_I_word']}")
    print(f"  ratio = {mp.nstr(best['_ratio_mp'], 12)}")
    print(f"  rel err = {mp.nstr(best_rel_err * 100, 6)}%")
    print()

    if best_rel_err < mp.mpf("0.001"):
        verdict = "candidate-found-precision-1e-3"
    elif best_rel_err < mp.mpf("0.01"):
        verdict = "near-miss-precision-1e-2"
    elif best_rel_err < mp.mpf("0.05"):
        verdict = "near-miss-precision-5pct"
    else:
        verdict = "no-clean-fit"
    print(f"VERDICT (B): {verdict}")
    print()

    # ── Witness assembly via WitnessBuilder ────────────────────
    from witness_base import WitnessBuilder
    w = (
        WitnessBuilder("wedderburn-lp-ew-wiring", engine="mpmath+clarabel-mpfr")
        .set_description(
            "Two deliverables: (A) wires wedderburn_pair_volumes into "
            "prop:knot-operator-lp-selection via concrete LP/SDP-dual "
            "program for EW-sector pair amplitudes (atom sweep "
            "proton..helium-4); (B) probes alternative Δ_I words on β_EW "
            "to close the 2.19% Weinberg gap on (3,2,1) max+/2nd-max+ "
            "= cot θ_W reading."
        )
        .set_content_block("prop:knot-operator-lp-selection")
        .add_parameter("q_0", str(q_0))
        .add_parameter("n_target_headline", n_target)
        .add_parameter("delta_I_minimal", "σ_2 σ_4 σ_2")
    )

    # LP behaviour assertions.  With the KLR-positive supply vector
    # (t_k = tr_M(σ_i σ_j) ≥ 0 by KLR positivity on the canonical-
    # basis cone) and the full H_n Wedderburn Gram on the pair-
    # operator algebra, strong duality holds on every atom in the
    # computable sweep.
    # `duality_gap` is now a decimal STRING (the MPFR value, not its f64
    # twin), so compare it as an mpf. The bare `< 1e-6` here survived the
    # serialization port and raised
    # `TypeError: '<' not supported between instances of 'str' and 'float'`
    # AFTER the whole H_9 compute had finished — a five-minute run thrown away
    # at the reporting step. Widening a value's precision changes its type, and
    # every comparison on it has to move with it.
    def _gap_mp(r):
        return abs(_mpf_or(r.get("duality_gap"), mp.inf))

    n_strong_dual = sum(
        1 for r in lp_results_per_atom
        if r.get("n_pairs", 0) > 0 and _gap_mp(r) < mp.mpf("1e-6")
    )
    n_expected = sum(
        1 for r in lp_results_per_atom if r.get("n_pairs", 0) > 0
    )
    # STRINGS, per add_assertion's own docstring ("the drained convention,
    # qou-t0rf"). These two are integer COUNTS — `float(...)` on them was
    # never meaningful, and it put three raw float64 fields into the witness
    # per assertion (computed/expected/tolerance), nine across the three.
    w.add_assertion(
        "lp_strong_duality_all_klr_atoms",
        str(n_strong_dual),
        str(n_expected),
        tolerance="0.5",
    )
    # KLR positivity assertion: every atom's KLR supply vector
    # min(t) ≥ -ε (tiny numerical noise tolerated; substantive
    # negative would indicate a non-canonical-basis pair or a bug).
    n_klr_positive = sum(
        1 for r in lp_results_per_atom
        if r.get("n_pairs", 0) > 0
        and _mpf_or(r.get("t_min_klr"), mp.mpf(-1)) >= mp.mpf("-1e-9")
    )
    w.add_assertion(
        "klr_positivity_supply_vector_all_atoms",
        str(n_klr_positive),
        str(n_expected),
        tolerance="0.5",
    )
    # Weinberg verdict: best rel_err < 2.5% (the σ_2 σ_4 σ_2 baseline)
    w.add_assertion(
        "weinberg_minimal_delta_I_optimal",
        fmt(best_rel_err),
        "0.0219",  # baseline 2.19% rel_err
        tolerance="0.005",
    )

    # (A) LP/SDP-EW deliverable
    w.add_data("deliverable_A_lp_sdp_wiring", {
        "headline_atom": {
            "Z": Z, "N": N,
            "name": atoms_to_test[headline_idx][0],
            "max_full_gram_n_strands": MAX_FULL_GRAM_N,
        },
        "n_pair_amplitudes": n_pairs,
        # Prefer the solver's MPFR `*_str` decimals over their f64 twins;
        # `float(...)` here would reintroduce the truncation at the witness
        # door that the mpmath port removes upstream.
        "primal_obj": (res_dict.get("primal_obj_str")
                       or fmt(res_dict["primal_obj"])),
        "dual_obj": res_dict.get("dual_obj_str") or fmt(res_dict["dual_obj"]),
        "duality_gap": (res_dict.get("duality_gap_str")
                        or fmt(res_dict["duality_gap"])),
        "y0_star": res_dict.get("y0_star_str") or fmt(res_dict["y0_star"]),
        "y_star": (res_dict.get("y_star_str")
                   or [fmt(y) for y in res_dict.get("y_star", [])]),
        "active_set": list(res_dict.get("active_set", [])),
        "n_target": n_target,
        # `G` is list[list[mpf]], not an ndarray — `.shape` was the THIRD
        # consumer the port broke, and the first two were value comparisons,
        # so the grep that caught them (fields that became strings) could not
        # see this one at all: it is a CONTAINER-API consumer of the
        # ndarray -> list change. Both categories move when a type widens.
        "supply_matrix_shape": [len(G), len(G[0]) if G else 0],
        # Solver, precision, and the full-precision decimals.
        **provenance(res),
        "atom_sweep": lp_results_per_atom,
    })

    # Top-level LP-dual fields for lp_dual_witness_validator
    w.add_data("primal_obj", res_dict.get("primal_obj_str")
               or fmt(res_dict["primal_obj"]))
    w.add_data("dual_obj", res_dict.get("dual_obj_str")
               or fmt(res_dict["dual_obj"]))
    w.add_data("duality_gap", res_dict.get("duality_gap_str")
               or fmt(res_dict["duality_gap"]))
    w.add_data("y0_star", res_dict.get("y0_star_str")
               or fmt(res_dict["y0_star"]))
    # The solver's MPFR decimals, not their f64 twins — 28 raw float64 fields
    # entered here alone. Same `*_str`-first rule as the other numerics.
    w.add_data("y_star", res_dict.get("y_star_str")
               or [fmt(y) for y in res_dict.get("y_star", [])])
    w.add_data("active_set", list(res_dict.get("active_set", [])))
    for _k, _v in provenance(res).items():
        w.add_data(_k, _v)

    # (B) Alt-Δ_I Weinberg probe. Drop the `_*_mp` working twins — they exist
    # only so ordering and the verdict thresholds compare mpf against mpf; the
    # serialized form is the `fmt()` string beside them.
    def _shed(rec: dict) -> dict:
        return {k: v for k, v in rec.items() if not k.startswith("_")}

    w.add_data("deliverable_B_alt_delta_I_weinberg_probe", {
        "codata_cot_theta_W": fmt(cot_codata),
        "candidates": [_shed(r) for r in results],
        "best": _shed(best),
        "verdict": verdict,
    })

    out_path = w.save()
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
