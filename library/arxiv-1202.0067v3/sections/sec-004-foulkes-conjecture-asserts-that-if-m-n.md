---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN\u2013NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON"
section_id: sec-004-foulkes-conjecture-asserts-that-if-m-n
section_title: "Foulkes\u2019 Conjecture asserts that if m \u2264 n"
section_number: 1
pages: 18-19
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON — 8 sections: Introduction; Deflation by averaging; Skew characters"
---
Equivalently, φ(m ) = IndSSmn
m oSn
then
D
E D m
E
n
φ(m ) , χλ ≥ φ(n ) , χλ
for all partitions λ of mn. Equivalent formulations of Foulkes’ Conjecture
exist in the language of general linear groups, symmetric polynomials, and
geometric invariant theory. Despite having been attacked from all these
directions (and more), it has only been proved when m ≤ 4 (see [2] and [13]),
asymptotically when n is very large compared to m (see [1, page 352]) and, in
a computational result of Müller and Neunhöffer [14], when m + n ≤ 17. For
n
further background, and some recent results on the constituents of φ(m ) ,
we refer the reader to [16] and [6].
In this section we use character deflations to prove a new recursive formula for the character multiplicities in Foulkes’ Conjecture. Firstly, using
Frobenius reciprocity, then the inflation-deflation reciprocity relation
D
E
(11)
hDef Sn ψ, χi = ψ, Inf SSnm oSn χ ,
where ψ is a character of Sm o Sn and χ is a character of Sn , we observe that
D
E D
E
n
φ(m ) , χλ = DefresSn χλ , 1Sn .
Proposition 5.1. Let m, n ∈ N. If λ is a partition of mn then
D

φ

(mn )

λ

,χ

E

n

D
E
1 XX
n−`
=
ε` (λ/µ) φ(m ) , χµ
n
µ
`=1

where the second sum is over all partitions µ of `m such that there exists an
m-border strip tableau of shape λ/µ and type (`).


CHARACTER DEFLATIONS

19

Proof. We have seen that
D
E D
E
1 X
n
φ(m ) , χλ = DefresSn χλ , 1Sn =
(DefresSn χλ )(g).
n!
g∈Sn

We may write each g ∈ Sn as a product of an `-cycle containing the letter 1
and some h ∈ Sn−` acting on the remaining letters. The number of possible
such `-cycles is (n − 1)!/(n − `)!, hence
n
D
E
