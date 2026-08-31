#!/usr/bin/env python3
"""Which c_5 does the ladder use -- and which does the block's own prose say?

Bean `qou-54g5`.  The bean's remaining open item was recorded as a MATH
question: "which fifth-rung coefficient is right, boxed -(b^2+1/2) = -1.2527 or
context/table-3 3c_3^2+b = +12.8676, opposite sign and an order of magnitude
apart."

It is not a math question.  It is an INDEX SLIP, and the corpus already says so
in its own words.  `q-beta-categorical-precision-ladder-context.md:29`:

    "The earlier c_4 = b^2 + 1/2 form is superseded: it is 9.5% off the
     empirical value, while c_3 * b^4 matches to 0.9%."

`b^2 + 1/2` is the retired **c_4**.  The boxed formula carries it at **rung 5**.
Site-by-site:

    site                                     c_4            c_5
    boxed formula (the .md)                  c_3*b^4  OK    b^2+1/2   <- retired c_4
    ladder() in qbeta_ladder_convention_fee  c_3*b^4  OK    b^2+1/2   <- retired c_4
    context, "mixing pattern across rungs"   c_3*b^4  OK    3c_3^2+b
    table-3 N=5 row                          --             3c_3^2+b

So the supersession updated rung 4 in the box and DISPLACED the retired
expression into the rung-5 slot rather than deleting it.  Two sites carry an
expression their own prose calls superseded; three sites agree on the other.

This file measures what that costs.  Everything here is CONVENTION C, the frame
the block was written in; the D-frame ladder does not exist (qou-cds1).

Exact mpmath at 50 dps; no float64; no mpf(str(<f64>)) of an f64 constant.
Emits no witness -- it audits published text against published code.
"""
import json
import pathlib
import sys

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

mp.mp.dps = 50

from qou_substrate.constants import M_E_MEV, Q_NEUTRON_MEV, q_at  # noqa: E402

ME = mp.mpf(str(M_E_MEV))
QEXP = mp.mpf(str(Q_NEUTRON_MEV))
MUON_WITNESS = HERE.parent / "q-pinning-50-digit.witness.json"


def zC(q):
    """Convention C, the frame the published ladder is locked to."""
    return mp.sqrt(q) / (q + 1)


def w_blind(q):
    """Colour-blind mixed crossing -- the published choice.

    Verbatim from `qbeta_ladder_convention_fee_probe.main`, NOT re-derived:
    an earlier draft of this file guessed `0` here and produced an 11.7 %
    residual, ~70x worse than the block's own 'Form A bare' row.  A wrong
    baseline makes every downstream comparison measure the baseline.
    """
    return (q - 1 / q) / 2


def ladder(q, c5_form, n_rungs=5):
    """The published five-rung ladder with a SELECTABLE c_5 expression.

    Identical to `qbeta_ladder_convention_fee_probe.ladder` except that the
    fifth rung's coefficient is a parameter, so the two candidate forms can be
    compared against the same four leading rungs.
    """
    h = q - 1 / q
    hb = (q - 1) / q
    b = mp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    z = zC(q)
    eps = w_blind(q) * h - h
    QA = abs(eps * ME / (q * (q - 1)))
    al = (z - 1) * h / 2

    c3 = mp.mpf(-2)                       # Hopf Jones at q=1
    if c5_form == "boxed":                # -(b^2 + 1/2): the RETIRED c_4 form
        rung5 = 1 - (b**2 + mp.mpf(1) / 2) * b**5 * hb**10
    elif c5_form == "context":            # 3*c_3^2 + b, per context + table 3
        rung5 = 1 - (3 * c3**2 + b) * b**5 * hb**10
    else:
        raise ValueError(c5_form)

    fs = [mp.cos(al - b * hb**2 / 2),
          1 - b**2 * hb**4,
          1 - 2 * b**3 * hb**6,
          1 - 2 * b**4 * b**4 * hb**8,
          rung5]
    out = QA
    for f in fs[:n_rungs]:
        out *= f
    return out


def ppb(v):
    return (v - QEXP) / QEXP * mp.mpf(10) ** 9


def main() -> int:
    checks = []

    q_pr = q_at(50)
    q_mu = mp.mpf(str(json.loads(MUON_WITNESS.read_text())
                      ["derived_50_digit"]["q"]))

    b_pr = mp.sqrt(q_pr**4 + q_pr**2 + 1) / (q_pr**2 + 1)
    c5_boxed = -(b_pr**2 + mp.mpf(1) / 2)
    c5_ctx = -(3 * mp.mpf(-2) ** 2 + b_pr)

    print("Convention C (the block's own frame).  mpmath, 50 dps.\n")
    print(f"  b(proton pin)  = {mp.nstr(b_pr, 12)}")
    print(f"  boxed  c_5 = -(b^2 + 1/2)  = {mp.nstr(c5_boxed, 10)}")
    print(f"  context c_5 = -(3c_3^2 + b) = {mp.nstr(c5_ctx, 10)}")
    print(f"  ratio                       = {mp.nstr(c5_ctx / c5_boxed, 8)}\n")

    # 1. The two candidates are the SAME SIGN, not opposite.  The bean recorded
    #    them as "opposite sign"; that came from comparing -(b^2+1/2) against a
    #    bare +(3c_3^2+b), i.e. one with the box's minus folded in and one
    #    without.  Both are negative coefficients of u^5.
    checks.append(("both candidate c_5 are NEGATIVE (not opposite sign)",
                   c5_boxed < 0 and c5_ctx < 0))
    checks.append(("they differ by ~10.3x in magnitude",
                   mp.mpf(10) < abs(c5_ctx / c5_boxed) < mp.mpf(11)))

    # 2. b^2 + 1/2 is numerically what the context calls the retired c_4.
    c4_retired = b_pr**2 + mp.mpf(1) / 2
    c4_live = mp.mpf(-2) * b_pr**4
    checks.append(("retired c_4 = b^2+1/2 ~ 1.2527",
                   abs(c4_retired - mp.mpf("1.2527")) < mp.mpf("0.001")))
    checks.append(("live c_4 = c_3*b^4 differs from it",
                   abs(abs(c4_live) - c4_retired) > mp.mpf("0.1")))

    # 3. What each choice does to the N=5 residual, at both pins.
    rows = []
    for label, q0 in (("proton", q_pr), ("muon", q_mu)):
        for form in ("boxed", "context"):
            rows.append((label, form, ppb(ladder(q0, form, 5))))

    print("N=5 residual vs CODATA, ppb:\n")
    print(f"  {'pin':8} {'c_5 form':10} {'residual (ppb)':>20}")
    for label, form, v in rows:
        print(f"  {label:8} {form:10} {mp.nstr(v, 8):>20}")

    d_pr = dict(((f, v) for l, f, v in rows if l == "proton"))
    d_mu = dict(((f, v) for l, f, v in rows if l == "muon"))
    print(f"\n  swap cost, proton pin: {mp.nstr(d_pr['context'] - d_pr['boxed'], 6)} ppb")
    print(f"  swap cost, muon pin:   {mp.nstr(d_mu['context'] - d_mu['boxed'], 6)} ppb")

    # 4. The swap is TINY -- u^5 is ~4.5e-11, so a 10x coefficient change moves
    #    the residual by well under a ppb.  This is the load-bearing measurement:
    #    it means the index slip does NOT explain the bean's headline discrepancy.
    swap_pr = abs(d_pr["context"] - d_pr["boxed"])
    checks.append(("the c_5 swap moves the residual by < 1 ppb",
                   swap_pr < 1))

    # 5. Neither choice reproduces table 3's published +0.04 ppb at N=5.
    for label, d in (("proton", d_pr), ("muon", d_mu)):
        for form in ("boxed", "context"):
            checks.append((f"{label} pin, {form} c_5: does NOT reproduce table-3 +0.04 ppb",
                           abs(d[form] - mp.mpf("0.04")) > 1))

    # 6. THE RESOLUTION.  The block's headline is -0.0066 ppm = -6.6 ppb, quoted
    #    to two significant figures.  With the CONTEXT c_5 at the MUON pin -- the
    #    block's own frame -- the ladder gives +6.6133 ppb, which rounds to
    #    0.0066 ppm exactly.  The bean could not see this because the live code
    #    carries the retired c_4 in the c_5 slot, which pushes N=5 to +7.1339.
    head_mag = mp.mpf("6.6")
    checks.append(("context c_5 at the muon pin reproduces the headline MAGNITUDE "
                   "to the quoted 2 s.f.",
                   abs(abs(d_mu["context"]) - head_mag) / head_mag < mp.mpf("0.005")))
    checks.append(("the BOXED c_5 does not (that is the index slip's cost)",
                   abs(abs(d_mu["boxed"]) - head_mag) / head_mag > mp.mpf("0.05")))
    checks.append(("sign still differs -- hypothesis (4) stands, unresolved here",
                   d_mu["context"] > 0))

    print("\n  RESOLUTION of the bean's open item:")
    print(f"    block headline            = -0.0066 ppm = -6.6 ppb (2 s.f.)")
    print(f"    context c_5, muon pin     = {mp.nstr(d_mu['context'], 8)} ppb"
          f"  -> {mp.nstr(d_mu['context'] / 1000, 5)} ppm")
    print(f"    magnitude agreement       = "
          f"{mp.nstr(abs(abs(d_mu['context']) - head_mag) / head_mag * 100, 3)} %")
    print(f"    boxed c_5, muon pin       = {mp.nstr(d_mu['boxed'], 8)} ppb"
          f"   <- what the live code gives")

    hb = (q_pr - 1) / q_pr
    u5 = (b_pr * hb**2) ** 5
    print(f"\n  u^5 at the proton pin = {mp.nstr(u5, 6)}  <- why the swap is sub-ppb")

    print("\n--- checks ---")
    ok = True
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok = ok and bool(passed)
    print(f"\n{sum(1 for _, p in checks if p)}/{len(checks)}")

    print("""
FINDINGS

1. The bean's remaining item is NOT a math question.  `b^2 + 1/2` is the
   SUPERSEDED c_4, named as such by the block's own context.  The boxed formula
   and `ladder()` carry it in the c_5 slot; the context's mixing pattern and
   table 3 both give `3c_3^2 + b`.  Documentation defect, two sites.

2. CORRECTION to the bean: the two candidates are NOT "opposite sign".  Both are
   negative coefficients of u^5.  The recorded opposition came from comparing
   the box's -(b^2+1/2) against a bare +(3c_3^2+b) -- one with the leading minus
   folded in, one without.  They differ by ~10.3x in MAGNITUDE only.

3. The slip is worth only -0.52 ppb (u^5 ~ 4.5e-11), but that is EXACTLY the
   size that matters here, and it RESOLVES the bean's open item:

       block headline         -0.0066 ppm  =  -6.6 ppb   (2 s.f.)
       context c_5, muon pin  +6.6133 ppb  ->  0.0066 ppm    0.20 % apart
       boxed   c_5, muon pin  +7.1339 ppb                    8.1 % apart

   The headline IS the N=5 muon-pin residual computed with the CONTEXT c_5.
   The bean could not see this because the live code carries the retired c_4 in
   the c_5 slot, so its N=5 lands at +7.13 and the nearest match to the headline
   looked like N=3 (+6.02, 8.8 % off).  Comparing to the wrong rung is what made
   the sign hypothesis look "necessary but not sufficient".

   The SIGN still differs and is NOT resolved here -- hypothesis (4) stands, now
   as a pure sign convention with no residual magnitude gap to explain.

4. NEITHER c_5 reproduces table 3's published +0.04 ppb at N=5.  Scope (a): a
   scope-limited negative about this reconstruction, NOT a claim that table 3 is
   wrong.  Table 3's column is a per-rung sequence quoted against inputs that
   predate the CODATA-2022 move the bean flagged; this file fixes the published
   colour-blind w and today's constants.  What IS established is that the c_5
   slot is not the cause of THAT gap either.

FIX: correct the c_5 slot in both carriers -- the boxed formula in
`q-beta-categorical-precision-ladder.md` and `ladder()` in
`qbeta_ladder_convention_fee_probe.py` -- from `(b^2 + 1/2)` to `(3c_3^2 + b)`.
That is a documentation/implementation correction to match the block's own
prose, not a change of claim.  Deliberately NOT done in this probe: it moves a
published number (37.707 -> 37.187 ppb at the canonical pin) and belongs in its
own commit with the witness refreshed.

NOT DONE, and not to be done by fitting: the sign, and table 3's column.  Do not
tune w, the pin, or CODATA until they come out -- that would manufacture
provenance for numbers whose origin is the actual open question.
""")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
