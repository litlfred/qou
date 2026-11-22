---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-075-critical-points-at-infinity
section_title: "Critical points at infinity"
section_number: null
pages: 447-448
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
429
Degeneracies of phase can also, in principle, be handled by resolving singu-
larities to obtain a normal crossing, using a change of coordinates mapping the
phase function into a monomial, expanding the resulting amplitude function
into a power series, and then applying known exact asymptotics to each term.
Resolution of singularities, together with the methods of [Var77], implies that
the possible asymptotic behaviors for any rational asymptotics fall in a limited
set of leading terms.
13.4 Critical points at inﬁnity
Let T = T(x), where x is in some component B of the complement of the
amoeba of the denominator Q of some rational function. As seen in Chapter 7,
non-existence of CPAI in the direction ˆr is a suﬃcient condition for [T] to be
representable as the sum of cycles corresponding to attachments at aﬃne criti-
cal points in direction ˆr. However, this non-existence is by no means necessary.
For instance,
• The trajectories ﬂowing to a CPAI may not be trajectories of any stratiﬁed
gradient-like ﬂow.
• A trajectory ﬂowing to a CPAI may be a gradient-like ﬂow, but the particular
torus [T] may ﬂow down to an aﬃne critical point and not be pulled down a
path leading to this CPAI.
• [T] may not ﬂow down without being pulled to inﬁnity, but there may be a
cobordism between T and a cycle lower than any CVAI.
• Even if [T] is pulled to inﬁnity by some gradient-like vector ﬁeld, the CPAI
there may not alter the topology and it might be possible to deform [T] to
“come back from inﬁnity.”
Problem 13.3. a) Can there be unreachable CPAI, meaning that there is a
downward gradient-like ﬁeld that has no ﬂows reaching a CPAI?
b) If so, how can we compute which CPAI are like this?
c) Do all CPAI alter the topology of V∗? Is there an attachment theory for
CPAI, giving a way to compute the topological eﬀect of each CPAI?
d) If there is a local attachment, can we ﬁnd a cycle α representing it and
determine
R
α z−r−1F(z) dz?
Another useful tool would be the capability to rule out the existence of CPAI
in some direction without an overly long computer algebra computation. An
early conjecture, which turned out not to be true, was that all CPAI must be
parallel to some face of the Newton polytope of Q. Some ongoing work proves
430
Challenges and extensions
that this conjecture is true when the polytope is sch¨on, a property deﬁned in
terms of compactiﬁcations via toric varieties [Huh13, Deﬁnition 3.6]. The set
of directions parallel to a face of the Newton polytope is a small set (it has
positive codimension) so it is useful to know when CPAI are restricted to these
directions. Generally, we would like to ﬁnd computable restrictions on the pos-
sible directions of CPAI.
