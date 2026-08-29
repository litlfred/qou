---
doc_id: hal-01215114
doc_title: "FPSAC 2011, Reykjavík, Iceland DMTCS proc. AO, 2011, 317–328 Dual combinatorics of zonal polynomials"
section_id: sec-002-notations
section_title: "Notations"
section_number: null
pages: 2-3
source_pdf: hal-01215114.pdf
source_sha256: c70f8b04a5542a1f
doc_brief: "FPSAC 2011, Reykjavík, Iceland DMTCS proc. AO, 2011, 317–328 Dual combinatorics of zonal polynomials — In this paper we establish a new combinatorial formula for zonal polynomials in terms of"
---
In this section, we give some deﬁnitions and notations on symmetric functions in general, on Jack poly-
nomials and, in particular, zonal polynomials. We also give a few deﬁnitions of pair-partitions, which are
the combinatorial objects involved in our formulas.
2.1 Symmetric functions
As much as possible, we use the notations of I.G. Macdonald’s book [Mac95].
By deﬁnition, a partition λ = (λ1,λ 2,... ) of the integer n is a non-increasing sequence of non-
negative integers of sumn. Its length𝓁(λ) is the number of non-zero terms in the sequence. Fori≥ 1 we
denote bymi(λ) the number of occurrences of i inλ. Finally, let us deﬁne aut(λ) :=∏
i≥1mi(λ)! and
zλ = aut(λ)·∏
jλj.
The ring Λ of symmetric functions has several classical linear bases, all indexed by partitions:
• monomial symmetric functions: let us use for monomials the short notation xv =xv1
1 xv2
2 ... , then
mλ :=
∑
v∈S∞(λ)
xv,
where the sum runs over all vectors v which are permutations ofλ (without multiplicities);
• power-sum symmetric functions: they are deﬁned by
p0 = 1, p k =
∑
i
xk
i, p µ =
∏
j
pµj;
• Schur functions (sλ): they have several equivalent deﬁnitions, one of them will be given in the next
paragraph.
In addition to the additive and multiplicative structures, the ring of symmetric functions can be endowed
with a scalar product (called Hall scalar product), for which:
⟨pλ,pµ⟩ =zλδλ,µ, ⟨sλ,sµ⟩ =δλ,µ.
Dual combinatorics of zonal polynomials 319
