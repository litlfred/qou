#!/usr/bin/env python3
"""I-6 — pin the canonical per-knot trace convention (GAP-A-4 gate, bean fv0y).

Before ANY ρ(K) per-knot-density search, the corpus carries (≥) two distinct
"per-knot Markov trace" objects for the SAME 𝓑₃ proton braid family, at
q₀ = 1.10997859555733471:

  (A) F_Bor convention  — the UNNORMALISED Borromean braid trace with the
      [3]_q!/q³ framing normalisation used by the muon-anchored mass facade:
          F_Bor = |tr_M(β_Bor)| · [3]_q!/q³        (canonical_mass.py)
      ⇒ |tr_M(β_Bor)| = F_Bor · q³/[3]_q! ≈ 0.998562.

  (B) chi-cache convention — the dim-λ-NORMALISED per-block trace consumed by
      the per-knot density / binding path:
          tr_M(K) = Σ_λ y_λ · χ^λ(β_K) / dim λ      (_li_2_q_util.per_knot_density_per_block)
      ⇒ tr_M(p) ≈ 1.0653, tr_M(n) ≈ 0.9232  (excision ledger precision;
        docs/coordination/2026-06-24-lambda-a-fit-excised-per-knot-density.md).

These are NOT the same number (ratio ≈ 1.0668), and the q-dim route probe
showed convention freedom is a hidden DOF spanning 0.41→5.62 on the ⁴He ceiling
— so any ρ(K) "match" is unfalsifiable until the convention is pinned
(scoping note docs/scope/2026-07-02-gap-a4-perknot-density-rule-scoping.md §I-6).

PIN (this gate's ruling, compute-checked below):
  • (B) the dim-λ-normalised chi-cache tr_M(K) is CANONICAL for ρ(K)/binding —
    it is p≠n distinct (15.4% asymmetric), which is the binding signal, and is
    the object `per_knot_density_per_block` already consumes.
  • (A) the F_Bor unnormalised+[3]_q!/q³ convention is reserved for the
    muon-anchored ABSOLUTE-mass facade (canonical_mass.py), where the framing
    normalisation is part of the dimensionless dressing factor.
  • The two are related by the explicit framing/normalisation factor
    R(K) = tr_M(K)_chicache / |tr_M(β_K)|_Fbor  (reported; ≈1.0668 for p).
    R is a per-knot normalisation, NOT a free parameter: fixing the convention
    to (B) removes the hidden DOF.

Companion Lean: QOU/MassTheory/TraceConventionGate.lean
  • I-6 `traceConvention_factor` — the two traces relate by a nonzero factor R.
  • I-1 `no_uniform_scalar_density` — the (b)-grade exclusion of the
    single-q₀-scalar density family (tr asymmetric, ρ_rt near-degenerate).

audit_only, parameter-free, no fit, no production consumer.
`-- Ref:` canonical-mass-formula-guardrail.md; Ram IMRN 1997 (tr_M = Σ y_λ χ^λ).
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
from mpmath import mp, mpf  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402
from m_p_substrate_identity_50dps import F_Bor  # noqa: E402

COMP = str(_COMP)
Q0 = "1.10997859555733471"

# chi-cache per-knot traces (dim-λ-normalised) at ledger precision — the
# scoping note reproduces every §1 value from first principles EXCEPT these,
# quoted at ledger precision (excision ledger 2026-06-24).
TRM_CHICACHE = {"p": mpf("1.0653"), "n": mpf("0.9232")}


def q_bracket(q, n):
    return (q ** n - q ** (-n)) / (q - 1 / q)


def main() -> int:
    q = mpf(Q0)
    # (A) F_Bor convention: |tr_M(β_Bor)| = F_Bor · q³/[3]_q!
    FB = F_Bor(q)
    three_q_fact = q_bracket(q, 1) * q_bracket(q, 2) * q_bracket(q, 3)
    framing = three_q_fact / q ** 3            # [3]_q!/q³
    trM_bor_Fbor = FB / framing                # ≈ 0.998562
    # (B) chi-cache convention
    trM_p = TRM_CHICACHE["p"]
    trM_n = TRM_CHICACHE["n"]
    # the explicit normalisation factor relating the two proton traces
    R_p = trM_p / trM_bor_Fbor
    # p/n asymmetry (chi-cache) vs the near-degenerate round-trip density
    trm_asym = trM_p / trM_n                    # 1.15392

    result = {
        "q0": Q0,
        "convention_A_Fbor": {
            "F_Bor": mp.nstr(FB, 12),
            "framing_[3]q!/q^3": mp.nstr(framing, 12),
            "abs_trM_beta_Bor": mp.nstr(trM_bor_Fbor, 12),
            "normalisation": "unnormalised Borromean braid trace × [3]_q!/q³ framing",
            "role": "muon-anchored ABSOLUTE-mass facade (canonical_mass.py)",
        },
        "convention_B_chicache": {
            "trM_p": mp.nstr(trM_p, 8) + " (ledger precision)",
            "trM_n": mp.nstr(trM_n, 8) + " (ledger precision)",
            "trM_p_over_n": mp.nstr(trm_asym, 8),
            "normalisation": "dim-λ-normalised per-block Σ_λ y_λ χ^λ/dim λ",
            "role": "per-knot density ρ(K) / BINDING (p≠n distinct is the signal)",
        },
        "relating_factor_R_p": mp.nstr(R_p, 8),
        "pin": ("CANONICAL for ρ(K)/binding = convention (B), the dim-λ-normalised "
                "chi-cache tr_M(K) (p≠n distinct). Convention (A) F_Bor is reserved "
                "for the muon-anchored absolute-mass facade. The two relate by the "
                "explicit per-knot framing factor R(K) = tr_M(K)_chicache / "
                "|tr_M(β_K)|_Fbor ≈ 1.0668 (p) — a normalisation, not a free DOF."),
        "hidden_dof_closed": ("Fixing the convention to (B) removes the 0.41→5.62 "
                              "convention-freedom span the q-dim route probe flagged."),
        "verdict": ("I-6 PINNED: dim-λ-normalised chi-cache tr_M(K) is canonical for "
                    "ρ(K); F_Bor's [3]_q!/q³-framed unnormalised trace is the "
                    "absolute-mass-facade convention; related by explicit factor R(K)."),
    }

    payload = {
        "computation": "i6-trace-convention-pin",
        "description": ("GAP-A-4 gate I-6: pin the canonical per-knot Markov-trace "
                        "convention. F_Bor (unnormalised × [3]_q!/q³) |tr_M(β_Bor)|=0.9986 "
                        "vs dim-λ-normalised chi-cache tr_M(p)=1.0653; related by explicit "
                        "factor R_p≈1.0668. Canonical for ρ(K) = chi-cache (B). "
                        "audit-only, parameter-free, no fit."),
        "tier": "structural (F_Bor side exact 50-dps; chi-cache side ledger precision)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 per-knot density ρ(K) — trace-convention gate (I-6)",
            "scoping_note": "docs/scope/2026-07-02-gap-a4-perknot-density-rule-scoping.md §I-6",
            "lean": "qou:QOU.MassTheory.TraceConventionGate",
            "facade": "computations/canonical_mass.py (F_Bor); _li_2_q_util.per_knot_density_per_block (chi-cache)",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "i6-trace-convention-pin", payload,
        script_path=__file__, engine="python+mpmath", output_dir=COMP,
    )
    wb.add_assertion("Fbor_implied_trM_beta_Bor_near_unity",
                     computed=mp.nstr(trM_bor_Fbor, 8), expected="0.998562", tolerance=1e-4)
    wb.add_assertion("chicache_trM_p_over_n_asymmetric",
                     computed=mp.nstr(trm_asym, 8), expected="1.15392", tolerance=1e-3)
    wb.add_assertion("conventions_distinct_factor_R_p_gt_1",
                     computed=mp.nstr(R_p, 8), expected="1.0668", tolerance=1e-3)
    out = wb.save(extra={"auditOnly": True})

    print("=== I-6 trace-convention pin ===")
    print(f"  (A) F_Bor         : |tr_M(β_Bor)| = {float(trM_bor_Fbor):.6f}  "
          f"(F_Bor={float(FB):.5f}, [3]_q!/q³={float(framing):.5f})")
    print(f"  (B) chi-cache     : tr_M(p) = {float(trM_p):.4f}  tr_M(n) = {float(trM_n):.4f}  "
          f"(p/n = {float(trm_asym):.5f})")
    print(f"  relating factor R_p = tr_M(p)/|tr_M(β_Bor)| = {float(R_p):.5f}")
    print("  PIN: canonical ρ(K) = (B) dim-λ-normalised chi-cache; (A) = abs-mass facade.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
