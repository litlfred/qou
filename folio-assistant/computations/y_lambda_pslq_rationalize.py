#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""PSLQ rationalisation of y_λ values from MPFR witness.

For each y_λ at 50 dps, run mpmath.pslq against the basis
{1, q, q², ..., q^N, 1/q, 1/q², ..., 1/q^N, q^{1/2}, q^{3/2}, ...}
to recover the q-rational form.

Strategy: fix a denominator structure based on cyclotomic Schur-element
patterns ((q+1), (q²+1), (q²-q+1), etc.), multiply y_λ_witness by
the candidate denominator, then PSLQ-rationalise the numerator
against integer-coefficient q-power basis.

If successful, gives closed-form y_λ in Q(q^{1/2}) at n=5..9 without
needing sympy's expensive linear-system solve.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 50  # match witness precision


def load_mpfr_witness():
    with open(Path(__file__).parent / "y-lambda-mpfr-witness.json") as f:
        W = json.load(f)
    return W


def cyclotomic_basis(q):
    """Common denominator factors in Schur-element / Jones-Markov rationals:
    (q+1), (q²+1), (q²-q+1), (q²+q+1), (q^4+1), (q^4-q²+1), etc."""
    factors = {
        "q+1": q + 1,
        "q-1": q - 1,
        "q^2+1": q**2 + 1,
        "q^2-q+1": q**2 - q + 1,
        "q^2+q+1": q**2 + q + 1,
        "q^4+1": q**4 + 1,
        "q^4-q^2+1": q**4 - q**2 + 1,
        "q^4+q^3+q^2+q+1": q**4 + q**3 + q**2 + q + 1,
        "q^6+1": q**6 + 1,
        "q^6-q^3+1": q**6 - q**3 + 1,
    }
    return factors


def try_pslq_rationalize(y_val, q, max_q_power=20):
    """Try to express y_val as a polynomial in q^{1/2} divided by a
    cyclotomic product. Returns (numerator coefficients, denominator
    label) or None if no clean relation found.

    Basis: {1, q^{1/2}, q, q^{3/2}, ..., q^{max_q_power/2}}.
    """
    qhalf = mp.sqrt(q)
    # Build a half-power basis
    basis_q = [qhalf**k for k in range(0, 2 * max_q_power + 1)]
    # Also negative powers
    basis_qi = [qhalf**(-k) for k in range(1, max_q_power + 1)]
    full_basis = [y_val] + basis_q + basis_qi
    # PSLQ
    try:
        rel = mp.pslq(full_basis, tol=mp.mpf(10)**(-30), maxcoeff=10**12)
        if rel is None:
            return None, None
        # Coefficient of y_val must be ±1
        if abs(rel[0]) != 1:
            return None, None
        # Normalize so coefficient of y_val is +1
        sign = 1 if rel[0] > 0 else -1
        coeffs = [-c * sign for c in rel[1:]]
        return coeffs, "polynomial"
    except Exception:
        return None, None


def try_with_denominator(y_val, q, denom_val, denom_label, max_q_power=20):
    """Try y_val · denom = polynomial in q^{1/2}."""
    target = y_val * denom_val
    coeffs, _ = try_pslq_rationalize(target, q, max_q_power)
    if coeffs is None:
        return None
    return (coeffs, denom_label)


def main():
    W = load_mpfr_witness()
    q_str = W.get("dps")  # not actually q; the dps note. Get q from a table
    # Get q from one of the tables
    sample = next(iter(W["tables_by_n"].values()))
    q = mp.mpf(sample["q"])
    print(f"q = {q}")
    print(f"PSLQ tolerance: 10^-30, max coeff: 10^12, dps: {mp.mp.dps}")

    factors = cyclotomic_basis(q)

    print(f"\n{'n':>3} {'λ':>14} {'y':>16} {'best fit':>50}")
    print("-" * 90)

    for n_str in sorted(W["tables_by_n"].keys(), key=int):
        if int(n_str) < 3:
            continue
        t = W["tables_by_n"][n_str]
        for ww in t.get("weights", []):
            p = tuple(ww["partition"])
            y_str = ww.get("y_lambda_mpfr_dps50") or ww.get("y_lambda")
            if not y_str:
                continue
            y = mp.mpf(y_str)

            # Try direct rationalisation, then with various cyclotomic denominators
            best = None
            best_denom = None
            best_label = "(no fit)"

            # First try plain (no denom)
            coeffs, _ = try_pslq_rationalize(y, q, max_q_power=12)
            if coeffs is not None:
                best = coeffs
                best_label = "1"

            if best is None:
                # Try single cyclotomic denominators
                for label, val in factors.items():
                    out = try_with_denominator(y, q, val, label, max_q_power=12)
                    if out is not None:
                        best = out[0]
                        best_label = label
                        break

            if best is None:
                # Try products of two cyclotomic factors
                items = list(factors.items())
                for i, (l1, v1) in enumerate(items):
                    for j, (l2, v2) in enumerate(items[i:]):
                        prod = v1 * v2
                        out = try_with_denominator(y, q, prod, f"{l1}·{l2}",
                                                     max_q_power=14)
                        if out is not None:
                            best = out[0]
                            best_label = f"{l1}·{l2}"
                            break
                    if best is not None:
                        break

            if best is None:
                print(f"{n_str:>3} {str(p):>14} {float(y):>+16.6f}  (no PSLQ fit)")
            else:
                # Truncate display
                nz_terms = [(k, c) for k, c in enumerate(best) if c != 0]
                if not nz_terms:
                    expr = "0"
                else:
                    parts = []
                    for k, c in nz_terms[:5]:  # show first few
                        if k == 0:
                            parts.append(f"{c}")
                        elif k <= len(best) // 2:
                            parts.append(f"{c}q^({k}/2)")
                        else:
                            parts.append(f"{c}q^(-{k-len(best)//2}/2)")
                    expr = " + ".join(parts)
                if len(nz_terms) > 5:
                    expr += f" + ... ({len(nz_terms)} terms)"
                print(f"{n_str:>3} {str(p):>14} {float(y):>+16.6f}  /({best_label}) = {expr[:60]}")


if __name__ == "__main__":
    main()
