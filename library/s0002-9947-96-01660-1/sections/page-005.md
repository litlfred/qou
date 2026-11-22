---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
toc_source: undetermined
doc_brief: "Invariants of piecewise-linear 3-manifolds — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state sum model on a tri- angulation."
---
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS
4001
1. For all morphisms, f : a →b, the following diagram commutes:
e
ϵ(a)
−−−−→a ⊗ˆa
ϵ(b)
y
yf⊗1
b ⊗ˆb −−−−→
1⊗ˆf
b ⊗ˆa
2. For all objects a, the following composite is the identity map of ˆa:
ˆa = e ⊗ˆa
ϵ(ˆa)⊗1
−−−−→(ˆa ⊗ˆˆa) ⊗ˆa = ˆa ⊗(a ⊗ˆa)b
1⊗ˆϵ(a)
−−−−→ˆa ⊗ˆe = ˆa.
3. For all objects a and b the following composite is required to be ϵ(a ⊗b):
e
ϵ(a)
−−→a ⊗ˆa = a ⊗(e ⊗ˆa)
1⊗(ϵ(b)⊗1)
−−−−−−−→a ⊗((b ⊗ˆb) ⊗ˆa) = (a ⊗b) ⊗(a ⊗b)b .
The functor b and the maps ϵ are not independent. The maps ϵ determine b .
Lemma 2.3. In any pivotal category, for any morphism f : a →b the following
composite is ˆf:
ˆb = ˆb ⊗e
1⊗ϵ(a)
−−−−→ˆb ⊗(a ⊗ˆa)
1⊗(f⊗1)
−−−−−→ˆb ⊗(b ⊗ˆa) = \
(ˆb ⊗ˆˆb) ⊗ˆa
ˆϵ(ˆb)⊗1
−−−−→ˆe ⊗ˆa = ˆa.
Proof. This follows directly from conditions (1) and (2) of the preceding deﬁnition.
Deﬁnition 2.4. Let a be any object in a pivotal category. Then the monoid End(a)
has two trace maps, trL, trR : End(a) →End(e). In a pivotal category trL(f) is
deﬁned to be the composite
e
ϵ(ˆa)
−−→
ˆa ⊗ˆˆa
=
ˆa ⊗a
1⊗f
−−→
ˆa ⊗a
=
(ˆa ⊗ˆˆa)b
ˆϵ(ˆa)
−−→
ˆe
=
e
and trR(f) is deﬁned to be the composite
e
ϵ(a)
−−→
a ⊗ˆa
f⊗1
−−→
a ⊗ˆa
=
(a ⊗ˆa)b
ˆϵ(a)
−−→
ˆe
=
e.
These are called trace maps because they satisfy trL(fg) = trL(gf) and trR(fg) =
trR(gf).
Deﬁnition 2.5. A pivotal category is spherical if, for all objects a and all mor-
phisms f : a →a,
trL(f) = trR(f).
An equivalent condition is that trL(f) = trL( ˆf), for all f : a →a. For each object
a in a spherical category, its quantum dimension is deﬁned to be dimq(a) = trL(1a).
Thus, dimq(a) = dimq(ˆa).
Also, in a spherical category, trL(f ⊗g) = trL(f). trL(g) (where the product is
in End(e)) for all f : a →a and all g: b →b.
All spherical categories considered in the rest of this are additive. This means
that each Hom set is a ﬁnitely generated abelian group with composition Z-bilinear
and that the data deﬁning the spherical structure is compatible with the additive
structure. This means that ⊗is Z-bilinear and that b is Z-linear.
In any additive monoidal category End(e) is a commutative ring (see [10]) and we
denote this ring by F. In particular each of the above trace maps takes values in this
ring. It follows that an additive monoidal category is F-linear. We need to assume
