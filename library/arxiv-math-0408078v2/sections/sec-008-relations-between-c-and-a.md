---
doc_id: arxiv-math-0408078v2
doc_title: "A basis for the full Homfly skein of the annulus"
section_id: sec-008-relations-between-c-and-a
section_title: "Relations between C and A"
section_number: null
pages: 10-11
source_pdf: 0408078v2.pdf
source_sha256: b632eb5e9b7a1753
toc_source: outline
doc_brief: "A basis for the full Homfly skein of the annulus — A basis, denoted {Qλ,µ}, for the full Homﬂy skein of the annulus C was introduced in [18], where λ and µ are partitions of integers n and p into k"
---
Relations between C and A
Two algebra homomorphisms l, r : C →A can be induced by placing an ele-
ment of C respectively under or over the simple arc e joining the distinguished
boundary points of the annulus. Thus
l(X) =
X
and
r(X) =
X
.
The eﬀects of the mirror map and the involution ∗are readily seen to give
l(X)
=
r(X)
(4)
(l(X))∗
=
r(X∗).
(5)
Then l(hn) = r(hn), where hn ∈C is the closure of the idempotent in Hn.
Deﬁne a closure map ⋄: A →C on diagrams by joining the distinguished
boundary points with a simple arc lying above the annulus. This map inter-
acts with l and r to give
⋄(r(X))
=
¯ϕ(X),
⋄(l(X))
=
δX,
⋄(Y l(X))
=
⋄(Y )X,
for any X ∈C, Y ∈A.
We shall construct eigenvectors of ϕ and ¯ϕ as determinants of matrices
with entries hn, h∗
n in C. When M is any such a matrix, with X = det M,
we have ¯ϕ(X) = ⋄(r(det M)) = ⋄(det r(M)), where r(M) is the matrix with
entries in A given by applying the algebra homomorphism r to all entries
in M. Our main calculation in the next section involves determinants of
matrices such as r(M) with entries in A. In advance of this we introduce
some relations in A which allow us to perform certain column operations on
the matrices.
Deﬁne elements yn ∈A, ﬁxed under the mirror map, by
yn := [n + 1] ×
hn+1
where hn+1 here is the idempotent in Hn+1.
10
Lemma 1.5 We have the relation
yn = s−1ayn−1 + l(hn).
(6)
Proof:
Apply Corollary 1.3 to write [n + 1]hn+1 = s−nhngn+1. Use the skein
relation (1) to write gn+1, and hence yn, as the sum of two parts. One of
these gives l(hn) at once and the other gives s−1ayn−1 on moving the box gn
in (1) round the annulus to combine with hn from above.
✷
Apply the mirror map to (6), noting that ¯s = s−1, to get
yn = sayn−1 + r(hn).
(7)
Since a∗= a−1 we can apply ∗to equations (6) and (7) to obtain
y∗
n
=
s−1a−1y∗
n−1 + r(h∗
n)
(8)
y∗
n
=
sa−1y∗
n−1 + l(h∗
n).
(9)
We rewrite equations (6) and (9) as
yn
=
s−1ayn−1 + ln,
(10)
y∗
n−1
=
s−1ay∗
n + Ln−1,
(11)
with ln = l(hn) and Ln−1 = −s−1al(h∗
n), for ease of use in our later matrix
work.
Similarly we rewrite (7) and (8) as
yn
=
sayn−1 + rn
(12)
y∗
n−1
=
say∗
n + Rn−1.
(13)
with rn = r(hn) and Rn−1 = −sar(h∗
n).
From equations (10) and (12) we get
(s −s−1)yn
=
sln −s−1rn,
(14)
and from (11) and (13) we get
(s −s−1)y∗
n−1
=
sLn−1 −s−1Rn−1.
(15)
