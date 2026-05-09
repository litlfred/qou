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


def negative_q_pole_order(chi_q: sp.Expr) -> int:
    """Order of pole at q = 0 of `chi_q` (Laurent series in q).

    For a rational expression $\\chi(q) = N(q)/D(q)$ in q, the pole
    order at $q = 0$ is `deg_q(D) - ord_{q=0}(N)`, where the latter
    is the lowest non-zero exponent of q in N.  Returns 0 if chi is
    a polynomial (no negative-power terms).
    """
    q = sp.symbols("q", positive=True)
    chi_simp = sp.simplify(chi_q)
    n, d = sp.fraction(chi_simp)
    n_poly = sp.Poly(n, q)
    d_poly = sp.Poly(d, q)
    n_low = min(m[0] for m in n_poly.monoms()) if n_poly.monoms() else 0
    d_deg = d_poly.degree() if d_poly.is_zero is False else 0
    return max(0, d_deg - n_low)


def main() -> int:
    """Compute χ^λ_q(β_p) and its q=0 pole order for each λ ⊢ 3.

    Empirical claim from AXKIA: per-proton pole order = 18.  This
    script computes the concrete values; if the H_3 maximizer's
    q-pole order ≠ 18, the discrepancy isolates a substrate-map /
    convention factor (u ↔ q relationship) for the audit doc."""
    print("=" * 80)
    print("  Per-irrep pole order — proton β_p at H_3 (Path A)")
    print("=" * 80)
    print()
    print("  Crossings (canonical word from atom_braid_word_3A(1, 0)):")
    crossings = proton_h3_crossings()
    print(f"    {len(crossings)} crossings: "
          f"{[(g, c[0]) for g, c in crossings]}")
    print()
    print(f"  {'λ':<14}{'χ^λ_q(β_p) (simplified)':<48}{'ord_{q=0}':>12}")
    print("  " + "-" * 74)
    pole_orders = {}
    for lam in H3_PARTITIONS:
        chi = chi_lambda_q_proton(lam)
        ord_q = negative_q_pole_order(chi)
        pole_orders[lam] = ord_q
        chi_str = str(sp.simplify(chi))[:46]
        print(f"  {str(lam):<14}{chi_str:<48}{ord_q:>12}")
    print()
    max_lam = max(pole_orders, key=pole_orders.get)
    max_ord = pole_orders[max_lam]
    print(f"  Maximizer:    λ = {max_lam}, ord_{{q=0}} = {max_ord}")
    print(f"  AXKIA claim:  ord_{{q=0}}^(-) χ^{{μ_p*}}(β_p) = 18")
    if max_ord == 18:
        print(f"  ✓ AXKIA empirical input verified (Path A closed for proton).")
    else:
        print(f"  ✗ Discrepancy: {max_ord} ≠ 18.  Investigate substrate map u ↔ q")
        print(f"    (the AXKIA u-pole order in D(u) likely uses a different")
        print(f"    normalisation than the χ^λ_q q-pole order; e.g.")
        print(f"    u = h = q − q⁻¹ with substrate map non-trivial at q=0).")
        print(f"    Audit: docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
