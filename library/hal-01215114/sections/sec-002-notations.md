---
doc_id: hal-01215114
doc_title: "FPSAC 2011, Reykjavík, Iceland"
section_id: sec-002-notations
section_title: "Notations"
section_number: null
pages: 2-3
source_pdf: hal-01215114.pdf
source_sha256: c70f8b04a5542a1f
toc_source: outline
doc_brief: "FPSAC 2011, Reykjavík, Iceland — In this paper we establish a new combinatorial formula for zonal polynomials in terms of power-sums. The proof relies on the sign-reversing involution principle."
---
Notations
In this section, we give some deﬁnitions and notations on symmetric functions in general, on Jack poly-
nomials and, in particular, zonal polynomials. We also give a few deﬁnitions of pair-partitions, which are
the combinatorial objects involved in our formulas.
2.1
Symmetric functions
As much as possible, we use the notations of I.G. Macdonald’s book [Mac95].
By deﬁnition, a partition λ = (λ1, λ2, . . . ) of the integer n is a non-increasing sequence of non-
negative integers of sum n. Its length ℓ(λ) is the number of non-zero terms in the sequence. For i ≥1 we
denote by mi(λ) the number of occurrences of i in λ. Finally, let us deﬁne aut(λ) := Q
i≥1 mi(λ)! and
zλ = aut(λ) · Q
j λj.
The ring Λ of symmetric functions has several classical linear bases, all indexed by partitions:
• monomial symmetric functions: let us use for monomials the short notation xv = xv1
1 xv2
2 . . . , then
mλ :=
X
v∈S∞(λ)
xv,
where the sum runs over all vectors v which are permutations of λ (without multiplicities);
• power-sum symmetric functions: they are deﬁned by
p0 = 1,
pk =
X
i
xk
i ,
pµ =
Y
j
pµj;
• Schur functions (sλ): they have several equivalent deﬁnitions, one of them will be given in the next
paragraph.
In addition to the additive and multiplicative structures, the ring of symmetric functions can be endowed
with a scalar product (called Hall scalar product), for which:
⟨pλ, pµ⟩= zλδλ,µ,
⟨sλ, sµ⟩= δλ,µ.
Dual combinatorics of zonal polynomials
319
