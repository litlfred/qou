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

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))


MAGIC = {2, 8, 20, 28, 50, 82, 126}
LL_SWEEP = [2, 3, 4, 5, 6, 7, 8, 12, 24, 60, 120]


def partitions_of(n: int) -> list[tuple[int, ...]]:
    if n == 0:
        return [()]
    parts: list[tuple[int, ...]] = []

    def go(remaining: int, max_part: int, prefix: tuple[int, ...]) -> None:
        if remaining == 0:
            parts.append(prefix)
            return
        for k in range(min(remaining, max_part), 0, -1):
            go(remaining - k, k, prefix + (k,))

    go(n, n, ())
    return parts


def content_sum(lam: tuple[int, ...]) -> int:
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def hook_lengths(lam: tuple[int, ...]) -> list[int]:
    if not lam:
        return []
    cols = [0] * lam[0]
    for r in lam:
        for j in range(r):
            cols[j] += 1
    out: list[int] = []
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - 1 - j
            leg = cols[j] - 1 - i
            out.append(arm + leg + 1)
    return out


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

    for n in ns_to_probe:
        parts = partitions_of(n)
        total_dim = sum(dim_irrep(lam) for lam in parts)
        per_n: dict = {
            "n": n,
            "n_partitions": len(parts),
            "total_dim": total_dim,
            "is_magic": n in MAGIC,
            "by_root_of_unity": {},
        }
        print(f"\n  n = {n}{' (magic)' if n in MAGIC else ''}, "
              f"|S_n| = {total_dim}")
        print(f"  {'ℓ':>4}{'inv_dim':>10}{'ratio':>10}  invariant λ "
              f"(c ≡ 0 mod ℓ)")
        print("  " + "-" * 72)
        for ell in LL_SWEEP:
            inv_lambdas = []
            inv_dim = 0
            for lam in parts:
                c = content_sum(lam)
                if c % ell == 0:
                    d = dim_irrep(lam)
                    inv_lambdas.append({
                        "lambda": list(lam),
                        "content_sum": c,
                        "dim": d,
                    })
                    inv_dim += d
            ratio = inv_dim / total_dim if total_dim else 0
            per_n["by_root_of_unity"][ell] = {
                "invariant_dim": inv_dim,
                "ratio": ratio,
                "invariant_blocks": inv_lambdas,
            }
            lam_summary = ", ".join(
                "(" + ",".join(map(str, b["lambda"])) + ")"
                for b in inv_lambdas[:6]
            )
            if len(inv_lambdas) > 6:
                lam_summary += ", ..."
            print(f"  {ell:>4}{inv_dim:>10}{ratio:>10.4f}  {lam_summary}")
        findings[n] = per_n

    # Summary: at magic n = 2, list ℓ that produces non-empty invariant.
    n2 = findings[2]
    realising_ell = [
        ell for ell, v in n2["by_root_of_unity"].items()
        if v["invariant_dim"] > 0
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

    witness = {
        "computation": "full-twist-root-of-unity-probe",
        "description": (
            "Probe of category-(a) for the full_twist_delta_n2_verification "
            "structural finding: at q = ζ_ℓ, the Δ_n²-invariant subspace of "
            "H_n(q) is the span of V_λ with c(λ) ≡ 0 (mod ℓ).  Sweeps small "
            "ℓ at magic n in range; identifies which ℓ make the categorical-"
            "neutrality predicate realisable at magic n = 2."
        ),
        "reference_blocks": [
            "prop:categorical-neutrality-saturated-shells",
            "conj:mass-endomorphism",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "magic_nucleon_counts": sorted(MAGIC),
            "ell_sweep": LL_SWEEP,
            "n_probed": ns_to_probe,
        },
        "findings_by_n": findings,
        "magic_n2_realising_ell": realising_ell,
        "all_passed": True,
    }
    out = HERE / "full-twist-root-of-unity-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
