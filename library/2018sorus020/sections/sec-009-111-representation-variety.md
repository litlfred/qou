---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-009-111-representation-variety
section_title: "Representation variety"
section_number: 1.1.1
pages: 16-17
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
Let Γ be a ﬁnitely generated group, withS ={γ1,...,γ n} a system of generators of
Γ, andk be an algebraically closed ﬁeld of characteristic zero.
Deﬁnition 1.1.1.A representation is a group homomorphismρ : Γ→ SL2(k). We
deﬁne therepresentation varietyR(Γ) = Hom(Γ, SL2(k)) = {ρ : Γ → SL2(k)}. It
15
is an aﬃne algebraic variety deﬁned overk (and even overQ). For any choice ofS
there is an embedding :
ιS :R(Γ)→ SL2(k)n ↪→k4n
ρ↦→ (ρ(γ1),...,ρ (γn))
that does not depend onS in the following way : for any otherS′ ={γ′
1,...,γ ′
m},
there is a group isomorphismfS,S′ : Γ→ Γ that turns the generatorsγi into words
wi(γ′
1,...,γ ′
m).Itinducesanalgebraicmap FS,S′ :k4n→k4m suchthat FS,S′◦ιS =ιS′
and the restriction ofFS,S′ :ιS(R(Γ)→ιS′(RΓ) is an isomorphism.
The function algebra of the representation variety is
k[R(G)] = k[Xi,j
γ ,1≤i,j≤2,γ∈Γ]/(Xe−Id,XγXδ−Xγδ,γ,δ∈Γ)
where for anyγ∈ Γ,Xγ denotes the 4-tuple
(
X1,1
γ X1,2
γ
X2,1
γ X2,2
γ
)
and with multiplication
induced by the two-by-two matrices multiplication. This algebra is, as well, ﬁnitely
generated, since any choice ofS provides a ﬁnite set of generators.
The group SL2(k) acts by conjugation on the representation varietyR(Γ), but the
topological quotient is not an algebraic variety in general, nor even a Hausdorﬀ
space, as is emphasized in the following example.
Example 1.1.2. Let Γ = Z. The representation variety R(Z) is isomorphic to
SL2(k) via ρ ↦→ ρ(1). The one-parameter subgroup
{
Mt =
(t 0
0 t−1
)}
t∈k∗ acts on
R(Γ) by conjugation, in particularMt ( 1 1
0 1 )M−1
t =
(
1 t2
0 1
)
, hence the whole family
given by
{
ρt : 1↦→
(
1 t2
0 1
)}
t∈k∗ lies in the sameSL2(k)-orbit. In particularρ0 : 1↦→
( 1 0
0 1 ) ∈ SL2(k)·ρ1, despite ρ0 and ρ1 are obviously not conjugated. This shows
that the topological quotientR(Z)/ SL2(k) is not Hausdorﬀ in this example. The
following section shows how to solve this issue.
