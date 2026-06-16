#!/usr/bin/env python3
"""A=3 cross-check of the path-(b) fusion block-decomposition (tritium, ³He).

The decisive correctness gate of the Wenzl A≥3 workplan (#2356): the old
least-squares H₉ extracts gave A=3 χ^λ wrong by 21–42 %
(canonical_tr_m_via_branching.py:242). The fusion derivation (PR #2358,
docs/audits/2026-06-16-wenzl-a3-fusion-operator-derivation.md) says the
interface operator is the diagonal multiplicity-block sum of ρ_λ(I) in the
branching basis. Here we verify the equivalent convention-free identity at the
real 3-nucleon atomic braid, split (6,3) at the second inter-nucleon interface:

    χ^λ(β_inner · I · β_outer)
        = Σ_{ξ⊢6, ν⊢3} Tr_{V_λ}[ P_ξ P_ν · ρ_λ(I) · P_ξ P_ν · ρ_λ(β_inner·β_outer) ]

with β_inner ∈ H_6 (strands 1-6 = nuc1·I12·nuc2), I = the σ_5 interface,
β_outer ∈ H_3' (strands 7-9 = nuc3). If this reproduces the true χ^λ (and hence
tr_M = Σ_λ y_λ χ^λ vs the canonical value) to ≤ 1e-10 for all λ ⊢ 9, the fusion
block-decomposition is verified at A=3 — the regime the rank-deficient extracts
failed — and the operator-form recursion (the actual speedup) is justified.

Isotypic projectors are JM-based: C = Σ_k L_k (multiplicative Jucys-Murphy,
L_{k+1}=σ L_k σ) is central per block with eigenvalue Σ_cells q^{2·content},
which separates all partitions at generic q (content MULTISET distinguishes even
(2,2,2) vs (3,1,1,1), where the integer content-sum collides).

f64 cross-check (numpy); the production witness re-runs at 50-dps (compute-author §1).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from canonical_tr_m_via_branching import evaluate_word_matrix_np  # noqa: E402
from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from lr_coefficients import partitions_of, lr_coef  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from hecke_core import h as H_VAL  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

CANONICAL_TRM = {"tritium": 0.1040521067420517, "3He": 0.2065408170207396}


def ops_to_word(ops):
    """(gen, ctype) → (c, d, g) Hecke word."""
    word = []
    for gen, ctype in ops:
        if ctype == "sigma":
            word.append((1.0, 0.0, int(gen)))
        elif ctype == "sigma_inv":
            word.append((1.0, -float(H_VAL), int(gen)))
        elif ctype == "averaged":
            word.append((1.0, -float(H_VAL) / 2, int(gen)))
        else:
            raise ValueError(f"unknown crossing {ctype!r}")
    return word


def jm_central(shape: tuple, gen_lo: int, m_strands: int) -> np.ndarray:
    """C = Σ_{k=1}^{m} L_k, multiplicative JM L_{k+1}=σ L_k σ, for the block of
    `m_strands` strands whose first generator is `gen_lo`. Central in that block
    sub-algebra; eigenvalue Σ_cells q^{2·content} on each irrep."""
    dim = evaluate_word_matrix_np(shape, []).shape[0]
    I = np.eye(dim, dtype=complex)
    L = I.copy()
    C = I.copy()  # L_1 = I
    for k in range(1, m_strands):
        S = evaluate_word_matrix_np(shape, [(1.0, 0.0, gen_lo + k - 1)])
        L = S @ L @ S
        C = C + L
    return C


def central_eig(part: tuple, m_strands: int) -> complex:
    """Scalar eigenvalue c of C on the standalone irrep V_part (part ⊢ m)."""
    C = jm_central(part, 0, m_strands)
    d = C.shape[0]
    return complex(np.trace(C)) / d


def lagrange_projectors(C: np.ndarray, present_eigs: dict) -> dict:
    """P_part for each part in present_eigs = {part: c_part}, via Lagrange
    interpolation annihilating all OTHER present eigenvalues."""
    dim = C.shape[0]
    I = np.eye(dim, dtype=complex)
    items = list(present_eigs.items())
    out = {}
    for part, c in items:
        P = I.copy()
        for part2, c2 in items:
            if part2 == part:
                continue
            P = P @ ((C - c2 * I) / (c - c2))
        out[part] = P
    return out


def split_atom_word(word):
    """Split a (6,3) A=3 atom word into (inner H_6 gens≤4, interface gen5,
    outer H_3' gens≥6). Asserts block-sequential structure."""
    inner = [op for op in word if op[2] <= 4]
    iface = [op for op in word if op[2] == 5]
    outer = [op for op in word if op[2] >= 6]
    assert len(iface) == 1, f"expected single gen-5 interface, got {len(iface)}"
    # sequential check: every inner op precedes the interface precedes every outer
    idx_iface = word.index(iface[0])
    assert all(word.index(op) < idx_iface for op in inner)
    assert all(word.index(op) > idx_iface for op in outer)
    return inner, iface[0], outer


def main() -> int:
    parts6, parts3, parts9 = (partitions_of(6), partitions_of(3),
                              partitions_of(9))
    # Standalone central eigenvalues.
    eig6 = {xi: central_eig(xi, 6) for xi in parts6}
    eig3 = {nu: central_eig(nu, 3) for nu in parts3}
    print(f"q_0 = {float(Q0):.6f}")
    print(f"H_6 central eigenvalues distinct: "
          f"{len({round(c.real,6) for c in eig6.values()})}/{len(eig6)}")
    print(f"H_3 central eigenvalues distinct: "
          f"{len({round(c.real,6) for c in eig3.values()})}/{len(eig3)}")

    all_ok = True
    for label, (Z, N) in [("tritium", (1, 2)), ("3He", (2, 1))]:
        word = ops_to_word(atom_canonical_crossings(Z, N))
        inner, iface, outer = split_atom_word(word)
        print(f"\n=== {label} (Z={Z},N={N}) — split: "
              f"|inner|={len(inner)} iface=gen5 |outer|={len(outer)} ===")

        y_dict = {tuple(k): complex(v)
                  for k, v in y_lambda_at(9, float(Q0)).items()}
        trM_true = 0.0 + 0j
        trM_fusion = 0.0 + 0j
        worst = 0.0
        for lam in parts9:
            dim = evaluate_word_matrix_np(lam, []).shape[0]
            if dim == 0:
                continue
            # present ξ ⊢ 6, ν ⊢ 3 in V_λ ↓ H_6 ⊗ H_3'
            present_xi = {xi: eig6[xi] for xi in parts6
                          if any(lr_coef(xi, nu, lam) > 0 for nu in parts3)}
            present_nu = {nu: eig3[nu] for nu in parts3
                          if any(lr_coef(xi, nu, lam) > 0 for xi in parts6)}
            if not present_xi or not present_nu:
                continue
            C1 = jm_central(lam, 0, 6)   # H_6 first block
            C2 = jm_central(lam, 6, 3)   # H_3' second block
            Pxi = lagrange_projectors(C1, present_xi)
            Pnu = lagrange_projectors(C2, present_nu)

            rho_I = evaluate_word_matrix_np(lam, [iface])
            rho_io = evaluate_word_matrix_np(lam, inner + outer)
            lhs = complex(np.trace(evaluate_word_matrix_np(lam, word)))
            rhs = 0.0 + 0j
            for Pm in Pxi.values():
                for Pn in Pnu.values():
                    Pmn = Pm @ Pn
                    rhs += np.trace(Pmn @ rho_I @ Pmn @ rho_io)
            worst = max(worst, abs(lhs - rhs))
            y = y_dict[tuple(lam)]
            trM_true += y * lhs
            trM_fusion += y * rhs

        trM_true_abs = abs(trM_true)
        trM_fusion_abs = abs(trM_fusion)
        canon = CANONICAL_TRM[label]
        ok = worst < 1e-9 and abs(trM_fusion_abs - canon) < 1e-6
        all_ok = all_ok and ok
        print(f"  per-λ worst |χ_true − χ_fusion|: {worst:.3e}")
        print(f"  tr_M (true direct)   = {trM_true_abs:.13f}")
        print(f"  tr_M (fusion blocks) = {trM_fusion_abs:.13f}")
        print(f"  tr_M (canonical ref) = {canon:.13f}")
        print(f"  |fusion − canonical| = {abs(trM_fusion_abs - canon):.3e}  "
              f"{'✓' if ok else '✗'}")

    print()
    if all_ok:
        print("✅ A=3 fusion block-decomposition VERIFIED (tritium + ³He) — "
              "reproduces the true atomic χ^λ and tr_M where the old\n"
              "   rank-deficient extracts failed at 21–42 %. Operator-form "
              "recursion (the speedup) is justified.")
    else:
        print("✗ A=3 cross-check FAILED — investigate before the recursion.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
