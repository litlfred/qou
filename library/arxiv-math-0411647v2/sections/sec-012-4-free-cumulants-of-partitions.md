---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-012-4-free-cumulants-of-partitions
section_title: "Free cumulants of partitions"
section_number: 4
pages: 26-27
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
4.1. Free cumulants. Let us ﬁx some ﬁnite ordered set X, a linear space
V and a map M : NC(X) →V called the moment map. Usually, the space
V carries some kind of multiplicative structure and there exists a sequence
M1, M2, . . ., called moment sequence, such that for every non–crossing
partition ρ = {ρ1, . . ., ρr} the moment map is given by a multiplicative
extension
(4.1)
Mρ =
Y
1≤s≤r
M|ρs|.
For every integer n ≥1 the Speicher’s free cumulant Rn [Spe94, Spe97,
Spe98] is deﬁned by
(4.2)
Rn =
X
ρ∈NC(1,2,...,n)
Moebρcomp Mρ,
where the sum runs over all non–crossing partitions of the set {1, 2, . . ., n}
and Moeb is the M¨obius function on the lattice of non–crossing partitions
given explicitly by
Moebσ =
Y
1≤s≤r
(−1)|σs|−1c|σs|−1
for σ = {σ1, . . ., σr} and where ck =
(2k)!
(k+1)!k! denotes the Catalan number.
We are going to use in this article the following deﬁning property of the
M¨obius function [Spe94].
Lemma 4.1. For every ρ ∈NC(1, 2, . . ., n)
X
π∈NC(1,...,n)
π≤ρ
Moebπ =

1
if ρ is trivial,
0
otherwise.
One can show [Spe94] that if (4.1) holds then the moments can be com-
puted from the corresponding cumulants by the following simple formula
(4.3)
Mn =
X
ρ∈NC(1,...,n)
Rρ,
where similarly as in (4.1) for every non–crossing partition ρ = {ρ1, . . ., ρr}
we set
Rρ =
Y
1≤s≤r
R|ρs|.
In a typical application the moments Mn are real numbers given by
Z ∞
Mn =
−∞
