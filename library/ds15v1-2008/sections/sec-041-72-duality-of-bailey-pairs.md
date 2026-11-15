---
doc_id: ds15v1-2008
doc_title: "Rogers-Ramanujan-Slater Type Identities"
section_id: sec-041-72-duality-of-bailey-pairs
section_title: "Duality of Bailey pairs"
section_number: 7.2
pages: 52-53
source_pdf: ds15v1-2008.pdf
source_sha256: aef155a324c6fdf4
toc_source: inferred
---
We recall that Andrews showed in [5] that if (αn(a, q), βn(a, q)) is a Bailey pair relative
to a, then (α∗
n(a, q), β∗
n(a, q)) is also a Bailey pair relative to a, where
α∗
n(a, q) = anqn2αn(1/a, 1/q),
β∗
n(a, q) = a−nq−n2−nβn(1/a, 1/q).
The pair (α∗
n(a, q), β∗
n(a, q)) is called the dual of (αn(a, q), βn(a, q)). Note that the dual
of (α∗
n(a, q), β∗
n(a, q)) is (αn(a, q), βn(a, q)). Identities that arise from Bailey pairs that are
duals of each other may be regarded in some sense as being related, so for completeness
sake we give a table that matches Bailey pairs with their duals.
Before giving this table, we make some comments. Firstly, Slater’s list of Bailey pairs
contains several pairs whose duals are not listed, so we list the new Bailey pairs that are
dual to these. Secondly, some pairs, such as H7 and E2 are in fact the same pair, and
we indicate the occurrence of such identical pairs. Thirdly, Slater’s list of Bailey pairs
contains a good many typographic errors. Sometimes retracing Slater’s steps (making the
same choices that she did for the parameters in the identities she used to derive the Bailey
pairs) will recover the correct Bailey pair, but this does not always work as in several cases
Slater employs an additional unstated manipulation to derive the Bailey pair(for example,
the same choice of parameters give rise to pairs B1 and B2, but only B1 follows directly
from substituting these values into Equation (4.1) of [40]).
In this latter case we can insert the stated sequence αn(a, q) (under the assumption
that the stated value for αn(a, q) is correct, and that the error is in the stated value for
the electronic journal of combinatorics 15 (2008), #DS15
52
βn(a, q)) into the equation
βn(a, q) =
n
X
r=0
1
(q; q)n−r(aq; q)n+r
αr(a, q),
(7.2.1)
use Mathematica to compute βn(a, q) for low values of n and hopefully recognize the form
of βn(a, q) for arbitrary n. If this does not work, then we try substituting the stated value
for βn(a, q) into (7.2.1), and use Mathematica to compute successive values for αn(a, q),
again try to ﬁnd the formula for αn(a, q). Of course there is the possibility that the pair
derived in this way is not the pair Slater intended. This could happen if, for example,
Slater incorrectly stated αn(a, q), but this αn(a, q) is part of an entirely diﬀerent Bailey
pair, so that the attempt to ﬁnd Slater’s correct pair would instead ﬁnd the other Bailey
pair (for example, Slater lists the same αn(a, q) for both F1 and H1, and assuming that
the αn(a, q) in H1 is correct would lead to a Bailey pair diﬀerent from what Slater had
in mind for H1).
