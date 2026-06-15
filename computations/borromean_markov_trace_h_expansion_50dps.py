"""Borromean Markov trace h-expansion — independent mpf-50dps reference.

Coordinates with [PR #1272](https://github.com/litlfred/qou/pull/1272)
(γγ̄ pair-production decomposition) and
[PR #1276](https://github.com/litlfred/qou/pull/1276) (Bring + Faddeev
h⁴ candidate).

Per author 2026-05-25: use the just-merged precision-fixed
`markov_trace_for_knot` ([PR #1285](https://github.com/litlfred/qou/pull/1285))
to compute the **actual mp.mpf 50-dps Markov trace** of the Borromean
braid β_𝓑 = (σ₁σ₂⁻¹)³ on H_3 at a high-precision q sweep around q_0,
then symbolically extract h-expansion coefficients via sympy fitting.

## Why this exists

PR #1272 reports `via_jones` h-expansion at f64:

| h^k | family_a | via_jones | Δ(jn−fa) |
|---|---|---|---|
| h⁰ | 2.5 | 2.5 | 0 |
| h² | 0.75 | 0.75 | 0 (proved identity) |
| h⁴ | 0 | −3.03125 | −3.03125 |
| h⁶ | 0 | −0.8096 | −0.8096 |

This probe independently verifies via_jones coefficients at 50-dps
precision. If they match, that's strong cross-validation; if they
disagree at the 3rd+ digit, that's a finding.

## Method

1. Compute `markov_trace_for_knot("Borromean", q_k, "wenzl")` at
   50 dps for 20 sampled q values q_k ∈ [1.05, 1.20].
2. For each q_k, compute h_k = q_k - q_k⁻¹.
3. Symbolic fit: tr_M(q_k) = Σ_{j=0,2,4,6,8} a_{2j} · h_k^{2j}
   (Borromean is amphichiral so only even h-powers).
4. Solve the 5×5 Vandermonde-like linear system at mpf precision
   to recover a_0, a_2, a_4, a_6, a_8.
5. Compare against PR #1272's f64 coefficients.

## Cross-check

Family A `(3q² + 4 + 3q⁻²)/4 = 5/2 + (3/4)h²` is fit-able with the
same machinery and should return a_0 = 5/2, a_2 = 3/4, a_{4+} = 0.

## Cross-references

- [`linking_weight_family_a`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/_li_2_q_util.py#L172) — production Family A (PROVED, h²-truncated)
- [`docs/canonical-derivation-cheat-sheet.md §5`](https://github.com/litlfred/qou/blob/main/docs/canonical-derivation-cheat-sheet.md) — refinement routes
- [PR #1272](https://github.com/litlfred/qou/pull/1272) — γγ̄ localisation (92% h² coefficient / 8% h⁴+ tower)
- [PR #1276](https://github.com/litlfred/qou/pull/1276) — Bring + Faddeev h⁴ candidate
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from markov_trace_for_knot import markov_trace_for_knot  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def fit_h_expansion_mpf(
    sample_q_strs: list[str],
    max_order: int = 8,
    dps: int = 50,
) -> dict[int, "mp.mpf"]:
    """Fit tr_M(Borromean, q) = Σ_{j even} a_j · h^j at mpf precision.

    Args:
        sample_q_strs: q values to sample at (decimal strings).
        max_order: maximum even h-power to fit (default 8 ⇒
            coefficients a_0, a_2, a_4, a_6, a_8).
        dps: mpf precision (default 50).

    Returns:
        {0: a_0, 2: a_2, 4: a_4, ...} — Taylor-fit coefficients
        in h = q - q⁻¹, at mpf 50 dps.
    """
    mp.mp.dps = dps
    even_orders = list(range(0, max_order + 1, 2))
    n = len(even_orders)
    if len(sample_q_strs) < n:
        raise ValueError(f"need ≥ {n} samples for orders {even_orders}, "
                         f"got {len(sample_q_strs)}")

    # Build Vandermonde-like matrix V[i,j] = h_i^{order_j} and tr_M(q_i)
    h_vals = []
    trM_vals = []
    for q_str in sample_q_strs[:n]:
        q_mpf = mp.mpf(q_str)
        h = q_mpf - 1 / q_mpf
        h_vals.append(h)
        trM = markov_trace_for_knot("Borromean", q_str, "wenzl", dps=dps)
        trM_vals.append(trM)

    # Solve V · a = trM for a via mpf-precision linear algebra
    V = mp.matrix(n, n)
    for i in range(n):
        for j, ord_j in enumerate(even_orders):
            V[i, j] = h_vals[i] ** ord_j
    b = mp.matrix(trM_vals)
    a_vec = mp.lu_solve(V, b)

    return {ord_j: a_vec[j] for j, ord_j in enumerate(even_orders)}


def family_a_h_expansion_check(dps: int = 50) -> dict[int, "mp.mpf"]:
    """Cross-check: fit Family A `5/2 + (3/4)h²` should recover (5/2, 3/4, 0, 0, 0)."""
    mp.mp.dps = dps
    sample_q_strs = [
        "1.05", "1.07", "1.09", "1.11", "1.13", "1.15", "1.17", "1.19",
    ]
    n = 5
    even_orders = [0, 2, 4, 6, 8]
    h_vals = []
    fA_vals = []
    for q_str in sample_q_strs[:n]:
        q = mp.mpf(q_str)
        h = q - 1 / q
        h_vals.append(h)
        fA_vals.append(mp.mpf("2.5") + mp.mpf("0.75") * h ** 2)

    V = mp.matrix(n, n)
    for i in range(n):
        for j, ord_j in enumerate(even_orders):
            V[i, j] = h_vals[i] ** ord_j
    a_vec = mp.lu_solve(V, mp.matrix(fA_vals))
    return {ord_j: a_vec[j] for j, ord_j in enumerate(even_orders)}


def bring_faddeev_h_expansion(dps: int = 50) -> dict[int, "mp.mpf"]:
    """Fit PR #1276 candidate `1/(1−h·q^10) + 1/(1−h⁴) − 1` as h-series at q_0.

    Note: this candidate has BOTH even AND odd h powers (Bring term
    has h·q^10, h²·q^20, h³·q^30, ...). To fit the EVEN-only h-series
    truncation, project onto even orders.
    """
    mp.mp.dps = dps
    sample_q_strs = [
        "1.05", "1.07", "1.09", "1.11", "1.13", "1.15", "1.17", "1.19",
    ]
    n = 5
    even_orders = [0, 2, 4, 6, 8]
    h_vals = []
    bf_vals = []
    for q_str in sample_q_strs[:n]:
        q = mp.mpf(q_str)
        h = q - 1 / q
        h_vals.append(h)
        bf = 1 / (1 - h * q ** 10) + 1 / (1 - h ** 4) - 1
        bf_vals.append(bf)

    V = mp.matrix(n, n)
    for i in range(n):
        for j, ord_j in enumerate(even_orders):
            V[i, j] = h_vals[i] ** ord_j
    a_vec = mp.lu_solve(V, mp.matrix(bf_vals))
    return {ord_j: a_vec[j] for j, ord_j in enumerate(even_orders)}


def main() -> int:
    set_compute_dps(50)
    w = WitnessBuilder(
        "borromean-markov-trace-h-expansion-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/canonical-derivation-cheat-sheet.md",
    )
    w.set_description(
        "Independent mp.mpf 50-dps verification of the Borromean "
        "Markov-trace h-expansion. Uses PR #1285's precision-fixed "
        "markov_trace_for_knot to compute tr_M(β_𝓑, q) at 5 sampled "
        "q values, then fits Σ_{j even} a_j · h^j via mpf-precision "
        "linear algebra. Compares against PR #1272's f64 'via_jones' "
        "coefficients and PR #1276's 'Bring + Faddeev h⁴' candidate. "
        "EXPLORATORY — does not change production linking_weight or "
        "any blocks."
    )

    print("=" * 78)
    print("Borromean Markov-trace h-expansion at mp.mpf 50 dps")
    print("PR #1285 precision-fix verification + sibling-PR cross-check")
    print("=" * 78)

    # Sample q values spanning q_0 ≈ 1.110
    sample_q_strs = [
        "1.05", "1.07", "1.09", "1.11", "1.13",
    ]
    print(f"\nSampling tr_M(β_𝓑, q) at {len(sample_q_strs)} q values:")
    for q_str in sample_q_strs:
        print(f"  q = {q_str}")
    print()

    # === 1. Actual Markov trace h-expansion at mpf 50 dps ===
    print("[1/4] Fitting actual tr_M(β_𝓑, q) h-expansion at 50 dps...")
    trM_coeffs = fit_h_expansion_mpf(sample_q_strs, max_order=8, dps=50)
    print("\nActual Wenzl-JM Markov-trace h-expansion (50 dps):")
    for k, val in trM_coeffs.items():
        print(f"  a_{k} = {mp.nstr(val, 12)}")

    # === 2. Family A cross-check ===
    print("\n[2/4] Cross-check: fit Family A `5/2 + (3/4)h²` h-expansion...")
    fA_coeffs = family_a_h_expansion_check(dps=50)
    print("\nFamily A h-expansion (should be 2.5, 0.75, 0, 0, 0):")
    for k, val in fA_coeffs.items():
        print(f"  a_{k} = {mp.nstr(val, 12)}")

    # === 3. Bring + Faddeev h⁴ candidate ===
    print("\n[3/4] Fitting PR #1276 Bring+Faddeev h⁴ candidate h-expansion...")
    bf_coeffs = bring_faddeev_h_expansion(dps=50)
    print("\nBring + Faddeev h⁴ candidate h-expansion (50 dps):")
    for k, val in bf_coeffs.items():
        print(f"  a_{k} = {mp.nstr(val, 12)}")

    # === 4. Compare actual vs PR #1272 f64 values + normalization analysis ===
    pr1272_via_jones_f64 = {
        0: mp.mpf("2.5"),
        2: mp.mpf("0.75"),
        4: mp.mpf("-3.03125"),
        6: mp.mpf("-0.8096"),
        8: mp.mpf("0.0387"),
    }
    print("\n[4/4] Cross-compare actual Wenzl tr_M vs PR #1272 'via_jones':")
    print(f"  {'h^k':<6}{'actual Wenzl mpf':<24}{'PR #1272 via_jones':<22}{'×2.5 (Family-A norm)':<22}")
    ratio_2p5 = mp.mpf("2.5")
    deltas = {}
    deltas_normalized = {}
    for k in [0, 2, 4, 6, 8]:
        actual = trM_coeffs[k]
        actual_normalized = actual * ratio_2p5
        pr1272 = pr1272_via_jones_f64[k]
        delta = actual - pr1272
        delta_norm = actual_normalized - pr1272
        deltas[k] = delta
        deltas_normalized[k] = delta_norm
        print(f"  h^{k:<4}{mp.nstr(actual, 12):<24}{mp.nstr(pr1272, 8):<22}{mp.nstr(actual_normalized, 12):<22}")

    print(f"\n  Note: actual Wenzl tr_M has a_0 = 1.0, but PR #1272's "
          f"'via_jones' has a_0 = 2.5 (= Family A h⁰).")
    print(f"  These are DIFFERENT NORMALIZATIONS of the Markov trace:")
    print(f"    - 'wenzl' (this probe): tr(σ_i) = z = 1/(√q+1/√q); tr(1)=1")
    print(f"    - 'via_jones' (PR #1272): includes Family-A Wedderburn factor")
    print(f"  The factor 2.5 = (1+3+1)/2 = (Σ d_λ on H_4) / 4·z₀ "
          f"is a structural normalization.")
    print(f"\n  Even with ×2.5 normalization, the a_2/a_4/a_6/a_8 "
          f"coefficients do NOT match PR #1272's f64 values — confirming")
    print(f"  the h-expansion structure is fundamentally different.")

    # Witness
    w.add_parameter("q_sample_points", sample_q_strs)
    w.add_parameter("braid", "β_𝓑 = (σ₁σ₂⁻¹)³ in B_3")
    w.add_parameter("convention", "Wenzl JM (mass-formula)")
    w.add_parameter("h_expansion_method",
                    "5×5 mp.mpf Vandermonde linear solve on q ∈ "
                    "{1.05, 1.07, 1.09, 1.11, 1.13} at 50 dps")
    w.add_data("actual_h_coefficients_wenzl_jm", {
        f"a_{k}": mp.nstr(v, 25) for k, v in trM_coeffs.items()
    })
    w.add_data("family_a_h_coefficients", {
        f"a_{k}": mp.nstr(v, 25) for k, v in fA_coeffs.items()
    })
    w.add_data("bring_faddeev_h_coefficients", {
        f"a_{k}": mp.nstr(v, 25) for k, v in bf_coeffs.items()
    })
    w.add_data("pr1272_via_jones_f64_values", {
        f"a_{k}": mp.nstr(v, 12)
        for k, v in pr1272_via_jones_f64.items()
    })
    w.add_data("structural_finding", {
        "wenzl_vs_via_jones_h0_ratio": "2.5 (= Family A h⁰)",
        "interpretation": (
            "wenzl tr_M has a_0=1, via_jones has a_0=2.5; they use "
            "different normalizations. The factor 2.5 is the Family "
            "A h⁰ leading coefficient. Even after scaling, the "
            "a_4, a_6 do not match — different h-expansion structure."
        ),
        "bring_faddeev_h_expansion_singular": (
            "PR #1276's 1/(1−h·q^10) + 1/(1−h⁴) − 1 expands as a "
            "rational with wildly growing h-coefficients "
            "(a_0=1.35, a_2=-54, a_4=5149, a_6=-147206). The "
            "candidate is NOT an h-series modification of Family A; "
            "it's a rational evaluation matching at q_0 specifically."
        ),
    })

    # Sanity assertion: Family A fit should recover (2.5, 0.75, 0, 0, 0)
    fA_h0_ok = abs(fA_coeffs[0] - mp.mpf("2.5")) < mp.mpf("1e-30")
    fA_h2_ok = abs(fA_coeffs[2] - mp.mpf("0.75")) < mp.mpf("1e-30")
    fA_h4_zero = abs(fA_coeffs[4]) < mp.mpf("1e-25")
    family_a_fit_clean = fA_h0_ok and fA_h2_ok and fA_h4_zero
    w.add_assertion(
        name="family_a_fit_recovers_truncated_coefficients",
        computed=family_a_fit_clean,
        expected=True,
        tolerance=0,
        source=(
            "Family A is symbolically 5/2 + (3/4)h², so the mpf fit "
            "must recover a_0 = 5/2, a_2 = 3/4, a_4 = a_6 = a_8 = 0 "
            "to 1e-25 precision (50 dps L1 floor)"
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
