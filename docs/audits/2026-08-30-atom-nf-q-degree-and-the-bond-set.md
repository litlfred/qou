# atom_nf_q_degree_probe — full output (2026-08-30)

Verbatim run of `computations/substrate/atom_nf_q_degree_probe.py` on `main` +
this branch. Regenerate with:

    python3 -u computations/substrate/atom_nf_q_degree_probe.py

```
atom_nf_q_degree_probe — q-degree of the six NF coefficients vs A
==============================================================================

Equivalence gate (Laurent mirror vs the authoritative hm_sym):
  hm_laurent == hm_sym on 18 (seed, gen, d) cases x 6 slots  OK
  build_atom_nf_laurent == build_atom_nf_sym, checked after every factor, on 6 nuclei / 174 steps  OK

Crossing count: measured factor applications vs 11A + C(A,2) + Z
 nucleus   Z   N    A   steps  11A+C(A,2)+Z   ok
      1H   1   0    1      12            12  yes
       n   0   1    1      11            11  yes
      2H   1   1    2      24            24  yes
      3H   1   2    3      37            37  yes
     3He   2   1    3      38            38  yes
     4He   2   2    4      52            52  yes
     6Li   3   3    6      84            84  yes
     7Li   3   4    7     101           101  yes
     9Be   4   5    9     139           139  yes
     12C   6   6   12     204           204  yes
     14N   7   7   14     252           252  yes
     16O   8   8   16     304           304  yes
    20Ne  10  10   20     420           420  yes
    24Mg  12  12   24     552           552  yes
    28Si  14  14   28     700           700  yes
     32S  16  16   32     864           864  yes
    40Ca  20  20   40    1240          1240  yes

Per-coefficient Laurent degree  (max exponent, min exponent, span, #terms)
 nucleus    A                γ               σ₀               σ₁               L₊               L₋               e⁻
      1H    1   10, -10, 20, 11   11, -11, 22, 12    9,  -9, 18, 10    8,  -8, 16,  9   10, -10, 20, 11    5,  -5, 10,  6
       n    1    9,  -9, 18,  8   10, -10, 20,  9    2,  -2,  4,  3    5,  -5, 10,  4    7,  -7, 14,  8    8,  -8, 16,  9
      2H    2   22, -22, 44, 23   23, -23, 46, 24   21, -21, 42, 22   20, -20, 40, 20   22, -22, 44, 23   17, -17, 34, 18
      3H    3   33, -33, 66, 34   34, -34, 68, 35   32, -32, 64, 33   31, -31, 62, 30   33, -33, 66, 34   28, -28, 56, 29
     3He    3   36, -36, 72, 37   37, -37, 74, 38   35, -35, 70, 36   34, -34, 68, 35   36, -36, 72, 37   33, -33, 66, 34
     4He    4   48, -48, 96, 49   49, -49, 98, 48   47, -47, 94, 48   46, -46, 92, 47   48, -48, 96, 49   45, -45, 90, 44
     6Li    6   76, -76,152, 77   77, -77,154, 78   75, -75,150, 76   74, -74,148, 75   76, -76,152, 77   73, -73,146, 74
     7Li    7   87, -87,174, 88   88, -88,176, 89   86, -86,172, 87   85, -85,170, 86   87, -87,174, 88   84, -84,168, 85
     9Be    9  119,-119,238,120  120,-120,240,119  118,-118,236,119  117,-117,234,116  119,-119,238,118  116,-116,232,117
     12C   12  176,-176,352,177  177,-177,354,178  175,-175,350,176  174,-174,348,175  176,-176,352,177  173,-173,346,174
     14N   14  216,-216,432,217  217,-217,434,218  215,-215,430,216  214,-214,428,215  216,-216,432,217  213,-213,426,214
     16O   16  260,-260,520,261  261,-261,522,262  259,-259,518,260  258,-258,516,259  260,-260,520,261  257,-257,514,258
    20Ne   20  360,-360,720,361  361,-361,722,362  359,-359,718,360  358,-358,716,359  360,-360,720,361  357,-357,714,358
    24Mg   24  476,-476,952,477  477,-477,954,478  475,-475,950,476  474,-474,948,475  476,-476,952,477  473,-473,946,474
    28Si   28  608,-608,1216,609  609,-609,1218,610  607,-607,1214,608  606,-606,1212,607  608,-608,1216,609  605,-605,1210,606
     32S   32  756,-756,1512,757  757,-757,1514,758  755,-755,1510,756  754,-754,1508,755  756,-756,1512,757  753,-753,1506,754
    40Ca   40 1100,-1100,2200,1101 1101,-1101,2202,1102 1099,-1099,2198,1100 1098,-1098,2196,1099 1100,-1100,2200,1101 1097,-1097,2194,1098

Degree span vs crossing count
 nucleus    A  max span   steps  2*steps-span
      1H    1        22      12             2
       n    1        20      11             2
      2H    2        46      24             2
      3H    3        68      37             6
     3He    3        74      38             2
     4He    4        98      52             6
     6Li    6       154      84            14
     7Li    7       176     101            26
     9Be    9       240     139            38
     12C   12       354     204            54
     14N   14       434     252            70
     16O   16       522     304            86
    20Ne   20       722     420           118
    24Mg   24       954     552           150
    28Si   28      1218     700           182
     32S   32      1514     864           214
    40Ca   40      2202    1240           278

Bar-symmetry of each coefficient under q -> 1/q  (even / odd / neither)
 nucleus    A  steps%2         γ        σ₀        σ₁        L₊        L₋        e⁻  rule
      1H    1        0      even       odd       odd      even      even       odd  ok
       n    1        1       odd      even      even       odd       odd      even  ok
      2H    2        0      even       odd       odd      even      even       odd  ok
      3H    3        1       odd      even      even       odd       odd      even  ok
     3He    3        0      even       odd       odd      even      even       odd  ok
     4He    4        0      even       odd       odd      even      even       odd  ok
     6Li    6        0      even       odd       odd      even      even       odd  ok
     7Li    7        1       odd      even      even       odd       odd      even  ok
     9Be    9        1       odd      even      even       odd       odd      even  ok
     12C   12        0      even       odd       odd      even      even       odd  ok
     14N   14        0      even       odd       odd      even      even       odd  ok
     16O   16        0      even       odd       odd      even      even       odd  ok
    20Ne   20        0      even       odd       odd      even      even       odd  ok
    24Mg   24        0      even       odd       odd      even      even       odd  ok
    28Si   28        0      even       odd       odd      even      even       odd  ok
     32S   32        0      even       odd       odd      even      even       odd  ok
    40Ca   40        0      even       odd       odd      even      even       odd  ok
  rule: bar-parity of (γ, L₊, L₋) = (-1)^(crossing count), (σ₀, σ₁, e⁻) opposite  ->  holds on every nucleus

Exponent parity per slot  (all-even / all-odd / mixed; 'gaps' = missing rungs)
 nucleus    A             γ            σ₀            σ₁            L₊            L₋            e⁻
      1H    1   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0
       n    1    odd gaps=2   even gaps=2   even gaps=0    odd gaps=2    odd gaps=0   even gaps=0
      2H    2   even gaps=0    odd gaps=0    odd gaps=0   even gaps=1   even gaps=0    odd gaps=0
      3H    3    odd gaps=0   even gaps=0   even gaps=0    odd gaps=2    odd gaps=0   even gaps=0
     3He    3   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0
     4He    4   even gaps=0    odd gaps=2    odd gaps=0   even gaps=0   even gaps=0    odd gaps=2
     6Li    6   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0
     7Li    7    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0
     9Be    9    odd gaps=0   even gaps=2   even gaps=0    odd gaps=2    odd gaps=2   even gaps=0
     12C   12   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0
     14N   14   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0
     16O   16   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0
    20Ne   20   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0
    24Mg   24   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0
    28Si   28   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0
     32S   32   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0
    40Ca   40   even gaps=0    odd gaps=0    odd gaps=0   even gaps=0   even gaps=0    odd gaps=0

BOND SET COMPARISON: the same word with only the pair-bond set changed
  complete = build_atom_nf_sym as written        (C(A,2) crossings)
  chain    = adjacent pairs, as closed_form_ratio (A-1 crossings)
  none     = no pair crossings at all            (the control)
 nucleus    A  complete   chain    none  compl-none  chain-none
      1H    1        22      22      22           0           0
       n    1        20      20      20           0           0
      2H    2        46      46      44           2           2
      3H    3        68      66      66           2           0
     3He    3        74      72      68           6           4
     4He    4        98      96      90           8           6
     6Li    6       154     146     136          18          10
     7Li    7       176     166     158          18           8
     9Be    9       240     216     204          36          12
     12C   12       354     296     274          80          22
     14N   14       434     346     320         114          26
     16O   16       522     396     366         156          30
    20Ne   20       722     496     458         264          38
    24Mg   24       954     596     550         404          46
    28Si   28      1218     696     642         576          54
     32S   32      1514     796     734         780          62
    40Ca   40      2202     996     918        1284          78

Finite differences along the evenly spaced N=Z chain (A = [12, 16, 20, 24, 28, 32, 36, 40], spacing 4)
  complete
    values [354, 522, 722, 954, 1218, 1514, 1842, 2202]
    Δ      [168, 200, 232, 264, 296, 328, 360]
    ΔΔ     [32, 32, 32, 32, 32, 32]
    ΔΔΔ    [0, 0, 0, 0, 0]
    => QUADRATIC in A; leading coefficient = 1
  chain
    values [296, 396, 496, 596, 696, 796, 896, 996]
    Δ      [100, 100, 100, 100, 100, 100, 100]
    ΔΔ     [0, 0, 0, 0, 0, 0]
    ΔΔΔ    [0, 0, 0, 0, 0]
    => LINEAR in A; slope = 25 per nucleon
  none
    values [274, 366, 458, 550, 642, 734, 826, 918]
    Δ      [92, 92, 92, 92, 92, 92, 92]
    ΔΔ     [0, 0, 0, 0, 0, 0]
    ΔΔΔ    [0, 0, 0, 0, 0]
    => LINEAR in A; slope = 23 per nucleon
  pairs-only (complete - none)
    values [80, 156, 264, 404, 576, 780, 1016, 1284]
    Δ      [76, 108, 140, 172, 204, 236, 268]
    ΔΔ     [32, 32, 32, 32, 32, 32]
    ΔΔΔ    [0, 0, 0, 0, 0]
    => QUADRATIC in A; leading coefficient = 1
  pairs-only (chain - none)
    values [22, 30, 38, 46, 54, 62, 70, 78]
    Δ      [8, 8, 8, 8, 8, 8, 8]
    ΔΔ     [0, 0, 0, 0, 0, 0]
    ΔΔΔ    [0, 0, 0, 0, 0]
    => LINEAR in A; slope = 2 per nucleon

The diagnostic, stated as measured
------------------------------------------------------------------------------
   complete bonds -> QUADRATIC in A; leading coefficient = 1
      chain bonds -> LINEAR in A; slope = 25 per nucleon
       none bonds -> LINEAR in A; slope = 23 per nucleon
  => the q-degree SEPARATES the two bond sets live in the corpus: the
     complete graph is quadratic in A while the adjacent-pair chain is
     linear, i.e. the same growth class as no pair bonds at all.

Closed forms on the N=Z chain, checked against every measured point
       none: all match
   complete: all match

Reading
------------------------------------------------------------------------------
  * The six NF coefficients are LAURENT POLYNOMIALS in q, not general
    rational functions: build_atom_nf_sym never touches z or the Wedderburn
    weights, whose (q^2+1) and (q^4+4q^2+1) denominators enter only at the
    trace/volume step.  Every denominator here is a power of q.
  * Every coefficient is bar-EVEN or bar-ODD -- never neither -- and which
    one is fixed by the parity of the crossing count.  The NF vector is
    bar-graded, with {gamma, L+, L-} on one side and {s0, s1, e-} on the
    other.  This is the bar-parity the arc uses, visible on the word.
  * All exponents in a slot share one parity, and for A >= 12 the slot is
    DENSE in that sublattice (gaps=0): the coefficient is q^-D * P(q^2)
    with P of full degree D.  So the degree is not carried by a sparse
    leading term that could cancel downstream.
  * The q-degree is QUADRATIC in A, and the ablation shows the quadratic
    is ENTIRELY the inter-nucleon loop: with that loop off the span is
    exactly linear (23A - 2 on the N=Z chain, second difference 0), and
    the pair crossings alone contribute a term with leading coefficient
    exactly 1 in A^2.  That is a control, not a fit.
  * Consequence for the bk-crossing arc: the braid word this producer
    builds encodes the COMPLETE GRAPH on the nucleons -- the bond set
    QOU.Mass.CoordinationSaturation proves gives B/A = eps*(A-1)/2,
    unbounded, with no plateau.  The q-degree is an algebraic readout of
    which bond set a producer uses, needing no q0, no anchor and no AME.
```
