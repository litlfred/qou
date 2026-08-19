---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-010-45-the-index-of-an-ideal-triangulation
section_title: "The index of an ideal triangulation"
section_number: 4.5
pages: 19-20
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
ary ∂M consists of r≥ 1 tori T1,...,T r, and let T be an ideal triangulation of M . Let
ϖ = (ϖ1,...,ϖ r) be a collection of oriented peripheral curves as above. By Theorem 4.3,
proved below, we can order the edges of T so that the 
rst N−r rows of the Neumann-Zagier
matrix (A| B) form an integer basis for its integer row space (i.e. the Z-module of all linear
combinations of its rows with integer coe
cients). Then we de
ne
(17) IT(ϖ)(q) =
∑
k∈ZN−r⊂ZN
(−q
1
2 )k·ν+νϖ
N∏
j=1
I∆(−bϖ,j−k·bj,aϖ,j +k·aj).
where aj and bj for j = 1,...,N denote the columns of A and B, and
ZN−r =
{
(k1,...,k N)∈ ZN :kj = 0 for j >N−r
}
.
It can be checked that this de
nition is independent of the quad choice involved in forming
(A| B); see (25). It is also independent of the choice of N−r edges used to produce an integer
basis for the integer row space of the Neumann-Zagier matrix, by Remark 4.6. In the case of
a 1-cusped manifold M , any N−1 edges can be used; in other words we could replace the do-
main of summation ZN−1 by any of the coordinate hyperplanes
{
(k1,...,k N)∈ ZN :ks = 0
}
with s∈{ 1,...,N }. In general, we choose a set B of N−r basic edges whose correspond-
ing rows we sum over, for example by using Theorem 4.3. Equivalently, we choose the
complementary set X of excluded edges .
20 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
Theorem 4.7 below shows that the index is unchanged by an isotopy of ϖ so only depends
on the homology class
[ϖ] =
[∑
ϖi
]
∈H1(∂M ; Z) =
N⨁
i=1
H1(Ti; Z).
So the index gives a well-de
ned function
IT :H1(∂M ; Z)−→ Z((q1/2)) where IT([ϖ]) =IT(ϖ).
If M is a 1-cusped manifold M , and µ and λ in H1(∂M ; Z) are a 
xed oriented meridian
and longitude on ∂M (a canonical choice exists when M is the complement of an oriented
knot in S3). Then we can write
(18) [ϖ] =−mλ +eµ
for integers e,m . The naming of the integers e and m (electric and magnetic charge) and
the above choice of signs was chosen to make our index compatible with the de
nition of
[DGG13] and [Garb].
