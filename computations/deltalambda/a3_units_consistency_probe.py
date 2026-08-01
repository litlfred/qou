#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""a3_units_consistency_probe.py — the "1.6× A=3 near-miss" is a UNITS ARTIFACT; the
dimensionally-consistent gap is 3.53×. Corrects the corpus (#4364 / three-walls) AND the
corpus-convention numbers in §2–3c of this PR's earlier probes.

THE PUN (found in borromean_h9_magnitude_lift_probe.py:188)
-----------------------------------------------------------
That probe prints `target μ₃ = 0.4708 (dimensionless, read as MeV)` and then computes
`c₃/μ₃ = 0.63 → "~1.6× short"`. But the two quantities have DIFFERENT DIMENSIONS:

  * μ₃ = M(3) = ρ_strong(3) − ρ_grad(3) is DIMENSIONLESS — a ratio coefficient
    (ρ_strong(A) = B(A)/B(²H), ρ_grad(A) = [A]_q!/[2]_q!; ρ_strong(2)=1 confirms it is a pure ratio).
  * c₃ = E₀·(1−τ_Borr) is a genuine ENERGY in MeV (E₀ = m_e/(q₀(q₀−1)) ≈ 4.19 MeV).

Comparing 0.297 MeV to 0.4708 (dimensionless) as "0.63×" silently sets B(²H) = 1 MeV. The correct
conversion into the dimensionless simplex decomposition is c₃ ↦ c₃/B(²H):

  c₃(ratio) = c₃_MeV / B(²H) = 0.297 / 2.224566 = 0.13351.

THE HONEST NUMBERS (× B(²H) = 2.224566 from the punned ones)
-----------------------------------------------------------
  * A=3 3-body gap  μ₃ / c₃(ratio)      = 3.53×      (NOT 1.6×)
  * cluster supplies c₃(ratio) / μ₃     = 28.4%      (NOT 63%)
  * A=3 binding miss (energy-consistent) = 8.85% / 0.750 MeV   (NOT 4.6%)
  * strengthened order-separation: a higher-order closure needs an h⁶ coefficient
        a₁ = (μ₃ − c₃_ratio)/(c₃_ratio·h²) ≈ 57.8   (vs the punned 13.4) — even MORE anomalous,
    so the "compute higher orders" route is ruled out even harder.
  * A=4 (energy-consistent): required 4-body c₄ ≈ −7.9 MeV, |c₄|/c₃ ≈ 26.6 (vs punned 13.1).

The discrepancy factor is EXACTLY B(²H) = 2.224566 — a single-factor, verifiable correction.

CONSEQUENCE
-----------
The A=3 magnitude is ~2× FURTHER from closure than the headline "1.6× near-miss" suggested: the
derived Borromean cluster reproduces only 28% of the needed 3-body binding, not 63%. This does not
refute the graded-dim route; it CORRECTS the magnitude of the open gap (makes it honestly larger) and
reinforces the Δ_λ-gated conclusion. Scope-(a) calibration (mirror of the "over-claim / under-claim"
disciplines: a units pun made an open gap look ~2× smaller than it is).

STRICT anti-fit: no fit; B(²H), c₃, μ₃ consumed as fixed inputs; nothing wired. The corpus files
(#4364, three-walls audit, borromean_h9_magnitude_lift_probe.py:188) still carry the pun — flagged for
coordination, not rewritten here. Exact (mpmath). EXPLORATORY — audit + witness only.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

BH2 = mp.mpf("2.224566")         # B(²H) MeV (AME) — the missing conversion factor
BHe4 = mp.mpf("28.296")          # B(⁴He) MeV (AME)
C3_MEV = mp.mpf("0.297")         # derived 3-body Borromean cluster, genuine MeV (E₀·deficit)
MU3 = mp.mpf("0.4708")           # dimensionless 3-body simplex coefficient (ratio units)
RHO_GRAD_G3 = mp.mpf("3.3420311")   # [3]_q at q₀, dimensionless
RHO_GRAD_G4 = mp.mpf("15.73957")    # [3]_q·[4]_q at q₀, dimensionless
RHO_STRONG3 = mp.mpf("3.8128")
H2 = mp.mpf("0.0437062")


def main() -> int:
    c3_ratio = C3_MEV / BH2                       # cluster in the dimensionless decomposition
    punned_gap = MU3 / C3_MEV                      # what the corpus computed (0.297 read as 0.4708-units)
    honest_gap = MU3 / c3_ratio                    # dimensionally consistent
    correction_factor = honest_gap / punned_gap    # must equal B(²H)

    cluster_frac_of_target = c3_ratio / MU3        # honest: 28.4% (vs punned 63%)
    miss_ratio = MU3 - c3_ratio
    miss_energy = miss_ratio * BH2
    # energy-consistent A=3 binding miss
    graded_E = BH2 * RHO_GRAD_G3
    model_E = graded_E + C3_MEV
    actual_BH3 = BH2 * RHO_STRONG3                 # isospin-corrected effective B(³H)
    miss_pct_binding = 100 * (actual_BH3 - model_E) / actual_BH3
    # strengthened order-separation
    a1_required = miss_ratio / (c3_ratio * H2)
    # A=4 honest (energy)
    c4_req_MeV = BHe4 - (BH2 * RHO_GRAD_G4 + 4 * C3_MEV)
    c4_over_c3_energy = abs(c4_req_MeV) / C3_MEV

    result = {
        "the_pun": {
            "site": "borromean_h9_magnitude_lift_probe.py:188 — 'target μ₃ = 0.4708 (dimensionless, "
                    "read as MeV)'",
            "mu3_dimensionless": mp.nstr(MU3, 6),
            "c3_MeV": mp.nstr(C3_MEV, 6),
            "E0_note": "E₀ = m_e/(q₀(q₀−1)) ≈ 4.19 MeV ⇒ c₃ = E₀·deficit is a genuine energy",
            "missing_conversion_factor_B2H_MeV": mp.nstr(BH2, 8),
        },
        "corrected_gap": {
            "c3_in_ratio_units": mp.nstr(c3_ratio, 8),
            "punned_gap_mu3_over_c3_MeV": mp.nstr(punned_gap, 6) + " ('1.6× near-miss')",
            "honest_gap_mu3_over_c3_ratio": mp.nstr(honest_gap, 6) + " (3.53×)",
            "correction_factor": mp.nstr(correction_factor, 8),
            "correction_factor_is_B2H": bool(abs(correction_factor - BH2) < mp.mpf("1e-6")),
            "cluster_frac_of_target_pct": mp.nstr(100 * cluster_frac_of_target, 5) + " (NOT 63%)",
        },
        "corrected_binding_miss": {
            "graded_energy_MeV": mp.nstr(graded_E, 8),
            "model_energy_MeV": mp.nstr(model_E, 8),
            "actual_effective_BH3_MeV": mp.nstr(actual_BH3, 8),
            "miss_energy_MeV": mp.nstr(actual_BH3 - model_E, 6),
            "miss_pct_binding": mp.nstr(miss_pct_binding, 5) + " (NOT 4.6%)",
        },
        "strengthened_order_separation": {
            "honest_missing_ratio": mp.nstr(miss_ratio, 6),
            "honest_missing_MeV": mp.nstr(miss_energy, 6),
            "required_h6_coefficient_a1": mp.nstr(a1_required, 6) + " (vs punned 13.4 — MORE anomalous)",
            "higher_order_route_ruled_out_harder": True,
        },
        "a4_honest": {
            "required_c4_MeV": mp.nstr(c4_req_MeV, 6),
            "c4_over_c3_energy": mp.nstr(c4_over_c3_energy, 6) + " (vs punned 13.1)",
        },
        "verdict": {
            "classification": "scope-(a) CALIBRATION: the '1.6× A=3 near-miss' is a UNITS ARTIFACT "
                              "(c₃ MeV compared to μ₃ dimensionless, ×B(²H) omitted). The honest gap is "
                              "3.53×; the derived cluster supplies 28% (not 63%) of the 3-body target; "
                              "the binding miss is 8.85% (not 4.6%). This is ~2× further from closure "
                              "than the headline — reinforcing the Δ_λ-gated conclusion, NOT refuting "
                              "the graded-dim route.",
            "corrects": "the corpus (#4364, three-walls audit, borromean probe:188) AND the "
                        "corpus-convention numbers in §2–3c of this PR's earlier probes. The corpus "
                        "files still carry the pun — flagged for coordination, not rewritten here.",
            "anti_fit": "single-factor B(²H) correction; no fit; nothing wired.",
        },
    }

    this = Path(__file__).resolve()
    witness = {
        "schema": "witness/v1",
        "producer": str(this.relative_to(ROOT)),
        "computation": "a3-units-consistency",
        "description": (
            "The '1.6× A=3 magnitude near-miss' is a UNITS ARTIFACT. The derived 3-body cluster "
            "c₃=0.297 is a genuine ENERGY (MeV; E₀=m_e/(q₀(q₀−1))·deficit) but is compared directly to "
            "the DIMENSIONLESS simplex coefficient μ₃=0.4708 (ρ_strong−ρ_grad, a pure ratio) — the "
            "borromean probe line 188 admits it: 'μ₃ (dimensionless, read as MeV)'. Converting the "
            "cluster into the dimensionless decomposition (c₃/B(²H)=0.1335) gives the honest A=3 3-body "
            "gap 3.53× (not 1.6×): the cluster supplies 28% (not 63%) of the target, and the "
            "energy-consistent binding miss is 8.85%/0.750 MeV (not 4.6%). The correction factor is "
            "exactly B(²H)=2.224566. The order-separation strengthens (required h⁶ coeff 57.8 vs 13.4). "
            "A=4 |c₄|/c₃ becomes 26.6 (vs 13.1). scope-(a) calibration — corrects the corpus (#4364, "
            "three-walls, borromean probe:188) and this PR's §2–3c corpus-convention numbers; the A=3 "
            "magnitude is ~2× further from closure than the headline, reinforcing Δ_λ-gating. No fit; "
            "nothing wired; exact (mpmath)."),
        "audit_only": True,
        "tier": "scope-(a) units-consistency calibration (single-factor B(²H) correction); no fit",
        "scriptHash": hashlib.sha256(this.read_bytes()).hexdigest()[:16],
        "result": result,
        "context": {
            "axis": "Δ_λ / A=3 magnitude — units consistency of the target",
            "builds_on": "borromean_h9_magnitude_lift_probe.py:188 (the pun), #4364, three-walls, "
                         "this PR's mu3/a3/a4 probes",
            "no_fit": True,
        },
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", str(this)],
            cwd=this.parent, text=True).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "a3-units-consistency.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str) + "\n")

    print("=== the '1.6× A=3 near-miss' is a UNITS ARTIFACT ===")
    print(f"PUN: c₃ = {mp.nstr(C3_MEV,4)} MeV  compared to  μ₃ = {mp.nstr(MU3,4)} (DIMENSIONLESS) "
          f"as '0.63×' — omits B(²H) = {mp.nstr(BH2,6)} MeV")
    print(f"correct: c₃(ratio) = c₃/B(²H) = {mp.nstr(c3_ratio,6)}")
    print()
    print(f"  punned gap  μ₃/c₃(MeV)    = {mp.nstr(punned_gap,5)}×   ('1.6× near-miss')")
    print(f"  HONEST gap  μ₃/c₃(ratio)  = {mp.nstr(honest_gap,5)}×   (correction ×{mp.nstr(correction_factor,6)} = B(²H))")
    print(f"  cluster supplies {mp.nstr(100*cluster_frac_of_target,4)}% of the 3-body target (NOT 63%)")
    print(f"  energy-consistent A=3 binding miss = {mp.nstr(miss_pct_binding,4)}% "
          f"({mp.nstr(actual_BH3-model_E,4)} MeV)  (NOT 4.6%)")
    print(f"  strengthened order-sep: required h⁶ coeff a₁ = {mp.nstr(a1_required,5)} (vs punned 13.4)")
    print(f"  A=4 honest: |c₄|/c₃ = {mp.nstr(c4_over_c3_energy,5)} (vs punned 13.1)")
    print()
    print("VERDICT (scope-a calibration): the A=3 magnitude is ~2× FURTHER from closure than the "
          "headline; derived cluster = 28% of target. Reinforces Δ_λ-gating; corrects corpus + this "
          "PR's §2–3c. No fit; nothing wired.")
    print(f"witness -> {out.name}")

    assert result["corrected_gap"]["correction_factor_is_B2H"], "correction must be exactly B(²H)"
    assert honest_gap > 3 and honest_gap < 4, "honest gap must be ~3.5×"
    assert a1_required > 50, "strengthened order-separation coefficient must exceed 50"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
