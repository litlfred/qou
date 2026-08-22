---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-023-24-the-logarithmic-limit-set-recall-the-spaces-g
section_title: "The logarithmic limit set. Recall the spaces Ghyp,N (T,b ) and NXhyp(M ), where"
section_number: 2.4
pages: 18-20
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
N ≥ 3 is odd (see Section 2.2.2); we saw that when M =S3 \ 41 these spaces are respectively
the solution set of the equations (31), and (up to birational isomorphism) the plane curve
whose points are pairs (κw(µK ),κ w(λK )) as in (33). Here we introduce a “limit” of the tower
of spaces {Ghyp,N (T,b )}N , that will be used in Section 4.1. It is related in a natural wa y (via
holonomy maps) to a tropical curve associated to the tower of curves {NXhyp(M )}N , and to
the PSL (2, C) A-polynomial of M (see Remark 2.11).
We use the notations of the previous section. As we are going t o let N vary and consider
corresponding sequences of points in the spaces Ghyp,N (T,b ), we reintroduce the dependence
in N in the notations; thus the points of Ghyp,N (T,b ) are the tuples ( u0,N, u1,N, v0,N, v1,N )
satisfying (31). Also for x ∈ { u, v} and k ∈ { 0, 1, 2}, setting uk,N := uN
k,N we get tuples
(u0,N,u 1,N,v 0,N,v 1,N ) in Ghyp(T,b ), possibly varying with N . As in (4) we write
(39) lu
k,N := 1
N
(
Log(uk,N ) + 2πia′
k,N
)
, lv
k,N := 1
N
(
Log(vk,N ) + 2πib′
k,N
)
.
Therefore a′
k,N,b ′
k,N ∈ Z/N are N -colors, and xk,N = exp(lx
k,N ). Put
(40) lx
k,∞ := lim
N →∞
lx
k,N ∈ C/2πiZ
assuming the limit exists. In this case, by the relations (33 ) the sequence ( κN )N converges
in H 1(∂ ¯M ; C∗) ∼
= (C∗)2. Then we put
κ∞ := lim
N →∞
κN ∈H 1(∂ ¯M ; C∗).
Consider the embedding
ΘN := Log|ΘN | × A(ΘN ) :Ghyp,N (T,b ) → R4 × (S1)4
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 19
where
Log|ΘN | : Ghyp,N (T,b ) − → R4
(u0,N, u1,N, v0,N, v1,N ) ↦− →
( 1
N Log|u0,N |, 1
N Log|u1,N |, 1
N Log|v0,N |, 1
N Log|v1,N |
)
A(ΘN ) :Ghyp,N (T,b ) − → (S1)4
(u0,N, u1,N, v0,N, v1,N ) ↦− →
(
e2πi
a′
0,N
N ,e 2πi
a′
1,N
N ,e 2πi
b′
0,N
N ,e 2πi
b′
1,N
N
)
.
The maps Log |ΘN | factor to maps deﬁned on Ghyp(T,b ), for which we keep the same notation.
The subspace R4 × (S1)4 ⊂ R4 × R4 has the metric d induced from the Euclidean distance,
and the set of its subsets inherits the corresponding Hausdo rﬀ (pseudo-)distance: d(X,Y ) =
max(supx∈X (d(x,Y )), supy∈Y (d(X,y ))) for all X,Y ⊂ R4 × (S1)4.
Lemma 2.10. The sequence (ΘN (Ghyp,N (T,b )))N converges to C(T,b )×A(T,b ) ⊂ R4 ×(S1)4
as N → +∞, N odd, where A(T,b ) := {(z1,z 2,z 3,z 4) ∈ (S1)4 | z2
1z2z2
3z4 = 1}, and C(T,b ) is
the union of the following four half lines in R4 (parametrized in R2 × R2):
L1 = {t((−1, 0), 2(0, 1)),t ≥ 0} , L 2 = {t(2(0, 1), (−1, 0)),t ≥ 0}
L3 = {t((−1, 0), 2(1, −1)),t ≥ 0} , L 4 = {t(2(1, −1), (−1, 0)),t ≥ 0}.
Proof. The convergence of Log |ΘN |(Ghyp(T,b )) to C(T,b ) is the only non obvious fact; it
follows from the Neumann-Zagier combinatorics [49], and is shown in Example 3.1 of [62]
(changing notations z1, z2 to u−1
0 , v−1
0 , respectively). The vectors ( −1, 0), (0, 1), (1, −1)
used to deﬁne the half-lines L1,...,L 4 are the directions where (Log |u0|, Log|u1|) (resp.
(Log|v0|, Log|v1|)) tends as u0 (resp. v0) tends to 0, 1 or ∞. The images of the bounded
subsets of Ghyp(T,b ) by the maps Log |ΘN | converge to {0} ⊂ R4 as N → +∞, hence the
limit of Log |ΘN |(Ghyp(T,b )) is the cone over its asymptotic directions, and the task is to
compute these directions.
Consider now the sets A(ΘN )(Ghyp,N (T,b )). By rewriting the system (35) in terms of the
parameters lu
k,N , lv
k,N in (39) and assuming the limits (40) exist, as N → +∞ we get
(41)











lu
0,∞ + lu
1,∞ + lu
2,∞ = 0 mod(2 πi)
lv
0,∞ + lv
1,∞ + lv
2,∞ = 0 mod(2 πi)
lu
1,∞ + 2lu
2,∞ − 2lv
0,∞ − lv
1,∞ = 0 mod(2 πi)
2lu
0,∞ − 2lu
2,∞ = Log( κ∞(λK)) mod(2 πi)
lu
2,∞ + lv
2,∞ = Log( κ∞(µK)) mod(2 πi).
Note that the following limits take values in R/2πZ:
α∞
k := I(lu
k,∞) = limN →∞
2πa′
k,N
N , β∞
k := I(lv
k,∞) = limN →∞
2πb′
k,N
N .
In particular the classical shape parameters uk,N and vk,N do not contribute to these limits.
Taking imaginary parts in the system (41), we ﬁnd that α∞
k ,β ∞
k ∈ R/2πZ, for k ∈ {0, 1, 2},
satisfy the relations:
(42)











α∞
0 +α∞
1 +α∞
2 = 0 mod(2 π)
β∞
0 +β∞
1 +β∞
2 = 0 mod(2 π)
α∞
1 + 2α∞
2 − 2β∞
0 −β∞
1 = 0 mod(2 π)
2α∞
0 − 2α∞
2 = arg( κ∞(λK )) mod(2 π)
α∞
2 +β∞
2 = arg( κ∞(µK )) mod(2 π).
The ﬁrst three relations are the only constraints on α∞
k ,β ∞
k , where k ∈ { 0, 1, 2} (in par-
ticular there is no contribution of the argument of the class ical dilation factors arg( δwN )
