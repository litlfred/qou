---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-004-21-the-ising-model
section_title: "The Ising model"
section_number: 2.1
pages: 4-5
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
in the literature. We mention Markov chains (see [29, 9, 8] and references therein), patterns in random
permutations (see [2, 31] for global patterns and [12, 2, 30] for local patterns) and arc conﬁgurations in
random set-partitions (CLTs for the number of arcs of size 1, which is a local pattern, and the number
of crossings, which is a global pattern, were given in [3]). Note that Markov chains are (discrete)
one-dimensional Markov random ﬁelds, while the random permutation model is a non-Markovian two-
dimensional model (when considering patterns, we think of permutations as permutation matrices).
Finding such CLT results in Markov random ﬁelds of dimension two or more, and in particular in the
Ising model, is therefore a natural problem.
We ﬁrst prove a CLT for local patterns. Let Sn,P denote the number of occurrences of a given local
patternP in Λn.
Theorem 1.3. Consider the Ising model on Zd, with inverse temperatureβ and magnetic ﬁeld h, such
that either h>h 1(d) or (h = 0; β <β1(d)) or (h = 0; β >β2(d)). Let P be a local pattern. Then
Sn,P− E(Sn,P)√
|Λn|
d
−−−−→
n→∞
N (0,v 2
P).
Similarly, if Sn, ˜P denotes the number of occurrences of a global pattern ˜P in Λn, we have the
following result.
Theorem 1.4. Consider the Ising model on Zd, with inverse temperatureβ and magnetic ﬁeld h, such
that either h > h1(d) or (h = 0; β < β1(d)) or (h = 0; β > β2(d)). Let ˜P be a global pattern of size
m. We assume that, for some positive constants A and η
(1.1) Var( Sn, ˜P)≥An2m−2+η.
Then
Sn, ˜P− E(Sn, ˜P)√
Var(Sn, ˜P)
d
−−−−→
n→∞
N (0, 1).
We do not have in general an estimate for the variance Var( Sn, ˜P). However, when the pattern
consists in positive spins only, we can prove that (1.1) is satisﬁed (with η = 1) — see Proposition 4.11
below. The reverse inequality Var(Sn, ˜P)≤Bn2m−1 is always fulﬁlled (see the proof of Theorem 1.4).
We ﬁnish this introduction with a comparison with other methods. Standard methods to get CLT
in random ﬁelds are the use of mixing techniques [24] or FKG inequalities [25, 26]. It seems that the
CLT for local patterns can be easily obtained with these methods. Indeed, in an exponentially mixing
ﬁeld such as the Ising model, if we denote ZP
i the characteristic function of the occurrence of P in
position i (see (4.3)), then the ﬁeld (ZP
i )i∈Zd is also exponentially mixing and we can use the criterion
given by Neaderhouser [24, Section 3]. CLT for functions of neighbouring spins are also accessible with
methods based on FKG inequalities, see [26] for a general result in this direction. On the contrary,
for global patterns, we do not know how to adapt these methods to prove Theorem 1.4. Indeed, if
we denote Z ˜P
{x1,...,xm} the characteristic function of the occurrence of ˜P in position{x1,...,x m} (see
(4.6)), then (Z ˜P
{x1,...,xm}) is not a mixing ﬁeld anymore.
The theory of weighted dependency graphs enables to deal with these diﬀerent kinds of patterns in
a uniform way. In principle it would also be feasible to mix local and global conditions (as in vincular
patterns for permutations [14]); besides the complexity of notation, a major diﬃculty is then to get
general estimates for the variance.
WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL 5
