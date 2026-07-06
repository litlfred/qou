"""Does q-Dirac eigenvalue rank predict the empirical Δ_λ-dominant partitions?

Per author 'how can I contribute to 1ppb' direction. Cross-references
my Dirac breakthrough (PR #1287) with sibling thread #1229 (merged
2026-05-25) + #1288 + Option E audit (on main 2026-05-25).

## Hypothesis

The Option E audit proposes:

  Δ_λ(K) = Σ_w n^w_λ · ρ_w(K)

where n^w_λ are KL multiplicities and ρ_w(K) is a canonical-basis
trace at crystal vertex w.

My PR #1287 finding shows q-Dirac eigenvalues D_q²(λ) = [c_λ]_q²
naturally produce structurally-relevant weighted sums (the (1+D_q²)
weighting gives Reading-A's negative h² SIGN at H_4).

**Hypothesis to test:** If q-Dirac eigenvalue rank predicts which
λ are empirically Δ_λ-dominant per atom-knot K, then D_q² is a
natural starting point for the Option E ρ_w(K) construction.

## Empirical data (from main / merged PRs)

Per Option E audit + PR #1229 (merged 2026-05-25) + PR #1288:

| atom | A | H_n  | empirical dominant λ*(K)  | shape          |
|------|---|------|---------------------------|----------------|
| D    | 2 | H_6  | (2,1,1,1,1)               | hook           |
| T    | 3 | H_9  | (2,2,2,1,1,1)             | ~staircase     |
| ³He  | 3 | H_9  | (2,2,2,1,1,1)             | (same as T)    |
| ⁴He  | 4 | H_12 | (9,3) (also (4,4,4) — PR #1288) | two-row + cube |

## Method

For each (atom, H_n) pair:
1. Enumerate all p(n) partitions
2. Compute D_q²(λ) at q_0 (mp.mpf 50 dps)
3. Rank partitions by D_q²(λ)
4. Identify position of empirical dominant λ*(K) in the D_q² ranking

If empirical λ*(K) is at or near rank 1 (top D_q²), Dirac eigenvalue
predicts the Δ_λ dominant. If it's far down the ranking (e.g. rank
20+), Dirac doesn't predict.

## What this PR does NOT do

- Does NOT prove Option E formula
- Does NOT compute Δ_λ values directly
- Does NOT close Δ_λ closure problem
- Provides cross-check data for the Option E ρ_w investigation

## Cross-references

- PR #1287 (Dirac breakthrough; this branch)
- PR #1288 (Wedderburn dominant-partition + Type-B folding)
- PR #1229 (merged 2026-05-25) — Probes 1/3/4 mapping the Δ_λ
  landscape per atom
- audit 2026-05-25 Option E crystal-weight Δ_λ closure
- chirality-residue-mass-term.md (q-Dirac operator definition)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


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


def content_sum(p):
    return sum(j - i for i, row in enumerate(p) for j in range(row))


def q_br(k, q):
    if k == 0:
        return mp.mpf(0)
    return (q ** k - q ** (-k)) / (q - 1 / q)


def D_q2(p, q):
    return q_br(content_sum(p), q) ** 2


def classical_dim(p):
    n = sum(p)
    rows = len(p)
    cols = p[0] if rows else 0
    col_h = [sum(1 for r in p if r > j) for j in range(cols)]
    from math import factorial
    pr = 1
    for i, rl in enumerate(p):
        for j in range(rl):
            arm = rl - 1 - j
            leg = col_h[j] - 1 - i
            pr *= (arm + leg + 1)
    return factorial(n) // pr


def main():
    set_compute_dps(50)
    w = WitnessBuilder(
        "q-dirac-vs-empirical-dominant-lambda-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md",
    )
    w.set_description(
        "Tests whether q-Dirac eigenvalue D_q²(λ) = [c_λ]_q² predicts "
        "the empirically Δ_λ-dominant partition λ*(K) per atom K from "
        "PR #1229 / #1288 / Option E audit (Δ_λ closure). "
        "Single-session structural input to Option E's ρ_w(K) "
        "investigation."
    )

    print("=" * 78)
    print("q-Dirac eigenvalue rank vs empirical Δ_λ-dominant partitions")
    print("=" * 78)

    q = mp.mpf(Q_50_DIGIT_STR)

    # Empirical data per Option E audit / PR #1229 / PR #1288
    empirical = {
        "D":   {"A": 2, "n": 6,  "dominant": (2, 1, 1, 1, 1)},
        "T":   {"A": 3, "n": 9,  "dominant": (2, 2, 2, 1, 1, 1)},
        "3He": {"A": 3, "n": 9,  "dominant": (2, 2, 2, 1, 1, 1)},
        "4He_91229": {"A": 4, "n": 12, "dominant": (9, 3)},
        "4He_1288":  {"A": 4, "n": 12, "dominant": (4, 4, 4)},
    }

    results = {}

    for atom_key, info in empirical.items():
        n = info["n"]
        dom = info["dominant"]
        parts = partitions_of(n)
        # Compute D_q²(λ) for each partition
        ranked = sorted(
            [(p, content_sum(p), D_q2(p, q), classical_dim(p)) for p in parts],
            key=lambda t: -t[2],  # descending D_q²
        )
        # Find position of dominant
        dom_position = None
        for i, (p, c, dq2, dcl) in enumerate(ranked):
            if p == dom:
                dom_position = i + 1  # 1-indexed
                dom_c = c
                dom_dq2 = dq2
                break

        n_parts = len(parts)
        results[atom_key] = {
            "n": n,
            "dominant": dom,
            "dominant_c_lambda": dom_c if dom_position else None,
            "dominant_D_q2": mp.nstr(dom_dq2, 12) if dom_position else None,
            "dominant_rank_by_D_q2": dom_position,
            "n_partitions": n_parts,
            "top3_D_q2": [
                {"partition": str(p), "c": c, "D_q2": mp.nstr(dq2, 12), "d_classical": dcl}
                for p, c, dq2, dcl in ranked[:3]
            ],
        }

        print(f"\n--- {atom_key} (A={info['A']}, H_{n}) ---")
        print(f"  empirical dominant λ*: {dom}")
        print(f"  c_lambda = {dom_c}")
        print(f"  D_q²(λ*) at q_0 = {mp.nstr(dom_dq2, 10)}")
        print(f"  rank by D_q² = {dom_position}/{n_parts}")
        print(f"  top 3 by D_q²:")
        for i, t in enumerate(ranked[:3]):
            p, c, dq2, dcl = t
            print(f"    #{i+1}: λ={p}, c={c}, D_q²={mp.nstr(dq2, 10)}, d_λ={dcl}")

    # === Summary ===
    print("\n" + "=" * 78)
    print("Summary: does D_q² rank predict empirical Δ_λ dominance?")
    print("=" * 78)

    print(f"\n  {'atom':<10}{'n':<4}{'dominant':<22}{'c_λ':<6}{'rank/total':<14}{'top-rank match?':<18}")
    for k, r in results.items():
        match = "✓ rank 1" if r["dominant_rank_by_D_q2"] == 1 else (
                f"top-5" if r["dominant_rank_by_D_q2"] <= 5 else f"rank {r['dominant_rank_by_D_q2']}")
        rank_total = f"{r['dominant_rank_by_D_q2']}/{r['n_partitions']}"
        print(f"  {k:<10}{r['n']:<4}{str(r['dominant'])[:20]:<22}{str(r['dominant_c_lambda']):<6}{rank_total:<14}{match:<18}")

    # Verdict
    top1_matches = sum(1 for r in results.values() if r["dominant_rank_by_D_q2"] == 1)
    top5_matches = sum(1 for r in results.values() if r["dominant_rank_by_D_q2"] <= 5)
    n_total = len(results)
    print(f"\n  Top-rank matches: {top1_matches}/{n_total}")
    print(f"  Top-5 matches:    {top5_matches}/{n_total}")

    if top1_matches == n_total:
        verdict = (
            "STRONG MATCH: D_q² rank predicts empirical Δ_λ dominance "
            "in all tested atoms. Strong candidate for Option E's ρ_w(K) "
            "construction."
        )
    elif top5_matches == n_total:
        verdict = (
            "PARTIAL: D_q² ranks dominant partitions in top-5. Worth "
            "investigation — possibly some other selection criterion "
            "(crystal-vertex-distance, KL polynomial degree) acts within "
            "the top-5 D_q² candidates."
        )
    else:
        verdict = (
            f"NEGATIVE: D_q² rank does NOT predict empirical Δ_λ dominance. "
            f"Only {top5_matches}/{n_total} are in top-5 by D_q². The "
            f"Δ_λ-dominance criterion is structurally distinct from Dirac "
            f"eigenvalue magnitude. Option E's ρ_w(K) needs a different "
            f"selection mechanism."
        )

    print(f"\n  VERDICT: {verdict}")

    w.add_parameter("q_0_50dps", Q_50_DIGIT_STR)
    w.add_data("per_atom", results)
    w.add_data("top1_matches", top1_matches)
    w.add_data("top5_matches", top5_matches)
    w.add_data("n_atoms_tested", n_total)
    w.add_data("verdict", verdict)
    w.add_data("implication_for_option_E", (
        "If D_q² rank does NOT match empirical dominant λ*(K), Option E's "
        "ρ_w(K) construction needs a selection mechanism beyond Dirac "
        "eigenvalues. The Type-B folding bar-symmetry (AGENTS.md §7b, "
        "PR #1288's transpose-pair theorems on main) may be the right "
        "structural input, since dominant pairs include both λ* and λ*^T "
        "(e.g. ⁴He: (4,4,4) ↔ (3,3,3,3))."
    ))

    w.add_assertion(
        name="probe_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source="Cross-check of D_q² ranking vs empirical Δ_λ dominance.",
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
