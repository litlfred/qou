---
doc_id: black-samson-phd2010sp
doc_title: "REPRESENTATIONS OF HECKE"
section_id: sec-008-12-summary-of-thesis
section_title: "Summary of Thesis"
section_number: 1.2
pages: 11-22
source_pdf: Black_Samson_phd2010sp.pdf
source_sha256: c16799b0bd54ff29
doc_brief: "REPRESENTATIONS OF HECKE — 19 sections: Acknowledgments; INTRODUCTION 1; SCHUR-WEYL DUALITY AND QUOTIENTS O"
---
In this dissertation, we consider a third alternative, indirectly related to the g[(111)­
approach, but we work only with braids, which is Jones' approach via Markov traces ([24]). There
is essentially no loss of generality, as any link has a diagram presenting it as the closure of a braid.
In Chapter II, we recall some of the basics regarding links, braids, and invariants. The
HOMFLYPT polynomial is constructed from representations of the braid group, factoring through
the Iwahori-Hecke algebra Hd (as in [24], although our notations are substantially different). Also,
a converse is presented: an invariant of links defined on braids that satisfies a skein relation
necessarily factors through the Hecke algebra. This latter perspective, namely that skein relations
determine certain algebras, is a motivation for the results in Chapter III. The remainder of the
chapter is devoted to a particular example: the Jones polynomial. We introduce the Temperley­
Lieb algebra T Ld, both as an explicit quotient of the Hecke algebra and as a diagrammatic algebra
carrying a particularly elegant trace. There are no new results here beyond the considerable task
of gathering this wealth of constructions and formulae into one consistent notational framework.
The groundwork is laid for the following chapters where certain analogous results are derived for
the Alexander polynomial.
In Chapter III, we look at special cases of Schur-Weyl duality between H d and Uv(g[(mln))
on tensor space. In particular, the representations of the Heeke algebra from Chapter II are
explicitly connected to the Reshetikhin- Turaev intertwiners. The Temperley-Lieb algebra appears
here as the centralizer algebra ofUv(g) in End(VI8J·· 'I8JV) for g[(210) = g[(2), or equivalently .5[(2).
Hence, using results of Jimbo ([21] and [22]), building on the classical work of Schur ([38]) and
Weyl ([41, Chapter III]), TL d is presented as a product of matrix algebras indexed by partitions
of at most two rows. As the Wedderburn components for Young diagrams of more than two rows
form a cellular ideal in Hd' the quotient T Ld inherits the cellular structure from Hd. In fact, T Ld
has a natural diagram basis that is easy to express in terms of the standard basis for Hd; hence,
4
the Markov trace on nd that produces the Jones polynomial can be calculated diagrammatically.
The Kauffman state-sum for the Jones polynomial comes directly from this formalism for TLd .
One of the goals of this work, only partially realized, is to find an analogous formalism for the
Alexander polynomial.
Alas, the story for the Alexander polynomial is not so simple. The Super Temperley-Lieb
algebra STL d is defined as the intertwiner algebra for the quantum group associated to g[(111).
Hence, the Markov trace on nd giving the Alexander polynomial on braids factors through STLd.
This algebra has Wedderburn components indexed by hook partitions. However, the ideal that
consists of components that are not hooks is not cellular in the dominance order on partitions, and
so ST Ld does not inherit the cellular structure from nd and the map nd --» ST Ld is quite subtle.
\Ve can obtain a basis for ST Ld' but it has no clear connection to the standard basis for nd, and so
it is not obvious how to calculate the Markov trace directly. In fact, because the transition matrix
from the standard basis for nd to our basis for ST Ld is only defined upon extending scalars to iQl(v),
it is no longer clear that the Alexander invariant is a Laurent polynomial in Z[v,V-I]. The main
result in this section is a presentation of the relations for ST Ld using some of the combinatorics
of the symmetric group adapted to nd.
This is why in Chapter IV we start again using Young's seminormal form for nd. To
begin, STL d is presented as a diagram algebra in the basis of matrix units of its Wedderburn
components. As a result, a lot of complicated information is packaged in the idempotents in nd
that project onto ST Ld. Using character formulas of Geck and Jacon ([16], [17]) for the irreducible
representations of nd and building upon the work of Jones ([24]), a combinatorial procedure is
deduced for calculating the trace, and hence the Alexander polynomial, from a braid diagram
directly. This state-sum has the appeal of being computable in terms of certain labeled diagrams
(the basis for ST Ld) that come from resolving crossings in the original braid. The trade-off for
changing basis so drastically is the aforementioned difficulty that the formula gives the Alexander
polynomial as a sum of rational functions involving quantum integers, obscuring the fact that the
invariant is actually a Laurent polynomial.
In Chapter V, we reprove the main theorem combinatorially. By analyzing possible states
in the expansion of a braid diagram, we are able to check invariance under the Markov moves
directly. Moreover, agreement with the Alexander polynomial is verified. This "naive" proof has
an unexpected advantage: it may be possible to extend the state-sum formula to the multivariable
5
Alexander polynomial using colored braids, as in the work of Murakami ([33]), using the combi­
natorics directly. In a different direction, we hope to recover the Alexander invariant for virtual
links ([27]) as a state-sum in an analogous fashion.
6
CHAPTER II
BRAIDS, LINKS, AND THE JONES POLYNOMIAL
ILL Links and Braids
II.l.l. Links
We recall some standard notions and establish some conventions (see [25, chapter 2] or [10,
chapter 1] for details). A link is a smooth embedding SI u· .. U SI ----> S3. Whenever it is convenient
and does not cause confusion, we also refer to the image of the embedding as the link. All links
are oriented. A link with one component is called a knot. An isotopy of links is a smooth path in
the space of embeddings, or equivalently a smooth embedding (SI U ... U SI) x I ----> S3. Isotopy
forms an equivalence relation whose equivalence classes are called link types. For our purposes, a
link invariant is a function on link types taking values in a ring.
A link diagram is a four-valent graph embedded in S2 along with the choice of over- and
under-crossing strands at each vertex. An isotopy of link diagrams is an isotopy of the underlying
graphs that preserves the crossing data. By compactness, we may assume that the diagram embeds
into a disk in lR?2 (which is how links are usually drawn), but we allow for isotopies of link diagrams
that utilize the connectivity of the sphere S2. A link diagram specifies a link type in a natural way:
compose the planar embedding of the link diagram with the standard embedding lR?2 '----> lR?3 and
locally perturb the two strands at each crossing in opposite directions normal to the plane. Thus,
we have a well-defined surjective map called realization V ----> 12, where V is the set of link diagrams
up to planar isotopy and £ is the set of link types. Using standard transversality arguments, there
exist generic projections JR3 ----> II, where II is a plane, under which the image of a link is a link
diagram (there are only finitely many transverse double points). Thus, we have sections £ ---->V of
the realization map. The fibers of the realization map are described by Reidemeister's theorem.
Theorem 11.1.1. Two link diagrams realize isotopic links if and only if they are related by a
7
sequence of planar isotopies and the following three local moves:
(R I) P " "110
(R II)
(R III)
II. 1. 2. Braids
There are many equivalent ways to define braids (see, e.g. [7] or [25, chapter 1]). A
geometric braid with d strands is a smooth embedding of of d disjoint arcs in ]R2 x [0, 1] such
that the endpoints of each strand have coordinates (i, 0, 0) and (7l"(i),0,1) for some permutation
7l" E Sd and the height function (projecting onto the third coordinate) has no critical points. Bya
geometric braid isotopy, we mean an isotopy of the ambient Euclidean space keeping the endpoints
of the strands fixed. When we speak of a braid, we mean an isotopy class of geometric braids. Let
Bd denote collection of braids on d strands.
By analogy with link diagrams, we consider geometric braid diagrams consisting of im-
mersed arcs in the strip ]R x [0, 1] connecting points (i, 0) to (7l"(i), 1) for i = 1, ... , d satisfying
the conditions that projection onto the second coordinate has no critical points and that self-
intersections are transverse. Each transverse double point in a geometric braid diagram is called a
cTOssing and carries with it the data of which strand passes over and which strand passes under.
There is an appropriate notion of isotopy of geometric braid diagrams that allows one to speak
simply of braid diagrams, meaning isotopy classes.
Braids naturally carry the structure of a group whose operation is given by placing dia-
grams on top of one another. We now define the braid group abstractly, following Artin [3]. Fix
d :::: 1. Let I:d = {erl, ... , erd-l} be the set of braid generators, and let I:;; denote the set of words
in the symbols I:d U I:dl. Then, Bd is the braid group on d strands, that is, the quotient of the
---- -----_.~-------
8
free group on ~d by the relations
O"jO"i when Ii - jl > 1.
For each d, there is a canonical map ~d ---» Bd . The map e : Bd ---> Z, O"i f-+ 1 induces an
isomorphism of groups Bd/[Bd, Bd] ---> Z. The image of 0 under Bd ---> Z is called the exponent sum
of o. Also there is a map Bd ---> .c, 0 f-+ 0, defined by closing a braid into a link by connecting the
top of strand i to the bottom of strand i for each i (see Figure II.1.2).
Figure 11.1: A diagram of the braid 0 = 0"210"i and its closure o.
Alexander showed in [2] that this map is surjective by giving an algorithm that transforms a
link diagram, using the Reidemeister moves, into an equivalent diagram that is evidently the closure
of a braid. We call two braids (not necessarily on the same number of strands) link equivalent if
they form isotopic links after closure. In [31], Markov made the following characterization of this
equivalence relation on Ud21 Bd' although the first published proof was due to Birman ([6]).
Theorem 11.1.2. Link of equivalence of braids is generated by the following two local moves.
(M I)
(M II)
(30,
where i : Bd '---+ Bd+l is the natural inclusion defined on generators by O"i f-+ O"i.
II ....I. II ....I..
9
(3
<-------->ITL
Figure II.2: The cyclic Markov move.
J J1 1
...
l~Cl' <--------> Cl'
T "If 1'-,
Figure IL3: The stabilization Markov move.
II.2. Representations of the Braid Group and the Iwahori-Hecke Algebra
In this section, we introduce the Iwahori-Hecke algebras of type A, and discuss their
central importance in knot theory. Initally, we will take the perspective that a link invariant
satisfying a skein relation akin to Ll is given, and use it to produce a particular quotient of the
braid group algebra that the invariant factors through. Afterwards, we take the Hecke algebra as
a starting point, and following Jones ([24]), show how to recover those link invariants (satisfying
skein relations) from the characters of its representations.
II. 2. 1. From Link Invariants to Algebras
Fix a commutative ring IF and consider a link invariant Q taking values in IF. By composing
with the closure map, for each d we get a linear function Qd : lFEd ----7 IF, defined on braids by
where lFEd is the group algebra of the braid group. Such a map Qd is actually a trace on account
of the first :Markov move, so the linear subspace
10
is a two-sided ideal, maximal among two-sided ideals on which the trace vanishes. Let Ad(Q) =
IFB,d ker Qd, and, by abuse of notation, let a denote the image of a under the canonical projection
IFBd -» Ad(Q). Note that Qd descends to the trace Q d : Ad(Q) ---+ IF that agrees with the original
link invariant in the sense that Qd(a) = Q(a) for any braid a E Bd. Furthermore, Ad(Q) is the
smallest quotient of IFBd through which the trace factors.
Now, suppose that IF = Z[x±1, v±1 , (v - V-I) -1] and that the link invariant Q satisfies the
following skein relation
(11.1)
where the links L+, L_, Lo are identical outside of a small disk and look like the tangles pictured
in 1.1 within the disk. This relation together with the normalization Q(unknot) = 1 defines a
two-variable invariant equivalent to the HOMFLYPT polynomial ([14] and [34]). We investigate
the consequence of this skein relation on the maps Qd'
For any choice of a, {3 E Bd and for any i = 1, ... ,d - 1, we have
(11.2)
Therefore, xai - x-lail - (v - V-I) E kerQd, which is equivalent to the relation
(II.3)
The HOMFLYPT invariant factors through this finite dimensional quotient Ad(Q) of IFBd by the
quadratic relation (II.3).
Lemma 11.2.1. Any a E Ad(Q) is equal to an IF-linear combination of words, each containing
exactly one instance of either ad-l or ad~l'
Proof. The relation ail = x2ai - x(v - V-I) shows that it suffices to consider positive braids:
words in the generators ai but not their inverses. It is a standard result that a is equal to an IF­
linear combination of words, that contain ad-l at most once. Any term in the resulting expression
that does not contain ad-l can then be replaced by (v - V-l)-l(xai - x-lail) to establish the
lemma.
Now we can prove the following result, connecting the algebras Ad(Q) together.
o
11
Proposition 11.2.2. The inclusion ~ Ed '---c> Ed+l descends to a well-defined injective algebra
Proof. Fix a E lFEd. Suppose that Qd(ab) = 0 for all b E lFEd and let c E lFEd+1 . By Lemma II.2.1,
we may write
for c;, cj E lFEd. (II.4 )
Then, by using the second Markov move,
Qd+l(~(a)c) = LQd+l(~(act)O'd) + LQd+l(~(acj)O'dl)
j
= L Qd(act) + L Qd(acj)
j
= O.
This shows that I is well-defined. To prove that I is injective, suppose that Qd(~(a)c) = 0 for all
c E lFEd+l and let b E lFEd. We have
[J
II. 2.2. From the Iwahori-Hecke Algebra to Link Invariants
Definition 11.2.3. Let 'Hd denote the Iwahori-Hecke algebra of type Ad- 1 associated to the
symmetric group 3d. This is the algebra over <C(v) generated by H1, ... ,Hd-l' subject to the
braid relations
(II.5 )
(II.6 )
and also the quadratic relations
(II. 7)
We recognize immediately that 'Hd --4> <C(v) 01F Ad(Q), Hi f---+ 1 0 XO'i, where <C(v) is
considered as a (<C(v), IF) bimod ule with x E IF acting on the right by 1. Let i denote the natural
12
Lemma II.2.4 (Ocneanu, [14]). For every y E <C(v), there is a linear map T : Ud~1 7-{d ----7 <C(v)
uniquely defined by
(i) T(ab) = T(ba),
(ii) T(i(a)H d ) = YT(a) for a E 7-{d, and
(iii) T(l) = 1.
Such a linear function is often called a Markov trace because of the first condition. Al-
though T does not give a link invariant directly (unless Y = 1), it is a useful notion for the following
two reasons. First of all, it behaves in a controlled manner with respect to the second Markov
move, and so it defines an invariant of framed links and can, moreover, be rescaled to make an
invariant of ordinary links. The second reason is that there are natural constructions of Markov
traces that arise by studying representations of the braid group and their characters for which Y
is a non-trivial quantity.
Here we how to construct a link invariant from a Markov trace. Following Jones, we
choose an invertible x so that T(X- IHi) = T((X- IHi)-l) for each 'i = 1, ... , n - 1. Noting that
the quadratic relation in 7-{d gives H;I = Hi - (v - V-I), we have x-Iy = x(y - (v - V-I)), and
finally
Therefore, we have
_ (V-V-
I
)
Y - X X _ X-I . (11.8)
(11.9)
Now, let cp : Ed ----7 7-{~ be the group homomorphism ai l--> Hi' Recall that e : Ed ----7 Z is
the exponent sum of a braid (often called the writhe).
Theorem II.2.5. The functions Pd : Ed ----7 IF given by
(ILl 0)
define a link invariant P v'ia the formula P(a) = Pd(a).
PTOof. Regarding the first Markov move, invariance of P follows from invariance of T and the fact
that the exponent sums match: e( 0.13) = e(f3o). It suffices to check invariance under the second
13
Markov move. Let 0: E Bd and calculate
The equality Pd +do:a-i1 ) = Pd(o:) follows from a similar calculation, noting that
o
The invariants {Pd }d2:1 are normalized so that P1 (1) = 1, where 1 is the trivial braid on
one strand, and they satisfy the following skein relation for any 0: E Bk and any i = 1, ... , d - 1,
(ILl 1)
Therefore, the link invariant P satisfies the relation II.l and we have the isomorphism
(II.12 )
Making the substitutions I = -Ax and m = A(v-v- 1 ) we recover the original normalization
of the HOMFLYPT polynomial pi: £ ----7 Z[l±,m±] ([14]) satisfying pl(unknot) = 1 and
(ILl3)
II. 2. 3. Specializing to the Jones Polynomial
In the sequel, we will be concerned with two different specializations of Q, which will be
shown to be equivalent to the Jones polynomial and the Alexander polynomial, respectively. For
novv, we consider the Jones polynomial.
14
Definition 11.2.6. The Jones polynomial is the function J : £ --> Z[v,v- 1J, defined by setting
x = v2 in P(L).
Thus, J is the unique isotopy invariant of links normalized so that J(unknot) = 1 and
satisfying the skein relation
(IU4)
Extending the Jones polynomial to braids, we have Jd : Ed --> Z[v, V-I] for each d ;::::: 1.
Since h is a specialization of the HOlvIFLYPT polynomial, it factors through the Hecke algebra.
In fact, it factors through a smaller quotient, Ad ( J) which we now describe.
