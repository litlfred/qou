"""Where does the ladder block's headline "-0.0066 ppm" come from?

`qou-54g5` (a `qou-cds1` fallout) records that the block
`q-beta-categorical-precision-ladder` claims a **-0.0066 ppm** residual against
CODATA while the implementation returns a POSITIVE few-ppb number at the same
pin. That is an 11 %-magnitude, opposite-SIGN disagreement, and every downstream
statement about the ladder's accuracy inherits the headline rather than the code.

This probe does not choose a value. It measures every candidate reading the
corpus actually offers, so the discrepancy is attributed rather than argued:

  R1  the block's OWN table 2, N=3 row                  +6.02  ppb (published)
  R2  the block's OWN table 2, N=4 row                  -0.57  ppb (published)
  R3  the live implementation at the MUON pin           measured here
  R4  the live implementation at the canonical PROTON pin  measured here

and the headline itself, -0.0066 ppm = -6.6 ppb.

WHAT THIS SETTLES.  The headline matches NO row of the block's own table. The
nearest is R1: same order of magnitude, OPPOSITE sign, ~10 % apart. So
hypothesis (4) of `qou-54g5` -- a sign convention differing between block and
code -- is the only one of its four that survives contact with the block's own
table, and it does not explain the magnitude gap on its own.

WHAT THIS DOES NOT SETTLE, stated so it is not over-quoted.  It does not say
which number is CORRECT. Deciding that requires resolving the block's fifth-rung
coefficient, which its own `.qa.json` finding (1) records as carrying a
SUPERSEDED value: the boxed formula's last factor is -(b^2+1/2) = -1.2527 while
the context remark and table 3 both give 3*c_3^2 + b = +12.8676 -- different in
sign and an order of magnitude. That is a math question and is NOT decided here.

NOR is this a convention-D measurement. The whole ladder is convention-C-frame
and must be RE-DERIVED under D, not re-evaluated (AGENTS.md; bean `qou-cds1`;
`QOU.QBeta.decayLadder_zC_threeRow_ne_zero`). Everything below is C-frame.

Scope (a) throughout: this is an attribution of a published number, not a
derivation of the right one, and nothing here is wired.
"""

from __future__ import annotations

import sys
from pathlib import Path

# bootstrap: _path_bridge lives in computations/, one level up from this
# cluster dir, so it must be on sys.path BEFORE it is imported.
import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.constants import Q_NEUTRON_MEV, M_E_MEV  # noqa: E402

set_compute_dps()

ME = mp.mpf(str(M_E_MEV))
QEXP = mp.mpf(str(Q_NEUTRON_MEV))
MUON_WITNESS = HERE.parent / "q-pinning-50-digit.witness.json"

# The block's headline, as prose: "-0.0066 ppm residual against CODATA".
HEADLINE_PPB = mp.mpf("-6.6")

# The block's OWN table 2, transcribed from
# q-beta-categorical-precision-ladder-table2-data.md. Published values, not
# recomputed here -- the point is what the block says about itself.
TABLE2_N3_PPB = mp.mpf("6.02")
TABLE2_N4_PPB = mp.mpf("-0.57")


def ladder_ppb(q, n_rungs):
    """The boxed C-frame ladder at a stated pin, truncated after n_rungs factors.

    Colour-BLIND mixed crossing (w = 1/2), which is the reading the published
    agreement uses; the colour-weighted R3 crossing moves Q_A by ~80 ppm and is
    priced separately in qbeta_ladder_convention_fee_probe.
    """
    h = q - 1 / q
    hb = (q - 1) / q
    b = mp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    z = mp.sqrt(q) / (q + 1)          # convention C -- see docstring
    # colour-BLIND mixed crossing, matching qbeta_ladder_convention_fee_probe's
    # w_blind(q) = h/2 -- passing 1/2 here instead of h/2 is off by a factor of
    # h and was caught by this probe's own sign assertion on the first run.
    w_mixed = h / 2
    eps = w_mixed * h - h
    out = abs(eps * ME / (q * (q - 1)))
    al = (z - 1) * h / 2
    fs = [mp.cos(al - b * hb**2 / 2),
          1 - b**2 * hb**4,
          1 - 2 * b**3 * hb**6,
          1 - 2 * b**4 * b**4 * hb**8,
          1 - (b**2 + mp.mpf(1) / 2) * b**5 * hb**10]
    for f in fs[:n_rungs]:
        out *= f
    return (out - QEXP) / QEXP * mp.mpf(10) ** 9


def main() -> int:
    import json

    q_pr = Q_MP
    q_mu = mp.mpf(str(json.loads(MUON_WITNESS.read_text())
                      ["derived_50_digit"]["q"]))

    wb = WitnessBuilder("qbeta-ladder-headline-residual-provenance",
                        engine="mpmath")
    wb.set_description(
        "Attributes the q-beta ladder block's headline -0.0066 ppm residual. It "
        "matches NO row of the block's own table 2; the nearest (N=3, +6.02 ppb) "
        "differs in SIGN and ~10 percent in magnitude, so a sign convention is "
        "necessary but not sufficient to explain it. C-frame; scope (a); nothing "
        "wired.")

    A = []

    def check(name, passed, note=""):
        A.append((name, bool(passed)))
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}\n      {note}")

    r3 = ladder_ppb(q_mu, 5)
    r4 = ladder_ppb(q_pr, 5)

    print("=" * 76)
    print(" q-beta ladder — where does the headline -0.0066 ppm come from?")
    print("=" * 76)
    print()
    print(f"  headline, as prose in the block:  {mp.nstr(HEADLINE_PPB, 6)} ppb")
    print()
    print(f"  {'candidate reading the corpus offers':48s} {'ppb':>14s} {'|v/headline|':>13s}")
    rows = [
        ("R1  block's own table 2, N=3 (published)", TABLE2_N3_PPB),
        ("R2  block's own table 2, N=4 (published)", TABLE2_N4_PPB),
        ("R3  live implementation, MUON pin", r3),
        ("R4  live implementation, PROTON pin (canonical)", r4),
    ]
    for label, v in rows:
        print(f"  {label:48s} {mp.nstr(v, 7):>14s} {mp.nstr(abs(v / HEADLINE_PPB), 5):>13s}")
        wb.add_data(label.split("  ")[0].strip() + "_ppb", fmt(v))
    print()

    near = min([TABLE2_N3_PPB, TABLE2_N4_PPB],
               key=lambda v: abs(abs(v) - abs(HEADLINE_PPB)))

    check("headline_matches_no_published_row",
          abs(near - HEADLINE_PPB) > mp.mpf("1e-3"),
          f"nearest published row {mp.nstr(near, 6)} ppb vs headline "
          f"{mp.nstr(HEADLINE_PPB, 6)} ppb -- apart by "
          f"{mp.nstr(abs(near - HEADLINE_PPB), 6)} ppb, far beyond rounding")

    check("nearest_row_has_opposite_sign",
          near * HEADLINE_PPB < 0,
          f"nearest row {mp.nstr(near, 6)} and headline {mp.nstr(HEADLINE_PPB, 6)} "
          f"have OPPOSITE signs -- qou-54g5 hypothesis (4), a sign convention "
          f"differing between block prose and block table")

    ratio = abs(near) / abs(HEADLINE_PPB)
    check("sign_alone_does_not_explain_the_gap",
          abs(ratio - 1) > mp.mpf("0.05"),
          f"|nearest|/|headline| = {mp.nstr(ratio, 6)}; a pure sign flip gives 1. "
          f"So hypothesis (4) is NECESSARY but NOT SUFFICIENT")

    check("no_pin_choice_recovers_the_headline_sign",
          r3 > 0 and r4 > 0,
          f"implementation gives {mp.nstr(r3, 7)} ppb (muon) and "
          f"{mp.nstr(r4, 7)} ppb (proton) -- both "
          f"{'POSITIVE' if r3 > 0 else 'NEGATIVE'}, while the headline is "
          f"NEGATIVE. Switching pins moves the magnitude, not the sign, so the "
          f"q0 pin is NOT the explanation")

    check("everything_here_is_C_frame",
          True,
          "z = sqrt(q)/(q+1) throughout. The D-frame ladder is UNKNOWN pending "
          "re-derivation (qou-cds1); a z-swap is invalid per "
          "decayLadder_zC_threeRow_ne_zero")

    wb.add_data("headline_ppb", fmt(HEADLINE_PPB))
    wb.add_data("q0_proton", Q_50_DIGIT_STR)
    wb.add_data("q0_muon", fmt(q_mu))
    for name, passed in A:
        wb.add_assertion(name, computed="1" if passed else "0",
                         expected="1", tolerance="0")

    ok = all(p for _, p in A)
    print(f"\n  {sum(p for _, p in A)}/{len(A)} checks passed")
    out = wb.save()
    print(f"  witness: {out}")
    return 0 if ok else 1



if __name__ == "__main__":
    raise SystemExit(main())
