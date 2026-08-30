---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-011-4-weighted-dependency-graphs-and-central-limit-t
section_title: "Weighted dependency graphs and central limit theorems"
section_number: 4
pages: 16-19
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
We will now use the bounds on cumulants obtained in the previous section to show that the family
of random variables {σi : i∈ Zd} has a weighted dependency graph, and we will use this fact to
deduce central limit theorems. We consider any of the regimes studied in the previous section: very
high temperature, or very low temperature with + boundary condition, or strong magnetic ﬁeld with
any boundary condition. To have uniform notation, we omit from now on the notation of the boundary
condition in low temperature.
4.1. Weighted dependency graph for the σi’s and central limit theorem for the magneti-
zation.
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 17
4.1.1. The weighted dependency graph. We start by proving Theorem 1.2, which gives a weighted
dependency graph for{σi :i∈ Zd}.
Proof of Theorem 1.2: LetB ={i1,...,i r} be a multiset of elements of Zd and consider the induced
subgraph G[B]. Then the maximum weightM(G[B]) of a spanning tree in G[B] satisﬁes
M(G[B]) =ε
𝓁′
T (B)
2 .
Thus by Proposition 2.2,
(4.1) ε𝓁T (B)≤M (G[B])≤ε
𝓁T (B)
2 .
By Proposition 5.2 of [8], it is suﬃcient to show that
⏐⏐⏐⏐⏐κβ,h
(∏
α∈B1
σα,...,
∏
α∈Bk
σα
)⏐⏐⏐⏐⏐≤DrM(G[B]),
for some sequence D = (Dr)r≥1, where B1,...,B k are the vertex-set of the connected components of
G1[B], which is the graph induced by edges of weight 1 of G on B.
The verticesi andj are connected in G1 if and only if i =j, because of the deﬁnition of the weights
we in G. Moreover the random variables σi are equal to +1 or −1, thus
σj
i =
{
σi if j odd,
1 if j even.
Therefore it is suﬃcient to prove that for any set B′ of distinct i1,...,i r,
(4.2) |κβ,h (σi1,...,σ ir)|≤ DrM(G[B′]).
But by Theorem 1.1,
|κβ,h (σi1,...,σ ir)|≤ Drε𝓁T (B′),
for some sequence D depending only onr. Thus using (4.1), Equation (4.2) is proved, which completes
the proof of the theorem. □
Remark 4.1. For alli∈ Zd, let us deﬁne Xi = σi+1
2 . Thus Xi = 1 (resp. 0) if and only if σi = 1 (resp.
−1). In the remainder of this paper, it will sometimes be more convenient to consider the Xi’s rather
than the σi’s. Since κβ,h(Xi1,...,X ir) = 1
2rκβ,h(σ1,...,σ r) for r≥ 2, the weighted graph G deﬁned
in Theorem 1.2 is also a C-weighted dependency graph for the family{Xi :i∈ Zd}, for some sequence
C = (Cr)r≥1.
4.1.2. The central limit theorem. We now use the weighted dependency graph from last section to
obtain the central limit theorem for the magnetization.
We consider the Ising model on Zd, with inverse temperature β and magnetic ﬁeld h. For any
positive integer n, we deﬁne Λn := [−n,n ]d the d-dimensional cube centred at 0 of side 2 n. We deﬁne
the magnetization
Sn :=
∑
i∈Λn
σi,
and let v2
n denote the variance of Sn. Let us further deﬁne the covariance
⟨σi;σj⟩β,h :=⟨σiσj⟩β,h−⟨σi⟩β,h⟨σj⟩β,h.
We now reprove the following well-known central limit for the magnetization Sn (for an early
reference, see [25]). This serves as a warm up, to illustrate the method of dependency graphs; moreover,
some computation made in this proof will be re-used in the next section, when studying patterns.
Theorem 4.2. Consider the Ising model on Zd, with inverse temperatureβ and magnetic ﬁeld h, such
that either h>h 1(d) or (h = 0; β <β1(d)) or (h = 0; β >β2(d)). Then, for some v,
Sn− E(Sn)√
|Λn|
d
−−−−→
n→∞
N (0,v 2).
18 JEHANNE DOUSSE AND VALENTIN F ´ERAY
Moreoverv2 > 0 so the Gaussian law is non-degenerate.
We start by a lemma of [6] on the asymptotics of the variance of Sn.
Lemma 4.3. [6, Lemma V.7.1] The limit
v2 := lim
n→∞
v2
n
|Λn|
exists as an extended real valued number and
v2 =
∑
i∈Zd
⟨σ0;σi⟩β,h.
But by Theorem 1.1, in the regimes we consider, the cumulants (so in particular the covariance) are
exponentially small, so the sum is absolutely convergent and we actually have the stronger statement:
Corollary 4.4. Suppose that either h>h 1 or (h = 0 and β <β1) or (h = 0 and β >β2). The limit
v2 := lim
n→∞
v2
n
|Λn| =
∑
i∈Zd
⟨σ0;σi⟩β,h
is ﬁnite.
Proof of Theorem 4.2: We will use Theorem 2.4. Let G be the weighted dependency graph deﬁned
in Theorem 1.2. Then for all n,G[Λn] is a C-weighted dependency graph for{σi;i∈ Λn}. The number
of vertices of G[Λn] is
Nn =|Λn| = (2n + 1)d,
and its maximal weighted degree is
∆n− 1 = max
i∈Λn
∑
j∈Λn
ε
‖i−j‖1
2 .
There are 2d(d+y−1
d−1
)
points at distancey of 0 in Zd. Indeed such a point has coordinates (y1,...,y d)
such that|y1| +··· +|yd| =y. There are
(d+y−1
d−1
)
choices for the values of|y1|,..., |yd|, and eachyi can
be either positive or negative, which multiplies the number of choices by 2 d. Thus there are at most
2d(d+y−1
d−1
)
points at distance y of any point x in Λn, and
∆n− 1≤
2dn∑
y=0
ε
y
2 2d
(d +y− 1
d− 1
)
≤C,
for some constant C because the inﬁnite series is absolutely convergent.
We now have to ﬁnd a sequence (an) and integerss andv such that conditions (1)-(3) of Theorem 2.4
are satisﬁed. We set for all n, an =
√
|Λn| = (2n + 1)
d
2, v=
√∑
i∈Zd⟨σ0;σi⟩β,h as in Lemma 4.3 and
we can choose s to be any integer≥ 3.
Now condition (1) is satisﬁed because of Lemma 4.3, as
v2
n
|Λn| = v2
n
a2n
−−−−→
n→∞
v2.
Condition (2) is also satisﬁed as a2
n = (2n + 1)d =Nn.
Finally, for some constant C′,
(Nn
∆n
) 1
s ∆n
an
≤C′ (2n + 1)
d
s
(2n + 1)
d
2
,
and the right-hand side tends to 0 as n tends to inﬁnity for s≥ 3. So (3) is satisﬁed too.
The central limit theorem is proved.
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 19
Moreover, whatever the values ofβ andh are, the spin at 0 is not constant, thus⟨σ0,σ 0⟩β,h > 0. On
the other hand, because of the GKS inequalities [13, 17], for all i∈ Zd,⟨σ0;σi⟩β,h≥ 0 (see eg. [10]).
Therefore,
v2 =⟨σ0,σ 0⟩β,h +
∑
i∈Zd\{0}
⟨σ0;σi⟩β,h > 0,
which ends the proof of the theorem. □
