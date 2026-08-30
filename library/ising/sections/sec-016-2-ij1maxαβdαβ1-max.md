---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-016-2-ij1maxαβdαβ1-max
section_title: "(‖i−j‖1−maxα,β∈D‖α−β‖1)≤ max"
section_number: 2
pages: 21-22
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
i∈Λn
∑
j∈Λn
CPε
1
2‖i−j‖1,
where CP is a positive constant depending only on the pattern P. Thus by the same argument as in
the proof of Theorem 4.1, ∆ n− 1≤C′
P, for some other constant C′
P.
Again we set for all n,an =
√
|Λn|. We also setv =vP as in Lemma 4.7 and we can choose s to be
any integer≥ 3.
Conditions (1) to (3) of Theorem 1.6 are satisﬁed again and the theorem is proved. □
Remark 4.8. The variance vP appearing in Theorem 1.8 might be equal to 0 for some patterns P, in
which case the central limit theorem is degenerate. If the pattern has only plus spins, the same proof
as before gives vP > 0.
4.2.3. Global patterns. In this ﬁnal section, we establish Theorem 1.9, the central limit theorem for
the number of occurrences of a global pattern of spins.
To ﬁnd a weighted dependency graph for the potential occurrences of ˜P of size m, we consider G ˜P,
the restriction of Gm
s to the ZI’s of the form
(4.7) Z
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
in Theorem 4.6.
Now deﬁne
Sn, ˜P :=
∑
{x(1),...,x(m)}⊂Λn
Z
˜P
{x(1),...,x(m)},
the number of occurrences of ˜P in Λn. Let v2
n, ˜P denote the variance of Sn, ˜P.
Proof of Theorem 1.9: Consider the weighted dependency graph G ˜P[Λn]. Its number of vertices is
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
By the proof of Theorem 4.1, the last sum is bounded by a certain constant C. Thus
∆n− 1 = max
{x(1),...,x(m)}⊂Λn
∑
y(1),...,y(m)∈Λn
ε
1
2 mini,j∈{1,...,m}‖x(i)−y(j)‖1≤m2|Λn|m−1C.
We want to apply Theorem 1.6 and set an =
√
v2
n, ˜P. Condition (1) is trivial, while (2) holds for
all weighted dependency graphs when an is the standard deviation of Xn (see [10, Lemma 4.10]).
