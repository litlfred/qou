---
doc_id: arxiv-1010.5321v3
doc_title: "Formulas on hyperbolic volume ∗ ´A.G.Horv´ ath Department of Geometry"
section_id: sec-014-333-the-case-of-dimension-n
section_title: "The case of dimension n"
section_number: 3.3.3
pages: 13-14
source_pdf: 1010.5321v3.pdf
source_sha256: c6bb20926b1f291f
doc_brief: "Formulas on hyperbolic volume ∗ Á.G.Horváth Department of Geometry — This paper collects some important formulas on hyperbolic volume."
---
The following lemma plays an important role in the n-dimensional case.
Lemma 1 We have two k-dimensional aﬃne subspaces Hk and H ′
k, respectively for which they
intersection have dimension k − 1. Assume that the points P ∈Hk, P ′ ∈H ′
k and P ′′ ∈Hk ∩H ′
k
hold the relations PP ′⊥H ′
k and P ′P ′′⊥Hk ∩H ′
k, respectively. Then the angle
α = tan −1 tanh(PP ′)
sinhP ′P ′′ ,
is independent from the position of P in Hk.
13
Proof: LetP andQ be two arbitrary points of Hk. Then by the theorem of three perpendiculars
we also have that PP ′′⊥Hk ∩H ′
k and Q′Q′′⊥Hk ∩H ′
k implying that P ′′Q′′ orthogonal to the
lines PP ′,P ′P ′′,QQ ′ and Q′Q′′, respectively. Thus the angles PP ′P ′′∠, QQ′Q′′∠ are equals.
This immediately implies the statement. □
Let now our orthosceme is the convex hull of the vertices 0 = A0,A 1,...,A n situated
into a hyperbolic orthogonal coordinate system as we did it i n the three dimensional case.
More precisely, the coordinates of the vertices are (0 ,..., 0)T , (0,..., 0,a n)T , (a1, 0,..., 0,a n)T ,
(a1,a 2, 0..., 0,a n)T ... (a1,a 2,...,a n)T , respectively. Introduce the function giving the up-
per boundary of the successive integrals. These are φ 0 = an, φ 1 : xn ↦→x1 for a point
(x1, 0,..., 0,x n)T of the edge conv ( OA2),φ 2 : (xn,x 1) ↦→x2 on the points (x1,x 2, 0...,x n)T of
the triangle conv ( OA2A3). In general φk : (x1,...,x k−1, 0,..., 0,x n) ↦→xk if the correspond-
ing point ( x1,x 2...x k−1,x k, 0,..., 0,x n)T is on the k − 1-face conv ( OA2A3 · · ·Ak+1) and so
on... From Lemma 1 we get that
tanhφk+1(xn,x 1,...,x k)
sinhxk
= tanhak+1
sinhak
,
implying that
φk+1(xn,x 1,...,x k) = tan −1
(tanhak+1
sinhak
sinhxk
)
.
In the case of k = 1, the volume can be determined by the following n-times integral: v(O) =
an∫
0
tan−1
( tanh a1
sinh an sinhxn
)
∫
0
· · ·
tan−1
( tanh an−1
sinh an−2
sinhxn−1
)
∫
0
(coshn−1xn−1)(coshn−2xn−2) · · · (coshx1)dxn−1 · · ·dx1dxn.
