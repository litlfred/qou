---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-002-12-results
section_title: "Results"
section_number: 1.2
pages: 1-4
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
is the number of boxes of the diagram. In particular, the exis tence of a limit shape implies that the
probability that a random diagram has a long row or column (of length ≫ √n) tends to 0. Therefore the
same method can not be used directly to study the asymptotic b ehavior of non-balanced Young diagrams,
such as diagrams under the q-Plancherel measure.
This measure is a natural q-analog of the Plancherel measure. It was ﬁrst introduced by Kerov in
[Ker92] via a deformed hook walk algorithm. The asymptotic behavior of d iagrams under this measure
has then been considered by a Strahov [ Str08]. By generalizing Kerov’s method of a diﬀerential growth
model [ Ker96], he has obtained a limit shape for a diagram under the q-Plancherel measure with a
parameter q depending of the size of the diagrams.
We have mentioned above that, if we ﬁx q, there is no hope in ﬁnding a limit shape of diagrams
rescaled by 1/√n as the ﬁrst rows or columns are not of order Θ( √n) . In this paper, we give the precise
behavior (ﬁrst- and second-order asymptotics) of the lengt h of these ﬁrst rows or columns (either rows
or columns, depending on the value of q, are of order Θ( n)). This is a good description of the shape of
the diagram as a ﬁnite number of rows or columns contain an arb itrarily big proportion of the boxes of
the Young diagram (outside a set of small probability). Our m ethod is close to the one of the papers
[IO02, Śni06]. The ﬁrst-order asymptotics actually follow from general results of harmonic analysis on
Key words and phrases. Asymptotics of Young diagrams, Hecke algebras, deformatio n of Plancherel measure.
1
2 V ALENTIN FÉRAY AND PIERRE-LOÏC MÉLIOT
the inﬁnite symmetric group ([ Tho64, KV81, KOO98, KOV04]); our computations are quite independent
of these results, and they allow to tackle with the same forma lism the second-order asymptotics.
A natural question arising after this result on q-Plancherel measure is the following: can our method be
adapted to measures for which typical diagrams have rows of intermediate scaling Θ( nα) with 1/2 < α < 1:
intermediate between the balanced case ( α = 1/2) and the q-Plancherel case ( α = 1)? The answer is yes
and, as examples, we look at measures associated to Schur-We yl duality. In these cases, the method gives
results on the global shape of the diagram, but not the precis e behavior of the ﬁrst rows and columns.
Indeed, as for balanced diagrams, the asymptotic behavior o f the lengths of the ﬁrst rows and columns is
not a direct consequence of the existence of the limit shape. For instance, in the case of the Plancherel
measure, a consequent amount of extra work is needed: see [ BDJ99, BDJ00, Oko00, BOO00, Joh01].
1.2. Results.
1.2.1. First rows of a random Young diagram under the q-Plancherel measure. Let us suppose q < 1.
In this paper, we prove a law of large numbers and a central lim it theorem for the vector containing
the lengths of the ﬁrst k rows of a random diagram under the q-Plancherel measure Mn,q. Note that
Theorem 1 implies that the ﬁrst k rows contain asymptotically (1 − qk) × n boxes, therefore describing
the length of theses rows gives a good description of the diag ram. As Mn,q−1(λ′) = Mn,q(λ) (this follows
from Deﬁnition 1), in the case q > 1, our result gives the asymptotic behavior of the columns, wh ich are,
in this case, the relevant quantities.
Theorem 1 (First order asymptotics) . Suppose q < 1. If λ = (λ1 ≥ λ2 ≥ · · · ) denotes a Young diagram
of size n under the q-Plancherel measure ( cf. ﬁgure
1), then
∀i ≥ 1, λi
n − →Mn,q (1 − q) qi−1;
where the arrow →Mn,q means convergence in probability.
Figure 1. A random Young diagram λ = (101 , 51, 28, 8, 7, 3, 1, 1) of size 200 under the
1/2-Plancherel measure.
Theorem 2 (Second order asymptotics) . Under the same hypothesis, if Yn,q,i is the rescaled deviation
√n
(λi
n − (1 − q) qi−1
)
,
then we have convergence of the ﬁnite-dimensional laws of th e random process (Yn,q,i)i≥1 towards those
of a gaussian process (Yq,i)i≥1 with:
/BX [Yq,i] = 0 ; /BX [Y 2
q,i] = (1 − q) qi−1 − (1 − q)2 q2(i−1) ; cov( Yq,i, Yq,j ) = −(1 − q)2 qi+j−2.
In particular, two diﬀerent coordinates Yq,i and Yq,j are negatively correlated. For the readers not
accustomed to the topology of convergence in law, let us give a more concrete version of Theorem 2.
Given ε > 0 and for any positive real numbers x1, . . . , xr, Theorem 2 ensures that, for n big enough:⏐
⏐
⏐
⏐
⏐
/C8
[
∀i ∈ [ [1, r] ], |λi − (1 − q) qi−1 n| ≤ xi
√n
]
− 1√
(2π)r det Q
∫ x1
−x1
· · ·
∫ xr
−xr
e−
tXQ−1 X
2 dX
⏐
⏐
⏐
⏐
⏐ ≤ ε,
ASYMPTOTICS OF q-PLANCHEREL MEASURES 3
where Q is the symmetric matrix with coeﬃcients Qij = δij (1 − q) qi−1 − (1 − q)2 qi+j−2. This matrix is
positive deﬁnite because of the Hadamard rule (in each colum n, the diagonal coeﬃcient is positive and
strictly bigger than the sum of the absolute values of the oth er coordinates).
1.2.2. Other measures. As mentioned in paragraph 1.1, our method is quite general. We can establish
limit shape theorems with diﬀerent rescalings. As an exampl e, in paragraph 6, we introduce some natural
probability measures on Young diagrams. We obtain the follo wing result:
Theorem 3. Let (λn)n be the sequence of random Young diagrams described in paragra ph 6.1. We
assume N ∼ c · nα with α < 1/2.
Then, for each ε, η > 0, there exists an integer n0 such that, for each n ≥ n0, the border of the diagram
λn is, after rescaling and with probability greater than 1 − ε, contained in the hatched area:
× n1− α
× nα
c
c− 1
c− 1η
cη
Figure 2. Limit shape of a rescaled random diagram under the Schur-Wey l measure of
parameters c > 0 and α < 1/2.
Unfortunately, one can not use this to give the precise behav ior of the ﬁrst row of the diagram. The
only result we have is the following (which is a consequence o f Proposition 23):
Proposition 4. Let λn be the sequence of random diagrams described in paragraph 6.1. Let us assume
that N ∼ c nα with α < 1/2. For any ε > 0, one has λ1 = o(n1−α+ε) in probability.
1.2.3. Longest increasing subsequence. It is well-known that the length of the ﬁrst row of a Young diag ram
of size n under Plancherel measure has the same distribution as the le ngth of the longest increasing
subsequence of a random permutation of size n (under the uniform distribution). Indeed, the shape of
the tableaux obtained by the Robinson-Schensted bijection deﬁnes a map
Sn − → {λ ⊢ n},
which sends the length of the longest increasing subsequenc e on the length of the ﬁrst row of λ. The
image of the uniform distribution on Sn is the Plancherel measure on Young diagrams of size n, and this
explains the aforementioned result.
Our results on the q-Plancherel measure can also be interpreted in the context o f longest increasing
subsequences. Indeed, E. Strahov [ Str08] has noticed that the q-Plancherel measure is the image by the
map above of the probability measure deﬁned by
∀ σ, /C8 [σ] = Z · qimaj(σ),
4 V ALENTIN FÉRAY AND PIERRE-LOÏC MÉLIOT
where imaj(σ), called major index, is the sum of the integers i between 1 and n−1 such that σ(i) > σ (i+1)
and Z = 1/{n!}q is the normalization constant such that the probabilities s um to 1. So Theorems 1 and
2 imply the following:
Theorem 5. Let q be a real in ]0, 1[ and n an integer. Consider the distribution on permutations such
that the probability of picking a permutation σ is proportional to qimaj(σ). The length ℓ(σ) of the longest
increasing subsequence of a permutation under this distribut ion is equivalent in probability to n(1 − q).
Moreover, the rescaled deviation (ℓ(σ) − n(1 − q))/√n converges in law towards a centered normal law of
variance q(1 − q).
As mentioned in subsection 6.1, the measure considered in section 6 is the image by the RSK algorithm
of the uniform distribution on words of length n with letters from 1 to N . So, Proposition 4 implies:
Corollary 6. Fix c > 0 and 0 < α < 1/2. Let ℓ be the length of the longest non-decreasing subsequence
of a random word with n letters between 1 and c · ⌊nα⌋. When n tends to inﬁnity, one has in probability:
ℓ = o(n1−α+ε).
1.3. T ools. Since we are looking at measures on diagrams of a given size, i rreducible character values on
a given permutation can be seen as random variables. Moreove r, in our context, their expectations are
easy to compute. Therefore we would like to express other ran dom variables, linked directly to the shape
of the diagrams in terms of the character value. This can be do ne thanks to Kerov’s and Olshanski’s
theory of polynomial functions on the set of Young diagrams ( see [ KO94]). Note that the guideline of
the proof is roughly the same as in Kerov’s proof of the centra l limit theorem for Young diagram under
Plancherel’s measure (see [ IO02]).
In this article, we shall use the power sums of Frobenius coor dinates. With an adequate gradation on
the functions on Young diagrams, we shall easily ﬁnd their as ymptotic behavior under the q-Plancherel
measure. Going back to the behavior of the ﬁrst rows is then a t echnical step.
