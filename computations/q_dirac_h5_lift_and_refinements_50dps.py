"""Q-Dirac scheme lifted to H_5 + further refinements (50 dps).

Per author 'continue exploring' — follows up on q_dirac_linking_weight_extended_50dps.py
which found (1+D_q²)/ΣW gives a_2_norm = -0.880 (3.5% off Reading-A's -G).

## Tests at H_5

Lifts the top Dirac variants to H_5 (7 partitions, KL polynomials
non-trivial). Does the match to -G improve at H_5, stay the same,
or degrade?

If h² coefficient is CONSTANT across N (= -0.880), it's an
H_N-independent structural quantity — strong evidence Dirac is
the right structure.

If h² coefficient drifts toward -G as N grows, the EXACT -G comes
from N → ∞ limit (would be a major finding).

If h² drifts away from -G, the H_4 hit is an accident.

## Refined variants at H_4

- (1 + α·D_q²) for α ∈ {1/24, 1/8, 1/4, 1, 2, 1/G}
- (1 + D_q²/4)
- (D_q² + ε)/(ΣW) for ε ∈ {0.5, 1, 2}
- cosh-like: (q^{c_λ} + q^{-c_λ})/2
- (sign · D_q²)
- Constructed to match -G EXACTLY: solve for α in (1 + α·D_q²)·dim_q / Σ

## Cross-references

- q_dirac_linking_weight_extended_50dps.py (parent, 3.5% finding)
- chirality-residue-mass-term.md (q-Dirac definition)
- audit 2026-05-25 Path C
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def hooks(p):
    rows = len(p)
    cols = p[0] if rows else 0
    col_h = [sum(1 for r in p if r > j) for j in range(cols)]
    out = []
    for i, rl in enumerate(p):
        for j in range(rl):
            out.append((rl - 1 - j) + (col_h[j] - 1 - i) + 1)
    return out


def content_sum(p):
    return sum(j - i for i, row in enumerate(p) for j in range(row))


def dim_q(p, q):
    n = sum(p)
    if n == 0:
        return mp.mpf(1)
    def br(k):
        if k == 1:
            return mp.mpf(1)
        return (q ** k - q ** (-k)) / (q - 1 / q)
    nf = mp.mpf(1)
    for k in range(1, n + 1):
        nf = nf * br(k)
    hp = mp.mpf(1)
    for h in hooks(p):
        hp = hp * br(h)
    return nf / hp


def q_br(k, q):
    if k == 0:
        return mp.mpf(0)
    return (q ** k - q ** (-k)) / (q - 1 / q)


def D_q2(p, q):
    return q_br(content_sum(p), q) ** 2


def partitions_of(n):
    out = []
    def rec(r, mx, pref):
        if r == 0:
            out.append(tuple(pref))
            return
        for k in range(min(mx, r), 0, -1):
            rec(r - k, k, pref + [k])
    rec(n, n, [])
    return out


def fit_h(values, h_vals, max_order=4):
    even = list(range(0, max_order + 1, 2))
    n = len(even)
    V = mp.matrix(n, n)
    for i in range(n):
        for j, o in enumerate(even):
            V[i, j] = h_vals[i] ** o
    a = mp.lu_solve(V, mp.matrix(values[:n]))
    return {even[j]: a[j] for j in range(n)}


def test_scheme(parts, alpha_W_fn, sample_q_strs, h_vals,
                G_target=None):
    """Compute (alpha_W(λ, q)·dim_q V_λ summed, then h-fit and report.

    alpha_W_fn: (λ, q) -> weight
    """
    try:
        vals = []
        for qs in sample_q_strs:
            q = mp.mpf(qs)
            num = sum(alpha_W_fn(p, q) * dim_q(p, q) for p in parts)
            den = sum(alpha_W_fn(p, q) for p in parts)
            if abs(den) < mp.mpf("1e-40"):
                return None
            vals.append(num / den)
        coeffs = fit_h(vals, h_vals, max_order=4)
        a0 = coeffs[0]
        a2 = coeffs[2]
        if abs(a0) < mp.mpf("1e-30"):
            return None
        a2_norm = a2 * mp.mpf("2.5") / a0
        delta = a2_norm - G_target if G_target is not None else a2_norm
        return {"a_0": a0, "a_2": a2, "a_2_norm": a2_norm,
                "abs_delta": abs(delta)}
    except Exception:
        return None


def main():
    set_compute_dps(50)
    w = WitnessBuilder(
        "q-dirac-h5-lift-and-refinements-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-path-c-categorical-principle-hunt.md",
    )
    w.set_description(
        "Q-Dirac probe Part 3: lifts (1+D_q²)/ΣW scheme to H_5 and "
        "tests refined variants at H_4 to close the 3.5% gap to -G. "
        "Includes alpha-tuned and cosh-based variants."
    )

    print("=" * 78)
    print("Q-Dirac H_5 lift + refinement variants (50 dps)")
    print("=" * 78)

    G = mp.catalan
    target = -G
    print(f"\nTarget h² coefficient: -G = {mp.nstr(-G, 12)}")

    sample_q_strs = ["1.05", "1.08", "1.11", "1.14", "1.17"]
    h_vals = [mp.mpf(qs) - 1 / mp.mpf(qs) for qs in sample_q_strs]
    print(f"Sample q values: {sample_q_strs}")

    # === Part 1: Lift (1+D_q²)/ΣW to H_4, H_5, H_6, H_7 ===
    print(f"\n--- Part 1: Lift (1+D_q²)/ΣW across H_N ---")
    print(f"{'N':<4}{'a_0':<14}{'a_2':<16}{'a_2_norm':<18}{'|Δ vs -G|':<14}")

    lift_results = {}
    for n in [4, 5, 6, 7]:
        parts = partitions_of(n)
        r = test_scheme(parts, lambda p, q: 1 + D_q2(p, q),
                        sample_q_strs, h_vals, G_target=target)
        if r is None:
            print(f"  H_{n}: FAILED")
            continue
        lift_results[f"H_{n}"] = {
            "a_0": mp.nstr(r["a_0"], 12),
            "a_2": mp.nstr(r["a_2"], 12),
            "a_2_norm": mp.nstr(r["a_2_norm"], 12),
            "abs_delta": mp.nstr(r["abs_delta"], 8),
        }
        print(f"  H_{n}: {mp.nstr(r['a_0'], 8):<14}{mp.nstr(r['a_2'], 12):<16}{mp.nstr(r['a_2_norm'], 12):<18}{mp.nstr(r['abs_delta'], 8):<14}")

    # === Part 2: Refined variants at H_4 ===
    print(f"\n--- Part 2: Refined α-tuned variants at H_4 ---")
    parts_4 = partitions_of(4)
    variants = {}

    # Different alpha values in (1 + α·D_q²)
    for alpha_label, alpha in [
        ("(1 + D_q²/24)", mp.mpf(1) / 24),
        ("(1 + D_q²/8)", mp.mpf(1) / 8),
        ("(1 + D_q²/4)", mp.mpf(1) / 4),
        ("(1 + D_q²/2)", mp.mpf(1) / 2),
        ("(1 + D_q²)", mp.mpf(1)),
        ("(1 + 2·D_q²)", mp.mpf(2)),
        ("(1 + D_q²·G)", G),
        ("(1 + D_q²/G)", 1 / G),
        ("(1 + D_q²·π/G)", mp.pi / G),
    ]:
        a_val = alpha
        r = test_scheme(parts_4, lambda p, q: 1 + a_val * D_q2(p, q),
                        sample_q_strs, h_vals, G_target=target)
        if r:
            variants[alpha_label] = r

    # Cosh-style: q^c + q^{-c}
    def cosh_weight(p, q):
        c = content_sum(p)
        if c == 0:
            return mp.mpf(2)  # 1 + 1
        return q ** c + q ** (-c)
    r = test_scheme(parts_4, cosh_weight, sample_q_strs, h_vals, G_target=target)
    if r:
        variants["(q^c + q^{-c}) [cosh]"] = r

    # Sinh²-style: |[c]_q|²·dim_q V_λ — same as D_q²
    # Already tested.

    # (q^{c_λ} - q^{-c_λ})² as a weight (= D_q² · (q-q⁻¹)²)
    def D_squared_unrescaled(p, q):
        c = content_sum(p)
        return (q ** c - q ** (-c)) ** 2
    r = test_scheme(parts_4, D_squared_unrescaled, sample_q_strs, h_vals, G_target=target)
    if r:
        variants["(q^c - q^{-c})²"] = r

    # Constant-shift weight: (k + D_q²) for various k
    for k_val in [mp.mpf(2), mp.mpf(4), mp.mpf("0.5"), mp.mpf("0.25")]:
        kk = k_val
        r = test_scheme(parts_4, lambda p, q: kk + D_q2(p, q),
                        sample_q_strs, h_vals, G_target=target)
        if r:
            variants[f"({mp.nstr(k_val, 4)} + D_q²)"] = r

    # cosh(c·h) where h = log(q) — formal sense
    def cosh_log_weight(p, q):
        c = content_sum(p)
        log_q = mp.log(q)
        return mp.cosh(c * log_q)
    r = test_scheme(parts_4, cosh_log_weight, sample_q_strs, h_vals, G_target=target)
    if r:
        variants["cosh(c · log q)"] = r

    print(f"\n  {'variant':<30}{'a_0':<14}{'a_2_norm':<18}{'|Δ vs -G|':<14}")
    sorted_variants = sorted(variants.items(), key=lambda kv: kv[1]["abs_delta"])
    for name, r in sorted_variants:
        marker = " ⭐" if r["abs_delta"] < mp.mpf("0.005") else (
                  " *" if r["abs_delta"] < mp.mpf("0.05") else "")
        print(f"  {name:<30}{mp.nstr(r['a_0'], 8):<14}{mp.nstr(r['a_2_norm'], 12):<18}{mp.nstr(r['abs_delta'], 8):<14}{marker}")

    # === Part 3: SOLVE for the alpha in (1+α·D_q²) that gives a_2_norm = -G exactly ===
    print(f"\n--- Part 3: Solve for alpha that hits -G exactly ---")
    # Use bisection / Newton to find alpha such that scheme (1+α·D_q²)/ΣW yields a_2_norm = -G
    def residual(alpha_val):
        r = test_scheme(parts_4, lambda p, q: 1 + alpha_val * D_q2(p, q),
                        sample_q_strs, h_vals, G_target=target)
        if r is None:
            return None
        return r["a_2_norm"] - target

    # bisect: residual(α=0) corresponds to (1·dim_q)/5 = Family A normalized
    #   = ? let me compute: just dim_q V_λ summed and div by 5
    #   That's not quite Family A; Family A is /4.
    # Try α from 0.001 to 10
    alpha_low = mp.mpf("0.001")
    alpha_high = mp.mpf("10")
    r_low = residual(alpha_low)
    r_high = residual(alpha_high)
    print(f"  residual at α={alpha_low}: {mp.nstr(r_low, 8) if r_low else 'None'}")
    print(f"  residual at α={alpha_high}: {mp.nstr(r_high, 8) if r_high else 'None'}")

    optimal_alpha = None
    if r_low is not None and r_high is not None and r_low * r_high < 0:
        for _ in range(60):  # bisection iterations
            alpha_mid = (alpha_low + alpha_high) / 2
            r_mid = residual(alpha_mid)
            if r_mid is None:
                break
            if r_mid * r_low < 0:
                alpha_high = alpha_mid
                r_high = r_mid
            else:
                alpha_low = alpha_mid
                r_low = r_mid
        optimal_alpha = (alpha_low + alpha_high) / 2
        print(f"\n  Optimal α (gives a_2_norm = -G exactly): {mp.nstr(optimal_alpha, 25)}")
        # Sanity recheck
        r_opt = test_scheme(parts_4,
                            lambda p, q: 1 + optimal_alpha * D_q2(p, q),
                            sample_q_strs, h_vals, G_target=target)
        if r_opt:
            print(f"  a_2_norm at α_opt: {mp.nstr(r_opt['a_2_norm'], 25)}")
            print(f"  Δ vs -G:            {mp.nstr(r_opt['abs_delta'], 10)}")
            # Identify α as a known constant?
            print(f"\n  Candidate matches for α_opt:")
            print(f"    α_opt = {mp.nstr(optimal_alpha, 15)}")
            print(f"    1/α_opt = {mp.nstr(1/optimal_alpha, 15)}")
            print(f"    α_opt · G = {mp.nstr(optimal_alpha * G, 15)}")
            print(f"    α_opt / G = {mp.nstr(optimal_alpha / G, 15)}")
            print(f"    1 - α_opt = {mp.nstr(1 - optimal_alpha, 15)}")
    else:
        print(f"  Cannot bisect — residuals don't bracket zero in [{alpha_low}, {alpha_high}]")

    # Witness
    w.add_parameter("sample_q_strs", sample_q_strs)
    w.add_parameter("target_h2_minus_G", mp.nstr(-G, 25))
    w.add_data("lift_results_by_N", lift_results)
    w.add_data("refined_variants", {
        name: {
            "a_0": mp.nstr(r["a_0"], 25),
            "a_2_norm": mp.nstr(r["a_2_norm"], 25),
            "abs_delta": mp.nstr(r["abs_delta"], 12),
        }
        for name, r in variants.items()
    })
    if optimal_alpha is not None:
        w.add_data("optimal_alpha_for_minus_G_exact", {
            "alpha": mp.nstr(optimal_alpha, 25),
            "1_over_alpha": mp.nstr(1/optimal_alpha, 25),
            "alpha_times_G": mp.nstr(optimal_alpha * G, 25),
            "alpha_over_G": mp.nstr(optimal_alpha / G, 25),
            "1_minus_alpha": mp.nstr(1 - optimal_alpha, 25),
        })

    # Summary
    closest_variant = min(variants.items(), key=lambda kv: kv[1]["abs_delta"]) if variants else None
    if closest_variant:
        name, r = closest_variant
        w.add_data("closest_variant_overall", {
            "name": name,
            "a_2_norm": mp.nstr(r["a_2_norm"], 25),
            "abs_delta": mp.nstr(r["abs_delta"], 12),
        })

    w.add_assertion(
        name="probe_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source="Q-Dirac H_5 lift + refinements completed.",
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
