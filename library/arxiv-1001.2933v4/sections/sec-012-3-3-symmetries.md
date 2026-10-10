---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-012-3-3-symmetries
section_title: "Symmetries"
section_number: "3.3"
pages: 41-48
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
3.3 Symmetries
Since gauge symmetry is an essential ingredient in Chern-Simons theory, including symmetries in our finite-dimensional models will improve their analogy with Chern-Simons. Before
taking this step, we consider a few preliminaries.
3.3.1 Oscillatory Integrals On More General Manifolds
One generalization is to consider, instead of an oscillatory integral on R
n
, an oscillatory
integral on some other space Y . Y must have a suitably nice complexification X, but we
will not attempt to be precise about this. Instead we just describe a typical example. We
take Y to be a real affine variety such as the one defined by the equation
x
2 + y2 = z2 + 1. (3.46)
Then we introduce a sufficiently generic polynomial f(x, y, z), and consider the oscillatory
integral Zλ =
R
Y
dθ exp(iλf), where dθ = dx dy/z is the natural volume form on Y .
Analytic continuation in λ can now be carried out by an obvious generalization of what
we have said for R
n
. We embed Y in the complex manifold X defined by the same equation
(3.46) but now with x, y, and z regarded as complex variables. The top degree form dθ on
Y extends to a holomorphic form of top degree on X (given by the same formula dx dy/z),
which can be integrated over any middle-dimensional cycle in X. Introducing the Morse
function h = Re (iλf), where f is regarded now as a holomorphic function on X, we associate
to each critical point a relative homology cycle obtained by downward flow. The analytic
continuation is made as usual by expressing the original integration cycle Y in terms of these
cycles, and then taking Stokes phenomena into account.
41

3.3.2 Manifolds Of Critical Points
Another generalization is to consider a polynomial f on R
n
(or on some more general space,
as just described) that has not isolated critical points but a manifold N of critical points.
The analytic continuation of f to a holomorphic function on C
n
likewise has a manifold M
of critical points; M is a complex manifold, of course, and its intersection with R
n
coincides
with N . (We will consider only the case that M is smooth, and we assume that the matrix
of second derivatives of f in the normal direction to M is invertible.) We want to use Morse
theory on C
n
to study the analytic continuation of the usual integral Zλ =
R
d
nx exp(iλf).
Suppose that M is a union of components Mα of complex dimension tα. I = iλf has a
constant value Iα on Mα, since Mα is a critical point set. As usual, we consider h = Re I
as a Morse function. Then Mα has Morse index n − tα. (This is shown by essentially the
same argument used in section 3.1.1 for the case tα = 0; one can choose local coordinates
in the normal direction to Mα so that I = c +
Pn−tα
i=1 z
2
i
.) The explanation in section 3.1.1
for why h is a perfect Morse function assumed that tα = 0 for all components, so that all
critical points have the same Morse index. Here is an alternative argument that does not
assume tα = 0. In general, a Morse function is perfect if there are no flows between distinct
critical points. (This is only possible for Morse functions that are unbounded below, like
the ones we consider here, since otherwise any downward flow from one critical point ends
at another critical point.) As we have found in eqn. (3.11), Im I is a conserved quantity for
the flow equation. Moreover, there never are flows between different critical points with the
same value of I. For generic λ, no two distinct components of Mα with different values of
Iα have the same value of Im Iα, so generically there are no flows between distinct critical
points and h is a perfect Morse function.
There is a general recipe, given a perfect Morse function on any manifold X, for describing
the relative homology of X in terms of downwards flows from critical points. Let S be a
component of the critical point set that has Morse index s. Let W ⊂ S be a cycle of
dimension r. For any point w ∈ W, the points in X that lie on downwards flows from w
form an s-dimensional subspace of X. So the points in X that can be reached by downward
flow from somewhere on W are a family of dimension r + s. This family is a cycle JW
of dimension r + s in the relative homology. These cycles, which we view as generalized
Lefschetz thimbles, generate the relative homology of X (subject only to the relations that
hold in the homology of the critical point set).
Applying this to our problem, if Mα is a component of the critical point set that has
complex dimension tα and Morse index n−tα, then to get an integration cycle on X – which
should be a cycle of dimension n – we need to start with a cycle on Mα of real dimension
tα, that is, a middle-dimensional cycle.
So the analytic continuation of the integral Zλ can be described using relative homology
42

cycles attached to the components Mα of the critical point set. But in general to a component
Mα we attach not just one cycle but a number equal to the rank of the middle-dimensional
homology of Mα.
This construction may have various applications to Chern-Simons theory, since in general the moduli space of representations of the fundamental group of a three-manifold has
components of positive dimension. However, the only application we will make in this paper
concerns reducible critical points, that is, flat connections that preserve some gauge symmetry. Moreover, this application concerns a situation in which every relevant component
of Mα has middle-dimensional cohomology of rank 1, and hence contributes only one cycle to the middle-dimensional cohomology. In a sense, therefore, our application involves a
situation that is as simple as the case of only isolated critical points.
3.3.3 Group Actions
Why might critical points not be isolated? One simple answer to this question will be
important in our study of gauge theory. In the presence of a group action, the critical points
will form orbits of the group, and this may force them to be non-isolated.
We consider a manifold Y with a chosen action of a compact connected Lie group H. We
also assume that Y has a good complexification X, which possesses a real involution that
leaves Y fixed. We endow Y with an H-invariant function f whose critical points consist of
finitely many H orbits Oσ, σ ∈ Σ.
As usual, we want to study the analytic continuation of the integral Zλ =
R
Y
dθ exp(iλf),
where dθ is the restriction to Y of a holomorphic top form on X. Assuming that f can be
analytically continued to a holomorphic function on Y (which we also denote as f), we
analytically continue the integral Zλ by embedding Y in X and using the Morse function
h = Re (iλf) on X. We assume that the H action on Y analytically continues to an action
on X of a complex Lie group G that is the complexification of H; in this case, the critical
points of h are orbits of G. We assume that there are only finitely many such critical orbits,
near each of which h is nondegenerate in the normal directions. For clarity, we will write
OG or OH for, respectively, a critical orbit of G acting on X or a critical orbit of H acting
on Y .
To orient ourselves, let us first consider the case that H acts freely on Y , and G acts
freely on X. Then we can write Zf as an integral over Y
′ = Y/H:
Zf =
Z
Y ′
dθ
′
exp(iλf), (3.47)
where the volume form dθ
′
is obtained by integrating dθ over the fibers of Y → Y
′
. From
43

a “downstairs” point of view, to analytically continue Zf , we must embed Y
′
in a suitable
complex manifold X′. Roughly speaking, the appropriate choice is X′ = X/G, which –
as G is a complexification of H and X is a complexification of Y – is a complexification
of Y
′ = Y/H. (Unstable orbits – the notion is discussed below – should be discarded in
defining the quotient X/G.)
Since f has only finitely many critical orbits as a function on X, it follows that as a
function on X′, f has only finitely many critical points. We are thus in the familiar situation
of isolated critical points only, and the relative homology of X′therefore has a basis consisting
of a Lefschetz thimble J
′
σ
for every critical point p
′
σ
. We can analytically continue the integral
Zf in the usual way by expressing the real cycle CR = Y
′ ⊂ X′
as a linear combination of
the J
′
σ
, and keeping track of Stokes phenomena.
How would we get an equivalent result by computing upstairs on Y and X rather than
downstairs on Y
′ and X′
? Every critical point p
′
σ
on X′corresponds to a critical orbit
OX
σ on X. Since we have assumed that G acts freely on X, the orbits are all copies of
G. Topologically, the complex Lie group G is isomorphic to the cotangent bundle T
∗H of
its maximal compact subgroup H. The middle-dimensional homology of T
∗H is of rank
1, generated by the zero section of the cotangent bundle. Hence, from an upstairs point of
view, the middle-dimensional relative homology of X has a basis with one generator for every
critical orbit. These generators correspond in an obvious way to the generators of the relative
homology of X′. The associated Lefschetz thimbles also have an obvious correspondence,
and the Stokes surfaces are the same whether one computes upstairs or downstairs. So we
can perform more or less equivalent computations upstairs or downstairs.
In the downstairs description, the critical points are isolated, so we do not really need
the theory sketched in section 3.3.2 as long as H acts freely. Now let us consider a more
general case in which H does not act freely on Y . This being so, the quotient Y
′ = Y/H is
singular, and the general theory would not readily apply to it. So instead we will calculate
on Y . We still assume that the critical point set of f on Y is a finite union of H orbits OH
σ
,
and that the critical point set of f on X is an analogous (but perhaps larger12) finite union
of G orbits OG
τ
.
Any critical orbit OH
σ
in Y has a complexification that is one of the OG
σ
. The complexification of an H orbit OH ⊂ Y is, from a topological point of view, simply T
∗OH. Its
middle-dimensional homology is of rank 1, generated by the zero section of the cotangent
bundle. Each critical orbit in Y therefore contributes one generator of the middle-dimensional
relative homology of X, just as in the case of a free action.
What about critical orbits in X that do not intersect Y ? We will show that not all critical
12 This is possible even in the absence of a group action. For example, the function f(x) = x3/3 + x has
complex critical points that do not lie on the real axis.
44

orbits need to be taken into account, but only certain “semistable” ones. The semistable
orbits are all topologically of the form T
∗OH for some H orbit OH, and again they have
middle-dimensional homology of rank 1. (Every critical orbit that intersects Y is semistable.)
So in short, the analytic continuation of Zf is made using a middle-dimensional relative
homology of X that has one generator for every semistable critical G orbit.
Now we will explain how semistability comes in. First of all, to construct the downward
flowing cycles associated to a critical point, we need to pick a metric on X. We generally
cannot pick this metric to be G-invariant, but it is commonly possible to pick an H-invariant
Kahler metric, such that the Kahler form ω is odd under the real involution of X that leaves
Y fixed. (For example, if Y = R
n with H-invariant metric P
i
(dx
i
)
2
, then we take on X = C
n
the H-invariant Kahler metric P
i
|dx
i
|
2
. In this case, ω = −i
P
k
dx
k∧dx
k
, and is odd under
x
k ↔ x
k
.) We assume the existence of such a metric. H acts on X preserving the symplectic
form ω, and it is possible to define a moment map ~µ for the action of H on X. Here ~µ maps
a vector field V that generates a one-parameter subgroup of H to a function µV that obeys
dµV = ιV ω, (3.48)
where ιV is the operation of contraction with V . In indices
∂µV
∂xi
= V
jωji,
∂µ
∂x
i
= V
jωji
. (3.49)
(The map from V to µV is a linear map from the Lie algebra of H to the space of realvalued smooth functions on X.) We fix possible additive constants in the µV by requiring
that these functions vanish identically on Y . This also ensures that the µV are odd under
complex conjugation. This follows from (3.48), since the vector fields V are even under
complex conjugation and ω is odd.
The downward flow equations of Morse theory have the beautiful property that ~µ is
conserved, in other words µV is conserved for all V . This follows from a straightforward
computation. We have
dµV
dt
=
∂µV
∂xi
dx
i
dt
+
∂µV
∂x
i
dx
i
dt
= −V
jωjig
ik
∂h
∂x
k
− V
jωji
g
ik ∂h
∂xk
. (3.50)
Since h is the real part of a holomorphic function I, we have ∂h/∂xi = i∂Im I/∂xi, ∂h/∂x
i =
−i∂ Im I/∂x
i
. On the other hand, the Kahler form ω and Kahler metric g obey ωjig
ik = iδk
j
,
ωji
g
ik = −iδk
j
. So
dµV
dt
= −V
j
∂ Im I
∂x
j
− V
j
∂ Im I
∂xj
= −ιV d Im I. (3.51)
The right hand side vanishes, since I is H-invariant.
45

A less computational explanation of this result can be found by observing that the gradient flow with respect to the Morse function Re I coincides with the Hamiltonian flow
with Hamiltonian Im I. (Here we regard X as a symplectic manifold with symplectic form
ω.) As usual, the moment map for H is a conserved quantity for the flow generated by an
H-invariant Hamiltonian.
We will call a critical G-orbit semistable if it contains at least one point with ~µ = 0 and
unstable otherwise. (If a semistable orbit is free or has only a finite stabilizer, we call it
stable.) Since ~µ is conserved along flows, and vanishes identically on Y , any critical G-orbit
that is connected to Y by a flow is semistable. So when we express the real integration
cycle CR = Y in terms of generalized Lefschetz thimbles associated to critical orbits, only
semistable critical orbits enter. Similarly, as we explain momentarily, in crossing a Stokes
surface, a cycle in the relative homology of X associated to a semistable critical orbit is
always re-expressed in terms of other cycles associated to semistable critical orbits. So the
analytic continuation of the integral Zf can always be described using the semistable critical
orbits only.
It remains to explain why Stokes phenomena connect semistable critical orbits only to
each other. Suppose that OG is a semistable critical G-orbit. It contains a distinguished
H orbit, namely the orbit W = OH with ~µ = 0. OG is the complexification of OH and
is topologically the cotangent bundle T
∗OH. The middle-dimensional homology of OH is
generated by W. Since ~µ is conserved along flows, any critical orbit to which W can be
connected by a flow has a point with ~µ = 0 and therefore is semistable.
In contrast to the middle-dimensional cohomology of a semistable G orbit, which is always
of rank 1, an unstable G orbit might have vanishing or more complicated middle-dimensional
cohomology. For G = SL(2, C), an example of an unstable orbit is CP1, whose middledimensional cohomology vanishes. (Since CP1
is a homogeneous space for H = SU(2), and
the condition ~µ = 0 is H-invariant, ~µ would have to vanish everywhere on CP1if it vanishes
anywhere; but if ~µ is identically zero, then (3.48) implies that V = 0 for all generators of H,
and the H action is trivial.) More generally, for any G, the flag manifold, which in general
can have a middle-dimensional cohomology of high rank, is an example of an unstable orbit.
3.3.4 More on Group Actions
Continuing the discussion of the last subsection, let Jσ be the Lefschetz thimble associated
to a semistable critical orbit OG
σ
. Jσ consists of the points that can be reached by downward
flow from OH
σ
, the points in OG
σ with ~µ = 0.
Suppose that we are given an integration cycle C and we wish to express it in terms of
46

the Jσ. C is a middle-dimensional, H-invariant element of the relative homology, and in
practice one is usually interested in the case that C lies in ~µ
−1
(0).
To find the coefficients in an expansion
C =
X
σ
nσJσ, (3.52)
one wants to intersect C with a dual set of cycles Kσ. The dual cycles should have a natural
pairing with the Jσ, such that
hJσ, Kτ i = δστ . (3.53)
As we have defined Jσ by downward flow from OH
σ ⊂ OGσ
, one’s first thought is to define
Kσ by upward flow from OH
σ
. This does not work well, since in this case the intersection of
Jσ with Kσ, rather than a single point, would be the orbit OH
σ
. (The algebraic intersection
number would equal the Euler characteristic of this orbit; for instance, it would vanish for
the case of a free orbit.) What one must do instead is to define Kσ by upward flow starting
from a suitable dual to OH
σ ⊂ OGσ
. The appropriate dual is a fiber of the cotangent bundle.
In other words, identifying OG
σ
as T
∗OH
σ
, we pick an arbitrary point qσ ∈ OH
σ
and write
OeH
σ
for the fiber of T
∗OH
σ
at qσ. Then Kσ, defined by upward flow from OeH
σ
, meets Jσ
precisely at qσ. (Kσ lies in a dual version of the relative homology, spanned by cycles that
are allowed to go to infinity along G orbits as well as in the region where the Morse function
becomes large.) Moreover, away from a Stokes curve, Kσ meets Jτ not at all if σ 6= τ . So
hJσ, Kτ i = δστ , and the coefficients in (3.52) are nσ = hC, Kσi.
Similar questions arise when one considers the jumping phenomena Jσ → Jσ+
P
τ mστJτ
in crossing a Stokes curve. The coefficients mστ is computed by counting downward flow
lines from OH
σ
to OeH
τ
. (Each such flow line is weighted by the sign of a certain determinant,
as described in section 4.1.2.) The asymmetry between the definitions of downwards and
upwards flowing cycles has an interesting consequence, which we will describe for the special
case that there are two types of critical orbits – trivial orbits and free orbits. Suppose that
the critical point set of an H-invariant Morse function h = Re I contains a critical point p
(located at ~µ = 0) and a free stable G orbit OG. In general (when allowed by conservation of
Im I), there may be flows from p to OeH, and the coefficient mpO that appears in a jumping
formula Jp → Jp + mpOJO may be nonzero. However, the coefficient mOp that counts flows
from OH to p always vanishes. A quick way to show this is to observe that by replacing OH
by an everywhere nonzero section of the cotangent bundle OG = T
∗OH → OH, such as the
section ~µ
−1
(c), where c is a nonzero constant, one can eliminate all flows from OH to p. So
the algebraic invariant counting such flows must vanish.
In a more general case in which the critical point set consists of several isolated points pσ
and several free orbits Oα, the coefficients mOα,pσ will vanish by the argument just indicated.
(All other coefficients may be nonzero in general.) This means that the subspace of the
relative homology generated by the cycles JOαis invariant under all jumping phenomena.
47

The subspace generated by the cycles Jpσ
is not invariant under jumping. This perhaps
surprising fact will be demonstrated in an explicit and useful example in section 3.4.2.
