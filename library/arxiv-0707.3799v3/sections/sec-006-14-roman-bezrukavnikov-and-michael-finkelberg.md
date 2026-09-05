---
doc_id: arxiv-0707.3799v3
doc_title: "EQUIVARIANT SATAKE CATEGORY AND KOSTANT-WHITTAKER REDUCTION"
section_id: sec-006-14-roman-bezrukavnikov-and-michael-finkelberg
section_title: "ROMAN BEZRUKAVNIKOV AND MICHAEL FINKELBERG"
section_number: 14
pages: 14-16
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
doc_brief: "EQUIVARIANT SATAKE CATEGORY AND KOSTANT-WHITTAKER REDUCTION — 16 sections: ROMAN BEZRUKAVNIKOV AND MICHAEL FI; ROMAN BEZRUKAVNIKOV AND MICHAEL FI; ROMAN BEZRUKAVNIKOV AND MICHAEL FI"
---
coming from the map Φµ
MV (F)⊗Φν
MV (G)→Φ µ+ν
MV (F∗G) induced by the tensor structure
on ΦMV , and the natural isomorphism
O(Γµ)⋆O(Γ ν) =H•
T×Gm(JGr
µ )⋆H •
T×Gm(JGr
ν )∼=H•
T×Gm(JGr
µ+ν) =O(Γ µ+ν).
The claim follows.□
4.Algebra
4.1.Some properties of the Kostant functorκ ℏ.The following properties of the
Kostant functor will play an important role in the proof of the main results.
Lemma 4.a) The functorsκ, κ ℏ are exact.
b) The functorsκ| Coh
ˇG×Gm
fr (ˇg∗),κ ℏ|HCfr
ℏ
are full embeddings.
Proofis essentially due to B. Kostant, cf. [21].
a) For the exactness ofκ, note that the functor of restrictionF7→F| Υ is exact on
Coh ˇG(ˇg∗), and thenF| Υ is an ˇN−-equivariant coherent sheaf on Υ. Recall that ˇN−
acts on Υ freely, and Υ/ ˇN−≃Σ. Hence the functor of invariantsG7→G ˇN− is exact on
Coh ˇN−(Υ). The exactness ofκfollows.
For the exactness ofκ ℏ, we will prove that both the functors of−ψ-coinvariants, and
ˇN−-invariants are exact, and henceκ ℏ is exact as their composition. It is enough to
check it on the positively gradedℏ-Harish-Chandra bimodules. Then it is enough to
check the exactness on the subcategory ofℏ-Harish-Chandra bimodules with grading
degrees between 0 andnfor a fixedn≫0. Thus it suffices to check the exactness on
the subcategory ofℏ-Harish-Chandra bimodules with nilpotent action ofℏ, and then
it suffices to consider the subcategory ofℏ-Harish-Chandra bimodules with thetrivial
action ofℏ. However, anℏ-Harish-Chandra bimoduleMwith the trivial action ofℏis
nothing else than a ˇG-equivariant coherent sheaf onˇg∗, andM
L
⊗Uℏ(ˇn−)2(−ψ) =M| Υ. In
particular, the functor of−ψ-coinvariants is exact according to the previous paragraph.
For the same reason,M7→(M
L
⊗Uℏ(ˇn−)2 (−ψ)) ˇN− = (M| Υ) ˇN− is exact. This completes
the proof of a).
b)κ| Coh
ˇG×Gm
fr (ˇg∗) is fully faithful since the complement to ( ˇg∗)reg in ˇg∗ has codimen-
sion 2, and the centralizer of a generic regular element is connected.
To prove thatκ ℏ|HCfr
ℏ
is fully faithful, we consider freeℏ-Harish-Chandra bimodules
M1 =U ℏ⊗V 1, M2 =U ℏ⊗V 2, and the following commutative diagram:
(5)
Hom(M1,M 2) ϵ−−−−→Hom(κ ℏM1,κ ℏM2) δ−−−−→Hom(κ ℏM1,κ ℏM2)/ℏyβ
yγ
Hom(M1/ℏ,M 2/ℏ) α−−−−→Hom(κ(M1/ℏ),κ(M 2/ℏ)) ∼−−−−→Hom((κℏM1)/ℏ,(κ ℏM2)/ℏ)
We have just proved thatαis an isomorphism. Moreover,βis surjective since
Hom(Uℏ⊗V 1,U ℏ⊗V 2) = Hom ˇG(V1⊗V ∗
2,U ℏ), and all the ˇG-modules in question are
semisimple. It follows thatγis surjective. On the other hand,γis injective since
EQUIVARIANT SATAKE CATEGORY AND KOSTANT-WHITTAKER REDUCTION 15
κℏM1, κℏM2 are free overk[ℏ]. Now thatγis proved to be an isomorphism, the
compositionδ◦ϵmust be surjective. Henceϵis surjective by Nakayama Lemma. It
remains to prove thatϵis injective. Sinceκ ℏ is exact, it is enough to prove thatκℏM̸= 0
for a nonzero subobjectMof a freeℏ-Harish-Chandra bimoduleM 2. We consider a
nonzero subobjectM/ℏ⊂M 2/ℏof a freeO( ˇg∗)-moduleM 2/ℏ. It suffices to prove that
κM̸= 0. However, the support of any nonzero section of a freeO( ˇg∗)-module is the
whole of ˇg∗, hence its restriction to Υ is nonzero.
The lemma is proved.□
4.2.De-symmetrized Kostant functorκ ℏ.We denote byπthe projection ˇt∗→
ˇt∗/W, and we denote by (π,Id,Id) the projection ˇt∗×(ˇt∗/W)×A 1→ ˇt∗/W× ˇt∗/W×A 1.
ForV∈Rep( ˇG) we are going to describe (π,Id,Id) ∗ϕ(V)∈Coh( ˇt∗×( ˇt∗/W)×A 1).
To this end we consider the universal Verma moduleM ℏ(−ρ) =U ℏ⊗Uℏ(ˇb) k[ℏ][ˇt](−ρ),
andk[ℏ][ ˇt](−ρ) is aU ℏ(ˇb)-module which factors through theU ℏ(ˇt) =k[ℏ][ ˇt]-module
wheret∈ ˇtacts by multiplication byt−ℏρ(t) (recall thatρis the halfsum of positive
roots of ˇg). For anℏ-Harish-Chandra bimoduleMwe setκ ℏ(M) :=M ℏ(−ρ)
L
⊗Uℏ
M
L
⊗Uℏ(ˇn−)2 ψ=k[ℏ][ ˇt](−ρ)
L
⊗Uℏ(ˇb)1 M
L
⊗Uℏ(ˇn−)2 ψ. This is anO( ˇt∗×( ˇt∗/W)×A 1)-
module: the action ofO( ˇt∗×A 1) =U ℏ(ˇt) comes from the fact thatU ℏ(ˇt) normalizes
Uℏ(ˇb), and the action ofO( ˇt∗/W×A 1) is the action of the centerZ(U ℏ) of the second
copy ofU ℏ, as before.
ForV∈Rep( ˇG) we setφ(V) :=κ ℏ(Fr(V)).
Lemma 5.ForV∈Rep( ˇG)we have a canonical isomorphismφ(V)≃(π,Id,Id) ∗ϕ(V).
Proof: We denote byW −
ℏ :=U ℏ⊗Uℏ(ˇn−)ψthe WhittakerU ℏ-module. By a theorem
of Kostant, End Uℏ(W−
ℏ ) =Z(U ℏ), and the categoryAof (U ℏ(ˇn−),ψ)-integrable
Uℏ-modules is equivalent to the category ofZ(U ℏ)-modules (here aU ℏ(ˇn−)-module
Lis called (U ℏ(ˇn−),ψ)-integrable if the action of ˇn− onL⊗(−ψ) is locally
nilpotent). Namely, a (U ℏ(ˇn−),ψ)-integrableU ℏ-moduleLgoes to theZ(U ℏ)-module
HomUℏ(W−
ℏ,L). Conversely, aZ(U ℏ)-moduleRgoes toW −
ℏ ⊗Z(Uℏ)R. In particular,
W−
ℏ goes to the free moduleZ(U ℏ).
For anℏ-Harish-Chandra bimoduleMwe will construct a canonical isomorphism
κℏ(M)≃Hom Uℏ(W−
ℏ,M⊗ Uℏ W−
ℏ ). In effect,L7→M⊗ UℏLis a right-exact endofunctor
of the category of (Uℏ(ˇn−),ψ)-integrableU ℏ-modules. Under Kostant’s equivalence, this
endofunctor goes to the convolution with theZ(U ℏ)-bimoduleXwhich corresponds by
Kostant to our endofunctor applied toW −
ℏ . In other words,X=Hom Uℏ(W−
ℏ,M⊗ Uℏ
W−
ℏ ). We have a tautological isomorphismX⊗ Z(Uℏ) W−
ℏ
∼−→M⊗Uℏ W−
ℏ . This yields the
desired isomorphismX ∼−→κℏ(M). In particular, for a freeℏ-Harish-Chandra bimodule
M=Fr(V), we obtainϕ(V)⊗ Z(Uℏ) W−
ℏ
∼−→V⊗ k W−
ℏ .
Now let us compute (M ℏ(−ρ)⊗V⊗W −
ℏ )⊗ Uℏ k[ℏ] = (M ℏ(−ρ)⊗(V⊗W −
ℏ ))⊗ Uℏ
k[ℏ] ∼−→(Mℏ(−ρ)⊗(W−
ℏ⊗Z(Uℏ)ϕ(V)))⊗ Uℏ k[ℏ] ∼−→(π,Id,Id)∗ϕ(V). The last isomorphism
arises from (M ℏ(−ρ)⊗W −
ℏ )⊗ Uℏ k[ℏ] ∼−→Uℏ(ˇt) =O( ˇt∗), sinceM ℏ(−ρ) =U ℏ⊗Uℏ(ˇb)
k[ℏ][ˇt](−ρ), andW −
ℏ =U ℏ⊗Uℏ(ˇn−)ψ.
