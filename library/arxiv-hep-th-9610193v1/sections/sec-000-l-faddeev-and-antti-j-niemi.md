---
doc_id: arxiv-hep-th-9610193v1
doc_title: "KNOTS AND PARTICLES"
section_id: sec-000-l-faddeev-and-antti-j-niemi
section_title: "Faddeev ∗♯ and Antti J. Niemi ∗∗♯"
section_number: L
pages: 1-8
source_pdf: 9610193v1.pdf
source_sha256: e879864ec3a68faf
doc_brief: "KNOTS AND PARTICLES — 2 sections: Faddeev ∗♯ and Antti J. Niemi ∗∗♯; References"
---
∗St.Petersburg Branch of Steklov Mathematical Institute
Russian Academy of Sciences, Fontanka 27 , St.Petersburg, R ussia‡
∗∗Department of Theoretical Physics, Uppsala University
P.O. Box 803, S-75108, Uppsala, Sweden ‡
and
♯Research Institute for Theoretical Physics
P.O. Box 9, FIN-00014 University of Helsinki, Finland
Using methods of high performance computing, we have found i ndications that knotlike
structures appear as stable ﬁnite energy solitons in a reali stic 3+1 dimensional model.
We have explicitly simulated the unknot and trefoil conﬁgur ations, and our results sug-
gest that all torus knots appear as solitons. Our observatio ns open new theoretical
possibilities in scenarios where stringlike structures ap pear, including physics of funda-
mental interactions and early universe cosmology. In nemat ic liquid crystals and 3He
superﬂuids such knotted solitons might actually be observe d.
‡ permanent address
∗ supported by Russian Academy of Sciences and the Academy of F inland
∗∗ Supported by G¨ oran Gustafsson Foundation for Science and M edicine
and by NFR Grant F-AA/FU 06821-308
∗ E-mail: F ADDEEV@PDMI.RAS.RU and F ADDEEV@PHCU.HELSINKI.FI
∗∗ E-mail: ANTTI.NIEMI@TEORFYS.UU.SE
In 1867 Lord Kelvin [1] proposed that atoms, which at the time were considered as
elementary particles, are knotted vortex tubes in ether. Fo r about 20 years his theory
was taken seriously, and motivated an extensive study of kno ts. The results obtained at
the time by Tait [2] remain a classic contribution to mathema tical knot theory [3]. More
recently the idea that elementary particles can be identiﬁe d with topologically distinct
knots has been advanced in particular by Jehle [4].
Today it is commonly accepted that fundamental interactions are described by string-
like structures [5], with diﬀerent elementary particles co rresponding to the vibrational
excitations of a fundamental string. Even though there are h ints of connections between
modern string theory and knot theory [6], knotlike structur es have not yet been of much
signiﬁcance.
There are also a number of other scenarios where knotted stru ctures may enter
Physics [3], [7]. These include models in statistical physi cs, QCD strings that conﬁne
quarks inside nuclear particles, cosmic strings that are ex pected to be responsible for
early universe structure formation, and approaches to quan tum gravity where knots are
supposed to determine gauge invariant observables. String like vortices appear in type-II
superconductors where they conﬁne magnetic ﬁelds within th e cores of vortex-like struc-
tures, and similar phenomena are also present in superﬂuid 4He. Recent experiments
with nematic liquid crystals [8] and 3He superﬂuids [9] have also revealed interesting
vortex structures that can be described by theoretical meth ods which are adopted from
cosmic string models. Finally, physics of knots is rapidly b ecoming an important part of
molecular biology, where entanglement of a DNA chain interf eres with vital life processes
of replication, transcription and recombination [10].
Thus far the physics of knotlike structures has been investi gated sparsely. This is
largely due to a lack of dynamical principles that enable the construction of stable knots.
One needs a theoretical model where knots emerge as solitons , i.e. as stable ﬁnite energy
solutions to the pertinent nonlinear ﬁeld equations.
The literature on solitons is enormous, and there are severa l extensive reviews [7],
[11], [12]. Until now the activity has mainly concentrated o n 1+1 dimensions with the
notable exceptions of the 2+1 dimensional vortex and nonlin ear σ-model soliton, and
skyrmeons and ’tHooft-Polyakov monopoles in 3+1 dimension s. These are all pointlike
conﬁgurations, and can not be directly associated with knot like structures.
When embedded in three dimensions, a pointlike two dimensio nal soliton becomes
a line vortex. For a ﬁnite energy its length must be ﬁnite whic h is possible if its core
forms a knot. In 1975 one of us [13] proposed that closed, knot ted vortices could be
constructed in a deﬁnite dynamical model. The explicit solu tion suggested in [13] is a
closed torus-like vortex ring, twisted once around its core before joining the ends which
ensures stability against shrinking. This closed vortex co rresponds to the unknot (see
ﬁgure 4) which is the simplest possible knotlike structure. However, despite numerous
attempts no such stable conﬁguration has been constructed, neither by explicit analysis
nor by a numerical investigation.
1
Here we shall report on our work to construct knotlike vortic es in the model intro-
duced in [13]. By employing numerical algorithms in powerfu l computers we have been
able to ﬁnd strong evidence for the existence of the unknot vo rtex. In addition we have
found indications supporting the existence of a trefoil vortex (see ﬁgure 5). A trefoil
is the simplest example of torus-knots, which are obtained b y winding around a torus
in both directions [3]. Our results suggest that in fact all t orus knots should appear as
vortex solitons in the model proposed in [13]. This model des cribes the 3+1 dimensional
dynamics of a three component vector ⃗n(x, τ) with unit length, ⃗n · ⃗n = 1. Such a vector
ﬁeld is a typical degree of freedom in the nonlinear σ-model, a prototype relativistic
quantum ﬁeld theory. It also appears as an order parameter in the Heisenberg ferro-
magnet. A unit vector ﬁeld is also present in models of nemati c liquid crystal where it
characterizes the average direction of the rod, and in 3He-A superﬂuid where it deter-
mines the spin projection direction for a Cooper pair. Indee d, the model proposed in
[13] is quite universal, and we expect our results to have a la rge number of applications.
In order that ⃗n(⃗x) describes a localized stationary knot, it must go to a const ant
vector ⃗n(⃗x) → ⃗n0 at large distances. Consequently ⃗n(⃗x) deﬁnes a mapping from the
compactiﬁed R3 ∼ S3 → S2. Such mappings fall into nontrivial homotopy classes
π3(S2) ≃ Z and can be characterized by the Hopf invariant [3]. For this w e introduce
the two-form F = (d⃗n∧d⃗n, ⃗n) on the target S2. Its preimage F⋆ on S3 is exact, F⋆ = dA⋆,
and the Hopf invariant QH is given by
QH =
∫
R3
F ∧ A (1)
The Hamiltonian proposed in [13] is
H = E2 + E4 =
∫
d3x g 2(∂µ⃗n)2 + e2F 2 (2)
This is the most general three dimensional Hamiltonian that admits a relativistically
invariant extension in 3+1 dimensions and involves only ter ms with no more than four
derivatives. It can be related to the SU (2) Skyrme model when restricted to a sphere
S2 ∈ SU (2), but its topological features are diﬀerent. In particul ar, the existence
of nontrivial knotted vortex solutions in (2) is strongly su ggested by the lower bound
H ≥ c · |QH |
3
4 [14].
The ﬁrst term E2 determines the standard nonlinear O(3) σ-model which admits
static solitons in two dimensions. But in three dimensions a scaling ⃗x → ρ⃗x reveals that
stable stationary solutions are possible only if E4 is also present. Indeed, under this
scaling E2 → ρE2 but E4 → ρ− 1E4 from which we conclude that in three dimensions
ﬁnite energy solutions obey the virial theorem,
E2 = E4 (3)
2
Several articles have been devoted for analyzing the genera l properties of the unknot
vortex in the model (2) [12]. However, to our knowledge there have been no real attempts
to ﬁnd an actual solution. This is due to the fact, that even in the simplest case of an
unknot the separation of variables eliminates only one of th e three space coordinates,
leaving numerical methods as the sole alternative for ﬁndin g a solution. With the recent,
enormous progress in supercomputing techniques serious at tempts are ﬁnally becoming
realistic.
The Euler-Lagrange equations for (2) determine a highly non linear elliptic system,
and a direct numerical approach appears to be complicated. I nstead, we consider the
parabolic equation
dφa
dt = − δH (φ)
δφa
(4)
where φa denotes a generic dynamical variable in (2). The t-bounded solutions of (4)
connect the critical points of H by ﬂowing away from an unstable critical point at
t → −∞ towards a stable critical point at t → +∞. From this we expect that by
deﬁning a suitable initial conﬁguration at t = 0, for large t ≫ 0 we ﬂow towards a stable
vortex solution of the original stationary equation.
We parametrize our unit vector by ⃗n = (cos ϕ sin θ, sin ϕ sin θ, cos θ) through stere-
ographic coordinates ϕ = − arctan( V
U ) and θ = 2 arctan
√
U 2 + V 2. In terms of these
variables the Hamiltonian (2) becomes
H =
∫
d3x 4g2
(1 + U 2 + V 2)2 (∂µU 2 + ∂µV 2) + 16e2
(1 + U 2 + V 2)4 (∂µU ∂νV − ∂νU ∂µV )2 (5)
By a global SO(3) rotation we can select our asymptotic vacuum vector ⃗n0 so that
outside of the vortex it points to the positive- z direction. This means that outside of
the vortex we are near the north pole where θ(⃗x) ≈ 0, while the core corresponds to
the south pole θ(⃗xc) = π. The internal structure of a vortex can then be investigated
by cutting it once with a plane at right angle to its core. This cross sectional plane is
topologically identical to a sphere S2: At the core we have θ(⃗xc) = π corresponding to
the south pole and outside of the vortex on the plane we have θ(⃗x) ≈ 0 corresponding
to the north pole. Furthermore, ϕ(⃗x) increases (or decreases, depending on orientation)
by 2π when we go around the core once on the cross sectional plane. 1 For Uand V this
means, that we identify them as local coordinates on the Riem ann sphere in a patch
that contains the north pole U(⃗x) = V (⃗x) = 0.
In ﬁgures 1 and 2 we have drawn θ(⃗x) and ϕ(⃗x) respectively for our unknot vortex.
The general structure is clearly visible in these pictures.
In the present model there are two symmetries that relate a gi ven vortex solution
with Hopf invariant QH to an antivortex solution with equal energy but opposite Hop f
1More generally, ϕ is deﬁned modulo 2 πn where n is an integer. Here we only consider the simplest
case with n = ±1.
3
invariant −QH . The ﬁrst symmetry emerges when we change orientation ϕ → −ϕ on the
cross sectional plane. The second symmetry interchanges th e north pole with the south
pole on the cross sectional plane, i.e. maps the core to θ(⃗xc) = 0 and the region outside
of the vortex to θ(⃗x) ≈ π. In terms of the U(⃗x) and V (⃗x) variables this means that
on each cross sectional plane the Hamiltonian (5) must be inv ariant under the inversion
Z(⃗x) = U(⃗x) + iV (⃗x) → Z − 1(⃗x). This implies in particular, that the energy density
H(⃗x) must be concentrated in a relatively narrow tubular neighb orhood around the core
of the vortex.
In ﬁgure 3 we have depicted the energy density on a cross secti onal plane for the
unknot vortex. The concentration of energy density in a tubu lar manner around the
core is clearly visible.
In order to specify the initial condition in (4) we need a knot conﬁguration which is
topologically equivalent to the desired vortex solution. W e specify this conﬁguration by
ﬁrst introducing a parametrization ⃗x(λ) for the center of the knot in R3, and then for
each λ use the Serret-Frenet equations to deﬁne local coordinates U(⃗x; λ) and V (⃗x; λ)
on the cross sectional planes.
The choice of initial parametrization ⃗x(λ) for the core introduces a scale which may
be quite diﬀerent from the one speciﬁed by the coupling const ant g in (5). In order to
enhance convergence, we adopt a simple renormalization pro cedure by promoting g to
a time dependent function g(t). We deﬁne this time dependence by demanding that at
each value of t the virial theorem (3) must be obeyed. Since a vortex solutio n obeys (3),
this means that g(t) ﬂows towards a ﬁxed point value g(t) → g⋆.
We have performed our numerical simulations using version 5 .3 of G. Sewell’s PDE2D
ﬁnite element algorithm [15]. During the early phase of our s imulations we have used
the initial knot conﬁguration to determine the boundary con ditions on the ﬁnite element
mesh. However, since the exact boundary conditions for the d esired vortex are a priori
unknown, after several time steps we have decreased the size of the ﬁnite element mesh
and used the pertinent simulated conﬁguration to determine the boundary conditions
in the new mesh. By starting from a suﬃciently large initial m esh, we then eventually
obtain a submesh with boundary conditions that are close to t hose of the actual solution.
For our simulation we have used two Silicon Graphics Power Ch allenge computers
with R8000 processors equipped with 1GB resp. 2GB of internal memory.
For the unknot vortex ( QH = ±1), the equations of motion can be simpliﬁed using
axial symmetry. We select the symmetry axis to coincide with the z-axis in R3, and
introduce cylindrical coordinates r, φ, z. With the Ansatz ϕ(⃗x) = ϕ(r, z) +φ and θ(⃗x) =
θ(r, z) the φ-coordinate separates, and we obtain a two dimensional equa tion for U(r, z)
and V (r, z). That such a separation of variables is possible follows di rectly from the
SO(2)×SO(2) symmetry of the unknot conﬁguration. The ensuing equati ons are deﬁned
on the half-plane r ≥ 0, z ∈ (−∞, ∞), which at each φ determines our cross sectional
4
plane. Besides the inversion invariance, the equations of m otion are now also invariant
under z → −z. Since the unknot solution is even in z, this halves the CPU time in our
simulation.
In ﬁgures 1-4 we describe an unknot vortex which is a result of over 50h of CPU time
with each time step taking about 9 minutes on a 9600 triangle m esh. The mesh has
been selected so that it is more dense at the boundaries and ne ar the core of the vortex.
In our simulation we ﬁnd impressive convergence, allowing u s to increase the time step
by up to 8 orders of magnitude while keeping the relative chan ge in energy intact. The
Hopf invariant is also very stable, and we have identiﬁed the ﬁnal conﬁguration on the
basis that the numerically computed Hopf invariant has a sli ght local maximum with
QH = 0.999996 ...
The trefoil vortex ( QH = ±3) described in ﬁgure 5 is a result of almost 200h in
CPU time on a 21 3 cubic ﬁnite element lattice with tri-cubic Hermite basis fu nctions.
Consequently the number of nodes is about the same as in the ca se of unknot, but due
to a lack of any obvious reﬂection symmetry each time iterati on now takes about 20
minutes of CPU time. The yellow center in ﬁgure 5 corresponds to the core ⃗x(λ) of
our initial conﬁguration, which has been determined using t he energy concept developed
by J. Simon [16]. The points in ﬁgure 5 have been evaluated usi ng the piecewise cubic
polynomial approximation obtained from the ﬁnite element a lgorithm. As in ﬁgure 4,
the picture describes a volume where the energy density insi de the vortex essentially
vanishes, i.e. it can be viewed as an extended core of our trefoil vortex.
We expect that the nonhomogeneity in ﬁgure 5 reﬂects the unde rlying lattice struc-
ture that we have used in our simulation. Indeed, a 21 3 lattice is obviously too rough
to describe our trefoil solution adequately, but unfortuna tely we do not have access to a
computer that would allow us to use an essentially larger lat tice. Nevertheless, we have
found deﬁnite numerical stability in the sense that the ﬁnal conﬁguration in ﬁgure 5 has
remained essentially intact under a large number of iterati ons. We view this stability as
a strong evidence that we indeed have convergence towards a t refoil vortex solution.
In conclusion, we have performed numerical simulations wit h a high-performance
computer to investigate knotted vortex solutions in the mod el introduced in [13]. By
investigating the unknot and trefoil vortices, we have foun d strong evidence that torus
knots indeed appear as solitons. For the unknot, we have foun d very impressive con-
vergence and our results for the trefoil are also quite encou raging. However, since the
computers we can access do not allow us to eﬀectively study de nse three dimensional
lattices, our simulation of the trefoil is still tentative.
We expect that our results will have numerous important appl ications. In particular,
since the order parameter in nematic liquid crystal and 3He superﬂuid involves a unit
three vector, an experimental investigation of vortices in these materials should reveal
the existence of stable knotlike structures. We also expect that an extension of our work
5
to spontaneously broken Yang-Mills-Higgs theories where s table knotlike vortices can
not be excluded by scaling arguments, should have interesti ng physical implications in
particular to early universe cosmology.
We wish to thank J.Hietarinta, T.K¨ arki, A.P.Niemi, K.Palo, J.Pitk¨ aranta, J.Rahola,
D.Riska, R.Scharein, G.Sewell, O.Tirkkonen and J.Tulkki f or helpful discussions and
valuable suggestions. We are particularly indebted to Sami Virtanen for his help with
visualization and simulating the initial Ansatz for the tre foil, and Matti Gr¨ ohn for
helping us with visualization. We are grateful to the Center for Scientiﬁc Computing in
Espoo, Finland for providing us with an access to their line o f Silicon Graphics Power
Challenge computers.
6
