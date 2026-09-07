---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-013-7-optimization-algorithms-over-flag-manifolds
section_title: "Optimization algorithms over flag manifolds"
section_number: 7
pages: 21-23
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
With analytic expressions for points, tangent vectors, metric, geodesic, parallel transport, Rie-
mannian gradient and Hessian in place, Riemannian manifold optimization algorithms are straight-
forward to derive from the usual ones. For example, for steepest descent, instead of adding a
negative multiple of the gradient to the current iterate, we move the current iterate along the ge-
odesic with initial velocity vector given by the negative of the gradient. Again, we may do this in
any of the four coordinates system we have introduced although for the same reason in Section 6,
we prefer the Stiefel coordinates. Thus here we will assume the identiﬁcation (45) as before.
7.1. Steepest descent over a ﬂag manifold. We describe this in Algorithm 1. A point JY K∈
Flag(n1,...,n d;n) is represented in Stiefel coordinates, i.e., as an orthonormal matrix Y ∈ Rn×nd,
Y TY =I. As usual, Y⊥∈ Rn×(n−nd) is such that X := [Y,Y ⊥]∈ O(n). The Riemannian gradient
∇f ∈ Rn×nd is given by Proposition 6.1 and we set G =−∇f to be the search direction. The
exponential map direction B ∈ Rn×n is uniquely obtained from BIn,nd = [Y,Y ⊥]TG, i.e., B is
the unique skew-symmetric matrix whose ﬁrst nd columns is [Y,Y ⊥]TG. The next iterate is then
found along the geodesic determined by the current iterate and the direction as in Proposition 4.14,
although the exact line search may be substituted by any reasonable strategy for choosing step size.
Note in particular that Algorithm 1 does not involve parallel transport.
Algorithm 1 Steepest descent in Stiefel coordinates
Require: JY0K∈ Flag(n1,...,n d;n) with Y0∈ Rn×nd and Y T
0Y0 =I;
1: ﬁnd Y⊥
0 ∈ Rn×(n−nd) such that [Y0,Y ⊥
0 ]∈ O(n);
2: set X0 = [Y0,Y ⊥
0 ];
3: for i = 0, 1,... do
4: set Gi =−∇f(JYiK); ⊿ gradient at JYiK as in (47)
5: set Xi = [Yi,Y ⊥
i ];
6: compute ˆB =X T
iGi;
7: set B∈ Rn×n as Bij = ˆBij for j≤nd;
8: Bij =−ˆBji for j≥nd and i≤nd;
9: Bij = 0 otherwise;
10: minimize f
(
Xi exp(tB)In,nd
)
overt∈ R; ⊿ tmin from exact line search
11: set Xi+1 =Xi exp(tminB);
12: end for
Ensure: JYoptK = JXoptIn,ndK
22 K. YE, K. S.-W. WONG, AND L.-H. LIM
7.2. Conjugate gradient over a ﬂag manifold. We present the conjugate gradient method
in Algorithm 2. Unlike steepest descent, conjugate gradient requires that we construct our new
descent direction from the (k− 1)th and kth iterates, i.e., one needs to compare tangent vectors at
two diﬀerent points on the manifold and the only way to do this is to parallel transport the two
tangent vectors to the same point. There is no avoiding parallel transport in conjugate gradient.
As the expression for parallel transport in (30) indicates, we will need to compute
e−ϕtB(X) =
∞∑
k=1
(−1)k
k! ϕk
tB(X), ϕ tB(X) = t
2[B,X ]m.
The rapid decay of the exponential series allows us to to replace it by a ﬁnite sum, reducing the
task to recursively computing the iterated brackets and projection onto m:
ϕk
tB(X) =ϕtB◦···◦ ϕtB(X) =
(t
2
)k
[B, [B,..., [B,X ]m... ]m]m.
As we had pointed out at the end of Section 4.1, this step is unnecessary for the Grassmannian
as [B,X ]m = 0 if d = 1, i.e., for Flag(k;n) = Gr(k,n ). A careful treatment of the computation of
e−ϕtB(X) requires more details than we could go into here and is deferred to [24].
Algorithm 2 Conjugate gradient in Stiefel coordinates
Require: JY0K∈ Flag(n1,...,n d;n) with Y0∈ Rn×nd and Y T
0Y0 =I;
1: ﬁnd Y⊥
0 ∈ Rn×(n−nd) such that [Y0,Y ⊥
0 ]∈ O(n);
2: set X0 = [Y0,Y ⊥
0 ];
3: set G0 =−∇f(JY0K) and H0 =−G0; ⊿ gradient at JY0K as in (47)
4: for i = 0, 1,... do
5: compute ˆB =X T
iHi;
6: set B∈ Rn×n as Bij = ˆBij for j≤nd;
7: Bij =−ˆBji for j≥nd and i≤nd;
8: Bij = 0 otherwise;
9: minimize f
(
Xi exp(tB)In,nd
)
overt∈ R; ⊿ tmin from exact line search
10: set Xi+1 =Xi exp(tminB);
11: set Yi+1 =Xi+1In,nd;
12: set Y⊥
i+1 =Xi+1In,n−nd;
13: set Gi+1 =−∇f(JYi+1K); ⊿ gradient at JYi+1K as in (47)
14: ﬁnd ~Gi+1∈ Rn×(n−nd) such that ˆGi+1 = [Gi+1,~Gi+1] is skew-symmetric;
15: procedure Descent(JYiK, JYi+1K,Gi,Hi) ⊿ new descent direction at JYi+1K
16: τHi =Xi exp(tminB)e−ϕtminB(B)In,nd; ⊿ parallel transport of Hi as in (30)
17: τGi =Xi exp(tminB)e−ϕtminB(ˆGi)In,nd; ⊿ parallel transport of Gi as in (30)
18: γi =gJYi+1K(Gi+1−τGi,Gi+1)/gJYiK(Gi,Gi); ⊿ gas in (29)
19: Hi+1 =−Gi+1 +γiτHi;
20: end procedure
21: reset Hi+1 =−Gi+1 if i + 1≡ 0 mod (k + 1)(n−k);
22: end for
Ensure: JYoptK = JXoptIn,ndK
7.3. Newton and other algorithms over a ﬂag manifold. The closed-form analytic expres-
sions derived in this article permit one to readily extend other optimization algorithms on Euclidean
spaces to ﬂag manifolds. For example, the Newton search direction is given by the tangent vector
OPTIMIZATION ON FLAG MANIFOLDS 23
X∈TJY K Flag(n1,...,n d;n) such that
∇2f(JY K)(X,X′) =gJY K
(
−∇f(JY K),X′)
=− tr(f T
YX′),
for every X′∈TJY K Flag(n1,...,n d;n), which gives us a system of linear equations upon plugging
in the expression for Riemannian Hessian in (50). Using the Newton search direction for Gi in
Algorithm 1 then gives us Newton method on the ﬂag manifold. In a similar vein, one may derive
other standard algorithms for unconstrained optimization, e.g., quasi-Newton method, accelerated
gradient descent, stochastic gradient descent, trust region methods, etc, for the ﬂag manifold.
Nevertheless, given that the goal of our article is to develop foundational material, we will leave
these to future work [24].
