---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-030-85-homology-of-cyclic-covers
section_title: "Homology of cyclic covers"
section_number: 8.5
pages: 28-29
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
νK ; Z[t±1]) its Alexander module. Given n ∈ N we denote by Ln then–fold cyclic branched
cover of K. Recall that we have a canonical isomorphism H/(tn − 1) ∼
= H1(Ln). Put
diﬀerently, the Alexander module determines the homology of the branched covers. In the
same vein, the following formula due to Fox ([Fo56] and see al so [Go78]) shows that the
Alexander polynomial determines the size of the homology of a branched cover:
(1) |H1(Ln)| =
⏐
⏐
⏐
⏐
⏐
⏐
n−1∏
j=1
∆ K(e2πij/n )
⏐
⏐
⏐
⏐
⏐
⏐
.
Here we write |H1(Ln)| = 0 if H1(Ln) has positive rank. Gordon [Go72] used this formula
to study extensively the homology of the branched covers of a knot. Gordon [Go72, p. 366]
asked whether the non–zero values of the sequence |H1(Ln)| converge to inﬁnity if there
exists a zero of the Alexander polynomial which is not a root o f unity.
Given a multivariable polynomial p :=p(t1,...,t n) ∈ C[t±1
1 ,...,t ±1
n ] the Mahler measure
is deﬁned as
m(p) = exp
∫ 1
θ1=0
...
∫ 1
θn=0
log
⏐
⏐
⏐p
(
e2πiθ1,...,e 2πiθ1
) ⏐
⏐
⏐dθ1...dθ n.
Note that the integral can be singular, but one can show that t he integral always converges.
It is known (cf. e.g. [SW02]) that an integral one variable po lynomial p always satisﬁes
m(p) ≥ 1, and it satisﬁes m(p) = 1 if and only if all zeroes of p are roots of unity.
Theorem 8.5. LetK be any knot, then
lim
n→∞
1
n log|TorH1(Ln)| = log(m(∆ K (t))).
A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS 29
This theorem was proved for most cases by Gonz´ alez-Acu˜ na and Short [GS91], the most
general statement was proved by Silver and Williams [SW02, T heorem 2.1]. We also refer
to [Ri90] for a related result. Note that by the above discuss ion this theorem in particular
implies the aﬃrmative answer to Gordon’s question.
Silver and Williams also generalized this theorem to links ( [SW02, Theorem 2.1]), relating
the Mahler measure multivariable Alexander polynomial to t he homology growth of ﬁnite
abelian covers of the link. Finally in [SW09c, Section 3] the se results are extended to the
twisted case for certain representations (e.g. integral re presentations). We refer to [SW09c,
Section 3] for the precise formulations and to [SW09c, Secti on 5] for an interesting example.
8.6. Alexander polynomials for links in RP 3. Given a link L ⊂ RP 3 Huynh and Le
[HL08, Section 5.3.2] use Reidemeister torsion correspond ing to abelian representations to
deﬁne an invariant ∇L(t) which lies in general in Z[t±1, (t −t−1)−1] and has no indetermi-
nacy. Furthermore they show in [HL08, Theorem 5.7] the surpr ising fact that this invariant
satisﬁes in fact a skein relation.
