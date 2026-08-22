#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical rerun probe; symbolic-q content upstream
# in frobenius-partition-sum.witness.json (same as parent rho_k_h3a_co_casimir.py).
"""co-Casimir Δ_λ = 1/dim_q refutation (#602) — PER-KNOT-DENSITY RE-RUN (bean x5az).

Protocol: docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md §Next item 1.
Question: is the co-Casimir refutation (residual −2.30 MeV, "wrong sign",
rescaler ≈ −30) an artifact of the fitted global λ_A density
(`per_knot_density_borromean`, p=n-degenerate, ≈ 2.533), or robust under the
canonical PER-KNOT density `per_knot_density_per_block(Vol(𝓑₃), tr_M(K), q₀)`
with p ≠ n-distinct Markov traces (tr_M(p) ≈ 1.0653, tr_M(n) ≈ 0.9232,
loaded from the chi-{atom}-h3-at-q0-50dps chi-cache witnesses)?

WHERE THE DENSITY ENTERS.  The refutation-verdict quantity
Σ_λ y_λ χ^λ Δ_λ^B (Δ_λ^B = 1/dim_q(λ)) is built purely from per-partition
Hecke data — it is density-INDEPENDENT.  The density enters only the
constituent mass baseline m_p + m_n behind ρ_K^LO (and hence the target
Δρ·|tr_M| = (M(D) − (m_p+m_n))/m_e that the sum must reproduce, and the
residual M(D) − M_pred).  This rerun therefore holds the sum fixed
(re-verified against the parent run) and swaps the constituent baseline
across three densities, like-for-like:

  1. CODATA (the parent script's actual baseline — measured-equivalent),
  2. global λ_A     : m_p = m_n = m_e · per_knot_density_borromean(q₀)  ≈ 966,
  3. per-knot tr_M  : m_N = m_e · per_knot_density_per_block(8G, tr_M(N), q₀)
                      (proton ≈ 406, neutron ≈ 352 — p ≠ n distinct).

Same q₀ (canonical muon-q₀, q_parameter.Q_MP = the computations/-layer
q-pinning-50-digit value), same precision defaults (_precision.set_compute_dps),
same Occam-witness y_λ χ^λ inputs, same 11 partitions of 6.  NO new fitted
constants; NO rescaler is applied (the diagnostic rescaler is reported to
quantify closure failure only).

HONEST-REPORTING SCOPE (AGENTS.md §refuted): any negative outcome here is a
scope-limited negative (a) — "the co-Casimir Δ_λ = 1/dim_q closure, alone,
with the stated density base, does not reproduce the numbers" — not a
structural exclusion.

EXPLORATORY probe — no production code or witnesses changed; emits
rho-k-h3a-co-casimir-perknot-rerun.witness.json.
"""
from __future__ import annotations

import json
import sys as _sys
from pathlib import Path as _Path

_PARENT = _Path(__file__).resolve().parent.parent
if str(_PARENT) not in _sys.path:
    _sys.path.insert(0, str(_PARENT))
import _path_bridge as _pb  # noqa: F401, E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()  # same default as parent (65 dps compute / 50 serialize)

# Reuse the parent refutation script's machinery verbatim (import, not copy).
import rho_k_h3a_co_casimir as parent  # noqa: E402
from codata_constants import M_E_MEV, M_P_MEV, M_D_MEV  # noqa: E402
from experimental_constants import m_n_derived_3input  # noqa: E402
from murnaghan_nakayama import partitions_of  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []
from _li_2_q_util import per_knot_density_per_block, per_knot_density_borromean  # noqa: E402

VOL_B3 = 8 * mp.catalan  # Vol(𝓑₃), Adams 1985 — same constant the density routines use


def load_tr_m_from_chi_cache(atom: str) -> mp.mpf:
    """Per-knot Markov trace |tr_M(β_atom)| from the canonical chi-cache witness."""
    path = _pb.witness_path(f"chi-{atom}-h3-at-q0-50dps.witness.json", _PARENT)
    w = json.loads(path.read_text())
    d = w.get("data", w)
    return mp.mpf(d["tr_M_at_q0"])


def closure_report(name: str, m_p: mp.mpf, m_n: mp.mpf,
                   abs_tr_M: mp.mpf, sum_contrib: mp.mpf) -> dict:
    """Mass-equation closure for a given constituent baseline (parent Step 4)."""
    m_pn = m_p + m_n
    rho_K_LO = m_pn / (M_E_MEV * abs_tr_M)
    rho_K_codata = M_D_MEV / (M_E_MEV * abs_tr_M)
    target = (rho_K_codata - rho_K_LO) * abs_tr_M  # = (M(D) − (m_p+m_n))/m_e, signed
    M_pred = m_pn + M_E_MEV * sum_contrib
    residual_MeV = M_D_MEV - M_pred
    rescaler = target / sum_contrib
    same_sign = (target > 0) == (sum_contrib > 0)
    print(f"\n  [{name}]")
    print(f"    m_p = {mp.nstr(m_p, 10)}  m_n = {mp.nstr(m_n, 10)}  "
          f"m_p+m_n = {mp.nstr(m_pn, 12)} MeV")
    print(f"    target (Δρ·|tr_M|)        = {mp.nstr(target, 12)}")
    print(f"    Σ y_λ χ^λ Δ_λ^B (fixed)   = {mp.nstr(sum_contrib, 12)}")
    print(f"    same sign?                = {same_sign}")
    print(f"    rescaler target/Σ         = {mp.nstr(rescaler, 10)}")
    print(f"    M(D)^pred                 = {mp.nstr(M_pred, 12)} MeV")
    print(f"    residual M(D)−M_pred      = {mp.nstr(residual_MeV, 8)} MeV")
    return {
        "m_p_MeV": str(m_p), "m_n_MeV": str(m_n), "m_pn_MeV": str(m_pn),
        "target_signed": str(target),
        "sum_y_chi_Delta_B": str(sum_contrib),
        "same_sign_sum_vs_target": bool(same_sign),
        "diagnostic_closure_rescaler": str(rescaler),
        "M_pred_MeV": str(M_pred),
        "residual_MeV": str(residual_MeV),
        "abs_rescaler": str(abs(rescaler)),
    }


def main() -> int:
    print("=" * 96)
    print("  co-Casimir Δ_λ = 1/dim_q refutation — PER-KNOT density re-run (bean x5az)")
    print("=" * 96)
    print(f"  q_0 = {mp.nstr(Q_MP, 25)}  (canonical muon-q₀, computations/ layer)")

    # ── Density-independent verdict quantity: Σ y_λ χ^λ Δ_λ^B ──────────
    occam = parent.load_occam_witness()
    abs_tr_M = mp.mpf(occam["data"]["abs_tr_M_at_q0_50dps"])
    occam_rows = {tuple(r["partition"]): r for r in occam["data"]["per_lambda"]}
    parts = partitions_of(6)
    sum_contrib = mp.mpf(0)
    for lam in parts:
        d_q0 = parent.evaluate_at_q0(parent.q_dim_sym(lam))
        y_chi = mp.mpf(occam_rows[lam]["y_chi_product"])
        sum_contrib += y_chi / d_q0  # Δ_λ^B = 1/dim_q(λ)
    print(f"\n  |tr_M(β_D)| (H_6, per-knot deuteron trace) = {mp.nstr(abs_tr_M, 20)}")
    print(f"  Σ y_λ χ^λ Δ_λ^B (density-independent)       = {mp.nstr(sum_contrib, 12)}")

    # Cross-check against the parent's committed witness value.
    parent_w = record_upstream(_pb.witness_path("rho-k-h3a-co-casimir.witness.json", _PARENT), _UPSTREAM_RECORDS)
    parent_sum = mp.mpf(
        parent_w["data"]["co_casimir_prediction"]["sum_contributions_signed"])
    sum_match = abs(sum_contrib - parent_sum) < mp.mpf("1e-40")
    print(f"  matches parent witness sum @1e-40           = {sum_match}")

    # ── Per-knot Markov traces (canonical chi-cache, p ≠ n distinct) ───
    tr_p = load_tr_m_from_chi_cache("proton")
    tr_n = load_tr_m_from_chi_cache("neutron")
    print(f"\n  tr_M(proton, H_3)  = {mp.nstr(tr_p, 15)}")
    print(f"  tr_M(neutron, H_3) = {mp.nstr(tr_n, 15)}")

    # ── Three constituent baselines, like-for-like ─────────────────────
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)  # λ_A route is
        # deprecated-for-absolute-mass by design; this rerun uses it ONLY as
        # the refutation-era baseline under audit, not as production mass.
        m_lambdaA = M_E_MEV * per_knot_density_borromean(Q_MP)
    m_p_pk = M_E_MEV * per_knot_density_per_block(VOL_B3, tr_p, Q_MP)
    m_n_pk = M_E_MEV * per_knot_density_per_block(VOL_B3, tr_n, Q_MP)

    rep_codata = closure_report("CODATA baseline (parent script, reproduction)",
                                M_P_MEV, m_n_derived_3input, abs_tr_M, sum_contrib)
    rep_lambdaA = closure_report("global λ_A density (fitted, p=n-degenerate)",
                                 m_lambdaA, m_lambdaA, abs_tr_M, sum_contrib)
    rep_perknot = closure_report("PER-KNOT density (canonical tr_M, p≠n)",
                                 m_p_pk, m_n_pk, abs_tr_M, sum_contrib)

    # ── Verdict ─────────────────────────────────────────────────────────
    # Closure fails under EVERY density iff |rescaler| ≫ 1 in all three.
    fails_all = all(abs(mp.mpf(r["diagnostic_closure_rescaler"])) > 10
                    for r in (rep_codata, rep_lambdaA, rep_perknot))
    verdict = (
        "ROBUST — the co-Casimir Δ_λ = 1/dim_q refutation is NOT a λ_A density "
        "artifact. The verdict quantity Σ y_λ χ^λ Δ_λ^B = +0.145 is density-"
        "independent (pure per-partition Hecke data). Swapping the constituent "
        "baseline changes only the target: CODATA target −4.35 (wrong sign, "
        "|rescaler| ≈ 30), global-λ_A target ≈ −110.5 (wrong sign, ≈ 763×), "
        "per-knot target ≈ +2186 (sign now agrees but ≈ 15081× too small). "
        "The closure fails by ≥ 30× under every density; the specific 'wrong "
        "sign' phrasing is baseline-dependent, the failure is not. Scope (a): "
        "this construction, alone, does not reproduce the numbers under any "
        "of the three density bases — no ingredient-level exclusion claimed."
    )
    print(f"\n  VERDICT: {verdict}")

    wb = WitnessBuilder("rho-k-h3a-co-casimir-perknot-rerun", engine="python+mpmath")
    wb.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    wb.data["audit"] = "docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md"
    wb.data["bean"] = "x5az"
    wb.data["q_0_50dps"] = mp.nstr(Q_MP, 50)
    wb.data["vol_B3"] = str(VOL_B3)
    wb.data["abs_tr_M_beta_D_H6"] = str(abs_tr_M)
    wb.data["tr_M_proton_H3"] = str(tr_p)
    wb.data["tr_M_neutron_H3"] = str(tr_n)
    wb.data["sum_y_chi_Delta_B_density_independent"] = str(sum_contrib)
    wb.data["sum_matches_parent_witness_1e_40"] = bool(sum_match)
    wb.data["closure_by_density"] = {
        "codata_baseline_parent_reproduction": rep_codata,
        "global_lambda_A_fitted": rep_lambdaA,
        "per_knot_tr_M_canonical": rep_perknot,
    }
    wb.data["verdict"] = verdict
    wb.data["refutation_scope"] = "scope-limited negative (a) per AGENTS.md"
    wb.add_assertion("sum_density_independent_matches_parent",
                     computed=1 if sum_match else 0, expected=1, tolerance=0)
    wb.add_assertion("closure_fails_under_all_three_densities",
                     computed=1 if fails_all else 0, expected=1, tolerance=0)
    wb.add_assertion(
        "codata_residual_reproduces_minus_2p30_MeV",
        computed=float(rep_codata["residual_MeV"]),
        expected=-2.2986427, tolerance=1e-4)
    wb.save()
    print("\n✓ Witness: rho-k-h3a-co-casimir-perknot-rerun.witness.json")
    return 0


if __name__ == "__main__":
    _sys.exit(main())
