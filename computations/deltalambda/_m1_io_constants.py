#!/usr/bin/env python3
"""The three infinite-order (IO) leading constants the M_1>0 arc shares, in ONE place.

WHY THIS MODULE EXISTS.  These three numbers were computed in PR #5901 and are consumed by 12
probes in this directory.  Until this module they were RETYPED at 24 sites -- every one of them
byte-identical today, which is the point: nothing made them stay that way.  A single edited digit
in one probe would have produced two probes disagreeing about the same limit with no diff to
notice, and the corpus has no producer here to arbitrate (see PROVENANCE below).

PROVENANCE, and the reason these are literals rather than a call.  No producer in THIS repository
computes rho_P, the CS margin, or the sigma ratio; all three arrive from merged PR #5901's IO
computation.  So a literal is the honest representation -- there is nothing to load from -- and the
`witness-value-copy` and `codata-truncation` gates should read them here, once, rather than at 24
scattered sites.

HOW MANY DIGITS ARE REAL.  These are NUMERICALLY EXTRAPOLATED limits, not closed forms, and they
are recorded at 12 significant digits.  The extrapolation is Richardson on the measured exponent
(see wlambda_covariance_epic_M1_CA_to_margin_conversion.py), which routinely gives 6-7 reliable
digits while being written out to 12.  Do NOT read the trailing digits as converged; in particular
do not use them to accept or reject a closed-form identification (see RHO_INF below).

Import by bare name -- these probes run as `python3 <script>.py`, so sys.path[0] is this directory
and a sibling module resolves without touching PYTHONPATH.  That is deliberately NOT the
`_path_bridge` case: the bootstrap trap is about reaching the PARENT `computations/` package, which
a sibling import does not do.
"""
from __future__ import annotations

import mpmath as mp

# Build the literals at a precision no caller undercuts.  Consumers set mp.mp.dps to 30 or 40 and
# do so AFTER their import block, so a module-level literal built at the caller's ambient dps would
# silently be a 15-dps value -- the exact precision-downgrade class this arc is auditing.  Fifty
# digits is well above both, and an mpf is a fixed binary object once built: a dps-30 caller rounds
# it in arithmetic exactly as it rounds anything else.
_DPS = 50

# --- merged PR #5901, IO leading constants -----------------------------------------------------


#: IO leading rho_P.  DERIVED, not extrapolated.
#:
#:     RHO_INF = 2*sqrt(6)/5,   RHO_INF**2 = 24/25   (EXACT)
#:
#: Derived from Kerov's central limit theorem for the Plancherel measure (Ivanov-Olshanski,
#: library/arxiv-math-0304010v1, eq. 0.3): the fluctuation field Delta(2 cos theta) =
#: (1/pi) sum_{k>=2} (xi_k/sqrt(k)) sin(k theta) with xi_k iid N(0,1).  Expanding the two
#: observables in that sine basis on the support [-2,2] gives G_k = pi*delta_{k,3} for x**2
#: (it couples to ONE mode) and F_k = 8*(-1)**((k-3)/2)/(k**2-4) for odd k>=3 for |x|; the
#: covariance sum telescopes to S = 8/9, and rho = ((8/5)pi/3)/sqrt((8/9)pi**2/3) = 2*sqrt(6)/5.
#: The k>=2 start of Kerov's sum is what encodes conditioning on the box count, which is the
#: arc's own `cond = cXY - cXN*cYN/VN`.  Producer, 8/8 PASS, exact symbolic throughout:
#: computations/deltalambda/wlambda_covariance_epic_M1_rho_inf_kerov_derivation.py
#:
#: SUPERSEDES the literal 0.979796195657 recorded by merged PR #5901, which was a numerical
#: extrapolation.  The two agree through six significant digits and depart at the seventh:
#:
#:     extrapolated  0.979796195657
#:     2*sqrt(6)/5   0.979795897113
#:     relative gap  3.047e-07   (6.09e-07 on the square)
#:
#: The former comment here said the discriminator was "whether digits 7-12 of the extrapolation
#: are converged".  The derivation answers it from the other side and the answer is NO: digits
#: 7-12 of that literal are extrapolation error, not signal.  Consequently the `approx`-not-`=`
#: instruction that used to close this comment is DISCHARGED for rho_inf -- it may now be written
#: with `=`, because it is exact.  It still binds SIG_RATIO_INF below, which remains extrapolated.
#:
#: Two consumers deliberately keep their own copy of the old literal and must NOT be "drained"
#: into this import: wlambda_covariance_epic_M1_rho_inf_closed_form_resolvability.py line 58
#: (RHO_LITERAL, "as recorded") studies that extrapolation as its object, so importing the exact
#: value would make it circular.
with mp.workdps(_DPS):
    RHO_INF = 2 * mp.sqrt(6) / 5

#: IO limit of sigma_D / sigma_A.
with mp.workdps(_DPS):
    SIG_RATIO_INF = mp.mpf('0.679609581496')

#: IO leading (Cauchy-Schwarz) margin, m_inf.
#:
#: DERIVED, not a fourth literal.  The three numbers PR #5901 reports are not independent: to all
#: twelve recorded digits, 0.979796195657 - 0.679609581496 = 0.300186614161 EXACTLY in decimal.
#:
#: MIXED TIER as of the rho_inf derivation above.  M_INF is now an EXACT value minus an
#: EXTRAPOLATED one, so it is no better than SIG_RATIO_INF and inherits that leg's ~1e-6.  It
#: moved 0.300186614161 -> 0.300186315617 (9.945e-07 relative) when RHO_INF was made exact; any
#: probe output differing from a pre-derivation record at the sixth decimal has THAT cause and is
#: not a regression.  Deriving SIG_RATIO_INF is what would make M_INF exact; that is still open.
#: That is the arc's own definition m_inf = rho_inf - (sigma_D/sigma_A)_inf, and typing it as a
#: separate literal made an identity look like a coincidence.  Deriving it has two consequences
#: worth knowing:
#:
#:   * the identity is now visible in the source instead of being a coincidence a reader has to
#:     notice.  It does NOT make the leg-decomposition closure column exactly zero -- MEASURED,
#:     because I first wrote that it would: building the constants at dps 50 (see _DPS) moves the
#:     residual in wlambda_covariance_epic_M1_margin_leg_decomposition.py from a printed 0.0 to
#:     3.9e-34 at some n and 1.5e-33 at others.  The LARGEST of those is still ~130x BELOW that
#:     probe's own dps-30 epsilon of 1.97e-31 (quote the worst case, not the best), and the exact
#:     0.0 was itself an artifact: at dps 30 and 40 the three decimals' binary roundings cancel
#:     identically, at dps 50 they leave one ulp (1.34e-51).  A closure column reading exactly zero
#:     for a rounding reason was not testing the closure;
#:   * M_INF carries FEWER reliable digits than either input, not the same twelve.  It is a
#:     difference of two numbers agreeing in their leading digit, so it loses one to cancellation
#:     on top of whatever the extrapolation had.
with mp.workdps(_DPS):
    M_INF = RHO_INF - SIG_RATIO_INF

# Aliases used by the probes that named them differently.  Same objects, not copies.
LEAD_MARGIN = M_INF
LEAD_RHO = RHO_INF
LEAD_SIGRATIO = SIG_RATIO_INF

__all__ = [
    "M_INF", "RHO_INF", "SIG_RATIO_INF",
    "LEAD_MARGIN", "LEAD_RHO", "LEAD_SIGRATIO",
]
