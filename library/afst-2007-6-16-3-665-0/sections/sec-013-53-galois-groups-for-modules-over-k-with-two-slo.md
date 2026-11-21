---
doc_id: afst-2007-6-16-3-665-0
doc_title: "Galois theory of q-difference equations"
section_id: sec-013-53-galois-groups-for-modules-over-k-with-two-slo
section_title: "Galois groups for modules over K with two slopes"
section_number: 5.3
pages: 35-38
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
toc_source: inferred
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
Let the q-diﬀerence module M over K be given by an exact sequence
0 →P1 →M →P2 →0, where P1, P2 are pure with slopes λ1 < λ2. The
Picard-Vessiot ring PV (M) of M contains PV (P1 ⊕P2), the Picard-Vessiot
ring of P1 ⊕P2. Thus there is an exact sequence 1 →H →G →G′ →1,
where G and G′ are the diﬀerence Galois groups of M and P1 ⊕P2. The
group G′ has been calculated in subsections 5.1 and 5.2. Further, H is the
diﬀerence Galois group of the extension PV (P1 ⊕P2) ⊂PV (M).
Let V1, V2, V denote the solution spaces for P1, P2, M. There is an obvi-
ous exact sequence 0 →V1 →V →V2 →0. The space V1 is invariant under
the action of G on V and the induced action of G on gr(V ) := V1 ⊕V2
coincides with G′. Hence H can be identiﬁed with a C-vector space of linear
maps from V2 to V1. Indeed, for h ∈H, the kernel of h −1 contains V1 and
the image of h −1 lies in V1. In other words, H can be identiﬁed with a
linear subspace W of V ∗
2 ⊗C V1, which is the solution space of P ∗
2 ⊗K P1.
For any diﬀerence module N over K we write 
N for the diﬀerence module
K ⊗K N over K. Consider the split exact sequence
0 →P1 →

M →P2 →0.
– 698 –
Galois theory of q-diﬀerence equations
The splitting P2 →

M is unique since the only morphism P2 →P1 of
q-diﬀerence modules over K is the zero map. Moreover, the canonical mor-
phism K ⊗PV (P1 ⊕P2) →PV (

M) is an isomorphism. The resulting
embedding PV (P1 ⊕P2) ⊂PV (

M) extends in a unique way to an em-
bedding PV (M) ⊂PV (

M). The solution space V of M can be deﬁned as
ker(Φ−1, K⊗K Univ⊗K M). Similar expressions are valid for V1, V2, the so-
lution spaces of P1, P2. Write G′′ for the diﬀerence Galois group of PV (

M).
The restriction map induces an isomorphism G′′ →G′. We conclude that
the exact sequences
1 →H →G →G′ →1 and 0 →V1 →V →V2 →0
have canonical splittings. Write V = V1 ⊕V2 for this splitting, then G′
(or G′′) can be identiﬁed with the subgroup of G leaving both V1 and V2
invariant. Thus G is the semi-direct product H ⋊G′. The exact sequence,
deﬁning M, is given by an element ξ ∈coker(Φ−1, Hom(P2, P1)). The main
issue is to derive H (or W) from the given ξ and to formulate ξ in terms of
the solution spaces V1, V2.
Let N be a pure diﬀerence module with slope λ < 0 and solution space
V (N). Our ﬁrst aim is to formulate coker(Φ −1, N) in terms of V (N).
Lemma 5.7. — Let N be a pure module with slope λ < 0. The canonical
map a →1 ⊗a from N to Univ ⊗K N induces an injective map
coker(Φ −1, N) →coker(Φ −1, Univ ⊗K N)
whose image consists of the elements which are invariant under the universal
group Guniv.
Proof. — It
suﬃces
to
consider
a
pure,
indecomposable
N
=
Res(E(dzt/n))⊗Um. By writing N as an extension of Res(E(dzt/n))⊗Um−1
by Res(E(dzt/n)), one is reduced to verify the lemma for Res(E(dzt/n)).
For notational reasons we write R = L ⊕Q for some Q-vector space L.
Let C ⊂C∗denote the elements c of the form e2πi(a0+a1τ) with a1 ∈L.
Then we can write Univ = ⊕c∈C,λ∈QK∞[ℓ]e(czλ). Then Univ ⊗K N =
⊕K∞[ℓ]e(czλ) ⊗K N. Each direct summand is invariant under the action
of Φ and Guniv. The cokernel of Φ −1 of each direct summand has a cer-
tain Guniv-action. Using the topological generators Γ, ∆, D of this group,
one ﬁnds that only the direct summand K∞[ℓ] ⊗K N can produce Guniv-
invariant elements in the cokernel of Φ −1. A further inspection shows
that this contribution comes from the subspace K ⊗K N. Thus we ﬁnd the
required bijection.
□
– 699 –
Marius van der Put, Marc Reversat
We observe that Univ ⊗K N = Univ ⊗C V (N), where the solution space
V (N) of N is deﬁned as ker(Φ −1, Univ ⊗K N). The Guniv-invariant part
of coker(Φ −1, Univ ⊗C V (N)), comes from K[{e(c)}, ℓ]e(z−λ) ⊗C V (N),
where D acts as the identity. We conclude the following.
Lemma 5.8. — Let N be a pure module with slope λ < 0 and solution
space V (N). Then coker(Φ −1, N) can be identiﬁed with the C-linear sub-
space of
(coker(φ −1, K[{e(c)}, ℓ]e(z−λ)) ⊗C V (N),
consisting of the elements invariant under Γ and ∆.
Lemma 5.9. — Let λ < 0. The subspace H(λ) :={⊕|q|−λ<|c|⩽1Ce(cz−λ)}[ℓ]
of K[{e(c)}, ℓ]e(z−λ) has the following properties:
H(λ) →coker(φ −1, K[{e(c)}, ℓ]e(z−λ)) is bijective and
H(λ) is invariant under the actions of Γ, ∆and D.
Proof. — From Theorem 2.5 it follows that we may, for the calculation of
this cokernel, replace K by C[z, z−1]. After replacing z by e(q−1), we have
to compute the coker of φ −1 on the space {⊕c̸=0Ce(cz−λ)}[ℓ]. Using 2.6
one ﬁnds that H(λ) has the ﬁrst property. An inspection of the actions of
Γ, ∆, D yields the second property.
□
Corollary 5.10. — The canonical map coker(Φ −1, N) →(H(λ) ⊗
V (N))<Γ,∆> (i.e., the elements invariant under the group generated by Γ
and ∆) is an isomorphism.
Corollary 5.11. — The exact sequences 0 →P1 →M →P2 →0
(with P1, P2 pure modules with slopes λ1 < λ2 and solution spaces V1, V2)
are in bijection with the elements of (H(λ1 −λ2) ⊗Hom(V2, V1))<Γ,∆>.
Theorem 5.12. — Let the diﬀerence module M be given by an exact
sequence 0 →P1 →M →P2 →0 with P1, P2 pure modules with slopes
λ1 < λ2. Let V1, V2 denote the solution spaces of P1, P2 and write V =
V1 ⊕V2 for the solution space of M.
Let ξ ∈coker(Φ −1, Hom(P2, P1)) and its image
ξ′ ∈(H(λ1 −λ2) ⊗Hom(V2, V1))<Γ,∆> which represents the exact sequence.
Deﬁne W ⊂Hom(V2, V1) to be the smallest subspace such that
ξ′ ∈H(λ1 −λ2) ⊗C W. Then:
The diﬀerence Galois group G ⊂GL(V ) of M is the semi-direct product
G = H ⋊G′ with: G′ = {g ∈G|g(Vi) = Vi for i = 1, 2} is the diﬀerence
– 700 –
Galois theory of q-diﬀerence equations
Galois group of P1⊕P2 and H consists of the linear maps of the form id+ ˜w
where ˜w is equal to V
pr2
→V2
w→V1 ⊂V with w ∈W.
Proof. — It suﬃces to prove the last statement. For any submodule N
of Hom(P2, P1) one considers the exact sequence 0 →N →Hom(P2, P1) →
N ′ →0. This gives rise to an exact sequence
0 →coker(Φ−1, N) →coker(Φ−1, Hom(P2, P1)) →coker(Φ−1, N ′) →0 .
It follows that there exists a smallest submodule N0 such that ξ lies in
coker(Φ −1, N0). The solution space V (N0) lies in Hom(V2, V1) and ξ′ be-
longs to H(λ1 −λ2) ⊗V (N0) (and is invariant under < Γ, ∆>).
It is clear that H identiﬁes with {id + ˜w| w ∈W1} for some W1 ⊂
Hom(V2, V1) which is invariant under the action of the diﬀerence Galois
group of Hom(P2, P1), acting upon its solution space Hom(V2, V1). In other
words, W1 is invariant under < Γ, ∆>. By Tannakian correspondence,
W1 corresponds to a submodule N1 of Hom(P2, P1). Moreover, ξ lies in
coker(Φ −1, N1).
One concludes that N0 = N1 and that W = W1.
□
The elements {e(cz−λ)ℓm}|q|−λ<|c|⩽1; m⩾0, with λ := λ1 −λ2, form a
C-basis of H(λ1 −λ2). Thus ξ′ can be written uniquely as  e(cz−λ)ℓm
⊗w(c, m) with all w(c, m) ∈Hom(V2, V1). Then W is the subspace of
Hom(V2, V1) generated by {w(c, m)}. This observation makes it possible
to compute the diﬀerence Galois group for explicit examples.
