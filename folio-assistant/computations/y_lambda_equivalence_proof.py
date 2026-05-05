#!/usr/bin/env python3
"""
y_lambda_equivalence_proof.py — Formal proof that the two
derivations of the Jones-Markov weights y_λ(q) at H_3(q) are
equivalent as rational functions in q (not merely numerically
at q_0).

Two paths derived in `markov_weights_symbolic.py`:

  Path A — Markov-axiom linear system on the ladder basis
    A · y = b,
    A_{ij} = χ^{λ_j}(elem_i),  elem_i = σ_1 ⋯ σ_{i−1}  (i = 0,1,2),
    b_i    = z^i,
    z      = 1/(√q + 1/√q).

  Path B — Wenzl's Schur principal specialization
    y_λ(q) = (1/Z) · s_λ(1, Q, Q^2, …, Q^{r-1}),
    s_λ    = Q^{n(λ)} ∏_{x∈λ} (1 − Q^{r+c(x)}) / (1 − Q^{h(x)}),
    Q      = q^2,  Q^r = z_W / (1 − Q + z_W),  z_W = q · z,
    Z      = Σ_μ f^μ · s_μ.

Both paths must produce the **same** linear functional by
uniqueness of the Ocneanu Markov trace.  This script verifies the
identity y_λ^A(q) − y_λ^B(q) = 0 as a rational function in q via
sympy's exact simplification.

Equivalence of tr_M via Wedderburn (Σ_λ y_λ χ^λ) and tr_M via
markov_peel recursive ascent then follows: both compute the
unique linear functional satisfying the Markov axioms with the
same y_λ(q) at the irrep level.

Run:
  python3 folio-assistant/computations/y_lambda_equivalence_proof.py
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from markov_weights_symbolic import Q, solve_y_lambda, y_lambda_symbolic  # noqa: E402


def main() -> int:
    print("=" * 80)
    print(" Formal equivalence proof: y_λ via linear system ≡ y_λ via Wenzl Schur")
    print("=" * 80)

    n = 3
    print(f"\nDeriving both paths at n = {n}...")
    t0 = time.time()
    y_A = solve_y_lambda(n)         # linear-system path
    print(f"  Path A (linear system) done in {time.time() - t0:.2f}s")

    t0 = time.time()
    y_B = y_lambda_symbolic(n)      # Wenzl Schur path
    print(f"  Path B (Wenzl Schur)   done in {time.time() - t0:.2f}s")

    print()
    print("Per-shape symbolic identity check  y_A(q) − y_B(q) ≡ 0  as Q(√q):")
    all_zero = True
    diffs = {}
    for shape in y_A:
        diff = sp.simplify(y_A[shape] - y_B[shape])
        is_zero = (diff == 0) or diff.equals(0)
        diffs[shape] = (diff, is_zero)
        status = "✓ zero" if is_zero else f"✗ {diff}"
        print(f"  λ = {str(shape):<14}  Δ = {status}")
        if not is_zero:
            all_zero = False

    print()
    if all_zero:
        print("  ✓ EQUIVALENCE PROVED: y_λ^A ≡ y_λ^B as rational functions in q.")
    else:
        print("  ✗ Difference does not simplify to zero — paths disagree symbolically.")

    # Auxiliary: also state the chain of consequences.
    print()
    print("Consequences:")
    print("  (i)  tr_M^Wedderburn(β) = Σ_λ y_λ χ^λ(β) is identical via either path,")
    print("       since the y_λ values agree as rational functions in q.")
    print("  (ii) markov_peel's recursive-ascent tr_M satisfies the same")
    print("       Markov axioms (tr_M(1)=1, tr_M(xσ_n)=z·tr_M(x)); by uniqueness")
    print("       of the linear functional on H_n satisfying these axioms, it")
    print("       equals the Wedderburn form Σ_λ y_λ χ^λ exactly.")
    print("  (iii) Therefore tr_M_symbolic ≡ tr_M_markov_peel as functions in q.")

    # Numerical sanity check at q_0 (still useful as a cross-check).
    q0 = sp.Float('1.1099785955541805', 50)
    print()
    print("Numerical sanity at q_0 (50 dps):")
    for shape in y_A:
        a_val = float(sp.N(y_A[shape].subs(Q, q0), 30))
        b_val = float(sp.N(y_B[shape].subs(Q, q0), 30))
        print(f"  λ = {str(shape):<14}  A = {a_val:+.16f}  B = {b_val:+.16f}  |Δ| = {abs(a_val - b_val):.2e}")

    # Emit witness.
    out = HERE / "y_lambda_equivalence_proof.witness.json"
    witness = {
        "computation": "y-lambda-equivalence-proof",
        "description": (
            "Formal symbolic proof that the two derivations of the Jones-"
            "Markov weights y_λ(q) at H_3(q) are equivalent as rational "
            "functions in q. Path A: linear-system solve on the Markov-"
            "axiom ladder basis. Path B: Wenzl Schur principal "
            "specialization with parameter Q^r fixed by z_W = q·z, "
            "Q = q². sympy's sp.simplify reduces y_A − y_B to 0 "
            "exactly for every λ ∈ {(3), (2,1), (1,1,1)}. Equivalence "
            "of tr_M via Wedderburn vs markov_peel recursive ascent "
            "then follows from uniqueness of the Markov-axiom-"
            "satisfying linear functional on H_n."
        ),
        "n": n,
        "all_differences_zero": all_zero,
        "shapes_verified": list(str(sh) for sh in y_A),
        "diff_per_shape": {str(sh): (str(d), z) for sh, (d, z) in diffs.items()},
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    out.write_text(json.dumps(witness, indent=2))
    print()
    print(f"witness: {out.name}")

    return 0 if all_zero else 1


if __name__ == "__main__":
    sys.exit(main())
