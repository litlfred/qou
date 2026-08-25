---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-022-101-theorem-leto-be-a-nilpotent-go-orbit-in-igo
section_title: "Theorem. LetO be a nilpotent Go-orbit in igo∗. Then"
section_number: 10.1
pages: 26-28
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 25 sections: Introduction; Construction of Weyl group represe"
---
µO =e!|Wo| lim
λ→ 0
∂O,λµλ (7)
and
ˆµO(x)=c o n s t.(λ,O)
π
∑
y∈W
χO(y)⟨λ,y ·x⟩e (8)
=c o n s t.(O)
π
∑
y∈Wo
χσ(y)⟨x,y ·x⟩eo (9)
The formula (7) has some history. ForO ={0},χ O = sign representation ofWo,p O =c o n s t .π,a n d( 7 )
becomes Harish-Chandra’s Limit Formula
µO = const. lim
λ→ 0
∂π,λµλ(x).
For special orbits Formula (7) was proved byBarbasch-Vogan [1982, 1983] bycase bycase computations
and conjectured to hold in general. This conjecture was then proved byHotta-Kashiwara [1984] (using
the theoryof holonomic sy stems).
11. A conjecture of Joseph
The asymptotic relation
θΓ(λ)= cΓ(λ)θO +o(|λ|e)( 1 )
maybe used to prove a conjecture of Joseph [1984, Conjecture 9.8]. The conjecture maybe explained as
follows. Let
T ={(b,ν)|b∈Bo,ν ∈b⊥ ∩bo
⊥}. (2)
This is the conormal varietyof the action of the ﬁxed Borel subgroupBo of Go on the ﬂag manifoldBo
of Go. (The complexiﬁcation ofGo does not enter into the picture here.)T is also the inverse image
Bo
∗(bo
⊥)o f bo
⊥ under the Springer mapBo
∗ →N o. Its dimension is no =d i mCBo
∗ and our general
construction gives a representation ofWo onH∗(T). In top degree,H2no(T) has as basis the fundamental
cycles of the components ofT. These components are the closures of the conormal bundlesTw of the
Bo-orbits Bo ·w−1bo:
Tw ={Bo ·(w−1bo,ν)|ν ∈bo
⊥ ∩w−1bo). (3)
For eachw ∈Wo there is a uniqueGo-orbitO =O(w)o nNo which intersectsbo
⊥∩w−1bo densely; and for
eachO the components ofO∩ bo
⊥ are the closures inO∩ bo
⊥ of the dense parts of theBo ·(bo
⊥∩w−1bo)
cut out byO when O(w)= O.F o r a g i v e nO these components V(w)o f O∩ bo
⊥ all have the same
dimension = 1
2dimO. (For these results see Steinberg [1976] and Joseph [1984].) To each such subvariety
V(w)o fNo Joseph associates a polynomialpV(w) on h∗
o, homogeneous of degreeno− 1
2dimO.T h i sd e g r e e
=eo =d i mBoν for ν ∈O . Joseph’s conjecture says that if one writes
Zw =
∑
y∈Wo
A(w,(y,1))(y,1)·Z 1 (4)
REPRESENTATIONS OF WEYL GROUPS 27
in the homologyH2n(Z) of the conormal varietyZ , then
pV(w) =c o n s t .
∑
y∈Wo
A(w,(y,1))y·ρoeo, (5)
and the exponent eo =d i mBoν in this relation is the least for which the right side is non-zero.ρo
denotes half the sum of the roots ofho in bo
⊥, which must here be thought of as an element ofho by
meansof aWo-invariant bilinear form (Joseph identiﬁesho and ho
∗); in (5) we take (y,1) as element of
W = Wo ×Wo and use theW-action on the homologyofZ deﬁned earlier (which bysection 12 is also
the action constructed byKazhdan-Lusztig [1980], to which Joseph refers. Joseph writes this action of
Wo ×Wo as aWo–Wo bimodule.)
To prove the conjecture we consider the projectionB∗ = Bo
∗ ×B o
∗ →B o through the second
factor. It restricts to a ﬁbration
T ⊂→Z →Bo (6)
with T as in (2) as ﬁbre overbo. The componentsZw of Z meet the ﬁbreT in the componentsTw of T.
For anyν ∈bo
⊥ there is a diagram
Bo
ν ⊂→T→ bo
⊥
∩∩∩
Bo
ν ⊂→Z→N
(7)
F o rag i v e nGo-orbitO onNo andν ∈O∩ bo
⊥,Zw meets the ﬁbreBν ofZ→N in a singleAo(ν)-orbit of
components;Tw meets the ﬁbreBoν ofT→ bo
⊥ in a union of components which lie in a singleAo(ν)-orbit
anddetermineanelementof H2eo(boν)Ao(ν). (ForthesefactsseeSpaltenstein[1977].) Accordingtoaresult
ofHotta[1984],themapwhichsends pV(w) tothis elementof H2eo(Boν)Ao(ν) extendstoa Wo-isomorphism
of the space spanned bythepV(w) , O(w)= O,o n t oH2eo(Boν)Ao(ν).
On the other hand, the inclusionBoν
⊂→Bo gives a Wo-injection H2eo(Boν)Ao(ν) → H2eo(Bo) ≈
H(ho), as we know from sections 3 and 7. Hence the element ofH2eo(Boν)Ao (ν) mentioned above gives
rise to another (harmonic) polynomial onho
∗, homogeneous of degreeeo. Because of Lemma 8.1, this
polynomial must bepV(w) up to a (non-zero) factor depending onlyonO.
To make use of the relation (1) note that the ﬁbration (6) leads to aWo ×{ 1}-isomorphism
H2n(Z) → H2no(T) which sends the fundamental cycle ofZw to the fundamental cycle ofTw.F r o m
Theorem 5.1 we know that the relation
Zw =
∑
y∈Wo
A(w,(y,1))(y,1)·Z 1 (4)
implies that
θSw = (−1)n
π
∑
y∈Wo
A(w,(y,1))e(y−1,1)λ. (8)
Of course, we also know that
A(w,y)=( −1)l(w)−l(y)Euy(Zw), (9)
REPRESENTATIONS OF WEYL GROUPS 28
but this will not even be needed. Rather, we use the formula (9.8) to write
cw(λ)= kO
∑
y∈Wo
A(w,(y,1))⟨λ1,y ·λ2⟩eo. (10)
On the other hand, the polynomialcw represents the fundamental cycle of the componentBν
w of Bν in
H2e(B)≈H (h). SinceBν =Boν ×Boν that component must factorBν
w =Cw ×C ′
w as a product of a pair
of components ofBoν depending onw. These two components correspond to two harmonic polynomials
pw , p′
w on ho
∗ and the factorizationBν∗w = Cw ×C ′
w means that
cw(λ)= pw(λ1)p′
w(λ2) (11)
if λ =( λ1,λ 2)i nh∗ = ho
∗ × ho
∗. From the discussion around diagram (7) it is clear that
pw =c o n s t .pV(w).
To prove Joseph’s conjecture we maytherefore replacepV(w) by pw in (5). From (10) and (11) one ﬁnds
pw(λ1)= kO
p′w(λ2)
∑
y∈Wo
A(w,(y,1))⟨λ1,y ·λ2⟩eo
provided p′
w(λ2) ⁄= 0, which know to be the case for regularλ2. Choosing λ2 = ρo we get the formula
conjectured byJoseph:
pV(w) =c o n s t .
∑
y∈Wo
A(w,(y,1))y·ρoeo.
For the record we point out once more that we have actuallyproved the more precise formula
pV(w) =c o n s t .
∑
y∈W/Wo
(−1)l(w)−l(y)Euy(Zw)y·ρoeo. (12)
for a constant depending onlyonO.
