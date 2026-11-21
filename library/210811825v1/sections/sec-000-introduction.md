---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 11-35
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
Paris, February 1809
The court of Napoleon Bonaparte ﬁlls with the sound of a Haydn melody, as our performer
teases a curious rotating glass cylinder with felt-covered rods. The performer is Ernst
Chladni, the “father of acoustics”. Upon ﬁnishing his concert, he proceeds to demonstrate
his experiments with acoustics to the emperor. These involve bowing a ﬁxed plate at
diﬀerent frequencies, and observing how the patterns made by sand on the plate change as
the frequency increases. The patterns that he recorded on a square plate were documented
in his seminal work, Akusik.
Whilst the music of the clavicylinder is of little interest to the contemporary math-
ematician, the investigation of the patterns of sand on a vibrating plate, that is, the
nodal lines of Dirichlet eigenfunctions, remains an interesting problem. Napoleon him-
self remarked to Chladni that if one could apply some of the calculations involved in
the mathematical formulation of acoustics to areas curved in more than one direction, it
“could be useful for applications to other subjects as well” [76].
What do we understand by the term “curved in more than one direction”? Broadly
speaking, the curvature of a surface S at a point p measures how much the surface diﬀers
from its tangent plane TpS, that is, how far away it is from being “ﬂat”. If the curvature
is constant, then this measure takes the same value for every p ∈S.
For a simple
example of a surface of constant curvature, one can consider the sphere.
There are
several diﬀerent notions of curvature; in this work we predominantly consider Gaussian
curvature. The normal vector n forms a plane with each vector v in TpS2, with each
direction v corresponding the direction of a curve on the surface. The principal curvatures
κi are the (orthogonal) directions that give the maximum and minimum “bending” of S
at p. The Gaussian curvature is then deﬁned at a point p as the product of the principal
1
curvatures, that is,
K = κ1(p)κ2(p).
Figure 1.1: Principal directions at a point p on S2
n
κ1(p)
κ2(p)
When dealing with surfaces of constant Gaussian curvature, there are three main
cases: when K is positive, when it is negative, and when it is zero. We call these surfaces
spherical, ﬂat or hyperbolic. Having positive Gaussian curvature means that the principal
curvatures at p curve “in the same way”, so the area around p resembles a cap. Conversely,
negative curvature implies that the principal curvatures curve in diﬀerent directions, so
p is both a maximum and a minimum. Every point on a hyperbolic surface resembles
a saddle, or indeed, a Pringle. Hitherto, we have alluded to the notion of surfaces, but
have not said precisely what we mean. We take this opportunity to formally introduce
the setting for the analysis in this work.
Deﬁnition 1.1 (Riemann surface) A Riemann surface is a two (real) dimensional,
orientable Riemannian manifold. The preﬁx “Riemannian” indicates that a smooth man-
ifold has a Riemannian metric, that is, a smooth family of inner products gp( · , · ) such
that
gp : TpM × TpM →R
depends smoothly on p ∈M.
If X and Y are C∞vector ﬁelds on M, then their inner product with respect to the
Riemannian metric is a C∞real valued function on M. The Riemannian metric gives us
a consistent way of measuring angles on the surface, and thus endows the surface with a
conformal structure.
The property of being orientable means that one can make a consistent choice of
normal vector on the surface, that is, we can move a normal vector along a closed loop
continuously, without it changing sign. Figure 1.2 shows the Möbius strip, which is an
example of a manifold that is not orientable. To see this, move the outward pointing
2
normal vector around the closed loop. When it returns to its original position, it will be
inward pointing, so the Möbius strip is not orientable. If we ﬁx a an orientation (normal
vector) on a surface, we say that it is oriented. Where a surface S has boundary, we deﬁne
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
Deﬁnition 1.2 (Genus) The genus of a connected, orientable surface is the maximum
number of simple, closed, non-intersecting curves that one can cut along such that the
resulting surface remains connected.
For example, the genus of the torus is 1, because one can cut along a simple, closed
curve to obtain a cylinder, but another such cut would result in two cylinders.
The
genus may also be thought of as the number of handles glued onto a sphere; one sees
straightaway that the sphere has genus 0. The Bolza surface has genus 2, and the Klein
quartic has genus 3.
The following theorem provides a link between the geometry of a surface and its
topology (see, for example, [16]).
Theorem 1.3 (Gauss-Bonnet) Let S be a compact Riemann surface without boundary,
with Gaussian curvature K. Then
Z
S
K dA = 2πχ(S),
3
where dA is the area measure of S, and χ(S) is its Euler characteristic. χ(S) is another
topological invariant, and can be calculated from the genus g using the formula
χ(S) = 2 −2g.
Remark 1.4 For compact Riemann surfaces of constant curvature, the uniformization
theorem (introduced in Section 2.2.1) enables us to normalize the Gaussian curvature
to K = ±1 or K = 0, depending respectively on whether the surface is positively or
negatively curved, or ﬂat. On surfaces of constant negative curvature, the Gauss-Bonnet
theorem then implies
Area(S) = 4π(g −1),
where g is the genus of the surface.
Napoleon showed great foresight in his comment regarding the study of curved surfaces.
He was (inadvertently, one supposes) predicting an arena for the study of: the Helmholtz
wave equation
∇2A −k2A = 0,
where ∇2 is the Laplacian, A is the amplitude and k is the wave number; the stationary
wave equation

∇2 −1
c2
∂2
∂t2

u(x, t) = 0;
and the Schrödinger equation
HΨ = EΨ,
(1.1)
where H is the Hamiltonian and E is the energy of the state Ψ. We will examine this
third equation shortly in the context of the Bolza surface.
Although spectral theory in a Euclidean setting was commonplace in physics prior to
the 1950s, during this decade the geometry and spectra of hyperbolic surfaces became an
avenue of interest for quantum physicists. These surfaces provide a model for studying
quantum chaos; Selberg’s trace formula helped to bridge the gap between classical and
quantum mechanics.
We will study the Laplace-Beltrami operator acting on functions on compact Riemann
surfaces of constant negative curvature, in particular, those φi that solve the equation
∆φi −λiφi = 0,
(1.2)
where the eigenvalues λi form a discrete spectrum
0 = λ0 < λ1 ≤λ2 ≤. . . .
This is a heuristic overview of the problem. In the following section, we give details
of the diﬀerent boundary value problems on the surfaces that we consider. We go into
4
greater detail about the formulation of Equation (1.2) in Section 2.1, where we deﬁne
the Laplacian and its domain, and prove that the eigenfunctions φi exist and form an
orthonormal basis of the L2 space of functions on the surface.
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
Deﬁnition 1.5 (Closed eigenvalue problem) For a connected, compact surface M,
ﬁnd all λ ∈R such that
∆φ −λφ = 0
has nontrivial solutions φ ∈C2(M).
In practice, we will not tackle the closed eigenvalue problem head on. It is not possible
to calculate such eigenvalues explicitly, and the surface as a whole is often too compli-
cated to analyze. Rather, we will use the symmetry of the surface to break the closed
problem down into one of the following, where we consider a boundary value problem on
a subspace of the surface. We deﬁne the following problems on the more general setting
of a connected, smooth, oriented Riemannian manifold M. Additional conditions will
be speciﬁed. Giving the deﬁnitions on general manifolds will allow us to consider these
problems on sub-manifolds later.
Deﬁnition 1.6 (Dirichlet eigenvalue problem) For ∂M̸ = ∅, M compact and con-
nected, ﬁnd all λ ∈R such that
∆φ −λφ = 0
has nontrivial solutions φ ∈C2(M) ∩C0(M) that satisfy the boundary condition
φ = 0
on ∂M.
5
Ω1
Ω2
Ω3
Figure 1.3: Domain monotonicity for a torus with a disk removed
Remark 1.7 (Domain monotonicity, Dirichlet data) Unless otherwise stated, “do-
main” refers to an open, connected subset in M with compact closure. Ideally, when Ωis
a subset of a compact Riemann surface, its boundary ∂Ωwill be a smooth curve. In prac-
tice, this is not always the case; some of the domains we wish to consider have piecewise
smooth boundary, by which we mean that the boundary is formed as the ﬁnite union of
smooth curves. Let
Ω1, . . . , Ωm
be pairwise disjoint domains with piecewise smooth boundary and compact closure in M.
If M has boundary, the boundary of Ωi, i = 1, . . . , m, meets ∂M tranversally.
For
example, in Figure 1.3, M is a torus with a disk removed, ∂M is a circle, and we have
three pairwise disjoint domains.
For i = 1, . . . , m, consider the Dirichlet eigenvalue
problem on ∂Ωi ∩M (where ∂M̸ = ∅, we do not impose a constraint on ∂Ωi ∩M). We
arrange all the eigenvalues of these domains into the increasing sequence
0 ≤ν1 ≤ν2 ≤. . .
repeated according to multiplicity. Then for λk in the Laplace spectrum of M, we have
λk ≤νk
for all k ∈N.
A useful corollary of this is that for a Dirichlet eigenvalue problem on Ω⊂M and any
eigenvalue problem on M, we have
λk(Ω) ≥λk(M)
for all k ∈N. For example, in Figure 1.3 the ﬁrst (and indeed kth) Dirichlet eigenvalues
of Ω1, Ω2, and Ω3 will all be larger than the ﬁrst (respectively kth) eigenvalue of the
manifold in which they are contained, that is, the torus with a disk removed, where we
impose Dirichlet conditions on the boundary circle.
6
Our survey of spectral theory in Section 2.1 will focus on the “Dirichlet Laplacian”,
that is, the Laplace operator associated with the above problem. Another important type
of boundary condition is the Neumann problem.
Deﬁnition 1.8 (Neumann eigenvalue problem) For ∂M̸ = ∅, M compact and con-
nected, ﬁnd all λ ∈R such that
∆φ −λφ = 0
has nontrivial solutions φ ∈C2(M) ∩C1(M) that satisfy the boundary condition
∂φ
∂n = 0
on ∂M, where
∂
∂n is the outward unit normal vector ﬁeld on ∂M.
Remark 1.9 (Domain monotonicity, Neumann data) Let
Ω1, . . . , Ωm
be as above. Considering now the Neumann eigenvalue problem, where the normal deriva-
tive of the eigenfunction is required to be 0 on ∂Ω∩M, we arrange all the eigenvalues of
these domains into the increasing sequence
0 ≤µ1 ≤µ2 ≤. . .
repeated according to multiplicity. Then for λk in the Laplace spectrum of M, we have
µk ≤λk
for all k ∈N.
Finally, it is possible to have a boundary value problem that requires both Dirichlet
and Neumann conditions.
Deﬁnition 1.10 (Mixed eigenvalue problem) For ∂M̸ = ∅, M compact and con-
nected compact and connected, N an open submanifold of ∂M, ﬁnd all λ ∈R such that
∆φ −λφ = 0
has nontrivial solutions φ ∈C2(M) ∩C1(M ∪N) ∩C0(M) that satisfy the boundary
conditions
φ = 0 on ∂M −N,
∂φ
∂n = 0 on N.
Using the symmetry group of a hyperbolic surface, we can reduce the closed problem
on the surface to a simpler Dirichlet, Neumann or mixed problem on a fundamental
domain of the group action on the surface. Useful to this approach is the concept of
7
nodal lines and nodal domains, that is, the points on which the eigenfunction is zero and
how they partition the domain. This has an obvious link to Dirichlet boundary problems,
and we hope to exploit the connection in Section 3.4.
Deﬁnition 1.11 (Nodal domain) Let S be a closed Riemann surface and
C0(S) ∋f : S →R.
The nodal set of f is Zf = {f −1(0)}, and each connected component of
S \ {f −1(0)}
is a nodal domain of f.
Theorem 1.12 (Courant’s nodal domain theorem, [19]) Consider a Neumann
eigenvalue problem on M, ∂M̸ = 0, M compact and connected with eigenvalues
0 = λ0 ≤λ1 ≤λ2 ≤. . .
corresponding to the complete orthonormal basis of eigenfunctions {φ0, φ1, . . .} of L2(M).
The number of nodal domains of φk is ≤k + 1.
Now consider a Dirichlet eigenvalue problem on the same region, with eigenvalues
0 < λ1 ≤λ2 ≤. . .
corresponding to the complete orthonormal basis of eigenfunctions {φ1, φ2, . . .} of L2(M).
Then the number of nodal domains of φk is ≤k.
A classic paper on the nodal sets of eigenfunctions is [18], where it is proved that
for the Laplace operator acting on functions on a Riemannian manifold, the nodal sets
of eigenfunctions are smooth sub-manifolds, apart from a closed set of lower dimension.
Cheng also generalizes Theorem 1.12 to manifolds of higher dimension, and proves that
for a Riemann surface S and V ∈C∞(S), a solution ϕ of the Schödinger equation
(∆+ V )ϕ = 0
with nodal set Zϕ has isolated critical points on Zϕ, and the meeting points of nodal lines
form an equiangular system.
A survey of historical results relating to the nodal sets of the Laplacian on surfaces of
variable curvature is given in [85]. In more recent years, there have been some interesting
results linking the topology of nodal sets to the spectrum of ∆; Otal and Rosas proved
an initial result in 2009 [66] that for a compact, orientable, hyperbolic surface S of genus
g,
λ2g−2(S) > 1
4.
(1.3)
8
The value 2g −2 is of course equal to −χ(S), the Euler characteristic of S. This is the
ﬁnite area version of the classical result by Buser [12], that for every hyperbolic surface
of genus g ≥2
λ4g−2(S) > 1
4.
The proof of Equation (1.3) uses a novel technique in which the topology of the nodal
sets of eigenfunctions is considered, and the analysis is done separately for nodal sets
that are topologically equivalent to a cross cap, an annulus or a disk. The constant 1
4 is
signiﬁcant, because in many applications of spectral theory it is important to distinguish
the two cases when an eigenvalue λ ≥1
4 and when λ < 1
4. This comes from the fact the
the function
x 7→sin
 
x

λn −1
4
 1
2!
is bounded in the ﬁrst case but grows exponentially in the second, as x →∞[13].
1
4 is well known to be the bottom of the spectrum of the hyperbolic plane. For this
reason, eigenvalues in the interval

0, 1
4

have the special title of small eigenvalues. For
a compact Riemann surface S, the small eigenvalues of ∆(S) inﬂuence the asymptotic
length distribution of its closed geodesics (see, for example, [21,73]). In the same paper,
Otal and Rosas prove that any ﬁnite area hyperbolic surface of genus g with n holes has
at most 2g −2 + n small eigenvalues.
Following the techniques of [66], Mondal proved several results that use the topology of
nodal sets of Laplace eigenfunctions to give bounds on small eigenvalues of the spectrum
that depend on the systole of the surface, that is, the length of the shortest closed geodesic
(not necessarily unique). The systole of a Riemann surface S will be denoted s(S). It has
a multiplicity corresponding to the number of non-homotopic geodesics of minimal length
that cannot be contracted. Starting with the main result (in this area) of his thesis [57],
published in [58], he proved that for S closed and hyperbolic,
λ2g−2(S) > 1
4 + ϵ0(S),
where
ϵ0(S) < min
(
1
4(g −1), 1
4
 cosh(ρ0)
sinh(ρ0)
2
−1
!)
and
2s(S) sinh(ρ0) = Area(S).
More results of a similar nature can be found in papers such as [58–60]. In joint work with
Ballmann and Matthiesen [4], he proved that a closed Riemann surface S with negative
Euler characteristic has at most −χ(S) small eigenvalues. This paper generalizes earlier
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
Deﬁnition 1.13 (Isoperimetric inequality) Let D be an open disk in the hyperbolic
plane H (see Section 2.2 for a discussion on hyperbolic geometry). An open domain Ωin
a hyperbolic surface S is said to satisfy the isoperimetric inequality if
A(Ω) = A(D) =⇒l(∂Ω) ≥l(∂D),
with equality if and only if Ωis isometric to D, where A(Ω) denotes the area of Ω, and
l(∂Ω) denotes the length of its boundary.
Caution must be used with this deﬁnition, since there exists a whole class of results
called isoperimetric inequalities that relate the area of a domain to its perimeter, and
do not take into account physical properties such as torsional rigidity.
Isoperimetric
inequalities are said to have their origins in ancient Carthage, where Queen Dido was
tasked with delimiting the boundary of her new city, such that it would occupy a region
that could be encompassed by a single ox-hide. Legend has it that she cut the hide
into long thin strips and chose a circular boundary, having conjectured that this would
maximize the area of land. More succinctly we have the famous formula
L2 ≥4πA,
where a curve C of length L encloses a region of area A, and equality holds if and only
if C is a circle. We take this form of the inequality from [65], where Osserman gives
an interesting historical exposition of signiﬁcant results following on from this classical
theorem.
The term isoperimetric inequality is used interchangeably in the literature for problems
of the above type, and those of more relevance to this work: isoperimetric problems, where
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
positive eigenvalue of a domain Ωsatisfying Deﬁnition 1.13.
Theorem 1.14 (Faber-Krahn inequality) Let Ωbe an open domain in a hyperbolic
surface S, and D be a disk in hyperbolic space (more information on such disks is given
in Section 2.3.1). If Ωsatisﬁes the isoperimetric inequality, then
A(Ω) = A(D) =⇒λ1(Ω) ≥λ1(D),
where λ1 is the ﬁrst Dirichlet eigenvalue.
To prove the Faber-Krahn inequality, the levels sets of eigenfunctions on an open
domain are radially symmetrized so that the ﬁrst Dirichlet eigenvalue can be compared
to that of a geodesic disk with equal area. This theorem can be stated more generally for
n-dimensional manifolds satisfying an equivalent isoperimetric property; details can be
found in [15]. While Theorem 1.14 is a powerful tool for analyzing domains that satisfy
Deﬁnition 1.13, not every domain that we will study has this property. In particular,
domains in surfaces that resemble annuli can have a boundary that is shorter than that
of the disk with equal area.
Another tool for creating lower bounds on λ1 is Cheeger’s inequality. For the cases
investigated in this work, it is not as strong as the Faber-Krahn inequality, so we will
not actually use it. However, we state it as a key result in the theory of isoperimetric
problems.
Deﬁnition 1.15 (Cheeger constant) Let M be a non-compact Riemann manifold of
dimension n ≥2, possibly with boundary, and possibly having compact closure.
The
Cheeger constant h(M) is deﬁned as the following inﬁmum:
h(M) = inf
Ω
l(∂Ω)
Area(Ω),
where Ωranges over all open domains of S with compact closure and smooth boundary
and l(∂Ω) denotes the length of the boundary of Ω.
11
Theorem 1.16 (Cheeger’s inequality, [17]) For Ω⊂S as above, we have
λ1(Ω) ≥h2(Ω)
4
.
We will also be interested in creating upper bounds on eigenvalues. In his classic trea-
tise on acoustics [69], Rayleigh gave a variational characterization of the ﬁrst eigenvalue
for the Dirichlet problem. This involves taking the gradient of a function. We stated
earlier that the eigenfunctions of the Laplacian on a compact Riemann surface S form an
orthonormal basis of L2(S). Recall that L2(S) is the space of square integrable functions
on S, that is, a function f on S is in L2(S) if
Z
S
|f|2dS ≤∞.
where dS is the Riemannian measure on S. L2(S) is special among the Lp(S) spaces
because its inner product
⟨f, g⟩L2 =
Z
S
f g dS
makes it a Hilbert space. The inner product induces the norm
∥f∥2 = ⟨f, f⟩L2.
Note that the L2 norm gives no indication about how smooth a function is. When
we apply the Laplacian, we may therefore uncover huge (or indeed, undeﬁned) second
derivatives, even if the L2 norm of a function is small. The Laplacian is unbounded on
L2(S) and operations such as taking the gradient of f ∈L2(S) simply do not make sense.
Therefore, we need to formulate a diﬀerent space of functions before we can introduce
Rayleigh’s principle. Rather than considering the whole space of square integrable func-
tions, we will work with those functions in L2(S) for which we can deﬁne a reasonable
notion of diﬀerentiability. First consider the multi-index
α = (α1, . . . , αd),
αj ∈N
of order
|α| :=
d
X
i=1
αi,
and for ψ(x) : Rd →C suﬃciently smooth, deﬁne
Dαψ(x) :=
∂|α|ψ(x)
∂xα1
1 . . . ∂xαd
d
.
For convenience, we deﬁne D1ψ(x) to be the gradient ∇ψ(x) and D2ψ(x) to be the
Hessian matrix for ψ(x), the trace of which is equal to ∆ψ(x). We are now ready to
deﬁne our notion of diﬀerentiability.
12
Deﬁnition 1.17 (Weak derivative) Let ψ and g be locally integrable functions on a
domain Ω⊂S. We say that g is the αth-weak partial derivative of ψ if for all ϕ ∈C∞
0 (Ω),
Z
Ω
ϕ(x)g(x)dx = (−1)|α|
Z
Ω
Dαϕ(x)ψ(x)dx.
With the weak derivative, we can now deﬁne the spaces of functions on which we
consider our eigenvalue problems, namely, Sobolev spaces. In Section 2.1, we will see
how to extend the Laplacian on these spaces to a self-adjoint operator on L2(S), but for
now, we simply give enough detail to deﬁne the subsequent “variational” theorems.
Deﬁnition 1.18 (Sobolev space) Let Ωbe as above. The Sobolev spaces, indexed by
p ∈[1, ∞) and k ∈N, are given by
W k, p := {ψ ∈Lp(Ω) | Dαψ ∈Lp(Ω), 0 ≤|α| ≤k} ,
and are complete with respect to the Sobolev norm
∥ψ∥W k, p :=

X
0≤|α|≤k
∥Dαψ∥p
Lp(Ω)


1
p
where Dαψ is the weak partial derivative. We may also deﬁne W k, p
0
(Ω) as the closure of
C∞
0 (Ω) with respect to the Sobolev norm.
Remark 1.19 Again, we are most interested in the case where p = 2, since W k, 2(Ω) is
a separable Hilbert space with inner product
⟨φ, ψ⟩W k, 2 =
X
0≤|α|≤k
⟨Dαφ, Dαψ⟩L2.
The variational characterization of the Laplacian (and its associated eigenvalue prob-
lems) is concerned with the validity of the formula
⟨∆φ, f⟩L2 = D[φ, f],
where the φ is typically an eigenfunction, and the quantity on the right is the Dirichlet
integral
D[f, h] := ⟨D1f, D1h⟩L2
for f, h ∈W 1, 2(Ω) in the case when we consider a closed or Neumann problem and f, h ∈
W 1, 2
0
(Ω) when we consider a Dirichlet problem. D1 denotes the ﬁrst weak derivative. We
can now state the following theorems as in [15].
13
Theorem 1.20 (Rayleigh’s theorem) Let S be a closed and connected Riemann sur-
face, Ω⊂S be a domain with compact closure and non-empty piecewise smooth boundary.
Consider a ﬁxed eigenvalue problem on Ωwith eigenvalues
λ1 ≤λ2 ≤. . .
repeated according to multiplicity. For any 0̸ = f ∈W 1, 2(Ω) in the case when we consider
a closed or Neumann problem, and 0̸ = f ∈W 1, 2
0
(Ω) when we consider a Dirichlet
problem,
λ1(Ω) ≤D[f, f]
∥f∥2 ,
with equality if and only if f eigenfunction corresponding to λ1. The object on the right
is called the Rayleigh quotient, and will be denoted R(f).
We can use Rayleigh’s quotient to characterize λk for any k. In particular, we have
the following pair of theorems, taken from [6]:
Theorem 1.21 (Max-min) Let M be a smooth, connected, compact manifold, possibly
with boundary ∂M. For the Neumann eigenvalue problem on M, or closed eigenvalue
problem where ∂M = ∅, we have
λk = sup
Vk
inf{R(f) | f̸ = 0, f ⊥Vk},
where Vk runs through the k-dimensional subspaces of W 1, 2(M). We consider the
(k −1)-dimensional subspaces of W 1, 2
0
(M) for the Dirichlet eigenvalue problem on M.
Theorem 1.22 (Min-max) Let M be as above. For the Neumann eigenvalue problem
on M, or closed eigenvalue problem where ∂M = ∅, we have
λk = inf
Vk sup{R(f) | f̸ = 0, f ∈Vk},
where Vk runs through the (k + 1)-dimensional subspaces of W 1, 2(M). We consider the
k-dimensional subspaces of W 1, 2
0
(M) for the Dirichlet eigenvalue problem on M.
Remark 1.23 In this work, we use Theorem 1.22 in Section 3.3 to produce an upper
bound on the second positive eigenvalue of the Bolza surface. We do not actually use its
sister theorem at any point, but include it for completion.
The eigenvalues in the spectrum of the Laplacian on a compact Riemann surface are
known to have ﬁnite multiplicity; it is a reasonable question to ask what this multiplicity
is, and and whether it is possible to bound the multiplicity for a given eigenvalue ei-
ther from below or above. We will see in Section 2.4 that the multiplicities of a compact
14
Riemann surface are connected to the irreducible representations of its group of automor-
phisms. Well established results are that 0 = λ0 has simple multiplicity for the Laplacian
on a closed, connected surface, and for a Schrödinger operator with a smooth potential,
the ﬁrst eigenvalue, whilst not necessarily 0, also has multiplicity one [5,15].
For a Schrödinger operator H on a surface S, Cheng [18] bounded the multiplicity m1
of λ1 by a quantity that is quadratic in χ(S), with the corollary that for the Laplacian
on the sphere S2 with the standard round metric, m1(S2) = 3. Besson improved this
to a bound that is linear in χ(S) [7], highlighting that for the projective plane P2 with
round metric, and the ﬂat torus T2, we have m1(P2) = 5 and m1(T2) = 6 respectively.
Nadirashvili slightly improved the linear bound to
m1(S) = 5 −2χ(S)
for surfaces S with negative Euler characteristic [62]. Sévannec [75] improved this bound
for surfaces for surfaces of negative Euler characteristic, asymptotically by a factor of 2.
In particular, he proved the following
Theorem 1.24 Let S be a closed surface. If χ(S) < 0, then m1(S) < 5 −χ(S).
Example 1.25 Theorem 1.24 already provides upper bounds for the multiplicities of the
ﬁrst eigenvalues of the Bolza surface and Klein quartic. Recall that the Euler character-
istic of a surface S may be given in terms of the genus g as
χ(S) = 2 −2g.
Hence, for surfaces of genus 2, m1(S) < 7 and for surfaces of genus 3, m1(S) < 9.
The Bolza surface
In Chapter 3, we will look at the speciﬁc case of the Bolza surface, denoted by B, which
can be obtained by identifying opposite edges of a regular octagon in the Poincare disk
D. The vertices are at the points
2−1
4e
πik
4 ,
k = 0, 1, . . . , 7,
and are joined by geodesic segments of equal length. The group of (orientation preserving)
symmetries of B is GL2(Z3), which has order 48 (see, for example, [46,51]). The full group
of isometries, including reﬂections, is the semi-direct product GL2(Z3) ⋊Z2. This is the
highest order of a symmetry group for any genus 2 surface [51]. The Bolza surface takes
its name from Oskar Bolza, a student of Klein, who investigated algebraic curves; in
15
particular binary sextic equations with linear transformation into themselves [8]. The
algebraic curve for the Bolza surface is
w2 = z(z4 −1),
(1.4)
where w and z are two functions.
Figure 1.4: The Bolza surface in D
1
2
3
4
5
6
7
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

1 +
√
2

and have multiplicity 12. These are the four associated edges in Figure 1.4, the four
diameters of D connecting their midpoints, and the curves that connect the midpoint of
one edge with the midpoint connecting the adjoining edge. The formula for the systole
follows immediately from the side lengths of the (2, 3, 8) triangles that tessellate the
surface (see, for example, Figure 3.3). The systole of the Bolza surface was considered
in [47], where it was conjectured to be optimal for the systolic ratio
SR(S) = sup
G
s(G)2
AreaG(S)
16
of CAT(0) metrics G on surfaces S of genus 2 (that is, metrics of negative curvature
including those that are singular).
It is the same work by Jenni [41] that inspired the method for the investigation of
the Bolza surface in this work. He investigated the class of Riemann surfaces of genus
g, labelled Fg, obtained by associating the opposite sides of a regular 4n-gon with angles
π
2g. In this class, all the surfaces have one rotational and two reﬂective symmetries; the
Bolza surface stands out because it has an extra rotational symmetry, due to the fact
that the regular octagon can be tessellated by equilateral triangles (see Figure 3.1); the
curves that make up this tessellation are the 12 geodesics with length equal to the systole
of the surface. As well as his results on the Bolza surface, he also proved that for g > 2,
Fg has 2g such curves of length
s(Fg) = 4 arccosh
√
2 cos
 π
4g

.
For g ≥20, he identiﬁed the group representation that appears in the ﬁrst eigenspace of
Fg, proved that the ﬁrst eigenvalue has multiplicity 2, and also proved that
lim
g→∞g · λ1(Fg) = 2.
Using the same methodology, he proved similar results on the ﬁrst eigenvalues of a surface
of genus 2 in [42], where the surface varies by changing the length l(µ) of one of the sides
µ that make up its fundamental domain Fµ. In particular,
lim
l(µ)→0
l(µ)
λ1(Fµ) = π2.
This surface does not have any obvious maximal properties.
The Bolza surface has been investigated in the context of eigenvalue maximization
in [39]. Here the authors look at the surface as a ramiﬁed double cover of the sphere
where
Π : P →S2
is a degree 2 branched cover of the sphere, and P is a surface of genus 2 with the conformal
structure of the Bolza surface, that is,
P :=

(z, w) ∈C | w2 = F(z) := z(z −1)(z −i)
(z + 1)(z + i)

.
It has been shown by Yang and Yau [84] that for non-constant holomorphic maps of
degree d from a closed, orientable Riemann surface S to S2, the ﬁrst positive eigenvalue
λ1 of S satisﬁes the following inequality
λ1(S)Area(S) ≤8πd.
(1.5)
17
This built on Hersch’s result [34] that for any metric g on S2,
λ1(g)Areag(S2) ≤8π,
where λ1(g) and Areag refer to the ﬁrst eigenvalue and area with respect to the metric
g. It was extended to non-orientable surfaces by Li and Yau in [54], where they showed
that for and metric g on the real projective plane RP 2
λ1(g)Areag(RP 2) ≤12π.
Similar inequalities hold for an orientable surface S of genus γ immersed into R2+p,
that is, M = X( ¯
M) where ¯
M is a compact orientable surface and X : ¯
M →R2+p is an
immersion. In this case, Ilias and El Souﬁ[22] improved the bound of Yang and Yau to
λ1(S)Area(S) ≤8π
γ + 3
2

,
(1.6)
where ⌊· ⌋is the ﬂoor function.
For example, the Bolza surface has area 4π by the
Gauss-Bonnet theorem, so we may use Equation (1.6) to state
λ1(B) ≤4,
when we view the Bolza surface as an immersed surface in R2+p.
For surfaces of genus 2, we can take d in Equation (1.5) to be 2; further information
can be found in [29], which also gives background information on many of the concepts
in this section relating to algebraic geometry, that will not reappear in the main body of
this work. The Bolza surface has 6 ramiﬁcation points, by the Riemann-Hurwitz formula.
These are called the Weierstrass points of the surface and they occur at
{0, ∞, ±1, ±i}.
Note that 0 and ∞are ﬁxed points of Equation (1.4), and 0, ±1, and ±i are its roots
when w = 0. These points are singularities of the metric g0 on P that is inherited from
S2 by pulling back the round metric. In [39], the following conjecture is made
Conjecture 1.26 The metric g0 on P gives equality in Equation (1.5), that is
λ1(P, g0)Area((P, g0)) = 16π.
As part of their investigation into this conjecture, the authors reduce a spectral prob-
lem on S2 to a mixed boundary problem on the semicircle. Of particular interest is the
fact that the two problems in Figure 1.5 are isospectral under an exchange of Dirich-
let and Neumann conditions.
This phenomenon, known as “Dirichlet-Neumann swap
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
double cover of the sphere S2, however, genus 2 surfaces are also ramiﬁed double covers
of the Riemann sphere [24].
The double cover consists of two sheets, and there is a
function, J, called the hyperelliptic involution that switches between the sheets. In the
case of the Bolza surface, the involution is the centre of the full isometry group (see
Proposition 3.5). The hyperelliptic involution leaves geodesics invariant, and its ﬁxed
points are the Weierstrass points of the surface [31]. For the Bolza surface, we have seen
that the Weierstrass points are {0, ±1, ±i, ∞}.
Suppose we start in the Riemann sphere and draw the geodesics that connect our
Weierstrass points to get a cross (see Figure 1.7). The line from 1 to ∞is dashed; the
complement of the cross joining the other ﬁve points is simply connected, but this fails to
be the case when we add ∞. Thus, ∞is a branch point when we lift to the cover. When
19
we lift, angles are preserved, except at Weierstrass points where they are halved. On the
picture on the left of Figure 1.7, imagine taking the following journey: start at ∞, walk
to 1, carry on to walk to 0, turn by π
2, walk to i, turn right around and walk back to 0.
Carry on moving around the cross until arriving back at 1, and then carry on to ∞.
When we lift to the surface, the angles are halved at Weierstrass points, so the same
journey becomes: start at ∞, walk to 1, turn by π
2, walk to 0, turn by π
4, walk to i,
carry on and walk to 0. Continuing the journey takes us around the upper half on the
octagon on the right hand side of Figure 1.7. This is one sheet of the cover; the other is
its conjugate. They are glued together along the dotted line.
Figure 1.7: Creating a double cover of the Riemann sphere
−1
1
i
−i
∞
0
0
0
0
0
0
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
has as its nodal lines one line of a (4, 4, 4) triangle, and its rotations around the centre of
the fundamental polygon (the notation for such a triangle is explained in Section 2.2.3).
When we take the quotient of the Bolza surface by the hyperelliptic involution J, the
centre points of the 16 (4, 4, 4) triangles will map to 8 points on the Riemann sphere.
These 8 points give a cubical subdivision of the quotient surface that is dual to the subdi-
vision obtained from the 6 ramiﬁcation (or Weierstrass) points that induce an octahedral
symmetry. Using the numerical results in Appendix C, we can plot the values of the three
eigenfunctions corresponding to λ1 in R3; this is shown in Figure 1.8. One can clearly
see the octahedral symmetry, as well as 5 of the 6 singular points that come from the
ramiﬁcations (the other is at the rear). It appears that the eigenfunctions corresponding
to λ1 provide an immersion into R3; for a symmetric image such as the one in Figure 1.8,
one should take the eigenfunctions to be orthonormal.
The spectral theory of the Bolza surface has been studied in the physics literature
as the quantum mechanical Hadamard-Gutzwiller model for quantum chaos [3, 30, 63].
20
Figure 1.8: Plotting the values of the functions in the ﬁrst eigenspace in R3
This is essentially billiards on a hyperbolic surface. The advantage of using a hyperbolic
surface over a Euclidean model is that Selberg’s trace formula is exact, as opposed to the
semiclassical approximations given by the Euclidean case. The Bolza surface is one of the
simplest surfaces on which to study this dynamical system, due to its high symmetry, low
genus, and the fact that much information is already known about it from the context
of algebraic geometry. It can be described as the quotient of the Poincaré disk by the so
called “octagon group” (see Section 2.2 for more details on quotient surfaces). This is the
Fuchsian group with four generators [63]
gk =
 
1 +
√
2
(2 +
√
2)α exp
  ikπ
4

(2 +
√
2)α exp
  −ikπ
4

1 +
√
2
!
,
where
α :=
q√
2 −1,
k = 0, . . . , 3,
and the inverses are given by conjugation with
 
exp
  iπ
2

0
0
exp
  −iπ
2

!
.
They satisfy the relation
g0g−1
1 g2g−1
3 g−1
0 g1g−1
2 g3 = I2,
where I2 is the 2 × 2 identity matrix. The quotient of the Poincaré disk by this group
tessellates the unit disk with regular octagons.
The two theorems we prove in Chapter 3 are to do with the multiplicities of low-lying
eigenvalues in the spectrum of B. In particular
21
Theorem 1.27 The dimension of the ﬁrst eigenspace of ∆(B) is 3.
This result was stated by Jenni in [42] after being proved in his thesis [41]. Upon
careful inspection, a gap was found in this proof, relating to the analysis of 3 and 4
dimensional irreducible representations. In this work, we give a proof, utilizing the entire
automorphism group as opposed to a smaller subgroup. We give the associated irreducible
representation explicitly. The proof relies on a conjecture, for which numerical evidence
is given in Appendix C. We also suggest how this conjecture may be proved in future
work. We also prove
Theorem 1.28 The dimension of the second eigenspace of ∆(B) is 4.
Remark 1.29 Both of these theorems are consistent with the numerical calculations of
eigenvalues listed in Table C.1. We observed in the numerics that there are 3 eigenvalues
roughly equal to 3.84 and 4 eigenvalues roughly equal to 5.35.
The Klein quartic
The Klein quartic, also called Klein’s curve, has the largest automorphism group of all
compact Riemann surfaces of genus 3. Klein studied the quotient of the hyperbolic plane
by Fuchsian groups, that is, discrete subgroups of PSL2(R). He found the group
Γ(7) = PSL2(Z7)
to be of particular interest, and highlighted some of its special properties [48]. Since
then, it has been studied extensively both as a Riemann surface and as an algebraic
curve; the best introduction is the book “The Eightfold Way” [53], written to accompany
the installation of a statue of the surface at the MSRI, Berkeley. The book covers the
geometry of the surface, a number theoretical approach to the surface, and many topics
in algebra that highlight the extensive interest in the curve. So far, however, the spectral
theory of the surface remains relatively untouched; the large symmetry group suggests
that surface may maximize λ1 among genus 3 compact Riemann surfaces.
We obtain the surface by associating sides 2n + 1 and 2n + 6
mod (14), n = 0, . . . , 6
in Figure 1.9. It is possible to tessellate this fundamental polygon with 336 triangles (see
Figure 4.2). This corresponds to the full isometry group of the surface, PGL2(Z7), which
has order 336. The group of orientation preserving isometries is half the size of this, that
is, 168. This means that the Klein quartic not only has the largest automorphism group
for genus 3, it is also optimal, by the following classical theorem.
22
Figure 1.9: The Klein quartic
1
2
3
4
5
6
7
8
9
10
11
12
13
14
Side associations:
1 – 6, 3 – 8, 5 – 10, 7 – 12, 9 – 14, 11 – 2, 13 – 4
Theorem 1.30 (Hurwitz’s automorphism theorem, [36]) The number of automor-
phisms (not including reﬂections) of a compact Riemann surface of genus g > 1 cannot
exceed 84(g −1).
We see that for genus 3, this bound is 168. The symmetry group of the Klein quartic
is therefore maximal. Any surface that achieves this bound is referred to as a Hurwitz
surface. A Hurwitz surface does not occur for every single genus g > 1; the next Hur-
witz surface is the Macbeath surface of genus 7, which has 504 orientation preserving
isometries [55]. The group is isomorphic to the simple group PSL2(Z8) [55] and is further
investigated in [83]. This surface is also known as Fricke’s surface, as Fricke investigated
the corresponding isometry group in [25]. The fundamental polygon is shown in [25],
along with the relevant side associations.
The Klein quartic, as its name suggests, can be obtained as the locus of a projective
quartic curve, namely
x3y + y3z + z3x = 0.
(1.7)
The study of this equation accounts for much of the interest in Klein’s curve in number
theory. Stating the key results would involve introducing many terms that are irrelevant
to the rest of this work - the interested reader can ﬁnd a thorough exposition in [23]
instead.
The Fermat quartic is a similar surface that also comes from a projective equation; in
23
fact there is a whole class of Fermat surfaces that are obtained as the locus of
xk + yk + zk = 0,
k ∈N,
k > 2.
For the genus 3 version, we set k = 4. The fundamental polygon for the Fermat quartic is
a 16-gon, shown in Figure D.2 along with the correct side identiﬁcations. Similar to the
Bolza surface, the Fermat quartic can be tessellated by (2, 3, 8) triangles; as it is a genus
3 surface, there are 192 of them. The Fermat quartic therefore has an automorphism
group of order 192. A presentation of the group of orientation preserving elements is
given in [52]. We can extend this by adding a (non-commutative) Z2 action to get the
following presentation of the whole group:

a, b, c | a8 = b3 = c2 = (ab)2 = (a2b2)3 = (a4b2)3 = acac = bcbc = e

,
where e is the identity element. In Remark D.1 of Appendix D we will comment further
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
