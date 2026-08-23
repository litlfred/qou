---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-011-5-application-to-two-dimensional-quantum-hyperbo
section_title: "Application to two-dimensional quantum hyperbolic geometry"
section_number: 5
pages: 12-14
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
It is known that the Racah-Wigner symbols of the modular double play an important role when
the quantum Teichm¨ uller theory [Fo97, Ka98, CF99] is studi ed in the length representation
[T03, T05]. Having ﬁxed a particular normalization in our deﬁnition of the b-6j symbols above
naturally leads to question what it corresponds to in this context. We are going to show that the
deﬁnition of the b-6j symbols corresponds to the quantization of a particular choice of Darboux-
coordinates for the classical Teichm¨ uller spaces. The Teichm¨ uller spacesT (C) are well-known
to be related to a connected component in the moduli space of ﬂ at SL(2, R)-connections on
Riemann surfaces. Natural Darboux coordinates for this spa ce have recently been discussed in
[NRS].
The quantization of the Teichm¨ uller spaces will be discussed in terms of the Darboux coor-
dinates of [NRS] in a self-contained manner in [TeVa]. In the following we will collect some
relevant observations that can fairly easily be extracted from the existing literature.
13
5.1 Classical Teichm ¨uller theory of the four-holed sphere
To be speciﬁc, let us restrict attention to four-holed spher esC0,4. The holes are assumed to be
represented by geodesics with lengths L = (l1,...,l 4). There are three simple closed curves
γs, γt, and γu encircling pairs of points (z1,z 2), (z2,z 3) and (z1,z 3), respectively. A set of
useful coordinate functions are deﬁned in terms of the hyper bolic cosines Lσ = 2 cosh lσ
2 ,
σ ∈ {s,t,u }, of the geodesic length functionslσ on T0,4 ≡ T (C0,4). lσ is deﬁned as the length
of the geodesicγσ, deﬁned by means of the constant negative curvature metric onC0,4.
The well-known relations between Teichm¨ uller spacesT (C) and the moduli spaces MG(C)
of ﬂatG =SL(2, R)-connections on Riemann surfaces imply that the geodesic length functions
Lσ are related to the holonomies gσ along γσ as Lσ = −Tr(gσ). This allows us to use the
description given in [NRS], which may be brieﬂy summarized a s follows. The structure of
MG(C0,4) as an algebraic variety is expressed by the fact that the thre e coordinate functions
Ls, Lt and Lu satisfy one algebraic relation of the form PL(Ls,L t,L t) = 0 . The Poisson
bracket {Lσ1,L σ2} deﬁned by the Weil-Petersson symplectic form is also algebraic in the length
variablesLσ, and can be written elegantly in the form
{Ls,L t } = ∂
∂Lu
PL(Ls,L t,L t). (5.1)
As shown in [NRS] one may representLs,Lt andLu in terms of Darboux-coordinatesls andks
which have Poisson bracket {ls,k s} = 2. The expressions forLs andLt are, in particular,
Ls = 2 cosh(ls/2), (5.2)
Lt(L2
s − 4) = 2( L2L3 +L1L4) +Ls(L1L3 +L2L4) + 2 cosh(ks)
√
c12(Ls)c34(Ls),
whereLi = 2 cosh li
2 , andcij(Ls) is deﬁned as
cij(Ls) = L2
s +L2
i +L2
j +LsLiLj − 4 (5.3)
= 2 cosh ls+li+lj
4 2 cosh ls+li−lj
4 2 cosh ls−li+lj
4 2 cosh ls−li−lj
4 .
Together with a similar formula forLu, these expressions ensure that both the algebraic relation
PL(Ls,L t,L t) = 0 and the Poisson structure (5.1) are satisﬁed. These Darboux coordinates are
identical to the Fenchel-Nielsen length-twist coordinates well-known in hyperbolic geometry.2
Similar Darboux coordinates (lt,k t) and (lu,k u) can be associated to the curves γt and γu,
respectively. The change of coordinates between the Darboux-coordinates (ls,k s) and (lt,k t) is
represented by a generating function S st
L (ls,l t) such that
∂
∂ls
S st
L (ls,l t) = −ks, ∂
∂lt
S st
L (ls,l t) = kt. (5.4)
2This can be inferred from [ALPS]. We thank T. Dimofte for pointing this reference out to us
14
Other natural sets of Darboux-coordinates (lσ,k ′
σ) can be obtained by means of canonical
transformationsk′
σ = kσ +f (lσ). By a suitable choice of f (σ), one gets Darboux coordinates
(ls,k ′
s) in which the expression forLt in (5.2) is replaced by
Lt(L2
s − 4) = 2( L2L3 +L1L4) +Ls(L1L3 +L2L4) (5.5)
+ 2 cosh ls+l1−l2
4 2 cosh ls+l2−l1
4 2 cosh ls+l3−l4
4 2 cosh ls+l4−l3
4 e+k′
s
+ 2 cosh ls+l1+l2
4 2 cosh ls−l1−l2
4 2 cosh ls+l3+l4
4 2 cosh ls−l3−l4
4 e−k′
s.
The Darboux coordinates (ls,k ′
s) are equally good to represent the Poisson structure of
MG(C0,4), but they have the advantage that the expressions forLσ do not contain square-roots.
This will later turn out to be important.
