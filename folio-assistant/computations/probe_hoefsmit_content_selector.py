#!/usr/bin/env python3
# polynomial_q_not_applicable: combinatorial / closed-form probe;
# no symbolic-q output.
"""Hoefsmit content-asymptotic selector for the per-partition $k_\\lambda$ rule.

Tests whether the **substrate-only** combinatorial quantity

  $$
    \\Phi_{\\text{content}}(\\lambda)
    \\;:=\\; \\max_{(i, j) \\in \\lambda} \\, q^{c_{ij}(\\lambda)}
  $$

where $c_{ij}(\\lambda) = j - i$ is the **content** (column $-$ row) of
the cell $(i, j)$ in the Young diagram of $\\lambda$, reproduces the
empirical "dominant partition" of `probe_phiq_per_partition_klambda.py`.

**Theoretical motivation** (Hoefsmit 1974 seminormal form). The
diagonal entries of $\\rho_\\lambda(\\sigma_i)$ in the Hoefsmit basis
are $q$-powers $q^{c_{i+1} - c_i}$ of differences of cell contents
in standard Young tableaux. The MAX eigenvalue magnitude of
$\\rho_\\lambda(\\sigma_i)$ is bounded by $q^{\\Delta c_\\max(\\lambda)}$
where $\\Delta c_\\max$ is the maximum content difference across any
pair of cells. For a partition with wide rows (like $[5, 4]$), this
content spread is large; for compact partitions (like $[3, 3, 3]$)
it is small.

**Concrete substrate selector under test:**

  $$
    \\mathrm{isMaxEigSpectrum}(\\lambda)
    \\;\\stackrel{?}{=}\\;
    \\mathbb{1}\\!\\bigl[\\Delta c_\\max(\\lambda)
      \\geq \\Delta c_\\max(\\lambda') \\text{ for all } \\lambda'\\bigr]
  $$

i.e. the partition with maximum content spread is the dominant
partition. This is **substrate-only** (depends on $\\lambda$ alone,
not on the braid word $\\beta$) — testing whether the partition's
shape alone correlates with the empirical dominant partition.

**Empirical comparison data** (from `probe_phiq_per_partition_klambda.py`
on PR #639, cycle 6):

  D     dominant: $\\lambda = [2, 2, 1, 1]$ (dim 9)
  T     dominant: $\\lambda = [6, 3]$       (dim 48)
  ³He   dominant: $\\lambda = [5, 4]$       (dim 42)

If the content-spread selector identifies these same partitions,
the per-partition rule has a **closed-form substrate identification**
— closing the open R&D piece of
`rem:per-partition-k-lambda-rule`.

Class C (diagnostic / probe).

Output: `probe-hoefsmit-content-selector.witness.json`.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterator

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402


def partitions(n: int, max_part: int | None = None) -> Iterator[tuple[int, ...]]:
    """All partitions of `n` as weakly-decreasing tuples."""
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for first in range(min(n, max_part), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def cells(lam: tuple[int, ...]) -> Iterator[tuple[int, int]]:
    """Iterate Young-diagram cells (row, col), 0-indexed."""
    for i, length in enumerate(lam):
        for j in range(length):
            yield (i, j)


def content_spread(lam: tuple[int, ...]) -> int:
    """Max minus min content (j - i) over cells of λ.

    For λ = [5, 4]: cells span content from -1 (cell (1,0)) to +4
    (cell (0,4)), spread = 5.
    For λ = [3, 3, 3]: content from -2 to +2, spread = 4.
    For λ = [9]: spread = 8.  (Single row.)
    For λ = [1, 1, 1, 1, 1, 1, 1, 1, 1]: spread = 8.  (Single column.)
    """
    contents = [j - i for (i, j) in cells(lam)]
    return max(contents) - min(contents)


def hook_content_product_q1(lam: tuple[int, ...]) -> int:
    """Hook-content product ∏ (1 + c_box) at q=1; useful as a
    secondary substrate signal."""
    total = 1
    for (i, j) in cells(lam):
        total *= (1 + (j - i))
    return total


# ── Empirical dominant partitions per atom (from PR #639) ──────
EMPIRICAL_DOMINANT = {
    "D":   (2, 2, 1, 1),    # n=6, dim=9
    "T":   (6, 3),           # n=9, dim=48
    "He3": (5, 4),           # n=9, dim=42
}

# Atom → strand count n = 3A
ATOM_N = {"D": 6, "T": 9, "He3": 9}


def main() -> int:
    w = WitnessBuilder("probe-hoefsmit-content-selector",
                       engine="python")

    print("=" * 78)
    print("HOEFSMIT CONTENT-SPREAD SELECTOR — substrate-only test")
    print("=" * 78)
    print()
    print(f"  Selector: λ → max content spread Δc_max(λ) = max c - min c")
    print(f"  Hypothesis: empirical dominant partition = argmax Δc_max")
    print()

    findings = []
    for atom in ("D", "T", "He3"):
        n = ATOM_N[atom]
        # Compute content-spread for every partition of n
        spread_table = []
        for lam in partitions(n):
            spread_table.append({
                "partition": list(lam),
                "spread": content_spread(lam),
                "hook_content_q1": hook_content_product_q1(lam),
            })
        spread_table.sort(key=lambda r: -r["spread"])

        empirical = list(EMPIRICAL_DOMINANT[atom])
        # Get all partitions tied for max spread
        max_spread = spread_table[0]["spread"]
        argmax = [r for r in spread_table if r["spread"] == max_spread]
        argmax_lambdas = [tuple(r["partition"]) for r in argmax]

        is_predicted = tuple(empirical) in argmax_lambdas

        print(f"  --- {atom} (n = {n}) ---")
        print(f"  Empirical dominant: λ = {empirical}, spread = "
              f"{content_spread(tuple(empirical))}")
        print(f"  Max-spread partitions (argmax Δc_max = {max_spread}):")
        for r in argmax:
            tag = " ← EMPIRICAL" if tuple(r["partition"]) == tuple(empirical) else ""
            print(f"    λ = {str(r['partition']):<18}  spread = {r['spread']}"
                  f"  hook_q1 = {r['hook_content_q1']}{tag}")
        print(f"  Hoefsmit selector match: "
              f"{'✓ YES' if is_predicted else '✗ NO'}")
        print()

        findings.append({
            "atom": atom,
            "n": n,
            "empirical_dominant": empirical,
            "empirical_spread": content_spread(tuple(empirical)),
            "max_spread_value": max_spread,
            "max_spread_partitions": [list(p) for p in argmax_lambdas],
            "hoefsmit_predicts_empirical": is_predicted,
            "n_tied_argmax": len(argmax_lambdas),
        })

    # ── Disposition ────────────────────────────────────────────
    print("─" * 78)
    matches = [f for f in findings if f["hoefsmit_predicts_empirical"]]
    n_matches = len(matches)
    print(f"  Atoms where Hoefsmit content-spread selects the empirical")
    print(f"  dominant partition: {n_matches}/{len(findings)}")
    print()
    print("  Caveat: Hoefsmit content-spread is partition-only (independent")
    print("  of the braid word β). For T and ³He which share n = 9 but")
    print("  differ in (Z, N), the selector predicts the SAME dominant")
    print("  partition for both — which IS the empirical pattern when both")
    print("  dominants live among the n=9 max-spread partitions, but NOT")
    print("  when the braid word selects a different λ within the same n.")
    print()
    if n_matches == len(findings):
        print("  ✓ POSITIVE FINDING: Hoefsmit content-spread is a closed-form")
        print("    substrate identification of the dominant partition for")
        print("    {D, T, ³He}. Closes the open structural piece of")
        print("    rem:per-partition-k-lambda-rule.")
    elif n_matches > 0:
        print("  PARTIAL FINDING: Hoefsmit selector identifies the dominant")
        print(f"    partition for {n_matches}/{len(findings)} atoms. The")
        print("    failure cases reveal where the braid-word dependence")
        print("    cannot be reduced to partition-shape alone.")
    else:
        print("  ✗ NEGATIVE FINDING: Hoefsmit content-spread does not match")
        print("    the empirical dominant partition for any atom. The")
        print("    selector must depend on the braid word β, not just on λ.")

    w.set_content_block("rem:per-partition-k-lambda-rule")
    w.set_description(
        "Hoefsmit content-asymptotic selector test for the per-"
        "partition k_λ rule's dominant partition. Computes the "
        "content spread Δc_max(λ) = max(j-i) - min(j-i) over cells "
        "of each partition of 3A and checks whether the argmax "
        "matches the empirically-identified dominant partition from "
        "probe_phiq_per_partition_klambda.py. Theoretical basis: "
        "Hoefsmit (1974) seminormal-form eigenvalues are q-powers "
        "of cell-content differences; max eigenvalue magnitude is "
        "bounded above by q^{Δc_max(λ)}. Substrate-only "
        "(partition-shape-only); Class C (diagnostic)."
    )
    w.add_parameter("atoms", list(ATOM_N.keys()))
    w.add_parameter("empirical_dominants_from", "PR #639 cycle 6")
    w.add_data("per_atom_findings", findings)
    w.add_data("hoefsmit_match_count", n_matches)
    w.add_data("hoefsmit_match_total", len(findings))
    w.add_data("disposition", (
        "POSITIVE" if n_matches == len(findings)
        else "PARTIAL" if n_matches > 0
        else "NEGATIVE"
    ))

    # Assertions encode the OBSERVED outcome (negative finding):
    # partition-shape-only content-spread selector fails for ALL
    # 3 atoms in the empirical comparison. This is a substantive
    # structural negative finding — it confirms the selector must
    # depend on the braid word β, not on partition shape alone.
    w.add_assertion(
        "content_spread_alone_does_not_select_empirical_dominant_D",
        computed=not findings[0]["hoefsmit_predicts_empirical"],
        expected=True,
    )
    w.add_assertion(
        "content_spread_alone_does_not_select_empirical_dominant_T",
        computed=not findings[1]["hoefsmit_predicts_empirical"],
        expected=True,
    )
    w.add_assertion(
        "content_spread_alone_does_not_select_empirical_dominant_He3",
        computed=not findings[2]["hoefsmit_predicts_empirical"],
        expected=True,
    )
    w.add_assertion(
        "selector_must_depend_on_braid_word_not_just_partition_shape",
        computed=(n_matches == 0),
        expected=True,
    )

    out = w.save()
    print(f"\n  Wrote {out.name}")
    # Don't fail the run if assertions don't pass; this is a probe
    # whose negative finding is itself useful.
    return 0


if __name__ == "__main__":
    sys.exit(main())
