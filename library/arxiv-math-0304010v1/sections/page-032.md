---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-032
section_title: "Page 32"
section_number: null
pages: 32-32
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
By Proposition 6.4, it suﬃces to check that
⟨
Y
k≥2
ηmk
k
⟩n →⟨
Y
k≥2
ξmk
k
⟩Gauss ,
n →∞,
(6.8)
for any ﬁnite collection {mk}k≥2 of nonnegative integers, where the brackets
⟨· ⟩Gauss mean expectation with respect to the standard Gaussian measure. The
uniqueness hypothesis of Proposition 6.4 is clearly satisﬁed.
The limit relations (6.8) are equivalent to the following ones:
⟨
Y
k≥2
Hmk(ηk)⟩n →
Y
k≥2
⟨Hmk(ξk)⟩Gauss
for any ﬁnite collection {mk ∈Z+}.
If all the numbers mk are equal to 0 then the expressions in both sides equal
1, and there is nothing to prove.
So, let us assume that some of the mk’s are
nontrivial. Then the right–hand side vanishes, because, for a standard Gaussian ξ,
⟨Hm(ξ)⟩Gauss =
1
√
2π
Z
R
Hm(x)e−x2/2dx = 0,
m = 1, 2, . . .,
by the orthogonal property of the polynomials Hm.
Let us examine the left–hand side. Set ρ = (Q
k≥2 kmk). By Proposition 6.2,
Y
k≥2
Hmk(ηk) = ηρ + a “remainder term” of strictly negative degree.
By our assumption, ρ is nonempty. Moreover, m1(ρ) = 0, so that ρ̸ = (1r). By
Proposition 5.1, ⟨ηρ⟩n ≡0. Finally, by Proposition 6.2,
⟨the “remainder term”⟩n = O(n−1/2).
(6.9)
This concludes the proof.
□
Theorem 6.1 can be generalized as follows:
Theorem 6.5. Let ρ range over the set of all partitions. We have
{η(n)
ρ }
d
−→{
Y
k≥2
Hmk(ρ)(ξk)} ,
n →∞,
where, as before, ξ2, ξ3, . . . are independent standard Gaussians.
Proof. The above argument shows that any mixed moment of the random variables
from the left–hand side converges, as n →∞, to the respective moment of the
random variables from the right–hand side. However, we cannot use the moment
method, because a polynomial in Gaussian variables does not necessarily satisfy
the uniqueness assumption mentioned in Proposition 6.4. For this reason we argue
in a diﬀerent way.
Assume that
{a(n)
1 , a(n)
2 , . . .}
d
−→{a1, a2, . . .} ,
n →∞,
32
