---
doc_id: arxiv-math-9909088v1
doc_title: "The Gauss Map and a Noncompact Riemann-Roch Formula for Constructible Sheaves on Semiabelian Varieties"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: 9909088v1.pdf
source_sha256: 52cfb568951f195f
toc_source: undetermined
doc_brief: "The Gauss Map and a Noncompact Riemann-Roch Formula for Constructible Sheaves on Semiabelian Varieties — For an irreducible subvariety Z in an algebraic group G we deﬁne an integer gdeg(Z) ≥0 as the"
---
6
J. FRANECKI, M. KAPRANOV
For ν = 0, . . . , n let An
ν ⊂P n be the aﬃne chart given by tν̸ = 0. This is an aﬃne
space with coordinates z(ν)
i
, i ∈{0, . . . , n} \ {ν} given by z(ν)
i
= ti
tν . Denote by
(C∗)n jν֒→An
ν
kν֒→P n
the embeddings. For ν = 0 we have z(0)
i
= zi.
We now apply Theorem 3.4 to U = (C∗)n, X = An
0, fi = zi, and our constructible
complex F. The recipe of the theorem requires us to introduce the family of 1-forms
ωs =
n
X
i=1
si d log zi , s = (s1, . . . , sn) ∈(C∗)n.
These forms are precisely the invariant 1-forms on G = (C∗)n. We can view s as
an element of g∗, where g = Cn is the Lie algebra of G. Theorem 3.4 then gives us:
(4.1)
CC(Rj0∗F) = CC(Rj∗F)|An
0 = lim
s→0(CC(F) + ωs),
the limit being taken in T ∗An
0.
Next, we apply Theorem 3.4 to U = (C∗)n and X = An
ν with arbitrary ν ∈
{0, . . . , n}. Then we should take fi = z(ν)
i
, i ∈{0, . . . , n} \ {ν} and consider the
1-forms
ω(ν)
s′
=
X
i̸=ν
s′
i d log z(ν)
i
, s′ ∈(C∗){0,...,n}\{ν}.
Now, each z(ν)
i
is a Laurent monomial in the z1, . . . , zn, so d log z(ν)
i
is an (integer)
linear combination of d log z1, . . . , d log zn. Therefore, ω(ν)
s′
= ωs where s = φν(s′)
is an image of s under a linear transformation φν : C{0,...,n}\{ν} →Cn. It is clear
that φν is invertible; in particular, s →0 iﬀs′ →0. This means that the answers
given by Theorem 3.4 for the CC(Rjν∗F), glue together into one global answer:
(4.2)
CC(Rj∗F) = lim
s→0
s∈E
(CC(F) + ωs).
Here the limit is taken in T ∗P n and s runs over the set
E = {(s1, . . . , sn) ∈(C∗)n : si̸ = sj , i̸ = j}.
(The condition s ∈E is equivalent to φ−1
ν (s) ∈(C∗){0,...,n}\{ν} for any ν.)
Now, Theorem 1.3 for G = (C∗)n would follow from (4.2) and the next lemma.
(4.3) Lemma. Let Λ ⊂T ∗(C∗)n be an irreducible conic Lagrangian variety. Then
lim
s→0
s∈E
(Λ + ωs), [P n])T ∗Pn = gdeg(Λ).
Proof: Let Ωs ⊂T ∗(C∗)n be the graph of ωs. If s ∈E, then Ωs is closed in T ∗Pn
as well. By translation, intersecting Λ + ωs with [P n] is equivalent to intersecting
Λ with Ω−s. By Proposition 2.2, there exists a Zariski open, nonempty set F ⊂Cn
such that for s(0) ∈F the intersection Λ ∩Ω−s(0) consists of gdeg(Λ) smooth
transverse points. Since E is also Zariski open, F ∩E meets any polydisk
Pε = {(z1, . . . , zn) ∈(C∗)n : 0 < |zi| < ε}
in an open dense set. By the “continuity of intersection” it follows that for |ε| ≪1
and s(0) ∈Pε ∩F ∩E

lim
s→0
s∈E
Λ + ωs), [P n]

T ∗P n= |Ω−s(0) ∩Λ| = gdeg(Λ)
and this completes the proof.
