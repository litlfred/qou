#!/usr/bin/env python3
"""pairing_delta_overdetermination_probe.py

delta is OVER-DETERMINED, and the two determinations disagree by 25-40x.

WHY THIS IS THE RIGHT WAY TO "DERIVE delta"
--------------------------------------------
fingerprint_screen_zero_parameter established that closed-form guessing is
entropically dead at this precision: with 1-2 significant digits available, a
family with k integer parameters of height H supplies ~(2H)^k candidates and is
evidence only when (2H)^k << 10^d. So hunting a formula that yields the right
delta is BANNED by the arc's own discipline.

The legitimate move is OVER-DETERMINATION: delta is fixed by the A<=4 cumulants,
and is INDEPENDENTLY measurable as the odd-even staggering of the binding curve.
If the two agree, delta is over-determined rather than fitted. If they disagree,
the pairing route is refuted quantitatively. No formula is proposed either way.

DETERMINATION 1 -- from the A<=4 cumulants
-------------------------------------------
Fitting smooth (C(2n,n)) + pairing to b3 and b4:

    raw isospin-averaged   delta = 0.58901076 MeV  -> pairing energy at A=2  0.208 MeV
    Coulomb-corrected      delta = 0.95593837 MeV  -> pairing energy at A=2  0.338 MeV

DETERMINATION 2 -- from the odd-even staggering
------------------------------------------------
3-point neutron gap D3(N) = (-1)^N/2 [B(A-1) - 2B(A) + B(A+1)] at fixed Z, over
the 51 usable triples with A >= 8:

    median |D3| = 1.80355 MeV   -- consistent with the standard 1-3 MeV light-nucleus gap

and the standard SEMF pairing energy at A = 2 (a_P = 12 MeV / sqrt(A)) is
8.48528 MeV.

THE DISAGREEMENT
----------------
    fitted at A=2   0.208 - 0.338 MeV
    physical at A=2 8.485 MeV
    ratio           25x - 41x

**The exponent cannot rescue it.** Pairing DECREASES with A, so a term giving
0.2-0.34 MeV at A=2 cannot reach ~1.8 MeV at A~10 for any positive exponent --
it is smallest exactly where pairing is largest. The discrepancy is in the
STRENGTH, not the mass dependence.

A MEASUREMENT ARTIFACT I HAD TO REMOVE, recorded because it nearly went in
--------------------------------------------------------------------------
Taking the median of |D3| * A^1.5 over ALL A gives an "implied delta" of 88 MeV
and a 92-150x ratio. That number is CONTAMINATED: the low-A entries (A=4 -> 85,
A=5 -> 90, A=6 -> 119) are SHELL-CLOSURE jumps, not pairing, and they dominate
the median. Restricting to A >= 8 and comparing pairing ENERGIES rather than a
rescaled coefficient gives the honest 25-40x. The headline ratio changed by ~4x
when the artifact was removed.

An earlier pass also printed no staggering rows at all, from a sign filter of
mine (`if d3 > 0`) that dropped every entry. Recorded so the absence is not later
read as an absence of signal.

VERDICT
-------
**The sign result stands and is untouched** -- pairing forces b3 > 0 from the
parities alone, for every delta, and that argument never uses delta's value
(PairingParityForcesPositiveB3).

**The magnitude route is refuted.** The pairing term that reproduces b3 and b4 is
25-40x too weak to be the physical nuclear pairing force, so pairing cannot be
the quantitative explanation of b3. Either the term is not really pairing, or
pairing supplies only a small part of b3 and something else supplies the rest.

Scope (a): refutes pairing as the SOLE quantitative mechanism. Does not exclude
it from a multi-term closure -- and its derived sign remains the only such result
in the arc.

Bean qou-edt7.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys  # noqa: E402
from math import comb  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(65)
P = {2: -mp.mpf(1) / mp.mpf(2) ** mp.mpf(1.5), 3: mp.mpf(0), 4: mp.mpf(1) / 8}


def main() -> int:
    wb = WitnessBuilder("pairing-delta-overdetermination", engine="mpmath")
    wb.set_description(
        "delta is over-determined: fixed by the A<=4 cumulants AND independently "
        "measurable as the odd-even staggering. The two disagree by 25-40x at "
        "A=2 (fitted 0.21-0.34 MeV vs SEMF 8.49 MeV), and no exponent rescues it "
        "since pairing is largest where the fitted term is smallest. Refutes "
        "pairing as the SOLE quantitative mechanism; the derived SIGN is untouched."
    )
    ok = True

    D = ame_binding_mev(1, 2)
    T3, He3, He4 = ame_binding_mev(1, 3), ame_binding_mev(2, 3), ame_binding_mev(2, 4)
    cb = (lambda n: mp.mpf(comb(2 * n, n)))

    # ---- determination 1 -------------------------------------------------
    print("DETERMINATION 1 -- delta from the A<=4 cumulants\n")
    fits = {}
    for cn, (b2t, B3, B4) in (("raw_isospin_average", (D, (T3 + He3) / 2, He4)),
                              ("coulomb_corrected", (D, T3, He4 + mp.mpf("0.70")))):
        b3, b4 = B3 - 3 * b2t, B4 - 4 * B3 + 6 * b2t
        s3, p3 = cb(3) - 3 * cb(2), P[3] - 3 * P[2]
        s4, p4 = cb(4) - 4 * cb(3) + 6 * cb(2), P[4] - 4 * P[3] + 6 * P[2]
        d = (s3 * b4 - b3 * s4) / (s3 * p4 - p3 * s4)
        e2 = d / mp.mpf(2) ** mp.mpf(1.5)
        fits[cn] = (d, e2)
        print(f"  {cn:<22} delta = {mp.nstr(d,8):>10} MeV   pairing at A=2 = "
              f"{mp.nstr(e2,6)} MeV")
    wb.add_data("determination_1_cumulants",
                {k: {"delta": fmt(v[0]), "energy_at_A2": fmt(v[1])} for k, v in fits.items()})

    # ---- determination 2 -------------------------------------------------
    print("\nDETERMINATION 2 -- delta from the odd-even staggering (A >= 8)\n")
    vals = []
    for Z in range(2, 9):
        for A in range(max(Z + 2, 8), 19):
            try:
                bm, b0, bp = ame_binding_mev(Z, A - 1), ame_binding_mev(Z, A), ame_binding_mev(Z, A + 1)
            except Exception:
                continue
            if not (bm and b0 and bp):
                continue
            vals.append(abs((bm - 2 * b0 + bp) / 2))
    med = sorted(vals)[len(vals) // 2]
    semf2 = mp.mpf(12) / mp.sqrt(2)
    print(f"  n = {len(vals)} triples,  median |D3| = {mp.nstr(med,6)} MeV")
    print(f"  (standard light-nucleus gap 1-3 MeV -- consistent)")
    print(f"  SEMF pairing at A=2, a_P = 12/sqrt(A):  {mp.nstr(semf2,6)} MeV")
    wb.add_data("determination_2_staggering", {
        "n_triples": len(vals), "median_abs_D3": fmt(med),
        "semf_energy_at_A2": fmt(semf2),
        "restricted_to": "A >= 8, to exclude shell-closure jumps",
    })

    # ---- the disagreement -------------------------------------------------
    print("\nTHE DISAGREEMENT\n")
    ratios = {}
    for cn, (d, e2) in fits.items():
        r = semf2 / e2
        ratios[cn] = r
        print(f"  {cn:<22} fitted {mp.nstr(e2,6):>9} MeV  vs physical "
              f"{mp.nstr(semf2,6)} MeV   -> {mp.nstr(r,5)}x too small")
    worst = min(ratios.values())
    wb.add_data("disagreement", {k: fmt(v) for k, v in ratios.items()})
    wb.add_assertion(
        name="fitted_pairing_is_far_too_weak",
        computed=fmt(worst), expected="25", tolerance="20",
        unit="ratio physical/fitted pairing energy at A=2",
        source=("fitted 0.208-0.338 MeV against the SEMF 8.485 MeV; no positive "
                "exponent rescues it, since pairing is largest at small A where "
                "the fitted term is smallest"),
    )
    ok &= worst > mp.mpf("10")

    wb.add_data("measurement_artifact_removed", {
        "contaminated_figure": "median of |D3| * A^1.5 over ALL A gives 88 MeV and "
                               "a 92-150x ratio",
        "why_wrong": "the low-A entries (A=4 -> 85, A=5 -> 90, A=6 -> 119) are "
                     "SHELL-CLOSURE jumps, not pairing, and dominate the median",
        "corrected_to": "restrict to A >= 8 and compare pairing ENERGIES; 25-40x",
        "headline_moved_by": "~4x when the artifact was removed",
        "earlier_slip": "a first pass printed NO staggering rows at all, from a "
                        "sign filter (if d3 > 0) of mine that dropped every entry; "
                        "recorded so the absence is not read as absence of signal",
    })
    wb.add_data("verdict", {
        "sign_result_untouched": True,
        "sign_why": "pairing forces b3 > 0 from the parities for EVERY delta; that "
                    "argument never uses delta's value",
        "magnitude_route_refuted": True,
        "magnitude_why": "the pairing term reproducing b3 and b4 is 25-40x too weak "
                         "to be the physical nuclear pairing force",
        "scope": "(a) -- refutes pairing as the SOLE quantitative mechanism, not "
                 "its presence in a multi-term closure",
        "delta_derived": False,
    })
    wb.save()
    print("\nOK" if ok else "\nFAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
