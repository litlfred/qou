---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-031-73-fenchelnielsen-coordinates
section_title: "Fenchel–Nielsen coordinates"
section_number: 7.3
pages: 210-219
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
It is now time to ﬁx a global set of coordinates for the Teichmüller space
when g > 2. These are the Fenchel–Nielsen coordinatesand they identify
Teich(Sg) with R6g−6, more precisely withR3g−3
>0 × R3g−3.
7.3.1. The coordinates. We want to construct a parametrisation for
Teich(Sg) when g > 2. To identify a ﬁnite-dimensional vector space with
Rn one needs to ﬁx a basis; likewise, here the parametrisation depends on the
choice of a frame.
Let Sg be oriented. Aframe forSg consists of two essential multicurves
µ andν in minimal position, such that:
(1) the multicurveµ is a pants decomposition,
(2) the multicurveν decomposes every pair-of-pants in two hexagons.
An example that generalises easily to any genusg≥ 2 is shown in Figure
7.8. The pants decompositionµ =γ1⊔... ⊔γ3g−3 consists of3g− 3 curves,
while the number of curves inν is not ﬁxed a priori and depends on our choice
ofν. We now show that a frame induces aFenchel–Nielsenmap
FN : Teich(Sg)−→ R3g−3
>0 × R3g−3
m↦−→(l1,...,l 3g−3,θ 1,...,θ 3g−3).
The map FN is deﬁned as follows. Letm∈ Teich(Sg) be a hyperbolic met-
ric. The 3g− 3 length parametersli = 𝓁γi (m) are deﬁned using the length
functions: the multicurveµ has a unique geodesic representative
¯µ = ¯γ1⊔... ⊔ ¯γ3g−3
in the metricm by Corollary 6.3.23, andli is the length of¯γi. Note that these
parameters depend only onµ and not onν.
The torsion anglesθi are more subtle to deﬁne: the geodesic multicurve
¯µ decomposes Sg into geodesic pairs-of-pants, and the angle θi measures
somehow the way the two geodesic pairs-of-pants are glued along the closed
geodesic ¯γi. The precise deﬁnition ofθi needs the auxiliary multicurveν.
7.3. FENCHEL–NIELSEN COORDINATES 203
Figure 7.9. A closed geodesic ¯γ1 and the two adjacent pairs-of-pants.
The torsion parameterθ1 measures the distance (in the universal covering)
between two orthogeodesics (coloured in green) via the formulaθi = 2πsi
li
.
We ﬁxi = 1 for simplicity and deﬁneθ1. Figure 7.9-(left) shows the two
geodesic pants adjacent to¯γ1 (they might coincide). The second multicurve
ν intersects these pants in four blue arcs, two of whichλ,λ′ intersect ¯γ1: we
pick one, sayλ. We ﬁx a lift˜P∈ H2 ofP = ¯γ1∩λ and we lift all the curves
incident toP: the geodesic¯γ1 lifts to a line˜γ1 andλ lifts to a (non-geodesic)
curve ˜λ that connects two lifts˜γ2 and ˜γ3 of the closed geodesics¯γ2 and ¯γ3.
See Figure 7.9-(right).
We draw as in the ﬁgure the unique orthogeodesics connecting˜γ1 to ˜γ2
and ˜γ3 and we denote bys1 the signed length of the segment in˜γ1 comprised
between these two orthogeodesics, with positive sign if (as in the ﬁgure) an
observer walking on a orthogeodesic towards˜γ1 sees the other orthogeodesic
on its left (here we use the orientation ofSg).
By repeating this construction for each¯γi we ﬁnd some real numberssi.
Finally, the torsion parameterθi is
θi = 2πsi
li
.
Theorem 7.3.1 (Fenchel-Nielsen coordinates).The mapFN is well-deﬁned
and is a bijection.
Proof. We ﬁrst note that in the deﬁnition of the torsion parameters we
could have chosenλ′ instead ofλ. We would have obtained the same length
si as shown in Figure 7.10. Moreover a hyperbolic metricm′ isometric tom
through a diﬀeomorphismϕ isotopic to the identity has the same parameters
li andθj since they depend only on the isotopy classes ofµ andν. Therefore
FN is well-deﬁned.
We prove thatFN is surjective. For every vector(l1,...,l 3g−3)∈ R3g−3
>0
we may use Proposition 6.2.1 and construct a metric onSg by assigning to
eachpair-of-pantsofthepantsdecomposition µthe(unique)hyperbolicmetric
204 7. TEICHMÜLLER SPACE
Figure 7.10. If we pickλ′ instead ofλ we ﬁnd a segment of the same
lengths1. This holds because the two geodesic pairs-of-pants incident to
γ1 decompose into two hexagons isometric toA andB as shown, and the
sides ofA and B contained in ˜γ1 have the same lengthl(γ1)
2 , that is half
the length ofγ1.
with boundary lengthsli. We get a metric with some arbitrary torsion angles
θ, which can be changed arbitrarily by an earthquake alongµ: it is easy to
check that an earthquake with anglesθ′ changes the torsion angles fromθ to
θ +θ′, hence any torsion parameter can be realised andFN is surjective.
We prove thatFN is injective. IfFN(m) = FN(m′), up to acting via earth-
quakes we may suppose that FN(m) = FN( m′) = ( l1,...,l 3g−3, 0,..., 0).
Since the torsion parameter is zero, the orthogeodesics in Figure 7.9-(right)
match and project inSg to a geodesic multicurve ¯ν isotopic to ν and or-
thogonal to ¯µ. ThereforeSg\ (¯µ∪ ¯ν) is a tessellation ofSg into right-angled
hexagons, determined by the lengthsli. Both metricsm andm′ have the same
tessellation and are hence isometric, via an isometry which is isotopic to the
identity. □
Remark7.3.2. Asshownintheproof, thetorsionparametersfor m arezero
if and only if the geodesic representatives¯ν and ¯µ ofν andµ are everywhere
orthogonal.
7.3.2. Length functions of 9g− 9 curves. It is now natural to ask
whether the length functions determine every point inTeich(Sg). The an-
swer is positive; as usual, to warm up we start by examining the torus.
Letγ,γ′ be two simple closed curves in the torusT withi(γ,γ′) = 1 and
letγ′′ =Tγ(γ′) be obtained by Dehn twistingγ′ alongγ, see Figure 7.11.
Proposition 7.3.3. The map
L: Teich(T )−→ R3
>0
m↦−→
(
𝓁γ(m),𝓁γ′
(m),𝓁γ′′
(m)
)
7.3. FENCHEL–NIELSEN COORDINATES 205
g g'
g''
g
g' g''
Figure 7.11. The curvesγ (red),γ′ (blue), andγ′′ =Tγ(γ′) (green) on
the torus.
gi gi '
gi ''
Figure 7.12. The curvesγi (red), γ′
i (blue), andγ′′
i =Tγi (γ′
i ) (green)
when γi is adjacent twice to the same pair of pants. It is an instructive
exercise to drawγ′
i andγ′′
i whenγi is incident to distinct pair of pants.
is injective.
Proof. After ﬁxingγ and γ′ as a homology basis, we haveγ = (1, 0),
γ′ = (0, 1), andγ′′ = (1,−1). Proposition 7.2.5 gives
L(z) =
( 1√
ℑz, |z|√
ℑz,|z− 1|√
ℑz
)
which is easily seen to be injective onTeich(T ) =H2. □
A similar set of 9g− 9 curves does the job onSg when g > 2. Let
µ =γ1⊔... ⊔γ3g−3 be a pants decomposition forSg. For eachγi we choose
a curveγ′
i as in Figure 7.7, and we indicate byγ′′
i =Tγi (γ′
i ) the curve obtained
by Dehn-twistingγ′
i alongγi, see an example in Figure 7.12.
Proposition 7.3.4. The map
L: Teich(Sg)−→ R9g−9
>0
m↦−→
(
𝓁γi (m),𝓁γ′
i (m),𝓁γ′′
i (m)
)
is injective.
Proof. We composeL with FN−1 and obtain a map
L◦ FN−1 : R3g−3
>0 × R3g−3−→ R9g−9
>0
(li,θi ) ↦−→(li,l′
i,l′′
i )
206 7. TEICHMÜLLER SPACE
l
f( )l a
r
s
r
b
Figure 7.13. Pick a segment of lengthl and draw two perpendiculars
at the endpoints: this determines a quadrilateral with two ideal vertices;
let f (l) be the distance between the opposite sidesl and r (left). A
geodesic pair-of-pants is the union of two isometric hexagons, which form
in H2 a right-angled octagon as drawn. The picture shows that the closed
boundary geodesicsa and b have disjointf (a) and f (b)-neighbourhoods,
coloured here in yellow (right).
We prove that it is injective: it suﬃces to consider the case where the values
li are ﬁxed andθi vary. Note thatγ′
i and γ′′
i intersect γj if and only ifi =j:
hencel′
i andl′′
i depend only onθi and not on the other torsion parametersθj.
Proposition 7.2.10 says thatl′
i =f (θi ) is strictly convex and Proposition 7.2.4
givesl′′
i =f (θi + 2π). A strictly convex proper functionf : R→ R is at most
2 to 1, hence the function
R−→ R× R
θi↦−→
(
f (θi ),f (θi + 2π)
)
is injective. ThereforeL is injective. □
7.3.3. Collar lemma.The thick-thin decomposition theorem implies that
the closed geodesics of length smaller than a Margulis constantε2 on a com-
plete hyperbolic surface are simple and have disjointR-neighbourhoods (see
Corollary 4.2.16). When the curves are very short, one may chooseR to be
very large: this fact is called thecollar lemmaand we prove it directly using
elementary tools.
For any numberl >0, draw the quadrilateral as in Figure 7.13-(left) and
deﬁnef (l) to be the distance between its opposite sidesl andr.
Exercise 7.3.5. The functionf : R>0→ R>0 is strictly decreasing and a
homeomorphism. In particular we getliml→0f (l) =∞. Explicitly, we have
sinhf (l) = 1
sinh l
2
.
Hint. Putl in vertical position inH2 and use Lemma 5.2.7. □
7.3. FENCHEL–NIELSEN COORDINATES 207
The functionf is simple to deﬁne, and is particularly useful.
Proposition7.3.6. LetP beageodesicpair-of-pantswithboundarylengths
a,b, andc. Thef (a), f (b), andf (c)-neighbourhoods of the boundary com-
ponents form three disjoint collars.
Proof. Consider two boundary componentsa andb. The geodesic pair-of-
pantsP is divided into two isometric hexagons, and we lift them toH2 where
they form a right-angled octagon as in Figure 7.13-(right). The picture shows
that thef (a) andf (b)-neighbourhoods ofa andb are disjoint. □
Here is the collar lemma.
Lemma 7.3.7 (Collar lemma).Letg> 2 andSg have a hyperbolic metric.
Disjoint simple closed geodesicsγ1,...,γ k of length l1,...,l k have disjoint
tubularf (li )-neighbourhoods.
Proof. We may suppose (by adding more simple closed geodesics if neces-
sary) that the closed geodesics form a pants decomposition, and it suﬃces to
consider two curves that cobound the same pair-of-pants. Proposition 7.3.6
applies. □
We recall from Corollary 4.2.16 that every closed geodesic shorter than
ε2 is simple. Therefore very short closed geodesics are simple and have large
disjoint tubular neighbourhoods: the more we shrink the curves, the larger are
their neighbourhoods, and hence the larger is the diameter of the surface (the
diameter of a metric space is the supremum of the distance of its points). In
particular, if on a sequence of closed hyperbolic surfaces the injectivity radius
tends to zero, their diameters must tend to inﬁnity.
Among the many consequences of the collar lemma, we focus on a simple
inequality which relates the geometric intersection of simple closed geodesics
to their lengths. We denote byL(γ) the length ofγ.
Corollary 7.3.8.Letg> 2 andSg have a hyperbolic metric. Letγ andη
be two simple closed geodesics inSg. The following inequality holds:
L(η)> 2i(η,γ )·f (L(γ)).
Proof. The geodesicγ has a tubularf (L(γ))-neighbourhood. The geo-
desicη intersectsγ ini(η,γ ) points and hence crosses the tubular neighbour-
hood at leasti(η,γ ) times, each with a segment of length> 2f (L(γ)). □
7.3.4. A topology for the Teichmüller space.There are various equiv-
alent ways to assign a topology to the Teichmüller space. On the torusT,
we have seen thatTeich(T ) can be identiﬁed with the hyperbolic planeH2,
and the mapping class group acts as isometries on it: we could not hope for
a better picture ofTeich(T ) and we are fully satisﬁed.
208 7. TEICHMÜLLER SPACE
When g> 2 we could similarly use the Fenchel-Nielsen coordinates and
give Teich(Sg) the topology ofR6g−6, but then to be honest we should also
checkthatthetopologydoesnotdependontheframe... weprefertoequipthe
Teichmüller space with an intrinsic topology and then prove that the Fenchel-
Nielsen coordinates are homeomorphisms.
We indicate by S = S (Sg) the set of all the non-trivial simple closed
curves inSg, considered up to isotopy and orientation reversal (we say that
the curves areunoriented). Each elementγ∈ S induces a length function
𝓁γ : Teich(Sg)−→ R>0.
We indicate as usual withRS the set of all functionsS → R and give it
the usual product topology (the weakest one such that all the projections are
continuous). The natural map
Teich(Sg)−→ RS
m↦−→
(
γ↦−→𝓁γ(m)
)
is injective by Propositions 7.3.3 and 7.3.4. We may hence considerTeich(Sg)
as a subspace ofRS and assign it the subspace topology. This topology on
Teich(Sg) is the weakest one where the length functions𝓁γ are continuous.
Recall that a topological space issecond-countable if it has a countable base.
Proposition 7.3.9. The space RS is Hausdorﬀ and second-countable.
Proof. Every product of Hausdorﬀ spaces is Hausdorﬀ, and every count-
able product of second-countable spaces is second-countable. □
We recall the following topological fact.
Proposition 7.3.10. Let f : X→ Y be a continuous and proper map be-
tween topological spaces. IfY is Hausdorﬀ and second-countable thenf is
closed.
Proper maps onto reasonable spaces are closed. If they are also injective,
we can obtain more.
Corollary 7.3.11. Let f : X → Y be a continuous, proper, and injective
map between topological spaces. IfY is Hausdorﬀ and second-countable then
f is a homeomorphism onto its image.
We will use this corollary in a moment. Recall that every isometryϕ∈
Isom+(H2) = PSL2(R)has a tracetrϕdeﬁned only up to sign, whose modulus
is> 2 precisely whenϕ is hyperbolic, see Proposition 2.3.9.
Proposition 7.3.12. Let S = H2/Γ be an orientable hyperbolic surface.
Every hyperbolic transformationϕ∈ Γ produces a closed geodesicγ inS with
|trϕ| = 2 coshL(γ)
2 .
7.3. FENCHEL–NIELSEN COORDINATES 209
Proof. Up to conjugacy we haveϕ(z) =eL(γ)z. The matrix is
ϕ =
(
e
L(γ)
2 0
0 e−L(γ)
2
)
hence|trϕ| = 2 cosh L(γ)
2 . □
In particular, the length ofγ depends continuously on the transformation
ϕ. We will use this fact to prove the following. We supposeg> 2.
Proposition 7.3.13. The Fenchel-Nielsen map
FN : Teich(Sg)−→ R3g−3
>0 × R3g−3
is a homeomorphism.
Proof. We considerTeich(Sg) inside RS and examine the inverse map
FN−1 : R3g−3
>0 × R3g−3−→ RS.
We prove thatFN−1 is continuous. The mapFN−1 assigns to the param-
eters (li,θi ) a metric onSg constructed by attaching right-angled hexagons.
Both the hexagons and the attaching maps depend continuously on the pa-
rameters (li,θi ) and lift to a tessellation ofH2 into hexagons. Since the de-
composition into hexagons varies continuously, its deck transformations vary
continuously in PSL2(R) and hence the length functions too by Proposition
7.3.12. Therefore FN−1 is continuous.
We prove thatFN−1 is proper. Take a diverging sequence of parameters
(li,θi ) (that is, without converging subsequences) inR3g−3
>0 × R3g−3: we need
to show that its image is also a diverging subsequence. The thesis is equivalent
to show that the length function of some curve goes to inﬁnity. Ifli→ +∞ for
somei we are done. Ifli→ 0, the length of any curve intersecting essentially
the shrinking curveγi goes to inﬁnity by Corollary 7.3.8. It remains to consider
the case where the length parametersli converge to some non-zero value, but
some twist parameterθj goes to inﬁnity: in that case the length of any curve
intersecting the twisted curveγj goes to inﬁnity by Proposition 7.2.10.
Finally, the map FN−1 is a homeomorphism onto its image by Corollary
7.3.11. The proof is complete. □
During the proof we have also discovered the following.
Proposition 7.3.14. If a sequence mi ∈ Teich(Sg) diverges, there is a
γ∈ S such that𝓁γ(mi )→∞ on a subsequence.
Recall that the action of a topological groupG on a topological spaceX
is continuous if the action mapG×X→X is continuous. This implies thatG
acts onX by homeomorphisms. We give the mapping class groupMCG(Sg)
the discrete topology.
210 7. TEICHMÜLLER SPACE
Proposition 7.3.15. The earthquakes and mapping class group actions on
the Teichmüller space are continuous.
Proof. The mapping class group acts onS by permutations, hence its
action on RS is continuous. On Fenchel-Nielsen coordinates the earthquake
action sendsθ toθ +θ′ and is hence continuous. □
The immersion inR9g−9 is also a topological embedding.
Proposition 7.3.16. The injective representationTeich(Sg)↪→ R9g−9 fur-
nished by Proposition 7.3.4 is a homeomorphism onto its image.
Proof. Using Fenchel-Nielsen coordinates the map is clearly continuous.
The proof that it is proper is as in Proposition 7.3.13. □
7.3.5. Surfaces of ﬁnite type.We have considered only closed surfaces
Sg for simplicity, but most of the arguments exposed in this chapter extend
easily to all surfacesSg,b,p of ﬁnite type with negative Euler characteristic.
The Teichmüller spaceTeich(Sg,b,p ) is the set of all the complete hyper-
bolic metrics with geodesic boundary, considered up to isometries that are
isotopic to the identity. Fenchel-Nielsen coordinates are deﬁned analogously:
the surface decomposes into−χ(Sg,b,p ) = 2g +b +p− 2 pairs-of-pants, and
the interior curves of the decomposition are
1
2
(
3(2g +b +p− 2)−b−p
)
= 3g +b +p− 3.
The Fenchel-Nielsen coordinates are
(
l1,...,l 3g+b+p−3,l∂
1,...,l ∂
b,θ 1,...,θ 3g+b+p−3
)
where theli and l∂
j are the length parameters of the3g +b +p− 3 interior
andb boundary curves, and theθi are the torsion angles of the interior curves.
We get a bijection
FN : Teich(Sg,b,p )−→ R3g+2b+p−3
>0 × R3g+b+p−3
whichisahomeomorphismwithrespecttothenaturaltopologyonTeichmüller
space as a subset ofRS. Therefore the Teichmüller space is homeomorphic
to a ball of dimension−3χ(Sg,b,p )−p.
For instance, the Teichmüller space of a pair-of-pants isR3
>0 parametrized
by the lengths of the boundary geodesics, while that of a thrice-punctured
sphere is a point (there is a unique metric).
An alternative description of the Teichmüller space for punctured surfaces,
with ideal triangles playing the role of pairs-of-pants, is described in the next
section.
