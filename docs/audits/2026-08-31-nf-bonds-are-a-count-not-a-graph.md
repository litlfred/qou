# nf_inter_nucleon_is_a_count_not_a_graph_probe — full output (2026-08-31)

Verbatim run. Regenerate with:

    python3 -u computations/substrate/nf_inter_nucleon_is_a_count_not_a_graph_probe.py

```
nf_inter_nucleon_is_a_count_not_a_graph_probe
==============================================================================
Every inter-nucleon factor in build_atom_nf_sym is at gen 0, for every
pair.  All such factors are polynomials in the same generator, so they
commute, so the product can depend only on the MULTISET of types.

TEST 1 — order-invariance.  Start from the real atom NF with no pair
bonds, then apply the same type multiset in many random orders.
  nucleus   A  bonds     (pp,pn,nn)   shuffles identical
      4He   4      6      (1, 4, 1)                40/40
      6Li   6     15      (3, 9, 3)                40/40
      9Be   9     36    (6, 20, 10)                40/40
      12C  12     66   (15, 36, 15)                40/40
      14N  14     91   (21, 49, 21)                40/40
  every shuffle bit-identical on every nucleus: True

TEST 2 — structure-invariance.  Two DIFFERENT graphs on the same
nucleons with the same type counts, and one with different counts.
                                  bond set  span(gamma)               identical to
           complete graph, C(6,2)=15 edges          152                   -- (new)
          degree-4 graph, 12 edges (5,4,3)          146                   -- (new)
    SAME counts (5,4,3), different pairing          146 degree-4 graph, 12 edges (5,4,3)
  same type counts, different pairing -> identical : True
  different type counts               -> differ    : True

Reading
------------------------------------------------------------------------------
  * The inter-nucleon block of build_atom_nf_sym is a product of
    COMMUTING factors, so it depends on the bond set only through
    (n_pp, n_pn, n_nn).  The bond SET is only ever a bond COUNT.
  * So 'complete graph vs bounded degree' is expressible in this
    producer only as a difference in COUNT.  A degree-k graph and the
    complete graph differ solely by having different type counts,
    never by their structure -- measured above.
  * Consequence for qou-brng: a coordination NUMBER cannot be derived
    from this word's geometry, because this word has no geometry in
    its inter-nucleon block.  #6345 asked for a k derived from the
    substrate and then compared to the plateau; this producer cannot
    supply one, and that is a property of the encoding, not a gap in
    anyone's search.
  * Where the geometry DOES live: atom_braid_word_3A places its
    pp/nn/pn crossing at gen 3k+2, a bridge between strand blocks k
    and k+1.  Adjacent-only, hence A-1 bonds by CONSTRUCTION rather
    than by choice.  That is the word to ask geometric questions of.

  Scope (a): about what the current encoding can represent.  Nothing here
  says the framework cannot have a coordination graph, and nothing here
  touches atom_braid_word_3A.
```
