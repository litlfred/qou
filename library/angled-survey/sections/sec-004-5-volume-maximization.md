---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-004-5-volume-maximization
section_title: "Volume maximization"
section_number: 5
pages: 16-19
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
toc_source: inferred
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifold M with"
---
In this section, we show how volume considerations give a way to turn an angle
structure into a genuine hyperbolic metric on M. To compute the volume of an
ideal hyperbolic tetrahedron, recall the Lobachevsky function L : R →R.
Its
deﬁnition is
(5.1)
L(x) = −
 x
0
log |2 sin t| dt.
Lemma 5.1. The Lobachevsky function L(x) is well deﬁned and continuous
on R (even though the deﬁning integral is improper), and periodic with period π.
Furthermore, if T is a hyperbolic ideal tetrahedron with dihedral angles α, β, γ, its
volume satisﬁes
vol(T) = L(α) + L(β) + L(γ).
Proof. See, for example, Milnor [19].
□
Following Lemma 5.1, we may deﬁne the volume of an angle structure in a
natural way.
Definition 5.2. Let τ be an ideal triangulation of M, containing n tetrahedra.
Let A(τ) ⊂R3n be the polytope of angle structures on M. Then we deﬁne a volume
functional V : A(τ) →R, by assigning to a point p = (p1, . . . , p3n) the real number
V(p) = L(p1) + . . . + L(p3n).
By Lemma 5.1, V(p) is equal to the sum of the volumes of the hyperbolic tetrahedra
associated to the angle structure p.
174
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES
17
Lemma 5.3. Let p = (p1, . . . , p3n) ∈A(τ) be an angle structure on τ, and let
w = (w1, . . . , w3n) ∈TpA(τ) be a nonzero tangent vector at p. Then the ﬁrst two
derivatives of V(p) satisfy
∂V
∂w =
3n

i=1
−wi log sin pi
and
∂2V
∂w2 < 0.
In particular, V is strictly concave down on A(τ).
Proof. Since the deﬁnition of V is linear over the tetrahedra in τ, it suﬃces
to consider the volume of one tetrahedron. Thus, suppose that a tetrahedron T
has angles p1, p2, p3 > 0, which are changing at rates w1, w2, w3. Note that, since
the tangent vector w must preserve the angle sum in each tetrahedron, we have
w1 + w2 + w3 = 0. We may also assume that at least one (hence, at least two) of
the wi are nonzero. Then, by equation (5.1) and Lemma 5.1,
∂vol(T)
∂w
=
3

i=1
−wi log |2 sin pi| =
3

i=1
−wi log sin pi,
because all sines are positive and  wi log 2 = 0. This completes the computation
of the ﬁrst derivative.
To compute the second derivative, assume by symmetry that p1, p2 < π/2.
Diﬀerentiating vol(T) a second time, we get
−∂2vol(T)
∂w2
=
w2
1 cot p1 + w2
2 cot p2 + w2
3 cot p3
=
w2
1 cot p1 + w2
2 cot p2 + (w1 + w2)2 1 −cot p1 cot p2
cot p1 + cot p2
=
(w1 + w2)2 + (w1 cot p1 −w2 cot p2)2
cot p1 + cot p2
≥
0.
In fact, the numerator in the next-to-last line must be strictly positive. For the
numerator to be 0, we must have w1 = −w2, hence cot p1 = −cot p2, which is im-
possible when p1, p2 ∈(0, π/2). Thus ∂2vol(T)/∂w2 < 0, and the volume functional
V is also strictly concave down.
□
By Lemma 5.3, the only potential critical point of V is a global maximum. As
the next proposition shows, derivatives of V are closely connected to the holonomy
of curves on ∂M.
Proposition 5.4. Let C be a cusp torus of M, with a tessellation by boundary
triangles coming from τ. Let σ ⊂C be an oriented normal closed curve. Recall the
holonomy H(σ) from Deﬁnition 2.3 and the tangent vector w(σ) ∈TpA(τ) from
Deﬁnition 4.1.
Then for every point p ∈A(τ), we have
∂V
∂w(σ) = Re(H(σ)).
Proof. Let σ1, . . . , σk be the segments of σ, with σi contained in boundary
triangle Δi. For each i, label the angles of Δi as αi, βi, γi, in clockwise order, such
175
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
18
DAVID FUTER AND FRANC¸ OIS GU´ERITAUD
that αi is the angle cut oﬀby σi. Recall that, in Deﬁnition 2.3, we deﬁned
ϵi =

1,
if αi is to the left of σi,
−1,
if αi is to the right of σi.
Comparing this with Deﬁnition 4.1 and Figure 3, we see that the vector w(σi)
increases angle βi at rate ϵi, and increases γi at rate −ϵi. By Lemma 5.3,
∂V
∂w(σ)
=
k

i=1
∂V
∂w(σi)
=
k

i=1
(−ϵi log sin βi + ϵi log sin γi)
=
k

i=1
ϵi log
sin γi
sin βi

=
k

i=1
ϵi log |zi|
by equation (3.1)
=
Re
k

i=1
ϵi log zi,
as desired.
□
Recall, from Section 3, that an angle structure on τ corresponds to solving the
imaginary part of the edge gluing equations. By Proposition 5.4, solving the real
part of each edge equation amounts to having vanishing derivative in the direction
of the corresponding deformation. This turns out to be the crucial step in the proof
of Theorem 1.2.
Theorem 1.2. Let M be an orientable 3–manifold with boundary consisting of
tori, and let τ be an ideal triangulation of M. Then a point p ∈A(τ) corresponds
to a complete hyperbolic metric on the interior of M if and only if p is a critical
point of the functional V : A(τ) →R.
Proof. For one direction of the theorem, suppose that p ∈A(τ) is a critical
point of V. This angle structure deﬁnes a shape parameter on each tetrahedron
of τ. By Proposition 2.5, proving that these shape parameters give a complete
hyperbolic metric on M amounts to checking the edge and completeness equations
of Deﬁnition 2.4.
First, consider the edge equation about an edge e. Note that the imaginary part
of the gluing equation about edge e is automatically satisﬁed for any angle structure.
To check the real part of the gluing equation, let σ ⊂∂M be a normal closed curve
encircling one endpoint of e. Since p is a critical point of V, Proposition 5.4 implies
that Re(H(σ)) = 0, as desired. Thus the edge gluing equations are satisﬁed.
To check completeness, let C be a boundary torus of M, and let σ1, σ2 be a pair
of simple closed normal curves that span π1(C) = H1(C). Recall that C is tiled by
boundary triangles that truncate the tips of ideal tetrahedra. The angle structure p
gives each of these triangles a Euclidean shape, well-deﬁned up to similarity. If Δ is
a triangle in which σ1 and σ2 intersect, we may place the corners of Δ at 0, 1, z ∈C,
and develop the other triangles of C from there. Note that, since the edge gluing
176
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES
19
equations are satisﬁed, the boundary triangles ﬁt together correctly around every
vertex of C.
Let d1 and d2 be the deck transformations of 	C corresponding to σ1 and σ2.
Consider the complex numbers
q = d1(0),
r = d2(0),
s = d1(r) = d2(q).
The four points 0, q, r, s form four corners of a fundamental domain for C. By the
deﬁnition of holonomy (Deﬁnition 2.3) and the solution to the edge equations,
H(σ1) = log s −q
r −0 ,
H(σ2) = log s −r
q −0 .
By Proposition 5.4, the real part of each of these holonomies is 0. Thus we have
|s −q| = |r| and |s −r| = |q|, hence the fundamental domain of C is a parallelo-
gram. Therefore, H(σ1) = H(σ2) = 0, and the completeness equations are satisﬁed
for cusp C.
For the converse implication of the theorem, suppose that p ∈A(τ) deﬁnes a
complete metric. Then the tetrahedron shapes corresponding to p must satisfy all
the edge and completeness equations of Deﬁnition 2.4: we must have H(σ) = 2πi
for every closed curve σ encircling an endpoint of an edge, and H(σj) = 0 for
a collection of simple closed curves σ1, . . . , σ2k that form a basis of H1(∂M). In
particular, the real part of each of these holonomies is 0.
But, by Proposition
4.6, the leading–trailing deformations that correspond to these closed curves span
TpA(τ). Thus p is a critical point of V, as desired.
□
