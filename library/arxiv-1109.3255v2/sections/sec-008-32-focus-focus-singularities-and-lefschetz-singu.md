---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-008-32-focus-focus-singularities-and-lefschetz-singu
section_title: "Focus-focus singularities and Lefschetz singularities"
section_number: 3.2
pages: 22-32
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
the case where the aﬃne structure on B contains a focus-focus singularity, that is,
a singularity with monodromy conjugate to
(
1 0
1 1
)
, and the monodromy invariant
direction of this singularity is parallel to the ﬁbers of the map η : B → I. The
goal is to construct a symplectic manifold X(B), along with a Lefschetz ﬁbration
w : X(B) → X(I). Topologically X(B) is a torus ﬁbration over B with a single
pinched torus ﬁber over the singular point.
Let B be an aﬃne manifold with a single focus-focus singularity, and η : B → I
a globally deﬁned aﬃne coordinate. Suppose B has vertical boundary consisting
of ﬁbers of η, as before, and suppose that the horizontal boundary consists of line
segments of rational slope. If we draw the singular aﬃne structur e with a branch
cut, one side will appear straight while the other appears bent, tho ugh the bending
is compensated by the monodromy of the focus-focus singularity. Figure 4 shows the
projection B →I, with the ﬁbers drawn as vertical lines.
Proposition 3.2. The manifold X(B) admits an exact symplectic structure making
w : X(B) → X(I) a symplectic Lefschetz ﬁbration, with a single Lefschetz cr itical
point. This critical point coincides with focus-focus sing ularity of the torus ﬁbration
π : X(B) → B. There is a neighborhood U ⊂ B of the ﬁber of η through the
singularity such that on the complement of π−1(U), the symplectic form is locally
given by a Hessian metric of the form considered in Lemma 3.1.
MIRROR OF THE PROJECTIVE PLANE 23
Proof. Suppose for convenience that the singularity occurs at η = 0. For the ﬁrst
step, divide the base B into regions B−ǫ = η−1(−∞, −ǫ] and B+ǫ = η−1[ǫ, ∞). On
these aﬃne manifolds we may take the Hessian metrics and associate d K¨ ahler forms
considered in Lemma 3.1, using functions K− and K+ derived from the example
following that Lemma. Hence we get a ﬁbration with symplectic connec tion over the
disjoint union of two annuli: w :X(B−ǫ
∐ B+ǫ) →X(I−ǫ
∐ I+ǫ)
The second step is extend the Lefschetz ﬁbration over a band con necting the two
annuli. Consider the two annuli X(I−ǫ)∐ X(I+ǫ) ⊂ C∗. Choose a path connecting
these two annuli, along the positive real axis, say. By identifying the ﬁbers over the
end points, the ﬁbration extends over this path. By thickening the path up to a band
and ﬁlling in the ﬁbers over the band, we get a Lefschetz ﬁbration ov er a surface
which is topologically a pair of pants. Since the ﬁbration over the band is trivial, the
gluing can be done in such a way that the horizontal boundary compo nents of the
total space are still foliated by multi-sections of the symplectic con nection.
The third step is to ﬁll in the rest of the region between the two annu li with the
standard model of a Lefschetz singularity. In order for this to ma ke sense, we need the
symplectic monodromy around the loop in the base being ﬁlled in to be a D ehn twist.
This can be seen by comparing the symplectic monodromy transform ations around the
loops in X(I−ǫ) and X(I+ǫ). Let z− and z+ denote complex coordinates on X(B−ǫ)
and X(B+ǫ) corresponding to a direction transverse to the ﬁbration η : B → I,
so that z− and z+ give coordinates on the ﬁbers of w : X(B) → X(I). Assume
these coordinates match up in one of the bands connecting B−ǫ to B+ǫ. Due to the
monodromy of the aﬃne manifold they do not coincide in the other ban d, where
we put the branch cut. Let F1 and F0 denote the top and bottom faces of ∂hB
respectively, and suppose that F0 is split into two parts F0+ and F0− by the branch
cut. Associated to each of these we have a slope σF .
Now we compute the monodromy obtained when we traverse a loop in X(I−ǫ) in
the negative sense followed by a loop in X(I+ǫ) in the positive sense, connecting these
paths through the band connecting the two annuli. We use Lemma 3.1 to measure
the diﬀerence between the amounts of phase rotation in the z− and z+ coordinates
along the top and bottom horizontal boundaries under symplectic p arallel transport,
encoding this as an overall twisting. By Lemma 3.1, as we transport a round the
negative loop in X(I−ǫ), the z− coordinate on π−1(F1) rotates through an angle
−2πσF1 and the z− coordinate on π−1(F0−) rotates through an angle −2πσF0−. Thus
the relative twist of the two ends of the ﬁber is −(σF1 −σF0−) turns. By the same
token, on the other side the z+ coordinate on π−1(F1) rotates through an angle 2 πσF1,
while the z+ coordinate on π−1(F0+) rotates through 2 πσF0+, and the overall relative
twisting is (σF1 −σF0+) turns. Composing these monodromy transformations, we ﬁnd
that the ﬁber undergoes a twisting of σF0− −σF0+ turns. Because the monodromy
of the aﬃne structure is a shear, this diﬀerence of slopes equals −1. Thus the ﬁber
undergoes a right-handed Dehn twist (whose local model is obtaine d by taking the
annulus {1 ≤ |z| ≤ 2} and rotating the outer boundary by one clockwise turn).
This allows us to ﬁll in the ﬁbration with a standard ﬁbration with a single Lefschetz
singularity whose vanishing cycle is the equatorial circle on the cylinde r ﬁber. Because
the top and bottom boundaries are ﬁxed under the monodromy tra nsformation, the
foliation of the horizontal boundary extends over the gluing. Since this local model
24 JAMES PASCALEFF
is symmetric under the S1–action which rotates the ﬁbers, choosing an S1–invariant
gluing allows us to deﬁne a symplectic S1–action on X(B) which rotates the ﬁbers of
w :X(B) →X(I).
Since the total space is S1–symmetric, we can construct the Lagrangian tori as
in section 2.1, by taking circles of constant |w| in the base and S1–orbits in the
ﬁber. These actually coincide with the tori found in X(B−ǫ
∐ B+ǫ) as ﬁbers of the
projection to B, so this construction extends the torus ﬁbrations on X(B−ǫ
∐ B+ǫ)
to all of X(B). □
Remark 5. Since this construction is local on the base X(I), the construction extends
in an obvious way to the situation where several focus-focus singu larities with parallel
monodromy-invariant directions are present. See Section 6 for fu rther discussion.
Remark 6. There is a more direct way to obtain the sort of symplectic structur e we
desire, based on a version of the mapping-torus construction. St art with a Lefschetz
ﬁbration over an rectangle, with a critical value corresponding to t he singular point
ofB. Trivialize the ﬁbration over the top and bottom sides of the base re ctangle, and
glue the top and bottom together, identifying the ﬁbers using a sym plectomorphism,
yielding a ﬁbration over an annulus that we identify with X(I). Choosing the gluing
symplectomorphism appropriately, we can ensure that the monodr omies around the
sub-annuli X(I±ǫ) ⊂ X(I) agree with what is obtained from the Hessian metric
construction. Our preference for the construction described a bove is that it proceeds
more naturally from the aﬃne geometry of B.
Remark 7. In the main example of this paper, the aﬃne manifold does not have
vertical boundary, but rather corners at the extreme values of η. To deﬁne the
symplectic structure, we deal with this by cutting oﬀ arbitrarily sma ll pieces of B
at the corners so that the result has vertical boundaries. Howev er, in terms of the
correspondence to tropical geometry, we still consider the unmo diﬁed manifold B.
Deﬁnition 1. Let B be the aﬃne manifold appearing in the mirror of ( CP2,D ).
We denote by X(B) be the symplectic manifold obtained from Proposition 3.2, after
cutting oﬀ the corners of B as in Remark 7.
Recall that the horizontal boundary ∂hX(B) is the union of two faces ( ∂hX(B))1
and (∂hX(B))0 corresponding to F1 andF0, the top and bottom faces of B. Likewise
we speak of the top and bottom boundary circles of the ﬁbers of w. The following
proposition summarizes key properties of X(B). It follows from the analysis of the
monodromies in the proof of Proposition 3.2 and Lemma 3.1.
Proposition 3.3. The Lefschetz ﬁbration w :X(B) →X(I) has the following prop-
erties:
(1) The monodromy given by traversing the inner boundary loop clockwise ﬁxes
the top boundary circle of the ﬁber, and rotates the bottom bo undary circle
through a half turn, in such a way that the square of this opera tion is isotopic
to a right-handed Dehn twist.
(2) The monodromy given by traversing the outer boundary loop clockwise ﬁxes
the top boundary circle and acts on the bottom boundary circl e by a half-turn,
except that the square of this operation is isotopic to a left-handed Dehn twist.
MIRROR OF THE PROJECTIVE PLANE 25
(3) As the top face F1 has integral slope (zero in our diagrams), the leaves of the
foliation on (∂hX(B))1 are single-valued sections of the w-ﬁbration.
(4) As the bottom face F2 has half-integral slope ( ±1/2 on either side of the cut in
our diagrams), the leaves of the foliation on (∂hX(B))0 are two-valued sections
of the w-ﬁbration.
Remark 8. The foliation of the boundary faces by horizontal sections is relate d to
the superpotential W = u +e−Λv2/(uv − 1) studied in the previous Section 2. The
general ﬁber W = constant is a twice-punctured torus. On the other hand, we can
consider the curves deﬁned by the individual terms of W . The equation u = constant
deﬁnes a curve such that the projection w =uv − 1 : X ∨ → C is one-to-one, so this
curve is a section of w. The curves deﬁned by the second term v2/(uv − 1) = constant
are likewise two-valued sections of w : X ∨ → C. Our perspective is that the leaves
of the foliations on the boundary components of X(B) correspond roughly to these
curves deﬁned by the individual terms of the superpotential.
3.3. Lagrangians ﬁbered over paths. The base of the Lefschetz ﬁbration is the
annulus X(I) = {R−1 ≤ |w| ≤ R} with a critical value at w = −1. The symplectic
structures constructed in 3.2 have the property that the symple ctic connection is ﬂat
throughout the annuli X(I−ǫ) = {R−1 ≤ |w| ≤ e−ǫ}, X(I+ǫ) = {eǫ ≤ |w| ≤ R}, as
well as through a band along the positive real axis joining these annu li.
We call the Lagrangians L(d) constructed here sections, because they will turn out
to be sections of the torus ﬁbration on X(B). At the same time, they are not sections
of the Lefschetz ﬁbration, but rather ﬁber over paths in X(I).
3.3.1. The zero-section. The ﬁrst step is to construct the Lagrangian submanifold
L(0) ⊂X(B), which we will use as a zero-section of the torus ﬁbration and refe rence
point through out the paper.
Deﬁnition 2. Let ℓ(0) ⊂ X(I) be the path that runs along the positive real axis.
Trivializing the ﬁbration along that path, take a path in the ﬁber cylind er connecting
the top and bottom boundary circles. The Lagrangian tori interse ct the ﬁbers of the
Lefschetz ﬁbration in circles, and we choose our ﬁber path so that it intersects each
such circle once. We denote by L(0) ⊂X(B) the product Lagrangian submanifold.
If we want to be speciﬁc, we could take the factor in the ﬁber to be t he positive real
locus of the coordinates z− or z+. By construction, L(0) intersects each Lagrangian
torus once.
OnceL(0) is chosen, it selects leaves of the foliations by horizontal sectio ns on each
boundary face, namely those leaves containing the ﬁberwise bound ary of L(0). Call
these leaves Σ 0 and Σ 1 (bottom and top respectively). Clearly we could have chosen
these leaves ﬁrst and then constructed L(0) accordingly.
3.3.2. The degree d section. We can now use L(0) as a reference to construct the
other Lagrangians L(d).
Deﬁnition 3. Letℓ(d) be a base path, with the same end points and midpoint as ℓ(0),
and which winds d times (relative to ℓ(0)) in X(I−ǫ) and also d times in X(I+ǫ). The
winding of ℓ(d) is clockwise as we go from smaller to larger radius. The Lagrangian
L(d) is deﬁned to coincide with L(0) in the ﬁber over the common endpoint of ℓ(0)
26 JAMES PASCALEFF
and ℓ(d) on the inner boundary circle of X(I), and to be deﬁned elsewhere as the
submanifold swept out by symplectic parallel transport along the pa th ℓ(d).
Recall that we cut oﬀ the corners of B so that we actually have ﬁbers at the
endpoints of ℓ(0) and ℓ(d). Because the boundary leaves Σ 0 and Σ 1 are preserved by
symplectic parallel transport, the boundary of L(d) is contained in these same leaves,
which as in Remark 8 correspond to hypersurfaces deﬁned by the in dividual terms of
the superpotential.
The behavior of L(d) in the ﬁber direction is determined with the aid of Proposition
3.3.
Proposition 3.4. As we parallel transport clockwise along ℓ(d) in inner annulus
X(I−ǫ), the ﬁber component of L(d) is transformed by half-right-handed Dehn twists,
while as we parallel transport clockwise along ℓ(d) in the outer annulus X(I+ǫ), we
pick up half-left-handed Dehn twists. In the end, all of the t wisting cancels out, so
that L(d) and L(0) again coincide over the common endpoint of ℓ(0) and ℓ(d) on the
outer boundary circle of X(I).
The proposition is illustrated in Figure 5, which depicts L(0),L(1), and L(2). The
lower portion of the ﬁgure shows the base: the straight line is ℓ(0), while the spirals
areℓ(1) and ℓ(2). The marked point is the Lefschetz critical value. The upper po rtion
of the ﬁgure shows the ﬁve ﬁbers where ℓ(0) and ℓ(2) intersect. The behavior of L(i)
for i = 0, 1, 2 in these ﬁbers is depicted.
The Lagrangian submanifold L(d) is indeed a section of the torus ﬁbration. If TR,λ
is the torus over the circle {|w| =R} at height λ, then since ℓ(d) intersects {|w| =R}
at one point, there is exactly one ﬁber of w : X(B) → X(I), where L(d) and TR,λ
intersect. Since L(d) intersects each S1–orbit in that ﬁber once, we ﬁnd that L(d)
and TR,λ indeed intersect once.
3.3.3. Admissibility. We now explain in what sense these Lagrangians are admissible.
The relevant notion of admissibility is the one found in [7, §7.2], where admissibility
with respect to a reducible hypersurface whose components corr espond to the terms
of the superpotential is discussed. In our case, we have two comp onents Σ 0 and Σ 1,
and the admissibility condition is that, near Σ i, the holomorphic function zi such
that Σ i = {zi = 1 } satisﬁes zi|L ∈ R. The Lagrangian L(d) will have this property
if the symplectic structure is chosen so that the symplectic monodr omy near Σ 1 is
actually trivial, while the symplectic monodromy near Σ 0 is a rigid rotation by π.
Otherwise, we can only say that the phase of zi varies within a small range near Σ i. In
the computations in section 4 we actually perturb these Lagrangian s in a prescribed
manner near the boundary.
The notion of admissibility also prescribes the behavior over the endp oints of the
base pathℓ(d). Recall that we cut oﬀ the corners of B in order to deﬁne the symplectic
structure. Our notion of admissibility remembers that there was a c orner at this
point, by requiring the L(d) to coincide with L(0) over the endpoints of ℓ(d). The
justiﬁcation for this is that, if we try to extend the geometry all th e way to the
corner of B, we see that the two components Σ 0 and Σ 1 would intersect, and we need
the Lagrangian to behave tamely at this intersection. A local model for this sort of
situation is the two complex curves Σ 0 = {x = 0 }, Σ 1 = {y = 0 } intersecting at
MIRROR OF THE PROJECTIVE PLANE 27
Figure 5. The Lagrangians L(0), L(1), and L(2). Parts of the ﬁgure
corresponding to L(i) are labeled by i.
(0, 0) in C2, with the Lagrangian being L = ( R≥0)2, and with the ﬁbration being
w =x +y : C2 → C.
3.3.4. Positive perturbations. The Lagrangians L(d) constructed above intersect each
other on the boundary of X(B), and in particular it is not clear whether such inter-
section points are supposed count toward the Floer cohomology. T here is a canonical
way to perturb the Lagrangians so as to push all intersection point s which should
count toward Floer cohomology into the interior of X(B), also used by Abouzaid [1].
This construction is not symmetric with respect to switching the Lag rangians.
Let K and L be two of the Lagrangians L(d). The perturbation process we use in
computing morphisms CF ∗(K,L ) from K to L has two steps. First we perturb the
Lagrangians near the boundary, staying within the class of Lagran gians ﬁbering over
paths, so that they intersect at the boundary in such way that th e tangent space to
the base path of L is a small counterclockwise rotation of the tangent space to base
path of K, and similarly in the ﬁber. If K =L(d1) and L =L(d2) with d1 <d 2, this
will create new intersection points in the interior, while if d1 > d2 the pair K,L is
already in the desired position.
The second step is that we perturb K and L at the boundary intersection so
as to destroy the intersection there. Alternatively, we could just forget about the
boundary intersection points in our computations, but actually rem oving them is more
convenient in the technical part of the paper. The pair of Lagrang ians obtained from
28 JAMES PASCALEFF
Figure 6. (a) The local picture of positive perturbation. (b) The end
result when K =L(0) and L =L(2).
this process is called positively perturbed. This has the eﬀect that one of Lagrangians
in the pair may not admissible in the sense above, since it does not have boundary
on Σ 0 and Σ 1. In section 4, the Lagrangians we work with are positive perturbat ions
of admissible Lagrangians.
Please see ﬁgure 6 for a local picture of the positive perturbation, and the end
result in the case of K =L(0) and L =L(2).
Remark 9. The asymmetry in the perturbations is essential for the mirror sym metry
statement that we wish to prove. Mirror symmetry predicts that HF ∗(L(d1),L (d2)) is
isomorphic to Ext ∗(OCP2(d1), OCP2(d2)) ∼=H ∗(CP2, OCP2(d2−d1)). (The main purpose
of the paper is to verify that this is true for d1 < d2 in a way compatible with the
product structures.) Even at the level of total dimension, this sp ace is not symmetric
with respect to swapping d1 andd2, so it makes sense that we must treat intersection
points diﬀerently depending on whether we consider them to be morp hisms from
L(d1) to L(d2) or vice versa.
While we only discuss the product µ2 on Floer cohomology in this paper, it would be
possible to use this sort of perturbation in the deﬁnition of higher A∞ operations, and
to deﬁne a Fukaya category, by adapting the analogous construc tions in Abouzaid’s
work [1, 3].
MIRROR OF THE PROJECTIVE PLANE 29
3.3.5. Gradings and degrees. We now explain how the degrees of the intersection
points between the positively perturbed Lagrangians L(d) is determined. Our con-
ventions follow Seidel [41, §11]. We choose a smooth trivialization of the canonical
bundle of X(B) given by a complex volume form Ω. Our X(B) is diﬀeomorphic to
the manifold X ∨ considered in section 2, which carries the volume form
(56) Ω X ∨ = du ∧dv
w = du
u ∧ dw
w
having the convenient property that, away from the singular ﬁber of the Lefschetz
ﬁbration, Ω X ∨ decomposes as a wedge product of one-forms with respect to the local
product structure determined by the coordinates ( u,w ). We can transfer this form
over to X(B), and deform it to a complex volume form Ω that is compatible with
the ﬁbration structure, in the sense that, when Ω is restricted to the tangent space of
a point on a smooth ﬁber, it decomposes into a wedge product of a on e-form on the
vertical tangent space and a one-form on the horizontal space.
We can also describe the trivialization determined by Ω in terms of the f oliation by
the tori TR,λ. The tangent space to X(B) at any point is the complexiﬁcation of the
tangent space to the torus TR,λ passing through that point, so an orientation on TR,λ
trivializes the canonical bundle of X(B) along that torus. Since all of these tori can
be oriented in a consistent manner, we obtain a trivialization of the ca nonical bundle
over the complement of the critical point in X(B). This trivialization is homotopic
to the one determined by Ω for the following reason. The holomorphic volume form
Ω X ∨ on X ∨ admits a family of special Lagrangian tori, which means precisely that
Ω X ∨ restricted to each torus is a real volume form times a constant pha se factor.
When we transfer Ω X ∨ over to X(B), this foliation by special Lagrangian tori goes
over to a foliation by tori that is isotopic to the foliation by the tori TR,λ. (The fact
that the tori are Lagrangian is not important here, only that they are totally real.)
The foliation by the tori TR,λ is also compatible with the ﬁbration structure, as each
torus ﬁbers over a circle in the base X(I) and intersects each ﬁber in a circle. Thus
we obtain foliations by circles on the base and the ﬁber.
The point of these choices is that we will be able to compute the degre es of our
intersection points in terms of amounts of rotation with respect to the circle foliations
on the base and the ﬁber. Because the Lagrangian L(d) satisﬁes H 1(L(d)) = 0, it
admits gradings. Moreover, because it ﬁbers over a path in the bas e, and consists of
a path in each ﬁber, it may be graded separately in the base and ﬁber directions. To
say what we mean by this, recall the notion of a squared phase map from [41]. This
is the map
(57) αL(d) :L(d) →S1, α L(d)(p) = Ω(v1 ∧v2)2
|Ω(v1 ∧v2)|2
where {v1,v 2} is a basis ofTpL(d). A grading is then a real-valued lift ˜αL(d) :L(d) → R
such that exp(2 πi ˜αL(d)) = αL(d). In our situation, we can decompose this squared
phase map into base and ﬁber components
(58) αb
L(d), αf
L(d) :L(d) →S1
such that αL(d) = αb
L(d) ·αf
L(d), such that αb
L(d) is the squared phase with respect to
the foliation by circles on the base, and αf
L(d) is the squared phase with respect to the
30 JAMES PASCALEFF
foliation by circles on the ﬁber. Normalizing and homotoping the volume form Ω if
necessary, we may assume that the squared phase of the torus TR,λ is 1 ∈ S1 for all
three versions, and so that the squared phase of L(0) is −1 ∈S1 for both αb and αf
(and hence its total phase is α = 1).
Now, if we set d> 0, and we consider L(d), we ﬁnd that the tangent space of L(d),
in either the base or ﬁber, is obtained from that of TR,λ by a small counterclockwise
rotation. This means that αb
L(d) and αf
L(d) lie on the upper half circle between 1 and
−1 in S1.
Next, choose lifts ˜αb and ˜αf for the base and ﬁber squared phase maps of the
manifolds L(d) for d ≥ 0, preferring values the interval [0 , 1]. Note that L(0) has
(59) ˜ αb
L(0) = ˜αf
L(0) = 1
2
For the other L(d) with d> 0 the value of ˜αb
L(d) will always lie in the interval (0 , 1
2),
while the value of ˜αf lies in the interval (0, 1), since the intersection of L(d) with any
ﬁber is always a path that is transverse to the foliation by circles.
Finally, with the gradings in place, we can compute the degrees of the intersection
points between L(0) and L(d) for d> 0.
Proposition 3.5. Supposed1 <d 2. The the Floer complex CF ∗(L(d1),L (d2)) of the
positively perturbed pairL(d1),L (d2) is concentrated in degree zero. The Floer complex
CF ∗(L(d2)),L (d1)) for the positively perturbed pair L(d2),L (d1) is concentrated in
degree two.
Proof. Let us ﬁrst consider the case d1 = 0 and d2 =d> 0. Using the local splitting
given by the ﬁbration, this degree is a sum of contributions from the base and ﬁber.
Since the base and ﬁber are complex one-dimensional, the base and ﬁ ber contributions
are for p ∈L(0) ∩L(d) using [41, Eq. 11.35],
ib(L(0),L (d),p ) = [ ˜αb
L(d) − ˜αb
L(0)] + 1(60)
if (L(0),L (d),p ) = [ ˜αf
L(d) − ˜αf
L(0)] + 1(61)
d where [ ·] denotes the greatest integer function. Look at the diagram sho ws that,
at any intersection point p, the quantity inside the [ ·] is negative, as the tangent
space to L(d) is a small clockwise rotation of the tangent space to L(0). Thus both
ib(L(0),L (d),p ) and if (L(0),L (d),p ) are zero, and the total degree is zero.
If we keep d> 0, but swap the roles of L(0) and L(d), we ﬁnd that
ib(L(d),L (0),p ) = [ ˜αb
L(0) − ˜αb
L(d)] + 1 = 1(62)
if (L(d),L (0),p ) = [ ˜αf
L(0) − ˜αf
L(d)] + 1 = 1(63)
so that the intersection point p, regarded as a morphism from L(d) toL(0), has degree
2.
A similar analysis shows that the degrees of intersections L(d1) ∩L(d2), regarded
as a morphism from L(d1) to L(d2), depends on d2 −d1. If d2 −d1 is positive, they
have degree 0, while if d2 −d1 is negative, they have degree 2. □
Since, in each case, the complex is concentrated in a single degree, t he diﬀerential
vanishes, and we may identify the complex CF ∗(L(d1),L (d2)) with its cohomology
HF ∗(L(d1),L (d2)).
MIRROR OF THE PROJECTIVE PLANE 31
3.3.6. Intersection points and integral points. With the above prescription for per-
turbing the Lagrangians L(d), we now work out the bijection between the intersection
points of L(0) and L(d) for d> 0, regarded as morphisms from L(0) to L(d), and the
(1/d)-integral points of B.
Proposition 3.6. Let B be scaled so that the top face has length 2. Take d > 0.
Then the intersection points L(0) ∩L(d) giving a basis of CF 0(L(0),L (d)) correspond
to (1/d)-integral points of B, including those on the boundary of B. For d <0, the
intersection points giving a basis of CF 2(L(0),L (d)) correspond the same set but with
points on the boundary of B excluded. For the pair L(d1),L (d2), the same conclusion
holds with d =d2 −d1.
This proposition is proved by explicitly indexing all of the various points . We start
at the intersection point of ℓ(0) and ℓ(d) near the inner radius of the annulus X(I).
This intersection point survives the perturbation. In the ﬁber ove r this point there
is one intersection point that survives after perturbation. As we t ransport around
the inner part of the annulus, we pick up half-twists in the ﬁber (Pro position 3.4),
which increases the number of intersection points by one after eve ry two turns in the
base. This pattern continues until ℓ(d) reaches the middle radius and starts winding
around the other side of the Lefschetz singularity, where the pat tern reverses. (See
Figure 5.)
Assign the rational numbers
[−1, 1] ∩ (1/d)Z = {−1, −(d − 1)/d,..., −1/d, 0, 1/d,..., 1}
to the intersection points of ℓ(0) and ℓ(d), then over the point indexed by a/d the
number of intersection points in the ﬁber is 1 +
⌊
d−|a|
2
⌋
. We index the points in a
given ﬁber using the index i ∈ {0, 1,...,
⌊
d−|a|
2
⌋
}, starting at the top of the ﬁber.
If we scaleB so that the top face has aﬃne length 2, the 1 /d integral points of B are
also organized by the projection η :B →I into columns indexed by [ −1, 1] ∩ (1/d)Z.
By inspection, the column over a/d has 1 +
⌊
d−|a|
2
⌋
points. These are also indexed by
i ∈ {0, 1,...,
⌊
d−|a|
2
⌋
}, starting at the top of the ﬁber.
Under this bijection the (1 /d)-integral points on the boundary of B correspond to
intersections of the unperturbed L(0) andL(d) that lie on the boundary of X(B). Ac-
cording to our deﬁnition of positive perturbation, these points do ( do not) contribute
when d> 0 (d< 0).
Deﬁnition 4. Take d > 0. For a ∈ {−d,...,d }, and i ∈ { 0, 1,...,
⌊
d−|a|
2
⌋
}, let
qa,i(n) ∈L(n) ∩L(n +d) be the intersection which lies in the column indexed by a/d,
and which is the ith from the top of the ﬁber.
We can already verify mirror symmetry at the level of the Hilbert poly nomial:
(64) |L(0) ∩L(d)| =
⏐⏐⏐⏐B
(1
d Z
)⏐⏐⏐⏐ = (d + 2)(d + 1)
2 = dimH 0(CP2, OCP2(d))
Figure 7 shows the points of B( 1
4Z) representing the basis of morphisms L(d) →
L(d + 4).
32 JAMES PASCALEFF
Figure 7. The 1/4–integral points of B.
3.3.7. Hamiltonian isotopies. There is an alternative way to express the relationship
between L(d) and L(0), which is by a Hamiltonian isotopy. There is a Hamiltonian
function H on X(B) such that the time- d ﬂow of H takesL(0) to L(d). During the
intermediate times of this isotopy the Lagrangian will not be admissible (or even close
to it), but at the end of the isotopy admissibility is restored. This obs ervation is used
when we consider wrapped Floer cohomology in section 7.
This isotopy also allows us to identify the intersection points L(n) ∩L(n +d) for
diﬀerent values of n. For this reason, we will write qa,i(n) as simply qa,i.
