#!/usr/bin/env python3
"""qbeta_precision_ladder_n5.py — the FIRST producer that actually reaches
N=5 on the Q_beta categorical precision ladder, and the settlement of the
published headline's SIGN.

Bean `qou-54g5`, blockers (A) sign convention and (B) no producer reaches N=5.

# Ref: folio/quantum-observable-universe/mass-theory/q-beta-categorical-precision-ladder.md
# Ref: folio/quantum-observable-universe/stochastic-mechanics/q-beta-categorical-precision-ladder-table2-data.md
# Ref: folio/quantum-observable-universe/stochastic-mechanics/q-beta-categorical-precision-ladder-table3-data.md

EVERYTHING HERE IS CONVENTION C (z = sqrt(q)/(q+1)), the frame the block was
written in.  The D-frame ladder does not exist (bean `qou-cds1`); nothing here
is migrated to D and no number here should be quoted as a D-frame result.

--------------------------------------------------------------------------
(B) WHAT PRODUCER REACHED N=5 BEFORE THIS ONE -- the answer is "none that
    computes the block's own ladder".

  * `probe_q_beta_operator_valued_N3.py`, the block's DECLARED producer,
    stops at N=3 and carries no c_5.  It is also not the generator of table 2
    at ALL: its witness records eps_N1 = 674.83 ppm and eps_N2 = 602.24 ppm
    against table 2's +73.79 ppm and +1.24 ppm, because its N=1 rung is
    cos(alpha_N1) with alpha_N1 = -0.0447444 rather than the box's
    cos(alpha - b*hbar^2/2) with alpha = (z-1)h/2 = -0.0404858.  Different
    ladder.  Asserted below.
  * `qbeta_ck_truncation_order_analysis.py` DOES iterate k = 3,4,5 -- but it
    seeds `Q = Q_N2` from that same N=3 witness, so its cumulative residuals
    start ~602 ppm and are not the block's column either; and it uses the
    SUPERSEDED c_5 = c_3^2*3 + b.
  * `_deprecated/precision-ladder-superseded/precision_ladder_ck_symbolic_probe.py`
    carries the superseded c_5 but computes no ladder residual at all.

  So this file is the first to evaluate the BOXED five-rung product itself,
  N = 0..5, at both documented pins, with a witness.

--------------------------------------------------------------------------
(A) THE SIGN -- SETTLED, and the published minus is wrong.

The block publishes "-0.0066 ppm".  Three independent measurements, all below:

  A1. CONVENTION IDENTIFICATION.  The residual convention is
      (Q_predicted - Q_CODATA)/Q_CODATA -- i.e. exactly
      `qbeta_ladder_convention_fee_probe.ppb`.  This is not assumed: the three
      rows of the block's own table 2 that are quoted with enough digits to be
      unambiguous reproduce, at the MUON pin, to their quoted digits and with
      a PLUS sign:

          table 2 N=0  +1677.5 ppm      this file  +1677.5385 ppm
          table 2 N=1    +73.79 ppm     this file    +73.79756 ppm
          table 2 N=2     +1.24  ppm    this file     +1.2488918 ppm

      At the PROTON pin N=1 is +73.828 ppm, which does not round to 73.79 --
      so the block's table is muon-frame, as the bean recorded.

  A2. STRUCTURE.  Q_A sits 1677 ppm ABOVE CODATA, and every rung factor
      1 + c_k*u^k with c_k < 0 is < 1.  The ladder therefore descends toward
      CODATA FROM ABOVE.  A negative residual requires overshooting zero.

  A3. REACHABILITY.  It does not overshoot.  At the muon pin the N=3 residual
      is +13.153 ppb, and the LARGEST total decrement rungs 4 and 5 can supply
      over every documented coefficient assignment is
      |c_4^retired|*u^4 + |c_5^superseded|*u^5 = 6.589 + 0.576 = 7.165 ppb,
      leaving N=5 >= +5.99 ppb.  At the proton pin N=3 is +43.73 ppb, further
      still.  No documented assignment is negative at either pin.

  Scope (a), and it is a scope-limited negative: this rules out a negative
  residual for THE BLOCK'S BOXED LADDER under the four documented (c_4, c_5)
  assignments at the two documented pins.  It is NOT a proved invariant about
  every ladder, and it is not a claim that no re-derivation could be negative.

  => the corrected headline sign is POSITIVE.

--------------------------------------------------------------------------
WHY THE TABLES SHOW NEGATIVES ANYWAY -- an input-epoch offset, not a sign flip.

Table 2's N=3 row (+6.02 ppb, three significant figures, the tightest
constraint in the block) sits 7.133 ppb BELOW this file's N=3.  A change of
inputs shifts Q_A/Q_CODATA by a relative delta and moves EVERY rung by the
same delta, so one number calibrates the whole column.  Applying that single
offset to this file's column:

    published-epoch N=4, with the RETIRED c_4 = -(b^2+1/2)   ->  -0.569 ppb
    table 2's own N=4 row                                        -0.57  ppb

The offset was calibrated on N=3 and then predicts N=4 to its quoted digits,
with the RETIRED c_4 -- so table 2's N=4 number predates the c_4 supersession
even though its label column already reads "c_3 * b^4".  Under the same offset
the published-epoch N=5 lies in [-0.63, +0.01] ppb over all four assignments.

That is the load-bearing consequence: **-6.6 ppb is not reachable at the
published epoch either.**  The headline's magnitude has no reproducible
provenance in the block's own ladder, at either epoch, under any documented
coefficient assignment -- so the minus sign is not an epoch artefact, and
"nearest row" arguments for the magnitude (the earlier passes' +6.6133 and
+6.02 coincidences) are not provenance.  NOT FITTED HERE: the cause of the
7.133 ppb offset is NOT identified.  It is not the stored Q_AME
(0.78233355931 vs today's Q_NEUTRON_MEV = 0.7823334093099085, a 191.7 ppb
gap in the wrong direction) and it is not the CODATA-2018 -> 2022 m_e move
(1.35 ppb).  Recorded as an unexplained epoch offset, not tuned to anything.

--------------------------------------------------------------------------
WHICH c_5 -- settled on `main` at e2f6a1a76d, restated so this file is
self-contained:

    SDP extraction (qbeta_decay_sdp_full_ck.py)   -1.2229
    -(b^2 + 1/2)                                  -1.2527   2.44 % off  CURRENT
    3*c_3^2 + b                                  +12.8676   1152 %,     SUPERSEDED
                                                             wrong sign

The superseded form survives only in `_deprecated/precision-ladder-superseded/`.
The live ladder here uses c_5 = -(b^2 + 1/2).

NO FITTING.  Every number is the published formula evaluated at a stated pin
with stated coefficients.  Nothing is tuned to make a published column come
out; where a published column is not reproduced this file says so and stops.

mpmath end to end; no float64; no mpf(str(<float64>)).
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys as _sys
import pathlib as _pl

_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    M_E_MEV, Q_NEUTRON_MEV, q_at, q_muon_at,
)

set_compute_dps()

ME = mp.mpf(str(M_E_MEV))
QEXP = mp.mpf(str(Q_NEUTRON_MEV))

# Table 2 / table 3 as PUBLISHED, in ppb.  Read, never written back.
PUB_N0_PPM = mp.mpf("1677.5")
PUB_N1_PPM = mp.mpf("73.79")
PUB_N2_PPM = mp.mpf("1.24")
PUB_N3_PPB = mp.mpf("6.02")
PUB_N4_PPB = mp.mpf("-0.57")
PUB_T3_N5_PPB = mp.mpf("0.04")
HEADLINE_PPM = mp.mpf("-0.0066")

C5_SDP_EXTRACTED = mp.mpf("-1.2229")   # qbeta_decay_sdp_full_ck.py


def b_of(q):
    """Hoefsmit off-diagonal coupling on V_(2,1)."""
    return mp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)


def zC(q):
    """Convention C.  The published ladder is z_C-locked; see the module doc."""
    return mp.sqrt(q) / (q + 1)


def w_blind(q):
    """Colour-blind mixed crossing -- the published choice.

    Verbatim from `qbeta_ladder_convention_fee_probe.main`, NOT re-derived.
    An earlier probe on this bean guessed 0 here and produced an 11.7 %
    residual, ~70x worse than the block's own 'Form A bare' row: a wrong
    baseline makes every downstream comparison measure the baseline.
    """
    return (q - 1 / q) / 2


def q_a(q):
    """Form A single-wrap baseline.  Algebraically identical to the block's
    m_e*|q^2 - 2q - 1|(q+1)/(2q^3); kept in the probe's eps form so this file
    and `qbeta_ladder_convention_fee_probe` are the same function."""
    h = q - 1 / q
    eps = w_blind(q) * h - h
    return abs(_qbeta_e0.order_zero_scaled(eps * ME, q))


def coefficients(q, c4="live", c5="live"):
    """The five rung coefficients c_1..c_5 of the boxed product.

    c_1 is the cosine rung and is handled separately (it is not of the
    1 + c_k u^k form).  c_2..c_5 are returned as SIGNED coefficients in the
    convention `factor_k = 1 + c_k * u^k` -- the convention the deprecated
    producer documents and the one the SDP extraction is quoted in.

      c4="live"     c_3 * b^4          = -2 b^4     (current)
      c4="retired"  -(b^2 + 1/2)                    (pre-supersession)
      c5="live"     -(b^2 + 1/2)                    (current, 6 sites)
      c5="superseded"  +(3 c_3^2 + b)  = +12.8676   (deprecated producer)
    """
    b = b_of(q)
    c3 = mp.mpf(-2)                       # J_Hopf(q=1)
    c4v = c3 * b**4 if c4 == "live" else -(b**2 + mp.mpf(1) / 2)
    if c5 == "live":
        c5v = -(b**2 + mp.mpf(1) / 2)
    elif c5 == "superseded":
        c5v = 3 * c3**2 + b               # POSITIVE: factor > 1, residual rises
    else:
        raise ValueError(c5)
    return {2: mp.mpf(-1), 3: c3, 4: c4v, 5: c5v}


def ladder_partials(q, c4="live", c5="live"):
    """Q_beta after N = 0,1,2,3,4,5 rungs.  Returns (list, u, factors)."""
    h = q - 1 / q
    hb = (q - 1) / q
    b = b_of(q)
    u = b * hb**2
    al = (zC(q) - 1) * h / 2
    c = coefficients(q, c4, c5)
    factors = [mp.cos(al - b * hb**2 / 2)] + [1 + c[k] * u**k for k in (2, 3, 4, 5)]
    out = [q_a(q)]
    for f in factors:
        out.append(out[-1] * f)
    return out, u, factors


def ppb(v):
    """Residual convention -- (predicted - CODATA)/CODATA, in ppb.

    Identical to `qbeta_ladder_convention_fee_probe.ppb`.  Finding A1 in the
    module docstring establishes that this is the block's OWN convention.
    """
    return (v - QEXP) / QEXP * mp.mpf(10) ** 9


def eps_ds_factor():
    """Q/(Q + m_e): the block's n-p mass-split transfer factor (~0.605)."""
    return QEXP / (QEXP + ME)


def main() -> int:
    checks = []

    def check(name, passed, note=""):
        checks.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  {note}" if note else ""))

    q_pr = q_at(50)
    q_mu = q_muon_at(50)
    pins = (("proton", q_pr), ("muon", q_mu))
    assigns = (("live", "live"), ("live", "superseded"),
               ("retired", "live"), ("retired", "superseded"))

    print("=" * 78)
    print(" Q_beta precision ladder, N = 0..5.  CONVENTION C.  mpmath, "
          f"{mp.mp.dps} dps.")
    print("=" * 78)
    print(f"  proton pin q0 = {mp.nstr(q_pr, 20)}")
    print(f"  muon   pin q0 = {mp.nstr(q_mu, 20)}")
    b_pr = b_of(q_pr)
    print(f"  b(proton)     = {mp.nstr(b_pr, 12)}"
          f"   u = {mp.nstr(b_pr * ((q_pr - 1) / q_pr) ** 2, 12)}")

    wb = WitnessBuilder("qbeta-precision-ladder-n5", engine="mpmath")
    wb.set_description(
        "First producer to evaluate the boxed Q_beta five-rung categorical "
        "precision ladder to N=5, at both documented q0 pins and over all four "
        "documented (c_4, c_5) assignments. Settles the published headline's "
        "SIGN: the residual convention is (predicted - CODATA)/CODATA, the "
        "ladder descends to CODATA from above, and no documented assignment "
        "reaches a negative residual at either pin or at the published input "
        "epoch -- so the published '-0.0066 ppm' minus is wrong. Convention C "
        "throughout. No fitting.")

    columns = {}
    for pin, q0 in pins:
        for c4, c5 in assigns:
            parts, u, factors = ladder_partials(q0, c4, c5)
            columns[(pin, c4, c5)] = [ppb(v) for v in parts]

    live_mu = columns[("muon", "live", "live")]
    live_pr = columns[("proton", "live", "live")]

    # ---- the LIVE column, both pins -------------------------------------
    ds = eps_ds_factor()
    print(f"\n  LIVE coefficients (c_4 = c_3 b^4, c_5 = -(b^2+1/2)).  "
          f"eps_dS = {mp.nstr(ds, 6)} * eps_Q\n")
    print(f"  {'N':>2} {'muon eps_Q':>18} {'muon eps_dS':>18} "
          f"{'proton eps_Q':>18} {'proton eps_dS':>18}")
    for n in range(6):
        print(f"  {n:>2} {mp.nstr(live_mu[n], 9):>18} "
              f"{mp.nstr(live_mu[n] * ds, 9):>18} "
              f"{mp.nstr(live_pr[n], 9):>18} "
              f"{mp.nstr(live_pr[n] * ds, 9):>18}   (ppb)")
        wb.add_data(f"muon_live_N{n}_eps_Q_ppb", fmt(live_mu[n]))
        wb.add_data(f"muon_live_N{n}_eps_dS_ppb", fmt(live_mu[n] * ds))
        wb.add_data(f"proton_live_N{n}_eps_Q_ppb", fmt(live_pr[n]))
        wb.add_data(f"proton_live_N{n}_eps_dS_ppb", fmt(live_pr[n] * ds))
    wb.add_data("eps_dS_over_eps_Q", fmt(ds))

    # ---- A1: convention identification, from table 2's unambiguous rows --
    print("\n  A1 -- the block's residual convention, read off its own table 2")
    # N=0 and N=1 are quoted coarsely enough that the 7.133 ppb epoch offset
    # (measured further down) is invisible in them, so they pin the SIGN and
    # the convention directly.  N=2 is quoted to 3 s.f., where 7.133 ppb is
    # 0.6 % of the last digit -- it is checked against its published-epoch
    # value instead, and is not evidence about the convention on its own.
    for lbl, n, pub_ppm, tol in (("N=0", 0, PUB_N0_PPM, "0.0001"),
                                 ("N=1", 1, PUB_N1_PPM, "0.0002")):
        got = live_mu[n] / 1000
        print(f"      {lbl}: published {mp.nstr(pub_ppm, 8):>12} ppm   "
              f"muon pin {mp.nstr(got, 9):>14} ppm")
        check(f"table2_{lbl}_reproduces_at_muon_pin_with_a_PLUS_sign",
              got > 0 and abs(got - pub_ppm) / pub_ppm < mp.mpf(tol))
    print(f"      N=2: published {mp.nstr(PUB_N2_PPM, 8):>12} ppm   "
          f"muon pin {mp.nstr(live_mu[2] / 1000, 9):>14} ppm   "
          f"(3 s.f.; see the epoch offset below)")
    check("table2_N=2_is_POSITIVE_as_published", live_mu[2] > 0)
    check("table2_N1_does_NOT_reproduce_at_the_proton_pin",
          abs(live_pr[1] / 1000 - PUB_N1_PPM) / PUB_N1_PPM > mp.mpf("0.0004"),
          f"proton N=1 = {mp.nstr(live_pr[1] / 1000, 8)} ppm vs published "
          f"{mp.nstr(PUB_N1_PPM, 6)} -- the block's table is muon-frame")

    # ---- A2: structure -- descends from above ---------------------------
    print("\n  A2 -- the ladder descends to CODATA from above")
    check("Q_A_is_above_CODATA", q_a(q_mu) > QEXP,
          f"Form A bare = {mp.nstr(live_mu[0] / 1000, 8)} ppm > 0")
    for pin, q0 in pins:
        _, _, facs = ladder_partials(q0, "live", "live")
        check(f"{pin}_every_live_rung_factor_is_below_one",
              all(f < 1 for f in facs))
        check(f"{pin}_live_column_is_strictly_decreasing",
              all(columns[(pin, 'live', 'live')][i + 1]
                  < columns[(pin, 'live', 'live')][i] for i in range(5)))

    # ---- A3: reachability -- never negative -----------------------------
    print("\n  A3 -- no documented assignment reaches a negative residual")
    print(f"      {'pin':>7} {'c_4':>8} {'c_5':>12} {'N=3':>13} {'N=4':>13} {'N=5':>13}")
    worst = None
    for pin, _ in pins:
        for c4, c5 in assigns:
            col = columns[(pin, c4, c5)]
            print(f"      {pin:>7} {c4:>8} {c5:>12} "
                  f"{mp.nstr(col[3], 8):>13} {mp.nstr(col[4], 8):>13} "
                  f"{mp.nstr(col[5], 8):>13}   (ppb)")
            check(f"{pin}_{c4}C4_{c5}C5_N5_is_POSITIVE", col[5] > 0)
            worst = col[5] if worst is None else min(worst, col[5])
            wb.add_data(f"{pin}_{c4}C4_{c5}C5_N5_ppb", fmt(col[5]))
    print(f"\n      most negative N=5 over all 8 cases = "
          f"{mp.nstr(worst, 9)} ppb  (published headline: "
          f"{mp.nstr(HEADLINE_PPM * 1000, 4)} ppb)")
    check("published_headline_sign_is_WRONG_in_the_blocks_own_convention",
          HEADLINE_PPM < 0 < worst)
    wb.add_data("min_N5_over_all_documented_assignments_ppb", fmt(worst))

    # ---- the epoch offset, calibrated on table 2's N=3 row ---------------
    print("\n  EPOCH OFFSET -- one number, calibrated on table 2's N=3 row")
    offset = live_mu[3] - PUB_N3_PPB
    print(f"      offset = this file's muon N=3 ({mp.nstr(live_mu[3], 8)}) "
          f"- published N=3 ({mp.nstr(PUB_N3_PPB, 3)}) = "
          f"{mp.nstr(offset, 8)} ppb")
    pred_n4_retired = columns[("muon", "retired", "live")][4] - offset
    pred_n4_live = columns[("muon", "live", "live")][4] - offset
    print(f"      predicted published-epoch N=4, RETIRED c_4 = "
          f"{mp.nstr(pred_n4_retired, 6)} ppb   (table 2: "
          f"{mp.nstr(PUB_N4_PPB, 3)})")
    print(f"      predicted published-epoch N=4, LIVE    c_4 = "
          f"{mp.nstr(pred_n4_live, 6)} ppb")
    check("epoch_offset_calibrated_on_N3_predicts_table2_N4_with_the_RETIRED_c4",
          abs(pred_n4_retired - PUB_N4_PPB) < mp.mpf("0.006"),
          "so table 2's N=4 NUMBER predates the c_4 supersession its LABEL "
          "column already reflects")
    check("the_LIVE_c4_does_not_predict_table2_N4",
          abs(pred_n4_live - PUB_N4_PPB) > mp.mpf("0.5"))
    # the same one-number offset also lands table 2's 3-s.f. N=2 row
    pred_n2 = (live_mu[2] - offset) / 1000
    print(f"      predicted published-epoch N=2 = {mp.nstr(pred_n2, 8)} ppm"
          f"   (table 2: {mp.nstr(PUB_N2_PPM, 3)}, i.e. 3 s.f.)")
    check("the_same_offset_lands_table2_N2_within_its_quoted_3_s_f",
          abs(pred_n2 - PUB_N2_PPM) < mp.mpf("0.005"))
    wb.add_data("published_epoch_offset_ppb", fmt(offset))
    wb.add_data("published_epoch_N4_retired_c4_ppb", fmt(pred_n4_retired))

    epoch_n5 = [columns[("muon", c4, c5)][5] - offset for c4, c5 in assigns]
    lo, hi = min(epoch_n5), max(epoch_n5)
    print(f"      published-epoch N=5 over all four assignments: "
          f"[{mp.nstr(lo, 4)}, {mp.nstr(hi, 4)}] ppb")
    check("minus_6p6_ppb_is_unreachable_AT_THE_PUBLISHED_EPOCH_TOO",
          lo > HEADLINE_PPM * 1000 + 1,
          f"so the minus is not an epoch artefact: "
          f"{mp.nstr(lo, 4)} > {mp.nstr(HEADLINE_PPM * 1000, 3)} ppb")
    check("and_table3_published_N5_lies_in_that_epoch_window",
          lo - mp.mpf("0.05") <= PUB_T3_N5_PPB <= hi + mp.mpf("0.05"),
          f"table 3's +{mp.nstr(PUB_T3_N5_PPB, 2)} ppb sits in "
          f"[{mp.nstr(lo, 3)}, {mp.nstr(hi, 3)}]")
    wb.add_data("published_epoch_N5_window_ppb",
                [fmt(lo), fmt(hi)])

    # ---- the declared producer is not the generator of table 2 ----------
    print("\n  (B) the block's DECLARED producer is a different ladder")
    import json
    n3w = _pl.Path(__file__).resolve().parent.parent / \
        "q-beta-operator-valued-N3.witness.json"
    d = json.loads(n3w.read_text())["data"]
    print(f"      probe_q_beta_operator_valued_N3 witness: "
          f"eps_N1 = {d['eps_N1_ppm']} ppm, eps_N2 = {d['eps_N2_ppm']} ppm")
    print(f"      table 2:                                 "
          f"eps_N1 = {mp.nstr(PUB_N1_PPM, 5)} ppm, eps_N2 = "
          f"{mp.nstr(PUB_N2_PPM, 3)} ppm")
    check("declared_producer_does_not_generate_table2_N1",
          abs(mp.mpf(str(d["eps_N1_ppm"])) - PUB_N1_PPM) > 100,
          "674.83 ppm vs 73.79 ppm -- a different N=1 rung, so the declared "
          "producer is not table 2's generator and never was")
    check("declared_producer_carries_no_c5",
          "c_5" not in json.dumps(d))

    # ---- which c_5 -----------------------------------------------------
    c_live = coefficients(q_pr, "live", "live")
    c_sup = coefficients(q_pr, "live", "superseded")
    print("\n  WHICH c_5 (restating the settled result, for self-containment)")
    print(f"      SDP extraction        {mp.nstr(C5_SDP_EXTRACTED, 6)}")
    print(f"      live -(b^2+1/2)       {mp.nstr(c_live[5], 8)}   "
          f"{mp.nstr(abs(c_live[5] - C5_SDP_EXTRACTED) / abs(C5_SDP_EXTRACTED) * 100, 3)} % off")
    print(f"      superseded 3c_3^2+b   {mp.nstr(c_sup[5], 8)}   "
          f"wrong sign")
    check("live_c5_is_within_3pct_of_the_SDP_extraction",
          abs(c_live[5] - C5_SDP_EXTRACTED) / abs(C5_SDP_EXTRACTED) < mp.mpf("0.03"))
    check("superseded_c5_has_the_opposite_sign_to_the_extraction",
          c_sup[5] > 0 > C5_SDP_EXTRACTED)
    wb.add_data("c5_live", fmt(c_live[5]))
    wb.add_data("c5_superseded", fmt(c_sup[5]))
    wb.add_data("c5_sdp_extracted", fmt(C5_SDP_EXTRACTED))

    # ---- what the corrected headline is --------------------------------
    print("\n  CORRECTED HEADLINE (live coefficients, convention C)")
    print(f"      muon pin  (the block's own frame): "
          f"+{mp.nstr(live_mu[5] / 1000, 5)} ppm  "
          f"(+{mp.nstr(live_mu[5], 8)} ppb)")
    print(f"      proton pin (canonical, R2):        "
          f"+{mp.nstr(live_pr[5] / 1000, 5)} ppm  "
          f"(+{mp.nstr(live_pr[5], 8)} ppb)")
    print(f"      published:                         "
          f"{mp.nstr(HEADLINE_PPM, 4)} ppm   <- wrong sign, and a magnitude "
          f"with no reproducible provenance")
    ceiling = mp.mpf("0.0094")
    check("corrected_muon_frame_headline_still_clears_the_cK_ceiling",
          live_mu[5] / 1000 < ceiling,
          f"{mp.nstr(live_mu[5] / 1000, 5)} ppm < {mp.nstr(ceiling, 3)} ppm")
    check("the_canonical_proton_pin_does_NOT_clear_it",
          live_pr[5] / 1000 > ceiling,
          f"{mp.nstr(live_pr[5] / 1000, 5)} ppm > {mp.nstr(ceiling, 3)} ppm "
          "-- say which pin")
    wb.add_data("corrected_headline_muon_ppm", fmt(live_mu[5] / 1000))
    wb.add_data("corrected_headline_proton_ppm", fmt(live_pr[5] / 1000))

    for name, passed in checks:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")
    ok = all(p for _, p in checks)
    print(f"\n  {sum(1 for _, p in checks if p)}/{len(checks)} checks passed")
    print(f"  witness: {wb.save()}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
