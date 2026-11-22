---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-020
section_title: "Page 20"
section_number: null
pages: 20-20
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Proposition 4.2. For any partition ρ, the function p#
ρ introduced in Deﬁnition 4.1
is an element of A. In the canonical grading, the top degree homogeneous component
of p#
ρ equals pρ.
Proof. Diﬀerent proofs are given in [KO] and [OO]. See also [IK], [LaT], [ORV].
□
Corollary 4.3. The elements p#
ρ form a basis in A.
Note that this basis is inhomogeneous both in the canonical grading and the
weight grading.
Given two partitions σ, τ, we denote by σ ∪τ the partition obtained by joining
the parts of both partitions and then arranging them in descending order. In other
words, σ ∪τ is characterized by
mi(σ ∪τ) = mi(σ) + mi(τ),
i = 1, 2, . . . .
Corollary 4.4. For any partitions σ, τ,
p#
σ p#
τ = p#
σ∪τ + . . . ,
where dots mean lower degree terms with respect to the canonical grading.
Here and in what follows we deﬁne the degree of an inhomogeneous element as
the maximal degree of its nonzero homogeneous components. In other words, we
switch from the grading to the corresponding ﬁltration.
Later on it will be shown that the claim of Corollary 4.4 also holds for the weight
grading (or ﬁltration), see Propositions 4.9 and 4.10.
Let f ρ
στ denote the structure constants of the algebra A in the basis {p#
ρ }. I.e.,
p#
σ p#
τ =
X
ρ
f ρ
στ p#
ρ .
By Corollary 4.4, f ρ
στ̸ = 0 implies |ρ| ≤|σ| + |τ|. Moreover,
f σ∪τ
στ
= 1.
(4.1)
Recall the conventional notation [Ma, §I.2]
zρ =
Y
i
imi(ρ) mi(ρ)!
Proposition 4.5. Let ρ, σ, τ be arbitrary partitions. We have
f ρ
στ = zσzτ
zρ
gρ
στ ,
where gρ
στ can be evaluated as follows.
Fix a set X of cardinality |ρ| and a permutation s : X →X whose cycle structure
is given by ρ. Then gρ
στ equals the number of quadruples (X1, s1, X2, s2) such that:
(i) X1 ⊆X,
X2 ⊆X,
X1 ∪X2 = X.
(ii) |X1| = |σ| and s1 : X1 →X1 is a permutation of cycle structure σ.
(iii) Likewise, |X2| = |τ| and s2 : X2 →X2 is a permutation of cycle structure
τ.
(iv) Denote by ¯s1 : X →X and ¯s2 : X :→X the natural extensions of s1,2 from
X1,2 to the whole X. I.e., ¯s1,2 is trivial on X \ X1,2. Then the condition is that
¯s1¯s2 = s.
Proof. See [IK, Proposition 6.2 and Theorem 9.1].
□
20
