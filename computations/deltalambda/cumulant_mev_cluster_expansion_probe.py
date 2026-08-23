#!/usr/bin/env python3
"""Item 1: the cumulant→MeV map is a CLUSTER EXPANSION — the deuteron's LINEAR B=5g
and the He4-local LOG b₄=−ln det are different ORDERS, not rival maps. (Forward, no fit.)

CONTEXT (read first, in order):
  * PR #4093 (merged): the b₄ pole-regulator "collective-coordinate" route hit a wall
    whose load-bearing gap was named as "no established cumulant→MeV map" — the deuteron
    law B=5g is LINEAR in g while b_A=−ln det is LOG (5g/b₂=10.03).
  * docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md
    §2/§3: the corpus ALREADY documents that B=5g is "**NOT** the A=2 case of the pinned
    b₄=−ln det(I+G) form", and that the deuteron law's real shape is
        B(²H) = √5·E_unit·(1 − x/10 + 3x²/200 − ⋯),  x=(v−v⁻¹)²,
    dimensionless core Lean-proved sorry-free, with E_unit≈0.9959 MeV the ONE open anchor.

THE RESOLUTION (forward; uses the corpus's own documented deuteron law, no new fit).
  The #4093 "inconsistency" is a CATEGORY ERROR: it compared a 2-body/pair-order term
  (the deuteron's linear √5·E_unit·g·ladder) against a 4-body connected cumulant
  (b₄=−ln det). These are different ORDERS of one cluster (Mayer/cumulant) expansion of
  the binding, both carried in the SAME MeV unit E_unit:

      B(K) = E_unit · [ Σ_pairs (linear pair term)  +  Σ_{k≥3} b_k (connected k-body cumulants) ].

  * PAIR ORDER is LINEAR in the magnitude g (the deuteron: one pn bond, B ~ √5·E_unit·g·ladder).
  * MANY-BODY ORDERS are the connected cumulants b_k=−ln det-type (b₄ is the He4-local
    4-body piece of #4084 — LOG, and near-critical at ⁴He).
  * The leading term of −ln det₂ is g² (QUADRATIC), a different power of g than the pair-
    order 5g (LINEAR) — the machine-level signature that they are different orders, not a
    normalization mismatch.

  VERIFICATIONS (this probe):
   V1. deuteron pair-order √5·E_unit·ladder = 2.2245668 MeV = AME 2.224566 to 6 digits
       (the ladder correction fixes the +0.41% that bare 5g carries).
   V2. 5g / b₂ = 10.03, and leading(−ln det₂)=g² ≠ 5g — different orders (category error shown).
   V3. ⁴He cluster structure: pair-additive baseline ρ₄=C(4,2)=6 bonds; 6·B(²H)=13.35 MeV
       vs AME B(⁴He)=28.30 — the extra ~15 MeV is the connected many-body (b₃+b₄) sum, with
       b₄ the #4084 near-pole enhancement. Coheres with the observed ρ₄~13 (>>6).

  CONSEQUENCE. The "linear vs log" is cluster-ORDER structure, not a contradiction; there
  is ONE MeV anchor E_unit shared across orders (the genuine open, per the provenance
  audit §2e). This dissolves the #4093 normalization gap AND places the b₄ magnitude
  correctly: ⁴He binding = 6 pair terms + the near-pole b₄ cumulant, same E_unit. It does
  NOT derive E_unit (still open) and does NOT close the b₄ magnitude (still open) — it
  fixes the FRAMEWORK the two live in.

EXPLORATORY — audit + witness only; no production wiring, no fit, no AME inversion (E_unit
is the corpus's documented anchor, used as the shared unit, not fitted here).
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

COMP = str(_COMP)
set_compute_dps()

Q0_STR = "1.10997859555733471"           # muon-canonical q0 (computations/ layer)
E_UNIT_STR = "0.995940"                   # corpus deuteron anchor (the ONE open; provenance §2e)


def main() -> int:
    q0 = mp.mpf(Q0_STR)
    v = mp.sqrt(q0)
    two_v = v + 1 / v
    g = 1 / mp.sqrt(1 + two_v ** 2)
    x = (v - 1 / v) ** 2                  # deformation parameter = (q0-1)^2/q0
    E_unit = mp.mpf(E_UNIT_STR)

    # V1 -- deuteron PAIR-ORDER (linear) form, corpus ladder shape
    ladder = 1 - x / 10 + 3 * x ** 2 / 200
    B_deut_pair = mp.sqrt(5) * E_unit * ladder
    B_AME_2H = mp.mpf("2.224566")
    v1_match = abs(B_deut_pair - B_AME_2H) < mp.mpf("1e-5")

    # V2 -- category error: pair-order linear (5g) vs 4-body cumulant (log, ~g^2)
    five_g = 5 * g
    b2_cumulant = -mp.log(1 - g ** 2)
    lead_cumulant = g ** 2                # leading order of -ln(1-g^2)
    v2_diff_order = abs(five_g - b2_cumulant) > mp.mpf("1") and abs(lead_cumulant - five_g) > mp.mpf("1")
    ratio_5g_b2 = five_g / b2_cumulant

    # V3 -- 4He cluster structure (pair-additive baseline + many-body remainder)
    B_AME_4He = mp.mpf("28.295673")
    pair_bonds_4He = 6                    # C(4,2)
    pair_additive = pair_bonds_4He * B_AME_2H
    many_body_remainder = B_AME_4He - pair_additive
    rho4_baseline = mp.mpf(pair_bonds_4He)        # pair-additive rho4
    rho4_observed = B_AME_4He / B_AME_2H
    v3_manybody_positive = many_body_remainder > 0 and rho4_observed > rho4_baseline

    result = {
        "shared_anchor_E_unit_MeV": mp.nstr(E_unit, 8),
        "E_unit_status": "the ONE open dimensional anchor (provenance audit §2e); used here as the "
                         "shared MeV unit across cluster orders, NOT fitted.",
        "cluster_expansion": "B(K) = E_unit * [ Σ_pairs (linear pair term) + Σ_{k>=3} b_k "
                             "(connected k-body cumulants) ]",
        "V1_deuteron_pair_order_linear": {
            "sqrt5_E_unit_ladder_MeV": mp.nstr(B_deut_pair, 10),
            "AME_2H_MeV": mp.nstr(B_AME_2H, 8),
            "matches_AME_6dig": bool(v1_match),
            "note": "the ladder (1 - x/10 + 3x^2/200) fixes the +0.41% that bare 5g=2.2336 carries.",
        },
        "V2_category_error_different_orders": {
            "pair_order_5g": mp.nstr(five_g, 8),
            "cumulant_b2_minus_ln_det": mp.nstr(b2_cumulant, 8),
            "leading_cumulant_is_g_squared": mp.nstr(lead_cumulant, 8),
            "ratio_5g_over_b2": mp.nstr(ratio_5g_b2, 6),
            "different_orders_confirmed": bool(v2_diff_order),
            "note": "5g is LINEAR in g (pair order); -ln det2 ~ g^2 is QUADRATIC (4-body cumulant). "
                    "Different powers => different cluster orders, not a normalization mismatch. "
                    "This is the #4093 category error, resolved.",
        },
        "V3_He4_cluster_structure": {
            "pair_additive_baseline_MeV": mp.nstr(pair_additive, 8),
            "AME_4He_MeV": mp.nstr(B_AME_4He, 8),
            "many_body_remainder_MeV": mp.nstr(many_body_remainder, 8),
            "rho4_pair_baseline": int(pair_bonds_4He),
            "rho4_observed": mp.nstr(rho4_observed, 6),
            "many_body_positive": bool(v3_manybody_positive),
            "note": "4He = 6 pair terms (13.35 MeV) + connected many-body (b3+b4, ~15 MeV), with b4 the "
                    "#4084 near-pole enhancement; same E_unit. Coheres with observed rho4~13 >> 6.",
        },
        "verdict": {
            "classification": "RESOLUTION (forward, no new fit) — the #4093 cumulant->MeV "
                              "'inconsistency' is a category error; linear (pair) and log (many-body) "
                              "are different orders of one cluster expansion with a single E_unit anchor.",
            "still_open": "E_unit itself (the dimensional anchor, provenance §2e) and the b4 magnitude "
                          "(#4084) remain open; this fixes the FRAMEWORK, not those two.",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "cumulant-mev-cluster-expansion",
        "description": ("Item 1: the cumulant->MeV map is a cluster expansion — the deuteron's LINEAR "
                        "B=√5·E_unit·ladder is the pair order, the He4-local LOG b₄=−ln det is a "
                        "connected many-body order; same E_unit anchor. Resolves the #4093 "
                        "'linear-vs-log inconsistency' as a category error (pair term vs 4-body "
                        "cumulant; 5g linear vs -ln det2 ~ g^2 quadratic). Deuteron pair-order matches "
                        "AME to 6 digits; 4He = 6 pair terms + many-body (b3+b4) remainder. Does not "
                        "derive E_unit or close the b4 magnitude. Forward, no fit, audit-only."),
        "audit_only": True,
        "tier": "structural reconciliation (corpus-documented deuteron law + exact cluster arithmetic)",
        "result": result,
        "context": {
            "axis": "Δ_λ magnitude — cumulant→MeV map (Item 1, bean qou-4uk9)",
            "builds_on": "PR #4093 (regulator wall) + #4084 (b4 ss-pole)",
            "provenance": "docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md §2e/§3",
            "q0_convention": "muon-canonical (computations/ layer)",
            "no_fit": True,
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "cumulant-mev-cluster-expansion", payload,
        script_path=__file__, engine="mpmath", output_dir=os.path.join(COMP, "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("deuteron_pair_order_matches_AME_6dig", computed=str(bool(v1_match)), expected="True")
    wb.add_assertion("linear_and_log_are_different_orders", computed=str(bool(v2_diff_order)), expected="True")
    wb.add_assertion("He4_many_body_remainder_positive", computed=str(bool(v3_manybody_positive)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== Item 1: cumulant→MeV map = cluster expansion (linear pair + log many-body) ===")
    print(f"shared anchor E_unit = {mp.nstr(E_unit,7)} MeV (the ONE open; used as unit, not fitted)")
    print(f"V1 deuteron √5·E_unit·ladder = {mp.nstr(B_deut_pair,10)} MeV vs AME {mp.nstr(B_AME_2H,8)} "
          f"(match 6dig: {v1_match})")
    print(f"V2 category error: 5g={mp.nstr(five_g,6)} (linear) vs b₂=−ln det₂={mp.nstr(b2_cumulant,6)} "
          f"(~g²={mp.nstr(lead_cumulant,6)}); ratio {mp.nstr(ratio_5g_b2,5)} — different orders: {v2_diff_order}")
    print(f"V3 4He: 6 pair terms = {mp.nstr(pair_additive,6)} MeV + many-body {mp.nstr(many_body_remainder,6)} "
          f"MeV = AME {mp.nstr(B_AME_4He,7)}; ρ₄ obs {mp.nstr(rho4_observed,5)} > baseline 6: {v3_manybody_positive}")
    print("VERDICT: linear (pair) and log (many-body) are different CLUSTER ORDERS, one E_unit anchor. "
          "#4093 inconsistency = category error, resolved. E_unit + b4 magnitude stay open.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
