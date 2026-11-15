---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I"
section_id: sec-014-42-subfactors-give-planar-algebras
section_title: "Subfactors give planar algebras"
section_number: 4.2
pages: 92-115
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
toc_source: inferred
doc_brief: "Planar Algebras, I — We introduce a notion of planar algebra, the simplest example of which is a vector space of tensors, closed under planar contractions."
---
We keep the notation of §4.1. The next theorem legitimizes the use of
pictures to prove subfactor results.
Theorem 4.2.1 Let N ⊂M be an extremal type II1 subfactor with [M :
N]
1
2 = δ < ∞. For each k let P N⊂M
k
= N′ ∩Mk−1 (isomorphic via θ to Vk,
i.e. N-central vectors in Nk
N M). Then P N⊂M = S
k P N⊂M
k
has a spherical
C∗-planar algebra structure (with labelling set P N⊂M) for which Φ( x ) = x
and, suppressing the presenting map Φ,
(i) For i = 1, 2, . . .k −1,
i
i+1
= Ei
(ii)
x
= δEM′(x) ,
x
= δEMk−2(x)
(iii)
x
=
x
(where on the right, x is considered as an
element of Mk+1)
(iv) Z( x
) = δktr(x)
(x ∈P N⊂M
k
)
Moreover, any other spherical planar algebra structure Φ′ with Φ′( x ) = x
and (i),(ii),(iv) for Φ′ is equal to Φ.
92
Proof. The idea of the proof is fairly simple but it will involve a lot of
details, so we begin with an informal description of the idea. We must show
how to associate an element Φ(T) in N′ ∩Mk−1 to a tangle T whose boxes
are labelled by elements of the appropriate N′ ∩Mj. An example with k = 5
is given in Figure 4.2.2.
R3
R2
R1
Figure 4.2.2
Shade the regions black and white and observe that a smooth oriented curve
starting and ending on the left-hand boundary, and missing the internal
boxes, will generically pass through a certain number of black regions. Num-
ber the connected components of the intersection of the curve with the black
regions 1, 2, . . .n in the order they are crossed. The regions on the curve will
be used to index the tensor product components in Nn
N M.
We will start with our curve close to the boundary so that it crosses no
black regions, and allow it to bubble outwards until it is very close to the
outside boundary at which point it will cross k black regions. As the curve
bubbles out, it will pass through non-generic situations with respect to the
strings of the tangle, and it will envelop internal boxes. At generic times we
will associate an N-central element of Nn
N M with the curve. As the curve
passes through exceptional situations we will change the element of Nn
N M
according to certain rules, the main one of which being that, when the curve
envelops a box labelled by a tensor, we will insert that label into the tensor
93
on the curve at the appropriate spot, as illustrated in Figure ??
x ⊗y ⊗z
a
b
x ⊗y ⊗z
a
b
Figure 4.2.3: Tensor on bubbling curve:
. . . ⊗a ⊗b ⊗. . . →. . . ⊗a ⊗x ⊗y ⊗z ⊗b ⊗. . .
When the curve arrives very close to the boundary it will have associated to
it a central element of Nk
N M which gives an element of N′ ∩Mk−1 via θ.
This element will be Φ(T).
This strategy meets several obstacles.
(1) We must show that Φ(T) is well deﬁned – note that the in-
sertions of 4.2.3 are not well deﬁned for the tensor product
over N.
(2) Φ(T) must be central. This will require either enveloping the
boxes only starting from the white region touching the ﬁrst
boundary point, or projecting onto central vectors at each
step. We will adopt the former policy.
(3)Φ(T) must be independent of isotopy of T and the choice of
the path. Since we must show isotopy invariance eventually,
we might as well suppose that the tangles are in a convenient
standard form, since any two ways of arriving at that standard
form from a given T will only diﬀer by an isotopy.
We begin the formal proof by describing the standard form.
A k-picture (or just “picture” if the value of k is clear) will be the inter-
section of the unit square [0, 1] × [0, 1] in the x−y plane with a system of
94
smooth curves, called strings, meeting only in ﬁnitely many isolated singu-
larities, called “cusps”, where 2m strings meet in a single point. The strings
must meet the boundary of [0, 1]×[0, 1] transversally in just 2k points on the
boundary line [0, 1] × {1}. A cusp (x, y) will be said to be in standard form
if, in some neighborhood of (x, y) the y-coordinates of points on the strings
are all greater than y. A picture may always be shaded black and white with
the y-axis being part of the boundary of a white region.
A picture Θ will be said to be standard if
(i) All its cusps are in standard form, and the region immediately
below the cusp is white.
(ii) The y-coordinate, restricted to strings, has only generic sin-
gularities, i.e., isolated maxima and minima.
(iii) The y-coordinates of all cusps and all maxima and minima are
distinct. This set will be written S(Θ) = {y1, y2, y3, . . . , yc}
with yi < yi+1 for 1 ≤i < c.
An example of a standard k-picture with k = 6 is in Figure 4.2.4.
y1
y2
y3
y5
y9
y7
y4
y8
y6
y10
Figure 4.2.4: A standard 6-picture with S(Θ) = {y1, y2, y3, . . . , y10}.
A standard k picture Θ will be labelled if there is a function from the cusps
of Θ to `
m Vm so that a cusp where 2m strings meet is assigned an element
of Vm (or N′ ∩Mm−1, via θ). We now describe how to associate an element
ZΘ of N′ ∩Mk−1 to a labelled standard k-picture Θ, using the operators of
deﬁnition 4.1.19.
95
Let Θ be a labelled standard k-picture with S(Θ) = {y1, y2, y3, . . . , yc}.
We deﬁne a locally constant function Z : [0, 1]\S(Θ) →Vk(y), where k(y)
is the number of distinct intervals of [0, 1] × {y} which are the connected
components of its intersection with all the black regions of Θ. For instance,
if Θ is as in Figure 4.2.4 and y8 < y < y9 then k(y) = 4. Obviously k(y) is
locally constant and k(y) = k for yc < y < 1. For y < y1, V0 = C and we
set Z(y) = 1. There are ﬁve possible ways for Z to change as y goes from a
value y−, just less than yi, to y+, just bigger than yi. We deﬁne Z(y+) from
Z(y−) in each case:
Case (i). yi is the y-coordinate of a cusp, between the (j −1)th and jth
connected components of the intersection of [0, 1]×y−with the black regions,
as below
y+
yi
y−
j −1
j
Set Z(y+) = αj,c(Z(y−)) where c is the label (in Vk(y−)) associated with the
cusp.
Case (ii).
yi is the y-coordinate of a minimum, with numbering and
shading as below:
y+
yi
y−
j −1
j
j + 1
Set Z(y+) = κj(Z(y−)).
96
Case (iii).
yi is the y-coordinate of a minimum, with numbering and
shading as below:
y+
yi
y−
j −1
j
Set Z(y+) = ηj(Z(y−)).
Case (iv).
yi is the y-coordinate of a maximum, with numbering and
shading as below:
y+
yi
y−
j + 1
j
Set Z(y+) = µj+1(Z(y−)).
Case (v). yi is the y-coordinate of a maximum with shading as below:
y+
yi
y−
j −1
j
j + 1
97
Set Z(y+) = aj(Z(y−)).
Finally, we deﬁne ZΘ = θ(Z(y)) for y > yc, also written Z1(Θ). Our main
job is now to prove that ZΘ is unchanged if Θ is changed by isotopy to another
standard picture Θ′, with labels transported by the isotopy. If the isotopy
passes only through standard pictures, critical points can never change order
or be annihilated or created. The pattern of connected components of the
intersection of the black regions with horizontal lines cannot be changed
either as such a change would have to involve two maxima, minima or cusps
having the same y coordinate. So isotopies through standard pictures do not
change ZΘ.
We next argue that if φt, 0 ≤t ≤1 is an isotopy which preserves the
standard form of each cusp, then ZΘ = Zφ1(Θ). For now Zφt(Θ) can only
change if the singularities of the y-coordinate function change. By putting
the isotopy in general position we see that this can be supposed to happen in
only two ways (see e.g. [Tu], or note that this argument can be made quite
combinatorial by using piecewise linear strings).
(1) The y-coordinates of two of the singularities coincide then
change order while the x-coordinates remain distinct.
(2) The y-coordinate along some string has a point of inﬂection
and the picture, before and after, looks locally like one of the
following
(A)
(B)
(C)
(D)
In case 2), invariance of ZΘ is guaranteed by (v) of 4.1.20 (in the order
C, D, B, A) and in case 1), (i)→(iv) of 4.1.20 is a systematic enumeration of
98
all 25 possibilities. For instance, the case
· · ·
· · ·
is covered by the ﬁrst equation of (iii) of 4.1.20 with j = i. Thus ZΘ is
invariant under isotopies preserving standardness of the cusps.
Now we argue that a general isotopy φt may be replaced by a ˜φt for
which ˜φt preserves the standard form of cusps for all t, without changing
ZΘ. To see this, construct a small disc around each cusp of Θ, suﬃciently
small so that the y-coordinates of all points in a given disc are distinct from
those in any other disc and distinct from any maxima or minima of y on the
strings, and such that the same is true for the images of these discs under
φ1. (Remember that φ1(Θ) is also a standard picture.) Now in each disc D,
construct a smaller disc D0 inside D, centered at the cusp, suﬃciently small
so that one can construct a new isotopy ˜φt having the properties
(i) ˜φt restricted to each D0 is just translation in the plane
(and ˜φt (a cusp) = φt (that cusp)).
(ii) ˜φt = φt on the complement of the discs D.
Thus inside ˜φt(D0), the cusp remains standard and ˜φt is extended somehow to
the annular region between ˜φt(D0) and φt(D). But the mapping class group
of diﬀeomorphisms of the annulus that are the identity on the boundary is
generated by a Dehn twist of 360◦. So in a neighborhood of each cusp point,
φ1 and ˜φ1 diﬀer only by some integer power of a single full twist. Figure ??
illustrates how φ1(Θ) and ˜φ1(Θ) would diﬀer if the twist incurred were a
99
single clockwise twist.
φ1(Θ), near cusp
˜φ1(Θ), near cusp.
Figure 4.2.5
We want to show, ﬁrst in this case and then in the case of an arbitrary
integral power of a full twist, that ZΘ is unchanged.
For this, consider
Figure 4.2.6 which is supposed to be part of a standard labelled picture
in which the maxima and minima of y, in the ﬁgure, and its cusps occur as
an uninterrupted sequence in S(Θ):
y−
y+
Figure 4.2.6
From the deﬁnition of Z(y) we see that
Z(y+)
=
ajµj+1αj+1,cκjηj(Z(y−))
=
αj,ρ(c)(Z(y−))
(by 4.1.13 and 4.1.14)
100
(Here the cusp is labelled by c ∈N′ ∩Mn−1 where n = 3 in Figure 4.2.6.)
Similarly we see that if the cusp is surrounded by a full 360◦twist,
Z(y+)
=
αj,ρn(b)(Z(y−))
=
αj, b(Z(y−))
(by Theorem 4.1.18)
Thus if a cusp (or any part of a picture that is just a scaled down standard
labelled picture) is surrounded by a single clockwise full twist, the eﬀect on
ZΘ is as if the twist were not there. If there were anticlockwise full twists
around a cusp, surround it further by the same number of clockwise twists.
This does not change ZΘ, but the cancelling of the positive and negative
twists involves only isotopies that are the identity near the cusps. Thus by
our previous argument clockwise full twists around cusps do not change ZΘ
either. We conclude
Zφ1(Θ) = Z˜φ1(Θ) = ZΘ .
We have established that ZΘ may be assigned to a standard labelled
picture by a product of elementary maps α, κ, η, a, µ in such a way that ZΘ is
unchanged by isotopies of Θ. We can now formally see how this makes `
n Vn
a planar algebra according to §1. The labelling set will be `
n Vn itself. The
ﬁrst step will be to associate a labelled picture β(T) with a labelled tangle
T. To do this, shrink all the internal boxes of T to points and isotope the
standard k-box to [0, 1] × [0, 1] with all the marked boundary points going
to points in [0, 1] × 1. Then distort the shrunk boxes of T to standard cusps,
by isotopy, so that the string attached to the ﬁrst boundary point of the box
becomes the ﬁrst string (from the left) attached to the cusp. The procedure
near a 4-box of T is illustrated in Figure ?? :
1
2
3
4
6
5
7
8
R
1
2
3
4
5
6
7
8
1
R
101
Figure 4.2.7
The label associated to the cusp is just θ−1 of the label associated to the box
but we may reasonably suppress θ−1.
Figure 4.2.8 illustrates a labelled tangle T and a labelled standard picture
β(T):
R
P
Q
R
P
Q
The tangle T
A standard picture β(T)
Figure 4.2.8
Note that β(T) is not well deﬁned, but two diﬀerent choices of β(T) for a
given T will diﬀer by an isotopy so the map Φ, Φ(T) = Zβ(T), gives a well
deﬁned linear map from the universal planar algebra on `
k N′ ∩Mk−1.
We now check that Φ makes (P N⊂M) into a connected spherical C∗-
planar algebra. The ﬁrst thing to check is that Φ is a homomorphism of
ﬁltered algebras. But if T1 and T2 are labelled k-tangles, a choice of β(T1T2)
is shown below (k = 3).
β(T1)
β(T2)
y
102
If y is as marked, from the deﬁnition of Z, Z(y) = Z(β(T1)) ⊗Z(β(T2)).
Moreover each pair of maximal
contributes a factor χi (= aiµi+1)
to Z(y) as y increases, so if k is even, part (1) of 4.1.24 gives Φ(T1T2) =
Φ(T1)Φ(T2) and if k is odd (as in the ﬁgure) the last maximum has the black
region above so contribute a factor µ and part (ii) of 4.1.24 applies.
That Φ is compatible with the ﬁltrations amounts to showing that
R
R
R
R
) = Φ(
Φ(
or Z(
)
)
) = Z(
If k is even this follows from 4.1.25 and if k is odd it follows from 4.1.26
(together with P
b∈B bvkb∗= δEkEk−1 . . . E2 to take care of the factor κ
introduced by the minimum in the picture). So Φ is a homomorphism of
ﬁltered algebras.
Annular invariance (and indeed the whole operadic picture) is easy. If
T is an element of P(`
k N′ ∩Mk−1) (linear combination of tangles) with
Φ(T) = 0, then if T is surrounded by an annular labelled tangle A, then we
may choose β(πA(T)) to look like
· · ·
β(A)
β(T)
(Strictly speaking, one needs to consider such a picture for each tangle in the
linear combination forming T, and add.) Clearly if Zβ(T) = 0, so is Zβ(πA(T)),
since the map αj,θ−1(Zβ(T )) is applied in forming Zβ(πA(T)).
We now turn to planarity. By deﬁnition V0 = C so we only need to show
dim V1,1 = 1. A basis element of P1,1(`∞
k=1 N′ ∩Mk−1) is a 1-tangle T with
103
a vertical straight line and planar networks to the left and right. We may
choose β(T) to be as depicted below
T1
T2
T3
where there are 0-pictures inside the regions T1, T2, . . .. It is a simple conse-
quence of our formalism that a closed picture surrounded by a white region
simply contributes a scalar in a multiplicative way. This is because one may
ﬁrst isotope the big picture so that all the maxima and cusps in the 0-picture
have y coordinates in an uninterrupted sequence in S, and the last singular-
ity must be a maximum, shaded below, the ﬁrst being a minimum, shaded
above. The ﬁnal map will be an aj and will send the contribution of the
0-picture to an element of N′ ∩N = C. Thus we only need to see that 0-
pictures inside a black region contribute a scalar in a multiplicative way. But
we may isotope the big picture so that the singular y-values of the 0-picture
occur in uninterrupted succession, and near the 0-picture the situation is as
below:
y1
y2
picture
some
With y1 as marked, Z(y1) will be P
b∈B b ⊗x ⊗b∗for some element x in
N′ ∩M. But then Z(y2) will be P
b∈B bxb∗∈M′ ∩M = C, by 4.1.5. So
P N⊂M is a planar algebra.
The spherical property is easy: comparing
104
picture
and
picture ,
we see that the partition functions are the same since one gives EM′ applied
to an element of N′∩M, and the other gives EN applied to the same element
with the correct powers of δ contributed from the minimum in the ﬁrst picture
and the maximum in the second. Either way we get the trace by extremality.
For the ∗-structure, observe ﬁrst that
θ(x1 ⊗x2 . . . ⊗xk)∗= θ(x∗
k ⊗x∗
k−1 ⊗. . . ⊗x∗
1)
so θ(αj,c(x))∗= θ(αk−j+2,c∗(x∗)),
θ(aj(x))∗= θ(ak−j+1(x∗)),
θ(µj(x))∗=
θ(µn−j+2(x∗)),
θ(ηj(x))∗= θ(ηk−j+2(x∗)) and θ(κj(x))∗= θ(κk−j+1(x∗)).
Moreover if T is a labelled tangle, β(T ∗) is β(T) reﬂected in the line x = 1
2 and
with labels replaced by their adjoints (via θ). We conclude that (Zβ(T))∗=
Zβ(T ∗) by applying the relations above at each of the y-values in S(β(T)) =
S(β(T ∗)).
The C∗-property is just the positive deﬁniteness of the partition function.
But if T is a labelled k-tangle,
β( T
) =
β(T)
soZΦ( T
) = δEMk−2(Φ( T
))
by 4.1.22. Applying this k times we get
Z( T
) = δk tr(Φ( T
))
so the positive deﬁniteness of Z follows from that of tr.
We now verify (i)→(iv) in the statement of the theorem.
(i) Since Φ is a homomorphism of ﬁltered algebras, it suﬃces to prove the
formula when k = i.
If k = 2p + 1,
Zβ(| |...
) = θ(Z1(
))
105
= δ−Pθ( P
b1,b2,...,bp b1 ⊗b2 ⊗. . . ⊗bp ⊗1 ⊗1 ⊗b∗
p ⊗. . . ⊗b∗
2 ⊗b∗
1)
= E2p+1
by Lemma 4.1.27.
If k = 2p,
Zβ(| |...
) = θ(Z1(
))
= δ−p−1θ( P
b1...bp+1 b1 ⊗b2 ⊗. . . ⊗bp ⊗b∗
pbp+1 ⊗b∗
p+1 ⊗b∗
p−1 ⊗. . . ⊗b∗
1)
= E2p
by Corollary 4.1.28.
(ii) The ﬁrst formula follows from 4.1.5 and we showed the second when
we proved the positive defIniteness of the partition function.
(iii) This is just the ﬁltered algebra property.
(iv) We also showed this in the positive deﬁniteness proof.
All that remains is to prove the uniqueness of the planar algebra structure.
First observe that, as in Proposition 1.14, a labelled tangle may be arranged
by isotopy so that all of its boxes occur in a vertical stack. After further
isotopy and the introduction of kinks or redundant loops, one may obtain
the picture below for the tangle (in Pk)
...
k boundary point
T =
R1
R2
σ1
σ2
σn
106
where the regions marked σ1, . . ., σn contain only strings and σ2, . . ., σn−1
have a ﬁxed number p of boundary strings top and bottom, ≥k. Clearly
p−k is even so we conclude that, if Φ1 is some other planar algebra structure
satisfying (i) and (ii) then
Φ1(T) = δ−p−k
2
Φ1(
T
) ,
where we have introduced p−k
2
maxima and minima. (To see this just apply
the second formula of (ii) p −k times.) Thus we ﬁnd that it suﬃces to prove
that Φ′ = Φ on a product of Temperley-Lieb tangles and tangles of the form
x
· · ·
· · ·
But the Temperley-Lieb algebra is known to be generated by {∥. . . ∪
∩i i+1∥}
whose images are the Ei’s by (i). By condition (ii), we see that it suﬃces to
show that
Φ′(|| x ) = Φ(|| x ). To this end we begin by showing
Φ′(
a ) = Φ(
a )
for a ∈N′ ∩Mk .
This follows from the picture below
a
· · ·
· · ·
for we know that
Φ′(| a ) = EM′(a) = Φ(| a ).
Now to show that X = Φ′(|| x ) = Φ(|| x ) = Y it suﬃces to show that
tr(aX) = tr(aY ) for all a ∈N′ ∩Mk. But up to powers of δ,
a
x
x
a
x
a
tr(Φ′(
)) =tr(Φ′(
)) =tr(Φ(
)) =tr(aY )
tr(aX) =
107
and we are done.
□
Deﬁnition 4.2.8. The annular Temperley Lieb algebra AT(n, δ), for n even,
will be the ∗-algebra with presentation:
· · ·
· · ·
,
F1 =
,
,
,
F2 =
Fk =
F2k =
Fk+2 =
Fk+1 =
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
Remark. Since (F1F2 . . . Fk)(F1F2 . . . Fk)∗= δF1 and (F1F2 . . . Fk)∗(F1F2 . . . Fk) =
δFk, if H is a Hilbert space carrying a ∗-representation of AT(n, δ), dim(FiH)
is independent of i.
Corollary 4.2.9 If N ⊂M is an extremal subfactor of index δ−2 > 4, each
N′ ∩Mk−1 is a Hilbert space carrying a ∗-representation of AT(2k, δ). And
dim(Fi(N′ ∩Mk−1)) = dim(N′ ∩Mk−2) = dim(M′ ∩Mk−1).
Proof. Let Fi be the elements of A(φ) deﬁned as follows
108
The relations are easily checked, the Hilbert space structure on N′ ∩Mk−1
being given by the trace −⟨a, b⟩= tr(b∗a). Since Fk(N′ ∩Mk−1) = N′ ∩Mk−2
and F2k(N′ ∩Mk−1) = M′ ∩Mk−1 (by (ii) of 4.2.1). We are through.
□
Lemma 4.2.10 If H carries an irreducible ∗-representation of AT(n, δ) for
δ > 2, n > 4, and dim(FiH) = ∞, then dim H = \ (remember n is even).
Proof.
Let vi be a unit vector in FiH for each i.
Then Fjvi is a
multiple of vj so the linear span of the vi’s is invariant, thus equal to H by
irreducibility. Here dim H ≤\ (this does not require δ > 2). Moreover
the commutation relations imply |⟨vi, vi+1⟩| = δ−1 and ⟨vi, vj⟩= 0 or 1 if
i̸ = j ± 1. The case ⟨vi, vj⟩= 1 forces i = j so it only happens if n = 4. So
by changing the vi’s by phases we may assume that the matrix δ⟨vi, vj⟩is
∆n(ω) =







δ
1
0
0 . . .ω
1
δ
1
0 . . . 0
0
1
δ
1 . . . 0
...
...
¯ω
0
. . .
1 δ







.
It is easy to check that det(∆n(ω)) = P2n(δ)−P2n−2(δ)−2Re(ω) where Pn(δ)
are Tchebychev polynomials. Thus det(∆n(ω)) is smallest, for ﬁxed δ, when
ω = 1. But then
∥∆n(1) −δ id∥= 2 by Perron-Frobenius so det ∆n(1) > 0 for δ > 2.
□
Corollary 4.2.11 Suppose the principal graph of the subfactor N ⊂M,
[M : N] > 4, has an initial segment equal to the Coxeter-Dynkin diagram
Dn+2 with ∗as shown:
n
· · ·
∗
Then there are at least two edges of the principal graph connecting the two
points at distance n + 1 from ∗to points of distance n + 2.
Proof. Since δ > 2, the Temperley-Lieb algebra generated by {1, e1, e2, . . . , ek}
in N′ ∩Mk has dimension
1
k+2
 2k+4
k+1

. The information on the principal graph
109
then gives the following Bratteli diagram for the inclusions N′ ∩Mn−1 ⊂
N′ ∩Mn ⊂N′ ∩Mn+1:
N′
∩
Mn+1
∪
N′
∩
Mn
∪
N′
∩
Mn−1
Here we have shown only that part of the Bratteli diagram relevant to the
proof. Only the two 1’s in the middle row can be connected to anything in the
top row other than vertices corresponding to the ideal generated by en+1. We
have to show that it is impossible for just one of these 1’s to be connected,
with multiplicity one, to a new principal graph vertex. By contradiction,
suppose this were the case. Then we would have
dim(N′ ∩Mn+1) =
1
n + 3
2(n + 2)
n + 2

−(n + 1)2 + (n + 2)2
since the only diﬀerence between the N′ ∩Mn+1 level of the Bratteli diagram
and the Temperley-Lieb Bratteli diagram (see [GHJ]) is that the “n + 1” in
Temperley-Lieb has become “n + 2”. Thus
dim(N′ ∩Mn+1) =
1
n + 3
2(n + 2)
n + 2

+ 2n + 3 .
But consider N′ ∩Mn+1 as a module over AT(2n + 4, δ). The Temperley-
Lieb subalgebra is invariant and so therefore is its orthogonal complement
TL⊥of dimension 2n + 3. But consider the image of Fn+2 = δEN′∩Mn. It
is
1
n + 2
2(n + 1)
n + 1

+ 1 because of the single extra vertex on the principal
graph at distance n + 1 from ∗.
But, by pictures, the image of Fn+2 restricted to the Temperley-Lieb sub-
algebra of N′∩Mn+1 is
1
n + 2
2(n + 1)
n + 1

. Hence on TL⊥, dim(F1(TL⊥) = 1.
So by Lemma 4.2.10, dim(TL⊥) ≥2n + 4, a contradiction.
□
We have obtained far more powerful results than the following by a study
of the representation theory of AT(n, δ). These results will be presented in a
110
future paper of this series. We gave the result here because it was announced
some time ago. It is a version of the “triple point obstruction” of Haagerup
and Ocneanu (see [Ha]) but proved by a rather diﬀerent method!
If we apply the argument we have just given when δ ≤2 we obtain
nontrivial but known results. The argument is very simple so we present it.
Deﬁnition 4.2.12 The critical depth of a planar algebra P will be the
smallest k for which there is an element in Pk which is not in the Temperley-
Lieb subalgebra TLk.
In the C∗- case, if δ < 2 ,the norm of the principal graph is less than 2 so
as in [GHJ] it follows that the principal graph is an A,D or E Coxeter graph
with ∗as far as possible from a vertex of valence 3. In particular if k is the
critical depth, the dimension of the quotient Pk
Vk is at most 1 so the rotation
acts on it by multiplication by a k-th root of unity. We will use the term
“chirality” for this root of unity in an appropriate planar algebra.
The restrictions on the principal graph in the following theorem were ﬁrst
obtained by Ocneanu.
Theorem 4.2.13 If P is a C∗-planar algebra with δ < 2 then the principal
graph can be neither Dn with n odd nor E7. If the principal graph is D2n the
chirality is −1, if it is E6 the chirality is e±2πi/3 and if it is E8 the chirality
is e±2πi/5.
Proof. If k is the critical depth, by drawing diagrams one sees that the
ω in the (2k + 2)x(2k + 2) matrix ∆n(ω) is the chirality. Also if δ = z + z−1,
we have det(∆n(ω)) = z2k+2 +z−(2k+2) −ω −ω−1. If κ is the Coxeter number
of the principal graph we have z = e±πi/κ.
On the other hand, by the argument of Corollary 4.2.11, the dimension
of Pk+1 would be too great if the determinant were non-zero. Thus we have,
whatever the Coxeter graph may be,
e(2k+2)πi/κ + e−(2k+2)πi/κ = ω + ω−1
for a k-th root of unity ω.
The critical depth for Dm would be m −2 so the left hand side of the
equation is −2 so that ω has to be −1. But if m is odd, −1 is not an m−2th
111
root of unity so Dm cannot be a principal graph. If m is even we conclude
that the chirality is −1.
The critcal depth for E7 is 4 and the Coxeter number is 18. The above
equation clearly has no solution ω which is a fourth root of unity.
For E6 the critical depth is 3 and the Coxeter number is 12 so ω = e±2πi/3.
For E8 the critical depth is 5 and the Coxeter number is 30 so ω = e±2πi/5.
□
The above analysis may also be carried out for δ = 2 where the Coxeter
graphs are replaced by the extended Coxeter graphs.
In the D case the
presence of the Fuss Catalan algebra of example 2.3 makes it appropriate to
replace the notion of critical depth by the ﬁrst integer such that Pk is bigger
than the Fuss Catalan algebra. One obtains then that the chirality, together
with the principal graph, is a complete invariant for C∗-planar algebras with
δ = 2 (see [EK] p. 586).
We end this section by giving more details of the planar structure on
N ⊂M. In particular we give the subfactor interpretations of duality, re-
duction, cabling and tensor product. The free product for subfactors is less
straightforward.
Corollary 4.2.12 If N ⊂M is an extremal II1 subfactor then, with the
notation of §3.2, λ1(P N⊂M) = P M⊂M1, as planar algebras.
(Note that
P M⊂M1
k
= M′ ∩Mk which is a subset of P N⊂M
k+1
. We are saying that the
identity map is an isomorphism of planar algebras.)
Proof. Equality of P N⊂M
k
and λ1(P N⊂M) as sets follows immediately
from (ii) of 4.2.1. To show equality of the planar algebra structure we use
the uniqueness part of 4.2.1.
By deﬁnition of λ1(Φ), for x ∈M′ ∩Mk ⊂N′ ∩Mk,
x = ΦM⊂M1( x ) = ΦN∩M( x
) = λ1(Φ)( x
).
Properties (i) and (iv) are straightforward as is the second equation of (ii).
So we only need to check the ﬁrst equation of (ii), i.e.,
λ1(ΦN⊂M)(
x ) = δEM1(x)forx ∈M′ ∩Mk.
112
But by deﬁnition
λ1(ΦN⊂M)(
x ) = 1
δΦ(
x ).
If we deﬁne g : ⊗k
NM →⊗k
NM and f : ⊗k
NM →⊗k−2
N M by g(y) = P
b∈B byb∗
and f(x1 ⊗. . . ⊗xk) = E(x1)x2 ⊗. . . ⊗xk−1E(xk), and if θ(y) = x for
x ∈M′ ∩Mk, by the deﬁnition of ΦN⊂M in Theorem 4.2.1,
ΦN⊂M(
x ) = θ(
X
b∈B
b ⊗f(g(y)) ⊗b∗).
But since θ is an M −M bimodule map and x commutes with M, g(y) = δ2y.
But by deﬁnition of θ and 4.1.8,
θ(
X
b∈B
b ⊗f(y) ⊗b∗) = δ−2 X
b∈B
bE1xE1b∗.
Since {bE1} is a basis for M1 over M, we are done by 4.1.5.
□
Iterating, we see that λn(P N⊂M) is the planar algebra for the subfactor
Mn−1 ⊂Mn.
For cabling we have the following
Corollary 4.2.13 If N ⊂M is an extremal II1 subfactor, the cabled planar
algebra Cn(P N⊂M) of §3.3 is isomorphic to P N⊂Mn−1.
Proof. We will again use the uniqueness part of 4.2.1. It follows from
[PP2] that if we deﬁne En
i to be
(EniEni−1Eni−2 . . . En(i−1)+1)(Eni+1Eni . . . En(i−1)+2) . . . (En(i+1)−1En(i+1) . . . Eni)
(a product of n products of E’s with indices decreasing by one), and vn
i with
respect to En
i as in 4.1.9, then the map x1⊗N x2 . . .⊗N xk →x1vn
1 x2vn
2 . . . vn
kxk
establishes, via the appropriate θ’s, a ∗-algebra isomorphism between the
(k −1)-th algebra in the tower for N ⊂Mn−1 and Mkn−1, hence between
P N⊂Mn−1
k
and P N⊂M
nk
= C\(PN ⊂M).
113
If γ is the inverse of this map, γ ◦C\(⊕) thus deﬁnes a spherical planar
algebra structure on P N⊂Mn−1. The labelling set is identiﬁed with P N⊂Mn−1
via γ, so
γ ◦Cn(ΦN⊂M)( x
) = ΦN⊂M)( x ) = x.
Condition (i) of 4.1 for γ ◦Cn(Φ) follows by observing that
Cn(Φ)(
i
i+1
) = En
i . Condition (ii) follows from 4.2.12, and condition
(iv) is clear.
□
Reduction is a little more diﬃcult to prove.
Corollary 4.2.14 Let N ⊂M be an extremal II1 subfactor and p a projec-
tion in N′∩M. The planar algebra p(P N⊂M)p of §3.3 is naturally isomorphic
to the planar algebra of the reduced subfactor pN ⊂pMp.
Proof. We ﬁrst claim that the tautological map
α :
k
O
pN
pMp →
k
O
N
M ,
α(
k
O
i=1
xi) =
k
O
i=1
xi
is an injective homomorphism of ∗-algebras when both domain and range of
α are equipped with their algebra structures via the respective maps θ as in
4.1.10. To see this observe that the conditional expectation EpN : pMp →pN
is just
1
tr(p)EN. It follows that αaj = ajα and clearly αµj = µjα, so by 4.1.24,
α is a ∗-algebra homomorphism.
The next thing to show is that α takes pN-central vectors to θ−1(pk(N′ ∩
Mk−1)pk), with pk as in 3.3, using the planar algebra structure on N′ ∩Mk.
Let π : ⊗k
NM →⊗k
NM be the map π(x1 ⊗x2 . . . ⊗xk) = px1p ⊗px2p ⊗. . . ⊗
pxkp, which is well deﬁned since p commutes with N. Then a diagram shows
that, for x ∈N′∩Mk−1, pkxpk = θ(π(θ(x))), and conversely, if θ−1(x) is in the
image of α, π(θ−1(x)) = θ−1(x) so pkxpk = x. Hence α induces a ∗-algebra
isomorphism between P pN⊂pMp
k
and pk(N′∩Mk−1)pk. To check that this map
induces the right planar algebra structure, we ﬁrst observe that α commutes
suitably with the maps η and κ of 4.1.19. For η we have α ◦η = π ◦η ◦α
by deﬁnition. For κ, note that if we perform the basic construction of [J1]
on L2(M),
1
tr(p)pENp is the basic construction projection for pN ⊂pMp on
114
L2(pMp). Thus if {b} is a basis for pMp over pN we have P
b bENb∗= tr(p)p.
So if
x = x1 ⊗. . . ⊗xk ∈
k
O
pN
pMp ,
α(κj(x)) =
1
tr(p)δ
X
b
x1 ⊗. . . ⊗xjb ⊗b∗⊗xj+1 ⊗. . . ⊗xk
and
κj(α(x)) = 1
δ
X
c
x1 ⊗. . . ⊗xjc ⊗c∗⊗xj+1 ⊗. . . ⊗xk .
Applying θ we see that ακj = κjα.
With these two commutation results it is an easy matter to check that α
deﬁnes planar algebra isomorphism between P Np⊂pMp and p(P N⊂M)p, using
the uniqueness part of 4.2.1 or otherwise.
Corollary 4.2.15 If N1 ⊂M1 and N2 ⊂M2 are extremal ﬁnite index
subfactors, then P N1⊗N2⊂M1⊗M2 is naturally isomorphic to the tensor product
P N1⊂M1 ⊗P N2⊂M2 of §3.4.
Proof. We leave the details to the reader.
□
