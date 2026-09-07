---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-007-12-the-homfly-q-and-kau
section_title: "The HOMFLY, Q, and Kau"
section_number: 1.2
pages: 18-21
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
man polynomials
The skein polynomial (or the HOMFLY polynomial) PL(l;m )2Z[l1;m1]o f
an oriented link L is uniquely characterized by
l−1PL+ (l;m )−lPL−(l;m )= mPL0 (l;m );
PO(l;m )=1 ;
where O denotes the trivial knot, and L+ , L−,a n dL0 are three oriented links,
which are identical except for a ball, where they di
er as shown in Figure 1.
For a knot K , PK (l;m )2 Z[l2;m ]. The Kau
man polynomial FL(a;z )2
Z[a1;z1] of an oriented link L is de
ned by FL(a;z )= a−w(D)[D] for an
unoriented diagram D presenting L (forgetting its orientation), where [ D]i s
uniquely characterized by
" #
+
" #
=z
 " #
+
" #!
" #
=a
" #
;
[O]=1 :
For a knot K , FK(a;z )2Z[a1;z ]. The Q polynomial QL(x)2Z[x1]o fa n
unoriented link L is uniquely characterized by
Q
 
+Q
 
=x
 
Q
 
+Q
 !
Q(O)=1 :
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 391
It is known that
VL(t)= PL(t;t 1=2−t−1=2)= FL(−t−3=4;t 1=4 +t−1=4);
L(t)= PL(1;t 1=2−t−1=2);
QL(z)= FL(1;z );
where L(t) denotes the Alexander polynomial of L.T h e v a r i a b l em of
PL(l;m ) is called the Alexander variable . See, e.g. [206, 255], for details of
this paragraph.
Let the span of a polynomial denote the maximal degree minus the minimal
degree of the polynomial.
Problem 1.13 (A. Stoimenow) Does the Jones polynomial V admit only

nitely many values of given span? What about the Q polynomial or the skein,
K a u 
 m a np o l y n o m i a l s( w h e n
 x i n gt h es p a ni nb o t hv a r i a b l e s ) ?
Remark (A. Stoimenow) It is true for the skein polynomial when bounding
the canonical genus (for which the Alexander degree of the skein polynomial is
a lower bound by Morton), in particular it is true for the skein polynomial of
homogeneous links [97]. It is true for the Jones, Q and Kau
man F polyno-
mial of alternating links (for F more generally for adequate links). One cannot
bound the number of di
erent links, at least for the skein and Jones polyno-
mial, because Kanenobu [192] gave in
nitely many knots with the same skein
polynomial.
Problem 1.14 (A. Stoimenow) Why are the unit norm complex numbers 

for which the valueQK (
) has maximal norm statistically concentrated around
e11p−1=25 ?
Remark (A. Stoimenow) The maximal point of jQK(e2p−1t)j for t2 [0; 1)
is statistically concentrated around t =1 1=50. This was revealed by an exper-
iment in an attempt to estimate the asymptotical growth of the coecients of
the Q polynomial. There seems no di
erence in the behaviour of alternating
and non-alternating knots.
Problem 1.15 (M. Kidwell, A. Stoimenow) Let K be a non-trivial knot, and
let WK be a Whitehead double of K. Is then
degmPWK (l;m )=2d e gz FK (a;z )+2?
Geometry &TopologyMonographs, Volume 4 (2002)
392 T. Ohtsuki (Editor)
Remark (A. Stoimenow) It is true for K up to 11 crossings. degmPWK (l;m )
is independent on the twist of WK if it is > 2 by a simple skein argument.
Update Gruber [157] showed that, if K is a prime alternating knot and WK
is its untwisted Whitehead double, then degmPWK (l;m ) 2d e gz FK (a;z )+2.
Problem 1.16 (E. Ferrand, A. Stoimenow) Is for any alternating link L,
(L) min degl
(
PL(l;m )

 min dega
(
FL(a−1;z )

?
Remark (A. Stoimenow) The second inequality is conjectured by Ferrand
[125] (see also comment on Problem 1.18), and related to estimates of the Ben-
nequin numbers of Legendrian knots. As for the 
rst inequality, by Cromwell
[97] we have min degl
(
PL(l;m )

 1−(L) and classically (L) 1−(L).
Problem 1.17 (A. Stoimenow) Ifrk is the coecient of zk in the Conway
polynomial and c(L) is the crossing number of a link L,i st h e n

rk(L)

 c(L)k
2kk! ?
Remark (A. Stoimenow) The inequality is non-trivial only for L of k+1;k−
1;::: components. It is also trivial for k = 0, easy for k =1( r1 is just the
linking number of 2 component links) and proved by Polyak-Viro [331] forknots
and k = 2. There are constants Ck with

rk(L)

Ckc(L)k ;
following from the proof (due to [27, 370] for knots, due to [375] for links) of
the Lin-Wang conjecture [263] for links, but determining Ck from the proof is
dicult. Can the inequality be proved by Kontsevich-Drinfel’d, say at least
for knots, using the description of the weight systems of r of Bar-Natan and
Garoufalidis [34]? More speci
cally, one can ask whether the (2 ;n )-torus links
(with parallel orientation) attain the maximal values of rk .O n e c a n a l s o a s k
about the shape ofCk for other families of Vassiliev invariants, likedk
dtkVL(t)

t=1 .
Problem 1.18 (A. Stoimenow) Does min dega
(
FL(a−1;z )

 1−(L) hold
for any link L?I f u(K) is the unknotting number of a knot K ,d o e s
min dega
(
FK (a−1;z )

 2u(K) hold for any knot K ?
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 393
Remark (A. Stoimenow) For the common lower bound of 2 u and 1− for
knots, 2gs , there is a 15 crossing knot K with 2gs(K)< min dega
(
FK (a−1;z )

.
Morton [285] conjectured long ago that 1 −(L) min degl
(
PL(l;m )

.T h e r e
are recent counterexamples, but only of 19 to 21 crossings. Ferrand [125] ob-
served that very often min degl
(
PK (l;m )

 min dega
(
FK (a−1;z )

(he conjec-
tures it in particular always to hold for alternating K ), so replacing
‘mindega
(
F(a−1;z )

’f o r‘ m i n d e gl
(
PK (l;m )

’ enhances the diculty of Mor-
ton’s problem (the counterexamples are no longer such).
