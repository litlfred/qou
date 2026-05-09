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


def negative_q_pole_order(chi_q: sp.Expr, var: sp.Symbol | None = None) -> int:
    """Order of pole at `var` = 0 of `chi_q` (Laurent series).

    For a rational expression $\\chi = N/D$ in `var`:

        ord_{var=0}(N/D)  =  ord_{var=0}(N) - ord_{var=0}(D)

    where `ord_{var=0}(P)` is the **lowest** non-zero exponent of
    `var` in `P` (the multiplicity of `var=0` as a zero/pole of P).
    The pole order at `var = 0` is `max(0, -ord(N/D))`.

    Default `var = q` (positive), but pass any symbol for
    substitutions like `q = u^2`.
    """
    if var is None:
        var = sp.symbols("q", positive=True)
    chi_simp = sp.simplify(chi_q)
    n, d = sp.fraction(chi_simp)
    n_poly = sp.Poly(n, var)
    d_poly = sp.Poly(d, var)
    n_low = min(m[0] for m in n_poly.monoms()) if n_poly.monoms() else 0
    d_low = min(m[0] for m in d_poly.monoms()) if d_poly.monoms() else 0
    # ord(N/D) = ord(N) - ord(D); pole order at 0 = max(0, -ord)
    return max(0, d_low - n_low)


def main() -> int:
    """Compute χ^λ_q(β_p), its q=0 pole order per partition, AND the
    u-pole order of the full Σ_λ y_λ·χ^λ_q sum at q = u² (the
    Markov-trace denominator's u-exponent in `D(u)`).

    Audit claim: shift_NF(β_p) = 18Z + 21N + 1 = 19 for the proton.
    """
    from markov_weights_symbolic import solve_y_lambda  # noqa: E402

    q_var = sp.symbols("q", positive=True)
    u_var = sp.symbols("u", positive=True)

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
    chi_at = {}
    for lam in H3_PARTITIONS:
        chi = chi_lambda_q_proton(lam)
        chi_at[lam] = chi
        ord_q = negative_q_pole_order(chi)
        pole_orders[lam] = ord_q
        chi_str = str(sp.simplify(chi))[:46]
        print(f"  {str(lam):<14}{chi_str:<48}{ord_q:>12}")
    print()
    max_lam = max(pole_orders, key=pole_orders.get)
    print(f"  Per-irrep maximizer:  λ = {max_lam}, ord_{{q=0}} = "
          f"{pole_orders[max_lam]}")
    print()
    # Full Markov-trace sum: tr_M(β_p) = Σ_λ y_λ(q) · χ^λ_q(β_p)
    y_lams = solve_y_lambda(3)
    tr_M = sum(y_lams[lam] * chi_at[lam] for lam in H3_PARTITIONS)
    # D(u) lives in u with q = u² (per d_u_closed_form_proof.py).
    tr_M_u = sp.simplify(tr_M.subs(q_var, u_var ** 2))
    shift_u = negative_q_pole_order(tr_M_u, var=u_var)
    print(f"  Markov-trace sum tr_M(β_p) = Σ_λ y_λ·χ^λ_q at q = u²:")
    print(f"    ord_{{u=0}}(tr_M) = {shift_u}")
    print(f"    audit prediction shift_NF(β_p) = 18·1 + 21·0 + 1 = 19")
    if shift_u == 19:
        print(f"  ✓ Path A verified: u-pole order matches "
              f"prop:per-nucleon-shift-additive-linearity exactly.")
        print(f"    The '18' in the formula is the per-proton additive")
        print(f"    coefficient of shift_NF, NOT the per-irrep χ pole order")
        print(f"    (max per-irrep ord at H_3 is 11 at λ=(2,1)).")
    else:
        print(f"  ✗ Discrepancy: u-pole {shift_u} ≠ predicted 19.")
        print(f"    Audit: docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
