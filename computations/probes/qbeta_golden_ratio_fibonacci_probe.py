"""qbeta_golden_ratio_fibonacci_probe.py — Golden-ratio analog of the
silver-ratio Pell-Lucas c_k benchmark.

The c_5 outlier at silver ratio (q = 1+√2) involves the inert prime
11 ∈ ℤ[1+√2]. The "is c_5 the unique outlier?" hypothesis from
prop:averaging-resonance-rule sharpens to a stronger claim if the
outlier disappears under a DIFFERENT quadratic specialisation:

  Hypothesis (falsifiability check): the c_5 outlier is SILVER-SPECIFIC,
  tied to silver being the β-decay null point (h=2 root of
  Δ(net) = h(h-2)/2). At golden ratio (q = φ, h = 1), there is no
  such null, so all c_k should be Fibonacci/Lucas-CLEAN with no
  inert-prime outlier.

This probe computes c_k(q) for k = 3..10 at golden q = φ, tests the
Fibonacci-or-Lucas-or-power-of-2 closure on the reduced numerator,
and compares with the silver-ratio outcome.

Predicted outcome:
  Silver q = 1+√2:  c_5 = -11/8, 11 INERT in ℤ[1+√2] → OUTLIER
  Golden q = φ:     c_5 = -13/10, 13 = F_7 Fibonacci → CLEAN

If observed, this provides a clean structural answer to "why is c_5
problematic specifically?" — it's the inert-prime fingerprint of
silver being the unique β-decay null.

Status: experimental (probe).
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from silver_ratio_utils import is_pell_lucas_clean  # noqa: E402


def fibonacci_up_to(bound: int) -> list[int]:
    """Fibonacci numbers F_n: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    up to and including the first value ≥ bound."""
    if bound <= 0:
        return [0]
    a, b = 0, 1
    out = [a]
    while a < bound:
        a, b = b, a + b
        out.append(a)
    return out


def lucas_up_to(bound: int) -> list[int]:
    """Generate the Lucas-number candidate set L_0, L_1, L_2, ... =
    2, 1, 3, 4, 7, 11, 18, 29, 47, 76, ...

    Returns every Lucas number L_n for n = 0, 1, 2, ... up to the first
    index where L_n >= bound (that final term is included).  Because
    L_1 = 1 < L_0 = 2, the returned list is NOT monotonically increasing
    at the head — it is a candidate set (which is exactly how
    is_fibonacci_lucas_clean consumes it), not a sorted prefix.
    """
    if bound <= 0:
        return []
    a, b = 2, 1
    out = [a, b]
    while max(a, b) < bound:
        a, b = b, a + b
        out.append(b)
    return out


def is_fibonacci_lucas_clean(value: Fraction) -> tuple[bool, str]:
    """Test if a rational value is Fibonacci-or-Lucas-clean at golden ratio.

    The reduced numerator (in absolute value) is considered clean iff
    it has the form f^j · 2^t for some Fibonacci F_n or Lucas L_n
    number f > 1, j ∈ {0, 1, ..., 4}, t ≥ 0. The j = 0 case collapses
    to a bare power of 2.

    Returns (is_clean, structural_description).
    """
    num = abs(value.numerator)
    if num == 0:
        return True, "zero"
    if (num & (num - 1)) == 0:
        return True, f"2^{num.bit_length() - 1}"

    # Build Fibonacci + Lucas combined candidate set
    fib = fibonacci_up_to(num)
    luc = lucas_up_to(num)
    candidates = sorted(set(fib + luc))

    for f in candidates:
        if f <= 1:
            continue
        p = 1
        for j in range(1, 5):
            p *= f
            if p > num:
                break
            if num % p == 0:
                quotient = num // p
                if quotient != 0 and (quotient & (quotient - 1)) == 0:
                    name = "F" if f in fib else "L"
                    if quotient == 1:
                        return True, f"{f}^{j} ({name}_*)"
                    return True, f"{f}^{j} · 2^{quotient.bit_length() - 1}"
    return False, f"{num} inert (not f^j · 2^t for F/L number f)"


def main() -> None:
    w = WitnessBuilder(
        name="qbeta-golden-ratio-fibonacci-probe",
        engine="python",
    )
    w.set_description(
        "Falsifiability probe: tests whether the c_5 outlier at silver "
        "ratio (q = 1+√2) is silver-specific or universal. Evaluates c_k "
        "closed forms at golden ratio (q = φ) where h = q - q⁻¹ = 1, "
        "b² = 4/5 exactly, q-integers reduce to Lucas L_n (n odd) or "
        "F_n·√5 (n even). Tests Fibonacci-or-Lucas-or-power-of-2 "
        "closure on each c_k numerator. Predicted outcome: all c_k "
        "clean (no outlier) at golden, since there is no β-decay null "
        "at h=1 to force the bar-invariant sector collapse."
    )

    # Golden-ratio values (exact rationals via q² = q + 1)
    # c_3 = -2 (q-independent)
    # c_4 = c_3 · b⁴ = -2 · (4/5)² = -32/25
    # c_5 = -(b² + 1/2) = -(4/5 + 1/2) = -13/10
    # c_6 = c_3² · b² = 4 · 4/5 = 16/5
    # c_7 = c_3³ = -8 (q-independent)
    # c_8 = c_3² · b⁴ = 4 · 16/25 = 64/25
    # c_9 = c_3³ · b² = -8 · 4/5 = -32/5
    # c_10 = c_3² · b⁶ = 4 · 64/125 = 256/125
    b_sq_golden = Fraction(4, 5)
    c_k_at_golden: dict[int, Fraction] = {
        3:  Fraction(-2),
        4:  Fraction(-2) * b_sq_golden**2,
        5:  -(b_sq_golden + Fraction(1, 2)),
        6:  Fraction(4) * b_sq_golden,
        7:  Fraction(-8),
        8:  Fraction(4) * b_sq_golden**2,
        9:  Fraction(-8) * b_sq_golden,
        10: Fraction(4) * b_sq_golden**3,
    }

    # Silver-ratio comparison (from prop:averaging-resonance-rule)
    b_sq_silver = Fraction(7, 8)
    c_k_at_silver: dict[int, Fraction] = {
        3:  Fraction(-2),
        4:  Fraction(-2) * b_sq_silver**2,
        5:  -(b_sq_silver + Fraction(1, 2)),
        6:  Fraction(4) * b_sq_silver,
        7:  Fraction(-8),
        8:  Fraction(4) * b_sq_silver**2,
        9:  Fraction(-8) * b_sq_silver,
        10: Fraction(4) * b_sq_silver**3,
    }

    print("=" * 78)
    print("Golden-ratio Fibonacci/Lucas probe — vs silver-ratio Pell-Lucas")
    print("=" * 78)
    print()
    print(f"Golden: q = (1+√5)/2 = φ, h = 1, b² = 4/5 exactly")
    print(f"Silver: q = 1+√2,        h = 2, b² = 7/8 exactly (β-decay null)")
    print()
    print(f"{'k':>3} | {'silver c_k':>12} | {'silver clean?':>26} | "
          f"{'golden c_k':>12} | {'golden clean?':>26}")
    print("-" * 100)
    rows: list[dict] = []
    for k in sorted(c_k_at_silver.keys()):
        s_val = c_k_at_silver[k]
        g_val = c_k_at_golden[k]
        s_clean = is_pell_lucas_clean(s_val)
        g_clean, g_why = is_fibonacci_lucas_clean(g_val)
        s_marker = "✓ Pell-Lucas" if s_clean else "✗ INERT (11)"
        g_marker = f"✓ {g_why}" if g_clean else f"✗ INERT ({g_why})"
        rows.append({
            "k": k,
            "silver_value": str(s_val),
            "silver_pell_lucas_clean": s_clean,
            "golden_value": str(g_val),
            "golden_fibonacci_lucas_clean": g_clean,
            "golden_clean_why": g_why,
        })
        print(f"{k:>3} | {str(s_val):>12} | {s_marker:>26} | "
              f"{str(g_val):>12} | {g_marker:>26}")
    print()

    silver_outliers = [r["k"] for r in rows if not r["silver_pell_lucas_clean"]]
    golden_outliers = [r["k"] for r in rows if not r["golden_fibonacci_lucas_clean"]]

    print(f"Silver outliers (Pell-Lucas-inert): {silver_outliers}")
    print(f"Golden outliers (Fibonacci-Lucas-inert): {golden_outliers}")
    print()
    if silver_outliers == [5] and golden_outliers == []:
        print("✓ HYPOTHESIS CONFIRMED: c_5 outlier is silver-specific.")
        print("  At silver (β-decay null at h=2), c_5 = -11/8 with 11 inert.")
        print("  At golden (no null at h=1), c_5 = -13/10 with 13 = F_7 clean.")
        print("  The outlier is the inert-prime fingerprint of the")
        print("  β-decay null collapse into the bar-invariant sector.")
        hypothesis_confirmed = True
    else:
        print("✗ HYPOTHESIS NOT MATCHED — investigate further.")
        hypothesis_confirmed = False

    w.add_data("hypothesis", "c_5 outlier is silver-specific (β-decay null)")
    w.add_data("rows", rows)
    w.add_data("silver_outliers", silver_outliers)
    w.add_data("golden_outliers", golden_outliers)
    w.add_data("hypothesis_confirmed", hypothesis_confirmed)
    w.add_assertion(
        "silver_unique_outlier_at_k5",
        computed=1 if silver_outliers == [5] else 0,
        expected=1,
        source="prop:averaging-resonance-rule empirical classification",
    )
    w.add_assertion(
        "golden_no_outliers",
        computed=1 if golden_outliers == [] else 0,
        expected=1,
        source=(
            "no β-decay null at h = 1, so no forced collapse into "
            "bar-invariant sector at golden ratio"
        ),
    )
    w.save()


if __name__ == "__main__":
    main()
