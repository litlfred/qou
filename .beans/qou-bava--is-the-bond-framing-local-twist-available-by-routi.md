---
# qou-bava
title: Is the bond framing local? Twist available by routing width
status: completed
type: task
priority: normal
created_at: 2026-09-02T21:33:43Z
updated_at: 2026-09-02T21:37:46Z
---


RESOLVED 2026-09-02 -- computations/probes/bond_framing_is_local_and_inverted_probe.py,
6/6. Closes qou-3s5e's embedding caveat, and MORE SHARPLY than the caveat was
posed. Also turns up an inversion.

FRAMING IS LOCAL. In a ribbon category the twist is a property of an OBJECT, and
a morphism's framing correction involves only the strands it acts on. A bond is
supported on the strands its routing touches, so it can carry only the twists of
B_w for that width -- whatever the ambient braid does elsewhere. The ambient
Coxeter element c_n is not localised to the bond and cannot be attributed to it.

WIDTH, READ OFF THE PRODUCTION CODE. band_between(i,j) uses generators
3i+2 .. 3j-1, hence strands 3i+2 .. 3j, so for separation k:

    w = 3k - 1     (verified for k = 1..6, not assumed)

AVAILABLE ASYMMETRY BY SEPARATION:

    sep k   width w   admissible t at n=w            achievable ratios
    1        2        NONE                            none
    2        5        4/5                             9
    3        8        1/2                             3
    4       11        2/11, 4/11, 8/11, 10/11         13/9, 15/7, 19/3, 21
    5       14        1/7, 2/7, 3/7, 4/7, 5/7         4/3, 9/5, 5/2, 11/3, 6
    6       17        2/17, 4/17, 6/17, 8/17, ...     19/15, 21/13, 23/11, ...

THE CAVEAT CLOSES. The deuteron's bond is ADJACENT -- separation 1, width 2 --
and B_2 offers only t = 1, the excluded boundary where the T=0 channel unbinds
and the ratio diverges. A free two-nucleon system has no wider routing to borrow
from, because there is nothing else in it.

So the two-nucleon impossibility stands for a LOCAL reason: not "the substrate
has no twist" but "a two-strand-supported bond cannot carry one". THAT IS
STRONGER than qou-3s5e's per-n statement, because it survives embedding the pair
in anything.

AND THE STRUCTURE IS INVERTED. The substrate supplies channel asymmetry to bonds
between DISTANT nucleons and NONE AT ALL to adjacent ones. Physics is the other
way round -- the nearest-neighbour interaction is the strong one and distant
pairs are weakly coupled.

This interacts with an earlier result. no_distance_decay_in_the_trace_probe found
four band routings of a separation-2 bond agreeing with the ADJACENT value to
5.6e-16, extended to separation 3 in qou-38i9 (3.4e-13). So the bond's own TRACE
is separation-INDEPENDENT while its available FRAMING is separation-DEPENDENT.
In this construction the framing is the ONLY thing distinguishing a near bond
from a far one -- and it is the one thing that gets the direction wrong.

CAVEATS, carried in the witness:
 - "framing is local" is a READING of the corpus's (1-h)^(e/2) factor in
   ribbon-category terms. Standard, and it is what makes the width argument work,
   but no ribbon structure is constructed and the locality is not verified
   against the corpus's own framing code. A non-local framing assignment would
   not be bound by this.
 - NO BINDING ENERGY IS MEASURED. This establishes which twists a bond of given
   separation COULD carry, from routing width and the Coxeter spectrum. Nothing
   attaches a twist to a bond in an atom word or recomputes a trace.
 - w = 3k-1 is specific to the production band routing. A different routing of
   the same topological bond spans a different width and admits different
   twists -- which is itself notable, since qou-38i9 showed four routings give
   IDENTICAL trace. Routing-independence of the trace and routing-DEPENDENCE of
   the available framing sit together uncomfortably and are NOT reconciled here.
