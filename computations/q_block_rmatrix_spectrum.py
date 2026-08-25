#!/usr/bin/env python3
"""Full-matrix spectrum of the block-swap braid β — the R-matrix eigenvalues.

Owner correction (2026-06-11): "don't assume scalar — have full matrices." My
#2120 reduced the symmetrizer to a scalar reweighting of {id, β} traces, which is
WRONG: the block-swap β (two 3-strand blocks) is a BRAID, not an involution
(β² = full twist ≠ id), and the proton module is reducible (it spans the H₃
blocks (3),(2,1),(1,1,1)), so β's R-matrix has MORE than two eigenvalues. The
spectral projector is a polynomial in β needing β, β², …, β^d — not span{id, β}.

This builds β as the FULL seminormal matrix on the two-proton H₆ space (block-swap
of strands [0,1,2]↔[3,4,5]) in every λ⊢6 block (dims ≤ 16) and diagonalizes it,
collecting the distinct R-matrix eigenvalues. The number of distinct eigenvalues
d+1 fixes how many powers tr_M(W·β^k), k=0..d, the EXACT q-correct spectral
projector requires — quantifying how far the {id,β} scalar reduction falls short.

Output: q-block-rmatrix-spectrum.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from per_irrep_pole_atom import parts_of  # noqa: E402
from derived_chi_catalogue_matrix_m_mpfr import seminormal_matrices_mpfr  # noqa: E402
from block_swap_binding import block_swap_word  # verified block-swap word  # noqa: E402


def _to_np(M, dim):
    return np.array([[complex(M[i, j]) for j in range(dim)] for i in range(dim)])


def main() -> int:
    t0 = time.monotonic()
    q = Q0
    n = 6
    beta_word = block_swap_word(0, 3, n)   # 0-based gens swapping [0,1,2]↔[3,4,5]
    print("=" * 78)
    print(f" Block-swap braid β spectrum on H₆ (two 3-strand blocks)")
    print(f"   q₀ = {float(q):.6f}   β word (0-based gens) = {beta_word}  "
          f"(length {len(beta_word)})")
    print("=" * 78)
    print(f" {'λ⊢6':>14}{'dim':>5}{'eigenvalues of β (rounded)':>44}")
    print(" " + "-" * 70)

    all_eigs = []
    rows = []
    for shape in parts_of(n):
        st = tuple(shape)
        sig = seminormal_matrices_mpfr(st, q)        # [σ_0 … σ_4] (0-based gens)
        dim = sig[0].rows if sig else 1
        B = mp.eye(dim)
        for g in beta_word:
            B = B * sig[g]
        eigs = np.linalg.eigvals(_to_np(B, dim))
        ev = sorted([complex(round(e.real, 6), round(e.imag, 6)) for e in eigs],
                    key=lambda z: (round(z.real, 4), round(z.imag, 4)))
        all_eigs.extend(ev)
        rows.append({"partition": list(st), "dim": dim,
                     "eigenvalues": [[e.real, e.imag] for e in ev]})
        shown = ", ".join(f"{e.real:+.3f}{'' if abs(e.imag)<1e-6 else f'{e.imag:+.3f}i'}"
                          for e in ev[:6]) + (" …" if len(ev) > 6 else "")
        print(f" {str(st):>14}{dim:>5}  {shown:>42}")
    print(" " + "-" * 70)

    # distinct eigenvalues (rounded) across all blocks → minimal-polynomial degree.
    distinct = sorted(set((round(e.real, 5), round(e.imag, 5)) for e in all_eigs),
                      key=lambda z: (z[0], z[1]))
    d_plus_1 = len(distinct)
    print(f" distinct eigenvalues across all λ⊢6: {d_plus_1}")
    for re_, im_ in distinct:
        tag = ""
        if abs(im_) < 1e-6:
            if abs(re_ - float(q)) < 1e-3:
                tag = "  ≈ q (symmetric/Hecke)"
            elif abs(re_ + 1 / float(q)) < 1e-3:
                tag = "  ≈ −q⁻¹ (antisym/Hecke)"
        print(f"    {re_:+.5f}{'' if abs(im_)<1e-6 else f'{im_:+.5f}i'}{tag}")
    print(f"\n ⇒ the exact spectral projector is a degree-{d_plus_1-1} polynomial in β:")
    print(f"   it needs tr_M(W·β^k) for k=0..{d_plus_1-1} — the {{id,β}} scalar "
          f"reduction (k≤1) is INSUFFICIENT (β has {d_plus_1} ≠ 2 eigenvalues).")

    w = WitnessBuilder("q-block-rmatrix-spectrum", engine="python+mpmath",
                       start_time=t0)
    w.set_description(
        "Full-matrix spectrum of the block-swap braid β (two 3-strand blocks) on "
        "the H₆ seminormal rep, per λ⊢6. β is a BRAID (β²=full twist≠id) on a "
        "reducible module, so it has more than the Hecke {q,−q⁻¹} eigenvalues — "
        f"{d_plus_1} distinct across all blocks. The exact q-correct spectral "
        f"projector is therefore a degree-{d_plus_1-1} polynomial in β, needing "
        f"tr_M(W·β^k) for k=0..{d_plus_1-1}; the #2120 {{id,β}} scalar reweighting "
        "(k≤1) is insufficient. Quantifies the owner's 'don't assume scalar' "
        "correction and sets the power-set for the exact block-swap S_atom."
    )
    w.add_parameter("q0", float(q))
    w.add_parameter("n_strands", n)
    w.add_data("beta_word_0based", beta_word)
    w.add_data("per_block", rows)
    w.add_data("distinct_eigenvalues", [{"re": r, "im": i} for r, i in distinct])
    w.add_data("n_distinct_eigenvalues", d_plus_1)
    w.add_data("spectral_projector_degree", d_plus_1 - 1)
    w.add_data("powers_needed_k", list(range(d_plus_1)))
    out = w.save()
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
