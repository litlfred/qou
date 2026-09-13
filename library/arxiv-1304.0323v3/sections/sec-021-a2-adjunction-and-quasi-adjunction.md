---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-021-a2-adjunction-and-quasi-adjunction
section_title: "A.2. Adjunction and Quasi-adjunction"
section_number: null
pages: 67-69
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
Deﬁnition A.2.1. LetT be a tensor category with a unit object 1. Let (X,Y ) be a
pair of objects and let ε : X⊗Y→ 1 and η : 1→Y⊗X be morphisms.
(i) We say that (ε,η ) is an adjunction and that X is a left dual to Y and Y is a
right dual to X if the conditions (a) and (b) below are satisﬁed:
(a) the composition X≃X⊗ 1
X⊗η
−−−→X⊗Y⊗X
ε⊗X
−−−→1⊗X≃X is equal to
the identity of X.
(b) the composition Y≃ 1⊗Y
η⊗Y
−−−→Y⊗X⊗Y
Y⊗ε
−−−→1⊗Y ≃Y is equal to the
identity of Y .
(ii) If the composition X⊗ 1
X⊗η
−−−→X⊗ Y ⊗ X
ε⊗X
−−−→1⊗ X and 1⊗Y
η⊗Y
−−−→
Y⊗X⊗Y
Y⊗ε
−−−→1⊗Y are isomorphisms, then we say that (ε,η ) is a quasi-
adjunction.
68 S.-J. KANG, M. KASHIW ARA, M. KIM
Lemma A.2.2. LetT be a tensor category with a unit object 1 and let ε : X⊗Y→ 1
be a morphism in T. Then the following conditions are equivalent.
(a) There exists a morphism η : 1→Y⊗X such that (ε,η ) is an adjunction.
(b) There exists a morphism η : 1→ Y ⊗X such that (ε,η ) is a quasi-adjunction.
Namely, the compositions
f : X
X⊗η
−−−→X⊗Y⊗X
ε⊗X
−−−→X and g : Y
η⊗Y
−−−→Y⊗X⊗Y
Y⊗ε
−−−→Y
are isomorphisms.
(c) For any V,W ∈T , the composition
HomT (V,Y ⊗W )→ HomT (X⊗V,X ⊗Y⊗W )
ε⊗W
− −−− →HomT (X⊗V,W )
is a bijection.
(d) For any V,W ∈T , the composition
HomT (V,W ⊗X)→ HomT (V⊗Y,W ⊗X⊗Y )
W⊗ε
− −−− →HomT (V⊗Y,W )
is a bijection.
In this case, the morphism η in (a) is unique.
Moreover, if (ε,η ) satisﬁes (b), then the following statements hold.
(i) We have (g−1⊗X)◦η = (Y ⊗f−1)◦η and the pair
(
ε, (g−1⊗X)◦η
)
is an
adjunction,
(ii) We have ε◦ (X⊗g−1) = ε◦ (f−1⊗Y ) and the pair
(
ε◦ (X⊗g−1),η
)
is an
adjunction.
Hence for an object X ofT , a left dual (resp. a right dual) of X is unique up to a
unique isomorphism if it exists.
Lemma A.2.3. LetT be an abelian tensor category such that •⊗ • is an exact bi-
functor. Let
0→X′→X→X′′→ 0, 0→Y′′→Y→Y′→ 0
be exact sequences and morphisms
ε′ : X′⊗Y′→ 1, ε : X⊗Y→ 1, ε ′′ : X′′⊗Y′′→ 1,
η′ : 1→Y′⊗X′, η : 1→Y⊗X, η ′′ : 1→Y′′⊗X′′
are given so that the following the diagrams are commutative :
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 69
X′⊗Y /d47/d47
/d15/d15
X′⊗Y′
ε′
/d15/d15
X⊗Y
ε /d47/d47 1
X⊗Y′′
/d79/d79
/d47/d47X′′⊗Y′′,
ε′′
/d79/d79
Y′⊗X′ /d47/d47Y′⊗X
/d15/d15
1
η′
/d79/d79
η′′
/d15/d15
η /d47/d47Y⊗X
/d15/d15
Y′′⊗X′′ /d47/d47Y⊗X′′.
Assume further that (ε′,η′) and (ε′′,η′′) are quasi-adjunctions. Then the pair (ε,η )
is also a quasi-adjunction.
Proof. We shall only show that the composition X⊗ 1→ X⊗Y⊗X→ 1⊗X is an
isomorphism. Consider the following diagram with exact rows:
0 /d47/d47X′⊗ 1
/c55/c54/c53/c52 /c48/c49/c50/c51A
/d47/d47
/d15/d15
X⊗ 1 /d47/d47
/d15/d15
/c55/c54/c53/c52 /c48/c49/c50/c51B
X′′⊗ 1 /d47/d47
/d15/d15
0
X′⊗Y′⊗X′
/d15/d15
X⊗Y⊗X
/d15/d15
X′′⊗Y′′⊗X′′
/d15/d15
0 /d47/d47 1⊗X′ /d47/d47 1⊗X /d47/d47 1⊗X′′ /d47/d47 0.
If we show that /c55/c54/c53/c52 /c48/c49/c50/c51A and /c55/c54/c53/c52 /c48/c49/c50/c51B are commutative, then the composition of the middle
vertical arrows is an isomorphism because the one in the right and th e one in the left
are isomorphisms. Hence it is enough to show the commutativity of th e squares. For
example, the square /c55/c54/c53/c52 /c48/c49/c50/c51B is commutative, because we have the following commutative
diagram.
X⊗ 1 /d47/d47
X⊗η
/d125/d125③③③③③③③③③③③③③③③③③③③③③
X⊗η′′
/d15/d15
X′′⊗ 1
X ′′⊗η′′
/d15/d15
X⊗Y′′⊗X′′ /d47/d47
/d15/d15
X′′⊗Y′′⊗X′′
ε′′⊗X ′′
/d124/d124①①①①①①①①①①①①①①①①①①①①①
X⊗Y⊗X /d47/d47
ε⊗X
/d15/d15
X⊗Y⊗X′′
ε⊗X ′′
/d15/d15
1⊗X /d47/d47 1⊗X′′.
The commutativity of /c55/c54/c53/c52 /c48/c49/c50/c51A can be shown in a similar way. □
