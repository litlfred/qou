#!/usr/bin/env python3
"""nz_chain_is_the_convention_free_observable_probe.py

The N=Z chain is the observable with resolution -- but its LEADING content is
the ordinary B/A saturation, and only its residual is the extensive term.

WHY THIS EXISTS
---------------
`binding_magnitude_is_not_validatable_probe` established that the consecutive-A
cumulant tower determines every b_n to under one significant digit, because
every odd A carries a mirror-convention choice. It closed with "the live
question is which observable has resolution" and offered no candidate. This is
the candidate, and the honest assessment of it.

THE OBSERVABLE
--------------
N=Z self-conjugate nuclei have no mirror partner, so no convention choice
exists: 2H, 4He, 6Li, 8Be, 12C, 16O. The band is 0 by construction, not by
measurement, and resolution is set by AME experiment (~1e-8 relative) instead --
roughly 8 digits against the tower's <1. That is a ~10^7 improvement in the
evidence a match could carry.

THE TRAP, recorded because I nearly reported it as a finding
------------------------------------------------------------
On this chain the "excess over the pairwise wall" B/(2(A-1)B(2)) rises to 2.1199
at A=4, dips at 6Li, then saturates at 1.9123 by A=16. That looks like a
convention-free signal. It is an ALGEBRAIC REWRITE of something already known:

    B / (2(A-1) B(2))  =  (B/A) / (2 B(2))  *  A/(A-1)

so the saturation is the ordinary B/A -> ~8 MeV volume term, rescaled by twice
the deuteron binding. Verified here to 7 digits at every A. It is not new
information and must not be presented as one.

WHERE THE EXTENSIVE TERM ACTUALLY LIVES
---------------------------------------
In the residual after a smooth volume+surface background. Least squares for
B = a*A + b*A^(2/3) over A = 4..16 gives a = 11.866 MeV, b = -9.798 MeV, and:

    A= 4   +5.519 MeV   (+19.50%)
    A= 6   -6.853       (-21.42%)
    A= 8   +0.760       ( +1.35%)
    A=12   +1.120       ( +1.22%)
    A=16   -0.030       ( -0.02%)

The deviation is concentrated entirely at A=4 and A=6 and has died by A=16 --
consistent with the whole arc's picture of a light-nucleus term that saturates,
and now stated on a convention-free chain.

THE LIMITATION, which is real and must travel with the result
-------------------------------------------------------------
The N=Z chain removes the CONVENTION ambiguity but a subtracted residual
introduces a FIT-FORM ambiguity in its place: two parameters fitted on five
points, and a different background form gives different residuals. So the ~8
digits are 8 digits of a fit-dependent quantity, which is not the same as 8
digits of a prediction target.

That is not fatal, and it says exactly what is needed: the residual becomes a
genuine parameter-free target the moment the FRAMEWORK supplies the background
rather than a fit. The framework does have a volume term (the saturated
fraction, qou-brng). So the constructive next step is to subtract the
framework's own background instead of a least-squares one -- at which point the
A=4 and A=6 residuals are convention-free, AME-precise, zero-parameter targets.

SCOPE
-----
Scope-(a). Derives nothing, refutes nothing, proposes no mechanism, and wires
nothing. It identifies an observable and prices it honestly, including the part
of it that is not new.

NO FLOAT64: mpmath end to end at 65 dps; AME from the vendored table.
"""

import sys
from pathlib import Path

_R = Path(__file__).resolve().parents[1]
for _p in (str(_R), str(_R / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from substrate.codata_constants import ame_binding_mev as B  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 65

CHAIN = [(1, 2), (2, 4), (3, 6), (4, 8), (6, 12), (8, 16)]


def fmt(x):
    return mp.nstr(mp.mpf(x), 30)


def main():
    wb = WitnessBuilder("nz-chain-convention-free-observable", engine="mpmath")
    wb.set_description(
        "The N=Z self-conjugate chain (2H,4He,6Li,8Be,12C,16O) has no mirror "
        "partner and hence no convention choice, giving ~8 digits against the "
        "consecutive-A cumulant tower's <1. But its leading content is an "
        "algebraic rewrite of the ordinary B/A saturation, NOT new information; "
        "the extensive term lives only in the residual after a volume+surface "
        "background, concentrated at A=4 (+19.5%) and A=6 (-21.4%) and dead by "
        "A=16 (-0.02%). The residual is fit-form dependent, so it becomes a "
        "zero-parameter target only once the framework supplies the background "
        "instead of least squares. Scope-(a)."
    )

    D = B(1, 2)
    ok = True

    # --- the trap: the wall excess is B/A rescaled -------------------------
    print("wall excess vs (B/A)/(2B(2)) * A/(A-1)  -- testing for an identity")
    worst = mp.mpf(0)
    rows = []
    for Z, A in CHAIN:
        v = B(Z, A)
        exc = v / (2 * (A - 1) * D)
        alt = (v / A) / (2 * D) * mp.mpf(A) / (A - 1)
        rel = abs(exc - alt) / exc
        worst = max(worst, rel)
        rows.append((A, exc))
        print(f"   A={A:2d}  excess={mp.nstr(exc,9):>11s}  rewrite={mp.nstr(alt,9):>11s}"
              f"  rel diff {mp.nstr(rel,3)}")
    wb.add_data("wall_excess_by_A", {str(A): fmt(e) for A, e in rows})
    wb.add_assertion(
        name="wall_excess_is_an_algebraic_rewrite_of_B_over_A",
        computed=fmt(worst), expected="0", tolerance="1e-50",
        unit="worst relative difference over the chain",
        source=("B/(2(A-1)B(2)) == (B/A)/(2B(2)) * A/(A-1) identically, so the "
                "1.9123 saturation is the ordinary volume term rescaled and is "
                "NOT new information"))
    if worst > mp.mpf("1e-50"):
        ok = False
        print("   FAIL: not an identity")

    # --- where the term actually lives: the residual -----------------------
    fit = [(A, B(Z, A)) for Z, A in CHAIN if A >= 4]
    S11 = sum(mp.mpf(A) ** 2 for A, _ in fit)
    S12 = sum(mp.mpf(A) ** (mp.mpf(5) / 3) for A, _ in fit)
    S22 = sum(mp.mpf(A) ** (mp.mpf(4) / 3) for A, _ in fit)
    T1 = sum(A * v for A, v in fit)
    T2 = sum(mp.mpf(A) ** (mp.mpf(2) / 3) * v for A, v in fit)
    det = S11 * S22 - S12 * S12
    a = (T1 * S22 - T2 * S12) / det
    b = (S11 * T2 - S12 * T1) / det
    print(f"\nvolume a = {mp.nstr(a,9)} MeV   surface b = {mp.nstr(b,9)} MeV")

    resid = {}
    for A, v in fit:
        pred = a * A + b * mp.mpf(A) ** (mp.mpf(2) / 3)
        resid[A] = (v - pred, (v - pred) / v)
        print(f"   A={A:2d}  resid {mp.nstr(v-pred,7):>11s} MeV "
              f"({mp.nstr((v-pred)/v*100,4)} %)")
    wb.add_data("volume_surface_fit", {"a_MeV": fmt(a), "b_MeV": fmt(b),
                                       "form": "B = a*A + b*A^(2/3), 2 params on 5 points"})
    wb.add_data("residuals", {str(A): {"MeV": fmt(r), "fraction": fmt(f)}
                              for A, (r, f) in resid.items()})

    # the structure: large at A=4,6; dead by A=16
    wb.add_assertion(
        name="deviation_is_concentrated_at_A4_and_A6",
        computed=fmt(min(abs(resid[4][1]), abs(resid[6][1])) /
                     max(abs(resid[16][1]), mp.mpf("1e-30"))),
        expected="800", tolerance="200",
        unit="ratio of the smaller light anomaly to the A=16 residual",
        source=("A=4 +19.50%, A=6 -21.42%, A=8 +1.35%, A=12 +1.22%, "
                "A=16 -0.02%: a light-nucleus term that has saturated by 16"))
    r = min(abs(resid[4][1]), abs(resid[6][1])) / max(abs(resid[16][1]), mp.mpf("1e-30"))
    if abs(r - 800) > 200:
        ok = False
        print(f"   FAIL: concentration ratio {mp.nstr(r,6)} outside 800+-200")

    wb.add_data("limitation", {
        "convention_ambiguity": "removed -- N=Z has no mirror partner",
        "fit_form_ambiguity": ("introduced -- 2 params on 5 points; a different "
                               "background form gives different residuals, so "
                               "the ~8 digits are of a fit-dependent quantity"),
        "what_would_fix_it": ("subtract the FRAMEWORK's own volume background "
                              "(qou-brng saturated fraction) instead of least "
                              "squares; the A=4 and A=6 residuals then become "
                              "convention-free, AME-precise, zero-parameter "
                              "targets"),
    })

    print("\n" + ("  OK" if ok else "  FAILURES"))
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
