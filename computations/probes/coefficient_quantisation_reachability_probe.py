#!/usr/bin/env python3
"""Is the log-family magnitude coefficient REACHABLE by a quantised carrier?

EXPLORATORY (audit-only, no rewire, no fit, no selection). Formalize-first
prune for bean `qou-fcn8` / arc `bk-crossing-mass-binding`: rather than SEARCH
for a per-bond correction factor, test whether the REQUIRED correction can lie
in the class a carrier-crossing invariant is able to produce.

-----------------------------------------------------------------------------
WHY THIS EXISTS (and how it differs from the sibling's live work)

A sibling session (`session_01CSQEiZrbpPxfMZEFrzbKtD`) is attacking the two-
nucleon BINDING CHANNEL ASYMMETRY (deuteron 3S1 bound 2.224566 MeV vs np 1S0
virtual ~0.066 MeV, ratio 33.7). Four routes to THAT number have closed:
isospin_channel_R=1; block_transposition ceiling 9; Markov-trace family rank;
and the linking class (I_3-valued, channel-blind, scope-(b)).

THIS probe targets a DIFFERENT number: the log-family MAGNITUDE coefficient
--- the forced-chain log-ratio binding lands at 0.79-3.26x AME across D..7Be
(`log_ratio_binding_prototype`), and `qou-fcn8`/`qou-brng` need to know what
could supply that correction. Same arc, different target, distinct angle.

THE OBSERVATION BEING TESTED. Every categorical invariant the arc has on hand
is QUANTISED:
  * carrier crossing counts -> `bRatio = c3/c2 - 3`, a ratio of INTEGERS
    (`QOU.Mass.CarrierCrossingQuantisation`; its Lean enumerates -2, -1, 0,
    -11/6 for the four canonical carriers);
  * inter-nucleon linking -> I_3-valued, {0, +-1}
    (`two_nucleon_linking_matrix_channel_blind_probe`);
  * block-transposition log-moduli -> integer-quantised to 1.8e-22 at 90 dps
    (`block_transposition_lift_probe`).
A quantised invariant supplies only a discrete set of rationals. The required
correction is a measured REAL. So the preregistered question is not "which
factor?" but:

    Are the required per-nucleus corrections small-denominator rationals
    (hence reachable by a ratio of small integer crossing counts), or not?

PREREGISTERED VERDICT RULE (fixed before the numbers are read):
  * If every required correction is within `TOL_REL` of a rational with
    denominator <= `Q_MAX`, the quantised class REMAINS LIVE and this probe
    reports the concrete integer targets a carrier would have to realise.
  * If they are not, the quantised carrier class CANNOT supply the coefficient
    --- a prune of the class, reported scope-(a) (it excludes THIS class at
    THIS denominator bound; it is not a claim about every conceivable carrier).

ENTROPY GUARD (AGENTS.md formalize-first / anti-fit). A small-denominator hit
is only weak evidence: with denominators up to Q_MAX there are O(Q_MAX^2)
rationals in range, so a hit at loose tolerance is expected by chance. The
probe therefore reports, alongside each hit, the COUNT of admissible rationals
within tolerance --- if that count is large the "hit" carries no information
and is reported as such. No value is selected; all are printed.

NO FIT: nothing here is tuned. AME and the committed log-ratio predictions are
inputs; the only computation is a continued-fraction best-rational search,
which is deterministic.

-- Ref: log_ratio_binding_prototype.py (the 0.79-3.26x forced-chain figures);
QOU/Mass/CarrierCrossingQuantisation.lean (bRatio = c3/c2 - 3, integer counts);
probes/two_nucleon_linking_matrix_channel_blind_probe.py (linking class dead);
probes/block_transposition_lift_probe.py (integer-quantised log-moduli);
docs/audits/2026-09-03-brng-substubs-closeout-and-coefficient-options.md.
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
if str(_COMP) not in sys.path:
    sys.path.insert(0, str(_COMP))
from substrate._precision import set_compute_dps  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_HE3_MEV_VALIDATION

set_compute_dps()

# Verdict-rule constants, fixed BEFORE reading any number.
Q_MAX = 12          # max denominator a "small integer crossing-count ratio" may have
TOL_REL = mp.mpf("0.02")   # 2% -- looser than the physics needs, deliberately generous

# Committed forced-chain log-ratio predictions vs AME
# (log_ratio_binding_prototype.py, B_log(E0) column; AME from its own table).
ROWS = [
    # atom,  A,  B_AME MeV,      B_chain_log MeV
    ("D",    2, mp.mpf("2.22457"), mp.mpf("2.83316")),
    ("T",    3, mp.mpf("8.4818"),  mp.mpf("6.63095")),
    ("3He",  3, AME_B_HE3_MEV_VALIDATION, mp.mpf("4.88387")),
    ("4He",  4, mp.mpf("28.2957"), mp.mpf("8.68166")),
    ("6Li",  6, mp.mpf("31.994"),  mp.mpf("14.5301")),
    ("7Li",  7, mp.mpf("39.2451"), mp.mpf("18.3279")),
    ("7Be",  7, mp.mpf("37.6008"), mp.mpf("16.5809")),
]


def best_rational(x: mp.mpf, qmax: int) -> Fraction:
    """Best rational approximation to x with denominator <= qmax (continued
    fractions, deterministic — no search over a tuned grid)."""
    return Fraction(float(x)).limit_denominator(qmax)


def count_admissible(x: mp.mpf, qmax: int, tol_rel: mp.mpf) -> int:
    """How many distinct rationals p/q (q <= qmax) sit within tol_rel of x.
    A large count means a 'hit' is uninformative (the entropy guard)."""
    lo, hi = x * (1 - tol_rel), x * (1 + tol_rel)
    seen = set()
    for q in range(1, qmax + 1):
        p_lo = int(mp.ceil(lo * q))
        p_hi = int(mp.floor(hi * q))
        for p in range(p_lo, p_hi + 1):
            if p <= 0:
                continue
            seen.add(Fraction(p, q))
    return len(seen)


def main() -> int:
    t0 = time.monotonic()
    rows, all_reachable = [], True
    for name, A, b_ame, b_pred in ROWS:
        r = b_ame / b_pred                      # required correction factor
        fr = best_rational(r, Q_MAX)
        approx = mp.mpf(fr.numerator) / fr.denominator
        rel = abs(approx - r) / r
        reachable = rel <= TOL_REL
        n_adm = count_admissible(r, Q_MAX, TOL_REL)
        if not reachable:
            all_reachable = False
        rows.append({
            "atom": name, "A": A,
            "B_AME_MeV": mp.nstr(b_ame, 6),
            "B_chain_log_MeV": mp.nstr(b_pred, 6),
            "required_correction": mp.nstr(r, 8),
            "best_rational_q_le_12": f"{fr.numerator}/{fr.denominator}",
            "rel_err": mp.nstr(rel, 4),
            "reachable_within_2pct": reachable,
            "n_admissible_rationals": n_adm,
        })

    spread = max(mp.mpf(r["required_correction"]) for r in rows) / \
        min(mp.mpf(r["required_correction"]) for r in rows)
    mean_adm = sum(r["n_admissible_rationals"] for r in rows) / len(rows)

    if all_reachable and mean_adm <= 2:
        verdict = ("LIVE + INFORMATIVE: every required correction is a "
                   "small-denominator rational and the admissible count is low.")
    elif all_reachable:
        verdict = (
            f"LIVE but UNINFORMATIVE: every required correction sits within "
            f"{float(TOL_REL)*100:.0f}% of some rational with q<={Q_MAX}, but on "
            f"average {mean_adm:.1f} distinct rationals qualify per nucleus — so "
            f"'it is a small rational' is expected by chance and carries NO "
            f"evidence that a quantised carrier supplies it. The correction "
            f"spread is {float(spread):.2f}x and A-dependent; a single carrier "
            f"ratio cannot track it. Scope-(a): the quantised carrier class is "
            f"not EXCLUDED here, but neither is it supported — this is a null "
            f"result, not a lead."
        )
    else:
        verdict = (
            f"PRUNED (scope-(a)): at least one required correction is NOT within "
            f"{float(TOL_REL)*100:.0f}% of any rational with denominator <= {Q_MAX}, "
            f"so a ratio of small integer crossing counts cannot supply it."
        )

    result = {
        "verdict_rule": {
            "Q_MAX": Q_MAX, "TOL_REL": mp.nstr(TOL_REL, 3),
            "fixed_before_reading_numbers": True,
        },
        "rows": rows,
        "correction_spread": mp.nstr(spread, 5),
        "mean_admissible_rationals": f"{mean_adm:.2f}",
        "verdict": verdict,
    }
    payload = {
        "computation": "coefficient-quantisation-reachability",
        "description": ("Formalize-first prune: can a quantised (integer "
                        "crossing-count) carrier supply the log-family magnitude "
                        "coefficient? Tests small-denominator reachability of the "
                        "required per-nucleus corrections, with an entropy guard. "
                        "Audit-only; no fit; no selection."),
        "tier": "exploratory (class-reachability prune)",
        "result": result,
    }
    import platform
    wb = WitnessBuilder.wrap_legacy(
        "coefficient-quantisation-reachability", payload,
        script_path=__file__, engine="python+mpmath",
        engine_version=f"python {platform.python_version()} + mpmath {mp.__version__}",
        output_dir=str(_HERE), start_time=t0,
    )
    wb.add_assertion("entropy_guard_reported",
                     computed=str(all("n_admissible_rationals" in r for r in rows)),
                     expected="True")
    wb.save(extra={"auditOnly": True})

    print("=== coefficient quantisation reachability (route-1 class prune) ===")
    print(f"  rule fixed in advance: q <= {Q_MAX}, tol {float(TOL_REL)*100:.0f}%")
    print(f"  {'atom':>5} {'req corr':>10} {'best p/q':>9} {'rel err':>9} {'#adm':>5}")
    for r in rows:
        print(f"  {r['atom']:>5} {r['required_correction']:>10} "
              f"{r['best_rational_q_le_12']:>9} {r['rel_err']:>9} "
              f"{r['n_admissible_rationals']:>5}")
    print(f"  spread {mp.nstr(spread,5)}x | mean admissible {mean_adm:.2f}")
    print("  " + verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
