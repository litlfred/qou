---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-006-adjunctions-in-2-categories
section_title: "Adjunctions in 2-categories."
section_number: null
pages: 12-14
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
The notion of an adjunction in a 2-category simultaneously g eneralizes the
notion of an adjunction between functors and the notion of a d uality between
objects of a monoidal category. As it is the former that arise s in the context
of integral transforms, we will use that as the motivation, b ut will come
back to the latter below.
The most familiar deﬁnition of adjoint functors is as follow s. For cat-
egories C and D, an adjunction Ψ ⊣ Φ between functors Ψ : D→ C and
Φ : C→ D is the speciﬁcation of a natural isomorphism
ta,b: HomC(Ψ(a), b) ∼−→ HomD(a, Φ(b))
for any a ∈ D and b ∈ C.
It is well known (see [8, page 91]) that this deﬁnition is equi valent to
an alternative deﬁnition of adjunction which consists of th e speciﬁcation of
unit and counit natural morphisms, namely
η : IdD⇒ Φ ◦ Ψ and ǫ : Ψ ◦ Φ⇒ IdC,
12
such that the composite natural transformations
Ψ
IdΨ ◦η
=⇒ Ψ ◦ Φ ◦ Ψ
ǫ ◦IdΨ
=⇒ Ψ and Φ
η◦IdΦ
=⇒ Φ ◦ Ψ ◦ Φ
IdΦ ◦ǫ 
=⇒ Φ
are respectively the identity natural transformation on Ψ and the identity
natural transformation on Φ.
It is straight forward to translate between the two diﬀerent deﬁnitions
of adjunction. Given η and ǫ as above, deﬁne ta,b: HomC(Ψ(a), b) ∼−→
HomD(a, Φ(b)) by ta,b(f) := Φ(f) ◦ ηa. The inverse of ta,b is deﬁned sim-
ilarly using the counit ǫ. Conversely, to get the unit and counit from the
natural isomorphism of hom-sets, deﬁne ηa := ta,Ψ (a)(IdΨ (a)) and deﬁne ǫ
similarly.
The deﬁnition involving the unit and counit is stated purely in terms of
functors and natural transformations — without mentioning objects — thus
it generalizes immediately to arbitrary 2-categories.
Deﬁnition. If C is a 2-category, X and Y are objects of C , and
Φ : X→ Y and Ψ : Y→ X
are 1-morphisms, then an adjunction between Φ and Ψ consists of two 2-
morphisms
η : IdY⇒ Φ ◦ Ψ and ǫ : Ψ ◦ Φ⇒ IdX,
such that
(ǫ ◦h IdΨ ) ◦v (IdΨ ◦h η) = IdΨ and (IdΦ ◦h ǫ) ◦v (η ◦h IdΦ ) = IdΦ .
Given such an adjunction we write Ψ ⊣ Φ.
It is worth noting that this also generalizes the notion of du ality in
a monoidal category, that is to say two objects are dual in a mo noidal
category if and only if the corresponding 1-morphisms are ad joint in the
corresponding 2-category-with-one-object. Indeed, taki ng this point of view,
May and Sigurdsson [12] refer to what is here called adjuncti on as duality.
It is at this point that the utility of the string diagram nota tion begins
to be seen. Given an adjunction Ψ ⊣ Φ the counit ǫ : Ψ ◦ Φ⇒ Id and the
unit η : Id⇒ Φ ◦ Ψ can be denoted as follows:
IdX
Φ Ψ 
ǫ ; and
Φ 
IdY
Ψ 
η .
However, adopting the convention of denoting the identity o ne-morphism by
omission, it is useful just to draw the unit and counit as a cup and a cap
respectively:
Ψ Φ 
:=
IdX
Φ Ψ 
ǫ ; and
Ψ Φ 
:=
Φ 
IdY
Ψ 
η .
13
The relations become the satisfying
Φ 
Ψ 
Ψ 
=
Ψ 
and
Φ 
Φ 
Ψ =
Φ 
.
Adjunctions in 2-categories, as deﬁned above, do correspon d to isomor-
phisms of certain hom-sets but in a diﬀerent way to the classi cal notion of
adjunction. Namely, if Θ : Z→ Y and Ξ : Z→ X are two other 1-morphisms,
then an adjunction Ψ ⊣ Φ as above gives an isomorphism
2-Hom(Ψ ◦ Θ, Ξ) ∼−→ 2-Hom(Θ, Φ ◦ Ξ)
Ξ
Ψ 
α 
Θ 
↦→
Ψ 
Φ 
Θ 
Ξ
α 
The inverse isomorphism uses the counit in the obvious way.
In a similar fashion, for ˆΘ : Y→ Z and ˆΞ : X→ Z two 1-morphisms, one
obtains an isomorphism
2-Hom( ˆΘ ◦ Φ, ˆΞ) ∼−→ 2-Hom( ˆΘ, ˆΞ ◦ Ψ),
for which the reader is encouraged to draw the relevant pictu res. It is
worth noting that with respect to the previous isomorphism, Ψ and Φ have
swapped sides in all senses.
Adjunctions are unique up to a canonical isomorphism by the u sual
argument. This means that if Ψ and Ψ ′ are, say, both left adjoint to Φ, then
there is a canonical isomorphism Ψ ∼=⇒ Ψ ′. This is pictured below and it is
easy to check that this is an isomorphism.
Φ 
Ψ 
Ψ ′
Adjunctions are natural in the sense that they are preserved by 2-func-
tors, so, for instance, given a pair of adjoint kernels in V ar, the corresponding
integral transforms are adjoint functors.
