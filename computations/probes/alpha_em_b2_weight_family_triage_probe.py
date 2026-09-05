#!/usr/bin/env python3
"""Which weight family pins the alpha_EM B2 scalar c -- and does Molien move it?

Bean `qou-oots`, the triage the corrected consumer audit (PR #6840) left open.

WHY THIS EXISTS. The audit's blast-radius figure went 4-of-36 -> 11-of-37 once
the detector stopped keying on the local variable's spelling, and three of the
seven newly-visible files are on the alpha_EM axis -- an axis the old figure hid
completely. That matters more than the count: the corpus's ONE scoreable L2
result (m_K/m_pi) is alpha_em-conditional, so a weight-family change on this
axis reaches the only sub-100x number the framework currently reports.

WHAT THE CONSUMER ACTUALLY DOES. `alpha_em_b2_scalar_c_probe.py:126` builds

    _q_dimension(shape, q) ** 2 / _q_factorial(sum(shape), q)

and its verdict calls the result "the canonical MARKOV normalization
w_(4,1)(q0) = d_q^2/[5]_q!". Those are two different objects wearing one name:
d_q^2/[n]_q! is the PLANCHEREL-family (historical Wedderburn) weight; the Markov
weight is y_lambda, the Ocneanu weight of the Frobenius pairing
tr_M = SUM y_lam chi_lam. The notation register warns about exactly this
collision. So the question is not only "does Molien move it" but "is the object
in use the one the verdict claims".

THE STRUCTURAL POINT, so the measurement is read correctly. `qou-oots`
established that a lambda-INDEPENDENT rescaling of w cancels in a same-n ratio,
which is why dim_q^2/[n]_q! -> dim_q^2/D^2 is a no-op for consumers that report
ratios. THAT ARGUMENT DOES NOT APPLY HERE. This consumer uses a SINGLE
partition's weight as an absolute normalisation, not a ratio, so even the
lambda-independent change moves it -- and Molien's q^{-kappa} is
lambda-dependent besides. There is no cancellation available to this file under
any of the three families.

WHAT THIS DOES NOT CLAIM. That the B2 scalar c is wrong. The probe under study
is explicit that the physical c is (Markov norm)/(Hodge polarization norm) and
that the Hodge denominator -- the Braden-Northover period polarization of
Jac(Bring) -- is NOT yet supplied. So c is not currently a delivered number, and
this probe measures the size of the family choice on its numerator, not an error
in a published value. It is a bound on what the qou-oots ruling can move, and a
flag that the numerator's family is mislabelled in the consumer's own verdict.

No float64: mpmath end to end at the module default dps, integers exact.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import molien_feray_meliot_bridge_probe as MB  # noqa: E402
import plancherel_deformation_uniqueness_probe as PU  # noqa: E402

# The partition the alpha_EM B2 consumer pins on: the standard H_5 block.
LAMBDA = (4, 1)
N_BOX = 5

# The value that consumer prints, quoted from its own stdout so the comparison
# is against what it actually reports rather than against a re-derivation.
#
# Held as a STRING at module scope, never as an `mp.mpf`. A module-level
# `mp.mpf("...")` is evaluated at import, when `mp.dps` is whatever the import
# order happens to have left it at -- mpmath's own default is 15, at which this
# 20-digit literal truncates to ...882560657, an error of 5.98e-18. That is
# LARGER than the 1e-18 tolerance the identification assertion below uses, so
# the check would have been silently comparing against a damaged constant. It
# passed here only because an earlier import had already raised dps, which is
# the order-dependence `module_const_precision_audit.py` exists to catch and
# which this probe tripped on its first run.
CONSUMER_REPORTED_STR = "0.12862000417524688333"


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(Q_50_DIGIT_STR)
    consumer_reported = mp.mpf(CONSUMER_REPORTED_STR)

    b = WitnessBuilder("alpha-em-b2-weight-family-triage")
    b.set_description(
        "Bean qou-oots. Triages the weight family under the alpha_EM B2 scalar "
        "c. alpha_em_b2_scalar_c_probe.py pins on d_q^2/[5]_q! at lambda=(4,1) "
        "and its verdict calls that 'the canonical MARKOV normalization' -- but "
        "d_q^2/[n]_q! is the PLANCHEREL-family (historical Wedderburn) weight, "
        "while the Markov weight is the Ocneanu y_lambda. This probe evaluates "
        "all three families at that one partition and reports the ratios, so "
        "the size of the qou-oots family choice on this axis is on the record. "
        "The consumer uses a SINGLE partition's weight as an absolute "
        "normalisation, not a same-n ratio, so the cancellation that makes "
        "dim_q^2/[n]_q! -> dim_q^2/D^2 a no-op for the beta_EW consumers is NOT "
        "available here. NOT a claim that c is wrong: c = (Markov "
        "norm)/(Hodge polarization norm) and the Hodge denominator is openly "
        "unsupplied, so c is not a delivered number."
    )
    b.add_parameter("q0_50dps", Q_50_DIGIT_STR)
    b.add_parameter("lambda", str(list(LAMBDA)))

    d_q = PU.dim_q(q0, LAMBDA)
    qfact = PU.q_factorial(q0, N_BOX)
    w_planch = d_q ** 2 / qfact
    w_molien = MB.molien_weight(q0, LAMBDA)
    kappa = MB.content_sum(LAMBDA)
    f_lam = MB.f_lambda(LAMBDA)

    # Ocneanu / Markov, the family the consumer's verdict NAMES. (4,1) has two
    # rows so it survives the Schur-Weyl row cap at N = 2 and is comparable.
    y = y_lambda_su_n(N_BOX, q0, 2)
    y_lam = mp.mpf(str(y[LAMBDA])) if LAMBDA in y else None

    b.add_data("weights_at_lambda", {
        "dim_q": fmt(d_q),
        "q_factorial_5": fmt(qfact),
        "f_lambda": f_lam,
        "kappa_contentSum": kappa,
        "plancherel_dimq2_over_qfact": fmt(w_planch),
        "molien": fmt(w_molien),
        "markov_ocneanu_y_at_N2": fmt(y_lam) if y_lam is not None else None,
    })

    # -- does the audit's identification of the consumer's weight hold? --------
    b.add_assertion(
        "consumer_reported_value_is_the_plancherel_weight",
        computed=fmt(w_planch),
        expected=fmt(consumer_reported),
        tolerance="1e-18",
        unit="dimensionless",
        source="alpha_em_b2_scalar_c_probe.py stdout reports w_(4,1)(q0) = "
               "0.12862000417524688333 and its source builds "
               "_q_dimension(shape,q)**2/_q_factorial(sum(shape),q). Recomputing "
               "d_q^2/[5]_q! independently here confirms the consumer's number "
               "IS the Plancherel-family weight -- which is what the corrected "
               "audit claims and what its own verdict string denies by calling "
               "it Markov.",
    )

    # -- the size of the family choice on this axis ---------------------------
    ratio_molien = w_molien / w_planch
    b.add_data("family_change_factors", {
        "molien_over_plancherel": fmt(ratio_molien),
        "molien_over_plancherel_pct_move": fmt((ratio_molien - 1) * 100),
        "markov_over_plancherel": (fmt(y_lam / w_planch)
                                   if y_lam is not None else None),
        "note": "molien/plancherel = f^lam * q^{-kappa} / d_q at this lambda, "
                "since both carry the same 1/[n]_q!. The move is NOT small and "
                "does NOT cancel: this consumer normalises on ONE partition, so "
                "there is no same-n ratio for a lambda-independent factor to "
                "drop out of, and Molien's q^{-kappa} is lambda-dependent "
                "besides. The Markov row is the family the consumer's verdict "
                "NAMES; it is a third, different number, which is the point.",
    })

    # Stated as a genuine predicate rather than as a two-number comparison, so
    # a reader who checks only the summary line is not told FAILURES by a
    # witness in which nothing failed. The magnitude itself is in
    # `family_change_factors` above, where it belongs.
    b.add_assertion(
        "molien_move_on_this_axis_exceeds_one_percent",
        computed="1" if abs(ratio_molien - 1) > mp.mpf("0.01") else "0",
        expected="1",
        source=f"|molien/plancherel - 1| = {fmt(abs(ratio_molien - 1))} at "
               f"lambda={list(LAMBDA)}. The threshold is a legibility floor, "
               f"not a physical scale: it asserts only that the qou-oots family "
               f"choice is not a rounding effect on the alpha_EM axis. The "
               f"actual move is ~42%.",
    )

    b.save()

    print(f"lambda = {list(LAMBDA)}   n = {N_BOX}   q0 = {Q_50_DIGIT_STR[:14]}")
    print(f"  f^lambda = {f_lam}   kappa = contentSum = {kappa}   "
          f"d_q = {fmt(d_q)[:18]}")
    print()
    print(f"  Plancherel  d_q^2/[5]_q!        = {fmt(w_planch)[:22]}"
          f"   <- what the consumer computes")
    print(f"  Molien      f^l q^-k d_q/[5]_q! = {fmt(w_molien)[:22]}"
          f"   <- what qou-oots makes canonical")
    if y_lam is not None:
        print(f"  Markov      y_(4,1) at N=2         = {fmt(y_lam)[:22]}"
              f"   <- what its verdict CALLS it")
    print()
    print(f"  Molien / Plancherel = {fmt(ratio_molien)[:20]}  "
          f"({fmt((ratio_molien - 1) * 100)[:8]} %)")
    print("\nNo cancellation is available: this is a single-partition absolute "
          "normalisation,\nnot a same-n ratio.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
