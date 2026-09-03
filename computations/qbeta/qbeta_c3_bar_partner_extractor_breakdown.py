#!/usr/bin/env python3
"""
`qou-qb8g` obstacle 1, made quantitative: the c_3 EXTRACTOR cannot be continued
to the bar-partner point 1/q0, and (H1) makes a concrete demand there that it
misses by five orders of magnitude.

qb8g states the obstacle qualitatively:

    "Not empirically accessible. c_3^even(q) = (c_3(q)+c_3(1/q))/2 needs c_3 at
     q ~ 0.901. Both anchors sit at q ~ 1.10998. No amount of anchor data
     determines the split."

That is true but understates it. The extractor

    c_3(q) = (Q_beta^exp / Q_N2(q) - 1) / u(q)^3          qbeta_utils.c3_target_at

IS an explicit function of q and CAN be evaluated at 1/q0. The point is what
comes out. `Q_beta^exp` is held FIXED while q moves by ~21% (the docstring of
`c3_target_at` says so in as many words: "the SAME at every substrate anchor --
it is a physical constant, not a function of q"). Away from the anchor the
numerator is therefore O(1) rather than O(u^3), and the 1/u^3 inversion turns
that into O(1e5).

So the naive continuation is not merely uninformative -- it is DOMINATED by the
fixed-Q_beta artifact, and anyone who evaluates `c3_target_at(1/q0)` and reads
the result as "c_3 at the bar-partner" gets a number that is ~1.7e5 times the
value at the anchor.

WHAT (H1) DEMANDS THERE. If c_3^even = -Vol(4_1) then

    c_3(1/q0) = 2*(-Vol(4_1)) - c_3(q0)

which is an O(1) number, and it is what any fibre carrier must reproduce there.

BUT IT IS NOT NEW INFORMATION, and this probe asserts that rather than leaving
it implied. (H1) is EQUIVALENT to "S_leak IS the bar-odd part", so the implied
bar-odd value is identically S_leak(q0) (checked to 0.0). The value at 1/q0 is
the ANCHOR datum transported by (H1), not an independent measurement. Per
AGENTS.md "Defined residual != derived decomposition", it must not be reported
as an out-of-sample test. Its discriminating power is also coarse: c_3(q0)
carries +/-1.262 propagated CAL-3 and the demand inherits that band.

What IS gained is METHODOLOGICAL, and it is the point of this probe. Combined
with the companion below, at 1/q0 the extractor is useless but (H1) still names
a value AND the carrier is inside its domain of convergence -- so a carrier can
be compared to (H1) without ever evaluating on the divergent side. The
comparison becomes possible; it does not become sharper.

STRUCTURAL COMPANION (PR #5084, `HabiroEvaluationTrichotomy.lean`): a fibre
carrier written as a q-series converges at 1/q0 < 1 and NOT at q0 > 1. So the
bar-even combination (F(q0) + F(1/q0))/2 cannot be formed from a single series
-- one term is outside the domain. That is a domain obstruction to the parity
read-off as usually stated, and it is why the object needed is a PAIR (or a
state integral holomorphic off the reals), not one series.

Arithmetic on committed values. No fit, no new measurement, no c_k wired.
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
from qou_substrate.constants import q_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60

ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(60):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))  # Vol(4₁) = 2·Cl₂(π/3), forced period

# c_3's propagated CAL-3 uncertainty at an anchor (registry §9e; the
# aomega_o2_stokes_to_observable_mechanism probe fires O1-remove on it).
C3_CAL3_BAND = mp.mpf("1.262")


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def main() -> int:
    q0 = q_at()          # experimental (proton) pin — 2026-08-07 owner directive
    qb = 1 / q0

    print("=" * 76)
    print("qb8g obstacle 1 — the c_3 extractor at the bar-partner 1/q0")
    print("=" * 76)
    print(f"\n  q0   = {mp.nstr(q0, 22)}   (experimental / proton pin)")
    print(f"  1/q0 = {mp.nstr(qb, 22)}")
    print(f"  Vol(4_1) = 2*Cl_2(pi/3) = {mp.nstr(VOL41, 14)}")

    print("\n" + "-" * 76)
    print("What the extractor returns at each point")
    print("-" * 76)

    out = {}
    for label, q in (("q0", q0), ("inv_q0", qb)):
        s = substrate_ladder_quantities(q)
        u = s["u"]
        c3 = c3_target_at(q, QCOD, ME)
        # the numerator, exposed — this is where the artifact lives
        numer = c3 * u ** 3
        out[label] = {"q": mp.nstr(q, 22), "u": mp.nstr(u, 16),
                      "inv_u_cubed": mp.nstr(1 / u ** 3, 12),
                      "numerator_Qcod_over_QN2_minus_1": mp.nstr(numer, 12),
                      "c3_extractor": mp.nstr(c3, 16)}
        nm = "q0  " if label == "q0" else "1/q0"
        print(f"\n  {nm}   u = {mp.nstr(u, 12)}     1/u^3 = {mp.nstr(1 / u ** 3, 10)}")
        print(f"         numerator (Q_cod/Q_N2 - 1) = {mp.nstr(numer, 12)}")
        print(f"         c_3 = numerator / u^3      = {mp.nstr(c3, 14)}")

    c3p = c3_target_at(q0, QCOD, ME)
    c3m = c3_target_at(qb, QCOD, ME)

    # the u-scaling is exact and predictable: u(1/q) = q^2 * u(q)
    u_p = substrate_ladder_quantities(q0)["u"]
    u_m = substrate_ladder_quantities(qb)["u"]
    u_ratio = u_m / u_p
    u_ratio_pred = q0 ** 2
    u_law_err = abs(u_ratio - u_ratio_pred) / u_ratio_pred
    print(f"\n  u(1/q0)/u(q0) = {mp.nstr(u_ratio, 14)}   vs predicted q0^2 = "
          f"{mp.nstr(u_ratio_pred, 14)}   rel.err {mp.nstr(u_law_err, 4)}")
    print("    (hbar_q = 1 - 1/q, so hbar_{1/q}^2 = q^2 * hbar_q^2 exactly —")
    print("     the u shift is TAME. The blow-up is entirely the numerator.)")

    numer_p = c3p * u_p ** 3
    numer_m = c3m * u_m ** 3
    numer_blowup = abs(numer_m / numer_p)
    print(f"\n  numerator ratio |N(1/q0)/N(q0)| = {mp.nstr(numer_blowup, 10)}")
    print("    => the artifact is Q_beta^exp held fixed while q moves ~21%.")

    print("\n" + "-" * 76)
    print("The extractor's 'bar decomposition' — and why it is meaningless")
    print("-" * 76)
    bar_even = (c3p + c3m) / 2
    bar_odd = (c3p - c3m) / 2
    print(f"\n  (c_3(q0) + c_3(1/q0))/2 = {mp.nstr(bar_even, 14)}")
    print(f"  (c_3(q0) - c_3(1/q0))/2 = {mp.nstr(bar_odd, 14)}")
    print(f"  -Vol(4_1), the (H1) candidate = {mp.nstr(-VOL41, 14)}")
    even_overshoot = abs(bar_even / VOL41)
    print(f"\n  |extractor bar-even| / Vol(4_1) = {mp.nstr(even_overshoot, 10)}")
    print("    The extractor's bar-even part is ~5 orders of magnitude off the")
    print("    (H1) candidate. It is the fixed-Q_beta artifact, not a split.")

    print("\n" + "-" * 76)
    print("What (H1) actually demands at 1/q0")
    print("-" * 76)
    c3m_required = -2 * VOL41 - c3p
    print(f"\n  (H1): c_3^even = -Vol(4_1)  =>  c_3(1/q0) = -2*Vol(4_1) - c_3(q0)")
    print(f"                                            = {mp.nstr(c3m_required, 14)}")
    print(f"  extractor gives                            {mp.nstr(c3m, 14)}")
    ratio_req = abs(c3m / c3m_required)
    print(f"  discrepancy factor                         {mp.nstr(ratio_req, 10)}")
    print(f"\n  Band: c_3(q0) carries +/-{mp.nstr(C3_CAL3_BAND, 5)} propagated CAL-3, so the")
    print(f"  demand inherits it: c_3(1/q0) = {mp.nstr(c3m_required, 8)} +/- "
          f"{mp.nstr(C3_CAL3_BAND, 5)}.")
    print("  Coarse — but the discrimination here is O(1) vs O(1e5), which the")
    print("  band does not touch.")

    # --- honesty check on the demand itself -------------------------------
    # (H1) c_3^even = -Vol(4_1) is EQUIVALENT to "S_leak IS the bar-odd part",
    # so the implied bar-odd value is S_leak(q0) identically, not a new datum.
    implied_bar_odd = (c3p - c3m_required) / 2
    s_leak_q0 = c3p + VOL41
    tautology_err = abs(implied_bar_odd - s_leak_q0)
    print("\n  HONESTY CHECK — this demand is NOT new information.")
    print(f"    implied bar-odd (c_3(q0) - c_3(1/q0)_req)/2 = {mp.nstr(implied_bar_odd, 14)}")
    print(f"    S_leak(q0) = c_3(q0) + Vol(4_1)             = {mp.nstr(s_leak_q0, 14)}")
    print(f"    difference                                  = {mp.nstr(tautology_err, 4)}")
    print("    They are identically equal: (H1) just says S_leak IS the bar-odd")
    print("    part, so the value at 1/q0 is the ANCHOR datum transported by (H1),")
    print("    not an independent measurement. Per AGENTS.md 'Defined residual !=")
    print("    derived decomposition', do not report it as an out-of-sample test.")
    print("\n    What IS gained is METHODOLOGICAL, and it is the point of this probe:")
    print("    a fibre carrier written as a q-series converges at 1/q0 and NOT at")
    print("    q0 (PR #5084). At 1/q0 the extractor is useless but (H1) still names")
    print("    a value, so the carrier can be compared to (H1) WITHOUT ever")
    print("    evaluating on the divergent side. The comparison becomes possible;")
    print("    it does not become sharper.")

    # assertions
    extractor_blows_up = abs(c3m) > mp.mpf("1e4")
    anchor_is_O1 = abs(c3p) < mp.mpf("10")
    required_is_O1 = abs(c3m_required) < mp.mpf("10")
    u_law_ok = u_law_err < mp.mpf("1e-40")
    band_does_not_bridge = abs(c3m - c3m_required) > 100 * C3_CAL3_BAND

    assertions = [
        {"name": "u_shift_is_tame_q_squared", "passed": bool(u_law_ok),
         "detail": "u(1/q) = q^2 u(q) exactly; rel.err " + mp.nstr(u_law_err, 4)},
        {"name": "extractor_at_bar_partner_blows_up", "passed": bool(extractor_blows_up),
         "detail": "|c_3^extr(1/q0)| = " + mp.nstr(abs(c3m), 10)},
        {"name": "extractor_at_anchor_is_O1", "passed": bool(anchor_is_O1)},
        {"name": "H1_demand_at_bar_partner_is_O1", "passed": bool(required_is_O1),
         "detail": "c_3(1/q0) required = " + mp.nstr(c3m_required, 12)},
        {"name": "cal3_band_cannot_bridge_the_gap", "passed": bool(band_does_not_bridge),
         "detail": "gap is >100x the +/-1.262 band"},
        {"name": "H1_demand_is_the_anchor_datum_transported_not_new_info",
         "passed": bool(tautology_err < mp.mpf("1e-40")),
         "detail": "implied bar-odd == S_leak(q0) identically; difference "
                   + mp.nstr(tautology_err, 4)},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(os.path.abspath(__file__), "rb") as f:
        src = f.read()

    witness = {
        "computation": "qbeta-c3-bar-partner-extractor-breakdown",
        "description": (
            "qou-qb8g obstacle 1 made quantitative. The c_3 extractor "
            "c_3 = (Q_beta^exp/Q_N2(q) - 1)/u(q)^3 is an explicit function of q and "
            "CAN be evaluated at the bar-partner 1/q0, but Q_beta^exp is held fixed "
            "while q moves ~21%, so away from the anchor the numerator is O(1) rather "
            "than O(u^3) and the 1/u^3 inversion returns O(1e5). Measured: "
            "c_3^extr(q0) = -2.069, c_3^extr(1/q0) = -352600 (1.7e5x). The u shift "
            "itself is tame — u(1/q) = q^2 u(q) exactly — so the blow-up is entirely "
            "the fixed-Q_beta artifact. Consequently the extractor's 'bar-even part' "
            "is -176301, about 8.7e4 x Vol(4_1), and is not a bar split. Separately, "
            "(H1) c_3^even = -Vol(4_1) DEMANDS c_3(1/q0) = -2 Vol(4_1) - c_3(q0), an "
            "O(1) number. That demand is NOT new information — it equals the anchor datum "
            "transported by (H1) (the implied bar-odd part is identically S_leak(q0)) — "
            "so it must not be reported as an out-of-sample test. What is gained is "
            "methodological: a fibre carrier converges at 1/q0 and not at q0 (PR #5084), "
            "so at 1/q0 the carrier can be compared to (H1) without evaluating on the "
            "divergent side. The comparison becomes possible, not sharper. "
            "Arithmetic on committed values; no fit, no c_k wired."),
        "audit_only": True,
        "tier": "exact arithmetic on the committed extractor (no fit)",
        # Declare the pin (AGENTS.md 2026-08-07 owner directive). NOTE: this
        # probe deliberately EVALUATES at 1/q0 as well, but the witness's
        # anchor is the proton pin q0 — 1/q0 is a derived point, not a second
        # anchor, and must not be read as one.
        "q0Anchor": "proton",
        "q0Value": mp.nstr(q0, 25),
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "q0": mp.nstr(q0, 22),
            "inv_q0": mp.nstr(qb, 22),
            "vol_4_1": mp.nstr(VOL41, 16),
            "per_point": out,
            "u_ratio_measured": mp.nstr(u_ratio, 16),
            "u_ratio_predicted_q0_squared": mp.nstr(u_ratio_pred, 16),
            "numerator_blowup_factor": mp.nstr(numer_blowup, 12),
            "extractor_bar_even": mp.nstr(bar_even, 16),
            "extractor_bar_odd": mp.nstr(bar_odd, 16),
            "extractor_bar_even_over_vol41": mp.nstr(even_overshoot, 12),
            "c3_at_inv_q0_required_by_H1": mp.nstr(c3m_required, 16),
            "c3_at_inv_q0_from_extractor": mp.nstr(c3m, 16),
            "discrepancy_factor": mp.nstr(ratio_req, 12),
            "c3_cal3_band_at_anchor": mp.nstr(C3_CAL3_BAND, 6),
            "implied_bar_odd_at_q0": mp.nstr(implied_bar_odd, 16),
            "s_leak_at_q0": mp.nstr(s_leak_q0, 16),
            "tautology_residual": mp.nstr(tautology_err, 6),
        },
        "context": {
            "axis": "qou-qb8g — c_3 bar-parity; the bar-partner evaluation point",
            "inputs": [
                "computations/qbeta/qbeta_utils.py::c3_target_at",
                "tools/qou-substrate/.../constants.py::q_at (proton pin)",
                "substrate.codata_constants (m_e, Q_beta)",
            ],
            "companion": (
                "PR #5084 QOU.QBeta.HabiroEvaluationTrichotomy — a fibre carrier "
                "written as a q-series converges at 1/q0 < 1 and NOT at q0 > 1, so "
                "the bar-even combination cannot be formed from a single series. "
                "Domain obstruction, complementary to the numerical one here."),
            "scope": (
                "Scope-(a) throughout. This does NOT refute (H1) — it shows the "
                "EXTRACTOR cannot test it at the bar-partner, and states what a "
                "fibre carrier must return there instead. No invariant is named "
                "forbidding a 4_1-volume ingredient in c_3's bar-even part."),
        },
    }

    out_path = HERE / "qbeta-c3-bar-partner-extractor-breakdown.witness.json"
    with open(out_path, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)
    print(f"\nwitness -> {out_path}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
