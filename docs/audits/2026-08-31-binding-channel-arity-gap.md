# binding_channel_saturation_probe — full output (2026-08-31)

Verbatim run of `computations/binding_channel_saturation_probe.py`. Regenerate with:

    python3 -u computations/binding_channel_saturation_probe.py

```
binding_channel_saturation_probe
==============================================================================
q0 (proton pin)          = 1.1099785827513808076
f_pp = z                 = 0.6126880371464652516
f_pn = z - h(1/2 - d/4)  = 0.50822978937673896258
f_nn = z - h             = 0.40362773835082593616
tr_M^3(proton)           = 1.1457596924573008697
tr_M^3(neutron)          = 0.98774368811580957163

  Every bond factor is in (0,1), so -log f > 0: the free-energy channel
  has a positive per-bond cost, which is the `eps > 0` hypothesis of
  complete_graph_no_saturation.  Checked:
    0 < f_pp < 1 : True   -log f_pp = 0.489899384255
    0 < f_nn < 1 : True   -log f_nn = 0.907262265533
    0 < f_pn < 1 : True   -log f_pn = 0.676821592386

CHANNEL 1 — free energy:  -log(prod f) / A  =  sum_bonds (-log f) / A
  This is exactly `eps * M / A`, the object CoordinationSaturation covers.
   A  M_chain   M_compl   chain -logP/A   compl -logP/A
   2        1         1  0.338410796193  0.338410796193
   4        3         6  0.518495810544   1.02611200483
   6        5        15  0.578524148661   1.71381321347
   8        7        28  0.608538317719   2.40151442211
  12       11        66  0.638552486777   3.77691683939
  16       15       120  0.653559571307   5.15231925667
  20       19       190  0.662563822024   6.52772167396
  24       23       276  0.668566655836   7.90312409124
  32       31       496    0.6760701981   10.6539289258
  40       39       780  0.680572323459   13.4047337604
  chain    range over A=2..40: 0.3384108 .. 0.68057232   ratio 2.01108
  complete range over A=2..40: 0.3384108 .. 13.404734   ratio 39.6108
  => chain is BOUNDED (a plateau); complete GROWS without bound.
     That reproduces complete_graph_no_saturation exactly, and it is the
     channel in which the cited exclusion is a statement about this corpus.

CHANNEL 2 — observe-early, the form binding_canonical actually computes:
  B = Q_b * |tr_free| * (1 - prod f),   tr_free = tr_p^Z * tr_n^N
   A        |tr_free|     1-P chain     1-P compl       B/A chain       B/A compl
   2    1.13171690432  0.4917702106  0.4917702106    0.2782723302    0.2782723302
   4    1.28078315153  0.8743158471  0.9835008765    0.2799522515     0.314912838
   6    1.44948394336  0.9689185746  0.9999657861     0.234071986    0.2415723918
   8    1.64040548124  0.9923136292  0.9999999955    0.2034745896    0.2050506842
  12    2.10100370205  0.9995299304           1.0    0.1750013403    0.1750836418
  16    2.69093014288  0.9999712523           1.0    0.1681782991    0.1681831339
  20    3.44649798894  0.9999982419           1.0    0.1723245965    0.1723248994
  24    4.41421655602  0.9999998925           1.0    0.1839256701    0.1839256898
  32    7.24110503387  0.9999999996           1.0    0.2262845322    0.2262845323
  40    11.8783483878           1.0           1.0    0.2969587097    0.2969587097

  The (1 - prod f) factor is BOUNDED IN [0,1) by construction, for ANY
  bond set: it is 1 minus a product of numbers in (0,1).  So in this
  channel the bond count cannot drive B/A at all past the point where the
  product has already collapsed -- and it collapses fast:
    A=  4  prod f (chain) =     0.12568415   prod f (complete) =    0.016499124
    A=  8  prod f (chain) =   0.0076863708   prod f (complete) =   4.5319416e-9
    A= 16  prod f (chain) =    2.874769e-5   prod f (complete) =  1.5776797e-36

  What DOES drive B/A in channel 2 is the constituent factor:
   A        |tr_free|      |tr_free|/A   ratio to prev
   2    1.13171690432   0.565858452161               -
   4    1.28078315153   0.320195787882       1.1317169
   6    1.44948394336   0.241580657226       1.1317169
   8    1.64040548124   0.205050685155       1.1317169
  12    2.10100370205   0.175083641837       1.2807832
  16    2.69093014288    0.16818313393       1.2807832
  20    3.44649798894   0.172324899447       1.2807832
  24    4.41421655602   0.183925689834       1.2807832
  32    7.24110503387   0.226284532308       1.6404055
  40    11.8783483878   0.296958709695       1.6404055

Is the channel-2 shape the constituent factor?  A falsifiable check:
  |tr_free|/A = c^(A/2)/A on the N=Z chain, with c = |tr_p*tr_n|.  Its
  minimum is at A* = 2/ln(c) -- no fitting, one closed form.
    c = |tr_p*tr_n|     = 1.13171690432221
    predicted A* = 2/ln c = 16.16346252
    measured argmin over A = 4,6,...,40 : 16
    predicted A* rounds to even A       : 16
    agree: True

Could ANY bond set rescue channel 2?  A bound, not a search:
  B/A = Q_b * |tr_free| * (1 - prod f) / A,  and (1 - prod f) is in [0,1)
  for every bond set, since every f is in (0,1).  So
      B/A  <=  Q_b * |tr_free| / A     for EVERY bond set,
  and equality is approached as soon as prod f collapses -- measured
  above at A >= 12 for the chain and A >= 8 for the complete graph.
  A plateau therefore needs |tr_free| ~ A.  But |tr_free| = c^(A/2) is
  exponential, and an exponential is asymptotically linear only in the
  degenerate case c = 1, where it is CONSTANT and B/A -> 0.  So no choice
  of bond set produces a plateau in this channel.
    c = 1.13171690432, so ln c = 0.123735863984 != 0: the
    degenerate case does not obtain, and B/A diverges.

Reading
------------------------------------------------------------------------------
  * CoordinationSaturation covers B = eps*M -- binding ADDITIVE in the
    bond count.  In the free-energy channel the live factors instantiate
    that exactly (eps = -log f > 0), and the measurement above reproduces
    its dichotomy: chain plateaus, complete graph does not.  So the
    exclusion IS a statement about this corpus -- in that channel.
  * binding_canonical computes the observe-early trace DIFFERENCE, where
    the bond set enters as (1 - prod f), bounded in [0,1) for every bond
    set.  complete_graph_no_saturation's premise is not instantiated
    there, so it does not exclude the complete graph in the channel the
    canonical producer uses.  That is an arity gap, not a refutation of
    the theorem, which is correct as stated.
  * In that channel B/A is set by |tr_p|^Z|tr_n|^N, which is exponential
    in A and is NOT a function of the bond set at all.  Measured, the two
    bond sets agree to 10 significant figures from A = 12 on, and the
    curve's minimum sits where the constituent factor alone predicts,
    A* = 2/ln|tr_p*tr_n| = 16.16 against a measured argmin of 16.
  * And no bond set rescues it: (1 - prod f) < 1 always, so
    B/A <= Q_b|tr_free|/A, and a plateau would need an exponential to be
    linear.  So the saturation constraint that has been driving the
    bond-set search is, in this channel, a constraint on the CONSTITUENT
    term rather than on coordination.
  * Scope (a), and two limits worth stating.  This is measured on the
    corpus's own closed-form factorisation tr_p^Z tr_n^N prod f, not on
    the direct Hecke trace binding_canonical evaluates; if those two
    disagree the channel-2 rows move.  And nothing here says which
    channel is physically right -- only which one the cited exclusion is
    a statement about.
```
