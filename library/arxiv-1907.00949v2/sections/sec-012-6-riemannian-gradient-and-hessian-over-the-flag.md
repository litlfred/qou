---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-012-6-riemannian-gradient-and-hessian-over-the-flag
section_title: "Riemannian Gradient and Hessian over the flag manifold"
section_number: 6
pages: 19-21
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
We will derive expressions for the Riemannian gradient and Riemannian Hessian of a real-valued
function on a ﬂag manifold, the main ingredients of optimization algorithms. Although in principle
we may use any of the four extrinsic coordinate systems introduced in the last two sections —
orthogonal (as n×n orthogonal matrices), Stiefel (as n×nd orthonormal matrices), projection or
reduced projection (as d-tuples ofn×n projection matrices) coordinates — Stiefel coordinates give
the most economical representation and we will use this as our coordinates of choice. So in the
following we will identify
Flag(n1,...,n d;n) = V(nd,n )/
(
O(n1)× O(n2−n1)×···× O(nd−nd−1)
)
. (45)
Our expressions for gradient and Hessian in Stiefel coordinates may of course be converted to other
coordinates — straightforward although the results may be notationally messy.
Proposition 6.1 (Riemannian gradient). Let f : Flag(n1,...,n d;n)→ R be a smooth function
expressed in Stiefel coordinates Y ∈ V(nd,n ). Deﬁne the n×nd matrix of partial derivatives,
fY :=
[ ∂f
∂yij
]n,nd
i,j=1
. (46)
Write Y = [Y1,...,Y d] whereYi∈ Rn×(ni−ni−1) and fY = [fY1,...,f Yd] wherefYi is the n× (ni−
ni−1) submatrix, i = 1,...,d . Then its Riemannian gradient at JY K∈ Flag(n1,...,n d;n) is given
by∇f(JY K) = [∆1,..., ∆d] where
∆i =fYi−
(
YiY T
i fYi +
∑
j⁄=i
Yjf T
YjYi
)
, i = 1,...,d. (47)
20 K. YE, K. S.-W. WONG, AND L.-H. LIM
Proof. For anyX∈TJY K Flag(n1,...,n d;n), let Xa∈ Rn×n be the unique skew-symmetric matrix
such that X =QXaIn,nd, where Q∈ O(n) is such that Y =QIn,nd. Since the metric expressed in
Stiefel coordinates (29) and expressed in orthogonal coordinates (14) must be equal,
gJY K
(
∇f(JY K),X
)
=gJQK
(
∇f(JY K)a,Xa
)
= 1
2 tr(∇f(JY K)T
aXa). (48)
By deﬁnition of Riemannian gradient (5), we also have
gJY K(∇f(JY K),X ) = tr(f T
YXa). (49)
Comparing (48) and (49), we see that∇f(JY K) is the projection offY ontoTJY K Flag(n1,...,n d;n),
i.e., fY =∇f(JY K) + Z for some Z orthogonal to TJY K Flag(n1,...,n d;n). We may take Z =
[Z1,...,Z d] to be
Zi :=YiY T
i fYi +
∑
j⁄=i
Yjf T
YjYi, i = 1,...,d,
and verify that because of (27), we indeed have fY−Z∈ TJY K Flag(n1,...,n d;n) and thus Z is
orthogonal to TJY K Flag(n1,...,n d;n). □
The Riemannian gradient∇f may also be derived by solving an optimization problem as in [29].
Note that if d = 1, (47) becomes ∇f(JY K) = ∆ = fY−YY TfY , the well-known expression for
Riemannian gradient of Grassmannian in [16].
Proposition 6.2 (Riemannian Hessian) . Let f : Flag(n1,...,n d;n)→ R be a smooth function
expressed in Stiefel coordinates Y ∈ V(nd,n ) and let fY be as in (46). Then its Riemannian
Hessian∇2f(JY K) at JY K∈ Flag(n1,...,n d;n) is the symmetric bilinear form given by
∇2f(JY K)(X,X′) =fY,Y (X,X′)− 1
2
[
tr(f T
YQBTQTX′) + tr(f T
YQC TQTX)
)]
, (50)
for X,X′∈TJY K Flag(n1,...,n d;n), where
fY,Y (X,X′) :=
n∑
i,k=1
nd∑
j,l=1
∂2f
∂yij∂ykl
xijx′
kl, (51)
Q∈ O(n) is such that QIn,nd =Y , and B,C ∈ Rn×n are the unique skew-symmetric matrices such
that X =QBIn,nd, X′ =QCIn,nd respectively.
Proof. By Proposition 4.14, a geodesic γ with γ′(0) = X and γ(0) = JY K takes the form γ(t) =
JQ exp(tB)In,ndK whereQ∈ O(n) is such that Y =QIn,nd andX =QBIn,nd. Applying chain rule,
d
dtf(γ(t)) = tr
(
f T
Yγ′(t)
)
, d2
dt2f(γ(t)) = tr
(
γ′(t)Tf T
γ(t),γ(t)γ′(t)
)
+ tr
(
f T
Yγ′′(t)
)
;
followed by evaluating at t = 0 gives
∇2f(JY K)(X,X ) = d2
dt2f(γ(t))
⏐⏐⏐
t=0
=fY,Y (X,X )− tr(f T
YQBTQTX).
The required expression (50) then follows from (5) and (4). □
Ifd = 1, (50) reduces to the well-known expression for Riemannian Hessian of the Grassmannian
[16, Section 2.5.4] since
∇2f(JY K)(X,X′) =fY,Y (X,X′)− tr(f T
YQBTQTX′)
=fY,Y (X,X′)− tr(f T
YY (X′)TX) =fY,Y (X,X′)− tr(X TX′Y TfY ).
OPTIMIZATION ON FLAG MANIFOLDS 21
There is slight inconsistency in our deﬁnitions of fY and fYY to make these expressions easily
portable into computer codes. To be consistent with (51), we could deﬁne fY as a linear form:
fY (X) =
n,nd∑
i,j=1
∂f
∂yij
xij
for X∈TJY K Flag(n1,...,n d;n). Alternatively, to be consistent with (46), we could deﬁne fYY to
be a hypermatrix of partials (this is not a 4-tensor, just a convenient way to represent a 2-tensor):
fYY =
[ ∂2f
∂yij∂ykl
]n,nd,n,nd
i,j,k,l=1
.
