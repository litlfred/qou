#!/usr/bin/env python3
"""
Option D (bean `qou-dvlt`): the c_3 front's actual deliverable, as a measurement
budget a nuclear-physics reader can act on.

The front is precision-blocked, not idea-blocked (front (e), PR #5093). Every
c_3 claim is gated by one experimental number, amplified by one factor:

    c_3 = (Q_beta^exp / Q_N2(q) - 1) / u(q)^3
    =>  dc_3/dQ_beta = 1 / (Q_N2 u^3)  ~  2.07e6 per MeV

so sigma(c_3) = sigma(Q_beta) * 2.07e6. At the present sigma(Q_beta) = 0.61 eV
that is +/-1.262 against |c_3| ~ 2.02 — a 62%-uncertain target, which is why the
"agrees to 0.48%" headline was worth 0.03 sigma.

THIS PROBE ANSWERS "WHICH MEASUREMENT, AND BY HOW MUCH". Two things make the ask
concrete rather than a bare factor:

  1. **Q_beta is reachable two ways**, and the corpus carries both. The direct
     CAL-3 value has sigma = 0.61 eV; the mass-difference route
     Q_beta = m_n - m_p - m_e gives sqrt(s_n^2 + s_p^2 + s_e^2) = 0.561 eV from
     the committed CODATA-2022 validation masses.

     **DO NOT read that as a free 9% improvement.** The quadrature sum assumes
     the three inputs are INDEPENDENT, and they are not: AME2020 is a global
     least-squares adjustment in which m_n, m_p and the neutron Q-value are
     correlated outputs of the same fit. Without the covariance — which this
     repository does not carry — the mass-difference sigma is a LOWER BOUND, not
     a measurement of the route's true precision. All factors below are therefore
     quoted against the DIRECT sigma = 0.61 eV, which needs no covariance to be
     meaningful. The mass-difference number is reported for orientation only.

  2. **The variance budget is lopsided.** sigma(m_n) = 0.48 eV against
     sigma(m_p) = 0.29 eV, so the neutron mass carries the large majority of the
     variance. An improvement programme that does not touch m_n cannot deliver
     the factors below.

WHAT IS *NOT* CLAIMED HERE. Whether any of these targets is experimentally
reachable, by what technique, or at what cost, is outside what this repository
can assess. The probe reports required sigmas; a domain reader supplies the
feasibility. Saying which number to improve is useful; pretending to know how is
not.

Scope-(a): an error-propagation budget on committed values. No fit, no new
measurement, no c_k wired, and no claim about (H1) either way.
"""

import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(60):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))

MEV_TO_EV = mp.mpf(10) ** 6


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def _cal3_sigma() -> tuple[mp.mpf, str]:
    with open(ROOT / "computations" / "cal-3-q-beta.witness.json") as f:
        w = json.load(f)
    return (mp.mpf(str(w["data"]["Q_beta_n_MeV_err"])),
            w["data"]["Q_beta_n_MeV_quoted"])


def main() -> int:
    q_p, q_m = q_at(), q_muon_at()
    sigma_direct, quoted = _cal3_sigma()

    print("=" * 78)
    print("Option D — the c_3 front as a measurement budget")
    print("=" * 78)

    # ---- the lever -------------------------------------------------------
    s = substrate_ladder_quantities(q_p)
    u = s["u"]
    c3p = c3_target_at(q_p, QCOD, ME)
    q_n2 = QCOD / (1 + c3p * u ** 3)
    lever = 1 / (q_n2 * u ** 3)

    print("\n" + "-" * 78)
    print("THE LEVER — one experimental number, one amplification")
    print("-" * 78)
    print(f"\n  u(q0)                = {mp.nstr(u, 12)}")
    print(f"  1/u^3                = {mp.nstr(1 / u ** 3, 10)}")
    print(f"  dc_3/dQ_beta         = 1/(Q_N2 u^3) = {mp.nstr(lever, 10)} per MeV")
    print(f"  Q_beta (CAL-3)       = {quoted}")
    print(f"  sigma(Q_beta) direct = {mp.nstr(sigma_direct * MEV_TO_EV, 6)} eV")
    print(f"  => sigma(c_3)        = {mp.nstr(lever * sigma_direct, 10)}"
          f"   ({mp.nstr(lever * sigma_direct / abs(c3p) * 100, 5)} % of |c_3|)")

    # ---- the two routes to Q_beta ---------------------------------------
    print("\n" + "-" * 78)
    print("WHICH MEASUREMENT — two routes to Q_beta, and the variance budget")
    print("-" * 78)
    s_n = mp.mpf(str(C.M_N_MEV_VALIDATION_ERR))
    s_p = mp.mpf(str(C.M_P_MEV_VALIDATION_ERR))
    s_e = mp.mpf(str(getattr(C, "M_E_MEV_ERR", 0)))
    sigma_massdiff = mp.sqrt(s_n ** 2 + s_p ** 2 + s_e ** 2)

    var_tot = s_n ** 2 + s_p ** 2 + s_e ** 2
    print(f"\n  route 1  direct CAL-3                     sigma = "
          f"{mp.nstr(sigma_direct * MEV_TO_EV, 6)} eV")
    print(f"  route 2  Q_beta = m_n - m_p - m_e          sigma = "
          f"{mp.nstr(sigma_massdiff * MEV_TO_EV, 6)} eV")
    better = "mass-difference" if sigma_massdiff < sigma_direct else "direct CAL-3"
    print(f"\n  smaller in quadrature: {better}"
          f"   (ratio {mp.nstr(sigma_direct / sigma_massdiff, 6)})")
    print("  *** NOT a free improvement: AME2020 is a GLOBAL least-squares")
    print("      adjustment, so m_n, m_p and Q_beta are CORRELATED. Without the")
    print("      covariance the quadrature sum is a LOWER BOUND. Factors below")
    print("      are quoted against the DIRECT sigma, which needs no covariance.")
    print(f"\n  variance budget of route 2:")
    for nm, sg in (("m_n", s_n), ("m_p", s_p), ("m_e", s_e)):
        share = (sg ** 2 / var_tot * 100) if var_tot > 0 else mp.mpf(0)
        print(f"    sigma({nm}) = {mp.nstr(sg * MEV_TO_EV, 6):>10} eV"
              f"    {mp.nstr(share, 5):>8} % of variance")
    print("\n  => an improvement programme that does not touch m_n cannot")
    print("     deliver the factors below.")

    # Quote factors against the DIRECT sigma: the mass-difference quadrature
    # ignores AME2020 correlations and is a lower bound, not a usable sigma.
    sigma_baseline = sigma_direct

    # ---- the thresholds --------------------------------------------------
    print("\n" + "-" * 78)
    print("THE TARGETS — what each level of sigma(Q_beta) buys")
    print("-" * 78)

    # (i) zero-location test resolves at the mu-p pin spread
    spread = abs(q_p - q_m)
    with open(ROOT / "docs" / "audits" / "scripts"
              / "qbeta-qstar-experimental-budget.witness.json") as f:
        bw = json.load(f)["result"]
    dqstar_dQ = abs(mp.mpf(bw["dqstar_dQbeta_per_MeV"]))
    sigma_qb_for_zero = spread / dqstar_dQ

    # (ii)/(iii) c_3 ~ -Vol(4_1) reaches 1 sigma at each anchor
    rows = []
    for name, q in (("proton", q_p), ("muon", q_m)):
        c3 = c3_target_at(q, QCOD, ME)
        disc = abs(c3 - (-VOL41))
        need_sigma_qb = disc / lever
        rows.append((f"c_3 ~ -Vol(4_1) at 1 sigma ({name})", need_sigma_qb, disc))

    targets = [("zero-location test resolves at mu-p scale",
                sigma_qb_for_zero, spread)] + rows

    print(f"\n  {'target':<44} {'need sigma(Q_b)':>16} {'factor':>9}")
    budget = []
    for label, need, ref in targets:
        factor = sigma_baseline / need
        budget.append({"target": label,
                       "required_sigma_Qbeta_eV": mp.nstr(need * MEV_TO_EV, 6),
                       "improvement_factor": mp.nstr(factor, 6)})
        print(f"  {label:<44} {mp.nstr(need * MEV_TO_EV, 4):>13} eV"
              f" {mp.nstr(factor, 5):>8}x")

    print(f"\n  (factors are against the DIRECT sigma, "
          f"{mp.nstr(sigma_baseline * MEV_TO_EV, 4)} eV — see the correlation note above)")

    # ---- one measurement or two? ----------------------------------------
    print("\n" + "-" * 78)
    print("ONE MEASUREMENT OR TWO — the routes differ, and it is not a detail")
    print("-" * 78)
    print("\n  The mass-difference route adds in quadrature, so EACH input must")
    print("  individually fall below the target. sigma(m_p) alone already exceeds")
    print("  every target below, so that route needs TWO campaigns, not one.\n")
    print(f"  {'target':<34}{'need':>10}  {'direct':>8} {'m_n':>8} {'m_p':>8}")
    per_meas = []
    for label, need, _ref in targets:
        f_d, f_n, f_p = sigma_baseline / need, s_n / need, s_p / need
        per_meas.append({"target": label,
                         "required_sigma_eV": mp.nstr(need * MEV_TO_EV, 6),
                         "factor_direct_Qbeta": mp.nstr(f_d, 6),
                         "factor_m_n": mp.nstr(f_n, 6),
                         "factor_m_p": mp.nstr(f_p, 6),
                         "massdiff_route_needs_both": bool(f_p > 1)})
        print(f"  {label:<34}{mp.nstr(need * MEV_TO_EV, 4):>8} eV "
              f"{mp.nstr(f_d, 4):>7}x {mp.nstr(f_n, 4):>7}x {mp.nstr(f_p, 4):>7}x")
    print(f"\n  sigma(m_p) = {mp.nstr(s_p * MEV_TO_EV, 4)} eV exceeds every target,")
    print("  so: DIRECT route = one measurement improved ~26x;")
    print("      MASS-DIFF route = two measurements improved ~20x and ~12x.")
    print("  Which is the cheaper programme is a domain question, not one this")
    print("  repository can answer — but the choice is now stated in the form an")
    print("  experimentalist works in.")

    print("\n" + "-" * 78)
    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("""
  Whether any of these is experimentally reachable, by what technique, or at
  what cost, is outside what this repository can assess. The budget reports
  required sigmas; a domain reader supplies the feasibility.

  Saying which number to improve is useful. Pretending to know how is not.
""")

    assertions = [
        {"name": "lever_is_one_over_QN2_u_cubed",
         "passed": bool(abs(lever - 1 / (q_n2 * u ** 3)) < mp.mpf("1e-40"))},
        {"name": "sigma_c3_exceeds_half_of_abs_c3",
         "passed": bool(lever * sigma_direct > abs(c3p) / 2),
         "detail": "target is " + mp.nstr(lever * sigma_direct / abs(c3p) * 100, 5)
                   + "% uncertain"},
        {"name": "neutron_mass_dominates_the_variance",
         "passed": bool(s_n ** 2 / var_tot > mp.mpf("0.5")),
         "detail": mp.nstr(s_n ** 2 / var_tot * 100, 5) + "% of variance"},
        {"name": "all_targets_need_improvement",
         "passed": bool(all(mp.mpf(b["improvement_factor"]) > 1 for b in budget))},
        {"name": "massdiff_route_needs_both_masses_improved",
         "passed": bool(all(pm["massdiff_route_needs_both"] for pm in per_meas)),
         "detail": "sigma(m_p) = " + mp.nstr(s_p * MEV_TO_EV, 4)
                   + " eV alone exceeds every target"},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(os.path.abspath(__file__), "rb") as f:
        src = f.read()

    witness = {
        "computation": "qbeta-c3-measurement-proposal-budget",
        "description": (
            "Option D: the c_3 front's deliverable as a measurement budget. Every c_3 "
            "claim is gated by sigma(Q_beta) amplified by dc_3/dQ_beta = 1/(Q_N2 u^3) "
            "~ 2.07e6 per MeV, giving sigma(c_3) = +/-1.26 against |c_3| ~ 2.02 — a "
            "62%-uncertain target. Makes the ask concrete two ways: (1) Q_beta is "
            "reachable both directly (CAL-3) and as m_n - m_p - m_e, and this probe "
            "computes both sigmas from committed values so the cheaper route is "
            "visible; (2) the mass-difference variance is dominated by the NEUTRON "
            "mass, so a programme not touching m_n cannot deliver the factors. "
            "Reports required sigma(Q_beta) for the zero-location test and for the "
            "c_3 ~ -Vol(4_1) comparison at each anchor. Explicitly does NOT assess "
            "experimental feasibility — outside what this repo can judge. Scope-(a); "
            "no fit, no c_k wired, no claim about (H1)."),
        "audit_only": True,
        "tier": "error propagation on committed values (no fit)",
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q_p, 25),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "u_at_q0": mp.nstr(u, 16),
            "inv_u_cubed": mp.nstr(1 / u ** 3, 12),
            "lever_dc3_dQbeta_per_MeV": mp.nstr(lever, 12),
            "Qbeta_quoted": quoted,
            "sigma_Qbeta_direct_eV": mp.nstr(sigma_direct * MEV_TO_EV, 8),
            "sigma_Qbeta_massdiff_eV": mp.nstr(sigma_massdiff * MEV_TO_EV, 8),
            "smaller_route_in_quadrature": better,
            "massdiff_is_lower_bound_only": "AME2020 is a global least-squares adjustment; m_n, m_p, Q_beta are correlated and the covariance is not carried here. Factors are quoted against the direct sigma.",
            "factor_baseline_sigma_eV": mp.nstr(sigma_direct * MEV_TO_EV, 8),
            "sigma_m_n_eV": mp.nstr(s_n * MEV_TO_EV, 8),
            "sigma_m_p_eV": mp.nstr(s_p * MEV_TO_EV, 8),
            "sigma_m_e_eV": mp.nstr(s_e * MEV_TO_EV, 8),
            "neutron_variance_share_pct": mp.nstr(s_n ** 2 / var_tot * 100, 6),
            "proton_variance_share_pct": mp.nstr(s_p ** 2 / var_tot * 100, 6),
            "sigma_c3_today": mp.nstr(lever * sigma_direct, 12),
            "sigma_c3_over_abs_c3_pct": mp.nstr(
                lever * sigma_direct / abs(c3p) * 100, 6),
            "budget": budget,
            "per_measurement_requirement": per_meas,
            "sigma_m_p_exceeds_every_target": True,
        },
        "context": {
            "axis": "front (a)/(e) triage, option D — the measurement ask",
            "inputs": [
                "computations/cal-3-q-beta.witness.json (direct sigma)",
                "computations/substrate/codata_constants.py "
                "(M_N/M_P/M_E validation masses + errors, CODATA-2022)",
                "docs/audits/scripts/qbeta-qstar-experimental-budget.witness.json "
                "(dq*/dQ_beta)",
            ],
            "not_claimed": (
                "experimental feasibility, technique, or cost of any target — "
                "outside what this repository can assess"),
            "scope": "Scope-(a). No fit; no claim about (H1) in either direction.",
        },
    }

    out_path = HERE / "qbeta-c3-measurement-proposal-budget.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    with open(out_path, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
    print(f"witness -> {out_path}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
