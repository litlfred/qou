---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-044-151-the-hyperﬁnite-type-ii1-factor-r
section_title: "The hyperﬁnite type II1 factor R"
section_number: 15.1
pages: 109-112
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
The hyperﬁnite type II1 factor R
The ﬁrst main result about hyperﬁniteness was proved by Murray and von
Neumann in []. We will use R to denote the hyperﬁnite II1 factor whose
uniqueness they proved.
Theorem 15.1.1. Up to abstract isomorphism there is a unique hyperﬁnite
II1 factor.
Sketch of proof. One works with the norm ||x||2 = tr(x∗x)1/2 on M. It is
not hard to show that a von Neumann subalgebra N of M is strongly dense
in M iﬀit is dense in ||−||2. Given a subalgebra A of M and a subset S ⊆M
one says
S
⊆
A
ε
if for each x ∈S there is a y ∈A with ||x −y||2 < ε.
The hyperﬁniteness condition then implies:
For every ﬁnite subset S ⊆M and every ε > 0 there is a ﬁnite dimen-
sional *-subalgebra A of M with
S
⊆
A.
ε
109
The next step is to show that the A in the preceeding condition can be
chosen to be the 2n × 2n matrices for some (possibly very large) n. This part
uses what might be described as “II1 factor technique”. One begins with A
and approximates all its minimal projections {ei} by ones whose traces are
numbers of the form k/2n. The matrix units of A can be changed a little bit
in || −||2 so that, together with matrix units conecting projections of trace
1/2n less than the ei, they generate a 2n×2n matrix algebra containing, up to
ε, the matix units of A. Perturbation of the matrix units will involve results
of the form:
If u ∈M satisﬁes ||(uu∗)2 −uu∗||2 < ϵ then there is a partial isometry
v ∈M with ||v −u||2 < F(ϵ)
(for some nice function f with f(0) = 0).
or:
If p and q are projections with ||pq||2 < ϵ then there is a projection q′ with
pq′ = 0 and ||q −q′|| < F(ϵ).
or:
If fij are “almost n × n matrix units”, i.e.
(a) ||fij −fji||2 < ϵ
(b) ||fijfkl −δj,kfil||2 < ϵ
(c) ||1 −Pn
i=1 fii||2 < ϵ
then there are n×n matrix units eij with ||eij −fij|| < F(ϵ) where F depends
only on n and F(0) = 0.
Such results are proved by a skilful use of the polar decomposition and
spectral theorem.
Thus one shows that in a hyperﬁnite type II1 factor one has:
Property * :
For every ﬁnite subset S ⊆M and every ε > 0 there is a
2n × 2n matrix subalgebra of M with
S
⊆
A.
ε
One may now proceed to prove the theorem by choosing a || −||2-dense
sequence xk in M and inductively constructing an increasing sequence of
2nk × 2nk matrix algebras Ak with the property that
For each k = 1, 2, 3, ...,
{x1, x2, ..., xk}
⊆
Ak .
1/k
110
The union of the Ak’s is clearly dense in || −||2. This is enough to prove
the theorem since the Ak’s can be used to give an isomorphism of M with
the type II1 factor ⊗∞M2(C) constructed in section 6.2.
To construct Ak+1 from Ak one needs to arrange for the new algebra
to contain the one already constructed. So to the elements x1, x2, ..., xk+1,
add matrix units eij for Ak+1. Now use property * to obtain a B almost
containing the xi and the matrix units, with ϵ small enough to control sums
over the matrix units eij. In B we know there are approximate matrix units
close to the eij so by a technical lemma, exact matrix units fij close to the
eij. Now choose a unitary close to the identity which conjugates the fij to
the eij and use this unitary to conjugate B to a superalgebra of Ak. This
superalgebra is Ak+1 and it contains the xi up to epsilon since u is close to
the identity.
This completes the sketch of the proof. The technique involved is con-
sidered standard in von Neumann algebras and the details can be found in
.
dixmier
Corollary 15.1.2. If S∞is the group of ﬁnitely supported permutations of
a countably inﬁnite set then vN(S∞) ∼= ⊗∞M2(C).
Proof. The subgroups of S∞permuting an increasing sequence of ﬁnite sets
show that vN(S∞) is hyperﬁnite.
It is surprising at ﬁrst sight that the type II1 factor L∞(X, µ)⋊Z obtained
from an ergodic measure-preserving transformation T is hyperﬁnite. This can
be shown by Rokhlin’s tower theorem which asserts that, for each n ∈N and
each ϵ > 0 there is a measurable subset A ⊆X with
(1) T i(A) ∩T j(A) = ∅for 1 ≤i < j ≤n,
and
(2) µ(X \ ∪n
i=0T i(A)) < ϵ.
The unitary u1 of the crossed product and the characteristic function of A
can be combined, with a little perturbation to get the identity, to get a n×n
matrix algebra. Careful application of the tower theorem will allow one to
get any element of L∞(X, µ), and u1, in this matrix algebra up to some ϵ.
This was ﬁrst proved by Henry Dye in who went on to prove that in fact all
Dye
groups of polynomial growth give hyperﬁnite II1 factors in this way.
The ultimate result in this direction is the celebrated “Injective factors”
theorem of Connes who showed that hyperﬁniteness for a von Neumann al-
gebra M on H is equivalent to “injectivity” which means there is a projection
in the Banach space sense of norm one from B(H) onto M. This theorem,
whose proof is a great, great tour de force, has a raft of corollaries, many of
111
which were open questions. Let us just mention the fact that it follows easily
that any subfactor of R which is inﬁnite dimensional is in fact isomorphic to
R. It also implies that vN(Γ), as well as L∞(X, µ) ⋊Γ is hyperﬁnite as soon
as Γ is amenable.
