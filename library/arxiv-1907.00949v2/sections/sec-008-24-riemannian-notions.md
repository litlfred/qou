---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-008-24-riemannian-notions
section_title: "Riemannian notions"
section_number: 2.4
pages: 7-7
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
state the famous Hopf–Rinow theorem [13, Theorem 1 .8] and recall the deﬁnitions of Riemannian
gradient and Hessian [20, 22, 8] below for easy reference.
Theorem 2.7 (Hopf–Rinow). Let (M,g ) be a connected Riemannian manifold. Then the following
statements are equivalent:
(i) closed and bounded subsets of M are compact;
(ii) M is a complete metric space;
(iii) M is geodesically complete, i.e., the exponential map expx :TxM→M is deﬁned on the whole
TxM for all x∈M.
Furthermore, any one of these conditions guarantees that any two pointsx,y onM can be connected
by a distance minimizing geodesic on M.
In the following we will write X(M) for the set of all smooth vector ﬁelds on M.
Deﬁnition 2.8 (Riemannian gradient and Hessian) . Let (M,g ) be a Riemannian manifold. Let
f :M→ R be a smooth function. The Riemannian gradient of f, denoted∇f, is deﬁned by
g(∇f,V ) =V (f),
for any V ∈ X(M). The Riemannian Hessian of f, denoted∇2f, is deﬁned by
(∇2f)(U,V ) =g
(
∇U(∇f),V
)
,
whereU,V ∈ X(M) and∇UV is the covariant derivative ofV alongU, which is uniquely determined
by the Riemannian metric g.
By their deﬁnitions,∇f is a smooth vector ﬁeld and∇2f is a smooth ﬁeld of symmetric bilinear
forms. In particular, ∇2f is uniquely determined by its values at points of the form ( V,V ) over all
V ∈ X(M) because of bilinearity and symmetry, i.e.,
∇2f(U,V ) = 1
2
(
∇2f(U +V,U +V )−∇ 2f(U,U )−∇ 2f(V,V )
)
, (4)
for any U,V ∈ X(M). Deﬁnition 2.8 is standard but not as useful for us as a pointwise deﬁnition
— the Riemannian gradient∇f(x) and Riemannian Hessian ∇2f(x) at a point x∈M is given by
gx(∇f(x),X ) = df
(
exp(tX)
)
dt
⏐⏐⏐
t=0
, ∇2f(x)(X,X ) = d2f
(
exp(tX)
)
dt2
⏐⏐⏐
t=0
, (5)
where exp(tX) is the geodesic curve emanating from x in the direction X∈TxM. We may obtain
(5) by Taylor expanding f
(
exp(tX)
)
.
Given a speciﬁc functionf, one may express (5) in terms of local coordinates onM but in general
there are no global formulas for ∇f(x) and∇2f(x), and without which it would be diﬃcult if not
impossible to do optimization on M. We will see in Section 6 that when M is a ﬂag manifold, then
(5) may be expressed globally in terms of extrinsic coordinates.
