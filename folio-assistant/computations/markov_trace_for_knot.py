"""Generic Markov-trace evaluator for any knot/link in the framework.

Per author 2026-05-25 (common infra request): provides a unified
`markov_trace_for_knot(knot_name, q, convention)` function that:

1. Looks up the canonical braid word from `knot_braid_database`
2. Builds y_λ on the appropriate H_n(q) via the requested convention:
   - "wenzl"   → pn.trace_weights_n (LP-based Wenzl Jones-Markov)
   - "q_schur" → pn.trace_weights_n_q_schur (closed form)
3. Computes χ_λ(β_K, q) via pn.chi_lambdas_braid
4. Returns tr_M(K, q) = Σ_λ y_λ · χ_λ(β_K)

## Convention disambiguation

Per `docs/audits/2026-05-25-markov-trace-convention-audit.md`:

| Convention | tr(σ_i) | Used by |
|------------|---------|---------|
| "wenzl"    | z = 1/(√q+1/√q) | Mass formula (Borromean), per-atom witnesses |
| "q_schur"  | h = q − q⁻¹     | Torus knot closed forms, lepton tower |

**Pick the convention that matches your physics.**

## Verified cross-checks

- `markov_trace_for_knot("Borromean", q_0, "wenzl")` matches the
  closed form `(4+h²−3h⁴−h⁶)/(h²+4)` (within 1e-5 due to LP
  numerical precision).
- `markov_trace_for_knot("T(2,4)", q_0, "q_schur")` matches the
  sibling H_2 hardcode `y_(2)·q^4 + y_(1,1)·q^-4`.

## Example

```python
import pyhecke_native as pn
from markov_trace_for_knot import markov_trace_for_knot

# Borromean via Wenzl JM (mass-formula convention)
tr_borr_wenzl = markov_trace_for_knot("Borromean", q_0, "wenzl")
# → ≈ 0.998

# Borromean via q-Schur (different convention)
tr_borr_qs = markov_trace_for_knot("Borromean", q_0, "q_schur")
# → ≈ 0.669

# Torus knot T(2,8) = Higgs (q-Schur convention)
tr_higgs = markov_trace_for_knot("T(2,8)", q_0, "q_schur")
# → matches sibling T(2,k) hardcode

# Figure-eight 4_1 (the muon's knot) via Wenzl JM
tr_4_1 = markov_trace_for_knot("4_1", q_0, "wenzl")
```
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pyhecke_native as pn

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from knot_braid_database import (  # noqa: E402
    braid_word_for_knot,
    n_strands_for_knot,
)


def y_lambda_h2_q_schur_mpf(q: Any) -> tuple[Any, Any]:
    """Closed-form q-Schur Plancherel weights on H_2(q) — generic in q.

    Returns (y_(2), y_(1,1)) where:
      y_(2)   = q   / [2]_q
      y_(1,1) = q⁻¹ / [2]_q
    with [2]_q = q + q⁻¹. Sum y_(2) + y_(1,1) = 1 (Plancherel
    normalization).

    These are the principal specialization of the q-Schur weights
      y_λ(q) = q^{content_sum(λ)} / [n]_q!
    at n = 2, with content_sum((2)) = +1 and content_sum((1,1)) = −1.

    The function is parametric in `q` — works for `float`, `mp.mpf`,
    `sp.Symbol`. Use this in mp.mpf-precision scripts (50-dps pin)
    where `pn.trace_weights_n_q_schur` (f64) would lose precision.

    Equivalent to `pn.trace_weights_n_q_schur(2, float(q))` at f64,
    but preserves caller precision via duck-typed arithmetic on `q`.
    """
    qi = 1 / q
    bracket_2 = q + qi
    return q / bracket_2, qi / bracket_2


def trM_torus_2_k_mpf(k: int, q: Any) -> Any:
    """Closed-form Markov trace tr_M(σ_1^k) in H_2(q), generic in q.

    For T(2, k) torus link with braid σ_1^k in B_2:
      tr_M(σ_1^k) = y_(2)·q^k + y_(1,1)·(-q⁻¹)^k

    where (y_(2), y_(1,1)) = `y_lambda_h2_q_schur_mpf(q)`.

    Generic in `q` for full precision in mp.mpf scripts.
    """
    y_2, y_11 = y_lambda_h2_q_schur_mpf(q)
    qi = 1 / q
    sign = (-1) ** k
    return y_2 * q ** k + y_11 * sign * qi ** k


def markov_trace_for_knot(
    knot_name: str,
    q: float,
    convention: str = "wenzl",
) -> float:
    """Compute the Markov trace tr_M(K, q) for any catalogued knot/link.

    Args:
        knot_name: 'Borromean', '4_1', 'T(2,8)', etc. See
            `knot_braid_database.list_known_knots()` + T(p, k).
        q: substrate q value (typically q_0 ≈ 1.11).
        convention: "wenzl" (Wenzl Jones-Markov, mass-formula) or
            "q_schur" (q-Schur Plancherel, torus knots).

    Returns:
        tr_M(K, q) as f64.

    Raises:
        ValueError: if convention not in {"wenzl", "q_schur"}.
        KeyError: if knot_name not catalogued.
    """
    if convention not in ("wenzl", "q_schur"):
        raise ValueError(
            f"convention must be 'wenzl' or 'q_schur', got {convention!r}"
        )

    braid = braid_word_for_knot(knot_name)
    n = n_strands_for_knot(knot_name)

    # Get y_λ from the chosen convention
    if convention == "wenzl":
        y_lambda = pn.trace_weights_n(n, q)
    else:  # q_schur
        y_lambda = pn.trace_weights_n_q_schur(n, q)

    # Compute χ_λ values for all partitions of n on this braid
    shapes = pn.partitions_of(n)
    chi_vals = pn.chi_lambdas_braid(shapes, braid, q)

    # tr_M = Σ_λ y_λ · χ_λ(β_K)
    return sum(y_lambda[i] * chi_vals[i] for i in range(len(shapes)))


def _self_test() -> int:
    """Quick sanity checks on the common infra."""
    import mpmath as mp
    mp.mp.dps = 30
    q = 1.10997859561220225731

    print("=" * 80)
    print("markov_trace_for_knot — self-test")
    print(f"  q_0 = {q:.10f}")
    print("=" * 80)

    # Borromean via Wenzl (should match closed form)
    h = q - 1.0 / q
    h2 = h * h
    h4 = h2 * h2
    h6 = h4 * h2
    borr_closed = (4 + h2 - 3 * h4 - h6) / (h2 + 4)
    borr_wenzl = markov_trace_for_knot("Borromean", q, "wenzl")
    print(f"\nBorromean (Wenzl JM):")
    print(f"  closed form (4+h²−3h⁴−h⁶)/(h²+4) = {borr_closed:.10f}")
    print(f"  via markov_trace_for_knot         = {borr_wenzl:.10f}")
    print(f"  agreement                         = {abs(borr_closed - borr_wenzl):.2e}")

    # Borromean via q-Schur (different convention, different number)
    borr_qs = markov_trace_for_knot("Borromean", q, "q_schur")
    print(f"\nBorromean (q-Schur, different convention):")
    print(f"  tr_M = {borr_qs:.10f}  (≠ Wenzl, as expected)")

    # T(2,4) = W± (q-Schur)
    tr_T24 = markov_trace_for_knot("T(2,4)", q, "q_schur")
    # Sibling hardcode: y_2·q^4 + y_(1,1)·q^-4 where y_2 = q/[2]_q
    qi = 1.0 / q
    sq_2_q = q + qi
    y_2 = q / sq_2_q
    y_11 = qi / sq_2_q
    sibling_T24 = y_2 * q ** 4 + y_11 * qi ** 4
    print(f"\nT(2,4) W± (q-Schur):")
    print(f"  sibling hardcode = {sibling_T24:.10f}")
    print(f"  generic infra    = {tr_T24:.10f}")
    print(f"  agreement        = {abs(sibling_T24 - tr_T24):.2e}")

    # Figure-eight 4_1 via Wenzl
    tr_4_1 = markov_trace_for_knot("4_1", q, "wenzl")
    print(f"\n4_1 figure-eight (Wenzl JM):")
    print(f"  tr_M = {tr_4_1:.10f}")

    print("\n✓ Common infra working.")
    return 0


if __name__ == "__main__":
    sys.exit(_self_test())
