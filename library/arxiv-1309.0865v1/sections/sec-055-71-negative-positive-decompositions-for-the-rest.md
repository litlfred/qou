---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-055-71-negative-positive-decompositions-for-the-rest
section_title: "Negative-positive decompositions. For the rest of this chapter we will be in-"
section_number: 7.1
pages: 70-73
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
terested in embedded graphs, not isotopy classes thereof. W e will abusively use the
term Soergel graph to refer to a graph embedded without horizontal tangent line s, so
that no two vertices share the same y-coordinate. This kind of graph can be written
as the product of the generators in the introduction, tensor ed with identity maps.
Recall that those generators were the bottom boundary dot, t he top boundary dot,
the trivalent split, the trivalent merge, the 2m-valent vertex viewed as a map with m
inputs and m outputs, and polynomials. In all our arguments, polynomial s will be
treated separately from other parts of a graph.
Given such a graph, it has heightk if it is a product of k generators, ignoring the
polynomials. At a given y-coordinate without a vertex, we say the diagram has width
k if the object given by the horizontal line at that coordinate isBx for a sequence of
length k (i.e. if the horizontal line passes through k strands). The maxwidth of a
diagram is the maximal width attained.
We classify the generators as being positive, neutral, or negative, depending on
whether they increase, preserve, or decrease the width when reading from bottom
to top. Thus a top boundary dot and a splitting trivalent are p ositive, a 2m-valent
vertex and a box are neutral, and a bottom boundary dot and a me rging trivalent
are negative. Note that light leaves LLx,e are constructed purely out of non-positive
maps. The negative height of a map is the number of negative generators used, and
similarly for the positive height.
+ + = − −
The central generator is supposed to represent any 2m-valent vertex.
A graph will be called negative-positive if it consists of a composition of negative
and neutral ( non-positive) maps followed by a composition of positive and neutral
(non-negative) maps. In other words, the maximal width is attained on the ou tside;
the map shrinks in width towards the middle and then expands a gain. We say the
map is strictly negative-positive if the width shrinks non-trivially . Bec ause polyno-
mials are neutral, they can appear anywhere. Given a morphis m in D, an expression
for it as a k-linear combination of negative-positive graphs is called a negative-positive
decomposition.
Any map of the formLLx,e is constructed out of non-positive generators. Thus ev-
ery double leaves map LL is a negative-positive map, and the main theorem implies
that every morphism in D has a negative-positive decomposition.
We state some lemmas about negative-positive decompositio ns:
Claim 7.1. Consider the Jones-Wenzl morphism as a degree 0 map (i.e. the RHS of (5.16)).
With the exception of the identity map, every other diagram i s strictly negative-positive.
Moreover, every other diagram attains a width ≤m − 2.
Proof. This is obvious. Perhaps it is most evident using the diagram matic cellular
structure on the Temperley-Lieb algebra. □
SOERGEL CALCULUS 71
Claim 7.2. Any strictly non-positive map from Bw, for w a reduced expression, is in the
span of maps with a bottom boundary dot.
Proof. No rex can be the source of a merging trivalent ss → s. Thus the map must
consist of some rex move with polynomials followed by a botto m dot. We know,
using (5.7), that a dot on top of a 2m-valent vertex yields a sum of diagrams, each of
which has a bottom boundary dot. Thus we can “pull” the dot suc cessively through
all the 2m-valent vertices in the rex move (ignoring any polynomials) until we have
a bottom boundary dot. □
Claim 7.3. If φ = fgh where f is non-negative, h is non-positive, and g has a (strictly)
negative-positive decomposition, then φ has a (strictly) negative-positive decomposition.
Proof. This is obvious. □
Lemma 7.4. Letw andw′ be two rexes for the same element w ∈ W , and let β andβ′ be
two rex moves from w tow′. Then β −β′ has a strictly negative-positive decomposition. In
particular,β −β′ is in the span of diagrams having both a bottom and a top bounda ry dot.
Proof. We already know (see section 4.2) that two rex moves can be con nected by a
series of transformations. These transformations corresp ond to the Zamolodchikov
relations (4.7), (4.8), (4.9), (4.5), and the relation (4.4 ). The difference between two rex
moves which differ by a single transformation in D is given by the analog of each of
these relations: (5.10), (5.11), (5.12), (5.8), and (5.16) . Applying the transformation for
A3 orB3 orA1 ×I2(m) will yield no difference between the rex moves. Applying the
transformation forH3 or (5.16) will have a difference with a strictly negative-positive
decomposition. More precisely , this transformation is applied somewhere within the
rex move, but using the previous claim, the overall differen ce will still have a strictly
negative-positive decomposition. We can write β −β′ = (β −β1) + (β1 −β2) +... +
(βk −β′) where each successive difference corresponds to a single tr ansformation.
The result follows. □
For w ∈ W and an arbitrary sequence x we write w ≤ x if there exists a subse-
quence e ofx expressingw.
Lemma 7.5. Letx be a sequence. The identity of Bx has a negative-positive decomposition
where each term factors through some Bw for some reduced expression w forw ≤x.
Proof. Let us use induction on the length of x. Whenever x is a reduced expression
the statement is trivial. Suppose that x contains a repeated index ss. One can apply
the relation (5.15) give a negative-positive decompositio n where each term factors
throughx′, the sequence identical to x except with one copy of s removed. Apply-
ing the inductive hypothesis to x′ and nesting negative-positive decompositions, we
have the result for x.
Suppose thatx is not a reduced expression. There is some ﬁnite sequence of b raid
relations sts.../bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
m
= tst.../bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
m
which, when applied to x, yield a new sequence which
72 BEN ELIAS AND GEORDIE WILLIAMSON
has a repeated index. Let us induct on the number of such relat ions which need
to be applied before a repeated index is reached. For each rel ation applied, we can
use (5.16) to replace the identity /BD
sts... inside /BD
x with the doubled 2m-valent vertex
(the LHS of (5.16)) plus a linear combination of strictly neg ative-positive maps. The
doubled 2m-valent vertex yields a neutral map factoring through some s equence
x′ which is closer to having a repeated index. Therefore, by ind uction, /BD
x has a
negative-positive decomposition as desired. □
7.2. Modulo lower terms. Let us ﬁx an element w ∈W with a reduced expressionw.
LetIw denote the right ideal (bottom ideal, if you think diagramma tically) consisting
of linear cominations of diagrams with arbitrary source x, ﬁxed target w and which
are strictly positive on top. We have already shown that this is the same as the ideal
generated by all the top boundary dots. The elements of this i deal are the so-called
lower terms (with respect to w). In the absence of localization, taking the quotient by
Iw is the best way to talk about maps to Qw. After all, Qw is the unique standard
summand which is joint kernel of the top boundary dots. When w = ∅, the ideal Iw
is zero.
Letw′ be the reduced expression obtained after placing a 2m-valent vertex above
w. The 2m-valent vertex, as a map from Bw → Bw′, clearly sends Iw → Iw′, because
we can “pull” top-dots through 2m-valent vertices. The color-reversed 2m-valent
vertex gives a map Bw′ → Bw sending Iw′ → Iw. The composition of these two
maps, minus the identity , has a strictly negative-positive decomposition, and thus
consists of lower terms. Therefore the doubled 2m-valent vertex acts as the identity
moduloIw. We see that, for any x, the spaces Hom(Bx,B w)/Iw and Hom(Bx,B w′)/Iw′
are isomorphic. In fact, for any two rexes, these spaces of mo rphisms modulo lower
terms are all canonically isomorphic. After all, for two arbitrary rexes w andw′, we
can use any rex move to give an isomorphism Hom(Bx,B w)/Iw → Hom(Bx,B w′)/Iw′,
and any two rex moves are equal modulo lower terms by Lemma 7.4 .
We are interested in the span of the mapsLLx,e with targetw, modulo lower terms.
By the previous paragraph, we do not care which rex w we chose, or what rex move
is applied at the very end of the construction of LLx,e. However, other choices of rex
moves in the construction of LLx,e may still be important.
Our ﬁrst step towards showing that LL forms a basis for all Hom spaces is show-
ing thatLL forms a basis for maps to rexes, modulo lower terms.
Proposition 7.6. Letx be arbitrary andw be a rex for w ∈W . Choose a map LLx,e for each
e expressingw. These maps form a basis for Hom(Bx,B w)/Iw, under the action of R on the
left.
We brieﬂy defer the proof of this proposition. The discussio n above implies that
knowing this Proposition for a single rex w ofw will imply the result for every rex of
w.
We already know linear independence using localization arguments, so it is enough
to show that they span. We will prove this by induction, but th e induction will not
SOERGEL CALCULUS 73
be easy . After all, the base case where x = w = ∅ is already a highly non-trivial
statement: that all diagrams without boundary reduce to the empty diagram (with
polynomials). We do not know how to show this statement direc tly (say , with graph
theory) except in type A or dihedral type; the equivalent statement for Dstd was
shown only using nontrivial arguments involving homotopy g roups.
Identical statements can be made about maps from w using the vertical ﬂip map
which is an antiinvolution. The proposition as stated above is equivalent to one
saying that maps from w modulo terms with bottom dots are spanned by LLx,e.
7.3. Reduction to working modulo lower terms.
Proof of Theorem 6.11 assuming Proposition 7.6. Fix sequencesx andy and a morphism
φ : x → y. We want to write φ as an R-linear combination of diagrams of the form
LLy,fLLx,e where the subsequences express a common element w ∈W .
The identity map of x has a negative-positive decomposition where every term
factors through a reduced expression, by Lemma 7.5. We only n eed to work with
one diagram at a time, so without loss of generality we assume thatφ =fg factors as
g : x →w andf : w →y for some reduced expressionw. We will prove the statement
by induction on w. That is, we assume that any morphism φ = fg which factors
through a rex v forv < wis in the span of LL. The base case follows from the same
arguments.
Writeg = gw +gl andf = fw +fl. Here gw is an R-linear combination of LLx,e,
and gl ∈ Iw; similarly ,fw is in the span of LLy,f and fl ∈ I w. This decomposition
is guaranteed by Proposition 7.6. The composition fwgw is clearly in the span of
