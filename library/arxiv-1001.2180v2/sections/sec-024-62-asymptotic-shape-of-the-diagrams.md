---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-024-62-asymptotic-shape-of-the-diagrams
section_title: "Asymptotic shape of the diagrams"
section_number: 6.2
pages: 24-26
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
on Young diagrams of size n. Here we are interested in the asymptotic shape of typical di agrams when
n tends to inﬁnity. That means, as the measure we introduced al so depends on an other parameter N ,
that we have to choose a value of N for each n. The case where the parameter N is equivalent of an
expression of the kind 1/c · nα with α ≥ 1/2 has already been solved by P. Biane [ Bia01, paragraph 3.1].
So we will look at the case α < 1/2.
Using the formula for expectation of normalized character v alues of the previous paragraph, one has:
(13) /BX [Σρ] = n↓|ρ| · N ℓ(ρ)−|ρ| ∼ c|ρ|−ℓ(ρ)n|ρ|+αℓ(ρ)−α|ρ|.
As in section 4, the ﬁrst step is to show that the power sums have the same asym ptotic behavior. Lemma
11 is true in this context, but not strong enough to obtain such a result. Unfortunately, with the gradation
we give in section 3, it is not possible to have a stronger upper bound. Thus one ha s to introduce another
gradation on O.
6.2.1. Gradations on O. Let us deﬁne (this may not be an integer, but it does not matter ):
degα(pρ) = |ρ| + αℓ(ρ) − α|ρ|.
As in the case α = 0 , the expression of Σk in terms of power sums (Proposition 7) gives us the degree
and the top homogeneous component of Σρ.
Lemma 21. For any ρ ∈ Y , one has:
Σρ = pρ + terms of lower degree .
Proof. It is enough to prove this for ρ = (k). Note that the α-degree can be written as:
degα(pλ) = (1 − 2α)|λ| + α(|λ| + ℓ(λ)).
(1) The ﬁrst term is a positive multiple (recall that α < 1/2) of the usual gradation, so if pλ appears
with a non-zero coeﬃcient in Σk, one has |λ| ≤ k, with equality if and only if λ = (k).
(2) The second term is a non-negative multiple of 2 deg1/2(λ) = |λ| + ℓ(λ). An easy consequence of
Proposition 7 is that all pλ appearing in Σk fulﬁll the condition |λ| + ℓ(λ) ≤ k + 1. Note that
we do not have the same necessary condition of equality as bef ore: in fact, deg1/2 is a classical
gradation of O (see [ IO02]), for which the top homogeneous component of Σρ is not pρ.
Finally, Σρ has degree |ρ| + αℓ(ρ) − α|ρ|, and its top homogeneous component for the new gradation is
pρ. □
6.2.2. Convergence of rescaled power sums and concentration of cha racters. Using equation ( 13), one has
the following analog of Lemma 11 (the gradation has been chosen for this purpose):
Lemma 22. For any x ∈ O, one has: /BX [x] = O(ndegα(x)).
Now, we have all the tools to prove the convergence of rescale d powers sums:
Proposition 23. Let (Nn)n≥1 be a sequence of positive integers such that Nn ∼ c · nα for some α < 1/2.
Under the measure associated with the action of the symmetric groups on the spaces (/BV
Nn )⊗n, one has
the following convergence in probability:
pk
nk+α−αk → ck−1.
Proof. Equation ( 13), Lemma 21 and Lemma 22 imply that:
/BX [pρ] ∼ cρ−ℓ(ρ)n|ρ|+αℓ(ρ)−α|ρ|.
The result follows thanks to Bienaymé-Chebyshev inequalit y as in the case α = 0. □
ASYMPTOTICS OF q-PLANCHEREL MEASURES 25
Corollary 24 (Concentration of characters) . Under the same assumptions, in probability,
Σρ
n|ρ|+αℓ(ρ)−α|ρ| → c|ρ|−ℓ(ρ).
6.2.3. Consequences on the shape of diagrams. To deduce some results on the shape of diagrams from
the convergence of the quantities pk/(nk+α−αk), one has to interpret them as the moments of some
measure-valued random variables. Therefore we deﬁne for a Y oung diagram λ the measure:
Xλ,α =
d∑
i=1
(a∗
i (λ)/n1−α)
δ(a∗
i (λ)/n1−α)
nα + (b∗
i (λ)/n1−α)
δ(−b∗
i (λ)/n1−α)
nα .
With this deﬁnition, Proposition 23 can be read as the convergence in probability of the moments o f
this random-valued measure towards the sequence (1, c, c2, . . .), which is obviously the sequence of the
moments of the measure δc (the Dirac mass at c). Since the probability measure δc is characterized by
its moments, this implies the convergence in law Xλ,α → δc in probability in the space of probability
measures M (/CA ).
Now, the negative part of Xλ,α is in fact negligible. Indeed, since ℓ(λ) ≤ N with probability 1, the
total weight of
d∑
i=1
(b∗
i (λ)/n1−α)
δ(−b∗
i (λ)/n1−α)
nα
is bounded from above and with probability 1 by:
N∑
i=1
N
n = N 2
n ≃ c−2 n2α−1 → 0
As a consequence, one can replace Xλ,α by its positive part ∑ d
i=1(a∗
i (λ)/n1−α)
δ(a∗
i (λ)/n1−α)
nα , and even by
the simpler probability measure
Yλ,α =
N∑
i=1
(λi/n1−α) δλi/n1−α
nα =
N∑
i=1
λi
n δλi/n1−α;
this random measure converges in probability towards δc in M (/CA ).
We ﬁx some positive real numbers θ, η and ε, and we consider a continuous function f : /CA → [0; 1]
such that f (x) = 0 outside the interval [c(1 − η/2), c(1 + η/2)], and f (c) = 1 . Then, for n big enough and
with probability greater than 1 − ε,
1 − θ = f (c) − θ ≤
N∑
i=1
λi
n f
( λi
n1−α
)
≤ f (c) + θ = 1 + θ
because of the convergence in law Yλ,α → δc. The sum involved in this estimate is bounded from above
by ∑
{i | λi/n1−α∈[c(1−η/2),c(1+η/2)]}
λi
n , and therefore by
c(1 + η/2)
nα card
{
i
⏐
⏐
⏐
⏐
λi
n1−α ∈ [c(1 − η/2), c(1 + η/2)]
}
.
As a consequence, the number of rows λi such that c(1 − η/2) ≤ λi/n1−η ≤ c(1 + η/2) is bigger than
1 − θ
c(1 + η/2) nα ≥ (1 − θ)(1 − η/2)
c nα ≥ 1 − η
c nα
for θ small enough. As by the very deﬁnition of our measure, our ran dom diagrams can not have columns
of length bigger than N , the proof of Theorem 3 is over.
26 V ALENTIN FÉRAY AND PIERRE-LOÏC MÉLIOT
Remark 6. The vector space (/BV
N )⊗n is also a representation of the unitary group UN and, using Schur-
Weyl duality, its isotypic components under the action of UN are the same as under the action of Sn. As
a consequence, the results of article [ CŚ09] can be used to study the asymptotic shape of the diagram. It
turns out that, in the case α < 1/2, this approach gives ﬁner results than ours. Nevertheless, as they are
two independent parameters, the space (/BV
N )⊗n remains a good example to show that our method works
with any intermediate decay of character values between O(1) and O(√n−|ρ|+ℓ(ρ)).
