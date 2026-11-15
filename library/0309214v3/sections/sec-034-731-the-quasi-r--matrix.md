---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-034-731-the-quasi-r--matrix
section_title: "The quasi-R--matrix"
section_number: 7.3.1
pages: 29-30
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
Fix a reduced word w representing the longest element of W . For each r, 1 ≤
r ≤t, let
Θr :=
X
k∈N
ck f k
r ⊗ek
r,
where
ck = (−1)kv−k(k−1)/2
γr
(vγr −v−1
γr )k
[k]γr!
.
Geometry & Topology, Volume 9 (2005)
1282
Stavros Garoufalidis and Thang T Q Lˆe
Here vγ = v(γ|γ)/2, and
[k]γ! =
k
Y
i=1
vi
γ −v−i
γ
vγ −v−1
γ
.
The main thing to observe is that ck is q–holonomic with respect to k. Note
that although Θr is an inﬁnite sum, for every weight λ ∈X , the action of Θr
on M(λ) ⊗M(λ) is well-deﬁned. This is because the action of er is locally
nilpotent, ie, for every x ∈M(λ), there is k such that ek
r · x = 0.
The quasi-R–matrix is:
Θ := ΘtΘt−1 . . . Θ1.
We will consider Θ as an operator from M(λ) ⊗M(λ) to itself. There is a
natural basis for M(λ) ⊗M(λ) coming from the PBW basis of M(λ).
Proposition 7.5 The matrix of Θ acting on M(λ) in a PBW basis is q–
holonomic with respect to all the coordinates of the entry and λ.
Proof It’s enough to prove the statement for each Θr.
The result for Θr
follows from the fact that the actions of ek
r, f k
r on M(λ), as well as ck, are
q–holonomic in k and so are all the coordinates of the matrix entries, by Propo-
sition 7.4 .
7.3.2
