# binding_channel_taxonomy_probe — full output (2026-08-31)

Verbatim run. Regenerate with:

    python3 -u computations/binding_channel_taxonomy_probe.py

```
binding_channel_taxonomy_probe
==============================================================================
q0 (50-digit proton pin) = 1.1099785827513808076
E_0 = m_e/(q0(q0-1))     = 4.18598136329 MeV   (the corpus's scale)
Q_beta                   = 0.78233340931 MeV
tr_p = 1.1457596924573   tr_n = 0.98774368811581
f      : {'pp': '0.6126880371', 'nn': '0.4036277384', 'pn': '0.5082297894'}
f_bar  : {'pp': '0.4036277384', 'nn': '0.6126880371', 'pn': '0.5080859861'}

THE FOUR EVALUABLE CHANNELS, on the chain bond set (the wired one)
  1 observe-early  Q_b*|tr_f|*(1-prod f)
  3 log-ratio      E_0*sum_bonds log(1/f)
  4 bar-norm log   (E_0/2)*sum_bonds log(1/(f*f_bar))
  5 pairwise sum   sum_bonds E_0*tr_pair_free*(1-f)   [signed, per-bond]

 nucleus   A     ch1 B/A     ch3 B/A     ch4 B/A     ch5 B/A
    1p1n   2  0.21770174   1.4165813   1.4168774   1.1648428
    1p2n   3   0.2317105   2.2103152   1.9193337   1.5884235
    2p1n   3  0.23285074   1.6279574   1.9193337   1.4860155
    2p2n   4    0.219016   2.1704138   2.1705619   1.7234078
    3p3n   6  0.18312233   2.4216913     2.42179   1.9095962
    3p4n   7  0.15800422   2.6182758   2.4935695   1.9847374
    6p6n  12   0.1369094   2.6729688   2.6730182   2.0957845
    8p8n  16   0.1315715   2.7357882   2.7358252   2.1423316
  12p12n  24   0.1438912   2.7986076   2.7986322   2.1888787
  16p16n  32  0.17702995   2.8300172   2.8300358   2.2121522
  20p20n  40  0.23232072   2.8488631   2.8488779   2.2261164

STRUCTURAL SCORING — the actual selector
  Extensive  <=>  B asymptotically LINEAR in A  <=>  second difference
  of B -> 0 on an evenly spaced grid.  Grid A = [8, 16, 24, 32, 40], spacing 8.

 ch   B/A at A=2  B/A at A=40    2nd diff of B (relative to 1st)  extensive?  additive/bond?
  1   0.21770174   0.23232072                           0.390395          no   no (1 - prod)
  3    1.4165813    2.8488631                        7.31201e-51         YES             YES
  4    1.4168774    2.8488779                        7.31201e-51         YES             YES
  5    1.1648428    2.2261164                        4.68501e-51         YES             YES

  A second difference that is EXACTLY zero (to 1e-30 of the first) means
  B is exactly affine in A on the chain -- which it must be, since the
  chain has A-1 bonds and the additive channels sum one term per bond.
  Channel 1's is not zero: its trace prefactor |tr_p|^Z|tr_n|^N is
  exponential in A, so B is too.

  'additive/bond?' is the criterion that decides whether
  QOU.Mass.CoordinationSaturation applies at all: its object is
  B = eps*M, binding additive in the bond count.  Channel 1 enters
  through (1 - prod f), which is bounded by 1 for ANY bond set, so the
  premise is not instantiated there (#6332).

THE THREE NOT RE-EVALUATED HERE, classified from source
------------------------------------------------------------------------------
  ch2  observe-last angle (binding_canonical)
        not evaluated: needs per-partition characters; self-marked '# refuted: small/neg/shrinks'
        structure: additive over PARTITIONS, not bonds -> CoordinationSaturation does not apply
  ch6  volume x Dtr (binding_link_volumes)
        not evaluated: not a trace-ratio channel; Vol(Hopf) = 0 kills the deuteron leg
        structure: extensivity depends on Vol(K_bind), which the corpus has only for A <= 3
  ch7  magic-A (magic_A_formula)
        not evaluated: marked DEPRECATION-CANDIDATE; carries acknowledged-anchor constants
        structure: extensive BY CONSTRUCTION (B = rho_F*m_e*A*Vol) -- so B/A is constant trivially, and it says nothing about coordination

AME COMPARISON — reported, and NOT the selector
  Choosing the channel that lands nearest the data is the fit this arc
  exists to avoid.  This column is here so nobody has to re-derive it,
  and it is deliberately not fed into any verdict above.
 nucleus   A      B_AME     ch1 x     ch3 x     ch4 x     ch5 x
    1p1n   2   2.224566    5.1092   0.78519   0.78502   0.95488
    1p2n   3   8.481798    12.202    1.2791     1.473    1.7799
    2p1n   3   7.718043    11.049    1.5803    1.3404    1.7313
    2p2n   4   28.29567    32.299    3.2592     3.259    4.1046
    3p3n   6   31.99456    29.119    2.2019    2.2019    2.7924
    3p4n   7   39.24452    35.482    2.1412    2.2483    2.8247
    6p6n  12   92.16173    56.097    2.8733    2.8732    3.6646
    8p8n  16   127.6193    60.623    2.9155    2.9155    3.7231

Reading
------------------------------------------------------------------------------
  * OF SEVEN LIVE CHANNELS, EXACTLY THREE are both extensive and
    additive over bonds: the log-ratio (3), the bar-norm log (4) and
    the signed pairwise sum (5).  Their second differences vanish to
    ~7e-51 of the first -- B is exactly affine in A on the chain.
  * Channels 3 and 4 are numerically near-identical (2.8488631 vs
    2.8488779 at A=40, 5e-6 apart) and converge together, because under
    convention D the bar involution EXCHANGES pp and nn, so on an N=Z
    chain the bar-symmetrisation is nearly a no-op.  So the seven
    channels collapse to TWO distinct extensive candidates: the log
    family, and the pairwise sum.
  * The one that SHIPS -- channel 1, binding_canonical's observe-early
    trace difference -- is neither extensive nor additive, for any bond
    set.  Its second difference is 0.39 of the first, because the trace
    prefactor is exponential in A.
  * The other four are excluded structurally, not numerically: ch2 is
    additive over PARTITIONS not bonds; ch6 needs a Vol(K_bind) the
    corpus has only for A <= 3 and which is 0 for the deuteron; ch7 is
    extensive by construction and so says nothing about coordination.
  * SO THE CHANNEL QUESTION AND THE BOND-SET QUESTION ARE NOT
    INDEPENDENT.  The chain is forced by the strand layout (#6346,
    QOU.Mass.StrandLayoutForcesChain); on the chain the additive
    channels are exactly affine, hence saturate; and
    complete_graph_no_saturation only ever bit on the additive family
    in the first place.  What is left open is the MAGNITUDE -- the
    AME column above, which is 2-3x on the log family and is NOT
    the selector.
  * PRECISION CAVEAT that bears on channel 3: its prototype producer
    log_ratio_binding_prototype.py imports the FLOAT64 q_parameter.Q
    and accumulates through math.log -- the identical defect fixed in
    derived_bond_graph_binding by #6338 (bean qou-vsqh), in the very
    channel this question turns on.  Not fixed here; it wants its own
    PR with a witness refresh.
```
