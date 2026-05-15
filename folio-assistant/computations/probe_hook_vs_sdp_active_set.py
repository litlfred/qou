#!/usr/bin/env python3
# polynomial_q_not_applicable: structural cross-reference probe
"""Probe: relationship between Path A u-pole hook λ_⋆(Z, N) and the
SDP / Φ_q operator-binding dominant partition.

Three distinct empirical "dominant partition" notions surface
across the codebase:

  1. **Path A u-pole maximizer** (this PR's audit-doc finding,
     from `per-irrep-pole-atom-crystal.witness.json`):
         λ_⋆(Z, N) = (Z + 2N + 1, 1^{2Z + N - 1})
     — the partition with maximum |ord_{u=0}(y_λ · χ^λ)| in tr_M.

  2. **PR #639 operator-Φ_q failure dominant** (from
     `per-partition-k-lambda-rule.md`): the partition where the
     operator-valued Φ_q probe's deviation from AME is largest at
     uniform truncation depth k.

  3. **SDP shadow-price argmax** (from
     `probe-sdp-active-set-dominant-partition.witness.json`): the
     LP-dual maximizer in the operator-selection LP.

This probe tests the hypothesis:

  **PR #639 dominant = lump_column(Path-A hook)**

i.e., the operator-Φ_q failure-dominant partition is obtained from
the Path A hook by replacing the column 1^{d-1} with a single row
of length d-1 — turning hook (w, 1^{d-1}) into 2-row [w, d-1].

If the hypothesis holds, it would identify the knot convolution
operator's "binding partition" as a structural FUNCTION of the
Markov-trace pole-maximizer hook — not an independent empirical
finding.

`auditOnly`: docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md

Witness: `hook-vs-sdp-active-set-probe.witness.json`

@module folio-assistant/computations/probe_hook_vs_sdp_active_set
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402


def lump_column(hook):
    """Collapse hook (w, 1^{d-1}) → 2-row [w, d - 1].

    Returns the lumped partition, or the original if not a hook.
    """
    if len(hook) == 0:
        return hook
    w = hook[0]
    rest = hook[1:]
    if all(c == 1 for c in rest):
        # It's a hook.
        col_count = len(rest)
        if col_count == 0:
            return hook
        return [w, col_count]
    return list(hook)


# PR #639 dominant partitions (from per-partition-k-lambda-rule.md table)
PR_639_DOMINANT = {
    (1, 1): [2, 2, 1, 1],
    (1, 2): [6, 3],
    (2, 1): [5, 4],
}


def main() -> int:
    cpa = json.loads(
        (HERE / "per-irrep-pole-atom-crystal.witness.json").read_text()
    )
    sdp = json.loads(
        (HERE / "probe-sdp-active-set-dominant-partition.witness.json").read_text()
    )

    # Index SDP findings by atom label.
    sdp_by_atom = {}
    for r in sdp["data"]["per_atom_findings"]:
        sdp_by_atom[r["atom"]] = r

    atom_keys = {(1, 1): "D", (1, 2): "T", (2, 1): "He3"}

    results = []
    for a in cpa["data"]["atoms"]:
        Z, N = a["Z"], a["N"]
        if (Z, N) not in PR_639_DOMINANT:
            continue
        hook = a["min_total_lambda"]
        lumped = lump_column(hook)
        pr_639 = PR_639_DOMINANT[(Z, N)]
        sdp_arg = sdp_by_atom.get(atom_keys[(Z, N)], {}).get(
            "argmax_y_star_partition"
        )

        results.append({
            "atom": a["atom"],
            "Z": Z, "N": N, "A": Z + N,
            "path_a_hook": hook,
            "hook_lumped_column": lumped,
            "pr_639_operator_phi_q_dominant": pr_639,
            "sdp_shadow_price_argmax": sdp_arg,
            "lumped_eq_pr_639": lumped == pr_639,
            "lumped_eq_sdp": lumped == sdp_arg,
            "pr_639_eq_sdp": pr_639 == sdp_arg,
        })

    builder = (
        WitnessBuilder("hook-vs-sdp-active-set-probe", engine="python")
        .set_description(
            "Cross-references three distinct 'dominant partition' "
            "notions across the codebase: (1) Path A u-pole hook "
            "λ_⋆(Z, N) = (Z+2N+1, 1^{2Z+N-1}); (2) PR #639 "
            "operator-valued Φ_q failure-dominant (per "
            "per-partition-k-lambda-rule.md); (3) SDP shadow-price "
            "argmax (per probe-sdp-active-set-dominant-partition).  "
            "Tests the hypothesis: PR #639 dominant = "
            "lump_column(Path-A hook), i.e., the operator-binding "
            "partition is a structural function of the Markov-trace "
            "pole-maximizer hook."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md"
        )
        .add_data("results", results)
    )

    # Print summary table.
    print("=" * 100)
    print("  Three dominant-partition notions vs each other")
    print("=" * 100)
    print()
    print(f"  {'atom':<6}{'(Z,N)':<8}{'Path A hook':<22}"
          f"{'lump_column(hook)':<22}{'PR #639':<14}{'SDP argmax':<14}"
          f"{'lumped=PR#639?':>16}")
    print("  " + "-" * 102)
    for r in results:
        zn = f"({r['Z']},{r['N']})"
        print(f"  {r['atom']:<6}{zn:<8}{str(r['path_a_hook']):<22}"
              f"{str(r['hook_lumped_column']):<22}"
              f"{str(r['pr_639_operator_phi_q_dominant']):<14}"
              f"{str(r['sdp_shadow_price_argmax']):<14}"
              f"{('✓' if r['lumped_eq_pr_639'] else '✗'):>16}")
    print()

    # Verdict
    lumped_pr_639 = sum(1 for r in results if r["lumped_eq_pr_639"])
    pr_639_sdp = sum(1 for r in results if r["pr_639_eq_sdp"])
    print(f"  PR #639 dominant = lump_column(hook): "
          f"{lumped_pr_639}/{len(results)} atoms")
    print(f"  PR #639 dominant = SDP shadow-price argmax: "
          f"{pr_639_sdp}/{len(results)} atoms")
    print()

    builder.add_data(
        "verdict",
        {
            "atoms_total": len(results),
            "lump_column_hypothesis_matches_pr_639": lumped_pr_639,
            "pr_639_matches_sdp_shadow_argmax": pr_639_sdp,
            "interpretation": (
                "The Path A hook λ_⋆(Z,N) is the u-pole maximizer "
                "of tr_M — a property of the Markov trace's "
                "leading singularity at q → 0.  Empirically the "
                "lump_column(hook) operation reproduces PR #639's "
                "operator-Φ_q failure-dominant partition at T and "
                "³He but NOT D, suggesting the relationship is "
                "structural for A = 3 atoms (n = 9 strands) but "
                "fails for the A = 2 deuteron.  The SDP "
                "shadow-price argmax is a separate optimisation "
                "(LP duality on the operator-selection problem) "
                "and does not in general match either."
            ),
        },
    )

    builder.add_assertion(
        name="lump_column_matches_pr_639_for_A_eq_3_atoms",
        computed=int(
            results[1]["lumped_eq_pr_639"] and results[2]["lumped_eq_pr_639"]
        ),
        expected=1,
    )

    out = builder.save()
    print(f"  Witness emitted: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
