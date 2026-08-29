---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-056-2-j-d
section_title: "J D"
section_number: 2
pages: 72-77
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
2 −1(kr).
(4.3)
If one expands the exponent in the integral in a series, the standard expansion
for the Bessel function arises.
A slightly more involved example is the quantum mechanical model of a
particle in the potential e−q, i.e. the theory of equation
 
−d2
dq2 + e−q
!
ψ(q) = 0
(4.4)
69
(one of course recognizes a simpliﬁed version of Toda models). It can be
solved by projection of the simple Sshr¨odinger equation for a particle, moving
on the upper part of the hyperboloid x2
0 −x2
1 −x2
2 = 1;
x0 > 0 [73]. If
x0 = cosh q
2 + 1
2z2eq/2;
x1 = sinh q
2 −1
2z2eq/2;
x2 = zeq/2,
then q = log(x0 + x1), Laplace operator on hyperboloid is
L = ∂2
∂q2 −1
2
∂
∂q + 1
4e−q ∂2
∂z2
(4.5)
and average of the wave function ψλ(q, z) provides the following expression
for solutions of (4.4):
ψλ(q) = eiλq
Z ∞
0
t2iλ−1e−(t+eq/t)dt.
(4.6)
This idea, which is sometimes refered to as ”projection method” (see [73]
for a broad review), reveals hidden symmetries of some complicated systems
(which do not possess any symmetry at all in the usual, Noether-like, sence
of the word), by considering them as embedded into wider theories with
more degrees of freedom. Quantum mechanical examples of applicability of
the method are by no means exhausted by the two systems above, one can
consider various projections, starting from (exactly solvable problem of) the
free motion on any group manifold, and in general this gives rise to a very
important theory of ”zonal spherical functions”, which nowadays is increas-
ingly attracting attention because of its obvious links to integrability theory
and quantum geometry (see [74] for discussion of the latter relation and [75],
where also relations with orthogonal polinomials and Generalized Kontsevich
model are partly revealed). An extremely important example of free motion
on a group manifold (in the inﬁnite-dimensional - Kac-Moody - case) is pro-
vided by 2-dimensional WZNW (Wess-Zumino-Novikov-Witten) model and
the corresponding version of projection method is known as Hamiltonian re-
ductions in conformal ﬁeld theory. Again the resulting theories (like minimal
conformal models) do not possess any kind of symmetry in the usual sense
of the word, but still they are very simple and exactly solvable, remembering
their origin in the theory of free ﬁelds.
In principle the theory which is reduced, i.e. complemented by constraints
(initial conditions), does not need to be absolutely symmetric, i.e. to have
70
Casimir operator or even zero (as in the WZNW case) as its Hamiltonian.
It can be in fact possible to use the projection method to gain a lot of infor-
mation about reductions of theories with more sophisticated Hamiltonians,
which are non-trivial functions of group generators.
The simplest exam-
ple is provided by the theory of quantum-mechanical ”quasi-exactly-solvable
models” [76],[77] and its CFT-generalizations [77],[78]. A more elaborated
technique has the name of ”localization theory”,24 (known also as geometrical
quantization, Fourier analysis on group manifolds and Duistermaat-Heckman
theory), it provides a very wide generalization of the above averaging proce-
dure, which maped plain waves into Bessel functions. The classical sample
system to illustrate all the aspects of integrability, starting from free motion
and ending with anyonic statistics, W∞-algebras and 2d Yang-Mills theory,
is the Calogero-Sutherland system, which can be associated in a uniform
way with any simple Lie algebras and in an ”intermediately involved” form
looks like a multiparticle theory in 1+1 dimension with interaction potential
g2 sin−2 ǫ(xi −xj). (See [73] for the introduction to the theory of Calogero-
type models and [80],[81] for the new developements.)
All this discussion was necessary just to illustrate a very simple idea: the
theory of free particles, though trivial, is in fact unexhaustively deep. It is
enough to impose sophisticated initial conditions or perform a sophisticated
change of variables in order to obtain very complicated dynamical systems,
which after they are studied per se appear to be surprisingly system, the
reason for this simplicity being that the real underlying dynamics is just
trivial - that of the free particles,- though it may be very hard probelm to
reveal this simplicity when the system is given. It is advantage of the general
theory, that one can begin from the proper side: just from the theory of free
particles and just start making it more and more complicated, by introducing
diﬀerent kind of variables, considering correlators of sophisticated operators
and so on. Everything what can be obtained in this way is by deﬁnition
trivially integrable, though it may be not so simple to guess for somebody
who did not know where the particular system at the end of this procedure
appeared from.
We now proceed to discussion of particularly important realization of this
24 For various views and approaches to this theory see [61],[62], [63],[5], [64].[65],[43],
[44],[79]. (So far there are no connections with Andersson localization in the solid state
physics.)
71
idea: the theory of ¯∂-operators in 1C dimension (i.e. the theory of free holo-
morphic ﬁelds in 2 real dimensions). When considered as functions of moduli
of the bundles over Riemann surfaces (i.e. of boundary conditions, imposed
on 2d free ﬁelds), these simple objects (known as ”τ=functions”) start look-
ing a little involved and after all appear related to sophisticated non-linear
equations (but of course integrable) in 2 and 3 dimensions (like KdV or
Kadomtsev-Petvishvili (KP) equation). We do not attempt to present an ex-
haustive theory of τ-functions and integrable hierarchies (besides being still
uncompleted, this is a very big ﬁeld), but instead concentrate on the very core
of it, which is just simple determinant formulas for the simplest τ-functions
(namely, associated with free-fermion theory and level k = 1 Kac-Moody
algebras). This issue will be discussed in some details, because besides being
the basis of integrable hierarchies theory, it is also exactly the place, where
the links with the matrix models are found.
4.2
The notion of τ-function
There are several diﬀerent deﬁnitions of τ-functions, but all of them are
particular realizations of the following idea: τ-function is a generating func-
tional of all the correlation functions in the theory of free particles in 1+1
dimensions. This basic quantity is a kind of ”det D”, where ”D” is a time-
evolution operator (continuous or discrete) and ”det” is a sort of a product
over eigenvalues of ”D”, which is usually expressed in the form of a functional
integral, associated with free particles (it is not a priori Gaussian in original
variables). This quantity is the most general deﬁnition of τ-function.
In practice one is usually more speciﬁc. The mostly well studied version
of τ-function arises if one thinks about free particles of a peculiar type:
free fermions with quadratic Hamiltonian and continuous time evolution,
i.e. one considers a theory of spin-1/2 b, c-system (fermions) ˜ψ(¯z, z), ψ(¯z, z),
described by the functional integral
τ{A} ∼Det(¯∂+ A) ∼
∼
Z
D ˜ψDψ exp
Z
d2z
˜ψ ¯∂ψ

exp
Z
d2z
Z
d2˜z A(z, ˜z)δ(¯˜z −¯z)ψ(z) ˜ψ(˜z)

where ¯z plays the role of time and A = A(z, ˜z)δ(¯˜z−¯z)d¯˜zd¯z is some ( 1
2, 1; 1
2, 1)-
bidiﬀerential (i.e. contains a factor of d˜z1/2d¯˜zdz1/2d¯z).
72
Of course, one can think about more general τ-functions, involving many
fermions (this is often done), and more general b, c- and β, γ-systems, in
particular, arising in the context of WZNW model, associated to any Kac-
Moody algebra of any level.25 Also of interset is consideration of discrete
time evolution (described by diﬀerence rather than diﬀerential equations),
though, as usual in the 2d theories, this is not a really independent problem.
In the language of matrix models the restriction to free −fermion τ-
functions is essentially equivalent to restriction to eigenvalue models. Serious
consideration of non-eigenvalue models, aimed at revealing their integrable
(solvable) structure will certainly involve the theory of generic τ-functions,
but both these things are matters of the future research, and we”ll not go
into details about them in these notes.
4.3
τ-function, associated with the free fermions
Because of speciﬁc form of the Lagrangian in (4.7) the functional integral can
be easily represented in Hamiltonian form, provided topology of the 2-surface
on which ¯z, z are coordinates, is trivial (genus 0: sphere or annulus). Namely,
consider ˜ψ and ψ as operator-valued functions of z only (not of the time ¯z).
Then the only reminiscent of kinetic term
R
d2z ˜ψ ¯∂ψ is canonical commutation
relation:
[ ˜ψ(˜z), ψ(z)]+ = δ(˜z −z)d˜z1/2dz1/2.
(4.7)
Then
τ{A} ∼⟨0 | exp
I
d˜z
I
dz A(z, ˜z)ψ(z) ˜ψ(˜z)

| 0⟩.
(4.8)
Now it is usual to expand around z = 0:
ψ(z) = P
n∈Z ψnzndz1/2;
˜ψ(z) = P
n∈Z ˜ψnz−n−1dz1/2;
25The main technical diﬀerence between generic and ”free-fermion” cases is that La-
grangian of generic free ﬁeld theory is not just quadratic in scalar ﬁelds φ, but can also
contain particular combinations of exponents eφ. It also deserves noting that the most
general expresiion, quadratic in scalar ﬁelds, if rewritten in terms of fermions is in fact
quartic (but of course not a generic quartic interaction arises in this way). Integrable
nature of certain quartic-fermion interactions is well known from the theory of Thirring
models (in this class of models interactions are usually local).
73
[ ˜ψm, ψn]+ = δm,n;
ψm | 0⟩= 0 for m < 0;
˜ψm | 0⟩= 0 for m ≥0;
A(z, ˜z) =
P
m,n∈Z z−m−1˜znAmndz1/2d˜z1/2;
so that
I
d˜z
I
dz A(z, ˜z)ψ(z) ˜ψ(˜z) =
X
m,n∈Z
Amnψm ˜ψn.
In fact this expansion could be around any point z0 and on a 2-surface of any
topology: topological eﬀects can be easily included as speciﬁc shifts of the
functional A(z, ˜z) - by combinations of the ”hadle-gluing operators”. Anal-
ogous shifts can imitate the change of basic functions zn for zn+α and more
complicated expressions (holomorphic 1/2-diﬀerentials with various bound-
ary conditions on surfaces of various topologies).
One can now wonder, whether local functionals A(z, ˜z) = U(z)δ(˜z −
z)dz1/2d˜z1/2 play any special role. The corresponding contribution to the
Hamiltonian looks like26
HCartan =
I
dz U(z)ψ(z) ˜ψ(z) =
I
dz U(z)J(z),
(4.9)
where
J(z) = ψ(z) ˜ψ(z) =
X
n∈Z
Jnz−n−1dz
(4.10)
is the U(1)k=1 Kac-Moody current;
Jn =
X
m∈Z
ψm ˜ψm+n;
[Jm, Jn] = mδm+n,0.
(4.11)
If scalar function (potential) U(z) is expanded as U(z) =
P
k∈Z tkzk, then
HCartan =
X
n∈Z
tkJk.
(4.12)
