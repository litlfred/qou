---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-016-4-1-the-flow-equation-for-chern-simons
section_title: "The Flow Equation For Chern-Simons"
section_number: "4.1"
pages: 63-71
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
---
4.1 The Flow Equation For Chern-Simons
Let M be a three-manifold. Let H be a compact Lie group and set G = HC. Let T be the
space of connections A on a fixed H-bundle E → M, and let TC be the space of complexvalued connections A on the complexification of E. We can write A = A + iφ where A and
φ are the real and imaginary parts of A; A is an h-valued connection, and φ is a one-form
on M with values in the adjoint bundle ad(E). The curvature of A will be denoted as
F = dA + A ∧ A, and that of A as F = dA + A ∧ A.
TC is a complex manifold; to define a flow equation, we need to endow it with a Kahler
63

metric. We pick a Riemannian metric g on M, which determines a Hodge star operator15
⋆M. We define the metric on T by
ds
2 = −
Z
M
Tr δ A ∧ ⋆MδA. (4.1)
This is a Kahler metric, with Kahler form
ω =
Z
M
Tr δφ ∧ ⋆MδA. (4.2)
The metric ds
2
is invariant under H-valued local gauge transformations, though not under
G-valued ones. The moment map for the H-valued local gauge transformations is
µ = dA ⋆M φ, (4.3)
where dA = d + [A, ·] is the covariant derivative with respect to A.
Critical “points” of the Chern-Simons function W(A), understood as a function on the
space of connections, actually form orbits under the group of complex gauge transformations.
For reasons described in section 3.3.3, we will only consider critical orbits that are semistable,
meaning that they admit a locus with µ = 0. The condition for a flat connection A, that
is a connection obeying 0 = F = dA + A ∧ A, to be gauge-equivalent to a connection for
which µ = 0 is [52] that the holonomy of the flat connection A is not strictly triangular. In
other words, if the holonomies of A around one-cycles in M can be simultaneously put in
upper triangular form

α β
0 γ

, (4.4)
then the upper right elements β all vanish. Strictly triangular flat connections are unstable
and we omit them. (A block diagonal flat connection with β = 0 is considered semistable,
and one that cannot be put in a triangular form at all is stable.)
The flow equation for a Morse function that is the real part of a holomorphic function I
is
dA
dt
= − ⋆M
δ I
δA
. (4.5)
We are interested in the case that I = λ W(A) where W is the Chern-Simons functional
and λ is a complex number. By rescaling t, we can reduce to the case that λ = 2π exp(−iα)
with real α. The flow equation then becomes
dA
dt
= − exp(−iα) ⋆M F, (4.6)
15 If dx1
, dx
2
, dx
3
is an oriented orthonormal frame, we pick the sign of ⋆M so that ⋆M(dx
1
) = dx
2 ∧ dx3
,
etc. Similarly, later the star operator of I × M is defined so that ⋆(dt ∧ dx
1
) = dx
2 ∧ dx3
, etc.
64

where F is the complex conjugate of the curvature F = dA + A ∧ A. More explicitly, this is
dA
dt
= − ⋆M

cos α(F − φ ∧ φ) − sin α dAφ

dφ
dt
= ⋆M

sin α(F − φ ∧ φ) + cos α dAφ

. (4.7)
The time t parametrizes a real one-manifold I (which is the real line or a portion of it).
We pull back E to a bundle over I×M and view A as a connection on this pullback. As such,
A has vanishing component in the I direction. We view this as a gauge condition. Relaxing
this gauge condition, we can write dAi/dt (i is an index tangent to M) in gauge-invariant
language as a component Fti of the curvature F = dA + A ∧ A. Similarly, we view φ as an
ad(E)-valued one-form on I × M; as such, it is not generic, since its component φtin the I
direction vanishes. We endow I ×M with a Riemannian metric that is the sum of the metric
dt
2 on I with the metric g on M, and we write simply ⋆ for the Hodge star operator on
I × M (normalized as in footnote 15). After taking linear combinations of the equations in
(4.7), one finds that these equations can be put in a form with four-dimensional symmetry
(F − φ ∧ φ)
+ = uDφ+
(F − φ ∧ φ)
− = −u−1Dφ−, (4.8)
with
u =
1 − cos α
sin α
, u−1 =
1 + cos α
sin α
. (4.9)
(For a two-form v, we define the projections v
± = (v ± ⋆v)/2.) To be more precise, the
four-dimensional symmetry is broken in our context by the condition φt = 0. But if we relax
this condition, the equations have full four-dimensional symmetry.
The moment map µ = dA ⋆M φ is as usual a conserved quantity for the flow equations.
As explained in section 3.3.3, we are primarily interested in solutions of the flow equations
with µ = 0. Bearing in mind that we anyway have the condition φt = 0, dA ⋆M φ can be
written in four-dimensional language as dA ⋆ φ. So we want to supplement the equations
(4.8) with an additional condition
dA ⋆ φ = 0. (4.10)
Henceforth, the phrase “flow equations” will refer to this combined system of equations.
The flow equations have been first encountered [53] in the gauge theory approach to
geometric Langlands.16 These are elliptic equations, modulo the gauge symmetry, and this
means that their general properties are much like those of flow equations for finitely many
variables in ordinary Morse theory. The relevant properties are stated in section (4.1.2).
16The parameter u is called t in [53], but here we prefer to avoid confusion with the time coordinate.
65

The condition φt = 0 can be reinterpreted in terms of a vanishing theorem similar to those
of section 3.3 of [53]. This argument proceeds as follows. Set V
+(u) = (F −φ∧φ)+ −uDφ+,
V
−(u) = (F − φ ∧ φ)− + u−1Dφ−, V0 = dA ⋆ φ, so the flow equations are V+(u) = V−(u) =
V0 = 0. Now consider the following sum of squares of these equations:
−
Z
I×M
Tr 
u
−1
u + u
−1
V
+(u) ∧ V+(u) + u
u + u
−1
V
−(u) ∧ V−(u) + V0 ∧ ⋆V0

= −
Z
I×M
d
4x
√
g Tr 
1
2
FµνF
µν + DµφνDµφν + Rµνφµφν +
1
2
[φµ, φν]
2

+
u − u
−1
u + u
−1
Z
I×M
Tr F ∧ F. (4.11)
(Indices µ, ν are tangent to I ×M, and Rµν is the Ricci tensor of I ×M, which is a pullback
from M.) Clearly, the left hand side of (4.11) is stationary when the flow equations are
obeyed. Therefore the right hand side is also stationary. The part of the right hand side
that depends on φtis simply
Z(φt) = −
Z
I×M
d
4x
√
g Tr X
µ
DµφtD
µφt +
X
µ6=t
[φt, φµ]
2
!
. (4.12)
The flow equations therefore imply that φt obeys the Euler-Lagrange equations derived from
(4.12), or
−
X
µ
DµD
µφt +
X
µ6=t
[φµ, [φµ, φt]] = 0. (4.13)
(Of course, this can also be proved by differentiating the equations (4.8) and (4.10).) Provided that one can integrate by parts, which is true if φt obeys either Dirichlet or Neumann
boundary conditions at each end of I, (4.13) implies that Z(φt) = 0. Given the definition
of Z(φt) as a sum of squares, this immediately implies that φtis covariantly constant and
commutes with all φµ. Thus, φt generates a symmetry of the solution.
We will always choose boundary conditions such that φt vanishes at (at least) one end of
I, and integration by parts is possible at the other end. The above argument shows that in a
solution of the flow equations obeying such boundary conditions, φtis identically zero. There
is no need to spoil the four-dimensional symmetry, or the elliptic nature of the equations,
by postulating in advance that φtis identically zero. This is a consequence of the equations
plus boundary conditions.
4.1.1 The Index
For applications, we need to know the expected value of the dimension of the moduli space
M of solutions of the above equations, with appropriate boundary conditions and modulo
66

gauge transformations. This equals the index of the linear elliptic operator L that arises from
those equations, after linearization and gauge fixing. We will show that on a four-manifold
of the form I × M, with certain types of boundary condition at the ends of I, the index
vanishes. This will lead in section 4.1.2 to behavior similar to that of Morse theory with
finitely many variables.
The index is independent of u, so it suffices to set u = 1. The relevant linear system
can be described as follows. We expand around a classical solution (A0, φ0) by setting
(A, φ) = (A0 + δA, φ0 + δφ). A convenient gauge-fixing condition is dA0 ⋆ δA = 0. For a
four-manifold X, let Ωq
X (ad(E)) be the space of q-forms on X with values in ad(E).
After acting on δφ with the ⋆ operator, we can think of δA and δφ as elements of
Ω
1
X (ad(E)) and Ω3X (ad(E)), respectively. We can view the gauge-fixing condition as asserting
the vanishing of the element ⋆dA0 ⋆ δA of Ω0
X (ad(E)), while the equations V
+ = V− = 0
assert the vanishing of the element V
+ + V− of Ω2
X (ad(E)), and the equation V0 = 0 asserts
the vanishing of an element of Ω4
X (ad(E)).
All told, our linear operator L maps Ω1
X (ad(E))⊕Ω
3
X (ad(E)) to Ω0X (ad(E))⊕Ω
2
X (ad(E))⊕
Ω
4
X (ad(E)). A familiar operator that does this is the operator L0 = dA + d∗
A mapping ad(E)-
valued differential forms of odd degree to those of even degree. L is actually equal to L0
modulo zeroth order terms that do not affect the index. As we explain momentarily, the
index of the operator L0, or of L, is unaffected by the twisting by the gauge bundle E. If
X is compact, this index is simply the product −χ(X) dim(H), where χ(X) is the Euler
characteristic of X and dim(H) is the dimension of the Lie group H. For X = I × M, the
topological Euler characteristic of X vanishes, and boundary contributions to the index are
also zero, so the index of L vanishes.
The value of the index for compact X and its vanishing for X = I ×M can be understood
as follows. Let S+ and S− be the two spin bundles of X; each is of rank 2. It is convenient
to express the operator L0 as a Dirac operator mapping sections of S+ ⊗ V to sections of
S− ⊗V for some vector bundle or difference of vector bundles V ; the index of L0 can then be
computed from the index theorem for the Dirac operator. To put L0 = dA +d∗
A in the desired
form, we must take V to be a formal difference of vector bundles V = (S+ ⊖ S−) ⊗ ad(E).
Taking the formal difference S+ ⊖ S− where S+ and S− have the same rank causes all bulk
and boundary contributions to the index that depend on E to cancel. (As X is a fourmanifold and E has vanishing first Chern class, the only bulk E-dependent contribution is
a multiple of the second Chern class of E; it cancels when we take the difference S+ ⊖ S−.
Boundary contributions are further discussed in the next paragraph.) Hence ad(E) can be
replaced by a trivial bundle of the same rank, namely dim(H), and L0 then reduces to the
sum of that number of copies of the standard operator d + d∗ mapping ordinary differential
forms of odd degree to those of even degree. The index of this operator on a four-manifold
without boundary is −χ(X).
67

Since the vanishing of boundary corrections to the index is important, let us spell it out
in more detail. If I has a boundary at a finite distance – for example the right boundary
of the half-line (−∞, 0] – then we will pick local boundary conditions. With local boundary
conditions, there is no E-dependent boundary contribution to the index, and as the metric of
I × M is a product, there is also no boundary contribution involving the extrinsic curvature
of the boundary. Alternatively, if I has an “end” at infinity – for example, the left end
of the half-line – then we want normalizable solutions of the equation LΨ = 0. Asking
for normalizable solutions is equivalent to cutting off the half-line at a finite distance and
imposing global Atiyah-Patodi-Singer boundary conditions. In general, in such a situation
there is a boundary contribution to the index of a Dirac-like operator, but it cancels when
we take the formal difference (S+ ⊖ S−) ⊗ ad(E) because S+ and S− are equivalent when
restricted to M.
The operator L is real, so it has a real determinant line bundle. This determinant line
bundle is topologically trivial17 and after fixing a trivialization, L has a natural real-valued
determinant function det L.
4.1.2 Applications Of The Flow Equation
The flow equation has two primary applications. The first is to determine the coefficients
when a given cycle C in the relative homology is expanded as a sum of Lefschetz thimbles
Jσ in the usual way,
C =
X
σ
nσJσ. (4.14)
We are only interested in cycles C that lie at µ = 0.
The coefficient nσ is obtained by counting, with suitable signs, the solutions of the upward
flow equation on the half-line R
− = (−∞, 0]. As usual, the upward flow equations are
obtained from the downward ones by reversing the sign of the time. The boundary conditions
are that the flow starts at a flat connection Aσ (corresponding to the cycle Jσ) at t = −∞
and ends on C at t = 0. Equivalently, we can consider downward flow equations on the
half-line R
+ = [0, ∞). In this case, we consider flows that start on C at t = 0 and end at Aσ
at t = ∞.
We write AM = AM + iφM for the restriction of A = A + iφ to M, at a fixed t. The
boundary condition that we want at t = 0 is that AM should lie in C. Since we assume that C
17In Donaldson theory, it is shown that the determinant line bundle of the Dirac operator twisted by
S+ ⊗ ad(E) is trivial under a mild topological restriction that is satisfied in our applications. In our case,
because we are twisting by the difference (S+ ⊖ S−) ⊗ ad(E), the topological condition in question is not
needed.
68

lies at µ = 0, the condition that AM lies in C implies in particular that µ = dA ⋆M φM = 0 at
t = 0. Subtracting this from the bulk equation dA ⋆φ = 0, which is one of the flow equations,
we find that the covariant normal derivative of φt vanishes at t = 0: Dtφt = 0. This is enough
to justify integration by parts in showing that Z(φt), defined in (4.12), vanishes. So it will
lead to global vanishing of φt after we also pick a suitable boundary condition at t = −∞.
The most basic example is the case that C is the real integration cycle of Chern-Simons
theory with compact gauge group H. In this case, the condition for AM to lie in C is simply
φM = 0. This certainly implies that dA ⋆ φM = 0.
At t = −∞ (or t = +∞ if we formulate the flow on R
+), we ask that AM approaches a
specified flat connection Aσ and that φt vanishes. Given this vanishing, and the fact that we
have chosen a boundary condition that allows integration by parts at t = 0, the vanishing
theorem implies that φt will vanish everywhere.
Let M be the moduli space of solutions of the flow equations with boundary conditions
just described. Since the index in the linearized problem vanishes, the expected dimension
of M is zero and for a generic metric on M, M consists of a finite set of points. We count
these points with a weight that is 1 or −1 depending on the sign18 of det L. Summing
the contributions of all critical points, we get the integer nσ that appears in the expansion
C =
P
σ
nσJσ.
Let us compare the definition of nσ to the definition of the most basic invariant in Donaldson theory of smooth four-manifolds. This invariant is defined in a situation in which the
index of the operator L− that arises in linearizing the Yang-Mills instanton equation on X is
zero. Under this circumstance, for a generic metric on X, the instanton equation has finitely
many solutions, and Donaldson’s invariant is defined by summing over all such solutions
with a weight given by the sign of det L−. Obviously, nσ is a close cousin of this, with the
usual instanton equations replaced by the flow equations for a complex-valued connection.
So far, the elliptic nature of the flow equations has enabled us to express a given cycle
C in terms of the Lefschetz thimbles Jσ, according to eqn. (4.14). The other important
application of the flow equation is to describe Stokes phenomena. Here we must consider
complete flow lines between two critical points corresponding to semistable flat connections
Aσ and Aτ on M. We must define an invariant mστ that controls what happens in crossing
a Stokes ray at which there are flows from Aσ to Aτ .
We consider the flow equations on X = R ×M, with the requirement that AM → Aσ for
18The overall sign of the function det L depends on a choice of orientation of the relevant determinant
line bundle. This amounts to a choice of relative orientations of the cycles C and Jσ that we are comparing.
Such choices of sign and orientation are discussed in, for example, [46] in the context of finite-dimensional
Morse theory and Floer cohomology.
69

t → −∞ and AM → Aτ for t → +∞. Further we require that φt → 0 at both ends. The
index of L still vanishes, but now there is a new ingredient: the flow equations are invariant
under the group T ∼= R of translations in the R direction, but a solution with σ 6= τ cannot
be translation-invariant. So any solution with σ 6= τ will have to come in a one-parameter
family, and hence it is impossible to have an isolated solution. This clashes with the fact
that the index is 0, and means that generically there are no flows from Aσ to Aτ .
We know an independent reason for this: the flow equation has a conserved quantity,
namely the imaginary part of the holomorphic function I = λW(A). For generic λ, conservation of Im I makes a flow from Aσ to Aτ impossible. The condition for a Stokes ray
is precisely that a flow from Aσ to Aτ is consistent with the conservation law. Taking
λ = 2π exp(−iα), a Stokes ray is characterized by some condition α = α0. Instead of regarding α as a constant in our flow equations (4.8) and (4.10), regard it as a variable that
takes values in a small interval near α = α0. This adds one variable to the problem without adding any new equations, and the index of the linearized problem is now 1. Thus the
moduli space of solutions should generically be one-dimensional – corresponding to families
of solutions, obtained from each other by the action of T, that appear at α = α0. To get
back to a problem with zero index, we can identify two field configurations that differ by
the action of T. This removes one variable, and the number of solutions is now generically
finite. Weighting the solutions by the sign of the determinant of the operator Le that appears
in the linearization around a solution, we arrive at the desired invariant mστ .
Concretely, adding one variable and removing another and replacing L by Le has the
following effect. Suppose we set α = α0 and find a solution of the flow equations. The
linearization L around a solution of the flow equations will have a zero mode ψ, generated
by the action of T on the given solution. Hence det L = 0. Now vary α away from α0. The
eigenvector ψ of L can be deformed with α so as to remain an eigenvector, but its eigenvalue
λ(α) generically vanishes only at α = α0. Replacing L by Le means that in evaluating the
determinant at α = α0, the factor that comes from the eigenvector ψ is not λ(α0) = 0 but
(dλ/dα)|α=α0, which is generically not zero. So det Le is generically nonzero and its sign is
the contribution of a given T-orbit of flow lines to mστ .
We have defined an invariant nσ associated to the flow equations on a half-line, and
another invariant mστ associated to the same equations on the full real line. The relation
between these invariants is that in crossing a Stokes ray at which there is a net number mστ
of downward flow lines from Aσ to Aτ , the invariant nτ jumps by nτ → nτ − nσmστ . As
explained in the discussion of eqn. (3.20), where m+− is taken to be ±1, this jumping of
the coefficients
P
nτ compensates for the jumping in the cycles Jσ and ensures that the sum
σ
nσJσ is invariant. In infinite dimensions, it seems most concise to describe the jumping
phenomenon in terms of the behavior of the coefficients.
Just as in Morse theory with finitely many variables, the jumping happens because at
70

α = α0 the set of points that can be reached by downward flow from Aσ ceases to be closed –
its closure contains Aτ . A downward flow from C to Aτ can split into a pair of flows, first from
C to Aσ and then from Aσ to Aτ . This leads to the “wall-crossing” behavior nτ → nτ −nσmστ .
See for example [41] in the context of flows with finitely many variables. Ellipticity means
that such statements about Morse theory carry over to the infinite-dimensional case. This
is an important fact in the context of Floer theory (of three-manifolds and of loop spaces of
symplectic manifolds). See for example [46, 47] for reviews. Hopefully the usual proofs in
the context of Floer theory can be adapted to the present situation.
