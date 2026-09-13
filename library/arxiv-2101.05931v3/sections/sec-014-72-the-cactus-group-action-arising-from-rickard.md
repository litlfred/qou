---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-014-72-the-cactus-group-action-arising-from-rickard
section_title: "The cactus group action arising from Rickard complexes"
section_number: 7.2
pages: 18-20
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
group actions arise from categorical representations, ana logous to the construction of the crystal
on Irr(C) in Proposition 3.4.
Let C be a categorical representation of Uq(g). For any weight µ ∈X, by Theorem 6.8 Θ w0
/BD
µ :
Db(Cµ) → Db(Cw0(µ)) is a perverse equivalence, and hence it induces a bijection ϕI 1µ : Irr(Cµ) →
Irr(Cw0(µ)). By varying µ we obtain a bijection ϕI : Irr(C) → Irr(C).
Now let J ⊆I be a connected subdiagram, and let gJ ⊂ g be the corresponding subalgebra. By
restriction, C is also a categorical representation of Uq(gJ ), and hence by the above discussion we
also obtain a bijection ϕJ : Irr(C) → Irr(C).
We will prove that this family of bijections deﬁnes an action of the cactus group Irr(C). First we
need the following technical result. The important point he re is just that there exists an integer n
such that t2
w01µ = ±qn1µ.
Lemma 7.4. Letλ ∈X+,µ ∈X, and let µ −w0(λ) = ∑ ℓ
r=1αir , where ir ∈I. Set jr =τ (ir) and
deﬁne n(λ,µ ) ∈ Z by
n(λ,µ ) = 2
¨
˝
ℓ∑
r=1
λjr + 1 −
∑
1≤r≤s≤ℓ
ajrjs + (λ,ρ )
˛
‚
CATEGORICAL BRAID GROUP ACTIONS AND CACTUS GROUPS 19
Then on L(λ)µ we have
t2
w01µ = (−1)⟨2λ,ρ∨⟩qn(λ,µ)1µ. (7.5)
Proof. We will prove the claim by induction on ht(µ −w0(λ)). For µ =w0(λ), we have that ℓ = 0
so n(λ,µ ) = ( λ,ρ ). By [25, Equation (7)] tw0(vλ) = ( −1)⟨λ,ρ∨⟩q(λ,ρ)vlow
λ , which, combined with
Lemma 6.2, implies that t2
w0(vlow
λ ) = ( −1)⟨λ,ρ∨⟩q(λ,ρ)vlow
λ . Since dim( L(λ)w0(λ)) = 1, this proves the
base case.
Now choose any µ and suppose (7.5) holds for any weight µ′ such that ht(µ′ −w0(λ))<ht (µ −
w0(λ)). Consider v =Ej1 · · ·Ejℓvlow
λ ∈L(λ)µ. First note that by [25, Lemma 5.4] we have that
t2
w0Ei =q2K −2
i Eit2
w0. (7.6)
Setting v′ =Ej2 · · ·Ejℓvlow
λ , by induction we have
t2
w0v =q2K −2
j1 Ej1t2
w0v′
= (q2K −2
j1 Ej1)(−1)⟨λ,ρ∨⟩qn(λ,µ−αj1 )v′
= (−1)⟨λ,ρ∨⟩q2+n(λ,µ−αj1 )−2(µ,αj1 )v
One checks easily that n(λ,µ ) = 2+ n(λ,µ −αj1 )−2(µ,α j1 ), proving that t2
w0v = (−1)⟨λ,ρ∨⟩qn(λ,µ)v.
Since this holds for any vector of the form Ej1 · · ·Ejℓvlow
λ in L(λ)µ, this completes the inductive
step. □
Theorem 7.7. The assignment cJ ↦→ϕJ deﬁnes an action of C on Irr(C).
Proof. We need to show that the bijections ϕJ satisfy the cactus group relations.
Relation (i) : Without loss of generality we may assume J = I. Fix a weight µ. Our aim is to
show that
ϕIϕI 1µ = Id Irr(Cµ). (7.8)
Since the ﬁltration of Cw0(µ) which we use in the perversity data of Θ w0
/BD
µ, agrees with the
ﬁltration of Cw0(µ) which we use in the perversity data of Θ w0
/BD
w0(µ), by Lemma 4.5 the composition
Θ w0Θ w0
/BD
µ is a perverse autoequivalence of Db(Cµ).
The functor [ ⟨2λ,ρ ∨⟩]⟨n(λ,µ )⟩ is also a perverse autoequivalence of Db(Cµ). By Lemma 7.4 these
two perverse equivalences induce the same map on Grothendie ck groups, and hence by Lemma 4.2
they also induce the same bijection. Since the bijection ind uced by [⟨2λ,ρ ∨⟩]⟨n(λ,µ )⟩ is the identity,
this proves relation (i).
Relation (ii) : Let J,K ⊂ I be disjoint subdiagrams with no connecting edges. Our aim is to
show that
ϕJϕK 1µ =ϕKϕJ 1µ. (7.9)
We prove a slightly more general statement, namely that for a ny categorical representation C of
Uq(gJ × gK), relation (7.9) holds.
Note that Θ J Θ K
/BD
µ ∼= Θ KΘ J
/BD
µ are isomorphic perverse equivalences, so they induce the sa me
bijections. It remains to show that
ϕΘ J Θ K
/BD
µ =ϕJ ◦ϕK 1µ. (7.10)
Consider ﬁrst the case when C categoriﬁes an simple representation of Uq(gJ × gK ). A minimal
categoriﬁcation of Uq(gJ × gK) is of the form L(λ) ⊗
/CZ
L(µ), where λ is a highest weight for gJ and
µ is a highest weight for gK . Hence by Lemma 3.5, a simple categoriﬁcation of Uq(gJ × gK) is of
the form L(λ) ⊗
/CZ
L(µ) ⊗
/CZ
A for some abelian category A.
This implies that as a categorical representation of Uq(gJ ) (respectively Uq(gK)), C categoriﬁes
an isotypic representation. By Corollary 6.7 Θ J
/BD
wK
0 (µ) and Θ K
/BD
µ are t-exact up shift on isotypics
categoriﬁcations. Hence Equation (7.10) follows by Lemma 4 .5.
20 IV A HALACHEV A, ANTHONY LICATA, IV AN LOSEV, AND ODED YACOB I
Now consider a Jordan-H¨ older ﬁltration (Theorem 3.6):
0 = C0 ⊂ · · · ⊂ C n = C,
where for every i, Ci is a subrepresentation of C, and Ci/Ci−1 is a simple categoriﬁcation of Uq(gJ ×
gK). Equation (7.10) now follows by an easy induction on i. Indeed the base case when i = 1 holds
by the paragraph above, and the inductive step by Lemma 4.6.
Relation (iii) : We need to show that ϕJϕK1µ = ϕKϕτK (J)1µ, where J ⊂ K. Again, we may
assume that K =I. Note that we have an isomorphism at the level of functors:
Θ −1
w0 Θ wJ
0
Θ w0
/BD
µ ∼= Θ w
τK (J )
0
/BD
µ,
which lifts the corresponding relation in B. Since this is an isomorphism of perverse equivalences,
they must induce the same bijections by Lemma 4.2.
It remains to show that
ϕΘ −1
w0 Θ wJ
0
Θ w0
/BD
µ =ϕ−1
I ◦ϕJ ◦ϕI. (7.11)
When C is a simple categoriﬁcation, by Corollary 6.7 Θ w0
/BD
µ is t-exact (up to shift). Hence Equation
(7.11) follows by Lemma 4.7. Now apply the same reasoning as i n the proof of Relation (ii) to deduce
equation (7.11) in the general case.
□
