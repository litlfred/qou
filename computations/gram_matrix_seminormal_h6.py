#!/usr/bin/env python3
"""gram_matrix_seminormal_h6.py — Option E Phase 1 deliverable.

**Per-block Hoefsmit-seminormal representation infrastructure at H_6
(deuteron) and H_3 (cross-check).**

The canonical 6×6 Hoefsmit-seminormal Gram for H_3(q) exists on main
(`folio/quantum-observable-universe/lean/QOU/Interactions/GramMatrixH3Symbolic.lean`)
but uses the NF basis (6 specific braid-word elements). For larger
H_n, this basis grows as n! (720 for H_6, 362,880 for H_9) and is
intractable.

The Wedderburn-block decomposition replaces this with one Gram-like
matrix per partition λ ⊢ n, of size dim_λ × dim_λ. Total entries
across all blocks = Σ_λ dim_λ² = n!.

## Phase 1 scope (this script)

For each partition λ ⊢ n (n ∈ {3, 6}):
  - Per-block Hoefsmit-seminormal σ_k matrices ρ_λ(σ_k), k=1..n-1
  - Per-block longest-word matrix ρ_λ(w_0) where w_0 is the
    longest element of S_n
  - Per-block character value χ_λ(w_0) computed two ways:
    (a) tr(ρ_λ(w_0)) via the full matrix product
    (b) `q_character_on_braid_word(λ, w_0_crossings, q)` — the
        canonical chain-rule computation
    These must agree to numerical precision (cross-check).

## Output witness

`option-e-phase1-gram-h6.witness.json` records:
  - n = 6, q_0 (50 dps)
  - For each λ ⊢ 6:
    - shape, dim_λ
    - Per-block σ_k matrices at q_0 (numerical, real part)
    - ρ_λ(w_0) at q_0
    - χ_λ(w_0) via both methods + cross-check residual
  - H_3 cross-check (same structure)

Usage:
    python3 gram_matrix_seminormal_h6.py

Dependencies: sympy, mpmath. NO pyhecke_native required (pure-Python
Hoefsmit construction).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp
from sympy.utilities.iterables import partitions as _sp_partitions

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()  # canonical compute precision per qou_substrate.precision

from hecke_character_symbolic import (  # noqa: E402
    _hoefsmit_build,
    q_character_on_braid_word,
)
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
# 🛑 PROTON PIN (migrated 2026-08-29, bean `qou-cds3`). AGENTS.md
# §"q₀ anchor convention": the experimental (proton) anchor is the default
# for all production compute, and the owner authorisation recorded there
# covers this sweep ("we want proton unless for an explicit reason ... fix
# all, even if not visible").
#
# This read `q-pinning-50-digit.witness.json` -> `derived_50_digit.q`, the
# MUON value, which NO manifest entry and NO `QOU_Q0_ANCHOR` could reach: a
# direct read of the anchor-defining witness computes at muon whatever the
# configuration says. The two pins differ by 11.54 ppb, the μ–p substrate
# tension itself.
#
# The upstream record is KEPT — that witness remains the canonical 3-CAL
# (muon) pin document, it is simply no longer the source of this
# computation's q₀. Idiom copied from `alpha/alpha_k_jones_markov_h12.py`.
record_upstream(Q_PIN, _UPSTREAM_RECORDS)
from q_parameter import Q_50_DIGIT_STR as _Q50_PROTON  # noqa: E402
Q0_MP = mp.mpf(_Q50_PROTON)
# `Q0_F64` is a DISPLAY/echo alias only -- the banner print and the
# `q_0_f64` witness field, which records the pin as the binary64 decimal it
# rounds to. It no longer feeds any computation: the conditioning
# diagnostics that used to need it now run through `mp.svd_r`. Every matrix
# entry is evaluated at `Q0_MP`, the full 50-digit pin.
Q0_F64 = float(Q0_MP)

# Digits requested from sympy's `evalf` for each matrix entry. Matched to the
# anchor's own 50, not to the corpus OUTPUT_DPS of 60: the pin carries 50, so
# asking for 60 would print ten digits nothing supplies.
_EVAL_DPS = 50


def _c(z) -> str:
    """Serialize one matrix entry's real part as a decimal string."""
    return mp.nstr(z.real if hasattr(z, "real") else z, _EVAL_DPS,
                   strip_zeros=False)


def partitions_of_descending(n: int) -> list[list[int]]:
    """All partitions of n as descending-sorted lists (no pyhecke_native dep)."""
    shapes = []
    for p in _sp_partitions(n):
        parts = sorted(p.items(), reverse=True)
        expanded = []
        for size, count in parts:
            expanded.extend([size] * count)
        shapes.append(expanded)
    return shapes


def longest_reduced_word(n: int) -> list[int]:
    """Coxeter longest-word reduced expression for S_n.

    Returns generator indices [k_1, ..., k_{n(n-1)/2}] (1-indexed in
    Coxeter notation) such that σ_{k_1} ... σ_{k_L} is reduced for
    w_0 ∈ S_n.
    """
    if n <= 1:
        return []
    return list(range(n - 1, 0, -1)) + longest_reduced_word(n - 1)


def _ev(expr, q_sym, q_val) -> "mp.mpc":
    """Evaluate one symbolic expression at the full-precision q0.

    Three sites collapsed a symbolic expression with `complex(expr.evalf(...))`
    and only one of them was inside `evaluate_matrix_numerical`. Missing the
    other two had a visible cost: `chi_direct` reached 50 digits while
    `chi_chain` stayed binary64, so `residual = |chi_direct - chi_chain|`
    stopped measuring whether the two DERIVATIONS agree and started measuring
    the f64 collapse of one leg. It read 1.11e-16 -- exactly binary64 epsilon,
    which is the tell.
    """
    return mp.mpmathify(str(sp.N(expr.subs({q_sym: q_val}), _EVAL_DPS)))


def evaluate_matrix_numerical(M_sym: sp.Matrix, q_sym: sp.Symbol, q_val
                               ) -> list[list["mp.mpc"]]:
    """Substitute q_sym -> q_val in M_sym at FULL precision.

    The source here is SYMBOLIC — `M_sym` is an exact sympy expression in
    `q` — so there is nothing approximate about these matrices until the
    substitution. This function used to do

        complex(M_sym[i, j].evalf(subs={q_sym: q_val}))

    with `q_val = float(Q0_MP)`, which threw the precision away twice over:
    the anchor was truncated to binary64 before substitution, and whatever
    `evalf` returned was then collapsed by `complex()`. A symbolic source
    evaluated into a double is the cheapest kind of precision to recover and
    the easiest to lose.

    `evalf` is now given the full 50-digit q0 and asked for `_EVAL_DPS`
    digits, and the result is carried as `mpc`.
    """
    n_rows, n_cols = M_sym.shape
    return [[mp.mpmathify(str(sp.N(M_sym[i, j].subs({q_sym: q_val}),
                                   _EVAL_DPS)))
             for j in range(n_cols)]
            for i in range(n_rows)]


def per_block_data(n: int, q_sym: sp.Symbol, q_val: float) -> dict[tuple, dict]:
    """For each λ ⊢ n, build per-block representation data.

    Returns dict keyed by partition tuple with:
      - dim, syts, sigma_k_at_q0, w0_matrix_at_q0, chi_lambda_w0_direct,
        chi_lambda_w0_via_chain, cross_check_residual
    """
    out: dict[tuple, dict] = {}
    word_w0_1based = longest_reduced_word(n)
    # crossings for q_character_on_braid_word: (gen_0based, "sigma")
    crossings = [(k - 1, "sigma") for k in word_w0_1based]

    for shape in partitions_of_descending(n):
        shape_t = tuple(shape)
        matrices_sym, dim, syts = _hoefsmit_build(list(shape), q_sym)

        if dim == 0:
            continue

        # σ_k matrices at q_0 (numerical)
        sigma_k_at_q0 = [evaluate_matrix_numerical(M, q_sym, q_val)
                         for M in matrices_sym]

        # ρ_λ(w_0) symbolic via chain product, then numerical
        if dim == 1:
            w0_sym = sp.eye(1)
            for k in word_w0_1based:
                w0_sym = w0_sym * matrices_sym[k - 1]
            # NOT `complex(... .evalf(...))`. That is the exact float64 round
            # trip `evaluate_matrix_numerical`'s docstring says it removed —
            # left behind here because this branch builds its 1x1 by hand
            # rather than calling that helper. It is why every w0_det the
            # float64-padding ratchet flags is a ONE-DIMENSIONAL block:
            # (3) and (1,1,1) at H_3, (6) and (1,1,1,1,1,1) at H_6, all dim 1
            # and all four claiming 50 digits over a binary64 (e.g. h6.(6)
            # `4.78320490856174895810681846342049539089202880859375...`, whose
            # tail is the exact binary64 expansion). The qou-k6b3 fix corrected
            # `_real_det` to run `mp.det` on mpmath matrices, which is right and
            # is not enough: the MATRIX reaching it was already float64 here.
            w0_at_q0 = evaluate_matrix_numerical(w0_sym, q_sym, q_val)
            chi_direct = _ev(w0_sym[0, 0], q_sym, q_val)
        else:
            w0_sym = sp.eye(dim)
            for k in word_w0_1based:
                w0_sym = w0_sym * matrices_sym[k - 1]
                # cancel keeps complexity manageable
                w0_sym = w0_sym.applyfunc(sp.cancel)
            w0_at_q0 = evaluate_matrix_numerical(w0_sym, q_sym, q_val)
            chi_direct = sum((_ev(w0_sym[i, i], q_sym, q_val)
                              for i in range(dim)), mp.mpc(0))

        # χ_λ(w_0) via canonical chain (q_character_on_braid_word)
        chi_chain_sym = q_character_on_braid_word(shape_t, crossings, q_sym)
        chi_chain = _ev(chi_chain_sym, q_sym, q_val)

        residual = abs(chi_direct - chi_chain)

        # Per-block det/cond telemetry. Both are computed at working
        # precision on the mpmath matrices these already are; nothing here
        # goes through numpy any more.

        def _real_part(M):
            """M's real part as a real mpmath matrix, refusing imag residue.

            The seminormal construction is real over real q, so any imaginary
            residue is a sqrt-branch artefact -- `_eval_matrix` applies this
            entrywise already; this repeats it at the point where the value
            is about to be consumed by a real-only routine (`mp.svd_r`).
            """
            # `M` is a list-of-lists of `mpc` here, not an `mp.matrix` --
            # `mp.det` coerces one silently, `mp.svd_r` does not.
            R = mp.matrix(len(M), len(M[0]))
            for i, row in enumerate(M):
                for j, v in enumerate(row):
                    im = abs(mp.im(v))
                    if im > mp.mpf("1e-40"):
                        raise ValueError(
                            f"entry ({i},{j}) has a non-negligible imaginary "
                            f"part {im} (sqrt-branch artefact or bug)")
                    R[i, j] = mp.re(v)
            return R

        def _real_cond(M):
            """cond_2(M) = sigma_max/sigma_min as a real mpf.

            This WAS `float(np.linalg.cond(...))`, a binary64 SVD, and it is
            the same defect class as the determinant below rather than a
            different one: the old comment here declared all four telemetry
            fields "float64 by construction", which was only ever true of
            `cond`, and `cond` did not have to be. `mp.svd_r` runs the SVD at
            working precision on the exact matrix, and on a worked 3x3 whose
            true condition number is 4 numpy returns 3.999999999999999 while
            this returns 4. Bean `qou-k6b3`.
            """
            if len(M) <= 1:
                return mp.mpf(1)
            S = mp.svd_r(_real_part(M), compute_uv=False)
            s_min, s_max = min(S), max(S)
            if s_min == 0:
                raise ValueError(
                    "matrix is singular; rho_lam(sigma_k) is a representation "
                    "of an invertible braid generator and cannot be")
            return s_max / s_min

        def _real_det(M):
            """det(M) as a real mpf, refusing a non-negligible imaginary part.

            The seminormal construction is real over real q, so any imaginary
            residue is a sqrt-branch artefact -- the same reasoning
            `_eval_matrix` applies entrywise, applied to the determinant.
            """
            d = mp.det(M)
            im = abs(mp.im(d))
            if im > mp.mpf("1e-40"):
                raise ValueError(
                    f"det has a non-negligible imaginary part {im} "
                    "(sqrt-branch artefact or bug)")
            return mp.re(d)

        # DETERMINANTS are exact; only the CONDITION NUMBERS need float64.
        # The comment above lumped the four fields together as "float64 by
        # construction", but that is true only of `cond`, which is a binary64
        # SVD. `mp.det` is LU-based and runs directly on the mpmath matrices
        # these already are — so the dets never needed the `_np_real` round
        # trip. It mattered: rho_lam(sigma_k) is a representation of an
        # invertible braid generator, so several of these determinants are
        # exactly +-1, and float64 returned -0.9999999999999999. The
        # raw-float64 ratchet cannot see that error while the true value is
        # whole (its integral carve-out skips an exact -1.0), so it stayed
        # hidden until an anchor change pushed the results off the integers.
        # Bean `qou-k6b3`.
        sigma_k_dets = [fmt(_real_det(M)) for M in sigma_k_at_q0]
        sigma_k_conds = [fmt(_real_cond(M)) for M in sigma_k_at_q0]
        w0_det = fmt(_real_det(w0_at_q0))
        w0_cond = fmt(_real_cond(w0_at_q0))

        # q → 1 classical-limit check (recorded as data, not asserted).
        # The Hoefsmit-seminormal construction has axial-distance
        # denominators `1 − q⁻²ρ` that vanish at q=1, so the direct
        # evaluation at q=1 yields 0/0 NaN. The genuine classical limit
        # exists via L'Hôpital (equals the classical Frobenius character
        # on the cycle type of w_0), but recovering it requires a basis
        # change to Young's natural / orthogonal form — out of scope for
        # this Phase 1 deliverable. Reported as data here for transparency:
        # a future phase should replace this with a symbolic L'Hôpital or
        # natural-form evaluation.
        try:
            chi_at_q_eq_1_sym = q_character_on_braid_word(
                shape_t, crossings, sp.Integer(1)
            )
            chi_at_q_eq_1_val = complex(chi_at_q_eq_1_sym.evalf())
            chi_at_q_eq_1 = (chi_at_q_eq_1_val.real
                             if chi_at_q_eq_1_val.real == chi_at_q_eq_1_val.real
                             else None)  # NaN check
        except (ZeroDivisionError, TypeError):
            chi_at_q_eq_1 = None

        out[shape_t] = {
            "dim": dim,
            "n_syts": len(syts),
            "sigma_k_at_q0_re": [[[_c(v) for v in row] for row in M]
                                 for M in sigma_k_at_q0],
            "w0_matrix_at_q0_re": [[_c(v) for v in row] for row in w0_at_q0],
            "chi_lambda_w0_direct": _c(chi_direct),
            "chi_lambda_w0_via_chain": _c(chi_chain),
            "cross_check_residual": mp.nstr(residual, _EVAL_DPS,
                                            strip_zeros=False),
            "chi_lambda_w0_at_q_eq_1": chi_at_q_eq_1,
            "sigma_k_dets": sigma_k_dets,
            "sigma_k_conds": sigma_k_conds,
            "w0_det": w0_det,
            "w0_cond": w0_cond,
            "w0_word": word_w0_1based,
        }
    return out


def main() -> None:
    # Witness builder created up front so durationMs measures the
    # actual per-block symbolic compute, not just JSON assembly.
    w = WitnessBuilder(name="option-e-phase1-gram-h6", engine="python")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Option E Phase 1: per-block Hoefsmit-seminormal σ_k matrices "
        "and longest-word matrix ρ_λ(w_0) for each partition λ ⊢ n "
        "(n ∈ {3, 6}) at substrate q_0. Per-block χ_λ(w_0) verified "
        "by cross-checking direct matrix-product trace vs canonical "
        "chain-rule computation. Within-block representation data "
        "needed by Option E Phase 2 (canonical-basis trace ρ_w(K))."
    )

    print("=" * 78)
    print("Option E Phase 1 — Hoefsmit-seminormal per-block ρ_λ at H_6")
    print("=" * 78)
    print(f"q_0 = {Q0_F64:.10f}")
    print()

    q = sp.Symbol("q", positive=True, real=True)

    results: dict[int, dict] = {}

    for n in (3, 6):
        print("-" * 78)
        atom = {3: "H_3 (cross-check baseline)",
                6: "H_6 (deuteron — main deliverable)"}[n]
        print(f"§. {atom}")
        print("-" * 78)
        t0 = time.time()
        # full-precision pin, not the f64 alias
        bd = per_block_data(n, q, Q0_MP)
        elapsed = time.time() - t0
        print(f"  Built in {elapsed:.1f}s")

        total_dim_sq = 0
        max_resid = mp.mpf(0)
        print(f"  {'λ':>20} {'dim_λ':>6} {'χ_λ(w_0) direct':>22} "
              f"{'χ_λ(w_0) chain':>22} {'|Δ|':>10}")
        for shape_t, data in bd.items():
            dim = data["dim"]
            total_dim_sq += dim ** 2
            # the cell is a decimal string; compare the value
            resid = mp.mpmathify(data["cross_check_residual"])
            max_resid = max(max_resid, resid)
            # the two chi cells are decimal strings now; float() for display
            print(f"  {str(shape_t):>20} {dim:>6} "
                  f"{float(data['chi_lambda_w0_direct']):>22.10e} "
                  f"{float(data['chi_lambda_w0_via_chain']):>22.10e} "
                  f"{resid:>10.2e}")
        import math
        n_fact = math.factorial(n)
        print(f"  Σ dim_λ² = {total_dim_sq} (expected: {n}! = {n_fact})")
        print(f"  max |χ_direct − χ_chain| = {max_resid:.2e}  "
              f"({'✓ PASS' if max_resid < 1e-6 else '✗ FAIL'})")
        print()

        results[n] = {
            "blocks": {"_".join(str(s) for s in k): v
                       for k, v in bd.items()},
            "total_dim_sq": total_dim_sq,
            "max_residual": max_resid,
            "compute_time_s": elapsed,
            "passed": max_resid < 1e-6,
        }

    # Witness assembly (builder created at top of main for durationMs accuracy)
    # f64 alias of the pin, recorded as the decimal it is
    w.add_data("q_0_f64", repr(Q0_F64))
    w.add_data("q_0_50dps", str(Q0_MP))
    w.add_data("h3", results[3])
    w.add_data("h6", results[6])
    w.add_assertion(
        "h3_chi_lambda_max_cross_check_residual",
        computed=mp.nstr(results[3]["max_residual"], _EVAL_DPS),
        expected="0", tolerance="1e-6",
        source="χ_λ(w_0) direct == χ_λ(w_0) via chain, for all λ ⊢ 3",
    )
    w.add_assertion(
        "h6_chi_lambda_max_cross_check_residual",
        computed=mp.nstr(results[6]["max_residual"], _EVAL_DPS),
        expected="0", tolerance="1e-6",
        source="χ_λ(w_0) direct == χ_λ(w_0) via chain, for all λ ⊢ 6",
    )
    # κ₂(ρ_λ(σ_k)) = q₀² for EVERY generator in EVERY block of dim > 1.
    # This became visible only once the condition numbers stopped being a
    # binary64 SVD: in float64 the SAME quantity was serialized under three
    # different spellings, so there was nothing to recognise. Exactly, all 47
    # such generators agree with q₀² to ~1e-50.
    #
    # The value is the ratio of the two Hecke eigenvalue magnitudes,
    # |q| / |-q⁻¹| = q², which is what κ₂ would be for a NORMAL matrix. The
    # seminormal ρ_λ(σ_k) is real but not symmetric, so that is an
    # OBSERVATION about the measured singular values, NOT a derivation --
    # normality (or an orthogonal-form conjugation that supplies it) is not
    # established here. Recorded as measured; the mechanism is open.
    _cond_devs = [
        abs(mp.mpf(c) - Q0_MP ** 2) / Q0_MP ** 2
        for res in (results[3], results[6])
        for blk in res["blocks"].values() if blk["dim"] > 1
        for c in blk["sigma_k_conds"]
    ]
    w.add_assertion(
        "generator_condition_number_equals_q0_squared",
        computed=mp.nstr(max(_cond_devs), 12),
        expected="0", tolerance="1e-45",
        source=(f"kappa_2(rho_lambda(sigma_k)) == q_0^2 for all {len(_cond_devs)} "
                "generators in blocks of dim > 1, over lambda |- 3 and lambda |- 6; "
                "max relative deviation. MEASURED, not derived -- see the comment "
                "at the assertion for why normality is not established."),
    )
    w.add_assertion(
        "h3_wedderburn_sum_dim_squared",
        computed=str(results[3]["total_dim_sq"]),
        expected="6", tolerance="0",
        source="Σ_λ dim_λ² = n! = 3! for n=3",
    )
    w.add_assertion(
        "h6_wedderburn_sum_dim_squared",
        computed=str(results[6]["total_dim_sq"]),
        expected="720", tolerance="0",
        source="Σ_λ dim_λ² = n! = 6! for n=6",
    )
    w.save()
    print("Witness saved: option-e-phase1-gram-h6.witness.json")

    overall = results[3]["passed"] and results[6]["passed"]
    sys.exit(0 if overall else 1)


if __name__ == "__main__":
    main()
