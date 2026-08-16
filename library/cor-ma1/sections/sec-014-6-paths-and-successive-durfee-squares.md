---
doc_id: cor-ma1
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-014-6-paths-and-successive-durfee-squares
section_title: "Paths and successive Durfee squares"
section_number: 6
pages: 18-19
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
We prove in this section that
(6.1) E k,i(a, q) =
∑
n1≥...≥nk−1≥0
q(
n1+1
2 )+n2
2+···+n2
k−1+ni+···+nk−1 (−1/a)n1an1
(q)n1−n2···(q)nk−2−nk−1(q)nk−1
.
This gives the case Ek,i(n, j) = Dk,i(n, j) of Theorem 1.4 as the right hand side of Equation (6.1) is the
generating function for the overpartitions counted by Dk,i(n, j) (see Equation (2.1)). We give an analytical
and a combinatorial proof.
6.1. An analytical proof. We use the Bailey lattice structure from [1] to transform (6. 1) into (1.1). Recall
that a pair of sequences ( αn, βn) form a Bailey pair with respect to a if for all n≥ 0 we have
βn =
n∑
r=0
αr
(q)n−r(aq)n+r
.
We need the following lemma which is a special case of (3.8) in [1].:
Lemma 6.1. If (αn, βn) is a Bailey pair with respect to q, then for all 0≤ i≤ k we have
1
(q,−aq)∞
×
∑
n1≥···≥nk≥0
q(
n1+1
2 )+n2
2+···n2
k+ni+1+···nk (−1/a)n1an1
(q)n1−n2···(q)nk−1−nk
βnk
= α0
(q)2
∞
+ 1
(q)2
∞
∑
n≥1
(−1/a)nanq(n2−n)(i−1/2)+in(1− q)
(−aq)n
×
(
q(n2+n)(k−i)
(1− q2n+1) αn− q((n−1)2+(n−1))(k−i)+2n−1
(1− q2n−1) αn−1
)
(6.2)
Proof. We set a = q, ρ1 =−1/a, and then let n as well as all remaining ρi and σi tend to∞ in (3.8) of [1]
to obtain (6.2). □
Proof of (6.1). We use the Bailey pair with respect to q [37, p.468, (B3)],
βn = 1
(q)∞
and αn = (−1)nqn(3n+1)/2(1− q2n+1)
(1− q) .
