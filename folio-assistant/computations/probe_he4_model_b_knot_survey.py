#!/usr/bin/env python3
# polynomial_q_not_applicable: candidate-survey witness; no fitting performed.
"""P1.E candidate-survey witness — ⁴He Model B canonical knot assignment.

Per `docs/audits/2026-05-12-1ppb-implementation-plan.md` § P1.E:
Model B encodes a nucleus as a *single canonical hyperbolic knot* in the
minimum-strand braid group.  For {D, T, ³He} the assignments are
$6_2$ (B_3), $8_{11}$ (B_5), $L6a4$ Borromean (B_3) — see
`probe-sdp-canonical-paper-formula.witness.json`.  ⁴He is open.

This script does NOT pick the canonical knot.  It computes |τ_M(β)|
at $q_0$ for each documented candidate and presents the ranked
results so the owner can select the canonical assignment.

Verification metric (per implementation plan, lines 191–195):
  ⁴He AME binding is 28.30 MeV; Model A under-predicts by ~25%, so
  the canonical Model B knot's |τ_M| should be in the range
  [0.05, 0.5] at $q_0$ to be plausible.

Candidates surveyed (braid words from KnotInfo / standard atlas):
  1. **L6a4 Borromean** — `[1,-2,1,-2,1,-2]` on B_3
     • Already used for ³He.  Including for explicit cross-check
       so the owner can rule out the degenerate-assignment risk
       called out in the plan.
  2. **8_18** — `[1,-2,1,-2,1,-2,1,-2]` on B_3, i.e. (σ₁σ₂⁻¹)^4
     • Hyperbolic, 4-bridge, 4-fold rotational symmetry matching
       ⁴He's α-particle structure.  Plan-cited candidate.
  3. **8_18^2** — `[1,-2,1,-2,1,-2,1,-2,1,-2,1,-2,1,-2,1,-2]` on B_3
     • The "doubled" 8_18 — exploratory, not in the plan candidates,
       but listed because the chirality table already has the
       sign-pattern $[+1,-1,+1,-1]$ which is the period of 8_18.
  4. **(L6a4)²** — `[1,-2,1,-2,1,-2,1,-2,1,-2,1,-2]` on B_3
     • Two L6a4 sub-knots concatenated; tests whether ⁴He as
       "two ³He clusters" is reproduced topologically.

Brunnian 4-component link (4-strand candidate from the plan):
  We do **not** compute |τ_M| for the 4-component Brunnian candidate
  here — there is no single canonical braid word for "the" Brunnian
  4-link in the literature (multiple inequivalent representatives
  exist), and a wrong choice would be misleading.  The candidate is
  flagged in the witness as `braid_word_pending` for owner
  specification.

For each computed candidate we report:
  - |τ_M| under both Plancherel and Wenzl-Schur conventions at $q_0$
  - In-range flag against [0.05, 0.5] from the plan
  - Predicted B(⁴He) = m_e · ρ · |τ_M| for ρ ∈ {1, 2, 4} and gap to
    AME = 28.30 MeV
  - A "best (knot, ρ, convention)" ranking by absolute relative error

NO fitting; ρ is iterated over a small set, not optimized.

Output: probe-he4-model-b-knot-survey.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# Reuse the canonical low-strand τ_M kernel from the SDP probe.
from probe_sdp_canonical_paper_formula import tr_M_sdp  # noqa: E402
from q_parameter import Q as Q0_FLOAT  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


# AME 2020 binding energy for ⁴He (MeV).  Same precision as
# `probe_magic_shell_empirical_instantiation.py:61` (the canonical
# Δ_cat witness source) so the two anchors stay consistent.
B_AME_HE4_MEV = 28.295674


# Candidates — each is a (label, braid_word, n_0, knot_name, note) tuple.
# Braid words use the convention σ_i ↔ +i, σ_i^{-1} ↔ -i.
CANDIDATES = [
    (
        "L6a4_Borromean",
        [1, -2, 1, -2, 1, -2],
        3,
        "L6a4",
        "Already used for ³He; included so owner can verify the "
        "degenerate-assignment risk explicitly.  Same braid word "
        "as the ³He Model B canonical.",
    ),
    (
        "8_18",
        [1, -2, 1, -2, 1, -2, 1, -2],
        3,
        "8_18",
        "Hyperbolic 3-strand knot (σ₁σ₂⁻¹)^4.  4-fold rotational "
        "symmetry matches the α-particle structure of ⁴He.  "
        "Plan-cited candidate.",
    ),
    (
        "8_18_squared",
        [1, -2, 1, -2, 1, -2, 1, -2,
         1, -2, 1, -2, 1, -2, 1, -2],
        3,
        "(8_18)²",
        "Exploratory: doubled 8_18.  Tests whether the "
        "chirality table sign pattern [+1,-1,+1,-1] survives "
        "doubling the period.",
    ),
    (
        "L6a4_squared",
        [1, -2, 1, -2, 1, -2,
         1, -2, 1, -2, 1, -2],
        3,
        "(L6a4)²",
        "Exploratory: two L6a4 sub-words concatenated.  Tests the "
        "'⁴He = two ³He clusters' topological reading.",
    ),
]

# ρ candidates — fixed iteration set, no fitting.
RHO_CANDIDATES = [1, 2, 4]


def _load_wenzl_table(n: int) -> dict | None:
    """Return Wenzl y_λ table for a given n, or None if unavailable."""
    yw = json.loads((HERE / "y-lambda-wenzl-witness.json").read_text())
    if str(n) not in yw["tables_by_n"]:
        return None
    return {
        tuple(w["partition"]): float(w["y_lambda_numeric"])
        for w in yw["tables_by_n"][str(n)]["weights"]
    }


def main() -> int:
    print("=" * 92)
    print("P1.E candidate-survey — ⁴He Model B canonical knot assignment")
    print("=" * 92)
    print(f"  q_0          = {Q0_FLOAT}")
    print(f"  m_e          = {M_E_MEV} MeV")
    print(f"  AME(⁴He)     = {B_AME_HE4_MEV} MeV  (binding)")
    print(f"  Plausibility band for |τ_M|: [0.05, 0.50]  "
          f"(per plan §P1.E)")
    print()

    rows = []
    for (label, braid_word, n_0, knot_name, note) in CANDIDATES:
        wenzl = _load_wenzl_table(n_0)
        if wenzl is None:
            print(f"  [{label}] no Wenzl table for n_0={n_0}; skip.")
            continue
        tr_P, tr_W, per_lam = tr_M_sdp(n_0, braid_word, wenzl)
        abs_tr_P = abs(tr_P)
        abs_tr_W = abs(tr_W)
        in_band_P = 0.05 <= abs_tr_P <= 0.50
        in_band_W = 0.05 <= abs_tr_W <= 0.50
        print(f"  [{label}]  knot={knot_name}  n_0={n_0}  "
              f"len(β)={len(braid_word)}")
        print(f"    |τ_M|_Plancherel  = {abs_tr_P:>10.6f}  "
              f"{'IN' if in_band_P else 'out'} band [0.05, 0.50]")
        print(f"    |τ_M|_Wenzl-Schur = {abs_tr_W:>10.6f}  "
              f"{'IN' if in_band_W else 'out'} band [0.05, 0.50]")
        for rho in RHO_CANDIDATES:
            B_P = M_E_MEV * rho * abs_tr_P
            B_W = M_E_MEV * rho * abs_tr_W
            err_P = (B_P - B_AME_HE4_MEV) / B_AME_HE4_MEV * 100.0
            err_W = (B_W - B_AME_HE4_MEV) / B_AME_HE4_MEV * 100.0
            print(f"      ρ={rho}: B_P={B_P:>9.3f} MeV ({err_P:>+8.2f}%)  "
                  f"B_W={B_W:>9.3f} MeV ({err_W:>+8.2f}%)")
        print(f"    note: {note}")
        print()
        rows.append({
            "candidate_label": label,
            "knot_name": knot_name,
            "n_0": n_0,
            "braid_word": braid_word,
            "braid_length": len(braid_word),
            "tr_M_plancherel": tr_P,
            "tr_M_wenzl_schur": tr_W,
            "abs_tr_M_plancherel": abs_tr_P,
            "abs_tr_M_wenzl_schur": abs_tr_W,
            "in_plausibility_band_plancherel": in_band_P,
            "in_plausibility_band_wenzl_schur": in_band_W,
            "B_predicted_MeV": {
                f"rho={rho}": {
                    "plancherel": M_E_MEV * rho * abs_tr_P,
                    "wenzl_schur": M_E_MEV * rho * abs_tr_W,
                    "rel_err_plancherel_pct":
                        (M_E_MEV * rho * abs_tr_P - B_AME_HE4_MEV)
                        / B_AME_HE4_MEV * 100.0,
                    "rel_err_wenzl_schur_pct":
                        (M_E_MEV * rho * abs_tr_W - B_AME_HE4_MEV)
                        / B_AME_HE4_MEV * 100.0,
                }
                for rho in RHO_CANDIDATES
            },
            "per_lambda": per_lam,
            "note": note,
        })

    # Rank by best |rel_err| across (rho, convention) for each row.
    print("=" * 92)
    print("Ranking by best |rel_err to AME| over (ρ, convention):")
    print("=" * 92)
    ranked = []
    for r in rows:
        best = None
        for rho in RHO_CANDIDATES:
            for conv in ("plancherel", "wenzl_schur"):
                key = f"rel_err_{conv}_pct"
                err_pct = r["B_predicted_MeV"][f"rho={rho}"][key]
                cand = (abs(err_pct), rho, conv, err_pct)
                if best is None or cand[0] < best[0]:
                    best = cand
        ranked.append({
            "candidate_label": r["candidate_label"],
            "knot_name": r["knot_name"],
            "best_abs_err_pct": best[0],
            "best_rho": best[1],
            "best_convention": best[2],
            "best_signed_err_pct": best[3],
        })
    ranked.sort(key=lambda x: x["best_abs_err_pct"])
    for i, r in enumerate(ranked, 1):
        print(f"  {i}. {r['candidate_label']:<18}  knot={r['knot_name']:<10}"
              f"  best ρ={r['best_rho']}  conv={r['best_convention']:<11}"
              f"  err={r['best_signed_err_pct']:>+8.2f}%")

    # Brunnian-4 candidate placeholder (not computed).
    pending = {
        "candidate_label": "Brunnian_4_component",
        "knot_name": "L?-Brunnian-4",
        "braid_word": None,
        "status": "braid_word_pending",
        "note": (
            "Plan §P1.E lists a Brunnian 4-component link as a "
            "candidate (matching the chirality-table sign pattern "
            "[+1,-1,+1,-1]).  Multiple inequivalent representatives "
            "exist in the literature; no single canonical braid word.  "
            "Owner input required to specify the candidate before "
            "|τ_M| can be computed.  When provided, run this script "
            "with the new braid word added to the CANDIDATES list."
        ),
    }
    print()
    print("Pending candidate (owner input required):")
    print(f"  - {pending['candidate_label']} ({pending['knot_name']}):"
          f" braid_word_pending")
    print()

    builder = WitnessBuilder("probe-he4-model-b-knot-survey",
                             engine="python")
    builder.set_description(
        "P1.E candidate-survey for the ⁴He Model B canonical "
        "hyperbolic knot assignment.  Computes |τ_M(β)| at q_0 for "
        "four documented candidates (L6a4, 8_18, (8_18)², (L6a4)²) "
        "under both Plancherel and Wenzl-Schur Markov-trace "
        "conventions, and reports B = m_e · ρ · |τ_M| for ρ ∈ {1, 2, 4} "
        "against AME(⁴He) = 28.30 MeV.  Plausibility band per plan: "
        "|τ_M| ∈ [0.05, 0.50].  No fitting performed.  Brunnian "
        "4-component candidate flagged as braid_word_pending — owner "
        "must specify the canonical representative before τ_M can "
        "be computed.  Witness is decision-support input for owner "
        "selection of the ⁴He Model B canonical knot."
    )
    builder.set_content_block("conj:magic-shell-stabilization")
    builder.add_parameter("q_0", float(Q0_FLOAT))
    builder.add_parameter("m_e_MeV", M_E_MEV)
    builder.add_parameter("B_AME_he4_MeV", B_AME_HE4_MEV)
    builder.add_parameter("plausibility_band_abs_tr_M", [0.05, 0.50])
    builder.add_parameter("rho_candidates", RHO_CANDIDATES)
    builder.add_data("candidates", rows)
    builder.add_data("ranked_by_best_rel_err_to_AME", ranked)
    builder.add_data("pending_candidates", [pending])
    builder.add_caveat(
        "Survey emits ranked decision-support data for owner "
        "selection.  No claim is made that the lowest-error candidate "
        "IS the canonical Model B knot — the canonical assignment "
        "must be derived from the categorical structure (knot "
        "complement geometry, KLR-canonical-basis class, etc.), not "
        "back-fit to AME.  ρ is iterated over a fixed small set, not "
        "optimized.  Conventions: Plancherel weight w_λ = "
        "(dim V_λ)²/n!; Wenzl-Schur weight y_λ from "
        "y-lambda-wenzl-witness.json (Markov / Jones-Markov "
        "convention)."
    )
    out = builder.save()
    print(f"\n  → wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
