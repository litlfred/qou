---
doc_id: arxiv-hep-th-0306165v1
doc_title: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial"
section_id: sec-011-31-a-polynomial-as-a-lagrangian-submanifold
section_title: "A-polynomial as a Lagrangian Submanifold"
section_number: 3.1
pages: 20-25
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
toc_source: inferred
doc_brief: "Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Polynomial — We study three-dimensional Chern-Simons theory with complex gauge group SL(2,C), which has many interesting connections"
---
In the previous section we described the classical solutions in a SL(2,C) Chern-Simons
theory with a single Wilson loop W(l,m)(K) or, equivalently, the classical solutions in a
theory without the Wilson loop, deﬁned on its complement, M = S3 \ K. In particular,
we found that the classical solutions are parametrized by points on an algebraic curve L,
which is a zero locus of the A-polynomial, A(l, m). Since the knot complement M is a
compact 3-manifold with a single torus boundary, Σ = T 2, there is a natural embedding
L֒ →P
(3.1)
induced by restricting a ﬂat connection from M to Σ. Here, P = C∗× C∗is the moduli
space of representations of π1(Σ) in SL(2,C), parametrized by two complex numbers, l
and m, cf. (2.10).
9 A proper embedding of a connected orientable surface F →M is called incompressible if
the induced map π1(F) →π1(M) is injective.
Its boundary slope is deﬁned as follows.
An
incompressible surface (F, ∂F) gives rise to a collection of parallel simple closed loops in ∂M.
Choose one such loop and write its homology class as γa
l γb
m. Then, the boundary slope of (F, ∂F)
is deﬁned as a rational number a/b.
19
In the Hamiltonian approach [3], one regards P as a classical phase space associated
to a closed surface Σ. Indeed, there is a symplectic structure ω on P derived from the
classical Poisson bracket of gauge ﬁelds in the Chern-Simons theory (1.1). In order to see
this explicitly, let us study the theory on Σ×IR1, i.e. near the boundary of M. On Σ×IR1
it is natural to choose the gauge A0 = 0. Then, the Chern-Simons Lagrangian (1.1), which
in this gauge looks like
I = t
8π
Z
dt
Z
Σ
ǫijTrAi
d
dtAj + t
8π
Z
dt
Z
Σ
ǫijTrAi
d
dtAj
(3.2)
leads to the following Poisson brackets:
{Aa
i (x), Ab
j(y)} = 4π
t · δabǫijδ2(x −y)
{A
a
i (x), A
b
j(y)} = 4π
t · δabǫijδ2(x −y)
(3.3)
These relations induce a Poisson structure on the classical phase space P, which is
parametrized by the SL(2,C) holonomies (2.10) around the longitude γl and the meridian
γm. It is convenient to introduce new variables10 u and v, such that
l = exp(u)
,
m = exp(v)
(3.4)
Since the curves γl and γm intersect transversely in a single point, from (3.3) we ﬁnd (see
also [57,51]):
{u, v} = 4π
t
{u, v} = 4π
t
(3.5)
These relations, together with {u, v} = {u, v} = 0, lead to the following non-trivial
Poisson brackets for the real and imaginary components of u and v:
{Re(v), Re(u)} = {Im(u), Im(v)} = −2π
k
k2 −σ2
{Re(u), Im(v)} = −{Re(v), Im(u)} = i2π
σ
k2 −σ2
(3.6)
Here we also used the explicit expression for the parameters t = k + σ and t = k −σ, both
of which are real in the present discussion.
10 Note, that our deﬁnition of u and v diﬀers from [52,55,56] by a factor of 2.
20
Writing the Poisson brackets (3.6) in the form {xi, xj} = ωij and inverting the con-
stant skew-symmetric matrix ωij, we obtain the corresponding 2-form ω = ωijdxi ∧dxj:
ω = k
π ωk + iσ
π ωσ
(3.7)
where ωk and ωσ are real non-degenerate 2-forms on P, given by
ωk = dRe(v) ∧dRe(u) + dIm(u) ∧dIm(v)
(3.8)
and
ωσ = −dRe(u) ∧dIm(v) + dRe(v) ∧dIm(u)
(3.9)
The diﬀerential 2-form ω is manifestly closed, dω = 0. Also, notice that ω has both real
and imaginary components. If its imaginary part vanishes (that is, if σ ∈iIR), we can
interpret (3.7) as the usual symplectic structure on the phase space P. This system can
be easily quantized by regarding u and v as operators on a certain Hilbert space, HΣ, and
by replacing the Poisson brackets with commutators, { , } →i[ , ]. The resulting eﬀective
quantum mechanics will be discussed in more detail below.
On the other hand, if σ ∈IR (and, say, k = 0), the Poisson structure (3.6) gives
rise to an imaginary 2-form ω = i(σ/π)ωσ, where ωσ is the natural symplectic structure
on P. Indeed, the phase space P = C∗× C∗can be regarded as the total space of the
cotangent bundle (2.12), with the natural symplectic 2-form (3.9). However, since in (3.7)
we have an imaginary multiple of this 2-form, the quantization of this system is more
naturally interpreted as a Euclidean quantum mechanics. In general, if both k and σ are
non-zero, we deal with a mixed situation. Notice, that this subtlety does not appear in a
Chern-Simons theory with real parameter s, which is related to de Sitter gravity in 2+1
dimensions. In this theory, one ﬁnds the Poisson brackets (3.6) with purely real values
on the right-hand side. Therefore, a quantization of such system leads to an ordinary
quantum mechanics on a “non-commutative” 2-torus, parametrized by Im(v) and Im(u).
To summarize, we found that the classical Poisson bracket in the Chern-Simons theory
gives C∞(P) the structure of a Lie algebra over C, and suggests to interpret (P, ω) as a
classical Hamiltonian system. To make this interpretation even more explicit, by a linear
change of variables we can always bring the 2-form ω to the canonical form
ω =
X
i
dpi ∧dqi
(3.10)
21
where qi and pi, i = 1, 2, are the canonical coordinates and momenta (given by linear
combinations of the real and imaginary components of u and v).
In Hamiltonian mechanics, a (semi-)classical state of a system is described by a La-
grangian submanifold in P, that is a middle dimensional subvariety L ⊂P such that the
restriction of ω to L vanishes,
ω|L = 0
(3.11)
In our problem, a character variety L that was deﬁned in (2.15) as the zero locus of the A-
polynomial is a natural candidate for a classical state. Indeed, it is a middle dimensional
subvariety in P which, by deﬁnition, describes the classical ﬁeld conﬁgurations on the
boundary Σ = ∂M that can be extended to a 3-manifold M.
On the other hand, L
is deﬁned as a holomorphic curve in P = C∗× C∗, with respect to its natural complex
structure, rather than a Lagrangian submanifold11. However, by performing a hyperK¨ahler
rotation it is easy to check that L is indeed a Lagrangian submanifold, with respect to the
symplectic structures (3.8) and (3.9) (and, hence, with respect to any linear combination
thereof). Speciﬁcally, we can write the 2-form (3.8) as
ωk = dRe(v) ∧dRe(u) + dIm(u) ∧dIm(v) =
= 1
4(dv + dv) ∧(du + du) −1
4(du −du) ∧(dv −dv) =
= −1
2(du ∧dv + du ∧dv)
(3.12)
Clearly, this 2-form vanishes when restricted to the holomorphic curve A(eu, ev) = 0.
Similarly, one can check that the restriction of the 2-form (3.9) also vanishes
ωσ = −dRe(u) ∧dIm(v) + dRe(v) ∧dIm(u) =
= −1
4i(du + du) ∧(dv −dv) + 1
4i(dv + dv) ∧(du −du) =
= i
2(du ∧dv −du ∧dv)
(3.13)
when restricted to L. Hence, the same is true for any linear combination of ωk and ωσ. In
particular, the condition (3.11) holds for the complex 2-form (3.7).
We conclude that in the SL(2,C) Chern-Simons theory the zero locus L of the A-
polynomial is naturally regarded as a Lagrangian submanifold in the phase space (P, ω).
11 A similar situation occurs in a diﬀerent, though possibly not unrelated context in string
theory [58].
22
Hence, we are naturally led to the quantization of (P, ω) in a real polarization12, where
elements of quantization are associated with Lagrangian submanifolds, cf. [61]. Then, it is
natural to expect that a quantization of this Hamiltonian system gives the quantum Hilbert
space, HΣ, of the SL(2,C) Chern-Simons theory in genus one. In particular, the semi-
classical partition function (1.2) for a 3-manifold M with a single torus boundary, Σ = T 2,
is given by the semi-classical wave function, Z(M) ∈HΣ, supported on the Lagrangian
submanifold L. To be more precise, the partition function Z(M) is a half-density13 on L,
and the resulting quantum system can be naturally viewed as a quantum mechanics on a
“non-commutative” 2-torus. Below, our goal will be to explain this prescription in more
detail and to verify that it leads to meaningful results.
Example. The Figure-eight Knot
As in the previous example, let K be the ﬁgure-eight knot, and let M = S3 \ K be
its complement. For a moment, let us also set k = 0. Then, the Poisson brackets (3.6)
suggest to deﬁne the canonical variables on the four-dimensional phase space P as

p1
p2

=

−Re(u)
Re(v)

and

q1
q2

=

Im(v)
Im(u)

(3.14)
In terms of these variables, the zero locus of the A-polynomial of the ﬁgure-eight knot,
with the factor (l −1) included, is given by

cosh(4p2 + 4iq1) −cosh(2p2 + 2iq1) −cosh(p1 −iq2) −1
  eiq2−p1 −1
= 0
(3.15)
This complex equation deﬁnes two real constraints in a dynamical system with trivial
Hamiltonian, whose quantization leads to an eﬀective quantum mechanics on a torus,
parametrized by q1 and q2. When the parameter s in the Chern-Simons action (1.1) is
real, one ﬁnds ordinary quantum mechanics, whereas for imaginary values of s (i.e. for
s = −iσ) the resulting system is best described as a Euclidean quantum mechanics. In
both cases, turning on the ‘level’ k leads to a deformation of the Poisson structure (3.6),
which can be naturally interpreted as a non-commutativity of the torus coordinates, q1
and q2 (as well as momenta, p1 and p2).
12 For quantization of Chern-Simons theory in complex polarizations see [1,59,60,37].
13 Given an n-dimensional manifold X, let BX denote the frame bundle of V = TX; its structure
group is GL(V ). Then, an r-density on X is a smooth function f: BX →C which transforms
under the action of GL(V ) as f ◦g = |Det(g)|rf, where g ∈GL(V ) and Det(g) is the determinant
of g. For r = 1 this deﬁnition gives the usual density on X, and for r = 1/2 it gives a half-density
on X.
23
Before we proceed, let us brieﬂy point out that the Chern-Simons action induces
SL(2,C)/SU(2) WZW theory on the boundary manifold Σ. However, the structure of the
Hilbert space in this theory is not completely clear at present. One might hope to get
further insights from the present approach.
