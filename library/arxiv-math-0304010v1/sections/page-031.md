---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-031
section_title: "Page 31"
section_number: null
pages: 31-31
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Proposition 6.3. For any partition ρ, we have
ηρ =
Y
k≥2
Hmk(ρ)(ηk) + . . .
(6.6)
where dots denote a remainder term with deg1( · ) < 0.
In particular, ηρ does not depend, up to terms of negative degree, from the value
of m1(ρ).
Proof. Examine ﬁrst the particular case ρ = (km), where k = 2, 3, . . . and m =
1, 2, . . . . Then our claim means that
η(km) = Hm(ηk) + . . . .
Taking σ = (km) in Proposition 4.12 we get
p#
(km) · p#
k = p#
(km+1) + k m p#
(km−1,1k) + · · · = p#
(km+1) + k m p#
(km−1) · (p#
1 )k + . . .
for any m ≥1, where dots mean lower degree terms. This is equivalent to
η(km) · ηk = η(km+1) + m η(km−1) + . . . ,
m ≥1,
(6.7)
where dots mean terms of negative degree. Within these terms, (6.7) coincides with
the recurrence relation (6.3), which proves (6.6).
The case of an arbitrary ρ is reduced to the particular case ρ = (km) using
Corollary 4.13.
□
The next claim is a well–known general result. It justiﬁes the moment method,
which is a convenient tool for checking convergence in distribution.
Proposition 6.4. Let a(n) be a sequence of real random variables. Assume that
a(n) have ﬁnite moments of any order, and the moments converge, as n →∞, to
the respective moments of a random variable a. Finally, assume that a is uniquely
determined by its moments, which holds, e.g., if the characteristic function of a is
analytic.
Then a(n)
d
−→a. Moreover, this claim also holds when the variables in question
take vector values, i.e., when each a(n), as well as a, is a system of random variables.
Sketch of proof. Let P (n) denote the distribution of the random variable a(n) and
P be the distribution of a. We have to prove that P (n) weakly converges to P as
n →∞. The assumption on the moments implies that {P (n)} is a tight family of
probability measures on R. So, it suﬃces to prove that any partial weak limit P ′ of
the sequence {P (n)} coincides with P. Using again the condition on the moments
one can show that the moments of P ′ exist and coincide with the limits of the
respective moments of {P (n)}. Hence, these are exactly the moments of P. By the
uniqueness assumption, P ′ = P.
□
For another proof, see Feller [Fe, ch. VIII, §6, Example b].
Proof of Theorem 6.1. We must prove that
{η(n)
k }k≥2
d
−→{ξk}k≥2 ,
n →∞.
31
