---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California"
section_id: sec-002-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-4
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
doc_brief: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California — We introduce a notion of planar algebra, the simplest exampl e of which is a vector space of tensors, closed"
---
At ﬁrst glance there is nothing planar about a subfactor. A fa ctor M is a
unital ∗-algebra of bounded linear operators on a Hilbert space, wit h trivial
centre and closed in the topology of pointwise convergence. The factor M is
of type II 1 if it admits a (normalized) trace, a linear function tr: M → C with
tr(ab) = tr(ba) and tr(1) = 1. In [J1] we deﬁned the notion of index [M : N]
for II 1 factors N ⊂ M. The most surprising result of [J1] was that [ M : N]
is “quantized” — to be precise, if [ M : N] < 4 there is an integer n ≥ 3
with [ M : N] = 4 cos 2 π/n. This led to a surge of interest in subfactors and
the major theorems of Pimsner, Popa and Ocneanu ([PP],[Po1] ,[O1]). These
results turn around a “standard invariant” for ﬁnite index s ubfactors, also
known variously as the “tower of relative commutants”, the “ paragroup”, or
the “ λ-lattice”. In favorable cases the standard invariant allow s one to recon-
struct the subfactor, and both the paragroup and λ-lattice approaches give
∗Research supported in part by NSF Grant DMS93–22675, the Mar sden fund UOA520,
and the Swiss National Science Foundation.
1
complete axiomatizations of the standard invariant. In thi s paper we give,
among other things, yet another axiomatization which has th e advantage of
revealing an underlying planar structure not apparent in other approaches.
It also places the standard invariant in a larger mathematic al context. In
particular we give a rigorous justiﬁcation for pictorial pr oofs of subfactor
theorems. Non-trivial results have already been obtained f rom such argu-
ments in [BJ1]. The standard invariant is suﬃciently rich to justify several
axiomatizations — it has led to the discovery of invariants i n knot theory
([J2]), 3-manifolds ([TV]) and combinatorics ([NJ]), and i s of considerable
interest in conformal and algebraic quantum ﬁeld theory ([W a],[FRS],[Lo]).
Let us now say exactly what we mean by a planar algebra. The bes t
language to use is that of operads ([Ma]). We deﬁne the planar operad ,
each element of which determines a multilinear operation on the standard
invariant.
A planar k-tangle will consist of the unit disc D (= D0) in C together with
a ﬁnite (possibly empty) set of disjoint subdiscs D1, D2, . . . , Dn in the interior
of D. Each disc Di, i ≥ 0, will have an even number 2 ki ≥ 0 of marked
points on its boundary (with k = k0). Inside D there is also a ﬁnite set
of disjoint smoothly embedded curves called strings which are either closed
curves or whose boundaries are marked points of the Di’s. Each marked
point is the boundary point of some string, which meets the bo undary of the
corresponding disc transversally. The strings all lie in th e complement of the
interiors
◦
Di of the Di, i ≥ 0. The connected components of the complement
of the strings in
◦
D \
n⋃
i=1
Di are called regions and are shaded black and white
so that regions whose closures meet have diﬀerent shadings. The shading
is part of the data of the tangle, as is the choice, at every Di, i ≥ 0, of a
white region whose closure meets that disc. The case k = 0 is exceptional
- there are two kinds of 0-tangle, according to whether the re gion near the
boundary is shaded black or white. An example of a planar 4-ta ngle, where
the chosen white regions are marked with a ∗ close to their respective discs,
is given below.
2
D6
∗D1
D2
D3
∗
D4
∗
D5
∗
∗
∗
∗
D7
∗
The planar operad P is the set of all orientation-preserving diﬀeomorphism
classes of planar k tangles, k being arbitrary. The diﬀeomorphisms preserve
the boundary of D but may move the Di’s, i > 1.
Given a planar k tangle T , a k′-tangle S, and a disk Di of T with ki = k′
we deﬁne the k tangle T ◦i S by isotoping S so that its boundary, together
with the marked points, coincides with that of Di, and the chosen white
regions for Di (in T ) and S share a boundary segment. The strings may
then be joined at the boundary of Di and smoothed. The boundary of Di is
then removed to obtain the tangle T ◦i S whose diﬀeomorphism class clearly
depends only on those of T and S. This gives P the structure of a coloured
operad, where each Di for i > 0 is assigned the colour ki and composition
is only allowed when the colours match. There are two distinc t colours for
k = 0 according to the shading near the boundary. The Di’s for i ≥ 1 are
to be thought of as inputs and D0 is the output. (In the usual deﬁnition of
an operad the inputs are labelled and the symmetric group Sn acts on them.
Because of the colours, Sn is here replaced by Sn1 × Sn2 × . . . × Snp where
nj is the number of internal discs coloured j. Axioms for such a coloured
operad could be given along the lines of [Ma] but we do not need them since
we have a concrete example.) The picture below exhibits the c omposition
3
T = S =
T ◦2 S
∗
∗
∗∗
∗
∗
D1
∗
∗
D5
D4
∗
D3
∗
∗
∗
D4
D5
D3
D1
D2
The most general notion of a planar algebra that we will conte mplate is
that of an algebra over P in the sense of [Ma]. That is to say, ﬁrst of all, a
disjoint union Vk of vector spaces for k > 0 and two vector spaces V white
0 and
V black
