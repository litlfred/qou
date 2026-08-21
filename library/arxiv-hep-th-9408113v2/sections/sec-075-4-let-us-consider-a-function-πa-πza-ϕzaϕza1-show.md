---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-075-4-let-us-consider-a-function-πa-πza-ϕzaϕza1-show
section_title: "Let us consider a function π(a) := π(z,a ) = ϕ(za)ϕ(za−1). Show that"
section_number: 4
pages: 83-85
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
i) π(z,a ) =
∑
n≥0
(−qz)nHn(a)
(q2;q2)n
, where Hn(a) := Hn(a;q2) is the so-called continuous
q-Hermite polynomial. Prove the recurrence relation for the continuousq-Hermite polyno-
mials:
Hn(a) = AHn−1(a)− (1−q2n−2)Hn−2(a), (4)
84 Anatol N. Kirillov
where A =a +a−1, H0(a) = 1, H1(a) = a +a−1.
It follows from (4), that
Hn(a;q2) = det
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
A 1 ... 0 0
1−q2 A ... 0 0
... ... ...
0 0 ... A 1
0 0 ... 1−q2n−2 A
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
n×n
.
Hint: use the functional equation:
π(qa)
π(q−1a) = 1 +za
1 +za−1. (5)
ii) (Modifyed Yang-Baxter equation). If ab =q2ba, then
π(z′,b )π(zz ′,qba )π(z,a ) = π(z,a )π(zz ′,qab −1)π(z′,b ). (6)
Proof. Let us remark at ﬁrst that ( ab =q2ba)
π(z,a )b(1 +zq −1a−1) = b(1 +zqa)π(z,a ), (7)
π(z,a )b−1(1 +zq −1a) = b−1(1 +zqa −1)π(z,a ).
Indeed, using the functional equation (5), one can ﬁnd
π(z,a )b(1 +aq−1a−1) = bπ(z,q 2a)(1 +zq −1a−1) = b(1 +zqa)π(z,a ).
To go further, let us use the relations (1) and (2). One can che ck
Φ := π(z′,b )π(zz ′,qba ) = ϕ(z′b)ϕ(z′b−1)ϕ(zz ′qba)ϕ(zz ′qb−1a−1)
(2c)
= ϕ(z′b)ϕ(zz ′qba)ϕ(z(z′)2a)ϕ(z′b−1)ϕ(zz ′qb−1a−1)
(1)
= ϕ(z′b(1 +qza))ϕ(z(z′)2a)ϕ(z′b−1(1 +qza −1)).
Consequently (use the relation (7) !),
Φ ·π(z,a ) = π(z,a )ϕ(z′b(1 +zq −1a−1))ϕ(z(z′)2a)ϕ(z′b−1(1 +zq −1a))
=π(z,a )π(zz ′,qab −1)π(z′,b ),
as it was claimed.
5 (Commutation relations for the continuous q-Hermite polynomials).
Show that (ab =q2ba)
i) q[B1(a),B n(b)] = (1−q2n)
{
B1(qab−1)Bn−1(b)−Bn−1(b)B1(qba)
}
,
Dilogarithm identities 85
q[Bn(a),B 1(b)] = (1−q2n)
{
Bn−1(a)B1(qab−1)−B1(qba)Bn−1(a)
}
.
ii) More generally, in the Weyl algebra {a,b|ab =q2ba} there exist the following relations
(m,n = 1, 2, 3,... )
min(n,m)∑
k=0
(−q−1)k
[
n
k
]
q2
[
m
k
]
q2
(q2;q2)kBn−k(b)Bk(qba)Bm−k(a) (8)
=
min(n,m)∑
k=0
(−q−1)k
[
n
k
]
q2
[
m
k
]
q2
(q2;q2)kBm−k(a)Bk(qab−1)Bn−k(b).
Hint: the relations (8) are equivalent to the modifyed Yang- Baxter equation (6).
