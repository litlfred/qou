#!/usr/bin/env python3
"""
per_irrep_pole_proton_h3.py — Path A verification of the per-proton
shift exponent in `prop:per-nucleon-shift-additive-linearity`.

For the proton ($Z = 1$, $N = 0$, $A = 1$, $n = 3$) this script:

  1. Computes $\\chi^\\lambda_q(\\beta_p)$ for each $\\lambda \\vdash 3$
     via the Hoefsmit seminormal representation (symbolic in $q$).
  2. Reports the q=0 pole order of each per-irrep $\\chi^\\lambda_q$.
  3. Sums $\\mathrm{tr}_M(\\beta_p) = \\sum_\\lambda y_\\lambda(q) \\chi^\\lambda_q(\\beta_p)$
     (Wenzl Jones-Markov $y_\\lambda$ at $n = 3$).
  4. Substitutes $q = u^2$ (the $D(u)$ convention from
     `d_u_closed_form_proof.py`) and reports
     $\\mathrm{ord}_{u=0}(\\mathrm{tr}_M(\\beta_p))$.

**Verified result:** $\\mathrm{ord}_{u=0}(\\mathrm{tr}_M(\\beta_p)) = 19$,
matching $\\mathrm{shift}_{\\mathrm{NF}}(\\beta_p) = 18 \\cdot Z + 21 \\cdot N + 1$
at $(Z, N) = (1, 0)$ from `prop:per-nucleon-shift-additive-linearity`.

The per-irrep maximum at $H_3$ is $11$ (at $\\lambda = (2, 1)$),
NOT $18$.  The "$18$" in the formula is the per-proton additive
coefficient of the FULL $u$-pole order of $\\mathrm{tr}_M$, not a
per-irrep $q$-pole order.  See audit doc for the reading correction.

Witness: per-irrep-pole-proton-h3.witness.json (CI-integrated)
Audit doc: docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md

@module computations/per_irrep_pole_proton_h3
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
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

    Emits per-irrep-pole-proton-h3.witness.json with the result
    table + assertions verifying shift_NF(β_p) = 19.
    """
    from markov_weights_symbolic import solve_y_lambda  # noqa: E402
    from witness_base import WitnessBuilder  # noqa: E402

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
    max_ord = pole_orders[max_lam]
    print(f"  Per-irrep maximizer:  λ = {max_lam}, ord_{{q=0}} = "
          f"{max_ord}")
    print()
    # Full Markov-trace sum: tr_M(β_p) = Σ_λ y_λ(q) · χ^λ_q(β_p)
    y_lams = solve_y_lambda(3)
    tr_M = sum(y_lams[lam] * chi_at[lam] for lam in H3_PARTITIONS)
    # D(u) lives in u with q = u² (per d_u_closed_form_proof.py).
    tr_M_u = sp.simplify(tr_M.subs(q_var, u_var ** 2))
    shift_u = negative_q_pole_order(tr_M_u, var=u_var)
    expected_shift = 18 * 1 + 21 * 0 + 1  # = 19
    print(f"  Markov-trace sum tr_M(β_p) = Σ_λ y_λ·χ^λ_q at q = u²:")
    print(f"    ord_{{u=0}}(tr_M) = {shift_u}")
    print(f"    audit prediction shift_NF(β_p) = 18·1 + 21·0 + 1 = "
          f"{expected_shift}")
    success = shift_u == expected_shift
    if success:
        print(f"  ✓ Path A verified: u-pole order matches "
              f"prop:per-nucleon-shift-additive-linearity exactly.")
    else:
        print(f"  ✗ Discrepancy: u-pole {shift_u} ≠ predicted {expected_shift}.")

    # Emit witness JSON.
    builder = (
        WitnessBuilder(name="per-irrep-pole-proton-h3", engine="sympy")
        .set_description(
            "Path A: symbolic Hoefsmit seminormal pole-order analysis "
            "of the proton's canonical 11-crossing braid word at H_3. "
            "Computes per-irrep χ^λ_q(β_p) for each λ ⊢ 3, then sums "
            "Σ_λ y_λ(q)·χ^λ_q (Wenzl Jones-Markov weights) and reports "
            "ord_{u=0}(tr_M) at q = u². Verifies shift_NF(β_p) = 19 = "
            "18·1 + 21·0 + 1, exactly matching "
            "prop:per-nucleon-shift-additive-linearity for the proton."
        )
        .set_audit_only(
            "docs/audits/2026-05-08-per-irrep-pole-18-21-research-note.md"
        )
    )
    per_irrep = []
    for lam in H3_PARTITIONS:
        per_irrep.append({
            "partition": list(lam),
            "chi_lambda_q_simplified": str(sp.simplify(chi_at[lam])),
            "ord_q_eq_0_negative": int(pole_orders[lam]),
        })
    builder.add_data("per_irrep_pole_orders_at_q_eq_0", per_irrep)
    builder.add_data("per_irrep_maximizer", {
        "partition": list(max_lam),
        "ord_q_eq_0_negative": int(max_ord),
        "note": (
            "Per-irrep max at H_3 is 11 (at λ=(2,1)); this is NOT the "
            "audit's '18'. The '18' is the per-proton additive "
            "coefficient of the FULL summed tr_M u-pole order."
        ),
    })
    builder.add_data("full_tr_M_u_pole", {
        "ord_u_eq_0": int(shift_u),
        "expected": expected_shift,
        "formula": "shift_NF(β_p) = 18·Z + 21·N + 1 at (Z=1, N=0) = 19",
    })
    builder.add_assertion(
        name="per_irrep_max_ord_q_eq_11",
        computed=int(max_ord),
        expected=11,
    )
    builder.add_assertion(
        name="full_tr_M_u_pole_eq_shift_NF_proton",
        computed=int(shift_u),
        expected=expected_shift,
    )
    builder.add_data("lean_uniqueness_ref", lean_uniqueness_ref("proton"))
    out_path = builder.save()
    print(f"\n  Witness emitted: {out_path}")
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
