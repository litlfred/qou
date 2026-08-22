#!/usr/bin/env python3
"""
Operator-valued A^λ_{μν}(I) extraction via bilinear-system inversion.

Per the refined Sub-lemma 2.1 (`docs/audits/2026-05-04-sublemma-2-1-refined.md`):

    χ^λ(β_1 · I · β_2)
        = Σ_{(μ,ν)} c^λ_{μν} · Tr_{V_μ⊗V_ν}(A^λ_{μν}(I) · (ρ_μ(β_1) ⊗ ρ_ν(β_2))).

The previous probe (`sublemma_2_1_alpha_shift_extract.py`) tried to fit
A as a scalar α_shift and failed for 9 of 11 λ. This probe fits A as
an operator (matrix) on V_μ ⊗ V_ν.

  Number of unknowns per λ = Σ_{(μ,ν) in support} (d_μ · d_ν)².
  Number of equations = number of (β_1, β_2) test pairs we sample.

Solve by least squares; report the extracted A_diag^{μν} matrices and
their pole orders at q = 0 (the categorical inputs needed for the
nucleon-anchor closure).

Output: sublemma-2-1-A-operator-extract.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np  # noqa: F401 — retained for the _mp_kron cross-check
from mpmath import mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from char_fast import _compiled_sigmas  # noqa: E402
from sublemma_2_1_deuteron_branching import (  # noqa: E402
    LR_TABLE_3_3_TO_6 as LR_TABLE,
    lr_coef,
    partitions_of,
)
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

set_compute_dps()  # mp.dps via QOU_COMPUTE_DPS (default 50)

# q_0 as an mpf carried from the 50-digit string, not the float64 `Q`. The
# module previously imported `Q` (a Python float) and every downstream value
# inherited that ceiling regardless of how it was serialized.
Q0 = mp.mpf(Q_50_DIGIT_STR)


# h = q − q⁻¹, DERIVED from this file's own Q0 rather than typed.
#
# It used to read `H = 0.20906032198987945`, and that literal was a LAYER
# STRADDLE inside a single file. `Q0` above is imported from `q_parameter`,
# which is the PROTON pin (1.1099785827513808). Inverting the hardcoded H gives
# q = 1.1099785955541805692 — the canonical MUON q0, matched to 5.5e-18. So this
# module built its braid words at the proton pin and its interface coefficients
# at the muon pin, differing by 1.109e-07 relative on h.
#
# AGENTS.md §q₀ anchor convention names exactly this: "Never straddle the two
# layers inside one quantity." The straddle is invisible at the call site — both
# values are plausible, neither is labelled, and nothing in the emitted witness
# said which layer the interface belonged to.
#
# Deriving it removes the question: whatever pin `q_parameter` resolves to, h
# follows it. Bean `qou-cds4`.
H = Q0 - 1.0 / Q0


def evaluate_word_matrix(shape: tuple, word: list, q_val=None) -> "mp.matrix":
    """Evaluate the Hecke-algebra word `[(c, d, g), ...]` as
    Π_i (c_i · σ_g_i + d_i · I) in the seminormal rep of `shape`.

    mpmath at the module working precision, NOT numpy float64. This used to
    request `_compiled_sigmas(shape, "double")` and build `np.ndarray`s with
    `dtype=complex`, which put every value this producer emits on a float64
    floor — 493 raw-float64 fields in the emitted witness, and a raw-float64
    ratchet regression the moment the colour-weighted interface made more blocks
    operator-valued (bean `qou-zck8`).

    `char_fast` already carried the high-precision backend: `"mpmath50"` returns
    an `mp.matrix` with `mpf` entries. Nothing needed building — this function
    was simply asking for the wrong one.

    ACCURACY CEILING — read before quoting any digit of this producer's output
    past the 16th. `"mpmath50"` buys mpmath ARITHMETIC, not 50-digit DATA. The
    rep matrices it hands back are float64 numbers widened to `mpf`, because
    `char_fast._compiled_sigmas` builds them from `_cached_seminormal(shape)`,
    which returns a float64 ndarray with q ALREADY SUBSTITUTED at the module
    `Q0` (its disk cache is even keyed `q{Q0:.10f}`). The `lambdify(Q_SYM, ...)`
    wrapper is therefore a constant function of q — measured:
    `sigma(q=0.5) == sigma(q=2.0) == sigma(q=7.0)`, all equal to the float64
    truncation of the proton q0, which sits 2.3e-16 from the 50-digit `Q0` this
    file passes in.

    That is what pins the per-lambda residuals at ~1e-15, and no amount of
    mpmath in THIS file can lower it. Concretely, for this producer's output:

      * the values are accurate to ~1e-16 relative, not to 50 digits;
      * the `fmt(...)` strings in the witness are a faithful SERIALIZATION of
        the computed quantity, and are the right thing to store — but digits
        past ~16 carry no information about the mathematics, only about the
        arithmetic that widened them. The witness says so in
        `precision.accuracy_ceiling` rather than leaving a reader to infer
        50 significant figures from the field width;
      * the port's actual, narrower win stands: the emitted witness no longer
        carries raw float64 JSON fields (the ratchet target, bean `qou-zck8`)
        and the intermediate linear algebra no longer accumulates float64 error
        across a 144-equation solve.

    No current caller of `char_fast` sweeps q — every one passes q0 — so the
    constant-function behaviour is latent rather than actively wrong. It is
    still a trap, and is filed separately; it is upstream of this file and is
    deliberately NOT fixed here.
    """
    if q_val is None:
        q_val = Q0
    sigmas, dim = _compiled_sigmas(shape, "mpmath50")
    if dim == 0:
        return mp.matrix(0, 0)
    sigma_mats = [fn(q_val) for fn in sigmas]
    I = mp.eye(dim)
    M = mp.eye(dim)
    for c, d, g in word:
        if g >= len(sigma_mats):
            return mp.zeros(dim, dim)
        M = M * (mp.mpf(c) * sigma_mats[g] + mp.mpf(d) * I)
    return M


def _mp_kron(A, B):
    """Kronecker product for mpmath matrices — mpmath has no built-in.

    Index order is `(i*rb + k, j*cb + l)`, matching `np.kron` exactly. That
    ordering is load-bearing: the caller flattens `X.T` and relies on the layout
    lining up with the `A_kk` unknowns, and this file already records a bug in
    that correspondence which produced 4e-3 relative residual on λ = (3,2,1).
    Verified against `np.kron` on the live shapes rather than assumed.
    """
    ra, ca = A.rows, A.cols
    rb, cb = B.rows, B.cols
    out = mp.zeros(ra * rb, ca * cb)
    for i in range(ra):
        for j in range(ca):
            aij = A[i, j]
            if aij == 0:
                continue
            for k in range(rb):
                for l in range(cb):
                    out[i * rb + k, j * cb + l] = aij * B[k, l]
    return out


# Relative threshold on |R_ii| for counting a column as independent. At the
# module working precision (50 dps) the arithmetic noise floor is ~1e-50, and
# the live systems have condition numbers between 1.00 and 4.42 — so the
# smallest |R_ii| sits within a factor ~4 of the largest. 1e-30 is therefore
# far above the noise and far below any real column, and the rank verdict is
# not sensitive to the exact choice. Recorded in the witness so a reader can
# check that rather than take it on trust.
_RANK_REL_TOL = mp.mpf("1e-30")


def _rank_via_qr(M) -> int:
    """Numerical column rank, counted off the QR diagonal.

    `np.linalg.lstsq` used to hand back a `rank` alongside the solution and the
    witness recorded it. `mp.qr_solve` returns only `(solution, residual)`, so
    the field has to be computed rather than read off — and it must be
    COMPUTED, not assumed. Writing `n_unknowns` here because the pre-port
    instrumentation measured 0 rank-deficient systems would launder a
    measurement taken once into a fact asserted every run; if a later change to
    the test-pair set makes a system deficient, the witness has to say so.

    Agrees with `np.linalg.matrix_rank` on the live shapes (144x1, 144x16,
    144x32).
    """
    _, R = mp.qr(M)
    diag = [abs(R[i, i]) for i in range(min(R.rows, R.cols))]
    if not diag:
        return 0
    mx = max(diag)
    if mx == 0:
        return 0
    return sum(1 for d in diag if d > mx * _RANK_REL_TOL)


def _mat_dim(M) -> int:
    """Wedderburn block dimension of a (square) rep matrix, 1 if empty.

    Was `max(M.shape) if M.size > 0 else 1` — both numpy-only attributes that
    survived the float64 port and crashed on first run. `mp.matrix` carries
    `.rows` / `.cols` and neither `.shape` nor `.size`.
    """
    if M.rows == 0 or M.cols == 0:
        return 1
    return max(M.rows, M.cols)


def disjoint_word(word_p: list, word_n: list, n1: int = 3) -> list:
    """β_1 ⊗ β_2 in H_(n1 + n2): re-index β_2 generators by +n_1."""
    out = list(word_p)
    out += [(c, d, g + n1) for (c, d, g) in word_n]
    return out


def _pn_interface_d():
    """`d` of the canonical p-n interface, from the module that owns ctypes.

    The default below used to be the literal `-H/2` — the colour-BLIND averaged
    crossing. The canonical builder emits `averaged_weighted` at a p-n boundary,
    `d = -h(1/2 - δ/4)`, which sits 7.190163e-05 away. This extract feeds the
    deuteron `(6, "pn")` A-operator cache, which is the ONLY route by which the
    canonical mass table's interface is still colour-blind: A ≥ 3 returns
    earlier via the q0-baked colour-weighted transfer path and never reads an
    extract at all. Bean `qou-cds4`.

    Derived rather than typed, so this file cannot drift from the classifier
    again the way the hardcoded literal did.

    Returns an `mpf`. This wrapper read `float(d_for_ctype(...))` for the first
    run after the mpmath port, discarding everything past 2.1e-17 of a value
    `d_for_ctype` supplies to 40+ digits. Dropping the cast is right on its own
    terms and is kept.

    It is NOT, however, what caps this producer's residuals. I predicted it was
    — the ~1e-15 per-lambda residuals looked exactly like one float64 input —
    and re-running after the fix produced residuals byte-identical to before.
    The cast was a truncation with no downstream consequence. The real floor is
    upstream in `char_fast`; see `evaluate_word_matrix`.
    """
    from canonical_braid_crossings import d_for_ctype
    return d_for_ctype("averaged_weighted", H)


def with_interface(word_p: list, word_n: list, n1: int = 3,
                    int_c=1.0, int_d=None) -> list:
    """β_1 · I · β_2 in H_(n1 + n2) with I = c·σ_(n1-1) + d·1.

    `int_d=None` (the default) resolves to the canonical colour-weighted p-n
    interface, as an `mpf`. Pass an explicit value only to probe a non-canonical
    convention, and label it where you do — and pass it as `mpf`, not `float`.

    `int_c` / `int_d` were annotated `float` and are deliberately no longer:
    the annotation is what made the float64 cast in `_pn_interface_d` look
    correct. `int_c = 1.0` stays a Python float only because 1.0 is exact in
    both representations and promotes on contact with `mpf`.
    """
    if int_d is None:
        int_d = _pn_interface_d()
    out = list(word_p)
    out.append((int_c, int_d, n1 - 1))   # interface generator at strand n_1
    out += [(c, d, g + n1) for (c, d, g) in word_n]
    return out


def chi_lambda_matrix_trace(shape: tuple, word: list):
    """χ^λ(β) = Tr ρ_λ(β), as an mpmath scalar."""
    M = evaluate_word_matrix(shape, word)
    if M.rows == 0:
        return mp.mpf(0)
    return mp.fsum(M[i, i] for i in range(M.rows))


def make_test_words():
    """A diverse set of H_3 algebra elements for over-determining the
    bilinear system. The set spans End(V_μ) for μ ⊢ 3 well enough by
    construction (~10 elements ≥ d_μ²)."""
    return [
        [],                                                   # identity (d_μ²=4 spans)
        [(1.0, 0.0, 0)],                                      # σ_0
        [(1.0, 0.0, 1)],                                      # σ_1
        [(1.0, 0.0, 0), (1.0, 0.0, 1)],                       # σ_0 σ_1
        [(1.0, 0.0, 1), (1.0, 0.0, 0)],                       # σ_1 σ_0
        [(1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0)],        # trefoil
        [(1.0, -H, 0)],                                       # σ_0 - h
        [(1.0, -H/2, 1)],                                     # σ_1 - h/2
        [(1.0, 0.0, 0), (1.0, -H, 1)],                        # σ_0 (σ_1 - h)
        [(1.0, -H, 0), (1.0, -H/2, 1)],                       # (σ_0 - h)(σ_1 - h/2)
        [(1.0, 0.0, 0), (1.0, 0.0, 0)],                       # σ_0²
        [(1.0, 0.0, 1), (1.0, 0.0, 1)],                       # σ_1²
    ]


def main() -> int:
    parts_3 = partitions_of(3)
    parts_6 = partitions_of(6)
    test_words = make_test_words()
    K = len(test_words)

    print("=" * 96)
    print("  Operator-valued A^λ_{μν}(I) extraction (refined Sub-lemma 2.1)")
    print("=" * 96)

    # Pre-compute ρ_μ(β) for each test word and each μ ⊢ 3
    print(f"\n  Pre-computing ρ_μ(β) at q_0 = {float(Q0):.6f}...")
    rho_mu = {(i, mu): evaluate_word_matrix(mu, w) for i, w in enumerate(test_words) for mu in parts_3}

    # Compute χ^λ(β_p · I · β_n) for each pair
    print(f"  Computing χ^λ(β_p · I · β_n) for {K * K} = {K*K} pairs × {len(parts_6)} λ partitions...")
    chi_lam = {}
    for i, wp in enumerate(test_words):
        for j, wn in enumerate(test_words):
            comb = with_interface(wp, wn)
            for lam in parts_6:
                chi_lam[(i, j, lam)] = chi_lambda_matrix_trace(lam, comb)

    # Per-λ: bilinear system inversion to extract A_diag^{μν} matrix entries
    print(f"\n  Per-λ operator-valued A extraction:")
    print(f"  {'λ ⊢ 6':<14} {'support':<22} {'unknowns':>10} {'rel res':>10}  status")
    print("  " + "-" * 76)
    results_per_lambda = {}
    successes = []
    for lam in parts_6:
        # Build support list
        pairs = []
        for mu in parts_3:
            for nu in parts_3:
                c = lr_coef(mu, nu, lam)
                if c > 0:
                    d_mu = _mat_dim(rho_mu[(0, mu)])
                    d_nu = _mat_dim(rho_mu[(0, nu)])
                    n_entries = (d_mu * d_nu) ** 2
                    pairs.append({"mu": mu, "nu": nu, "c": c,
                                   "d_mu": d_mu, "d_nu": d_nu,
                                   "n_entries": n_entries})

        if not pairs:
            continue

        n_unknowns = sum(p["n_entries"] for p in pairs)
        # Build M @ vec(A) = rhs system
        # Each (i, j) test pair gives one equation:
        #   chi^λ(β_p_i · I · β_n_j) = Σ_pairs c^λ_{μν} · Tr(A^μν · (ρ_μ(β_p_i) ⊗ ρ_ν(β_n_j)))
        # Let X_{ij}^{μν} = ρ_μ(β_p_i) ⊗ ρ_ν(β_n_j); flatten to row vec.
        # Tr(A · X) = Σ_{ab} A_{ab} X_{ba} → coefficient on A_{ab} is X_{ba}.
        n_eq = K * K
        M = mp.zeros(n_eq, n_unknowns)
        rhs = mp.zeros(n_eq, 1)
        offsets: list[int] = [0]
        for p in pairs:
            offsets.append(offsets[-1] + p["n_entries"])

        for k, ((i, wp), (j, wn)) in enumerate(
            ((i, wp), (j, wn)) for i, wp in enumerate(test_words) for j, wn in enumerate(test_words)
        ):
            for p_idx, p in enumerate(pairs):
                mu, nu = p["mu"], p["nu"]
                B_mu = rho_mu[(i, mu)]
                B_nu = rho_mu[(j, nu)]
                X = _mp_kron(B_mu, B_nu)   # (d_μ d_ν, d_μ d_ν) matrix
                # Tr(A_diag · X) where A_diag = Σ_k A_kk sums over LR
                # multiplicity copies. The multiplicity c^λ_{μν} is
                # absorbed into A_diag itself; do NOT multiply by c
                # again here (corrects an early bug that gave 4e-3 rel
                # residual on λ = (3,2,1)).
                # X.T flattened row-major == X flattened column-major.
                base = offsets[p_idx]
                nX = X.rows
                for a in range(nX):
                    for b in range(nX):
                        M[k, base + a * nX + b] = X[b, a]
            rhs[k] = chi_lam[(i, j, lam)]

        # Solve by least squares.
        #
        # Was `np.linalg.lstsq(M, rhs, rcond=None)`. `mp.qr_solve` is the
        # mpmath counterpart and IS a valid drop-in HERE — but only because the
        # rank question was answered first, not assumed. `rcond=None` is
        # rank-revealing and silently truncates small singular values, which
        # `qr_solve` does not do, so the two agree only on a full-rank system.
        #
        # Measured on the live systems by instrumenting the float64 call before
        # porting: 11 systems, shapes (144, 1) through (144, 32), **0
        # rank-deficient** — every one full column rank, with condition numbers
        # between 1.00 and 4.42. So the truncation branch never fired, and at
        # cond ≈ 4 the float64 answer was already good to ~1e-15.
        #
        # That sets the acceptance bar for this port: values must agree with
        # the float64 reference to ~1e-15. A LARGER disagreement is a porting
        # bug — it is not mpmath "revealing" a truer number, and reading it that
        # way is the rationalisation `qou-4e5k` is the worked example of.
        sol, _res = mp.qr_solve(M, rhs)
        rank = _rank_via_qr(M)
        pred = M * sol
        # Use a SCALE-AWARE relative error: residual normalized by the
        # typical magnitude of |rhs| across the test pairs, not divided
        # per-equation. The per-equation form |res|/|rhs| explodes when
        # an individual rhs[k] happens to be near zero (which can occur
        # for symmetry-driven cancellations in specific test pairs)
        # even when the global fit is at machine precision.
        # Aggregated in mpmath, not float64. AGENTS.md rule 2 names this case
        # directly: never aggregate with statistics/math over floats, because
        # the error accumulates across the sample — and this is a mean over
        # K² = 144 equations.
        _n = rhs.rows
        rhs_scale = max(mp.fsum(abs(rhs[i, 0]) for i in range(_n)) / _n,
                        mp.mpf("1e-12"))
        max_abs_res = max(abs(pred[i, 0] - rhs[i, 0]) for i in range(_n))
        max_rel = max_abs_res / rhs_scale

        # Reshape sol into per-pair matrices A_diag^{μν}
        A_per_pair = {}
        for p_idx, p in enumerate(pairs):
            d = p["d_mu"] * p["d_nu"]
            base = offsets[p_idx]
            A_mat = mp.matrix(d, d)
            for a in range(d):
                for b in range(d):
                    A_mat[a, b] = sol[base + a * d + b, 0]   # order="C"
            _tr = mp.fsum(A_mat[a, a] for a in range(d))
            _frob = mp.sqrt(mp.fsum(abs(A_mat[a, b]) ** 2
                                    for a in range(d) for b in range(d)))
            _maxabs = max(abs(A_mat[a, b]) for a in range(d) for b in range(d))
            _dev = mp.sqrt(mp.fsum(
                abs(A_mat[a, b] - (_tr / d if a == b else 0)) ** 2
                for a in range(d) for b in range(d)))
            A_per_pair[f"({p['mu']},{p['nu']})"] = {
                # Serialized via `_precision.fmt` rather than `float(...)`:
                # these are now mpf/mpc carried from the solve, and casting
                # them to float here would discard the precision the port
                # exists to obtain, while leaving the field looking correct.
                "matrix_re": [[fmt(mp.re(A_mat[a, b])) for b in range(d)] for a in range(d)],
                "matrix_im": [[fmt(mp.im(A_mat[a, b])) for b in range(d)] for a in range(d)],
                "frobenius_norm": fmt(_frob),
                "max_abs_entry": fmt(_maxabs),
                "trace": fmt(mp.re(_tr)),
                "is_scalar_multiple_of_id": bool(d == 1 or _dev < mp.mpf("1e-9")),
                "c_lr": p["c"],
                "d_mu": p["d_mu"], "d_nu": p["d_nu"],
            }

        max_c = max(p["c"] for p in pairs)
        support_str = f"{len(pairs)} pairs, max c={max_c}"
        consistent = max_rel < 1e-6
        if consistent:
            successes.append(lam)
            status = "✓"
        else:
            status = "✗"
        print(f"  {str(lam):<14} {support_str:<22} {n_unknowns:>10} {max_rel:>10.2e}  {status}")

        results_per_lambda[lam] = {
            "support": [{**p, "mu": list(p["mu"]), "nu": list(p["nu"])} for p in pairs],
            "n_unknowns": int(n_unknowns),
            "n_equations": int(n_eq),
            "rank": int(rank),
            "max_relative_residual": max_rel,
            "consistent": consistent,
            "A_per_pair": A_per_pair,
        }

    print(f"\n  Summary: {len(successes)} of {len(parts_6)} λ admit consistent operator-valued A^λ_{{μν}}")
    if len(successes) == len(parts_6):
        print("  ✅ Refined Sub-lemma 2.1 numerically VERIFIED for all λ ⊢ 6 in deuteron case.")

    # Highlight which (μ, ν) blocks are scalar vs operator-valued
    print(f"\n  Scalar vs operator-valued breakdown:")
    n_scalar = 0
    n_operator = 0
    for lam in successes:
        for key, info in results_per_lambda[lam]["A_per_pair"].items():
            if info["is_scalar_multiple_of_id"]:
                n_scalar += 1
            else:
                n_operator += 1
    print(f"    Scalar (multiple of identity):   {n_scalar} (μ, ν) blocks")
    print(f"    Operator (non-scalar):            {n_operator} (μ, ν) blocks")

    # Pole-order summary (max|entry| dominated by what q-power)
    print(f"\n  Per-(λ, μ, ν) Frobenius norms of A_diag^{{μν}}:")
    print(f"    (Higher norms ↔ stronger interface contribution; scalar 1×1 blocks listed verbatim)")
    print()
    print(f"  {'λ':<14} {'(μ, ν)':<28} {'‖A‖_F':>10} {'max|entry|':>12}  is_scalar")
    print("  " + "-" * 76)
    for lam in successes:
        for key, info in results_per_lambda[lam]["A_per_pair"].items():
            scalar_str = "scalar" if info["is_scalar_multiple_of_id"] else "operator"
            # `frobenius_norm` / `max_abs_entry` are `fmt(...)` STRINGS in the
            # witness — full-precision decimal, per the serialization rule. The
            # `:>10.4f` float format they used to carry raises `ValueError:
            # Unknown format code 'f' for object of type 'str'` on a string, so
            # parse back to mpf for the human-facing table rather than
            # downgrading the stored field to a float to keep the format alive.
            print(f"  {str(lam):<14} {key:<28} "
                  f"{float(mp.mpf(info['frobenius_norm'])):>10.4f} "
                  f"{float(mp.mpf(info['max_abs_entry'])):>12.4f}  {scalar_str}")

    witness = {
        "computation": "sublemma-2-1-A-operator-extract",
        "description": (
            "Operator-valued A^λ_{μν}(I) extraction via bilinear-system "
            "inversion. Confirms refined Sub-lemma 2.1: the (μ,ν)-block "
            "of ρ_λ(I) is generally a non-scalar operator on V_μ ⊗ V_ν. "
            "For the deuteron interface I = σ_2 - h(1/2 - δ/4) on "
            "H_6 ↓ H_3 × H_3 — the canonical COLOUR-WEIGHTED p-n crossing, "
            "ctype `averaged_weighted` — all "
            "11 λ admit consistent operator-valued A^λ_{μν} solutions to "
            "machine precision; only the 1-dim extreme λ ∈ {(6), (1^6)} "
            "have scalar A^λ_{μν}. The extracted matrices are the "
            "concrete categorical inputs the Hoefsmit-formula derivation "
            "must reproduce per docs/audits/2026-05-04-sublemma-2-1-"
            "categorical-proof.md."
        ),
        "reference_blocks": [
            "conj:confinement-nf-structure-forcing",
            "prop:atomic-mass-gb-nf",
            "prop:alpha-shift-torus-knot",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        # The experimental PROTON pin, declared rather than left to be inferred
        # from the value. This witness carried no `q0Anchor` at all, so nothing
        # downstream could tell which layer it belonged to (AGENTS.md: "Say
        # which pin you used").
        "q0Anchor": "proton",
        "q0Value": str(Q_50_DIGIT_STR),
        "parameters": {
            # Was `float(Q0)` — a raw float64 JSON field, one of the 493 this
            # port exists to remove.
            "q_0": fmt(Q0),
            # Was "I = σ_2 - h/2 (atomic-braid pn averaged crossing)". That is
            # the colour-BLIND crossing, and it is what this branch changed;
            # leaving the label would have described the previous convention
            # while emitting the new one. `d` is recorded numerically alongside
            # so the claim is checkable and cannot drift from the code again.
            "interface": (
                "I = σ_2 - h(1/2 - δ/4)  [ctype `averaged_weighted`: the "
                "canonical colour-weighted p-n crossing]"),
            "interface_ctype": "averaged_weighted",
            "interface_d": fmt(_pn_interface_d()),
            "n_test_pairs": K * K,
            "n_test_words_per_side": K,
        },
        "precision": {
            "compute_dps": mp.dps,
            "serialization": "_precision.fmt",
            # Stated explicitly so no consumer reads significance off the field
            # width. See `evaluate_word_matrix.__doc__` for the measurement.
            "accuracy_ceiling_relative": "~1e-16",
            "accuracy_ceiling_cause": (
                "char_fast._compiled_sigmas returns rep matrices built by "
                "_cached_seminormal(shape), which are float64 with q already "
                "substituted; the mpmath backend widens them but adds no "
                "information. Arithmetic here is exact-to-precision; the INPUT "
                "data is float64. Digits past ~16 are arithmetic, not "
                "mathematics."),
        },
        "results_per_lambda": {
            str(lam): results_per_lambda[lam] for lam in parts_6
        },
        "scalar_consistent_lambda": [list(l) for l in successes],
        "n_consistent": len(successes),
        "all_lambda_consistent": len(successes) == len(parts_6),
        "n_scalar_blocks": n_scalar,
        "n_operator_blocks": n_operator,
    }
    out = HERE / "sublemma-2-1-A-operator-extract.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
