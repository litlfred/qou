#!/usr/bin/env python3
"""The two c_3 bands differ by exactly 100x — the L2 factor — and mean different
things.  Neither refutes `c_3 = -2`.

Bean `qou-cds1`, tranche S1.  Coordination note for PRs #6342 / #6353, which
reached the second band independently and first.

TWO BANDS ARE NOW IN THE CORPUS FOR THE SAME NUMBER:

  (1) EXPERIMENTAL, `mass-theory/rem-qstar-decay-sector-q0.md:43`
      sigma_exp(c_3) = sigma(Q_beta)/(Q_N2 * u^3) = +/- 1.262   (61 % of |c_3|)
      -> "the absence of a measurement ... every candidate constant in
          [0.807, 3.331] agrees at least as well"

  (2) L2 TOLERANCE, PR #6353 via #6342
      c_3 = -2.069342577 +/- 0.01262   (0.61 %)   [c_3 recomputed live; see below]
      -> "c_3 = -2 = J_Hopf(q=1) is 5.495x outside"

**They are the same sigma divided by 100.**  Band (2) is band (1) scaled by the
L2 goal's own factor (`sigma_pred <= sigma_exp/100`).  Verified below to the
digit, including that #6353's `5.495x` reproduces from the NEUTRON-ONLY sigma.

WHY THIS MATTERS -- the two support OPPOSITE-SOUNDING sentences, both true:

    |c_3 - (-2)| = 0.0693426
      vs band (1)   0.055 sigma   INSIDE   -> experimentally indistinguishable
      vs band (2)   5.495 x       OUTSIDE  -> misses the L2 goal by 5.5x

**`5.495x outside` is NOT a refutation of `c_3 = -2`.**  Experimentally `-2` sits
at 0.055 sigma from the extracted value; nothing in the data disfavours it.  What
the 5.495x says is: *if* `-2` is right, Q_beta's L2 goal is missed by 5.5x.  A
statement about the GOAL, not about the candidate.

Reading (2) as evidence against `-2` is precisely the trap AGENTS.md's own c_k
banner records -- "a quantity differing only by normalisation, mistaken for a
discrepancy" -- one normalisation over.

THE STRUCTURAL CONSEQUENCE, which is the point of this file:

  A derived `c_3` that MEETS the L2 tolerance CANNOT BE VALIDATED BY Q_beta.
  It would be a number claimed to 0.61 % in a quantity the experiment pins to
  61 %.  The measurement cannot tell a correct derivation from a wrong one
  landing anywhere in `[0.807, 3.331]`.

So the L2 target for Q_beta sits **two orders of magnitude beyond current
experimental reach on this parameter**.  That is not a defect in anyone's work;
it is a fact about the target, and it fixes how a derived `c_3` must be
justified: **structurally, not empirically**, until the neutron Q-value improves
by the 32x (proton pin) / 130x (muon pin) the source block quotes.

Exact mpmath; no float64; emits no witness (it audits two published bands).

c_3 is RECOMPUTED, not typed: `qbeta_utils.c3_proton_extracted()` is the same
extraction `qbeta_ck_cache.py` performs (proton pin, CODATA 2022, convention C).
It used to carry a typed copy that no producer reproduces (2026-10-13).
"""
import sys

import mpmath as mp

from qbeta_utils import c3_proton_extracted

mp.mp.dps = 50


def main() -> int:
    checks = []

    c3 = c3_proton_extracted()
    cand = mp.mpf(-2)
    gap = abs(cand - c3)

    sig_neutron = mp.mpf("1.262")        # block's figure (neutron-mass sigma)
    sig_quad = mp.mpf("1.37865")         # quadrature sigma (m_n + m_p + m_e)
    band2 = mp.mpf("0.01262")            # #6353's quoted tolerance

    # 1. Band (2) is band (1) over 100 -- the L2 factor, not a new measurement.
    checks.append(("band(2) == band(1)/100 exactly, to the quoted digits",
                   abs(band2 - sig_neutron / 100) < mp.mpf("1e-12")))

    # 2. #6353's 5.495x reproduces from the neutron-only sigma.
    checks.append(("#6353's 5.495x reproduces from the neutron-only sigma",
                   abs(gap / band2 - mp.mpf("5.495")) < mp.mpf("0.001")))

    # 3. The SAME gap is inside band (1) and outside band (2).
    checks.append(("|c_3 - (-2)| is INSIDE the experimental band",
                   gap < sig_neutron))
    checks.append(("the same gap is OUTSIDE the L2 tolerance", gap > band2))
    checks.append(("so the two bands support opposite-sounding true sentences",
                   gap < sig_neutron and gap > band2))

    # 4. It is not a marginal call either way -- two orders of magnitude of room.
    checks.append(("experimentally it is not marginal: < 0.1 sigma",
                   gap / sig_neutron < mp.mpf("0.1")))

    # 5. Under the quadrature sigma the ratio softens but nothing flips.
    band2q = sig_quad / 100
    checks.append(("under the quadrature sigma it is 5.03x, still outside",
                   abs(gap / band2q - mp.mpf("5.03")) < mp.mpf("0.01")))
    checks.append(("and still well inside experimentally", gap < sig_quad))

    print("The two c_3 bands.  mpmath, 50 dps.\n")
    print(f"  extracted c_3            = {mp.nstr(c3, 12)}")
    print(f"  candidate  J_Hopf(q=1)   = {mp.nstr(cand, 12)}")
    print(f"  gap                      = {mp.nstr(gap, 8)}\n")
    print(f"  {'band':34} {'value':>12} {'gap in units':>14} {'verdict':>10}")
    for name, s in (("(1) experimental, neutron-only", sig_neutron),
                    ("(1') experimental, quadrature", sig_quad),
                    ("(2) L2 tolerance = (1)/100", band2),
                    ("(2') L2 tolerance = (1')/100", band2q)):
        v = gap / s
        verdict = "INSIDE" if gap < s else "outside"
        print(f"  {name:34} {mp.nstr(s, 6):>12} {mp.nstr(v, 5):>14} {verdict:>10}")

    print(f"\n  band(1)/band(2) = {mp.nstr(sig_neutron / band2, 6)}"
          f"   <- the L2 factor, exactly")

    print("\n--- checks ---")
    ok = True
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok = ok and bool(passed)
    print(f"\n{sum(1 for _, p in checks if p)}/{len(checks)}")

    print("""
FINDING

  The two published c_3 bands are the SAME sigma, 100x apart -- the L2 goal's
  own factor.  Both are correct.  They answer different questions, and the same
  gap of 0.0693 is INSIDE one and OUTSIDE the other.

  So `5.495x outside` must NOT be read as evidence against `c_3 = -2`.
  Experimentally that candidate is 0.055 sigma from the extracted value, and
  nothing in the data disfavours it.  The 5.495x says only that IF `-2` holds,
  Q_beta's L2 goal is missed by 5.5x -- a statement about the goal.

  CONSEQUENCE: a derived `c_3` meeting the L2 tolerance could not be checked
  against Q_beta at all -- 0.61 % claimed inside a 61 % measurement.  The L2
  target for Q_beta is two orders of magnitude beyond experimental reach on this
  parameter, so a derived c_3 has to be justified STRUCTURALLY.  Empirical
  agreement with Q_beta is available to any candidate in [0.807, 3.331] and
  therefore discriminates nothing.

SCOPE (a).  Not a claim that `c_3 = -2` is right, nor that the L2 goal is
unreachable -- the source block quotes the 32x / 130x sharpening that would make
it testable.  Only that the two bands must not be conflated, and that the
experiment currently cannot arbitrate this parameter.

COORDINATION.  Band (2) is #6353's, reached independently and first; #6342
relays it.  This file adds the relation between the bands and its consequence,
and takes no position on the entry-9 `|c_4| <= 1.4816` threshold, which is
those PRs' result and is not re-derived here.
""")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
