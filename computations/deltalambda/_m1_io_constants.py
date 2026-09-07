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


#: IO leading rho_P.
#:
#: A CONJECTURED closed form 2*sqrt(6)/5 = sqrt(24/25) is annotated in the arc.  It is neither
#: confirmed nor refuted by this literal, and the arithmetic is worth stating so nobody re-derives
#: it as a refutation:
#:
#:     RHO_INF**2      = 0.96000058502393...
#:     24/25           = 0.96
#:     relative gap    = 6.09e-07   (3.05e-07 on RHO_INF itself)
#:
#: i.e. the literal agrees with the candidate through SIX significant digits and departs at the
#: seventh -- exactly the signature of a 6-7-digit extrapolation written to 12.  The discriminator
#: is whether digits 7-12 of the extrapolation are converged, which the arc has not established.
#: Until it does, write the identification with `approx`, never `=` (AGENTS.md section 7ab).
with mp.workdps(_DPS):
    RHO_INF = mp.mpf('0.979796195657')

#: IO limit of sigma_D / sigma_A.
with mp.workdps(_DPS):
    SIG_RATIO_INF = mp.mpf('0.679609581496')

#: IO leading (Cauchy-Schwarz) margin, m_inf.
#:
#: DERIVED, not a fourth literal.  The three numbers PR #5901 reports are not independent: to all
#: twelve recorded digits, 0.979796195657 - 0.679609581496 = 0.300186614161 EXACTLY in decimal.
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
