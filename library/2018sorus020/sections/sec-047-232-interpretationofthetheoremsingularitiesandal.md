---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-047-232-interpretationofthetheoremsingularitiesandal
section_title: "InterpretationoftheTheorem:singularitiesandAlexan-"
section_number: 2.3.2
pages: 58-65
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
der module
The aim of this section is to provide a geometric signiﬁcation to the length of the
module H1(M, Ad◦ρ)v that appears in the statement of the Main Theorem 1.
Notice that ifv corresponds to an irreducible character,H1(M, Ad◦ρ)v≃ Ω ¯B[Γ]/k⊗
Ov. If ν(v) is a smooth point, the latter is isomorphic to the localization of the
moduleofdiﬀerentialsat v :H1(M, Ad◦ρ)v≃ ΩOv/k,andthisissimply Ov.Hencewe
are interessed by the cases whenν(v) is not a smooth point ofY, or does correspond
to a reducible character. This case is a singular case too : herev corresponds in
X(M) to an intersection point of a component of irreducible type and the reducible
component. We treat both cases.
Singularities at irreducible characters
One has the following exact sequence0→T→ Ω ¯B[Γ]/k⊗O v→ ΩOv/k provided by
the normalization mapν. Thus length(T ) is an invariant of the branch ofv at the
singularityν(v). We do not know any general formula, but we are able to compute
it directly if a curve equation is given. Notice that this general question relies on
the (still open) following problem : given a point of a curvex∈ X, is it true that
x is smooth iﬀΩOx/k≃O x? See [Ber94] for a survey of the topic. We treat some
examples of plane singularities.
Assume x = (0, 0)∈ k2, andC is the curve deﬁned by the polynomialXp−Yq,
with p<q . The singular pointx has multiplicityp; pick ˜x a pre-image ofx by the
57
normalization ν : ˜C→ C, and denote its discrete valuation ring byO. Denote by
n = gcd(p,q ),p′ = p
n,q′ = q
n. The normalizationν : A1
k→C is given by
k[X,Y ]/(Xp−Yq)→k[S]
X↦→Sq′
,Y ↦→Sp′
We compute ΩOx/k =OxdX⊕O xdY/ (pXp−1dX−qY q−1dY ), thus ΩOx/k⊗O =
OdX⊕OdY/ (pSq′(p−1)dX−qSp′(q−1)dY ). The morphismΩOx/k⊗O→ ΩO/k sends
dX to q′Sq′−1dS and dY to p′Sp′−1dS. The kernel of this morphism is generated
by p′dX−q′Sq′−p′
dY ∈ ΩOx/k⊗O , and its annihilator is(nSq′(p−1)). HenceT ≃
O/(Sq′(p−1)) and length(T ) =q′(p− 1).
Singularities at reducible characters
In this section we focus onv∈ Y that corresponds to a reducible character. It is
precisely the case when it corresponds to an intersection point of the component
of irreducible type corresponding toY with the reducible component. By Section
1.3.11, we can pick the tautological representation ρ : Γ → SL2(Ov) to be not
residually abelian.
We need to study theOv-module H1(M, Ad◦ρ)v, but here we do not dispose of
an interpretation in terms of the cotangent space. The strategy is the following :
recall that we can writeH1(M, Ad◦ρ)v =Ov⊕
l⨁
i=1
Ov/(tni), so we need to compute
∑
ini. First we considerH1(M, Ad◦ρ)v⊗O v/(t)≃ H1(M, Ad◦¯ρ), it is ak-vector
space whose dimension will be the integerl + 1. Then we prove that under some
hypothesis, all of theni’s are equal to1.
Up to conjugacy, we know that we can ﬁx the tautological representationρ : Γ→
SL2(Ov) such that∀γ ∈ Γ, ¯ρ(γ) =
(
λϕ(γ) λ−ϕ(γ)u(γ)
0 λ−ϕ(γ)
)
for some λ ∈ k∗ such that
∆M(λ2) = 0, see Section 1.4.2.
Lemma 2.3.12.TheOv-moduleH0(M, Ad◦ρ)v is trivial.
Proof. Using twice the Universal Coeﬃcient Theorem, we have
H0(M, Ad◦ρ)⊗OvOv/(t)≃H0(M, Ad◦¯ρ)≃H0(M, Ad◦¯ρ)∗
and the last term is trivial since¯ρ is not abelian.
This section aims to relate the order of the torsion at such a ﬁnite pointv where
58
the tautological representation is residually reducible, with the order ofλ2 as a root
of the Alexander polynomial. We will denote byC∗(M,kλ±2) the complex of group
cohomology of Γ with coeﬃcients ink twisted by the action ofλ2, resp. λ−2. As
we proved in Section 1.4.2, the mapu : Γ→ k is a non trivial cocycle in the ﬁrst
cohomology groupH1(M,λ 2).
Let ﬁx some notations : the adjoint action of¯ρ on sl2(k) has the following matrix in
the basis{E,H,F } :
Ad◦¯ρ =


λ2 −2u −λ−2u2
0 1 λ−2u
0 0 λ−2

 (2.2)
The Γ-module sl2(k) will be denoted by Ad◦¯ρ, and K will be the submodule
spank⟨E,H⟩ with the induced Γ-action given by
(λ2−2u
0 1
)
. We denote bykλ−2 the
submodule spank⟨F⟩. From the matrix (2.2) we obtain the splitting ofΓ-modules :
0→K→ Ad◦¯ρ→kλ−2→ 0
that gives rise to the long exact sequence :
0→H1(M,K )→H1(M, Ad◦¯ρ)→H1(M,λ−2)
→H2(M,K )→H2(M, Ad◦¯ρ)→H2(M,λ−2)→ 0 (2.3)
Notice thatH0(M,λ 2) is trivial as soon as there existsγ∈ Γ such thatλ2(γ)⁄= 1,
i.e. as soon as¯ρ is not central as a character.
Similarly, theΓ module K splits as :
0→kλ2→K→k→ 0
wherekλ2 denotes the submodulespank⟨E⟩ andk denotes the submodulespank⟨H⟩,
hence we obtain the following exact sequence
0→H0(M,k )→H1(M,λ 2)→H1(M,K )
→H1(M,k )
δ
− →H2(M,λ 2)→H2(M,K )→ 0 (2.4)
59
Deﬁnition 2.3.13.We deﬁne thecup-bracket :
[.∪.] :H1(Γ, Ad◦¯ρ)×H1(Γ, Ad◦¯ρ)→H2(Γ, Ad◦¯ρ)
(ζ1,ζ 2)↦→ ([ζ1∪ζ2] : (γ,δ )↦→ [ζ1(γ), Ad◦¯ρ(γ)ζ2(δ)])
Deﬁnition 2.3.14.We deﬁne the ﬁrst order deformation of¯ρ as the map ξ ∈
C1(M, Ad◦¯ρ) such that in SL2(Ov/(t2)), the mod (t2)-reduced tautological repre-
sentation is given byρ′ = (Id +tξ)¯ρ.
The following lemma recalls the fact of deformation theory (see [Gol84, section 1.4]
forinstance)that ξ isacocyclein H1(M, Ad◦¯ρ)andthat [ξ∪ξ] = 0inthiscontext,in
other words,ξ lies in the kernel of the morphismB :H1(M, Ad◦¯ρ)→H2(M, Ad◦¯ρ)
that sends a cocycleζ on the cup-bracket[ζ∪ξ].
Lemma 2.3.15. The ﬁrst order deformationξ of ρ is a cocycle, andB(ξ) = 0 ∈
H2(M, Ad◦¯ρ).
Proof. The ﬁrst claims follows from the fact that, for allγ,δ ∈G,ρ′(γδ) =ρ′(γ)ρ′(δ)
mod(t2). Moreover, letρ′′ = (Id +tξ +t2η)¯ρ be the mod(t3) representation : Γ →
SL2(Ov/(t3)). Again,ρ′′ is a group homomorphism, hence a direct computation gives
η(γδ) = η(γ) + Ad◦¯ρ(γ)η(δ) +ξ(γ) Ad◦¯ρ(γ)ξ(δ). This equality can be written as
dη(γ,δ ) =ξ∪ξ(γ,δ )∈H2(Γ, Ad◦¯ρ⊗ Ad◦¯ρ), henceξ∪ξ = 0. On the other hand,
dξ2(γ,δ ) =ξ2(γδ)−ξ2(γ)− Ad◦¯ρ(γ)ξ2(δ)
= (ξ(γ) + Ad◦¯ρ(γ)ξ(δ))2−ξ2(γ)− Ad◦¯ρ(γ)ξ2(δ)
=ξ2(γ) +ξ(γ) Ad◦¯ρ(γ)ξ(δ) + Ad◦¯ρ(γ)(ξ(δ))ξ(γ)
+ (Ad◦¯ρ(γ)ξ(δ))2−ξ2(γ)− (Ad◦¯ρ(γ)ξ(δ))2
=ξ(γ) Ad◦¯ρ(γ)ξ(δ) + Ad◦¯ρ(γ)(ξ(δ))ξ(γ)
=−[ξ∪ξ](γ,δ ) + 2ξ∪ξ(γ,δ )
hence [ξ∪ξ] =d(2η−ξ2) = 0∈H2(Γ, Ad◦¯ρ).
The theorem is the following :
Theorem 2.3.16. Let v ∈ Y a ﬁnite point, assume that the tautological repre-
sentation ρ : Γ → SL2(Ov) is residually reducible with residual representation
¯ρ(γ) =
(
λϕ(γ) λ−ϕ(γ)u(γ)
0 λ−ϕ(γ)
)
and denote byr≥ 1 the order ofλ2 as a root of the Alexan-
der poynomial ∆M. Assume moreover that the morphismB has maximal rank, i.e.
kerB =k⟨ξ⟩. Then the torsion form’s vanishing order atv is bounded by2r− 2.
60
Remark 2.3.17. In the generic case whenλ2 is a simple root, then the technical
assumption is automatically satisﬁed and the theorem always holds : thus in this
case tor(M, Ad◦ρ) does not vanish atv.
Proof. Asλ2 is a root of orderr of the Alexander polynomial, the Alexander module
H1(M,k [t±1]ϕ) has (t−λ2)-length equal tor, in other words, its(t−λ2)-torsion is of
the form
l⨁
i=1
k[t±1]
(t−λ2)ni with
l∑
i=1
ni =r. In particular1≤l≤r and from the Universal
Coeﬃcients Theorem, one obtains thatdimH1(M,λ 2) =l∈{ 1,...r}. Ifl =r, then
we use Proposition 2.3.19 (postponed at the end of this section) to conclude that the
mapδ in the sequence (2.4) is injective, hencedimH1(M,K ) = dimH1(M,λ 2)−1 =
r− 1. Otherwisel≤r− 1, and asdim(H1(M,k )) = 1, again by sequence (2.4) the
inequality dim(H1(M,K ))≤r− 1 holds.
Now we consider the sequence (2.3). As the Alexander polynomial is symmetric, we
know that dim(H1(M,λ−2)) = dim(H1(M,λ 2))≤ r. A careful observation of this
exact sequence is now enough to prove thatdimH1(M, Ad◦¯ρ)≤ 2r− 1. We denote
this dimension bym.
Consider the sequence ofΓ-modules
0→ sl2(Ov/(t))
.t
− →sl2(Ov/(t2))
mod t
−−−→sl2(Ov/(t))→ 0
From this we get
0→H1(M, Ad◦¯ρ)→H1(M, Ad◦ρ′)
p
− →H1(M, Ad◦¯ρ)
B
− →H2(M, Ad◦¯ρ)→H2(M, Ad◦ρ′)→H2(M, Ad◦¯ρ)→ 0 (2.5)
where Ad◦ρ′ denotes the homology of the complex with coeﬃcients insl2(Ov/(t2)).
By Lemma 2.3.18 below, the connection operator is nothing but the mapB we
deﬁned above.
We write H1(M, Ad◦ρ)v = Ov⊕
m−1⨁
i=1
Ov/(tni), hence we have H1(M, Ad◦¯ρ) =
Ov/(t)⊕⨁
iOv/(t). Moreover we haveH1(M, Ad◦ρ′)≃O v/(t2)⊕⨁
iOv/(tmin(ni,2)),
and by the Universal Coeﬃcients Theorem,
H1(M, Ad◦ρ′)≃ Hom(H1(M, Ad◦ρ′),Ov/(t2))≃H1(M, Ad◦ρ′)
61
The ﬁrst terms of equation (2.5) become
0→O v/(t)⊕
⨁
i
Ov/(t)
i
− →Ov/(t2)⊕
⨁
i
Ov/(tmin(ni,2))
p
− →Ov/(t)⊕
⨁
i
Ov/(t)
B
− →...
The image ofp is the kernel ofB, thus it is a copy ofOv/(t) generated byξ. Hence
the image ofi isOv/(t)⊕⨁
iOv/(tmin(ni,2)), and a simple count of dimensions proves
thatni = 1forall i.Inconclusion H1(M, Ad◦ρ)v≃O v⊕(Ov/(t))m−1 andthetorsion
vanishes at orderm− 1≤ 2r− 2.
Lemma 2.3.18. The connexion operator in the sequence (2.5) is the map B :
H1(M, Ad◦¯ρ)→H2(M, Ad◦¯ρ), ζ↦→ [ξ∪ζ].
Proof. We draw the diagram
C1(M, Ad◦ρ) C1(M, Ad◦ρ′) C1(M, Ad◦ρ)
C2(M, Ad◦ρ) C2(M, Ad◦ρ′) C2(M, Ad◦ρ)
0
0
0
0
d d d
with exact rows. We pickζ∈ Z1(M, Ad◦ρ), and we lift it to˜ζ∈ C1(M, Ad◦ρ′).
Forγ,δ ∈ Γ, we computed˜ζ(γ,δ ) = ˜ζ(γ) + Ad◦¯ρ(γ)˜ζ(δ) +t(ξ(γ) Ad◦¯ρ(γ)˜ζ(δ)−
Ad◦¯ρ(γ)˜ζ(δ)ξ(γ)) = ˜dζ(γ,δ ) +t[ξ∪ζ](γ,δ ). Asdζ = 0, the result follows.
Proposition 2.3.19. If dimH1(M,λ 2) = r, then the morphismδ : H1(M,k )→
H2(M,λ 2) is injective.
The proof consists of the following succession of lemmas.
Lemma 2.3.20.The morphismδ :H1(M,k )→H2(M,λ 2) is the mapϕ↦→ 2u∪ϕ.
Proof. Again, we draw the diagram
C1(M,λ 2) C1(M,K ) C1(M,k )
C2(M,λ 2) C2(M,K ) C2(M,k )
0
0
0
0
d d d
with exact rows.
Pickϕ∈C1(M,k ) such thatdϕ = 0. Take˜ϕ∈C1(M,K ) deﬁned by˜ϕ(γ) =ϕ(γ)H.
Then computed ˜ϕ(γ,δ ) = ˜ϕ(γδ)− ˜ϕ(γ)−γ. ˜ϕ(δ) Observe that by the adjoint matrix
62
(2.2) we haveγ. ˜ϕ(δ) = Ad◦¯ρ(γ)|K
˜ϕ(δ) = ˜ϕ(δ)− 2u(γ)ϕ(δ)E. Asϕ∈Z1(M,k ), we
get that ˜ϕ(γδ) = ˜ϕ(γ) + ˜ϕ(δ), thus
d ˜ϕ(γ,δ ) =−2u(γ)ϕ(δ)E
The conclusion follows.
The multiplication byt−λ2 induces the splitting ofΓ-modules :
0→k[t±1]ϕ
t−λ2
− −− →k[t±1]ϕ→kλ2→ 0 (2.6)
Lemma 2.3.21.The sequence above induces the following long exact sequence :
0→H1(M,λ 2)→H1(M,k [t±1]ϕ)→H1(M,k [t±1]ϕ)→H2(M,λ 2)→ 0 (2.7)
Proof. Let’s write the long exact sequence in homology induced by (2.6)
...→H1(M,λ 2)→H2(M,k [t±1]ϕ)→H2(M,k [t±1]ϕ)→H2(M,λ 2)→...
First, let’s prove that the ﬁrst and the last arrows of this sequence are0’s. We
remark that the missing term on the right isH3(k[t±1])≃ 0. Then as the missing
term on the left isH1(k[t±1]ϕ)≃ Ext(H0(M,k [t±1]ϕ),k [t±1])≃k[t±1]/(t− 1) by the
universal coeﬃcients theorem, we obtain that the map induced by multiplication by
t−λ2
H1(M,k [t±1]ϕ)
.(t−λ2)
−−−−→H1(M,k [t±1]ϕ)
is surjective, thus the ﬁrst map on the left isH1(M,k [t±1]ϕ)
0
− →H1(M,λ 2).
Now, we have the universal coeﬃcients theorem that gives the following isomorphism
H2(M,k [t±1]ϕ)≃ Ext(H1(M,k [t±1]ϕ),k [t±1]). SinceH1(M,k [t±1]ϕ) is a torsion mo-
dule, the latter isH1(M,k [t±1]ϕ) itself, that ends the proof of the lemma.
We denote byθ :H1(M,λ 2)→H2(M,λ 2) the composition of the ﬁrst and the third
map in the sequence (2.7).
Lemma 2.3.22.θ(z) =λ−2ϕ∪z, in particular2λ2θ(u) =δ(ϕ).
Proof. Again, consider the sequence :
0→H1(M,λ 2)→H2(M,k [t±1]ϕ)→H2(M,k [t±1]ϕ)→H2(M,λ 2)→ 0
63
Then the same kind of computation as in the proof of Lemmas 2.3.18 and 2.3.20
gives the result. We sketch the proof : givenz∈ H1(M,λ 2), ﬁrst lift it as˜z(t)∈
C1(M,k [t±1]ϕ). Denote byD :C1(M,k [t±1]ϕ)→C2(M,k [t±1]ϕ) the boundary map;
then send ˜z on D˜z(t)
t−λ2 ∈C2(M,k [t±1]ϕ), and then take the evaluation att =λ2. The
result is precisely d
dt
⏐⏐
t=λ2D˜z(t) =λ−2ϕ∪z∈H2(M,λ 2)
Lemma 2.3.23.If dim(H1(M,λ 2)) =r, then the mapθ is an isomorphism.
Proof. Consider the endomorphism A of H1(M,k [t±1]ϕ) induced by the multipli-
cation by (t−λ2). Its kernel (and cokernel) is exactly
r⨁
i=1
k[t±1]
(t−λ2) because teh di-
mension of the vector space(H1(M,λ 2)) is equal tor, henceθ is an isomorphism
kerA→ cokerA.
Proof of Proposition 2.3.19.The mapθ is an isomorphism, in particularθ(u)⁄= 0,
hence δ(ϕ)⁄= 0 and δ is injective.
