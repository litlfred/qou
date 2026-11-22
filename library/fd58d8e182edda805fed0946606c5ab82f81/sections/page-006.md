---
doc_id: fd58d8e182edda805fed0946606c5ab82f81
doc_title: "GRÖBNER-SHIRSHOV BASES FOR TEMPERLEY-LIEB ALGEBRAS"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: fd58d8e182edda805fed0946606c5ab82f81.pdf
source_sha256: 292cb048e7097935
toc_source: undetermined
doc_brief: "GRÖBNER-SHIRSHOV BASES FOR TEMPERLEY-LIEB ALGEBRAS — For Temperley-Lieb algebras of type B, we construct their Gröbner-Shirshov bases and the corresponding standard monomials, which give another"
---
Theorem 4.2. The algebra T (Bn) has a Gröbner-Shirshov basis bRT (Bn) with respect to our
monomial order <:
E2
i −δEi
for 0 ≤i ≤n −1,
EiEj −EjEi
for i > j + 1,
bRT (Bn) :
Ei,jEi −Ei−2,jEi
for i > j > 0,
EjEi,j −EjEi,j+2
for i > j > 0.
EiEjEiEj −2EiEj
for {i, j} = {0, 1},
Ei,0E1,jEi −Ei−2,0E1,jEi
for i > j + 1 ≥1.
The cardinality of the set MT (Bn), i.e. the set of bRT (Bn)-standard monomials, is
dim T (Bn) = (n + 2)Cn −1.
Proof. First, we consider a mapping
ϕ : M0+
T (Bn) \ {E0} →M0−
T (Bn)
deﬁned by ϕ(E0Ei1,j1Ei2,j2 · · · Eip,jp) = E′
i1,j1Ei2,j2 · · · Eip,jp. Then this map is a bijection. In
order to compute |M0
T (Bn)|, it is enough to count the the number of elements in M0+
T (Bn). For
this, we consider the following procedure.
In the lattice plane, we plot the sequence of points (i1, j1), (i2, j2), . . . , (ip, jp) corresponding
to the monomial E0Ei1,j1Ei2,j2 · · · Eip,jp in (4.2). Set ℓ> 0 to be the largest i such that (i, 0)
belongs to the sequence of plotted points. Then the number of sequences of plotted points
between (ℓ, 0) and (n, n) is the number of paths from (ℓ+ 1, 0) and (n, n) .
Counting the number of these paths, we have
(2n −ℓ−1
n
)
−
(2n −ℓ−1
n + 1
)
= ℓ+ 2
n + 1
(2n −ℓ−1
n
)
.
Thus the number of monomials of the form E0Ei1,0 · · · Eip,jp (4.2) is
n−1
∑
ℓ=1
ℓ+ 2
n + 1
(2n −ℓ−1
n
)
2ℓ−1,
which is the same quantity as 1
2
(∑n−2
k=0 C(n, k)|PB(n, k)| + 1
)
=
n−1
2 Cn, as we have men-
tioned in (2.3) as well as in [7, Corollary 2.14].
Therefore we have
|M0+
T (Bn)| = Cn + n−1
2 Cn = n+1
2 Cn.
Then, the number of bRT (Bn)-standard monomials becomes
|MT (An−1)| + 1 + 2|M0+
T (Bn) \ {E0}| = Cn + 1 + 2
( n+1
2 Cn −1
)
,
which gives exactly the number equal to
dim T (Bn) = (n + 2)Cn −1
as mentioned in [17, §5] and [6, §7]. Theorem 2.6 yields that bRT (Bn) is a Gröbner-Shirshov
basis for T (Bn).
Example 4.3. (1) We enumerate the bRT (B3)-standard monomials containing E0:
E0, E0E1,0, E1,0, E0E1, E′
1, E0E2,0, E2,0, E0E2,1, E′
2,1, E0E2, E′
2,
E0E1,0E2,0, E1,0E2,0, E0E1,0E2,1, E1,0E2,1, E0E1,0E2, E1,0E2, E0E1E2, E′
1E2.
(2) The product of two bRT (B3)-standard monomials is a scalar multiple of a standard mono-
mial. For instance, we multiply E0E1,0E2,0 by E2 from the left:
E2(E0E1,0E2,0) = E0E2,0E2,0 = E0E0E2E1,0 = δE0E2,0.
