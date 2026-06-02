#!/usr/bin/env python3
"""
Probe (a) for full_twist_delta_n2_verification's structural finding
at magic n=2: empirically check whether the categorical-neutrality
predicate becomes realisable when q is specialised to a root of
unity.

At generic q, the Δ_n²-invariant subspace of H_n(q) is the span of
V_λ with c(λ) = 0.  At q = ζ_ℓ (primitive ℓ-th root of unity), the
condition q^c(λ) = 1 becomes c(λ) ≡ 0 (mod ℓ), so additional blocks
become invariant.

This probe sweeps ℓ ∈ {2, 3, 4, 5, 6, 7, 8, 12, 24, 60, 120} (the
small ℓ that arise in Habiro-style root-of-unity expansions, plus
the orders of S_n centers for small n) and reports, at each magic
n in range and each ℓ:

  - The set of λ ⊢ n with c(λ) ≡ 0 (mod ℓ).
  - The dimension of the resulting invariant subspace.
  - Whether the predicate becomes realisable (invariant_dim > 0).

Output: full-twist-root-of-unity-probe.witness.json
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

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))


MAGIC = {2, 8, 20, 28, 50, 82, 126}
LL_SWEEP = [2, 3, 4, 5, 6, 7, 8, 12, 24, 60, 120]


# Partition + hook-length utilities — shared with schur_weyl_symbolic
# (centralised per Gemini PR #548 medium-pri).
from schur_weyl_symbolic import partitions_of, hook_lengths  # noqa: E402


def content_sum(lam: tuple[int, ...]) -> int:
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def dim_irrep(lam: tuple[int, ...]) -> int:
    n = sum(lam)
    if n == 0:
        return 1
    from math import factorial
    fact_n = factorial(n)
    prod = 1
    for h in hook_lengths(lam):
        prod *= h
    return fact_n // prod


def main() -> int:
    print("=" * 96)
    print("  Full-twist Δ_n² invariance under q ↦ ζ_ℓ (root-of-unity probe)")
    print("  Per (a) of full_twist_delta_n2_verification's structural finding.")
    print("=" * 96)

    ns_to_probe = sorted({2, 8} | {n for n in MAGIC if n <= 12})
    findings: dict = {}

    from math import factorial
    for n in ns_to_probe:
        parts = partitions_of(n)
        # |S_n| = n! = Σ dim(V_λ)² (regular-rep dim).  Σ dim(V_λ) is
        # a separate, smaller quantity.  Per Copilot PR #548 — both
        # are reported so callers don't conflate.
        sum_dim_irrep = sum(dim_irrep(lam) for lam in parts)
        per_n: dict = {
            "n": n,
            "n_partitions": len(parts),
            "Sn_order_factorial": factorial(n),  # = n! = Σ dim(V_λ)²
            "sum_dim_irrep": sum_dim_irrep,      # = Σ dim(V_λ)
            "is_magic": n in MAGIC,
            "by_root_of_unity": {},
        }
        print(f"\n  n = {n}{' (magic)' if n in MAGIC else ''}, "
              f"|S_n| = n! = {per_n['Sn_order_factorial']}, "
              f"Σ dim(V_λ) = {sum_dim_irrep}")
        print(f"  {'ℓ':>4}{'inv Σ dim²':>14}{'ratio (S_n)':>14}  invariant λ "
              f"(c ≡ 0 mod ℓ)")
        print("  " + "-" * 78)
        for ell in LL_SWEEP:
            inv_lambdas = []
            inv_sum_dim = 0
            inv_sum_dim_sq = 0
            for lam in parts:
                c = content_sum(lam)
                if c % ell == 0:
                    d = dim_irrep(lam)
                    inv_lambdas.append({
                        "lambda": list(lam),
                        "content_sum": c,
                        "dim": d,
                    })
                    inv_sum_dim += d
                    inv_sum_dim_sq += d * d
            # Ratio of |S_n|: invariant fraction of the regular rep.
            ratio_Sn = (inv_sum_dim_sq / per_n["Sn_order_factorial"]
                        if per_n["Sn_order_factorial"] else 0)
            per_n["by_root_of_unity"][ell] = {
                "invariant_sum_dim": inv_sum_dim,
                "invariant_sum_dim_sq": inv_sum_dim_sq,
                "ratio_in_Sn": ratio_Sn,
                "invariant_blocks": inv_lambdas,
            }
            lam_summary = ", ".join(
                "(" + ",".join(map(str, b["lambda"])) + ")"
                for b in inv_lambdas[:6]
            )
            if len(inv_lambdas) > 6:
                lam_summary += ", ..."
            print(f"  {ell:>4}{inv_sum_dim_sq:>14}{ratio_Sn:>14.4f}  "
                  f"{lam_summary}")
        findings[n] = per_n

    # Summary: at magic n = 2, list ℓ that produces non-empty invariant.
    n2 = findings[2]
    realising_ell = [
        ell for ell, v in n2["by_root_of_unity"].items()
        if v["invariant_sum_dim_sq"] > 0
    ]
    print(f"\n  Magic n = 2 realising ℓ (invariant_dim > 0): {realising_ell}")
    if realising_ell:
        print(f"    The categorical-neutrality predicate at magic n = 2")
        print(f"    becomes realisable at q = ζ_ℓ for ℓ ∈ "
              f"{realising_ell}.")
    else:
        print(f"    No ℓ in the swept range realises the predicate at n = 2.")
        print(f"    Investigation paths (b) sum-cancellation or (c) non-")
        print(f"    scalar action remain open.")

    # Emit via WitnessBuilder (canonical schema).  Per Copilot PR #548.
    from witness_base import WitnessBuilder
    w = (WitnessBuilder("full-twist-root-of-unity-probe", engine="python")
         .set_description(
            "Probe of category-(a) for the full_twist_delta_n2_verification "
            "structural finding: at q = ζ_ℓ, the Δ_n²-invariant subspace of "
            "H_n(q) is the span of V_λ with c(λ) ≡ 0 (mod ℓ).  Sweeps small "
            "ℓ at magic n in range; identifies which ℓ make the categorical-"
            "neutrality predicate realisable at magic n = 2."
         )
         .set_content_block("conj:categorical-neutrality-saturated-shells"))
    w.parameters.update({
        "magic_nucleon_counts": sorted(MAGIC),
        "ell_sweep": LL_SWEEP,
        "n_probed": ns_to_probe,
    })
    w.add_data("reference_blocks", [
        "conj:categorical-neutrality-saturated-shells",
        "conj:mass-endomorphism",
    ])
    w.add_data("findings_by_n", findings)
    w.add_data("magic_n2_realising_ell", realising_ell)
    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
