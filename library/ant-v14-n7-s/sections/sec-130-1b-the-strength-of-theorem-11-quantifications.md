---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-130-1b-the-strength-of-theorem-11-quantifications
section_title: "1B. The strength of Theorem 1.1: quantifications"
section_number: null
pages: 247-249
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
which holds for a range of integers r, to assess its strength for H near the lower-bound threshold that
yields a nontrivial bound for |S(N, H)|, we must compute which value of r produces maximum savings.
For example, in Burgess’s original result, if H = q1/4+κ the bound (1-1) with parameter value r yields the
upper bound |S(N, H)| ≪Hq−δ where δ = (4κr −1)/(4r2). Computing the maximum of δ with respect
to r, we see that by choosing r to be the nearest integer to 1/(2κ) we may obtain the best value δ ≈κ2.
We perform an analogous optimization of our result, summarized in two corollaries.
Corollary 1.3. For each n ≥2 and r ≥1, Theorem 1.1 with the parameters n,r provides a nontrivial
upper bound |S(F; N, H)| = on,r,1,D(∥H∥) for all H = (H, . . . , H) with H = qβ with β in the range
1
2 −
2−1
22(n+1) < β ≤1
2 + 1
42,
(1-6)
in which 2 = 2n,r = ⌊(r −1)/(n −1)⌋. This range includes a nonempty interval of β < 1
2 as soon as
r ≥2n −1, so that 2 = 2n,r > 1. In particular, this range always requires β > βn with
βn := 1
2 −
1
2(n+1).
(1-7)
1914
Lillian B. Pierce and Junyan Xu
For H = qβn+κ for small κ, we obtain a nontrivial bound ∥H∥q−δn with savings approximately of size
δn ≈(n + 1)2
4(n −1)κ2
as κ →0.
Remark. In the approximate value of the savings δn stated above (and similarly in Corollary 1.4 below),
the symbol ≈is used to denote that certain approximations were used in the derivation, such as (i) letting
the value θ1 = ⌊(r −1)/(n −1)⌋be approximated by r/(n −1), which is reasonable, for ﬁxed n, for the
very large values of r = r(κ) that are chosen when κ →0; and (ii) considering the limiting case κ →0 in
order to isolate the main term in computations. More details are given in Section 7A.
The threshold βn deﬁned in (1-7) has appeared in n-dimensional Burgess bounds that were previously
proved in very special cases, such as [Burgess 1967b; 1968; Davenport and Lewis 1963] (see Section 1C2
for an overview, including the stronger results [Chang 2008; 2009; Bourgain and Chang 2010; Heath-
Brown 2016]).
In full generality, our main result Theorem 1.1 is in fact stronger than Corollary 1.3, as it can allow
one or more of the lengths Hi to be smaller than qβn, as long as other Hi are commensurably larger.
We cannot let Hi vary in a completely uncontrolled fashion, since our savings comes from the smallest
parameter Hmin; thus we assume that H is proportionate, in the sense that Hmin ≥∥H∥c0/n for some
constant 0 < c0 ≤1. The relation (1-9) below shows that if we take c0 smaller so that Hmin becomes a
decreasing proportion of ∥H∥, for our Burgess bound to be nontrivial the geometric mean ∥H∥1/n is
forced into an ever shorter range near q1/2.
Corollary 1.4. For each n ≥2 and r ≥1, Theorem 1.1 with the parameters n,r provides a nontrivial
upper bound |S(F; N, H)| = on,r,1,D(∥H∥) for all H = (H1, . . . , Hn) with HminHmax < q1+1/22 as
long as Hmin ≥∥H∥c0/n for some 0 < c0 ≤1 and ∥H∥1/n = qβ with β in the range
1
2 −
c02−1
22(n+c0) < β ≤1
2 + 1
42,
(1-8)
in which 2 = 2n,r = ⌊(r −1)/(n −1)⌋. This range includes a nonempty interval of β < 1
2 as soon as
r ≥(1/c0 + 1)(n −1) + 1, so that c02 > 1. In particular this range always requires ∥H∥1/n = qβ with
β > βn,c0 = 1
2 −
c0
2(n+c0) ≥1
2 −
1
2(n+1).
(1-9)
Alternatively, we can state that Theorem 1.1 obtains a nontrivial upper bound if
∥H∥Hmin ≫qn/2+κ
for some small κ. As κ →0 we obtain a nontrivial bound ∥H∥q−δn with
δn ≈(n + c0)2
4(n −1) κ2.
Burgess bounds for short character sums evaluated at forms
1915
