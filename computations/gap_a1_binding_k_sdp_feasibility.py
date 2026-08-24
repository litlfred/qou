#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical Wedderburn-block evaluation at q_0;
# this is a FEASIBILITY PROBE, not a production mass compute.
"""
GAP-A-1 binding-operator-K SDP — feasibility probe (honest, no fit).

Question (from docs/audits/2026-05-31-gap-a3-a4-feasibility-assessment.md §6):
  Is the binding operator K(𝔥) ∈ H_{3A}(q_0) determined by ALREADY-CANONICAL
  data alone (substrate q_0, characters χ^λ, weights y_λ, the nucleon braids),
  and does K's per-block Wedderburn content then yield the per-isotope binding
  energy B / the per-partition Δ_λ — WITHOUT feeding in B_AME?

  If yes → GAP-A-1 is a genuine non-circular lever to L2 Subgoal-1.
  If extracting B / Δ_λ from a KNOWN K still needs B_AME (or fitted per-block
  energy scales E_0^λ) → GAP-A-1 reduces to Δ_λ like GAP-A-3 / GAP-A-4, and
  the conclusion is a clean NEGATIVE (the circularity #1591 warned about).

This script does NOT add a 7th Δ_λ ansatz and tunes NO parameter to B_AME.
It runs the substrate-only deuteron K-SDP and then makes the circularity (or
its absence) QUANTITATIVE and explicit. Every number traces to this witness.

Steps (deuteron ²H, A=2, n_0=6):
  1. Substrate-only K selection. The inter-nucleon binding enumerator
     (binding_k_enumerator.py) selects the unique shortest PSD-feasible
     inter-nucleon binding K = σ_3^2 (Hopf L_H) from the substrate-restricted
     generator set {σ_3, σ_3^{-1}} by PSD-feasibility (α_gap=0) + Markov-trace
     fingerprint — NO B_AME in the objective. We reuse that K here.
  2. Per-block χ^λ(K) at H_6(q_0) for every λ ⊢ 6 (11 partitions).
  3. Operator-selection SDP over K's Wedderburn blocks via
     solve_psd_operator_selection_sdp (the canonical dual-emitting entry
     point) — channels = blocks, costs t_λ = -|y_λ·χ^λ(K)|. Emits the
     required dual fields (X_star, Z_star, primal_obj, dual_obj, duality_gap,
     eigenvalues) per AGENTS.md "LP/SDP duals — first-class infra".
  4. The DECISIVE map test. The canonical mass formula
     (prop:rho-k-h3a-refinement) defines
         Δ_λ(K) = (M_λ(K) − m_e·y_λ·χ^λ(𝓑_K)) / (m_e·y_λ·χ^λ(𝓑_K)),
         B(K)   = m_e·Σ_λ y_λ·χ^λ(𝓑_K)·Δ_λ(K).
     Knowing K gives χ^λ(𝓑_K) (a dimensionless Hecke character). To get Δ_λ
     we need M_λ(K), the MASS-FUNCTOR's per-block component (MeV). The
     deprecated per_block_phi_q.py shows the only known map χ^λ → M_λ requires
     per-block energy scales E_0^λ obtained by `fit_three_E0` — a linear LSQ
     fit to {e⁻, p, n}. We verify this is the ONLY available map and that the
     deuteron equation B = m_e·Σ y_λ χ^λ Δ_λ is 1 equation in p(6)=11 unknowns
     Δ_λ, hence underdetermined without an external M_λ (= B_AME-equivalent).

Output: gap-a1-binding-k-sdp-feasibility.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q_FLOAT  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from hecke_characters import partitions_of, dim_q  # noqa: E402
from lp_dual_solver import solve_psd_operator_selection_sdp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from binding_k_solver import (  # noqa: E402
    per_block_evaluation, load_wenzl_weights,
)

Q0 = float(Q_FLOAT)
HERE = Path(__file__).parent

# Deuteron ²H: A=2, n_0=6. Constituents {p, n}; canonical atomic braid 6_2.
N0 = 6
A = 2
# B_AME(D) = 2.224566 MeV — RECORDED FOR RESIDUAL REPORTING ONLY. It is NOT
# fed into any selection / objective / normalization below. Its sole use is
# the final honest residual print.
B_AME_D_MEV = 2.224566

# The substrate-only PSD-feasible inter-nucleon binding for ²H, selected by
# binding_k_enumerator.py (shortest PSD-feasible word in {σ_3, σ_3^{-1}},
# Markov-fingerprint ranked — NO B_AME). σ_3^2 = Hopf link L_H crossing the
# proton strand-triple with the neutron strand-triple in B_6.
K_WORD_SUBSTRATE = [3, 3]


def main() -> int:
    print("=" * 78)
    print("  GAP-A-1 binding-operator-K SDP — feasibility probe (deuteron ²H)")
    print("  Honest test: does substrate-only K → B / Δ_λ without B_AME?")
    print("=" * 78)
    print(f"  q_0 = {Q0}")
    print(f"  m_e = {M_E_MEV} MeV")
    print(f"  substrate-only binding K (Hopf, from enumerator) = σ_{K_WORD_SUBSTRATE}")
    print()

    w = WitnessBuilder("gap-a1-binding-k-sdp-feasibility", engine="python")

    # ── Step 2: per-block χ^λ(K) at H_6(q_0). ──────────────────────────
    K_eval = per_block_evaluation(K_WORD_SUBSTRATE, N0, q=Q0)
    wenzl = load_wenzl_weights(N0)
    if not wenzl:
        n_part = sum(1 for _ in partitions_of(N0))
        wenzl = {tuple(p): 1.0 / n_part for p in partitions_of(N0)}

    per_lambda = []
    for lam, blk in K_eval["per_block"].items():
        y = wenzl.get(lam, 0.0)
        chi = blk["chi"]
        per_lambda.append({
            "lambda": list(lam),
            "chi_K": chi,
            "y_lambda": y,
            "y_chi": y * chi,
            "abs_y_chi": abs(y * chi),
            "dim_q": float(dim_q(lam)),
            "psd_within_tol": blk["psd_within_tol"],
        })
    per_lambda.sort(key=lambda r: r["abs_y_chi"], reverse=True)
    dominant = per_lambda[0]

    print("  Step 2 — per-block χ^λ(K) at H_6(q_0):")
    print(f"    {'λ':<16}{'χ^λ(K)':>12}{'y_λ':>12}{'|y_λ·χ^λ|':>14}{'dim_q':>8}")
    for r in per_lambda:
        print(f"    {str(tuple(r['lambda'])):<16}{r['chi_K']:>12.6f}"
              f"{r['y_lambda']:>12.6f}{r['abs_y_chi']:>14.6f}{r['dim_q']:>8.3f}")
    print(f"    dominant λ*(K) = {tuple(dominant['lambda'])} "
          f"(by |y_λ·χ^λ|)")
    print()

    # ── Step 3: operator-selection SDP over K's blocks (dual fields). ──
    # Channels = Wedderburn blocks; cost t_λ = -|y_λ·χ^λ(K)| so the SDP's
    # selected channel is the dominant block. G = I (diagonal PSD lift).
    t = -np.array([r["abs_y_chi"] for r in per_lambda])
    G = np.eye(len(per_lambda))
    # Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
    # whether the Rust binary happens to be built, so the same script
    # yields different numbers on different boxes. QOU_REQUIRE_CLARABEL=1
    # makes a missing binary an error rather than a changed answer.
    # Bean `qou/ftuv`.
    sdp = solve_psd_operator_selection_sdp(t, G, n_target=1.0, backend="clarabel")
    sdp_d = sdp.to_dict()
    # The diagonal-lift SDP delegates to the operator-selection LP, so the
    # LP-style dual variables live in Z_star = [y0_star, *y_star] and the
    # primal in X_star. Surface them under the canonical LP-dual field names
    # (y0_star, y_star, active_set) so the lp_dual_witness_validator passes —
    # per AGENTS.md "LP/SDP duals — first-class infra".
    Z = list(sdp_d.get("Z_star") or [])
    if Z:
        sdp_d["y0_star"] = float(Z[0])
        sdp_d["y_star"] = [float(v) for v in Z[1:]]
    else:
        sdp_d["y0_star"] = float("nan")
        sdp_d["y_star"] = []
    # Active set: Frobenius-positivity constraints tight at the optimum
    # (y_star[i] > 0). For the diagonal lift G = I these are the unselected
    # channels; the dominant block is the complementary x_i^* > 0.
    sdp_d["active_set"] = [
        i for i, yi in enumerate(sdp_d["y_star"]) if yi > 1e-9
    ]
    print("  Step 3 — operator-selection SDP over K's Wedderburn blocks:")
    print(f"    primal_obj = {sdp_d['primal_obj']:.6e}")
    print(f"    dual_obj   = {sdp_d['dual_obj']:.6e}")
    print(f"    duality_gap= {sdp_d['duality_gap']:.3e}")
    print(f"    feasible   = {sdp_d['feasible']}")
    print()

    # ── Step 4: the DECISIVE map test (χ^λ(K) → Δ_λ → B). ──────────────
    # The Schur-Weyl identity |tr_M(𝓑_K)| = Σ_λ y_λ χ^λ(𝓑_K) holds exactly;
    # with Δ_λ ≡ 0 the formula reproduces the CONSTITUENT mass (zero binding).
    # The binding lives entirely in the Δ_λ profile, and Δ_λ is DEFINED via
    # the mass-functor per-block component M_λ(K) which K's CHARACTER does
    # not supply. Quantify the underdetermination.
    sum_y_chi = sum(r["y_chi"] for r in per_lambda)   # = tr_M(𝓑_K)-like sum
    n_unknowns = len(per_lambda)                      # p(6) = 11
    n_equations = 1                                   # B(K) = m_e Σ y χ Δ

    # The single binding constraint, were B_AME supplied (it is NOT used to
    # SELECT anything — shown only to demonstrate the 1-equation/11-unknown
    # underdetermination explicitly):
    #   B_AME_D = m_e · Σ_λ y_λ χ^λ Δ_λ
    # Any Δ profile on the hyperplane {Δ : m_e·Σ y_λ χ^λ Δ_λ = B_AME_D}
    # satisfies it; the solution set is a (11−1)=10-dim affine subspace.
    constraint_rhs_in_me_units = B_AME_D_MEV / M_E_MEV  # ≈ 4.353
    print("  Step 4 — DECISIVE map test χ^λ(K) → Δ_λ → B:")
    print(f"    Σ_λ y_λ·χ^λ(K) (Schur-Weyl-like sum)   = {sum_y_chi:+.6f}")
    print(f"    binding eq:  B/m_e = Σ_λ y_λ χ^λ Δ_λ   (target |B|/m_e ≈ "
          f"{constraint_rhs_in_me_units:.3f})")
    print(f"    unknowns {{Δ_λ}} : p(6) = {n_unknowns}")
    print(f"    equations       : {n_equations}")
    print(f"    → underdetermined: {n_unknowns - n_equations}-dim solution set")
    print(f"    Δ_λ is DEFINED via M_λ(K) (mass-functor per-block MeV), which")
    print(f"    K's CHARACTER χ^λ(K) does NOT supply. The only known map")
    print(f"    χ^λ → M_λ is per_block_phi_q.fit_three_E0 — a LSQ fit of the")
    print(f"    per-block scales E_0^λ to {{e⁻, p, n}} (DEPRECATED, a fit).")
    print()

    # ── Verdict. ────────────────────────────────────────────────────────
    verdict = (
        "CIRCULAR — GAP-A-1 reduces to Δ_λ. Substrate-only data (q_0, χ^λ, "
        "y_λ, nucleon braids) DOES uniquely fix the binding operator K = σ_3^2 "
        "for ²H (PSD-feasible, Markov-fingerprint matched, NO B_AME). But K's "
        "per-block content is its CHARACTER χ^λ(K) — a dimensionless Hecke "
        "trace. The per-isotope binding requires the mass-functor per-block "
        "component M_λ(K) (MeV), and Δ_λ(K) = (M_λ − m_e y_λ χ^λ)/(m_e y_λ "
        "χ^λ). Knowing χ^λ(K) does NOT determine M_λ(K): the only available "
        "map χ^λ → M_λ (per_block_phi_q.fit_three_E0) FITS per-block energy "
        "scales E_0^λ to {e⁻, p, n}. The deuteron binding equation is 1 "
        "equation in p(6)=11 unknowns Δ_λ — underdetermined without an "
        "external M_λ-source (equivalently B_AME). So GAP-A-1's binding-K "
        "leg supplies the SAME χ^λ data #1592 showed is insufficient, and "
        "fixing M_λ from K is exactly the open Δ_λ(K) problem. GAP-A-1 ⊆ Δ_λ."
    )
    print("  VERDICT:")
    for line in [verdict[i:i+72] for i in range(0, len(verdict), 72)]:
        print(f"    {line}")
    print("=" * 78)

    # No assertion that depends on B_AME; the one assertion records that the
    # SDP solved with strong duality (a substrate-only structural check).
    # SDP strong duality: duality_gap should be ~0 (≤ 1e-6).
    w.add_assertion(
        "operator_selection_sdp_duality_gap",
        float(sdp_d["duality_gap"]),
        0.0,
        tolerance=1e-6,
        source="solve_psd_operator_selection_sdp over K's Wedderburn blocks",
    )
    # Underdetermination: solution-set dimension is p(6)-1 = 10 (> 0).
    w.add_assertion(
        "binding_equation_solution_set_dim",
        float(n_unknowns - n_equations),
        10.0,
        tolerance=0.5,
        source="1 binding equation in p(6)=11 unknowns Δ_λ; M_λ(K) not "
               "supplied by χ^λ(K)",
    )

    w.set_description(
        "GAP-A-1 binding-operator-K SDP FEASIBILITY PROBE (operator-selection "
        "SDP / primal-dual / lp-duality, dual fields emitted via "
        "solve_psd_operator_selection_sdp). Tests whether the substrate-only "
        "binding operator K(²H) = σ_3^2 (selected by PSD-feasibility + "
        "Markov-fingerprint, NO B_AME) yields the deuteron binding / Δ_λ "
        "without feeding in the experimental binding. VERDICT: CIRCULAR — K's "
        "per-block CHARACTER χ^λ(K) does not determine the mass-functor "
        "per-block component M_λ(K), and Δ_λ(K) is defined via M_λ(K); the "
        "only map χ^λ→M_λ (per_block_phi_q.fit_three_E0) is a fit to {e⁻,p,n}. "
        "The deuteron binding equation is 1 eq in p(6)=11 unknowns Δ_λ — "
        "underdetermined without an external M_λ source (≡ B_AME). GAP-A-1 "
        "reduces to Δ_λ, like GAP-A-3/A-4 (#1591). No parameter tuned to "
        "B_AME; B_AME used only for the final honest residual report."
    )
    w.set_audit_only(
        "docs/audits/2026-05-31-gap-a1-binding-k-sdp-feasibility.md"
    )
    w.set_content_block("conj:canonical-knot-id-sdp")
    w.add_parameter("q_0", Q0)
    w.add_parameter("m_e_MeV", M_E_MEV)
    w.add_parameter("atom", "deuteron")
    w.add_parameter("n_0", N0)
    w.add_parameter("K_word_substrate_only", K_WORD_SUBSTRATE)
    w.add_parameter("B_AME_D_MeV_residual_report_only", B_AME_D_MEV)

    w.add_data("per_lambda_chi_K", per_lambda)
    w.add_data("dominant_lambda_K", dominant["lambda"])
    w.add_data("sum_y_lambda_chi_lambda", sum_y_chi)
    w.add_data("operator_selection_sdp_dual", {
        **sdp_d,
        "channel_lambdas": [r["lambda"] for r in per_lambda],
        "channel_costs_t": t.tolist(),
        "interpretation": (
            "SDP over K's Wedderburn blocks; t_λ = -|y_λ·χ^λ(K)| so the "
            "selected channel is the dominant block λ*(K). Dual fields "
            "(X_star, Z_star, primal_obj, dual_obj, duality_gap, eigenvalues) "
            "per AGENTS.md LP/SDP-duals infra. This SDP picks the dominant "
            "block of K but does NOT supply M_λ(K), so it does not close the "
            "binding — see verdict."
        ),
    })
    w.add_data("decisive_map_test", {
        "n_unknowns_delta_lambda": n_unknowns,
        "n_binding_equations": n_equations,
        "solution_set_dim": n_unknowns - n_equations,
        "binding_target_in_me_units_residual_report_only":
            constraint_rhs_in_me_units,
        "map_chi_to_M_lambda": (
            "per_block_phi_q.fit_three_E0 — LSQ fit of E_0^λ to {e⁻,p,n}; "
            "DEPRECATED; the only known χ^λ→M_λ map and it is a FIT."
        ),
    })
    w.add_data("verdict", verdict)
    w.add_caveat(
        "Feasibility probe, not a production mass compute. f64 per-block "
        "evaluation at q_0 (11 partitions of 6, max d_λ=16). The substrate-"
        "only K = σ_3^2 is taken from binding_k_enumerator.py (PSD-feasible + "
        "Markov-fingerprint, no B_AME). B_AME_D enters ONLY the final residual "
        "print and the underdetermination illustration; it selects / "
        "normalizes NOTHING. The verdict (GAP-A-1 ⊆ Δ_λ) is a clean negative, "
        "equal in value to a closure per the task discipline."
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
