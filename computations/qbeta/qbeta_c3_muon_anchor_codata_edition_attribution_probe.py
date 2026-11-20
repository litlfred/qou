#!/usr/bin/env python3
"""qou-cds1 FINDING B is qou-t39x, and the CAL error bar swallows it whole.

WHAT WAS ALREADY KNOWN, AND BY WHOM. Bean `qou-t39x` (2026-08-29, PR #5952)
established the attribution this probe re-derives independently: there is no
single "muon c_3", there are three, each correct at its own pin --

    proton                          -2.06934257712   corpus proton, exactly
    muon FROZEN pin  (...5557...)   -2.02018812814
    muon CODATA-2018 (...5554...)   -2.02020023502   the committed corpus value
    muon CODATA-2022 (...5642...)   -2.01986031187   what the extractor computes today

`qou-cds1`'s Finding B reports the last two as a 3.4e-4 disagreement and calls
-2.01986031187 "a third value" of unknown origin. It is not: it is the SAME
formula evaluated at the CODATA-2022 anchor that `fca08de7d2` (2026-08-22) moved
the muon pin to, three weeks before Finding B was written. So Finding B and
qou-t39x are one defect, and this probe closes the first against the second.

TWO CORRECTIONS TO WHAT FINDING B RECORDS, both checked here:

  * "the committed witness on disk already records allPassed: False" -- it does
    not. `qbeta-c3-ladder-trace-convention-sensitivity.witness.json` records
    `allPassed: true` with `c_3(muon) = -2.020200235021255`, i.e. it was
    generated (computedAt 2026-08-15) BEFORE the anchor moved. The 8/9 is live
    only; the witness is stale-but-internally-consistent, which is worse to read
    and better to fix.
  * "neither the live -2.02020024 nor the superseded -2.0097; a third value" --
    it is the live one. -2.02020024 is the superseded one.

WHAT IS NEW HERE: THE EXPERIMENTAL IDEAL. qou-t39x prices the three values
against each other. Nothing prices them against the calibration inputs they are
built from. Doing that -- CAL-1 m_e, CAL-2 m_mu/m_e, and the Q_beta the extractor
inverts against, each recomputed at +-1 sigma of its CODATA-2022 published
uncertainty rather than through a recorded derivative -- changes what the whole
disagreement means:

  1. THE AMPLIFICATION IS 1/u^3 = 1.6e6, AND IT RE-GRADES A STANDING VERDICT.
     `qou_substrate/constants.py` prices the frozen-vs-derived q drift at
     0.0769 ppb and rules it "A precision defect, not a physics one", on the
     correct ground that it sits far below the 11.5 ppb mu-p substrate tension.
     The c_3 extractor divides by u^3 = 6.2e-7, so relative moves in q reach c_3
     multiplied by ~2.1e6: the CODATA edition step of 1.451 ppb on the mass ratio
     is 1.7e-4 relative on c_3. Below the substrate tension does NOT imply below
     the resolution of what divides by u^3, and this channel is the counterexample.

  2. c_3(muon) = -2.0199 +- 1.26, AND THE DISAGREEMENT IS 0.00027 SIGMA.
     The budget is dominated by Q_beta alone: 0.78 ppm on a 0.782 MeV Q-value,
     times 1/u^3, is +-1.26 by itself. The registry quotes NINE significant
     figures for a quantity whose own calibration inputs support 0.2 of one. The
     3.4e-4 that Finding B calls "340x the tolerance" is 3700x INSIDE the error
     bar; the 1e-6 tolerance is a reproducibility tolerance being read as a
     physics one.

  3. THE CROSS-ANCHOR SWING SURVIVES, AND IT IS THE ONLY THING THAT DOES.
     Q_beta and m_e are COMMON MODE -- they enter both anchors identically, so
     they cancel in c_3(p) - c_3(mu) to 7.6e-7 and 3.1e-10. The swing is
     -0.0494823 +- 0.0052, i.e. 9.5 sigma, and it is 9.5 sigma for the same
     reason the mu-p tension is: it is the same physical statement. So the
     "REFUTED as real-q fibre element" verdict, which rests on the swing
     (sensitivity-probe assertion `anchor_swing_mechanism_convention_immune`),
     is experimentally supported, while every absolute c_3 digit past the first
     is not. That asymmetry is the usable result.

  4. AND THE PROTON ARM EXPLAINS WHY ONLY ONE ANCHOR BROKE. m_p/m_e moved by
     2e-12 relative between editions against the muon ratio's 1.5e-9, so the
     proton arm still reproduces its corpus value to 2.9e-9 and gave no warning.

WHAT THIS PROBE DOES NOT DO. It does not re-pin `Q_MUON_50_DIGIT_STR` and does
not migrate the files carrying the 17-digit ancestor q; that is owner-authorised
re-pin work sequenced behind PR #5500 and the qou-1c4y migration. It measures.

SCOPE. Convention C throughout -- the frame the committed corpus values were
extracted in, so a regression attribution has to stay in it. No convention is
adjudicated, no c_k value is changed here, no constant is re-pinned.
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

from qbeta_utils import c3_target_at  # noqa: E402
from qbeta_utils import substrate_ladder_quantities  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    MASS_RATIO_MU_E_STR, MASS_RATIO_P_E_STR, Q_MUON_50_DIGIT_STR,
    q_at, q_muon_at, vol_4_1_at,
)
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60

# ── CAL inputs, read (never transcribed) at full published precision ──
# CAL-1  m_e      : codata_2022_source, 0.51099895069(16) MeV
# CAL-2  m_mu/m_e : NIST table row, 206.7682827(46)  -> q via the muon closed form
# Q_beta          : the experimental neutron beta-decay Q-value the extractor
#                   inverts against (CAL-2 proxy per codata_constants.py).
ME = mp.mpf(str(C.M_E_MEV))
ME_ERR = mp.mpf(str(C.M_E_MEV_ERR))
QB = mp.mpf(str(C.Q_BETA_MEV))
QB_ERR = mp.mpf(str(C.Q_BETA_MEV_ERR))

_MU_E = codata("muon-electron mass ratio")
_P_E = codata("proton-electron mass ratio")
R_MU_2022 = mp.mpf(_MU_E.value_str)
R_MU_2022_ERR = mp.mpf(_MU_E.uncertainty_str.replace(" ", ""))
R_P_2022 = mp.mpf(_P_E.value_str)
R_P_2022_ERR = mp.mpf(_P_E.uncertainty_str.replace(" ", ""))

# DELIBERATE HISTORICAL LITERAL -- the CODATA-2018 muon-electron mass ratio.
# This is the number this repo carried under a "CODATA 2022" comment until
# 2026-08-15; see the "Input measurements" note in qou_substrate/constants.py.
# It is here to REPRODUCE a superseded extraction, which is the whole point of
# the probe, and must not be "corrected" to the 2022 value.
R_MU_2018 = mp.mpf("206.7682830")

VOL41 = vol_4_1_at(60)

# Committed corpus values (registry section 9f window endpoints;
# qbeta-c3-barodd-sleak.witness.json) -- the regression target.
CORPUS_C3_PROTON = mp.mpf("-2.06934258")
CORPUS_C3_MUON = mp.mpf("-2.02020024")


def _head_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
    except Exception:
        return "unknown"


def q_muon_from_ratio(r: mp.mpf) -> mp.mpf:
    """The muon closed form q = 1/(1 - sqrt(Vol(4_1)/r)).

    Mirrors qou_substrate.constants.q_muon_at with the ratio as a parameter, so
    a superseded CODATA edition can be evaluated without editing the constant.
    """
    return 1 / (1 - mp.sqrt(VOL41 / r))


def q_proton_from_ratio(r: mp.mpf) -> mp.mpf:
    """The proton substrate identity solved for q, ratio as a parameter.

    Transcribed from qou_substrate.constants.q_at._resid; assertion
    `proton_solver_reproduces_q_at` gates the transcription.
    """
    def _resid(q):
        h = q - 1 / q
        hbar_sq = (1 - 1 / q) ** 2
        tr_m = mp.fabs((4 + h**2 - 3 * h**4 - h**6) / (h**2 + 4))
        qf3 = (q**2 + 1 + q**(-2)) * (q + q**(-1))
        return 2 * VOL41 / hbar_sq * (tr_m * qf3 / q**3) - 12 - r
    return mp.findroot(_resid, mp.mpf("1.10997858"))


def u_of(q: mp.mpf) -> mp.mpf:
    """The ladder expansion variable u = b*hbar_q^2 -- the 1/u^3 lever."""
    h = q - 1 / q
    hbar = (q - 1) / q
    return mp.sqrt((h**2 + 3) / (h**2 + 4)) * hbar**2


def c3(q: mp.mpf, me: mp.mpf = None, qb: mp.mpf = None) -> mp.mpf:
    """C-frame c_3 target, through the public extractor (no re-spelling)."""
    return c3_target_at(q, QB if qb is None else qb,
                        ME if me is None else me, convention="C")


def sig_round(x: mp.mpf, sig: int) -> mp.mpf:
    """Round to `sig` significant figures, at working precision."""
    if x == 0:
        return mp.mpf(0)
    e = mp.floor(mp.log10(mp.fabs(x))) - (sig - 1)
    return mp.nint(x / mp.mpf(10) ** e) * mp.mpf(10) ** e


def main() -> int:
    t0 = time.monotonic()

    print("=" * 78)
    print(" qou-cds1 FINDING B: attribution of the 3.4e-4 muon c_3 disagreement")
    print("=" * 78)

    # ---- 0. inputs are at full published precision, mpf all the way ------
    print("\n  CAL inputs, read from the tables (no transcription, no float):")
    print(f"    CAL-1  m_e       = {_fmt(ME)} +- {_fmt(ME_ERR)} MeV"
          f"   rel {mp.nstr(ME_ERR / ME, 4)}")
    print(f"    CAL-2  m_mu/m_e  = {_MU_E.value_str}({_MU_E.uncertainty_str})"
          f"        rel {mp.nstr(R_MU_2022_ERR / R_MU_2022, 4)}   [CODATA 2022]")
    print(f"    CAL-2' m_p/m_e   = {_P_E.value_str}({_P_E.uncertainty_str})"
          f"     rel {mp.nstr(R_P_2022_ERR / R_P_2022, 4)}   [CODATA 2022]")
    print(f"    Q_beta           = {_fmt(QB)} +- {_fmt(QB_ERR)} MeV"
          f"   rel {mp.nstr(QB_ERR / QB, 4)}")

    # ---- 1. the two editions -------------------------------------------
    q_mu_22 = q_muon_from_ratio(R_MU_2022)
    q_mu_18 = q_muon_from_ratio(R_MU_2018)
    q_mu_frozen = mp.mpf(Q_MUON_50_DIGIT_STR)
    q_p_22 = q_proton_from_ratio(R_P_2022)

    c3_22 = c3(q_mu_22)
    c3_18 = c3(q_mu_18)
    c3_frozen = c3(q_mu_frozen)
    c3_p_22 = c3(q_p_22)

    gap = CORPUS_C3_MUON - c3_22          # the Finding-B disagreement
    edition = c3_18 - c3_22               # pure CODATA edition shift
    residual = CORPUS_C3_MUON - c3_18     # what is left after the edition
    explained = edition / gap

    print("\n  muon anchor, SAME extractor, two CODATA editions:")
    print(f"    q  (2022, 206.7682827) = {mp.nstr(q_mu_22, 28)}")
    print(f"    q  (2018, 206.7682830) = {mp.nstr(q_mu_18, 28)}")  # noqa: P31 — the 2018 edition, compared on purpose
    print(f"    q  (frozen pin)        = {mp.nstr(q_mu_frozen, 28)}")
    print(f"    c_3 @ 2022  = {mp.nstr(c3_22, 15)}   <- what the probe computes")
    print(f"    c_3 @ 2018  = {mp.nstr(c3_18, 15)}   <- what the corpus records")
    print(f"    c_3 @ frozen= {mp.nstr(c3_frozen, 15)}")
    print(f"    corpus      = {mp.nstr(CORPUS_C3_MUON, 15)}")
    print(f"\n    disagreement  corpus - c_3(2022) = {mp.nstr(gap, 8)}")
    print(f"    edition shift c_3(2018)- c_3(2022) = {mp.nstr(edition, 8)}")
    print(f"    residual      corpus - c_3(2018)   = {mp.nstr(residual, 8)}")
    print(f"    explained fraction                 = {mp.nstr(explained, 10)}")
    print(f"    c_3(2018) rounded to 9 sig figs    = {mp.nstr(sig_round(c3_18, 9), 12)}"
          f"   corpus {mp.nstr(CORPUS_C3_MUON, 12)}")
    print(f"    frozen-pin miss |corpus - c_3(frozen)| = {mp.nstr(mp.fabs(CORPUS_C3_MUON - c3_frozen), 6)}"
          f"   ({mp.nstr(mp.fabs(CORPUS_C3_MUON - c3_frozen) / mp.fabs(residual), 6)}x the ancestor residual)")

    # ---- 2. the amplification lever ------------------------------------
    u_mu = u_of(q_mu_22)
    lever = 1 / u_mu**3
    rel_q = mp.fabs(q_mu_18 - q_mu_22) / q_mu_22
    rel_c3 = mp.fabs(edition) / mp.fabs(c3_22)
    amp = rel_c3 / rel_q
    print("\n  amplification (why a sub-ppb anchor drift is visible at 1e-4):")
    print(f"    u  = {mp.nstr(u_mu, 12)}      1/u^3 = {mp.nstr(lever, 12)}")
    print(f"    relative move in q   = {mp.nstr(rel_q, 6)}  ({mp.nstr(rel_q * 10**9, 5)} ppb)")
    print(f"    relative move in c_3 = {mp.nstr(rel_c3, 6)}")
    print(f"    amplification factor = {mp.nstr(amp, 6)}")
    print("    for scale: the mu-p substrate tension is 11.5 ppb, so this drift is")
    print("    far BELOW it -- and still 1.7e-4 relative once divided by u^3.")

    # ---- 3. CAL experimental budget, by direct recomputation ------------
    # Each input is shifted ONCE and BOTH anchors are recomputed, so Q_beta and
    # m_e enter the swing as the common-mode terms they physically are.
    def state(q_mu, q_p, me, qb):
        a, b = c3(q_p, me, qb), c3(q_mu, me, qb)
        return a, b, a - b

    base = state(q_mu_22, q_p_22, ME, QB)

    def half_range(pert):
        hi, lo = state(*pert(1)), state(*pert(-1))
        return [mp.fabs(hi[i] - lo[i]) / 2 for i in range(3)]

    rows = [
        ("CAL-2  m_mu/m_e", half_range(lambda s: (
            q_muon_from_ratio(R_MU_2022 + s * R_MU_2022_ERR), q_p_22, ME, QB))),
        ("CAL-2' m_p/m_e", half_range(lambda s: (
            q_mu_22, q_proton_from_ratio(R_P_2022 + s * R_P_2022_ERR), ME, QB))),
        ("CAL-1  m_e", half_range(lambda s: (q_mu_22, q_p_22, ME + s * ME_ERR, QB))),
        ("Q_beta", half_range(lambda s: (q_mu_22, q_p_22, ME, QB + s * QB_ERR))),
    ]
    total = [mp.sqrt(sum(d[i]**2 for _, d in rows)) for i in range(3)]

    print("\n  EXPERIMENTAL 1-sigma budget (each CAL input recomputed at +-1sigma;")
    print("  Q_beta and m_e are COMMON MODE, so they cancel in the swing):")
    print(f"    {'input':18s} {'d c_3(proton)':>15s} {'d c_3(muon)':>15s} {'d swing':>15s}")
    for label, d in rows:
        print(f"    {label:18s} {mp.nstr(d[0], 5):>15s} {mp.nstr(d[1], 5):>15s} "
              f"{mp.nstr(d[2], 5):>15s}")
    print(f"    {'quadrature TOTAL':18s} {mp.nstr(total[0], 5):>15s} "
          f"{mp.nstr(total[1], 5):>15s} {mp.nstr(total[2], 5):>15s}")

    digits = [mp.log10(mp.fabs(base[i]) / total[i]) for i in range(3)]
    print(f"\n    c_3(proton) = {mp.nstr(base[0], 12)} +- {mp.nstr(total[0], 4)}"
          f"   ({mp.nstr(digits[0], 3)} supported sig figs; registry quotes 9)")
    print(f"    c_3(muon)   = {mp.nstr(base[1], 12)} +- {mp.nstr(total[1], 4)}"
          f"   ({mp.nstr(digits[1], 3)} supported sig figs; registry quotes 9)")
    print(f"    swing       = {mp.nstr(base[2], 12)} +- {mp.nstr(total[2], 4)}"
          f"   ({mp.nstr(digits[2], 3)} supported sig figs)")
    swing_sigma = mp.fabs(base[2]) / total[2]
    print(f"    swing significance = {mp.nstr(swing_sigma, 6)} sigma")
    print(f"    disagreement / sigma(c_3 muon) = {mp.nstr(mp.fabs(gap) / total[1], 6)}")

    # ---- 4. downstream re-grade: what the repentance actually moves -----
    # Every quantity below is DEFINED from c_3(muon), so each inherits the
    # edition step. Recorded as a ledger because the direction of every corpus
    # finding is unchanged while three published MARGINS are not.
    PHIB_DEFICIT = mp.mpf("0.0094")        # Phi_b state-integral volume deficit, PR #3654
    S_MUON_QUOTED = mp.mpf("886.8")        # 2026-07-07 audit, 4 significant figures
    kappa21 = lambda q: (q - 1)**3 * (q + 1) / q**2   # noqa: E731 — the KC21 carrier

    def regrade(q_mu, c3_mu):
        leak = c3_mu + VOL41
        return {
            "S_leak_muon": leak,
            "kc21_agreement_pct": mp.fabs(leak - PHIB_DEFICIT) / PHIB_DEFICIT * 100,
            "S_kappa_muon": -c3_mu / kappa21(q_mu),
            "swing_pct": mp.fabs(c3_p_22 - c3_mu) / mp.fabs(c3_mu) * 100,
        }

    old = regrade(q_mu_18, c3_18)
    new = regrade(q_mu_22, c3_22)
    s_win = mp.mpf("0.05") / S_MUON_QUOTED          # 4-s.f. rounding window
    s_out = (mp.fabs(new["S_kappa_muon"] - S_MUON_QUOTED) / S_MUON_QUOTED) / s_win

    print("\n  DOWNSTREAM RE-GRADE (CODATA-2018 -> CODATA-2022 muon pin):")
    print(f"    {'quantity':34s} {'2018 (quoted)':>16s} {'2022 (live)':>16s}")
    for key, label in (("S_leak_muon", "S_leak(muon) = c_3 + Vol(4_1)"),
                       ("kc21_agreement_pct", "KC21 |S| vs Phi_b deficit  [%]"),
                       ("S_kappa_muon", "S := -c_3/kappa_(2,1)  (muon)"),
                       ("swing_pct", "cross-anchor swing of c_3  [%]")):
        print(f"    {label:34s} {mp.nstr(old[key], 8):>16s} {mp.nstr(new[key], 8):>16s}")
    print(f"    the audit-quoted S(muon) = {S_MUON_QUOTED} is now {mp.nstr(s_out, 3)}x OUTSIDE")
    print(f"    its own 4-s.f. window; at the live anchor it reads "
          f"{mp.nstr(new['S_kappa_muon'], 4)}.")
    print(f"    KC21's scale match is {mp.nstr(new['kc21_agreement_pct'] / old['kc21_agreement_pct'], 3)}x "
          "WORSE at the live pin. The Phi_b")
    print("    deficit 0.0094 is anchor-blind to sub-ppm, so all of the movement")
    print("    is on the |S| side -- the margin was never a property of the saddle.")

    # ---- assertions -----------------------------------------------------
    a = [
        {"name": "inputs_are_full_published_precision_no_float_truncation",
         "passed": bool(MASS_RATIO_MU_E_STR == _MU_E.value_str
                        and MASS_RATIO_P_E_STR == _P_E.value_str
                        and mp.fabs(mp.mpf(str(q_muon_at(50))) - q_mu_22) < mp.mpf("1e-45")),
         "detail": "constants.py reads the NIST table verbatim; q_muon_at reproduces "
                   "the closed form from it to 1e-45 -- the gap is not a precision artefact"},
        {"name": "proton_solver_reproduces_q_at",
         "passed": bool(mp.fabs(q_p_22 - mp.mpf(str(q_at(50)))) < mp.mpf("1e-40")),
         "detail": "local transcription of the proton substrate identity == constants.q_at"},
        {"name": "proton_arm_reproduces_corpus_under_codata_2022",
         "passed": bool(mp.fabs(c3_p_22 - CORPUS_C3_PROTON) < mp.mpf("1e-6")),
         "detail": f"|c_3(p) - corpus| = {mp.nstr(mp.fabs(c3_p_22 - CORPUS_C3_PROTON), 6)} "
                   "-- m_p/m_e barely moved between editions, so only the muon arm broke"},
        {"name": "disagreement_is_the_codata_2018_to_2022_edition_shift",
         "passed": bool(mp.fabs(explained - 1) < mp.mpf("1e-4")),
         "detail": f"edition shift / disagreement = {mp.nstr(explained, 10)} "
                   "-- 99.9985 % of the 3.4e-4 gap is 206.7682830 -> 206.7682827"},
        {"name": "residual_after_edition_is_the_corpus_literals_own_rounding",
         # mp.mpf(10)**e is not binary-exact, so sig_round's output is compared
         # with a tolerance far below the 9th figure rather than with `==`.
         "passed": bool(mp.fabs(residual) < mp.mpf("1e-8")
                        and mp.fabs(sig_round(c3_18, 9) - CORPUS_C3_MUON)
                        < mp.mpf("1e-20")),
         "detail": f"residual {mp.nstr(residual, 6)}; c_3(2018) rounds to the corpus "
                   "literal at the 9 sig figs it quotes -- nothing is left unexplained"},
        {"name": "attribution_is_the_17_digit_ancestor_not_the_frozen_pin",
         "passed": bool(mp.fabs(CORPUS_C3_MUON - c3_frozen)
                        > 1000 * mp.fabs(residual)),
         "detail": f"frozen pin misses by {mp.nstr(mp.fabs(CORPUS_C3_MUON - c3_frozen), 6)}; "
                   "the corpus c_3 is the CODATA-2018 ancestor q, not Q_MUON_50_DIGIT_STR"},
        {"name": "one_over_u_cubed_amplifies_the_anchor_drift_by_2e6",
         "passed": bool(lever > mp.mpf("1.6e6") and amp > mp.mpf("1e6")),
         "detail": f"1/u^3 = {mp.nstr(lever, 8)}, amplification {mp.nstr(amp, 6)} -- "
                   "'below the 11.5 ppb mu-p tension' does not imply below the "
                   "resolution of what divides by u^3"},
        {"name": "cal_experimental_budget_swamps_the_disagreement",
         "passed": bool(total[1] > 1 and mp.fabs(gap) / total[1] < mp.mpf("1e-3")
                        and digits[1] < 1),
         "detail": f"c_3(muon) = {mp.nstr(base[1], 8)} +- {mp.nstr(total[1], 4)} "
                   f"(Q_beta-dominated); disagreement is "
                   f"{mp.nstr(mp.fabs(gap) / total[1], 4)} sigma; "
                   f"{mp.nstr(digits[1], 3)} sig figs supported vs 9 quoted"},
        {"name": "cross_anchor_swing_survives_common_mode_cancellation",
         "passed": bool(swing_sigma > 5 and total[2] < total[1] / 100),
         "detail": f"swing = {mp.nstr(base[2], 8)} +- {mp.nstr(total[2], 4)} "
                   f"= {mp.nstr(swing_sigma, 4)} sigma; Q_beta cancels to "
                   f"{mp.nstr(rows[3][1][2], 4)} -- the refutation's mechanism is "
                   "experimentally supported, the absolute c_3 digits are not"},
        {"name": "kc21_scale_agreement_degrades_at_the_live_anchor",
         "passed": bool(new["kc21_agreement_pct"] > 2 * old["kc21_agreement_pct"]),
         "detail": f"Phi_b deficit vs |S_leak(muon)|: {mp.nstr(old['kc21_agreement_pct'], 3)} % "
                   f"at CODATA-2018 -> {mp.nstr(new['kc21_agreement_pct'], 3)} % at CODATA-2022. "
                   "The deficit is anchor-blind, so KC21's quoted ~2.9 % is a "
                   "superseded number rather than a property of the saddle"},
        {"name": "audit_quoted_S_muon_is_outside_its_own_rounding_window_now",
         "passed": bool(s_out > 1),
         "detail": f"quoted 886.8 is {mp.nstr(s_out, 3)}x outside its 4-s.f. window at the "
                   f"live pin; it reads {mp.nstr(new['S_kappa_muon'], 4)} there -- a second "
                   "CODATA-2018-era literal surfaced by the same edition step"},
    ]
    all_passed = all(x["passed"] for x in a)

    print("\n  assertions:")
    for x in a:
        print(f"    [{'PASS' if x['passed'] else 'FAIL'}] {x['name']}")
        if x.get("detail"):
            print(f"           {x['detail']}")
    print(f"\n  allPassed: {all_passed}  ({sum(1 for x in a if x['passed'])}/{len(a)})")

    witness = {
        "name": "qbeta-c3-muon-anchor-codata-edition-attribution",
        "engine": "mpmath",
        "description": (
            "qou-cds1 Finding B: the 3.4e-4 muon c_3 disagreement is the "
            "CODATA-2018 -> 2022 m_mu/m_e edition change (206.7682830 -> "
            "206.7682827) amplified by the extractor's 1/u^3 = 1.6e6 lever, not "
            "a third value or a computation error. Residual after the edition is "
            "5.0e-9, the corpus literal's own 9-sig-fig rounding. Prices the "
            "whole c_3 target against the CAL-1/2/3 published uncertainties."),
        "contentBlock": "def:three-calibration-discipline",
        "assertions": a,
        "allPassed": all_passed,
        "parameters": {
            "markov_convention": "C",
            "ladder_frame": "u",
            "dps": 60,
            "codata_edition_2022": {
                "m_mu_over_m_e": _MU_E.value_str,
                "m_mu_over_m_e_err": _MU_E.uncertainty_str,
                "m_p_over_m_e": _P_E.value_str,
                "m_p_over_m_e_err": _P_E.uncertainty_str,
            },
            "codata_edition_2018_historical": {"m_mu_over_m_e": "206.7682830"},
            "cal_inputs": {
                "CAL-1_m_e_MeV": _fmt(ME), "CAL-1_m_e_MeV_err": _fmt(ME_ERR),
                "Q_beta_MeV": _fmt(QB), "Q_beta_MeV_err": _fmt(QB_ERR),
            },
        },
        "data": {
            "q_muon": {"codata_2022": mp.nstr(q_mu_22, 30),
                       "codata_2018": mp.nstr(q_mu_18, 30),
                       "frozen_pin": mp.nstr(q_mu_frozen, 30)},
            "q_proton_codata_2022": mp.nstr(q_p_22, 30),
            "c3_muon": {"codata_2022": mp.nstr(c3_22, 15),
                        "codata_2018": mp.nstr(c3_18, 15),
                        "frozen_pin": mp.nstr(c3_frozen, 15),
                        "corpus_literal": mp.nstr(CORPUS_C3_MUON, 15)},
            "c3_proton_codata_2022": mp.nstr(c3_p_22, 15),
            "attribution": {
                "disagreement": mp.nstr(gap, 10),
                "edition_shift": mp.nstr(edition, 10),
                "residual": mp.nstr(residual, 10),
                "explained_fraction": mp.nstr(explained, 12),
                "frozen_pin_miss": mp.nstr(mp.fabs(CORPUS_C3_MUON - c3_frozen), 10),
            },
            "amplification": {
                "u": mp.nstr(u_mu, 15), "one_over_u_cubed": mp.nstr(lever, 12),
                "rel_move_q": mp.nstr(rel_q, 8), "rel_move_c3": mp.nstr(rel_c3, 8),
                "factor": mp.nstr(amp, 8),
            },
            "experimental_budget_1sigma": {
                label: {"c3_proton": mp.nstr(d[0], 8), "c3_muon": mp.nstr(d[1], 8),
                        "swing": mp.nstr(d[2], 8)} for label, d in rows},
            "experimental_budget_total": {
                "c3_proton": mp.nstr(total[0], 8), "c3_muon": mp.nstr(total[1], 8),
                "swing": mp.nstr(total[2], 8)},
            "supported_significant_figures": {
                "c3_proton": mp.nstr(digits[0], 4), "c3_muon": mp.nstr(digits[1], 4),
                "swing": mp.nstr(digits[2], 4), "registry_quotes": 9},
            "downstream_regrade": {
                "codata_2018": {k: mp.nstr(v, 10) for k, v in old.items()},
                "codata_2022": {k: mp.nstr(v, 10) for k, v in new.items()},
                "phib_deficit": mp.nstr(PHIB_DEFICIT, 6),
                "audit_quoted_S_muon": mp.nstr(S_MUON_QUOTED, 6),
                "audit_quoted_S_muon_windows_outside": mp.nstr(s_out, 6),
            },
            "swing_sigma": mp.nstr(swing_sigma, 8),
            "disagreement_in_sigma": mp.nstr(mp.fabs(gap) / total[1], 8),
            "vol_4_1": mp.nstr(VOL41, 20),
        },
        "context": {
            "axis": "qou-cds1 Finding B attribution + CAL experimental budget on c_3",
            "closes": (
                "Finding B is CLOSED as a defect: -2.01986031187 is not a third "
                "value, it is the CODATA-2022 evaluation of the same formula whose "
                "CODATA-2018 evaluation is the committed -2.02020024. The "
                "sensitivity probe's 8/9 is a stale regression target, not a bug."),
            "opens": (
                "(i) the registry's 9-figure c_3 literals exceed what the CAL inputs "
                "support by ~8 figures; (ii) the corpus muon c_3 is on a superseded "
                "CODATA edition, as are the 336 files carrying the 17-digit ancestor q "
                "in this channel. Both are re-pin work sequenced behind PR #5500 and "
                "qou-1c4y; NOT done here."),
            "scope": (
                "Scope-(a), convention C only -- the frame the corpus values were "
                "extracted in. No convention adjudicated, no c_k value changed, "
                "no constant re-pinned."),
        },
        "gitCommit": _head_sha(),
        # int ms, not float sec: a float64 duration is the one raw-float64
        # ratchet this witness would otherwise hit (NO-FLOAT64 discipline).
        "durationMs": int((time.monotonic() - t0) * 1000),
    }

    out = HERE / "qbeta-c3-muon-anchor-codata-edition-attribution.witness.json"
    with open(out, "w") as f:
        from qou_substrate.witness import WitnessBuilder as _WB
        witness.setdefault("scriptFile", os.path.basename(__file__))
        # The anchor is DECLARED, not resolved: this witness is about the
        # difference between anchors, so letting the resolver pick one would
        # record exactly the ambiguity the probe exists to remove.
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="ambiguous", q0_anchor_reason="reads BOTH pins on purpose: proton q_at() + muon q_muon_at() @ CODATA 2022",
            q0_value=mp.nstr(q_mu_22, 30))
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")
    return 0 if all_passed else 1


def _fmt(x: mp.mpf) -> str:
    """Shortest decimal that round-trips the constant at its own precision."""
    return mp.nstr(x, 15, strip_zeros=True)


if __name__ == "__main__":
    sys.exit(main())
