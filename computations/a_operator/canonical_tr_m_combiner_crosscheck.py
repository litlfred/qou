"""A≥3 cross-check: operator-valued combiner tr_M vs the production transfer.

The fine-Bratteli transfer matrix (`tr_m_atom_via_transfer.tr_m_atom_zn`) is the
canonical A≥3 `tr_M` route in `canonical_tr_m_via_branching.compute_tr_m_via_branching`
(it is lossless and fast — no `d_λ` wall). This module provides an *independent*
cross-check of that value via the operator-valued Wenzl branching combiner
(`a_operator_recursive.interface_blocks`, the Young-basis recursion kernel):

  tr_M(β_atom) = Σ_{λ⊢3A} y_λ · χ^λ(β_atom),
  χ^λ(W_inner·I·β_block) = Σ_{ξ⊢3(A−1), ν⊢3}
                            Tr_{V_ξ⊗V_ν}( A^λ_{ξν}(I)·(ρ_ξ(W_inner)⊗ρ_ν(β_block)) ).

It peels the **last** nucleon (the H_3 block on the last 3 strands) off the
canonical `atom_braid_word_3A(Z,N)`; the word factors exactly as
`[W_inner on gens 0..n_inner−1][bridge σ_{n_inner−1}][β_block]` with
`n_inner = 3(A−1)`.

**Honest framing (no production-value change).** Per the main-merged bond-
dimension verdict `χ_eff(k)=p(3k)`, the combiner cannot beat the transfer
asymptotically; this is a *cross-check*, not a replacement. The transfer stays
the production default. The combiner's value is (a) an independent re-derivation
of the A≥3 χ^λ from representation theory (vs the rank-deficient least-squares
H_9+ extracts the old per-λ branching path used — closure path (b) of the
`compute_chi_lambda_via_branching` docstring, now implemented), and (b) the
Wedderburn shadow-price structure (which (ξ,ν) blocks saturate each λ) that the
scalar transfer discards.

Runtime note: ρ_ξ(W_inner) is evaluated directly at d_ξ (mpmath). For D (ξ⊢3)
and ³He (ξ⊢6, d≤16) this is fast (< a few s); ⁴He (ξ⊢9, d≤216) takes ~25 min and
is validated separately in `a_operator_recursive_he4_crosscheck.py`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
_sys.path.insert(0, str(_Path(__file__).resolve().parent))

import time  # noqa: E402
import mpmath as mp  # noqa: E402

import a_operator_categorical as aoa  # noqa: E402
import a_operator_recursive as rec  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from lr_coefficients import partitions_of  # noqa: E402


def _word_matrix(mats, word):
    M = mp.eye(mats[0].rows)
    for (c, d, g) in word:
        M = M * (mp.mpf(c) * mats[g] + mp.mpf(d) * mp.eye(mats[0].rows))
    return M


def _trace_A_kron(A, RWx, RBn, d_mu, d_nu):
    # Tr[A · kron(RWx, RBn)] = Σ_{a,b,a',b'} A[a·d_ν+b, a'·d_ν+b'] RWx[a',a] RBn[b',b]
    s = mp.mpf(0)
    for a in range(d_mu):
        for ap in range(d_mu):
            rwa = RWx[ap, a]
            if rwa == 0:
                continue
            for b in range(d_nu):
                for bp in range(d_nu):
                    rbb = RBn[bp, b]
                    if rbb == 0:
                        continue
                    s += A[a * d_nu + b, ap * d_nu + bp] * rwa * rbb
    return s


def tr_m_via_combiner(Z: int, N: int, dps: int = 50) -> dict:
    """`tr_M(β_atom)` for nucleon counts (Z,N) via the recursion-kernel combiner,
    peeling the last nucleon. Returns a dict with the combiner tr_M, the transfer
    reference, and the agreement metrics."""
    if mp.mp.dps < dps + 10:
        mp.mp.dps = dps + 10
    A = Z + N
    if A < 2:
        raise ValueError("combiner needs A ≥ 2 (an inter-nucleon interface)")
    q = aoa.q0_mp(dps)
    q_str = mp.nstr(q, dps)
    n = 3 * A
    n_inner = 3 * (A - 1)
    bridge_gen = n_inner - 1

    w = atom_braid_word_3A(Z, N)
    idx = next(i for i, (c, d, g) in enumerate(w) if g == bridge_gen)
    W_inner = w[:idx]
    I_c, I_d, I_g = w[idx]
    assert I_g == bridge_gen, f"bridge gen mismatch: {I_g} != {bridge_gen}"
    block = [(c, d, g - n_inner) for (c, d, g) in w[idx + 1:]]

    p_in, p3 = partitions_of(n_inner), partitions_of(3)
    t0 = time.time()
    RW = {xi: _word_matrix(aoa.exact_seminormal_matrices(xi, q_str, dps)[0], W_inner)
          for xi in p_in}
    RB = {nu: _word_matrix(aoa.exact_seminormal_matrices(nu, q_str, dps)[0], block)
          for nu in p3}

    chi_comb = {}
    for lam in partitions_of(n):
        blocks = rec.interface_blocks(lam, n_inner, 3, q_str, mp.mpf(I_d), dps)
        s = mp.mpf(0)
        for (xi, nu), info in blocks.items():
            s += _trace_A_kron(info["A"], RW[xi], RB[nu], info["d_mu"], info["d_nu"])
        chi_comb[lam] = s
    comb_wall = time.time() - t0

    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q0).items()}
    trM_comb = sum((y[k] * chi_comb[k] for k in chi_comb), mp.mpf(0))

    tr_ref, _free, _chi, ref_wall = tr_m_atom_zn(Z, N, dps=dps)
    abs_d = abs(abs(trM_comb) - abs(tr_ref))
    rel_d = abs_d / abs(tr_ref) if tr_ref != 0 else abs_d
    return {
        "Z": Z, "N": N, "A": A, "n": n,
        "trM_combiner": mp.nstr(abs(trM_comb), dps),
        "trM_transfer": mp.nstr(abs(tr_ref), dps),
        "abs_diff": mp.nstr(abs_d, 6),
        "rel_diff": mp.nstr(rel_d, 6),
        "combiner_wall_s": round(comb_wall, 2),
        "transfer_wall_s": round(ref_wall, 3),
    }


def main() -> int:
    # D (A=2) and ³He (A=3) — both fast (inner d_ξ ≤ 16). ⁴He validated in
    # a_operator_recursive_he4_crosscheck.py (~25 min, ξ⊢9).
    for label, (Z, N) in [("D", (1, 1)), ("3He", (2, 1))]:
        r = tr_m_via_combiner(Z, N)
        print(f"{label} (Z={Z},N={N}): combiner={r['trM_combiner']}  "
              f"transfer={r['trM_transfer']}  rel={r['rel_diff']}  "
              f"({r['combiner_wall_s']}s vs {r['transfer_wall_s']}s)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
