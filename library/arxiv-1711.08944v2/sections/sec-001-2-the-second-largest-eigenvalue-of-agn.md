---
doc_id: arxiv-1711.08944v2
doc_title: "The second largest eigenvalues of some Cayley graphs on alternating groups ∗"
section_id: sec-001-2-the-second-largest-eigenvalue-of-agn
section_title: "The second largest eigenvalue of AGn"
section_number: 2
pages: 3-12
source_pdf: 1711.08944v2.pdf
source_sha256: ad7a020e7e92b788
doc_brief: "The second largest eigenvalues of some Cayley graphs on alternating groups ∗ — Let An denote the alternating group of degree n with n ≥ 3."
---
In this section, we focus on determining the second largest eigenva lue of AGn. In
order to obtain enough information about the eigenvalues of AGn, we need a well
known result on equitable partition.
Let G be a graph of order n, and let Π : V (G) = V1 ∪ V2 ∪ · · · ∪ Vk be a
vertex partition of G. The characteristic matrix χΠ of Π is the n × k matrix whose
columns are the character vectors of V1, . . . , Vk. The partition Π is called an equitable
partition of G if, for any v ∈ Vi, |N(v) ∩ Vj| = bij is a constant only dependent on
i, j (1 ≤ i, j ≤ k). The matrix BΠ = ( bij)k×k is called the divisor matrix of G with
respect to Π.
Lemma 2.1 ( [
13]). Let G be a graph with adjacency matrix A(G), and let Π :
V (G) = V1 ∪ V2 ∪ · · · ∪ Vk be an equitable partition of G with divisor matrix BΠ .
Then each eigenvalue of BΠ is also an eigenvalue of A(G). Furthermore, A(G) has
the following two kinds of eigenvectors:
(i) the eigenvectors in the column space of χΠ , and the corresponding eigenvalues
coincide with the eigenvalues of BΠ ;
(ii) the eigenvectors orthogonal to the columns of χΠ , i.e., those eigenvectors that
sum to zero on each block Vi for 1 ≤ i ≤ k.
Recall that AGn = Cay( An, T1), where T1 = {(1, 2, i), (1, i, 2) | 3 ≤ i ≤ n}.
Clearly, AGn is (2 n − 4)-regular. If n = 3, then AGn = K3, which has −1 as its
second largest eigenvalue. Now suppose n ≥ 4. For each ﬁxed i (1 ≤ i ≤ n), we
deﬁne
X(i) = {τ ∈ An | τn = i},
Y (i) = {τ ∈ An | τ1 = i},
Z(i) = {τ ∈ An | τ2 = i},
W (i) = {τ ∈ An | τ1 ⁄= i, τ2 ⁄= i, τn ⁄= i}.
(1)
Now we verify that Π : An = X(i)∪Y (i)∪Z(i)∪W (i) is exactly an equitable partition
of AGn. For each τ ∈ X(i), we have N(τ ) ∩ X(i) = {(1, 2, k)τ, (1, k, 2)τ | 3 ≤ k ≤
n − 1}, N(τ ) ∩ Y (i) = {(1, n, 2)τ }, N(τ ) ∩ Z(i) = {(1, 2, n)τ } and N(τ ) ∩ W (i) = ∅.
4
This implies that each τ ∈ X(i) has exactly 2 n − 6 neighbors in X(i), one neighbor
in Y (i), one neighbor in Z(i) and no neighbors in W (i). Similarly, for each τ ∈ Y (i),
we have N(τ ) ∩ X(i) = {(1, 2, n)τ }, N(τ ) ∩ Y (i) = ∅, N(τ ) ∩ Z(i) = {(1, k, 2)τ |
3 ≤ k ≤ n} and N(τ ) ∩ W (i) = {(1, 2, k)τ | 3 ≤ k ≤ n − 1}, and for each τ ∈ Z(i),
we have N(τ ) ∩ X(i) = {(1, n, 2)τ }, N(τ ) ∩ Y (i) = {(1, 2, k)τ | 3 ≤ k ≤ n},
N(τ ) ∩ Z(i) = ∅ and N(τ ) ∩ W (i) = {(1, k, 2)τ | 3 ≤ k ≤ n − 1}. For each
τ ∈ W (i), we know that τℓ = i for some 3 ≤ ℓ ≤ n − 1 because τ1, τ2, τn ⁄= i.
Then N(τ ) ∩ X(i) = ∅, N(τ ) ∩ Y (i) = {(1, ℓ, 2)τ }, N(τ ) ∩ Z(i) = {(1, 2, ℓ)τ } and
N(τ ) ∩ W (i) = {(1, 2, k)τ, (1, k, 2)τ | 3 ≤ k ≤ n, k ⁄= ℓ}. Therefore, the divisor
matrix of AGn with respect to Π is equal to
BΠ =




2n − 6 1 1 0
1 0 n − 2 n − 3
1 n − 2 0 n − 3
0 1 1 2 n − 6



 .
By simple computation, we know that BΠ has eigenvalues 2 n − 4, 2 n − 6, n − 4 and
2 − n. Thus, by Lemma
2.1, we have
Lemma 2.2. Let AGn be the alternating group graph with n ≥ 4. Then AGn has
eigenvalues 2n − 4, 2n − 6, n − 4 and 2 − n. Moreover, if f is an eigenvector of
AGn corresponding to any other eigenvalue, then for each i ∈ {1, 2, . . . , n}, we have
∑
x∈X(i)
f (x) =
∑
y∈Y (i)
f (y) =
∑
z∈Z(i)
f (z) =
∑
w∈W (i)
f (w) = 0 ,
where X(i), Y (i), Z(i) and W (i) are deﬁned in ( 1).
Now we are in a position to prove the main result of this section.
Theorem 2.3. Let AGn be the alternating group graph with n ≥ 4. Then the two
largest eigenvalues of AGn are λ1(AGn) = 2 n − 4 and λ2(AGn) = 2 n − 6.
Proof. Clearly, the largest eigenvalue of AGn is λ1(AGn) = 2 n − 4 because AGn
is (2 n − 4)-regular. We shall prove λ2(AGn) = 2 n − 6 by induction on n. If
n = 4, the result follows since all the distinct eigenvalues of AG4 are 4, 2, 0 and
−2. Now suppose n > 4, and assume that the result holds for n − 1, that is,
λ2(AGn−1) = 2( n − 1) − 6 = 2 n − 8.
Let λ be an eigenvalue of AGn other than 2 n − 4, 2 n − 6, n − 4 and 2 − n. It
suﬃces to show λ < 2n − 6. Take any ﬁxed eigenvector f of AGn corresponding to
λ. We have the following claim.
Claim 1. There exists an i such that
2
∑
x∈X(i)
f (x)2 ≥
∑
y∈Y (i)
f (y)2 +
∑
z∈Z(i)
f (z)2
and ∑
x∈X(i)
f (x)2 > 0.
5
Proof. Notice that the vertex set of AGn can be partitioned in the following ways:
An = X(1) ∪X(2) ∪ · · ·∪X(n) = Y (1) ∪Y (2) ∪ · · ·∪Y (n) = Z(1) ∪Z(2) ∪ · · ·∪Z(n).
Thus we have
n∑
j=1
∑
x∈X(j)
f (x)2 =
n∑
j=1
∑
y∈Y (j)
f (y)2 =
n∑
j=1
∑
z∈Z(j)
f (z)2 > 0,
and hence
n∑
j=1
2
∑
x∈X(j)
f (x)2 =
n∑
j=1

 ∑
y∈Y (j)
f (y)2 +
∑
z∈Z(j)
f (z)2

 > 0.
Therefore, there exists an index i such that
2
∑
x∈X(i)
f (x)2 ≥
∑
y∈Y (i)
f (y)2 +
∑
z∈Z(i)
f (z)2.
Let I be the set of indices i satisfying this inequality. Then we claim that there
exists some i ∈ I satisfying ∑
x∈X(i)
f (x)2 > 0
because f ⁄= 0.
Now ﬁx an i satisfying the inequalities in Claim 1, and consider an arbitrary
vertex x ∈ X(i). As noted above, x has 2 n − 4 neighbors in AGn, in which 2 n − 6
neighbors in X(i), one neighbor in Y (i) and one neighbor in Z(i). Observe that
the induced subgraph of AGn on X(i) is isomorphic to AGn−1 = Cay( An−1, T ′
1),
where T ′
1 = {(1, 2, k), (1, k, 2) | 3 ≤ k ≤ n − 1}. In fact, if i = n then AGn[X(i)] is
obviously isomorphic to AGn−1 since τn = n for each τ ∈ X(n); if i < n , we deﬁne
φ : X(i) − → An−1
τ =
( 1 2 · · · l · · · n − 1 n
τ1 τ2 · · · n · · · τn−1 i
)
↦− →
( 1 2 · · · l · · · n − 1
τ1 τ2 · · · i · · · τn−1
)
It is easy to check that φ is one-to-one and onto. For any two distinct vertices
τ =
(
1 2 · · · l · · · n − 1 n
τ1 τ2 · · · n · · · τn−1 i
)
and τ ′ =
(
1 2 · · · m · · · n − 1 n
τ ′
1 τ ′
2 · · · n · · · τ ′
n−1 i
)
of X(i), we have
τ ′τ −1 =
( 1 2 · · · m · · · n − 1 n
τ ′
1 τ ′
2 · · · n · · · τ ′
n−1 i
) ( τ1 τ2 · · · n · · · τn−1 i
1 2 · · · l · · · n − 1 n
)
=
( 1 2 · · · m · · · n − 1 n
∗ ∗ · · · l · · · ∗ n
)
=
( 1 2 · · · m · · · n − 1
∗ ∗ · · · l · · · ∗
)
=
( 1 2 · · · m · · · n − 1
τ ′
1 τ ′
2 · · · i · · · τ ′
n−1
) ( τ1 τ2 · · · i · · · τn−1
1 2 · · · l · · · n − 1
)
6
= φ(τ ′)φ(τ )−1.
Then {τ, τ ′} ∈ E(G[Xi]) if and only if τ ′τ −1 ∈ T ′
1, which is the case if and only if
φ(τ ′)φ(τ )−1 ∈ T ′
1, which is the case if and only if {φ(τ ), φ(τ ′)} ∈ E(AGn−1). Thus φ
is exactly an isomorphism from G[X(i)] to AGn−1. Also note that the edges between
X(i) and Y (i) (resp. X(i) and Z(i)) form a matching. Let x′ (resp. x′′) be the
unique neighbor of x in Y (i) (resp. Z(i)). By the eigenvalue-eigenvector equation,
we have
λf (x) =
∑
y∈N (x)∩X(i)
f (y) + f (x′) + f (x′′)
and further,
λf (x)2 =
∑
y∈N (x)∩X(i)
f (x)f (y) + f (x)(f (x′) + f (x′′)).
Summing both sides over x ∈ X(i), we obtain
λ
∑
x∈X(i)
f (x)2 =
∑
x∈X(i)
∑
y∈N (x)∩X(i)
f (x)f (y) +
∑
x∈X(i)
f (x)(f (x′) + f (x′′)),
which gives that
λ =
∑
x∈X(i)
∑
y∈N (x)∩X(i) f (x)f (y)∑
x∈X(i) f (x)2 +
∑
x∈X(i) f (x)(f (x′) + f (x′′))∑
x∈X(i) f (x)2 . (2)
Here we use the fact ∑
x∈X(i) f (x)2 > 0 by Claim 1. Now we shall ﬁnd upper bounds
for the two terms in ( 2). Let G1 = AGn[X(i)]. Then G1 ∼= AGn−1 as mentioned
above. Set g = f |X(i). We have g ⊥ 1 since ∑
x∈X(i) f (x) = 0 according to Lemma
2.2, where 1 is the all ones vector, which is also the eigenvector of λ1(G1). Thus
∑
x∈X(i)
∑
y∈N (x)∩X(i) f (x)f (y)∑
x∈X(i) f (x)2 = gT A(G1)g
gT g
≤ max
h⊥1
hT A(G1)h
hT h
= λ2(G1)
= λ2(AGn−1)
= 2 n − 8.
Next consider the second term in ( 2). Recall that the edges between X(i) and Y (i),
and X(i) and Z(i) form two matchings. Thus when x range over the vertices of
X(i), x′ and x′′ will range over the vertices of Y (i) and Z(i), respectively. Then
∑
x∈X(i) f (x)(f (x′) + f (x′′))∑
x∈X(i) f (x)2 ≤
√
(∑
x∈X(i) f (x)2)(∑
x∈X(i)(f (x′) + f (x′′))2)
∑
x∈X(i) f (x)2
=
√ ∑
x∈X(i)(f (x′) + f (x′′))2
∑
x∈X(i) f (x)2
7
≤
√ ∑
x∈X(i) 2(f (x′)2 + f (x′′)2)∑
x∈X(i) f (x)2
=
√
2(∑
y∈Y (i) f (y)2 + ∑
z∈Z(i) f (z)2))∑
x∈X(i) f (x)2
≤
√
2 · 2 ∑
x∈X(i) f (x)2
∑
x∈X(i) f (x)2 ,
= 2 ,
where the ﬁrst inequality follows from the Cauchy–Schwarz inequalit y, the second
use the fact ( a + b)2 ≤ 2(a2 + b2) and the third follows from Claim 1.
Combing the above two bounds with ( 2) yields
λ ≤ 2n − 8 + 2 = 2 n − 6,
which implies that there are no eigenvalues in (2 n − 6, 2n − 4). Therefore, we have
λ2(AGn) = 2 n − 6.
3 The second largest eigenvalues of EAGn and
CAG n
Recall that the complete alternating group graph is deﬁned as CAG n = Cay(An, T3),
where T3 = {(i, j, k), (i, k, j) | 1 ≤ i < j < k ≤ n} is the set of all 3-cycles in Sn. In
this section, we mainly focus on determining the second largest eigen value of CAG n.
The main idea is to ﬁnd some suitable equitable partition so that we can d ecompose
the edge set of CAG n into that of n copies of CAG n−1 and that of the extended
alternating group graph EAGn = Cay( An, T2), where T2 = {(1, i, j), (1, j, i) | 2 ≤
i < j ≤ n} is the set of 3-cycles in Sn moving 1, which ensures that the way of
induction could be used to ﬁnd the second largest eigenvalue of CAG n. For this
reason, we ﬁrst need to consider the same problem for the graph EAGn, and again,
the main method depends on ﬁnding some suitable equitable partition t o decompose
the edge set of EAGn.
For 1 ≤ i, j ≤ n, we deﬁne
Xi(j) = {τ ∈ An | τj = i}. (3)
For any ﬁxed i (resp. j), we see that Xi(1), Xi(2), . . . , Xi(n) (resp. X1(j), X2(j), . . . ,
Xn(j)) partition An. Now we shall verify that Π : An = Xi(1) ∪ Xi(2) ∪ · · ·∪Xi(n) is
an equitable partition of EAGn for each i. For τ ∈ Xi(1), we have N(τ ) ∩ Xi(1) = ∅
since ( στ )1 ⁄= τ1 = i for any σ ∈ T2, and N(τ ) ∩ Xi(j) = {(1, k, j)τ | 2 ≤ k ≤
n, k ⁄= j} for 2 ≤ j ≤ n. Thus each τ ∈ Xi(1) has no neighbors in Xi(1) and
n − 2 neighbors in Xi(j) for each j (2 ≤ j ≤ n). For each ﬁxed j (2 ≤ j ≤ n), let
τ ∈ Xi(j), we have N(τ ) ∩ Xi(1) = {(1, j, k)τ | 2 ≤ k ≤ n, k ⁄= j}, N(τ ) ∩ Xi(j) =
{(1, k, l)τ, (1, l, k)τ | 2 ≤ k < l ≤ n, k, l ⁄= j}, and N(τ ) ∩ Xi(ℓ) = {(1, ℓ, j)τ } for any
ℓ ⁄∈ {1, j}. This implies that τ has n − 2 neighbors in Xi(1), (n − 2)(n − 3) neighbors
8
in Xi(j), and one neighbor in Xi(ℓ) for each ℓ ⁄∈ {1, j}. Thus the partition Π is an
equitable partition of EAGn with divisor matrix
BΠ =







0 n − 2 n − 2 · · · n − 2
n − 2 ( n − 2)(n − 3) 1 · · · 1
n − 2 1 ( n − 2)(n − 3) · · · 1
.
.
. .
.
. .
.
. . . . .
.
.
n − 2 1 1 · · · (n − 2)(n − 3)







Xi(1)
Xi(2)
Xi(3)
.
.
.
Xi(n)
Then the characteristic polynomial of BΠ is equal to
|λIn − BΠ | =
⏐
⏐
⏐
⏐
⏐
⏐
⏐
λ −(n−2) −(n−2) ··· − (n−2)
−(n−2) λ−(n−2)(n−3) −1 ··· − 1
−(n−2) −1 λ−(n−2)(n−3) ··· − 1
.
.
. .
.
. .
.
. ... .
.
.
−(n−2) −1 −1 ··· λ−(n−2)(n−3)
⏐
⏐
⏐
⏐
⏐
⏐
⏐
= ( λ − (n − 1)(n − 2))
⏐
⏐
⏐
⏐
⏐
⏐
⏐
1 −(n−2) −(n−2) ··· − (n−2)
1 λ−(n−2)(n−3) −1 ··· − 1
1 −1 λ−(n−2)(n−3) ··· − 1
.
.
. .
.
. .
.
. ... .
.
.
1 −1 −1 ··· λ−(n−2)(n−3)
⏐
⏐
⏐
⏐
⏐
⏐
⏐
= ( λ − (n − 1)(n − 2))
⏐
⏐
⏐
⏐
⏐
⏐
⏐
1 0 0 ··· 0
1 λ−(n−2)(n−4) n−3 ··· n−3
1 n−3 λ−(n−2)(n−4) ··· n−3
.
.
. .
.
. .
.
. ... .
.
.
1 n−3 n−3 ··· λ−(n−2)(n−4)
⏐
⏐
⏐
⏐
⏐
⏐
⏐
= ( λ − (n − 1)(n − 2))
⏐
⏐
⏐
⏐
⏐
⏐
λ−(n−2)(n−4) n−3 ··· n−3
n−3 λ−(n−2)(n−4) ··· n−3
.
.
. .
.
. ... .
.
.
n−3 n−3 ··· λ−(n−2)(n−4)
⏐
⏐
⏐
⏐
⏐
⏐
= ( λ−(n − 1)(n − 2)) |(λ−(n − 2)(n − 4))In−1+(n − 3)(Jn−1−In−1)|
= ( λ − (n − 1)(n − 2))(λ − (n2 − 5n + 5))n−2(λ + (n − 2)),
where In−1 and Jn−1 denote the identity matrix and all ones matrix of order n − 1,
respectively. By Lemma
2.1, we have
Lemma 3.1. Let EAGn be the extended alternating group graph with n ≥ 3. Then
EAGn has eigenvalues (n − 1)(n − 2), n2 − 5n + 5 (with multiplicity at least n − 2)
and 2 − n. Moreover, if f is an eigenvector of EAGn corresponding to any other
eigenvalue, then for all i, j ∈ {1, 2, . . . , n}, we have
∑
x∈Xi(j)
f (x) = 0 ,
where Xi(j) is deﬁned in ( 3).
Now we give the second largest eigenvalue of EAGn.
Theorem 3.2. Let EAGn be the extended alternating group graph with n ≥ 3.
Then the two largest eigenvalues of EAGn are λ1(EAGn) = ( n − 1)(n − 2) and
λ2(EAGn) = n2 − 5n + 5.
9
Proof. Obviously, λ1(EAGn) = ( n − 1)(n − 2) because EAGn is ( n − 1)(n − 2)-
regular. Now we prove λ2(EAGn) = n2 − 5n + 5 by induction on n. For n = 3, we
have EAG3 = K3, which gives that λ2(EAG3) = −1, and the result follows. Now
suppose n ≥ 4 and assume that the result holds for EAGn−1, i.e., λ2(EAGn−1) =
(n − 1)2 − 5(n − 1) + 5. Let λ be an eigenvalue of EAGn that is not equal to
(n − 1)(n − 2), n2 − 5n + 5 or 2 − n, and let f be any ﬁxed eigenvector corresponding
to λ. Then f must sum to zero on Xi(j) for all 1 ≤ i, j ≤ n. Now we partition
the vertex set of EAGn as An = X1(2) ∪ X2(2) ∪ · · · ∪ Xn(2). As in the proof of
Theorem 2.3, one can easily verify that the induce subgraph of EAGn on Xi(2) is
isomorphic to EAGn−1 for each i (1 ≤ i ≤ n). Let E1 = ∪n
i=1E(EAGn[Xi(2)]) and
E2 = E(EAGn) \ E1. We claim that E2 is exactly the set of edges of the alternating
group graph AGn = Cay( An, T1), where T1 = {(1, 2, k), (1, k, 2) | 3 ≤ k ≤ n}. In
fact, for any γ ∈ Xi(2) and γ′ ∈ Xj(2) ( i ⁄= j), we have {γ, γ ′} ∈ E(EAGn) if and
only if γ′γ−1 ∈ T2 (i.e., γ′γ−1 is a 3-cycle moving 1), which is the case if and only
γ′γ−1 ∈ T1(⊆ T2) because γ′γ−1 must move 2 due to i ⁄= j. This implies that the
edges in E2 come from T1. On the other hand, we see that T1 can only be used to
produce the edges in E2 because each edge in E1 comes from T2 \ T1, i.e., the set of
3-cycles in T2 ﬁxing 2. Then
λ = f T A(EAGn)f
f T f
=
2 ∑
{x,y}∈E(EAGn) f (x)f (y)∑
x∈An f (x)2
=
2 ∑
{x,y}∈E1 f (x)f (y)∑
x∈An f (x)2 +
2 ∑
{x,y}∈E2 f (x)f (y)∑
x∈An f (x)2 .
For the ﬁrst term, we have
2 ∑
{x,y}∈E1 f (x)f (y)∑
x∈An f (x)2 =
∑ n
i=1 2 ∑
{x,y}∈E(EAGn[Xi(2)]) f (x)f (y)
∑ n
i=1
∑
x∈Xi(2) f (x)2
≤ max
1≤i≤n
2 ∑
{x,y}∈E(EAGn[Xi(2)]) f (x)f (y)
∑
x∈Xi(2) f (x)2
≤ λ2(EAGn−1),
where the last inequality follows from the fact ∑
x∈Xi(2) f (x) = 0 for each i according
to Lemma 3.1. For the second term, since f is orthogonal to the all ones vector 1,
we have
2 ∑
{x,y}∈E2 f (x)f (y)∑
x∈An f (x)2 ≤ max
g⊥1
gT A(AGn)g
gT g = λ2(AGn).
Combining above two bounds, we conclude that
λ ≤ λ2(EAGn−1) + λ2(AGn) = ( n − 1)2 − 5(n − 1) + 5 + 2n − 6 = n2 − 5n + 5
by Theorem 2.3. Hence λ2(EAGn) = n2 − 5n + 5, and our result follows.
10
Now we focus on the complete alternating group graph CAG n = Cay( An, T3)
where T3 = {(i, j, k), (i, k, j) | 1 ≤ i < j < k ≤ n}. Obviously, CAG n is a 2
( n
3
)
-
regular graph. As above, we shall verify that Π : An = Xi(1) ∪ Xi(2) ∪ · · · ∪ Xi(n)
is also an equitable partition of CAG n for each ﬁxed i, where Xi(j) is deﬁned in
(3). For each ﬁxed j (1 ≤ j ≤ n), let τ ∈ Xi(j). We have N(τ ) ∩ Xi(j) =
{(k, l, m)τ, (k, m, l)τ | 1 ≤ k < l < m ≤ n, k, l, m ⁄= j}, and N(τ ) ∩ Xi(ℓ) =
{(ℓ, j, k)τ | 1 ≤ k ≤ n, k ⁄= ℓ, j} for each ℓ ⁄= j. This implies that τ has 2
( n−1
3
)
neighbors in Xi(j), and n − 2 neighbors in Xi(ℓ) for each ℓ ⁄= j. Thus Π is an
equitable partition of CAG n with divisor matrix
BΠ =







2
( n−1
3
)
n − 2 n − 2 · · · n − 2
n − 2 2
( n−1
3
)
n − 2 · · · n − 2
n − 2 n − 2 2
( n−1
3
)
· · · n − 2
.
.
. .
.
. .
.
. . . . .
.
.
n − 2 n − 2 n − 2 · · · 2
( n−1
3
)







Xi(1)
Xi(2)
Xi(3)
.
.
.
Xi(n)
.
It is easy to see that BΠ has eigenvalues 2
( n
3
)
and 1
3 n(n − 2)(n − 4), where the ﬁrst
one is of multiplicity 1 having the all ones vector 1 as its eigenvector, and the second
one is of multiplicity n − 1 having each vector orthogonal to 1 as an eigenvector.
Again by Lemma 2.1, we have
Lemma 3.3. Let CAG n be the complete alternating group graph with n ≥ 3. Then
CAG n has eigenvalues 2
( n
3
)
and 1
3 n(n − 2)(n − 4) (with multiplicity at least n − 1).
Moreover, if f is an eigenvector of CAG n corresponding to any other eigenvalue,
then for all i, j ∈ {1, 2, . . . , n}, we have
∑
x∈Xi(j)
f (x) = 0 ,
where Xi(j) is deﬁned in ( 3).
Now we prove the main result of this section.
Theorem 3.4. Let CAG n be the complete alternating group graph with n ≥ 3.
Then the two largest eigenvalues of CAG n are λ1(CAG n) = 2
( n
3
)
and λ2(CAG n) =
1
3n(n − 2)(n − 4).
Proof. Clearly, we have λ1(CAG n) = 2
( n
3
)
because CAG n is 2
( n
3
)
-regular. We
shall prove λ2(CAG n) = 1
3n(n − 2)(n − 4) by induction on n. For n = 3, we have
λ2(CAG 3) = λ2(K3) = −1, as required. Now suppose n ≥ 4. Assume that the
result holds for n − 1, i.e., λ2(CAG n−1) = 1
3 (n − 1)(n − 3)(n − 5). Let λ be any
eigenvalue of CAG n that is not equal to 2
( n
3
)
or 1
3n(n − 2)(n − 4), and pick any
eigenvector f of CAG n corresponding to λ. Again, the vector f must sum to zero
on Xi(j) for all i, j according to Lemma 3.3. We partition the vertex set of CAG n
as An = X1(1) ∪ X2(1) ∪ · · · ∪ Xn(1). Let E1 = {{τ, σ} ∈ E(CAG n) | τ1 ⁄= σ1} and
Ei
2 = {{τ, σ} ∈ E(CAG n) | τ1 = σ1 = i} for 1 ≤ i ≤ n. Then E1 ∪ E1
2 ∪ E2
2 ∪ · · · ∪En
2
is a partition of E(CAG n). As in the proof of Theorem 3.2, we see that E1 is exactly
the set of edges of the extended alternating group graph EAGn = Cay(An, T2) with
11
T2 = {(1, k, l), (1, l, k) | 2 ≤ k < l ≤ n}, and for each i, Ei
2 is exactly the set of edges
of the induced subgraph of CAG n on Xi(1) which is also isomorphic to CAG n−1.
Then we have
λ = f T A(CAG n)f
f T f
=
2 ∑
{x,y}∈E(CAG n) f (x)f (y)∑
x∈An f (x)2
=
2 ∑
{x,y}∈E1 f (x)f (y)∑
x∈An f (x)2 +
∑ n
i=1 2 ∑
{x,y}∈Ei
2
f (x)f (y)
∑
x∈An f (x)2 .
For the ﬁrst term, since f is orthogonal to the all ones vector 1, we have
2 ∑
{x,y}∈E1 f (x)f (y)∑
x∈An f (x)2 ≤ max
g⊥1
gT A(EAGn)g
gT g = λ2(EAGn).
For the second term, we have
∑ n
i=1 2 ∑
{x,y}∈Ei
2
f (x)f (y)
∑
x∈An f (x)2 =
∑ n
i=1 2 ∑
{x,y}∈E(CAG n[Xi(1)]) f (x)f (y)
∑ n
i=1
∑
x∈Xi(1) f (x)2
≤ max
1≤i≤n
2 ∑
{x,y}∈E(CAG n[Xi(1)]) f (x)f (y)
∑
x∈Xi(1) f (x)2
≤ λ2(CAG n−1),
where the last inequality follows from the fact ∑
x∈Xi(1) f (x) = 0 for each i according
to Lemma 3.1. Combining above two bounds, we conclude that
λ ≤ λ2(EAGn)+λ2(CAG n−1) = n2−5n+5+ 1
3(n−1)(n−3)(n−5) = 1
3 n(n−2)(n−4)
by Theorem 3.2. Hence λ2(EAGn) = 1
3n(n − 2)(n − 4), as required.
At the end of this paper, we pose the following problem.
Problem 1. How to determine all distinct eigenvalues (with multiplici ties) of AGn,
EAGn and CAG n?
Acknowledgments
The authors are grateful to the anonymous referees for their u seful and constructive
comments, which have considerably improved the presentation of t his paper.
References
[1] D. Aldous,
https://www.stat.berkeley.edu/users/aldous/Research/OP/index.html.
12
[2] P. Caputo, T.M. Liggett, T. Richthammer, Proof of Aldous’ spec tral gap con-
jecture, J. Amer. Math. Soc. 23(3) (2010) 831–851.
[3] F. Cesi, Cayley graphs on the symmetric group generated by initia l reversals
have unit spectral gap, Electron. J. Combin. 16(1) (2009) #N29.
[4] F. Cesi, On the eigenvalues of Cayley graphs on the symmetric gro up generated
by a complete multipartite set of transpositions, J. Algebraic Combin . 32(2) (2010)
155–185.
[5] J.M. Chang, J.S. Yang, Panconnectivity, fault tolerant Hamiltonic ity and Hamil-
tonian connectivity in alternating group graphs, Networks 44 (200 4) 302–310.
[6] J.M. Chang, J.S. Yang, Fault-tolerant cycle-embedding in alterna ting group
graphs, Appl. Math. Comput. 197 (2008) 760–767.
[7] Y.K. Cheng, T. Lau, K.B. Wong, Cayley graph on symmetric group g enerated
by elements ﬁxing k points, Linear Algebra Appl. 471 (2015) 405–426.
[8] F. Chung, J. Tobin, The spectral gap of graphs arising from sub string reversals,
Electron. J. Combin. 23(3) (2017) #P3.4.
[9] D.M. Cvetkovi´ c, P. Rowlinson, S.K. Simi´ c, An Introduction to t he Theory of
Graph Spectra, Cambridge Univ. Press, Cambridge, 2010.
[10] P. Diaconis, M. Shahshahani, Generating a random permutation with random
transpositions, Z. Wahrscheinlichkeitstheor. Verw. Geb. 57(2) ( 1981) 159–179.
[11] L. Flatto, A.M. Odlyzko, D.B. Wales, Random shuﬄes and group re presenta-
tions, Ann. Probab. 13(1) (1985) 154–178.
[12] J. Friedman, On Cayley graphs on the symmetric group generat ed by transpo-
sitions, Combinatorica 20(4) (2000) 505–519.
[13] C.D. Godsil, G. Royle, Algebraic Graph Theory, in: Graduate Text s in Math-
ematics, vol. 207, Springer, New York, 2001.
[14] X.Y. Huang, Q.X. Huang, Automorphism group of the complete alt ernating
group graph, Appl. Math. Comput. 314 (2017) 58–64.
[15] J.S. Jwo, S. Lakshmivarahan, S.K. Dhall, A new class of interconn ection net-
works based on the alternating group, Networks 23 (1993) 315–3 26.
[16] M. Suzuki, Group Theory I, Springer, New York, 1982.
[17] J.X. Zhou, The automorphism group of the alternating group gr aph, Appl.
Math. Lett. 24 (2011) 229–231.
