---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-007-26-algebras-over-a-closed-interval
section_title: "Algebras over a closed interval"
section_number: 2.6
pages: 30-32
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
---
Deﬁnition 2.30 (AssRL). Let AssRL denote an∞-operad corepresenting triples (A;Q,P ) consisting
of an associative algebra together with a unital left and a unital righ t module. Speciﬁcally, it is a
unital multi-category whose space of colors is the three-element s et{M,R,L}, and with spaces of
multi-morphisms given as follows. Let I
σ
− →{M,R,L} be a map from a ﬁnite set.
• AssRL(σ,M ) is the set of linear orders on I for which no element is related to an element
of σ−1({R,L}). In other words, should σ−1({R,L}) be empty, then there is one multi-
morphism from σ toM for each linear order on σ−1(M ); should σ−1({R,L}) not be empty,
then there are no multi-morphisms from σ to M .
• AssRL(σ,L ) is the set of linear orders on I for which each element of σ−1(L) is a minimum,
and no element is related to an element of σ−1(R). In other words, should σ−1({R}) be
empty and σ−1({L}) have cardinality at most 1, then there is one multi-morphism from σ
to M for each linear order on σ−1(M ); should σ−1({R}) not be empty or σ−1({L}) have
cardinality greater than 1, then there are no multi-morphisms from σ to M .
• AssRL(σ,R ) is the set of linear orders on I for which each element of σ−1(R) is a maximum,
and no element is related to an element of σ−1(L). In other words, should σ−1({L}) be
empty and σ−1({R}) have cardinality at most 1, then there is one multi-morphism from σ
to M for each linear order on σ−1(M ); should σ−1({L}) not be empty or σ−1({R}) have
cardinality greater than 1, then there are no multi-morphisms from σ to M .
Composition of multi-morphisms is given by concatenating linear order s.
Consider the oriented 1-manifold with boundary [ −1, 1], which is the closed interval, that we
regard as a structured stratiﬁed space in the sense of [AFT]. Takin g connected components depicts
a map of symmetric monoidal ∞-categories
[−] : Diskor
1 −→ Env
(
AssRL)
to the symmetric monoidal envelope, where [ R] = M , [ R≥0] = L, and [ R≤0] = R.
30
Observation 2.31. The symmetric monoidal functor Disk∂,or
1
[−]
−−→Env
(
AssRL)
factors as an equiv-
alence of symmetric monoidal ∞-categories:
(2.6.1) Disk∂,or
1
≃
−−→Env
(
AssRL)
– this follows by inspecting the morphism spaces of the ∞-category Disk∂,or
1 , which are discrete.
Observation 2.32. Consider the ordinary category ORL for which an object is a linearly ordered
ﬁnite set ( I,≤) together with a pair of disjoint subsets R⊂ I⊃ L for which each element of R
is a minimum and each element of L is a maximum, and for which a morphism ( I,≤,R,L )→
(I ′,≤′,R ′,L ′) is an order preserving map I
f
− →I ′ for which f (R⊔L)⊂ R′⊔L′. (Note that the
cardinality of each of L and of R is at most one.) Concatenating linear orders makes ORL into a
multi-category, and it is equipped with a canonical maps of operads t o Env
(
AssRL)
. By inspection,
the equivalence (2.6.1) of Observation 2.31 lifts to an equivalence of ∞-operads,
(2.6.2) [ −] : Disk∂,or
1/[−1,1]
≃
− →ORL .
After these observations, there is this immediate consequence.
Corollary 2.33. There is a canonical equivalence of ∞-categories:
∫
−
: AlgAssRL (V)
≃
−−→Alg[−1,1](V) .
Proof. So the remaining point to check is that restriction along the map of ∞-operads Disk∂,or
1/[−1,1]→
Disk∂,or
1 implements an equivalence of symmetric monoidal∞-categories Env
(
Disk∂,or
1/[−1,1]
) ≃
− →Disk∂,or
1
from the symmetric monoidal envelope. Well, for each object U∈ D∂,or
1 it is standard that the space
of morphisms Mﬂd∂,or
1
(
U, [−1, 1]
)
≃∗ is contractible; and it follows that this functor gives an equiva-
lence on spaces of objects of underlying ∞-categories. That this functor gives an equivalence on the
space of morphisms follows because the functor on the active ∞-subcategories Disk∂,or
1/[−1,1]→ Disk∂,or
1
is a right ﬁbration.
□
Proposition 2.34. Let (A;P,Q ) be an AssRL-algebra in V; which is to say an associative algebra A
together with a unital left and a unital right A-module. Applying Observation 2.31, regard (A;P,Q )
as a Disk∂,or
1 -algebra in V. There is a canonical equivalence in V:
Q⊗
A
P
≃
−−→
∫
[−1,1]
(A;P,Q ) .
Proof. There is the standard fully faithful functor ∆ op⊂ ORL whose essential image consists of those
objects (I,≤,R,L ) for which R⁄=∅⁄=L. Adjoining minima and maxima gives a left adjoint to this
functor, and so it is ﬁnal. Through Observation 2.32, there is a ﬁnal functor ∆ op→ Disk∂,or
1/[−1,1];
and the resulting simplicial object
Bar•
(
Q,A,P
)
: ∆ op→ Disk∂,or
1/[−1,1]→ Disk∂,or
1
[−]
−−→Env
(
AssRL) (A;P,Q)
−−−−−→V
is identiﬁed as the two-sided bar construction, as indicated. We con clude the equivalence in V:
Q⊗
A
P≃ colim
(
∆ op Bar•
(
Q,A,P
)
−−−−−−−−→V
) ≃
− →
∫
[−1,1]
(A;P,Q ) .
□
Lemma 2.24 and Proposition 2.34 assemble as the next result.
31
Corollary 2.35. Let F : Mﬂd(B)−→ V be a symmetric monoidal functor. Let X∼= X−
⋃
R×X0
X+
be a collar-gluing among B-manifolds. Then there is a canonical arrow in V:
(2.6.3) F (X−)
⨂
F (X0)
F (X+)−→F (X) .
Proof. The collar-gluing is prescribed by a constructible bundle ~X
f
− →[−1, 1] from a reﬁnement of
X. From Lemma 2.24, there is the composite map of ∞-operads
f −1 : Disk∂,or
1/[−1,1]
f −1
−−→Mﬂd(B)/ ~X→ Mﬂd(B)
F
− →V .
The universal property of factorization homology as a left adjoint gives the canonical arrow:
F (X−)
⨂
F (X0)
F (X+) ≃
Prop 2.34
∫
[−1,1]
Ff −→ F
(
f −1([−1, 1])
)
=F (X) ;
namely, this arrow is the counit of the adjunction
∫
: AlgDisk(B)(V) ⇄ Fun⊗(
Mﬂd(B), V
)
, evaluated
on F .
□
