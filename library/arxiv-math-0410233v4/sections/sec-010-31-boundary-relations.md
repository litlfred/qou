---
doc_id: arxiv-math-0410233v4
doc_title: "Cusp shapes under cone deformation"
section_id: sec-010-31-boundary-relations
section_title: "Boundary relations"
section_number: 3.1
pages: 11-15
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "Cusp shapes under cone deformation — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
We will let U be a horoball neighborhood of the one cusp, and V1, . . . , Vn
be tubular neighborhoods of the components of the singular l ocus Σ, each
with radius R. Here, we are letting n be the total number of components
of Σ. We will assume throughout that these neighborhoods are chosen such
that all intersections of distinct neighborhoods are trivi al.
Let ω ∈ H 1(X; E) correspond to a harmonic inﬁnitesimal deformation
of hyperbolic structure at time t, and decompose ω in tubular neighbor-
hoods and horoball neighborhoods as in the previous section , and consider
boundary terms.
By equation (12), we see immediately that
(13) − bU (η0, η0) ≤
n∑
j=1
bj.
Again, note that η0 in the term bU (η0, η0) refers to the decomposition of η
valid only in the horoball neighborhood U . Also, recall that the terms of
equation (13) all depend on time t, but we are suppressing t for notational
purposes.
Now, we will analyze the left hand side of (13). Recall that in a horoball
neighborhood of a cusp, ω0 can be written as a complex multiple of the form
ωℓ = ωℓ(∞) in equation (6). That is, there are real numbers a and b (for
ﬁxed t) such that
(14) ω0 = (a + ib)


0 0 0
0 −1 −i
0 −i 1


Lemma 3.1. Using the notation above,
−bU (η0, η0) = 2( a2 + b2)Area(∂U ).
Proof. By equation (14), we may write η0 = Re(ω0) and ∗Dη0 = Im(ω0) as:
(15) η0 =


0 0 0
0 −a b
0 b a

 =


0
−a
b

 ω2 +


0
b
a

 ω3
and:
∗Dη0 =


0 0 0
0 −b −a
0 −a b

 =


0
−b
a

 ω2 +


0
−a
b

 ω3.
Here ω1, ω2, and ω3 are forms dual to the vectors e1, e2, and e3 giving
cylindrical coordinates on U . Recall in particular that e1 is radial, and e2 is
tangent to a meridian.
12 JESSICA S. PURCELL
We then may compute −bU (η0, η0) explicitly in terms of the constants a
and b.
−bU (η0, η0) =
∫
∂U
η0 ∧ ∗Dη0 =
∫
∂U
2(a2 + b2)ω2 ∧ ω3.
Since ω2 ∧ ω3 is the area form for the torus ∂U , we have:
−bU (η0, η0) = 2( a2 + b2)Area(∂U ).
□
Notice that equation (13) and Lemma 3.1 imply:
(16) 0 ≤
∑
j
bj,
and that we have equality by equation (11) if and only if η is trivial on
X − V , which happens only when the deformation is trivial.
3.2. T eichm¨ uller Space.We now turn our attention to the term ( a2 + b2)
in Lemma 3.1. This term is closely related to the change in met ric of the
torus ∂U .
Under the hyperbolic metric on X = M − Σ, the boundary ∂U inherits
a Euclidean structure. This gives a point in the Teichm¨ ulle r space of the
torus, T (T 2).
Remark. We view T (T 2) as the space of ﬂat structures on the torus. To
each ﬂat structure ζ is associated a unit area Euclidean metric gζ, and vice
versa. However, in the following discussion we will refer to both the ﬂat
structure and its associated metric, and so we will continue to distinguish
between the two. We use Greek letters γ, ζ to denote points in T (T 2), and
g with appropriate subscripts to denote the induced metric on the torus.
As the metric on X changes under the cone deformation, the point in
T (T 2) will also change, tracing out a smooth path γ(t), with tangent vector
γ′(t). The tangent vector γ′(t) is an inﬁnitesimal change of the ﬂat structure
on the torus. Our 1–form ω encodes the inﬁnitesimal deformation of the
hyperbolic cone structure Xt on X = M − Σ. So we may relate γ′(t) to ω,
or more particularly, to a2 + b2. We will do so using the Teichm¨ uller metric
on T (T 2).
Deﬁnitions of the Teichm¨ uller distance vary by constant fa ctors in the
literature. We will use the convention that the Teichm¨ uller distance between
two points, σ and τ in T (T 2), is deﬁned to be
d(σ, τ) = 1
2 inf
f
log Kf ,
where f : σ → τ is a Kf –quasiconformal map, with Kf the smallest such
constant. (See for example [17].)
CUSP SHAPES UNDER CONE DEFORMATION 13
Lemma 3.2. Let γ(t) denote the path of ∂U through T (T 2). Let γ′(t) denote
its tangent vector. Then
√
a2 + b2 =
‖
‖γ′(t)
‖
‖ ,
where the metric is the Teichm¨ uller metric.
Proof. Fix t = t0, and consider the ﬂat structure on the torus given by
∂Ut0 = γ(t0). We may assume it has unit area. Recall that any Teichm¨ ulle r
geodesic through γ(t0) is given as follows. Select two orthogonal geodesic
foliations F1 and F2 on the torus. Select λ > 0. For any u ∈ R, obtain a new
metric by multiplying vectors along F1 by exp(−λ u) and multiplying vectors
along F2 by exp(λ u). This is a “stretch–squeeze” map, which preserves the
area of the torus. It gives a one–parameter family of ﬂat stru ctures on the
torus, which we denote by ζ(u).
Teichm¨ uller’s theorem says that in the case of the torus, th is stretch–
squeeze map has the minimal quasiconformal distortion, so i s a Teichm¨ uller
geodesic. For each u, the derivative of the map ζ(u) takes an inﬁnitesimal
circle to an inﬁnitesimal ellipse, the ratio of whose axes is exp(2uλ). Thus
for any u, the distance between the structure ζ(0) = γ(t0) at time 0 and
ζ(u) at time u is
d(ζ(0), ζ(u)) = 1
2 inf
f
log Kf = 1
2 log(e2uλ) = λ u.
Therefore, λ = ‖ζ ′(u)‖, where the norm is given with respect to the Te-
ichm¨ uller metric. In particular, λ = ‖ζ ′(0)‖.
On the other hand, for any point on the torus, let u1 and u2 be orthonor-
mal vectors in the directions of F1 and F2 respectively. Then when we write
the inﬁnitesimal change of metric induced by ζ ′(0) in coordinates given by
u1 and u2, we obtain at every point a diagonal matrix Λ with −λ, λ on the
diagonal, since at each time u those vectors are just multiplied by e−λ u,
eλ u, respectively. Thus if we let gu be the metric on the torus induced by
ζ(u), we have
d
du
⏐
⏐
⏐
⏐
u=0
gu(x, y) = 2 g0(Λ x, y).
Now we relate this discussion to the term a2 + b2.
Recall the inﬁnitesimal deformation of the hyperbolic cone structure of
X is encoded by the one–form ω. In particular, the inﬁnitesimal change in
metric is given by the real part η. That is, if we let gt be the metric on X
at time t, then
(17) d
dt
⏐
⏐
⏐
⏐
t0
gt(x, y) = 2 gt0 (η(t0)x, y).
(See the displayed equation on page 374 of [14].)
We are interested in the inﬁnitesimal change in the metric on ∂Ut0 . Since
η decomposes into η0 + ηc, and only η0 changes the holonomy of ∂U , we
know the inﬁnitesimal change in metric on ∂Ut0 is given by η0.
14 JESSICA S. PURCELL
We have an explicit formula for η0, written in orthonormal coordinates
with respect to the metric gt0 , given by e1, e2, e3, where e1 is radial and
e2 points in the direction of the meridian. Consider again equa tion (15).
Since the ﬁrst row and column for the matrix of η0 are zero, we see that
η0 actually has no eﬀect on or contribution to the change of metri c in the
radial direction of U . Hence η0 itself gives the inﬁnitesimal change of metric
on the torus ∂Ut0, or γ′(t0) = η0(t0).
When we write η0 in orthonormal coordinates e2, e3 on the torus, we
discard the ﬁrst row and column of the matrix of equation (15) , and obtain
the 2 × 2 matrix
(18) A =
[
−a b
b a
]
.
Here the ﬁrst column of A gives the inﬁnitesimal change in the meridional
direction, the second the change in the direction orthogona l to the meridian.
That is, if we restrict the metric gt to ∂Ut, we may rewrite equation (17) as
d
dt
⏐
⏐
⏐
⏐
t=t0
gt(x, y) = 2 gt0 (η0(t0) x, y) = 2 ⟨Ax, y⟩.
Hence A is a matrix representation of γ′(t0), the inﬁnitesimal change of
metric of the torus ∂Ut0.
We can diagonalize A. For any point on the torus, there exist orthonormal
vectors u1 and u2 such that when we put A into coordinates given by u1 and
u2, A is diagonal with −
√
a2 + b2 and
√
a2 + b2 on the diagonal. Moreover,
since A does not depend on the point on the torus (that is, for any poin t on
the torus we obtain the same matrix A), u1 and u2 determine orthogonal
geodesic foliations F1 and F2. These, in turn, determine a Teichm¨ uller
geodesic ζ(u) with ζ(0) = γ(t0), whose initial tangent vector ζ ′(0) agrees
with A at every point, and has Teichm¨ uller norm ‖ζ ′(0‖ =
√
a2 + b2. Thus
inﬁnitesimally, γ(t) and ζ(u) agree near t = t0 and u = 0, respectively.
Hence ‖γ′(t0)‖ = ‖ζ ′(0)‖ =
√
a2 + b2. □
Remark. In the proof of Lemma 3.2, we showed that for any time t, γ(t)
agrees inﬁnitesimally with an explicit Teichm¨ uller geode sic which is com-
pletely determined by the matrix A. We will use this again below.
Finally, putting Lemmas 3.1, and 3.2 together with equation (13), we
have completed the proof of the following theorem.
Theorem 3.3. Let Xt be a hyperbolic cone deformation with a cusp. That
is, for each time t, the hyperbolic cone manifold Xt has a cusp which remains
a cusp throughout the deformation. Let Ut be a horoball neighborhood of the
cusp. Let γ(t) denote the path ∂Ut travels through the Teichm¨ uller space of
the torus. Then the change in ∂Ut is bounded by the following inequality.
2 ‖γ′(t)‖2Area(∂Ut) ≤
∑
bj(t)
CUSP SHAPES UNDER CONE DEFORMATION 15
The sum on the right hand side is over all components of the sing ular locus.
Note Theorem 3.3 gives an inequality identical to that of The orem 1.2,
except for the boundary terms bj on the right hand side. We will bound
these, and complete the proof of Theorem 1.2, in Section 4. Fi rst, we set up
a similar theorem to Theorem 1.3.
