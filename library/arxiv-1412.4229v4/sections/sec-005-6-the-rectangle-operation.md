---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-005-6-the-rectangle-operation
section_title: "The Rectangle Operation"
section_number: 6
pages: 32-37
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — Let A → B be a homomorphism of commutative rings."
---
In this section we continue with the material of Section 5, but with slightly
diﬀerent notation. Recall thatPDGR is the category of central pairs of DG rings,
and PDGR≤0 is the full subcategory of nonpositive central pairs. See Deﬁnitions
3.6 and 3.7.
The main result here is Theorem 6.11. Throughout this section we work in the
following setup.
Setup 6.1. We are given:
(1) A central morphismw/v :B′/A′→B/A in PDGR≤0 (namely a morphism
in PDGR≤0
⃗ce , see Deﬁnition 3.7(3)).
(2) K-ﬂatresolutionss/r : ˜B/ ˜A→B/Aands′/r′: ˜B′/ ˜A′→B′/A′in PDGR≤0,
and morphisms
˜w0/˜v0, ˜w1/˜v1 : ˜B′/ ˜A′→˜B/ ˜A
in PDGR≤0 abovew/v. See Deﬁnitions 3.8, 3.9 and 3.15.
(3) An object (Ml,M r) in D(B)×D(Bop), an object (M′l,M′r) in D(B′)×
D(B′op), and a morphism
(θl,θr) : (Ml,M r)→(M′l,M′r)
in D(B′)×D(B′op).
The DG ring input is depicted in the following commutative diagram in the
category PDGR≤0, fori = 0, 1.
˜B′/ ˜A′˜wi/˜vi //
s′/r′

˜B/ ˜A
s/r

B′/A′w/v //B/A
The four central homomorphisms, belonging to the four central pairs above, are
u :A→B, u′:A′→B′, ˜u : ˜A→˜B and ˜u′: ˜A′→˜B′.
From here until Lemma 6.7 (inclusive), we also assume the next condition.
Condition 6.2.
(i) The homomorphism ˜u′: ˜A′→˜B′is noncommutative semi-free (Deﬁnition
3.11(2)).
THE SQUARING OPERATION 33
(ii) The homomorphisms ˜v0, ˜v1 : ˜A′→˜A are equal.
In view of item (ii) in Condition 6.2, we may write ˜v := ˜v0 = ˜v1; this is a
homomorphism ˜v : ˜A′→˜A in DGR≤0
sc , lying abovev :A′→A. The DG ring input
of Setup 6.1 and Condition 6.2 can be summarized as the following commutative
diagrams in the categoryDGR≤0/ce ˜A′, fori = 0, 1:
˜B′
w◦s′
˜A′ //
˜u′
>>
˜u◦˜v   
B
˜B
s
??
˜B′
w◦s′

˜wi

˜A′
˜u′
>>
˜u◦˜v   
B
˜B
s
??
Recall the cylinder DG ring from Deﬁnition 1.23.
Lemma 6.3. Under Condition 6.2, there is a homomorphism
˜wcyl : ˜B′→Cyl( ˜B)
in DGR/ce ˜A′, such that diagram(6.4) is commutative fori = 0, 1.
(6.4) ˜B′˜wcyl //
s′

˜wi

Cyl( ˜B)
ηi //
Cyl(s)

˜B
s

B′ϵ◦w // Cyl(B)
ηi //B
Proof. Weknowthat ˜u′: ˜A′→˜B′isnoncommutativesemi-free, and sisasurjective
quasi-isomorphism. So Theorem 4.3 applies. We obtain an ˜A′-linear DG ring
homotopy γ: ˜w0⇒˜w1 such thats◦γ= 0. By Proposition 4.5 we deduce the
existence of a DG ring homomorphism ˜wcyl : ˜B′→Cyl( ˜B). The formula, for
b∈˜B′, is
˜wcyl(b) =
)
˜w0(b) ξ·γ(b)
0 ˜ w1(b)
[
.
This shows the commutativity of the half-moon in the diagram. Next, because the
elementξcommutes with the homomorphisms, and becauses◦γ= 0, we have
Cyl(s)( ˜wcyl(b)) =
)
s( ˜w0(b)) s(ξ·γ(b))
0 s( ˜w1(b))
[
=
[w(s′(b)) 0
0 w(s′(b))
]
.
We deduce the commutativity of the ﬁrst square in the diagram. The second square
is trivially commutative. □
There are central homomorphismsϵ◦u :A→Cyl(B) and ϵ◦˜u : ˜A→Cyl( ˜B),
and thus two more central pairsCyl(B)/A and Cyl( ˜B)/ ˜A. These central pairs ﬁt
into a commutative diagram
34 AMNON YEKUTIELI
(6.5) ˜B′/ ˜A′ ˜wcyl/˜v //
s′/r′

˜wi/˜v

Cyl( ˜B)/ ˜A
ηi/ id //
Cyl(s)/r

˜B/ ˜A
s/r

B′/A′(ϵ◦w)/v //
w/v
BBCyl(B)/A
ηi/ id //B/A
in the categoryPDGR, fori = 0, 1. Moreover, the morphisms between the pairs in
the lower row are central, namely they are inPDGR⃗ce. The pairs in the upper row
are K-ﬂat, and the vertical morphisms are quasi-isomorphisms.
Consider the DG moduleCyl(Ml)∈M(Cyl(B)). Deﬁne homomorphisms
η∨
0 :Ml→Cyl(Ml), η∨
0 (m) :=
[m 0
0 0
]
and
η∨
1 :Ml→Cyl(Ml), η∨
1 (m) :=
[0 0
0 m
]
.
Thenη∨
i : Forηi(Ml)→Cyl(Ml) is a homomorphism inM(Cyl(B)). Next, deﬁne a
homomorphism
ϵ∨: Cyl(Ml)→Ml, ϵ∨(
[m0 n
0 m1
]
) :=m0 +m1.
Then ϵ∨: Forϵ(Cyl(Ml))→Ml is a homomorphism inM(B). And ϵ∨◦η∨
i = id.
All this can be done forMr too.
Consider the next commutative diagram, fori = 0, 1, in the categoryD(B′)×
D(B′op).
(6.6) (M′l,M′r)
(
Cyl(Ml), Cyl(Mr)
{(θl◦ϵ∨,θr◦ϵ∨)oo (Ml,M r)
(η∨
i ,η∨
i )oo
(θl,θr)
cc
Lemma 6.7. Under Condition 6.2, there is equality
(6.8) Rect ˜w0/˜v
w/v (θl,θr) = Rect ˜w1/˜v
w/v (θl,θr)
of morphisms
Rect
˜B/ ˜A
B/A(Ml,M r)→Rect
˜B′/ ˜A′
B′/A′(M′l,M′r)
in D(B′ce).
Proof. Step 1. Here we assume thatB′/A′=B/A, ˜B′/ ˜A′= ˜B/ ˜A, the morphisms
w/v, ˜w0/˜v and ˜w1/˜v are the identity automorphisms, and there is equalitys′/r′=
s/r. Also we assume that(M′l,M′r) = (Ml,M r), and the morphism(θl,θr) is the
identity automorphism. We may also assume that ˜wcyl = ϵ◦˜w, but that is not
important. By functoriality (Proposition 5.17), we have
(6.9) Rect ˜wcyl/˜v
ϵ◦w/v (θl◦ϵ∨,θr◦ϵ∨)◦Rectηi/ id
ηi/ id(η∨
i ,η∨
i ) = Rect ˜wi/˜v
w/v (θl,θr),
THE SQUARING OPERATION 35
in D(Bce), fori = 0, 1. Compare to diagrams (6.5) and (6.6). By Lemma 5.14, all
three morphisms above are isomorphisms. Some caution is needed here: the mor-
phism Rectηi/ id
ηi/ id(η∨
i ,η∨
i ) is actually in the categoryD(Cyl(B)ce), and the forgetful
functor
Forϵce : D(Cyl(B)ce)→D(Bce)
has been hidden. But but we know (see Proposition 1.24) that the DG ring homo-
morphismϵ:B→Cyl(B)induces an isomorphismϵce :Bce→Cyl(B)ce. Therefore
the functor Forϵce is an equivalence.
Since ˜w1 = ˜w0 here, formula (6.9) fori = 0, 1 leads us to conclude that
(6.10) Rectη1/ id
η1/ id(η∨
1,η∨
1 ) = Rectη0/ id
η0/ id(η∨
0,η∨
0 ),
as isomorphisms
Rect
˜B/ ˜A
B/A(Ml,M r)→RectCyl( ˜B)/ ˜A
Cyl(B)/A
(
Cyl(Ml), Cyl(Mr)
{
in D(Cyl(B)ce).
Step 2. Now there are no special assumptions. We choose a homomorphism˜wcyl
as in Lemma 6.3. By functoriality, we again have the equalities (6.9), fori = 0, 1.
Formula (6.10) from part (1) applies here, because it does not depend onB′/A′.
We deduce that (6.8) holds. □
Here is the key technical result of the paper (the noncommutative version).
Theorem 6.11 (Homotopy Invariance). In the situation of Setup 6.1, there is
equality
Rect ˜w0/˜v0
w/v (θl,θr) = Rect ˜w1/˜v1
w/v (θl,θr)
of morphisms
Rect
˜B/ ˜A
B/A(Ml,M r)→Rect
˜B′/ ˜A′
B′/A′(M′l,M′r)
in D(B′ce).
Proof. Choose the following resolutions in PDGR≤0: a strict K-ﬂat resolution
s♦/id : ˜B♦/A →B/A, a strict noncommutative semi-free resolution s♥/id :
˜B♥/ ˜A→˜B/ ˜A, and a strict noncommutative semi-free resolutions′♦/id : ˜B′♦/ ˜A′
→˜B′/ ˜A′. These exist by Theorem 3.21.
There is a homomorphisms†: ˜B♥→˜B♦in DGR≤0/ce ˜A such thats♦◦s†=
s◦s♥. For i = 0, 1 there is a homomorphism ˜w♦
i : ˜B′♦→˜B♥in DGR≤0/ce ˜A′,
such thats♥◦˜w♦
i = ˜wi◦s′♦. These homomorphisms exist by Theorem 3.22.
The resolutions and the homomorphisms between them, from the two paragraphs
above, ﬁt into the following commutative diagram inPDGR≤0, fori = 0, 1. The
central pairs ˜B′♦/ ˜A′and ˜B′/ ˜A′are K-ﬂat resolutions ofB′/A′, and the central
pairs ˜B♥/ ˜A, ˜B♦/A and ˜B/ ˜A are K-ﬂat resolutions ofB/A.
(6.12) ˜B♥/ ˜A
s♥/id

s†/r
$$
˜B′♦/ ˜A′
˜w♦
i /˜vi
00
s′♦/id //
(s′◦s′♦)/r′
%%
˜B′/ ˜A′ ˜wi/˜vi //
s′/r′

˜B/ ˜A
s/r

˜B♦/A
s♦/id
zz
B′/A′ w/v //B/A
36 AMNON YEKUTIELI
Let us introduce the temporary abbreviations
R( ˜B/ ˜A) := Rect
˜B/ ˜A
B/A(Ml,M r), R( ˜B′/ ˜A′) := Rect
˜B′/ ˜A′
B′/A′(M′l,M′r),
R( ˜wi/˜vi) := Rect ˜wi/˜vi
w/v (θl,θr), R(s†/r) := Rects†/r
id/id(id, id),
etc. Applying functoriality (Proposition 5.17) to the commutative diagram (6.12),
we obtain a commutative diagram
(6.13)
R( ˜B♥/ ˜A)R( ˜w♦
i /˜vi)
xx
R( ˜B′♦/ ˜A′) R( ˜B′/ ˜A′)
R(s′♦/id)oo R( ˜B/ ˜A)
R(s♥/id)
OO
R( ˜wi/˜vi)oo R( ˜B♦/A)
R(s†/r)
ff
in D(B′ce), fori = 0, 1. All the morphisms whose names contain the letter “s” are
isomorphisms.
Note thatr◦˜vi =v◦r′. We get a commutative diagram
(6.14) R( ˜B♥/ ˜A)R( ˜w♦
i /˜vi)
{{
R( ˜B′♦/ ˜A′) R( ˜B♦/A)
R(s†/r)
ff
R((s†◦˜w♦
i )/(v◦r′))oo
in D(B′ce), for i = 0, 1. Because Condition 6.2 is satisﬁed for the morphisms of
resolutions
(s†◦˜w♦
i )/(v◦r′) : ˜B′♦/ ˜A′→˜B♦/A,
Lemma 6.7 tells us that
R((s†◦˜w♦
0 )/(v◦r′)) = R((s†◦˜w♦
1 )/(v◦r′)).
Since R(y†/r) is an isomorphism, we conclude that
R( ˜w♦
0/˜v0) = R( ˜w♦
1/˜v1).
Going back to diagram (6.13), and using the fact that bothR(s♥/id) and R(s′♦/id)
are isomorphisms, we see that
R( ˜w0/˜v0) = R( ˜w1/˜v1).
□
Theorem 6.15(Existence of Rectangles). LetA be a commutative DG ring, and
let A→B be a central homomorphism of nonpositive DG rings. Given a pair
(Ml,M r)∈D(B)×D(Bop),
there is a DG module
RectB/A(Ml,M r)∈D(Bce),
unique up to a unique isomorphism, together with an isomorphism
rect
˜B/ ˜A : RectB/A(Ml,M r)
≃
− →Rect
˜B/ ˜A
B/A(Ml,M r)
for every K-ﬂat resolution˜B/ ˜A of B/A in PDGR≤0, such that the following condi-
tion holds.
