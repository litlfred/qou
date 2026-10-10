---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-005-5-steinberg-schemes-of-braids
section_title: "Steinberg Schemes of Braids"
section_number: 5
pages: 38-41
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the W eyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
5.1. Let S ⊆W be the set of simple reﬂections in the chosen Coxeter present ation
of W . Let BrW be the Artin braid group of W , and let Br +
W ⊆ BrW be the
monoid of positive braids determined by S. Each element s ∈S lifts to an element
σs ∈ Br +
W , such that {σs}s∈S is a generating set for Br +
W . The following result is
[D97, §1.11].
Theorem 5.1.1 (Deligne). There is a map from elements β ∈ Br +
W toG0-varieties
O(β)0 over B0 × B0 such that:
(1) O(σs)0 =Os,0 for all s ∈S.
(2) If β =β′β′′, then there is a ﬁxed isomorphism
O(β)0
∼
− →O(β′)0 ×B0O(β′′)0,
where the ﬁber product is formed with respect to the right pro jectionO(β′)0 →
B0 and the left projection O(β′′)0 → B 0. These isomorphisms are associa-
tive in the sense that the diagram
O(β′β′′β′′′)0 O(β′β′′)0 ×B0O(β′′′)0
O(β′)0 ×B0O(β′′β′′′)0 O(β′)0 ×B0O(β′′)0 ×B0O(β′′′)0
∼
∼
∼
∼
is commutative.
In particular, if w =s1 · · ·sℓ is a reduced expression, then
O(σw)0 ≃O(σs1 )0 ×B0 · · · ×B0O(σsℓ )0 ≃Ow,0
by way of these ﬁxed isomorphisms.
Deligne attributes the varieties O(β)0 to Broué–Michel [ BM97], though they are
implicit in Lusztig’s earlier papers on character sheaves. Note that dim O(β) =
|β| +N , where |β| is the writhe of β (see § A.2).
5.2. Rouquier introduced an extension of Deligne’s result i n which the full group
BrW replaces the monoid Br +
W , and in which objects of HW replace varieties over
B0 × B0. The ﬁber product over B0 is replaced by the convolution on HW .
Each element s ∈S gives rise to objects R+
s, R−
s ∈ HW that can be represented
by complexes of the following form:
R+
s = 0 → ICs → IC 1⟨ 1⟩,
R−
s = IC 1⟨− 1⟩ → ICs → 0.
Above, the underlined terms are the terms in degree zero. To d escribe the mor-
phisms, factor j1 :O1,0 → B 0 × B0 as the composition
O1,0
is
− →¯Os,0
¯js
− → B0 × B0.
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 39
Since O1,0 and ¯Os,0 are smooth and closed in B2
0, we have
IC 1 =j1,∗ ¯Qℓ⟨−r −N ⟩,
ICs = ¯js,∗ ¯Qℓ⟨ 1 −r −N ⟩.
Then the nontrivial morphism in R+
s , resp. R−
s , is induced by pushing forward
¯Qℓ →is,∗i∗
s ¯Qℓ
∼
− →is,∗ ¯Qℓ,
resp. is,∗ ¯Qℓ⟨− 2⟩
∼
− →is,!i!
s ¯Qℓ → ¯Qℓ,
along ¯js.
In [ So], Soergel gave a module-theoretic description of C(B × B ) (see Remark
2.4.2), and hence, of HW . Under it, the complexes R+
s and R−
s correspond to the
complexes of bimodules over Sym( V) deﬁned by Rouquier in §9.2.1 and §9.2.4 of
[R06]. Thus, Thm. 10.5 of ibid. amounts to the following result:
Theorem 5.2.1 (Rouquier). There is a map from elements β ∈ Br +
W to objects
R(β) ∈ HW such that:
(1) R(σs) = R+
s and R(σ−1
s ) = R−
s for all s ∈S.
(2) If β =β′β′′, then there is a ﬁxed isomorphism
R(β)
∼
− → R(β′)⋆ R(β′′).
These isomorphisms are associative in the sense that the dia gram
R(β′β′′β′′′) R(β′β′′)0⋆ R(β′′′)
R(β′)0⋆ R(β′′β′′′) R(β′)⋆ R(β′′)⋆ R(β′′′)
∼
∼
∼
∼
commutes.
5.3. The results of Deligne and Rouquier are related as follo ws. For all w ∈ W ,
let jβ be the map O(β)0 → B 0 × B0. Let
∆(β) = jβ,! ¯Qℓ⟨|β| −r −N ⟩,
∇(β) = jβ,∗ ¯Qℓ⟨|β| −r −N ⟩.
In the case where β = σs, we abbreviate by writing ∆ s = ∆(β) and ∇s = ∇(β).
The following lemma is strongly suggested by the statements in [ R06, §11], though
it does not seem to appear there.
Lemma 5.3.1. We have
ρ(R(β)) ≃ ∆(β),
ρ(R(β−1)) ≃ ∇(β)
for all β ∈ Br +
W .
40 MINH-TÂM QUANG TRINH
Proof. The explicit deﬁnitions of R+
s and R−
s show that
ρ(R+
s ) ≃ ∆s,
ρ(R−
s ) ≃ ∇s
for all s ∈S. We now apply the commutativity of ( 11). □
5.4. We deﬁne G0-schemesG(β)0, U(β)0, Z(β)0 by stipulating that all squares in
the commutative diagram below are cartesian.
O(β)0 G(β)0 U(β)0 Z(β)0
B0 × B0 G0 × B0 U0 × B0 ˜U0 × B0
pr 0 × pr ℓ
act i × id p × id
Let 1 ∈ BrW denote the identity braid. Then U(1)0 = ˜U0, the Springer resolution,
and Z(1)0 = Z0, the Steinberg scheme from the previous section.
Deﬁnition 5.4.1. For all β ∈ Br +
W , we say that Z(β)0 is the Steinberg scheme
attached to β.
In what follows, let pβ be the composition U(β)0 → U 0 × B0 → U 0. Note that
p1,! ¯Qℓ ≃p1,∗ ¯Qℓ ≃ S . We can now prove Theorem 2, relating the AW trace to the
generalized Steinberg schemes Z(β)0.
Theorem 5.4.2. For all β ∈ Br +
W and i,j , we have:
AHi,j(R(β)) ≃ grw
j+r Homi+r(pβ,! ¯Qℓ, S),
AHi,j(R(β−1)) ≃ grw
j+r Homi+r(pβ,∗ ¯Qℓ, S).
In particular, since S =p∗ ¯Qℓ⟨−r⟩ , we have
AHi,j(R(β)) ≃ grw
j+2r H!,G
−(i+2r)(Z(β))
by Lemma 4.3.1.
Proof. By the commutativity of ( 12), Lemma 5.3.1, and both smooth and proper
base change,
AHi,j(R(β)) ≃ grw
j Homi(Kb(i∗⟨−r⟩ ◦ CH ◦ρ)(R(β)), S)
≃ grw
j Homi((i∗⟨−r⟩ ◦ CH)(∆(β)), S)
≃ grw
j+r Homi+r(pβ,! ¯Qℓ, S).
The argument for R(β−1) is completely analogous. The remaining statement follows
from Lemma 4.3.1. □
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 41
