---
# qou-9el1
title: 'A-scaling sweep: is the binding shortfall constant or growing with A?'
status: completed
type: task
priority: normal
created_at: 2026-09-01T06:07:32Z
updated_at: 2026-09-01T06:49:27Z
---


RESOLVED 2026-09-01 -- computations/probes/the_alpha_spike_is_an_inverted_stagger_probe.py,
6/6. Neither constant nor growing: 4He is a SINGULAR outlier, and the underlying
error is a sign inversion, not a magnitude.

A=2..6 now computable. A sparse row-chunked Markov trace (generators are ~1.0-1.6
nonzeros per row, so the accumulator never goes dense-square) reproduces the
dense n=12 engine to 1e-12 and then runs n=15 in ~2s and n=18 in ~172s.

  iso    A   B model    B AME   model/AME  shortfall
  2H     2    2.83316   2.22457   1.2736    0.79x  (OVER-binds)
  3H     3    8.00298   8.48180   0.9435    1.06x
  3He    3    6.69944   7.71804   0.8680    1.15x
  4He    4   10.24709  28.29566   0.3621    2.76x  <-- spike
  5He    5   16.15903  27.56066   0.5863    1.71x
  5Li    5   13.91407  26.33066   0.5284    1.89x
  6He    6   18.99577  29.27112   0.6490    1.54x
  6Li    6   17.10450  31.99399   0.5346    1.87x

Every other A>=3 isotope is 1.06..1.89x; 4He exceeds the next-worst by 1.46x.

THE SPIKE IS AN INVERTED STAGGER, NOT A MISSING PEAK. Second difference of B/A:

  A   B/A model  B/A AME   d2 model   d2 AME
  3     2.6677    2.8273   +0.6785    -1.2658   OPPOSITE
  4     2.5618    7.0739   -0.3880    +2.9042   OPPOSITE
  5     3.2318    5.5121   +0.3679    -0.6910   OPPOSITE

Opposite sign at ALL THREE. The model peaks at ODD A where physics peaks at EVEN
A -- nature's pairing binds even-even nuclei MORE, this construction binds them
LESS. 4He is one instance of a systematic sign error, which is why attacking 4He
alone was the wrong diagnosis. NOT an ordering artifact: grouping (ppnn instead
of pnpn) still gives d2(4) = -0.2915.

CHANNEL PURITY HOLDS ONLY ON THE CHAIN. band_between(0,2) touches generators
2,3,4,5 = strong(n0), intra(n1), EM(n1), strong(n1). A non-adjacent bond routes
through the intervening nucleon's intra and EM generators, so "3k+2 = strong" is
exact only for the chain and every all-pairs atom with A>=3 is channel-mixed by
construction. Restricting to the pure-strong chain moves the AME comparison
FURTHER away at 5/6 isotopes -- the clean channel does not rescue it.

EM PRESENT, ISOSPIN ASYMMETRY ABSENT:

  pair          dZ  dB model   dB AME   ratio
  3H  -> 3He     1   +1.3035   +0.7638   1.707
  5He -> 5Li     1   +2.2450   +1.2300   1.825
  6He -> 6Li     1   +1.8913   -2.7229  -0.695  *** SIGN INVERTED ***

The model always penalises higher Z (Coulomb-like, 1.7-1.8x too strong where the
sign is right). AME reverses at A=6 because (N-Z)^2 outweighs Coulomb. The model
has no such term. Liquid-drop reading: VOLUME-LIKE yes, COULOMB-LIKE yes,
PAIRING BACKWARDS, ASYMMETRY ABSENT.

This converges with the independent Tower/channel survey, which recommends
grading the interface by T rather than T_3 (the NN scattering length flips sign
across T, not T_3) and notes the corpus carries no NN partial-wave data at all.
Two routes, same gap.

TWO CORRECTIONS TO qou-38i9:
 1. Its "3.4693x short" headline is B(4He)/B(2H) -- the worst undershoot over the
    only overshoot. Across A=2..6 the model is within ~1.9x everywhere except
    4He. The ratio is true; as a summary it was misleading.
 2. Its two-row collapse is a COROLLARY of this corpus's own Lean theorems --
    convention D is Wenzl level r=2 (wenzlLevel_conventionD) and
    schurPrincipal_eq_zero_iff gives s_lambda = 0 <=> l(lambda) > r. New was only
    the application: nobody had used it to collapse H_12. Measurement stands,
    framing did not.

FOLLOW-ON THAT THIS OPENS. The blocks r=2 annihilates are exactly where colour
would live (l(lambda)=3 needs r>=3). At n=12 the r=3 structure is 19 blocks with
max dim 2673 -- SMALLER than the 13260 already run at n=18, so the level-3
experiment flagged as the highest-leverage unrun item is cheap with this
machinery. Not attempted here.
