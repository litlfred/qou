---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-005-6-dmitri-nikshych-and-leonid-v-ainerman
section_title: "DMITRI NIKSHYCH AND LEONID V AINERMAN"
section_number: 6
pages: 6-7
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
for all h,g ∈ H, where we used Proposition 2.2.1(iv) and easy identities εt(hg) =
εt(hεt(g)) and εs(hg) = εt(εs(h)g). Dualizing the above arguments we show that
S is also a coalgebra anti-homomorphism :
ε(S(h)) = ε(S(h(1))εt(h(2))) = ε(S(h(1))h(2)) = ε(εt(h)) = ε(h),
∆( S(h)) = ∆( S(h(1))εt(h(2)))
= ∆( S(h(1)))(εt(h(2)) ⊗ 1)
= ∆( S(h(1)))(h(2)S(h(4)) ⊗εt(h(3)))
= ∆( εs(h(1)))(S(h(3)) ⊗S(h(2)))
= S(h(3)) ⊗εs(h(1))S(h(2)) = S(h(2)) ⊗S(h(1)).
The proof of the bijectivity of S can be found in ([BNSz], 2.10).
Next, we investigate the relations between the antipode and counit al maps.
Proposition 2.3.2. We have S ◦εs =εt ◦S and εs ◦S =S ◦εt. The restriction
of S deﬁnes an algebra anti-isomorphism between counital subal gebrasHt and Hs.
Proof. Using results of Proposition 2.3.1 we compute
S(εs(h)) = S(1(1))ε(h1(2)) = ε(1(1)S(h))1(2) =εt(S(h)),
for all h ∈ H. The second identity is proven similarly. Clearly, S maps Ht to Hs
and vice versa. Since S is bijective, and dim Ht = dim Hs by Proposition 2.2.2,
therefore S|Ht and S|Hs are anti-isomorphisms.
Proposition 2.3.3 ([NV1], 2.1.12) . Any nonzero morphism α : H →K of quan-
tum groupoids preserves counital subalgebras, i.e. Ht ∼= Kt and Hs ∼= Ks. Thus,
quantum groupoids with a given target (source) counital sub algebra form a full sub-
category.
Proof. It is clear that α|Ht :Ht →Kt is a homomorphism. If we write
∆(1 H ) =
n∑
i=1
wi ⊗zi
with {wi}n
i=1 and {zi}n
i=1 linearly independent, then ∆(1 K) = ∑ n
i=1 α(wi) ⊗α(zi).
By Proposition 2.2.2, Kt = span{α(zi)}, i.e., α|Ht is surjective. Since
zj =εt(zj) =
n∑
i=1
ε(wizj)zi,
then ε(wizj) = δij, therefore,
dimHt = n =
n∑
i=1
εH(wizi) =
n∑
i=1
εH(wiS(zi))
= εH(εt(1H )) = εH(1H ) = εK(1K) = dim Kt,
so α|Ht is bijective. The proof for source subalgebras is similar.
Let us recall that a k-algebra A is said to be separable [P] if the multiplication
epimorphismm :A ⊗kA →A has a right inverse as an A −A bimodule homomor-
phism. This is equivalent to the existence of a separability elemente ∈A ⊗kA such
thatm(e) = 1 and ( a ⊗ 1)e =e(1 ⊗a), (1 ⊗a)e =e(a ⊗ 1) for all a ∈A.
FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS 7
Proposition 2.3.4. The counital subalgebras Ht and Hs are separable, their sep-
arability elements are et = (S ⊗ id)∆(1) and es = (id ⊗S)∆(1) , respectively.
Proof. For all z ∈Ht we compute, using Propositions 2.2.1 and 2.3.2 :
1(1)S−1(z) ⊗ 1(2) = S−1(z)(1) ⊗εt(S−1(z)(2))
= 1 (1) ⊗εt(1(2)S−1(z)) = 1 (1) ⊗εt(1(2)z) = 1 (1) ⊗ 1(2)z,
applying (S ⊗ id) to this identity we get etz =zet. Clearly, m(et) = 1, whence et
is a separability element. The second statement follows similarly.
