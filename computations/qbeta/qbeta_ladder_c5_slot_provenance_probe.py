#!/usr/bin/env python3
"""Which c_5 does the ladder use -- and which does the block's own prose say?

Bean `qou-54g5`.  The bean's remaining open item was recorded as a MATH
question: "which fifth-rung coefficient is right, boxed -(b^2+1/2) = -1.2527 or
context/table-3 3c_3^2+b = +12.8676, opposite sign and an order of magnitude
apart."

ANSWER: `-(b^2 + 1/2)` is CURRENT and `3c_3^2 + b` is SUPERSEDED, so the stale
sites are the block's HEADLINE, TABLE 3, and the context's mixing-pattern line
-- not the six carriers.  Evidence in finding 5 below.

  *** Two earlier versions of this docstring got this wrong in opposite     ***
  *** directions.  The first called `b^2+1/2` a displaced leftover and      ***
  *** counted two stale carriers against three good ones -- from a grep of  ***
  *** only the two files already open.  The second had the count right      ***
  *** (6 vs 2) but left the direction undetermined.  Both are recorded      ***
  *** because the trap is real: the corpus says, at                         ***
  *** `...-ladder-context.md:29`, "the earlier c_4 = b^2 + 1/2 form is      ***
  *** superseded", and that line reads like a complete answer while         ***
  *** describing a DIFFERENT slot's supersession.                           ***

The c_4 -> c_5 reassignment was DELIBERATE.
`q-beta-gamma-gamma-canonical-derivation.md:48` gives `b^2+1/2` at **c_4** with
the reading "Kashiwara + half-Hopf mixed"; `conj-qbeta-c-k-closed-forms.md`
gives it at **c_5** with THE SAME reading and a recorded **2.4 % empirical
residual**.  When c_4 was superseded to `c_3*b^4`, the expression moved to the
c_5 slot carrying its interpretation -- an intentional, empirically-checked
assignment, not a slip.

Site by site, c_5 only:

    -(b^2 + 1/2)                              3c_3^2 + b
    -----------------------------------       -------------------------------
    boxed formula (.md)                       context, "mixing pattern"
    ck-extraction-from-algebraic-rules.md     table-3, N=5 row
    conj-qbeta-c-k-closed-forms.md
      (+ the Lean class it formalizes)
    ladder() in qbeta_ladder_convention_fee
    ladder() in qbeta_ladder_headline_...
                                    6 sites                           2 sites

Separately, `q-beta-gamma-gamma-canonical-derivation.md` is stale on the OTHER
end: its table still publishes the retired `b^2+1/2` at **c_4**, where the
supersession replaced it.  That is a third defect, not part of the c_5 question.

The measurement below is what makes it matter: the published headline is
reproduced by the TWO-site form and missed by the SIX-site form -- which, given
the direction above, means the HEADLINE is the stale artifact.

This file measures what that costs.  Everything here is CONVENTION C, the frame
the block was written in; the D-frame ladder does not exist (qou-cds1).

Exact mpmath at 50 dps; no float64; no mpf(str(<f64>)) of an f64 constant.
Emits no witness -- it audits published text against published code.
"""
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
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
    QA = abs(_qbeta_e0.order_zero_scaled(eps * ME, q))
    al = (z - 1) * h / 2

    c3 = mp.mpf(-2)                       # Hopf Jones at q=1
    if c5_form == "boxed":                # -(b^2 + 1/2): the CURRENT c_5
        rung5 = 1 - (b**2 + mp.mpf(1) / 2) * b**5 * hb**10
    elif c5_form == "context":            # 3*c_3^2 + b: SUPERSEDED (deprecated
                                          # producer); kept to show what the
                                          # published headline was computed with
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

    # 1. AS LADDER COEFFICIENTS both are negative -- `c5_ctx` here carries the
    #    box's leading minus.  AS QUOTED IN THEIR SOURCES they are opposite:
    #    -(b^2+1/2) = -1.2527 against a bare +(3c_3^2+b) = +12.8676, which is
    #    what the bean recorded.  Both readings are right about different
    #    objects; finding 7 compares the QUOTED forms, which is the one that
    #    matters against the SDP extraction.
    checks.append(("as ladder coefficients (minus folded in) both are negative",
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

    # 7. WHICH IS RIGHT.  The live producer for the conjecture block,
    #    `qbeta/qbeta_decay_sdp_full_ck.py`, records the SDP-extracted value
    #    c_5 = -1.2229.  -(b^2+1/2) = -1.2527 is 2.4 % from it (exactly the
    #    residual the conj block publishes).  3c_3^2+b = +12.8676 is ~10x off
    #    AND the wrong sign.
    c5_extracted = mp.mpf("-1.2229")
    err_six = abs(c5_boxed - c5_extracted) / abs(c5_extracted)
    err_two = abs(-c5_ctx - c5_extracted) / abs(c5_extracted)   # as quoted, +12.87
    checks.append(("six-site -(b^2+1/2) is within 3 % of the SDP extraction",
                   err_six < mp.mpf("0.03")))
    checks.append(("two-site 3c_3^2+b is off by more than 5x",
                   err_two > 5))
    checks.append(("and has the opposite sign to the extraction",
                   (-c5_ctx) > 0 and c5_extracted < 0))

    print("\n  WHICH c_5 IS RIGHT -- against the SDP extraction:")
    print(f"    extracted (qbeta_decay_sdp_full_ck) = {mp.nstr(c5_extracted, 6)}")
    print(f"    six-site  -(b^2+1/2) = {mp.nstr(c5_boxed, 8)}"
          f"   {mp.nstr(err_six * 100, 3)} % off")
    print(f"    two-site  3c_3^2+b   = {mp.nstr(-c5_ctx, 8)}"
          f"   {mp.nstr(err_two * 100, 4)} % off, WRONG SIGN")
    print("    -> six-site form is CURRENT; two-site form is SUPERSEDED and")
    print("       lives only in _deprecated/precision-ladder-superseded/.")

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

1. The corpus is INTERNALLY INCONSISTENT about c_5, 6 sites to 2 -- and the
   published headline agrees with the 2.  It is not a documentation slip in two
   places, which is what an earlier pass of this file claimed on an incomplete
   grep.  The six-site form carries a categorical reading and a recorded 2.4 %
   empirical residual, so it is a deliberate claim, not a leftover.

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
   The bean could not see this because the live code uses the OTHER c_5, so its
   N=5 lands at +7.13 and the nearest match to the headline looked like N=3
   (+6.02, 8.8 % off).  Comparing to the wrong rung is what made the sign
   hypothesis look "necessary but not sufficient".

   This does NOT establish which c_5 is correct.  It establishes that the
   headline was computed with the minority one, while the framework's formalized
   coefficient family claims the majority one.  Those cannot both be right.

   The SIGN still differs and is NOT resolved here -- hypothesis (4) stands, now
   as a pure sign convention with no residual magnitude gap to explain.

4. NEITHER c_5 reproduces table 3's published +0.04 ppb at N=5.  Scope (a): a
   scope-limited negative about this reconstruction, NOT a claim that table 3 is
   wrong.  Table 3's column is a per-rung sequence quoted against inputs that
   predate the CODATA-2022 move the bean flagged; this file fixes the published
   colour-blind w and today's constants.  What IS established is that the c_5
   slot is not the cause of THAT gap either.

5. DIRECTION SETTLED, and it is the reverse of how the question was posed.
   `3c_3^2 + b` lives in exactly one place in the tree:
   `fsh-guts/deprecated/computations/precision-ladder-superseded/`.  Its coefficient
   family there is identical to the live conjecture family at c_4, c_6 and c_7
   and differs ONLY at c_5 -- so c_5 is precisely what the supersession changed.

   Against the SDP extraction the live producer
   (`qbeta/qbeta_decay_sdp_full_ck.py`) records:

       extracted             -1.2229
       -(b^2 + 1/2)          -1.2527    2.4 % off        <- six sites, CURRENT
       3c_3^2 + b           +12.8676    ~10x, wrong sign <- two sites, SUPERSEDED

   So the 0.202 % agreement in finding 3 is NOT evidence that `3c_3^2+b` is
   right.  It is evidence that the PUBLISHED HEADLINE WAS COMPUTED BY THE
   DEPRECATED PRODUCER and never recomputed when c_5 changed.  Same for table 3,
   whose N=4/N=5 rows the block's own declared producer
   (`probe_q_beta_operator_valued_N3.py`) cannot generate -- it stops at N=3.

   The stale sites are the HEADLINE, TABLE 3, and the context's mixing-pattern
   line -- NOT the six carriers.  An earlier pass of this file proposed
   rewriting the six to match the two; that would have propagated a superseded
   coefficient into the framework's formalized family.

STILL NO FIX APPLIED, and this one must not be applied blind: correcting the
headline means recomputing a published number with the live c_5, and its SIGN is
unresolved (hypothesis 4).  Settle the sign, then recompute the headline and
table 3 together from a producer that actually reaches N=5.

Also open, unchanged: `q-beta-gamma-gamma-canonical-derivation.md` still
publishes the retired `b^2+1/2` at **c_4**, where the supersession replaced it.

Not to be closed by fitting: do not tune w, the pin, or CODATA to make a column
come out -- that would manufacture provenance for numbers whose origin is the
actual open question.
""")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
