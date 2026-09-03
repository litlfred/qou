---
doc_id: arxiv-1105.0091v1
doc_title: "E-mail: meliot@phare.normalesup.org"
section_id: sec-002-4-kerov-vershik-law-of-large-numbers
section_title: "Kerov-Vershik law of large numbers"
section_number: 4
pages: 31-36
source_pdf: 1105.0091v1.pdf
source_sha256: 7d6f72e016b25027
doc_brief: "E-mail: meliot@phare.normalesup.org — In this paper, we review the representation theory of the inﬁnite symmetric group, and we extend the works of Kerov and Vershik by proving that the irreducible"
---
In this section, we recall the results of Kerov and Vershik; although nothing
isnewhere,weshallintroducetheimportantconceptofa(random)probability
measure associated to a (random) diagram, that will later prove useful for the
analysis of the ﬂuctuations of the rows and columns, see §5.2.
4.1 Law of large numbers for the irreducible characters
Given an irreducible characterχω, we replace it on Sn by the random
function χλ, whereλ is taken according to the probability measurePn,ω. The
law of large numbers of Kerov and Vershik ensures thatχλ converges toχω:
Theorem 13. For any permutationσ∈ S∞,
χλ(σ)−→Pn,ω χω(σ),
where the long right arrow means that one has convergence in probability.
Proof. For any partitionµ, En,ω
[
Σµ
n|µ|
]
≃pµ(A−B +γE ), and
En,ω
[(Σµ
n|µ|
)2]
= En,ω
[Σµ⊔µ
n2|µ|
]
+ 1
n2|µ| En,ω[obs. of degree at most2|µ|− 1]
= (pµ(A−B +γE ))2 +O(n−1)≃ (pµ(A−B +γE ))2.
Here, we have used the estimateEn,ω[X] = O(ndegX ) mentioned at the end of
the previous paragraph, the factorization property of the symbolsΣµ in higher
degree,andthecomputationoftheexpectations En,ω[Σµ]performedattheend
of §3.1. Because of Bienaymé-Chebyshev inequality, these two estimates ensure
that Σµ
n|µ|≃χλ(µ⊔ 1n−|µ|) converges in probability towardspµ(A−B +γE ) =
χω(µ).
Again, Theorem 13 can be given an uniform ﬂavour: namely, for anyσ∈
S∞, and anyε> 0,
sup
ω∈Ω
Pn,ω[|χλ(σ)−χω(σ)|≥ ε]→n→∞ 0.
On the other hand, we shall see in Section 5 that in fact, a much stronger result
holds: for any permutationσ, the renormalized diﬀerence√n (χλ(σ)−χω(σ))
converges in law towards a centered gaussian variable. Now, let us remark that
for anyk,
En,ω
[(pk−Σk
nk
)2]
= En,ω[obs. of degree at most2k− 2]
n2k =O(n−2)→ 0.
32 Pierre-Loïc Méliot
So, Theorem 13 implies that for anyk≥ 1, and anyω∈Ω,
pk(λ)
nk −→Pn,ω pk(A−B +γE ).
We are now going to interpret this result in geometric terms, thereby proving
a law of large numbers for the ﬁrst rowsλ1,λ 2,... and the ﬁrst columns
λ′
1,λ′
2,... of a random partitionλ chosen according to a lawPn,ω.
4.2 Random measures associated to random partitions
We denote byP([−1, 1]) the set of borelian probability measures on the in-
terval [−1, 1]; this is a metrizable compact set for Skorohod’s topology of weak
convergence, see [Bil69, Chapter 1]. A distance compatible with this topology
is provided by any dense sequence of functions in the space of continuous (real-
valued) functionsC ([−1, 1]) — by Stone-Weierstrass theorem, such a sequence
(fn)n∈N exists, and we can for instance take{fn}n∈N = Q[x]. Thus,
d(m1,m 2) =
∞∑
n=0
1
2n min(1,|m1(fn)−m2(fn)|)
is a distance on P([−1, 1]) that deﬁnes the topology of weak convergence6.
Now, to any partitionλ of sizen, we associate a probability measureXλ∈
P([−1, 1]):
Xλ =
d∑
i=1
ai
n δ(
ai
n ) +
d∑
i=1
bi
n δ(
−bi
n
),
where thea’s and theb’s are the Frobenius coordinates ofλ. Notice that the
moments ofXλ are up to a shift of index the renormalized Frobenius moments
of λ:
∀k≥ 0, Xλ(xk) = pk+1(λ)
nk+1 .
If λ is random, we will then considerXλ as arandom measure, that is to
say a random point of the spaceP([−1, 1]).
If ω = ((α1,α 2,... ), (β1,β 2,... )) is a point of the Thoma simplexΩ, we
can also associate to it a probability measureXω∈ P([−1, 1]):
Xω =
∞∑
i=1
αiδ(αi) +
∞∑
i=1
βiδ(−βi) +γδ 0.
The moments ofXω are up to a shift of index the specializations of the power
sums on the formal alphabetA−B +γE:
∀k≥ 0, Xω(xk) = pk+1(A−B +γE ).
6 Here, for anyf∈ C ([−1, 1]) and anym∈ P([−1, 1]), m(f ) =
∫ 1
−1f (x)m(dx).
A central limit theorem for the characters ofS∞ and H (S∞) 33
We have seen in the previous paragraph that under the coherent system of
measures Pn,ω, pk(λ)
nk converges in probability towardspk(A−B +γE ) for any
k. Consequently,
∀k≥ 0, Xλ(xk)−→Pn,ω Xω(xk).
By linearity, we have the same result for any evaluation of the measures on a
polynomial in Q[x], and sinceQ[x] is dense inC ([−1, 1]), we conclude that:
Proposition 14. For the topology of weak convergence,
Xλ−→Pn,ω Xω.
More concretely, forany functionf∈ C ([−1, 1]) and anyε> 0, Pn,ω[|Xλ(f )−
Xω(f )|≥ ε]→ 0. In fact, these convergences are again uniform on the Thoma
simplex:
sup
ω∈Ω
Pn,ω[|Xλ(f )−Xω(f )|≥ ε]→n→∞ 0.
Finally, let us translate the Kerov-Vershik law of large numbers in terms of
the asymptotic geometry of the random partitions. From the result on random
measures, it is easy to guess that the following should be true:
Theorem 15.Takeλ randomly according to a measurePn,ω, withω = (α,β ).
∀i≥ 1, λi
n ≃ ai
n −→Pn,ω αi ; ∀j≥ 1, λ′
j
n ≃ bj
n −→Pn,ω βj.
Proof. One of the main diﬃculty when recovering the shapes of the partitions
is that we have to take account of the multiplicities of the coordinatesαi,βj of
the pointω∈Ω. Let us prove rigorously that ifα1 =α2 =··· =αm >α m+1
are the biggest coordinates of α, then the renormalized m ﬁrst parts ofλ
converge in probability to the valueα1. We ﬁxε >0, and we split the proof
in two parts.
1. First, let us prove thata1
n is smaller thanα1 + 2ε with probability going
to 1 as n goes to inﬁnity (of course, we supposeα1 < 1, this case being
obvious). We consider a test functionf +
ε that takes its values in[0, 1], is
continuous, and is equal to 1 after α1 + 2ε and to 0 before α1 +ε (see
Figure 1). On the one hand,Xω(f +
ε ) = 0, and on the other hand,
Xλ(f +
ε )≥ (α1 + 2ε) card
{
i
⏐⏐ ai
n ≥α1 + 2ε
}
.
SinceXλ(fε) converges in probability toXω(f +
ε ) = 0, this implies that the
cardinality is equal to0 for n big enough and with big probability.
34 Pierre-Loïc Méliot
f +
ε
α1αm+1
1
Fig. 1 Test functionf +
ε .
f −
ε
α1αm+1
2
Fig. 2 Test functionf−
ε .
2. Similarly, let us prove thatam
n is bigger thanα1−2ε with probability going
to 1 as n goes to inﬁnity (again, we suppose thatα1 > 0, this case being
obvious). We consider a test functionf−
ε that takes its values in[0, 1], is
continuous, and is equal to 1 after α1−ε and to 0 before α1− 2ε (see
Figure 2). Forε small enough, we may also suppose thatα1− 2ε>α m+1.
Then, Xω(f−
ε ) = mα1, whereas
Xλ(f−
ε )≤ (α1 + 2ε) card
{
i
⏐⏐ ai
n ≥α1− 2ε
}
with big probability — indeed, we already know that theai’s are smaller
than α1 + 2ε with probability almost1. Forε small enough and asn goes
to inﬁnity, this leads to the inequalitycard{i| ai
n ≥α1− 2ε}≥ m, which
is equivalent to ask thatam
n ≥α1− 2ε.
Thus, for anyε> 0, the probability of the event
α1 + 2ε≥ a1
n ≥···≥ am
n ≥α1− 2ε
goes to1 asn goes to inﬁnity, which is exactly Theorem 15 for them ﬁrst rows
of λ. Now, an induction enables us to treat the other rows, and the columns
are treated exactly the same way.
Example. Whenω = 0, the law of large numbers ensures that all the rows ofλ
are someo(n), and similarly for its columns. Actually, it is a well-known fact
that the rows and the columns have order of magnitude√n, and that there is a
limit shape for the random partitions under Plancherel measures after scaling
the Young diagrams in both directions by the factor√n (cf. [LS77,KV77]):
A central limit theorem for the characters ofS∞ and H (S∞) 35
n =5 0 0
3
Fig. 3 Random partition under the Plancherel measurePn,0 = Pn.
Hence, for this particular point ofΩ, the law of large numbers is not precise
enough; however, an accurate law of large numbers and a central limit theorem
can be proved in this case (and for other classes of measures on partitions) by
a slight modiﬁcation of the tools that we use here (see [IO02,Mél11]). Another
important example is whenω = (α,β ) with α and β geometric progressions
of same ratioq. However, these examples are better understood in the setting
of the Hecke algebras, see Section 7.
To conclude this section, let us interpret the geometric law of large numbers
in terms of properties ofω-shuﬄes. We ﬁx an integerr. Given a shuﬄeσ of
n1 +n2 +··· +m1 +m2 +··· +l cards as in §2.3, it is obvious that the maximal
sum
𝓁(iw1) +𝓁(iw2) +··· +𝓁(iwr)
of the lengths ofr disjoint increasing subwords inσ is at leastn1 +n2 +··· +nr.
Indeed, it suﬃces to consider the words
iwj = [ [n1 +··· +nj−1 + 1,n 1 +··· +nj] ],
because they stay in this order inσ.
Example. Taker = 1, n = 9 = 5 + 4 . Any shuﬄe of12345 and 6789 contains
an increasing subword of length at least5, namely,12345. However, for many
shuﬄes, one can do better: for instance,162378495 is a shuﬄe of12345 with
6789, and it contains an increasing subword of length6, namely,123789.
Thus, the r-th Greene invariant ofσ, which we shall denote byGIr(σ), is
bigger thann1 +··· +nr. Now, if the sizes of the blocks are taken according
to a multinomial law of parameter(α,β,γ ), then the law of large numbers
36 Pierre-Loïc Méliot
ensures that ni
n converges in probability toαi. Thus, with probability going
to 1, ifσ is a permutation obtained by anω-shuﬄe, then
GIr(σ)
n ≥α1 +··· +αr−ε
for anyε> 0. However, one could imagine that “many”ω-shuﬄes yield permu-
tations with greater Greene invariants (this impression may be strengthened
by the randomized block of size l ≃ nγ). The Kerov-Vershik law of large
numbers and Propositions 6 and 7 ensure that it is not the case:
Proposition 16.Letσ be a permutation of sizen chosen randomly according
to Qn,ω. Asn goes to inﬁnity,
GIr(σ)
n −→Qn,ω α1 +··· +αr.
Of course, the same holds if one replaces the increasing subwords by the de-
creasing subwords and theα’s by theβ’s.
Proof. Because of Proposition 6, the distribution ofGIr(σ) under Qn,ω is the
same as the distribution ofλ1 +··· +λr under Pn,ω. Then, it suﬃces to apply
Theorem 15.
Hence,ω-shuﬄes do not create bigger increasing subwords than those given
by the sizes of the blocks. In Section 5, we are going to prove a central limit
theorem that will improve this result. Hence, assuming that theαi’s are all
distinct, up to order√n (and notn), the asymptotic distribution ofGIr(σ) is
the same as the asymptotic distribution of the sizen1 +··· +nr of ther ﬁrst
blocks of theω-shuﬄe, that is to say
n (α1 +··· +αr) +√n
√
(α1 +··· +αr)(1−α1−···− αr)N (0, 1) +o(√n)
withN (0, 1) a standard gaussian variable.
