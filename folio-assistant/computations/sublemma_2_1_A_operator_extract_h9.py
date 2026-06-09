#!/usr/bin/env python3
"""Sub-lemma 2.1 operator-valued A^λ_{ξν}(I_2) extraction at H_9.

Multi-interface extension of `sublemma_2_1_A_operator_extract.py`
(deuteron / H_6 single-interface case, verified at machine ε for all
11 λ ⊢ 6).

Scaffold described in
`docs/audits/2026-05-15-sublemma-2-1-h9-multi-interface-extension.md`.
Implementation strategy:

  For a 2-interface atomic braid β_K ∈ H_9 written as

      β_K = W_inner · I_2 · β_3,
        W_inner = β_1 · I_1 · β_2 ∈ H_6
        β_3 ∈ H_3
        I_2 ∈ {I_pp, I_pn, I_nn}     (the OUTER interface)

  apply Sub-lemma 2.1 at H_9 ↓ H_6 × H_3:

      χ^λ(β_K) = Σ_{ξ⊢6, ν⊢3} c^λ_{ξν} · Tr_{V_ξ ⊗ V_ν}(
          A^λ_{ξν}(I_2) · (ρ_ξ(W_inner) ⊗ ρ_ν(β_3))).

This probe extracts A^λ_{ξν}(I_2) for a given I_2 ∈ {pn, nn, pp} via
bilinear-system inversion across K_6 × K_3 test pairs.

Scope (Phase 1, tractable):
  - K_6 = K_3 = 12 H_6 / H_3 test words → 144 equations per λ.
  - Some large-dim λ (e.g. (4,3,1,1) with d_λ=216 → 3390 unknowns)
    are UNDER-determined at this K; we report rank deficiency.
  - Verifies machine-ε agreement of bilinear-system reconstruction
    for the OVER-determined low-dim λ subset.

Phase 2 (deferred): expand K to 60+ test words to make ALL λ ⊢ 9
over-determined for the high-dim (ξ,ν)=( (3,2,1), * ) blocks.
That's substantial compute (~hours); deferred.

Output: sublemma-2-1-A-operator-extract-h9-{pn|nn|pp}.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from char_fast import _compiled_sigmas, chi_lambda_fast  # noqa: E402
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402


H = float(Q0 - 1 / Q0)  # h = q − q⁻¹ at q_0

# Interface generator coefficients (c, d) acting at strand index n_1-1
# (between H_n_1 and H_n_2 in the embedding H_{n_1+n_2}):
#   pp:   (1, 0)        — bare σ
#   pn:   (1, -h/2)     — averaged
#   nn:   (1, -h)       — σ⁻¹ via Hecke
INTERFACE_COEFS = {
    "pp": (1.0, 0.0),
    "pn": (1.0, -H / 2),
    "nn": (1.0, -H),
}


def shape_dim(shape: tuple) -> int:
    """Hoefsmit dimension dim V_shape via char_fast cache."""
    _, d = _compiled_sigmas(shape, "double")
    return d


def evaluate_word_matrix(shape: tuple, word: list, q_val: float = None) -> np.ndarray:
    """Evaluate Π_i (c_i σ_{g_i} + d_i I) on V_shape at q_val."""
    if q_val is None:
        q_val = float(Q0)
    sigmas, dim = _compiled_sigmas(shape, "double")
    if dim == 0:
        return np.zeros((0, 0), dtype=complex)
    sigma_mats = [np.asarray(fn(q_val), dtype=complex) for fn in sigmas]
    I = np.eye(dim, dtype=complex)
    M = I.copy()
    for c, d, g in word:
        if g >= len(sigma_mats):
            return np.zeros((dim, dim), dtype=complex)
        M = M @ (complex(c) * sigma_mats[g] + complex(d) * I)
    return M


def with_interface_h9(word_6: list, word_3: list, interface: str,
                      n1: int = 6) -> list:
    """Build the H_9 word: W_inner · I_2 · β_3 with I_2 at strand n_1-1."""
    if interface not in INTERFACE_COEFS:
        raise ValueError(f"unknown interface {interface!r}; "
                         f"expected one of {sorted(INTERFACE_COEFS)}")
    int_c, int_d = INTERFACE_COEFS[interface]
    out = list(word_6)
    out.append((int_c, int_d, n1 - 1))
    out += [(c, d, g + n1) for (c, d, g) in word_3]
    return out


def make_h6_test_words() -> list[list]:
    """Diverse H_6 elements spanning End(V_ξ) for low-dim ξ ⊢ 6.

    Generators σ_0 .. σ_4 (5 generators). K = 12.
    """
    return [
        [],                                                      # 1
        [(1.0, 0.0, 0)],                                         # σ_0
        [(1.0, 0.0, 2)],                                         # σ_2
        [(1.0, 0.0, 4)],                                         # σ_4
        [(1.0, 0.0, 0), (1.0, 0.0, 1)],                          # σ_0 σ_1
        [(1.0, 0.0, 1), (1.0, 0.0, 0)],                          # σ_1 σ_0
        [(1.0, 0.0, 2), (1.0, 0.0, 3)],                          # σ_2 σ_3
        [(1.0, 0.0, 3), (1.0, 0.0, 2)],                          # σ_3 σ_2
        [(1.0, -H, 0)],                                          # σ_0 - h
        [(1.0, -H / 2, 1)],                                      # σ_1 - h/2
        [(1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0)],           # trefoil at low
        [(1.0, 0.0, 2), (1.0, 0.0, 3), (1.0, 0.0, 2)],           # trefoil at mid
    ]


def make_h3_test_words() -> list[list]:
    """Diverse H_3 elements (matches the deuteron-extract H_3 word set)."""
    return [
        [],
        [(1.0, 0.0, 0)],
        [(1.0, 0.0, 1)],
        [(1.0, 0.0, 0), (1.0, 0.0, 1)],
        [(1.0, 0.0, 1), (1.0, 0.0, 0)],
        [(1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0)],
        [(1.0, -H, 0)],
        [(1.0, -H / 2, 1)],
        [(1.0, 0.0, 0), (1.0, -H, 1)],
        [(1.0, -H, 0), (1.0, -H / 2, 1)],
        [(1.0, 0.0, 0), (1.0, 0.0, 0)],
        [(1.0, 0.0, 1), (1.0, 0.0, 1)],
    ]


def _reduced_word(perm: tuple) -> list[int]:
    """Reduced expression of `perm` in adjacent transpositions s_0..s_{n-2}.

    Bubble-sort `perm` to the identity, recording each adjacent swap
    index; the recorded indices form a reduced word (length = Coxeter
    length = #inversions).
    """
    p = list(perm)
    n = len(p)
    w: list[int] = []
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                w.append(i)
                changed = True
    return w


def make_h6_perm_basis() -> list[list]:
    """Full S_6 permutation basis as H_6 test words (720 words).

    By the double-centralizer theorem, ρ_ξ(H_6) = End(V_ξ) for every
    irreducible V_ξ, so {ρ_ξ(T_w) : w ∈ S_6} spans End(V_ξ) EXACTLY
    (verified: span rank = d_ξ² for all ξ ⊢ 6). The hand-picked
    12-word `make_h6_test_words` family is a degenerate spanning set
    (reaches only ~97/256 of End(V_{(3,2,1)})), which is why the
    Phase-1 H_9 extracts were rank-deficient. This basis closes that.
    """
    import itertools
    return [[(1.0, 0.0, g) for g in _reduced_word(perm)]
            for perm in itertools.permutations(range(6))]


def make_h3_perm_basis() -> list[list]:
    """Full S_3 permutation basis as H_3 test words (6 words)."""
    import itertools
    return [[(1.0, 0.0, g) for g in _reduced_word(perm)]
            for perm in itertools.permutations(range(3))]


def _to_braid_terms(
    word: list, h_num: float
) -> list[tuple[float, list[tuple[int, int]]]]:
    """Expand a `(c, d, gen)` word into native braid TERMS `[(coeff, braid)]`.

    Each `braid` is `[(sign, gen_1based)]`; by linearity of the character,
    `χ^λ(word) = Σ_terms coeff · χ^λ(braid)`.  Crossing dictionary:

      σ        (c=1, d=0)    → 1 term: (+1) generator
      σ⁻¹      (c=1, d=−h)   → 1 term: (−1) generator
      averaged (c=1, d=−h/2) → σ − (h/2)·1, i.e. 2 terms:
                                 σ branch (+1 generator, coeff 1) and
                                 identity branch (no generator, coeff −h/2)

    An averaged crossing doubles the term count.  With one outer interface
    crossing I_2 the result has 1 term (pp/nn — pure braid) or 2 terms
    (pn — the averaged color-blind crossing).  This is what lets `--native`
    cover the pn interface (needed for ³He) without leaving the fast
    `chi_lambdas_braid` path: each branch is a pure braid word the Rust
    kernel evaluates directly (the identity branch is the empty braid,
    χ^λ(1) = d_λ).  Raises on any unrecognised crossing so convention
    drift fails loudly.
    """
    tol = 1e-7
    h_val = float(h_num)
    # Cast (c, d) to float so the tolerance checks return Python bools even
    # if they arrive as sympy Float/Rational rather than plain floats.
    terms: list[tuple[float, list[tuple[int, int]]]] = [(1.0, [])]
    for c, d, g in word:
        c_val, d_val = float(c), float(d)
        if abs(c_val - 1.0) < tol and abs(d_val) < tol:
            terms = [(co, bw + [(1, g + 1)]) for co, bw in terms]
        elif abs(c_val - 1.0) < tol and abs(d_val + h_val) < tol:
            terms = [(co, bw + [(-1, g + 1)]) for co, bw in terms]
        elif abs(c_val - 1.0) < tol and abs(d_val + h_val / 2) < tol:
            split: list[tuple[float, list[tuple[int, int]]]] = []
            for co, bw in terms:
                split.append((co, bw + [(1, g + 1)]))       # σ branch
                split.append((co * (-h_val / 2.0), bw))      # identity branch
            terms = split
        else:
            raise ValueError(
                f"--native: unrecognised crossing (c={c}, d={d}) at gen={g}; "
                f"expected σ (d=0), σ⁻¹ (d=−h), or averaged (d=−h/2)."
            )
    return terms


def _to_braid_word(word: list, h_num: float) -> list[tuple[int, int]]:
    """Single-term (pure-braid) view of `_to_braid_terms`.

    Valid only when `word` has no averaged crossing; raises otherwise.
    Retained for callers that need one braid word rather than a sum.
    """
    terms = _to_braid_terms(word, h_num)
    if len(terms) != 1 or abs(terms[0][0] - 1.0) > 1e-9:
        raise ValueError(
            "word contains an averaged crossing — use _to_braid_terms "
            "(linearity expansion), not _to_braid_word."
        )
    return terms[0][1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--interface", choices=sorted(INTERFACE_COEFS),
                        default="nn",
                        help="outer interface I_2 (default: nn, "
                             "relevant for tritium = β_p·I_pn·β_n·I_nn·β_n)")
    parser.add_argument("--rank-tol", type=float, default=1e-8,
                        help="singular-value cutoff for under-determined "
                             "system detection (default: 1e-8)")
    parser.add_argument("--full-basis", action="store_true",
                        help="use the full S_6 (720) × S_3 (6) permutation "
                             "basis as test words — spans End(V_ξ) exactly, "
                             "making ALL λ ⊢ 9 over-determined and full-rank. "
                             "Default uses the 12+12 hand-picked family "
                             "(Phase 1, under-determined for high-dim λ).")
    parser.add_argument("--native", action="store_true",
                        help="evaluate χ^λ via pyhecke_native.chi_lambdas_braid "
                             "(~900× faster; all interfaces pp/nn/pn — pn's "
                             "averaged crossing is handled by linearity, 2 "
                             "braid terms). Makes --full-basis tractable "
                             "(~30s vs ~7h).")
    args = parser.parse_args()

    interface = args.interface
    parts_6 = partitions_of(6)
    parts_3 = partitions_of(3)
    parts_9 = partitions_of(9)
    lr_table = get_lr_table(6, 3)

    if args.full_basis:
        test_words_6 = make_h6_perm_basis()
        test_words_3 = make_h3_perm_basis()
    else:
        test_words_6 = make_h6_test_words()
        test_words_3 = make_h3_test_words()
    K_6 = len(test_words_6)
    K_3 = len(test_words_3)

    print("=" * 96)
    print(f"  Sub-lemma 2.1 operator-valued A^λ_{{ξν}}(I_2={interface}) at H_9")
    print("=" * 96)
    print(f"  q_0 = {float(Q0):.10f}, h = {H:.10f}")
    print(f"  Interface coefs (c, d) = {INTERFACE_COEFS[interface]}")
    print(f"  K_6 = {K_6} H_6 test words, K_3 = {K_3} H_3 test words "
          f"→ K_6·K_3 = {K_6 * K_3} test pairs")
    print()

    # ── Pre-compute ρ_ξ(W_6[i]) for each H_6 test word and each ξ ⊢ 6
    t0 = time.monotonic()
    print(f"  [1/3] Pre-computing ρ_ξ(W_6[i]) at q_0 for {K_6} × {len(parts_6)} "
          f"= {K_6 * len(parts_6)} matrices...")
    rho_xi: dict[tuple[int, tuple], np.ndarray] = {}
    for i, w in enumerate(test_words_6):
        for xi in parts_6:
            rho_xi[(i, xi)] = evaluate_word_matrix(xi, w)
    print(f"      done in {time.monotonic() - t0:.1f}s")

    # ── Pre-compute ρ_ν(W_3[j]) for each H_3 test word and each ν ⊢ 3
    t0 = time.monotonic()
    print(f"  [2/3] Pre-computing ρ_ν(W_3[j]) at q_0 for {K_3} × {len(parts_3)} "
          f"= {K_3 * len(parts_3)} matrices...")
    rho_nu: dict[tuple[int, tuple], np.ndarray] = {}
    for j, w in enumerate(test_words_3):
        for nu in parts_3:
            rho_nu[(j, nu)] = evaluate_word_matrix(nu, w)
    print(f"      done in {time.monotonic() - t0:.1f}s")

    # ── Compute χ^λ(W_6[i] · I_2 · W_3[j]) for each (i, j, λ)
    t0 = time.monotonic()
    n_chi = K_6 * K_3 * len(parts_9)
    chi_lam: dict[tuple[int, int, tuple], complex] = {}
    progress = 0
    if args.native:
        import pyhecke_native as _pn
        q_native = float(Q0)
        parts9_lists = [list(l) for l in parts_9]
        print(f"  [3/3] Computing χ^λ(β_K) at H_9 for {n_chi} (i, j, λ) "
              f"triples via pyhecke_native (batch over λ)...")
        for i, w6 in enumerate(test_words_6):
            for j, w3 in enumerate(test_words_3):
                # Sum the linearity terms (1 for pp/nn, 2 for the pn
                # averaged crossing); each branch is a pure braid word.
                terms = _to_braid_terms(
                    with_interface_h9(w6, w3, interface), H)
                acc = [0.0] * len(parts9_lists)
                for coeff, braid in terms:
                    vals = _pn.chi_lambdas_braid(parts9_lists, braid, q_native)
                    for k, v in enumerate(vals):
                        acc[k] += coeff * v
                for lam, v in zip(parts_9, acc):
                    chi_lam[(i, j, lam)] = complex(v)
                progress += len(parts_9)
                if progress % 6000 == 0 or progress == n_chi:
                    pct = 100 * progress / n_chi
                    print(f"      progress: {progress}/{n_chi} ({pct:.1f}%) "
                          f"t={time.monotonic()-t0:.1f}s")
    else:
        print(f"  [3/3] Computing χ^λ(β_K) at H_9 for {n_chi} (i, j, λ) triples...")
        for i, w6 in enumerate(test_words_6):
            for j, w3 in enumerate(test_words_3):
                comb = with_interface_h9(w6, w3, interface)
                for lam in parts_9:
                    chi_lam[(i, j, lam)] = chi_lambda_fast(lam, comb)
                progress += len(parts_9)
                if progress % 600 == 0 or progress == n_chi:
                    pct = 100 * progress / n_chi
                    print(f"      progress: {progress}/{n_chi} ({pct:.1f}%) "
                          f"t={time.monotonic()-t0:.1f}s")
    chi_time = time.monotonic() - t0
    print(f"      done in {chi_time:.1f}s")

    # ── Per-λ bilinear-system inversion
    print()
    print("  Per-λ bilinear A^λ_{ξν}(I_2) extraction:")
    print(f"  {'λ ⊢ 9':<22} {'dim_λ':>6} {'support':>9} {'unknowns':>10} "
          f"{'rank/eqs':>10} {'rel res':>10}  status")
    print("  " + "-" * 90)

    results_per_lambda = {}
    n_overdet = 0
    n_underdet = 0
    n_consistent = 0
    for lam in parts_9:
        # Support list (ξ, ν, c^λ_{ξν}, d_ξ, d_ν)
        pairs = []
        for xi in parts_6:
            for nu in parts_3:
                c = lr_table.get((xi, nu, lam), 0)
                if c > 0:
                    d_xi = shape_dim(xi)
                    d_nu = shape_dim(nu)
                    pairs.append({"xi": xi, "nu": nu, "c": c,
                                  "d_xi": d_xi, "d_nu": d_nu,
                                  "n_entries": (d_xi * d_nu) ** 2})
        if not pairs:
            continue

        n_unknowns = sum(p["n_entries"] for p in pairs)
        n_eq = K_6 * K_3
        underdet = n_unknowns > n_eq

        # Build M @ vec(A) = rhs system, K_6·K_3 × n_unknowns
        M = np.zeros((n_eq, n_unknowns), dtype=complex)
        rhs = np.zeros(n_eq, dtype=complex)
        offsets = [0]
        for p in pairs:
            offsets.append(offsets[-1] + p["n_entries"])

        for k_idx, (i, j) in enumerate((i, j) for i in range(K_6) for j in range(K_3)):
            for p_idx, p in enumerate(pairs):
                B_xi = rho_xi[(i, p["xi"])]
                B_nu = rho_nu[(j, p["nu"])]
                X = np.kron(B_xi, B_nu)
                coef = X.T.flatten()
                M[k_idx, offsets[p_idx]:offsets[p_idx] + p["n_entries"]] = coef
            rhs[k_idx] = chi_lam[(i, j, lam)]

        # Least-squares solve; rcond=args.rank_tol thresholds the
        # singular-value cutoff for rank determination, so the reported
        # `rank` is consistent with --rank-tol.
        sol, residuals, rank, sv = np.linalg.lstsq(M, rhs, rcond=args.rank_tol)
        pred = M @ sol
        rhs_scale = max(float(np.mean(np.abs(rhs))), 1e-12)
        max_abs_res = float(np.max(np.abs(pred - rhs)))
        max_rel = max_abs_res / rhs_scale
        consistent = max_rel < 1e-6

        if underdet:
            status = "under"
            n_underdet += 1
        elif consistent:
            status = "✓"
            n_overdet += 1
            n_consistent += 1
        else:
            status = "✗"
            n_overdet += 1

        d_lam = shape_dim(lam)
        support_str = f"{len(pairs)} pairs"
        print(f"  {str(lam):<22} {d_lam:>6} {support_str:>9} {n_unknowns:>10} "
              f"{rank:>5}/{n_eq:<4} {max_rel:>10.2e}  {status}")

        # Reshape sol into per-pair A matrices.  Emit FULL matrix
        # entries (real and imag) in the witness so downstream
        # verification probes (sublemma_2_1_h9_tritium_verify.py) can
        # apply A^λ_{ξν}(I_2) directly without re-extracting.
        A_per_pair = {}
        for p_idx, p in enumerate(pairs):
            d = p["d_xi"] * p["d_nu"]
            A_flat = sol[offsets[p_idx]:offsets[p_idx] + p["n_entries"]]
            A_mat = A_flat.reshape((d, d), order="C")
            A_per_pair[f"({p['xi']},{p['nu']})"] = {
                "matrix_re": [[float(A_mat[a, b].real) for b in range(d)] for a in range(d)],
                "matrix_im": [[float(A_mat[a, b].imag) for b in range(d)] for a in range(d)],
                "frobenius_norm": float(np.linalg.norm(A_mat)),
                "max_abs_entry": float(np.max(np.abs(A_mat))),
                "trace": complex(np.trace(A_mat)).real,
                "is_scalar_multiple_of_id": bool(
                    d == 1 or
                    (np.linalg.norm(A_mat - (np.trace(A_mat) / d) * np.eye(d)) < 1e-9)
                ),
                "c_lr": p["c"],
                "d_xi": p["d_xi"], "d_nu": p["d_nu"],
            }

        results_per_lambda[str(list(lam))] = {
            "support_size": len(pairs),
            "n_unknowns": int(n_unknowns),
            "n_equations": int(n_eq),
            "rank": int(rank),
            "underdetermined": bool(underdet),
            "max_relative_residual": max_rel,
            "consistent": bool(consistent),
            "A_per_pair": A_per_pair,
        }

    print()
    print(f"  Summary at K_6={K_6}, K_3={K_3}, I_2={interface}:")
    print(f"    Over-determined λ:                {n_overdet}/{len(parts_9)}")
    print(f"    Of which consistent (rel res < 1e-6): {n_consistent}/{n_overdet}")
    print(f"    Under-determined λ:               {n_underdet}/{len(parts_9)}")
    print()

    # ── Witness emission
    from witness_base import WitnessBuilder
    builder = (
        WitnessBuilder(f"sublemma-2-1-A-operator-extract-h9-{interface}",
                       engine="numpy")
        .set_description(
            f"Multi-interface Sub-lemma 2.1: operator-valued "
            f"A^λ_{{ξν}}(I_2) extraction at H_9 ↓ H_6 × H_3 for "
            f"I_2 = {interface}. Phase 1 (tractable scope) with "
            f"K_6 = {K_6}, K_3 = {K_3} test words. Low-dim λ ⊢ 9 "
            f"are over-determined and reach machine-ε consistency; "
            f"high-dim λ (e.g. (4,3,1,1) with d_λ=216) are "
            f"under-determined at this K and flagged. Phase 2 "
            f"(K = 60+) deferred."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-sublemma-2-1-h9-multi-interface-extension.md"
        )
        .add_data("interface_type", interface)
        .add_data("interface_coefs", list(INTERFACE_COEFS[interface]))
        .add_data("q_0", float(Q0))
        .add_data("h", H)
        .add_data("K_6_h6_test_words", K_6)
        .add_data("K_3_h3_test_words", K_3)
        .add_data("n_test_pairs", K_6 * K_3)
        .add_data("chi_compute_time_seconds", chi_time)
        .add_data("n_partitions_9", len(parts_9))
        .add_data("n_overdetermined", n_overdet)
        .add_data("n_consistent", n_consistent)
        .add_data("n_underdetermined", n_underdet)
        .add_data("results_per_lambda", results_per_lambda)
        .add_caveat(
            "Phase 1 scope: K_6 = K_3 = 12 test words gives 144 "
            "equations per λ. The high-dim ξ = (3,2,1) (d=16) "
            "supports up to 16²·2² = 1024 unknowns per block, "
            "exceeding 144 — those λ are under-determined and "
            "their A_per_pair summaries reflect a least-squares "
            "projection, not a unique extraction. Phase 2 (K ≥ 60) "
            "is needed for the high-dim λ subset."
        )
        .add_caveat(
            "At q_0 the bilinear system uses numpy complex (f64). "
            "Verification of the iterated Sub-lemma 2.1 formula at "
            "machine ε is bounded by f64 precision (~1e-12 relative). "
            "An mpmath 50-dps version of this extraction would push "
            "the floor to ~1e-45 but at substantially higher cost; "
            "deferred to follow-up if 1-ppb mass-prediction work "
            "requires it."
        )
    )

    builder.add_assertion(
        "overdetermined_lambda_consistent",
        computed=n_consistent,
        expected=n_overdet,
        source="bilinear-system inversion at machine ε",
    )

    out_path = builder.save()
    print(f"  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
