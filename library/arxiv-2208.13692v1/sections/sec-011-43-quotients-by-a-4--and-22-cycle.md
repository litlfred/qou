---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-011-43-quotients-by-a-4--and-22-cycle
section_title: "Quotients by a 4- and 2,2-cycle"
section_number: 4.3
pages: 21-24
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
doc_brief: "Bring's curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
quotients we expect we shall now write them explicitly. We will begin with the 2,2-cycle
corresponding to U 2 with the 4-cycle U arising in the discussion. Recall that we have
U 2 : [X,Y,Z ]→ [X,Z,Y ], ψ (U 2) = (12)(34).
The normaliser of ⟨(12)(34)⟩ in S5 is NS5(⟨(12)(34)⟩) = ⟨(12), (1324)⟩∼= D8. As we re-
marked earlier, NS5(⟨(12)(34)⟩)/⟨(12)(34)⟩∼=V4 are symmetries which remain when we go
to the quotient B/
⟨
U 2⟩
and we expect the quotient genus-2 curve to have (at least) this
V4 symmetry group. One of these involutions, which we will later see to be (12) = (34),15
is the hyperelliptic involution of the quotient curve and so further quotienting by this sym-
metry gives P1. Quotienting by the other two involutions will yield elliptic curves, and we
will complete this construction now, both from the perspective of the HC-model, and the
P4-model.
Starting in the HC-model, in order to get the ﬁrst quotient B/
⟨
U 2⟩
we express our curve
in terms of the invariants of U 2: X, T :=Y +Z, and V :=YZ . Then
0 =X(Y 5 +Z 5) + (XYZ )2−X 4YZ − 2(YZ )3,
=X(T 5− 5T 3V + 5TV 2) +X 2V 2−X 4V− 2V 3.
In P1,1,2 this is our genus-4 curve. Setting 16 T = 1 and viewing
0 =X(1− 5V + 5V 2) +X 2V 2−X 4V− 2V 3
as the aﬃne part of a projective curve we have (after a not-very-illuminating transformation,
for which Maple was used) the hyperelliptic curve
(10) C1 : B2 =A6 + 4A5 + 10A3 + 4A + 1.
This is the genus-2 curve of [RR92] with automorphism group V4. Calculating the Igusa-
Clebsch invariants (which give the Q-isomorphism class of a curve) and searching the
LMFDB [LMF22] shows that this is a model for the modular curve X0(50), which we ver-
ifying by directly calculating a model for X0(50) over Q using [Shi95]. The substitutions
A = (2 +A′)/(2−A′), B = 4B′/(2−A′)3 make the V4 symmetry clearer, giving
(B′)2 +
[
(A′)6− 5(A′)4− 40(A′)2− 80
]
= 0,
where we have the hyperelliptic involution B′→− B′ and the map A′→− A′ generating
V4. We shall now be explicit about how these work.
15The ⟨(12)(34)⟩ cosets of the normaliser are {e, (12)(34)}, {(12), (34)}, {(13)(24), (14)(23))}, and
{(1324), (1423)}.
16Equally one may set X = 1 but we note that setting V = 1 yields a genus 4 curve as here V is not of
weight 1.
22 H. W. BRADEN AND LINDEN DISNEY-HOGG
As previously mentioned, quotientingC1 by either of the two non-hyperelliptic involutions
yields an elliptic curve, with each involution having two ﬁxed points from Riemann-Hurwitz.
Quotienting by (B′,A′)→ (B′,−A′) by introducing A′′ =−(A′)2 yields
(11) E1 : (B′)2 = (A′′)3− 5(A′′)2− 40(A′′)− 80 with j-invariant jE1 =−5× 293
25 =j(τ0).
The ﬁxed points are ( A′,B′) = (0 ,±√−80), corresponding to the two points ( X,V ) =
([1±
√
5]/2,−1±
√
5/2), which are the images of the four vertices [1 : ±i :∓i :−1 : 0] and
[1 :±i :−1∓i : 0] respectively, depending on sign. We recognise E1 to be the elliptic curve
E1 in [RR92].
We may also quotientC1 by (B′,A′)→ (−B′,−A′). To do this write C1 as
(B′)2C 4 +
[
(A′)6− 5(A′)4C 2− 40(A′)2C 4− 80C 6]
= 0,
from where we see the same automorphism acts as C→−C. Quotienting by this action by
introducing C′ =−C 2 yields
(B′)2(C′)2 = (A′)6− 5(A′)4(C′)− 40(A′)2(C′)2− 80(C′)3.
Setting A′ = 1 and taking B′′ =B′C′ gives the standard elliptic form
(12) E2 : (B′′)2 = 1− 5(C′)− 40(C′)2− 80(C′)3, j E2 =−25
2 =j(5τ0).
The ﬁxed point of this involution is [ B′ :A′ :C] = [1 : 0 : 0]; this is a singular point where
the desingularization corresponds to the 2 points at inﬁnity, or correspondingly ( X,V ) =
(∓i/2−1/2, 1/4), which are the images of the two vertices [1 :−1 :±i :∓i : 0]. We recognise
E2 to be E2 in [RR92].17
Next let us quotient the P4-model directly by the action of (12)(34) and compare with
these quotients just obtained from the HC-model. To this end we introduce semi-invariants
of the action of (1324) = ψ(U), deﬁned by
(s1,s 2,s 3,s 4)T =


1 1 1 1
1 −1 i −i
1 1 −1 −1
1 −1 −i i

 (x1,x 2,x 3,x 4)T.
These are constructed such that U·sj = ij−1sj, and so we have U 2-invariants [s : t : u :
v] := [s1 :s2s4 :s3 :s2
4]∈ P1,2,1,2.18 In terms of these invariants we have
H2 = 1
4
(
5s2 +u2 + 2t
)
,
H3 = 3
16
(
−5s3 +su2 + t2u
v + 2st +uv
)
.
Eliminating t from these equations, and setting s = 1, we can use Maple to get the genus-2
curve in Weierstrass form
(13) C1 : y2 = 100− 25x2− 10x4−x6
where x = u and y =−10 + 2uv. The roots of the sextic here are a M¨ obius transform
of the curve C1 previously given (namely x↦→
√
20/x), so these curves are the same over
Q[
√
5]. Note the reason we see Q[
√
5] here is that it is the degree-2 subﬁeld of Q[ζ], the
17There is a typo in the constant term of R&R’s E2 if it is to have the stated j-invariant.
18Note one could have instead taken v = s2
2 for the last invariant, but the choice above happens to be
better around the vertices that are the ﬁxed points of the 4-cycle. Moreover, recognise that the invariants
taken are deﬁned over the ﬁeld extension Q[i] and not Q.
BRING’S CUR VE: OLD AND NEW 23
ﬁeld required to have equivalence of the Hulek-Craig and P4-models of Bring’s curve. We
now aim to identify theV4 of this curve described earlier with the quotient of the normaliser
⟨(12), (1324)⟩/⟨(12)(34)⟩. One can check that (12) : [ s : t : u : v]→ [s : t : u : t2/v]. This
ﬁxes x, and so must be the automorphism y→−y; that is (12) = (34) is the hyperelliptic
involution ofC1. Indeed one can check
y =−10 + 2uv↦→− 10 + 2t2u
v ,
=−10− 2
(
−5 +u2 + 2t +uv
)
,
=−10− 2
(
−10 +uv + (5 +u2 + 2t)
)
,
= 10− 2uv =−y.
Likewise, (1324) : [ s : t : u : v]→ [s : t :−u :−v], and so leads to the automorphism
(x,y )→ (−x,y ). Now if x = x2, the elliptic curve y2 = 100 − 25x− 10x2− x3 has j-
invariant−25/2 and so we may identify E2∼=B/⟨(12)(34), (1324)⟩ =B/⟨(1324)⟩. Similarly
(13)(24) : [s :t :u :v]→ [s :t :−u :−t2/v] leads to (x,y )→ (−x,−y) and we may identify
E1∼=B/⟨(12)(34), (13)(24)⟩. Note when we compare with [RR92], we diﬀer from R&R in
the identiﬁcation of which quotient is being taken and their ascribing of τ0 and 5τ0. Our
results agree with those of [Web05], wherein the author describes an order-4 rotation (which
he calls φ, but we shall call ˜U), and calculates the quotient by its action T =B/
⟨
˜U
⟩
to be
T : y2 = 4x3− 75x− 1475, j T =−25
2 =j(5τ0).
Note that our strategy of semi-invariants can be used directly to calculate the quotient by
the 4-cycle (1324), something we were unable to do in the HC-model because of the non-
linearity of the automorphism U. To do so introduce new variables invariant under (1324)
(and so necessarily under (12)(34)) given by u′ = uv, v′ = v2. These let us rewrite the
deﬁning equations of Bring’s curve as
H2 = 1
4
(
5s2 + (u′)2
v′ + 2t
)
,
H3 = 3
16
(
−5s3 + s(u′)2
v′ + t2u′
v′ + 2st +u′
)
,
and we can apply Maple to ﬁnd a Weierstrass form of the resulting elliptic curve. This is
exactly the process of quotienting by (x,y )↦→ (−x,−y) as above, but in a diﬀerent language.
Furthermore, from our previous investigation using group theory, we know that the quo-
tientB/V4, where this V4 is the one containing only 2,2-cycles, can further be quotiented
by (234) to giveB/A4. Rather than attempt to construct this quotient using the invariants
previously calculated on the 2,2-quotient, we step back and recall that the invariant ring
Q[x1,...,x n]An is generated by the symmetric polynomials sk =∑n
i=1xk
i for k = 1,...,n
and the Vandermonde polynomial V =∏
1≤i<j≤n(xj−xi). As generators of the invariant
algebra we know that there must be a relation between V 2 and the other generators as V 2
is an Sn-invariant, and theSn-invariant algebra is generated by thesk. Taking n = 4 in the
case of Bring’s curve, the relations imposed from the curve are s2 +s2
1 = 0 = s3−s3
1, and
this gives for the additional relation,
(14) 4 s3
4− 373
16 s4
1s2
4 + 431
8 s8
1s4− 701
16 s12
1 +V 2 = 0.
24 H. W. BRADEN AND LINDEN DISNEY-HOGG
Settings1 = 1 (as we may do at all points on the quotient except those points coming from
the vertices on Bring’s curve) we see this is clearly an elliptic curve E3 with hyperelliptic
involutionV →−V , and for which we can calculate the j-invariant to be 2113×5
215 =j(3τ0).19
Further quotienting by the hyperelliptic involution then corresponds to the quotient B/S4,
which is P1 as expected, being the quotient by a large automorphism group.
