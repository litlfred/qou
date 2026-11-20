#!/usr/bin/env python3
"""qou-cds1: the four determinations of z, priced against the CAL inputs — and
there is no D-frame anchor for the c_k ladder.

WHY THIS AND NOT A RE-DERIVATION. Both routes to re-deriving the ladder under
convention D are blocked at the ANCHOR, not the extraction (this bean, Finding A,
2026-08-31): the per-rung route needs `c_2 = -1` as its gate and that is a
C-frame statement; the global-trace route is dead independent of convention.
Before looking for a D-frame anchor it is worth asking whether one can exist —
and that is an experimental question the corpus had not put.

THE SETUP THIS INHERITS. For a NORMALISED Markov trace the 3x3 Markov system
consumes all freedom, so the weights are a one-parameter family in `z` and
`y_(1^3)` is a function of `z` alone (this bean's correction to PR #6144's
"jointly determined" framing). Every channel therefore determines THE SAME
scalar, and the system is OVER-determined. The corpus records three
determinations at the muon pin — cap 0.612688050638 (derived,
`FibreDimensionForcesTL.lean`), mass 0.612812650836 ("0.0203 %"), decay
0.998500302563 ("62.97 %") — and **not one of them carries an error bar**. An
over-determined system with no error bars cannot tell a real tension from a
leverage artefact, and the standing reading ("the anomaly is localised to the
decay channel; mass essentially confirms the cap") rests on exactly that
distinction.

METHOD. Every CAL input is shifted +-1 sigma of its CODATA-2022 published
uncertainty and BOTH ENDS OF EACH GAP ARE RECOMPUTED TOGETHER, so correlations
survive — `q0` is itself a function of `m_mu/m_e`, so the cap and the mass
determination move together and a naive per-quantity bar would be wrong in both
directions. Same discipline as the c_3 budget
(`qbeta-c3-muon-anchor-codata-edition-attribution`).

WHAT IT FINDS

  1. THE MASS CHANNEL DOES NOT CONFIRM THE CAP. The quoted "0.0203 %" is
     **9.49 sigma**. It is four and a half orders of magnitude closer than the
     decay channel and it is still a decisive disagreement. The sentence "an
     independent, non-circular measurement puts z essentially where the derived
     cap puts it" does not survive its own error bar and should not be used to
     localise the anomaly to decay.

  2. AND THAT 9.49 IS NOT A NEW NUMBER — three corpus facts are ONE measurement.
     The mu-p substrate tension (11.6 ppb), the c_3 cross-anchor swing, and this
     mass-vs-cap gap in `z` all evaluate to **9.4936 sigma**, because all three
     are the same quantity: the gap between the muon-pinned and proton-pinned
     `q`, divided by CODATA's uncertainty on `m_mu/m_e`. They are carried in the
     corpus as three separate facts in three coordinates.

  3. `c_2 = -1` IS A 1.6-SIGMA EMPIRICAL STATEMENT, NOT A THEOREM AND NOT A
     "1.76 % MISS". Implied `c_2` at `z_C` is `-1.0172 +- 0.0107` (the bar is
     `Q_beta`'s 0.78 ppm divided by `u^2 = 7.3e-5`). So the corpus's two
     readings are both wrong in opposite directions: the red team's "the Lean is
     a ring tautology, the identification is asserted" is right that it is not
     proved, and the extraction's "-1.0176 vs -1" is not a 1.76 % failure — it
     is agreement at 1.6 sigma. Under D the same quantity is `-9.2984`, which is
     **773 sigma** from -1.

  4. THE LADDER'S ANCHOR IS ITSELF A MEASUREMENT OF z, AND IT SELECTS C. Solving
     implied-`c_2` `= -1` for `z` at fixed `q` gives a FOURTH determination,
     `z = 0.499110 +- 0.000132`, which sits **1.60 sigma** from `z_C` and
     **863 sigma** from the derived cap `z_D`. So the ladder is not merely
     *written* in convention C: its empirical anchor independently measures the
     Markov parameter and lands on `z_C`.

  5. THEREFORE THERE IS NO D-FRAME ANCHOR, and that is the answer to what this
     bean has been asking. The object that would play `c_2 = -1`'s role under D
     is excluded by the same data that supports it under C, at 773 sigma. "Re-
     derive the ladder under D" cannot proceed by finding a D-frame `c_2`: the
     ladder's FORM has to change, not its parameter. This is the anchor-side
     statement of what `decayLadder_zC_threeRow_ne_zero` says structurally.

  6. AND THE TWO DECAY-SIDE FUNCTIONALS DISAGREE WITH EACH OTHER. The trace
     reduction wants `z = 0.9985`; the ladder wants `z = 0.4991`. Both claim to
     reproduce the same `Q_beta`, so they are reconcilable only by a scale `K`
     off by **2.2656x**, i.e. 126.6 % — against the 6.31 % wall Step 14 measured
     for parameter-free `K` corrections. That is **20x** outside it, so the
     disagreement is not a missing normalisation of the kind already searched
     for.

SCOPE. Scope-(a) measurement throughout. Nothing is derived, proposed, wired or
readmitted; no convention is adjudicated; no `c_k` value changes. In particular
a `z` landing near an inadmissible point is a statement of TENSION, not
permission to use that point — `one_not_root` stands, as does the derived cap.

Anchor: the MUON pin, which is the only convention-free one — the proton pin is
fixed *through* `F_Bor` and so presupposes what is under test.
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate")]
import _path_bridge  # noqa: E402, F401

from qbeta_z_symbolic_borromean_crosscheck import borromean_symbolic  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60

# ── CAL inputs at full published precision, read from the tables ──────────────
_MU = codata("muon-electron mass ratio")
_PE = codata("proton-electron mass ratio")
R_MU = mp.mpf(_MU.value_str)
R_MU_ERR = mp.mpf(_MU.uncertainty_str.replace(" ", ""))
R_P = mp.mpf(_PE.value_str)
R_P_ERR = mp.mpf(_PE.uncertainty_str.replace(" ", ""))
ME = mp.mpf(str(C.M_E_MEV))
ME_ERR = mp.mpf(str(C.M_E_MEV_ERR))
QB = mp.mpf(str(C.Q_BETA_MEV))
QB_ERR = mp.mpf(str(C.Q_BETA_MEV_ERR))

# The decay leg's data/theory ratio, from qbeta-d-frame-admissible-base-
# correction-search.witness.json (2026-08-29). Its base is proportional to
# tr_M(Delta_S), so F is linear in Q_beta and inverse-linear in m_e; that is how
# it is perturbed below. Reconstructing F rather than re-deriving it costs ~1.5e-8
# absolute on z_decay -- 0.02 sigma against a 0.386 gap, and asserted as a
# tolerance rather than assumed away.
F_REQUIRED_TRM = mp.mpf("1.75923699054610623")

# Committed values this probe must reproduce before its bars mean anything.
COMMITTED_Z_CAP = mp.mpf("0.6126880506382724")
COMMITTED_Z_MASS = mp.mpf("0.6128126508361218")
COMMITTED_Z_DECAY = mp.mpf("0.998500302563013")
K_WALL_PCT = mp.mpf("6.31")          # Step 14: closest parameter-free K correction


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def _build_trace():
    """The Borromean Markov trace with `z` SYMBOLIC, from the existing derivation.

    Imported rather than re-derived: `qbeta_z_symbolic_borromean_crosscheck`
    already carries the symbolic control (at `z = z_D` it reproduces
    `BorromeanMarkovTrace.lean`'s closed form identically, not to a tolerance),
    and a second spelling of the same object is exactly the kind of drift this
    bean keeps paying for.
    """
    trM, Y, X = borromean_symbolic()
    q, z = sp.symbols("q z", positive=True)
    return (sp.lambdify((q, z), trM, "mpmath"),
            sp.lambdify((q, z), sp.diff(trM, z), "mpmath"))


F_TR, D_TR = _build_trace()


def determinations(r_mu, r_p, me, qb) -> dict:
    """Every determination of `z` at one setting of the four CAL inputs.

    `q0` is the MUON pin `1/(1 - sqrt(Vol(4_1)/r_mu))` — pure geometry, no trace
    convention anywhere, which is why it is the pin this comparison can use.
    Note it moves with `r_mu`, so the cap and the mass determination are
    CORRELATED and must be recomputed together; that is the whole method.
    """
    vol41 = 2 * mp.clsin(2, mp.pi / 3)
    q0 = 1 / (1 - mp.sqrt(vol41 / r_mu))
    z_cap = q0 ** 3 / (q0 ** 2 + 1)               # y_(1^3) = 0, derived
    z_C = mp.sqrt(q0) / (1 + q0)                  # the excised convention

    # --- mass: the measured m_p read back through the symbolic trace ---
    b2, b3 = q0 + 1 / q0, q0 ** 2 + 1 + 1 / q0 ** 2
    trM_req = ((r_p / 2 + 6) / r_mu) / (b2 * b3 / q0 ** 3)
    z_mass = mp.findroot(lambda zz: F_TR(q0, zz) - trM_req, z_cap)

    # --- decay: g is AFFINE in z, so the inversion is exact and unique ---
    g_cap = (q0 ** 4 + 1) / (q0 ** 2 + 1) ** 2    # = g(z_D), since y_(1^3) = 0
    fac = F_REQUIRED_TRM * (qb / QB) * (ME / me)
    g_req = g_cap * fac
    z_decay = (g_req * (q0 ** 2 + 1) + q0 ** 2 - 1) / (2 * q0)

    # --- the ladder's own anchor, solved for z (the fourth determination) ---
    h = q0 - 1 / q0
    hbar = (q0 - 1) / q0
    b = mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))
    u = b * hbar ** 2
    q_a = me * mp.fabs(q0 ** 2 - 2 * q0 - 1) * (q0 + 1) / (2 * q0 ** 3)

    def c2_at(z):
        return (qb / (q_a * mp.cos((z - 1) * h / 2 - u / 2)) - 1) / u ** 2

    # cos is even, so alpha - u/2 = +-arccos(...): two branches, z ~ 0.499 and
    # z ~ 1.599. The lower one is taken; the upper is reported so the choice is
    # visible rather than silent, and NEITHER is the decay channel's 0.9985.
    arg = qb / (q_a * (1 - u ** 2))
    z_c2_lo = 1 + 2 * (u / 2 - mp.acos(arg)) / h
    z_c2_hi = 1 + 2 * (u / 2 + mp.acos(arg)) / h

    def g_of(z):
        return (2 * q0 * z - q0 ** 2 + 1) / (q0 ** 2 + 1)

    return {
        "q0": q0, "u": u, "z_cap": z_cap, "z_C": z_C, "z_mass": z_mass,
        "z_decay": z_decay, "z_c2": z_c2_lo, "z_c2_upper": z_c2_hi,
        "c2_at_zC": c2_at(z_C), "c2_at_zD": c2_at(z_cap),
        "K_ratio": g_of(z_decay) / g_of(z_c2_lo),
        "sens_mass": D_TR(q0, z_cap) * z_cap / F_TR(q0, z_cap),
        "q_muon_minus_q_proton": q0 - mp.mpf(str(q_at(50))),
    }


GAPS = {
    "mass - cap": lambda d: d["z_mass"] - d["z_cap"],
    "decay - cap": lambda d: d["z_decay"] - d["z_cap"],
    "ladder anchor - z_C": lambda d: d["z_c2"] - d["z_C"],
    "ladder anchor - cap": lambda d: d["z_c2"] - d["z_cap"],
    "c_2(z_C) + 1": lambda d: d["c2_at_zC"] + 1,
    "c_2(z_D) + 1": lambda d: d["c2_at_zD"] + 1,
    "mu-p tension in q": lambda d: d["q_muon_minus_q_proton"],
}


def main() -> int:
    t0 = time.monotonic()
    print("=" * 78)
    print(" qou-cds1: four determinations of z, priced against the CAL inputs")
    print("=" * 78)

    base = determinations(R_MU, R_P, ME, QB)

    print(f"\n  muon pin q0 = {mp.nstr(base['q0'], 20)}   (pure geometry, no trace)")
    print("\n  CONTROL — the committed determinations, reproduced:")
    for lbl, got, want, tol in (
            ("cap   (y_(1^3)=0, derived)", base["z_cap"], COMMITTED_Z_CAP, "1e-15"),
            ("mass  (measured m_p)", base["z_mass"], COMMITTED_Z_MASS, "1e-15"),
            ("decay (measured Q_beta)", base["z_decay"], COMMITTED_Z_DECAY, "1e-7")):
        print(f"    {lbl:28s} {mp.nstr(got, 18):>21s}  vs committed "
              f"{mp.nstr(want, 18):>21s}   |d| = {mp.nstr(mp.fabs(got - want), 3)}"
              f"  (tol {tol})")
    print(f"    {'d ln tr_M / d ln z':28s} {mp.nstr(base['sens_mass'], 8):>21s}"
          "  vs committed 0.00119")

    print("\n  and the FOURTH, from the ladder's own anchor (implied c_2 = -1):")
    print(f"    z = {mp.nstr(base['z_c2'], 18)}   "
          f"(other cos branch: {mp.nstr(base['z_c2_upper'], 12)})")
    print(f"    z_C (the excised convention) = {mp.nstr(base['z_C'], 18)}")
    print(f"    implied c_2 at z_C = {mp.nstr(base['c2_at_zC'], 10)}     "
          f"at z_D = {mp.nstr(base['c2_at_zD'], 10)}")

    # ---- the budget: both ends of every gap recomputed together ----------
    perts = [
        ("CAL-2  m_mu/m_e", lambda s: (R_MU + s * R_MU_ERR, R_P, ME, QB)),
        ("CAL-2' m_p/m_e", lambda s: (R_MU, R_P + s * R_P_ERR, ME, QB)),
        ("CAL-1  m_e", lambda s: (R_MU, R_P, ME + s * ME_ERR, QB)),
        ("Q_beta", lambda s: (R_MU, R_P, ME, QB + s * QB_ERR)),
    ]
    sigma = {k: mp.mpf(0) for k in GAPS}
    rows = []
    for name, pert in perts:
        hi, lo = determinations(*pert(1)), determinations(*pert(-1))
        row = {}
        for key, fn in GAPS.items():
            d = mp.fabs(fn(hi) - fn(lo)) / 2
            sigma[key] = mp.sqrt(sigma[key] ** 2 + d ** 2)
            row[key] = d
        rows.append((name, row))

    print("\n  1-SIGMA ON EACH GAP — both ends recomputed together, so the q0")
    print("  correlation between the cap and the mass determination survives:")
    hdr = "".join(f"{k.replace(' ', ''):>18s}" for k in GAPS)
    print(f"    {'input':18s}{hdr}")
    for name, row in rows:
        print(f"    {name:18s}" + "".join(f"{mp.nstr(row[k], 4):>18s}" for k in GAPS))
    print(f"    {'quadrature TOTAL':18s}"
          + "".join(f"{mp.nstr(sigma[k], 4):>18s}" for k in GAPS))

    sig = {k: mp.fabs(fn(base)) / sigma[k] for k, fn in GAPS.items()}
    print(f"\n  {'gap':22s}{'value':>24s}{'1 sigma':>14s}{'significance':>18s}")
    for key, fn in GAPS.items():
        print(f"  {key:22s}{mp.nstr(fn(base), 10):>24s}{mp.nstr(sigma[key], 5):>14s}"
              f"{mp.nstr(sig[key], 6) + ' s':>18s}")

    # the three-facts-one-measurement identity
    trio = (sig["mu-p tension in q"], sig["mass - cap"])
    spread = mp.fabs(trio[0] - trio[1]) / trio[0]
    print(f"\n  ONE MEASUREMENT, THREE COORDINATES: the mu-p substrate tension is "
          f"{mp.nstr(trio[0], 6)} sigma;")
    print(f"  the mass-vs-cap gap in z is {mp.nstr(trio[1], 6)} sigma — they agree to "
          f"{mp.nstr(spread * 100, 3)} %,")
    print("  because both are (q_muon - q_proton) over CODATA's bar on m_mu/m_e. The")
    print("  c_3 cross-anchor swing is the same quantity again (9.4936 sigma, measured in")
    print("  qbeta-c3-muon-anchor-codata-edition-attribution). Carried as three facts.")

    print(f"\n  THE TWO DECAY-SIDE FUNCTIONALS DISAGREE: the trace reduction wants")
    print(f"  z = {mp.nstr(base['z_decay'], 12)}, the ladder wants "
          f"{mp.nstr(base['z_c2'], 12)}. Reconciling them needs a scale K off by")
    print(f"  {mp.nstr(base['K_ratio'], 8)}x = {mp.nstr((base['K_ratio'] - 1) * 100, 5)} %, "
          f"against Step 14's {K_WALL_PCT} % wall for parameter-free K")
    print(f"  corrections — {mp.nstr((base['K_ratio'] - 1) * 100 / K_WALL_PCT, 4)}x outside it.")

    a = [
        {"name": "control_reproduces_the_committed_determinations",
         "passed": bool(mp.fabs(base["z_cap"] - COMMITTED_Z_CAP) < mp.mpf("1e-15")
                        and mp.fabs(base["z_mass"] - COMMITTED_Z_MASS) < mp.mpf("1e-15")
                        and mp.fabs(base["z_decay"] - COMMITTED_Z_DECAY) < mp.mpf("1e-7")),
         "detail": "cap and mass to 1e-15 through the imported symbolic trace; decay to "
                   f"{mp.nstr(mp.fabs(base['z_decay'] - COMMITTED_Z_DECAY), 3)} "
                   "(F reconstructed, not re-derived — stated as a tolerance)"},
        {"name": "mass_channel_does_not_confirm_the_cap",
         "passed": bool(sig["mass - cap"] > 5),
         "detail": f"the quoted '0.0203 %' is {mp.nstr(sig['mass - cap'], 6)} sigma. Far "
                   "closer than decay and still a decisive disagreement; 'mass puts z "
                   "essentially where the cap does' does not survive its own bar"},
        {"name": "decay_channel_is_excluded_by_five_orders_of_sigma",
         "passed": bool(sig["decay - cap"] > mp.mpf("1e5")),
         "detail": f"{mp.nstr(sig['decay - cap'], 6)} sigma — the decay anomaly is real "
                   "and is not a leverage artefact"},
        {"name": "mu_p_tension_and_mass_cap_gap_are_one_measurement",
         "passed": bool(spread < mp.mpf("0.01")),
         "detail": f"{mp.nstr(trio[0], 6)} vs {mp.nstr(trio[1], 6)} sigma, agreeing to "
                   f"{mp.nstr(spread * 100, 3)} % — same quantity in two coordinates, "
                   "and the c_3 swing is a third"},
        {"name": "c2_equals_minus_one_is_a_low_sigma_C_frame_statement",
         "passed": bool(sig["c_2(z_C) + 1"] < 2),
         "detail": f"implied c_2 at z_C = {mp.nstr(base['c2_at_zC'], 9)} +- "
                   f"{mp.nstr(sigma['c_2(z_C) + 1'], 4)}, i.e. "
                   f"{mp.nstr(sig['c_2(z_C) + 1'], 4)} sigma from -1: agreement, not a "
                   "1.76 % miss — and empirical, not proved"},
        {"name": "c2_equals_minus_one_is_excluded_under_D",
         "passed": bool(sig["c_2(z_D) + 1"] > 500),
         "detail": f"implied c_2 at z_D = {mp.nstr(base['c2_at_zD'], 9)}, "
                   f"{mp.nstr(sig['c_2(z_D) + 1'], 6)} sigma from -1 — THERE IS NO "
                   "D-FRAME ANCHOR at c_2 = -1"},
        {"name": "ladder_anchor_is_a_measurement_of_z_and_selects_C",
         "passed": bool(sig["ladder anchor - z_C"] < 2
                        and sig["ladder anchor - cap"] > 500),
         "detail": f"z from implied-c_2 = -1 is {mp.nstr(base['z_c2'], 9)} +- "
                   f"{mp.nstr(sigma['ladder anchor - z_C'], 3)}: "
                   f"{mp.nstr(sig['ladder anchor - z_C'], 4)} sigma from z_C, "
                   f"{mp.nstr(sig['ladder anchor - cap'], 6)} sigma from the derived cap"},
        {"name": "two_decay_side_functionals_disagree_beyond_the_K_wall",
         "passed": bool((base["K_ratio"] - 1) * 100 > 10 * K_WALL_PCT),
         "detail": f"trace reduction z = {mp.nstr(base['z_decay'], 9)} vs ladder "
                   f"z = {mp.nstr(base['z_c2'], 9)}; reconciling needs K off by "
                   f"{mp.nstr(base['K_ratio'], 8)}x, "
                   f"{mp.nstr((base['K_ratio'] - 1) * 100 / K_WALL_PCT, 4)}x outside the "
                   f"{K_WALL_PCT} % parameter-free wall"},
    ]
    all_passed = all(x["passed"] for x in a)
    print("\n  assertions:")
    for x in a:
        print(f"    [{'PASS' if x['passed'] else 'FAIL'}] {x['name']}")
        print(f"           {x['detail']}")
    print(f"\n  allPassed: {all_passed}  ({sum(1 for x in a if x['passed'])}/{len(a)})")

    witness = {
        "computation": "qbeta-d-frame-z-determinations-experimental-budget",
        "engine": "sympy+mpmath",
        "description": (
            "qou-cds1: the four determinations of the Markov parameter z, each priced "
            "against the CAL-1/2/3 CODATA-2022 published uncertainties by recomputing "
            "both ends of every gap together (so the q0 correlation survives). The mass "
            "channel does NOT confirm the derived cap -- the quoted 0.0203 % is 9.49 "
            "sigma -- and that 9.49 is the mu-p substrate tension and the c_3 "
            "cross-anchor swing in different coordinates: three corpus facts, one "
            "measurement. c_2 = -1 is a 1.6-sigma empirical statement at z_C (not a "
            "theorem, and not a 1.76 % miss) and is excluded at 773 sigma under D. "
            "Solving implied-c_2 = -1 for z gives a FOURTH determination, "
            "0.499110 +- 0.000132, which is 1.60 sigma from z_C and 863 sigma from the "
            "cap: the ladder's anchor independently measures z and selects C. Hence "
            "there is no D-frame anchor and the ladder's FORM must change, not its "
            "parameter. Scope-(a); nothing derived, wired or readmitted."),
        "contentBlock": "def:three-calibration-discipline",
        "assertions": a,
        "allPassed": all_passed,
        "parameters": {
            "pin": "muon (convention-free: m_mu/m_e = Vol(4_1)/hbar_q^2)",
            "dps": 60,
            "F_required_trM": mp.nstr(F_REQUIRED_TRM, 18),
            "K_wall_pct": mp.nstr(K_WALL_PCT, 4),
            "cal_inputs": {
                "m_mu_over_m_e": f"{_MU.value_str}({_MU.uncertainty_str})",
                "m_p_over_m_e": f"{_PE.value_str}({_PE.uncertainty_str})",
                "m_e_MeV": mp.nstr(ME, 12), "m_e_MeV_err": mp.nstr(ME_ERR, 4),
                "Q_beta_MeV": mp.nstr(QB, 12), "Q_beta_MeV_err": mp.nstr(QB_ERR, 4),
            },
        },
        "data": {
            "determinations": {
                "z_cap_derived": mp.nstr(base["z_cap"], 20),
                "z_mass_measured_m_p": mp.nstr(base["z_mass"], 20),
                "z_decay_measured_Q_beta": mp.nstr(base["z_decay"], 20),
                "z_ladder_anchor_c2_eq_minus1": mp.nstr(base["z_c2"], 20),
                "z_ladder_anchor_other_branch": mp.nstr(base["z_c2_upper"], 20),
                "z_C_excised_convention": mp.nstr(base["z_C"], 20),
            },
            "implied_c2": {"at_z_C": mp.nstr(base["c2_at_zC"], 12),
                           "at_z_D": mp.nstr(base["c2_at_zD"], 12)},
            "budget_1sigma": {
                name: {k: mp.nstr(row[k], 8) for k in GAPS} for name, row in rows},
            "budget_total": {k: mp.nstr(sigma[k], 8) for k in GAPS},
            "gap_values": {k: mp.nstr(fn(base), 12) for k, fn in GAPS.items()},
            "significance_sigma": {k: mp.nstr(sig[k], 8) for k in GAPS},
            "one_measurement_three_coordinates": {
                "mu_p_tension_sigma": mp.nstr(trio[0], 8),
                "mass_vs_cap_sigma": mp.nstr(trio[1], 8),
                "relative_spread": mp.nstr(spread, 6),
                "c3_swing_sigma_measured_elsewhere": "9.49363",
            },
            "K_ratio_between_decay_functionals": mp.nstr(base["K_ratio"], 12),
            "sens_mass_dlog_trM_dlog_z": mp.nstr(base["sens_mass"], 10),
        },
        "context": {
            "axis": "qou-cds1 anchor side: does a D-frame ladder anchor exist?",
            "answer": (
                "NO. c_2 = -1 is supported at 1.6 sigma under C and excluded at 773 "
                "sigma under D, and the ladder anchor read as a measurement of z lands "
                "1.60 sigma from z_C and 863 sigma from the derived cap. The C->D move "
                "cannot be completed by finding a D-frame c_2; the ladder's functional "
                "FORM has to change. This is the anchor-side statement of what "
                "decayLadder_zC_threeRow_ne_zero says structurally."),
            "corrects": (
                "the standing reading that mass 'essentially confirms' the cap and so "
                "localises the anomaly to decay: mass-vs-cap is 9.49 sigma. Both "
                "channels disagree with the derived cap; decay disagrees 5.8e4 times "
                "harder."),
            "scope": (
                "Scope-(a). Nothing derived, proposed, wired or readmitted; no "
                "convention adjudicated; no c_k value changed. A z landing near an "
                "inadmissible point is TENSION, not permission -- one_not_root stands, "
                "as does the derived two-row cap."),
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec (NO-FLOAT64 discipline; ephemeral meta).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }

    out = HERE / "qbeta-d-frame-z-determinations-experimental-budget.witness.json"
    with open(out, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="sympy+mpmath",
            q0_anchor="muon",
            q0_value=mp.nstr(base["q0"], 30))
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
