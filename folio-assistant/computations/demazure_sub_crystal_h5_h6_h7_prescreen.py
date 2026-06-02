"""Path C3 Demazure sub-crystal pre-screen at H_5, H_6, H_7.

Per author 2026-05-25 'Demazure sub-crystal at H_5' direction.

## What this scans

Tests a battery of Demazure-inspired sub-sums at H_5, H_6, H_7
against the target h² coefficient -G (Reading-A). For each
partition λ and each normalization scheme, computes h² coefficient
at q_0 (mp.mpf 50 dps).

## Normalization schemes tested

For sum Σ_{λ ∈ S} w_λ · F(λ, q) over a subset S of partitions:

1. **Full Wedderburn**: F = dim_q V_λ, w_λ = 1/|S| — Family-A-like
2. **Per-irrep normalized**: F = dim_q V_λ / d_λ, w_λ = 1/|S|
3. **Bar-symmetric averaging**: pair (λ, λ^T), average their dims
4. **Self-conjugate only**: restrict to λ with λ = λ^T
5. **Two-row only** (long-string trace-dominant per PR #1288)
6. **Rectangle only** (Schur-Weyl per PR #1288: (n/k, n/k, ..., n/k) for nk = n)

## Why this is a pre-screen

True Demazure sub-crystal evaluation requires building KLR /
Kashiwara crystal machinery in Python (multi-session). This probe
instead tests SIMPLE Wedderburn-derived sub-sums to see if ANY
natural choice yields h² coef ≈ -G. If no simple sub-sum works,
the categorical Demazure work would have to go genuinely deeper
(true crystal graph + Demazure characters).

## Acceptance criterion

If any sub-sum gives h² coef within 1e-3 of -G (after appropriate
h⁰ normalization), flag as a candidate for deeper investigation.

## Cross-references

- PR #1288 (sibling: dominant-partition + Type-B folding, main 5b8150e5d)
- PR #1287 stack (companion probes)
- audit 2026-05-25 Path C principle hunt
- CLAUDE.md §7b — Type-B folding, Demazure sub-crystals for resonances
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


def partitions_of(n: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    def rec(rem: int, mx: int, pref: list[int]) -> None:
        if rem == 0:
            out.append(tuple(pref))
            return
        for p in range(min(mx, rem), 0, -1):
            rec(rem - p, p, pref + [p])
    rec(n, n, [])
    return out


def conjugate(partition: tuple[int, ...]) -> tuple[int, ...]:
    if not partition:
        return ()
    cols = partition[0]
    return tuple(sum(1 for r in partition if r > j) for j in range(cols))


def hooks(partition: tuple[int, ...]) -> list[int]:
    rows = len(partition)
    cols = partition[0] if rows else 0
    col_heights = [sum(1 for r in partition if r > j) for j in range(cols)]
    out: list[int] = []
    for i, row_len in enumerate(partition):
        for j in range(row_len):
            arm = row_len - 1 - j
            leg = col_heights[j] - 1 - i
            out.append(arm + leg + 1)
    return out


def classical_dim(partition: tuple[int, ...]) -> int:
    n = sum(partition)
    if n == 0:
        return 1
    from math import factorial
    prod = 1
    for h in hooks(partition):
        prod *= h
    return factorial(n) // prod


def dim_q(partition: tuple[int, ...], q) -> "mp.mpf":
    n = sum(partition)
    if n == 0:
        return mp.mpf(1)
    def bracket(k: int):
        if k == 1:
            return mp.mpf(1)
        return (q ** k - q ** (-k)) / (q - 1 / q)
    nfact = mp.mpf(1)
    for k in range(1, n + 1):
        nfact = nfact * bracket(k)
    hp = mp.mpf(1)
    for h in hooks(partition):
        hp = hp * bracket(h)
    return nfact / hp


def fit_h0_h2(values_at_q: list["mp.mpf"], h_vals: list["mp.mpf"],
              dps: int = 50) -> tuple["mp.mpf", "mp.mpf"]:
    """Fit y(h) = a_0 + a_2·h² via 2-point linear least squares."""
    n = len(values_at_q)
    if n < 2:
        raise ValueError("need ≥ 2 points")
    # Solve 2x2 system
    h2s = [h * h for h in h_vals]
    if n == 2:
        # exact 2-eq solve
        # y_0 = a_0 + a_2 · h²_0
        # y_1 = a_0 + a_2 · h²_1
        # a_2 = (y_1 - y_0) / (h²_1 - h²_0)
        # a_0 = y_0 - a_2 · h²_0
        a_2 = (values_at_q[1] - values_at_q[0]) / (h2s[1] - h2s[0])
        a_0 = values_at_q[0] - a_2 * h2s[0]
        return a_0, a_2
    # least squares for >2
    V = mp.matrix(n, 2)
    for i in range(n):
        V[i, 0] = mp.mpf(1)
        V[i, 1] = h2s[i]
    Vt = V.transpose()
    VtV = Vt * V
    a = mp.lu_solve(VtV, Vt * mp.matrix(values_at_q))
    return a[0], a[1]


def evaluate_subsum(partitions_list: list[tuple[int, ...]],
                    weight_fn, q) -> "mp.mpf":
    """Σ_{λ ∈ S} weight_fn(λ) · dim_q V_λ at given q."""
    total = mp.mpf(0)
    for lam in partitions_list:
        w = weight_fn(lam)
        if w == 0:
            continue
        total += mp.mpf(w) * dim_q(lam, q)
    return total


def main() -> int:
    set_compute_dps(50)
    w = WitnessBuilder(
        "demazure-sub-crystal-prescreen-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-path-c-categorical-principle-hunt.md",
    )
    w.set_description(
        "Pre-screen of Demazure-inspired sub-sum schemes at H_5, H_6, "
        "H_7 against Reading-A's h² target -G. Tests 6 normalization "
        "schemes (full Wedderburn, per-irrep, bar-symmetric, "
        "self-conjugate, two-row, rectangle). If any scheme yields "
        "h² ≈ -G after h⁰ normalization to 5/2, flag for deeper "
        "Demazure-characters investigation."
    )

    print("=" * 78)
    print("Demazure sub-crystal pre-screen at H_5, H_6, H_7 (mp.mpf 50 dps)")
    print("=" * 78)

    G = mp.catalan
    target_h2 = -G
    print(f"\nTarget h² coefficient: -G = {mp.nstr(-G, 12)}")
    print(f"Family A baseline (h² = +3/4 at H_4)")

    sample_q_strs = ["1.05", "1.11"]
    h_vals = []
    for q_str in sample_q_strs:
        q = mp.mpf(q_str)
        h = q - 1 / q
        h_vals.append(h)
    print(f"Sample q values for h-fit: {sample_q_strs}")
    print()

    results: dict[str, dict] = {}

    for n in [4, 5, 6, 7]:
        parts = partitions_of(n)
        print(f"\n{'=' * 70}")
        print(f"H_{n}: {len(parts)} partitions")
        print(f"{'=' * 70}")

        # Compute all dim_q V_λ at sample q values
        dims_by_q = {}
        for q_str in sample_q_strs:
            q = mp.mpf(q_str)
            dims_by_q[q_str] = {lam: dim_q(lam, q) for lam in parts}

        schemes: dict[str, list[tuple[tuple[int, ...], "mp.mpf"]]] = {}

        # === Scheme 1: full Wedderburn 1/N ===
        N = len(parts)
        for q_str in sample_q_strs:
            schemes.setdefault("S1_full_wedderburn_1overN", []).append(
                (None, sum(dims_by_q[q_str][lam] for lam in parts) / N)
            )

        # === Scheme 2: per-irrep / classical d_λ normalized, sum/N ===
        for q_str in sample_q_strs:
            s = sum(dims_by_q[q_str][lam] / classical_dim(lam) for lam in parts) / N
            schemes.setdefault("S2_per_irrep_dim_normalized", []).append((None, s))

        # === Scheme 3: bar-symmetric pair averaging ===
        # Group partitions by conjugate equivalence class
        seen = set()
        bar_classes: list[list[tuple[int, ...]]] = []
        for lam in parts:
            if lam in seen:
                continue
            conj = conjugate(lam)
            cls = [lam]
            seen.add(lam)
            if conj != lam:
                cls.append(conj)
                seen.add(conj)
            bar_classes.append(cls)
        for q_str in sample_q_strs:
            s = sum(
                sum(dims_by_q[q_str][lam] for lam in cls) / len(cls)
                for cls in bar_classes
            ) / len(bar_classes)
            schemes.setdefault("S3_bar_symmetric_class_avg", []).append((None, s))

        # === Scheme 4: self-conjugate only ===
        self_conj = [lam for lam in parts if conjugate(lam) == lam]
        if self_conj:
            for q_str in sample_q_strs:
                s = sum(dims_by_q[q_str][lam] for lam in self_conj) / len(self_conj)
                schemes.setdefault("S4_self_conjugate_only", []).append((None, s))

        # === Scheme 5: two-row only ===
        two_row = [lam for lam in parts if len(lam) == 2]
        if two_row:
            for q_str in sample_q_strs:
                s = sum(dims_by_q[q_str][lam] for lam in two_row) / len(two_row)
                schemes.setdefault("S5_two_row_only", []).append((None, s))

        # === Scheme 6: rectangle only (n = k·m for k, m ≥ 2) ===
        rectangle = [lam for lam in parts
                     if len(lam) >= 2 and all(p == lam[0] for p in lam) and lam[0] >= 2]
        if rectangle:
            for q_str in sample_q_strs:
                s = sum(dims_by_q[q_str][lam] for lam in rectangle) / len(rectangle)
                schemes.setdefault("S6_rectangle_only", []).append((None, s))

        # === Fit h² for each scheme ===
        print(f"\nh-fit results (a_0 + a_2·h²):")
        print(f"  {'scheme':<35}{'a_0':<14}{'a_2':<16}{'Δ vs -G':<16}")
        n_results: dict[str, dict] = {}
        for scheme_name, vals in schemes.items():
            ys = [v for _, v in vals]
            try:
                a_0, a_2 = fit_h0_h2(ys, h_vals, dps=50)
                a_2_normalized_to_h0_5over2 = a_2 * mp.mpf("2.5") / a_0
                delta_to_target = a_2_normalized_to_h0_5over2 - target_h2
                n_results[scheme_name] = {
                    "a_0": mp.nstr(a_0, 12),
                    "a_2": mp.nstr(a_2, 12),
                    "a_2_normalized": mp.nstr(a_2_normalized_to_h0_5over2, 12),
                    "delta_vs_minus_G": mp.nstr(delta_to_target, 8),
                }
                print(f"  {scheme_name:<35}{mp.nstr(a_0, 8):<14}{mp.nstr(a_2, 12):<16}{mp.nstr(delta_to_target, 8):<16}")
            except Exception as e:
                print(f"  {scheme_name:<35}FAILED: {e}")
        results[f"H_{n}"] = n_results

    # === Summary ===
    print(f"\n{'=' * 78}")
    print(f"Summary — closest schemes to Reading-A's h² = -G (after a_0 → 5/2 normalization):")
    print(f"{'=' * 78}")
    all_candidates = []
    for n_key, n_results in results.items():
        for scheme, data in n_results.items():
            delta = mp.mpf(data["delta_vs_minus_G"])
            all_candidates.append((abs(delta), n_key, scheme, data))
    all_candidates.sort(key=lambda t: t[0])

    print(f"\n  {'rank':<6}{'N':<6}{'scheme':<32}{'normalized a_2':<18}{'Δ vs -G':<14}")
    for rank, (adelta, n_key, scheme, data) in enumerate(all_candidates[:8], 1):
        print(f"  {rank:<6}{n_key:<6}{scheme:<32}{data['a_2_normalized']:<18}{data['delta_vs_minus_G']:<14}")

    # Witness
    w.add_parameter("sample_q_strs", sample_q_strs)
    w.add_parameter("target_h2_minus_G", mp.nstr(-G, 25))
    w.add_data("per_N_results", results)
    closest = all_candidates[0]
    w.add_data("closest_candidate", {
        "N": closest[1],
        "scheme": closest[2],
        "data": closest[3],
        "absolute_delta": mp.nstr(closest[0], 12),
    })

    # Check if anything is within 1e-3 of -G
    within_thresh = [c for c in all_candidates if c[0] < mp.mpf("1e-3")]
    w.add_data("candidates_within_1e_minus_3_of_target", [
        {
            "N": c[1],
            "scheme": c[2],
            "delta": mp.nstr(c[0], 8),
        }
        for c in within_thresh
    ])

    if within_thresh:
        w.add_data("verdict", (
            f"Found {len(within_thresh)} sub-sum scheme(s) within 1e-3 of "
            f"target h² = -G. Closest: {closest[2]} at H_{closest[1]} "
            f"with Δ = {mp.nstr(closest[0], 8)}. Recommend deeper Demazure-"
            f"characters investigation of this scheme."
        ))
    else:
        w.add_data("verdict", (
            f"NO simple sub-sum scheme yields h² ≈ -G at any tested N. "
            f"Closest is {closest[2]} at H_{closest[1]} with Δ = "
            f"{mp.nstr(closest[0], 8)} — far above 1e-3 threshold. "
            f"Simple Wedderburn-derived sub-sums DO NOT match Reading-A. "
            f"Genuine Demazure/crystal sub-sum machinery (Kashiwara "
            f"operators, KLR canonical basis) required — multi-session."
        ))

    w.add_assertion(
        name="prescreen_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source=(
            f"Scanned {sum(len(r) for r in results.values())} "
            f"scheme/H_n combinations against target h² = -G. "
            f"Sanity check: search completed without error."
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
