---
# qou-v3u2
title: 'Two-nucleon falsification: can any Wedderburn channel unbind pp/nn?'
status: completed
type: task
priority: normal
created_at: 2026-09-01T07:56:28Z
updated_at: 2026-09-01T08:01:46Z
---


RESOLVED 2026-09-01 -- computations/probes/two_nucleon_pattern_is_unreachable_probe.py,
6/6. Answer: no channel can, and the reason is an impossibility rather than a
mis-fit.

VERIFIED FROM OWN MEASUREMENTS (the claim reached me via a survey agent quoting
L_pp = +2.5416 / L_nn = +3.3069, which are NOT my numbers; re-measured here):

  bond   d              mu = z+d      L = -log(mu)   model    nature
  pp     0.0000000000   0.612688037   0.4898993843   BOUND    UNBOUND (diproton)
  pn    -0.1044582478   0.508229789   0.6768215924   BOUND    bound, 2.2245 MeV
  nn    -0.2090602988   0.403627738   0.9072622655   BOUND    UNBOUND (dineutron)

Nature binds 1 of 3; the model binds 3 of 3 and makes the DINEUTRON THE MOST
BOUND. The substance of the survey's claim is confirmed even though its numbers
were not mine.

STRUCTURAL, NOT PARAMETRIC. d = -beta*h with beta in [0,1], so d <= 0 always,
so mu = z + d <= z = 0.612688 < 1, so L > 0 for every single crossing. Unbinding
needs z > 1 i.e. q^3 > q^2 + 1 -- threshold at the supergolden ratio
q* = 1.4655712318767680, with q0 24.3 % below. beta, colour convention, framing
and writhe normalisation ALL only move d, so none of them can help.

THE IMPOSSIBILITY. mu(d) = z + d EXACTLY: slope 1 (spread 5.33e-15) and
|mu(d)-(z+d)| <= 8.9e-16 with the exact Wenzl r=2 weights, flavour-independent.
(Via load_cost it is 3.1e-9 -- that path's documented stored-f64 floor, not a
defect.) Affine because the bond crossing occurs exactly once:
tr(W(M+dI)) = tr(WM) + d*tr(W).

Nature requires {d : mu(d) > 1} to contain BOTH endpoints of [-h, 0] and EXCLUDE
an interior point. For an affine mu that set is a HALF-LINE. Therefore NO
assignment of bond offsets -- in any Wedderburn block or any weighted
combination -- reproduces the physical pattern.

And the affineness is not incidental: the constant is the MARKOV PARAMETER. The
property that makes this trace a link invariant is the same one forbidding the
two-nucleon pattern. That trade-off is the real content of the falsification.

UNBINDING EXISTS BUT IS WRONGLY PATTERNED. Per-block on the four live H_6 blocks:

  block    dim        y      mu_pp      mu_pn      mu_nn
  (3,3)     5   0.015124   0.370566   0.431211   0.457700
  (4,2)     9   0.046032   0.208466   0.398117   0.035035
  (5,1)     5   0.078953  -0.276707  -0.944701  -1.500687   NEGATIVE
  (6,)      1   0.115324   1.109979   1.005520   0.900918   > 1 twice

The trivial block gives mu = q + d exactly (q0, q0+D_PN, 1/q0), so it unbinds pp
and pn but binds nn -- wrong pattern, and still affine, so same obstruction. The
(5,1) block's ratio is NEGATIVE, so per-block "binding" is not even well defined
there; only the y-weighted total is a Markov trace.

WHY: NATURE GRADES BY (T,S), NOT FLAVOUR.
  a_pp(1S0) = -17.3     unbound
  a_nn(1S0) = -18.9     unbound
  a_np(1S0) = -23.740   unbound   <- np is ALSO unbound in 1S0
  a_np(3S1) =  +5.419   BOUND     <- the only bound channel
All three T=1 states are unbound. The single bound two-nucleon state is the T=0
spin-triplet, which only np can form because Pauli forbids it for pp and nn. A
construction assigning one scalar per flavour pair is answering a question
nature does not ask. This is the same gap qou-9el1 found from the A>=3 side
(no isospin asymmetry term) and that the Tower survey recommends closing by
grading on T rather than T_3 -- three independent routes, one gap.

ESCAPE ROUTES:
 (a) MORE THAN ONE CROSSING PER BOND -- mu becomes polynomial in d of degree =
     crossing count; degree >= 2 can be non-monotone. Minimal structural fix.
 (b) A GRADING THAT SELECTS AN OPERATOR PER CHANNEL, not an offset -- genuine
     (T,S) labels. The n=2 Wedderburn split IS the sym/antisym decomposition, so
     the labels already exist and nothing uses them.
 (c) q > q* -- CLOSED, q0 is fixed 24.3 % below.
(a) and (b) are live and not exclusive. Neither attempted here.

SCOPE: the impossibility is proved for a SINGLE-CROSSING bond with a real
offset, which is what the construction uses -- so it applies to it as built and
to every convention variant. It does NOT say the substrate cannot describe the
two-nucleon sector; escape (a) removes the obstruction immediately.
