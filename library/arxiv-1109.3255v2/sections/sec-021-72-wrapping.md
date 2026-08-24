---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-021-72-wrapping
section_title: "Wrapping"
section_number: 7.2
pages: 64-68
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
Floer cohomology in the mirrors of UL,U C, and UD.
MIRROR OF THE PROJECTIVE PLANE 65
7.2.1. Completions. Wrapped Floer cohomology is formulated in terms of noncom-
pact manifolds containing noncompact Lagrangian submanifolds. Th ese can be de-
ﬁned as (partial) completions of compact manifolds with boundary.
The starting point for all three cases is the original Lefschetz ﬁbr ation X(B) →
X(I) containing the Lagrangians {L(d)}d∈Z. We deﬁne completions ˆXL, ˆXC, and ˆXD.
This process involves replacing a boundary component with an inﬁnite end, either on
the base or in the ﬁber of the Lefschetz ﬁbration.
• L: The manifold ˆXL retains a boundary component at the top horizontal
boundary, corresponding to the ﬁber of the superpotential WL = u. The
ﬁbers of X(B) → X(I) are completed at the other, bottom, end. The base
annulus X(I) is completed to a cylinder ˆX(I), and the ﬁbration is extended
over this cylinder.
• C: The manifold ˆXC retains a boundary component at the bottom horizontal
boundary, corresponding to the ﬁber of the superpotential WC = e−Λ v2
uv−1 . The
ﬁbers are completed at the other, top, end. The base annulus is co mpleted to
a cylinder ˆX(I), and the ﬁbration is extended over this cylinder.
• D: The manifold ˆXD has no boundary, and the ﬁbers are completed at both
ends. The base annulus is completed to a cylinder ˆX(I), and the ﬁbration is
extended over this cylinder.
The torus ﬁbration on X(B) extends to these completions, and yields torus ﬁbra-
tions over completed bases ˆBL, ˆBC, ˆBD.
• ˆBL is a half-plane with singular aﬃne structure given by removing the bot tom
boundary from B and extending in that direction.
• ˆBC is a half-plane with singular aﬃne structure given by removing the top
boundary from B and extending in that direction.
• ˆBD is an entire plane with singular aﬃne structure given by removing all
boundaries from B and extending in all directions.
The Lagrangian submanifolds L(d) are extended to ˆL(d); In all cases, we extend
L(d) into whatever ends are attached so as to be invariant under the L iouville ﬂow
within the end. However, in the case of L, respectively C, we still have the boundary
condition that ˆL(d) is required to end on Σ 1 (the complex hypersurface contained in
the top boundary), respectively Σ 0 (contained in the bottom boundary).
7.2.2. Hamiltonians. The most crucial diﬀerence between the three cases comes from
the choices of Hamiltonians that are be used to perform the wrappin g. The Hamil-
tonians we consider are the sum of contributions from the base and the ﬁber.
Let Hb : ˆX(B) → R be the pullback of a function on the base cylinder which is
a function of the radial coordinate η = log |w| only. Writing the symplectic form on
the base as dρ ∧dθ, where ρ is a function of η, we take Hb to be a convex function
ofρ on the compact part X(I), and linear in ρ on the ends. We also require Hb ≥ 0,
with minimum on the central circle η = 0. Since dHb vanishes on the ﬁbers, XHb is
horizontal.
The ﬁber Hamiltonian Hf is chosen diﬀerently in each case. The main constraint
is that its diﬀerential must vanish at any boundary component which may still be
present. The construction is most convenient if we assume the com pletion preserves
66 JAMES PASCALEFF
theS1-symmetry that rotates the ﬁbers. If µ denotes the moment map for this action,
we can take Hf to be a function of µ. Since XHf is tangent to the ﬁbers, we have
(120) {Hb,H f } =ω(XHb,X Hf ) = 0
which allows us to compute the ﬂow of Hb +Hf term by term.
We use the same base Hamiltonian Hb for all cases. The speciﬁc choice of Hf in
each case is as follows.
• L: Let Hf,L ≥ 0 be a function with a minimum at the top of the ﬁber, convex
in µ on the compact part, and linear in µ on the bottom end.
• C: Let Hf,C ≥ 0 be a function with a minimum at the bottom of the ﬁber,
convex in µ on the compact part, and linear in µ on the top end.
• D: Let Hf,D ≥ 0 be a function with a minimum in the two-thirds of the
way down from the top of the compact part of the ﬁber, convex in µ on the
compact part, and linear in µ on the ends.
In each case, the total Hamiltonian H = Hb +Hf achieves its minimum along a
torus in X(B), which is one of the ﬁbers of the torus ﬁbration over B. Since L(r)
is a section of the torus ﬁbration, H has a unique minimum on L(r), and hence
there is a unique constant chord for L(r), which corresponds to the identity element
er ∈HW ∗(L(r),L (r)). The cases are:
• L: The minimum is along the torus corresponding to the midpoint of the t op
edge of B, where the generator y lies. All of the Lagrangians L(r) for r ∈ Z
intersect this torus at the same point. As an intersection point of L(0) and
L(d), the minimum corresponds to qa,i for (a,i ) = (0, 0).
• C: The minimum is along the torus corresponding to the midpoint of the
bottom edge of B, where the generator p lies. All of the Lagrangians L(r) for
r ∈ 2Z intersect this torus at the same point. As an intersection point of L(0)
and L(r), the minimum corresponds to qa,i for (a,i ) = (0,r/ 2).
• D: The minimum is along the torus two-thirds of the way from the top of
the middle ﬁber of the map B → I, where the generator yp lies. All of
the Lagrangians L(r) for r ∈ 3Z intersect this torus in the same point. As
an intersection point of L(0) and L(r), the minimum corresponds to qa,i for
(a,i ) = (0,r/ 3).
Remark 14. The Hamiltonians we obtain as Hb +Hf are not admissible in the usual
sense, because they vanish at some boundaries, and, even in the c aseD, are not linear
with respect to a cylindrical end. Closer to our situations are the Lefschetz admissible
Hamiltonians considered by Mark McLean [34], that are precisely thos e functions on
the total space of a Lefschetz ﬁbration that are the sum of admis sible Hamiltonians
on the base and ﬁber separately.
7.2.3. Generators. Given Lagrangian submanifoldsL1,L 2 ofX, equipped with Hamil-
tonianH, and r ∈ R, we get Floer cohomology complexes CF ∗(L1,L 2;rH ) generated
by time-1 trajectories of XrH starting on L1 and ending on L2. As usual the diﬀer-
ential counts inhomogeneous pseudo-holomorphic strips. We also h ave continuation
maps
(121) CF ∗(L1,L 2;rH ) →CF ∗(L1,L 2;r′H), r<r ′
MIRROR OF THE PROJECTIVE PLANE 67
given by counting strips where the inhomogeneous term interpolate s between r′XH
and rXH. At the homology level, the continuation maps form an inductive syst em,
and we deﬁne the wrapped Floer cohomology
(122) HW ∗(L1,L 2) = lim
r→∞
HF ∗(L1,L 2;rH )
Our purpose in this section is simply to set up an enumeration of the ge nerators
of CF ∗(L(d1),L (d2);rH ) in each of the three cases. These generators can also be
regarded as intersection points φrH (L(d1)) ∩L(d2). In order to make the situation as
convenient as possible for our later arguments, we reﬁne our choic e of Hamiltonians so
as to ensure that φrH (L(d)) is actually L(d′) for some d′; thus we can identify wrapped
Floer cohomology generators with intersection points of our origina l Lagrangians.
This is done by adjusting the slopes of our Hamiltonians on the ends.
• We take the base Hamiltonian Hb so that the time–1 ﬂow completes 1 turn
on the cylindrical ends of the base.
• For cases L andC, we take the ﬁber Hamiltonian Hf so that the time–1 ﬂow
completes 1/2 turn on the cylindrical end of the ﬁber.
• For caseD, we take the ﬁber Hamiltonian Hf so that the time–1 ﬂow completes
1/3 turn at the top of the ﬁber, and 1 /6 turn at the bottom of the ﬁber.
In all cases the total Hamiltonian we use is H =Hb +Hf .
The way to understand the ﬂow of H is to ﬁrst apply Hf , then Hb. The ﬂow of Hf
wraps L(d) in the ﬁber, while the ﬂow of Hb, when it completes a loop in the base,
performs the monodromy of the Lefschetz ﬁbration around that loop, which undoes
some of the wrapping due to Hf .
We can relate φH(L(d)) to L(d′) as follows:
• L: we have φrH (L(d)) = L(d −r).
• C: we have φ2rH (L(d)) = L(d −2r). Note that the same cannot be said with r
in place of 2r; in that case the two Lagrangians intersect the bottom boundary
(where no wrapping occurs) in diﬀerent points.
• D: we have φ3rH (L(d)) = L(d − 3r). Again the same cannot be said with r
in place of 3 r.
In order to identify generators with intersection points, we pertu rb the boundary
intersection points in a positive sense just as before. In the cases with boundary,
where the Hamiltonian is supposed to have a minimum at the boundary, it is useful
to perform this perturbation in an extra collar attached to the bou ndary, so that the
Lagrangians still intersect at the minimum of H if they did prior to the perturbation.
Once this is done, we can identify
(123) CF ∗(L(d1),L (d2);rH ) ∼=CF ∗(φrH (L(d1)),L (d2)) ∼=CF ∗(L(d1 −r),L (d2))
wherer ∈ Z in case L,r ∈ 2Z in case C, and r ∈ 3Z in case D. This identiﬁcation is
compatible with the gradings, which shows that for r > d1 −d2, the Floer complex
CF ∗(L(d1),L (d2);rH ) is concentrated in degree zero, and so has vanishing diﬀeren-
tial. Recall that the generators of the last group are identiﬁed with B( 1
d2−d1+r Z).
Once we are in the range d2 − d1 + r > 0, we ﬁnd that as r increases, new
generators are created, none are destroyed, and the generat ors that already ex-
ist are “compressed” toward the minimum of H. This gives rise to naive inclu-
sion maps i : CF ∗(L(d1),L (d2);rH ) → CF ∗(L(d1),L (d2);r′H) for r < r′, where
68 JAMES PASCALEFF
r > d1 −d2. In terms of fractional integral points, this i corresponds to the map
B( 1
d2−d1+r Z) →B( 1
d2−d1+r′ Z) which is dilation by the appropriate factor centered at
the point corresponding to the minimum of H.
We can index the points of ˆB( 1
dZ) with two indices. The index a ∈ Z corresponds
to the column lying at η = a/d, while the index i that indexes points within a
column, and which lies in {0,...,
⌊
d−|a|
2
⌋
} in the compact case, is now unbounded
in the positive direction in case L, in the negative direction in case C, and in both
directions in case D. We use the notation qa,i for these points.
