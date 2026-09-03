---
doc_id: arxiv-0705.1468v1
doc_title: "Knots in the Skyrme-Faddeev model Paul Sutcliffe"
section_id: sec-002-rational-maps-torus-knots-and-links
section_title: "Rational maps, torus knots and links"
section_number: null
pages: 7-11
source_pdf: 0705.1468v1.pdf
source_sha256: 4ff578cb3657e4a4
doc_brief: "Knots in the Skyrme-Faddeev model Paul Sutcliffe — The Skyrme-Faddeev model is a modiﬁed sigma model in three-d imensional space, which has string-like topological solitons classiﬁed by th e"
---
Torus knots are classiﬁed by a pair ( a, b) of coprime positive integers with a > b. A knot
is a torus knot if it lies on the surface of a torus, in which cas e the integers a and b count
the number of times that the knot winds around the two cycles o f the torus. The simplest
example is the trefoil knot, which is the (3 , 2)-torus knot and has three crossings. In the
standard knot catalogue notation it is 3 1, where the number refers to the crossing number
of the knot and the subscript labels its position in the knot c atalogue. Other torus knots
7
which will be of interest in this paper include the (5 , 2)-torus knot, also known as Solomon’s
seal knot, which has ﬁve crossings (knot 5 1 in the catalogue), and the (4 , 3)-torus knot which
has crossing number eight (knot 8 19 in the catalogue). In general the ( a, b)-torus knot has
crossing number C = a(b − 1).
Denote by Ka,b any ﬁeld conﬁguration in which the position curve is an ( a, b)-torus knot.
Such a ﬁeld conﬁguration will have Hopf charge Q = C + T, where C = a(b − 1) is the
knot crossing number and the integer T counts the number of times that the linking curve
twists around the position curve (only situations where the orientation is such that T is
non-negative will be of relevance here). The main aim of this section is to construct ﬁelds
of type Ka,b for a large range of charges Q.
The ﬁrst step is to recall the standard description [3] of a to rus knot as the intersection
of a complex algebraic curve with the three-sphere. Conside r ( Z1, Z0) ∈ C2 and the unit
three-sphere S3 ⊂ C2 given by |Z1|2 + |Z0|2 = 1 . Then the intersection of this three-sphere
with the complex algebraic curve Z a
1 + Z b
0 = 0 is indeed the ( a, b)-torus knot.
To use the above description to produce a ﬁeld conﬁguration, the spatial coordinates
(x1, x2, x3) ∈ R3 are mapped to the unit three-sphere via a degree one spherica lly equivariant
map. Explicitly,
(Z1, Z0) = (( x1 + ix2) sin f
r , cos f + isin f
r x3), (3.1)
where r2 = x2
1 + x2
2 + x2
3 and the proﬁle function f (r) is a monotonically decreasing function
of the radius r, with boundary conditions f (0) = π and f (∞) = 0 . The precise form of this
function will be speciﬁed shortly.
A Riemann sphere coordinate W, is used on the target two-sphere of the ﬁeld φ , deter-
mined via stereographic projection as
W = φ1 + iφ2
1 + φ3
. (3.2)
With these deﬁnitions, then constructing a map φ : R3 ↦→S2 is equivalent to specifying
W (Z1, Z0), that is, W : S3 ↦→CP1, a map from the three-sphere to the complex projective
line. This map will be taken to be a rational map, which means t hat W = p/q, where both
p and q are polynomials in the variables Z1 and Z0.
For an ( a, b)-torus knot the mapping is chosen to have the form
W = p
q = Z α
1 Z β
0
Z a
1 + Z b
0
, (3.3)
where α is a positive integer and β is a non-negative integer. A map of this form has
the correct boundary conditions at spatial inﬁnity, since a s r → ∞ then ( Z1, Z0) → (0, 1)
and, because α > 0, this gives W → 0, which is the stereographic projection of the point
φ = (0, 0, 1) = e3. Furthermore, the position curve is the preimage of the point −e3, which
corresponds to W = ∞, and hence is given by q = 0 = Z a
1 + Z b
0. As the coordinates ( Z1, Z0)
automatically lie on the unit three-sphere then the positio n curve is the ( a, b)-torus knot, for
all values of α and β.
8
The Hopf charge of the map determined by (3.3) is given by the c ross ratio
Q = αb + βa. (3.4)
To see this note that a rational map
W : S3 ↦→CP1, given by W (Z1, Z0) = p(Z1, Z0)
q(Z1, Z0) , (3.5)
has a natural extension to a map
(p, q) : B4 ⊂ C2 ↦→C2, given by ( p(Z1, Z0), q(Z1, Z0)). (3.6)
Here B4 denotes the 4-ball with boundary S3, and is obtained by replacing the constraint
|Z1|2 + |Z0|2 = 1 by the inequality |Z1|2 + |Z0|2 ≤ 1. The map ( p, q) is between manifolds of
the same dimension and has a degree, deﬁned by counting preim ages of a generic point of
the target space, weighted by the signs of the Jacobian. As al l the other mappings involved
in the ansatz have degree one, and the standard Hopf map ( p, q) ↦→p/q is employed, then
the Hopf charge Q of the combined mapping is equal to the degree of the mapping ( p, q).
Furthermore, as the mapping ( p, q) is holomorphic then the sign of the Jacobian of all generic
preimage points is positive, so the degree is simply the numb er of preimages.
For the mapping ( p, q) given by (3.3) take the generic point in target space to be ( ǫ, 0), so
the Hopf charge is the number of solutions of the equation ( Z α
1 Z β
0 , Za
1 + Z b
0) = ( ǫ, 0). Writing
Z0 in terms of Z1 from the ﬁrst component of this equation and substituting in to the second
component yields the polynomial equation Z αb +βa
1 = (−1)β ǫb, which clearly has Q = αb + βa
solutions, as stated.
For any ( a, b)-torus knot the above ansatz can be used to construct a ﬁeld c onﬁguration
of the type Ka,b with Hopf charge Q, providing there are integers ( α, β), with α positive
and β non-negative, for which Q = αb + βa. For example, in the case of the trefoil knot
then ( a, b) = (3 , 2) hence any Q > 3 can be obtained. In fact a trefoil knot with Q = 3
can also be obtained by interchanging the roles of Z1 and Z0, but a ﬁeld of this type is not
relevant, as will be made clear later. Note that for some valu es of Q, and ﬁxed ( a, b), there
are multiple solutions for ( α, β). These multiple solutions produce qualitatively similar ﬁe lds,
in that both describe the same ( a, b)-torus knot position curve, and the linking curve twists
the same number of times around the position curve; though th e distribution of twist may
vary. In examples where such multiple solutions were used as initial conditions, the energy
relaxation algorithm produced identical ﬁnal results for a ll choices.
Recall that a proﬁle function f (r) needs to be speciﬁed, satisfying the boundary condi-
tions f (0) = π and f (∞) = 0 . In fact, these are the correct boundary conditions in an inﬁn ite
domain but in the ﬁnite domain used for numerical simulation s the last boundary condition
needs to be replaced by f = 0 at the boundary of the numerical grid. As the ansatz is
only used to provide initial conditions then most reasonabl e monotonic functions will suﬃce.
The simulations discussed in this paper were performed on a c ubic grid of side-length 2 L,
that is, −L ≤ xi ≤ L, where 2 L = 15 . A simple linear proﬁle function was used, given by
9
Figure 2: The position (light tube) and linking (dark tube) c urves for initial conditions
created using the rational map ansatz: (a) Q = 7 trefoil knot; (b) Q = 6 link L1, 1
2, 2.
f (r) = π(L − r)/L, for r ≤ L and zero otherwise. For a given rational map one could aim to
minimize the energy of the ansatz over all proﬁle functions, but this has not been attempted
for reasons discussed shortly.
As an illustration of the use of the ansatz, consider an appro ximation to the minimal
energy Q = 7 trefoil knot. To construct a ﬁeld K3, 2 with Q = 2 α + 3 β = 7 , requires
(α, β) = (2 , 1), resulting in the map W = Z 2
1 Z0/(Z 3
1 + Z 2
0 ). The ﬁeld generated from this
rational map is displayed in Figure 2a, where both the positi on and linking curves are shown.
It is clear from this ﬁgure that the ﬁeld has similar qualitat ive features to the minimal energy
soliton, in that it is a trefoil knot with four twists. The mai n qualitative diﬀerence is that
the ansatz produces a more symmetric ﬁeld, having a cyclic C3 symmetry. This symmetry
is obvious from the form of the rational map, as a rotation by 1 20◦ around the x3-axis
corresponds to the transformation Z1 ↦→e2πi/ 3Z1, upon which the rational map changes by
only a phase; which is simply an action of the global O(2) symmetry on target space.
Using the above ﬁeld as the initial condition for an energy re laxation simulation yields the
minimal energy soliton very quickly, and certainly require s far less computational resources
than computing the solution from a perturbed axial conﬁgura tion. Note that, in practice,
the cyclic C3 symmetry is slightly broken by the cubic numerical grid, and in particular
its boundary, so an explicit symmetry breaking perturbatio n is not required. In examples
discussed later, where initial conditions have a cyclic C4 symmetry, then the conﬁguration
is created with a slight displacement from the centre of the g rid to again slightly break any
exact symmetry.
As mentioned above, the proﬁle function could be optimized t o ﬁnd the minimal energy
conﬁguration, for a given rational map, but this has not been attempted. As with the
above example, generally the ansatz is more symmetric than t he relaxed solution, so it is
not expected that a good estimate of the energy can be obtaine d in this way. It might be
possible to improve the approximation to a quantitative lev el by minimizing over families
of rational maps, which include symmetry breaking terms, ra ther than using the rational
10
maps in this paper; chosen to be the simplest with the correct qualitative features. In this
case it would be worthwhile to also minimize the proﬁle funct ion, but as the minimization
problem couples the rational map and the proﬁle function tog ether then this is not a simple
numerical task. In fact, this numerical problem appears to h ave about the same level of
diﬃculty as performing energy relaxation via full ﬁeld simu lations. As the energy relaxation
code produces a solution very quickly and eﬃciently from the simple ansatz, then there
appears little need to try and improve upon it. The proﬁle fun ction could be adjusted to a
minimal extent, for example, by including parameters to set the scale and thickness of the
knot, but again this has not been necessary.
So far only knot initial conditions have been considered, bu t the ansatz can also be used
to construct a variety of unknots and links by choosing suita ble rational maps. For example,
axial ﬁelds of the form An,m are generated by a rational map W = Z n
1 /Zm
0 .
Links correspond to rational maps in which the curve determi ned by the denominator
is reducible. The torus knot maps with ( a, b) coprime degenerate to links if ( a, b) are not
coprime. As an example, links of the type L1, 1
n,n (which have Hopf charge Q = 2 n + 2) are
derived from the rational map
W = Z n+1
1
Z 2
1 − Z 2
0
= Z n
1
2(Z1 − Z0) + Z n
1
2(Z1 + Z0), (3.7)
where the partial fraction decomposition reveals the charg es of the constituent links by
comparison with the axial maps. The Q = 6 ﬁeld constructed using the rational map (3.7)
with n = 2 is displayed in Figure 2b. As can be seen from this ﬁgure, th e ﬁeld is qualitatively
similar to the minimal energy Q = 6 soliton, which is of the type L1, 1
2, 2. More examples of
rational maps associated to linked conﬁgurations will appe ar in the following section.
