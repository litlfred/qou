---
doc_id: arxiv-2208.14188v2
doc_title: "Prepared for submission to JHEP KIAS-P22064 Resurgence in complex Chern-Simons theory at generic levels Zhihao Duana Jie Gub aKorea Institute for Advanced Study 85 Hoegiro, Dongdae"
section_id: sec-007-32-holomorphic-blocks
section_title: "Holomorphic blocks"
section_number: 3.2
pages: 19-21
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels Zhihao Duana Jie Gub aKorea Institute for Advanced Study 85 Hoegiro, Dongdaemun-gu, Seoul 02455, Korea bSchool of Phyiscs and Shing-Tung Yau"
---
One happy fact of state integral model of knot 41 at level 1 is that when Im b⁄= 0, it can
be evaluated by summing over residues and it factorises to products of q- and ˜q-series [52],
i.e., the holomorphic blocks [51]. In addition, variants known as the descendants of the
state integral can be written, which also enjoys factorisation. This fact turns out to be very
useful in the resurgence analysis, as the Stokes matrices can be written in terms of them
[31, 32]. We ﬁnd here at generic level k, we can also write down descendants of the state
integral and they also factorise to holomorphic blocks. In fact, the holomorphic blocks
are independent of k (only implicitly through x, ˜x,q, ˜q, cf. [15]), while the factorisation
formulas are not.
We introduce the following descendant state integral for knot 41
χ(k)
41;r,s(µ,n ;τ) = ηk
k
∑
m∈Zk
∫
C
dσZ(k)
b [∆](σ−µ,m−n)Z(k)
b [∆](σ,m )
× (−1)me
πi
k ((σ−cb)2−2(µ−σ+cb)2−m2+2(n−m)2)
×e
2πi
k (−i(rb+sb−1)(cb−σ)+(r−s)m). (3.22)
The motivation for the particular form of the descendant state integral is that both the
tetrahedron partition functionZ(k)
b [∆](σ,m ) and the extra factor colored in blue
f(σ,m ) = exp
(2π
k (rb +sb−1)(cb−σ) + 2πi
k (r−s)m
)
(3.23)
in the integrand enjoys nice quasi-periodicity property under the shift
(σ,m )→ (σ− ib±1,m± 1), (σ,m )→ (σ + ib±1,m∓ 1). (3.24)
The former is given in (A.8), and the latter is simply
f(σ∓ ib,m± 1) =f(σ,m )q±r, (3.25a)
f(σ± ib−1,m± 1) =f(σ,m )˜q±s. (3.25b)
– 18 –
In addition, the form of the descendant state integral may be related to insertion of a light
knot from the Chern-Simons theory point of view [53], or to turning on FI parameters from
the 3d SCFT point of view [54].
Note that compared to the state integralχ(k)
41 (µ,n ;τ) deﬁned in (3.1), here the contour
of integral C has to be modiﬁed such that it asymptotes at both ±∞ to the horizontal
line Imσ = σ0 with σ0 < Im(cb)−| Im(µ)|−| Re(rb +sb−1)| but is deformed near the
origin so that all the poles of the integrand are below the contour. The integrand only
has poles coming from the two tetrahedron partition functions Z(k)
b [∆](σ−µ,m−n) and
Z(k)
b [∆](σ,m ), and they are located respectively at
v =µ− ibα− ib−1, α −β≡m−n (modk), (3.26)
σ =−ibα− ib−1β, α −β≡m (modk). (3.27)
On the other hand, since the integrand decays exponentially fast towards inﬁnity below
the contourC, we can evaluate the descendant state integrand by completing the contour
from below and adding up residues from these poles. Then we ﬁnd in this way that
χ(k)
41;r,s(µ,n ;τ) =e−πik
4 −πi
2k−πi
4k (τ+τ−1)Ar(x,q )A−s(˜x, ˜q−1)
+ e
πik
4 +πi
2k +πi
4k (τ+τ−1)Br(x,q )B−s(˜x, ˜q−1). (3.28)
Here Ar(x,q ),Br(x,q ) are descendant holomorphic blocks deﬁned by
Ar(x,q ) =θ(−q1/2x;q)−2x2rJ(qrx2,x ;q), (3.29)
Br(x,q ) =θ(−q−1/2x;q)xrJ(qrx,x−1;q), (3.30)
where J(x,y ;qε) :=Jε(x,y ;q) for|q|< 1 and ε =± is the q-Hahn Bessel function
J+(x,y ;q) = (qy;q)∞
∞∑
n=0
(−1)n q
1
2n(n+1)xn
(q;q)n(qy;q)n
(3.31a)
J−(x,y ;q) = 1
(y;q)∞
∞∑
n=0
(−1)n q
1
2n(n+1)xny−n
(q;q)n(qy−1;q)n
. (3.31b)
Note that the deﬁnition of descendant holomorphic blocks as function of x,q are indepen-
dent ofk. They enjoy the same properties as discussed in [31]. If we deﬁne the descendant
Wronskian matrix
Wr(x;q) =
(
Ar(x;q) Br(x;q)
Ar+1(x;q) Br+1(x;q)
)
, (3.32)
it enjoys the inversion property that
Wm(x;q)
(
1 0
0−1
)
W𝓁(x;q−1)T∈GL(2, Z[q±1x±1]). (3.33)
In particular
W−1(x;q)
(
1 0
0−1
)
W−1(x;q−1)T =
(
x−2 +x−1− 1 1
1 0
)
. (3.34)
– 19 –
III
III IV
Figure 2: Singular points of the Borel transform of the vector of trans-series of thesl(2, C)
Chern-Simons theory at level k = 1 on the complement of the knot 41.
