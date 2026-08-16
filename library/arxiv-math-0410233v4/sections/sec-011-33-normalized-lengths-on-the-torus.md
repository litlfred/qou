---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMA TION JESSICA S. PURCELL"
section_id: sec-011-33-normalized-lengths-on-the-torus
section_title: "Normalized lengths on the torus"
section_number: 3.3
pages: 15-17
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION JESSICA S. PURCELL — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
how normalized lengths of curves on the torus ∂U change over the deforma-
tion.
Deﬁnition 3.4. Let β be a slope on the torus T , that is, an isotopy class
of simple closed curves. The normalized length of β is deﬁned to be:
Normalized length( β) = Length(β)
√
Area(T )
,
where Length( β) is deﬁned to be the length of a geodesic representative of
β on T .
Lemma 3.5. Let β be a slope on ∂Ut. Let Lt(β) denote its normalized
length, with derivative ˙L(β). Then Lt(β) satisﬁes:
(19) − ‖γ′(t)‖ Lt(β) ≤ ˙L(β) ≤ ‖ γ′(t)‖ Lt(β).
Proof. Fix a time t = t0. We will show the lemma for t0.
We saw in the proof of Lemma 3.2 that γ(t) agrees inﬁnitesimally with an
explicit Teichm¨ uller geodesicζ(u) determined by the matrix A of equation
(18) when t = t0 and u = 0. More speciﬁcally, ζ(u) multiplies vectors along
F1 by exp(−u
√
a2 + b2), and multiplies vectors along F2 by exp(u
√
a2 + b2),
where F1 and F2 are orthogonal geodesic foliations (determined by the ma-
trix A) on the torus ∂Ut0. Thus we will prove the lemma by showing it is
true when the change in metric on ∂Ut0 is given by ζ(u).
Now, Lt(β) is deﬁned to be the length of a geodesic representative of β
divided by
√
Area(∂Ut). Without loss of generality, we may assume that
Area(∂Ut) = 1, since γ′(t) is given by a trace free (hence area preserving)
matrix A. Thus Lt(β) is just the length of a geodesic representative of β at
time t0.
Let ˆβt0 : I → ∂Ut0 be a geodesic representative of β at time t0. Then ˆβt0
makes some angle θ with the foliation F1. For any u, ζ(u) takes ˆβt0 to a
new geodesic, still with slope β, and length Lu(β) = αu(θ) Lt0 (β). Here
αu(θ) =
√
cos2 θ exp(−2u
√
a2 + b2) + sin2 θ exp(2u
√
a2 + b2)
is maximized when θ = π/2 and minimized when θ = 0. Thus we have
exp(−
√
a2 + b2 u) Lt0 (β) ≤ Lu(β) ≤ exp(
√
a2 + b2 u) Lt0 (β).
16 JESSICA S. PURCELL
Since d
dt
⏐
⏐
t=t0
Lt(β) = d
du
⏐
⏐
u=0 Lu(β),
−
√
a2 + b2 Lt0(β) ≤ d
dt
⏐
⏐
⏐
⏐
t=t0
Lt(β) ≤
√
a2 + b2 Lt0(β).
□
Combining this with the inequality of Theorem 3.3, we obtain the follow-
ing theorem.
Theorem 3.6. Let Lt be the normalized length of a slope on a cusp torus
∂Ut under a cone deformation, with derivative ˙L = d
dt Lt. Then the change
in Lt is bounded by the following inequality:
−
( √ ∑ bi(t)
2Area(∂Ut)
)
Lt ≤ ˙L ≤
( √ ∑ bi(t)
2Area(∂Ut)
)
Lt.
Proof. Solving for ‖γ′(t)‖ in the inequality of Theorem 3.3, we ﬁnd
‖γ′(t)‖ ≤
√ ∑ bj(t)
2Area(∂Ut) .
The result is given by substituting this into equation (19). □
3.3.1. Normalized height. For our applications, the curve on the torus we
are particularly interested in is the one running orthogona l to the meridian.
When we are dealing with link complements in S3, as in a future section
of this paper, there is a well deﬁned meridian on a cusp torus. Otherwise,
choose the shortest nontrivial simple closed curve on the in itial cusp torus to
be the meridian (for our applications to knots and links in S3, these choices
will agree).
We will be interested in estimating the length of the next sho rtest non-
trivial simple closed curve. This length will be at least as l ong as the length
of the arc orthogonal to the meridian.
At time t, let pt denote the geodesic arc perpendicular to the meridian,
running from meridian to meridian on ∂Ut. This arc will generally not
be a closed curve. Let ht be the normalized length of pt, that is, ht =
Length(pt)/
√
Area(∂Ut). We refer to ht as the normalized height of the
torus at time t. Denote its derivative at time t by ˙h.
Lemma 3.7. The normalized height ht satisﬁes
−
√
a2 + b2 ht ≤ ˙h ≤
√
a2 + b2 ht.
Proof. Let µ denote the meridian slope, with Lt(µ) its normalized length at
time t. Then htLt(µ) = 1. Thus
˙h
ht
+
˙L(µ)
Lt(µ) = 0.
CUSP SHAPES UNDER CONE DEFORMATION 17
By Lemma 3.5 and Lemma 3.2,
−
√
a2 + b2 ≤
˙L(µ)
Lt(µ) ≤
√
a2 + b2.
Hence −
√
a2 + b2 ht ≤ ˙h ≤
√
a2 + b2 ht.
□
Again Lemma 3.7, combined with the inequality of Theorem 3.3 , gives
(20) −
( √ ∑ bi
2Area(∂Ut)
)
ht ≤ ˙h ≤
( √ ∑ bi
2Area(∂Ut)
)
ht
We simplify equation (20) by noting the area of Ut is given by the length
of the meridian times the actual length of the arc pt. Recall that the length
of pt is
√
Area(∂Ut) Lt(pt) =
√
Area(∂Ut)ht. So denoting the length of the
meridian of ∂Ut by mt, we have
√
Area(∂Ut) = mtht.
Putting this into equation (20), we obtain:
Theorem 3.8. Let M be a hyperbolic 3–manifold with a cusp, and let X
be a hyperbolic 3–manifold which can be joined to M by a smooth family of
hyperbolic cone manifolds. Let ht denote the normalized height at time t of
the cusp which deforms to the cusp of M , and let mt denote the length of
its meridian. Finally, denote by ˙h the derivative of ht. Then
(21) −
√ ∑ bi(t)
mt
√
2
≤ ˙h ≤
√ ∑ bi(t)
mt
√
2
