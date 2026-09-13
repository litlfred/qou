#!/usr/bin/env python3
"""Is `beta_ew_delta_I_321_and_wedderburn.py`'s "Markov trace" a Markov trace?

Follow-on from bean `qou-oots` (Molien ruled canonical for Phi_k, 2026-09-05).
While measuring that ruling's blast radius, the consumer audit named
`beta_ew_delta_I_321_and_wedderburn.py` as the one live non-harness file still
carrying the superseded `dim_q^2/[n]_q!` weight. The obvious follow-on was to
migrate it to Molien. Reading it first turns up a different and prior question.

The file computes, and labels, a **"Wedderburn-weighted Markov trace"**:

    tr_M(beta_EW Delta_I) = SUM_lam w_lam * chi^lam,   w_lam = dim_q^2/[n]_q!

But the canonical Frobenius pairing of this framework is

    tr_M = SUM_lam y_lam * chi_lam

with the **Ocneanu/Markov** weights y_lam -- not a Plancherel-family weight.
AGENTS.md states that form in the canonical derivation chain, and the notation
register separates the three partition-weight families explicitly, warning that
they coincide only at q = 1.

So the question this probe asks is NOT "which Plancherel family should it use".
It is: **does the quantity that file calls tr_M equal the Markov trace at all?**
If it does, the naming is loose and nothing else follows. If it does not, then
its six Weinberg-angle cot(theta_W) candidates are ratios of a quantity that is
not the object they are named after, and the qou-oots migration question is
moot for this file because the weight is from the wrong family entirely.

WHAT IS MEASURED, and what each outcome would mean:

  T1  y_lam vs w_lam per partition at n = 6, the file's own n. If these agree
      the whole question dissolves.
  T2  the two traces of the SAME character vector, SUM y_lam chi and
      SUM w_lam chi, on the file's own partitions of 6. Reported as a ratio and
      as a relative deviation.
  T3  the SIX candidate readings the file reports are all RATIOS of w-weighted
      quantities at fixed n, so a lambda-INDEPENDENT reweighting cancels from
      every one of them. This checks whether y/w is lambda-independent -- i.e.
      whether the file's *conclusions* are affected at all, separately from
      whether its *label* is right. A wrong label with invariant conclusions is
      a documentation defect; a wrong label with moving conclusions is not.
  T4  the q -> 1 limit, where the register says the families coincide. This is
      the control: if T1/T2 show a difference that does NOT vanish as q -> 1,
      the difference is not the q-deformation and something else is wrong.

NOT ASSUMED: that y_lam is "the right" weight for this file's physics. That is
a question about what beta_EW Delta_I is a trace OF, which this probe does not
touch. What it establishes is only whether the computed object matches its name.

Characters are taken from the file's own construction path so the comparison is
of WEIGHTS ONLY, not of two different character conventions -- comparing a
quantity computed two different ways is how a weight difference gets attributed
to the wrong cause.

Exact where possible, mpmath at 50 dps otherwise. No float64 (AGENTS.md
NO-FLOAT64 binds probes; note the consumer under study declares an
`archimedean_by_design` float64 exemption for its numpy eigenvalue path, which
this probe does not inherit and does not exercise).
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

from molien_feray_meliot_bridge_probe import (  # noqa: E402
    partitions, hooks, f_lambda,
)


def qint(q, k: int):
    return (q ** k - q ** (-k)) / (q - q ** (-1))


def qfac(q, n: int):
    out = mp.mpf(1)
    for k in range(1, n + 1):
        out *= qint(q, k)
    return out


def dim_q(q, lam):
    den = mp.mpf(1)
    for h in hooks(lam):
        den *= qint(q, h)
    return qfac(q, sum(lam)) / den


def w_plancherel(q, lam):
    """The weight the consumer actually uses: dim_q^2/[n]_q!."""
    d = dim_q(q, lam)
    return d * d / qfac(q, sum(lam))


def main() -> int:
    set_compute_dps()
    b = WitnessBuilder("beta-ew-weight-is-not-markov")
    b.set_description(
        "Asks whether the quantity `beta_ew_delta_I_321_and_wedderburn.py` "
        "labels a 'Wedderburn-weighted Markov trace' -- SUM_lam "
        "(dim_q^2/[n]_q!) chi^lam -- equals the Markov trace SUM_lam y_lam "
        "chi_lam that AGENTS.md gives as this framework's canonical Frobenius "
        "pairing. Follow-on from bean qou-oots, which named this file as the "
        "one live non-harness consumer of the superseded Plancherel weight. "
        "The prior question is not WHICH Plancherel family it should use but "
        "whether a Plancherel weight belongs there at all, since the Markov "
        "trace is defined with the Ocneanu weights y_lam. Reports the "
        "per-partition weight ratio, the two traces of the same character "
        "vector, whether the ratio is lambda-INDEPENDENT (which decides "
        "whether the file's six cot(theta_W) candidates -- all same-n ratios "
        "-- move at all, as against only its label being wrong), and the "
        "q -> 1 control where the register says the families coincide."
    )
    b.add_parameter("q0_50dps", Q_50_DIGIT_STR)
    b.add_parameter("consumer_under_study",
                    "computations/beta_ew_delta_I_321_and_wedderburn.py")
    b.add_parameter("n", "6")

    q0 = mp.mpf(Q_50_DIGIT_STR)
    n = 6
    lams = partitions(n)

    # y_lambda_su_n returns the Ocneanu family at N=2 (the mass-channel member,
    # convention D). Keyed by partition tuple.
    y_raw = y_lambda_su_n(n, q0, 2)
    y = {}
    for k, v in y_raw.items():
        key = tuple(k) if not isinstance(k, tuple) else k
        y[key] = mp.mpf(str(v)) if not isinstance(v, mp.mpf) else v

    # -- T1: per-partition comparison -----------------------------------------
    rows = {}
    ratios = []          # only over the SHARED support (both weights nonzero)
    missing = []
    y_zero_lams, w_zero_lams = [], []
    for lam in lams:
        wl = w_plancherel(q0, lam)
        yl = y.get(lam)
        if yl is None:
            missing.append(list(lam))
            continue
        if yl == 0:
            y_zero_lams.append(list(lam))
        if wl == 0:
            w_zero_lams.append(list(lam))
        rows[str(list(lam))] = {
            "rows_in_lambda": len(lam),
            "y_lambda": fmt(yl), "w_plancherel": fmt(wl),
            "ratio_y_over_w": (fmt(yl / wl) if wl != 0 else None),
        }
        if wl != 0 and yl != 0:
            ratios.append(yl / wl)
    b.add_data("T1_per_partition_n6", {
        "note": "y_lambda is the Ocneanu/Markov weight (SU(2) member, "
                "convention D) as the corpus computes it; w_plancherel is the "
                "weight the consumer uses.",
        "partitions_without_a_y_weight": missing,
        "y_lambda_ZERO_on": y_zero_lams,
        "w_plancherel_ZERO_on": w_zero_lams,
        "shared_support_size": len(ratios),
        "total_partitions": len(lams),
        "rows": rows,
    })
    b.add_assertion(
        "the_two_weights_have_DIFFERENT_SUPPORT",
        computed="1" if (y_zero_lams and not w_zero_lams) else "0", expected="1",
        source=f"At n=6 the Markov weight y_lambda vanishes on "
               f"{len(y_zero_lams)} of {len(lams)} partitions (every lambda "
               f"with more than 2 rows -- the SU(2) row cap) while the "
               f"Plancherel weight the consumer uses is nonzero on all "
               f"{len(lams)}. They are not two weightings of one sum; they are "
               f"sums over DIFFERENT INDEX SETS, and no lambda-independent "
               f"rescaling relates them.",
    )

    families_differ = (bool(y_zero_lams)
                       or any(abs(r - 1) > mp.mpf("1e-30") for r in ratios))
    b.add_assertion(
        "markov_and_plancherel_weights_differ",
        computed="1" if families_differ else "0", expected="1",
        source="y_lambda != dim_q^2/[n]_q! per partition at n=6, q0 — so the "
               "consumer's weight is not the Markov weight",
    )

    # -- T3 (computed before T2 because it decides what T2 MEANS) -------------
    # If y/w is lambda-INDEPENDENT, every same-n ratio the consumer reports is
    # invariant and only its label is wrong.
    spread = None
    lam_independent = None
    if ratios and min(ratios) != 0:
        spread = max(ratios) / min(ratios)
        lam_independent = abs(spread - 1) < mp.mpf("1e-30")
    b.add_data("T3_is_the_reweighting_lambda_independent", {
        "ratio_spread_max_over_min_ON_SHARED_SUPPORT":
            fmt(spread) if spread is not None else None,
        "lambda_independent": lam_independent,
        "CAVEAT": "Computed only where BOTH weights are nonzero, so it "
                  "UNDERSTATES the difference -- the partitions where y_lambda "
                  "vanishes are excluded, and those are the point. A weight "
                  "that is zero where the other is positive cannot be reached "
                  "by ANY lambda-independent rescaling, so the invariance "
                  "question is already settled NO by the support difference.",
        "consequence":
            "The consumer reports SIX cot(theta_W) candidates and every one is "
            "a ratio of w-weighted quantities at the SAME n. A "
            "lambda-independent reweighting cancels exactly from all of them, "
            "so if this is True the label is wrong but the numbers stand; if "
            "False the reported candidates are not invariant under using the "
            "weight the name claims.",
    })

    # -- T2: the two traces of the SAME character vector ----------------------
    # A synthetic character vector is used deliberately: the real chi comes from
    # the consumer's float64 numpy eigenvalue path, and importing that would put
    # a float64 quantity on BOTH sides, hiding nothing but adding noise. What is
    # under test is the weighting, so any fixed chi exhibits it.
    chi = {lam: mp.mpf(f_lambda(lam)) for lam in lams}   # chi at the identity
    tr_y = mp.fsum(y[lam] * chi[lam] for lam in lams if lam in y)
    n_terms_y = sum(1 for lam in lams if lam in y and y[lam] != 0)
    tr_w = mp.fsum(w_plancherel(q0, lam) * chi[lam] for lam in lams)
    # THE DECISIVE ONE. chi^lam(identity) = f^lam, so these two sums evaluate
    # each weighting at the identity braid. A Markov trace is NORMALISED --
    # tr_M(1) = 1 by definition -- so this is not a comparison of two
    # conventions, it is a test of whether the object is a Markov trace at all.
    # RESIDUAL against 0, not value against target: the verdict path
    # (qou_substrate/witness.py) compares float(computed) to
    # float(expected), so a value-vs-value form here could not resolve
    # anything below the float64 floor and the tolerance below it was
    # unreachable by ~10^24. A residual near zero IS representable as a
    # float64 all the way down, so the same tolerance is a real bound.
    # Gate: computations/audits/tolerance_below_arithmetic_floor_audit.py.
    b.add_assertion(
        "markov_trace_of_identity_is_one",
        computed=fmt(abs(tr_y - 1)), expected="0", tolerance="1e-40",
        source="|SUM_lam y_lam chi^lam(1) - 1| = 0 exactly -- y_lam IS a "
               "normalised Markov trace, confirming the weights were read "
               "correctly",
    )
    b.add_assertion(
        "consumer_weighting_of_identity_is_NOT_one",
        computed="1" if abs(tr_w - 1) > mp.mpf("0.5") else "0", expected="1",
        source=f"SUM_lam (dim_q^2/[n]_q!) chi^lam(1) = {fmt(tr_w)[:12]}, not 1. "
               f"A Markov trace sends the identity to 1 by definition, so the "
               f"quantity the consumer labels tr_M is not a Markov trace -- "
               f"this is a fact about the object, independent of any "
               f"convention choice.",
    )
    b.add_data("T2_traces_of_the_same_character_vector", {
        "chi_used": "chi^lam(identity) = f^lam — a fixed, exactly-known vector, "
                    "so any difference is attributable to the WEIGHTS alone",
        "nonzero_terms_in_y_trace": n_terms_y,
        "nonzero_terms_in_w_trace": len(lams),
        "trace_with_y_lambda": fmt(tr_y),
        "trace_with_w_plancherel": fmt(tr_w),
        "ratio": fmt(tr_y / tr_w) if tr_w != 0 else None,
        "rel_deviation": fmt(abs(tr_y - tr_w) / abs(tr_w)) if tr_w != 0 else None,
    })

    # -- T4: control at q -> 1 ------------------------------------------------
    q1 = mp.mpf(1) + mp.mpf(10) ** (-25)
    y1 = y_lambda_su_n(n, q1, 2)
    r1, y1_zero = [], 0
    for lam in lams:
        wl = w_plancherel(q1, lam)
        yv = y1.get(lam)
        if yv is None:
            continue
        yv = mp.mpf(str(yv))
        if yv == 0:
            y1_zero += 1
            continue
        if wl != 0:
            r1.append(yv / wl)
    q1_spread = (max(r1) / min(r1)) if r1 and min(r1) != 0 else None
    b.add_data("T4_control_at_q_to_1", {
        "q_used": "1 + 1e-25",
        "ratio_spread_at_q_to_1_ON_SHARED_SUPPORT":
            fmt(q1_spread) if q1_spread is not None else None,
        "y_lambda_still_zero_on_this_many_partitions_at_q_to_1": y1_zero,
        "reading": "If y_lambda is STILL zero on the same partitions as q -> 1, "
                   "the support difference is NOT a q-deformation effect -- it "
                   "is the SU(2) row cap, a statement about N that survives the "
                   "classical limit. The register's 'the families coincide at "
                   "q = 1' then does not extend to y_lambda at N = 2.",
        "note": "The notation register says the three partition-weight "
                "families coincide at q = 1. If the spread here does NOT "
                "collapse toward 1, the difference measured at q0 is not the "
                "q-deformation and a different explanation is needed.",
    })

    b.save()
    print(f"T1 families differ at n=6:            {families_differ}")
    print(f"   y_lambda ZERO on {len(y_zero_lams)}/{len(lams)} partitions; "
          f"w_plancherel zero on {len(w_zero_lams)}/{len(lams)}")
    print(f"T3 reweighting lambda-independent:    {lam_independent}"
          f"   (spread {fmt(spread)[:12] if spread is not None else 'n/a'})")
    print(f"T2 trace with y_lambda:  {fmt(tr_y)[:20]}")
    print(f"   trace with w_plancherel: {fmt(tr_w)[:20]}")
    print(f"T4 spread as q -> 1:      "
          f"{fmt(q1_spread)[:14] if q1_spread is not None else 'n/a'}"
          f"   (y still zero on {y1_zero})")
    if missing:
        print(f"!! partitions with no y weight: {missing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
