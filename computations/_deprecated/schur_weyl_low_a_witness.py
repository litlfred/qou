#!/usr/bin/env python3
"""
P2.2a — Schur–Weyl H_{3A} weights for low A (D, ³He, ⁴He)

Wires schur_weyl_symbolic.global_wedderburn_sum_symbolic into a
witness comparing the **proper** H_{3A} Wedderburn weights against
the **H_3-at-H_{3A} approximation** that the live mass tower
currently uses (per
docs/audits/2026-05-01-h3-at-h3a-weight-derivation.md).

For each light nucleus:

  D   (Z=1, N=1, A=2, n=6,  p(6)=11 partitions)
  ³He (Z=2, N=1, A=3, n=9,  p(9)=30 partitions)
  ⁴He (Z=2, N=2, A=4, n=12, p(12)=77 partitions)

we compute:

  proper:  Σ_{λ ⊢ 3A} w_λ(q) · χ^λ(𝒜)         via schur_weyl_symbolic
  h3_approx: (w_sym + w_std + w_alt)^{3A-1}    the broken approximation

and report (a) the proper symbolic form, (b) numerical evaluation
at q_0, (c) the H_3 approximation evaluation, and (d) per-partition
contribution magnitudes.

Goal: confirm that proper H_{3A} weights produce |Σ w_λ χ^λ| < q
(restoring Φ_q convergence) where the H_3 approximation produces
divergent values.

Witness: docs/audits/2026-05-01-p2-2a-schur-weyl-low-a.witness.json
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from schur_weyl_symbolic import (
    global_wedderburn_sum_symbolic,
    h3_additive_approximation_symbolic,
)
from witness_polynomial import expose_polynomial
from q_parameter import Q as Q0_FLOAT

q = sp.Symbol("q", positive=True, real=True)
q0 = sp.Rational(str(Q0_FLOAT))

ATOMS = [
    ("D", 1, 1, 2),
    ("3He", 2, 1, 3),
    ("4He", 2, 2, 4),
]


def analyze(name, Z, N, A):
    print(f"\n=== {name} (Z={Z}, N={N}, A={A}, n=3A={3*A}) ===")

    # Proper Schur-Weyl sum
    proper, terms = global_wedderburn_sum_symbolic(
        A, q, char_kind="mn-atom", Z=Z, N=N, include_inter=True
    )
    proper_at_q0 = sp.N(proper.subs(q, q0), 50)
    print(f"  proper Σ:  {proper}")
    print(f"  at q_0:    {proper_at_q0}")
    print(f"  partitions used: {len(terms)}")

    # H_3 approximation (the broken one)
    h3_approx = h3_additive_approximation_symbolic(A, q)
    h3_at_q0 = sp.N(h3_approx.subs(q, q0), 50)
    print(f"  H_3 approx: {h3_approx}")
    print(f"  at q_0:     {h3_at_q0}")

    # Convergence diagnostic — is proper |Σ| < q_0?
    proper_abs = abs(complex(proper_at_q0))
    h3_abs = abs(complex(h3_at_q0))
    q0_float = float(q0)
    proper_phi_convergent = proper_abs < q0_float
    h3_phi_convergent = h3_abs < q0_float
    print(
        f"  Φ_q convergence (|·| < q_0={q0_float:.6f}):  "
        f"proper={proper_phi_convergent} ({proper_abs:.4f}), "
        f"H_3={h3_phi_convergent} ({h3_abs:.4f})"
    )

    # Per-partition contribution magnitudes (top 5)
    contribs = sorted(
        [
            (str(t["partition"]), float(abs(complex(sp.N(t["contribution"].subs(q, q0))))))
            for t in terms
        ],
        key=lambda x: -x[1],
    )
    print(f"  top 5 partitions by |contribution|:")
    for lam, mag in contribs[:5]:
        print(f"    λ = {lam:30s} |c| = {mag:.6e}")

    # Polynomial-form exposure
    proper_form = expose_polynomial(proper, q, q0=q0, simplify=False)
    h3_form = expose_polynomial(h3_approx, q, q0=q0, simplify=False)

    return {
        "atom": name,
        "Z": Z,
        "N": N,
        "A": A,
        "n_strands": 3 * A,
        "n_partitions": len(terms),
        "proper_sw_sum": proper_form,
        "h3_approximation": h3_form,
        "convergence_diagnostic": {
            "q_0": float(q0),
            "proper_abs_at_q0": proper_abs,
            "h3_abs_at_q0": h3_abs,
            "proper_phi_convergent": proper_phi_convergent,
            "h3_phi_convergent": h3_phi_convergent,
        },
        "top_partitions": [
            {"partition": lam, "abs_contribution_at_q0": mag}
            for lam, mag in contribs[:5]
        ],
    }


print("=" * 80)
print("P2.2a — Schur–Weyl H_{3A} vs H_3-approximation for low A")
print("=" * 80)
print(f"q_0 = {q0}")

results = []
for name, Z, N, A in ATOMS:
    try:
        r = analyze(name, Z, N, A)
        results.append(r)
    except Exception as e:
        import traceback
        traceback.print_exc()
        results.append({"atom": name, "error": str(e)})

witness = {
    "audit": "P2.2a — Schur-Weyl H_{3A} weights vs H_3 approximation (low A)",
    "generated": datetime.now(timezone.utc).isoformat(),
    "q_0": str(q0),
    "atoms": results,
    "interpretation": (
        "Per docs/audits/2026-05-01-h3-at-h3a-weight-derivation.md, the "
        "H_3 weights applied per-generator at H_{3A} push V̂_i above "
        "the Φ_q convergence radius. The proper Schur-Weyl sum at "
        "H_{3A} (per-partition w_λ = s_λ(q,q⁻¹)/H_q(λ), summed against "
        "Murnaghan-Nakayama characters χ^λ) should produce |Σ| < q_0 "
        "so that Φ_q(|·|) converges. This witness compares the two."
    ),
}

out_path = Path(__file__).parent.parent.parent / "docs/audits/2026-05-01-p2-2a-schur-weyl-low-a.witness.json"
out_path.write_text(json.dumps(witness, indent=2, default=str))
print()
print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")
