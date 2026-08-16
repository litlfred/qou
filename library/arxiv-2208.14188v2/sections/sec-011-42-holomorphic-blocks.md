---
doc_id: arxiv-2208.14188v2
doc_title: "Prepared for submission to JHEP KIAS-P22064 Resurgence in complex Chern-Simons theory at generic levels Zhihao Duana Jie Gub aKorea Institute for Advanced Study 85 Hoegiro, Dongdae"
section_id: sec-011-42-holomorphic-blocks
section_title: "Holomorphic blocks"
section_number: 4.2
pages: 30-32
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels Zhihao Duana Jie Gub aKorea Institute for Advanced Study 85 Hoegiro, Dongdaemun-gu, Seoul 02455, Korea bSchool of Phyiscs and Shing-Tung Yau"
---
As in the example of knot 41, here we introduce descendants of the state integral and
demonstrate their property of factorisation into holomorphic blocks.
The descendant state integral for the knot 52 takes the form,
χ(k)
52;r,s(µ,n ; b) =(ηk)3
k
∑
m∈Zk
∫
C
dσZ(k)
b [∆](σ,m )Z(k)
b [∆](σ +µ,m +n)Z(k)
b [∆](σ−µ,m−n)
× (−1)ne
πi
k (−(σ+µ−cb)2−(σ−µ−cb)2−µ2+(m+n)2+(m−n)2+n2)
×e
2πi
k (−i(rb+sb−1)(cb−σ)+(r−s)m), (4.22)
where the contour of integral C is such that it asymptotes at both ±∞ to the horizontal
line Imσ =σ0 withσ0< Im(cb)−| Re(rb +sb−1)| but is deformed near the origin so that
all the poles of the integrand are below the contour.
– 29 –
The integrand only has poles coming from the tetrahedron partition functions and they
are located at
v =−ibα− ib−1β, α −β≡m (modk), (4.23)
v =µ− ibα− ib−1β, α −β≡m−n (modk), (4.24)
v =−µ− ibα− ib−1β, α −β≡m +n (modk). (4.25)
We can evaluate the descendant state integral by completing the contour from below and
summing up residues from all these poles. We ﬁnd in this way that
χ(k)
52;r,s(µ,n ; b) =(−1)nqr/2˜q−s/2
(
e−πi
12 + 5πi
6k + 5πi
12k (τ+τ−1)Ar(x;q)As(˜x, ˜q−1)
+ e− 5
12πik+πi
6k + πi
12k (τ+τ−1)Br(x;q)Bs(˜x, ˜q−1)
+ e− 5
12πik+πi
6k + πi
12k (τ+τ−1)Cr(x;q)Cs(˜x, ˜q−1)
)
. (4.26)
Here Ar(x,q ),Br(x,q ),Cr(x,q ) are descendant holomorphic blocks deﬁned by
Ar(x;q) =H(x,x−1,qr;q), (4.27a)
Br(x;q) =θ(−q1/2x;q)−2xrH(x,x 2,qrx2;q), (4.27b)
Cr(x;q) =θ(−q−1/2x;q)−2x−rH(x−1,x−2,qrx−2;q), (4.27c)
where H(x,y,z ;qε) for|q|< 1 and ϵ =±1 and
H+(x,y,z ;q) =(qx;q)∞(qy;q)∞
∞∑
n=0
qn(n+1)zn
(q;q)n(qx;q)n(qy;q)n
(4.28a)
H−(x,y,z ;q) = 1
(x;q)∞(y;q)∞
∞∑
n=0
(−1)n q
1
2n(n+1)x−ny−nzn
(q;q)n(qx−1;q)n(qy−1;q)n
. (4.28b)
Note again that the deﬁnition of descendant holomorphic blocks as functions of x,q are
independent of k. They thus enjoy the same properties as discussed in [31]. If we deﬁne
the descendant Wronskian matrix
Wr(x;q) =


Ar(x;q) Br(x;q) Cr(x;q)
Ar+1(x;q) Br+1(x;q) Cr+1(x;q)
Ar+2(x;q) Br+2(x;q) Cr+2(x;q)

, (4.29)
it enjoys the identity
Wm(x−1;q) =Wm(x;q)


1 0 0
0 0 1
0 1 0

, (4.30)
as well as the inversion property
Wm(x;q)W𝓁(x;q−1)T∈PSL (3, Z[x±1,q±1]). (4.31)
In particular
W−1(x;q)W−1(x;q−1)T =


1 0 0
0 0 1
0 1 x +x−1

. (4.32)
– 30 –
III
IVIII
Figure 5: Singular points of the Borel transform of the vector of trans-series of thesl(2, C)
Chern-Simons theory at level k = 1 on the complement of the knot 52.
