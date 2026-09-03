---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-002-6-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 6
pages: 6-8
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
Figure 4
The expression forδ 1
YB(f) is depicted in Figure 3, where YBOs are represented by crossings
and 1-cocyclesfare represented by circles on edges. The expression forδ 2
YB(ϕ) is depicted in
Figure 4, where 2-cocyclesϕare represented by double circles. The first positive terms in the figure
correspond to the left-hand side of the YBE, while the negative terms to the right-hand side. The
three terms for each is obtained by replacing a crossing by a double circle at exactly one place.
We cite the following lemma that relates 2-cocycles to deformations.
Lemma 3.1([18]).LetR:V→Vbe a YBO. Letϕ∈C 2
YB(V,V)be a YB 2-cochain forR. Then,
˜R=R+ℏϕis a YBO on ˜V=k[[ℏ]]/(ℏ 2)⊗Vif and only ifϕ∈Z 2
YB(V,V).
Proof.One computes the YBE for ˜R, and checks that the terms forℏconstitutes the YB 2-cocycle
condition. □
This YBO ˜R=R+ℏϕon ˜Vis called aninfinitesimal deformationofR.
3.2.YB cohomology in higher dimensions.In this subsection we review definitions of YB
cohomology theory from [18], see also [19].
We setσ n,i =1⊗(i−1)⊗R⊗1 ⊗(n−i−1). Then, forϕ∈Hom(V ⊗n,V ⊗n), the partial differentials
for YB cohomology are defined as
dn
YB,i(ϕ) =σ n+1,n+1−i···σ n+1,2σn+1,1(1⊗ϕ)σ n+1,1···σ n+1,i−1σn+1,i
−σn+1,i+1···σ n+1,nσn+1,n+1(ϕ⊗1)σ n+1,n+1···σ n+1,i+2σn+1,i+1.
The partial differentialsd n
YB,i are graphically depicted as in Figure 5.
n φφ
1 n+1
1
1
1 n+1
i n+1 i
n+1
n−i+2 i−1
i−1
n−i+2 i−1
i−1
i φ(   )dYB,
Figure 5
Definition 3.2([18]).We define the YB cohomology complex ofV, with YBOR, as the cochain
groupsC n(V,V) := Hom k(V⊗n,V ⊗n) and differentials∂ n
YB :=Pn
i=1(−1)idn
YB,i as an alternating
sum of partial differentials. The associated cohomology is calledYang-Baxter cohomologyand
denotedH n
YB(V,R).
Lemma 3.3([18]).The YB cohomology complex of Definition 3.2 is indeed a cochain complex.
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 7
To prove the result it is sufficient to show that wheneveri < jthe equalityd n+1
YB,jdn
YB,i =
dn+1
YB,idn
YB,j−1 holds. We include a diagrammatic argument in Figure 6 to show this fact.
φ
φ φ
φ
(4)
d i
n φ(   )n+1
dj φ
φ
φ
n+1i1 j n+1i1 n+1 i1j j n+1 i1 j
(8)(7)(6)(5)
(1) (2) (3)
φ
j n+1i1 j n+1i1j n+1i1 j n+1i1
φ(   )n+1
d d n
i j−1
Figure 6
A natural question to ask at this point is whether the two cohomology theories, from Definition 3.2
and [7], are related or not. In low degrees, it turns out that whenRis invertible (i.e. it is a YBO
rather than being just a pre-YBO) the cohomology groups are isomorphic. In the following, we
denote by ˆHn
YB(V,R) the YB cohomology groups of [6,7], and their differentials by ˆdn
YB. We recall
the following definition, found in [18].
Definition 3.4.LetR:V ⊗2 −→V ⊗2 be a Yang-Baxter operator over thek-moduleV. An
operator ˜R: ˜V⊗2−→ ˜V⊗2, where ˜V:=k[[ℏ]]/(ℏ 2)⊗V, is said to be aYang-Baxter deformation
ofR, or YB deformation for short, if it satisfies [R− ˜R](V⊗2)⊂ℏV ⊗2. Two YB deformationsR 1
andR 2 ofRare said to be equivalent if there exists a mappingf:V−→Vsuch that
R2 =R 1(f⊗1) +R 1(1⊗f)−(f⊗1)R 1−(1⊗f)R 1.
We observe that this definition coincides with the one found in [6], see Definition 5 therein,
upon taking the idealm= (ℏ). We lastly recall that in [6, 7] and [18] it has been shown that
the group of YB deformations is isomorphic to the respective second cohomology groups. See for
instance Proposition 27 in [6], and Theorem 3.9 in [18] where the proof is given for the more general
Yang-Baxter-Hochschild cohomology.
Proposition 3.5.Suppose thatRis a YBO. Then, we have
H1
YB(V,R) ∼= ˆH1
YB(V,R)
H2
YB(V,R) ∼= ˆH2
YB(V,R).
