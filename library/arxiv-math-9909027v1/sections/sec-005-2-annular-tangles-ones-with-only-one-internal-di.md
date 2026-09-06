---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California"
section_id: sec-005-2-annular-tangles-ones-with-only-one-internal-di
section_title: "Annular tangles: ones with only one internal disc, e.g.,"
section_number: 2
pages: 6-13
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
doc_brief: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California — We introduce a notion of planar algebra, the simplest exampl e of which is a vector space of tensors, closed"
---
6
∗
∗
The universal planar algebra is useful for constructing pla nar algebras
and restriction to the two generating tangles sometimes mak es it shorter to
check that a given structure is a planar algebra. The algebra structure we
begin with in §1 corresponds of course to the multiplication tangle given
above.
The original algebra structure has been studied in some deta il (see §3.1)
but it should be quite clear that the operad provides a vast fa mily of algebra
structures on a planar algebra which we have only just begun t o appreciate.
For instance, the annular tangles above form an algebra over which all the
Vk’s in a planar algebra are modules. This structure alone seem s quite rich
([GL]) and we exploit it just a little to get information on pr incipal graphs of
subfactors in 4.2.11. We have obtained more sophisticated r esults in terms
of generating functions which we will present in a future pap er.
We present several examples of planar algebras in §2, but it is the connec-
tion with subfactors that has been our main motivation and gu ide for this
work. The two leading theorems occur in §4. The ﬁrst one shows how
to obtain a planar algebra from a ﬁnite index subfactor N ⊂ M. The
vector space Vk is the set of N-central vectors in the N − N bimodule
Mk−1 = M ⊗N M ⊗N . . . ⊗N M (k copies of M), which, unlike Mk−1 itself,
is ﬁnite dimensional. The planar algebra structure on these Vk’s is obtained
by a method reminiscent of topological quantum ﬁeld theory. Given a planar
k-tangle T whose internal discs are labelled by elements of the Vj’s, we have
to show how to construct an element of Vk, associated with the boundary
of T , in a natural way. One starts with a very small circle (the “bu bble”)
in the distinguished white region of T , tangent to the boundary of D. We
then allow this circle to bubble out until it gets to the bound ary. On its
7
way the bubble will have to cross strings of the tangle and env elop internal
discs. As it does so it acquires shaded intervals which are it s intersections
with the shaded regions of T . Each time the bubble envelops an internal
disc Di, it acquires ki such shaded intervals and, since an element of Vki is
a tensor in ⊗ki
N M, we assign elements of M to the shaded region according
to this tensor. There are also rules for assigning and contra cting tensors as
the bubble crosses strings of the tangle. At the end we have an element of
⊗k
N M assigned to the boundary. This is the action of the operad ele ment
on the vectors in Vki. Once the element of ⊗k
N M has been constructed and
shown to be invariant under diﬀeomorphisms, the formal oper adic properties
are immediate.
One could try to carry out this procedure for an arbitrary inc lusion A ⊂
B of rings, but there are a few obstructions involved in showin g that our
bubbling process is well deﬁned. Finite index (extremal) su bfactors have
all the special properties required, though there are surel y other families of
subrings for which the procedure is possible.
The following tangle:
∗
∗
deﬁnes a rotation of period k (2k boundary points) so it is a consequence
of the planar algebra structure that the rotation x1 ⊗ x2 ⊗ . . . ⊗ xk ↦→x2 ⊗
x3 ⊗ . . . ⊗ xk ⊗ x1, which makes no sense on Mk−1, is well deﬁned on N-
central vectors and has period k. This result is in fact an essential technical
ingredient of the proof of Theorem 4.2.1.
Note that we seem to have avoided the use of correspondences i n the
sense of Connes ([Co1]) by working in the purely algebraic tensor product.
But the avoidance of L2-analysis, though extremely convenient, is a little
illusory since the proof of the existence and periodicity of the rotation uses L2
methods. The Ocneanu approach ([EK]) uses the L2 deﬁnition and the vector
8
spaces Vk are deﬁned as Hom N,N (⊗j
N M) and Hom N,M (⊗j
N M) depending on
the parity of k. It is no doubt possible to give a direct proof o f Theorem 4.2.1
using this deﬁnition - this would be the “hom” version, our me thod being
the “ ⊗” method.
To identify the operad structure with the usual algebra stru cture on Mk−1
coming from the “basic construction” of [J1], we show that th e multiplication
tangle above does indeed deﬁne the right formula. This, and a few similar
details, is suprisingly involved and accounts for some unpl easant looking
formulae in §4. Several other subfactor notions, e.g. tensor product, ar e
shown to correspond to their planar algebra counterparts, a lready abstractly
deﬁned in §3. Planar algebras also inspired, in joint work with D. Bisch ,
a notion of free product. We give the deﬁnition here and will e xplore this
notion in a forthcoming paper with Bisch.
The second theorem of §4 shows that one can construct a subfactor from a
planar algebra with ∗-structure and suitable “reﬂection” positivity. It is trul y
remarkable that the axioms needed by Popa for his constructi on of subfactors
in [Po2] follow so closely the axioms of planar algebra, at le ast as formulated
using boxes and the universal planar algebra. For Popa’s con struction is
quite diﬀerent from the “usual” one of [J1], [F+], [We1], [We 2]. Popa uses
an amalgamated free product construction which introduces an unsatisfac-
tory element in the correspondence between planar algebras and subfactors.
For although it is true that the standard invariant of Popa’s subfactor is
indeed the planar algebra from which the subfactor was const ructed, it is
not true that, if one begins with a subfactor N ⊂ M, even hyperﬁnite, and
applies Popa’s procedure to the standard invariant, one obt ains N ⊂ M as a
result. There are many diﬃcult questions here, the main one o f which is to
decide when a given planar algebra arises from a subfactor of the Murray-von
Neumann hyperﬁnite type II 1 factor ([MvN]).
There is a criticism that has and should be made of our deﬁniti on of a
planar algebra - that it is too restrictive. By enlarging the class of tangles in
the planar operad, say so as to include oriented edges and bou ndary points,
or discs with an odd number of boundary points, one would obta in a notion of
planar algebra applicable to more examples. For instance, i f the context were
the study of group representations our deﬁnition would have us studying say,
9
SU(n) by looking at tensor powers of the form V ⊗ ¯V ⊗ V ⊗ ¯V . . . (where V
is the deﬁning representation on Cn)
whereas a full categorical treatment would insist on arbitr ary tensor prod-
ucts. In fact, more general notions already exist in the lite rature. Our planar
algebras could be formulated as a rather special kind of “spi der” in the sense
of Kuperberg in [Ku], or one could place them in the context of pivotal and
spherical categories ([FY],[BW]), and the theory of C ∗−tensor categories
even has the ever desirable positivity ([LR],[We3]). Also, in the semisimple
case at least, the work in section 3.3 on cabling and reductio n shows how to
extend our planar diagrams to ones with labelled edges.
But it is the very restrictive nature of our deﬁnition of plan ar algebras
that should be its great virtue. We have good reasons for limi ting the gen-
erality. The most compelling is the equivalence with subfac tors, which has
been our guiding light. We have tried to introduce as little f ormalism as pos-
sible compatible with exhibiting quite clearly the planar n ature of subfactor
theory. Thus our intention has been to give pride of place to t he pictures.
But subfactors are not the only reason for our procedure. By r estricting the
scope of the theory one hopes to get to the most vital examples as quickly
as possible. And we believe that we will see, in some form, all the examples
in our restricted theory anyway. Thus the Fuss-Catalan alge bras of [BJ2]
(surely among the most basic planar algebras, whatever one’ s deﬁnition)
ﬁrst appeared with our strict axioms. Yet at the same time, as we show
in section 2.5, the homfly polynomial, for which one might have thought
oriented strings essential, can be completely captured wit hin our unoriented
framework.
It is unlikely that any other restriction of some more genera l operad is as
rich as the one we use here. To see why, note that in the operadi c picture, the
role of the identity is played by tangles without internal discs -see [Ma]. In our
case we get the whole Temperley-Lieb algebra corresponding to the identity
whereas any orientation restriction will reduce the size of this “identity”.
The beautiful structure of the Temperley-Lieb algebra is th us always at our
disposal. This leads to the following rather telling reason for looking carefully
at our special planar algebras among more general ones: if we introduce the
generating function for the dimensions of a planar algebra, ∑ ∞
n=0 dim(Vn)zn,
10
we shall see that if the planar algebra satisﬁes reﬂection po sitivity, then this
power series has non-zero radius of convergence. By contras t, if we take the
natural oriented planar algebra structure given by the homfly skein, it is
a result of Ocneanu and Wenzl ([We1],[F+]) that there is a pos itive deﬁnite
Markov trace on the whole algebra, even though the generatin g function has
zero radius of convergence.
In spite of the previous polemic, it would be foolish to negle ct the fact that
our planar algebra formalism ﬁts into a more general one. Sub factors can be
constructed with arbitrary orientations by the procedure o f [We1],[F+] and
it should be possible to calculate their planar algebras by p lanar means.
We end this introduction by discussing three of our motivati ons for the
introduction of planar algebras as we have deﬁned them.
Motivation 1 Kauﬀman gave his now well-known pictures for the Temperley-
Lieb algebra in [Ka1]. In the mid 1980’s he asked the author if it was possible
to give a pictorial representation of all elements in the tow er of algebras of
[J1]. We have only developed the planar algebra formalism fo r the sub-
tower of relative commutants, as the all-important rotatio n is not deﬁned on
the whole tower. Otherwise this paper constitutes an answer to Kauﬀman’s
question.
Motivation 2 One of the most extraordinary developments in subfactors
was the discovery by Haagerup in [Ha] of a subfactor of index ( 5 +
√
13)/2,
along with the proof that this is the smallest index value, gr eater than 4,
of a ﬁnite depth subfactor. As far as we know there is no way to o btain
Haagerup’s “sporadic” subfactor from the conformal ﬁeld th eory/quantum
group methods of [Wa],[We3],[X],[EK]. It is our hope that th e planar algebra
context will put Haagerup’s subfactor in at least one natura l family, besides
yielding tools for its study that are more general than those of [Ha]. For
instance it follows from Haagerup’s results that the planar algebra of his
subfactor is generated by a single element in V4 (a “4-box”). The small di-
mensionality of the planar algebra forces extremely strong conditions on this
4-box. The only two simpler such planar algebras (with reﬂec tion positivity)
are those of the D6 subfactor of index 4 cos 2 π/10 and the ˜E7 subfactor of
index 4. There are analogous planar algebras generated by 2- boxes and 3-
boxes. The simplest 2-box case comes from the D4 subfactor (index 3) and
11
the two simplest 3-box cases from E6 and ˜E6 (indices 4 cos 2 π/12 and 4).
Thus we believe there are a handful of planar algebras for eac h k, generated
by a single k-box, satisfying extremely strong relations. C ommon features
among these relations should yield a uniﬁed calculus for con structing and
manipulating these planar algebras. In this direction we ha ve classiﬁed with
Bisch in [BJ1] all planar algebras generated by a 2-box and tightly restricted
in dimension. A result of D.Thurston shows an analogous resu lt should exist
for 3-boxes - see section 2.5. The 4-box case has yet to be atte mpted.
In general one would like to understand all systems of relati ons on planar
algebras that cause the free planar algebra to collapse to ﬁn ite dimensions.
This is out of sight at the moment. Indeed it is know from [BH] t hat sub-
factors of index 6 are “wild” in some technical sense, but up t o 3 +
√
3 they
appear to be “tame”. It would be signiﬁcant to know for what in dex value
subfactors ﬁrst become wild.
Motivation 3 Since the earliest days of subfactors it has been known
that they can be constructed from certain ﬁnite data known as a commuting
square (see [GHJ]). A theorem of Ocneanu (see [JS] or [EK]) re duced the
problem of calculating the planar algebra component Vk of such a subfactor to
the solution of a ﬁnite system of linear equations in ﬁnitely many unknowns.
Unfortunately the number of equations grows exponentially with k and it is
unknown at present whether the most simple questions concer ning these Vk
are solvable in polynomial time or not. On the other hand the p lanar algebra
gives interesting invariants of the original combinatoria l data and it was a
desire to exploit this information that led us to consider pl anar algebras.
First it was noticed that there is a suggestive planar notati on for the linear
equations themselves. Then the invariance of the solution s pace under the
action of planar tangles was observed. It then became clear t hat one should
consider other ways of constructing planar algebras from co mbinatorial data,
such as the planar algebra generated by a tensor in the tensor planar algebra.
These ideas were the original motivation for introducing pl anar algebras.
We discuss these matters in more detail in section 2.11 which is no doubt the
most important part of this work. The signiﬁcance of Popa’s r esult on λ−
lattices became apparent as the deﬁnition evolved. Unfortu nately we have
not yet been able to use planar algebras in a convincing way as a tool in the
12
calculation of the planar algebra for speciﬁc commuting squ ares.
This paper has been written over a period of several years and many
people have contributed. In particular I would like to thank Dietmar Bisch,
Pierre de la Harpe, Roland Bacher, Sorin Popa, Dylan Thursto n, Bina Bhat-
tacharya, Zeph Landau, Adrian Ocneanu, Gib Bogle and Richar d Borcherds.
Deborah Craig for her patience and ﬁrst-rate typing, and Tsu kasa Yashiro
for the pictures.
