---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-008-6-a-few-simple-consequences-concerning-critical
section_title: "A few simple consequences concerning critical knots"
section_number: 6
pages: 23-25
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
The main result of the paper states that critical points of the generalized integral Menger cur-
vature intM(p,2) are not only smooth, which was known before, cf. [BR15, Theorem4], but also
analytic. Recalling and employing special properties for analytic functions, we hence decude a
few simple corollaries for critical knots ofintM(p,2) and some other knot energies.
The following statements hold for any functionalE :C0(R/Z, R3)→(0,∞] whose (arc-length
parametrized) critical points with respect to ﬁxed length are analytic. As a consequence, the
results also apply to the generalized integral Menger curvatureintM(p,2) and some of O’Hara’s
knot energies, cf. [BV19, Vor20].
Central to these consequences is a real version of the identity theorem. It is a well-known
result for analytic functions which easily carries over to the periodic case:
Proposition 6.1. If two analytic functions on R/Z are identical at inﬁnitely many distinct
points, they are identical everywhere.
Proof. Let γ,η: R/Z→R3 be analytic and without loss of generalityt1 <t 2 <...∈[0, 1) such
thatγ(ti) =η(ti) for alli∈N. Deﬁneg,h : (−1, 2)→R3 as the restrictions ofγandηto (−1, 2)
which are clearly also analytic. Asti∈[0, 1] for alli∈N, we have a subsequence converging to
t0∈[0, 1]⊆(−1, 2), so by [KP02, Corollary 1.2.7],g =h and thusγ=η.
Lemma 6.2. Letγ: R/Z→R3 andF : R3→R both be analytic. Then,F◦γeither has ﬁnitely
many roots or is uniformly zero.
Proof. F◦γ: R/Z →R is analytic as a composition of analytic functions (see e.g. [KP02,
Proposition 2.2.8]). Using the zero function in Proposition 6.1,F◦γeither is uniformly zero or
has only ﬁnitely many roots.
Proposition 6.3. Let γ∈C1(R/Z, R3) be a simple curve parametrized by arc-length which is
a critical point ofE. Then, it is the unknot or it has only ﬁnitely many intersections with any
hyperplane or sphere inR3. In particular,γcannot have straight segments.
Proof. First of all, let us consider any hyperplane with normal vectorn ∈R3 and position
vector x0∈R3, described by the equationF (x) = 0, whereF : R3→R, F (x) =⟨n,x−x0⟩.
Furthermore, letγ: R/Z→R3 be a critical point ofE that is simple and parametrized by arc-
length. We then observe that bothF andγare analytic, which is why we can apply Lemma 6.2
and observe that the curveγeither intersects the hyperplane ﬁnitely many times or is entirely
23
contained therein. In the latter case we obtain the unknot, which is the only simple planar knot,
cf. [CF77, p. 5] or [New51, Chapter VI, 18.]. Ifγcontains a straight segment, this segment is in
particular contained in two distinct hyperplanes. Thus, the whole curve has to be contained in
both hyperplanes and therefore has to be a straight line which is impossible for a closedC1-curve
of ﬁnite length.
We then turn our focus to any sphere with centerx0∈R3 and radiusr >0, described by
the equationF (x) = 0, whereF : R3→R, F (x) =|x−x0|2−r2. Therefore, similarly to the
hyperplane, Lemma 6.2 gives us that any critical analytic knotγofE either intersects the sphere
ﬁnitely many times or is entirely contained therein.
In the second case, we would intuitively expect to obtain the unknot by applying a stereo-
graphic projection from the sphere to the plane and then argue as above. To make this rigorous,
we need to construct an ambient isotopy, cf. [Hir76, Chapter 8.1], to avoid any kind of self-
intersection or pull-tight phenomena during the projection process. To simplify the upcoming
computations, we assume that the sphere is the unit sphere centered in the origin and that the
knot γon the sphere does not intersect the north pole of the sphere. We omit the proof that
translations and dilations of the sphere do not change the knot type of the spherical knot and
remark that stereographic projections can be done from any other point on the sphere as well.
The existence of such point on the sphere, which the knotγdoes not intersect, is ensured due to
the fact thatγis rectiﬁable. Furthermore, note that since the curveγis continuous, there exists
an r> 0 such thatγdoes not intersect a ball around the north pole with radiusr.
We begin with constructing aC1-isotopy fromγto the stereographic projection ofγfrom
the north pole onto the planez = 0 denoted by ˜γ. Note that ˜γis indeed a C1-embedding:
As γ∈Cω(R/Z, R3) is a diﬀeomorphism onto its image and the stereographic projection
P : S2\ (0, 0, 1) →R2 given by P (x,y,z ) = ( x
1−z, y
1−z ) with inverse function P−1(u,v ) =
1
u2+v2+1(2u, 2v,u 2 +v2−1) is a diﬀeomorphism from the sphere without the north pole to the
plane z = 0, also ˜γ∈C1(R/Z, R3) is diﬀeomorphic onto its image. We then deﬁne the map
h : R/Z×[0, 1]→R3 by
ht(w) := (1−t)γ(w) +t˜γ(w),
which is continuously diﬀerentiable in time and space.
To see thath is aC1-isotopy (cf. [Hir76, Section 8.1]), we construct a continuously diﬀeren-
tiable left-inverse of eachht and thus show thatht is aC1-embedding. First note that by the
nature of stereographic projection,ht(w) lies on the unique straight line passing through both
the north poleN andγ(w). Sinceγlies on the sphere and does not containN, this line does not
contain any other points ofγorh( ˜w, [0, 1]) for any ˜w⁄=w. This means that for anyx∈ht(R/Z),
we may obtainw =h−1
t (x) as γ−1(y), wherey =λN+ (1−λ)x with|y|= 1. Solving forλ∈R
yields eitherλ= 0, which we may safely ignore since it corresponds toy being the north pole,
orλ= |x|2−1
|x−N|2. Asx has to stay away from the north pole, we found aC1 right-inverse ofht and
so, h is aC1-embedding.
Obviously, also
h(·, 0) =γ and h(·, 1) = ˜γ
hold. Now by [Hir76, Section 8.1, Exercise 4] or [Bla09, Theorem 1.2], we can extend theC1-
isotopy betweenγand ˜γto an ambient isotopy ofR3 and therefore obtain that the knot type is
preserved throughout the stereographic projection.
As a direct consequence of Lemma 6.2 and Proposition 6.3, we obtain the following.
Corollary 6.4. Let γ∈C1(R/Z, R3) be a simple curve parametrized by arc-length which is
a critical point ofE and letF : R3→R be an analytic map that describes an implicit surface
24
F (x,y,z ) = 0. Then, the curveγeither is entirely contained in the implicit surfaceF (x,y,z ) = 0
or has only ﬁnitely many intersections with it. In particular, if the given surface is ambient
isotopic to a sphere or a hyperplane, the curveγis the unknot or has ﬁnitely many intersections
with the surface.
Corollary 6.5. Letγ,ηbe critical points ofE which are parametrized by arc-length. As soon as
γ(t) =Aη(t) +x0
for ﬁxedA∈R3×3, x0∈R3, and inﬁnitely many distinctt∈[0, 1), we haveγ=Aη+x0.
Proof. Note that by assumption,γandηare analytic. Then, the statement follows from the fact
that Aη+x0 is analytic as well and applying Proposition 6.1.
Acknowledgements
Daniel Steenebrügge acknowledges support by the Deutsche Forschungsgemeinschaft (DFG, Ger-
man Research Foundation) – project number 320021702/GRK2326 –Energy, Entropy, and Dis-
sipative Dynamics (EDDy)and Nicole Vorderobermeier by the Austrian Science Fund (FWF),
Grant P29487. Funding from RWTH Aachen University for Nicole Vorderobermeier’s research
visit is also gratefully acknowledged.
In addition, the authors would like to sincerely thank Simon Blatt for his constant support
and indispensable discussions throughout the development of this research paper, Heiko von der
Mosel for his generous support and hospitality as well as fruitful discussions, from which Section
6 emerged, and Philipp Reiter for having a sympathetic ear for the authors and giving important
hints to deal with some ﬁlthy estimates in Section 4.2.
