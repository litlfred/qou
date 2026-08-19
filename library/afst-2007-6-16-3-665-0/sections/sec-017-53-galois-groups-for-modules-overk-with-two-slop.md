---
doc_id: afst-2007-6-16-3-665-0
doc_title: "ANNALES DE LA FACULTÉ DES SCIENCES Mathématiques"
section_id: sec-017-53-galois-groups-for-modules-overk-with-two-slop
section_title: "Galois groups for modules overK with two slopes"
section_number: 5.3
pages: 35-38
source_pdf: AFST_2007_6_16_3_665_0.pdf
source_sha256: 402b61574e561f86
doc_brief: "Galois theory of q-difference equations (van der Put–Reversat, Ann. Fac. Sci. Toulouse XVI:3, 2007, 665–718) — Galois-theoretic framework for q-difference equations."
---
Let theq-diﬀerence moduleM over K be given by an exact sequence
0 →P1 →M →P2 → 0, whereP1,P 2 are pure with slopesλ1 <λ 2. The
Picard-Vessiot ringPV (M)o fM containsPV (P1 ⊕P2), the Picard-Vessiot
ring ofP1 ⊕P2. Thus there is an exact sequence 1→ H → G → G′ → 1,
where G and G′are the diﬀerence Galois groups ofM and P1 ⊕P2. The
group G′has been calculated in subsections 5.1 and 5.2. Further,H is the
diﬀerence Galois group of the extensionPV (P1 ⊕P2) ⊂PV (M).
LetV1,V 2,V denote the solution spaces forP1,P 2,M. There is an obvi-
ous exact sequence 0→V1 →V →V2 →0. The spaceV1 is invariant under
the action ofG on V and the induced action ofG on gr(V): =V1 ⊕V2
coincides withG′. HenceH can be identiﬁed with aC-vector space of linear
maps fromV2 toV1. Indeed, forh ∈H, the kernel ofh −1 containsV1 and
the image ofh −1 lies inV1. In other words,H can be identiﬁed with a
linear subspaceW ofV ∗
2 ⊗CV1, which is the solution space ofP ∗
2 ⊗K P1.
Foranydiﬀerencemodule N overK wewrite ˆN forthediﬀerencemodule
ˆK ⊗K N over ˆK. Consider the split exact sequence
0 → ˆP1 → ˆM → ˆP2 →0.
– 698 –
Galois theory ofq-diﬀerence equations
The splitting ˆP2 → ˆM is unique since the only morphism ˆP2 → ˆP1 of
q-diﬀerence modules overˆK is the zero map. Moreover, the canonical mor-
phism ˆK ⊗ PV (P1 ⊕ P2) → PV ( ˆM) is an isomorphism. The resulting
embedding PV (P1 ⊕P2) ⊂ PV ( ˆM) extends in a unique way to an em-
bedding PV (M) ⊂PV ( ˆM). The solution spaceV of M can be deﬁned as
ker(Φ−1, ˆK ⊗KUniv ⊗KM).Similarexpressionsarevalidfor V1,V 2,theso-
lution spaces ofP1,P 2. WriteG′′for the diﬀerence Galois group ofPV ( ˆM).
The restriction map induces an isomorphismG′′→ G′. We conclude that
the exact sequences
1 →H →G →G′→1 and 0→V1 →V →V2 →0
have canonical splittings. WriteV = V1 ⊕V2 for this splitting, thenG′
(or G′′) can be identiﬁed with the subgroup ofG leaving bothV1 and V2
invariant. ThusG is the semi-direct productH ⋊G′. The exact sequence,
deﬁningM, is given by an elementξ ∈coker(Φ−1,Hom(P2,P 1)). The main
issue is to deriveH (orW) from the givenξ and to formulateξ in terms of
the solution spacesV1,V 2.
LetN be a pure diﬀerence module with slopeλ< 0 and solution space
V(N). Our ﬁrst aim is to formulate coker(Φ−1,N) in terms ofV(N).
Lemma 5.7.—L etN be a pure module with slopeλ< 0. The canonical
map a ↦→1 ⊗a fromN to Univ ⊗K N induces an injective map
coker(Φ −1,N) →coker(Φ −1,Univ ⊗K N)
whose image consists of the elements which are invariant under the universal
group Guniv.
Proof.— It suﬃces to consider a pure, indecomposable N =
Res(E(dzt/n))⊗Um.Bywriting N asanextensionof Res(E(dzt/n))⊗Um−1
by Res(E(dzt/n)), one is reduced to verify the lemma forRes(E(dzt/n)).
For notational reasons we writeR = L ⊕ Q for some Q-vector spaceL.
Let C ⊂ C∗ denote the elementsc of the forme2πi(a0+a1τ ) with a1 ∈ L.
Then we can writeUniv = ⊕c∈C,λ∈QK∞[𝓁]e(czλ). Then Univ ⊗K N =
⊕K∞[𝓁]e(czλ) ⊗K N. Each direct summand is invariant under the action
of Φ andGuniv. The cokernel of Φ−1 of each direct summand has a cer-
tain Guniv-action. Using the topological generators Γ,∆,D of this group,
one ﬁnds that only the direct summandK∞[𝓁] ⊗K N can produce Guniv-
invariant elements in the cokernel of Φ− 1. A further inspection shows
that this contribution comes from the subspaceK ⊗K N. Thus we ﬁnd the
required bijection. □
– 699 –
Marius van der Put, Marc Reversat
We observe thatUniv ⊗KN =Univ ⊗CV(N), where the solution space
V(N)o fN is deﬁned as ker(Φ−1,Univ ⊗K N). The Guniv-invariant part
of coker(Φ−1,Univ ⊗C V(N)), comes fromK[{e(c)},𝓁]e(z−λ) ⊗C V(N),
whereD acts as the identity. We conclude the following.
Lemma 5.8.—L et N be a pure module with slopeλ< 0 and solution
spaceV(N). Thencoker(Φ −1,N) can be identiﬁed with theC-linear sub-
space of
(coker(φ −1,K[{e(c)},𝓁]e(z−λ)) ⊗CV(N),
consisting of the elements invariant underΓ and ∆.
Lemma 5.9.—L etλ< 0. The subspaceH(λ): ={⊕|q|−λ<|c|⩽1Ce(cz−λ)}[𝓁]
of K[{e(c)},𝓁]e(z−λ) has the following properties:
H(λ) →coker(φ −1,K[{e(c)},𝓁]e(z−λ)) is bijective and
H(λ) is invariant under the actions ofΓ,∆ and D.
Proof.— FromTheorem2.5itfollowsthatwemay,forthecalculationof
this cokernel, replaceK by C[z,z −1]. After replacingz bye(q−1), we have
to compute the coker ofφ −1 on the space{⊕c⁄=0Ce(cz−λ)}[𝓁]. Using 2.6
one ﬁnds thatH(λ) has the ﬁrst property. An inspection of the actions of
Γ,∆,D yields the second property. □
Corollary 5.10.— The canonical map coker(Φ − 1,N) → (H(λ) ⊗
V(N))<Γ,∆> (i.e., the elements invariant under the group generated byΓ
and ∆) is an isomorphism.
Corollary 5.11.— The exact sequences 0 → P1 → M → P2 → 0
(with P1,P 2 pure modules with slopesλ1 <λ 2 and solution spacesV1,V 2)
are in bijection with the elements of(H(λ1 −λ2) ⊗Hom(V2,V 1))<Γ,∆>.
Theorem 5.12.— Let the diﬀerence moduleM be given by an exact
sequence 0 → P1 → M → P2 → 0 with P1,P 2 pure modules with slopes
λ1 <λ 2.L e tV1,V 2 denote the solution spaces ofP1,P 2 and write V =
V1 ⊕V2 for the solution space ofM.
Letξ ∈coker(Φ −1,Hom(P2,P 1)) and its image
ξ′∈(H(λ1 −λ2) ⊗Hom(V2,V 1))<Γ,∆> which represents the exact sequence.
Deﬁne W ⊂Hom(V2,V 1) to be the smallest subspace such that
ξ′∈H(λ1 −λ2) ⊗CW. Then:
The diﬀerence Galois groupG ⊂GL(V) ofM is the semi-direct product
G = H ⋊G′with: G′= {g ∈ G|g(Vi)= Vi for i =1 ,2} is the diﬀerence
– 700 –
Galois theory ofq-diﬀerence equations
Galois group ofP1 ⊕P2 andH consists of the linear maps of the formid+˜w
where ˜w is equal toV
pr2
→ V2
w
→V1 ⊂V with w ∈W.
Proof.— It suﬃces to prove the last statement. For any submoduleN
of Hom(P2,P 1) one considers the exact sequence 0→N →Hom(P2,P 1) →
N ′→0. This gives rise to an exact sequence
0 →coker(Φ −1,N) →coker(Φ −1,Hom(P2,P 1)) →coker(Φ −1,N ′) →0.
It follows that there exists a smallest submoduleN0 such that ξ lies in
coker(Φ −1,N 0). The solution spaceV(N0) lies in Hom(V2,V 1) andξ′be-
longs toH(λ1 −λ2) ⊗V(N0) (and is invariant under<Γ,∆>).
It is clear thatH identiﬁes with {id +˜w| w ∈ W1} for some W1 ⊂
Hom(V2,V 1) which is invariant under the action of the diﬀerence Galois
group of Hom(P2,P 1), acting upon its solution space Hom(V2,V 1). In other
words, W1 is invariant under< Γ,∆ >. By Tannakian correspondence,
W1 corresponds to a submoduleN1 of Hom(P2,P 1). Moreover,ξ lies in
coker(Φ −1,N 1).
One concludes thatN0 =N1 and thatW =W1. □
The elements {e(cz−λ)𝓁m}|q|−λ<|c|⩽1; m/greaterorequalslant0, with λ := λ1 −λ2, form a
C-basis ofH(λ1 −λ2). Thusξ′can be written uniquely as∑ e(cz−λ)𝓁m
⊗w(c,m) with all w(c,m) ∈ Hom(V2,V 1). Then W is the subspace of
Hom(V2,V 1) generated by {w(c,m)}. This observation makes it possible
to compute the diﬀerence Galois group for explicit examples.
