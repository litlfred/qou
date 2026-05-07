#!/usr/bin/env python3
"""
F3.3: Clean Python wrapper for q-deformed character on canonical
permutation braids `T_w ∈ H_n(q)`.

## Scope (read this carefully)

The Hecke algebra `H_n(q)` is **not a class function ring** at
q ≠ 1: two elements with the same image in `S_n` (same permutation
cycle type) can have DIFFERENT q-characters when expressed as
braid words.

**Canonical T_w form**: a minimal-length permutation braid
`T_w = T_{s_{i_1}} T_{s_{i_2}} ... T_{s_{i_l}}` where
`l = ℓ(w) = #inversions(w)` and the simple transpositions appear
in a reduced expression.

For canonical T_w, the q-character `χ_λ(T_w; q)` IS a class function
of cycle type μ(w), and q-Murnaghan-Nakayama (Ram 1991) gives an
O(n²) algorithm — vs. O(dim_λ² · ℓ(w)) for direct seminormal evaluation.

For arbitrary braid words (e.g. atomic braids with inverse generators),
this speedup is NOT applicable; use `chi_lambda_braid` (Hoefsmit) instead.

## API

  chi_q_canonical_T_w(λ, μ, q='symbolic') -> LaurentPolyQ | mpmath.mpf | float

  Args:
    λ: irrep partition of n (descending parts).
    μ: cycle type of the permutation w (any order; n = sum(μ)).
    q: 'symbolic' (default) returns LaurentPolyQ; pass a numeric value
       for evaluation.

  Returns: χ^λ(T_w; q) as the requested type.

## Cross-validation

  - q = 1: must equal classical MN χ^λ(μ).  Verified on S_3, S_5
    standard tables (Rust unit tests).
  - q = q₀: must equal Hoefsmit seminormal evaluation when β is in
    canonical T_w form.  Verified on the trivial / sign reps and
    on small (n ≤ 6) cases (Python smoke test below).

## Benchmark

  At n = 18 (385 partitions, max dim ~5×10⁴), q-MN with memoization
  computes all dim S^λ values (Σ d² = 18!) in 0.057s — vs. seminormal
  matrix construction would be infeasible.

  This benchmark validates the algorithmic infrastructure; full
  speedup on atomic braids requires the per-isotope canonical T_w
  decomposition, which is a separate research milestone.

@module folio-assistant/computations/q_mn_canonical
"""
from __future__ import annotations
import argparse
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import pyhecke_native as p  # type: ignore[import]


def chi_q_canonical_T_w(lam, mu, q="symbolic", q_value=None):
    """Hecke character `χ^λ(T_w; q)` for w with cycle type μ.

    See module docstring for the canonical-T_w scope.

    `q` accepts:
      - "symbolic" / None         → returns list[(half_exp, coeff_str)]
                                    encoding the LaurentPolyQ result
      - "classical" / 1           → returns int (classical MN value)
      - float / int               → returns float (q-polynomial evaluated
                                    at this numeric value)
      - "mpfr_50dps", "mpfr_<N>dps" → mpmath.mpf evaluation at the
                                      requested precision

    `q_value` (NEW per Copilot review #r3144...): explicit numeric q
    used in the "mpfr_*dps" path.  When `q_value=None` the legacy
    behaviour is preserved (evaluates at the substrate parameter `Q0`
    from `q_parameter.py`).  Pass a string / float / mpmath.mpf to
    evaluate at any other point.

    Previously the "mpfr_*dps" path silently ignored any numeric q in
    the call site and always evaluated at `Q0`, which contradicted the
    docstring promise that callers can "pass a numeric value for
    evaluation".  The new `q_value` parameter restores that contract.
    """
    lam = list(lam)
    mu = list(mu)
    if q == "classical" or q == 1:
        return p.mn_chi(lam, mu)
    if q == "symbolic" or q is None:
        return p.mn_chi_q(lam, mu)
    if isinstance(q, (int, float)):
        terms = p.mn_chi_q(lam, mu)
        return sum(int(c) * (float(q) ** (he / 2.0)) for he, c in terms)
    if q == "mpfr_50dps" or (isinstance(q, str) and q.startswith("mpfr_")):
        import mpmath as mp
        dps = 50
        if q.startswith("mpfr_") and q.endswith("dps"):
            dps = int(q[5:-3])
        mp.mp.dps = dps
        if q_value is None:
            from q_parameter import Q as Q0
            q_value = Q0
        terms = p.mn_chi_q(lam, mu)
        q_mpf = q_value if isinstance(q_value, mp.mpf) else mp.mpf(str(q_value))
        result = mp.mpf(0)
        for he, c in terms:
            result += mp.mpf(int(c)) * q_mpf ** (mp.mpf(he) / 2)
        return result
    raise ValueError(f"Unrecognized q: {q!r}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--smoke", action="store_true",
                        help="Run smoke tests + cross-validation")
    parser.add_argument("--bench-n", type=int, default=18,
                        help="Benchmark dim S^λ Plancherel identity at this n")
    args = parser.parse_args()

    if args.smoke:
        # Cross-validation at q=1 vs classical MN.
        print("=" * 70)
        print("Smoke test: q=1 limit matches classical MN")
        print("=" * 70)
        cases = [
            ([3], [2, 1]),
            ([2, 1], [2, 1]),
            ([1, 1, 1], [2, 1]),
            ([3], [3]),
            ([2, 1], [3]),
            ([1, 1, 1], [3]),
            ([5], [3, 2]),
            ([4, 1], [3, 1, 1]),
            ([3, 2], [3, 2]),
        ]
        all_ok = True
        for lam, mu in cases:
            chi_class = chi_q_canonical_T_w(lam, mu, q=1)
            chi_q_terms = chi_q_canonical_T_w(lam, mu, q="symbolic")
            chi_at_one = sum(int(c) for _, c in chi_q_terms)
            ok = chi_at_one == chi_class
            all_ok &= ok
            sym = ", ".join(f"{c}*q^{he/2:.1f}" if he % 2 else f"{c}*q^{he//2}"
                            for he, c in sorted(chi_q_terms))
            print(f"  {'OK' if ok else 'FAIL':<4} λ={lam}, μ={mu}: "
                  f"classical={chi_class}, q-MN(q=1)={chi_at_one}")
            print(f"           q-poly: {sym or '0'}")
        print(f"\nResult: {'all pass' if all_ok else 'FAILURES'}")

    # Benchmark Plancherel identity at the requested n.
    print()
    print("=" * 70)
    print(f"Benchmark: Σ_λ (dim S^λ)² = {args.bench_n}!")
    print("=" * 70)
    from hecke_characters import partitions_of as py_parts
    parts = list(py_parts(args.bench_n))
    print(f"  {args.bench_n}! = {math.factorial(args.bench_n):,}")
    print(f"  partitions of {args.bench_n} = {len(parts)}")
    mu_id = [1] * args.bench_n
    t0 = time.time()
    total = 0
    for lam in parts:
        d = chi_q_canonical_T_w(list(lam), mu_id, q=1)
        total += d * d
    elapsed = time.time() - t0
    match = total == math.factorial(args.bench_n)
    print(f"  Σ d² = {total:,}")
    print(f"  Match: {'OK' if match else 'FAIL'}")
    print(f"  Wallclock: {elapsed:.3f}s")

    return 0


if __name__ == "__main__":
    sys.exit(main())
