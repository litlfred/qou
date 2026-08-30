---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-014-18-jehanne-dousse-and-valentin-f-eray
section_title: "JEHANNE DOUSSE AND VALENTIN F ´ERAY"
section_number: 18
pages: 18-20
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
Lemma 4.2. [8, Lemma V.7.1] The limit
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
Corollary 4.3. Suppose that (β,h )∈R(β1,β 2,h 1). The limit
v2 := lim
n→∞
v2
n
|Λn| =
∑
i∈Zd
⟨σ0;σi⟩β,h
is ﬁnite.
Proof of Theorem 4.1: We will use Theorem 1.6. Let G be the weighted dependency graph deﬁned
in Theorem 1.5. Then for all n,G[Λn] is a C-weighted dependency graph for{σi;i∈ Λn}. The number
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
We now have to ﬁnd a sequence (an) and integerss andv such that conditions (1)-(3) of Theorem 1.6
are satisﬁed. We set for all n, an =
√
|Λn| = (2n + 1)
d
2, v=
√∑
i∈Zd⟨σ0;σi⟩β,h as in Lemma 4.2 and
we can choose s to be any integer≥ 3.
Now condition (1) is satisﬁed because of Lemma 4.2, as
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
Moreover, whatever the values ofβ andh are, the spin at 0 is not constant, thus⟨σ0,σ 0⟩β,h > 0. On
the other hand, because of the GKS inequalities [17, 22], for all i∈ Zd,⟨σ0;σi⟩β,h≥ 0 (see e.g. [13]).
Therefore,
v2 =⟨σ0,σ 0⟩β,h +
∑
i∈Zd\{0}
⟨σ0;σi⟩β,h > 0,
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 19
which ends the proof of the theorem. □
4.2. Central limit theorem for occurrences of given patterns.
4.2.1. Power of weighted dependency graphs. A major advantage of the theory of weighted dependency
graphs is that this structure is stable by taking powers.
Deﬁnition 4.4. Let G be an edge-weighted graph with vertex set A and weight function w; we also
consider a positive integer m. We denote by MSet ≤m(A) the set of multisets of elements of A with
cardinality at most m. Then the m-th power Gm of G is by deﬁnition the graph with vertex-set
MSet≤m(A) and where the weight between I and J is given by wm(I,J ) = max i∈I,j∈Jw(i,j ). As
usual, edges not in the graph should be seen as edges of weight 0.
This deﬁnition is justiﬁed by the following property, proved in [10, Section 5.3].
Proposition 4.5. Let{Ya,a ∈ A} be a family of random variables with a C-weighted dependency
graph G. Then Gm is a D-weighted dependency graph for the family {YI,I ∈ MSet≤m(A)}, where
YI =∏
a∈IYa, and D depends only on m and C.
Instead of applying this to the variables σi, we will rather work with the variables X(i,+) :=Xi =
1+σi
2 and X(i,−) = 1−Xi. Start with the following observation. For all A ={(i1,s 1),..., (ir,sr)}⊆
Zd×{ +,−}, we have, for r≥ 2,
⏐⏐κβ,h(X(i1,s1),...,X (ir,sr))
⏐⏐ = 1
2r|κβ,h(σi1,...,σ ir)|,
Mimicking the proof of Theorem 1.5, we obtain the following. Let Gs be the complete weighted graph
with vertex set Zd×{ +,−}, such that for all i,j ∈ Zd,
w′((i, +), (j, +)) =w′((i, +), (j,−)) =ε
1
2‖i−j‖1.
In other words, we ignore the sign and use the weight function w from the previous section. Then
Gs is a C-weighted dependency graph for the family {X(i,s);i∈ Zd,s ∈{ +,−}}, for some sequence
C = (Cr)r≥1.
By considering the powers of Gs and using Proposition 4.5, we obtain weighted dependency graphs
for the products of X(i,+)’s and X(i,−)’s with a bounded number of terms.
Theorem 4.6. Consider the Ising model on Zd, with inverse temperature β and magnetic ﬁeld h,
such that (β,h ) ∈ R(β1,β 2,h 1). Let m be a ﬁxed positive integer; for multisets I of elements of
Zd×{ +,−}, we deﬁne ZI :=∏
i∈IXi. Then Gm
s is a Dm-weighted dependency graph for the family
of random variables {ZI;I∈ MSet≤m
(
Zd×{ +,−}
)
}, for some sequence Dm depending only on m.
4.2.2. Local patterns. In this section, we prove Theorem 1.8, that is the CLT for the number of occur-
rences of a given local pattern of spins (for example, the number of isolated + spins).
To ﬁnd a weighted dependency graph for the potential occurrences of a pattern P = (D, s) of size
m, we consider GP, the restriction of Gm
s to the ZI’s of the form
(4.3) ZP
i =
∏
j∈D
X(i+j,s(j)).
Note that vertices of GP are canonically indexed by i∈ Zd so that we will think of GP as a graph
with vertex set Zd. The weight of the edge between i1 and i2 is then
(4.4) wP(i1,i 2) = max
j1∈D,j2∈D
w(i1 +j1,i 2 +j2)≤ε
1
2 (‖i1−i2‖1−maxα,β∈D‖α−β‖1).
The graph GP is a D-weighted dependency graph for {Zi,i ∈ Zd}, for some sequence D depending
only onP. Indeed, it is a restriction of the weighted dependency graph given in Theorem 4.6.
We deﬁne
Sn,P :=
∑
i∈Λn
ZP
i ,
