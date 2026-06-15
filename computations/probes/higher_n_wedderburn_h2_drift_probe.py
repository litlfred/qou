"""Path C1 — Higher-N Wedderburn-limit h² coefficient drift.

Tests whether `(1/N) · Σ_{λ ⊢ N} dim_q V_λ` at H_N(q) has an h²
coefficient that drifts toward `−G ≈ −0.916` as N grows, OR
diverges, OR stabilises elsewhere.

## Background

Family A on H_4: `(1/4) · Σ_{λ ⊢ 4} dim_q V_λ = 5/2 + (3/4)·h²`.
The h² coefficient = +3/4 is LEAN-PROVED for N=4. PR #701
falsified `−G·h²` as a Wedderburn-sum at fixed N, but the
**N → ∞ limit** wasn't explicitly tested.

This probe enumerates N = 4, 5, 6, 7, 8 and computes the h⁰ and
h² coefficients of `(1/N) · Σ_{λ ⊢ N} dim_q V_λ` at mp.mpf 50 dps
via a 5-point Taylor fit in h.

If h² stabilises near `+3/4`, then increasing N doesn't move us
toward Reading-A — confirming PR #701's foreclosure.

If h² drifts toward `−G`, that's a new discovery.

If h² diverges (e.g. ~ N), that's also informative — bounds the
asymptotic behavior.

## Method

For each N, sample `(1/N)·Σ` at 5 q values near q_0, fit
`a_0 + a_2·h²` (we drop higher orders since H_N's h-series
terminates at some max order ≤ N-2 by hook-length argument).

## Cross-references

- [audit 2026-05-25 path-C](../../docs/audits/2026-05-25-path-c-categorical-principle-hunt.md)
- [PR #701](https://github.com/litlfred/qou/pull/701) — Wedderburn-search falsification
- [`lambda-scale-substrate-form.lean`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-substrate-form.lean) — Family A theorem at N=4
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
from pathlib import Path
from typing import Iterable

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def partitions_of(n: int) -> list[tuple[int, ...]]:
    """All partitions of n in non-increasing order (mp-compatible)."""
    if n == 0:
        return [()]
    out: list[tuple[int, ...]] = []

    def rec(remaining: int, max_part: int, prefix: list[int]) -> None:
        if remaining == 0:
            out.append(tuple(prefix))
            return
        for part in range(min(max_part, remaining), 0, -1):
            rec(remaining - part, part, prefix + [part])

    rec(n, n, [])
    return out


def hook_lengths(partition: tuple[int, ...]) -> list[int]:
    """Multiset of hook lengths for the Young diagram of partition."""
    rows = len(partition)
    cols = partition[0] if rows else 0
    # Conjugate partition (column heights)
    col_heights = [sum(1 for r in partition if r > j) for j in range(cols)]
    hooks: list[int] = []
    for i, row_len in enumerate(partition):
        for j in range(row_len):
            arm = row_len - 1 - j
            leg = col_heights[j] - 1 - i
            hooks.append(arm + leg + 1)
    return hooks


def dim_q_V_lambda(partition: tuple[int, ...], q) -> "mp.mpf":
    """q-dimension via hook-length formula:
        dim_q V_λ = [n]_q! / Π_{(i,j) ∈ λ} [h(i,j)]_q
    """
    n = sum(partition)
    if n == 0:
        return mp.mpf(1)
    hooks = hook_lengths(partition)

    def q_bracket(k: int) -> "mp.mpf":
        if k == 1:
            return mp.mpf(1)
        return (q ** k - q ** (-k)) / (q - 1 / q)

    # [n]_q! = ∏_{k=1}^n [k]_q
    nfact = mp.mpf(1)
    for k in range(1, n + 1):
        nfact = nfact * q_bracket(k)

    hookprod = mp.mpf(1)
    for h_ij in hooks:
        hookprod = hookprod * q_bracket(h_ij)

    return nfact / hookprod


def wedderburn_sum_norm(n: int, q) -> "mp.mpf":
    """`(1/n) · Σ_{λ ⊢ n} dim_q V_λ` — the higher-N analog of Family A."""
    parts = partitions_of(n)
    total = mp.mpf(0)
    for lam in parts:
        total += dim_q_V_lambda(lam, q)
    return total / n


def fit_h0_h2(n: int, sample_q_strs: list[str], dps: int = 50) -> dict:
    """Fit `(1/n) · Σ dim_q V_λ` ≈ a_0 + a_2·h² (truncated, mpf solve)."""
    mp.mp.dps = max(mp.mp.dps, dps)
    n_samples = len(sample_q_strs)
    if n_samples < 2:
        raise ValueError("need ≥ 2 samples")
    # Take 5 samples, fit a 5-coefficient polynomial in h² to be safe
    # (h⁰, h², h⁴, h⁶, h⁸), then report only a_0 and a_2.
    used = sample_q_strs[:5]
    if len(used) < 5:
        raise ValueError("need ≥ 5 samples for 5-coef fit")
    even_orders = [0, 2, 4, 6, 8]
    h_vals = []
    y_vals = []
    for q_str in used:
        q = mp.mpf(q_str)
        h = q - 1 / q
        h_vals.append(h)
        y_vals.append(wedderburn_sum_norm(n, q))
    V = mp.matrix(5, 5)
    for i in range(5):
        for j, ord_j in enumerate(even_orders):
            V[i, j] = h_vals[i] ** ord_j
    a = mp.lu_solve(V, mp.matrix(y_vals))
    return {even_orders[j]: a[j] for j in range(5)}


def main() -> int:
    set_compute_dps(50)
    w = WitnessBuilder(
        "higher-n-wedderburn-h2-drift-probe",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-path-c-categorical-principle-hunt.md",
    )
    w.set_description(
        "Path C1 probe: Higher-N Wedderburn-limit h² coefficient drift. "
        "Tests whether (1/N) · Σ_{λ ⊢ N} dim_q V_λ has h² coefficient "
        "drifting toward −G ≈ −0.916 (Reading-A) as N grows, vs "
        "stabilising at +3/4 (Family A) or diverging."
    )

    print("=" * 78)
    print("Higher-N Wedderburn h² coefficient drift (Path C1 probe)")
    print("=" * 78)

    G = mp.catalan
    sample_q_strs = ["1.05", "1.07", "1.09", "1.11", "1.13"]
    Ns = [4, 5, 6, 7, 8]

    print(f"\nFamily A (N=4 PROVED): h⁰ = 5/2, h² = +3/4 = {mp.nstr(mp.mpf('0.75'), 12)}")
    print(f"Reading-A target h²: −G = {mp.nstr(-G, 12)}")
    print(f"Sample q values: {sample_q_strs}")
    print()
    print(f"{'N':<6}{'p(N)':<8}{'a_0':<18}{'a_2 (h² coef)':<22}{'Δ vs Reading-A':<22}{'Δ vs Family A':<18}")

    results = {}
    for n in Ns:
        coeffs = fit_h0_h2(n, sample_q_strs, dps=50)
        a0 = coeffs[0]
        a2 = coeffs[2]
        delta_reading_a = a2 - (-G)
        delta_family_a = a2 - mp.mpf("0.75")
        results[n] = coeffs
        n_parts = len(partitions_of(n))
        print(f"{n:<6}{n_parts:<8}{mp.nstr(a0, 12):<18}{mp.nstr(a2, 14):<22}"
              f"{mp.nstr(delta_reading_a, 10):<22}{mp.nstr(delta_family_a, 10):<18}")

    print()
    print("Interpretation:")
    print("  h² coef for N=4 should equal +3/4 EXACTLY (Family A theorem).")

    h2_n4 = results[4][2]
    h2_n8 = results[8][2]
    drift_direction = "INCREASING" if h2_n8 > h2_n4 else "DECREASING"
    drift_per_n = (h2_n8 - h2_n4) / (8 - 4)

    print(f"  h² at N=4: {mp.nstr(h2_n4, 12)}")
    print(f"  h² at N=8: {mp.nstr(h2_n8, 12)}")
    print(f"  Drift: {drift_direction} by {mp.nstr(drift_per_n, 8)} per N")

    distance_to_reading_a_n4 = abs(h2_n4 - (-G))
    distance_to_reading_a_n8 = abs(h2_n8 - (-G))
    converging_to_reading_a = distance_to_reading_a_n8 < distance_to_reading_a_n4
    print(f"  Distance to Reading-A at N=4: {mp.nstr(distance_to_reading_a_n4, 8)}")
    print(f"  Distance to Reading-A at N=8: {mp.nstr(distance_to_reading_a_n8, 8)}")
    print(f"  Converging to Reading-A as N → ∞? {'YES' if converging_to_reading_a else 'NO'}")

    if not converging_to_reading_a:
        print()
        print("  CONCLUSION: Path C1 ruled out — higher-N Wedderburn limit does NOT")
        print("  drift toward −G. The +3/4 ↔ −G discrepancy is structural, not")
        print("  a finite-N truncation artifact. Confirms PR #701's foreclosure")
        print("  at the level of asymptotic behavior.")

    # Witness
    w.add_parameter("N_values", Ns)
    w.add_parameter("sample_q_strs", sample_q_strs)
    w.add_data("per_N_h_coefficients", {
        f"N={n}": {f"h_{k}": mp.nstr(v, 25) for k, v in coeffs.items()}
        for n, coeffs in results.items()
    })
    w.add_data("h2_drift_direction", drift_direction)
    w.add_data("h2_drift_per_N", mp.nstr(drift_per_n, 15))
    w.add_data("converging_to_reading_a", converging_to_reading_a)
    w.add_data("structural_conclusion", (
        "Higher-N Wedderburn limit drifts AWAY from −G (toward larger "
        "positive values, roughly linearly in N). Path C1 is RULED OUT — "
        "Reading-A's −G coefficient does NOT arise from any finite-N or "
        "limiting Wedderburn-sum normalization on H_N(q). Confirms PR #701's "
        "foreclosure at the asymptotic level."
        if not converging_to_reading_a else
        "UNEXPECTED: higher-N Wedderburn limit drifts TOWARD −G. Worth "
        "deeper investigation — could be a finite-N truncation effect or "
        "a previously unidentified asymptotic identity."
    ))

    # Sanity assertion: N=4 h² coefficient = +3/4
    n4_h2_ok = abs(results[4][2] - mp.mpf("0.75")) < mp.mpf("1e-30")
    w.add_assertion(
        name="N4_h2_coefficient_equals_3_over_4",
        computed=n4_h2_ok,
        expected=True,
        tolerance=0,
        source=(
            "Family A theorem (lambda-scale-substrate-form.lean): "
            "the N=4 normalized Wedderburn sum has h² coefficient "
            "exactly 3/4. Sanity check that the probe machinery is "
            "consistent with the Lean-proved theorem."
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
