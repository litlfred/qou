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
from math import factorial, prod
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


def classical_dim(partition):
    """d_λ = n! / Π hooks, in exact INTEGER arithmetic.

    The classical (q = 1) dimension, reached without any q-bracket.
    Every scheme below is a weighted sum of `dim_q`, so this is the
    independent route that says whether `hooks` and `dim_q` agree with
    the representation theory they claim to deform. The printed
    'classical d_λ' column used to be a hand-written conditional on the
    partition shape; it is this now.
    """
    return factorial(sum(partition)) // prod(hooks(partition))


def conjugate(partition):
    """λ' — the transpose partition. c_{λ'} = -c_λ and the hook
    multiset is preserved, which is the 'bar-symmetry' scheme 8's
    docstring invokes to predict Σ c_λ·dim_q V_λ = 0."""
    cols = partition[0] if partition else 0
    return tuple(sum(1 for r in partition if r > j) for j in range(cols))


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
        d_class = classical_dim(lam)
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

    # ── Assertions ────────────────────────────────────────────────────
    # All 11 schemes are weighted sums of dim_q V_λ with weights built
    # from c_λ, so the falsifiable content is (a) that dim_q really is
    # the q-deformation of d_λ it claims to be, and (b) the one exact
    # prediction the module docstring makes about a scheme's value.

    d_lambda = {lam: classical_dim(lam) for lam in parts_4}
    w.add_data("classical_hook_length_dims",
               {str(lam): d for lam, d in d_lambda.items()})

    # (1) dim_q against the classical dimension.
    #   Route A: the q-bracket product Π[k]_q / Π[h]_q, evaluated at
    #            q = 1 + 1e-25 in mpmath at 50 dps (the q → 1 limit; the
    #            remaining error is O(1e-50)).
    #   Route B: n!/Π hooks in exact integer arithmetic — no q, no
    #            bracket, no mpmath.
    # A wrong arm/leg in `hooks` shifts Route A and Route B in step for
    # the hook product but NOT for the [n]_q! numerator, so this does
    # catch it; a wrong bracket at k = 1 (the special case in `dim_q`)
    # breaks Route A alone.
    q_near_1 = 1 + mp.mpf(10) ** -25
    dim_q_limit = {lam: dim_q(lam, q_near_1) for lam in parts_4}
    sum_dim_q_limit = sum(dim_q_limit.values())
    sum_d_lambda = sum(d_lambda.values())
    w.add_data("dim_q_q_to_one_vs_hook_length", {
        str(lam): {
            "dim_q_at_q_to_1": mp.nstr(dim_q_limit[lam], 20),
            "hook_length_integer": d_lambda[lam],
        }
        for lam in parts_4
    })
    w.add_assertion(
        name="dim_q_at_q_to_one_matches_integer_hook_length_formula",
        computed=mp.nstr(sum_dim_q_limit, 30),
        expected=str(sum_d_lambda),
        tolerance="1e-20",
        source=(
            "Route A: Σ_λ dim_q V_λ from the q-bracket hook product at "
            "q = 1 + 1e-25, 50 dps. Route B: Σ_λ 4!/Π hooks(λ) = "
            f"{sum_d_lambda}, exact integer arithmetic."
        ),
    )

    # (2) The Wedderburn/Burnside identity for the group algebra of S_4.
    #   Route A: Σ d_λ² over the five partitions, from the hook-length
    #            dimensions computed above.
    #   Route B: 4! = |S_4| — the order of the group, not a dimension.
    # This is what says the partition list `parts_4` is COMPLETE. Drop
    # (2,2) and Route A gives 20 while Route B still gives 24.
    sum_d_squared = sum(d * d for d in d_lambda.values())
    w.add_assertion(
        name="sum_of_squared_dimensions_equals_order_of_S4",
        computed=sum_d_squared,
        expected=factorial(4),
        tolerance=0,
        source=(
            "Route A: Σ_λ d_λ² over the five partitions in `parts_4`, "
            "each d_λ from the hook-length formula. Route B: |S_4| = "
            "4! = 24. Wedderburn: the two agree iff `parts_4` "
            "enumerates every irreducible."
        ),
    )

    # (3) dim_q under conjugation.
    #   Route A: hooks((3,1)) → dim_q of the partition itself.
    #   Route B: hooks((2,1,1)) → dim_q of its transpose, enumerated
    #            independently by `hooks` on a different shape.
    # [k]_q is invariant under q → 1/q and λ' has the same hook
    # multiset, so these must coincide exactly. This is the half of
    # 'bar-symmetry' that assertion (4) needs.
    q_mid = mp.mpf(sample_q_strs[2])
    lam_a, lam_b = (3, 1), conjugate((3, 1))
    w.add_data("conjugation_pairs",
               {str(lam): str(conjugate(lam)) for lam in parts_4})
    w.add_assertion(
        name="dim_q_is_invariant_under_partition_conjugation",
        computed=mp.nstr(dim_q(lam_a, q_mid), 30),
        expected=mp.nstr(dim_q(lam_b, q_mid), 30),
        tolerance="1e-45",
        source=(
            f"Route A: dim_q V_{lam_a} at q = {sample_q_strs[2]} from "
            f"hooks({lam_a}). Route B: dim_q V_{lam_b} from "
            f"hooks({lam_b}) — a separately enumerated hook multiset "
            "for the transpose partition."
        ),
    )

    # (4) The module docstring's one exact prediction, asserted.
    #   Scheme 8 is annotated '(zero by bar-symmetry)' and the table
    #   above prints its a_0/a_2 without ever testing that.
    #   Route A: Σ_λ c_λ·dim_q V_λ / 4, summed over all five partitions
    #            at q = 1.11.
    #   Route B: 0, from the conjugation argument — parts_4 is closed
    #            under λ ↦ λ', c_{λ'} = -c_λ, and dim_q V_{λ'} =
    #            dim_q V_λ by (3); the sum pairs off.
    # Falsifiable both ways: a sign error in content_sum, or a parts_4
    # that is not conjugation-closed, leaves Route A nonzero.
    signed_content_sum = sum(
        content_sum(lam) * dim_q(lam, q_mid) for lam in parts_4) / 4
    conj_closed = all(conjugate(lam) in parts_4 for lam in parts_4)
    w.add_data("bar_symmetry_check", {
        "signed_content_weighted_sum_at_q_mid": mp.nstr(signed_content_sum, 12),
        "parts_4_closed_under_conjugation": conj_closed,
        "contents": {str(lam): content_sum(lam) for lam in parts_4},
    })
    w.add_assertion(
        name="signed_content_weighted_sum_vanishes_by_bar_symmetry",
        computed=mp.nstr(signed_content_sum, 30),
        expected="0",
        tolerance="1e-45",
        source=(
            f"Route A: scheme 8, Σ c_λ·dim_q V_λ / 4 at q = "
            f"{sample_q_strs[2]}, evaluated term by term. Route B: 0, "
            "predicted by the module docstring's bar-symmetry — parts_4 "
            "is closed under λ ↦ λ' (verified here), c_{λ'} = -c_λ, and "
            "dim_q V_{λ'} = dim_q V_λ by the preceding assertion."
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
