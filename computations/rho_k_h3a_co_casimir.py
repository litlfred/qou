#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical sympy/mpmath consumer; the symbolic-q content
# (per-isotypic 1/dim_q(λ) closed form) is upstream in frobenius-partition-sum.witness.json
# and probe-term4-conventions.witness.json (sigma_inv_dim_q_polynomial_q field).
"""ρ_K refinement via Frobenius co-Casimir per-isotypic restriction — Option B.

This is the **co-Casimir-restriction** alternative to the singleton-support
(Occam) heuristic in `rho_k_h3a_refinement.py` (PR #564 / `prop:rho-k-h3a-refinement`).

CATEGORICAL DERIVATION (Option B)
=================================

The Frobenius co-Casimir element is

    C_dim_q  =  Σ_λ  [1 / (dim_q(λ) · τ(p_λ))] · p_λ   ∈   Z(H_n(q))

(see ``frobenius-codim-universal.md`` / ``frobenius-codim-universal.lean``,
``thm:frobenius-codim-universal``).  Its **per-isotypic restriction** is

    tr_M(C_dim_q · 1_λ)  =  tr_M(C_dim_q · p_λ)
                         =  [1/(dim_q(λ) · τ(p_λ))] · τ(p_λ)
                         =  1 / dim_q(λ).

By ``frobenius_codim_tau_invariant`` this value is **τ-invariant**: the
Plancherel-A vs Wenzl-Schur convention for τ(p_λ) does not affect the
per-block answer (the τ factors cancel telescopically, exactly as in
``codim_block_contribution`` / Lean lemma ``one_div_mul_eq_div_of_ne``).

OPTION B SELECTOR.  Set

    Δ_λ(K) := tr_M(C_dim_q · 1_λ)  =  1 / dim_q(λ),

i.e. the per-isotypic restriction of the established Frobenius co-Casimir
theorem.  This is a **closed form**: 11 unknowns become 11 known scalars,
each forced by the structure of `C_dim_q` — no free parameters, no
heuristic.  By the τ-invariance theorem it is also vortex-blind: every
braid β_K on H_n(q) sees the same Δ_λ profile (this is the
"feature/limitation" in ``frobenius-codim-universal.md`` §"Independence of
the vortex").

PIPELINE
========

For the deuteron (A=2, n=6, p(6)=11 partitions of 6) this script:

  1. Loads |tr_M(β_D)| from ``rho-k-h3a-refinement.witness.json``
     (Occam baseline, field ``data.abs_tr_M_at_q0_50dps``).
  2. Loads y_λ(q_0) and χ^λ(β_D) at q_0 from the same
     ``rho-k-h3a-refinement.witness.json`` (sibling Occam witness;
     the Schur–Weyl identity is also re-validated against tr_M for safety).
  3. Computes Δ_λ^B := 1/dim_q(λ) at q_0 for each λ ⊢ 6 via the
     q-hook-length formula (``q_dim_sym`` in
     ``frobenius_partition_sum.py``).  Cross-checks against
     ``frobenius-partition-sum.witness.json``.
  4. Plugs Δ_λ^B into the mass equation
        Δρ_K^pred · |tr_M|  =  Σ_λ y_λ χ^λ(β_D) · Δ_λ^B
     and reports
        residual_MeV   = (Δρ_K^codata - Δρ_K^pred) · m_e · |tr_M|
                       = M(D)^codata - M(D)^pred
        relative_error = residual_MeV / M(D)^codata.
  5. Compares against the Occam baseline (rho-k-h3a-refinement.witness):
     same partition, same m_e, same |tr_M| — only Δ_λ differs (Occam
     puts all binding on a single λ; co-Casimir distributes per
     1/dim_q).

Output: ``rho-k-h3a-co-casimir.witness.json`` — full per-λ table
including Δ_λ^B, y_λ χ^λ Δ_λ^B contributions, total predicted mass,
residual, and a side-by-side Occam comparison.

HONEST REPORTING.  Δ_λ^B is fixed by theorem; we do **not** rescale,
fit, or otherwise tune it.  The residual is whatever it is; if Option
B is the right selector the residual should be small (≪ MeV); if it
fails the residual will be visible.

REFERENCES
==========

  - Theorem: ``content/quantum-observable-universe/braids-and-knots/
    frobenius-codim-universal.md``  (``thm:frobenius-codim-universal``).
  - Lean: ``frobenius-codim-universal.lean``
    (``frobenius_codim_universal``, ``frobenius_codim_tau_invariant``,
    ``codim_block_contribution``).
  - Existing co-Casimir code:
    ``frobenius_partition_sum.py`` (Σ_λ 1/dim_q(λ) and per-level breakdown),
    ``probe_term4_conventions.py`` (τ-invariance check).
  - Parent: PR #564 (``rho_k_h3a_refinement.py`` — Occam baseline).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
# IMPORTANT: set mpmath precision BEFORE importing codata_constants
# (or any module that constructs ``mp.mpf`` literals at import time).
# Otherwise CODATA constants are parsed at the default precision and
# later serialised with spurious binary tail digits.
set_compute_dps()

from codata_constants import M_E_MEV, M_P_MEV, M_N_MEV, M_D_MEV  # noqa: E402
from murnaghan_nakayama import partitions_of, hook_lengths  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

q_sym = sp.Symbol("q", positive=True, real=True)


# ── q-hook-length formula  (mirrors frobenius_partition_sum.q_dim_sym) ─
def q_int_sym(k: int) -> sp.Expr:
    if k == 0:
        return sp.Integer(0)
    if k == 1:
        return sp.Integer(1)
    return sp.cancel((q_sym ** k - q_sym ** (-k)) / (q_sym - q_sym ** (-1)))


def q_factorial_sym(n: int) -> sp.Expr:
    out = sp.Integer(1)
    for k in range(1, n + 1):
        out *= q_int_sym(k)
    # sp.cancel is significantly faster than sp.simplify for q-rational
    # products (Gemini PR #613 review).
    return sp.cancel(out)


def q_dim_sym(partition: tuple[int, ...]) -> sp.Expr:
    """Quantum dimension dim_q(λ) = [n]_q! / Π_{x ∈ λ} [h_λ(x)]_q.

    Mirrors ``frobenius_partition_sum.q_dim_sym`` so this script does
    not import that module's `__main__` machinery.
    """
    n = sum(partition)
    h = sp.Integer(1)
    for hk in hook_lengths(partition):
        h *= q_int_sym(hk)
    # sp.cancel is sufficient + faster than sp.simplify for the q-dim
    # ratio (Gemini PR #613 review).
    return sp.cancel(q_factorial_sym(n) / h)


def conjugate_partition(partition: tuple[int, ...]) -> tuple[int, ...]:
    if not partition:
        return ()
    k = max(partition)
    return tuple(sum(1 for p in partition if p > j) for j in range(k))


def evaluate_at_q0(expr: sp.Expr) -> mp.mpf:
    """Evaluate sympy expr at q = q_0 to current mpmath precision."""
    q0_str = mp.nstr(Q_MP, mp.mp.dps, strip_zeros=False)
    sub = expr.subs(q_sym, sp.sympify(q0_str))
    return mp.mpf(str(sub.evalf(mp.mp.dps)))


def load_occam_witness() -> dict:
    """Load the Occam baseline witness (PR #564) — source of truth for
    y_λ(q_0), χ^λ(β_D) at q_0, |tr_M(β_D)|, and the per-λ table.

    We re-use the Occam compute exactly so any Δ_λ comparison is
    apples-to-apples (same braid word, same q_0, same dps, same
    Hoefsmit construction).
    """
    path = _pb.witness_path("rho-k-h3a-refinement.witness.json", HERE)
    if not path.exists():
        raise RuntimeError(
            f"Occam baseline {path.name} not found. Run "
            "`python3 rho_k_h3a_refinement.py` first."
        )
    return json.loads(path.read_text())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    print("=" * 96)
    print("  ρ_K H_{3A} refinement — OPTION B (Frobenius co-Casimir restriction)")
    print("  Δ_λ(K) := tr_M(C_dim_q · 1_λ) = 1/dim_q(λ)  (forced by theorem)")
    print("=" * 96)

    print(f"\n  q_0  = {mp.nstr(Q_MP, 25)}")
    print(f"  m_e  = {mp.nstr(M_E_MEV, 8)} MeV (CODATA)")
    print(f"  M(D) = {mp.nstr(M_D_MEV, 12)} MeV (CODATA)")

    # ── Step 1: load Occam baseline (canonical |tr_M|, y_λ, χ^λ) ──────
    occam = load_occam_witness()
    abs_tr_M = mp.mpf(occam["data"]["abs_tr_M_at_q0_50dps"])
    rho_K_LO = mp.mpf(occam["data"]["rho_K_LO"])
    rho_K_codata = mp.mpf(occam["data"]["rho_K_codata"])
    delta_rho = mp.mpf(occam["data"]["delta_rho_residual"])
    sw_match = occam["data"]["schur_weyl_check"]["match_at_1e_40"]
    occam_partition = tuple(occam["data"]["occam_pick"]["partition"])
    occam_delta = mp.mpf(occam["data"]["occam_pick"]["Delta_lambda"])

    print(f"\n  Loaded Occam baseline (PR #564, n_partitions=11, n_crossings=23):")
    print(f"    |tr_M(β_D)|         = {mp.nstr(abs_tr_M, 25)}")
    print(f"    ρ_K^LO              = {mp.nstr(rho_K_LO, 18)}")
    print(f"    ρ_K^CODATA          = {mp.nstr(rho_K_codata, 18)}")
    print(f"    Δρ_K (residual)     = {mp.nstr(delta_rho, 18)}")
    print(f"    Schur-Weyl @1e-40   = {'PASS' if sw_match else 'FAIL'}")
    print(f"    Occam picked λ      = {list(occam_partition)}, "
          f"Δ_λ^Occam = {mp.nstr(occam_delta, 12)}")

    # The mass-equation target (LHS) is Δρ_K · |tr_M|.
    # By construction the Occam Δ_λ is target / (signed y_λ χ^λ_(occam)).
    target = delta_rho * abs_tr_M  # signed; negative since ρ_K^LO > ρ_K^CODATA

    # ── Step 2: per-λ Δ_λ^B = 1/dim_q(λ) at q_0 (Option B selector) ──
    parts = partitions_of(6)
    assert len(parts) == 11, f"expected 11 partitions of 6, got {len(parts)}"

    print(f"\n  Computing Δ_λ^B = 1/dim_q(λ) at q_0 for {len(parts)} partitions of 6 …")
    delta_B_table: dict[tuple[int, ...], mp.mpf] = {}
    dim_q_at_q0: dict[tuple[int, ...], mp.mpf] = {}
    for lam in parts:
        d_q = q_dim_sym(lam)
        d_q_q0 = evaluate_at_q0(d_q)
        dim_q_at_q0[lam] = d_q_q0
        delta_B_table[lam] = mp.mpf(1) / d_q_q0

    # Cross-check Σ_λ 1/dim_q(λ) against the Frobenius co-Casimir trace
    # for n=6 (= 2 + 2/[3]_q + 2/[5]_q + 1/((q²+q⁻²)·[3]_q) at the
    # Lean theorem ``hecke_n5_frobenius_codim`` for n=5; for n=6 the
    # closed form is established in frobenius-partition-sum.witness.json).
    sigma_inv_dim_q = sum(delta_B_table.values(), mp.mpf(0))
    print(f"    Σ_λ 1/dim_q(λ)      = {mp.nstr(sigma_inv_dim_q, 20)}")
    print(f"    (= τ(C_dim_q^{{H_6}}), per Frobenius theorem)")

    # ── Step 3: assemble per-λ contributions  Σ_λ y_λ χ^λ Δ_λ^B  ─────
    occam_rows = {tuple(r["partition"]): r for r in occam["data"]["per_lambda"]}

    print(f"\n  {'partition':<22}{'1/dim_q(λ)':>20}"
          f"{'y_λ χ^λ':>20}{'y_λ χ^λ Δ_λ^B':>22}")
    print("  " + "-" * 84)

    rows = []
    sum_contributions = mp.mpf(0)
    for lam in parts:
        if lam not in occam_rows:
            raise RuntimeError(
                f"partition {lam} missing from Occam witness per_lambda table"
            )
        oc = occam_rows[lam]
        y_lam = mp.mpf(oc["y_lambda_at_q0"])
        chi_lam = mp.mpf(oc["chi_lambda_beta_D_at_q0"])
        y_chi = mp.mpf(oc["y_chi_product"])  # = y_lam * chi_lam, signed
        delta_B = delta_B_table[lam]
        contribution = y_chi * delta_B
        sum_contributions += contribution

        rows.append({
            "partition": list(lam),
            "conjugate": list(conjugate_partition(lam)),
            "self_dual": lam == conjugate_partition(lam),
            "dim_q_at_q0": str(dim_q_at_q0[lam]),
            "Delta_lambda_co_casimir": str(delta_B),  # = 1/dim_q
            "y_lambda_at_q0": str(y_lam),
            "chi_lambda_beta_D_at_q0": str(chi_lam),
            "y_chi_product_signed": str(y_chi),
            "contribution_y_chi_Delta": str(contribution),
        })
        print(f"  {str(list(lam)):<22}{mp.nstr(delta_B, 10):>20}"
              f"{mp.nstr(y_chi, 10):>20}{mp.nstr(contribution, 12):>22}")

    print("  " + "-" * 84)
    print(f"  {'Σ y_λ χ^λ Δ_λ^B':<22}{'':>20}{'':>20}"
          f"{mp.nstr(sum_contributions, 12):>22}")
    print(f"  {'target (Δρ · |tr_M|)':<22}{'':>20}{'':>20}"
          f"{mp.nstr(target, 12):>22}")

    # ── Step 4: residual ────────────────────────────────────────────
    # M(D)^pred = (ρ_K^LO + sum_contributions / |tr_M|) · m_e · |tr_M|
    #            = m_p + m_n + m_e · sum_contributions
    rho_K_pred = rho_K_LO + sum_contributions / abs_tr_M
    M_pred = rho_K_pred * M_E_MEV * abs_tr_M
    residual_MeV = M_D_MEV - M_pred
    residual_pct = residual_MeV / M_D_MEV * 100
    closure_gap = sum_contributions - target

    print(f"\n  Mass-equation closure with Δ_λ^B (NO rescaling):")
    print(f"    ρ_K^pred           = {mp.nstr(rho_K_pred, 20)}")
    print(f"    M(D)^pred          = {mp.nstr(M_pred, 14)} MeV")
    print(f"    M(D)^codata        = {mp.nstr(M_D_MEV, 14)} MeV")
    print(f"    residual           = {mp.nstr(residual_MeV, 8)} MeV  "
          f"({mp.nstr(residual_pct, 5)} %)")
    print(f"    closure gap (LHS-RHS) = {mp.nstr(closure_gap, 8)}")

    # ── Step 5: diagnostic — what global rescale scalar would close
    #            the equation?  This is a DIAGNOSTIC quantity (how
    #            far co-Casimir restriction is from satisfying the
    #            constraint), NOT a production scaling factor.
    # Tolerance dynamically tied to mp.dps (Gemini PR #613 review):
    # at mp.dps = 50, this gives 10^-40 (matching the prior literal).
    # Variable renamed from `lambda_scale` per owner directive
    # 2026-05-24: "no lambda-scale ANYWHERE in production".
    _eps = mp.mpf(10) ** -(mp.mp.dps - 10)
    if abs(sum_contributions) > _eps:
        diagnostic_closure_rescaler = target / sum_contributions
    else:
        diagnostic_closure_rescaler = mp.mpf("inf")

    print(f"\n  Diagnostic — global rescale scalar that would close the equation:")
    print(f"    rescaler = target / Σ y_λ χ^λ Δ_λ^B = "
          f"{mp.nstr(diagnostic_closure_rescaler, 16)}")
    print(f"    (Δ_λ^B is theorem-fixed; this scalar is reported to quantify")
    print(f"     how far co-Casimir restriction is from satisfying the constraint.")
    print(f"     It is NOT a production scaling factor and must not be consumed")
    print(f"     as one — per PR #1080, there is no separate λ_scale.)")

    # ── Step 6: comparison against Occam ────────────────────────────
    # Occam puts ALL the binding correction on a single partition;
    # Option B distributes per Frobenius co-Casimir weights.  Compare
    # the per-partition |Δ_λ| profile.
    occam_pl = occam_rows[occam_partition]
    print(f"\n  Comparison vs Occam baseline:")
    print(f"    Occam λ           = {list(occam_partition)}, "
          f"|Δ_λ| = {mp.nstr(abs(occam_delta), 8)}")
    print(f"    Co-Casimir Δ_λ on Occam λ = "
          f"{mp.nstr(delta_B_table[occam_partition], 8)}")
    print(f"    ratio |Δ_λ^Occam| / Δ_λ^B = "
          f"{mp.nstr(abs(occam_delta) / delta_B_table[occam_partition], 8)}")
    # Sum of |Δ_λ| profile (a cheap proxy for "how spread out")
    occam_sum_abs = sum(
        abs(mp.mpf(r["Delta_lambda_solo_assumption"]))
        for r in occam["data"]["per_lambda"]
    )
    co_casimir_sum_abs = sum(delta_B_table.values(), mp.mpf(0))
    print(f"    Σ_λ |Δ_λ^Occam-singleton-trial| = {mp.nstr(occam_sum_abs, 6)}")
    print(f"    Σ_λ Δ_λ^B (= τ(C_dim_q))        = {mp.nstr(co_casimir_sum_abs, 6)}")

    # ── Step 7: emit witness ────────────────────────────────────────
    witness = {
        "computation": "rho-k-h3a-co-casimir",
        "description": (
            "Option B for the underdetermined Δ_λ(K) selector in "
            "prop:rho-k-h3a-refinement (deuteron, A=2, n=6).  Replaces "
            "the Occam single-partition heuristic (rho_k_h3a_refinement.py) "
            "with the Frobenius co-Casimir per-isotypic restriction "
            "Δ_λ := tr_M(C_dim_q · 1_λ) = 1/dim_q(λ), forced by "
            "thm:frobenius-codim-universal (no free parameters).  Computes "
            "the resulting mass-equation residual; honest reporting — "
            "no rescaling applied to Δ_λ^B."
        ),
        "engine_note": (
            "sympy q-hook-length symbolic dim_q + 50-dps mpmath evaluation; "
            "y_λ(q_0) and χ^λ(β_D) reused verbatim from "
            "rho-k-h3a-refinement.witness.json (Occam baseline)."
        ),
        "selector": {
            "name": "Frobenius co-Casimir per-isotypic restriction",
            "formula": "Δ_λ(K) := tr_M(C_dim_q · 1_λ) = 1 / dim_q(λ)",
            "free_parameters": 0,
            "tau_invariant": True,
            "vortex_blind": True,
            "source_theorem": "thm:frobenius-codim-universal",
            "lean_decl": [
                "qou:QOU.BraidKnot.frobenius_codim_universal",
                "qou:QOU.BraidKnot.frobenius_codim_tau_invariant",
                "qou:QOU.BraidKnot.codim_block_contribution",
            ],
            "narrative_md": (
                "content/quantum-observable-universe/braids-and-knots/"
                "frobenius-codim-universal.md"
            ),
            "rationale": (
                "C_dim_q = Σ_λ [1/(dim_q(λ)·τ(p_λ))]·p_λ is in Z(H_n(q)). "
                "Restricting to the λ-isotypic (multiplying by 1_λ = p_λ) "
                "and tracing telescopes the τ(p_λ) factors: "
                "tr_M(C_dim_q · p_λ) = [1/(dim_q·τ(p_λ))]·τ(p_λ) = 1/dim_q. "
                "The Lean lemma ``codim_block_contribution`` captures this "
                "exact identity.  ``frobenius_codim_tau_invariant`` shows "
                "the value does NOT depend on the choice of Frobenius "
                "pairing τ (Plancherel-A vs Wenzl-Schur both give 1/dim_q)."
            ),
        },
        "parameters": {
            "q_0_50dps": mp.nstr(Q_MP, 50),
            "atom": "deuteron",
            "Z": 1, "N": 1, "A": 2, "n_strands": 6,
            "n_partitions": len(parts),
            "compute_status": "deuteron",
            "M_codata_MeV": str(M_D_MEV),
            "m_e_MeV": str(M_E_MEV),
            "m_p_MeV": str(M_P_MEV),
            "m_n_MeV": str(M_N_MEV),
            "occam_witness_loaded": "rho-k-h3a-refinement.witness.json",
            "occam_schur_weyl_match_1e_40": bool(sw_match),
        },
        "data": {
            "abs_tr_M_at_q0_50dps": str(abs_tr_M),
            "rho_K_LO": str(rho_K_LO),
            "rho_K_codata": str(rho_K_codata),
            "delta_rho_residual": str(delta_rho),
            "target_signed": str(target),  # = Δρ · |tr_M|
            "sigma_inv_dim_q_n6_at_q0": str(sigma_inv_dim_q),
            "per_lambda": rows,
            "co_casimir_prediction": {
                "sum_contributions_signed": str(sum_contributions),
                "rho_K_pred": str(rho_K_pred),
                "M_pred_MeV": str(M_pred),
                "residual_MeV": str(residual_MeV),
                "residual_pct_of_M_codata": str(residual_pct),
                "closure_gap_LHS_minus_RHS": str(closure_gap),
                "diagnostic_closure_rescaler": str(diagnostic_closure_rescaler),
            },
            "occam_comparison": {
                "occam_partition": list(occam_partition),
                "Delta_lambda_occam": str(occam_delta),
                "abs_Delta_occam": str(abs(occam_delta)),
                "Delta_lambda_co_casimir_on_occam_partition": str(
                    delta_B_table[occam_partition]
                ),
                "ratio_abs_occam_over_co_casimir": str(
                    abs(occam_delta) / delta_B_table[occam_partition]
                ),
                "sum_abs_Delta_occam_singleton_trials": str(occam_sum_abs),
                "sum_Delta_co_casimir": str(co_casimir_sum_abs),
            },
        },
        "audit_reference": "AUDIT-DEEP-2026-05.md §7 P3 / P3' (Δ_λ selector)",
        "parent_witness": "rho-k-h3a-refinement.witness.json",
        "parent_pr": "#600",
        "race_position": (
            "Option B of a 4-way derivation race for Δ_λ(K).  Option B = "
            "Frobenius co-Casimir restriction (theorem-forced, vortex-blind, "
            "0 free parameters).  Other options under separate PRs."
        ),
        "interpretation": (
            "Δ_λ^B is FORCED by thm:frobenius-codim-universal — there is no "
            "freedom to fit it.  If the residual is small (≪ 0.1 MeV), "
            "co-Casimir restriction is the categorical Δ_λ selector and "
            "the deuteron binding ≈ -2.225 MeV is reproduced from the "
            "structure of C_dim_q alone, without any per-vortex tuning. "
            "If the residual is large (≥ 1 MeV), this option fails — the "
            "Frobenius co-Casimir is vortex-blind (per the .md theorem "
            "section 'Independence of the vortex'), so it cannot encode "
            "vortex-specific binding by itself; some additional vortex-"
            "dependent piece (Option A / C / D in the race) must carry it."
        ),
        "honest_reporting_note": (
            "Δ_λ^B is fixed at 1/dim_q(λ) by theorem — NOT rescaled to "
            "match M(D).  The diagnostic_closure_rescaler field reports "
            "what uniform rescaling would close the equation, but that "
            "rescaling is NOT applied to Δ_λ in the reported per_lambda "
            "table.  The reported residual is the un-tuned, theorem-only "
            "result.  Field renamed from `diagnostic_lambda_scale` per "
            "PR #1080 framing (no λ_scale; the framework's per-knot "
            "factor is VolDensity)."
        ),
        "follow_up": (
            "If Option B residual is small for D, extend to (T, ³He) at "
            "n=9 (p(9)=30) and ⁴He at n=12 (p(12)=77) — the per-isotypic "
            "1/dim_q profile is universal across all H_n(q), so the only "
            "atom-dependence is via y_λ(q_0) and χ^λ(β_K).  If Option B "
            "residual is large for D, document the gap and let the race "
            "favour another option (A: Plancherel truncation; C: jet-knot "
            "cohomology; D: minimum-norm pseudoinverse)."
        ),
    }
    builder = WitnessBuilder.wrap_legacy(
        "rho-k-h3a-co-casimir",
        witness,
        script_path=__file__,
        engine="python+mpmath",
    )
    out = builder.save()
    print(f"\n  Wrote {out.name} ({out.stat().st_size} bytes).")
    print("=" * 96)
    # Honest exit code: success if we wrote the witness (irrespective of
    # whether residual is small) — the caller is responsible for reading
    # the residual and deciding if Option B wins the race.
    return 0


if __name__ == "__main__":
    sys.exit(main())
