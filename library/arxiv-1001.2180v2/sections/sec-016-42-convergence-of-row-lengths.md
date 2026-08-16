---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-016-42-convergence-of-row-lengths
section_title: "Convergence of row lengths"
section_number: 4.2
pages: 15-16
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
of the sequence ((1 − q), (1 − q)q, (1 − q)q2, . . .). Indeed,
∞∑
i=1
(1 − q)k q(i−1)k = (1 − q)k
1 − qk .
In this paragraph, we show that the convergence of power sums implies the convergence of the sequence.
This corresponds to the end of the proof of Theorem 1.
The main idea is to consider, given a Young diagram λ of size n, the probability measure Xλ deﬁned
by
Xλ =
d∑
i=1
(a∗
i (λ)/n) δ(a∗
i (λ)/n) + (b∗
i (λ)/n) δ(−b∗
i (λ)/n).
The k-th moment of Xλ is exactly pk+1(λ)/nk+1. So, thanks Lemma
12, under q-Plancherel measure, the
moments of Xλ, which can be seen as random variables, converge in probabil ity towards the moments of
the measure
X∞;q =
∞∑
i=1
(1 − q)qi−1 δ(1−q)qi−1 .
Lemma 14. As usual, we consider a sequence of random diagrams λn ∈ Yn taken with q-Plancherel
measure. At any point x ⁄= (1 − q) qi−1, one has convergence in probability of the repartition funct ions,
that is to say: ∑
y≤x
ny∈Aλ+Bλ
|y| − → Mn,q
∑
(1−q)qi−1≤x
(1 − q)qi−1.
Proof. In the following, we consider λ ↦→Xλ as a measure-valued random variable Xn,q; its law is by
deﬁnition the image of Mn,q by λ ↦→Xλ. The set M ([−1, 1]) of probability measures on [−1, 1], where
Xn,q takes its values, is included in the dual of C ([−1, 1]) and is compact and metrizable with respect to
the ∗-weak topology 1. Indeed, if (fn)n∈ /C6
is a sequence of continuous functions dense in C ([−1, 1]), then
d(m1, m2) =
∑
n∈ /C6
1
2n max(1, |m1(fn) − m2(fn)|)
is a distance compatible with the topology of M ([−1, 1]). We choose {fn}n∈ /C6
= /C9 [X] (dense by Stone-
Weierstrass theorem), thus the convergence of moments impl ies that Xn,q converges in probability in
(M ([−1, 1]), d) towards X∞;q.
But, for Radon measures on the real line, the weak convergenc e Xn,q ⇀ X ∞;q is equivalent to the
convergence of repartition functions FXn,q (x) → FX∞;q (x) at points x ∈ [−1, 1] where FX∞;q is continuous
— it is a part of the Portmanteau theorem ([ Bil69, Chapter1]). □
1It is a particular case of the Prohorov theorem: if E is a separable and complete metric space (in other words, a po lish
space), then the same holds for the set of probability measur es M (E), see [ Bil69, Chapter 1]. As a consequence, convergence
in probability makes sense for random probability measures on a closed subset of the real line.
16 V ALENTIN FÉRAY AND PIERRE-LOÏC MÉLIOT
End of proof of Theorem 1. Now, let us take x = 1 − q + η with η > 0 suﬃciently small. We also ﬁx
1 − q > ε > 0. Note that FX∞;q = 1 on an open set containing x. Consequently, for n big enough and
outside a set of arbitrarily small probability, all rows of λ are smaller than nx, because
FXλ (x) =
∑
y≤x
ny∈A+B
|y| ≥ FX∞;q (x) − ε = 1 − ε > q,
and this could not be if a row were bigger than n(1 − q + η). Indeed, we would then have
FXλ (1) ≥ FXn,q (x) + 1 − q + η > 1 + η > 1.
Hence, for n big enough, a∗
1(λ)/n is smaller than x outside a set of arbitrary small probability. Now, if
x′ = 1 − q − η, then FX∞;q = q on an open set containing x′, and therefore, for n big enough and outside
a set of arbitrarily small probability, some rows of λ are bigger than nx′; otherwise, we would have
FXλ (1) = FXλ (x′) ≤ FX∞;q (x′) + ε = q + ε < 1.
We conclude that for n big enough and outside a set of arbitrarily small probabilit y, the rescaled ﬁrst
column a∗
1(λ)/n is between x′ and x. Consequently, a∗
1(λ)/n converges in probability towards 1 − q, and
the same argument holds for the following rows (with an induc tion on the index i of the row). Of course,
a∗
i (λ)/n − λi/n = O(1/n), so we have proved Theorem
1. □
Remark 3. Unfortunately, our estimates are not strong enough to prove almost surely convergence.
Let us look at the ﬁrst column of a random diagram under the q-Plancherel measure. If we take x = 0
in Lemma 14, then we see that ∑ d
i=1 b∗
i (λ)/n goes to 0 in probability: so, the column lengths are o(n).
Nevertheless, we can not determine their precise order of ma gnitude.
Remark 4. The same proof works for any measure for which we can compute e xpectation of character
values as soon as (the following condition implies the conve rgence of variance of power sums towards 0
in Lemma
12):
/BX [Σ k,k] = /BX [Σ k]2 + o(n2k).
This is similar to the result obtained by Biane for balanced d iagrams in [ Bia01].
