#!/usr/bin/env python3
"""
probe_d_symbolic_prospects.py — deuteron-restricted symbolic prospects for
the four A≥3-binding open items (owner request 2026-07-03, PR #3266).

EXPLORATORY (production-vs-exploratory discipline): probe_ prefix,
audit-only witness. Derive-or-refute; every near-match reported TIERED,
nothing wired. Companion audit doc:
docs/audits/2026-07-03-deuteron-from-scratch-error-ledger.md

## P1 — Δ_λ(D) ≈ 1/h(q₀): sharpen the PROBE-1 observation

On the trace-canonical path B_diag = Q_β·(tr_free − tr_atom), the residual
Δ_λ(D) = B_AME/B_diag was observed ≈ q₀^15.0002 ≈ 1/h(q₀) (PROBE-1,
2026-07-02). This probe:
  (i)   recomputes Δ_λ(D)·h(q₀) − 1 and the q₀-exponent at 50 dps;
  (ii)  evaluates the candidate closed form  B_D = Q_β·Δtr/h  vs AME;
  (iii) tests the cross-coincidence  Q_β/h  vs  m_e·8G  (the α_{k≥4}
        plateau constant) and vs E₀ = m_e/(q₀(q₀−1)) — if Q_β/h ≈ m_e·8G
        the "1/h" observation and the tower plateau are the SAME
        near-coincidence seen from two sides;
  (iv)  compares the symbolic CAL-2 proxy closed form
        Q_β/m_e = |q²−2q−1|(q+1)/(2q³)  against the production Kashiwara
        b² Q_β (attribution of the Q_β-form spread).
All (i)–(iv) are OBSERVATION-TIER near-matches unless an invariant is
found (formalize-first §3.3): no structural argument currently forces
Δ_λ(D)·h = 1, so nothing here is wired.

## P2 — α_k assignment restricted to the D tower: what IS symbolic

  (a) DERIVED exact (reproduced here symbolically from Hoefsmit n=3):
      χ^{(2,1)}(σ₁σ₂σ₁) = 0, hence tr_M(T_Δ) = z + h·z² =
      z·(1 + q^{1/2} − q^{−1/2}) ≠ z³ — the z^k marker series breaks at
      k = 3 structurally.
  (b) NEAR-MATCH: α₃ = 1 itself — the collapsed weight
      1 + q^{1/2} − q^{−1/2} evaluates to ≈ 1.1044 at q₀ (10.4%).
  (c) The D depth-stratified tower gap B_AME/B_tower(D) ≈ 3.66 has
      q₀-exponent ≈ 12.4 — NOT near-integer; no q₀-power bookkeeping
      closes the D tower (consistent with the PROBE-1 refutation of the
      Laurent-degree route).

## P3 — the per-λ weight (Δ_λ / FR-restricted projector) at D:
       UNDER-DETERMINATION result

At A=2 the scalar binding supplies ONE equation while λ ⊢ 6 supplies
ELEVEN per-block unknowns w_λ in Σ_λ w_λ·y_λ·Δχ^λ = B/E₀. So:
  — D data alone CANNOT determine a per-λ weight (10-dim solution
    space), and CANNOT falsify any candidate that preserves the scalar
    sum — this is exactly why the PROBE-4 collapse-last towers
    reproduced the scalar tower to ≤6.6e-7;
  — the FR-restricted projector χ^λ·χ^λ(e_{K*}) (brane-tower plan §7)
    is therefore only falsifiable CROSS-A (D fixes its scalar
    normalization; A≥3 fixes its shape).
The probe emits the D per-λ atom vector (y_λ, χ^λ_atom, contribution)
— the un-collapsed carrier the projector must weight — as data.

## P4 — many-body series + mirror pair: what D can decide

  — D IS the 2-body base case of the many-body series (one bond); the
    series reconciliation (2-body vs 4-body decompositions) is not
    decidable at A=2. Recorded as a scope statement, no compute.
  — the mirror-pair magnitude is an A=3 object (³H/³He); D is silent.

50 dps floor; q₀ from the canonical pin; no fits, no new constants.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
warnings.filterwarnings("ignore")

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

DPS = 50
mp.mp.dps = DPS + 10

from q_parameter import Q_50_DIGIT_STR, Q_MP, CATALAN_G  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION,
)
from derived_masses import q_beta_kashiwara_n2_mev  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from y_lambda_wenzl_bridge import (  # noqa: E402
    y_lambda_wenzl_bridge_numeric, partitions_of,
)
from witness_base import WitnessBuilder  # noqa: E402


def p1_delta_lambda(q: mp.mpf) -> dict:
    m_e = mp.mpf(str(M_E_MEV))
    B_AME = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    h = q - 1 / q
    E0 = m_e / (q * (q - 1))
    ta, tf, _, _ = tr_m_atom_zn(1, 1, dps=DPS)
    dtr = mp.mpf(tf) - mp.mpf(ta)

    # production Q_β (Kashiwara b² truncation) and the symbolic CAL-2
    # proxy closed form
    Qb_prod = q_beta_kashiwara_n2_mev()
    Qb_sym = m_e * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)

    B_diag = Qb_prod * dtr
    delta_D = B_AME / B_diag
    x = delta_D * h
    expo = mp.log(delta_D) / mp.log(q)

    # candidate closed form B = Q_β·Δtr/h
    B_cand = Qb_prod * dtr / h
    B_cand_sym = Qb_sym * dtr / h

    # cross-coincidence: Q_β/h vs m_e·8G (α_{k≥4} plateau) vs E₀
    plateau = m_e * 8 * mp.mpf(str(CATALAN_G))
    QbOverH = Qb_prod / h

    return {
        "Delta_tr": mp.nstr(dtr, 30),
        "Q_beta_production_MeV": mp.nstr(Qb_prod, 25),
        "Q_beta_symbolic_proxy_MeV": mp.nstr(Qb_sym, 25),
        "Q_beta_form_spread_rel": float((Qb_sym - Qb_prod) / Qb_prod),
        "Delta_lambda_D": mp.nstr(delta_D, 25),
        "Delta_lambda_D_times_h_minus_1": float(x - 1),
        "q0_exponent_of_Delta_lambda_D": mp.nstr(expo, 12),
        "exponent_gap_vs_15": float(expo - 15),
        "B_candidate_Qb_dtr_over_h_MeV": mp.nstr(B_cand, 25),
        "B_candidate_err_vs_AME_rel": float((B_cand - B_AME) / B_AME),
        "B_candidate_symbolicQb_err_vs_AME_rel":
            float((B_cand_sym - B_AME) / B_AME),
        "QbOverH_MeV": mp.nstr(QbOverH, 25),
        "plateau_me_8G_MeV": mp.nstr(plateau, 25),
        "QbOverH_vs_plateau_rel": float((QbOverH - plateau) / plateau),
        "E0_MeV": mp.nstr(E0, 25),
        "QbOverH_over_E0": float(QbOverH / E0),
        "tier": (
            "ALL observation-tier NEAR-MATCHES; no invariant forces "
            "Δ_λ(D)·h = 1 — NOT wired (formalize-first: the candidate "
            "class 'B_D = Q_β·Δtr/h' needs a structural argument for "
            "the 1/h before any cross-A wiring)"
        ),
    }


def p2_alpha_k(q: mp.mpf) -> dict:
    # symbolic reproduction of χ^{(2,1)}(σ₁σ₂σ₁) = 0 from the Hoefsmit
    # seminormal 2×2 matrices for λ = (2,1) over ℚ(q):
    #   ρ(σ₁) = [[q, 0], [0, -1/q]]
    #   ρ(σ₂) = [[q - 1/[2], c], [c', -1/q + 1/(q[2])]] with the standard
    # seminormal off-diagonals; we use the axial-distance form.
    # χ^{(2,1)}(σ₁σ₂σ₁) from the repo's OWN Hoefsmit seminormal
    # symbolic matrices (hecke.hecke_character_symbolic) — the honest
    # reproduction of the PROBE-2a derived-exact break.
    from hecke.hecke_character_symbolic import hoefsmit_matrices_symbolic
    qs = sp.symbols("q", positive=True)
    mats, _dim, _tab = hoefsmit_matrices_symbolic((2, 1), qs)
    r1, r2 = sp.Matrix(mats[0]), sp.Matrix(mats[1])
    chi21_delta = sp.simplify((r1 * r2 * r1).trace())

    # collapsed weight (exact): tr_M(T_Δ)/z³ would be α₃·(...): the
    # derived form is tr_M(T_Δ) = z + h·z² = z(1 + q^{1/2} − q^{−1/2})
    z = q**3 / (q**2 + 1)
    h = q - 1 / q
    collapsed = 1 + mp.sqrt(q) - 1 / mp.sqrt(q)

    # D tower gap exponent (uses the committed depth-stratified D value
    # from the 2026-06-09 canonical-default audit witnesses)
    import json
    B_AME = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    tower_D = None
    wp = COMP / "binding-depth-stratified-rust.witness.json"
    if wp.exists():
        row = json.loads(wp.read_text())["data"]["per_atom"].get("D")
        if row:
            tower_D = mp.mpf(str(row["B_MeV"]))
    tower_gap = (B_AME / tower_D) if tower_D else None

    return {
        "chi21_garside_symbolic": str(chi21_delta),
        "chi21_garside_is_zero": bool(sp.simplify(chi21_delta) == 0),
        "collapsed_weight_symbolic": "1 + q^(1/2) - q^(-1/2)",
        "collapsed_weight_at_q0": mp.nstr(collapsed, 20),
        "alpha3_eq_1_near_match_pct": float((collapsed - 1) * 100),
        "z_at_q0": mp.nstr(z, 20), "h_at_q0": mp.nstr(h, 20),
        "tower_D_B_MeV": (mp.nstr(tower_D, 15) if tower_D else None),
        "tower_D_gap": (float(tower_gap) if tower_gap else None),
        "tower_D_gap_q0_exponent": (
            mp.nstr(mp.log(tower_gap) / mp.log(q), 10)
            if tower_gap else None),
        "tier": (
            "(a) k=3 break DERIVED exact (reproduced symbolically); "
            "(b) α₃=1 NEAR-MATCH 10.4%; (c) D tower gap exponent "
            "~12.4 NOT near-integer — no q₀-power closes the D tower"
        ),
    }


def p3_per_lambda_underdetermination(q: mp.mpf) -> dict:
    m_e = mp.mpf(str(M_E_MEV))
    B_AME = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    E0 = m_e / (q * (q - 1))
    ta, tf, chi_atom, _ = tr_m_atom_zn(1, 1, dps=DPS)
    parts = partitions_of(6)
    vec = []
    chi_map = {}
    if isinstance(chi_atom, dict):
        chi_map = {tuple(k) if not isinstance(k, tuple) else k: v
                   for k, v in chi_atom.items()}
    for lam in parts:
        y = y_lambda_wenzl_bridge_numeric(lam, q, dps=DPS)
        chi = chi_map.get(tuple(lam))
        vec.append({
            "lambda": list(lam),
            "y_lambda": mp.nstr(mp.mpf(str(y)), 20),
            "chi_atom": (mp.nstr(mp.mpf(str(chi)), 20)
                         if chi is not None else None),
            "y_chi_contribution": (
                mp.nstr(mp.mpf(str(y)) * mp.mpf(str(chi)), 20)
                if chi is not None else None),
        })
    n_unknowns = len(parts)
    return {
        "n_partitions_H6": n_unknowns,
        "scalar_constraints_at_D": 1,
        "solution_space_dim": n_unknowns - 1,
        "required_scalar": mp.nstr(B_AME / E0, 20),
        "scalar_from_trace_Delta": mp.nstr(mp.mpf(tf) - mp.mpf(ta), 20),
        "per_lambda_atom_vector": vec,
        "conclusion": (
            "UNDER-DETERMINED at D: one scalar equation, 11 per-λ "
            "unknowns — no unique symbolic Δ_λ is derivable from "
            "deuteron data alone, and any collapse-last candidate "
            "preserving the scalar sum is UNFALSIFIABLE at A=2 (this is "
            "the structural reason PROBE-4's per-λ towers reproduced "
            "the scalar tower to ≤6.6e-7). The FR-restricted projector "
            "χ^λ·χ^λ(e_{K*}) must be tested CROSS-A: D only pins its "
            "scalar normalization"
        ),
    }


def main() -> int:
    q = Q_MP
    print("=" * 72)
    print("D-RESTRICTED SYMBOLIC PROSPECTS (P1–P4) — exploratory, tiered")
    print("=" * 72)

    p1 = p1_delta_lambda(q)
    print("\n[P1] Δ_λ(D) vs 1/h(q₀)")
    for k in ("Delta_lambda_D", "Delta_lambda_D_times_h_minus_1",
              "q0_exponent_of_Delta_lambda_D", "exponent_gap_vs_15",
              "B_candidate_err_vs_AME_rel", "QbOverH_vs_plateau_rel",
              "Q_beta_form_spread_rel", "QbOverH_over_E0"):
        print(f"  {k} = {p1[k]}")

    p2 = p2_alpha_k(q)
    print("\n[P2] α_k at A=2")
    for k in ("chi21_garside_symbolic", "chi21_garside_is_zero",
              "collapsed_weight_at_q0", "alpha3_eq_1_near_match_pct",
              "tower_D_B_MeV", "tower_D_gap", "tower_D_gap_q0_exponent"):
        print(f"  {k} = {p2[k]}")

    p3 = p3_per_lambda_underdetermination(q)
    print("\n[P3] per-λ weight at D")
    print(f"  unknowns={p3['n_partitions_H6']}  constraints="
          f"{p3['scalar_constraints_at_D']}  solution-space dim="
          f"{p3['solution_space_dim']}")
    print(f"  {p3['conclusion'][:120]}…")

    p4 = {
        "many_body_series": (
            "D IS the 2-body base case (one bond, exact by "
            "construction); the 2-body/4-body reconciliation and the "
            "ρ·A scale rule are NOT decidable at A=2"
        ),
        "mirror_pair": (
            "³H/³He magnitude is an A=3 object; D is silent — no "
            "D-restricted symbolic answer exists"
        ),
    }
    print("\n[P4] scope statements")
    for k, v in p4.items():
        print(f"  {k}: {v}")

    wb = (WitnessBuilder("probe-d-symbolic-prospects",
                         engine="mpmath+sympy")
          .set_description(
              "Deuteron-restricted symbolic prospects for the four "
              "A≥3-binding open items: P1 Δ_λ(D)≈1/h sharpened + the "
              "Q_β/h ≈ m_e·8G cross-coincidence; P2 χ^{(2,1)}(Δ)=0 "
              "reproduced symbolically + α₃ near-match + D tower-gap "
              "exponent; P3 per-λ under-determination theorem-shape "
              "statement (1 eq, 11 unknowns) + per-λ atom vector; P4 "
              "scope statements. Exploratory; nothing wired.")
          .set_audit_only(
              "docs/audits/2026-07-03-deuteron-from-scratch-error-ledger.md")
          .add_parameter("q0", Q_50_DIGIT_STR)
          .add_parameter("compute_dps", DPS)
          .add_data("P1_delta_lambda", p1)
          .add_data("P2_alpha_k", p2)
          .add_data("P3_per_lambda", p3)
          .add_data("P4_scope", p4))
    wb.add_assertion(
        "chi21_garside_zero_symbolic",
        computed=p2["chi21_garside_is_zero"], expected=True,
        source="Hoefsmit (2,1) seminormal, trace of ρ(σ₁σ₂σ₁) — "
               "PROBE-2a derived-exact reproduced")
    wb.add_assertion(
        "p3_underdetermined",
        computed=p3["solution_space_dim"], expected=10,
        source="11 partitions of 6 minus 1 scalar constraint")
    wb.save()
    print("\nwitness → probe-d-symbolic-prospects.witness.json (audit-only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
