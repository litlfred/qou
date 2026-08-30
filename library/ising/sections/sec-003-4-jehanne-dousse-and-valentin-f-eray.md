---
doc_id: ising
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-003-4-jehanne-dousse-and-valentin-f-eray
section_title: "JEHANNE DOUSSE AND VALENTIN F ´ERAY"
section_number: 4
pages: 4-6
source_pdf: ising.pdf
source_sha256: 9f84d7209731d299
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
with vertex set A is a family of random variables {Ya,a ∈ A} such that, for subsets B,B′,B′′⊂ A,
{Ya,a ∈ B} and{Ya,a ∈ B′} are independent conditionally on {Ya,a ∈ B′′} as soon as every path
going from B to B′ in G goes through B′′; this is also sometimes called global Markov property [23].
Informally, in a Markov random ﬁeld, a variable interacts directly only with its neighbours. We
can thus expect that the dependency between variables is weaker when their distance in the graph G
increases. Indeed, such variables only interact through all variables lying between them in the graph.
In other terms, we expect to have a weighted dependency graph which is complete (because there is
no reason to have unconditionally independent variables), but whose weights decrease with the graph
distance. This was observed in the case of Markov chains, which are one-dimensional Markov random
ﬁelds, in [10, Section 10]. The present paper gives such a statement for the d-dimensional Ising model.
In both cases, weights decrease exponentially with the graph distance.
1.3. Central limit theorems. Central limit theorems (CLTs) play a key role in probability theory
and have also been a subject of interest in the study of the Ising model. We refer to the second
edition of Georgii’s classical book [14, Bibliographic Notes on Section 8.2, p.469] for an overview of
the diﬀerent methods used to obtain such results. The goal of this paper is to prove new central limit
theorems, using the weighted dependency graph technique. To this end, we shall use the following
normality criterion, which is a slightly modiﬁed version of the main theorem in [10].
Theorem 1.6. Suppose that, for each n,{Yn,i, 1≤i≤Nn} is a family of random variables with ﬁnite
moments deﬁned on the same probability space. Let C = (Cr)r≥1 be a ﬁxed sequence that does not
depend on n.
Assume that, for each n, one has a C-weighted dependency graph Gn for{Yn,i, 1≤ j≤ Nn} and
denote ∆n− 1 its maximal weighted degree.
LetXn =∑Nn
i=1Yn,i and v2
n =Var (Xn). Assume that there exists a sequence (an), an integer s≥ 3
and a real number v such that
(1) v2
n
a2n
−−−−→
n→∞
v2, (2) for all n, a2
n≤C2Nn∆n, (3)
(Nn
∆n
) 1
s ∆n
an
−−−−→
n→∞
0.
Then in distribution,
Xn− E(Xn)
an
d
−−−−→
n→∞
N (0,v 2).
Remark 1.7. The proof of Theorem 1.6 is almost identical to the proof of the normality criterion in
[10, Section 4.3] replacing σn byan. Indeed, as noticed in [10, Section 4.3], in the special case Ψ ≡ 1
to which we restrict ourselves in this article, the quantities Rn and Qn deﬁned there can be replaced
respectively by Nn (the number of vertices) and ∆n (the maximal weighted degree plus one).
Recall from the previous section that spins, and therefore products of spins, admit a weighted
dependency graph. The normality criterion above can thus be used to ﬁnd CLTs for polynomials of
spins in a growing box Λ n := [−n,n ]d. To illustrate this, we consider number of occurrences of two
kinds of spin patterns: local and global patterns.
We deﬁne a local pattern P to be a pair ( D, s), where D is a ﬁnite subset of Zd containing 0
and s is a function D −→ {+,−}. The cardinality of D is called the size of the pattern P. An
example of local pattern is a positive spin surrounded by negative ones. In that case the subset is
D ={j∈ Zd :‖j‖1≤ 1}, while the sign function is given by s(0) = + and s(j) =− for all j∈D\{ 0}.
This pattern has size 2d + 1. An occurrence of a local patternP = (D, s) is a set{(i +j, s(j)) :j∈D} ,
where i∈ Zd is the position of the occurrence.
While in local patterns we consider spins that are at a ﬁxed distance from one another, in global
patterns they can be as far as we want, as long as they have a certain global shape. Formally, we deﬁne
a global pattern ˜P of size m to be a pair (O, s), whereO = (≤1,..., ≤d) is a d-tuple of total orders
over{1,...,m }, and s is a function{1,...,m }−→{ +,−}. An occurrence of ˜P in a spin conﬁguration
ω is a set{x(1),...,x (m)} ofm elements of Zd such that there exists some ordering (x(1),...,x (m)) of
these elements such that
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 5
(1) for all i∈{ 1,...,m }, σx(i)(ω) = s(i),
(2) for all i,j ∈{ 1,...,m }, for all k∈{ 1,...d }, x(i)
k ≤x(j)
k if and only if i≤k j.
For example, ifd = 2,≤1,≤2 are both the natural ordering and s(i) = + for alli, then an occurrence of
the global pattern (O, s) is a set ofm positive spins such that each of them is located to the North-East
of the previous one.
CLTs for local and global patterns in other structures than the Ising model have attracted attention
in the literature. We mention Markov chains (see [34, 12, 10] and references therein), patterns in ran-
dom permutations (see [2, 21] for global patterns and [16, 2, 7] for local patterns) and arc conﬁgurations
in random set-partitions (CLTs for the number of arcs of size 1, which is a local pattern, and the num-
ber of crossings, which is a global pattern, were given in [4]). Note that Markov chains are (discrete)
one-dimensional Markov random ﬁelds, while the random permutation model is a non-Markovian two-
dimensional model (when considering patterns, we think of permutations as permutation matrices).
Finding such CLT results in Markov random ﬁelds of dimension two or more, and in particular in the
Ising model, is therefore a natural problem.
We ﬁrst prove a CLT for local patterns. Let Sn,P denote the number of occurrences of a given local
patternP in Λn.
Theorem 1.8. Consider the Ising model on Zd, with inverse temperatureβ and magnetic ﬁeld h, such
that (β,h )∈R(β1,β 2,h 1). Let P be a local pattern. Then
Sn,P− E(Sn,P)√
|Λn|
d
−−−−→
n→∞
N (0,v 2
P),
where
v2
P = lim
n→∞
Var(Sn,P)
|Λn| .
Similarly, if Sn, ˜P denotes the number of occurrences of a global pattern ˜P in Λn, we have the
following result.
Theorem 1.9. Consider the Ising model on Zd, with inverse temperatureβ and magnetic ﬁeld h, such
that (β,h )∈ R(β1,β 2,h 1). Let ˜P be a global pattern of size m. We assume that, for some positive
constantsA and η
(1.2) Var( Sn, ˜P)≥A|Λn|2m−2+η.
Then
Sn, ˜P− E(Sn, ˜P)√
Var(Sn, ˜P)
d
−−−−→
n→∞
N (0, 1).
We do not have in general an estimate for the variance Var( Sn, ˜P). However, when the pattern
consists of positive spins only, we can prove that (1.2) is satisﬁed (with η = 1) — see Proposition 4.10
below. The reverse inequality Var(Sn, ˜P)≤B|Λn|2m−1 is always fulﬁlled (see the proof of Theorem 1.9).
We ﬁnish this introduction with a comparison with other methods. Standard methods to get CLT
in random ﬁelds are mixing properties [29] or FKG inequalities [30, 31]. It seems that the CLT for
local patterns can be easily obtained with these methods. Indeed, in an exponentially mixing ﬁeld
such as the Ising model, if we denote ZP
i the characteristic function of the occurrence of P in position
i (see (4.3)), then the ﬁeld (ZP
i )i∈Zd is also exponentially mixing and we can use the criterion given by
Neaderhouser [29, Section 3]. CLT for functions of neighbouring spins are also accessible with methods
based on FKG inequalities, see [31] for a general result in this direction.
On the contrary, we do not know how to adapt these methods to global patterns. Obtaining a CLT
for subword occurrences in Markov chains (the analogue problem in one-dimensional Markov ﬁeld) is
already a diﬃcult problem, see [3, 12] for some history on this problem. The technique of dependency
graphs gives access to CLTs for such global patterns, as shown in Theorem 1.9.
