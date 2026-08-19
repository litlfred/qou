---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-011-45-the-index-of-an-ideal-triangulation
section_title: "The index of an ideal triangulation"
section_number: 4.5
pages: 19-20
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
ary ∂M consists of r≥ 1 tori T1,...,T r, and let T be an ideal triangulation ofM. Let
ϖ = (ϖ1,...,ϖ r) be a collection of oriented peripheral curves as above. By Theorem 4.3,
proved below, we can order the edges ofT so that the ﬁrstN−r rows of the Neumann-Zagier
matrix (A| B) form aninteger basisfor its integer row space (i.e. theZ-module of all linear
combinations of its rows with integer coeﬃcients). Then we deﬁne
(17) IT(ϖ)(q) =
∑
k∈ZN−r⊂ZN
(−q
1
2 )k·ν+νϖ
N∏
j=1
I∆(−bϖ,j−k·bj,aϖ,j +k·aj).
whereaj andbj for j = 1,...,N denote the columns ofA and B, and
ZN−r =
{
(k1,...,k N)∈ ZN :kj = 0 for j >N−r
}
.
It can be checked that this deﬁnition is independent of the quad choice involved in forming
(A| B); see(25). Itisalsoindependentofthechoiceof N−r edgesusedtoproduceaninteger
basis for the integer row space of the Neumann-Zagier matrix, by Remark 4.6. In the case of
a 1-cusped manifoldM, anyN−1 edges can be used; in other words we could replace the do-
main of summationZN−1 by any of the coordinate hyperplanes
{
(k1,...,k N)∈ ZN :ks = 0
}
with s∈{ 1,...,N }. In general, we choose a setB of N−r basic edgeswhose correspond-
ing rows we sum over, for example by using Theorem 4.3. Equivalently, we choose the
complementary set X of excluded edges.
Theorem 4.7 below shows that the index is unchanged by an isotopy ofϖ so only depends
on the homology class
[ϖ] =
[∑
ϖi
]
∈H1(∂M ; Z) =
N⨁
i=1
H1(Ti; Z).
So the index gives a well-deﬁned function
IT :H1(∂M ; Z)−→ Z((q1/2)) where IT([ϖ]) =IT(ϖ).
20 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
If M is a 1-cusped manifoldM, andµ and λ in H1(∂M ; Z) are a ﬁxed oriented meridian
and longitude on∂M (a canonical choice exists whenM is the complement of an oriented
knot inS3). Then we can write
(18) [ϖ] =−mλ +eµ
for integerse,m. The naming of the integerse and m (electric and magnetic charge) and
the above choice of signs was chosen to make our index compatible with the deﬁnition of
[DGGa] and [Garb].
