#!/usr/bin/env python3
"""
tr_m_q_hecke_seminormal.py — close the character gap completely.

Per docs/audits/2026-05-08-p3-h-3a-divergence.md (cross-check finding),
the partition-sum path

    tr_M(β) = Σ_λ y_λ(q) · χ^λ_q(β)

correctly computes tr_M IFF both (a) y_λ is the canonical Jones-Markov
weight (Wenzl Schur principal specialization — fixed in PR #572 commit
ac7880c5) AND (b) χ^λ_q is the q-deformed Hecke character at q_0
(NOT the q=1 classical Murnaghan–Nakayama character that
`schur_weyl_symbolic.specht_character_atomic` returns).

This script closes (b) by composing two existing modules:

  1. `wedderburn_jones_markov.y_lambda_at(n, q_val=q_0)` — Wenzl y_λ at q_0
  2. `hecke_characters.build_seminormal_matrices(shape, q=q_0)` — Hoefsmit
     seminormal matrices σ_1, …, σ_{n−1} at q_0
  3. `mass_at_3A_proper.chi_lambda_of_word(sigmas, dim, word, ...)` —
     trace of the matrix product over the atomic-braid word

The seminormal-trace χ^λ_q is the **canonical Hecke character**
(Hoefsmit 1974, Mathas 1999 §3.4); χ^λ_q(σ_i) on a SYT pair (T, T')
is the (T, T') matrix entry of σ_i in the seminormal basis, summed
over the diagonal.  At q = 1 it reduces to the classical Murnaghan–
Nakayama character; at q = q_0 it is the q-deformed Hecke character.

The integrated cross-check:

    tr_M_pred(β_atomic(Z, N))
        = Σ_{λ ⊢ 3A} y_λ(q_0) · tr(ρ_λ_q0(β_atomic(Z, N)))

should agree with `markov_trace_recursive` (canonical Markov-axiom
reducer; reference at `atomic-tr-m-mpfr-50dps.witness.json`) to
1e-6 relative or better.  If yes: the character gap is **closed**.

Witness: tr-m-q-hecke-seminormal.witness.json
Audit-only: docs/audits/2026-05-08-q-hecke-character-gap-closure.md

@module computations/tr_m_q_hecke_seminormal
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import os
import sys
import time
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps(max(mp.mp.dps, 80))

from hecke_characters import partitions_of  # noqa: E402
from hoefsmit_mpmath import (BlockCacheMP,  # noqa: E402
                             chi_lambda_of_word_sparse_mp,
                             seminormal_matrices_mp)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q_MP  # noqa: E402  — single source of truth (mpf)
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Was `sp.Float(Q_0_FLOAT, 30)`, i.e. THIRTY DIGITS OF A SEVENTEEN-DIGIT VALUE:
# `q_parameter.Q` is the float64 q₀, so asking sympy for 30 dps could not
# recover precision that was already gone. It read as a high-precision call and
# was not one. `Q_MP` is the mpf q₀ and carries the digits for real.
Q_0_HIGH = Q_MP
# ANCHOR-MATCHED REFERENCE. This producer computes at Q_MP, the PROTON pin, and
# the base-name reference `atomic-tr-m-mpfr-50dps.witness.json` is the MUON one
# (`atomic_tr_m_mpfr_50dps` is tagged `ideal_muon`). Comparing across that
# boundary is the straddle AGENTS.md forbids regardless of size -- and here it
# was the WHOLE measured disagreement:
#
#     atom       vs MUON ref     vs PROTON ref
#     proton      7.8403e-8       4.67e-51
#     deuteron    1.5143e-7       1.86e-50
#     helium-3    2.5171e-7       3.31e-51
#
# The two routes agree EXACTLY, to the serialization limit. The ~1e-7 was never
# a methodological difference between the q-Hecke partition sum and the
# canonical route; it was a proton computation measured against a muon
# reference, and it scaled linearly with strand count because tr_M is a product
# over ~n crossings and so inherits ~n x the 11.5 ppb mu-p q0 gap.
#
# The straddle PREDATES the exact-arithmetic migration: the producer previously
# read `Q_0_FLOAT = q_parameter.Q`, which is the proton float64. Removing the
# float64 noise did not create the discrepancy, it made it legible -- the noise
# had been the same order as the straddle.
_REF_NAME = ("atomic-tr-m-mpfr-50dps-proton.witness.json"
             if str(Q_MP).startswith("1.10997858")
             else "atomic-tr-m-mpfr-50dps.witness.json")
REF_WITNESS = _pb.witness_path(_REF_NAME, HERE)


_Y_LAMBDA_CACHE: dict[int, dict] = {}


def _y_lambda_cached(n: int):
    """Cache y_λ across atoms with the same n (T + ³He both share n=9)."""
    if n not in _Y_LAMBDA_CACHE:
        _Y_LAMBDA_CACHE[n] = y_lambda_at(n, q_val=Q_0_HIGH)
    return _Y_LAMBDA_CACHE[n]


def _load_canonical_tr_m() -> dict:
    """Canonical tr_M reference, kept as mpf.

    The field is named `tr_M_at_q0_50dps` and `float()` threw 33 of those
    digits away on the way in -- while this producer's whole purpose is to
    measure agreement AGAINST that reference to 1e-6.
    """
    if not REF_WITNESS.exists():
        return {}
    data = json.loads(REF_WITNESS.read_text())
    out: dict = {}
    for row in data.get("results", []):
        name = row.get("atom")
        val = row.get("tr_M_at_q0_50dps")
        if name and val is not None:
            out[name] = mp.mpf(str(val))
    return out


def _chi_contribution_worker(args):
    """Top-level worker for multiprocessing.Pool over partitions.

    Computes the per-partition contribution
    `y_λ · χ^λ_q(β_atomic)` for one shape.  Returns the row dict (or
    None if the partition cannot support the generator count, e.g. a
    column partition (1^k) at H_n with k < n_gens_required + 1).
    """
    shape, y_val, q_val, word, n_gens_required = args
    sigmas, dim, _syts = seminormal_matrices_mp(
        tuple(shape), cache=BlockCacheMP(mp.mpf(str(q_val))))
    if dim == 0:
        return None
    try:
        chi = chi_lambda_of_word_sparse_mp(sigmas, dim, word, n_gens_required)
    except IndexError:
        return None
    y_mp = mp.mpf(str(y_val))
    contrib = y_mp * chi
    return {
        "partition": list(shape),
        "dim": int(dim),
        "y_at_q0": fmt(y_mp),
        "chi_q_at_q0": fmt(chi),
        "contribution": fmt(contrib),
        "_contribution_mp": contrib,
    }


def tr_m_via_partition_sum_q_hecke(
    Z: int, N: int, q_val=Q_MP,
    *, include_inter: bool = True, workers: int | None = None,
) -> tuple[mp.mpf, list[dict]]:
    """tr_M(β_atomic(Z, N)) = Σ_{λ ⊢ 3A} y_λ(q) · χ^λ_q(β_atomic).

    Composes:
      - y_λ via Wenzl (numerical-q-from-start for n ≥ 6)
      - χ^λ_q via Hoefsmit seminormal matrices at q_val (numerical)

    `workers` (default None = sequential) enables `multiprocessing.Pool`
    over the per-partition χ^λ_q loop.  Recommended for n ≥ 9 where
    partition count is large (n=9: 30 partitions; n=12: 77).

    Returns (tr_M_value, per_partition_breakdown).
    """
    A = Z + N
    n = 3 * A

    # Build the atomic braid word once.
    word = atom_braid_word_3A(Z, N, include_inter=include_inter)

    # y_λ at q_0 for all λ ⊢ n.
    # Hybrid precision: 30-dps sympy Float for y_λ (preserves
    # accuracy on q^large_exponent Wenzl-Schur terms) + float64 for
    # the seminormal χ^λ_q below.  This combination closes T (n=9)
    # at machine ε in ~2s vs 1.6e-5 for pure float64 or 240+s
    # timeouts for full symbolic.
    y_vals = _y_lambda_cached(n)

    n_gens_required = n - 1
    work = [(shape, y, q_val, word, n_gens_required)
            for shape, y in y_vals.items()]

    rows = []
    if workers and workers > 1 and len(work) > 1:
        with Pool(processes=workers) as pool:
            for row in pool.imap_unordered(_chi_contribution_worker, work):
                if row is not None:
                    rows.append(row)
    else:
        for w in work:
            row = _chi_contribution_worker(w)
            if row is not None:
                rows.append(row)

    total = mp.fsum(r.pop("_contribution_mp") for r in rows)
    return total, rows


# Test bench scoped to A ≤ 2 to keep session-time tractable
# (n=3: ~0.2s for y_λ + small seminormals; n=6: ~3.8s for y_λ +
# 11 seminormal builds).  A = 3 (n = 9) takes ~63s for y_λ + 30
# seminormal builds — feasible but extends the witness substantially.
ATOMIC_TEST_BENCH = [
    (1, 1, 0, "proton"),
    (1, 0, 1, "neutron"),
    (2, 1, 1, "deuteron"),
    (3, 1, 2, "tritium"),
    (3, 2, 1, "helium-3"),
    # ⁴He (4, 2, 2): timed out at 600s — y_λ at n=12 with 30-dps
    # sympy Float requires ~6-13 minutes for the Wenzl-Schur sum
    # over p(12)=77 partitions.  The hybrid 30-dps path is feasible
    # for n ≤ 9; A=4 (n=12) needs either parallelisation
    # (multiprocessing on the 77 partitions) or full 50-dps mpmath
    # (#564's rho_k_h3a_refinement.py path).  Deferred to a
    # follow-up that adds the parallel option.
]


# ── Jing–Liu [jing-liu-2021] (arXiv:2104.06067v1) Thm 2.9 & Thm 2.11 ─────────
# Independent 80-dps closed-form cross-check of Hoefsmit χ^λ_q values (bean qou-4py9).
#
# Convention bridge (no free parameters):
#   Jing–Liu (§1 eq. e:Hecke3):  T_i^2 = (Q - 1) T_i + Q
#   QOU Hoefsmit:                σ_i^2 = (q - q^{-1}) σ_i + 1
# Under Q = q^2 and T_i = q σ_i, (q σ_i)^2 = (q^2 - 1)(q σ_i) + q^2 holds
# identically.  For the parabolic Coxeter element σ_μ = σ_{μ_1} × ⋯ × σ_{μ_r}
# of cycle-type partition μ ⊢ n, the reduced word length is ℓ(σ_μ) = n - l(μ),
# so T_{σ_μ} = q^{n - l(μ)} σ_{σ_μ} and therefore
#
#     χ^λ_{Hoefsmit, q}(σ_{σ_μ}) = q^{-(n - l(μ))} · χ^λ_{JL, μ}(q^2).

def _poly_mul_mp(p: list[mp.mpf], q_poly: list[mp.mpf]) -> list[mp.mpf]:
    """Exact mpmath polynomial product over v^0, v^1, ..."""
    out = [mp.mpf(0)] * (len(p) + len(q_poly) - 1)
    for i, pi in enumerate(p):
        if pi == 0:
            continue
        for j, qj in enumerate(q_poly):
            if qj != 0:
                out[i + j] += pi * qj
    return out


def _coxeter_word_for_partition(mu: tuple[int, ...]) -> list[tuple[mp.mpf, mp.mpf, int]]:
    """Parabolic Coxeter word σ_μ in (c, d, gen_idx) triples for hoefsmit_mpmath."""
    one = mp.mpf(1)
    zero = mp.mpf(0)
    word: list[tuple[mp.mpf, mp.mpf, int]] = []
    offset = 0
    for part in mu:
        for g in range(offset, offset + part - 1):
            word.append((one, zero, g))
        offset += part
    return word


def jing_liu_ab_polynomials_mp(
    mu: tuple[int, ...], Q_val: mp.mpf,
) -> tuple[list[mp.mpf], list[mp.mpf]]:
    """Coefficients a_i(μ; Q) and b_i(μ; Q) for 0 ≤ i ≤ |μ| (Jing–Liu Lemma 2.8):

        (1 - Q^{-1} v)^r ∏_{j=1}^r (1 + v + ⋯ + v^{μ_j - 1}) = ∑_{i=0}^n a_i(μ; Q) v^i,
        ∏_{j=1}^r (Q^{-1} + v^{μ_j} + (1 - Q^{-1})(1 + v + ⋯ + v^{μ_j - 1})) = ∑_{i=0}^n b_i(μ; Q) v^i.
    """
    one = mp.mpf(1)
    inv_Q = one / Q_val
    one_minus_inv_Q = one - inv_Q

    a_poly = [one]
    b_poly = [one]
    lin = [one, -inv_Q]
    for m in mu:
        a_poly = _poly_mul_mp(a_poly, lin)
        a_poly = _poly_mul_mp(a_poly, [one] * m)
        # Factor for b: Q^{-1} + v^m + (1 - Q^{-1}) ∑_{t=0}^{m-1} v^t
        # At t = 0: Q^{-1} + (1 - Q^{-1}) = 1 (plus v^0 if m == 0, impossible for partition parts ≥ 1).
        b_fac = [mp.mpf(0)] * (m + 1)
        b_fac[0] += inv_Q
        b_fac[m] += one
        for t in range(m):
            b_fac[t] += one_minus_inv_Q
        b_poly = _poly_mul_mp(b_poly, b_fac)
    return a_poly, b_poly


def jing_liu_hook_chi_jl_mp(n: int, k: int, mu: tuple[int, ...], Q_val: mp.mpf) -> mp.mpf:
    """Jing–Liu Theorem 2.9 (eq. e:hook) in T_i^2 = (Q - 1)T_i + Q convention:
    χ^{(k, 1^{n-k})}_μ(Q) = (-1)^{n - k + l(μ)} ∑_{i=k}^n a_i(μ; Q) Q^i.
    """
    a_poly, _ = jing_liu_ab_polynomials_mp(mu, Q_val)
    sign = mp.mpf(-1) if ((n - k + len(mu)) % 2 == 1) else mp.mpf(1)
    total = mp.fsum(a_poly[i] * (Q_val ** i) for i in range(k, n + 1))
    return sign * total


def jing_liu_tworow_chi_jl_mp(n: int, k: int, mu: tuple[int, ...], Q_val: mp.mpf) -> mp.mpf:
    """Jing–Liu Theorem 2.11 (eq. e:two) in T_i^2 = (Q - 1)T_i + Q convention:
    for k ≥ n - k ≥ 0, χ^{(k, n-k)}_μ(Q) = Q^{n - l(μ)} (b_k(μ; Q) - b_{k+1}(μ; Q)).
    """
    _, b_poly = jing_liu_ab_polynomials_mp(mu, Q_val)
    bk = b_poly[k] if k < len(b_poly) else mp.mpf(0)
    bk1 = b_poly[k + 1] if (k + 1) < len(b_poly) else mp.mpf(0)
    return (Q_val ** (n - len(mu))) * (bk - bk1)


def cross_check_jing_liu_2021(q_val: mp.mpf) -> dict:
    """80-dps cross-check of Hoefsmit χ^λ_q against Jing–Liu [jing-liu-2021] Thm 2.9 & Thm 2.11."""
    q_mp = mp.mpf(q_val)
    Q_mp = q_mp * q_mp
    cache = BlockCacheMP(q_mp)

    # 1. Verify Jing–Liu's two published worked symbolic examples at Q = q_0^2:
    #    Ex. 2.10 (below Thm 2.9): λ = (6, 1, 1), μ = (2, 2, 2, 2) => 6 Q^2 - 12 Q^3 + 3 Q^4
    ex_hook_jl = jing_liu_hook_chi_jl_mp(8, 6, (2, 2, 2, 2), Q_mp)
    ex_hook_exact = 6 * (Q_mp ** 2) - 12 * (Q_mp ** 3) + 3 * (Q_mp ** 4)
    ex_hook_diff = abs(ex_hook_jl - ex_hook_exact)

    #    Ex. 2.12 (below Thm 2.11): λ = (4, 2), μ = (3, 2, 1) => 2 Q^3 - 3 Q^2 + Q
    ex_tworow_jl = jing_liu_tworow_chi_jl_mp(6, 4, (3, 2, 1), Q_mp)
    ex_tworow_exact = 2 * (Q_mp ** 3) - 3 * (Q_mp ** 2) + Q_mp
    ex_tworow_diff = abs(ex_tworow_jl - ex_tworow_exact)

    # 2. Theorem 2.9: all hook irreps (k, 1^{n-k}) vs Hoefsmit across all μ ⊢ n for n = 3..6
    hook_pairs_checked = 0
    hook_max_abs_diff = mp.mpf(0)
    hook_samples: list[dict] = []
    for n in (3, 4, 5, 6):
        mus = [tuple(p) for p in partitions_of(n)]
        words_by_mu = {mu: _coxeter_word_for_partition(mu) for mu in mus}
        for k in range(1, n + 1):
            shape = (k,) + (1,) * (n - k)
            sigmas, dim, _ = seminormal_matrices_mp(shape, cache=cache)
            for mu in mus:
                word = words_by_mu[mu]
                chi_hoef = (
                    mp.mpf(dim) if not word
                    else chi_lambda_of_word_sparse_mp(sigmas, dim, word, n - 1)
                )
                chi_jl_rescaled = (q_mp ** (-(n - len(mu)))) * jing_liu_hook_chi_jl_mp(n, k, mu, Q_mp)
                diff = abs(chi_hoef - chi_jl_rescaled)
                if diff > hook_max_abs_diff:
                    hook_max_abs_diff = diff
                hook_pairs_checked += 1
                if (n, shape, mu) in (
                    (3, (2, 1), (3,)),
                    (6, (4, 1, 1), (3, 2, 1)),
                    (6, (3, 1, 1, 1), (6,)),
                ):
                    hook_samples.append({
                        "n": n,
                        "lambda": list(shape),
                        "mu": list(mu),
                        "dim": int(dim),
                        "hoefsmit_chi_q": fmt(chi_hoef),
                        "jing_liu_thm2_9_rescaled": fmt(chi_jl_rescaled),
                        "abs_diff": fmt(diff),
                    })

    # 3. Theorem 2.11: all two-row irreps (k, n-k) (k ≥ n-k ≥ 0) + cumulative sum eq. (240)
    #    vs Hoefsmit across all μ ⊢ n for n = 3..8 (covers n ≥ 4 two-row Temperley–Lieb blocks)
    tworow_pairs_checked = 0
    tworow_max_abs_diff = mp.mpf(0)
    cumsum_checks = 0
    cumsum_max_abs_diff = mp.mpf(0)
    tworow_samples: list[dict] = []
    for n in (3, 4, 5, 6, 7, 8):
        mus = [tuple(p) for p in partitions_of(n)]
        words_by_mu = {mu: _coxeter_word_for_partition(mu) for mu in mus}
        sem_by_i: dict[int, tuple] = {}
        for i in range(0, n // 2 + 1):
            shape = (n - i,) if i == 0 else (n - i, i)
            sem_by_i[i] = (shape, *seminormal_matrices_mp(shape, cache=cache)[:2])
        for mu in mus:
            word = words_by_mu[mu]
            _, b_poly = jing_liu_ab_polynomials_mp(mu, Q_mp)
            hoef_sum = mp.mpf(0)
            for i in range(0, n // 2 + 1):
                k = n - i
                shape, sigmas, dim = sem_by_i[i]
                chi_hoef = (
                    mp.mpf(dim) if not word
                    else chi_lambda_of_word_sparse_mp(sigmas, dim, word, n - 1)
                )
                hoef_sum += chi_hoef
                chi_jl_rescaled = (q_mp ** (-(n - len(mu)))) * jing_liu_tworow_chi_jl_mp(n, k, mu, Q_mp)
                diff = abs(chi_hoef - chi_jl_rescaled)
                if diff > tworow_max_abs_diff:
                    tworow_max_abs_diff = diff
                tworow_pairs_checked += 1
                if (n, shape, mu) in (
                    (4, (2, 2), (4,)),
                    (6, (4, 2), (3, 2, 1)),
                    (6, (3, 3), (3, 3)),
                    (8, (5, 3), (4, 3, 1)),
                    (8, (4, 4), (4, 4)),
                ):
                    tworow_samples.append({
                        "n": n,
                        "lambda": list(shape),
                        "mu": list(mu),
                        "dim": int(dim),
                        "hoefsmit_chi_q": fmt(chi_hoef),
                        "jing_liu_thm2_11_rescaled": fmt(chi_jl_rescaled),
                        "abs_diff": fmt(diff),
                    })
            # Thm 2.11 eq. (2): ∑_{i=0}^{[n/2]} χ^{(n-i, i)}_μ(Q) = Q^{n - l(μ)} b_{[n/2]}(μ; Q)
            # Rescaled by q^{-(n - l(μ))}: ∑_{i=0}^{[n/2]} χ_{Hoefsmit} = q^{n - l(μ)} b_{[n/2]}(μ; q^2)
            jl_cumsum_rescaled = (q_mp ** (n - len(mu))) * b_poly[n // 2]
            cdiff = abs(hoef_sum - jl_cumsum_rescaled)
            if cdiff > cumsum_max_abs_diff:
                cumsum_max_abs_diff = cdiff
            cumsum_checks += 1

    return {
        "source": "[jing-liu-2021] arXiv:2104.06067v1, Lemma 2.8, Theorem 2.9 (hooks), Theorem 2.11 (two-row)",
        "convention_bridge": "T_i = q * sigma_i, Q = q^2 => chi_Hoefsmit(sigma_mu; q) = q^{-(n - l(mu))} * chi_JL(T_sigma_mu; q^2)",
        "compute_dps": int(mp.mp.dps),
        "published_examples": {
            "ex_2_10_hook_6_1_1_on_2_2_2_2_abs_diff": fmt(ex_hook_diff),
            "ex_2_12_tworow_4_2_on_3_2_1_abs_diff": fmt(ex_tworow_diff),
        },
        "thm_2_9_hooks": {
            "n_range": [3, 4, 5, 6],
            "pairs_checked": hook_pairs_checked,
            "max_abs_diff": fmt(hook_max_abs_diff),
            "samples": hook_samples,
        },
        "thm_2_11_two_row": {
            "n_range": [3, 4, 5, 6, 7, 8],
            "pairs_checked": tworow_pairs_checked,
            "max_abs_diff": fmt(tworow_max_abs_diff),
            "cumulative_sum_identities_checked": cumsum_checks,
            "cumulative_sum_max_abs_diff": fmt(cumsum_max_abs_diff),
            "samples": tworow_samples,
        },
        "_ex_hook_diff": ex_hook_diff,
        "_ex_tworow_diff": ex_tworow_diff,
        "_hook_max_abs_diff": hook_max_abs_diff,
        "_tworow_max_abs_diff": tworow_max_abs_diff,
        "_cumsum_max_abs_diff": cumsum_max_abs_diff,
    }


def main() -> int:
    set_compute_dps(max(mp.mp.dps, 80))
    canonical = _load_canonical_tr_m()
    if not canonical:
        print("ERROR: canonical reference witness not loadable", file=sys.stderr)
        return 1

    builder = (
        WitnessBuilder(
            name="tr-m-q-hecke-seminormal",
            engine="mpmath",
        )
        .set_description(
            "Closes the character gap in the partition-sum tr_M path: "
            "tr_M(β) = Σ_λ y_λ(q) · χ^λ_q(β) via canonical Wenzl y_λ "
            "(numerical-q-from-start) + Hoefsmit seminormal χ^λ_q at q_0, "
            "and cross-checks Hoefsmit χ^λ_q at 80 dps against the closed-form "
            "vertex-operator formulas of Jing–Liu [jing-liu-2021] Theorem 2.9 "
            "(hook partitions) and Theorem 2.11 (two-row partitions). "
            "Cross-checks tr_M against `markov_trace_recursive` reference "
            "(atomic-tr-m-mpfr-50dps-proton.witness.json)."
        )
    )

    rows = []
    all_passed = True
    for A_param, Z, N, name in ATOMIC_TEST_BENCH:
        canonical_val = canonical.get(name)
        # No canonical reference yet for ⁴He+ at canonical-word
        # convention (per convention_status="DEPRECATED_DISJOINT" in
        # PR #564's atomic-tr-m-helium4.witness.json).  Compute the
        # value via this PR's hybrid-precision path and emit it as
        # the FIRST canonical-word reference (no rel-err comparison).
        t0 = time.monotonic()
        try:
            total, breakdown = tr_m_via_partition_sum_q_hecke(
                Z, N, q_val=Q_MP
            )
            elapsed = time.monotonic() - t0
            new_abs = abs(total)
            if canonical_val is None:
                # No canonical reference: this PR establishes the first
                # canonical-word value.  Future regeneration of
                # atomic-tr-m-mpfr-50dps.witness.json will validate
                # against this number.
                rel_err = mp.nan
                agrees_1e6 = False
                agrees_1e3 = False
                row = {
                    "atom": name,
                    "Z": Z,
                    "N": N,
                    "A": Z + N,
                    "n_strands": 3 * (Z + N),
                    "canonical_abs_tr_M": None,
                    "canonical_status": (
                        "no canonical-word reference yet — this PR's "
                        "hybrid-precision value is the FIRST canonical "
                        "(operator-valued interface) tr_M for this atom"
                    ),
                    "q_hecke_partition_sum": fmt(total),
                    "q_hecke_abs": fmt(new_abs),
                    "elapsed_sec": f"{elapsed:.3f}",
                    "non_zero_partitions": len(breakdown),
                    "top_3_contributions": sorted(
                        breakdown,
                        key=lambda r: -abs(mp.mpf(r["contribution"])),
                    )[:3],
                }
                rows.append(row)
                builder.add_assertion(
                    name=f"q_hecke_seminormal_value_finite[{name}]",
                    computed=str(mp.mpf(0) < new_abs < mp.mpf("1e6")),
                    expected="True",
                )
                print(f"  {name}: canonical=N/A (first-time computation), "
                      f"q-Hecke seminormal={mp.nstr(new_abs, 12)}, {elapsed:.2f}s",
                      file=sys.stderr)
                continue
            rel_err = (
                abs(new_abs - canonical_val) / canonical_val
                if canonical_val != 0
                else mp.inf
            )
            agrees_1e6 = rel_err < mp.mpf("1e-6")
            agrees_1e3 = rel_err < mp.mpf("1e-3")
            rows.append({
                "atom": name,
                "Z": Z,
                "N": N,
                "A": Z + N,
                "n_strands": 3 * (Z + N),
                "canonical_abs_tr_M": fmt(canonical_val),
                "q_hecke_partition_sum": fmt(total),
                "q_hecke_abs": fmt(new_abs),
                "rel_err_vs_canonical": fmt(rel_err),
                "agrees_to_1e_minus_3": bool(agrees_1e3),
                "agrees_to_1e_minus_6": bool(agrees_1e6),
                "elapsed_sec": f"{elapsed:.3f}",
                "non_zero_partitions": len(breakdown),
                "top_3_contributions": sorted(
                    breakdown,
                    key=lambda r: -abs(mp.mpf(r["contribution"])),
                )[:3],
            })
            builder.add_assertion(
                name=f"q_hecke_seminormal_closes_gap[{name}]_to_1e-3",
                computed=str(agrees_1e3),
                expected="True",
            )
            builder.add_assertion(
                name=f"q_hecke_seminormal_closes_gap[{name}]_to_1e-6",
                computed=str(agrees_1e6),
                expected="True",
            )
            if not agrees_1e3:
                all_passed = False
            print(f"  {name}: canonical={mp.nstr(canonical_val, 6)}, "
                  f"q-Hecke seminormal={mp.nstr(new_abs, 6)}, "
                  f"rel_err={mp.nstr(rel_err, 3)}, {elapsed:.2f}s",
                  file=sys.stderr)
        except Exception as exc:
            elapsed = time.monotonic() - t0
            rows.append({
                "atom": name, "Z": Z, "N": N,
                "error": f"{type(exc).__name__}: {exc}",
                "elapsed_sec": f"{elapsed:.3f}",
            })
            print(f"  {name}: ERROR after {elapsed:.2f}s — "
                  f"{type(exc).__name__}: {exc}", file=sys.stderr)
            all_passed = False

    t_jl = time.monotonic()
    jl_data = cross_check_jing_liu_2021(Q_MP)
    dt_jl = time.monotonic() - t_jl
    tol_jl = mp.mpf("1e-65")
    ex_ok = (jl_data.pop("_ex_hook_diff") < tol_jl) and (jl_data.pop("_ex_tworow_diff") < tol_jl)
    hook_ok = jl_data.pop("_hook_max_abs_diff") < tol_jl
    tworow_ok = jl_data.pop("_tworow_max_abs_diff") < tol_jl
    cumsum_ok = jl_data.pop("_cumsum_max_abs_diff") < tol_jl
    jl_data["elapsed_sec"] = f"{dt_jl:.3f}"

    builder.add_assertion(
        name="jing_liu_2021_published_examples_agree_80dps",
        computed=str(bool(ex_ok)),
        expected="True",
    )
    builder.add_assertion(
        name="jing_liu_2021_thm2_9_hooks_match_hoefsmit_n3_to_6_80dps",
        computed=str(bool(hook_ok)),
        expected="True",
    )
    builder.add_assertion(
        name="jing_liu_2021_thm2_11_tworow_match_hoefsmit_n3_to_8_80dps",
        computed=str(bool(tworow_ok)),
        expected="True",
    )
    builder.add_assertion(
        name="jing_liu_2021_thm2_11_tworow_cumulative_sum_n3_to_8_80dps",
        computed=str(bool(cumsum_ok)),
        expected="True",
    )
    if not (ex_ok and hook_ok and tworow_ok and cumsum_ok):
        all_passed = False
    print(
        f"  [jing-liu-2021] Thm 2.9 hooks ({jl_data['thm_2_9_hooks']['pairs_checked']} pairs, "
        f"max_diff={jl_data['thm_2_9_hooks']['max_abs_diff']}) & "
        f"Thm 2.11 two-row ({jl_data['thm_2_11_two_row']['pairs_checked']} pairs, "
        f"max_diff={jl_data['thm_2_11_two_row']['max_abs_diff']}) in {dt_jl:.2f}s",
        file=sys.stderr,
    )

    builder.add_data("cross_check_table", rows)
    builder.add_data("jing_liu_2021_cross_check", jl_data)
    builder.add_data(
        "method",
        {
            "formula": "tr_M(β) = Σ_{λ ⊢ 3A} y_λ(q_0) · χ^λ_q(β_atomic)",
            "y_lambda_source": (
                "wedderburn_jones_markov.y_lambda_at — Wenzl Schur "
                "principal specialization with numerical-q-from-start "
                "(closes the WEIGHT bug; PR #572 ac7880c5)"
            ),
            "chi_q_source": (
                "hoefsmit_mpmath.seminormal_matrices_mp + "
                "chi_lambda_of_word_sparse_mp — Hoefsmit "
                "seminormal matrices at q = q_0, cross-checked at 80 dps "
                "against Jing–Liu [jing-liu-2021] Thm 2.9 (hooks) and "
                "Thm 2.11 (two-row partitions)"
            ),
            "canonical_reference": (
                "atomic-tr-m-mpfr-50dps-proton.witness.json — produced by "
                "markov_trace_recursive / Hoefsmit-Wenzl bridge at proton pin."
            ),
            "tolerance_tight": "1e-6 relative (full-precision agreement)",
            "tolerance_loose": "1e-3 relative (engineering tolerance)",
        },
    )

    out_path = builder.save()
    print(f"\n  Wrote {out_path}", file=sys.stderr)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
