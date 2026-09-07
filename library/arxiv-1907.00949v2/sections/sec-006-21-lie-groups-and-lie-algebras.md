---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-006-21-lie-groups-and-lie-algebras
section_title: "Lie groups and Lie algebras"
section_number: 2.1
pages: 5-6
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
bundle. A Riemannian metric on M is a smooth section g : M→ T∗M⊗T∗M such that gx :=
g(x)∈ T∗
xM⊗T∗
xM is a positive deﬁnite symmetric bilinear form on the tangent space TxM for
every x∈ M. Intuitively, a Riemannian metric gives an inner product on TxM for every x∈ M
and it varies smoothly with respect to x∈ M. Let G be a group and let m : G×G→ G be
the multiplication map m(a1,a 2) = a1a2 and i : G→ G be the inversion map i(a) = a−1. Then
G is a Lie group if it is a smooth manifold and the group operations m and i are smooth maps.
The tangent space g of G at the identity e∈G is a Lie algebra, i.e., a vector space equipped with
a Lie bracket, a bilinear map [ ·,·] : g× g→ g satisfying [X,Y ] =−[Y,X ] (skew-symmetry) and
[X, [Y,Z ]]+[Z, [X,Y ]]+[Y, [Z,X ]] = 0 (Jacobi identity). For example, if G is the orthogonal group
O(n) of all n×n real orthogonal matrices, then its Lie algebra so(n) is the vector space of all n×n
real skew-symmetric matrices.
For a Lie group G, we may deﬁne the left and right translation maps La,Ra : G → G by
La(x) =m(a,x ) =ax and Ra(x) =m(x,a ) =xa. We say that a Riemannian metric g on G is left
invariant if for all a∈G,
gLa(x)
(
(dLa)x(X), (dLa)x(Y )
)
=gx(X,Y );
right invariant if for all b∈G,
gRb(x)
(
(dRb)x(X), (dRb)x(Y )
)
=gx(X,Y );
and bi-invariant if for all a,b∈G,
gRb◦La(x)
(
(d(Rb◦La))x(X), (d(Rb◦La))x(Y )
)
=gx(X,Y )
over all X,Y ∈TxM.
2.2. Homogeneous spaces. We now recall some basic deﬁnitions and facts about homogeneous
spaces. Throughout this article, we will use double brackets JxK to denote the equivalence class of
x.
Deﬁnition 2.1. LetG be a Lie group acting on a smooth manifold M viaϕ :G×M→M. If the
actionϕ is smooth and transitive, i.e., for any x,y∈M, there is some a∈G such thatϕ(a,x ) =y,
then M is called a homogeneous space of the Lie group G.
For a point x∈ M, the subgroup Gx ={a∈ G : ϕ(a,x ) = x} is called the isotropy group of
x. We write G/Gx for the quotient group of G by Gx and denote by JaK∈ G/Gx the coset (or
equivalence class) of a∈ G. Since G acts on M transitively, we see that there is a one-to-one
correspondence F betweenG/Gx and M given by
F :G/Gx→M, F (JaK) =ϕ(a,x ),
for any x∈ M. In fact, F deﬁnes a diﬀeomorphism between the two smooth manifolds, which is
the content of the following theorem [8, Theorems 9.2 and 9.3].
Theorem 2.2. LetG be a Lie group acting on a smooth manifold M. For any x∈M, there exists
a unique smooth structure on G/Gx such that the action
ψ :G×G/Gx→G, ψ (a, Ja′K) = Jaa′K
is smooth. Moreover, the map F :G/Gx→M sending JaK to ϕ(a,x ) is a G-equivariant diﬀeomor-
phism, i.e., F is a diﬀeomorphism such that F
(
ψ(a, Ja′K)
)
=ϕ
(
a,F (Ja′K)
)
.
The Grassmannian Gr(k,n ) ofk-dimensional subspaces in Rn is probably the best known example
of a homogeneous space in manifold optimization. Indeed, O( n) acts transitively on Gr(k,n ) and
as any k-dimensional subspace W⊆ Rn has isotropy group isomorphic to O( k)× O(n−k), we
obtain the well-known characterization of Grassmannian
Gr(k,n )∼= O(n)/
(
O(k)× O(n−k)
)
6 K. YE, K. S.-W. WONG, AND L.-H. LIM
that is crucial for manifold optimization. Throughout this article ‘ ∼=’ will mean diﬀeomorphism.
Let G be a Lie group and M a homogeneous space of G with action ϕ :G×M→M. Fix any
x∈M and let H denote its isotropy group. By Theorem 2.2 we may identify M with G/H. The
left translation map in Section 2.1 may be extended to this setting asLa :M→M,La(y) =ϕ(a,y )
for any a∈G. In particular, if a∈H, then La(x) =x, and we have a linear isomorphism
(dLa)x :TxM→TxM.
Letg :M→T∗M⊗T∗M be a Riemannian metric on M. We say that g isG-invariant if for every
y∈M and a∈G, we have
gLa(y)
(
(dLa)y(X), (dLa)y(Y )
)
=gy(X,Y ) for all X,Y ∈TyM.
AsM =G/H, we haveTJeKM = g/h where g and h are the Lie algebras ofG andH respectively.
Heree∈G is the identity element. This allows us to deﬁne the adjoint representation AdH :H→
GL(g/h), a↦→d(La◦Ra−1)JeK. In other words, for any a∈H and X∈ g/h,
AdH(a)(X) =d(La◦Ra−1)JeK(X).
An inner product η on the vector space g/h is said to be Ad H-invariant if for every a∈H,
η(AdH(a)(X), AdH(a)(Y )) =η(X,Y ) for all X,Y ∈ g/h.
We state an important result about their existence and construction [13, Proposition 3.16].
Proposition 2.3. LetG be a connected Lie group and H a closed Lie subgroup with Lie algebras g
and h respectively. If there is a subspace m of g such that g = m⊕ h and AdH(m)⊆ m, then there is
a one-to-one correspondence between G-invariant metrics on M =G/H and AdH-invariant inner
products on m.
Proposition 2.3 says that if h⊆ g admits a complement m, then we may obtain a G-invariant
metric g onM by an AdH-invariant inner product on m. Moreover, we may identify TxM with m,
implying that the metric g onM is essentially determined by gx at a single arbitrary point x∈M.
If in addition G is simple and compact, then G admits the unique bi-invariant metric called the
canonical metric on M and (M,g ) is called a normal homogeneous space.
Proposition 2.4. IfG is a compact Lie group, then G admits a bi-invariant metric and this metric
induces a G-invariant metric g on M =G/H for any closed subgroup H⊆G.
