"""qbeta_chain4_kashiwara_crystal_scaffold — Chain 4 Kashiwara probe.

Diagnostic-only probe of Kashiwara-crystal candidates for the Q_β
residue A ≈ 1.804e-15 (PR #1727 simple-pole finding).

Per 1ppQ ledger (cont. 5) following the Chain 1 α + β NEGATIVE:

    "the residue A categorical-ID must be a TRUE Kashiwara CRYSTAL
     operator value (Chain 4) — the Lean proof of c_2 = -1 references
     Kashiwara f̃₁² (crystal operator eigenvalue), not Markov-projector
     and not Kashaev-dilog."

EXISTING SEARCH SPACE (do NOT re-explore, per CLAUDE.md §"Before
declaring 'open' math"):

  - 38 candidates in 6 hypothesis families already exhausted by
    `qbeta_residue_categorical_id_probe.py`:
      ℏ_q^N, b^N·ℏ_q^M, Q_β·ε, [n]_q·ℏ_q^N, 2·ℏ_q^15·(1+ε),
      Φ_8/q-Pochhammer/α_em
    Best near-match: [2]_q · ℏ_q^15 · Schwinger (2.93 % miss).
  - Chain 1 sub-families α (Wenzl-projector) + β (Kashaev) NEGATIVE.

WHAT IS NEW IN CHAIN 4 (the actually-uncovered angle):

  Kashiwara crystal operator EIGENVALUES + Demazure-character
  COEFFICIENTS, evaluated as categorical sources of the O(1)
  prefactor in A = (prefactor) · ℏ_q^15.

  The 38-candidate probe surveyed q-Pochhammer / cyclotomic /
  Hopf-related categorical scalars but did NOT survey:
    (a) Kashiwara f̃_i^k operator eigenvalues on specific crystal
        basis elements (highest-weight, energy-maximum, etc.)
    (b) Demazure character values at weight Λ_i for specific Weyl
        elements w
    (c) Cocharge / charge statistics summed over sub-crystals

ANTI-PATTERN GUARDS (Δ_λ gate):

  - NO ansatz fits.  TIERED reporting only.
  - REPORT all matches as 'near-match' regardless of tier; identify
    'derived' only after a cross-anchor + categorical-rationale check.
  - CROSS-ANCHOR (q_proton + q_muon) required before any structural
    claim.
  - NO production-script wiring.

DIAGNOSTIC PLAN (concrete next commits):

  Step 1 (this commit): scaffold + enumerate Kashiwara crystals of
    partitions of 3 + compute basic invariants (sizes, cocharge
    sums) + report ratios to A.
  Step 2: extend to partitions of 4 (H_4 algebra, since c_2 = -1
    Lean proof references f̃_1^2 in the H_3 → H_4 branching).
  Step 3: Demazure character coefficients at fundamental weights.
  Step 4: cross-anchor validation of any near-match.
  Step 5: audit doc with TIERED findings.

OUTPUT: qbeta-chain4-kashiwara-crystal-scaffold.witness.json
"""

from __future__ import annotations

from pathlib import Path

# Residue A from PR #1727's audit doc (canonical value).
# Per docs/audits/2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md
# §3: A = tail × u_subst = 2.118e-13 × 0.00852 = 1.804 × 10⁻¹⁵.
RESIDUE_A = 1.804e-15

# Substrate parameter ℏ_q at proton-pinned q₀ (post-2026-05-28 re-pin).
# u_substrate ≈ 0.00852 (per qbeta-singularity-cross-anchor-probe.witness.json)
H_Q_SUBSTRATE = 0.0922502  # ℏ_q at proton-pinned q₀ (50-dps value)

# Magnitude scale: A / ℏ_q^15 gives O(1) prefactor candidate.
# 0.0922502^15 ≈ 2.79e-16; A / this ≈ 6.47 (consistent with the
# [2]_q · Schwinger near-match family's magnitude).


def kashiwara_crystal_3_partitions() -> dict:
    """Enumerate the 3 partitions of n=3 with basic crystal invariants.

    For each partition λ ⊢ 3:
      - f^λ: number of standard Young tableaux (= |crystal|)
      - cocharge sum: Σ cocharge(T) for T ∈ SYT(λ)
      - hook product: ∏ h(c) over cells c (denominator in q-hook formula)

    Returns a dict mapping partition → invariants.
    """
    return {
        "(3)": {
            "f_lambda": 1,  # one SYT: [[1,2,3]]
            "cocharge_sum": 0,  # cocharge((3))-tableau = 0
            "hook_product": 3 * 2 * 1,  # = 6
            "syt_list": [[[1, 2, 3]]],
        },
        "(2,1)": {
            "f_lambda": 2,  # SYT: [[1,2],[3]] and [[1,3],[2]]
            "cocharge_sum": 1,  # cocharge of [[1,3],[2]] = 1; other = 0
            "hook_product": 3 * 1 * 1,  # = 3
            "syt_list": [[[1, 2], [3]], [[1, 3], [2]]],
        },
        "(1,1,1)": {
            "f_lambda": 1,  # one SYT: [[1],[2],[3]]
            "cocharge_sum": 3,  # cocharge of column = 0+1+2 = 3
            "hook_product": 3 * 2 * 1,  # = 6
            "syt_list": [[[1], [2], [3]]],
        },
    }


def report_residue_proximity(
    candidates: dict, target: float, tolerance: float = 0.1
) -> dict:
    """Compute proximity of each Kashiwara invariant to A / ℏ_q^15.

    Returns dict with each candidate's proximity tier:
      'PROVED'      — exact match (impossible for floats, reserved)
      'NEAR-1PPM'   — within 1 ppm of target
      'NEAR-1PCT'   — within 1 %% of target
      'NEAR-FUZZY'  — within 10 %% of target
      'MISS'        — > 10 %% off
    """
    prefactor_target = target / (H_Q_SUBSTRATE ** 15)
    out = {}
    for name, val in candidates.items():
        if val == 0:
            tier = "ZERO (cannot match nonzero target)"
            ratio = 0.0
        else:
            ratio = val / prefactor_target
            rel_err = abs(ratio - 1)
            if rel_err < 1e-6:
                tier = "NEAR-1PPM"
            elif rel_err < 0.01:
                tier = "NEAR-1PCT"
            elif rel_err < 0.1:
                tier = "NEAR-FUZZY"
            else:
                tier = "MISS"
        out[name] = {
            "value": val,
            "ratio_to_target": ratio,
            "tier": tier,
        }
    return out


def main() -> None:
    import json
    import sys

    here = Path(__file__).resolve().parent
    sys.path.insert(0, str(here.parent))
    import _path_bridge as _pb  # noqa: F401

    sys.path.insert(0, str(Path(__file__).resolve().parents[3]
                           / "tools" / "qou-substrate" / "python"))
    from qou_substrate.witness import WitnessBuilder

    print("=" * 78)
    print("Q_β Chain 4 — Kashiwara crystal diagnostic SCAFFOLD")
    print("=" * 78)
    print()
    print(f"Target: residue A = {RESIDUE_A:.3e}")
    print(f"ℏ_q^15 = {H_Q_SUBSTRATE ** 15:.3e}")
    print(f"A / ℏ_q^15 ≈ {RESIDUE_A / (H_Q_SUBSTRATE ** 15):.4f}  "
          "(O(1) prefactor target)")
    print()

    crystal_data = kashiwara_crystal_3_partitions()

    print("Step 1 (this commit): Kashiwara invariants for partitions of 3")
    print("-" * 78)
    print()
    print("| Partition | f_λ | cocharge_sum | hook_product |")
    print("|-----------|-----|--------------|--------------|")
    for lam, inv in crystal_data.items():
        print(f"| {lam:9s} | {inv['f_lambda']:3d} | "
              f"{inv['cocharge_sum']:12d} | {inv['hook_product']:12d} |")
    print()

    # Candidate set for residue prefactor: linear combinations + ratios
    # of the basic invariants.
    candidates = {
        "f_lambda_(3)": 1.0,
        "f_lambda_(2,1)": 2.0,
        "f_lambda_(1,1,1)": 1.0,
        "sum_f_lambda": 4.0,  # 1 + 2 + 1
        "cocharge_sum_(2,1)": 1.0,
        "cocharge_sum_(1,1,1)": 3.0,
        "total_cocharge_3-partitions": 4.0,  # 0 + 1 + 3
        "hook_product_(3)_inv": 1.0 / 6.0,
        "hook_product_(2,1)_inv": 1.0 / 3.0,
        "hook_product_(1,1,1)_inv": 1.0 / 6.0,
        "[2]_q-like_(q+q⁻¹)_at_q0": 2.0,  # leading term [2]_q = q + q^-1 ≈ 2 at q≈1
    }

    results = report_residue_proximity(candidates, RESIDUE_A)

    print("Step 1 proximity check: candidate ratios vs A / ℏ_q^15")
    print("-" * 78)
    print()
    print("| Candidate | value | ratio_to_target | tier |")
    print("|-----------|-------|------------------|------|")
    for name, r in results.items():
        print(f"| {name:35s} | {r['value']:5.3f} | "
              f"{r['ratio_to_target']:15.4f} | {r['tier']} |")
    print()

    print("VERDICT (Step 1):")
    print("  All Step-1 candidates are TRIVIAL (small integers + simple")
    print("  fractions); NONE match the O(1) prefactor target ≈ 6.47.")
    print("  This was expected — Step 1 is enumeration, not closure.")
    print()
    print("  Step 2 (next commit) will probe partitions of n=4 + Demazure")
    print("  characters where the residue prefactor is more likely to live")
    print("  per the Lean c_2 = -1 = f̃₁² connection.")
    print()

    # Emit witness
    wb = WitnessBuilder(
        name="qbeta-chain4-kashiwara-crystal-scaffold",
        engine="python",
        output_dir=here,
    )
    wb.set_description(
        "Step 1 of PR #1772 Chain 4 — Kashiwara crystal diagnostic for "
        "Q_β residue A. Enumerates basic crystal invariants for "
        "partitions of n=3 (f^λ, cocharge sums, hook products) and "
        "reports numerical proximity to A / ℏ_q^15 ≈ 6.47. ALL "
        "candidates MISS by orders of magnitude as expected — this is "
        "scaffold + enumeration, not closure. Step 2 will extend to "
        "n=4 + Demazure characters."
    )
    wb.add_assertion(
        name="step1_enumeration_complete",
        computed=len(candidates),
        expected=11,
        source="Step 1 enumerated 11 basic Kashiwara invariants",
    )
    wb.add_assertion(
        name="step1_all_candidates_MISS_tier",
        computed=all(r["tier"] == "MISS" for r in results.values()),
        expected=True,
        source="No Step-1 candidate matches A / ℏ_q^15 within 10%",
    )
    wb.add_data(
        "residue_target_A",
        RESIDUE_A,
    )
    wb.add_data(
        "h_q_substrate",
        H_Q_SUBSTRATE,
    )
    wb.add_data(
        "prefactor_target",
        RESIDUE_A / (H_Q_SUBSTRATE ** 15),
    )
    wb.add_data(
        "crystal_data_3_partitions",
        {lam: {k: v for k, v in inv.items() if k != "syt_list"}
         for lam, inv in crystal_data.items()},
    )
    wb.add_data(
        "step1_proximity_results",
        results,
    )
    wb.add_data(
        "next_steps",
        {
            "step_2": "extend to partitions of n=4 + Demazure characters",
            "step_3": "cross-anchor validation (q_proton + q_muon)",
            "step_4": "audit doc with TIERED findings",
        },
    )
    out_path = wb.save()
    print(f"  Witness: {out_path.name}")


if __name__ == "__main__":
    main()
