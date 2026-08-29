---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-002-12-presentation
section_title: "Presentation"
section_number: 1.2
pages: 3-4
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
mine whether the ‘Kauﬀman trace’, that is the Markov trace aﬀording the Kauﬀman poly-
nomial, was indeed the only Markov trace factoring through the BMW-algebra (in addition
to the one factoring to the smaller Hecke algebra quotient). When we tried to answer this
question, we faced another problem. First of all, it is well-known that there are two varia-
tions of the Kauﬀman polynomial, one of them having been given the name of the city of
Dubrovnik. These two variations can be seen as Markov traces, after specialization of the pa-
rametersa,b,c , subject to a polynomial relation a =bc ora =−bc. But they are not Markov
trace on the same BMW-algebra ! More precisely, although the two relevant BMW-algebras
are isomorphic as algebras, they are a priori not the same quotient of the group algebra of
the braid group. Indeed, the additional relation on 3 strands involves a,b,c and depends on
whether a =bc or a =−bc. Viewing the BMW-algebras as centralizer algebras for quantum
groups actions, these two specializations correspond to the diﬀerence between the orthogonal
and symplectic groups (see the end of §3).
Because of this, we tried to dig deeper into the deﬁning relations of the BMW-algebras.
When translated into braid words, the usual additional relation (in both cases), relatingeisjei
and ei for|i−j| = 1, involves 12 terms. We use another relation, that relates s−1
j eis−1
j and
siejsi, involving only 6 terms when expanded into braid words, which holds inside both BMW-
algebras, and which is enough to ensure the ﬁniteness of the dimension. Because of this, we
can deﬁne a ﬁnite-dimensional ‘cover’ of the two BMW-algebras involved in the computation
of the Kauﬀman polynomial, as well as the ortho-symplectic quantum invariants, that we call
~BMW n.
From this we get a satisfying algebraic setup to explore the possible Markov traces for
every single value of the parameters. We prove that, for generic values of the parameters,
this cover is actually isomorphic to the usual BMW-algebras, thus providing in these cases an
even simpler deﬁnition (as a quotient of the group algebra of Bn) of the BMW-algebras (see
4 Ivan Marin & Emmanuel Wagner
propositions 4.4 and 4.5). However, for generic values satifying a2 =y, we ﬁnd that ~BMW 3
has one dimension more than expected.
Concerning Markov traces we ﬁrst get (proposition 5.5) that, when a2⁄= y2 and a2⁄= y
(and actually : also when a2 = y and a2⁄= y2, see proposition 5.7), the only Markov trace
factoring through ~BMW n is the Ocneanu trace, deﬁned on the Hecke algebra quotient.
We specialize to the situation a2 = y2. Then, we have in addition the Kauﬀman trace.
When y⁄= 1, we prove that the only Markov traces factoring through our algebra lead either
to the Kauﬀman polynomial or to the Homﬂy polynomial, and that this algebra is actually
isomorphic to the usual BMW-algebra. When y = 1, that is when a2 = y2 and a2 = y, we
have ﬁrst to exclude a very degenerate case,x =−2a, for which there is an inﬁnite number of
Markov traces, namely the ones factoring through the group algebra of the symmetric group
(see proposition 5.10) ; it is well-known that these ones detect only the number of components
of the links. In the general case y = 1, we get an additional Markov trace t††
n that basically
provides the parity of the number of components of the link. These 3 Markov traces exhaust
all possible traces, and are linearly independent one from the other, for generic x. The special
values for which this does not hold, besides x =−2a, are x =a and x = 2a.
In order to understand what happens in these two special cases, we provide a description
of the algebra ~BMW n when specialized at a2 = y = 1. For this we deﬁne by generators
and relations an algebra over Q [a,x,x−1]/(a2− 1) that we denote Fn. It is a free module of
rank 1 more than the dimension of BMWn (corollary 6.6) and it can be viewed as a central
extension of BMWn by a 1-dimensional ideal spanned by some element that we call C. This
element squares to 0, and therefore the extension cannot split, precisely when x = a and
x = 2a. We prove that it is indeed the specialization we want of ~BMW n, as soon as x⁄=−2a
(theorem 6.8), while the specialization of ~BMW n for the case x =−2a provides a larger
algebra, of which we provide a partly conjectural description (see section 6.8). Finally, we
use the structure of Fn to check that the space of Markov traces factoring through Fn has
dimension at most 3 : there is at most one way to ﬁnd an additional Markov trace in the
special cases x =a and x = 2a.
In passing, we deduce from the existence of Fn a similar central extension ~TLn of the
Temperley-Lieb algebra, which is a subalgebra of Fn. We ﬁnd natural (diagrammatic) inter-
pretations of the two (potential) additional Markovs trace when restricted to this subalgebra.
Finally, we manage to construct the expected additional Markov trace in the case x = 2a by
constructing a central extension of the classical Hecke algebra.
More generally, we prove that, for an arbitrary Coxeter system ( W,S ), the usual Iwahori-
Hecke algebra atq =−1 has a natural non-split central extension, of dimension 1+#W ifW is
ﬁnite, and that there existes a Markov trace on this algebra whenW = Sn (see theorems 6.22
and 6.26). This Markov trace provides what we need. The case x = a remains conjectural,
although we are conﬁdent that the corresponding invariant exists. We guess that an algebraic
proof of the existence of the Kauﬀman trace similar to the one that Jones provided for the
Ocneanu trace should be easy to generalize to our central extension. However it appears that
no one provided such a proof yet, and ﬁnding such a proof seems to us to be quite more tricky
than the Hecke algebra case.
