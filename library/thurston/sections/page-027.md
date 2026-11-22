---
doc_id: thurston
doc_title: "The Geometry and Topology of Three-Manifolds"
section_id: page-027
section_title: "Page 27"
section_number: null
pages: 27-27
source_pdf: Thurston.pdf
source_sha256: 6010919ed83edd81
toc_source: undetermined
doc_brief: "The Geometry and Topology of Three-Manifolds — 33 sections: Page 1; Page 2; Page 3"
---
2. ELLIPTIC AND HYPERBOLIC GEOMETRY
space as one sheet of the “sphere” of radius i with respect to the quadratic form
Q(X) = X2
1 + · · · + X2
n −X2
n+1
in Rn+1. The set Rn+1, equipped with this quadratic form and the associated inner
product
X · Y =
n
X
i=1
X1Y1 −Xn+1Yn+1,
is called En,1. First we will describe the geodesics on level sets Sr = {X : Q(X) = r2}
of Q. Suppose that Xt is such a geodesic, with speed
s =
q
Q( ˙Xt).
We may di↵erentiate the equations
Xt · Xt = r2,
˙Xt · ˙Xt = s2,
to obtain
Xt · ˙Xt = 0,
˙Xt · ¨Xt = 0,
and
Xt · ¨Xt = −˙Xt · ˙Xt = −s2.
Since any geodesic must lie in a two-dimensional subspace,
¨Xt must be a linear
combination of Xt and ˙Xt, and we have
2.6.1.
¨Xt = −
⇣s
r
⌘2
Xt.
This di↵erential equation, together with the initial conditions
2.13
X0 · X0 = r2,
˙X0 · ˙X0 = s2,
X0 · ˙X0 = 0,
determines the geodesics.
Given two vectors X and Y in En,1, if X and Y have nonzero length we deﬁne
the quantity
c(X, Y ) =
X · Y
kXk · kY k,
where kXk =
p
X · X is positive real or positive imaginary. Note that
c(X, Y ) = c(λX, µY ),
where λ and µ are positive constants, that c(−X, Y ) = −c(X, Y ), and that c(X, X) =
1. In Euclidean space En+1, c(X, Y ) is the cosine of the angle between X and Y . In
En,1 there are several cases.
We identify vectors on the positive sheet of Si (Xn+1 > 0) with hyperbolic space.
If Y is any vector of real length, then Q restricted to the subspace Y ? is indeﬁnite
of type (n −1, 1). This means that Y ? intersects Hn and determines a hyperplane.
18
Thurston — The Geometry and Topology of 3-Manifolds
