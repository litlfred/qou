---
doc_id: fd58d8e182edda805fed0946606c5ab82f81
doc_title: "GRÖBNER-SHIRSHOV BASES FOR TEMPERLEY-LIEB ALGEBRAS"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: fd58d8e182edda805fed0946606c5ab82f81.pdf
source_sha256: 292cb048e7097935
toc_source: undetermined
doc_brief: "GRÖBNER-SHIRSHOV BASES FOR TEMPERLEY-LIEB ALGEBRAS — For Temperley-Lieb algebras of type B, we construct their Gröbner-Shirshov bases and the corresponding standard monomials, which give another"
---
where δ ∈C is a parameter. .
Fix our monomial order < to be the degree-lexicographic order with
E0 < E1 < · · · < En−1.
We write Ei,j = EiEi−1 · · · Ej for i ≥j ≥0, and Ei,j = EiEi+1 · · · Ej for i ≤j. By
convention, Ei,i+1 = 1 and Ei+1,i = 1 for i ≥0.
Lemma 4.1. The following relation holds in T (Bn):
Ei,0E1,jEi = Ei−2,0E1,jEi
for i > j + 1 ≥1.
Proof. Since 2 ≤i ≤n −1 and 0 ≤j ≤i −2, we calculate that
Ei,0E1,jEi = (EiEi−1Ei)Ei−2,0E1,j = EiEi−2,0E1,j = Ei−2,0E1,jEi
by the commutative relations and EiEi−1Ei = Ei.
Let bRT (Bn) be the set of deﬁning relations (4.1) combined with (3.1) and the relation in
Lemma 4.1. From this, we deﬁne MT (Bn) by the set of bRT (Bn)-standard monomials. Among
the monomials in MT (Bn), we consider the monomials which are not bRT (An−1)-standard. That
is, we take only bRT (Bn)-standard monomials which are not of the form (3.2). This set is denoted
by M0
T (Bn). Note that each monomial in M 0
T (Bn) contains E0. We decompose the set M 0
T (Bn)
into two parts as follows :
M0
T (Bn) = M0+
T (Bn) ⨿M0−
T (Bn)
where the monomials in M0+
T (Bn) are of the form
E0Ei1,j1Ei2,j2 · · · Eip,jp
(0 ≤p ≤n −1)
(4.2)
with
1 ≤i1 < i2 < · · · < ip ≤n −1,
0 ≤j1 ≤j2 ≤· · · ≤jp ≤n −1,
i1 ≥j1, i2 ≥j2, . . . , ip ≥jp, and
jk > 0 (1 ≤k < p) implies jk < jk+1
(the case of p = 0 is the monomial E0), and the monomials in M0−
T (Bn) are of the form
E′
i1,j1Ei2,j2 · · · Eip,jp
(1 ≤p ≤n −1)
with
E′
i,j = Ei,0E1,j
and the same restriction on i’s and j’s as above. It can be easily checked that M0
T (Bn) is the set
of bRT (Bn)-standard monomials which are not bRT (An−1)-standard.
To each monomial E0Ei1,0Ei2,0 · · · Eik,0Eik+1,jk+1 · · · Eip,jp in M0+
T (Bn) with jk+1 > 0, we can
associate a unique path
(0, 0) →(i1, 0) →(i2, 0) →· · · →(ik, 0) →(ik+1, jk+1) →· · · →(ip, jp) →(n, n).
Here, a path consists of moves to the east or to the north, not above the diagonal in the lattice
plane. The move from (i, j) to (i′, j′) (i < i′ and j < j′) is a concatenation of eastern moves
followed by northern moves. As an example, the monomial E0E1,0E2,1 ∈M0+
T (B3) corresponds
to
(0, 0) →(1, 0) →(2, 1) →(3, 3).
Counting the number of elements in M0
T (Bn), we obtain the following theorem.
