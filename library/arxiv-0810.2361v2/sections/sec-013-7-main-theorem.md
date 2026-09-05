---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON"
section_id: sec-013-7-main-theorem
section_title: "Main Theorem"
section_number: 7
pages: 38-41
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
doc_brief: "2-VECTOR SPACES AND GROUPOIDS JEFFREY C. MORTON — This paper describes a relationship between essentially ﬁn ite groupoids and 2-vector spaces."
---
Having now described the eﬀect of the functor Λ at each level - gro upoids, spans,
and spans of spans—it remains to check that these really deﬁne a 2- functor of the
right kind. We begin by explicitly laying out what this 2-functor is, then verify the
remaining properties.
7.1. The 2-Linearization F unctor. We have been deﬁning the maps involved
in Λ throughout the last few sections, so here we collect the full deﬁ nition in one
place.
Deﬁnition 7.1.1. The 2-linearization process Λ : Span( FinGpd)→ 2V ectis de-
ﬁned as follows:
• For an essentially ﬁnite groupoid A it assigns:
(166) Λ( A) = [ A, V ect]
• For a span of groupoids:
(167) A
s
← X
t
→ B
it assigns:
(168) Λ( S) = t∗◦ s∗
2-VECTOR SPACES AND GROUPOIDS 39
• For a (strictly commuting) span of maps between two spans wit h the same
source and target:
(169) X1
s1
/d126/d126/d125 /d125 /d125 /d125 /d125 /d125 /d125 /d125 t1
/d32/d32/d65/d65/d65/d65/d65/d65/d65/d65
A Y
s
/d79/d79
t
/d15/d15
B
X2
s2
/d96/d96/d65 /d65 /d65 /d65 /d65 /d65 /d65 /d65
t2
/d62/d62/d125/d125/d125/d125/d125/d125/d125/d125
Λ assigns a natural transformation:
(170) Λ( Y ) = ǫL,t◦ ηR,s : (t1)∗s∗
1 =⇒ (t2)∗s∗
2
(and analogously for weakly commuting spans of maps as in Deﬁ nition
6.1.1)
Λ also associates the following:
• For each composable pair X : A1→ A2 and X ′ : A2→ A3, a natural iso-
morphism
(171) β : Λ( X ′◦ X)→ Λ( X ′)◦ Λ( X)
, as described in Theorem 5.2.1.
• For each object X∈ FinGpd, the natural transformation
(172) UB : 1 Λ( B)
∼
→ Λ(1 B)
is the natural transformation induced by the equivalence be tween B and 1B.
Then we have the following:
Theorem 7.1.2. The construction given in Deﬁnition 7.1.1 deﬁnes a weak 2-
functor Λ : Span( FinGpd)→ 2V ect.
Proof. First, we note that by the result of Lemma 4.1.1, we know that Λ assig ns a
2-vector space to each object of Span( FinGpd).
If S : B→ B′ span of essentially ﬁnite groupoids—i.e. a morphism in Span( FinGpd),
the map Λ( S) deﬁned in Deﬁnition 5.1.1 is a linear functor by the result of The-
orem 4.2.1, since it is a composite of two linear maps. This respects com position
of morphisms, as shown in Theorem 5.2.1, and of 2-morphisms in both h orizontal
and vertical directions, as shown in Theorems 6.1.3 and 6.1.4.
Next we need to check that our Λ satisﬁes the remaining properties of a weak 2-
functor: that the isomorphisms from the weak preservation of co mposition and units
satisfy the requisite coherence conditions; and that Λ strictly pre serves horizontal
and vertical composition of natural transformations.
The coherence conditions for the compositor morphisms
(173) βS,T : Λ( T◦ S)→ Λ( T )◦ Λ( S)
40 JEFFREY C. MORTON
and the associator say that these must make the following diagram c ommute for
all composable triples ( X, X ′, X′′):
(174)
Λ( X ′′)◦ Λ( X ′)◦ Λ( X)
Λ( X ′′◦ X ′)◦ Λ( X)
Λ(( X ′′◦ X ′)◦ X)Λ( X ′′◦ (X ′◦ X))
Λ( X ′′)◦ Λ( X ′◦ X)
1⊗β2,1
/d54/d54/d110/d110/d110/d110/d110/d110/d110/d110/d110/d110/d110/d110/d110/d110/d110
β3,2⊗1
/d104/d104/d80 /d80 /d80 /d80 /d80 /d80 /d80 /d80 /d80 /d80 /d80 /d80 /d80 /d80 /d80
β3,21
/d86/d86/d44 /d44 /d44 /d44 /d44 /d44 /d44 /d44 /d44 /d44 /d44 /d44
β32,1
/d72/d72/d18/d18/d18/d18/d18/d18/d18/d18/d18/d18/d18/d18
Λ( αX′′ ,X′ ,X )
/d47/d47
We implicitly assume here a trivial associator for the 2-linear maps in th e expres-
sion Λ( X ′′)◦ Λ( X ′)◦ Λ( X). This is because each 2-linear map is just a composite of
functors, so this composition is associative. But note that we can s imilarly assume,
without loss of generality, that the associator α for composition of spans is trivial.
The composite X ′◦ X is a weak pullback. This is only deﬁned up to isomorphism,
but one candidate is the comma category for any x∈ A2. Any other candidate is
isomorphic to this one. But then, the associator
(175) αX ′′,X ′,X : Λ( X ′′◦ (X ′◦ X))→ Λ(( X ′′◦ X ′)◦ X)
is just given by the obvious canonical map between the comma categ ories. In
particular, both composites give comma categories whose objects are determined
by choices ( x, f, x′, g, x′′) where f : t1(x)→ s2(x′) and g : t2(x′)→ s3(x′′), and
whose morphisms are triples of morphisms in X× X ′× X ′′ making the appropriate
diagrams commute. However, these comma categories are deﬁned in terms of pairs,
with diﬀerent parenthesizations. So αX ′′,X ′,X is the evident isomorphism between
these composites.
So it suﬃces to show that, up to this identiﬁcation:
(176) (1 ⊗ βX ′,X )◦ βX ′′,X ′◦X = (βX ′′,X ′⊗ 1)◦ βX ′′◦X ′,X
The β isomorphisms are given by the α up to which the weak pullbacks commute,
and so are given by choices of the functions f ∈ A2 and g∈ A3 in the comma
categories. The associator isomorphism induces an corresponding isomorphism be-
tween these composite β maps by the correspondence between the choices of f and
g in the pullback squares on each side of this equation. So indeed, this is true.
In general, the coherence conditions for the “unit” isomorphism
(177) UA : 1 Λ( A)
∼
→ Λ(1 A)
2-VECTOR SPACES AND GROUPOIDS 41
which accomplishes weak preservation of identities, say that it must make the fol-
lowing commute for any span X : A1→ A2:
(178) Λ( X)
Λ( X)◦ Λ(1 A1)
1⊗UA1
/d79/d79
Λ( X◦ 1A1)
Λ( rX )
/d101/d101/d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76 /d76βX,1A1/d111/d111
where rA1 is the right unitor for A1. There is also the symmetric condition for the
left unitor.
We notice that, as with Λ(1 A1), Λ( rA1 ) is equivalent to the identity. The map
rX : X◦ 1A1→ X is the canonical isomorphism taking composition of X with an
identity span to X which is just a projection from a comma category. Since X◦ 1A1
and X are thus isomorphic, .
So the condition amounts to the fact that βX,1A1 : Λ( X◦1A1)→ Λ( X)◦Λ(1 A1) =
Λ( X) is equivalent to the identity in such a way that (178) commutes. But this is
immediate since this β map is being applied to an identity span. □
