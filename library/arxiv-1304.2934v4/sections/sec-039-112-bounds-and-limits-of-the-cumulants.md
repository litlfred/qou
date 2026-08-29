---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-039-112-bounds-and-limits-of-the-cumulants
section_title: "Bounds and limits of the cumulants"
section_number: 11.2
pages: 93-96
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
11.2.1. The dependency graph for random character values. If k =|µ|, we are interested in
the non-commutative random variables
Σµ,n = ∑
A∈A(n,k)
ρµ(A)∈ CS(n).
Again, to control the cumulants, we shall exhibit a dependency graph for the families
of random variables{ρµ(A)}A∈A(n,k).
Due to the multiplicative form of Equation (52), if I and J have disjoint subsets of
[n], the subalgebras CS(I) and CS(J) are tensor independent (here, S(I) denotes the
group of permutations ofI, canonically included inS(n)). Therefore, one can associate
to{ρµ(A)}A∈A(n,k) the dependency graph B deﬁned by:
• its vertex set is A(n, k);
• there is an edge between A and A′ if|A∩ A′|≥ 1.
The graph B is obviously regular with degree strictly smaller than k2 n↓k−1. On the
other hand, all joint moments of the family (ρµ(A))A∈A(n,k) are normalized characters
of single permutations and hence bounded by 1 in absolute value. So one can once
again apply Theorem 9.7 and we get:
Proposition 11.10. Fix a partition µ of size k. For any r≤ 1, one has
⏐⏐κ(r)(Σµ)
⏐⏐≤ 2r−1rr−2 n↓k (k2n↓k−1)r−1;
⏐⏐κ(r)(X(n)
ρµ )
⏐⏐≤ rr−2
(2k2
n
)r−1
.
Remark 11.11. Using Theorem 9.11, one can also obtain a bound for joint cumulants of
the X(n)
ρµ , namely,
⏐⏐⏐κ
(
X(n)
ρµ1, . . . ,X(n)
ρµr
)⏐⏐⏐≤ k1··· kr
(
r· max
1≤i≤r
ki
)r−2
( 2
n
)r−1
for integer partitions µ1, . . . ,µr of sizes k1, . . . ,kr. In the following, we shall focus
on the case of simple random variables X(n)
ρµ , though most results also hold in the
multi-dimensional setting. Actually, in order to compute the asymptotics of the ﬁrst
cumulants of Xρµ, it will be a bit clearer to manipulate joint cumulants of variables
Σµ1, . . . ,Σµr with arbitrary integer partitions.
94 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
11.2.2. Limits of the second and third cumulants. Because of Lemma 11.9 and Proposition
11.10, for any ﬁxed integer partitions,
κ
(
X(n)
ρµ1, . . . ,X(n)
ρµr
)
n1−r≃ κ
(
Σµ1, . . . ,Σµr
)
nk1+···+kr−(r−1)
converges to a constant. Let us compute this limit when r = 2 or 3; we use the same
reasoning as in Section 10.3.2.
As κ is invariant by simultaneous conjugacy of its arguments, the summand in
Equation (53) depends only on the graph G = GA associated to the collection A =
(A1, . . . ,Ar), and we shall denote it κ(G). We ﬁx partitions µ1, . . . ,µr of respective
sizes k1, . . . ,kr, and write
κ(Σµ1, . . . ,Σµr ) = ∑
G
κ(G) NG.
Here, as in Section 10, NG denotes the number of list A of arrangements with associ-
ated graph G.
When r = 2, we have to look for graphs G on vertex set Vk = [ k1]⊔ [k2] with 1-
contraction connected and at least k1 + k2− 1 connected components, because these
are the ones that will give a contribution for the coefﬁcient of nk1+k2−1. For i∈ [𝓁(µ1)]
and j∈ [𝓁(µ2)], denote
(µ1⋊ ⋉µ2)(i, j) = ( µ1\ µ1
i )⊔ (µ2\ µ2
j )⊔{ µ1
i + µ2
j− 1}.
This is the cycle type of a permutation ρµ1(A1) ρµ2(A2), where GA is the graph with
one edge joining an element of A1 in the cycle of length µ1
i with an element of A2 in the
cycle of length µ2
j . These graphs are the only ones involved in our computation, and
they yield
κ(G) = p(µ1⋊ ⋉µ2)(i,j)(ω)− pµ1⊔µ2(ω),
where for a partition µ we denote pµ(ω) the product ∏
𝓁(µ)
i=1 pµi (ω). So,
Proposition 11.12. For any partitions µ and ν, the limit of n κ(X(n)
ρµ , X(n)
ρν ) is
𝓁(µ)
∑
i=1
𝓁(ν)
∑
j=1
µi νj
(
p(µ⋊ ⋉ν)(i,j)(ω)− pµ⊔ν(ω)
)
.
In particular, for cycles µ = (k) and ν = (l),
lim
n→∞
n κ
(
X(n)
k , X(n)
l
)
= kl
(
pk+l−1(ω)− pk,l(ω)
)
.
On the other hand, if µ = ν, then the limit of n κ(2)(X(n)
ρµ ) is
(pµ(ω))2
∑
1≤i,j≤𝓁(µ)
µi µj
( p(µiµj−1)(ω)
pµi (ω) pµj(ω)− 1
)
.
When r = 3, we look for graphs G on vertex set Vk = [ k1]⊔ [k2]⊔ [k3] with 1-
contraction connected and at least k1 + k2 + k3− 2 connected components. They are of
three kinds:
MOD-φ CONVERGENCE, I 95
(1) One cycle in ρµ2(A2) is connected to two cycles in ρµ1(A1) and ρµ3(A3), but not
by the same point in this cycle ofρµ2(A2). This gives for ρµ1(A1) ρµ2(A2) ρµ3(A3)
a permutation of cycle type
(µ1⋊ ⋉µ2⋊ ⋉µ3)(i, j, k) = ( µ1\ µ1
i )⊔ (µ2\ µ2
j )⊔ (µ3\ µ3
k)⊔{ µ1
i + µ2
j + µ3
k− 2};
and the corresponding cumulant is
κ(G) = pµ1⊔µ2⊔µ3(ω) + p(µ1⋊ ⋉µ2⋊ ⋉µ3)(i,j,k)(ω)
− p((µ1⋊ ⋉µ2)(i,j))⊔µ3(ω)− p((µ2⋊ ⋉µ3)(j,k))⊔µ1(ω).
In this description, one can permute cyclically the indices 1, 2, 3, and this gives
3 different graphs.
(2) One cycle in ρµ2(A2) is connected to two cycles in ρµ1(A1) and ρµ3(A3), and
by the same point in this cycle of ρµ2(A2). In other words, there is an identity
a1
s = a2
t = a3
u. This gives again for ρµ1(A1) ρµ2(A2) ρµ3(A3) a permutation of
cycle type (µ1 ⋊ ⋉µ2 ⋊ ⋉µ3)(i, j, k), but the corresponding cumulant takes now
the form
κ(G) = 2 pµ1⊔µ2⊔µ3(ω) + p(µ1⋊ ⋉µ2⋊ ⋉µ3)(i,j,k)(ω)− p((µ1⋊ ⋉µ2)(i,j))⊔µ3(ω)
− p((µ2⋊ ⋉µ3)(j,k))⊔µ1(ω)− p((µ1⋊ ⋉µ3)(i,k))⊔µ2(ω).
Here, there is no need to permute cyclically the indices in the enumeration for
NG.
(3) Two distinct cycles in ρµ2(A2) are connected to a cycle of ρµ1(A1) and to a cycle
of ρµ3(A3), which gives a permutation of cycle type
(µ1⋊ ⋉µ2⋊ ⋉µ3)(i, j; k, l)
= ( µ1\ µ1
i )⊔ (µ2\{ µ2
j , µ2
k})⊔ (µ3\ µ3
l )⊔{ µ1
i + µ2
j− 1, µ2
k + µ3
l− 1}.
The cumulant corresponding to this last case is
κ(G) = pµ1⊔µ2⊔µ3(ω) + p(µ1⋊ ⋉µ2⋊ ⋉µ3)(i,j;k,l)(ω)
− p((µ1⋊ ⋉µ2)(i,j))⊔µ3(ω)− p((µ2⋊ ⋉µ3)(k,l))⊔µ1(ω),
and again one can permute cyclically the indices 1, 2, 3 to get 3 different graphs.
Consequently:
Proposition 11.13. For any partitions µ, ν and δ, the limit of n2 κ(X(n)
ρµ , X(n)
ρν , X(n)
ρδ ) is
∑
Z/3Z
(𝓁(µ)
∑
i=1
𝓁(ν)
∑
j=1
𝓁(δ)
∑
k=1
µi νj (νj− 1) δk
( pµ⊔ν⊔δ(ω)+p(µ⋊ ⋉ν⋊ ⋉δ)(i,j,k)(ω)
−p((µ⋊ ⋉ν)(i,j))⊔δ(ω)−p((ν⋊ ⋉δ)(j,k))⊔µ(ω)
)
+
𝓁(µ)
∑
i=1
𝓁(ν)
∑
(j⁄=k)=1
𝓁(δ)
∑
l=1
µi νj νk δl
( pµ⊔ν⊔δ(ω)+p(µ⋊ ⋉ν⋊ ⋉δ)(i,j;k,l)(ω)
−p((µ⋊ ⋉ν)(i,j))⊔δ(ω)−p((ν⋊ ⋉δ)(k,l))⊔µ(ω)
)


+
𝓁(µ)
∑
i=1
𝓁(ν)
∑
j=1
𝓁(δ)
∑
k=1
µi νj δk
(2 pµ⊔ν⊔δ(ω)+p(µ⋊ ⋉ν⋊ ⋉δ)(i,j,k)(ω)−p((µ⋊ ⋉ν)(i,j))⊔δ(ω)
−p((ν⋊ ⋉δ)(j,k))⊔µ(ω)−p((µ⋊ ⋉δ)(i,k))⊔ν(ω)
)
,
where ∑Z/3Z means that one permutes cyclically the partitions µ, ν, δ.
96 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
In particular, for cycles µ = ( k), ν = ( l) and δ = ( m), limn→∞ n2 κ(X(n)
k , X(n)
l , X(n)
m ) is
equal to
klm
(
(k + l + m− 1) pk,l,m(ω) + (k + l + m− 2) pk+l+m−2(ω)
− (k + l− 1) pk+l−1,m(ω)− (l + m− 1) pl+m−1,k(ω)− (l + m− 1) pk+m−1,l(ω)
)
.
One recovers for k = l = m the values of σ2 and L announced in Theorem 11.4. On the
other hand, if µ = ν = δ, then the limit of
n2 κ(3)(X(n)
ρµ )
(pµ(ω))3 is
∑
1≤i,j,k≤𝓁(µ)
3 µi µ2
j µk
(
1 +
pµi+µj+µk−2(ω)
pµi (ω) pµj(ω) pµk (ω)−
pµi+µj−1(ω)
pµi (ω) pµj(ω)−
pµj+µk−1(ω)
pµj(ω) pµk (ω)
)
+ ∑
1≤i,j⁄=k,l≤𝓁(µ)
3 µi µj µk µl
(
1−
pµi+µj−1(ω)
pµi (ω) pµj(ω)
)(
1− pµk+µl−1(ω)
pµk (ω) pµl (ω)
)
+ ∑
1≤i,j,k≤𝓁(µ)
µi µj µk
(
3
pµi+µj−1(ω)
pµi (ω) pµj(ω)− 2
pµi+µj+µk−2(ω)
pµi (ω) pµj(ω) pµk (ω)− 1
)
.
