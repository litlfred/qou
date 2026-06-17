#!/usr/bin/env python3
"""Necessary conditions for the s5-so3 keystone's Sasakian S¹-equivariant index.

The keystone open object: an index on the Wu manifold SU(3)/SO(3) reproducing the
q-Plancherel weights  W_λ = d_q(λ)²/[n]_q!.  Before building it, verify the
NECESSARY conditions any valid index must satisfy (formalize-first pruning) — see
docs/audits/2026-06-16-keystone-index-necessary-conditions.md.

  C1 normalization  Σ_λ W_λ   (≈0.982 at q0 — W_λ is NOT a probability measure;
                               expected, since the quantum dim d_q has no sum rule:
                               Σ d_λ²=n! holds for ORDINARY dims, not d_q. Only open
                               item: normalization convention d_q²/[n]! vs d_q²/Σd_q²)
  C2 conjugation    W_λ = W_λ' (EXACT — forces the chirality involution)
  C3 positivity     W_λ > 0    (genuine, not signed/virtual index)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))

from pyhecke import atom  # noqa: E402
import pyhecke.constants as c  # noqa: E402
from lr_coefficients import partitions_of  # noqa: E402
import mpmath as mp  # noqa: E402


def conjugate(lam: tuple) -> tuple:
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p >= i) for i in range(1, lam[0] + 1))


def main() -> int:
    mp.mp.dps = 30
    print(f"q0 = {float(c.q0):.8f}\n")
    print(f"  {'n':>2} {'Σ W_λ (C1)':>16} {'max|W_λ−W_λ′| (C2)':>20} {'min W_λ (C3)':>14}")
    for n in (3, 4, 5, 6):
        qn = atom.q_factorial(n)
        W = {tuple(l): atom.q_dimension(tuple(l)) ** 2 / qn for l in partitions_of(n)}
        tot = sum(W.values())
        sym = max(abs(W[l] - W[conjugate(l)]) for l in W)
        pos = min(W.values())
        print(f"  {n:>2} {float(tot):>16.12f} {float(sym):>20.2e} {float(pos):>14.4e}")
    print("\n  C2 conjugation symmetry exact; C3 positivity holds; C1 Σ≠1 at q0")
    print("  ([n]_q! ≠ Σ d_q² at q0 — coincide only at q=1) — see audit doc.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
