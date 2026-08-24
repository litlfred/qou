---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-005-22-the-topology-of-the-map-w
section_title: "The topology of the map W"
section_number: 2.2
pages: 16-19
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
tentialW given by (9) has three critical points
(40) Crit( W ) = {(v =eΛ /3e2πi(n/3),w = 1) |n = 0, 1, 2},
and corresponding critical values
(41) Critv( W ) = {3e−Λ /3e−2πi(n/3) |n = 0, 1, 2}.
As expected, Critv(W ) is the set of eigenvalues of quantum multiplication byc1(T CP2)
in QH ∗(CP2), that is, multiplication by 3 h in the ring C[h]/⟨h3 =e−Λ ⟩.
Proposition 2.3. Any regular ﬁber W −1(c) ⊂X ∨ is a twice-punctured elliptic curve.
Proof. In the (u,v ) coordinates, W −1(c) is deﬁned by the equation
(42) u + e−Λv2
uv − 1 =c,
(43) u(uv − 1) +e−Λv2 =c(uv − 1).
This is an aﬃne cubic plane curve, and it is disjoint from the aﬃne conic {uv −1 = 0 }.
It is smooth as long as c is a regular value.
The projective closure of W −1(c) in (u,v ) coordinates is given by the homogeneous
equation (with ξ as the third coordinate)
(44) u(uv −ξ2) +e−Λv2ξ =cξ(uv −ξ2).
MIRROR OF THE PROJECTIVE PLANE 17
This is a projective cubic plane curve, hence elliptic, and it intersects the line at
inﬁnity {ξ = 0} when u2v = 0. So it is tangent to the line at inﬁnity at ( u :v :ξ) =
(0 : 1 : 0) and intersects it transversely at ( u : v : ξ) = (1 : 0 : 0). Hence the aﬃne
curve is the projective curve minus these two points. □
Remark 1. The function W above is to be compared to the “standard” superpotential
for CP2, namely,
(45) W =x +y + e−Λ
xy
corresponding to the choice of the toric boundary divisor, a union o f three lines, as
anticanonical divisor. This W has the same critical values, and its regular ﬁbers are
all thrice-punctured elliptic curves. Hence smoothing the anticano nical divisor to the
union of a conic and a line corresponds to compactifying one of the pu nctures of
W −1(c).
2.3. Tropicalization in a singular aﬃne structure. Our goal is to ﬁnd the same
aﬃne manifold B (that comes from symplectic structure of CP2 \D) embedded in the
base of the torus ﬁbration on X ∨, equipped with the complex aﬃne structure. We
shall see that it is obtained as a bounded chamber inside a particular t ropical curve,
the tropicalization of the ﬁber of W .
For some real number ǫ> 0, consider the curve W −1(eǫΛ ):
(46) W =u + e−Λv2
w =eǫΛ
The tropicalization corresponds to the limit Λ → ∞ , or t :=e−Λ → 0. The amoeba
of A(W −1(t−ǫ)) is the image of the curve in the aﬃne base of the torus ﬁbration on
X ∨. We want to produce a tropical curve in the base that reﬂects the asymptotic
geometry of these amoebas A(W −1(t−ǫ)) as t → 0. In the standard situation, this is
done by rescaling the amoebas by log t and taking the Hausdorﬀ limit. Our situation
is not standard because the aﬃne manifold in which our tropical curv e is to live has a
singularity. Thus, none of the standard tropicalization techniques [26] apply directly.
Since we do not know of any general theory of tropicalization when t he aﬃne structure
is singular, we will here content ourselves with an ad hoc method involv ing explicit
computation in two coordinate charts, and checking that the resu lts ﬁt together in
the singular aﬃne structure.
In the standard picture of tropicalization, one considers a family of subvarieties of
an algebraic torus Vt ⊂ (C∗)n. The map Log : ( C∗)n → Rn given by Log(z1,...,z n) =
(log |z1|,..., log |zn|) projects these varieties to their amoebas Log(Vt), and the rescaled
limit of these amoebas is the tropicalization of the family Vt. The tropicalization is
also given as the non-archimedean amoeba of the deﬁning equation o f Vt.
The map Log : ( C∗)n → Rn is special Lagrangian ﬁbration. Its ﬁbers are the tori
{|z1| = r1,..., |zn| = rn}. These tori are Lagrangian with respect to the standard
symplectic form, and they are special with respect to the holomorp hic volume form
(47) Ω toric = dz1
z1
∧ · · · ∧dzn
zn
,
which has logarithmic poles along the coordinate hyperplanes in Cn. The complex
aﬃne coordinates are log |zi|.
18 JAMES PASCALEFF
The torus ﬁbration on X ∨ is approximated by this standard structure as follows.
Equation (29) shows that in the ( w,u ) coordinates (where u ⁄= 0), the holomorphic
volume form is standard. If the special Lagrangian ﬁbration were a lso standard,
the aﬃne coordinates would be (log |w|, log |u|). Proposition 2.2 shows that, while
η = log |w| is still an aﬃne coordinate (reﬂecting the fact that there is still an S1-
symmetry), the other aﬃne coordinate ξ is the average value of log |u| along a loop
in the ﬁber. We also see that as |λ| becomes large, the approximation ξ ≈ log |u|
holds with increasing accuracy. Similarly, in the ( w,v ) coordinates (when v ⁄= 0), the
holomorphic volume form is standard, and η = log |w| and ψ ≈ log |v| form aﬃne
coordinates.
We shall see that as t = e−Λ → 0, the amoebas A(W −1(t−ǫ)) move farther away
from the singularity, where the approximations ξ ≈ log |u| and ψ ≈ log |v| hold with
increasing accuracy, while η = log |w| holds exactly everywhere.
The approximations ξ ≈ log |u| andψ ≈ log |v| and the identity η = log |w| suggest
the approach to ﬁnding the tropicalization. We represent the equa tion W = u +
e−Λv2/w =eǫΛ as a polynomial equation in the coordinates ( w,u ) ∈ (C∗)2. We then
compute the corresponding tropical curve, using the standard p rocedures [26], and
we plot the result in the aﬃne plane whose coordinates are (log |w|, log |u|). This is
shown in Figure 3(a). We repeat the process in the coordinate syst em (w,v ), and plot
the resulting tropical curve in the aﬃne plane whose coordinates ar e (log |w|, log |v|).
This is shown in Figure 3(b). We then transfer these tropical curve s into the singular
aﬃne manifold by simply identifying ξ with log |u| and ψ with log |v|.
We now observe that the two curves actually match up, at least awa y from the
vertical line passing through the singularity, and we claim that the re sult is as depicted
in Figure 3(c). This is evident in comparing the left-hand portions of p arts (a) and
(b) of Figure 3. On the right-hand portion, we must take into accou nt that the
coordinate ψ ≈ log |v| has been aﬀected by a shear in passing from (b) to (c).
There is apparently a problem along the vertical line passing through the singular-
ity, since the curves depicted in (a) and (b) have vertical legs ther e, which we claim
do not appear in (c). Our reasoning is this: the coordinate system ( w,u ) ∈ (C∗)2
only covers the locus where u ⁄= 0, which is also where the function ξ is well deﬁned.
Thus we cannot expect the curve in (a) to be valid near the vertical going down from
the singularity, it is valid above the singularity. Conversely, the ﬁgur e in (b) is only
valid in the region below the singularity. Thus the extra vertical legs a re illusory.
We call the resulting tropical curve Tǫ.
Proposition 2.4. Forǫ> 0, Tǫ is a trivalent graph with two vertices, a cycle of two
ﬁnite edges, and two inﬁnite edges.
Proposition 2.5. For ǫ > 0, the complement of Tǫ has a bounded component that
is an integral aﬃne manifold with singularities that is isom orphic, after rescaling, to
the base B of the special Lagrangian ﬁbration on CP2 \D with the aﬃne structure
coming from the symplectic form.
Remark 2. The topology of the tropical curve Tǫ corresponds to that of a twice-
punctured elliptic curve.
Remark 3. We can apply the same patching procedure for ǫ in the range ( −1/3) <
ǫ< 0. This changes Figure 3 so that the triangles in (a) and (b) become s maller and
MIRROR OF THE PROJECTIVE PLANE 19
Figure 3. The tropical ﬁber of W for ǫ >0. (a) ( w,u ) coordinates.
(b) (w,v ) coordinates. (c) The tropical ﬁber Tǫ.
they lie entirely below point marked with ×. Thus, assuming that (a) is valid above
the singularity, while (b) is valid below the singularity, we ﬁnd that Tǫ is essentially
the same as what appears in (b), but that the vertical leg must ter minate at the
singularity, in order to be consistent with the fact that in (a) no par t of the curve
appears above the singularity. Thus we ﬁnd that Tǫ is a trivalent graph with three
vertices, a cycle of three ﬁnite edges, two inﬁnite edges and one ed ge connecting a
vertex to the singular point of the aﬃne structure.
We note that the value ǫ = −1/3 corresponds to the critical values of W .
Remark 4. This proposition is another case of the phenomenon, described in Ab ouzaid’s
paper [1], that for toric varieties, the bounded chamber of the ﬁbe r of the superpoten-
tial is isomorphic to the moment polytope. In the general case of a m anifold X with
eﬀective anticanonical divisor D, the boundary of the symplectic aﬃne base of the
torus ﬁbration on X \D corresponds to a torus ﬁber collapsing onto D, a particular
class of holomorphic disks having vanishing area, and the correspon ding term of the
superpotential having unit norm. On the other hand, the tropicaliz ation of the ﬁber
of the superpotential has some parts corresponding to one of th e terms having unit
norm, and it is expected that these bound a chamber which is isomorp hic to the base
of the original torus ﬁbration.
