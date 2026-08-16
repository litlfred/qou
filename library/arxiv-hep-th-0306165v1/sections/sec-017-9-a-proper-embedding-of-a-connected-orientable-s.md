---
doc_id: arxiv-hep-th-0306165v1
doc_title: "which has many interesting connections with three-dimensi onal quantum gravity and ge- ometry of hyperbolic 3-manifolds. We show that, in the prese nce of a single knotted Wilson l"
section_id: sec-017-9-a-proper-embedding-of-a-connected-orientable-s
section_title: "A proper embedding of a connected orientable surface F → M is called incompressible if"
section_number: 9
pages: 20-23
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting connections with three-dimensi onal quantum gravity"
---
the induced map π1(F ) → π1(M ) is injective. Its boundary slope is deﬁned as follows. An
incompressible surface ( F, ∂F ) gives rise to a collection of parallel simple closed loops i n ∂M .
Choose one such loop and write its homology class as γa
l γb
m. Then, the boundary slope of ( F, ∂F )
is deﬁned as a rational number a/b.
19
In the Hamiltonian approach [3], one regards P as a classical phase space associated
to a closed surface Σ. Indeed, there is a symplectic structur e ω onP derived from the
classical Poisson bracket of gauge ﬁelds in the Chern-Simon s theory (1.1). In order to see
this explicitly, let us study the theory on Σ × I R1, i.e. near the boundary of M . On Σ × I R1
it is natural to choose the gauge A0 = 0. Then, the Chern-Simons Lagrangian (1.1), which
in this gauge looks like
I = t
8π
∫
dt
∫
Σ
ǫijTrAi
d
dtAj + t
8π
∫
dt
∫
Σ
ǫijTrAi
d
dtAj (3.2)
leads to the following Poisson brackets:
{Aa
i (x),Ab
j(y)} = 4π
t ·δabǫijδ2(x−y)
{A
a
i (x),
A
b
j(y)} = 4π
t ·δabǫijδ2(x−y)
(3.3)
These relations induce a Poisson structure on the classical phase space P, which is
parametrized by the SL(2,C) holonomies (2.10) around the longitude γl and the meridian
γm. It is convenient to introduce new variables 10 u and v, such that
l = exp(u) , m = exp(v) (3 .4)
Since the curves γl andγm intersect transversely in a single point, from (3.3) we ﬁnd ( see
also [57,51]):
{u,v} = 4π
t
{u,v} = 4π
t
(3.5)
These relations, together with {u,v} ={u,v} = 0, lead to the following non-trivial
Poisson brackets for the real and imaginary components of u and v:
{Re(v), Re(u)} ={Im(u), Im(v)} =−2π k
k2−σ2
{Re(u), Im(v)} =−{Re(v), Im(u)} =i2π σ
k2−σ2
(3.6)
Here we also used the explicit expression for the parameters t =k +σ andt =k−σ, both
of which are real in the present discussion.
10 Note, that our deﬁnition of u and v diﬀers from [52,55,56] by a factor of 2.
20
Writing the Poisson brackets (3.6) in the form {xi,x j} = ωij and inverting the con-
stant skew-symmetric matrix ωij, we obtain the corresponding 2-form ω =ωijdxi∧dxj:
ω = k
πωk +iσ
πωσ (3.7)
where ωk and ωσ are real non-degenerate 2-forms on P, given by
ωk =dRe(v)∧dRe(u) +dIm(u)∧dIm(v) (3 .8)
and
ωσ =−dRe(u)∧dIm(v) +dRe(v)∧dIm(u) (3 .9)
The diﬀerential 2-form ω is manifestly closed, dω = 0. Also, notice that ω has both real
and imaginary components. If its imaginary part vanishes (t hat is, if σ∈ iI R), we can
interpret (3.7) as the usual symplectic structure on the pha se space P. This system can
be easily quantized by regarding u andv as operators on a certain Hilbert space, HΣ , and
by replacing the Poisson brackets with commutators, {,}→ i[, ]. The resulting eﬀective
quantum mechanics will be discussed in more detail below.
On the other hand, if σ ∈ I R (and, say, k = 0), the Poisson structure (3.6) gives
rise to an imaginary 2-form ω = i(σ/π)ωσ , where ωσ is the natural symplectic structure
onP. Indeed, the phase space P = C∗× C∗ can be regarded as the total space of the
cotangent bundle (2.12), with the natural symplectic 2-for m (3.9). However, since in (3.7)
we have an imaginary multiple of this 2-form, the quantizati on of this system is more
naturally interpreted as a Euclidean quantum mechanics. In general, if both k and σ are
non-zero, we deal with a mixed situation. Notice, that this s ubtlety does not appear in a
Chern-Simons theory with real parameter s, which is related to de Sitter gravity in 2+1
dimensions. In this theory, one ﬁnds the Poisson brackets (3 .6) with purely real values
on the right-hand side. Therefore, a quantization of such sy stem leads to an ordinary
quantum mechanics on a “non-commutative” 2-torus, paramet rized by Im(v) and Im(u).
To summarize, we found that the classical Poisson bracket in the Chern-Simons theory
gives C∞(P) the structure of a Lie algebra over C, and suggests to interpret ( P,ω ) as a
classical Hamiltonian system. To make this interpretation even more explicit, by a linear
change of variables we can always bring the 2-form ω to the canonical form
ω =
∑
i
dpi∧dqi (3.10)
21
where qi and pi, i = 1, 2, are the canonical coordinates and momenta (given by linea r
combinations of the real and imaginary components of u andv).
In Hamiltonian mechanics, a (semi-)classical state of a sys tem is described by a La-
grangian submanifold in P, that is a middle dimensional subvariety L⊂P such that the
restriction of ω to L vanishes,
ω|L = 0 (3 .11)
In our problem, a character variety L that was deﬁned in (2.15) as the zero locus of the A-
polynomial is a natural candidate for a classical state. Ind eed, it is a middle dimensional
subvariety in P which, by deﬁnition, describes the classical ﬁeld conﬁgura tions on the
boundary Σ = ∂M that can be extended to a 3-manifold M . On the other hand, L
is deﬁned as a holomorphic curve in P = C∗× C∗, with respect to its natural complex
structure, rather than a Lagrangian submanifold 11. However, by performing a hyperK¨ ahler
rotation it is easy to check that L is indeed a Lagrangian submanifold, with respect to the
symplectic structures (3.8) and (3.9) (and, hence, with res pect to any linear combination
thereof). Speciﬁcally, we can write the 2-form (3.8) as
ωk =dRe(v)∧dRe(u) +dIm(u)∧dIm(v) =
= 1
