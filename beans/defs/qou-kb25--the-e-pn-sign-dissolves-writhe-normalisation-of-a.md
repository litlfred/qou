---
# qou-kb25
title: 'The e_pn sign dissolves: writhe normalisation of a mixed bond is not an exponent'
status: completed
type: task
priority: normal
created_at: 2026-09-01T04:57:46Z
updated_at: 2026-09-01T04:58:03Z
---


RESOLVED 2026-09-01 -- computations/probes/pn_writhe_is_not_an_exponent_probe.py,
6/6. Answers the flag qou-brng left open in commit 1b85370fd, verbatim:
"Interpolating from e_pp = +1 and e_nn = -1 gives e_pn = +delta/2, but
production says -delta/2 -- OPPOSITE SIGN. I do not know which is right and did
not guess. Flagged for whoever settles it."

IT SETTLES BY DISSOLVING. Both candidates are wrong and the sign was never the
live degree of freedom.

The framed bond ratio is EXACTLY linear in beta (symbolic residual 0):

    z - beta h  =  (1-beta) . z  +  beta . (z-h)

the two summands being the ratios of the pure crossings sigma (writhe +1) and
sigma^-1 (writhe -1). The Markov trace is linear and the writhe factor
(1-h)^(e/2) is defined PER DIAGRAM -- a formal sum of two diagrams is not a
diagram and has no writhe. So the normalised bond is

    (b)  (1-beta) z (1-h)^(1/2) + beta (z-h) (1-h)^(-1/2)

not the whole ratio under an averaged exponent

    (a)  (z - beta h) (1-h)^((1-2beta)/2)

(a) and (b) agree EXACTLY at beta = 0 and beta = 1 -- which is why p-p and n-n
can never detect the difference, and why an interpolation anchored on those two
points reproduces itself.

    beta       1-2beta (interpolated)     e_eff (linearity)
    0                +1                        +1        exact
    0.25             +0.5                      +0.6035
    beta_pn          +/-0.000688               +0.149437
    0.75             -0.5                      -0.3789
    1                -1                        -1        exact

e_eff lies above the chord at all 99 interior grid points, peaking +0.14968 at
beta = 0.54, so interpolation understates it everywhere between the endpoints.
e_eff(beta_pn) is 217.25x either candidate, and both candidates are zero to
three decimals.

WORTH 108x THE DISPUTE IT REPLACES:
    sign question       dL_pn = 1.6133e-4   0.0238 % of L_pn
    exponent vs linear  dL_pn = 1.7443e-2   2.5769 % of L_pn
    on 4He: 0.29207 MeV of 28.2957 (1.03 %); up to 3.28 % of AME across the table

EXACTLY CONFINED TO THE p-n BOND. L_pp shift 0.0, L_nn shift 0.0, spread
(L_nn - L_pp) shift 0.0, mirror 3H - 3He shift 0.0 -- p-p and n-n sit at the
exact endpoints and p-n multiplicity Z.N is mirror-symmetric. Binding MAGNITUDES
move up (1-3 %); NO asymmetry observable moves at all. The mirror-pair ordering
and the 56 % spread compression from qou-6pt7 both survive verbatim.

SELF-RETRACTION: this withdraws the +delta/2 half of qou-6pt7's A2. The operator
identity it rests on is correct and is reused here; what was wrong was feeding
its coefficient average into an exponent. qou-6pt7's docstring now carries a
forward pointer, and its A1/A4/A5/A6 stand.

SCOPE: a correction WITHIN the writhe-normalised convention. The framed branch
(bond constants, additivity, no-distance-decay) applies no normalisation and is
untouched. Which convention binding should use is STILL the open physics
question from qou-6pt7 -- framing is Tw in Lk = Wr + Tw.
