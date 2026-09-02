# bridge_generator_index_probe — full output (2026-08-31)

Verbatim run. Regenerate with:

    python3 -u computations/bridge_generator_index_probe.py

```
bridge_generator_index_probe
==============================================================================
Diffing atom_braid_word_3A(include_inter=False) against (=True): the
generators the inter-nucleon bridges occupy, read off the producer.

 nucleus   A  strands                  bridge generators  count  = A-1  = 3k+2
      2H   2        6                                [2]      1    yes     yes
      3H   3        9                             [2, 5]      2    yes     yes
     3He   3        9                             [2, 5]      2    yes     yes
     4He   4       12                          [2, 5, 8]      3    yes     yes
     6Li   6       18                  [2, 5, 8, 11, 14]      5    yes     yes
     7Li   7       21              [2, 5, 8, 11, 14, 17]      6    yes     yes
     9Be   9       27      [2, 5, 8, 11, 14, 17, 20, 23]      8    yes     yes
     12C  12       36 [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32]     11    yes     yes

  every bridge at 3k+2, k = 0..A-2 : True
  exactly A-1 bridges              : True

Which generators of a 3A-strand braid cross a nucleon boundary?
  block(m) = m // 3 ; sigma_m swaps strands m, m+1.
   A             crossing gens (m//3 != (m+1)//3)  all m%3==2  all consecutive
   2                                          [2]        True             True
   3                                       [2, 5]        True             True
   4                                    [2, 5, 8]        True             True
   6                            [2, 5, 8, 11, 14]        True             True
  10            [2, 5, 8, 11, 14, 17, 20, 23, 26]        True             True
  layout claim holds on every A tried: True

Reading
------------------------------------------------------------------------------
  * The producer places its inter-nucleon bridges at 3k+2 for
    k = 0..A-2 -- exactly the generators that cross a nucleon
    boundary, and exactly A-1 of them.
  * Every boundary-crossing generator joins CONSECUTIVE nucleons.
    So under this layout the chain is not one bond set chosen among
    others: it is the only one expressible as single crossings.  A
    non-adjacent bond would need a word transporting strands past
    each other, which this producer does not write.
  * Proved for all A, not just those tabulated, in
    QOU.Mass.StrandLayoutForcesChain (crossesBlocks_iff,
    adjacent_of_crosses, no_single_generator_joins_nonadjacent).
  * Consequence: the layout is a LINEAR ORDER on nucleons, so the
    chain bond set and the nucleon-ordering convention are the SAME
    unlicensed choice -- merging this question into qou-48is, where
    the ordering is measured to move tr_M by O(10 %) at A >= 3.
```

## Lean verification

`lean`-direct against the real Mathlib import cone, exit 0 with zero output;
`#print axioms` on all five declarations:

```
'QOU.Mass.StrandLayoutForcesChain.crossesBlocks_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
'QOU.Mass.StrandLayoutForcesChain.adjacent_of_crosses' depends on axioms: [propext, Quot.sound]
'QOU.Mass.StrandLayoutForcesChain.no_single_generator_joins_nonadjacent' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'QOU.Mass.StrandLayoutForcesChain.bridge_crosses' depends on axioms: [propext, Classical.choice, Quot.sound]
'QOU.Mass.StrandLayoutForcesChain.bridge_joins_consecutive' depends on axioms: [propext, Quot.sound]
```

No `sorryAx` — the three listed are the standard Mathlib axioms.
