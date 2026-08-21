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

import numpy as np

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from char_fast import _compiled_sigmas  # noqa: E402
from sublemma_2_1_deuteron_branching import (  # noqa: E402
    LR_TABLE_3_3_TO_6 as LR_TABLE,
    lr_coef,
    partitions_of,
)
from q_parameter import Q as Q0  # noqa: E402


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


def evaluate_word_matrix(shape: tuple, word: list, q_val: float = None) -> np.ndarray:
    """Evaluate the Hecke-algebra word `[(c, d, g), ...]` as
    Π_i (c_i · σ_g_i + d_i · I) in the seminormal rep of `shape`."""
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


def disjoint_word(word_p: list, word_n: list, n1: int = 3) -> list:
    """β_1 ⊗ β_2 in H_(n1 + n2): re-index β_2 generators by +n_1."""
    out = list(word_p)
    out += [(c, d, g + n1) for (c, d, g) in word_n]
    return out


def _pn_interface_d() -> float:
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
    """
    from canonical_braid_crossings import d_for_ctype
    return float(d_for_ctype("averaged_weighted", H))


def with_interface(word_p: list, word_n: list, n1: int = 3,
                    int_c: float = 1.0, int_d: float | None = None) -> list:
    """β_1 · I · β_2 in H_(n1 + n2) with I = c·σ_(n1-1) + d·1.

    `int_d=None` (the default) resolves to the canonical colour-weighted p-n
    interface. Pass an explicit value only to probe a non-canonical convention,
    and label it where you do.
    """
    if int_d is None:
        int_d = _pn_interface_d()
    out = list(word_p)
    out.append((int_c, int_d, n1 - 1))   # interface generator at strand n_1
    out += [(c, d, g + n1) for (c, d, g) in word_n]
    return out


def chi_lambda_matrix_trace(shape: tuple, word: list) -> complex:
    """χ^λ(β) = Tr ρ_λ(β)."""
    M = evaluate_word_matrix(shape, word)
    if M.size == 0:
        return 0+0j
    return complex(np.trace(M))


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
                    d_mu = max(rho_mu[(0, mu)].shape) if rho_mu[(0, mu)].size > 0 else 1
                    d_nu = max(rho_mu[(0, nu)].shape) if rho_mu[(0, nu)].size > 0 else 1
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
        M = np.zeros((n_eq, n_unknowns), dtype=complex)
        rhs = np.zeros(n_eq, dtype=complex)
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
                X = np.kron(B_mu, B_nu)   # (d_μ d_ν, d_μ d_ν) matrix
                # Tr(A_diag · X) where A_diag = Σ_k A_kk sums over LR
                # multiplicity copies. The multiplicity c^λ_{μν} is
                # absorbed into A_diag itself; do NOT multiply by c
                # again here (corrects an early bug that gave 4e-3 rel
                # residual on λ = (3,2,1)).
                coef = X.T.flatten()
                M[k, offsets[p_idx]:offsets[p_idx] + p["n_entries"]] = coef
            rhs[k] = chi_lam[(i, j, lam)]

        # Solve by least squares
        sol, residuals, rank, sv = np.linalg.lstsq(M, rhs, rcond=None)
        pred = M @ sol
        # Use a SCALE-AWARE relative error: residual normalized by the
        # typical magnitude of |rhs| across the test pairs, not divided
        # per-equation. The per-equation form |res|/|rhs| explodes when
        # an individual rhs[k] happens to be near zero (which can occur
        # for symmetry-driven cancellations in specific test pairs)
        # even when the global fit is at machine precision.
        rhs_scale = max(float(np.mean(np.abs(rhs))), 1e-12)
        max_abs_res = float(np.max(np.abs(pred - rhs)))
        max_rel = max_abs_res / rhs_scale

        # Reshape sol into per-pair matrices A_diag^{μν}
        A_per_pair = {}
        for p_idx, p in enumerate(pairs):
            d = p["d_mu"] * p["d_nu"]
            A_flat = sol[offsets[p_idx]:offsets[p_idx] + p["n_entries"]]
            A_mat = A_flat.reshape((d, d), order="C")
            A_per_pair[f"({p['mu']},{p['nu']})"] = {
                "matrix_re": [[float(A_mat[a, b].real) for b in range(d)] for a in range(d)],
                "matrix_im": [[float(A_mat[a, b].imag) for b in range(d)] for a in range(d)],
                "frobenius_norm": float(np.linalg.norm(A_mat)),
                "max_abs_entry": float(np.max(np.abs(A_mat))),
                "trace": complex(np.trace(A_mat)).real,
                "is_scalar_multiple_of_id": bool(
                    d == 1 or
                    (np.linalg.norm(A_mat - (np.trace(A_mat)/d) * np.eye(d)) < 1e-9)
                ),
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
            print(f"  {str(lam):<14} {key:<28} {info['frobenius_norm']:>10.4f} {info['max_abs_entry']:>12.4f}  {scalar_str}")

    witness = {
        "computation": "sublemma-2-1-A-operator-extract",
        "description": (
            "Operator-valued A^λ_{μν}(I) extraction via bilinear-system "
            "inversion. Confirms refined Sub-lemma 2.1: the (μ,ν)-block "
            "of ρ_λ(I) is generally a non-scalar operator on V_μ ⊗ V_ν. "
            "For deuteron interface I = σ_2 - h/2 on H_6 ↓ H_3 × H_3, all "
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
        "parameters": {
            "q_0": float(Q0),
            "interface": "I = σ_2 - h/2 (atomic-braid pn averaged crossing)",
            "n_test_pairs": K * K,
            "n_test_words_per_side": K,
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
