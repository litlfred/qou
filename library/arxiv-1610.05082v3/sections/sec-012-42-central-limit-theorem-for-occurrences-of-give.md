---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-012-42-central-limit-theorem-for-occurrences-of-give
section_title: "Central limit theorem for occurrences of given patterns"
section_number: 4.2
pages: 19-23
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
4.2.1. Power of weighted dependency graphs. A major advantage of the theory of weighted dependency
graphs is that this structure is stable by taking powers.
Deﬁnition 4.5. Let G be an edge-weighted graph with vertex set A and weight function w; we also
consider a positive integer m. We denote by MSet ≤m(A) the subset of multisets of elements of A
with cardinality at most m. Then the m-th power Gm of G is by deﬁnition the graph with vertex-set
MSet≤m(A) and where the weight between I andJ is given by wm(I,J ) = maxi∈I,j∈Jw(i,j ). (Edges
not in the graph should be seen as edges of weight 0.)
This deﬁnition is justiﬁed by the following property, proved in [8, Section 5.3].
Proposition 4.6. Let{Ya,a∈A} be a family of random variables with a weighted dependency graph
G. Then Gm is a weighted dependency graph for the family{YI,I ∈ MSet≤m(A)}, whereYI =∏
a∈IYa.
Instead of applying this to the variables σi, we will rather work with the variables X(i,+) :=Xi =
1+σi
2 andX(i,−) = 1−Xi. Start with the following observation. We have, for all A ={i1,...,i r}⊆ Zd,
|κβ,h(Xi1,...,X ir)| =|κβ,h(Yi1,...,Y ir)|,
where on some subset B of A, Yi =X(i,+), and on A\B, Yi =X(i,−).
Mimicking the proof of Theorem 1.2, we obtain the following. Let Gs be the complete weighted
graph with vertex set Zd×{ +,−}, such that for all i,j ∈ Zd,
w′((i, +), (j, +)) =w′((i, +), (j,−)) =ε
1
2‖i−j‖1.
In other words, we ignore the sign and use the weight function w from the previous section. Then
Gs is a C-weighted dependency graph for the family {X(i,s);i∈ Zd,s ∈{ +,−}}, for some sequence
C = (Cr)r≥1.
By considering the powers of Gs and using Proposition 4.6, we obtain weighted dependency graphs
for the products of X(i,+)’s and X(i,−)’s with a bounded number of terms.
Theorem 4.7. Consider the Ising model on Zd, with inverse temperatureβ and magnetic ﬁeldh, either
forh>h 1 or (h = 0 andβ <β1) or (h = 0 andβ >β2). Let m be a ﬁxed positive integer; for multisets
I of elements of Zd×{ +,−}, we deﬁne ZI :=∏
i∈IXi. Then Gm
s is a Dm-weighted dependency graph
for the family of random variables {ZI;I∈ MSet≤m
(
Zd×{ +,−}
)
}, for some sequence Dm depending
only on m.
4.2.2. Local patterns. In this section, we prove Theorem 1.3, the CLT for the number of occurrences
of a given local pattern of spins (for example isolated + spins).
To ﬁnd a weighted dependency graph for the potential occurrences of a pattern P of size m, we
consider GP the restriction of Gm
s to the ZI’s of the form
(4.3) ZP
i =
∏
j∈D
X(i+j,s(j)).
Note that vertices of GP are canonically indexed by i∈ Zd so that we will think of GP as a graph
with vertex set Zd. The weight of the edge between i1 and i2 is then
wP(i1,i 2) = max
j1∈D,j2∈D
w(i1 +j1,i 2 +j2)≤ε
1
2 (‖i1−i2‖1−maxα,β∈D‖α−β‖1).
20 JEHANNE DOUSSE AND VALENTIN F ´ERAY
The graph GP is a D-weighted dependency graph for {Zi,i ∈ Zd}, for some sequence D depending
only onP. Indeed, it is a restriction of the weighted dependency graph given in Theorem 4.7.
We deﬁne
Sn,P :=
∑
i∈Λn
ZP
i ,
the number of occurrences of P whose position is in Λn. In the example of isolated + spins, we have
Sn,P :=
∑
i∈Λn

Xi
∏
j:‖i−j‖1=1
(1−Xj)

.
It is also easy to encode in this framework the number of + connected components of any given shape.
Let v2
n,P denote the variance of Sn,P. We have a lemma analogous to Lemma 4.3.
Lemma 4.8. As n tends to inﬁnity, the quantity
v2
n,P
|Λn| tends to v2
P :=∑
k∈Zd⟨ZP
0 ;ZP
k⟩β,h <∞.
Proof: That GP is a weighted dependency graph for the family ZP
i implies that
⟨ZP
0 ;ZP
k⟩β,h≤D2ε
1
2 (k−maxα,β∈D‖α−β‖1).
This proves that v2
P is ﬁnite as claimed.
Let ε> 0 be ﬁxed. We want to show that for n large enough,
⏐⏐⏐⏐⏐⏐
v2
n,P
|Λn|−
∑
k∈Zd
⟨ZP
0 ;ZP
k⟩β,h
⏐⏐⏐⏐⏐⏐
≤ε.
We have
v2
n,P
|Λn| = 1
|Λn|
∑
i∈Λn
∑
j∈Λn
⟨ZP
i ;ZP
j⟩β,h
= 1
|Λn|
∑
i∈Λn
∑
j∈Zd
⟨ZP
i ;ZP
j⟩β,h− 1
|Λn|
∑
i∈Λn
∑
j∈Zd\Λn
⟨ZP
i ;ZP
j⟩β,h.
By translation invariance of⟨ZP
i ;ZP
j⟩β,h, the ﬁrst sum equals∑
k∈Zd⟨ZP
0 ;ZP
k⟩β,h. Thus the only thing
left to do is to show that for n large enough, the absolute value of the second term is bounded by ε.
We cut the sum oni into two parts : the points that are far from the boundary of Λ n and those which
are not. Recall that the boundary ∂Λn consists of points j not in Λ, which have a neighbour in Λ n.
We denoteδ(i,∂ Λn) = minj∈∂Λn‖i−j‖1, which is the distance between i and ∂Λn ForR a positive
integer, let us consider the points i∈ Λn at distance more than R from the boundary of Λn. We have,
again by translation invariance
1
|Λn|
∑
i∈Λn
δ(i,∂Λn)>R
∑
j∈Zd\Λn
|⟨ZP
i ;ZP
j⟩β,h|≤
∑
k∈Zd
|k|>R
|⟨ZP
0 ;ZP
k⟩β,h|.
But the series ∑
k∈Zd|⟨ZP
0 ;ZP
k⟩β,h| is absolutely convergent so the sum above tends to 0 as R tends
to inﬁnity. Therefore, there exists some integer R0 such that
(4.4) 1
|Λn|
∑
i∈Λn
δ(i,∂Λn)>R0
∑
j∈Zd\Λn
|⟨ZP
i ;ZP
j⟩β,h|≤ ε
2.
Now let us consider the points of Λ n that are at distance at most R0 of ∂Λn. There are at most
C|∂Λn|Rd
0 such points. Therefore
1
|Λn|
∑
i∈Λn
δ(i,∂Λn)≤R0
∑
j∈Zd\Λn
|⟨ZP
i ;ZP
j⟩β,h|≤ 1
|Λn|
∑
i∈Λn
δ(i,∂Λn)≤R0
∑
k∈Zd
|⟨ZP
0 ;ZP
k⟩β,h|≤ C′|∂Λn|
|Λn| Rd
0.
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 21
But as n tends to∞, |∂Λn|
|Λn| tends to 0. Therefore for n large enough,
(4.5) 1
|Λn|
∑
i∈Λn
δ(i,∂Λn)≤R0
∑
j∈Zd\Λn
|⟨ZP
i ;ZP
j⟩β,h|≤ ε
2.
Adding (4.4) and (4.5) completes the proof. □
We are now ready to prove the central limit theorem.
Proof of Theorem 1.3: We proceed as in the proof of Theorem 4.2. We consider GP[Λn].
The number of vertices is Nn =|Λ′
n| =|Λn| and, from the discussion above, its maximal weighted
degree ∆n− 1 is bounded as follows:
∆n− 1≤ max
i∈Λn
∑
j∈Λn
ε
1
2 (‖i−j‖1−maxα,β∈D‖α−β‖1)≤ max
i∈Λn
∑
j∈Λn
CPε
1
2‖i−j‖1,
where CP is a positive constant depending only on the pattern P. Thus by the same argument as in
the proof of Theorem 4.2, ∆ n− 1≤C′
P, for some other constant C′
P.
Again we set for all n,an =
√
|Λn|. We also setv =vP as in Lemma 4.8 and we can choose s to be
any integer≥ 3.
Conditions (1) to (3) of Theorem 2.4 are satisﬁed again and the theorem is proved. □
Remark 4.9. The variance vP appearing in Theorem 1.3 might be equal to 0 for some patterns P, in
which case the central limit theorem is degenerate. If the pattern has only plus spins, the same proof
as before gives vP > 0.
4.2.3. Global patterns. In this ﬁnal section, we establish Theorem 1.4, the central limit theorem for
the number of occurrences of a global pattern of spins.
To ﬁnd a weighted dependency graph for the potential occurrences of ˜P of size m, we consider G ˜P
the restriction of Gm
s to the ZI’s of the form
(4.6) Z
˜P
{x(1),...,x(m)} =
m∏
i=1
X(x(i),s(i)).
In G ˜P, the weight of the edge between {x(1),...,x (m)} and{y(1),...,y (m)} is given by
w ˜P({x(1),...,x (m)},{y(1),...,y (m)}) = max
i,j∈{1,...,m}
w(x(i),y (j)) =ε
1
2 mini,j∈{1,...,m}‖x(i)−y(j)‖1.
Again, the graphG ˜P is a D-weighted dependency graph for{Z ˜P
{x(1),...,x(m)},{x(1),...,x (m)}⊂ Zd}, for
some sequence D depending only on P as it is a restriction of the weighted dependency graph given
in Theorem 4.7.
Now deﬁne
Sn, ˜P :=
∑
{x(1),...,x(m)}⊂Λn
Z
˜P
{x(1),...,x(m)},
the number of occurrences of ˜P in Λn. Let v2
n, ˜P denote the variance of Sn, ˜P.
Proof of Theorem 1.4: Consider the weighted dependency graph G ˜P[Λn]. Its number of vertices is
Nm
n =|Λn|m. Let us now bound its maximal weighted degree ∆ n− 1. Fix {x(1),...,x (m)}⊂ Λn. We
have
∑
{y(1),...,y(m)}⊂Λn
ε
1
2 mini,j∈{1,...,m}‖x(i)−y(j)‖1≤
∑
y(1),...,y(m)∈Λn
m∑
i=1
m∑
j=1
ε
1
2‖x(i)−y(j)‖1
≤
m∑
i=1
m|Λn|m−1 ∑
y∈Λn
ε
1
2‖x(i)−y‖1.
22 JEHANNE DOUSSE AND VALENTIN F ´ERAY
By the proof of Theorem 4.2, the last sum is bounded by a certain constant C. Thus
∆n− 1 = max
{x(1),...,x(m)}⊂Λn
∑
y(1),...,y(m)∈Λn
ε
1
2 mini,j∈{1,...,m}‖x(i)−y(j)‖1≤m2|Λn|m−1C.
We want to apply Theorem 2.4 and set an =
√
v2
n, ˜P. Condition (1) is trivial, while (2) holds for all
weighted dependency graphs whenan is the standard deviation ofXn (see [8, Lemma 4.10]). Condition
(3) is fulﬁlled since, using (1.1) and the inequality above for ∆ n,
(Nn
∆n
) 1
s ∆n
an
≤
( |Λn|m
m2|Λn|m−1C
) 1
s m2|Λn|m−1C√
A|Λn|2m−2+ε≤ cst|Λn|1/s−ε/2
and the right-hand side tends to 0 for n big enough. □
We now show a simple suﬃcient condition – the pattern consisting in positive spins only – so that
the bound (1.1) of the variance is fulﬁlled.
We start with a lemma.
Lemma 4.10. Fixm≥ 2. There exist some constants R> 0 andB >0 such that the following holds.
For any lists (x(1),...,x (m)) and (y(1),...,y (m)) such that x(1) =y(1) but no two elements in the set
{x(1),...,x (m),y (2),...,y (m)} are at distance less than R, we have
Cov
( m∏
i=1
X(x(i),+),
m∏
i=1
X(x(i),+)
)
≥B.
Proof: By deﬁnition, and using that X(x(1),+)X(y(1),+) =X2
(x(1),+) =X(x(1),+), we have
Cov
( m∏
i=1
X(x(i),+),
m∏
i=1
X(x(i),+)
)
= E
[
X(x(1),+)··· X(x(m),+)X(y(2),+)...X (y(m),+)
]
− E
[
X(x(1),+)··· X(x(m),+)
]
E
[
X(x(1),+)X(y(2),+)...X (y(m),+)
]
.
Using the expression of joint moments in terms of cumulants – see, e.g. [8, Eq. (3)] – and the bound
for cumulants of spins (Theorem 1.1), we have that there exists a constant cst m such that
⏐⏐E
[
X(x(1),+)...X (x(m),+)
]
− E
[
X(x(1),+)].... E
[
X(x(m),+)
]⏐⏐≤ cstmεR,
whenever thex(i) all lie at distance at least R from each other. The same holds for the other products
above and we get
Cov
( m∏
i=1
X(x(i),+),
m∏
i=1
X(x(i),+)
)
=
(
E
[
X(x(1),+)
]
− E
[
X(x(1),+)
]2)
· E
[
X(x(2),+)]··· .E
[
X(x(m),+)
]
E
[
X(y(2),+)]··· .E
[
X(y(m),+)
]
+ error,
where the error is uniformly bounded by cstmεR. The main term in the above equation is positive (as a
product of positive terms) and independent from thex(i) and they(i) (by translation invariance), while
the error can be made as small as wanted by making R tend to inﬁnity. This proves the lemma. □
Proposition 4.11. Let ˜P be a global pattern of size m and assume that the function s deﬁning ˜P
takes only value +1. Then there exists a constant A such that Var(Sn, ˜P)≥An2m−1.
Proof: We expand the variance as
Var(Sn, ˜P) =
∑
{x(1),...,x(m)}⊂Λn
{y(1),...,y(m)}⊂Λn
Cov(Z
˜P
{x(1),...,x(m)},Z
˜P
{y(1),...,y(m)}).
When ˜P involves only positive spins, the FKG inequality ensures that all summands are positive. Re-
stricting the sum to sets with an ordering that fulﬁlls the hypothesis of Lemma 4.10 gives a lower bound.
Therefore Var(Sn, ˜P)≥B·N1, whereN1 is the number of pairs of sets ({x(1),...,x (m)},{y(1),...,y (m)})
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 23
as in Lemma 4.10. For ﬁxed R >0, this number is clearly of order N2m−1, ﬁnishing the proof of the
proposition. □
