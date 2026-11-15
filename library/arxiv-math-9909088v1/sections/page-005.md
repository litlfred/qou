---
doc_id: arxiv-math-9909088v1
doc_title: "The Gauss Map and a Noncompact Riemann-Roch Formula for Constructible Sheaves on Semiabelian Varieties"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: 9909088v1.pdf
source_sha256: 52cfb568951f195f
toc_source: undetermined
doc_brief: "The Gauss Map and a Noncompact Riemann-Roch Formula for Constructible Sheaves on Semiabelian Varieties — For an irreducible subvariety Z in an algebraic group G we deﬁne an integer gdeg(Z) ≥0 as the"
---
NONCOMPACT RIEMANN-ROCH
5
For a point s = (s1, . . . , sn) ∈(C∗)n and a conic Lagrangian variety Λ ⊂T ∗U
we form, similarly to (3.1), a non-conic Lagrangian variety
(3.3)
Λ#
s = Λ +
n
X
i=1
sid log fi ⊂T ∗X.
The total space of this family lies in T ∗X ×(C∗)n. Taking the closure in T ∗X ×Cn
and then intersecting with T ∗X × {(0, . . . , 0)} deﬁnes, similarly to the above, a
conic Lagrangian cycle
lim
s→(0,...,0) Λ#
s . Of course, this “limit” could be taken along
any curve in Cn passing through 0 and generically lying in (C∗)n. As before, we
extend this construction by linearity to conic Lagrangian cycles in T ∗U. The next
statement follows by iterated application of Theorem 3.2.
(3.4) Theorem. If F is a bounded constructible complex on U, then
CC(Rj∗F) =
lim
s→(0,...,0) CC(F)#
s , s = (s1, . . . , sn) ∈(C∗)n.
Taking the limit along diﬀerent curves approaching (0, . . . , 0) corresponds, roughly,
to diﬀerent choices of our equation for the reducible hypersurface X \U. For exam-
ple, restricting to the curve with parametric equation si = tmi, mi > 0 corresponds
to taking Q
i f mi
i
as an equation.
We now need a slight globalization of Theorem 3.4. First of all, let (L, ∇) be a
line bundle on X with an algebraic ﬂat connection. If f is a regular section of L,
then f −1∇f is a scalar 1-form regular over the open set {f̸ = 0}. We denote this
form ∇log f.
Suppose now that we have n line bundles with ﬂat connections (Li, ∇i) on X,
i = 1, . . . , n. Suppose fi ∈Γ(X, Li), i = 1, . . . , n and U ⊂X is the intersection of
the open sets {fi̸ = 0}. As before, let j : U֒ →X be the embedding.
(3.5) Theorem. For a bounded constructible complex F on U we have
CC(Rj∗F) =
lim
s→(0,...,0)

CC(F) +
n
X
i=1
si∇i log fi

.
Proof:
As before, it is enough to consider the case n = 1, as the general case
can be obtained by iteration, as in [9], Appendix A. The statement for n = 1 is
a consequence of Theorem 6.3 of [8] which deals with the more general case of
the zero locus of a section f of an arbitrary line bundle L, not necessarily with
connection. The recipe in this case is to consider the “twisted cotangent bundles”
(T ∗X)(s), s ∈C, deﬁned as the symplectic quotients of T ∗L by the hamiltonian
action of C∗induced by dilations of L. Now, if L is equipped with a ﬂat connection
∇, then all the (T ∗X)(s) become identiﬁed with T ∗X and the formulation of [8],
Theorem 6.3 reduces to our statement.
4. Proof of Theorem 1.3 for G = (C∗)n
We ﬁrst consider the case when G = (C∗)n is an algebraic torus. Let z1, . . . , zn,
zi̸ = 0, be the standard coordinates in (C∗)n. We compactify G by the projective
space P n with homogeneous coordinates (t0 : · · · : tn) by
j : (C∗)n֒ →P n , (z1, . . . , zn) 7→(1 : z1 : · · · : zn)
