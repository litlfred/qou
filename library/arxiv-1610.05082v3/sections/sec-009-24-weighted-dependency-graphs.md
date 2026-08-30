---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-009-24-weighted-dependency-graphs
section_title: "Weighted dependency graphs"
section_number: 2.4
pages: 7-8
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
x1 = (0, 1)
x2 = (1, 0)
x3 = (0, −1)
x4 = (−1, 0)
21
𝓁T (A) = 4 𝓁′
T (A) = 6
Figure 1. The two tree lengths on an example
Proposition 2.2. For all A ={x1,...,x n} ﬁnite subset of Zd, we have
𝓁T (A)≤𝓁′
T (A)≤ 2𝓁T (A).
2.4. Weighted dependency graphs. Weighted dependency graphs have been introduced by the
second author in [8]. The following is a simpliﬁed deﬁnition, suﬃcient for the purpose of this paper
(it corresponds to the case Ψ ≡ 1 of the general deﬁnition, given in [8]).
Deﬁnition 2.3. Let{Yα,α ∈ A} be a family of random variables with ﬁnite moments, living in the
same probability space; and let C = (C1,C 2,··· ) be a sequence of positive real numbers.
A weighted graph G is a C-weighted dependency graph for {Yα,α ∈ A} if, for any multiset
B ={α1,...,α r} of elements of A, one has
(2.2)
⏐⏐⏐⏐κ
(
Yα;α∈B
)⏐⏐⏐⏐≤CrM
(
G[B]
)
.
Here G[B] denotes the graph induced by G on the vertex set B.
Weighted dependency graphs are a toolbox to prove central limit theorems. Here is a normality
criterion, which is a slightly modiﬁed version of the main theorem in [8].
Theorem 2.4. Suppose that, for each n,{Yn,i, 1≤ j≤ Nn} is a family of random variables with
ﬁnite moments deﬁned on the same probability space. Let C = (Cr)r≥1 be a ﬁxed sequence that does
not depend on n.
Assume that, for each n, one has a C-weighted dependency graph Gn for{Yn,i, 1≤ j≤ Nn} and
denote ∆n− 1 its maximal weighted degree.
LetXn =∑Nn
i=1Yn,i and v2
n =Var (Xn). Assume that there exists a sequence (an), an integer s≥ 3
and a real number v such that
(1) v2
n
a2n
−−−−→
n→∞
v2,
(2) for all n, a2
n≤C2Nn∆n,
(3)
(Nn
∆n
) 1
s ∆n
an
−−−−→
n→∞
0.
Then in distribution,
Xn− E(Xn)
an
d
−−−−→
n→∞
N (0,v 2).
Proof: The proof is almost identical to the proof of the normality criterion in [8, Section 4.3] replacing
σn byan. Indeed, as noticed in [8, Section 4.3], in the special case Ψ≡ 1 (to which we restrict ourselves
in this article), the quantitiesRn andQn deﬁned there can be replaced respectively byNn (the number
of vertices) and ∆n (the maximal weighted degree plus one). □
8 JEHANNE DOUSSE AND VALENTIN F ´ERAY
