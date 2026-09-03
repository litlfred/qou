---
doc_id: arxiv-math-0701051v4
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA"
section_id: sec-010-33-generalized-circular-operators
section_title: "Generalized circular operators"
section_number: 3.3
pages: 11-13
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA — We prove an upper bound for characters of the symmetric groups."
---
functions on R+. We equip it with an expected value φ : D → C given by
φ(f ) =
∫ ∞
0 f (t)dt.
We consider an operator-valued probability space, which by deﬁnition
is some ∗-algebra A such that D ⊆ A and equipped with a conditional
expectation E : A → D . For a given (generalized) Young diagramλ let T ∈
A be a generalized circular operator [VDN92, Spe98] with a covariance
[
k(T, f T ∗)
]
(s) =
∫
t:(t,s)∈λ
f (t) dt,
[
k(T ∗, f T)
]
(s) = −
∫
t:(s,t)∈λ
f (t) dt,(16)
[
k(T, f T)
]
(s) = 0 ,
[
k(T ∗, f T∗)
]
(s) = 0 .
Theorem 10. For any (generalized) Young diagramλ
Rλ
l+1 = φ
[
(T ∗T )l]
.
Proof. It is easy to check that for permutations σ1, σ2 which contribute to
(15) the corresponding bipartite graph is a tree therefore t he calculation of
N λ(σ1, σ2) is particularly simple, namely it is a certain iterated inte gral.
The same iterated integral appears in the nested evaluation of amalgamated
free cumulants therefore N λ(σ1, σ2) = ±φ
[
kσ2(T ∗, T, · · · , T ∗, T )
]
. The
plus/minus sign is due to the minus sign in the covariance (16). It is easy to
check that in fact
(−1)|σ1|N λ(σ1, σ2) = φ
[
kσ2(T ∗, T, · · · , T ∗, T )
]
.
The moment-cumulant formula
E
[
(T ∗T )l]
=
∑
σ∈NC2
kσ(T ∗, T, · · · , T ∗, T )
ﬁnishes the proof since there is a bijective correspondence between non-
crossing pair partitions and the minimal factorizations. □
12 V ALENTIN FÉRAY AND PIOTR ´SNIADY
Due to the analytic machinery of free probability the calcul ation of the
moments of T in a closed form is possible in many cases therefore Theorem
10 gives a practical method of calculating the free cumulant s of the Young
diagrams.
4. T ECHNICAL ESTIMATES
4.1. Estimates for the number of colorings N λ(σ1, σ2). As we already
mentioned in Example 3 to permutations σ1, σ2 we can associate a bipartite
graph C(σ1) ⊔ C(σ2) with an edge between c1 ∈ C(σ1) and c2 ∈ C(σ2) if
c1 ∩ c2 ⁄= ∅.
For a bipartite graph G = C1 ⊔ C2 (not necessarily arising from the
above construction) and a Young diagramλ we deﬁne N λ(G) as the number
of colorings h of the vertices of C1 ⊔ C2 which are compatible with the
Young diagram λ (the deﬁnition of compatibility in this context is a natural
extension of the old one, i.e. we require that if c1 ∈ C1 and c2 ∈ C2 are
connected by an edge then
(
h(c1), h(c2)
)
∈ λ).
We denote byGp,q a full bipartite graph for which|C1| = p and |C2| = q.
Lemma 11. Let G be a ﬁnite bipartite graph with a property that the degree
of any vertex is non-zero. It is possible (not necessarily in a unique way) to
remove some of the edges of G in such a way that the resulting graph ˜G is
a disjoint union of the graphs of the form G1,1, Gk,1, G1,k.
Assume that a Young diagram λ consists of n boxes. Then, for any A ≥
r(λ), c(λ)
(17) N λ(G) ≤ A(number of vertices of G)
( n
A2
) (number of connected components of ˜G)
.
Proof. If the graph G contains an edge which connects two vertices of de-
gree bigger than one we remove it and iterate this procedure; if no such
edge exists then the resulting graph ˜G has the desired property.
Clearly, N λ(G) ≤ N λ( ˜G) therefore it is enough to ﬁnd a suitable up-
per bound for N λ( ˜G). Since both sides of (17) are multiplicative with
respect to the disjoint sum of graphs it is enough to prove (17 ) for ˜G ∈
{G1,1, Gk,1, G1,k}. Now, the lemma follows from:
N λ(Gk,1) =
∑
i
λk
i ≤
∑
i
λiAk−1 = nAk−1
and the analogous inequality for N λ(G1,k). □
ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS 13
Proposition 12. Suppose that r(λ), c(λ) ≤ A ≤ n and σ1, σ2 ∈ Sl and
π = σ1σ2. Then
(18) N λ(σ1, σ2) ≤ A|C(σ1)|+|C(σ2)|
( n
A2
) orbits(σ1,σ2)
≤ Al−|C(π)|n|C(π)|
( 1
A
) o(σ1,σ2)
,
where orbits(σ1, σ2) denotes the number of orbits in the action of ⟨σ1, σ2⟩
on the set {1, . . . , n} and
o(σ1, σ2) = l − |C(σ1)| − |C(σ2)| + orbits(σ1, σ2).
Proof. The ﬁrst inequality is a simple corollary from Lemma 11 sinceA2 ≥
r(λ)c(λ) ≥ n and the number of connected components of ˜G is bounded
from below byorbits(σ1, σ2). The second inequality follows by multiplying
by ( n
A
) |C(π)|−orbits(σ1,σ2)
≥ 1. □
