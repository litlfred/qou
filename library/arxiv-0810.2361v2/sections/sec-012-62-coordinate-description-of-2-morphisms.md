---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON"
section_id: sec-012-62-coordinate-description-of-2-morphisms
section_title: "Coordinate Description of 2-Morphisms"
section_number: 6.2
pages: 35-38
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
doc_brief: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON — This paper describes a relationship between essentially ﬁn ite groupoids and 2-vector spaces."
---
behaviour of Λ on 2-morphisms, namely the assignment of a natural transformation
to a span of span maps. As discussed in Section 4, any natural tran sformation
between a pair of 2-linear maps between KV 2-vector spaces can be represented as
a matrix of linear operators, as in (18). We would like to describe explic itly the
linear maps composing Λ( Y ) and some consequences.
To motivate the rest, we can begin with the special case of hom Span(FinGpd)(1, 1),
where 1 is the trivial groupoid with one object (which we denote ⋆) and its identity
morphism. We can summarize the eﬀect of Λ on this hom-category by the following
theorem:
Theorem 6.2.1. On homSpan(FinGpd)(1, 1), the 2-functor Λ , expressed in coordi-
nates, reproduces groupoidiﬁcation in the sense of (4).
Proof. First, we note that Λ( 1)∼= V ect, since the only irreducible representation
of the trivial group (basis object) is C itself.
Since 1 is terminal in FinGpd, any groupoid has a unique map into it. Thus,
any span from 1 to 1 is of the form:
(146) 1
!
← X
!
→ 1
which just amounts to a choice of X. Then Λ( X) =! ∗!∗ can be described as a 1 × 1
matrix of vector spaces,
Λ( X)(⋆,C),(⋆,C) = hom(! ∗C, !∗C)(147)
∼=
⨁
[x]∈X
C(148)
since ! ∗C is the representation of X assigning a copy of C to each object. In
particular, inducing up the representation C gives, at each x∈ X, the representation
(149) C[Aut(⋆)]⊗C[Aut(x)] C = C
since ! ∗C, is the trivial representation of Aut(x).
For each isomorphism class in X, we thus get a copy of hom C, C∼= C. This is
the vector space associated to X by groupoidiﬁcation.
Similarly, a 2-morphism Y : X1→ X2 just amounts to an isomorphism class of
spans of groupoids (since Y and the Xi have unique maps to !. Then the linear
map
(150) Λ( Y )(⋆,C),(⋆,C) : Λ( X1)(⋆,C),(⋆,C)→ Λ( X2)(⋆,C),(⋆,C)
just becomes a map
(151) T (Y ) : C[X1]→ C[X2]
given by T (Y ) = ǫL,t◦ ηR,s.
By the above, (58), using F (x1)∼= C, can be written:
36 JEFFREY C. MORTON
(152) ηR,s(F )(y) : C→
⨁
[y]|s(y)∼=x1
C[Aut(x1)]⊗C[Aut(y)] C
So now for each [ x1]∈ X1, every y in the essential preimage of x1 under s gets a
copy of the trivial representation C for each coset of Im(Aut(y)) in Aut((x1). This
describes a decomposition of a representation of Aut(y) in terms of irreps (all of
which are necessarily trivial in this case). Call this representation G. In particular,
a vector in Λ X1(⋆,C),(⋆,C) gives a complex number at each [ x1]. The unit ηR,s takes
such a vector v to, at each y with s(y)∼= x1,
(153) 1
#Aut(y)
∑
g∈Aut(x1)
g−1⊗ 1
By commutativity for the span of span maps (which is necessarily str ict here!),
we also must have that
(154)⨁
[y′]|t(y′)∼=t(y)
C[Aut(t(y))]⊗C[Aut(y′)] G(y′)∼=
⨁
[y′]|s(y′)∼=s(y)
C[Aut(s(y))]⊗C[Aut(y)] C
Similarly, then, using this (63) can be written:
(155) ǫL,t(G)(y) :
⨁
[y′]|t(y′)∼=t(y)
C[Aut(t(y))]⊗C[Aut(y′)] G(y′)→ G(y)
So now consider the vector v ∈ Λ( X1)(⋆,C),(⋆,C) which gives 1 at [ x1] and 0
elsewhere. (That is, it gives the identity intertwining map between th e copies of
the representation ! ∗C at objects in [ x1] and the zero intertwiner elsewhere). Then
the natural transformation induces a map on the coeﬃcient:
(156) ηR,s : v↦→
⨁
[y]|s(y)∼=x1
1
#Aut(y)
∑
g∈Aut(x1)
g−1⊗ 1
but then suppose we look for the coeﬃcient of the result at [ x2]∈ X2. Only those
y over [x2] will contribute, but then, since the g−1 have no eﬀect on vectors in C,
we get:
(157) ǫL,t :
⨁
[y]|s(y)∼=x1
1
#Aut(x1)
∑
g∈Aut(x1)
g−1⊗ 1↦→
∑
y|(s,t)(y)∼=(x1,x2)
#Aut(x1)
#Aut(y)
But this is just
(158) # Aut(x1)
∑
y|(s,t)(y)∼=(x1,x2)
1
#Aut(y) = #Aut(x1)| ˆ(x1, x2)|
where the second term is the groupoid cardinality of the essential p reimage of
(x1, x2). This is just the coeﬃcient we ﬁnd in groupoidiﬁcation in the sense of Baez
and Dolan. □
Similar calculations apply for less trivial situations as well, although for these
we will require a little more of the representation theory of the grou poids Ai.
Lemma 6.2.2. Given a (strict) span between spans, Y : X1→ X2, for X1, X2 :
A1→ A2, then the natural transformation
(159) Λ( Y ) : Λ( X1)→ Λ( X2)
2-VECTOR SPACES AND GROUPOIDS 37
is a natural transformation given by a matrix of linear opera tors:
(160) Λ( Y )([a1],W1),([a2],W2) : Λ( X2)([a1],W1),([a2],W2)→ Λ( X2)([a1],W1),([a2],W2)
or equivalently
Λ( Y )([a1],W1),([a2],W2) :
⨁
[x1]
homRep(Aut(x1))[s∗
1(W1), t∗
1(W2)](161)
→
⨁
[x2]
homRep(Aut(x2))[s∗
2(W1), t∗
2(W2)]
Such that for each block ([x1], [x2]), the corresponding linear operator behaves as
follows: for f∈ hom[s∗
1(W1), t∗
1(W2)] we get:
(162) Λ( Y )([a1],W1),([a2],W2)|(x1,x2)(f ) =| ˆ(x1, x2)|
∑
g∈Aut(x1)
g−1f g
where ˆ(x1, x2) is the essential preimage of (x1, x2) under (s, t), namely the comma
category ((s, t)↓ (x1, x2)).
Proof. The argument here is similar to that in Theorem 6.2.1, except that we m ust
deal with nontrivial representations of the Aut(xi). That is, when we apply the
Nakayama isomorphism, and the evaluation maps, we cannot use triv iality. The
“group-averaging” acting on intertwiners in the expression we hav e given is exactly
the exterior trace used in the Nakayama isomorphism. Here its func tion is to project
a linear map (a “pulled-back” intertwiner) onto a space of intertwine rs as we push
it along the functor t.
In particular, the eﬀect of ηR, s on coordinates (i.e. choosing particular repre-
sentations Wi) is to take an intertwiner f∈ hom[s∗
1(W1), t∗
1(W2)] and produce an
intertwiner at the representations pulled back to Y . The counit ηL, t “pushes” this
down to an intertwiner in hom[ s∗
2(W1), t∗
2(W2)]. The group averaging ensures this
will be an intertwiner itself. □
Remark 6.2.3. Using the formula for composition of 2-linear maps and natural
transformations in a general 2-vector space, we can readily see h ow horizontal and
vertical composition work.
Vertical composition is given by composition of linear maps component -wise, so
we have:
(163) Λ( Y ′◦ Y )([a1],W1),([a2],W2)
with components given by by:
⨁
([x1],[x3])
| ˆ(x1, x3)|
∑
g∈Aut(x3)
g−1f g(164)
=
⨁
([x1],[x3])
∑
[x2]
| ˆ(x2, x3)|·| ˆ(x1, x2)|· # Aut(x2)
( ∑
g∈Aut(x3)
g−1f g
)
This uses the fact that the two group averages each give project ions into spaces
of intertwiners, which is redundant, so we omit one, taking only the o rder of the
group. We also use that ˆ(x1, x3) is a subgroupoid of Y ′◦Y . In fact, it is a union over
all equivalence classes [ x2] in X2 of the objects in the weak pullback Y ′◦ Y based
over [x2], which gives the sum over [ x2] (which performs the matrix multiplication
in each component).
38 JEFFREY C. MORTON
The horizontal composite, Λ( Y ′◦ Y )∼= Λ( Y ′)◦ Λ( Y ), on the other hand, in-
volves “matrix multiplication” at the level of composition of 2-linear ma ps. The
(([a1], W1), ([a3], W3)) component of the product is a linear map given as a block
matrix with one block for each basis 2-vector. The blocks consist of the tensor
products of the matrices from the components of Λ( Y ) and Λ( Y ′). In particular,
the β isomorphisms from the horizontal composition of source and targe t induce
an isomorphism which acts on intertwiners ι⊗ ι′ by:
( ⨁
([x1 ,f1 ,x′
1])
([x2,f2,x′
2])
| ˆ((x1, x′
1), (x2, x′
2))|
∑
(g,g′)∈Aut([x1],[x′
1])
(g, g′)−1ι⊗ ι′(g, g′)
)
(165)
∼=
⨁
([a2],W2)
( ⨁
([x1],[x2])
| ˆ(x1, x2)|
∑
g∈Aut(x1)
g−1ιg
)
⊗
( ⨁
([x′
1],[x′
2])
| ˆ(x′
1, x′
2)|
∑
g′∈Aut(x′
1)
(g′)−1ι′g′
)
=
⨁
([a2],W2)
( ⨁
([x1],[x2])
([x′
1],[x′
2])
| ˆ(x1, x2)|·| ˆ(x′
1, x′
2)|
∑
(g,g′)∈Aut(x1)×Aut(x′
1)
(g, g′)−1ι⊗ ι′(g, g′)
)
Here, we note that since Y ′◦ Y is a weak pullback over A2, its objects consist of
triples ( y, h, y′), we implicitly have a sum over [ y, h, y′] in the groupoid cardinality,
which is| ˆ(x1, x2)|·| ˆ(x′
1, x′
2)|·| Aut(a2).
