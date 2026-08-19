---
doc_id: 210811825v1
doc_title: "for the award of Doctor of Philosophy of Loughborough University"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 9-163
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups Joseph Cook A Doctoral Thesis for the award of Doctor of Philosophy of Loughborough University — 1 sections: Introduction"
---
2 Background 25
2.1 Spectral theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2.2 Hyperbolic geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
2.3 Harmonic analysis onH . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
2.4 Representation theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
2.5 Selberg’s trace formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3 The Bolza Surface 50
3.1 Symmetry group of the Bolza surface . . . . . . . . . . . . . . . . . . . . 50
3.2 Length spectrum of the Bolza surface . . . . . . . . . . . . . . . . . . . . 55
3.3 Upper bounds on eigenvalues of the Bolza surface . . . . . . . . . . . . . 56
3.4 First eigenspace of the Bolza surface . . . . . . . . . . . . . . . . . . . . 64
3.5 Second eigenspace of Bolza surface . . . . . . . . . . . . . . . . . . . . . 85
4 The Klein Quartic 88
4.1 Systole of the Klein quartic . . . . . . . . . . . . . . . . . . . . . . . . . 88
4.2 Fenchel-Nielsen parameters of the Klein quartic . . . . . . . . . . . . . . 90
4.3 Spectral theory of the Klein quartic . . . . . . . . . . . . . . . . . . . . . 93
5 Concluding Remarks 98
A GAP Code for Bolza Surface 101
B GAP Code for Klein Quartic 105
C FreeFEM++ Code for Genus 2 108
D FreeFEM++ Code for Genus 3 120
viii
E FreeFEM++ Code for Genus 4 134
F Mathematica Code for Bolza Surface 140
G Alternative approach to proving Conjecture 3.12 143
ix
Chapter 1
Introduction
Paris, February 1809
ThecourtofNapoleonBonaparteﬁllswiththesoundofaHaydnmelody, asourperformer
teases a curious rotating glass cylinder with felt-covered rods. The performer is Ernst
Chladni, the “father of acoustics”. Upon ﬁnishing his concert, he proceeds to demonstrate
his experiments with acoustics to the emperor. These involve bowing a ﬁxed plate at
diﬀerent frequencies, and observing how the patterns made by sand on the plate change as
thefrequencyincreases. Thepatternsthatherecordedonasquareplateweredocumented
in his seminal work,Akusik.
Whilst the music of the clavicylinder is of little interest to the contemporary math-
ematician, the investigation of the patterns of sand on a vibrating plate, that is, the
nodal lines of Dirichlet eigenfunctions, remains an interesting problem. Napoleon him-
self remarked to Chladni that if one could apply some of the calculations involved in
the mathematical formulation of acoustics to areas curved in more than one direction, it
“could be useful for applications to other subjects as well” [76].
What do we understand by the term “curved in more than one direction”? Broadly
speaking, the curvature of a surfaceS at a pointpmeasures how much the surface diﬀers
from its tangent planeTpS, that is, how far away it is from being “ﬂat”. If the curvature
is constant, then this measure takes the same value for everyp∈ S. For a simple
example of a surface of constant curvature, one can consider the sphere. There are
several diﬀerent notions of curvature; in this work we predominantly consider Gaussian
curvature. The normal vectorn forms a plane with each vectorv in TpS2, with each
directionvcorresponding the direction of a curve on the surface. The principal curvatures
κi are the (orthogonal) directions that give the maximum and minimum “bending” ofS
atp. The Gaussian curvature is then deﬁned at a pointp as the product of the principal
1
curvatures, that is,
K =κ1(p)κ2(p).
Figure 1.1: Principal directions at a pointp on S2
n
κ1(p)
κ2(p)
When dealing with surfaces of constant Gaussian curvature, there are three main
cases: whenK is positive, when it is negative, and when it is zero. We call these surfaces
spherical, ﬂat or hyperbolic. Having positive Gaussian curvature means that the principal
curvatures atpcurve “in the same way”, so the area aroundpresembles a cap. Conversely,
negative curvature implies that the principal curvatures curve in diﬀerent directions, so
p is both a maximum and a minimum. Every point on a hyperbolic surface resembles
a saddle, or indeed, a Pringle. Hitherto, we have alluded to the notion of surfaces, but
have not said precisely what we mean. We take this opportunity to formally introduce
the setting for the analysis in this work.
Deﬁnition 1.1 (Riemann surface)A Riemann surface is a two (real) dimensional,
orientable Riemannian manifold. The preﬁx “Riemannian” indicates that a smooth man-
ifold has a Riemannian metric, that is, a smooth family of inner productsgp(·,· ) such
that
gp :TpM×TpM→ R
depends smoothly onp∈M.
IfX andY areC∞ vector ﬁelds onM, then their inner product with respect to the
Riemannian metric is aC∞ real valued function onM. The Riemannian metric gives us
a consistent way of measuring angles on the surface, and thus endows the surface with a
conformal structure.
The property of being orientable means that one can make a consistent choice of
normal vector on the surface, that is, we can move a normal vector along a closed loop
continuously, without it changing sign. Figure 1.2 shows the Möbius strip, which is an
example of a manifold that is not orientable. To see this, move the outward pointing
2
normal vector around the closed loop. When it returns to its original position, it will be
inward pointing, so the Möbius strip is not orientable. If we ﬁx a an orientation (normal
vector) on a surface, we say that it is oriented. Where a surfaceS has boundary, we deﬁne
an orientation on its interior, and this in turn induces an orientation on the boundary
∂S.
These additional conditions on a smooth manifold of two real dimensions allow us
to give the manifold a complex structure. This leads us to an alternative deﬁnition of
a Riemann surface as a connected, one (complex) dimensional complex manifold. The
complex structure allows us to deﬁne holomorphic functions between Riemann surfaces;
in particular, the transition maps are holomorphic.
Figure 1.2: The Möbius strip is not orientable
The Bolza surface and Klein quartic are interesting because they have maximal sym-
metry among hyperbolic surfaces in their respective topological classes. The topological
invariant that we use to classify such surfaces is the genus.
Deﬁnition 1.2 (Genus)The genus of a connected, orientable surface is the maximum
number of simple, closed, non-intersecting curves that one can cut along such that the
resulting surface remains connected.
For example, the genus of the torus is 1, because one can cut along a simple, closed
curve to obtain a cylinder, but another such cut would result in two cylinders. The
genus may also be thought of as the number of handles glued onto a sphere; one sees
straightaway that the sphere has genus 0. The Bolza surface has genus 2, and the Klein
quartic has genus 3.
The following theorem provides a link between the geometry of a surface and its
topology (see, for example, [16]).
Theorem 1.3 (Gauss-Bonnet)LetS be a compact Riemann surface without boundary,
with Gaussian curvatureK. Then
∫
S
KdA = 2πχ(S),
3
wheredA is the area measure of S, andχ(S) is its Euler characteristic.χ(S) is another
topological invariant, and can be calculated from the genusg using the formula
χ(S) = 2− 2g.
Remark 1.4For compact Riemann surfaces of constant curvature, the uniformization
theorem (introduced in Section 2.2.1) enables us to normalize the Gaussian curvature
to K =±1 or K = 0, depending respectively on whether the surface is positively or
negatively curved, or ﬂat. On surfaces of constant negative curvature, the Gauss-Bonnet
theorem then implies
Area(S) = 4π(g− 1),
whereg is the genus of the surface.
Napoleonshowedgreatforesightinhiscommentregardingthestudyofcurvedsurfaces.
He was (inadvertently, one supposes) predicting an arena for the study of: the Helmholtz
wave equation
∇2A−k2A = 0,
where∇2 is the Laplacian,A is the amplitude andk is the wave number; the stationary
wave equation (
∇2− 1
c2
∂2
∂t2
)
u(x,t) = 0;
and the Schrödinger equation
HΨ =EΨ, (1.1)
whereH is the Hamiltonian andE is the energy of the stateΨ. We will examine this
third equation shortly in the context of the Bolza surface.
Although spectral theory in a Euclidean setting was commonplace in physics prior to
the 1950s, during this decade the geometry and spectra of hyperbolic surfaces became an
avenue of interest for quantum physicists. These surfaces provide a model for studying
quantum chaos; Selberg’s trace formula helped to bridge the gap between classical and
quantum mechanics.
We will study the Laplace-Beltrami operator acting on functions on compact Riemann
surfaces of constant negative curvature, in particular, thoseφi that solve the equation
∆φi−λiφi = 0, (1.2)
where the eigenvaluesλi form a discrete spectrum
0 =λ0<λ 1≤λ2≤....
This is a heuristic overview of the problem. In the following section, we give details
of the diﬀerent boundary value problems on the surfaces that we consider. We go into
4
greater detail about the formulation of Equation (1.2) in Section 2.1, where we deﬁne
the Laplacian and its domain, and prove that the eigenfunctionsφi exist and form an
orthonormal basis of theL2 space of functions on the surface.
The interplay between hyperbolic surfaces and Fuchsian groups gives us additional
tools to analyze their spectral theory. In Chapter 2, we give an outline of hyperbolic
geometry, and the analytical methods used to investigate the spectra of these surfaces.
We introduce Selberg’s trace formula (Theorem 2.47), and give a generalization to cases
where an isometry group is acting.
Eigenvalue Problems
A topic of central interest in this work is the eigenvalue spectrum of the Laplacian cor-
responding to a particular closed or boundary value problem, which will take the form
of one of the following. We follow the deﬁnitions of [15]. The Riemann surfaces that
we consider have no boundary, so their eigenvalues and eigenfunctions satisfy the closed
eigenvalue problem:
Deﬁnition 1.5 (Closed eigenvalue problem)For a connected, compact surfaceM,
ﬁnd allλ∈ R such that
∆φ−λφ = 0
has nontrivial solutionsφ∈C2(M).
In practice, we will not tackle the closed eigenvalue problem head on. It is not possible
to calculate such eigenvalues explicitly, and the surface as a whole is often too compli-
cated to analyze. Rather, we will use the symmetry of the surface to break the closed
problem down into one of the following, where we consider a boundary value problem on
a subspace of the surface. We deﬁne the following problems on the more general setting
of a connected, smooth, oriented Riemannian manifoldM. Additional conditions will
be speciﬁed. Giving the deﬁnitions on general manifolds will allow us to consider these
problems on sub-manifolds later.
Deﬁnition 1.6 (Dirichlet eigenvalue problem)For∂M⁄=∅, M compact and con-
nected, ﬁnd allλ∈ R such that
∆φ−λφ = 0
has nontrivial solutionsφ∈C2(M)∩C0(M) that satisfy the boundary condition
φ = 0
on∂M.
5
Ω1
Ω2
Ω3
Figure 1.3: Domain monotonicity for a torus with a disk removed
Remark 1.7 (Domain monotonicity, Dirichlet data)Unless otherwise stated, “do-
main” refers to an open, connected subset inM with compact closure. Ideally, whenΩ is
a subset of a compact Riemann surface, its boundary∂Ω will be a smooth curve. In prac-
tice, this is not always the case; some of the domains we wish to consider have piecewise
smooth boundary, by which we mean that the boundary is formed as the ﬁnite union of
smooth curves. Let
Ω1,..., Ωm
be pairwise disjoint domains with piecewise smooth boundary and compact closure inM.
If M has boundary, the boundary ofΩi, i = 1,..., m, meets∂M tranversally. For
example, in Figure 1.3,M is a torus with a disk removed,∂M is a circle, and we have
three pairwise disjoint domains. Fori = 1,..., m, consider the Dirichlet eigenvalue
problem on∂Ωi∩M (where∂M⁄=∅, we do not impose a constraint on∂Ωi∩M). We
arrange all the eigenvalues of these domains into the increasing sequence
0≤ν1≤ν2≤...
repeated according to multiplicity. Then forλk in the Laplace spectrum ofM, we have
λk≤νk
for allk∈ N.
A useful corollary of this is that for a Dirichlet eigenvalue problem onΩ⊂M and any
eigenvalue problem onM, we have
λk(Ω)≥λk(M)
for allk∈ N. For example, in Figure 1.3 the ﬁrst (and indeedkth) Dirichlet eigenvalues
of Ω1, Ω2, and Ω3 will all be larger than the ﬁrst (respectivelykth) eigenvalue of the
manifold in which they are contained, that is, the torus with a disk removed, where we
impose Dirichlet conditions on the boundary circle.
6
Our survey of spectral theory in Section 2.1 will focus on the “Dirichlet Laplacian”,
that is, the Laplace operator associated with the above problem. Another important type
of boundary condition is the Neumann problem.
Deﬁnition 1.8 (Neumann eigenvalue problem)For∂M⁄=∅, M compact and con-
nected, ﬁnd allλ∈ R such that
∆φ−λφ = 0
has nontrivial solutionsφ∈C2(M)∩C1(M) that satisfy the boundary condition
∂φ
∂n = 0
on∂M, where ∂
∂n is the outward unit normal vector ﬁeld on∂M.
Remark 1.9 (Domain monotonicity, Neumann data)Let
Ω1,..., Ωm
be as above. Considering now the Neumann eigenvalue problem, where the normal deriva-
tive of the eigenfunction is required to be 0 on∂Ω∩M, we arrange all the eigenvalues of
these domains into the increasing sequence
0≤µ1≤µ2≤...
repeated according to multiplicity. Then forλk in the Laplace spectrum ofM, we have
µk≤λk
for allk∈ N.
Finally, it is possible to have a boundary value problem that requires both Dirichlet
and Neumann conditions.
Deﬁnition 1.10 (Mixed eigenvalue problem)For∂M ⁄=∅, M compact and con-
nected compact and connected,N an open submanifold of∂M, ﬁnd allλ∈ R such that
∆φ−λφ = 0
has nontrivial solutionsφ∈ C2(M)∩C1(M∪N)∩C0(M) that satisfy the boundary
conditions
φ = 0on∂M−N, ∂φ
∂n = 0onN.
Using the symmetry group of a hyperbolic surface, we can reduce the closed problem
on the surface to a simpler Dirichlet, Neumann or mixed problem on a fundamental
domain of the group action on the surface. Useful to this approach is the concept of
7
nodal lines and nodal domains, that is, the points on which the eigenfunction is zero and
how they partition the domain. This has an obvious link to Dirichlet boundary problems,
and we hope to exploit the connection in Section 3.4.
Deﬁnition 1.11 (Nodal domain)LetS be a closed Riemann surface and
C0(S)∋f :S→ R.
The nodal set off isZf ={f−1(0)}, and each connected component of
S\{f−1(0)}
is a nodal domain off.
Theorem 1.12 (Courant’s nodal domain theorem, [19])Consider a Neumann
eigenvalue problem onM,∂M⁄= 0,M compact and connected with eigenvalues
0 =λ0≤λ1≤λ2≤...
corresponding to the complete orthonormal basis of eigenfunctions{φ0, φ1,...}ofL2(M).
The number of nodal domains ofφk is≤k + 1.
Now consider a Dirichlet eigenvalue problem on the same region, with eigenvalues
0<λ 1≤λ2≤...
corresponding to the complete orthonormal basis of eigenfunctions{φ1, φ2,...}ofL2(M).
Then the number of nodal domains ofφk is≤k.
A classic paper on the nodal sets of eigenfunctions is [18], where it is proved that
for the Laplace operator acting on functions on a Riemannian manifold, the nodal sets
of eigenfunctions are smooth sub-manifolds, apart from a closed set of lower dimension.
Cheng also generalizes Theorem 1.12 to manifolds of higher dimension, and proves that
for a Riemann surfaceS andV∈C∞(S), a solutionϕ of the Schödinger equation
(∆ +V )ϕ = 0
with nodal setZϕ has isolated critical points onZϕ, and the meeting points of nodal lines
form an equiangular system.
A survey of historical results relating to the nodal sets of the Laplacian on surfaces of
variable curvature is given in [85]. In more recent years, there have been some interesting
results linking the topology of nodal sets to the spectrum of∆; Otal and Rosas proved
an initial result in 2009 [66] that for a compact, orientable, hyperbolic surfaceS of genus
g,
λ2g−2(S)> 1
4. (1.3)
8
The value2g− 2 is of course equal to−χ(S), the Euler characteristic ofS. This is the
ﬁnite area version of the classical result by Buser [12], that for every hyperbolic surface
of genusg≥ 2
λ4g−2(S)> 1
4.
The proof of Equation (1.3) uses a novel technique in which the topology of the nodal
sets of eigenfunctions is considered, and the analysis is done separately for nodal sets
that are topologically equivalent to a cross cap, an annulus or a disk. The constant1
4 is
signiﬁcant, because in many applications of spectral theory it is important to distinguish
the two cases when an eigenvalueλ≥ 1
4 and whenλ <1
4. This comes from the fact the
the function
x↦→ sin
(
x
(
λn− 1
4
)1
2
)
is bounded in the ﬁrst case but grows exponentially in the second, asx→ ∞[13].
1
4 is well known to be the bottom of the spectrum of the hyperbolic plane. For this
reason, eigenvalues in the interval[0, 1
4
] have the special title ofsmall eigenvalues. For
a compact Riemann surfaceS, the small eigenvalues of∆(S) inﬂuence the asymptotic
length distribution of its closed geodesics (see, for example, [21,73]). In the same paper,
Otal and Rosas prove that any ﬁnite area hyperbolic surface of genusg withn holes has
at most2g− 2 +n small eigenvalues.
Following the techniques of [66], Mondal proved several results that use the topology of
nodal sets of Laplace eigenfunctions to give bounds on small eigenvalues of the spectrum
that depend on the systole of the surface, that is, the length of the shortest closed geodesic
(not necessarily unique). The systole of a Riemann surfaceS will be denoteds(S). It has
a multiplicity corresponding to the number of non-homotopic geodesics of minimal length
that cannot be contracted. Starting with the main result (in this area) of his thesis [57],
published in [58], he proved that forS closed and hyperbolic,
λ2g−2(S)> 1
4 +ϵ0(S),
where
ϵ0(S)< min
{
1
4(g− 1), 1
4
((cosh(ρ0)
sinh(ρ0)
)2
− 1
)}
and
2s(S) sinh(ρ0) = Area(S).
More results of a similar nature can be found in papers such as [58–60]. In joint work with
Ballmann and Matthiesen [4], he proved that a closed Riemann surfaceS with negative
Euler characteristic has at most−χ(S) small eigenvalues. This paper generalizes earlier
9
results, including Equation (1.3), by removing the restriction that the surface must be of
negatively curved, that is, it is true for arbitrary Riemannian metrics.
Comparing eigenvalues
In general, we cannot compute eigenvalues of surfaces, or domains within surfaces, ex-
plicitly. There are several analytical tools that use the geometry of the surface to create
both upper and lower bounds on particular eigenvalues. To bound eigenvalues from be-
low, we can compare them to the eigenvalues of disks having equivalent area; these are
known to minimize the eigenvalue provided a certain condition is satisﬁed, namely the
isoperimetric inequality:
Deﬁnition 1.13 (Isoperimetric inequality)LetD be an open disk in the hyperbolic
plane H (see Section 2.2 for a discussion on hyperbolic geometry). An open domainΩ in
a hyperbolic surfaceS is said to satisfy the isoperimetric inequality if
A(Ω) =A(D) =⇒ l(∂Ω)≥l(∂D),
with equality if and only ifΩ is isometric toD, whereA(Ω) denotes the area ofΩ, and
l(∂Ω) denotes the length of its boundary.
Caution must be used with this deﬁnition, since there exists a whole class of results
called isoperimetric inequalities that relate the area of a domain to its perimeter, and
do not take into account physical properties such as torsional rigidity. Isoperimetric
inequalities are said to have their origins in ancient Carthage, where Queen Dido was
tasked with delimiting the boundary of her new city, such that it would occupy a region
that could be encompassed by a single ox-hide. Legend has it that she cut the hide
into long thin strips and chose a circular boundary, having conjectured that this would
maximize the area of land. More succinctly we have the famous formula
L2≥ 4πA,
where a curveC of lengthL encloses a region of areaA, and equality holds if and only
if C is a circle. We take this form of the inequality from [65], where Osserman gives
an interesting historical exposition of signiﬁcant results following on from this classical
theorem.
The term isoperimetric inequality is used interchangeably in the literature for problems
oftheabovetype, andthoseofmorerelevancetothiswork: isoperimetricproblems, where
(often) variational calculus is used to show that in a certain class of domains, a physical
property is shown to be extremal for radially symmetric regions. In [67], Payne gives a
10
similar treatise to that of Osserman, covering the extension of isoperimetric inequalities
to physical properties of surfaces. Whilst being a thorough survey of key research up
to 1967, the fact that the spectral theory of surfaces is still a hot topic means that this
reference is good introduction to early work in the ﬁeld but is far from complete. A
slightly more up to date survey article is given by Ashbaugh [1]. This mainly pertains to
the Laplacian on Euclidean domains, but as one sees in [15], many of these results can
be generalized to diﬀerent geometries, including hyperbolic.
Of course, here the physical property we are interested in is eigenvalues; in particular,
λ1. The most important result is the following, which gives a lower bound on the ﬁrst
positive eigenvalue of a domainΩ satisfying Deﬁnition 1.13.
Theorem 1.14 (Faber-Krahn inequality)Let Ω be an open domain in a hyperbolic
surfaceS, andD be a disk in hyperbolic space (more information on such disks is given
in Section 2.3.1). IfΩ satisﬁes the isoperimetric inequality, then
A(Ω) =A(D) =⇒ λ1(Ω)≥λ1(D),
whereλ1 is the ﬁrst Dirichlet eigenvalue.
To prove the Faber-Krahn inequality, the levels sets of eigenfunctions on an open
domain are radially symmetrized so that the ﬁrst Dirichlet eigenvalue can be compared
to that of a geodesic disk with equal area. This theorem can be stated more generally for
n-dimensional manifolds satisfying an equivalent isoperimetric property; details can be
found in [15]. While Theorem 1.14 is a powerful tool for analyzing domains that satisfy
Deﬁnition 1.13, not every domain that we will study has this property. In particular,
domains in surfaces that resemble annuli can have a boundary that is shorter than that
of the disk with equal area.
Another tool for creating lower bounds onλ1 is Cheeger’s inequality. For the cases
investigated in this work, it is not as strong as the Faber-Krahn inequality, so we will
not actually use it. However, we state it as a key result in the theory of isoperimetric
problems.
Deﬁnition 1.15 (Cheeger constant)LetM be a non-compact Riemann manifold of
dimensionn≥ 2, possibly with boundary, and possibly having compact closure. The
Cheeger constanth(M) is deﬁned as the following inﬁmum:
h(M) = inf
Ω
l(∂Ω)
Area(Ω),
where Ω ranges over all open domains ofS with compact closure and smooth boundary
andl(∂Ω) denotes the length of the boundary ofΩ.
11
Theorem 1.16 (Cheeger’s inequality, [17])For Ω⊂S as above, we have
λ1(Ω)≥ h2(Ω)
4 .
We will also be interested in creating upper bounds on eigenvalues. In his classic trea-
tise on acoustics [69], Rayleigh gave a variational characterization of the ﬁrst eigenvalue
for the Dirichlet problem. This involves taking the gradient of a function. We stated
earlier that the eigenfunctions of the Laplacian on a compact Riemann surfaceS form an
orthonormal basis ofL2(S). Recall thatL2(S) is the space of square integrable functions
onS, that is, a functionf onS is inL2(S) if
∫
S
|f|2dS≤∞.
wheredS is the Riemannian measure onS. L2(S) is special among theLp(S) spaces
because its inner product
⟨f, g⟩L2 =
∫
S
fgdS
makes it a Hilbert space. The inner product induces the norm
‖f‖2 =⟨f, f⟩L2.
Note that theL2 norm gives no indication about how smooth a function is. When
we apply the Laplacian, we may therefore uncover huge (or indeed, undeﬁned) second
derivatives, even if theL2 norm of a function is small. The Laplacian is unbounded on
L2(S)and operations such as taking the gradient off∈L2(S)simply do not make sense.
Therefore, we need to formulate a diﬀerent space of functions before we can introduce
Rayleigh’s principle. Rather than considering the whole space of square integrable func-
tions, we will work with those functions inL2(S) for which we can deﬁne a reasonable
notion of diﬀerentiability. First consider the multi-index
α = (α1,..., αd), α j∈ N
of order
|α| :=
d∑
i=1
αi,
and forψ(x) : Rd→ C suﬃciently smooth, deﬁne
Dαψ(x) := ∂|α|ψ(x)
∂xα1
1 ...∂x αd
d
.
For convenience, we deﬁneD1ψ(x) to be the gradient∇ψ(x) and D2ψ(x) to be the
Hessian matrix forψ(x), the trace of which is equal to∆ψ(x). We are now ready to
deﬁne our notion of diﬀerentiability.
12
Deﬁnition 1.17 (Weak derivative)Letψ and g be locally integrable functions on a
domainΩ⊂S. We say thatg is theαth-weak partial derivative ofψ if for allϕ∈C∞
0 (Ω),
∫
Ω
ϕ(x)g(x)dx = (−1)|α|
∫
Ω
Dαϕ(x)ψ(x)dx.
With the weak derivative, we can now deﬁne the spaces of functions on which we
consider our eigenvalue problems, namely, Sobolev spaces. In Section 2.1, we will see
how to extend the Laplacian on these spaces to a self-adjoint operator onL2(S), but for
now, we simply give enough detail to deﬁne the subsequent “variational” theorems.
Deﬁnition 1.18 (Sobolev space)Let Ω be as above. The Sobolev spaces, indexed by
p∈ [1,∞) andk∈ N, are given by
Wk,p :={ψ∈Lp(Ω)|Dαψ∈Lp(Ω), 0≤|α|≤ k},
and are complete with respect to the Sobolev norm
‖ψ‖Wk,p :=

 ∑
0≤|α|≤k
‖Dαψ‖p
Lp(Ω)


1
p
whereDαψ is the weak partial derivative. We may also deﬁneWk,p
0 (Ω)as the closure of
C∞
0 (Ω)with respect to the Sobolev norm.
Remark 1.19Again, we are most interested in the case wherep = 2, sinceWk,2(Ω) is
a separable Hilbert space with inner product
⟨φ, ψ⟩Wk,2 =
∑
0≤|α|≤k
⟨Dαφ, Dαψ⟩L2.
The variational characterization of the Laplacian (and its associated eigenvalue prob-
lems) is concerned with the validity of the formula
⟨∆φ, f⟩L2 =D[φ,f ],
where theφ is typically an eigenfunction, and the quantity on the right is the Dirichlet
integral
D[f,h] :=⟨D1f, D1h⟩L2
forf, h∈W1, 2(Ω)in the case when we consider a closed or Neumann problem andf, h∈
W1, 2
0 (Ω)when we consider a Dirichlet problem.D1 denotes the ﬁrst weak derivative. We
can now state the following theorems as in [15].
13
Theorem 1.20 (Rayleigh’s theorem)LetS be a closed and connected Riemann sur-
face,Ω⊂S be a domain with compact closure and non-empty piecewise smooth boundary.
Consider a ﬁxed eigenvalue problem onΩ with eigenvalues
λ1≤λ2≤...
repeated according to multiplicity. For any0⁄=f∈W1, 2(Ω)in the case when we consider
a closed or Neumann problem, and0⁄= f ∈ W1, 2
0 (Ω) when we consider a Dirichlet
problem,
λ1(Ω)≤D[f, f]
‖f‖2 ,
with equality if and only iff eigenfunction corresponding toλ1. The object on the right
is called the Rayleigh quotient, and will be denotedR(f).
We can use Rayleigh’s quotient to characterizeλk for anyk. In particular, we have
the following pair of theorems, taken from [6]:
Theorem 1.21 (Max-min)LetM be a smooth, connected, compact manifold, possibly
with boundary∂M. For the Neumann eigenvalue problem onM, or closed eigenvalue
problem where∂M =∅, we have
λk = sup
Vk
inf{R(f)|f⁄= 0, f⊥Vk},
whereVk runs through thek-dimensional subspaces ofW1, 2(M). We consider the
(k− 1)-dimensional subspaces ofW1, 2
0 (M) for the Dirichlet eigenvalue problem onM.
Theorem 1.22 (Min-max)LetM be as above. For the Neumann eigenvalue problem
onM, or closed eigenvalue problem where∂M =∅, we have
λk = inf
Vk
sup{R(f)|f⁄= 0, f∈Vk},
whereVk runs through the(k + 1)-dimensional subspaces ofW1, 2(M). We consider the
k-dimensional subspaces ofW1, 2
0 (M) for the Dirichlet eigenvalue problem onM.
Remark 1.23In this work, we use Theorem 1.22 in Section 3.3 to produce an upper
bound on the second positive eigenvalue of the Bolza surface. We do not actually use its
sister theorem at any point, but include it for completion.
The eigenvalues in the spectrum of the Laplacian on a compact Riemann surface are
known to have ﬁnite multiplicity; it is a reasonable question to ask what this multiplicity
is, and and whether it is possible to bound the multiplicity for a given eigenvalue ei-
ther from below or above. We will see in Section 2.4 that the multiplicities of a compact
14
Riemann surface are connected to the irreducible representations of its group of automor-
phisms. Well established results are that0 =λ0 has simple multiplicity for the Laplacian
on a closed, connected surface, and for a Schrödinger operator with a smooth potential,
the ﬁrst eigenvalue, whilst not necessarily 0, also has multiplicity one [5,15].
For a Schrödinger operatorH on a surfaceS, Cheng [18] bounded the multiplicitym1
ofλ1 by a quantity that is quadratic inχ(S), with the corollary that for the Laplacian
on the sphereS2 with the standard round metric,m1(S2) = 3. Besson improved this
to a bound that is linear inχ(S) [7], highlighting that for the projective planeP2 with
round metric, and the ﬂat torusT2, we havem1(P2) = 5 andm1(T2) = 6 respectively.
Nadirashvili slightly improved the linear bound to
m1(S) = 5− 2χ(S)
for surfacesS with negative Euler characteristic [62]. Sévannec [75] improved this bound
for surfaces for surfaces of negative Euler characteristic, asymptotically by a factor of 2.
In particular, he proved the following
Theorem 1.24LetS be a closed surface. Ifχ(S)< 0, thenm1(S)< 5−χ(S).
Example 1.25Theorem 1.24 already provides upper bounds for the multiplicities of the
ﬁrst eigenvalues of the Bolza surface and Klein quartic. Recall that the Euler character-
istic of a surfaceS may be given in terms of the genusg as
χ(S) = 2− 2g.
Hence, for surfaces of genus 2,m1(S)< 7 and for surfaces of genus3,m1(S)< 9.
The Bolza surface
In Chapter 3, we will look at the speciﬁc case of the Bolza surface, denoted byB, which
can be obtained by identifying opposite edges of a regular octagon in the Poincare disk
D. The vertices are at the points
2−1
4e
πik
4 , k = 0, 1,..., 7,
andare joinedbygeodesicsegments ofequallength. Thegroupof (orientationpreserving)
symmetries ofBis GL2(Z3), which has order 48 (see, for example, [46,51]). The full group
of isometries, including reﬂections, is the semi-direct productGL2(Z3) ⋊ Z2. This is the
highest order of a symmetry group for any genus 2 surface [51]. The Bolza surface takes
its name from Oskar Bolza, a student of Klein, who investigated algebraic curves; in
15
particular binary sextic equations with linear transformation into themselves [8]. The
algebraic curve for the Bolza surface is
w2 =z(z4− 1), (1.4)
wherew andz are two functions.
Figure 1.4: The Bolza surface inD
1
23
4
5
6 7
8
Side associations:
1 – 5, 2 – 6, 3 – 7, 4 – 8
The Bolza surface has attracted the attention of spectral theorists, as it is conjectured
to be the surface that maximizes the ﬁrst positive eigenvalue of the Laplace operator
among all compact Riemann surfaces of genus two with constant negative curvature.
The conjecture is given in [77], and is based on numerical calculations carried out by the
authors. This is thought to be related to the fact that the Bolza surface has the largest
automorphism group in this class of surfaces. As well as having maximal symmetry in
this class, the Bolza surface also maximizes the systole [72], which Jenni [41] showed to
be
s(B) = 2 arccosh
(
1 +
√
2
)
and have multiplicity 12. These are the four associated edges in Figure 1.4, the four
diameters ofD connecting their midpoints, and the curves that connect the midpoint of
one edge with the midpoint connecting the adjoining edge. The formula for the systole
follows immediately from the side lengths of the(2, 3, 8) triangles that tessellate the
surface (see, for example, Figure 3.3). The systole of the Bolza surface was considered
in [47], where it was conjectured to be optimal for the systolic ratio
SR(S) = sup
G
s(G)2
AreaG(S)
16
of CAT(0) metricsG on surfacesS of genus 2 (that is, metrics of negative curvature
including those that are singular).
It is the same work by Jenni [41] that inspired the method for the investigation of
the Bolza surface in this work. He investigated the class of Riemann surfaces of genus
g, labelledFg, obtained by associating the opposite sides of a regular4n-gon with angles
π
2g. In this class, all the surfaces have one rotational and two reﬂective symmetries; the
Bolza surface stands out because it has an extra rotational symmetry, due to the fact
that the regular octagon can be tessellated by equilateral triangles (see Figure 3.1); the
curves that make up this tessellation are the 12 geodesics with length equal to the systole
of the surface. As well as his results on the Bolza surface, he also proved that forg >2,
Fg has 2g such curves of length
s(Fg) = 4 arccosh
(√
2 cos
(π
4g
))
.
Forg≥ 20, he identiﬁed the group representation that appears in the ﬁrst eigenspace of
Fg, proved that the ﬁrst eigenvalue has multiplicity 2, and also proved that
lim
g→∞
g·λ1(Fg) = 2.
Using the same methodology, he proved similar results on the ﬁrst eigenvalues of a surface
of genus 2 in [42], where the surface varies by changing the lengthl(µ) of one of the sides
µ that make up its fundamental domainFµ. In particular,
lim
l(µ)→0
l(µ)
λ1(Fµ) =π2.
This surface does not have any obvious maximal properties.
The Bolza surface has been investigated in the context of eigenvalue maximization
in [39]. Here the authors look at the surface as a ramiﬁed double cover of the sphere
where
Π :P→ S2
is a degree 2 branched cover of the sphere, andP is a surface of genus 2 with the conformal
structure of the Bolza surface, that is,
P :=
{
(z,w )∈ C|w2 =F(z) :=z(z− 1)(z−i)
(z + 1)(z +i)
}
.
It has been shown by Yang and Yau [84] that for non-constant holomorphic maps of
degreed from a closed, orientable Riemann surfaceS to S2, the ﬁrst positive eigenvalue
λ1 ofS satisﬁes the following inequality
λ1(S)Area(S)≤ 8πd. (1.5)
17
This built on Hersch’s result [34] that for any metricg on S2,
λ1(g)Areag(S2)≤ 8π,
whereλ1(g) and Areag refer to the ﬁrst eigenvalue and area with respect to the metric
g. It was extended to non-orientable surfaces by Li and Yau in [54], where they showed
that for and metricg on the real projective planeRP2
λ1(g)Areag(RP2)≤ 12π.
Similar inequalities hold for an orientable surfaceS of genusγ immersed intoR2+p,
that is,M =X( ¯M) where ¯M is a compact orientable surface andX : ¯M→ R2+p is an
immersion. In this case, Ilias and El Souﬁ [22] improved the bound of Yang and Yau to
λ1(S)Area(S)≤ 8π
⌊γ + 3
2
⌋
, (1.6)
where⌊·⌋ is the ﬂoor function. For example, the Bolza surface has area4π by the
Gauss-Bonnet theorem, so we may use Equation (1.6) to state
λ1(B)≤ 4,
when we view the Bolza surface as an immersed surface inR2+p.
For surfaces of genus 2, we can taked in Equation (1.5) to be 2; further information
can be found in [29], which also gives background information on many of the concepts
in this section relating to algebraic geometry, that will not reappear in the main body of
this work. The Bolza surface has 6 ramiﬁcation points, by the Riemann-Hurwitz formula.
These are called the Weierstrass points of the surface and they occur at
{0,∞,±1,±i}.
Note that0 and∞ are ﬁxed points of Equation (1.4), and0,±1, and±i are its roots
whenw = 0. These points are singularities of the metricg0 onP that is inherited from
S2 by pulling back the round metric. In [39], the following conjecture is made
Conjecture 1.26The metricg0 onP gives equality in Equation(1.5), that is
λ1(P,g 0)Area((P,g 0)) = 16π.
As part of their investigation into this conjecture, the authors reduce a spectral prob-
lem onS2 to a mixed boundary problem on the semicircle. Of particular interest is the
fact that the two problems in Figure 1.5 are isospectral under an exchange of Dirich-
let and Neumann conditions. This phenomenon, known as “Dirichlet-Neumann swap
isospectrality”, is investigated further in [40], where the authors explain how to construct
18
an isospectral domain. It was encountered in this work during the investigation of the
4-dimensional irreducible representations of the Bolza surface (see Section 3.4), where nu-
merical results indicate that the hyperbolic pentagon with mixed boundary conditions,
shown in Figure 1.6, also has the property of swap isospectrality. The relevant ﬁnite
element code is included in Appendix C.
Figure 1.5: Boundary value problems on a semicircle, [39] (dashed lines indicate a Neumann boundary
condition, and solid, Dirichlet)
Figure 1.6: Boundary value problems on a pentagon
In the above case, the conformal structure of the Bolza surface was investigated as a
double cover of the sphereS2, however, genus 2 surfaces are also ramiﬁed double covers
of the Riemann sphere [24]. The double cover consists of two sheets, and there is a
function,J, called thehyperelliptic involutionthat switches between the sheets. In the
case of the Bolza surface, the involution is the centre of the full isometry group (see
Proposition 3.5). The hyperelliptic involution leaves geodesics invariant, and its ﬁxed
points are the Weierstrass points of the surface [31]. For the Bolza surface, we have seen
that the Weierstrass points are{0,±1,±i,∞}.
Suppose we start in the Riemann sphere and draw the geodesics that connect our
Weierstrass points to get a cross (see Figure 1.7). The line from 1 to∞ is dashed; the
complement of the cross joining the other ﬁve points is simply connected, but this fails to
be the case when we add∞. Thus,∞is a branch point when we lift to the cover. When
19
we lift, angles are preserved, except at Weierstrass points where they are halved. On the
picture on the left of Figure 1.7, imagine taking the following journey: start at∞, walk
to 1, carry on to walk to 0, turn byπ
2, walk toi, turn right around and walk back to 0.
Carry on moving around the cross until arriving back at 1, and then carry on to∞.
When we lift to the surface, the angles are halved at Weierstrass points, so the same
journey becomes: start at∞, walk to 1, turn byπ
2, walk to 0, turn byπ
4, walk toi,
carry on and walk to 0. Continuing the journey takes us around the upper half on the
octagon on the right hand side of Figure 1.7. This is one sheet of the cover; the other is
its conjugate. They are glued together along the dotted line.
Figure 1.7: Creating a double cover of the Riemann sphere
−1 1
i
−i
∞0
0
0
0
0 0
0
0
0
i
−1
−1
∞
i
1
−i
−i
1
We will see in Section 3.4 that an eigenfunction in the ﬁrst (non-trivial) eigenspace
has as its nodal lines one line of a(4, 4, 4)triangle, and its rotations around the centre of
the fundamental polygon (the notation for such a triangle is explained in Section 2.2.3).
When we take the quotient of the Bolza surface by the hyperelliptic involutionJ, the
centre points of the 16(4, 4, 4) triangles will map to 8 points on the Riemann sphere.
These 8 points give a cubical subdivision of the quotient surface that is dual to the subdi-
vision obtained from the 6 ramiﬁcation (or Weierstrass) points that induce an octahedral
symmetry. Using the numerical results in Appendix C, we can plot the values of the three
eigenfunctions corresponding toλ1 in R3; this is shown in Figure 1.8. One can clearly
see the octahedral symmetry, as well as 5 of the 6 singular points that come from the
ramiﬁcations (the other is at the rear). It appears that the eigenfunctions corresponding
toλ1 provide an immersion intoR3; for a symmetric image such as the one in Figure 1.8,
one should take the eigenfunctions to be orthonormal.
The spectral theory of the Bolza surface has been studied in the physics literature
as the quantum mechanical Hadamard-Gutzwiller model for quantum chaos [3,30,63].
20
Figure 1.8: Plotting the values of the functions in the ﬁrst eigenspace inR3
This is essentially billiards on a hyperbolic surface. The advantage of using a hyperbolic
surface over a Euclidean model is that Selberg’s trace formula is exact, as opposed to the
semiclassical approximations given by the Euclidean case. The Bolza surface is one of the
simplest surfaces on which to study this dynamical system, due to its high symmetry, low
genus, and the fact that much information is already known about it from the context
of algebraic geometry. It can be described as the quotient of the Poincaré disk by the so
called “octagon group” (see Section 2.2 for more details on quotient surfaces). This is the
Fuchsian group with four generators [63]
gk =
(
1 +√2 (2 + √2)αexp(ikπ
4
)
(2 +√2)αexp(−ikπ
4
) 1 +√2
)
,
where
α :=
√√
2− 1, k = 0,..., 3,
and the inverses are given by conjugation with
(
exp(iπ
2
) 0
0 exp (−iπ
2
)
)
.
They satisfy the relation
g0g−1
1 g2g−1
3 g−1
0 g1g−1
2 g3 =I2,
whereI2 is the2× 2 identity matrix. The quotient of the Poincaré disk by this group
tessellates the unit disk with regular octagons.
The two theorems we prove in Chapter 3 are to do with the multiplicities of low-lying
eigenvalues in the spectrum ofB. In particular
21
Theorem 1.27The dimension of the ﬁrst eigenspace of∆(B) is 3.
This result was stated by Jenni in [42] after being proved in his thesis [41]. Upon
careful inspection, a gap was found in this proof, relating to the analysis of 3 and 4
dimensional irreducible representations. In this work, we give a proof, utilizing the entire
automorphismgroupas opposedtoasmallersubgroup. Wegivetheassociatedirreducible
representation explicitly. The proof relies on a conjecture, for which numerical evidence
is given in Appendix C. We also suggest how this conjecture may be proved in future
work. We also prove
Theorem 1.28The dimension of the second eigenspace of∆(B) is 4.
Remark 1.29Both of these theorems are consistent with the numerical calculations of
eigenvalues listed in Table C.1. We observed in the numerics that there are 3 eigenvalues
roughly equal to 3.84 and 4 eigenvalues roughly equal to 5.35.
The Klein quartic
The Klein quartic, also called Klein’s curve, has the largest automorphism group of all
compact Riemann surfaces of genus 3. Klein studied the quotient of the hyperbolic plane
by Fuchsian groups, that is, discrete subgroups ofPSL2(R). He found the group
Γ(7) = PSL2(Z7)
to be of particular interest, and highlighted some of its special properties [48]. Since
then, it has been studied extensively both as a Riemann surface and as an algebraic
curve; the best introduction is the book “The Eightfold Way” [53], written to accompany
the installation of a statue of the surface at the MSRI, Berkeley. The book covers the
geometry of the surface, a number theoretical approach to the surface, and many topics
in algebra that highlight the extensive interest in the curve. So far, however, the spectral
theory of the surface remains relatively untouched; the large symmetry group suggests
that surface may maximizeλ1 among genus 3 compact Riemann surfaces.
We obtain the surface by associating sides2n + 1and 2n + 6 mod (14) ,n = 0,..., 6
in Figure 1.9. It is possible to tessellate this fundamental polygon with 336 triangles (see
Figure 4.2). This corresponds to the full isometry group of the surface,PGL2(Z7), which
has order 336. The group of orientation preserving isometries is half the size of this, that
is, 168. This means that the Klein quartic not only has the largest automorphism group
for genus 3, it is also optimal, by the following classical theorem.
22
Figure 1.9: The Klein quartic
1
2
3
45
6
7
8
9
10
11 12
13
14
Side associations:
1 – 6, 3 – 8, 5 – 10, 7 – 12, 9 – 14, 11 – 2, 13 – 4
Theorem 1.30 (Hurwitz’s automorphism theorem, [36])The number of automor-
phisms (not including reﬂections) of a compact Riemann surface of genusg >1 cannot
exceed84(g− 1).
We see that for genus 3, this bound is 168. The symmetry group of the Klein quartic
is therefore maximal. Any surface that achieves this bound is referred to as a Hurwitz
surface. A Hurwitz surface does not occur for every single genusg >1; the next Hur-
witz surface is the Macbeath surface of genus 7, which has 504 orientation preserving
isometries [55]. The group is isomorphic to the simple groupPSL2(Z8) [55] and is further
investigated in [83]. This surface is also known as Fricke’s surface, as Fricke investigated
the corresponding isometry group in [25]. The fundamental polygon is shown in [25],
along with the relevant side associations.
The Klein quartic, as its name suggests, can be obtained as the locus of a projective
quartic curve, namely
x3y +y3z +z3x = 0. (1.7)
The study of this equation accounts for much of the interest in Klein’s curve in number
theory. Stating the key results would involve introducing many terms that are irrelevant
to the rest of this work - the interested reader can ﬁnd a thorough exposition in [23]
instead.
The Fermat quartic is a similar surface that also comes from a projective equation; in
23
fact there is a whole class of Fermat surfaces that are obtained as the locus of
xk +yk +zk = 0, k ∈ N, k > 2.
For the genus 3 version, we setk = 4. The fundamental polygon for the Fermat quartic is
a 16-gon, shown in Figure D.2 along with the correct side identiﬁcations. Similar to the
Bolza surface, the Fermat quartic can be tessellated by(2, 3, 8)triangles; as it is a genus
3 surface, there are 192 of them. The Fermat quartic therefore has an automorphism
group of order 192. A presentation of the group of orientation preserving elements is
given in [52]. We can extend this by adding a (non-commutative)Z2 action to get the
following presentation of the whole group:
⟨a,b,c|a8 =b3 =c2 = (ab)2 = (a2b2)3 = (a4b2)3 =acac =bcbc =e⟩,
wheree is the identity element. In Remark D.1 of Appendix D we will comment further
on this group, and how it relates to numerical computations of the eigenvalues of the
Fermat quartic.
In Chapter 4, we introduce the notion of a pants decomposition and give the Fenchel-
Nielsen parameters of the Klein quartic. We show how to calculate a closed formula for
its systole, and that the multiplicity of the systole is 21 (this is not new information,
see [72]). We ﬁnally show that its ﬁrst eigenspace is either 6, 7, or 8 dimensional. Of
course, this is not a complete result as in the case of the Bolza surface, however it
uses the same mechanisms, and a proof along the same lines as that of Theorem 3.9 is
theoretically possible. Based on our ﬁndings in Table D.1, we can at least conjecture that
the multiplicity of the ﬁrst positive eigenvalue of the Klein quartic is 8.
24
Chapter 2
Background
2.1 Spectral theory
The Laplace-Beltrami operator∆, on a Riemannian manifoldM, is given in local coor-
dinates by the formula
∆ =−
n∑
i,k=1
1√g
∂
∂xi
√ggik ∂
∂xk
,
wheregik is the metric tensor,g its determinant, andgik are the components of the dual
metric on the cotangent bundle ofM.
There exists an orthonormal basis{φi|i∈ N0} inL2(M) consisting of eigenfunctions
∆φi =λiφi (2.1)
such that
0 =λ0<λ 1≤λ2≤... (2.2)
form an ascending sequence with∞ as the only accumulation point. We understand
Equation (2.1) in terms of the weak derivative.
The sequence in Equation (2.2) is called the spectrum of∆, and the individualλis are
referred to as eigenvalues. In this work,M will be either a compact Riemann surface,
or a subspace of a compact Riemann surface on which we consider a Neumann, Dirichlet
of mixed boundary problem. Recall the deﬁnition of these eigenvalue problems from
Chapter 1. In particular, note that we takeΩ to have compact closure and piecewise
smooth boundary. The property of compactness, along with the smoothness condition
where we consider a boundedΩ, ensure that the spectrum is discrete.
This result is entirely non-trivial; to see where it comes from, we will consider the
example of the Dirichlet Laplacian∆D on a domainΩ in a Riemann surface (recall
Deﬁnition 1.6). The approach we take is via sesquilinear forms, which will be deﬁned
shortly. The spectral theory of∆can also be explained through heat kernel asymptotics,
25
details of which are given in [13] and [28]. We start by introducing some classical theory
of unbounded operators, following [50] and [64]. Another good reference for the theory
of unbounded operators is [78].
LetH be a separable, complex Hilbert space. LetA be a linear operator inH. A
bounded linear operatorA can be deﬁned for allu∈H; it satisﬁes the inequality
‖Au‖≤ C‖u‖,
where the least possible value ofC deﬁnes the norm‖A‖. Conversely, diﬀerential oper-
ators, in particular∆, are unbounded and as a result do not have this property. They
are however deﬁned for someu∈H, so to properly deﬁne an unbounded operatorA, we
must also give its domainD(A)⊂H. Often we will write(A, D(A)). The graph of the
operator is used to deﬁneA as
gr(A) :={(u,Au)|u∈D(A)}⊂H×H ,
and comes with a norm (called the graph norm):
‖u‖A =‖u‖ +‖Au‖.
Deﬁnition 2.1 (Densely deﬁned operator)We say thatAis densely deﬁned ifD(A)
is dense inH.
Example 2.2∆Ω, that is, the Laplacian acting onΩ, is deﬁned onC∞
0 (Ω), and satisﬁes
Dirichlet boundary conditions trivially due to the property of compact support. Note that
it is also a non-negative operator since forφ∈C∞
0 (Ω), an integration by parts shows that
(φ, ∆φ) =‖∇φ‖2≥ 0.
C∞
0 (Ω) is dense inL2(Ω), so (∆Ω, C∞
0 (Ω)) is densely deﬁned onL2(Ω). Using Theo-
rem 2.13, we will create an extension ofPΩ
D = (∆Ω, C∞
0 (Ω))to deﬁne∆Ω
D onL2(Ω).
Being densely deﬁned is an essential property for deﬁning the adjoint of an unbounded
operator. For our unbounded, densely deﬁned operatorA, we want to construct an
extension ofA to a continuous operator on all ofH, that is, a linear operator˜A such
thatD(A)⊂D( ˜A) and for allu∈D(A), Au = ˜Au. In the case of bounded operators,
we have the bounded linear transformation (or so-called ‘BLT’) theorem that allows us
to do this (see, for example, [70] for details of this and other named but unacknowledged
theorems in this section). On the other hand, for unbounded operators
sup
0⁄=u∈D(A)
‖Au‖
‖u‖ =∞,
so a continuous extension is not possible. The problem then, is to create a natural
extensionofD(A)inawaythatallowsustoreplicate, oratleastapproximate, thespectral
theory of bounded operators. First, we need to introduce the concept of closability.
26
Deﬁnition 2.3 (Closed operator)A is called closed if for allu,v∈H and a sequence
{un}n∈N⊂D(A), the conditions
un→u and Aun→v
asn→∞ imply
u∈D(A) and Au =v.
In other wordsA is closed ifD(A) is a complete vector space with respect to the graph
norm.
Any bounded operator is closed by the closed graph theorem. Unbounded operators
are not necessarily closed, but we have a similar notion:A is called closable if it has a
closed extension, that is, if its graph remains the graph of an operator¯Awhen its closure
gr(A) is taken. Once again, question of domains makes deﬁning the adjoint harder for
unbounded operators; for bounded operators, it follows from the Riesz representation
theorem.
Deﬁnition 2.4 (Adjoint of an unbounded operator)LetAbe a densely deﬁned op-
erator inH. Its adjointA∗ is uniquely deﬁned as follows
D(A∗) :={u∈H|∃ u∗∈H s.t.∀v∈D(A), (u,Av) = (u∗,v )},
A∗u :=u∗
.
Proposition 2.5A∗ is always closed, regardless of whether or notA is.
To see this, we can look at an alternative deﬁnition of the adjoint, taking advantage
of the fact that we can describe an operator by its graph. ForA∗,
gr(A∗) =R(gr(A)⊥),
whereR acts like a rotation onH×H , namelyR(u1,u 2) = (u2,−u1).
Deﬁnition 2.6 (Symmetric operator)A is symmetric if it is densely deﬁned and its
adjointA∗ is an extension ofA.
An easy consequence of Proposition 2.5 is that ifA is symmetric, then it is closable.
The preceding deﬁnitions have laid the groundwork for us to deﬁne self-adjointness for
unbounded operators. These will be crucial for developing a functional calculus of oper-
atorsf(A),f : R→ C, whereby we will be able to use function analytic methods in our
spectral analysis of operators.
27
Deﬁnition 2.7 (Self-adjoint operator)A is self-adjoint if it is densely deﬁned,A∗ =
A andD(A) =D(A∗). A symmetric operatorA is essentially self-adjoint if its closure¯A
is self-adjoint.
We now consider sesquilinear forms. The aim is to establish a one to one corre-
spondence between these forms and self-adjoint operators; this will allow us to create
self-adjoint extensions of densely deﬁned, symmetric, non-negative operators.
Deﬁnition 2.8 (Sesquilinear form)A sesquilinear form inH is a map
q :D(q)×D(q)→ C,
whereD(q)⊂H, such that
(u,v)→q(u,v)
is linear in the second entry and semi-linear in the ﬁrst. The mapping
D(q)→ C
u↦→q[u] :=q(u,u)
is called the quadratic form associated toq. q is semi-bounded below if
q[u]≥α‖u‖2
for someα∈ R. q is called elliptic if
|q[u]|≥ c‖u‖2
for somec >0. Finally,q is closed if it is semi-bounded below andD(q) is a complete
Hilbert space with respect to the norm
‖u‖2
q =q(u,u) + (|α| + 1)‖u‖2.
Example 2.9For our study of the Dirichlet Laplacian, we will introduce a sesquilinear
formQΩ
D such that
D(QΩ
D) :=D(PΩ
D)
and forφ∈W1, 2
0 ,
QΩ
D[φ] := (φ, ∆φ) =‖∇φ‖2.
Deﬁnition 2.10 (Adjoint of a sesquilinear form)The adjointq∗ ofq is deﬁned as
D(q∗) :=D(q),
q∗(φ,ψ) :=q(ψ,φ).
q is symmetric ifq∗ =q.
28
Now letq be a symmetric, densely deﬁned sesquilinear form that is bounded from
below. As before,q is closable if it has a closed extension, that is, if for all{ψn}n∈N⊂
D(q),
D(q)∋ψn
n→∞
−−−→0
q[ψn−ψk]
n,k→∞
−−−−→0
implyq[ψn]
n→∞
−−−→0, thenq has closure¯q deﬁned as
D(¯q) :=
{
ψ∈H|∃{ ψn}⊂ D(q) s.t. ifψn
n→∞
−−−→ψ, q[ψn−ψk]
n,k→∞
−−−−→0
}
,
¯q[ψ] := lim
n→∞
q[ψn].
Example 2.11The formQΩ
D is not closed onC∞
0 , but note that the norm
‖φ‖2
QΩ
D
=QΩ
D[φ] + (|α| + 1)‖u‖2
is the norm on the Sobolev spaceW1, 2
0 (Ω)(compare Deﬁnition 1.18). The domain of the
closure ˜QΩ
D =QΩ
D is thereforeW1, 2
0 (Ω), and forφ∈W1, 2
0 (Ω),
˜QΩ
D[φ] =‖∇φ‖2,
where we interpret∇φ in a distributional sense.
From the sesquilinear formq, we wish to induce an operatorAq that is self-adjoint and
bounded from below. The correspondence is as follows. Suppose we haveAq as above.
Then
˙q[ψ] := (ψ,Aqψ), D ( ˙q) :=D(Aq)
is densely deﬁned, symmetric and bounded from below. It is closable, so we take the
closureq := ¯˙q as our desired form. On the other hand, suppose we haveq as above. Then
we will use the following to deﬁne the corresponding operator:
Theorem 2.12 (Representation theorem, [45])Letq be densely deﬁned, symmetric,
closed, and bounded from below inH. Then
D(Aq) :={ψ∈D(q)|∃η∈H s.t.∀φ∈D(q), q(φ,ψ) = (φ,η)},
Aqψ :=η
is self-adjoint and bounded from below.D(q) is called the form domain of the operator
Aq.
We now introduce a special construction that produces the self-adjoint operator with
the smallest form domain, that is, the domain ofq is contained in the form domain of any
29
other self-adjoint extension˜Aq ofAq. We will use this to deﬁne the Dirichlet Laplacian as
theself-adjointextensionofaminimaloperatorthathasthesmooth, compactlysupported
functions as its domain.
Theorem 2.13 (Friedrichs extension)LetA be a symmetric operator, bounded from
below. LetqA be the sesquilinear form such that
qA[ψ] := (ψ,Aψ),
and
D(qA) :=D(A)
is densely deﬁned, symmetric and bounded from below. IfqA is closable, we take the
closure
˜qA :=qA.
Finally, we can associate to˜qA the self-adjoint linear operatorA˜q via Theorem 2.12.
Example 2.14Using Theorem 2.12 and Theorem 2.13, we are now ready to deﬁne∆Ω
D
onL2(Ω)as a self-adjoint extension ofPΩ
D via the quadratic form˜QΩ
D. The deﬁnition in
the Representation Theorem gives us
D(∆Ω
D) ={ψ∈W1, 2
0 (Ω)|∃η∈L2(Ω)s.t.∀φ∈W1, 2
0 (Ω), (∇φ,∇ψ) = (φ, η)}, (2.3)
∆Ω
Dψ =η.
We may abbreviate this deﬁnition slightly, using the knowledge thatC∞
0 (Ω)is dense in
W1, 2
0 (Ω), and that the condition in 2.3 deﬁnes the distributional Laplacian, to state
D(∆Ω
D) ={ψ∈W1, 2
0 (Ω)| ∆ψ∈L2(Ω)},
∆Ω
Dψ = ∆ψ.
We deﬁne the spectrum of an unbounded operator via the inverse,(A−z)−1 of a
self-adjoint operator inH. It exists for all values ofz that are not eigenvalues ofA.
Deﬁnition 2.15 (Resolvent)The resolvent set ofA,
ρ(A) :={z∈ C| (z−A) :D(A)→H is bijective and(z−A)−1 is bounded}
is an open subset ofC. The resolvent operator
ρ(z) := (z−A)−1
depends analytically onz insideρ(A).
30
Example 2.16The resolvent operator for the Dirichlet Laplacian,ρ(−1) = (∆Ω
D + 1)−1
is a bounded map
ρ(−1) :L2(Ω)→W1, 2
0 (Ω).
Deﬁnition 2.17 (Spectrum)The spectrum ofA is the complement
σ(A) := C\ρ(A).
Remark 2.18We are interested in the discrete spectrumσdis, which is the set of isolated
eigenvalues of ﬁnite multiplicity, that is
σdis(A) ={λ∈ C|∃ψ∈D(A),‖ψ‖ = 1, Aψ=λψ}.
Ifλ∈σdis(A), then its multiplicity is given bydim(ker(A−λ))<∞.
Now that we have deﬁned the resolvent operator, we just need to show that it is
compact, and then we can apply the spectral theorem for compact, self-adjoint operators.
First, we deﬁne what it means to be a compact operator.
Deﬁnition 2.19 (Compact operator)A bounded operatorAis compact if for a bounded
sequence(un)n∈N, (Aun)n contains a converging sub-sequence.
There are alternative criteria for a bounded operator to be compact, for example, we
have
Proposition 2.20Let A be bounded operator on a Hilbert spaceH. Then the following
are equivalent [64]:
(i) A is compact;
(ii)A is the norm limit of a sequence of ﬁnite rank operators;
(iii) for any weakly convergent sequenceun⇀u,Aun→u strongly;
(iv) for any ﬁnite orthonormal system(en),Aen→ 0.
Theorem 2.21 (Rellich-Kondrachov embedding theorem)Let Ωbe a bounded do-
main of a compact Riemann surfaceS. The the embedding
W1, 2(Ω)⊂L2(Ω)
is compact.
Example 2.22We have seen thatρ(−1) is bounded fromL2(Ω) to W1,2
0 (Ω). By the
Rellich-Kondrachov embedding theorem,W1,2
0 (Ω) has a compact embedding intoL2(Ω),
since Ω is compact, as is the surfaceS for which it is a subset.
31
The following theorem guarantees that any complex number in the spectrum of a
compact operator is an eigenvalue.
Theorem 2.23 (Fredholm alternative)LetA be a compact operator. Forz0⁄= 0,
(i) either(z0−A)−1 exists and is a bijectionH→H ,
(ii) orz0 is an eigenvalue of ﬁnite multiplicity.
Therefore, the spectrum of the compact resolventρ(−1)consists ofσdis∪{0}, and its
eigenvalues have ﬁnite multiplicity. Moreover the only accumulation point of its spectrum
is zero.
The upshot of Theorem 2.23 is that we can “invert” the property of a compact resolvent
ρ(z) of A to get information about what we are really interested in - the spectrum of
A. In particular,A has a purely discrete spectrum that has∞ as its only accumulation
point. To see this, note that for the eigensystem(µn, un) ofρz,
(z0−A)−1un =µnun ⇐⇒ (1−z0µn)un =−µnAun.
Rearranging the right hand sides tells us that the eigenvalues ofA are
λn =z0µn− 1
µn
.
One can see that an accumulation of the resolventµn→ 0 will correspond to an accu-
mulation at inﬁnity for the spectrum ofA. Returning to∆Ω
D, we have seen that it has
a compact resolvent, and therefore a discrete spectrum. We ﬁnish the section by stating
the general spectral theorem for self adjoint operators.
Theorem 2.24If A is compact and self-adjoint, then it admits an orthonormal eigen-
basis (un, λn) withλn→ 0.
2.2 Hyperbolic geometry
WenowwanttolookattheLaplacianintwospeciﬁcmodelsofhyperbolicgeometry. First,
we will consider the Poincaré disk model. This is the setting through which we view the
Riemann surfaces. Next, we will consider the Laplacian in geodesic polar coordinates
on the Poincaré upper half plane,H. Harmonic analysis onH will give us a method to
calculate the eigenvalues of hyperbolic disks. As a result, we can then use the Faber-
Krahn inequality as a comparison tool for Dirichlet boundary problems on our surfaces.
32
2.2.1 The upper half plane
As a model for hyperbolic geometry, we consider the upper half plane
H ={z∈ C|ℑz >0},
with metric
ds2
H =y−2(dx2 +dy2).
The Laplacian with this metric takes the form
∆H =−y2
(∂2
∂x2 + ∂2
∂y2
)
.
The distance function is
ρ(z,w ) = log
(|z−w| +|z−w|
|z−w|−| z−w|
)
.
Geodesics inHare semicircles and half lines perpendicular to the real line. The isometries
of hyperbolic space are given by Möbius transformations
t :z↦→az +b
cz +d,
such thata, b, c, d∈ Randad−bc = 1. With these conditions, a Möbius transformation
t determines a matrix of the form (
a b
c d
)
,
up to a sign. Since the identity transformation can be given bya = d =±1 (and
b =c = 0), the group of orientation preserving isometriesIsom+(H) is
PSL2(R) = SL2(R)/(±1).
In this thesis, we will be working with the full group of isometriesIsom(H); this is given
by the Möbius transformations and the reﬂectionz↦→−z. The function
cosh(ρ(z,w )) = 1 + 2u(z,w ),
where
u(z,w ) =|z−w|2
4ℑzℑw,
deﬁnes a point pair invariant, that is, fort∈ Isom(H),
cosh (ρ(tz,tw)) = cosh(ρ(z,w )).
Any element inIsom+(H), not equal to the identity, is conjugate to a unique matrix of
one of the following forms:
(
γ 0
0 1
)
,
(
cos(θ) −sin(θ)
sin(θ) cos( θ)
)
, or
(
1 1
1 0
)
,
33
whereγ >1 and 0<θ ≤ π
2. These three cases respectively describe hyperbolic, elliptic,
and parabolic transformations.
Where we have an orientation reversing isometryt∈ Isom−(H) = Isom(H)\Isom+(H),
t :z↦→az +b
cz +d,
such thatad−bc =−1,t will be conjugate to a matrix of the form
(
γ 0
0 1
)
or
(
−1 0
0 1
)
,
whereγ <−1. The ﬁrst case describes a glide reﬂection, and the second, a reﬂection.
Deﬁnition 2.25 (Fuchsian group)A subgroupΓ⊂ PSL2(R) is called Fuchsian if it
acts onH discontinuously. A Fuchsian groupΓ is said to be of the ﬁrst kind if its limit
set, that is, the limit points of orbits ofΓ is∂H
Deﬁnition 2.26 (Fundamental domain)A setF⊂ H is a fundamental domain for
Γ ifF is a closed domain inH, and the translations ofF under Γ tessellate H.
Every ﬁnite area hyperbolic surfaceS can be represented as the quotient of theH by
the action of a Fuchsian groupΓ of the ﬁrst kind, that is
S∼= Γ\ H.
If Γ contains only hyperbolic elements, then the surface will be smooth and compact,
with genusg≥ 2. This neat isomorphism comes from the uniformization theorem, which
we state in two parts (see, for example, [24]).
Theorem 2.27 (Koebe, Poincaré)For any smooth Riemannian metric on a surface,
there exists a conformally equivalent metric of constant curvature.
We can use a global rescaling to restrict ourselves to curvatures of+1, 0, and−1.
Then we have the following
Theorem 2.28 (Hopf)Up to isometry, the only smooth, complete, simply connected
surfaces of constant curvature areS2, R2, andH2.
The complex analogue of this is that every simply connected Riemann surface is holo-
morphically equivalent toC∪∞, C or H.
Since Fuchsian groups act discontinuously, a fundamental domainF will share a border
with a ﬁnite number of translates of itself in the associated tessellation. IfΓis a Fuchsian
group of the ﬁrst kind, its fundamental domain can be chosen to be a convex polygon
given by
D(w) ={z∈ H|ρ(z,w )<ρ (z,γw )∀γ∈ Γ, γ⁄=I},
34
forw∈ H not ﬁxed by such aγ, whereI is the identity action. This object is referred
to as the Dirichlet polygon. Side associations can be given onD(w) such that the group
actions that “glue” a side to its pair, also generateΓ.
2.2.2 The Poincaré disk
ThePoincarédiskisaconformalmodelofhyperbolicgeometry; thepropertyofpreserving
Euclidean angles, and radial symmetry, means that it is a convenient model in which to
view symmetric hyperbolic surfaces. It is the open unit disk in the complex plane
D ={z∈ C||z|< 1},
with Riemannian measure
ds2 = 4dzdz
(1−|z|2)2.
Since the metric is radially symmetric about the origin, it means that the regular polygons
we will consider actually ‘look’ regular, as opposed to the upper half plane model, where
they are skewed towards the real line. This makes it much easier to see, for example, the
rotational symmetry of the surfaces.
Geodesics in this model are diameters of the unit circle, and circles meeting the bound-
ary of the disk perpendicularly. All the lines in the tessellations shown in Chapter 3 and
Chapter 4 are made up of geodesics.
Figure 2.1: Geodesics in the Poincare disk
2.2.3 Triangle groups
The fundamental polygons for the surfaces we consider in this paper can be tessellated
by hyperbolic triangles: for the Bolza surface, the fundamental octagon is tessellated
35
with 96 triangles having angles(π
2, π
3, π
8); the 14-gon of the Klein quartic contains 336
triangles with angles(π
2, π
3, π
7); and the surface M3 [72] has 96(π
2, π
3, π
12) triangles.
Deﬁnition 2.29 (Triangle group)A triangle group is a subgroupΓ⊂ PSL2(R) gen-
erated by reﬂections in the sides of an(l, m, n) triangle (a triangle with anglesπ
l, π
m and
π
n, where1
l + 1
m + 1
n < 1 andl, m, n∈ N). For an(l, m, n) triangle with side reﬂections
given byx, y, z, the corresponding triangle groupT(l, m, n) has the presentation
T(l, m, n) =⟨x, y, z|x2 =y2 =z2 = (xy)l = (yz)m = (zx)n =e⟩.
Figure 2.2: Generators of an(l, m, n) triangle group
π
l
π
m
π
n
x
y
z
The area of a right angled hyperbolic triangle is
π
2−α−β,
whereα and β are the sizes of the other two angles. This formula is known as the
Gauss defect, and comes from the more general Gauss-Bonnet theorem. Hence a(2, 3, 7)
triangle has areaπ
42, a(2, 3, 8) triangle has areaπ
24 and a(2, 3, 12)triangle has areaπ
12.
We can use the following formulae from [13] to calculate the hyperbolic lengths of the
sides, based on the fact that we know all the angles.
Theorem 2.30For any right angled hyperbolic triangle, the following hold:
cosh(c) = cot(α) cot(β),
cos(α) = cosh(a) sin(β),
wherec is the hypotenuse,a is the side with opposite angleα, andb is the side with
opposite angleβ.
The hyperbolic side lengths for the(2, 3, 7) triangle are:
a = arccosh
(
csc(π
7
)
2
)
≈ 0.545,
b = arccosh
(
2 cos(π
7
)
√3
)
≈ 0.283,
36
c = arccosh
(
cot(π
7
)
√3
)
≈ 0.621.
For the(2, 3, 8) triangle, they are:
L = arccosh
(
csc(π
8
)
2
)
≈ 0.7642,
M = arccosh
(
2 cos(π
8
)
√3
)
≈ 0.3635,
N = arccosh
(
cot(π
8
)
√3
)
≈ 0.8607.
We will not need the side lengths for a(2, 3, 12)triangle in this report, but clearly they
will take a similar form.
The isometries of the surfaces come from the movements of a triangle around the
tessellation by reﬂections in one or more of its sides. The relations between these reﬂec-
tions form the triangle group, and where the polygons have side associations, additional
relations will arise in the presentation of the group.
2.3 Harmonic analysis on H
2.3.1 Disks
Here we take “disk” to mean a general disk in hyperbolic space rather than the Poincaré
disk model. Due to the radial symmetry of the disk, it is possible to give an explicit
formula for the eigenfunctions. From these, we can calculate the eigenvalues of the disk
and use them to bound the eigenvalues of a domain in our surface from below. First,
we introduce a more convenient polar co-ordinate system, known as the geodesic polar
co-ordinates. Recall the diﬀerent forms that a group action inIsom+(H) can take (for
example, reﬂection or rotation matrices). An elementg∈ Isom+(H) can be written as
g =k(ϕ)a(e−r)k(θ), where
k(ϕ) =
(
cos(ϕ) sin( ϕ)
−sin(ϕ) cos( ϕ)
)
, 0≤ϕ<π,
a(e−r) =
(
e−r/2 0
0 er/2
)
, r ≥ 0,
and k(θ) is a rotation by angle2θ aroundi. This way of expressingg is known as
Cartan’s decomposition [38]. Given a pointz∈ Csuch thatz =x+yi, in geodesic polar
co-ordinates,z =k(ϕ)e−ri and we use the following to deﬁne the change of co-ordinates:
y = (cosh(r) + sinh(r) cos(2ϕ))−1,
37
x =y sinh(r) sin(2ϕ).
The Riemannian measure and length element in terms of(r, ϕ) are now
ds2 =dr2 + (2 sinh(r))2dϕ2,
dz = (2 sinhr)drdϕ.
These give us formulae for the area of a diskD:
Area(D) = 4π sinh2
(r
2
)
,
and circumference of its boundary
l(∂D) = 2π sinh(r),
where we normalize the disk to be centred ati and taker as above to be its radius. The
Laplacian takes the form
∆ =−
(∂2
∂r2 + 1
tanhr
∂
∂r + 1
(2 sinhr)2
∂2
∂ϕ2
)
,
and eigenfunctions are Legendre p functions
P−s(cosh(r)) = 2F1
(
s, 1−s; 1; 1− cosh(r)
2
)
,
where
2F1(a, b;c;z) =
∞∑
k=0
(a)k(b)k
(c)kk! zk, (s)k =s··· (s +k− 1)
is the hypergeometric function andλ =s(1−s) are the eigenvalues. The full derivation
of these eigenfunctions is given in [38].
2.3.2 Cylinders
Not all domains in hyperbolic surfaces satisfy the isoperimetric inequality. It may still
be desirable to investigate the eigenvalues of such regions; we will see a particular case
of this when we look at the Bolza surface in Section 3.4. One region that does not,
in general, satisfy the isoperimetric inequality is the hyperbolic cylinder. We take the
deﬁnition from [57].
Deﬁnition 2.31 (Hyperbolic Cylinder)A hyperbolic cylinderC, with core geodesicγ
of lengthl, is the quotient ofH by a hyperbolic isometry
τ =
(
el/2 0
0 e−l/2
)
, l> 0.
The core geodesic is the image of the axis ofτ under the quotient mapH/⟨τ⟩.
38
C
Cw
θ
ρ
γ
Figure 2.3: CollarCw contained in hyperbolic cylinderC
We use Fermi coordinates to describe a pointp∈C . Denote byl the length ofγ,
parametrized with constant speed.ρ is the signed distance ofp fromγ and θ is the
projection ofp ontoγ. For example, in Figure 2.3, the Fermi coordinates of the point on
the boundary ofCw at the end of the arrow are(ρ, θ).
Deﬁnition 2.32 (Collar)The collarCw, forw≥l is
Cw ={(ρ, θ)∈C| l cosh(ρ)<w, 0≤θ≤ 2π}.
Remark 2.33Note thatCw is diﬀeomorphic to a annulusΩ of constant widthρ, with
two boundary components of lengthw. In particular, for such an annulus, we have the
following formulae for its area and the length of its boundary:
A(Ω) =2l sinh(ρ),
l(∂Ω) =2l cosh(ρ),
where again,l is the length of the core geodesic, andρ is the constant distance from the
core geodesic to the boundary.
With respect to the Fermi coordinates,C has the metric
ds2 =dρ2 +l2 cosh2ρ
4π2 dθ2.
The Laplacian onC is given by
∆ =−
(d2
dρ2 + tanhρd
dρ + 4π2
l2 cosh2(ρ)
d2
dθ2
)
.
39
There is a fundamental system of even and odd eigenfunctions; these are given and
analyzed in [11]. With respect to the core geodesicγ, the even function is
φeven
k (s;ρ) = (cosh(ρ))
2πik
l 2F1
(s
2 +πik
l , 1−s
2 +πik
l ; 1
2;−sinh2(ρ)
)
and the odd function is
φodd
k (s;ρ) = sinh(ρ)(cosh(ρ))
2πik
l 2F1
(1 +s
2 +πik
l , 2−s
2 +πik
l ; 3
2;−sinh2(ρ)
)
where, once again, the corresponding eigenvalues areλ =s(1−s).
Although annuli in hyperbolic cylinders do not satisfy the isoperimetric inequality
in Deﬁnition 1.13, Mondal proved that hyperbolic cylinders satisfy a similar geometric
isoperimetric inequality. First we need the notion of symmetrization:
Deﬁnition 2.34 (Symmetrization)Let Ω be an essential annulus with core geodesic
γ. The symmetrization ofΩ is the annulusΩ0 of constant width that is symmetric with
respect to the core geodesicγ and has the same area asΩ.
Then we have the following:
Lemma 2.35[57, Lemma 2.2.3] LetΩ be an essential annulus with piecewise smooth
boundary andΩ0 be the symmetrisation ofΩ. Thenl(∂Ω)≥l(∂Ω0).
Proof: The proof is a partial reproduction of that in [57]. LetΩbe an essential annulus
in a cylinderC with core geodesicγ of lengthk, andΩ0 its symmetrisation. Lemma 2.35
is proved in two parts; ﬁrst, when∂Ω is graph overγ, and the more general case when
∂Ω is arbitrary. The two parts of the proof are similar, so here we just reproduce the
ﬁrst part.
Since∂Ωis a graph overγ, we can take two piecewise functionsr1 andr2 to mapγ to
the boundary in the positive and negative directions respectively (recall that the distance
in Fermi coordinates is signed). Formally, fori∈{ 1, 2},
ri : [0, k]→ R, r i(0) =ri(k),
and∂Ω is parametrised in Fermi coordinates as
{(t,ri(t))|t∈ [0,k ]}.
Without loss of generality, we can assumer1(t)>r 2(t) fort∈ [0, k]. We integrate with
respect to the hyperbolic cylinder metric (see Section 2.3.2) to calculate
A(Ω) =
∫ k
0
∫ r2(t)
r1(t)
cosh (r)drdt =
∫ k
0
(sinh (r2(t))− sinh (r1(t)))dt
40
and
l(∂Ω) =
∫ k
0
(r′
1(t) + 1)
1
2 cosh (r1(t))dt +
∫ k
0
(r′
2(t) + 1)
1
2 cosh (r2(t))dt.
Note that
l(∂Ω)≥
∫ k
0
(cosh (r1(t)) + cosh (r2(t)))dt,
andletLdenotetheexpressionontherighthandsideofthisinequality. Forthesymmetri-
sationΩ0, the functions from the core geodesic to the boundary are constant, for example
equal to±ρ, whereρ = sinh−1
(
A(Ω)
2k
)
. Taking such aρensures thatA(Ω) =A(Ω0). Here,
recall the simpler formulae
l(∂Ω0) = 2|k| cosh(ρ)
and
A(Ω0) = 2|k| sinh(ρ).
To prove the lemma, we show that
l(∂Ω)2−A(Ω)2≥l(∂Ω0)2−A(Ω0)2.
The result follows from the equality of the surface areas. First, note that
l(∂Ω)2−A(Ω)2≥ (L +A(Ω))(L−A(Ω)).
Let us consider the two factors on the right hand side of this inequality:
L +A(Ω) =
∫ k
0
((cosh (r2(t)) + sinh (r2(t))) + (cosh(r1(t))− sinh (r1(t))))dt
=
∫ k
0
(exp(r2(t)) + exp(−r1(t)))dt
and
L−A(Ω) =
∫ k
0
(exp(−r2(t)) + exp(r1(t)))dt.
By Hölder’s inequality,
(L +A(Ω))(L−A(Ω))≥
(∫ k
0
(
(exp(r2(t)) + exp(−r1(t)))
1
2(exp(−r2(t)) + exp(r1(t)))
1
2
)
dt
)2
=
(∫ k
0
(2 + 2 cosh (r1(t) +r2(t)))
1
2dt
)2
≥ 4k2,
since cosh(t)≥ 1. On the other hand,4k2 is precisely the value of
l(∂Ω0)2−A(Ω0)2.
Therefore, Lemma 2.35 is proved forΩ with ‘nice’ boundary. □
41
2.4 Representation theory
Deﬁnition 2.36 (Representation)Let V be ann-dimensional vector space overC.
Then GL(V ) denotes the the group of isomorphismsV →V. If V has a ﬁnite basis of
vectors{e1,..., en}, then each linear mapa :V→V is deﬁned by ann×n matrix (aij)
such that
a(ej) =
n∑
i=j
aijei.
A representation of a ﬁnite groupG is a group homomorphism
ρ :G→ GL(V ).
For eachg,h∈G, we have a mapρ(g) :V→V such that
(i) ρ(gh) =ρ(g)ρ(h),
(ii)ρ(1) = 1,
(iii)ρ(g−1) =ρ(g)−1.
Denote bydim(V ) the dimension of the representation. A sub-representation ofρ is
a sub-vector spaceW⊆V such thatρ(g)w∈W for allw∈W andg∈G. A subspace
with this property is calledG-invariant (or just invariant).
Deﬁnition 2.37 (Irreducible representation)Letρ : G→ GL(V ) be a representa-
tion. We say thatρ is irreducible ifV⁄= 0and if no subspace ofV isG-invariant, except
{0} andV, that is, only “trivial” subspaces areG-invariant.
Deﬁnition 2.38 (Unitary representation)WhereV is a complex Hilbert space, a
representationρ of G is unitary ifρ(g) = Ug is a unitary operator for everyg∈ G,
that is,Ug is surjective and preserves the inner product onV. We have
U∗
gUg =UgU∗
g =I,
that is,Ug is the inverse of its adjoint.
Deﬁnition 2.39 (Character)The character of a representationρ of a groupG, as
above, is a functionχρ : G→F, whereF is the ﬁeld over which the vector spaceV is
deﬁned. Forg∈G, it is given by
χρ(g) = Tr(ρ(g)).
Remark 2.40We will not always include a subscript when talking about characters; it
will depend on the context. Characters take a constant value on each conjugacy class.
They will be used in the next section, where we introduce a general version of Selberg’s
trace formula that uses a character to restrict to a particular irreducible representation.
42
In Chapter 3 and Chapter 4, we look at the irreducible representations of the isometry
groups of speciﬁc surfaces. We use these to investigate the orthonormal basis of eigen-
functions ofL2(Γ\ H); our ﬁrst step towards achieving this is the Peter-Weyl theorem.
Theorem 2.41 (Peter-Weyl Theorem, taken from [49])LetHbe the Hilbert space
of square integrable functions overG, that isL2(G). Letρ be a unitary representation of
G that acts onH as
ρ(h)f(g) =f(h−1g).
ThenL2(G)decomposes as an orthogonal direct sum of unitary irreducible representations
ofG, where the multiplicity of a representation is equal to its degree. We have
L2(G) =
⨁
ρ
E⊕dim(Eρ)
ρ ,
where the sum runs over the total spacesEρ of the representationsρ.
Next, we have the following property of the Laplacian:
Lemma 2.42The Laplace operator commutes with the group of isometries of the surface
(see, for example, [14]).
For a isometryφ :S→S of a compact Riemann surfaceS, and an eigenfunction of
the Laplacianf :S→ R with eigenvalueλ, this means
∆(f◦φ) = (∆f)◦φ = (λf)◦φ =λ(f◦φ).
Consider the eigenspaces of the Laplacian
Ei =Ei(S) ={φi∈L2(S)| ∆φi =λiφi}.
We can use the Peter-Weyl theorem along with the invariance of the Laplacian under
isometries to decompose the eigenspaceEi as a direct sum of eigenspaces of irreducible
representations (these can appear more than once). Huber showed that for every irre-
ducible representation, there are inﬁnitely many eigenspaces in which this representation
is involved [35].
2.5 Selberg’s trace formula
We start by following the basic presentation of the trace formula given in [10,38,56].
Recall that a hyperbolic surfaceS can be represented as a quotient of the hyperbolic
plane by a Fuchsian group that only has hyperbolic elements (with the exception of the
43
identity), that is,S∼= Γ\ H. The space of square integrable functions onS comes from
the functionsf∈L2(H) that are invariant under the action of an isometry
Tγ(z)f =f(γ−1z) =f(z), γ ∈ Γ,
and are square integrable over any fundamental domainFΓ of Γ (recall Deﬁnition 2.26).
We obtain the Hilbert spaceL2(Γ\ H) by deﬁning the obvious inner product
⟨f1, f2⟩ =
∫
FΓ
f1f2dµ
on these functions, wheredµis the Riemannian measure. In a similar way, we can identify
functions inC∞(Γ\ H) with the functions inC∞(H) that are invariant under the action
ofTγ, γ∈ Γ. We have seen that the Laplacian commutes with isometries; as a result it
commutes withTγ and thus mapsC∞(H)→C∞(H).
Deﬁnition 2.43 (Point pair invariant)A point pair invariant for a Fuchsian group
Γ is a functionk : H× H→ C that satisﬁes the following relations:
1. k(γz, γw) =k(z, w) for allγ∈ Γ,z, w∈ H;
2. k(z, w) =k(w, z) for allz, w∈ H.
Such a functionk(z, w) depends on the hyperbolic distanced(z, w) =u between the
two points. In this way, we can viewk as a function of one non-negative variablek(u).
If we takek(z, w) to be the kernel of an integral operator
(Lf)(z) =
∫
H
k(z, w)f(w)dµ,
thenL is invariant under the action ofIsom(H). Both the Laplacian andL are invariant
under isometries, and in particular, we have the following theorem (see [38, Theorem
1.9]):
Theorem 2.44The invariant integral operators commute with the Laplace operator.
This commutative property gives a relation between eigenfunctions of the Laplacian
and those of the invariant integral operators; in particular, iff is a solution to
(∆f−λf) = 0,
whereλ = 1
2 +t2, then it is also a solution to
Lf =h(t)f,
whereh(t) can be computed fromk(z, w) using the Selberg/Harish-Chandra transform
[38]:
q(v) =
∫ ∞
v
k(u)(u−v)−1
2du,
44
g(r) =2q
((
sinh
(r
2
))2)
,
h(t) =
∫ ∞
−∞
eirtg(r)dr.
To study the spectrum of the Laplacian onΓ\ H, note that the point pair invariant
on H× H induces a point pair invariant onΓ\ H× Γ\ H with
kΓ(z, w) =
∑
γ∈Γ
(γz, w).
This allows us to deﬁne an invariant integral operator
(Kf)(z) =
∫
Γ\H
kΓ(z, w)f(w)dµ
on functionsf∈C∞(Γ\ H). If such anf is an eigenfunction of the Laplacian, then it
again satisﬁes
Kf =h(t)f,
since ∫
FΓ
kΓ(z, w)f(w)dµ =
∫
H
k(z, w)f(w)dµ,
whereFΓ is a fundamental domain forΓ\ H.
Remark 2.45In this presentation, we have given little attention to the convergence of
the various series and integrals considered - the ﬁner details can be found in [56]. The
relation between eigenfunctions of the Laplacian and of the invariant integral operators
depends onkbeing smooth, and of compact support, onH(or Γ\H). It is more common to
specify conditions on the spectral functionh(t), since this function, along with its Fourier
transform, appear in Selberg’s trace formula below. In particular, we require the following
conditions:
(i) h is analytic on|ℑ(t)|≤ σ for someσ >1
2;
(ii)h(t) =h(−t);
(iii)|h(t)|≪ (1 +ℜ(t))−2−δ for ﬁxedδ >0, uniformly∀t in|ℑ(t)|≤ σ.
Let{ϕ0, ϕ1,...}∈ C∞(Γ\ H) be eigenfunctions of∆, and recall that these form an
orthonormal basis ofL2(Γ\ H). In particular, forf∈C2(Γ\ H), we have the spectral
decomposition
f(z) =
∑
j
⟨f, ϕj⟩ϕj(z).
Now forh(t) satisfying the conditions in Remark 2.45, we have the eigenvalue equation
Kϕj =h(tj)ϕj,
45
and the decomposition of our point pair invariant (see [56, Proposition 9])
kΓ(z, w) =
∞∑
j=0
h(tj)ϕj(z)ϕj(w).
Deﬁnition 2.46 (Trace class)LetFΓ be a fundamental domain forΓ\ H as above.
The integral operator withK withkΓ(z, w) as its kernel are of trace class ifkΓ(z, w) is
absolutely integrable forz =w. The trace ofK is
TrK =
∫
FΓ
kΓ(z,z )dµ.
Selberg’s trace formula allows us to computeTrK in two diﬀerent ways; one using the
spectral decomposition ofkΓ, and the other using the geometry ofΓ. First, we integrate
over the spectral decomposition ofkΓ, that is
kΓ(z, z) =
∑
j
h(tj)|ϕj(z)|2,
to get
TrK =
∑
j
h(tj),
since theϕj are orthonormal. This gives us the spectral side of the formula. Now recall
kΓ(z, z) =
∑
γ∈Γ
k(γz, z).
Taking the trace ofK, we get
TrK =
∑
γ∈Γ
∫
FΓ
kΓ(γz, z)dµ.
Let [γ] denote the conjugacy class of an element ofΓ, that is
[γ] ={˜γ∈ Γ| ˜γ =τγτ−1 for someτ∈ Γ}.
We deﬁne the partial kernel over a conjugacy class to be
k[γ](z, z) =
∑
γ∈[γ]
k(γz, z).
Note that
kΓ(z, z) =
∑
[γ]
k[γ](z, z) and TrK =
∑
[γ]
TrK[γ],
whereK[γ] is the integral operator that has kernelk[γ]. The centralizer ofγ is
Zγ ={τ∈ Γ|τγ =γτ}.
46
Two elementsτ, τ′∈ Γ give the same conjugate ofγ if and only ifτ′τ−1 belongs to
the centralizer ofγ. The upshot is that the fundamental domain of the centralizer of a
hyperbolic element is in general much simpler than that of the fundamental domainFΓ
(and therefore the integrals over such a domain are much simpler). Such a fundamental
domain is shown in Figure 2.4.
i
Figure 2.4: Fundamental domain for the centralizer of a hyperbolic element
Forγ∈ [γ]
TrK[γ] =
∑
τ∈Zγ\Γ
∫
FΓ
k(τ−1γτz, z)dµ
=
∫
Zγ\H
k(γz, z)dµ.
This depends only on[γ], that is, ifγ′ =g−1γg,g∈ SL2(R), then
TrK[γ] =
∫
g−1Z(γ)g\H
k(g−1γgz, z)dµ = TrK[γ′].
The integral depends only on the distanced(z,γz ), and can be explicitly computed
(see [38, Sections 10.4 and 10.5]). The most common version of the trace formula is for
compact Riemann surfaces, where there are only hyperbolic conjugacy classes (and the
identity motion). There is an exact correspondence between hyperbolic conjugacy classes
and the lengths of primitive geodesics (multiple loops are not included), so this is the
most interesting version for seeing the relation between the energy and length spectra.
Theorem 2.47 (Selberg’s trace formula, [74])Leth(t) be as above, and letg(t) be
its Fourier transform. LetS be a compact Riemann surface. Then
∞∑
j=0
h(tj) = Area(S)
4π
∫ ∞
−∞
h(t) tanh(πt)tdt +
∑
[γ]
∞∑
n=1
lγg(nlγ)
2 sinh(nlγ/2).
47
One interesting application of this theorem is to prove Weyl’s law, the famous formula
that describes the asymptotic properties of Laplace eigenvalues. We deﬁne the set of
eigenvalues below a certain value as
N(λ) = #j{λj≤λ}.
Theorem 2.48 (Weyl’s law, [82])LetS be a compact Riemann surface. Then
N(λ)∼ Area(S)
4π λ, λ→∞.
This can be proved by using the heat kernel
h(t) =e−βt2
with Fourier transform
g(s) =e−s2/2β
√4πβ
in Selberg’s trace formula, whereβ >0. In particular, withλj =t2
j + 1
4, we take the limit
lim
β→0
∞∑
j=0
e−βλj,
and the result follows from a Tauberian theorem of Wiener-Ikehara (see Theorem 9.4.7
in [13]).
If one has information about the irreducible representations of the automorphism
group of a surface, one can consider a more general version of Selberg’s trace formula,
given in [9]. The advantage of this is that one can restrict the formula to a single unitary
characterχ on Γ, that is, consider the spaceL2(Γ\ H,χ) rather than simplyL2(Γ\ H).
L2(Γ\ H,χ) is the Hilbert space of functionsf : H→ C such that
f(Tz)≡χ(T)f(z)
for allT∈ Γ andf∈L2(Γ\ H).
Theorem 2.49 ( [9])LetM be the setT∈ Γsuch thatT does not have a cusp of[Γ+]as
a ﬁxed point. LetI denote the identity action, andMI =M∪[I]. LetF be a fundamental
domain forΓ\ H. For each non-ellipticT∈M, there exists a hyperbolic element or glide
reﬂectionT0∈Z(T) such that the inﬁnite cyclic group
[T0] ={Tn
0|n∈ Z}
48
has index 1, 2, or 4 inZ(T). Then for each admissibleh(t) we have
∑
T∈MI
∫
Γ\H
χ(T)k(z,Tz )dµz = Area(F)
4π
∫ ∞
−∞
h(t) tanh(πt)tdt
+
∑
T∈M
non−ell
logN(T0)
[ZΓ(T) : [T0]]
χ(T)g(logN(T))
N(T)
1
2− sgn(detT)N(T)−1
2
+
∑
T∈M
elliptic
χ(T)
2|ZΓ(T)| sin(θ(T))
∫ ∞
−∞
exp(−2θ(T)t)
1 + exp(−2πt)h(t)dt,
where the[T]sums are taken over distinct conjugacy classes ofΓ, and the non-elliptic sum
consists of conjugacy classes whereT is a reﬂection, hyperbolic transformation or glide
reﬂection (see Section 2.2 on hyperbolic geometry; also forθ). The sums and integrals are
all convergent with good majorants. The elliptic sum is ﬁnite. Note thesgn function in
the non-elliptic sum, which distinguishes between orientation preserving and orientation
reversing isometries.
This theorem is interesting in that it includes orientation reversing isometries. The
disadvantage is that it only applies to unitary characters. For characters of higher di-
mensional irreducible representations, Theorem 4.1 in Chapter 8 of [33] provides a similar
formula, although this does not deal with reﬂections. One might conjecture that it is pos-
sible to combine the two formulae to get a more general version of Selberg’s trace formula
for characters of higher dimensional representations of an automorphism group that in-
cludes reﬂections.
49
Chapter 3
The Bolza Surface
3.1 Symmetry group of the Bolza surface
In his thesis, Jenni [41] lists the generators of the group of isometries, and the relations
between them. The whole isometry group is generated by 4 actions, which are shown in
Figure 3.1:
• R - rotation of order 8 around the origin (centre of the Bolza surface) that maps
Qi↦→Qi+1 (modulo 8), and preservesP1 andP2;
• S - reﬂection in the real line that mapsQi↦→Q9−i, and preservesP1 andP2;
• T - reﬂection that switches the centre point with the outmost, that is, mapsP1↦→P2
and preserves theQis;
• U - rotation of order 3 around the centre of a(4, 4, 4)triangle, 16 of which tessellate
the surface. This is the only action which permutes theP andQpoints; for example,
it mapsP1↦→Q8,Q8↦→Q1, andQ1↦→P1.
Remark 3.1Each element of the group of isometries can be written uniquely in the
canonical form
RiSjTkUl, i ∈{ 0,..., 7}, j, k∈{ 0, 1}, l ∈{ 0, 1, 2}.
An easy computation conﬁrms that there will be8· 2· 2· 3 = 96elements [41].
Remark 3.2R and U are orientation preserving actions, whereasS and T are ori-
entation reversing. Therefore the orientation preserving elements ofIsom(B), denoted
Isom+(B), will have the formRi(ST)jUl. The orientation reversing elements will take
the form eitherRiSUl orRiTUl.
50
Figure 3.1: Symmetries of the Bolza surface
P2
P2
P2
P2
P2
P2
P2
P2
Q7Q6
Q2
P1
Q3
Q8
Q1
Q5
Q4
Calculations in GAP [26] show that the relations given in Satz32 of Jenni’s thesis give
a ﬁnitely presented group of order 12. This implies that there is a problem with at least
one of his relations. After scrutinizing the actions ofR,S,T, andU on the tessellation
regular octagons, we oﬀer the following corrected theorem:
Theorem 3.3 (Correction to Satz 32 in [41])The generators of the Bolza surface
satisfy the following relations:
R8 =S2 =T2 =U3 =RSRS =STST =RTR3T =e,
UR =R7U2, U2R =STU, US =SU2, UT =RSU,
wheree is the trivial (identity) action.
Remark 3.4UR =R7U2 replaces the erroneousUR =RU2.
We check that these relations are satisﬁed by considering the actions ofR,S,T, and
U on the 16 equilateral triangles shown in Figure 3.2, where the verticesPi, i∈{ 1, 2},
andQj,j∈{ 1,..., 4}, represent the Weierstrass points of the surface; the bar notation
denotes that a point is in the other sheet of the cover (compare Figure 1.7).
We tabulate this information in Table 3.1, and from this point it is straightforward to
verify that the relations hold by “chasing” the triangle around the table. For example, if
we want to know whereRS sendsP1Q1Q2, we observe
RS(P1Q1Q2) =R(S(P1Q1Q2))
51
Figure 3.2: The Bolza surface tessellated by 16 equilateral triangles
P2
P2
P2
P2
P2
P2
P2
P2
Q3Q2
Q2
P1
Q3
Q4
Q1
Q1
Q4
=R(P1Q3Q4)
=P1Q4Q1.
Table 3.2 records the orbits of the triangles under the action of the generators.
Proposition 3.5The centre of the isometry group isR4.
Proof: To prove this, we ﬁrst have to show thatR4 commutes with the three other
isometries. We start withS. UsingRS =SR7,
R4S =R3SR7
=SR5R7
=SR12
=SR4.
ForT, we will useR3T =TR7; this comes from multiplying both sides ofRTR3T =e
byTR7. UsingRTR3 =T andRT =TR5,
R4T =R3TR5
=TR7R5
=TR4.
And forU, we useUR =R7U2,RUR =U2, andRU =U2R7,
52
Table 3.1: Actions of isometries on equilateral triangles
Triangle R S T U
P1Q4Q1 P1Q1Q2 P1Q4Q1 P2Q4Q1 P1Q4Q1
P1Q1Q2 P1Q2Q3 P1Q3Q4 P2Q1Q2 P1Q3Q4
P1Q2Q3 P1Q3Q4 P1Q2Q3 P2Q2Q3 P2Q3Q4
P1Q3Q4 P1Q4Q1 P1Q1Q2 P2Q3Q4 P2Q4Q1
P1Q4Q1 P1Q1Q2 P1Q4Q1 P2Q4Q1 P1Q4Q1
P1Q1Q2 P1Q2Q3 P1Q3Q4 P2Q1Q2 P1Q3Q4
P1Q2Q3 P1Q3Q4 P1Q2Q3 P2Q2Q3 P2Q3Q4
P1Q3Q4 P1Q4Q1 P1Q1Q2 P2Q3Q4 P2Q4Q1
P2Q4Q1 P2Q1Q2 P2Q4Q1 P1Q4Q1 P1Q1Q2
P2Q1Q2 P2Q2Q3 P2Q3Q4 P1Q1Q2 P1Q2Q3
P2Q2Q3 P2Q3Q4 P2Q2Q3 P1Q2Q3 P2Q2Q3
P2Q3Q4 P2Q4Q1 P2Q1Q2 P1Q3Q4 P2Q1Q2
P2Q4Q1 P2Q1Q2 P2Q4Q1 P1Q4Q1 P1Q1Q2
P2Q1Q2 P2Q2Q3 P2Q3Q4 P1Q1Q2 P1Q2Q3
P2Q2Q3 P2Q3Q4 P2Q2Q3 P1Q2Q3 P2Q2Q3
P2Q3Q4 P2Q4Q1 P2Q1Q2 P1Q3Q4 P2Q1Q2
R4U =R3U2R7
=UR5R7
=UR4.
ObviouslyR4 commutes withR. Since it commutes with each of the basic actions it
will commute with every isometry of the formRiSjTkUl. Now we just need to show that
there are no more elements in the centre. We know from analysis in GAP [26] that the
centre is isomorphic toZ2, and must contain the identity element. HenceR4 is the only
non-trivial element that can appear.(R4)2 =R8 =e, so when we create the isomorphism,
we mapR4 to the non-identity element inZ2.
□
The Bolza surface can also be tessellated by 96(2, 3, 8)triangles, each with areaπ/24.
A (2, 3, 8) triangle is fundamental domain forIsom(B). The domains that we consider
in Section 3.4 will be constructed using these triangles; for example, the equilateral
(4, 4, 4)triangles of Figure 3.1 can be barycentrically subdivided into 6(2, 3, 8)triangles.
Reﬂections in the geodesic lines in Figure 3.3 can be described as a combination ofR,
S, T, andU. In the ﬁgures of Section 3.4, a bold and a dashed line will respectively
denote Dirichlet and Neumann boundary conditions. The subscripts onR,S,T, andU
make it clear which irreducible representation we are using, and distinguishes the group
53
Table 3.2: Checking the relations between the generators of the Bolza surface
RSRS STST RTR3T UR R 7U U 2R STU US SU 2 UT RSU
P1Q4Q1 P1Q4Q1 P1Q4Q1 P1Q4Q1 P1Q3Q4 P1Q3Q4 P2Q4Q1 P2Q4Q1 P1Q4Q1 P1Q4Q1 P1Q1Q2 P1Q1Q2
P1Q1Q2 P1Q1Q2 P1Q1Q2 P1Q1Q2 P2Q3Q4 P2Q3Q4 P2Q1Q2 P2Q1Q2 P2Q4Q1 P2Q4Q1 P1Q2Q3 P1Q2Q3
P1Q2Q3 P1Q2Q3 P1Q2Q3 P1Q2Q3 P2Q4Q1 P2Q4Q1 P1Q1Q2 P1Q1Q2 P2Q3Q4 P2Q3Q4 P2Q2Q3 P2Q2Q3
P1Q3Q4 P1Q3Q4 P1Q3Q4 P1Q3Q4 P1Q4Q1 P1Q4Q1 P1Q4Q1 P1Q4Q1 P1Q3Q4 P1Q3Q4 P2Q1Q2 P2Q1Q2
P1Q4Q1 P1Q4Q1 P1Q4Q1 P1Q4Q1 P1Q3Q4 P1Q3Q4 P2Q4Q1 P2Q4Q1 P1Q4Q1 P1Q4Q1 P1Q1Q2 P1Q1Q2
P1Q1Q2 P1Q1Q2 P1Q1Q2 P1Q1Q2 P2Q3Q4 P2Q3Q4 P2Q1Q2 P2Q1Q2 P2Q4Q1 P2Q4Q1 P1Q2Q3 P1Q2Q3
P1Q2Q3 P1Q2Q3 P1Q2Q3 P1Q2Q3 P2Q4Q1 P2Q4Q1 P1Q1Q2 P1Q1Q2 P2Q3Q4 P2Q3Q4 P2Q2Q3 P2Q2Q3
P1Q3Q4 P1Q3Q4 P1Q3Q4 P1Q3Q4 P1Q4Q1 P1Q4Q1 P1Q4Q1 P1Q4Q1 P1Q3Q4 P1Q3Q4 P2Q1Q2 P2Q1Q2
P2Q4Q1 P2Q4Q1 P2Q4Q1 P2Q4Q1 P1Q2Q3 P1Q2Q3 P2Q3Q4 P2Q3Q4 P1Q1Q2 P1Q1Q2 P1Q4Q1 P1Q4Q1
P2Q1Q2 P2Q1Q2 P2Q1Q2 P2Q1Q2 P2Q2Q3 P2Q2Q3 P2Q2Q3 P2Q2Q3 P2Q1Q2 P2Q1Q2 P1Q3Q4 P1Q3Q4
P2Q2Q3 P2Q2Q3 P2Q2Q3 P2Q2Q3 P2Q1Q2 P2Q1Q2 P1Q2Q3 P1Q2Q3 P2Q2Q3 P2Q2Q3 P2Q3Q4 P2Q3Q4
P2Q3Q4 P2Q3Q4 P2Q3Q4 P2Q3Q4 P1Q1Q2 P1Q1Q2 P1Q3Q4 P1Q3Q4 P1Q2Q3 P1Q2Q3 P2Q4Q1 P2Q4Q1
P2Q4Q1 P2Q4Q1 P2Q4Q1 P2Q4Q1 P1Q2Q3 P1Q2Q3 P2Q3Q4 P2Q3Q4 P1Q1Q2 P1Q1Q2 P1Q4Q1 P1Q4Q1
P2Q1Q2 P2Q1Q2 P2Q1Q2 P2Q1Q2 P2Q2Q3 P2Q2Q3 P2Q2Q3 P2Q2Q3 P2Q1Q2 P2Q1Q2 P1Q3Q4 P1Q3Q4
P2Q2Q3 P2Q2Q3 P2Q2Q3 P2Q2Q3 P2Q1Q2 P2Q1Q2 P1Q2Q3 P1Q2Q3 P2Q2Q3 P2Q2Q3 P2Q3Q4 P2Q3Q4
P2Q3Q4 P2Q3Q4 P2Q3Q4 P2Q3Q4 P1Q1Q2 P1Q1Q2 P1Q3Q4 P1Q3Q4 P1Q2Q3 P1Q2Q3 P2Q4Q1 P2Q4Q1
generators from their irreducible representations.
Figure 3.3: Tessellation ofB by (2, 3, 8) and (4, 4, 4) (in bold) triangles
Remark 3.6Recall the side lengths of(2, 3, 8) triangles calculated in Section 2.2.3,
and the comment in the introduction regarding the systoles of the Bolza surface. From
Figure 3.3, we can see that the systole of the Bolza surface consists of four “medium
length”(2, 3, 8) triangle sides, that is,
s(B) = 4 arccosh
(
csc(π
8
)
2
)
.
54
This is equivalent to the formula
2 arccosh
(
1 +
√
2
)
from [41], given in the introduction.
3.2 Length spectrum of the Bolza surface
An expression for the lengths of primitive geodesics of the Bolza surface in terms of
algebraic numbers has been given in [2]. We have seen the form of the generators in the
introduction; an equivalent form is given by
gk =
(
cosh(l0
2
) exp(i(kπ
4
))sinh(l0
2
)
exp(−i(kπ
4
))sinh(l0
2
) cosh(l0
2
)
)
, k = 0,..., 3,
where
cosh
(l0
2
)
= cot
(π
8
)
= 1 +
√
2
describes the length of the ﬁrst geodesic. In fact, the periodic orbit matrices for all
geodesics in the spectrum take a similar form:
g =
(
α β
β∗ α∗
)
,
where
α =a +
√
2b
and
β =
√
1 +
√
2
(
c +
√
2d
)
, a, b, c, d∈ Z[i].
The lengths of the corresponding geodesics are determined by
|ℜ(α)| =m +
√
2n, m, n∈ N.
We learn from [2] thatn runs through all the natural numbers, apart fromn = 48 and
n = 72, where there are no orbits.m is the odd natural number that minimizes
|m/n−
√
2|.
Once we have obtained a sequence of(m,n) pairs from the above rule, we have a handy
way to compute the lengths of primitive geodesics in closed form, in particular
cosh
(ln−1
2
)
=m +
√
2n, m, n∈ N.
Having an exact formula for the length spectrum will be helpful later in the chapter,
when we create bounds on eigenvalue multiplicity using Selberg’s trace formula.
55
3.3 Upper bounds on eigenvalues of the Bolza surface
We use the Rayleigh quotient (Theorem 1.20) to give upper bounds on the ﬁrst two
distinct positive eigenvalues of∆(B). We have calculated these numerically and listed
them in Table C.1; in particular, the ﬁrst and second positive eigenvalues are roughly
equal to 3.84 and 5.35 respectively. Since the Rayleigh quotient is an equality for the
ﬁrst eigenfunction, the closer the test function is to the ﬁrst eigenfunction, the better the
bound will be. Rather than simply trying to guess a function, we can use the calculation
forχ8 in Section 3.4 to tell us where the function should be zero (see Figure 3.13).
We know that the ﬁrst eigenfunction satisﬁes mixed boundary conditions on a(4, 4, 4)
equilateral triangle; Dirichlet on one side and Neumann on the other two. We also know
that the eigenfunction should be radially symmetric with respect to the origin of the unit
disk, since the(4, 4, 4)triangle is rotated about the centre of the Poincare disk byR. We
will work in the upper half plane model when performing calculations, since the metric is
slightly easier to work with. Transformations between the Poincaré disk and the upper
half plane are given by the Cayley transform:
f(z) = z +i
iz + 1,
where the inverse function naturally mapsHto D. Under this transformation, a(4, 4, 4)
triangle that is symmetric with respect to the real line is now symmetric with respect to
theℑaxis, including our manufactured boundary conditions. This means we can simplify
our calculations further by integrating over the(2, 4, 8) triangle in Figure 3.4, denoted
ΩT, where the equations of the boundary curves are given by
c1(x) =
√
q2−x2
and
c2(x) =
√
csc2
(π
8
)
−
(
x + cot
(π
8
))2
,
whereq =
√
3 + 2√2− 2
√
4 + 3√2.
After some experimentation with various test functions, we settled on the function
ϕ1(x,y) =
(
y−
√
1− 22x2− 1
)(
y−
√
q2−x2
)
,
which is equal to zero onc1 due to they−
√
q2−x2 factor. Note that we only enforce
a (Dirichlet) boundary condition alongc1; the function is “free” along the other two
sides of the domain in Figure 3.4 (recall from Theorem 1.20 that test functions for a
Neumann boundary condition in the variational characterization used for the min-max
principle only have to be inW1, 2 and not identically 0). The factor ofy−√1− 22x2−1
56
i
c1
c2
Figure 3.4: The domain of integrationΩT in H
represents the circular symmetry that we observed when plotting the eigenfunction in
FreeFEM++. We started with 1 as the coeﬃcient ofx2, and after several numerical
experiments, found 22 to be among the optimal integer coeﬃcients for producing a good
bound.
We wish to evaluate theL2 norms of both this function and its gradient overΩT.
Unfortunately, thesecannotbeexplicitlycalculated, howeverwecanuseMathematica[37]
to integrate explicitly with respect toy and then approximate the ﬁnal integral using
Simpson’s rule, as we will then be integrating a continuous curve over an interval in
one variable. We are aware of the limitations of performing symbolic integration using
computer software, however the integrands that we integrate with respect toy consist
of terms that are integer powers ofy. We have chosen Mathematica to perform our
integrations, but have checked them in SAGE [79], which is open source, and have also
checked some of the less cumbersome ones by hand.
First, we considerϕ1(x, y). Integrating with respect toy allows us to deﬁne a function
inx,
h(x) =
∫ c2(x)
c1(x)
(y−√1− 22x2− 1)2(
y−
√
q2−x2
)2
y2 dy.
We do not display the closed evaluated form ofh(x) here, since it is long, unpleasant,
and tells us little information. It is given as a sum of polynomial terms ofx, as well as
their square roots and logs, and can be calculated in Mathematica with the following line
of code:
q = Sqrt [3 + 2 Sqrt [2] − 2 Sqrt [4 + 3 Sqrt [ 2 ] ] ] ;
u[x_, y_] = (y − 1− Sqrt [1 − 22 x^2]) (y − Sqrt [q^2 − x^2]);
Integrate [(u[x, y] u[x, y])/y^2, {y, Sqrt [q^2 − x^2] ,
Sqrt [Csc[ Pi/8]^2 − (x + Cot[ Pi/8])^2]}]
We now need to approximate the integral
∫ 2
1
4−1
0
h(x)dx.
57
Simpson’s rule allows us to control the accuracy of our approximation by selecting the
step size, and comes with a formula for a rigorous error bound. Moreover, both the error
bound and the approximation can be given symbolically. Recall that for an even value
ofn, Simpson’s rule approximates an integral as
∫ b
a
f(x)dx≈Sn,
where
Sn = ∆x
3 (f(x0) + 4f(x1) + 2f(x2) + 4f(x3) +... + 2f(xn−2) + 4f(xn−1) +f(xn)),
∆x =b−a
n , and xi =a +i∆x, i ∈{ 0,..., n}.
The error for such an approximation depends on the maximum value of the fourth deriva-
tive on the interval. In particular, suppose that
⏐⏐f(4)(x)
⏐⏐≤K fora≤x≤b andK∈ R.
Then ⏐⏐⏐⏐
∫ b
a
f(x)dx−Sn
⏐⏐⏐⏐≤K(b−a)5
180n4 .
We will chosen such that our error will be less than10−6 every time we approximate
with Simpson’s rule, that is, we take the smallest even value ofn such that
(
106(max
⏐⏐f(4)(x)
⏐⏐) (2
1
4− 1)5
180
)1
4
< n.
Forh(x), the maximum value will occur at the upper end of the integral, that is, at
x = 2
1
4−1. This is due to the fact that bothh(x)function and its fourth derivative include
the termlog(1−x2− 2xcot(π
8
)), which has a singularity just outside the interval.
The following line of code gives us the closed form of the fourth derivative evaluated
at 2
1
4− 1, and then substituted into our error formula.
h[x_]=Integrate [(u[x, y] u[x, y])/y^2, {y, Sqrt [q^2 − x^2] ,
Sqrt [Csc[ Pi/8]^2 − (x + Cot[ Pi /8])^2]}];
adh[x_] = Abs[D[h[x] , {x, 4}]];
((10^6) (adh[2^(1/4) − 1] (2^(1/4) − 1)^5)/180)^(1/4)
Again, the symbolic output is too long to include here, but it is approximately equal
to 89.7433. Therefore, we take ourn to be the next even integer, 90, to guarantee the
required level of accuracy. We can now approximate the integral ofh(x), and thus the
L2 norm ofϕ1(x,y), usingS90. The following input in Mathematica gives us our closed
form.
phi = ((2^(1/4) − 1)/(270)) Total [{h[0] , h[2^(1/4) − 1] ,
Total [ Table [
2 h[ i ] , {i , 2 (2^(1/4) − 1)/90,
88 (2^(1/4) − 1)/90, (2^(1/4) − 1)/45}]] ,
58
Total [ Table [
4 h[ i ] , {i , (2^(1/4) − 1)/90,
89 (2^(1/4) − 1)/90, (2^(1/4) − 1)/45}]]}]
Once again, we do not display the output due to its length. It is approximately equal
to 0.0280905. This gives‖ϕ1‖2 correct to within10−6. Since we divide by‖ϕ1‖2 in the
Rayleigh quotient, and want an upper bound on the ﬁrst eigenvalue, we want a lower
bound on‖ϕ1‖2. We take
28089
1000000<‖ϕ1‖2.
Now we need to bound the‖∇ϕ1‖2, this time from above. This time, since we are
working with the gradient, we must analyze
‖∇ϕ1‖2 =
∫ 2
1
4−1
0
∫ c2(x)
c1(x)
⟨∇ϕ,∇ϕ⟩
y2 dydx.
Note that we have the following formula for taking the scalar product of a vectorX =
Xn ∂
∂xn of dimensionn with itself, with respect to the Riemannian metric:
⟨X, X⟩ =gijXiXj,
where we use the Einstein summation convention. We also have that for the gradient of
a functionf(x1,..., xn),
∇f =
n∑
j=1
n∑
i=1
gij∂f
∂xi
∂
∂xj.
For a functionf(x, y) in H, we have
⟨∇f,∇f⟩ =g11(g11∂xf)2 +g22(g22∂yf)2
=g11(∂xf)2 +g22(∂yf)2
=y2((∂xf)2 + (∂yf)2).
Therefore, when we integrate with respect to the hyperbolic metric, they2 term cancels.
We are essentially integrating the Euclidean gradient of a function of two variable with
respect to the Euclidean metric. As before, we can integrate explicitly with respect to
they variable to deﬁne a function inx:
g(x) =
∫ c2(x)
c1(x)
((
−
√
1− 22x2−
√
q2−x2 + 2y− 1
)2
+

x(−√1− 22x2 +y− 1)
√
q2−x2 +
22x
(
y−
√
q2−x2
)
√1− 22x2


2
dy.
This can be evaluated using the following in Mathematica; again we suppress the
lengthy output.
59
q = Sqrt [3 + 2 Sqrt [2] − 2 Sqrt [4 + 3 Sqrt [ 2 ] ] ] ;
u[x_, y_] = (y − 1− Sqrt [1 − 22 x^2]) (y − Sqrt [q^2 − x^2]);
Integrate [
Grad[u[x, y] , {x, y}].Grad[u[x, y] , {x, y}] , {x, 0, 2^(1/4) − 1}, {y,
Sqrt [q^2 − x^2] , Sqrt [Csc[ Pi/8]^2 − (x + Cot[ Pi/8])^2]}]
As before, we ﬁnd a value forn, based on the maximum value of
⏐⏐g(4)(x)
⏐⏐, to ensure
Sn is accurate enough. Once again, we ﬁnd that we take the maximum value ofx in our
interval, that is,2
1
4− 1, to achieve this maximum. Our error formula is
g[x_]=Integrate [
Grad[u[x, y] , {x, y}].Grad[u[x, y] , {x, y}] , {x, 0, 2^(1/4) − 1}, {y,
Sqrt [q^2 − x^2] , Sqrt [Csc[ Pi/8]^2 − (x + Cot[ Pi/8])^2]}]
adg[x_] = Abs[D[g[x] , {x, 4}]];
((10^6) (adg[2^(1/4) − 1] (2^(1/4) − 1)^5)/180)^(1/4)
This time we ﬁnd that we must taken = 150in Simpson’s formula. Our approximation
is calculated with the following in Mathematica:
gradphi=((2^(1/4) − 1)/(450)) Total [{g[0] , g[2^(1/4) − 1] ,
Total [ Table [
2 g[ i ] , {i , 2 (2^(1/4) − 1)/150,
148 (2^(1/4) − 1)/150, (2^(1/4) − 1)/75}]] ,
Total [ Table [
4 g[ i ] , {i , (2^(1/4) − 1)/150,
149 (2^(1/4) − 1)/150, (2^(1/4) − 1)/75}]]}];
The symbolic form of this is approximately equal to 0.1164682, correct again to within
10−6. We need an upper bound for‖∇ϕ1‖2, so we take
‖∇ϕ1‖2< 116469
1000000.
We can ﬁnally bound the ﬁrst positive eigenvalue of the Bolza surface by
λ1≤R (ϕ1)< 116469
28089≈ 4.1464274.
It is possible to bound higher eigenvalues using the min-max principle. We will need an
upper bound forλ2 in order to prove that it has multiplicity 4. The Rayleigh quotient of
a functionϕ2 that is orthonormal toϕ1 will give us such a bound, if we chose the function
appropriately (that is,{ϕ1, ϕ2} form a 2 dimensional subspace ofW1, 2
0 as required by
Theorem 1.22).
Remark 3.7Why is it suﬃcient to only consider two test functions? There are three
functions corresponding to the ﬁrst eigenvalue on the entire surface, but here we have re-
stricted ourselves to a fundamental domainΩof a subgroup of the isometry groupIsom(B).
By reﬂection, we can extend an eigenfunction on this domain to one on the entire sur-
face (see Remark 3.11). In particular, when we reﬂect the domain along its “free” edges,
that is, the edges with a Neumann boundary condition, we get a larger region with closed
60
Dirichlet boundary. It is well known that the ﬁrst Dirichlet eigenvalue of a connected
domain is simple (has multiplicity one) and strictly positive (see, for example, [27]), so
there will only be one corresponding function whose Rayleigh quotient, when evaluated
over Ω, gives this eigenvalue. Therefore, we only need to consider a two dimensional
subspace ofW1, 2
0 to get an upper bound on the second positive eigenvalue ofΩ.
The test function we would like to work with is
ϕ2(x, y) =
(
11y
2 −
(11y
2
)3
3! +
(11y
2
)5
5! −
(11y
2
)7
7! +
(11y
2
)9
9! −
(11y
2
)11
11!
)(
1− x2
100
)
.
Here the1− x2
100 factor is to represent the behaviour of an eigenfunction ofλ2 observed
in a numerical plot. We started with1−x2, and found experimentally that reducing the
size of thex2 coeﬃcient gave a better bound. Note that the ﬁrst term in the product is
clearly an approximation ofsin(11y
2
). We initially constructed an orthonormal set of test
functions using trigonometric functions as an obvious choice (again experimenting to ﬁnd
an “optimal” coeﬃcient; although we couldn’t produce accurate enough bounds with these
alone, we found that by modifying them with a factor derived from our numerical insight,
we were able to produce good enough bounds. We use the Taylor series approximation
so that we can evaluate⟨ϕ1, ϕ2⟩ (integrating a polynomial function is much easier with
respect to the hyperbolic metric over this domain). Fortunately, the approximation gives
a slightly better bound than the function itself.
We use the Gram-Schmidt procedure onϕ2 andϕ1 to construct a function˜ϕ2 that is
orthogonal toϕ1, by subtracting a “projection” ofϕ1 fromϕ2:
˜ϕ2(x, y) =ϕ2(x, y)−⟨ϕ1, ϕ2⟩
‖ϕ1‖2 ϕ1(x, y)
Let us consider the inner product in the numerator of the projection. As we have alluded,
we may integrate it explicitly with respect toy:
q = Sqrt [3 + 2 Sqrt [2] − 2 Sqrt [4 + 3 Sqrt [ 2 ] ] ] ;
u[x_, y_] = (y − 1− Sqrt [1 − 22 x^2]) (y − Sqrt [q^2 − x^2]);
v[x_, y_] = (11 y/2 − ((11 y/2)^3)/3! + ((11 y/2)^5)/
5! − ((11 y/2)^7)/7! + ((11 y/2)^9)/9! − ((11 y/2)^11)/11!) (1 −
x^2/100);
Integrate [(u[x, y] v[x, y])/y^2, {y, Sqrt [q^2 − x^2] ,
Sqrt [Csc[ Pi/8]^2 − (x + Cot[ Pi/8])^2]}]
We deﬁne a functionp(x),x∈ [0, 2
1
4−1], as the output of this integral and once again
use Simpson’s rule to approximate it. Similar computations to before show us that we
needn = 146for our desired degree of accuracy, and we proceed in the same vein:
p[x_]=Integrate [(u[x, y] v[x, y])/y^2, {y, Sqrt [q^2 − x^2] ,
Sqrt [Csc[ Pi/8]^2 − (x + Cot[ Pi /8])^2]}];
P = ((2^(1/4) − 1)/(3 146)) Total [{p[0] , p[2^(1/4) − 1] ,
61
Total [ Table [
2 p[ i ] , {i , 2 (2^(1/4) − 1)/146,
144 (2^(1/4) − 1)/146, (2^(1/4) − 1)/73}]] ,
Total [ Table [
4 p[ i ] , {i , (2^(1/4) − 1)/146,
145 (2^(1/4) − 1)/146, (2^(1/4) − 1)/73}]]}];
This constantP is correct to with10−6. We get an upper and lower bound bound on
⟨ϕ1, ϕ2⟩:
− 9662
1000000<⟨ϕ1, ϕ2⟩<− 9660
1000000.
We have already seen the lower bound on‖ϕ1‖2, and we can easily obtain an upper bound
from our knowledge of the error. We get
28089
1000000<‖ϕ1‖2< 28091
1000000.
Therefore we get can bound the projection coeﬃcient from above and below by
− 9662
28089<⟨ϕ1, ϕ2⟩
‖ϕ1‖2 <− 9660
28091.
We will also need to consider terms involving the square of the projection coeﬃcient, so
we include now the relevant bounds:
93315600
789104281<
(⟨ϕ1, ϕ2⟩
‖ϕ1‖2
)2
< 93354244
788991921.
We are now ready to bound theL2 norm of˜ϕ2 from below. We have
‖˜ϕ2‖2 =
∫ 2
1
4
0
∫ c2(x)
c1(x)
1
y2
(
ϕ2
2− 2⟨ϕ1, ϕ2⟩
‖ϕ1‖2 ϕ1ϕ2 +
(⟨ϕ1, ϕ2⟩
‖ϕ1‖2
)2
ϕ2
1
)
dydx
≥
∫ 2
1
4
0
(∫ c2(x)
c1(x)
(ϕ2
y
)2
dy + 2
( 9660
28091
)
p(x) + 93315600
789104281h(x)
)
dx.
As before, we can integrate ∫ c2(x)
c1(x)
(ϕ2
y
)2
dy
explicitly using the following line of code in Mathematica, where the output deﬁnes a
functionc(x):
q = Sqrt [3 + 2 Sqrt [2] − 2 Sqrt [4 + 3 Sqrt [ 2 ] ] ] ;
v[x_, y_] = (11 y/2 − ((11 y/2)^3)/3! + ((11 y/2)^5)/
5! − ((11 y/2)^7)/7! + ((11 y/2)^9)/9! − ((11 y/2)^11)/11!) (1 −
x^2/100);
Integrate [(v[x, y] v[x, y])/y^2, {y, Sqrt [q^2 − x^2] ,
Sqrt [Csc[ Pi/8]^2 − (x + Cot[ Pi/8])^2]}]
We now use Simpson’s rule to approximate
∫ 2
1
4
0
(
c(x) + 2
( 9660
28091
)
p(x) + 93315600
789104281h(x)
)
dx. (3.1)
62
We ﬁnd that we need to taken = 194 for the required degree of accuracy, and the
following code generates our approximation. As before, the symbolic output is yet longer
and so we do not display it.
c [x_] = Integrate [(v[x, y] v[x, y])/y^2, {y, Sqrt [q^2 − x^2] ,
Sqrt [Csc[ Pi/8]^2 − (x + Cot[ Pi /8])^2]}];
v2[x_] = c [x] + 2 (9660/28091) p[x] + (9660/28091)^2 h[x ];
V = ((2^(1/4) − 1)/(3 194)) Total [{v2[0] , v2[2^(1/4) − 1] ,
Total [ Table [
2 v2[ i ] , {i , 2 (2^(1/4) − 1)/194,
192 (2^(1/4) − 1)/194, (2^(1/4) − 1)/97}]] ,
Total [ Table [
4 v2[ i ] , {i , (2^(1/4) − 1)/194,
193 (2^(1/4) − 1)/194, (2^(1/4) − 1)/97}]]}];
From this, we achieve the following lower bound:
‖˜ϕ2‖2> 252552
1000000.
Remark 3.8Whilst this is an accurate bound for the integral in Equation(3.1), we have
lost some overall accuracy through the propagation of error through division and squaring
in our bounds for the projection coeﬃcient.
All that remains is to bound‖∇˜ϕ2‖2. This time we want an upper bound, so we use
the alternative bounds on our projection coeﬃcient to get the following inequality:
‖∇˜ϕ2‖2≤
∫ 2
1
4
0
(∫ c2(x)
c1(x)
⟨∇ϕ2,∇ϕ2⟩dy + 2
( 9662
28089
)∫ c2(x)
c1(x)
⟨∇ϕ2,∇ϕ1⟩dy
+ 93354244
788991921
∫ c2(x)
c1(x)
⟨∇ϕ1,∇ϕ1⟩dy
)
dx
Note that here, the angular brackets are for the scalar product of vector ﬁelds rather
than theL2 inner product. The integrals with respect toy can all be evaluated using
Mathematica; indeed we have already analyzed the third. At this stage we are doing
nothing new, so can speed up the process to deﬁne our function ofx:
gradv2 [x_] =
Integrate [
Grad[v[x, y] , {x, y}].Grad[v[x, y] , {x, y}] , {y, Sqrt [q^2 − x^2] ,
Sqrt [Csc[ Pi/8]^2 − (x + Cot[ Pi/8])^2]}] +
2 (9662/28089) Integrate [
Grad[u[x, y] , {x, y}].Grad[v[x, y] , {x, y}] , {y, Sqrt [q^2 − x^2] ,
Sqrt [Csc[ Pi/8]^2 − (x + Cot[ Pi/8])^2]}] + (9662/
28089)^2 Integrate [
Grad[u[x, y] , {x, y}].Grad[u[x, y] , {x, y}] , {y, Sqrt [q^2 − x^2] ,
Sqrt [Csc[ Pi/8]^2 − (x + Cot[ Pi/8])^2]}]
We need to setn = 192to reach our desired degree of accuracy, andS192 is calculated
with the following, where “gradv2zero” is the value of the function at zero..
63
gradv2zero =
1/47439344237055551266766192640000
(42733474853681838723362084401119381839 +
30216456180729532565343854445094502400 Sqrt [2] −
14884598099207334170365080185497190400 Sqrt [4 + 3 Sqrt [2]] −
10524501996471252904537914913220198400 Sqrt [8 + 6 Sqrt [2]] −
14701142201104864428066135243859376480655624 Sqrt [
6 + 4 Sqrt [2] − 4 Sqrt [4 + 3 Sqrt [2]]] −
20790554698446527074663610993142635407996047 Sqrt [
3 + 2 Sqrt [2] − 2 Sqrt [4 + 3 Sqrt [2]]] +
7241572618891368984131337252583167797784996 Sqrt [
24 + 17 Sqrt [2] − 8 Sqrt [4 + 3 Sqrt [2]] −
6 Sqrt [8 + 6 Sqrt [2]]] +
5120565152731139523888774472702071524171224 Sqrt [
2 (24 + 17 Sqrt [2] − 8 Sqrt [4 + 3 Sqrt [2]] −
6 Sqrt [8 + 6 Sqrt [2]])]);
GradV = ((2^(1/4) − 1)/(3 192)) Total [{ gradv2zero ,
gradv2[2^(1/4) − 1] ,
Total [ Table [
2 gradv2 [ i ] , {i , 2 (2^(1/4) − 1)/192,
190 (2^(1/4) − 1)/192, (2^(1/4) − 1)/96}]] ,
Total [ Table [
4 gradv2 [ i ] , {i , (2^(1/4) − 1)/192,
191 (2^(1/4) − 1)/192, (2^(1/4) − 1)/96}]]}]
The upshot of this is that we now have the upper bound we were seeking, namely,
‖∇ ˜ϕ2‖2< 1408244
1000000,
and thus, an upper bound on the second positive eigenvalue of the Bolza surface:
λ2≤R ( ˜ϕ2)< 1408244
252552≈ 5.57606.
If a Dirichlet boundary problem corresponding to an irreducible representation gives a
lower bound in the Faber-Krahn inequality that is greater thanR(ϕ1), it cannot appear in
E1. We aim to prove that there are only two irreducible representations that allow a lower
bound that is less thanR(ϕ1). One will be the trivial representation, which corresponds
to the trivial eigenspaceE0, the other toE1. We will use the notationλ1(χi) to denote
the ﬁrst positive eigenvalue of theith irreducible representation, and the notationΩi to
denote the boundary of the subspace ofB corresponding to boundary conditions coming
from theith irreducible representation. We will then show that the trivial representation
cannot appear.
3.4 First eigenspace of the Bolza surface
Theorem 3.9The dimension of the ﬁrst eigenspaceE1 of ∆ is 3, and the irreducible
representation appearing in this eigenspace isχ8.
64
In order to calculate the dimension of the ﬁrst eigenspace, we must use the irreducible
representations ofIsom(B)to create boundary value problems on the surface. Then, using
the Faber-Krahn inequality, we can determine which irreducible representations appear
inE1 (counting multiplicity).
Since we can describe the isometry group as a ﬁnitely presented group on 4 elements,
satisfying a set of relations, we can use GAP [26] to obtain information about the repre-
sentation theory of the group. This is shown in Appendix A. To come up with boundary
value problems corresponding to a particular irreducible representation, we need the ma-
trices associated to each of the four generators ofIsom(B).
Given a fundamental domainΩ⊂B with respect to the action of eitherIsom(B) or
one of its subgroups, a reﬂection in one of its sides will correspond to the action of some
Φ∈ Isom(B). Such an Ω consists of one or more(2, 3, 8) triangles. We consider the
following three domains:
• a single(2, 3, 8) triangle, which is the fundamental domain given by the action of
the whole isometry group;
• half of a(4, 4, 4)triangle, corresponding the the subgroup ofIsom(B) generated by
R,S, andT;
• a right-angled pentagon of areaπ
2, corresponding to the subgroup ofIsom(B) gen-
erated byR4,S, andT.
For every irreducible representationχi of Isom(B), we want to see how a non-zero
vector is moved byχi to adjacent fundamental domains. The aim is to construct a vector
vfrom the basis of eigenvectors of the representation matrices, that satisﬁes eitherΦv =v
or Φv =−v; thiswillimplythateitherthenormalderivativeofthevectorvaluedfunction,
or the function itself, will vanish on∂Ω, hence corresponding to either a Neumann or
Dirichlet boundary condition respectively. Diﬀerent irreducible representations will give
diﬀerentboundaryconditionsonafundamentaldomain. SinceouraimistousetheFaber-
Krahn inequality, we must have a domain with purely Dirichlet boundary conditions. If
we have a mixed boundary value problem onΩ, we extend the domain by reﬂecting
in a boundary geodesic that has a Neumann condition. In this way, we obtain closed
domains with only Dirichlet boundary conditions. The isoperimetric inequality is known
to be satisﬁed in the hyperbolic plane, so for simply connectedΩwith Dirichlet boundary
conditions, we may apply Faber-Krahn. Before we use this method on the complicated
isometry group of the Bolza surface, we give an example using the simplest groupZ2 to
make the method clear.
65
Example 3.10 (Z2) Z2 is the isometry group of a kiteK with only one line of symmetry,
generated by a single reﬂectionS.
Figure 3.5: KiteK with one line of symmetry
s
Z2 has two irreducible representations,M1 andM2, both one dimensional.M1 is the
trivial representation, whereS1 takes the value 1. OnM2, S2 takes the value−1. A
fundamental domain forZ2 acting onK is one of two scalene triangles (for example, the
one shaded in Figure 3.5). We look at a vector valued functionf that takes valuev⁄= 0
on the shaded region, and see how it is aﬀected by the group action. Since both irreducible
representations are one dimensional,v∈ R.
When we map the shaded region to the white region, the value ofv on the white region
becomesSv. Restricting toM1,S1 = 1, soS1v =v. Hence all functionsf that correspond
to M1 are even with respect to the line of symmetry. On the other hand, restricting to
M2, S2v =−v, so the functions that correspond toM2 are odd with respect to the line
of symmetry. Functions corresponding toM2 will therefore disappear on this line. If we
were solving a Dirichlet boundary value problem onK, we could restrict the problem to
the fundamental domain with Dirichlet boundary conditions in the case ofM2; in the case
ofM1 we could restrict to a mixed boundary problem on the fundamental domain, with a
Neumann condition on the dashed line.
Remark 3.11This technique was used in [41,42] in precisely the same manner as we
intend to use it, and was also used in [43] to investigate the relationship between geodesics
on a hyperbolic surface, and the nodal lines of Laplace eigenfunctions. Given a surfaceS
with isometry groupIsom(S), and a fundamental domainΩ for the action of a subgroup
of Isom(S), it allows us to extend an eigenfunctionf of the mixed boundary problem on
Ω, to one on the whole surfaceS. The following sketched proof comes from [43]. For
the Dirichlet case, letf = 0 on a geodesic boundary edgeB∈∂Ω. Since the Laplacian
commutes with the isometry group ofS, for a reﬂectionrB∈ Isom(S) aboutB such
that f◦ rB =−f, the composition is also an eigenfunction of the Laplacian with the
same eigenvalue. Letg =f, g :S→ R on one component ofS−B andg =−f◦ rB
on the other.g is now a weak solution to the eigenvalue problem, and by the elliptic
66
regularity theorem, a strong solution also.f = g on an open set, sof = g on S, and
f =−f◦rB. For a Neumann boundary condition, diﬀerentiating an even function gives
an odd function and the hence the gradient ofv will vanish on this part of∂Ω, and we
follow a similar argument.
In this proof, we will systematically produce lower bounds on the ﬁrst eigenspace
in which the representation can appear. We will show that onlyχ8 can appear in the
ﬁrst eigenspace ofB. We will start with the 1 dimensional irreducible representations,
χ1,...,χ 4. Sinceχ1 gives Neumann conditions on all three sides of a(2, 3, 8) triangle,
it will correspond to the ﬁrst Neumann eigenspace, that is, the trivial eigenspaceE0. We
also have to show that it does not appear again inE1, but we will defer the proof of
this to Lemma 3.15. In the following, we will denote byνx the ﬁrst zero of the Legendre
function
P−s
(
cosh
(
2 arcsinh
(√x
4π
)))
=P−s
(
1 + x
2π
)
,
wherex is ﬁxed and we considerP−s as a function oft withs = 1
2 +it. Thenνx is the
ﬁrst eigenvalue of the hyperbolic disk of areax with Dirichlet boundary condition (see
the analysis in [38, Chapter 1]).
By the Faber-Krahn inequality, we can useνx as a lower bound for Dirichlet boundary
problems on domains on areaxthat satisfy the isoperimetric inequality (Deﬁnition 1.13).
Inturn, weneedalowerbound onνxforeachx. Thelargestdomainwhoseﬁrsteigenvalue
we bound using the Faber-Krahn inequality has areaπ. By the property of domain
monotonicity for Dirichlet eigenvalues (Remark 1.7), a disk with areaπ will have a lower
ﬁrst Dirichlet eigenvalue than any disk with smaller area, that is,
νπ<νx ∀x<π.
Therefore, we just need to boundνπ from below in order to get a lower bound on every
otherνx that we consider. Note that this bound will be far from optimal asx decreases,
but it suﬃces for it to be larger than our upper bound on the ﬁrst eigenvalue of the whole
surface, that is,116469
28089.
Forx =π, we consider the ﬁrst zero of the functionP−s
(3
2
), wheres = 1
2−it. As a
hypergeometric function, this is
f(t) = 2F1
(1
2−it, 1
2 +it; 1;−1
4
)
.
We can approximatef(t) using its power series; recall the general deﬁnition from Sec-
tion 2.3.1:
2F1 (a,b;c;z) =
∞∑
k=0
(a)k(b)k
(c)kk! zk,
67
and that this power series converges ifc is not a negative integer, and|z|< 1. As both
of these conditions are satisﬁed forf(t), we know that the functions given by the partial
sums, that is,
fn(t) =
n∑
k=0
(1
2−it)
k
(1
2 +it)
k
(1)kk!
(
−1
4
)k
,
approximatef(t) more and more closely for eachn. Considering the numerator
(1
2−it
)
k
(1
2 +it
)
k
,
we see that fork = 1we have
(1
2−it
)( 1
2 +it
)
=
(1
4 +t2
)
,
fork = 2,
(1
2−it
)( 1
2 +it
)( 3
2−it
)( 3
2 +it
)
=
(1
4 +t2
)( 9
4 +t2
)
,
and so on. This means that the numerator will always be a polynomial with even powers
of t; in particular it will be positive. Now note that the series is alternating, due to
the(−1
4
) term. This means that for oddn, fn(t)< f(t), and for evenn, fn(t)> f(t).
Therefore, we can bound the ﬁrst positive zero off(t) from below by the ﬁrst positive
zero offn(t) forn odd. It turns out that takingf3(t) already gives us a good enough
lower bound.
We need to ﬁnd the ﬁrst positive real root of
f3(t) =− t6
2304 + 109t4
9216− 8035t2
36864 + 15479
16384.
Note that this function is cubic int2, so we can use Cardano’s formula to ﬁnd a real value
oft2 such thatf3(t) = 0. Cardano’s formula states that the real root of a general cubic
equation
ax3 +bx2 +cx +d = 0
is given by
x =− 1
3a
(
b +C + ∆0
C
)
,
where
∆0 =b2− 3ac,
∆1 = 2b3− 9abc+ 27a2d, and
C =
3
√
∆1±
√
∆2
1− 4∆3
0
2 .
68
Forf3(t) = 0, we ﬁnd that
t2 = 1
12
(
109− 1528
3
√
108√789− 1495
+ 8
3
√
108
√
789− 1495
)
= 23
4
is a root, and thus
√23
2 is the positive zero off3(t). To check this, we have
f3
(√23
2
)
=− 12167
147456+ 57661
147456− 184805
147456+ 15479
16384 = 0.
This gives us our lower bound:
νπ>
(√23
2
)2
+ 1
4 = 6.
Forχ2, R2v =U2v =v andS2v =T2v =−v, so any reﬂection will give a Dirichlet
condition (since all reﬂections are orientation reversing). We therefore have a Dirichlet
boundary problem on one of the(2, 3, 8) triangles, with areaπ
24, so we may use the
Faber-Krahn inequality, which gives us
λ1(χ2)≥νπ
24 >νπ> 6.
This rules outχ2.
Figure 3.6: Boundary conditions forχ2
Forχ3,R3v =T3v =−v andS3v =U3v =v. The Dirichlet boundary problem is one
of the equilateral(4, 4, 4) triangles, with areaπ
4. The Faber-Krahn inequality gives us
λ1(χ3)≥νπ
4 >νπ> 6.
This rules outχ3.
69
Figure 3.7: Boundary conditions forχ3
Forχ4, R4v = S4v =−v andT4v = U4v = v. In this case the Dirichlet boundary
problem is the double of a(2, 3, 8) triangle (reﬂection along the hypotenuse). This has
area π
12. The Faber-Krahn inequality gives us
λ1(χ4)≥νπ
12 >νπ> 6.
This rules outχ4.
Figure 3.8: Boundary conditions forχ4
For the 2 and 3 dimensional irreducible representations, we consider the irreducible
representations of the symmetry group (given in Appendix A after the ﬁrst set of ir-
reducible representations) acting on the standard basis ((1, 0)T, (0, 1)T for dimension
2, and similarly for dimension 3). These correspond to the basis of eigenfunctions in
the eigenspace corresponding to a representation, for example, ife1 is a function in the
eigenspace corresponding toχ5, its vector representation will be(1, 0)T.
Forχ5, ﬁrst notice that the matrix representation ofT5 is−I2, whereIn denotes the
70
n×nidentity matrix. Now see thatR5S5 =−I2 andR2
5 =I2. We represent the function
˜u =e1−e2 as a vectoru =
(
1
−1
)
, we see thatS5u =−u. Therefore
Ri
5S5u =



R5S5u, ifi∈{ 1, 3, 5, 7},
S5u, ifi∈{ 0, 2, 4, 6},
and
Ri
5S5u =−u i ∈{ 0,..., 8}.
We see that the Dirichlet boundary problem is half of a(4, 4, 4) triangle, with areaπ
8.
The Faber-Krahn inequality gives us
λ1(χ5)≥νπ
8 >νπ> 6.
This rules outχ5.
Figure 3.9: Boundary conditions forχ5
Forχ6, note thatT6 =R6S6 =I2. We only need to consider the eigenvectors ofS6.
Again, let˜u =e1−e2, thenu =
(
1
−1
)
, and
S6u =Ri
6S6u =−u, i ∈{ 0, 2, 4, 6}.
Here we have a larger Dirichlet boundary problem; we use the side associations to see
that it has areaπ. The Faber-Krahn inequality gives us
λ1(χ6)≥νπ> 6.
This rules outχ6.
Things are slightly trickier in 3 dimensions; we must consider more than one boundary
value problem for each representation. We consider one of the 16(4, 4, 4) triangles that
tessellates the Bolza surface, as well as its line of symmetry with respect to the real line.
71
Figure 3.10: Boundary conditions forχ6
S
RS
R7S
T
Figure 3.11:(4, 4, 4) triangle with line of symmetry
Forχ7, we consider the vectore1 = (1, 0, 0)T. We haveR7S7e1 =T7e1 =e1, S7e1 =
R7
7S7e1 =−e1. Fore2 = (0, 1, 0)T we haveR7S7e2 =S7e1 =−e2, R7
7S7e2 =T7e2 =e2,
and fore3 = (0, 0, 1)T we haveR7S7e3 =R7
7S7e3 =e3,S7e3 =T7e3 =−e3. When closed,
the Dirichlet boundary problem for each basis function, shown in Figure 3.12, contains
an area ofπ
4. As above, Faber-Krahn shows us
λ1(χ7)≥νπ
4 >νπ> 6.
This rules outχ7.
(a) e1 (b) e2 (c) e3
Figure 3.12: Boundary conditions forχ7
Forχ8, we again considere1,e2, ande3 as above. We have:R8S8e1 =S8e1 =T8e1 =e1
andR7
8S8e1 =−e1;R7
8S8e2 =S8e2 =T8e2 =e2 andR8S8e2 =−e2; andR8S8e3 =S8e3 =
R7
8S8e3 = e3 and T8e3 =−e3. We observe that in each case the Dirichlet boundary
72
contains an area of2π, that is, half of the surface. Courant’s nodal domain theorem tells
us that the ﬁrst eigenfunction has exactly 2 nodal domains, so we now have a candidate
for the ﬁrst eigenspace. We would expect the Faber-Krahn inequality to produce a bound
that does not rule outχ8. Indeed, it tells us that
λ1(χ8)≥ν2π≈ 3.66204.
This means thatχ8 could appear in the ﬁrst eigenspace.
(a) e1 (b) e2 (c) e3
Figure 3.13: Boundary conditions forχ8
Forχ9, we have:R9S9e1 =S9e1 =T9e1 =−e1 andR7
9S9e1 =e1; R7
9S9e2 =S9e2 =
T9e2 =−e2 andR9S9e2 =e2; andR9S9e3 =S9e3 =R7
9S9e3 =−e3 andT9e3 =e3. The
Dirichlet boundary problems corresponding toe1 ande2 involve a triangle with areaπ
8,
ande3 corresponds to a triangle of areaπ
4. The Faber-Krahn inequality gives us
λ1(χ9)≥νπ
4 >νπ> 6.
This rules outχ9.
(a) e1 (b) e2 (c) e3
Figure 3.14: Boundary conditions forχ9
Finally, forχ10 we have: R10S10e1 = T10e1 =−e1 and R7
10S10e1 = S10e1 = e1;
R7
10S10e2 = T10e2 =−e2 andR10S10e2 = S10e2 = e2; andR10S10e3 = R7
10S10e3 =−e3
andT10e3 =S10e3 =e3. In each case, the Dirichlet boundary problem corresponds to a
quadrilateral with areaπ
2. The Faber-Krahn inequality yields
λ1(χ10)≥νπ
2 >νπ> 6.
This rules outχ10.
73
(a) e1 (b) e2 (c) e3
Figure 3.15: Boundary conditions forχ10
The four dimensional irreducible representations of the isometry group of the Bolza
surface correspond to the boundary conditions on a (non-regular) right-angled hyperbolic
pentagon, of areaπ
2, shown in Figure 3.16. Note that due to the relations in Theorem 3.3,
we haveR2TR6 =T andRTR7 =R4T. Forχ11, the vector


1
2
(−i−√3)
1
2
((−2−i) +√3)
1
4
((−2 +i) +√3)(i +√3)
1


satisﬁes the boundary conditions. Forχ12 it is


1
2
((1 + 2i)−i√3)
1
1
2
(i−√3)
1


,
and forχ13 it is 

1
−1(1
2 + i
2
)(1 +√3)
1


.
Figure 3.16: Pentagon with boundary conditions
S
R4S
T
T
R4T
74
There is no way to create a region with closed Dirichlet boundary as we have done
with the triangles corresponding to lower dimensional irreducible representations. We
therefore cannot use the Faber-Krahn inequality to create a lower bound on the ﬁrst
eigenvalue of the pentagon.
On the other hand, we can reﬂect the pentagon along the vertical side, which has a
Neumann boundary condition, usingR4S, to create a right-angled hyperbolic hexagon
of areaπ. This is shown in Figure 3.17, along with its boundary conditions. Observe
that the hexagon now has two Neumann boundaries of the same length,a anda′. In
particular, the side lengths of the hexagon are as follows:
l(a) =l(a′) =l(α) = 2 arccosh
(
csc(π
8
)
2
)
≈ 1.52857,
l(b) =l(b′) = arccosh
(
csc(π
8
)
2
)
≈ 0.764285,
l(c) = 2 arccosh
(
2 cos(π
8
)
√3
)
+ 2 arccosh
(
cot(π
8
)
√3
)
≈ 2.44845,
l(d) = arccosh
(
2 cos(π
8
)
√3
)
+ arccosh
(
cot(π
8
)
√3
)
≈ 1.22423.
An eigenfunction on the hexagon is even with respect to the vertical sided; it will take
the same values onaas it does ona′. Therefore we can “glue”atoa′ to create an annulus
Ωthat lies within a hyperbolic cylinder. It has one geodesic boundary and one piecewise
geodesic boundary composed of three geodesics. Eigenfunctions on this surface will be
periodic and will satisfy Dirichlet conditions on the boundary.
Figure 3.17: Hexagon from reﬂection along the vertical
aa′
bb′
c
d
α
We have already seen that the circumference of a disk of areaπ is
2π sinh
(
2 arcsinh
(1
2
))
≈ 7.02481.
75
Figure 3.18: Cylinder from gluinga toa′
a≈a′
bb′
c
α
On the other hand, the boundary ofΩ, after gluing, has length
2 arccosh
(
2 cos(π
8
)
√3
)
+ 2 arccosh
(
cot(π
8
)
√3
)
+ 4 arccosh
(
csc(π
8
)
2
)
≈ 5.50559.
The annulusΩ does not satisfy the hypothesis of the Faber-Krahn inequality. In order
to rule out the 4 dimensional irreducible representations, we need to make use of the
following conjecture about the ﬁrst Dirichlet eigenvalue ofΩ.
Conjecture 3.12Let Ω be the annulus described above (alternatively, the right angled
pentagon with boundary conditions as in Figure 3.16). Thenλ1(Ω)> 4.15.
Remark 3.13There is strong numerical evidence to support this conjecture. Table C.2
shows the eigenvalues ofΩ with boundary conditions as in Figure 3.16, calculated using
FreeFEM++ (the corresponding code is also given in Appendix C). One can see that the
ﬁrst positive eigenvalue is approximately 5.35, and can compare this with the spectrum
ofB given in Table C.1, where the same eigenvalue appears with multiplicity 4. Unfor-
tunately, we were not able to prove this conjecture rigorously, but in Section 3.4.1, we
outline a method that could be used to produce the relevant bound.
The truth of this conjecture would imply thatλ(χ11), λ(χ12), and λ(χ13) do not
appear inE1. Assuming this, we continue our proof of Theorem 3.9 by ruling out the
trivial representation,χ1. We require the following corollary to Courant’s nodal domain
theorem (Theorem 1.12):
Proposition 3.14[18, Proposition 1.1] For Neumann boundary problems, the number of
nodal domains of the eigenfunction corresponding to the ﬁrst positive eigenvalue is 2. For
Dirichlet boundary problem problems, the number of nodal domains of the eigenfunction
corresponding to the second positive eigenvalue is 2.
76
Lemma 3.15The trivial representation does not appear inE1.
Proof: To prove this, we will consider the ﬁrst positive Neumann eigenvalue of the
(2, 3, 8) triangle. Proposition 3.14 implies that there will be a nodal line within the
triangle that separates it into two domains. The line can intersect two of the boundary
lines, one boundary line twice, or be contained entirely in the triangle. In the case where
it is contained entirely, it already bounds a Dirichlet region in the triangle; by domain
monotonicity it will certainly have a ﬁrst eigenvalue larger than that of the(2, 3, 8)
triangle with Dirichlet boundary conditions. In the case where it intersects one boundary
twice, when we extend the eigenfunction to the entire surface, the nodal line will bound
a Dirichlet region over two(2, 3, 8) triangles, and so will have a ﬁrst eigenvalue larger
than that of a hyperbolic disk of areaπ
12.
In the case where the nodal line intersects two edges of the triangle, we can quickly
convince ourselves that the largest possible domain it can bound occurs when it intersects
the two largest edges; when we extend such a nodal line to the surface, it will be contained
in one of 6 small octagons, each of area2π
3 , which tessellate the surface. By domain
monotonicity, this Dirichlet region will have an eigenvalue larger than that of the2π
3
octagon. Using Faber-Krahn, we see that such an octagonΩO satisﬁes
λ1(ΩO)≥ν2π
3
>νπ> 6.
Hence the trivial representation does not appear in the ﬁrst eigenspace. □
The ﬁnal thing we must show is thatχ8 only appears once in the ﬁrst eigenspace, that
is, we know that the dimension of the ﬁrst eigenspace is a multiple of 3, but it remains
to prove that it is exactly 3. To do this, we prove that the multiplicity is strictly less
than 6. We use the upper bound on the ﬁrst eigenvalue (from Section 3.3) to create a
bound on the multiplicity using Selberg’s trace formula (see Theorem 2.47). Considering
the spectral side of the formula, we have
h(t0) +mh(t1)<
∑
j
h(tj),
wherem is the multiplicity that we wish to bound. Rearranging this gives
m<
∑
jh(tj)−h(t0)
h(t1) ,
and we will choose a functionh(t) such that
m<
∑
jh(tj)−h(t0)
h(t1) <
∑
jh(tj)−h(t0)
h
(√
116469
28089 + 1/4
),
77
that is, it is decreasing on the interval containingt1 and
√
116469
28089 + 1/4 (recalling our
bound on the ﬁrst eigenvalue). We calculate the value of∑
jh(tj) using the geometric
side of Selberg’s trace formula. We only have precise information about the multiplicity
of the systole, so we use the test function
h(t) =
(sin(tL)
tL
)4
,
as in [38], so that the Fourier transform
g(ξ) = 1
192L4
((ξ− 4L)3sgn(ξ− 4L)− 4(ξ− 2L)3sgn(ξ− 2L)− 4(2L +ξ)3sgn(2L +ξ)
+(4L +ξ)3sgn(4L +ξ) + 6ξ3sgn(ξ))
is supported on[−4L,4L], where4L is taken to be less than the length of the second
primitive geodesic. Using the formula from Section 3.2, we know this is
2 arccosh
(
3 + 2
√
2
)
≈ 4.896904895356152.
In this way, we only get a contribution from the ﬁrst length
2 arccosh
(
1 +
√
2
)
≈ 3.057141839.
We can choose any
L< 1
2 arccosh
(
3 + 2
√
2
)
,
however, we want our bound to be optimal. We can run a program in Mathematica (see
Appendix F) to numerically plot how the bound onm changes when we evaluate the
geometric side of the formula for diﬀerent values ofL. In this way, we ﬁnd that deﬁning
h(t) as above withL = 93
100 gives the strongest bound onm. To do our analysis, we alter
Theorem 2.47 by using the equality
k(z,z ) =− 1
2π
∫ ∞
0
g′(t)
sinh(t
2
)dt
for the point pair invariant. In our case,g(t) has compact support in[−93
25, 93
25
], so the
trace formula is
∑
i
h(ρi) =
∫ 93
25
0
g′(t)
sinh(t
2
)dt + 24
( l1g(l1)
2 sinh(l1/2)
)
.
The right hand side of this equation can be evaluated explicitly using Mathematica. It
is equal to the rather complicated
F = 200
74805201
√
2 +√2
(
25
√
2 +
√
2
(
27900Li2
( 1
e93/50
)
− 55800Li2
(
− 1
e93/100
)
78
− 55800Li2
( 1
e93/100
)
+ 5000Li3
( 1
e93/25
)
− 45000Li3
( 1
e93/50
)
− 60000Li3
(
− 1
e93/100
)
+ 100000Li3
( 1
e93/100
)
− 105000ζ(3)
− 25947 log(e93/100− 1) + 25947 log(1 +e93/100) + 69192 tanh−1
( 1
e93/50
)
− 51894 tanh−1
( 1
e93/100
)
− 69192 coth−1(e93/100)− 34596 log
(
tanh
( 93
200
))
+34596 log
(
tanh
( 93
100
)))
+ 232500
√
2 +
√
2π2
+ 3217428(23/4) cosh−1
(
1 +
√
2
)
− 5189400(23/4) cosh−1
(
1 +
√
2
)2
+2790000 23/4 cosh−1
(
1 +
√
2
)3
− 500000(23/4) cosh−1
(
1 +
√
2
)4)
,
where
Lin(z) =
∞∑
k=1
zk
kn
is the polylogarithm function, and
ζ(s) =
∞∑
k=1
k−s
is the Riemann zeta function (forℜ(s)> 1).
The terms involving trigonometric functions, hyperbolic functions, or logs are ﬁne,
however we need to approximate the terms involving a power series in order to give an
upper bound forF. Let us start by analyzing the terms with a dilogarithm function
(Li2(z)). We may simplify the ﬁrst two negative terms using the following functional
equation for the dilogarithm,
Li2(z) +Li2(−z) = 1
2Li2(z2),
to get
−55800
(
Li2
(
− 1
e93/100
)
+Li2
( 1
e93/100
))
=−27900Li2
( 1
e93/50
)
,
which cancels with the dilogarithm term in the expression forF. Moving on to the
trilogarithm terms, we can use the similar formula,
Li3(z) +Li3(−z) = 1
4Li3(z2),
to simplify
−45000Li3
( 1
e93/50
)
− 60000Li3
(
− 1
e93/100
)
+ 100000Li3
( 1
e93/100
)
79
into
−60000Li3
( 1
e93/50
)
+ 160000Li3
( 1
e93/100
)
.
Our problem is now reduced to ﬁnding upper bounds for Li3
(
e−93
25
)
and Li3
(
e− 93
100
)
,
and lower bounds for Li3
(
e−93
50
)
andζ(3). For the upper bounds, note thate−93
25 and
e− 93
100 are both less than 1. The power series for the polylogarithm has a positive integer
in the denominator that is greater than or equal to 1, so
Li3
(
e−93
25
)
=
∞∑
k=1
(
e−93
25
)k
k3 <
∞∑
k=1
(
e−93
25
)k
.
The term on the right is a geometric series, minus the ﬁrst term, so the sum of the
geometric series gives us
Li3
(
e−93
25
)
< 1
1−e−93
25
− 1 = 1
e
93
25− 1
≈ 0.0248358.
The same trick with Li3
(
e− 93
100
)
does not give such a close bound, however we can make it
as strong as we like by choosing where we start approximating with the geometric series,
that is, we subtract the ﬁrstk + 1terms of the geometric series and add the ﬁrstk terms
of the trilogarithm series. Withk = 8, we get
Li3
(
e− 93
100
)
< 1
e93/100− 1− 511
512e186/25− 342
343e651/100− 215
216e279/50− 124
125e93/20
− 63
64e93/25− 26
27e279/100− 7
8e93/50
≈ 0.417148.
For our lower bounds, we can simply truncate the power series at a point where a
suitable degree of accuracy has been achieved. For Li3
(
e−93
50
)
, truncating after 5 terms
gives us
Li3
(
e−93
50
)
> 1
125e93/10 + 1
64e186/25 + 1
27e279/50 + 1
8e93/25 + 1
e93/50≈ 0.158852,
and forζ(3)summing the ﬁrst 30 terms yields
ζ(3)> 15180616603702475646118887931489459603
12634514775682409397575348713152000000≈ 1.20152.
Our precise upper bound forF is
˜F = 200
74805201
√
2 +√2
(
25
√
2 +
√
2
(
5000
( 1
e
93
25− 1
)
− 60000
( 1
125e93/10
+ 1
64e186/25 + 1
27e279/50 + 1
8e93/25 + 1
e93/50
)
+ 160000
( 1
e93/100− 1
80
− 511
512e186/25− 342
343e651/100− 215
216e279/50− 124
125e93/20− 63
64e93/25
− 26
27e279/100− 7
8e93/50
)
− 105000
(15180616603702475646118887931489459603
12634514775682409397575348713152000000
)
− 25947 log(e93/100− 1) + 25947 log(1 +e93/100) + 69192 tanh−1
( 1
e93/50
)
− 51894 tanh−1
( 1
e93/100
)
− 69192 coth−1(e93/100)− 34596 log
(
tanh
( 93
200
))
+34596 log
(
tanh
( 93
100
)))
+ 232500
√
2 +
√
2π2
+ 3217428(23/4) cosh−1
(
1 +
√
2
)
− 5189400(23/4) cosh−1
(
1 +
√
2
)2
+2790000 23/4 cosh−1
(
1 +
√
2
)3
− 500000(23/4) cosh−1
(
1 +
√
2
)4)
,
which is approximately equal to 1.60267. We have
h(t0) +mh(t1)<
∑
j
h(tj),
wherem is the dimension ofE1. We therefore have
h(t0) +mh(t1)<F < ˜F,
and a simple rearrangement gives
m<
˜F−h(t0)
h(t1) .
Sinceh(t) is decreasing on the interval[0, 93
25
], we can apply our bound on the ﬁrst
eigenvalue to state
h(t1)>h
(√
116469
28089 + 1/4
)
.
We conclude that
m<
˜F−h(i/2)
h
(√
116469
28089 + 1/4
)≈ 5.87519,
where
h(i/2) = 1600000000 sinh4( 93
200
)
74805201
and
h
(√
116469
28089 + 1/4
)
=
15585025600000000 sin4
(
93
√48643
3121
200
)
176999686686876249 .
We have shown thatm is less than 6, soχ8 can only appear once inE1. The dimension
ofE1 is 3.
81
3.4.1 Method for proving Conjecture 3.12
Consider the annulusΩin Figure 3.18 with Dirichlet boundary conditions. In particular,
we can takeΩ to be a subspace of a hyperbolic cylinder withα as its core geodesic.
Table C.2 shows that numerically,
λ1(Ω)≈ 5.35.
Regarding the fact that 5.35 is relatively much larger than the ﬁgure of 4.15 that we want
to bound it away from, the outlook for producing a rigorous bound seems good.
The method that we have in mind to prove Conjecture 3.12 is a generalization of the
maximum principle. In particular, we have the following:
Theorem 3.16[68, Theorem 10] Letu(x) be an eigenfunction of the Laplacian with
eigenvalueλ on a compact Riemannian manifold(M, g) with Lipschitz boundary∂M. If
there exists a functionw(x) that is strictly positive onM∪∂M, and
(−∆ +λ)u(x)≤ 0 in M,
thenu(x)/w(x) cannot attain a non-negative maximum inM unless it is a constant. If
u(x)/w(x) attains its non-negative maximum at a pointp∈∂M that lies on the boundary
of a ball inM and ifu/w is not constant, then
∂
∂ν
(u
w
)
> 0 at p,
where ∂
∂ν is any outward directional derivative.
Corollary 3.17Let (M, g) be as above, and assume∂M⁄=∅. Assume there exists a
strictly positive functionw∈C∞(M) with
(−∆ +λ)w≤ 0 inM.
Then there is no Dirichlet eigenvalue in[0, λ] inM.
Corollary 3.18Let (M, g) be as above, and assume∂M⁄=∅. Assume there exists a
functionw∈ C∞(M) that is positive on the interior ofM and non-negative onM,
satisfying
(−∆ +λ)w≤ 0 inM.
Then there is no Dirichlet eigenvalue in[0, λ) inM.
Proof: [Sketch of proof of Corollary 3.18] If we have a functionwthat is strictly positive
on the interior ofM, then we can makeM a tiny bit smaller to obtain a regionMδ⊂M.
82
0.5 1.0 1.5
1.0
1.4
1.6
1.8
2.0
2.2
Figure 3.19: Comparing the nodal line of the test functionw, as a function oft (blue curve), to the
boundary ofΩ (red, lilac, green curves)
Now onMδ we can construct a functionwδ that is equal tow on Mδ, and cut it oﬀ
smoothly in the regionM\Mδ by multiplying by a cut oﬀ functionχ∈C∞
0 (M), such
thatwδ is zero on∂M. OnMδ, wδ is strictly positive and sub-harmonic, so there is no
Dirichlet eigenvalue in[0,λ] onMδ by Corollary 3.17. Then we can create a sequence of
domainsMδ getting progressively closer toM such that the ﬁrst eigenvalues ofMδ will
converge to the ﬁrst eigenvalue ofM asδ goes to zero. In particular, we use the sequence
of corresponding functionswδχ in the Rayleigh quotient to bound the ﬁrst Dirichlet
eigenvalue ofM from above (recall that by domain monotonicity,λ1(M)≤λ1(Mδ)). The
gradient ofwδχ only diﬀers from that ofw in an increasingly smaller area, and we can
make its contribution to the Rayleigh quotient arbitrarily small (that is, such that there
is no Dirichlet eigenvalue onM in the interval[0, λ+ϵ] forϵ> 0). We obtain that there
is no eigenvalue in[0,λ). □
Now for our annulusΩ, numerical experiments show that if we take a certain com-
bination of the ﬁrst three odd eigenfunctions of the cylinder with core geodesicα (see
Section 2.3.2) and eigenvalueλ = 5, we can ﬁnd a test function that satisﬁes the condi-
tions of Corollary 3.18 onΩ. Note that alongα, such functions are zero by construction
but the test function we create will be positive everywhere else onΩ. Thus we show that
there is no Dirichlet eigenvalue in the interval[0, 5). In particular, the eigenfunctions are
φ0(ρ) = sinh(ρ)2F1
(
3
4 +i
√
λ− 1/4
2 , 3
4 +i
√
λ− 1/4
2 ; 3
2;−sinh2(ρ)
)
,
83
φ1(ρ) = sinh(ρ)(cosh(ρ))
2πi
l 2F1
(
3
4 +i
√
λ− 1/4
2 +πi
l , 3
4 +i
√
λ− 1/4
2 +πi
l ; 3
2;−sinh2(ρ)
)
,
φ2(ρ) = sinh(ρ)(cosh(ρ))
4πi
l 2F1
(
3
4 +i
√
λ− 1/4
2 + 2πi
l , 3
4 +i
√
λ− 1/4
2 + 2πi
l ; 3
2;−sinh2(ρ)
)
,
where
l =l(α) = 2 arccosh
(
csc(π
8
)
2
)
.
The combination that we take is
w(ρ, t) =φ0(ρ)− 0.038 sin
(2πt
l −π
2
)
φ1(ρ)− 0.0002 cos
(4πt
l
)
φ2.
This function is sub-harmonic overΩ; in particular
(−∆ +λ)w(ρ, t) = 0
over Ω, sinceφ0, φ1, andφ2 have been constructed as eigenfunctions of the Laplacian
(with respect to the cylinder metric described in Section 2.3.2). It is not immediately
obvious thatwis strictly positive overΩ, but we can plot the nodal line ofwas a function
oft to see at which values ofρ the function is zero, and then compare it to the boundary
of Ω. This comparison is shown in Figure 3.19. The blue curve shows the values ofρ
wherew changes sign ast runs over the length of the core geodesic. The green, red and
lilac curves show the boundary ofΩ in Fermi coordinates. Close inspection shows that
the nodal line is always outside the boundary ofΩ. The code that produced this plot is
given in Appendix F.
Remark 3.19The proof of Conjecture 3.12 now amounts to showing that the test func-
tionw(ρ, t) is positive inΩ. One could perhaps do this by approximating the hyperge-
ometric functions by polynomials inρ, which are easier to analyze. Here, care must be
taken to ensure that the ﬁrst and second derivatives are approximated well enough such
that the approximating function is still sub-harmonic overΩ. One can see from Fig-
ure 3.19 that the test functionw is only just positive insideΩ, so ﬁnding a suﬃciently
accurate polynomial approximant could prove diﬃcult. On the other hand, we have room
to manoeuver withλ; the current value of 5 is still “far away” from the value of 4.15 that
would be the lowest suﬃcient value to prove Conjecture 3.12. Changingλ to a slightly
smaller value may give more freedom to ﬁnd a polynomial approximant and show that it
satisﬁes the hypothesis of Corollary 3.17.
Remark 3.20At one point, we thought it would be possible to prove Conjecture 3.12
using a Faber-Krahn style inequality for half cylinders. This would amount to proving
84
that the ﬁrst Dirichlet eigenvalue ofΩ is greater than the ﬁrst Dirichlet eigenvalue of the
symmetric half cylinder withαas its core geodesic, such that its area is equal to that ofΩ.
Proving this condition seems to be less attainable than the more direct approach described
above, however, we include the alternative method in Appendix G.
3.5 Second eigenspace of Bolza surface
Having calculated lower bounds for the eigenvalues of each irreducible representation, we
have done the bulk of the work to make a statement about the second eigenspace,E2.
We begin with the following
Lemma 3.21The dimension ofE2 is a multiple of 4.
Proof: Recall our upper bound onλ2 in Section 3.3. The only irreducible representations
that can appear in this eigenspace areχ8 and the four dimensional ones. To rule outχ8,
wewillreturntoProposition3.14. Theeigenfunctioncorrespondingtothesecondpositive
eigenvalue of the domain in Figure 3.13 has 2 nodal domains. So we have two Dirichlet
boundary problems each with the same eigenvalue. The entire region has area2π, so
unless the nodal line splits it equally, one of the nodal domains will have area less than
π. Therefore, we can takeπ as an upper bound on the area of at least one of the nodal
domains, and use the Faber-Krahn inequality so conclude that the eigenvalue of the nodal
domain, and therefore the whole region, is greater thanνπ and therefore greater than 6.
This means that only the four dimensional irreducible representations can appear inE2.
□
Theorem 3.22The dimension ofE2(B) is 4.
Proof: By Lemma 3.21, we already know that the multiplicity ofλ2 is a multiple of 4.
To prove that it is exactly four, we will prove that the multiplicity is less than 8. We will
use Selberg’s trace formula in the same way as for the multiplicity bound above, using
our upper bounds on the ﬁrst and second positive eigenvalues. Again, we use the test
function
h(t) =
(sin(tL)
tL
)4
,
so that the Fourier transform ofh(t) is supported on[−4L,4L]. We choose4L to be less
than the length of the shortest closed geodesic of the Bolza surface to avoid contribution
from the length spectrum. Recall that the shortest closed geodesic has length
2 arccosh
(
1 +
√
2
)
≈ 3.057141839.
85
Choosing
L = 3/4,
Selberg’s trace formula becomes
∑
j
h(tj) = 2
∫ ∞
0
h(t) tanh(πt)tdt.
Figure 3.20:h(t) on [0, 4]
1 2 3 4
0.2
0.4
0.6
0.8
1.0
Now we use the straightforward inequality
tanh(x)< 1
to state ∑
j
h(tj)< 2
∫ ∞
0
h(t)tdt.
The integral on the right hand side can be explicitly calculated; forL = 3/4, we have
2
∫ ∞
0
h(t)tdt = 32 log(2)
9 .
On the other hand, by Theorem 3.9 we have
h(t0) + 3h(t1) +mh(t2)<
∑
j
h(tj),
wherem is the dimension ofE2. We therefore have
h(t0) + 3h(t1) +mh(t2)< 32 log(2)
9 ,
86
and a simple rearrangement gives
m<
32 log(2)
9 −h(t0)− 3h(t1)
h(t2).
Sinceh(t) is decreasing on the interval[0, 4L], we can apply our bounds on the ﬁrst two
eigenvalues to state
h(t1)>h
(√
116469
28089 + 1/4
)
and
h(t2)>h
(√
1408244
252552 + 1/4
)
.
We conclude that
m<
32 log(2)
9 −h(i/2)− 3h
(√
116469
28089 + 1/4
)
h
(√
1408244
252552 + 1/4
)
=
4070947840281 csc4
(√2017659
10523
8
)


32 log(2)
9 −
39897665536 sin4
(
3
√
48643
3121
8
)
63885819123 − 4096
81 sinh4(3
8
)


453564534784
≈ 7.1091.
□
87
Chapter 4
The Klein Quartic
4.1 Systole of the Klein quartic
The systole of the Klein quartic is described in Klein’s original paper [48] on the prop-
erties of the quartic curve, and is expounded upon in [44,80]. We will useK to denote
the surface. Consider a tessellation ofK by heptagons (these can be barycentrically sub-
divided into 14(2, 3, 7) triangles, see Figure 4.2). Starting with the central heptagon,
join the midpoints of two adjoining edges with a geodesic. Extend this geodesic in both
directions until it meets the boundary of the fundamental 14-gon. On its way, it passes
through the midpoints of a further 3 and a half heptagon midpoints in either direction; a
total of 8 midpoints. For this reason, Karcher and Weber coin it an “eight step geodesic”.
Note that the two boundary edges that it meets are actually the same edge once the side
associations are made; that is, we have a simple closed geodesic. In fact, the length of
this curve turns out to be the systole of the surface [44]. An order 7 rotation around the
centre of the 14-gon maps this geodesic onto six other copies.
We obtain two more geodesics of length equal to the systole by creating curves that
pass through adjoining edges of heptagons at varying distances from the centre; these
are shown in Figure 4.2. There are 7 heptagons surrounding the central heptagon. The
magenta curve passes through two edges of one of these. This time, when it reaches the
boundary, it does not form a closed curve since the two sides are not associated with
one another. We make the relevant side association and continue the geodesic from here,
following the pattern of passing through midpoints of heptagon edges, until the geodesic
is closed. Since we could have chosen any of the 7 heptagons, we get a further 7 closed
geodesics. The orange (and green) curves pass through two adjoining edges of a heptagon
in the second closest group from the centre. Again, there will be 7 of these. They follow
the same pattern through 8 heptagon edge midpoints, thus having the same length. The
multiplicity of the systole is 21.
88
Figure 4.1: Calculating1
8 of the systole
bc
a
We calculate the systole using basic hyperbolic trigonometry to give a closed formula
foroneofthe“steps”, andthenmultiplythisby8. SimilartotheformulaeinTheorem2.30
for right-angled hyperbolic triangles, we have
sinh(a) = sin(α) sinh(c) (4.1)
for a right-angled hyperbolic triangle wherec is the length of the hypotenuse andα is
the angle opposite the side of lengtha [13]. Also recall from Section 2.2.3 that the side
of medium length in a(2, 3, 7) triangle has length
arccosh
(1
2 csc
(π
7
))
.
Consider the blue geodesic in Figure 4.2. We can zoom in on its centre “step” to get
the triangle shown in Figure 4.1. Since step is symmetric with respect tob, we can divide
the larger triangle into two smaller right-angled triangles. Note that the medium side of
a (2, 3, 7) triangle is the hypotenuse of the right-angled triangle in Figure 4.1. Leta be
half the length of the blue line, that is, the shortest side of the triangle on the left. We
calculate the length ofa using Equation (4.1), whereα is the angle oppositea and is
equal toπ
7. We have
sinh (a) = sin
(π
7
)
sinh
(
arccosh
(1
2 csc
(π
7
)))
= sin
(π
7
)√(
−1 + 1
2 csc
(π
7
))(
1 + 1
2 csc
(π
7
))
= sin
(π
7
)(1
2
√
csc2
(π
7
)
− 4
)
.
Thus
l(a) = arcsinh
((1
2
√
csc2
(π
7
)
− 4
)
sin
(π
7
))
.
This is half of the length of one step of the geodesic, and there are eight steps altogether,
therefore
s(K) = 16 arcsinh
((1
2
√
csc2
(π
7
)
− 4
)
sin
(π
7
))
≈ 3.93594624883.
89
Remark 4.1Note that there is more than one way to calculate a closed formula for the
systole; [72] came up with
8 arccosh
(3
2− 2 sin2
(π
7
))
≈ 3.93594624883.
Figure 4.2: Geodesics of length equal to the systole
Remark 4.2Numerical calculations of the other values in the geodesic length spectrum of
the Klein quartic are given in the doctoral thesis of Vogeler [81], along with multiplicities.
Vogeler also gives similar length spectra calculations for many other Hurwitz surfaces,
including the Macbeath surface mentioned in the introduction to this work.
4.2 Fenchel-Nielsen parameters of the Klein quartic
To discuss Fenchel-Nielsen parameters, we ﬁrst need to introduce the notion of a pants
decomposition. A pair of pants (sometimes called a Y-piece) is the simplest hyperbolic
surface; topologically, itisaspherewiththreedisksremoved. AcompactRiemannsurface
of genusg≥ 2 can be decomposed into pairs of pants by cutting along3g− 3 simple,
closed, non-intersecting geodesics. These geodesics form the boundaries of each pair of
pants. A pair of pants has a speciﬁc geometry; we can form them by gluing together two
right-angled (hyperbolic) hexagons, where alternate sides of each hexagon will be equal
to half the length of one of the boundary geodesics of the pair of pants. The lengths of
the sides in between these curves are ﬁxed, since a geodesic joining two other geodesics
90
perpendicularly is unique. This construction is shown in Figure 4.3; the bold curves on
the pair of pants (on the left) are the boundary curvesγi, i∈{ 1, 2, 3}, with length
li =l(γi). The pants are obtained by gluing two copies of the hexagon on the right along
the dashed lines. The bold curves in the hexagon have lengthli
2. A complete derivation of
the geometry of hyperbolic hexagons, staring from a hyperbolic triangle, is given in [13].
This is also an excellent reference for the ﬁne details of pants decompositions.
Figure 4.3: A hyperbolic pair of pants can be split into two identical hexagons
The Teichmüller spaceTg is the space of all Riemann surfaces of genusg up to marking
equivalence. We will not go into depth here, but again, [13] provides a thorough intro-
duction to this theory. The Fenchel-Nielsen parameters are a set of6g− 6 coordinates
that completely classify a surface in Teichmüller space. Knowing the lengths of these
geodesics provides half of these parameters. Additionally, for each geodesic we need to
know whether it is twisted at all before being glued back together. This means that we
also have3g− 3 twist parameters. The Fenchel-Nielsen parameters (or coordinates) are
given as
{l1, t1,..., l 3g−3, t3g−3},
whereli andti,i∈{ 1,..., 3g− 3}, respectively denote the length and twist parameters
of a geodesicγi.
To obtain a decomposition of the Klein quartic into four pairs of pants, simply take
six non-intersecting curves of length equal to the systole, as is shown in Figure 4.2. This
decomposition is described in [44], along with a decomposition into hexagons that are
not right-angled. The latter decomposition is interesting in that all the twist parameters
are zero. An inspection of the number of regular heptagons enclosed by the curves in
Figure 4.2 conﬁrms that each pair of pants contains six heptagons. A heptagon is made
up of 14 triangles of areaπ
42. Therefore each pair of pants has area
6(14)
(π
42
)
= 2π.
91
Figure 4.4: Calculating the twist parametert1 ofγ1
t1
γ1
γ2
γ3
γ3
γ4
This is the correct area for a pair of pants having constant negative curvature.
We now calculate the six twist parameters. We start with the ‘central’ pair of pants,
bounded by the geodesicsγ1, γ2, andγ3 in Figure 4.4. We draw the unique geodesic
segment that meetsγ1 andγ2 perpendicularly. To calculate the twist parametert1 ofγ1,
consider the other pair of pants for whichγ1 is a boundary (the other two boundaries are
γ4 andγ5). We draw the unique geodesic segment that meetsγ1 andγ4 perpendicularly.
When we twist alongγ1, we want the two perpendicular sections (dashed lines in the
ﬁgure) to match up. The twist parameter forγ1 is the distance along theγ1 between the
points where it intersects the perpendicular geodesics. Simply by examining Figure 4.2,
we see that this is1
8 of the systole. Therefore
t1 = arccosh
(3
2− 2 sin2
(π
7
))
≈ 0.4919932811037915.
We can play a similar game with the other boundary curves to conclude that the twist
parameters for each curve will be the same, that is,1
8 of the systole. Therefore, we have
a complete set of Fenchel-Nielsen coordinates for the Klein quartic:
{
s(K), s(K)
8 , s(K), s(K)
8 , s(K), s(K)
8 , s(K), s(K)
8 , s(K), s(K)
8 , s(K), s(K)
8
}
,
wheres(K) is the systole ofK.
92
4.3 Spectral theory of the Klein quartic
The symmetry group of the Klein quartic comes from the 336(2, 3, 7) triangles that
tessellate the surface. We saw the presentation of such a group in the hyperbolic ge-
ometry section; since there are side associations on our surface, we have the following
presentation:
⟨a,b,c|a2 =b2 =c2 = (ab)2 = (ac)7 = (bc)3 = (abc)8 =e⟩,
where the lengths ofa, b andc are given in Section 2.2. As with the Bolza surface, we
can use this presentation in GAP to get information about the structure of the group,
and more importantly, its irreducible representations (see Appendix B). We see that the
isometry group (including reﬂections) of the Klein quartic has two one dimensional, three
six dimensional, two seven dimensional, and two eight dimensional irreducible represen-
tations.
i
γ1
γ2
Figure 4.5: The domain of integration inH
As with the Bolza surface, we can exploit the symmetry group and its representation
theory to prove results about the spectrum ofK, which is given numerically in Table D.1.
To begin with, we need an upper bound on the ﬁrst eigenvalue of the surface; in Table D.1
we see that this is roughly 2.67. Following the strategy of Section 3.3, we construct a test
function that is close to the ﬁrst eigenfunction. This can then be used in the Rayleigh
quotient. We work once again in the upper half plane model, although this time we
use a slightly diﬀerent triangle. Joining the vertices of the fundamental 14-gon with
(Euclidean) straight lines tessellates the Klein quartic with 14(7, 7, 7) triangles of area
4π
7 . We take one of these and map it toHusing the Cayley transform on its vertices. We
then use the fact that it has an additional line of symmetry with respect to theℑ axis,
and work with half the triangle, which has area2π
7 . This triangle, denotedΩK, is shown
93
in Figure 4.5. The boundary curves are given by
γ1(x) =
√
r2−x2
and
γ2(x) =
√
csc2
(π
14
)
−
(
x + cot
(π
14
))2
,
where
r =
vuuuuu√
−(cos(π
14
) − 1) exp
(
4
(
cosh−1
(
2 cos( π
7 )√3
)
+ cosh−1
(
cot( π
7 )√3
)
+ cosh−1(1
2 csc(π
7
))))
+ 1 + cos(π
14
)
(1 + cos(π
14
)) exp
(
4
(
cosh−1
(
2 cos( π
7 )√3
)
+ cosh−1
(
cot( π
7 )√3
)
+ cosh−1(1
2 csc(π
7
))))
+ 1 − cos(π
14
) .
The test function we use is
φ1(x, y) =y−
√
r2−x2.
Note thatφ1(x, y) = 0 onγ1(x). Our aim is to bound itsL2 norm onΩK from below.
We start by integrating it explicitly with respect toy, to deﬁne a functionu(x) as
u(x) =
∫ γ2(x)
γ1(x)
(φ1(x, y)
y
)2
dy
= 2
√
r2−x2 log


√r2−x2
√
csc2(π
14
)−(x + cot(π
14
))2


− r2−x2
√
csc2(π
14
)−(x + cot(π
14
))2
+
√
csc2
(π
14
)
−
(
x + cot
(π
14
))2
.
We now use Simpson’s rule in exactly the same way as with the Bolza surface, with a
maximum error of10−6. To approximate∫ p
0
u(x)dx,
where
p =
sin(π
14
)(
exp
(
4
(
cosh−1
(
2 cos( π
7 )√3
)
+ cosh−1
(
cot( π
7 )√3
)
+ cosh−1(1
2 csc(π
7
))))
− 1
)
(1 + cos(π
14
)) exp
(
4
(
cosh−1
(
2 cos( π
7 )√3
)
+ cosh−1
(
cot( π
7 )√3
)
+ cosh−1(1
2 csc(π
7
))))
+ 1 − cos(π
14
),
with this degree of accuracy, we need to taken = 1648. The following input in Mathe-
matica [37] generatesS1648.
\[Phi ][x_, y_] = y − Sqrt [ r^2− x^2];
u[x_] = (Sqrt [Csc[ Pi/14]^2 − (x + Cot[ Pi/14])^2] −
2 Sqrt [ r^2− x^2] Log[
Sqrt [Csc[ Pi/14]^2 − (x + Cot[ Pi/14])^2]] − (r^2 − x^2)/
Sqrt [Csc[ Pi/14]^2 − (x + Cot[ Pi/14])^2]) − (Sqrt [ r^2− x^2] −
2 Sqrt [ r^2− x^2] Log[ Sqrt [ r^2 − x^2]] − (r^2 − x^2)/
Sqrt [ r^2− x^2]);
U=((p)/(3 1648)) Total [{u[0] , u[p] ,
Total [ Table[2 u[ i ] , {i , 2 (p)/1648, 1646 (p)/1648, (p)/824}]] ,
Total [ Table[4 u[ i ] , {i , (p)/1648, 1647 (p)/1648, (p)/824}]]}]
94
As before, the symbolic output is too long to display here, but it gives us the bound
‖φ1‖2> 29997
1000000.
Next, we bound‖∇φ1‖2 from above. We integrate the scalar product of
∇φ1 =
{ x√r2−x2, 1
}
with itself with respect toy to get
gu(x) =
∫ γ2
γ1
⟨∇φ1,∇φ1⟩dy
=
( x2
r2−x2 + 1
)(√
csc2
(π
14
)
−
(
x + cot
(π
14
))2
−
√
r2−x2
)
.
We approximate the integral ofgu(x) using Simpson’s rule withn = 2522, that is,
gu[x_] = Integrate [
Grad[\[ Phi ][ x, y] , {x, y}].Grad[\[ Phi ][ x, y] , {x, y}] , {y,
Sqrt [ r^2− x^2] , Sqrt [Csc[ Pi/14]^2 − (x + Cot[ Pi /14])^2]}];
gU = ((p)/(3 2252)) Total [{gu[0] , gu[p] ,
Total [ Table [
2 gu[ i ] , {i , 2 (p)/2252, 2250 (p)/2252, (xval )/1126}]] ,
Total [ Table[4 gu[ i ] , {i , (p)/2252, 2251 (p)/2252, (p)/1126}]]}]
to get the following upper bound:
‖∇φ1‖2< 84077
1000000.
Finally, we can take the quotient of our bounds to get an upper bound on the ﬁrst positive
eigenvalue of the Klein quartic, namely
λ1< 84077
29997≈ 2.8027.
Comparedto the numerical value of 2.76, we see that this is a reasonably good bound.
We get get one result quite quickly:
Lemma 4.3E1 of the Klein quartic is not one dimensional.
Proof: We start by ruling out the non-trivial one dimensional irreducible representation.
We see that reﬂection in each side of a(2, 3, 7)triangle changes the sign of a vector as it is
moved around the surface by this representation. Therefore, we have Dirichlet boundary
conditions on a(2, 3, 7) triangle. Its ﬁrst eigenvalue is greater than or equal to the ﬁrst
eigenvalue of a hyperbolic disk of areaπ
42 by the Faber-Krahn inequality. That is,
λ1(ρ2)≥νπ
42 >νπ> 6,
meaningρ2 does not appear in the ﬁrst eigenspace.
95
Now we consider the trivial representation, and use an argument identical to that in
Lemma 3.15, using Proposition 3.14 on nodal lines and domain monotonicity. We now
have a heptagonΩH of areaπ
3, by the Faber-Krahn inequality
λ1(ρ1)≥λ1(ΩH)≥νπ
3 >νπ> 6.
Therefore, the trivial representation does not appear in the ﬁrst eigenspace either.□
WecanalsouseSelberg’straceformulatoboundthemultiplicityoftheﬁrsteigenvalue,
like we did in Sections 3.4 and 3.5.
Lemma 4.4The multiplicity ofλ1 is less than or equal to 10.
Proof: As before, we use the test function
h(t) =
(sin(tL)
tL
)4
,
so that the Fourier transform ofh(t) is supported on[−4L,4L]. We choose4Lto be less
than the length ofs(K) to avoid contribution from the length spectrum. Choosing
L = 87
100,
Selberg’s trace formula becomes
∑
j
h(tj) = 4
∫ ∞
0
h(t) tanh(πt)tdt.
Note that the coeﬃcient of the integral is a 4 now rather than a 2, as it was in the case
of the Bolza surface. This is because the area of the Klein quartic is twice the area of the
Bolza surface. Again we use
tanh(x)< 1
to state ∑
j
h(tj)< 4
∫ ∞
0
h(t)tdt.
The integral on the right hand side can be explicitly calculated; forL = 87
100, we have
4
∫ ∞
0
h(t)tdt = 40000 log(2)
7569 .
We have
h(t0) +mh(t1)< 40000 log(2)
7569 .
Rearranging this gives
m<
40000 log(2)
7569 −h(t0)
h(t1) .
96
Sinceh(t) is decreasing on the interval[0, 4L], we can apply our bound on the ﬁrst
eigenvalue to state
h(t1)>h
(√
84077
29997 + 1/4
)
.
We conclude that
m<
40000 log(2)
7569 −h(i/2)
h
(√
84077
29997 + 1/4
)
=
66361650332217601 csc4
(
29
√306311
3333
200
)(
40000 log(2)
7569 −
1600000000 sinh4( 87
200)
57289761
)
17774222400000000
≈ 10.0855.
□
We can combine the multiplicity bound of Lemma 4.4 with Lemma 4.3 to state that
any irreducible representation of Isom(K) that appears inE1 only does so once. This
leads us to the following obvious observation:
Corollary 4.5The eigenspace corresponding to the ﬁrst positive eigenvalue of the Klein
quartic is either 6, 7, or 8 dimensional.
Remark 4.6The inferred multiplicities from the numerical calculations of eigenvalues,
shown in Table D.1, support this corollary. In particular, they suggest that the ﬁrst
eigenspace is 8 dimensional.
97
Chapter 5
Concluding Remarks
The spectral theory of Riemann surfaces has been a popular and fruitful ﬁeld of study for
manyyears, andisstillanactiveareaofresearch. Themainbodyofthisworkdocumented
the investigation of the Laplace spectra of two speciﬁc surfaces: the Bolza surface and
the Klein quartic. These are of particular interest because they have maximal symmetry
among all compact Riemann surfaces with constant negative curvature, of genus 2 and 3
respectively. In particular, the Klein quartic is a Hurwitz surface.
In Chapter 3, we used the representation theory of its automorphism group to show
that the ﬁrst non-trivial Laplace eigenspace of the Bolza surface has dimension 3, and
that this corresponds to the irreducible representation that we denotedχ8. This proof
relies on a certain conjecture, which is supported by numerical evidence. We gave a
potentially eﬀective strategy for proving this conjecture, and went on to show that the
second eigenspace has dimension 4. Unfortunately, we were not able to state the exact
irreducible representation corresponding to this. We suspect that the reﬁned version of
the Selberg trace formula (Theorem 2.49) could be used to pinpoint the representation
we are looking for.
Our work on the Bolza surface built on work done by Jenni in the 1980s, and our
investigation was part of the initial step in addressing a wider open problem related to
the Bolza surface, namely
Conjecture 5.1Among all compact Riemann surfaces of genus 2 with constant nega-
tive curvature, the Bolza surface globally maximizes the ﬁrst positive eigenvalue in the
spectrum of the Laplace-Beltrami operator.
It is thought that by analyzing the nodal lines of eigenfunctions relating toχ8 under
perturbations in Teichmüller space, one would be able to show that the Bolza surface is a
local maximum forλ1. One would then be able to use this as a building block for proving
that it is a global maximum.
98
In Chapter 4, we aimed to analyze the Klein quartic in much the same way as the Bolza
surface, to prove results about the low lying eigenspaces. Analysis of the Klein quartic
in this manner proved to be more complicated than the work of Chapter 3, although we
proved an initial result that the dimension of the ﬁrst eigenspace is not one dimensional.
Combined with the bound given on the multiplicity of the ﬁrst eigenvalue using Selberg’s
trace formula, and the dimensions of the irreducible representation of the automorphism
group, we can say the the eigenspace is either 6, 7, or 8 dimensional. Also in this section,
we investigated the systole and a pants decomposition of the Klein quartic, and gave
Fenchel-Nielsen coordinates for the surface in Teichmüller space. As in the case of the
Bolza surface, proving a result on the ﬁrst eigenspace would have been an early step
towards proving the following
Conjecture 5.2Among all compact Riemann surfaces of genus 3 with constant nega-
tive curvature, the Klein quartic globally maximizes the ﬁrst positive eigenvalue in the
spectrum of the Laplace-Beltrami operator.
In Appendix D we have carried out numerical experiments to support this conjecture.
WecalculatedthespectrumofthesurfacedenotedM3in[72], whichmaximizesthesystole
length for genus 3 surfaces, and found it to have a smaller value ofλ1 than the Klein
quartic. Likewise, we investigated the Fermat quartic, and found that its ﬁrst positive
eigenvalue is smaller than that of the Klein quartic. Of course, the natural temptation
in light of the previous two conjectures is to postulate
Conjecture 5.3Forn≥ 2, among all compact Riemann surfaces of genusn with con-
stant negative curvature, the surface with the largest automorphism group globally maxi-
mizes the ﬁrst positive eigenvalue in the spectrum of the Laplace-Beltrami operator.
However, this assumes that there is a unique surface that maximizes the automorphism
group. If we restrict our attention to Hurwitz surfaces, we can conjecture that the
Macbeath surface in genus 7 has this maximization property. Unfortunately, in the next
genus that admits a Hurwitz surface, that is, genus 14, there is a triple of non-isomorphic
Hurwitz surfaces (see, for example, [61]). It is unclear which of these would be the best
candidate for eigenvalue maximization, but it seems reasonable to guess that one of them
is.
Alongside the surface M3, other surfaces diﬀerent to the focal two have been touched
upon in this thesis. The examples in genus 2 have simpler automorphism groups than
the Bolza surface, so theoretically, results about their eigenspaces could be gained with-
out as much work. In genus 3, the Fermat quartic and M3 surface again have smaller
automorphism groups than that of the Klein quartic (although they are comparable to,
99
if not larger than, that of the Bolza surface) and could be another avenue of study to add
to the collective knowledge of these surfaces.
Whilst pants decomposition are known for the Bolza surface and Klein quartic, we
do not have explicit pants decompositions for the other surfaces. Again, knowledge of
these, and the corresponding Fenchel-Nielsen parameters, would be helpful in carrying
out accurate computations of eigenvalues, improving on the rudimentary ﬁnite element
calculations given in the appendices.
100
Appendix A
GAP Code for Bolza Surface
The following output gives details of the isometry group of the Bolza surface, computed
by the computer algebra package GAP [26]. We ﬁrst deﬁne the group as a free group on
the 4 generators introduced in Section 3.1 with the relevant relations. We conﬁrm that
the order of this group is 96, and the “StructureDescription” command tells us that it is
isomorphic toGL2(Z3) ⋊ Z2.
Representatives of each conjugacy class ofIsom(B) are given by the command “Con-
jugacyClasses”. Each row of the character table tell us the value of one of the characters
on each of the 13 conjugacy classes of the group, where the conjugacy classes are in the
same order as the output of “ConjugacyClasses”. The data at the top of the character
table concerns the various “power maps” of the character table, and is irrelevant to this
work. The interested reader can learn how to interpret this data by consulting the GAP
manual. To interpret the character values on the diﬀerent conjugacy classes, one must
also be aware of the following notation used by GAP:
E(x) :=e
2πi
x .
The “IrreducibleAﬀordingRepresentation”s below the ﬁrst set of irreducible represen-
tations give a simpler set of representation matrices that are easier to work with, but
correspond to the same character table. One may see more easily which of these corre-
spond to rotations, and so on. Unfortunately it was not possible to calculate these for
the four dimensional representations, but we make use of them for our analysis of the 2
and 3 dimensional representations in Section 3.4.
gap> f:=FreeGroup("r" ,"s" ,"t" ,"u");
<free group on the generators [ r , s , t , u ]>
gap> g:=f /[ f .1^8 , f .2^2 , f .3^2 , f .4^3 , f .1∗f .2∗f .1∗f .2 , f .2∗f .3∗f .2∗f .3 , f .1∗f .3∗f .1^3∗f .3 ,
f .1^7∗f .4^2∗f .1^7∗f .4^2 , f .4^2∗f .1∗f .4^2∗f .3∗f .2 , f .4∗f .2∗f .4∗f .2 ,
f .4∗f .3∗f .4^2∗f .2∗f .1^7];
<fp group on the generators [ r , s , t , u ]>
gap> Order(g);
101
96
gap> ConjugacyClasses(g);
[ <identity ...>^G, r ^2 ∗ t ^G, s ^G, u^G, r ^3 ∗ s ∗ t ^G, r ^4^G,
r ^2∗ s ∗ t ^G, r ^2 ∗ t ∗u^G, r ∗ s ^G, r ^5 ∗ t ^G, r ∗ s ∗ t ∗u^G,
r ^3^G, r ^7 ∗ t ∗u∗ r ^G ]
gap> RequirePackage("repsn");
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
Repsn f o r Constructing Representations of Finite Groups
Version 3.0.2
Written by
Vahid Dabbaghian
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
true
gap> StructureDescription (g);
"GL(2 ,3):C2"
gap> Display(CharacterTable(g));
CT1
2 5 4 3 2 4 5 3 2 4 3 2 3 2
3 1 1 . 1 . 1 . 1 . . 1 . 1
1a 4a 2a 3a 4b 2b 2c 12a 2d 8a 6a 8b 12b
2P 1a 2b 1a 3a 2b 1a 1a 6a 1a 4b 3a 4b 6a
3P 1a 4a 2a 1a 4b 2b 2c 4a 2d 8a 2b 8b 4a
5P 1a 4a 2a 3a 4b 2b 2c 12b 2d 8a 6a 8b 12a
7P 1a 4a 2a 3a 4b 2b 2c 12b 2d 8a 6a 8b 12a
11P 1a 4a 2a 3a 4b 2b 2c 12a 2d 8a 6a 8b 12b
X.1 1 1 1 1 1 1 1 1 1 1 1 1 1
X.2 1 −1−1 1 1 1 1 −1−1−1 1 1 −1
X.3 1 −1 1 1 1 1 −1 −1−1 1 1 −1 −1
X.4 1 1 −1 1 1 1 −1 1 1 −1 1 −1 1
X.5 2 −2 . −1 2 2 . 1 −2 . −1 . 1
X.6 2 2 . −1 2 2 . −1 2 . −1 . −1
X.7 3 −3−1 . −1 3 1 . 1 1 . −1 .
X.8 3 −3 1 . −1 3 −1 . 1 −1 . 1 .
X.9 3 3 −1 . −1 3 −1 . −1 1 . 1 .
X.10 3 3 1 . −1 3 1 . −1−1 . −1 .
X.11 4 . . −2 . −4 . . . . 2 . .
X.12 4 . . 1 . −4 . A . . −1 . −A
X.13 4 . . 1 . −4 . −A . . −1 . A
A =−E(12)^7+E(12)^11
= Sqrt (3) = r3
gap> IrreducibleRepresentations (g);
[ [ r , s , t , u ] −> [ [ [ 1 ] ] , [ [ 1 ] ] , [ [ 1 ] ] , [ [ 1 ] ] ] ,
[ r , s , t , u ] −> [ [ [ 1 ] ] , [ [ −1 ] ] , [ [ −1 ] ] , [ [ 1 ] ] ] ,
[ r , s , t , u ] −> [ [ [ −1 ] ] , [ [ 1 ] ] , [ [ −1 ] ] , [ [ 1 ] ] ] ,
[ r , s , t , u ] −> [ [ [ −1 ] ] , [ [ −1 ] ] , [ [ 1 ] ] , [ [ 1 ] ] ] ,
[ r , s , t , u ] −> [ [ [ 0, 1 ] , [ 1, 0 ] ] , [ [ 0, −1 ] , [ −1, 0 ] ] ,
[ [ −1, 0 ] , [ 0, −1 ] ] , [ [ 0, −1 ] , [ 1, −1 ] ] ] ,
[ r , s , t , u ] −> [ [ [ 1, 0 ] , [ −1, −1 ] ] , [ [ 1, 0 ] , [ −1, −1 ] ] ,
[ [ 1, 0 ] , [ 0, 1 ] ] , [ [ −1, −1 ] , [ 1, 0 ] ] ] ,
102
[ r , s , t , u ] −> [ [ [ −1, 0, −1 ] , [ 1, 0, 0 ] , [ 1, 1, 0 ] ] ,
[ [ −1, 0, −1 ] , [ 0, −1, 1 ] , [ 0, 0, 1 ] ] ,
[ [ 0, 1, −1 ] , [ 1, 0, 1 ] , [ 0, 0, 1 ] ] ,
[ [ 1, 1, 0 ] , [ 0, −1, 1 ] , [ 0, −1, 0 ] ] ] ,
[ r , s , t , u ] −> [ [ [ 1, 1, 1 ] , [ −1, 0, −1 ] , [ −1, −1, 0 ] ] ,
[ [ 1, 0, 0 ] , [ −1, 0, −1 ] , [ −1, −1, 0 ] ] ,
[ [ 1, 0, 0 ] , [ 0, 0, 1 ] , [ 0, 1, 0 ] ] ,
[ [ 1, 1, 0 ] , [ −1, −1, −1 ] , [ −1, 0, 0 ] ] ] ,
[ r , s , t , u ] −> [ [ [ 0, −1, 1 ] , [ 1, 1, 0 ] , [ 0, 1, 0 ] ] ,
[ [ −1, 0, 0 ] , [ 0, 0, −1 ] , [ 0, −1, 0 ] ] ,
[ [ −1, 0, 0 ] , [ 1, 0, 1 ] , [ 1, 1, 0 ] ] ,
[ [ 1, 0, 1 ] , [ 0, 0, −1 ] , [ 0, 1, −1 ] ] ] ,
[ r , s , t , u ] −> [ [ [ 0, −1, 0 ] , [ 0, 0, −1 ] , [ −1, 1, −1 ] ] ,
[ [ 1, −1, 1 ] , [ 0, 0, 1 ] , [ 0, 1, 0 ] ] ,
[ [ 0, 0, 1 ] , [ 1, −1, 1 ] , [ 1, 0, 0 ] ] ,
[ [ 1, −1, 1 ] , [ 0, −1, 1 ] , [ 0, −1, 0 ] ] ] ,
[ r , s , t , u ] −> [ [ [ 0, 0, −E(12)^7, 0 ] , [ 0, 0, 0, −E(3) ] ,
[ −E(12)^7, E(4) , 0, 0 ] , [ −1, −E(3) , 0, 0 ] ] ,
[ [ 0, 0, 0, −E(12)^7 ] , [ 0, 0, −E(3) , 0 ] ,
[ 0, −E(3)^2, 0, 0 ] , [ E(12)^11, 0, 0, 0 ] ] ,
[ [ −E(12)^11, E(12)^7, 0, 0 ] , [ E(12)^7, E(12)^11, 0, 0 ] ,
[ 0, 0, E(12)^11, −E(3) ] , [ 0, 0, E(3) , −E(12)^11 ] ] ,
[ [ E(3) , 0, 0, 0 ] , [ −1, E(3)^2, 0, 0 ] , [ 0, 0, E(3) , E(4) ] ,
[ 0, 0, 0, E(3)^2 ] ] ] ,
[ r , s , t , u ] −> [ [ [ 0, −E(3)^2, 0, 0 ] , [ 1, 0, −E(3)^2, 0 ] ,
[ 0, −1, 0, −E(12)^7 ] , [ −E(12)^7, 0, 0, 0 ] ] ,
[ [ 0, −E(4) , 0, E(3) ] , [ 0, 0, −E(12)^7, 0 ] , [ 0, E(12)^11, 0, 0 ] ,
[ E(3)^2, 0, 1, 0 ] ] ,
[ [ E(12)^11, 0, −E(12)^7, 0 ] , [ 0, 0, 0, −1 ] ,
[ −E(12)^7, 0, −E(12)^11, 0 ] , [ 0, −1, 0, 0 ] ] ,
[ [ 0, 0, E(3)^2, 0 ] , [ 0, −E(3)^2, 0, −E(4) ] ,
[ −1, 0, −E(3) , 0 ] , [ 0, −E(12)^7, 0, 0 ] ] ] ,
[ r , s , t , u ] −> [ [ [ 0, −E(12)^7, 0, E(3)^2 ] , [ 0, 0, E(4) , 0 ] ,
[ 0, 0, 0, 1 ] , [ −E(3)^2, 0, E(3) , 0 ] ] ,
[ [ 0, 1, 0, 0 ] , [ 1, 0, 0, 0 ] , [ 0, −E(3)^2, 0, E(12)^7 ] ,
[ −E(12)^7, 0, −E(12)^11, 0 ] ] ,
[ [ −E(12)^7, 0, −E(12)^11, 0 ] , [ 0, 0, 0, 1 ] ,
[ −E(12)^11, 0, E(12)^7, 0 ] , [ 0, 1, 0, 0 ] ] ,
[ [ 1, 0, E(3) , 0 ] , [ 0, −E(3)^2, 0, −E(4) ] , [ 0, 0, E(3)^2, 0 ] ,
[ 0, −E(12)^7, 0, 0 ] ] ] ]
gap> chis:=Irr (g );;
gap> IrreducibleAffordingRepresentation ( chis [1]);
[ f1 , f2 , f3 , f4 ] −> [ [ [ 1 ] ] , [ [ 1 ] ] , [ [ 1 ] ] , [ [ 1 ] ] ]
gap> IrreducibleAffordingRepresentation ( chis [2]);
[ f1 , f2 , f3 , f4 ] −> [ [ [ 1 ] ] , [ [ −1 ] ] , [ [ −1 ] ] , [ [ 1 ] ] ]
gap> IrreducibleAffordingRepresentation ( chis [3]);
[ f1 , f2 , f3 , f4 ] −> [ [ [ −1 ] ] , [ [ 1 ] ] , [ [ −1 ] ] , [ [ 1 ] ] ]
gap> IrreducibleAffordingRepresentation ( chis [4]);
[ f1 , f2 , f3 , f4 ] −> [ [ [ −1 ] ] , [ [ −1 ] ] , [ [ 1 ] ] , [ [ 1 ] ] ]
gap> IrreducibleAffordingRepresentation ( chis [5]);
[ f1 , f2 , f3 , f4 ] −> [ [ [ 0, −1 ] , [ −1, 0 ] ] , [ [ 0, 1 ] , [ 1, 0 ] ] ,
[ [ −1, 0 ] , [ 0, −1 ] ] , [ [ E(3)^2, 0 ] , [ 0, E(3) ] ] ]
gap> IrreducibleAffordingRepresentation ( chis [6]);
[ f1 , f2 , f3 , f4 ] −> [ [ [ 0, 1 ] , [ 1, 0 ] ] , [ [ 0, 1 ] , [ 1, 0 ] ] ,
103
[ [ 1, 0 ] , [ 0, 1 ] ] , [ [ E(3)^2, 0 ] , [ 0, E(3) ] ] ]
gap> IrreducibleAffordingRepresentation ( chis [7]);
[ f1 , f2 , f3 , f4 ] −> [ [ [ 0, −1, 0 ] , [ 1, 0, 0 ] , [ 0, 0, −1 ] ] ,
[ [ 0, −1, 0 ] , [ −1, 0, 0 ] , [ 0, 0, −1 ] ] ,
[ [ 1, 0, 0 ] , [ 0, 1, 0 ] , [ 0, 0, −1 ] ] ,
[ [ 0, 1, 0 ] , [ 0, 0, 1 ] , [ 1, 0, 0 ] ] ]
gap> IrreducibleAffordingRepresentation ( chis [8]);
[ f1 , f2 , f3 , f4 ] −> [ [ [ 0, 1, 0 ] , [ −1, 0, 0 ] , [ 0, 0, 1 ] ] ,
[ [ 0, 1, 0 ] , [ 1, 0, 0 ] , [ 0, 0, 1 ] ] ,
[ [ 1, 0, 0 ] , [ 0, 1, 0 ] , [ 0, 0, −1 ] ] ,
[ [ 0, 1, 0 ] , [ 0, 0, 1 ] , [ 1, 0, 0 ] ] ]
gap> IrreducibleAffordingRepresentation ( chis [9]);
[ f1 , f2 , f3 , f4 ] −> [ [ [ 0, 1, 0 ] , [ −1, 0, 0 ] , [ 0, 0, 1 ] ] ,
[ [ 0, −1, 0 ] , [ −1, 0, 0 ] , [ 0, 0, −1 ] ] ,
[ [ −1, 0, 0 ] , [ 0, −1, 0 ] , [ 0, 0, 1 ] ] ,
[ [ 0, 1, 0 ] , [ 0, 0, 1 ] , [ 1, 0, 0 ] ] ]
gap> IrreducibleAffordingRepresentation ( chis [10]);
[ f1 , f2 , f3 , f4 ] −> [ [ [ 0, −1, 0 ] , [ 1, 0, 0 ] , [ 0, 0, −1 ] ] ,
[ [ 0, 1, 0 ] , [ 1, 0, 0 ] , [ 0, 0, 1 ] ] ,
[ [ −1, 0, 0 ] , [ 0, −1, 0 ] , [ 0, 0, 1 ] ] ,
[ [ 0, 1, 0 ] , [ 0, 0, 1 ] , [ 1, 0, 0 ] ] ]
104
Appendix B
GAP Code for Klein Quartic
The GAP code in this appendix has the same format as that in Appendix A; please refer
to the commentary there in order to interpret this code.
gap> f := FreeGroup ( " a " , "b" , " c " ) ;
< f r e e g r o u p on t h e g e n e r a t o r s [ a , b , c ]>
gap> g := f / [ f . 1 ^ 2 , f . 2 ^ 2 , f . 3 ^ 2 , ( f . 1∗ f . 2 ) ^ 2 , ( f . 2∗ f . 3 ) ^ 3 , ( f . 1∗ f . 3 ) ^ 7 , ( f . 1∗ f . 2∗ f . 3 ) ^ 8 ] ;
<f p g r o u p on t h e g e n e r a t o r s [ a , b , c ]>
gap> Order ( g ) ;
336
gap> S t r u c t u r e D e s c r i p t i o n ( g ) ;
"PSL ( 3 , 2 ) : C2"
gap> C o n j u g a c y C l a s s e s ( g ) ;
[ < i d e n t i t y . . . > ^G, b^G, b ∗c^G, a ∗b∗c∗a∗( c∗a∗b ) ^ 2∗( c∗a )^2∗ c^G,
a∗c∗a∗( c∗a∗b ) ^ 2∗( c∗a )^2∗ c^G, c ∗a^G, b∗c∗a^G, ( a ∗b∗( c∗a )^2∗ c )^2^G,
b∗( c∗a∗b∗c∗a )^2∗b∗c^ G ]
gap> R e q u i r e P a c k a g e ( " r e p s n " ) ;
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
Repsn f o r C o n s t r u c t i n g R e p r e s e n t a t i o n s o f F i n i t e Groups
V e r s i o n 3 . 0 . 2
W r i t t e n by
Vahid Dabbaghian
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
true
gap> D i s p l a y ( C h a r a c t e r T a b l e ( g ) ) ;
CT1
2 4 1 1 2 . 4 3 3 3
3 1 1 1 1 . . . . .
7 1 . . . 1 . . . .
1 a 3 a 6 a 2 a 7 a 2b 8 a 4 a 8b
2P 1 a 3 a 3 a 1 a 7 a 1 a 4 a 2b 4 a
3P 1 a 1 a 2 a 2 a 7 a 2b 8b 4 a 8 a
5P 1 a 3 a 6 a 2 a 7 a 2b 8b 4 a 8 a
7P 1 a 3 a 6 a 2 a 1 a 2b 8 a 4 a 8b
X. 1 1 1 1 1 1 1 1 1 1
X. 2 1 1 −1−1 1 1 −1 1 −1
X. 3 6 . . . −1−2 . 2 .
X. 4 6 . . . −1 2 A . −A
X. 5 6 . . . −1 2 −A . A
X. 6 7 1 −1−1 . −1 1 −1 1
X. 7 7 1 1 1 . −1−1−1−1
X. 8 8 −1−1 2 1 . . . .
105
X. 9 8 −1 1 −2 1 . . . .
A = −E(8)+E( 8 ) ^ 3
=−S q r t ( 2 ) =−r 2
gap> I r r e d u c i b l e R e p r e s e n t a t i o n s ( g ) ;
[ [ a , b , c ] −> [ [ [ 1 ] ] , [ [ 1 ] ] , [ [ 1 ] ] ] ,
[ a , b , c ] −> [ [ [ −1 ] ] , [ [ −1 ] ] , [ [ −1 ] ] ] ,
[ a , b , c ] −> [ [ [ 1 / 2 , 3 / 2 , 0 , −1/2 , 0 , 1 ] , [ 3 / 2 , 1 / 2 , −1, 1 / 2 , 0 , 1 ] ,
[ 0 , 0 , 0 , −1, 0 , 0 ] , [ 0 , 0 , −1, 0 , 0 , 0 ] , [ 0 , −1, 0 , 0 , 1 , −1 ] ,
[ −3/2 , −3/2 , 1 , −1/2 , 0 , −2 ] ] ,
[ [ −1/2 , −3/2 , 0 , 1 / 2 , 0 , −1 ] , [ −1/2 , 1 / 2 , 0 , 1 / 2 , 0 , 0 ] ,
[ −3/2 , −3/2 , 1 , −1/2 , 0 , −2 ] , [ 0 , 0 , 0 , 0 , 0 , −1 ] ,
[ −1, 0 , 1 , −1, −1, 0 ] , [ 0 , 0 , 0 , −1, 0 , 0 ] ] ,
[ [ −1/2 , −1/2 , 1 , −1/2 , −1, 0 ] , [ −1, 0 , 1 , 0 , 0 , −1 ] , [ 0 , 0 , 0 , 0 , −1, 0 ] ,
[ −1/2 , 1 / 2 , 0 , 1 / 2 , −1, 1 ] ,
[ 0 , 0 , −1, 0 , 0 , 0 ] , [ 1 / 2 , −1/2 , −1, 1 / 2 , 0 , 0 ] ] ] ,
[ a , b , c ] −> [ [ [ −1, −E(8)+E( 8 ) ^ 3 , −1, 0 , 0 , 0 ] , [ 0 , 1 , 0 , 0 , 0 , 0 ] ,
[ 0 , 0 , 1 , 0 , 0 , 0 ] ,
[ −E(8)+E( 8 ) ^ 3 , E(8)−E( 8 ) ^ 3 , 1−E(8)+E( 8 ) ^ 3 ,−1−E(8)+E( 8 ) ^ 3 , 2 , 0 ] ,
[ −1−E(8)+E( 8 ) ^ 3 , 0 , −1, −1−E(8)+E( 8 ) ^ 3 , 1+E(8)−E( 8 ) ^ 3 , 0 ] ,
[ −2, 1−E(8)+E( 8 ) ^ 3 ,−3+ E(8)−E( 8 ) ^ 3 ,−2, 2 ∗E(8)−2∗E( 8 ) ^ 3 ,−1 ] ] ,
[ [ 0 , 0 , 0 , 1 , 0 , 0 ] , [ 1 , −1, 1−E(8)+E( 8 ) ^ 3 , 1 , −E(8)+E( 8 ) ^ 3 , 0 ] ,
[ 0 , 0 , 1 , 0 , 0 , 0 ] , [ 1 , 0 , 0 , 0 , 0 , 0 ] ,
[ 0 , 0 , 0 , 0 , 1 , 0 ] , [ −1, 0 , −1, −1, 1+E(8)−E( 8 ) ^ 3 ,−1 ] ] ,
[ [ 1 , 0 , 0 , 0 , 0 , 0 ] , [ 1 , −1, 1 , 1+E(8) −E( 8 ) ^ 3 ,−1−E(8)+E( 8 ) ^ 3 , 0 ] ,
[ −1, 1 , −1, −2, 1+E(8)−E( 8 ) ^ 3 ,−1 ] ,
[ 1+E(8)−E( 8 ) ^ 3 , 0 , E(8) −E( 8 ) ^ 3 , 1+E(8)−E( 8 ) ^ 3 ,−2−E(8)+E( 8 ) ^ 3 , 0 ] ,
[ 2 , −1+ E(8)−E( 8 ) ^ 3 , 2−E(8)+E( 8 ) ^ 3 , 2−E(8)+E( 8 ) ^ 3 ,−E(8)+E( 8 ) ^ 3 , 1−E(8)+E( 8 ) ^ 3 ] ,
[ 1 , −1, 1−E(8)+E( 8 ) ^ 3 , 1 , −E(8)+E( 8 ) ^ 3 , 0 ] ] ] ,
[ a , b , c ] −> [ [ [ 1 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 1 , 0 , 0 , 0 ] , [ 0 , 1 , 0 , 0 , 0 , 0 ] ,
[ −3−2∗E(8)+2∗E( 8 ) ^ 3 , 5+4∗E(8)−4∗E( 8 ) ^ 3 , 4+3∗E(8)−3∗E( 8 ) ^ 3 , 1+E(8)−E( 8 ) ^ 3 ,
−2−E(8)+E( 8 ) ^ 3 , 3+2∗E(8)−2∗E( 8 ) ^ 3 ] ,
[ −2−E(8)+E( 8 ) ^ 3 , 3+2∗E(8)−2∗E( 8 ) ^ 3 , 2+2∗E(8)−2∗E( 8 ) ^ 3 , E(8)−E( 8 ) ^ 3 ,−1−E(8)+E( 8 ) ^ 3 ,
1+E(8)−E( 8 ) ^ 3 ] ,
[ E(8) −E( 8 ) ^ 3 ,−1−E(8)+E( 8 ) ^ 3 ,−1−E(8)+E( 8 ) ^ 3 , 0 , 0 , −1 ] ] ,
[ [ 1 , 0 , 0 , 0 , 0 , 0 ] , [ −1−2∗E(8)+2∗E( 8 ) ^ 3 , 3+3∗E(8)−3∗E( 8 ) ^ 3 , 3+2∗E(8)−2∗E( 8 ) ^ 3 ,
1 , −2−E(8)+E( 8 ) ^ 3 , 2+E(8)−E( 8 ) ^ 3 ] ,
[ 4+2 ∗E(8)−2∗E( 8 ) ^ 3 ,−6−4∗E(8)+4∗E( 8 ) ^ 3 ,−5−3∗E(8)+3∗E( 8 ) ^ 3 ,−1−E(8)+E( 8 ) ^ 3 ,
2+2∗E(8)−2∗E( 8 ) ^ 3 ,−3−2∗E(8)+2∗E( 8 ) ^ 3 ] ,
[ 0 , 0 , 0 , 0 , 0 , 1 ] , [ 1+E(8) −E( 8 ) ^ 3 ,−2−2∗E(8)+2∗E( 8 ) ^ 3 ,−2−E(8)+E( 8 ) ^ 3 , −1, 1 ,
−1−E(8)+E( 8 ) ^ 3 ] , [ 0 , 0 , 0 , 1 , 0 , 0 ] ] ,
[ [ 3+E(8) −E( 8 ) ^ 3 ,−4−2∗E(8)+2∗E( 8 ) ^ 3 ,−3−2∗E(8)+2∗E( 8 ) ^ 3 ,−E(8)+E( 8 ) ^ 3 ,
1+E(8)−E( 8 ) ^ 3 ,−2−2∗E(8)+2∗E( 8 ) ^ 3 ] ,
[ 3+2 ∗E(8)−2∗E( 8 ) ^ 3 ,−4−3∗E(8)+3∗E( 8 ) ^ 3 ,−3−2∗E(8)+2∗E( 8 ) ^ 3 ,−1−E(8)+E( 8 ) ^ 3 ,
2+E(8)−E( 8 ) ^ 3 ,−2−2∗E(8)+2∗E( 8 ) ^ 3 ] ,
[ −E(8)+E( 8 ) ^ 3 , E(8)−E( 8 ) ^ 3 , 0 , 1 , −1, 1 ] , [ 3+2 ∗E(8)−2∗E( 8 ) ^ 3 ,−5−4∗E(8)+4∗E( 8 ) ^ 3 ,
−5−3∗E(8)+3∗E( 8 ) ^ 3 ,−1, 2+E(8)−E( 8 ) ^ 3 ,−3−2∗E(8)+2∗E( 8 ) ^ 3 ] ,
[ 4+2 ∗E(8)−2∗E( 8 ) ^ 3 ,−6−4∗E(8)+4∗E( 8 ) ^ 3 ,−5−3∗E(8)+3∗E( 8 ) ^ 3 ,−1−E(8)+E( 8 ) ^ 3 ,
2+2∗E(8)−2∗E( 8 ) ^ 3 ,−3−2∗E(8)+2∗E( 8 ) ^ 3 ] , [ −1, 1 , 1 , 0 , 0 , 0 ] ] ] ,
[ a , b , c ] −> [ [ [ −3/2 , −5/4 , 5 / 4 , 1 1 / 4 , 1 / 2 , −7/4 , 1 ] ,
[ −1/2 , −3/4 , 3 / 4 , 1 / 4 , −1/2 , 3 / 4 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 1 , 0 ] ,
[ −3/2 , −5/4 , 1 9 / 1 2 , 3 7 / 1 2 , −1/6 , −29/12 , 4/3 ] ,
[ 3 / 2 , −1/4 , −1/12 , −19/12 , 1 / 6 , 1 1 / 1 2 , −1/3 ] , [ 0 , 0 , 1 , 0 , 0 , 0 , 0 ] ,
[ 3 / 2 , 3 / 4 , 1 / 4 , −13/4 , 1 / 2 , 1 3 / 4 , −2 ] ] ,
[ [ 2 , 1 , −2/3 , −14/3 , 1 / 3 , 1 3 / 3 , −8/3 ] , [ 0 , −1, 0 , 0 , 0 , 0 , 0 ] ,
[ 1 / 2 , −3/4 , 5 / 1 2 , −13/12 , 1 / 6 , 5 / 1 2 , −1/3 ] , [ 3 / 2 , 5 / 4 , −19/12 , −37/12 , 1 / 6 ,
2 9 / 1 2 ,−4/3 ] , [ 0 , 0 , 0 , 0 , 0 , 0 , 1 ] ,
[ 1 , 1 , −4/3 , −4/3 , 2 / 3 , 2 / 3 , −1/3 ] , [ 0 , 0 , 0 , 0 , 1 , 0 , 0 ] ] ,
[ [ 0 , 1 , 0 , 0 , 0 , 0 , 0 ] , [ 1 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , −1/2 , 1 / 2 , 1 / 2 , 0 , 1 / 2 , −1 ] ,
[ 3 / 2 , 5 / 4 , −1/4 , −7/4 , 1 / 2 , 3 / 4 , 0 ] , [ 1 / 2 , −3/4 , 3 / 4 , −7/4 , 1 / 2 , 1 1 / 4 , −1 ] ,
[ 3 / 2 , 5 / 4 , −11/12 , −17/12 , 5 / 6 , 1 / 1 2 , 1/3 ] ,
[ 1 , 1 , −4/3 , −4/3 , 2 / 3 , 2 / 3 , −1/3 ] ] ] ,
[ a , b , c ] −> [ [ [ 5 / 3 , −4, −11/3 , 2 / 3 , −7/3 , 3 , 1 ] , [ −1, 0 , 1 , 1 , 1 , −1, 0 ] ,
[ 2 , −3, −5, −1, −4, 5 , 1 ] , [ 0 , 0 , 0 , 1 , 0 , 0 , 0 ] ,
106
[ 1 3 / 3 , −8, −25/3 , 4 / 3 , −20/3 , 8 , 3 ] , [ 1 4 / 3 , −8, −29/3 , 2 / 3 , −25/3 , 1 0 , 3 ] ,
[ −7/3 , 1 , 4 / 3 , −1/3 , 8 / 3 , −2, 0 ] ] ,
[ [ 0 , 1 , 0 , 0 , 0 , 0 , 0 ] , [ 1 , 0 , 0 , 0 , 0 , 0 , 0 ] ,
[ 5 / 3 , −3, −14/3 , −1/3 , −13/3 , 5 , 1 ] , [ 5 / 3 , −3, −8/3 , 2 / 3 , −4/3 , 2 , 1 ] ,
[ 1 , −1, −3, 0 , −2, 3 , 0 ] , [ 8 / 3 , −4, −20/3 , −1/3 , −16/3 , 7 , 1 ] ,
[ 7 / 3 , −1, −4/3 , 1 / 3 , −8/3 , 2 , 0 ] ] ,
[ [ 2 , −3, −5, −1, −4, 5 , 1 ] , [ −11/3 , 4 , 1 1 / 3 , −5/3 , 1 6 / 3 , −5, −1 ] ,
[ 4 / 3 , 0 , −1/3 , 1 / 3 , −5/3 , 1 , −1 ] , [ −7/3 , 1 , 4 / 3 , −1/3 , 8 / 3 , −2, 0 ] ,
[ 8 / 3 , −4, −20/3 , −1/3 , −16/3 , 7 , 1 ] , [ 2 / 3 , 0 , −5/3 , −1/3 , −4/3 , 2 , −1 ] ,
[ −7/3 , 3 , 7 / 3 , −4/3 , 1 1 / 3 , −4, −1 ] ] ] ,
[ a , b , c ] −> [ [ [ 1 / 2 , 1 / 2 , 1 / 2 , 1 , 1 , −1/2 , 3 / 2 , 1 ] ,
[ −3/2 , −3/2 , −3/2 , 0 , 0 , −1/2 , −1/2 , −1 ] , [ 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ] ,
[ 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 ] , [ 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ] ,
[ 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 ] , [ 3 / 2 , 1 / 2 , 0 , −2, −3/2 , 1 , −3/2 , 0 ] ] ,
[ [ 3 / 2 , 1 / 2 , 0 , −2, −3/2 , 1 , −3/2 , 0 ] , [ −3/2 , −1/2 , 0 , 2 , 1 / 2 , −1, 1 / 2 , 0 ] ,
[ 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ] , [ 1 , 1 , 0 , −1, −1, 1 , −1, 0 ] ,
[ 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ] ,
[ −1, −1, −1, 0 , 0 , 0 , 0 , 0 ] , [ 1 / 2 , 1 / 2 , 1 / 2 , 1 , 1 , −1/2 , 3 / 2 , 1 ] ] ,
[ [ 0 , 1 , 1 , 2 , 2 , −1, 2 , 2 ] , [ 2 , 0 , 0 , −3, −2, 1 , −2, −1 ] ,
[ −2, −1, −1, 1 , 0 , −1, 0 , −1 ] , [ −1/2 , 1 / 2 , 1 , 2 , 3 / 2 , −1, 3 / 2 , 2 ] ,
[ 0 , −1, −1, −1, 0 , 0 , −1, −1 ] , [ −1, −1, −1, 0 , 0 , 0 , 0 , 0 ] ,
[ 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 ] , [ 1 / 2 , 1 / 2 , 0 , 0 , −1/2 , 1 , −1/2 , 0 ] ] ] ,
[ a , b , c ] −> [ [ [ −1, 1 , −1, 0 , 1 , 0 , 0 , 0 ] , [ 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 ] ,
[ 0 , 0 , 0 , 0 , −1, 0 , 0 , 0 ] , [ 1 , 0 , 1 , 0 , −1, 1 , 1 , −1 ] ,
[ 0 , 0 , −1, 0 , 0 , 0 , 0 , 0 ] , [ 1 , 0 , 0 , 1 , 0 , 0 , 1 , −1 ] ,
[ 0 , 0 , 0 , 0 , 0 , 0 , −1, 0 ] , [ 0 , 1 , 0 , 0 , 0 , 0 , 0 , −1 ] ] ,
[ [ −1, 0 , 1 , −1, 0 , 1 , 0 , 0 ] , [ 0 , −1, 0 , 0 , 0 , 0 , 0 , 0 ] ,
[ 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ] , [ 1 , 0 , 0 , 1 , 0 , 0 , 1 , −1 ] , [ 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ] ,
[ 1 , 0 , 1 , 0 , −1, 1 , 1 , −1 ] , [ 0 , 0 , −1, 1 , 0 , −1, −1, 0 ] ,
[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , −1 ] ] ,
[ [ 0 , 0 , 0 , 0 , 0 , −1, 0 , 0 ] , [ 0 , 0 , −1, 0 , 0 , −1, −1, 0 ] ,
[ 1 , −1, 0 , 0 , −1, 0 , 0 , 0 ] , [ −1, 0 , 0 , −1, 0 , 1 , 0 , 0 ] ,
[ 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 ] , [ −1, 0 , 0 , 0 , 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ] ,
[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , −1 ] ] ] ]
107
Appendix C
FreeFEM++ Code for Genus 2
The following box contains the FreeFEM++ code for the Bolza surface. It contains basic
comments, but for more information about the various solvers and ﬁnite element spaces
available in the software, please consult the manual [32].
i n t n = 30; // number o f modes
i n t nev=100; // number o f e i g e n v a l u e s t o b e c a l c u l a t e d
string fnm = "bolza_surface_30n_100nev . txt"; // f i l e name f o r s a v i n g
real r = 0.4550898605622276; // r a d i u s o f c i r c l e
real c = 1.09868411346781; // c e n t r e o f c i r c l e on x −a x i s
border G1 (t=5 ∗pi/4,3 ∗pi/4) { x=c+r ∗cos(t ); y=r ∗sin (t );};
border G2 (t=5 ∗pi/4,3 ∗pi/4) { x=cos(pi /4) ∗(c+r∗cos(t)) −sin (pi/4) ∗r∗sin (t );
y=sin (pi /4)∗(c+r∗cos(t))+cos(pi/4) ∗r∗sin (t );};
border G3 (t=5 ∗pi/4,3 ∗pi/4) { x=cos(pi /2) ∗(c+r∗cos(t)) −sin (pi/2) ∗r∗sin (t );
y=sin (pi /2)∗(c+r∗cos(t))+cos(pi/2) ∗r∗sin (t );};
border G4 (t=5 ∗pi/4,3 ∗pi/4) { x=cos(3 ∗pi /4)∗(c+r∗cos(t)) −sin (3∗pi/4)∗r∗sin (t );
y=sin (3∗pi /4)∗(c+r∗cos(t))+cos(3 ∗pi/4)∗r∗sin (t );};
border G5 (t=5 ∗pi/4,3 ∗pi/4) { x=cos(pi ) ∗(c+r∗cos(t)) −sin (pi)∗r∗sin (t );
y=sin (pi )∗(c+r∗cos(t))+cos(pi) ∗r∗sin (t );};
border G6 (t=5 ∗pi/4,3 ∗pi/4) { x=cos(5 ∗pi /4)∗(c+r∗cos(t)) −sin (5∗pi/4)∗r∗sin (t );
y=sin (5∗pi /4)∗(c+r∗cos(t))+cos(5 ∗pi/4)∗r∗sin (t );};
border G7 (t=5 ∗pi/4,3 ∗pi/4) { x=cos(6 ∗pi /4)∗(c+r∗cos(t)) −sin (6∗pi/4)∗r∗sin (t );
y=sin (6∗pi /4)∗(c+r∗cos(t))+cos(6 ∗pi/4)∗r∗sin (t );};
border G8 (t=5 ∗pi/4,3 ∗pi/4) { x=cos(7 ∗pi /4)∗(c+r∗cos(t)) −sin (7∗pi/4)∗r∗sin (t );
y=sin (7∗pi /4)∗(c+r∗cos(t))+cos(7 ∗pi/4)∗r∗sin (t );};
plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n));
mesh Th=buildmesh(G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n) , fixeborder= true );
plot (Th, wait=true , f i l l=true );
fespace Vh(Th,P2, periodic =[[1 ,y] ,[5 ,y] ,[3 ,x] ,[7 ,x] ,[2 ,y −x] ,[6 ,y−x] ,[4 ,y+x] ,[8 ,y+x ]]);
// g l u e s o p p o s i t e s i d e s s u c h t h a t o r i e n t a t i o n i s p r e s e r v e d
Vh u1, u2;
real sigma = 0.00001; // v a l u e o f t h e s h i f t
varf op(u1,u2)= int2d(Th)(dx(u1) ∗dx(u2)+ dy(u1) ∗dy(u2)− sigma∗(4∗u1∗u2)/(1−x^2−y^2)^2);
108
varf b([u1 ] ,[ u2]) = int2d(Th)((4 ∗u1∗u2)/(1−x^2−y^2)^2);
matrix OP= op(Vh,Vh, solver=Crout , factorize =1);
matrix B=b(Vh,Vh, solver=CG, eps=1e−20);
real [ i n t] ev(nev );
Vh[ i n t] eV(nev );
i n t k=EigenValue(OP,B,sym= true , sigma=sigma , value=ev , vector=eV, tol=1e−10,maxit=0,ncv=0);
f o r ( i n t i=0;i<k; i++) {
u1=eV[ i ];
real gg = int2d(Th)(dx(u1) ∗dx(u1) + dy(u1) ∗dy(u1)); real mm = int2d(Th)(u1 ∗u1) ;
ofstream Eva(fnm, append );
Eva << ev[ i ] << "\n";
// c o u t < <"−−−−" < < i < <"" < <e v [ i ]<<" e r r ="
//< <dx ( u1 )∗ dx ( u1 ) + dy ( u1 )∗ dy ( u1 )− ( e v [ i ] )∗ u1∗u1 < < " −−−"<<e n d l ; p l o t (eV [ i ] ,
cmm="Eigen/uni2423Vector/uni2423"+i+"/uni2423valeur/uni2423=" + ev[ i ] ,wait=1,value=1);
//un−comment t h e a b o v e two l i n e s t o d i s p l a y l e v e l s e t s f o r each e i g e n f u n c t i o n
}
Table C.1 shows the positive eigenvalues of the Bolza surface, up to approximately
100. They can be compared with the much higher accuracy eigenvalues calculated by
Strohmaier and Uski using the algorithm described in [77]. The data ﬁles associated with
the paper can be obtained from the personal website of Professor Strohmaier:http:
//www1.maths.leeds.ac.uk/~pmtast/publications/eigdata/datafile.html. Here
can be found the ﬁrst 1000 eigenvalues of the Bolza surface, and other genus 2 surfaces,
including the other two in this appendix.
Related to the Bolza surface is the(2, 3, 8) triangle that tessellates it. We have
produced a program to calculate that eigenvalues of this - please see the Bolza surface
codeforcomments. Theonecommentincludedinthiscoderelatestoboundaryconditions
- it is straightforward to change between Dirichlet and Neumann boundary conditions.
i n t n = 50;
i n t nev = 100;
string fnm = "238tri_50n_100nev_nnn. txt";
border G1 (t=0,0.4056163087774724) { x=t ; y=0;};
border G2 (t=0.33681578765748216,0) { x=t ; y=t ∗tan(pi /8);};
border G3 (t=0.4056163087774724,0.33681578765748216) { x=t ;
y=0.5946036542842016 −sqrt ((1.189207445439991^2) −(t−1.435500206409523)^2);};
plot (G1(n)+G2(n)+G3(n));
mesh Th=buildmesh(G1(n)+G2(n)+G3(n));
plot (Th);
fespace Vh(Th,P2);
109
Vh u1, u2;
real sigma = 0.001;
varf op(u1,u2)= int2d(Th)(dx(u1) ∗dx(u2)+ dy(u1) ∗dy(u2)− sigma∗(4∗u1∗u2)/(1−x^2−y^2)^2);
// n a t u r a l l y , t h i s g i v e s Neumann boundary c o n d i t i o n s on a l l t h r e e s i d e s .
//To change one or more s i d e s t o a D i r i c h l e t c o n d i t i o n , add t h e p h r a s e
// ‘+on (G1 , u1 =0) ’ a f t e r t h e c l o s e d p a r e n t h e s i s .
// This w i l l g i v e a D i r i c h l e t c o n d i t i o n on G1 .
varf b([u1 ] ,[ u2]) = int2d(Th)((4 ∗u1∗u2)/(1−x^2−y^2)^2);
matrix OP= op(Vh,Vh, solver=Crout , factorize =1);
matrix B=b(Vh,Vh, solver=CG, eps=1e−20);
real [ i n t] ev(nev );
Vh[ i n t] eV(nev );
i n t k=EigenValue(OP,B,sym= true , sigma=sigma , value=ev , vector=eV, tol=1e−10,maxit=0,ncv=0);
f o r ( i n t i=0;i<k; i++) {
u1=eV[ i ];
real gg = int2d(Th)(dx(u1) ∗dx(u1) + dy(u1) ∗dy(u1)); real mm = int2d(Th)(u1 ∗u1) ;
ofstream Eva(fnm, append );
Eva << ev[ i ] << "\n";
}
Also of interest is the spectrum of the right angled pentagon of areaπ
2 with mixed
boundary conditions, studied in Section 3.4. All of the multiplicity 4 eigenvalues ofB ap-
pear in this spectrum with simple multiplicity. Recall the discussion about isospectrality
in the introduction to this work - one can see for oneself that swapping the Dirichlet and
Neumann conditions in the code below (see the comments in the code for the(2, 3, 8)
triangle) produces the same spectrum! Table C.2 shows the eigenvalues of this problem
up to 200; one can compare this to Table C.1, where all of the eigenvalues in Table C.2
appear with multiplicity 4.
i n t n=30;
i n t nev=100;
real r=0.643594;
string fnm = "pentagon_30n_100nev. txt"; // f i l e name f o r s a v i n g
border G1 (t=0.5,1) { x=r ∗2∗cos(pi/8)+r ∗cos((9−2∗t)∗pi /8); y=r∗sin((9 −2∗t)∗pi /8);};
border G2 (t= −1,0) { x=cos(pi/4) ∗r∗2∗cos(pi/8)+r ∗cos((9−2∗t)∗pi /8);
y=sin (pi/4) ∗r∗2∗cos(pi/8)+r ∗sin((9 −2∗t)∗pi /8);};
border G3 (t=1,0.5) { x=r ∗sin((9 −2∗t)∗pi /8); y=r∗2∗cos(pi/8)+r ∗cos((9−2∗t)∗pi /8);};
border G4 (t=0.545613,0) { x=0; y=t ;};
border G5 (t=0,0.545613) { x=t ; y=0;};
plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n));
mesh Th=buildmesh(G1(n)+G2(n)+G3(n)+G4(n)+G5(n));
110
plot (Th);
fespace Vh(Th,P2);
Vh u1, u2;
real sigma = 0.00001;
varf op(u1,u2)= int2d(Th)(dx(u1) ∗dx(u2)+ dy(u1) ∗dy(u2)− sigma∗ u1∗u2)
+on(G2,u1=0)+on(G4,u1=0);
varf b([u1 ] ,[ u2]) = int2d(Th)((4 ∗u1∗u2)/(1−x^2−y^2)^2);
matrix OP= op(Vh,Vh, solver=Crout , factorize =1);
matrix B=b(Vh,Vh, solver=CG, eps=1e−20);
real [ i n t] ev(nev );
Vh[ i n t] eV(nev );
i n t k=EigenValue(OP,B,sym= true , sigma=sigma , value=ev , vector=eV, tol=1e−10,maxit=0,ncv=0);
f o r ( i n t i=0;i<k; i++) {
u1=eV[ i ];
real gg = int2d(Th)(dx(u1) ∗dx(u1) + dy(u1) ∗dy(u1)); real mm = int2d(Th)(u1 ∗u1) ;
ofstream Eva(fnm, append );
Eva << ev[ i ] << "\n";
}
We have produced FreeFEM++ codes for other genus 2 surfaces during this project,
and would like to include them in this appendix. First, we give the code that computes
the spectrum of the surface with automorphism groupZ10:
i n t n = 50;
i n t nev = 50;
string fnm="Z10 −Eigenvalues −n50−nev50 . txt"; // f i l e name f o r s a v i n g
real r = 0.4133042381223985;
real c = 1.082044543098821;
real s = 0.6687403049764225;
real x01 = s ;
real y01 = 0;
real x04 = s ∗cos(3∗pi /5);
real y04 = s ∗sin (3∗pi /5);
real x03 = s ∗cos(2∗pi /5);
real y03 = s ∗sin (2∗pi /5);
real x06 = s ∗cos(pi );
real y06 = s ∗sin (pi );
real x05 = s ∗cos(4∗pi /5);
real y05 = s ∗sin (4∗pi /5);
real x08 = s ∗cos(7∗pi /5);
real y08 = s ∗sin (7∗pi /5);
real x07 = s ∗cos(6∗pi /5);
real y07 = s ∗sin (6∗pi /5);
111
real x10 = s ∗cos(9∗pi /5);
real y10 = s ∗sin (9∗pi /5);
real x09 = s ∗cos(8∗pi /5);
real y09 = s ∗sin (8∗pi /5);
real x02 = s ∗cos(pi /5);
real y02 = s ∗sin (pi /5);
border G1 (t=6 ∗pi/5,4 ∗pi/5) { x=c+r ∗cos(t ); y=r ∗sin (t );};
border G2 (t=6 ∗pi/5,4 ∗pi/5) { x=cos(pi /5) ∗(c+r∗cos(t)) −sin (pi/5) ∗r∗sin (t );
y=sin (pi /5)∗(c+r∗cos(t))+cos(pi/5) ∗r∗sin (t );};
border G3 (t=6 ∗pi/5,4 ∗pi/5) { x=cos(2 ∗pi /5)∗(c+r∗cos(t)) −sin (2∗pi/5)∗r∗sin (t );
y=sin (2∗pi /5)∗(c+r∗cos(t))+cos(2 ∗pi/5)∗r∗sin (t );};
border G4 (t=6 ∗pi/5,4 ∗pi/5) { x=cos(3 ∗pi /5)∗(c+r∗cos(t)) −sin (3∗pi/5)∗r∗sin (t );
y=sin (3∗pi /5)∗(c+r∗cos(t))+cos(3 ∗pi/5)∗r∗sin (t );};
border G5 (t=6 ∗pi/5,4 ∗pi/5) { x=cos(4 ∗pi /5)∗(c+r∗cos(t)) −sin (4∗pi/5)∗r∗sin (t );
y=sin (4∗pi /5)∗(c+r∗cos(t))+cos(4 ∗pi/5)∗r∗sin (t );};
border G6 (t=6 ∗pi/5,4 ∗pi/5) { x=cos(pi ) ∗(c+r∗cos(t)) −sin (pi)∗r∗sin (t );
y=sin (pi )∗(c+r∗cos(t))+cos(pi) ∗r∗sin (t );};
border G7 (t=6 ∗pi/5,4 ∗pi/5) { x=cos(6 ∗pi /5)∗(c+r∗cos(t)) −sin (6∗pi/5)∗r∗sin (t );
y=sin (6∗pi /5)∗(c+r∗cos(t))+cos(6 ∗pi/5)∗r∗sin (t );};
border G8 (t=6 ∗pi/5,4 ∗pi/5) { x=cos(7 ∗pi /5)∗(c+r∗cos(t)) −sin (7∗pi/5)∗r∗sin (t );
y=sin (7∗pi /5)∗(c+r∗cos(t))+cos(7 ∗pi/5)∗r∗sin (t );};
border G9 (t=6 ∗pi/5,4 ∗pi/5) { x=cos(8 ∗pi /5)∗(c+r∗cos(t)) −sin (8∗pi/5)∗r∗sin (t );
y=sin (8∗pi /5)∗(c+r∗cos(t))+cos(8 ∗pi/5)∗r∗sin (t );};
border G10 (t=6 ∗pi/5,4 ∗pi/5) { x=cos(9 ∗pi /5)∗(c+r∗cos(t)) −sin (9∗pi/5)∗r∗sin (t );
y=sin (9∗pi /5)∗(c+r∗cos(t))+cos(9 ∗pi/5)∗r∗sin (t );};
plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n));
mesh Th=buildmesh(G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n) ,
fixeborder= true );
plot (Th, wait=true , f i l l=true );
fespace Vh(Th,P2, periodic =[[1 ,y] ,[4 , cos(2 ∗pi /5)∗(y−y04)−sin(−2∗pi /5)∗(x−x04 )] ,
[3 , cos(2∗pi /5)∗(y−y03)−sin (2∗pi /5)∗(x−x03 )] ,[6 ,y] ,
[5 , cos(2∗pi /5)∗(y−y05)−sin(−2∗pi /5)∗(x−x05 )] ,
[8 , cos(2∗pi /5)∗(y−y08)−sin(−2∗pi /5)∗(x−x08 )] ,
[7 , cos(2∗pi /5)∗(y−y07)−sin (2∗pi /5)∗(x−x07 )] ,
[10 , cos(2∗pi /5)∗(y−y10)−sin(−2∗pi /5)∗(x−x10 )] ,
[9 , cos(2∗pi /5)∗(y−y09)−sin (2∗pi /5)∗(x−x09 )] ,
[2 , cos(2∗pi /5)∗(y−y02)−sin (2∗pi /5)∗(x−x02 )]]);
Vh u1, u2;
real sigma = 0.00001;
varf op(u1,u2)= int2d(Th)(dx(u1) ∗dx(u2)+ dy(u1) ∗dy(u2)− sigma∗(4∗u1∗u2)/(1−x^2−y^2)^2);
varf b([u1 ] ,[ u2]) = int2d(Th)((4 ∗u1∗u2)/(1−x^2−y^2)^2);
matrix OP= op(Vh,Vh, solver=Crout , factorize =1);
matrix B=b(Vh,Vh, solver=CG, eps=1e−20);
real [ i n t] ev(nev );
Vh[ i n t] eV(nev );
i n t k=EigenValue(OP,B,sym= true , sigma=sigma , value=ev , vector=eV, tol=1e−10,maxit=0,ncv=0);
f o r ( i n t i=0;i<k; i++) {
112
u1=eV[ i ];
real gg = int2d(Th)(dx(u1) ∗dx(u1) + dy(u1) ∗dy(u1)); real mm = int2d(Th)(u1 ∗u1) ;
ofstream Eva(fnm, append );
Eva << ev[ i ] << "\n";
}
1
2
34
5
6
7
8 9
10
Side associations:
1 – 4, 3 – 6, 5 – 8, 7 – 10, 9 – 2
Figure C.1: Fundamental polygon for the surface with automorphism groupZ10
Next, we have the surface that has a semi-regular 12-gon as its fundamental domain,
and has automorphism group(4, 6| 2, 2) of order 24 (see [20] for a classiﬁcation of this
group):
i n t n = 50;
i n t nev = 50;
string fnm="12gon −Eigenvalues −n50−nev50 . txt"; // f i l e name f o r s a v i n g
real cx = 1.0206207261596574;
real cy = 0.3535533905932733;
real r = 0.4082482904638626;
real s=0.6835992463050957;
real theta=0.22037122071230927;
real x01=s ∗cos(theta );
real y01=s ∗sin (theta );
real x02=s ∗cos(pi/3 −theta );
real y02=s ∗sin (pi/3−theta );
real x03=s ∗cos(pi/3+theta );
real y03=s ∗sin (pi/3+theta );
real x04=s ∗cos(2∗pi/3−theta );
real y04=s ∗sin (2∗pi/3−theta );
real x05=s ∗cos(2∗pi/3+theta );
real y05=s ∗sin (2∗pi/3+theta );
real x06=s ∗cos(3∗pi/3−theta );
113
real y06=s ∗sin (3∗pi/3−theta );
real x07=s ∗cos(3∗pi/3+theta );
real y07=s ∗sin (3∗pi/3+theta );
real x08=s ∗cos(4∗pi/3−theta );
real y08=s ∗sin (4∗pi/3−theta );
real x09=s ∗cos(4∗pi/3+theta );
real y09=s ∗sin (4∗pi/3+theta );
real x10=s ∗cos(5∗pi/3−theta );
real y10=s ∗sin (5∗pi/3−theta );
real x11=s ∗cos(5∗pi/3+theta );
real y11=s ∗sin (5∗pi/3+theta );
real x12=s ∗cos(−theta );
real y12=s ∗sin(−theta );
border G1 (t=4 ∗pi/3,pi) { x=cx+r ∗cos(t ); y=cy+r ∗sin (t );};
border G2 (t=pi ,2 ∗pi/3) { x=cos(pi /3) ∗(cx+r∗cos(t)) −sin (pi/3)∗(−cy+r∗sin (t ));
y=sin (pi /3)∗(cx+r∗cos(t))+cos(pi/3) ∗(−cy+r∗sin (t ));};
border G3 (t=4 ∗pi/3,pi) { x=cos(pi /3) ∗(cx+r∗cos(t)) −sin (pi /3)∗(cy+r∗sin (t ));
y=sin (pi /3)∗(cx+r∗cos(t))+cos(pi /3) ∗(cy+r∗sin (t ));};
border G4 (t=pi ,2 ∗pi/3) { x=cos(2 ∗pi /3)∗(cx+r∗cos(t)) −sin (2∗pi/3)∗(−cy+r∗sin (t ));
y=sin (2∗pi /3)∗(cx+r∗cos(t))+cos(2 ∗pi/3)∗(−cy+r∗sin (t ));};
border G5 (t=4 ∗pi/3,pi) { x=cos(2 ∗pi /3)∗(cx+r∗cos(t)) −sin (2∗pi /3)∗(cy+r∗sin (t ));
y=sin (2∗pi /3)∗(cx+r∗cos(t))+cos(2 ∗pi /3)∗(cy+r∗sin (t ));};
border G6 (t=pi ,2 ∗pi/3) { x=cos(3 ∗pi /3)∗(cx+r∗cos(t)) −sin (3∗pi/3)∗(−cy+r∗sin (t ));
y=sin (3∗pi /3)∗(cx+r∗cos(t))+cos(3 ∗pi/3)∗(−cy+r∗sin (t ));};
border G7 (t=4 ∗pi/3,pi) { x=cos(3 ∗pi /3)∗(cx+r∗cos(t)) −sin (3∗pi /3)∗(cy+r∗sin (t ));
y=sin (3∗pi /3)∗(cx+r∗cos(t))+cos(3 ∗pi /3)∗(cy+r∗sin (t ));};
border G8 (t=pi ,2 ∗pi/3) { x=cos(4 ∗pi /3)∗(cx+r∗cos(t)) −sin (4∗pi/3)∗(−cy+r∗sin (t ));
y=sin (4∗pi /3)∗(cx+r∗cos(t))+cos(4 ∗pi/3)∗(−cy+r∗sin (t ));};
border G9 (t=4 ∗pi/3,pi) { x=cos(4 ∗pi /3)∗(cx+r∗cos(t)) −sin (4∗pi /3)∗(cy+r∗sin (t ));
y=sin (4∗pi /3)∗(cx+r∗cos(t))+cos(4 ∗pi /3)∗(cy+r∗sin (t ));};
border G10 (t=pi ,2 ∗pi/3) { x=cos(5 ∗pi /3)∗(cx+r∗cos(t)) −sin (5∗pi/3)∗(−cy+r∗sin (t ));
y=sin (5∗pi /3)∗(cx+r∗cos(t))+cos(5 ∗pi/3)∗(−cy+r∗sin (t ));};
border G11 (t=4 ∗pi/3,pi) { x=cos(5 ∗pi /3)∗(cx+r∗cos(t)) −sin (5∗pi /3)∗(cy+r∗sin (t ));
y=sin (5∗pi /3)∗(cx+r∗cos(t))+cos(5 ∗pi /3)∗(cy+r∗sin (t ));};
border G12 (t=pi ,2 ∗pi/3) { x=cx+r ∗cos(t ); y=−cy+r∗sin (t );};
plot (G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)+G12(n));
mesh Th=buildmesh(G1(n)+G2(n)+G3(n)+G4(n)+G5(n)+G6(n)+G7(n)+G8(n)+G9(n)+G10(n)+G11(n)
+G12(n) , fixeborder= true );
plot (Th, wait=true , f i l l=true );
fespace Vh(Th,P2, periodic =[[2 ,( cos(pi /6)) ∗(y−y02)−(sin (pi /6))∗(x−x02 )] ,
[5 ,( cos(−pi /6))∗(y−y05)−(sin(−pi /6))∗(x−x05 )] ,
[4 ,( cos(pi /2)) ∗(y−y04)−(sin (pi /2))∗(x−x04 )] ,
[7 ,( cos(pi /6)) ∗(y−y07)−(sin (pi /6))∗(x−x07 )] ,
[6 ,( cos(−7∗pi /6))∗(y−y06)−(sin( −7∗pi /6))∗(x−x06 )] ,
[9 ,( cos(pi /2)) ∗(y−y09)−(sin (pi /2))∗(x−x09 )] ,
[8 ,( cos(pi /6)) ∗(y−y08)−(sin (pi /6))∗(x−x08 )] ,
[11 ,( cos(pi /6)) ∗(y−y11)−(sin(−pi /6))∗(x−x11 )] ,
[10 ,( cos(pi /2)) ∗(y−y10)−(sin (pi /2))∗(x−x10 )] ,
[1 ,( cos(pi /6)) ∗(y−y01)−(sin (pi /6))∗(x−x01 )] ,
[12 ,( cos(pi /6)) ∗(y−y12)−(sin(−pi /6))∗(x−x12 )] ,
[3 ,( cos(−pi /2))∗(y−y03)−(sin(−pi /2))∗(x−x03 )]]);
114
Vh u1, u2;
real sigma = 0.00001;
varf op(u1,u2)= int2d(Th)(dx(u1) ∗dx(u2)+ dy(u1) ∗dy(u2)− sigma∗(4∗u1∗u2)/(1−x^2−y^2)^2);
varf b([u1 ] ,[ u2]) = int2d(Th)((4 ∗u1∗u2)/(1−x^2−y^2)^2);
matrix OP= op(Vh,Vh, solver=Crout , factorize =1);
matrix B=b(Vh,Vh, solver=CG, eps=1e−20);
real [ i n t] ev(nev );
Vh[ i n t] eV(nev );
i n t k=EigenValue(OP,B,sym= true , sigma=sigma , value=ev , vector=eV, tol=1e−10,maxit=0,ncv=0);
f o r ( i n t i=0;i<k; i++) {
u1=eV[ i ];
real gg = int2d(Th)(dx(u1) ∗dx(u1) + dy(u1) ∗dy(u1)); real mm = int2d(Th)(u1 ∗u1) ;
ofstream Eva(fnm, append );
Eva << ev[ i ] << "\n";
}
1
3
5
7
9
11
12
2
4
6
8
10
Side associations:
2 – 5, 4 – 7, 6 – 9, 8 – 11, 10 – 1, 12 – 3
Figure C.2: Fundamental domain for the surface with order 24 automorphism group
115
Eigenvalue Numerical multiplicity
3.83618 3
5.35083 4
8.24401 2
14.7149 4
15.0386 3
18.645 3
20.5069 4
23.0545 1
28.0591 3
30.8081 4
32.6493 1
36.2126 2
38.9353 4
40.0913 3
42.8344 4
43.9864 3
50.5199 3
57.4478 4
59.4306 4
60.988 2
62.595 3
67.5682 3
71.3853 4
73.6255 2
74.8779 1
75.5018 3
75.6305 4
86.1472 4
86.6702 3
91.4225 1
93.3361 4
97.8419 3
100.675 3
Table C.1: First positive eigenvalues of the Bolza surface
116
Eigenvalue Numerical multiplicity
5.35323 1
14.7246 1
20.5174 1
30.8305 1
38.956 1
42.852 1
57.4803 1
59.4601 1
71.4156 1
75.6649 1
86.177 1
93.3682 1
105.547 1
110.988 1
111.675 1
127.163 1
133.738 1
144.59 1
151.081 1
154.5 1
166.766 1
170.721 1
182.089 1
193.034 1
200.792 1
Table C.2: First positive eigenvalues of the mixed boundary problem on a pentagon of areaπ
2
117
Eigenvalue Numerical multiplicity
3.48586 2
4.56299 2
5.05739 2
8.6528 2
8.96267 2
12.1336 1
14.9476 2
16.2255 2
16.9401 2
19.9236 2
20.7194 2
22.1597 1
24.0114 2
24.0994 2
28.7943 2
32.0614 2
32.3071 2
34.5634 2
36.383 2
36.8106 2
40.0014 1
43.8803 2
44.0732 2
45.5809 2
46.316 2
48.2176 2
Table C.3: First positive eigenvalues ofZ10 surface
118
Eigenvalue Numerical multiplicity
3.10942 2
4.12201 2
6.96949 1
7.78 2
8.98983 4
11.1973 1
15.0295 1
16.7819 2
19.5961 2
20.6216 4
20.9365 1
24.5947 2
25.0792 2
26.7752 2
28.8984 2
34.0612 4
34.7219 1
36.2501 1
39.9781 2
40.008 3
46.176 2
46.2604 4
47.5021 1
Table C.4: First positive eigenvalues of the 12-gon with order 24 symmetry group
119
Appendix D
FreeFEM++ Code for Genus 3
Similarly to Appendix C, here we give the FreeFEM++ codes for particular surfaces of
genus 3. We start with the Klein quartic:
i n t n =30;
i n t nev =100;
s t r i n g fnm=" k l e i n _ q u a r t i c−E i g e n v a l u e s−n30−nev100 . t x t " ; // f i l e name f o r s a v i n g
r e a l cx = 1 . 0 3 1 9 6 9 7 2 2 ;
r e a l r = 0 . 2 5 4 8 7 5 4 7 3 ;
r e a l s = 0 . 7 7 7 0 9 4 2 4 8 8 5 8 9 6 3 3 ;
r e a l x06=s ∗ c o s ( 5∗ p i / 7 ) ;
r e a l y06=s ∗ s i n ( 5∗ p i / 7 ) ;
r e a l x03=s ∗ c o s ( 2∗ p i / 7 ) ;
r e a l y03=s ∗ s i n ( 2∗ p i / 7 ) ;
r e a l x05=s ∗ c o s ( 4∗ p i / 7 ) ;
r e a l y05=s ∗ s i n ( 4∗ p i / 7 ) ;
r e a l x10=s ∗ c o s ( 9∗ p i / 7 ) ;
r e a l y10=s ∗ s i n ( 9∗ p i / 7 ) ;
r e a l x07=s ∗ c o s ( 6∗ p i / 7 ) ;
r e a l y07=s ∗ s i n ( 6∗ p i / 7 ) ;
r e a l x12=s ∗ c o s ( 1 1∗ p i / 7 ) ;
r e a l y12=s ∗ s i n ( 1 1∗ p i / 7 ) ;
r e a l x09=s ∗ c o s ( 8∗ p i / 7 ) ;
r e a l y09=s ∗ s i n ( 8∗ p i / 7 ) ;
r e a l x14=s ∗ c o s ( 1 3∗ p i / 7 ) ;
r e a l y14=s ∗ s i n ( 1 3∗ p i / 7 ) ;
r e a l x11=s ∗ c o s ( 1 0∗ p i / 7 ) ;
r e a l y11=s ∗ s i n ( 1 0∗ p i / 7 ) ;
r e a l x02=s ∗ c o s ( p i / 7 ) ;
r e a l y02=s ∗ s i n ( p i / 7 ) ;
r e a l x13=s ∗ c o s ( 1 2∗ p i / 7 ) ;
r e a l y13=s ∗ s i n ( 1 2∗ p i / 7 ) ;
r e a l x04=s ∗ c o s ( 3∗ p i / 7 ) ;
r e a l y04=s ∗ s i n ( 3∗ p i / 7 ) ;
b o r d e r G1 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=cx+r ∗ c o s ( t ) ; y=r∗ s i n ( t ) ; l a b e l = 1 ; } ;
b o r d e r G2 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( p i / 7 )∗( r∗ s i n ( t ) ) ;
y=s i n ( p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( p i / 7 )∗( r∗ s i n ( t ) ) ; } l a b e l = 2 ; ;
b o r d e r G3 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 2∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 2∗ p i / 7 )∗ r∗ s i n ( t ) ;
y=s i n ( 2∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 2∗ p i / 7 )∗ r∗ s i n ( t ) ; } l a b e l = 3 ; ;
b o r d e r G4 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 3∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 3∗ p i / 7 )∗ r∗ s i n ( t ) ;
y=s i n ( 3∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 3∗ p i / 7 )∗ r∗ s i n ( t ) ; l a b e l = 4 ; } ;
b o r d e r G5 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 4∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 4∗ p i / 7 )∗ r∗ s i n ( t ) ;
120
y=s i n ( 4∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 4∗ p i / 7 )∗ r∗ s i n ( t ) ; l a b e l = 5 ; } ;
b o r d e r G6 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 5∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 5∗ p i / 7 )∗ r∗ s i n ( t ) ;
y=s i n ( 5∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 5∗ p i / 7 )∗ r∗ s i n ( t ) ; l a b e l = 6 ; } ;
b o r d e r G7 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 6∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 6∗ p i / 7 )∗ r∗ s i n ( t ) ;
y=s i n ( 6∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 6∗ p i / 7 )∗ r∗ s i n ( t ) ; l a b e l = 7 ; } ;
b o r d e r G8 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 7∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 7∗ p i / 7 )∗ r∗ s i n ( t ) ;
y=s i n ( 7∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 7∗ p i / 7 )∗ r∗ s i n ( t ) ; l a b e l = 8 ; } ;
b o r d e r G9 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 8∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 8∗ p i / 7 )∗ r∗ s i n ( t ) ;
y=s i n ( 8∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 8∗ p i / 7 )∗ r∗ s i n ( t ) ; l a b e l = 9 ; } ;
b o r d e r G10 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 9∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 9∗ p i / 7 )∗ r∗ s i n ( t ) ;
y=s i n ( 9∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 9∗ p i / 7 )∗ r∗ s i n ( t ) ; l a b e l = 1 0 ; } ;
b o r d e r G11 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 1 0∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 1 0∗ p i / 7 )∗ r∗ s i n ( t ) ;
y=s i n ( 1 0∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 1 0∗ p i / 7 )∗ r∗ s i n ( t ) ; l a b e l = 1 1 ; } ;
b o r d e r G12 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 1 1∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 1 1∗ p i / 7 )∗ r∗ s i n ( t ) ;
y=s i n ( 1 1∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 1 1∗ p i / 7 )∗ r∗ s i n ( t ) ; l a b e l = 1 2 ; } ;
b o r d e r G13 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 1 2∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 1 2∗ p i / 7 )∗ r∗ s i n ( t ) ;
y=s i n ( 1 2∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 1 2∗ p i / 7 )∗ r∗ s i n ( t ) ; l a b e l = 1 3 ; } ;
b o r d e r G14 ( t =9∗p i / 7 , 5∗ p i / 7 ) { x=c o s ( 1 3∗ p i / 7 )∗( cx+r∗ c o s ( t ))− s i n ( 1 3∗ p i / 7 )∗ r∗ s i n ( t ) ;
y=s i n ( 1 3∗ p i / 7 )∗( cx+r∗ c o s ( t ))+ c o s ( 1 3∗ p i / 7 )∗ r∗ s i n ( t ) ; l a b e l = 1 4 ; } ;
p l o t (G1( n)+G2( n)+G3( n)+G4( n)+G5( n)+G6( n)+G7( n)+G8( n)+G9( n)+G10 ( n)+G11 ( n)+G12 ( n)+G13 ( n )
+G14 ( n ) ) ;
mesh Th =b u i l d m e s h (G1( n)+G2( n)+G3( n)+G4( n)+G5( n)+G6( n)+G7( n)+G8( n)+G9( n)+G10 ( n)+G11 ( n )
+G12 ( n)+G13 ( n)+G14 ( n ) , f i x e b o r d e r=true ) ;
p l o t ( Th , w a i t=true , f i l l = true ) ;
f e s p a c e Vh( Th , P2 , p e r i o d i c = [ [ 1 , y ] , [ 6 , ( c o s ( 2∗ p i / 7 ) )∗ ( y−y06 )−( s i n (−2∗ p i / 7 ) )∗ ( x−x06 ) ] ,
[ 3 , ( c o s ( 2∗ p i / 7 ) )∗ ( y−y03 )−( s i n ( 2∗ p i / 7 ) )∗ ( x−x03 ) ] , [ 8 , y ] ,
[ 5 , ( c o s ( 4∗ p i / 7 ) )∗ ( y−y05 )−( s i n ( 4∗ p i / 7 ) )∗ ( x−x05 ) ] ,
[ 1 0 , ( c o s ( 2∗ p i / 7 ) )∗ ( y−y10 )−( s i n ( 2∗ p i / 7 ) )∗ ( x−x10 ) ] ,
[ 7 , ( c o s ( 6∗ p i / 7 ) )∗ ( y−y07 )−( s i n ( 6∗ p i / 7 ) )∗ ( x−x07 ) ] ,
[ 1 2 , ( c o s ( 4∗ p i / 7 ) )∗ ( y−y12 )−( s i n ( 4∗ p i / 7 ) )∗ ( x−x12 ) ] ,
[ 9 , ( c o s ( 6∗ p i / 7 ) )∗ ( y−y09 )−( s i n (−6∗ p i / 7 ) )∗ ( x−x09 ) ] ,
[ 1 4 , ( c o s ( 6∗ p i / 7 ) )∗ ( y−y14 )−( s i n ( 6∗ p i / 7 ) )∗ ( x−x14 ) ] ,
[ 1 1 , ( c o s ( 4∗ p i / 7 ) )∗ ( y−y11 )−( s i n (−4∗ p i / 7 ) )∗ ( x−x11 ) ] ,
[ 2 , ( c o s ( 6∗ p i / 7 ) )∗ ( y−y02 )−( s i n (−6∗ p i / 7 ) )∗ ( x−x02 ) ] ,
[ 1 3 , ( c o s ( 2∗ p i / 7 ) )∗ ( y−y13 )−( s i n (−2∗ p i / 7 ) )∗ ( x−x13 ) ] ,
[ 4 , ( c o s ( 4∗ p i / 7 ) )∗ ( y−y04 )−( s i n (−4∗ p i / 7 ) )∗ ( x−x04 ) ] ] ) ;
Vh u1 , u2 ;
r e a l sigma = 0 . 0 0 0 0 1 ;
v a r f op ( u1 , u2)= i n t 2 d (Th ) ( dx ( u1 )∗ dx ( u2)+ dy ( u1 )∗ dy ( u2)− sigma∗( 4∗ u1∗u2 )/(1−x^2−y ^ 2 ) ^ 2 ) ;
v a r f b ( [ u1 ] , [ u2 ] ) = i n t 2 d (Th ) ( ( 4 ∗ u1∗u2 )/(1−x^2−y ^ 2 ) ^ 2 ) ;
m a t r i x OP = op (Vh , Vh , s o l v e r=Crout , f a c t o r i z e = 1 ) ;
m a t r i x B =b (Vh , Vh , s o l v e r= CG, e p s=1e−2 0 ) ;
r e a l [ i n t] ev ( nev ) ;
Vh [i n t] eV ( nev ) ;
i n t k=E i g e n V a l u e (OP, B , sym=true , sigma=sigma , v a l u e=ev , v e c t o r=eV , t o l =1e−10 , maxit =0 , ncv = 0 ) ;
f o r ( i n t i =0; i <k ; i ++) {
u1=eV [ i ] ;
r e a l gg = i n t 2 d (Th ) ( dx ( u1 ) ∗ dx ( u1 ) + dy ( u1 )∗ dy ( u1 ) ) ; r e a l m m = i n t 2 d (Th ) ( u1∗u1 ) ;
o f s t r e a m Eva ( fnm , append ) ;
Eva < < ev [ i ] < < " \n" ;
}
Of relevance to the Klein quartic (and indeed to Hurwitz surfaces in other genera) is
the (2, 3, 7)triangle. We include the code for its spectrum; as with the(2, 3, 8)triangle
121
and the pentagon in Appendix C, it is possible to add a Dirichlet condition to one or
more of its sides.
i n t n = 3 0 ;
i n t nev =100;
s t r i n g fnm="237−E i g e n v a l u e s−n30−nev100 . t x t " ; // f i l e name f o r s a v i n g
r e a l c = 2 . 0 1 2 1 9 2 1 7 2 6 1 2 2 7 8 ;
r e a l r = 1 . 7 4 6 1 1 4 9 2 7 3 5 2 1 9 ;
b o r d e r G1 ( t = 0 , 0 . 2 6 6 0 7 7 2 4 5 2 6 0 0 8 7 9 ) { x=t ; y = 0 ; } ;
b o r d e r G2 ( t = 0 . 3 0 0 7 4 2 6 1 8 7 4 6 3 7 8 9 , 0 ) { x=c o s ( p i / 7 )∗ t ; y=t ∗ s i n ( p i / 7 ) ; } ;
b o r d e r G3 ( t=p i , 3 . 0 6 6 7 9 2 8 2 8 5 0 4 3 2 2 ) { x=c+r∗ c o s ( t ) ; y=r∗ s i n ( t ) ; } ;
p l o t (G1( n)+G2( n)+G3( n ) ) ;
mesh Th =b u i l d m e s h (G1( n)+G2( n)+G3( n ) ) ;
p l o t (Th ) ;
f e s p a c e Vh( Th , P2 ) ;
Vh u1 , u2 ;
r e a l sigma = 0 . 0 0 0 5 ;
v a r f op ( u1 , u2)= i n t 2 d (Th ) ( dx ( u1 )∗ dx ( u2)+ dy ( u1 )∗ dy ( u2)− sigma∗( 4∗ u1∗u2 )/(1−x^2−y ^ 2 ) ^ 2 ) ;
v a r f b ( [ u1 ] , [ u2 ] ) = i n t 2 d (Th ) ( ( 4 ∗ u1∗u2 )/(1−x^2−y ^ 2 ) ^ 2 ) ;
m a t r i x OP = op (Vh , Vh , s o l v e r=Crout , f a c t o r i z e = 1 ) ;
m a t r i x B =b (Vh , Vh , s o l v e r= CG, e p s=1e−2 0 ) ;
r e a l [ i n t] ev ( nev ) ;
Vh [i n t] eV ( nev ) ;
i n t k=E i g e n V a l u e (OP, B , sym=true , sigma=sigma , v a l u e=ev , v e c t o r=eV , t o l =1e−10 , maxit =0 , ncv = 0 ) ;
f o r ( i n t i =0; i <k ; i ++) {
u1=eV [ i ] ;
r e a l gg = i n t 2 d (Th ) ( dx ( u1 ) ∗ dx ( u1 ) + dy ( u1 )∗ dy ( u1 ) ) ; r e a l m m = i n t 2 d (Th ) ( u1∗u1 ) ;
o f s t r e a m Eva ( fnm , append ) ;
Eva < < ev [ i ] < < " \n" ;
}
Next, we include the code for the surfaceM3 in [72]:
i n t n = 3 0 ;
i n t nev = 1 0 0 ;
s t r i n g fnm="m3−E i g e n v a l u e s−n30−nev100 . t x t " ; // f i l e name f o r s a v i n g
r e a l cx = 1 . 0 1 2 2 ;
r e a l cy = 0 . 1 5 6 6 ;
r e a l r = 0 . 2 2 1 4 ;
r e a l s = 0 . 8 0 4 5 ;
r e a l t h e t a = 0 . 1 2 3 8 ;
r e a l x01 = s ∗ c o s ( t h e t a ) ;
r e a l y01 = s ∗ s i n ( t h e t a ) ;
r e a l x02 = s ∗ c o s ( p i /6−t h e t a ) ;
r e a l y02 = s ∗ s i n ( p i /6−t h e t a ) ;
r e a l x03 = s ∗ c o s ( p i /6+ t h e t a ) ;
r e a l y03 = s ∗ s i n ( p i /6+ t h e t a ) ;
r e a l x04 = s ∗ c o s ( 2∗ p i /6−t h e t a ) ;
r e a l y04 = s ∗ s i n ( 2∗ p i /6−t h e t a ) ;
r e a l x05 = s ∗ c o s ( 2∗ p i /6+ t h e t a ) ;
122
r e a l y05 = s ∗ s i n ( 2∗ p i /6+ t h e t a ) ;
r e a l x06 = s ∗ c o s ( 3∗ p i /6−t h e t a ) ;
r e a l y06 = s ∗ s i n ( 3∗ p i /6−t h e t a ) ;
r e a l x07 = s ∗ c o s ( 3∗ p i /6+ t h e t a ) ;
r e a l y07 = s ∗ s i n ( 3∗ p i /6+ t h e t a ) ;
r e a l x08 = s ∗ c o s ( 4∗ p i /6−t h e t a ) ;
r e a l y08 = s ∗ s i n ( 4∗ p i /6−t h e t a ) ;
r e a l x09 = s ∗ c o s ( 4∗ p i /6+ t h e t a ) ;
r e a l y09 = s ∗ s i n ( 4∗ p i /6+ t h e t a ) ;
r e a l x10 = s ∗ c o s ( 5∗ p i /6−t h e t a ) ;
r e a l y10 = s ∗ s i n ( 5∗ p i /6−t h e t a ) ;
r e a l x11 = s ∗ c o s ( 5∗ p i /6+ t h e t a ) ;
r e a l y11 = s ∗ s i n ( 5∗ p i /6+ t h e t a ) ;
r e a l x12 = s ∗ c o s ( 6∗ p i /6−t h e t a ) ;
r e a l y12 = s ∗ s i n ( 6∗ p i /6−t h e t a ) ;
r e a l x13 = s ∗ c o s ( 6∗ p i /6+ t h e t a ) ;
r e a l y13 = s ∗ s i n ( 6∗ p i /6+ t h e t a ) ;
r e a l x14 = s ∗ c o s ( 7∗ p i /6−t h e t a ) ;
r e a l y14 = s ∗ s i n ( 7∗ p i /6−t h e t a ) ;
r e a l x15 = s ∗ c o s ( 7∗ p i /6+ t h e t a ) ;
r e a l y15 = s ∗ s i n ( 7∗ p i /6+ t h e t a ) ;
r e a l x16 = s ∗ c o s ( 8∗ p i /6−t h e t a ) ;
r e a l y16 = s ∗ s i n ( 8∗ p i /6−t h e t a ) ;
r e a l x17 = s ∗ c o s ( 8∗ p i /6+ t h e t a ) ;
r e a l y17 = s ∗ s i n ( 8∗ p i /6+ t h e t a ) ;
r e a l x18 = s ∗ c o s ( 9∗ p i /6−t h e t a ) ;
r e a l y18 = s ∗ s i n ( 9∗ p i /6−t h e t a ) ;
r e a l x19 = s ∗ c o s ( 9∗ p i /6+ t h e t a ) ;
r e a l y19 = s ∗ s i n ( 9∗ p i /6+ t h e t a ) ;
r e a l x20 = s ∗ c o s ( 1 0∗ p i /6−t h e t a ) ;
r e a l y20 = s ∗ s i n ( 1 0∗ p i /6−t h e t a ) ;
r e a l x21 = s ∗ c o s ( 1 0∗ p i /6+ t h e t a ) ;
r e a l y21 = s ∗ s i n ( 1 0∗ p i /6+ t h e t a ) ;
r e a l x22 = s ∗ c o s ( 1 1∗ p i /6−t h e t a ) ;
r e a l y22 = s ∗ s i n ( 1 1∗ p i /6−t h e t a ) ;
r e a l x23 = s ∗ c o s ( 1 1∗ p i /6+ t h e t a ) ;
r e a l y23 = s ∗ s i n ( 1 1∗ p i /6+ t h e t a ) ;
r e a l x24 = s ∗ c o s ( t h e t a ) ;
r e a l y24 = s ∗ s i n (−t h e t a ) ;
b o r d e r G1 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=cx+r ∗ c o s ( t ) ; y=cy+r∗ s i n ( t ) ; } ;
b o r d e r G2 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=c o s ( p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( p i /6)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( p i /6)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G3 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=c o s ( p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( p i / 6 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( p i / 6 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G4 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=c o s ( 2∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 2∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 2∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 2∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G5 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=c o s ( 2∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 2∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 2∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 2∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G6 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=c o s ( 3∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 3∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 3∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 3∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G7 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=c o s ( 3∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 3∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 3∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 3∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G8 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=c o s ( 4∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 4∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 4∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 4∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G9 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=c o s ( 4∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 4∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 4∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 4∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G10 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=c o s ( 5∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 5∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 5∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 5∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G11 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=c o s ( 5∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 5∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 5∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 5∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G12 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=c o s ( 6∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 6∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 6∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 6∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G13 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=c o s ( 6∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 6∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ;
123
y=s i n ( 6∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 6∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G14 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=c o s ( 7∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 7∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 7∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 7∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G15 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=c o s ( 7∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 7∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 7∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 7∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G16 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=c o s ( 8∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 8∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 8∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 8∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G17 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=c o s ( 8∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 8∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 8∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 8∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G18 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=c o s ( 9∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 9∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 9∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 9∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G19 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=c o s ( 9∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 9∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 9∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 9∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G20 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=c o s ( 1 0∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 1 0∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 1 0∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 1 0∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G21 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=c o s ( 1 0∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 1 0∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 1 0∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 1 0∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G22 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=c o s ( 1 1∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 1 1∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 1 1∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 1 1∗ p i /6)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G23 ( t =15∗ p i / 1 2 , 1 1∗ p i / 1 2 ) { x=c o s ( 1 1∗ p i / 6 )∗( cx+r∗ c o s ( t ))− s i n ( 1 1∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 1 1∗ p i / 6 )∗( cx+r∗ c o s ( t ))+ c o s ( 1 1∗ p i / 6 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G24 ( t =11∗ p i / 1 2 , 1 5∗ p i / 1 2 ) { x=cx+r ∗ c o s ( t ) ; y=−cy−r∗ s i n ( t ) ; } ;
p l o t (G1( n)+G2( n)+G3( n)+G4( n)+G5( n)+G6( n)+G7( n)+G8( n)+G9( n)+G10 ( n)+G11 ( n)+G12 ( n)+G13 ( n )
+G14 ( n)+G15 ( n)+G16 ( n)+G17 ( n)+G18 ( n)+G19 ( n)+G20 ( n)+G21 ( n)+G22 ( n)+G23 ( n)+G24 ( n ) ) ;
mesh Th =b u i l d m e s h (G1( n)+G2( n)+G3( n)+G4( n)+G5( n)+G6( n)+G7( n)+G8( n)+G9( n)+G10 ( n)+G11 ( n )
+G12 ( n)+G13 ( n)+G14 ( n)+G15 ( n)+G16 ( n)+G17 ( n)+G18 ( n)+G19 ( n)+G20 ( n)+G21 ( n)+G22 ( n)+G23 ( n )
+G24 ( n ) , f i x e b o r d e r=true ) ;
p l o t ( Th , w a i t=true , f i l l = true ) ;
f e s p a c e Vh( Th , P2 , p e r i o d i c = [ [ 2 , ( c o s ( p i / 1 2 ) )∗ ( y−y02 )−( s i n ( p i / 1 2 ) )∗ ( x−x02 ) ] ,
[ 9 , ( c o s ( 3∗ p i / 1 2 ) )∗ ( y−y09 )−( s i n (−3∗ p i / 1 2 ) )∗ ( x−x09 ) ] ,
[ 4 , ( c o s ( 3∗ p i / 1 2 ) )∗ ( y−y04 )−( s i n ( 3∗ p i / 1 2 ) )∗ ( x−x04 ) ] ,
[ 1 1 , ( c o s ( p i / 1 2 ) )∗ ( y−y11 )−( s i n (−p i / 1 2 ) )∗ ( x−x11 ) ] ,
[ 6 , ( c o s ( 5∗ p i / 1 2 ) )∗ ( y−y06 )−( s i n ( 5∗ p i / 1 2 ) )∗ ( x−x06 ) ] ,
[ 1 3 , ( c o s ( p i / 1 2 ) )∗ ( y−y13 )−( s i n ( p i / 1 2 ) )∗ ( x−x13 ) ] ,
[ 8 , ( c o s ( 7∗ p i / 1 2 ) )∗ ( y−y08 )−( s i n ( 7∗ p i / 1 2 ) )∗ ( x−x08 ) ] ,
[ 1 5 , ( c o s ( 3∗ p i / 1 2 ) )∗ ( y−y15 )−( s i n ( 3∗ p i / 1 2 ) )∗ ( x−x15 ) ] ,
[ 1 0 , ( c o s ( 9∗ p i / 1 2 ) )∗ ( y−y10 )−( s i n ( 9∗ p i / 1 2 ) )∗ ( x−x10 ) ] ,
[ 1 7 , ( c o s ( 5∗ p i / 1 2 ) )∗ ( y−y17 )−( s i n ( 5∗ p i / 1 2 ) )∗ ( x−x17 ) ] ,
[ 1 2 , ( c o s ( 1 1∗ p i / 1 2 ) )∗ ( y−y12 )−( s i n ( 1 1∗ p i / 1 2 ) )∗ ( x−x12 ) ] ,
[ 1 9 , ( c o s ( 7∗ p i / 1 2 ) )∗ ( y−y19 )−( s i n ( 7∗ p i / 1 2 ) )∗ ( x−x19 ) ] ,
[ 1 4 , ( c o s ( 1 3∗ p i / 1 2 ) )∗ ( y−y14 )−( s i n ( 1 3∗ p i / 1 2 ) )∗ ( x−x14 ) ] ,
[ 2 1 , ( c o s ( 9∗ p i / 1 2 ) )∗ ( y−y21 )−( s i n ( 9∗ p i / 1 2 ) )∗ ( x−x21 ) ] ,
[ 1 6 , ( c o s ( 1 5∗ p i / 1 2 ) )∗ ( y−y16 )−( s i n ( 1 5∗ p i / 1 2 ) )∗ ( x−x16 ) ] ,
[ 2 3 , ( c o s ( 1 1∗ p i / 1 2 ) )∗ ( y−y23 )−( s i n ( 1 1∗ p i / 1 2 ) )∗ ( x−x23 ) ] ,
[ 1 8 , ( c o s ( 1 7∗ p i / 1 2 ) )∗ ( y−y18 )−( s i n ( 1 7∗ p i / 1 2 ) )∗ ( x−x18 ) ] ,
[ 1 , ( c o s ( 1 3∗ p i / 1 2 ) )∗ ( y−y01 )−( s i n ( 1 3∗ p i / 1 2 ) )∗ ( x−x01 ) ] ,
[ 2 0 , ( c o s ( 1 9∗ p i / 1 2 ) )∗ ( y−y20 )−( s i n ( 1 9∗ p i / 1 2 ) )∗ ( x−x20 ) ] ,
[ 3 , ( c o s ( 1 5∗ p i / 1 2 ) )∗ ( y−y03 )−( s i n ( 1 5∗ p i / 1 2 ) )∗ ( x−x03 ) ] ,
[ 2 2 , ( c o s ( 2 1∗ p i / 1 2 ) )∗ ( y−y22 )−( s i n ( 2 1∗ p i / 1 2 ) )∗ ( x−x22 ) ] ,
[ 5 , ( c o s ( 1 7∗ p i / 1 2 ) )∗ ( y−y05 )−( s i n ( 1 7∗ p i / 1 2 ) )∗ ( x−x05 ) ] ,
[ 2 4 , ( c o s ( 2 3∗ p i / 1 2 ) )∗ ( y−y24 )−( s i n ( 2 3∗ p i / 1 2 ) )∗ ( x−x24 ) ] ,
[ 7 , ( c o s ( 1 9∗ p i / 1 2 ) )∗ ( y−y07 )−( s i n ( 1 9∗ p i / 1 2 ) )∗ ( x−x07 ) ] ] ) ;
Vh u1 , u2 ;
r e a l sigma = 0 . 0 0 0 0 1 ;
v a r f op ( u1 , u2)= i n t 2 d (Th ) ( dx ( u1 )∗ dx ( u2)+ dy ( u1 )∗ dy ( u2)− sigma∗( 4∗ u1∗u2 )/(1−x^2−y ^ 2 ) ^ 2 ) ;
v a r f b ( [ u1 ] , [ u2 ] ) = i n t 2 d (Th ) ( ( 4 ∗ u1∗u2 )/(1−x^2−y ^ 2 ) ^ 2 ) ;
m a t r i x OP = op (Vh , Vh , s o l v e r=Crout , f a c t o r i z e = 1 ) ;
m a t r i x B =b (Vh , Vh , s o l v e r= CG, e p s=1e−2 0 ) ;
r e a l [ i n t] ev ( nev ) ;
124
Vh [i n t] eV ( nev ) ;
i n t k=E i g e n V a l u e (OP, B , sym=true , sigma=sigma , v a l u e=ev , v e c t o r=eV , t o l =1e−10 , maxit =0 , ncv = 0 ) ;
f o r ( i n t i =0; i <k ; i ++) {
u1=eV [ i ] ;
r e a l gg = i n t 2 d (Th ) ( dx ( u1 ) ∗ dx ( u1 ) + dy ( u1 )∗ dy ( u1 ) ) ; r e a l m m = i n t 2 d (Th ) ( u1∗u1 ) ;
o f s t r e a m Eva ( fnm , append ) ;
Eva < < ev [ i ] < < " \n" ;
}
1
3
5
7
9
11
13
15
17
19
21
23
24
2
4
6
8
10
12
14
16
18
20
22
Side associations:
2 – 9, 4 – 11, 6 – 13, 8 – 15, 10 – 17, 12 – 19,
14 – 21, 16 – 23, 18 – 1, 20 – 3, 22 – 5, 24 – 7
Figure D.1: Fundamental polygon for the surfaceM3
We also include the code for the Fermat quartic:
i n t n =30;
i n t nev =100;
s t r i n g fnm=" f e r m a t _ q u a r t i c−E i g e n v a l u e s−n30−nev100 . t x t " ; // f i l e name f o r s a v i n g
r e a l cx = 1 . 0 0 4 4 ;
r e a l cy = 0 . 2 2 7 5 ;
r e a l r = 0 . 2 4 6 3 ;
r e a l s = 0 . 7 8 8 1 ;
r e a l t h e t a = 0 . 1 6 9 8 ;
r e a l x01=s ∗ c o s ( t h e t a ) ;
r e a l y01=s ∗ s i n ( t h e t a ) ;
r e a l x06=s ∗ c o s ( 3∗ p i /4−t h e t a ) ;
r e a l y06=s ∗ s i n ( 3∗ p i /4−t h e t a ) ;
125
r e a l x03=s ∗ c o s ( p i /4+ t h e t a ) ;
r e a l y03=s ∗ s i n ( p i /4+ t h e t a ) ;
r e a l x08=s ∗ c o s ( p i−t h e t a ) ;
r e a l y08=s ∗ s i n ( p i−t h e t a ) ;
r e a l x05=s ∗ c o s ( p i /2+ t h e t a ) ;
r e a l y05=s ∗ s i n ( p i /2+ t h e t a ) ;
r e a l x10=s ∗ c o s ( 5∗ p i /4−t h e t a ) ;
r e a l y10=s ∗ s i n ( 5∗ p i /4−t h e t a ) ;
r e a l x07=s ∗ c o s ( 3∗ p i /4+ t h e t a ) ;
r e a l y07=s ∗ s i n ( 3∗ p i /4+ t h e t a ) ;
r e a l x12=s ∗ c o s ( 6∗ p i /4−t h e t a ) ;
r e a l y12=s ∗ s i n ( 6∗ p i /4−t h e t a ) ;
r e a l x09=s ∗ c o s ( p i+t h e t a ) ;
r e a l y09=s ∗ s i n ( p i+t h e t a ) ;
r e a l x14=s ∗ c o s ( 7∗ p i /4−t h e t a ) ;
r e a l y14=s ∗ s i n ( 7∗ p i /4−t h e t a ) ;
r e a l x11=s ∗ c o s ( 5∗ p i /4+ t h e t a ) ;
r e a l y11=s ∗ s i n ( 5∗ p i /4+ t h e t a ) ;
r e a l x16=s ∗ c o s ( t h e t a ) ;
r e a l y16=s ∗ s i n (−t h e t a ) ;
r e a l x13=s ∗ c o s ( 6∗ p i /4+ t h e t a ) ;
r e a l y13=s ∗ s i n ( 6∗ p i /4+ t h e t a ) ;
r e a l x02=s ∗ c o s ( p i /4−t h e t a ) ;
r e a l y02=s ∗ s i n ( p i /4−t h e t a ) ;
r e a l x15=s ∗ c o s ( 7∗ p i /4+ t h e t a ) ;
r e a l y15=s ∗ s i n ( 7∗ p i /4+ t h e t a ) ;
r e a l x04=s ∗ c o s ( p i /2−t h e t a ) ;
r e a l y04=s ∗ s i n ( p i /2−t h e t a ) ;
b o r d e r G1 ( t =11∗ p i / 8 , 7∗ p i / 8 ) { x=cx+r ∗ c o s ( t ) ; y=cy+r∗ s i n ( t ) ; } ;
b o r d e r G2 ( t =7∗p i / 8 , 1 1∗ p i / 8 ) { x=c o s ( p i / 4 )∗( cx+r∗ c o s ( t ))− s i n ( p i /4)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( p i / 4 )∗( cx+r∗ c o s ( t ))+ c o s ( p i /4)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G3 ( t =11∗ p i / 8 , 7∗ p i / 8 ) { x=c o s ( p i / 4 )∗( cx+r∗ c o s ( t ))− s i n ( p i / 4 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( p i / 4 )∗( cx+r∗ c o s ( t ))+ c o s ( p i / 4 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G4 ( t =7∗p i / 8 , 1 1∗ p i / 8 ) { x=c o s ( p i / 2 )∗( cx+r∗ c o s ( t ))− s i n ( p i /2)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( p i / 2 )∗( cx+r∗ c o s ( t ))+ c o s ( p i /2)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G5 ( t =11∗ p i / 8 , 7∗ p i / 8 ) { x=c o s ( p i / 2 )∗( cx+r∗ c o s ( t ))− s i n ( p i / 2 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( p i / 2 )∗( cx+r∗ c o s ( t ))+ c o s ( p i / 2 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G6 ( t =7∗p i / 8 , 1 1∗ p i / 8 ) { x=c o s ( 3∗ p i / 4 )∗( cx+r∗ c o s ( t ))− s i n ( 3∗ p i /4)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 3∗ p i / 4 )∗( cx+r∗ c o s ( t ))+ c o s ( 3∗ p i /4)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G7 ( t =11∗ p i / 8 , 7∗ p i / 8 ) { x=c o s ( 3∗ p i / 4 )∗( cx+r∗ c o s ( t ))− s i n ( 3∗ p i / 4 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 3∗ p i / 4 )∗( cx+r∗ c o s ( t ))+ c o s ( 3∗ p i / 4 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G8 ( t =7∗p i / 8 , 1 1∗ p i / 8 ) { x=c o s ( p i )∗ ( cx+r∗ c o s ( t ))− s i n ( p i )∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( p i )∗ ( cx+r∗ c o s ( t ))+ c o s ( p i )∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G9 ( t =11∗ p i / 8 , 7∗ p i / 8 ) { x=c o s ( p i )∗ ( cx+r∗ c o s ( t ))− s i n ( p i )∗ ( cy+r∗ s i n ( t ) ) ;
y=s i n ( p i )∗ ( cx+r∗ c o s ( t ))+ c o s ( p i )∗ ( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G10 ( t =7∗p i / 8 , 1 1∗ p i / 8 ) { x=c o s ( 5∗ p i / 4 )∗( cx+r∗ c o s ( t ))− s i n ( 5∗ p i /4)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 5∗ p i / 4 )∗( cx+r∗ c o s ( t ))+ c o s ( 5∗ p i /4)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G11 ( t =11∗ p i / 8 , 7∗ p i / 8 ) { x=c o s ( 5∗ p i / 4 )∗( cx+r∗ c o s ( t ))− s i n ( 5∗ p i / 4 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 5∗ p i / 4 )∗( cx+r∗ c o s ( t ))+ c o s ( 5∗ p i / 4 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G12 ( t =7∗p i / 8 , 1 1∗ p i / 8 ) { x=c o s ( 6∗ p i / 4 )∗( cx+r∗ c o s ( t ))− s i n ( 6∗ p i /4)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 6∗ p i / 4 )∗( cx+r∗ c o s ( t ))+ c o s ( 6∗ p i /4)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G13 ( t =11∗ p i / 8 , 7∗ p i / 8 ) { x=c o s ( 6∗ p i / 4 )∗( cx+r∗ c o s ( t ))− s i n ( 6∗ p i / 4 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 6∗ p i / 4 )∗( cx+r∗ c o s ( t ))+ c o s ( 6∗ p i / 4 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G14 ( t =7∗p i / 8 , 1 1∗ p i / 8 ) { x=c o s ( 7∗ p i / 4 )∗( cx+r∗ c o s ( t ))− s i n ( 7∗ p i /4)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 7∗ p i / 4 )∗( cx+r∗ c o s ( t ))+ c o s ( 7∗ p i /4)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G15 ( t =11∗ p i / 8 , 7∗ p i / 8 ) { x=c o s ( 7∗ p i / 4 )∗( cx+r∗ c o s ( t ))− s i n ( 7∗ p i / 4 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 7∗ p i / 4 )∗( cx+r∗ c o s ( t ))+ c o s ( 7∗ p i / 4 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G16 ( t =7∗p i / 8 , 1 1∗ p i / 8 ) { x=cx+r ∗ c o s ( t ) ; y=−cy−r∗ s i n ( t ) ; } ;
p l o t (G1( n)+G2( n)+G3( n)+G4( n)+G5( n)+G6( n)+G7( n)+G8( n)+G9( n)+G10 ( n)+G11 ( n)+G12 ( n)+G13 ( n )
+G14 ( n)+G15 ( n)+G16 ( n ) ) ;
mesh Th =b u i l d m e s h (G1( n)+G2( n)+G3( n)+G4( n)+G5( n)+G6( n)+G7( n)+G8( n)+G9( n)+G10 ( n)+G11 ( n )
+G12 ( n)+G13 ( n)+G14 ( n)+G15 ( n)+G16 ( n ) , f i x e b o r d e r=true ) ;
126
p l o t ( Th , w a i t=true , f i l l = true ) ;
f e s p a c e Vh( Th , P2 , p e r i o d i c = [ [ 1 , c o s ( p i / 8 )∗( y−y01)− s i n ( p i / 8 )∗( x−x01 ) ] ,
[ 6 , c o s ( 3∗ p i / 8 )∗( y−y06)− s i n (−3∗ p i / 8 )∗( x−x06 ) ] ,
[ 3 , c o s ( 3∗ p i / 8 )∗( y−y03)− s i n ( 3∗ p i / 8 )∗( x−x03 ) ] ,
[ 8 , c o s ( p i / 8 )∗( y−y08)− s i n (−p i / 8 )∗( x−x08 ) ] ,
[ 5 , c o s ( 5∗ p i / 8 )∗( y−y05)− s i n ( 5∗ p i / 8 )∗( x−x05 ) ] ,
[ 1 0 , c o s ( p i / 8 )∗( y−y10)− s i n ( p i / 8 )∗( x−x10 ) ] ,
[ 7 , c o s ( 7∗ p i / 8 )∗( y−y07)− s i n ( 7∗ p i / 8 )∗( x−x07 ) ] ,
[ 1 2 , c o s ( 3∗ p i / 8 )∗( y−y12)− s i n ( 3∗ p i / 8 )∗( x−x12 ) ] ,
[ 9 , c o s ( 9∗ p i / 8 )∗( y−y09)− s i n ( 9∗ p i / 8 )∗( x−x09 ) ] ,
[ 1 4 , c o s ( 5∗ p i / 8 )∗( y−y14)− s i n ( 5∗ p i / 8 )∗( x−x14 ) ] ,
[ 1 1 , c o s ( 1 1∗ p i / 8 )∗( y−y11)− s i n ( 1 1∗ p i / 8 )∗( x−x11 ) ] ,
[ 1 6 , c o s ( 7∗ p i / 8 )∗( y−y16)− s i n ( 7∗ p i / 8 )∗( x−x16 ) ] ,
[ 1 3 , c o s ( 1 3∗ p i / 8 )∗( y−y13)− s i n ( 1 3∗ p i / 8 )∗( x−x13 ) ] ,
[ 2 , c o s ( 9∗ p i / 8 )∗( y−y02)− s i n ( 9∗ p i / 8 )∗( x−x02 ) ] ,
[ 1 5 , c o s ( 1 5∗ p i / 8 )∗( y−y15)− s i n ( 1 5∗ p i / 8 )∗( x−x15 ) ] ,
[ 4 , c o s ( 1 1∗ p i / 8 )∗( y−y04)− s i n ( 1 1∗ p i / 8 )∗( x−x04 ) ] ] ) ;
Vh u1 , u2 ;
r e a l sigma = 0 . 0 0 0 0 1 ;
v a r f op ( u1 , u2)= i n t 2 d (Th ) ( dx ( u1 )∗ dx ( u2)+ dy ( u1 )∗ dy ( u2)− sigma∗( 4∗ u1∗u2 )/(1−x^2−y ^ 2 ) ^ 2 ) ;
v a r f b ( [ u1 ] , [ u2 ] ) = i n t 2 d (Th ) ( ( 4 ∗ u1∗u2 )/(1−x^2−y ^ 2 ) ^ 2 ) ;
m a t r i x OP = op (Vh , Vh , s o l v e r=Crout , f a c t o r i z e = 1 ) ;
m a t r i x B =b (Vh , Vh , s o l v e r= CG, e p s=1e−2 0 ) ;
r e a l [ i n t] ev ( nev ) ;
Vh [i n t] eV ( nev ) ;
i n t k=E i g e n V a l u e (OP, B , sym=true , sigma=sigma , v a l u e=ev , v e c t o r=eV , t o l =1e−10 , maxit =0 , ncv = 0 ) ;
f o r ( i n t i =0; i <k ; i ++) {
u1=eV [ i ] ;
r e a l gg = i n t 2 d (Th ) ( dx ( u1 ) ∗ dx ( u1 ) + dy ( u1 )∗ dy ( u1 ) ) ; r e a l m m = i n t 2 d (Th ) ( u1∗u1 ) ;
o f s t r e a m Eva ( fnm , append ) ;
Eva < < ev [ i ] < < " \n" ;
}
Remark D.1The observant reader will recognizeλ2 in Table D.3 - it is roughly equal to
the ﬁrst positive eigenvalue of the Bolza surface! Moreover, it appears to have the same
multiplicity. In fact, if one takes the subset of eigenvalues in Table D.3 with multiplicity
1, 2 or 3, one ﬁnds that they match the subset of eigenvalues of Table C.1, and that
the multiplicities are the same. This is no coincidence. Recall the presentation of the
automorphism group given in Chapter 1:
⟨a,b,c|a8 =b3 =c2 = (ab)2 = (a2b2)3 = (a4b2)3 =acac =bcbc =e⟩,
wherea is a rotation of order 8 around the centre of the fundamental 16-gon,b is a
rotation of order 3 around one of the 32(4, 4, 4) triangles that can be used to tessellate
the surface (note this is twice as many as in the case of the Bolza surface), andc is a
reﬂection in the real line. As we have done with the Bolza surface and Klein quartic, we
can input this presentation into GAP to get information about the structure of the group
127
1
3
5
7
9
11
13
15
16
2
4
6
8
10
12
14
Side associations:
1 – 6, 3 – 8, 5 – 10, 7 – 12,
9 – 14, 11 – 16, 13 – 2, 15 – 4
Figure D.2: Fundamental polygon for the Fermat quartic
and information about its representation theory. The code below indicates that the full
automorphism group is isomorphic to(((Z4× Z4) ⋊ Z3) ⋊ Z2) ⋊ Z2.
gap> g:=FreeGroup(3);
<free group on the generators [ f1 , f2 , f3 ]>
gap> f:=g/[g.1^8 ,g.2^3 ,g.3^2 ,(g.1 ∗g.2)^2 ,(g.1^2 ∗g.2^2)^3 ,(g.1^4 ∗g.2^2)^3,
g.1∗g.3∗g.1∗g.3 ,g.2 ∗g.3∗g.2∗g .3];
<fp group on the generators [ f1 , f2 , f3 ]>
gap> Order( f );
192
gap> StructureDescription ( f );
"(((C4xC4):C3):C2):C2"
gap> RequirePackage("repsn");
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
Repsn f o r Constructing Representations of Finite Groups
Version 3.0.2
Written by
Vahid Dabbaghian
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
true
gap> Display(CharacterTable( f ));
CT1
2 6 4 4 1 5 6 4 3 4 3 4 5 1 4
3 1 . . 1 . . 1 . . . . . 1 .
1a 2a 2b 3a 4a 2c 2d 8a 4b 8b 4c 4d 6a 2e
2P 1a 1a 1a 3a 2c 1a 1a 4d 2c 4a 2c 2c 3a 1a
3P 1a 2a 2b 1a 4a 2c 2d 8a 4b 8b 4c 4d 2d 2e
5P 1a 2a 2b 3a 4a 2c 2d 8a 4b 8b 4c 4d 6a 2e
128
7P 1a 2a 2b 3a 4a 2c 2d 8a 4b 8b 4c 4d 6a 2e
X.1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
X.2 1 −1−1 1 1 1 1 −1−1−1−1 1 1 1
X.3 1 −1 1 1 1 1 −1−1−1 1 1 1 −1−1
X.4 1 1 −1 1 1 1 −1 1 1 −1−1 1 −1−1
X.5 2 . . −1 2 2 −2 . . . . 2 1 −2
X.6 2 . . −1 2 2 2 . . . . 2 −1 2
X.7 3 −1−1 . −1 3 3 1 −1 1 −1−1 . −1
X.8 3 −1 1 . −1 3 −3 1 −1−1 1 −1 . 1
X.9 3 1 −1 . −1 3 −3−1 1 1 −1−1 . 1
X.10 3 1 1 . −1 3 3 −1 1 −1 1 −1 . −1
X.11 6 −2 . . 2 −2 . . 2 . . −2 . .
X.12 6 . −2 . −2−2 . . . . 2 2 . .
X.13 6 . 2 . −2−2 . . . . −2 2 . .
X.14 6 2 . . 2 −2 . . −2 . . −2 . .
gap> chi:=Irr ( f );;
gap> IrreducibleAffordingRepresentation (chi [1]);
[ f1 , f2 , f3 ] −> [ [ [ 1 ] ] , [ [ 1 ] ] , [ [ 1 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [2]);
[ f1 , f2 , f3 ] −> [ [ [ −1 ] ] , [ [ 1 ] ] , [ [ −1 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [3]);
[ f1 , f2 , f3 ] −> [ [ [ −1 ] ] , [ [ 1 ] ] , [ [ 1 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [4]);
[ f1 , f2 , f3 ] −> [ [ [ 1 ] ] , [ [ 1 ] ] , [ [ −1 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [5]);
[ f1 , f2 , f3 ] −> [ [ [ 0, −1 ] , [ −1, 0 ] ] , [ [ E(3)^2, 0 ] , [ 0, E(3) ] ] ,
[ [ 0, 1 ] , [ 1, 0 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [6]);
[ f1 , f2 , f3 ] −> [ [ [ 0, 1 ] , [ 1, 0 ] ] , [ [ E(3)^2, 0 ] , [ 0, E(3) ] ] ,
[ [ 0, 1 ] , [ 1, 0 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [7]);
[ f1 , f2 , f3 ] −> [ [ [ 0, 1, 0 ] , [ −1, 0, 0 ] , [ 0, 0, 1 ] ] ,
[ [ 0, 1, 0 ] , [ 0, 0, 1 ] , [ 1, 0, 0 ] ] ,
[ [ 0, −1, 0 ] , [ −1, 0, 0 ] , [ 0, 0, −1 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [8]);
[ f1 , f2 , f3 ] −> [ [ [ 0, 1, 0 ] , [ −1, 0, 0 ] , [ 0, 0, 1 ] ] ,
[ [ 0, 1, 0 ] , [ 0, 0, 1 ] , [ 1, 0, 0 ] ] ,
[ [ 0, 1, 0 ] , [ 1, 0, 0 ] , [ 0, 0, 1 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [9]);
[ f1 , f2 , f3 ] −> [ [ [ 0, −1, 0 ] , [ 1, 0, 0 ] , [ 0, 0, −1 ] ] ,
[ [ 0, 1, 0 ] , [ 0, 0, 1 ] , [ 1, 0, 0 ] ] ,
[ [ 0, −1, 0 ] , [ −1, 0, 0 ] , [ 0, 0, −1 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [10]);
[ f1 , f2 , f3 ] −> [ [ [ 0, −1, 0 ] , [ 1, 0, 0 ] , [ 0, 0, −1 ] ] ,
[ [ 0, 1, 0 ] , [ 0, 0, 1 ] , [ 1, 0, 0 ] ] ,
[ [ 0, 1, 0 ] , [ 1, 0, 0 ] , [ 0, 0, 1 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [11]);
[ f1 , f2 , f3 ] −>
[ [ [ 0, 1, 0, 0, 0, 0 ] , [ E(4) , 0, 0, 0, 0, 0 ] , [ 0, 0, E(4) , 0, 0, 0 ] ,
[ 0, 0, 0, 0, −E(4) , 0 ] , [ 0, 0, 0, 1, 0, 0 ] ,
[ 0, 0, 0, 0, 0, −E(4) ] ] ,
[ [ 0, 0, 1, 0, 0, 0 ] , [ −1, 0, 0, 0, 0, 0 ] , [ 0, −1, 0, 0, 0, 0 ] ,
[ 0, 0, 0, 0, −1, 0 ] , [ 0, 0, 0, 0, 0, −1 ] , [ 0, 0, 0, 1, 0, 0 ] ] ,
129
[ [ 0, 0, 0, 1, 0, 0 ] , [ 0, 0, 0, 0, 1, 0 ] , [ 0, 0, 0, 0, 0, 1 ] ,
[ 1, 0, 0, 0, 0, 0 ] , [ 0, 1, 0, 0, 0, 0 ] , [ 0, 0, 1, 0, 0, 0 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [12]);
[ f1 , f2 , f3 ] −>
[ [ [ 0, 0, 0, 1, 0, 0 ] , [ 0, 0, 0, 0, 1, 0 ] , [ 0, 0, 0, 0, 0, 1 ] ,
[ −E(4) , 0, 0, 0, 0, 0 ] , [ 0, 1, 0, 0, 0, 0 ] , [ 0, 0, E(4) , 0, 0, 0 ]
] , [ [ 0, 1, 0, 0, 0, 0 ] , [ 0, 0, 1, 0, 0, 0 ] , [ 1, 0, 0, 0, 0, 0 ] ,
[ 0, 0, 0, 0, 0, −E(4) ] , [ 0, 0, 0, E(4) , 0, 0 ] , [ 0, 0, 0, 0, 1, 0 ]
] ,
[ [ 0, 0, −1, 0, 0, 0 ] , [ 0, −1, 0, 0, 0, 0 ] , [ −1, 0, 0, 0, 0, 0 ] ,
[ 0, 0, 0, 0, 0, E(4) ] , [ 0, 0, 0, 0, −1, 0 ] ,
[ 0, 0, 0, −E(4) , 0, 0 ] ] ]
gap> IrreducibleAffordingRepresentation (chi [13]);
[ f1 , f2 , f3 ] −>
[ [ [ 0, 0, 0, 1, 0, 0 ] , [ 0, 0, 0, 0, 1, 0 ] , [ 0, 0, 0, 0, 0, 1 ] ,
[ −E(4) , 0, 0, 0, 0, 0 ] , [ 0, 1, 0, 0, 0, 0 ] , [ 0, 0, E(4) , 0, 0, 0 ]
] , [ [ 0, 1, 0, 0, 0, 0 ] , [ 0, 0, 1, 0, 0, 0 ] , [ 1, 0, 0, 0, 0, 0 ] ,
[ 0, 0, 0, 0, 0, −E(4) ] , [ 0, 0, 0, E(4) , 0, 0 ] , [ 0, 0, 0, 0, 1, 0 ]
] , [ [ 0, 0, 1, 0, 0, 0 ] , [ 0, 1, 0, 0, 0, 0 ] , [ 1, 0, 0, 0, 0, 0 ] ,
[ 0, 0, 0, 0, 0, −E(4) ] , [ 0, 0, 0, 0, 1, 0 ] , [ 0, 0, 0, E(4) , 0, 0 ]
] ]
gap> IrreducibleAffordingRepresentation (chi [14]);
[ f1 , f2 , f3 ] −>
[ [ [ 0, 1, 0, 0, 0, 0 ] , [ E(4) , 0, 0, 0, 0, 0 ] , [ 0, 0, −E(4) , 0, 0, 0 ] ,
[ 0, 0, 0, 0, −E(4) , 0 ] , [ 0, 0, 0, 1, 0, 0 ] , [ 0, 0, 0, 0, 0, E(4) ]
] , [ [ 0, 0, 1, 0, 0, 0 ] , [ 1, 0, 0, 0, 0, 0 ] , [ 0, 1, 0, 0, 0, 0 ] ,
[ 0, 0, 0, 0, 1, 0 ] , [ 0, 0, 0, 0, 0, 1 ] , [ 0, 0, 0, 1, 0, 0 ] ] ,
[ [ 0, 0, 0, 1, 0, 0 ] , [ 0, 0, 0, 0, 1, 0 ] , [ 0, 0, 0, 0, 0, 1 ] ,
[ 1, 0, 0, 0, 0, 0 ] , [ 0, 1, 0, 0, 0, 0 ] , [ 0, 0, 1, 0, 0, 0 ] ] ]
130
Eigenvalue Numerical multiplicity
2.6767 8
6.61848 7
10.8637 6
12.1775 8
17.2397 7
21.9563 7
24.0649 8
25.9085 6
30.7817 6
36.4369 8
37.4073 8
41.4847 6
44.8658 8
49.0165 6
50.6025 6
57.7794 8
57.8082 7
61.9464 7
67.7629 8
69.9676 6
71.0138 8
75.6357 6
81.8839 6
82.6094 7
89.4299 7
90.5087 8
92.7509 8
96.8869 6
Table D.1: First positive eigenvalues of the Klein Quartic
131
Eigenvalue Numerical multiplicity
2.45206 4
2.8381 3
4.35754 3
7.61965 4
8.45728 1
10.126 4
10.1635 3
11.76 3
14.1724 4
14.2628 2
17.6818 2
18.812 1
19.2547 3
21.2083 4
22.827 4
24.166 3
24.1744 4
26.9546 3
28.0159 1
28.3388 3
30.7729 4
35.8649 3
37.1106 3
37.3413 4
37.976 4
38.6914 3
38.9579 2
42.7433 3
44.0167 4
44.6724 4
46.6306 2
49.448 4
Table D.2: First positive eigenvalues of the surfaceM3
132
Eigenvalue Numerical multiplicity
2.4877 6
3.83889 3
7.16032 6
8.24958 2
11.4272 6
13.3096 6
15.049 3
18.6587 3
19.3559 6
23.0736 1
24.7216 6
27.0788 6
27.5915 6
28.0796 3
32.6738 1
36.1647 6
36.2386 2
38.8039 6
40.1168 3
44.0176 3
44.412 6
45.5628 6
Table D.3: First positive eigenvalues of the Fermat quartic
133
Appendix E
FreeFEM++ Code for Genus 4
Figure E.1: Fundamental polygon for Bring’s surface
The most symmetric surface of genus 4 is Bring’s surface (also referred to as Bring’s
curve) [71]. It can be obtained by associating the sides of a hyperbolic icosagon of
area 12π, as shown in Figure E.1. Similarly to the Bolza surface and Klein quartic, we
conjecture that because it has maximal symmetry among hyperbolic surfaces of genus 4,
it also maximizes the ﬁrst positive eigenvalue of the Laplace-Beltrami operator among
surfaces of this class. In this appendix, we provide a ﬁnite element code for computing the
ﬁrst 100 eigenvalues of Bring’s surface, along with the output, shown in Table E.1, which
134
lists the eigenvalues and their predicted multiplicities based on the numerical results.
The FreeFEM++ code follows the same style as that in earlier appendices; please refer
to Appendix C for comments on how to interpret it.
The fundamental polygon for Bring’s surface can be tessellated by 240(2, 4, 5) tri-
angles. The group actions that provide maps between the triangles in this tessellation
give the 240 symmetries of Bring’s surface. Note that this means Bring’s surface is not a
Hurwitz surface (recall Theorem 1.30), and that there does not exist a Hurwitz surface
of genus 4. The generators of the group satisfy the following relations
⟨r, s, t|r5 =s2 =t2 =rtrt =stst = (rs)4 = (sr3sr2)2 =e⟩,
wherer is rotation of order 5 about the center of the fundamental icosagon,s is rotation
of order 2 about a vertex where 4 triangles meet in the tessellation by(2, 4, 5)triangles,
andt is a reﬂection in the real line (see [71] for more details on this group). The ﬁnal
piece of code in this appendix shows analysis of this ﬁnitely presented group in GAP. In
particular, we see that it is isomorphic toS5× Z2, and show its character table.
i n t n = 3 0 ;
i n t nev = 1 0 0 ;
s t r i n g fnm=" b r i n g s−s u r f a c e−E i g e n v a l u e s−n30−nev100 . t x t " ; // f i l e name f o r s a v i n g
r e a l cx = 1 . 0 0 1 5 6 ;
r e a l cy = 0 . 1 7 1 7 8 ;
r e a l r = 0 . 1 8 0 6 2 1 ;
r e a l s = 0 . 8 3 7 8 4 3 ;
r e a l t h e t a = 0 . 1 3 8 8 5 5 ;
r e a l x01 = s ∗ c o s ( t h e t a ) ;
r e a l y01 = s ∗ s i n ( t h e t a ) ;
r e a l x02 = s ∗ c o s ( p i /5−t h e t a ) ;
r e a l y02 = s ∗ s i n ( p i /5−t h e t a ) ;
r e a l x03 = s ∗ c o s ( p i /5+ t h e t a ) ;
r e a l y03 = s ∗ s i n ( p i /5+ t h e t a ) ;
r e a l x04 = s ∗ c o s ( 2∗ p i /5−t h e t a ) ;
r e a l y04 = s ∗ s i n ( 2∗ p i /5−t h e t a ) ;
r e a l x05 = s ∗ c o s ( 2∗ p i /5+ t h e t a ) ;
r e a l y05 = s ∗ s i n ( 2∗ p i /5+ t h e t a ) ;
r e a l x06 = s ∗ c o s ( 3∗ p i /5−t h e t a ) ;
r e a l y06 = s ∗ s i n ( 3∗ p i /5−t h e t a ) ;
r e a l x07 = s ∗ c o s ( 3∗ p i /5+ t h e t a ) ;
r e a l y07 = s ∗ s i n ( 3∗ p i /5+ t h e t a ) ;
r e a l x08 = s ∗ c o s ( 4∗ p i /5−t h e t a ) ;
r e a l y08 = s ∗ s i n ( 4∗ p i /5−t h e t a ) ;
r e a l x09 = s ∗ c o s ( 4∗ p i /5+ t h e t a ) ;
r e a l y09 = s ∗ s i n ( 4∗ p i /5+ t h e t a ) ;
r e a l x10 = s ∗ c o s ( 5∗ p i /5−t h e t a ) ;
r e a l y10 = s ∗ s i n ( 5∗ p i /5−t h e t a ) ;
r e a l x11 = s ∗ c o s ( 5∗ p i /5+ t h e t a ) ;
r e a l y11 = s ∗ s i n ( 5∗ p i /5+ t h e t a ) ;
r e a l x12 = s ∗ c o s ( 6∗ p i /5−t h e t a ) ;
r e a l y12 = s ∗ s i n ( 6∗ p i /5−t h e t a ) ;
r e a l x13 = s ∗ c o s ( 6∗ p i /5+ t h e t a ) ;
r e a l y13 = s ∗ s i n ( 6∗ p i /5+ t h e t a ) ;
r e a l x14 = s ∗ c o s ( 7∗ p i /5−t h e t a ) ;
r e a l y14 = s ∗ s i n ( 7∗ p i /5−t h e t a ) ;
135
r e a l x15 = s ∗ c o s ( 7∗ p i /5+ t h e t a ) ;
r e a l y15 = s ∗ s i n ( 7∗ p i /5+ t h e t a ) ;
r e a l x16 = s ∗ c o s ( 8∗ p i /5−t h e t a ) ;
r e a l y16 = s ∗ s i n ( 8∗ p i /5−t h e t a ) ;
r e a l x17 = s ∗ c o s ( 8∗ p i /5+ t h e t a ) ;
r e a l y17 = s ∗ s i n ( 8∗ p i /5+ t h e t a ) ;
r e a l x18 = s ∗ c o s ( 9∗ p i /5−t h e t a ) ;
r e a l y18 = s ∗ s i n ( 9∗ p i /5−t h e t a ) ;
r e a l x19 = s ∗ c o s ( 9∗ p i /5+ t h e t a ) ;
r e a l y19 = s ∗ s i n ( 9∗ p i /5+ t h e t a ) ;
r e a l x20 = s ∗ c o s ( t h e t a ) ;
r e a l y20 = s ∗ s i n (−t h e t a ) ;
b o r d e r G1 ( t =7∗p i / 5 , 4∗ p i / 5 ) { x=cx+r ∗ c o s ( t ) ; y=cy+r∗ s i n ( t ) ; } ;
b o r d e r G2 ( t =4∗p i / 5 , 7∗ p i / 5 ) { x=c o s ( p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( p i /5)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( p i /5)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G3 ( t =7∗p i / 5 , 4∗ p i / 5 ) { x=c o s ( p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( p i / 5 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( p i / 5 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G4 ( t =4∗p i / 5 , 7∗ p i / 5 ) { x=c o s ( 2∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 2∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 2∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 2∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G5 ( t =7∗p i / 5 , 4∗ p i / 5 ) { x=c o s ( 2∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 2∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 2∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 2∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G6 ( t =4∗p i / 5 , 7∗ p i / 5 ) { x=c o s ( 3∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 3∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 3∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 3∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G7 ( t =7∗p i / 5 , 4∗ p i / 5 ) { x=c o s ( 3∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 3∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 3∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 3∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G8 ( t =4∗p i / 5 , 7∗ p i / 5 ) { x=c o s ( 4∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 4∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 4∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 4∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G9 ( t =7∗p i / 5 , 4∗ p i / 5 ) { x=c o s ( 4∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 4∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 4∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 4∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G10 ( t =4∗p i / 5 , 7∗ p i / 5 ) { x=c o s ( p i )∗ ( cx+r∗ c o s ( t ))− s i n ( p i )∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( p i )∗ ( cx+r∗ c o s ( t ))+ c o s ( p i )∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G11 ( t =7∗p i / 5 , 4∗ p i / 5 ) { x=c o s ( p i )∗ ( cx+r∗ c o s ( t ))− s i n ( p i )∗ ( cy+r∗ s i n ( t ) ) ;
y=s i n ( p i )∗ ( cx+r∗ c o s ( t ))+ c o s ( p i )∗ ( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G12 ( t =4∗p i / 5 , 7∗ p i / 5 ) { x=c o s ( 6∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 6∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 6∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 6∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G13 ( t =7∗p i / 5 , 4∗ p i / 5 ) { x=c o s ( 6∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 6∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 6∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 6∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G14 ( t =4∗p i / 5 , 7∗ p i / 5 ) { x=c o s ( 7∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 7∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 7∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 7∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G15 ( t =7∗p i / 5 , 4∗ p i / 5 ) { x=c o s ( 7∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 7∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 7∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 7∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G16 ( t =4∗p i / 5 , 7∗ p i / 5 ) { x=c o s ( 8∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 8∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 8∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 8∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G17 ( t =7∗p i / 5 , 4∗ p i / 5 ) { x=c o s ( 8∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 8∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 8∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 8∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G18 ( t =4∗p i / 5 , 7∗ p i / 5 ) { x=c o s ( 9∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 9∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ;
y=s i n ( 9∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 9∗ p i /5)∗(−cy−r∗ s i n ( t ) ) ; } ;
b o r d e r G19 ( t =7∗p i / 5 , 4∗ p i / 5 ) { x=c o s ( 9∗ p i / 5 )∗( cx+r∗ c o s ( t ))− s i n ( 9∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ;
y=s i n ( 9∗ p i / 5 )∗( cx+r∗ c o s ( t ))+ c o s ( 9∗ p i / 5 )∗( cy+r∗ s i n ( t ) ) ; } ;
b o r d e r G20 ( t =4∗p i / 5 , 7∗ p i / 5 ) { x=cx+r ∗ c o s ( t ) ; y=−cy−r∗ s i n ( t ) ; } ;
p l o t (G1( n)+G2( n)+G3( n)+G4( n)+G5( n)+G6( n)+G7( n)+G8( n)+G9( n)+G10 ( n)+G11 ( n)+G12 ( n)+G13 ( n )
+G14 ( n)+G15 ( n)+G16 ( n)+G17 ( n)+G18 ( n)+G19 ( n)+G20 ( n ) ) ; mesh
Th =b u i l d m e s h (G1( n)+G2( n)+G3( n)+G4( n)+G5( n)+G6( n)+G7( n)+G8( n)+G9( n)+G10 ( n)+G11 ( n)+G12 ( n )
+G13 ( n)+G14 ( n)+G15 ( n)+G16 ( n)+G17 ( n)+G18 ( n)+G19 ( n)+G20 ( n ) , f i x e b o r d e r=true ) ;
p l o t ( Th , w a i t=true , f i l l = true ) ;
f e s p a c e Vh( Th , P2 , p e r i o d i c = [ [ 1 , ( c o s ( p i / 1 0 ) )∗ ( y−y01 )−( s i n ( p i / 1 0 ) )∗ ( x−x01 ) ] ,
[ 1 4 , ( c o s ( 3∗ p i / 1 0 ) )∗ ( y−y14 )−( s i n ( 3∗ p i / 1 0 ) )∗ ( x−x14 ) ] ,
[ 3 , ( c o s ( 3∗ p i / 1 0 ) )∗ ( y−y03 )−( s i n ( 3∗ p i / 1 0 ) )∗ ( x−x03 ) ] ,
[ 1 2 , ( c o s ( p i / 1 0 ) )∗ ( y−y12 )−( s i n ( p i / 1 0 ) )∗ ( x−x12 ) ] ,
[ 5 , ( c o s ( 5∗ p i / 1 0 ) )∗ ( y−y05 )−( s i n ( 5∗ p i / 1 0 ) )∗ ( x−x05 ) ] ,
[ 1 8 , ( c o s ( 7∗ p i / 1 0 ) )∗ ( y−y18 )−( s i n ( 7∗ p i / 1 0 ) )∗ ( x−x18 ) ] ,
136
[ 7 , ( c o s ( 7∗ p i / 1 0 ) )∗ ( y−y07 )−( s i n ( 7∗ p i / 1 0 ) )∗ ( x−x07 ) ] ,
[ 1 6 , ( c o s ( 5∗ p i / 1 0 ) )∗ ( y−y16 )−( s i n ( 5∗ p i / 1 0 ) )∗ ( x−x16 ) ] ,
[ 9 , ( c o s ( 9∗ p i / 1 0 ) )∗ ( y−y09 )−( s i n ( 9∗ p i / 1 0 ) )∗ ( x−x09 ) ] ,
[ 2 , ( c o s ( 1 1∗ p i / 1 0 ) )∗ ( y−y02 )−( s i n ( 1 1∗ p i / 1 0 ) )∗ ( x−x02 ) ] ,
[ 1 1 , ( c o s ( 1 1∗ p i / 1 0 ) )∗ ( y−y11 )−( s i n ( 1 1∗ p i / 1 0 ) )∗ ( x−x11 ) ] ,
[ 2 0 , ( c o s ( 9∗ p i / 1 0 ) )∗ ( y−y20 )−( s i n ( 9∗ p i / 1 0 ) )∗ ( x−x20 ) ] ,
[ 1 3 , ( c o s ( 1 3∗ p i / 1 0 ) )∗ ( y−y13 )−( s i n ( 1 3∗ p i / 1 0 ) )∗ ( x−x13 ) ] ,
[ 6 , ( c o s ( 1 5∗ p i / 1 0 ) )∗ ( y−y06 )−( s i n ( 1 5∗ p i / 1 0 ) )∗ ( x−x06 ) ] ,
[ 1 5 , ( c o s ( 1 5∗ p i / 1 0 ) )∗ ( y−y15 )−( s i n ( 1 5∗ p i / 1 0 ) )∗ ( x−x15 ) ] ,
[ 4 , ( c o s ( 1 3∗ p i / 1 0 ) )∗ ( y−y04 )−( s i n ( 1 3∗ p i / 1 0 ) )∗ ( x−x04 ) ] ,
[ 1 7 , ( c o s ( 1 7∗ p i / 1 0 ) )∗ ( y−y17 )−( s i n ( 1 7∗ p i / 1 0 ) )∗ ( x−x17 ) ] ,
[ 1 0 , ( c o s ( 1 9∗ p i / 1 0 ) )∗ ( y−y10 )−( s i n ( 1 9∗ p i / 1 0 ) )∗ ( x−x10 ) ] ,
[ 1 9 , ( c o s ( 1 9∗ p i / 1 0 ) )∗ ( y−y19 )−( s i n ( 1 9∗ p i / 1 0 ) )∗ ( x−x19 ) ] ,
[ 8 , ( c o s ( 1 7∗ p i / 1 0 ) )∗ ( y−y08 )−( s i n ( 1 7∗ p i / 1 0 ) )∗ ( x−x08 ) ] ] ) ;
Vh u1 , u2 ;
r e a l sigma = 0 . 0 0 0 0 1 ;
v a r f op ( u1 , u2)= i n t 2 d (Th ) ( dx ( u1 )∗ dx ( u2)+ dy ( u1 )∗ dy ( u2)− sigma∗ u1∗u2 ) ;
v a r f b ( [ u1 ] , [ u2 ] ) = i n t 2 d (Th ) ( ( 4 ∗ u1∗u2 )/(1−x^2−y ^ 2 ) ^ 2 ) ;
m a t r i x OP = op (Vh , Vh , s o l v e r=Crout , f a c t o r i z e = 1 ) ;
m a t r i x B =b (Vh , Vh , s o l v e r= CG, e p s=1e−2 0 ) ;
r e a l [ i n t] ev ( nev ) ;
Vh [i n t] eV ( nev ) ;
i n t k=E i g e n V a l u e (OP, B , sym=true , sigma=sigma , v a l u e=ev , v e c t o r=eV , t o l =1e−10 , maxit =0 , ncv = 0 ) ;
f o r ( i n t i =0; i <k ; i ++) {
u1=eV [ i ] ;
r e a l gg = i n t 2 d (Th ) ( dx ( u1 ) ∗ dx ( u1 ) + dy ( u1 )∗ dy ( u1 ) ) ; r e a l m m = i n t 2 d (Th ) ( u1∗u1 ) ;
// cout < <"−−−−" < < i < <"" < <ev [ i ]<<" e r r="
// < <i n t 2 d (Th)(4/(1−x^2−y ^2)^2) < < " −−−" < <e n d l ; p l o t (eV [ i ] ,c m m ="Eigen Vector "+ i +" v a l e u r ="
+ ev [ i ] , w a i t =1 , v a l u e = 1 ) ;
o f s t r e a m Eva ( fnm , append ) ;
Eva < < ev [ i ] < < " \n" ;
}
The following shows the GAP analysis of the symmetry group of Bring’s surface.
Please refer to Appendix A for details on how to interpret this code.
gap> f:=FreeGroup(3);
<free group on the generators [ f1 , f2 , f3 ]>
gap> g:=f /[ f .1^5 , f .2^2 , f .3^2 , f .1∗f .3∗f .1∗f .3 , f .2∗f .3∗f .2∗f .3 ,
( f .1∗f .2)^4 ,( f .2∗f .1^3∗f .2∗f .1^2)^2];
<fp group on the generators [ f1 , f2 , f3 ]>
gap> Order(g);
240
gap> StructureDescription (g);
"C2/uni2423x/uni2423S5"
gap> RequirePackage("repsn" );;
gap> Display(CharacterTable(g));
CT1
2 4 3 4 2 3 2 1 3 2 3 2 1 4 4
3 1 1 . 1 1 1 . . 1 . 1 . . 1
5 1 . . . . . 1 . . . . 1 . 1
137
1a 2a 2b 6a 2c 3a 5a 4a 6b 4b 6c 10a 2d 2e
2P 1a 1a 1a 3a 1a 3a 5a 2d 3a 2d 3a 5a 1a 1a
3P 1a 2a 2b 2c 2c 1a 5a 4a 2a 4b 2e 10a 2d 2e
5P 1a 2a 2b 6a 2c 3a 1a 4a 6b 4b 6c 2e 2d 2e
7P 1a 2a 2b 6a 2c 3a 5a 4a 6b 4b 6c 10a 2d 2e
X.1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
X.2 1 −1−1 1 1 1 1 −1−1 1 −1 −1 1 −1
X.3 1 −1 1 −1−1 1 1 −1−1−1 1 1 1 1
X.4 1 1 −1−1−1 1 1 1 1 −1−1 −1 1 −1
X.5 4 −2 . 1 −2 1 −1 . 1 . 1 −1 . 4
X.6 4 2 . −1 2 1 −1 . −1 . 1 −1 . 4
X.7 4 2 . 1 −2 1 −1 . −1 . −1 1 . −4
X.8 4 −2 . −1 2 1 −1 . 1 . −1 1 . −4
X.9 5 1 1 1 1 −1 . −1 1 −1−1 . 1 5
X.10 5 −1 1 −1−1−1 . 1 −1 1 −1 . 1 5
X.11 5 −1−1 1 1 −1 . 1 −1−1 1 . 1 −5
X.12 5 1 −1−1−1−1 . −1 1 1 1 . 1 −5
X.13 6 . −2 . . . 1 . . . . 1 −2 6
X.14 6 . 2 . . . 1 . . . . −1−2−6
gap> ConjugacyClasses(g);
[ <identity ...>^G, f1^2 ∗(f1^2∗f2)^2∗f1∗f2∗f1∗f3^G, f3^G,
f1^2∗(f1^2∗f2)^2∗f1∗f2∗f1^G, f2^G, f1^3 ∗(f1∗f2)^2∗f1^4^G, f1^G,
f1^2∗(f1^2∗f2)^2∗f1∗f2∗f3^G, f2 ∗f1^4∗f3^G, f2 ∗f1^G,
f1^3∗(f1∗f2)^2∗f1^3∗f3^G, f1^3 ∗(f1∗f2)^2∗f1^2∗f3^G, f1 ∗(f1∗f2)^2∗f1^4^G,
(f1∗f2∗f1)^3∗f2∗f3^G ]
138
Eigenvalue Numerical multiplicity
1.91556 6
2.78954 5
5.89883 5
7.3379 5
8.26099 4
8.55338 6
13.2289 6
13.5082 4
15.1462 4
17.0459 6
17.7721 5
19.0882 6
22.5953 4
24.3521 5
24.6075 4
28.0573 6
28.5767 6
29.6861 4
31.4013 5
Table E.1: First positive eigenvalues of Bring’s surface
139
Appendix F
Mathematica Code for Bolza Surface
The following block of code helps us to choose the optimal value ofL to deﬁne the
spectral functionh(t) in Section 3.4. We ﬁrst deﬁne “lemult” as the ordered list of
lengths of geodesics in the length spectrum, using the formula in Section 3.2, along with
their multiplicities. Note that only the multiplicity of the ﬁrst length in the spectrum is
precise; all others have been calculated numerically. Also note that whilst the multiplicity
of the systole of the Bolza surface is 12, here we are concerned about moving along the
geodesic in both a positive and negative direction, so we double the multiplicity to take
this into account. We then use “les” to ﬂatten this into one list, rather than a list of pairs,
where each length appears multiple times.
We deﬁne the spectral function
h(x,L) =
(sinLx
Lx
)4
,
along with its Fourier transformg(ξ,L), and the derivative of the Fourier transform,
gd(x,L). Note that all of these are functions ofL as well as the usual variable.
For a given value ofL, the function “multbound” calculates the bound on the mul-
tiplicity of the ﬁrst eigenvalue, using the method described in Section 3.4. Finally, we
can use Mathematica’s “DiscretePlot” function to plot the bounds onm given by “mult-
bound(L)” for values ofL between 0.4 and 1, with a step size of 0.01. The output is
shown in Figure F.1, where we see thatL = 93
100 gives the lowest bound.
lemult = {{2 ArcCosh[1 + Sqrt [2]] , 24}, {2 ArcCosh[3 + 2 Sqrt [2]] ,
24}, {2 ArcCosh[5 + 3 Sqrt [2]] , 48}, {2 ArcCosh[7 + 5 Sqrt [2]] ,
96}, {2 ArcCosh[9 + 6 Sqrt [2]] , 48}, {2 ArcCosh[9 + 7 Sqrt [2]] ,
48}, {2 ArcCosh[11 + 8 Sqrt [2]] , 8}, {2 ArcCosh[13 + 9 Sqrt [2]] ,
96}};
les = Flatten [
Table [ Table [ lemult [[ i ]][[1]] , {k, 1, lemult [[ i ]][[2]]}] , {i , 1,
8}]];
140
h[x_, L_] = (Sin [L x]/(L x))^4
g[\[ Xi]_, L_] = FourierTransform [h[t , L] , t , \[Xi ]]/ Sqrt [2 Pi ]
Zer [x_] = 0;
gd[x_, L_] = D[g[x, L] , x] /. {Sign ’ −>Zer}
multbound[L_]:=(h[x_]=h[x,L];
/uni2423/uni2423/uni2423/uni2423g[\[ Xi]_]=g[\[ Xi] ,L];
/uni2423/uni2423/uni2423/uni2423gd[x_]=gd[x,L];
/uni2423/uni2423/uni2423/uni2423RightSide=−2NIntegrate [gd[x]/Sinh [x/2] ,{x,0 ,4L}]+
/uni2423/uni2423/uni2423/uni2423Sum[Sum[ les [[ i ]] g[k∗les [[ i ]]]/(2 Sinh [k ∗les [[ i ]]/2]) ,{ i ,1 ,Length[ les ]}] ,{k,1 ,10}];
/uni2423/uni2423/uni2423/uni2423(RightSide−h[ I /2])/h[ Sqrt[116469/28089 −1/4]])
DiscretePlot [multbound[L] ,{L,0.4 ,1.0 ,0.01}]
0.5 0.6 0.7 0.8 0.9 1.0
6
7
8
9
10
11
Figure F.1: Output of the function “multbound” for diﬀerent values ofL
We also include the code used to produce Figure 3.19. Here we construct a test
function to satisfy the hypothesis of Corollary 3.17, and plot its nodal line as a function
oft. We superimpose this plot of the nodal line against a plot of the boundary of the
annulus considered in Section 3.4.1 to show that the test function is positive inside the
desired region.
(∗ Eigenvalue ∗)
\[Lambda] = 5.;
(∗ Length of core geodesic ∗)
ell = 2. ArcCosh[1/2 Csc [\[ Pi ]/8]];
(∗ Hypergeometric functions with eigenvalue \[Lambda]. For efunc1 , \
141
the m variable gives the restriction of the eigenfunction to the mth \
Fourier node ∗)
efunc0 [\[Rho]_] =
Re[ Evaluate [
Sinh [\[Rho]] Hypergeometric2F1[(3/2 + I Sqrt [\[Lambda] − 1/4])/
2, (2 − (1/2 + I Sqrt [\[Lambda] − 1/4]))/2 ,
3/2, −Sinh [\[Rho]]^2] ] ] ;
efunc1 [\[Rho]_, m_] =
Re[ Evaluate [
Sinh [\[Rho]] Cosh[\[Rho]]^(2 Pi I m/
ell ) Hypergeometric2F1[(3/2 + I Sqrt [\[Lambda] − 1/4])/2 +
I m Pi/ell , (2 − (1/2 + I Sqrt [\[Lambda] − 1/4]))/2 +
Pi I m /ell , 3/2, −Sinh [\[Rho]]^2] ] ] ;
(∗ Nodal Line as a function of t . ∗)
\[Rho] zero [
t_] := (\[Rho] /.
FindRoot[
efunc0 [\[Rho]] − (0.038 Sin [2 Pi (t)/ ell − Pi/2]) efunc1 [\[Rho] ,
1] − (0.0002 Cos[2 2 Pi (t)/ ell ]) efunc1 [\[Rho] , 2] , {\[Rho] ,
0.5 , 1.9}]);
nodal = Plot [{\[Rho] zero [ t ]} , {t , 0, ell }];
(∗ Parametric plot of boundary of annulus ∗)
x1 = Cos[2 Pi t/ ell ];
y1 = Sin [2 Pi t/ ell ];
x2 = 4.61158 Cos[2 Pi t/ ell ];
y2 = 4.61158 Sin [2 Pi t/ ell ];
x3 = 1.0986840182524393 + 0.4550896306919397 Cos[2 Pi t/ ell ];
y3 = 0.4550896306919397 Sin [2 Pi t/ ell ];
x3 = 1.0986840182524393 + 0.4550896306919397 Cos[2 Pi t/ ell ];
y3 = 0.4550896306919397 Sin [2 Pi t/ ell ];
x4 = 2.5537741953480246 + 1.3820929243421862 Cos[2 Pi t/ ell ];
y4 = 1.3820929243421862 Sin [2 Pi t/ ell ];
x5 = 5.066671210777469 + 2.0986830534021754 Cos[2 Pi t/ ell ];
y5 = 2.0986830534021754 Sin [2 Pi t/ ell ];
boundary =
ParametricPlot [{{Log[ Sqrt [y1^2 + x1^2]] ,
ArcSinh [x1/y1]} , {Log[ Sqrt [y2^2 + x2^2]] ,
ArcSinh [x2/y2]} , {Log[ Sqrt [y3^2 + x3^2]] ,
ArcSinh [x3/y3]} , {Log[ Sqrt [y4^2 + x4^2]] ,
ArcSinh [x4/y4]} , {Log[ Sqrt [y5^2 + x5^2]] , ArcSinh [x5/y5]}} , {t ,
0.0001 , ell }, AspectRatio −> Automatic , PlotRange −> All ];
(∗ Superimpose nodal line plot onto boundary of annulus ∗)
\
Show[ nodal , boundary , PlotRange −> {{0, 1.6} , {1, 2.3}}]
142
Appendix G
Alternative approach to proving
Conjecture 3.12
In this appendix, we outline another method that could be used to prove Conjecture 3.12.
As in Section 3.4.1, consider the annulusΩ in Figure 3.18 with Dirichlet boundary con-
ditions. In particular, we can takeΩ to be a subspace of a hyperbolic cylinder withα as
its core geodesic. We have a Dirichlet boundary condition onα, so one method that we
could use to boundλ1(Ω)would be to compare it to the ﬁrst eigenvalue of the symmetric
half cylinder with core geodesicα, having the same area asΩ, that is,π. Here we make
the following conjecture, which is essentially a Faber-Krahn inequality for half-cylinders.
Conjecture G.1Let Ω0 be the symmetric half-cylinder with core geodesicα of length
l(α) = 2 arccosh
(
csc(π
8
)
2
)
,
and areaπ. Then
λ1(Ω)≥λ1(Ω0).
Remark G.2Recall from Lemma 2.35 that annuli in hyperbolic cylinders satisfy an
isoperimetric inequality. This is a similar hypothesis to that in the classical Faber-Krahn
inequality (compare Theorem 1.14), so it may be possible to prove Conjecture G.1 in a
similar way.
If we assume Conjecture G.1 holds, we consider the ﬁrst odd eigenfunction onΩ0, that
is,
φ(s) = sinh(l(α)) 2F1
(1 +s
2 , 2−s
2 ; 3
2;−sinh2(l(α))
)
as a function oft, withs = 1
2 +it. The corresponding eigenvalueλ =s(1−s) is obtained
by taking the ﬁrst zero ofφ(s). This eigenfunction is odd on a symmetric cylinder of area
143
2πwith respect to the core geodesicα, so will satisfy a Dirichlet boundary condition onα,
as well as its other boundary geodesic, that is, it satisﬁes Dirichlet boundary conditions
on a symmetric half-cylinder of areaπ.
To get a lower bound onλ, we analyze the diﬀerential equation, loosely following the
method of Appendix A in [77]. As a function ofρ, we know that
φ(ρ) = sinh(ρ) 2F1
(1 +s
2 , 2−s
2 ; 3
2;−sinh2(ρ)
)
satisﬁes (
− 1
cosh (ρ)
d
dρ cosh(ρ)d
dρ−λ
)
φ(ρ) = 0
with initial conditionφ(0) = 0and d
dρφ(0) = 1, whereλ =s(1−s) (recall our deﬁnition
of the Laplacian on a hyperbolic cylinder in Section 2.3.2). We substitute
ϕ = 2 arctan
(
tanh
(ρ
2
))
to get (
− d2
dϕ2− λ
cos2(ϕ)
)
Ψ(ϕ) = 0, (G.1)
where Ψ(ϕ) =φ(ρ(ϕ)) satisﬁesΨ(0) = 0and d
dρΨ(0) = 1. We prove the following
Theorem G.3Suppose we haveg∈ C2[0, x0] such thatg≥ 0 on [0, x0], g > 0 on
(0, x0), and (
−g′′(x)
g(x)− λ
cos2(x)
)
≥ 0 (G.2)
on [0, x0]. Thenf∈C2[0, x0] that is a solution to Equation(G.1), that is,f solves
−f′′(x)− λ
cos2(x)f(x) = 0, f (0) = 0, f ′(0) = 1,
has no zero in(0, x0).
Proof: The proof is done by contradiction. Letr0∈ (0, x0) be the ﬁrst positive zero of
f. Then, on[0, r0) we havef≥ 0,g≥ 0, and on(0, r0),g >0. We also havef >0 on
(0, r0). This is becausef′(0) = 1. The deﬁnition of the derivative implies thatf must
be positive for some value close to zero, in particular
1 =f′(0) = lim
h→0
f(0 +h)
h ,
sof will be positive until it is zero again atr0. Consider the Wronskian
F(x) =f′(x)g(x)−g′(x)f(x),
noting thatF(0) = 0, and its derivative
F′(x) =f′′(x)g(x)−g′′(x)f(x)
144
=
(
− λ
cos2(x)−g′′(x)
g(x)
)
g(x)f(x).
ThenF′(x)≥ 0, that is, it is increasing on(0, r0), which impliesF(r0)≥ 0. On the other
hand, consider the limit from below of
f′(r0) = lim
h→0−
f(r0 +h)
h ,
that is, for negativeh. We know thatf(r0−h) is positive for smallh, sincef(x) is
positive on(0, r0), sof′(r0)< 0. Withf′(r0)< 0 andg(r0)> 0, we haveF(r0)< 0, a
contradiction. □
Choosing a suitable functiong(x) that satisﬁes the hypothesis of Theorem G.3, we
can show thatφ(ρ) does not have a zero on the interval(0,ρ) for certainλ. The “certain
λ” condition will give us our bound onλ1(Ω). First, we need to change variables fromρ
toϕ, that is
ϕ = 2 arctan

tanh


arcsinh
(
π
2 arccosh(1
2 csc(π
8))
)
2



≈ 1.11795903.
Takeg(x) =x− 4x3
5 . We have to show that it is positive on(0, ϕ), and ﬁnd the values
ofλ for which Equation (G.2) is satisﬁed on[0, ϕ]. Let us start by showingg(x) > 0.
We have
g′(x) = 1− 12x2
5 ,
which is zero ifx =±
√
5
12. The second derivative
g′′(x) =−24x
5
tells us thatg(x) has a maximum at
√
5
12 and a minimum at−
√
5
12. Now,
g
(√
5
12
)
=
√
5
12
(2
3
)
,
so the maximum value is positive. The roots ofg(x) are atx = 0 andx =±
√
5
4. Note
that
√
5
4 is outside the interval[0, ϕ], sog(0) = 0and for all other values on the interval
it is positive.
Now we have to ﬁnd the values ofλ> 0 for which
24
5 ≥
λ
(
1− 4x2
5
)
cos2(x) .
145
Cross multiplying here is ﬁne, since1− 4x2
5 > 0 on [0, ϕ]. Let us try to maximize
h(x) = sec2(x)
(
1− 4x2
5
)
.
The (diagonal) Padé approximant ofsec2(x) of order 4 is
13x4
945 + 11x2
63 + 1
163x4
945 − 52x2
63 + 1.
We use this expression to approximatesec2(x) on [0, ϕ]; we can get an error bound on
our approximant using Taylor’s remainder theorem. First, we maximize
˜h(x) =
(
13x4
945 + 11x2
63 + 1
163x4
945 − 52x2
63 + 1
)(
1− 4x2
5
)
.
We have
˜h′(x) =−2x(8476x8− 81120x6− 798345x4 + 2664900x2− 893025)
5 (163x4− 780x2 + 945)2 .
This clearly has a root at zero, and to ﬁnd the other roots, we need to ﬁnd the roots of
the order 8 polynomial in parentheses. Notice that this is quartic inx2, so we may use
Ferrari’s method to ﬁnd its roots and then take their square roots. For a general quartic
polynomial
ax4 +bx3 +cx2 +dx +e,
the four roots are given by
x1, 2 =− b
4a± 1
2
√
−2p + q
S− 4S2−S and
x3, 4 =− b
4a± 1
2
√
−2p− q
S− 4S2 +S,
where
p = 8ac− 3b2
8a2 ,
q = 8a2d− 4abc+b3
8a3 ,
∆0 = 12ae− 3bd +c2,
∆1 =−72ace+ 27ad2 + 27b2e− 9bcd+ 2c3,
Q =
3
√√
∆2
1− 4∆3
0 + ∆1
2 , and
S = 1
2
√
1
3a
(∆0
Q +Q
)
− 2p
3.
146
We ﬁnd that fora = 8476, b =−81120, and so on, the only positive real root of the
polynomial whose square root lies in[0, ϕ] isx1. Therefore, the turning points of˜h′(x)
that we need to consider are at 0 and√x1. The second derivative
−2(1381588x12 − 19833840x10 + 652299885x8 − 2085793200x6 − 674616600x4 + 5465313000x2 − 843908625)
5 (163x4 − 780x2 + 945)3
is positive at 0 and negative atx1, so ˜h(x) takes its maximum value atx1. We do not
show the lengthy closed form here, but it is roughly equal to 1.04542. To ﬁnd out how
accurate this is, we can compare the Taylor series ofsec2(x),
1 +x2 + 2x4
3 + 17x6
45 + 62x8
315 + 1382x10
14175 +O(x11),
with the Taylor series of our approximant, that is,
1 +x2 + 2x4
3 + 17x6
45 + 62x8
315 + 28963x10
297675 +O(x11).
We see that these agree for the ﬁrst ﬁve terms, and so the error is the maximum value of
1382x10
14175 − 28963x10
297675 = 59x10
297675
on [0, ϕ]. This occurs atϕ, sincesec2(x) is increasing on this interval, so our error is
δx1 = 59ϕ10
297675≈ 0.000604461.
Now 24
5 ≥λ
(˜h(x1−δx1)
)
is satisﬁed for positiveλ when
λ≤ 24
5
(˜h(x1−δx1)
)≈ 4.591456764,
that is, for any suchλ,φ(ρ) does not have a zero on(0, ρ). Hence
λ1(Ωi)> 24
5
(˜h(x1−δx1)
)≈ 4.591456764, i ∈{ 11, 12, 13}.
147
References
[1] Mark S Ashbaugh. Isoperimetric and universal inequalities for eigenvalues.London
Mathematical Society Lecture Note Series, 273:95–139, 1999.
[2] Ralf Aurich and Frank Steiner. On the periodic orbits of a strongly chaotic system.
Physica D: Nonlinear Phenomena, 32(3):451–460, 1988.
[3] RalfAurichandFrankSteiner. Periodic-orbitsumrulesfortheHadamard-Gutzwiller
model. Physica D: Nonlinear Phenomena, 39(2):169–193, 1989.
[4] Werner Ballmann, Henrik Matthiesen, and Sugata Mondal. Small eigenvalues of
closed surfaces.Journal of Diﬀerential Geometry, 103(1):1–13, 2016.
[5] Pierre Berard.Analysis of Riemannian manifolds and geometric applications: an
introduction. Inst. de matematica pure e aplicada Rio de Janeiro, 1986.
[6] Pierre H Bérard. Spectral geometry: direct and inverse problems, volume 1207.
Springer, 2006.
[7] Gérard Besson. Sur la multiplicité de la première valeur propre des surfaces rieman-
niennes.Ann. Inst. Fourier (Grenoble), 30(1):109–128, 1980.
[8] Oskar Bolza. On binary sextics with linear transformations into themselves.Amer-
ican Journal of Mathematics, pages 47–70, 1887.
[9] Andrew R Booker and Andreas Strömbergsson. Numerical computations with the
trace formula and the Selberg eigenvalue conjecture.Journal für die reine und ange-
wandte Mathematik (Crelles Journal), 2007(607):113–161, 2007.
[10] David Borthwick. Introduction to spectral theory on hyperbolic surfaces.Spectral
geometry, 84:3–48, 2012.
[11] David Borthwick. Sharp geometric upper bounds on resonances for surfaces with
hyperbolic ends.Analysis & PDE, 5(3):513–552, 2012.
[12] Peter Buser. Riemannsche Flächen mit Eigenwerten in (0, 1/4).Commentarii Math-
ematici Helvetici, 52(1):25–34, 1977.
[13] Peter Buser.Geometry and spectra of compact Riemann surfaces. Springer Science
& Business Media, 2010.
148
[14] Yaiza Canzani. Analysis on manifolds via the Laplacian.Lecture Notes, Harvard
University, http://www. math. harvard. edu/ canzani/math253. html, 2013.
[15] Isaac Chavel.Eigenvalues in Riemannian geometry, volume 115. Academic press,
1984.
[16] Isaac Chavel.Riemannian geometry: a modern introduction, volume 98. Cambridge
University press, 2006.
[17] Jeﬀ Cheeger. A lower bound for the smallest eigenvalue of the Laplacian.Problems
in analysis, pages 195–199, 1970.
[18] Shiu-Yuen Cheng. Eigenfunctions and nodal sets.Commentarii Mathematici Hel-
vetici, 51(1):43–55, 1976.
[19] Richard Courant and David Hilbert.Methoden der mathematischen Physik, vol. 1.
Berlin, 1931.
[20] Harold SM Coxeter and William OJ Moser.Generators and relations for discrete
groups, volume 14. Springer Science & Business Media, 2013.
[21] Jozef Dodziuk, Thea Pignataro, Burton Randol, and Dennis Sullivan. Estimating
small eigenvalues of Riemann surfaces.The legacy of Sonya Kovalevskaya (Cam-
bridge, Mass., and Amherst, Mass., 1985), Contemp. Math, 64:93–121, 1987.
[22] Ahmad El Souﬁ and Saıd Ilias. Le volume conforme et ses applications d’après Li et
Yau.Séminaire de théorie spectrale et géométrie, 2:1–15, 1983.
[23] Noam D Elkies. The Klein quartic in number theory.The eightfold way (S. Levy,
ed.), Math. Sci. Res. Inst. Publ, 35:51–101, 1999.
[24] Hershel M Farkas and Irwin Kra.Riemann surfaces. Springer, 1992.
[25] Robert Fricke. Ueber eine einfache Gruppe von 504 Operationen.Mathematische
Annalen, 52(2):321–339, 1899.
[26] The GAP Group.GAP – Groups, Algorithms, and Programming, Version 4.7.8,
2015. (http://www.gap-system.org).
[27] Denis S Grebenkov and B-T Nguyen. Geometrical structure of laplacian eigenfunc-
tions. SIAM Review, 55(4):601–667, 2013.
[28] Daniel Grieser. Notes on heat kernel asymptotics. Available on his website:
http://www. staﬀ. unioldenburg. de/daniel. grieser/wwwlehre/Schriebe/heat. pdf,
2004.
[29] Phillip Griﬃths and Joseph Harris.Principles of algebraic geometry. John Wiley &
Sons, 2014.
149
[30] Martin C Gutzwiller. Classical quantization of a Hamiltonian with ergodic behavior.
Physical Review Letters, 45(3):150, 1980.
[31] Andrew Haas and Perry Susskind. The geometry of the hyperelliptic involution in
genus two.Proceedings of the American Mathematical Society, 105(1):159–165, 1989.
[32] Frédéric Hecht. New development in FreeFem++.J. Numer. Math., 20(3-4):251–265,
2012.
[33] Dennis A Hejhal.The Selberg trace formula for PSL (2, R), volume 2. Springer,
2006.
[34] Joseph Hersch. Quatre propriétés isopérimétriques de membranes sphériques homo-
genes. CR Acad. Sci. Paris Sér. AB, 270(A1645-A1648):5, 1970.
[35] Heinz Huber. Über die Darstellungen der Automorphismengruppe einer Rie-
mannschen ﬂäche in den Eigenräumen des Laplace operators.Commentarii Mathe-
matici Helvetici, 52(1):177–184, 1977.
[36] Adolf Hurwitz. Über algebraische Gebilde mit eindeutigen Transformationen in sich.
Mathematische Annalen, 41(3):403–442, 1892.
[37] Wolfram Research Inc. Mathematica, Version 10.0, 2014.
[38] Henryk Iwaniec.Spectral methods of automorphic forms, volume 53. American
Mathematical Society Providence, 2002.
[39] Dmitry Jakobson, Michael Levitin, Nikolai Nadirashvili, Nilima Nigam, and Iosif
Polterovich. How large can the ﬁrst eigenvalue be on a surface of genus two?Inter-
national Mathematics Research Notices, 2005(63):3967–3985, 2005.
[40] Dmitry Jakobson, Michael Levitin, Nikolai Nadirashvili, and Iosif Polterovich. Spec-
tral problems with mixed Dirichlet–Neumann boundary conditions: isospectrality
and beyond. Journal of computational and applied mathematics, 194(1):141–155,
2006.
[41] Felix Jenni.Ueber das Spektrum des Laplace-Operators auf einer Schar kompakter
Riemannscher Flachen. PhD thesis, University of Basel, 1981.
[42] Felix Jenni. Über den ersten Eigenwert des Laplace-Operators auf ausgewählten
Beispielen kompakter Riemannscher Flächen.Commentarii Mathematici Helvetici,
59(1):193–203, 1984.
[43] Chris Judge and Sugata Mondal. Geodesics and nodal sets of Laplace eigenfunctions
on hyperbolic manifolds.Proceedings of the American Mathematical Society, 2017.
[44] Hermann Karcher and Matthias Weber. The geometry of Klein’s Riemann surface.
The eightfold way, MSRI Publ. 35 (1999), 9–49.
150
[45] Tosio Kato.Perturbation theory for linear operators, volume 132. Springer Science
& Business Media, 2013.
[46] KarinKatz, MikhailKatz, MichaelMSchein, andUziVishne. Bolzaquaternionorder
and asymptotics of systoles along congruence subgroups.Experimental Mathematics,
25(4):399–415, 2016.
[47] Mikhail Katz and Stéphane Sabourau. An optimal systolic inequality for CAT (0)
metrics in genus two.Paciﬁc journal of mathematics, 227(1):95–107, 2006.
[48] FelixKlein. UeberdieTransformationsiebenterOrdnungderelliptischenFunctionen.
Mathematische Annalen, 14(3):428–471, 1878.
[49] Anthony W Knapp.Representation Theory of Semisimple Groups: An Overview
Based on Examples (PMS-36). Princeton university press, 2016.
[50] David Krejcirik. Geometrical aspects of spectral theory.Lecture notes given at the
Faculty of Nuclear Sciences and Physical Engineering of the Czech Technical Uni-
versity, Prague, http://http://gemma.ujf.cas.cz/ krejcirik/other/gspec16.pdf, 2016.
[51] Tapani Kuusalo and Marjatta Näätänen. Geometric uniformization in genus 2. In
Annales-Academiae Scientiarum Fennicae Series A1 Mathematica, volume 20, pages
401–418. Academia Scientiarum Fennica, 1995.
[52] Dami Lee. On a triply periodic polyhedral surface whose vertices are weierstrass
points.Arnold Mathematical Journal, pages 1–13, 2017.
[53] Silvio Levy. The eightfold way: the beauty of Klein’s quartic curve, volume 35.
Cambridge University Press, 2001.
[54] Peter Li and Shing-Tung Yau. On the Schrödinger equation and the eigenvalue
problem.Communications in Mathematical Physics, 88(3):309–318, 1983.
[55] Alexander Murray Macbeath. On a curve of genus 7.Proceedings of the London
Mathematical Society, 3(1):527–542, 1965.
[56] Jens Marklof. Selberg’s trace formula: An introduction.Hyperbolic geometry and
applications in quantum chaos and cosmology, page 83, 2012.
[57] Sugata Mondal.Small eigenvalues of hyperbolic surfaces. PhD thesis, Université de
Toulouse III Paul Sabatier, 2013.
[58] Sugata Mondal. Systole and λ2g−2 of a hyperbolic surface. arXiv preprint
arXiv:1305.4741, 2013.
[59] Sugata Mondal. On largeness and multiplicity of the ﬁrst eigenvalue of ﬁnite area
hyperbolic surfaces.Mathematische Zeitschrift, 281(1-2):333–348, 2015.
151
[60] Sugata Mondal. On topological upper-bounds on the number of small cuspidal eigen-
values of hyperbolic surfaces of ﬁnite area.International Mathematics Research No-
tices, 2015(24):13208–13237, 2015.
[61] Israel Moreno-Mejía. The quadrics through the Hurwitz curves of genus 14.Journal
of the London Mathematical Society, 81(2):374–388, 2010.
[62] Nikolai Semenovich Nadirashvili. Multiple eigenvalues of the Laplace operator.
Sbornik: Mathematics, 61(1):225–238, 1988.
[63] Holger Ninnemann. Gutzwiller’s octagon and the triangular billiard T*(2, 3, 8) as
models for the quantization of chaotic systems by Selberg’s trace formula.Interna-
tional Journal of Modern Physics B, 9(13n14):1647–1753, 1995.
[64] Stephane Nonnenmacher. Lecture notes: Spectral theory of selfadjoint operators.
Given at CMI-LMS summer school on “Microlocal Analysis and its Applications” at
Cardiﬀ University, June 2017.
[65] Robert Osserman. The isoperimetric inequality.Bulletin of the American Mathe-
matical Society, 84(6):1182–1238, 1978.
[66] Jean-Pierre Otal and Eulalio Rosas. Pour toute surface hyperbolique de genreg,
λ2g−2> 1
4. Duke Mathematical Journal, 150(1):101–115, 2009.
[67] Lawrence E Payne. Isoperimetric inequalities and their applications.SIAM review,
9(3):453–488, 1967.
[68] Murray H Protter and Hans F Weinberger.Maximum principles in diﬀerential equa-
tions. Springer Science & Business Media, 2012.
[69] John W Strutt Baron Rayleigh.The theory of sound, volume 2. Macmillan, 1896.
[70] Michael Reed and Barry Simon.Methods of modern mathematical physics. vol. 1.
Functional analysis. Academic New York, 1980.
[71] Gonzalo Riera and Rubi Rodriguez. The period matrix of Bring’s curve.Paciﬁc
Journal of Mathematics, 154(1):179–200, 1992.
[72] Paul Schmutz. Riemann surfaces with shortest geodesic of maximal length.Geomet-
ric & Functional Analysis GAFA, 3(6):564–631, 1993.
[73] Richard Schoen, Scott Wolpert, and Shing-Tung Yau. Geometric bounds on the low
eigenvalues of a compact surface.Proc. Sympos. Pure Math, 36:279–285, 1980.
[74] Atle Selberg. Harmonic analysis and discontinuous groups in weakly symmetric
Riemannian spaces with applications to Dirichlet series.Journal of the Indian Math-
ematical Society, 20(1-3):47–87, 1956.
[75] Bruno Sévennec. Multiplicity of the second Schrödinger eigenvalue on closed surfaces.
Mathematische Annalen, 324(1):195–211, 2002.
152
[76] Hans-Jürgen Stöckmann. Chladni meets Napoleon.The European Physical Journal-
Special Topics, 145(1):15–23, 2007.
[77] Alexander Strohmaier and Ville Uski. An algorithm for the computation of eigen-
values, spectral zeta functions and zeta-determinants on hyperbolic surfaces.Com-
munications in Mathematical Physics, 317(3):827–869, 2013.
[78] Michael E Taylor.Partial diﬀerential equations. I. , Basic theory. Applied mathe-
matical sciences. Springer, New York, 1996. Corr. 2nd print. 1997.
[79] The Sage Developers.SageMath, the Sage Mathematics Software System (Version
8.1), 2018.http://www.sagemath.org.
[80] Felix Klein translated by Silvio Levy. On the order-seven transformation of elliptic
functions.Math. Sci. Res. Inst. Publ, 35:287–331, 1999.
[81] Roger Vogeler.On the geometry of Hurwitz surfaces. PhD thesis, Florida State
University, 2003.
[82] Hermann Weyl. Das asymptotische Verteilungsgesetz der Eigenwerte linearer par-
tieller Diﬀerentialgleichungen (mit einer Anwendung auf die Theorie der Hohlraum-
strahlung).Mathematische Annalen, 71(4):441–479, 1912.
[83] Klaus Wohlfahrt. Macbeath’s curve and the modular group.Glasgow Mathematical
Journal, 27:239–247, 1985.
[84] Paul C Yang and Shing-Tung Yau. Eigenvalues of the Laplacian of compact Riemann
surfaces and minimal submanifolds.Annali della Scuola Normale Superiore di Pisa-
Classe di Scienze, 7(1):55–63, 1980.
[85] Steve Zelditch. Eigenfunctions and nodal sets.arXiv preprint arXiv:1205.2812, 2012.
153
