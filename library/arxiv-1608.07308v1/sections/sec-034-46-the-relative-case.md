---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-034-46-the-relative-case
section_title: "The relative case"
section_number: 4.6
pages: 38-40
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
namely when can we factor a map from a category to a scheme through another scheme:
(4.23)
More precisely,ι′ should satisfy the equationsι∗ =ι′∗◦π∗ andι∗ =π∗◦ι′
∗ and all the functors
should be derived from now on. The situation we will study in this paper is when:
Y = PV∨ := ProjX(S•V)
whereV is a coherent sheaf onX of projective dimension 0 or 1. Let us ﬁrst study the case of
projective dimension zero, so assume thatV is a vector bundle.
Proposition 4.15. Suppose that Y = PV∨ and that the map ι in (4.23) is constructed. The
datum of the extensionι′ is equivalent to an invertible objectF∈C together with an arrow:
(4.24) ι∗V
α
−→F
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 39
inC. This givesC the structure of a category overY if and only if:
(4.25)
[
...
α
−→ι∗(
∧kV
)
⊗F−k α
−→...
] h.e.
∼= 0 ∈ Kb(C)
The mapι′ is birational if and only ifι satisﬁes:
(4.26) SkV∼=ι∗(Fk) ∀k≥ 0
Proof. All notationsO orO(k) will refer to invertible sheaves on PV∨. If ι′ exists and has
all the expected properties, then set F = ι′∗(O(1)). In this case, the map (4.24) is simply ι′∗
applied to the tautological morphism:
π∗V−→O (1)
onY . The fact that the complex (4.25) is quasi-isomorphic to 0 follows by applying ι′∗ to the
Koszul complex ofY . The birationality of ι′ implies thatι′
∗1∼=O, from which the projection
formula implies ι′
∗(Fk)∼=O(k). Applying π∗ to this relation implies precisely (4.26). Con-
versely, suppose that we are given a morphism (4.24) which satisﬁes (4.25), and let us construct
the mapι′ that makes the diagram (4.23) commute. Note that (4.24) gives us an arrow:
ι∗(
V⊗k)
−→Fk
for allk≥ 0. BecauseF is invertible, this arrow factors through:
(4.27) ι∗(
SkV
)
−→Fk
for allk≥ 0 (sinceF is invertible, so isFk, and hence has no nontrivial endomorphisms; this
implies that the anti-symmetric projector is zero, henceSkF =Fk). This allows us to deﬁne:
ι′∗(M) =
(
π∗(M)
⨂
S•V
∞⨁
k=−∞
Fk
)0
A priori, this only determines the functorι′∗ on the level of the homotopy category of coherent
sheaves on PV∨. To check that it descends to a functor on the derived category, we must show
thatι′∗ takes quasi-isomorphic complexes to isomorphic complexes. The fact that this statement
is true for the Koszul complex is precisely the assumption (4.25). The fact that this is sufﬁcient
is due to Theorem 2.10 of [35] (see also [6]), which asserts that:
Db (Coh(PV∨))∼= homotopy category of complexes of
(rankV−1⨁
i=0
Ei(i)
)
E0,E1,...∈Db(Coh(X))
As for the right adjoint functor, we set:
ι′
∗(C) =ι∗
( ∞⨁
k=0
Fk⊗C
)
as a gradedOX−module. To realize the right hand side as a sheaf on Y , we need to endow it
with an action ofS∗V, namely with an associative homomorphism of graded algebras:
S∗V⊗OX ι∗
( ∞⨁
k=0
Fk⊗C
)
−→ι∗
( ∞⨁
k=0
Fk⊗C
)
The above morphism is obtained via adjunction and (4.27). □
40 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
