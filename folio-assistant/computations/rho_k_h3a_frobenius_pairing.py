#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer; symbolic-q polynomials
# live upstream in y_lambda_wenzl_bridge / hoefsmit_symbolic / Markov-trace witnesses.
"""ρ_K refinement via the Frobenius-pairing minimum-norm closure — Option G.

Sibling of #564 / #602 / #603 / #609 in the Δ_λ derivation race tracked
under PR #600.  Where Options A (Occam singleton), B (co-Casimir
1/dim_q), C (Demazure), D (LP shadow), and F (Wenzl-bridge augmented)
each propose a *heuristic* selector, **Option G derives Δ_λ from the
Frobenius pairing structure alone**, with no fit and no calibration
beyond the existing CAL-3 (m_e, m_p, m_n).

CATEGORICAL DERIVATION (Option G)
=================================

(H_n(q), τ) is a symmetric Frobenius algebra with pairing

    ⟨a, b⟩_F  :=  τ(a · b)   = (Markov trace).

The center is Z(H_n(q)) = ⊕_{λ ⊢ n} R · p_λ with

    ⟨p_λ, p_μ⟩_F  =  δ_{λ μ} · y_λ · d_λ                        (★)

where d_λ = number of standard Young tableaux of λ and y_λ is the
Wenzl-bridge weight.  (Plug a = b = p_λ into ⟨,⟩_F: τ(p_λ²) = τ(p_λ)
because p_λ is idempotent, and τ(p_λ) = y_λ · χ^λ(1) = y_λ · d_λ.)

**Step 1 — project β_K into Z(H_n(q)).**
The orthogonal projection of β_K onto the center w.r.t. ⟨,⟩_F is

    β_K^{(Z)}  =  Σ_λ  (⟨β_K, p_λ⟩_F / ⟨p_λ, p_λ⟩_F) · p_λ
              =  Σ_λ  (y_λ χ^λ(β_K) / (y_λ d_λ)) · p_λ
              =  Σ_λ  (χ^λ(β_K) / d_λ) · p_λ.

**Step 2 — solve the underdetermined mass equation by min-norm.**
Δ_λ(K) is the per-block component of an element δ_K ∈ Z(H_n(q))
satisfying

    ⟨β_K, δ_K⟩_F  =  Σ_λ y_λ χ^λ(β_K) Δ_λ  =  -B(K) / m_e.

Among all δ_K ∈ Z satisfying this single linear constraint, the
**minimum Frobenius norm** element is unique (orthogonal-projection
onto a 1-dim affine subspace) and given by the Lagrange-multiplier
solution

    δ_K  =  (-B/m_e) / ⟨β_K, β_K^{(Z)}⟩_F  ·  β_K^{(Z)}.

Reading off the components δ_K = Σ_λ Δ_λ^G · p_λ gives the
**Frobenius-pairing-derived Δ_λ**:

      ┌─────────────────────────────────────────────────────────┐
      │     Δ_λ^G(K)  =  -B(K)/m_e   ·  χ^λ(β_K)                │
      │                  ─────────      ─────────                │
      │                     S_K            d_λ                   │
      │                                                          │
      │     S_K  :=  Σ_μ y_μ χ^μ(β_K)² / d_μ                     │
      │                                                          │
      │              =  ⟨β_K, β_K^{(Z)}⟩_F   (Frobenius norm² of │
      │                                       central projection)│
      └─────────────────────────────────────────────────────────┘

**STRUCTURAL FEATURES of Option G** (that distinguish it from siblings):

  - **Vortex-aware.**  Δ_λ depends on β_K via χ^λ(β_K) — different
    nuclei get different Δ_λ profiles.  Options B (co-Casimir) and F
    (Wenzl-bridge constant) both give Δ_λ independent of K.

  - **Closed form, no heuristic.**  The minimum-Frobenius-norm
    principle is the L² analogue of basis pursuit; it is the unique
    least-squares solution given (i) a single linear constraint,
    (ii) the requirement δ_K ∈ Z(H_n(q)), and (iii) the Frobenius
    pairing as the inner product on H_n(q).

  - **Frobenius norm of δ_K.**  ‖δ_K‖_F²  =  τ(δ_K²)  =
    Σ_λ y_λ d_λ (Δ_λ^G)²  =  (B(K)/m_e)² / S_K.  Smaller S_K ⇒ larger
    ‖δ_K‖_F (binding requires more "central mass").

PIPELINE
========

For the deuteron (n = 6, p(6) = 11) the script:

  1. Loads y_λ(q_0), χ^λ(β_D), |tr_M(β_D)|, B(D)/m_e from the existing
     Occam witness ``rho-k-h3a-refinement.witness.json`` (re-uses the
     50-dps mpmath computations verbatim).
  2. Computes d_λ via the hook-length formula.
  3. Computes S = Σ_μ y_μ χ^μ(β_D)² / d_μ.
  4. Reports Δ_λ^G(D) = (target / S) · χ^λ / d_λ for each λ ⊢ 6.
  5. Sanity-checks the binding equation: Σ_λ y_λ χ^λ Δ_λ^G ≡ target
     (residual ≈ machine ε at 50 dps).
  6. Side-by-side comparison to Options A (Occam singleton), F
     (Wenzl-bridge constant) including each option's Frobenius norm
     ‖δ_K‖_F².

Cross-atom extension to T / ³He (n = 9, p(9) = 30) and ⁴He (n = 12,
p(12) = 77) is mechanically the same formula but requires full
per-λ χ^λ data which is not in the canonical witness today
(``chi-tritium-h9.witness.json`` and ``chi-helium-3-h9.witness.json``
are only partial; ⁴He has no chi cache at all).  Deferred to a
follow-up that extends those caches.

REFERENCES
==========

  - Symmetric Frobenius algebras / Markov trace as Frobenius pairing:
    ``def:frobenius-hopf-substrate``, ``thm:jones-markov-trace``.
  - Sibling options:
    A: ``rho_k_h3a_refinement.py`` (PR #564),
    B: ``rho_k_h3a_co_casimir.py`` (PR #602),
    C: Demazure-fiber Markov (e77a4b4d),
    D: ``rho_k_h3a_lp_dual.py`` (PR #603),
    F: ``rho_k_h3a_wenzl_bridge.py`` (PR #609).
  - Audit: ``docs/audits/2026-05-09-mass-table-fitting-audit.md``.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
# `hook_lengths` and `d_lambda` (= dim_specht, # of SYT, hook-length
# formula) imported from the shared helper rather than re-implemented
# locally — Gemini PR #613 review (dedup across the 4 race scripts).
from murnaghan_nakayama import hook_lengths, d_lambda  # noqa: E402, F401


def main() -> int:
    print("=" * 96)
    print("  ρ_K H_{3A} Wedderburn refinement — DEUTERON, Option G")
    print("  (Frobenius-pairing minimum-norm closure)")
    print("  Sibling of #564 (A=Occam) / #602 (B=co-Casimir) /")
    print("  #603 (D=LP shadow) / #609 (F=Wenzl-bridge)")
    print("=" * 96)

    # WitnessBuilder is instantiated HERE (start of main) so durationMs
    # captures the full computation runtime — per Copilot PR #611 review.
    # The witness-data calls below populate it; final .save() is at end.
    builder = (
        WitnessBuilder(
            name="rho-k-h3a-frobenius-pairing",
            engine="mpmath",
        )
        .set_description(
            "Option G in the Δ_λ derivation race: Δ_λ derived from the "
            "Frobenius-pairing minimum-norm closure on Z(H_n(q)). "
            "Δ_λ^G(K) = (-B(K)/m_e) · (1/S_K) · χ^λ(β_K) / d_λ, where "
            "S_K = Σ_μ y_μ χ^μ(β_K)² / d_μ is the Frobenius norm² of "
            "β_K's projection onto the center.  Sibling of PR #600's "
            "race; structurally distinct from A/B/C/D/F because Δ_λ "
            "depends on β_K (vortex-aware).  Deuteron-only for now; "
            "T / ³He / ⁴He extension requires full per-λ chi caches."
        )
    )

    # ── Step 1: load Occam baseline (= source of truth for y_λ, χ^λ) ──
    occam_path = _pb.witness_path("rho-k-h3a-refinement.witness.json", HERE)
    if not occam_path.exists():
        raise RuntimeError(
            f"Occam baseline {occam_path.name} not found; run "
            "`python3 rho_k_h3a_refinement.py` first to generate it."
        )
    occam_blob = json.loads(occam_path.read_text())
    data = occam_blob["data"]

    abs_tr_M = mp.mpf(data["abs_tr_M_at_q0_50dps"])
    rho_K_LO = mp.mpf(data["rho_K_LO"])
    rho_K_codata = mp.mpf(data["rho_K_codata"])
    delta_rho = mp.mpf(data["delta_rho_residual"])
    target = delta_rho * abs_tr_M  # = -B(D)/m_e

    print(f"\n  |tr_M(β_D)|        = {mp.nstr(abs_tr_M, 25)}")
    print(f"  ρ_K^LO             = {mp.nstr(rho_K_LO, 18)}")
    print(f"  ρ_K^CODATA         = {mp.nstr(rho_K_codata, 18)}")
    print(f"  Δρ_K (residual)    = {mp.nstr(delta_rho, 18)}")
    print(f"  target = Δρ·|tr_M| = {mp.nstr(target, 18)}  (= -B(D)/m_e)")

    # ── Step 2: per-λ data + d_λ ──────────────────────────────────────
    print(f"\n  Per-λ table (deuteron, n=6, p(6)=11 partitions):")
    print(f"  {'partition':<22}{'d_λ':>5}{'y_λ':>20}{'χ^λ(β_D)':>20}"
          f"{'y_λ χ^λ':>20}{'(y_λ χ^λ)²/d_λ':>22}")
    print("  " + "-" * 109)

    rows: list[dict] = []
    for r in data["per_lambda"]:
        lam = tuple(r["partition"])
        dl = d_lambda(lam)
        y = mp.mpf(r["y_lambda_at_q0"])
        chi = mp.mpf(r["chi_lambda_beta_D_at_q0"])
        y_chi = mp.mpf(r["y_chi_product"])
        contrib_S = y * chi * chi / dl  # = y_λ χ^λ² / d_λ  (per Gemini PR #611 review — earlier "·y/1" was an algebra typo)
        rows.append({
            "partition": lam,
            "d_lambda": dl,
            "y_lambda": y,
            "chi_lambda": chi,
            "y_chi": y_chi,
            "S_contrib": contrib_S,
        })
        print(f"  {str(list(lam)):<22}{dl:>5}{mp.nstr(y, 8):>20}"
              f"{mp.nstr(chi, 8):>20}{mp.nstr(y_chi, 8):>20}"
              f"{mp.nstr(contrib_S, 8):>22}")

    # ── Step 3: Frobenius-norm² of central projection ────────────────
    S = mp.mpf(0)
    for r in rows:
        S += r["S_contrib"]

    print(f"\n  S = Σ_μ y_μ χ^μ(β_D)² / d_μ = {mp.nstr(S, 18)}")
    print(f"  ⟨β_K, β_K^(Z)⟩_F = S         = {mp.nstr(S, 18)}")
    print(f"  (Frobenius norm² of the central projection)")

    # ── Step 4: Δ_λ^G via the Frobenius-pairing closure ─────────────
    print(f"\n  Δ_λ^G(D)  =  (target / S) · χ^λ(β_D) / d_λ")
    print(f"  {'partition':<22}{'χ^λ/d_λ':>20}{'Δ_λ^G':>20}{'y_λ χ^λ Δ_λ^G':>22}")
    print("  " + "-" * 84)

    sum_check = mp.mpf(0)
    for r in rows:
        chi_over_d = r["chi_lambda"] / r["d_lambda"]
        delta_G = target * chi_over_d / S
        contrib = r["y_chi"] * delta_G
        sum_check += contrib
        r["chi_over_d"] = chi_over_d
        r["delta_G"] = delta_G
        r["contribution"] = contrib
        print(f"  {str(list(r['partition'])):<22}{mp.nstr(chi_over_d, 8):>20}"
              f"{mp.nstr(delta_G, 10):>20}{mp.nstr(contrib, 8):>22}")

    print("  " + "-" * 84)
    print(f"  {'Σ y_λ χ^λ Δ_λ^G':<42}{mp.nstr(sum_check, 18):>42}")
    print(f"  {'target = Δρ·|tr_M|':<42}{mp.nstr(target, 18):>42}")
    residual = sum_check - target
    print(f"  {'residual':<42}{mp.nstr(residual, 6):>42}  (= 0 by construction at 50 dps)")

    # ── Step 5: Frobenius norm of δ_K ────────────────────────────────
    # ‖δ_K‖_F²  =  τ(δ_K²)  = Σ_λ τ(p_λ) · Δ_λ²  = Σ_λ y_λ d_λ Δ_λ²
    # which equals (target/S)² · Σ_λ y_λ (χ^λ/d_λ)² · d_λ
    #            = (target/S)² · Σ_λ y_λ χ^λ² / d_λ
    #            = (target/S)² · S  =  target² / S.
    norm_G_sq = target * target / S

    print(f"\n  Frobenius norm² of δ_K (Option G):")
    print(f"    ‖δ_K^G‖_F²  =  target² / S  =  {mp.nstr(norm_G_sq, 12)}")

    # ── Step 6: comparison to siblings ────────────────────────────────
    occam_pick = data["occam_pick"]
    occam_lam = tuple(occam_pick["partition"])
    occam_delta = mp.mpf(occam_pick["Delta_lambda"])
    # Occam singleton: only one Δ_λ ≠ 0 at λ = occam_lam.
    # ‖δ^A‖_F² = y_{λ_A} · d_{λ_A} · Δ_A²
    occam_dl = d_lambda(occam_lam)
    occam_y = next(mp.mpf(r["y_lambda_at_q0"])
                   for r in data["per_lambda"]
                   if tuple(r["partition"]) == occam_lam)
    norm_A_sq = occam_y * occam_dl * occam_delta * occam_delta

    # Wenzl-bridge constant: Δ_λ = Δρ_D ∀ λ
    # ‖δ^F‖_F² = Σ_λ y_λ d_λ · Δρ²  =  Δρ² · Σ_λ y_λ d_λ.
    # And τ(1) = Σ_λ y_λ d_λ = 1 (Schur–Weyl normalization for tr_M(1) = 1).
    sum_y_d = mp.mpf(0)
    for r in rows:
        sum_y_d += r["y_lambda"] * r["d_lambda"]
    norm_F_sq = delta_rho * delta_rho * sum_y_d

    print(f"\n  Sibling comparison (Frobenius norm² of δ_K):")
    print(f"    Option A (Occam singleton, λ={list(occam_lam)})")
    print(f"      Δ_λ = {mp.nstr(occam_delta, 10)}  on a single block")
    print(f"      ‖δ^A‖_F² = y_λ · d_λ · Δ²  =  {mp.nstr(norm_A_sq, 10)}")
    print(f"    Option F (Wenzl-bridge, Δ_λ = Δρ_D constant)")
    print(f"      Δ_λ = {mp.nstr(delta_rho, 10)}  ∀ λ")
    print(f"      ‖δ^F‖_F² = Δρ² · Σ_λ y_λ d_λ  =  {mp.nstr(norm_F_sq, 10)}")
    print(f"      (Σ_λ y_λ d_λ = {mp.nstr(sum_y_d, 12)} — should be 1 by tr_M(1)=1)")
    print(f"    Option G (Frobenius pairing, this PR)")
    print(f"      Δ_λ = (target/S) · χ^λ/d_λ  (vortex-aware)")
    print(f"      ‖δ^G‖_F² = target² / S  =  {mp.nstr(norm_G_sq, 10)}")
    print()
    # Min-norm property: G should have the SMALLEST Frobenius norm
    # among all δ ∈ Z(H_n(q)) that satisfy the constraint.
    print(f"  Min-norm verification:")
    if norm_G_sq <= norm_A_sq and norm_G_sq <= norm_F_sq:
        print(f"    ✓ ‖δ^G‖_F² is the smallest of the three "
              f"(min-norm property holds by construction).")
    else:
        print(f"    ✗ ‖δ^G‖_F² is NOT the smallest — error in derivation!")

    # ── Step 7: populate the witness (builder created at top of main) ─
    # Renamed `frobenius_norm_S_squared` → `S_central_projection` per
    # Copilot PR #611 review (S itself IS a squared norm; the "_squared"
    # suffix was misleading).
    (
        builder
        .add_data("computation_status", "deuteron")
        .add_data("atom", "deuteron")
        .add_data("Z", 1)
        .add_data("N", 1)
        .add_data("A", 2)
        .add_data("n_strands", 6)
        .add_data("n_partitions", len(rows))
        .add_data("source_witness", "rho-k-h3a-refinement.witness.json")
        .add_data("abs_tr_M_at_q0_50dps", str(abs_tr_M))
        .add_data("rho_K_LO", str(rho_K_LO))
        .add_data("rho_K_codata", str(rho_K_codata))
        .add_data("delta_rho_residual", str(delta_rho))
        .add_data("target_yc_delta_sum", str(target))
        .add_data(
            "S_central_projection",
            {
                "value": str(S),
                "formula": "S = Σ_μ y_μ · χ^μ(β_D)² / d_μ",
                "interpretation": (
                    "S itself is a squared Frobenius norm: "
                    "S = ⟨β_K, β_K^(Z)⟩_F = ‖β_K^(Z)‖_F², the "
                    "Frobenius norm² of β_K's orthogonal projection onto "
                    "Z(H_n(q)).  Smaller S ⇒ larger ‖δ_K‖_F (binding "
                    "requires more 'central mass')."
                ),
            }
        )
        .add_data(
            "delta_lambda_formula",
            {
                "expression": "Δ_λ^G(K) = (-B(K)/m_e) / S_K · χ^λ(β_K) / d_λ",
                "derivation": (
                    "Min-Frobenius-norm element δ_K ∈ Z(H_n(q)) "
                    "satisfying ⟨β_K, δ_K⟩_F = -B(K)/m_e.  Lagrange "
                    "multiplier on a 1-dim affine subspace ⇒ unique "
                    "orthogonal-projection answer."
                ),
                "vortex_aware": True,
                "free_parameters": 0,
            }
        )
        .add_data(
            "per_lambda",
            [
                {
                    "partition": list(r["partition"]),
                    "d_lambda": r["d_lambda"],
                    "y_lambda_at_q0": str(r["y_lambda"]),
                    "chi_lambda_beta_D_at_q0": str(r["chi_lambda"]),
                    "y_chi_product": str(r["y_chi"]),
                    "chi_over_d_lambda": str(r["chi_over_d"]),
                    "Delta_lambda_frobenius_pairing": str(r["delta_G"]),
                    "y_chi_Delta_contribution": str(r["contribution"]),
                }
                for r in rows
            ]
        )
        .add_data(
            "closure_check",
            {
                "sum_y_chi_Delta": str(sum_check),
                "target": str(target),
                "residual": str(residual),
                "match_at_machine_eps": abs(residual) < mp.mpf(10) ** -(mp.mp.dps - 10),
            }
        )
        .add_data(
            "frobenius_norm_squared",
            {
                "option_G_this_PR": str(norm_G_sq),
                "option_A_occam_singleton": str(norm_A_sq),
                "option_F_wenzl_bridge_constant": str(norm_F_sq),
                "min_norm_holds": (
                    norm_G_sq <= norm_A_sq and norm_G_sq <= norm_F_sq
                ),
                "interpretation": (
                    "The Frobenius-pairing-derived δ^G has the smallest "
                    "norm among all δ ∈ Z(H_n(q)) satisfying the "
                    "binding constraint.  Options A and F are "
                    "feasible but suboptimal in this norm."
                ),
            }
        )
        .add_data(
            "open_followup",
            {
                "task": (
                    "Extend Option G to T (n=9, p(9)=30), ³He (n=9), "
                    "⁴He (n=12, p(12)=77).  Mechanically the same "
                    "formula; needs full per-λ χ^λ data which is not "
                    "yet in the canonical witness "
                    "(chi-tritium-h9.witness.json and chi-helium-3-h9 "
                    "are partial; ⁴He has no chi cache)."
                ),
                "status": "deferred to follow-up PR",
            }
        )
        .add_assertion(
            name="frobenius_pairing_closure_at_50dps",
            computed=float(abs(residual)),
            expected=0.0,
            tolerance=1e-40,
        )
        # Min-norm assertions encoded per Gemini + Copilot PR #611 review:
        # `add_assertion` checks abs(computed - expected) ≤ tolerance, so
        # to ENFORCE the inequality `‖δ^G‖² ≤ ‖δ^X‖²` we set
        # `expected = min(norm_G, norm_X)`.  When G ≤ X, expected = G ⇒
        # check passes; when G > X, expected = X ≠ G ⇒ check fails by
        # |G - X| > 1e-12.  The earlier `tolerance = expected * 2` was a
        # loose proximity check that didn't enforce the inequality.
        .add_assertion(
            name="min_norm_vs_occam_singleton",
            computed=float(norm_G_sq),
            expected=float(min(norm_G_sq, norm_A_sq)),
            tolerance=1e-12,
            source="‖δ^G‖² should be ≤ ‖δ^A‖² (min-norm property)",
        )
        .add_assertion(
            name="min_norm_vs_wenzl_bridge_constant",
            computed=float(norm_G_sq),
            expected=float(min(norm_G_sq, norm_F_sq)),
            tolerance=1e-12,
            source="‖δ^G‖² should be ≤ ‖δ^F‖² (min-norm property)",
        )
    )
    out_path = builder.save()
    print(f"\n  Wrote {out_path.name} ({out_path.stat().st_size} bytes).")
    print("=" * 96)
    print(f"  OUTCOME: derived (no fit, no calibration); residual = {mp.nstr(residual, 6)}")
    print("=" * 96)
    return 0


if __name__ == "__main__":
    sys.exit(main())
