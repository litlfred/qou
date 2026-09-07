---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces Aidan Roy ∗"
section_id: sec-006-other-bounds
section_title: "Other bounds"
section_number: null
pages: 18-19
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
doc_brief: "Bounds for codes and designs in complex subspaces Aidan Roy ∗ — We introduce the concepts of complex Grassmannian codes and designs."
---
Certain cases of equality in Corollaries 6.5 and 6.6 also ach ieve equality for
bounds on the size of the largest angle in a set of subspaces. F or real Grass-
mannians, Conway, Hardin and Sloane [8] call these bounds th e simplex and
orthoplex bounds. Here we give their complex analogues.
Recall that if Pa be the n × n projection matrix for a ∈ G m,n , then Pa is
Hermitian with trace m, so P ′
a = Pa − mI/n lies in a real space of dimension
n2 − 1. Moreover ||P ′
a||2 := tr( P ′
aP ′
a) = m(1 − m/n ), so P ′
a is embedded onto
a sphere of radius
√
m(1 − m/n ) in Rn2−1. Further recall that the chordal
distance on Gm,n is deﬁned by
dc(a, b )2 = m − tr(PaPb)
= 1
2 ||Pa − Pb||2 = 1
2 ||P ′
a − P ′
b||2.
With this distance, the Grassmannians are isometrically em bedded into Rn2−1.
The “Rankin bounds” given in Theorem 7.1 below (see [4, Theor ems 6.1.1 &
6.1.2]) are bounds on the minimum distance between points on a real sphere
as a function of the number of points and the dimension of the s pace. An
equatorial simplex refers to a set of N points on the unit sphere that form a
simplex in a hyperplane of dimension N − 1.
Theorem 7.1. Given N points on a sphere of radius r in RD, the minimum
distance d between any two points satisﬁes
d ≤ r
√
2N
N − 1 .
Equality requires N ≤ D + 1 and occurs if and only if the points form a regular
equatorial simplex. For N > D + 1, the minimum distance satisﬁes
d ≤ r
√
2,
and equality requires N ≤ 2D. When N = 2 D, equality occurs if and only if
the points are the vertices of a regular orthoplex.
Conway, Hardin and Sloane [8] apply these bounds to get the si mplex and
orthoplex bounds for real Grassmannians: we can do the same f or the complex
Grassmannians.
18
Corollary 7.2. Given a set S points in Gm,n , the largest inner product value
α = ⟨a, b ⟩ between any two points satisﬁes
α ≥ m m|S| − n
n|S| − n . (7.1)
Equality requires |S| ≤ n2 and occurs if and only if the points form a regular
equatorial simplex in Rn2−1. For |S| > n2, the largest inner product β satisﬁes
β ≥ m2
n , (7.2)
and equality requires |S| ≤ 2(n2 − 1). Equality occurs if the points are the
2(n2 − 1) vertices of a regular orthoplex in Rn2−1.
If S is an {α }-code, then solving inequality (7.1) for |S| recovers the relative
bound in Corollary 6.5. Moreover, if |S| = n2 (equality in the absolute bound
of Corollary 6.2), then
α = m(mn − 1)
n2 − 1 .
On the other hand, if S is a {0, m 2/n }-code, and m = n/ 2, then the relative
bound in Corollary 6.6 implies that
|S| ≤ 2(n2 − 1),
which corresponds to equality in the orthoplex bound (7.2).
