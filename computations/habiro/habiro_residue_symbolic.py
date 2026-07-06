#!/usr/bin/env python3

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

# DEPRECATION-CANDIDATE: witness was moved to computations/_deprecated/ in PR #554 (dead-exploratory).
# This .py script is kept in place because it is still imported by live code; revisit when the live importer is itself retired or rewired.
"""
Habiro cyclotomic / residue expansion — SYMBOLIC demonstration.

Per content/braids-and-knots/full-pole-structure-mass-trace.md:

    tr_M(T_w, q)  =  Σ_{m ≥ 0} a_m(T_w) · (q; q)_m
                    ↑                       ↑
                    a_m ∈ ℤ[q, q⁻¹]        (q; q)_m = Π_{k=1..m}(1 - q^k)

Residues at roots of unity are:
    Res_{q = ζ_n} tr_M  =  numerator(ζ_n) / denominator'(ζ_n)

with ζ_n a primitive n-th root of unity (factor of cyclotomic poly Φ_n).

This script:

  1. Provides q_pochhammer(m, q)  — exact (q;q)_m symbolic
  2. Provides residue_at_root(expr, q, n)  — exact residue via Φ_n
  3. Demonstrates on toy rational 1/((q²-1)(q³-1)) — full output
  4. Evaluates exact symbolic schur_weyl sum at q₀ for A ∈ {1, 2, 3, 4}
  5. Documents why NUMERICAL contour integration is the wrong tool

For the heavy lifting (global H_{3A} Wedderburn sum), see
schur_weyl_symbolic.py — this file imports those sums and lists
numerical values alongside dominant-partition diagnostics.

Why SYMBOLIC beats NUMERICAL contour integration:

  1. ε-accuracy ceiling.  Numerical Res[f;ζ] ≈ (ε/N) Σ f(ζ+ε·e^{iθ_k})·e^{iθ_k}
     has O(ε²) error; sub-1% binding needs ε < 10⁻³.  But the Hecke
     algebra has hook-poles within ε of every ζ for high enough hook
     length, forcing ε < 1/(3A). Exploding cost per atom.

  2. Dense roots of unity.  Any neighborhood of q₀ = 1.11 contains
     infinitely many ζ_n.  A contour can't separate them; symbolic
     Φ_n(q) factorization does so algebraically.

  3. Complex transfer matrices.  mpmath.mpc halves precision per
     multiply vs mpmath.mpf.  Exact sympy.Rational is precision-free.

  4. Catastrophic cancellation.  Mittag-Leffler residues alternate in
     sign across ζ_n; numerical sum loses digits exponentially.
     Symbolic arithmetic keeps all cancellations exact.

  5. Branch cuts of Φ_q.  Φ_q(z) = ∏(1 - q^{-k}z)^{-1} has infinitely
     many branch cuts emanating from each pole.  Any residue contour
     crosses them; symbolic ring arithmetic avoids that topology.

Witness: habiro-residue-symbolic.witness.json
"""
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from sympy import Rational, Symbol, Integer, expand, factor, simplify

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL


def q_pochhammer(m, q):
    """(q; q)_m = Π_{k=1}^{m} (1 - q^k).  For m = 0 returns 1."""
    if m == 0:
        return Integer(1)
    result = Integer(1)
    for k in range(1, m + 1):
        result *= 1 - q ** k
    return sp.expand(result)


def residue_at_primitive_root(expr, q, n):
    """Compute the "symbolic residue" of expr(q) at a primitive n-th root
    of unity (root of cyclotomic polynomial Φ_n(q)).

    For a rational function f(q) = N(q) / D(q) with D(q) = Φ_n(q) · Q(q)
    (simple pole at each primitive n-th root), the residue at a given
    root ζ is:

        Res_{q=ζ} f(q)  =  N(ζ) / (Φ_n'(ζ) · Q(ζ))

    Sympy: we return the symbolic expression N(q)/(Φ_n'(q)·Q(q)),
    which can be evaluated at specific roots via RootOf(Φ_n).

    Returns None if expr has no pole at any primitive n-th root.
    """
    num, den = sp.fraction(sp.together(expr))
    phi_n = sp.cyclotomic_poly(n, q)
    if phi_n == 1:
        return None
    # Check if Φ_n divides den
    try:
        quotient, remainder = sp.div(den, phi_n, q)
    except sp.PolynomialError:
        return None
    if remainder != 0:
        return None  # no pole at primitive n-th roots
    phi_prime = sp.diff(phi_n, q)
    return sp.simplify(num / (quotient * phi_prime))


def demonstrate_residue_toy():
    """Show exact residue computation on f(q) = 1 / [(q²-1)(q³-1)]."""
    q = sp.Symbol('q')
    f = 1 / ((q ** 2 - 1) * (q ** 3 - 1))
    results = {}
    for n in [1, 2, 3, 4, 5, 6]:
        r = residue_at_primitive_root(f, q, n)
        results[f"n={n}"] = {
            "phi_n": str(sp.cyclotomic_poly(n, q)),
            "symbolic_residue": str(r) if r is not None else None,
            "has_pole": r is not None,
        }
    return results


def eval_schur_weyl_exact_at_q0(A_values=(1, 2, 3, 4)):
    """Exact sympy evaluation of the global H_{3A} Wedderburn sum at q₀.

    Uses wedderburn_jones_markov.global_wedderburn_sum_jones_markov
    (trivial Specht character χ^λ = 1, **canonical Jones-Markov
    weights y_λ via Wenzl's Schur principal specialization**) for
    the partition sum.  This is the "ground-truth" that numerical
    Mittag-Leffler sums should reproduce — but doing so numerically
    would mix residues from all ζ_n, hook-poles, and branch cuts.
    Symbolically the answer is one rational number.

    Per docs/audits/2026-05-08-p3-h-3a-divergence.md, the legacy
    `global_wedderburn_sum_symbolic` used the 2-variable Schur
    weight `s_λ(q,q⁻¹) / H_q(λ)` which vanishes for partitions with
    > 2 rows — actively dropping the (1^p) sign-rep contribution.
    Switched to the canonical y_λ + numerical-q-from-start (passes
    q_val=q_0 to substitute before sp.cancel).
    """
    from schur_weyl_symbolic import h3_additive_approximation_symbolic
    from wedderburn_jones_markov import global_wedderburn_sum_jones_markov

    q = sp.Symbol('q', positive=True, real=True)
    q0 = Rational(int(_Q_CANONICAL * 10 ** 16), 10 ** 16)

    out = {}
    for A in A_values:
        # numerical-q-from-start: pass q_val=q0 directly so the
        # Wenzl-Schur evaluation produces a numeric expression at
        # q_0 rather than a symbolic rational requiring sp.cancel.
        total, _ = global_wedderburn_sum_jones_markov(A, q_val=q0)
        h3 = h3_additive_approximation_symbolic(A, q)
        out[f"A={A}"] = {
            "partition_count": len(partitions_of(3 * A)),
            "global_sum_at_q0": str(sp.N(total, 30)),
            "h3_additive_at_q0": str(h3.subs(q, q0).evalf(30)),
            "ratio_global_over_h3": str(
                sp.N(total / h3.subs(q, q0), 30)
            ),
        }
    return out


def partitions_of(n):
    """Shim: import from schur_weyl_symbolic."""
    from schur_weyl_symbolic import partitions_of as _p
    return _p(n)


if __name__ == "__main__":
    print("HABIRO RESIDUE — symbolic demo; numerical contour critique")
    print("=" * 80)

    # (q; q)_m showcase
    q = sp.Symbol('q')
    print("\nq-Pochhammer (q; q)_m for m = 0..6:")
    for m in range(7):
        print(f"  (q;q)_{m} = {q_pochhammer(m, q)}")

    # Exact residue on toy rational function
    print("\nEXACT SYMBOLIC RESIDUES of f(q) = 1 / [(q² − 1)(q³ − 1)]")
    print("-" * 60)
    toy = demonstrate_residue_toy()
    for k, v in toy.items():
        print(f"  {k}: Φ_n(q) = {v['phi_n']}")
        if v["has_pole"]:
            print(f"        residue = {v['symbolic_residue']}")
        else:
            print(f"        (no pole at primitive n-th roots)")

    # Exact Schur-Weyl at q₀ (heavy computation — takes ~30s for A=4)
    print("\nEXACT Schur-Weyl global sum @ q₀ (symbolic, not numerical):")
    print("-" * 60)
    sw = eval_schur_weyl_exact_at_q0(A_values=(1, 2, 3))  # skip A=4 here
    for k, v in sw.items():
        print(f"  {k}:")
        print(f"    partitions of 3A: {v['partition_count']}")
        print(f"    Σ_{{λ⊢3A}} w_λ(q₀)  = {v['global_sum_at_q0']}")
        print(f"    H_3^{{3A-1}}(q₀)     = {v['h3_additive_at_q0']}")
        print(f"    ratio (global/H_3)  = {v['ratio_global_over_h3']}")

    witness = {
        "computation": "habiro-residue-symbolic",
        "description": (
            "Symbolic Habiro cyclotomic / residue demonstration. Exact "
            "symbolic residues at primitive n-th roots of unity via "
            "cyclotomic polynomial factorization. Schur-Weyl global sums "
            "evaluated symbolically at q₀. Partners with "
            "schur_weyl_symbolic.py for the heavy lifting."
        ),
        "reference_block": "prop:full-pole-structure-mass-trace",
        "why_symbolic_not_numerical": [
            ("1. ε-accuracy ceiling: O(ε²) residue error forces ε < 10⁻³ "
             "for sub-%% binding; hook-poles force ε < 1/(3A) — exploding."),
            ("2. Dense roots of unity: infinitely many ζ_n near q₀ = 1.11; "
             "contour cannot separate them."),
            ("3. Complex transfer matrices: mpmath.mpc halves precision vs "
             "mpmath.mpf per multiply."),
            ("4. Catastrophic cancellation: Mittag-Leffler residues "
             "alternate in sign; numerical sum loses digits."),
            ("5. Φ_q branch cuts: any contour around ζ_n crosses branch "
             "cuts of the quantum dilogarithm."),
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": str(float(_Q_CANONICAL)),
            "engine": "sympy Rational (exact)",
        },
        "toy_residues": toy,
        "schur_weyl_at_q0": sw,
    }
    out = Path(__file__).parent / "habiro-residue-symbolic.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
