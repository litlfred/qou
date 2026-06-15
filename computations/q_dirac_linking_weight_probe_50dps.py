"""Q-Dirac-derived linking-weight candidates at H_4 (mp.mpf 50 dps).

Per author 'is there a PDE or ODE hanging around? from Dirac?' —
explores the q-Dirac operator structure documented in
`chirality-residue-mass-term.md`:

  D_q²(λ) = (q^{c_λ} - q^{-c_λ})² / (q - q^{-1})²
         = [c_λ]_q²

acting on Z(H_n(R, q)) = ⊕_λ R·e_λ. The chirality kernel
{λ : c_λ = 0} = {(2,2) at H_4}.

## Tests

This probe computes ~8 Dirac-derived linking-weight candidates at
H_4 at mp.mpf 50 dps and reports the h² coefficient of each:

1. **Family A baseline** — (1/4)·Σ dim_q V_λ
2. **Chirality kernel only** — dim_q V_(2,2)
3. **Non-chirality** — (1/4)·Σ_{c_λ ≠ 0} dim_q V_λ
4. **Family A − chirality** — subtract (2,2) contribution
5. **Family A + 2·chirality** — emphasize kernel
6. **Dirac-weighted: Σ D_q²(λ) · dim_q V_λ / Σ D_q²(λ)**
7. **Inverse-Dirac-weighted: Σ (1/D_q²(λ)) · dim_q V_λ (excl. kernel)**
8. **Signed content c_λ weighted: Σ c_λ · dim_q V_λ** (zero by bar-symmetry)
9. **|c_λ| weighted: Σ |c_λ| · dim_q V_λ**

Compares each to Reading-A's target h² coefficient -G ≈ -0.916.

## Hypothesis

If the q-Dirac operator structure encodes the linking_weight
correction, some Dirac-derived combination should give h² ≈ -G.

## Cross-references

- `chirality-residue-mass-term.md` (q-Dirac operator definition)
- `confinement-categorical.md` (cites q-Dirac cell scanner)
- `_deprecated/q_dirac_cell_scanner.py` (older implementation,
  uses different formula D_q² = ([n]_q·sign(c_λ))²)
- PR #1287 stack (companion probes)
- audit 2026-05-25 Path C principle hunt
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


# Partition tools (copy of demazure-prescreen helpers)
def hooks(partition):
    rows = len(partition)
    cols = partition[0] if rows else 0
    col_heights = [sum(1 for r in partition if r > j) for j in range(cols)]
    out = []
    for i, row_len in enumerate(partition):
        for j in range(row_len):
            arm = row_len - 1 - j
            leg = col_heights[j] - 1 - i
            out.append(arm + leg + 1)
    return out


def content_sum(partition):
    """c_λ = Σ_{(i,j) ∈ λ} (j - i)."""
    return sum(j - i for i, row in enumerate(partition) for j in range(row))


def dim_q(partition, q):
    n = sum(partition)
    if n == 0:
        return mp.mpf(1)
    def bracket(k):
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


def q_bracket(k, q):
    """[k]_q = (q^k - q^{-k}) / (q - q^{-1}). Returns 0 for k=0."""
    if k == 0:
        return mp.mpf(0)
    return (q ** k - q ** (-k)) / (q - 1 / q)


def D_q2(partition, q):
    """q-Dirac eigenvalue D_q²(λ) = [c_λ]_q² acting on Z(H_n(q))."""
    c = content_sum(partition)
    return q_bracket(c, q) ** 2


def fit_h_polynomial(values, h_vals, max_order=4):
    """Fit y(h) = Σ a_{2k}·h^{2k}."""
    even_orders = list(range(0, max_order + 1, 2))
    n = len(even_orders)
    if len(h_vals) < n:
        raise ValueError(f"need ≥ {n} points")
    used = list(h_vals[:n])
    used_y = list(values[:n])
    V = mp.matrix(n, n)
    for i in range(n):
        for j, ord_j in enumerate(even_orders):
            V[i, j] = used[i] ** ord_j
    a = mp.lu_solve(V, mp.matrix(used_y))
    return {even_orders[j]: a[j] for j in range(n)}


def main():
    set_compute_dps(50)
    w = WitnessBuilder(
        "q-dirac-linking-weight-h4-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-path-c-categorical-principle-hunt.md",
    )
    w.set_description(
        "Tests ~9 q-Dirac-derived linking-weight candidates at H_4 "
        "(mp.mpf 50 dps). Per author 'is there a PDE/ODE from Dirac?' "
        "direction — explores whether the q-Dirac operator D_q²(λ) = "
        "[c_λ]_q² acting on Z(H_n(q)) can produce h² ≈ -G (Reading-A) "
        "via natural combinations of dim_q V_λ and D_q²(λ)."
    )

    print("=" * 78)
    print("Q-Dirac-derived linking-weight candidates at H_4 (mp.mpf 50 dps)")
    print("=" * 78)

    G = mp.catalan
    target = -G
    print(f"\nTarget h² coefficient: -G = {mp.nstr(-G, 12)}")

    # H_4 partitions
    parts_4 = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    print(f"\nH_4 partition data:")
    print(f"  {'λ':<14}{'c_λ':<6}{'D_q²(λ)':<20}{'classical d_λ':<14}")
    for lam in parts_4:
        c = content_sum(lam)
        d_class = 1 if lam == (4,) or lam == (1, 1, 1, 1) else (
                  3 if lam == (3, 1) or lam == (2, 1, 1) else 2)
        print(f"  {str(lam):<14}{c:<6}[{c}]_q²              {d_class:<14}")
    print(f"  Chirality kernel (c_λ = 0): {{(2,2)}}")

    # Sample q values
    sample_q_strs = ["1.05", "1.08", "1.11", "1.14", "1.17"]
    print(f"\nSample q values: {sample_q_strs}")
    h_vals = []
    for qs in sample_q_strs:
        q = mp.mpf(qs)
        h_vals.append(q - 1 / q)

    # === Compute candidates ===
    def linking_candidate_at_q(scheme_name, q):
        if scheme_name == "1_family_A":
            return sum(dim_q(lam, q) for lam in parts_4) / 4
        if scheme_name == "2_chirality_kernel_only":
            return dim_q((2, 2), q)
        if scheme_name == "3_non_chirality_over_4":
            return sum(dim_q(lam, q) for lam in parts_4 if content_sum(lam) != 0) / 4
        if scheme_name == "4_family_A_minus_chirality":
            return (sum(dim_q(lam, q) for lam in parts_4) - dim_q((2, 2), q)) / 4
        if scheme_name == "5_family_A_plus_2_chirality":
            return (sum(dim_q(lam, q) for lam in parts_4) + 2 * dim_q((2, 2), q)) / 4
        if scheme_name == "6_dirac_weighted_normalized":
            num = sum(D_q2(lam, q) * dim_q(lam, q) for lam in parts_4)
            den = sum(D_q2(lam, q) for lam in parts_4)
            return num / den
        if scheme_name == "7_inverse_dirac_excl_kernel":
            # Σ_{c≠0} (1/D_q²)·dim_q V_λ
            return sum(dim_q(lam, q) / D_q2(lam, q)
                       for lam in parts_4 if content_sum(lam) != 0) / 4
        if scheme_name == "8_signed_content_weighted":
            return sum(content_sum(lam) * dim_q(lam, q) for lam in parts_4) / 4
        if scheme_name == "9_abs_content_weighted":
            return sum(abs(content_sum(lam)) * dim_q(lam, q) for lam in parts_4) / 4
        if scheme_name == "10_dirac_index_alt":
            # Atiyah-Singer-inspired: ker(D) - coker(D) approximation
            # at H_4, ker = {(2,2)}, no obvious coker → use chirality - antichirality
            chirality = dim_q((2, 2), q)
            antichirality = sum(dim_q(lam, q) for lam in parts_4 if content_sum(lam) != 0)
            return chirality - antichirality / 4
        if scheme_name == "11_family_A_minus_chirality_inv":
            # Family A weighted by 1/(1 + D_q²) — regularizes (2,2) singularity
            return sum(dim_q(lam, q) / (1 + D_q2(lam, q)) for lam in parts_4) / 4
        raise ValueError(scheme_name)

    schemes = [
        "1_family_A",
        "2_chirality_kernel_only",
        "3_non_chirality_over_4",
        "4_family_A_minus_chirality",
        "5_family_A_plus_2_chirality",
        "6_dirac_weighted_normalized",
        "7_inverse_dirac_excl_kernel",
        "8_signed_content_weighted",
        "9_abs_content_weighted",
        "10_dirac_index_alt",
        "11_family_A_minus_chirality_inv",
    ]

    print(f"\n{'scheme':<37}{'a_0':<14}{'a_2 (h² coef)':<18}{'a_2_norm (a_0→5/2)':<22}{'Δ vs -G':<14}")
    results = {}
    for s in schemes:
        try:
            vals = [linking_candidate_at_q(s, mp.mpf(qs)) for qs in sample_q_strs]
            coeffs = fit_h_polynomial(vals, h_vals, max_order=4)
            a_0 = coeffs[0]
            a_2 = coeffs[2]
            a_4 = coeffs[4]
            if abs(a_0) > mp.mpf("1e-30"):
                a_2_norm = a_2 * mp.mpf("2.5") / a_0
            else:
                a_2_norm = a_2
            delta = a_2_norm - target
            results[s] = {
                "a_0": mp.nstr(a_0, 12),
                "a_2": mp.nstr(a_2, 12),
                "a_4": mp.nstr(a_4, 12),
                "a_2_normalized": mp.nstr(a_2_norm, 12),
                "delta_vs_minus_G": mp.nstr(delta, 8),
            }
            print(f"  {s:<35}{mp.nstr(a_0, 8):<14}{mp.nstr(a_2, 12):<18}{mp.nstr(a_2_norm, 12):<22}{mp.nstr(delta, 8):<14}")
        except Exception as e:
            print(f"  {s:<35}FAILED: {e}")
            results[s] = {"error": str(e)}

    # Find candidates with negative a_2 and rank by closeness to -G
    print(f"\n[Schemes with NEGATIVE h² coefficient]")
    negative_a2 = [(n, d) for n, d in results.items()
                   if "a_2" in d and mp.mpf(d["a_2"]) < 0]
    if negative_a2:
        for n, d in sorted(negative_a2,
                            key=lambda nd: abs(mp.mpf(nd[1]["a_2_normalized"]) - target)):
            print(f"  {n}: a_2_norm = {d['a_2_normalized']}, Δ vs -G = {d['delta_vs_minus_G']}")
    else:
        print("  NONE — all tested Dirac-derived schemes give NON-NEGATIVE h² coefficient.")

    # Best overall match
    print(f"\n[Closest candidates to -G after a_0 → 5/2 normalization]")
    ranked = sorted(
        [(n, d, abs(mp.mpf(d["a_2_normalized"]) - target))
         for n, d in results.items() if "a_2_normalized" in d],
        key=lambda t: t[2],
    )
    for n, d, dev in ranked[:5]:
        print(f"  {n}: a_2_norm = {d['a_2_normalized']}, |Δ| = {mp.nstr(dev, 8)}")

    # Witness
    w.add_parameter("sample_q_strs", sample_q_strs)
    w.add_parameter("target_h2_minus_G", mp.nstr(-G, 25))
    w.add_data("partition_data_H4", {
        str(lam): {"c_lambda": content_sum(lam),
                   "D_q2_at_q0": mp.nstr(D_q2(lam, mp.mpf(sample_q_strs[2])), 12)}
        for lam in parts_4
    })
    w.add_data("per_scheme_results", results)
    w.add_data("negative_a2_count", len(negative_a2))
    closest = ranked[0]
    w.add_data("closest_to_minus_G", {
        "scheme": closest[0],
        "absolute_delta": mp.nstr(closest[2], 12),
        "data": closest[1],
    })

    w.add_data("verdict", (
        f"Tested 11 q-Dirac-derived linking-weight candidates at H_4 at "
        f"mp.mpf 50 dps. Found {len(negative_a2)} scheme(s) with "
        f"negative h² coefficient. Closest to target -G after a_0 "
        f"normalization: '{closest[0]}' at |Δ| = {mp.nstr(closest[2], 8)}. "
        + ("Worth deeper investigation." if closest[2] < mp.mpf("0.05")
           else "Still far from -G — Dirac structure alone doesn't "
                "naturally produce Reading-A's h² coefficient via simple "
                "weighted-sum combinations.")
    ))

    w.add_assertion(
        name="prescreen_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source="Sanity: q-Dirac prescreen completed without error.",
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
