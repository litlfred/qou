---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-001-11-context
section_title: "Context"
section_number: 1.1
pages: 1-3
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
1.2. Presentation 3
1.3. Organisation of the paper 4
2. Preliminaries on the cubic Hecke algebras on 3 strands 5
3. Two BMW algebras as quotients of the braid groups 8
4. A universal cover for the two BMW algebras, and a shorter deﬁning relation 13
Date: July 17, 2014.
1
arXiv:1403.4021v2  [math.GT]  20 Jul 2014
2 Ivan Marin & Emmanuel Wagner
5. Traces on ~BMW n 19
5.1. General inductive properties 19
5.2. Restrictions to 3 strands, and the Ocneanu trace 21
5.3. The Kauﬀman trace 22
5.4. An additional trace when y =a2 = 1 23
6. A central extension of BMW 24
6.1. Deﬁnition 24
6.2. A genuine extension of BMW±
n 26
6.3. The algebra Fn as a specialization of ~BMW n 27
6.4. Computations inside Fn 32
6.5. A central extension of the Temperley-Lieb algebra 32
6.6. Splittings 35
6.7. A central extension of the ( −1)-Hecke algebras 36
6.8. The case x =−2a 41
7. Knot invariants 42
7.1. Number of connected components, special trace and change of variables 42
7.2. The special case a =±1, b =∓j, c =∓j2 43
7.3. The special case a =b =c =±1 43
7.4. Tables 44
References 46
1. Introduction
1.1. Context. When the Jones and Homﬂy polynomial appeared, they were ﬁrst described as
Markov traces on the group algebra of the braid group, and therefore as invariants of oriented
links produced by the virtue of Markov theorem. Indeed this theorem says that an invariant
of oriented links is the same thing as a Markov trace on the tower of the group algebra
of the braid group. This approach has had a great descent, on the existence of quantum
invariants originating from a quantum trace, in the study of Markov traces on generalized
Hecke algebras, and the Khovanov homology in more recent years has a description in terms
of Soergel bimodules that can be seen as part of the same thread of thinking.
On the other hand, the construction of its cousin the Kauﬀman polynomial has a very
diﬀerent story. Indeed this polynomial was ﬁrst described as an invariant of regular isotopy
by way of unoriented skein relations, and then turned into an invariant of (oriented) links
by twisting the invariant of regular isotopy of the underlying unoriented link by the writhe
of the link. This approach was shown to be also applicable to the Jones polynomial (and
later on used in the deﬁnition of Khovanov homology) through the Kauﬀman bracket, whose
description involves unoriented skein relations.
Conversely, there has been very soon an attempt to describe the Kauﬀman polynomial
in terms of Markov traces. This lead to the deﬁnition, independently by Murakami and
Birman-Wenzl, of the BMW-algebra. This algebra however, in spite of the quantum moto
describing both the Hecke and BMW algebra as ‘quantizations’ of the symmetric group and
of the Brauer algebra respectively, and therefore as quantizations of the centralizer algebras
of the tensor powers of the standard modules of the most classical Lie algebras sln and
son/spn, never reached the level of recognition of the Hecke algebra. As a sample test for
MARKOV TRACES ON THE BMW-ALGEBRAS 3
a not so nice behavior, a completely satisfactory ‘categoriﬁcation’ is still lacking, and the
known generalizations of this algebra to other Coxeter or complex reﬂection groups have
ﬂatness issues (as modules over the natural ring attached to this context). The most natural
description of the BMW-algebra is probably as an algebra of unoriented tangle diagrams,
following the original work of Kauﬀman. Then, BMWn can be described as an homomorphic
image of the group algebra of the braid group, by converting a given braid into a non-
oriented tangle. Describing the kernel of this map as a ﬁnite set of meaningful relations
presenting BMWn as a quotient is the next natural goal. Following the insight given by
the tangle picture, relations on 2 strands are easily found to be given by a cubic relation
(si−a)(si−b)(si−c) on the Artin generators, hence BMWn belongs to the family of cubic
quotients of the group algebra of the braid group Bn. In the sequel we will denote x =b +c
andy =bc since most deﬁnitions involving the BMW-algebras are symmetric in b,c (but not
in a,b,c !). We will also assume x⁄= 0 which is necessary in order to express the elementary
tanglesei as linear combinations of braids. As opposed to the quadratic quotients, for which
the Hecke algebra provides a universal ﬁnite-dimensional model, the ‘cubic Hecke algebra’
does not enjoy universal ﬁniteness properties, because the factor group Bn/s3
i is inﬁnite for
n≥ 6. There are thus additional relations on 3 strands, and it turns out that these relations
on 3 strands are enough to deﬁne the BMWn algebras for every single n.
