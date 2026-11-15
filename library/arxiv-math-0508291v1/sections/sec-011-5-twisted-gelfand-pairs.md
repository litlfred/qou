---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05"
section_id: sec-011-5-twisted-gelfand-pairs
section_title: "Twisted Gelfand Pairs"
section_number: 5
pages: 27-29
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
toc_source: outline
doc_brief: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05 — Stein’s method is used to prove limit theorems for random character ratios."
---
Let G be a ﬁnite group and H a subgroup of G. If φ is a linear charac-
ter of H such that the induced representation IndG
H(φ) is multiplicity free,
28
then (G, H, φ) is referred to as a twisted Gelfand pair (this terminology was
introduced in [Stm]).
The approach taken in this section is a bit diﬀerent than that in the
sections on ﬁnite groups and Gelfand pairs. Due both to a lack of interesting
examples which are not Gelfand pairs and to technical complications which
do not arise for ﬁnite groups or Gelfand pairs, a completely general theory is
not developed. Instead, we focus on one very interesting example: character
values of random projective representations of the symmetric group.
It
should however be noted that many of the lemmas resemble those of earlier
sections, and the calculations are organized in a way which should generalize
to other examples.
It is known (see [HH] for a friendly exposition) that the character values in
question are expressed in terms of the coeﬃcients Xλ
ρ , where λ is a strict (i.e.
all parts distinct) partition of n that parameterizes an irreducible character,
and µ is an odd (i.e.
all parts odd) partition of n that parameterizes a
conjugacy class. Throughout this section DP(n) will denote the set of strict
partitions of size n, and OP(n) will denote the set of odd partitions of size
n.
Central limit theorems for random projective representations of the sym-
metric group have been studied by Ivanov [I]. The underlying probability
measure on strict partitions chooses λ with probability
2n−l(λ)g2
λ
n!
,
where l(λ) is the number of parts of a partition λ and gλ = Xλ
(1n) is the
number of standard shifted tableaux of shape λ ([HH],[Mac]). This mea-
sure on strict partitions is known as shifted Plancherel measure, and Ivanov
proves the following result.
Theorem 5.1. ([I]) Fix i ≥1. Let λ be chosen from the shifted Plancherel
measure on strict partitions of size n. Then as n →∞, the random variable
n
2i+1
2
Xλ
(2i+1,1n−2i−1)
2i√2i+1gλ
converges in distribution to a normal random variable
with mean 0 and variance 1.
This section reﬁnes the result of Ivanov, which was proved by the method
of moments, so as to obtain an error term. In the statement of the result,
recall that zµ = Q
j≥1 jmj(µ)mj(µ)!, where mj(µ) is the number of parts of
µ of size j.
Theorem 5.2. Fix i ≥1 and let µ = (2i+1, 1n−2i−1). Choosing λ from the
shifted Plancherel measure on partitions of size n, deﬁne a random variable
W =
s
n!
zµ2n−l(µ)
Xλ
µ
gλ
.
29
Then there is a constant Ai such that for all real x0,

P(W ≤x0) −
1
√
2π
Z x0
−∞
e−x2
2 dx

 ≤Ain−1/4.
The organization of this section is as follows. Subsection 5.1 collects and
