---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-012-46-signs
section_title: "Signs"
section_number: 4.6
pages: 52-54
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
we need to specify the brane structures on the Lagrangians L(d). Since L(d) ﬁbers
over a curve in the base, and its intersection with each ﬁber is a curv e, the tangent
bundle of L(d) is trivial, and we can deﬁne a framing of TL (d) using the vertical
and horizontal tangent vectors at each point. Using this framing, we can give L(d) a
trivial Spin(2) structure, which is induced by product of the trivial Spin(1) structures
on the horizontal an vertical tangent bundles.
MIRROR OF THE PROJECTIVE PLANE 53
Although we have not said much about it up until now, strictly speakin g the gen-
erators of CF ∗(L(d1),L (d2)) are not canonically identiﬁed with intersection points
q ∈ L(d1) ∩L(d2). Rather, each intersection point q gives rise to an abstract 1-
dimensional R–vector space, the orientation line o(q). Following [41, Ch. 11], this
line is canonically isomorphic up to multiplication by a positive number with t he
determinant line of a certain Fredholm operator Dq. The moduli space of pseudo-
holomorphic curves is canonically oriented relative to these lines.
In the case d1 ≤d2, where all the intersections have degree 0, there is a preferred
choice of trivialization for o(q). Let q ∈ L(d1) ∩L(d2). Then we have horizontal-
vertical splittings
(95) TqL(di) = (TqL(di))h ⊕ (TqL(di))v
The intersection pointq has degree 0 as a morphism from L(d1) toL(d2), and moreover
both (TqL(di))h and (TqL(di))v tilt clockwise by a small amount as we pass from L(d1)
to L(d2).
Let H denote the half-plane with a negative puncture. We deﬁne the orien tation
operator Dq = Dh
q ⊕Dv
q , acting on the product bundle C × C → H, where the
boundary condition in the ﬁrst factor is the short path ( TqL(d1))h → (TqL(d2))h,
while that in the second factor is the short path ( TqL(d1))v → (TqL(d2))v. By [41,
Eq. (11.39)], there is a canonical isomorphism
(96) det( Dq) ∼=o(q)
which for our purposes we take as the deﬁnition of o(q). On the other hand, Dq is the
direct sum of the operators Dh
q and Dv
q , which have vanishing kernel and cokernel.
Hence
(97) det( Dq) ∼= det(Dh
q ) ⊗ det(Dv
q ) ∼= R ⊗ R ∼= R
where all isomorphisms are canonical. This gives us a preferred choic e of isomorphism
o(q) ∼= R.
Proposition 4.24. Taking the preferred isomorphisms o(q) ∼= det(Dq) ∼= R for all
generatorsq ∈CF 0(L(d1),L (d2)) for d1 ≤d2, all of the holomorphic triangles found
above have the same sign. Hence, after possibly reversing al l oﬀ the preferred isomor-
phisms o(q) ∼= R, all of them have a positive sign.
Proof. Letu :S →X(B) be a triangle with positive punctures at q1 ∈CF 0(L(d1),L (d2))
and q2 ∈ CF 0(L(d2),L (d3)) and negative puncture at q0 ∈ CF 0(L(d1),L (d3)). Let
Du denote the linearized operator at u. Gluing onto Du the chosen orientation oper-
ators Dq2 and Dq1 in that order gives another orientation operator D′
q0 for the point
q0, and we want to compare the two orientations for the line o(q0).
The linearized operator Du is an operator in the pulled back tangent bundle
u∗TX (B). The bundle TX (B) has a splitting into horizontal and vertical subspaces
TX (B) = TX (B)h ⊕TX (B)v given by the symplectic connection. Over the bound-
aries of S, the Lagrangian boundary condition also splits. Recall from the disc ussion
on gradings in Section 3.3.5 that we have phase maps on horizontal an d vertical sub-
spaces, which measure rotation with respect to the foliations by cir cles on the base
and ﬁber respectively. These serve to give us preferred trivializat ions of u∗TX (B)h
54 JAMES PASCALEFF
and u∗TX (B)v. With respect to these trivializations, the Lagrangian boundary co n-
ditions move only by a small amount: in the horizontal space, TL h has essentially
constant phase, while in the vertical space, TL v moves in such a way that it never
crosses the the line corresponding to the circle foliation on the ﬁber s.
The next step is to observe that the boundary conditions for the o perator Du
are essentially the same independent of the map u and of the chosen degree zero
generators q0,q 1,q 2, and that hence all of the maps u must contribute with the same
sign. In all cases we have an operator in a trivial rank two vector bu ndle, with split
Lagrangian boundary conditions, each factor of which is trivial. Add itionally, each
pair of Lagrangians at a puncture has the same local form, namely t hey are related
by a small clockwise rotation in both the horizontal and vertical dire ctions. The
orientation operators Dqi used to deﬁne the orientation lines are also essentially the
same for every point qi. Hence the relative sign between the determinant of D′
q0 and
o(q0) must be the same for each map u.
If the signs are all positive, we are done. Otherwise by reversing ou r choice of
generator for every line o(q) we obtain bases for the groups CF 0(L(d1),L (d2)) in
which all curves contribute positively.
□
Remark 10. The preceding proposition is another example of the phenomenon ob -
served by Abouzaid [1, Lemma 3.21]. A similar argument is found in [41, ( 13c)].
