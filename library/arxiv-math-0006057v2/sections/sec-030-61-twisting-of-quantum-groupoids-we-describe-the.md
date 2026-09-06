---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-030-61-twisting-of-quantum-groupoids-we-describe-the
section_title: "Twisting of quantum groupoids. We describe the procedure of construct-"
section_number: 6.1
pages: 23-24
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
ing new quantum groupoids by twisting a comultiplication. Twisting of Ho pf alge-
broids without an antipode was developed in [Xu] and a special case of twisting of
∗-quantum groupoids was considered in [NV1].
Deﬁnition 6.1.1. A twist for a quantum groupoid H is a pair (Θ , ¯Θ), with
Θ ∈ ∆(1)( H ⊗kH), ¯Θ ∈ (H ⊗kH)∆(1) , and Θ ¯Θ = ∆(1)(46)
satisfying the following axioms :
(ε ⊗ id)Θ = (id ⊗ε)Θ = ( ε ⊗ id) ¯Θ = (id ⊗ε) ¯Θ = 1 ,(47)
(∆ ⊗ id)(Θ)(Θ ⊗ 1) = (id ⊗ ∆)(Θ)(1 ⊗ Θ),(48)
( ¯Θ ⊗ 1)(∆ ⊗ id)( ¯Θ) = (1 ⊗ ¯Θ)(id ⊗ ∆)( ¯Θ),(49)
(∆ ⊗ id)( ¯Θ)(id ⊗ ∆)(Θ) = (Θ ⊗ 1)(1 ⊗ ¯Θ),(50)
(id ⊗ ∆)( ¯Θ)(∆ ⊗ id)(Θ) = (1 ⊗ Θ)( ¯Θ ⊗ 1).(51)
Note that for ordinary Hopf algebras the above notion coincides wit h the usual
notion of twist and each of the four conditions (48) – (51) implies the other three.
But since Θ and ¯Θ are, in general, not invertible we need to impose all of them.
The next Proposition extends Drinfeld’s twisting construction to th e case of
quantum groupoids.
Proposition 6.1.2. Let ( Θ, ¯Θ) be a twist for a quantum groupoid H. Then there
is a quantum groupoid HΘ having the same algebra structure and counit as H with
a comultiplication and antipode given by
∆ Θ (h) = ¯Θ∆( h)Θ, S Θ (h) = v−1S(h)v,(52)
for all h ∈HΘ , where v =m(S ⊗ id)Θ is invertible in HΘ .
Proof. The proof is a straightforward veriﬁcation, see [EN] for details.
Remark 6.1.3. (a) One can check that the counital maps of the twisted quantum
groupoid HΘ are given by
(εt)Θ (h) = ε(Θ (1)h)Θ (2), (εs)Θ (h) = ¯Θ (1)ε(h ¯Θ (2)).
(b) It is possible to generalize the above twisting construction by we akening the
counit condition (47) and requiring only the existence of u,w ∈H such that
ε(Θ (1)w)Θ (2) = Θ (1)ε(Θ (2)w) = 1, ε (u ¯Θ (1)) ¯Θ (2) = ¯Θ (1)ε(u ¯Θ (2)) = 1.(53)
Then the counit of the twisted quantum groupoid HΘ is
εΘ (h) = ε(uhw), h ∈H.(54)
(c) If (Θ , ¯Θ) is a twist for H and x ∈ H is an invertible element such that
εt(x) = εs(x) = 1 then (Θ x, ¯Θ x), where
Θ x = ∆( x)−1Θ(x ⊗x) and ¯Θ x = (x−1 ⊗x−1) ¯Θ∆( x),
is also a twist for H. The twists (Θ , ¯Θ) and (Θ x, ¯Θ x) are called gauge equiv-
alent and x is called a gauge transformation . Given such an x, the map
h ↦→x−1hx is an isomorphism between quantum groupoids HΘ and HΘ x.
