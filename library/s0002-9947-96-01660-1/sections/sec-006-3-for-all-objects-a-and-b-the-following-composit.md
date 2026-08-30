---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: sec-006-3-for-all-objects-a-and-b-the-following-composit
section_title: "For all objects a and b the following composite is required to be ϵ(a⊗b):"
section_number: 3
pages: 5-6
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
doc_brief: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state"
---
e
ϵ(a)
−−→a⊗ ˆa =a⊗ (e⊗ ˆa)
1⊗(ϵ(b)⊗1)
−−−−−−−→a⊗ ((b⊗ ˆb)⊗ ˆa)=( a⊗b)⊗ (a⊗b)ˆ.
The functorˆ and the maps ϵ are not independent. The maps ϵ determineˆ .
Lemma 2.3. In any pivotal category, for any morphism f : a→ b the following
composite is ˆf:
ˆb = ˆb⊗e
1⊗ϵ(a)
−−−−→ ˆb⊗ (a⊗ ˆa)
1⊗(f⊗1)
−−−−−→ˆb⊗ (b⊗ ˆa)= ˆ(ˆb⊗ ˆˆb)⊗ ˆa
ˆϵ(ˆb)⊗1
−−−−→ ˆe⊗ ˆa =ˆa.
Proof. This follows directly from conditions (1) and (2) of the preceding deﬁnition.
Deﬁnition 2.4. Leta be any object in a pivotal category. Then the monoid End(a)
has two trace maps, tr L, trR : End(a)→ End(e). In a pivotal category tr L(f)i s
deﬁned to be the composite
e
ϵ(ˆa)
−−→ ˆa⊗ ˆˆa =ˆ a⊗ a
1⊗f
−−→ ˆa⊗ a =( ˆa⊗ ˆˆa)ˆ
ˆϵ(ˆa)
−−→ ˆe = e
and trR(f) is deﬁned to be the composite
e
ϵ(a)
−−→ a ⊗ ˆa
f⊗1
−−→ a ⊗ ˆa =( a ⊗ ˆa)ˆ
ˆϵ(a)
−−→ ˆe = e.
These are called trace maps because they satisfy trL(fg )=t rL(gf )a n dt rR(fg )=
trR(gf ).
Deﬁnition 2.5. A pivotal category is spherical if, for all objects a and all mor-
phismsf : a→a,
trL(f)=t rR(f).
An equivalent condition is that trL(f)=t rL( ˆf), for allf : a→a. For each object
a in a spherical category, its quantum dimension is deﬁned to be dimq(a)=t rL(1a).
Thus, dimq(a)=d i mq(ˆa).
Also, in a spherical category, trL(f⊗g)=t rL(f). trL(g) (where the product is
in End(e)) for all f :a→a and all g :b→b.
All spherical categories considered in the rest of this are additive. This means
that each Hom set is a ﬁnitely generated abelian group with compositionZ-bilinear
and that the data deﬁning the spherical structure is compatible with the additive
structure. This means that ⊗ isZ-bilinear and that ˆ isZ-linear.
In any additive monoidal category End(e) is a commutative ring (see [10]) and we
denote this ring byF. In particular each of the above trace maps takes values in this
ring. It follows that an additive monoidal category is F-linear. We need to assume
4002 JOHN W. BARRETT AND BRUCE W. WESTBURY
some further conditions. These are that F is a ﬁeld and that each set of morphisms
is a ﬁnite dimensional vector space over F. In this paper an additive spherical
category means a spherical category in which these conditions are satisﬁed.
The main examples of additive spherical categories arise as the category of rep-
resentations of a Hopf algebra with some additional structure. This is discussed in
section 6.
Example 2.6. An example of a spherical category which cannot be regarded as
a category whose objects are ﬁnite dimensional vector spaces is given by taking
the freeZ[δ,z ]-linear category on the category of oriented framed tangles and then
taking the quotient by the well-known skein relation for the HOMFLY polynomial.
This is a spherical category, and for each pair of objects X and Y ,H o m (X,Y )i s
a ﬁnitely generated free module. This example satisﬁes all the conditions for an
additive spherical category except thatF is not a ﬁeld. However the objects cannot
be taken to be ﬁnitely generated modules unless z is a quantum integer.
Strict pivotal categories are discussed in [6], where it is shown that the category
of oriented planar graphs up to isotopy and with labelled edges is a strict pivotal
category. Similar constructions are discussed [9], [7], [19]. The following is an
informal statement of the result needed in the discussion in this paper. This result
is not required for the proofs in this paper, as an algebraic proof can always be given
in place of a diagrammatic proof. However it is important for an understanding of
the proofs.
Given a trivalent planar graph with the following data attached:
