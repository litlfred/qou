---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-021
section_title: "Page 21"
section_number: null
pages: 21-21
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Deﬁnition 4.6. Fix an arbitrary subset J ⊆N, where N = {1, 2, . . .}. For any
partition ρ, set
|ρ|J = |ρ| +
X
j∈J
mj(ρ).
In particular, in the two extreme cases we have
|ρ|∅= |ρ|,
|ρ|N = |ρ| + ℓ(ρ).
Next, following [IK], deﬁne a ﬁltration of the vector space A by setting
degJ(p#
ρ ) = |ρ|J
and, more generally, for any f = P
ρ fρp#
ρ ∈A,
degJ(f) = max
ρ: fρ̸=0 |ρ|J .
Proposition 4.7. For any J ⊆N, the ﬁltration by degJ( · ) as deﬁned above is
compatible with the multiplication in A. I.e., for any partitions ρ, σ, τ,
f ρ
στ̸ = 0 =⇒|ρ|J ≤|σ|J + |τ|J ,
so that this is an algebra ﬁltration.
Proof. The argument presented below is a slightly rewritten version of that given
in [IK, Proposition 10.3].
Assume we are given partitions ρ, σ, τ such that f ρ
στ̸ = 0. Fix a set X and a
permutation s : X →X as in the statement of Proposition 4.5. By that proposition,
there exists a quadruple {X1, s1, X2, s2} satisfying the four conditions (i)–(iv). Fix
any such quadruple.
Decompose each of the permutations s, s1, s2 into cycles and denote by CJ( · )
the set of all cycles whose lengths belong to the set J. Write
CJ(s1) = AJ(s1) ⊔BJ(s1),
CJ(s2) = AJ(s2) ⊔BJ(s2),
(4.2)
where AJ(s1) ⊆CJ(s1) denotes the subset of those cycles of s1 that are entirely
contained in X1 \ X2, while BJ(s1) ⊆CJ(s1) denotes the subset of those cycles
of s1 that have a nonempty intersection with X1 ∩X2. (Note that we count ﬁxed
points viewed as cycles of length 1, provided that 1 ∈J.) The sets AJ(s2) and
BJ(s2) are deﬁned similarly.
In this notation we have
CJ(s) = AJ(s1) ⊔AJ(s2) ⊔BJ(s),
(4.3)
where BJ(s) is the set of those cycles in CJ(s) that intersect both X1 and X2.
Remark that
|ρ|J = |X| + |CJ(s)|,
|σ|J = |X1| + |CJ(s1)|,
|τ|J = |X2| + |CJ(s2)|.
21
