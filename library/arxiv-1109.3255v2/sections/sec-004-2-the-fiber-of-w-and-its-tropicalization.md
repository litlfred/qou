---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-004-2-the-fiber-of-w-and-its-tropicalization
section_title: "The fiber of W and its tropicalization"
section_number: 2
pages: 11-16
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
2.1. Torus ﬁbrations on CP2 \D and its mirror. Let
(16) D = {xyz −y3 = 0} ⊂ CP2
be a binodal cubic curve. We equip CP2 and CP2 \D with standard Fubini-Study
symplectic forms. Both CP2 \D and its mirror X ∨ = {(u,v ) ∈ C2 | uv ⁄= 1 } admit
special Lagrangian torus ﬁbrations. In fact, these spaces are d iﬀeomorphic, each being
C2 minus a conic. The torus ﬁbrations are essentially the same on both s ides, but we
are interested in the symplectic aﬃne structure associated to the ﬁbration on CP2 \D
and the complex aﬃne structure associated to X ∨.
The construction is of the torus ﬁbrations is taken from [7, §5]. We have that
CP2 \D is an aﬃne algebraic variety with coordinates x andz, where xz ⁄= 1. Hence
we can deﬁne a map
(17) f : CP2 \D → C∗ f (x,z ) = xz − 1
This map is a Lefschetz ﬁbration with critical point (0 , 0) and critical value −1. The
ﬁbers are aﬃne conics, and the map is invariant under the S1 action eiθ(x,z ) =
(eiθx,e −iθz) that rotates the ﬁbers. Each ﬁber contains a distinguished S1–orbit,
namely the vanishing cycle {|x| = |z|}. We can parametrize the other S1–orbits by
the function δ(x,z ) which denotes the signed symplectic area between the vanishing
cycle and the orbit through ( x,z ). The function δ is a moment map for the S1-action.
Symplectic parallel transport in every direction preserves the circ le at level δ = λ,
and so by choosing any loop γ ⊂ C∗, and λ ∈ (−Λ, Λ) (where Λ =
∫
CP1ω is the area
of a line), we obtain a Lagrangian torus Tγ,λ ⊂ CP2 \D. If we let TR,λ denote the
torus at level λ over the circle of radius R centered at the origin in C∗, we ﬁnd that
TR,λ is special Lagrangian with respect to the form
(18) Ω = dx ∧dz/(xz − 1).
The torus ﬁbration on X ∨ is essentially the same, except that the coordinates ( x,z )
are changed to ( u,v ). For the rest of the paper, we denote by
(19) w =uv − 1
the quantity to which we project in order to obtain the Lagrangian t ori TR,λ (and
later the Lagrangian sections L(d)) as ﬁbering over paths. For the time being, and in
order to enable the explicit computations in section 2.3, we will equip X ∨ with the
standard symplectic form in the ( u,v )–coordinates, so the quantity
(20) δ(u,v ) = |u|2 − |v|2
is the standard moment map. In summary, for X ∨, we have
(21) TR,λ = {(u,v ) | |w| = |uv − 1| =R, |u|2 − |v|2 =λ}.
Each torus ﬁbration has a unique singular ﬁber T1,0, which is a pinched torus.
12 JAMES PASCALEFF
Figure 1. The Lefschetz ﬁbration with a torus that maps to a circle.
Figure 1 shows several ﬁbers of the Lefschetz ﬁbration, with a La grangian torus
that maps to a circle in the base. The two marked points in the base re present a
Lefschetz critical value (ﬁlled-in circle), and a puncture (open circ le).
For the symplectic aﬃne structure, the aﬃne coordinates are obt ained by integrat-
ing the symplectic two-form ω over one-cycles in the torus ﬁbers to obtain one-forms
on the base, which may be integrated to functions. For the complex aﬃne structure,
we instead integrate the imaginary part of the holomorphic volume fo rm Im Ω over
(n − 1) cycles in the ﬁber to obtain one-forms on the base, where in our c ase n = 2.
See [16, §2] for an explanation of this construction.
We begin by describing the symplectic aﬃne structure on the base B of the torus
ﬁbration on CP2 \D. Recall that an integral aﬃne structure has a canonically deﬁned
local system of integral tangent vectors. In the case when the a ﬃne manifold has
singularities, this local system may have monodromy around the sing ular locus. The
following result can be extracted from the analysis of [7, §5.2].
Proposition 2.1. The integral aﬃne manifold B is topologically a disk. It has one
singular point, with monodromy conjugate to
(
1 0
1 1
)
. In aﬃne coordinates, the
boundary of B consists of two line segments that are straight with respect to the aﬃne
structure. The corners are locally equivalent, by an aﬃne li near transformation, to
the standard quadrant R2
≥0 ⊂ R2.
Proof. The symplectic aﬃne coordinates are the symplectic areas of disks in CP2 with
boundary on TR,λ. Let H denote the class of a line. We consider the cases R> 1 and
R< 1.
On the R> 1 side, we take β1,β 2 ∈H2(CP2,T R,λ) to be the classes of two sections
over the disk bounded by the circle of radius R in the base, where β1 intersects the
MIRROR OF THE PROJECTIVE PLANE 13
z-axis and β2 the x-axis. Then the torus ﬁber collapses onto line {y = 0} when
(22) ⟨[ω],H −β1 −β2⟩ = 0.
On the R< 1 side, we take α,β ∈H2(CP2,T R,λ), where β is now the unique class
of sections over the disk bounded by the circle of radius R, and α is the class of a
disk connecting an S1-orbit to the vanishing cycle within the conic ﬁber and capping
oﬀ with the thimble. The torus ﬁber collapses onto the conic {xz −y2 = 0} when
(23) ⟨[ω],β ⟩ = 0.
The two sides R > 1 and R < 1 are glued together along the wall at R = 1,
but the gluing is diﬀerent for λ > 0 than for λ < 0, leading to the monodromy.
Let us take η = ⟨[ω],α ⟩ and ξ = ⟨[ω],β ⟩ as aﬃne coordinates in the R < 1 region.
We continue these across the λ > 0 part of the wall using correspondence between
homology classes:
α ↔β1 −β2
β ↔β2
H − 2β −α ↔H −β1 −β2
(24)
Thus, in the λ> 0 part of the base, the conic appears as ξ = 0, while the line appears
as
(25) 0 = ⟨[ω],H − 2β −α⟩ = Λ − 2ξ −η
which is a line of slope of −1/2 with respect to the coordinates ( η,ξ ). The pair of
functions ξ and Λ − 2ξ −η also form an aﬃne coordinate system, and in this system
the corner appears as a standard quadrant.
In the λ< 0 part of the base, we instead use
α ↔β1 −β2
β ↔β1
H − 2β +α ↔H −β1 −β2
(26)
Hence in this region the conic appears as ξ = 0 again, while the line appears as
(27) 0 = ⟨[ω],H − 2β +α⟩ = Λ − 2ξ +η
which is a line of slope 1/2 with respect to the coordinates (η,ξ ). The pair of functions
ξ and Λ − 2ξ +η also form an aﬃne coordinate system, and in this system the corner
appears as a standard quadrant.
The discrepancy between the two gluings represents the monodro my. As we pass
from {R > 1,λ > 0} → { R < 1,λ > 0} → { R < 1,λ < 0} → { R > 1,λ < 0} →
{R> 1,λ> 0}, the coordinates (η,ξ ) under go the transformation ( η,ξ ) → (η,ξ −η),
which is indeed a simple shear.
□
Figure 2 shows the aﬃne manifold B. The marked point is a singularity of the aﬃne
structure, and the dotted line is a cut in the aﬃne coordinates. The aﬃne coordinates
η,ξ,ψ are indicated. The function ξ is undeﬁned on the cut below the singularity,
while ψ is undeﬁned at points directly above the singularity. Going around th e
singularity counterclockwise, the monodromy of the local system o f integral tangent
14 JAMES PASCALEFF
η η
ξ
ψ
ξ
ψ
Figure 2. The aﬃne manifold B.
vectors
(
1 0
1 1
)
, which also serves as the gluing map along the cut. The edges of
the picture are boundaries. The upper edge corresponds to point s where the torus
collapses onto the line {y = 0 }. It has slope zero in this picture. The lower edge
corresponds to points where the torus collapses onto the conic {xz −y2 = 0 }. On
the left portion the lower edge has slope −1/2, while on the right portion it has slope
1/2. The lower edge is actually straight with respect to the aﬃne struc ture, and the
nontrivial gluing is what compensates for the apparent bend.
On the mirror side, we compute the complex aﬃne structure (deter mined by the
holomorphic volume form) on the base of the torus ﬁbration on X ∨. The holomorphic
volume form is
(28) Ω = du ∧dv
uv − 1 = du ∧dv
w .
Diﬀerentiating the deﬁning equation uv = 1 + w and substituting gives the other
formulas
(29) Ω = du
u ∧dw
w , when u ⁄= 0,
(30) Ω = −dv
v ∧dw
w , when v ⁄= 0.
The special Lagrangian ﬁbration on X ∨ to consider is constructed in [7]. The ﬁbers
are the tori
(31)
TR,λ = {(u,v ) ∈X ∨ | |uv − 1| =R, |u|2 − |v|2 =λ}, (R,λ ) ∈ (0, ∞) × (−∞, ∞),
and the ﬁber T1,0 is a pinched torus. Thus ( R,λ ) are coordinates on the base of
this ﬁbration. They are not aﬃne coordinates, which must be compu ted using Im Ω.
Due to the simple algebraic form of this ﬁbration, it is possible to ﬁnd an integral
representation of the complex aﬃne coordinates explicitly.
MIRROR OF THE PROJECTIVE PLANE 15
Proposition 2.2. The following functions are aﬃne linear with respect to aﬃne
structure induced by Im Ω .
η = log |w| = logR
ξ = 1
2π
∫
TR,λ ∩{u∈R+}
log |u|d arg(w)
= 1
2π
∫ 2π
0
1
2 log
(
λ +
√
λ2 + 4 · |1 +Reiθ|2
2
)
dθ
ψ = 1
2π
∫
TR,λ ∩{v∈R+}
log |v|d arg(w)
= 1
2π
∫ 2π
0
1
2 log
(
−λ +
√
λ2 + 4 · |1 +Reiθ|2
2
)
dθ
(32)
(η is deﬁned everywhere, ξ is deﬁned where u ⁄= 0 , and ψ is deﬁned where v ⁄= 0 ).
They satisfy the following relations on their common domain of deﬁnition.
(1) At every point, η is independent from ξ and from ψ.
(2) In the subset where R< 1, the relation ξ +ψ = 0 holds.
(3) In the subset where R> 1, the relation ξ +ψ =η holds.
Proof. This is essentially straightforward so we only give an example of the co mpu-
tation.
The general procedure for computing aﬃne coordinates from the ﬂux of the holo-
morphic volume form is as follows: we choose, over a local chart on th e base, a
collection of (2 n − 1)–manifolds {Γ i}n
i=1 in the total space X such that the torus
ﬁbers Tb intersect each Γ i in an ( n − 1)–cycle, and such that these ( n − 1)–cycles
Tb ∩ Γ i form a basis of Hn−1(Tb; Z). The aﬃne coordinates ( yi)n
i=1 are deﬁned up to
constant shift by the property that
(33) yi(b′) −yi(b) = 1
2π
∫
Γ i∩π−1(γ)
Im Ω
where γ is any path in the local chart on the base connecting b to b′. Because Ω is
closed, this integral does not depend on the choice of γ.
To get the coordinate η, start with the submanifold
(34) Γ 1 = {w ∈ R+}
The intersection Γ 1 ∩TR,λ is a loop on TR,λ. The function arg( u) gives a coordinate
on this loop (brieﬂy, w ∈ R+ and |w| =R determineuv, along with |u|2 −|v|2 =λ this
determines the |u| and |v|; the only parameter left is arg( u) since arg(v) = − arg(u)),
and we declare the loop to be oriented so that −d arg(u) restricts to a positive volume
form on it. Using (29) we see
(35) Im Ω = d arg(u) ∧d log |w| +d log |u| ∧d arg(w)
Using the fact that arg( w) is constant on Γ 1, we see that for any path γ in the subset
of the base where R< 1 connecting b = (R,λ ) to b′ = (R′,λ ′), we have
(36)
∫
Γ 1∩π−1(γ)
Im Ω =
∫
Γ 1∩π−1(γ)
d arg(u) ∧d log |w|.
16 JAMES PASCALEFF
But d arg(u) ∧d log |w| =d(− log |w|d arg(u))), so the integral above equals
(37)
∫
Γ 1∩Tb′
− log |w|d arg(u) −
∫
Γ 1∩Tb
− log |w|d arg(u) = 2π(logR′ − logR)
(the minus signs within the integrals are absorbed by the orientation convention for
Γ 1 ∩Tb). Thus η = logR is the aﬃne coordinate corresponding to Γ 1.
The same idea applied to Γ 2 = {u ∈ R+} yields the aﬃne coordinate
(38) ξ = 1
2π
∫
Γ 2∩Tb
log |u|d arg(w)
To arrive at the second formula for ξ, we must solve for |u| in terms of R,λ , and
θ = arg(w). The equations uv = 1 + Reiθ and |u|2 − |v|2 = λ imply |u|4 −λ|u|2 =
|1 +Reiθ|2. Solving for |u|2 by the quadratic formula and taking logarithms gives the
result.
The formulas for ψ are obtained by applying the same method to Γ ′
2 = {v ∈ R+}.
To prove the linear relations, we ﬁnd that ξ +ψ reduces by the law of logarithms
and the Cauchy integral formula to
(39) 1
2π
∫ 2π
0
log |1 +Reiθ|dθ =
{
0, R< 1
logR, R> 1
□
Proposition 2.2 determines the monodromy around the singular point (at η =ξ =
ψ = 0) of the base, and show that the aﬃne structure is in fact integr al. Once again,
the monodromy is a shear.
