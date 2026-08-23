"""Infrastructural A^λ_{ξν}(I) extractor at arbitrary H_n level.

.. note::
   **STATUS (2026-06-16): the H_9+ extracts produced here are INERT in
   production and SUPERSEDED.** The A≥3 path of
   ``canonical_tr_m_via_branching.py`` returns the value via the lossless
   fine-Bratteli transfer matrix (``tr_m_atom_via_transfer.tr_m_atom_zn``);
   ``compute_chi_lambda_via_branching`` returns ``None`` for A≥3 *before* these
   least-squares extracts are applied, so they feed no live mass/binding value.
   They are also rank-deficient min-norm fits (suspect per
   ``docs/audits/2026-06-16-unjustified-least-squares-fitting-audit.md``). The
   correct, non-fitted replacement is the closed-form **categorical** interface
   operator ``A^λ_{ξν}(I) = Π_{ξν} ρ_λ(I) Π_{ξν}``
   (``a_operator_categorical.py`` / ``a_operator_gauge_align.py``, verified exact
   at 1e-49). Only the H_6 deuteron extract is full-rank/correct and live (A=2).
   See ``docs/audits/2026-06-16-wenzl-a3-wireup-scope-and-deflag.md``.

Generalization of `sublemma_2_1_A_operator_extract_h9.py` (H_9-specific)
and `sublemma_2_1_A_operator_extract.py` (H_6-specific) to handle ANY
peel level needed by the operator-valued Wenzl branching combiner.

## Scope

For a canonical atomic braid β ∈ H_n decomposed via the peel-one-
nucleon recursion

    β = W_inner · I · β_block,
        W_inner ∈ H_{n-3}   (the (A-1)-nucleon prefix at left strands)
        β_block ∈ H_3        (the A-th nucleon intra-block at right strands)
        I ∈ {I_pp, I_nn, I_pn}  (the outer-most interface)

Sub-lemma 2.1 gives

    χ^λ(β) = Σ_{ξ⊢n-3, ν⊢3} c^λ_{ξν} · Tr(A^λ_{ξν}(I) · (ρ_ξ(W_inner) ⊗ ρ_ν(β_block)))

This script extracts A^λ_{ξν}(I) for each (λ, ξ, ν) via bilinear-
system inversion on K_inner × K_block test pairs, at any
n_outer ∈ {6, 9, 12, 15, 18, 21, ...} corresponding to A ∈ {2, 3, 4, 5, 6, 7, ...}.

## Reuse across isotopes

For an A-nucleon atom the full χ^λ requires A-1 levels of peeling.
Each level n_k = 3(A-k+1) for k=1..A-1 needs its A^λ_{ξν}(I_k) extract,
where I_k is the (A-k)→(A-k+1) interface type.

By running this extractor at every (n_outer, interface) combination
seen across the atom registry, we get a **persistent operator-valued
cache** consumed by the branching combiner.

## CLI

    python3 A_operator_extract_at_level.py --n-outer 9 --interface pp
    python3 A_operator_extract_at_level.py --n-outer 12 --interface pn

Outputs `A-operator-extract-h{n}-{interface}.witness.json`.

## Test-word generation

The bilinear system has K_inner · K_block equations per λ. The
default is `K_inner = max(12, n_outer * 2)` (matches the
implementation `--K-inner` default); this is **NOT** sufficient
to over-determine high-dim λ for large n (per Gemini review on
PR #708 — the theoretically-required count for an `((d_μ d_ν)²
× support_size)`-unknown system is much larger than `n_outer*2`).

Currently-shipped extracts have over-determined low-dim λ and
pseudo-inverse-determined high-dim λ; the latter still emit
consistent `A_per_pair` data (residual ~1e-14) because the LR
support fixes the structure, but uniqueness is not guaranteed
outside the test-word span. The deuteron extract has been verified
end-to-end at machine ε via the operator-valued combiner
(`canonical_tr_m_via_branching.py`).

## Memory scaling caveat (Gemini review #708)

`np.kron(B_xi, B_nu)` and the dense `M` matrix for `lstsq` grow
as O((d_μ d_ν)²) per support pair. For H_18 (d_λ_max ≈ 16M) this
exceeds available memory. Practical ceiling for the current
implementation: **H_12** (⁴He outer interfaces). Beyond that, the
operator-valued combiner falls back to markov_peel (see
`canonical_tr_m_via_branching.py`); a sparse-Hoefsmit-block
approach is the long-term path.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from char_fast import _compiled_sigmas, chi_lambda_fast  # noqa: E402
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402
from q_parameter import Q as Q_FLOAT  # noqa: E402
from canonical_braid_crossings import d_for_ctype  # noqa: E402

Q0 = float(Q_FLOAT)
H = Q0 - 1.0 / Q0   # h = q − q⁻¹ at q_0

# Interface coefficients, DERIVED from the canonical classifier rather than
# typed here. The comment above this table used to say it followed "the standard
# atomic-braid convention (mass_at_3A_proper.atom_braid_word_3A)" while `pn` read
# `-H/2` — and that had stopped being true: the canonical builder emits
# `averaged_weighted` at a p-n boundary, `d = -h(1/2 - δ/4)`, which is
# 7.190163e-05 away from `-h/2`.
#
# This was a THIRD private ctype vocabulary, keyed pp/nn/pn. Both existing
# detectors are structurally blind to it: `test_ctype_consumer_coverage` Part B
# looks for the {sigma, sigma_inv, averaged, averaged_weighted} vocabulary, and
# Part F looks for a `pn_convention=` kwarg. This table has neither, while being
# the thing that actually sets the interface in the mass-table path. Bean
# `qou-cds4`.
#
# The pp and nn rows were already exactly right — verified against
# `atom_canonical_crossings`, which emits `sigma` at a p-p boundary and
# `sigma_inv` at n-n, whose `d` values match `0.0` and `-H` to the bit. Only
# `pn` was wrong, which is why this is a one-row correction and not a rewrite.
_IFACE_CTYPE = {"pp": "sigma", "nn": "sigma_inv", "pn": "averaged_weighted"}
INTERFACE_COEFS: dict[str, tuple[float, float]] = {
    iface: (1.0, float(d_for_ctype(ct, H)))
    for iface, ct in _IFACE_CTYPE.items()
}


def shape_dim(shape: tuple) -> int:
    """Dimension of the seminormal rep of H_n at partition `shape`."""
    _, d = _compiled_sigmas(shape, "double")
    return d


def evaluate_word_matrix(shape: tuple, word: list,
                         q_val: float = None) -> np.ndarray:
    """Compute ρ_shape(W) ∈ M_{d×d} for word W = [(c, d, gen_idx), ...].

    Optimization (Gemini review #708): avoid allocating
    `(c σ + d I)` as an intermediate dense matrix; apply
    `M ← c · (M @ σ) + d · M` in place. Saves one O(dim²) allocation
    per crossing.
    """
    if q_val is None:
        q_val = Q0
    sigmas, dim = _compiled_sigmas(shape, "double")
    sigma_mats = [np.asarray(fn(q_val), dtype=complex) for fn in sigmas]
    M = np.eye(dim, dtype=complex)
    for (c, d, g) in word:
        if g >= len(sigma_mats):
            raise ValueError(f"gen {g} out of range for shape {shape}")
        cc = complex(c)
        dd = complex(d)
        if dd == 0:
            M = cc * (M @ sigma_mats[g])
        else:
            # M ← c·(M @ σ_g) + d·M
            M = cc * (M @ sigma_mats[g]) + dd * M
    return M


def with_outer_interface(
    word_inner: list, word_block: list, interface: str, n_inner: int
) -> list:
    """Build the H_{n_inner + 3} word: W_inner · I · β_block.

    The interface I acts at strand (n_inner - 1) (0-based generator
    index), connecting the rightmost strand of W_inner to the leftmost
    strand of β_block. The block's gens shift by n_inner.
    """
    if interface not in INTERFACE_COEFS:
        raise ValueError(
            f"unknown interface {interface!r}; "
            f"expected one of {sorted(INTERFACE_COEFS)}"
        )
    int_c, int_d = INTERFACE_COEFS[interface]
    out = list(word_inner)
    out.append((int_c, int_d, n_inner - 1))
    out += [(c, d, g + n_inner) for (c, d, g) in word_block]
    return out


def make_test_words_h3() -> list[list]:
    """Standard 12-word H_3 test set. Reused at every level."""
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


def make_test_words_h_n(n: int, K_target: int = 16) -> list[list]:
    """Generate K_target diverse H_n test words.

    Strategy: parameterised over generators σ_0 .. σ_{n-2}. Include
    the identity, single generators, adjacent products, h-shifted
    crossings, and a couple of order-3 trefoil-like words. For
    n > 6 the test-word count grows with n to keep the bilinear
    system over-determined for low-dim λ.
    """
    gens = list(range(n - 1))
    words: list[list] = [
        [],                              # identity
    ]
    for g in gens:
        words.append([(1.0, 0.0, g)])    # σ_g
    for g in gens[:-1]:
        words.append([(1.0, 0.0, g), (1.0, 0.0, g + 1)])  # σ_g σ_{g+1}
        words.append([(1.0, 0.0, g + 1), (1.0, 0.0, g)])  # σ_{g+1} σ_g
    # h-shifted crossings — exercise the (1, -h) channel
    for g in gens[:2]:
        words.append([(1.0, -H, g)])
        words.append([(1.0, -H / 2, g)])
    # Trefoil-like at low strands
    if n >= 3:
        words.append(
            [(1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0)]
        )
    if n >= 5:
        words.append(
            [(1.0, 0.0, 2), (1.0, 0.0, 3), (1.0, 0.0, 2)]
        )
    # Truncate to K_target (or pad with simple words if too few).
    if len(words) > K_target:
        words = words[:K_target]
    return words


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n-outer", type=int, required=True,
                        help="H_n level (e.g. 6 for D, 9 for T/³He, 12 for ⁴He, "
                             "15 for ⁵Li, 18 for ⁶Li, 21 for ⁷Li)")
    parser.add_argument("--interface", choices=sorted(INTERFACE_COEFS),
                        required=True,
                        help="outer interface type")
    parser.add_argument("--K-inner", type=int, default=None,
                        help="test-word count for the H_{n-3} inner system "
                             "(default: max(12, n-2) for over-determination)")
    parser.add_argument("--rank-tol", type=float, default=1e-8)
    args = parser.parse_args()

    n_outer = args.n_outer
    if n_outer < 6 or n_outer % 3 != 0:
        print(f"  ERROR: n_outer must be a multiple of 3 and ≥ 6 "
              f"(got {n_outer})")
        return 2
    n_inner = n_outer - 3
    n_block = 3
    interface = args.interface

    K_inner_default = max(12, n_outer * 2)
    K_inner = args.K_inner if args.K_inner is not None else K_inner_default

    parts_inner = partitions_of(n_inner)
    parts_block = partitions_of(n_block)
    parts_outer = partitions_of(n_outer)
    lr_table = get_lr_table(n_inner, n_block)

    test_words_inner = make_test_words_h_n(n_inner, K_target=K_inner)
    test_words_block = make_test_words_h3()
    K_i = len(test_words_inner)
    K_b = len(test_words_block)

    print("=" * 96)
    print(f"  A^λ_{{ξν}}(I={interface}) extraction at H_{n_outer}"
          f" ↓ H_{n_inner} × H_{n_block}")
    print("=" * 96)
    print(f"  q_0 = {Q0:.12f}, h = {H:.12f}")
    print(f"  Interface coefs (c, d) = {INTERFACE_COEFS[interface]}")
    print(f"  K_inner = {K_i} H_{n_inner} test words")
    print(f"  K_block = {K_b} H_{n_block} test words")
    print(f"  → {K_i * K_b} test pairs per λ")
    print(f"  |partitions(H_{n_outer})| = {len(parts_outer)}")
    print()

    t0 = time.monotonic()
    print(f"  [1/3] ρ_ξ(W_inner) at q_0: "
          f"{K_i} × {len(parts_inner)} = {K_i*len(parts_inner)} mats...")
    rho_xi = {}
    for i, w in enumerate(test_words_inner):
        for xi in parts_inner:
            rho_xi[(i, xi)] = evaluate_word_matrix(xi, w)
    print(f"        done in {time.monotonic()-t0:.1f}s")

    t0 = time.monotonic()
    print(f"  [2/3] ρ_ν(W_block) at q_0: "
          f"{K_b} × {len(parts_block)} = {K_b*len(parts_block)} mats...")
    rho_nu = {}
    for j, w in enumerate(test_words_block):
        for nu in parts_block:
            rho_nu[(j, nu)] = evaluate_word_matrix(nu, w)
    print(f"        done in {time.monotonic()-t0:.1f}s")

    t0 = time.monotonic()
    n_chi = K_i * K_b * len(parts_outer)
    print(f"  [3/3] χ^λ(W_inner · I · β_block) at H_{n_outer}: {n_chi} triples...")
    chi_lam = {}
    progress = 0
    for i, w_i in enumerate(test_words_inner):
        for j, w_b in enumerate(test_words_block):
            comb = with_outer_interface(w_i, w_b, interface, n_inner)
            for lam in parts_outer:
                chi_lam[(i, j, lam)] = chi_lambda_fast(lam, comb)
            progress += len(parts_outer)
        if progress // len(parts_outer) % 4 == 0:
            print(f"        progress: {progress}/{n_chi} "
                  f"({100*progress/n_chi:.1f}%) t={time.monotonic()-t0:.1f}s")
    chi_time = time.monotonic() - t0
    print(f"        done in {chi_time:.1f}s")
    print()

    # Per-λ bilinear inversion
    print(f"  Per-λ A^λ_{{ξν}}(I={interface}) extraction:")
    print(f"  {'λ ⊢ '+str(n_outer):<24} {'dim':>5} {'pairs':>6} "
          f"{'unkn':>7} {'rank/eqs':>11} {'rel res':>10}  ")
    print("  " + "-" * 80)

    results_per_lambda = {}
    n_consistent = 0
    n_underdet = 0
    for lam in parts_outer:
        pairs = []
        for xi in parts_inner:
            for nu in parts_block:
                c = lr_table.get((xi, nu, lam), 0)
                if c > 0:
                    d_xi = shape_dim(xi)
                    d_nu = shape_dim(nu)
                    pairs.append({
                        "xi": xi, "nu": nu, "c": c,
                        "d_xi": d_xi, "d_nu": d_nu,
                        "n_entries": (d_xi * d_nu) ** 2,
                    })
        if not pairs:
            continue

        n_unknowns = sum(p["n_entries"] for p in pairs)
        n_eq = K_i * K_b
        underdet = n_unknowns > n_eq

        M = np.zeros((n_eq, n_unknowns), dtype=complex)
        rhs = np.zeros(n_eq, dtype=complex)
        offsets = [0]
        for p in pairs:
            offsets.append(offsets[-1] + p["n_entries"])
        for k_idx, (i, j) in enumerate(
            (i, j) for i in range(K_i) for j in range(K_b)
        ):
            for p_idx, p in enumerate(pairs):
                B_xi = rho_xi[(i, p["xi"])]
                B_nu = rho_nu[(j, p["nu"])]
                X = np.kron(B_xi, B_nu)
                coef = X.T.flatten()
                M[k_idx, offsets[p_idx]:offsets[p_idx] + p["n_entries"]] = coef
            rhs[k_idx] = chi_lam[(i, j, lam)]

        sol, _, rank, _ = np.linalg.lstsq(M, rhs, rcond=args.rank_tol)
        pred = M @ sol
        rhs_scale = max(float(np.mean(np.abs(rhs))), 1e-12)
        max_rel = float(np.max(np.abs(pred - rhs))) / rhs_scale
        consistent = max_rel < 1e-6
        if underdet:
            n_underdet += 1
        if consistent:
            n_consistent += 1

        d_lam = shape_dim(lam)
        status = "✓" if consistent else ("under" if underdet else "✗")
        print(f"  {str(lam):<24} {d_lam:>5} {len(pairs):>6} "
              f"{n_unknowns:>7} {rank:>5}/{n_eq:<4} {max_rel:>10.2e}  {status}")

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
                    d == 1
                    or (np.linalg.norm(A_mat - (np.trace(A_mat) / d) * np.eye(d)) < 1e-9)
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
    print(f"  Summary: {n_consistent}/{len(parts_outer)} consistent, "
          f"{n_underdet}/{len(parts_outer)} under-determined")
    print()

    from witness_base import WitnessBuilder
    builder = (
        WitnessBuilder(
            f"A-operator-extract-h{n_outer}-{interface}",
            engine="numpy",
        )
        .set_description(
            f"Operator-valued A^λ_{{ξν}}(I_{interface}) extraction at "
            f"H_{n_outer} ↓ H_{n_inner} × H_{n_block} via bilinear-system "
            f"inversion. Generalises sublemma_2_1_A_operator_extract_h9.py "
            f"for any (n_outer, interface) — infrastructural for the "
            f"operator-valued Wenzl branching combiner across all atomic "
            f"isotopes."
        )
        .add_parameter("n_outer", n_outer)
        .add_parameter("n_inner", n_inner)
        .add_parameter("n_block", n_block)
        .add_parameter("interface_type", interface)
        .add_parameter("interface_coefs", list(INTERFACE_COEFS[interface]))
        .add_parameter("K_inner", K_i)
        .add_parameter("K_block", K_b)
        .add_parameter("K_total", K_i * K_b)
        .add_parameter("q_0", Q0)
        .add_data("n_partitions", len(parts_outer))
        .add_data("n_consistent", n_consistent)
        .add_data("n_underdetermined", n_underdet)
        .add_data("results_per_lambda", results_per_lambda)
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
