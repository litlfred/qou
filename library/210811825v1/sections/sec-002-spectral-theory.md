---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-002-spectral-theory
section_title: "Spectral theory"
section_number: null
pages: 35-43
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
Spectral theory
The Laplace-Beltrami operator ∆, on a Riemannian manifold M, is given in local coor-
dinates by the formula
∆= −
n
X
i, k=1
1
√g
∂
∂xi
√ggik ∂
∂xk
,
where gik is the metric tensor, g its determinant, and gik are the components of the dual
metric on the cotangent bundle of M.
There exists an orthonormal basis {φi | i ∈N0} in L2(M) consisting of eigenfunctions
∆φi = λiφi
(2.1)
such that
0 = λ0 < λ1 ≤λ2 ≤. . .
(2.2)
form an ascending sequence with ∞as the only accumulation point. We understand
Equation (2.1) in terms of the weak derivative.
The sequence in Equation (2.2) is called the spectrum of ∆, and the individual λis are
referred to as eigenvalues. In this work, M will be either a compact Riemann surface,
or a subspace of a compact Riemann surface on which we consider a Neumann, Dirichlet
of mixed boundary problem.
Recall the deﬁnition of these eigenvalue problems from
Chapter 1. In particular, note that we take Ωto have compact closure and piecewise
smooth boundary. The property of compactness, along with the smoothness condition
where we consider a bounded Ω, ensure that the spectrum is discrete.
This result is entirely non-trivial; to see where it comes from, we will consider the
example of the Dirichlet Laplacian ∆D on a domain Ωin a Riemann surface (recall
Deﬁnition 1.6). The approach we take is via sesquilinear forms, which will be deﬁned
shortly. The spectral theory of ∆can also be explained through heat kernel asymptotics,
25
details of which are given in [13] and [28]. We start by introducing some classical theory
of unbounded operators, following [50] and [64]. Another good reference for the theory
of unbounded operators is [78].
Let H be a separable, complex Hilbert space. Let A be a linear operator in H. A
bounded linear operator A can be deﬁned for all u ∈H; it satisﬁes the inequality
∥Au∥≤C∥u∥,
where the least possible value of C deﬁnes the norm ∥A∥. Conversely, diﬀerential oper-
ators, in particular ∆, are unbounded and as a result do not have this property. They
are however deﬁned for some u ∈H, so to properly deﬁne an unbounded operator A, we
must also give its domain D(A) ⊂H. Often we will write (A, D(A)). The graph of the
operator is used to deﬁne A as
gr(A) := {(u, Au) | u ∈D(A)} ⊂H × H,
and comes with a norm (called the graph norm):
∥u∥A = ∥u∥+ ∥Au∥.
Deﬁnition 2.1 (Densely deﬁned operator) We say that A is densely deﬁned if D(A)
is dense in H.
Example 2.2 ∆Ω, that is, the Laplacian acting on Ω, is deﬁned on C∞
0 (Ω), and satisﬁes
Dirichlet boundary conditions trivially due to the property of compact support. Note that
it is also a non-negative operator since for φ ∈C∞
0 (Ω), an integration by parts shows that
(φ, ∆φ) = ∥∇φ∥2 ≥0.
C∞
0 (Ω) is dense in L2(Ω), so (∆Ω, C∞
0 (Ω)) is densely deﬁned on L2(Ω). Using Theo-
rem 2.13, we will create an extension of P Ω
D = (∆Ω, C∞
0 (Ω)) to deﬁne ∆Ω
D on L2(Ω).
Being densely deﬁned is an essential property for deﬁning the adjoint of an unbounded
operator.
For our unbounded, densely deﬁned operator A, we want to construct an
extension of A to a continuous operator on all of H, that is, a linear operator ˜A such
that D(A) ⊂D( ˜A) and for all u ∈D(A), Au = ˜Au. In the case of bounded operators,
we have the bounded linear transformation (or so-called ‘BLT’) theorem that allows us
to do this (see, for example, [70] for details of this and other named but unacknowledged
theorems in this section). On the other hand, for unbounded operators
sup
0̸=u∈D(A)
∥Au∥
∥u∥= ∞,
so a continuous extension is not possible.
The problem then, is to create a natural
extension of D(A) in a way that allows us to replicate, or at least approximate, the spectral
theory of bounded operators. First, we need to introduce the concept of closability.
26
Deﬁnition 2.3 (Closed operator) A is called closed if for all u, v ∈H and a sequence
{un}n∈N ⊂D(A), the conditions
un →u
and
Aun →v
as n →∞imply
u ∈D(A)
and
Au = v.
In other words A is closed if D(A) is a complete vector space with respect to the graph
norm.
Any bounded operator is closed by the closed graph theorem. Unbounded operators
are not necessarily closed, but we have a similar notion: A is called closable if it has a
closed extension, that is, if its graph remains the graph of an operator ¯A when its closure
gr(A) is taken. Once again, question of domains makes deﬁning the adjoint harder for
unbounded operators; for bounded operators, it follows from the Riesz representation
theorem.
Deﬁnition 2.4 (Adjoint of an unbounded operator) Let A be a densely deﬁned op-
erator in H. Its adjoint A∗is uniquely deﬁned as follows
D(A∗) := {u ∈H | ∃u∗∈H s.t. ∀v ∈D(A), (u, Av) = (u∗, v)} ,
A∗u := u∗
.
Proposition 2.5 A∗is always closed, regardless of whether or not A is.
To see this, we can look at an alternative deﬁnition of the adjoint, taking advantage
of the fact that we can describe an operator by its graph. For A∗,
gr(A∗) = R(gr(A)⊥),
where R acts like a rotation on H × H, namely R(u1, u2) = (u2, −u1).
Deﬁnition 2.6 (Symmetric operator) A is symmetric if it is densely deﬁned and its
adjoint A∗is an extension of A.
An easy consequence of Proposition 2.5 is that if A is symmetric, then it is closable.
The preceding deﬁnitions have laid the groundwork for us to deﬁne self-adjointness for
unbounded operators. These will be crucial for developing a functional calculus of oper-
ators f(A), f : R →C, whereby we will be able to use function analytic methods in our
spectral analysis of operators.
27
Deﬁnition 2.7 (Self-adjoint operator) A is self-adjoint if it is densely deﬁned, A∗=
A and D(A) = D(A∗). A symmetric operator A is essentially self-adjoint if its closure ¯A
is self-adjoint.
We now consider sesquilinear forms.
The aim is to establish a one to one corre-
spondence between these forms and self-adjoint operators; this will allow us to create
self-adjoint extensions of densely deﬁned, symmetric, non-negative operators.
Deﬁnition 2.8 (Sesquilinear form) A sesquilinear form in H is a map
q : D(q) × D(q) →C,
where D(q) ⊂H, such that
(u, v) →q(u, v)
is linear in the second entry and semi-linear in the ﬁrst. The mapping
D(q) →C
u 7→q[u] := q(u, u)
is called the quadratic form associated to q. q is semi-bounded below if
q[u] ≥α∥u∥2
for some α ∈R. q is called elliptic if
|q[u]| ≥c∥u∥2
for some c > 0. Finally, q is closed if it is semi-bounded below and D(q) is a complete
Hilbert space with respect to the norm
∥u∥2
q = q(u, u) + (|α| + 1)∥u∥2.
Example 2.9 For our study of the Dirichlet Laplacian, we will introduce a sesquilinear
form QΩ
D such that
D(QΩ
D) := D(P Ω
D)
and for φ ∈W 1, 2
0
,
QΩ
D[φ] := (φ, ∆φ) = ∥∇φ∥2.
Deﬁnition 2.10 (Adjoint of a sesquilinear form) The adjoint q∗of q is deﬁned as
D(q∗) := D(q),
q∗(φ, ψ) := q(ψ, φ).
q is symmetric if q∗= q.
28
Now let q be a symmetric, densely deﬁned sesquilinear form that is bounded from
below. As before, q is closable if it has a closed extension, that is, if for all {ψn}n∈N ⊂
D(q),
D(q) ∋ψn
n→∞
−−−→0
q[ψn −ψk]
n, k→∞
−−−−→0
imply q[ψn]
n→∞
−−−→0, then q has closure ¯q deﬁned as
D(¯q) :=
n
ψ ∈H | ∃{ψn} ⊂D(q) s.t. if ψn
n→∞
−−−→ψ, q[ψn −ψk]
n, k→∞
−−−−→0
o
,
¯q[ψ] := lim
n→∞q[ψn].
Example 2.11 The form QΩ
D is not closed on C∞
0 , but note that the norm
∥φ∥2
QΩ
D = QΩ
D[φ] + (|α| + 1)∥u∥2
is the norm on the Sobolev space W 1, 2
0
(Ω) (compare Deﬁnition 1.18). The domain of the
closure ˜QΩ
D = QΩ
D is therefore W 1, 2
0
(Ω), and for φ ∈W 1, 2
0
(Ω),
˜QΩ
D[φ] = ∥∇φ∥2,
where we interpret ∇φ in a distributional sense.
From the sesquilinear form q, we wish to induce an operator Aq that is self-adjoint and
bounded from below. The correspondence is as follows. Suppose we have Aq as above.
Then
˙q[ψ] := (ψ, Aqψ),
D( ˙q) := D(Aq)
is densely deﬁned, symmetric and bounded from below. It is closable, so we take the
closure q := ¯˙q as our desired form. On the other hand, suppose we have q as above. Then
we will use the following to deﬁne the corresponding operator:
Theorem 2.12 (Representation theorem, [45]) Let q be densely deﬁned, symmetric,
closed, and bounded from below in H. Then
D(Aq) := {ψ ∈D(q) | ∃η ∈H s.t. ∀φ ∈D(q), q(φ, ψ) = (φ, η)} ,
Aqψ := η
is self-adjoint and bounded from below. D(q) is called the form domain of the operator
Aq.
We now introduce a special construction that produces the self-adjoint operator with
the smallest form domain, that is, the domain of q is contained in the form domain of any
29
other self-adjoint extension ˜
Aq of Aq. We will use this to deﬁne the Dirichlet Laplacian as
the self-adjoint extension of a minimal operator that has the smooth, compactly supported
functions as its domain.
Theorem 2.13 (Friedrichs extension) Let A be a symmetric operator, bounded from
below. Let qA be the sesquilinear form such that
qA[ψ] := (ψ, Aψ),
and
D(qA) := D(A)
is densely deﬁned, symmetric and bounded from below. If qA is closable, we take the
closure
˜qA := qA.
Finally, we can associate to ˜qA the self-adjoint linear operator A˜q via Theorem 2.12.
Example 2.14 Using Theorem 2.12 and Theorem 2.13, we are now ready to deﬁne ∆Ω
D
on L2(Ω) as a self-adjoint extension of P Ω
D via the quadratic form ˜QΩ
D. The deﬁnition in
the Representation Theorem gives us
D(∆Ω
D) =

ψ ∈W 1, 2
0
(Ω) | ∃η ∈L2(Ω) s.t. ∀φ ∈W 1, 2
0
(Ω), (∇φ, ∇ψ) = (φ, η)
	
,
(2.3)
∆Ω
Dψ = η.
We may abbreviate this deﬁnition slightly, using the knowledge that C∞
0 (Ω) is dense in
W 1, 2
0
(Ω), and that the condition in 2.3 deﬁnes the distributional Laplacian, to state
D(∆Ω
D) =

ψ ∈W 1, 2
0
(Ω) | ∆ψ ∈L2(Ω)
	
,
∆Ω
Dψ = ∆ψ.
We deﬁne the spectrum of an unbounded operator via the inverse, (A −z)−1 of a
self-adjoint operator in H. It exists for all values of z that are not eigenvalues of A.
Deﬁnition 2.15 (Resolvent) The resolvent set of A,
ρ(A) := {z ∈C | (z −A) : D(A) →H is bijective and (z −A)−1 is bounded}
is an open subset of C. The resolvent operator
ρ(z) := (z −A)−1
depends analytically on z inside ρ(A).
30
Example 2.16 The resolvent operator for the Dirichlet Laplacian, ρ(−1) = (∆Ω
D + 1)−1
is a bounded map
ρ(−1) : L2(Ω) →W 1, 2
0
(Ω).
Deﬁnition 2.17 (Spectrum) The spectrum of A is the complement
σ(A) := C \ ρ(A).
Remark 2.18 We are interested in the discrete spectrum σdis, which is the set of isolated
eigenvalues of ﬁnite multiplicity, that is
σdis(A) = {λ ∈C | ∃ψ ∈D(A), ∥ψ∥= 1, Aψ = λψ}.
If λ ∈σdis(A), then its multiplicity is given by dim(ker(A −λ)) < ∞.
Now that we have deﬁned the resolvent operator, we just need to show that it is
compact, and then we can apply the spectral theorem for compact, self-adjoint operators.
First, we deﬁne what it means to be a compact operator.
Deﬁnition 2.19 (Compact operator) A bounded operator A is compact if for a bounded
sequence (un)n∈N, (Aun)n contains a converging sub-sequence.
There are alternative criteria for a bounded operator to be compact, for example, we
have
Proposition 2.20 Let A be bounded operator on a Hilbert space H. Then the following
are equivalent [64]:
(i) A is compact;
(ii) A is the norm limit of a sequence of ﬁnite rank operators;
(iii) for any weakly convergent sequence un ⇀u, Aun →u strongly;
(iv) for any ﬁnite orthonormal system (en), Aen →0.
Theorem 2.21 (Rellich-Kondrachov embedding theorem) Let Ωbe a bounded do-
main of a compact Riemann surface S. The the embedding
W 1, 2(Ω) ⊂L2(Ω)
is compact.
Example 2.22 We have seen that ρ(−1) is bounded from L2(Ω) to W 1,2
0 (Ω). By the
Rellich-Kondrachov embedding theorem, W 1,2
0 (Ω) has a compact embedding into L2(Ω),
since Ωis compact, as is the surface S for which it is a subset.
31
The following theorem guarantees that any complex number in the spectrum of a
compact operator is an eigenvalue.
Theorem 2.23 (Fredholm alternative) Let A be a compact operator. For z0̸ = 0,
(i) either (z0 −A)−1 exists and is a bijection H →H,
(ii) or z0 is an eigenvalue of ﬁnite multiplicity.
Therefore, the spectrum of the compact resolvent ρ(−1) consists of σdis ∪{0}, and its
eigenvalues have ﬁnite multiplicity. Moreover the only accumulation point of its spectrum
is zero.
The upshot of Theorem 2.23 is that we can “invert” the property of a compact resolvent
ρ(z) of A to get information about what we are really interested in - the spectrum of
A. In particular, A has a purely discrete spectrum that has ∞as its only accumulation
point. To see this, note that for the eigensystem (µn, un) of ρz,
(z0 −A)−1un = µnun ⇐⇒(1 −z0µn)un = −µnAun.
Rearranging the right hand sides tells us that the eigenvalues of A are
λn = z0µn −1
µn
.
One can see that an accumulation of the resolvent µn →0 will correspond to an accu-
mulation at inﬁnity for the spectrum of A. Returning to ∆Ω
D, we have seen that it has
a compact resolvent, and therefore a discrete spectrum. We ﬁnish the section by stating
the general spectral theorem for self adjoint operators.
Theorem 2.24 If A is compact and self-adjoint, then it admits an orthonormal eigen-
basis (un, λn) with λn →0.
2.2
Hyperbolic geometry
We now want to look at the Laplacian in two speciﬁc models of hyperbolic geometry. First,
we will consider the Poincaré disk model. This is the setting through which we view the
Riemann surfaces. Next, we will consider the Laplacian in geodesic polar coordinates
on the Poincaré upper half plane, H. Harmonic analysis on H will give us a method to
calculate the eigenvalues of hyperbolic disks. As a result, we can then use the Faber-
Krahn inequality as a comparison tool for Dirichlet boundary problems on our surfaces.
32
2.2.1
The upper half plane
