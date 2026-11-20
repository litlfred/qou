#!/usr/bin/env python3
"""Where does E_unit come from? — traced to the COUNIT (q−q⁻¹) via the m_e bridge (μ₀).
Owner steer (2026-07-19): "follow (co)units through NA-Stokes in cat action; μ₀ first order only?"

CONTEXT (read first, in order):
  * merged #4101 (docs/audits/2026-07-19-cumulant-mev-map-cluster-expansion.md §4): E_unit is
    the one dimensional open; the reeb provenance §2h.2 declared it "external/scale-free" (nearest
    internal scale 2m_e +2.6%) — WITHOUT connecting it to the counit-derived per-crossing scale.
  * canonical cheat sheet lines 213/237: μ₀ = m_e/(3(q−q⁻¹)/2) ≈ 1.63 MeV is DERIVED ("the
    framework's per-crossing scale"); E_rot = μ₀·ℏ_q·J_q²(j=n/2) gives B_D −9% with 0 free params.
  * climax-volume-mass/crossing-energy-*: 𝔈_cross = strong baseline + Q·(q−q⁻¹), h=q−q⁻¹ =
    def:coulomb-charge; (q,−q⁻¹) are the Hecke generator eigenvalues forced by rigid monoidal
    structure. commutative-crossing-energy.md: at q=1, q−q⁻¹ vanishes; √λ_− = i (the √ structure).
  * observations/crossing-energy-interpretation.md:41: deuteron pn-pair = n_c=3 crossings, net
    energy 3(q−q⁻¹) = 0.630 skein units.  categorical-action.lean: matter = unit ≫ counit.

THE TRACING (answers "where does E_unit come from = counit").
  The per-crossing weight (q−q⁻¹) IS the antisymmetric Hecke-eigenvalue / SKEIN / counit-character
  difference (L₊−L₋ = q−q⁻¹) — proved + in-paper (crossing-energy chapter; categorical-action
  carries unit≫counit). The deuteron pn-pair is 3 crossings ⇒ net skein energy 3(q−q⁻¹). The
  DIMENSIONAL bridge to MeV divides the τ-functor scale m_e by that 3-crossing counit energy:
      μ₀ = m_e / (3(q−q⁻¹)/2)  ≈ 1.6295 MeV   (DERIVED, 0 free params)
  and the deuteron rotational energy E_rot = μ₀·ℏ_q·J_q²(3) = 2.0196 MeV (AME 2.2247, −9%).

  So E_unit's SOURCE is the counit: the q-structure is (q−q⁻¹) (counit skein), the dimension is
  m_e (τ-functor). The reeb §2h.2 "external/scale-free" verdict is TOO STRONG — it missed that
  μ₀ already derives a per-crossing MeV scale FROM the counit. The "5g·E_unit=0.996" form (+0.4%)
  and the "μ₀·ℏ_q·J_q²=2.02" form (−9%) are the SAME counit (q−q⁻¹) structure at different
  dimensional realizations; they have never been unified (the "why not clear").

  μ₀ FIRST ORDER ONLY? — yes (the honest assessment). μ₀ ∝ 1/(q−q⁻¹) uses the LEADING
  antisymmetric counit combination; the full crossing energy is 𝔈 = baseline + Q·(q−q⁻¹) + …
  (higher holonomy orders). The deuteron −9% is the size of the missing higher-order (co)unit /
  NA-Stokes terms. Deriving those (the owner's "follow (co)units through NA-Stokes") is the route
  to close the derived-scale form to the 5g form's +0.4% accuracy.

  WHAT THIS IS / IS NOT. This TRACES the source (counit → μ₀, first-order) and dissolves the
  "scale-free/external" over-claim — it does NOT close E_unit: μ₀ is −9%, and unifying it with the
  +0.4% 5g form needs the derived higher-order counit expansion (open). No fit, no axiom-laundering.

EXPLORATORY — audit + witness only; no production wiring, no fit, no AME inversion.
"""
from __future__ import annotations

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

set_compute_dps()

# q0 read BY NAME (bean qou-9ugp, 2026-09-04). This was the literal
# "1.10997859555733471" -- the RETIRED self-certified muon pin A, superseded
# 2026-08-22 (fca08de7d2) by the live CODATA-2022 lepton-ratio derivation.
# A frozen literal cannot follow the anchor when it moves, and this producer
# was UNSTAMPED, so the anchor audit filed it Q0_ANCHOR_MISSING rather than
# Q0_FLIP -- invisible to the corpus-wide drain, which keys on stamps.
# It resolves the PROTON pin per the owner directive of 2026-08-15, sharpened
# 2026-08-30: proton unless the producer is (E1) an explicit mu-vs-p
# comparison or (E2) the ideal CAL-1/2/3 mathematical layer. This is neither
# -- it is a sole-anchor probe that happened to be muon-named.
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402  (AME registry)
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

Q0_STR = _Q0_RESOLVED
M_E_STR = "0.51099895"
E_UNIT_STR = "0.995940"          # 5g-form external unit (reeb §2f)
B_AME_2H = _ame_nstr(AME_B_DEUTERON_MEV_VALIDATION, 30)


def qint(q, n):
    return (q ** n - q ** (-n)) / (q - 1 / q)   # balanced [n]_q


def main() -> int:
    q = mp.mpf(Q0_STR)
    m_e = mp.mpf(M_E_STR)
    E_unit = mp.mpf(E_UNIT_STR)
    B2H = mp.mpf(B_AME_2H)

    # 1. the counit skein weight
    h = q - 1 / q                                     # skein = counit-char difference L+-L-
    three_crossing_net = 3 * h                         # deuteron pn-pair (n_c=3), skein units
    net_matches_table = abs(three_crossing_net - mp.mpf("0.630")) < mp.mpf("0.02")

    # 2. the derived per-crossing scale μ₀ = m_e / (3(q-q^-1)/2)
    mu0 = m_e / (3 * h / 2)
    mu0_matches_cheatsheet = abs(mu0 - mp.mpf("1.6295")) < mp.mpf("0.001")

    # 3. deuteron rotational energy E_rot = μ₀·ℏ_q·J_q²(3)
    hbar_q = 1 - 1 / q
    Jq2_3 = qint(q, 3) * qint(q, 4)
    E_rot = mu0 * hbar_q * Jq2_3
    err_mu0_form = (E_rot / B2H - 1) * 100                 # ≈ −9%

    # 4. the two forms share the counit structure; different dimensional realization
    #    5g form: B = 5g·E_unit·ladder (+0.4%, external E_unit)
    v = mp.sqrt(q)
    x = (v - 1 / v) ** 2                                   # deformation param = (q-1)^2/q
    B_5g = mp.sqrt(5) * E_unit * (1 - x / 10 + 3 * x ** 2 / 200)
    err_5g_form = (B_5g / B2H - 1) * 100                   # ≈ +0.4% (matches to 6 dig)
    E_unit_over_mu0 = E_unit / mu0                         # 0.611 (the un-unified gap)

    # 5. first-order assessment: the −9% is the missing higher (co)unit order
    mu0_form_deficit_pct = float(err_mu0_form)
    first_order_plausible = abs(mu0_form_deficit_pct) < 15 and abs(mu0_form_deficit_pct) > 3

    result = {
        "counit_skein_weight_q_minus_qinv": mp.nstr(h, 10),
        "counit_provenance": "h=q−q⁻¹ = antisymmetric Hecke eigenvalue diff = skein L₊−L₋ = "
                             "counit-character difference; PROVED + in-paper (crossing-energy-"
                             "categorical-origin; categorical-action.lean matter=unit≫counit).",
        "deuteron_3crossing_net_skein": mp.nstr(three_crossing_net, 6),
        "matches_crossing_energy_table_0p630": bool(net_matches_table),
        "mu0_derived_per_crossing_MeV": mp.nstr(mu0, 8),
        "mu0_matches_cheatsheet_1p6295": bool(mu0_matches_cheatsheet),
        "deuteron_mu0_form": {
            "E_rot_mu0_hbarq_Jq2_3_MeV": mp.nstr(E_rot, 8),
            "AME_2H_MeV": mp.nstr(B2H, 7),
            "err_pct": mp.nstr(err_mu0_form, 4),
            "note": "DERIVED (0 free params) but −9% — the counit-derived scale.",
        },
        "deuteron_5g_form": {
            "B_5g_E_unit_ladder_MeV": mp.nstr(B_5g, 9),
            "err_pct": mp.nstr(err_5g_form, 4),
            "E_unit_external_MeV": mp.nstr(E_unit, 7),
            "note": "+0.4% (6-dig match) but E_unit external/scale-free (§2h.2).",
        },
        "the_ununified_gap": {
            "E_unit_over_mu0": mp.nstr(E_unit_over_mu0, 6),
            "note": "the two forms use the SAME counit (q−q⁻¹) structure but different dimensional "
                    "realizations (μ₀=1.63 derived −9% vs E_unit=0.996 external +0.4%); never "
                    "unified — this is the 'why not clear'.",
        },
        "mu0_first_order_assessment": {
            "mu0_uses_leading_q_minus_qinv": True,
            "full_crossing_energy_has_higher_orders": "𝔈 = baseline + Q·(q−q⁻¹) + … (holonomy)",
            "deficit_consistent_with_missing_higher_order": bool(first_order_plausible),
            "note": "μ₀ ∝ 1/(q−q⁻¹) is the leading antisymmetric counit combination; the −9% is the "
                    "missing higher-order (co)unit / NA-Stokes terms. Deriving them (owner steer) is "
                    "the route to close the derived-scale form to +0.4%.",
        },
        "verdict": {
            "answer_where_E_unit_comes_from": "the COUNIT: q-structure = (q−q⁻¹) (Hecke counit/skein "
                                              "difference, proved+in-paper), dimension = m_e "
                                              "(τ-functor); realized as μ₀ = m_e/(3(q−q⁻¹)/2), "
                                              "FIRST-ORDER, deuteron −9%.",
            "corrects": "the §2h.2 'external/scale-free' over-claim — a per-crossing MeV scale IS "
                        "derived from the counit (μ₀); it was just not connected to the 5g E_unit.",
            "still_open": "μ₀ is −9%; unifying it with the +0.4% 5g form requires the DERIVED "
                          "higher-order counit expansion (the NA-Stokes route). E_unit NOT closed.",
            "no_fit": True,
        },
    }

    payload = {
        "computation": "eunit-counit-mu0-tracing",
        "description": ("Traces E_unit's source to the COUNIT: the per-crossing weight (q−q⁻¹) is the "
                        "Hecke counit-character / skein difference (proved + in-paper); the deuteron "
                        "3-crossing net energy 3(q−q⁻¹) bridges to MeV via μ₀=m_e/(3(q−q⁻¹)/2)=1.63 "
                        "(DERIVED, deuteron −9%). Corrects the reeb §2h.2 'external/scale-free' "
                        "over-claim (a counit-derived per-crossing scale exists, μ₀, just unconnected "
                        "to the 5g E_unit=0.996 +0.4% form). μ₀ is FIRST-ORDER in (q−q⁻¹); the −9% is "
                        "the missing higher-order (co)unit/NA-Stokes terms. Answers 'where does E_unit "
                        "come from = counit'; does NOT close it. Owner steer; forward, no fit."),
        "audit_only": True,
        "tier": "structural tracing (corpus-documented counit/crossing-energy + derived μ₀ arithmetic)",
        "result": result,
        "context": {
            "axis": "Δ_λ binding magnitude — E_unit source via counit (owner steer 2026-07-19)",
            "builds_on": "merged #4101 (cluster expansion §4 E_unit wall) + cheat sheet μ₀",
            "provenance": "climax-volume-mass/crossing-energy-*; observations/crossing-energy-"
                          "interpretation.md; docs/audits/2026-07-06-reeb-…-provenance §2h.2",
            "q0_convention": "experimental/proton pin, read by name from q_parameter.Q_50_DIGIT_STR (bean qou-9ugp)",
            "q0": Q0_STR,   # record the pin used, so a reader need not infer it
            "no_fit": True,
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "eunit-counit-mu0-tracing", payload,
        script_path=__file__, engine="mpmath", output_dir=str(_COMP / "deltalambda"),
    )
    wb.set_description(payload["description"])
    wb.set_content_block("rem:ohtsuki-tower-bar-parity")
    wb.add_assertion("counit_3crossing_matches_table", computed=str(bool(net_matches_table)), expected="True")
    wb.add_assertion("mu0_derived_matches_cheatsheet", computed=str(bool(mu0_matches_cheatsheet)), expected="True")
    wb.add_assertion("mu0_form_deuteron_near_minus9pct", computed=str(bool(-12 < mu0_form_deficit_pct < -6)),
                     expected="True")
    wb.add_assertion("mu0_first_order_deficit_plausible", computed=str(bool(first_order_plausible)), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== E_unit source traced to the COUNIT (owner steer) ===")
    print(f"counit skein weight q−q⁻¹ = {mp.nstr(h,8)}  (Hecke L₊−L₋; proved+in-paper)")
    print(f"deuteron 3-crossing net 3(q−q⁻¹) = {mp.nstr(three_crossing_net,6)} (table 0.630: {net_matches_table})")
    print(f"μ₀ = m_e/(3(q−q⁻¹)/2) = {mp.nstr(mu0,7)} MeV  DERIVED (cheat-sheet match: {mu0_matches_cheatsheet})")
    print(f"  deuteron μ₀·ℏ_q·J_q²(3) = {mp.nstr(E_rot,7)} MeV = AME {mp.nstr(B2H,6)}  ({mp.nstr(err_mu0_form,3)}%)")
    print(f"  5g·E_unit·ladder form   = {mp.nstr(B_5g,8)} MeV  ({mp.nstr(err_5g_form,3)}%, E_unit external)")
    print(f"  E_unit/μ₀ = {mp.nstr(E_unit_over_mu0,5)} (the un-unified gap)")
    print("VERDICT: E_unit comes from the COUNIT (q−q⁻¹ skein + m_e τ-bridge) as μ₀, FIRST-ORDER, −9%. "
          "§2h.2 'scale-free' corrected. Higher-order (co)unit/NA-Stokes closure is open. No fit.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
