---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-028-22-dmitri-nikshych-and-leonid-v-ainerman
section_title: "DMITRI NIKSHYCH AND LEONID V AINERMAN"
section_number: 22
pages: 22-22
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
(ii) For any i ∈I, there exists i∗ ∈I such that Vi∗ is isomorphic to V ∗
i .
(iii) All objects of V are dominated by the family {V }i∈I .
(iv) The square matrix S = {Sij}i,j∈I = {trq(cVi,Vj ◦cVj ,Vi)}i,j∈I is invertible over
k (here tr q is the quantum trace in a ribbon category deﬁned by (43)).
If a quantum groupoid H is connected and semisimple over an algebraically
closed ﬁeld, modularity of Rep( H) is equivalent to Rep( H) being ribbon and such
that the matrix S = {Sij}i,j∈I = {trq(cVi,Vj ◦cVj ,Vi )}i,j∈I , where I is the set of
all (equivalent classes of) irreducible representations, is invertible . The following
proposition extends a result known for Hopf algebras ([EG], 1.1).
Proposition 5.5.1. If H is a connected, ribbon, factorizable quantum groupoid
over an algebraically closed ﬁeld k, possessing a normalized two-sided integral, then
Rep(H) is a modular category.
Proof. Here we only need to prove the invertibility of the matrix formed by
Sij = tr q(cVi,Vj ◦cVj ,Vi )
= (dim Ht)−1Tr ((uν) ◦cVi,Vj ◦cVj ,Vi )
= (dim Ht)−1(χj ⊗χi)((uν ⊗uν)R21R),
whereVi are as above, I = {1,...n }, {χj} is a basis in the space C(H) of characters
of H (we used above the formula (45) for the quantum trace).
It was shown in ([NTV], 5.12, 8.1) that the map F : φ ↦→(φ ⊗ id)(R21R) is a
linear isomorphism between C(H)↼uν and the center Z(H) (here (χ↼uν )(a) =
χ(uνa) ∀a ∈ H, χ ∈ C(H)). So, there exists an invertible matrix T = (Tij)
representing the map F in the bases {χj} ofC(H) and {ei} ofZ(H), i.e., such that
F (χj ↼uν ) = ∑
i Tijei. Then
Sij = (dim Ht)−1χi(uνF (χj ↼uν )) = (dim Ht)−1 ∑
k
Tkjχi(uνe k)
= (dim Ht)−1(dimVi)χi(uν)Tij.
Therefore, S = DT , where D = diag {(dimHt)−1(dimVi)χi(uν)}. Theorem7.2.2
below, shows that the existence of a normalized two-sided integral inH is equivalent
to H being semisimple and possessing an invertible element g such that S2(x) =
gxg −1 for allx ∈H andχ(g−1) ⁄=O for all irreducible character χ ofH. Then u−1g
is an invertible central element of H andχi(u−1) ⁄= 0 for all χi. By Corollary 5.2.8
uS(u) = c is invertible central, therefore χi(u) = χi(c)χi(S(u−1))) ⁄= 0. Hence,
χi(uν) ⁄= 0 for all i and D is invertible.
