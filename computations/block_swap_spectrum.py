#!/usr/bin/env python3
"""Generic full-matrix block-swap spectral-projector infra (any block size m, any n).

Owner directive (2026-06-11): generalize the H₆ block-swap spectrum finding into
reusable compute infra. "Don't assume scalar — have full matrices."

The block-swap braid β (swap two adjacent m-strand blocks) is a BRAID, not an
involution: β² = full twist ≠ id, and on a reducible module it carries far more
than the Hecke {q, −q⁻¹} eigenvalues (22 distinct at m=3, n=6). The q-correct
symmetrizer is therefore the FULL spectral projector — a polynomial in β of degree
(#distinct eigenvalues − 1), NOT the rank `(β+q⁻¹)/(q+q⁻¹)` that assumes the Hecke
relation. This module provides:

- `block_swap_word(m, start, n)`   — the verified block-transposition braid word
- `beta_matrix(shape, word, q)`    — β as a full mpmath seminormal matrix per λ⊢n
- `spectrum(m, n, q, start)`       — eigenvalues per λ⊢n (numpy diagonalization)
- `lagrange_spectral_projector(B, target, eigs)` — Π_{μ≠target}(B−μ)/(target−μ),
  the projector onto the `target`-eigenspace (idempotent; verified)
- `q1_swap_multiplicities(m, n, start)` — the plain-swap (q=1) ±1 eigenspace dims
  (dim S²/Λ² of the symmetric/antisymmetric subspaces), the q→1 anchor that
  labels which q-eigenvalues are bosonic vs fermionic.

Lean backing: the generator-level case (β satisfies the Hecke relation ⇒ 2
eigenvalues ⇒ rank projectors `e_±`) is proved idempotent/orthogonal/complete in
`QOU.Hecke.SpectralProjector`; this module is the general-word extension.

Output (when run): block-swap-spectrum-infra.witness.json
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

mp.mp.dps = 40

from per_irrep_pole_atom import parts_of  # noqa: E402
from derived_chi_catalogue_matrix_m_mpfr import seminormal_matrices_mpfr  # noqa: E402


def block_swap_word(m: int, start: int, n: int) -> list[int]:
    """Reduced word (0-based gens) swapping adjacent m-blocks at [start, start+m)
    and [start+m, start+2m).  SELF-VERIFIED against the realized permutation."""
    target = list(range(n))
    for p in range(start, start + m):
        target[p] = p + m
    for p in range(start + m, start + 2 * m):
        target[p] = p - m
    inv = [0] * n
    for i, t in enumerate(target):
        inv[t] = i
    cur = list(range(n))
    word: list[int] = []
    for pos in range(n):
        ci = cur.index(inv[pos])
        while ci > pos:
            cur[ci], cur[ci - 1] = cur[ci - 1], cur[ci]
            word.append(ci - 1)
            ci -= 1
    # verify
    arr = list(range(n))
    for j in word:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    realized = [0] * n
    for idx, s in enumerate(arr):
        realized[s] = idx
    assert realized == target, "block_swap_word does not realize the block transposition"
    return word


def beta_matrix(shape: tuple[int, ...], word: list[int], q: mp.mpf):
    """β = Π σ_g (0-based gens) as a full seminormal mpmath matrix for λ = shape."""
    sig = seminormal_matrices_mpfr(shape, q)
    dim = sig[0].rows if sig else 1
    B = mp.eye(dim)
    for g in word:
        B = B * sig[g]
    return B, dim


def _to_np(M, dim):
    return np.array([[complex(M[i, j]) for j in range(dim)] for i in range(dim)])


def spectrum(m: int, n: int, q: mp.mpf, start: int = 0):
    """Per-λ⊢n eigenvalues of the block-swap β (numpy diagonalization)."""
    word = block_swap_word(m, start, n)
    out = {}
    for shape in parts_of(n):
        st = tuple(shape)
        B, dim = beta_matrix(st, word, q)
        out[st] = list(np.linalg.eigvals(_to_np(B, dim)))
    return out, word


def lagrange_spectral_projector(B, target, eigs, tol: float = 1e-6):
    """Spectral projector onto the `target` eigenvalue: Π_{μ≠target}(B−μ)/(target−μ).

    `eigs` = the DISTINCT eigenvalues. Returns (P, idempotency_residual ‖P²−P‖)."""
    dim = B.shape[0]
    P = np.eye(dim, dtype=complex)
    for mu in eigs:
        if abs(mu - target) < tol:
            continue
        P = P @ (B - mu * np.eye(dim, dtype=complex)) / (target - mu)
    resid = float(np.max(np.abs(P @ P - P)))
    return P, resid


def q1_swap_multiplicities(m: int, n: int, start: int = 0):
    """Plain-swap (q=1) ±1 eigenspace dims per λ⊢n — the bosonic/fermionic anchor.

    At q=1 the block-swap is an involution s (s²=1); dim(+1)=dim S² (bosonic),
    dim(−1)=dim Λ² (fermionic). Computed from tr(s) = #fixed SYT-pairs via the
    seminormal matrices at q→1 (q=1+ε numerically, then round)."""
    q1 = mp.mpf("1.0000001")
    word = block_swap_word(m, start, n)
    res = {}
    for shape in parts_of(n):
        st = tuple(shape)
        B, dim = beta_matrix(st, word, q1)
        ev = np.linalg.eigvals(_to_np(B, dim)).real
        n_plus = int(round(sum(1 for e in ev if e > 0)))
        res[st] = {"dim": dim, "dim_sym_+1": n_plus, "dim_antisym_-1": dim - n_plus}
    return res


def main() -> int:
    import json
    from witness_base import WitnessBuilder
    from q_parameter import Q_MP as q0
    t0 = time.monotonic()

    print("=" * 80)
    print(" Generic block-swap spectral-projector infra — demo + idempotency check")
    print("=" * 80)
    demos = [(2, 4), (3, 6)]   # (block size m, n strands): swap two m-blocks
    rows = []
    for m, n in demos:
        spec, word = spectrum(m, n, q0)
        all_ev = [e for evs in spec.values() for e in evs]
        distinct = sorted(set(complex(round(e.real, 5), round(e.imag, 5)) for e in all_ev),
                          key=lambda z: (z.real, z.imag))
        # pick the largest-|λ| block and verify a Lagrange projector is idempotent
        big = max(spec, key=lambda s: len(spec[s]))
        B, dim = beta_matrix(big, word, q0)
        Bnp = _to_np(B, dim)
        d_ev = sorted(set(complex(round(e.real, 6), round(e.imag, 6))
                          for e in np.linalg.eigvals(Bnp)), key=lambda z: z.real)
        _, resid = lagrange_spectral_projector(Bnp, d_ev[-1], d_ev)
        mult = q1_swap_multiplicities(m, n)
        tot_sym = sum(v["dim_sym_+1"] for v in mult.values())
        tot_anti = sum(v["dim_antisym_-1"] for v in mult.values())
        rows.append({"m_block": m, "n_strands": n, "word_len": len(word),
                     "n_distinct_eigs": len(distinct),
                     "projector_idempotency_resid": resid,
                     "total_dim_sym_q1": tot_sym, "total_dim_antisym_q1": tot_anti})
        print(f"\n  m={m}, n={n}: β word length {len(word)}, "
              f"{len(distinct)} distinct eigenvalues across λ⊢{n}")
        print(f"    Lagrange projector (top eigval, block {big}, dim {dim}): "
              f"‖P²−P‖ = {resid:.2e}  {'✓ idempotent' if resid < 1e-6 else '✗'}")
        print(f"    q→1 anchor: Σ dim S²(bosonic) = {tot_sym}, "
              f"Σ dim Λ²(fermionic) = {tot_anti}  (total {tot_sym+tot_anti})")

    w = WitnessBuilder("block-swap-spectrum-infra", engine="python+mpmath",
                       start_time=t0)
    w.set_description(
        "Generic full-matrix block-swap spectral-projector infra (any block size m, "
        "any n). β (block-transposition braid) is built as a full seminormal matrix "
        "per λ⊢n; its spectrum carries far more than the Hecke {q,−q⁻¹} pair (a "
        "braid, β²=full twist≠id, on a reducible module). The Lagrange spectral "
        "projector Π_{μ≠λ}(β−μ)/(λ−μ) is verified idempotent (‖P²−P‖<1e-6). The q→1 "
        "swap multiplicities (dim S²/Λ²) anchor which q-eigenvalues are bosonic vs "
        "fermionic. Demos: (m=2,n=4) and (m=3,n=6, the 22-eigenvalue ⁴He proton-"
        "pair). Generalizes q_block_rmatrix_spectrum.py; Lean backing for the "
        "generator-level rank case in QOU.Hecke.SpectralProjector."
    )
    w.add_data("demos", rows)
    w.add_assertion(
        name="lagrange_projector_idempotent",
        computed=max(r["projector_idempotency_resid"] for r in rows),
        expected=0.0, tolerance=1e-6,
        source="max ‖P²−P‖ over the demo blocks — the full-matrix spectral "
               "projector built from β's actual spectrum is idempotent.",
    )
    out = w.save()
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
