#!/usr/bin/env python3
"""R&D 3: Drop the H_4 anchor — test other Hecke levels.

If H_4 is wrong, the proton's natural categorical level may be
H_3, H_5, H_6, or higher. For each H_n, compute:
  π_alg(H_n) = (1/4) · Σ_{λ ⊢ n} dim_q V_λ  (or different normalization)

and check (a) what its leading term is at q=1, and (b) what its
h² coefficient is. We want both:
  - leading = 5/2 (matches the half-symmetric partition count
    interpretation OR matches the CODATA target after scaling)
  - h² coefficient ≈ -G (matches the empirical 5.4 ppm match)

The "(1/4)" normalization at H_4 was chosen to give 5/2 leading.
For other H_n, the natural normalization may differ.
"""
from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json, sys
from pathlib import Path
import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from q_parameter import Q_50_DIGIT_STR, Q_MP

mp.mp.dps = 80
Q_NUM = Q_MP
H_NUM = Q_NUM - 1/Q_NUM
G_NUM = mp.catalan


def partitions(n):
    """List all partitions of n."""
    if n == 0:
        return [()]
    out = []
    def rec(rem, max_part, prefix):
        if rem == 0:
            out.append(prefix)
            return
        for k in range(min(rem, max_part), 0, -1):
            rec(rem - k, k, prefix + (k,))
    rec(n, n, ())
    return out


def dim_q_hook_content(shape, q_sym):
    """q-deformed dimension via hook-content formula:
    dim_q V_λ = [n]_q! / ∏_x [h_x(λ)]_q
    where h_x is the hook length at cell x in λ.
    """
    n = sum(shape)
    # n! in q
    def qint(k):
        return (q_sym**k - q_sym**(-k)) / (q_sym - 1/q_sym)
    num = sp.Integer(1)
    for k in range(1, n+1):
        num *= qint(k)
    # Hook lengths in λ
    den = sp.Integer(1)
    for i, row in enumerate(shape):
        for j in range(row):
            # hook at (i, j): arm + leg + 1
            arm = row - j - 1
            leg = sum(1 for r_below_idx, r_below in enumerate(shape) if r_below_idx > i and r_below > j)
            h = arm + leg + 1
            den *= qint(h)
    return sp.simplify(num / den)


def main() -> int:
    w = WitnessBuilder("lambda-scale-rd3-hecke-levels", engine="sympy")
    w.set_description(
        "R&D 3: test natural categorical sum at H_3, H_5, H_6, H_7. "
        "For each H_n compute (1/?) · Σ_λ dim_q V_λ and extract its "
        "leading + h² coefficients. Find a level (and normalization) "
        "matching `5/2 − h²·G` empirically."
    )
    w.set_content_block("conj:lambda-scale-substrate-form")

    q = sp.Symbol("q", positive=True)
    eps = sp.Symbol("eps", real=True)
    h_sym = sp.Symbol("h_sym")

    results = []
    for n in [2, 3, 4, 5, 6, 7]:
        parts = partitions(n)
        sum_dim_q = sp.Integer(0)
        for shape in parts:
            d = dim_q_hook_content(shape, q)
            sum_dim_q += d
        sum_dim_q = sp.simplify(sum_dim_q)

        # Evaluate at q=1
        at_1 = sp.limit(sum_dim_q, q, 1)
        # h-expansion
        as_eps = sum_dim_q.subs(q, 1 + eps)
        try:
            as_series = sp.series(as_eps, eps, 0, 5).removeO()
            eps2_coeff = as_series.coeff(eps, 2)
            # h ≈ 2ε at leading, so h² ≈ 4ε² → ε² coeff / 4 = h² coeff
            h2_coeff = eps2_coeff / 4
        except Exception:
            h2_coeff = None

        print(f"H_{n}:  p({n}) = {len(parts)}, Σ dim_q V_λ at q=1 = {at_1}, h² coeff = {h2_coeff}")
        if h2_coeff is not None and at_1 != 0:
            # What normalization gives leading 5/2?
            norm_for_5_2 = at_1 / (sp.Rational(5, 2))
            h2_normalized = h2_coeff / norm_for_5_2
            print(f"      / ({norm_for_5_2}) = 5/2 + ({h2_normalized})·h² (target: -G ≈ -0.916)")
            try:
                h2_num = float(h2_normalized.subs(q, float(Q_NUM)))
            except Exception:
                h2_num = float(h2_normalized)
            results.append({"n": n, "at_q1": str(at_1),
                            "h2_coeff_normalized": float(h2_num),
                            "matches_neg_G": abs(h2_num - (-float(G_NUM))) < 0.01})

    w.add_data("results_by_n", results)
    print()
    print("LOOKING FOR: a level n where h2_coeff_normalized ≈ -0.916 = -G")
    matches = [r for r in results if r["matches_neg_G"]]
    if matches:
        for r in matches:
            print(f"  H_{r['n']}: MATCH (h² = {r['h2_coeff_normalized']})")
    else:
        print("  No level gives h² ≈ -G with the simple Σ dim_q normalization.")

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
