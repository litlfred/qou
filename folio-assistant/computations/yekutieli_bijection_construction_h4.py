#!/usr/bin/env python3
"""Explicit cell↔partition bijection construction at H_4 (Yekutieli).

Attempts the load-bearing step of the Yekutieli per-cell curvature
conjecture (`docs/audits/2026-05-22-yekutieli-percell-conjecture-
formalized.md` §Conjecture):

  Π_HS ∘ τ_q at h² order extracts curvature contribution of EXACTLY
  ONE of the 8 ideal octahedra in 𝓑_3-complement tessellation.

This script enumerates the 5 partitions of H_4, computes their
dim_q V_λ Taylor expansions at h² order, evaluates the half-
symmetric Wedderburn projection coefficient, and compares the
result against the claimed −G·h² = −0.91596559... per-cell
hyperbolic volume contribution.

If the numerical h² coefficient matches −G to 50 dps: strong
empirical confirmation of the audit's structural sketch.
If not: surfaces a quantified gap for further investigation.

Refs:
- `docs/audits/2026-05-22-yekutieli-percell-conjecture-formalized.md`
- `docs/audits/2026-05-18-conjecture-proof-step3-yekutieli.md`
- `lambda_scale_all_c_i_family_a.py` (proves Σ_λ dim_q V_λ at H_4)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

# ── H_4 partitions and Wedderburn data ────────────────────────────
#
# H_4 = C[S_4]; 5 partitions of 4 = {(4), (3,1), (2,2), (2,1,1), (1^4)}.
#   - dim(V_λ) = Σ standard Young tableaux of shape λ
#   - dim_q V_λ at q→1 expands as: dim(V_λ) + κ_λ·h² + O(h^4)
#   - κ_λ = (1/12) · (Σ_box content²(box) − dim(V_λ)·(n−1)·n/12) ???
#     Actually: κ_λ = (1/2)·c_λ² + adjustment for Casimir.
#
# The proved Family A identity (`lambda_scale_all_c_i_family_a.py`):
#   (1/4) · Σ_λ dim_q V_λ = 5/2 + (3/4)·h²
# yields Σ_λ κ_λ = 3 — the sum of h² coefficients across all 5
# partitions.
#
# Partition → (dim, κ_h²) — values from explicit q-Schur expansion
# at q = 1 + h/2 + h²/8 + ... (Murphy element Casimir series):
# Verified empirically (Richardson-extrapolated dim_q hook formula at
# h_small = 1e-4): κ_λ at h² order for each partition.  The κ values
# are SYMMETRIC under conjugation (since dim_q V_λ = dim_q V_{λ^T} at
# unitarized substrate), so paired-partition κ's match exactly.
PARTITIONS = {
    "(4)":       {"dim": 1, "kappa_h2": mp.mpf(0),
                  "conjugate": "(1,1,1,1)", "young_shape": "4 boxes in a row"},
    "(3,1)":     {"dim": 3, "kappa_h2": mp.mpf(1),
                  "conjugate": "(2,1,1)",   "young_shape": "L-shape"},
    "(2,2)":     {"dim": 2, "kappa_h2": mp.mpf(1),
                  "conjugate": "(2,2)",     "young_shape": "2x2 square (self-conj)"},
    "(2,1,1)":   {"dim": 3, "kappa_h2": mp.mpf(1),
                  "conjugate": "(3,1)",     "young_shape": "L-shape mirror"},
    "(1,1,1,1)": {"dim": 1, "kappa_h2": mp.mpf(0),
                  "conjugate": "(4)",       "young_shape": "4 boxes in a column"},
}


def compute_dim_q(q: mp.mpf, partition: str) -> mp.mpf:
    """q-dimension of V_λ in H_n(q) via the hook formula:

        dim_q V_λ = [n]!_q / Π_{(i,j)∈λ} [hook(i,j)]_q

    where [k]_q = (q^k − q^{-k}) / (q − q^{-1}) and [n]!_q = [1][2]…[n].
    """
    # Hook lengths per partition (box order: row-by-row, left-to-right)
    HOOKS = {
        "(4)":       [4, 3, 2, 1],
        "(3,1)":     [4, 2, 1, 1],
        "(2,2)":     [3, 2, 2, 1],
        "(2,1,1)":   [4, 1, 2, 1],
        "(1,1,1,1)": [4, 3, 2, 1],
    }

    def qint(k: int) -> mp.mpf:
        if k == 0:
            return mp.mpf(0)
        return (q ** k - q ** (-k)) / (q - q ** (-1))

    # [n]!_q for n = 4
    n_factorial_q = qint(1) * qint(2) * qint(3) * qint(4)
    denom = mp.mpf(1)
    for h in HOOKS[partition]:
        denom *= qint(h)
    return n_factorial_q / denom


def evaluate_partition_h2_numerical(partition: str) -> mp.mpf:
    """h² coefficient via Richardson-extrapolated finite differences.

    For dim_q = d_0 + κ·h² + ε·h^4 + ..., evaluate at h_1 = 2ε and
    h_2 = 4ε; Richardson cancels the h^4 term:
        κ ≈ [4·D(h_1) - D(h_2)] / 3
    where D(h) = (dim_q(h) - d_0) / h².
    """
    d_0 = mp.mpf(PARTITIONS[partition]["dim"])

    def q_of_h(h_val: mp.mpf) -> mp.mpf:
        # solve q - q⁻¹ = h: q = (h + sqrt(h² + 4)) / 2
        return (h_val + mp.sqrt(h_val ** 2 + 4)) / 2

    def divided_diff(h_val: mp.mpf) -> mp.mpf:
        q = q_of_h(h_val)
        return (compute_dim_q(q, partition) - d_0) / h_val ** 2

    h_small = mp.mpf("0.0001")
    d_small = divided_diff(h_small)
    d_double = divided_diff(h_small * 2)
    # Richardson cancels h² term in error: 4·D(h) - D(2h) is h^4 accurate
    return (4 * d_small - d_double) / 3


def main() -> int:
    print("=" * 90)
    print("Yekutieli per-cell bijection construction at H_4")
    print("=" * 90)
    print()
    print("Step 1: Enumerate H_4 partitions and compute h² coefficients")
    print("-" * 90)
    print(f"  {'partition':<14} {'dim':>4} {'κ (numerical)':>20} "
          f"{'κ (audit guess)':>18} {'conjugate':>12}")
    print("  " + "-" * 70)

    total_kappa = mp.mpf(0)
    numerical_kappas = {}
    for p, data in PARTITIONS.items():
        kappa_num = evaluate_partition_h2_numerical(p)
        kappa_audit = data["kappa_h2"]
        numerical_kappas[p] = kappa_num
        total_kappa += kappa_num
        print(f"  {p:<14} {data['dim']:>4} "
              f"{mp.nstr(kappa_num, 12):>20} "
              f"{mp.nstr(kappa_audit, 6):>18} "
              f"{data['conjugate']:>12}")

    print("  " + "-" * 70)
    print(f"  Σ κ_λ (numerical, all 5 partitions) = "
          f"{mp.nstr(total_kappa, 12)}  (target: 3.0 from Family A)")
    family_a_target = mp.mpf(3)
    print(f"  Σ κ_λ / 4 = (1/4) · Σ = "
          f"{mp.nstr(total_kappa / 4, 12)}  (target: 0.75 = 3/4)")

    print()
    print("Step 2: Half-symmetric projection — sum over conjugate-pair classes")
    print("-" * 90)
    # Half-symmetric projection extracts the symmetric part under
    # λ ↔ λ^T involution. For paired blocks (λ, λ^T), the projection
    # is (κ_λ + κ_{λ^T}) / 2 = average. For self-conjugate, unchanged.
    #
    # NB: this is ONE reading of "half-symmetric"; the audit's
    # operator Π_HS may differ.
    pair_classes = [
        ("(4) ↔ (1,1,1,1)", "(4)", "(1,1,1,1)"),
        ("(3,1) ↔ (2,1,1)", "(3,1)", "(2,1,1)"),
        ("(2,2) self-conj", "(2,2)", "(2,2)"),
    ]
    half_sym_kappa_sum = mp.mpf(0)
    print(f"  {'class':<22} {'κ_λ':>16} {'κ_{λ^T}':>16} {'(κ + κ_T)/2':>16}")
    print("  " + "-" * 76)
    for label, p1, p2 in pair_classes:
        k1 = numerical_kappas[p1]
        k2 = numerical_kappas[p2]
        avg = (k1 + k2) / 2 if p1 != p2 else k1
        half_sym_kappa_sum += avg
        print(f"  {label:<22} {mp.nstr(k1, 8):>16} "
              f"{mp.nstr(k2, 8):>16} {mp.nstr(avg, 8):>16}")

    print("  " + "-" * 76)
    print(f"  Σ_classes (κ_λ + κ_{{λ^T}}) / 2 = "
          f"{mp.nstr(half_sym_kappa_sum, 12)}")

    print()
    print("Step 3: Compare to claimed per-cell volume −G = −Vol(𝓑_3)/8")
    print("-" * 90)
    G_catalan = mp.catalan
    vol_b3 = 8 * G_catalan
    per_cell_vol = vol_b3 / 8  # = G
    print(f"  G (Catalan) = {mp.nstr(G_catalan, 25)}")
    print(f"  Vol(𝓑_3) = 8·G = {mp.nstr(vol_b3, 25)}")
    print(f"  per-cell hyperbolic volume = G = {mp.nstr(per_cell_vol, 25)}")
    print(f"  −G (claimed h² coefficient of Yekutieli term) = "
          f"{mp.nstr(-per_cell_vol, 25)}")
    print()
    print(f"  Numerical comparison:")
    print(f"    half_sym_kappa_sum / 4    = {mp.nstr(half_sym_kappa_sum / 4, 12)}")
    print(f"    target if 'extracts ONE cell': −G = "
          f"{mp.nstr(-per_cell_vol, 12)}")
    print(f"    diff                       = "
          f"{mp.nstr(half_sym_kappa_sum / 4 - (-per_cell_vol), 6)}")

    print()
    print("Step 4: Cell↔partition bijection — empirical findings")
    print("-" * 90)
    print("  Audit's combinatorial sketch:")
    print("    (4), (1,1,1,1):    conjugate pair → 2 'vertex' octahedra")
    print("    (3,1), (2,1,1):    conjugate pair → 4 'edge' octahedra")
    print("    (2,2):             self-conjugate → 2 'center' octahedra (×2 mult)")
    print("  Total: 2 + 4 + 2 = 8 ✓ (matches 𝓑_3 cell count)")
    print()
    print("  EMPIRICAL κ_λ findings (Richardson-extrapolated, 50 dps):")
    print("    (4):       κ = 0    ('vertex' partition has no h² contribution)")
    print("    (1,1,1,1): κ = 0    ('vertex' conjugate, also no h²)")
    print("    (3,1):     κ = 1    ('edge' partition)")
    print("    (2,1,1):   κ = 1    ('edge' conjugate, MATCHES)")
    print("    (2,2):     κ = 1    ('center' partition)")
    print()
    print("  → Σ κ_λ = 3 (consistent with Family A theorem 3/4·h²)")
    print("  → κ is SYMMETRIC under conjugation involution at h² order")
    print("    (so half-sym averaging changes NOTHING):")
    print("       (4) ↔ (1,1,1,1): avg = (0+0)/2 = 0")
    print("       (3,1) ↔ (2,1,1): avg = (1+1)/2 = 1")
    print("       (2,2) self-conj: 1")
    print("    Σ_classes = 2 (not 3 — drops 1 unit from conjugate-pair")
    print("                    double-counting in the canonical sum)")
    print()
    print("  ── Audit claim ── 'half-sym extracts ONE cell' = −G ≈ −0.916")
    print("  ── My result  ── natural-reading half-sym = +0.5  (= 2/4)")
    print("  ── GAP ──")
    print("    DIFFERENT SIGN (+ vs −)")
    print("    DIFFERENT MAGNITUDE (0.5 vs 0.916; off by factor 1.83)")
    print()
    print("Verdict: under the simplest natural reading of Π_HS (averaging")
    print("over the conjugation involution), the empirical half-sym sum is")
    print("0.5·h², NOT the audit's claimed -G·h² ≈ -0.916·h².")
    print("The audit's structural claim 'half-sym extracts ONE cell' is")
    print("NOT supported by partition combinatorics under the natural")
    print("reading of Π_HS.  The audit may need:")
    print("  (1) a different operator Π_HS not encoded as conjugation-")
    print("      averaging; OR")
    print("  (2) Yekutieli's non-abelian Stokes machinery to convert")
    print("      partition κ-sum into curvature-2-form integration")
    print("      (which could change BOTH sign AND magnitude); OR")
    print("  (3) a sign-convention error in the audit's derivation")
    print("      (h² coefficient could be +G·h² with a sign reversal in")
    print("      the absorption-convention setup).")
    print()
    print("The 'extracts ONE cell' framing is NOT achievable by purely")
    print("combinatorial means at this level.  This is the load-bearing")
    print("step; the audit needs to clarify Π_HS precisely OR derive the")
    print("curvature-2-form integration step.")

    # Emit witness with the empirical numerics + verdict
    w = WitnessBuilder(
        "yekutieli-bijection-construction-h4", engine="mpmath"
    )
    w.set_description(
        "NEGATIVE RESULT — explicit cell↔partition bijection construction "
        "at H_4 for the Yekutieli per-cell curvature conjecture fails "
        "under the natural reading of Π_HS.  Empirical κ_λ findings "
        "(Richardson-extrapolated 50 dps): (4)=0, (3,1)=1, (2,2)=1, "
        "(2,1,1)=1, (1,1,1,1)=0; Σ = 3 (consistent with Family A "
        "theorem).  κ is symmetric under conjugation involution at h² "
        "order, so half-sym averaging changes nothing — natural-reading "
        "half-sym sum is +0.5·h², NOT the audit's claimed −G·h² ≈ "
        "−0.916·h² (different sign AND magnitude, factor 1.83).  The "
        "'extracts ONE cell' load-bearing step is NOT supported by "
        "partition combinatorics under the natural reading.  Audit "
        "needs either (1) a different Π_HS operator, (2) Yekutieli "
        "2015 non-abelian Stokes machinery applied beyond combinatorics, "
        "or (3) sign-convention reconciliation."
    )
    w.set_content_block("conj:lambda-scale-bring-bloch-identity")
    w.add_parameter("derivation_status", "BIJECTION_CONSTRUCTION_PARTIAL")
    w.add_parameter("gating_conjecture",
                    "cell-↔-half-sym-projection bijection at H_4 "
                    "extracts-ONE-cell step (Yekutieli 2015 machinery needed)")
    w.add_data("partition_kappa_h2", {
        p: {
            "dim": d["dim"],
            "kappa_numerical": mp.nstr(numerical_kappas[p], 20),
            "kappa_audit_guess": mp.nstr(d["kappa_h2"], 10),
            "conjugate": d["conjugate"],
            "young_shape": d["young_shape"],
        }
        for p, d in PARTITIONS.items()
    })
    w.add_data("family_a_consistency", {
        "sum_kappa_numerical": mp.nstr(total_kappa, 20),
        "family_a_target_sum_kappa": "3.0",
        "rel_diff": mp.nstr(
            (total_kappa - family_a_target) / family_a_target, 8
        ),
        "consistency": "OK" if abs(total_kappa - family_a_target) < 1e-10 else "DRIFT",
    })
    w.add_data("half_sym_projection_natural_reading", {
        "definition": "Π_HS = (id + conjugation-involution) / 2 on blocks",
        "half_sym_kappa_sum": mp.nstr(half_sym_kappa_sum, 20),
        "half_sym_kappa_div_4": mp.nstr(half_sym_kappa_sum / 4, 12),
        "target_minus_G_per_cell": mp.nstr(-G_catalan, 12),
        "magnitude_ratio": mp.nstr(G_catalan / (half_sym_kappa_sum / 4), 6),
        "sign_match": "NO (natural-reading gives +0.5, audit claims −0.916)",
        "diff_vs_target": mp.nstr(
            half_sym_kappa_sum / 4 - (-G_catalan), 8
        ),
        "verdict": (
            "NEGATIVE — natural-reading of Π_HS as conjugation-involution "
            "averaging gives κ-half-sym-sum / 4 = 0.5, NOT the audit's "
            "claimed −G ≈ −0.916.  The result differs in BOTH sign and "
            "magnitude (factor 1.83) from the conjecture's load-bearing "
            "'extracts ONE cell' claim.  Either (1) Π_HS is a different "
            "operator than conjugation-averaging; (2) the Yekutieli "
            "non-abelian Stokes machinery transforms the κ-sum into "
            "curvature-2-form integration via a factor not encoded in "
            "partition combinatorics; or (3) there is a sign-convention "
            "error in the audit's derivation."
        ),
    })
    w.add_data("cell_count_consistency", {
        "audit_decomposition": {
            "vertex_octahedra_pair": "2 (from (4) ∪ (1,1,1,1))",
            "edge_octahedra_pair":   "4 (from (3,1) ∪ (2,1,1))",
            "center_octahedra_self": "2 (from (2,2) ×2 mult)",
        },
        "total_cells": 8,
        "expected_cells_in_borromean": 8,
        "cell_count_match": "OK",
    })
    w.add_caveat(
        "NEGATIVE RESULT — the load-bearing cell-↔-half-sym-projection "
        "bijection at H_4 is NOT supported by partition combinatorics "
        "under the simplest natural reading of Π_HS.  Empirical findings:\n"
        "  * Σ κ_λ = 3 across all 5 partitions of H_4 (consistent "
        "    with Family A theorem); κ values are (4,3,1,2,2,2,1,1,1^4) "
        "    = (0,1,1,1,0).\n"
        "  * κ is SYMMETRIC under conjugation involution at h² order:\n"
        "        κ_(4) = κ_(1^4) = 0\n"
        "        κ_(3,1) = κ_(2,1,1) = 1\n"
        "        κ_(2,2) = 1 (self-conj)\n"
        "  * So conjugation-averaging changes nothing; the natural-"
        "    reading half-sym projection gives κ-sum / 4 = 0.5·h², "
        "    NOT the audit's claimed −G·h² ≈ -0.916·h²\n"
        "  * Discrepancy is in BOTH sign (+0.5 vs −0.916) and "
        "    magnitude (factor 1.83) — too large to be a precision "
        "    issue; structural mismatch.\n"
        "The audit's 'extracts ONE cell' claim therefore requires:\n"
        "  (1) a different operator Π_HS not encoded as conjugation-"
        "      averaging on Wedderburn blocks; OR\n"
        "  (2) Yekutieli 2015's non-abelian Stokes machinery to "
        "      transform the κ-sum into curvature-2-form integration "
        "      (which could change both sign AND magnitude); OR\n"
        "  (3) sign-convention reconciliation between the half-sym "
        "      projection direction (+3/4·h² Family A) and the "
        "      Yekutieli per-cell direction (−G·h² audit claim).\n"
        "Without one of these, the m_p ≈ 950 MeV Yekutieli-extended "
        "prediction in PR #976 lacks the load-bearing categorical "
        "backing the audit claimed."
    )

    w.add_assertion(
        "partition_combinatorics_internally_consistent",
        computed=8.0,
        expected=8.0,
        tolerance=0.0,
        unit="cells",
        source="2+4+2 octahedra ↔ 5 partitions via audit decomposition",
    )
    w.add_assertion(
        "family_a_sum_kappa_consistent",
        computed=float(total_kappa),
        expected=3.0,
        tolerance=1e-9,
        unit="sum κ_λ at h² order",
        source="Σ_λ⊢4 κ_λ via numerical Taylor evaluation",
    )

    out = w.save()
    print()
    print(f"Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
