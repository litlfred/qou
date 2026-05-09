#!/usr/bin/env python3
"""
per_irrep_pole_proton_h3.py — Path A scaffolding for the categorical
derivation of the per-proton pole order `18` from
`prop:per-nucleon-shift-additive-linearity`.

**Status:** Research-grade scaffolding only.  See
`docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md`
for the three derivation paths (A: seminormal pole-order, B:
q-ribbon-tableau, C: KLR/categorification).

This script implements **Path A** as a tractable starting point: for
each $\\lambda \\in \\{(3), (2, 1), (1, 1, 1)\\}$ at $H_3$, compute the
Hoefsmit seminormal trace $\\chi^\\lambda_q(\\beta_p)$ on the proton's
canonical 11-crossing word $\\beta_p = $ `atom_braid_word_3A(1, 0)`,
restricted to its $H_3$ block, and report the pole order at
$q \\to 0$ (i.e. negative $u$-power) of the matrix entries.

The maximizer $\\mu_p^\\ast$ should be the column partition $(1^3)$
(per the conjecture in the audit doc); the maximum negative-$u$-power
of $\\chi^{(1^3)}_q(\\beta_p)$ should equal `18`.

This validates the empirical AXKIA input cited in
[`prop:per-nucleon-shift-additive-linearity`](
../../content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md
) (`18Z + 21N + 1`).

Witness: per-irrep-pole-proton-h3.witness.json (TODO once the
script is filled in)

Audit doc: docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md

@module folio-assistant/computations/per_irrep_pole_proton_h3
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from hoefsmit_symbolic import Q, chi_lambda_symbolic  # noqa: E402

# Note: H_3 has 3 partitions of 3 — (3), (2,1), (1,1,1)
H3_PARTITIONS = [(3,), (2, 1), (1, 1, 1)]


def proton_h3_crossings():
    """Build the proton's H_3 canonical word.

    Source of truth: `mass_at_3A_proper.atom_braid_word_3A(Z=1, N=0)`,
    truncated to the H_3 block (the first proton block).  The full
    atomic word `β_atomic(Z=1, N=0)` already lives in H_3 since the
    proton is a single-block atom (Z+N=1, A=1, 3A=3).

    Returns: list of (gen_idx, ctype) crossings consumable by
    `chi_lambda_symbolic`.
    """
    return atom_canonical_crossings(1, 0)


def chi_lambda_q_proton(shape: tuple) -> sp.Expr:
    """Compute χ^λ_q(β_p) symbolically.

    Returns sympy expression in q.
    """
    crossings = proton_h3_crossings()
    return chi_lambda_symbolic(shape, crossings)


def negative_u_pole_order(chi_q: sp.Expr) -> int:
    """Largest k such that q^{-k} appears with non-zero coefficient
    in `chi_q` (Laurent series in q centred at 0).

    The substrate parameter `q ↔ u` correspondence: pole order at
    `u → 0` corresponds to pole order at `q → 0` modulo the Hecke
    skein relation $\\sigma_i - \\sigma_i^{-1} = q - q^{-1}$.

    TODO(path-a): implement Laurent expansion at q=0.  For rational
    expressions in q, this is `sp.degree(sp.numer(chi_q), 1/q) -
    sp.degree(sp.denom(chi_q), 1/q)`.  Care needed when q appears
    only in numerator or only in denominator.
    """
    # Stub — research-grade.  Returns sentinel until implemented.
    raise NotImplementedError(
        "Path A pole-order analysis is research-grade.  "
        "See docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md "
        "for the three implementation paths."
    )


def main() -> int:
    """Print χ^λ_q(β_p) for each λ ⊢ 3 at H_3.  Filling in the
    pole-order analysis recovers the empirical AXKIA `18` constant."""
    print("=" * 80)
    print("  Per-irrep pole order — proton β_p at H_3 (Path A scaffold)")
    print("=" * 80)
    print()
    print("  Crossings (canonical word from atom_braid_word_3A(1, 0)):")
    crossings = proton_h3_crossings()
    print(f"    {len(crossings)} crossings")
    for i, (g, c) in enumerate(crossings):
        print(f"    [{i:2}]  σ_{g}  ({c})")
    print()
    print("  χ^λ_q(β_p) for each λ ⊢ 3:")
    for lam in H3_PARTITIONS:
        chi = chi_lambda_q_proton(lam)
        print(f"    λ = {lam}:  χ = {sp.simplify(chi)}")
    print()
    print("  TODO(Path A): implement `negative_u_pole_order` and verify")
    print("  the maximizer μ_p* = (1,1,1) yields pole order 18.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
