"""H_3(q) Hoefsmit-seminormal Gram determinant — full symbolic factorization.

Companion to `gram_h3_symbolic_regression.py` (which asserts det at q_0
is non-zero numerically). This script computes the FULL symbolic
factorization of `det(gramMatrix u)` and emits it as a witness for
the Lean theorem `gramMatrix_det_ne_zero` discharge.

## Key finding (2026-05-25)

The original theorem statement was:

    gramMatrix_det_ne_zero (u : ℝ) (hu_pos : 0 < u) (hu_ne_one : u ≠ 1)
      : det ≠ 0

This is FALSE — the determinant has TWO positive real roots:
  u = 1                            (classical limit, expected)
  u ≈ 0.6823278038                 (root of u³ + u - 1 = 0)

The framework substrate q_0 ≈ 1.110 ⟹ u_0 ≈ 1.0535 > 1, so the framework
itself is unaffected; only the Lean theorem statement needs a tightened
hypothesis. See
`docs/audits/2026-05-25-gram-h3-det-second-root-correctness-finding.md`.

## Output

`gram-h3-det-factorization.witness.json` contains:

  - Full numerator polynomial in u, factored form
    (numerator degree 44 in u after rational-cancellation against
    the denominator u^10·(u²+1)^12)
  - Factor list (6 irreducible factors)
  - Numerical sign vs u table (proves two positive real roots)
  - Positivity certificate for u > 1 (each factor manifestly > 0)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402


def build_gram_h3_symbolic():
    """Build the symbolic Gram matrix on H_3(q) NF basis (u = √q)."""
    u = sp.Symbol("u", positive=True, real=True)
    e: dict[tuple[int, int], sp.Expr] = {}
    e[(0, 0)] = sp.Integer(1)
    e[(0, 1)] = e[(0, 2)] = u / (u**2 + 1)
    e[(0, 3)] = e[(0, 4)] = u**2 / (u**2 + 1) ** 2
    e[(0, 5)] = (u**2 + u - 1) / (u**2 + 1)
    e[(1, 1)] = e[(2, 2)] = (u**2 + u - 1) / u
    e[(1, 2)] = u**2 / (u**2 + 1) ** 2
    e[(1, 3)] = e[(1, 4)] = e[(2, 3)] = e[(2, 4)] = (u**2 + u - 1) / (u**2 + 1)
    big = (u**4 + u - 1) * (u**4 + u**3 - 1) / (u**2 * (u**2 + 1) ** 2)
    e[(1, 5)] = e[(2, 5)] = e[(3, 3)] = e[(4, 4)] = big
    e[(3, 4)] = ((u**2 + u - 1) / u) ** 2
    big5 = (u**10 + u**9 - u**8 - u**5 + u**2 + u - 1) / (u**4 * (u**2 + 1))
    e[(3, 5)] = e[(4, 5)] = big5
    e[(5, 5)] = (
        u**12 + u**11 - 2 * u**10 - u**9 + 2 * u**8 + u**7 - u**6 - u**5
        + 2 * u**4 + u**3 - 2 * u**2 - u + 1
    ) / u**6

    G = sp.zeros(6, 6)
    for (i, j), v in e.items():
        G[i, j] = v
        G[j, i] = v
    return G, u


def factorize_det(G: sp.Matrix, u: sp.Symbol) -> dict:
    """Compute det(G) and factor numerator/denominator. Returns dict."""
    # Multiply through by the per-entry common denominator to clear
    # fractions. Max (u²+1) power in any entry's denominator is 2
    # (e.g. G[0,3], G[1,5]); max u power is 6 (G[5,5]).
    common = u**6 * (u**2 + 1) ** 2
    G_poly = sp.zeros(6, 6)
    for i in range(6):
        for j in range(6):
            G_poly[i, j] = sp.expand(G[i, j] * common)

    # Berkowitz det is fastest for symbolic matrices
    t0 = time.time()
    det_poly = G_poly.det(method="berkowitz")
    t_det = time.time() - t0

    # det(G) = det_poly / common^6 (det scales by common^6 since every
    # entry was multiplied by common)
    det_G = sp.cancel(det_poly / common**6)
    num, denom = sp.fraction(det_G)
    num_fact = sp.factor(num)
    denom_fact = sp.factor(denom)

    return {
        "compute_time_s": t_det,
        "det_full": str(det_G),
        "numerator_factored": str(num_fact),
        "denominator_factored": str(denom_fact),
        "numerator_degree_in_u": sp.Poly(sp.expand(num), u).degree(),
    }


def row_cleared_decomposition(G: sp.Matrix, u: sp.Symbol) -> dict:
    """Row-lcm structural route for a future Lean det proof.

    The brute-force Lean route — expand `(gramMatrix u).det` over the
    *rational* entries via `Matrix.det_succ_row_zero` + `field_simp; ring`
    — is infeasible: the cofactor expansion of a dense 6×6 exhausts the
    `simp` heartbeat/step budget *before* `ring` is even reached (measured
    2026-06-20: a moderate dense 6×6 polynomial det runs past 16M
    heartbeats; the real degree-16-entry matrix past 50M / 20M steps).
    Mathlib has no `det_fin_six`.

    The viable route is *structural*: scale each row `i` by the lcm `L_i`
    of that row's denominators so the matrix becomes polynomial-entried,
    then the determinant identity is a polynomial `ring` goal (no
    division). This function emits the exact data that route needs:

      - `L` — the six row multipliers (lcm of each row's denominators),
      - `entries` — the 36 cleared polynomial entries `M[i,j] = L_i·G[i,j]`,
      - the verified identity `det(M) = -num · u^8`, where `num` is the
        degree-44 factored numerator and `det(G) = -num/(u^10 (u²+1)^12)`.

    Since `det(diag(L)·G) = (∏ L_i)·det(G)` and `∏ L_i = u^18 (u²+1)^12`,
    we get `det(M) = -num · u^18 (u²+1)^12 / (u^10 (u²+1)^12) = -num · u^8`.
    A future Lean proof discharges `gramMatrix_det_eq_factorization` by
    (1) `Matrix.det` of `diag(L)·G` = `(∏L)·det G` and (2) this polynomial
    identity — only step (2)'s 6×6 polynomial det remains open, and it is
    far lighter than the rational expansion.
    """
    L = [
        (u**2 + 1) ** 2,
        u**2 * (u**2 + 1) ** 2,
        u**2 * (u**2 + 1) ** 2,
        u**4 * (u**2 + 1) ** 2,
        u**4 * (u**2 + 1) ** 2,
        u**6 * (u**2 + 1) ** 2,
    ]
    M = sp.zeros(6, 6)
    for i in range(6):
        for j in range(6):
            M[i, j] = sp.expand(sp.cancel(L[i] * G[i, j]))
    all_poly = all(
        sp.cancel(M[i, j]).is_polynomial(u) for i in range(6) for j in range(6)
    )
    det_M = sp.Poly(M.det(method="berkowitz"), u)
    num = sp.expand(
        -(
            (u - 1) * (u + 1) * (u**3 + u - 1) ** 5 * (u**3 + u**2 + 1) ** 5
            * (u**6 - u**5 + u**4 - u**3 + 2 * u**2 - u + 1)
            * (u**6 + u**5 + 2 * u**4 + u**3 + u**2 + u + 1)
        )
    )
    target = sp.Poly(sp.expand(num * u**8), u)
    matches = (det_M - target).is_zero
    return {
        "row_multipliers_L": [str(sp.factor(x)) for x in L],
        "prod_L": str(sp.factor(sp.prod(L))),  # u^18 (u²+1)^12
        "cleared_entries": [
            [str(M[i, j]) for j in range(6)] for i in range(6)
        ],
        "all_entries_polynomial": bool(all_poly),
        "det_M_degree_in_u": det_M.degree(),
        "det_M_num_terms": len(det_M.terms()),
        "max_entry_degree_in_u": max(
            sp.Poly(M[i, j], u).degree() for i in range(6) for j in range(6)
        ),
        "det_M_equals_minus_num_times_u8": bool(matches),
    }


def positive_real_roots_of_numerator(
    u: sp.Symbol,
) -> list[tuple[str, float]]:
    """Compute all positive real roots of the numerator factor by factor.

    Returns a list of (factor_name, root_value) tuples, sorted by root
    value in increasing order.
    """
    factors_to_check = [
        ("u - 1", u - 1),
        ("u + 1", u + 1),
        ("u^3 + u - 1", u**3 + u - 1),
        ("u^3 + u^2 + 1", u**3 + u**2 + 1),
        ("u^6 - u^5 + u^4 - u^3 + 2u^2 - u + 1",
         u**6 - u**5 + u**4 - u**3 + 2 * u**2 - u + 1),
        ("u^6 + u^5 + 2u^4 + u^3 + u^2 + u + 1",
         u**6 + u**5 + 2 * u**4 + u**3 + u**2 + u + 1),
    ]
    all_pos_roots: list[tuple[str, float]] = []
    for name, poly in factors_to_check:
        roots = sp.nroots(poly, n=20)
        for r in roots:
            if abs(sp.im(r)) < sp.Rational(1, 10**12) and sp.re(r) > 0:
                all_pos_roots.append((name, float(sp.re(r))))
    all_pos_roots.sort(key=lambda x: x[1])
    return all_pos_roots


def sign_table(G: sp.Matrix, u: sp.Symbol) -> list[dict]:
    """det(G) sign at sample u values, including near the two roots."""
    samples = [0.5, 0.6, 0.68232780, 0.7, 0.8, 0.9, 1.0,
               1.05, 1.054, 1.110, 1.2, 1.5, 2.0, 3.0]
    out = []
    for u_val in samples:
        d = float(G.subs(u, u_val).det())
        out.append({"u": float(u_val), "det": d, "sign": "0" if abs(d) < 1e-9
                    else ("+" if d > 0 else "-")})
    return out


def positivity_certificate_for_u_gt_one(u: sp.Symbol) -> dict:
    """Show each numerator factor is provably > 0 for u > 1.

    For u > 1:
      - (u - 1) > 0       (immediate)
      - (u + 1) > 0       (sum of two positives)
      - (u³ + u - 1) > 0  (u³ > 1, u > 1, so u³ + u - 1 > 1)
      - (u³ + u² + 1) > 0 (all positive monomials)
      - p(u) > 0 unconditionally on ℝ (no real roots; min ≈ 0.86)
      - r(u) > 0 for u > 0 (all positive coefficients)
    Denominator u^10·(u²+1)^12 > 0 for u > 0.

    Therefore det(G(u)) < 0 for all u > 1 (the leading negative sign
    comes from the explicit minus in the factorization).
    """
    return {
        "u_minus_1": "> 0 by hypothesis u > 1",
        "u_plus_1":  "> 2 by u > 1",
        "u3_u_minus_1": "> 1 by u > 1 (u^3 > 1, u > 1 ⟹ u^3 + u - 1 > 1)",
        "u3_u2_1": "> 3 by u > 1 (all positive monomials)",
        "p_u": "> 0.86 on all of ℝ (no real roots; numerical lower bound)",
        "r_u": "> 0 by all-positive-coefficient sum for u > 0",
        "denominator": "u^10 (u² + 1)^12 > 0 by u > 0",
        "conclusion": "det(G(u)) = -(positive) / (positive) ≠ 0 for u > 1",
    }


def main() -> int:
    # Construct WitnessBuilder FIRST so its captured start_time spans
    # the expensive symbolic-determinant work (per Copilot PR #1266
    # review: `durationMs` should reflect real runtime, not just save).
    w = WitnessBuilder(
        "gram-h3-det-factorization",
        engine="python+sympy",
    )

    print("=" * 78)
    print("H_3(q) Gram determinant — symbolic factorization witness")
    print("=" * 78)

    G, u = build_gram_h3_symbolic()
    print(f"Built symbolic Gram matrix on H_3(q) NF basis (6x6)")

    print("\nComputing det via Berkowitz on polynomial-cleared matrix...")
    f = factorize_det(G, u)
    print(f"  det compute: {f['compute_time_s']:.2f}s")
    print(f"  numerator degree in u: {f['numerator_degree_in_u']}")
    print(f"\nNumerator factored:")
    print(f"  {f['numerator_factored']}")
    print(f"\nDenominator factored:")
    print(f"  {f['denominator_factored']}")

    print("\nPositive real roots of numerator (factor by factor):")
    pos_roots = positive_real_roots_of_numerator(u)
    for name, r in pos_roots:
        print(f"  {name:<50}  root at u = {r:.10f}")

    print("\nNumerical sign table:")
    sign = sign_table(G, u)
    for r in sign:
        marker = ""
        if r["u"] == 0.68232780:
            marker = "  ← root of u³+u-1"
        if r["u"] == 1.0:
            marker = "  ← root u=1"
        if abs(r["u"] - 1.054) < 1e-3:
            marker = "  ← q_0 substrate (q_0=1.110)"
        print(f"  u={r['u']:<10}  det = {r['det']:+.6e}  ({r['sign']}){marker}")

    print("\nPositivity certificate for u > 1:")
    cert = positivity_certificate_for_u_gt_one(u)
    for k, v in cert.items():
        print(f"  {k:<20}: {v}")

    print("\nRow-cleared structural route (for a future Lean det proof):")
    rc = row_cleared_decomposition(G, u)
    print(f"  all cleared entries polynomial: {rc['all_entries_polynomial']}")
    print(f"  det(M) degree {rc['det_M_degree_in_u']}, "
          f"{rc['det_M_num_terms']} terms, max entry deg "
          f"{rc['max_entry_degree_in_u']}")
    print(f"  det(M) == -num·u^8 : {rc['det_M_equals_minus_num_times_u8']}")

    # Witness (builder already constructed at start of main)
    w.set_audit_only(
        "docs/audits/2026-05-25-gram-h3-det-second-root-correctness-finding.md",
    )
    w.set_description(
        "Symbolic factorization of det(gramMatrix u) for the H_3(q) "
        "Hoefsmit-seminormal Gram matrix. Identifies TWO positive real "
        "roots — u=1 (classical limit) and u≈0.6823 (root of u³+u-1=0) "
        "— forcing a correctness fix to the Lean theorem "
        "gramMatrix_det_ne_zero (hypothesis must be u > 1, not "
        "0 < u ∧ u ≠ 1)."
    )
    w.add_data("factorization", f)
    w.add_data("positive_real_roots", [{"factor": n, "root": r}
                                       for n, r in pos_roots])
    w.add_data("numerical_sign_table", sign)
    w.add_data("positivity_certificate_for_u_gt_one", cert)
    w.add_data("row_cleared_structural_route", rc)
    w.add_assertion(
        name="row_cleared_det_equals_minus_num_times_u8",
        computed=rc["det_M_equals_minus_num_times_u8"],
        expected=True,
        tolerance=0,
        source="Berkowitz det of row-lcm-cleared polynomial matrix; the "
               "reduced (polynomial-entry) gap for a future Lean discharge "
               "of gramMatrix_det_eq_factorization",
    )
    w.add_assertion(
        name="numerator_has_exactly_two_positive_real_roots",
        computed=len(pos_roots),
        expected=2,
        tolerance=0,
        source="Sympy nroots on factor list; correctness fix evidence",
    )
    w.add_assertion(
        name="root_at_u_eq_one_present",
        computed=any(abs(r - 1.0) < 1e-9 for _, r in pos_roots),
        expected=True,
        tolerance=0,
        source="Classical-limit root; was correctly identified in original proof strategy",
    )
    w.add_assertion(
        name="second_root_at_u_approx_0_6823_present",
        computed=any(abs(r - 0.6823278038) < 1e-6 for _, r in pos_roots),
        expected=True,
        tolerance=0,
        source="Newly-found second root; correctness finding for Lean theorem statement",
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
