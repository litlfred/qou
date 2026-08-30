#!/usr/bin/env python3
"""saturated_fraction_is_not_monotonic_probe.py

Two results, both negative, both cheap, and the second corrects the corpus.

1. THE FRAMEWORK'S VOLUME TERM IS NOT A USABLE BACKGROUND (my own proposal,
   tested and withdrawn one turn after making it).

   `nz_chain_is_the_convention_free_observable_probe` closed by recommending:
   subtract the FRAMEWORK's volume background (qou-brng's saturated fraction,
   B_vol = A * m_N * hbar_q^2, zero parameters) from the N=Z chain instead of a
   least-squares one, so the A=4 and A=6 residuals become convention-free AND
   parameter-free.

   Measured, that does not work. The residuals are

       A= 2   -728.1 %      A= 8   -30.4 %
       A= 4    -30.2 %      A=12   -19.9 %
       A= 6    -72.7 %      A=16   -15.5 %

   against light-nucleus anomalies of +19.5 % / -21.4 %. The saturated fraction
   is still climbing across this whole range (0.12 -> 0.87), so the residual is
   dominated by the unsaturated approach to hbar_q^2, not by the term of
   interest. A pure volume background needs a derived SURFACE partner before it
   can isolate anything, and the framework does not supply one here.

2. "RISES MONOTONICALLY" IS FALSE AT THE LIGHT END -- a correction to
   bean qou-brng.

   qou-brng states: "the fraction rises monotonically toward hbar_q^2 with A
   (2H 0.12*hbar_q^2 -> 4He 0.77 -> 40Ca 0.93 -> 56Fe 0.95*hbar_q^2)". The bean
   already corrects the HIGH end further down (it peaks at 0.954 at 62Ni and
   falls to 0.82 at 238U). The LOW end has not been checked, and it fails too:

       A= 2  0.1207534
       A= 4  0.7679696   <- local max
       A= 6  0.5788970   <- DIP, 24.6% below 4He
       A= 8  0.7667233   <- still below 4He (8Be is unbound to 2 alpha)
       A=12  0.8337840
       A=16  0.8659256

   The quoted four-point sequence is monotonic only because it steps from A=4
   straight to A=40, skipping the dip. Measured on the N=Z chain, the fraction
   is NOT monotonic in A: it is non-monotonic at BOTH ends, and the true shape
   is rise -> local max at 4He -> dip through 6Li/8Be -> rise -> peak at 62Ni ->
   fall.

   This does not touch the bean's verdict, which is already that the exact
   hbar_q^2 saturation value is "more likely numerology than a derived
   prediction". It removes a stated empirical regularity that a future
   derivation might otherwise try to reproduce.

SCOPE
-----
Scope-(a) throughout. Nothing is refuted, no mechanism is excluded, nothing is
wired. Result 1 withdraws a recommendation I made; result 2 corrects a
descriptive claim in a bean.

NO FLOAT64: mpmath 65 dps; AME from the vendored table; q0 via Q_MP.
"""

import sys
from pathlib import Path

_R = Path(__file__).resolve().parents[1]
for _p in (str(_R), str(_R / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

import canonical_mass as cm  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from substrate.codata_constants import ame_binding_mev as B  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 65

CHAIN = [(1, 2), (2, 4), (3, 6), (4, 8), (6, 12), (8, 16)]


def fmt(x):
    return mp.nstr(mp.mpf(x), 30)


def main():
    wb = WitnessBuilder("saturated-fraction-is-not-monotonic", engine="mpmath")
    wb.set_description(
        "Two negatives. (1) Subtracting the framework's zero-parameter volume "
        "background A*m_N*hbar_q^2 from the N=Z chain does NOT isolate the "
        "light-nucleus term -- residuals run -15% to -728% against anomalies of "
        "~20%, because the saturated fraction is still climbing; this withdraws "
        "a recommendation I made one turn earlier. (2) qou-brng's 'the fraction "
        "rises monotonically toward hbar_q^2' is FALSE at the light end: it "
        "peaks at 4He (0.768), DIPS to 0.579 at 6Li and is still below 4He at "
        "8Be (0.767). The bean's four-point sequence is monotonic only because "
        "it skips A=6 and A=8. Scope-(a)."
    )

    q = +Q_MP
    h2 = (1 - 1 / q) ** 2
    mN = cm.proton_mass_mev()
    ok = True

    print(f"q0 = {mp.nstr(q,12)}   hbar_q^2 = {mp.nstr(h2,12)}   m_N = {mp.nstr(mN,10)} MeV\n")
    print(f"{'A':>3s}{'B_AME':>12s}{'B_vol':>12s}{'resid %':>11s}{'fraction':>12s}")
    rows = {}
    for Z, A in CHAIN:
        v = B(Z, A)
        vol = A * mN * h2
        frac = v / vol
        rows[A] = (v, vol, (v - vol) / v, frac)
        print(f"{A:>3d}{mp.nstr(v,8):>12s}{mp.nstr(vol,8):>12s}"
              f"{mp.nstr((v-vol)/v*100,5):>11s}{mp.nstr(frac,7):>12s}")

    wb.add_data("volume_background_test", {
        str(A): {"B_AME": fmt(v), "B_vol": fmt(vol), "resid_fraction": fmt(r),
                 "saturated_fraction": fmt(f)}
        for A, (v, vol, r, f) in rows.items()})

    # 1. the volume background is not usable: worst residual dwarfs the anomaly
    worst = max(abs(rows[A][2]) for A in rows)
    wb.add_assertion(
        name="framework_volume_alone_does_not_isolate_the_light_term",
        computed=fmt(worst), expected="7.281", tolerance="0.01",
        unit="worst |residual| as a fraction of B",
        source=("A=2 residual is -728% against light-nucleus anomalies of ~20%; "
                "the saturated fraction is still climbing over this range so "
                "the residual is the unsaturated approach, not the term"))
    if abs(worst - mp.mpf("7.281")) > mp.mpf("0.01"):
        ok = False
        print("   FAIL: worst residual moved")

    # 2. monotonicity fails at the light end
    fr = [(A, rows[A][3]) for A, _ in [(a, None) for a in sorted(rows)]]
    dips = [(fr[i - 1][0], fr[i][0]) for i in range(1, len(fr))
            if fr[i][1] < fr[i - 1][1]]
    print(f"\nfraction decreases at: {dips}")
    wb.add_data("monotonicity", {
        "sequence": {str(A): fmt(f) for A, f in fr},
        "decreasing_steps": str(dips),
        "bean_claim": ("qou-brng: 'rises monotonically toward hbar_q^2 with A "
                       "(2H 0.12 -> 4He 0.77 -> 40Ca 0.93 -> 56Fe 0.95)' -- "
                       "monotonic only because it skips A=6 and A=8"),
    })
    wb.add_assertion(
        name="saturated_fraction_is_not_monotonic_at_the_light_end",
        computed=str(len(dips)), expected="1", tolerance="0",
        unit="decreasing steps in the N=Z chain",
        source="4He 0.7680 -> 6Li 0.5789 is a 24.6% dip; 8Be 0.7667 is still below 4He")
    if len(dips) != 1:
        ok = False
        print(f"   FAIL: expected 1 decreasing step, got {len(dips)}: {dips}")

    below4 = [A for A, f in fr if A > 4 and f < rows[4][3]]
    print(f"still below the 4He fraction at A = {below4}")
    wb.add_assertion(
        name="two_nuclides_sit_below_the_4He_fraction",
        computed=str(len(below4)), expected="2", tolerance="0",
        unit="N=Z nuclides with A>4 below the 4He saturated fraction",
        source="6Li 0.5789 and 8Be 0.7667 against 4He 0.7680")
    if len(below4) != 2:
        ok = False
        print(f"   FAIL: expected 2, got {len(below4)}")

    print("\n" + ("  OK" if ok else "  FAILURES"))
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
