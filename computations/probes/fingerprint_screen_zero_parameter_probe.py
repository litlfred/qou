#!/usr/bin/env python3
"""fingerprint_screen_zero_parameter_probe.py

Screening candidates against the two-number fingerprint -- and what the screen
says about ITSELF.

THE FINGERPRINT
---------------
two_term_structure_degeneracy established that with the saturating half inert
below A=5, ONE term carries b2, b3 and b4, leaving two parameter-free predictions.
Normalised to f(2) = 1, they are:

    f(4) = B(4)/B(2) = 12.71963154        <- CONVENTION-INDEPENDENT
    f(3) = 3.641123 (isospin avg) .. 3.812787 (Coulomb-corrected), a 4.7% band

Note the asymmetry, which the screen exploits: f(4) does not involve the A=3
binding at all, so it carries NO convention systematic. f(3) carries all of it.

RESULT 1 -- A FREE PARAMETER DESTROYS THE TEST
-----------------------------------------------
First design: give each one-parameter family f_alpha its head, fit alpha to the
SOLID number f(4), then PREDICT f(3). One parameter, one prediction.

Ten families; one hit (alpha^A * A, alpha = 2.5219, predicting f(3) = 3.7828).

**That hit is exactly the chance expectation and is NOT evidence.** The nine
valid predictions span 3.089 .. 4.820, a range of 1.731; the band is 0.172 wide;
so the per-candidate chance rate is 9.9% and the expected number of hits is 0.89.
Observed: 1.

The root cause is structural: spending the f(4) constraint on a fitted parameter
leaves a single prediction against a 4.7% band, which is a ~10% false-positive
filter. **A fingerprint only discriminates when applied with ZERO free
parameters**, so that both numbers are predictions.

RESULT 2 -- ZERO-PARAMETER SCREEN: 0 of 14
-------------------------------------------
Re-run with candidates the framework supplies outright -- no fitting anywhere,
q0 fixed at the proton pin:

    candidate           f(3)      f(4)     f3 err   f4 err
    n!                  3.0       12.0     17.61%    5.66%
    [n]_q!              3.0437    12.5087  16.41%    1.66%
    C(2n,n)             3.3333    11.6667   8.45%    8.28%
    n! * q0^n           3.3299    14.7846   8.55%   16.23%
    (n-1)! * 2^n        4.0       24.0      5.14%   88.68%
    Catalan(n)          2.5        7.0     31.34%   44.97%
    involutions I(n)    2.0        5.0     45.07%   60.69%
    ... (14 total)

**None hits both.** Closest overall is C(2n,n) at ~8% on each -- not a hit, and
with 14 candidates an 8% near-miss is unremarkable.

RESULT 3 -- THE MISS IS STRUCTURED, WHICH IS THE USEFUL PART
-------------------------------------------------------------
The factorial family lands f(3) ~ 3.00-3.04 against a measured 3.64-3.81: LOW by
16-18%, while [n]_q! is within 1.7% on f(4). So these families get the A=4
growth roughly right and the A=3 step badly wrong -- they give b3/b2 ~ 0 where
the measurement wants 0.64.

That is the same defect the whole arc keeps hitting, in the fingerprint's
coordinates: a smoothly-growing single term reproduces the FOURTH cumulant far
better than the THIRD. Whatever supplies b3 is not a smooth growth law.

SCOPE
-----
An honest negative screen. Derives nothing, refutes no named framework claim, and
does not exhaust the candidate space -- 14 hand-chosen zero-parameter functions
is a sample, not an enumeration. Its durable content is RESULT 1: the fingerprint
must be applied with zero free parameters or it does not discriminate, which is a
constraint on how any future candidate gets tested.

Bean qou-edt7.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import comb, factorial  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from q_parameter import Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)


def main() -> int:
    wb = WitnessBuilder("fingerprint-screen-zero-parameter", engine="mpmath")
    wb.set_description(
        "Screens candidates against the (f(3), f(4)) fingerprint. The "
        "one-parameter design yields 1 hit in 10, which is EXACTLY the chance "
        "expectation (0.89) -- a free parameter reduces the test to a ~10% "
        "false-positive filter. The zero-parameter screen, where both numbers are "
        "predictions, hits 0 of 14. The misses are structured: factorial families "
        "get f(4) to within 1.7% and f(3) low by 16-18%."
    )
    ok = True

    D = ame_binding_mev(1, 2)
    T3, He3, He4 = ame_binding_mev(1, 3), ame_binding_mev(2, 3), ame_binding_mev(2, 4)
    f4 = He4 / D
    f3lo, f3hi = ((T3 + He3) / 2) / D, T3 / D
    q = mp.mpf(str(Q))

    print(f"f(4) = {mp.nstr(f4,10)}  (convention-INDEPENDENT)")
    print(f"f(3) in [{mp.nstr(f3lo,8)}, {mp.nstr(f3hi,8)}]  ({mp.nstr((f3hi-f3lo)/f3lo*100,3)}% band)\n")
    wb.add_data("fingerprint", {"f4": fmt(f4), "f3_lo": fmt(f3lo), "f3_hi": fmt(f3hi)})

    # ---- Result 1: the chance rate of the one-parameter design -----------
    preds = [mp.mpf(x) for x in ("4.426660177", "3.566459244", "3.782801274",
                                 "3.934809046", "3.101337465", "3.954896932",
                                 "3.088644307", "4.819570325", "3.57597092")]
    spread = max(preds) - min(preds)
    band = f3hi - f3lo
    rate = band / spread
    expected = len(preds) * rate
    print(f"RESULT 1  one-parameter design: 1 hit in 10")
    print(f"  predictions span {mp.nstr(spread,6)}; band {mp.nstr(band,6)}")
    print(f"  per-candidate chance {mp.nstr(rate*100,4)}%   EXPECTED hits {mp.nstr(expected,4)}   observed 1")
    print("  -> the hit is the chance expectation. A free parameter kills the test.")
    wb.add_data("one_parameter_chance_rate", {
        "n_families": len(preds), "prediction_spread": fmt(spread),
        "band_width": fmt(band), "per_candidate_chance": fmt(rate),
        "expected_hits": fmt(expected), "observed_hits": 1,
        "verdict": "hit is at chance level; not evidence",
    })
    wb.add_assertion(
        name="one_parameter_hit_is_at_chance_level",
        computed=fmt(expected), expected="1", tolerance="0.5",
        unit="expected hits under the null",
        source=("9 predictions over a range of 1.731 against a 0.172 band gives a "
                "9.9% per-candidate rate; 1 observed against 0.89 expected"),
    )
    ok &= abs(expected - 1) < mp.mpf("0.5")

    # ---- Result 2: the zero-parameter screen -----------------------------
    def qint(n):
        return sum(q ** (n - 1 - 2 * k) for k in range(n)) if n > 0 else mp.mpf(0)

    def qfact(n):
        r = mp.mpf(1)
        for k in range(1, n + 1):
            r *= qint(k)
        return r

    INV = {1: 1, 2: 2, 3: 4, 4: 10}
    zD = q ** 3 / (q ** 2 + 1)
    cands = {
        "n!": lambda n: mp.mpf(factorial(n)),
        "q_factorial": qfact,
        "qfact_times_qint": lambda n: qfact(n) * qint(n),
        "n!_times_qint": lambda n: mp.mpf(factorial(n)) * qint(n),
        "Catalan": lambda n: mp.mpf(comb(2 * n, n)) / (n + 1),
        "central_binomial": lambda n: mp.mpf(comb(2 * n, n)),
        "involutions": lambda n: mp.mpf(INV[n]),
        "n!_times_n": lambda n: mp.mpf(factorial(n)) * n,
        "n!_pow_4_3": lambda n: mp.mpf(factorial(n)) ** (mp.mpf(4) / 3),
        "n!_over_zD^n": lambda n: mp.mpf(factorial(n)) / zD ** n,
        "qfact_squared": lambda n: qfact(n) ** 2,
        "n!_times_pairs": lambda n: mp.mpf(factorial(n)) * comb(n, 2),
        "shifted_fact_2^n": lambda n: mp.mpf(factorial(n - 1)) * 2 ** n,
        "n!_times_q0^n": lambda n: mp.mpf(factorial(n)) * q ** n,
    }
    print("\nRESULT 2  zero-parameter screen -- BOTH numbers predicted\n")
    print(f"  {'candidate':<20} {'f(3)':>12} {'f(4)':>12} {'f3 err':>9} {'f4 err':>9}")
    rows, hits, best = [], 0, None
    for nm, f in cands.items():
        b = f(2)
        if b == 0:
            continue
        p3, p4 = f(3) / b, f(4) / b
        e3 = mp.mpf(0) if f3lo <= p3 <= f3hi else min(abs(p3 - f3lo), abs(p3 - f3hi)) / f3lo
        e4 = abs(p4 - f4) / f4
        h = e3 == 0 and e4 < mp.mpf("0.05")
        hits += h
        if best is None or (e3 + e4) < best[1]:
            best = (nm, e3 + e4, e3, e4)
        rows.append({"candidate": nm, "f3": fmt(p3), "f4": fmt(p4),
                     "f3_err": fmt(e3), "f4_err": fmt(e4), "hits_both": bool(h)})
        print(f"  {nm:<20} {mp.nstr(p3,7):>12} {mp.nstr(p4,7):>12} "
              f"{mp.nstr(e3*100,4):>8}% {mp.nstr(e4*100,4):>8}%")
    wb.add_data("zero_parameter_screen", rows)
    print(f"\n  hits: {hits} of {len(rows)}    closest: {best[0]} "
          f"({mp.nstr(best[2]*100,3)}% / {mp.nstr(best[3]*100,3)}%)")
    wb.add_assertion(
        name="zero_parameter_screen_finds_nothing",
        computed=str(hits), expected="0", tolerance="0",
        unit="candidates hitting both numbers",
        source="14 zero-parameter candidates; none within the f(3) band AND 5% on f(4)",
    )
    ok &= hits == 0

    wb.add_data("structured_miss", {
        "pattern": "the factorial family lands f(3) ~ 3.00-3.04 against a measured "
                   "3.64-3.81 (low by 16-18%) while [n]_q! is within 1.7% on f(4)",
        "reading": "these families get the A=4 growth roughly right and the A=3 step "
                   "badly wrong -- b3/b2 ~ 0 where the measurement wants 0.64",
        "implication": "whatever supplies b3 is not a smooth growth law",
    })
    wb.add_data("scope", {
        "derives_anything": False,
        "refutes_a_named_framework_claim": False,
        "is_an_enumeration": False,
        "sample_size": len(rows),
        "durable_content": "the fingerprint must be applied with ZERO free "
                           "parameters or it does not discriminate -- one free "
                           "parameter makes it a ~10% false-positive filter",
    })
    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
