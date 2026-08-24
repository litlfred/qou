---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-007-31-symplectic-monodromy-associated-to-a-hessian
section_title: "Symplectic monodromy associated to a Hessian metric"
section_number: 3.1
pages: 20-22
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
dimensional aﬃne manifold with aﬃne coordinates ( η,ξ ) that embed B as a subset of
R2. In this subsection B does not have any singularities. Suppose that η :B → R is
a submersion over some interval I ⊂ R, and that the ﬁbers of this map are connected
intervals. For our purposes, we consider the case where B is a quadrilateral, bounded
on two opposite sides by line segments of constant η (the vertical boundary ∂vB),
and on the other two sides by line segments that are transverse to the projection to
η (the horizontal boundary ∂hB).
Associated to B and I, we deﬁne complex manifolds X(B) and X(I). The space
X(B) is the subset of the complex torus ( C∗)2 with coordinates w and z such that
(η,ξ ) = (log |w|, log |z|) lies in B, and X(I) is the subset of ( C∗) with coordinate
w such that η = log |w| lies in I. Thus X(I) is an annulus, and we have a map
w :X(B) →X(I), which is a non-singular ﬁbration with ﬁbers isomorphic to annuli.
Philosophically speaking, the map η : B → I is a tropical model of the map w :
X(B) →X(I).
In this situation, the most natural way to prescribe a K¨ ahler stru cture on X(B)
is through a Hessian metric on the base B. This is a metric g such that locally
g = Hess K for some function K : B → R, where the Hessian is computed with
respect to an aﬃne coordinate system. If π : X(B) → B denotes the projection,
then φ = K ◦π is a K¨ ahler potential on X(B), and the positivity of g = Hess K
corresponds to the positivity of the real closed (1 , 1)-form ω = −ddcφ. Explicitly, if
y1,...,y n are aﬃne coordinates corresponding to complex coordinates z1,...,z n on
(C∗)n, then
(48) g =
n∑
i,j=1
∂2K
∂yi∂yj
dyidyj
(49) ω = −ddcφ =
√−1
2
n∑
i,j=1
∂2K
∂yi∂yj
dzi
zi
∧d¯zj
¯zj
Any such K¨ ahler structure is invariant under the S1–action eiθ(z,w ) = ( eiθz,w )
that rotates the ﬁbers of the map w :X(B) →X(I).
We now have a K¨ ahler structure on X(B) such that the ﬁbration w : X(B) →
X(I) has symplectic ﬁbers. Thus there is a symplectic connection on this ﬁbration
whose horizontal subspaces are the symplectic orthogonal spac es to the ﬁbers. This
connection deﬁnes a notion of symplectic parallel transport along p aths in the base
X(I), and symplectic monodromy around loops in the base. Since our ﬁbe rs have
boundary we must show that the symplectic parallel transport pre serves the boundary.
Given that, symplectic parallel transport deﬁnes symplectomorph isms between the
ﬁbers.
We now compute the symplectic connection. Let X ∈T(z,w)X(B) denote a tangent
vector. Let Y ∈ kerdw denote the general vertical vector. The relation deﬁning the
MIRROR OF THE PROJECTIVE PLANE 21
horizontal distribution is ω(X,Y ) = 0, or,
0 =
{
Kηη
dw
w ∧ d ¯w
¯w +Kηξ
(dw
w ∧d¯z
¯z + dz
z ∧ d ¯w
¯w
)
+Kξξ
dz
z ∧ d¯z
¯z
}
(X,Y )
=Kηξ
(dw(X)
w
d¯z(Y )
¯z − d ¯w(X)
¯w
dz(Y )
z
)
+Kξξ
(dz(X)
z
d¯z(Y )
¯z −dz(Y )
z
d¯z(X)
¯z
)
=
(
Kηξ
dw(X)
w +Kξξ
dz(X)
z
)d¯z(Y )
¯z − complex conjugate
(50)
Since dz(Y ) can have any phase, this shows that the quantity in parentheses on the
last line must vanish:
(51) d logz(X) = −Kηξ
Kξξ
d logw(X)
Tropically, this formula has the following interpretation: In the ( η,ξ ) coordinates,
the vertical tangent space is spanned by the vector (0 , 1). The g-orthogonal to this
space is spanned by the vector ( Kξξ, −Kηξ), whose slope with respect to the aﬃne
coordinates is the factor −Kηξ/Kξξ appearing in the formula for the connection.
Lemma 3.1. Let K be such that ∂hB is g-orthogonal to the ﬁbers of the map η :
B →I, and assume that the slope σF of each boundary face F ofB is rational. Then
(1) parallel transport around the loop {|w| =R} acts on the ﬁber over w =R by
rotating each circle of constant |z| through a phase 2π(−Kηξ/Kξξ), and
(2) for each boundary face F , we have 2π(−Kηξ/Kξξ) = 2πσF , the part of ∂hX(B)
lying over F is foliated by multi-sections of the ﬁbration that are horiz ontal
with respect to the symplectic connection.
Proof. Consider the parallel transport of the connection around the loop {|w| =R},
which is a generator of π1(X(I)). As w traverses the path R exp(it), the initial condi-
tion (z,w ) = (r exp(iθ),R ) generates the solution (r exp(iθ+(−Kηξ/Kξξ)it),R exp(it)),
where the expression −Kηξ/Kξξ is constant along the solution curve. As a self-map
of the ﬁber over w =R, this monodromy transformation maps circles of constant |z|
to themselves, but rotates each by the phase 2 π(−Kηξ/Kξξ).
We now consider the behavior of the symplectic connection near the horizontal
boundary ∂hX(B). Let F be a component of ∂hB. Since F is a straight line segment
g-orthogonal to the ﬁbers of η, the function −Kηξ/Kξξ is constant on F and equal
to its slope, which we denote σ = σF . This slope is rational by assumption. The
part of X(B) lying over F is deﬁned by the condition log |z| = σ log |w| +C. Let
w = w0 exp(ρ(t) + iφ(t)) describe an arbitrary curve in the base annulus X(I). If
(z0,w 0) is an initial point that lies over F , then
(52) z =z0 exp {σ(ρ(t) +iφ(t))},w =w0 exp(ρ(t) +iφ(t))
is a path in X(B) that lies entirely over F , and which by virtue of this fact also solves
the symplectic parallel transport equation. Thus the part of ∂hX(B) that lies over
F is foliated by horizontal sections of the ﬁbration, namely ( w/w0)σ = (z/z0) where
π(z0,w 0) ∈F . Take note that σ is merely rational, so these horizontal sections may
actually be multi-sections. □
22 JAMES PASCALEFF
Figure 4. The ﬁbration B →I.
Examples of the Hessian metrics such that ∂hB is g-orthogonal to the ﬁbers of η
may be constructed by starting with the function
(53) F (x,y ) = x2 + y2
x
(54) Hess F =
(
2 + 2 y2
x3 −2 y
x2
−2 y
x2 2 1
x
)
(55) −Fxy
Fyy
= y
x
Thus the families of lines x = c and y = σx form an orthogonal net for Hess F . By
taking x and y to be shifts of the aﬃne coordinates η and ξ on B, we can obtain
a Hessian metric on B such that the vertical boundary consists of lines of the form
x =c, while the horizontal boundary consists of lines of the form y =σx.
