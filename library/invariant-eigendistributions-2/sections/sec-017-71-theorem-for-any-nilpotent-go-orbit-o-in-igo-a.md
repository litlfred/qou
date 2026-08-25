---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-017-71-theorem-for-any-nilpotent-go-orbit-o-in-igo-a
section_title: "Theorem. For any nilpotent Go-orbit O in igo∗ and any 2n-cycle Γ∈H2n(S( ¯O)) over ¯O,"
section_number: 7.1
pages: 13-20
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 25 sections: Introduction; Construction of Weyl group represe"
---
1
(2πi)n
∫
pλΓ
exλ−σλ =cΓ(λ) 1
(2πi)d
∫
O
exO −σO +o(|λ|e) (11)
Explanation and remarks . d = d(O)=d i mCO,e = e(O)=d i mCBν(ν ∈O ); xO is x considered as a
function onO; σO is the canonical 2-form onO:
σO(x·ν,y ·ν)= ⟨ν,[x,y]⟩.
The equation (11) is understood as an identityof distributions ongo, as usual. It will be abbreviated to
θΓ(λ)= cΓ(λ)θO +o(|λ|e). (12)
with
θΓ(λ)= 1
(2πi)n
∫
pλΓ
exλ−σλ ,
θO = 1
(2πi)d
∫
O
exO −σO .
The equation (11) can also be written as an asymptotic relation asx→ 0i ngo in the sense of Barbasch
and Vogan [1980]:
θΓ(λ)∼cΓ(λ)θO as x→ 0i ngo. (13)
REPRESENTATIONS OF WEYL GROUPS 14
This means thatcΓ(λ)θO is the leading term in the asymptotic expansion ofθΓ(λ)a tx =0d e s c r i b e di n
Theorem 1.3 of [Barbasch-Vogan 1980].
Proof of the theorem.F i xt h eGo-orbit O on N∩ igo∗ and Γ∈H2n(S( ¯O)). Forf ∈C∞
c (g), set
ϕ(ξ)=
∫
g
eξ(x)f(x)dx.
The theorem says that for all suchf
(−1)n
(2πi)nn!
∫
pλΓ
ϕσλn =cΓ(λ) (−1)d
(2πi)dd!
∫
O
ϕσOd +o(|λ|e).
To determine the asymptotic behaviour of the integral on the left we need some general remarks on
symplectic structure. LetQ be an orbit of the complex groupG on the nilpotent coneN ing∗. As before,
put
B∗(Q)= {(b,ν)|ν ∈Q}
Then there are injections
B∗(Q) ⊂→B×Q (15)
B∗(Q) ⊂→ Ωλ (16)
the ﬁrst map being the natural inclusion, the second one the restriction of the bijection
pλ :B∗ → Ωλ,u ·(s1,ν)→u·(λ+ν)
(u ∈ U,ν ∈ s1⊥). In view (15) and (16) we can restrict toB∗(Q)t h e2 - f o r mτλ +σQ on B×Q and the
2-form σλ on Ωλ.
7.2 Lemma. The 2-forms τλ +σQ and σλ agree on B∗(Q).
Proof of the lemma . Because of U-invariance it suﬃces to show that the forms agree at a point (s1,ν)
with ν ⊂s1⊥ ∩Q.L e t
u(t)·(s1,v(t)·ν) (17)
be a smooth curve onB∗(Q)w i t hu(t) ∈ U, v(t) ∈ G, v(t)·ν ∈ s1⊥,u (0) = 1,v (0) = 1. Its tangent
vector att =0i s
(u′·s1,(u′+v′)·ν) (18)
REPRESENTATIONS OF WEYL GROUPS 15
u′,v ′∈ g being the tangent vectors ofu(t)a n dv(t)a tt =0 . The 2-formτλ +σQ assigns to two such
tangent vectors at (s1,ν)t h ev a l u e
⟨λ,[u′,u ′′]⟩+⟨ν,[u′,u ′′]⟩+⟨ν,[u′,v ′′]⟩+⟨ν,[v′,u ′′]⟩+⟨ν,[v′,v ′′]⟩. (19)
The curve on Ωλ corresponding to (17) under the injection (16) is
u(t)·λ+u(t)v(t)·ν
and its tangent vector atλ+ν, corresponding to the vector (18) at (s1,ν), is
u′·(λ+ν)+ v′·ν.
The 2-formσλ assigns to two such tangent vectors atλ+ν the value
⟨λ,[u′,u ′′]⟩+⟨ν,[u′,u ′′]⟩+⟨ν,[u′,v ′′]⟩+⟨ν,[v′,u ′′]⟩+⟨λ+ν,[v′,v ′′]⟩. (20)
The last term of (20) = 0, asλ+s1⊥ ⊂ Ωλ is an isotropic (in fact Lagrangian) submanifold of Ωλ, which
is clear. The same is true of the last term of (19), but this is less clear: it is known that, for anyb,b ⊥∩Q
is a co-isotropic subvarietyofQ [Joseph 1984, Lemmas 7.5 and 9.6(i)] of dimension = 1/2=d i mQ (as
follows from [Spaltenstein 1977] and [Steinberg 1976, section 4]), hence in fact Lagrangian. Thus (19)
agrees with (20), proving the lemma.
Remark. The fact thatb
⊥ ∩Q is Lagrangian onQ is mentioned in [Ginsburg 1986, Proposition 4.3]. The
proof indicated there uses generalfacts from symplectic geometry. [NB(2003). These facts (moment maps
preserving Poisson brackets) implyalso that the formσ
Q is the canonical 2-form onB∗ over the open
orbit Q,w h e r eB∗ →{N is regular.]
We return to the proof of the theorem. Applythe above lemma to theG-orbit Q containing theGo-orbit
O. The ﬁbration
Bν⊂→B∗(Q)→Q (21)
restricts to
Bν⊂→S(O)→O . (22)
ForΓitsuﬃcestotakeacomponentof S(O). Asexplainedfor Z(O)inconnectionwith(4.2),acomponent
of S(O) is a dense part of anSw , denotedSw(O). The ﬁbration (22) restricts to a ﬁbration
Bνw
⊂→Sw(O)→O . (23)
AccordingtoSteinberg[1976]theﬁbre Bνw =Sw(O)∩Bν overν ∈O in(23)isasingleorbitofcomponents
ofBν under the component groupAo(ν) of the stabilizer ofν in Go. These components all have the same
REPRESENTATIONS OF WEYL GROUPS 16
dimension e = e(O)=d i mCBν, bya result of Spaltenstein [1977]. The fundamental class of such a
component inH2e(B) is independent ofν in O,a sO is connected. Note, incidentally, that
d+e =n
because of the ﬁbration (14). Now calculate:
(−1)n
(2πi)nn!
∫
pλSw (O)
ϕσλn = (−1)n
(2πi)nn!
∫
Sw (O)
(ϕ◦pλ)(τλ +σO)n
= (−1)n
(2πi)nd!e!
∫
O
{ ∫
Bν w
ϕ(pλ(b,ν))τλe(db)
}
σOd(dν)+ o(|λ|e) (24)
where we used the ﬁbration (22) and Lemma 7.2 to write the integral overSw(O)a sa ni n t e g r a lo v e rt h e
ﬁbre Bνw followed byan integral over the baseO.
In the integral (24) write (b,ν)= u·(s1,ν 1)w i t hu∈U andν1 ∈s1⊥. Then the integrand becomes
ϕ(pλ(b,ν)) =ϕ(u·(λ+ν1))
=ϕ(u·ν1)+ o(|λ|)
=ϕ(ν)+ o(|λ|)
Thus
(24) = (−1)n
(2πi)nd!e!
∫
O
ϕ(ν)
{ ∫
Bν w
τλe(db)
}
σOd(dν)+ o(|λ|e)
= (−1)d
(2πi)dd!
∫
O
ϕ(ν)⟨c,eλ⟩σOd(dν)+ o(|λ|e)
= (−1)d
(2πi)dd!c(λ)
∫
O
ϕ(ν)σOd(dν)++ o(|λ|e) (25)
where c = cνw ∈He(h∗) is the harmonic polynomial onh∗ representing the fundamental class ofBνw in
H∗(B) under Borel’s isomorphism (6). As in (7),⟨c,f⟩is the natural pairing of polynomials onh∗ and
formal power series onh ,s ot h a t⟨c,eλ⟩=c(λ). This proves the theorem.
8. Harmonic polynomials
We studyin some more detail the harmonic poly nomialscΓ ∈H e(h∗) associated to a 2n-cycle Γ ∈
H2n(S( ¯O)) over ¯O bythe relation
θΓ(λ)= cΓ(λ)θO +o(|λ|e). (1)
These polynomials, or variants thereof, have a history. WhenθΓ represents a coherent familyof virtual
characters of Harish-Chandra modules, thencΓ is the character polynomial studied byKing [1979] using
results of Joseph [1980], except that in King’s deﬁnition the polynomials are not canonically normalized:
there theyare deﬁned up to a constant factor which depends on an arbitraryregular element in the
REPRESENTATIONS OF WEYL GROUPS 17
Cartan ho. King shows that these polynomials are essentially the same as the polynomials introduced by
Jantzen [1977], Joseph [1980], and Vogan [1978]. The approachtaken here is logicallyindependent of (but
stronglyinspired by ) these developments; it opens up some (from the previous point of view) surprising
perspectives, among them the relation of thec
Γ to the homologyof the ﬂag variety , and a formula for the
cΓ in terms of Euler numbers.
Write
Γ=
∑
y∈W/Wo
myy·S 1. (2)
Then
θΓ(λ)= 1
π
∑
y∈W
myey−1λ. (3)
Expanding the exponential gives
θΓ(λ)=
∞∑
k=0
1
k!
1
π
∑
y∈W
myy−1λk. (4)
Comparing (1) and (4) one ﬁnds that
∑
y∈W
myy−1λk =0 f o rk<e (5)
and
∑
y∈W
myy−1λe =cΓ(λ)pO (6)
where
pO =e!πθO. (7)
From equation (7) it appears thatpO is aGo-invariant distribution ongo (the Wo-invariant polynomial
π on ho extends to aGo-invariant polynomial ongo), but from (6) one sees that onho
pO is aWo-invariant polynomial onh, homogeneous of degreee =e(O). (8)
(In this interpretation we used implicitlyHarish-Chandra’s regularitytheorem, which guarantees thatθO
is a locallyintegrable function ongo.)
The relation (6) is an amazingly powerful tool for analyzing the polynomialscΓ. First of all we get
from (6) a fromula for thecΓ for arbitraryΓ ∈H2n(S( ¯O)):
If Γ =
∑
y∈W/Wo
myy·S 1 ,t h e ncΓ = 1
pO(x)
∑
y∈W
myy·xe (9)
REPRESENTATIONS OF WEYL GROUPS 18
For anyx ∈ h with pO(x) ⁄=0 . In particular, for Γ =Sw (any w ∈ W/Wo)w et a k ef o rO = O(w)t h e
unique nilpotentGo-orbit inigo∗ which intersectss1⊥ ∩igo∗ densely(which amounts to O intersecting
bo
⊥ ∩w−1bo
⊥ denselyif we think of O as aGo-orbit ongo∗ and representw ∈ W/Wo as (1,w)); then
Sw ∈H2n(S( ¯O(w))) and according to Corollary5.2
Sw =
∑
y∈W/Wo
(−1)l(w)−l(y)Euy(Sw)y·S 1. (10))
Γ= Sw ∈ H2n(S( ¯O)) corresponds to the fundamental cycle [Bνw] ∈ H2e(B) of the componentBν
w of Bν
under the map
H2n(S( ¯O))→H2n(S(O))≈H2e(Bν)Ao (ν) →H2e(B).
From the deﬁnition ofcΓ the correspondingcΓ = cw is explicitlygiven bythe formula
cw(λ)=
∫
Bν w
eωλ. (11)
On the other hand, the formula (9) says that
cw = 1
pO(x)
∑
y∈W
(−1)l(w)−l(y)Euy(Sw)y·xe (12)
for anyx∈h with pO(x)⁄= 0. Comparing (11) and (12) leads to the curious integral formula
∫
Bν w
eωλ = 1
pO(x)
∑
y∈W
(−1)l(w)−l(y)Euy(Sw)⟨λ,y ·x⟩e (12)
for anyx∈h with pO(x)⁄=0
The polynomials cΓ have some positiviyand integralityproperties which should be mentioned.
When λ∈h∗ is thes1-heighest weight of a ﬁnite-dimensional representationVλ of G, the integral on the
left of (13) can be thought of as follows.
Embed the ﬂag-manifoldB of G into the projective spacePVλ of Vλ by
iλ :B→ PVλ,b → [b-highest weight vector]. (14)
Then
ωλ =iλ∗ωPV λ
where ωPV λ is the K¨ahler 2-form of the Fubini-Studymetric onPVλ. Thus for a complex subvarietyV of
B,
∫
V
eωλ =v o lλ(V)= 1
(dimV)!degλ(V) (15)
REPRESENTATIONS OF WEYL GROUPS 19
where volλ(V)i st h ev o l u m eo fV with respect to the metric onB coming from the embedding (14) and
degλ(V) is the degree of the projective varietyiλ(V)i n PVλ. (See [Griﬃth-Harris 1978], p. 171, for
example.) The formula (11) says that forλ regular, s1-positive, integral
cw(λ)=v o lλ(Bνw)= 1
e!degλ(Bνw). (16)
Thus
e!cw(λ) is positive integral for regular,s1-positive, integralλ. (17)
We want a more explicit formula for theWo-invariant polynomial pO. For that purpose we make a
particular choice for Γ∈H2n(S( ¯O)) as follows.
We know that the W-quotient H2n(S(O)) of H2n(S( ¯O)) is ≈ H2e(Bν)Ao (ν) and contains the
A(ν)-invariants He(Bν)A(ν) as an irreducible subrepresentation (isomorphic with the spaceHe(h∗)o f
W-harmonic polynomials onh∗). Let
χO = character ofWo on H2e(Boν)Ao (ν).
(Note that we passed from the irreducible representationH2eo(Bν)A(ν) of W = Wo × Wo to the cor-
responding irreducible representationH2e(Boν)Ao(ν) of Wo.) It follows from these remarks that we can
choose Γ = ΓO in H2n(S( ¯O)) so that
my = eo
|W|χO(y) (18)
where
eo =d e gχO =d i mBoν
and we identifyW/Wo = Wo via (y1,y 2) → y1y2−1 to think ofχO as a function onW/Wo (or as a
Wo-bi-invariant function onW). Explicitly:
χO(y)= χO(y1y2−1)
when we writey ∈W =Wo ×Wo as y =(y1,y 2). With this choice ofmy the element
∑
y∈W
myy−1 = eo
|W|
∑
y∈W
χO(y)y−1 (19)
of the group ring ofW operates as the projection on theWo-invariants of typeχO ⊗χO, which have
dimension = 1 in the irreducibleW-module of this type.
W r i t eo u tt h ee q u a t i o n( 6 )w i t hmy given by(18):
cO(λ)pO(x)= eo
|W|
∑
y∈W
χO(y)⟨λ,y ·x⟩e. (20)
REPRESENTATIONS OF WEYL GROUPS 20
If one identiﬁesh and h∗ bya W-invariant, C-bilinear, symmetric, inner product, then the right side of
(20) is symmetric inλ and x, since χO(y)= χO(y−1) as function ofW. As a consequence,
cO =c o n s t.pO (21)
for some constant depending onlyonO.I np a r t i c u l a r ,pO belongs toHe(h∗), and consequently:
pO = eo
cO (λ)|W |
∑
y∈W
χO(y)y−1 ·λe (22)
is the (up to a constant factor) uniqueWo-invariant, harmonic polynomial onho which transforms under
W by χO ⊗χO. In (22) we can take anyλ for whichcO(λ) ⁄= 0. For the same values (18) ofmw the
relations (5) and (6) imply:
The W-representation of typeχO ⊗χO occurs with multiplicityone in degreee =e(O)i n C[h∗]
and not at all in lower degree.
This follows from (5), (6), and (22), since theλk span the homogeneous polynomials of degreek on h∗
and each irreducible subspace of typeC[h∗] contains exactlyoneWo-invariant (up to scalar multiples).
On the other hand,C[h∗]≈ C[ho
∗]⊗ C[ho
∗]a sW =Wo ×Wo module, so we can pass fromW to Wo to
get the following result of Borho-Macpherson [1981]:
